# 🧷 THE_STOLEN_SKY — REFERANS PAKETİ (TASLAK · 20.09.2026)

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 · sayfa §4 · kullanım §5 · kapı §6 · döngü §7) ·
giysi kimliği `ASTRONOT_DONANIM` · varlık `UZAYLI_VARLIK` §4 · ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya → kabul kapısı → seed kilidi → denemeler P1–P6 →
> DORUK S84 → S92 → S94/S95 → S00 → S59 → gerisi [D168]. ⛔ Referans kareler KURGUYA GİRMEZ.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR (opak düz panel vizör · Veyra kalkan kavisi · portal halkası).
> ⭐ **SAPMA 3 (opak vizör):** bu pakette "vizör-ardı yüz CU" sayfası YOKTUR; D79 optik-berrak cümlesi hiçbir sayfada yazılmaz.
> ⭐ Her sayfanın kimlik cümleleri `THE_STOLEN_SKY_PLAN.md` Bible bloklarıyla BİREBİR (üreteç `00_ANALIZ/06_PROMPT_URETECI/common.py`); sayfa değişirse Bible ve 96 prompt birlikte değişir.
>
> ⚠️ **BETİK DAVRANIŞI:** `### 📸 IMAGE PROMPT` başlığı `prompt_kontrol.py` başlık desenine uyar; bu dosya DOSYA modunda imaj promptu gibi denetlenir
> (IN FRAME · negatif çekirdek · D79 — opak tasarım, D79 bulgusu düşer). ⛔ İngilizce prompt başlıktan sonraki İLK çitli bloktur.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: dört insan, 96/96 sahne (vizör opak — SAPMA 3)
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: opak düz panel vizör · Veyra kalkan kavisi · portal halkası
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: K-1 · E-1/E-2 · C-0 · avcı · T3 kulesi · hangar · kaldıraç
☑ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: Veyra askeri · Serrak · kalibrasyon subayı
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: kalkan sapması (9 sahne) · portal açılışı (S02 S19 S43 S56 S73)
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: K-1 (30+ klip, K0→K3) · işaretleyici drone (5)
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_STOLEN_SKY          FORMAT: yatay 16 dk · 96 × 10 s       ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4K (3840 × 2160)     SAHNE SAYISI: 96
SAYFA: 6   TOPLAM PANEL: 22   ARİTMETİK: R1 4 + R2 5 + R3 3 + R4 3 + R5 4 + R6 3 = 22
İMAJ MODELİ + SÜRÜM: ⬜ (OMNI 1.1 imaj yolu / sahip aracı — ilk sayfada yazılır)   TARİH: 20.09.2026 (TASLAK)
VİDEO: OMNI 1.1 Flash I2V (sahip Q1)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_STOLEN_SKY_KAPAK.md` (RK onayından SONRA; kapak adayı S92)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> Sıra: referans sayfaları → denemeler P1–P6 → DORUK S84 → S92 → S94 · S95 → S00 → S59 → sınır çiftleri → BOLUM_8 → BOLUM_1 → …

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | DÖRT İNSAN | 4 | dört giysi yan yana ön · 3/4 · arka (sırt pozitif) · kask makro (opak panel + çerçeve) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R2 | VEYRA | 5 | asker ön · 3/4 · profil (kalkan yönü) · arka · uzuv/alt bacak ayrıntısı + Serrak (tepe · omuz çıkıntısı) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R3 | K-1 ÜÇ DURUM | 3 | K0 sağlam · K2 kelepçe · K3 kelepçe + arka güdük (aynı kadraj · aynı ışık · ±%3) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R4 | E-1 · E-2 · C-0 | 3 | yatay bant · iki dikey bant (+ is izi varyantı) · kavisli komuta gemisi | 🟠 S05'ten önce | | | ⬜ TASLAK |
| R5 | AVCI · DRONE · ÜÇ ŞEKİL | 4 | avcı · drone (üç kenetleme bacağı) · KALKAN kavisi · PORTAL (iki nokta arası sınırlı kapı) / KAFES (örgü) | 🟠 S01'den önce | | | ⬜ TASLAK |
| R6 | MEKÂN | 3 | T3 kulesi + hangar kapıları (dış) · rezerv odası (depo · T-kol · iki boru) · platform (kaldıraç kafesi · vinç yükü) | 🟠 S47'den önce | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: OMNI arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa "arayüzde yok" yazılır, kapı SHA-256'ya devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanır.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| H-C | komutan (kobalt) | insan | S00 | S94 | R1 | kask/vizör 🟠 · kimlik ≤3 |
| H-O | pilot (turuncu) | insan | S04 | S94 | R1 | kask/vizör 🟠 · sırt ünitesi (tek dar) |
| H-W | mühendis (kırık beyaz) | insan | S02 | S94 | R1 | kask/vizör 🟠 · sırt modül çerçevesi |
| H-G | ağır silahçı (grafit/hardal) | insan | S01 | S59 | R1 | kask/vizör 🟠 · uzun alet (politika) |
| V-S | Veyra askeri (kalkanlı) | canlı | S01 | S89 | R2 | anatomi 🟠 · sayı ≤3 |
| V-K | Serrak (tepe + omuz çıkıntısı) | canlı | S09 | S60 | R2 | anatomi 🟠 |
| V-O | kalibrasyon subayı (dar omuz işareti + kol anahtarı) | canlı | S38 | S39 | R2 p5 | politika (düşüş) |
| K1 | hücumbot (K0 → K3) | araç | S04 | S95 | R3 | oran 🟠 · hasar merdiveni |
| E1 / E2 | tahliye gemileri | araç | S05 | S95 | R4 | desen (yatay / iki dikey bant) |
| C0 | komuta gemisi (kavisli, kehribar) | araç | S69 | S84 (yarıkta) | R4 | oran |
| F | avcı (kavisli, kesintisiz) | araç | S25 | S90 | R5 | siluet ↔ K-1 farkı |
| DR | işaretleyici drone | prop | S02 | S74 | R5 | küçük · kenetlenme |
| SH / PT / LT | KALKAN · PORTAL · KAFES | olay/şekil | S00 | S93 | R5 | üç şekil karışması 🔴 |
| T3 / HG / RR / PL | kule · hangar · rezerv odası · platform | mekân | S00 | S95 | R6 | ölçek şahidi (1H kadrajda) |
```
⛔ KOD kullanılır, AD kullanılmaz [D34] — Mara/Rey/Ada/Bor · Veyra · T3 · K-1 · NEREV-4 promptta yok.
⛔ Envanterde olup sayfası olmayan varlık = çapasız (yok) · sayfası olup çağrılmayan = YETİM (yok).
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| K1 | K0 (temel) | — | S04 | — | R3 p1 |
| K1 | K1 | sağ itki bileziği eğik, dönmez | S29 | S29 | (metne devredilir — ara durum, R3'te panel yok; p1↔p2 arası) |
| K1 | K2 | sağ bileziğe kare çelik kelepçe, sabit açı | S66 | S66 | R3 p2 |
| K1 | K3 | + arka algılayıcı güdüğü (kopuk, ham parlak) | S90 | S90 | R3 p3 |
| H-C | K0 → K1 | sol göğüs plakasında uzun açık sıyrık | S03 | S03 | R1 p1 (K0) — K1 metne devredilir |
| H-G | K0 → K1 → K2 | sağ diz plakası çatlak (S51) · göğüs hücre yuvaları boş (S57) | S51 / S57 | S51 / S57 | R1 p1 (K0) — K1/K2 metne devredilir |
| H-W | K0 → K1 | sırt modül çerçevesi BOŞ (modül kulede kaldı) | S85 | S85 | R1 p3 (K0 dolu) — K1 metne devredilir |
| E2 | K0 → K1 | sağ denge yüzeyinde koyu is | S89 | S89 | R4 p2 (K0) — K1 metne devredilir |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönüş yok [D147 · D84].
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en) — R3'ün üç paneli bu kuralla üretilir.
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişki — bu dosyanın seçimi: R3 ÜÇ PANEL AYNI SAYFADA (ölçülecek; ayrışırsa K2/K3 ayrı sayfaya alınır).
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME (özet — tam liste bölüm dosyalarındaki İNSAN/veyra sütunundan çıkar)

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 · S12 · S13 · S87 · S95 | dış · halka key | R6 p1 (kule+hangar) + R5 p4 (kafes) + R1 p3 (S00 sırt) | geniş | K0 | savrulan gemi (tek kullanımlık, sayfa yok) · koridor bandı eni |
| S01 · S07 · S20 · S22 · S36 · S37 · S72 | dış/iç · kalkan sahneleri | R2 p3 (profil, kalkan yönü) + R1 p1 (ilgili insan) | orta | K0 | dört nokta sapması (hareket) · kalkan yönü cümlesi |
| S02 · S19 · S21 · S43 · S56 · S73 · S74 | portal/drone | R5 p2 (drone) + R5 p3 (portal) | orta | K0 | portal açılış/kapanış (hareket) |
| S04 · S14–S17 · S26 · S30 · S94 | kabin | R3 p1 (K-1 kabin arkası kırpımı) + R1 p1 | orta | K0 / S94 K3 | koltuk düzeni · 0 g kemer |
| S05 · S80 | hangar | R6 p1 (hangar kapıları) + R4 p1/p2 | geniş | K0 | rampalar · sivil ≤3 |
| S09 · S44 · S60 · S70 | C-0 iç | R2 p1 (Serrak) + R4 p3 (C-0 dış — yalnız S69/S70 pencere) | orta | K0 | maket · ekran ikonları · halka |
| S23–S31 · S68 · S77 · S78 · S86 · S90–S93 | uçuş | R3 p1/p2/p3 (sahneye göre durum) + R5 p1 (avcı) | geniş/orta | K0→K3 | sapma yönü (sağa) · jetler |
| S32–S35 · S40–S42 · S45–S59 | havuz · istasyon · platform | R6 p3 (platform) + R1 + R2 | orta | K0/K1 | kaldıraç kafesi · vinç yükü inişi · Bor topallama |
| S61–S67 · S69 · S71–S76 · S79 · S81–S85 | rezerv odası | R6 p2 (depo · T-kol · iki boru) + R1 p1 (eller) | yakın | K0 | lamba durumları · mandal · nabız |
| S38 · S39 | subay | R2 p5 (uzuv + anahtar) | orta/yakın | K0 | düşüş (nötr) · anahtarın çıkarılması |
```
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir. Dördüncü varlık kadraj dışına alınır ya da metne devredilir — PLAN kararı.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR — bu dosyanın seçimi: KIRPIM · gerekçe: OMNI referans girişinin tek nesne okuması (TUR 20 kaydı; sınanacak P1–P3).
· OMNI çağırma: `@R⬜` biçimi arayüzde VAR MI — ⚙️ SINANMAMIŞ; yoksa görsel yükleme sırası tablodaki sıradır.
```

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · DÖRT İNSAN (4 panel: ön · 3/4 · arka · kask makro)
```
IN FRAME: full body, back
Reference sheet, four panels, plain mid-grey seamless backdrop, even neutral key light, 35mm film grain.
Panel 1, front, four suited figures in a row at the same height, feet apart, arms at the sides, every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim. From the left: a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate, a short flat tool in the gloves, a small wrist control on the left forearm; a burnt-orange hard-shell suit with white bands on both upper arms and a narrow flat unit on the back; an off-white hard-shell suit with teal forearms, a flat rectangular module frame on the back, a field reader at the belt; a graphite-grey hard-shell suit with broad mustard chest plates carrying a row of spare power cells, a long dark tool held across the front.
Panel 2, the same four at three-quarter angle.
Panel 3, the same four from behind: the cobalt and graphite-grey backs each one continuous sculpted surface from collar to hip carrying nothing; the burnt-orange back one continuous surface carrying only one narrow flat unit; the off-white back one continuous surface carrying only one flat rectangular module frame.
Panel 4, macro of one helmet: squared shell, thick dark rim, one flat pane fully opaque matte black, nothing visible behind it. Fine grey dust in every seam on all four.
NEGATIVE: Exactly 4 human characters in suits, no duplicates, no extra person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No backpack, no tank, no hose, no rear housing beyond the one unit and the one frame named. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · ön dört giysi (renk bandı + işaret)   p2 · 3/4 — siluet hattı   p3 · SIRT — düz siluet, Rey tek ünite, Ada tek çerçeve [D139]   p4 · kask makro (opak panel + çerçeve) [D146]
⛔ "seamless visor" YAZILMAZ; "optically clear / zero tint" YAZILMAZ (SAPMA 3).
⛔ ARKA PANELDE yokluk listesi TUTMAZ — panel sırta ne KOYACAĞINI söyler: pozitif yüzey [D123 · D139].
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      dört figür, dört farklı ana renk; 120 px'te dört renk bandı ayrışıyor; p3'te sırt çıkıntısı 0 (Rey 1 dar ünite · Ada 1 çerçeve hariç); p4'te panel arkasında hiçbir biçim yok
  RET:        beşinci figür · kubbe vizör · yansıma/yüz izi · sırtta hortum/tank · plakalarda harf
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "kaç kişi, hangisi ağır silahçı?" · doğru cevap: "dört; hardal göğüslü olan"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S00 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: kişi başına öznitelik = 3 (renk · işaret/bant · ekipman) — boy/ten/saç/yaş/yüz 0
```

