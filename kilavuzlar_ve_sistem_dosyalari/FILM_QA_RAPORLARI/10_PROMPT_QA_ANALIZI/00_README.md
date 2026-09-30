# 🔎 PROMPT QA ANALİZİ — ham QA bulgusu × prompt metni

> **Açılış:** 18.09.2026 · **Girdi:** `02_HAM_RAPORLAR/` + film klasörlerinin prompt dosyaları
> **Makine yarısı:** `../../RAPOR_KONTROL/prompt_hata_analizi.py`
> **Soru:** "Bu kusurun kaynağı PROMPTTA mıydı?"

---

## ⭐ NEDEN VAR

Depoda 564 ham QA raporu var ve hepsi ekranda **görülen** kusuru yazıyor.
Hiçbiri kusurun **sahibini** toplu olarak söylemiyor. Bu soruyu soran tek mercek
⑬ UYUM ve tablosu (`../T13_UYUM_KALITE.md`) bugüne kadar **hiç koşmadı**.
Aynı borç ikinci kez yazılı: `../../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md`
01.08.2026 kesitinde dondu — o gün depoda 11 rapor vardı, bugün 564.

Sonuç: **arıza ölçülüyor ama yazım standardına dönmüyor.** Bu klasör o dönüşü kurar.

```
🅐 MODEL SAPMASI   kilit promptta YAZIYORDU, model tutmadı  → motor sorunu
🅑 PROMPT BOŞLUĞU  kilit HİÇ YOKTU                          → ÖNLENEBİLİR OLAN TEK SINIF
🅒 BULGU DÜŞER     mercek tasarım kararını kusur sanmış     → ⑩ ÖNERME KAPISI
🅓 EŞLENEMEDİ      sahne çapası belirsiz                    → sayılır, sınıfa girmez
```

⛔ **Ölçülen filmin promptuna DOKUNULMAZ.** Prompt tarihtir; bu klasörün çıktısı
SONRAKİ filmin yazım standardıdır [T13 kuralı].

---

## 📁 DOSYALAR

| Dosya | Ne | Kim yazar |
|---|---|---|
| `01_BULGU_DEFTERI.md` | bulgu → sahne eşlemesi, film film | ⛔ **betik** (`--yaz`) |
| `02_FILM_ANALIZLERI/<FILM>.md` | bulgu başına 🅐/🅑 hükmü + **alıntılanmış** prompt cümlesi | okuma |
| `03_PROMPT_HATA_SINIFLARI.md` | ⭐ asıl çıktı: sınıflar, kaç filmde, önerilen yazım kuralı | okuma |
| `04_KAPI_ONERILERI.md` | kapı metni + regex + **ölçülmüş** yanlış-pozitif sayısı | okuma + betik |
| `05_ESLESMEYENLER.md` | B ve C grupları, sebebiyle | ⛔ **betik** (`--yaz`) |

---

## 🚪 GEÇERLİLİK — neyi saymaz

```
✂️ KESİK          rk.kesik_mi GEÇERSİZ dedi → bulgusu alınmaz
⑨-⑫ mod V        plan sadakati merceği belgesiz koştuysa satırı alınmaz [D190]
çapasız satır     zaman damgası da sahne no da yoksa sahneye oturmaz
ızgara dışı çapa  sahne aralığının dışına düşen numara UYDURULMAZ
⛔ KARANTİNA      ③ KİMLİK KAPISI: raporlar başka bir filmi anlatıyor
```

⭐ **ESKİ BİÇİM raporlar SAYILIR.** Ham arşiv üç kuşak rubrik taşıyor; en eskisinde
hiç `##` başlığı yok (THE_FROST_LINE · THE_PAYLOAD · THE_SKYLIGHT). Onlar kesik koşu
değil, **sözleşme öncesi biçimdir** ve kendi şiddet tablolarını taşırlar. Beyaz liste
kullanan ilk sürüm o kuşağı sessizce siliyordu (13 ham rapor → 0 bulgu); betik bu
yüzden **kara liste** kullanır.

---

## ⚠️ KAPININ SINIRI — dürüst kayıt

③ KİMLİK KAPISI'nın **makine yarısı zayıftır**. Ölçüldü ve yazıldı:

```
· rapor künyesindeki FILM: alanı çoğu eski raporda YOK ("künyesiz" — zayıf iz)
· dosya adı kimlik değildir ("the cold weld.mp4" filmin adıdır, "THE LAST
  CUSTODIAN" başka bir filmdir — ikisi de FILM: alanında görüldü)
· süre/sahne aritmetiği yarım ve çeyrek masterları meşru saydığı için
  BAŞKA bir filmin yarım masterını da meşru sayar
· kelime örtüşmesi ölçüldü ve AYIRT ETMEDİ: 31 filmde 0,127-0,351 bandı,
  bant film sözlüğünün BÜYÜKLÜĞÜNÜ ölçüyor, kimliği değil → sahte kapı kurulmadı
```

Bu yüzden kimlik hükmü **okumayla** verilir: raporun anlattığı NESNELER filmin
promptlarındaki nesnelerle karşılaştırılır ve sonuç `prompt_hata_analizi.py`
içindeki `KIMLIK_NOTU`'na yazılır. Sayıdan çıkarma (`KARANTINA`) ayrı ve daha ağır
bir karardır; **bugün boştur** — hiçbir filmin raporu sayıdan çıkarılmadı.

