# 🧷 THE_LOCKED_PULSE — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK S20 → BEDEL S22 → KAPANIŞ S24 → S2 → S12 → S0 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR (SKYLIGHT 3 kask · YERÇEKİMİ F2 · STANDING WIRE kubbe ·
> STATIC_SHADOW vizör). Bu filmde kilitlenen dört biçim: kask/vizör · sırt · port yakası + bilek halkası · jet.
>
> ⚠️ **BETİK DAVRANIŞI:** `### 📸 IMAGE PROMPT` başlığı `prompt_kontrol.py`'nin BAŞLIK desenine UYAR; bu dosya DOSYA
> modunda normal imaj promptu gibi denetlenir (⑯ ⑮ ⑲ D79 · uzunluk). `## SAHNE n` başlığı TAŞIMADIĞI için KLASÖR
> modunun DİZİ kapılarına GİRMEZ. ⛔ İngilizce prompt, başlıktan sonraki İLK çitli bloktur; künye ve kabul sınavı ALTINDA.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: RK1 mühendis — 24/25 sahne
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: vizör (kubbe ↔ düz pane) · sırt (D139) · port yakası dış halkası
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: halka koridoru kesiti + bay (RI1 · RP) · dış halka/spoke/hub (RX)
□ T4 İNSAN DIŞI CANLI                                            hangi: — (yok)
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: soğutucu buhar jeti (RO) S3 · S8 · S10
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: vana istasyonu 20/25 sahne (RP); emsal: COUNTED_TURN ② kimlik kırılması · HARD_DOCK kumanda kolu değişimi
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_LOCKED_PULSE          FORMAT: yatay 3-5 dk        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4K (3840×2160)    SAHNE SAYISI: 25
SAYFA: 5   TOPLAM PANEL: 19   ARİTMETİK: RK1 6 + RI1 4 + RP 4 + RO 3 + RX 2 = 19
   ⛔ Bu toplam §2 tablosunun panel toplamına EŞİT olmalı (§7 ①) — 6+4+4+3+2 = 19 ✓
