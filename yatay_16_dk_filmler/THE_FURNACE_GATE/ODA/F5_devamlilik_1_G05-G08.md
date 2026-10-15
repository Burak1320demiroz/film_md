**Okunmayan kısımlar (koordinatörün istediği liste).** Görev girdisinin hepsi açıldı: G05–G08 tam, G01 satır 1–200 (REFERANS PROMPTLARI ve C01), FILM.md §3·§4·§5 tam. Şunlar okunmadı:
- G01'in C02–C12 bölümü ve FLOW İŞ EMRİ. Yalnız grep eşleşmelerinden gördüğüm satırlar var (satır 212, 217, 255, 381; bağlamları okunmadı).
- G02, G03, G04. G02 ve G03'te yalnız "EMP" grep eşleşmesini gördüm.
- `THE_FURNACE_GATE_16MIN_96_CLIPS.md`, NOTLAR.md, SAHNELEME.md, ODA/*.
- ARIZA_LISTESI.md, GECIS_VE_SES_SUREKLILIGI.md, PROMPT_HATA_ATLASI.md.
- ILK_30_SANIYE_KILAVUZU.md (yalnız ilk 5 satır).

Tarama, koordinatörün tur sınırı mesajıyla yarıda kesildi. Aşağıdaki "ölümcül yok" sonucu bu kesik taramaya aittir.

---

### B1 · CİDDİ · C56'da Rhea'nın bilek bağlantısı sol kolda; referans sayfası ve önceki promptlar sağ kol diyor
KANIT G05 C56 Görsel: "The unmarked ivory wrist-link sits on the pearl sleeve of her left forearm". G05 başlığı: "Rhea'nın bilek bağlantısı SOL ön kolunda (FILM.md §3 yan yazmıyor; benim seçimim …)".
Karşı kanıt: G01 2.RHEA sayfası "an unmarked ivory wrist-link on her right wrist". G01 başlık satır 20: "Bilek bağlantısı Rhea'nın SAĞ bileğinde … (1.LEON · 2.RHEA sayfalarında sabit)". G01 satır 212, 217, 255, 381'de de "right forearm" eşleşmesi var (C02, C04, C10 görsel/video).
NEDEN Asimetrik işaret (hangi kol) sayfayla çelişiyor. C56 görselinde model sayfadaki sağ bilekle metindeki sol kolu uzlaştıramaz; C04, C10 ve C56 ekranda farklı kolu gösterir.
ARIZA yeni (ARIZA_LISTESI açılmadı)
ÖNERİ C56'yı sağ ön kola çevir: kamera sağ ön kolun üstünde, bağlantı sağ kolda, başparmak sol eldivenden girer. G05 başlığındaki "SOL ön kol" cümlesini sil.

### B2 · CİDDİ · C64'te "başı kadraj soluna dönük" ile "sağ çene yarası görünür" aynı karede mümkün değil
KANIT G06 C64 Görsel: "seen in three-quarter view from her right front with her head turned toward frame-left, so that her small right-chin scar shows plainly".
G06 C64 notu: "yüz kadraj soluna dönük → sağ yanak kameraya".
Aynı dosyanın kuralı G05 başlığında doğru yazılmış: Rhea karenin sağına döner, sağ çene kameraya (C50 ve C58 böyle).
NEDEN Yüz kadraj soluna dönünce kameraya sol yanak döner. Model yarayı hiç çizmez ya da yanlış yüze çizer. Yara Rhea'nın kimlik işareti.
ARIZA yeni
ÖNERİ C64'te başı kadraj sağına çevir: "head turned toward frame-right", turuncu kol karenin sağında. Ya da yarayı sağ ön ¾'te bırakıp bakışı kameraya yakın tut. Not metnindeki gerekçeyi de düzelt.

### B3 · CİDDİ · C68 ve C72'de hangi gantri kolunun yakın, hangisinin uzak olduğu kendi içinde çelişiyor
KANIT G06 C68 Görsel: "its port flank along the upper half of the frame. In the upper foreground the port gantry clamp arm … Across the hull, lower in the frame and farther from the lens, the opposite starboard clamp arm". C72 Görsel'de aynı yapı var.
NEDEN Yukarıdan 45° bakışta kadrajın üst yarısı uzak, alt yarısı yakındır. Metin "üst = yakın, alt = uzak" diyor. Hareket eden çene (port) iki çekimin tek olayı, yani tam çelişen kısım. Model hangi kolun açılacağını karıştırabilir.
ARIZA yeni
ÖNERİ Burun sağda kalacak şekilde "upper half, farther from the lens" ve "lower half, nearer the lens" yaz. Hareketli port çenesi küçük kalmasın diye 24 mm yerine 35 mm kullan ve çeneyi "mid-frame" konumlandır. C68 ve C72'de aynı değişiklik.

### B4 · CİDDİ · Dış çekimlerde gök/uzay cümlesi film içinde üç biçimde; bu gruplarda 10 dış görselde hiç yok
KANIT
- G01 C01: "Everything hangs in deep black space with sparse stars." G01 başlık satır 18 bunu her dış çekim için kural koyuyor.
- G05 C52 · C57 ve G06 C62 · C68 · C72: "Deep black space with sparse stars surrounds the foundry."
- G02 (grep): "… surrounds the foundry, and a huge curved blue gas giant fills the far background."
- G07 C74 · C80 · C81 · C84 ve G08 C85 · C87 · C89 · C91 · C92 · C96 görsellerinde gök cümlesi yok. C96'da yalnız gaz devi geçiyor.
- G07 başlığı: "§3'te ayrı bir gök cümlesi yok". G08 başlığı: "DIŞ ışık cümlesi gök cümlesi sayıldı". Her grup farklı karar vermiş.
FILM §4 C01 risk sütunu: "T18 gök cümlesi her dış planda birebir".
NEDEN Kesmede yıldız yoğunluğu, arka plan ve gaz devi görünürlüğü sıçrar. Dış kesmelerin çoğu bu çekimlerde.
ARIZA T18
ÖNERİ FILM §3'e tek gök cümlesi sabitle (G01'inki: "Everything hangs in deep black space with sparse stars."). Bu 10 görselin hepsine ışık cümlesinden hemen önce ekle. G02, G05, G06'daki "… surrounds the foundry" biçimini onunla değiştir.

### B5 · CİDDİ · Replik, eylemin tamamlanmasından önce söyleniyor; düzeltme C58, C60 ve C84'te yapıldı, C65, C72, C85'te yapılmadı
KANIT
- G06 C65: replik 0-3 vuruşunda ("Catch engaged."), kol durdurucuya 3-7'de oturuyor.
- G06 C72: "Both clear. Come back to the ark." 0-4'te, sancak çenesi 7-10'da açık.
- G08 C85: "Hard seal." 0-3'te, kelepçe 7-10'da oturuyor.
- Düzeltilenler: G07 C84 ("Contact." ikinci vuruşa, not: "R82 Saniye 1.5 → ~6.0 olmalı"), G05 C58 ("Core seated." 4-7'ye), G05 C60 (3-7'ye).
NEDEN Tamamlanmış durumu bildiren cümle, görüntüde iş bitmeden 5-8 s önce duyulur. Replik vuruşun son cümlesi olduğundan model onu o vuruşta söyler.
ARIZA yeni
ÖNERİ Replik cümlesini tamamlanma vuruşuna taşı: C65 → 3-7, C72 → 7-10, C85 → 7-10. FILM §5 saniyelerini güncelle (R67, R73, R83).

### B6 · CİDDİ · 10 s vuruş iskeleti tekrar ediyor; hiçbir çekimde 4 vuruş yok
KANIT Grep sayımı, 48 çekim:
- 0-3·3-7·7-10: 18 çekim (G05 3, G06 1, G07 6, G08 8). G08'de 12 çekimin 8'i aynı iskelet.
- 0-4·4-7·7-10: 13 çekim (G05'te 6).
- Bu ikisi 31/48. 4 vuruşlu çekim yok; 2 vuruşlu 5 çekim var (C50, C73, C76, C77, C96).
- G01 başlık satır 22: "aynı iskelet en çok iki çekimde".
- Son vuruşlar çoğu zaman yalnız tutuş + kamera yavaşlaması: C51 7-10 "The push eases closer … glow steady"; C60 7-10, C65 7-10, C67 6-10, C71 6-10 "the glove stays wrapped around the grip".
NEDEN Tempo düzlüğü (LAST_GATE'te ölçülmüş) ve son vuruşta donma riski.
ARIZA yeni
ÖNERİ G08 ve G07'de en az dört çekimi 4 vuruşa (0-2·2-5·5-8·8-10) ya da 0-5·5-10'a çevir. Aday çekimler: C89, C91, C92, C85, C90. Eldiven-kol çekimlerinin (C65 · C67 · C71) son vuruşuna yeni bir evre koy; yalnız "stays" yazma.

### B7 · CİDDİ · Sayfalarda gerekli yan paneller yok: Leon'un sağ profili, Rhea'nın sol yanı
KANIT
- 1.LEON panelleri: ön, arka, "full-length from his left side", sol ¾ yüz, eldiven. Sağ profil paneli yok.
- Leon çekimleri: C76 "seen in right profile … facing frame-right" (panel: face close-up). C79 "shows the right side of his face in profile" (panel: side full-body). C55 ve C82 "¾ from his right front" (panel: face close-up).
- 2.RHEA panelleri sağ yan ve sağ ¾. G07 C75: "head turned toward the hatch at frame-left … left glove" (panel: face close-up, sağ ¾). Rhea'nın sol yüzü yok.
NEDEN Kimlik işareti (Leon sol şakak, Rhea sağ çene) panelin gösterdiği yanda. Gösterilmeyen yan modele bırakılır; yara karşı yüze ya da iki yüze çıkabilir.
ARIZA yeni
ÖNERİ FILM §3'ün yetkisiyle G01 yazarı yeni panel ekler, adı değişmez: 1.LEON'a `right-profile close-up panel`, 2.RHEA'ya `left-profile close-up panel`. C55, C76, C79, C82 ve C75'in panel anahtarını yeni panele bağla.

### B8 · CİDDİ · Yasaklı `body` sözcüğü dokuz görsel promptta; üç grup başlığı "hiçbir promptta geçmez" diyor
KANIT "full-body panel" şu promptlarda geçiyor:
- G05 C49 ("back full-body panel"), C58 ve C60 ("front full-body panel").
- G06 C63, C65, C67 ("side full-body panel").
- G07 C73, C77 ("front full-body panel"), C79 ("side full-body panel").

Başlıklar: G05 "`body` … hiçbir promptta geçmez"; G06 "`body` · `dead` … hiçbir promptta geçmez"; G07 "`body` sözcüğü ve türevleri hiçbir promptta geçmez". G08 başlığı ise aynı panelleri baştan `the full-length front panel` diye yazdığını söylüyor.
BILINEN_TUZAKLAR §A: `body` listede; "olumsuz blokta bile" red sebebi.
NEDEN Aynı film içinde iki farklı kelime politikası var. Flow bir kez reddederse dokuz kare tek tek değişir; başlıklardaki beyan yanlış.
ARIZA BILINEN_TUZAKLAR §A
ÖNERİ Bütün gruplarda panel anahtarını G08 gibi `full-length` yaz. Aynı anda FILM §3'teki iki panel adını (`front/back/side full-body panel`) `… full-length panel` yap. G01 başlık satır 20-21'deki "red gelirse" ertelemesini kaldır.

### B9 · KÜÇÜK · Aynı numaralı referansın rol etiketi gruptan gruba değişiyor
KANIT
- 5: "(foundry)" G05, G06, G08; "(station)" G07 C81.
- 1, 2, 3, 6: "(man) · (woman) · (tug) · (ark)" G05–G07; "(the man) · (the woman) · (the tug) · (the ark)" G08.
- 15: "(accessories)" G05, G07; "(tools)" G08.
- 4: "(cockpit)" G07; "(tug cockpit)" G08.
- 9: "(loading bridge)" G05; "(bridge)" G07.
- 14: "(service catwalk)" G07; "(service catwalk and socket)" G08.
- C94: "(the spent core)" ve "(gate-control room)".
NEDEN Anahtar cümle sayı + rol çiftine dayanıyor; rol kelimesi oynayınca eşleme zayıflar.
ARIZA yeni
ÖNERİ FILM §3'e tek rol tablosu koy ve sekiz grupta uygula: 1 man · 2 woman · 3 tug · 4 cockpit · 5 foundry · 6 ark · 9 bridge · 10 core · 12 control room · 14 catwalk · 15 accessories.

### B10 · KÜÇÜK · Video promptlarında kişi adı geçiyor
KANIT G06 C64 Video: "while Rhea shifts her weight". G06 C70 Video: "a slow, small push toward Leon". G08 başlığı: "ad yazılmaz — tek istisna §3 voice-over cümlesi". BILINEN_TUZAKLAR §C: büyük harfli ad göğüs kutusuna basıldı (ORION).
NEDEN Ad, giysiye isim etiketi olarak yazılabilir.
ARIZA yeni
ÖNERİ "the woman shifts her weight", "a slow, small push toward the man".

### B11 · KÜÇÜK · Çekimlerin istediği nesneler referans sayfası promptlarında yok
KANIT
- C54: "fixed navy grab rail". Not kendisi: "Korkuluk 13.KOMUTA sayfasında yazı değil".
- C61: "Heavy fixed metal contact strips run along the cradle rim". 12.KONTROL_ODASI sayfasında bara konnektörü var, şerit yok.
- C73: "one round red bridge-warning lamp sits dark". Sayfada yok.
- C83: "the broad unmarked battery-power toggle of the tug socket housing". 14.ISKELE sayfasında yaka kelepçesi ve lambalar var, anahtar yok.
NEDEN Bu nesneler yalnız metinle taşınıyor; C84, C85, C87'de soket anahtarsız çizilebilir.
ARIZA yeni
ÖNERİ G01 sayfa promptlarına birer cümle ekle: 13'e korkuluk, 12'ye kontak şeritleri ve kırmızı köprü lambası, 14'e soket anahtarı.

### B12 · KÜÇÜK · Ark komutasındaki bilek bağlantısı yuvası C55'te boş, C78'de dolu; cihaz sayısı belirsiz
KANIT G05 C55 Görsel: "the unmarked wrist-link docking cradle sits empty". G07 C78 Görsel: "the unmarked ivory wrist-link sits seated in its cradle". Araya bunu yerleştiren çekim yok. Ayrıca Rhea'nın koluna takılı bağlantı (C56) ve kokpit yuvasındaki bağlantı (C88, C93) var.
NEDEN Aynı cihaz mı üç ayrı cihaz mı belli değil; durum merdiveninde bir nesne birden belirir.
ARIZA yeni
ÖNERİ C55'te yuvaya bağlantıyı oturmuş yaz (C78 ile aynı). Cihaz sayısını (ark yuvası ayrı, Rhea'nınki ayrı) FILM §3 sabit tasarıma tek cümleyle ekle.

### B13 · KÜÇÜK · C84→C85'te kelepçenin hangi yakada olduğu belirsiz
KANIT G07 C84 Görsel: "its round bow collar aligned with … socket … and one broad hinged clamp standing open on the collar". G08 C85 Görsel: "The socket's one broad hinged clamp stands open above its latch plate". FILM §3'te hem 3.KESTREL yakasında hem 14.ISKELE soketinde birer menteşeli kelepçe tarif edilmiş; C80 ve C87'de tug yakası "unlatched".
NEDEN C85, C84'ün bıraktığı kelepçeyi kapatmayabilir; iki kelepçe ya da yanlış kelepçe çıkabilir.
ARIZA yeni
ÖNERİ C84'te "one broad hinged clamp standing open on the socket collar" yaz; tug yakasının kapalı ve düz olduğunu ekle.

### B14 · KÜÇÜK · G08 C91 panel seçimi metinle çelişiyor
KANIT G08 C91 Görsel: "two giant gantry clamp arms standing open … using the gate open panel". G01 5.FOUNDRY sayfası "gate open panel": "the clamps still locked". C89 doğru paneli seçmiş (`clamps open panel`).
NEDEN Panel kelepçeleri kapalı gösteriyor, metin açık istiyor.
ARIZA yeni
ÖNERİ C91'de `clamps open panel` kullan.

### B15 · KÜÇÜK · Referans promptlarında büyük harfli "EMP"
KANIT G01 2.RHEA: "one small matte-grey fictional EMP puck". G01 15.ARACLAR: "one small matte-grey fictional EMP puck with an amber indicator". BILINEN_TUZAKLAR §C: `EVA` kısaltması sırta basıldı. G05–G08 prompt gövdelerinde "EMP" yok. G02 ve G03'teki grep eşleşmeleri kapsam dışı (bağlam okunmadı).
NEDEN Kısaltma, disk ya da giysi üzerine yazı olarak basılabilir.
ARIZA yeni
ÖNERİ "one small matte-grey fictional disruptor puck" yaz; panel anahtarı `emp puck panel` küçük harfle kalabilir ama promptta geçmesin.

### B16 · KÜÇÜK · EKLE satırı biçimi gruptan gruba değişiyor
KANIT G07 (ve G01) EKLE: "başlangıç karesi: kare/C73.png · referans (yükleme sırası): ref/2.RHEA_v1.png …" FLOW "Frames to Video" altında. G05, G06, G08: "KARE (Görsel): … · VİDEO (Frames to Video): yalnız kare/…". G05 başlığı: Frames to Video'ya referans eklenirse mod Ingredients'e kayar.
NEDEN Satır harfi harfine uygulanırsa video işine referans yüklenir.
ARIZA yeni
ÖNERİ G07 EKLE satırlarını G05 biçimine çevir.

### B17 · KÜÇÜK · FILM.md §4 Referans sütunu ve §3 "Kullanan çekimler", PROMPTLAR EKLE ile 9 çekimde uyuşmuyor
KANIT Grup yazarları gerekçeyle referans çıkarmış, FILM.md güncellenmemiş:
- C50 (−15), C53 (−10), C55 (−10, −15), C56 (−10), C78 (−10).
- C79 (−5, −10, −15), C86 (−5, −6, −10, −15), C93 (−5), C95 (−10, −15).

NEDEN `film_dogrula.py` sayı eşlemesi kırılır; FILM.md EKLE'den farklı kalır.
ARIZA yeni
ÖNERİ Birleştirmede §4 Referans sütununu ve §3 "Kullanan çekimler" listelerini EKLE'ye göre güncelle.

---

KORU: ORTAK GÖRÜNÜM cümlesi G05–G08'de her dosyada 24/24 promptun sonunda birebir (grep).
KORU: ORTAM SESİ cümlesi 48 video promptunun hepsinde §3 metniyle aynı ve doğru mekâna bağlı (grep).
KORU: MEKÂN IŞIĞI cümlesi 48 görselde §3 ile aynı kelimelerle yazılı; kimlik tabanı kelimeleri gözle karşılaştırıldı, fark bulunmadı (karakter karakter diff yapılmadı).
KORU: Her videoda replik vuruşun son cümlesi ve ilk vuruş hareketle başlıyor; ağız kadrajda çekimlerde öteki ağız kapalı yazılmış (G08).

KAPSAM DIŞI: C48→C49 grup sınırı (G04 okunmadı). Faz 7 kare denetimi (kare dosyası verilmedi).

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 9
KARAR    TUR KAPANABİLİR (ölümcül bulgu yok; tarama yarıda kaldı, aşağıya bak)
GİRDİ    PROMPTLAR/G05.md · G06.md · G07.md · G08.md (tam); PROMPTLAR/G01.md satır 1–200;
         FILM.md §3 · §4 · §5 (ayrıca §6 geçiş tablosu ve §7 okundu);
         uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md; ILK_30_SANIYE_KILAVUZU.md ilk 5 satır.
         Grep: ORTAK GÖRÜNÜM, ışık, ortam sesi, vuruş sınırları, "Leon|Rhea", EMP, gök cümlesi, bilek tarafı.
         EKSİK: yok (görevin verdiği girdiler eksiksiz açıldı).
YAPILMADI  ≤4.300 karakter ölçümü · film_dogrula.py koşusu · ARIZA_LISTESI eşlemesi (ARIZA sütunu "yeni") ·
         G02–G04 ile gruplar arası karşılaştırma · plan dosyası ve GECIS_VE_SES_SUREKLILIGI/PROMPT_HATA_ATLASI karşılaştırması ·
         kare denetimi · C74/C75/C77/C81 dış-iç geometrisi (port/sancak, ark yönü) tam doğrulanmadı.
```

Eleştirdiğim dosyalar (hepsi `/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/` altında):
- PROMPTLAR/G05.md
- PROMPTLAR/G06.md
- PROMPTLAR/G07.md
- PROMPTLAR/G08.md
- PROMPTLAR/G01.md (REFERANS PROMPTLARI bölümü)
- FILM.md
