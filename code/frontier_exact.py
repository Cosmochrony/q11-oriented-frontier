#!/usr/bin/env python3
"""frontier_exact.py -- stdlib-only exact frontier check (no spectral_O12, no numpy, no sibling repo).

Heis_3 law (a,b,z)(a',b',z') = (a+a', b+b', z+z'+a*b'); generators {+-X, +-Y}; outgoing frontier
d+S_m = {(g,s): d(e,g)=m, d(e,gs)=m+1}; central increment Delta A_c(g,s) = z(gs)-z(g) = a(g)*s_b (c=1).
Runs in H_3(Z) (modulus None) and in H_3(Z/qZ) for the corpus primes; prints exact rationals.
"""
from fractions import Fraction
from collections import deque

def frontier(mmax, q=None):
    red = (lambda v: v) if q is None else (lambda v: v % q)
    cen = (lambda v: v) if q is None else (lambda v: ((v + q // 2) % q) - q // 2)   # centred residue
    mul = lambda g, s: (red(g[0]+s[0]), red(g[1]+s[1]), red(g[2]+s[2]+g[0]*s[1]))
    gens = [(1,0,0), (red(-1),0,0), (0,1,0), (0,red(-1),0)]
    dist = {(0,0,0): 0}; dq = deque([(0,0,0)])
    while dq:
        g = dq.popleft()
        if dist[g] > mmax: continue            # depth-limited BFS: ball of radius mmax+2 only
        for s in gens:
            h = mul(g, s)
            if h not in dist: dist[h] = dist[g] + 1; dq.append(h)
    rows = []
    for m in range(1, mmax + 1):
        absum = sup = cnt = sgn_plus = sgn_sym = n_sym = 0
        for g, d in dist.items():
            if d != m: continue
            for s in gens:
                h = mul(g, s); dh = dist.get(h); dA = cen(h[2] - g[2])
                if dh == m + 1: absum += abs(dA); sup += (dA != 0); cnt += 1; sgn_plus += dA; sgn_sym += dA; n_sym += 1
                elif dh == m - 1: sgn_sym += dA; n_sym += 1
        rows.append((m, Fraction(absum, cnt), Fraction(sup, cnt), sgn_plus, sgn_sym))
    return rows

if __name__ == "__main__":
    ref = frontier(6)
    print("H_3(Z): m, <|dA|>_d+, support fraction, sum dA over d+, sum dA over d+ U d-")
    for r in ref: print(*r)
    for q in (61, 101, 151, 211, 307):
        rq = frontier(6, q)
        print(f"q={q}: sequence equals H_3(Z) one: {[r[1] for r in rq] == [r[1] for r in ref]}; "
              f"signed sums zero: {all(r[3] == 0 and r[4] == 0 for r in rq)}")
    # rho_chi = <sigma_L dA>/<|dA|> with sigma_L := sign(dA) on the support is 1 by construction wherever <|dA|> != 0
