# 🌹 THE ROSE COAT — FİLM KAYDI

> **Koşu tarihi:** 26.08.2026 · **beş mercek** (① ② ③ ④ ⑤)
> **Plan:** [`../../../yatay_2_dk_filmler/THE_ROSE_COAT/THE_ROSE_COAT_DUST_PLAIN_FILM.md`](../../../yatay_2_dk_filmler/THE_ROSE_COAT/THE_ROSE_COAT_DUST_PLAIN_FILM.md)
> **SPEC:** [`../../../yatay_2_dk_filmler/THE_ROSE_COAT/THE_ROSE_COAT_QA_SPEC.md`](../../../yatay_2_dk_filmler/THE_ROSE_COAT/THE_ROSE_COAT_QA_SPEC.md)
> **Format:** 2-4 dk · yatay · 13 sahne × 10 s = 130 s · 0 kesme · 0 replik
>
> ## 🚨 BU KOŞUNUN TEK CÜMLELİK ÖZETİ
>
> **SPEC dosyası filmin kendi klasöründe, planın yanında duruyordu ve beş
> merceğin beşi de mod V koşuldu.** Bedeli bu kayıtta sayıyla yazılı: ④'ün
> kesme listesi filmin DORUĞUNU, KAPAK KARESİNİ ve iki VİRALİNİ kesiyor;
> ①'in üç 🔴 BLOCKER'ı filmin NOVUM'unu tarif ediyor; ②'nin 7,2'si ve ⑤'in
> 6,0'ı iki kapıdan geçtikten sonra **arkasında tek bir kapalı hücre
> bırakmıyor.**

---

## 📦 MALZEME VE HAM DOSYALAR

| Mercek | Ham rapor | Mod | Rapor toplamı | Durum |
|---|---|:--:|:--:|---|
| 🔧 ① KARE | [`KARE_HAM`](../02_HAM_RAPORLAR/THE_ROSE_COAT/THE_ROSE_COAT_KARE_HAM.md) | V | 5,0 | Ⓥ ⛔ ÖN KOŞU · ⚠️ ŞARTLI |
| 🔗 ② DEVAMLILIK | [`DEVAMLILIK_HAM`](../02_HAM_RAPORLAR/THE_ROSE_COAT/THE_ROSE_COAT_DEVAMLILIK_HAM.md) | belgesiz (tasarım) | 7,2 | ⚠️ ŞARTLI |
| 🔊 ③ SES | [`SES_HAM`](../02_HAM_RAPORLAR/THE_ROSE_COAT/THE_ROSE_COAT_SES_HAM.md) | belgesiz (tasarım) | — | `AUDIO ABSENT — RUN NOT STARTED` |
| 📖 ④ HİKAYE | [`HIKAYE_HAM`](../02_HAM_RAPORLAR/THE_ROSE_COAT/THE_ROSE_COAT_HIKAYE_HAM.md) | V | 2,3 | Ⓥ ⛔ ÖN KOŞU · ⚠️ ŞARTLI |
| 🖼️ ⑤ ARKA PLAN | [`ARKA_PLAN_HAM`](../02_HAM_RAPORLAR/THE_ROSE_COAT/THE_ROSE_COAT_ARKA_PLAN_HAM.md) | belgesiz (tasarım) | 6,0 | ⚠️ ŞARTLI · matrise girmez |

---

## ⭐ ÖLÇÜM KAPISI ⑪ [D125] — ⛔ KOŞULMADI

```
⛔ AÇIK. Master dosya ölçülmedi; aşağıdaki her sayı RAPORLARIN sayısıdır.
   Kapatmak için (~30 sn):

   M="<master.mp4>"
   ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate "$M"
   ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
   ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
   ⭐ EK — bu filmde ZORUNLU (③ AUDIO ABSENT bildirdi):
   ffprobe -v error -select_streams a -show_entries stream=codec_type "$M"
   → çıktı BOŞSA dosyada ses kanalı YOKTUR ve bu bir TESLİM KUSURUDUR
     (plan 13 sahnenin 11'inde müzik yazıyor — §0.15 MUSIC-FREE SCENES: 2)
```

---

## ⛔ ORTAK ADIM KAPILARI — sonuç

