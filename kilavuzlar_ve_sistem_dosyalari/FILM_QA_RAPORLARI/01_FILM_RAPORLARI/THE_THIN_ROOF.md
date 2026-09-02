# 🕳️ THE THIN ROOF — FİLM KAYDI

> **Durum:** film üretildi ve kurgulandı · teslim dosyası `~/Downloads/the thın roof.mp4`
> **Ölçüm:** 28.08.2026 · **altı mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE
> · 🖼️ ARKA PLAN · ⚖️ FİZİK) — **altısı da mod V.**
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T6'YA GİRMEDİ.** Sebep tek ve kesin: film klasöründe
> `THE_THIN_ROOF_QA_SPEC.md` **VARDIR** ve altı raporun altısı `INPUT MODE: V`
> yazıyor → ortak adım ① gereği koşu TEKRARLANIR; ham rapor 02/'ye düşer,
> T tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi UYGULANMAZ [D129].
> **SPEC yazılmış olduğu hâlde mod V koşulan film sayısı artık 7.**
>
> ⭐ **BU KOŞUNUN GERÇEK ÇIKTISI SKOR DEĞİL, ÖLÇÜM VE KARELERDİR.** Master
> ffprobe/ffmpeg ile ölçüldü, tartışmalı 6 saniyenin karesi tek tek çıkarılıp
> gözle bakıldı. Sonuç: **18 etiketli bulgunun 4'ü gerçek**, 6'sı ⑩'da düştü,
> 8'i açık kaldı — ve **filmin ölçülmüş 6 gerçek ihlalinin 6'sı da raporlarda
> YOK.** Altı yeni ders buradan çıktı: **D137-D142**.

---

## 📦 MALZEME VE HAM DOSYALAR

```
MALZEME:  teslim kurgusu · 65,030 s · 720×1280 · 30 fps · AAC stereo 48 kHz
MERCEK:   🔧 1_KARE · 🔗 2_DEVAMLILIK · 🔊 3_SES · 📖 4_HIKAYE
          · 🖼️ 5_ARKA_PLAN · ⚖️ 6_FIZIK   (altısı da mod V)
OTURUM:   🚨 ŞÜPHELİ [D110] — ② ⑤ ⑥ raporlarının OUT-OF-SCOPE satırları,
          ①'in TOP 3 listesini timecode ve severity etiketi dâhil BİREBİR
          tekrar ediyor (0:35 🔴 · 0:43 🟠 · 0:52 🟠, hatta "Motion jello /
          robotic movement on character push-up" cümlesiyle). Bağımsız
          ölçüm bu kadar aynı çıkmaz; bu doğrulama değil KOPYADIR.
HAM:      ../02_HAM_RAPORLAR/THE_THIN_ROOF_{KARE,DEVAMLILIK,SES,HIKAYE,ARKA_PLAN,FIZIK}_HAM.md
PLAN:     ../../../dikey_shorts_filmler/THE_THIN_ROOF/THE_THIN_ROOF_DIKEY_SHORTS.md
SPEC:     ✅ VAR — ../../../dikey_shorts_filmler/THE_THIN_ROOF/THE_THIN_ROOF_QA_SPEC.md
          (A/B/C/D/E blokları · D bloğu 24 satırlık KİLİT LİSTESİ ·
           E bloğu 3 makine kapısı) — ⛔ operatöre VERİLMEDİ
KAYNAK KLİPLER: ~/Downloads/Woman_{walking_on_dark_pavement,kneeling_on_rock_edge,
          crouches_near_rock_edge,crawling_on_rock_pavement,lying_on_rock_edge,
          watching_rolling_stone}_2026082716-17.mp4
MÜZİK:    ~/Downloads/Lithosphere.mp3 (27.08 17:17)
```

---

## ⭐ ⑪ ÖLÇÜM KAPISI — master'dan okunan sayılar (rapor sayıları DEĞİL) [D125]

```bash
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "/Users/dai/Downloads/the thın roof.mp4"
```

