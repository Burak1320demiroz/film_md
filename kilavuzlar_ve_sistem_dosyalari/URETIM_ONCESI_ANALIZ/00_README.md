# 🔮 ÜRETİM ÖNCESİ ANALİZ

> ⚠️ **KESİT UYARISI (eklendi 21.08.2026):** Bu klasörün 00/01/02
> dosyaları **01.08.2026 kesitiyle** yazıldı — o gün depoda 11 QA raporu
> ve 50 ders vardı. Güncel sayılar: `bash ../sayac.sh`. 01 raporu
> D51-119'u HİÇ ölçmedi (bilinen borç: `../KILAVUZ_REHBERI.md` §9).
> 02'ye 10-12 kartları 21.08.2026'da eklendi; eski filmlerin `n/9` risk
> skorları 9 kartlık sürümle ölçüldü ve yeniden yazılmaz.
> Akış şeması 22.08.2026'da güncellendi: konsept+tema kapısı ve
> PROMPT_KONTROL adımı işaretçi olarak eklendi (içerik kesit malıdır).

> **Amaç:** Parayı harcamadan önce neyin bozulacağını bilmek.
> **Oluşturma:** 31 Temmuz 2026
> **Girdi:** Yeni üretim YOK. Yalnızca 01.08.2026 kesitindeki 11 QA raporu + 50 ders.

---

## 🎯 BU KLASÖR NEDEN VAR

Kesit gününde projede üç mercek vardı ve **üçü de para harcandıktan
sonra bakıyordu** (bugünkü rubrik listesi: `../QA_PROMPTLARI/00_README.md`):

```
PLAN → BIBLE → PROMPT → ÜRETİM ──┬── VIDEO_QA      ← para harcandı
                                 ├── MANTIK_QA     ← para harcandı
                                 └── SENARYO_QA    ← para harcandı
```

Kesitteki 50 ders (01.08.2026) bu üç mercekten çıktı. Ama kalite tablosunda **11 filmin ortalaması
hiç 5'i geçmedi** ve seri düz: `4 · 5 · 5 · 3 · 4.5 · 4 · 5 · 5 · 3 · 4 · 5`.

**Kural eklemek kaliteyi artırmadı.** Bu klasör bunun üzerine kuruldu:
üretmeden önce, elimizdeki veriye bakarak **bu filmin nerede kırılacağını**
söylemek.

---

