> Fable notu: 15 tur sınırında durdu; SendMessage devamıyla raporu verdi (aynı çağrı).

# G01 teknik danışman eleştirisi (F5 tur 1): `yatay_4_dk_filmler/MOONMOTHER/PROMPTLAR/G01.md`

Talimat gereği yeni okuma yapmadım ve dosya açmadım. `MEDYA_DURUMU.md` ref 0/4, kare 0/24 diyor, yani yalnız metni inceledim. Pilot sorularının (C01, C06) hepsi için cevap **görülmedi**.

## Bulgular

### B1 · CİDDİ · C06: dev manta pozu, ekli referans panelinin pozuyla çelişiyor
YER       C06 Görsel, `G01.md:269` ve `:275`; kaynak panel `G01.md:60`
KANIT     3.ANNE ② paneli: `a full-length three-quarter view from the front, head turned toward the viewer and her left side toward the viewer, tail behind her`. C06 rol cümlesi: `take her complete form from it, using the three-quarter front full-length panel`. C06 gövdesi: `Her head points toward the shore at the left with her left side toward the camera`. C07 aynı pozu ① panelinden ister: `using the full-length left-side profile panel` (`:304`).
ETKİ      Filmin akrabalık çekiminde model, baş izleyiciye dönük bir referanstan baş sola bakan profil çizmeye zorlanır. Karmaşık manta şekli yeniden poza sokulurken kimlik kayar ve "bütün gövde, tek göz, üç ışık, iki yüzgeç" kare kabulü tutmaz.
DOĞDUĞU   referans (panel seçimi)
KURAL     `KIMLIK_VE_REFERANS_KILAVUZU.md:37` (çekim anahtarı paneli adlandırır, `using the back-view panel`) [TERCİH]
ARIZA     T16 / T15 (yakın)
DÜZELTME  C06: `using the three-quarter front full-length panel` → `using the full-length left-side profile panel`. FILM §4 C06 satırındaki "¾ önden tam gövde paneli" notunu Fable günceller.

### B2 · CİDDİ · 2.ORU sayfası insan kolu ve eli çağırıyor
YER       `G01.md:47` (2.ORU referans promptu)
KANIT     `Every panel shows only Oru, … a small juvenile small enough to rest on a person's forearm` ve panel 8: `Oru held upright in a cradled posture, head raised, belly turned toward a flat vertical surface behind it`.
ETKİ      `person's forearm` ve `held` birlikte kol ya da el çizdirir. Bu sayfa C02, C04, C06 ve C08'e referans olarak girer (4/8 çekim). İnsan eli, filmin tek insansız evrenine ve "yalnız Oru" panel kuralına aykırıdır. Referans iki denemede tutmazsa sonraki 16 çekim durur.
DOĞDUĞU   metin (referans promptu)
KURAL     `GPT_IMAGE_OMNI_KILAVUZU.md:140` (eller ya tam görünür ya kadraj dışı) [TERCİH]; `PROMPT_HATA_ATLASI.md:84` A07 (tutanı olmayan nesne ya da gövdesiz el) [HİPOTEZ]
ARIZA     T15 (yakın)
DÜZELTME  `a small juvenile small enough to rest on a person's forearm` → `a small juvenile`. Panel 8: `Oru held upright in a cradled posture` → `Oru floating upright in a cradled posture`.

### B3 · CİDDİ · C04: yüzü denizde, geriye doğru iki ayak hareketi
YER       C04 Video, `G01.md:214`; Görsel `:201`; başlık notu `:422`
KANIT     Video: `takes one careful sideways step: the foot nearer the arch lifts, moves toward the arch and plants on the basalt, while his chest and face stay turned toward the sea at the right` ve `his second foot comes in beside the first and both feet cross the shadow line into the shade`. Görsel: `in three-quarter view with his right side toward the camera, his chest and face turned toward the dark sea`. Başlık notu: `adım kemere doğru geri-yan`.
ETKİ      Kemer Khev'in arkasında, yüzü ise zıt yönde. Digitigrad bacaklı bir yaratıktan 10 saniyede iki ayrı geri-yan ayak hareketi istenmiş. Model gövdeyi yürüyüş yönüne çevirir ya da ayak kayar. Bu durumda "gövdesini Oru ile deniz arasına koyuyor" bilgisi bozulur. Mevcut YEDEK tüm adımı siler.
DOĞDUĞU   hareket
KURAL     `ARIZA_LISTESI.md:53` T10 (HAREKET sadeleşir) [SÖZLEŞME]
ARIZA     T10
DÜZELTME  Ayak hareketini ikiden bire indir.
          Görsel: `one short step from the shadow line` → `his rear foot exactly on the shadow line`.
          Video: `0-4 s … 4-7 s …` bölümlerini şununla değiştir: `0-7 s: his front foot draws back beside his rear foot and both feet stand in the shade, his chest and face still turned toward the sea; the curved fin edge in the sky creeps across the stars.`

