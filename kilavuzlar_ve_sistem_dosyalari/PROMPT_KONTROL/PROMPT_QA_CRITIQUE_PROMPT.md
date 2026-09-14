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

# 3b. 🚫 YASAK LİSTESİ POLİTİKA MALİYETİ  ⭐ ÜRETİLEBİLİRLİK KAPISI

> ⭐ **01.09.2026 · KAPSAM DARALDI.** Bu kategorinin KELİME yarısı artık
> betiğe indi: `prompt_kontrol.py ⑯ POLİTİKA SÖZLÜĞÜ` T1/T2 tetikleyicileri
> NEGATIVE bloğu DÂHİL sayıyor. **Betik koşulmadan bu kategori okunmaz** —
> aşağıdaki sayım soruları betiğin çıktısını YORUMLAR, tekrarlamaz.
>
> Mekanizma: `NEGATIVE:` bloğuna yazılan yasak, yasakladığı kavramı
> promptun İÇİNE sokar. Politika sınıflandırıcısı "no" önekini değil
> KELİMEYİ okur. Filmde hiç olmayan bir şiddet, onu yasaklayan cümle
> yüzünden prompta girer ve üretimi durdurur.
>
> Sözlük ve kurtarma merdiveni:
> `../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` §2 · §5

```
□ Promptta, YASAKLAMAK İÇİN YAZILMIŞ bir şiddet/tehlike kelimesi var mı?
     gore · blood · wound · injury · corpse · body · victim · weapon ·
     jump scare · horror · suicide · drowning · burning
     → VARSA: filmde o şeyin kaç karesi var?
          0 kare  → 🚨 BULGU. Kelime SİLİNİR, yerine MALZEME TARİFİ
                    yazılır. Yasak, koruduğu şeyi üretilemez kılıyor.
          >0 kare → tasarım kararı; kilit satırında gerekçesi olmalı
□ İnsan kütlesi nasıl adlandırılmış?
     "crowd of figures" / "bodies" + kaçan-kovalanan bir insan
     → model için KİTLESEL KAZA okuması. Filmin tasarımı figürleri
       cansız/hareketsiz kuruyorsa promptun dili de ÖYLE olmalı.
□ Fiiller şiddetli mi?
     "hurls X into the chest" · "strikes his head" · "slams into her"
     → aynı fiziği taşıyan nötr hâl var mı?
       ("at hip height" · "against the base" · "meets the next one")
□ Sınırlama nasıl yazılmış?
     yasak:  "no figure falls off the bridge"      🚨 tehlikeyi adlandırır
     kural:  "the barrier holds them; the fold stops at the concrete"  ✅
```

⛔ **ÇÖZÜM HER ZAMAN AYNI YÖNDE:** yasağı sil, malzemeyi tarif et.
Aynı işi yapar ve daha iyi yapar — yasak yüzü YASAKLAR, tarif yüzü
ORTADAN KALDIRIR.

```
✗  no visible faces, no eyes, no open mouths, no teeth
✓  the head is a smooth dust shell with no readable features, like a
   plaster cast left standing in the open
```

⚠️ **Sınıflandırıcı promptu BÜTÜN olarak okur.** Tek tek masum üç cümle
(kalabalık + koşan insan + devrilen gövdeler) birlikte bir felaket
sahnesi tarif eder. Bu kategoriyi cümle cümle değil, **promptun toplam
izlenimi** üzerinden de bir kez sor: "bunu bilmeyen biri okusa ne
anlatıldığını sanır?"

---

# 3c. 🎞️ KOMPOZİSYON YÜZEYİ  ⭐ 🆕 01.09.2026 · BETİĞİN GÖREMEDİĞİ TEK EKSEN

> **Varlık sebebi:** YERCEKIMI F1 S8 (31.08.2026). Promptun kelimeleri
> TEMİZDİ. Reddedilen şey KADRAJDI: yan yana iki ön kol + tepeden makro +
> yüzsüz izolasyon. Önce yalnız sözcükler değiştirildi (bilek→ön kol,
> kayış→bant) — **yetmedi.** Kadraj değişince geçti. Depo bu vakada bir
> sahneyi kaybetti.
>
> ⛔ Bu eksende betik hiçbir zaman yardım edemez: `⑯` kelime sayar,
> kadrajı okumaz. Buradaki dört soru **insan gözünün tek işidir.**

