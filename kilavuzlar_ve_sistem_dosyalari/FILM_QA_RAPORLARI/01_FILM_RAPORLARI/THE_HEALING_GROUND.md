# 🌱 THE HEALING GROUND — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı · **master ÖLÇÜLDÜ** ✅
> **Koşu:** 04.09.2026 · **yedi mercek** (🔧 KARE · 🔗 DEVAMLILIK · 📖 HİKAYE ·
> 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR) — yedisi de tek Gemini
> oturumunda, **yedisi de mod V**. ③ SES hiç koşulmadı.
>
> ⛔ **HİÇBİR SKOR SATIRI HİÇBİR T TABLOSUNA GİRMEDİ.**
> ① `THE_HEALING_GROUND_QA_SPEC.md` **VAR** *ve* mod-D paketi
> `QA_PROMPTLARI/FILME_OZEL/THE_HEALING_GROUND/PAKET_1..8` **VAR** — ikisi de
> filmle aynı gün, 05:00'te üretilmişti. Operatör yine çıplak rubriği
> yapıştırdı → koşu TEKRARLANIR [D129].
> **SPEC yazılmış olduğu hâlde mod V koşulan film: 13.** (THE STILL SWARM
> 01.09 · THE SINKING STAKE 02.09 · THE UPWARD FALL 04.09 · bu film 04.09 —
> son ikisi AYNI GÜN, aynı sebep, arka arkaya.)
> ② ⑤ ARKA PLAN tek başına tabloya girebilecekti (9,0 ⚠️ ŞARTLI) — **girmedi**:
> master FİLİGRANLI, ve D150 "filigranlı master master değildir; mercekler onu
> ölçmemiş sayılır" der.
>
> ⭐ **AMA BU KAYIT ASKIDA DEĞİL.** ⑪ ÖLÇÜM KAPISI koşuldu ve aşağıdaki
> bulguların hiçbiri bir rapordan gelmiyor — hepsi ÖLÇÜMDEN, ses profilinden
> ve karelerden geliyor. **Yedi merceğin yedisi de bunların hiçbirini
> görmedi.**

---

## 📦 MALZEME

```
MASTER:   /Users/dai/Downloads/the healıng ground.mp4
          145,09 s · 1920x1080 · 30 fps · AAC · 48,4 MB
İKİZ:     /Users/dai/Downloads/the healıng ground (1).mp4 — AYNI SÜRE
          (145,09 s), 3840x2160, 141,4 MB. Aynı kurgunun iki çözünürlüğü.
KART:     140,10 → 145,09 s · 4,99 s · BAŞLIK KARTI
          "THE HEALING GROUND / NOTHING WARM STAYS ON THIS GROUND"
          ⛔ SPEC B: `SCREEN TEXT: 0,0 saniye — jenerik/başlık kartı DAHİL`
          ⛔ Kartın GÖRSELİ filmin dünyası DEĞİL: turuncu gökyüzü, ufku kaplayan
             dev gezegen, SİYAH giysi, kapıları ışıklı kubbeler. Filmin kendi
             paleti soluk kum + kehribar pus, gezegen YOK, giysi arduvaz grisi.
             Kart bir KAPAK görselidir, filmden bir kare değil.
          Kart hem SAYIMIN hem SÜRENİN dışında tutuldu [D93 · D120].
GÖVDE:    140,00 s = 14 klip × 10,0 s
          kesme ızgarası: 10,03 · 20,03 · 30,03 · 40,03 · 50,03 · 60,03 ·
          70,07 · 80,07 · 90,07 · 100,07 · 110,07 · 120,07 · 130,07 (13 kesme)
          + 140,10 (gövde→kart)
MERCEK:   ① 6,6 · ② 6,7 · ③ — · ④ 3,0 · ⑤ 9,0 · ⑥ — · ⑦ — · ⑧ 3,8
          (düzeltilmiş ortalamalar · ②'nin sayısı 🚨 GEÇERSİZ ·
           ⑥⑦ düzeltmeden sonra HİÇ hücre kalmıyor ·
           HİÇBİRİ TABLOYA GİRMEZ [D129 + D150])
```

---

## §⑪ ÖLÇÜM KAPISI — `olcum_kapisi.sh` · 04.09.2026 · **KOŞULDU**

