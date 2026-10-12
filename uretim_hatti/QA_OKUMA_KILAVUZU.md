# 🔬 QA OKUMA KILAVUZU — Gemini raporundan NOTLAR.md satırına

> **Ne için:** TARAMA · SÜREKLİLİK · ANLATIM raporlarının ve İZLEME formlarının tek okuma yolu:
> **bulgu → zaman → çekim → o çekimin promptu → sınıf → NOTLAR.md.**
> **Kim kullanır:** Fable (rapor ya da form gelince) · sahip (doğrulama, altın set, iki oturum) ·
> planlanan rapor-prompt karşılaştırma skill'i (bu dosyayı uygular, yeniden yazmaz).
> **Ne değildir:** puan yok · "bulunamadı" temiz demek değildir (AGENTS §1 ⑥) · kural üretmez (§1 ④).
> **Kaynak:** `ARASTIRMA/04_SUZME_20261007.md` R7 (yalnız KABUL) · `ARASTIRMA/qa_prompt_analizi_20261006/`
> (`GOREV.md` sınıfları · `OZET_topla.txt` sayıları). **Tarih:** 07.10.2026 · **sözleşme v1.0**
> (değişikliği sahip onaylar; sürüm artar, eski sürüm silinmez).

## 1 · Sınıflama sözleşmesi v1.0

Her bulgu **iki ayrı sütun** taşır; biri öbürünün yerine geçmez.

| Sütun | Soru | Değerler |
|---|---|---|
| **Sınıf** | Bu çekimin promptu kusuru önleyebilir miydi? | 🅐 · 🅑 · 🅑+ · 🅒 · 🅓 |
| **Doğduğu yer** (AGENTS §3) | Kusur nerede doğdu, müdahale nereye? | kare · hareket · seçim · kurgu · anlatım · 🅒/🅓'de `—` |

| Sınıf | Tanım |
|---|---|
| 🅐 model sapması | prompt doğru hâli açıkça istedi ya da kusuru açıkça yasakladı; model tutmadı |
| 🅑 prompt boşluğu | gereken nitelik o çekimin promptunda yok |
| 🅑+ prompt daveti | promptun kendi ifadesi kusuru çağırdı ya da prompt kendiyle çelişti |
| 🅒 QA yanıldı | kusur videoda yok, ya da kusur sanılan şey bir tasarım kararı |
| 🅓 eşlenemedi | bulgu bir çekime ve o çekimin promptuna bağlanamıyor |

**Karar ağacı** (sıra değişmez; ilk "evet"te durulur):
```
S1  Bulgu videoda / karede var mı?                    hayır → 🅒 · bakılamıyor → S4
S2  O çekimin promptu bunu çağırdı mı, ya da kendiyle (Görsel ↔ Video ↔ kare) çelişti mi?
                                                       evet → 🅑+   (alıntılanabilen ifade şart)
S3  Prompt doğru hâli açıkça istedi ya da kusuru açıkça yasakladı mı?
                                                       evet → 🅐 · hayır → 🅑
S4  Hiçbiri cevaplanamıyor (an bulunamıyor · içerik hiçbir çekimin promptuna uymuyor ·
    rapor başka filmi anlatıyor)                       → 🅓
```
```
⭐ Promptta belirtilmemiş bir nitelikte modelin varsayılanı model hatası sayılmaz → 🅑.
⭐ "O çekimin promptu" = o denemeye GÖNDERİLEN sürüm: Görsel + Video + başlangıç/bitiş karesi.
   Görselden videoda video promptu yalnız hareketi yazar (04 R6): karede doğru görünen nitelik
   "istenmiş" sayılır; video promptunda yeniden tarif edilmemesi boşluk değildir.
⭐ Talimatın filmin BAŞKA çekiminde yazılı olması yetmez (GOREV.md).
⭐ Tasarım kararını kusur sanmak 🅒'dir: bilinçli sessizlik · opak vizör · post'ta eklenen başlık
   kartı · doğru fizik (BILINEN_TUZAKLAR §D).
```

**Sınır vakaları** (06.10 analizinden):

