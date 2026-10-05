# 🧾 BLIND_ORBIT — ÜRETİM DEFTERİ

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
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

> 🆕 Bu film ÇOK KLİPLİ SAHNE rejimindedir: satır SAHNE değil KLİP başınadır (K01…K24) ve
> sıra ÜRETİM sırasıdır, dramatik sıra değildir [D168]. Satır aralıkları 05.10.2026 yazım hâlidir.
> ⭐ İLK SATIR K15 OLMAK ZORUNDA (PLAN · ÜRETİM SIRASI ① · İPTAL KAPISI). K15 iki üretimde
> "yüz durur · kara delik çeyrek tur döner" ölçüsünü tutmazsa kamera A'ya taşınır ve karar sahibe döner.

| klip | prompt kaynağı (dosya · satır) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|---|---|---|---|:--:|---|---|---|
| K15 | `BLIND_ORBIT_BOLUM_2.md` · 123-167 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K20 | `BLIND_ORBIT_BOLUM_2.md` · 360-404 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K21 | `BLIND_ORBIT_BOLUM_2.md` · 406-450 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K18 | `BLIND_ORBIT_BOLUM_2.md` · 263-313 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K24 | `BLIND_ORBIT_BOLUM_2.md` · 548-591 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K23 | `BLIND_ORBIT_BOLUM_2.md` · 504-546 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K01 | `BLIND_ORBIT_BOLUM_1.md` · 37-79 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K02 | `BLIND_ORBIT_BOLUM_1.md` · 81-131 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K19 | `BLIND_ORBIT_BOLUM_2.md` · 315-358 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K16 | `BLIND_ORBIT_BOLUM_2.md` · 169-214 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K17 | `BLIND_ORBIT_BOLUM_2.md` · 216-261 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K22 | `BLIND_ORBIT_BOLUM_2.md` · 452-502 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K14 | `BLIND_ORBIT_BOLUM_2.md` · 76-121 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K13 | `BLIND_ORBIT_BOLUM_2.md` · 32-74 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K03 | `BLIND_ORBIT_BOLUM_1.md` · 133-175 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K04 | `BLIND_ORBIT_BOLUM_1.md` · 177-222 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K05 | `BLIND_ORBIT_BOLUM_1.md` · 224-268 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K06 | `BLIND_ORBIT_BOLUM_1.md` · 270-315 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K07 | `BLIND_ORBIT_BOLUM_1.md` · 317-361 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K08 | `BLIND_ORBIT_BOLUM_1.md` · 363-413 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K09 | `BLIND_ORBIT_BOLUM_1.md` · 415-458 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K10 | `BLIND_ORBIT_BOLUM_1.md` · 460-505 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K11 | `BLIND_ORBIT_BOLUM_1.md` · 507-552 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| K12 | `BLIND_ORBIT_BOLUM_1.md` · 554-598 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |

```
ÜRETİM SIRASI (PLAN'dan · satırlar bu sırayla uzar):
  ⓪ referans paketi RD → RB → RO → RA → RI1 → RI2 → RK1 → RK2 ONAYLANIR (KAPI 0 — defterde satır AÇMAZ)
  ① K15 (İPTAL KAPISI)  ② K20 → K21 (DORUK · ikisi de iki üretimde tutmazsa film ÜRETİLMEZ)
  ③ K18 (merkezî seçim)  ④ K24 → K23  ⑤ K01 → K02  ⑥ K19 · K16 · K17 · K22 · K14 · K13
  ⑦ S2 (K03-K08)  ⑧ S3 (K09-K12)
⛔ İKİNCİ üretilen insanlı klipte kubbe/balon vizör görülürse ÜRETİM DURUR [D146 · RK1/RK2].
⛔ Konuşan ağız kadrajda görülürse klip RET (sebep: okunurluk) — replikler bedensizdir.
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
   ARŞİV: BLIND_ORBIT_K<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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