| ölçüm | master | raporlar ne dedi | hüküm |
|---|---|---|---|
| süre | **65,030 s** | altısı da "64 s measured" | ⚠️ altısı da 1 s eksik ölçtü |
| çözünürlük | **720 × 1280** | ölçülmedi | 🔴 ihraç eşiği 1440p+ — **ALTINDA** |
| kare hızı | **30 fps** | ⑥ "FRAME RATE ASSUMED: 24 fps" | 🚨 ⑥'nın türettiği HER süre %25 hatalı |
| ses kanalı | **VAR** · AAC stereo 48 kHz · 253 kbps | altısı da "no audio information at all" | 🚨 **ALTISI DA YANILDI → D137** |
| entegre gürlük | **−17,3 LUFS** · LRA 14,1 LU · tepe −0,9 dB | ③ "AUDIO ABSENT — RUN NOT STARTED" | 🚨 hedef −14 LUFS · 3,3 LU altında |
| sessizlik (−50 dB / 0,3 s) | **tek aralık yok** | ③ "not one sound in the entire runtime" | 🚨 ölçüm çürüttü |
| kesme ızgarası | 10,033 · 20,033 · 30,033 · 40,033 · 50,033 · **60,033** | altısı da 5 kesme (60,033'ü saymadı) | kart sınırı sayılmamış — kabul |

**IZGARA:** 6 klip × 10,033 s = **60,20 s** · sahne dışı kart **60,033 → 65,030 = 4,997 s**

---

## ⛔ ④ KURGU KAPISI — önce ayıkla, sonra say [D93 · D109 · D118 · D120]

**SAHNE-DIŞI MALZEME:** başlık kartı, **4,997 s**, kurgunun SONUNDA.
🔴 loglandı [D70/D72] · sayımın VE sürenin dışında tutuldu.

| satır | plan | master (karttan arındırılmış) | sonuç |
|---|---|---|---|
| a) klip sayısı | SCENE / SHOT / CLIP = 6 / 6 / 6 | 6 / 6 / 6 | ✅ |
| b) süre | 60,03 s ± 0,5 | **60,033 s** | ✅ (Δ = +0,003 s) |
| c) İNSAN ŞERİDİ [D118] | `111111` | `111111` (dört raporda da aynı) | ✅ |

⭐ **Kurgu kapısının üç satırı da geçti — ve film yine de finalini teslim etmedi.**
Kapı klip SAYAR, vuruş sayamaz. Ayrıntı §⑨ ve **D141**.

---

## 🧭 ⑨ HİZALAMA KAPISI — ızgara PLANDAN alınır [D115]

`sahne başlangıcı(n) = 0 + (n−1) × 10,033`

| plan sahnesi | plan aralığı | master aralığı | raporların "sahnesi" |
|---|---|---|---|
| S0 kanca · yürüyüş · tohum · kapak anı | 0,00–10,01 | 0,000–10,033 | "Scene 1 · Lava plain" |
| S1 diz çöküş · birinci avuç testi | 10,01–20,01 | 10,033–20,033 | "Scene 2 · Canyon edge" |
| S2 **ASİMETRİ ANI · halka kapanır** | 20,01–30,02 | 20,033–30,033 | "Scene 3 · Circular depression" |
| S3 çıkıntı · EL YUVASI | 30,02–40,02 | 30,033–40,033 | "Scene 4 · Cliff edge (close-up)" |
| S4 çakıl · merkezî seçim | 40,02–50,03 | 40,033–50,033 | "Scene 5 · floating stones" |
| S5 ayağa kalkış · TWIST · döngü | 50,03–60,03 | 50,033–60,033 | "Scene 6 · Aftermath" |

🚨 **Raporların sahne 1-6 numaralandırması planın S0-S5'iyle bir yuva kaymıştır.**
Bütün rapor timecode'ları bu kaydırmayla okunmalıdır; "S3 vs S5" diye yazılan
her karşılaştırma aslında **S2 vs S4**'tür. ② ve ⑤'in "circular depression S3 →
massive hole S5" çelişkisi bu yanlış eşlemenin üstüne kurulmuştur.

---

## 🔧 SPEC E BLOĞU — ÜÇ MAKİNE KAPISI, İLK KEZ KOŞULDU

> ⛔ Bu kapılar SPEC'te yazılıydı ve **QA koşusundan önce koşulmamıştı.**
> Aşağıdaki sayılar 28.08'de bu kayıt yazılırken alındı.

### ① GÖLGE DOLGUSU KAPISI — bu filmin varlık şartı
Ölçüm: her sahnenin +5. saniyesi, kare 8×14 bloğa indirgenip (blok ≈ 90 px)
her bloğun luma ortalaması okundu. Eşik: **YAVG < 18/255 → sahne reddedilir**,
beklenen bant 28-55.

