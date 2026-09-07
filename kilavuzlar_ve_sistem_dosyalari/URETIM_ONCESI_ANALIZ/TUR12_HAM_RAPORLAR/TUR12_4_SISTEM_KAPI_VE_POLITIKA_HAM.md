# TUR 12 · RAPOR 4 — MAKİNE OKUNUR ŞEMA, SAYISAL KAPI, YAŞAM DÖNGÜSÜ VE POLİTİKA (ham metin)

> Girdi promptu: `../15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` PROMPT 4
> Koşu tarihi: 06.09.2026 · Sahibin yapıştırdığı metin, DEĞİŞTİRİLMEDEN.
> Süzme: `../04_ARASTIRMA_BULGULARI.md` §TUR 12

---

Yapay Zekâ Destekli Görüntüden Videoya Üretim Hatlarında Makine Okunur Referans Paketi ve Varlık Yaşam Döngüsü Yönetimi

Yapay zekâ tabanlı görüntüden videoya üretim hatları, geleneksel CGI ve VFX süreçlerinden farklı olarak deterministik olmayan, olasılıksal bir doğaya sahiptir. Özellikle uzay temalı, basınç giysili ve kasklı karakterlerin yer aldığı, kamera açılarının ağırlıklı olarak sabit tutulduğu ve 8-10 saniyelik kliplerin ardışık olarak üretildiği dizilerde, görsel devamlılığın sağlanması en kritik mühendislik problemidir. İnsan gözü, art arda gelen iki klipte kask vizörünün yansıma açısındaki milimetrik bir değişimi ya da göğüs panelindeki yapısal bir kaymayı anında bir hata olarak algılar. Bu bağlamda, üretim hattında kullanılan "referans paketleri"nin, sanat yönetmenleri tarafından okunan statik birer PDF veya mood board olmaktan çıkarılarak; alanları makineler tarafından denetlenebilen, eşikleri sayısal temellere oturtulmuş, ömrü ve mülkiyeti kriptografik olarak tanımlanmış, tam otomatik çalıştırılabilir bir üretim aletine dönüştürülmesi zorunludur.

## Birinci Bölüm: Veri Modeli ve Varlık Kütüphanesinin Makine Okunur Künyesi

Modern bir üretim hattında varlık kütüphanesinin makine okunur künyesi, verilerin salt bir metin dizgesi olarak tutulduğu ilkel dosya sistemlerini reddeder. Akademi Yazılım Vakfı (ASWF) tarafından desteklenen OpenAssetIO gibi standartlar, varlıkların statik dosya yolları yerine bağlama duyarlı varlık referansları (Entity Reference) ile çağrılmasını şart koşar.

Varlık adlandırma şemaları, sistemin hiyerarşik yapısını yansıtmalı ve benzersizlik kuralına katı bir şekilde uymalıdır. Geleneksel dosya yolları yerine URN yapısına benzeyen, çözümlenebilir dizgiler kullanılır:

- asset://nebula_proj/char/eva_commander/v012 (sürüm kilitli ana karakter kimliği)
- asset://nebula_proj/prop/oxygen_tank/status/depleted (kanonik durum bildiren alt nesne)
- asset://nebula_proj/env/airlock_door/cam/static_front (kamera açısı içeren ortam kimliği)

Varlık sınıfı ve kanonik görünüş/durum adlarının serbest metin olarak tutulması, makine doğrulaması sırasında veri kirliliği ve otomasyon çöküşü yaratır. ISO 25964-1 standardı, yapılandırılmış denetimli sözlüklerin (controlled vocabulary) ve taksonomilerin kullanımını zorunlu kılar. Her durum ISO 25964 hiyerarşisine uygun bir taksonomi ağacından çekilir: SuitState -> Helmet -> VisorDown. Bu sayede makine, "vizör aşağıda" ile "kask kapalı" ibarelerinin eşanlamlı mı yoksa alt-üst kavram mı olduğunu deterministik olarak bilir.

