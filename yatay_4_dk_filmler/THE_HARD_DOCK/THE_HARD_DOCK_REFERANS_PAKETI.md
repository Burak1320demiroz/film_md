# 🧷 THE_HARD_DOCK — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → S22 DORUK → S23 → S19 → S24 → S01 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> **Revizyon 11.09.2026:** ilk taslak "gold mirrored visor" ile "optically clear
> visor" cümlelerini aynı sayfada taşıyor, R2 promptunu üç kez yapıştırıyor ve
> üretilmemiş panellere uydurma seed/SHA ile ONAYLI yazıyordu. Hepsi silindi;
> paket ⬜ TASLAK durumundadır, hiçbir panel henüz üretilmedi.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: A01 pilot
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: A01 kask paneli · V01 halka + dört dikme
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: M01 istasyon yakası (gemi/istasyon 1/20)
□ T4 İNSAN DIŞI CANLI                                            —
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY                                 —
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: THE_AMBER_LATTICE (istasyon panelleri sahneler arası boyut değiştirdi)
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_HARD_DOCK          FORMAT: yatay 3-5 dk    ORAN: 16:9
SAYFA ORANI = FİLM ORANI     ÇÖZÜNÜRLÜK: 3840×2160   SAHNE SAYISI: 24
SAYFA: 4   TOPLAM PANEL: 16   ARİTMETİK: R1 4 + R2 5 + R3 3 + R4 4 = 16
İMAJ MODELİ + SÜRÜM: ⬜ araçtan yazılır (üretim günü)   TARİH: 11.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_HARD_DOCK_KAPAK.md` (R1/R2 onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> Sıra: R1 → R2 → R3 → R4 → DORUK S22 → S23 → merkezî seçim S19 → kapanış S24 → S01 → kalanı

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 4 | A01 pilot — giysi · kask (berrak düz panel) · düz sırt · vizör ardı yüz | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| R2 | 2 | 5 | V01 servis gemisi — burun halkası + DÖRT dikme (K0 uzun · K1 çökük) | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| R3 | 3 | 3 | M01 istasyon sekizgen yakası + bükük mandal güdükleri + kopuk kol | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| R4 | 4 | 4 | I01 kokpit — pencere · konsol · koruma kapağı (kapalı/açık) · dört lamba | 🟠 S02'den önce | ⬜ | ⬜ | ⬜ TASLAK |
```
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ. Bugün ONAYLI sayfa: 0.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa "arayüzde yok".
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanır.
```

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| A01 | pilot (kasklı, mühürlü, berrak panel) | insan | S02 | S24 | R1 | yüksek (kask geometrisi D146 · sırt D139) |
| V01 | servis gemisi burnu — halka + 4 dikme | araç | S01 | S23 | R2 | yüksek (dikme sayısı · çökme durumu) |
| M01 | istasyon yakası + gövde + kopuk kol | mimari | S01 | S24 | R3 | orta (sekizgen · güdük sayısı) |
| I01 | kokpit: pencere · konsol · kapak · lambalar · iptal barı | mekân | S02 | S24 | R4 | orta (ekran 0 · lamba 4) |
| P01 | kopan radyatör paneli | prop | S02 | S13 | R3 p3 | düşük (metne devredildi: dönüş) |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Sayfası olup çağrılmayan sayfa (YETİM): 0.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| V01 dikmeler | K0 (temel) | dört dikme tam uzunlukta, halka yakası yuvarlak | S01 | — | R2 p4 |
| V01 dikmeler | K1 | dört dikme sonuna kadar çökük, yaka bükük | S22 (6,0 s) | S23 · S24 | R2 p5 |
| I01 koruma kapağı | K0 | kapak KAPALI | S02 | — | R4 p2 |
| I01 koruma kapağı | K1 | kapak AÇIK, düğme açıkta | S19 (3,0 s) | S20-S24 | R4 p3 |
| I01 lambalar | K0 | dördü sönük | S02 | — | R4 p1 |
| I01 lambalar | K1 | dördü yanık | S24 | — | R4 p4 |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönüş yok (dikme çökmesi, kapak, lamba: üçü de tek yönlü).
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK: R2 p4↔p5 · R4 p2↔p3.
A01 pilot: durum merdiveni YOK — giysi, kask, eldiven 24/24 aynı; kir/yıpranma 0 (kabin içi).
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01 S05 S07 S13 | dış · istasyon arkadan ışıklı | R3 p1 · R2 p4 | yaka + halka alt kenar | K0 | salınım hızı · panelin dönüşü (S13) |
| S06 | dış · üst açı | R2 p2 · R3 p2 | iki gövde, oran 1/20 | K0 | boşluk (altı gemi boyu) |
| S14 S15 | dış · tepe | R3 p2 | istasyon gövdesi + kollar | K0 | salınım |
| S16 | dış · port-kilitli | R3 p1 · R2 p1 | yaka ön planda, gemi uzakta | K0 | arka planın kayması |
| S02 S04 S08 S12 S17 S21 | iç · OTS | R1 p3 · R4 p1 | sırt + pencere + konsol | K0 | pencerede istasyonun hâli · kol/parmak hareketi |
| S03 S09 S11 S18 S20 | iç · yüz | R1 p4 · R4 p2 | vizör ardı yüz + konsol üst kenarı | K0 (S20: kapak K1) | bakış · nefes · omuz |
| S10 | iç · el makro | R4 p2 · R1 p1 (eldiven) | eldiven + T-kol + kapak KAPALI | K0 | iki tık · itiş |
| S19 | iç · el makro | R4 p3 · R1 p1 (eldiven) | eldiven + kapak AÇIK | K1 | kapağın kalkışı (klip içi, tek yönlü) |
| S22 | dış · port-kilitli | R3 p1 · R2 p1 · R2 p4 | gemi kadraja girer, dikmeler UZUN | K0→K1 (6,0 s) | oturma anı — klip içinde, sahne SINIRINDA değil (B1) |
| S23 | dış · port-kilitli | R3 p1 · R2 p5 | dikmeler ÇÖKÜK, gemi sabit | K1 | gezegenin kayması |
| S24 | iç · OTS | R1 p3 · R4 p4 | pencere dolu, dört lamba yanık | K1 | eldivenlerin açılışı |
```
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir. YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR (§4.3);
   bu dosyanın seçimi: KIRPIM · gerekçe: panel oluğu ve etiket sızıntısı depoda ölçüldü.
