# 📚 YERÇEKİMİ — FAZ 7 / SES · QA DERSLERİ VE AKSİYON

```
Koşu    06.09.2026 · Gemini · YALNIZ PROMPT A (kör geçiş)
Ham     ../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
        02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ07_KOR_HAM.md
Mod     ⚠️ V — SPEC yok [D129] · master yok [⑪] → film-dersi YAZILAMAZ
⛔ KATALOG GEÇİŞİ KOŞULMADI. D164: yalnız A → "GERÇEK ama ÖLÇÜSÜZ".
   Kimlik kapısı ve sıra skoru geçerli; kategori skorları YOK.
```

---

# ⭐ ÖNCE İKİ SAYI — ikisi de depoda ilk kez ölçüldü

```
① KLİP SÜRESİ = 10,0 s · 12 segment · 120 s toplam.
   ⛔ ÖLÇÜM BORCU KAPANDI [D125 · ortak adım ⑪]. F7-F10 ızgarası
     DOĞRULANDI; belgelerdeki mutlak zamanlar kaymıyor.
   ⚠️ F1-F6 hâlâ ölçülmedi. Kapanan borç bu fazındır, filmin değil —
     "film iki ızgaralı mı" sorusu için ffprobe yine gerekli.

② SIRA SKORU = 3/12.   F2 8/12 · F3 5/12 · F7 3/12
   Kör denetçinin sırası : 1·2·3·11·7·6·4·5·8·10·12·9
   Gerçek sıra (segment) : 1·2·4·3·5·6·7·8·9·11·10·12
   Doğru yerleşen: 1, 2 ve 6. numara. Üç tane.
```

⭐ **AMA TEŞHİS 12/12 TUTTU.** Kör denetçi on iki klibin on ikisini
birbirinden AYIRDI ve dört karıştırılabilir grubun DÖRDÜNÜ de doğru
ayrımla anlattı (L↔D: gözler açılıyor / gözler geziniyor · G↔K: ızgara
yumuşak / vana net · I↔F: gevşek / doğruluyor · H↔B: sağ el saatsiz /
sol el saatli). **Rubriğin ayırt edicileri çalıştı; başarısız olan
şey SIRA, ve sebebi rubrik değil.**

---

# 🔴 SIRA SKORUNUN DÜŞÜŞ SEBEBİ — ve o sebep bir KUSUR

Geçiş C'de "beklenti düşük olmalı, çünkü faz bir döngü" yazmıştım.
Ölçüm bunu YARIM doğruladı. Asıl sebep başka ve daha kötü:

```
Kör denetçinin EN GÜÇLÜ saati şuydu (kendi sözleri):
  "Gravity state: Normal gravity in Seg 1, zero-gravity in Seg 2.
   Confidence: High."

Seg 1 = C (S73). Promptta: "Her hair lifts and holds away from the
headrest instead of pressing flat against it."
EKRANDA: "her hair HANGS DOWN."
```

⛔ **YERÇEKİMİ FİLMİN 73. SAHNESİNDE GERİ GELDİ.** Bir 0g render
kusuru, kör denetçinin bir numaralı tek yönlü saati oldu ve fazın
tamamını yanlış hizaladı: filmin en sessiz sahnesi "yerçekimi hâlâ
varken" okundu, sonraki her klip ona göre dizildi.

⭐ **BU ÖRÜNTÜNÜN İKİNCİ VAKASI.** F3'te aynı şey olmuştu: iki klipte
kask düşmüş, kör denetçi onu "hayatta kalma saati" sayıp fazın SONUNA
koymuş, sıra skoru 8/12'den 5/12'ye inmişti.

```
SAHTE SAAT — vaka defteri
  F3  D(S28)+J(S34) kask kaybı  → "terminal end" saati  → 5/12
  F7  C(S73) saç düşmesi        → "yerçekimi var" saati → 3/12
⚠️ İki vaka. Üçüncüsünde ders yazılır [00_DERS_YAZIM_KONTRATI].
   Şimdilik: GOZLEM_DEFTERI ADAY-4'e ikinci vaka olarak düşer.
```

⛔ **VE BU BİR ÖLÇÜM UYARISIDIR, BİR SIRA UYARISI DEĞİL:** sıra skoru
düştüğünde ilk sorulacak soru "faz bağlamsız mı" değil, **"kör denetçi
hangi saati kullandı ve o saat GERÇEK Mİ"** olmalı. Bu soru rubriğe
zaten yazılı (STEP 4/c CLOCKS) ve cevabı bu koşuda tek satırda verdi.

