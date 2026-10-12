# F5 · teknik-danisman (eleştirmen) · tur 1 — THE_WRONG_BURN G01

> Girdi: PROMPTLAR/G01.md (tam) + FILM §3 §4 + F3_teknik-danisman_2 (önceki bulgular) + F3_yonetmen_3 (cevaplar) + G01 YAZAR NOTLARI. Ajanın cevabı aynen (Fable kaydı, 09.10.2026).

## Faz 5 · teknik-danışman · tur 1 · THE_WRONG_BURN · G01

### Önceki bulguların denetimi (F3_teknik-danisman_2 B1-B9)
Dokuzu de G01'de uygulanmış.
- **B1:** C06'da "omuz" yok, "on the side opposite to where she looks" var.
- **B2:** C09'da "mesafe sabit" yok.
- **B3:** C09 kamerası sol arkada, kanca ve gösterge çıkmış.
- **B4:** C10'da tek kol kalkışı var, `BRAM_kolkalkik` kullanılmış.
- **B5:** C07'de el sol kenara açılıyor.
- **B6:** 7-10 s ve 6-10 s cümleleri ayrı bloklarda, 8 s promptlarına girmemiş.
- **B7:** "sallanıyor" ve "asılı" yok. Yeni bir bulgu B11'de.
- **B8:** C08'de bant başlangıçta zaten parlak.
- **B9:** Referans tarifleri olumlu geometride. "Body" yalnız başlık notunda geçiyor, prompt gövdelerinde geçmiyor.

### B1 · CİDDİ · Durum referansları aynı karede çelişiyor (C10 başlangıcı, C08, C09)
KANIT    İş emri satır 30, C10 başlangıç karesi: "ref/BRAM_v1.png · ref/BRAM_kontrolsuz_v1.png · ref/BRAM_kolkalkik_v1.png · ref/KANCA_cantada_v1.png · ref/DUNYA_alcak_ust_v1.png". C10 EKLE (a) aynı listeyi taşıyor. Aynı çekimin Görsel metni: "the left arm, nearest the camera, hangs loosely half-open at his side". Satır 31 (bitiş karesi) `BRAM_kolkalkik`'i zaten ayrıca alıyor. C08 ve C09 satırları (27, 29): `BRAM_v1` ("upright, arms at his sides, legs together") ile `BRAM_kontrolsuz_v1` ("loosely half-open") birlikte.
NEDEN    Kolu kalkık bir referansla üretilen başlangıç karesi kolu kalkık çıkabilir. O zaman iki kare aynı olur ve C10'un tek hareketi kaybolur. C08 ve C09'da dik ve yarı açık iki duruş birbirine karışır. Durum merdiveni metinle tutmuyor (BILINEN §B5; SINIF 🅐5).
ARIZA    T05 · T09
ÖNERİ    1) `BRAM_kolkalkik_v1`'i satır 30'dan ve C10 EKLE (a)'daki başlangıç tarafından çıkar. Yalnız satır 31'de (bitiş) kalsın.
2) C08, C09 ve C10 başlangıç karelerinde `BRAM_v1`'i çıkar. `BRAM_kontrolsuz` zaten `BRAM_v1`'den türedi ve bant, vizör, lamba, ezik çanta ile halkayı taşıyor.

### B2 · CİDDİ · SELA_v1 bileği son durumda (0/4) sabitliyor, C03 ve C07 çelişkili iki referansla üretilecek
KANIT    SELA_v1: "a row of four round recessed bays on her right wrist, all four dark hollows". C03 EKLE: "referans: ref/SELA_v1.png · ref/BILEK_2-2_v1.png". C07 EKLE: "ref/SELA_v1.png · ref/BILEK_1-3_v1.png". YAZAR NOTU 2: "yuva sayısı ve durumu BILEK_2-2 referansından gelir". F3_yonetmen_3 §3: "durumu BILEK karelerinde".
NEDEN    Yuva sayısı filmin bedeli ve "yanan = kalan" okumasının tek taşıyıcısı. Sela referansı 12 çekimin 10'unda bu sayıyı filmin sonundaki hâlinde (0/4) veriyor. C03'te (2/2) ve C07'de (1/3) model iki farklı durum görüyor. Sola kaçacak sayım, hikâyenin ödemesini bozar.
ARIZA    T09 · T05 · T06
ÖNERİ    1) SELA_v1'de sağ kol yanda, bilek bandı kadraj dışında olsun. Prompttan "Her right forearm is held across her waist … all four dark hollows" cümlesini çıkar.
2) Bu poz ayrıca ön kolu sağ kalçadaki halka ve iple yan yana getiriyor (T01). Eller yanda, ip boşta olsun.
3) C03 kare satırından `SELA_v1`'i düşür. Çekimde yalnız bilek ve Dünya var.

