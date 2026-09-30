# -*- coding: utf-8 -*-
import sys, os, importlib
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from render import CAM_TR, zaman

OUT = "/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_STOLEN_SKY/THE_STOLEN_SKY_PLAN.md"
scenes = []
for b in range(1, 9):
    scenes += importlib.import_module(f"b{b}").SCENES
assert len(scenes) == 96

# iskelet + işaretler
LAST = {}; rows = []; iskelet = []
donus = 0; kume = 0
for s in scenes:
    n, L = s["n"], s["L"]
    if s.get("Z"):
        isa = f"küme S{n-1:02d}"; kume += 1
    elif L in LAST:
        isa = f"dönüş S{LAST[L]:02d}"
        if n - LAST[L] <= 3: donus += 1
    else:
        isa = "ilk"
    LAST[L] = n
    iskelet.append(L)
    vol = s["vol"]; vol_tr = "→".join(vol) if isinstance(vol, tuple) else vol
    ses = (s.get("audio", "") or "").split(",")[0][:48]
    rows.append(f"| S{n:02d} | {s['title']} | {s['vurus'].split(' — ')[0][:34]} · {s['sek']} | {L} · {isa} · {CAM_TR[L]} · IN FRAME: {s['inframe']} | {vol_tr} · {ses} | {zaman(n)} · insan {s.get('humans',0)} · veyra {s.get('veyra',0)} |")

ISK = " ".join(iskelet)
harf_sayisi = len(set(iskelet))

CAM_ROWS = "\n".join(f"{k}  {v}" for k, v in CAM.items())

