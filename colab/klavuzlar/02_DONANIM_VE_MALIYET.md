# 💰 02 — DONANIM (VRAM) VE MALİYET

> **Kaynak:** Colab resmî FAQ · @GoogleColab duyurusu (G4 / RTX PRO 6000 eklenmesi) ·
> `googlecolab/google-colab-cli` deposu (`--gpu` değerleri) · Thunder Compute
> "Google Cloud GPU Instances (2026)" ve "Colab Alternatives (Ağustos 2026)" ·
> Chris McCormick Colab GPU yazısı · colabtools issue #5342 ve #6013
> **Doğrulama:** ⚠️ **KISMEN — T4 satırı 11.08.2026'da ÖLÇÜLDÜ** (ücretsiz
> katman, `colab run --gpu T4`). Diğer kartlar hâlâ denenmedi.
> **Son güncelleme:** 11.08.2026

---

## ✅ ÖLÇÜLDÜ — ücretsiz katman T4 (11.08.2026)

Ücretsiz hesap, CLI üzerinden **T4 verdi.** Resmî ajan dosyasının
*"most accounts can only get CPU"* uyarısı bu hesap için gerçekleşmedi.

```
GPU                    Tesla T4 · compute capability 7.5 · 40 SM
VRAM                   14.6 GB   ← "16 GB" pazarlama; torch'un gördüğü bu
sistem RAM             12.7 GB   ← CPU offload bütçesi; VRAM'den KÜÇÜK
disk (boş)             65.9 GB
python / torch         3.12.13 / 2.11.0+cu128
oturum akışı           colab run: aç → koş → kendi kendine kapat  ✅
```

### 🔬 bf16 TUZAĞI — ölçümle kapandı

```
torch.cuda.is_bf16_supported()                       -> VAR   ⚠️ YANILTICI
torch.cuda.is_bf16_supported(including_emulation=False) -> YOK  ✅ gerçek cevap

2048² matmul ×20:   fp16  0.73 ms  ~23.5 TFLOPS
                    bf16  7.94 ms  ~2.2  TFLOPS     → 10.9× YAVAŞ
```

**Sonuç:** T4'te bf16 çalışır ama emülasyonla. bf16 ağırlıklı model fp16'ya
çevrilerek koşulmalı; dtype seçimi `including_emulation=False` ile yapılmalı.
FP8 zaten yok (Ada/Hopper gerekiyor). Bu, üretim betiğinde düzeltildi
(`../betikler/01_FLUX_DEV_NF4.py`) — yanlış kontrol 11× yavaşlatıyordu.

> ⚠️ VRAM sayıları çip modelinden gelir ve güvenilirdir. **CU (kredi) oranları
> ikinci el blog derlemesidir ve birbiriyle çelişir** (→ §ÇELİŞKİ).

---

## 🖥️ COLAB'DA KULLANILABİLEN VRAM — tam liste

Resmî CLI'nın kabul ettiği `--gpu` değerleri: **T4 · L4 · G4 · A100 · H100**
(TPU: `v5e1` · `v6e1`).

