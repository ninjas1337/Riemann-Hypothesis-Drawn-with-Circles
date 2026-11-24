# The Riemann Hypothesis, Drawn with Circles

**An interactive explainer of the most famous problem in mathematics, for everyone. No formulas needed until the very end.**

👉 **Open it here: https://ninjas1337.github.io/Riemann-Hypothesis-Drawn-with-Circles/**

![Preview](preview.png)

## The idea in one paragraph

Draw a circle of radius 3 standing on a line. Next to it, a circle of radius 5, just touching. Then 7, 11, 13, and so on: one circle for every prime. The centres follow a smooth curve predicted by the prime number theorem, but never exactly; they wobble. Split that wobble into its frequencies and out come 14.13, 21.02, 25.01, 30.42 … the zeros of the Riemann zeta function. Replace the primes with random numbers and the zeros vanish. The Riemann Hypothesis says the wobble never grows beyond a certain size, no matter how far you go.

## What the page covers

1. **The circles:** one circle of prime radius for every prime, each touching the next.
2. **Complex numbers are not complex:** *i* is just a quarter-turn; the "imaginary" axis is the direction at right angles to the number line. For a 3D version with a sphere, see [Complex numbers are not imaginary](https://ninjas1337.github.io/Imaginary-numbers-are-real/).
3. **The wobble:** how far each centre lies from the smooth curve, for every prime up to 100 million.
4. **The wobble is music:** its hidden frequencies are the zeta zeros; with random numbers they disappear. The wobble rebuilt from "wheels", one per zero.
5. **What the hypothesis says:** all wheels stay the same size. Move one zero off the critical line and the wobble runs away.
6. **Where it stands:** the reported proof of November 2026, and what a proof would settle.

## Mathematical background

The construction is as far as I know new as a picture; but the mathematics behind it is classical. The horizontal position of the n-th centre is essentially twice the sum of the primes up to pₙ, which by the prime number theorem follows 2·li(pₙ²). The fluctuations are described by the explicit formula of Riemann and von Mangoldt, where each zeta zero ρ contributes a wave. Via von Koch's criterion (1901), the Riemann Hypothesis is equivalent to

    xₙ = 2·li(pₙ²) − pₙ + O(pₙ^(3/2+ε))   for every ε > 0.

## Reproduce the numbers

```
python3 scripts/compute_data.py   # zeros, circle chain up to 10^8, spectra (numpy, scipy)
python3 scripts/build_page.py     # embeds the data into index.html
```

## Credits

Concept and construction: **Sanjin Redzic** ([ORCID 0009-0006-7034-6869](https://orcid.org/0009-0006-7034-6869)). Code and computations written with Claude (Anthropic).

Related: [Complex numbers are not imaginary](https://ninjas1337.github.io/Imaginary-numbers-are-real/) (a sphere seen from the front and from above) · [Prime Helix](https://github.com/ninjas1337/Prime-Helix) · [Gibbs phenomenon explained geometrically](https://github.com/ninjas1337/Fourier-Gibbs-Phenomenon-Explained-Geometrically)

## References

- B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, Monatsber. Berliner Akad., 1859.
- H. von Koch, *Sur la distribution des nombres premiers*, Acta Math. 24 (1901), 159–182.
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer GTM 74, 2000, ch. 17–18.
- J. E. Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. Paris 158 (1914), 1869–1872.
- H. Cramér, *On the order of magnitude of the difference between consecutive prime numbers*, Acta Arith. 2 (1936), 23–46.
- A. M. Odlyzko, *Tables of zeros of the Riemann zeta function*.

## License

MIT, see [LICENSE](LICENSE).