| ölçüm | değer | SPEC ne diyor | sonuç |
|---|---|---|---|
| süre | **145,09 s** | 139 s | ⛔ **+6,1 s** |
| gövde süresi (kartsız) | **140,00 s** | 139 s | ⚠️ **+1 s** |
| sahne | **14** | 14 | ✅ |
| ızgara | **10,0 s hook + n×10,0** | **9 s** hook + n×10 | ⚠️ hook 9 değil **10** |
| kesme (sahne↔sahne) | **13** | 13 | ✅ |
| ses kanalı | **VAR** — AAC | sesli (4 replik) | ✅ kanal var |
| replik | **3 duyuldu / 4 planlı** | R1 41,0 · R2 72,0 · R3 113,5 · R4 135,0 | ⚠️ R4 zayıf |
| sessizlik (−50 / −40 / −30 dB) | **HİÇBİR ARALIK YOK** | S12'de **2 s MUTLAK sessizlik** | 🔴 **DORUK TESLİM EDİLMEDİ** |
| loudness | **I = −14,7 LUFS · Peak −0,4 dBFS** | −14 LUFS / −1,0 dBTP | 🔴 **tepe kilidi aşıldı** |
| köşe testi | **FİLİGRAN VAR** — sağ altta dört uçlu beyaz ✦, 5/5 gövde örneği (5·30·60·90·120 s) | — | 🔴 **TESLİM KUSURU [D150]** |
| kuyruk kartı | 140,10 → SON, 4,99 s, yanan başlık | ekran metni 0,0 s | 🔴 **[D70 · D72]** |
| DÖNGÜ KANITI | ⛔ **ÖLDÜ** — S0 ↔ S13 eş kadraj çifti kartın arkasında kaldı | SPEC B: döngü kanıtı zorunlu | 🔴 |

```
⛔ ÜÇ TESLİM KUSURU. Bu master master DEĞİLDİR:
   ① üretici filigranı (✦) gövdenin 140 saniyesinin 140'ında duruyor
   ② kuyrukta 5 saniyelik yanan başlık kartı var, ve kartın görseli
      filmin dünyasından değil
   ③ true peak −0,4 dBTP — ihraç kilidi −1,0
   Üçü de rapor bulgusu DEĞİL, TESLİM kusurudur. Master yeniden ihraç
   edilmeden hiçbir mercek yeniden koşulmaz.
⚠️ Bunlar THE UPWARD FALL'ın (04.09, aynı gün) ÜÇ kusurunun AYNISI.
   İki film üst üste, aynı imza: filigran + kuyruk kartı + ihraç seviyesi.
   → Kusur film başına değil, İHRAÇ HATTINA aittir.
```

### §⑪.b SES PROFİLİ — 300-3400 Hz bandı, saniyede bir RMS

```
medyan −22,4 dB · min −41,2 · maks −17,5

PLANLI REPLİK  ÖLÇÜLEN                    SONUÇ
R1  41,0 s     43 s'de −18,2 (+4,2 dB)    ✅ VAR (①②⑧ alıntıladı)
R2  72,0 s     72-78 s −19,0…−20,7        ✅ VAR
R3 113,5 s     114-115 s −18,6…−20,4      ✅ VAR
R4 135,0 s     135 s −21,7, tek saniye    ⚠️ ZAYIF — komşuları −27…−34

⭐ DORUK PENCERESİ  S12 = 120-130 s
   planlı MUTLAK SESSİZLİK 125,5-127,5 s → ÖLÇÜLEN −20,4 · −20,6 · −20,2 dB
   Bu, filmin SESLİ seviyesidir. Filmin gerçek sessiz dibi 130-141 s
   arasındadır (−26,8 … −34,7 dB).
   ⛔ Sessizlik bıçağı yalnız EKSİK değil: doruk, filmin GÜRÜLTÜLÜ
     anlarından biri, ve sessizlik doruktan BEŞ SANİYE SONRA geliyor.
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 04.09.2026 · **7 rapor**

```
--hook 10 --klip 10 --olcum-kesme 13 --olcum-sahne 14

🚨 GEÇERSİZ  ② DEVAMLILIK  iddia n=11 Σ=87 ort=7,9 │ hücreler n=12 Σ=97 ort=8,08
                            ARİTMETİK FABRİKE — hiçbir hücre kümesi 87'yi üretmiyor
                            + 5 hücre D131'den düştü → n=7 Σ=47 ort=6,7
                            + tally (0,3,3) ≠ yazılı etiketler (0,1,3)