· Flow çağırma: `@R1` … `@R4` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
```

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · A01 pilot
```
Photorealistic reference sheet, 16:9, 4K, four equal panels side by side on a plain neutral mid-grey seamless backdrop, even neutral key light with soft fill and a small local light inside the helmet so the face reads in every panel. Exactly one human character, the same person in all four panels — no clones, no second person.

She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane at every head angle. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing.

Panel one: full length, three-quarter view, standing straight, gloves open at her sides. Panel two: full length, exact profile, the flat front pane and its dark rim seen edge-on. Panel three: full length from directly behind — the back of the suit is one continuous smooth white panel from collar to hip, unbroken, carrying nothing: no pack, no tank, no housing, no strap, no hose, no cable, no hard-point; a plain surface, and the plain surface is what this panel shows. Panel four: close-up of the helmet from the front, the face fully readable through the clear flat pane, the dark rim all the way round, the thin specular line along the upper edge, the collar seal ring at the bottom.

NEGATIVE: 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The pane is clear glass with zero tint, zero mirror coating and zero reflection — no gold, no black, no mirrored visor. No bubble helmet, no dome, no seamless wrap-around pane. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — no patch, no flag, no logo; no panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No watermark. Photorealistic, 35mm film grain.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy   p2 · profil — düz panel kenardan   p3 · SIRT — düz [D79/D139]   p4 · vizör ardı yüz CU [D146]
KABUL SINAVI (R1): KABUL: p2'de panel DÜZ ve çerçeve görünür · p3'te sırt çıkıntısı 0 · p4'te yüz okunur ve pane'de çevre yansıması 0
                   RET: kubbe/balon · aynalı veya renkli pane · sırtta herhangi bir ünite · çıplak deri
                   YABANCI GÖZ: "Kaskın camı düz mü kavisli mi? Yüzünü görüyor musun?" · doğru cevap: "düz, evet"
                   SONUÇ: ⬜ · ⑲ KİMLİK YIĞINI: 3 (yaş · yapı · ten)
```

### 📸 IMAGE PROMPT — SAYFA R2 · V01 servis gemisi burnu
```
Photorealistic reference sheet, 16:9, 4K, five equal panels in one row on a plain neutral mid-grey backdrop, soft top light with a faint reflection from below. Human count in this frame: zero — a machine only, no figure.

The subject is the nose of a small blunt-nosed service craft: matte white hull with two safety-orange bands, and at the very front a round docking ring about a third of the craft's width, held out from the hull on exactly four spring struts spaced evenly around the ring — four struts, no more, no fewer. Each strut is a straight telescoping cylinder with a visible spring sleeve. No markings of any kind on the hull.