```
□ Kadrajda ① yüz YOK ② bir uzuv/gövde parçası kadrajın KONUSU ③ kamera
  TEPEDEN ya da MAKRO — üçü birden var mı?
     → 🚨 BULGU. Kamerayı nesne HİZASINA al; parçaları yan yana değil
       ARD ARDA, farklı derinlikte diz. (YERCEKIMI S8 çözümü — ve kadraj
       ANLATIYI da iyileştirdi: hangisinin konu olduğu artık kadrajla
       söyleniyor.)

□ Sahnede bedenden BİR ŞEY ÇIKARILIYOR mu (kask · eldiven · bant · maske)?
     → 🚨 BULGU. COLD BURN S28 bu eylemle İKİ KEZ reddedildi ve sözcük
       değişimi çözmedi. Çözüm: nesne sahneye ZATEN ÇIKMIŞ olarak girer.

□ Kadrajda insan KÜTLESİ + kaçan/kovalanan/düşen tek kişi birlikte mi?
     → 🚨 BULGU. "real people in situations like that" reddi bu imzadan
       geldi (LAST SPAN S8). Kütle heykel gibi adlandırılır ve HAREKETSİZ olur.

□ Aynı promptta ① konuşan yüz ② kapital kimlik bloğu (`44-YEAR-OLD MAN`,
  `LIP-SYNC REQUIRED`) ③ tehlike çerçevesi — üçü birden var mı?
     → 🚨 BULGU. RISING SNOW S2 tam bu üçlüyle reddedildi.
       Üçü aynı prompta konmaz; kimlik düz cümleye iner.

□ ⛔ İKİ YENİLGİ KURALI: bu kare daha önce İKİ KEZ reddedildiyse
  üçüncü SÖZCÜK denemesi bulgu DEĞİL, İHLALDİR. Değişecek olan KAMERADIR.
```

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

# 6. 🎥 AÇI VURUŞLA EŞLEŞİYOR MU  🆕 26.08.2026

> **Bu kategorinin varlık sebebi:** betik açı SAYISINI ölçüyor (kaç kurulum,
> kaç açı tipi, derece bandın içinde mi) ama açının DOĞRU açı olup olmadığını
> ölçemez. Bu, modele değil insana sorulacak tek kamera sorusudur.

```
□ Sahnenin VURUŞU nedir? (keşif · tehditle yüzleşme · mutlak yenilgi ·
  sistem çöküşü · epifani · hiçlik — SENARYO_VE_VIRAL_KAMERA §2)
□ Promptun açısı, o vuruşun KAMERA_ACISI §3 tablosundaki karşılığı mı?
     keşif           → OTS / MLS 35-50mm
     tehditle yüzleşme → alt açı, bel-diz yüksekliği / MCU 24mm
     mutlak yenilgi   → üst açı, tavan yüksekliği / LS 85mm
     sistem çöküşü    → eğik 15-20° / CU 14-20mm
     epifani          → göz hizası, tam profil / MS 50mm
     hiçlik           → tepe / kuşbakışı (zenit) / XLS
□ Değilse: bilinçli sapma mı, yoksa açı hiç seçilmemiş mi?
     Bilinçliyse plana TEK SATIR gerekçe [D74]. Gerekçesiz sapma bulgudur.
□ Bir önceki sahneyle arasında GÜVENLİ BANT var mı — ≥1 ölçek kademesi
  VE ≥45° açı farkı? (ACI_YAYI §3)
     ⚠️ Betik bunu ancak KURULUM İMZASI yazılıysa ölçebiliyor; imza
        eksikse sayı değil bu soru karar verir.
□ Açı, kılavuzun SÖZLÜĞÜYLE mi yazılmış? (KAMERA_ACISI §6)
     ✅ "low angle" · "high angle" · "Dutch angle (tilted exactly 15 degrees)"
        · "over-the-shoulder"
     ❌ "locked-off tripod, low" — model bu biçimi tutmuyor; §6'nın
        tamamı bunun üzerine kurulu
□ Sabitlik emri cümle başında VE sonunda tekrarlanmış mı? (§6 kural ①)
□ Hareket süngeri var mı — toz/sis/yansıma? (§6 kural ②)
     Süngersiz lockoff ya fotoğraf donukluğuna ya kamera kaymasına düşer.
```

⛔ **Kamera hareketi ÖNERME.** Klip içi lockoff bu deponun ölçülmüş kalite
kararıdır (`02_RISK_KARTLARI.md` KART 8). Bu kategoride tartışılan tek şey
sahneler ARASINDA açının değişip değişmediğidir.

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
  BLOCK   3+ tarih kilidi · 🔴 tetikleyici kilitsiz · A1 çelişkisi ·
          filmde 0 karesi olan bir şiddeti YASAK OLARAK yazan prompt (3b)
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
| Yanlış pozitif duvarı | Ring Light gerekçesi (şablon 11.09.2026'da silindi; kural burada yaşar) |