| sahne | en koyu blok | kare ortalaması | <18 olan blok | hüküm |
|---|---|---|---|---|
| S0 | **29** | 117 | 0/112 | ✅ bantta |
| S1 | **3** | 90 | **8/112** | 🔴 **GÖLGE İÇİ SİYAH — SAHNE REDDEDİLİR** |
| S2 | **22** | 93 | 0/112 | ✅ |
| S3 | **16** | 72 | 1/112 | ⚠️ eşiğin hemen altında |
| S4 | **26** | 82 | 0/112 | ✅ |
| S5 | **45** | 116 | 0/112 | ✅ |

⭐ **Filmin vakum filmlerinden ayrıldığı TEK fiziksel nokta S1'de çöktü** ve
altı mercekten hiçbiri bunu söylemedi. ⑥ FİZİK tam tersine, 0:30'da
**var olmayan** bir "çakışan gölge yönü" için −4 puan yazdı.

### ② KAMERA SABİTLİK KAPISI — ⛔ YAZILDIĞI GİBİ KOŞULAMADI
`vidstabdetect` yerel ffmpeg 8.1 yapısında **YOK** (libvidstab derlenmemiş).
Yerine ikame: ardışık kare çifti (t+0,5 s ve t+9,3 s) satır/sütun luma
profilleri ±25 px çapraz korelasyonla eşlendi.

| sahne | dikey kayma | yatay kayma | hüküm |
|---|---|---|---|
| S0 | −14 px | −25 px (raya dayandı) | ⬜ ÖLÇÜLEMEDİ — üst bantta özne baskın |
| S1 | 0 px | 0 px | ✅ kilitli |
| S2 | 0 px | 0 px | ✅ kilitli |
| S3 | +1 px | −7 px | ⬜ ÖLÇÜLEMEDİ — kadrajı özne dolduruyor |
| S4 | 0 px | 0 px | ✅ kilitli |
| S5 | 0 px | −2 px | ✅ kilitli |

→ **D142 adayı:** SPEC'e kurulu olmayan bir filtreye kapı yazıldı. Yazılmış
ama koşulamayan kapı, koşulmamış kapıdır [D74].

### ③ KURGU KAPISI (tam teslim)
`süre = 6 × 10,033 = 60,20 ± 0,5` → ölçülen **60,033** ✅
`ekran metni: 0,0 s — başlık kartı dâhil` → ölçülen **≈ 7,0 s** 🔴 (aşağıda)

### ⛔ DÖRDÜNCÜ KAPI — HALKA KAPISI (insan gözü, S2 · 22,41 s)
**✅ GEÇTİ — VE FİLMİN 1 NUMARALI RİSKİ TUTTU.**
22,41 s karesinde halka, 9 metrelik üst açıdan **kapalı, kesiksiz, pas
renkli tam bir daire** olarak okunuyor; diğer soğuma eklemlerinden açıkça
ayrışıyor. Novum'un taşıyıcısı ekrandadır.

---

## 🔴 RAPORLARIN GÖRMEDİĞİ ALTI İHLAL — kareden ölçüldü

> Altısı da SPEC'in C BLOĞU'nda **"🔴 GERÇEK İHLAL"** başlığı altında
> yazılıdır. Altısı da tek kareden okunur. Altı mercekten hiçbiri yazmadı.

