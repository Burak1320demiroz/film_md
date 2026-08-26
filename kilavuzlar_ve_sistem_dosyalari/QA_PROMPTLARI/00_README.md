# 🔍 QA PROMPTLARI — RUBRİK KLASÖRÜ REHBERİ

> **Üç dosya türü, üç ayrı ev:**
>
> | Ne | Nerede |
> |---|---|
> | Rubrik (girdi — filmi eleştiren prompt) | **bu klasör** · `*_CRITIQUE_PROMPT.md` |
> | Rapor (çıktı — skorlar, bulgular) | `../FILM_QA_RAPORLARI/` |
> | Çalıştırma kayıtları + operatör dipnotları | `CALISTIRMA_KAYITLARI.md` (bu klasörde) |

---

## ⭐ SALT PROMPT İLKESİ (12.08.2026)

**Her rubrik dosyası yalnız prompt içerir.** Dışarıdaki herhangi bir modele
**medya + tek .md dosyası** verirsin, başka hiçbir şey vermezsin; rapor gelir.

```
ÇALIŞTIRMA TARİFİ — üç adım:
1. Aşağıdaki tablodan doğru rubriği seç
2. Rubrik dosyasının TAMAMINI kopyala + medyayı (video/kurgu) yükle
   · filmin planında 📋 QA SPEC BLOĞU varsa (2-4 dk dosyalarında §0.15):
     KES, rubriğin SPEC/SCENE SPECIFICATION alanına YAPIŞTIR → MOD D
   · SPEC yapıştırmadıysan koşu MOD V'dir ve bunun bedeli vardır [DERS 94]
3. Gelen raporu asla doğrudan tabloya işleme —
   aşağıdaki 🤖 AJAN KULLANIMI bölümündeki karta göre işle

⛔ HER MERCEK TEMİZ OTURUMDA KOŞULUR [DERS 110]
   Yeni sohbet · yalnız medya + tek rubrik. Aynı oturumda ikinci bir
   rubrik çalıştırma: mercekler birbirinin sahne haritasını, zaman
   kodlarını ve severity sayımını devralıyor. O zaman "dört mercek aynı
   şeyi gördü" bir doğrulama değil, tek raporun dört kopyasıdır.

⛔ ÖNCE KURGU KAPISI, SONRA QA [DERS 109 + 101]
   Kapı ÜÇ BİRİM sayar (21.08.2026 — Last Shift vakasıyla düzeltildi):
   klip = plan CLIP COUNT · çekim = SHOT COUNT · sahne = SCENE COUNT
   (üçü eşitse tek satır yeter; eşit değilse ÜÇÜ DE ölçülür) ve
   süre = plan RUNTIME ±2 s. Tutmuyorsa koşu ÖN KOŞU'dur; film boyuna
   bakan kategoriler puan taşımaz. Kapının tam listesi:
   ../KURGU_VE_TESLIM_KILAVUZU.md
```

Bu yüzden rubrik dosyalarına ŞUNLAR YAZILMAZ:
- Türkçe operatör notu, tarihçe, çalıştırma kaydı → `CALISTIRMA_KAYITLARI.md`
- `[DERS n]` / `[LESSON n]` etiketi, tarih, film adı, koşu anlatısı,
  depo yolu (`../LESSONS_LEARNED.md` vb.) → aynı dosya, iz defteri bölümü
- film-özel sayı/kural → `FILME_OZEL/<FILM>_QA_CRITIQUE_PROMPT.md`
- skor, bulgu, rapor özeti → `../FILM_QA_RAPORLARI/`

Ders yamaları rubrik gövdesine **yalnız İngilizce kural olarak** girer —
numarasız, tarihsiz, film adsız (17.08.2026 temizliği). Modelin göremediği
bir belgeye atıf, onun için doldurulacak bir boşluktur. Dersin hangi rubriğin
hangi bölümünde yaşadığı `CALISTIRMA_KAYITLARI.md` · **DERS → RUBRİK İZ
DEFTERİ** bölümünde tutulur; tek izlenebilirlik kaydı orasıdır.

---

## 📦 MEVCUT RUBRİKLER — 4  (22.08.2026'dan beri)

Ayrım ekseni **konu değil ZAMAN**: kusuru söylemek için kaç sahneye
bakman gerekiyor?

