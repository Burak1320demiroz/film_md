# 🧾 THE_COUNTED_RIVET — ÜRETİM DEFTERİ

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
PROMPT SAYISI:   48        ← 24 🎥 VİDEO + 24 📸 GÖRSEL (bölüm dosyalarından sayıldı)
KLİP SAYISI:     24        ← ⛔ ÇOK KLİPLİ SAHNE: SAHNE (7) ≠ KLİP (24). Makarada
                 sayılacak birim KLİPTİR; "7 sahne saydım" bir uyuşmazlık DEĞİLDİR —
                 24'ten farklı bir KLİP sayısı uyuşmazlıktır [D188 · COK_KLIPLI §1]
⛔ KLİP ≠ VİDEO PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

| klip | prompt kaynağı (dosya · satır) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|---|---|---|---|:--:|---|---|---|
| K14 | `THE_COUNTED_RIVET_BOLUM_2.md` · 61-100 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| ⬜ |  |  |  |  |  |  |  |

```
⭐ ÜRETİM SIRASI — PLAN'dan; dramatik sıra DEĞİLDİR [D168]:
   ① K14  politika kapısı — en red-riskli kare (risk kartı 12)
   ② K15  novum kanıtı · ⛔ İPTAL KAPISI — üç denemede şeridin altındaki boşluk
          okunmazsa TAŞIYICI DEĞİŞİR ve Plan B devreye girer (perçin sayımı
          birincil kanıt olur, şerit ikinci kanıta düşer)
   ③ K21  doruk
   ④ K24  kapanış imajı (K01'in kamera cümlesini birebir taşır)
   ⑤ K01  hook
   ⑥ kalan 19 klip
⛔ İLK KABUL satırı K14 DEĞİLSE ikinci klip üretilmez.
⛔ İkinci üretilen klipte biçim sapması (kubbe/balon vizör) görülürse üretim
   DURUR ve referans paketi kararı sahibe geri gider [04_UYARI ⛔5].
```

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik)
SEED:    araçta alan VAR mı önce sınanır [D142]; yoksa "ALAN YOK" yazılır, uydurulmaz
ARAÇ:    Veo · Flow · <başka> — sürüm biliniyorsa yazılır
ARAÇ AYARI [D215 · 14.09.2026] — üç kutu, ilk klipten ÖNCE işaretlenir; işaretsiz kutuyla üretilen klip KABUL edilmez:
   □ altyazı/caption: KAPALI     □ filigran: YOK (ücretli katman/ayar)     □ konuşan ağız: kadraj dışı
   ⛔ Üçüncü kutu bu filmde YAPISAL olarak kapalı: 0 replik · ağız 24/24 klipte
      kadraj dışı (yüz yalnız K19'da ve orada da konuşmuyor).
   (bu üçü prompt cümlesiyle değil araç ayarıyla çözülür — ADAY-7 kapanışı; kurgu kapısı ④ üç sayıyı masterda ölçer)
KLİP SÜRESİ ÖLÇÜMÜ [D124] — ilk kabul edilen klipten SONRA, bir kez:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
   ÖLÇÜLEN: ⬜ s     PLANLANAN: 10,0 s
   ⛔ Ölçüm 10,0 değilse RUNTIME ve QA_SPEC'in A/B bloğu düzeltilir, PLAN değil:
      ızgara aracın ayarıdır, bir tercih değildir.
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: THE_COUNTED_RIVET_K<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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
| arşiv dosyası | klip | neden farklı (tek cümle) |
|---|---|---|
| ⬜ | ⬜ | ⬜ |
```

---

## 4. ✅ DEFTER KAPANIŞ KONTROLÜ

```
□ İLK KABUL satırı = PLAN'daki ÜRETİM SIRASI'nın ilk halkası (doruk / merkezî seçim).
  Değilse İKİNCİ KLİP ÜRETİLMEZ — sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ her kabul edilen klibin satırı var (master'daki KLİP sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu dört madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
