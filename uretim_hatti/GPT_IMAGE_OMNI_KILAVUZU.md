# 🎞️ GPT IMAGE + GEMINI OMNI KILAVUZU — kareyi GPT Image'da kur, Omni'de hareketlendir

> **Ne için:** başlangıç karesini GPT Image ile, hareketi Gemini Omni 1.1 Flash ile üreten filmin (THE_SKY_CATCH yolu) üretim yöntemi.
> **Kim okur:** goruntu-yonetmeni · teknik-danisman · devamlilik · kurgucu · Fable · sahip (F7-F8).
> **Kaynak:** `ARASTIRMA/ham/26_GPT_IMAGE_OMNI_KILAVUZ_HAM.md` → `ARASTIRMA/11_SUZME_20261016.md`. Yalnız KABUL satırları burada.
> **Ne değildir:** kural kitabı değil. Hat kuralları (AGENTS.md) önce gelir. Hat kuralıyla çatışan dört öneri (K1-K4)
> süzme §D'de sahibin kararını bekliyor; kılavuzdaki şablonlar bugünkü hat kuralına göre yazıldı.
> **Tarih:** 16.10.2026. Araç olguları `FLOW_GERCEKLERI.md` Ek 2'de; burada tekrar edilmez.

---

## 0 · Dört filmden tek sayfa (15.10.2026 QA)

```
Anlaşılmayı belirleyen   diyaloğun filme girmesi. "Kurguda kaydedilecek" denen 3 filmin 3'ünde kayıt yapılmadı;
                         repliği videoya gömen THE_MAYDAY_SEA anlaşıldı.
Dördünde ortak kusur     kimlik/giysi kayması · vakumda klip sesi · vakumda duman/damla — hepsi ÜRETİMDE doğdu.
Ajan sayısı              sonucu belirlemedi (50 çağrı → "Kopuk"; 7 çağrı → anlaşıldı).
Kayıt                    hangi referansın yüklendiği, hangi denemenin seçildiği hiçbir filmde yazılı değil.
```
Bu kılavuzun işi bu dört kusurun doğduğu yere (kare · hareket · seçim · kurgu) yöntem koymak.

---

## 1 · Araç gerçeği — Flow değil, Gemini uygulaması

| Bilinen (RESMİ) | Bilinmeyen — varsayma |
|---|---|
| 10 s video · yerel ses · 5'e kadar görsel · sahne uzatma · videodan videoya düzenleme (plan/bölgeye bağlı) | ayrı başlangıç/bitiş karesi yuvası (Gemini uygulamasında yok; yalnız Flow web'de) |
| Oran yüklenen görseli izler | seed · kare kilidi · fps · çözünürlük · günlük kota |

- Flow'da gördüğün düğmeyi (ilk + son kare, uzatma modeli, seed) Gemini uygulamasında varmış gibi kullanma.
- **Zincir** (AGENTS §0, gerçek ilk + son kare) yalnız Flow web'de kurulur. Gemini uygulamasında aynı iş §8 ile yapılır.
- Filmin hangi araçta üretildiği ilk denemede `NOTLAR.md`'ye yazılır (model adı: "Gemini Omni 1.1 Flash").
- Görsel tarafı (16.10.2026, `ARASTIRMA/15`): ChatGPT'de "ChatGPT Images 2.5"; API'de `gpt-image-2.5-sunburst` (hassas düzenleme) ya da `gpt-image-2.5-flare` (hızlı).
  Boyut, kalite, maske, `input_fidelity`: `FLOW_GERCEKLERI.md` Ek 3.

---

## 2 · Pilot önce — üç çekim, sesiyle

Bütün referans arşivini büyütmeden önce **üç çekimi sesiyle birleştir ve izle**:

1. **Nerede olduğumuzu gösteren geniş plan** (coğrafya + tehlike)
2. **Tek önemli hareket**
3. **Hareketin sonucu ya da insan tepkisi**

Hazırlık: bir karakter referansı, bir ana mekân geniş planı, gereken tek önemli nesne. Üç kareyi GPT Image'da üret, kimlik + el/nesne teması +
başlangıç durumunu kontrol et; Omni'de her kareye ayrı hareket iste; geçici replik + ortam sesiyle yan yana koy, bir kez izle.
Yüz, mekanik tasarım, ses ve model davranışı burada görülür; kalan çekimler çalışan örnekten türer.

