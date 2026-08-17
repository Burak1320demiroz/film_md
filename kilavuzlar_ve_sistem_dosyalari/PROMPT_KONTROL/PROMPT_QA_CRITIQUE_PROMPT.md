# 🔎 PROMPT QA — ÜRETİM ÖNCESİ DENETİM RUBRİĞİ

> **Ne zaman:** Promptlar yazıldı, **tek kare üretilmedi.**
> **Girdi:** Bir filmin prompt dosyası (veya tek sahnenin IMAGE+VIDEO çifti).
> Başka hiçbir şey verilmez — bu rubrik tek dosya çalışır.
> **Çıktı:** `GO` / `FIX` / `BLOCK`. BLOCK ise üretme.
>
> ⛔ **Bu rubrik SAYMAZ.** Karakter uzunluğu, yasak kelime taraması, negatif
> çekirdek imzası ve sahne sayısı tutarlılığı betiğin işidir:
> `python3 prompt_kontrol.py <dosya>`
> Betik koşulmadan bu rubrik çalıştırılmaz — ikisi aynı şeyi ölçmez.
> Burada ölçülen tek şey, grep'in göremediği şey: **kilit gerçekten
> kilitliyor mu.**

---

# STEP 0 — KAPI

```
□ prompt_kontrol.py koşuldu mu?      hayır → ÖNCE ONU KOŞ, buraya dönme
□ Betiğin kararı BLOCK mu?           evet  → önce onu düzelt, sonra buraya gel
□ Dosyada IMAGE + VIDEO çifti var mı? hayır → EKSİK GİRDİ, koşu başlamaz
```

---

# ⛔ YANLIŞ POZİTİF DUVARI — bunlar İHLAL DEĞİLDİR

> Bu depoda üç QA koşusu çalışan tasarımı bozmaya yönlendirdi. Aşağıdakiler
> hakkında bulgu yazılmaz; yazılırsa bulgu düşer.

```
· TIRNAK İÇİ TÜRKÇE REPLİK        replik Türkçedir ve öyle olmalıdır
                                   (VEO kılavuzu §3 tırnak sentaksı)
· BÜYÜK HARF VURGUSU              "THREE hard black shadow bands" — bu
                                   depo vurguyu kapitalle yapar, metin değil
· METİNSİZ SAYAÇ                  "the gauge shows eight sockets" A1'in
                                   İHLALİ değil ÇÖZÜMÜdür (D50)
· MUTLAK SİYAH GÖLGE              vakumda doğru fizik, "detay kaybı" değil
· SESSİZLİK                       bu depodaki filmlerin çoğu bilinçli sessiz
· SENTETİK SES                    seri diegetik yapay ses kullanıyor
· YAVAŞLIK / SABİT KAMERA         lockoff bir karar, kusur değil
· YEDEK SÜRÜMLERİN ÇIPLAKLIĞI     B/C/D sürümlerinin varlık sebebi
                                   negatif bloğun kaldırılmasıdır (§7)
```

---

# 1. 🔢 KİLİT SAYIYA ÇEVRİLMİŞ Mİ  ⭐ EN AĞIR KATEGORİ

> Ölçülmüş tek gerçek: **tarif kilidi %0 tuttu, sayısal kilit %100 tuttu.**
> Kaynak: `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md`

Promptta geçen her kilidi tabloya yaz ve sınıflandır:

| Kilit | Promptta yazan hâli | SAYI mı TARİF mi | Önerilen sayısal hâl |
|---|---|---|---|

```
TARİF örnekleri (hepsi BULGU):
  ✗ "low gravity"              → ✅ "0.38g — düşen nesne 1 saniyede 1.9 m"
  ✗ "massive ship"             → ✅ "140 m gövde, 9 m lander'ın 15 katı"
  ✗ "she is alone"             → ✅ "Exactly 1 human figure"
  ✗ "dust settles slowly"      → ✅ "dust reaches the surface in 3 seconds"
  ✗ "the creature's anatomy"   → ✅ "4 legs, 1 head, 1 tail — every frame"

⛔ BULGU YAZ: tarif kilidi başına bir satır. Üç ve üzeri tarif kilidi → BLOCK.
```

---

# 2. 🎯 SAHNE HANGİ DERSİ TETİKLİYOR, KİLİT VAR MI