### B3 · CİDDİ · "Elin tutuşu değişmez" cümlesi C02, C06 ve C12 video promptlarında yok
KANIT    FILM Risk: C02 "T01 kumanda tutuşu baştan kurulu, el kıpırdamaz", C06 aynısı, C12 "T01 tutamak teması baştan kurulu ve değişmez". G01 C06 Video: "Her suit jolts sharply toward the left in one hard push … She stays turned toward the left in the same posture". C02 Video: "A fine, steady tremor runs through her suit as it is pushed toward the right". C12 Video: "Both figures and the frayed rope end stay in place". C01 Video bunu yapıyor: "The woman keeps both gloves on the grab handle".
NEDEN    Tutuş yalnız başlangıç karesinde var. Eldiven en çok sert itişte (C06) ve titremede (C02) kutudan kayar ya da giysiye gömülür. C01'de çözülen kalıp üç çekimde atlanmış. T01, 49 filmin 21'inde 🔴.
ARIZA    T01 · T03
ÖNERİ    1) C02 ve C06 Video'ya ekle: "Her right glove stays gripped on the control box on her chest."
2) C12 Video'ya ekle: "Her right glove stays on the grab handle."
3) "pushed" ve "one hard push" sözcüklerini hareketin kendisine çevir: "the whole suit shifts sharply toward the left once". İtici çağrışımı gaz izi (T03) doğurabilir. Bu çıkarım ölçülmedi.

### B4 · CİDDİ · C08: "güneşin önündeki siluet" iki prompt metninde aynı yere oturmuyor
KANIT    C08 Görsel: "The curved limb of planet Earth fills the upper half of the frame above her head. At the left, at the edge of Earth, the sun touches the limb … Directly in front of her face, at the same height, in front of the sun, a small, dark astronaut silhouette … the silhouette is dark against the sun." DUNYA_dogus_ust: "The lower half of the frame is black emptiness."
NEDEN    Güneş üst yarıdaki limbte, siluet yüz hizasında yani alt yarıda. Üst üste binmiyorlar. Siluet ya siyah boşluğa karşı koyu üstüne koyu kalır, ya da model güneşi yüz hizasına indirir ve "Dünya üstte" bilgisi bozulur. "Bram tam önünde, güneşe karşı" tek karede okunmaz. Bu iki prompt metninden çıkarılmış bir geometri, ölçülmedi.
ARIZA    T11 · T18
ÖNERİ    Güneşi siluetle aynı hizaya getir: "the horizon of Earth is rolled so its left end dips to the height of her face, and the sun touches the limb there, directly behind the silhouette". Bu olmuyorsa "in front of the sun" ve "dark against the sun" cümlelerini sil. Siluet güneşten gelen ince kenar ışığı ve kehribar noktayla okunur.