| # | ihlal | nerede | kilit | kanıt |
|---|---|---|---|---|
| **İ1** | 🔴 **EKRANDA YAZI — halkanın içinde "11 metres"** ve beyaz kertikli gradasyon yayı | S2 · ≈21,0–23,0 s | C bloğu "Ekranda herhangi bir yazı/rakam" · D bloğu "on-screen text = 0.0 s" | 22,41 karesi — okunabilir |
| **İ2** | 🔴 **SIRT ÜNİTESİ** — altın altıgen sırt çantası + omuz kayışları | S2 · 20,03–30,03 (10 s, 6/6 karede) | "completely FLAT back — no backpack…" [D79] | 20,20 · 21,50 · 24,00 · 26,50 · 28,00 · 29,80 |
| **İ3** | 🔴 **KLON** — ikinci kask + ikinci yüz, omuzdan doğuyor | S3 · **30,20–30,50** (≈0,30 s) | "İkinci insan, klon" · Kart 4 [D20/D69] | 10 fps şerit, 3./4./5. kare |
| **İ4** | 🔴 **ÇAKIL HAVADA** — ~0,3 m'lik küre havada süzülüyor, yön değiştiriyor, bir karede İKİYE çıkıyor, sonra yok oluyor | S4 · 43–45 s | "Çakılın havada uçması, zıplaması, yön değiştirmesi" · çakıl 62 mm | 1 fps şerit, 4.-6. kare |
| **İ5** | 🔴 **TWIST ÜRETİLMEDİ** — ovada üç çöküntü daha, ufka kadar: arka planda YOK | S5 · 56,53–58,03 olmalıydı | "TOHUM → KARŞILIK" üçüncü halka · doğal doruk | 56,50 · 58,00 · 59,50 kareleri |
| **İ6** | 🔴 **DÖNGÜ ÖLDÜ** — son kare S0'ın ilk karesiyle eşleşmiyor (farklı kamera yüksekliği, farklı arka plan) **ve** arkasına 4,997 s başlık kartı eklendi | 59,90 vs 00,10 · 60,03–65,03 | "S5'te son karenin S0'ın ilk karesiyle eşleşmemesi (döngü ölür)" | iki kare yan yana |

⭐ **İ1 ve İ6, rubriklerin OTOMATİK BLOCKER kutusudur.** ① KARE rubriği
"The automatic-BLOCKER boxes — on-screen text/subtitles … may NEVER be
written into FLAGS as a question" diye AÇIKÇA yasaklarken, ① KARE raporu
kartı tam olarak öyle yazdı:
`1:00 — title card text "THE THIN ROOF" — QUESTION: is this burned-in text intentional…`
Negatif kutusunu işaretlemedi, bulguya çevirmedi, `NEGATIVE BOX COUNT: 2`
diyerek kapattı. Kutunun kendisi 3 olmalıydı.

---

## 📓 ② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — raporun her bulgusu plana karşı

| # | rapor ne dedi (timecode) | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | ① ② "duplicate character / twin faces" 0:30-0:35 🔴 | C bloğu "İkinci insan, klon" | 30,03-30,83 · 10 fps şerit | 🔴 **FİLM SAPTI** — 30,20-30,50, ≈0,30 s |
| 2 | ① ⑤ ⑥ "floating spherical stones" 0:43 🟠 | C bloğu "Çakılın havada uçması" · "Havada asılı" | S4 · 1 fps şerit | 🔴 **FİLM SAPTI** — küre havada, yön değiştiriyor, ikileniyor |
| 3 | ① "Safe Zone: faces in the top 250px UI band" 0:30 🟠 | dikey güvenli alan (200-254 px) | S3 karesi ölçüldü: yüz merkezi ≈235 px | 🟠 **FİLM SAPTI** — reveal üst UI bandında |
| 4 | ② "backpack present S3, missing S5" 🟠 | "flat back 6/6" [D79] | S2 6 kare + S0/S1/S4/S5 kareleri | 🔴 **FİLM SAPTI — ama teşhis TERS**: çanta S2'de VAR olmamalıydı; yok olması değil, olması ihlal |
| 5 | ② ⑤ "solid floor S3 → massive hole S5" 🟠🟠 | C bloğu: pit S0/S5'te görünmez · halka KALDIRIMDA, pit KENARIN ÖTESİNDE | 22,41 vs 43,50 kareleri | ⚪ **RAPOR UYDURDU** — iki ayrı nesne (halka ≠ pit); C bloğu bu yanlış okumayı önceden yazmıştı → ⑩ DÜŞER |
| 6 | ② "pristine chest after lying on lava" 0:55 🟡 | C bloğu "KALKAN TOZ OLMAMASI → tasarım" | — | ⚪ **⑩ DÜŞER** — zemin rüzgârın temizlediği bazalt |
| 7 | ⑥ "conflicting shadow directions" 0:30 🟡 | C bloğu "gölge içi dolgu MEŞRUDUR" | gölge kapısı ölçümü: S3 en koyu blok 16 | ⚪ **⑩ DÜŞER** — tek kaynak + saçılma; çoklu kaynak yok |
| 8 | ⑥ "push-up too fast vs walking" 🟡 | 30 fps master, rapor 24 fps varsaydı | ⑪ ölçümü | ⚪ **ÖLÇÜM HATASI** — türetilen süre %25 yanlış → düşer |
| 9 | ① "AI bloom on visors" 0:30 🟡 | C bloğu "parlama, hale, bloom" = gerçek ihlal | S3 kareleri: vizör berrak, hale yok | ⬜ **AÇIK** — kareden hale okunmadı, leaning "uydurdu" |
| 10 | ① "texture swimming on canyon cliff" 0:15 🟡 | — | tek kare yetmez, hareket gerekir | ⬜ **AÇIK** |
| 11 | ① "motion jello / disjointed push-up" 0:52 🟠🟠 | C bloğu "Ağır çekim, hız rampası" | tek kare yetmez | ⬜ **AÇIK** |
| 12 | ① "dead center, not lower third" 0:20 🟡 | plan lower-third KİLİTLEMİYOR (kurulum C tepeden halka) | 22,41 karesi | ⬜ **AÇIK** — rubrik varsayılanı, film kilidi değil |
| 13 | ⑤ "smooth melted artifacts on S6 ground" 0:50 🟡 | — | tek kare yetmez | ⬜ **AÇIK** |
| 14 | ③ "AUDIO ABSENT — no audio information" | plan: kesintisiz ambiyans yatağı [D83] + Lithosphere.mp3 | ⑪ ölçümü: AAC 253 kbps, −17,3 LUFS | ⚪ **RAPOR UYDURDU → D137** |