### 📸 IMAGE PROMPT — SAYFA R2 · VEYRA (5 panel: ön · 3/4 · profil kalkanlı · arka · uzuv/anahtar + Serrak)
```
IN FRAME: full body, back
Reference sheet, five panels on one page, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, 35mm film grain. Beside every figure a plain grey human-height post for scale.
Panel 1, front: a tall pale-ceramic figure a head taller than a human, narrow chest, a long head sweeping back, the lower leg bending backward, dark seams at every joint, a curved amber shield on the forearm with its convex face forward; exactly two arms, two legs and one head.
Panel 2, the same figure at three-quarter angle.
Panel 3, the same figure in exact profile, the shield held out on the far arm so the convex face points along the figure's front and the near flank is bare pale ceramic.
Panel 4, the same figure from behind: the back is one continuous smooth pale-ceramic surface with dark seams, carrying nothing.
Panel 5, two studies side by side: a second figure with the same anatomy but a raised crest on the long head and a single wide ridge on one shoulder (the leader); and a close study of one forearm carrying an amber service key the length of a hand seated in a forearm slot, with a single narrow mark on the shoulder above it (the officer).
NEGATIVE: Exactly two tall figures with two arms, two legs and one head, human count zero, no duplicates. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no human face on any figure. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No extra limbs, no tail, no wings, no second head. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 5   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 ön (ANATOMY LOCK) · p2 3/4 · p3 PROFİL — kalkan yönü (S22 iptal kapısının kaynağı) · p4 arka · p5 Serrak + subay kolu
KABUL SINAVI: KABUL — boy şahidi ölçüsünde figür 1,15–1,25 insan boyu; alt bacak geriye bükümlü; kalkan kavisi p3'te tek bakışta "öne bakan" · RET — insan yüzü/ağzı · üçüncü kol · kalkan düz plaka · Serrak'ta iki omuz çıkıntısı · YABANCI GÖZ — "kalkan hangi tarafı koruyor?" → "önünü" · SONUÇ ⬜ · ⑲ öznitelik: 3 (renk · baş biçimi · kalkan)
```

