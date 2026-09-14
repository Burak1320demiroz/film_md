# 🎈 LOSS OF LIFT — FİLM QA KAYDI

> **Plan:** `yatay_4_dk_filmler/LOSS_OF_LIFT/LOSS_OF_LIFT_PLAN.md`
> **Format:** 16:9 · 3-5 dk · bilimkurgu · Venüs bulut katmanı (54 km)
> **Plan özeti:** 25 sahne (Hook 9 s + 24 × 10 s = 249 s) · 0 sahne içi kesme ·
> 1 replik (S22) · viral S5·S13·S19·S23 · doruk S20 · insansız S0·S13·S19·S24
> **QA partisi:** 21.08.2026 · Gemini · 3 koşu (📖 SENARYO ×1 · 🧩 MANTIK ×2)

---

## 🔭 MERCEK DURUMU (21.08.2026)

| Mercek | Durum | Skor | Geçerlilik |
|---|---|:--:|---|
| 🔧 TEKNİK | koşulmadı | — | ❌ |
| 📖 SENARYO | koşuldu — mod V | Ⓥ 7.0 | ⛔ **ÖN KOŞU** [D94] — SPEC planda hazırdı (satır 738), verilmedi |
| 🧩 MANTIK | koşuldu — mod V ×2 | ~~8 / 6~~ | 🚨 **GEÇERSİZ** — kopya çifti [D110] + aritmetik ihlali [D119] |
| 🔊 SES (ops.) | koşulmadı | — | ❌ |
| 🧍 KARAKTER (ops.) | koşulmadı | — | ❌ |

**Üç koşu da AYNI oturumda, AYNI 255 s kurgu üzerine yapıldı ve AYNI 26 satırlık
sahne haritasını paylaşıyor** — haritanın hatalarına kadar birebir. Bu üç ölçüm
değil, **tek ölçümün üç kılıfıdır** [D110]. Ham raporlar:
`02_HAM_RAPORLAR/LOSS_OF_LIFT_{SENARYO,MANTIK}_HAM.md`

---

## 🪪 ③ KİMLİK KAPISI [D105] — ✅ GEÇTİ (4 çapa, gereken 2)

Rapor gerçekten BU filmi ölçmüş. Metin-olmayan çapalar:

```
① SAYISAL   manifold: rapor "~12 small nozzles in a row" (1:40)
            plan  : 12 yuva · 11 boş ve sökülü · 1 dolu 600 kg tüp
② SAYISAL   ızgara: rapor 0:00-0:09 hook + 24 × ~10 s
            plan  : Hook 9 s + 24 × 10 s = 249 s
③ KOSTÜM    rapor "beige/light grey knit cardigan over grey coveralls"
            plan  : "faded sand-grey thermal jumpsuit ... under an old
                    light-grey knitted cardigan with a stretched-open collar"
④ REPLİK    rapor 3:40 · "Ağırlık bende kalsın."
            plan  : S22 · "Ağırlık bende kalsın." — ızgarada 3:39 (Δ 1 s)
```

⛔ 4:10'daki **"LOSS OF LIFT" başlık kartı çapa olarak KULLANILMADI** — ekrandaki
yazı kimlik kanıtı değildir [D105] ve bu filmde ekran metni kilidi 0.0 saniyedir.

---

## 🚪 ④ KURGU KAPISI [D109] — ✅ SAYI VE SÜRE GEÇTİ · ⛔ SIRA GEÇEMEDİ

**Önce ayıkla, sonra say [D93]:**

```
SAHNE-DIŞI MALZEME:  4:10-4:15 · 5 s · statik "LOSS OF LIFT" başlık kartı
                     → kurgunun SONUNDA · sayımın DIŞINDA · 🔴 loglandı [D70/72]
```

```
a) KLİP SAYISI   26 − 1 kart = 25   =  plan 25          ✅
b) SÜRE          255 − 5 kart = 250 s ≈ plan 249 s (Δ 1 s ≤ 2) ✅
c) SIRA          insan şeridi TUTMUYOR — aşağıda            ⛔
```

> 🔴 **BAŞLIK KARTI, 8. VAKA [D70/72 zinciri].** Planın kilidi: `EKRAN METNİ
> 0.0 saniye`; kapak dosyasında da "kapak çıktısı kurguya GİRMEZ" yazılı.
> Prompt seviyesindeki metin yasağı tutmuş (25 klibin hiçbirinde yazı yok),
> yasak KURGU masasında delinmiş. Prompt yasağı kurguyu koruyamaz.

