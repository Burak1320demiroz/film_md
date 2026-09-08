# ⚡ THE OPEN CIRCUIT — FİLM KAYDI

> **Durum:** film üretildi ve birleştirildi · **master ÖLÇÜLDÜ** ✅ · **kurgu YAPILMAMIŞ**
> **Koşu:** 08.09.2026 · **on iki mercek** (① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE ·
> ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK)
> — **on ikisi de mod V.**
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T12'YE GİRMEDİ.** Üç ayrı kapı aynı hükmü verdi:
> ① SPEC kapısı [D129]: `THE_OPEN_CIRCUIT_QA_SPEC.md` **VAR** *ve* paket
>   `QA_PROMPTLARI/FILME_OZEL/THE_OPEN_CIRCUIT/PAKET_1..12` **VAR** (07.09.2026'da üretilmiş) —
>   operatör yine çıplak rubriği yapıştırdı. **SPEC hazırken mod V koşulan film: 13.**
> ②.9 TESLİM KAPISI [D188]: plan **25 sahne**, makarada **23 klip** → parti GEÇERSİZ.
> ③ TESLİM SINIFI [D181 · D150]: **filigran** 23/23 klipte + kuyrukta 5 s kart → 🚨 **HAM ZİNCİR**.
>
> ⭐ **AMA BU KAYIT ASKIDA DEĞİL.** ⑪ ölçüm kapısı koşuldu ve makara KAREYLE okundu.
> Aşağıdaki 🔴 bulguların **hiçbiri bir rapordan gelmiyor** — hepsi ölçümden ve karelerden
> geliyor, ve **on iki merceğin on ikisi de hepsini kaçırdı.**

---

## 📦 MALZEME

```
MASTER:   /Users/dai/Downloads/the open cırcuıt (1).mp4
          235,136 s · 3840x2160 · 30 fps · ses kanalı VAR · 226,6 MB
İKİZ:     /Users/dai/Downloads/the open cırcuıt.mp4 — AYNI SÜRE (235,136 s), 1280x720
          Aynı kurgunun iki çözünürlüğü; ⑪.0 kimliği 4K'dan alındı, kesme ızgarası birebir aynı.
          ⚠️ ⑦ AKSİYON künyesi `the open cırcuıt_2.mp4`, ⑧ EFOR künyesi `the open cırcuıt_3.mp4`
             yazıyor. Bu adlarda dosya diskte YOK; iki mercek hangi dosyaya koştuğunu
             kanıtlayamıyor [D160 — dosya adı kimlik değildir].
KART:     230,13 – 235,14 s · 5,0 s · BAŞLIK KARTI "THE OPEN CIRCUIT / YOU DON'T HAVE TO
          TOUCH IT TO GET SHOCKED" (freezedetect: 230,1'den dosya sonuna donuk)
          ⛔ Her sahnenin NEGATIVE bloğu "no title card, no captions" yazıyor. Kart hem
          SAYIMIN hem SÜRENİN dışında tutuldu [D93 · D120], 🔴 loglandı [D70/D72].
GÖVDE:    230,1 s = **23 klip × 10,0 s**
          kesme ızgarası: 10 · 20 · 30 … 230 (scene>0,3 bunların 19'unu gördü; 10/60/70/80
          karanlık ya da eş kurulum olduğu için kaçtı — ızgara 10 s katıdır ve replik
          ekseni ±1,0 s ile doğruladı)
PLAN:     25 sahne · 249,0 s = 9 s hook + 24 × 10 s
MERCEK:   ① 3,6 · ② 5,4 · ③ 5,3 · ④ 2,8 · ⑤ 5,0 · ⑥ 7,0 · ⑦ 7,7 · ⑧ 1,0 · ⑨ 3,0 ·
          ⑩ 2,9 · ⑪ 4,8 · ⑫ 5,0   (rapor_kontrol düzeltmesi sonrası; **hiçbiri tabloya girmez**)
```

---

## §⑪ ÖLÇÜM KAPISI — `olcum_kapisi.sh` · 08.09.2026 · **KOŞULDU**

| ölçüm | değer | SPEC / plan ne diyor | sonuç |
|---|---|---|---|
| süre | **235,14 s** | 249,0 ± 1,0 s (SPEC KAPI ①) | ⛔ **−13,9 s** |
| gövde (kartsız) | **230,1 s** | 249,0 s | ⛔ **−18,9 s ≈ 2 klip** |
| klip | **23** | CLIP COUNT 25 | ⛔ **−2 klip** |
| ASL | **10,0 s** | 9,96 s (9,0-10,0 bandı) | ✅ bandın içinde |
| hook klibi | **10,0 s** | 9,0 s | ⚠️ +1,0 s |
| ses kanalı | **VAR** | 5 katmanlı diegetik tasarım | ✅ kanal var |
| sessizlik (−50 dB / 0,3 s) | **DOSYADA TEK ARALIK YOK** | 193,0-195,0 s planlı HARD MUTE (SPEC KAPI ③) | 🔴 **planlı sessizlik teslim EDİLMEDİ** [D180] |
| loudness | **I = −16,6 LUFS · Peak 0,0 dBFS** | −14 LUFS / −1,0 dBTP | 🔴 **İHRAÇ KUSURU** (hem hedefin altında hem tepede kırpıyor) |
| köşe testi | **FİLİGRAN VAR** — sağ altta siyah disk + camgöbeği ok, 0→229 s her örnekte | her promptta "no watermark" | 🔴 **TESLİM KUSURU [D150]** |
| kuyruk kartı | **230,13 → son** | ekran metni 0,0 s | 🔴 **[D70 · D72]** |
| karanlık taban | 49 s sonrası **min YAVG = 28,8/255** | ≥ 8/255 (SPEC KAPI ②) | ✅ **GEÇTİ** — gölgenin içi dolu |
| TESLİM SINIFI | 🚨 **HAM ZİNCİR** | — | ⛔ mercek koşulmaz, rapor okunmaz, satır yazılmaz |

```
⛔ DÖRT TESLİM KUSURU. Bu master master DEĞİLDİR:
   ① üretici filigranı 230 saniyenin 230'unda duruyor
   ② kuyrukta 5 saniyelik başlık kartı var (her prompt onu yasaklıyor)
   ③ −16,6 LUFS / 0,0 dBFS
   ④ planlı 2 saniyelik mutlak sessizlik hiç uygulanmamış — bıçak KURGUDAYDI [D180]
   Beşincisi teslim değil ÜRETİM kusuru: iki sahne makarada yok (aşağıda).
```

---

## §①.9 TESLİM KAPISI [D188] — **HANGİ İKİ SAHNE MAKARADA YOK**

Makaranın 23 yuvası, planın 25 sahnesine kareyle ve replik ekseniyle eşlendi.
Her satırın kanıtı ya bir KARE ya bir REPLİK zaman kodudur.

| yuva | in-out | ekranda ne var | plan sahnesi | kanıt |
|---|---|---|---|---|
| 0 | 0-10 | ECU: eldiven kelepçeye uzanır — **kıvılcım YOK** | S0 | kare 3-9 s |
| 1 | 10-20 | aynı kurulum; **kıvılcım 14,20 s'de atlar** | S1 | kare 14,20 |
| 2 | 20-30 | ikisi ayakta — **giysi tasarımı filmin geri kalanıyla AYNI DEĞİL** | **S3** | replik #1 21 s · #2 25 s |
| 3 | 30-40 | bot + mast ayağı + yanan şeritler | **S2** | kare 35 s |
| 4 | 40-50 | diz çökmüş, kangal bırakılır | S4 | kare 45 s |
| 5 | 50-60 | ikisi ovaya bakar | S5 | replik #3 52 s |
| 6 | 60-70 | LS: üssün tamamı | S6 | kare 65 s |
| 7 | 70-80 | EWS: toz halkası + **boşalma 73,1-73,3** | S7 | YAVG sıçraması |
| 8 | 80-90 | LS: gece, üs | S8 | kare 85 s |
| 9 | 90-100 | ikisi diz çökmüş, plaka | S9 | replik #4 91 s · #5 96 s |
| 10 | 100-110 | CU: kelepçe | S10 | kare 105 s |
| 11 | 110-120 | ikisi karşılıklı | S11 | replik #6 111 s · #7 114 s |
| 12 | 120-130 | CU: kalça + kesici | S12 | kare 125 s |
| 13 | 130-140 | iç mekân, kol | S13 | replik #8-#10 131/134/136 |
| 14 | 140-150 | MCU: kadın | S14 | replik #11 144 s |
| 15 | 150-160 | iç mekân, gaz girer | S15 | replik #12 152 s · flaş 154,5/157,1 |
| 16 | 160-170 | MCU: adam | S16 | replik #13 161/163 |
| 17 | 170-180 | **DIŞARISI**, gece, diz çökmüş, ayak oturtuluyor | **S18** | kare 175 s |
| 18 | 180-190 | ikisi, kesici kabloda | S19 | replik #16 181 s · #17 186 s |
| 19 | 190-200 | CU: kabuk sıyrılır | S20 | replik #18 190-195 · #19 197 |
| 20 | 200-210 | ECU: kayış oturur | S21 | kare 205 s |
| 21 | 210-220 | ikisi arkadan, üs | **S23** | replik #21 212 s · #22 214/216 |
| 22 | 220-230 | LS: mast; **222,3 ve 226,3'te ŞİMŞEK iner** | S24 | kare 222,2-222,7 |

```
⛔ MAKARADA OLMAYAN İKİ SAHNE — ADIYLA:

  S17 "HE TAKES IT DOWN"  (169-179 s · iç mekân)
      Adam kesiciyi duvardan indirir ve kapağa döner — planın "AYRILIK TERSİNİR"
      vuruşu. Yuva 17'de bunun yerine S18 (dışarısı) duruyor.
      ⭐ İKİNCİ KANIT: bu sahnenin repliği "Counted." (SPEC B #14 · 173,5 s)
        ON İKİ RAPORUN HİÇBİRİNİN `LINES HEARD` satırında YOK.

  S22 "⭐DORUK b · IT GOES DOWN"  (219-229 s · ECU · KÜME ②)
      Sıradaki boşalma kayıştan AŞAĞI, eldivenin yanından TOPRAĞA iner.
      Planın DORUĞU ve filmin tek cümlelik vaadi. Yuva 21'de bunun yerine S23 duruyor.
      ⭐ İKİNCİ KANIT: bu sahnenin repliği "Ground path is closed." (SPEC B #20 · 221,0 s)
        ON İKİ RAPORUN HİÇBİRİNİN `LINES HEARD` satırında YOK.

  ⛔ ÜÇÜNCÜ ARIZA — SIRA: S2 ile S3 YER DEĞİŞTİRMİŞ (yuva 2 = S3, yuva 3 = S2).
     Şerit bunu göremez (`1111111111111111111111` — insansız yuva yok, D163'ün
     "şerit ÖLÇMEDİ" hâli); replik ekseni gördü: #1/#2 planda 30,5/34,5 s,
     makarada 21/25 s — tam bir klip erken.

⛔ Kapı ateşledi: kesme listesi · REMOVE reçetesi · yeniden üretim UYGULANMAZ.
   Soru QA masasından ÜRETİM masasına geçti: iki klip üretilmemiş mi, kurguya mı girmemiş?
```

---

## §④ KURGU KAPISI — dört satır

| satır | plan | makara | sonuç |
|---|---|---|---|
| a) klip sayısı | 25 | **23** | ⛔ DÜŞTÜ |
| b) süre ±2 s | 249,0 s | **230,1 s** (kartsız) | ⛔ DÜŞTÜ (−18,9 s) |
| c) insan şeridi | tek kâşifli değil, 25/25 insanlı | `1111111111111111111111` | ⚠️ **ÖLÇMEDİ** [D163] — insansız yuva 0/23 ≤ 1/10, şerit sabittir ve sıra eksenini ölçemez. Sıra ⑪'in sahne ızgarasından okundu (yukarıdaki tablo) ve **BOZUK** çıktı. |
| d) FİNAL VURUŞ KANITI [D141] | S24'te "ufukta cephenin kuyruğunun arkasında ince açık bant" + üs KARANLIK | kare 225 s: ince açık bant **VAR** ✅ · üs **YANIYOR** 🔴 | ⛔ yarım |

