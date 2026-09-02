# 📚 YERÇEKİMİ — FAZ 3 / HALAT · QA DERSLERİ VE AKSİYON

```
Koşu    01.09.2026 · iki mühürlü geçiş (A kör + B katalog), Gemini, ayrı sohbetler
Ham     .../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI_FAZ03_{KOR,KATALOG}_HAM.md
Defter  .../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/YERCEKIMI.md § KOŞU 3
Mod     ⚠️ V — SPEC yok [D129] · master yok [⑪] → film-dersi YAZILAMAZ
Sisteme GOZLEM_DEFTERI: ADAY-3 (3. vaka) · ADAY-4 (2. vaka) · ⭐ ADAY-5 yeni
```

---

# ✅ ÖNCE İYİ HABER — FİLMİN İLK TEMİZ FAZI

```
MATCHED 12/12 · MISSING 0 · UNMATCHED 0 · KOPYA 0 · figür sayımı 10/10

F1  S8 iptal          → 11/12
F2  C üretilmedi, B iki kez → 11/12
F3  TAM               → 12/12   ⭐ ilk kez
```

Ayrıca **kapsül burnu EKRAN-SOLDA tuttu** (E ve H) — F2'de mekiğin burnu
6 klibin 5'inde ters çıkmıştı. Fark F2'nin dersini doğruluyor: **yön kilidi
kadrajda YÜK TAŞIDIĞINDA tutuyor.** Kapsül, tanımlı bir uca kenetli;
mekik uzak bir siluetti.

İkisi de temiz: **sıfır okunur karakter · kimse dönmüyor.**

---

# 🔴 AMA HİKÂYENİN SONU DEĞİŞTİ — bu fazın asıl bulgusu

Kör denetçi (belge yok, katalog yok) fazı şöyle bitirdi:

> *"Ultimately, both astronauts are exposed to the vacuum of space, with
> one opening his helmet visor and the other floating entirely without
> her helmet."*

```
FİLMİN S25-S36'sı İSTASYONA VARIŞLA biter.
İZLEYİCİNİN GÖRDÜĞÜ: varırlar → el ele tutuşurlar → vakumda ÖLÜRLER.
16:00'lık filmin 4:48'inde iki ana karakter ölmüş görünüyor.
```

⛔ **Bu bir süreklilik ayrıntısı değil, olay örgüsünün tersine çevrilmesidir.**
F2'nin kusurları (kubbe vizör, mekik yönü) kozmetikti ve "geri dönüş yok"
kararı onlar için savunulabilirdi. **Bu farklı bir sınıf.**

## Sahte saat nasıl kuruldu

Kör denetçi kendi "tek yönlü saat" listesine şunu yazdı:

```
"Survivability: Helmets sealed (1,2,3,5,6,9,11,12)
 → Helmets removed or open in space (4, 10).   Confidence: HIGH"
```

D ve J'yi bu yüzden **sona** koydu: *"a state representing the terminal end."*
İki render kusuru, olmayan bir anlatı saati uydurdu.

⭐ **Benim kurduğum saat çalıştı:** *"Proximity to station: dot → medium →
fills frame. Confidence: High."* İlk üç konum doğru, hedef doğru okundu.
Sahte saat onu ezdi.

```
SIRA SKORU  5/12   (F2: 8/12)
⛔ Düşüş görsel zincirin zayıflığından DEĞİL — iki kusurdan.
```

---

# 🔬 İKİ KUSURUN SEBEBİ BULUNDU

## ① D (S28) — kask yok · SEBEP: promptun kendi cümlesi

Denetçi sordu: *"Promptta 'kask takılı' yazıyor muydu?"* Cevap komut
satırında [D125]:

```
S28 IMAGE : helmet ×3 · tam vizör cümlesi ölçüleriyle VAR
S28 VIDEO : helmet ×4
⭐ AMA S28 VIDEO'DA ŞU CÜMLE VAR:
   "Her body is never rigid: shoulders lead, legs follow,
    HAIR LIFTS INSIDE THE HELMET."

RENDER: SAÇ KALKTI, KASK GİTTİ.
```

Küçük ve hareketli ayrıntı, kapsayan katı nesneyi ezdi. Aynı kalıp A'da
(S25) yarı düştü: kask kaldı ama saç *"rüzgârdaymış gibi şiddetle"* uçuştu.

```
"hair … in/inside the helmet" KALIBI FİLMDE 8 YERDE:
   FAZ_01 3 · FAZ_03 3 · FAZ_04 2
⭐ F4 HENÜZ ÜRETİLMEDİ → iki geçiş ŞİMDİ düzeltilirse kusur F4'te DOĞMAZ.
⚠️ F5-F9'daki 47 "hair lift" KASKSIZ sahnelerde; onlara dokunulmaz.
→ GOZLEM_DEFTERI ADAY-5
```

## ② J (S34) — vizör açık okunuyor · SEBEP: kubbeyi kabul etmenin bedeli

```
J'nin promptunda vizör VAR (visor ×4, geometri cümlesi ×1).
İki geçiş de "vizör açık / yüz vakuma açık" dedi.

MEKANİZMA [D95 → D146]:
   D95  : "optik berrak vizör 'kask yok' diye okunur."
   D146 : cevabı GÖRÜNÜR ÇERÇEVEYDİ.
   01.09: kubbe kabul edildi → çerçeve de gitti.
   Geniş ve orta planda sorun yok. YAKIN PLANDA
   çerçevesiz + berrak cam = KASK YOK.
```

