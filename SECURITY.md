# Security Policy

## Supported Versions

We provide security updates and patches for the following versions of the `film_md` production pipeline:

| Version | Supported | Status |
|---|:---:|---|
| **2.0.x** (Current Hat v2) | :white_check_mark: | Actively supported and maintained |
| < 2.0.0 (Legacy Pipeline) | :x: | Frozen archive; no security updates |

---

## Reporting a Vulnerability

The `film_md` team and **Apex AI Cinema** take the security and integrity of our codebase, tools, and developer environments seriously.

If you discover a security vulnerability or sensitive information exposure in this repository, please do **NOT** open a public issue. Instead, report it privately through one of the following channels:

1. **GitHub Private Vulnerability Reporting:**
   Use GitHub's built-in private reporting feature by navigating to **Security** -> **Advisories** -> **Report a vulnerability**.
2. **Direct Contact:**
   Contact the repository maintainer directly via GitHub profile messaging or email at `burakdemiroz@gmail.com` (or the email linked on the GitHub profile).

### Scope of Security Concerns
- **API Key & Secret Leaks:** Exposure of LLM provider keys (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`), YouTube Data API credentials, or cloud access tokens.
- **Command Injection & Path Traversal:** Unsanitized arguments or subprocess invocations inside CLI tools (`film_dogrula.py`, `kurgu.py`, `kareler.py`, `medya.py`).
- **Sandbox Bypasses:** Circumvention of filesystem isolation hooks (such as `uretim_hatti/araclar/izleyici_kanca.py`).

### What to Include in Your Report
To help us resolve the issue swiftly, please include:
- A clear description of the vulnerability.
- Steps to reproduce or proof-of-concept (PoC).
- Potential impact and affected files or commands.
- Any suggested remediations.

### Response Timeline
- **Initial Acknowledgement:** Within 48 hours.
- **Triage & Status Update:** Within 5 business days.
- **Resolution & Disclosure:** A patch will be published alongside an advisory once verified.

Thank you for responsibly disclosing vulnerabilities and keeping the AI cinema production ecosystem secure.