```
⭐ DÖNGÜ AYRI KANITTIR: ilk kare (ECU kelepçe, gündüz) ile son kare (LS mast, gece)
  aynı kurulum değil — plan da zaten S24'ü S6/S8'in eş kadrajı yapıyor, S0'ın değil.
  ⑨ KADRAJ'ın "rhyme pair fail → S22'yi yeniden üret" hükmü bu yüzden PLANA AYKIRI
  bir sipariştir [⑩ önerme kapısı] — ve zaten S22 makarada yok.
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 08.09.2026 · **12 rapor**

```
--film yatay_3_5_dk_filmler/THE_OPEN_CIRCUIT --hook 10 --klip 10
--olcum-kesme 22 --olcum-sahne 23 --olcum-filigran VAR --olcum-lufs -16.6

🚨 TESLİM EKSİK — plan 25 sahne, ÖLÇÜLEN 23 [D188] → parti GEÇERSİZ
🚨 TESLİM KUSURU — filigran ölçümle doğrulandı [D150 · D177]
🚨 GEÇERSİZ  ④ HİKAYE   iddia n=10 Σ=32 ort=3,2 │ hücreler n=10 Σ=28 ort=2,8 — ARİTMETİK FABRİKE
🚨 GEÇERSİZ  ⑨ ⑩ ⑪ ⑫ · plan sadakati merceği mod V → KARANTİNA [D190 · bu koştuda doğdu]
⛔ TEKRAR    ① ⑥ ⑦ ⑧ · D129 (SPEC var, mod V)
⚠️ ŞARTLI    ② ③ · belgesiz mercek, ama parti geçersiz
✅ GO        ⑤ (tek başına) — parti geçersiz olduğu için satır yine yazılmaz
TOPLAM       12 rapor · 🚨 12 GEÇERSİZ · ✅ 0 GO

