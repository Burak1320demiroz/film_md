# 🧾 THE_LAST_TOW — ÜRETİM DEFTERİ

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
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı
PROMPT SAYISI:   ⬜        ← bölüm dosyalarındaki 🎥 VİDEO PROMPT sayısı
⛔ SAHNE ≠ PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
⚠️ ÇOK KLİPLİ SAHNE REJİMİ: burada karşılaştırılan sayı KLİP sayısıdır (48), sahne
   sayısı DEĞİL (12). SCENE COUNT ≠ CLIP COUNT bu rejimde tasarımdır, uyuşmazlık değil
   (QA_SPEC B bloğu: SHOT COUNT = CLIP COUNT = 48).
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

> 🆕 Bu film ÇOK KLİPLİ SAHNE rejimindedir: satır SAHNE değil KLİP başınadır
> (K01…K48) ve sıra ÜRETİM sırasıdır, dramatik sıra değildir [D168].
> ⭐ İLK SATIR K43 OLMAK ZORUNDA (PLAN · ÜRETİM SIRASI ①). K43 kabul edilmezse
> ikinci klip üretilmez.

| klip | prompt kaynağı (dosya · satır) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|---|---|---|---|:--:|---|---|---|
| K43 | `THE_LAST_TOW_BOLUM_2.md` · ⬜-⬜ | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| ⬜ |  |  |  |  |  |  |  |

```
ÜRETİM SIRASI (PLAN'dan · satırlar bu sırayla uzar):
  ① K43   merkezî seçim + BEDEL — filmin en pahalı karesi
  ② K39 + K40   doruk (kopuş ve yük) — aynı oturumda, art arda
  ③ K48   kapanış imajı (kafiye çiftinin ikinci yarısı)
  ④ K02   kafiye çiftinin BİRİNCİ yarısı — ③'ten SONRA, aynı kurulum metniyle
  ⑤ K01   hook
  ⑥ kalan 43 klip, sahne sahne (bir sahnenin klipleri AYNI oturumda [D84 ②])
⛔ K31 ile K43 AYNI GÜN üretilmez: ikisi de yüzsüz yakın kadraj ve ikinci giysiyi
  taşıyor (red defteri #13'ün örüntüsü).
⛔ İKİNCİ üretilen klipte kubbe/balon vizör görülürse ÜRETİM DURUR ve biçim kararı
  sahibe geri gider [D146]. ⚠️ Referans paketi YAZILMADIĞI için bu tek savunmadır.
⛔ K31'de kadrajda bir YÜZ ya da ikinci insan belirirse ÜRETİM DURUR (iptal kapısı ①).
⛔ K44'te iki yüzey ERİYOR/birbirine geçiyorsa ÜRETİM DURUR (iptal kapısı ②);
  hazır düşüş: kanıt K45'e taşınır, kaynama ANI hiç gösterilmez.
```

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik)
SEED:    araçta alan VAR mı önce sınanır [D142]; yoksa "ALAN YOK" yazılır, uydurulmaz
ARAÇ:    Veo · Flow · <başka> — sürüm biliniyorsa yazılır
ARAÇ AYARI [D215 · 14.09.2026] — üç kutu, ilk klipten ÖNCE işaretlenir; işaretsiz kutuyla üretilen klip KABUL edilmez:
   □ altyazı/caption: KAPALI     □ filigran: YOK (ücretli katman/ayar)     □ konuşan ağız: kadraj dışı
   (bu üçü prompt cümlesiyle değil araç ayarıyla çözülür — ADAY-7 kapanışı; kurgu kapısı ④ üç sayıyı masterda ölçer)
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: THE_LAST_TOW_K<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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
□ İLK KABUL satırı = K43 (PLAN'daki ÜRETİM SIRASI'nın ilk halkası — merkezî seçim).
  Değilse İKİNCİ KLİP ÜRETİLMEZ — sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ her kabul edilen klibin satırı var (master'daki sahne sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu dört madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