## 📁 DOSYALAR

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `01_DERS_ETKINLIK_RAPORU.md` | kesit dersleri (01.08.2026) hangisi işe yarıyor — kanıtla | ders eklerken / çıkarırken |
| `02_RISK_KARTLARI.md` | "Filmde su var" → ne bozulacak, ne yapılmalı | **plan yazmadan önce** |
| `03_PLAN_ONCESI_KONTROL_LISTESI.md` | Yazılmış planı üretime sokmadan tara | plan bitti, üretim başlamadan |
| `04_ARASTIRMA_BULGULARI.md` 🆕 | Dış araştırma turlarının süzme kaydı: hangi bulgu hangi kılavuza indi, hangisi **girmedi ve neden** | dış araştırma geldiğinde · bir kuralın gerekçesi sorulduğunda |
| `05_DIKEY_HAT_TESHISI.md` 🆕 | **Dikey hattın neden "anlamsız" hissettirdiği** — 18 filmin makine taraması, dört üretim önleminin hikâye formatına dönüşme mekanizması, maliyete göre sıralı altı çözüm ve iki prob | dikey film yazmadan önce · "neden hepsi aynı film?" sorulduğunda |
| `06_HIKAYE_HATTI_TESHISI.md` 🆕 | **Bütün deponun neden "saçma" hissettirdiği** — 79 filmin taraması, üç halkalı kapalı döngü (yasaklar türü kurdu · kapılar yalnız üretimi ölçtü · **tür kendini ölçen rubriğe "bu kusur değildir" diye yazıldı**), maliyete göre sıralı çözüm + sahibin iki editoryal kararı | **her film yazmadan önce** · "hikâye neden zayıf?" sorulduğunda · rubrik/novum kuralı tartışılırken |
| `08_SENARYO_ARASTIRMA_PROMPTLARI.md` 🆕 | Hikâye tarafı için dört derin araştırma promptu (çıkarılabilir an · sözsüz istek-hasım · az replikli senaryo · uzay kısa film rakip seti) — altışar cümle, salt prompt, kapanışları aynı | 06'nın açık sorularını dış bilgiyle kapatırken · araştırma turu koşulacağında |
| `12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` ✅ | Uzay üssü / istasyon mimarisi için dört derin araştırma promptu (yörünge dış anatomi · yüzey üssü yapı sistemi · basınçlı iç mekân · tek sabit planda ölçek kanıtı) — altışar cümle, salt prompt, astronot-göreli oran ister, ölçüyü gövdeye yazdırmaz [D138] | kurulacak `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` için araştırma turu koşulacağında · Ders 32 ↔ 138 çelişkisi çözülürken |
| `13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` ✅ | Film girişi ve finali için dört derin araştırma promptu (açılış planı / ilk imge · kapanış planı / muhatap / sonrası bütçesi · açılış-kapanış çifti · süre bandına göre giriş-çıkış bütçesi) — altışar cümle, salt prompt, TUR 1/4 ile çakışanlar "ZATEN VAR" etiketiyle düşer | `HOOK` platosu kırılacağında · `FINAL` §2'ye 10-20 dk satırı yazılacağında · araştırma turu koşulacağında |
| `14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` 🆕 | Deponun ÖLÇÜLMÜŞ dört arızasına vuran dört derin araştırma promptu (sahne zinciri · kurgu kaybı · duygu kanalı · kural temizliği) — altışar cümle, salt prompt, cevabın biçimini dayatmaz, "ZATEN VAR" kapısı açık | 06'nın kapalı döngüsü ve KURGU §0 kaybı kapatılacağında · araştırma turu koştu → TUR 11, süzme 04 §TUR 11 |
| `16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` 🆕 | Mars ekseninde açılan yeni yatay film (15 faz × 12 sahne × 10 s = 30:00, replikli, motor OMNI) için dört derin araştırma promptu (uzun formda tek kişilik hayatta kalma açılışı · yalnız adamın muhatabı ve 10 s klipte replik üretimi · 15 birimlik prosedürelin problem zinciri ve üst katmanı · metinsiz geçen zamanın gövde/mekân merdiveni) — altışar cümle, salt prompt. ⚠️ Künyede ÜÇ AÇIK ÇELİŞKİ kayıtlı: bant tavanı 10 fazdır (15 faz %50 üstü), referans filmin zaman motoru ara yazıdır (bu hatta yasak), OMNI red defteri vaka 15'in motorudur [D167 · kapı ⑲] | plan yazılmadan önce · araştırma turu koşulacağında (TUR 13) |
| `17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` 🆕 | Yeni filmin EKSEN aldığı tek yapımı (The Martian, 2015) söken dört derin araştırma promptu (Mars hattını Dünya hattından ayırma ve bilgi borcu · günlük kamerasının çekim grameri ve yerleşim haritası · FİLM ile GERÇEK ayrı sütunlu Mars künyesi · hasımsız gerilimde mizah ve yetkinlik) — altışar cümle, salt prompt. ⛔ Özel kapısı KOPYA SINIRI [MESHUR_SAHNE §4]: bulgu ancak GEOMETRİYE ve MEKANİZMAYA çevrilerek iner, film/karakter/marka adı üretim promptuna yazılmaz; süzmede üçüncü liste **GEOMETRİYE ÇEVRİLDİ** tutulur. 16 türü sorar, 17 tek yapımı — ayrı tur (TUR 14) | eksen film seçildikten sonra · 16 ile birlikte, plan yazılmadan önce |
| `TUR9_HAM_RAPORLAR/` · `TUR10_HAM_RAPORLAR/` · `TUR11_HAM_RAPORLAR/` 🆕 | TUR 9 (uzay üssü), TUR 10 (giriş/final) ve TUR 11 (ölçülmüş arızalar) ham raporları — düzeltilmemiş, kısaltılmamış, kaynak listeleri dâhil; her dosyanın başında koşulan prompt birebir durur | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |
| `PROB_KOSUSU.md` + `prob_olcum.sh` 🆕 | 05 §5④'ün koşu sayfası: yapıştırmaya hazır iki prob, adım adım koşu, boş sonuç tablosu ve **makineyle ölçüm betiği** (gerçek master üstünde doğrulandı) | dört yasak (ikinci insan · replik · isim · kesme) sınanacağında |

