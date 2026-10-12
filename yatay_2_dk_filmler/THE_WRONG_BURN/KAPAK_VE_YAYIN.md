# 📦 THE_WRONG_BURN — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK
<!-- kaynak: ODA/F6_kapak-tasarimcisi_2.md §1 (birleştirme geçişi + Fable kararları 1-8 işlenmiş hâli, birebir; F6 KAPANDI 10.10.2026). Kapak A/B promptları MAKET'tir; final kare C04 videosundan, faz 9. Riskler R1-R7 ve faz 9 ön notu ODA dosyası §2-§3. Kapak anı kilidi FILM §4 C04 Risk hücresinde. -->


```
DENEY SORUSU   Kehribar nokta kaskla aynı hizada, karşıda dururken mi, yoksa kaskın çok altında, Dünya'nın
               mavi kenarının hemen üstünde dururken mi daha çok izlenme süresi payı alır?
               (nokta kask hizasında ↔ nokta kaskın altında, ufkun hemen üstünde)
DEĞİŞKEN       zamanlama: aynı çekimin iki anı. A = iniş başlamadan (C04 0,3 s) · B = inişin siyah gökteki
               son karesi (C04 ≈1-2 s). Değişen: noktanın yüksekliği (A→B ≈16-20 puan aşağı). İnişin filmdeki
               yan etkileri B'de onunla birlikte gelir (nokta biraz küçülür ve ≈1-4 puan sağa kayar, ufuk
               ≈1-2 puan iner). Bunlar aynı zamanlamanın parçası, ayrı değişken değil.
SABİTLER       karakter tarifi (FILM §3 SELA_arka_v1 + G01 C04 sözcükleri, birebir) · dünya ışığı: gündüz,
               Dünya altta tam aydınlık; DUNYA_gunduz_alt_v1 (ref'te güneş tepede; yönü prompt veriyor: "high
               at the left …", G01 C04 Görsel ile birebir, FILM §4 SAPMA 4) · figür sayısı (bir kadın + bir
               kehribar nokta; adam nokta boyunu geçmez) · kamera ve kadraj (C04: 35 mm, sağ arka ¾, belden
               yukarısı, kamera sabit) · Sela'nın pozu ve kask yönü · kaynak (ikisi de aynı C04 videosundan,
               aynı çözünürlük ve ölçekleme) · başlık (iki seçenek aynı başlıkla) · üretim aracı ve ayarları
AN             A: çekim C04, 0,0-0,5 s (film 0:30,0-0:30,5; seçilen t = 0,3 s)
               B: çekim C04, ≈1,0-2,0 s (film ≈0:31-0:32). Noktanın siyah gökte kalıp Dünya'nın mavi kenarına
                  en çok yaklaştığı SON kare: nokta y ≥ %40 ve mavi kenarın ≥3 puan üstünde. Arama 0,5-2,5 s.
               (plandan seçildi. KAPAK ANI: C04 0,0-4,0 s kurguda kesilmez ve kırpılmaz)
               yedek çift (R1/R2): C02 0,5 s ↔ 7 s
TEK İLİŞKİ     160×90'da okunacak tek şey: soldaki beyaz kask/omuz lekesi ile sağdaki kehribar nokta
               arasındaki siyah boşluk. A'da nokta kask hizasında (y ≈%28). B'de ≈16-20 puan aşağıda
               (y ≈%44-48), mavi kenarın üstünde ve siyah gökte.
BOŞ ALAN       sağ alt köşe (süre rozeti) x %80-100 · y %84-100: yalnız Dünya'nın düz aydınlık yüzü
               alt şerit y %88-100: anlam taşıyan öğe yok (solda giysinin bel kesiti, sağda düz Dünya)
               başlık katmanı (sol üstten) x %50-96 · y %4-16: düz siyah gök, sönük yıldızlar; noktayla ≥12 puan
               (görsele film adı basılacak mı: F9'da yayin kararı; basılmazsa alan boş kalır)
               toplam boş alan ≈ %35-40 (sağ üst siyah gök x %42-100 · y %0-48 + sağ alttaki düz Dünya yüzü)
               ana renkler: siyah · beyaz · mavi-beyaz. Kehribar yalnız noktada; turuncu bant küçük.
FİNAL          faz 9: gerçek kare (C04 videosu; A/B promptları yalnız maket)
               → ~/film_medya/THE_WRONG_BURN/cikti/kapak_A.png · kapak_B.png
```

