# 🌑 THE STATIC SHADOW — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı · **master ÖLÇÜLEMEDİ** ⛔ (dosya depoda/diskte
> yok; operatör yol vermedi) · **üretim defteri BOŞ** (teslim satırı ⬜, 0 klip satırı)
> **Koşu:** 13.09.2026 · **on üç mercek** (①-⑫ + ⑬ UYUM) — **on ikisi mod V, ⑬ STEP −1'de
> DOĞRU DURDU** (prompt · SPEC · defter verilmedi).
>
> ⛔ **HİÇBİR SKOR SATIRI HİÇBİR T TABLOSUNA GİRMEDİ.** `rapor_kontrol.py`: 13/13 🚨 GEÇERSİZ.
> ① SPEC kapısı: `THE_STATIC_SHADOW_QA_SPEC.md` **VARDI**, operatör çıplak rubriği
> yapıştırdı → ①④⑥⑦⑧ TEKRAR [D129], ⑨⑩⑪⑫ GEÇERSİZ/karantina [D190], ②⑤ tekil
> ŞARTLI ama parti düştü. **SPEC hazırken mod V koşulan film: 17.**
> ①.9 TESLİM KAPISI: **plan 15 sahne · makara 12** → parti GEÇERSİZ [D188].
>
> ⭐ **BU KAYDIN ÜRÜNÜ ÜÇ DERS + ÜÇ BETİK KAPISI — üçü de BELGEDEN çıktı, rapordan değil:**
> planın 7 repliği promptlara hiç geçmemiş (D203 · ㉓) · SPEC yedi makine çapasının
> yedisini de kaybetmiş bir kabuk (D204 · ㉔) · ⑤ çapraz kapı süreyi hiç karşılaştırmıyordu
> (D205 · ⑤ SÜRE). Ekran bulgularının TAMAMI ⬜ AÇIK — master gelmeden hiçbiri ders olmaz.

---

## 📦 MALZEME

```
MASTER:   BULUNAMADI. Raporlar "the statıc shadow.mp4" diyor (⑩ ⑫); depo ve ~/ altında
          mdfind/find sıfır sonuç. ⑪.0 kimlik karesi ÇIKARILAMADI.
RAPORLAR: 124-125 s (on mercek) · 12 sahne × 10 s + kuyrukta 4-5 s başlık kartı
          ("THE STATIC SHADOW" — ⑩ ve ⑫ ayrıca tagline "SOME SHADOWS CHANGE EVERYTHING")
          ⑩ 60 s ve ⑫ 25 s yazdı → zaman ekseni uydurma [D205]
PLAN:     15 sahne · 150 s (10 s hook + 14 × 10 s) · 7 HELIOS repliği (MACHINE) ·
          kask 15/15 kapalı, vizör %100 opak · pod = kalkanın 1/30'u · dış kamera mutlak sessiz
PROMPT:   30 prompt (BOLUM_1 16 · BOLUM_2 14) · tırnak karakteri 0 · "no title card /
          no watermark / no atmospheric smoke" 30/30
DEFTER:   THE_STATIC_SHADOW_URETIM_DEFTERI.md — TESLİM SATIRI ⬜ · KLİP SATIRI 0 · SHA yok
MERCEK:   ① — · ② 8,7 · ③ — · ④ — · ⑤ 7,2 · ⑥ 9,1 · ⑦ 7,7 · ⑧ 1,0 · ⑨ 4,0 · ⑩ 1,5 ·
          ⑪ 6,7 · ⑫ 5,8 · ⑬ MISSING   (betik düzeltmesi sonrası; HİÇBİRİ TABLOYA GİRMEZ)
```

---

## §⑪ ÖLÇÜM KAPISI — **KOŞULAMADI**