### B5 · CİDDİ · C09: 7-10 s cümlesi Bram'ı kamera düzlemine sokuyor, dönüş sınırı prompttan düşmüş
KANIT    Görsel: "from about one metre behind a woman's left shoulder, camera at her head height". 7-10 s: "He keeps gliding and turning slowly at the same pace, up above and beyond the back of her helmet." FILM 7 s: "Sela'nın kaskının gerisinde ve yukarısında". Video: "turning very slowly about a single axis". FILM Risk: "7 s'de çeyrek turdan az". BRAM_v1: "viewed from his left side and slightly from behind". BRAM_kontrolsuz: "seen from behind … three-quarter".
NEDEN    Kask kameranın önünde 1 m'de. Kaskın arkasının ötesi kamera tarafı demek. Bram'ın yolu kaskın ve kameranın düzlemine girer: kask teması ya da ölçek sıçraması (T01). Dönüşün sayısal sınırı ve ekseni metinde yok. Çeyrekten fazla dönerse hiçbir referansta olmayan ön yüz ve ayna vizör üretilir. Tur 2 B2'nin "hiçbir noktada bir insan boyundan yakın değil" güvencesi 7 s'den sonra tutmuyor.
ARIZA    T01 · T10
ÖNERİ    1) Video: "turning very slowly about one vertical axis, by less than a quarter turn in the whole clip".
2) 7-10 s: "He keeps gliding toward the upper right at the same pace, staying high above her helmet and never nearer to it."

### B6 · CİDDİ · Sela'nın arkadan görünüşü için referans yok
KANIT    SELA_v1: "front view … mid-thigh up … Backpack straps over her shoulders". Arkadan görünen çekimler: C04 "the back of her helmet … the top of her backpack", C09 "The back of her helmet", C11 "a backpack on her back", C12 "seen from behind … a backpack on her back".
NEDEN    Çanta ve kask arkası dört çekimde ve kapanış karesinde her başlangıç karesinde yeniden uydurulur. Ekipman kayması, filmlerin 18/49'unda 🔴 (T05; SINIF 🅑3).
ARIZA    T05 · T09
ÖNERİ    `SELA_arka_v1` ekle: sağ arkadan, aynı giysi, çanta tam görünür. Bunu C04, C09, C11 ve C12 kare satırlarına koy.
YAZAR NOTU 7 (yüz) için ayrı referans gerekmez. C05 karesi onaylanınca C06 ve C07 başlangıç karesi satırlarına referans olarak eklenir. C06'da yüzün alt yarısı yansımada, C07'de yüz küçük.

### B7 · KÜÇÜK · EKLE satırları Frames to Video bloklarına "referans" yazıyor
KANIT    C01 bloğu: "FLOW Frames to Video / EKLE başlangıç karesi: kare/C01.png · referans: ref/SELA_v1.png · ref/BRAM_v1.png …". İş emri satır 34: "Frames to Video | başlangıç kare/C01.png". Aynı kalıp C01-C12'nin hepsinde.
NEDEN    Referans eklemek Ingredients modudur. FLOW_GERCEKLERI §1'e göre Quality'de Ingredients yok, Lite ve Fast yalnız 8 s veriyor. İş emri doğru. Bloğu izleyen operatör modu yanlış seçer ya da kare adımının referanslarını video adımına taşır.
ARIZA    yeni (Mod ↔ model)
ÖNERİ    Her blokta EKLE'yi ikiye böl: "KARE (Görsel): referans …" ve "VİDEO (Frames to Video): başlangıç karesi [+ bitiş karesi]". Referanslar video satırından çıksın.

### B8 · KÜÇÜK · C08 siluet: %5 büyüme, koyuluk ve lamba yeri
KANIT    Video: "the dark silhouette in front of the sun grows very slightly larger … white light spreads outward across the frame". Bitiş: "about five percent larger". Siluette: "a small amber point at the centre of the helmet". BRAM_v1: "a small amber beacon lamp on top of the helmet, always lit".
NEDEN    Küçücük koyu bir şekilde %5 görünmez. Aynı karede güneş kayması, ışık yayılması ve bant solması zaten tek olay. Büyüme ikinci durum değişimi ve "kamera sabit" riskini (zoom gibi okunma) artırır. Işık yayılırken siluet önden aydınlanabilir (bilim B7'nin koşulu). Lamba başka her çekimde (C01, C09-C12) kaskın tepesinde. C08'de ortada olması aynı referanslı karede çelişki.
ARIZA    T18 · T05
ÖNERİ    1) Siluet iki karede aynı boy. "grows very slightly larger" ve "five percent larger" cümlelerini sil; FILM C08'deki "hafifçe büyüyor" cümlesi de düşer.
2) Video'ya ekle: "The silhouette stays dark."
3) "at the centre of the helmet" yerine "at the top of the helmet".

