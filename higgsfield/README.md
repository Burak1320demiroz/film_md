# 🌀 HIGGSFIELD — ÜRETİM MOTORU BÖLÜMÜ

> **Bu bölüm ne değildir:** film yazma kılavuzu. Senaryo, sahne, tür, fizik
> kuralları **`../kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`**'de kalır.
>
> **Bu bölüm nedir:** yazılmış `.md` filmi **görüntüye çeviren araç** katmanı.
> Higgsfield'in CLI/MCP'si, model kartları, komut referansı, maliyet ve
> tuzakları burada durur.
>
> **Kural:** Depodaki film dosyaları araç-bağımsızdır. Bir prompt'un içine
> "Higgsfield ile üret" yazılmaz — hangi motorla üretildiği **üretim notuna**
> düşer (AGENTS.md görev kartı B).

---

## 🧭 SINIR — ne buraya, ne oraya

```
FİLM TARAFI                          MOTOR TARAFI (bu klasör)
──────────────────────────           ──────────────────────────
ne anlatılıyor                       hangi model, hangi komut
sahne haritası, süre, diyalog        en-boy oranı, süre limiti, ses
negatif çekirdek, kamera dili        kredi/maliyet, kuyruk süresi
QA rubrikleri                        red sebepleri, API tuzakları

→ kilavuzlar_ve_sistem_dosyalari/    → higgsfield/klavuzlar/
```

Bir bilgi ikisine de uyuyorsa **film tarafında** durur; burada yalnızca ona
işaret edilir. Aynı bilgiyi iki yerde tutmak, birini yanlış tutmaktır.

---

## 📦 KLASÖR

```
higgsfield/
├── README.md          ← BU DOSYA · bölümün kapısı
└── klavuzlar/
    ├── 00_README.md              ⭐ kılavuz indeksi + doluluk durumu
    ├── 02_MODEL_KARTLARI.md      🆕 model × format · ses · maliyet oranı
    ├── 05_PROMPT_KURALLARI.md    🆕 üç katman · MCSLA ↔ V2 · uzunluk çelişkisi
    ├── 07_URETIM_AKISI.md        🆕 tek değişken · ucuz taslak · seed · 5-8 sn
    └── 09_KARAKTER_TUTARLILIGI.md 🆕 Soul ID ve bizim üç sorunumuz
```

**Durum (03.08.2026):** 4 kılavuz yazıldı, dördü de tek kaynağa dayanıyor
(kullanıcının araştırma raporu) ve **hiçbiri doğrulanmadı.** Kalan 4 dosya
(kurulum, komut referansı, skills, maliyet) resmi doc bekliyor.
Ayrıntı: `klavuzlar/00_README.md`.

---

## 🔌 HIGGSFIELD NEDİR — tek paragraf

Görsel ve video üreten modelleri tek çatı altında toplayan servis. İki bağlanma
yolu var: **MCP** (ajan araç protokolü) ve **CLI** (terminal komutu). Claude Code
ve Codex gibi terminal ajanları için üretici **CLI'yı öneriyor**. Bağlandıktan
sonra ajan; görsel üretir, video üretir, karakter eğitir, geçmiş üretimleri
listeler — hepsi tek oturum içinde.

> ⚠️ Bu paragraf ve aşağıdaki kurulum bloğu **higgsfield.ai tanıtım
> sayfasından** (02.08.2026) alındı, resmi doküman değil. Doc'lar geldiğinde
> `klavuzlar/` altında doğrulanacak ve çelişki çıkarsa **doc kazanır.**

---

## ⚙️ KURULUM — üç komut

```bash
npm i -g @higgsfield/cli          # 1. CLI
higgsfield auth login             # 2. tarayıcıda giriş
npx skills add higgsfield-ai/skills   # 3. yardımcı yetenekler
```

Üçüncü adım depoya yetenek yazar → bittiğinde `AI_AJAN_YETENEKLERI.md` ve
`skills-lock.json` güncellenir (yeni yetenek eklendiğinde zaten kural).

**Durum:** ❌ henüz kurulmadı. Kurulum yapıldığında bu satır güncellenir.

---

## 🎛️ ERİŞİLEBİLEN MODELLER — tanıtım sayfasındaki liste

| Model | Tanıtımdaki tür |
|---|---|
| Seedance 2.0 · 2.0 Fast · 2.0 Mini | video |
| Kling 3 | video |
| Google Omni Flash (Gemini) | video |
| Nano Banana Pro | görsel |
| Seedream 5.0 Lite | görsel |
| GPT Image 2 | görsel |
| Soul 2.0 | görsel / karakter |

Hangi modelin bu depodaki hangi işe (yatay 2-4 dk / 7-9 dk / dikey shorts /
kapak) uygun olduğu **karara bağlanmadı.** Model kartları yazılınca
`klavuzlar/02_MODEL_KARTLARI.md`'ye girer.

