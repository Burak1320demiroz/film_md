# 🧰 BETİKLER — Colab'da çalışan kod

> **Son güncelleme:** 10.08.2026
> **Durum:** ❌ hiçbiri koşturulmadı — kimlik doğrulama insan adımını bekliyor
> **Kılavuzlar:** `../klavuzlar/00_README.md`

Buradaki `.py` dosyaları **Colab VM'inde** çalışır, yerelde değil.
Yerelden `colab run` / `colab exec` ile gönderilir.

```
00_ORTAM_TESTI.py      GPU adı · VRAM · bf16/FP8 desteği · RAM · disk
                       Model indirmez, saniyeler sürer, maliyeti ~sıfır.
01_FLUX_DEV_NF4.py     FLUX.1-dev 12B · 4-bit NF4 · 9:16 kapak görseli
                       + provenance kaydı (.json): seed, adım, süre, tepe VRAM
```

---

## 🚦 ÖNCE İKİ İNSAN ADIMI — ajan yapamaz

### 1. CLI kimlik doğrulama — gcloud GEREKMİYOR

> ⚠️ **`colab skill` ve `colab readme` bu konuda YANLIŞ.** İkisi de varsayılanın
> `adc` olduğunu ve `gcloud` gerektiğini söylüyor. **Kaynak kod aksini
> gösteriyor** (`colab_cli/cli.py`: `AuthProvider.OAUTH2` varsayılan;
> `colab_cli/auth.py`: paketin içinde `oauth_config.json` gömülü).
> Doğrulama tarihi: 11.08.2026. **Kod kazanır.**

Paket, Google'ın cloud-SDK OAuth istemcisini kendi içinde taşıyor ve
kopyala-yapıştır akışı kullanıyor (localhost sunucusu yok, OOB yok):

```bash
colab sessions          # ilk çağrı yetkilendirmeyi başlatır
```

Akış: bir URL basılır → tarayıcıda Google'a girilir → Google bir kod
gösterir → kod terminale yapıştırılır. Token `~/.config/colab-cli/token.json`
altına yazılır, sonraki çağrılar sessizdir.

Gömülü kapsamlar (`auth.py: PUBLIC_SCOPES`) zaten gerekli olanların hepsini
içeriyor — `userinfo.email` (yoksa 401), `colaboratory` (yoksa keep-alive 403),
`cloud-platform`, `openid`, `drive.file`. Yani ADC'nin dört-kapsam derdi burada yok.

