# F5 · devamlilik (eleştirmen) · tur 1 — THE_WRONG_BURN G01

> Girdi: PROMPTLAR/G01.md (tam) + FILM §3 §4. Ajanın cevabı aynen (Fable kaydı, 09.10.2026).

## Faz 5 · tur 1 · devamlilik · THE_WRONG_BURN G01

### B1 · CİDDİ · C10 başlangıç karesine bitiş durumu referansı bağlı
KANIT    FILM §3: `BRAM_kolkalkik_v1 … Kullanan çekimler: C10 (son)`. G01 FLOW İŞ EMRİ satır 30 (C10 kare, Görsel) ve C10 `EKLE (a)`: `ref/BRAM_v1.png · ref/BRAM_kontrolsuz_v1.png · ref/BRAM_kolkalkik_v1.png · ref/KANCA_cantada_v1.png`. C10 Görsel: `the left arm, nearest the camera, hangs loosely half-open at his side`.
NEDEN    Kolu kalkık referans başlangıç karesine sızarsa video "kalkış" eylemini atlar (görsel ↔ video sınıfı). Üç Bram referansı üç ayrı duruş taşıyor (dik / yarı açık / kol kalkık). FLOW_GERCEKLERI §5 karakter için 1-2 görsel diyor.
ARIZA    T05 · T09 · görsel ↔ video (yeni örnek)
ÖNERİ    Satır 30'dan `BRAM_kolkalkik_v1` ve `BRAM_v1`'i çıkar. Kalan: kontrolsuz + KANCA_cantada + DUNYA_alcak_ust. `BRAM_kolkalkik` yalnız satır 31'e (C10_bitis) girsin. C10 `EKLE (a)` satırını "başlangıç üretimi" ve "bitiş üretimi" diye ikiye böl.
Bu uygulanmazsa ve F7 karesinde kol kalkıksa bulgu ÖLÜMCÜL'e çıkar.

### B2 · CİDDİ · SELA_v1 iki durum taşıyor: bilek 0/4 ve kanca kalçada kenetli
KANIT    SELA_v1: `a row of four round recessed bays on her right wrist, all four dark hollows` ve `A short rope with a hook, clipped to the metal ring at her right hip`.
- İş emri satır 21 (C03): `SELA_v1 + BILEK_2-2`. Satır 25 (C07): `SELA_v1 + BILEK_1-3`.
- C06: `Her right glove grips the flat, matte, unmarked control box on her chest`. Bilek görünür, tek referans SELA_v1.
- C11/C12: `a hook caught in the bent frame` ve `a rope running perfectly straight from the ring at her waist to him`.

NEDEN    C03 ("dört yuvadan ikisi yanıyor") ve C07 ("1/3") tek-bilgilik çekimler. Ana referans bu bilgiyi yalanlıyor. Merdiven ters: filmin bitiş durumu (0/4, kanca Sela'da) kimlik karesine gömülü. C11-C12'de kanca zaten Bram'da.
ARIZA    T09 · T05
ÖNERİ
- SELA_v1'de bilek göstergesi yok (düz kılıf) ve kalçada yalnız boş halka olsun (`a bare metal ring at her right hip`, Bram'ın halkasıyla aynı kalıp). İp ve kanca KANCA_ referanslarından gelir.
- C03 satırından SELA_v1'i çıkar. C07'de yalnız yüz için kalsın. Gösterge ancak BILEK_ referansından gelsin.
- C06'da bilek görünüyorsa 2/2 → 1/3 geçişi için BILEK_2-2 ekle. Görünmüyorsa bunu FILM satırına yaz.

### B3 · CİDDİ · C12 kamerası C01 ve KAPAK referansıyla aynı yazılmamış, ayrıca kendi içinde çelişiyor
KANIT
- FILM §4 C12: `C01 ile aynı korkuluk ve kopuk uç ilişkisi`.
- KAPAK_iki_uc_v1 ve C01: `camera at handrail height at the edge of an open hatch of a space station, looking outward`.
- C12: `24 mm lens from inside an open hatch looking outward, camera at chest height`.
- C12 iç çelişki: `In the nearest plane, the plain, matte, unmarked metal rim of the hatch` ile `her right glove grips a grab handle on the hatch rim ahead of her, her forearm running continuously from the glove away from the camera to her shoulder`.
- C01: `both gloves gripping a grab handle` (hangisi olduğu yok). S12 ise "S1'deki kapağın tutamağı" diyor.