Sahne listesinin çağırdığı bir kodun gerçekten var olduğu, OpenAssetIO gibi bir sistemin çözümleyici API'sine gönderilen bir sorgu ile doğrulanır. Kullanılmayan bir kayıt, sistemin yönlendirilmiş asiklik grafiğinde (DAG) hiçbir sahne düğümü tarafından referans edilmediğinde otomatik olarak "yetim" (orphan) işaretlenir (tahmin). Eksik bir üretim varlığı, takip sisteminde kırmızı bayraklı bir "pipeline debt" bloğu olarak görünür ve bu varlık düğümü çözülmeden bağımlı hiçbir sahnenin üretim kuyruğu tetiklenmez (kanıtsız öneri).

Paketin fiziksel gövdesi; C2PA meta verilerini barındıran kilitli görseller ve bu görselleri yöneten tek bir ana JSON veya YAML dosyasından oluşur. Görseller, isimlerine göre değil, metin dosyasında tutulan SHA-256 kriptografik özetleri ile metne bağlanır. Her üretim öncesi betiği, diskteki görselin o anki hash'ini hesaplar ve JSON içindeki hash ile karşılaştırır. Bağ koparsa, görsel tahrif edilmiş sayılır; süreç anında durdurulur. Aynı varlık birden çok yapımda yeniden kullanıldığında proje üstü global bir kütüphanede urn:global:char:eva_suit:v2 şeklinde sürümlenir; alt projeler yalnız okuma erişimiyle bağlanır (kanıtsız öneri).

### Varlık Kütüphanesi Alan Tablosu

| Alan Adı | Veri Tipi | Zorunluluk | Geçerlilik Kuralı | İhlal Seviyesi | Örnek Değer |
|---|---|---|---|---|---|
| asset_urn | String | Evet | Regex tam eşleşmesi (ASWF OpenAssetIO, 2024) | Kritik (Durdurma) | asset://spc/char/commander/v012 |
| class_type | Enum | Evet | Geçerli ISO 25964-1 taksonomi düğümü (2011/2013) | Kritik (Durdurma) | character.suit.eva |
| canonical_state | Enum | Evet | class_type'ın hiyerarşik alt kümesi (ISO 25964-1) | Yüksek | helmet.visor_down |
| image_hash | String | Evet | SHA-256, 64 karakter (Tahmin) | Kritik (Durdurma) | e3b0c44298fc1c149afb... |
| c2pa_manifest | Boolean | Evet | Geçerli JUMBF C2PA v2.x konteyneri (C2PA Spec v2.4, 2024) | Yüksek (Karantina) | true |
| dependencies | Array | Hayır | Her URN sistemde Resolved dönmeli (OpenAssetIO API, 2024) | Kritik (Durdurma) | ["asset://spc/prop/oxy/v01"] |
| yolo_item_count | Integer | Evet | Değer ≥0, kural tabanlı algılama adedi (Ultralytics YOLO, 2024) | Orta | 1 |

### Örnek Kayıt Şeması (JSON Payload)

    {
      "asset_urn": "asset://project_nebula/character/engineer_suit/v005",
      "metadata": {
        "class_type": "character.suit.eva",
        "canonical_state": "helmet.visor_down",
        "creator_provenance": {
          "AISystemUsed": "Midjourney v6.1",
          "AIPromptWriterName": "AI-TD-01"
        }
      },
      "physical_payload": {
        "file_path": "s3://assets/nebula/engineer_v005.png",
        "image_hash": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
        "has_c2pa_manifest": true
      },
      "validation_thresholds": {
        "lightglue_match_minimum": 0.85,
        "sam2_silhouette_iou": 0.92,
        "yolo_text_count": 0
      },
      "dependencies": ["asset://project_nebula/prop/oxygen_tank/v002"]
    }

## İkinci Bölüm: Kabul Kapısı ve Sayısal Ölçütler