### 📸 IMAGE PROMPT — SAYFA R3 · K-1 ÜÇ DURUM (3 panel: K0 · K2 · K3 — aynı kadraj, aynı ışık, tek fark)
```
IN FRAME: none
Reference sheet, three identical panels in a row, plain neutral mid-grey seamless backdrop, even neutral key light from the upper left, 35mm film grain, a plain grey human-height post beside the craft for scale in every panel. The same craft in every panel at exactly the same size, angle and place: a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters, seen from the right rear three-quarter so the right thrust ring and the tail are fully visible, the nose pointing away to the left; the ramp closed; the tail one continuous flat surface carrying only the two rings and a short sensor stub.
Panel 1: both thrust rings whole, the tail stub whole.
Panel 2: the only difference — a squared steel clamp bolted across the right thrust ring holding it at one fixed angle, the ring bent out of line under the clamp.
Panel 3: the only differences — the same clamp on the bent right ring, and the rear sensor stub torn off leaving a raw bright stump on the tail.
NEGATIVE: Human count zero in this frame, the craft is the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Equipment identical across the three panels except the two named differences, no drift. Particles obey the stated gravity with continuous momentum, never hovering. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 K0 sağlam (S04–S28) · p2 K2 kelepçe (S66–S89) · p3 K3 kelepçe + güdük (S90–S95)   — K1 (eğik, kelepçesiz · S29–S65) p1→p2 arası, metne devredilir
KABUL SINAVI: KABUL — üç panelde araç eni ±%3; kelepçe p2/p3'te aynı biçim; güdük yalnız p3 · RET — dört koltuk sayılamıyor (kabin görünmüyorsa ayrı kabin kırpımı: p1'den kabin-arkası çerçeve) · burun yönü değişiyor · YABANCI GÖZ — "üç araç mı tek araç mı?" → "tek araç, gittikçe hasarlı" · SONUÇ ⬜
```

