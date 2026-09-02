# 🎬 Veo 3.1 Fast Modeli İle Diyalog Üretimi ve Video İş Akışı Optimizasyonu Kılavuzu

> **Yapay Zeka Sinematografisinde Çift Akışlı Difüzyon, Eşzamanlı Ses Sentezi, JSON Promptlama ve Lip-Sync Stratejileri**

---

## 1. 🚀 GİRİŞ: ÇİFT AKIŞLI DİFÜZYON VE EŞZAMANLI SES DÖNEMİ

Google DeepMind imzalı **Veo 3.1** ve **Veo 3.1 Fast** modelleri, yapay zeka film üretiminde varsayılan sessiz video dönemini kapatıp işitsel-görsel (audiovisual) eşzamanlı üretim dönemini başlatmıştır.

* **Çift Akışlı (Dual-Stream) Difüzyon:** Ses ve görüntü verisi aynı gizli uzayda (latent space) işlenir.
* **10ms Senkronizasyon Gecikmesi:** Ses ve görüntü arasında doğal bir nedensellik bağı kurulur.
* **%87 Komut Eşleşmesi (Prompt Adherence):** Metin komutlarına yüksek sadakat sağlanır.
* **Hız & Maliyet Avantajı:** Veo 3.1 Fast, standart modele göre **%30 daha hızlı** çalışır ve API maliyetlerini önemli ölçüde düşürür.

---

## 📊 2. VEO 3.1 MODEL VARYANTLARI TEKNİK VE EKONOMİK KARŞILAŞTIRMASI

> ⛔ **BİLGİ AMAÇLI (21.08.2026):** Bu tablo karar girdisi değildir —
> hat Flow üzerinden üretir, model/fiyat seçimi yapılmaz. Fiyatlar
> yazıldığı günün değeridir, güncelliği doğrulanmadan alıntılanmaz.

| Model Varyantı | Çözünürlük ve Kare Hızı | Süre Seçenekleri | Maliyet (Saniye Başına) | İdeal Kullanım Senaryosu |
| :--- | :--- | :--- | :--- | :--- |
| **Veo 3.1 Standard** | 720p, 1080p, 4K* (24fps) | 4s, 6s, 8s | ~$0.40 | Maksimum sinematik detay gerektiren, bütçe kısıtlaması olmayan prestijli sahneler. |
| **Veo 3.1 Fast** | 720p, 1080p, 4K* (24fps) | 4s, 6s, 8s | **~$0.15 (Sesli) / ~$0.10 (Sessiz)** | Hızlı iterasyon, sosyal medya içerikleri, bütçe dostu profesyonel film üretimi. |
| **Veo 3.1 Lite** | 720p, 1080p (24fps) | 4s, 6s, 8s | Fast modelin %50'sinden az | Geliştiriciler için yüksek hacimli video uygulamaları ve hızlı prototipleme. |

> [!NOTE]
> *4K çözünürlük üretimleri Veo 3.1 Fast modelinde saniye başına sesli üretimde **$0.35**, sessiz üretimde **$0.30** maliyete ulaşabilmektedir.

---

## 🗣️ 3. DİYALOG ÜRETİMİNİN TEMEL DİNAMİKLERİ VE SENTAKS KURALLARI

Veo 3.1 Fast varsayılan olarak sessiz video üretmeye eğilimlidir. Karakterin konuşması için özel sentaks kullanılmalıdır.

### 📜 Tırnak İşareti Sentaksı (The Quotes Syntax Rule)
Difüzyon modelinin cümleyi eylem değil diyalog olarak algılaması için şu formül uygulanmalıdır:

$$\text{[Karakter Tanımı]} + \text{[Fiziksel Eylem/Duygu]} + \text{says:} + \text{["Konuşulacak Tam Metin"]}$$

#### ❌ Yanlış Kullanım:
> *"A woman says hello"* (Model kararsız kalır, sessiz veya anlamsız dudak hareketi üretir).

#### ✅ Doğru Kullanım:
> *"A young detective looks directly at the camera and says in a weary voice, 'Of all the offices in this town, you had to walk into mine.'"*

### 🎭 Ton ve Duygu Optimizasyonu
Zarflar (`in a weary voice`, `angrily`, `softly whispers`, `excitedly`) sesin akustik yankısını, nefes alışverişlerini ve yüz kaslarının mikro-ifadelerini doğrudan yönlendirir.

---

## 🎥 4. DUDAK SENKRONİZASYONUNU (LIP-SYNC) ARTIRAN SİNEMATOGRAFİK PARAMETRELER