| Dosya | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `1_KARE_QA_CRITIQUE_PROMPT.md` | ① 🔧 KARE | "bu karede ne bozuk" | klip / montaj · yatay **veya dikey** | 11 +3 | `../FILM_QA_RAPORLARI/T1_KARE_KALITE.md` |
| `2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | ② 🔗 DEVAMLILIK | "film ve insanı kendiyle çelişiyor mu" | tam kurgu | 13 | `../FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` |
| `3_SES_QA_CRITIQUE_PROMPT.md` | ③ 🔊 SES | "doğru ses doğru bedenden mi" | **TAM KURGU** | 9 | `../FILM_QA_RAPORLARI/T3_SES_KALITE.md` |
| `4_HIKAYE_QA_CRITIQUE_PROMPT.md` | ④ 📖 HİKAYE | "kimse umursar mı" | film (+ PLAN = MOD D) | 10 | `../FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` |

**Dördü de kendi kendine yeter** — tek dosya + medya, başka hiçbir şey.

```
① KARE        tek KAREden söylenebilen her kusur. Tek klibe koşulabilir.
② DEVAMLILIK  söylemek için İKİ SAHNE gerekenler. Gövde 1-6, dünya 7-13.
③ SES         film boyu, ses ekseni. Yalnız tam kurgu.
④ HİKAYE      film boyu, anlatı ekseni.
```

### 🔬 DERİN TARAMA MERCEKLERİ — 2 (24.08.2026'da açıldı)

> Zaman eksenine oturmayan iki KONU merceği. ⑤ zaman ekseninin ikisini
> birden tarar (kadraj içi VE sahneler arası) ama yalnız ÖZNE-DIŞI alanda;
> ⑥ her yerde, ama yalnız SAYI taşıyan bulgularda. Bu yüzden ①-④'ün
> yanına beşinci/altıncı zorunlu mercek olarak DEĞİL, ayrı bir sınıf
> olarak eklendiler.

| Dosya | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md` | ⑤ 🖼️ ARKA PLAN | "çekimin KONUSU OLMAYAN alan yerinde duruyor mu" | tam kurgu · **yalnız video** | 9 | `../FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` |
| `6_FIZIK_QA_CRITIQUE_PROMPT.md` | ⑥ ⚖️ FİZİK | "dünyanın davranışı ÖLÇÜMDEN sağ çıkıyor mu" | tam kurgu (+ SAYISAL KİLİTLER = MOD D) | 9 | `../FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` |

```
⑤ ARKA PLAN   kimlik testi: bulgu, çekimin KONUSU OLMAYAN bir şeyde mi?
              Özne her sahnede yalnız DIŞLAMAK için adlandırılır. Model
              sadakat bütçesini özneye harcar; insan gözü de özneyi izler
              — altıncı parmak orta planda on izlemeden sağ çıkar. Bu
              mercek bir koşuyu tamamen özneye BAKMAMAYA harcar.
⑥ FİZİK       kimlik testi: bulgu bir ÖLÇÜM taşıyor mu ya da kırdığı
              yasayı adlandırıyor mu? ① "toz sıvı gibi akıyor" DESENİNİN
              sahibi kalır; ⑥ "aynı tür düşüş bir sahnede 1.1 s, diğerinde
              2.8 s — iki ayrı yerçekimi" ARİTMETİĞİNİN sahibi.
              ⭐ MOD D bu merceğin varlık sebebi: planların sayısal kilit
              satırları NUMERIC LOCK LIST'e kopyalanır ve tek tek ekranda
              doğrulanır (PASS/FAIL/UNMEASURABLE/NOT EXERCISED). Depoda
              yazılmış kilitleri üretilmiş videoya karşı doğrulayan ilk
              alet budur.
              ⭐ ÖNERME KAPISI rubriğin içinde YAPISALDIR (STEP 0 PREMISE
              GATE): filmin dünya kuralı ilan ettiği imkânsız fizik bulgu
              değildir, yalnız TUTARLILIĞI puanlanır.

⛔ /4 PAYDASINA GİRMEZLER — tamlık matrisi dört zorunlu mercekle kalır.
   22.08 konsolidasyonu (6→4) geri alınmıyor: bu ikisi zorunlu tur değil,
   RİSK TETİKLİ tarama. Ne zaman koşulur:
     ⑤ → kalabalık / ikinci figür riski (kart 4) · katmanlı dünya (6b) ·
         yoğun set — ya da bir çekirdek merceğin arka alana bıraktığı
         OUT-OF-SCOPE FLAG'i kovalamak için
     ⑥ → novum bir fizik iddiasıysa · plan sayısal kilit taşıyorsa (mod D)
         · parçacık riski (kart 6) — ya da fizik kokan bir OUT-OF-SCOPE
         FLAG'i kovalamak için
   ⚠️ Eski sistemin ölçülmüş dersi: "opsiyonel" mercek koşulmaz (34 kaydın
   5'inde ses vardı). Bu ikisinin farkı: tetikleyicisi belirsiz bir tercih
   değil, filmin risk kartlarında ZATEN yazılı olan satırlardır — riski
   yazılı filme taramayı koşmamak, kartı okumamış olmaktır.

⛔ BULGU SAHİPLİĞİ (D108'in derin tarama eki): çekirdek mercek her zaman
   sahiptir. ⑤/⑥ bulgusu bir çekirdek kapsamına da oturuyorsa film kaydına
   ÇEKİRDEK SAHİBİN bölümüne yazılır ("⑤/⑥ taraması buldu" notuyla); T5/T6
   skoru kendi tablosunda ayrıca durur ve T1-T4 ile toplanmaz/karşılaştırılmaz.
   İki mercek aynı olayı gördüyse film kaydında TEK satır, iki kaynak —
   çifte fatura değil çapraz doğrulama.
```