| Sınır | Vaka | Karar |
|---|---|---|
| 🅐 ↔ 🅑 | GUNES_MEZARI S13: kask kayboldu; vizör cümlesi K12'de var, K13'te yok | talimat başka çekimde → 🅑 |
| 🅑 ↔ 🅐 | THE_COUNTED_RIVET K04: çekicin türü yazılı değil, balyoz pençe çekice döndü | belirtilmemiş nitelikte varsayılan → 🅑 |
| 🅑+ ↔ 🅐 | THE_BRITTLE_EDGE S00: `Dust lifts and never settles` + `no airborne smoke clouds` | yasak yazılı ama aynı prompt çağırıyor; S2 S3'ten önce → 🅑+ |
| 🅑+ ↔ 🅑 | THE_STOLEN_SKY S49: `spring apart`; 06.10'da 🅑, notu "kayma çağırıyor" | çağıran ifade alıntılanabiliyorsa 🅑+; yalnız kilit eksikse 🅑 |
| 🅒 ↔ 🅓 | THE_LAST_TOW K04: başka filmin SPEC'iyle koşu; berrak vizör "altın ayna değil" diye 🔴 | an bulundu, beklenti yanlış → 🅒 |
| 🅓 ↔ 🅒 | THE_LISTENING_WORLD S2-S3: 11 mercek rampa ve gemi anlatıyor; o promptlarda ikisi de yok | görüntü bu promptlardan çıkmamış → 🅓; en yakın çekime zorla bağlanmaz. Yeni hatta önce DENEMELER'deki prompt sürümüne bakılır |

**Doğduğu yer:** başlangıç karesi · gönderilen prompt · ham klip · finaldeki kullanım yan yana açılır
(AGENTS §3). **kare** karede zaten yanlış · **hareket** kare doğru, hareketle bozuluyor · **seçim** ham
klipte temiz aralık var · **kurgu** sıra/tekrar/eksik · **anlatım** görüntü temiz, olay anlaşılmıyor.
Filigran beşine de uymaz: `araç` yazılır (AGENTS §3 kapanma listesi). Örnek: temas cümlesi yazılıyken
el tokaya eriyorsa **🅐 + hareket**; müdahale kadraj ve kesmedir, prompt değil (BILINEN_TUZAKLAR §B 1).

```
⚠️ 05.10'daki "%17" ile 06.10'daki "%56" KARŞILAŞTIRILAMAZ — iki ayrı sınıflama karıştı.
   05.10 (ARIZA_LISTESI T): 49 film · yalnız 🔴 · soru "nerede düzeldi" → prompt metni %17.
   06.10 (OZET_topla): 12 film · 🔴+🟠 698 bulgu · soru "prompt önleyebilir miydi" ·
         payda 🅐+🅑+🅑+ = 443 → (🅑 180 + 🅑+ 68) / 443 = %56.
   Soru, payda ve film kümesi farklı; aynı bulgu hem 🅑 hem "hareket" olabilir.
   Bundan sonra her yüzde sözleşme sürümü + sütun + paydayla birlikte yazılır.
```

## 2 · Okuma protokolü