**⬜ AÇIK madde sayısı: 5.** ⛔ Açık madde varken o merceğin skoru ŞARTLI,
bulgudan ders yazılmaz, yeniden üretim siparişi verilmez. Yukarıdaki beş
ders (D137-D141) **açık maddelerden değil**, ① ② ③ ④ 14 ve İ1-İ6'dan çıktı.

---

## 🔁 ⑤ ÇAPRAZ SAYIM KAPISI [D107 · D121 · D135]

| eksen | ① | ② | ③ | ④ | ⑤ | ⑥ | hüküm |
|---|---|---|---|---|---|---|---|
| sahne sayısı | 6 | 6 | — | 6 | 6 | 6 | fark 0 ✅ |
| kesme sayısı | 5 | 5 | — | 5 | 5 | 5 | fark 0 ✅ (gerçek 6) |
| süre | 64 s | 1:04 | — | 64 s | 1:04 | 1:04 | fark 0 ✅ (gerçek 65,030) |
| kart in-out | 1:00-1:04 | 1:00-1:04 | — | 1:00-1:04 | 1:00-1:04 | 1:00-1:04 | fark 0 ✅ (gerçek 60,03-65,03) |
| **replik** | none — **no audio information at all** | aynı | **STOP** | aynı | — | aynı | 🚨 **ALTISI DA AYNI ŞEKİLDE YANLIŞ** |
| **şerit** | `111111` | `111111` | — | `111111` | `111111` | `111111` | ✅ |

⛔ **Uyuşma bu partide doğrulama DEĞİLDİR.** Altı mercek aynı 1 saniyelik
süre hatasını, aynı eksik kesmeyi ve aynı ses yanılgısını üretti. D110'un
kopya testi ayrıca ② ⑤ ⑥'nın OUT-OF-SCOPE satırlarında birebir doğrulandı.
**Skorlar çöpe gider, kurgu aritmetiği gitmez [D121]** — §④ ve §⑨ ayakta.

---

## 🔍 ⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108]

| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| klon / ikiz yüz · 30,20-30,50 | ① 🔴 · ② 🔴 · ④ · ⑤ · ⑥ (dördü out-of-scope) | ② DEVAMLILIK (kat. 12) | ② · diğerleri →🔧 |
| küre havada · 43-45 s | ① 🟠 · ⑤ 🟠 · ⑥ 🟠 | ⑥ FİZİK (kat. 5) | ⑥ · ① ⑤ →🔧 |
| başlık kartı · 60,03-65,03 | ① (FLAGS) · ② (FLAGS) · ④ (NON-SCENE) · ⑤ (NON-SCENE) · ⑥ (NON-SCENE) | ① KARE (negatif kutu) | **hiçbiri taşımadı** 🚨 |
| sırt çantası · S2 | ② 🟠 (ters teşhis) | ② DEVAMLILIK (kat. 4) | ② |
| halka içindeki yazı · 21-23 s | **hiçbiri** | ① KARE + ⑤ ARKA PLAN (kat. 9) | **hiçbiri** 🚨 |

