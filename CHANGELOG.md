# Changelog

All notable changes to the **film_md** production pipeline are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<p align="left">
  <a href="https://keepachangelog.com/en/1.0.0/"><img alt="Keep a Changelog" src="https://img.shields.io/badge/changelog-Keep%20a%20Changelog%20v1.0.0-E8F7FF?style=flat-square&labelColor=05080E"></a>
  <a href="https://semver.org/spec/v2.0.0.html"><img alt="Semantic Versioning" src="https://img.shields.io/badge/semver-2.0.0-7FD8FF?style=flat-square&labelColor=05080E"></a>
  <a href="https://www.conventionalcommits.org/"><img alt="Conventional Commits" src="https://img.shields.io/badge/commits-Conventional%20Commits-2E9BD6?style=flat-square&labelColor=05080E"></a>
  <a href="https://github.com/Burak1320demiroz/film_md/releases"><img alt="GitHub Releases" src="https://img.shields.io/badge/release-v2.0.0-00E5FF?style=flat-square&labelColor=05080E"></a>
</p>

---

## Quick Navigation

- [Unreleased](#unreleased)
- [2.0.0 — 2026-10-22 (Hat v2: Autonomous Agentic Pipeline)](#200--2026-10-22)
- [1.0.0 — 2026-10-05 (Hat v1: The Foundational 125-Film Archive)](#100--2026-10-05)
- [Migration Guide: Upgrading from v1.x to v2.x](#migration-guide-upgrading-from-v1x-to-v2x)
- [Release Cadence & Versioning Policy](#release-cadence--versioning-policy)

---

## [Unreleased]

### Planned
- **Web UI & Dashboard**: Lightweight, local web-based timeline and prompt inspector (`araclar/gorsel_denetim.py`).
- **ComfyUI Local Bridge**: Direct node bridge for generating turnaround reference panels without external web interfaces.
- **Multilingual Subtitle Compiler**: Automated subtitle timing and translation compiler based on `timeline.json` dialogue offsets.

---

## [2.0.0] - 2026-10-22

### 🚀 Major Architecture Overhaul (Hat v2 Launch)

**film_md v2.0.0** marks the transition from static markdown rulebooks to an **autonomous, docs-as-code multi-agent production studio**. Based on empirical data from 5 pilot films and 876 Gemini analytical reports (`ARASTIRMA/16`), Hat v2 eliminates rule proliferation, solves audio/visual continuity, and introduces deterministic shot timing and in-video model dialogue.

### 💥 Breaking Changes

- **Deprecated Prompt Continuity Chaining**: The legacy prompt phrasing `"continues the previous clip"` has been completely banned. Video clips are now linked via **physical keyframe visual images** (Keyframe $B$ of shot $n$ becomes starting frame $A$ of shot $n+1$, with $\le 4$ links per chain).
- **In-Video Model-Voiced Dialogue**: Post-production voice-over and dialogue dubbing have been replaced with **in-video model-generated speech** using Google Flow Omni Flash 1.1 (`DIYALOG model sesi`). Prompts must contain the verbatim line enclosed in quotation marks.
- **Strict 10.0-Second Shot Mathematics**: Every shot in the timeline is strictly 10.0 seconds. The number of shots is deterministic:
  $$\text{Total Shots} = \frac{\text{Target Duration (seconds)}}{10}$$
  *(2 min $\rightarrow$ 12 shots, 4 min $\rightarrow$ 24 shots, 8 min $\rightarrow$ 48 shots, 16 min $\rightarrow$ 96 shots).*
- **Single Reference Sheet Invariant**: Multiple loose facial or costume crops have been consolidated into **one multi-view panel per subject** (`ref/<No>.<NAME>_v1.png`) featuring front, side, back, 3/4, close-up, and material callouts.
- **Sub-Agent Call Budget Cap**: Every film is capped at **50 agent invocations** (maximum 30 calls across text phases F1–F6, leaving at least 20 calls reserved for the F3p pilot and production phases F7–F9).
- **Elimination of Subjective AI Scoring**: Numeric scores (e.g., "Story: 8.5/10") have been completely replaced with **evidence-based critique protocols** requiring exact timecodes, frame evidence, and severity tags (`ÖLÜMCÜL` / `CİDDİ` / `ÖNERİ`).

### ✨ Added

#### Autonomous Sub-Agent System (`.claude/agents/`)
- **18 Specialized Sub-Agents**:
  - **Producer**: `fable` (Orchestrator & Delivery Owner), `denetci` (Gate Auditor), and `medya.py` CLI integration.
  - **Narrative**: `senarist` (Screenplay), `diyalog-yazari` (Dialogue), and `dramaturg` (Story Structure & Climax).
  - **Directing**: `yonetmen` (Director & Shot Lists), `sahneleyici` (Staging & Keyframes), and `mekan-haritacisi` (Spatial Topology).
  - **Visual Generation**: `goruntu-yonetmeni` (Cinematographer & Video Prompts, Pilot, Redesign).
  - **Editing & Audio**: `kurgucu` (Editor & Timeline Assembly), `ses-tasarimcisi` (Sound Designer & Room-Tone Beds), and `besteci` (Music Prompts).
  - **Packaging**: `kapak-tasarimcisi` (YouTube Thumbnail Designer) and `yayin` (English Metadata & SEO).
  - **Independent Verification**: `izleyici` (Blind Audience Test), `devamlilik` (Continuity Inspector), `teknik-danisman` (Physics & Model Risk), `zincir-bekcisi` (Keyframe Stitch Auditor), and `bilim-danismani` (Hard Sci-Fi Scientific Accuracy).
- **Physical Audience Sandboxing (`araclar/izleyici_kanca.py`)**:
  - Implements filesystem-level read isolation: the `izleyici` agent is physically prevented from reading the script, director's notes, or plot outlines, ensuring authentic blind viewer testing.

#### Production CLI Suite (`uretim_hatti/araclar/`)
- **`film_dogrula.py`**:
  - Automated linter validating contract invariants, character count limits ($\le 4,300$ chars), temporal beat continuity (`0-3s ... 3-7s ... 7-10s`), in-video dialogue, and English publishing kits.
- **`kurgu.py`**:
  - Automated timeline assembler from `timeline.json`.
  - Broadcast loudness normalizer implementing EBU R128 / ITU-R BS.1770-4 standards ($-14\text{ LUFS}$, $\le -1\text{ dBTP}$).
  - Video cut transition renderer (hard cut, 0.3–0.8s `xfade`, 0.5–1.5s fade-to-black).
- **`kareler.py`**:
  - Contact sheet synthesizer and SSIM / PSNR seam continuity checker.
  - Multi-surface YouTube thumbnail inspector simulating mobile, desktop, and sidebar resolutions (360×202, 168×94, 120×68).
- **`medya.py`**:
  - Two-way media ledger synchronizing physical video assets in `~/film_medya/<FILM>/` with repo metadata (`DURUM.md`, `NOTLAR.md`).
  - Automated take hashing, generation parameter logging, and cut extraction (`medya.py bol`).

#### 3-Layer Audio-Visual Continuity Engine
- **Layer 1 (Visual)**: Shared visual identity sentence and illumination sentence repeated verbatim across prompt groups.
- **Layer 2 (Audio)**: Unbroken location room-tone beds (`yataklar`) running continuously across clip cuts with J/L sound overlaps.
- **Layer 3 (Edit)**: Mathematically timed timeline transitions ensuring visual stability across scene boundaries.

#### F3p Early Pilot Phase
- Mandatory physical generation of 1–3 high-risk shots (opening hook, complex mechanical interaction, or character speech) in Google Flow before writing full-film prompt manifests.

#### Quality & Testing Infrastructure
- **Automated Regression Suite (`uretim_hatti/test/kos.py`)**:
  - 46 comprehensive unit and integration test suites covering linters, audio normalizers, media parsers, and invariant checkers with 100% pass rate.
- **Continuous Integration (`.github/workflows/ci.yml`)**:
  - Automated GitHub Actions pipeline verifying Python 3 compatibility, running `kos.py`, running `film_dogrula.py` on flagship films, and enforcing the zero-media-in-repo invariant.

#### Community & Open Source Governance
- **Documentation Overhaul**:
  - Bilingual `README.md` (English & Turkish) with full architecture breakdown, visual workflows, and catalog navigation.
  - 8 cinematic 2.39:1 widescreen production stills, contact sheets, and terminal logs in `images/readme_*.png`.
  - Standardized governance docs: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff`, and issue/PR templates.

### 🔄 Changed

- Replaced monolithic prompt scripts with lightweight modular tools using only Python standard library and `ffmpeg`.
- Replaced ambiguous narrative beats with temporal 2–4 phase movement arcs (`0-3s`, `3-7s`, `7-10s`) ensuring that ending beats do not freeze.
- Updated all reference prompts to strictly follow the prefix schema: `"Reference <No> (<role>): ..."`.
- Migrated all git commit conventions to versioned Conventional Commits (`release(v2.0.0): ...`).

### 🛡️ Verification & Metrics

- **Regression Tests**: 46/46 passing (`python3 uretim_hatti/test/kos.py`).
- **Broadcast Audio**: Verified $-14.0\text{ LUFS} \pm 0.5$ and $\le -1.0\text{ dBTP}$ true peak compliance.
- **Zero Media Invariant**: Fully verified; binary media strictly isolated in `~/film_medya/` outside git tracking.

---

## [1.0.0] - 2026-10-05

### 🚀 Foundational Release (Hat v1 Archive)

The initial release of **film_md**, documenting the foundational methods, scripts, and analytical archives developed during the production of 121 original sci-fi short film plans.

### ✨ Added

- **121 Short Film Plans**:
  - Full production plans across 2-minute (12 shots), 4-minute (24 shots), 8-minute (48 shots), 16-minute (96 shots), and 32-minute formats.
  - Complete prompt manifests, character dossiers, and scene breakdowns.
- **63 Production Manuals (~27,000 lines)**:
  - Deep-dive technical guides on spacesuit kinematics, cockpit ergonomics, relativistic physics, camera lenses, lighting ratios, and narrative pacing (`kilavuzlar_ve_sistem_dosyalari/`).
- **QA Analysis Archive**:
  - **876 Raw QA Reports**: Analytical reports evaluating produced films across 15 Gemini analytical lenses (`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/`).
  - **77 Film-Level Synthesis Reports**: Aggregated structural diagnoses.
  - **D217 Empirical Failure Lessons**: Catalogued edge cases and prompt failure modes.
- **Monolithic Prompt Checker**:
  - Initial 2,950-line Python validation script (`film_dogrula_eski.py`).
- **Published Portfolio**:
  - 225 video releases deployed to the Apex AI Cinema YouTube channel.

### ❄️ Deprecated & Archived

- **Monolithic Rule System**: Frozen and archived to `kilavuzlar_ve_sistem_dosyalari/ARSIV/`.
- Rule proliferation policy replaced by Hat v2 root-cause isolation.

---

## Migration Guide: Upgrading from v1.x to v2.x

1. **Shot Structure**:
   - *v1.x*: Variable shot lengths (4s, 6s, 8s) with unstructured prompt descriptions.
   - *v2.x*: Every shot must be exactly 10s with explicit beat timestamps (`0-3s: ... 3-7s: ... 7-10s: ...`). Total shots must equal $\text{Duration} / 10$.
2. **Dialogue Handling**:
   - *v1.x*: Script dialogue intended for post-production voice-over recording.
   - *v2.x*: Script dialogue marked as `DIYALOG model sesi` and embedded directly inside the video prompt in quotation marks.
3. **Reference Sheets**:
   - *v1.x*: Multiple image files per character (face, suit, action).
   - *v2.x*: Single turnaround sheet per subject (`ref/<No>.<NAME>_v1.png`) with uniform number tags.
4. **Validation Tooling**:
   - Run `python3 uretim_hatti/araclar/film_dogrula.py <FILM>` instead of legacy checker scripts.
   - Note: Legacy films without numbered references are processed with compatibility warnings (`⚠️`).

---

## Release Cadence & Versioning Policy

- **Major Releases (X.0.0)**: Major architectural redesigns, schema overhauls, or breaking production rule changes.
- **Minor Releases (x.Y.0)**: New sub-agents, new production CLI features, new film format templates, or guideline updates.
- **Patch Releases (x.y.Z)**: Bug fixes in CLI tools (`film_dogrula.py`, `kurgu.py`, `medya.py`), test suite enhancements, or documentation corrections.

---

[Unreleased]: https://github.com/Burak1320demiroz/film_md/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/Burak1320demiroz/film_md/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/Burak1320demiroz/film_md/releases/tag/v1.0.0
