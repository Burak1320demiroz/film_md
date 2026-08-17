# 📄 FAZ DOSYASI ŞABLONU — Sahne Prompt Yapısı

> Bu şablon `01_FAZ_1_KURULUS.md` … `05_FAZ_5_COZULME.md` dosyalarının iskeletidir.
> Start/End Frame zinciri mantığına göre kurulmuştur — 2-4 dk filmlerdeki
> text-to-video şablonundan **yapısal olarak farklıdır**.

---

## ⚠️ EN KRİTİK FARK: SAHNE BAŞINA **TEK** YENİ İMAJ

Zincirleme mantıkta bir sahnenin başlangıç karesi, bir önceki sahnenin bitiş karesidir.
Yani her sahne için **iki değil, bir** imaj promptu yazılır.

```
SEKANS BAŞI:  ÇAPA İMAJI üretilir           (İmaj 1)
Sahne 1:      İmaj 1 → [İmaj 2 üretilir]  = Video 1
Sahne 2:      İmaj 2 → [İmaj 3 üretilir]  = Video 2
Sahne 3:      İmaj 3 → [İmaj 4 üretilir]  = Video 3
Sahne 4:      İmaj 4 → [İmaj 5 üretilir]  = Video 4
SEKANS SONU:  zincir kırılır, yeni çapa imajı
```

> 4 sahnelik bir sekans = 5 imaj + 4 video.
> Her sahne dosyasında yazılan IMAGE PROMPT, **o sahnenin BİTİŞ karesidir**.

---

## 📋 FAZ DOSYASI İSKELETİ

````markdown
# 🎬 FAZ N — [FAZ ADI]
## [Film Adı] | Sahne X-Y | 12 sahne × 8s = 96 saniye

> **Zaman aralığı:** M:SS – M:SS
> **Tempo imzası:** [yavaş / artan / kırılgan / hızlı / geniş]
> **Bu fazın işlevi:** [tek cümle]

---

## 🔗 FAZ GİRİŞ BAĞLANTISI

**Önceki fazın son karesi:** [tarif]
**Bu faza köprü tipi:** [match cut / eylem sürekliliği / ışık geçişi]
**Bu fazın ilk karesi (ÇAPA İMAJI 1):** [tarif]

---

## 📊 FAZ SAHNE HARİTASI

| # | Sahne | Sekans | Mekan | Aksiyon | Diyalog | Yeni imaj |
|---|---|:---:|---|---|:---:|:---:|
| SX | ... | 1A | ... | ... | — | İmaj 2 |
| ... | | | | | | |

**Bu fazda üretilecek:** 15 imaj (3 çapa + 12 bitiş karesi), 12 video

---

## 🎬 SEKANS 1A — [SEKANS ADI] (Sahne X-X+3)

### 🖼️ ÇAPA İMAJI 1 — Sekans Başlangıç Karesi

> ⚠️ Bu imaj zincirin ilk halkasıdır. Sekans içindeki tüm devamlılık buna dayanır.
> Karakter seed'i ve mekan referansı burada kilitlenir.

```
[TAM SELF-CONTAINED IMAGE PROMPT — aşağıdaki bölüm şablonuna göre]
```

---

### 🎬 SAHNE X — [SAHNE ADI]

```
START FRAME:  Çapa İmajı 1
END FRAME:    İmaj 2  ← aşağıda üretiliyor
SÜRE:         8 saniye
LENS:         [32mm / 75mm]
MESAFE:       [X metre]
HAREKET:      [tek hareket tipi]
```

#### 🖼️ IMAGE PROMPT — İmaj 2 (bitiş karesi)

```
[TAM SELF-CONTAINED IMAGE PROMPT]
```

#### 🎥 VIDEO PROMPT — Video X (İmaj 1 → İmaj 2)

```
[START/END FRAME VIDEO PROMPT]
```

---

[Sahne X+1, X+2, X+3 aynı yapıda...]

---

## 🎬 SEKANS 1B — ... (zincir kırılır, yeni çapa imajı)

[Aynı yapı tekrarlanır]

---

## 🔗 FAZ SONU BAĞLANTI NOTU

**Bu fazın son karesi:** [tarif]
**Sonraki faza köprü tipi:** [match cut / eylem sürekliliği / ışık geçişi]
**Sonraki fazın ilk karesine bağlantı:** [tarif]
**Renk sıcaklığı devri:** [XXXXk → XXXXk]
````

---

## 🖼️ IMAGE PROMPT ŞABLONU (Self-Contained)

> Bible'a atıf YOK. Her prompt tek başına çalışır.
> `[CHARACTER BIBLE]` gibi etiketler **yasak** — içerik doğrudan yazılır.

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. [tür/mekan].
Faz N, Sahne X. EXACTLY ONE human character in frame.

SCENE:
[Tek cümlelik özet — ne oluyor, kim nerede. Bu kare zincirin hangi halkası?]

