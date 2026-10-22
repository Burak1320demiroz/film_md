# 📦 THE_SNAP_LINE — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

```
DENEY SORUSU   Yüzdeki klostrofobik kask dehşeti (İç gerilim) mi, kordona dayanan makas eylemi (Dış gerilim) mi daha çok tıklatır?
DEĞİŞKEN       Odak (Kask vizörü yakın planı vs. Makas ve gerilen kordon aksiyon planı)
SABİTLER       Karakter tarifi (1.MILLER), 310 m zifiri karanlık su altı (2.MEKAN), tek kişi, sarı-siyah renk kontrastı
AN             A: Çekim C02/C03 · B: Çekim C08
TEK İLİŞKİ     Dalgıç × Kendisini yukarı ölüme çeken gergin sarı kablo
BOŞ ALAN       Sağ alt %20 (YouTube süre rozeti için tamamen boş); sol üst %15 (kapak yazısı için)
KAPAK YAZISI   CUT IT (2 kelime · film adı yazılmaz · başlığı tekrar etmez)
VAAT SINIRI    Dalgıç kaskı (C02), sarı kordon (C03), hidrolik makas (C08), karanlık sualtı fonu (C01–C12)
YÜKLEME SIRASI A ilk (en güvenli yüz/dehşet kancası) · B ikinci
FİNAL          faz 9: ~/film_medya/THE_SNAP_LINE/cikti/kapak_A.png · kareler.py kapak → izleyici/kapak/A/
```

### Kapak A (Vizör Dehşeti ve Kordon Yansıması — Varsayılan)
```text
A cinematic high-contrast close-up shot of a commercial saturation diver's heavy cast-brass helmet at 310 meters underwater, 16:9 aspect ratio. Inside the condensation-fogged curved glass visor illuminated by amber emergency hazard lights, a weathered man in his forties stares in pure terror, his eyes wide and jaw tense. Reflected distinctly in the curved glass of the visor is a taut, vibrating yellow umbilical cable stretching violently upward into the black water. The diver wears a bulky deep-sea yellow diving suit with one thick black chevron band across the left shoulder. The background is pitch-black deep ocean abyss with faint suspended marine silt illuminated by the helmet's white floodlight beam. The bottom right 20 percent of the frame is completely empty dark ocean void with no critical details. No text, no logos, no titles.
```

### Kapak B (Kordona Kilitlenen Makas Çeneleri — A/B Testi)
```text
A dramatic, high-tension eye-level medium-close action shot of a saturation diver cutting away his lifeline at 310 meters deep underwater, 16:9 aspect ratio. In the center-left, two heavy yellow-rubberized work gloves clamp a massive hydraulic tungsten-steel cable-cutter around a thick, vibrating 4-inch yellow umbilical cord that snaps taut straight upward. The diver's cast-brass helmet beam shines a harsh, razor-sharp white spotlight directly onto the cutter's heavy serrated steel jaws biting deep into the yellow rubber sheath. Outside the focused cone of light, the surrounding ocean is total pitch-black abyss. The bottom right 20 percent of the frame is intentionally kept clear and dark. High contrast, visceral tactile textures, no text, no subtitles.
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