| ölçüm | değer | sonuç |
|---|---|---|
| master dosya | yok | ⛔ `olcum_kapisi.sh` koşulmadı; raporların süre/sahne/kesme sayıları HİÇBİR kapıya ölçüm olarak girmedi |
| ses kanalı | ölçülmedi | ③'ün `STATE B` beyanı ölçüm değildir [D137]; 7 planlı replik yokluğu **belgeyle** açıklandı (aşağıda) |
| filigran (köşe testi) | ölçülmedi | ⑤ 12/12 sahnede sağ altta yeşil üçgen bildirdi, ① sustu → 🚨 SUSKUNLUK [D162] — ⬜ kareyle |
| kuyruk kartı (freezedetect) | ölçülmedi | 12/12 rapor 2:00'de kart bildirdi — oybirliği ölçüm değildir [D188 mantığı]; ⬜ |
| LUFS / true peak | ölçülmedi | — |

⛔ Master gelince sıra: `olcum_kapisi.sh <master>` → `sahne_kapisi.sh <master> 10 15` →
`rapor_kontrol.py … --olcum-kesme --olcum-sahne --olcum-sure --olcum-filigran` → kilit
defterindeki 16 madde tek tek kareyle kapatılır.

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 13.09.2026 · **13 rapor**

```
--film yatay_2_dk_filmler/THE_STATIC_SHADOW --hook 10 --klip 10 (ölçüm bayrağı YOK)

🚨 GEÇERSİZ  ① KARE       mod V · SPEC var [D129] · SCORES SUMMARY bölümü YOK — hücre okunamadı
⚠️ ŞARTLI    ② DEVAMLILIK  n=12 Σ=106 → Wear 10/10 kusursuz → `—` [D186] → n=11 ort 8,7
🚨 GEÇERSİZ  ③ SES        SCORES SUMMARY YOK (AUDIT SUMMARY yazmış) — hücre okunamadı
🚨 GEÇERSİZ  ④ HİKAYE     mod V · SPEC var [D129] · SCORES SUMMARY YOK
⚠️ ŞARTLI    ⑤ ARKA PLAN  n=6 ort 7,2 · tally (0,1,4) ≠ etiket (0,1,2) [D161]
⛔ TEKRAR    ⑥ FİZİK      mod V · SPEC var · tally (0,0,2) ≠ etiket (0,0,0)
⛔ TEKRAR    ⑦ AKSİYON    mod V · SPEC var · tally (0,2,3) ≠ etiket (0,2,0)
⛔ TEKRAR    ⑧ EFOR       mod V · SPEC var · tally (3,3,1) ≠ etiket (2,2,0)
🚨 GEÇERSİZ  ⑨ KADRAJ     mod V → karantina [D190] · 5 hücre "no in-scope source"+10 → `—` [D131] → ort 4,0
🚨 GEÇERSİZ  ⑩ OYUNCULUK  mod V → karantina [D190] · süre 60 s ≠ ortanca 124 [D205]
🚨 GEÇERSİZ  ⑪ IŞIK       mod V → karantina [D190]
🚨 GEÇERSİZ  ⑫ HOOK       mod V → karantina [D190] · süre 25 s ≠ ortanca 124 [D205] · tally ≠ etiket
🚨 GEÇERSİZ  ⑬ UYUM       INPUT MODE: MISSING — rubrik doğru durdu; defter boş → koşu YOK

⑤ ÇAPRAZ: kesme 11-12 ✅ (yayılım 1) · 🚨 TESLİM ŞÜPHESİ plan 15 / 9 mercek 12 [D188] ·
          şerit 8 mercek `-111---1-1-1` ✅ · replik 9 mercek 0 ✅ · ⑤ SÜRE sapan ⑩ 60 · ⑫ 25 ·
          🚨 SUSKUNLUK filigran (⑤ dedi, ① sustu) [D162] · filigran ekseni ÖLÇÜLMEDİ [D177]
TOPLAM 13 · 🚨 13 GEÇERSİZ   → RAPOR_KONTROL/RAPORLAR/THE_STATIC_SHADOW_20260913_RAPOR_KONTROL.md
```

**Betiğin yakaladığı yapısal kusurlar:**