### B4 · CİDDİ · C02: sağ üst köşeye dört çelişkili talimat
YER       C02 Görsel, `G01.md:123`, `:129`, `:131`
KANIT     `Reference 3 (mother manta): take only the colour and the round shape of her open amber eye from it`. Gövde: `She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. In this frame it reads only as one soft round amber glow with no sharp detail`. Işık cümlesi: `the gas giant's thin pale rim light from the upper right`. Başlık notu (`:420`): gök cümlesi atıldı çünkü "sağ üstteki odak dışı amber yuvarlakla aynı köşede çakışıp ikinci göz riski doğururdu".
ETKİ      Aynı köşe için ayrıntılı göz cümlesi, ayrıntı veren bir referans ve "ayrıntı yok" isteği birlikte duruyor. Gaz devi de aynı köşede anılıyor ve atılan gök cümlesinin gerekçesi bu ışık cümlesi için de geçerli. Sonuç: ayrıntılı göz, ikinci yuvarlak ya da gezegen. C02 açılış ve kapak karşılığı olduğu için ILK_30 göz-asimetrisi kapısına takılır.
DOĞDUĞU   metin
KURAL     `PROMPT_HATA_ATLASI.md:66` A05 (aynı promptta birbirini yalanlayan iki istek) [HİPOTEZ]; `ILK_30_SANIYE_KILAVUZU.md:96-103` kare kapısı [UYGULAMA]
ARIZA     T15, T18
DÜZELTME  Üç değişiklik:
          1. `She has one enormous amber eye … thick organic eyelid. ` cümlesini sil.
          2. Reference 3 cümlesini sil ve `ref/3.ANNE_v1.png`'yi `EKLE`'den çıkar (3 → 2 referans).
          3. Işık cümlesinde `the gas giant's thin pale rim light from the upper right` → `a thin pale rim light from the upper right`.
          Üçü de FILM §3'ün "birebir" satırlarından sapar, Fable onaylar. C05'te de aynı ışık cümlesi var (gözün kadrajı doldurduğu çekim); orada gezegen belirmez ama gereksiz.

### B5 · CİDDİ · C01 ve C03: sırtı dönük Khev'in "göğsündeki" Oru kameradan görünmez
YER       C01 Görsel `G01.md:89`; C03 Görsel `:167`
KANIT     C01: `standing upright … and his back to the camera, facing the sea` … `Khev presses Oru against his chest with both forearms` … `At this distance Oru reads only as a small teal shape against his chest.` C03: `Oru reads only as a tiny teal shape against his chest.` FILM §3'te "arkadan siluet" cümlesi var (`FILM.md:143`) ve C06 onu kullanıyor (`:271`).
ETKİ      Göğüs kameradan uzağa bakıyor. Model teal şekli ya sırta yapıştırır (sırt çantası gibi) ya da Khev'i döndürür. "Korunan yavru" bilgisi, filmin ilk çekiminde silüet okunurluğuna bağlı.
DOĞDUĞU   metin
KURAL     `FILM.md:160-165` (kadrajda görünen parça kimlik cümlesiyle) [SÖZLEŞME]
ARIZA     T11 (yön) ve T01 (silüet teması), yeni varyant
DÜZELTME  C01: `a small teal shape against his chest` → `a small teal shape beside his right shoulder`. C03: `a tiny teal shape against his chest` → `a tiny teal shape beside his right shoulder`. Bu, C06'daki yerleşimle aynıdır.