⛔ TEKRAR    ① KARE        n=9 Σ=59 ort=6,6 · D129
⛔ TEKRAR    ④ HİKAYE      n=9 Σ=27 ort=3,0 · D129
⛔ TEKRAR    ⑥ FİZİK       n=7 Σ=49 → 7 hücrenin 7'si `—` [D131] → HİÇ SAYI KALMADI
⛔ TEKRAR    ⑦ AKSİYON     n=7 Σ=70 → 7 hücrenin 7'si `—` [D131] → HİÇ SAYI KALMADI
⛔ TEKRAR    ⑧ EFOR        n=5 Σ=19 ort=3,8 · D129 · PREMISE REGISTER yalnız ORTAM [D166]
⚠️ ŞARTLI    ⑤ ARKA PLAN   n=6 Σ=54 ort=9,0 (② ③ ⑤ tasarımca mod V)

TOPLAM 7 · 🚨 1 · ⛔ 5 · ⚠️ 1 · ✅ 0
tam çıktı: RAPOR_KONTROL/RAPORLAR/THE_HEALING_GROUND_20260904_RAPOR_KONTROL.md
```

⭐ **⑥ ve ⑦ ders niteliğindedir.** İkisi de "PHYSICS HOLDS" / "ACTION READS"
dedi ve **10,0 ile 7,0** verdi. Betik D131'i uygulayınca ikisinde de
**tek bir hücre kalmadı**: bütün hücrelerin issue alanı "no in-scope
source" yazıyordu. Yani iki mercek de hiçbir şey ölçmemiş, sonra tam not
vermişti. ⑦'nin 10,0'ı bu depodaki en yüksek mercek skoruydu.

---

## §⑤ ÇAPRAZ KAPI — yedi rapor yan yana

| eksen | ⑤ | ⑥ | ⑦ | ④ | ① | ② | ⑧ | ÖLÇÜM |
|---|---|---|---|---|---|---|---|---|
| kesme | 13 | 13 | 13 | 13 | 13 | 13 | 13 | **13** ✅ |
| sahne | 14 | 14 | 14 | 14 | ? | 14 | 14 | **14** ✅ |
| süre | 146 | 146 | 146 | 146 | ~145 | ~145 | ~145 | **145,09** |
| **replik** | — | **0** | **0** | **0** | **3** | **3** | **3** | **3-4 VAR** |
| **şerit** | `11111111111111` | `11111111111111` | `1111-1…` | `1111-1…` | `11111111111111` | `1111-1…` | `1111-1…` | **`1111-1…`** |

```
🔴 ÇAPRAZ KAPININ EN BÜYÜK BULGUSU — REPLİK EKSENİ İKİYE BÖLÜNDÜ.
   ①②⑧ üçü de AYNI ÜÇ CÜMLEYİ, AYNI zaman kodlarıyla yazdı:
     0:43  "The last one's gone under. Same as the others."
     1:13  "Whoever walks this line next, start from this end."
     1:55  "It'll hold once it's cold."
   ⑥⑦④ üçü de "none — nothing audible to me" yazdı.

   ⑪ ölçümü hakem: ses kanalı VAR, ve üç zaman kodunun ÜÇÜ DE ses
   bandında tepe veriyor (43 s +4,2 dB · 72-78 s · 114-115 s).
   ⭐ Üstelik üçü de SPEC'in planladığı üç repliğin +1 s kaymış hâli
     (41,0 → 43 · 72,0 → 73 · 113,5 → 115) — kayma ızgaranın 9 s yerine
     10 s hook ile ihraç edilmesinden geliyor. Yani ①②⑧ DOĞRU DUYDU.
   ⛔ ⑥⑦④'ün "nothing audible" satırı YANLIŞ. Üçünün de ses ekseni sıfır
     değerindedir; ④'ün Diyalog hücresine yazdığı "silent film → N/A"
     bu yüzden ölçüm değil, sağırlıktır.