### ⛔ DİKEY ARTIK AYRI BİR RUBRİK DEĞİL

Eski `SHORTS_QA` 16 kategori taşıyordu ve **13'ü başka bir rubriğin
aynısıydı** (1-8 birebir VIDEO_QA, 12 negatif, 13 mantık, 14-15 senaryo,
16 ses). Gerçekten özgün olan üçü — 9:16 kadraj · güvenli alan · kanca
zamanlaması — hepsi KARE düzeyi ölçümdür, yani tek kareden okunur.

Bu yüzden dikey hat artık bir **FORMAT ANAHTARI**:

```
① KARE      FORMAT: DİKEY → kategori 12-14 açılır (9:16 · güvenli alan · kanca)
④ HİKAYE    FORMAT: DİKEY → kanca ZAMANLAMA YASASI + saniye ölçekli
                            tutundurma merdiveni devreye girer
② ③         format farkı yok — devamlılık ve ses iki yönde de aynı şeydir
```

Dikey bir filme de aynı dört mercek koşulur; rubrik aspect'i **dosyadan
ölçer**, başlıktan veya operatörün sözünden almaz.

### Hangi filme hangi mercekler?

```
HER FİLM — yatay ve dikey fark etmez:

  TEK KLİP        ① KARE                      (diğer üçü iki sahne ister)
  TAM KURGU       ① KARE + ② DEVAMLILIK + ④ HİKAYE   ← üç zorunlu
                  + ③ SES  — kurguda ses varsa ZORUNLU, sessizse STEP 0
                             kapısı zaten N/A verir
                  + ⑤ ⑥    — RİSK TETİKLİ derin tarama (yukarıdaki bölüm);
                             /4 paydasına girmezler

⛔ OPSİYONEL MERCEK KALMADI. Eski sistemde karakter ve ses "opsiyonel"di
   ve bu yüzden çoğu film ölçülmeden geçti: 34 film kaydının yalnız 5'inde
   ses raporu, 10'unda karakter raporu vardı. Karakter artık ②'nin gövde
   yarısıdır ve atlanamaz.

7-9 dk                 BU KLASÖR DEĞİL → yatay_7_9_dk_filmler/kilavuzlar/
                       kalite_kontrol/ (3 geçişli ayrı sistem — skorları
                       buradaki tablolarla KARŞILAŞTIRILAMAZ)
```

⛔ **Bir filme koşulan bütün merceklere AYNI dosya verilir.** Starless
Circle'da iki mercek 12 s'lik klibi, iki mercek 2:54'lük kurguyu ölçtü —
dört skor aynı satıra yazılamadı [DERS 75].

---

## ⭐ İKİ GİRDİ MODU

Her rubrik raporunun ilk satırında hangi modda çalıştığını **ilan eder**:

```
MOD D — BELGELİ      medya + operatörün plan dosyasından kopyaladığı SPEC
                     BLOĞU. Tüm kategoriler puanlanır, TASARIMA UYGUNLUK
                     ölçülür. Skor tabloya işaretsiz girer.

MOD V — SADECE VİDEO medya + rubriğin kendisi. SPEC boş. Film KENDİSİYLE ve
                     FİZİKLE ölçülür. Belge isteyen her denetim puan almaz,
                     `FLAGS FOR DOCUMENT CHECK` altında SORUYA döner.
                     Satır tabloya `Ⓥ` (+ senaryoda ⚠️ ŞARTLI) girer.
```