| Sinematografik Değişken | Optimizasyon Stratejisi | Kaçınılması Gereken Yaklaşım | Teknik Gerekçe ve Etki |
| :--- | :--- | :--- | :--- |
| **Kamera Açısı ve Kadraj** | **Orta Yakın Çekim (Medium Close-Up)**, Omuz Çekimi, Doğrudan Bakış. | Geniş Çekim (Wide Shot), Tam Profil, Tepe Kamerası (Overhead). | Geniş çekimde ağız piksel ızgarasında küçük kalır. Yakın çekim yüz detaylarını odaklamaya zorlar. |
| **İstenmeyen Metinler (Subtitles)** | Negatif alana veya komut sonuna `no subtitles!` veya `No subtitles` eklemek. | Alt yazıları engellemek için hiçbir önlem almamak. | Model eğitim verisinden ötürü ekrana otomatik altyazı koyabilir; altyazı dudak çizgisini bozar. |
| **Kelime Ekonomisi ve Süre** | Diyalogları **5 saniyenin altında**, kısa ve vurucu tutmak. | 8 saniyelik klibin tamamını dolduran uzun tiratlar yazmak. | 5 saniye üstü diyaloglarda ses kesilebilir veya zamanla çerçeve kayması (frame drift) oluşur. Taşmanın ikinci belirtisi: konuşma doğal olmayan biçimde HIZLANIR. Ön test: repliği sesli okuyup süresini tut.† |
| **Ses Netliği (Audio Isolation)** | Ortam seslerini sınırlamak, komuta `Clean dialogue only` eklemek. | Şiddetli yağmur, müzik ve patlamayı aynı anda talep etmek. | Çok fazla ses katmanı diyaloğu boğar. Temiz diyalog post-prodüksiyonda müzik ekleme esnekliği sağlar. |

---

## 💻 5. YAPIOLANDIRILMIŞ KOMUT MÜHENDİSLİĞİ: JSON TABANLI İŞ AKIŞLARI

> ⛔ **BU ŞABLON BU HATTA KULLANILMAZ (21.08.2026):** Aşağıdaki örnek
> `35mm anamorphic lens` (vakumda YASAK — REHBER §3.1 + SİNEMATOGRAFİK
> §11) ve `Cinematic realism` (D33 "cinematic lighting" riskinin
> akrabası) içerir; 1800 karakter JSON sınırı da hattın düzyazı bandıyla
> (REHBER §7: video 2.000-2.600) çelişir. Hat DÜZYAZI prompt kullanır —
> iskelet: `IMAGE_VIDEO_PROMPT_TEMPLATES.md`. Bölüm, Dzine/Flow-dışı
> platform araştırması olarak arşivdedir.

Veo 3.1 Fast, özellikle **Dzine** veya **Flow** gibi gelişmiş platformlarda JSON formatındaki komutlara dikkat sızıntısını (attention bleed) engelleyerek mükemmel tepki verir.

> [!WARNING]
> **Yazılım Kuralları:** JSON içinde tekrarlanan anahtar (duplicate keys) kullanılmamalıdır. Toplam komut uzunluğu **1800 karakter kuralına (1800-character limit)** uymalıdır.

### 📝 İdeal JSON Komut Şablonu

```json
{
  "shot_composition": "Medium close-up, rule of thirds composition, subject positioned left frame",
  "subject_and_action": "A woman in a matte grey suit with short dark hair, looking at the camera with a focused expression and saying in a clear calm voice: 'The archive is unlocked.'",
  "environment": "Ancient obsidian temple interior, glowing cyan light veins, volumetric mist",
  "camera_movement": "Tracking shot moving backwards smoothly at eye level",
  "style_and_mood": "Cinematic realism, 35mm anamorphic lens, shallow depth of field, cool cyan and warm gold lighting contrast",
  "audio_and_dialogue": "Audio: Clean dialogue only. Ambient: Soft low sub-bass hum in the background"
}
```

---

## 👤 6. GÖRSEL VE KARAKTER TUTARLILIĞI: "INGREDIENTS TO VIDEO" & MASTER SEED

Sahneler arası karakter morflanmasını önlemek için **Master Seed (Ana Tohum)** yöntemi uygulanır:

1. **Referans Portre Yaratımı:** Gemini 2.5 Flash / Dzine ile yüksek kaliteli karakter portresi üretilir (`Main-Character-Shot-1`).
2. **Referans Yükleme:** Veo 3.1 Fast sistemine en fazla **3 adet referans görsel** (Ön görünüm, Kıyafet, Arka Plan) yüklenir.
3. **Metin ile Çapraz Doğrulama (Cross-Validation):** Görsel referans yüklense dahi metin komutuna karakter özellikleri (`woman in matte grey suit`, `dark hair`) tekrar yazılmalıdır.
4. **Prompt İçinde Referans Atfı:** Yüklenen referanslara metinde açıkça atıf yapılır: *"The character from reference_1 walks into the location from reference_2 holding the object from reference_3."*†

