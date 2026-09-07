# 🎬 THE STANDING WIRE — QA KAYDI

```
FİLM        THE STANDING WIRE · yatay 16:9 · 3-5 dk bandı
YAZIM       05.09.2026 (aynı gün) · prompt_kontrol klasör modu: 0 BLOCK · GO
QA KOŞUSU   05.09.2026 · Gemini · sekiz mercek, TEK OTURUM (bağımsız değil [D110])
SONUÇ       🚨 PARTİ GEÇERSİZ — hiçbir satır T tablosuna girmez
            iki ayrı sebep, her biri tek başına yeter:
            ① SPEC VAR + sekiz raporun sekizi de INPUT MODE: V   [D129]
            ② master ÜRETİCİ FİLİGRANI taşıyor, ölçümle doğrulandı [D150 · D177]
```

---

## ⑪ ÖLÇÜM KAPISI — `olcum_kapisi.sh` · 05.09.2026

### ⑪.0 KİMLİK [D160] — aynı ada uyan İKİ dosya vardı, ikisi de ölçüldü

```
~/Downloads/the standıng wıre.mp4       1280×720   245,141 s   56 MB
~/Downloads/the standıng wıre (1).mp4   3840×2160  245,141 s  258 MB   ← ÖLÇÜLEN
→ SÜRE BİREBİR AYNI = AYNI KURGU, farklı çözünürlük.
  Raporlar 720p kopyayı ölçmüş; ölçüm 4K master üzerinde koşuldu.
  ⛔ İhraç kilidi 1440p+ — 720p kopya master DEĞİLDİR, dağıtım kopyasıdır.
```

### ⑪.1 SAYILAR — planla yan yana

| ölçüt | PLAN (SPEC) | ÖLÇÜM | sonuç |
|---|---|---|---|
| süre | 249,0 s | **245,141 s** | ⛔ Δ = −3,86 s (tolerans ±2 s) |
| klip | 25 | **24** | ⛔ bir klip EKSİK |
| sahne | 25 (S0-S24) | **24** | ⛔ |
| ızgara | hook 9,0 + 24×10,0 | **24 × 10,0** | ⛔ hook kırpması (10→9) YAPILMAMIŞ |
| ekran metni | **0 saniye** | **5,0 s başlık kartı** | 🔴 |
| filigran | 0 | **VAR — 6/6 örnek** | 🔴 |
| LUFS (I) | −14 (ihraç kilidi) | **−35,5** | 🔴 21,5 LU altında |
| true peak | −1,0 dBTP | −6,7 dBFS | ⚠️ |
| ses kanalı | var | VAR (AAC 48 kHz stereo) | ✅ |

Kesme ızgarası (scene>0.3): 10,03 · 20,03 · 30,03 · 40,03 · 60,03 · 70,07 · 80,07 ·
90,07 · 100,07 · 110,07 · 120,07 · 130,07 · 140,10 · 150,10 · 160,10 · 170,10 ·
190,10 · 200,10 · 210,13 · 220,13 · 230,13 · 240,13
(50 ve 180 karanlık kesmede dedektör kör — ızgara 10 s katı, 24 kesme.)

⛔ **249 → 245 farkı bir yuvarlama değil.** 24 × 10,0 = 240,0 + 5,0 kart = 245,0.
Yani teslim edilen dosya **24 klibin uç uca eklenmesi + bir kart**tır; planın
25. klibi hiç yok ve S0'ın 1 saniyelik kırpması hiç uygulanmamış.

### ⑪.2 FİLİGRAN — 🔴 TESLİM KUSURU [D150]

```
KÖŞE TESTİ · altı örnek (5 · 60 · 120 · 180 · 240 s + kurgu ortası)
BULGU: altı örneğin ALTISINDA, aynı yerde, aynı şekil —
       siyah daire içinde camgöbeği "▷" ikonu (üretim aracının işareti),
       kadrajın sağ-alt çeyreğinde.
       25 karelik sahne ızgarasında da 25 karenin 25'inde görünür.
→ Filigranlı master master değildir. Sekiz mercek onu ÖLÇMEMİŞ sayılır,
  mod V'den BAĞIMSIZ olarak. Önce master yeniden ihraç edilir.
⛔ %3 crop yetmez — ikon kenardan içeride; temizlik kadrajın ~%12'sini götürür.
```

### ⑪.3 KUYRUK KART — 🔴 [D70/D72] · bu ailenin 10. vakası

