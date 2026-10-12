# F5 · teknik-danisman · tur 1 — THE_PLANET_THIEF

> Girdi: PROMPTLAR/G01.md · G02.md · G03.md (risk sütunu dolu çekimler + 9 referans sayfası) + FILM.md §3 §4. Ajanın cevabı aynen (Fable kaydı, 10.10.2026).

# Faz 5 · tur 1 · teknik-danisman · THE_PLANET_THIEF · G01-G03

Kapsam: risk sütunu dolu 20 çekim (C01-C04, C06-C09, C11-C15, C17-C24) ve 9 referans sayfası. Hiçbir promptta büyük harfli jeton, çekim kodu ya da başlık satırı yok. Vuruş planları 0'da başlıyor, 10'da bitiyor ve boşluksuz. C05, C10 ve C16'ya ayrıca baktım; bulgu çıkmadı.

### B1 · CİDDİ · "body" kelimesi G02'de dört promptta geçiyor
KANIT    G01 başlık notu: `"body" sözcüğü hiçbir promptta geçmez (full-length · fuselage · hull yazıldı).` G02 C09 Görsel: `using the rear full-body panel`. Aynı kalıp C11 ve C12'de `using the front full-body panel`, C14'te `using the rear full-body panel`.
NEDEN    `body` kelimesi SLOW STONE S4'te ve LAST SPAN S8-S9'da üretim reddi aldı. G01 bunu bilerek önlemiş, G02 aynı kelimeyi dört yerde geri getirmiş. Reddedilirse 4 kare ve ona bağlı 4 video düşer.
ARIZA    BILINEN_TUZAKLAR §A satır 1 (kelime reddi, RED 8-11)
ÖNERİ    `full-body panel` yerine `full-length panel` yaz. G01'deki sayfa promptu zaten bu biçimde.

### B2 · CİDDİ · C14: pencereden geri çekilince görüş genişlemez; kare zaten tam düzeni gösteriyor
KANIT    Video: `a slow dolly outward from the panoramic glass, the window edges and railing drifting outward as the view starts to widen` ve `more of the six-world arrangement opens around the artificial sun`. Görsel: `Six rocky worlds float at separate depths, each held by thin amber containment arcs`.
NEDEN    Pencereden geri gidince dışarıdan görünen alan daralır, oda ve çerçeve görünür. Altı dünya ilk karede zaten açık olduğu için "açılma" için gösterilecek yeni bir şey yok. Model ya çevreyi uydurarak büyütür ya da zoom-out gibi eritir. Bu çekim öncelikli önizlemede ve filmin ana açılımı.
ARIZA    T07 (kamera kayması), yeni nokta: optik yön çelişkisi
ÖNERİ    Hareketi cama doğru ileri dolly yap. Kare, pencere çerçevesinin yarısı kadrajda ve dünyalar çerçeveyle kısmen kırpılmış olsun. Yaklaştıkça çerçeve dışarı kayar ve düzen gerçekten açılır. Geri çekilmeyi C24'e bırak. FILM.md §4 C14 kamera sütunundaki "geri dolly" de değişir.

### B3 · CİDDİ · C06→C07: soket önce yan duvarda, sonra tavanda
KANIT    C06 Görsel: `a small round docking socket on a recessed side wall at frame-right`. C06 Video: `toward the docking socket on the right-hand wall`. C07 Görsel: `directly beneath the ark's fixed round docking socket on the berth ceiling`. C07 Video: `rise ... in a straight vertical line beneath the fixed socket`. 5.YANASMA_KORIDOR sayfası ise soketi `at the far wall` diye veriyor.
NEDEN    Halka aracın sırtında. Sırt halkası yan duvardaki sokete bakamaz, tavandakine bakar. Üç yerde üç konum var. Kesmeden sonra model C07'de geometriyi kendi uydurur ve izleyici yanaşmanın yönünü okuyamaz.
ARIZA    T11 (yön/coğrafya)
ÖNERİ    Tek konum seç: tavan. C06'da soket "in the canyon's upper wall, overhead at frame-right" olsun. Araç altından kayarak hizalansın. Böylece C07'nin ilk karesi C06'nın sonunun devamı olur. 5.YANASMA_KORIDOR'daki "far wall" ifadesini de aynı hizaya çek.