### B9 · KÜÇÜK · C07 bitiş karesi SEÇENEĞİ: karar "kullanma"
KANIT    Düzenleme promptu: "Keep the identical camera, framing, face … and the row of bays on the wrist. Change only the right glove: it now rests at chest height near the left edge of the frame". FLOW_GERCEKLERI §9 (satır 159): "Frames to Video bitiş karesini tutuyor mu, hangi modelde" kaydı ölçülmedi.
NEDEN    Eldiven kenara giderken bilek ve yuvalar da onunla gider. "Yalnız eldiveni değiştir" demek düzenleme modeline bileği eski yerde bırakma izni verir: kopuk el ve ikinci yuva sırası (T01, T15). Bitiş karesi C08 ve C10'da zaten ölçülmemiş bir özelliğe dayanıyor; üçüncü bağımlılığa gerek yok. Tur 2 B5'in derdi hedefin kadrajda kalmasıydı ve video promptu bunu söylüyor: "comes to rest near that edge, with the wrist and its row of bays staying in view".
ARIZA    T01 · T15
ÖNERİ    C07 yalnız başlangıç karesiyle üretilsin; iş emri satır 26 yedek olarak kalsın. İki denemede el kadrajdan çıkar ya da yumruk olursa satır 26'ya geç. Düzenleme promptunda "Change only the right glove" yerine "Move the right forearm, wrist with its row of bays, and glove together" yaz.

### B10 · KÜÇÜK · C07: baş sola, bakış hedefi sağda
KANIT    "front view … her head turned toward the left of the frame, her eyes lowered toward a small amber point of light at the lower edge of the frame in its right half". SELA_v1: "The helmet and the suit are one piece."
NEDEN    Baş solda, hedef sağ altta. Model ya başı noktaya çevirir (kask gövdeden ayrı döner, T10 ve T05) ya da bakışı çapraz üretir. Önden bir gövdede "head turned" ifadesi de kaskı gövdeden ayırıyor.
ARIZA    T10 · T11
ÖNERİ    "her upper body angled toward the left of the frame, the helmet facing the same way as the suit, her eyes lowered. At the lower edge of the frame in its right half, a small amber point of light." Bakış ile nokta ayrı cümlelerde olsun.

### B11 · KÜÇÜK · C01: kopuk uç için çelişkili hareket, üç eşzamanlı hareket
KANIT    C01 Video: "The large radiator arm … slowly retracts and settles into place, while the man drifts away … The free frayed rope end beside the handrail slides very slowly along its own line." KAPAK_iki_uc: "its far end frayed and free, held in place".
NEDEN    Referans "held in place" diyor, video "slides". Korkuluğa bağlı bir ucun kendi doğrultusunda kayması ipin uzunluğunun değişmesi olarak okunur. Model onu yılan gibi dalgalandırabilir (T08). Açılış karesinde radyatör, Bram ve ip ucu olmak üzere üç bağımsız hareket var.
ARIZA    T08 · T10
ÖNERİ    "The free frayed rope end beside the handrail stays where it is." C12'deki "stays in place" ile aynı kalıp olur. FILM C01'deki "kayıyor" da düşer.

### B12 · KÜÇÜK · C08 ve C12: boş uzayı "aydınlatan" ışık hacimsel görünür
KANIT    C08 Video: "white light spreads outward across the frame". C12 Video: "Light spreads outward from the rising sun … brightening the open space between the two figures".
NEDEN    Boş uzayın aydınlanması model için ışık huzmesi ve sis demek; vakumda duman, toz ve buhar görünümüne kayar (T03 22/49; BILINEN §B4). Çıkarım, ölçülmedi.
ARIZA    T03 · T18
ÖNERİ    Işığı yüzeylere bağla. C12: "sunlight reaches the shoulders of both figures and the hatch rim, brightening their white suits". C08: "white light blooms around the sun".

