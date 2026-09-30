# 🧾 GUNES_MEZARI — ÜRETİM DEFTERİ

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

## 0. 🧭 YAZIMIN DEFTERE BIRAKTIĞI — üretim başlamadan okunacak üç şey

> Bu bölümü YAZIM doldurdu (25.09.2026); gerisi ÜRETİM'in. Defter boş doğar
> kuralı satır defteri (§2) içindir — üretim sırası ve ölçüm randevuları
> PLAN'da kararlaştı ve buraya taşınmadıkça kaybolur.

```
⑴ ÜRETİM SIRASI [D168] — ilk kabul satırı bu sıranın ilk halkası OLMAK ZORUNDA:
     ① K21  DORUK        halkalar açılır, küre ayrılıp yükselir     (kurulum I · 24mm · 25,0 m)
     ② K17  BEDEL        mühürler kırılır, gemi ışıkları sırayla ölür (kurulum D · 50mm · 1,3 m)
     ③ K24  FİNAL        oyuk, şimdi ışıkta; üç yapraklı filiz        (kurulum C · 35mm · 2,2 m)
     ④ K01  HOOK         karanlıkta dönen kısık küre                  (kurulum C)
     ⑤ kalan 20 klip, sahne sırasıyla — ⛔ baştan başlanmaz
   GEREKÇE: sıra baştan başlarsa elde hep KURULUM kalır, eksik kalan şey filmin
   KARAR bloğu olur (depoda 3 vaka).
   ⛔ K21 üç denemede tutmazsa PLAN B kapısı açılır: küre kadraja HİÇ girmez,
   K22 birincil kanıt olur (İPTAL KAPISI · 03_SAHNE_SIRALAMASI §7).

⑵ ARAÇ AYARI — ilk klipten ÖNCE, üç kutu (§2'de de duruyor, burada gerekçesi):
     □ altyazı/caption KAPALI   □ filigran YOK   □ konuşan ağız kadraj dışı
   ⭐ BU FİLMDE ÜÇÜNCÜSÜ KOLAY: kadrajda konuşan ağız YOK — tek replik bir
     KAYITTAN gelir (K03 · 24,0 s ve K10 · 90,0 s). Ağız berrak vizörün ardında
     görünür ve film boyunca KAPALI kalır. Araç yine de ayarla kilitlenir.

⑶ ÜÇ ÖLÇÜM RANDEVUSU — tahmin YAZILMAZ, ölçüm buraya yazılır:
   ⬜ KLİP SÜRESİ [D124] — araç gerçekten kaç saniye veriyor? Bütün ızgara
      (24 × 10,0 s = 240,0 s · replik 24,0/90,0 s · müzik 72 BPM ölçü çizgileri)
      bu sayıya bağlı. Aracın verdiği süre 10,0 s DEĞİLSE ızgara yeniden
      hesaplanır, prompt dosyaları DEĞİL (üretimden sonra prompt güncellenmez).
      ölçüm: `ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>`
      ÖLÇÜLEN: ⬜ s     TARİH: ⬜     ARAÇ+SÜRÜM: ⬜
   ⬜ VİZÖR BİÇİMİ — ÜRETİLEN İKİNCİ KLİPTE kontrol edilir: tek düz pane +
      kalın koyu çerçeve mi, yoksa kubbe/balon mu? KUBBE ÇIKARSA ÜRETİM DURUR
      ve karar SAHİBE döner (paket var ama biçim kayması riski kapanmadı — D146).
      SONUÇ: ⬜     hangi klipte: ⬜
   ⬜ KÜRE OKUMASI [A5] — ilk üretilen K21'de küre KÜRE mi okunuyor, ATEŞ TOPU mu?
      Kenar keskin · korona 0 · halkaların iç açıklığına oranı 4/5.
      SONUÇ: ⬜     deneme sayısı: ⬜
   ⬜ ⭐VİRAL ÜÇ ADAY (K03 · K12 · K23) — hedef yazılmadı, ölçüm bekliyor
      (03_SAHNE_SIRALAMASI §7b'nin ikinci ölçümü depoya borçtur)
```

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
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı · BEKLENEN 7
KLİP SAYISI:     ⬜        ← masterda sayılan kesme sayısı · BEKLENEN 24
PROMPT SAYISI:   48       ← bölüm dosyalarındaki 📸+🎥 sayısı (24 image + 24 video) · ölçüldü 25.09.2026
⛔ ÇOK KLİPLİ SAHNE REJİMİ: SAHNE ≠ KLİP ≠ PROMPT olması NORMALDİR (7 ≠ 24 ≠ 48).
   Uyuşmazlık kapısı şudur: masterdaki KLİP sayısı 24 DEĞİLSE hiçbir mercek koşulmaz.
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

| klip | sahne | prompt kaynağı (dosya · satır) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|---|---|---|---|---|:--:|---|---|---|
| K21 | S06 4/4 | `GUNES_MEZARI_BOLUM_2.md` · ⬜-⬜ | ⬜ | ⬜ | 1 | ⬜ | ⬜ | NONE |
| ⬜ |  |  |  |  |  |  |  |  |

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik)
SEED:    araçta alan VAR mı önce sınanır [D142]; yoksa "ALAN YOK" yazılır, uydurulmaz
ARAÇ:    Veo · Flow · <başka> — sürüm biliniyorsa yazılır
ARAÇ AYARI [D215 · 14.09.2026] — üç kutu, ilk klipten ÖNCE işaretlenir; işaretsiz kutuyla üretilen klip KABUL edilmez:
   □ altyazı/caption: KAPALI     □ filigran: YOK (ücretli katman/ayar)     □ konuşan ağız: kadraj dışı
   (bu üçü prompt cümlesiyle değil araç ayarıyla çözülür — ADAY-7 kapanışı; kurgu kapısı ④ üç sayıyı masterda ölçer)
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: GUNES_MEZARI_S<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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