İMAJ MODELİ + SÜRÜM: ⬜ (üretim günü yazılır — NBP / NB2 / OMNI; MOTOR sütunu zorunlu)   TARİH: 13.09.2026 (yazım)
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_LOCKED_PULSE_KAPAK.md` (RK1 onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK S20 → BEDEL S22 → KAPANIŞ S24 → S2 (iptal kapısı) → S12 → S0 → kalanı

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| RK1 | mühendis (kimlik · kask · sırt · yüz · bilek halkası) | 6 | 3/4 tam boy · profil · SIRT · vizör ardı yüz CU · sağ bilek halkası makro · kask makro | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RP | vana istasyonu (çark · yaka açık/kilitli çifti · levye+anahtar · fren çarkı) | 4 | bay tam · yaka DURUM ÇİFTİ · aletler · küçük çark | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RI1 | halka koridoru (4 bakış, sahne ışığında) | 4 | A bakışı · bay duvarı · ters E · tavan H | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RO | soğutucu jeti (tam · yarı · yok) | 3 | biçim · uzunluk kademesi · bitiş | 🟠 S3'ten önce | | | ⬜ TASLAK |
| RX | dış halka (uzak · hub'dan) | 2 | anatomi 1+4+1 · S13 kadrajı | 🟠 S13'ten önce | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp karşılaştırılır.
ALARM ÇİFTİ: RI1 p2'nin iki hâli `RI1_ALARM_SONUK` / `RI1_ALARM_YANIK` (aynı kadraj, tek fark kırmızı lamba) — nabız iki uçtur.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| K1 | mühendis (kasklı, arketip I) | insan | S0 | S24 | RK1 | kask/vizör (KART 3) · kimlik ≤3 (⑲) |
| K1-BİLEK | sağ bilek halkası (brushed steel, çeyrek tur mühür) | prop | S10 | S24 | RK1 p5 · RP p2 | bedel çapası (D89) |
| M1 | halka koridoru (deck · paneller · tavan · kayış) | mekân | S0 | S24 | RI1 | tekrar eden birim (KART 13) |
| P1 | vana istasyonu: çark + port yakası + lamba dizisi + alarm lambası | prop | S0 | S24 | RP p1-p2 | sayılabilir nesne (7 lamba) |
| P2 | fren çarkı (sarı-siyah bant, zemin) | prop | S0 | S24 | RP p4 | reddedilen nesne — dokunulmaz |
| P3 | levye (kol boyu) · anahtar | prop | S2 / S6 | S24 (zeminde) | RP p3 | D152 küçük alet buharlaşır → büyük |
| O1 | soğutucu buhar jeti | olay | S3 | S10 | RO | KART 6 parçacık |
| M2 | halka dış görünümü (1 halka · 4 spoke · 1 hub) | mekân | S13 | S13 | RX | KART 13 · KART 10 |
| P4 | alet dolabı | prop | S5 | S6 | RI1 p3 | — |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Envanterde olup sayfası olmayan varlık: yok. YETİM sayfa: yok (RX → S13 · RO → S3/S8/S10).
BELGEDE KALAN (sayılabilir/yer): 7 lamba · şerit SOL pazu+uyluk · bilek halkası SAĞ · 4 spoke · kayış −Y tarafı · fren çarkı zemin
YALNIZ GÖRSELDE KİLİTLENEN (dokunsal/biçim): kask kabuğu + pane çerçevesi · sırt ribli yüzey · yaka dış halkası · jet kenarı · kapitone doku
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| K1 eldiven | K0 (temel) | iki eldiven giyili | S0 | — | RK1 p1-p6 |
| K1 eldiven | K1 | sağ eldiven YAKADA, sağ el çıplak | S22 (224,0 s) | S22 | RK1 p5 (halka) + RP p2 (yaka kapalı) — birleşik okunur |
| P1 port yakası | P0 | açık, dış halka proud | S0 | — | RP p2 sol yarı |
| P1 port yakası | P1 | dış halka çeyrek dönmüş, kapalı | S12 (123,0 s) | S12 | RP p2 sağ yarı |
| P1 lamba dizisi | L0 | 6 yanık + 1 sönük | S0 | — | RP p1 |
| P1 lamba dizisi | L1 | 7 yanık | S23 (233,0 s) | S23 | — (metne devredilir: "all seven lit white") |
| O1 jet | J0 / J1 / J2 | bir karış / yarım karış / yok | S3 / S8 / S10 | S8 · S10 | RO p1 / p2 / p3 |
| RI1 alarm | A0 / A1 | sönük / yanık (nabız uçları) | S0 | her sahne | RI1_ALARM_SONUK / _YANIK |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönülmüyor: eldiven K0→K1 tek geçiş · yaka P0→P1 tek geçiş · lamba L0→L1 tek geçiş · jet J0→J1→J2 [D147 · D84]
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en): RP p2 iki yarı · RI1 alarm çifti · RO üç panel aynı kadraj.
⚠️ Aynı sayfada iki durum (RP p2): seçildi çünkü kilit anının BİTİŞİK okunması gerekiyor (S12 kilit = tek tık, iki hâl aynı ölçekte);
   kılavuz §3 ② ölçülmemiş çelişkisi kabul edilerek — PROB (kırpılmış panel ↔ tam sayfa) sonucu gelince gözden geçirilir.
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S0 · S21 · S24 | iç · A · alarm 2,0/1,0 s | RK1 p1 · RI1 p1 · RP p1 | WS | K0 / K0 / K1 | kayış salınım süresi · duruş · S24 eldiven yakada + 7 lamba (metin) |
| S1 · S18 | iç · B | RK1 p3 (sırt) · RP p1 · RI1 p2 | OTS | K0 | omuz hareketi · anons · S18 kol yakada |
| S2 · S4 · S7 · S10 | iç · C | RK1 p2 · RI1 p1 · RP p1 | MS | K0 | anahtar düşüşü · iki vuruş · çekiş · yumruk yakaya · jet (S4/S7/S10: RO p1/p2) |
| S3 · S8 | iç · D | RP p2 (sol yarı) · RO p1 / p2 | CU | P0 · J0/J1 | çark dönüşü · jet kısalması |
| S5 · S6 | iç · E | RK1 p1 · RI1 p3 · (S6) RP p3 | WS | K0 | yürüyüş · dolap · levye alma |
| S9 | iç · H | RI1 p4 | WS low | — | kask alt banda girer |
| S11 · S15 · S16 | iç · G | RK1 p3 · RP p2 · (S15) RP p3 | MCU high | K0 · P1 | omuz çöküşü · levye düşüşü · kask dönüşü |
| S12 · S14 | iç · D | RP p2 (sağ yarı = kilitli) · RK1 p5 | CU | P1 | çeyrek tur + tık (S12 klip içi) · çekiş |
| S13 | dış · vakum | RX p2 | EWS | — | yıldız süpürmesi · anons (ses) |
| S17 · S19 | iç · J | RK1 p2 · RP p4 · RP p1 | MS dutch | K0 · P1 | el tereddüdü · gövde dönüşü |
| S20 | iç · M | RP p4 | ECU | — | el girer/durur/çıkar |
| S22 · S23 | iç · C | RK1 p2 · RK1 p5 · RP p2 (sağ yarı) | MS | K0→K1 · P1 | mühür açılışı · çıplak el · 7. lamba (S23) |
```
⛔ "METNE DEVREDİLEN" hiçbir satırda boş değil [kılavuz §5.1]. Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2) — hiçbir satır 3'ü aşmıyor.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [§4.3]. Bu dosyanın seçtiği yükleme biçimi: KIRPIM (panel tek tek) · gerekçe: T12
   (panel KIRPIMI yüklenir; tam sayfa modelin panel kenarlarını kadraja taşıma riski — ölçülmedi, PROB açık).
