# ⛔ COMMIT ATMAN YASAK

Bu depoda commit ve push'u **sadece proje sahibi** atar.

Uygulama (05.08.2026):
- `.claude/settings.json` → `permissions.deny` içinde `git commit` ve `git push`
  engellendi. Ajan bu komutları çalıştıramaz.
- `AGENTS.md` §5 güncellendi: görev kartlarındaki "commit" adımı
  "işi commit'e hazır bırak" anlamına gelir.

Ajan işi bitirince: değişen dosyaları listeler, önerilen commit mesajını yazar,
commit'i sahibine bırakır.