```
① ①③④ raporlarında SCORES SUMMARY YOK. _KAYNAK/1_KARE rubriği o bölümü zorunlu kılar
   (satır 1008); ④ ve ③ rubrikleri de. Ya eski rubrik metni yapıştırıldı ya model
   bölümü atladı — hangisi olduğu bilinmiyor, çünkü künyede girdi yolu ve rubrik
   sürümü YOK. Üç çekirdek mercek bu yüzden hücre bile üretmedi.
② SEVERITY TALLY ≠ yazılı etiketler — 13 raporun 7'sinde [D161].
③ ⑨ yedi hücrenin beşine "no in-scope source" yazıp 10/10 verdi → `—` [D131]; kalan tek
   hücre 4/10 (kafiye) — ve o kafiye planın hiç ilan etmediği bir çift (aşağıda ⑩).
④ ⑩ ve ⑫ aynı 12 sahneye 60 s ve 25 s yazdı; ⑫ 25 fps varsaydı. Eski kapı bunu
   görmüyordu → D205, kapı bu koşuda yazıldı ve ikisini yakaladı.
```

---

## §③ KİMLİK KAPISI [D105] — **ATTRIBUTED ✅** (5 metinsiz çapa · 2 sayısal çelişki)

| # | çapa | rapor ne dedi | belge |
|---|---|---|---|
| 1 | görsel | "yellow chevron shoulder straps" (①) · "yellow/black hazard chevron across shoulder pads" (②) | SPEC B: omuzlarda sarı-siyah ikaz şeritleri |
| 2 | görsel | "conical spacecraft capsule" (②) · "white space capsule" (⑤) | SPEC B: mat beyaz seramik pod, sivri titanyum burun |
| 3 | görsel | "octagonal docking ring structure" (⑤ ⑨) | SPEC B: 500 m sekizgen kalkan |
| 4 | görsel | "cylindrical lower module and upper optical telescope assembly" (⑤ S1) | SPEC B: 80 m silindirik teleskop |
| 5 | vuruş | "nose cone contacts metallic docking arm, emitting sparks" (② S6 · 1:00) | plan S07 İlk Başarısızlık: burun rail'den geri teper |
| ✗ | sayısal | ⑥ "capsule-to-station scale ratio (1:6) held" | SPEC C/B: **1/30** → kilit defteri #3 |
| ✗ | sayısal | ② S1 "unhelmeted, bare head" (0:09-0:19) | SPEC B/D197: kask 15/15, vizör opak → kilit defteri #1 |

⛔ Kuyruk kartındaki "THE STATIC SHADOW" yazısı çapa olarak KULLANILMADI (yasak).

---

## §④ KURGU KAPISI — **ÖN KOŞU** · 🔴 **KARAR BLOĞU MAKARADA YOK**

```
a) klip sayısı   12 ≠ 15                          ⛔
b) süre          120 s gövde (+4-5 s kart) ≠ 150 s · Δ = −30 s = 3 klip   ⛔
c) sıra          plan şeridi  -111---1-111--1   (S09 insansız: BOLUM_2 S09 promptu dış hull LED'leri)
                 rapor şeridi -111---1-1-1      (8 mercek birebir)
                 çözünürlük: insansız 7/15 → şerit ÖLÇER [D163]
                 ilk 10 hane BİREBİR → Δ = 0 (0-100 s: plan S01-S10 yerinde)
                 11. hane: plan 1 (S11 OTS) · rapor - (dış çarpma)  → sapma BURADA başlar
d) FİNAL VURUŞ KANITI [D141]   SPEC'te satır YOK (㉔ · D204) → KOŞULAMADI
                 planın kanıtı: gölge hattı teleskopta SABİT + "eller konsoldan inik" (S15)
                 raporlar: "pilot holds joystick" (④ ⑦ S12) → eller KONSOLDA → ⬜ kare 1:55
```

**Δ okuması [D121] — eksik üçü ADIYLA:**