· Flow çağırma: `@RK1` · `@RP` · `@RI1` · `@RO` · `@RX` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun kopyasıdır; ayrışırsa tablo düzeltilir.
```

## 6. 📸 REFERANS SAYFALARI
> ⛔ **İngilizce prompt BAŞLIKTAN SONRAKİ İLK çitli bloktur.** Künye ve kabul sınavı promptun ALTINDA.
> ⛔ RK1'deki kimlik bloğu PLAN Character Bible ve 50 sahne promptuyla BAYT-AYNIDIR (§7 ⑬ diff).

### 📸 IMAGE PROMPT — SAYFA RK1 · mühendis (kimlik · kask · sırt · yüz · bilek halkası)
```
Photorealistic reference sheet, 16:9, 4K: six full-length and close panels of the same man laid out in two rows of three on one plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, no set, no props except the suit. Exactly one human figure — this film has exactly one human total. He is a man in his forties with a broad square face, a heavy brow ridge over deep-set dark eyes, a broad nose, a heavy jaw, set lines across his forehead at rest, and medium olive-brown skin with visible pores. He is sealed in a heavy industrial pressure suit of muted slate-grey quilted padding with broad padded shoulder caps rising to the collar, dark bronze joint rings at the shoulders, elbows and hips, and one amber band around the LEFT upper arm and one around the LEFT thigh. Heavy segmented dark-grey gloves join the sleeves at brushed-steel wrist rings, one piece with the sleeve. The helmet is a rounded hard shell seated deep in a wide bronze collar ring, with a single flat front pane inside a thick dark rim — not a bubble, not a dome — the rim visible at every head angle, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, a soft neutral fill from inside the rim on his face, his face readable through the pane. The back of the suit is one continuous ribbed surface from collar to hip, closed and smooth, carrying nothing. The whole suit carries an even matte dusting of grey grit that never moves. Panel one: three-quarter view, full length, standing straight, facing the lens. Panel two: full profile, full length, the flat front pane seen edge-on inside its thick dark rim. Panel three: seen from directly behind, full length — the back of the suit is that one continuous ribbed surface from collar to hip, closed and smooth, carrying nothing, and the plain closed surface is what this panel shows. Panel four: close-up of the face through the front pane, the pane optically clear, a soft neutral fill from inside the rim, the heavy brow ridge and set forehead lines readable, the thick dark rim and bronze collar ring framing the pane. Panel five: macro of the right wrist where the glove joins the sleeve, the brushed-steel wrist ring seated closed, its quarter-turn release notch visible, the segmented dark-grey glove below it and the quilted sleeve above it. Panel six: macro of the helmet from the side, the rounded hard shell seated in the wide bronze collar ring, the thick dark rim of the single flat front pane, one thin specular line along the pane's upper edge.