- Açılış filmlerinde pilot = C01-C03 (`ILK_30_SANIYE_KILAVUZU` §6 zaten açılışın önce üretilmesini istiyor).
- Sonra 6 çekimlik bölüm: üret → kurgula → izle → üstüne ilerle. 96 klibi üretip ilk kez sonda izleme.
- Hikâyeyi göz kırpmasına, mutlak sessizliğe, görünmez zamanlamaya ya da kare kesinliğinde mekanik rastlantıya bağlama.

**Üç soruluk seçim:** bu planda kim var? Hangi olay ya da bilgi değişiyor? Sonraki planın başıyla uyumlu mu? Üçü açıksa küçük kozmetik kusur yüzünden sahneyi baştan tasarlama.

---

## 3 · Süre — ham 10 s, kullanılabilir aralık

Hat kuralı: her çekim 10 s, çekim sayısı = HEDEF_SURE / 10 (sahip, 08.10.2026). Omni'den 10 s almak 10 s'nin
**kullanılabilir** olduğu anlamına gelmez; baştaki hazırlık ya da sondaki bozulma kesilince süre düşer.

```
Kullanılabilir aralık < 10 s ise (sırayla):
  1  aynı çekimden ikinci deneme (AGENTS §4: ilk tur 2 deneme)
  2  uyumlu devam üretimi (§8 CONT-01) ya da sahne uzatma — dikiş yeniden izlenir
  3  olayın SONUCUNU gösteren ek plan (yeni bilgi taşır)
YOK: bozuk görüntüyü uzatmak · aynı hareketi döngüye almak · yavaşlatmak
```
- Her denemenin giriş/çıkış saniyesi NOTLAR DENEMELER'e yazılır (§14). THE_SKY_CATCH montajı 02:41'de kaldı; hedef 04:00'tı.
- Görüntü değişmiyorsa ya konuşma yeni bilgi verir ya da beklemenin dramatik nedeni vardır.
- Kesin süre için bitiş başlığı son planın içine konur; bindirmeli geçiş toplamı kısaltır (`kurgu.py gecis`).

---

## 4 · Kimlik, durum, referans yükleme

**Sabit kalan / değişebilen**

| Tür | Sabit | Durumla değişebilir |
|---|---|---|
| İnsan | yüz · yaş · ten · beden · takım kesimi · bant/rozet tasarımı | bakış · ifade · poz · önceden tanımlı kask açık/kapalı sürümü |
| Mekân | kapı · pencere · koltuk · panel yerleşimi | aynı mekânın ışık/hasar sürümü |
| Araç | burun · motor · kapı · bağlantı geometrisi | motor açık/kapalı · ayrık/bağlı |
| Nesne | boyut · malzeme · menteşe · tutma noktası | kapalı/açık · katlı/açılmış · boş/dolu |

- **Durum ayrı adlandırılır** ve aynı üretimde zıt iki durum eşit ağırlıkla verilmez (kapalı kapak + açık kapak). Hat adlandırmasında
  durum, özne sayfasının paneli olur (`ref/7.SERVIS_v1.png` → "the closed-hatch panel"); panel kararı süzme §D K1'de, P17 ölçülene kadar.
- **Kimlik cümlesi** `FILM.md` §3 ORTAK GÖRÜNÜM'den birebir kopyalanır; plana yeni sıfat eklenmez. Giysi değişiyorsa yeni durum yazılır,
  eski referans sessizce yenilenmez.
- **Dosya adını yazmak yüklemek değildir.** `Reference <No>` yalnız o üretime gerçekten eklenen görseli işaret eder. Yükleme sırası
  `EKLE` satırıyla aynıdır ve her denemede `NOTLAR.md`'ye yazılır (hangi numaralar eklendi). Raporlardaki "referans kullanılmadı"
  tahmini ancak bu satırla doğrulanır.
- Her sahne grubunun başında referanslar **yeniden eklenir**; uzun sohbet ayrıntıyı korumaz. GPT Image'ın sohbet geçmişi Omni'ye geçmez.
- Çok panelli sayfa **Omni'ye girdi olmaz**; Omni'ye onaylı tek başlangıç karesi gider (§7).

**Rol cümlesi (GPT Image, resmî: "Identify each input by number and purpose"):**
```text
Reference 1 (engineer): take her face, hair and the pearl-white suit with turquoise upper-arm bands from it.
Reference 2 (control room): take the architecture, the round rear doorway and the blue window light from it.
Reference 3 (hatch): take the closed service hatch and its single top hinge from it.
Create one cinematic film frame that combines these roles in a single camera angle.
```

---

## 5 · Mekân ve coğrafya bir kez kurulur