### B13 · KÜÇÜK · C10 başlangıç karesinde kol ile ip arasındaki boşluk yazılı değil
KANIT    Görsel: "the left arm, nearest the camera, hangs loosely half-open at his side … from the hook a rope runs perfectly straight and taut, down and to the left, to the lower-left corner". Bitiş promptu bu boşluğu veriyor: "open empty space between the arm and the rope below it".
NEDEN    Başlangıçta sarkık kol ile çantanın solundan sol alta inen ip aynı bölgeden geçiyor. Kol-ip kesişmesi, kolun kalkışından önce üretiliyor (T01).
ARIZA    T01
ÖNERİ    Görsel'e ekle: "a clear gap between the hanging left arm and the rope".

### B14 · KÜÇÜK · C11: Bram'ın baktığı yön yazılı değil
KANIT    "to a man behind her at the centre-right of the frame: a man … upright, arms at his sides, legs together, a hook caught in the bent frame on the left side of his backpack".
NEDEN    Kanca çantanın sol yanında ve ip Sela'ya gidiyor. Bram Sela'nın baktığı yöne bakmazsa ip gövdesinden geçer, ya da kameraya dönüp ayna vizörünü gösterir (hiçbir referansta ön yüz yok). T11 · T01.
ARIZA    T11 · T01
ÖNERİ    Ekle: "facing the left of the frame like her, the bent side of his backpack toward the camera, the rope reaching the hook on that side".