NEGATIVE: Fixed camera, single sheet. Exactly one human figure — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing. The front pane is optically clear glass with zero tint, zero mirror coating and zero reflection; the face fully readable through it. No back-mounted unit, no backpack, no tank, no hose, no cable, no rear housing of any kind. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign; no flag, no logo, no patch. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No subtitles, no watermark. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 6   SEED: ⬜ (arayüzde alan VAR mı önce sınanır [D142]; yoksa "arayüzde yok")   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş   p2 · profil — siluet hattı, pane edge-on   p3 · SIRT — ribli kapalı yüzey [D79/D139]   p4 · vizör ardı yüz CU [D146]   p5 · sağ bilek halkası makro (bedel çapası D89)   p6 · kask makro yandan
```
```
KABUL SINAVI (RK1) — dört alan ZORUNLU [D144]:
  KABUL:      p3 sırtta çıkıntı 0 ve yüzey ribli-kapalı okunur · p4 yüz pane ardında okunur, çerçeve görünür (kubbe 0) · p1-p2 amber şerit SOL pazu+uyluk · p5 bilek halkası tek parça, çentik görünür · 6/6 panelde tek insan
  RET:        kubbe/çerçevesiz vizör · sırtta herhangi bir kutu/hortum · şerit sağda ya da iki kolda · ikinci figür · harf/rakam · çıplak deri
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Bu adamın sırtında ne var? / Kaç kişi var?" · doğru cevap: "Hiçbir şey — kapalı, düz, ribli bir yüzey. / Bir kişi."
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · bağlı sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 2 (ten değeri · —; yaş 'forties' regex dışı, yüz işareti 0, saç 0, kesin boy 0)
```

### 📸 IMAGE PROMPT — SAYFA RP · vana istasyonu (çark · yaka açık/kilitli · aletler · fren çarkı)
```
Photorealistic reference sheet, 16:9, 4K: four close panels of the same valve bay laid out in two rows of two, all under the corridor's own even neutral light from above with a red lamp pulse on the panel face. Human count zero — no figure, no hand in any panel. The subject: a recessed valve bay set into a pale grey matte wall panel of a spinning ring habitat's corridor. Panel one: the whole bay square-on — a brushed-steel hand-wheel with four spokes about the width of a helmet at chest height, a round port collar the width of a wrist ring to the left of the wheel at hip height with a second, wider brushed-steel outer ring around it, and above the wheel a horizontal row of seven round lamps each the size of a fist, six lit white and the last one on the right dark; a red lamp above the bay; at deck level below, a second, smaller wheel with a yellow-and-black band around its rim. Panel two: macro of the port collar side-on, split in two halves on the same page with the same framing and light — left half the outer ring standing proud and open, right half the outer ring turned a quarter of a turn and closed flat over the collar's mouth; the scuffed matte grey panel around it. Panel three: on the dark grey ribbed deck, a forearm-long steel bar and a steel wrench about as long as a forearm, lying side by side, both dull steel with worn edges. Panel four: macro of the small deck-level wheel, its brushed-steel rim carrying a matte yellow-and-black band, standing a hand-span above the ribbed deck against the pale grey panel.

