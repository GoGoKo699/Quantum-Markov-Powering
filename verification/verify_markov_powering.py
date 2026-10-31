#!/usr/bin/env python3
"""Deterministic finite-dimensional checks for clean Markov powering.

These checks validate circuit phases, access-model details and small examples.
They do not prove the asymptotic index-erasure lower bound.
Only NumPy and the Python standard library are required.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import time
import traceback
from pathlib import Path

import numpy as np


TOL = 2e-11
SEED = 20261031


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def close(actual, expected, message, atol=TOL):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    require(error <= atol, f"{message}: maximum entry error {error:.3g}")
    return error


def opnorm(matrix):
    return float(np.linalg.norm(matrix, 2))


def trace_distance(a, b):
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(a - b))))


def ket_density(vector):
    return np.outer(vector, vector.conj())


def hadamard(size):
    require(size >= 1 and size & (size - 1) == 0, "Hadamard size must be a power of two")
    matrix = np.ones((1, 1))
    while len(matrix) < size:
        matrix = np.block([[matrix, matrix], [matrix, -matrix]]) / np.sqrt(2)
    return matrix


def prepare_real(vector):
    """A full, real unitary taking |0> to a normalized real vector."""
    vector = np.asarray(vector, dtype=float)
    close(np.linalg.norm(vector), 1, "state normalization")
    first = np.zeros(len(vector))
    first[0] = 1
    direction = first - vector
    norm = np.linalg.norm(direction)
    if norm < 1e-14:
        return np.eye(len(vector))
    direction /= norm
    return np.eye(len(vector)) - 2 * np.outer(direction, direction)


def peaked_flat_preparation(dimension):
    """Full matrix of the known prefix-controlled circuit for |chi_0>."""
    require(dimension >= 2 and dimension & (dimension - 1) == 0,
            "the endpoint dimension must be a power of two")
    bits = dimension.bit_length() - 1
    unitary = np.eye(dimension, dtype=complex)
    previous_prefix_mass = 1.0
    for position in range(1, bits + 1):
        prefix_mass = (1 + 2.0**(-position)) / 2
        zero_probability = prefix_mass / previous_prefix_mass
        zero_rotation = coin_rotation(1 - zero_probability)
        suffix_identity = np.eye(2**(bits - position))
        blocks = [np.kron(zero_rotation if prefix == 0 else hadamard(2), suffix_identity)
                  for prefix in range(2**(position - 1))]
        unitary = block_diagonal(blocks) @ unitary
        previous_prefix_mass = prefix_mass
    return unitary


def hard_chain(n, m, injection):
    require(len(set(injection)) == n, "f must be injective")
    kernels = np.full((n, m), 1 / (2 * m))
    kernels[np.arange(n), injection] += 0.5
    transition = np.empty((n * m, n * m))
    for x in range(n):
        for y in range(m):
            transition[x * m + y] = np.tile(kernels[x] / n, n)
    marginal = np.full(m, 1 / (2 * m))
    marginal[injection] += 1 / (2 * n)
    stationary = np.tile(marginal / n, n)
    return transition, stationary, kernels, marginal


def discriminant(transition):
    return np.sqrt(transition * transition.T)


def check_full_oracle_completion():
    n, m = 2, 16
    injection = np.array([3, 12])
    _, _, kernels, _ = hard_chain(n, m, injection)
    kappa = np.full(m, 1 / np.sqrt(2 * m))
    kappa[0] = np.sqrt(0.5 + 1 / (2 * m))
    endpoint_preparation = peaked_flat_preparation(m)
    close(endpoint_preparation[:, 0], kappa, "prefix-controlled background preparation")
    known_preparation = np.kron(hadamard(n), endpoint_preparation)
    full_preparation = np.kron(np.eye(n), known_preparation)
    dimension = n * n * m  # Registers (source x, output z, output w); source y is a spectator.
    oracle = np.zeros((dimension, dimension))
    for x, z, w in itertools.product(range(n), range(n), range(m)):
        column = (x * n + z) * m + w
        row = (x * n + z) * m + (w ^ int(injection[x]))
        oracle[row, column] = 1
    clean_oracle = oracle @ full_preparation
    close(clean_oracle.conj().T @ clean_oracle, np.eye(dimension), "full completion unitarity")
    close(clean_oracle @ full_preparation.conj().T, oracle, "O_f = U_P A^dagger on ALL inputs")
    for x in range(n):
        output = clean_oracle[:, x * n * m].reshape(n, n, m)
        expected = np.zeros_like(output)
        expected[x] = np.sqrt(kernels[x] / n)[None, :]
        close(output, expected, "clean row amplitudes")
    rng = np.random.default_rng(SEED)
    reference_state = rng.normal(size=(dimension, 3)) + 1j * rng.normal(size=(dimension, 3))
    reference_state /= np.linalg.norm(reference_state)
    recovered = clean_oracle @ (full_preparation.conj().T @ reference_state)
    reference_error = float(np.linalg.norm(recovered - oracle @ reference_state))
    require(reference_error < TOL, "completion identity failed with an entangled reference")
    # An alternative extension has the same initialized row columns but is far away elsewhere.
    phase = np.ones(dimension)
    phase[1] = -1
    other_completion = clean_oracle @ np.diag(phase)
    initialized_columns = np.arange(n) * n * m
    close(other_completion[:, initialized_columns], clean_oracle[:, initialized_columns], "same row promise")
    arbitrary_completion_distance = opnorm(other_completion - clean_oracle)
    close(arbitrary_completion_distance, 2, "off-promise completion negative control")
    return {"n": n, "m": m, "full_dimension": dimension,
            "reference_vector_error": reference_error,
            "same_rows_other_completion_distance": arbitrary_completion_distance}


def reflection_zero(vector):
    result = vector.copy()
    result.flat[0] *= -1
    return result


def amplification_step(vector, prepare, unprepare, good, inverse=False):
    """Q = -A S_0 A^dagger S_good, with its exact adjoint when requested."""
    if inverse:
        result = prepare(reflection_zero(unprepare(vector)))
        result = result.copy()
        result[good] *= -1
    else:
        result = vector.copy()
        result[good] *= -1
        result = prepare(reflection_zero(unprepare(result)))
    return -result


def coin_rotation(success):
    require(-TOL <= success <= 1 + TOL, "invalid coin probability")
    success = float(np.clip(success, 0, 1))
    a, b = np.sqrt(1 - success), np.sqrt(success)
    return np.array([[a, -b], [b, a]])


def index_erasure_preparation(n, m, injection):
    h = hadamard(n)
    xor = np.arange(m)[None, :] ^ np.asarray(injection)[:, None]

    def a_ie(vector):
        result = h @ vector
        result = np.take_along_axis(result, xor, axis=1)
        return h @ result

    # This is the explicit conservative cap in the constructive proof. Conjugating
    # its uniform-index good subspace by H moves it to index zero in this simulation.
    iterations = int(np.ceil(np.sqrt(n)))
    alpha = np.pi / (4 * iterations + 2)
    dilution = n * np.sin(alpha) ** 2
    rotation = coin_rotation(dilution)

    def prepare(vector):
        rotated = np.tensordot(rotation, vector, axes=(1, 0))
        return np.stack([a_ie(rotated[coin]) for coin in range(2)])

    def unprepare(vector):
        reversed_ie = np.stack([a_ie(vector[coin]) for coin in range(2)])
        return np.tensordot(rotation.T, reversed_ie, axes=(1, 0))

    good = np.zeros((2, n, m), dtype=bool)
    good[1, 0, :] = True

    def full(vector):
        result = prepare(vector)
        for _ in range(iterations):
            result = amplification_step(result, prepare, unprepare, good)
        return result[::-1].copy()  # Reset the successful coin from 1 to 0.

    def full_inverse(vector):
        result = vector[::-1].copy()
        for _ in range(iterations):
            result = amplification_step(result, prepare, unprepare, good, inverse=True)
        return unprepare(result)

    return full, full_inverse, iterations


def check_exact_amplification_and_lcu():
    rng = np.random.default_rng(SEED + 1)
    records = []
    for n, m in [(2, 16), (4, 32), (8, 128)]:
        injection = rng.choice(m, n, replace=False)
        full_f, full_f_inverse, iterations = index_erasure_preparation(n, m, injection)
        shape = (2, n, m)
        zero = np.zeros(shape, dtype=complex)
        zero.flat[0] = 1
        target_f = np.zeros(shape, dtype=complex)
        target_f[0, 0, injection] = 1 / np.sqrt(n)
        f_error = float(np.linalg.norm(full_f(zero) - target_f))
        require(f_error < TOL, "exact index erasure failed, including its controlled-use phase")
        arbitrary = rng.normal(size=shape) + 1j * rng.normal(size=shape)
        arbitrary /= np.linalg.norm(arbitrary)
        close(full_f_inverse(full_f(arbitrary)), arbitrary, "index-erasure full inverse")

        s = n / m
        c = (np.sqrt(1 + s) - np.sqrt(s)) / np.sqrt(2)
        b = 1 / np.sqrt(2)
        total_weight = c + b
        selector_rotation = coin_rotation(b / total_weight)
        h_m = hadamard(m)

        def uniform_prepare(vector):
            return vector @ h_m.T

        def lcu(vector, inverse=False, wrong_f_phase=False):
            rotated = np.tensordot(selector_rotation, vector, axes=(1, 0))
            chosen_f = full_f_inverse(rotated[0]) if inverse else full_f(rotated[0])
            if wrong_f_phase:
                chosen_f = -chosen_f
            selected = np.stack([chosen_f, uniform_prepare(rotated[1])])
            return np.tensordot(selector_rotation.T, selected, axes=(1, 0))

        lcu_zero = np.zeros((2,) + shape, dtype=complex)
        lcu_zero.flat[0] = 1
        lcu_state = lcu(lcu_zero)
        stationary = np.full(m, 1 / (2 * m))
        stationary[injection] += 1 / (2 * n)
        target_q = np.sqrt(stationary)
        expected_good = np.zeros(shape, dtype=complex)
        expected_good[0, 0] = target_q / total_weight
        close(lcu_state[0], expected_good, "positive-amplitude LCU branch")
        success = float(np.linalg.norm(lcu_state[0]) ** 2)
        close(success, 1 / total_weight**2, "known LCU success probability")
        require(success >= 0.5 - TOL, "LCU success lower bound")
        wrong_lcu = lcu(lcu_zero, wrong_f_phase=True)
        wrong_phase_error = float(np.linalg.norm(wrong_lcu[0] - expected_good))
        require(wrong_phase_error > 0.2, "negative control failed to expose a relative-phase error")

        dilution_rotation = coin_rotation(1 / (4 * success))

        def prepare_q(vector):
            rotated = np.tensordot(dilution_rotation, vector, axes=(1, 0))
            return np.stack([lcu(rotated[coin]) for coin in range(2)])

        def unprepare_q(vector):
            reversed_lcu = np.stack([lcu(vector[coin], inverse=True) for coin in range(2)])
            return np.tensordot(dilution_rotation.T, reversed_lcu, axes=(1, 0))

        q_zero = np.zeros((2, 2) + shape, dtype=complex)
        q_zero.flat[0] = 1
        good = np.zeros_like(q_zero, dtype=bool)
        good[1, 0, :, :, :] = True
        q_state = amplification_step(prepare_q(q_zero), prepare_q, unprepare_q, good)
        q_state = q_state[::-1].copy()
        exact_target = np.zeros_like(q_state)
        exact_target[0, 0, 0, 0] = target_q
        q_error = float(np.linalg.norm(q_state - exact_target))
        require(q_error < TOL, "exact LCU cleanup failed, including all garbage and phase")
        records.append({"n": n, "m": m, "m_equals_n_to_four": m == n**4,
                        "grover_iterations": iterations,
                        "image_preparation_queries": 2 * iterations + 1,
                        "stationary_preparation_queries": 3 * (2 * iterations + 1),
                        "index_erasure_vector_error": f_error,
                        "lcu_success": success, "clean_qsample_vector_error": q_error,
                        "wrong_relative_phase_branch_error": wrong_phase_error})
    return {"cases": records}


def check_postselection_constants():
    rng = np.random.default_rng(SEED + 2)
    n, m = 4, 64
    injection = np.array([1, 7, 23, 58])
    _, _, _, stationary = hard_chain(n, m, injection)
    q = np.sqrt(stationary)
    uniform = np.ones(m) / np.sqrt(m)
    image = np.zeros(m)
    image[injection] = 1 / np.sqrt(n)
    projection = np.eye(m) - np.outer(uniform, uniform)
    projected = projection @ q
    success = float(np.vdot(projected, projected).real)
    normalized = projected / np.sqrt(success)
    ideal = ket_density(q)
    ideal_post = ket_density(normalized)
    close(trace_distance(ideal_post, ket_density(image)), np.sqrt(n / m), "index-erasure target error")
    require(success >= 7 / 32, "uniform projection-success constant")
    records = []
    for mode in ["pure", "mixed"]:
        for parameter in [0.001, 0.02, 0.1]:
            direction = rng.normal(size=m) + 1j * rng.normal(size=m)
            direction -= q * np.vdot(q, direction)
            direction /= np.linalg.norm(direction)
            if mode == "pure":
                perturbed = np.sqrt(1 - parameter**2) * q + parameter * direction
                actual = ket_density(perturbed)
            else:
                actual = (1 - parameter) * ideal + parameter * ket_density(direction)
            epsilon = trace_distance(actual, ideal)
            unnormalized = projection @ actual @ projection
            observed_success = float(np.trace(unnormalized).real)
            conditional_error = trace_distance(unnormalized / observed_success, ideal_post)
            require(abs(observed_success - success) <= epsilon + TOL, "success probability continuity")
            require(conditional_error <= epsilon / success + TOL, "postselection error <= epsilon / p")
            records.append({"input_type": mode, "input_trace_error": epsilon,
                            "success": observed_success, "conditional_trace_error": conditional_error,
                            "proved_bound": epsilon / success})
    return {"n": n, "m": m, "m_equals_n_to_four": m == n**4,
            "ideal_success": success, "uniform_lower_bound": 7 / 32, "cases": records}


def check_chain_and_product_spectra():
    n, m = 2, 16
    transition, stationary, _, _ = hard_chain(n, m, np.array([2, 13]))
    dimension = n * m
    close(transition.sum(axis=1), np.ones(dimension), "stochastic rows")
    close(stationary @ transition, stationary, "stationarity")
    powered = transition @ transition
    close(powered, np.tile(stationary, (dimension, 1)), "exact two-step mixing")
    uniform = np.ones(dimension) / dimension
    close(uniform @ transition, stationary, "one-step mixing from the uniform warm start")
    close(np.max(uniform / stationary), 2, "two-warm initialization")
    d_one, d_two = discriminant(transition), discriminant(powered)
    target = np.sqrt(stationary)
    close(d_two, np.outer(target, target), "rank-one flat discriminant")
    difference = d_two - d_one @ d_one
    measured_difference = opnorm(difference)
    independent_lower_bound = 1 - opnorm(d_one)**2
    rayleigh = float(target @ difference @ target)
    require(measured_difference >= rayleigh - TOL, "operator norm below an explicit Rayleigh quotient")
    require(rayleigh >= independent_lower_bound - TOL, "independent contraction lower bound")
    require(measured_difference > 0.25, "the flat-composition negative control became trivial")
    cases = []
    for scale in [4, 9, 64]:
        slow = np.array([[1 - 1 / scale, 1 / scale], [1 / scale, 1 - 1 / scale]])
        product = np.kron(transition, slow)
        product_stationary = np.kron(stationary, [0.5, 0.5])
        product_square = product @ product
        close(product_square, np.kron(powered, slow @ slow), "product square")
        detailed_balance = product_stationary[:, None] * product_square
        close(detailed_balance, detailed_balance.T, "exact reversibility after two steps")
        flat = discriminant(product_square)
        close(flat, np.kron(np.outer(target, target), slow @ slow), "product flat factorization")
        spectrum = np.linalg.eigvalsh(flat)
        expected_spectrum = np.zeros(2 * dimension)
        expected_spectrum[-2:] = [(1 - 2 / scale)**2, 1]
        close(spectrum, expected_spectrum, "product spectrum")
        for steps in [2, 5]:
            row = np.linalg.matrix_power(product, steps)[0]
            distance = 0.5 * np.sum(np.abs(row - product_stationary))
            close(distance, (1 - 2 / scale)**steps / 2, "worst-case mixing formula after two steps")
        cases.append({"T": scale, "measured_gap": float(spectrum[-1] - spectrum[-2]),
                      "predicted_gap": 4 / scale - 4 / scale**2})
    return {"n": n, "m": m, "m_equals_n_to_four": m == n**4,
            "within_main_theorem_n_at_least_four": n >= 4,
            "purpose": "finite algebraic diagnostic; no asymptotic lower bound is tested",
            "flat_composition_norm_error": measured_difference,
            "rayleigh_witness": rayleigh, "independent_norm_lower_bound": independent_lower_bound,
            "product_cases": cases}


def path_data(transition, steps):
    size = len(transition)
    powered = np.linalg.matrix_power(transition, steps)
    affinity = np.zeros_like(transition)
    history = np.zeros((size ** (steps + 1), size))
    for path in itertools.product(range(size), repeat=steps + 1):
        weight = np.prod([transition[path[k], path[k + 1]] for k in range(steps)])
        index = np.ravel_multi_index(path, (size,) * (steps + 1))
        history[index, path[0]] = np.sqrt(weight)
    reversal = [np.ravel_multi_index(path[::-1], (size,) * (steps + 1))
                for path in itertools.product(range(size), repeat=steps + 1)]
    compressed = history.T @ history[reversal]
    for x, y in itertools.product(range(size), repeat=2):
        for internal in itertools.product(range(size), repeat=steps - 1):
            path = (x,) + internal + (y,)
            forward = np.prod([transition[path[k], path[k + 1]] for k in range(steps)])
            backward = np.prod([transition[path[k + 1], path[k]] for k in range(steps)])
            affinity[x, y] += np.sqrt(forward / powered[x, y] * backward / powered[y, x])
    return powered, affinity, compressed


def check_bridge_identity_and_controls():
    rng = np.random.default_rng(SEED + 3)
    flows = rng.uniform(0.1, 1, (3, 3))
    flows += flows.T
    reversible = flows / flows.sum(axis=1)[:, None]
    nonreversible = np.array([[0.2, 0.7, 0.1], [0.1, 0.2, 0.7], [0.7, 0.1, 0.2]])
    cases = []
    for label, transition in [("reversible", reversible), ("nonreversible", nonreversible)]:
        for steps in [2, 3, 4]:
            powered, affinity, compressed = path_data(transition, steps)
            flat = discriminant(powered)
            direct_power = np.linalg.matrix_power(discriminant(transition), steps)
            close(compressed, direct_power, "whole-path compression equals D(P)^j")
            close(compressed, flat * affinity, "conditional bridge affinity identity")
            error = opnorm(flat - compressed)
            deficit = float(np.max(1 - affinity))
            require(error <= max(0, deficit) * opnorm(flat) + TOL, "uniform bridge-affinity norm bound")
            if label == "reversible":
                close(affinity, np.ones_like(affinity), "reversible bridge equality")
                require(error < TOL, "reversible flat powers must compose")
            elif steps == 2:
                require(error > 0.1, "nonreversible flat-power negative control")
                cycle_forward = transition[0, 1] * transition[1, 2] * transition[2, 0]
                cycle_reverse = transition[0, 2] * transition[2, 1] * transition[1, 0]
                require(abs(cycle_forward - cycle_reverse) > 0.1, "cycle criterion negative control")
            cases.append({"chain": label, "steps": steps, "flat_power_error": error,
                          "maximum_bridge_affinity_deficit": deficit,
                          "norm_bound": max(0, deficit) * opnorm(flat)})
    # Strict positivity is essential to the j=2 converse. A lazy directed five-cycle
    # is irreducible and aperiodic, is not reversible, yet its flat squares agree.
    cycle = np.zeros((5, 5))
    cycle[np.arange(5), (np.arange(5) + 1) % 5] = 1
    sparse_nonreversible = (np.eye(5) + cycle) / 2
    sparse_error = opnorm(discriminant(sparse_nonreversible @ sparse_nonreversible)
                          - discriminant(sparse_nonreversible) @ discriminant(sparse_nonreversible))
    require(sparse_error < TOL, "sparse support counterexample to an unqualified converse")
    require(opnorm(sparse_nonreversible - sparse_nonreversible.T) > 0.5,
            "the sparse counterexample must remain nonreversible")
    return {"cases": cases, "nonpositive_support_converse_counterexample_error": sparse_error}


def correcting_rotation(first, second):
    """Unitary R with R first=second and ||R-I||=||first-second||."""
    first, second = np.asarray(first, dtype=complex), np.asarray(second, dtype=complex)
    z = np.vdot(first, second)
    perpendicular = second - z * first
    s = float(np.linalg.norm(perpendicular))
    identity = np.eye(len(first), dtype=complex)
    if s < 1e-13:
        return identity + (z - 1) * ket_density(first)
    other = perpendicular / s
    return (identity + (z - 1) * ket_density(first) + (z.conjugate() - 1) * ket_density(other)
            + s * (np.outer(other, first.conj()) - np.outer(first, other.conj())))


def block_diagonal(blocks):
    size = sum(len(block) for block in blocks)
    result = np.zeros((size, size), dtype=complex)
    start = 0
    for block in blocks:
        end = start + len(block)
        result[start:end, start:end] = block
        start = end
    return result


def check_coherent_bridge_compiler():
    transition = np.array([[0.2, 0.7, 0.1], [0.1, 0.2, 0.7], [0.7, 0.1, 0.2]])
    size = len(transition)
    powered = transition @ transition
    row_units = [prepare_real(np.sqrt(row)) for row in transition]
    second_step = block_diagonal(row_units)
    zero = np.zeros(size * size, dtype=complex)
    zero[0] = 1
    compiled_blocks, exact_blocks, target_columns = [], [], []
    bridge_errors, row_errors, extension_errors = [], [], []
    for x in range(size):
        history = second_step @ np.kron(row_units[x], np.eye(size))
        bridge_unitary = np.zeros((size * size, size * size), dtype=complex)
        for y in range(size):
            bridge = np.sqrt(transition[x] * transition[:, y] / powered[x, y])
            exact_bridge = prepare_real(bridge)
            # A small source/endpoint-dependent complex unitary perturbation.
            angle = 0.012 * (1 + x + 2 * y)
            phase = np.diag(np.exp(1j * angle * np.arange(size)))
            approximate_bridge = phase @ exact_bridge
            bridge_errors.append(float(np.linalg.norm(approximate_bridge[:, 0] - bridge)))
            indices = np.arange(size) * size + y
            bridge_unitary[np.ix_(indices, indices)] = approximate_bridge
        compiled = bridge_unitary.conj().T @ history
        target = np.zeros(size * size, dtype=complex)
        target[:size] = np.sqrt(powered[x])
        actual = compiled @ zero
        correction = correcting_rotation(actual, target)
        close(correction.conj().T @ correction, np.eye(size * size), "correcting rotation unitarity")
        close(correction @ actual, target, "one fixed exact extension column")
        distance = float(np.linalg.norm(actual - target))
        close(opnorm(correction - np.eye(size * size)), distance, "optimal completion rotation distance")
        exact = correction @ compiled
        close(exact[:, 0], target, "corrected clean row")
        compiled_blocks.append(compiled)
        exact_blocks.append(exact)
        target_columns.append(target)
        row_errors.append(distance)
        extension_errors.append(opnorm(compiled - exact))
    compiled = block_diagonal(compiled_blocks)
    exact = block_diagonal(exact_blocks)
    delta = max(bridge_errors)
    require(max(row_errors) <= delta + TOL, "uniform bridge error must control all clean row columns")
    require(opnorm(compiled - exact) <= delta + TOL, "one full-unitary completion bound")
    close(opnorm(compiled.conj().T - exact.conj().T), opnorm(compiled - exact), "consistent inverse bound")
    # Coherent source-reference input: the reference explicitly retains each source label.
    entangled = np.zeros((size**3, size), dtype=complex)
    for x in range(size):
        entangled[x * size * size, x] = 1 / np.sqrt(size)
    reference_error = float(np.linalg.norm((compiled - exact) @ entangled))
    require(reference_error <= delta + TOL, "reference-preserving coherent approximation")
    rng = np.random.default_rng(SEED + 4)
    known, _ = np.linalg.qr(rng.normal(size=compiled.shape) + 1j * rng.normal(size=compiled.shape))
    composed_actual = compiled.conj().T @ known @ compiled
    composed_ideal = exact.conj().T @ known @ exact
    require(opnorm(composed_actual - composed_ideal) <= 2 * delta + TOL,
            "two coherent forward/inverse calls with intervening source mixing")
    # A pure-state fidelity promise alone allows arbitrary endpoint-dependent phases.
    uniform_bridge = np.ones(2) / np.sqrt(2)
    prepared_with_phase = [-uniform_bridge, uniform_bridge]
    fidelities = [float(abs(np.vdot(uniform_bridge, vector))**2) for vector in prepared_with_phase]
    close(fidelities, np.ones(2), "phase-blind bridge promises are all perfect")
    bad_endpoint = np.array([-1, 1]) / np.sqrt(2)
    good_endpoint = np.ones(2) / np.sqrt(2)
    endpoint_fidelity = float(abs(np.vdot(good_endpoint, bad_endpoint))**2)
    require(endpoint_fidelity < TOL, "negative control must expose endpoint-dependent phases")
    return {"uniform_bridge_vector_error": delta, "maximum_row_vector_error": max(row_errors),
            "full_unitary_completion_error": opnorm(compiled - exact),
            "reference_vector_error": reference_error,
            "two_call_operator_error": opnorm(composed_actual - composed_ideal),
            "phase_blind_bridge_fidelities": fidelities,
            "phase_blind_compiler_endpoint_fidelity": endpoint_fidelity}


CHECKS = [check_full_oracle_completion, check_exact_amplification_and_lcu,
          check_postselection_constants, check_chain_and_product_spectra,
          check_bridge_identity_and_controls, check_coherent_bridge_compiler]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also write the machine-readable report to this path")
    args = parser.parse_args()
    report = {"scope": "Finite circuit and algebra checks only. The inherited asymptotic query lower bound is not numerically tested.",
              "python": platform.python_version(), "numpy": np.__version__, "seed": SEED,
              "absolute_tolerance": TOL, "checks": []}
    for check in CHECKS:
        started = time.perf_counter()
        try:
            values = check()
            result = {"name": check.__name__, "status": "pass", "results": values}
        except Exception as error:
            result = {"name": check.__name__, "status": "fail", "error": str(error),
                      "traceback": traceback.format_exc()}
        result["elapsed_seconds"] = time.perf_counter() - started
        report["checks"].append(result)
    report["status"] = "pass" if all(item["status"] == "pass" for item in report["checks"]) else "fail"
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")
    raise SystemExit(0 if report["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