### 🧬 İNSAN ŞERİDİ — sıranın metinsiz parmak izi [yeni kilit · D118]

Planın "İnsan" sütunu 25 karakterlik bir dizedir; raporun "Present" sütunu da
aynı dizeyi üretir. İkisi yan yana:

```
PLAN    -111111111111-11111-1111-
RAPOR   -111111111111-111111-111-
                            ^^
                            slot 19 ve 20 YER DEĞİŞTİRMİŞ
```

Plan: S19 = insansız viral (gecede tek mor lomboz) · S20 = **doruk** (kol
manifoldda atılır). Rapor: 3:09'da adam manifoldda, 3:19'da insansız gece dışı.
Sayı ve süre kapılarının ikisi de geçtiği hâlde **filmin doruğu yanlış yuvada
olabilir** — bu kapı olmasaydı üç QA koşusu bu soruyu hiç sormayacaktı.

---

## 📐 ⑨ HİZALAMA KAPISI [D115] — ✅ IZGARA GERİ ALINDI

Raporun sahne SAYISI hiçbir kapıya girdi sayılmaz; ızgara PLANDAN alınır:
`sahne başlangıcı(n) = 9 s + (n−1) × 10 s`. Replikle doğrulama:

```
beklenen (S22)  = 9 + 21 × 10 = 219 s = 3:39
raporun repliği = 3:40                        |Δ| = 1 s ≤ 2  ✅ SAHNE YERİNDE
```

**Raporun numaralandırması bir kaydırmadır: rapor Sn = plan S(n−1).** Aşağıdaki
tablo raporun kendi haritasının yerine geçer.

| Rapor | Zaman | Plan | Plan sahnesi | Uyum |
|:--:|---|:--:|---|:--:|
| S1 | 0:00-0:09 | **S0** | HOOK — gömülmekte (insansız) | ✅ |
| S2 | 0:09-0:19 | **S1** | YAMA — iç kabukta ütüyle yama | ✅ |
| S3 | 0:19-0:29 | **S2** | PİN YAYI (gondol) | ⬜ rapor "sphere, sighs" |
| S4 | 0:29-0:39 | **S3** | NE SOLUYORSA O TUTUYOR (zarf içi) | ⬜ rapor "brass dial" |
| S5 | 0:39-0:49 | **S4** | DÖRT ASKI | ✅ |
| S6 | 0:49-1:00 | **S5** | VİRAL #1 — SIRT | ✅ |
| S7 | 1:00-1:10 | **S6** | DIŞ YAMA | ⬜ rapor "looking at horizon" |
| S8 | 1:10-1:20 | **S7** | AŞINMA | ⬜ rapor "rolling patch" |
| S9 | 1:20-1:30 | **S8** | AKCİĞER — ilk renk (mor) | ✅ |
| S10 | 1:30-1:40 | **S9** | CAM — tek temas | ⬜ rapor "stepping back" |
| S11 | 1:40-1:50 | **S10** | HESAP — manifold, orta nokta | ✅ |
| S12 | 1:50-2:00 | **S11** | SÖYLEMEDİĞİ — verici | ✅ |
| S13 | 2:00-2:10 | **S12** | PART A KAPANIŞ — lomboz | ✅ |
| S14 | 2:10-2:20 | **S13** | VİRAL #2 — VARMAYAN YAĞMUR (insansız) | ✅ |
| S15 | 2:20-2:30 | **S14** | GECE | ✅ |
| S16 | 2:30-2:39 | **S15** | DÖRDÜNCÜ KOLTUK | ✅ |
| S17 | 2:39-2:50 | **S16** | ÖLEN BANT | ✅ |
| S18 | 2:50-3:00 | **S17** | YÜKSELİM — yanlış umut | ⛔ yön çelişkisi |
| S19 | 3:00-3:09 | **S18** | ISI — S3'ün eş kadrajı | ⬜ rapor "hatch" |
| S20 | 3:09-3:20 | **S19** | VİRAL #3 — TEK MOR (insansız) | ⛔ rapor: adam manifoldda |
| S21 | 3:20-3:30 | **S20** | **SEÇİM — DORUK** (manifold) | ⛔ rapor: insansız gece |
| S22 | 3:30-3:40 | **S21** | BEDEL — son pin, vizör kapalı | ✅ |
| S23 | 3:40-3:50 | **S22** | DEVRETME — kartuş + **tek replik** | ✅ |
| S24 | 3:50-4:00 | **S23** | VİRAL #4 — İKİ IŞIK | ⬜ rapor "closes eyes" |
| S25 | 4:00-4:10 | **S24** | FİNAL — S0'ın aynası | ⚠️ rapor: sonda DÜŞÜYOR |
| S26 | 4:10-4:15 | — | **başlık kartı** — sahne değil | 🔴 |