- Önce **boş mekân geniş planı** (kim nerede durur, giriş/çıkış nerede, ana ışık nereden); sahnede önemliyse **ters açı** ve ana nesne detayı.
  Yakın planlar bu coğrafyadan türer; kapı başka duvara taşınmaz.
- **Dev gezegen yerleşimi** tek kez sabitlenir: ufuk eğrisi, geminin göreli boyu, ışık yönü. Gezegenin görünmediği çekim ayrıca yazılır.
  ("Huge planet" demek tek başına aynı coğrafyayı vermez — THE_PLANET_THIEF C24'te kıta döndü.)
- Ters açıda ekranın sağı/solu değişebilir; **ışığın dünyadaki yönü** takip edilir (Dünya soldaysa mavi ışık nedensiz sağa geçmez).
- Ters açı ve yeni açı promptunda yer "sol/sağ" ile değil **sabit mimari çapayla** yazılır: `the airlock door is in the wall behind the main console`.
  Model "left/right"ı kareye göre okur ve odayı aynalayabilir (`ARASTIRMA/15` B2).

---

## 6 · GPT Image karesi ve düzeltme

**Kare, hareketten ÖNCEKİ anın fotoğrafıdır.** "Kapıyı açar, içeri girer, pilota bakar" kare tarifi değildir: kapalı kapak + tutulan kol
başlangıçtır; açılma videonun işidir. Temas noktası ve hareket payı (kolun döneceği yer, yürünecek boşluk, geminin yaklaşacağı aralık)
karede görünür; kadraj dışı el hareket gerektiriyorsa model eli uydurur.

Alanlar (büyük harfli etiket değil, bu sırada düz cümle — §C kadraja basılma):
yer + zaman + ışık durumu → kim görünüyor (kimlik cümlesi birebir) → kadraj ve kamera yönü → **başlangıç durumu** →
ekran konumları, bakış, temas → yalnız önemli nesneler ve şu anki durumları → tek tutarlı ışık yönü → doku.

```text
Reference 1 (engineer): take her face, closed visor and suit from it. Reference 7 (hatch): take the closed service hatch from it.
A horizontal cinematic medium shot at eye level beside the exterior service hatch, lit by cool blue planet light from frame left
with a restrained amber work light. The adult engineer is already braced beside the hatch, both boots locked to the platform,
her right glove already gripping the hatch handle. The hatch is fully closed and its single top hinge is clearly visible.
Natural skin and materials, fine 35 mm film grain, readable shadows.
```
- Ağır karanlıkta yüz/nesne okunmuyorsa videoya geçmeden düzelt. Sis ve yoğun grain yerine malzeme, silüet, seçilebilir gölge.
- **Saf siyah alan bırakma:** giysi ve kaskta kenar ışığı, Dünya yansıması ya da panel ışığı olsun. Google: "A sharp, clear, and well-composed photograph yields a more coherent and higher-quality video."
- **Eller ya tam görünür ya kadraj dışı;** yarım görünen el videoda en çok bozulan yerdir. Uzuv kadraj kenarında kesiliyorsa eklemden temiz kes ya da tam beden çek.
- **Hareketsiz kalacak kablo, hortum, emniyet bağı** karede ve promptta sabit tarif edilir (`the cable lies still along the floor`); yoksa model onu canlandırır (MAYDAY C11, SKY C09).
  ⚠️ Düzeltme 16.10: iki film örneği bu satırı desteklemiyor. MAYDAY hat C12'de istenen şey sıvı şeritti, kablo değil; SKY plan C10'da bağ gevşek istenmiş, sert tel gibi çıkmıştı. Satır dış kaynağa dayanır (ham 26/32) — ARASTIRMA/16 §E.
- Kamera hareketi istenen çekimde ön planda bir katman (tutamak, cam çerçevesi) paralaks verir; düz fonda kamera hareketi dokuyu esnetir.
- GPT Image'ın aşırı keskin/plastik görünümüne karşı: `35 mm film still, natural depth of field`, malzeme adı (`matte white fabric`, `brushed metal`); "8K, hyperdetailed" yazılmaz; ışığı sahnenin kendi kaynağı belirler. Etkisi ölçülmedi (UYGULAMA).
- **Karedeki hata video promptuyla telafi edilmez.** Yanlış yüz, fazla el, yanlış menteşe, yanlış durum → kare düzeltilir.

**Düzeltme: tek kusur, korunacaklar sayılır** (resmî: "request one change, and repeat the details to preserve")
```text
Edit the supplied frame. Change only the service hatch: make it fully closed, matching Reference 7.
Keep the engineer's face, body, glove contact, the camera angle, the lighting, the background architecture
and every other object exactly as they are.
```
```text
Edit the supplied film frame using Reference 1. Restore only her original facial identity and hair.
Keep the pose, expression, helmet, suit, lighting, framing and background exactly as they are.
```
```text
Create a new camera angle of the same established scene. Use the supplied master frame for the world layout and light direction
and Reference 1 for identity. New framing: a low three-quarter view from behind her right shoulder.
The hatch is still closed and every prop stays where it is; the doorway stays on the same wall.
```
- Yeni açı küçük düzeltme değildir; perspektif değişir. Yeni kareyi master yerleşimle karşılaştır, yalnız yüze bakma.
- Bir düzeltmede yüz + ışık + takım + mekân birlikte değişirse neyin işe yaradığı ayrılamaz. Yüz doğruysa ona dokunma.
- Tekrarlanan düzenleme korunması istenen ayrıntıyı da değiştirebilir: her sonuçta kimlik ve geometriyi yeniden kontrol et.
- **Düzeltme sınırı:** aynı yapısal hata iki kontrollü düzeltmede kalırsa çekim yeniden tasarlanır (hareketi böl · başka açı · sonucu kesmeyle göster). AGENTS §4 ile aynı.

---

## 7 · Omni'de kareden videoya

1. Onaylı başlangıç karesini aç; doğru dosya ve sürüm mü (`kare/Cxx.png`).
2. Oranı pikselden kontrol et (§13): Omni oranı karenin oranından alır.
3. Video oluşturmada **o tek kareyi** yükle. Panel sayfasını onun yerine koyma.
4. Ek görsel gerekiyorsa yalnız rolüyle (aşağıda); önce tek kareyle dene.
5. Hareket promptunu ekle; karede görüneni roman gibi yeniden anlatma.
6. Çıktıyı **indir**, normal hızda baştan sona izle; yüz, temas, nesne durumu, hareketin sonucu. Giriş/çıkış saniyesini yaz (§14).

Video promptu: **tek ana hareket · kamera davranışı · bitiş durumu.** Kamera ve özne hareketi ayrı cümle.

> **Google resmî (Vertex, `ARASTIRMA/15` V40):** görselden videoda karakteri, arka planı, ışığı **yeniden tarif etme** ("Redundant prompts confuse the model");
> karaktere "the subject / the woman / she" de; kamera hareketi, özne hareketi, çevre değişimi yaz. Hattın "ORTAK GÖRÜNÜM cümlesi her promptta birebir"
> kuralı (AGENTS §2) bununla çatışıyor → **sahip kararı K9** (`ARASTIRMA/15` §D). Karar gelene kadar hat kuralı yürürlükte.
```text
The camera stays locked. Her glove already holds the handle; she swings the existing hatch open on its single visible hinge
and holds it fully open. Her boots stay braced and her body stays in place. Her face, closed visor, gloves and the surrounding
hull keep their shape throughout.
```
Hat biçimi (sahip, 10.10.2026): bu hareket `0-3 s · 3-7 s · 7-10 s` vuruş planıyla yazılır (goruntu-yonetmeni). Vuruşlar tek hareketin evreleridir.

| İstek | Kamera | Kullanım |
|---|---|---|
| Locked camera | konum ve yön sabit | mekanik temas, önemli nesne detayı |
| Slow push-in | yavaşça yaklaşır | karar ya da tehdit; özne az hareket eder |
| Pan | yerinde döner | aynı geniş mekânda başka şeyi göstermek |
| Tracking | özneyle yer değiştirir | kısa kontrollü hareket, araç yaklaşması |
| Pull-back | uzaklaşır | ölçek, coğrafya, sonucun açılması |

- Bir planda yörünge + hızlı zoom + pan + koşu istenmez. "35 mm film look" ile "35 mm lens" aynı şey değildir; bir planda üç lens yok.
- **Ek referans gerekiyorsa** (rol yazılı, yeni kişi doğmaz):
```text
Image 1 is the primary composition for this shot; the scene, framing and starting state come from it.
Image 2 is an identity reference for the same engineer's face and suit.
One continuous shot.
```
- Omni düzenleme özelliği hesapta varsa iyi bir videonun **tek** kusuru düzeltilebilir; sonra yüz, süre ve ses yeniden kontrol edilir.

---

## 8 · Devamlılık — Gemini uygulamasında zincir yerine

**A · Aynı hareketi sürdürmek:** onaylı videonun **son temiz** karesini çıkar (`kareler.py cikar`); son kare bulanıksa daha erkenini seç.
O kare sonraki üretimin kompozisyon girdisi olur; gerçekleşmiş durum açıkça yazılır.
```text
Continue the same scene from the supplied clean frame. The camera position, her identity and the light direction stay the same.
The hatch is already fully open. She reaches inside and closes her glove around the folded pull lever, then holds it.
The open hatch stays open and the hull stays unchanged.
```
**B · Yeni açıya kesmek:** bozuk son kareyi tek kaynak yapma; ana karakter + mekân referanslarına dön, önceki olayın sonucunu yeni kareye işle.
```text
Reference 1 (engineer) and Reference 2 (station). The next moment of the established scene: the hatch is already open
and the engineer is already crouched beside it. A wide view from the station's far side, the planet below, light from frame left.
The identities, the set layout, the lighting and the open hatch stay exactly as established.
```
**C · Başlangıç + bitiş karesi:** yalnız arayüz iki ayrı zaman rolünü açıkça sunuyorsa (Flow web) — o zaman AGENTS §0 zinciri geçerli.

| Durum | Yol |
|---|---|
| tek görsel girdisi | kare temel; hareket + istenen sonuç tarif edilir |
| iki görsel var, zaman rolü yok | ilk/son kare gibi sunma; ana kompozisyon + tasarım referansı rolü |
| başlangıç/bitiş gerçekten var (Flow web) | zincir; ortası ve son durum yine izlenir |
| uzatma var | uzat; yüz, yön ve ses devamlılığı yeniden izlenir |

Her yeni klibi bir öncekinin giderek bozulan karesinden üretmek kaliteyi sürükler; açı değişiminde ya da kimlik kaymasında temiz kaynağa dön.
Sıçramasız tek çekim zorunlu değilse anlamlı bir kesme daha verimlidir.

---

## 9 · Eksen, bakış, tepki planı

- Önce geniş planda iki kişinin (ya da iki aracın) yeri kurulur; çekimler arasında **dünya yerleşimi** korunur, "ekran solu" ezberlenmez.
  Eksen aşılacaksa yeni coğrafya görünür biçimde kurulur. (THE_SKY_CATCH C05→C06, C11→C12: araçlar yer değiştirdi. QA no. → plan C04→C06, C12→C13 — ARASTIRMA/16 §E.)
- Tepki planı: emir, tehdit ya da büyük açıklamadan sonra dinleyenin karşılığı olayın ağırlığını taşır. Yalnız yeni anlam yaratıyorsa eklenir;
  aynı yüz aynı ifadeyle art arda gelirse süre dolgusudur.
```text
Reference 2 (pilot) and Reference 5 (cockpit). A medium close-up of the pilot, looking toward the engineer just off-camera to the left,
on the established side of the cockpit. He has already heard the news; his expression is clear concern, restrained.
The same face, suit, helmet state and light direction; his hands rest below the frame.
```

---

## 10 · Zor hareket

| Hareket | Kare | Videoda |
|---|---|---|
| Yürüme | zemin düzlemi, iki ayak, temas gölgesi, gidilecek boşluk | sabit ya da basit takip kamerası; birkaç kısa adım |
| Kol/mandal | el kolu zaten tutuyor; tek mekanizma ve yön okunur | bir dönüş, bitişte sabit tutuş |
| Kapı açma | kişi yerinde, el kolda, kapı kapalı, menteşe görünür | yalnız kapının tek menteşeden açılması |
| İçeri geçme | önceki planda kapı açılmış | gerekirse kesme: kişi zaten içeride |
| Kask durumu | açık/kapalı sürüm referansla kurulmuş | durum sabit; çıkarma ayrı test |
| EVA geçişi | kısa mesafe, tek emniyet bağı, hedef platform görünür | tek yavaş yer değiştirme; yakalama ayrı plan |
| Kenetlenme | iki araç tek geniş planda anlaşılmış; bağlantı biçimi sabit | yaklaşma · temas · sonuç ayrı planlar |

- **0 g'de zeminde yürüme yazılmaz:** aracın/platformun göreli hareketi, tutunma noktası, emniyet bağının ucu yazılır (THE_SKY_CATCH C07/C08/C16: 1 g yürüme; QA no. → plan C09/C09/C19).
- Gerçekleşmiş temastan başlamak, aynı klipte yaklaşma-tutma-kilitlenme istemekten kolay kontrol edilir.
- Çekme kolu, motor, emniyet bağı hikâyede önemliyse **referansta baştan bulunur**; kriz anında yeni cihaz doğmaz.
- Yürüyüş kayıyorsa: kamerayı sabitle, mesafeyi kısalt; hâlâ kayıyorsa varışa kes.
- Zor anın kadraj/kesme kataloğu: `GOSTERIM_COZUMLERI.md`.

**Örnek dizi — dört çekimde yanaşma (her plan ayrı bilgi):** C01 coğrafya (gemi solda, istasyon sağda, arada güvenli boşluk, yavaş yaklaşma, temas yok) ·
C02 tek temas (halkalar zaten hizalı, kısa düz ilerleme, düz oturma, sekme yok) · C03 insan sonucu (oturan pilot, tek rahat baş sallama) ·
C04 sonucun kanıtı (bağlı gövdeler, çok yavaş geri çekilme, ölçek açılır). Promptların İngilizcesi ham §15'te.

---

## 11 · Diyalog — film başında seçilir, montajdan önce hazırdır

| Yöntem | Ne zaman | Kontrol |
|---|---|---|
| **Omni içinde konuşma** (model sesi, `FILM.md` §5 Kaynak) | kısa, tek konuşmacılı replik | doğru kişi · doğru kelime · telaffuz · fazla konuşma · ağız (alıcıdan gelen seste kadrajdaki ağız kapalı) |
| **Ayrı kayıt** | uzun filmde aynı ses, telsiz, iç ses, kadraj dışı konuşma | sesin karakter ve mekânla uyumu, kesmede ritim |
| **Karma** | ortam/mekanik sesi klipten, ana diyalog kayıttan | iki ortamın ve müziğin üst üste binmemesi |

- ⭐ **21.10.2026 sahip kararı: diyalog kurguda eklenmez** — yeni filmde yalnız ilk satır (Omni içinde konuşma) kullanılır; ayrı kayıt ve karma eski filmler içindir.
- ⭐ **Kurgu kaydı seçildiyse (eski film) replikler montajdan ÖNCE kaydedilir.** Repliksiz montaj "taslak" sayılmaz, izleyiciye gösterilmez.
  (THE_WRONG_BURN · THE_PLANET_THIEF · THE_SKY_CATCH repliksiz izlendi; üçünde de hikâye çöktü.)
- Metinle ses tarifi kimlik kilidi değildir: Omni aynı sesi her klipte vermeyebilir (P18). İki konuşanın tonu karışırsa
  (THE_MAYDAY_SEA 00:11 ↔ 00:24) birinin satırları kayıtla değiştirilir ya da telsiz filtresiyle ayrıştırılır.
- Ön plan: ~2-2,5 kelime/saniye; 10 s'de ~12 kelime. Kesin giriş/çıkış gerçek kayıtta ayarlanır; milisaniye takvimi senkron garantisi değildir.
- ⭐ **İstenmeyen klip sesi kurguda değiştirilir, görüntü yeniden üretilmez.** Vakumda dış ses (çarpma, rüzgâr, dalga, motor) kliple gelirse
  o parçanın sesi kapatılır, mekân yatağı (`FILM.md` §6) altta sürer. Model sesi replik varsa yalnız replik aralığı klipten alınır
  (`timeline.json` `klip_sesi`). Dört filmin dördünde bu adım atlandı.
- Ses köprüsü: sonraki planın repliği kesmeden az önce başlar ya da önceki ortam yeni görüntünün altında sürer (`GECIS_VE_SES_SUREKLILIGI.md`).
  Müzik konuşmanın üstüne değil, karar ve sonuca yerleşir.

---

## 12 · Sorun hangi aşamada çözülür

| Belirti | Önce bak | İlk düzeltme | AGENTS §3 |
|---|---|---|---|
| Yüz ilk karede farklı | GPT Image karesi + yüklenen kimlik girdisi | kimliği yerel düzenlemeyle geri getir (§6) | kare |
| Yüz hareket içinde değişiyor | hareket ve kamera karmaşıklığı | hareketi sadeleştir · kısa aralık seç · yeni açı | hareket |
| Giysiye bayrak/arma/şerit eklendi | karede mi, videoda mı | karedeyse kareyi düzelt; videoda doğduysa aralık seç | kare / hareket |
| Ayaklar kayıyor · 0 g'de yürüme | zemin, temas, mesafe; uzayda tutunma noktası | kısa adım + sabit kamera ya da tutunarak süzülme; varışa kes | hareket |
| Kapı/kask biçim değiştiriyor | başlangıç geometrisi + çoklu eylem | durumu sabitle, hareketi ayrı plana böl | kare / hareket |
| El fazlalaşıyor, nesne eriyor | temas noktası karede görünüyor mu | önceden tutulmuş pozdan başla, tek çevirme | kare / hareket |
| İki kişi tek yüze benziyor | karışan rol referansları | kimlikleri ayrı kaynakla kur; sade kadraj | kare |
| Işık/gezegen yönü sıçrıyor | mekân master'ı, ekran coğrafyası | yeni kareyi aynı dünya yerleşiminden kur | kare |
| Vakumda duman, damla, alev bulutu | karede mi, promptta "smoke/drip/water" var mı | kareyi kuru/temiz kur; videoda doğduysa aralık seç ya da kes | kare / hareket |
| Sonraki klip eylemi baştan alıyor | başlangıç/bitiş durumu | gerçekleşmiş olayı yeni kareye işle (§8 B) | kare |
| İki ardışık plan birbirini yalanlıyor | seçilen denemeler | doğru denemeyi seç; yoksa sonuç planı (WRONG_BURN C11→C12 — ⚠️ 16.10: orada seçim hatası yoktu, C11 promptu uzaklaşmayı istiyordu — ARASTIRMA/16 §E) | seçim |
| Vakumda dış ses, fazla konuşma, yanlış kelime | klip sesi kurguda kısıldı mı | klip sesini kapat, yatak + kayıt (§11) | kurgu |
| Oran yanlış | karenin piksel ölçüsü | tuvali düzelt, sonra video (§13) | kare |
| Sahne güzel ama anlaşılmıyor | çekimin anlatacağı bilgi | geniş yerleşim, tepki ya da sonuç ekle; promptu süsleme | anlatım |
| Süre eksik | kullanılabilir toplam | §3 sırası; ham süre final süre değildir | seçim |

Öncelik: önce hikâyeyi bozan hata (yanlış kişi, yanlış olay, bozuk temas, yanlış durum), sonra göze batan kusur. Grain farkı ya da
arka plan pürüzü çalışan sahneyi yeniden üretime sokmaz. Her denemede değişen tek şey bir cümleyle yazılır.

---

## 13 · Oran, kaba kurgu, dosya

| Dosya | Gerçek oran | Sonuç |
|---|---|---|
| 1920×1080 | 16:9 | yatay film |
| 1080×1920 | 9:16 | dikey |
| 1536×1024 | **3:2** | 16:9 değil; promptta "horizontal" yazması yetmez |
| 1024×1536 | **2:3** | 9:16 değil |

- **Önce doğrudan 16:9 üret** (16.10.2026, `FLOW_GERCEKLERI` Ek 3): API'de özel boyut, kenarlar 16'nın katı — 1536×864 · 2048×1152 · 2560×1440 · 3840×2160
  (1920×1080 olmaz); ChatGPT'de oran seçici ya da promptta oran, sonra indirilen dosyanın pikseli ölçülür. PNG indir; dış büyütücüyle keskinleştirme yapma.
- Olmazsa kırp; genişletme (outpaint) son çare — uydurulan kenar videoda kayar.
- 1536×1024 → merkezden 1536×864 = 16:9 (üst/alt 80'er px). 1024×1536 → 864×1536 = 9:16 (yanlar 80'er px).
  Yüz ya da el kesiliyorsa tuvali genişlet ya da kadrajı yeniden kur; **esnetme yok**. Omni oranı bu kareden alır.
- Dosyanın gerçek süre/fps/çözünürlüğü (dosyayı değiştirmez; P6 ile aynı):
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,r_frame_rate:format=duration -of json ham/C01_d1.mp4
```
- Önce bütün film basit kesme + geçici sesle (`kurgu.py taslak`): başlangıç, hedef, engel, karar, sonuç anlaşılıyor mu. Renk ve efekt sonra;
  sahne grubunda ortak son görünüm. Diyaloğu telefon hoparlöründe de dinle.
- Film adı ve kapak yazısı kurguda eklenir; kaynak görsele yazı istenmez. Dikey tanıtım için ayrı kadraj (`KAPAK_VE_BASLIK_KILAVUZU`).

---

## 14 · Kayıt — tahmin değil, satır

Hattın klasörleri (`~/film_medya/<FILM>/ref · kare · ham · ses · cikti`) ve `NOTLAR.md` DENEMELER tablosu aynı işi görür; ayrı klasör düzeni açılmaz.
Dört filmde bu tablolar boş kaldı; bu yüzden QA raporlarının "kök neden" cümleleri tahmin olarak kaldı.

| Ham kılavuzun SHOT_LOG alanı | Hattın yeri |
|---|---|
| shot_id · image_version · video_version | DENEMELER: Çekim · Deneme · Prompt sürümü; dosya `kare/Cxx.png` · `ham/Cxx_dN.mp4` |
| actual_model · aspect_ratio | DENEMELER "Flow modu" sütununa "Gemini Omni 1.1 Flash · 16:9" |
| eklenen referanslar | DENEMELER "Sonuç" sütununda `ref 1,7` (§4) |
| raw_seconds · usable_in · usable_out | Sonuç: `✅ kullanılabilir 00.5–08.5` |
| attempt_count · cost_units | her deneme ayrı satır · Kredi sütunu |
| status · note | ✅/❌ + doğduğu yer (`→ kare · hareket · seçim · kurgu · anlatım`) |

Maliyet bütün denemelerden toplanır; seçilen kullanılabilir saniyeye bölünür. Görsel ve video denemeleri ayrı sayılır.
Üretilmemiş görsel ya da video "üretildi" diye yazılmaz; QA'nın tahmini kök nedeni kayıtla doğrulanmadan karar satırına girmez.

---

## 15 · Bitti sayma ölçütü

Seçim ekranında normal hızda izle; hemen ardından **sonraki planla birlikte** izle.
1. **Kimlik ve olay:** doğru kişi, doğru ana hareket ya da bilgi.
2. **Devamlılık:** başlangıç/bitiş, nesne durumu, bakış, ışık sonraki planla uyumlu.
3. **İzlenebilirlik:** konuşma duyuluyor; kullanılan süre olayın ritmine hizmet ediyor.

Üçü sağlanıyorsa seç ve ilerle. Teslimden önce: tek parça izleme (açılış · amaç · değişen plan · final anlaşılır) · gerçek toplam süre hedefle eşleşir ·
kişiler sesle ayırt edilir, kesmede anlamsız müzik/konuşma sıçraması yok · kimlik ve önemli nesne biçimi dikkat dağıtacak kadar değişmez ·
doğru oran ve hedef platformda ön izleme. Sorun çözüldükten sonra aynı bölüm yeni bir neden olmadan baştan açılmaz.

---

## Ek A · Sabit kimlik blokları (sahibin EVA blokları, birebir)

Kilitli blok aynen kopyalanır; değişiklik yeni sürüm adıyla yazılır. Yüz görünür / görünmez iki sürüm ayrı tutulur. İç mekân kıyafeti ayrı blok olur.

**KAYA · face visible**
```text
a man in his late fifties with a lined, weathered face visible through the large clear visor of his round white helmet, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a red band around the top of each sleeve at the shoulder, white gloves with red cuffs, and a boxy white thruster pack with smooth, unmarked faces on his back, set in an open tubular grab frame; a red tether line runs from a clip at the centre of his waist to a steel safety hook
```
**KAYA · face hidden**
```text
a man in his late fifties in a round white helmet with a large clear visor, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a red band around the top of each sleeve at the shoulder, white gloves with red cuffs, and a boxy white thruster pack with smooth, unmarked faces on his back, set in an open tubular grab frame; a red tether line runs from a clip at the centre of his waist to a steel safety hook
```
**IPEK · face visible**
```text
a woman in her late twenties with a smooth, narrow face visible through the large clear visor of her round white helmet, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a blue band around the top of each sleeve at the shoulder, white gloves with blue cuffs, and a slim, flat white life‑support pack on her back; a blue tether line runs from a clip at the centre of her waist to a steel safety hook
```
**IPEK · face hidden**
```text
a woman in her late twenties in a round white helmet with a large clear visor, wearing a plain white outer spacewalk suit with smooth, unmarked chest and sleeves, a blue band around the top of each sleeve at the shoulder, white gloves with blue cuffs, and a slim, flat white life‑support pack on her back; a blue tether line runs from a clip at the centre of her waist to a steel safety hook
```
Başlıklar kod bloğunun dışındadır; prompta yalnız bloktaki cümle yapıştırılır.

---

> **Bu dosya ne zaman değişir:** süzme §D kararları (K1-K8) gelince ilgili bölüm yeni tarihle yazılır; eski hâl süzmede kalır.
> P17 · P18 · P13 sonucu gelince §4 · §11 · §6 güncellenir. Kaynaksız satır girmez.
