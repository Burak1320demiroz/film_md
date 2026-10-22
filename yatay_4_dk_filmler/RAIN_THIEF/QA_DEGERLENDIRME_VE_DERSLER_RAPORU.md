# 📊 RAIN_THIEF — QA Değerlendirme, Kök Neden ve Çıkarılan Dersler Raporu

> **Montaj / Taslak Dosyası:** `raın thıef (1).mp4` (Süre: ~03:40 · 25 Çekim C01–C25 · 24 Kesme)  
> **Tarih:** 22.10.2026 · **Değerlendiren:** Fable (Ana Ajan)  
> **Kaynak:** `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/RAIN_THIEF/HAM_QA_RAPORU_MONTAJ_TASLAK_20261022.md`  
> **İncelenen Mercekler:** Anlatım Testi (1–8 + A1–A4 Bulguları #1–#12), İzleme Formu (A/B0), Süreklilik Raporu (C01–C25 Kesme Listesi + Bulgular #1–#26), Tarama / Görsel Denetim (T1, T3, T6, T12, T13).  
> **Dayanak:** `AGENTS.md` §1b, §3 (Hata Nerede Doğdu) · `uretim_hatti/QA_OKUMA_KILAVUZU.md` · `FILM.md` · `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md`.

---

## 1 · Yönetici Özeti ve Genel Karne

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    RAIN_THIEF (~03:40 MONTAJ TASLAĞI) KARNESİ                    ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ • Hikâye Omurgası & Anlatım : 9.5 / 10 (Sıfır bilgiyle kusursuz anlaşıldı)     ║
║ • Karakter & Duygu (Empati) : 9.2 / 10 (Adalet, fedakârlık ve umut hissi tam)   ║
║ • Model Hareketi & Fizik    : 4.5 / 10 (Yerinde sayma, ağırlıksız tutuş, kayma)  ║
║ • Ses Tasarımı & Miks       : 5.5 / 10 (Müzik kesilmeleri, yersiz patlama)     ║
║ • Görsel Süreklilik & Çapa  : 4.0 / 10 (Tüp tasarımı morfları, çark yönü sıçrama)║
║ • Diyalog & Dudak Senkronu  : 4.0 / 10 (Ağızlar oynamıyor, "note" telaffuz hatası)║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

### 1.1 Başarılar (Neler Tutsun Diye Planlandı ve Tuttu?)
1. **Hikâye ve İstek Dönüşümü Eksiksiz Anlaşıldı:**  
   İzleyici ve model testleri olay örgüsünü tek seferde doğru kavradı: Kett'in pazar yerinde çaldığı hava tüpüyle kaçmak istemesi, pazarda susuzluk çeken yaşlı Tula'nın çiçeğine bir damla vererek empati kurması, kaçış gemisini feda edip kuleye yönelmesi, muhafız Vorr'un takibinden sıyrılıp tüpü sisteme takması ve tüm şehre bedava yağmur yağdırması tam bir netlikle okundu.
2. **Bedel (B5 Omurgası) ve Çatışma Kusursuz Çalıştı:**  
   - 00:45'te geminin gitmesine izin verip *"I'm changing the weather"* demesi,
   - 01:31'de yüksek platformda elindeki bozuk paraya bakarken kaçan gemiyi izlemesi (ilk bedel),
   - 03:05'te muhafızın elinde sarı pelerinini bırakıp vanaya atılması (ikinci bedel) izleyicide güçlü bir takdir uyandırdı.
3. **Duygusal Katarsis (Final Hissi):**  
   Sonunda yağmurun yağması, çiçeğin açması, Tula'nın fincanıyla su toplaması ve halkın sevinci izleyicide sıcak bir tatmin, adalet ve umut duygusu yarattı.

### 1.2 Kritik Kırılmalar (Neler Bozuldu?)
1. **Yerinde Sayma / Yürüme Döngüsü Hatası (T13 / A2 - İzleyiciyi Bıraktıran Anlar):**
   - **00:04–00:09 (C01):** Kett koşma hareketi yaparken arka plan akmıyor; 6 saniye boyunca taş zeminde buz pateni yapar gibi yerinde sayıyor.
   - **01:11–01:20 (C10):** Kett merdiveni tırmanma hareketi yapıyor fakat 9 saniye boyunca hiçbir basamak yukarı çıkmadan aynı yerde sayıyor. Dış izleyici bu anı *"videoyu bırakmak istediğim an"* olarak işaretledi.
2. **Dudak Senkronu ve Replik Hataları (A3):**
   - 00:42, 01:05, 03:24 ve 03:34'te replikler duyulurken konuşan karakterlerin ağızları hiç kıpırdamıyor (kukla etkisi).
   - 03:24'te hem yaşlı uzaylının sorusunu (*"How much?"*) hem Kett'in cevabını (*"For once... nothing."*) aynı ses tonu tek nefeste söylüyor.
   - 03:34'te Kett muhafıza pelerini bırakırken replik *"Keep the coat"* yerine yapay zekâ tarafından açıkça *"Keep the note, you'll need it"* olarak telaffuz edilmiş.
3. **Görsel Tasarım Morfları ve Süreklilik Sıçramaları (S1 / S4 / S5):**
   - **Fırtına Tüpü Şekil Değişimi:** 24 kesmenin 9'unda tüpün tasarımı değişiyor: Düz cam silindir → metal dikmeli fener → yatay 3 halkalı tüp → kafesli tüp → dev cam boru.
   - **01:34 Çift Tüp Glitch'i:** Sağ elindeki tüp bir anda sol ele atlıyor ve sağ elde yoktan ikinci bir metal silindir beliriyor (A1-7).
   - **02:56 vs 03:04 Çark Yönü Sıçraması:** Mavi vana çarkı C19'da yatay bir disk iken, C21'de dev bir gemi dümenine dönüşüyor, C22'de tekrar yatay diske dönüyor.
4. **Ses Miksi ve Müzik Kesintileri (A4 / S7):**
   - 00:48'de ekranda hiçbir hareket yokken aniden patlayan yüksek metalik çarpma/uğultu efekti.
   - 02:21 ve 02:37'de arka plan müziğinin aniden bıçak gibi kesilmesi ve birkaç saniye sonra patlayarak geri gelmesi.

---

## 2 · Hata Nerede Doğdu? (Kök Neden Analizi · AGENTS.md §3)

`AGENTS.md` §3 uyarınca rapordaki bulgular doğduğu kaynaklara göre sınıflandırılmıştır:

```
┌────────────────────────────────────────────────────────────────────────┐
║                  RAIN_THIEF HATA DOĞUŞ YERİ DAĞILIMI                   ║
├────────────────────────────────────────────────────────────────────────┤
║ 1. MODEL HAREKETİ & FİZİK : %35 (Yerinde koşma/tırmanma, ağırlıksızlık)║
║ 2. BAŞLANGIÇ KARESİ       : %30 (Tüp tasarımı, çark yönü, giysi morfu) ║
║ 3. SES MİKSİ & TTS        : %20 (Müzik kesilmeleri, "note" telaffuzu)  ║
║ 4. KURGU & SEÇİM          : %15 (Yerinde sayan kısımların kırpılmaması)║
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Model Hareketi ve Fizikten Doğanlar (Motion & Physics)
- **Treadmill Efekti (00:04 ve 01:11):** Video modelinin (Veo/Flow) "koşma" ve "merdiven tırmanma" istemlerinde kamera takibi ile karakter adım hızını eşleyememesi. Karakter hareket ediyor ancak zemin kaymıyor.
- **Ağırlıksız Havaya Kaldırma (02:57):** İri muhafız küçük uzaylıyı pelerininden kaldırdığında kumaşta hiçbir gerilme, karakterin kollarında hiçbir yerçekimi sarkması oluşmaması (T12).
- **El-Çark Kayması (03:13):** Çark çevrilirken parmakların metal yüzey üzerinde tutunmadan kayması (T13).

### 2.2 Başlangıç Karesinden Doğanlar (Start Frame & Consistency)
- **Fırtına Tüpü Değişimleri:** Farklı çekimler için üretilen başlangıç karelerinde tüpün tek bir referans çapasından (`3.TUP` / `R03`) alınmaması; modelin bazen fener, bazen düz şişe, bazen reaktör çizmesi.
- **Mavi Vana Çarkı (Yatay / Dikey):** C19 başlangıç karesinde çarkın yatay zemin vanası, C21 başlangıç karesinde ise dikey duvar dümeni olarak üretilmesi.
- **Kett'in Pelerin Altı Kıyafeti (01:51 ve 03:12):** Tenteden kayarken ve pelerin çıktıktan sonra tulumunun renginin, askılarının ve ayak parmak sayısının (2 parmaktan 3 parmağa) değişmesi.

### 2.3 Ses Miksi ve TTS Sentezinden Doğanlar (Audio & Voice)
- **"Keep the note" Telaffuz Hatası:** Metin seslendirme motorunun *"Keep the coat"* kelimesini yanlış hecelemesi veya promptta sehven *"note"* yazılması.
- **Müzik Kesilmeleri (02:21 ve 02:37):** Müzik klibinin timeline'a parça parça konması ve geçişlerde cross-fade (çapraz geçiş) kullanılmaması.
- **00:48 Hayalet Darbe Sesi:** Efekt kütüphanesinden yanlışlıkla diyalog arasına düşen izole bir "impact" foley sesi.

### 2.4 Kurgu ve Seçimden Doğanlar (Edit & Selection)
- **Atıl Sürelerin Kesilmemesi:** 00:04'teki 6 saniyelik yerinde koşma ve 01:11'deki 9 saniyelik yerinde tırmanma sahneleri ham klipte mevcutken kurguda doğrudan 10 saniye blok olarak korunmuştur. Çözüm: Kurgu makasıyla (trim) ilk 1-2 saniye alınıp hızla bir sonraki kesmeye geçilmelidir.

---

## 3 · Çıkarılan Somut Üretim Dersleri (Film İçi & Hat İçi)

`AGENTS.md` Madde ④ gereği: **Yeni kural yazılmaz; sisteme yeni genel kılavuz türetilmez.** Ancak bu 4 dakikalık montajdan çıkan ve filmin revizyonunda uygulanacak **6 somut üretim dersi** şunlardır:

### 💡 Ders 1: Video Modellerinde "Yerinde Sayma" (Treadmill) Kurguda Bırakılamaz
- **Vaka:** Karakterin koştuğu veya merdiven tırmandığı sahnelerde arka plan akmıyorsa ve karakter basamak çıkmıyorsa, izleyici 3. saniyeden itibaren yapay zekâ hatasını fark etmekte ve sıkılmaktadır.
- **Pratik Çözüm:** Bu çekimler kurguda asla tam süre tutulmaz. Yerinde sayan hareketin yalnızca ilk 1.5–2 saniyesi (eylemin başladığı an) alınır ve hemen varış planına (üst platforma ayak basma veya kaçış noktası) sert kesmeyle (hard cut) geçilir.

### 💡 Ders 2: Nesne/Prop İçin Değişmez Çapa Tanımı (Design Morphing Tuzağı)
- **Vaka:** Fırtına tüpünün kavanozdan fenere, kafesli tüpten dev silindire morflanması filmin merkezindeki "çalıntı novum" hissini zayıflatmıştır.
- **Pratik Çözüm:** Hikâyenin merkezindeki taşınabilir ana nesne için promptlarda tek ve net bir geometrik tanım kilitlenir: *"A handheld clear cylindrical glass canister containing miniature swirling storm clouds and lightning, sealed with brass end-caps and a single blue rotary valve."* Başlangıç kareleri mutlaka bu görsel referans üzerinden türetilir.

### 💡 Ders 3: Mekanizma ve Çark Yönü Kurguda Sıfırlanamaz (S5 State Reset)
- **Vaka:** Çarkın C19'da yatay, C21'de dikey, C22'de tekrar yatay olması sahne mekaniğinin inandırıcılığını kırmıştır.
- **Pratik Çözüm:** Mekanik etkileşim sahnelerinde (vana, kol, şalter) nesnenin mekândaki ekseni (yatay/dikey) sahneleme odasında sabitlenir; açı değişse bile vananın boruya bağlanış geometrisi korunur.

### 💡 Ders 4: TTS Seslendirmelerinde "Monolog Diyalog" ve Telaffuz Kontrolü
- **Vaka:** Yaşlı uzaylının sorusu ile cevabının tek bir ses tarafından okunması ve *"coat"* yerine *"note"* denmesi final anının duygusal ciddiyetini düşürmüştür.
- **Pratik Çözüm:** İki karakter arasındaki konuşma asla tek bir ses kütüğünde üretilmez. Tula'nın sorusu ayrı ses modeli/aktörüyle, Kett'in cevabı ayrı kanalla kaydedilir. Final repliğindeki *"coat"* kelimesi telaffuz doğrulaması yapılmadan filme konulamaz.

### 💡 Ders 5: Eylem ile Replik Senkronu (Sözü Eyleme Uydurmak)
- **Vaka:** Satıcı *"Pour in"* (dök) dediği halde Kett'in tüpü dökmeyip bütün olarak sokete takması izleyicide çelişki yaratmıştır.
- **Pratik Çözüm:** Ya görüntüdeki eylem repliğe uydurulur (vidayı açıp döker), ya da replik eyleme göre revize edilir: *"Lock it in. Turn the blue wheel."* (Yerine kilitle. Mavi çarkı çevir).

### 💡 Ders 6: Kesintisiz Müzik Kanalı (Cross-Fade Zorunluluğu)
- **Vaka:** Müzik klibinin sahne değişimlerinde (02:21 ve 02:37) pat diye kesilip sonra aniden başlaması kurgu hatası hissi vermektedir.
- **Pratik Çözüm:** Müzik sahne kesmelerine göre parça parça dizilmez; filmin altına tek bir master müzik kanalı olarak serilir. Gerilim düşüşlerinde müzik duracaksa en az 1.5 saniyelik fade-out ile indirilir, aniden bıçak gibi kesilmez.

---

## 4 · Somut Düzeltme ve İyileştirme Reçetesi (Action Plan)

Filmi final kalitesine ulaştırmak için yapılması gereken net adımlar:

### 🛠️ Kurgu Masasında Sıfır Krediyle Düzeltilecekler (Hemen)
1. **00:04–00:09 Koşma Sahnesini Kırp:** Kett'in yerinde saydığı 6 saniye atılsın; sadece koşuya başladığı ilk 2 saniye tutulup doğrudan C02 Vorr kesmesine geçilsin.
2. **01:11–01:20 Merdiven Sahnesini Kırp:** 9 saniyelik yerinde sayma planı 2.5 saniyeye indirilsin; Kett merdivene elini atar atmaz C11 sera geçişine kesilsin.
3. **00:48 Hayalet Patlama Sesini Sil:** Görüntüyle uyuşmayan metalik çarpma efekti ses kanalından temizlensin.
4. **02:21 ve 02:37 Müzik Çukurlarını Onar:** Müzik kanalı kesintisiz tek blok haline getirilsin, sahne aralarında sesin düşmesi gerekiyorsa yumuşak hacim otomasyonu (volume automation) uygulansın.
5. **03:24 Replik Ayrımı:** *"How much?"* sorusu yaşlı Tula için daha çatallı/kısık bir tona ayrılsın; *"For once... nothing"* cevabı Kett'in sesine verilsin.
6. **03:34 Telaffuz Düzeltmesi:** *"note"* sesi temizlenerek *"Keep the coat, you'll need it"* şeklinde doğru telaffuzla değiştirilsin.

### 🎨 Yeniden Üretilmesi Önerilen Çekimler (Minimum Kredi)
1. **C12 (01:34 Çift Tüp Glitch'i):** Kett'in elindeki tüpün aniden sol ele geçip sağ elde ikinci metal borunun belirdiği 2 saniyelik aralık temiz bir başlangıç karesiyle yenilensin.
2. **C15 (02:01 "Free delivery" bağlantısı):** Satıcının kolu çekme eylemi, yukarıdaki tentenin serbest kalıp Kett'in üstüne atlamasını sağlayacak net bir görsel neden-sonuç bağıyla eşlensin.
3. **C21 (02:56 Çark Yönü):** Çarkın dikey dümen değil, C19'daki gibi yatay vana çarkı olarak göründüğü bir başlangıç karesiyle çekim düzeltilsin.

---

## 5 · Kayıt Güncellemesi

Bu değerlendirme sonuçları:
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/RAIN_THIEF/HAM_QA_RAPORU_MONTAJ_TASLAK_20261022.md` dosyasına ham veri olarak,
- `yatay_4_dk_filmler/RAIN_THIEF/QA_DEGERLENDIRME_VE_DERSLER_RAPORU.md` dosyasına analiz ve dersler olarak,
- `yatay_4_dk_filmler/RAIN_THIEF/NOTLAR.md` dosyasına izleme tablosu ve ret nedenleri olarak işlenmiştir.