### 📸 IMAGE PROMPT — SAYFA R4 · E-1 · E-2 · C-0 (3 panel)
```
IN FRAME: none
Reference sheet, three panels on one page, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, 35mm film grain, a plain grey human-height post beside every craft for scale.
Panel 1: a wide evacuation ship with one broad horizontal white band along its grey hull, blunt nose pointing to the left, ramp closed, three engine bells at the tail; it is four times the length of the post.
Panel 2: a second evacuation ship of the same shape and size with two vertical white bands on its grey hull, nose pointing to the left; a small inset beside it shows its right stabiliser with a dark scorch along it.
Panel 3: the curved amber Veyra command ship, seamless hull, no seams, no windows except one wide dark window band near its front, two smooth turret shapes on its underside, nose pointing to the left; it is twelve times the length of the post.
NEGATIVE: Human count zero in this frame, the craft are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Equipment identical throughout, no drift. Particles obey the stated gravity with continuous momentum, never hovering. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S05'ten önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 E-1 yatay bant · p2 E-2 iki dikey bant (+ is izi inseti, S89+) · p3 C-0 kavisli
KABUL SINAVI: KABUL — 120 px'te yatay/dikey bant ayrımı okunuyor; C-0'da köşe/kenar 0 · RET — bant sayısı değişiyor · C-0'da insan mimarisi izi · YABANCI GÖZ — "hangisi düşmanın?" → "kehribar kavisli" · SONUÇ ⬜
```