```
rapor S11 (1:40-1:50) dış · burun rail'e çarpar, kıvılcım, ⑨ "dutch low angle WS"
      ↔ plan S13 KARLI HÜCUM (24mm WIDE arka) ya da S14 MOMENT KOLU (35mm MS yan · galling)
        — hangisi olduğu KAREYLE ayrılır (1:41 · 1:45)
rapor S12 (1:50-2:00) OTS · yeşil ışık · uydu pencereden uzaklaşır
      ↔ plan S15 DURGUN GÖLGE (35mm OTS · HELIOS "Shadow lock stabilized")

→ MAKARADA OLMAYAN ÜÇ SAHNE:
   S11  ABORT EMRİ        35mm OTS · HELIOS "Abort" · omuz gerilmesi
   S12  KARAR / KIRILMA   50mm ECU üst · tıklatmasız kapak — CENTRAL CHOICE + TEMA sahnesi
   S13 ya da S14          KARLI HÜCUM / MOMENT KOLU — TEMA + DORUK + TEK KARE sahnesi
   Üçü ARDIŞIK ve filmin KARAR BLOĞU. Planın ÜRETİM SIRASI "S14 → S12 → S15 → S01 → kalanı"
   yazıyordu: ilk iki halka makarada yok, S01-S10 tam → sıra baştan üretilmiş [D168 3. vaka].
   Üretim defteri boş olduğu için hangi klibin ne zaman kabul edildiği BİLİNMİYOR.
```

**⑩ ve ④ bu boşluğu NİYET sandı [D190 · D188]:** ⑩ CHOICE'u S4 joystick'e yazdı (planın
seçimi S12, makarada yok); ④ "filmin sorusu: pilot yanaşmayı atlatacak mı" dedi — planın
sorusu "500 m'lik kalkan neden yalpalıyor, teleskop korunacak mı"; makarada replik olmadığı
için soru hiç sorulmadı (D203).

---

## §⑤ ÇAPRAZ SAYIM KAPISI [D107 · D121 · D135 · D159 · D162 · D205]

```
KESME:   ② 12 · ⑨ 12 · ③⑤⑥⑦⑧⑩⑪⑫ 11 · ① "12 scene cuts" (karta kesme dâhil) → yayılım 1 ✅
SAHNE:   9 mercek 12 · ④ 13 (kartı S13 saydı) · plan 15 → 🚨 TESLİM ŞÜPHESİ [D188]
ŞERİT:   ⑤⑥⑦⑧⑨⑩⑪⑫ `-111---1-1-1` ✅ · ④ şerit basmaz ama haritası S1'i KOKPİT yapıyor
         (11 mercek: dış kalkan) → ④'ün türetilmiş şeridi `1111---1-1-1` 🚨 [D135]; ④'ün
         "S1 ile S2 aynı kadraj, S2'yi kes" bulgusu bu kaymanın ürünüdür → DÜŞER
REPLİK:  9 mercek `none` · plan 7 HELIOS → ⛔ belgeyle çözüldü: promptta replik YOK (D203)
SÜRE:    on mercek 124-125 s · ⑩ 60 s · ⑫ 25 s → ikisinin zaman ekseni 🚨 [D205]
METİN:   ③ ve ⑥ OUT-OF-SCOPE satırı HARFİ HARFİNE aynı ("00:20 & 01:30 — Visor HUD reticle
         static graphic overlay consistency") → 🚨 KOPYA [D159] · aynı oturum [D110 6. vaka]
SUSKUNLUK: ⑤ "sağ altta yeşil üçgen, 12/12 sahne" · sahibi ① Negative Bible kutusu: yalnız
         başlık kartı → 🚨 [D162] — kapı İLK KEZ gerçek bir iddiada ateşledi (D177 öncesi hep
         sıfır iddiaydı). Çözüm köşe testi; o zamana dek ①-10 ve ⑤-9 sayı taşımaz.
```

---

## §② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 16 madde · **1'i BELGEYLE kapandı · 15'i ⬜ AÇIK**