⚠️ ŞERİT — ⑤⑥① `11111111111111` yazdı; ④⑦②⑧ `1111-111111111`.
   Çoğunluk + ölçüm haklı: S4 (40-50 s) kadrajında insan YOK — yalnız bir
   kubbe ve zeminde duran bir eldiven var. ⑤ bunu KENDİ envanterinde
   ("SUBJECT: Dome, glove, alien stingray") yazdı ve yine de şeridine 1
   koydu [D135].
```

---

## §⑩ ÖNERME KAPISI — plana çarpıp DÜŞEN bulgular

| bulgu | kim | plan ne diyor | hüküm |
|---|---|---|---|
| "Kubbe dizilimi tamamen yeniden diziliyor (S2 tek sıra → S12 iki yanlı cadde)" −6 | ⑤ | **Novum budur.** Zemin sıcak olan her şeyin üstünü kapatır: yeni kubbeler adamın geçtiği yerde kabarır (S2 bot izi, S4 taze kubbe), eskiler düzleşir (S10, S13). Ayrıca ⑤'in kendi kuralı iki çekimin AYNI MESAFEDEN olmasını ve mesafe ipucunun adlandırılmasını ister — adlandırılmadı. S1 dizinin BOYUNCA, S11 dizinin KARŞIDAN bakıyor. | ⛔ **DÜŞTÜ** — puan iade |
| "Açıklanmayan çubuk (S10): öncesinde de sonrasında da taşınmıyor, KES" | ②⑦ | Çubuk filmin **TOHUMU**: S1'de 0:15-0:17'de ufukta duruyor (SPEC: ENDING TYPE · seed), S9'da ödemesi yapılıyor. Kesilirse final anlamsızlaşır. | ⛔ **DÜŞTÜ** |
| "S8 ve S9 gereksiz yürüme düğümleri — KES" (kesme listesi 1 ve 2) | ④ | **S8 ve S10 ⭐VİRAL interstitial ve SPEC'te "⛔ THESE MAY NOT BE CUT".** ④'ün numaralandırması 1-tabanlı: onun S8 = planın S7 (tepe çekimi, ⚡İRONİ, bilgi asimetrisinin taşıyıcısı — izleyici yassı formu görür, adam görmez, pencere 10 s açık). | ⛔ **DÜŞTÜ** |
| "S11 duraklama, KES" (kesme listesi 3) | ④ | ④'ün S11 = planın S10 = **⭐VİRAL #2**, kesilemez; eli göğüs mandalına gider ve durur — merkezî seçimin kurulumu. | ⛔ **DÜŞTÜ** |
| "Yerçekimi ~8 m/s² · Dünya standardı" | ⑥ | SPEC: **0,38 g ≈ 3,7 m/s²**. ⑥ tek bir düşüşten (L3) cetvelsiz tahmin yürüttü ve iki katından fazla saptı. | ⛔ **CETVELSİZ — düşer** |
| "Süre 146 s / 02:26" | ⑤⑥⑦④ | ölçülen 145,09 s | ⚠️ ±2 s içinde, geçer |

⭐ **DÜŞEN BULGULARIN HEPSİ AYNI SEBEPTEN DÜŞTÜ: mercek belgeyi görmedi.**
④'ün kesme listesindeki üç sahnenin üçü de SPEC'te KESİLEMEZ yazıyor.
Mod V bir hikâye merceğine kesme listesi yazdırmak, filmi tam da
korunması gereken üç sahnesinden budamak demektir.

---

## ⭐ ASIL TEŞHİS — "hikâye neden berbat?"

> ④ HİKAYE **3,0/10** verdi ve satırı tabloya giremez. **Ama sayı düşerken
> teşhis düşmüyor.** Merceğin en sert dört cümlesi plana çarpınca ayakta
> kalıyor, ve dördü de AYNI ŞEYİ söylüyor:

| ④ ne dedi | plan ne yazmıştı | ölçüm ne diyor |
|---|---|---|
| "Character 2/10 — kamera taşıyıcı, istek yok, korku yok" | B5 İSTEK: son diski yerleştirip hattı kapatmak | ⬜ ekranda hiç görünmüyor |
| "Theme 3/10 — **hiçbir bedel ödenmiyor**" | B5 BEDEL: **S11'de ısıtıcıyı kapatır, vent tüyü söner** | 🔴 aşağıya bak |
| "no peak located" | DORUK S12: **2 s mutlak sessizlik** + kenarın kalkması | 🔴 sessizlik yok, doruk filmin sesli anı |
| "Ending 2/10 — bitmiyor, DURUYOR" | KAPANIŞ: S0'ın aynı kurulumu → DÖNGÜ KANITI | 🔴 kuyruğa kart yapıştırıldı, döngü öldü |

### 🔴 BULGU 1 — BEDEL SAHNESİ: imaj promptu değişimin SONRASINI dondurmuş

Filmin bütün anlamı S11'de tek bir jestte duruyor: **göğüs kapağını açar,
ısıtıcıyı kapatır, kalçasındaki buhar tüyü söner.** Video promptu bunu
doğru yazmış:

```
0.0s — ... A short white vapour plume stands at his hip.
2.0s — he reaches inside and turns one plain recessed switch. The plume at
       his hip thins, drops and goes out