### 📸 IMAGE PROMPT — SAYFA R5 · AVCI · DRONE · ÜÇ ŞEKİL (4 panel)
```
IN FRAME: none
Reference sheet, four panels on one page, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, 35mm film grain, a plain grey human-height post in every panel for scale.
Panel 1: a curved seamless Veyra fighter with an amber-lit edge, no straight lines anywhere on it, nose pointing to the left, three times the length of the post.
Panel 2: a small marker drone the size of a helmet with three short clamp legs, shown twice — in the air with the legs folded, and clamped to a flat grey plate with the legs biting it.
Panel 3: the three shapes side by side, each a separate object: a curved amber shield on a pale-ceramic arm with its convex face forward; a bounded gate of amber light standing between two marker points, its edge a clean line, the height of the post; and a flat square sample of the sky lattice — straight amber lines crossing at right angles, spaced no wider than two ship-lengths, drawn on dark sky.
Panel 4: the same lattice sample with one straight gap parted through it, two ship-widths wide, with hard amber edges — the corridor.
NEGATIVE: Human count zero in this frame, the objects are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Equipment identical throughout, no drift. Particles obey the stated gravity with continuous momentum, never hovering. The shield, the gate and the lattice are three different shapes and never blend into one effect. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S01'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 avcı (siluet ↔ K-1) · p2 drone (havada + kenetli) · p3 ÜÇ ŞEKİL yan yana · p4 kafes + koridor bandı
KABUL SINAVI: KABUL — p3'te üç şekil üç ayrı nesne olarak sayılıyor; kalkan kavisi, kapı kenarı ve örgü çizgileri farklı kalınlıkta · RET — glow/ışıma tek efekte dönüşüyor · avcıda düz kenar · YABANCI GÖZ — "kaç farklı ışıklı şey var?" → "üç" · SONUÇ ⬜
```