Hedefin algılanması, tanınması ve kimliklendirilmesi askeri ve optik mühendislikte Johnson Kriterleri ile yönetilir. Orijinal olarak termal kameralar için 1958'de John Johnson tarafından geliştirilen bu standart, modern dijital sensörler için piksel değerlerine uyarlanmıştır. Bir detayın insan gözünce tam olarak tanımlanabilmesi (Identification seviyesi) için hedefin kritik boyutu boyunca en az 12 ila 14 piksel (6.4 çizgi çifti) çözünürlüğe ihtiyaç vardır. Eğer kask üzerindeki spesifik rütbe şeritleri veya göğüs panelindeki butonlar 14 pikselin altına düşerse, makine okumasında ve insan algısında yapısal devamlılık kanıtlanamaz.

Karakterin kask vizörü açık olduğunda ve yüz hatları göründüğünde, 2019'da Jiankang Deng ve ekibi tarafından literatüre kazandırılan ArcFace mimarisi kullanılır. ArcFace embeddings arasındaki kosinüs benzerliği eşiği, aynı kişiyi doğrularken 0.65'in üzerinde tutulur.

Yüz metrikleri tamamen çöktüğünde vekil (proxy) ölçümler devreye girmelidir:

- Giysi Geometrisi, Ekipman ve Rol Şeridi: LightGlue algoritması (Lindenberger ve Sarlin, 2023) görüntü çiftleri arasındaki seyrek yerel özellikleri eşleştirir. Beyaz uzay giysileri pürüzsüz olsa da eklem yerleri, oksijen tüpü bağlantıları ve göğüs paneli kıvrımları ideal anahtar noktalar oluşturur. Eşik: LightGlue eşleşme skoru %85 üzeri.
- Sırt Silueti ve Gövde Oranı: SAM 2 maskeleri IoU ile üst üste bindirilir; %88 üzerindeki örtüşme kütle deformasyonu olmadığını ispatlar.
- Algısal ve Yapısal Benzerlik: LPIPS (VGG/AlexNet ara katman aktivasyonları) ile ölçülür; değişim istenmeyen bölgelerde LPIPS mesafesi 0.15'in altında olmalıdır. Renk farkları CIEDE2000 ile hesaplanır; ΔE<2.5 eşiği gerçek renk bozulması olmadığını doğrular.

Sayfalarda "sıfır yazı bulunduğu" ve sayılabilir öğelerin tam sayısı, Ultralytics YOLO mimarisi ile tespit edilir. Güven eşiği 0.75 üzerine sabitlenerek görüntü taranır; class: text sayımı tam olarak 0 olmalıdır.

Tek kişilik bir hatta ücretsiz ve yerel bir doğrulama zinciri şu şekilde kurulur: FFmpeg ile üretilen videodan saniyede 1 kare çıkarılır. Python betiği üzerinden OpenCV ile görüntüler belleğe alınır. Yerel Hugging Face kütüphaneleri kullanılarak ArcFace, LightGlue ve SAM 2 sırayla koşturulur. Metriklerin koşulamadığı durumlarda, cevabı tek kelimeyle sayılabilen insan sınavları yazılır: "Kask güzel mi?" gibi öznel değil, "Kask vizörünün rengi nedir? (Mavi/Altın/Siyah)" veya "Göğüs panelinde kaç buton var?" şeklinde kapalı uçlu sorular.

### Kabul Kapısı Tablosu

| Ölçüt | Neyi Kanıtlar | Araç ve Komut | Eşik | Tolerans | Yanlış Kabul Riski | Ret Sonucu |
|---|---|---|---|---|---|---|
| Yüz Gömme Uzaklığı | Vizör açıkken aynı kişi | ArcFace: cosine_sim(f1,f2) (Deng vd., 2019) | >0.65 | ±0.05 | Aşırı poz sapmalarında farklı kişiyi kabul | Klip çöpe atılır |
| Kenar ve Oran (DRI) | Detayın tanınabilirliği | OpenCV: cv2.boundingRect() (Johnson, 1958) | ≥14 piksel | Yok | Modelin donanımı küçük çizmesi | Detay algılanamaz, onaylanmaz |
| Giysi Geometrisi | Vizör kapalıyken aynı giysi | LightGlue: match_pair() (2023) | >%85 nokta | ±%5 | Beyaz zemin parlamasında nokta erimesi | Giysi/panel değişti uyarısı |
| Algısal Benzerlik | Arka plan/doku tutarlılığı | LPIPS: lpips.LPIPS(net='vgg') (Zhang vd., 2018) | <0.15 | ±0.02 | Tarz kayması geometrik kayma olmadan kabul edilebilir | Karakter bağlamdan koptu |
| Siluet Maskesi Örtüşmesi | Kütle deformasyonu yok | SAM 2: calculate_iou() (Meta AI, 2024) | >0.88 IoU | ±0.03 | Ani hamlede maske kayması | Uzuv eksikliği/erime |
| Sıfır Yazı | Halüsinasyon yazı yok | YOLOv10: yolo predict conf=0.75 (2024) | =0 | SIFIR | Düşük güvenli yazıyı çizik sanma | Katı iptal |

