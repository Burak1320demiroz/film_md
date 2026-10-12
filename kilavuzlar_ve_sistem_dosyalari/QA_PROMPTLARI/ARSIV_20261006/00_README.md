# 🗄️ ARŞİV — 15 mercek + üç geçişli QA (06.10.2026)

> **Sahip kararı, 06.10.2026:** eski QA promptları arşive alındı. Yeni hat 4 QA promptuyla devam ediyor:
> `uretim_hatti/QA_PROMPTLARI/`.
> - Gemini için: TARAMA (klip içi) · SUREKLILIK (kesmenin iki yanı) · ANLATIM_TESTI (plansız izleyici).
> - İnsan için: IZLEME_FORMU.
>
> Dosyalar silinmedi, değiştirilmedi; yalnız `git mv` ile buraya taşındı.

| Burada | Eskiden |
|---|---|
| `_KAYNAK/` (1-15 mercek + `1_KARE_DIKEY_EK.md`) | `QA_PROMPTLARI/_KAYNAK/` |
| `UC_GECISLI_QA/` | `QA_PROMPTLARI/UC_GECISLI_QA/` |

## Neden

- **Yeni hatla uyumsuz:** 15 merceğin 15'i filmin `<FILM>_QA_SPEC.md` dosyasına dayanıyordu; yeni hat bu dosyayı üretmiyor.
- **Sonuç zayıf:** 725 mercek raporunun %11'i GO. 12 filmin 698 tekil bulgusunun %31'i QA yanılgısıydı.
  - ⑫ HOOK: yanılgı %91.
  - ⑩ OYUNCULUK: yanılgı %60.
  - ⑬ UYUM: 5 koşunun 5'i yarım; bir kez bile sonuç vermedi.
- **Pahalı:** 16 dakikalık bir film 60 ayrı Gemini sohbeti istiyordu. Rubrikler 13-25 KB'tı; modelin kendi aritmetiği tutmadı.
- **Kör nokta:** Gemini videoyu saniyede 1 kareyle okur. 1 saniyeden kısa kusuru hiçbir mercek güvenilir yakalayamazdı.
- Ölçüm: `uretim_hatti/ARASTIRMA/02_SUZME_20261006.md` (R5) ve 06.10.2026 oturum analizi.

## Merceklerin yeni karşılığı

| Eski | Yeni |
|---|---|
| ① kare · ② klip içi · ⑥ fizik · ⑦ aksiyon · ⑧ efor · ⑨ kadraj · ⑭ hareket | TARAMA (T1-T14; kare modu) |
| ② kesmeler arası · ⑤ arka plan · ⑪ ışık · ⑮ yön | SUREKLILIK (S1-S7) |
| ④ hikâye · ⑫ hook · ③ diyalog anlaşılırlığı | ANLATIM_TESTI (+ dramaturg, izleyici ajanı) |
| ⑩ oyunculuk · ③ ses dengesi | IZLEME_FORMU (insan) + `kurgu.py yukseklik` |
| ⑬ uyum (prompt ↔ ekran) | Kaldırıldı. Yerine rapor-prompt karşılaştırma skill'i gelecek (sahip kararı) |

## Bilinen etki

- **Eski araçlar:** `sayac.sh` "rubrik hacmi" satırı bu klasörü okuyacak biçimde tek satırda güncellendi. `rapor_kontrol.py`'deki "_KAYNAK/ rubriği" mesajı yalnız metindir, kod bağlantısı yok.
- **Eski belgeler:** donmuş eski hat skill'leri (`qa-isle`, `yeni-film/ESKI_HAT_SKILL.md`) ve eski README'ler `_KAYNAK/` yolunu anar. Eski hat donduğu için düzeltilmedi; eski bir raporu yeniden üretmek gerekirse yol buradadır.
