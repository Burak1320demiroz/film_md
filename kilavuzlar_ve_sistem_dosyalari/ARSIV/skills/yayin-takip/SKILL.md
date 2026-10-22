---
name: yayin-takip
description: Yayın öncesi kimlik satırı + 24/48/72 saat metrik işleme + geri besleme (AGENTS.md Kart Y). Girdi: film adı ($1) ve evre ($2 = once | 24 | 48 | 72 | geri-besleme).
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(bash:*)
---

# Kart Y — Yayın takibi

Kılavuz: `kilavuzlar_ve_sistem_dosyalari/YAYIN_VE_PERFORMANS_KILAVUZU.md`
Tablo: `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md`
Çelişkide AGENTS.md Kart Y + kılavuz kazanır.

⛔ **ZAMAN KURALI** (bu skill'in var olma sebebi): satır YAYINDAN ÖNCE açılır.
Kullanıcı "film dün çıktı, kaydı şimdi açalım" derse satır ancak 🚨 GEÇERSİZ
işaretiyle açılır ve bu kendisine açıkça söylenir — hangi kapak, hangi başlık,
hangi hook tipi sonradan hatırlanarak yazılamaz.

⛔ **ONAY KURALI**: tabloya satır yazmadan önce doldurulacak alanlar kullanıcıya
özet olarak gösterilir; kullanıcı onaylamadan yazılmaz. (Bu kural gövdededir,
çünkü YAML kısıtları tek başına güvence değildir.)

Girdi `$2` evresine göre üç bölümden biri koşulur:

## `once` — yayından önce
- 08 tablosu §1 kimlik satırı doldurulur (kapak · başlık · hook tipi · seri).
- Plan B kapağı hazır mı → `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §7.2.
- ⛔ TEK DEĞİŞKEN KİLİDİ: ilk 48 saatte kapak VEYA başlık değişebilir —
  İKİSİ DEĞİL. Hangisinin seçildiği satıra ve kullanıcıya yazılır.
- Seri/playlist kararı: `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` §5.1
  (bir film yalnız TEK resmi seride yer alır).

## `24` / `48` / `72` — metrik işleme
- Kılavuz §2 metrik satırı · §3 eğri teşhisi · §4 karar satırı.
- ⭐ Terk saniyesi SAHNEYE ızgara aritmetiğiyle çevrilir:
  `sahne başlangıcı(n) = hook + (n−1) × klip` (ortak adım ⑨ ile aynı formül).
  Elle sahne tahmini yapılmaz.
- Suçlu değişken eleme sırası (ucuzdan pahalıya):
  paketleme → kurgu → ses → sahne → plan → format.

## `geri-besleme` — 72 saatten sonra, kartın var olma sebebi
- Kılavuz §6 tablosundan hangi BELGENİN revize edileceği bulunur.
- ⛔ SIRA: veri → belge revizyonu → (ancak tekrarlarsa) ders.
  Yeni ders yazmak ilk refleks DEĞİLDİR.
- ⭐ QA skoru yüksek + gerçek metrik düşük → yanlış olan RUBRİKTİR →
  `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md`.
- Devam adaylığı: `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` §4.2
  (üç filmde ölçülmeden tam kapıya geçilmez).

## Bitiş
- Satır geçerlilik işareti taşır: ✅ / ⚠️ / 🚨.
- Commit ATILMAZ — "commit'e hazır" diye raporlanır.