⛔ **01.09'da yazdığım "optik kazandı, geometriyi bırak" sonucu yakın
planlar için eksikti.** Çerçeve dekorasyon değildi — kaskı yakın planda
kask yapan şeydi. Düzeltme: **yalnız CU yüz kadrajlarında görünür çerçeve
geri gelir**; geniş planlar kubbe kalabilir.

---

# ⭐ F3'ÜN ÖLÇMEK İÇİN TASARLANDIĞI ŞEY ÖLÇÜLDÜ

## Sırt ünitesi YEDİ klipte aynı değil

Kör geçişe hiçbir tarif verilmedi. Kendi gözüyle:

```
B · C · L → "kocaman kutu biçimli metal yapı, omuzlardan geniş, sırttan
             çok çıkık, yatay paneller, yan raylar, DÖRT dikdörtgen nozul"
G · I · K → "bu kocaman yapı TAMAMEN YOK, yerinde sıradan küçük
             yuvarlak beyaz sırt çantası"
```

⭐ **Örüntü:** ünite arkadan/uzaktan çekimlerde VAR, yandan orta plan
ikili çekimlerde YOK. Model, yan orta planda jenerik sırt çantasına dönüyor.

⭐ **Ve fazlar arası çapa:** F2'nin kör geçişi de aynı aileyi tarif
etmişti (katı dikdörtgen levha, dört köşe nozulu). İki faz, iki kör
geçiş, aynı nesne — **RC'nin tasarım yönü doğru, sadece hiç sabitlenmemiş.**

## İstasyon her klipte başka hasarlı

```
H  tek dev yırtık  ·  I  tek orta delik  ·  K  çok sayıda küçük delik
L  dev sürekli yarık
```

RE paneli üretilmedi → tam beklendiği gibi. **Ama mimarisi tuttu:** dört
modül, omurga, bir sağlam bir parçalanmış kanat, sol uçta kapsül — ikisi
de doğru okudu. Bozulan yalnız HASAR.

⛔ **⑩ notu:** katalog geçişi H'yi "spec'teki delik değil dev yırtık" diye
kusur yazdı. Asıl bulgu boyut değil TUTARSIZLIK; ve **H istasyonun tek tam
boy görüntüsüdür → RE p2 yerine geçecek olan odur. H sapma değil, MASTER.**

---

# 🔴 ÇEHOV 7 KURULMADI — F4'Ü DOĞRUDAN ETKİLİYOR

```
I (S33): gök kaymıyor. İki geçiş de kaydetmedi.
KİLİT 10: "bu kurulum S43'ün FEDA FİZİĞİNİN ÖN ŞARTIDIR;
           merkezkaç oradan gelir."
⛔ F4'ün fedasının fiziksel zemini şu an EKRANDA YOK.
```

---

# 🔴 KARE BEKLEYEN İKİ ÇELİŞKİ

```
① KADININ SIRTI — kör geçiş A ve C'de "yuvarlak BEYAZ SIRT ÇANTASI" gördü;
   katalog geçişi "sırtı düz" dedi. Düz-sırt filmin en sert kilidi.
   ffmpeg -ss 4 -i <makara>.mp4 -frames:v 1 sirt_A.jpg

② J'DEKİ ŞERİT — kör geçiş "DÖRT parlayan dikdörtgen" gördü; katalog
   geçişi 1 yanık varsayıp "düşmedi" dedi. Dördü yanıksa sayaç YUKARI
   gitmiştir ve Çehov 3 hiç ödenmemiştir.
   ffmpeg -ss 74 -i <makara>.mp4 -frames:v 1 serit_J.jpg
```

---

# 🔧 AKSİYON

```
🔴 BU İKİSİ İÇİN GERİ DÖNÜLMELİ — sebep süreklilik değil, OLAY ÖRGÜSÜ
 ① D (S28)  önce promptu düzelt (saç cümlesi), sonra yeniden üret
 ② J (S34)  CU'da görünür çerçeve geri gelsin
 İkisi de TEK FİGÜRLÜ — fazın en ucuz iki yeniden üretimi.

🟠 ÜÇÜNCÜ ADAY  I (S33) — Çehov 7 hiç kurulmadı, F4 ondan besleniyor.

🟡 ÜCRETSİZ, F4 ÜRETİLMEDEN
 · F4'teki iki "hair … inside the helmet" geçişi şimdi düzeltilir
 · RE p2 → H'nin karesi master ilan edilir (üretim gerekmez, kare yeter)

🔵 KABUL EDİLEBİLİR ("geri dönüş yok" kapsamında)
 · sırt ünitesinin kaybolması · istasyon hasarının değişmesi ·
   ışık tarafı sapmaları (B·H·K·L) · sayaçların düşmemesi ·
   L'de el ele tutuşma · pufların sürekli olması · C'de halatın sarkması
 ⚠️ Sırt ünitesi ve istasyon F4-F10 boyunca devam ediyor; RC ve RE
   panelleri üretilmedikçe her fazda tekrarlar.
```