---

## 🎞️ 6B. İMAJDAN-VİDEOYA (FIRST FRAME) — I2V KURALLARI †

Hattın akışı imaj-önce-video olduğu hâlde bu mod belgesizdi (27.08.2026'da
eklendi). Onaylı imaj **ilk kare** olur; prompt artık sahneyi değil yalnız
HAREKETİ yönetir.

```
I2V PROMPT KURALLARI
  ⛔ Statik öğeyi YENİDEN TARİF ETME — imaj zaten taşıyor. Yeniden tarif,
     modeli o öğeyi yeniden üretmeye çağırır (kayma riski).
  □ Yalnız şunlar yazılır: hareket · kamera · ışık DEĞİŞİMİ · ses.
  □ Kimlik koruması: prompta `maintain the subject from the first frame`
     satırı eklenir.
  □ İmaj ile prompt ÇELİŞEMEZ (imaj loşsa "bright sunny day" yazılmaz) —
     iç çelişki kareyi birkaç saniyede eritir.
```

Örnek (İngilizce, hat standardı; ses ortama uyarlanır):

> *Maintain the subject from the first frame. Slow push-in. She exhales,
> her eyes shift to the left, one strand of hair falls across her forehead.
> Warm rim light grows stronger. Audio: soft breath, low cabin hum.
> Duration: 6 seconds.*

⚠️ **§6 ile ayrım — iki modun kimlik stratejisi FARKLIDIR:** Ingredients
modunda (çoklu referans) karakter özellikleri metne TEKRAR yazılır (§6.3).
First Frame modunda uzun kimlik tekrarı GEREKMEZ — `maintain...` satırı +
kısa çapa yeter. Karıştırılırsa ya kimlik kayması ya iç çelişki üretilir.

---

## 🔊 7. İŞİTSEL TASARIM & KATMANLANDIRMA STRATEJİLERİ

### 🔗 Nedensel Bağlama (Causal Binding)
Görsel eylem ile ses `as`, `when`, `while` bağlaçlarıyla senkronize edilmelidir:
* *Doğru:* `"As the door creaks open, a gust of wind rushes in"`
* *Doğru:* `"She walks across the obsidian floor, her boots clicking softly with each step"`

### 🎚️ Ses Katmanlandırma (Maksimum 3-4 Katman Limiti)
* **Ön Plan (Foreground):** Karakter diyaloğu (`loud`, `dominating`).
* **Orta Plan (Midground):** Çevresel etki sesleri (`footsteps clicking`).
* **Arka Plan (Background):** Ortam akustiği (`faintly`, `in the distance`, `softly`).

> **Komut Etiketleri:** Metinsel girdileri ayırmak için `Audio:`, `SFX:`, `Ambient:`, `Background music:` etiketleri kullanılmalıdır. Anlık ses olayları için üçüncü biçim satır içi parantezdir: *(a loud thunderclap)* · *(key turning in a lock)*.†

---

## 👥 8. ÇOKLU KARAKTER SAHNELERİ VE "SAHNE AKIŞI" (SCENE FLOW)

İki veya daha fazla karakter aynı anda konuştuğunda dudak senkronizasyon başarısı %40'ın altına düşer.

* **Çözüm 1 (Tekli Çekim / Single Speaker):** Sahneler tek karakterli planlar (shot-by-shot) halinde üretilip kurguda birleştirilmelidir.
* **Çözüm 2 (Sıra Alma / Turn-Taking):** Çoklu sahnede senaryo sırası net bildirilmelidir:
  > *"Woman speaks first, then pauses. Man nods and replies."*

---

## 🔄 9. İLERİ SEVİYE HİBRİT İŞ AKIŞLARI (ELEVENLABS SYNC 3 ENTEGRASYONU)

> ⛔ **KULLANILMIYOR (21.08.2026):** Hat ElevenLabs entegrasyonu
> kullanmıyor — ses üretimi Veo native + miks. Yazım tarafı:
> `SES_VE_DIYALOG_URETIM_KILAVUZU.md`.

İngilizce dışındaki dillerde (Türkçe vb.) veya yüksek kaliteli seslendirmelerde **Hibrit Metot** uygulanır:

```
[1. STEP: Veo 3.1 Fast]  --> Sessiz/Temiz Diyalog Ham Video Üretimi (Clean dialogue, No subtitles)
[2. STEP: ElevenLabs]    --> Türkçe / Hedef Dilde Yüksek Kaliteli TTS veya Voice Clone Ses Kaydı
[3. STEP: Sync 3]        --> Sync 3 Teknolojisi ile 4K Lip-Sync Yeniden Şekillendirme
```

