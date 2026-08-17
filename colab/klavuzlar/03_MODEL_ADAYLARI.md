# 🎛️ 03 — MODEL ADAYLARI (VİDEO + GÖRSEL)

> **Kaynak:** LTX blog "Open Source Video Generation Models (2026)", Wikipedia
> LTX-2 / LTX maddeleri, Hugging Face `Wan-AI/Wan2.2-TI2V-5B` model kartı,
> Thunder Compute / BentoML / Simplismart "Best Open-Source Image Models 2026",
> Isi-dev Colab notebook derlemesi, Stable Diffusion Art ve Civitai yazıları
> **Doğrulama:** ❌ denenmedi — hiçbir model indirilmedi
> **Son güncelleme:** 09.08.2026

> 🖥️ **Colab'da kullanılabilen VRAM:** T4 16 · L4 24 · A100 40/80 · H100 80 ·
> **G4 96 GB.** Yani aşağıdaki eşiklerin *hiçbiri* Colab için erişilemez değil —
> soru "sığar mı" değil, "hangi katmana para verilecek". → `02_DONANIM_VE_MALIYET.md`

> ✅ **ÖLÇÜLDÜ 11.08.2026 — Colab'ın HAZIR yığını yeterli, kurulum gerekmiyor:**
> `diffusers 0.39.0 · transformers 5.13.1 · numpy 2.0.2 · torch 2.11.0+cu128`
> içinde **`StableDiffusionXLPipeline`, `ZImagePipeline`, `FluxPipeline` üçü de
> hazır.** Yani model kodu için `pip install` adımı YOK — sadece ağırlıklar iner.
> ⚠️ `pip install -U` demek bu yığını KIRIYOR → `../betikler/00_README.md` §EN PAHALI DERS

> ⚠️ VRAM sayıları kaynaklar arasında **çelişiyor** (→ §ÇELİŞKİ). Kuantizasyon
> (FP8 / GGUF) bu eşikleri aşağı çeker, kalite bedeli ölçülmemiştir.

---

## 🎬 VİDEO — üç aday

| Model | Lisans | 9:16 | Klip | Ses | VRAM (iddia) | Bize uygunluğu |
|---|---|:--:|---|:--:|---|---|
| **LTX-2.3** | Apache 2.0 | ✅ doğrudan | 10 s'e kadar, birleştirilebilir | native, tek geçiş | 12 / 16 / 32 GB ⚔️ | **1. aday** — 9:16 + 10 s tam bizim shorts kalıbı; LoRA ekosistemi (IC-LoRA, kamera LoRA'ları) en geniş |
| **Wan 2.2 TI2V-5B** | HF model kartı | ölçülmedi | 720p / 24 fps | ❌ yok | 24 GB (offload) · 27.4 GB fp16 | **2. aday** — tek çatıda T2V+I2V, **ilk-son kare** akışı var → zincir formatı |
| **HunyuanVideo 1.5** | ölçülmedi | ölçülmedi | ölçülmedi | ❌ | ölçülmedi | Colab notebook'u mevcut; LoRA eğitimi anlatılıyor |

### Neden LTX-2.3 birinci

```
· Apache 2.0 → YouTube dahil ticari kullanım net (Wan/Hunyuan lisansları DOĞRULANMADI)
· 9:16 desteği kaynakta açıkça yazıyor → dikey_shorts_filmler/ doğrudan hedef
· 10 s klip = deponun standart birimi (8 s'lik Veo kalıbından bile rahat)
· Hugging Face'te 2026 içinde 18M+ indirme → sorun çıkınca topluluk cevabı var
· FP8 kuantizasyonu 32 GB akışları için belgelenmiş → 24 GB'a çekme yolu var
```

### Native ses — risk değil, kapatılabilir düğme

Higgsfield'de native ses bir **risktı** (`../higgsfield/klavuzlar/02_MODEL_KARTLARI.md`)
çünkü servis sesi dayatıyordu. Burada ağırlık bizde: ses kanalı üretilmez ya da
atılır. Sessiz filmlerimiz için sorun yok.

---

## 🖼️ GÖRSEL — kapak, referans kare, LoRA veri seti

| Model | Boyut | VRAM | Güçlü yanı |
|---|---|---|---|
| **Z-Image-Turbo** | 6B | 13–16 GB ✅ | az adımda üretim, ücretsiz T4'e sığan en hızlı seçenek; FLUX.2 dev / Imagen 4 seviyesinde kalite iddiası |
| **FLUX.2 [klein]** | 4B | 13–16 GB ✅ | 16 GB sınıfının ikinci hızlısı |
| **FLUX.1 [dev]** ⭐ | 12B | ≈24 GB bf16 → **NF4 ile <16 GB** | ⭐ **SEÇİLDİ** — ilk deneme bununla. Lisansı iki katmanlı (→ `04`), negatif prompt `true_cfg_scale>1` ister |
| **FLUX.2 [dev]** | — | ≈24 GB | talimat uyumunda lider, VRAM'de en ağır |
| **Qwen-Image** | — | ≈24 GB | görsel içi **okunur metin** (pankart, tabela, kitabe) |
| **Qwen-Image-Edit** | — | ≈24 GB | var olan kareyi düzenleme → **karakter veri seti üretimi** |
| **SDXL** | — | en düşük | en derin LoRA kütüphanesi |