NEGATIVE: Fixed camera, single sheet. Human count zero — no figure anywhere. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign; no flag, no logo. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No subtitles, no watermark. No haze, no lens flare. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜ (arayüzde alan VAR mı önce sınanır [D142]; yoksa "arayüzde yok")   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · bay tam (7 lamba · çark · yaka · küçük çark)   p2 · yaka DURUM ÇİFTİ P0/P1 (aynı kadraj)   p3 · levye + anahtar zeminde   p4 · fren çarkı makro
```
```
KABUL SINAVI (RP) — dört alan ZORUNLU [D144]:
  KABUL:      p1 lamba sayısı TAM 7 (6 yanık + 1 sönük, sönük SAĞ uçta) · p2 iki yarıda aynı kadraj/ışık, tek fark dış halka açık↔kapalı · p4 sarı-siyah bant matte, rim brushed · p3 iki alet, ikisi de dull steel · 4/4 panelde el/figür 0
  RET:        lamba ≠ 7 · sönük lamba yanlış uçta · p2 iki yarı farklı kadraj · bantta yazı · üçüncü alet · el
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Kaç lamba var, kaçı yanıyor? / Sağdaki iki yaka arasındaki fark ne?" · doğru cevap: "Yedi, altısı yanıyor. / Biri açık, biri kapalı (halka dönmüş)."
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · bağlı sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA RI1 · halka koridoru (dört bakış, sahne ışığında)
```
Photorealistic reference sheet, 16:9, 4K: four panels of the same empty corridor laid out in two rows of two, each panel a different fixed camera position inside the corridor, all under the corridor's own light. The place: inside the curved corridor of a spinning ring habitat — a dark grey ribbed metal deck that rises visibly into the distance like the inside of a great wheel, walls of pale grey matte panels in four large blocks to each side, a single arched ceiling panel running overhead and giving an even neutral light from above, one red lamp on the right-hand wall above a recessed valve bay, a stiff woven webbing strap clipped to a ceiling rail on the opposite side and reaching almost to the deck as one straight line, a tall pale grey tool cabinet at the far end. Human count zero — no figure in any panel. Panel one: wide view along the corridor from the strap toward the bay, the bay in the right third, the corridor curving up into the distance. Panel two: the bay wall square-on from where a kneeling man's head would be — the brushed-steel hand-wheel about the width of a helmet at the centre, a round port collar the width of a wrist ring to the left of the wheel at hip height, a horizontal row of seven round lamps each the size of a fist above the wheel, six lit white and the last one on the right dark, the red lamp above, and at deck level a second, smaller wheel with a yellow-and-black band. Panel three: the reverse wide view from the far end past the tool cabinet, the bay far down on the left-hand wall. Panel four: from the deck looking up at the arched ceiling panel curving away into the distance, the red lamp high on the right. Shadows are short and soft-edged, softened by bounce from the pale panels; highlights roll off smoothly; no window, no sky, no stars anywhere.

NEGATIVE: Fixed camera, single sheet. Human count zero — no figure anywhere. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign; no flag, no logo. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No subtitles, no watermark. No haze, no lens flare. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜ (arayüzde alan VAR mı önce sınanır [D142]; yoksa "arayüzde yok")   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · A bakışı (WS, kayış solda, bay sağda)   p2 · bay duvarı square-on (B/C referansı) — ALARM ÇİFTİ ayrıca üretilir   p3 · ters E (dolap önde, bay uzakta solda)   p4 · tavan H (zeminden yukarı)
```
```
KABUL SINAVI (RI1) — dört alan ZORUNLU [D144]:
  KABUL:      p1-p3 koridor zemini yukarı kıvrılıyor (halka okunur) · duvar başına 4 blok · tavan tek kemer · pencere 0 · 4/4 panelde figür 0 · kayış tek düz çizgi · alarm lambası 1
  RET:        düz koridor (kavis yok) · pencere/yıldız · ikinci tavan/güverte · figür · yazı · kayış dalgalı
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Bu koridorda garip olan ne?" · doğru cevap: "Zemin yukarı kıvrılıyor / bir çemberin içi gibi."
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · bağlı sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0
```

### 📸 IMAGE PROMPT — SAYFA RO · soğutucu buhar jeti (tam · yarı · yok)
```
Photorealistic reference sheet, 16:9, 4K: three panels in one row of the same open port collar on a pale grey matte panel, seen side-on at collar height under an even neutral light, against the collar a thin white vapour jet — a straight, sharp-edged line of white vapour pointing out from the collar's mouth across the panel. Human count zero — no figure, no hand. Panel one: the jet a hand-span long, straight as a ruler, its edge sharp, not spreading. Panel two: the same collar, the same framing and light, the jet half a hand-span long, still straight and sharp-edged. Panel three: the same collar, the same framing and light, the collar's mouth dark and empty, nothing coming out of it. The vapour is a single narrow line of constant width in every panel; it does not billow, spread, curl or thin toward its tip.

NEGATIVE: Fixed camera, single sheet. Human count zero — no figure anywhere. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign; no flag, no logo. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No subtitles, no watermark. No haze, no mist, no cloud, no lens flare. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S3'ten önce   PANEL: 3   SEED: ⬜ (arayüzde alan VAR mı önce sınanır [D142]; yoksa "arayüzde yok")   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · J0 bir karış   p2 · J1 yarım karış   p3 · J2 yok (aynı kadraj, aynı ışık — durum üçlüsü)
```
```
KABUL SINAVI (RO) — dört alan ZORUNLU [D144]:
  KABUL:      3/3 panelde aynı kadraj+ışık · p1 jet düz, kenarı keskin, uzunluk p2'nin ~2 katı · p3 yakadan çıkan hiçbir şey yok · girdap/bulut 0 · jet genişliği üçünde aynı
  RET:        jet kıvrılıyor / dağılıyor / bulut · p3'te kalıntı · uzunluk farkı okunmuyor
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Üç panelde ne değişiyor?" · doğru cevap: "Jetin uzunluğu — sonra hiç yok."
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · bağlı sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0
```