ENVIRONMENT:
[Mekanın tam fiziksel tarifi — atmosfer, zemin, gökyüzü, ışık kaynakları,
ölçek referansları. Bible'dan kopyalanır, atıf yapılmaz.]

SUBJECT:
[KARAKTER ÇAPA BLOĞU — 60 sahnede KELİMESİ KELİMESİNE aynı. Yaş, boy,
cilt dokusu, yüz yapısı, saç, iz/yara, suit'in her detayı ölçüsüyle,
vizör durumu. Ardından: bu karedeki poz, eylem, ifade, ekipman durumu.]

CAMERA:
[Lens]mm anamorphic, f/[X], ISO [X], camera fixed at approximately [X] meters,
[açı]. [Alan derinliği]. Physically accurate perspective, correct
engineering proportions, realistic scale relationships.

LIGHTING:
[Numaralı ışık kaynakları, her biri motivasyonlu ve görünür kaynaklı.
Renk sıcaklıkları Kelvin cinsinden. Sharp directional light, clear falloff,
0% bloom. ANTI-GLOW: "glowing/ethereal/radiant/shimmering" KULLANMA.]

PHYSICS:
[Yerçekimi değeri, partikül davranışı, temas bütünlüğü, ölçek referansları.]

NEGATIVE:
[Tam yazılmış negatif blok — bkz. aşağıdaki EVRENSEL NEGATİF BLOK]
```

---

## 🎥 VIDEO PROMPT ŞABLONU (Start/End Frame Modu)

> Bu şablon text-to-video şablonundan farklıdır: iki kare zaten verildiği için
> prompt **aradaki hareketi** tarif eder, sahneyi sıfırdan kurmaz.
> Ancak karakter çapa bloğu **yine de yazılır** — Veo kılavuzu §6 çapraz doğrulama
> kuralı, referans görsel yüklense bile metinde tekrar edilmesini şart koşar.

```
Photorealistic cinematic video. 16:9 widescreen. Single continuous shot,
0 cuts, 8 seconds. [tür]. EXACTLY ONE human character.

START FRAME: [başlangıç karesinin tek cümlelik tarifi]
END FRAME:   [bitiş karesinin tek cümlelik tarifi]
The shot begins exactly on the start frame and ends exactly on the end
frame. Everything between is one unbroken continuous move.

SUBJECT ANCHOR:
[KARAKTER ÇAPA BLOĞU — kelimesi kelimesine aynı]

MOTION (8s, [lens]mm, [hareket tipi], [X] meters):
0s — [başlangıç durumu = start frame]
2s — [ilk beat]
4s — [ikinci beat]
6s — [üçüncü beat]
8s — [bitiş durumu = end frame]. No cuts.

DIALOGUE:
[Tırnak sentaksı: "she says in a [ton] voice: '[replik]'"
Her replik <5 saniye. Tek konuşmacı sırayla. Geniş çekimde diyalog varsa
"off-screen / comms audio, no lip-sync required" açıkça yazılır.]

AUDIO:
Clean dialogue only. [Diyalog loud/dominant] + [orta plan efekt] +
[arka plan ambiyans faintly]. Maksimum 3 katman. No music. No subtitles.

[EVRENSEL NEGATİF BLOK]
```

---

## 🚫 EVRENSEL NEGATİF BLOK (her prompta yapıştırılır)

```
Single unbroken take. No cuts, no edits, no camera resets, no multiple
shots, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change, no chase-cam. EXACTLY ONE human character
— no duplicates, no clones, no second person. 0% bloom, no glow filter,
no soft focus, no dreamy haze, no ethereal or radiant light, no lens flare
— all light sources emit sharp directional light with clear falloff and
defined shadows, never a color wash; every surface retains visible texture.
Photorealistic skin pores, sweat, scars and fatigue retained under all
light conditions — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure and eye spacing throughout.
Visor ALWAYS visible regardless of head angle, fully transparent, no tint,
no HUD graphics, no autonomous or invented reflections. Suit and equipment
detail identical to the description — no equipment drift. No readable text,
digits, letters or symbols on any display or surface — abstract pulsing
light shapes only. All hand-surface contacts maintain a clear structural
boundary — no merging, no phasing, no extra fingers, rigid-body collision
throughout. All particles obey the stated gravity with continuous physical
momentum — never hovering, never floating without trajectory, never frozen,
no anti-gravity behavior, no frame-rate variance on particle motion, no
low-density CGI particle spray. Environment static and stable — no melting
terrain, no warping topology, no swimming texture. No text overlay, no
title card, no watermark, no subtitles. No Unreal Engine look, no CGI
aesthetic, no video game aesthetic. Photorealistic with 35mm anamorphic
film grain.
```

---

## ✅ FAZ DOSYASI TESLİM CHECKLIST

```
□ 12 sahne (veya kararlaştırılan sayı) tamamlandı
□ 3 çapa imajı + 12 bitiş karesi promptu yazıldı (toplam 15)
□ Karakter çapa bloğu 15 promptta KELİMESİ KELİMESİNE aynı
□ Hiçbir promptta [BIBLE] etiketi kalmadı (self-contained)
□ Her video promptunda START FRAME / END FRAME satırı var
□ Her video promptunda "No cuts." ve negatif blok var
□ Diyaloglu her sahnede "No subtitles" ve "Clean dialogue only" var
□ Geniş çekimdeki diyaloglarda "no lip-sync required" notu var
□ Anti-glow sözlüğü ihlali yok (glowing/ethereal/radiant/shimmering)
□ Sekans kırılma noktaları işaretli
□ FAZ SONU BAĞLANTI NOTU yazıldı
□ Renk sıcaklığı devri bir sonraki faza bağlandı
```

---

## 🔁 ÜRETİM SIRASI (dosya hazır olduktan sonra)

```
1. Çapa imajını üret → seed'i kaydet → REFERANS_PAKETI.md'ye işle
2. Sekans içindeki bitiş karelerini SIRAYLA üret
   (her biri bir öncekini referans alarak — zincir bozulmasın)
3. Sekans imajları onaylandıktan SONRA videolara geç
   ⚠️ İmajlar onaylanmadan video üretme — yanlış imaj = boşa video
4. Video üretiminde: Start frame + End frame yükle, prompt yapıştır
5. Her videoyu bir öncekiyle yan yana kontrol et (devamlılık)
6. Faz bitince VIDEO_QA_CRITIQUE_PROMPT.md çalıştır
7. Yeni hata çıkarsa LESSONS_LEARNED.md'ye ders ekle
```