> ⚠️ **04, diğer üçünden farklıdır ve kesit uyarısına tabi değildir.**
> Diğer üçü 01.08.2026 kesitinden konuşur; 04 tarih tarih büyüyen bir
> kayıttır ve ilk turu 27.08.2026'dır. Kural 04'ten okunmaz — 04, kuralın
> NEREDEN geldiğini tutar.

> ⚠️ **05 de kesit uyarısına tabi değildir (30.08.2026).** Kendi taramasını
> kendi içindeki betikle yapar (§9.1) ve istendiği an yeniden koşulabilir.
> ⭐ **05, bu klasörün ilk TERS YÖNLÜ dosyasıdır:** 01/02/03 "bu film
> nerede kırılacak" diye sorar; 05 "yazdığımız her filmin AYNI yerde
> kırılmasının sebebi ne" diye sorar. Tek filme değil, HATTA bakar.

---

## 🔁 AKIŞTAKİ YERİ

```
   FİKİR
     │
     ▼
  KONSEPT + TEMA KAPISI  ← ../ONERME_VE_NOVUM_KILAVUZU.md (üç kabul testi —
     │                      geçmeyen konsept plana dönüşmez) + tema kararı:
     │                      ../TEMA_MUHENDISLIGI_KILAVUZU.md (22.08.2026)
     ▼
  06_HIKAYE_HATTI_TESHISI ← ⛔ HER FORMAT: İSTEK/ENGEL/BEDEL/HASIM'ın
     │                      GEREKÇESİ. Kapı 03_PLAN_ONCESI B5'tedir ve
     │                      prompt_kontrol ⑰ olarak KOŞAR (02.09.2026)
     ▼
  05_DIKEY_HAT_TESHISI   ← ⛔ DİKEY FİLM YAZILACAKSA: dört yasağın
     │                      birikme mekanizması + final vuruş kanıtı
     ▼
  02_RISK_KARTLARI       ← "bu filmde su + canlı + diyalog var"
     │                      → 3 risk kartı, 3 sayısal kilit, 1 uyarı
     ▼
   PLAN + BIBLE yazılır
     │
     ▼
  03_PLAN_ONCESI_KONTROL ← plan kendi içinde çelişiyor mu, sahne sayısı
     │                      tutuyor mu, doruk yazılmış mı
     ▼
   PROMPT
     │
     ▼
  ../PROMPT_KONTROL/     ← betik + rubrik · sıfır kare (12.08.2026)
     │
     ▼
   ÜRETİM → QA mercekleri (güncel liste: ../QA_PROMPTLARI/00_README.md)
     │
     ▼
  01_DERS_ETKINLIK       ← QA sonucu buraya döner: ders tuttu mu tutmadı mı
```

Döngü kapanıyor: QA yeni ders üretiyor, **01** o dersin işe yarayıp
yaramadığını ölçüyor, **02** işe yarayanları bir sonraki filmin planına
sokuyor. Şu ana kadar eksik olan halka **01**'di — ders yazılıyor ama
tuttu mu tutmadı mı hiç ölçülmüyordu.

---

## ⚠️ BU KLASÖRÜN DÜRÜSTLÜK KURALI

```
Her satır bir KANITA dayanır: film adı + kategori skoru veya timestamp.
Kanıt yoksa satır "ÖLÇÜLEMEDİ" yazar — tahmin yazmaz.

Kesit gününde (01.08.2026) 50 dersin 36'sı ÖLÇÜLEMEDİ durumundaydı. Bu bir eksiklik değil,
BULGUNUN KENDİSİ: proje kurallarının çoğunun işe yarayıp yaramadığını
bilmiyor. Bunu gizlemek, 44 dersi 50'ye çıkarıp aynı yerde saymak olurdu.
```

---

## 🔗 KOMŞU KLASÖRLER — karıştırma

| Klasör | Ne zaman | Neye bakar |
|---|---|---|
| **URETIM_ONCESI_ANALIZ** (bu) | üretimden **önce** | geçmiş veriye — "ne bozulacak" |
| `../QA_PROMPTLARI/` | üretimden **sonra** | üretilmiş işe — "ne bozuldu" |
| `../FILM_QA_RAPORLARI/` | sonra | rapor arşivi + üç skor tablosu |
| `../LESSONS_LEARNED.md` | sürekli | ders dizini (güncel sayı: sayac.sh) |