| # | rapor ne dedi (timecode) | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | ② S1 0:09-0:19 kask YOK, kısa koyu saç | SPEC B kask 15/15, vizör opak [D197] · 11 mercek kasklı yazdı | kare 0:12 | ⬜ AÇIK |
| 2 | ⑪ S3 vizör "şeffaf HUD camı", S10 opak | opak aynalı vizör; S03 retikül YANSIMASI planlı | kare 0:25 ↔ 1:35 | ⬜ AÇIK |
| 3 | ⑥ ölçek 1:6 "tutarlı" | SPEC 1/30 (S06 oran karesi) | kare 0:55 | ⬜ AÇIK |
| 4 | ⑥ kalkan dönüşü 1,2-1,5°/s | 0,008 rad/s = 0,46°/s | S01 0 s ↔ 10 s iki kare | ⬜ AÇIK |
| 5 | ③ dış kamerada RCS tıslaması (0:41), ark cızırtısı (1:22), çarpma (1:41) | SPEC C dış kamera MUTLAK SESSİZLİK | ses bandı 0:40-0:50 · 1:40-1:50 | ⬜ AÇIK |
| 6 | 12/12 mercek replik 0 | SPEC A 7 HELIOS repliği | `grep -c '"' BOLUM_*` = 0 | ✅ **PROMPT SAPTI** — replikler prompta hiç girmemiş (D203) |
| 7 | 12/12 kuyrukta 4-5 s başlık kartı, 2:00 | prompt "no title card" 30/30 · kurgu ekran metni 0 | freezedetect + son_kare.jpg | ⬜ AÇIK (D70/72 sayacı ölçümle artar) |
| 8 | ⑤ sağ altta yeşil üçgen filigran 12/12 | "no watermark" 30/30 | köşe testi `kose_SA.png` | ⬜ AÇIK (D150 sayacı ölçümle artar) |
| 9 | ⑤ S8 pencerede ay/gezegen yüzeyi (1:12) | plan derin uzay, gezegen/uydu yok | kare 1:12 | ⬜ AÇIK |
| 10 | ① ⑤ ⑥ ⑦ ⑪ vakumda duman/pus/hacimsel ışın (0:00 · 0:42 · 1:42) | NEGATIVE "no atmospheric smoke/haze" 30/30 | kare 0:42 · 1:42 | ⬜ AÇIK (D36 ailesi) |
| 11 | ① ⑦ havai fişek kıvılcım, kavisli düşen enkaz (1:01 · 1:42) | SPEC C "NO melting metal cliché" · S14 galling parlaması | kare 1:01 · 1:42 | ⬜ AÇIK |
| 12 | ⑥ çarpmada sıfır geri tepme (1:41) ↔ ⑦ "before rebounding" | plan S14 galling + vakum yapışması = PLANLI yapışma; S13 ise hücum | kare 1:41-1:45 (S13 mü S14 mü) | ⬜ AÇIK |
| 13 | ④ ⑦ S12 "pilot holds joystick" (1:55) | plan S15 "eller konsoldan inik" | kare 1:55 | ⬜ AÇIK |
| 14 | ⑪ S8 KIRMIZI alarm, S12 YEŞİL LED | plan S08 AMBER alarm · S15 amber HUD, yeşil yok | kare 1:12 · 1:55 | ⬜ AÇIK (⑪ karantina — ders üretmez) |
| 15 | ⑨ kokpit OTS üç farklı konum (S2 · S8 · S12) | plan S02·S08·S11·S15 TEK kurulum (35mm OTS göz) | kare 0:15 · 1:15 · 1:55 | ⬜ AÇIK (⑨ karantina) |
| 16 | 12 raporun HİÇBİRİ "gölge" olayını yazmadı | S01 TIMELINE: gölge hattı teleskoptan kayar, turuncu ısı parlaması; S15 gölge sabit | kare 0:03 · 0:07 · 1:55 | ⬜ AÇIK (D151 / ADAY-1 ailesi → ADAY-92) |

⛔ **15 madde açıkken ekran bulgularından DERS YAZILMAZ, yeniden üretim siparişi VERİLMEZ.**
Madde 6 belgeden kapandı ve D203 oradan doğdu.