```
freezedetect: donmuş 241,9-244,9 s (3,0 s)
son_kare.jpg → BAKILDI: kadrajda "THE STANDING WIRE" yazısı, altın/beyaz
               tipografi, S0'ın kompozisyonu üzerinde.
```

⭐ Bu kart **KAPAK çıktısının kendisidir** ve `THE_STANDING_WIRE_KAPAK.md` tam
olarak bunu yasaklıyordu: *"⛔ KLİP ZİNCİRİNE KARIŞMAZ [D70/D72]."* Yasak filmin
kendi klasöründe, kendi dosyasında yazılıydı ve tutmadı.

⛔ **İkinci ve daha pahalı zarar:** kart, planlanan AÇILIŞ-KAPANIŞ KAFİYESİNİ
öldürüyor. SPEC ilk kare 6,0 s ↔ son kare 247,0 s diyordu; 247,0 s artık kartın
içinde. İzleyicinin filmden çıkarken gördüğü son görüntü S24 değil, bir afiş.

### ⑪.4 PLANLI SESSİZLİK — ⚠️ TESLİM EDİLMEDİ [D180 · ilk ölçülmüş vaka]

SPEC: `KURGUDA HARD MUTE: sn 214,0 – 239,0`, üç eşikte doğrulanacak.

```
−50 dB   214-239 aralığı DÖRT parçaya bölünmüş; en büyük delik 220,1→230,1 (10,0 s)
−40 dB   hâlâ 220,1→230,1 deliği var
−30 dB   193,7-245,1 kesintisiz sessiz
```

→ Aralık **sessiz değil, yalnız kısık.** D180'in istediği kurgudaki bıçak
uygulanmamış. Bu, D180'in yazıldığı günün ilk ölçülmüş vakasıdır ve **düştü.**

### ⑪.5 SAHNE IZGARASI — 25 kare, gözle bakıldı

```
sahne ortaları: 5,02 15,03 25,03 … 235,13 · 242,57(KART)
```

**İNSAN ŞERİDİ — kareyle sayıldı:**

```
PLAN     111111111111111111111-1-1   (25 · insansız S21 ve S23)
EKRAN    111111111111111111111-11    (24 · insansız TEK sahne, 215 s)
```

⛔ **Eksik klip, iki insansız sahneden BİRİDİR** — yani YANAŞMA setinin
V1/V6 zorunlu vuruşlarından biri. Şerit bunu yakaladı; süre tek başına
yakalayamazdı (24×10+5 = 245 makul bir film süresidir) [D118 · D163].

### ⑪.6 FİNAL VURUŞ KANITI [D141] — ✅ EKRANDA, ve **sekiz mercek görmedi**

```
ffmpeg -ss 236 → BAKILDI
SPEC : 6 askı · 5 dolu · 1 BOŞ
EKRAN: 5 askı · 4 dolu · 1 BOŞ   ← sayı sapıyor, ŞEKİL TAM TUTUYOR
```

Sonuncu askı **boş** ve çıplak gözle sayılabiliyor; twist okunuyor. Ayrıca aynı
karede **tel ilk kez SARKIYOR** (tek kavis) — novum'un kapanış kanıtı da ekranda.

⛔ **Sekiz raporun hiçbirinde "hook", "bracket", "coil on the wall" ya da boş
askı geçmiyor.** ② DEVAMLILIK onu ters okudu: halkayı `OPEN THREAD` yazdı
(*"Carried to the edge of space, never attached or used, abandoned"*) ve
reçetesi *"Insert a shot of her attaching/dropping it"* oldu — yani **filmin
twist'ini yok etmeyi önerdi.** ⑩ ÖNERME KAPISI bu bulguyu DÜŞÜRÜR. → [[D182]]

### ⑪.7 VİZÖR GEOMETRİSİ — ⛔ EKRANDA DÜŞTÜ [D146 · ADAY-2'nin 2. filmi]

```
SPEC : "vizör TEK DÜZ PANEL, görünür koyu çerçeve içinde — kubbe DEĞİL"
       "optik berrak: 0 ton · 0 ayna kaplaması · 0 çevre yansıması"
EKRAN (105 s CU + 25 karelik ızgara): KUBBE/BALON vizör, yüzü tümüyle saran
       yuvarlak kapak; ayrıca vizörde belirgin çevre yansıması var.
```