| # | Kapı | Sonuç |
|:--:|---|---|
| ⑪ | ÖLÇÜM [D125] | ⛔ **KOŞULMADI** — master ölçülmedi, aşağısı raporun sayısıdır |
| ③ | KİMLİK [D105] | ✅ **GEÇTİ** — iki metin-dışı çapa (aşağıda) |
| ① | SPEC [D94/D117] | ❌ **DÜŞTÜ** — SPEC dosyası VARDI, verilmedi → tüm koşular ÖN KOŞU |
| ④ | KURGU [D109/118/120/121] | ⚠️ **KISMİ** — sayı ✅ · süre ✅ (kart hariç) · şerit ⛔ okunamadı |
| ⑤ | ÇAPRAZ SAYIM [D107/121] | ✅ **GEÇTİ** — 13/13/13/13 sahne · 13/13/13 kesme · replik yok/yok/yok |
| ⑦ | PARMAK İZİ [D112] | ⬜ açık — önceki iki koşunun künyesi karşılaştırılmadı |
| ⑨ | HİZALAMA [D115] | ✅ **GEÇTİ** — ızgara `n × 10 s`, raporların blokları birebir oturuyor |
| ⑩ | ÖNERME [D87/D116] | ❌ **AĞIR** — aşağıda 11 bulgu düştü |
| ⑥ | ÇAPRAZ GÖZLEM [D108] | ❌ iki gözlem iki tabloya faturalandı (aşağıda) |
| ⑧ | FRAGMAN [D111] | ✅ film, fragman değil |

### ③ KİMLİK KAPISI — çapalar

```
⛔ Beş raporun beşi de FILM: (not supplied) yazdı. Atıf operatörde koşuldu.
⛔ 1:18'deki "rose" yazısı ÇAPA DEĞİLDİR [D105] — ekrandaki yazı kimlik
   kanıtı olarak geçersizdir ve zaten filmin en ağır ihlal adayıdır.

ÇAPA 1 · VURUŞ    plan S2 "ÖNCE KARESİ — gömülü mekik, üs avlusu"
                  ↔ ② ve ④ sahne 3 (0:20-0:29) "Buried shuttle"
ÇAPA 2 · SAYISAL  plan §0.9 "13 sahne × 10 s = 130 s · 0 kesme ·
                  insansız 1 sahne: S0 (hook)"
                  ↔ dört raporun dördü: 13 sahne · 10 s ızgara ·
                  presence string ilk yuvası insansız
EŞLEŞME: 2/2 → koşu ATIFLI. Skor satırı yazılabilir (ŞARTLI).
```

### ④ KURGU KAPISI

```
a) klip sayısı  plan 13  ↔ rapor 13                              ✅
b) süre         plan 130 s ↔ rapor 135 s − 5 s kart = 130 s      ✅
                ⛔ kartın kendisi bir İHLALDİR (aşağıda, kilit 1)
c) İNSAN ŞERİDİ ⛔ KAPI KOŞULAMADI
   plan yazıyor : -222222222222   (gövde sayısı: 2 = iki insan)
   rapor yazıyor: -111111111111   (rubriğin çıktı şartnamesi: 1 = insan VAR)
   Bu iki dize hiçbir zaman eşit olamaz — rubrik "2" üretemez.
   Kapı, ÖLÇME ALETİNİN ÜRETEMEYECEĞİ bir notasyonda yazılmış. [→ D135]
   ⭐ Kilidin ÖZÜ yine de tutuyor: ②'nin appearance table'ı 12 sahnenin
     12'sinde tam iki gövde sayıyor, üçüncü figür 0. Ama bunu okuyan
     hiçbir kapı yok.
   ⭐ ⑤ ARKA PLAN şeridi `1111111111111` yazdı — ilk yuvada insan
     GÖSTERİYOR, oysa kendi envanterinde S1'in öznesi "sand pouring from
     wall slit" ve figür yok. Dört şerit hiçbir yerde yan yana konmuyor.
```

---

## 🔒 KİLİT ÇELİŞKİSİ DEFTERİ [D96]

> `çözüm eylemi` = master'ın O SANİYESİNİ izlemek (~10 sn iş)
> ⛔ ⬜ AÇIK madde varken o merceğin skoru ŞARTLI'dır ve **bulgudan ders
> yazılmaz, yeniden üretim siparişi verilmez.**