> ⚠️ `input()` çağırdığı için **TTY şart** — ajan bu komutu koşamaz, insan koşar.
> `colab` ikili dosyası: `~/.local/bin/colab` (PATH'te).

### 2. Hugging Face token (FLUX.1-dev kapılı depo)

Token'ı **sohbete yapıştırma.** Yerelde bir dosyaya yaz, oturuma yükle:

```bash
printf 'hf_XXXXXXXX' > ~/.hf_token && chmod 600 ~/.hf_token
colab upload -s film ~/.hf_token /root/.cache/huggingface/token
```

Betik önce `HF_TOKEN` ortam değişkenine, sonra bu dosyaya bakar.

---

## ▶️ ÇALIŞTIRMA

### Ortam testi — ilk iş bu (maliyet ~sıfır)

```bash
colab run --gpu T4 --timeout 300 colab/betikler/00_ORTAM_TESTI.py
```

Çıktısı üç şeyi söyler: gerçekten hangi kart geldi, kaç GB VRAM,
**bf16/FP8 var mı.** Bu üçü `../klavuzlar/02_DONANIM_VE_MALIYET.md`'deki
tabloya ölçülmüş satır olarak yazılır.

### FLUX.1-dev kapak görseli

```bash
colab new -s film --gpu T4
colab upload -s film ~/.hf_token /root/.cache/huggingface/token
colab exec -s film -f colab/betikler/01_FLUX_DEV_NF4.py
colab download -s film /content/ciktilar/kapak.png ./kapak.png
colab download -s film /content/ciktilar/kapak.json ./kapak.json
colab stop -s film        # ⛔ UNUTMA — açık oturum CU yakmaya devam eder
```

Depodaki gerçek promptla üretmek için:

```bash
# promptu .md dosyasından bir txt'ye çıkar, sonra:
colab upload -s film prompt.txt /content/prompt.txt
echo 'import sys; sys.argv=["x","--prompt-dosya","/content/prompt.txt"]' | colab exec -s film
```

ya da `colab run` ile tek seferde:

```bash
colab run --gpu T4 --timeout 3600 colab/betikler/01_FLUX_DEV_NF4.py -- \
  --prompt-dosya /content/prompt.txt --true-cfg 4.0
```

---

## ⚠️ BİLİNMESİ GEREKEN DÖRT ŞEY

```
1. --timeout VARSAYILANI 30 SANİYE.
   `colab run`/`exec` için açıkça uzatılmalı. Model indirme + üretim
   T4'te 10-40 dakika sürebilir → --timeout 3600.

2. AÇIK OTURUM PARA YAKAR.
   Hiçbir şey oturumu otomatik kapatmıyor (24 saatlik keep-alive tavanı
   dışında). `colab stop -s <ad>` unutulmaz. `colab run` (--keep'siz)
   işi bitirince VM'i kendi kapatır — bu yüzden tek seferlik işler için
   daha güvenli.

3. HIZLANDIRICI KATMANA BAĞLI.
   Resmî ajan dosyası: "most accounts can only get CPU. Don't assume a
   GPU/TPU will allocate." Ücretsiz hesap T4 alamayabilir — 00 testi
   bunu söyler. Tanınmayan bir --gpu değeri SESSİZCE A100'e düşer.

4. NEGATİF PROMPT VARSAYILAN OLARAK YOK SAYILIYOR.
   FluxPipeline `negative_prompt` alır ama `true_cfg_scale > 1`
   verilmedikçe kullanmaz. Deponun negatif çekirdeği için --true-cfg 4.0
   şart; bedeli ~2x süre.
```

---

## 📏 ÖLÇÜM DEFTERİ — koşturulunca doldurulur

| Tarih | GPU | VRAM | bf16 (yerli) | Model | Ölçü | Adım | Yükleme | Üretim | Tepe VRAM |
|---|---|---|:--:|---|---|--:|--:|--:|--:|
| 11.08.2026 | Tesla T4 (ücretsiz) | 14.6 GB | ❌ (emülasyon, 11× yavaş) | — ortam testi | — | — | — | — | — |

Her satır bir `.json` provenance kaydından gelir. Tahmin yazılmaz.

**11.08.2026 ortam testinden çıkanlar:**

```
· Ücretsiz katman CLI üzerinden T4 VERDİ (skill dosyası "çoğu hesap sadece
  CPU alır" diyordu — bu hesapta öyle olmadı).
· VRAM 14.6 GB · sistem RAM 12.7 GB (VRAM'den KÜÇÜK) · disk 65.9 GB boş
· fp16 ~23.5 TFLOPS · bf16 ~2.2 TFLOPS  → dtype fp16 olacak
· FP8 yok. torch 2.11.0+cu128, python 3.12.13
· colab run akışı sorunsuz: oturum açıldı, koştu, kendi kendine kapandı
```

### 🔴 EN PAHALI DERS — `pip install -U` YAPMA (11.08.2026)

```
Colab'in HAZIR yigini calisiyor ve bizim istedigimiz her seyi iceriyor:
    diffusers 0.39.0 · transformers 5.13.1 · numpy 2.0.2 · torch 2.11.0+cu128
    → StableDiffusionXLPipeline ✅  ZImagePipeline ✅  FluxPipeline ✅

Buna `pip install -U diffusers transformers ...` demek üç kırılma üretti:

1. numpy 2.0.2 → 2.5.2 yükseldi, scipy'nin ikili uyumu bozuldu
     "cannot import name '_center' from 'numpy._core.umath'"
2. transformers 5.13.1 → 5.15.0 yükseldi, diffusers 0.39 ile çalışmıyor
     "Could not import module 'PreTrainedModel'"
3. `transformers<5` ile geri düşürmek huggingface-hub'ı 0.36.2'ye çekti,
     gradio/datasets çakıştı, sonunda KERNEL ÇÖKTÜ ve OTURUM DÜŞTÜ.

KURAL: önce hazır yığını SINA, gerekmedikçe hiçbir şey kurma.
       Kurmak zorundaysan tek paket kur, `-U` verme, numpy/scipy/transformers'a
       dokunma, sonra `colab restart-kernel`.
       Betik bunu destekliyor: URETIM_KURULUM=0 → kurulum adımı atlanır.
```

### 🐞 Diğer üç tuzak — tekrar yaşanmasın

```
1. jupyter-kernel-client SÜRÜM ÇAKIŞMASI
   CLI bağımlılığı sabitlememiş (`Requires-Dist: jupyter-kernel-client`).
   1.0.x'te sınıf adı KernelClient -> JupyterKernelClient olarak değişti,
   CLI eski adı çağırıyor ve her exec `AttributeError` ile ölüyor.
   ÇÖZÜM (uygulandı):
     uv tool install --force google-colab-cli --with "jupyter-kernel-client==0.15.0"

2. is_bf16_supported() YANILTIYOR
   Varsayılan olarak emülasyonu da "var" sayar. Bu kontrole güvenen kod
   T4'te bf16 seçer ve 11× yavaşlar. Doğrusu:
     torch.cuda.is_bf16_supported(including_emulation=False)

3. colab upload HEDEF KLASÖR YOKSA 500 DÖNER
   Contents API ara dizin oluşturmuyor, hata mesajı da bunu söylemiyor.
   Yüklemeden önce:
     echo 'import os; os.makedirs("/content/promptlar", exist_ok=True)' | colab exec -s <ad>

4. OTURUM ÖLEBİLİR — durum kaybolur
   Kernel çökerse `colab status` "Session not found" der ve VM gider;
   inen model de gider. Bu yüzden: uzun işi TEK exec'te koştur, ara
   durumu diske yaz, model indirme ile üretimi aynı çağrıda birleştir.

5. ⛔ ÇALIŞAN OTURUMA İKİNCİ exec ATMA (11.08.2026'da yaşandı)
   Uzun bir `colab exec` sürerken aynı oturuma ilerleme sorma amaçlı
   ikinci `exec` atmak 404/401 üretti ve CLI YEREL KAYDI TEMİZLEDİ
   ("Session appears to be lost. Cleaning up"). İş sunucuda çalışmaya
   devam etti ama artık `-s <ad>` ile erişilemiyor: `colab sessions`
   onu `[?]` orphan olarak gösteriyor, `download` yapılamıyor.
   → İlerleme öğrenmek için exec ATMA. `colab exec` çıktısını zaten
     iş bitince tek seferde döküyor; beklemek tek doğru davranış.
   → `colab status` da (salt okunur olsa bile) aynı anda çalıştırılmaz.
```