## Üçüncü Bölüm: Yaşam Döngüsü ve Geçersizlik Mekanizmaları

Profesyonel bir hat yapısında görsel çapa üretimi, tüm üretim sırasının mutlak sıfırıncı noktasıdır. Çapa üretimi bitmeden, onaylanmadan ve kilitlenmeden asıl üretime geçilmesi, yapay zekânın halüsinasyon sarmalına girmesine neden olur. Onaysız varlıkla üretime başlanmaması kuralı doğrudan CI/CD mekanizmalarına yazılır. Makine bunu bloke ederken, insan tarafında Baş Yapımcı veya Teknik Yönetmen C2PA manifestosunu kriptografik olarak imzalayarak onay verir. Onaylı bir varlık sürümlendiğinde v001 etiketi alır, C2PA ile kilitlenir ve değiştirilemez hâle gelir.

Prompt inşasında büyük bir risk mevcuttur: Aynı kimlik metni, onlarca sahnenin promptunda kopyala-yapıştır olarak durduğunda, herhangi bir tasarım revizyonu tüm kopyalara manuel olarak yansıtılamaz. Bir revizyonun bütün kopyalara inmesi, "tek kaynaktan derleme" (single source of truth) yaklaşımıyla garanti edilir. Bu sadece bir seçenek değil, mühendislik zorunluluğudur. Metin dosyalarında kopyayı hiç üretmeyen Jinja2 şablon motoru kullanılır: {{ assets.characters.eva_commander.appearance_prompt }}. Derleme zamanında varlık kütüphanesinden en güncel ve onaylı metin çekilerek sahne promptu oluşturulur.

Referans karesi ile saha belgesi çeliştiğinde, makine tabanlı bir hiyerarşide referans paketi daima üstündür (kanıtsız öneri); çünkü referans paketi matematiksel eşiklerden geçmiş, denetlenebilir son veridir. Saha belgesi ise bir niyet beyanıdır.

Bir referans çapası, üretim esnasında kendi çıktısı üzerinden beslenirse "nesil kaybı" veya "gizli uzay kayması" yaşar. Uygulamalı tahminlere göre en fazla 3 üretim döngüsünden sonra tamamen bozulur ve aslından kopar (tahmin). Bu yüzden üretilen kareler asla yeni bir çapa olarak sisteme geri verilmez; her ardışık klip doğrudan v001 onaylı orijinal çapaya referans vermek zorundadır.

Onaylı referans karesi, kör koşan modele girdi olarak verilir. Ancak devamlılık değerlendirmesi aşamasında da referans kullanılmalıdır — üretim bittikten sonra, doğrulama aşamasında, üretilen klip ile orijinal referansın LPIPS ve LightGlue skorları karşılaştırılırken açılır. Pratik bir hatta, eşiklerden geçen doğru bir referans sayfası ortalama 15-20 iterasyon ile yaklaşık 45 dakikada ortaya çıkar (tahmin). Bu maliyetli süreç, referans paketi 4-5 farklı sahnede ve en az 2 farklı varlıkta hatasız kullanıldıktan sonra kendini amorti eder (kanıtsız öneri).

### Yaşam Döngüsü Tablosu

