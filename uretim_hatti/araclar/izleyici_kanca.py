#!/usr/bin/env python3
"""izleyici ajanının PreToolUse kancası: yalnız ~/film_medya/<FILM>/izleyici*/ altını okutur.

.claude/agents/izleyici.md frontmatter'ından çağrılır; yalnız izleyici çalışırken devrededir.
Girdi: stdin'de kanca JSON'u (tool_name, tool_input.file_path …).
Çıkış 0 = izin · 2 = engel (sebep stderr'e). Gerekçe: izleyici planı görürse "bilmeyen
seyirci" testi geçersizdir (uretim_hatti/ELESTIRI_PROTOKOLU.md · AJAN_GOREVLERI izleyici).
"""
import json
import sys
from pathlib import Path

IZINLI_KOK = Path.home() / "film_medya"


def main():
    try:
        veri = json.load(sys.stdin)
    except json.JSONDecodeError:
        print("izleyici kancası: girdi okunamadı — okuma engellendi", file=sys.stderr)
        return 2
    yol = (veri.get("tool_input") or {}).get("file_path") or ""
    try:
        p = Path(yol).expanduser().resolve()
        goreli = p.relative_to(IZINLI_KOK.resolve())
    except (ValueError, OSError):
        print(f"izleyici yalnız ~/film_medya/<FILM>/izleyici*/ altındaki kareleri okuyabilir: {yol}",
              file=sys.stderr)
        return 2
    parcalar = goreli.parts
    if len(parcalar) >= 3 and parcalar[1].startswith("izleyici"):
        return 0
    print(f"izleyici yalnız ~/film_medya/<FILM>/izleyici*/ altındaki kareleri okuyabilir: {yol}",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