---

## 🧮 ⑩ ÖNERME KAPISI — puan geri verilir, toplam yeniden hesaplanır [D87·D116·D130·D131·D134]

| mercek | raporun toplamı | ⑩ sonrası | ayakta, sayı taşıyan hücre | T tablosuna |
|---|---|---|---|---|
| ① KARE | 7,2/10 | — | Character 3 · Safe Zone 7 · Particles 5 ayakta; Lighting/Environment/Vertical kaynaksız kaldı | ⛔ **SATIR YOK** [D129] |
| ② DEVAMLILIK | 8,1/10 | — | Equipment 6 · Quantity 1 ayakta; Geography ve Wear ⑩'da düştü → kaynaksız | ⛔ **SATIR YOK** |
| ③ SES | — | — | 0 | ⛔ **SATIR YOK** |
| ④ HİKAYE | 3,5/10 | — | on kategorinin dokuzu belgesiz okuma; ⑨'daki yuva kayması yüzünden sahne haritası yanlış | ⛔ **SATIR YOK** |
| ⑤ ARKA PLAN | 7,3/10 | — | Horizon ve Props ⑩'da düştü → **ayakta hücre 0** | ⛔ **SATIR YOK** |
| ⑥ FİZİK | 6,3/10 | — | Particles 5 ayakta; Light&Shadow ⑩'da, Rates ölçüm hatasında düştü | ⛔ **SATIR YOK** |

⛔ **⑩ sonrası sayı hesaplanmadı ve hesaplanmayacak:** ortak adım ① gereği bu
partinin hiçbir satırı tabloya girmiyor. ⑩ tablosu burada, düşen bulguların
KAYDI olarak duruyor — bir sonraki (mod D) koşuda başlangıç noktasıdır.

---

## ⭐ ④ HİKAYE MERCEĞİ — tek doğru teşhis, yanlış sebeple

**④ tek başına filmin gerçek yarasını buldu:** `ENDS OR STOPS: **Stops**` ·
`Ending 3/10` · "the character pushes up, completely ignoring the climax".
Bu okuma **doğrudur ve İ5 + İ6 ile ölçümle doğrulanmıştır** — twist üretilmedi,
döngü öldü.

Ama ④ sebebi bilmiyordu ve reçetesi filmi öldürürdü:
- kesme listesi **S2'yi (asimetri anı) ve S4'ü** kesiyor — ikisi de SPEC'te
  **"KESİLEMEZ SAHNELER"** yazıyor
- 30 s kesince süre 34 s'ye düşüyor — kendi raporu "BELOW FORMAT FLOOR" diyor
- "S1'i çakılın düşüşünün ekstrem yakın çekimiyle değiştir" reçetesi, filmin
  kanca tipini (yanlışlık kompozisyonu) ve tohum-karşılık zincirini siliyor

⛔ **Kesme listesi UYGULANMAZ** [D129 · ⑩].

---

## 🎬 SAHNE SAHNE — plan vs ekran (ölçülmüş)

| sahne | tasarlanan vuruş | ekranda | hüküm |
|---|---|---|---|
| S0 | yürüyüş · gölgenin ucu kesilir (04,20) · tohum (06,20-06,90) · diz çöküş / kapak anı (07,40) | yürüyüş ✅ · gölge ✅ · diz çöküş ≈09,9 (2,5 s geç) | ⚠️ kapak anı kaydı |
| S1 | göz hizası · avuç basınç testi (14,81-16,61) | diz çökme + kenar, **çıkıntı burada ZATEN açılıyor** | ⚠️ S3'ün şoku S1'de harcandı |
| S2 | **halka kapanır (22,41)** — asimetri anı | ✅ halka kapalı daire · 🔴 İ1 yazı · 🔴 İ2 sırt çantası | 🔴 |
| S3 | çıkıntı (32,02) · EL YUVASI ≥%28 (34,02-35,82) | ✅ çıkıntı muhteşem · ✅ el yuvası (avuç kadrajda büyük) · ✅ ten dokusu/gözenek | 🔴 İ3 klon |
| S4 | çakıl sallanır (38,42) · yuvarlanır 0,40 m (43,22-46,82) · merkezî seçim (48,10) | yüzükoyun uzanma erken (≈43) · çakıl **yuvarlanmadı** | 🔴 İ4 |
| S5 | ayağa kalkış (55,63) ✅ · **TWIST (56,53-58,03)** · döngü (58,53-60,03) | ayağa kalkış ✅ · twist YOK · döngü YOK | 🔴 İ5 İ6 |