### 📸 IMAGE PROMPT — SAYFA RX · dış halka (uzak · hub'dan)
```
Photorealistic reference sheet, 16:9, 4K: two panels in one row of the same spinning ring habitat seen from outside in hard vacuum, one hard sun from the upper right, every shadow absolutely black with razor edges, a flat black sky with sharp white stars. Human count zero. Panel one: the whole structure from a distance, filling the frame — a broad ring of riveted grey-metal panels, four straight spokes from a small central hub to the ring, the ring's far side a thin line beyond the hub; one ring, four spokes, one hub, nothing else attached. Panel two: the view from the hub along one spoke toward the ring, the spoke running away up the frame, the ring crossing the upper half of the frame and running out of it on both sides, the other three spokes reaching from the hub to the ring at the sides and below.

NEGATIVE: Fixed camera, single sheet. Human count zero — no figure anywhere. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign; no flag, no logo. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No subtitles, no watermark. No free-floating debris; every panel rigid and taut. No atmospheric haze, no scatter, no lens flare. No tilt-shift look, no miniature or toy-model read. No planet, no moon, no second structure. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S13'ten önce   PANEL: 2   SEED: ⬜ (arayüzde alan VAR mı önce sınanır [D142]; yoksa "arayüzde yok")   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · uzak bütün (anatomi kartı 1+4+1)   p2 · hub'dan spoke boyunca (S13 kadrajı)
```
```
KABUL SINAVI (RX) — dört alan ZORUNLU [D144]:
  KABUL:      spoke sayısı TAM 4 · hub 1 · halka 1 (ikinci yapı 0) · gölge mutlak siyah, dolgu 0 · gezegen/ay 0 · p2 halka kadrajı taşar (ölçek şahidi)
  RET:        spoke ≠ 4 · gezegen · yumuşak gölge / pus · maket okuması · yazı/bayrak
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Kaç kol var? Arka planda ne var?" · doğru cevap: "Dört. Yalnız yıldızlar."
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · bağlı sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_LOCKED_PULSE_QA_SPEC.md` 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
□ ① PANEL ARİTMETİĞİ  §1 künye toplamı 19 = §2 tablo toplamı 6+4+4+3+2 = 19 ✓ (yazımda)
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var ✓ · YETİM sayfa 0 ✓ · P4 dolap RI1 p3'te
□ ③ 120 PX TESTİ      panel 120 px'e inince şu öğe hâlâ ayırt ediliyor: RK1 p3 sırt düz kapalı yüzey · RP p1 lamba dizisi (7 nokta) · RX p1 dört spoke
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138] — GÖZLE (yolo 'text' sınıfı yok, T12)
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146] — RK1 p2/p4/p6
□ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0 AMA yüzey POZİTİF tarifli (ribli, kapalı) — RK1 p3
□ ⑦ D69 KLON          RK1 6/6 panelde figür sayısı = 1; RI1/RP/RO/RX'te 0
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0 gri.png` (ffmpeg 8.1 · hue ✅ 13.09.2026) — amber şerit gri tonda da silüetle ayrışıyor mu (tek insan: figür↔zemin)
□ ⑧ DURUM ÇİFTİ       RP p2 iki yarı · RI1 alarm çifti · RO üçlü: aynı kadraj · aynı ışık yönü · ±%3
□ ⑨ ⑲ KİMLİK YIĞINI   RK1 promptunda kişi başına öznitelik ≤3 (betik: prompt_kontrol ⑲ — 13.09.2026 koşusu: FIX 0)
□ ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin SONRASINI yazmıyor [D179] — RO p3 "nothing coming out" durum panelidir, sahne imajı değil
□ ⑪ ÖLÇEK ŞAHİDİ      RX p2 halka kadrajı taşar + 4 spoke tekrar eden birim; RI1 p1 koridor kavisi (1H figür RK1'de ayrı)
□ ⑫ SEED / SHA KAYDI  §2 tablosuna YAZILDI (üretim günü)
□ ⑬ BAYT AYNILIĞI ⚙️  RK1 kimlik bloğu ↔ BOLUM_1/2 promptları `diff` temiz (üreteç tek kaynak: aynı sabit; yazımda ✓)
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ✅ GO (13.09.2026 klasör koşusu · 5 prompt · BLOCK 0 · FIX 0; ⑯ ⑮ ⑲ D79 temiz)
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
☑ Tetikleyici kontrolü işaretlendi (T1 T2 T3 T5 T6)   ☑ Envanter · merdiven · eşleme dolu
☑ Sayfa blokları yazıldı (RK1 · RP · RI1 · RO · RX)   ⬜ Kabul kapısı koşulmadı, seed/SHA boş (ÜRETİM günü) → DURUM: 5/5 TASLAK
```