Sahnenin İÇERİĞİNE bak ve tetiklenen dersin kilidinin promptta olup
olmadığını kontrol et. Kaynak: `DERSLER/` · `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| Sahnede varsa | Aranan kilit | Yoksa |
|---|---|---|
| su / sıvı teması | temas sahnesi sayımı · eldiven | 🔴 |
| canlı / hayvan | uzuv sayımı + adım eklemlenmesi | 🔴 |
| kask / vizör | kask takvimi + D79 iki cümlesi | 🟠 |
| ekran / sayaç | metinsiz kanal (geometri/mesafe/gölge) | 🟠 |
| ikinci figür | insan sayısı kilidi | 🟠 |
| patlama / parçacık | sayılı ve yerel ("3 m gri toz sütunu") | 🟡 |
| diyalog | konuşan ekranda mı · dudak kuralı | 🟡 |
| sıfır-g | mikro hareket (eksen dönüşü, uzuv sürüklenmesi) | 🟡 |
| biniş / iniş hareketi | ⛔ D69: kadraj DIŞI olmalı | 🔴 |
| ayna / yansıtıcı yüzey | D20/D69 — kopya karakter riski | 🔴 |

```
⛔ 🔴 işaretli bir tetikleyici kilitsizse → BLOCK.
   Prompt iyileştirmek işe yaramıyor; malzeme azaltmak gerekiyor olabilir
   (5+ risk → film şu anki sistemle 5/10'u geçemez).
```

---

# 3. 📵 YASAK ↔ ANLATIM ÇELİŞKİSİ (A1) — anlam düzeyinde

> Betik bunun sözdizimsel hâlini yakalar ("the countdown reads 6:00:00").
> Burada aranan anlam düzeyi: **promptun anlatmak istediği bilgi, promptun
> kendi yasağıyla öldürülüyor mu?**

```
□ Promptun taşıdığı DRAMATİK BİLGİ nedir? (tek cümle yaz)
□ O bilgi hangi kanaldan okunacak?
     metin → 🚨 yasak onu silecek, model her zaman yasağı seçer
     geometri / mesafe / gölge / sayı / ses → ✅
□ Kanal yoksa: bilgi ekrana HİÇ çıkmıyor demektir.
```

> 🚨 **Tidal Hunt:** satır 285 `NEVER text`, satır 338 `the countdown reads
> 6:00:00`. Sayaç ekrana hiç çıkmadı; "6 saatte geç" filminden geriye
> "bir kadın koşuyor" kaldı. Ekranda yanlış bir şey yoktu — sadece bir şey
> yoktu, ve QA bunu göremedi. → Ders 50

---

# 4. 🧱 SELF-CONTAINED MI — anlam düzeyinde

```
□ Bu prompt, filmin geri kalanını hiç görmemiş birine tek başına verilse
  aynı kareyi üretir mi?
□ Karakter/araç tanımı KELİMESİ KELİMESİNE önceki sahnelerdeki gibi mi?
     ⚠️ "aynı anlamda" YETMEZ. Çapa bloğu birebir aynı dize olmalı
        (SAHNE_DEVAMLILIK §2.1)
□ Promptta film dışı bir şeye atıf var mı? ("as before", "same as S3")
```

---

# 5. 🎬 ÇEKİM GERÇEKTEN TARİF EDİLMİŞ Mİ

```
□ VIDEO promptunda zaman damgaları var mı ve toplam süreyi dolduruyor mu?
□ Her damgada GÖRÜLEN bir değişim var mı — yoksa ölü saniye mi?
□ Kamera kararı yazılı mı (lockoff / hareket) ve tek çekim mi?
□ Sahnenin doruğu bu promptun İÇİNDE mi, yoksa bir sonrakine mi düşüyor?
     🚨 Tidal Hunt: dalganın çarptığı an hiçbir sahnede yazılmamıştı
```

---

# 📤 ÇIKTI BİÇİMİ

```
PROMPT QA — <FİLM> · <SAHNE>            tarih: GG.AA.YYYY
BETİK KARARI: <GO/FIX/BLOCK>            (prompt_kontrol.py çıktısı)

KARAR: GO | FIX | BLOCK

1. KİLİT TABLOSU        [tablo]
2. TETİKLENEN DERSLER   [ders no → kilit var/yok]
3. BULGULAR
   Her bulgu ŞUNU TAŞIMAK ZORUNDA:
     · promptun ihlal eden CÜMLESİNİ birebir alıntı
     · hangi ders/kural (numarayla)
     · önerilen SAYISAL karşılık
   Alıntı taşımayan bulgu AÇIK SORU'ya iner, bulgu sayılmaz.
4. AÇIK SORULAR         [plan dosyasından cevaplanacaklar]
```

```
KARAR EŞİKLERİ
  BLOCK   3+ tarih kilidi · 🔴 tetikleyici kilitsiz · A1 çelişkisi
  FIX     kalan her bulgu
  GO      bulgu yok — üretime geç
```

---

# 📝 KAYNAK

Bu rubriğin her maddesi bir gerçek olaydan çıktı:

| Bölüm | Kaynak |
|---|---|
| 1 | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` §4 |
| 2 | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` · `DERSLER/` |
| 3 | Ders 50 · The Tidal Hunt |
| 4 | AGENTS.md kural ③ · `SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1 |
| 5 | `03_PLAN_ONCESI_KONTROL_LISTESI.md` B1 · The Tidal Hunt |
| Yanlış pozitif duvarı | `QA_PROMPTLARI/FILME_OZEL/` Ring Light gerekçesi |