| Colab adı | Çip | **VRAM** | Katman | Bizim işimize |
|---|---|---:|---|---|
| **T4** ✅ | Tesla T4 (Turing, 2018) | **14.6 GB ölçüldü** (pazarlama 16 GB) | ücretsiz + ücretli | görsel ✅ · video ⚠️ (bkz. §bf16 TUZAĞI) |
| **L4** | L4 (Ada) | **24 GB** | ücretli | video için **alt eşik**, FP8 destekli |
| **A100** | A100 | **40 GB** · **80 GB** | ücretli | rahat video + LoRA eğitimi |
| **H100** | H100 | **80 GB** (standart kapasite) | ücretli | hız; Colab VRAM'i ayrıca teyit etmiyor |
| **G4** 🆕 | RTX PRO 6000 Blackwell Server Ed. | **96 GB** | ücretli | **en yüksek VRAM** · 960 BF16 TFLOPS (A100-80G'den ~%50 hızlı) |
| TPU v5e1 / v6e1 | — | — | ücretli | diffusers/ComfyUI hattı CUDA'ya bakıyor → pratik değil |

**Yani tavan 96 GB, taban 16 GB.** Ücretsiz katmanda pratikte **16 GB**.

> A100'ün 40 GB mı 80 GB mı geldiği, bir kaynağa göre GPU ayarlarındaki
> **"High RAM"** anahtarıyla seçiliyor. Doğrulanmadı.

---

## ⚠️ İSTEDİĞİN VRAM'İ ALDIĞININ GARANTİSİ YOK

FAQ açıkça yazıyor: *"The types of GPUs and TPUs that are available in Colab
vary over time"* ve kaynaklar *"not guaranteed and not unlimited."*

Sahadan kanıt: colabtools issue #5342 ve #6013 — **Pro kullanıcısı A100
istiyor, sistem otomatik L4'e düşürüyor.** Hiçbir Colab katmanı belirli bir
çipi bir iş boyunca garanti etmiyor.

```
KURAL: her oturumun İLK hücresi GPU adını ve VRAM'i yazdırır.
       Model seçimi ona göre yapılır, tersi değil.

  import torch; p=torch.cuda.get_device_properties(0)
  print(p.name, round(p.total_memory/1024**3,1), "GB")
```

Süre: ücretsiz katmanda notebook **en fazla 12 saat**; Pro+ yeterli CU ile
**24 saate** çıkıyor. Ücretsiz katmanda 90 dk boşta kopma var.

---

## 🕳️ T4 TUZAĞI — ölçüldü, doğru çıktı

Yukarıdaki ölçüm bunu kapattı: T4'te bf16 **emülasyon** (11× yavaş), FP8 yok.
2026 modellerinin çoğu bf16 ağırlıkla geliyor ve düşük-VRAM akışları FP8'e
dayanıyor. İkinci darboğaz: **sistem RAM 12.7 GB, VRAM'den küçük** — yani
"CPU'ya taşır kurtarırız" stratejisinin tavanı düşük.

**Sonuç: ücretsiz T4 = görsel üretimi ve hat testi için. Video için L4 ve üstü.**

---

## 🎯 HANGİ VRAM NE AÇIYOR

```
16 GB (T4, ücretsiz)   Z-Image-Turbo · FLUX.2 klein → KAPAK ve REFERANS KARE
                       video: yalnız kuantize/küçük model, yavaş, bf16 sorunu
24 GB (L4)             LTX-2.3 FP8 · Wan 2.2 5B (offload) · FLUX.2 dev ·
                       Qwen-Image · LoRA eğitimi (önerilen eşik)
40 GB (A100)           LTX-2.3 rahat · kuantizasyon derdi azalır
80 GB (A100/H100)      tam hassasiyet · uzun klip · paralel deneme
96 GB (G4)             LTX-2.3'ün "en az 32 GB" resmî tavsiyesini fazlasıyla
                       aşar → kalite tavanı burada, hız da en iyisi
```

Model eşiklerinin kaynağı ve çelişkileri → `03_MODEL_ADAYLARI.md`.

---

## 🔥 CU YAKMA ORANI — saat başına

**Para birimi compute unit (CU).** 100 CU = $9.99 → **1 CU ≈ $0.10**.
Pro aylık 100 CU, Pro+ aylık 500 CU (Pro+ plan fiyatı doğrulanmadı).

| GPU | CU/sa | ≈ $/sa | Not |
|---|---|---|---|
| T4 16 GB | 1.19 **veya** 1.76 | $0.12–0.18 | iki kaynak çelişiyor |
| L4 24 GB | **bilinmiyor** | — | Kasım 2024'te %20 indirildi, oran yayınlanmamış |
| A100 40 GB | 5.40 **veya** 15 | $0.54–1.50 | 3× çelişki |
| A100 80 GB | 7.52 | ≈ $0.75 | tek kaynak |
| H100 80 GB | **bilinmiyor** | — | — |
| G4 96 GB | **bilinmiyor** | — | 2026'da eklendi, oran yayınlanmamış |

> **Bize en çok gereken üç satır (L4, H100, G4) boş.** İlk ücretli oturumda
> CU sayacına bakarak ölçülecek — Colab harcamayı arayüzde gösteriyor.

---

## ⚖️ KIYAS — klip başına, Veo 3.1 Fast'e karşı

Deponun standart birimi: **10 saniyelik klip.**

```
VEO 3.1 FAST (mevcut hat)
  saniye başına $0.10–0.15 → 10 s klip ≈ $1.00–1.50
  ⚠️ HER DENEME TAM ÜCRET. 4 denemeli sahne ≈ $4–6.
  (Veo 3.1 standart $0.40/s → 10 s ≈ $4.00)

COLAB + AÇIK AĞIRLIK
  saat başına $0.12 (T4) – $0.75 (A100 80 GB); L4/G4 bilinmiyor
  hız tahmini: Wan 2.2 5B tüketici GPU'sunda 5 s/720p için <9 dk
              → 10 s klip ≈ 15 dk → saatte ~4 klip
  10 s klip ≈ $0.03 (T4) – $0.19 (A100 80 GB)
  ⚠️ DENEME PARA DEĞİL, ZAMAN HARCAR.

FİLM ÖLÇEĞİNDE (2-4 dk ≈ 18 klip, tek deneme)
  Veo    ≈ $18–27 · denemeler dahil $50-70
  Colab  ≈ $1–3   · ama 3–6 saat GPU süresi
```

**Mertebe: klip başına ~10×, deneme yoğun sahnelerde daha fazla.**

> 🎯 Asıl kazanç ucuzluk değil, **"tek değişken" kuralının bedava olması.**

**Kıyasa girmeyen maliyet:** kurulum ve bakım bizde, her oturumda 5–10 dk model
yükleme, ve kalite farkı — açık modeller Veo'nun talimat uyumunu vermiyor (→ 03).

---

## ⚔️ ÇELİŞKİ — kapatılacak sayılar

```
□ T4 CU/sa: 1.19 mu 1.76 mı              → tek oturumda ölçülür
□ L4 · H100 · G4 CU/sa: yayınlanmamış     → ölç (L4 en kritik)
□ A100 40 GB: 5.40 mı 15 mi (3× fark)     → ölç
□ A100 80 GB "High RAM" anahtarıyla mı seçiliyor → tek kaynak, doğrula
□ H100 VRAM'i Colab'da 80 GB mı           → çip standardı öyle, Colab yazmıyor
□ Veo Fast saniye ücreti: $0.10/$0.12/$0.15 → resmî Gemini API sayfasından doğrula
□ "10 s klip ≈ 15 dk" TAHMİN — 5 s ölçümünden iki katına çıkarıldı, ölç
```

---

## 🧾 KARAR TASLAĞI — ölçüm gelmeden geçerli değil

```
DENEME       ücretsiz T4 16 GB · yalnız GÖRSEL (Z-Image / FLUX.2 klein)
             sebep: 16 GB'a sığdığı net, maliyet sıfır, köprü test edilir
VİDEO TESTİ  Pro · --gpu L4 (24 GB) · gelmezse T4'e düşürüldüğünü not et
KALİTE ÜSTÜ  --gpu G4 (96 GB) tek klip · LTX-2.3'ü kuantize etmeden dene,
             L4/FP8 çıktısıyla yan yana koy → kuantizasyonun bedeli ölçülür
ÜRETİM       karar bu üç ölçümden sonra
```

Ücretsiz katmanı üretim hattı yapmak **yanlış**: çip garantisi yok, 90 dk
boşta kopma ve 12 sa sınırı toplu üretimi kesiyor, T4 mimarisi modern video
modellerinin kısayollarını desteklemiyor.

---

## 🔗 İLGİLİ

```
Bağlantı yolları (CLI/MCP) → 01_BAGLANTI_YOLLARI.md
Hangi model hangi VRAM      → 03_MODEL_ADAYLARI.md
Kural/risk                  → 04_KURALLAR_VE_RISKLER.md
Higgsfield kredi hattı      → ../../higgsfield/klavuzlar/07_URETIM_AKISI.md
```
