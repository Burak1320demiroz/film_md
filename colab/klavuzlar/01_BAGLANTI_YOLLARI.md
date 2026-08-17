# 🔌 01 — BAĞLANTI YOLLARI: COLAB CLI ve COLAB MCP

> **Kaynak:** Google Developers Blog "Introducing the Google Colab CLI" (Haziran 2026)
> + resmî depo `github.com/googlecolab/google-colab-cli` · MarkTechPost (06.06.2026)
> · Help Net Security (08.06.2026) · Google Developers Blog "Announcing the Colab
> MCP Server" (Nisan 2026) + `github.com/googlecolab/colab-mcp`
> **Doğrulama:** ❌ denenmedi — ikisi de kurulmadı
> **Son güncelleme:** 09.08.2026

---

## 🧭 İKİ AYRI YOL VAR — biri bizim işimiz

Google 2026'da Colab'ı ajanlara **iki** kapıdan açtı. Karıştırılmamalı:

| | **Colab CLI** (Haziran 2026) | **Colab MCP** (Nisan 2026) |
|---|---|---|
| Ne yapar | terminalden runtime açar, yerel script'i uzak GPU'da koşturur | ajanı **tarayıcıdaki** notebook oturumuna köprüler |
| GPU seçimi | ✅ `--gpu T4/L4/G4/A100/H100` | ❓ belgelenmemiş |
| Dosya indirme | ✅ `colab download` | ❓ belgelenmemiş |
| Uzun/arka plan iş | ✅ `colab run` (geçici iş koşucusu) + "otomatik keep-alive" | ❓ belgelenmemiş |
| Tarayıcı gerekir mi | ❌ gerekmez | muhtemelen evet |
| Bizim için | ⭐ **TOPLU ÜRETİM YOLU** | notebook'u elle kurcalarken |

> ⭐ **Karar: Colab CLI birincil yol.** MCP'nin cevaplayamadığı üç açık
> sorumuzu (GPU seçimi · dosya indirme · uzun iş) CLI belgelenmiş komutlarla
> zaten cevaplıyor. Help Net Security manşeti de bunu söylüyor:
> *"Colab CLI opens runtimes to Claude Code and Codex."*

---

## ⚙️ KURULUM — CLI · ✅ 11.08.2026'da YAPILDI

```bash
uv tool install google-colab-cli     # veya: pip install google-colab-cli
```

Kurulu sürüm bu makinede: `~/.local/bin/colab` (uv aracı). Ajan yetenek
dosyası pakete gömülü: **`colab skill`** ve **`colab readme`** komutları basar.

### 🔑 KİMLİK — gcloud GEREKMİYOR (belge yanlış, kod doğru)

```
colab skill / colab readme diyor:   varsayılan `adc`, gcloud ile ADC mint et
KOD diyor (cli.py, auth.py):        varsayılan OAUTH2, oauth_config.json gömülü
                                    → kopyala-yapıştır akışı, gcloud yok
```

Tek komut yetkilendirmeyi başlatır (URL bas → tarayıcıda giriş → kodu yapıştır):

```bash
colab sessions
```

Token `~/.config/colab-cli/token.json`. Gömülü kapsamlar (`PUBLIC_SCOPES`)
`colaboratory` + `userinfo.email` + `cloud-platform` + `openid` + `drive.file`
içeriyor — skill dosyasının "dört kapsamı elle mint et" uyarısı bu yolda geçersiz.

> ⚠️ `input()` kullandığı için TTY şart → **ajan koşamaz, insan koşar.**

> 📌 gcloud denendi ve **geri alındı**: brew cask'ı son adımda
> `gcloud config virtualenv create` çalıştırıyor, o da `github.com`'dan bir
> wheel indiriyor; DNS o an çözmedi ve Homebrew kurulumu purge etti.
> **Artık gerek yok** — oauth2 yolu bunu tamamen atlıyor.

---

## 📋 KOMUT HARİTASI — resmî depodan

```
OTURUM
  colab new [-s AD] [--gpu GPU] [--tpu TPU]     runtime açar (varsayılan CPU)
  colab sessions · colab status · colab stop
  colab restart-kernel · colab url [--open]

ÇALIŞTIRMA
  colab run [--gpu GPU] [--keep] SCRIPT [ARGS]  ⭐ geçici iş: aç → koş → kapat
  colab exec [-s AD] [-f DOSYA] [--output-image PATH]
  colab repl · colab console · colab ssh [--proxy-mode]

DOSYA
  colab ls · colab upload YEREL UZAK · colab download UZAK YEREL
  colab rm · colab edit

OTOMASYON
  colab auth · colab drivemount · colab install [-r requirements.txt | PKG...]
  colab log [-n N] [-o DOSYA] · colab pay · colab version · colab update
```

