# 🕳️ THE SKYLIGHT — FİLM KAYDI

> **Durum:** film üretildi ve kurgulandı · teslim dosyaları `~/Downloads/the skylight.mp4`
> (1920×1080) ve `~/Downloads/the skylight (1).mp4` (3840×2160) — aynı kurgu, iki ihraç
> **Ölçüm:** 29.08.2026 · **altı mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE ·
> 🖼️ ARKA PLAN · ⚖️ FİZİK) — **altısı da mod V.** Raporlar Gemini; ①②③④ `the skylight.mp4`,
> ⑤⑥ `the skylight_2.mp4` üzerine koşuldu (ölçümde iki dosyanın süresi ve ses izi birebir).
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T6'YA GİRMEDİ.** Film klasöründe `THE_SKYLIGHT_QA_SPEC.md`
> **VARDIR** ve altı raporun altısı `INPUT MODE: V` yazıyor → ortak adım ① gereği koşu
> TEKRARLANIR; ham raporlar 02/'ye düştü, T tablosuna satır yazılmadı, kesme listesi ve
> REMOVE reçetesi UYGULANMADI [D129]. **SPEC yazılmış olduğu hâlde mod V koşulan film
> sayısı 8.**
>
> ⭐ **BU KOŞUNUN GERÇEK ÇIKTISI SKOR DEĞİL, ÖLÇÜM VE KARELERDİR.** Master ffprobe/ffmpeg
> ile ölçüldü; 18 tartışmalı saniyenin karesi iki kontakt sayfası + köşe şeridi olarak
> çıkarılıp gözle bakıldı. Sonuç: raporların 21 etiketli bulgusundan **9'u kareyle
> doğrulandı**, 6'sı ⑩'da tasarım çıktı, 6'sı ⬜ açık — ve **raporların hiç görmediği 9
> ihlal** ölçüldü (filigran · toz şelalesi · kapak kartı · kırpılmamış hook · 2 eksik sahne
> · −17 LUFS/0 dBTP · 2 dijital delik · beyaz "ışık gölü" · cıvata halüsinasyonu).
> Sekiz yeni ders buradan çıktı: **D143-D150**.

---

## 📦 MALZEME VE HAM DOSYALAR

```
MALZEME:  teslim kurgusu · 315,155 s · 30 fps · AAC 253 kbit/s 48 kHz stereo
          1080p ve 4K ihraç (süre, ses izi, sessizlik aralıkları birebir aynı)
MERCEK:   🔧 1_KARE · 🔗 2_DEVAMLILIK · 🔊 3_SES · 📖 4_HIKAYE
          · 🖼️ 5_ARKA_PLAN · ⚖️ 6_FIZIK   (altısı da mod V)
OTURUM:   🚨 ŞÜPHELİ [D110] — ⑤'in künyesi ④'ün satırlarını taşıyor (INPUT MODE /
          BASELINE "THE FILM AS SCREENED" / ENDS OR STOPS / PEAK — ⑤ rubriğinde bu
          satırlar YOKTUR); ② ve ⑥'nın OUT-OF-SCOPE satırları ①'in TOP-3'ünü
          (4:50 rigid · 4:20 exhaust) birebir tekrar ediyor.
HAM:      ../02_HAM_RAPORLAR/THE_SKYLIGHT_{KARE,DEVAMLILIK,SES,HIKAYE,ARKA_PLAN,FIZIK}_HAM.md
PLAN:     ../../../yatay_4_dk_filmler/THE_SKYLIGHT/THE_SKYLIGHT_PLAN.md
SPEC:     ✅ VAR — ../../../yatay_4_dk_filmler/THE_SKYLIGHT/THE_SKYLIGHT_QA_SPEC.md
          (A/B/C blokları · C bloğu 30 satırlık kilit listesi) — ⛔ operatöre VERİLMEDİ
MÜZİK:    THE_SKYLIGHT_MUZIK.md yazıldı (28.08) — kurguda müzik VAR mı ölçülmedi
          (aşağıda: ses yatağı var, cue ayrımı kulakla yapılmadı)
KARELER:  scratchpad/qa/sheetA.png (0:05·0:25·0:35·1:05·2:07·2:25·3:03·3:07·3:15)
          scratchpad/qa/sheetB.png (2:15·3:55·4:05·4:15·4:24·4:45·4:55·5:05·5:12)
          scratchpad/qa/corner2.png (sağ alt köşe, 30 s'de bir, 11 örnek)
```