| # | Rapor ne dedi | Hangi kilit | Çözüm eylemi | Sonuç |
|:--:|---|---|---|---|
| 1 | 4/4 mercek: `NON-SCENE MATERIAL: 2:10-2:15 title card` | B BLOĞU `SCREEN TEXT: 0.0 saniye — başlık kartı YOK` | gerekmez: dört bağımsız mercek aynı in-out'u verdi | 🔴 **FİLM SAPTI** — kart kurguya eklenmiş (D70/72/120 zincirinin 5. vakası) |
| 2 | ①·②·④·⑤ 2:00-2:09: "A climbs the ladder" · ① 2:02 eller basamaktan geçiyor | C BLOĞU `BİNİŞ 0 kare · film merdivenin dibinde biter` + plan S12 `FİNAL — iki sırt, iki renk` | **master 2:00-2:10** | ⬜ **AÇIK — EN YÜKSEK ÖNCELİK.** Dört mercek merdiven tırmanışında hemfikir. Doğruysa filmin PLANLI FİNALİ üretilmemiş, yerine yasak bir vuruş geçmiş [D62/D72 kuyruk kuralı] |
| 3 | ② her sahnede sırt çantası (var/yok/renk değişiyor) · ① 0:45 fırça çantadan geçiyor | C BLOĞU `SIRT PANELİ: düz, gömme, dikdörtgen · çanta 0 · silüet 13/13 DÜMDÜZ` | **master 0:40-0:50 + 1:30** | ⬜ **AÇIK.** ②'nin Kostüm(1) · Yıpranma(3) · Ekipman(2) hücrelerinin ÜÇÜ de bu okumaya asılı |
| 4 | ② `0:10 bot siyah ↔ 0:40 bot beyaz` 🔴 | C BLOĞU `KADRO KİLİDİ: UZUN = koyu antrasit eldiven+bot · KISA = beyaz` | **master 0:10 + 0:40 + 0:50** | ⬜ **AÇIK.** Doğruysa bu "kostüm sürüklenmesi" değil: filmin ÜÇ ayrım kanalından biri çökmüş demektir [→ D134] |
| 5 | ① STEP 1: "static lockoffs **or very slow, steady push-ins**" | B BLOĞU `13/13 sabit lockoff · 0 pan · 0 tilt · 0 zoom · 0 track` | **master, herhangi 3 sahne** | ⬜ **AÇIK.** ① kendi taban envanterinde push-in bildirip Kamera'ya 10/10 · "no in-scope source" yazdı |
| 6 | ① 0:22 + ⑤ 0:20: gömülü mekiğin gölgesi SOLA, figürlerinki aşağı/öne | C BLOĞU `yıldız 13/13 EKRAN-SOL · gölgeler 13/13 EKRAN-SAĞ` | **master 0:20-0:30** | ⬜ **AÇIK.** İki mercek aynı kareyi bağımsız işaretledi; raporun iki yönü de kilide aykırı |
| 7 | ① 0:55 "sand falling off the hull behaves as a unified 2D fluid waterfall" | C BLOĞU `Kaldırılan toz DÜZ AŞAĞI, 0,25 m/s · asılı kalmaz · girdap yapmaz · **sıvı gibi akmaz**` | **master 0:50-1:00** | ⬜ **AÇIK.** Düz inen perde TASARIM; sıvı gibi akan kütle YASAK. İkisi bitişik okumalar ve ayrımı yalnız sayısal kilit yapıyor |
| 8 | ② `Counter Logic: N/A — no counter present` | C BLOĞU `SIRT SAYACI — filmin ANA sayacı, beş görsel durum` + `pada mesafe 600→0 m` + `fırça kılları` (üç sayaç) | **master S1/S4/S7/S11 sırt renkleri** | ⬜ **AÇIK.** Ya film paleti üretmedi ya belgesiz mercek doygunluğu sayaç olarak okuyamadı. İkisi de ağır |
| 9 | ① 1:18 sırt çantasında "rose" yazısı 🔴 | C BLOĞU `METİN 0 kare — gövde yazısı, logo, marka, numara, sembol hiçbir yüzeyde yok` | **master 1:15-1:20** | ⬜ **AÇIK.** Tek mercek bildirdi |
| 10 | ③ `AUDIO ABSENT — RUN NOT STARTED` (dosyada ses bilgisi yok) | plan §0.15 `MUSIC-FREE SCENES: 2` → 11 sahnede müzik VAR · S11 7,0 s'de iki eldiven tıklaması | `ffprobe -select_streams a` | 🔴 **TESLİM KUSURU (yüksek olasılık).** Plan sesi yazıyor, dosyada ses kanalı yok [→ D136 dosyası: bunu partide yalnız ③ gördü ve ③ hiçbir tabloya satır bırakmıyor] |