```

**Ama aynı sahnenin İMAJ promptu şunu yazıyor:**

```
A flat chest module sits at the centre of his chest, its hinged cover
standing open. ... There is no vapour plume at his hip: the vent is dark
and still. ... Around the dark disc under his gloves there is no vapour
```

⛔ **İmaj promptu, video promptunun 10. saniyesini tarif ediyor.**
I2V hattında imaj = t=0'dır. Modelden söndüremeyeceği bir tüyü söndürmesi
istendi; o da **başka bir yere** tüy koyup onu söndürdü.

**Ekranda ölçülen (111 s ↔ 119 s, aynı kurulum, iki kare):**
- 111 s: adam diz üstü, iki eli diskin üstünde, **diskten** beyaz bir tüy yükseliyor
- 119 s: aynı kadraj, **tüy yok**
- Göğüs kapağı **hiç açılmıyor**, el **hiç içeri girmiyor**, anahtar **hiç yok**
- Tüy kalçada değil **diskte**
- Kamera 40 m EWS değil, ~3-4 m önden MS

Yani izleyicinin gördüğü: *"bir adam bir tabağın üstünde duruyor ve buhar
kesiliyor."* Görmediği: **adamın kendi ısısını kapattığı.**
Bedel yazıldı, sebep üretilmedi → ④'ün "no thematic cost is paid" cümlesi
DOĞRUDUR ve ⑩'dan geçer.

⚠️ Planın kendisinin de payı var: S11 kurulumu **A · 24mm · EWS · 40 m**.
Kırk metreden bir kalça tüyünün sönmesi üç pikselik bir olaydır. Film
merkezî seçimini kendi EN GENİŞ kurulumuna yazmış.

### 🔴 BULGU 2 — DORUK: sessizlik bıçağı video modeline ısmarlanmış

MUZIK dosyası doğru yazmış: *"filmin en pahalı iki saniyesi"*, KESİLEMEZ
listesinde. SPEC bunu **KAPI ④** yapmış. Ama bıçak yalnız S12'nin **video
promptunun AUDIO satırında** duruyor: `From 5.5s to 7.5s absolute silence`.

Veo'nun yerel sesi mutlak sessizlik teslim etmez. Ölçüm:
**125-128 s = −20,2…−20,6 dB, filmin sesli seviyesi.**
Filmin gerçek sessizliği 130-141 s'de, yani doruğun BEŞ SANİYE SONRASINDA.

⛔ Planlı bir sessizlik KURGU işidir; zaman çizgisine sert mute olarak
konur. Video modelinden istenirse gelmez, ve gelmediği hiçbir merceğin
gözüne çarpmaz — çünkü mercekler "sessizlik yok" diye bir kutu aramaz.

### 🔴 BULGU 3 — KAPANIŞ: kuyruk kartı döngüyü öldürdü

SPEC B: `DÖNGÜ KANITI: ilk kare (S0 · 0,0 s) ↔ son kare (S13 · 139,0 s):
AYNI kurulum (C · 35mm · alt açı 22° · h 0,45 m · 4,0 m)`.
Ekranda S13, 140,10 s'de bitiyor ve arkasına 4,99 s'lik yanan başlık kartı
geliyor. İzleyici son kare olarak **kartı** görüyor. Döngü kanıtı ölü.
④'ün "stops, does not land" cümlesi bunun tarifidir.

⚠️ Ayrıca S13 planla uyuşmuyor: plan *"soluk kenar sağ eldiveninin ÜSTÜNDE
duruyor"* diyor; ekranda adam varlığı **iki eliyle kucağında tutuyor**.
⑦'nin tek out-of-scope bayrağı bunu yakaladı: alma jesti hiç gösterilmiyor.

### 🟠 BULGU 4 — S4'ün eldiveni: kolu yazılmayan eldiven KOPUK doğuyor

②'nin "The Magic Glove" bulgusu gerçektir, ve kaynağı promptun kendisidir:

```
Only one glove and forearm are in shot ... The glove rests open on the
floor at the bottom edge of frame.
```

Model "forearm"ı düşürdü, "rests open on the floor"u kelimesi kelimesine
uyguladı → **kadrajda sahibi olmayan, boş bir eldiven.** HUMAN COUNT LOCK
1 × 14 olan bir filmde bu, ikinci bir insanın bıraktığı ekipman gibi
okunuyor: ④ onu "Disconnected Stakes", ② "ikinci mürettebat mı?" diye
işaretledi. Filmin en yüksek sesli cevapsız sorusu bir KAZA.

---

## 📋 KİLİT DEFTERİ

| # | madde | durum |
|---|---|---|
| K1 | Filigran ✦ sağ alt — 5/5 örnek | 🔴 **KAPANDI** (`olcum_kapisi.sh` köşe testi + 5·30·60·90·120 s sağ-alt montajı) — master yeniden ihraç [D150 · 4. vaka] |
| K2 | Kuyruk kartı 140,10-145,09 s | 🔴 **KAPANDI** (`son_kare.jpg` — betik basar, bakıldı) — kart kesilir [D70/D72 · 11. vaka] |
| K3 | True peak −0,4 dBTP | 🔴 **KAPANDI (ebur128)** — kilit −1,0 |
| K4 | S12 mutlak sessizlik | 🔴 **KAPANDI** (ses profili, üç eşik) — teslim edilmedi → **[D180]** |
| K5 | S11 bedel jesti (kapak + anahtar + kalça tüyü) | 🔴 **KAPANDI** (kare 111 ↔ 119) — üretilmedi → **[D179]** |
| K6 | S13 varlık eldivenin üstünde mi kucakta mı | 🔴 **KAPANDI (kare 137)** — kucakta |
| K7 | S4 kopuk eldiven | 🟠 **KAPANDI** (kare 45 + prompt) — prompt kaynaklı → **[ADAY-9]** |
| K8 | Izgara 9 s hook → 10 s ihraç edildi | ⚠️ **KAPANDI** — bütün replikler +1 s kaydı |
| K9 | R4 (135,0 s) duyuldu mu | ⬜ **AÇIK** — ses bandında tek saniyelik zayıf tepe var; ③ SES koşulunca kapanır |
| K10 | Kostüm mutasyonu S7/S11/S14 (②) | ⬜ **AÇIK** — ② 🚨 GEÇERSİZ olduğu için hüküm verilmez; temiz masterda yeniden koşulur |
| K11 | ③ SES hiç koşulmadı | ⬜ **AÇIK** — filmin 4 repliği var, ses merceği yok |

---

## 🎓 DERSLER — Kart G KOŞULDU (04.09.2026)

### 🔴 DERS 179 — İMAJ PROMPTU DEĞİŞİMİN SONRASINI YAZMAZ; I2V'de imaj t=0'dır.
`DERSLER/06_METIN_VE_PROMPT_DILI.md` · **KAPI:** BETİK · `prompt_kontrol.py` ⑳b DEĞİŞİM KAPISI
Bir sahne "X yanıyor → X sönüyor" üstüne kuruluysa, imaj promptunda X
**YANIYOR** olmalıdır. Sonrası yazılırsa model söndürecek bir şey bulamaz;
başka bir yere koyup onu söndürür ve filmin BEDELİ ekrana hiç gelmez.
Kaynak: THE HEALING GROUND S11 — imaj "no vapour plume at his hip: the
vent is dark and still", video "0.0s — A short white vapour plume stands
at his hip". Ekranda tüy kalçada değil diskte çıktı, göğüs kapağı hiç
açılmadı. → **prompt_kontrol'e kapı:** BEDEL/MERKEZÎ SEÇİM sahnesinin imaj
promptu, video promptunun 0.0 s satırıyla çelişemez.

### 🔴 DERS 180 — PLANLI SESSİZLİK KURGUDA KESİLİR, VİDEO MODELİNDEN İSTENMEZ.
`DERSLER/07_KURGU_VE_ANLATI.md` · **KAPI:** BETİK · `olcum_kapisi.sh` SESSİZLİK satırı
**TEKRAR: 1** — THE UPWARD FALL (aynı gün) ile iki vaka.
⭐ ③ SES rubriği yamandı: §9'a "A DECLARED SILENCE IS A DELIVERY ITEM" bloğu.
Veo'nun yerel sesi mutlak sessizlik teslim etmiyor. THE HEALING GROUND'ın
doruğu 2 s mutlak sessizlik üstüne kuruluydu; ölçüm 125-128 s'de −20,4 dB
gösteriyor (filmin sesli seviyesi), gerçek sessizlik doruktan 5 s sonra
geliyor. → SESSİZLİK BIÇAĞI taşıyan her film, MUZIK dosyasına **"kurguda
hard mute · sn X,X-Y,Y"** satırı yazar; video promptundaki AUDIO satırı
yedek olarak kalır ama kapı KURGUDADIR.

### 🟠 ADAY-9 — KOLU YAZILMAYAN ELDİVEN KOPUK DOĞAR.
`DERSLER/GOZLEM_DEFTERI.md` · vaka 1, ders için ≥2 bekleniyor (kapı adayı: BETİK).
Yalnız elin kadrajda olduğu ECU'larda "the glove rests on the floor"
yazılırsa model bileği ve kolu düşürür; tek insanlı filmde zeminde duran
boş eldiven İKİNCİ İNSAN gibi okunur. → doğru kalıp: *"the glove rests on
the crust, the wrist and forearm continuing unbroken out of the bottom
edge of frame."*

### ♻️ TEKRAR SAYAÇLARI İLERLEDİ (yeni ders değil)
· **D129** · SPEC + PAKET varken mod V koşulan film: **12 → 13.** Son iki film aynı
  gün, arka arkaya. Sorun artık "paket yok" değil, **paketin operatöre
  ulaşmaması.**
· **D150** filigran · **3 → 4** vaka · üst üste **2** film.
· **D70 / D72** kuyruk kartı · **10 → 11** vaka · üst üste **2** film.
· Izgara 9 s → 10 s ihraç · üst üste **2** film.
  ⭐ Dördü de İHRAÇ HATTINDA, film yazımında değil.

---

## ✅ NE YAPILIR — sıra

```
1. MASTER YENİDEN İHRAÇ (kurgu tarafı):
   · filigransız ihraç
   · kuyruk kartı KESİLİR (ekran metni 0,0 s)
   · true peak ≤ −1,0 dBTP · I = −14 LUFS
   · S12'ye 2 s HARD MUTE (125,5-127,5 s ızgarasına göre)
   · ızgara: hook 9 s mi 10 s mi — biri seçilir ve SPEC'e yazılır
