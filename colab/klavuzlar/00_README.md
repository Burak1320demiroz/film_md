# 📚 COLAB KILAVUZLARI — İNDEKS

> **Son güncelleme:** 09 Ağustos 2026
> **Bölüm kapısı:** `../README.md`
> **Film tarafı:** `../../kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`

Buradaki her dosya **tek konu** anlatır ve **kaynağını gösterir.** Kaynağı
olmayan cümle kılavuza girmez — tahmin, doc'un yerini tutmaz.

---

## 📦 DURUM — 4 dosya yazıldı, hiçbiri doğrulanmadı

**Kaynak** = hangi belgeden çıkarıldı · **Doğrulama** = fiilen denendi mi.

> ⚠️ Dördünün kaynağı **web araştırması** (08–09.08.2026): iki resmî Google
> blog yazısı, iki resmî GitHub deposu, Colab FAQ, gerisi ikinci el blog/haber.
> **Hiçbiri üretimde doğrulanmadı** — hiçbir şey kurulmadı, tek kare üretilmedi.

| # | Dosya | Ne anlatır | Kaynak | Doğrulama |
|:--:|---|---|:--:|:--:|
| 01 | **`01_BAGLANTI_YOLLARI.md`** | **Colab CLI (birincil)** ve Colab MCP · komut haritası · **iki kaynak çelişkisi** | 📄 resmî blog + repo | ❌ |
| 02 | **`02_DONANIM_VE_MALIYET.md`** | **VRAM tam listesi (16→96 GB)** · T4 tuzağı · compute unit · **Veo ile klip başına kıyas** | 📄 FAQ + repo + blog | ❌ |
| 03 | **`03_MODEL_ADAYLARI.md`** | Video + görsel modeller · VRAM · 9:16 · süre · **karakter hattı** | 📄 model kartları + blog | ❌ |
| 04 | **`04_KURALLAR_VE_RISKLER.md`** | Colab FAQ yasakları · webui kısıtı · oturum kopması · lisans | 📄 FAQ + haber | ❌ |

Planlı ama **yazılmadı** (kurulum yapılmadan içerik uydurulmaz):

```
05_KOMUT_REFERANSI.md      MCP araç adları + parametreler  → kurulum sonrası
06_URETIM_AKISI.md         hücre şablonu, toplu üretim, dosya yolu → ölçüm sonrası
07_BILINEN_TUZAKLAR.md     kopan oturum, OOM deseni, bozuk çıktı → ilk denemeden
```

> Liste sabit değil. **Dosya sayısını korumak için içerik uydurulmaz.**

---

## 🎯 HANGİ DOSYA HANGİ SORUYA BAKAR

```
"Claude Code Colab'ı sürebilir mi?"          → 01
"Kaç GB VRAM kullanabiliyoruz?"              → 02 §VRAM TAM LİSTESİ
"Ücretsiz katman yeter mi, Pro şart mı?"     → 02
"Klip başına kaç para, Veo'dan ucuz mu?"     → 02 §KIYAS
"9:16 · 10 s · sessiz üretebilir miyim?"     → 03
"Kostüm tutarlılığı çözülür mü?"             → 03 §KARAKTER HATTI
"Hesabım kapatılır mı, ticari kullanılır mı?"→ 04
```

---

## 🚧 AÇIK SORULAR — 09.08.2026 güncellemesi

**Colab CLI bulgusu (09.08) üç açık soruyu belge seviyesinde kapattı.**
Araştırma sekiz sorunun beşini kapattı, ikisi kısmen, biri açık.

```
✅ KAPANDI — araştırmadan cevaplandı

□ Claude Code Colab'a bağlanabilir mi?
     → Evet, İKİ yoldan. Colab CLI (Haziran 2026) toplu üretim için
       daha uygun; Colab MCP notebook kurcalamak için.  → 01

□ Ücretsiz katmanda GPU var mı?
     → Var: T4 16 GB. 12 saat üst sınır, 90 dk boşta kopma,
       yoğun saatte GPU hiç verilmeyebilir.  → 02

□ Kaç GB VRAM'e kadar çıkabiliyoruz?
     → 16 GB (T4) → 24 (L4) → 40/80 (A100) → 80 (H100) → 96 GB (G4).
       Ücretsiz katmanda pratikte 16 GB. ⚠️ İstediğin çipin geleceği
       GARANTİ DEĞİL (colabtools #5342/#6013).  → 02

□ GPU tipi ajan tarafından seçilebiliyor mu?
     → Evet: colab new/run --gpu T4|L4|G4|A100|H100  → 01

□ Üretilen dosya depoya nasıl iniyor?
     → colab download UZAK YEREL (+ colab drivemount)  → 01

□ Açık modeller 9:16 ve 10 saniye verebiliyor mu?
     → Evet. LTX-2.3 doğrudan 9:16 + 10 s + Apache 2.0 (ticari serbest).
       Wan 2.2 TI2V-5B 720p/24fps + ilk-son kare akışı.  → 03

⚠️ KISMEN KAPANDI

□ Ücretsiz T4 video üretebilir mi?
     → 16 GB sayı olarak sınırda ama T4 Turing mimarisi: bf16 yok, FP8 yok.
       Modern video modellerinin düşük-VRAM kısayolları bu ikisine dayanıyor.
       → Ücretsiz katman muhtemelen GÖRSEL için; video L4'ten başlıyor.
       ⚠️ Bu çıkarım çip mimarisinden, Colab kaynağından DEĞİL.  → 02 §T4 TUZAĞI

□ 16 GB VRAM hangi modele yeter?
     → Görsel tarafta net: Z-Image-Turbo ve FLUX.2 klein 13–16 GB'a sığıyor.
       Video tarafta kaynaklar ÇELİŞİYOR (LTX-2.3 için 12 GB / 16 GB / 32 GB
       aynı hafta içinde üç ayrı kaynakta). Kuantizasyon (FP8/GGUF) bu aralığı
       kaydırıyor ama kalite bedeli ölçülmemiş.  → 03 §ÇELİŞKİ

□ Maliyet gerçekten Veo'dan düşük mü?
     → Aritmetik "evet, ~10×" diyor ama iki bilinmeyen var: CU yakma oranı
       kaynaklar arasında 1.19–1.76 CU/sa (T4) ve 5.4–15 CU/sa (A100) diye
       çelişiyor; klip başına deneme sayısı (kaç çöp çıktı) bizde ölçülmemiş.
       → 02 §ÇELİŞKİ

🚧 AÇIK — araştırma cevaplamıyor

□ 10+ dakikalık iş gerçekten hayatta kalıyor mu?  ← KALAN EN KRİTİK SORU
     CLI'da "otomatik keep-alive" ve geçici iş koşucusu (colab run) var ama
     ne süre sınırı ne kopma davranışı belgelenmiş. Terminal kapanınca
     iş devam ediyor mu? Ölçülecek → 01 §ÖLÇÜM 2.

□ L4 · H100 · G4 için CU/saat oranı — hiçbir yerde yayınlanmamış.
     Maliyet planının tamamı L4 satırına bağlı.  → 02
```

---

## ✍️ HER KILAVUZUN ZORUNLU ÜST BLOĞU

Yeni dosya açarken bu blokla başla:

```markdown
> **Kaynak:** <hangi belge/URL · tarih>
> **Doğrulama:** ❌ denenmedi | ⚠️ kısmen | ✅ üretimde doğrulandı
> **Son güncelleme:** GG.AA.YYYY
```

Doğrulama işareti `❌` olan bir dosyaya dayanarak **film taşınmaz.**
