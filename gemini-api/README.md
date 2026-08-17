# Gemini API ile Görsel Üretimi

> Araştırma: 2026-08-09 · Canlı test: 2026-08-10

## Durum: ⛔ ÜRETİM YAPILAMIYOR — iki ayrı engel

Gerçek anahtarla test edildi. İki bağımsız blokaj var, ikisi de çözülmeden
tek görsel bile üretilemiyor.

### Engel 1 — Proje erişime kapalı (403)

Anahtarın projesi (`gen-lang-client-0173297387`) **hiçbir modele** istek
atamıyor, görsel değil düz metin bile:

```
403 PERMISSION_DENIED
"Your project has been denied access. Please contact support."
```

Model listeleme (`ListModels`) çalışıyor, üretim (`generateContent`) çalışmıyor —
yani anahtar geçerli, engellenen proje. Google forumlarında yeni açılan
projelerde yaygın; bilinen sebepleri bölge kısıtı, ödeme katmanının
"Unavailable" olması ve otomatik kötüye kullanım tespitinin yanlış işaretlemesi.
Kullanıcı tarafından çözülemiyor, Google destek gerekiyor.

### Engel 2 — Görsel modellerinin ücretsiz kotası sıfır

403 çözülse bile görsel üretimi ücretsiz katmanda **yapısal olarak kapalı.**
Dört görsel modelinin dördü de aynı cevabı verdi:

```
429 RESOURCE_EXHAUSTED
Quota exceeded for metric: generate_content_free_tier_requests, limit: 0
```

`limit: 0` kritik ayrıntı — kota "dolmadı", ücretsiz katmanda tahsis hiç yok.
Beklemek işe yaramaz. Imagen modelleri de 403 verdi (zaten 17 Ağustos 2026'da
kapanıyorlar).

### Karar noktası

| Seçenek | Ne gerekiyor | 6 sahnelik film maliyeti |
|---|---|---|
| Google desteğe başvur | 403'ün sebebini sor; ücretsiz kotayı açmaz | — |
| Faturalamayı aç | Kart tanımla → hem 403 hem kota çözülür | ~$0.20 (2.5-flash) / ~$0.60 (3.1-flash) |
| Başka sağlayıcı | Farklı API'ye geç | — |

Faturalama açılırsa boru hattı hazır: `--kuru` ile önce maliyet görülür,
sonra tek sahne test edilir, beğenilirse tamamı üretilir.

## Modeller ve fiyatlar (Ağustos 2026)

| Model | Model ID | Görsel başı |
|---|---|---|
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | ~$0.034 (sadece 1K) |
| Nano Banana 2 | `gemini-3.1-flash-image` | $0.022–$0.151 |
| Nano Banana Pro | `gemini-3-pro-image` | $0.134–$0.24 |
| Nano Banana (eski) | `gemini-2.5-flash-image` | $0.039 |
| Imagen 4 | — | **Kullanma:** 17.08.2026'da kapanıyor |

Batch API her modelde ~%50 indirim uyguluyor.

## Bu depo için önemli özellikler

- **9:16 (dikey shorts)** ve **16:9 / 21:9 (yatay)** destekleniyor.
- 3.1 Flash'ta **14 referans görsele** kadar — karakter devamlılığı için kritik.
- Pro model görsel içinde okunaklı metin üretiyor (kapak).
- Tüm çıktılara görünmez **SynthID filigranı** ekleniyor.

## ⚠️ Dokümanla SDK arasındaki fark

Resmi doküman `client.interactions.create(...)` gösteriyor ama kurulu SDK'da
(`google-genai 1.47.0`) **böyle bir API yok** — henüz yayınlanmamış bir yüzey.
Çalışan yol:

```python
from google import genai
from google.genai import types

client = genai.Client()
r = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="A lone soldier walking through a snowy trench at dawn",
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="9:16"),
    ),
)
veri = r.candidates[0].content.parts[0].inline_data.data
```

Bu sürümde **çözünürlük parametresi yok**, yalnız `aspect_ratio` var.
`gemini_ortak.gorsel_uret()` iki yüzeyi de destekliyor; yeni API gelirse
onu tercih ediyor.

## Dosyalar

| Dosya | İşi |
|---|---|
| `gemini_ortak.py` | Anahtar yükleme, görsel üretme, hata teşhisi — tek kaynak |
| `probe_free.py` | Erişim testi: kademeli, en fazla 1 görsel/model |
| `promptlari_cikar.py` | Film `.md` → `prompts.json` (promptlara dokunmaz) |
| `film_gorselleri_uret.py` | Toplu üretim; `--kuru`, `--sahne`, kaldığı yerden devam |
| `.env` | `GEMINI_API_KEY=...` — gitignore'da |

## Kurulum ve kullanım

```bash
cd gemini-api
python3 -m venv .venv && ./.venv/bin/pip install google-genai
echo 'GEMINI_API_KEY=...' > .env        # https://aistudio.google.com/apikey

./.venv/bin/python probe_free.py         # erişim var mı?
./.venv/bin/python promptlari_cikar.py ../dikey_shorts_filmler/THE_FIRST_MORNING_DIKEY_SHORTS.md
./.venv/bin/python film_gorselleri_uret.py prompts.json ciktilar/THE_FIRST_MORNING/ --kuru
./.venv/bin/python film_gorselleri_uret.py prompts.json ciktilar/THE_FIRST_MORNING/ --sahne 04
```

Sıra önemli: önce `--kuru` (maliyet), sonra tek sahne (kalite), sonra tamamı.

## Gizlilik notu

Ücretsiz katmanda Google promptları ve çıktıları ürün geliştirmede
kullanabiliyor; ücretli katmanda kullanmıyor. Depodaki özgün senaryoları
ücretsiz katmandan geçirmek, metinleri eğitim verisi olarak vermek anlamına
gelebilir.

## Kaynaklar

- [Görsel üretim dokümanı](https://ai.google.dev/gemini-api/docs/image-generation)
- [Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing)
- [403 "project denied access" forum kayıtları](https://discuss.ai.google.dev/t/gemini-api-project-denied-access-403-permission-denied-on-a-freshly-created-project/175599)
- [Nano Banana 2 duyurusu](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/)