⚠️ Beş rapor SEVERITY TALLY ≠ yazılı etiket (① ② ③ ⑥ ⑦ ⑪) → verdict'ler türetilemez [D161]
⚠️ 13 hücre "no in-scope source" / "kusur yok" olduğu hâlde 7-10 puan taşıyordu [D131 · D186]
⚠️ ⑦ ORTAK DEFTER ŞÜPHESİ [D110]: ⑤ + ⑥ künyeleri BİREBİR aynı ve çoğunluktan sapıyor
⚠️ ① KARE şeridi 21 hane (çoğunluk 22) · ⑩ GAZE STRING 23 hane (kesme+1 = 22)
⚠️ ① KARE ızgarası +10 s kaymış — 10,03'teki kesmeyi görmemiş (S0/S1 eş kurulum kümesi)
```

```
⭐ ①.10 GÖZ KAPILARI [D191 · bu koşuda doğdu] — betik SPEC'in F bloğundaki
  12 maddeyi artık her koşuda ⬜ listesi olarak basıyor. Bu filmde beşi
  kareyle DÜŞTÜ (aşağıdaki "SPEC MAKİNE VE GÖZ KAPILARI" tablosu).
```

---

## §⑤ ÇAPRAZ SAYIM KAPISI — beş satır

| eksen | sonuç |
|---|---|
| **kesme** | ölçüm 22 · raporlar 21 (10 mercek) / 22 (⑤ ⑥) → fark ≤ 1, eksen doğrulandı; sapma 10,03'teki eş kurulum kesmesi |
| **sahne** | ölçüm 23 · raporların hepsi 22 → hepsi aynı yönde yanılıyor (S0+S1 kümesini tek sahne saydılar) |
| **şerit** | 10 mercek `1111111111111111111111`, ① KARE 21 hane 🚨 |
| **replik** | 🚨 **ÜÇ AYRI GRUP**: 25 replik (① ② ③ ④) · 22 replik (⑥ ⑦ ⑧) · 16 replik (⑨ ⑩ ⑪ ⑫). Grup içi metinler BİREBİR aynı. **Bağımsız ölçüm sayısı en fazla 3'tür, 12 değil** [D110]. Üç grubun üçü de SPEC'in 22 kaydına oturmuyor. |
| **metin / SUSKUNLUK** | Hiçbir rapor **filigranı** yazmadı — sahibi ① KARE de yazmadı 🚨 SUSKUNLUK [D162]. 235 saniyenin 230'unda duran sabit köşe işareti on iki mercekten geçti. |

---

## §③ KİMLİK KAPISI [D105] — iki metin-dışı çapa

| çapa | rapor ne dedi | belgede ne yazıyor | eşleşti mi |
|---|---|---|---|
| vuruş | "kneeling astronaut sets a rolled strap down on the dirt" (0:40) | S4 · "kadın kangalı ikinci ayağın olduğu yere bırakır" | ✅ |
| sayısal kilit | "four-segment habitat module" (0:19) | KART 13 · dört modül + düğüm + mast | ✅ |

Eşleşme = 2 → koşu bu filme atfedilebilir. (Başlık kartı çapa olarak KULLANILMADI.)

---

## §② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — rapor mu saptı, film mi

| # | rapor ne dedi (tc) | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | ② "Visors flip from UP (faces exposed) to DOWN" 🔴 BLOCKER (1:30 / 1:50) | PLAN §ORTAM: "vizör 25/25 KAPALI, ara durum YOK · cam optik BERRAK [D79]" | kare 91 s + 184 s | **RAPOR YANLIŞ OKUDU** — kask 25/25 kapalı, cam berrak. Şeffaf pencereyi "açık vizör" sanmış. Bulgu DÜŞER, 🔴 BLOCKER iptal. |
| 2 | ② "arm band flips left↔right" 🟠 (2:20 vs 3:00) | REFERANS §"never swap strap limb" | kare 91 · 184 · 215 | **⬜ AÇIK** — 91/184'te bant aynı kolda; ön/arka çekim aynası ayıklanmadan hüküm verilemez. Sayı taşımaz. |
| 3 | ② "chest stains disappear" 🟠 | göz kapısı ⑦ · kir MONOTONİK [D147] | kare 145 vs 196 | **⬜ AÇIK** — iç mekânda temiz, dışarıda kirli; kir fazı sahne sırasıyla okunmadı. |
| 4 | ⑥ "Blue beam shoots **UP** mast · 3,3 m/s" (3:40) | SPEC göz kapısı ⑤ · "S22'de kıvılcım AŞAĞI iner; yukarı çıkıyorsa filmin doruğu YOKTUR" | kare 222,2→222,7 | **RAPOR YANLIŞ OKUDU** — boşalma GÖKTEN AŞAĞI iner ve **masta değil PLAKAYA** vurur. ⑥'nın tek doruk ölçümünün hem yönü hem hedefi yanlış; üstüne Işık-Gölge 10/10 verilmiş. |
| 5 | ⑫ "Peak Placement 9/10 — S22 03:40 lands perfectly" | SPEC C · DORUK S22 · 222,5 s | yuva eşlemesi | **FİLM SAPTI** — 3:40'ta izlenen sahne S24'tür; planın doruğu S22 **makarada yok**. Var olmayan bir doruğa 9/10 verilmiş. |
| 6 | ③ "'Crust first' üç kez tetikleniyor" 🟡 · "'Node is open' iki kez" | SPEC B · her replik BİR kez | konuşma bandı zarf analizi (350-3200 Hz) sonuç vermedi | **⬜ AÇIK · KULAK** — müzik yatağı eşik ayrımını yutuyor; ölçülmeden tabloya girmez. Üç rapor grubunun replik sayısı da bu yüzden ayrışıyor olabilir. |
| 7 | ③ "dış rüzgâr iç mekânda aynen sürüyor" 🟠 | PLAN §3.10 · iç zemin = sürekli fan uğultusu | — | **⬜ AÇIK · KULAK** |
| 8 | ⑤ "habitat mutates / module count 4→2" 🟠 | KART 13 · dört modül sabit | kare 65 · 91 · 215 · 225 | **FİLM SAPTI** — 91 s'de modül dizisi bir trene benziyor (10+ pencere), 215/225'te iki-üç gövde. Ölçek/sayım kilidi tutmamış. |

---

## §⑩ ÖNERME KAPISI [D87 · D116 · D130 · D134] — düşen siparişler

| bulgu / sipariş | hangi mercek | plan ne diyor | karar |
|---|---|---|---|
| "S4'ü KES — kangal hiçbir işe yaramıyor" | ④ | S4 = **⭐TEMA #1 (NESNE)** · motif kanalının ilk vuruşu | ⛔ DÜŞER — filmin tema zincirini kesiyor |
| "S3'ü (mast ayağı) KES — gereksiz" | ④ | S2 = bitmiş ayağın tek kanıtı (sayaç 1/4) | ⛔ DÜŞER — sayaç eksenini siler |
| "S12'yi (kalçadaki kesici) KES — hiçbir yere varmıyor" | ④ | S12 = **el 4** · S17/S19'un kesici kurulumu | ⛔ DÜŞER — ödemenin kurulumunu siler |
| "S14'ü KES — devamlılığı bozuyor" | ② | S14 = **göz 1** · kadının tek cevabı | ⛔ DÜŞER |
| "S22'yi S1'in eş kadrajı olarak yeniden üret" | ⑨ | S24 planlı olarak S6/S8'in eş kadrajıdır | ⛔ DÜŞER — ve zaten S22 makarada yok |
| "başlık kartını kaldır, döngüyü öldürüyor" | ⑫ | her prompt "no title card" · ekran metni 0,0 s | ✅ **AYAKTA** — tek doğru sipariş; kart kesilir |
| "vizörleri kapalı yeniden üret (S9/S18)" | ② | vizörler zaten 25/25 kapalı | ⛔ DÜŞER (defter #1) |

> ⭐ ALTINCI SATIR — NOVUM SINIRI [D183]: bu filmin novum'u "fırtına İTMEZ, YÜKLER" ve
> "patlama BASINÇ olayıdır, alev yoktur". Sınır cümlesi: *dışarıda süregiden alev
> İMKÂNSIZDIR; boşalma TEK, İNCE, DÜZ ve SÖNÜMLÜ bir çizgidir.*
> **Sınır KAREYLE sınandı ve İHLAL EDİLDİ** — aşağıdaki 🔴 4.

---

## 🔴 ÖLÇÜMÜN BULDUĞU, ON İKİ MERCEĞİN KAÇIRDIĞI

| # | bulgu | kanıt | kaç mercek yazdı |
|---|---|---|---|
| 1 | **İki sahne makarada yok** (S17 · S22 — biri filmin DORUĞU) | yuva eşlemesi + iki repliğin hiçbir raporda olmaması | **0 / 12** — ⑫ üstüne "peak 9/10" verdi |
| 2 | **Üretici filigranı** 230 saniyenin 230'unda, sağ alt köşede | `kose_*.png` · her kare | **0 / 12** |
| 3 | **S2 ↔ S3 yer değiştirmiş** | replik #1/#2 bir klip erken | **0 / 12** |
| 4 | **Doruk boşalması ŞİMŞEK olarak üretilmiş** — kalın, dallanan, kadraja ışık bırakan; her promptun NEGATIVE'i "no lightning bolt, no plasma beam, no continuous glow" diyor | kare 222,2-222,7 · 226,3-226,5 | **0 / 12** (⑥ ölçtü, yönünü ters yazdı ve 10/10 verdi) |
| 5 | **Işık takvimi geri yandı** — S19'da sönen şeritler aynı klibin sonunda (189 s) geri geliyor, S23/S24'te üs YANIYOR; oysa S23/S24 promptu "No window strip is lit and no structure light is on anywhere" diyor | YAVG 183:58,8 → 186:29,5 → 189:47,5 · kare 215 · 225 | **0 / 12** (⑪ yalnız key yönü yazdı) |
| 6 | **ABD bayrağı yaması** adamın omzunda | kare 196 s | **0 / 12** — her promptta "No flag, agency logo, mission patch" · ASTRONOT_DONANIM §1 "gerçek bayrak YOK" |
| 7 | **Kask ön penceresi KUBBE** — referans sayfası "FLAT window in a visible rim — no bubble helmet" diyor | kare 145 · 184 · 215 | **0 / 12** [D146] |
| 8 | **Planlı 2 s mutlak sessizlik hiç uygulanmamış** (193-195 s) | silencedetect: dosyada tek aralık yok | **0 / 12** (③ "ambience hole: None" yazdı — doğru gözlem, eksik soru) |
| 9 | **Katalizör 10 s geç** — kıvılcım S0'da (4,0 s) değil S1'de (14,20 s); S1'in NEGATIVE'i "No spark in this frame" | kare 3-9 s (kıvılcım yok) · 14,20 (kıvılcım var) | **0 / 12** |
| 10 | **İhraç kilidi tutmamış** — −16,6 LUFS / 0,0 dBFS | ebur128 | **0 / 12** |
| 11 | **Yuva 2'nin giysi tasarımı filmin geri kalanıyla aynı değil** — ince, kemerli tulum; diğer 22 klipte kalın göğüs plakalı EVA giysisi | kare 25 s ↔ 91 s | **0 / 12** (② yalnız "band flips" yazdı) |

---

## 🧾 SPEC MAKİNE VE GÖZ KAPILARI — sonuç

| kapı | sonuç |
|---|---|
| KAPI ① teslim sayımı (249 ± 1 s) | 🔴 **DÜŞTÜ** — 235,1 s |
| KAPI ② karanlık taban (YAVG ≥ 8) | ✅ **GEÇTİ** — min 28,8 |
| KAPI ③ planlı sessizlik | 🔴 **DÜŞTÜ** — aralık yok |
| KAPI ④ kamera sabitliği (ikame) | ⚪ gözlem satırı üretildi; kuyruk kartı dışında donma yok |
| GÖZ ① ağız (0 kare konuşan ağız) | 🔴 **DÜŞTÜ** — S14/S16/S19/S20 yuvalarında yüz ve ağız kadrajda |
| GÖZ ② kask (çerçeveli + DÜZ pencere) | 🔴 **DÜŞTÜ** — kubbe/kavisli pencere |
| GÖZ ④ kıvılcım (tek, ince, düz, sönümlü) | 🔴 **DÜŞTÜ** — şimşek |
| GÖZ ⑤ yön (S22'de aşağı) | ⚠️ boşalma AŞAĞI iniyor ✅ ama S22 makarada yok; olay S24'e taşınmış |
| GÖZ ⑧ şerit 4→3→2→0 monotonik | 🔴 **DÜŞTÜ** — geri yanıyor |
| GÖZ ⑫ metin (hiçbir yüzeyde) | 🔴 **DÜŞTÜ** — başlık kartı + filigran |
| GÖZ ⑪ iki figür | ✅ üçüncü gövde/klon görülmedi |

---

## 📌 SİPARİŞ — sıra değişmez

```
1. ÜRETİM MASASI: S17 ve S22 üretildi mi? Üretildiyse kurguya neden girmedi?
   (S22 filmin DORUĞU ve İPTAL KAPISI'dır — plan onsuz filmin doruğu YOKTUR der.)
2. S22 yeniden üretilirken: boşalma TEK · İNCE · DÜZ · SÖNÜMLÜ, kayıştan AŞAĞI.
   Şimşek değil. Aynı düzeltme S24'ün iki boşalmasına da uygulanır.
3. S3'ün giysisi referans sayfasıyla yeniden üretilir; S2/S3 sırası düzeltilir.
4. Işık takvimi: S19'dan sonra hiçbir pencere şeridi yanmaz (S19 sonu · S20-S24).
5. Bayrak yaması ve kubbe kask taşıyan her klip yeniden üretilir.
6. KURGU: kart kesilir · 193-195 s HARD MUTE uygulanır · master FİLİGRANSIZ ve
   −14 LUFS / −1,0 dBTP ile yeniden ihraç edilir.
7. Yeni master ölçülür (TESLİM SINIFI temiz çıkmalı), SONRA on iki mercek
   PAKET_1..12 ile **mod D** koşulur. Bu koşu tekrarlanmadan hiçbir T satırı yazılmaz.
```

---

## 📚 BU KAYITTAN DOĞAN DERSLER — dördü de YAZILDI ve KAPIYA İNDİ

| ders | ne | KAPI (nerede koşuyor) |
|---|---|---|
| **D190** | ⑨-⑫ mod V'de boş değil TERSİNE çalışır — ⑫ makarada olmayan doruğa 9/10 verdi | BETİK · `rapor_kontrol.py` ⑨-⑫ mod V = 🚨 GEÇERSİZ + dört rubriğin STEP −1'i mod V'de DURDURUR |
| **D191** | SPEC'in göz kapılarını koşan mercek yok — 12 maddenin 5'i ihlal, 12 mercekte 0 bulgu | BETİK · `rapor_kontrol.py` ①.10 F bloğunu ⬜ listesi basar |
| **D192** | Filmin 1 numaralı riski tarif kilidiyle korundu, doruk ŞİMŞEK geldi | LİSTE · `03_PLAN_ONCESI_KONTROL_LISTESI.md` **A5** (risk SAYIYLA yazılır) |
| **D193** | Işık takvimi yazıldı, ölçülmedi — sönen şeritler geri yandı | BETİK · `olcum_kapisi.sh` **IŞIK TAKVİMİ İZİ** (↑ · ⟳) |

**TEKRAR sayacı artan dersler:** D129 (15→**16** film) · D150 (5→**6**) ·
D165 (2→**3** ⛔ ÇALIŞMIYOR) · D146 (3→**4**) · D70 (11→**12**) · D72 (12→**13**) ·
D180 (2→**3** ⛔ ÇALIŞMIYOR) · D110 (3→**4**) · D125 (3→**4**) · D181 (1→**2**) ·
D188 (0→**1** ⭐ ÇALIŞIYOR — kapı ilk kez ateşledi ve partiyi düşürdü)