---

## 📋 ① SPEC KAPISI [D94] — ⛔ ÖN KOŞU · 6. VAKA

```
Planda 📋 QA SPEC BLOĞU VAR    → LOSS_OF_LIFT_PLAN.md satır 738
Üç koşu da MOD V              → SPEC rubriğe verilmedi
```

Sonuç, sözleşme gereği:

```
· skor satırları tabloya Ⓥ ⚠️ ŞARTLI girer
· 00_INDEX tamlık matrisinde üç hücre de ❌ KALIR (0/3)
· KESME LİSTELERİ VE REMOVE REÇETELERİ UYGULANMAZ
```

⭐ Bu, deponun **6. mod-V-rağmen-SPEC** vakası (Slow Stone · Starless Circle ·
Third Dune · Ring Light · Banded Deep · **Loss of Lift**) ve mod D hâlâ **0 kez**
koşuldu. SPEC bu kez üretimden ÖNCE, yazım paketinin parçası olarak yazılmıştı —
yine de kullanılmadı. Teşhis: SPEC 906 satırlık planın 738. satırında GÖMÜLÜ ve
QA anında operatörün eline hiçbir şey vermiyor. Karşılığı → **[D117]** ve bu
filmin yanına çıkarılan `LOSS_OF_LIFT_QA_SPEC.md`.

---

## 🧾 ⑤ ÇAPRAZ SAYIM [D107] + KOPYA DENETİMİ [D110]

```
📖 SENARYO : 26 sahne · 25 kesme · 255 s
🧩 MANTIK 1: 26 sahne · 25 kesme · 255 s
🧩 MANTIK 2: 26 sahne · 25 kesme · 255 s
fark 0 ≤ 1  → sayım kapısı biçimsel olarak geçti
```

⛔ **Ama bu doğrulama değil KOPYADIR.** D110'un imzası birebir gerçekleşti:

```
· üç raporun sahne sınırları saniyesi saniyesine aynı
· iki MANTIK koşusunun ÇELİŞKİ DEFTERİ üç satırıyla birebir aynı
· severity tally birebir aynı: 🔴0 🟠1 🟡2
· üç rapor da AYNI dört yanlış okumayı taşıyor (S2/S3 · S6/S7 · S19/S20 · S17)
```

Üstelik MANTIK rubriğinin STEP 1'inde "bu envanteri yalnız medyadan kur, aynı
oturumdaki bir haritayı delil sayma" yasağı **yazılıydı** ve model onu okurken
kopyaladı. Rubrik kendi oturumunu göremez — bu yasağın uygulanma yeri operatör
tarafıdır: her mercek TEMİZ sohbette koşulur.

**Yeni gözlem — D110'a ek:** kopya defter ölçüm sapmasını her zaman KÜÇÜK
göstermiyor. Burada iki koşu **tek bir yeni gözlem üretmeden 2.0 puan** ayrıştı
(8/10 vs 6/10). Fark filmden değil rubriğin aritmetik boşluğundan geliyor → **[D119]**.

---

## 🔒 ② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 6 madde, 6'sı ⬜ AÇIK

⛔ Aşağıdaki maddeler bulgu listesinden ALINMIŞTIR. Hiçbiri puan düşürmez,
hiçbirinden ders yazılmaz, hiçbiri yeniden üretim siparişi doğurmaz — **master'ın
o saniyesi izlenene kadar.** Toplam iş: **~1,5 dakika seyretme.**