**Yerleşim (sol üstten %):**

| Öğe | x · A | x · B | y · A | y · B |
|---|---|---|---|---|
| Sela'nın kaskı (arkası) | %10-32 | aynı | %12-40 | aynı |
| Sela'nın gövdesi (bel üstü) | %0-42 | aynı | %30-100 | aynı |
| Kehribar nokta | ≈%74 | **≈%75-78** (sağa kayar) | **≈%28** (kask hizası) | **≈%44-48** (kaskın altı; mavi kenarın ≥3 puan üstü) |
| Dünya'nın mavi kenarı (ufuk), nokta sütununda | %0-100 | aynı | ≈%50 | **≈%51-52** (C04'te iner) |
| Başlık katmanı | %50-96 | aynı | %4-16 | aynı (A'da noktayla 12 puan, B'de ≥28) |
| Süre rozeti köşesi | %80-100 | aynı | %84-100 | aynı (yalnız düz Dünya) |

> B değerleri plan geometrisinden hesaplandı (FILM §4 C04: 7 s'de nokta belin çok altında; G01 Video: "the curved horizon
> … slips a little lower"). Gerçek değerler faz 9'da karede ölçülür.
> Nokta iki seçenekte de **siyah gökte** durur. Dünya'nın önüne düşerse gri tonlamada kaybolur (kehribar ≈ açık gri,
> Dünya ≈ açık gri), bu yüzden C04'ün 2 s sonrası ve 7 s karesi seçilmez.

**Duygu (yüzsüz kadraj, kural 7):** Kask ve omuz iki seçenekte de aynı: kıpırtısız, sağa ve derine dönük. Duyguyu
gövdenin kıpırdamaması ve kaskın yönü taşıyor. A'da nokta kaskın yüksekliğinde, karşıda. B'de kask aynı yöne dönükken
nokta onun çok altında. Sırttan bakışın nereye vardığı okunmaz (yayin B2). Bu yüzden B'nin "geride kalış" diye okunacağı
iddia edilmiyor; okunup okunmadığını deney ölçer. Vizör bu açıdan görünmüyor (FILM §4 C04 AĞIZ notu). Yüz, göz ya da
yansıma yazılmadı.

### Kapak A
`MAKET: yalnız yerleşim ön izlemesi, yayına girmez; FINAL = C04 video karesi (faz 9).`
`Araç: Görsel · 16:9 · 3840×2160 (araç ayarında; 4K yoksa en yüksek çözünürlük; ≥1280×720 şart) · referans: ref/SELA_arka_v1.png · ref/DUNYA_gunduz_alt_v1.png (C04 kare satırıyla aynı)`
`Çözünürlük prompta yazılmaz (§C: prompttaki sayı ve etiket kadraja basılabilir).`
```text
Photorealistic cinematic film still, 16:9 frame, natural colour. Medium-wide shot with a 35 mm lens from about three metres behind and to the right of a woman, camera at her head height. She fills the left of the frame from the waist up, seen from her right rear three-quarter: the back of her helmet and her right shoulder, in a white spacesuit with an orange band on each shoulder, the top of her backpack behind her shoulders. The helmet and the suit are one piece, the helmet facing the same direction as the suit. Her helmet sits in the upper-left part of the frame; she looks toward the right and deep into the distance, perfectly still. At the right-centre of the frame, level with her helmet, a small, distinct amber point of light against the black sky, the beacon lamp of a distant man. A wide gap of black sky lies between her helmet and the amber point. The upper right of the frame is open black sky with faint, dim white stars. The lower half of the frame is the fully lit face of planet Earth with its curved horizon edged with a thin blue rim, running just below the middle of the frame; the lower right corner holds only the plain, evenly lit face of Earth. Open space: a black sky with faint, dim white stars and planet Earth with a thin blue atmospheric rim; the vacuum keeps every edge crisp. The sun is high at the left, well above the horizon, about two-thirds of the way down from overhead: its hard white light picks out the upper-left edge of her helmet and shoulder, and her right side is softly lit by the glow of Earth.
```