prompt_kontrol.py bu filme **GO** verdi — çünkü kapı cümlenin VARLIĞINI ölçer,
ekrandaki GEOMETRİYİ değil. Aynı mekanizma YERÇEKİMİ FAZ 2'de ölçülmüştü
(ADAY-2). Bu **2. ölçülmüş film**. Filmde REFERANS_PAKETI yoktu (üretilmiş panel: 0).

### ⑪.8 TUTAN KİLİTLER — dürüstlük için

```
✅ SIRT ÜNİTESİ YOK — düz siluet, sırttan çekimlerde doğrulandı        [D79]
✅ SIRT POZİTİF YÜZEY — 50-60 s sırt kadrajı temiz                     [D139]
✅ NOVUM KAPANIŞI — tel S24'te sarkıyor, tek kavis                     [ONERME]
✅ FİNAL VURUŞUN ŞEKLİ — boş askı okunuyor                             [D141]
✅ TEK İNSAN — 24 sahnenin hiçbirinde ikinci figür/klon/yansıma yok
✅ SAHNE İÇİ KESME 0 — ızgara tam 10,0 s katlarında
```

---

## ①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 05.09.2026

```
python3 RAPOR_KONTROL/rapor_kontrol.py 02_HAM_RAPORLAR/THE_STANDING_WIRE_*_HAM.md \
  --film yatay_3_5_dk_filmler/THE_STANDING_WIRE --hook 10 --klip 10 --rapor \
  --olcum-kesme 24 --olcum-sahne 24 --olcum-filigran VAR --olcum-lufs -35.5

TOPLAM 8 rapor · 🚨 8 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 0 ŞARTLI · ✅ 0 GO
🚨 🔴 TESLİM KUSURU — filigran ÖLÇÜMLE doğrulandı → parti GEÇERSİZ
tekil kararlar (parti düşmeden önce):
  ⑦ TEKRAR · ⑤ ŞARTLI · ② ŞARTLI · ⑧ TEKRAR · ⑥ TEKRAR · ④ TEKRAR · ① TEKRAR · ③ ŞARTLI
```

Betiğin yakaladığı iç tutarsızlıklar:
- ⑧ EFOR: SEVERITY TALLY (1,6,0) ≠ yazılı etiketler (3,11,0) → verdict o tally'den
  türetildi, `NOBODY PAYS` hükmü UYGULANMAZ [D161].
- ⑧ EFOR: COST CURVE düz sıfır ama altı efor olayı var → eğri ÖLÇMEDİ demektir.
- ③ SES: iki hücre "no in-scope source" yazıp 10/10 almış → düşürüldü [D131],
  ort 7,5 → 6,7.
- ⑥ FİZİK ve ① KARE: yuvarlama sapması.

---

## ⑤ ÇAPRAZ KAPI — sekiz mercek yan yana

| eksen | ölçüm | ① | ② | ③ | ④ | ⑤ | ⑥ | ⑦ | ⑧ |
|---|---|---|---|---|---|---|---|---|---|
| kesme | **24** | 24 | 23 | 23 | 23 | 24 | 24 | 24 | 24 |
| sahne | **24** | ? | 24 | ? | 24 | 24 | 24 | 24 | 24 |
| replik | ⚠️ bkz. | **1** | **4** | **4** | **4** | 0 | 0 | 0 | 0 |
| şerit (24) | `…1-11` | `…111-`(25) | **`…1-11`** ✅ | — | **`…1-11`** ✅ | `…1111` | `…1111` | `…1111` | `…1111` |