| Durum | Giriş Koşulu | Çıkış Koşulu | Onaylayan | Bloke Olan Sahneler |
|---|---|---|---|---|
| Draft | Varlık UUID atanması ve prompt inşası | Sayısal eşiklerin %80'ini geçmek | Otomatik CI/CD betiği (tahmin) | Varlığı çağıran tüm sahneler derleme öncesi bloke |
| Review | Test betiklerinden geçiş | C2PA hash imzası ve kriptografik kilit | Teknik Yönetmen (C2PA Spec v2, 2024) | Render bloke |
| Approved | İnsan imzası + C2PA doğrulaması | Geçersiz kılan olay | Üretim Hattı API (OpenAssetIO, 2024) | Yok |
| Deprecated | Aynı URN için yeni Approved sürüm | Soğuk arşive taşınma | Sistem (otomatik) (tahmin) | Eski sürümü statik çağıran sahneler |

### Geçersizlik Tablosu

| Olay | Tespit Yöntemi | Zorunlu Eylem |
|---|---|---|
| Model sürümü değişimi | IPTC AISystemVersionUsed uyuşmazlığı (IPTC, 2025) | Eski çapalar LPIPS/LightGlue testinden tekrar geçirilir |
| Oran veya çözünürlük değişikliği | Piksel matris boyutlarının pre-flight okunması (tahmin) | Johnson DRI eşiği ihlalinde paket reddedilir |
| Bağlantı kopması / C2PA uyuşmazlığı | Manifestonun çözülememesi veya hash farkı (C2PA v2.4) | Karantina, temiz kopya çekilir |
| Sağlayıcı saklama süresinin dolması | Bulut URL'sinin 404/410 dönmesi (tahmin) | Yerel payload devreye girer |
| Tasarım revizyonu | Varlık yönetim sisteminden manuel tetikleme (kanıtsız öneri) | Durum Draft'a çekilir, derlemeler kilitlenir |

## Dördüncü Bölüm: Politika, Yazım Yüzeyi ve Hukuki Kısıtlar

DALL-E 3 System Card, "istemin dönüştürülmesi" (prompt transformation) yöntemiyle kullanıcı metnini güvenlik filtrelerine uygun hâle getirdiğini açıkça belirtir. Bir cümlede üç veya dört kişisel özniteliğin (yaş, ırk, yüz yapısı, spesifik cinsiyet vb.) üstünde detay kullanıldığında, sistemin demografik önyargı veya stereotip filtresine takılma ve red riski belirgin biçimde artar. Sora Sistem Kartı (2024) da benzer şekilde, haksız kullanım ve derin kurgu riskini önlemek için metin ve görselleri C2PA ile işaretler ve şüpheli ünlü yüzlerini engeller. Fotogerçekçi bir yüzün referans olarak doğrudan yüklenmesi, biyometrik eşleme güvenlik önlemleri nedeniyle engellenebilir veya çıktı kasıtlı olarak deforme edilebilir.

Biyometrik yüz verilerinin yapay zekâya referans olarak beslenmesi, Türk Hukuku kapsamında 6698 sayılı KVKK m. 6 (özel nitelikli kişisel veri) bağlamında ihlal riski taşır. Ayrıca bir karakterin yüzünün bilinen birine benzemesi, TMK m. 24-25 bağlamında kişilik haklarının ihlali davalarına neden olur. Bu kısıtlamaları dolanmak yerine mühendislik düzeyinde kökten çözmek gerekir. Kimlik, biyometrik yığın (göz aralığı, çene kemiği) yerine tamamen biyometrik olmayan donanım ayırt edicilerine çevrilir: gövde kütle oranı, sırt siluetindeki spesifik teçhizat geometrisi, kol ve omuzdaki rol şeritlerinin yeri, kask vizörünün oval-köşeli oranı.

Platform beyan kuralları (AB Yapay Zekâ Yasası Art. 50 ve California SB 942) ve şeffaflık yükümlülükleri, AI ile üretilen içeriklerin makine okunabilir şekilde işaretlenmesini zorunlu kılar. IPTC 2025.1 Fotoğraf Meta Veri Standardı, XMP uzantısı içinde AISystemUsed, AISystemVersionUsed ve AIPromptWriterName alanlarını tanımlar. Görünmez damgalar (örn. Google SynthID) piksellerin frekans uzayına işlenirken, C2PA kriptografik imzaları dosya başlıklarında tutulur.