### B4 · CİDDİ · C08: temas anı kadrajda ve aynı çekimde iki durum değişimi
KANIT    Video: `0-3 s: ... the collar makes a short straight contact movement and the two rigid rings meet. 3-8 s: The one visible rigid clamp begins to rotate slowly on its hinge ... 8-10 s: The clamp finishes its swing and settles against the collar`.
NEDEN    Önce halka teması, sonra menteşeli kelepçenin kapanması var. İkisi de nesne-nesne teması. Model halkaları ya kaynaştırır ya da kelepçeyi halkanın içinden geçirir. Ayrıca C08 karesi, henüz var olmayan C07 videosunun son karesine bağlanıyor (bu fiilen video→kare bağımlılığı).
ARIZA    T01 (aynı kapanış yolu: temas gösterilmez, kesmeyle atlanır); `yeni`: ikinci durum değişimi
ÖNERİ    Temas C07 ile C08 arasındaki kesmeye düşsün. C08 karesinde halkalar oturmuş olsun (boşluk yok) ve kelepçe açık dursun. Videoda tek hareket kelepçenin kapanması kalsın: `0-3 s` kilitli bekleme, `3-8 s` kelepçe döner, `8-10 s` yaslanır. Böylece C07 son karesine bağımlılık ortadan kalkar ve C08 tek başına öncelikli önizleme olarak koşabilir.

### B5 · CİDDİ · C12: çekimin tek bilgisi halka ışığı, ama prompt eldeki kavramayı ve çekimde görünmeyen giysiyi de istiyor
KANIT    `his white gloved hands grip the matte-black cutter, whose edge fills the right side of the frame, all correctly proportioned`. Aynı promptta: `a man's ivory-white pressure suit with rigid ivory chest armor, graphite shoulder panels and joint seals, a burnt-orange stripe on each upper arm`. G02 başlık notu ise `C12 yalnız kol/eldiven` diyor.
NEDEN    85 mm'lik bileklik yakın planında göğüs zırhı, omuz paneli ve üst kol şeridi kadraja giremez. Bunları sayınca model kadrajı açar ya da bunları bileğe yapıştırır. İki eldivenli elin kesiciyi kavraması, hiç bilgi taşımayan bir T01 yüzeyi ekliyor.
ARIZA    T01 · T05
ÖNERİ    Giysi cümlesini "ivory sleeve cuff above a white glove, broad dark strap" ile sınırla. Kesiciyi kadrajdan çıkar ve eller kadraj dışında kalsın. Kesici sürekliliğini C11 ve C19 taşır. Videoda `the wrist and the cutter edge move only with a slight natural tremor` cümlesi `the wrist moves only with a slight natural tremor of breathing` olsun.

### B6 · CİDDİ · C20: halka ilk karede zaten yanık; başparmak basışı kadrajda ve anatomik olarak zor
KANIT    Görsel: `an ivory rectangular wrist scanner with a black glass face showing one plain cyan circular light, on a broad dark strap, sits on his left wrist, and his left thumb is close to the scanner's side switch`. Video: `5-7 s: his thumb makes one small press on the switch.` ve `7-10 s: the cyan ring on the scanner lights up and stays steadily lit`.
NEDEN    Üç sorun var:
- Halka 0. karede yanıyorsa "lights up" modeli söndürüp yakmaya ya da sıçramaya iter.
- Sol başparmağın aynı kolun bileğindeki cihaza basması elin bükülmesini gerektirir.
- Basış temas anının kendisi ve 2 sn'e sıkıştırmak onu kadrajdan çıkarmıyor.
ARIZA    T01 · T10
ÖNERİ    Kare: halka sönük ya da loş olsun ve başparmak kadrajda görünmesin (el sırtı kameraya dönük). Video: yalnız halka loştan parlağa geçsin, basış yazılmasın; basış C19→C20 kesmesinin içinde kalsın. Vuruşlar: `0-5 s` itiş + duruş, `5-8 s` halka parlar, `8-10 s` sabit.

### B7 · CİDDİ · C21: bitiş karesi düzenleme talimatı yanlış görsele bağlı
KANIT    `Reference 4 (ark): keep the ark and Earth exactly as in it. Move the whole spherical Earth deeper through the aperture so that most of its trailing hemisphere is covered by the near amber rim`. İş emri satır 6: `kare/C21.png · ref/4.ARK_v1.png`.
NEDEN    Ref 4'te Dünya girişin tamamen dışında ve kamera farklı. "Exactly as in it" ifadesi modeli C21 karesine değil ref 4'e çeker. Düzenlenen görsel C21 karesi olmalı. Bu, filmin ana görsel vaadi olan çekimin bitiş karesi. Frames to Video'nun bitiş karesini tutup tutmadığı da hâlâ ölçülmedi (FLOW_GERCEKLERI §9).
ARIZA    T09 · T07
ÖNERİ    Talimat şöyle olsun: "In the first attached image, keep the camera, the ark, the light, and Earth's size and continents exactly; move the whole spherical Earth deeper through the aperture ...". Ref 4'ü yalnız ark dokusu için ikinci görsel olarak kullan. İki deneme planla: biri başlangıç+bitiş karesiyle, biri yalnız başlangıçla. "İsteğe bağlı" kaydı kalksın ve karşılaştırma NOTLAR.md'ye yazılsın.

