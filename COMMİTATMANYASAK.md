# ⛔ COMMIT ATMAN YASAK

Bu depoda commit ve push'u **sadece proje sahibi** atar.

Uygulama (05.08.2026):
- `.claude/settings.json` → `permissions.deny` içinde `git commit` ve `git push`
  engellendi. Ajan bu komutları çalıştıramaz.
- `AGENTS.md` §5 güncellendi: görev kartlarındaki "commit" adımı
  "işi commit'e hazır bırak" anlamına gelir.

Ajan işi bitirince: değişen dosyaları listeler, önerilen commit mesajını yazar,
commit'i sahibine bırakır.

---

# ⭐ 30.09.2026 · YASAK LİSTESİ GENİŞLETİLDİ — asıl risk commit değil, GERİ ALMA

05.08'in iki satırı yalnız **yayını** kapatıyordu. Ölçüm şunu gösterdi: bu deponun
her anki değeri **commit'lenmemiş** iştir, ve onu yok eden komutlar açıktaydı.

```
KANIT  THE_LAST_GATE (30.09.2026): 31 .md dosyası · 96 klip · 184 prompt · 0 commit.
       Kart A'nın bitiş hâli tanımı gereği budur — "iş commit'e HAZIR bırakılır".
       Yani filmin tamamı, her zaman, yalnız çalışma ağacında durur.
⭐ GERİ DÖNÜŞ YOK  Claude Code'un oturum checkpoint'i kendi metninde
       "bash-made changes excluded" diyor. Bu deponun filmleri python üreteçleri
       ve heredoc'larla yazılıyor (emsal: 00_ANALIZ/06_PROMPT_URETECI) — yani
       üretilen dosyaların çoğu checkpoint kapsamının DIŞINDA.
       Sonuç: `git reset --hard` tek satırda 31 dosyayı siler ve hiçbir mekanizma
       geri getirmez. Yedek yoktur, çünkü yedek = commit ve commit yasaktır.
```

İki öbek eklendi:

```
① YAYIN (sahibin tekeli)      commit · push · tag · remote · gh
   + git -C · git --git-dir · git --work-tree
     ⛔ NEDEN: `Bash(git commit*)` bir ÖN EK eşleştiricisidir; `git -C <yol> commit`
        onu atlar. Üçü de bu depoda hiç kullanılmıyor (30.09 ölçümü) — kapatmak bedava.
② GERİ DÖNÜŞSÜZ KAYIP         reset · checkout · restore · clean · stash
     clean → takipsiz dosyalar = YENİ film klasörünün TAMAMI
     stash → sinsi olanı: hata vermez, ağacı temizler
```

**Yıkıcı olmayan alternatifler** (ajan bunları kullanır, yasak değiller):

```
eski sürüme bakmak   git show <ref>:<yol>        ⛔ git checkout DEĞİL
farkı görmek         git diff · git status
dosya silmek         rm <yol>  → sahip commit'ler  ⛔ git rm DEĞİL
```

**Ölçülen davranış (30.09.2026):** `permissions.deny` **anında** etkindir ve
`bypassPermissions` kipini de ezer — `git remote -v` denenip
`Permission to use Bash ... has been denied` alındı; `git status` ve `git show`
bozulmadı. Yeni oturum beklemek gerekmiyor.

⚠️ **Dürüst sınır:** deny bir ön ek eşleştiricisidir, kasa değil. Emniyet kemeridir;
**asıl kapı hâlâ yazılı kuraldır** [D74 ruhu: kaydı olmayan kapı, koşulmamış kapıdır].
Sahibin kendi terminali bu listeden etkilenmez.

🔧 **Listeden bir satır yolunuza çıkarsa:** `.claude/settings.json` →
`permissions.deny` dizisinden o satır silinir. Gerekçesi buraya yazılır.