Referans karesini üreten ana istem katı denetim kapılarından geçmeli; ancak bu istemden türetilen "kamera açıları" gibi komutlar biyometrik filtrelerden muaf tutulmalıdır (kanıtsız öneri). Belirsiz sıfatların ölçülü geometriye çevrilmesi zorunludur: "Büyük tank" yerine "omuz genişliğinin %80'i çapında silindir", "modern giysi" yerine "açısal polimer plakalı, eklem yeri gizli dış iskelet". Olumsuz kuyruk ise şablonlarda varsayılan olarak [text, watermark, human_face, soft_fabric] şeklinde kurallaştırılır.

### Yeniden Yazım Tablosu

| Riskli Kalıp | Güvenli Karşılığı | Gerekçe | Kaynak |
|---|---|---|---|
| "[Gerçek Ünlü Adı] tarzı sert bakışlı yüz" | "Köşeli çene hatlı, keskin elmacık kemikli sentetik yüz modeli" | Gerçek kişi kullanımı IP korumasını ve TMK 24'ü tetikler, model reddeder | (DALL-E 3 System Card, 2023); (Topaktaş, 2024) |
| "Asyalı genç güzel kadın astronot" | "Minyon iskelet yapısına sahip, koyu saçlı karakter" | Etnik köken, yaş ve cinsiyetin bir arada kullanımı ret oranını çok artırır | (DALL-E 3 System Card, 2023) |
| "Modern, havalı ve kesintisiz uzay giysisi" | "Açısal beyaz zırh panelleri ve altıgen eklem matrisli giysi" | "Modern" özneldir, her nesilde rastgele yorumlanır; devamlılığı yıkar | (Kanıtsız Öneri) |
| "Savaşan, kanlı silahlı komutan" | "Aktif termal yayıcı taşıyan, zırhında karbon yanıkları olan figür" | Şiddet/NSFW filtreleri katı iptal uygular | (Sora System Card, 2024); (Sozee, 2024) |

### Sayısal Risk Skoru Formülasyonu

Risk_Skoru = (3.0 × Biyometrik Atıf B) + (2.0 × Etnik/Cinsiyet Atıfı E) + (1.5 × Öznel Sıfat S) − (2.0 × Geometrik Metrik G)

- B = Biyometrik veya ünlü kişilere ait isim/özellik sayısı (ceza puanı en yüksek).
- E = Irk, yaş veya cinsiyete atıfta bulunan kelimeler.
- S = Soyut/öznel sıfatlar (büyük, güzel, karanlık).
- G = Ölçülebilir metrik sayısı (cm, yüzde, açı, renk kodu) — skoru düşürür.

Risk_Skoru > 4.0 ise CI/CD promptu reddeder ve manuel onaya gönderir (tahmin).

## Beşinci Bölüm: Otomatik Koşulabilir Denetim Kuralı Listesi

