# Q11 Oriented Frontier — A Recursive Diagnostic for the Angular Generation Split

J. Beau, Independent Researcher, France

## Status

Working note (preprint), v1.0.

## Abstract

The symmetric-capacity obstruction establishes that the raw shell observable of the angular
generation split vanishes identically, $\Theta_{\mathrm{raw}} = 0$: on a symmetric BFS shell the
involution $g \mapsto g^{-1}$ pairs opposite central phases and erases the oriented
$J_\Pi$-odd component before the radial recursion can act.

This note defines the honest replacement: a **frontier transfer observable** attached to the
directed outgoing edges $g \to gs$ of the cascade, whose central increment is the Heisenberg
cocycle $a(g)\, s_b$, the discrete counterpart of the Baker–Campbell–Hausdorff term
$\tfrac{1}{2}[X, Y]$ and hence of the dynamical $J_3$.

The orientation is the recursive arrow $\partial_\tau = \log g$ from the projection origin to
increasing BFS depth, not an extracted weight. The first test is not an amplitude value but the
existence of an oriented signal,
$\langle \Delta A_c \rangle_{\partial^+ S_m} \neq 0$, which may fail if a residual automorphism
re-pairs the frontier; the discriminating anti-bias control is the symmetrised-frontier
cancellation $\langle \Delta A_c \rangle_{\partial^+ S_m \cup \partial^- S_m} = 0$.

No normalisation $\mathcal{N}_A$, no dictionary value, and no $\varepsilon$ appear in this
note: it tests only whether the recursion produces a non-zero, bias-free oriented signal.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It is a
companion diagnostic note to Q14, supplying the falsification protocol for the recursive
existence of the $J_3$-odd cascade signal that underlies the Q14 §6 inter-generation splitting
mechanism. Together with the **angular-amplitude-reduction** note (BCH reduction; observable
to be measured) and the **projective-residue-schur** note (operator-side Schur form,
finite/Lorentzian separation), it completes the diagnostic frame in which the remaining
quantitative step of the fermionic sector can be carried out.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/Q11OrientedFrontier.tex` and produces
`out/Q11OrientedFrontier.pdf`.