- MANTIK / KARAKTER / SES rubrikleri **her zaman video-only** çalışır —
  doküman verilmez, baseline'ı STEP 1'de videodan kendileri kurar.
  "Eksik sahne/replik" raporlaması bu üçünde YASAKTIR.
- ⛔ **SPEC hazırken mod V koşmak bedava değildir [DERS 94]:** koşu bir ÖN
  KOŞU sayılır — skor Ⓥ ⚠️ ŞARTLI girer, tamlık matrisinde hücre ❌ kalır,
  kesme listeleri ve REMOVE reçeteleri uygulanmaz. Bu depoda mod D hâlâ hiç
  denenmedi; SPEC'i hazırken mod V koşulan film sayısı 4.
- `INPUT MISSING` hiçbir rubrikte geçerli çıktı değildir. Yaşayan üç
  durdurucu: `SPEC MISMATCH` (yalnız mod D) · `MEDIA MISSING` (oynatılabilir
  video yok [DERS 80]) · `AUDIO ABSENT` (yalnız ③ SES STEP 0).

---

## 🤖 AJAN KULLANIMI — rapor geldiğinde ne yapılır

> Rubriği çalıştırmak işin yarısı; **raporu işlemek ayrı bir disiplindir.**
> Her merceğin `AGENTS.md` §3'te bir görev kartı var. Kartı açmadan tabloya
> skor yazma.

| Gelen rapor | Görev kartı | Ham rapor dosyası | Skor satırı |
|---|---|---|---|
| ① KARE | **C** | `02_HAM_RAPORLAR/<FILM>_KARE_HAM.md` | `T1_KARE_KALITE.md` |
| ② DEVAMLILIK | **E** | `<FILM>_DEVAMLILIK_HAM.md` | `T2_DEVAMLILIK_KALITE.md` |
| ③ SES | **E3** | `<FILM>_SES_HAM.md` | `T3_SES_KALITE.md` |
| ④ HİKAYE | **D** | `<FILM>_HIKAYE_HAM.md` | `T4_HIKAYE_KALITE.md` |
| ⑤ ARKA PLAN | **F** | `<FILM>_ARKA_PLAN_HAM.md` | `T5_ARKA_PLAN_KALITE.md` (matrise girmez) |
| ⑥ FİZİK | **F2** | `<FILM>_FIZIK_HAM.md` | `T6_FIZIK_KALITE.md` (matrise girmez) |

> ⚠️ Eski ham rapor adları (`_TEKNIK_` · `_MANTIK_` · `_KARAKTER_` ·
> `_SENARYO_` · `_SHORTS_`) **değiştirilmez** — onlar arşivlenmiş
> rubriklerin çıktısıdır ve hangi aletle ölçüldükleri adlarından okunur.

**Her kartın değişmez ilk adımları** (ayrıntı AGENTS.md §3, C/D/E ortak blok):

```
① SPEC KAPISI [D94]      planda SPEC vardı da mod V mi koşuldu? → ÖN KOŞU
② KİLİT ÇELİŞKİSİ [D96]  rapor, planda YAZILI bir kilide aykırı bulgu mu
                         veriyor? → bulgu listeden çıkar, deftere yazılır,
                         master'ın o saniyesi izlenerek çözülür
③ HAM RAPORU KAYDET      02_HAM_RAPORLAR/ altına, DÜZENLEMEDEN — bu depoda
                         11 filmin ham raporu bir kez kayboldu (kural ④)
④ FLAGS'İ CEVAPLA        FLAGS FOR DOCUMENT CHECK soruları plan/bible
                         dosyasından cevaplanır, cevap film kaydına yazılır —
                         video-only rubriklerin İKİNCİ YARISI budur
⑤ REÇETEYİ GREP'LE [D85] her REMOVE/REPLACE önerisi uygulanmadan önce:
                         grep -rn "<tam dize>" <film klasörü>/
                         boş çıkarsa veya dize yasağın içindeyse reçete DÜŞER
⑥ TABLO + 00_INDEX       skor satırı + tamlık matrisi aynı oturumda güncellenir
⑦ YENİ DERS → kart G     yama ÖNCE kaynak rubriğe (İngilizce kural, gövdeye,
                         numarasız); tarih/tutanak + "D<n> → hangi rubriğin
                         hangi bölümü" satırı CALISTIRMA_KAYITLARI.md'ye
```

**Ölçüm sapmasını unutma:** aynı rubrik aynı filmi iki kez ölçtü, kategoriler
2 puana kadar oynadı. 1.5'ten küçük skor farkları GÜRÜLTÜDÜR — "A filmi
B'den iyi" deme (AGENTS §2-⑥).

