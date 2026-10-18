# MOONMOTHER G01 (C01-C08 + REFERANS PROMPTLARI): devamlılık eleştirisi, Faz 5 tur 1

Tabloda emoji yerine harf kullandım: OK = uygun, X = bulgu var, — = bu çekimde yok.

## 8 soru tablosu

| Çekim | 1 işaret | 2 kimlik birebir | 3 ortak cümle | 4 açıklığın ardı | 5 akışkan | 6 ekran + kilit | 7 referans rolü | 8 ses · zıt istek |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| C01 | OK | OK | OK | OK | OK | OK | OK | OK |
| C02 | OK | OK | X (B4) | OK | OK | OK | X (B7) | OK |
| C03 | X (B9) | OK | OK | OK | OK | OK | OK | OK |
| C04 | OK | OK | OK | OK | OK | OK | OK | X (B2) |
| C05 | OK | OK | X (B4) | — | OK | OK | OK | OK |
| C06 | X (B1) | OK | OK | OK | OK | OK | OK | X (B1) |
| C07 | OK | OK | OK | OK | OK | OK | OK | OK |
| C08 | OK | OK | OK | OK | OK | OK | OK | X (B10) |

## Sorular tek tek (evet/hayır · kanıt)

1. **İşaret sayı + taraf + konum ile yazılı mı?**
   - Hayır, üç yerde eksik: C03, C04 ve C06.
   - Khev'in tek işareti sol kaval. Bacağın kadrajda olduğu 5/5 çekimde var (`G01.md` 89, 167, 201, 271, 342). Sayı `one`, taraf `left`, konum `shin plate`.
   - Oru çentiği C02'de (127). `the only amber lights on it` C02, C04 ve C08'de (127, 201, 342). Annenin `the only lights on her head` C03, C05, C06 ve C07'de.
   - Eksikler: dev manta yüzgeç tarafı C03 ve C04'te (B9). Oru'nun görünen yüzgeç tarafı C06'da (B1).

2. **Kadrajdaki her öznenin kimlik cümlesi §3 ile birebir mi?**
   - Evet, 8/8 çekimde. Kelime kelime karşılaştırdım: her cümle `FILM.md` §3 tablosuyla eşleşti. Satır numaraları:
     - Khev ¾ yüz: 125, 201, 342. Khev arkadan: 89, 167, 271.
     - Khev gövde: 89, 125, 167, 201, 271, 342. Khev sol kaval: 89, 167, 201, 271, 342.
     - Oru gövde: 89, 127, 167, 201, 271, 342. Oru baş ve ışık: 127, 201, 342.
     - Oru kucak: 127, 201, 271, 342. Oru arkadan siluet: 271.
     - Anne baş zırhı: 93, 165, 237, 275, 308. Anne göz: 93, 129, 165, 237, 275, 308. Anne üç ışık: 165, 237, 275, 308. Anne yüzgeç ve kuyruk: 165, 205, 275, 308.
     - Kemer, kemer ağzı ve teras: 91, 169, 203, 273, 306, 340. Alt çıkıntı ve çıkıntı yüksekliği: 340.
   - Kimlik cümlesinden kaynaklanan sapma yok. Sorun cümlelerin dışında (B3, B13, B14).

3. **Ortak cümle çekimle çelişen ışık, gezegen ya da ses taşıyor mu?**
   - ORTAK GÖRÜNÜM 16/16 prompt sonunda birebir (satır 97, 102, 133, 138, 173, 178, 209, 214, 241, 246, 279, 284, 312, 317, 346, 351). İçinde ışık, su, gezegen veya ses yok.
   - Gök ve ufuk cümlesi 6 çekimde var (C01, C03, C04, C06, C07, C08). C02 ve C05'te yok. Işık cümlesi 8/8'de var. Yalnız C02 ve C05'te gaz devi tanıtılmadan anılıyor (B4).

4. **Görünen her açıklığın ve kişinin arkası bu promptta yazılı mı?**
   - Evet. Kemer ağzının ardı (`dark stone inner wall`) kemerin göründüğü 6/6 çekimde var (91, 169, 203, 273, 306, 340).
   - C01'de göz kapağı aralığının ardı yazılı: `through which the amber eye and its dark pupil can be seen`.
   - C02'de Khev'in arkası `blurred black basalt shore`, eller kadraj dışı.
   - C05'te açıklık yok.

