# 🧍 KARAKTER DEVAMLILIK KALİTE TABLOSU

> **Kaynak prompt:** `../QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Oluşturma:** 05.08.2026 — rubriğin ilk çalıştırmasıyla birlikte
> (kart E2 kuralı: ilk çalıştıran ajan tabloyu 04'ün formatını taklit ederek açar)
>
> Projenin **dördüncü** skor tablosu. Ne ölçtüğü diğerlerinden farklı:
>
> ```
> LESSONS_LEARNED · KALİTE TAKİP    kare içi teknik    "bu klip doğru mu"
> 03_HIKAYE_KALITE_TABLOSU          dramatik           "kimse umursar mı"
> 04_MANTIK_KALITE_TABLOSU          sahneler arası     "film kendiyle çelişiyor mu"
> 06_KARAKTER_KALITE_TABLOSU ← bu   sahneler arası     "karakter aynı karakter mi"
> ```
>
> ⚠️ Bu rubrik **doküman istemez** (baseline = STEP 1 karakter pasaportu,
> videodan kurulur). Satırlar doğrudan geçerlidir. Karşılığında rubrik
> "bible'daki karakter bu değil" diyemez; çözemediğini `FLAGS FOR DOCUMENT
> CHECK` altına soru yazar, cevaplar film kaydına işlenir.
>
> ⚠️ **MANTIK_QA ile kesişim:** karakterin üzerinde/elindeki her şey bu
> tablonun, dünyaya ait her şey 04'ün. İki rubrik aynı filme koşulduysa
> kesişen kostüm bulguları birleştirmede teke indirilir — Stone Sky'da
> sınır tuttu: rover kayması 04'e, göğüs ünitesi buraya gitti, çift sayım 0.

---

## 📊 TABLO

| Film | Yüz | Saç-Beden | Kostüm | Yıpranma | Ekipman | Kesme | Sayı | Ses | Genel |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **The Stone Sky** | 8 | **9** | 4 | 5 | 8 | 7 | **1** | 8 | **6/10** 🚨 IDENTITY BREAK |
| **The Unbroken City** | **9** | **9** | 8 | 8 | **9** | 8 | N/A | N/A | **8/10** |
| **The Starless Circle** | **9** | **9** | 8 | **9** | **4** | 8 | **1** | N/A | **6/10** 🚨 IDENTITY BREAK |
| **The Blind Return** | 6 | 6 | 4 | **3** | **3** | **3** | N/A | N/A | **4/10** DRIFTS |
| **The Cold Burn** | 7 | 7 | 6 | 5 | **4** | 6 | **7** | →🔊 | **6/10** DRIFTS |
| **The Third Dune** | **9** | **9** | 5 | **3** | 8 | 6 | **9** | 9 | **7/10** DRIFTS |
| **The Ring Light** ⚠️ | 9* | 9* | **4** | 10 | 8* | 9 | **10** | 9* | ⚠️ **8.5/10** DRIFTS |
| **The Last Shift** ⚠️ | **UNV** | 7 | **2** | 9 | **3** | 8 | **10** | N/A | ⚠️ **6.0/10** IDENTITY BREAK |
| ~~**The Black Cradle**~~ | ~~7~~ | ~~7~~ | ~~6~~ | ~~5~~ | ~~6~~ | ~~6~~ | ~~N/A~~ | ~~5~~ | 🚨 **GEÇERSİZ** |

> 🌑 **Black Cradle (17.08.2026) — 🚨 GEÇERSİZ: rubriğin KANIT TABANI EŞİĞİ delindi
> [D97'nin 2. vakası].** Raporun kendi ölçümü: yüz **1/4 sahne · ~25 s / 232 s (%11)**.
> Eşik "3 sahneden az VEYA sürenin %25'inden az → ⚠️ PARTIAL, sayı YOK" diyor; sekiz
> sütunun yedisi yine de puanlandı. Üstüne pasaportlar 4 sahnelik envanterden kuruldu
> [DERS 107] ve **Ses 5/10** aynı filme SES_QA koşulduğu hâlde puanlandı — kart E2
> adım 5 / kart E3 adım 6 gereği →🔊 işaretçisine inmeliydi [DERS 108].
> ⛔ Kilit çelişkisi: rapor **altın tonlu yansıtıcı vizör** ve **kırık beyaz-gri suit**
> gördü; plan **optik berrak, yansımasız vizör** [D79/D95] + **mat kömür siyahı** suit
> diyor. Aynı dosyaya koşulan VIDEO_QA "dark matte + orange/teal accent" yazdı —
> yani iki rapor birbirini de yalanlıyor. Roller de ters: planda **pilot KADIN**
> (turkuaz) · **mühendis ERKEK** (amber) ve ikisi aynı kabinde.
> ⬜ 11 madde AÇIK [D96]:
> [`01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`](01_FILM_RAPORLARI/THE_BLACK_CRADLE.md)

> 🟫 **Last Shift (16.08.2026) — ⭐ D95 ve D97 bu koşuda TUTTU.** Yüz sütunu
> **UNVERIFIABLE** yazıldı ve kanıt tabanı ölçüldü (kadın 0 s / 14 sahne · erkek
> ~10 s / 2 sahne); kask "sealed — evidence: solid visor pane and collar lock"
> diye KANITLA kaydedildi. Ring Light'ta aynı iki sütun 9/10 yazılmıştı.
> ✅ **D89 de tuttu:** filmin tek ekipman değişimi S10'daki SAĞ eldivendir ve rapor
> tam onu gördü — ikinci mühür açılmadı.
> 🔴 Kostüm 2/10'un tek kaynağı 2:20: bant SOL koldan SAĞ kola geçiyor, bot modeli
> değişiyor (§0.12 KADRO KİLİDİ). Raporun 0:20 taban okuması kilide birebir uyduğu
> için bu bulgunun ön kabulü GÜÇLÜ, ama defterde ⬜ AÇIK [D96] — master kontrolü
> bekliyor. Ekipman 3/10 (kutu ve kanca çubuk) kurgu sırası değişimiyle
> açıklanabilir → aynı defter, madde 4-5.
> ⚠️ Aritmetik notu: raporun altı sayılı sütununun ortalaması 6.5, rapor 6.0 yazdı
> (D62a örüntüsü, ölçüm gürültüsü bandının içinde).
> Belge cevapları: [`01_FILM_RAPORLARI/THE_LAST_SHIFT.md`](01_FILM_RAPORLARI/THE_LAST_SHIFT.md)

> 🪐 **Ring Light satırı ŞARTLI — `*` işaretli dört sütun filmin %14'ünden
> ölçüldü (12.08.2026).** İki insan 6 sahnede var, ama yüz yalnız son iki
> sahnede okunuyor: **20 s / 144 s.** Pasaport 2:00'da kuruldu, Yüz 9 ve
> Saç-Beden 9 iki sahnenin karşılaştırmasından yazıldı → **DERS 97** (kanıt
> tabanı eşiği: 3 sahneden azsa kategori sayı taşımaz).
> ⛔ **Ses 9/10 GEÇERSİZ:** gerekçesi "single on-screen spoken line matches the
> physical body" — filmde ekranda konuşan ağız YOKTUR, 7 repliğin 7'si gövdesiz
> AI'dır (§0.11, D82'nin yapısal panzehiri). Sütun N/A olmalıydı; N/A ile genel
> 8.4 olurdu. Rapor bir insan repliği duyduğunu bildiriyor → kilit çelişkisi
> defteri madde 1, master dinlenerek kapanır (**DERS 96**).
> ⛔ **Ekipman 8/10 da şüpheli:** rapor "visors up/retracted, unhelmeted faces"
> okudu; plan `kask 14/14 mühürlü, durum değişimi 0` diyor. En muhtemel sebep
> üretim hatası değil, kilidin görünmezliği: renksiz + yansımasız + çerçevesiz
> vizör ekranda "vizör yok"tan ayırt edilemiyor → **DERS 95**.
> ✅ **Kostüm 4/10 AYAKTA ve tek gerçek üretim bulgusu:** S12 (2:00) ↔ S13
> (2:10) arasında iki suitin de omuz/göğüs plakaları değişiyor; planda hiçbir
> kostüm değişimi yok. S13 yeniden üretilir, çapa S12'nin son karesi.
> ✅ **Sayı 10/10 · klonsuz** — D69/77 sıcak noktası (biniş-iniş) bu filmde
> **planda hiç açılmadı** (§0.14 A4: biniş hareketi 0 sahne) ve klon çıkmadı.
> Belge cevapları: [`01_FILM_RAPORLARI/THE_RING_LIGHT.md`](01_FILM_RAPORLARI/THE_RING_LIGHT.md)

> 🏜️ **Third Dune satırı (11.08.2026):** deponun **ikinci** iki karakterli
> koşusu ve ikincisi de **KLONSUZ** (Sayı 9) — D69/77 sıcak noktası
> (araç biniş-iniş) bu filmde de tekrarlamadı, üstelik filmde kargo boşaltma
> ve kokpit sahneleri VAR. Yüz yine tuttu (9), örüntü bozulmadı.
> ⚠️ **Yıpranma 3 = tablonun en düşük ikinci değeri** ve bu kez sebep eksik
> cümle DEĞİL: toz seviyesi 3 kademeli sayısal takvimle her sahneye, temiz
> referans şeridi çapasıyla birlikte yazılmıştı. 2:29'da kaskatı kumlu iki
> suit 2:40'ta tertemiz. → **DERS 84** (metin kilidi sahneler arasını
> tutmuyor). Sırt ünitesi D79'un **5. vakası**, ilk kez cümlenin VARLIĞINA
> rağmen. Ses sütunu puanlandı çünkü SES_QA koşusu girdisiz kaldı (geçersiz).
> Belge cevapları: `01_FILM_RAPORLARI/THE_THIRD_DUNE.md`

> 🔊 **Cold Burn satırı (09.08.2026):** Ses sütunu `→🔊` — SES_QA aynı
> kurguya koşulduğu için ses bulguları 07_SES_KALITE_TABLOSU.md'de
> raporlandı, burada işaretçiye indi (kart E3 adım 6, çift sayım yasağı).
> KLONSUZ koşu: D69/77 sıcak noktası tekrarlamadı — ama planın en riskli
> sahnesi (S25 tünel) zaten ekranda yok, bu yüzden "azaltım tuttu" kanıtı
> sayılmaz. Pasaport D79'u 4. kez yakaladı (iki suitte de sırt ünitesi;
> bible SIRT DÜZ diyor) — üretim zinciri şerhiyle, bkz. film kaydı.

```
ÖLÇÜLEN FİLM: 6        ⚠️ altı satırla ortalama/örüntü çıkarılmaz (±1.3 sapma kuralı)
IDENTITY BREAK: 2/5    ikisi de KLON — Stone Sky 1:40 (araçtan iniş) ·
                       Starless Circle 2:10 (gemiye biniş). İkisinde de
                       Sayı-Ayrışma 1/10, diğer kategoriler 8-9 bandında.
                       Blind Return klonsuz çıktı (Sayı N/A — tek karakter).