* **Sync 3 Avantajı:** Karakterin orijinal mimiklerini (`emotion preservation`) bozmadan Türkçe sese göre dudakları kare seviyesinde (frame-accurate) yeniden senkronize eder.

---

## 🛠️ 10. POST-PRODÜKSİYON HATA AYIKLAMA (TROUBLESHOOTING)

| Karşılaşılan Sorun | Hatanın Temel Nedeni | Çözüm ve Hata Ayıklama Stratejisi |
| :--- | :--- | :--- |
| **Sessiz Video Çıktısı (No Audio)** | Kalite ayarlarının "Preview" modunda kalması veya ses emrinin metin sonuna gizlenmesi. | Ayarları **"Highest Quality"** moduna alın. Ses komutlarını (`Audio:`, `SFX:`) komutun en başına yazın. |
| **Diyalog ve Dudak Uyuşmazlığı** | Cümlenin 8 saniyeyi aşması veya çoklu karakter olması. | Her sahnede **tek konuşmacı (Single speaker)** kullanın. Diyaloğu **<5 saniye** tutun. |
| **Arka Plan Sesinin Diyaloğu Yutması** | Ses hiyerarşisi belirtilmeden rastgele ses yığılması. | Diyalog için `loud` zarfını kullanın, ortam sesini `faintly` yapın. Katman sayısını 3 ile sınırlayın. |
| **Dudak Senkronu Zayıf (Sentaks)** † | Lead-in fiilden sonra virgül kullanımı. | Virgülü iki noktaya çevirin — `says: "..."` formu çoğu koşuda virgülden güvenilirdir; lead-in fiilin (says/whispers/shouts) varlığını doğrulayın. |
| **Mood Kelimesi Nesne Rengini Değiştiriyor (Concept Bleed)** † | Atmosfer tanımı kimlik cümlesine sızıyor. | Kimlik cümlesi ile stil/atmosfer cümlesini AYIRIN; mood kelimesini kimlik cümlesinden uzak tutun, kimlik tanımını değiştirmeden yeniden sıralayın. |
| **Kamera Yönergesi Yok Sayılıyor** † | Kamera tarifi promptun ortasına gömülü. | Prompta KAMERAYLA başlayın — baştaki "Wide aerial shot", ortadaki süslü tariften güçlüdür. |

### ⏩ Video Extensions & Zaman Damgaları (Timestamp Prompting)
* **Kademeli Uzatma (Video Extension):** 5 saniyelik temel klip üretildikten sonra `Extend` veya *first/last frame* fonksiyonuyla video 60 saniyeye kadar uzatılabilir.
* **Zaman Damgaları (Timestamps):** Diyalog zamanlaması için komut içine `[00:03-00:08]` etiketleri eklenebilir.

---

## ⚖️ 11. AÇIK KAYITLAR (27.08.2026)

```
① UZUNLUK BANDI ÇELİŞKİSİ — KARAR DEĞİŞMEDİ, ÖLÇÜM BEKLİYOR
   İki bağımsız dış kaynak (visual-skills veo referansı: 50-200 kelime ·
   video-prompt derin araştırması: 80-120 kelime) hattın düzyazı bandından
   (REHBER §7) belirgin biçimde KISA bant öneriyor ve "uzun prompt →
   model seçmece yapar (cherry-picks)" diyor. Bant ölçüm yapılmadan
   DEĞİŞTİRİLMEZ; test tarifi: aynı sahne iki bantla üretilir, deneme
   (re-roll) sayısı kıyaslanır.

② JSON KARARI — ARŞİVE EK KAYIT
   §5'teki yasak, şablonun İÇERİĞİ yüzündeydi (yasaklı terimler + karakter
   sınırı). İkinci bağımsız kaynak JSON'u süreklilik / concept-bleed önleme
   için doğruluyor. Format kararı sahip tarafından yeniden
   değerlendirilebilir; o güne dek hat DÜZYAZI kullanır.
```

---

## 📌 SONUÇ

Veo 3.1 Fast; Tırnak İşareti Sentaksı, JSON komut mimarisi, Nedensel Bağlama (Causal Binding) ve ElevenLabs Sync 3 hibrit iş akışları ile birleştirildiğinde yapay zeka sinemacılığında stüdyo kalitesinde diyaloglu sahneler üretmenin en güçlü aracıdır.

---

> **†** işaretli maddeler ve 6B bölümü şu kaynaktan damıtılmıştır:
> **Serge Shima — github.com/smixs/visual-skills** (CC BY 4.0, atıf zorunlu)
> · eklenme: 27.08.2026. Örnekteki ses/lens ayrıntıları hat kurallarına
> uyarlanmıştır (lens sayısı ve ortam-dışı sesler çıkarıldı).