---

## ⭐ ⑪ ÖLÇÜM KAPISI — master'dan okunan sayılar (rapor sayıları DEĞİL) [D125]

| Ölçüm | Değer | Raporlar ne dedi | Sonuç |
|---|---|---|---|
| Süre (container) | **315,155 s** | ~314 / ~315 s ESTIMATED | ✅ |
| Çözünürlük · fps | 1920×1080 ve 3840×2160 · **30 fps** | ⑥ "24 fps assumed" | ⑥'nın süreleri ×0,8 kayık |
| Ses kanalı | **VAR** — AAC 253 376 bit/s · 48 kHz · 2 kanal | 6/6 "nothing audible to me" · ③ "AUDIO STATE B" | ⛔ **D137 · 3. vaka** — ölçüm satırı rubriğe yapıştırılmadı; ses ekseni ÖLÇÜLMEMİŞ sayılır |
| Loudness | **−17,0 LUFS** integrated · mean −19,8 dB · **true peak −0,0 dBFS** | — | ⛔ ihraç kilidi (KURGU_RITMI §6): −14 LUFS · −1,0 dBTP — **3 LU kısık, tepe sınırın 1 dB üstünde** |
| silencedetect −50 dB / 0,3 s | 200,09-200,47 (0,38 s) · 210,06-210,49 (0,43 s) · 310,15-315,16 (5,0 s) | ③ "ambience hole: none" | ⛔ iki klip başı dijital delik (S20 ve S21 girişleri) [D83] · son 5 s = kart |
| Kesme ızgarası scene>0,3 | tek kesme: 131,6 s | 30 kesme | ⛔ dedektör KARANLIK filmde kör (eşik 0,08'de de 4 nokta) |
| Izgara ikamesi | delikler 200,09 · 210,06 + kart başı 310,15 → hepsi **10 s'nin katı** | — | ✅ ızgara **10 + (n−1)×10** — hook 10 s, **9'a KIRPILMAMIŞ**; 31 klip = 310 s |
| I-frame'ler | sabit ~6 s GOP (0,0 · 6,6 · 12,6 …) | — | ikame olarak İŞE YARAMAZ (kesmeye değil GOP'a oturuyor) |
| Köşe şeridi (crop 360×240 sağ alt · 30 s'de bir) | **11/11 örnekte aynı "▷" ikonu** | ⑤ "EDGES: Clean" ×31 · ① filigran kutusu boş | 🔴 **ÜRETİCİ FİLİGRANI HER KAREDE** → D150 |

> Rapor ile ölçüm çelişen her yerde ÖLÇÜM kazanır. Kesme dedektörünün körlüğü kayda
> geçer: bu filmde ızgara ses deliklerinden ve kart başından okundu (üçü de 10 s katı).

---

## ⛔ ④ KURGU KAPISI — önce ayıkla, sonra say [D93 · D109 · D118 · D120]

```
SAHNE-DIŞI MALZEME:  5:10,15-5:15,16 · 5,0 s · "THE SKYLIGHT" başlık kartı
                     → kurgunun SONUNDA · sayımın ve sürenin DIŞINDA · 🔴 loglandı
                     ⛔ kart, KAPAK A'nın (eski S0 kapağı) tipografili hâlidir —
                        KAPAK dosyası "kapak çıktısı kurguya EKLENMEZ" der
                        [D34/D70/D72]; D70/72 zincirinin yeni vakası
                        (Loss of Lift 8., Rose Coat, Blue Drift, Thin Roof…)

a) KLİP SAYISI   31                ≠ plan 33            ⛔  (−2 klip)
b) SÜRE          310,15 s          ≠ plan 329 s         ⛔  (Δ −19 s = −2 klip −20 s
                                                            + hook kırpılmadı +1 s)
c) SIRA          şerit TUTMUYOR — aşağıda                ⛔
d) FİNAL VURUŞ   5:05 karesi: pencere OTS, Mars limb'i, terminatör, siyah uzay,
   [D141]        kask+omuz → planın S32'si EKRANDA ✅ · 3:40-3:50 "glowing orange
                 spot at crater floor" (② ve ⑤ birbirinden bağımsız) → S24 KALAN
                 IŞIK ekranda ✅ (kare çıkarılmadı, iki rapor + ölçek tarifi yeterli)
```

### 🧬 İNSAN ŞERİDİ — Δ okuması [D118 · D121]

```
PLAN (33)          1111111111111111111111111111-1111        insansız yuva S28 → 279 s
④ HİKAYE (31)      11111111111111111111111111-1111          "-" S26 → 4:20 = 260 s ✅ kendi envanteriyle tutarlı
② ⑤ ⑥ (30!)       1111111111111111111111111-1111           31 sahne için 30 karakter — "-" 26. sırada = S25 ✗
                                                            (üçü de kendi envanterinde S26 yazıyor: 1 kısa)
① KARE (30)        111111111111111111111111111111           insansız yuva HİÇ YOK — kendi 4:24 bulgusuyla çelişir 🚨

Δ = 260 − 279 = −19 s  →  −2 klip (−20 s) + hook +1 s
· kalkıştan SONRAKİ yuva sayısı: plan 4 (S29-S32) = rapor 4 (S27-S30) → KUYRUK TAM ✅
· eksik iki klip kalkıştan ÖNCE, yani ODA bölümünde (plan S0-S24'ün 23'ü ekranda)
```

**Eksik ikisinin yeri (kareyle daraltıldı):** plan S13 (eğik sütun) kurguda **2:07 =
yuva 12** (kare: sütun 30° eğik, elips zeminde ✅) → S0-S12 arasında **1 eksik**; plan S20
(son taş, ışık klip içinde söner) kurguda **3:00-3:10 = yuva 18** (kare 3:03 loş gün ışığı +
jalon #2 → 3:07 zifir + fener ✅) → S14-S19 arasında **1 eksik**. Altı raporun hiçbiri
**pusula** (S14, pirinç, rakamsız gül) ve **duvara sürtülen eldiven** (S11, katmanlar)
yazmadı → adaylar **S11 + S14** — ⬜ sahip master'da 1:40-2:10 ve 2:10-2:50'yi izleyip
kapatır. Yuva 19-20 (3:10-3:30: "kare cihaz" = S22 yedek hücre ✅ · "taş ekler" = ?) plan
S21/S22 ile **SIRA ŞÜPHESİ** taşıyor: devir (S22) koni dönüşünden (S21) ÖNCE görünüyor
olabilir → ⬜ 3:10-3:30 izlenir.

---

## 🧭 ⑨ HİZALAMA KAPISI — ızgara PLANDAN alınır [D115]

Sessiz film: replik ekseni yok; ızgara dilimleri ses delikleriyle doğrulandı (200,09 ·
210,06 → S20/S21 girişleri; plan 199/209 olacaktı → **+1 s = kırpılmamış hook**).

| Kurgu yuvası | Zaman | Plan | Kanıt |
|:--:|---|:--:|---|
| 0 | 0:00-0:10 | S0 | kare 0:05: delik, dipte parlak oval, kenarda minik figür ✅ (oval BEYAZ/düz — aşağıda) |
| 2 | 0:20-0:30 | S2 | kare 0:25: OTS, dipteki oval "su birikintisi/buz" gibi ✅ raporla aynı okuma |
| 3 | 0:30-0:40 | S3 | kare 0:35: sütun = **toz perdesi/şelalesi**, kıvrımlı ⛔ |
| 6 | 1:00-1:10 | S6 | kare 1:05: profil yürüyüş, sütun = beyaz toz sütunu ⛔ |
| 12 | 2:00-2:10 | S13 | kare 2:07: sütun 30° eğik ✅ · **İKİ FİGÜR** 🔴 |
| 13-17 | 2:10-3:00 | S14-S19 (biri eksik) | kare 2:15: eldivenden toz döker (S15 taş?) · 2:25: sırt tozlu, tünel |
| 18 | 3:00-3:10 | **S20 DORUK** | kare 3:03 → 3:07: gün ışığı klip içinde SÖNDÜ ✅ — ④ "no peak located" = RAPOR |
| 19 | 3:10-3:20 | S22 (devir) | kare 3:15: cairn üstüne amber ışıklı küçük hücre ✅ ("square device") |
| 21-22 | 3:30-3:50 | S23-S24 | ②⑤: samanyolu · kraterde turuncu nokta ✅ |
| 23 | 3:50-4:00 | S25 | kare 3:55: şafak ovası, gemi uzakta, delik solda, venting ✅ |
| 24 | 4:00-4:10 | S26 | kare 4:05: gemi yakın, el bacakta ✅ · **kanyon duvarları** ⛔ |
| 25 | 4:10-4:20 | S27 | kare 4:15: kabin, kemer, çubuk ✅ · kask **tam saydam kubbe** ⛔ · suit tertemiz ⛔ |
| 26 | 4:20-4:30 | S28 | kare 4:24: kalkış, 3 mavi-beyaz alev, toz bulutu yok ✅ · alev OPAK, bacaklarla çakışık ⛔ |
| 28 | 4:40-4:50 | S30 | kare 4:45: OTS pencere, kalkan volkanlar, ince limb ✅ |
| 29 | 4:50-5:00 | S31 | kare 4:55: kemerli, eller kolçakta, yüzen **cıvatalar** ⛔ |
| 30 | 5:00-5:10 | S32 | kare 5:05: Mars limb'i + terminatör ✅ · kask **koyu tonlu** ⛔ |
| — | 5:10-5:15 | kart | kare 5:12: KAPAK A + "THE SKYLIGHT" tipografisi 🔴 |

---

## 🪪 ③ KİMLİK KAPISI [D105] — ✅ GEÇTİ (5 çapa, gereken 2)

```
① SAYISAL   gemi: 3 iniş bacağı · tek gövde · gövde boyunca tek ince şerit
            rapor ② "single black vertical stripe" · kare 3:55 ✅
② VURUŞ     turuncu-beyaz çizgili jalon cairn'lerin yanında (plan: jalon #1 S7, #2 S20)
            rapor ②⑤ 1:10 ve 3:00 ✅
③ SAYISAL   ışık sütunu 30° eğik, elips zeminde (plan S13) — kare 2:07 ✅
④ VURUŞ     gün ışığı klip İÇİNDE söner + fener yanar (plan S20 CENTRAL CHOICE) — kare 3:03→3:07 ✅
⑤ VURUŞ     MECO: gevşek kemer, yüzen kayış ucu, siyah uzay (plan S31) — rapor ②④ 4:50 ✅
```
⛔ 5:12'deki başlık kartı çapa olarak KULLANILMADI [D105]; ④'ün `FILM: THE SKYLIGHT`
satırı karttan okunmuştur, kanıt değildir.

---

## 🔁 ⑤ ÇAPRAZ SAYIM KAPISI [D107 · D121 · D135]

```
KESME     ① 30 · ② 31 · ③ 30 · ④ 30 · ⑤ 30 · ⑥ 30      fark ≤ 1 ✅ (② karta giden kesmeyi de saydı)
REPLİK    6/6 "none — nothing audible to me"              ✅ tutarlı — ama ölçüm: −17 LUFS ses VAR [D137]
ŞERİT     ④ 31 karakter ✅ · ②⑤⑥ 30 karakter (1 kısa) · ① insansız yuva yok 🚨
          → şerit ekseni yalnız ④'te sağlam; ① kendi bulgusuyla çelişiyor
⑦ PARMAK İZİ  önceki koşu THE THIN ROOF (65 s · 6 seg · kart 0:58) ↔ bu (315 s · 31 seg ·
          kart 5:10) → şüphe YOK ✅
```

---

## 📓 ② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — raporun her bulgusu plana ve KAREYE karşı

| # | rapor ne dedi (timecode) | hangi kilit | çözüm eylemi | sonuç |
|:--:|---|---|---|---|
| 1 | ① 🔴 2:07 ikinci astronot | SPEC C "İNSAN tam 1" | kare 2:07 | 🔴 **FİLM SAPTI** — iki figür yan yana elipste (S13, geniş, silüet ölçeği) |
| 2 | ① 🔴 4:24 alev bacakların içinden | plan "gemi sürekli ivmelenir" (bacak kilidi YOK) | kare 4:24 | 🔴 **FİLM SAPTI + TASARIM BOŞLUĞU** → D148 |
| 3 | ①⑥ 🟠 4:52 0g'de rijit beden | SPEC "İNSAN KEMERLİ, süzülme 0 [D23]" | kare 4:55 | ⚖️ **TASARIM** (⑩ düşer) — ama kollar da yüzmeli → D149 tasarım eki |
| 4 | ②⑤ "floating bolts" 4:50 | prompt "two dust motes + strap end" | kare 4:55 | ⛔ **FİLM SAPTI** — nesne halüsinasyonu (cıvata) → D149 |
| 5 | ② 🟠 kask: opak yanak 0:10 → saydam kubbe 4:10 | bible "closed, seamless optically clear visor" (geometri YOK) | kare 0:25 · 4:15 · 5:05 | ⛔ **FİLM SAPTI + TASARIM BOŞLUĞU** — üç kask → D146 |
| 6 | ② 🟠 kir: sırt tozlu 2:20 → tertemiz 4:10 | SPEC "tam 3 sabit bölge [D42]" | kare 2:25 · 4:15 | ⛔ **FİLM SAPTI** (mağara partisi bible'dan saptı, kabin uydu) → D147 |
| 7 | ②⑤ 🟠 jalon 1:10'da var, 1:50'de yok | SPEC "cairn sayacı: S7 7 taş + jalon #1 → S12 5 taş (jalonsuz)" | plan okundu | ✅ **RAPOR UYDURDU / TASARIM** — 1:50 cairn #2'dir, jalonu yoktur |
| 8 | ② 🟡 cairn ~4 taş 1:10 → ~7 taş 3:00 | dört AYRI cairn (1→4) | plan okundu | ✅ **TASARIM** — farklı istasyonlar |
| 9 | ②⑤ 🟡 krater dibi 0:00 kuru → 0:20 su/buz | S0 kapısı "delik + ışık gölü" | kare 0:05 · 0:25 | ⚠️ **YARI** — göl S0'da VAR (rapor uydurdu) ama beyaz/düz, iki mercek "su/buz" okudu → novum okunurluğu → D144 |
| 10 | ⑤ 🟠 4:00 kanyon duvarları | plan "open plain" · SHIP BIBLE | kare 4:05 | ⛔ **FİLM SAPTI** → D145 |
| 11 | ② 🟠 gemi şeridi siyah dikey 3:50 → beyaz yatay bant 4:00 | bible "TEK amber şerit · düz yatay pencere bandı" | kare 3:55 · 4:05 | ⚠️ **YARI** — 3:55 amber şerit ✅; 4:05'te pencere bandı BEYAZ parladı, şerit görünmez → prompt kilidi eksik |
| 12 | ⑤ 🟡 4:50 gri ay | (kilit yok; gerçekçilik: Mars'ın büyük ayı yok) | rapor | ⛔ **FİLM SAPTI** — "no moon" kilidi S31/S32 promptuna |
| 13 | ⑥ 🟡 toz sütunda asılı 0:30 ↔ elden düşen hızlı 0:40 | SPEC "toz 3-4 s'de TAM çöker" | kare 0:35 · 1:05 | ⛔ **FİLM SAPTI** — sütun toz ŞELALESİ (⑥ "accept it" dedi; kabul edilmez) → D143 |
| 14 | ⑥ 🟡 1 g yürüyüş ↔ 0,38 g toz | SPEC "yürüyüş NORMAL tempoda [D44]" | plan | ✅ **TASARIM** — ⑥'nın g tahmini 3,8 m/s² Mars'ı DOĞRULADI |
| 15 | ⑥ 🟡 gemi gölgesi uzun ↔ gök parlak | plan "şafak, uzun mor gölgeler" | kare 3:55 | ✅ **TASARIM** (şafak) |
| 16 | ④ "no peak located" · "adds rock 3:20" | SPEC "DORUK S20 → ışık klip içinde söner" | kare 3:03→3:07 | ✅ **RAPOR** — sönüş EKRANDA; mod V mercek okumadı |
| 17 | ④ "square device = only true novum / AI hallucination?" | SPEC "YEDEK HÜCRE S22'de cairn #1 üstüne" | kare 3:15 | ✅ **TASARIM** — ama izleyici için EN dikkat çeken nesne oldu (açık soru, aşağıda) |
| 18 | ② "Counter: NONE" · ⑤ count log yalnız taş | SPEC 4 metinsiz sayaç (sütun eğimi · cairn 1→4 · fener hücresi · kir) | — | ⬜ **ÖLÇÜM BOŞLUĞU** [D134] — sayaç okunmadı; mod D'de C bloğu ⑤'e verilir |
| 19 | ① 🟠 0:14 parmaklar kayaya kaynıyor · 🟠 2:14 toz eldivenden geçiyor · 🟠 4:16 eller kemere kaynıyor · 🟡 1:23 mumsu cilt · 🟠 1:31 fener bloom · 🟠 3:39 kayarak yürüme | negatif çekirdek (temas · bloom · adım) | kare yok (bu saniyeler çıkarılmadı) | ⬜ **AÇIK** ×6 — mod D koşusunda kareyle kapatılır |
| 20 | ② 🟡 boru 1:30 yok → 1:50 kalçada | bible "slim horizontal rod-case, always worn" | kare 1:05 sırtta ✅ | ⬜ **AÇIK** — 1:30 karesi çıkarılmadı |
| 21 | 6/6 "nothing audible" · ③ "AUDIO STATE B, unverifiable" | ölçüm: −17 LUFS, delik yalnız 3 yerde | ffprobe/ffmpeg | ✅ **RAPOR YANILDI** [D137 · 3. vaka] — ses ekseni bu partide ölçülmemiş sayılır |

**Kapalı:** 15 · **Açık:** 6 (19: altı temas/bloom/adım bulgusu · 20 · 18). ⛔ Açık madde
varken ① ve ②'nin skoru zaten tabloya girmiyor [D129]; **dersler yalnız KAPALI satırlardan
yazıldı** (1 · 2 · 4 · 5 · 6 · 9 · 10 · 13 + ölçüm satırları).

---

## 🔴 RAPORLARIN GÖRMEDİĞİ DOKUZ İHLAL — ölçümden ve kareden

| # | İhlal | Kanıt | Kilit |
|:--:|---|---|---|
| 1 | **Üretici filigranı her karede** (sağ alt "▷") | köşe şeridi 11/11 · sheetA/B 18/18 | metin/logo 0 kare · **teslim kusuru** → D150 |
| 2 | **Toz şelalesi** — sütun toz perdesi | kare 0:35 · 1:05 · 2:07 | çekirdek "never swirling" · S3 kapısı → D143 |
| 3 | **Kapak kurguya girdi** — 5 s tipografili kart | kare 5:12 · silencedetect 310,15 | D34/D70/D72 · KAPAK dosyası |
| 4 | **Hook kırpılmadı** — S0 10 s | delikler 200,09/210,06 (plan 199/209) | SPEC "TRIM BUDGET 1 s (S0 10→9)" |
| 5 | **2 sahne eksik** (31 ≠ 33) | Δ −19 s · şerit | D100 (klip düşürme) · kurgu kapısı a/b |
| 6 | **−17,0 LUFS · true peak −0,0 dBFS** | ebur128 · volumedetect | KURGU_RITMI §6: −14 LUFS · −1,0 dBTP |
| 7 | **İki klip-başı dijital delik** 0,38 s · 0,43 s | silencedetect 200,09 · 210,06 | D83 (yatak klip sınırında ölmez) |
| 8 | **Işık gölü BEYAZ/BUZ okunuyor** (S0/S2) | kare 0:05 · 0:25 + ②⑤ "puddle/ice" | novum okunurluğu · S0 kapısı → D144 |
| 9 | **"toz zerresi" → cıvata** (S31) | kare 4:55 · ②⑤ "bolts" | D23 nesneyle kanıt — adsız nesne → D149 |

---

## 🔍 ⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108]

| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| 0g'de rijit beden (4:50-4:52) | ① 🟠 · ⑥ 🟠 cat 9 · ② ④ flag | ① (kare deseni) | ⑩'da düştü — tasarım [D23]; D149 tasarım eki |
| alev bacaklardan geçiyor (4:20-4:24) | ① 🔴 · ② ⑥ flag | ① | ① — ⑥'ya işaretçi |
| krater dibi su/buz (0:00 ↔ 0:20) | ② 🟡 cat 6 · ⑤ 🟡 cat 4 | ⑤ (alan) | ⑤ — ② işaretçi |
| jalon yok (1:50) | ② 🟠 cat 8 · ⑤ 🟠 cat 6 | — | ⑩'da düştü (cairn #2 jalonsuz) |
| gri ay (4:50) | ⑤ 🟡 | ⑤ | ⑤ |
| başlık kartı (5:10) | 6/6 NON-SCENE | — | kurgu kapısı 🔴 — puan değil, teslim kusuru |

---

## 🧮 ⑩ ÖNERME KAPISI [D87 · D116 · D130 · D131 · D134] — bilgi amaçlı; tabloya girmez [D129]

```
DÜŞEN bulgular (kaynağı planda yazılı): 0g rijit beden (D23) · 1 g yürüyüş (D44) ·
  jalon yok 1:50 (cairn #2) · cairn taş sayısı (4 ayrı cairn) · "square device" (S22
  hücre) · "no peak" (S20 ekranda) · uzun gölge (şafak) · "dust hangs" KISMEN (yavaş
  çöküş tasarım — ama perde değil)
AYAKTA kalanlar: klon 2:07 · alev/bacak 4:24 · kask üç hâl · kir sıfırlanması · kanyon
  4:00 · ay 4:50 · toz şelalesi · cıvatalar · pencere bandı beyaz 4:00
② geri verilen puan (bilgi): cat 8 +3 (jalon) · cat 12 +1 (cairn) → 87 → 91 / 12 = 7,6
⑥ geri verilen puan (bilgi): cat 9 +4 (0g tasarım) · cat 7 +2 (yürüyüş) · cat 8 +2 →
  64 → 72 / 8 = 9,0 — ⑥'nın g ≈ 3,8 m/s² tahmini planın 0,38 g'sini DOĞRULAR
⑤ SPEC'e göre yeniden sıralama [D134]: ① kanyon (SHIP BIBLE/ova kilidi) · ② ay ·
  ③ krater dibi — "jalon" listeden düşer
④ HİKAYE: mod V, SPEC'siz → kesme listesi (S13·S10·S12) UYGULANMAZ — üçü de sütun
  saati sahneleri (S14/S10/S13 aileleri), biri KESİLEMEZ viral (S13). Aynı desen:
  D129 (Rose Coat) · D116.
```

---

## ⭐ ④ HİKAYE MERCEĞİ — ne doğru gördü, ne göremedi

Mod V bir hikâye merceği = filmi ilk kez gören izleyicidir; bu yüzden sayısı tabloya
girmese de OKUMASI veri:

```
GÖRDÜ    · "An astronaut wanders through caves to build a small stack of rocks before
           flying away" — ölçek novum'u ve SAAT (sütun eğimi) OKUNMADI; altı "sütun"
           sahnesi "aynı sahne" sayıldı
         · shareable moment = 0:00 krater — S30 değil (⚠️ kapak kararı için veri)
         · "square device" en dikkat çeken nesne — hücre, sütundan daha çok okundu
GÖREMEDİ · doruk 3:03→3:07 (ışık klip içinde söner) — "no peak located"
         · S24 kalan ışık = tema ödemesi — "Bookend"
         · viral/interstitial koruması — kesme listesi S13'ü kesiyor
AÇIK     ⬜ sütun eğimi sayacı (dik → 30° → kopuk) izleyiciye "zaman" olarak geçiyor
         mu? Tek mod-V okuma ders değildir; cevap yayın verisi (tutunma eğrisi
         1:40-2:50) ve mod D koşusudur. Şimdilik: HİKAYE_KALİTE tablosuna girmez.
```

---

## 📊 SKOR SATIRLARI

```
T1-T6: SATIR YOK [D129]. Raporların kendi toplamları (referans, ölçüm değil):
  ① 6,8 (5 kategori) · ② 7,3 · ③ — (hiçbir kategori) · ④ 3,3Ⓥ · ⑤ 8,2 · ⑥ 8,0
Tamlık matrisi: 0/4 KALIR.
```

---

## ✅ BİR SONRAKİ KOŞU İÇİN — sırayla

```
1. MASTER YENİDEN İHRAÇ (kurgu, sahip):
   □ filigransız kaynak klipler (üretici ihraç ayarı) — köşe testi 0/11
   □ başlık kartı YOK (kapak ayrı dosya) · hook S0 10→9 s
   □ −14 LUFS integrated · true peak ≤ −1,0 dBTP · 4K (1440p+)
   □ klip başı delikler kapatılır: yatak tek parça serilir (200,1 · 210,1) [D83]
   □ MUZIK cue'ları kurguya serildi mi (3:14 kesiş · 5:09 MECO) — kulakla
2. YENİDEN ÜRETİM (⬜ sahip onayı — D129: bu partinin reçetesi uygulanmaz, ölçülen
   kareler uygulanır): S13 (klon) · S3/S6 (toz yoğunluğu, D143) · S26 (ufuk kilidi,
   D145) · S28 (bacak/alev, D148) · S27/S29/S31/S32 (kask geometrisi D146 + kir
   fazı 4 D147 + 0g beden D149 + "no moon") · eksik 2 sahne (aday S11 · S14)
   — ÖNCE bible'a kask geometrisi + kir merdiveni girer, sonra prompt_kontrol
3. MOD D KOŞUSU: ①'e A+B, ④'e A, ⑤'e C'nin üç kilidi, ⑥'ya C'nin sayısal kilitleri;
   ⑪ ölçüm satırı (SES KANALI: VAR · −x LUFS) her rubriğin künyesine YAPIŞTIRILIR
   [D137]; her mercek TEMİZ oturumda [D110]; altısına AYNI dosya [D75]
4. Kapak kararı: ④ shareable = 0:00 krater; S30 kapağı yayın-sonrası karar kuralıyla
   (KAPAK dosyası) — bu koşu veri, karar değil
```

---

## 📚 BU KAYITTAN ÇIKAN DERSLER

```
YENİ   D143 toz cümlesi yoğunluk sayısı taşımadı → toz şelalesi (03_FIZIK)
       D144 üretim kapısında KABUL/RET ölçütü yoktu (09_SISTEM)
       D145 alçak açı ufku kapatır, model duvar doldurur (04_ISIK)
       D146 "seamless visor" = kubbe daveti; vizör geometrisi sayıyla (02_KARAKTER)
       D147 sabit aşınma tozlu ortamda tutmaz → kir merdiveni (02_KARAKTER)
       D148 kalkışta katlanan bacak + opak alev (03_FIZIK)
       D149 0g'de kemerli insanın kolları da yüzer; adsız zerre cıvata olur (03_FIZIK)
       D150 filigran 315/315 s — altı mercek görmedi; köşe testi ⑪'e (08_QA)
TEKRAR D129 (8. film) · D137 (3. vaka) · D70/72 (başlık kartı, kapak olarak) ·
       D100 (2 klip düştü) · D83 (2 delik) · D74 (kapı koşulmadı) · D110 (oturum)
```