**Tutan tasarım kararları (korunacak):** halka kapısı · gölge dolgusu (5/6) ·
ten gözeneği + ter + kir (plastik ten YOK) · kamera kilidi (4/6 ölçüldü, 6/6
gözle) · sıfır kare havada toz · vizör berrak/tintsiz 6/6 · tek karakter 5/6.

---

## 📊 SKOR SATIRLARI

```
T1 KARE          ⛔ SATIR YAZILMADI [D129]
T2 DEVAMLILIK    ⛔ SATIR YAZILMADI [D129]
T3 SES           ⛔ SATIR YAZILMADI — koşu stop bloğuyla bitti VE ölçüm çürüttü
T4 HİKAYE        ⛔ SATIR YAZILMADI [D129]
T5 ARKA PLAN     ⛔ SATIR YAZILMADI [D129] — ayrıca ⑩ sonrası ayakta hücre 0
T6 FİZİK         ⛔ SATIR YAZILMADI [D129] — ayrıca 24 fps varsayımı
00_INDEX tamlık  ⑥ hücrenin altısı da ❌ KALDI (0/4)
```

---

## ✅ BİR SONRAKİ KOŞU İÇİN — sırayla

```
1. 🔴 S2 ve S3 YENİDEN ÜRETİLİR
     S2: halka aynı kalsın, ama prompt gövdesinden ÖLÇÜ CÜMLELERİ çıkarılır
         (D138) + "no engraved, painted or inscribed characters on any
         surface" negatif satırı + sırt paneli POZİTİF tarif edilir (D139)
     S3: klibin ilk 0,5 saniyesi klon üretti; yeniden üretilir ve
         ilk 0,6 s 10 fps şeritle taranır (D140)
2. 🔴 S4 YENİDEN ÜRETİLİR — çakıl 62 mm, YUVARLANIR, havalanmaz
3. 🔴 S5 YENİDEN ÜRETİLİR — TWIST ekranda olmalı; SPEC'e FİNAL VURUŞ KANITI
     satırı yazılır (D141) ve tek kareyle kontrol edilir
4. 🔴 BAŞLIK KARTI KURGUDAN ÇIKARILIR — 60,03 son karedir, döngü orada kurulur
5. 🔴 S1 gölge dolgusu kapısından geçmedi (en koyu blok 3/255) — yeniden üretilir
     ya da kurguda gamma ile derin çukur açılır ve kapı yeniden koşulur
6. ⚠️ MASTER 1440×2560'a yeniden ihraç edilir (720p ihraç eşiğinin altında),
     −14 LUFS / −1,0 dBTP'ye normalize edilir
7. ⭐ SONRA: altı mercek MOD D ile, HER BİRİ TEMİZ OTURUMDA koşulur —
     operatöre rubrik + THE_THIN_ROOF_QA_SPEC.md birlikte verilir [D129]
```

---

## 📚 BU KAYITTAN ÇIKAN DERSLER

| ders | başlık | dosya |
|---|---|---|
| **D137** 🔴 | ses kanalı VAR, altı merceğin altısı "hiç ses bilgisi yok" dedi | `DERSLER/08_QA_SURECI.md` |
| **D138** 🔴 | metin yasağı kostüme yazıldı, ölçü zemine — model ölçüyü zemine bastı | `DERSLER/06_METIN_VE_PROMPT_DILI.md` |
| **D139** 🔴 | düz sırt kilidi yalnız sırt görünmezken tutuyor | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` |
| **D140** 🔴 | klon klibin ilk 0,5 saniyesinde doğup kayboluyor | `DERSLER/02_KARAKTER_VE_CANLI.md` |
| **D141** 🔴 | klip var, vuruş yok — kurgu kapısının üç satırı da geçti | `DERSLER/07_KURGU_VE_ANLATI.md` |
| **D142** 🟡 | SPEC'in makine kapısı kurulu olmayan filtreye yazıldı (vidstabdetect) | `DERSLER/09_SISTEM_VE_SUREC.md` |
