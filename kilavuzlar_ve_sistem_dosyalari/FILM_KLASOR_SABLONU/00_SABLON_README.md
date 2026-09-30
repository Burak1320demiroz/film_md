# 🗂️ FİLM KLASÖRÜ ŞABLONU — kopyala, doldur

> **Kural metni burada DEĞİL.** İskeletin tanımı ve format deltaları tek
> yerde durur: `KILAVUZ_REHBERI.md` **§2.0**. Bu klasör o tanımın
> **kopyalanabilir hâlidir** — çelişkide §2.0 kazanır.

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
     <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
```

⛔ **ELLE `cp -r` YAPILMAZ (08.09.2026).** Betik dört işi birden yapar ve
dördü de elle yapılınca kaçıyordu: şablonu kopyalar · dosyaları
`<FILM>_<ROL>.md` yapar · `00_ANALIZ/05_SAHNE_CALISMALARI/` altına ≤8
sahnede sahne başına çalışma dosyası damgalar, >8 sahnede `00_SAHNE_TABLOSU.md`
üretir (14.09.2026) · okuma çizelgesini üretir. Yer tutucuları (`<FILM_ADI>` ·
`<FILM>` · `<NN>`) da o doldurur. Kilit sahneler (HOOK · NOVUM · DORUK · BEDEL ·
FINAL) sonradan `--kilit-sahne <FMT> <FILM> S<nn> <ROL>` ile damgalanır.
`00_HIKAYE_ONAYI.md` kopyası klasörü YENİ REJİME sokar (`prompt_kontrol.py`
㉕-㉚); `--analiz-ekle` eski klasöre onu kopyalamaz.

Sahne sayısı sıralama sırasında değişirse:
```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
     <FORMAT_KLASORU> <FILM_ADI> <YENİ_SAHNE_SAYISI> --sahne-guncelle
```
Var olan çalışma dosyasına DOKUNMAZ, yalnız eksikleri damgalar.

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
| `<FILM>_URETIM_DEFTERI.md` | ⛔ YAZIMDA DEĞİL — üretim sırasında (kart B); klip başına bir satır + teslim satırı | `AGENTS.md` kart B · ⑬ UYUM rubriği |
| `<FILM>_PLAN.md` | akış adım 1-2 | `KILAVUZ_REHBERI` §6 · `TEMA_MUHENDISLIGI` · `ACI_YAYI` |
| `<FILM>_BOLUM_1.md` | akış adım 3 | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` + §5 negatif çekirdek |
| `<FILM>_BOLUM_2.md` | akış adım 3 | aynı |
| `<FILM>_KAPAK.md` | adım 10 (PLAN'dan sonra) — İKİ aday prompt (A·B) + tek deney | `FILM_KAPAGI_KILAVUZU.md` |
| `<FILM>_MUZIK.md` | adım 9 (yazımda taslak) | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 |
| `<FILM>_YAYIN_PAKETI.md` | adım 11 (yazımda taslak) | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` + `apexaic/<platform>/PAKETLEME_SABLONU.md` + `apexaic/CAPRAZ_YAYIN.md` §7 |
| `<FILM>_QA_SPEC.md` | yazım paketinin SON parçası | AGENTS.md Kart A · [D117 · D122 · D141 · D142] |
| `<FILM>_REFERANS_PAKETI.md` | ⚠️ **İSTEĞE BAĞLI** (08.09.2026) | `REFERANS_PAKETI_KILAVUZU.md` §1 |
| `00_ANALIZ/` | 🆕 yazımdan ÖNCE, adım adım | kendi README'si |

---

## 🔬 00_ANALIZ — yazımdan önceki iş

08.09.2026'da eklendi (sahip kararı). Film yazılmadan önce TÜM dersler, TÜM
kılavuzlar ve QA raporları okunur; okunanlar bu filme düşen kilitlere,
kilitler sahne sıralamasına ve uyarı notlarına, uyarılar da sahne başına bir
çalışma dosyasına dönüşür. Altı adım, altı dosya — sırası ve kapıları
`00_ANALIZ/00_ANALIZ_README.md`'de.

⛔ `prompt_kontrol.py`'nin `ATLA` deseni `00_ANALIZ` içeren her yolu atlar.
Klasör adı DEĞİŞTİRİLMEZ; değişirse taslak metinler denetime girer ve
`05_SAHNE_CALISMALARI/` ayrı bir FİLM sayılır.

⚠️ **REFERANS PAKETİ ARTIK ZORUNLU DEĞİL** (08.09.2026 · sahip kararı).
Tetikleyici doğruyken atlanıyorsa PLAN'a tek satır gerekçe yazılır [D74
kalıbı]; sessizce atlanmaz. Yazıldıysa kapı sertliğini korur: onaysız
sayfanın varlığı geçtiği hiçbir sahne üretilmez [D168]. Karşı kayıt duruyor —
D146'nın üç ölçülmüş vakası ve SINKING STAKE'in "çapa yok" kaydı.

⛔ **Boş bırakılan dosya silinmez, `⬜ BEKLİYOR` satırıyla durur.** Var olan
boş dosya görünür borçtur; olmayan dosya borç değil, unutmadır.

---

## Şablonun kendisi denetime girmez

`prompt_kontrol.py` yol içinde `SABLON` geçen her şeyi atlar (`ATLA` deseni).
Yani bu klasör BLOCK üretmez; kopyası üretir.