5. **Akışkan, ateş ya da su çağıran kelime var mı?**
   - Hayır. `smoke/steam/mist/fog/vapor/plume/exhaust/drip/splash/bubble/wet/rain/flame/droplet/soot` 0/16 promptta. Bunlar `film_dogrula.py` AKISKAN deseni (satır 88-89) ve sizin Y5 listenizdir.
   - Kalan sıvı kelimeler `cloud`, `ridge`, `spray`, `sea` (C07, C08). Atmosferli dünyada kullanılıyor, `FIZIK_IDDIASI yok`.

6. **Ekran adıyla mı yazılmış, yazı kilidi var mı?**
   - Ekran, gösterge ve HUD kelimesi yok. `plain unmarked surfaces` 16/16'da var, kemerde `no symbols` 7/7'de var.
   - Sayfa promptlarında olumsuz yazı kilidi duruyor (B12).

7. **Her `Reference n (rol)` yalnız o sayfada görüneni mi istiyor?**
   - C02 hariç evet.
   - Sayı, sıra ve rol 8/8'de `EKLE` ve `FILM.md` §3 ile eşleşiyor. Her cümle sayfadaki bir paneli adlandırıyor ve en çok 3 referans var.
   - C02'de eller kadraj dışıyken el paneli isteniyor, odak dışı parıltı için de baş paneli isteniyor (B7).

8. **Video'da ses kelimesi ya da aynı promptta zıt iki istek var mı?**
   - Ses kelimesi yok: 0/8 (satır 102, 138, 178, 214, 246, 284, 317, 351). `slow` en çok 1 kez.
   - Zıt istek var: C04 (B2), C06 (B1), C08 (B10).

## Bulgular