NEDEN
- Ödeme karesinde (S1'in yankısı) korkuluk ve kopuk uç, ref'teki kamera konumundan farklı çıkar.
- Rim en yakın düzlemde ise tutamak Sela'nın "önünde" (derinde) olamaz.
- Ön kol eldivenden omuza kameradan uzağa gidiyorsa eldiven kameraya yakın, yani tutamak Sela'nın arkasındadır.
- Model tutamağı bir yere koyar, kol kopuk ya da uzamış görünür.

ARIZA    T09 · T11 · T01
ÖNERİ
- "from inside an open hatch looking outward, camera at chest height" yerine `camera at handrail height at the edge of the open hatch, looking outward` yaz (ref ile birebir).
- "ahead of her" yerine `her right glove reaches back to the grab handle on the hatch rim nearer the camera, her forearm running continuously from the glove away from the camera to her shoulder` yaz.
- C01'de tutamağı kapak kenarına bağla: `a grab handle on the rim beside the handrail`.

### B4 · CİDDİ · Işık merdiveni: C04 ile C05 aynı sözcüğe düşüyor, referans ışığı metni yalanlıyor
KANIT
- FILM C04: `güneş zenitten ≈65° geride … yatığa yakın`. FILM C05: `≈85° geride … yataya yakın`.
- G01 C04: `The sun is low at the left, almost grazing` ve `The lower half of the frame is the fully lit face of planet Earth`.
- G01 C05: `The sun is almost level with the horizon, far behind her at the left`.
- C04'e bağlı ref DUNYA_gunduz_alt_v1: `The sun is directly overhead`.
- C01'e bağlı ISTASYON_v1: `Hard white sunlight arrives from the upper left`. C01 metni: `The sun is directly overhead`.

NEDEN
- Zaman geçişi ışık yönünden okunacaktı (T18), ama 65° ile 85° aynı kelimelerle yazılmış.
- "Grazing" ile "tam aydınlık Dünya" aynı promptta tutmaz; yatık güneşte Dünya alacakaranlığa gider (C05'in dünyası).
- Referans ve metin iki farklı güneş söylüyor.

ARIZA    T18 · T04
ÖNERİ
- C04: "almost grazing" ve "low" sil. Yerine `The sun is high at the left, well above the horizon, about two-thirds of the way down from overhead` yaz. Gerisi aynı kalsın.
- ISTASYON_v1: güneş cümlesini `from directly above` yap (C01 zenit). C11'de ışığı metin taşır.

### B5 · CİDDİ · İp uzunluğu hiçbir yerde tanımlı değil, "short" ile "one rope length" çelişiyor
KANIT
- SELA_v1: `A short rope with a hook`.
- KANCA_bosta_v1: `a short rope that floats in a slack, loose curl`. C02 aynı.
- C09: `two person-heights beyond the open glove`.
- C12: `one rope length away`.
- FILM S10: `ip tam boyunda`. S9: "tek araç ipin boyu".

NEDEN
- Model "short"u yaklaşık 1 m okur. Ama ıska 2 insan boyudur ve tam boy gergin ip bunu aşmalıdır.
- S9-S10'un tek aracı ipin boyuysa boy bir kez ölçüye bağlanmalı. Şimdi C10-C12'de "taut" var, boy yok.

ARIZA    T09 (nesne sürekliliği)
ÖNERİ    SELA_v1, KANCA_bosta ve C02'de `short rope` yerine `a rope about four person-heights long, coiled in a slack loose curl`. C10, C11, C12 ve KANCA_cantada'da `a rope about four person-heights long, perfectly straight and taut`. C12'deki "one rope length away" olduğu gibi kalır.

### B6 · CİDDİ · C05 yakın planında yüz tek ve küçük bir referanstan geliyor
KANIT    SELA_v1: `portrait framing, mid-thigh up`. C05: `Close-up with an 85 mm lens from about one metre`; iş emri satır 23 referansları: `ref/SELA_v1.png · ref/DUNYA_alacakaranlik_alt_v1.png`. Karakter referansı sınırı 1-2 görsel (FLOW_GERCEKLERI §5), ikinci slot boş.
NEDEN    Filmin tek yakın tepki karesi (gözler kapanıyor) yüzü SELA_v1'den çekiyor, oysa yüz o karede küçük. Kimlik kayması riski. C07'de yüz de küçük.
ARIZA    T16
ÖNERİ    19. referans: `SELA_yuz_v1`, "head-and-shoulders, ¾ front, 85 mm, clear visor, aynı kimlik cümlesi". C05 (ve C06) EKLE'ye ekle. FILM §3 tablosuna satır aç.

### B7 · CİDDİ · C10 başlangıcında sol kol ile ip aynı ekran bölgesinde
KANIT    C10 Görsel: `a hook is caught in that bent frame` (sol yan), `from the hook a rope runs perfectly straight and taut, down and to the left` ve `the left arm, nearest the camera, hangs loosely half-open at his side`. Bitiş: `open empty space between the arm and the rope below it`.
NEDEN
- El-ip kaynaşması en sık hata (T01).
- Başlangıçta kolun ipe göre yeri yazılı değil.
- Kol "ipin altından" kalkarsa ipi keser. Bitişte kol ipin üstünde.

ARIZA    T01
ÖNERİ    Başlangıç cümlesi: `the left arm floats close against his side, above the line of the rope, a hand's width clear of it` (kalkış ipi geçmez). "hangs" kelimesi B9'a göre değişir.

### B8 · KÜÇÜK · Bram'ın kehribar lambası: konum çelişiyor, C10 ve C12'de hiç yok
KANIT
- BRAM_v1, BRAM_kontrolsuz, C09: `a small amber beacon lamp on top of the helmet, always lit`.
- C08: `a small amber point at the centre of the helmet`.
- C10: `A man in a white spacesuit with a blue band on each shoulder` (lamba yok).
- C12: `a man seen from behind in a white spacesuit with a blue band on each shoulder, upright …` (lamba yok).

NEDEN    C08'de ref "tepede", metin "ortada". C10 ("ayılıyor") ve C12'de "hayatta" işareti kimlik cümlesinden düşmüş.
ARIZA    T05
ÖNERİ    C08: "at the centre of the helmet" yerine `on top of the helmet`. C10 ve C12'ye `a small amber beacon lamp on top of the helmet, always lit` ekle.

### B9 · KÜÇÜK · Ağırlıksız nesnede "hangs / hanging"
KANIT    KANCA_bosta: `the hook at its free end hangs open`. C02: `the hook at its end hangs free`. C08: `two arms hanging half-open outward`. C10: `hangs loosely half-open at his side`.
NEDEN    Model aşağı sarkma çizer (T08), oysa kanca ve kollar süzülüyor.
ARIZA    T08
ÖNERİ    "hangs / hanging" yerine `floats` yaz.

### B10 · KÜÇÜK · C07'de ağız durumu yazılmamış
KANIT    C07 Görsel'de "lips" yok. SELA_v1, C02 ve C05'te `lips closed` var. FILM §5 replik 10, C07 1,5 s, kask içi: "Bram?".
NEDEN    Yüzü görünen tek çekimde ağız belirsiz; model dudak oynatabilir (replik zaten kurguda).
ARIZA    yeni
ÖNERİ    C07 Görsel yüz cümlesine `lips closed` ekle.

### B11 · KÜÇÜK · Sela'nın donanım adları tutmuyor
KANIT
- SELA_v1 ve KANCA_bosta: `the metal ring at her right hip`. C11 ve C12: `the metal ring at her waist`.
- SELA_v1: `a row of four round recessed bays on her right wrist`. BILEK_2-2: `A wide wrist band carries a row of four round recessed bays`.

NEDEN    Halka yeri ve bilek bandı iki ayrı tarifte; "wide wrist band" kimlikte hiç yok.
ARIZA    T05
ÖNERİ    Her yerde `at her right hip`. SELA_v1 bilek cümlesine `on a wide wrist band` ekle (B2'deki yeniden yazımla birlikte).

### B12 · KÜÇÜK · "band" üç ayrı nesne için kullanılıyor
KANIT    C08 aynı promptta: `an orange band on each shoulder` ve `a thin orange-and-blue band glows along the edge`. Ayrıca BILEK: `A wide wrist band`.
NEDEN    Ufuk bandının renkleri omuz bandına ya da siluete kayabilir.
ARIZA    T05
ÖNERİ    Ufuk için `a thin orange-and-blue glow along the edge` (DUNYA_dogus_ust, DUNYA_ikinci_dogus, C08, C12). "band" yalnız omuz ve bilek bandı için kalsın.

### B13 · KÜÇÜK · C11'de Bram'ın bakış yönü yazılmamış
KANIT    C11: `a man in a white spacesuit with a blue band on each shoulder, upright, arms at his sides, legs together, a hook caught in the bent frame on the left side of his backpack`. C10: `turned away from the camera toward the left of the frame`. C12: iki figür derine bakıyor.
NEDEN    C10'da Bram sola bakıyor. C11'de yön yazılı değil, "helmet facing the same direction as the suit" da (BRAM_v1'de var) yok. Model Bram'ı Sela'ya ya da istasyona çevirebilir.
ARIZA    T11
ÖNERİ    C11'e `facing the left of the frame, the helmet facing the same direction as the suit` ekle.

KORU
- Dünya cümlesi `Open space: a black sky with faint, dim white stars and planet Earth with a thin blue atmospheric rim; the vacuum keeps every edge crisp.` C01-C12'nin on ikisinde de birebir aynı.
- Bram'ın "sol yanı ezik çanta" ve mavi/turuncu omuz bantları C01, C09, C10, C11, C12'de aynı sözcüklerle geçiyor.
- Sela'nın kimlik cümlesi (turuncu bant, `clear visor over a dark, plain helmet interior`) kayma yok.
- Ekran yönleri (C02 sağ, C06-C09 sol, C05'te sağdan sola dönüş) FILM §4 "Taraf / yön" ile uyuşuyor.
- FILM §3 "Kullanan çekimler" ile G01 EKLE satırları C10 `BRAM_kolkalkik` dışında birebir eşleşiyor.

BULGU YOK
- Meta etiket: gövdede çekim kodu, "Clip n of N", başlık satırı veya başka çekime atıf yok.
- Şiddet kelimeleri: `body`, `dead`, `blood` vb. gövdede geçmiyor (grep ile baktım).
- Sayı: "four bays", "two ropes", "two bands" dış tutarlı. C03'te rakamsızlık bilerek.
- Gruplar arası: tek grup var, sınır geçişi yok.

KAPSAM DIŞI: güneşin batış ve doğuş yönünün yörünge fiziği, Veo 8/10 s yöntemi (P14), kurgu ve ses.

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 7 · KÜÇÜK 6
KARAR    TUR KAPANABİLİR (B1 ve B2 uygulanmadan F7 karesine geçilmesin; B1 uygulanmaz ve kare kolu kalkık çıkarsa ÖLÜMCÜL)
GİRDİ    uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md (tam) · yatay_2_dk_filmler/THE_WRONG_BURN/FILM.md (§1-§7, tam) · PROMPTLAR/G01.md (tam: 18 referans + C01-C12 + FLOW İŞ EMRİ + YAZAR NOTLARI) · ARIZA_LISTESI.md (H/T satırları) · FLOW_GERCEKLERI.md §5 (karakter görseli)
YAPILMADI  Faz 7 kare denetimi (kare/ ve ref/ dosyaları bu fazda yok) · film_dogrula.py çalıştırılmadı · PROMPT_HATA_ATLASI.md açılmadı · ODA/ dosyaları okunmadı (bağımsızlık)
```