1. C2PA İmza Bütünlüğü Kontrolü — geçerli, kurcalanmamış C2PA (JUMBF/CBOR) sertifikası yoksa reddet. (C2PA Spec v2.4, 2024)
2. IPTC Yasal Meta Veri Denetimi — AIPromptWriterName ve AISystemUsed boşsa durdur. (IPTC 2025.1)
3. Taksonomik Sözlük Eşleşmesi — kanonik durum ISO 25964 ağacındaki anahtarlarla tam eşleşmiyorsa reddet.
4. Varlık Bağımlılık Çözümlemesi — alt varlıklar Resolved dönmüyorsa işi asılı bırak. (OpenAssetIO, 2024)
5. Derleme Zamanı Şablon Hatası — tanımsız değişkende derlemeyi kes. (Jinja2)
6. Fiziksel Dosya Kriptografik Bütünlüğü — SHA-256 farkında hattı bloke et. (Tahmin)
7. Johnson's Criteria Minimum Piksel Algısı — kritik detay bounding box'ı 14 pikselin altındaysa fail. (1958/2015)
8. DINOv2 Anlamsal Sapma Testi — çapa ile üretim arasındaki kosinüs benzerliği 0.80 altındaysa iptal. (Oquab vd., 2023)
9. YOLO Text/Halüsinasyon Sayımı — class: text sayımı >0 ise klibi sil. (Ultralytics, 2024)
10. LPIPS Algısal Tolerans Maskesi — maskelenmiş bölgede LPIPS >0.15 ise reddet. (Zhang vd., 2018)
11. ArcFace Benzerlik Çöküşü — "kask_açık" etiketinde kosinüs <0.65 ise reddet. (Deng vd., 2019)
12. LightGlue Yapısal Ekipman Eşleşmesi — %85 keypoint eşleşmesi yoksa flicker kabul et. (2023)
13. SAM 2 Siluet Stabilitesi — IoU <0.88 ise gövdeyi deforme say. (2024)
14. Geçerlilik Ömrü (Model Shift) Aşımı — AISystemVersionUsed farklıysa çapayı Deprecated yap. (IPTC, 2025)
15. Etnik/Biyometrik Metin İhlali Sensörü — Risk Skoru >4.0 ise derlemeyi durdur. (DALL-E 3 System Card, 2023)
16. Optik Matris ve Çözünürlük Kaybı Kontrolü — oran/matris 1:1 uyuşmuyorsa kareyi at. (Kanıtsız öneri)
17. CIEDE2000 Renk Uzayı Sapması — maske içi ΔE >2.5 ise renk kayması tespit et. (Mantiuk vd., 2024)

---

## RAPORUN KAYNAK LİSTESİ (sahibin yapıştırdığı hâliyle)

github.com — OpenAssetIO · tac.aswf.io — Academy Software Foundation TAC ·
accessinn.com — Taxonomy, Thesaurus, or Ontology · zenodo.org — ISO 25964-1 ·
spec.c2pa.org — C2PA Specifications / Content Credentials Technical Specification ·
docs.ultralytics.com — solutions.config API Reference / Model Prediction · github.com — YOLOv8 Object Counting ·
farsight-eo.com / en.wikipedia.org — Johnson's criteria · opg.optica.org — Sensor performance conversions ·
thermal-image.com — The Sweet-Spot Sensor · scribd.com / arxiv.org / mdpi.com / researchgate.net / medium.com — ArcFace ·
researchgate.net / emergentmind.com / arxiv.org / github.com — LightGlue · huggingface.co — SAM2 ·
proceedings.mlr.press — On the Effectiveness of Adversarial Training · cvpr.thecvf.com / openaccess.thecvf.com — AEROBLADE ·
cvpr.thecvf.com — Faster Inference of Adversarial Networks · arxiv.org — Evaluating quality metrics through psychophysical lenses ·
achapiro.github.io — ColorVideoVDP · paul-hackenberger.medium.com — Programmatic Prompt Optimization ·
arxiv.org — SkCC: Portable and Secure Skill Compilation · numonic.ai — IPTC 2025.1 & C2PA ·
encypher.com — What Is the C2PA Standard · mlflow.org — Prompt Registry ·
arxiv.org — Evaluating Intellectual Property Guardrails of Generative Image ·
rg-cs.co.uk — ChatGPT Gets Image Upgrade · ceur-ws.org — Designed to exclude? ·
openai.com — Sora System Card · researchgate.net — Deepfakes on Demand ·
ajklaw.com.tr / bilalalyar.av.tr / topaktas.av.tr — Yapay zekâ ve fikri mülkiyet / KVKK ·
fast.io — How to Detect AI-Generated Images Using Metadata · sozee.ai — Content Moderation for AI-Generated Photos ·
vectra.ai — An autonomous AI agent compromised Hugging Face · iptc.org — Video Metadata Hub User Guide ·
openaccess.thecvf.com — A Mixed Diet Makes DINO An Omnivorous Vision Encoder · arxiv.org — DINOv2