> 📌 Depodaki mevcut üretim hattı **Veo 3.1 Fast** üzerine kurulu
> (`VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md`). Higgsfield onun
> yerine geçmez — **ikinci hat**. Hangi filmde hangisinin kullanılacağı,
> model kartları çıktıktan sonra karşılaştırmayla belirlenecek.

---

## 🚧 AÇIK SORULAR — güncellendi 03.08.2026

Araştırma raporu (→ `klavuzlar/`) sekiz sorunun dördünü kapattı,
biri kısmen kapandı, üçü açık kaldı.

```
✅ KAPANDI — rapordan cevaplandı

□ Karakter tutarlılığı: eğitme sistemimizin yerine mi geçer?
     → Soul ID: 20+ fotoğrafla eğitilen kalıcı kimlik katmanı.
       YERİNE GEÇMİYOR, YANINDA çalışıyor — yüzü çözüyor,
       KIYAFETİ çözdüğü belirsiz. Bizim asıl sorunumuz kıyafet.
       → klavuzlar/09_KARAKTER_TUTARLILIGI.md

□ Ses/diyalog native mi, ayrı lipsync adımı mı?
     → Native. Veo 3.1 · Kling 3.0 · Seedance 2.0 videoyu ve sesi
       aynı geçişte üretiyor. ⚠️ Sessiz filmlerimiz için bu bir RİSK.
       → klavuzlar/02_MODEL_KARTLARI.md

□ Önceki üretimi girdi olarak verme (image-to-video, referans) var mı?
     → Var ve geniş: Seedance 2.0 "Omni-Reference" 9 görsel + 3 video +
       3 ses klibi alıyor; Popcorn 4 referans görsel; start/end frame
       koşullandırması destekleniyor.
       → 7-9 dk zincir formatı için doğrudan ilgili.

□ Fiyatlandırma birimi: kredi mi, süre mi?
     → Kredi, video başına. Rapor ORAN veriyor: premium modeller
       ~40-70 kredi, Kling 3.0 ~6 kredi. Plan fiyatı YOK.
       → klavuzlar/07_URETIM_AKISI.md (ucuz taslak stratejisi)

⚠️ KISMEN KAPANDI

□ 9:16 destekleniyor mu, hangi modellerde?
     → Rapor Wan 2.6'nın 9:16 desteklediğini söylüyor ve girdi en-boy
       oranının hedefle aynı olmasını öneriyor. Model bazında tam liste YOK.

🚧 AÇIK — rapor cevaplamıyor

□ Süre limiti nedir? 8 s sabit mi, uzatma (extend) var mı?
     → EN KRİTİK AÇIK SORU. Rapor yalnız tek bir yerde "15 saniye"
       geçiyor (Orb çekimi formatı). Genel limit belirsiz.
       2-4 dk filmler 10 s'lik kliplerin birleşimi — limit yapıyı belirler.
□ Red/moderasyon davranışı: hangi kelimeler reddediliyor?
□ CLI çıktısı dosyaya mı iniyor, URL mi dönüyor?
```

🆕 **RAPORDAN ÇIKAN YENİ AÇIK SORU**

```
□ Modellerin GERÇEK listesi nedir?
     Tanıtım sayfası ile araştırma raporu ÇELİŞİYOR — Veo 3.1, Sora 2,
     Wan 2.6 tanıtımda yok, raporda var. Depodaki mevcut hat Veo 3.1
     üzerine kurulu olduğu için bu çelişki doğrudan hattı ilgilendiriyor.
     → klavuzlar/02_MODEL_KARTLARI.md §ÖNCE BU
```

---

## ▶️ SIRADAKİ ADIM

```
1. ✅ İlk belge geldi (araştırma raporu) → 4 kılavuz yazıldı
2. ⏭️ KURULUM — üç komut yukarıda. Kurulmadan hiçbir kılavuz doğrulanamaz.
3. ⏭️ İLK ÜÇ ÖLÇÜM (02_MODEL_KARTLARI.md sonu):
      · gerçek model listesi  → çelişki tablosu silinir
      · klip süre limiti      → yapıyı belirler
      · sessiz üretim mümkün mü → ses kanalı kapatılabiliyor mu
4. ⏭️ TEK SAHNE DENEMESİ — THE HOLDING FIELD S1 (yay çizmeyen taş).
      Sebep: Ders 59'un düzeltmesi zaten bu sahnede yapıldı, karşılaştırma
      için Veo çıktısı elimizde var. Aynı prompt, iki motor, tek değişken.
5. ⏭️ Sonuç ne olursa olsun üretim notuna ve `08_BILINEN_TUZAKLAR.md`'ye yazılır
6. İş bitince commit (AGENTS.md §5)
```

> ⚠️ **Hiçbir film Higgsfield'e taşınmaz** — açık sorulardan süre limiti ve
> sessiz üretim cevaplanana kadar. Yarım bilgiyle hat değiştirmek, mevcut
> Veo hattını da bozar.