---

# 🔴🔴 EN BÜYÜK BULGU — ALTYAZI DENEYİ ÇÜRÜDÜ VE SEBEP ARAÇTA

Bu makaranın varlık sebebi ADAY-7'nin kapanış ölçümüydü. Kapandı.

```
F5  tırnaklı sahne 2 · sesi anlatan beat VAR  → altyazı 2
F6  tırnaklı sahne 2 · sesi anlatan beat VAR  → altyazı 3
F7  tırnaklı sahne 0 · sesi anlatan beat 0    → altyazı 7  ⛔⛔
```

**Tek değişken değişti, sonuç TERS YÖNDE İKİYE KATLANDI.**

⭐ Ve daha kötüsü: **YEDİSİ DE UYDURMA. Yedisinin de karşılığı REPLİK
DEFTERİ'nde YOK.**

| Seg | Sahne | Ekrana basılan | Defterde yazan |
|:--:|:--:|---|---|
| 3 | S76 | "You should remember that." (×2) | "Told you. Half of it's storytelling." |
| 5 | S77 | "Officially decisions and" | ⛔ REPLİK 0 |
| 6 | S78 | "We are drifting off course." | "Landing rockets are rockets, engineer." |
| 9 | S81 | "It's closer than you think." | "Go home. Take the watch with you." |
| 11 | S82 | "Singing have a timed" | ⛔ REPLİK 0 |
| 12 | S84 | "Primary valve rotation complete." | "OXYGEN SIX PERCENT. RECOVERING." |

```
⛔ Repliksiz İKİ sahne (S77 · S82) altyazı taşıyor. Biri (S77) fazın
   kanıt sahnesi: kamera sesin kaynağına gider ve kaynak boştur —
   ve o boş ızgaranın üstünde bir cümle yazıyor.
⛔ İki altyazı ANLAMSIZ ("Officially decisions and" · "Singing have a
   timed") — model cümleyi tamamlayamıyor bile.
⛔ Biri (S76) AYNI KLİPTE İKİ KEZ basılmış.
```

**SONUÇ — ADAY-7 KAPANIYOR ve hipotez ÇÜRÜYOR:**

```
Tetikleyici tırnak DEĞİL.  (F6 çürüttü)
Tetikleyici sesi anlatan beat satırı DEĞİL.  (F7 çürüttü)
Tetikleyici promptta HİÇBİR ŞEY DEĞİL.
→ SEBEP ARAÇTIR. Model klibe kendi diyaloğunu yazıyor ve basıyor.
→ ÇÖZÜM PROMPT DEĞİL: ① araç ayarı  ② üretim sonrası maskeleme/kırpma
⛔ prompt_kontrol.py'ye ALTYAZI KAPISI YAZILMAZ. Yazılırsa depo,
  düzeltemeyeceği bir şeyi her fazda kontrol etmiş gibi yapar.
```

⚠️ **AMA `Audio:` BLOĞU HÂLÂ DENENMEDİ.** F7'de beat satırları
temizlendi, `Audio:` paragrafları DOKUNULMADAN kaldı ve her biri sesi
uzun uzun anlatıyor. Deneyin son adımı budur ve F9'a yazıldı
(aşağıda AKSİYON ②).

---

# 🔴 SEKİZ SAHNE KİLİDİ EKRANDA TUTMADI

Kör denetçinin tarifi, kataloğun kilitleriyle yan yana:

| Girdi | Sahne | Kilit | Ekranda | Ciddiyet |
|:--:|:--:|---|---|:--:|
| C | S73 | saç KALKAR ve TUTAR | saç **aşağı sarkıyor** | 🔴 |
| G | S75 | ⛔ baş DÖNMEZ (maks.) | **başını sola çevirip geri dönüyor** | 🔴 |
| A | S79 | tik el kadrajda %40/%20 | **el kadraj DIŞINDA** | 🔴 |
| F | S80 | koltukta doğrulur, taşmaz | **koltuktan çıkıp yükseliyor** | 🔴 |
| H | S83 | ⛔ çark BİR DERECE dönmez | **çark saat yönünde dönüyor** | 🔴 |
| B | S84 | kapak AÇILIR ve açık kalır | **kapak İTİLİP KAPATILIYOR** | 🔴🔴 |
| D | S82 | gözler ekran-sola KİLİTLİ | **gözler sağa sola geziniyor** | 🟠 |
| K | S81 | SAĞ el vana çarkında | **SOL el bir "boruda"** | 🟠 |