| # | Rapor ne dedi | Hangi kilit | İzlenecek saniye | Sonuç |
|:--:|---|---|---|:--:|
| 1 | 3:09'da adam manifoldda, 3:19'da insansız gece dışı | Plan: S19 insansız viral · S20 DORUK · insan şeridi | **3:09-3:29** | ⬜ AÇIK |
| 2 | 2:50'de "ibre hızla düşüyor, alarm" | `PİN YAYI`: S17 = **+2 çentik YUKARI**, 6 s, sonra aynı çentiğe dönüş; alarm yok | **2:49-2:59** | ⬜ AÇIK |
| 3 | Manifold 1:40'ta ~12 ağızlı, 3:09'da ~6 büyük tüplü | `TÜP`: 12 yuva · 11 boş · 1 dolu · S10↔S20 **eş kadraj** (32mm/4 m) | **1:39-1:49 + 3:19-3:29** | ⬜ AÇIK |
| 4 | 0:09'da yamalar üst üste, 0:19'da ızgara düzeninde | Rapor iki AYRI mekânı aynı sanıyor: S1 zarf içi ↔ S2 gondol | **0:19-0:39** | ⬜ AÇIK |
| 5 | 1:00'da bakıyor, 1:10'da yamalıyor (sıra ters) | Plan: S6 DIŞ YAMA → S7 AŞINMA | **0:59-1:19** | ⬜ AÇIK |
| 6 | 4:00'da "sonda ayrılıp DÜŞÜYOR" | `EKRAN YÖNÜ KİLİDİ`: yükselen üst üçlükten çıkar, batan altta oturur; S24'te sonda **YUKARI** | **3:59-4:09** | ⬜ AÇIK |

> ⛔ **6 madde açıkken 🧩 MANTIK skoru sayı taşımaz ve bu partiden içerik dersi
> yazılmaz.** Yazılan üç ders (D117-D119) bu maddelerin HİÇBİRİNDEN değil,
> kapıların kendi davranışından çıkarılmıştır — sonuçları ne olursa olsun
> geçerlidirler.

---

## ⑩ ÖNERME KAPISI [D87 · D116] — planda YAZILI olduğu için DÜŞEN bulgular

| Rapor bulgusu | Planda yazılı kaynak | Karar |
|---|---|:--:|
| "Coveralls S12'de göğüsten açık, S15'te farklı yaka" 🟡 | Kostüm kilidi: hırka **stretched-open collar** ile yazılı; jumpsuit ÜSTÜNDE hırka var | ⬇️ DÜŞTÜ |
| "Yerçekimi normal Dünya" (fizik) | `YERÇEKİMİ 0.904 g` — düşen alet ilk saniyede 4.4 m; "ordinary Earth pace" bilinçli [D44] | ⬇️ DÜŞTÜ |
| "Balon havada asılı duruyor / hovering" | `nötr yüzerlik` filmin ÖNERMESİ — pozitif cümleyle yazılı [D59] | ⬇️ DÜŞTÜ |
| "Gölgesiz, her yönden yayılmış ışık" | Ortam kartı: güneş diski YOK, ışık her yönden [D41 zemini yok] | ⬇️ DÜŞTÜ |
| SENARYO: "S3 CUT — hiçbir yeni bilgi yok" (= plan S2/S3) | S2 = KATALİZÖR (pin bir çentik aşağı) · S3 = filmin TEZİ | ⬇️ DÜŞTÜ |
| SENARYO: "S7 CUT · S10 CUT · S15 CUT" (= plan S6/S9/S14) | S6 direnç · S9 filmin **tek şefkati** · S14 gece geçişi | ⬇️ DÜŞTÜ |
| SENARYO: "S18'i 14. pozisyona taşı" (= S17'yi S13'ün önüne) | Umut-önce-düşüş kilidi: S17 geceden SONRA, seçimden ÖNCE olmak zorunda | ⬇️ DÜŞTÜ |

⛔ **Kesme listesinin 4 maddesinin 4'ü de planın omurgasını hedefliyor** —
katalizör, tez, tek şefkat beati ve gece geçişi. Mod V'nin yapısal körlüğü:
`VIRAL INTERSTITIALS` ve `CENTRAL CHOICE` alanları SPEC'te yazılıydı, rubriğe
verilmedi. Kesme listesi UYGULANMAZ.

---

## ❓ FLAGS FOR DOCUMENT CHECK — plandan cevaplandı

| Raporun sorusu | Plandan cevap |
|---|---|
| 4:10'daki poster kartı fragman işareti mi? | **Hayır.** Kilit: `EKRAN METNİ 0.0 saniye`. Kart kurguda eklenmiş, filmin parçası değil — kaldırılmalı 🔴 |
| Plan bir doruk ilan ediyor mu, 2:50 mi 3:40 mı? | **S20 (3:19-3:29)** — vuruş haritası: "Bedelli seçim / Doruk %79-83". Raporun 2:50 dediği yer S17 = **yanlış umut** beati; raporun bunu doruk sanması ①. maddeyi güçlendiriyor |
| Planın son sahnesi 4:00'daki mi? | **Evet, S24** — ama yön ters okunmuş: plan "sonda YUKARI, küre AŞAĞI" der (defter madde 6) |
| 1:50'deki acı veren düğme ne? | **S11 SÖYLEMEDİĞİ** — vericiyi açıyor, amber lamba nabız atıyor, konuşmuyor, kapatıyor. Acı fiziksel değil: kimseye söylemeyeceğinin kabulü |