### B8 · CİDDİ · 1.ELIAS: iki panel tek çekimde isteniyor ve profil paneli yok
KANIT    C11 Görsel: `take his face from it, using the head-and-shoulders portrait panel, and his helmet and pressure suit from it, using the front full-body panel`. Sayfa panelleri: önden, arkadan, portre. C11 (`stands at frame-left in profile`) ve C19 (`Medium close side view`) profil çekimi. G02 notu: `Yandan görünüş sayfada yok`.
NEDEN    Aynı görselden iki panel istemek, modeli sayfa düzenini (yan yana üç figür) sahneye taşımaya ya da yüzü yanlış figüre bağlamaya iter. P17 ölçülmedi. Profilde sırt çantası derinliği, omuz paneli ve rozet için kaynak yok, model uydurur. Elias 9 çekimde.
ARIZA    T05 · T16
ÖNERİ    Sayfaya dördüncü panel ekle: "full-length from his right side" (C11 ve C19'da sağ yüz, yani yara görünüyor). P17 ölçümüne kadar her çekimde yalnız tek panel adı geçsin. C11'de yüz için yalnız portre paneli kullan; giysi zaten metinde sayılı.

### B9 · CİDDİ · 6.GOZLEM_BOLMESI sayfası koridorla ve üç çekimle ters
KANIT    Sayfa 6: `At frame-left a thick vertical transparent conduit is filled with steady amber energy`, `At frame-right a tall narrow glass observation slit`, `The corridor entrance behind camera opens directly into this chamber`. Sayfa 5: `a thick transparent cylinder ... runs continuously along the right wall`. C11 Görsel: `The vertical amber conduit rises at frame-right`. G02 notu: `R06 sayfasındaki yerleşimin aynalısıdır`.
NEDEN    Koridorun sağ duvarındaki hat düz girince bölmede de sağda kalır. Sayfa 6 bunu solda veriyor. C11, C19 ve C20 referansa ters yerleşim istiyor ve model referansın düzenini kopyalar. Bu, ekran yönü kayması ve arka plan değişimi riski.
ARIZA    T11 · T04
ÖNERİ    Sayfa 6 henüz üretilmedi, maliyeti sıfır: promptu aynala. Hat frame-right, cam yarık frame-left olsun. C11/C19 notlarındaki "ayna" uyarısı kalkar.

### B10 · KÜÇÜK · Elias kimlik yığını (HİPOTEZ)
KANIT    1.ELIAS: `a 38-year-old orbital rescue pilot with a lean athletic build, weathered light olive skin, short dark hair slightly grey at the temples, dark brown eyes, close dark stubble and a small old scar through his right eyebrow`. Aynı yığın C11, C19 ve C20'de tekrarlanıyor, üstüne portre referansı da ekli.
NEDEN    Kesin yaş, ten, saç ve yüz izi üst üste "ünlü kişi" reddi vakasına (SINKING STAKE) benziyor; sonucu sınanmadı. Kök sayfa reddedilirse 9 çekim düşer. Referans zaten ekliyken tekrarın faydası yok.
ARIZA    BILINEN_TUZAKLAR §A satır 7 ve satır 5 (RISING SNOW: kesin yaş + yara izi)
ÖNERİ    C11/C19/C20'de yaş, ten, saç, göz ve sakal listesini sök, "face from the portrait panel" ve "small scar through his right eyebrow, visible through the visor" kalsın. Sayfa promptunda "38-year-old" gitsin ("adult man" zaten var).

### B11 · KÜÇÜK · Prompt gövdesinde "no/not" kalıpları
KANIT    C19 ve C20: `a single circular blue-and-gold mission badge on his left chest with an abstract crescent and no lettering`. G01 7.KASA: `not open outer space`. G03 C18: `without touching its surface`.
NEDEN    "lettering" kelimesi rozete yazı basma riskini artırabilir (P13 ölçülmedi). C11 ve sayfa 1'deki rozet cümlesi bu ekle olmadan yazılmış. Dolayısıyla kimlik cümlesi çekimler arasında da tutarsız.
ARIZA    T06 · "no X" yasağı
ÖNERİ    `and no lettering` sil, C11 ve sayfa 1 ile aynı cümleye dön. `not open outer space` yerine `enclosed by built walls` yaz. `without touching its surface` yerine `curve around Earth at a small distance` yaz.

### B12 · KÜÇÜK · EKLE bloğu Frames to Video altında referans listeliyor
KANIT    G01 C01: `FLOW Frames to Video` / `EKLE başlangıç karesi: kare/C01.png · referans (yükleme sırası): ref/4.ARK_v1.png`. Aynı kalıp bütün çekimlerde var.
NEDEN    Referans kare üretimine ait. İş emri tablosu doğru (videoda yalnız kare), ama blok yanıltıcı. Videoya referans eklenirse mod Malzemeden video'ya kayar: 8 s, Quality'de yok.
ARIZA    yeni (FLOW_GERCEKLERI §1)
ÖNERİ    EKLE satırını `KARE İÇİN:` ve `VİDEO İÇİN: yalnız kare/Cxx.png` diye ikiye böl.

### B13 · KÜÇÜK · Kilit olay son 2 saniyede
KANIT    C08 `8-10 s: The clamp finishes its swing and settles`. C22 `8-10 s: the last sliver goes out under the front`. C18 `8-10 s: Earth's leading edge comes right up to the intake plane`. C07 `7-10 s: The gap closes to a thin sliver`.
NEDEN    10 s yolu ölçülmedi (P14); Veo 8 s verirse bu olaylar kesilir.
ARIZA    H10 notu; FLOW_GERCEKLERI §9
ÖNERİ    Kilit olayı 7. saniyeye çek, son vuruş sabit tutuş olsun.

### B14 · KÜÇÜK · C04 "layout" kelimesi ekrana arayüz çağırıyor
KANIT    `the screen layout unchanged`, `the bezel, the screen layout and the blurred cockpit behind stay as they are`, `a simple live telescope image`.
NEDEN    "layout" ve "live telescope" kelimeleri HUD çerçevesi, artı işareti ya da yazı çağırır. Okunacak ekran yazısız tasarlanmış, kelimeler bunu bozuyor.
ARIZA    T06
ÖNERİ    `the screen layout unchanged` yerine `the picture on the glass fills it edge to edge`. `live telescope image` yerine `plain full-frame picture of the Sun`.

### B15 · KÜÇÜK · Görünmeyen kimlik parçaları kadrajda isteniyor
KANIT    C09 Görsel (arkadan): `a single circular blue-and-gold mission badge on his left chest with an abstract crescent`. C14 Görsel (silüet): `rigid ivory chest armor, graphite shoulder panels and joint seals, white gloves, black boots and a compact ivory life-support pack` ve arkadan paneli referans.
NEDEN    G02 başlığı "kadrajda olmayan kısım atılır" diyor ama uygulanmamış. Arkadan çekimde rozet modeli gövdeyi döndürmeye iter. Silüet figüre ayrıntı yüklemek figürü büyütür ve ölçeği bozar.
ARIZA    T05 · T08 (ölçek)
ÖNERİ    C09'dan rozet cümlesini çıkar. C14'te `a tiny helmeted figure in an ivory pressure suit, seen from behind` yaz ve arkadan panel referansını kaldır.

KORU: C07'de temasın bilerek C08'e bırakılması (`temas olmadan biter`). C10'un insansız ve kişiye gönderme içermemesi. C04'ün yalnız resim taşıyan ekranı ve kurguda yerleştirme yedeği. C21'de `The aperture diameter is visibly larger than Earth` ölçek çıpası.

KAPSAM DIŞI: C18 ile C01 neredeyse aynı çekim (H01 tekrar riski). C22'de Dünya'nın yokluğu yalnız sesle okunuyor.

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 9 · KÜÇÜK 6
KARAR    TUR KAPANABİLİR
GİDİ     uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md · FLOW_GERCEKLERI.md · SMOKE_TEST.md (P14, P16, P17 satırları ve Sonuçlar) · yatay_4_dk_filmler/THE_PLANET_THIEF/FILM.md (tam) · PROMPTLAR/G01.md · G02.md · G03.md (tam) · ODA/DURUM.md · ODA/SAHIP_PLANI.md (yalnız C06-C08 satırları, grep ile)
YAPILMADI  P14 (10 s), P16 (vuruş biçimi) ve P17 (panel seçimi) için sonuç yok. ref/ ve kare/ dosyaları henüz yok, görsel kontrol yapılamadı. Flow Görsel modunda en çok kaç görsel eklenebildiği ölçülmedi; çekimlerin çoğu 3 görsel yüklüyor. PROMPT_HATA_ATLASI.md, GOSTERIM_COZUMLERI.md ve SAHNELEME.md okunmadı.
```
