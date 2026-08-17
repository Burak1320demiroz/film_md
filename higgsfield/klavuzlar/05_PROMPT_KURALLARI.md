# ✍️ PROMPT KURALLARI — Higgsfield biçimi ↔ depodaki V2 iskeleti

> **Kaynak:** Kullanıcının hazırladığı araştırma raporu — *"Higgsfield AI
> Ekosisteminde Hatasız Görüntü ve Video Üretimi"* (sohbete yapıştırıldı)
> **Alındığı tarih:** 03.08.2026
> **Doğrulama:** ❌ denenmedi
> **Kapsam:** Higgsfield'in beklediği prompt biçimi ve bunun depodaki V2
> iskeletiyle **nerede uyuştuğu, nerede çeliştiği.**
> **CEVAPLAMADIĞI şeyler:** karakter sınırı (kaç karakterlik prompt kabul
> ediliyor), negatif prompt için ayrı alan var mı, red/moderasyon sözlüğü.

---

## 1. ÜÇ KATMAN AYRIMI — raporun ana tezi

Rapor, her prompt'un **tek bir göreve** odaklanmasını zorunlu tutuyor.
Üç katman, üç ayrı araç, üç ayrı prompt:

| Katman | Neyi kontrol eder | ⛔ Bu katmana YAZILMAZ |
|---|---|---|
| **Görüntü / Anahtar kare** | çerçeveleme, ışık, lens, ortam düzeni, konumlandırma | zamansal eylem, **kamera hareketi**, koreografi |
| **Kimlik** | yüz anatomisi, yaş, kostüm, vücut oranı, mikro-ifade | arka plan, **ışık kaynağı**, kamera açısı |
| **Video / Hareket** | kamera devinimi, koreografi, fiziksel etkileşim, zamanlama | karakterin temel dış görünüşü, sahne statikleri |

**Gerekçe (rapor):** komutlar tek prompt'ta yığıldığında difüzyon modelinin
gizli uzayında parametre çakışması oluyor → görsel kayma, yüz deformasyonu,
arka plan titremesi.

---

## 2. DEPODAKİ İSKELETLE KARŞILAŞTIRMA — ne tutuyor, ne tutmuyor

Depodaki V2 iskeleti (`../../kilavuzlar_ve_sistem_dosyalari/IMAGE_VIDEO_PROMPT_TEMPLATES.md`)
zaten iki katmanlı: `IMAGE PROMPT` + `VIDEO PROMPT`.

```
✅ TUTUYOR — IMAGE PROMPT'ta kamera HAREKETİ yok
   Bizim IMAGE bloğu yalnız "sabit pozisyon, X metre, açı" yazıyor;
   "kamera sağa kayar" gibi zamansal komut hiç geçmiyor.
   → Raporun 1. katman kuralı bizde zaten uygulanıyor.

✅ TUTUYOR — VIDEO PROMPT zaman çizelgesi taşıyor
   0s / 2s / 5s / 10s kırılımı raporun "koreografi katmanı" tarifiyle aynı.

⚠️ KISMEN — kimlik katmanı bizde AYRI DEĞİL
   Bizim SUBJECT bloğu hem kimliği (yüz, yara izi, kıyafet) hem pozu
   taşıyor ve aynı prompt'ta LIGHTING bloğu da var.
   Rapor: "kimlik katmanına ışık yazılmaz."
   → Soul ID kurulursa bu ayrım doğal olarak oluşur (09_KARAKTER_TUTARLILIGI).
     Kurulmazsa mevcut hâli koruruz — tek prompt'ta üretim yapan bir
     modelde kimliği ayırmanın yolu yok.

🚨 ÇELİŞİYOR — UZUNLUK
   Rapor: "uzun, betimleyici, edebi paragraflar yerine KISA, doğrudan,
   sinematik terminolojiye hakim cümleler. Modeller uzun metinlerin
   niyetini yorumlarken halüsinasyona eğilim gösterir."
   Bizim promptlarımız: image 3.4-4.0k karakter, video 2.4-2.8k.
   → Bu UZUN. Ve uzunluğun sebebi Ders 55 (self-contained zorunluluğu).
```

### Uzunluk çelişkisi — çözülmemiş, ama tek istisna var

Rapor kendi içinde bir istisna tanımlıyor: **Seedance 2.0 için yoğun,
yapılandırılmış ve uzun metinler daha iyi sonuç veriyor** — yeter ki
gereksiz betimleme değil, **bloklu ve sıralı** olsun.

```
SEEDANCE 2.0'IN İSTEDİĞİ SIRA (rapor · "six-block prompt anatomy")
  1. referans bildirimleri   ("Görüntü 1: karakter referansı")
  2. sahne ve zamanlama
  3. özne
  4. kamera dili
  5. ışık ve doku
  6. ses niyetleri

BİZİM SIRAMIZ
  SCENE · ENVIRONMENT · SUBJECT · CAMERA · LIGHTING · PHYSICS · NEGATIVE

→ İkisi neredeyse aynı. Bizim iskelet Seedance 2.0'ın istediği biçime
  şaşırtıcı derecede yakın; farkımız referans bildirimi ve ses bloğunun
  olmaması, PHYSICS bloğunun fazladan olması.
```