### B1 · CİDDİ · C06: Oru'nun görünen yüzgeci kucak yönüyle ve kendi durum cümlesiyle çelişiyor
```
YER       G01.md:271 (C06 Görsel) · G01.md:284 (C06 Video 0-4 s) · FILM.md:186 (§4 C06)
KANIT     "Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso."
          "Oru's head and right fin stand out as a clear outline against the night sky beside Khev's right shoulder, the right fin hanging half open and the left fin folded against its side."
          Video: "Oru lifts its right fin fully open beside Khev's shoulder while its left fin stays folded"
ETKİ      Arkadan bakışta karnı Khev'in göğsüne dönük Oru'nun Khev'in sağ omzunun yanında görünen yüzgeci SOL yüzgeçtir (çentikli, sonradan yaralı olan). Metin sağ yüzgeç istiyor.
          Model ya yanlış yüzgeci kaldırır ya da Oru'yu Khev'in gövdesi arkasında bırakır. Pilot sorusu (akrabalık siluetten okunacak) bununla ölçülür.
          Ayrıca "both fins half closed" ile "left fin folded" aynı promptta çatışıyor. "hanging half open" ise sol yüzgecin yaralı durumunun dili (FILM.md:141).
DOĞDUĞU   metin
KURAL     devamlilik.md:51 "Taraf ve yön: asimetrik işaretler (hangi kol)" [SÖZLEŞME] · FILM.md:142 kucak duruşu
ARIZA     T11 (yön/taraf) · T05 (yüzgeç durumu)
DÜZELTME  `beside Khev's right shoulder, the right fin hanging half open and the left fin folded against its side`
          → `beside Khev's left shoulder, the right fin half open and the left fin folded against its side`
          (Video'daki "beside Khev's shoulder" taraf-nötr, değişmez.)
          Fable'a not: FILM.md:186 "Khev'in sağ kolunda … sağ omzunun yanında" → "sol kolunda … sol omzunun yanında" plan sapmasıdır, sahip onayı gerekir.
          Sol omuz kabul edilmezse yeni cümle: "left fin" görünür yüzgeçtir. O zaman Video'da kaldırılan yüzgeç de sol olur ve plan S6 ("sağ yüzgeç") değişir.
```

### B2 · CİDDİ · C04: Video 7-10 s'de Oru Khev'in göğsünde, ama kollar "Oru ile deniz arasında" perde oluyor
```
YER       G01.md:214 (C04 Video 7-10 s) · G01.md:201 (C04 Görsel)
KANIT     Görsel: "his chest and face turned toward the dark sea at the right of the frame" + "Khev presses Oru against his chest with both forearms"
          Video 0-4 s: "while his chest and face stay turned toward the sea at the right"
          Video 7-10 s: "so that his arms and shoulders form a screen between Oru and the sea"
ETKİ      Oru göğüste ve göğüs denize bakıyor. Oru zaten Khev ile deniz arasında, perde Oru'nun denize bakan tarafında olamaz.
          Model Khev'i döndürür (göğsü artık denize dönük değil, çekimin tek yön kuralı bozulur) ya da kolları saçma bir yere koyar. Çekimin tek bilgisi olan koruma jesti bu cümleye bağlı.
DOĞDUĞU   metin
KURAL     devamlilik.md:54-58 "Çelişki" ve :59-62 "Görsel ↔ video" [SÖZLEŞME]
ARIZA     T10 (sebepsiz dönüş)
DÜZELTME  `so that his arms and shoulders form a screen between Oru and the sea.`
          → `so that his arms and bowed shoulders close around Oru.`
```

### B3 · CİDDİ · 4.KIYI sayfası ile çekim cümleleri aynı derinliği iki farklı ölçüyle tarif ediyor
```
YER       G01.md:72 (4.KIYI sayfa promptu, master panel) · G01.md:340 (C08 Görsel) · FILM.md:106 ve :154
KANIT     Sayfa: "a drop about as deep as the arch is tall"
          C08: "The lower ledge lies about twice Khev's height below the end of the causeway."
          FILM.md:106: "alt çıkıntı orta-sağda Khev boyunun yaklaşık iki katı aşağıda"
ETKİ      Kemer yüksekliğinin Khev'e oranı hiçbir kimlik cümlesinde ve hiçbir promptta yok. Sayfada Khev da yok.
          Referans görsel "çıkıntı = kemer yüksekliği" öğretir, metin "çıkıntı = 2 × Khev" der. Kemer Khev'in 4 katıysa C08 çıkıntıyı 4 katı derinlikte çizer.
          Atlayış (C13) ve dik duvar (C14, C16) bu coğrafyadan türer.
DOĞDUĞU   metin (F3p referans sayfası)
KURAL     GPT_IMAGE_OMNI_KILAVUZU.md:111 "Mekân ve coğrafya bir kez kurulur; yakın planlar bu coğrafyadan türer" [SÖZLEŞME]
ARIZA     T04 (coğrafya) · T11
DÜZELTME  Sayfa promptunda: `a drop about as deep as the arch is tall`
          → `a drop about twice the height of a standing biped, about as deep as the arch is tall`
          (kemer ≈ çıkıntı farkı ≈ 2 × Khev tek ölçüde bağlanır.)
          C08 KARE KABUL'e ekle: "kemer yüksekliği ≈ çıkıntı farkı ≈ Khev'in iki katı".
          Daha sağlam yol: FILM.md §3 No 4 kemer cümlesine `Its opening is about twice Khev's height.` eklemek. Bu cümle 7 promptta birebir gider.
```

### B4 · CİDDİ · C02 (açılış) ve C05: ışık cümlesi gaz devini anıyor, ama gök cümlesi yok ve gaz devi tanıtılmıyor
```
YER       G01.md:129-131 (C02 Görsel) · G01.md:239 (C05 Görsel) · FILM.md:156-157 ve :172
KANIT     C02: "High at the upper right, far out of focus, hangs the eye of the mother manta." (129) +
              "The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, ..." (131)
          FILM.md:172: "MEKÂN IŞIĞI ve GÖK (birebir, her dış çekim): … 'gök ve ufuk' + 'ışık' satırları"
ETKİ      C02'de gaz devi hiçbir yerde tanıtılmadan "the gas giant's … from the upper right" deniyor. Model sağ üste halkalı bir gezegen çizebilir.
          Orası odak dışı amber yuvarlağın yeri, dolayısıyla "ikinci göz" kare kapısı düşer. C02 açılış çekimi (ILK_30 §6), deneme hakkı en çok orada.
          C05'te gökyüzü kadrajda yok, risk daha küçük, ama aynı atıf var.
DOĞDUĞU   metin
KURAL     FILM.md:156-157 + :172 [SÖZLEŞME] · goruntu-yonetmeni.md:113 (soru 3)
ARIZA     T18 (gök/ışık) · T15 (ikinci yuvarlak)
DÜZELTME  C02 (131) ve C05 (239):
          `the gas giant's thin pale rim light from the upper right`
          → `a thin pale rim light from the upper right`
          Birebir ölçülebilsin diye FILM.md §3 No 4'e ayrı bir satır ekle: "ışık — gaz devi kadraj dışı: The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence."
```

### B5 · KÜÇÜK · C01 ve C03: arkadan çekimde Oru "göğsünde" okunacak deniyor, taşınma tarafı yazılı değil
```
YER       G01.md:89 (C01 Görsel) · G01.md:167 (C03 Görsel)
KANIT     "At this distance Oru reads only as a small teal shape against his chest." (C01)
          "At this distance Oru reads only as a tiny teal shape against his chest." (C03)
ETKİ      Kamera Khev'in arkasında. Göğüsteki Oru gövdenin arkasında kalır, görünmez. AÇILIŞ tablosunun "üç varlık bir karede" iddiası (FILM.md:231) düşer.
          Model Oru'yu uydurur (kolun üstünde, havada). C06'daki taraf B1'in düzeltmesine bağlı olduğundan üç arkadan çekimde Oru'nun taşındığı yan farklı kalır.
DOĞDUĞU   metin
KURAL     devamlilik.md:63-66 "Tutan ve bağlantı" [SÖZLEŞME]
ARIZA     T09 (sürekliliğin yan bilgisi)
DÜZELTME  C01: `a small teal shape against his chest` → `a small teal shape beside his left shoulder`
          C03: `a tiny teal shape against his chest` → `a tiny teal shape beside his left shoulder`
          (Yan, B1'deki kararla aynı olmalı.)
```

### B6 · KÜÇÜK · C04: "sideways step" ile "toward the arch" yön olarak çelişiyor
```
YER       G01.md:214 (C04 Video 0-4 s) ↔ G01.md:201
KANIT     "takes one careful sideways step: the foot nearer the arch lifts, moves toward the arch and plants on the basalt, while his chest and face stay turned toward the sea at the right"
ETKİ      Khev sağ yanı kameraya, göğsü sağa dönük. Kemer solda, yani arkasında. Kemere atılan adım yan adım değil geri adımdır. Model dönüp yürümeye kayar (FILM T10 riski).
DOĞDUĞU   metin
KURAL     devamlilik.md:51 "ekran yönü, kamera tarafı" [SÖZLEŞME]
ARIZA     T10 · T11
DÜZELTME  `one careful sideways step` → `one careful backward step`
```

### B7 · KÜÇÜK · C02: eller kadraj dışıyken el paneli isteniyor, odak dışı parıltı için baş paneli isteniyor
```
YER       G01.md:123 (C02 Görsel, rol cümleleri) · G01.md:125
KANIT     "using the three-quarter face panel and the forearm-and-hand panel"
          "His two forearms … run out through the lower edge of the frame, so his hands stay outside the frame."
          Reference 3: "take only the colour and the round shape of her open amber eye from it, using the panel of the head with the eye fully open"
ETKİ      Açılış çekiminde parmak sayısı ve el kaynaşması ek ölçüt (ILK_30 §6). El paneli modeli elleri çizmeye iter.
          Tek bir odak dışı glow için dev mantanın bütün baş paneli verilince bulanık yuvarlağın yerine zırhlı bir baş çıkabilir.
DOĞDUĞU   metin
KURAL     GPT_IMAGE_OMNI_KILAVUZU.md:140 "Eller ya tam görünür ya kadraj dışı" · KIMLIK_VE_REFERANS_KILAVUZU.md:37 [TERCİH]
ARIZA     T01 · T15
DÜZELTME  `using the three-quarter face panel and the forearm-and-hand panel` → `using the three-quarter face panel`
          d1'de yuvarlak yerine baş çıkarsa Reference 3 cümlesi atılır, EKLE "ref 1,2" olur (Faz 7'de karar).
```

### B8 · KÜÇÜK · C02 KARE KABUL, açılış ek ölçütlerinden filigran/logo ve eli yazmıyor
```
YER       G01.md:142-144 (C02 KARE KABUL)
KANIT     "… renk ayrımı teal Oru / indigo deri / fildişi plaka · yazı yok · 16:9 piksel"
          (C01 ve C03'te "yazı/logo/filigran yok (ILK_30 §6)" var.)
ETKİ      C02 üç açılış çekiminin biri. Filigran ve köşe işareti kare kapısında bakılmazsa video üretilir, sonra "açılışta kullanılamaz" çıkar.
DOĞDUĞU   metin
KURAL     ILK_30_SANIYE_KILAVUZU.md:96-103 [SÖZLEŞME]
ARIZA     T17
DÜZELTME  `· yazı yok · 16:9 piksel` → `· yazı/logo/filigran/köşe işareti yok (ILK_30 §6) · kadrajda parmak yok · 16:9 piksel`
```

### B9 · KÜÇÜK · C03 ve C04: kadraja giren dev manta yüzgecinin tarafı yazılı değil
```
YER       G01.md:165 (C03 Görsel) · G01.md:205 (C04 Görsel)
KANIT     "Of these only the curved tip of one fin is in the frame"
          "High at the upper right the long curved edge of one immense silver-blue fin of the mother manta crosses the star field."
ETKİ      Tretman S19 bu yüzgeci "S3'te yıldızları örten aynı sol yüzgeç" diye geri çağırıyor (FILM.md:65). Sol yüzgeç çanaklı olan, kimlik işareti (FILM.md:148). C03 ve C04'te taraf yazılmadığı için hangi yüzgeç olduğu modele kalıyor.
DOĞDUĞU   metin
KURAL     devamlilik.md:51 [SÖZLEŞME] · FILM.md:65 ve :148 [TERCİH]
ARIZA     T09
DÜZELTME  C03: `the curved tip of one fin` → `the curved tip of her left fin`
          C04: `edge of one immense silver-blue fin of the mother manta` → `edge of her immense silver-blue left fin`
```

### B10 · KÜÇÜK · C08: yavaş itme ile "yerlerini korur" aynı promptta
```
YER       G01.md:351 (C08 Video)
KANIT     "the camera makes a very slow push-in toward the arch and the causeway" + "The arch, the causeway and the ledge keep their places in the frame throughout."
ETKİ      İtme kemeri ve geçidi kadrajda büyütür ve kaydırır, "yerlerini korur" bunu yasaklar. Model ya itmeyi bırakır ya coğrafyayı esnetir.
DOĞDUĞU   metin
KURAL     KIMLIK_VE_REFERANS_KILAVUZU.md:82 (tek ve yavaş kamera) [TERCİH]
ARIZA     T07 · T04
DÜZELTME  `keep their places in the frame throughout` → `keep their shapes and their left-to-right order throughout`
```

### B11 · KÜÇÜK · YEDEK kareleri başlangıç durumunu değiştiriyor, ama o duruma uyan Video metni yazılı değil (yalnız C07'de var)
```
YER       G01.md:184-185 (C03 YEDEK) ↔ :178 (C03 Video) · benzer: C01 :108 · C04 :220 · C08 :359
KANIT     C03 YEDEK: "yüzgeç ilk karede bulutun üstünde tam görünür başlar, video yalnız yükseliş"
          C03 Video 0-5 s: "the curved tip of the fin climbs out from behind the edge of the cloud bank"
ETKİ      Yedek karede yüzgeç zaten bulutun üstünde. Orijinal Video "bulutun ardından çıkıyor" der, işin bitmiş hâli (ÖLÜMCÜL adayı sınıfı: model hareketi atlar ya da geri sarar).
          F7'de yedek devreye girdiğinde Video metni yerinde uydurulur.
DOĞDUĞU   metin
KURAL     devamlilik.md:59-62 [SÖZLEŞME]
ARIZA     yeni
DÜZELTME  C03 YEDEK satırına ekle: `Video (yedek kare): 0-5 s: the fin, already above the edge of the cloud bank, keeps rising up and to the left across the sky.`
          C01, C04 ve C08 YEDEK satırlarına da kendi Video 0. vuruşunun yedek cümlesi yazılır.
```

### B12 · KÜÇÜK · Dört referans sayfası promptunda olumsuz yazı kilidi var
```
YER       G01.md:37 · :47 · :60 · :72
KANIT     "…even soft studio light from the front-left, no text anywhere."
ETKİN     Kılavuz, sahip kararı K2 gelene kadar yalnız olumlu kilit istiyor. Çekim promptlarında `plain unmarked surfaces` var, sayfalarda olumsuz kalıp var. Sayfada olumlu kilit olsaydı etiket riski aynı korunurdu.
DOĞDUĞU   metin
KURAL     KIMLIK_VE_REFERANS_KILAVUZU.md:76 [TERCİH, sahip kararı K2 bekliyor]
ARIZA     T06
DÜZELTME  `no text anywhere` → `every panel plain and unmarked` (4 sayfada)
```

### B13 · KÜÇÜK · 2.ORU sayfası: boy için insan kolu veriliyor, ⑥ ve ⑦ aynı "fixed angle" dilini kullanıyor
```
YER       G01.md:47
KANIT     "a small juvenile small enough to rest on a person's forearm"
          ⑥: "Oru lying on dark stone with its left fin held away from its torso at a fixed angle it cannot open from"
          ⑦: "its left fin hangs half open and drooping at a fixed angle"
ETKİ      Boy ölçüsü "Khev'in önkolundan kısa" iken sayfada "insan kolu" geçiyor (35 cm, insan önkolundan uzun, FILM.md:92) ve panele insan kolu sızdırabilir.
          ⑥ ve ⑦ sol yüzgeci aynı "sabit açı" cümlesiyle tarif ediyor. C12-C14 (yatık) ve C15-C23 (kucakta) durumları panelde ayrışmayabilir.
DOĞDUĞU   metin
KURAL     FILM.md:92-95 [TERCİH]
ARIZA     yeni
DÜZELTME  `small enough to rest on a person's forearm` → `shorter than the forearm of a tall biped`
          ⑥: `held away from its torso at a fixed angle it cannot open from` → `held stiffly out to the side, away from its torso, unable to open or fold`
          (⑦ cümlesi §3 kimlik cümlesidir, değişmez.)
```

### B14 · KÜÇÜK · Oru'nun teal tonu cümlesi C02 ve C06'da var, C04 ve C08'de yok
```
YER       G01.md:127 (C02) · :271 (C06) var; :201 (C04) · :342 (C08) yok
KANIT     C02: "…and its teal is one shade lighter than the night around it."
          C06: "Oru's teal is one shade lighter than the night around it."
ETKİN     Oru dört çekimde de gece ışığında görünüyor ve kucakta. Cümle olan iki çekimde Oru ayrışır, olmayan ikisinde koyu teal gecenin içine karışabilir (FILM.md:96, TD B14). Oru'nun parlaklığı çekimden çekime oynar.
DOĞDUĞU   metin
KURAL     FILM.md:96 [TERCİH]
ARIZA     yeni
DÜZELTME  C04 ve C08'de Oru paragrafının sonuna ekle: `Oru's teal is one shade lighter than the night around it.`
```

### B15 · KÜÇÜK · FILM.md §3: 3.ANNE blok başlığı 9 panel diyor, tablo ve G01 sayfası 10 panel
```
YER       FILM.md:97-104 ↔ FILM.md:78
KANIT     :97 "3.ANNE   karakter (erişkin) · tek sayfa · 9 panel" (⑩ tarifi blokta yok)
          :78 "TEK SAYFA (10 panel; ⑩ yüzgeç ucu kıvrık, 17.10.2026)"
ETKİ      Sayfa promptu 10 panel üretiyor ama onun tarif kaynağı olan blok hâlâ 9 diyor. Faz 7'de panel sayımı iki farklı belgeye karşı yapılır.
DOĞDUĞU   metin
KURAL     —
ARIZA     yeni
DÜZELTME  FILM.md:97 `9 panel` → `10 panel`; :104'ten sonra ⑩ satırı: `⑩ DURUM sol yüzgeç ucu KIVRIK yakın (sığ çanak; C20 sonu-C23)`
```

## Prompt denetimi (kalan kontroller)

- **Referans anahtarı:**
  - EKLE ↔ `Reference <No>` ↔ §3 numarası 8/8 çekimde eşleşiyor.
  - Roller sabit: 1 Khev · 2 Oru · 3 mother manta · 4 shore. Her cümle panel adlandırıyor.
  - C06 mekânı yalnız metinden alıyor (3 referans sınırı). YEDEK 4.KIYI'yi ekleme yolunu yazıyor.
- **Referans sayfası:**
  - Çekimlerin istediği paneller sayfa promptlarında var: back-view, intact left-shin, ¾ yüz, forearm-and-hand, sağ yan; cradle-pose, yüz yakın, yüzgeç arka kenarı, üstten; anne ③ ④ ⑤, profil, ¾ önden; KIYI master ve kemer ağzı.
  - Sayfa içi sorunlar: B13 ve B15.
  - İki sayfa iki zıt durumu aynı promptta veriyor: 1.KHEV'de kaval ⑦ sağlam / ⑧ çatlak, 3.ANNE'de yüzgeç ucu düz / ⑩ kıvrık. İkisi "first seven panels / eighth panel only" türü cümlelerle ayrılmış. Çatlağın ①-⑦'ye sızması görsel olmadan ölçülemez (YAPILMADI).
- **10 s planı:**
  - Vuruş iskeleti 5 farklı: C01 ve C06 [0-4-8-10]; C02 [0-3-6.5-10]; C03 [0-5-10]; C04 [0-4-7-10]; C05 ve C08 [0-5-7-10]; C07 [0-4-6-10]. Tempo düzlüğü yok.
  - İlk vuruş 8/8'de hareketle başlıyor. Son vuruş 8/8'de donmuyor. Her vuruş ≥ 2.0 s.
  - Vuruşlar C02 ve C06'da farklı özneler. C02 neden-sonuç zinciri. C06'da son vuruş (annenin yüzgeç düzleşmesi) bağımsız bir ikinci eylem ve C07 başlangıç durumunu hazırlıyor.
- **Kesme sürekliliği:**
  - ORTAK GÖRÜNÜM 16/16 birebir. Model sesi KAPALI olduğundan ORTAM SESİ cümlesi yok (doğru).
  - Ölçek/açı zinciri: çok geniş → orta-yakın → çok geniş → orta-boy → çok yakın → çok geniş → geniş (≥ 30°) → geniş yüksek. Jump cut riski yok.
  - C06 ile C07'de anne aynı sol profilde, başı sola dönük (ekran yönü korunuyor).
- **Dünya ve ışık:** gaz devi sağ üstte ve ışık sağ üstten 8/8; ufuk "one third" C03, C06 ve C07'de tutarlı. Sapma B4.
- **Durum merdiveni:**
  - Sol kaval SAĞLAM 5/5, çatlak hiçbir yerde anılmıyor.
  - Anne ışıkları: C03'te "too small and dim", C05'te sönük → yanık, C06 ve C07'de "small amber dots". Merdiven doğru.
  - Khev'in gölge sınırına göre konumu: C04 sonu gölgede → C06 başı çizgide, "not yet over it" → C08 başı çizginin bir adım gerisinde. Yazılı bir çelişki yok, kesmeler arasında zaman var.
- **Sayı:** üç ışık (Oru, anne), bir çentik, iki yüzgeç, bir kuyruk, iki adım (C01), üç aşamalı baş çevirişi (C08) tutarlı.
- **Görsel ↔ video:** 8/8'de görsel hareketten önceki anı gösteriyor. Eksik olan yedek karenin video metni (B11).
- **Tutan:** Oru her çekimde Khev'in kollarında, eller kadraj dışı ya da Oru'nun arkasında, havada asılı nesne yok. Arkadan çekimde Oru'nun görünürlüğü B5.
- **Meta etiket:** 8 Görsel ve 8 Video bloğunda çekim kodu, "Clip/Scene", referans kodu ya da büyük harfli etiket yok. 63 eşleşmenin hepsi blok dışında (başlık, YEDEK, FLOW İŞ EMRİ). `body/wound/dead/blood` blokta 0.
- **Prompt uzunluğu:** en uzun görseller C06 ≈ 3.950 karakter (tahmin), C03 ≈ 3.770, 3.ANNE sayfası < 3.400. Hepsi ≤ 4.300 sınırının altında (tahmin; araç koşulmadı).
- **Zk.n düzenleme talimatları:** zincir yok. YEDEK düzenleme cümleleri (C02, C03, C04, C05) kimliği değiştiren bir şey söylemiyor. Hepsi "Keep … exactly as they are" ile bitiyor.
- **Gruplar arası geçiş:** C08 sonu "toes on the shadow line" ↔ FILM.md:188-189 C09 başı "Khev gölge sınırında başlıyor" plan düzeyinde bağlanıyor. G02 promptları verilmediği için görülmedi.

KORU: Kimlik cümlelerinin 8/8 çekimde birebir olması ve ORTAK GÖRÜNÜM'ün 16/16 yerinde kalması.
KORU: C05 Reference 3'ün yalnız "ışıklar sönük" panelini istemesi (G01.md:235). Zıt "yanık" panel anılmıyor.
KORU: Khev'in elleri hiçbir kareye girmiyor (C01 ve C03 arkadan, C02 kadraj dışı, C04 ve C08 Oru'nun ardında).

KAPSAM DIŞI: `FLOW İŞ EMRİ` "Üretim önceliği: … C06 … → C04 · C05 · C07 · C08. Tablo sırası çekim sırasıdır" diyor (G01.md:372), ama tablo C06'yı 15. ve 16. sıraya koyuyor (G01.md:390-391). Pilot sorusu C06'ya bağlı, sıra netleşmeli.

---
```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 4 · KÜÇÜK 11
KARAR    TUR KAPANABİLİR
         (ÖLÜMCÜL yok. B1-B4 CİDDİ; yazar KABUL ya da gerekçeli RED verir. B1'in düzeltmesi bir plan sapması, sahip onayı bekler.)
GİRDİ    uretim_hatti/ELESTIRI_PROTOKOLU.md (tam) · BILINEN_TUZAKLAR.md (tam) · ILK_30_SANIYE_KILAVUZU.md (tam) · KIMLIK_VE_REFERANS_KILAVUZU.md (tam)
         GECIS_VE_SES_SUREKLILIGI.md (satır 1-90, §1-§5) · GPT_IMAGE_OMNI_KILAVUZU.md (satır 78-275, §4-§10; üst başlıklar Grep ile)
         MOONMOTHER/FILM.md satır 1-268 (§1-§5 başı: §3 KİMLİK CÜMLELERİ + ORTAK GÖRÜNÜM tam, §4 tam, AÇILIŞ tablosu) · MOONMOTHER/PROMPTLAR/G01.md satır 1-427 (tam)
         .claude/agents/devamlilik.md (tam) · goruntu-yonetmeni.md (yalnız 8 soru satırları) · uretim_hatti/ARIZA_LISTESI.md (H/T satırları) · araclar/film_dogrula.py (satır 78-108, 536-577)
         Kimlik ve ORTAK cümle denetimi Grep ile, 12 cümle türü için satır numaralarıyla yapıldı. Hiçbir kare ya da referans görseli verilmedi, görülmedi.
YAPILMADI  film_dogrula.py koşulmadı (bu ajanda kabuk yok); sayım Grep ile yapıldı.
           G01'deki "PILOT.md'den birebir" iddiası doğrulanmadı (PILOT.md görev girdisi değil).
           G02/G03 promptları ve ODA/ dosyaları (yazar gerekçesi, öteki eleştirmenler) okunmadı; C08→C09 geçişi yalnız FILM.md §4 düzeyinde.
           FILM.md satır 269-414 (SES PLANI devamı, MÜZİK) okunmadı. Sayfa panelleri arası kimlik karşılaştırması ve çatlak sızması Faz 7'ye kalır.
```