**1 · Girdi.** Rapor olduğu gibi + hangi prompt, mod (video · kare) ve dosya verildiği (parçaysa
parçanın film içindeki başı) + raporun koşulduğu taslağın `<FORMAT>_filmler/<FILM>/timeline.json`'u (aynı sürüm).
- Önce `python3 uretim_hatti/araclar/kurgu.py kontrol <tl>` → ✅ olmalı. ⚠️ Dosyası eksik parça listeden
  düşer, sonraki bütün zamanlar **sessizce** kayar; `liste --zaman` uyarmaz (07.10.2026, deneme timeline'ıyla görüldü).
- `kurgu.py liste <tl> --kesmeler` → `n  MM:SS.s  Cxx → Cyy  SAME|?` (kesme zamanı = sonraki parçanın başı).
- `kurgu.py liste <tl> --zaman MM:SS.s` → `MM:SS.s → C07 · C07_d2.mp4 içinde 3.40 s` (çekim + ham klipteki saniye).

**2 · Birleştir.** Aynı kusuru anlatan satırlar tek bulgu olur: zaman farkı ±2 s içinde **ve** aynı nesne.
- Nesne kelimeyle değil, gösterilen şeyle eşlenir. Film başına eş anlamlılar sözlüğü: FILM.md'deki ad →
  raporlardaki adlar (rover → "buggy" · gümüş bant → "duct tape", BILINEN_TUZAKLAR §D); NOTLAR.md TARAMA başlığının altına tek satır.
- Birleşen bulgu bütün kaynaklarını taşır (rapor · satır # · güven). Kalibrasyonda (§3) birleştirmeden
  önceki satırlar sayılır. İki satır ayrı çekime düşüyorsa birleştirilmez, 3. adıma gider.

**3 · Kesme yakını.** `--kesmeler`'deki bir kesmeye ±0,5 s yakın bulgu **"kesme yakını"** diye işaretlenir. **Otomatik ret yok.**
İki yandaki iki çekim de açılır, kusurun hangi yanda olduğu kareden okunur. `--zaman` yarı açıktır: tam kesme anı sonraki çekime düşer.

**4 · Zaman → çekim, yalnız `kurgu.py`'yle.**
- Aralık verilmişse (`01:00–01:10`) **başlangıç** alınır. Zaman `time` sütunundan okunur, `what` metnindeki saatten değil.
- Sahne ya da klip numarasıyla aritmetik yapılmaz (`⌊t/10⌋`, "S n"); Gemini'nin yazdığı numaraya bakılmaz.
- ≤90 s parçada film zamanı = parçanın başı + rapor zamanı; parçanın başı kesim kaydından alınır, dosya adından değil.
- Ham klip ve kare modunda zaman klip içidir, çekim verilen dosyanın adıdır (`ham/C07_d2.mp4`). Kontak sayfası
  etiketi saniyedir: `01.png` = 0,00 s (`kareler.py` → `zamanlar.txt`); dosya numarasından zaman hesaplanmaz.
- Çekimin promptu anlatılan içerikle uyuşmuyorsa komşu çekime bakılır: içerik ona uyuyorsa "çapa: içerik"
  notuyla yazılır (06.10 THE_STOLEN_SKY yöntemi), hiçbirine uymuyorsa 🅓.

Eski betikte (`prompt_hata_analizi.py`, eski hat, düzeltilmedi) bulunan dört eşleme hatası; bu adım dördünü kapatır:

| Hata | Vaka (06.10) | Bu hatta neden olmaz |
|---|---|---|
| sıfırdan sayma kayması | THE_BRITTLE_EDGE · THE_LISTENING_WORLD · THE_STILL_POINT: 0 tabanlı sahneler 1 tabanlı ızgarayla eşlendi, bir sahne kaydı | sahne no hesabı yok; çekim timeline'dan |
| aralıkta bitişin alınması | THE_COUNTED_RIVET: `1:00–1:10`'da bitiş alındı, K07 → "S08" | başlangıç alınır |
| dosya adından yanlış bölüm | THE_LAST_GATE: `_PART2_5_`'teki mercek no PART aralığı sanıldı (PART2_5 → +64 s) | parça başı kayıttan |
| okunmayan alt klasör | THE_STOLEN_SKY: raporlar alt klasörde, glob inmedi → 0 bulgu | girdi adıyla verilir; 0 bulguda önce girdi sayılır |

Aynı aileden: THE_BRITTLE_EDGE'de ayrıştırıcı açıklama metnindeki "00:10"u zaman sandı.

**5 · O çekimin promptunu aç, birebir alıntıla.**
- NOTLAR.md → DENEMELER'den o dosyanın (C07 · d2) **prompt sürümü** bulunur; alıntı gönderilen sürümden, güncel metinden değil.
- `<FORMAT>_filmler/<FILM>/PROMPTLAR/<grup>.md` → `## C07` → `### Görsel` + `### Video`. Zincir halkasında Görsel yoktur:
  `EKLE` satırındaki anahtar karenin (`Z1.0` …) Görsel'i açılır. Başlangıç karesi de açılır (`~/film_medya/<FILM>/kare/C07.png`).
- Kusurla ilgili cümle **birebir** alıntılanır (çeviri ya da özet yok); yoksa `YOK`.

**6 · Sınıfla** (§1): ağaç + doğduğu yer. S1'in cevabı insanındır: Fable kare sayfasında duran kusuru görür;
hareket kusurunda S1 sahibin işaretidir (AGENTS §1 ⑤). Cevap yoksa "insan doğrulaması: ?" kalır, sınıf geçicidir.

**7 · NOTLAR.md'ye yaz.**

| Rapor | Bölüm | Şablon sütunları nasıl dolar |
|---|---|---|
| TARAMA | TARAMA | Zaman: film zamanı (ham klip/kare modunda klip içi) · Çekim: `kurgu.py` · Tür: T1-T14 · Ne görüldü: Gemini'nin cümlesi, birebir · Gemini: SURE/LIKELY/UNSURE · İnsan doğrulaması: ✅ var · ❌ yok · ? bakılmadı |
| SÜREKLİLİK | SÜREKLİLİK | Kesme no · zaman: `--kesmeler` · Çekimler: önce → sonra · Karar: "yanlış alarm" = 🅒 |
| ANLATIM | ANLATIM | 1-8 → "planlanan bilgi" tablosu · A1-A4 → ikinci tablo; A1/A2'nin insan doğrulaması İZLEME'de aynı an |
| İZLEME | İZLEME | olduğu gibi; zamanlı cevabın yanına çekim (`--zaman`); 3. soru ("saçma bir şey") ağaçtan geçer, Gemini `—` |

- Her satırın sağına beş sütun: **Sınıf · Doğduğu yer · Prompt (sürüm + alıntı | YOK) · Kesme yakını · Kaynak (geçerli | geçersiz: neden)**.
  Şablonda yoklar; şablona eklenmeleri sahibin kararıdır.
- Gerçek kusur (🅐 · 🅑 · 🅑+) DENEMELER'deki ret nedenine (`→ hareket` …) ya da KARARLAR'a bağlanır.
  Aynı hata iki ayrı filmde tekrar ederse sahibe sorulur (AGENTS §1 ④); kural yazılmaz.

## 3 · Güven ve kalibrasyon

SURE / LIKELY / UNSURE'un bir anlamı olup olmadığı **ölçülür, varsayılmaz**. 07.10.2026'da ölçülmedi
(eski raporlar şiddet yazıyordu: 🔴/🟠); tablo yeni hattın ilk raporlarıyla dolar. Geçerli ve geçersiz kaynak ayrı satırlarda (§4).

| Güven | Satır n | Doğrulandı (🅐 · 🅑 · 🅑+) | Yanlış (🅒) | 🅓 (paydada yok) | Oran | Wilson %95 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| SURE | | | | | | |
| LIKELY | | | | | | |
| UNSURE | | | | | | |

**Altın set:** ≈40-50 bulgu, rastgele (kolay olanlar ayıklanmaz). "Var / yok" hükmü sahibindir, klibi ya da
kareyi görerek. Oran = doğrulandı / (doğrulandı + yanlış). Ölçtüğü **isabettir**; Gemini'nin kaçırdığını ölçmez.

**Wilson aralığı** (küçük n'de ve 0 ya da 1'e yakın oranda normal aralık bozulur):
`alt, üst = ( p̂ + z²/2n ∓ z·√( p̂(1−p̂)/n + z²/4n² ) ) / ( 1 + z²/n )` · p̂ = k/n · z = 1,96 (%95)
- Hesap sınaması (veri değil): k=0, n=15 → 0,000–0,204 · k=12, n=15 → 0,548–0,930.
- Aralıklar örtüşüyorsa güven sınıfları arasındaki fark kanıtlanmamıştır. Eşik yok, otomatik ret yok (§6).

**Sözleşmenin sınaması: Krippendorff α.**
- Sahip aynı 50 bulguyu iki ayrı oturumda beş sınıftan birine koyar (ayrı günler, ilk sınıflamayı görmeden, sıra karıştırılarak).
- α = 1 − D_o / D_e (nominal; D_o gözlenen, D_e şansla beklenen uyuşmazlık).
  **≥0,800 kesin · ≥0,667 geçici** (Krippendorff 2004, s. 241; süzme Y10). Altında: sözleşme yazıldığı gibi uygulanamıyor.
- O zaman karışıklık tablosundan en çok karışan çift bulunur, o sınırın vakası yeniden yazılır → v1.1.
- Aynı kişinin iki oturumu kararlılığı ölçer, iki kişi arasındaki uyumu değil.

## 4 · Geçersiz rapor: atılmaz, ağırlığı düşer

**Kanıt:** 06.10 korpusunda 2.049 🔴/🟠 satırın 1.142'si (**%56**) TEKRAR/GEÇERSİZ sayılan raporlardan
(`qa_prompt_analizi_20261006/korpus.json`). Okununca iki yön çıktı: gerçek kusur (THE_STILL_POINT S02 ⑨ mod V:
kilitli kamera yazılıyken kayma → 🅐) ve yoğun yanılgı (THE_LAST_GATE: 53 🅒'nin 33'ü ⑨-⑫ mod V satırı).

**Bu hatta geçersiz kaynak** (QA_PROMPTLARI'ndaki ⛔ satırlarından; "Kaynak" sütununa nedeniyle yazılır):
`plan` (plan/hikâye/logline/çekim listesi verildi) · `eski sohbet` · `>90 s` · `ne olmalı` (eksik ya da başka filmin) ·
`kesme` (liste parçaya kaydırılmadı) · `ANLATIM` (sessiz ya da film adı verildi) · `biçim` (tablo yok, puan var,
Türkçe — ARIZA Q05) · `eski hat` (mod V · TEKRAR · GEÇERSİZ · KESİK).

**Ağırlık sayıyla değil, sırayla düşer:**
- satır okunur ve ağaçtan geçer; insan doğrulaması (S1 ✅) olmadan ret nedeni olmaz;
- yalnız geçersiz kaynakta görülen bulgu geçerli kaynaklılardan sonra okunur; geçerli bir koşu aynı bulguyu
  verirse (±2 s + aynı nesne) birleşir ve kaynak "geçerli" olur; kalibrasyonda (§3) ayrı satır;
- ANLATIM'a plan sızdıysa 1-8 cevapları "izleyicinin anladığı" diye yazılmaz: ölçtüğü şey bozuldu.

## 5 · Bilinen önyargılar

Liste `BILINEN_TUZAKLAR.md` §D'dedir, burada tekrar edilmez. QA'nın kendi arızaları: `ARIZA_LISTESI.md` Q
(Q03 sahibin kararını hata saymak = 🅒'nin ana kaynağı · Q04 mercek çelişkisi). Okurken ek olarak:
- **1 fps:** Gemini videoyu saniyede 1 kareyle okur; 1 saniyeden kısa kusur (parmak erimesi) videodan kaçar.
  Şüpheli 2-3 saniye TARAMA **KARE MODU**'yla yeniden koşulur (`kareler.py cikar <klip> --hedef … --aralik 0.25 --sayfa`).
- **Uzunluk:** 60-90 saniyeden sonra ayrıntı düşer; video modunda parça ≤90 s (TARAMA).
- **COULD NOT CHECK** kör nokta listesidir: o türde "bulunamadı" bir şey söylemez; NOTLAR'a "bakılamadı" yazılır.
- **CLEAN WINDOWS** ve **CUTS WITH NOTHING FOUND** temiz demek değildir; final insan gözüyle, sesli, baştan sona izlenir.

## 6 · Çürütülenler ve hat dışı (süzme R7 NOT satırları)

| Yöntem | Neden yok | Ne zaman bakılır |
|---|---|---|
| PPI (tahmin destekli çıkarım) | büyük etiketsiz seti küçük etiketli setle birleştirip aralığı daraltır; tek kişilik oturumda gereksiz | — |
| Rogan-Gladen düzeltmesi | ham oranı duyarlılık ve özgüllükle düzeltir; ikisi için Gemini'nin kaçırdığı kusurları da bilmek gerekir (insanın baştan sona işaretlediği film). Altın set yalnız isabeti verir | gerekirse ileride: tür başına gerçek sıklık sorulursa |
| "Wilson alt sınırı %70'in altındaysa raporu reddet" | eşik keyfî | — |
| Geçersiz rapora sabit yüzde indirim | sayı kaynaksız; süzme yalnız "ağırlığı düşürülür" dedi | — |
| 23,976 ↔ 24 fps kayması | Hatta kare sayan adım yok: Gemini saniye verir; kare etiketi, `timeline.json` ve `kurgu.py` saniyeyle çalışır; taslak `fps=` süzgeciyle kare ekleyip atar, hızı değiştirmez. Kayma ancak kare numarası yanlış hızla saniyeye çevrilir ya da video hızlandırılarak dışa aktarılırsa doğar; o zaman bile %0,1 (16 dakikada ≈1 s, ±2 s penceresinin içinde). Flow'un fps'i resmî değil (G13) | SMOKE P6 fps'i ölçer |