### B6 · CİDDİ · 4.KIYI çıkıntı derinliği, C08'in sayısıyla çelişiyor
YER       `G01.md:72` (KIYI sayfası); C08 Görsel `:338` ve `:340`
KANIT     KIYI: `a drop about as deep as the arch is tall`. C08: `The lower ledge lies about twice Khev's height below the end of the causeway.` ve `using the wide master panel`. FILM §3'te kemer: `A tall ancient black-basalt arch` (`FILM.md:150`). Kemer yüksekliğinin Khev'e oranı hiçbir yerde yazılı değil.
ETKİ      C08'in tek bilgisi üç seviyenin haritası. Referanstaki master panelde derinlik kemer boyu kadar, metinde Khev boyunun iki katı. Kemer "tall" ise ikisi birbirini tutmaz. C09-C13 aynı master panelden geometri alır.
DOĞDUĞU   referans (KIYI promptu)
KURAL     `FILM.md:154` (çıkıntı yüksekliği "yalnız geniş planlar", Khev'e göre) [SÖZLEŞME]
ARIZA     T04
DÜZELTME  KIYI promptunda `, a drop about as deep as the arch is tall,` ifadesini sil. Derinliği yalnız kare promptları taşır. Kemer yüksekliğini Khev boyuyla yazmak (FILM §3 kimlik satırı) Fable'ın kararı.

### B7 · KÜÇÜK · C04 Video: "screen" kelimesi nesne çağırır
YER       C04 Video, `G01.md:214`
KANIT     `so that his arms and shoulders form a screen between Oru and the sea`. Başlık notu (`:422`): `like a shield` yerine `a screen` seçilmiş. `film_dogrula.py:90` `screens?` yakalıyor ama `:555` Y8'i yalnız Görsel'de tarıyor.
ETKİ      `screen` ekran ya da perde nesnesi çağırabilir. Tarama Video'yu görmediği için kimse uyarılmaz.
DOĞDUĞU   metin
KURAL     `PROMPT_HATA_ATLASI.md:152` A14 (istenmeyeni çağıran pozitif sözcük çıkarılır) [HİPOTEZ]
ARIZA     T06 (yakın)
DÜZELTME  `form a screen between Oru and the sea` → `stand between Oru and the sea`

### B8 · KÜÇÜK · 2.ORU: mavi karın ışığı paneli hiçbir çekimde kullanılmıyor ama 4 çekime sızabilir
YER       `G01.md:47` (panel 3)
KANIT     `a low side view showing the thin translucent belly with a faint pale-blue glow inside it`. FILM §4 C12 riski: "mavi karın ışığı kareye girmez (ikinci ışık kodu)". C01-C08 rol cümlelerinin hiçbiri bu paneli anmıyor.
ETKİ      Sayfa bütün olarak C02, C04, C06 ve C08'e eklenir. Panel seçimi sayfadaki pikselleri ortadan kaldırmaz; amber-only ışık kodu mavi bir ikinci kodla kirlenebilir. Sızma ölçülmedi (P17).
DOĞDUĞU   referans
KURAL     `KIMLIK_VE_REFERANS_KILAVUZU.md:36` (panelden sızma, ölçülmedi) [HİPOTEZ]
ARIZA     T09 (yakın), yeni
DÜZELTME  `showing the thin translucent belly with a faint pale-blue glow inside it` → `showing the thin translucent belly`. Planın karın ışığına ileride ihtiyacı varsa o çekimde ayrı üretilir.

### B9 · KÜÇÜK · C06: Oru'nun yüzgeç durumu sayfada yok ve aynı paragrafta kendiyle çelişiyor
YER       C06 Görsel `G01.md:271`; Video `:284`
KANIT     `Cradled, Oru keeps … both fins half closed against its torso` ve aynı paragrafta `the right fin hanging half open and the left fin folded against its side`. Video: `while its left fin stays folded`. 2.ORU'da sağ yarım açık + sol katlı panel yok (panel 7: sağ açık, sol yarım açık; panel 8: ikisi yarım kapalı).
ETKİ      Durum sayfada panel olarak yok ve "yarım kapalı" ile "katlı" aynı yerde. Model birini seçer ya da iki yüzgeci de değiştirir.
DOĞDUĞU   metin
KURAL     `AGENTS` §T05/T09: her durum sayfada panel (`teknik-danisman.md:28`) [SÖZLEŞME]
ARIZA     T05, T09
DÜZELTME  Görsel: `, the right fin hanging half open and the left fin folded against its side` ifadesini sil. Video: `while its left fin stays folded` → `while its left fin stays half closed`.

### B10 · KÜÇÜK · C06 Video: son iki saniyede dev yüzgeçlerin biçim değiştirmesi bilgi taşımıyor
YER       C06 Video, `G01.md:284`
KANIT     `8-10 s: the mother manta's fins curl a little and level out while the cloud strands keep drifting`
ETKİ      Akrabalık bilgisini silüet taşıyor (FILM §4 C06 riski). Klibin sonunda dev nesnenin şekil değiştirmesi hiçbir şey eklemiyor; yalnız deformasyon riski artıyor. Sonda bozulma `GPT_IMAGE_OMNI_KILAVUZU.md:62` (§3) ve etkisi bu filmde ölçülmedi.
DOĞDUĞU   hareket
KURAL     `GPT_IMAGE_OMNI_KILAVUZU.md:178` (tek ana hareket) [TERCİH]
ARIZA     T15 (yakın), T05
DÜZELTME  `the mother manta's fins curl a little and level out while the cloud strands keep drifting` → `the cloud strands keep drifting across the mother manta's fins`

### B11 · KÜÇÜK · C07 Video: hızlı küçük hareket sözcükleri su ölçeğini küçültür
YER       C07 Video, `G01.md:317`
KANIT     `spray leaping from its crest and the loose stones along the shore bouncing`. FILM §4 C07 riski: "su geniş ve yavaş … maket suyu görünümü yok".
ETKİ      `leaping` ve `bouncing` hızlı, küçük parçacık hareketi; devasa sırt maket su gibi okunur.
DOĞDUĞU   metin
KURAL     `ARIZA_LISTESI.md:46` T03 [SÖZLEŞME]
ARIZA     T03
DÜZELTME  `spray leaping from its crest` → `spray lifting from its crest`

### B12 · KÜÇÜK · C01 Video: "mother manta" adı, ay gibi duran yüzeye gövde çağırır
YER       C01 Video, `G01.md:102`
KANIT     `the mother manta's eyelid begins to lift, widening the amber opening`. Kare yalnız `Only her rounded brow is visible … it looks like a moon` gösteriyor. FILM §4 C01: "ay kayadan canavara dönüşmez".
ETKİ      Videoda özneyi gösteren ad "manta". Model bulutun ardından gövdeyi çıkarabilir. Bu, C06'daki açığa çıkışı önceden harcar.
DOĞDUĞU   metin
KURAL     `FILM.md` §4 C01 riski (gövde ufuk bulutunun arkasında kalır, yeni beden doğmaz) [SÖZLEŞME]
ARIZA     T16
DÜZELTME  `the mother manta's eyelid begins to lift` → `the eyelid of the round pitted surface begins to lift`

### B13 · KÜÇÜK · C08 Video: kamera ve özne hareketi aynı cümlede
YER       C08 Video, `G01.md:351`
KANIT     `Khev turns his head in three stages, … then out to the open sea; the camera makes a very slow push-in toward the arch and the causeway, and the sea keeps breaking …`
ETKİ      Üç baş dönüşü ile itme tek cümlede. Geniş planda küçük bir figürün bakışı zaten zor okunur.
DOĞDUĞU   metin
KURAL     `GPT_IMAGE_OMNI_KILAVUZU.md:178` ("kamera ve özne hareketi ayrı cümle") [TERCİH]
ARIZA     T07
DÜZELTME  `…then out to the open sea; the camera makes` → `…then out to the open sea. The camera makes`

### B14 · KÜÇÜK · Referans sayfalarında ad girişi
YER       `G01.md:37` ve `:47`
KANIT     `The same alien biped, Khev, appears in eight panels` ve `The same small alien creature, Oru, appears in eight panels`
ETKİ      Karakter sayfaları başlık ya da etiket basılmaya en yatkın görsellerdir. Ad ayrıca kimlik cümlelerinde de tekrar ediyor.
DOĞDUĞU   metin
KURAL     `BILINEN_TUZAKLAR.md:62-77` §C (ORION kutuya yazıldı) [HİPOTEZ]; `PROMPT_HATA_ATLASI.md:120` A11
ARIZA     T06
DÜZELTME  `The same alien biped, Khev, appears` → `The same alien biped appears`; `The same small alien creature, Oru, appears` → `The same small alien creature appears`. İlk kare kabulünde sayfada başlık ya da etiket aranır.

### B15 · KÜÇÜK · C06 `d2` satırında üçüncü deneme kuralı yok
YER       `G01.md:291`
KANIT     C06: `aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir.` C01-C05, C07 ve C08'de `İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.` var.
ETKİ      Pilot çekim olan C06'da aynı promptun üçüncü kez gönderilmesine engel yok.
DOĞDUĞU   metin
KURAL     `teknik-danisman.md:60` [SÖZLEŞME]
ARIZA     —
DÜZELTME  Cümleyi C06 `d2` satırına ekle.

KORU: C05'te Reference 3 yalnız "sönük" göz panelini ister, "yanık" panelini anmaz (`G01.md:235`). Bu, zıt iki durumu aynı üretimde eşit ağırlıkla vermeme kuralına uyuyor.
KORU: C02'de eller kadraj dışı (`:125`), C04 ve C08'de Oru'nun ardında (`:201`, `:342`).
KORU: Tek kusurlu `YEDEK` düzeltmeleri `Keep … exactly as they are` biçiminde yazılı (C02 `:147`, C03 `:185`, C04 `:221`, C05 `:253`).

## Faz 5 kontrol listesi cevapları

**Promptta riskli an hâlâ isteniyor mu?** Evet, şu altı yerde:
- C01: iki adım ve dur.
- C04: geri-yan iki ayak hareketi (B3).
- C05: sıralı üç ışık (T09). Kare kabulü ve YEDEK var.
- C06: dev yüzgeç kıvrımı (B10).
- C07: "yaklaş-dur" ve sırt.
- C08: üç baş dönüşü ve kamera itmesi (B13).

**Meta etiket, büyük harfli jeton ya da çekim kodu var mı?** Hayır. Okumayla baktım: kod bloklarında çekim kodu, `Clip n of N` ve KHEV/ORU etiketi yok. `Reference n (rol)` anahtarı 10.10.2026 sözleşmesidir, §C kapsamı dışında. Ad tekrarı için B14.

**Çekim listesi maddeleri, promptlara uygulanmış hâliyle:**
- **T01:** C01 ve C03'te silüet ölçeğinde temas okunmaz, kabul edilmiş (B5 yerleşimi düzeltir). C02: eller kadraj dışı. C04 ve C08: eller Oru'nun ardında. C06: Oru'nun yüzgecinin Khev'in omzuna yakın kalkması kaynaşma riski taşıyor, YEDEK yalnız oklüzyon için yazılmış.
- **T03 / T13:** Dünya atmosferli, vakum değil. Deniz, sprey ve taş C07 ve C08'de meşru. `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` §3 ve §8'in vakum maddeleri uygulanmaz. B11 ölçek sözcüğü.
- **T06:** Görsel'de ekran ve yazı yok. Video'da `screen` var (B7).
- **T05 / T09 (panel, SMOKE P17):** Wrong-panel riski en yüksek yerler:
  - C05: ANNE ⑤ ve ⑥ aynı göz, yalnız ışık durumu farklı.
  - C01, C03, C06: ANNE sayfasında dört baş paneli var.
  - C06: panel poz çelişkisi (B1) ve yüzgeç durumu (B9).
  Çekim başına referans: 8/8 çekimde ≤3 (C01 3, C02 3, C03 3, C04 3, C05 1, C06 3, C07 2, C08 3).
- **T15:** Aynı kadrajda canlı sayısı: C01 3 (Khev, Oru, dev manta), C02 2 + odak dışı göz, C03 3, C04 2 + yüzgeç kenarı, C05 1, C06 3, C07 1, C08 2. Hepsi hikâye için şart. C02 sağ üst köşe için B4.
- **Açılış (C01-C03):** Kalabalık yok, kamera üçünde de sabit, karmaşık el-nesne teması yok. C02 vizörsüz ama yüz orta-yakın planı; ILK_30 §6 kare kapısı ve `¾ arkadan` YEDEK'i yazılı. YEDEK yalnız karedeki bozulmayı kapsıyor. Video içindeki yüz dönüşü için ayrı yedek yok; kare ve video onayı F7'de.
- **T08:** Aynı kadrajda tek rejim. Süzülen canlılar ile yerdeki Khev doğal kuralla ayrılıyor. "Süzülür" sözü C03 ve C07'de yok (`advances`, `climbs`).
- **T02 / T10:** C01 iki adım, C04 B3, C08 tek adım + kamera itmesi. Diz çökme ve kalkma C01-C08'de yok.
- **Replik:** `REPLIK yok`, uygulanmaz. Video'da ses ya da çağrı kelimesi yok; Omni yerel sesi kurguda atılacak (`FILM.md` künye).
- **Kesme sürekliliği:** C01→C02→C03→C04→C05→C06→C07→C08 geçişlerinin hepsinde ölçek ya da açı farkı büyük; jump cut riski görmedim. C06→C07 kamera açısı farkı FILM'de yazılı. C01 ve C04 durağan kareyle başlıyor. Ortak görünüm cümlesi 8/8 Görsel ve 8/8 Video'da var; C05 ve C02 gök cümlesi taşımıyor ama ışık cümlesi var.
- **Mod ↔ model:** Omni'ye tek başlangıç karesi gidiyor; malzemeden video, videodan videoya ya da uzatma istenmiyor. Uygun.
- **Red riski:** `body`, `wound(ed)`, `injured`, ölüm ve kan kelimeleri promptlarda yok (başlık satırı hariç). Milliyet ve bedenden bir şey çıkarma eylemi yok. Kompozisyon reddi tipi yan yana iki ön kol ya da tepeden makro yok.
- **Uzunluk (tahmin):** Eşik taramasıyla sınırladım. Referans sayfaları ≈3,1k altında, C06 Görsel ≈4k. Hiçbir blok 4.300'ü aşmıyor görünüyor. `film_dogrula`'yı ben koşmadım; DURUM kaydına göre C01-C08'de hata yok.

KAPSAM DIŞI: Video promptlarında ORTAK GÖRÜNÜM'ün her seferinde tekrarı, `GPT_IMAGE_OMNI_KILAVUZU.md:181-182` K9 sahip kararı bekliyor. Hat kuralı yürürlükte, bulgu yazmadım.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 6 · KÜÇÜK 9
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok). CİDDİ B1-B6 için yazar KABUL/RED cevabı vermeli.
GİRDİ    `uretim_hatti/ELESTIRI_PROTOKOLU.md` · `BILINEN_TUZAKLAR.md` · `GPT_IMAGE_OMNI_KILAVUZU.md` · `KIMLIK_VE_REFERANS_KILAVUZU.md` · `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` · `PROMPT_HATA_ATLASI.md` · `ILK_30_SANIYE_KILAVUZU.md` (§6 satırları) · `FLOW_GERCEKLERI.md` (Ek 2-3) · `ARIZA_LISTESI.md` (yalnız T bölümü, Grep satırları) · `PROMPTLAR/G01.md` (tamamı) · `PROMPTLAR/PILOT.md` (C01 ve C06 ile REFERANS PROMPTLARI'nı G01 ile gözle karşılaştırdım, fark görmedim) · `FILM.md` (§1-§4, §3 kimlik tabloları) · `ODA/DURUM.md` · `ODA/MEDYA_DURUMU.md` · `.claude/agents/teknik-danisman.md` · `araclar/film_dogrula.py` (yalnız satır 90 ve 525-569). Başka ajanların `ODA/` çıktılarını ve `SAHIP_PLANI.md`'yi okumadım. EKSİK yok.
YAPILMADI  Kare ve video incelemesi (medya yok, ref 0/4 ve kare 0/24). Pilot soruları C01 ve C06 için **görülmedi**. `film_dogrula.py` koşulmadı (bu ajanda kabuk yok). Karakter sayımı eşik taramasıyla sınırlandırılmış tahmin, kesin sayım değil. `GECIS_VE_SES_SUREKLILIGI.md` ve `GOSTERIM_COZUMLERI.md` okunmadı.
