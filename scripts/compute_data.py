"""Reproduce every number used by index.html.

Run:  python3 scripts/compute_data.py
Writes scripts/explainer_data.json (the data embedded in index.html).
Needs numpy and scipy. Sieves all primes up to 10^8 (about 100 MB of memory, a few minutes).

What it computes
  1. Zeros of the Riemann zeta function up to height 300 (Riemann-Siegel formula + bisection).
  2. The circle chain: circles of radius p (every prime p >= 3) standing on a line, each
     touching the next, so consecutive centres are 2*sqrt(p*q) apart horizontally.
  3. The wobble: centre position minus the smooth curve 2*li(y^2) - y - 3, scaled by y^1.5/ln y.
  4. The spectrum of the wobble in ln y, for real primes and for Cramer's random model.
"""
import json, os
import numpy as np
from scipy.special import expi

HERE = os.path.dirname(os.path.abspath(__file__))
li = lambda v: expi(np.log(v))

# 1. zeta zeros via the Riemann-Siegel Z function
def theta(t): return t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
def Z(t):
    N = int(np.sqrt(t/(2*np.pi))); n = np.arange(1, N+1)
    s = 2*np.sum(np.cos(theta(t) - t*np.log(n))/np.sqrt(n))
    a = np.sqrt(t/(2*np.pi)); p = a - N
    C0 = np.cos(2*np.pi*(p*p - p - 1/16))/np.cos(2*np.pi*p)
    return s + (-1)**(N-1)*a**-0.5*C0
ts = np.arange(10, 300, 0.005); v = np.array([Z(t) for t in ts]); zeros = []
for i in np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]:
    a, b = ts[i], ts[i+1]
    for _ in range(40):
        m = (a+b)/2
        if np.sign(Z(m)) == np.sign(Z(a)): a = m
        else: b = m
    zeros.append((a+b)/2)
print(len(zeros), "zeros up to 300; first:", np.round(zeros[:5], 6))

# 2-3. circle chain and wobble
def sieve(X):
    s = np.ones(X+1, bool); s[:2] = False
    for i in range(2, int(X**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0].astype(float)
def wobble(p):
    x = np.concatenate([[0], np.cumsum(2*np.sqrt(p[:-1]*p[1:]))])
    E = x - (2*li(p**2) - p - 3)
    return np.log(p), E/(p**1.5/np.log(p))
p8 = sieve(10**8); p8 = p8[p8 >= 3]
u, f = wobble(p8)
ug = np.linspace(np.log(1e3), u[-1], 3000); fg = np.interp(ug, u, f)

# 4. spectra (primes up to 10^7, same method for real primes and Cramer's model)
def spectrum(p):
    uu, ff = wobble(p)
    g2 = np.linspace(np.log(1e3), uu[-1], 40000); y = np.interp(g2, uu, ff); y -= y.mean()
    w = np.hanning(len(g2)); du = g2[1]-g2[0]
    gam = np.arange(5, 52.01, 0.05)
    return gam, np.array([abs(np.sum(w*y*np.exp(-1j*g*g2)))*du for g in gam])
p7 = p8[p8 <= 10**7]
rng = np.random.default_rng(7); n = np.arange(3, 10**7+1)
cram = n[rng.random(len(n)) < 1/np.log(n.astype(float))].astype(float)
gam, Ar = spectrum(p7); _, Ac = spectrum(cram)

data = {"zeros": [round(z, 6) for z in zeros],
        "wobble": {"u": [round(x, 5) for x in ug], "f": [round(x, 4) for x in fg]},
        "spec": {"t": [round(x, 2) for x in gam], "real": [round(x, 4) for x in Ar], "random": [round(x, 4) for x in Ac]}}
json.dump(data, open(os.path.join(HERE, "explainer_data.json"), "w"), separators=(",", ":"))
print("wrote scripts/explainer_data.json")