⭐ Bu kapının ilk koşusu bir **yanlış alarmı da kaydetti**: THE_FALLING_WORLD'ün
raporları ilk okumada başka bir filmi anlatıyor sanıldı ("buggy · canyon · duct
tape · eclipse ring"). Nesne nesne karşılaştırılınca kimlik TUTTU — QA modeli
rover'a buggy, gümüş banda duct tape, merceklenmiş halkaya eclipse ring diyor.
**Ders: kimlik kelimeyle değil NESNEYLE eşlenir.**

---

## 🧭 BÖLÜM OFSETİ — 19.09.2026'da eklendi, beş filmi düzeltti

6/8 dk hattında QA birimi **BÖLÜMDÜR** ve ikinci yarımın masterı **0:00'dan
başlar** — ama filmin 240. saniyesidir. İlk sürüm bunu bilmiyordu ve ikinci
yarımın BÜTÜN bulgularını birinci yarının sahnelerine yazıyordu: sessiz ve
toptan yanlış eşleme.

```
düzeltme: ofset = (a − 1) × (film_süresi / Q)
          a  = dosya adındaki bölüm numarası (PART2 · BOLUM_1_2 · PART3_4)
          Q  = round(film_süresi / parça_ölçülen)   ← ölçülen süreden TÜREtilir
⛔ Ofset ölçülen süreden DOĞRUDAN hesaplanmaz: makara nominalden kısa teslim
   edilmiş olabilir (THE_FALLING_WORLD ikinci yarım 230 s ≠ 240 s) ve ölçüyü
   doğrudan kullanmak ofseti iki sahne kaydırır.

ETKİ: BENI_HATIRLAMA 13 · KRONOS_SON_SINYAL 38 · MARS_SON_CIKIS 21 ·
      SUSMAYAN_NOBETCI 17 · THE_FALLING_WORLD 21  = 110 bulgunun sahnesi değişti.
      Sınıflar ve hükümler DEĞİŞMEDİ; 02_FILM_ANALIZLERI'ndeki beş dosya
      uyarı bandı taşır ve kesin numara için deftere işaret eder.
```

---

## ⚠️ SAHNE EŞLEMESİNİN SINIRI — ±1 sahne

Zaman damgası → sahne çevirisi `QA_SPEC`'in `GRID:` satırına dayanır ve ızgara
**varsayımdır** (klip süresi D124 ile ölçülmedikçe 10 s bir tahmindir). Ayrıca
kesme dedektörünün saydığı sahne ile planın sahnesi 31 filmin 26'sında birebir
tutmuyor (`③ kimlik` satırları).

```
✅ GÜVENİLİR   sınıf örüntüsü — "bu filmde temas sınırı cümlesi hiç yok"
⚠️ ±1 SAHNE    tek bir bulgunun tam olarak hangi sahneye düştüğü
⛔ İDDİA EDİLMEZ  "S21'in klibi promptundan saptı" — bu ⑬ UYUM'un işidir,
               kareyle kapanır, bu klasör ondan hüküm çıkarmaz
```

Bu yüzden `03_PROMPT_HATA_SINIFLARI.md` **sınıf** sayar, sahne değil.

---

## 🔬 KAPI ÖNERİSİ NASIL YAZILIR

⛔ Regex önerisi **yanlış-pozitif sayısı ölçülmeden** `04_`'e yazılmaz:

```bash
python3 ../../RAPOR_KONTROL/prompt_hata_analizi.py --regex-dene "<desen>"
```

Betik deseni **bütün depo prompt korpusunda** koşturur ve sahne başına isabet
basar. Gerekçe deponun kendi kaydıdır: `prompt_kontrol.py`'nin yanlış pozitifleri
(`from behind` · `lever` · `through the suit`) kural doğru yazıldığı hâlde
üretimi durdurdu.

⛔ **Bu klasör `prompt_kontrol.py`'yi DEĞİŞTİRMEZ.** `04_` yalnız METNİ hazırlar;
kapının betiğe girmesi ayrı bir iştir ve sahibin onayına bağlıdır.

---

## 🔁 DERS EŞİĞİ

`00_DERS_YAZIM_KONTRATI` §2b burada da geçerlidir: **tek filmde görülen örüntü
ders olmaz.** `03_`'teki her sınıf en az **iki farklı filmden** kanıt taşır;
tek filmlik örüntü ADAY olarak `../../DERSLER/GOZLEM_DEFTERI.md`'ye düşer.


---

## 🐛 YOL BOYUNCA BULUNAN — BU KLASÖRÜN İŞİ DEĞİL, RAPOR EDİLİR

Betik yazılırken format klasörleri **dinamik** tarandı (`yatay_*` / `dikey_*`)
çünkü depodaki iki sabit liste eskimişti. Sonra ölçüldü:

```
⛔ yatay_10_20_dk_filmler ARTIK YOK (13.09.2026 · yatay_10_dk + yatay_16_dk'ya bölündü)
   ama hâlâ sabit listede duruyor:
     sayac.sh           satır 82 · 106 · 274 · 451
     RAPOR_KONTROL/qa_saglik.py   satır 34

SONUÇ (bugün ölçüldü):
     sayac.sh TOPLAM        107
     dosya sistemi          112   (yatay_10_dk 4 + yatay_16_dk 1 sayılmıyor)
     00_INDEX               111
     → `❌ 00_INDEX TUTMUYOR` uyarısı bundan çıkıyor; INDEX değil SAYAÇ eksik sayıyor.
```

Beş film **beş listeden birden** düşüyor: film sayımı · tema dağılımı · SPEC borcu ·
⑯ politika taraması · matris uyumu. ⛔ **Düzeltilmedi** — deponun kanonik film
sayısını değiştirir ve bu sahibin kararıdır. Düzeltme tek satırlık: iki dosyada
`yatay_10_20_dk_filmler` yerine `yatay_10_dk_filmler yatay_16_dk_filmler`.
