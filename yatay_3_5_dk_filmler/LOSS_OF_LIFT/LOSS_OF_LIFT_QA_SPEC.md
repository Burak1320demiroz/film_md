# 📋 LOSS OF LIFT — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **Bu dosya neden ayrı duruyor [DERS 117]:** SPEC bloğu 20.08'de planın içine
> yazıldı ve 21.08'de üç QA koşusunun üçü de onsuz, mod V yapıldı. Blok 906
> satırlık planın 738. satırındaydı — operatörün QA anında eline hiçbir şey
> vermiyordu. Artık SPEC bir BÖLÜM değil, bir DOSYA: rubrikle birlikte
> yapıştırılır ve koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR — önce bunu oku

```
📖 SENARYO_QA   → aşağıdaki A BLOĞU yapıştırılır          MOD D
🔧 VIDEO_QA     → aşağıdaki A + B BLOĞU yapıştırılır       MOD D
🧩 MANTIK_QA    → ⛔ HİÇBİR ŞEY. Baseline filmin kendi iç tutarlılığıdır.
🧍 KARAKTER_QA  → ⛔ HİÇBİR ŞEY. Baseline videodan kurulan pasaporttur.
🔊 SES_QA       → ⛔ HİÇBİR ŞEY. Baseline kurgudan kurulan ses defteridir.

Belgesiz üç mercek için bu dosyanın işi koşudan SONRA başlar: raporun
FLAGS FOR DOCUMENT CHECK soruları C BLOĞU'ndan cevaplanır.
⛔ Her mercek AYRI ve TEMİZ sohbette koşulur [D110] — aynı oturumda ikinci
   rubrik çalıştırılmaz, yoksa parti tek ölçümün kılıflarına dönüşür.
```

---

## 🅰️ A BLOĞU — SENARYO_QA SPEC (rubriğin alan sırasıyla, birebir yapıştır)

```
FILM:                 LOSS OF LIFT
FORMAT:               3-5dk
RUNTIME:              249 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:          25  (S0-S24)
REVIEW INPUT:         video only

LOGLINE (intended):   A lone air-cycle engineer on a sinking balloon station in
                      the Venusian cloud layer finds that his last gas cylinder
                      lifts the station only 70 metres — but exactly fills a
                      small probe that would carry his living culture column
                      above the acid.
THEME (intended):     For something to rise, you have to go down.
INTENDED EMOTION:     calm handover, not rescue — the viewer arrives asking
                      "will it sink?" and leaves asking "what went up?"
ENDING TYPE:          ambiguous (his fate is never shown; the probe's is)

PROTAGONIST:          air / life-cycle engineer, male, 51, unnamed in prompts.
                      Wants: to put the last 600 kg where it still buys height.
                      Fears: that nothing he kept alive leaves the acid.
ANTAGONIST/FORCE:     the envelope leak — 322 kg/h, silent, unstoppable;
                      station sinks 30 m/h. No villain, no machine voice.
CENTRAL CHOICE:       S20 — he throws the manifold lever to the PROBE pipe
                      instead of the envelope feed. Cost lands IN THE SAME
                      SHOT: the feed line goes silent, the needle starts
                      falling again.

DIALOGUE LINES:       1     (S22, over the helmet radio, mouth out of frame)
SILENT SCENES:        24
VIRAL INTERSTITIALS:  S5 · S13 · S19 · S23   ⛔ THESE MAY NOT BE CUT
COVER/THUMBNAIL:      face 60% of frame, eyes on the upper third, looking
                      screen-left at rain curtains that end in mid-air.
                      Promise: "why is the rain stopping in the sky?"
TITLE:                LOSS OF LIFT — the counter is altitude, not power.
LIBRARY CONTEXT:      sibling of LOW POWER (same engine: one person, silent
                      slow unstoppable threat, one number, two colours,
                      handover). Also in library: THE BLUE DRIFT,
                      THE BLACK CRADLE, THE COLD BURN (3-5 dk).
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (kurgu kapısı ve VIDEO_QA için)

```
CLIP COUNT:      25          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      25 · 0 sahne içi kesme · ASL 9.96 s
GRID:            sahne başlangıcı(n) = 9 s + (n−1) × 10 s
RUNTIME:         249 s   (Hook 9 s + 24 × 10 s)
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı YOK
CAMERA:          25/25 sabit lockoff
REPLİK ZAMANI:   S22 → 219 s = 3:39   (±2 s doğrulama noktası [D115])
DORUK:           S20 → 199 s = 3:19-3:29
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