ÖRÜNTÜ:                YÜZ TUTUYOR (8-9-9; Blind Return 6 — köpük S11+ yüzü
                       tasarım gereği kapatıyor), SAYI TUTMUYOR (2 klon).
EKİPMAN İLK KEZ DÜŞTÜ: Starless Circle 4/10 — vizör açık/aynalı arasında
                       gidip geliyor; bible "no tint, no coating" diyordu
                       ve cümle negatif çekirdekte yoktu → DERS 79
SIRT ÜNİTESİ 3. VAKA:  Blind Return pasaportu yine "Backpack" + "dual
                       headlamps" yazdı; bible ikisini de yasaklıyor,
                       D79 cümlesi çekirdekte yine yoktu → D79 ×3 · D77
```

> ⚠️ **Dördüncü koşu (07.08.2026 · THE BLIND RETURN) — 4.0'ın çoğu
> tasarımın ve kurgunun cezası.** Üç MAJOR'ın üçü de belge kontrolünde
> kimlik değiştirdi: ① "opak kask takası" (01:56) filmin DORUĞU —
> FOAM SCHEDULE köpüğün vizörün tamamını örtmesini şart koşuyor, yüz
> S11-S14 tasarım gereği görünmez (bulgu düşer); ② "silinen hasar" (02:40)
> S16'nın planlı YENİ vizörü — ama kurulum sahnesi S15 kurguda olmadığı
> için ekranda "sihirli tamir" gibi okundu (bulgu kurgu hatası olarak
> ayakta → DERS 81); ③ "uzamsal sıçramalar" kurgunun S16↔S17 sırasını
> bozmasından (MANTIK ile kesişen bulgu, birleştirmede teke indi).
> Pasaportun bible karşılaştırması ise üç gerçek üretim ihlali çıkardı:
> sırt ünitesi (D79 ×3) · çift lamba · sağ uylukta tüp (bible: SOL).
> → cevaplar: [`01_FILM_RAPORLARI/THE_BLIND_RETURN.md`](01_FILM_RAPORLARI/THE_BLIND_RETURN.md)

> 🚨 **Üçüncü koşu (06.08.2026 · THE STARLESS CIRCLE) iki şeyi kanıtladı.**
> ① **Klon sıcak noktası üçüncü kez tuttu** — bu kez planın kendi eklediği
> S14 BİNİŞ sahnesinde ("yedi basamak"), yani DERS 69'un ① maddesinin
> yasakladığı sahne tipinde; ders yazıldıktan bir gün sonra plana girmişti
> → **DERS 77.** ② **Pasaportun belgeyle karşılaştırması üç ek bulgu verdi**
> (mod V bilemezdi, ikisi Unbroken City'nin birebir tekrarı):
> sırt yaşam destek ünitesi (bible: "No back-mounted tank, no hose, no
> cable") · sabit yıpranma izlerinin üretilmemesi · **pasaportta güç
> hücresinin ve boş kalça yuvasının hiç geçmemesi** — filmin BEDELİ tam
> olarak odur (S0-S8 takılı, S10-S14 "cradle EMPTY, clamp standing open").
> Karakter merceği 14 sahne boyunca kalçaya bakmadı çünkü orada bakılacak
> bir şey üretilmemişti → **DERS 78** (bedel nesnesi siluet testi) ve
> **DERS 79** (bible'ın olumsuz kilidi çekirdeğe girmedikçe tutmuyor).
> → cevaplar: [`01_FILM_RAPORLARI/THE_STARLESS_CIRCLE.md`](01_FILM_RAPORLARI/THE_STARLESS_CIRCLE.md)

> 🚨 **İlk koşunun ana dersi: kimlik tutuyor, SAYI tutmuyor.** Yüz 8, ses 8,
> beden 9 — AI'ın "aynı insan" sözleşmesi bu filmde büyük ölçüde yerinde.
> Kırılma tek yerden geldi: araçtan İNİŞ segmentinde ikinci kopya (planın
> önceden işaretlediği klon sıcak noktası) → **DERS 69.** Verdict kuralı
> çalıştı: 7 kategori temizken tek kopya filmi IDENTITY BREAK yaptı — bu
> tablonun genel skoru tek başına okunmaz, verdict'le birlikte okunur.
>
> ⚠️ İlk koşuda bir de **rubrik uyum notu:** rapor `FILM:` alanına başlık
> kartından okuduğu adı yazdı — DERS 65 kuralının ihlali. Bulgular
> etkilenmedi; çalıştırma kaydına işlendi (rubrik dipnotu).

---

## 📥 SATIR EKLEME KURALI

```
1. KARAKTER QA çalıştırılır — YALNIZ VİDEO verilir, doküman VERİLMEZ
2. Rapor header'ında "BASELINE: SELF-CONSISTENCY" var mı kontrol et
3. Ham çıktı 02_HAM_RAPORLAR/<FILM>_KARAKTER_HAM.md olarak kaydedilir
4. Satır bu tabloya yapıştırılır — IDENTITY BREAK verdicti satıra yazılır
5. ⭐ FLAGS FOR DOCUMENT CHECK soruları bible/plan dosyasından cevaplanır,
   cevaplar 01_FILM_RAPORLARI/<FILM>.md içine yazılır
6. MANTIK_QA aynı filme koşulduysa kesişen bulgular birleştirmede teke iner
7. OUT-OF-SCOPE FLAGS satırları ilgili merceğin kaydına taşınır
```

---

## 🔗 İLGİLİ

| Dosya | İçerik |
|---|---|
| `00_INDEX.md` | film başına QA kapsamı |
| `04_MANTIK_KALITE_TABLOSU.md` | dünya tarafı — kesişimin öbür yakası |
| `../LESSONS_LEARNED.md` | teknik skorlar + dersler (69 bu rubriğin ilk koşusundan çıktı) |