## ⛔ B (S84) — PERDE DÖNÜŞÜ 2 EKRANDA OLMADI

Fazın ve perdenin taşıyıcısı. Üç iş yapacaktı; **üçü de olmadı ya da
tersine döndü:**

```
① vana çeyrek tur AÇILIR   → çark dönüyor ✔ ama H'de de dönüyor:
                              vana filmde İKİ KEZ açılmış oluyor
② halka 1/6 YANIP SÖNMEYE  → ⛔ halka kadrajda HİÇ YOK (aşağıda)
   başlar
③ kırmızı kapak AÇILIR     → ⛔ TERSİ: kapak duvara İTİLİP KAPANIYOR
```

⭐ **BEDELİ ANLATI SEVİYESİNDEDİR, SÜREKLİLİK SEVİYESİNDE DEĞİL.**
Kör okuma şöyle bitiyor: *"…turns a second valve wheel and pushes an
adjacent red metal flap flat against the wall, closing it."*
Filmin "geri dönüş yolu kapandı" eşiği, ekranda **bir kapağın
kapanması** olarak okunuyor — tam tersi. Çehov 6 açılmadı.

⛔ **VE BU BİR FAZLAR ARASI ÇELİŞKİ ÜRETTİ:** F8 makarasının iki
sahnesi (S92 · S95) kapağın AÇIK ve altındaki kolun görünür olduğu
kadrajlardır ve öyle üretilmişler. İki makara birbiriyle çelişiyor.

## ⭐ H ile B AYNI İŞİ YAPIYOR — sahne ayrımı çöktü

Belge ayrımı nettir: **kavramak karar, çevirmek eylem** (KİLİT 32).
Ekranda ikisi de çeviriyor. Kör denetçi bunu kendi başına fark etti ve
"iki ayrı sistem mi?" diye sordu — yani ayrım izleyiciye ulaşmıyor.

---

# 🔴 HALKA HİÇ RENDER OLMADI — filmin omurgası ekranda yok

```
Kör pasaport, birebir:
  "A watch with a black face and a metal/black band is worn on the
   LEFT wrist. Visible in Seg 9 and Seg 12. The RIGHT wrist is bare."
⛔ ALTI SEGMENTLİ AMBER HALKA: 12 klipte 0 görülme.
```

⭐ **VE SEBEBİ BELGEDE DURUYORDU.** ÜÇ NOT ①'de üretimden önce
yazmıştım: Equipment Bible halkayı SOL, saati SAĞ bileğe koyuyor;
S81 ve S84 promptları **ikisini birden SOL bileğe** yazmıştı.

```
SONUÇ: model tek bilekteki İKİ nesneyi BİRLEŞTİRDİ ve hayatta kalan
       nesne SAAT oldu. Halka silindi.
⭐ KURAL — F8-F10 ve bundan sonraki her film:
   ⛔ BİR BİLEĞE İKİ NESNE YAZILMAZ. Halka SOL, saat SAĞ.
   ⛔ İkisi aynı kadraja giriyorsa promptta AYRI CÜMLELERLE ve
     "on the OTHER wrist" ifadesiyle ayrılır.
```

⛔ **ETKİSİ FİLM BOYUNCADIR:** oksijen zinciri (S8 6/6 → S19 4/6 →
S30 3/6 → S46 2/6 → S71 1/6 → S84 1/6 yanıp söner → S96 sabit) bu
filmin en uzun sayacıdır ve **ekranda hiç okunmuyor.** F8'de bir kez
"turuncu göstergeli siyah bilek bandı" olarak görülüp kayboluyor.

---

# 🟢 TUTAN KİLİTLER — F8-F10'da BOZMA

Bunlar ölçüldü ve çalıştı.