### KORU
- C10 (b) fon yönü: "sağa" doğru. Kamera Bram'a kilitli ve C11'de çifti sola çeken sarsıntı geliyor. Kayma birkaç derece olduğundan Dünya'nın aydınlık yayı sol yarıdan çıkmaz. (b) iki hareket taşır, (a) bozulursa kullanılsın.
- Ezik çanta solda: C10 (sol arka kamera, sol omuz bandı) ve C12 (arkadan sol = ekran solu, ip Sela'dan geliyor) tutuyor.
- Sela'nın kancası sağ kalçada: C01 ve C02 (sağ yan, kamera tarafı) ve C12 (arkadan sağ = Bram tarafı) tutuyor. C09'da kanca zaten kadraj dışı.
- C03 promptlarında sayı ve sayı kelimesi yok ("left half / right half").
- C09 ve C10 arasında atış ve takılma kesmede. Promptta temas yok.
- 7-10 s ve 6-10 s cümleleri ayrı bloklarda; her promptta ortak dünya cümlesi birebir aynı.

### Red ve sözcük taraması
BULGU YOK — çünkü:
- Prompt gövdelerinde şiddet ve ölüm sözcüğü yok. Tarama: dead, corpse, blood, wound, gore, limp, unconscious, burn, fire, gas, smoke, dust, steam, plume. "body" yalnız başlık notunda geçiyor.
- Milliyet ifadesi yok. Bedenden bir şeyin çıkarılması eylemi yok. Ekran, yazı ve ses sözcüğü yok.
- Çekim kodu, referans kodu ve büyük harfli etiket gövdelerde yok. Her prompt 4.300 karakterin çok altında.
- Kompozisyon reddi: C08 ve C09 yüzsüz, hareketsiz astronot içeriyor. Kayıtlı eşleşen vaka yok (RED defterinde bu sözcüklerle eşleşme çıkmadı). Bulgu yazmadım.

KAPSAM DIŞI: C04'te kehribar noktanın aydınlık Dünya yüzü önünde okunurluğu ve saniye damgasız promptlarda olayların ses kurgusuyla hizası.

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 6 · KÜÇÜK 8
KARAR    TUR KAPANABİLİR
GİRDİ    /Users/dai/github/apex_md/film_md/yatay_2_dk_filmler/THE_WRONG_BURN/PROMPTLAR/G01.md (tam, 603 satır) ·
         /Users/dai/github/apex_md/film_md/yatay_2_dk_filmler/THE_WRONG_BURN/FILM.md (tam, §1-§7) ·
         /Users/dai/github/apex_md/film_md/yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F3_teknik-danisman_2.md (tam) ·
         /Users/dai/github/apex_md/film_md/yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F3_yonetmen_3.md (tam, 330 satır; §0 CEVAPLAR dahil) ·
         /Users/dai/github/apex_md/film_md/uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md (tam) ·
         /Users/dai/github/apex_md/film_md/uretim_hatti/FLOW_GERCEKLERI.md (satır 20-130 ve mod/bitiş-karesi taraması) ·
         /Users/dai/github/apex_md/film_md/kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md (yalnız limp/unconscious/astronaut taraması, eşleşme yok)
YAPILMADI  film_dogrula.py ve prompt_kontrol koşulmadı (bu ajanda kabuk yok); sözcük taraması Grep ile yapıldı.
           Flow'da kare ve video denenmedi. B1-B14'teki sol-sağ ve derinlik çıkarımları (özellikle B4, B5, B12, B14) prompt metinlerinden türetildi, ölçülmedi.
           Flow'un görsel üretimde kaç referansı kabul ettiği FLOW_GERCEKLERI'nde yok (yalnız Karakter için "1 or 2 images").
           C01 ve C10'un kare satırları 5, C12'nin 6 referans taşıyor; sınır ölçülmedi.
           SAHNELEME.md, F3_yonetmen_4.md, ODA/NOTLAR.md ve öteki eleştirmen çıktıları görev girdisi olmadığı için okunmadı.
```

---

## Fable kararı (09.10.2026) — F5 tur 1 kapanışı

İki eleştirmen de ÖLÜMCÜL 0 → tur kapanıyor. Bütçe 44/50 (40 geçildi: CİDDİ/KÜÇÜK için yeni çağrı açılmaz). CİDDİ/KÜÇÜK bulgular **birleştirme geçişiyle** (yeni-film §2c) yazara gider; goruntu-yonetmeni aynı çağrı içinde sürdürülür (SendMessage, sayaca girmez; HELMET dersi). Eleştirmenler yeniden çağrılmaz; denetci Ö4 ile sınar.

1. **Ortak bulgular (devamlilik B1 = teknik B1; devamlilik B2 = teknik B2; devamlilik B7 = teknik B13; devamlilik B8 = teknik B8/3; devamlilik B13 = teknik B14):** yazar tek cevapla kapatır.
2. **C07 bitiş karesi:** teknik B9 "kullanma" → Fable varsayılanıyla aynı: C07 yalnız başlangıç karesi; iş emri satır 26 yedek, düzenleme promptu teknik B9 ifadesiyle düzeltilir. Karar kapandı (NOTLAR KARARLAR'daki "teknik-danisman karar verir" maddesi).
3. **C08 siluet boyu:** teknik B8 "iki karede aynı boy" → sahneleyici §4b'nin yazılı yedeğiyle aynı; uygulanır. FILM §4 C08 metni ("hafifçe büyüyor") değişmez: yönetmen eseri; sapma NOTLAR'a, F7 KARE denetimi "Bram önünde" bilgisini ölçer.
4. **C01 kopuk uç (teknik B11):** prompt "stays where it is" (KAPAK_iki_uc referansıyla birebir); FILM §4 C01 "çok yavaş kendiliğinden kayıyor" değişmez, sapma NOTLAR'a (F7'de uç kımıldamazsa bilgi kaybı yok: teknik B7 F3 kararı zaten "sarkmaz").
5. **Yeni referans önerileri (devamlilik B6 SELA_yuz_v1 · teknik B6 SELA_arka_v1; teknik "yüz için ayrı gerekmez" diyor):** yazar KABUL/RED ile karar verir (FLOW §5 karakter 1-2 görsel sınırı içinde). Kabul ettiği her yeni referans için FILM §3 satır metnini ("Referans · Dosya · v1 · Kullanan çekimler") YAZAR NOTLARI'na yazar; Fable §3'e birebir kopyalar.
6. **FILM §4 ile sapmalar:** yazar uygulanan her sapmayı (C01 uç, C08 siluet, varsa başka) YAZAR NOTLARI'nda "FILM §4 SAPMA" listesinde toplar; Fable NOTLAR KARARLAR'a taşır. §4 metni bu fazda değişmez.
7. **Teknik B3/3 ("pushed" → T03) · B4 (C08 güneş-siluet hizası) · B12 (hacimsel ışık):** ölçülmemiş çıkarım; yazarın KABUL/RED'i. RED gerekçeli olur.
8. Sonra: film_dogrula --bolum cekim sahneleme prompt → denetci (Ö + F5) → Fable → F6.