Panel one: the craft nose-on, the ring a full circle in the centre, the four struts seen end-on at four evenly spaced points. Panel two: exact profile of the whole craft, nose pointing toward screen-right, the ring standing out ahead of the hull on its struts. Panel three: three-quarter view from above, nose toward screen-right. Panel four: close-up of the ring and its four struts from the side, every strut at its full extended length, the ring's rim perfectly round. Panel five: the identical close-up from the identical position, with one difference — all four struts fully compressed down to almost nothing between the ring and the hull, and the ring's rim slightly buckled; nothing else changes.

NEGATIVE: 0% bloom, no glow filter, no soft focus. No human figure, no pilot, no scale figure. Exactly four struts in every panel — never three, never five, never six. No readable text, letters, digits, numbers or symbols anywhere in the frame — no flag, no logo; no panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No plume, no exhaust, no flame, no spark, no smoke. No lens flare, no anamorphic streak. No CGI aesthetic. No watermark. Photorealistic, 35mm film grain.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 5   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · burundan   p2 · profil (burun sağa)   p3 · 3/4 üst   p4 · halka + dikme makro K0 UZUN   p5 · aynı kadraj K1 ÇÖKÜK
KABUL SINAVI (R2): KABUL: her panelde dikme sayısı TAM 4 · p4↔p5 aynı kadraj, tek fark dikme boyu (±%3 en)
                   RET: 3 ya da 5 dikme · p5'te halka kaybolmuş · p4/p5 kadraj farkı
                   YABANCI GÖZ: "Halkayı kaç çubuk tutuyor? Son iki panelde ne değişti?" · doğru cevap: "dört · çubuklar kısaldı"
                   SONUÇ: ⬜ · ⑲ KİMLİK YIĞINI: — (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R3 · M01 istasyon yakası
```
Photorealistic reference sheet, 16:9, 4K, three equal panels side by side. Human count in this frame: zero — structures only, no figure. The light in all three panels is the film's own single light: a hard white sun from upper screen-right and out of frame, absolutely black razor-edged shadows to screen-left, and a weak deep-orange light from below; no fill, no haze.

The subject is the docking end of a derelict industrial relay station: a long dark-grey cylindrical hub, and at its near end an OCTAGONAL docking collar — eight straight sides, a dark open throat — with the station's own capture latches around the collar's rim bent flat into useless stubs, all of them bent inward. Two long radiator arms leave the hub at right angles; the screen-left arm is torn short, its remaining panels bent. Dark titanium plating everywhere, dull, scratched; no markings of any kind.

Panel one: the collar face-on and filling the panel, the octagon exact, the throat dark, the bent stubs clearly visible around the rim. Panel two: the whole station from a three-quarter view above, the collar end toward screen-right, both arms visible, the screen-left arm torn short; in the lower-left corner of this panel the nose ring of a small white service craft, drawn at one-twentieth of the station's length, for scale only. Panel three: a single torn radiator panel, alone against black, edge-on, its bent edge catching the hard light — a flat rectangular slab about the width of the collar.

NEGATIVE: 0% bloom, no glow filter, no soft focus. No human figure, no crew. The collar is an octagon — not a circle, not a square. No readable text, letters, digits, numbers or symbols anywhere in the frame — no flag, no logo; no panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. No atmosphere, no clouds, no stars, no haze, no dust, no flame, no spark, no smoke, no lens flare, no anamorphic streak. No CGI aesthetic. No watermark. Photorealistic, 35mm film grain.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · yaka önden (sekizgen + güdükler)   p2 · istasyon 3/4 üst + ölçek şahidi gemi halkası (1/20)   p3 · kopan panel (P01) tek başına
ÖLÇEK ŞAHİDİ [§7 ⑪]: 1H (kasklı gövde) YERİNE gemi halkası — gerekçe: insan hiçbir sahnede gemi dışında değil; V3 oranı (1/20) zaten gemiye bağlı
KABUL SINAVI (R3): KABUL: p1'de kenar sayısı TAM 8 · güdükler içe bükük · p2'de kopuk kol screen-left · gemi/istasyon oranı ~1/20
                   RET: yuvarlak yaka · sağlam mandallar · iki kol da bütün · gemi istasyon boyunda
                   YABANCI GÖZ: "Yaka kaç kenarlı? Mandallar çalışır mı?" · doğru cevap: "sekiz · hayır, bükük"
                   SONUÇ: ⬜ · ⑲ KİMLİK YIĞINI: — (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R4 · I01 kokpit
```
Photorealistic reference sheet, 16:9, 4K, four equal panels side by side, each lit by the cockpit's own light: one small white cabin lamp above the window, and a deep orange light entering low through the round window; hard black shadows; no haze. Human count in this frame: zero — an empty seat, no figure.

The subject is a small single-seat cockpit. A round forward window, thick, in a dark frame, reflection-free, with a plain black field beyond it. Below the window a flat dark console: a row of exactly four round white indicator lamps; at the right-hand position a T-shaped translation handle in a straight slot; just to screen-right of that handle a single push-button under a hinged red-and-white striped guard; at the left-hand position a short rotation handle; at the far screen-left end of the console a tall yellow-and-black striped abort bar standing upright. No screens, no displays, no dials, no markings anywhere.

Panel one: the whole console and window from behind the empty seat, the four lamps all dark, the guard closed. Panel two: close-up along the right-hand end of the console from the side at hip height — the closed striped guard nearest, the T-handle beyond it, the abort bar far in the background. Panel three: the identical close-up from the identical position, with one difference — the striped guard flipped up and standing open on its hinge, the button exposed; nothing else changes. Panel four: close-up of the row of four lamps, all four lit as small steady white points with no halo.

NEGATIVE: 0% bloom, no glow filter, no soft focus, no glow halo on the lamps. No human figure, no hands, no pilot. Exactly four lamps — never three, never five. No screens, no displays, no dials, no HUD. No readable text, letters, digits, numbers or symbols anywhere in the frame — no labels on the console; no panel gutters, no captions, no arrows, no callouts, no dimension lines, no panel titles. No lens flare, no anamorphic streak. No CGI aesthetic. No watermark. Photorealistic, 35mm film grain.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🟠 S02'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · konsol + pencere (arkadan)   p2 · kapak KAPALI makro (D kadrajı)   p3 · aynı kadraj kapak AÇIK   p4 · dört lamba YANIK
KABUL SINAVI (R4): KABUL: lamba sayısı TAM 4 · ekran/yazı 0 · p2↔p3 tek fark kapak · bar screen-left, kapak screen-right
                   RET: beşinci lamba · herhangi bir ekran/ibre · kapak ile bar yer değiştirmiş
                   YABANCI GÖZ: "Konsolda kaç lamba var? Yazı görüyor musun?" · doğru cevap: "dört · hayır"
                   SONUÇ: ⬜ · ⑲ KİMLİK YIĞINI: — (insan yok)
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
```
□ ① PANEL ARİTMETİĞİ  4 + 5 + 3 + 4 = 16 = §2 toplamı ✅ (yazımda)
□ ② ÇAPRAZ BAĞ        §5'teki kodlar A01 V01 M01 I01 P01 §3'te var ✅ · YETİM 0 ✅
□ ③ 120 PX TESTİ      ⬜ (panel üretilince: kask çerçevesi · dört dikme · sekizgen · dört lamba)
□ ④ METİN SAYIMI      ⬜ (panel üretilince)
□ ⑤ D79 VİZÖR         ⬜ optik berrak · yansıma 0 · yüz her açıda · GÖRÜNÜR ÇERÇEVE [D95/D146]
□ ⑥ D79/D139 SIRT     ⬜ sırt çıkıntı 0, yüzey POZİTİF tarifli (R1 p3)
□ ⑦ D69 KLON          ⬜ R1'de figür sayısı = 1 (dört panelde aynı kişi)
□ ⑦b GRİ TON ⚙️       ⬜ `ffmpeg -i <panel> -vf hue=s=0` — kapak/bar ayrımı biçimle (çizgi yönü) de okunuyor mu
□ ⑧ DURUM ÇİFTİ       ⬜ R2 p4↔p5 · R4 p2↔p3 aynı kadraj ±%3
□ ⑨ ⑲ KİMLİK YIĞINI   R1 öznitelik 3 ✅
□ ⑩ ⑳b DEĞİŞİM        imaj promptları t = 0 yazıyor ✅ (K1 panelleri AYRI panel, sahne imajı değil)
□ ⑪ ÖLÇEK ŞAHİDİ      R3 p2 gemi halkası 1/20 (1H yerine — gerekçe §6 R3)
□ ⑫ SEED / SHA KAYDI  ⬜
□ ⑬ BAYT AYNILIĞI ⚙️  R1 kimlik cümlesi = PLAN Character Bible = bölüm promptları ✅ (11.09.2026 diff temiz)
□ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ✅ GO (11.09.2026 klasör koşusu)
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
⬜ Paneller üretilmedi (R1-R4)    ⬜ Kabul kapısı ③-⑧ ve ⑫ koşulmadı, seed boş
```
