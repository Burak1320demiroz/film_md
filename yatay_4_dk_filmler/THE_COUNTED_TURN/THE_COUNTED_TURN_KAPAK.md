# 🖼️ THE_COUNTED_TURN — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S13 (OVERVIEW) · gerekçe: filmin TEK kapalı-halka karesi.
                120 px'te iki şekil hayatta kalıyor: KAPANAN HALKA ve solda
                küçük bir gövdedeki TEK TURUNCU İZ. Yüz zaten gri lekedir ve
                bu kapak yüze hiç yaslanmıyor.
                ⛔ "en güzel sahne" gerekçe değildir — tek sınav 120 px'tir.
                ⭐ Kapak ANI plana yazıldı; kapak AYRI bir kare olarak üretilir
                  ve KURGUYA GİRMEZ (kapak çıktısı klip zincirine karışmaz
                  [D70/D72 — on üç vakalık zincir]).
BAŞLIKLA UYUM:  Kapak "kapanmış bir halka + tek küçük insan" vaat ediyor;
                başlık THE COUNTED TURN aynı şeyi söylüyor: sayılan bir dönüş.
                Çapraz kontrol: THE_COUNTED_TURN_YAYIN_PAKETI.md → CROSS-PLATFORM
PLAN B KAPAK:   S24 (AÇIK KALAN) — makro: pimde iki klips, biri açık.
                ⛔ Kart Y yayından ÖNCE hazır olmasını ister (§7.2); 48 saatte
                  üretilmeye BAŞLANAN kapak karar penceresini kaçırmıştır.
                ⚠️ Plan B TWIST'i açık ettiği için ikinci sıradadır ve yalnız
                  CTR %1-2 alarm bandına düşerse devreye alınır.
ÖLÇÜ:           yatay 1280×720 (+ 4K master)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 IMAGE PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic still image, 16:9 widescreen, 4K, 35mm film grain. Hard science fiction, the inside of a ring station under construction. Exactly one human character — no clones, no second person.

A single suited figure stands small on the bare machined aluminium deck, low in the left third of frame, one gloved hand still on a heavy dark grey woven band that runs away from her along a welded seam. The deck curves upward on both sides and closes overhead, and the same band she has laid runs along that overhead deck from one side of frame to the other, so the whole ring reads as one closed loop of work around a single small body. Nothing is standing on the overhead deck. One section of the inner skin is unplated and the star field shows through the open ribs behind her — individual separate points, no trails, no streaks. She is in a matte pale-grey pressure suit whose back is one continuous smooth panel from collar to hip, carrying nothing; the helmet has a flat rectangular front pane in a visible brushed metal rim, optically clear with zero tint and zero mirror coating, and her face is fully readable through it. A short row of anodised orange clips rides on her right hip — the only warm colour anywhere in the frame.

COMPOSITION: 16:9. The figure sits low in the left third, small against the curve; the closed ring fills the upper two thirds. Nothing story-critical falls in the bottom sixth or the right sixth of the frame, where platform interface elements sit. Read at 120 pixels, two shapes survive: the closed ring, and one small bright-orange mark on a pale body.

LIGHTING: One hard source along the ring's axis grazing the deck. No fill and no bounce; shadows completely black with razor edges. Highlights roll off smoothly and keep texture instead of clipping to white.

NEGATIVE: Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. The suit has no back-mounted unit of any kind: no backpack, no tank, no hose, no rear housing. No dust, no smoke, no sparks and no flame anywhere. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle. No miniature look, no tilt-shift, no scale-model appearance. No text, no letters, no numbers, no watermark, no HUD overlay.

Output: 16:9, 1280x720 and 4K master, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
  KAPANAN HALKA (üst iki üçte bir) + solda TEK TURUNCU İZ (kalça sırası)

⛔ İKİ AYRI GÖRÜNTÜYE koşulur [SHORTS_SISTEM_PROMPTU 3.6 · 27.08.2026]:
   ① bu kapak   ② S0'ın İLK KARESİ
   İkisi de 120 px'te tek şekil vermeli. "Bence okunuyor" demek bu testi
   geçmek sayılmaz.

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)

CTR SKALASI [KAPAK §7.1]: %1-2 alarm · %3-4 ortalama · %5-6 güçlü · %7+ olağanüstü
⛔ İlk 48 saatte TEK değişken oynatılır: kapak VEYA başlık, ikisi birden değil.
```