**Çalıştırma kaydı nereye:** koşu bittiğinde `CALISTIRMA_KAYITLARI.md`'de
ilgili rubriğin bölümüne tek blok eklenir:
`> Çalıştırma kaydı: son <tarih> — <FİLM> (mod, geçerlilik, skor, 1-2 bulgu)`.
Rubrik dosyasına YAZILMAZ (salt prompt ilkesi).

---

## 🎯 FİLME ÖZEL RUBRİKLER — `FILME_OZEL/` (sayıma girmez)

| Dosya | Film | Neyi ölçer | Girdi |
|---|---|---|---|
| `FILME_OZEL/THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md` ⚠️ | THE RING LIGHT | aksiyon (planlı vuruş + ölü kare) ve filmin kendi sayısal kilitleri | tek klip (MOD K) veya tam kurgu (MOD F) |
| `FILME_OZEL/THE_BLUE_DRIFT_QA_CRITIQUE_PROMPT.md` | THE BLUE DRIFT | tek klibin promptuna UYGUNLUĞU + **ATIF**: kilit prompt'ta var da model mi uymadı, yoksa kilit prompt'ta hiç yok muydu | tek klip (MOD K) + AS-BUILT prompt |
| `FILME_OZEL/00_YANLIS_POZITIF_DUVARI_SABLONU.md` ⭐ 🆕 | — (ŞABLON) | **YANLIŞ-POZİTİF DUVARI ŞABLONU** — filme özel rubrik yazarken kopyalanır. Duvar depoda yalnız filme özel rubriklerde yaşıyordu; bu dosya onu yeniden kullanılabilir hâle getirir. Uzay hattına uyarlandı: klip içi lockoff · kesmesiz ızgara · yavaşlık · hareketsiz sahne · vizör arkası yüz · sessizlik · yarasızlık · metinsizlik · dar palet. ⛔ Duvar hiçbir ÖLÇÜMÜ susturmaz (kurulum envanteri · süre · kesme · replik sayımı muaftır) | film DEĞİL — kopyalanacak blok |

```
⚠️ BUNLAR MERCEK DEĞİL, ÜRETİM KAPISIDIR.
   ⚠️ RING LIGHT dosyası ortak çekirdeğe ve salt-prompt ilkesine HENÜZ
      uymuyor (Türkçe operatör kuyruğu taşıyor). Bilinen borç.
   ✅ LAST SPAN dosyası (25.08.2026) o borcu tekrarlamadan yazıldı:
      gövde tamamen İngilizce, ders numarası/tarih/film-dışı yol yok,
      ortak çekirdeğin kapıları (MEDIA GATE · CUTS COUNTED · NON-SCENE
      MATERIAL · NOT OBSERVABLE · OUT-OF-SCOPE FLAGS) yerinde.
      Türkçe yalnız BAŞLIK satırında — üç dosyada da öyle.
   · 4'lük sayıma girmezler, skorları T1-T4 tablolarına YAZILMAZ.
   · Verdikleri şey skor değil KARARDIR: KABUL / KURGUDA DÜZELT / YENİDEN ÜRET.
   · Genel merceklerin yerine geçmezler, önlerinde dururlar.

⛔ NEDEN AYRI KLASÖR: film-özel bilgi genel rubriğe ASLA girmez — SHORTS_QA
   31.07'de tam da bu yüzden sıfırdan yazıldı (eski sürüm "KULE 7" yapımına
   gömülüydü ve başka hiçbir filme uygulanamıyordu).

⭐ NE ZAMAN YAZILIR: filmin riski genel rubriklerin ölçmediği bir eksende
   yoğunlaşıyorsa (Ring Light: tasarımı gereği yavaş film — genel rubrik ya
   "durgun" diye cezalandırır ya ölü kareyi "tasarım" diye geçirir).
   ⭐ LAST SPAN aynı boşluğun daha keskin hâli: genel mercek için YÜRÜYEN
   BİR ZOMBİ HATA DEĞİLDİR — türün normalidir, geçer. Oysa o filmde tek
   kare yürüyüş premisi siler. Aynı mercek, PASİF kalabalığı "tehdit yok"
   diye cezalandırır — yani tam olarak çalışan şeyi bozmayı önerir.
   Genel alet burada iki yönde birden yanılıyor; kapı bu yüzden yazıldı.
```

---

## 🗺️ KAPSAM HARİTASI — neyi ölçüyoruz, neyi ölçmüyoruz