PLAN = f"""# 🎬 THE_STOLEN_SKY — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.
>
> **Yazıldı:** 20.09.2026 · kaynak: `00_ANALIZ/` (02_KONSEPT · 03_SIRALAMA · 04_UYARI · 05_SAHNE_CALISMALARI) —
> analiz dosyaları KARAR verir, bu dosya kararı ÜRETİME taşır; çelişkide 00_ANALIZ kazanır ve buraya işlenir.
> ⭐ Bölüm dosyalarındaki 96 × 2 prompt bu dosyanın Bible bloklarından ÜRETİLDİ (aynı harf = aynı CAMERA metni,
> aynı hacim = aynı PHYSICS/AUDIO, çekirdek NEGATIVE her promptta birebir) — `00_ANALIZ/05_SAHNE_CALISMALARI/00_96_KLIP_PROMPT_HAZIRLIK.md` olay kaynağıdır.

```
FORMAT:        yatay 16 dk · 96 sahne × 10 s · 8 BÖLÜM × 12 (KILAVUZ_REHBERI §2.8 · 19.09.2026 — bu film kartın ilk referansı)
               ⚠️ QA birimi PART: PART n = BOLUM_{{2n−1}} + BOLUM_{{2n}} (24 klip · 4:00) · 4 PART + TAM-FİLM koşusu — SPEC A `PART GRID` dolu
ORTAM:         §3.3 DÜNYA ATMOSFERİ (tarihli yeniden açılış · 0,9 g · 1,0 atm) + §3.10 iç hacim + §3.1 vakum (S93 · S95) — hacim sütunu sahne haritasında
TÜR:           bilimkurgu · dal: işgal altında tahliye (aksiyon) — §4.3 SAVAŞ kartının KİLİTLERİ ödünç (SAPMA 2), tür kartı açılmadı
MOTOR:         OMNI 1.1 Flash I2V (sahip Q1) · Z klipleri gerçek son kare zinciri · CAMERA `In a single continuous shot.` · tırnak 0
KLİP SÜRESİ:   10,000 s HEDEF · ⬜ ARAÇTAN ÖLÇÜLDÜ [D124]: ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
               kurgu birimi 240 kare @24 fps (sahip Q3) · KIRPMA satırı SPEC A · kurgu kapısı 960,000 s ±0
SAHNE SAYISI:  96        RUNTIME: 960,000 s = 0 + 96 × 10,000 s (hook = S00, ayrı sahne değil)
LOGLINE:       Kara deliğe yakın bir kolonide göğü kapatan işgalciye karşı dört kişilik ekip tek kuleyi ele geçirir ve tek rezervi intikam yerine altmış saniyelik bir koridora harcar.
```

---

## 🎭 TEMA

```
TEMA: SORUMLULUK (aday etiket — TEMA_MUHENDISLIGI §3b'ye tarihli satır FAZ 6'da; GÜVEN emsali)
      — "Gücü eline alan, onu kime borçlu olduğunu da seçer."   (TANIM cümlesi; TAKAS kalıbı değil [§3c])

MOTİF SAHNELERİ: S18 · S59 · S81 · S84 · S94
      NESNE: kemer kayışı (S18 Bor sıkar → S94 Mara kapatır) + rezerv seçici kolu (S16 ikon · S67 fiziksel · S81 · S84)
      KİNESİK: el durur (S81) → tek kararlı çeviriş (S84) → el kemerde kalır (S94)
      KAMERA+IŞIK: C-0 hedef ikonu kehribar canlı (S69 · S81) → söner, koridor ikonu yanar (S84) — iki çıkış aynı kadrajda
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Yörünge Kafesi — gökyüzünün üst katmanındaki kehribar örgü kalkışı ve sıçramayı keser; altında alçak uçuş serbest;
                     hasar gören düğümü komşu kuleler saniyeler içinde kapatır; tek kule kontrol altındayken aynı alan 60 s boyunca
                     TERS çevrilip iki gemi eninde dar bir koridor açar. (kalkan · geçit · işaretleyici aynı ailenin türevleri — ikinci ihlal değil)
NOVUM TAŞIYICISI:    KEHRİBAR ÖRGÜ (lattice) × insan gemisinin kalkışı → burun örgüye değince yana savrulur, düşer (S00)
                     SEÇİM TAŞIYICISI: REZERV SEÇİCİ KOLU (T-handle) × Mara'nın eldiveni → iki çıkış (kısa kalın boru = darbe · uzun ince boru = koridor), tek depo (S16 · S67 · S81 · S84)
TEK KARE (§4①):      ✅ S00 · 0,0 s — insan gemisinin burnu KEHRİBAR ÖRGÜYE (lattice) değmiş, gövde yana savrulmak üzere; aynı karede örgü + gemi + siperde Mara.
                     Taşıyıcı nesnenin adı cümlede: "its nose touching the lowest amber line" [D157]. S00'da ikinci olay yok.
KİNETİK BAĞIMSIZLIK: ✅ savrulma (S00) · örgünün kapanması (S13) · kalkan sapması (S01 · S22) · örgüde açılan bant (S87) · kapanış (S93) — replik/metin yok
BAŞLIK ŞEMASI:       ✅ "The Stolen Sky" / "Çalınan Gökyüzü" — 3 kelime, izleyici göğe bakar
KURAL TEKRARI (§5):  KURULUM S00 · DOĞRULAMA S13 (farklı nesne) · S25–S26 (aynı aile) · SONUÇ S87–S93 → ≥3 sahne · ≥2 nesne ✅
NOVUM KİLİDİ SAYIYLA: örgü çizgileri iki gemi enini geçmeyen aralık · koridor "two ship-widths wide" (S87) → "one and a half" (S92) → "one" · S13 kapanma ≤2 s · S87 açıklık İLK KAREDE · S93 kapanma ilk 3 s
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   İki tahliye gemisini (E-1 · E-2) kafesin dışına çıkarmak — film başlamadan var olan İŞ (hangarda yükleniyorlar, S05)
   □ ENGEL:   Yörünge Kafesi + yönlü kalkanlar + komşu kulelerin yedeklemesi (S13) + Serrak'ın uyarlanması (S40 sırt sırta · S48 örtüşen kalkan · S64 anahtar iptali · S56/S73 yeni işaretleyici)
   □ BEDEL:   Bor kulede ölür · S59 ⭐ + Mara C-0'a saldırı fırsatından VAZGEÇER · S84 (Serrak hayatta, koloni geride · S95)
              + K-1 kalıcı hasar S29 · S66 · S90 — bedel bedende: S58 el boşta · S61 sıkılı yumruk · S94 kemer
   □ MUHATAP: Serrak (her insan hamlesine karşı hamle: S09 · S44 · S60 · S70) + Bor (S58 "git" — istek çaprazı) + K-1'in sağ bileziği (ortamın kalıcı değişen parçası)
   □ AYRILIK: S58 — Mara Bor'un KALDIRACA GELMESİNİ ister (kolu çeker), Bor Mara'nın GİTMESİNİ ister (kolu çeker, son mermileriyle geri iter); nesne: Bor'un sol manşeti (B5b)
              ikincil ayrılık S53/S55 (Rey aşağı, Mara/Ada yukarı — anlaşmalı)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  0 REFERANS PAKETİ taslak (6 sayfa) [KAPI 0] → 1 DENEMELER P1 S48 · P2 S01 · P3 S02 · P4 S68 · P5 S90 · P6 S59+S38 → 2 ANİMATİK 96 kare →
  3 DORUK/SEÇİM S84 → S92 → S94 · S95 → S00 → BEDEL S59 → 4 sınır çiftleri S23/S24 · S47/S48 · S71/S72 →
  5 BOLUM_8 → BOLUM_1 → BOLUM_5 → BOLUM_7 → BOLUM_6 → BOLUM_2 → BOLUM_3 → BOLUM_4 (Z klipleri kaynağıyla aynı oturumda)
İPTAL KAPISI: S84 (kol + ikon tek kadrajda okunmuyorsa) · S59 (üç işaret 10 s'de okunmuyorsa) · S22 (kalkan yönü profilde okunmuyorsa) · S00 (örgü+gemi+savrulma tek karede okunmuyorsa) → film ÜRETİLMEZ · P1 (S48) okunmuyorsa S48 sadeleştirilir, ikinci figür SİLİNMEZ
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
— yatay film; bu blok uygulanmaz. Bilgi asimetrisi yine de yazılı: DRAMATİK İRONİ — taşıyıcı Serrak'ın planları (S09 · S44 · S70), izleyici düşman hamlesini ekipten önce görür.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | %0 | S00 gemi örgüye çarpar | — |
| 2 | Kurulum | %0–10 | S00–S08 | — |
| 3 | Katalizör | %11 | S11 «Kuleyi alacağız.» | — |
| 4 | Tartışma / kural | %14–20 | S14–S18 | — |
| 5 | İlk küçük zafer | %23 | S22 açık yan | — |
| 6 | Bedel 1 (araç) | %30 | S29 sağ bilezik | — |
| 7 | Orta nokta (sahte zafer) | %49 | S47 platform + pusu | — |
| 8 | Umut-önce-düşüş | %52–58 | S50 · S52 | — |
| 9 | Her şeyin kaybı | %62 | S59 Bor | — |
| 10 | Güç el değiştirir | %66–70 | S63–S67 | — |
| 11 | İntikam hazır | %72 | S69 | — |
| 12 | Karar penceresi | %84–87 | S81–S83 | — |
| 13 | Merkezî seçim | %88 | S84 «Koridoru aç.» | — |
| 14 | Doruk (fiziksel) | %91–97 | S87–S92 | — |
| 15 | Çözülme | %98 | S94 boş koltuk | — |
| 16 | Kapanış imajı | %100 | S95 üç ışık | — |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       in medias res — bir insan gemisi görünmez tavana çarpar
S0 SORUSU:       "Gök neden geçilmez?" (0:00–0:10)
S1 İKİNCİ BİLGİ: insan ateşi de işe yaramaz (S01 kalkan sapması) → soru "nasıl kaçacaklar?"a döner; S02 düşman arkadan da çıkar
İLK 2 SN SESİ:   motor tırmanışı + uzak namlu (diegetik, müzik yok)
AÇILIŞ↔KAPANIŞ:  KAFİYE S00 ↔ S95 — aynı harf A, aynı CAMERA cümlesi; değişen: örgüye ÇARPAN 1 gemi ↔ örgünün DIŞINDA 3 gemi
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi taşır (`KARAKTER_VE_DUYGU §6` · `KURGU_RITMI §2` örüntü kırıcı — ardışık iki sahne aynı kademe + palet + ses dokusunda değil, 0 ihlal; ölçüm `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §2–§3).
> Kurulum sütunu bölüm dosyalarındaki başlık bloğuyla BİREBİR (aynı üreteçten). Olay ayrıntısı: `00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md`.

| S | başlık | olay / vuruş · sekans | kurulum (harf · işaret · lens · ölçek · açı · IN FRAME) | hacim · ses | zaman · kadro |
|---|---|---|---|---|---|
{chr(10).join(rows)}

```
AÇI TİPİ SAYISI: 6 ≥3   (low angle · eye level · high angle · over-the-shoulder · from below/behind · profile — KAMERA_ACISI §2)
KURULUM SAYISI:  {harf_sayisi} (ACI_YAYI §4 bandı ≤48 ✅ · bölüm başına ≤12: dosya düzeyi "üst bant 6" notu 96 sahnelik filmde beklenir [D74])
KURULUM İSKELETİ: {ISK}
                 KÜME (Z): {kume} klip — S13 S35 S37 S41 S48 S49 S72 S74 S82 S90 (9 küme, tavan 3 klip ✅)
                 DÖNÜŞ: 36 / 96 = %37,5 (prompt_kontrol ⑩④ ölçümü · kaynağından ≤3 sahne sonra gelen tekrar; hedef 39)  ⛔ hedef ≥%40 — D74 SAPMA (UYGULANMAYAN KİLİTLER'e bak)
                 ⛔ Aynı harf AYNI kurulumdur: CAMERA metni Camera Bible'dan birebir; dönüş → "— the same position, height and lens as Scene N."
                   küme → "continues the previous clip from its exact last frame — the same position, height and lens as Scene N." (N = S+1)
BÖLÜM KESİĞİ:    S11|S12 · S23|S24 (PART) · S35|S36 · S47|S48 (PART · Z) · S59|S60 (bilinçli şok) · S71|S72 (PART · Z) · S83|S84 — hepsi ardışık çift denetiminde ✅
BİLİNÇLİ ŞOK:    2 — S59→S60 (kaldıraç içi → C-0) · S93→S94 (vakum geniş → kabin)
```

---

## 🎙️ REPLİK TABLOSU (8 replik · POST-DUB · promptta 0 · SPEC A `DIALOGUE LINES: 0 · POST-DUB LINES: 8`)

| # | S | saniye | konuşan | REGISTER | kanal | İŞLEV (B5 satırı / vuruş) | DEĞİŞ-TOKUŞ (hamle → cevap · DEĞİŞİM) |
|---|---|---|---|---|---|---|---|
| 1 | S10 | 104,0 | tahliye kaptanı | H · telsiz | kadraj dışı — dinleyen Mara | ENGEL: kafes içinde sıçrama yok | bilgi → S11 eylem (6 s) · NİYET: kule |
| 2 | S11 | 117,0 | Mara | H · kask içi | konuşan (opak, ağız yok) | KARAR: kuleyi alacağız | emir → üçü rampaya (1 s) · GÜÇ: Mara |
| 3 | S14 | 145,0 | Ada | H · kask içi | konuşan | ENGEL→İSTEK: yıkmak işe yaramaz | teklif → Mara baş sallar (2 s) · NİYET: rezerv |
| 4 | S53 | 533,0 | Rey | H · telsiz | konuşan | İSTEK (Rey): botu çatıya | teklif → S54 koordinat (0–1 s) · MESAFE ↑ |
| 5 | S58 | 583,5 | Bor | H · kask içi, zorlanmış | konuşan | AYRILIK: git | ret+emir → Mara'nın eli boşta (1 s) · GÜÇ: Bor |
| 6 | S67 | 674,0 | Ada | H · kask içi | konuşan | 🔶 D217: iki çıkış KADRAJDA — öneri «Bir kez. Sonra biter.» / sil — SAHİP KARARI | uyarı → Mara durur (2 s) · BİLGİ: tek kullanım |
| 7 | S82 | 821,0 | tahliye kaptanı | H · telsiz | kadraj dışı — dinleyen Mara | MUHATAP: iki gemi hazır, seni bekliyoruz | çağrı → S84 eylem (2 klip) · NİYET: intikam → tahliye |
| 8 | S84 | 841,5 | Mara | H · kask içi | konuşan | KARAR: koridoru aç | emir → S85 Ada tetikler (0–1 s) · GÜÇ: rezerv tahliyeye |

```
İLK REPLİK:     S10 · 104,0 s · öncesindeki kesintisiz sessizlik 104,0 s · vuruş: "kaçış hattı yok"
BEDENLEŞTİRME:  □ yok — bütün replikler AKUZMATİK (opak vizör, ağız 0 kare; tasarım, kısıt değil)
⛔ saniyeler HESAPLATILDI: replik(S_n) = 0 + n × 10,000 + TIMELINE ofseti [D122] · <5 s · tek konuşmacı [D35] · duygu adlandırılmaz
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md — beklenen sonuç "NO DIALOGUE FOUND" (kapsam sınırı; post-dub tablosu SPEC A'da)
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız o karenin `IN FRAME:` satırındaki kısmı gider
> (14.09.2026 · D214 · ㉖). "BIBLE'a bak" atfı YASAK; self-contained ≠ Bible'ın tamamı. Videoya Bible girmez — `START FRAME:` tek satır.
> ⭐ Bu bloklar `00_ANALIZ/06_PROMPT_URETECI/common.py` üreteciyle bölüm dosyalarına BİREBİR kopyalandı — Bible değişirse 96 prompt yeniden üretilir, elle düzeltilmez.

### 👤 Character Bible — dört insan (opak vizör · SAPMA 3 · ⭐VİRAL YÜZ satırı yok)
```
HELMET (dördü aynı):  {PANE}
  çoğul biçimi:       {PANES}
  ⛔ D79 vizör cümlesi ("optically clear / zero tint / fully readable") HİÇBİR promptta YAZILMAZ — tasarım opak; dosya düzeyi D79 bulgusu bu filmde DÜŞER.
MARA  full:  {CH['MARA']['full']}
      short: {CH['MARA']['short']}
      torso: {CH['MARA']['torso']}
      hands: {CH['MARA']['hands']}
      back:  {CH['MARA']['back']}
      YIPRANMA (S03+, göğüs kadrajdaysa): {CH['MARA']['scar']}
REY   full:  {CH['REY']['full']}
      short: {CH['REY']['short']}
      torso: {CH['REY']['torso']}
      hands: {CH['REY']['hands']}
      back:  {CH['REY']['back']}
ADA   full:  {CH['ADA']['full']}
      short: {CH['ADA']['short']}
      torso: {CH['ADA']['torso']}
      hands: {CH['ADA']['hands']}
      back:  {CH['ADA']['back']}
BOR   full:  {CH['BOR']['full']}
      short: {CH['BOR']['short']}
      torso: {CH['BOR']['torso']}
      hands: {CH['BOR']['hands']}
      back:  {CH['BOR']['back']}
      YIPRANMA (S51+): {CH['BOR']['limp']}   ·   (S57+): {CH['BOR']['empty']}   ·   S60'tan sonra 0 kare / 0 ses
KONUM KİLİDİ: iki-figürlü kadrajda MARA SOL · BOR SAĞ (S18'den S58'e); kabin koltukları S30'da sabit: Rey ön-sol · Ada ön-sağ · Mara arka-sol · Bor arka-sağ (S94 boş koltuk = arka-sağ)
KİMLİK YIĞINI: kişi başına ≤3 öznitelik (renk · işaret · ekipman); boy · ten · saç · yaş · yüz YOK [⑲ · D167]
```

### 👽 Creature Bible — Veyra (tek ANATOMY LOCK · SAPMA 1: kadrajda ≤3 · ırk adı prompta girmez)
```
ASKER (kalkanlı):  {VEYRA}
ASKER (kalkansız): {VEYRA_NOSHIELD}
KISA (çoklu kadraj): {VEYRA_S}
SERRAK:            {SERRAK}
KALİBRASYON SUBAYI (S38–S39): {OFFICER}
ÜÇ ŞEKİL (aynı ışık efekti üçü için kullanılmaz):
  KALKAN = öne bakan kavis ("convex face forward/to X") · PORTAL = {PORTAL_OPEN} · KAFES = {LATTICE}
KALKAN SAPMASI (1 numaralı risk, sayıyla · her tekrarında aynı cümle ailesi): four bright points meet the shield face-on and glance off to the side in under half a second, striking … two figure-lengths from the figure; the shield keeps its curve and its side to the shooter; no glow lingers.
ÖLÜM/DÜŞÜŞ NÖTR: "a hard impact light spreads on the ceramic and fades within half a second; the figure folds and goes down as one piece" — kan · yara · ceset · silah adı 0
```

### 🚀 Vehicle Bible — beş araç + drone (oran referans paketi ③④⑤'te; promptta gövde/araç boyu ölçüsü)
```
K-1:  {K1}
      DURUM MERDİVENİ (tek yönlü): K0 sağlam (S00–S28) → K1 {K1_BENT} (S29–S65) → K2 {K1_CLAMP} (S66+) → K3 + {K1_STUB} (S90+)
      SAPMA YÖNÜ: her uçuşta SAĞA eğik (S30 · S68 · S77 · S78 · S86 · S90–S93) — "leaning right"
E-1:  {E1}          E-2: {E2} · S89'dan: {E2_DMG}
C-0:  {C0}          AVCI: {FIGHTER}          DRONE: {DRONE}
YÖNELİM KİLİDİ: her araç geçişinde "nose pointing …" (uzamsal kılavuz §5.1 soru ①)
```

### 🌍 World Bible — NEREV-4 (DÜNYA ÇAPASI 3 cümle [D209] · yön NESNE-GÖRELİ [D174])
```
① {WORLD}; the human structures are squared and worn, the Veyra surfaces smooth and curved.
② {LATTICE}, and {RING} — two different shapes that never blend; the lattice is the nearer one.
③ Shadow direction is away from the ring; the lattice throws no shadow of its own.
KUŞBAKIŞI HARİTA (PLAN kararı · 03 §0.3): yeraltı hangar (E-1 · E-2 · K-1) — uçuş koridoru (boru hatları · servis hendeği) — T3 kulesi;
  T3 tabanında çatılı kuru servis havuzu · havuzdan servis koridoruyla geçiş istasyonu · T3 platformu → kaldıraç → rezerv odası → manuel bakım kapağı → ÇATI.
  Halka T3'ün ÜSTÜNDE (kamera kuleye bakıyorsa üst-orta), koridor halkaya DOĞRU açılır. ⛔ Pusula kelimesi ve ekran koordinatı promptta yok.
HACİMLER: YÜZEY (siper · uçuş koridoru · çatı · gök) · İÇ (hangar · kanal · havuz · koridor · istasyon · platform · rezerv odası) · KABİN (yerde/uçuşta) ·
          KABİN 0 g (yalnız S94) · C-0 (Veyra iç) · VAKUM (S93 · S95) — geçişli klipler: S03 S23 S31 S45 S60 S68 S79 S88 S92
```

### 🎥 Camera Bible — 20 harf, aynı harf = aynı metin BİREBİR (ACI_YAYI §7 ⑥ · her satırda lens · yükseklik · mesafe · açı tipi imzası)
```
{CAM_ROWS}
dönüş satırı → "— the same position, height and lens as Scene N."      (N = S + 1)
küme satırı  → "continues the previous clip from its exact last frame — the same position, height and lens as Scene N."
her CAMERA satırı "In a single continuous shot." ile biter (OMNI katmanı)
```

### 💡 Lighting Bible (IŞIK TAKVİMİ mekân başına [D193 · D201] · IŞIK bloğu yüzeye renk atmaz [D176])
```
YÜZEY:     one hard amber key from the ring (above the tower), cold sky fill, shadows soft but deep · kamera ringin tersine bakıyorsa key arkadan, uzun öne düşen gölge (S02)
HANGAR:    cold blue-white work lamps + amber bars from the roof slots (S05 · S08 · S19 · S80) · dış kapak kapanınca amber kesilir (S08 tek adımda)
KABİN:     cold blue-white ceiling lamps; kabin uçuştayken cam üstünden amber şerit; uyarı lambası tek, metinsiz
İÇ (T3):   cold conduit/plate lamps + rezerv deposunun kehribar slotları; gözlem yarığından amber iplik (S61 · S69 · S81 · S84)
C-0:       low amber from the hull surfaces, no cold source
VAKUM:     ring key as one hard rim, shadows absolute black with razor edges (S93 · S95)
SON 3 s IŞIK OLAYLARI (planlı sınırlar): S08 kapak · S12/S13 hücre · S21/S43/S57/S74 portal · S59 göğüs lambası · S84 iki lamba · S87/S93 bant
```

### ⚙️ Physics Bible — her promptta AYNI sayı (§5.1b · sahip Q2)
```
YÜZEY/İÇ:  {PHYS['YUZEY']}
KABİN:     {PHYS['KABIN']}
KABİN 0 g: {PHYS['KABIN0G']}
C-0:       {PHYS['C0']}
VAKUM:     {PHYS['VAKUM']}
AUDIO:     YÜZEY "{AUD['YUZEY']}" · İÇ "{AUD['IC']}" · KABİN "{AUD['KABIN']}" · C-0 "{AUD['C0']}" · VAKUM "{AUD['VAKUM']}" — hepsi "No dialogue. No music." ile biter
PARÇACIK:  0,9 g — sparks and fragments fall straight down and settle within two seconds; smoke → "haze" (politika sözlüğü); vakumda fragman düz çizgi + kendi ekseni
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.1 çekirdek (bu filmin kapsam satırıyla) + havuz
```
ÇEKİRDEK (video 8 · image 7 — ① yalnız video):
① {N_TAKE}
② Exactly N human character(s) in suit(s) [+ and exactly N tall figure(s) with two arms, two legs and one head], no duplicates, no extra person.
③ {N_BLOOM}
④ {N_TEXT}
⑤ {N_GRAIN}
⑥ {N_GEAR}
⑦ {N_HAND}
⑧ {N_PART}
İNSANSIZ KISA ÇEKİRDEK (<900 karakter · KART 10): "Human count zero in this frame, the empty deck and sky are the subject." + ③ + kısa ④ + ⑤ + ⑥ + ⑧ (+ ≤1 sahneye özel)
SAHNEYE ÖZEL ≤2 (fiilî tavan: betik kapanış çitini cümle sayıyor → 8 + 2 = 10): havuz —
  kalkan: the shield never opens, spreads or changes colour · the points touch only the shield and the plating
  portal: hard bounded edge between two points, not a glow and not a beam · one gate, one drone
  kafes/halka: two different shapes that never blend · the gap is a straight band with hard edges, never a hole
  hasar: the ring only bends, the engine does not stop, nothing explodes · the clamp holds, nothing is straightened
  politika: the impact light lives on the ceramic surface only, nothing spills · no mouth, no invented on-screen speaker
  sayı: exactly two fighters · exactly three tall figures · exactly four seats and three occupants
⛔ NEGATIVE'e şiddet sözlüğü YAZILMAZ (blood · corpse · gore · weapon — KART 12 · D123); "no human figures" kalıbı YAZILMAZ (KART 10)
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| kalkan sapması süresi | ≤0,5 s · 4 nokta · 2 figür boyu | KART 9 · A5 | S01 S07 S20 S26 S36 S37 S40 S48 S72 |
| Bor'un ölümü üç işaret | alet düşer 2,5 s · gövde kayar 2,5 s · ışık söner 5,5 s | KART 12 | S59 |
| koridor eni | 2 gemi eni (S87) → 1,5 (S92) → 1 (S93 kapanış ≤3 s) | KART 5 · novum | S87 S92 S93 |
| örgü kapanması | ≤2 s, iki komşu kuleden | KART 6b | S13 |
| kadrajdaki Veyra sayısı | ≤3 (2 muhafız + Serrak) | KART 2 · SAPMA 1 | S47 S48 S49 |
| kadrajdaki insan sayısı | sahne başına rakam 0–4 (harita sütunu) | KART 4 | 96/96 |
| sivil figür | ≤3 hangarda, kalabalık 0 | KART 4 | S05 S80 |
| K-1 sapma | her uçuşta sağa, düzeltme 3 jet | KART 13 | S30 S68 S78 |
| ana nesne | ≥100 px (tablo OPTİK sütunu, 5 düzeltme) | D179 | 96/96 |
| koltuk | 4 koltuk · 3 dolu · 1 kemer kliği | D141 · KART 4 | S94 |
| kapanış | 3 gemi tek karede | D141 · D210 | S95 |
| replik | 8 post-dub · promptta 0 · saniye formülle | KART 7 · D122 | tablo |
| klip süresi | 240 kare @24 fps · kurgu 960,000 s ±0 | KART 11 · D124 | SPEC A |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D192 | 1 numaralı risk (kalkan sapması) sayıyla yazılır: 4 nokta · ≤0,5 s · 2 figür boyu · artık ışık 0 | Creature Bible · S01 vid_lock · A5 |
| D174 | yön nesne-göreli; pusula ve ekran koordinatı prompta girmez | üreteç PUS/TOWARD denetimi · World Bible |
| D179 | imaj = 0,0 s başlangıç durumu; sonuç ilk karede yazılmaz | img_lock "not yet" cümleleri (S02 S19 S33 S40 S46 S48 S62 S87 S93) |
| D213 | temas · değişim · sonuç aynı klip, temas ilk 2 s | S03 S28 S29 S51 S59 S74 S84 TIMELINE |
| D206 (+169 · 175) | efor eldiven üstünde: forearm tightening · shoulders dropping · rear boot loading; mühür tek cümle | S18 S41 S49 S51 S58 S63 S79 |
| D207 | yorgunluk 0–6 kanalı: topallama S51+ · nefes daralması S59/S61 | Bor limp satırı · AUDIO |
| D202 | ÇAPA ÜÇLÜSÜ: CHOICE S81/S84 · FINAL S94 · BEFORE/AFTER tek nesne | T-handle · kemer |
| D209 | DÜNYA ÇAPASI 3 cümle her ortam promptunda | World Bible ①②③ |
| D208 (+42) | KİMLİK DİZİSİ + YIPRANMA takvimi (Mara izi S03+ · Bor diz S51+ · K-1 merdiveni) | Character/Vehicle Bible |
| D210 (+62 · 141) | kafiye A↔A (S00↔S95) · FİNAL VURUŞ KANITI: kemer 1 klik · 3 gemi tek kare | S94 S95 |
| D193 (+201) | ışık takvimi mekân başına; ışık olayı klip içinde planlı sınır | Lighting Bible · S08 |
| D200 (+198) | fizik sayıyla (0,9 g · 2 s çökme); 0 g yalnız S94 tek serbest nesne | Physics Bible |
| D138 (+34 · 215) | ekranlar ikon/çizgi, harf-rakam 0; ad değil kod (kule/bot adı prompta girmez) | S06 S14 S16 S43 S70 S82 |
| D214 (+146 · 139) | IN FRAME'e göre parça; sırt POZİTİF yüzey OTS/arkadan her promptta | back_of satırı (video) · Bible back |
| D157 (+172 · 78) | TEK KARE cümlesi taşıyıcı adıyla; drone yolu görünür; kural tekrarı ≥3 sahne | S00 · S02 S19 S56 S73 · novum bloğu |
| D211 (+212) | hareket enerjisi yüksek sahnelerde YÜZ satırı yok (opak); jest gövdeyle | S10 S61 S81 S82 |
| D203 (+217 · 216 · 180) | replik akuzmatik, sayısı formülle; replik göründüğünü söylemez (S67 🔶) | Replik tablosu |
| D167 (+KART 12) | silah adlandırılmaz; kan/yara/ceset 0; NEGATIVE'de sözlük 0; kimlik ≤3 öznitelik | üreteç POL denetimi |
| D1 (+70 · 45) | tek çekim her video; küme/dönüş işareti; [LESSON] etiketi gövdeye girmez | CAMERA satırı |
| D176 (+KART 9) | IŞIK bloğu yüzeye renk atmaz; tek baskın ışığa karşı dört kanal | LIGHT satırları (üreteç denetimi) |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle

| ders | neden bu filmde uygulanmadı |
|---|---|
| ACI_YAYI §4b DÖNÜŞ ≥%40 | 36/96 = %37,5 (prompt_kontrol ölçümü; 03 §4 DP hesabı 32 idi, betik küme kaynaklarını da sayıyor) — sahibin 24 sekanslık yapısı (her sekans yeni mekân/hedef, sekans içi kesmeler bakış açısı değişimi); 96 sahnenin izinli kurulumları ve bant kısıtı altında en iyi atama 32 (DP taraması, 03 §4). Süreklilik 10 KÜME (gerçek son kare) ile kuruluyor; yeniden sıralama onaylı hikâyeyi bozar [D74] |
| D79 (vizör optik berrak · REFERANS §4 opak yasağı) | sahip talebi "yüzler bütün film boyunca kapalı" — SAPMA 3; emsal THE_FALLING_WORLD; dosya düzeyi D79 bulgusu bu filmde düşer, ⭐VİRAL etiketi kullanılmaz |
| D124 ızgara ±2 s | sahip "tam 10 s" — ham araçtan ölçülür, kurgu birimi 240 kare (SAPMA 5) |
| §4.3 SAVAŞ kartı (rafta) | tür kartı açılmadı; yalnız kilitleri ödünç (SAPMA 2) |
| UZAYLI_VARLIK ① tek varlık · uzay operası yasağı | Veyra ordusu tek ANATOMY LOCK + kadrajda ≤3 (SAPMA 1); kılavuza tarihli istisna notu FAZ 6 |
| D69 biniş/iniş 0 kez | S23 · S32 · S86 hareketin ortasından, D69 ① gereği (SAPMA 9) |
| 03 §7 "kurulum sayısı üst bant 6 / 12 sahne" | bölüm dosyası başına 8–9 harf; 96 sahnelik filmde 20 kurulum bandın içinde (≤48), dosya düzeyi not kabul [D74] |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S59 (Bor'un ölümü) — ikinci S38, üçüncü S51, dördüncü S58, beşinci S48
NÖTR TARİFİ:         Seen through a fine metal mesh in the foreground, a broad grey-suited figure leans against a cargo crate on a wide metal platform; a tall
                     pale-ceramic figure stands three figure-lengths beyond him with one arm raised. A single brief flash at the end of the raised arm. The broad
                     figure's torso slides down the side of the crate and the long dark tool slips from his gloves to the deck; the small lamp on his chest goes
                     dark. The lift cage rises and the platform drops out of frame.   (= S59 vid_lock; kan 0 · yara 0 · ceset 0 · silah adı 0)
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| isabet anı ve yara kadrajda değil; kan/ceset/silah kelimeleri prompta girmez (S59 · S38 · S51) | ölümün görsel kesinliği tek kareden değil üç işaretten okunur (0,5 s gecikme) | alet tepkisi (durum ışığı söner · alet düşer) + malzeme sonucu (zırh darbe ışığı) + temassız gövde (S58 boş el · S61 yumruk) + S60'tan itibaren Bor'un kanalı sessiz |
| silahlar "short tool / long tool", ateş "bright points" | tür sözlüğünün keskinliği | kütle-hız: sapan noktaların mesafesi ve süresi sayıyla; siper/duvar parçalanması |
| Veyra ırk adı ve T3/K-1/NEREV-4 adları prompta girmez | — | kod/tarifle kimlik (tall pale-ceramic figure · the boat · the tower) |

```
RESMÎ KURAL KAYNAĞI: ⬜ OMNI politika sayfası URL + tarih (FAZ 3'te aranır; bulunamazsa "resmî kaynak yok" yazılır) · DENEME KAYDI: P6 (S59 + S38) → URETIM_DEFTERI §0b
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
```

---

## 📌 SAPMA DEFTERİ (02_KONSEPT §1 + 03 §8 — PLAN'a taşınan)

```
1 Veyra ordusu → tek ANATOMY LOCK, kadrajda ≤3 · 2 savaş kilitleri ödünç · 3 opak vizör (D79 düşer) · 4 §3.3 yeniden açılış 0,9 g · 1 atm ·
5 tam 10 s (240 kare) · 6 replik 10 → 8 (S06 · S83 görsel) + S67 🔶 · 7 S64 tek mekân · 8 SEK01–24 / S00–S95 · 9 biniş/iniş ortadan ·
10 DÖNÜŞ %37,5 · 11 ⭐VİRAL 0 · 12 TARGET ASL 10,0 s sabit · 13 çizelge "— (not)" hücreleri salt "—" (㉘) · 14 hikâye onayı üç fiil eş anlamlısı (㉙ jargon)
```
"""
with open(OUT, "w", encoding="utf-8") as f:
    f.write(PLAN)
print("PLAN yazıldı", len(PLAN)//1024, "KB · iskelet", len(iskelet), "harf ·", harf_sayisi, "kurulum · dönüş", donus, "· küme", kume)
