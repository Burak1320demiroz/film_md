## Description
Brief summary of the changes made and the motivation behind them.

## Related Issues
Fixes #(issue number) or relates to #(issue number).

## Invariant Checklist
Before requesting review, please confirm that this PR conforms to all repository invariants:

- [ ] **Strictly Text Only:** No binary video (`.mp4`), audio (`.wav`), or raw image files were committed. (Sole exception: documentation files in `images/readme_*.png`).
- [ ] **Tests Green:** All 46 automated regression tests pass cleanly:
  ```bash
  python3 uretim_hatti/test/kos.py
  ```
- [ ] **Linter Validated:** If modifying film plans, `film_dogrula.py` reports zero errors.
- [ ] **Frozen Archives Intact:** No edits made to `kilavuzlar_ve_sistem_dosyalari/` or `AGENTS_ESKI_HAT.md`.
- [ ] **Standard Library Only:** No external pip dependencies introduced (all tools use Python standard library).
- [ ] **Semantic Commit:** Commit message follows versioned Conventional Commits (`feat(v2.x):`, `fix(v2.x):`, etc.).
