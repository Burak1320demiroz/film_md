# 🎛️ MODEL KARTLARI

> **Kaynak:** Kullanıcının hazırladığı araştırma raporu — *"Higgsfield AI
> Ekosisteminde Hatasız Görüntü ve Video Üretimi"* (sohbete yapıştırıldı)
> **Alındığı tarih:** 03.08.2026
> **Doğrulama:** ❌ hiçbiri denenmedi — tek kare üretilmedi
> **Kapsam:** Bu dosya **model seçimi** anlatır.
> **CEVAPLAMADIĞI şeyler:** klip süre limiti (saniye), en-boy oranı listesi
> model bazında, kuyruk süresi, red/moderasyon davranışı, plan fiyatı.
> Bunlar hâlâ açık — `../README.md` §AÇIK SORULAR.

---

## 🚨 ÖNCE BU — İKİ KAYNAK ÇELİŞİYOR

Elimizde Higgsfield'in model listesine dair **iki ayrı kaynak** var ve
birbirini tutmuyor:

```
A · TANITIM SAYFASI (higgsfield.ai, 02.08.2026 · ../README.md)
   Seedance 2.0 / Fast / Mini · Kling 3 · Google Omni Flash (Gemini)
   Nano Banana Pro · Seedream 5.0 Lite · GPT Image 2 · Soul 2.0

B · ARAŞTIRMA RAPORU (03.08.2026 · bu dosyanın kaynağı)
   Sora 2 · Google Veo 3.1 · Kling 3.0 · Seedance 2.0 · Wan 2.6
   Hailuo/Minimax · Popcorn · Soul ID · Cinema Studio 3.0 ·
   Draw-to-Video · LipSync Studio
```

| | A'da var | B'de var |
|---|:--:|:--:|
| Seedance 2.0 · Kling 3 · Nano Banana Pro · Seedream 5.0 · GPT Image 2 · Soul | ✅ | ✅ |
| **Veo 3.1 · Sora 2 · Wan 2.6 · Hailuo** | ❌ | ✅ |
| **Google Omni Flash (Gemini)** | ✅ | ❌ |
| **Popcorn · Cinema Studio · Draw-to-Video · LipSync Studio** | ❌ | ✅ (araç, model değil) |

```
⛔ KARAR VERİLMEDİ. İkisi de resmi doküman değil; biri tanıtım sayfası,
   diğeri ikinci el araştırma. Hangi modelin hesapta FİİLEN göründüğü
   ancak kurulumdan sonra bilinir.
   → Kurulum yapılınca ilk iş: modellerin gerçek listesini yaz ve bu
     tabloyu sil.
```

**Bu çelişki neden önemli:** Depodaki mevcut hat **Veo 3.1 Fast** üzerine
kurulu (`VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md`). Rapor Veo 3.1'in
Higgsfield içinde erişilebilir olduğunu söylüyor; tanıtım sayfası söylemiyor.
Doğruysa geçiş ucuz, değilse hat değişikliği demek.

---

## 📊 MODEL × BU DEPONUN İŞİ

> Aşağıdaki "uzmanlık" ve "maliyet" sütunları **rapordan** alındı.
> Bu depoda hiçbiri ölçülmedi. Sayılar rapordaki haliyle korunuyor.

| Model | Rapora göre güçlü olduğu yer | Yerli ses | Kredi (rapor) | Bu depodaki karşılığı |
|---|---|:--:|:--:|---|
| **Google Veo 3.1** | fiziksel gerçekçilik, akışkan, ışık kırılması, kumaş | ✅ diyalog + foley | 40-70 | ⭐ **Fizik ağırlıklı sahneler** — toz, itki, düşen enkaz. Mevcut hattımız zaten bu. |
| **Kling 3.0** | insan anatomisi, karakter tutarlılığı, duygusal ifade | ✅ ortam + çok dil | ~6 | ⭐ **Karakter sahneleri** — yüz, el, yürüyüş. En ucuz. |
| **Seedance 2.0** | komut uyumu, çoklu referans (Omni-Reference), metin | ✅ çift kanal | orta-düşük | ⭐ **Tekrar eden varlık kilidi** (Ders 58) — 9 referans görsel |
| **Wan 2.6** | hızlı iterasyon, 9:16 | belirtilmemiş | düşük | **Dikey shorts** hattı + ucuz taslak |
| **Sora 2** | karmaşık kompozisyon, 3D tutarlılık | ❌ / sınırlı | 40-70 | Sessiz filmlerde pahalı alternatif — önceliğimiz değil |

