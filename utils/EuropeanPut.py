import numpy as np
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.algorithms import IterativeAmplitudeEstimation, EstimationProblem
from qiskit.circuit.library import LinearAmplitudeFunction
from qiskit_aer.primitives import Sampler
from qiskit_finance.circuit.library import LogNormalDistribution
from scipy.stats import norm


def monte_carlo(N, s0, K, T, r, sigma):
    w = np.random.standard_normal(N)
    st = s0 * np.exp(sigma * np.sqrt(T) * w + (r - sigma ** 2 / 2) * T)
    payoff = np.maximum(K - st, 0)
    c = np.exp(-r * T) * np.mean(payoff)
    return c


def BSM(s0, K, T, r, sigma):
    d1 = (np.log(s0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - s0 * norm.cdf(-d1)


def classic(param: list) -> dict:
    s0, k, t, r, sigma, eps, n = param
    res = {}
    res["BSM"] = BSM(s0, k, t, r, sigma)
    samples = np.linspace(0, n, 21)[1:]
    prices = [monte_carlo(int(sample), s0, k, t, r, sigma) for sample in samples]
    res["result"] = prices[-1]
    res["log"] = [samples, prices]
    res["eps"] = -int(np.log10(eps))
    return res


def compile_circuit(circuit, opt):
    basis_gates = ["h", "ry", "cry", "cx", "ccx",
                   "p", "cp", "x", "s", "sdg", "y", "t", "cz"]
    return transpile(circuit, basis_gates=basis_gates, optimization_level=opt)


def get_uncertainty_model(nbits, mu, sigma, low, high):
    return LogNormalDistribution(nbits, mu=mu, sigma=sigma ** 2, bounds=(low, high))


def get_european_put_objective(nbits, K, low, high, c):
    breakpoints = [low, K]
    slopes = [-1, 0]
    offsets = [K - low, 0]
    f_min, f_max = 0, K - low
    return LinearAmplitudeFunction(
        nbits, slopes, offsets,
        domain=(low, high), image=(f_min, f_max),
        breakpoints=breakpoints, rescaling_factor=c
    )


def quantum_monte_carlo(nbits, S0, sigma, r, T, K, opt, c=0.25, epsilon=0.01, alpha=0.05, nshots=1000):
    mu = (r - sigma ** 2 / 2) * T + np.log(S0)
    sigma *= np.sqrt(T)
    mean = np.exp(mu + sigma ** 2 / 2)
    var = (np.exp(sigma ** 2) - 1) * np.exp(2 * mu + sigma ** 2)
    stdvar = np.sqrt(var)
    low = np.maximum(0, mean - 3 * stdvar)
    high = mean + 3 * stdvar
    uncertainty_model = get_uncertainty_model(nbits, mu, sigma, low, high)
    european_put_objective = get_european_put_objective(
        nbits, K, low, high, c)
    num_bits = european_put_objective.num_qubits
    circ = QuantumCircuit(num_bits)
    circ.append(uncertainty_model, range(nbits))
    circ.append(european_put_objective, range(num_bits))
    problem = EstimationProblem(
        state_preparation=circ,
        objective_qubits=[nbits],
        post_processing=european_put_objective.post_processing)
    ae = IterativeAmplitudeEstimation(
        epsilon_target=epsilon, alpha=alpha, sampler=Sampler(
            run_options={"shots": nshots})
    )
    circuit = compile_circuit(ae.construct_circuit(problem, 1, True), opt=opt)
    result = ae.estimate(problem).estimation_processed * np.exp(-r * T)
    return [circuit, result]


def quantum(param) -> dict:
    s0, k, t, r, sigma, eps, nbits, opt = param
    res = {}
    _res = quantum_monte_carlo(nbits, s0, sigma, r, t, k, opt, epsilon=eps)
    res["circuit"] = _res[0]
    res["result"] = _res[1]
    return res