2. S11 YENİDEN ÜRETİLİR — imaj promptu düzeltilerek:
   kapak KAPALI, kalçada tüy YANIYOR, disk henüz yerde DEĞİL.
3. S4 YENİDEN ÜRETİLİR — eldivenin kolu kadraj dışına kesintisiz gidiyor.
4. TEMİZ MASTER ÜSTÜNDE SEKİZ MERCEK MOD D KOŞULUR:
   PAKET_1..8 zaten hazır → QA_PROMPTLARI/FILME_OZEL/THE_HEALING_GROUND/
   ⛔ Çıplak rubrik açılmaz.
5. ③ SES ilk kez koşulur (film 4 replikli).
```

---

> **Kayıt zinciri:** ham raporlar `02_HAM_RAPORLAR/THE_HEALING_GROUND_*_HAM.md`
> (7 dosya) · betik çıktısı
> `RAPOR_KONTROL/RAPORLAR/THE_HEALING_GROUND_20260904_RAPOR_KONTROL.md`
> · T tablosu satırı: **YOK** (D129 + D150)
> · dersler: **D179** (06) · **D180** (07) · **ADAY-9** (GOZLEM_DEFTERI)
> · rubrik yaması: `3_SES_QA_CRITIQUE_PROMPT.md` §9 · iz defteri:
>   `QA_PROMPTLARI/CALISTIRMA_KAYITLARI.md` §DERS → RUBRİK İZ DEFTERİ 179-180 eki.
