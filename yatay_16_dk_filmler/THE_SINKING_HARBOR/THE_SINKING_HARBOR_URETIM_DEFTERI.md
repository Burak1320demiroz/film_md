# 🧾 THE_SINKING_HARBOR — ÜRETİM DEFTERİ

> **Kim doldurur:** ÜRETİM (görev kartı B). Yazım değil — bu dosya film klasörü
> açılırken BOŞ doğar, her kabul edilen klipte bir satır uzar.
>
> **Neden var (11.09.2026):** ⑬ UYUM merceği "bu klip kendi promptunun dediği şey mi"
> sorusunu sorar ve ikinci bir soruyu daha sorar: **kilit prompt'ta hiç yok muydu,
> yoksa model mi uymadı?** İkinci soru ancak *gönderilen* prompt biliniyorsa
> cevaplanır. Bu defter olmadan mercek, gönderilmemiş olabilecek bir metinle
> kıyaslar ve bulgularının yarısı sahte olur.
>
> ⛔ **DEFTERSİZ ⑬ KOŞUSU YOKTUR.** Rubriğin STEP −1'i bu dosyayı ister.
> ⛔ **Prompt dosyaları ÜRETİMDEN SONRA GÜNCELLENMEZ** — ne bu filmde ne başkasında.
> Üretilmiş filmin promptu kanıttır; ⑬ onu ölçer, değiştirmez. Kazanç bir sonraki
> filmin dersinde toplanır.

---

## 1. 📦 TESLİM SATIRI — master kimliği

> Bir kere yazılır, kurgu bittiğinde. D188'in (teslim şüphesi) ölçüm ayağı budur:
> "plan 16 sahne yazıyor, dört mercek makarada 32 sahne saydı" krizi bu satır
> yazılmadığı için çözülemedi.

```
MASTER DOSYA:    ⬜ (ad + yol)   ⛔ DEPO DIŞINDA durur — bu repoda image/video
                 bulunmaz [.gitignore · 08.09 + 11.09 sahip kararı]. Buraya
                 dosyanın KENDİSİ değil, KİMLİĞİ yazılır.
SHA-256:         ⬜        ← shasum -a 256 <master>
SÜRE:            ⬜ s      ← ölçülen, planlanan değil (ffprobe)
                 (plan 960,000 s — ÖLÇÜLMEDİ, üretim 0 kare)
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı  (plan 24)
PROMPT SAYISI:   92        ← ÖLÇÜLDÜ: bölüm dosyalarında 92 🎥 VİDEO PROMPT
                 (+ 92 📸 IMAGE = 184 prompt · + K01-K04 dört kesim kartı)
⛔ SAHNE ≠ PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
   ⚠️ **BU SATIR BU FİLMDE OLDUĞU GİBİ KOŞMAZ** [22.09.2026 ÇOK KLİPLİ SAHNE]:
   SAHNE ≠ KLİP artık TASARIMDIR. 24 sahne · 92 üretilen klip · 92 video
   promptu. Doğru eşitlik **PROMPT = KLİP**, sahne değil. `sahne_kapisi.sh`
   masterda SAHNE sayarsa 24 beklenir, KESME sayarsa 92.
   ⛔ Mercek koşmadan önce hangisinin sayıldığı YAZILIR, yoksa D188 krizi
   (plan 16 ↔ makarada 32) bu filmde 24 ↔ 92 olarak tekrarlar.
İHRAÇ:           3840×2160 · 24 fps · −14 LUFS · −1,0 dBTP  ← HEDEF (ölçülmedi)
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

| sahne | prompt kaynağı (dosya · satır) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|---|---|---|---|:--:|---|---|---|
| K⬜ | `THE_SINKING_HARBOR_BOLUM_⬜.md` · ⬜-⬜ | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| ⬜ |  |  |  |  |  |  |  |

⛔ **DEFTER BUGÜN BOŞ — ÜRETİM 0 KARE.** Birim SAHNE değil KLİPtir (K01…K96);
   şablonun `S00` satırı bu rejimde `K⬜` olur [ADAY: şablon satırı güncellenmeli].
   PLAN'ın ÜRETİM SIRASI'na göre İLK satır **K84** olacak (doruk), ikinci **K48**
   (merkezî seçim), üçüncü **K96** (kapanış) — sıra baştan başlarsa ikinci klip
   ÜRETİLMEZ [D168 · §4 birinci madde].
⛔ KAPI 0 AÇILMADI: referans paketinin yedi sayfası TASLAK. Hiçbir klip
   üretilemez [D168 · REFERANS_PAKETI §7].

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik)
SEED:    araçta alan VAR mı önce sınanır [D142]; yoksa "ALAN YOK" yazılır, uydurulmaz
ARAÇ:    Veo · Flow · <başka> — sürüm biliniyorsa yazılır
ARAÇ AYARI [D215 · 14.09.2026] — üç kutu, ilk klipten ÖNCE işaretlenir; işaretsiz kutuyla üretilen klip KABUL edilmez:
   ☑ altyazı/caption: KAPALI     ☑ filigran: YOK (ücretli katman/ayar)     ☑ konuşan ağız: kadraj dışı
   ⭐ ÜÇÜ DE YAZIM AŞAMASINDA KARARA BAĞLANDI (04.10.2026) — ayar değil KARAR
      olarak işaretlidir; üretim başlarken araçta FİİLEN sınanır ve sınanmadan
      ilk klip üretilmez [D215 · ADAY-7].
      · altyazı: 38 replik var, hiçbiri ekrana YAZILMAZ (`dialog` negatifi)
      · filigran: ücretli katman gerekiyorsa üretim BEKLER [D138]
      · konuşan ağız: 34 replikli klibin 34'ünde konuşanın ağzı kadraj
        dışında ya da kaskı çevrili — K45 · K55 · K96 bu yüzden böyle
        kurulmuştur, kurulum kararı replikten SONRA değil ÖNCE verildi
   (bu üçü prompt cümlesiyle değil araç ayarıyla çözülür — ADAY-7 kapanışı; kurgu kapısı ④ üç sayıyı masterda ölçer)
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: THE_SINKING_HARBOR_S<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
                                    §3'e birebir kopyalanır (emsal: THE_BLUE_DRIFT_S1_ASBUILT_V1)
⛔ "hatırlamıyorum" bir cevap değildir: o klip için ATIF sütunu ⑬'te
   "🅑 doğrulanamadı" olur ve o sahne kilit sayımına GİRMEZ.
```

---

## 3. 🗄️ AS-BUILT ARŞİVİ — yalnız sapma varsa

> Dosya başına bir giriş; gönderilen metin **birebir**, parafraz değil.
> ⛔ Bu arşiv prompt dosyasının yerine geçmez, onun YANINDA durur: dosyadaki metin
> filmin tasarımı, buradaki metin o klibi gerçekten üreten metindir.

```
| arşiv dosyası | sahne | neden farklı (tek cümle) |
|---|---|---|
| ⬜ | ⬜ | ⬜ |
```

---

## 4. ✅ DEFTER KAPANIŞ KONTROLÜ

```
□ İLK KABUL satırı = PLAN'daki ÜRETİM SIRASI'nın ilk halkası (doruk / merkezî seçim).
  Değilse İKİNCİ KLİP ÜRETİLMEZ — sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ her kabul edilen klibin satırı var (master'daki sahne sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu dört madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