| Üretim aşaması | Durum |
|---|---|
| Senaryo / yapı | ✅ ④ HİKAYE |
| Görsel/video promptu (üretimden önce) | ✅ **`../PROMPT_KONTROL/`** — 12.08.2026'da açıldı: betik (sayar) + rubrik (yargılar) |
| Video — kare içi (yatay **ve** dikey) | ✅ ① KARE |
| Video — sahneler arası, dünya **ve** karakter | ✅ ② DEVAMLILIK |
| Video — özne-dışı alan (arka plan figürleri, ufuk, derinlik, kadraj kenarı) | ✅ ⑤ ARKA PLAN — derin tarama, risk tetikli (24.08.2026) |
| Video — sayısal fizik doğrulaması (plan kilitleri ekranda, görünür g, hız/ölçek aritmetiği) | ✅ ⑥ FİZİK — derin tarama, mod D kilit tablosuyla (24.08.2026) |
| Video — dikey | ✅ ① KARE `FORMAT: DİKEY` + ④ HİKAYE dikey merdiveni |
| Video — 7-9 dk | ✅ 3 geçişli sistem (kendi klasöründe, ayrı skor evreni) |
| Montaj bütünlüğü (planlanan sahne ekranda var mı) | ✅ kurgu kapısı [D70/72/81] + ④ HİKAYE zirve kontrolü |
| Kapak / thumbnail | ⚠️ **rubriksiz** — 120 px testi elle (12.08.2026'dan beri) |
| Ses tasarımı / diyalog / miks | ✅ ③ SES |
| Müzik | ⚠️ kısmi — ③ SES §9 miksteki davranışı ölçer; beste ölçülmüyor |
| Başlık & açıklama paketi | ❌ rubrik yok — yazım tarafı kılavuzlu: `../PAKETLEME_VE_VAAT_KILAVUZU.md` + `../VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` |

### ⛔ KAPSAM DIŞI — bilinçli olarak ölçülmeyecek (05.08.2026)

```
KARAKTER & DÜNYA BIBLE'I / ANAHTAR KARE     girdiyi ölçmek — ① KARE ve
   ② DEVAMLILIK zaten SONUCU ölçüyor; tutmayan Bible ekranda kostüm-prop
   çelişkisi olarak zaten görünür. Ayrıca puanlamak aynı hatayı iki
   isimle iki tabloya yazar.
YAYIN SONRASI İZLEYİCİ VERİSİ               QA değil analitik — rubrik bir
   yapıma puan verir; izlenme verisi zaman serisidir, yeri tablodur.
   22.08.2026'dan beri o tablo VAR:
   ../FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md
   (kılavuz: ../YAYIN_VE_PERFORMANS_KILAVUZU.md · AGENTS kart Y).
```

⚠️ Bu satırları "eksik" sanıp yeniden açma — karar gerekçesiyle burada kayıtlı.

---

## 📝 DEĞİŞİKLİK KAYDI

```
24.08.2026  🔬 DERİN TARAMA SINIFI AÇILDI — ⑤ ARKA PLAN + ⑥ FİZİK
            İki KONU merceği; 22.08'in ZAMAN eksenine oturmadıkları için
            ①-④'ün yanına zorunlu mercek olarak değil, /4 paydasının
            DIŞINDA risk-tetikli sınıf olarak eklendi (6→4 kararı geri
            alınmadı). ⑤ özne-dışı alanı tarar (özne yalnız dışlamak için
            adlandırılır); ⑥ tek sayısal mercek — mod D'de planın sayısal
            kilitlerini ekranda doğrular (depoda ilk), önerme kapısı
            STEP 0'da yapısal. Skor tabloları T5/T6 açıldı; bulgu
            sahipliği kuralı (çekirdek her zaman sahiptir) yukarıda.
            Görev kartları: AGENTS.md F ve F2.
            Tutanak: CALISTIRMA_KAYITLARI.md

22.08.2026  ⭐⭐ ALTI MERCEK → DÖRT. Ayrım ekseni konu değil ZAMAN oldu:
            ① KARE (sahne içi) · ② DEVAMLILIK (sahneler arası) ·
            ③ SES (film boyu · ses) · ④ HİKAYE (film boyu · anlatı).
            62 kategori yuvası → 45. Kaybolan kategori YOK, kaybolan KOPYA var.
            · SHORTS_QA dağıldı: 16 kategorisinin 13'ü zaten başka bir
              rubriğin aynısıydı; özgün üçü (9:16 · güvenli alan · kanca)
              ① içinde FORMAT ANAHTARI oldu. Dikey artık ayrı rubrik değil.
            · MANTIK + KARAKTER birleşti → ② (13 kat.: gövde 1-6, dünya 7-13).
              Sınır kuralı zaten yazılıydı ("üzerindeyse karakter, dünyaya
              aitse dünya"); birleşmede o kural YAPIYA döndü.
            · Karakter ve ses artık OPSİYONEL DEĞİL. Eskiden öyleydi ve
              bedeli ölçülebilir: 34 film kaydının yalnız 5'inde ses,
              10'unda karakter raporu vardı.
            · Altı eski rubrik → ARSIV_6_MERCEK/ (silinmedi: 83 ham rapor
              onlarla üretildi, ancak kendi metinleriyle okunabilirler).
            · Beş skor tablosu + LESSONS_LEARNED teknik tablosu DONDURULDU;
              dört yeni tablo boş açıldı (T1-T4). Eski ve yeni skorlar
              KARŞILAŞTIRILAMAZ — payda ve kategori sınırları değişti.
            · Tamlık matrisi paydası 3 → 4; ③ SES sütunu eklendi.
              ⛔ Hiçbir film henüz 4/4 değil; dört merceğin hiçbiri henüz
              hiçbir filme koşulmadı.
            Tutanak: CALISTIRMA_KAYITLARI.md

22.08.2026  ⭐ ORTAK ÇEKİRDEK — sekiz kapı altı rubrikte birebir aynı
            MEDIA GATE · CUTS COUNTED · DECLARED ABSENCE · ARITHMETIC GATE
            · SCORES SUMMARY ④ · NOT IN THIS PASS · OUT-OF-SCOPE sonuç
            bloğu · OUT-OF-SCOPE FLAGS çıktısı. Öncesinde kapılar rastgele
            dağılmıştı; en ağır ikisi: kapsam sınırı VIDEO ve SHORTS'ta HİÇ
            yoktu (11 ve 16 kategorili iki mercek başkasının kusurunu kendine
            yazabiliyordu), ARITHMETIC GATE yalnız SHORTS'taydı.
            Aynı turda üç çelişki kapandı: SENARYO'nun dokuz/on payda
            çatışması · VIDEO'da negatif ihlal SAYISININ ortalamaya girmesi ·
            VIDEO tablo satırının 11 kategoriden 7'sini taşıması (VERBATIM
            sütun kapısı eklendi, satır tamamlandı).
            Ölü `→ KAPAK_QA` işaretçileri (MANTIK · KARAKTER · RING LIGHT)
            temizlendi — o rubrik 12.08'de kaldırılmıştı.
            Tutanak: CALISTIRMA_KAYITLARI.md · ⛔ AÇIK BORÇ: LESSONS_LEARNED
            teknik tablosu hâlâ 7 sütunlu, başlığı "11 kategori" diyor.
            ⭐ Bu bir HAZIRLIK: sıradaki adım altı merceğin DÖRDE inmesi
            (① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE).

22.08.2026  Kapsam haritası işaretçileri güncellendi: yayın sonrası veri
            artık 08_YAYIN_PERFORMANS_TABLOSU + kart Y'ye işaret eder
            (KAPSAM DIŞI kararı değişmedi — QA değil analitik); başlık &
            açıklama satırına yazım kılavuzu işaretçisi eklendi (rubrik
            hâlâ yok, bilinçli).

12.08.2026  ⭐ RUBRİKLER SALT PROMPT'A İNDİRİLDİ
            Altı rubriğin sonunda biriken Türkçe ders dipnotları ve
            çalıştırma kayıtları (594 satır) CALISTIRMA_KAYITLARI.md'ye
            taşındı. İlke: rubrik .md + film = rapor; dosyada modelin işine
            yaramayan hiçbir şey durmaz. Yeni kayıtlar rubriğe değil
            CALISTIRMA_KAYITLARI.md'ye yazılır (kart G adım 5 güncellendi).

12.08.2026  🎨 KAPAK_QA_CRITIQUE_PROMPT.md KALDIRILDI
            31.07'de yazıldı, hiç çalıştırılmadı; 00_INDEX tamlık matrisi
            paydası 4→3'e indi. Kapak denetimi elle 120 px testi.
            Film dosyalarındaki işaretçiler güncellendi.

12.08.2026  Bu README sıfırdan yazıldı: salt-prompt ilkesi, çalıştırma
            tarifi, 🤖 ajan kullanım akışı (görev kartı eşlemesi) eklendi.
            Eski sürümün mod gerekçeleri ve tarihçesi korundu (aşağıda).

12.08.2026  FILME_OZEL/ klasörü açıldı — ilk dosya:
            THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md (MOD K/F, kilit alıntılama
            zorunluluğu, ACTION UPLIFT çıktısı; skoru tablolara girmez).

09.08.2026  SES_VE_DIYALOG_QA yazıldı — ses merceği. VIDEO_QA §8'in ses
            tarafını film boyuna yayar; 9 kategori; REGISTER sütunu
            (HUMAN/MACHINE/UNCLEAR — seri diegetik yapay ses kullanıyor,
            register'sız "AI gibi konuşuyor" bulgusu çalışan tasarımı bozar);
            STEP 0 ses varlık kapısı (sessiz film ≠ sesi ihraç edilmemiş
            dosya). Yalnız TAM KURGUYA koşulur. Aynı gün ilk koşu:
            Cold Burn 5.0 → 07 tablosu açıldı, DERS 82-83.

05.08.2026  KARAKTER_DEVAMLILIK_QA yazıldı — MANTIK_QA 5. kategorisinin
            karakter tarafını derinleştiren opsiyonel mercek. 8 kategori;
            kimlik kırılması ve kopya karakter = BLOCKER. İlk koşu aynı gün:
            Stone Sky 6/10 → 06 tablosu açıldı, DERS 69.

05.08.2026  ⭐ MOD D / MOD V İKİLİĞİ EKLENDİ — rubrikler tek dosya çalışır
            Tetikleyen: üç Dawn Front koşusu repo erişimi olmayan modelde
            yapıldı, üçü de rapor üretemedi (INPUT MISSING / UNVERIFIABLE /
            altı kategori kapalı; üçü de modele repoda ls/grep çalıştırmasını
            söylüyordu). → INPUT MISSING geçersiz çıktı ilan edildi; mod V'de
            rubrik baseline'ını videodan kurar; belge isteyen denetim soruya
            döner; mod V satırı Ⓥ işaretlenir. Film-özel "tek dosya paketi"
            ihtiyacı bitti.

05.08.2026  Kapsam haritasından üç satır KAPSAM DIŞI ilan edildi
            (Bible QA · anahtar kare QA · izleyici verisi — gerekçeler yukarıda).

31.07.2026  MANTIK_VE_DEVAMLILIK_QA yazıldı (yatayın üçüncü merceği), aynı
            gün yalnız-video'ya çevrildi: "eksik" raporlaması yasaklandı,
            FLAGS FOR DOCUMENT CHECK doğdu, her bulgu iki timecode taşır.
            03 ve 04 skor tabloları açıldı (hikaye ve mantık skorları teknik
            skorla aynı tabloda toplanamaz).

31.07.2026  VIDEO_QA ve SENARYO_QA'ya STEP 0 SPEC DOĞRULAMA KAPISI eklendi
            (Low Power raporu var olmayan 7 sahnelik kurguyu puanlamış ve
            filmde ZATEN VAR olan iki beati eksik diye raporlamıştı).
            SENARYO_QA'ya zirve kontrolü + format tabanı uyarısı + sessiz
            filmde Diyalog N/A + viral ara sahne kesilemez kuralları eklendi.

31.07.2026  SHORTS_QA sıfırdan yazıldı (eski sürüm "KULE 7" yapımına
            gömülüydü). Kategori 1-8 isimleri VIDEO_QA ile aynı tutuldu.
            ⚠️ Dosya aynı gün bir kez dosya sisteminden kayboldu ve geri
            yazıldı; yedeği yok.

31.07.2026  PROMPT_QA yazıldı ve bu klasörden çıkarıldı → PROMPT_KONTROL/
            (klasör hiç açılmadı — kapsam haritasında açık boşluk).
            ✅ 12.08.2026'da kapandı. Ama 31.07'de yazılan dosya
            KURTARILAMADI: 18 commit tarandı, `PROMPT_QA` geçen tek bir
            blob yok — dosya taşınırken düştü, hiç commit'lenmedi.
            Sıfırdan yazıldı. ⛔ Ders: bir dosyayı klasörden ÇIKARMADAN
            önce gideceği klasör açılır; "sonra taşırım" bu depoda bir
            kez dosya kaybettirdi (SHORTS_QA, aynı gün) ve bir kez
            dosyayı hiç var olmamış hâle getirdi (bu).
```

> Rubriklerin koşu tarihçesi, ders dipnotları ve operatör kuralları:
> **`CALISTIRMA_KAYITLARI.md`** — bu README'de tekrarlanmaz.