```
⛔ KARAR: promptları KISALTMA kararı VERİLMEDİ.
   Sebep: uzunluk bizde estetik tercih değil, Ders 55'in zorunlu sonucu
   (Bible'sız üretim = her sahnede yeniden icat edilen kıyafet).
   Kısaltma ancak Soul ID kimliği üstlenirse mümkün olur.
   → Test edilmeden hiçbir prompt kısaltılmaz.
```

---

## 3. MCSLA FORMÜLÜ — rapordaki endüstri standardı

```
M · Model      hangi model
C · Camera     kamera
S · Subject    özne
L · Look       görünüm
A · Action     eylem
```

Bizim iskeletimizde `Model` yok (araç-bağımsız yazıyoruz, bu bilinçli —
`../README.md` kuralı), gerisi karşılığını buluyor: Camera→CAMERA,
Subject→SUBJECT, Look→LIGHTING, Action→VIDEO PROMPT zaman çizelgesi.

---

## 4. ANAHTAR KARE ÖNCELİĞİ — bizim 7-9 dk formatımızın bilimsel gerekçesi

Rapor, video difüzyonunun nedensel zamansal VAE yapısını anlatıyor:

> *İlk kare bağımsız kodlanır; sonraki kareler önceki karelere **nedensel
> bağımlılıkla** gruplar hâlinde kodlanır. Dolayısıyla ilk karedeki en ufak
> kompozisyon hatası, sonraki tüm karelere **katlanarak** yansır.*

```
BU DEPODA NE ANLAMA GELİYOR
  7-9 dk formatı (start/end frame zinciri) zaten bu mantık üzerine kurulu
  ve KILAVUZ_REHBERI §2.4 şunu yazıyordu:
    "75 imajlık zincirde çapa kilitlenmezse 3. fazda yüz kayar ve
     geri dönüşü olmaz."
  → Rapor bunun SEBEBİNİ veriyor. Kural doğruymuş, gerekçesi eksikmiş.

  2-4 dk formatı text-to-video ve her sahne AYRI üretiliyor —
  yani zincir yok, katlanma yok. Bu bir zayıflık değil, KORUMA.
  (Ders 1'in "her sahne ayrı üretilir" kuralı, kesme sorununu çözerken
   farkında olmadan katlanma sorununu da çözmüş.)
```

---

## 5. NEGATİF PROMPT — rapordan alınacak somut ifadeler

Rapor, sentetik yapay zeka estetiğini engellemek için kullanılan negatif
komutları veriyor. Bizim negatif çekirdeğimizde **olmayan** dördü:

```
no beauty grade          ← bizde yok
no skin smoothing        ≈ bizde "no smoothed skin" var
no HDR                   ← bizde yok
no contrast push         ← bizde yok
no saturation boost      ← bizde yok

+ POZİTİF DİREKTİF (rapor):
  "photorealistic, this is a film frame not an advertisement"
```

```
⚠️ EKLEME KARARI VERİLMEDİ. Sebep: negatif çekirdek 28 prompt'a
   kopyalanmış durumda ve şu an 1.145 karakter. Dört ifade daha eklemek
   promptu ~80 karakter uzatır — en uzun prompt zaten eşiğin 269 karakter
   altında.
   → Önce ölç: bu dört ifadenin eksikliği bir QA bulgusuna yol açtı mı?
     Bugüne kadar HAYIR. O hâlde eklenmez (Ders 51-54 dersi: kural
     eklemek kaliteyi artırmadı).
   → Higgsfield'e geçilirse ve mumsu cilt çıkarsa, o zaman eklenir.
```

---

## 6. DEPOYA DOĞRUDAN AKTARILABİLİR TEK CÜMLE

Raporun bu depo için en değerli tek cümlesi, uzunluk veya model seçimi
değil, **kamera dili**:

> *Yalnızca "sinematik" veya "efsanevi" kelimesini kullanmak işe yaramaz;
> fiziksel kamera donanımının hareket terimleri (dolly in, orbit, crane up,
> crash zoom) yapay zekaya yön vermek için en kesin yoldur.*

Bu, `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md`'nin zaten savunduğu şey ve
Ders 33'ün ("cinematic lighting" → mumsu cilt) ikizi. Rapor bunu bağımsız
bir kaynaktan doğruluyor.

```
✅ ÇAPRAZ DOĞRULAMA: "cinematic" kelimesinin zararlı olduğu artık
   iki bağımsız kaynaktan geliyor (bizim Ders 33 + bu rapor).
   Negatif çekirdekteki yasağı koruyoruz.
```