```
✅ DÜZ SIRT          üç sırt kadrajının üçünde de temiz
✅ TEK KİŞİ          12/12 · ikinci figür 0 · boş koltukta kimse 0
✅ AYNI YÜZ          "It is the same face in every segment"
✅ SOL ŞAKAK İZİ     Seg 3 ve Seg 11'de bağımsız olarak görüldü
✅ KASKSIZ + ÇIPLAK EL   12/12
✅ E (S77) İNSANSIZ  kadrajda insan 0 — fazın en riskli kadraj kararı
✅ IŞIK MİMARİSİ     tek amber + soluk mavi; üçüncü kaynak 0;
                     yanıp sönen lamba 0 (B'nin halkası hariç, o da yok)
✅ SERT GÖLGE 0      "shadows are generally soft" — L3 rejimi tuttu
✅ DUDAKLAR KAPALI   konuşan ağız 0/12 (altyazılara rağmen!)
✅ KAMERA 12/12 KİLİTLİ   hareketli plan 0 — depoda ilk kez tam tuttu
✅ D'DE TİK KADRAJ DIŞI   tasarlandığı gibi görülmedi ve sorulmadı
```

⭐ **"KAMERA 12/12 KİLİTLİ" DEPONUN EN İYİ SONUCUDUR.** Fazın hiçbir
klibinde pan, tilt, kayma ya da sarsıntı yok. Sebep tek satırlık bir
yazım kararı: her MOTION bloğunda `fixed lockoff` + `absolutely no
camera movement` birlikte yazılı. F8-F10'da bu ikili KORUNUR.

---

# 🔧 AKSİYON

```
🔴 GERİ DÖNÜŞ GEREKTİREN İKİ SAHNE — sebep süreklilik değil, OLAY ÖRGÜSÜ
 ① B (S84) — kapak AÇILMALI. Perde dönüşü ekranda yok ve F8 makarası
   onun açık olduğunu varsayıyor. İki makara çelişiyor.
   ⭐ ÖNCE PROMPT: aşağıdaki "durum değişimi" kalıbıyla yeniden yazılır
     (F9/F10 kapısı K5), sonra üretilir.
 ② C (S73) — saç. Fazın açılış karesi ve kör denetçinin bir numaralı
   saati. 0g kilidi burada tutmazsa sonraki her ölçüm kayar.

🟠 ÜÇÜNCÜ ADAY  H (S83) — çark dönmemeli. B düzeltilirse H'nin dönmesi
   "vana iki kez açıldı" çelişkisini tek başına ayakta tutar.

🟡 ÜCRETSİZ — hiçbir üretim gerektirmez
 · ⛔ BİR BİLEĞE İKİ NESNE YASAĞI F8-F10'a tarandı: F10 S115 TEK
   ihlaldi ve düzeltildi (bu turda).
 · ADAY-7 kapatıldı, GOZLEM_DEFTERI'ne "sebep araç" olarak yazılır.
 · Sahte saat vakası ADAY-4'e ikinci vaka olarak eklenir.

🔵 KABUL EDİLEBİLİR ("geri dönüş yok" kapsamında, sahip kararına açık)
 · G'de baş dönmesi · A'da tik elinin kadraj dışı kalması ·
   F'de koltuktan çıkma · D'de gözlerin gezinmesi · K'de yanlış el ·
   halkanın hiç görünmemesi
 ⚠️ Halka kabul edilirse film SAYACINI KAYBEDER ve gerilim yalnız
   gövdeden gelir. F9 KİLİT 46 zaten bunu söylüyor ("sayaç S96'da
   bitti; gerilim artık GÖVDEDEN"), yani film bu kaybı kaldırabilir —
   ama bilerek kabul edilmeli, fark edilmeden değil.
```

---

# ⭐ F8-F10'A GEÇEN ALTI KURAL

Bunların hepsi F9 ve F10 dosyalarına **06.09.2026 kapıları** olarak
yazıldı. Burada yalnız sebepleri duruyor.

```
K1 ALTYAZI  → sebep ARAÇ. Prompt kapısı yazılmaz; ölçüm ve maskeleme.
K2 BİLEK    → bir bileğe iki nesne yazılmaz.
K3 SAÇ/0g   → 0g saç kilidi POZİTİF eylemle yazılır, yasakla değil.
K4 BAKIŞ    → "dönmez / kilitli" yasağı tek başına tutmuyor; gözün ve
              başın NE YAPTIĞI yazılır.
K5 DURUM    → durum değiştiren sahnede İLK KARE durumu ve SON KARE
              durumu ayrı ayrı, aynı kelimelerle, iki kez yazılır.
K6 JEST     → sahnenin konusu olan jest, kadrajın köşesine
              yüzdeyle yerleştirilmez; kendi ölçeğini alır.
```