> 📌 `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` işi için ücretsiz T4 + Z-Image
> **bugün denenebilir** — en ucuz, en hızlı doğrulama. Video beklemez.

---

## 🧍 KARAKTER HATTI — deponun en düşük skoru için

Depodaki en düşük ölçülen kategori **Kostüm-Prop** (7 MANTIK raporunun
7'sinde 4/10 altı). Araştırmanın önerdiği dört adımlı zincir:

```
1. TASARIM      Z-Image / FLUX.2 ile karakterin tek kanonik karesi
2. ÇOĞALTMA     Qwen-Image-Edit ile aynı yüz + aynı kıyafet, farklı açı/poz
                → tutarlı veri seti (araştırmanın en çok tekrarlanan tarifi)
3. EĞİTİM       AI Toolkit (Ostris) ile LoRA: Wan / FLUX.2 dev / Qwen / Z-Image / SDXL
                ⚠️ ücretsiz T4'te ancak DÜŞÜK çözünürlükte; 24 GB öneriliyor
4. ÇEKİM        Wan 2.2 ilk-son kare akışı → kamera karakterin etrafında dönerken
                kimlik korunuyor
```

Bu, Higgsfield'in Soul ID'sinin **açık ağırlık karşılığıdır** ama iki farkı var:
ağırlık bizde kalır (tekrar tekrar bedava kullanılır) ve **kıyafeti öğretmek
yüzü öğretmekle aynı mekanizma** — Soul ID'de kıyafetin çözülüp çözülmediği
belirsizdi, LoRA'da veri setine ne koyarsak o öğrenilir.

> ⚠️ Karakterlerimiz **kurgusal** olmalı. Gerçek bir insanın yüzüyle eğitim
> Colab'ın deepfake yasağına girer → `04_KURALLAR_VE_RISKLER.md`.

---

## ⚔️ ÇELİŞKİ — kapatılacak eşikler

```
□ LTX-2.3 VRAM: aynı hafta üç kaynak üç şey diyor
     · resmî doc (aktarıldığı şekliyle): en az 32 GB
     · 1080p için RTX 3080 10 GB "yeterli"
     · alt eşik 12 GB (RTX 3060), rahat 1080p için 16 GB+
   → Colab'da L4 24 GB ile 1080p 9:16 10 s ÜRETİLEBİLİYOR MU: ölç.
   → Çelişki ne çıkarsa çıksın **G4 96 GB en yüksek iddiayı (32 GB) 3× aşıyor**;
     yani "kuantizasyonsuz tam kalite" Colab'da mümkün. Bedeli CU (oranı bilinmiyor).
□ Wan 2.2 TI2V-5B: "24 GB offload ile" ve "27.4 GB fp16 (25 kare, 768×512)"
   birbirini tutmuyor → ücretsiz T4 16 GB için kuantize sürüm ŞART.
□ Wan / Hunyuan / Z-Image LİSANSLARI okunmadı → ticari kullanım belirsiz.
   Apache 2.0 olan yalnız LTX-2.3.
□ Negatif prompt: açık modellerin ayrı negatif girdisi olduğu genel bilgi,
   MODEL BAZINDA doğrulanmadı. Deponun negatif çekirdeği buna dayanacak.
□ Seed determinizmi: diffusers'ta standart, bu modellerde test edilmedi.
```

---

## 🧪 İLK DENEME PLANI — tek değişken

```
HEDEF     bir dikey shorts sahnesi · 9:16 · 10 s · sessiz
MOTOR     LTX-2.3 (L4) — elde Veo çıktısı olan bir sahne seçilir
DEĞİŞKEN  yalnız motor. Prompt, seed niyeti, negatif çekirdek aynı kalır.
ÖLÇÜM     VIDEO_QA (teknik) + MANTIK_QA rubrikleri, aynı rubrik aynı skor tablosu
ÖNCE      ücretsiz T4 + Z-Image ile TEK KAPAK GÖRSELİ — köprüyü doğrular
```

---

## 🔗 İLGİLİ

```
Köprü/kurulum        → 01_BAGLANTI_YOLLARI.md
VRAM hangi katmanda  → 02_DONANIM_VE_MALIYET.md
Lisans/yasak         → 04_KURALLAR_VE_RISKLER.md
Prompt iskeleti      → ../../kilavuzlar_ve_sistem_dosyalari/IMAGE_VIDEO_PROMPT_TEMPLATES.md
Seed/karakter çapası → ../../kilavuzlar_ve_sistem_dosyalari/SAHNE_DEVAMLILIK_KILAVUZU.md
```
