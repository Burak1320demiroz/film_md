# Contributing to film_md

Thank you for your interest in contributing to **film_md** (the production system behind **Apex AI Cinema**)!

`film_md` is an agentic, docs-as-code production pipeline for photoreal AI science-fiction short films. Because this repository acts as a deterministic build system for creative film projects, all contributions must respect our established production discipline and architectural invariants.

---

## Invariant Rules (Non-Negotiable)

Before submitting any Pull Request or proposing changes, you must review and adhere to the invariant rules defined in [`AGENTS.md`](AGENTS.md):

1. **No Media in Git (Strictly Text Only):**
   - Images, video clips, and audio tracks **never enter this repository**.
   - All production assets reside outside git in `~/film_medya/<FILM>/`.
   - `.gitignore` strictly rejects media files.
   - *Sole exception:* Essential documentation assets located in `images/readme_*.png`.
2. **Frozen Archives are Read-Only:**
   - Legacy directories (`kilavuzlar_ve_sistem_dosyalari/`), historical QA reports (`FILM_QA_RAPORLARI/`), and `AGENTS_ESKI_HAT.md` are frozen historical records. Do not modify, reformat, or delete them.
3. **An Error Does Not Become a Rule:**
   - In-production failures are recorded in the film's `NOTLAR.md`.
   - New pipeline rules are not created on a whim; they require documented, reproducible recurrence across at least two distinct films and sign-off from the repository owner.
4. **Owner Merge & Commit Authority:**
   - The repository owner holds sole commit and merge authority. Automated agents do not commit directly to the repository.

---

## How to Contribute

### 1. Tooling & Test Suite Improvements
Our CLI tools live in `uretim_hatti/araclar/` and use **only Python 3 standard library** (plus `ffmpeg`/`ffprobe` for audio-video operations):
- `film_dogrula.py`: Structure linter for shot counts, 10s beat plans, and model-voiced lines.
- `kurgu.py`: Edit decision list compiler, transitions (`xfade`), and broadcast loudness mastering (-14 LUFS).
- `kareler.py`: Contact sheet generator, seam SSIM/PSNR stitch analyzer, and YouTube thumbnail inspector.
- `medya.py`: Physical media synchronization with `DURUM.md` ledgers.

### 2. Expanding Test Coverage
All automated regression tests live in `uretim_hatti/test/kos.py`. Any bug fix or new tool feature must be accompanied by an automated test case.

### 3. Error Atlas & Research
Contributions to `uretim_hatti/PROMPT_HATA_ATLASI.md`, `uretim_hatti/BILINEN_TUZAKLAR.md`, or deep research digests in `uretim_hatti/ARASTIRMA/` are welcome if supported by empirical model testing.

---

## Development & Verification Workflow

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Burak1320demiroz/film_md.git
   cd film_md
   ```

2. **Verify system dependencies:**
   - Python 3.10+ (standard library only)
   - `ffmpeg` and `ffprobe` (for media tools)

3. **Run the test suite:**
   All 46 regression tests must pass without errors:
   ```bash
   python3 uretim_hatti/test/kos.py
   # Expected output: 46/46 test geçti
   ```

4. **Lint an existing film folder:**
   ```bash
   python3 uretim_hatti/araclar/film_dogrula.py yatay_4_dk_filmler/THE_MAYDAY_SEA
   ```

---

## Commit Message & Versioning Standards

We follow [Semantic Versioning](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/) tagged with the pipeline version:

```text
<type>(<version or scope>): <short summary>

[optional body]

[optional footer]
```

### Commit Types
- `feat(v2.x)`: A new feature or tool enhancement
- `fix(v2.x)`: A bug fix in tooling or linter logic
- `docs(v2.x)`: Documentation updates or new guides
- `test(v2.x)`: Adding or updating regression tests in `test/kos.py`
- `refactor(v2.x)`: Code restructuring without changing functionality
- `release(v2.0.0)`: Version bumps and release snapshots

### Examples
- `feat(v2.0): add SSIM edge drift detection to kareler.py`
- `fix(v2.0): prevent false alarm in film_dogrula for negative prompt clauses`
- `docs(v2.0): add bilingual README and 3-layer continuity diagram`
- `test(v2.0): add regression test for model-voiced dialogue quotes`

---

## Pull Request Checklist

Before opening a Pull Request, ensure that:
- [ ] No binary media files (`.mp4`, `.wav`, `.png`, `.jpg`) have been added outside `images/readme_*.png`.
- [ ] `python3 uretim_hatti/test/kos.py` passes all 46 tests cleanly.
- [ ] No modifications were made to frozen legacy folders (`kilavuzlar_ve_sistem_dosyalari/`).
- [ ] All code conforms to Python 3 standard library (no external pip dependencies).
- [ ] Commit messages follow the version-tagged conventional commit convention.

Thank you for helping push the boundaries of agentic, docs-as-code cinema!