### Kapak B
`MAKET: yalnız yerleşim ön izlemesi, yayına girmez; FINAL = C04 video karesi (faz 9).`
`Araç: A ile aynı (araç, ayar, referans, ölçekleme). Metin A'nın birebir aynısı; yalnız nokta cümlesi ve ardından gelen boşluk cümlesi değişir.`
```text
Photorealistic cinematic film still, 16:9 frame, natural colour. Medium-wide shot with a 35 mm lens from about three metres behind and to the right of a woman, camera at her head height. She fills the left of the frame from the waist up, seen from her right rear three-quarter: the back of her helmet and her right shoulder, in a white spacesuit with an orange band on each shoulder, the top of her backpack behind her shoulders. The helmet and the suit are one piece, the helmet facing the same direction as the suit. Her helmet sits in the upper-left part of the frame; she looks toward the right and deep into the distance, perfectly still. At the right of the frame, well below the level of her helmet and just above the thin blue rim of Earth's curved horizon, still against the black sky, a small, distinct amber point of light, the beacon lamp of a distant man. Her helmet faces level toward the right, above the amber point, and a tall gap of black sky lies between the line of her helmet and the point below it. The upper right of the frame is open black sky with faint, dim white stars. The lower half of the frame is the fully lit face of planet Earth with its curved horizon edged with a thin blue rim, running just below the middle of the frame; the lower right corner holds only the plain, evenly lit face of Earth. Open space: a black sky with faint, dim white stars and planet Earth with a thin blue atmospheric rim; the vacuum keeps every edge crisp. The sun is high at the left, well above the horizon, about two-thirds of the way down from overhead: its hard white light picks out the upper-left edge of her helmet and shoulder, and her right side is softly lit by the glow of Earth.
```

> Promptlar _1 ile aynı. Fable kararlarından hiçbiri prompt metnini değiştirmiyor. Maket olarak ufkun B'deki 1-2 puanlık
> inişi prompta yazılmadı: bu fark promptla kurulamaz, final karede kendiliğinden gelir.
> Sözcük denetimi: kimlik cümlesi G01 C04 Görsel + SELA_arka_v1 ile birebir, dünya cümlesi "Open space: …" birebir,
> güneş cümlesi G01 C04 Görsel ile birebir (FILM §4 SAPMA 4; yayin B5 RED). Ad, çekim kodu, referans kodu, büyük harfli
> etiket, "text/title/logo" sözcüğü ve olumsuz liste yok. Sayı yalnız G01 ile ortak iki teknik ifadede: "16:9 frame",
> "35 mm lens" (§C yasak listesinde değil). §A red kelimesi yok. Uzunluk ≈1.650 karakter (A) · ≈1.750 (B), ≤4.300.
> C04 Görsel'den tek sapma kadraj yeri: "helmet in the upper-left part", "point against the black sky", sağ üst ve sağ alt
> boşluk cümleleri. Maket olduğu için kabul. "distinct" G01 C02'den geliyor.

### Görünen tarif (izleyici için, yalnız görülen)

| | EN (yayın dili) | TR |
|---|---|---|
| A | An astronaut in a white suit with orange shoulder bands, seen from behind at the left, faces right; far off to the right, at helmet height, a small amber light hangs in the black sky above a bright Earth. | Turuncu omuz bantlı beyaz giysili bir astronot solda, arkadan görünüyor, sağa dönük; sağda, uzakta, kask hizasında küçük kehribar bir ışık siyah gökte duruyor, altta aydınlık Dünya. |
| B | An astronaut in a white suit with orange shoulder bands, seen from behind at the left, faces right; far off to the right, well below helmet height, a small amber light hangs in the black sky just above Earth's blue horizon. | Turuncu omuz bantlı beyaz giysili bir astronot solda, arkadan görünüyor, sağa dönük; sağda, uzakta, kask hizasının çok altında küçük kehribar bir ışık siyah gökte, Dünya'nın mavi ufkunun hemen üstünde duruyor. |

> İki tarif artık aynı iskeletle yazılı ve yalnız ışığın yüksekliği değişiyor. _1'deki A "faces a small amber light"
> ifadesi bakışın nereye gittiğini söylüyordu, görünen şey değildi; "faces right" oldu.

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