Hızlandırıcı değerleri: **`--gpu T4 · L4 · G4 · A100 · H100`** ·
**`--tpu v5e1 · v6e1`**. *"Accelerator availability depends on your active
Colab plan"* — yani bayrak yazmak GPU'yu garanti etmiyor (→ `02` §GARANTİ YOK).

`exec` yerel dosyayı okuyup içeriğini gönderiyor: **ayrı yükleme adımı yok**,
yerelde düzenle-koş döngüsü doğrudan çalışıyor.

---

## 🎬 BİZİM AKIŞA OTURMASI — hayali ama komutları gerçek

```
1.  .md filmden prompt bloğu okunur                    (ajan, yerelde)
2.  uretim.py yazılır: model + prompt + seed + negatif  (ajan, yerelde)
3.  colab run --gpu L4 uretim.py                        (10 s klip üretilir)
4.  colab download /content/out.mp4 ./ciktilar/         (dosya yerele iner)
5.  QA rubriği çalıştırılır                             (mevcut sistem)
```

> ⚠️ Bu beş satır **doğrulanmadı.** Komutlar resmî depodan, akış bizim
> varsayımımız. İlk denemeden sonra `06_URETIM_AKISI.md` olarak yazılacak.

`colab ssh` komutunun varlığı ayrıca dikkat çekici: FAQ SSH'i yasaklar ama
resmî CLI kendi SSH'ini sunuyor → **resmî yol üzerinden yapılan iş meşru.**
(FAQ yasakları → `04_KURALLAR_VE_RISKLER.md`)

---

## 🔌 COLAB MCP — ikincil yol, kaydı kalsın

Yerel ajanı bir Colab oturumuna bağlar: hücre açar, markdown/kod yazar, hücre
sırasını değiştirir, `pip install` yapar, kodu çalıştırıp sonucu okur. Kurulum:

```json
"colab-proxy-mcp": {
  "command": "uvx",
  "args": ["git+https://github.com/googlecolab/colab-mcp"],
  "timeout": 30000
}
```

Önkoşul `python`, `git`, `uv`. İstemcinin `notifications/tools/list_changed`
desteklemesi şart; **Claude Code destekliyor.** `timeout: 30000` MCP bağlantı
zaman aşımıdır, hücre süresi değil.

**İki kaynak çelişiyor:** resmî depo köprüyü *"tarayıcıdaki Colab oturumuna"*
bağlıyor; ikinci el bloglar `pip install google-colab-mcp` + `serve --port 8765`
+ başsız OAuth anlatıyor. Resmî satır geçerlidir. Katkı kabul edilmiyor
(issue değil, discussions) → hata çıkarsa düzeltmesini bekleyemeyiz.

**Ne zaman MCP:** notebook'u insan gibi kurcalamak, ara sonuç görmek, hücre
hücre deneme. **Ne zaman CLI:** üretim, toplu klip, dosya indirme.

---

## 🧪 KURULUMDA ÖLÇÜLECEK ÜÇ ŞEY — sırayla

```
1. AYAKTA MI
   colab run --gpu T4 gpu_test.py
   içerik: torch.cuda.get_device_properties(0) → ad + VRAM
   → 02'deki VRAM tablosuna gerçek satır yazılır

2. UZUN İŞ
   10+ dakikalık script. "Otomatik keep-alive" gerçekten koruyor mu?
   Terminali kapatınca / ağ kopunca iş yaşıyor mu, colab log ile geri
   alınabiliyor mu?

3. DOSYA YOLU
   Bir PNG üret, colab download ile depoya indir. Kaç adım, elle müdahale var mı?
```

Üçü geçerse `05_KOMUT_REFERANSI.md` (ölçülmüş bayraklar) ve
`06_URETIM_AKISI.md` (hücre/script şablonu) yazılır.

---

## 🔗 İLGİLİ

```
VRAM ve maliyet   → 02_DONANIM_VE_MALIYET.md
Hangi model       → 03_MODEL_ADAYLARI.md
Yasak/risk        → 04_KURALLAR_VE_RISKLER.md
Ajan yeteneği     → ../../AI_AJAN_YETENEKLERI.md (AGENTS.md kuralı)
```