```
⚠️ "Kredi" sütunu ORANDIR, fiyat değil. Rapor plan fiyatı vermiyor.
   6 vs 70 → aralarında ~11 kat fark var. Bu tek başına iş akışını belirler:
   TASLAK UCUZ MODELDE, FİNAL PAHALI MODELDE.  → 07_URETIM_AKISI.md
```

---

## 🎯 BU DEPO İÇİN ÖNERİLEN EŞLEME — henüz karar değil, hipotez

Depodaki filmlerin ortak profili: **tek karakter · sıfır kesme · fizik
ağırlıklı · çoğu sessiz.** Rapordaki uzmanlık alanlarına göre:

```
YATAY 2-4 DK (13-14 sahne × 10 s)
  fizik sahneleri (toz, itki, düşen enkaz, iniş)   → Veo 3.1
  karakter sahneleri (yüz, el, halka, yürüyüş)     → Kling 3.0
  → AYNI FİLMDE İKİ MODEL kullanmak devamlılık riski taşır.
    ⚠️ Test edilmeden yapılmaz: iki modelin cilt/ışık işleyişi farklıysa
       sahneler arası kayma çıkar ve MANTIK_QA bunu yakalar.

YATAY 7-9 DK (start/end frame zinciri)
  → Referans/anahtar kare desteği en güçlü olan model gerekir.
    Rapor Seedance 2.0'ın 9 referans görsel + 3 referans video aldığını
    söylüyor. Doğruysa 75 imajlık zincir için en uygun aday budur.

DİKEY SHORTS (9:16 · 6 sahne × 8 s)
  → Wan 2.6 (rapor: 9:16 desteği + hızlı iterasyon + düşük maliyet)

KAPAK FOTOĞRAFI (1280×720 metinsiz)
  → Görsel modeller: Nano Banana Pro / Seedream 5.0 / GPT Image 2.
    Rapor bunların kapak için karşılaştırmasını YAPMIYOR. Açık soru.
```

---

## 🔊 YERLİ SES (native audio) — bizim için ne anlama geliyor

Rapora göre Veo 3.1, Kling 3.0 ve Seedance 2.0 videoyu **ve** sesi aynı
geçişte üretiyor: diyalog, ortam sesi, foley.

```
BU DEPODA ÇOĞU FİLM SESSİZ  → yerli ses bir avantaj değil, bir RİSK.
   Model istenmeden ortam sesi veya foley ekleyebilir.
   → Sessiz film üretirken ses kanalının kapatılıp kapatılamadığı
     kurulumdan sonra ilk denenecek şeylerden biri.
   → Kapatılamıyorsa: post'ta sil, ve bunu üretim notuna yaz.

DİYALOGLU FİLM (Dead Approach hattı) → yerli ses gerçek kazanç:
   Risk Kartı 7'nin "sıra alma = lip-sync çöküşü" sorunu, sesi ayrı
   üretip üstüne bindirmekten kaynaklanıyordu.
```

---

## ▶️ KURULUMDAN SONRA İLK ÜÇ ÖLÇÜM

```
1. Gerçek model listesi — yukarıdaki çelişki tablosu silinir
2. Klip süre limiti (saniye) ve extend var mı — yapıyı belirler
3. Sessiz üretim mümkün mü — ses kanalı kapatılabiliyor mu
```

> Bu üçü cevaplanmadan tek bir film Higgsfield'e taşınmaz.