---

## ✅ RAPORLARIN DOĞRULADIĞI TASARIM KARARLARI

Bu koşu ÖN KOŞU'dur, ama mod V'nin meşru olarak cevaplayabildiği tek soru —
"hiçbir şey bilmeyen bir izleyiciye ne oluyor?" — üç noktada net cevap verdi:

```
① TEK REPLİK ÇALIŞTI.  Diyalog 9/10 · "korunacak üç şey"in birincisi ·
   "does not narrate the visible" — D35/D40 tasarımı hedefine vurdu.
   Replik ızgarada ±1 s yerinde ve ağız kadraj dışı kilidi bozulmamış.
② NOVUM OKUNDU.        "The one thing nothing else does: tension built around
   a purely physical VERTICAL constraint. The setting is the plot."
   = planın novum cümlesi. Özgünlük 8/10, "swappable değil".
③ FİNAL İMAJI TUTTU.   Paylaşılabilir an olarak S24 seçildi; "resolves the
   choice without needing to show his face" — S0↔S24 çifti işini yaptı.
```

Ölçülen zayıf nokta (mod V'nin meşru okuması, kilit çelişkisi değil):
**sayaç semantiği geç kuruluyor.** "Gauge function unclear until 2:50" ve
0:19 düşme tahmini aynı şeyi söylüyor — pirinç yay S2'de bir kez hareket ediyor,
sonra S17'ye kadar hiç. İzleyici çentiğin ne demek olduğunu doruğa kadar
öğrenemiyor. Bu bir prompt cümlesiyle değil **sahne haritasıyla** çözülür ve
madde 1-2 kapandıktan sonra ders adayıdır → aşağıda.

---

## 📊 TABLOLARA GİDEN SATIRLAR

```
03_HIKAYE : | Loss of Lift Ⓥ | 3-5dk | 6 | 7 | 5 | 7 | 8 | 9 | 6 | 8 | 8 | 6 | ⚠️ 7.0/10 ŞARTLI |
04_MANTIK : ~~satır~~ 🚨 GEÇERSİZ — kopya çifti, iki toplam (8 · 6), ikisi de
            kendi hücrelerinin ortalaması değil (9.5 ve 6.6)
00_INDEX  : tamlık 0/3 DEĞİŞMEDİ — üç hücre de ❌ (ÖN KOŞU [D94])
```

---

## 📚 BU PARTİDEN ÇIKAN DERSLER

| # | Ders | Nereden çıktı |
|:--:|---|---|
| **117** | SPEC gömülü kaldığı sürece mod D hiç koşulmuyor — bloğu DOSYAYA çıkar | ① SPEC kapısı · 6/6 mod V |
| **118** | Kurgu kapısı sayıyı ve süreyi doğruluyor, SIRAYI doğrulamıyor — insan şeridi | ④ kurgu kapısı · doruk yuvası |
| **119** | OVERALL rubrikte yazılı bir aritmetik değilse model uyduruyor | ⑤ kopya çifti · 2.0 puan sapma |

---

## 🎯 SIRADAKİ İŞ (operatör)

```
1. ⏱️ 1,5 DAKİKA SEYRET — defterdeki 6 saniye aralığı, sırayla:
     3:09-3:29 (doruk yuvası — en pahalısı) · 2:49-2:59 · 1:39-1:49 +
     3:19-3:29 · 0:19-0:39 · 0:59-1:19 · 3:59-4:09
   sonuçları deftere FİLM SAPTI / RAPOR UYDURDU olarak yaz
2. ✂️ BAŞLIK KARTINI KURGUDAN ÇIKAR (4:10-4:15) — kilit: ekran metni 0.0 s
3. 🔁 PARTİYİ YENİDEN KOŞ [D110]: her mercek AYRI ve TEMİZ sohbette,
     bu kez MOD D — `LOSS_OF_LIFT_QA_SPEC.md` dosyasını rubrikle birlikte yapıştır
4. 🔧 TEKNİK mercek hiç koşulmadı — sırada o var
```
