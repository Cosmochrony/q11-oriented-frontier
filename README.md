# Q11 Oriented Frontier — A Recursive Diagnostic for the Angular Generation Split

J. Beau, Independent Researcher, France

## Status

Working note (preprint), v1.1 (local candidate, not deposited; last deposited version 1.0.1). DOI: [10.5281/zenodo.20601245](https://doi.org/10.5281/zenodo.20601245)

## Abstract

The symmetric-capacity obstruction establishes that the raw shell observable of the angular
generation split vanishes identically, $\Theta_{\mathrm{raw}} = 0$: on a symmetric BFS shell the
involution $g \mapsto g^{-1}$ pairs opposite central phases and erases the oriented
$J_\Pi$-odd component before the radial recursion can act.

This note defines the honest replacement: a **frontier transfer observable** attached to the
directed outgoing edges $g \to gs$ of the cascade, whose central increment is the Heisenberg
cocycle $a(g)\, s_b$, the discrete oriented increment of the cascade. It is a counterpart of the
orientation datum (a quantity odd under reversal of the cascade, linear in $s_b$, related to the
orientation of the ordered $\mathfrak{sl}_2$ product only by analogy), and not the $J_3$ coefficient of
the metaplectic step, which in the $\mathrm{SL}(2)$ model of Q14 is produced by the
$\mathfrak{sl}_2$ commutator $[E,F]=H$ (Q14, Proposition 6.5).

The orientation is the arrow of the Cayley graph from the projection origin to increasing BFS depth,
not an extracted weight; no identification of this arrow with an ordering derivative
$\partial_\tau$ is made. The chiral lift of the residual reflection is reduced to one named hypothesis [H-WS]: $R_b=W(-I)$
acts on the chiral carrier $S_L\oplus S_R$ as the scalar $-1$, so that $[\gamma_5,R_b]=0$ (supplied by no
source; the stronger group-level formulation is not available at the corpus primes). The first test is not an amplitude value but the
existence of an oriented signal,
$\langle \Delta A_c \rangle_{\partial^+ S_m} \neq 0$, which may fail if a residual automorphism
re-pairs the frontier; the discriminating anti-bias control is the symmetrised-frontier
cancellation $\langle \Delta A_c \rangle_{\partial^+ S_m \cup \partial^- S_m} = 0$.

No normalisation $\mathcal{N}_A$, no dictionary value, and no $\varepsilon$ appear in this
note: it tests only whether the recursion produces a non-zero, bias-free oriented signal.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It is a
companion diagnostic note to Q14, supplying the falsification protocol for the existence of an
oriented frontier signal, a counterpart of the orientation datum of the Q14 §6 inter-generation
splitting mechanism (not of its $J_3$ coefficient). Together with the **angular-amplitude-reduction** note (BCH reduction; observable
to be measured) and the **projective-residue-schur** note (Schur form of the
compression remainder, conditional generation reading), it completes the diagnostic frame in which the remaining
quantitative step of the fermionic sector can be carried out.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/Q11OrientedFrontier.tex` and produces
`out/Q11OrientedFrontier.pdf`.