---

## §⑩ ÖNERME KAPISI [D87 · D116 · D130] — planla okunan bulgular

| bulgu | getiren | planda kaynağı | karar |
|---|---|---|---|
| "HUD reticle disappears in S10" | ⑨ ⑪ ① | S03 retikül yansıması · S10 İPTAL KOLU yansıması — İKİ AYRI planlı yansıma | ✅ DÜŞER |
| "RHYME PAIR FAILS — S1 EWS ↔ S12 OTS" | ⑨ | plan kafiyesi S15 ↔ S02/S08/S11 (OTS ailesi); S01 EWS ile kafiye hiç ilan edilmedi | ✅ DÜŞER — ⑨ ekrandan çift uydurdu [D190] |
| "out-of-order: contact → arc → crash" | ② | plan sırası S07 geri tepme → S09 particle event → S13 hücum: PLANLI | ✅ DÜŞER |
| "capsule attached in S5/S8, S10 re-enacts impact" | ② | S05 yanaşma · S07 geri tepme · S13 yeniden hücum: PLANLI | ✅ DÜŞER |
| "zero recoil at impact" | ⑥ | S14 galling + soğuk vakum yapışması = PLANLI | ⚠️ ŞARTLI — rapor S11'in S14 olduğu kareyle kesinleşince düşer |
| "no stakes / no question in first 10 s" | ⑫ ④ | S01 ANOMALİ REVEAL + HELIOS telemetri planlı — ama replik prompta girmedi | ⚠️ AYAKTA, sebebi ÜRETİM değil PROMPT (D203) |
| "S1 ≈ S2, cut S2" | ④ | ④'ün haritası bir sahne kaymış (S1 kokpit değil kalkan) | ✅ DÜŞER [D135] |
| "electrical arcs behave like atmospheric plasma" | ① ⑦ | plan S09 "energetic particle event · ışık parlaması" — ark PLANLI DEĞİL, parlama planlı | ⬜ kare 1:23 |
| "mannequin / nobody pays" | ⑧ ⑩ | plan S10 hızlı nefes · S11 omuz gerilmesi · S13 itki sarsıntısı · S14 tutulan nefes — bedenin ödediği sahneler MAKARADA YOK (S11·S13/S14) | ⚠️ ölçülen makara bedel sahnelerini içermiyor → ADAY-93 |
| ⑥ NOVUM sınır sorusu [D183] | — | SPEC C'de `⛔` sınır cümlesi YOK (㉔) | ⬜ sınır sınanamadı |

⑩ sonrası toplam: **hesaplanmadı** — on üç merceğin on üçü GEÇERSİZ/TEKRAR/karantina; ⑩'un
puan geri verme satırı tabloya girmeyen rapora uygulanmaz. Yalnız kayıt.

---

## §⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108 · D159]

| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| vakumda duman / pus / hacimsel ışın (0:00 · 0:42 · 1:42) | ① ⑤ ⑥ ⑦ ⑪ | ① | ① · ⬜ kare |
| havai fişek kıvılcım (1:01 · 1:42) | ① ⑦ | ① | ① · ⬜ kare |
| kuyruk başlık kartı (2:00) | 12/12 | ① | ① · ⬜ freezedetect |
| sağ alt filigran (0:00-2:00) | yalnız ⑤ | ① (sustu) | 🚨 SUSKUNLUK → köşe testi |
| vizör HUD retikül / yansıma | ① ③ ⑤ ⑥ ⑨ ⑪ | ② | ③ ve ⑥ aynı cümle → KOPYA; ⑨'unki ⑩'da düştü |
| kalkan kenarı: karbon ↔ beyaz seramik doku (0:52 · 1:22) | ① ⑤ ⑦ | ⑤ | ⑤ · ⬜ kare |
| pilot manken / bedel yok | ⑧ ⑩ | ⑩ (karantina) · ⑧ (tekrar) | ADAY-93 |

---

