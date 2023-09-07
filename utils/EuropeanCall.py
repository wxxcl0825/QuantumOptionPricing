import numpy as np
from scipy.stats import norm


def monte_carlo(N, s0, K, T, r, sigma):
    w = np.random.standard_normal(N)
    st = s0 * np.exp(sigma * np.sqrt(T) * w + (r - sigma ** 2 / 2) * T)
    payoff = np.maximum(st - K, 0)
    c = np.exp(-r * T) * np.mean(payoff)
    return c


def BSM(s0, K, T, r, sigma):
    d1 = (np.log(s0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return s0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


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


def quantum(param):
    return {}
