# Third-party notices

The original work in this repository is released under the MIT License (see [`LICENSE`](LICENSE)).
The five skills listed below were written by other authors and **are not covered by that license**.
Each one keeps its own license, and a copy of that license sits next to its files.
Sources and content hashes of the installed skills (`image`, `video`) are recorded in [`skills-lock.json`](skills-lock.json). The three marketingskills skills were archived on 21.10.2026: they are no longer installed, but their files and licenses are kept in the repository.

| Skill | Path | Source | License | Copyright | Local changes |
|---|---|---|---|---|---|
| `ab-testing` | `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/ab-testing/` (archived 21.10.2026) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | © 2025 Corey Haines | none recorded |
| `content-strategy` | `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/content-strategy/` (archived 21.10.2026) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | © 2025 Corey Haines | none recorded |
| `social` | `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/social/` (archived 21.10.2026) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | © 2025 Corey Haines | none recorded |
| `image` | `.claude/skills/image/` | [smixs/visual-skills](https://github.com/smixs/visual-skills) | CC BY 4.0 | © 2026 Serge Shima | **modified**, see below |
| `video` | `.claude/skills/video/` | [smixs/visual-skills](https://github.com/smixs/visual-skills) | CC BY 4.0 | © 2026 Serge Shima | **modified**, see below |

## coreyhaines31/marketingskills (MIT)

The full MIT license text, including the copyright notice, is in:
- `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/ab-testing/LICENSE`
- `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/content-strategy/LICENSE`
- `kilavuzlar_ve_sistem_dosyalari/ARSIV/skills/social/LICENSE`

## smixs/visual-skills (CC BY 4.0)

**Attribution:** Serge Shima — https://t.me/aimastersme · https://sergeshima.com · https://aimasters.me
**Source:** https://github.com/smixs/visual-skills
**License:** [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

Each folder includes two files from the upstream repository, copied verbatim: the full license text (`LICENSE`) and the author's `NOTICE`. The `NOTICE` also credits [agentara/skills](https://github.com/agentara/skills) (MIT).
- `.claude/skills/image/LICENSE` and `.claude/skills/image/NOTICE`
- `.claude/skills/video/LICENSE` and `.claude/skills/video/NOTICE`

**Changes made in this repository (30.09.2026):** in both `SKILL.md` files, `disable-model-invocation: true` was added to the frontmatter, and a short Turkish note ("YEREL DEĞİŞİKLİK") was placed above the body to explain why. The skills now run only when called by name (`/image`, `/video`). They no longer trigger by themselves. Apart from these two changes, the files are kept as they were installed. Upstream has been updated since then, so this copy is an older version. Every file in `references/` still ends with its author line.

## Names and marks

The MIT License covers code and text. It does not grant rights to the channel name **Apex AI Cinema / APEXAIC**, the **Λ** mark or the `images/readme_logo.png` logo. You may use the name to describe where the project came from. Do not use it in a way that suggests your work is the channel's own or is endorsed by it.

## Services mentioned

Claude Code, Google Flow (Veo, Gemini Omni, Flow Music), Gemini and YouTube are named only to describe the workflow. None of their code, models or media is included here. Their names belong to their owners.