## 📋 FLAGS FOR DOCUMENT CHECK — plandan cevaplar

```
①  duman/kıvılcım stil mi?   HAYIR. RCS = görünür soğuk gaz püskürmesi (S05), "no atmospheric
                             smoke" 30/30; kıvılcım = galling parlaması, "NO melting metal cliché".
①  başlık kartı ihracın parçası mı?   HAYIR. "no title card" 30/30; kapak ayrı dosya, kurguya girmez.
②  kask S1-S2 arası mı takılıyor?     HAYIR. Kask 15/15 kapalı; S1(rapor)=S02(plan) OTS sırttan, kasklı.
⑤  istasyon bir uydunun yörüngesinde mi?   HAYIR. Derin uzay; hiçbir promptta gezegen/uydu yok.
⑤  atmosfer var mı?                   HAYIR. §3.1 vakum; 0% bloom, no haze.
⑥  %100 mikro-yerçekimi mi?           EVET. §3.1 vakum + §3.10 basınçlı iç hacim, 0 g.
⑦  B4 kaza mı, kasıtlı mı?            KASITLI. S12 kararından sonra S13 pilot podu rail'e sürer;
                                       S09'daki "ark" planda energetic particle event (ışık parlaması).
⑦  B2 parçacık: sızıntı mı, gaz mı?   Hiçbiri planlı değil: S07 sessiz geri tepme; gaz yalnız RCS (S05).
⑧  sönümleme teknolojisi mi?          HAYIR. S10 hızlı nefes · S11 omuz gerilmesi · S13 sarsıntı ·
                                       S14 tutulan nefes PLANLI — o sahneler makarada yok.
⑨  S2/S8/S12 ayrı kurulum mu?         HAYIR, tek kurulum (35mm OTS göz) — sapma ⬜ (karantina).
⑨  retikül kapanıyor mu?              EVET, planlı: S03 retikül · S10 İPTAL kolu yansıması.
⑩  panik mi soğukkanlılık mı?         "Sessiz, prosedürel, ekonomik"; S10-S11 ölçülü gerilim.
⑩  vizör yarı şeffaf mı?              HAYIR, %100 opak 15/15 [D197].
⑪  kırmızı alarm yalnız çarpmada mı?  Plan AMBER alarm (S08); kırmızı da yeşil LED de planda yok.
⑫  format · kapak anı · kanca?        16:9 · kapak anı = S14 TEK KARE · kanca = S01 ANOMALİ REVEAL
                                       (HELIOS telemetri — prompta girmedi, ekranda yok).
```

---

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FİLM: 15 sahnenin 12'si teslim edildi; eksik üçü ARDIŞIK ve filmin KARAR BLOĞU
   (S11 abort · S12 merkezî seçim · S13/S14 doruk). Üstüne 7 replik hiç üretilmedi —
   çünkü promptlara hiç yazılmamıştı. Ekrana ulaşan şey: yanaşma, kıvılcım, kart.
   → S11 · S12 · S13/S14 üretimi + replikli prompt + defter + master; sonra 13 mercek MOD D.
2. QA: on üç mercek koştu, on üçü düştü; ⑬ tek doğru davranan mercekti (durdu). Bu partiden
   ekran bilgisi çıkmadı — master yok, 15 madde açık. Belge bilgisi çıktı: üç ders, üç kapı.
3. SİSTEM: D203 (㉓) · D204 (㉔) · D205 (⑤ SÜRE) yazıldı ve betiğe indi; D168 3. vakayla
   ⛔ ÇALIŞMIYOR → üretim defteri §4 KARAR; D129 17 · D188 3 · D190 1 · D110 6.
```

**Sıradaki iş:** master + üretim defteri teslim satırı → ⑪ ölçüm → kilit defteri 15 madde
kareyle → eksik üç sahne üretimi (önce S14, sonra S12 — plan sırası) → repliklerin prompta
yazılması (㉓ BLOCK kapanmadan üretim yok) → SPEC B/C/E doldurulması (㉔) → on üç mercek MOD D.