---

## 🧬 ÖNERME KAPISI ⑩ [D87/D116] — DÜŞEN BULGULAR

> **Kural:** kaynağı planda YAZILI olan bulgu DÜŞER; film kaydına "önerme"
> yazılır. ⛔ Bulguyu getiren merceğin adı bu kararı değiştirmez.

| Bulgu (mercek · timecode) | Planda YAZILI kaynak | Karar |
|---|---|:--:|
| ① 0:03 🔴 "sand pours from a flat slit with no volume, 2D fluid generator" | plan §0.3 KANCA: silecek çubuğu bir darbe atar, panel BEMBEYAZ çıkar, kaldırılan toz **düz bir perde hâlinde 0,25 m/s** iner | **DÜŞER** — filmin NOVUM'u |
| ① 1:33 🔴 "texture swimming: surface morphs pink→white while brushing" | C BLOĞU FIRÇA VERİMİ: bir darbe 0,25-0,60 mm kaldırır; panel DURUM 3 → DURUM 0'a iner | **DÜŞER** — filmin ANA MEKANİĞİ |
| ① 0:12 / 0:32 "moonwalk · glide · jello" | C BLOĞU `YERÇEKİMİ 0,40 g` + `KOŞU/ZIPLAMA 0 kare · adım uzun, iniş yavaş` | **KISMİ** — "düşük-g yürüyüş" düşer; "ayak zemine kilitlenmiyor" ⬜ açık |
| ① "Gravity read: ~1g" (taban envanteri) | `0,40 g — gövde 1,0 m'yi 0,71 s'de düşer` | **DÜŞER** (taban yanlış kurulmuş) |
| ② Coğrafya −3 `0:50 panel alçak ↔ 1:30 panel devasa` | plan §0.9 pada mesafe: S5 **120 m** ↔ S9 **0 m** (monotonik 600→0) | **DÜŞER** — mesafe sayacı |
| ② Çapraz Kesme −3 "düşüyor, sonra rahatça ayakta" | C BLOĞU TEMAS: `S7'de düşen figüre YARDIM EDİLMEMESİ TASARIMDIR (temas bütçesi)` | **DÜŞER** |
| ⑤ Ufuk −5 `0:30 düz sert zemin ↔ 1:00 yuvarlanan kumullar` | S3 = ova kenarı **500 m** ↔ S6 = pad **30 m** — iki ayrı yer | **DÜŞER** |
| ⑤ Derinlik −3 `0:50 ↔ 1:00 roket bacak ölçeği değişiyor` | S5 **120 m** ↔ S6 **30 m** | **DÜŞER** |
| ⑤ Arka Set −6'nın ilk yarısı `0:50 ↔ 1:30 panel yüksekliği` | aynı mesafe sayacı | **DÜŞER** |
| ⑤ Gökyüzü −4 `0:20 gölge/gökyüzü uyuşmazlığı` | ① 0:22 ile AYNI GÖZLEM — sahibi ① [D108] | **DÜŞER** (⑤'ten) |
| ④ Final 1/10 "stops rather than ends · no payoff" | C BLOĞU `BİNİŞ 0 kare · GENİŞLEME finali · "final kesik" bulgusu DÜŞER` | ⬜ **ASILI** — kilit 2 kapanmadan karar verilemez: planlı S12 ekrandaysa DÜŞER, merdiven tırmanışı yerine geçtiyse AYAKTA |

### ⛔ ⑩'IN AÇIK BIRAKTIĞI DELİK — bu koşunun en pahalı bulgusu

```
Kapı "bulgu DÜŞER" diyor. PUANI kim geri veriyor? Hiç kimse.
Iron Slope satırı bunu yazıyla itiraf ediyor:
   "Toplam, rubriğin kendi aritmetiğidir."
Yani ⑩ tabloyu HİÇ değiştirmiyor; yalnız hücreyi parantez içine alıyor.

Bu filmde bedeli:
   ② DEVAMLILIK  7,2 → düşenler ve ⬜'ler ayıklandığında AYAKTA HÜCRE: 0
   ⑤ ARKA PLAN   6,0 → aynı işlem sonrası AYAKTA HÜCRE: 0
   ① KARE        5,0 → üç 🔴'ün ikisi düştü, biri (0:55) ⬜
```

---

## 🔁 ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108]

| Gözlem (timecode) | Hangi raporlarda | Sahibi | Puanı kim taşıyor |
|---|---|---|---|
| Gölge yönü ↔ ışık kaynağı uyuşmuyor (0:20-0:22) | ① Işık −3 · ⑤ Gökyüzü −4 | **① KARE** (ışık fiziği) | ① · ⑤ → 🔧 işaretçi, hücre düşürülmez |
| Roket paneli/tabanı iki sahnede farklı (0:50 ↔ 1:30) | ② Coğrafya −3 · ⑤ Arka Set −6 | **② DEVAMLILIK** (eylem panele DOKUNUYOR — fırçalıyorlar) | ikisi de ⑩'dan düştü; hücrelerin ikisi de tam puana döner |

### 🚨 ÜÇÜNCÜ SATIR — D108'in tanımadığı çakışma türü

```
0:00-0:05 · AYNI BEŞ SANİYE, İKİ MERCEKTE ZIT HÜKÜM

   ① KARE   → TOP 3 CRITICAL ERRORS #1 · 🔴 BLOCKER · "REGENERATE"
   ④ HİKAYE → "THE THREE THINGS WORTH PROTECTING" #1
              + SHAREABLE MOMENT (filmin tek paylaşılabilir anı)
              + SCENE-BY-SCENE VERDICT: KEEP

D108'in tablosu "aynı gözlem iki kez faturalandı mı" diye sorar.
Burada fatura değil HÜKÜM çakışıyor ve tablo bunu göremiyor: bir mercek
"yeniden üret", öteki "filmin korunacak tek anı" diyor. Operatör ①'i
uygularsa filmin kancasını siler.
⭐ Ve ikisi de yanlış: o beş saniye filmin planlı NOVUM'udur (⑩ düşürdü).
```

---

## 📖 ④ HİKAYE — KESME LİSTESİ ⛔ UYGULANMAZ

> Ön koşu olduğu için zaten uygulanmaz [D94]. Ama neyi kestiği kayda
> geçmelidir, çünkü bu SPEC'siz koşmanın fiyat etiketidir.

Rapor numaralandırması filmin numaralandırmasından **bir kayıktır**
(rapor S1 = plan S0):

| Sıra | Rapor kesiyor | = plan sahnesi | O sahne aslında ne |
|:--:|---|---|---|
| 1 | S4 (0:30-0:39) | **S3** | ⭐ **VİRAL 1** ⛔ `KESİLEMEZ` · ölçek şoku · ÇEHOV 3 (uzak) kurulumu |
| 2 | S6 (0:50-0:59) | **S5** | **ÇEHOV 4 KURULUMU** — birikinti sağlam çıkar; ödemesi raporun "en iyi ikinci anı" dediği düşüş |
| 3 | S10 (1:30-1:39) | **S9** | ⭐ **ARİTMETİK** — üç yüzey, bir fırça · **SEÇİMİN KURULUMU** · ÇEHOV 5 ödemesi |
| 4 | S12 (1:50-1:59) | **S11** | 🎯 **DORUK** + ⭐ **VİRAL 3** ⛔ `KESİLEMEZ` + **KAPAK KARESİ** (6,0 s) |
| 5 | S3 (0:20-0:29) | **S2** | **ÖNCE KARESİ** · ÇEHOV 5 kurulumu (ödemesi S9'un dördüncü bakışı) |

```
⛔ Beş kesme adayının BEŞİ de yük taşıyan sahne; ikisi SPEC'te açıkça
   "KESİLEMEZ" yazan viral.
⛔ Rapor filmin doruğunu "One last redundant brush before climbing.
   Unnecessary." diye tarif etti ve `PEAK LOCATED AT: no peak located`
   yazdı. Doruk planda 110-120 s olarak SANİYESİ SANİYESİNE yazılı.
⛔ Raporun "korunacak üç şey" listesinde üç viralden HİÇBİRİ ve doruk YOK.
⛔ Raporun okuduğu önerme ("neden sürekli temizlik yapıyorlar?") filmin
   önermesi DEĞİL: filmin novum'u KİMSE KENDİ SIRTINA ULAŞAMAZ. Rapor
   135 saniye boyunca fırçanın her zaman ÖTEKİNİN sırtında olduğunu bir
   kez bile yazmadı.
```

---

## 📊 SKOR SATIRLARI — hepsi ⚠️ ŞARTLI

| Mercek | Raporun toplamı | D131 düzeltmesi (kaynaksız hücre ortalamaya girmez) | ⑩ + ⬜ sonrası ayakta hücre |
|---|:--:|:--:|:--:|
| ① KARE | 5,0 | 25/6 = **4,2** | 0 kapalı 🔴, 1 ⬜ (0:55) |
| ② DEVAMLILIK | 7,2 | 26/6 = **4,3** | **0** |
| ⑤ ARKA PLAN | 6,0 | Kenarlar 7→10 [D119 ihlali] → 6,5; kaynaksız çıkınca 29/5 = **5,8** | **0** |
| ④ HİKAYE | 2,3 | — (kaynaksız hücre yok) | kesme listesi geçersiz |

```
⭐ ②'nin 12 puanlı hücresinden 6'sı "no in-scope source · 10/10".
   Altı tam puan, çöken bir filmi 4,3'ten 7,2'ye taşıdı: Δ = 2,9 puan.
   Raporun kendi hükmü "STRUCTURAL PROBLEM" — ama tabloya giren sayı 7,2.
   Sözü ve sayısı zıt yöne bakan bir satır tabloya girdi. [→ D131]
```

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

| # | Ders | Dosya |
|:--:|---|---|
| 129 | SPEC dosyası klasörde dururken mod V koşuldu — kesme listesi doruğu, kapağı ve iki virali kesti | `DERSLER/08_QA_SURECI.md` |
| 130 | ⑩ önerme kapısı bulguyu düşürüyor, PUANI geri vermiyor | `DERSLER/08_QA_SURECI.md` |
| 131 | "no in-scope source" = 10/10 → kaynaksızlık ödüllendiriliyor | `DERSLER/08_QA_SURECI.md` |
| 132 | SEVERITY TALLY yalnız bir rubrikte sayılıyor — aynı partide A/B kanıtı | `DERSLER/08_QA_SURECI.md` |
| 133 | Monotonik mesafe sayacı olan filmde belgesiz mercek, tasarlanmış yaklaşmayı "geometri sürüklenmesi" yazar | `DERSLER/08_QA_SURECI.md` |
| 134 | Belgesiz merceğin bulgu sıralaması SONUÇ sıralaması değildir — bot rengi üç kimlik kanalından biriydi | `DERSLER/08_QA_SURECI.md` |
| 135 | İnsan şeridi kilidi, ölçme aletinin üretemeyeceği notasyonda yazılı | `DERSLER/09_SISTEM_VE_SUREC.md` |
| 136 | Plan 11 sahnede müzik yazıyor, dosyada ses kanalı yok — ve bunu gören tek mercek hiçbir tabloya satır bırakmıyor | `DERSLER/08_QA_SURECI.md` |

---

## 🧾 KARAR — operatörün önüne konan iş (sipariş değil)

```
⛔ HİÇBİR YENİDEN ÜRETİM SİPARİŞİ VERİLMEDİ. On kilit maddesinin
   sekizi ⬜ AÇIK; ⬜ açıkken sipariş verilmez [ortak adım ②].

SIRAYLA YAPILACAK — toplam ~4 dakika master izleme:

1. ffprobe ses kanalı        → kilit 10 · TESLİM KUSURU mu?      (10 sn)
2. master 2:00-2:10          → kilit 2  · PLANLI FİNAL ekranda mı? (10 sn)
   ⛔ EN PAHALI SORU. Yoksa film finalini kaybetmiş demektir.
3. master 0:40-0:50 + 1:30   → kilit 3  · sırt çantası mı, gömme panel mi?
4. master 0:10 / 0:40 / 0:50 → kilit 4  · bot-eldiven ayrım kanalı
5. master 0:20-0:30          → kilit 6  · gölge yönü
6. master 0:50-1:00          → kilit 7  · toz perde mi, sıvı mı
7. master S1/S4/S7/S11       → kilit 8  · sırt sayacı paleti ekranda mı
8. master 1:15-1:20          → kilit 9  · "rose" yazısı
9. kart 2:10-2:15            → kilit 1  · ZATEN KAPALI 🔴 — kart kaldırılır

SONRA: SPEC dosyasıyla ① ve ④ MOD D olarak YENİDEN koşulur.
Bu koşunun skorları o zaman ARŞİVLENİR, güncellenmez — mod V ve mod D
aynı ölçüm değildir.
```