### 📸 IMAGE PROMPT — SAYFA R6 · MEKÂN (3 panel: kule + hangar dış · rezerv odası · platform — sahnenin kendi ışığı)
```
IN FRAME: none
Reference sheet, three panels, each lit by its own scene light, 35mm film grain, a plain grey human-height post in every panel for scale.
Panel 1, exterior: black basalt ridges and angular worn human structures down a slope; one tall squared service tower with an emitter at its top; two heavy hangar doors set into the slope; high in the sky a wide amber lattice of straight lines spaced no wider than two ship-lengths, and beyond it, lower and smaller, the lensed bright ring above the tower's silhouette; amber key from the ring, cold sky fill.
Panel 2, interior: a squared reserve room of grey plate under cold lamps; one big cylindrical tank with narrow slots showing an amber light inside; on its flank a control housing with a T-handle selector in a slotted guide between two outputs — a short thick pipe with a squared cap on the left, a long thin pipe running to a far valve on the right; a small spring latch under the handle; a narrow slit high on the far wall; a heavy squared containment door hanging raised on rails above the entrance.
Panel 3, interior: a wide metal platform under cold lamps; two cargo lines on the deck; stacked crates; a caged lift of fine metal mesh with a long lever beside it; a heavy squared load hanging from a ceiling crane; at one end a tall gate frame of two marker points in a curved amber wall.
NEGATIVE: Human count zero in this frame, the places are the subject. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. Equipment identical throughout, no drift. Particles obey the stated gravity with continuous momentum, never hovering, terrain static. The lattice and the ring are two different shapes that never blend. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S47'den önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 kule + hangar + kafes + halka (S00/S87 çapası) · p2 rezerv odası (S61–S85 çapası: depo · T-kol · iki boru · mandal · yarık · muhafaza kapağı) · p3 platform (S47–S59 çapası)
KABUL SINAVI: KABUL — p1'de örgü ve halka ayrı; p2'de iki boru kalın/ince ve kısa/uzun ayrımı 120 px'te okunuyor; p3'te kaldıraç kafesi + asılı yük sayılıyor · RET — yüzeylerde harf/ok · örgü halkaya karışıyor · YABANCI GÖZ — "kol hangi iki şey arasında?" → "kısa kalın boru ile uzun ince boru" · SONUÇ ⬜
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
```
□ ① PANEL ARİTMETİĞİ  §1 künye 22 = §2 tablo 4+5+3+3+4+3 = 22 ✅ (yazımda)
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var · YETİM sayfa 0
□ ③ 120 PX TESTİ      panel 120 px'e inince şu öğeler ayırt ediliyor: dört giysi rengi · yatay/dikey bant · kelepçe · örgü/halka ayrımı · iki boru
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
□ ⑤ VİZÖR (SAPMA 3)   opak mat siyah düz panel + görünür kalın çerçeve; panel arkasında hiçbir biçim yok (kubbe değil) [D146]
□ ⑥ D139 SIRT         sırt çıkıntı sayısı 0 (Rey 1 dar ünite · Ada 1 çerçeve hariç) VE yüzey POZİTİF tarifli
□ ⑦ SAYI              R1 figür 4 · R2 figür 2 · R3 araç 1 × 3 · R5 üç şekil 3
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — dört giysi gri tonda da ayrışıyor mu (kobalt/turuncu/kırık beyaz/grafit → değer farkı); önce fiilen sınanır
□ ⑧ DURUM ÇİFTİ       R3 üç panel aynı kadraj · aynı ışık yönü · ±%3
□ ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik ≤3 (betik: FIX)
□ ⑩ ⑳b DEĞİŞİM        referans promptu değişimin SONRASINI yazmıyor (R3 durumlar ayrı panel) [D179]
□ ⑪ ÖLÇEK ŞAHİDİ      her yapı/araç panelinde gri direk (1H) kadrajda
□ ⑫ SEED / SHA KAYDI  §2 tablosuna YAZILDI
□ ⑬ BAYT AYNILIĞI ⚙️  paketteki kimlik cümleleri ile PLAN Bible / bölüm promptları `diff` temiz (üreteç common.py tek kaynak)
□ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ⬜
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
☑ Tetikleyici kontrolü işaretlendi      ☑ Envanter · merdiven · eşleme yazıldı
☑ Sayfa blokları yazıldı (R1–R6 TASLAK)  ⬜ Kabul kapısı koşulmadı, seed/SHA boş — sayfalar üretilince (sahip · imaj aracı)
```