Kurgunun sahne SIRASI bu 25 karakterlik dizeyle doğrulanır. Her QA raporunun
sahne tablosunda "who is present" sütunu vardır; oradan aynı dize yazılır ve
yan yana konur. Tutmuyorsa **sıra bozuk demektir — puanlamadan önce çözülür.**

```
PLAN:  -111111111111-11111-1111-
        │            │     │   └ S24 insansız (final)
        │            │     └──── S20-S23 insanlı (doruk → devretme)
        │            └────────── S19 insansız (viral #3)
        └─────────────────────── S13 insansız (viral #2) · S0 insansız (hook)

insansız 4 sahne: S0 · S13 · S19 · S24   ·   insanlı 21 sahne
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN SORULARINI CEVAPLAYAN KİLİTLER

> Koşu SIRASINDA verilmez. Rapor geldikten sonra `FLAGS FOR DOCUMENT CHECK`
> ve önerme kapısı [D87/D116] bu listeden cevaplanır.

```
İNSAN         tam 1 · 21 sahnede görünür · 4 sahne insansız
KASK          kapalı 7 (S4-S7, S21-S23) · kasksız 14 · ara durum 0 ·
              giyme/çıkarma hareketi 0 kare (geçişler sahne sınırında) [D69]
KOSTÜM        soluk kum-grisi termal tulum + üstünde eski açık gri örgü hırka,
              yakası GENİŞLEMİŞ-AÇIK (tasarım — kostüm hatası değil);
              göğüsteki koyu dikdörtgen BOŞ, hiçbir harf taşımaz
SUIT YIPRANMA tam 3 ağarmış bölge: sağ omuz · sol ön kol · iki diz
YERÇEKİMİ     0.904 g — düşen alet ilk saniyede 4.4 m ("ordinary Earth pace")
YÜZERLİK      nötr — istasyon 30 m/saat sabit hızla iner; "asılı durma" filmin
              ÖNERMESİDİR, hata değil [D59]
IŞIK          güneş diski hiçbir sahnede yok, gölge yumuşak ve her yönden
PİN YAYI      60 cm pirinç çeyrek daire · 24 çentik · çentik = 250 m ·
              rakam ve harf YOK · ibre S0'da 7., S24'te 13. çentikte
              ⭐ S17 = tek YUKARI hareket: +2 çentik, ekranda ~6 s, sonra
                 AYNI çentiğe dönüş. Kalıcı kazanç 0 m. ALARM YOK.
TÜP/MANİFOLD  12 yuva · 11 boş ve sökülü · 1 dolu · 600 kg · tek kol · iki boru
              (S10 ve S20 AYNI SET, eş kadraj 32mm / 4 m)
SONDA         12 m balon · amber fener 4 saniyede 1 nabız · hedef 61-63 km
EKRAN YÖNÜ    yukarı = kaldırma/soğuk/gelecek · aşağı = asit/ısı/şimdi.
              Yükselen üst üçlükten çıkar, batan altta oturur. S24'te
              SONDA YUKARI, KÜRE AŞAĞI — 25 sahnenin 25'inde tersine dönmez.
EŞ KADRAJ     S0↔S24 · S2↔S17 · S3↔S18 · S9↔S16 · S10↔S20 · S12↔S21 · S11↔S23
SES REGISTER  1 replik HUMAN (kask telsizi). MACHINE replik 0 — bu filmde AI yok.
SESSİZLİK     3:19-3:49 müziksiz (doruk + bedel + tek replik) — tasarım [MUZIK]
```