⭐ **ŞERİT KAPISI TERSİNE İŞLEDİ [D173'ün 2. vakası].** Çoğunluk (4 mercek)
`111111111111111111111111` dedi ve betik sapan olarak ② ④ ①'i işaretledi.
**Ölçüm çoğunluğu değil azınlığı doğruladı:** 215 s'de insansız sahne VAR,
② ve ④ doğru saydı. Dört mercek ortak kör noktayı paylaştı.

⚠️ **REPLİK EKSENİ AYRIŞTI — ve bu filmin en ağır sorusu.** Üç mercek (② ③ ④)
0:50-0:59 arasında **aynı dört cümleyi birebir aynı zaman kodlarıyla** yazdı;
① bir cümle diye tek satırda yazdı; dört mercek "hiçbir şey duymadım" dedi.
SPEC: `DIALOGUE LINES: 0 · SILENT SCENES: 25/25 · film TAMAMEN SESSİZ`.

**Ölçüm ne diyor:**

```
300-3400 Hz (konuşma bandı) pencere RMS
   40-50 s   −41,1 dB        100-110 s  −44,8 dB
   50-60 s   −32,4 dB  ⬅ +9…+10 dB, filmin TEK zirvesi
   60-70 s   −42,8 dB        150-160 s  −43,7 dB · 200-210 s  −62,9 dB

−30 dB eşiğinde 50-60 s içinde DÖRT ayrık patlama:
   51,2-52,3 · 53,1-54,3 · 55,3-56,5 · 58,0-59,4   (her biri ~1,2 s)
raporların iddiası:  0:50 · 0:52 · 0:55 · 0:58   ← dördü de tutuyor
```

Kadraj o sırada **sırttan**; ağız hiç görünmüyor, o yüzden lip-sync ile
çürütülemiyor. Prompt tarafı: bölüm dosyalarında **tırnak içinde tek cümle yok**
ve AUDIO blokları defalarca `No voice, no music` yazıyor.

⛔ **KAPATMA — sahip 10 saniyede kapatır, model kapatamaz:**
```
ffplay -ss 50 -t 10 "the standıng wıre (1).mp4"      # ya da herhangi bir oynatıcı
KONUŞMA VARSA  → ADAY-7'nin 3. vakası KESİNLEŞİR → ders yazılır
KONUŞMA YOKSA  → üç mercek aynı halüsinasyonu paylaştı → D151/D173 ailesi
```
Bu satır kapanana kadar ⑧ EFOR'un `Delivery vs Performance 4/10` hükmü ve
④'ün `Dialogue 4/10` hükmü ASKIDADIR.

---

## ⑩ ÖNERME KAPISI — düşen bulgular

| bulgu | kaynak | karar |
|---|---|---|
| "coil abandoned, never used — insert a shot of her dropping it" | ② | ⛔ DÜŞER — bu filmin TWIST'idir; halka S17'de bilerek bırakılır, karşılığı S24'teki boş askıdır |
| "Character is a camera-carrier; no choices made" 5/10 | ④ | ⛔ DÜŞER — merkezî seçim S17, SPEC A bloğunda sahne numaralı |
| "Theme: no cost or sacrifice" 5/10 | ④ | ⛔ DÜŞER — bedel S17, TEMA sahneleri S11·S17·S19·S24 |
| "Why she is climbing is never established" | ④ | ⚠️ AYAKTA — planlı tohum S2 (baraka duvarında tek boş askı) ekranda okunmuyor |
| "yumuşak gölge / dolgu ışığı kusuru" | ⑤ ⑥ | ⛔ DÜŞER — SPEC ATMOSFER kartı: ~1 kPa'da meşru |
| "rocks float at 0:02" | ① ⑤ ⑥ | ⚠️ AYAKTA — SPEC: tele bağlı OLMAYAN her şey 0,42 g'de normal düşer |
| "sun splits 1:20 vs 2:30" | ⑥ | ⚠️ AYAKTA — SPEC EKRAN YÖNÜ: güneş S12-S23 boyunca ekran-SOLDA |
| "wire diameter 10× at station" | ⑥ | ⚠️ AYAKTA |
| "persistent vertical line artifact 2:10-2:40" | ⑤ | ⚠️ AYAKTA |

⛔ Parti GEÇERSİZ olduğu için AYAKTA kalan bulgular da **uygulanmaz**; master
yeniden ihraç edilip koşu mod D tekrarlanınca yeniden değerlendirilirler.

---

## 🚦 SONUÇ — ne yapılır, hangi sırada

```
1. MASTER YENİDEN İHRAÇ  — filigransız, 1440p+, −14 LUFS / −1,0 dBTP
2. KUYRUK KARTI KES      — ekran metni 0 s; kafiye S24'ün son karesiyle kapanır
3. EKSİK KLİBİ ÜRET      — insansız yanaşma vuruşu (şeritteki kayıp hane)
4. HOOK'U KIRP           — S0 10,0 → 9,0 s
5. PLANLI SESSİZLİĞİ AÇ  — 214,0-239,0 s hard mute, kurguda
6. 0:50-0:59 DİNLE       — replik var mı; varsa ses yatağı yeniden kurulur
7. QA'YI MOD D TEKRARLA  — PAKET_1..8 zaten hazır [D165]
```

⛔ 1-5 arası **kurgu işidir, yeniden üretim değildir.** 24 klibin hiçbiri
yeniden üretilmek zorunda değil.
