# data/ -- campaign summaries (June 2026)

Six `*_summary.json` files (about 21 KB in total), copied unchanged from the archived working directory of the
campaign (`simulation/fermionic-matter/`, untracked there).

| file | produced by | q | file date |
|---|---|---|---|
| `angular_area_q{61,101,151}_summary.json` | `weil_bfs_angular_area.py --mode full` | 61, 101, 151 | 7 June 2026 (23:43-23:44) |
| `q11_frontier_q{61,101,151}_summary.json` | `q11_oriented_frontier.py` (mode full) | 61, 101, 151 | 8 June 2026 (15:03) |

Provenance.

- Pipeline: the campaign was run with the `spectral_O12` conventions (the checkpoints, not archived here, carry the
  stamp `"pipeline": "spectral_O12"`). The scripts of this repository carry the two functions they use from that
  module (`build_generators`, `heisenberg_mul_batch`) as local reference functions, identical function by function;
  they stamp `"heis3-local"`.
- Random seed: `RNG_SEED = 20260607` (the block sampling for the capacity $\sigma_{\rm pair}$ uses `RNG_SEED + q`).
- Script versions: the files do not record the revision of the script that wrote them. The script history is in
  the git log of this repository (`weil_bfs_angular_area.py`: 7-8 June 2026; `q11_oriented_frontier.py`:
  8 June 2026, maximal-locking bound added 16 June 2026).
- Reproduction check (5 October 2026): re-running the scripts (`q11_oriented_frontier.py` here;
  `weil_bfs_angular_area.py` is carried by the repository `angular-amplitude-reduction`, which holds the same six
  files and runs it), from a fresh `git archive`
  copy, with `numpy` 2.4.0 and Python 3.14, reproduces every key of the six files to $10^{-12}$ (lists, flags,
  edge counts, status strings; the `NaN` at index 0 of `Theta_Weil` is `NaN` in both). The archived
  `*_profile.csv`, `*_checkpoint.jsonl` and `*.pdf` of the campaign are not versioned here: the scripts regenerate
  them.
- These files are data, not claims: the statements made in the note about them are listed in its
  Reproduction section (`README.md`) together with the exact scripts.
