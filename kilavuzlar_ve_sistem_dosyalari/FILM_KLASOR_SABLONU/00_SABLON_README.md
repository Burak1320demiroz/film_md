# 🗂️ FİLM KLASÖRÜ ŞABLONU — kopyala, doldur

> **Kural metni burada DEĞİL.** İskeletin tanımı ve format deltaları tek
> yerde durur: `KILAVUZ_REHBERI.md` **§2.0**. Bu klasör o tanımın
> **kopyalanabilir hâlidir** — çelişkide §2.0 kazanır.

```bash
cp -r kilavuzlar_ve_sistem_dosyalari/FILM_KLASOR_SABLONU <FORMAT_KLASORU>/<FILM_ADI>
cd <FORMAT_KLASORU>/<FILM_ADI> && rm 00_SABLON_README.md
for f in FILM_*.md; do mv "$f" "<FILM_ADI>${f#FILM}"; done
```

Sonra dosya başlarındaki `<FILM_ADI>` yer tutucularını doldur.

---

## Neden şablon bir KLASÖR, tarif değil

Bu depo aynı dersi iki kez ödedi: **D117** — QA SPEC planın içinde bir
*bölüm* olarak yazılıyordu ve dokuz filmde bir kez bile mod D koşulmadı;
SPEC ayrı bir **dosyaya** çıkarılınca koşuldu. Nesre yazılmış yapı
uygulanmıyor, kopyalanabilir yapı uygulanıyor.

---

## Dosyalar ve sahipleri

| Dosya | Ne zaman yazılır | Kaynak kılavuz |
|---|---|---|
| `<FILM>_PLAN.md` | akış adım 1-2 | `KILAVUZ_REHBERI` §6 · `TEMA_MUHENDISLIGI` · `ACI_YAYI` |
| `<FILM>_BOLUM_1.md` | akış adım 3 | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` + §5 negatif çekirdek |
| `<FILM>_BOLUM_2.md` | akış adım 3 | aynı |
| `<FILM>_KAPAK.md` | adım 10 (yazımda taslak) | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` |
| `<FILM>_MUZIK.md` | adım 9 (yazımda taslak) | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 |
| `<FILM>_YAYIN_PAKETI.md` | adım 11 (yazımda taslak) | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` + `apexaic/<platform>/PAKETLEME_SABLONU.md` + `apexaic/CAPRAZ_YAYIN.md` §7 |
| `<FILM>_QA_SPEC.md` | yazım paketinin SON parçası | AGENTS.md Kart A · [D117 · D122 · D141 · D142] |

⛔ **Boş bırakılan dosya silinmez, `⬜ BEKLİYOR` satırıyla durur.** Var olan
boş dosya görünür borçtur; olmayan dosya borç değil, unutmadır.

---

## Şablonun kendisi denetime girmez

`prompt_kontrol.py` yol içinde `SABLON` geçen her şeyi atlar (`ATLA` deseni).
Yani bu klasör BLOCK üretmez; kopyası üretir.
