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
1. MERCEĞİN RUBRİĞİNİ AÇ:  _KAYNAK/<n>_<MERCEK>_QA_CRITIQUE_PROMPT.md
2. Filmin `<FILM>_QA_SPEC.md`'sini rubriğin BAŞINA yapıştır, sonra rubriğin
   TAMAMINI kopyala + medyayı (video/kurgu) yükle. Koşu ancak SPEC bu
   mesajın içindeyse MOD D'dir [D129].
   ⛔ 11.09.2026: filme özel PAKET kaldırıldı (`FILME_OZEL/` +
     `rubrik_paketle.sh` silindi) — SPEC'i yapıştırmak artık OPERATÖRÜN
     işidir, betiğin değil.
3. Gelen raporu asla doğrudan tabloya işleme —
   aşağıdaki 🤖 AJAN KULLANIMI bölümündeki karta göre işle

⛔ ÇIPLAK RUBRİK YAPIŞTIRILMAZ [D129 · 13 film · son vaka 04.09.2026]
   `_KAYNAK/` altındaki 1-8 numaralı dosyalar BETİĞİN girdisidir,
   operatörün değil. Elle yapıştırılırsa koşu MOD V olur ve mod V
   koşusu T tablolarına GİREMEZ — yedi mercek koşulur, yedisi de düşer.
   Bu, deponun en büyük tekrar sayacıdır; sebebi bilgi eksikliği değil,
   yanlış dosyanın doğru dosyadan kolay olmasıydı (düzeltildi 04.09.2026).

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
- film-özel sayı/kural → filmin kendi `<FILM>_QA_SPEC.md`'si
  (filme özel rubrik YAZILMAZ — 11.09.2026 kararı)
- skor, bulgu, rapor özeti → `../FILM_QA_RAPORLARI/`

> ⭐ **14.09.2026 — MODEL SAYMAZ, BETİK SAYAR (QA çıktı reformu FAZ 1).** 13 rubrikten
> `SEVERITY TALLY`, `ARITHMETIC GATE` (SCORED / SUM / DIVISION) ve `OVERALL SCORE`
> çıkarıldı: model yalnız SCORES SUMMARY hücrelerini (sayı · `—` · N/A), 🔴🟠🟡 etiketli
> timecode'lu bulguları ve tablonun altına **kapalı listeden tek VERDICT** yazar;
> `rapor_kontrol.py` etiketleri sayar, ortalamayı hücrelerden hesaplar, hükmü listeyle
> kıyaslar (①.13). Ölçüm: 241 raporun 99'unda modelin kendi sayımı yazdığı etiketlere
> uymuyordu, 16 raporda hiçbir hücre kümesinin üretemeyeceği bir toplam vardı — hepsi
> "geçersizlik" sayılıyordu. "no in-scope source" kuralı 13 rubrikte tek: hücre `—`,
> ortalamaya girmez (⑦-⑫'deki "keeps 10/10" kalktı; ⑦'nin 8,3 ortalamasının kaynağı
> buydu). Çıkarılan metin `ARSIV_CIKTI_KURALLARI.md` §14.09'da.

Ders yamaları rubrik gövdesine **yalnız İngilizce kural olarak** girer —
numarasız, tarihsiz, film adsız (17.08.2026 temizliği). Modelin göremediği
bir belgeye atıf, onun için doldurulacak bir boşluktur. Dersin hangi rubriğin
hangi bölümünde yaşadığı `CALISTIRMA_KAYITLARI.md` · **DERS → RUBRİK İZ
DEFTERİ** bölümünde tutulur; tek izlenebilirlik kaydı orasıdır.

---

## 📦 MEVCUT RUBRİKLER — 4  (22.08.2026'dan beri)

Ayrım ekseni **konu değil ZAMAN**: kusuru söylemek için kaç sahneye
bakman gerekiyor?

| Yapıştırılacak dosya (paket) | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/1_KARE_QA_CRITIQUE_PROMPT.md` | ① 🔧 KARE | "bu karede ne bozuk" | klip / montaj · yatay **veya dikey** | 11 +3 | `../FILM_QA_RAPORLARI/T1_KARE_KALITE.md` |
| `_KAYNAK/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | ② 🔗 DEVAMLILIK | "film ve insanı kendiyle çelişiyor mu" | tam kurgu | 13 | `../FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` |
| `_KAYNAK/3_SES_QA_CRITIQUE_PROMPT.md` | ③ 🔊 SES | "doğru ses doğru bedenden mi" | **TAM KURGU** | 9 | `../FILM_QA_RAPORLARI/T3_SES_KALITE.md` |
| `_KAYNAK/4_HIKAYE_QA_CRITIQUE_PROMPT.md` | ④ 📖 HİKAYE | "kimse umursar mı" | film (+ PLAN = MOD D) | 10 | `../FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` |

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

| Yapıştırılacak dosya (paket) | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md` | ⑤ 🖼️ ARKA PLAN | "çekimin KONUSU OLMAYAN alan yerinde duruyor mu" | tam kurgu · **yalnız video** | 9 | `../FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` |
| `_KAYNAK/6_FIZIK_QA_CRITIQUE_PROMPT.md` | ⑥ ⚖️ FİZİK | "dünyanın davranışı ÖLÇÜMDEN sağ çıkıyor mu" | tam kurgu (+ SAYISAL KİLİTLER = MOD D) | 9 | `../FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` |

```
⑤ ARKA PLAN   kimlik testi: bulgu, çekimin KONUSU OLMAYAN bir şeyde mi?
              Özne her sahnede yalnız DIŞLAMAK için adlandırılır. Model
              sadakat bütçesini özneye harcar; insan gözü de özneyi izler
              — altıncı parmak orta planda on izlemeden sağ çıkar. Bu
              mercek bir koşuyu tamamen özneye BAKMAMAYA harcar.
              ⛔ 07.09.2026 [D189] — ② ile SINIR NETLEŞTİ: bir sahnede
              ÖZNE olan nesne başka sahnede ARKA PLAN DEĞİLDİR. Adı olan,
              planın andığı, bir sahnenin konusu olan nesne (kapsül,
              araç, kapı) ②'nindir. ⑤'in olan ADSIZ ALANDIR: doku,
              döşeme, kalabalık yoğunluğu, kimsenin adlandırmadığı dekor.
              Sebep: bir kapsül yerleşimi DÖRT mercekte birden puan
              düşürdü (① ② ⑤ ⑨) — iki rubrik metni çelişiyordu.
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

### 🏃 AKSİYON MERCEKLERİ — 2 (01.09.2026'da açıldı)

> Fiziksel olayın İKİ ayrı ekseni. ⑥ FİZİK "sayı doğru mu" diye sorar;
> bu ikisi sayıyı hiç sormaz. ⑦ **izleyicinin olayı OKUYABİLİP okuyamadığını**
> ölçer, ⑧ **işin bedene neye mal olduğunu**. Bir dövüş aritmetik olarak
> kusursuz, okunabilirlik olarak sıfır olabilir — o bulgunun sahibi yoktu.

| Yapıştırılacak dosya (paket) | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/7_AKSIYON_QA_CRITIQUE_PROMPT.md` | ⑦ 🎯 AKSİYON | "izleyici ne olduğunu anlatabilir mi" | tam kurgu (+ A/C blokları = MOD D) | 9 | `../FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` |
| `_KAYNAK/8_EFOR_QA_CRITIQUE_PROMPT.md` | ⑧ 💪 EFOR | "iş bedene neye mal oldu, faturası ekranda mı" | tam kurgu (+ A/C blokları = MOD D) | 9 | `../FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` |

```
⑦ AKSİYON     kimlik testi: ANLATIM CÜMLESİ yazılabiliyor mu? Her beat için
              izleyicinin söyleyeceği cümle yazılır ("boot'unu payandaya
              dayar, kolu iki kez çeker, kıpırdamaz, üçüncüde eldiveni
              yırtılır"). Cümle "sanırım / galiba" olmadan bitmiyorsa beat
              OKUNMUYOR demektir. Bulgu bu cümledir.
              ⭐ En pahalı deseni ④ AKSİYON ELİZYONU: kesme hamlenin
              başında düşüp sonrasında açılır — beat hiç üretilmemiştir,
              kurgu üreticinin yapamadığını saklar. Kesme başına bakılır.
⑧ EFOR        kimlik testi: FATURA CÜMLESİ — "bu işten SONRA bu bedende ne
              değişti?" Cevap "hiçbir şey" ise bulgu odur. Yalnız çekim
              anındaki zorlanma değil, borcun BİRİKMESİ ölçülür: COST CURVE
              sahne başına bir hane, her düşüş RESET LOG'da gerekçelenir.
              ⭐ Düşük yerçekimi düşük efor DEĞİLDİR: ağırlık azalır, kütle
              ve atalet azalmaz. "0.12g'de kolay olur" mazereti bulgudur.
              ⭐ Pattern ⑭ ters hatayı da cezalandırır: sebepsiz gelen
              yorgunluk, ödenmeyen fatura kadar sahtedir.

⛔ /4 PAYDASINA GİRMEZLER — ⑤/⑥ ile aynı sınıf: risk tetikli tarama.
   ⚠️ README'nin kendi dersi burada da geçerlidir: "opsiyonel mercek
   koşulmaz". Bu ikisinin tetikleyicisi de tercih değil, filmin risk
   kartlarında ZATEN yazılı satırlardır:
     ⑦ → KART 11 (sahne içi kesme / değişken süre — elizyon riski doğrudan
         buradan doğar) · KART 4 (ikinci figür → temas) · KART 2 (canlı ile
         temas) · KART 6 (parçacık: kuvvetin dünyada cevabı) · KART 8
         (kamera aksiyonu gizliyor mu) — ya da bir çekirdek merceğin
         "ne olduğunu anlamadım" diye bıraktığı OUT-OF-SCOPE FLAG'i kovalamak
     ⑧ → KART 3 (kask / vizör / ekipman — eldiven direnci, kısıtlı baş
         dönüşü) · planın YÜK, SÜRE ya da YARALANMA kilidi taşıması ·
         ortamın bedensel bedeli olması (soğuk · ısı · ince hava · basınç)
   📌 **Dürüst açık:** "sürekli fiziksel iş / yük" için ayrılmış bir risk
   kartı YOKTUR. ⑧ bugün KART 3 ve plan kilitleri üzerinden tetiklenir;
   yeni bir kart açılırsa (KART 13 — SÜREKLİ İŞ / YÜK) tetikleyici oraya
   taşınır. Kart yokluğu tetikleyici yokluğu sayılmaz, ama yazılı kalır.

⛔ BULGU SAHİPLİĞİ: ⑤/⑥ kuralının aynısı. Çekirdek mercek her zaman sahiptir;
   ⑦/⑧ bulgusu bir çekirdek kapsamına da oturuyorsa film kaydına ÇEKİRDEK
   SAHİBİN bölümüne yazılır ("⑦/⑧ taraması buldu" notuyla). T7/T8 skoru kendi
   tablosunda durur, T1-T4 ile toplanmaz.

⛔ ⑥ İLE SINIRI — bu üçü sık karıştırılır, ayrım tek cümlelik:
     ⑥ "bu düşüş 1,1 s, öteki 2,8 s → iki yerçekimi"      → ARİTMETİK
     ⑦ "vuruşun bağlanıp bağlanmadığını göremedim"        → OKUMA
     ⑧ "80 kg'ı kaldırdı ama eli hiç sıkılmadı"           → BEDEL
   Aynı olay üçünü birden üretebilir; her mercek KENDİ türünü yazar,
   ötekinin türünü yazmaz. Çifte fatura değil, çapraz doğrulama.
```

### 🎯 PLAN SADAKATİ MERCEKLERİ — 4 (06.09.2026'da açıldı)

> Sekiz mercek THE KEPT LIGHT'ın 8 gerçek kusurunun 2'sini yazdı [D184].
> Kaçan altının üçü ÜRETİM hatasıydı ve üçünün ortak yanı şuydu: plan bir şey
> söylüyordu (kamera 0,6 m üstte · alet güverteye çarpar · S0↔S24 aynı
> kurulum), ekran başka bir şey gösteriyordu, ve HİÇBİR MERCEK PLANI EKRANA
> KARŞI OKUMUYORDU. ①②③⑤⑦⑧ planı görmez; ④ hikayeyi, ⑥ sayıyı okur. Bu dördü
> yalnız bunu yapar: planın bir satırını alır, kareye bakar, tutuyor mu der.
> Bu yüzden SPEC'siz koşuları tanım gereği BOŞTUR ve mod V satırı tablolarına
> GİRMEZ.

| Yapıştırılacak dosya (paket) | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/9_KADRAJ_QA_CRITIQUE_PROMPT.md` | ⑨ 🎯 KADRAJ | "kamera planın koyduğu yerde mi, orada kalıyor mu" | tam kurgu + B bloğu (MOD D) | 7 | `../FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` |
| `_KAYNAK/10_OYUNCULUK_QA_CRITIQUE_PROMPT.md` | ⑩ 🎭 OYUNCULUK | "istediği, seçtiği, hissettiği BEDENDE okunuyor mu" | tam kurgu + A bloğu (MOD D) | 9 | `../FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` |
| `_KAYNAK/11_ISIK_QA_CRITIQUE_PROMPT.md` | ⑪ 💡 IŞIK | "ışık klipten klibe tutuyor mu, yalnız planlı sınırda mı değişiyor" | tam kurgu + C ışık takvimi (MOD D) | 8 | `../FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` |
| `_KAYNAK/12_HOOK_QA_CRITIQUE_PROMPT.md` | ⑫ 🪝 HOOK | "filmi seçmemiş bir yabancı kalır mı, nerede gider" | tam kurgu + A/B + KAPAK ANI (MOD D) | 8 | `../FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` |

```
⑨ KADRAJ      kimlik testi: KARE ÖNCE, HARF SONRA. Her sahnede gözlenen
              boyut/açı/lens/konum yazılır, SONRA plan harfi atanır; SETUP
              STRING planın KURULUM İSKELETİ'yle yan yana konur. Kafiye çifti
              (ilk kare ↔ son kare) her filmde koşulur. ⭐ Diğer bütün mercekler
              kameranın içinden özneye bakar; bu mercek kameraya bakar. Kept
              Light S24'ün yanlış açısını sekiz merceğin hiçbiri yazmadı.
⑩ OYUNCULUK   kimlik testi: İZLEYİCİ CÜMLESİ — "bu beden ne istiyor?" — plan
              okunmadan yazılır; üç çapa vuruşta (SEÇİM · BEDEL · FİNAL)
              öncesi/sonrası karesi dondurulur, bedendeki fark bir cümledir.
              "Hiçbir şey" → vuruş ekrana ulaşmamış. ⭐ Kask kapalıysa yüz
              N/A'dır, 1/10 değil. ⑧ bedeli, ⑦ olayı, ④ sayfayı okur; kişiyi
              yalnız bu okur. "Hikayesi berbat" şikâyetinin gerçek ölçütü.
⑪ IŞIK        kimlik testi: KOMŞU ÇİFT — her kesmede "ışıkta ne değişti?"
              Aynı bölgede değişim = sıçrama; planlı sınırda değişim = PASS.
              ⭐ Ortam yasayı koyar: vakumda pus/bloom/kaldırılmış gölge
              bulgudur. Lambanın varlığı ②/⑤'in; YANIP yanmadığı bu merceğin.
              Isı/pozlama grade işi; yön/dolgu/sönük lamba yeniden üretim.
⑫ HOOK        kimlik testi: YABANCININ CÜMLESİ — açılış penceresinde SORU
              oluşuyor mu, viral ara sahne tek başına gidiyor mu, son kare ilk
              kareye mi dönüyor. Tek kalıcı çıktısı DROP-OFF PREDICTION: üç
              saniye + sabit listeden sebep → 08_YAYIN_PERFORMANS_TABLOSU'na
              kopyalanır, yayından sonra gerçek eğriyle kıyaslanır — aleti
              izleyiciye karşı kalibre eden ilk satır. ⭐ KESME ÖNERMEZ.

⛔ /4 PAYDASINA GİRMEZLER — KOŞUL tetikli. Koşullar:
     ⑨ → SPEC'te KURULUM İSKELETİ satırı (yeni-film şablonu her filmde yazar)
     ⑩ → replik 0 · ya da SPEC'te CENTRAL CHOICE satırı
     ⑪ → SPEC'te IŞIK TAKVİMİ kaydı · ya da ≥12 klipten kurulu kurgu
     ⑫ → film yayınlanacak (kart Y) — yayından ÖNCE koşulur
   Dördü de ÖLÇÜMDEN SONRA koşulur: TESLİM SINIFI 🚨 HAM ZİNCİR ise HİÇBİR
   mercek koşulmaz [D181] — kurgulanmamış dosyaya plan sadakati sorulmaz.

⛔ SAYI MODELE SORULMAZ, VERİLİR: dördünün paketine ızgara (hook + klip) ve
   iskelet SPEC'ten gömülür; rapor `CUTS OFF GRID` satırıyla ızgaraya
   UYMAYAN kesmeyi bildirir, sahneyi yeniden numaralandırmaz. Sekiz eski
   mercek 24 kesmeyi 20, 25 sahneyi 7 blok saydı — sayan model değil,
   doğrulayan model. Rubrikler ~350 satır (eskilerin 500-1.186'sına karşı).

⛔ BULGU SAHİPLİĞİ: aynı kural. Kameranın KONUMU ⑨'un · karenin İÇİ ①'in ·
   ışık ⑪'in · arkası ⑤'in · bedenin BEDELİ ⑧'in · bedenin NİYETİ ⑩'un ·
   olayın OKUNURLUĞU ⑦'nin · yabancının KALIŞI ⑫'nin · yapının kendisi ④'ün.
   T9-T12 kendi tablosunda durur, T1-T4 ile toplanmaz.

⛔ NUMARA ÇAKIŞMASI — mercek ⑨⑩⑪ ile AGENTS §3'ün kapı ⑨ HİZALAMA · ⑩ ÖNERME ·
   ⑪ ÖLÇÜM aynı rakamı taşır (①-⑧ için zaten öyleydi). Yazımda hep önek:
   "mercek ⑪" / "kapı ⑪". Öneksiz ⑪ bu depoda ÖLÇÜM KAPISI'dır.
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
                  + ⑦ ⑧    — RİSK TETİKLİ aksiyon mercekleri (kart 11/4/2/6/8 · kart 3)
                  + ⑨ ⑩ ⑪ ⑫ — KOŞUL TETİKLİ plan sadakati (yukarıdaki bölüm);
                             SPEC'siz KOŞULMAZ; ölçüm HAM ZİNCİR dediyse hiçbiri

⛔ OPSİYONEL MERCEK KALMADI. Eski sistemde karakter ve ses "opsiyonel"di
   ve bu yüzden çoğu film ölçülmeden geçti: 34 film kaydının yalnız 5'inde
   ses raporu, 10'unda karakter raporu vardı. Karakter artık ②'nin gövde
   yarısıdır ve atlanamaz.

⛔ FAZ MİMARİSİYLE YAZILMIŞ FİLM (10-20 dk hattı) — BURADAKİ MERCEKLER
   DOĞRUDAN KOŞULMAZ [D185 · 06.09.2026]:

     QA birimi FİLM değil FAZDIR. Her fazın KENDİ rubriği vardır ve fazın
     kendi kilitlerini taşır:  <FILM>/FAZ_nn_AD/FAZ_nn_QA_PROMPT.md
     (761-1.674 satır · YERÇEKİMİ'nde dokuz fazın sekizinde yazılı)

     ① Faz rubriği VARSA  → o koşulur. Buradaki mercekler onun yedeği DEĞİL,
       başka ölçekte başka bir alettir.
     ② Faz rubriği YOKSA  → önce O YAZILIR. Rubriksiz faz denetlenmez.
     ③ Yine de genel mercek koşulduysa, ④ ⑨ ⑫'nin şu kategorileri SAYI
       TAŞIMAZ (rapor_kontrol.py ①.8 basar):
          ④ Hook · Structure & Pacing · Ending · Retention Risk
          ⑫ Hook Question · Stakes · Plateau · Peak Placement · Exit
          ⑨ Rhyme Pair
       Sebep: hook filmin BAŞINDA, final SONUNDA, tutundurma eğrisi filmin
       TAMAMINDADIR. Bir orta segmentte üçü de ölçülemez.
       ⚠️ Faz ölçeğinde GEÇERLİ kalanlar sayı taşımaya devam eder: kare içi
       her şey (①), aynılık (②), ses (③), alan (⑤), sayı (⑥), okunurluk (⑦),
       bedel (⑧), kurulum sadakati (⑨'un kalanı), beden (⑩), ışık (⑪),
       kapak saniyesi ve paylaşım anları (⑫'nin kalanı).
     ⛔ Ve kesme listesi / yeniden sıralama HİÇBİR fazda uygulanmaz: fazın
       kesmesi filmin kurgusudur, faz raporunun yetkisi değildir.
     📌 Vaka: YERÇEKİMİ F8 (sekiz mercek) ve F9 (on iki mercek), 06.09.2026,
       ardışık iki fazda aynı gün.

⭐ BÖLÜM BİRİMLİ FİLM (6 dk · 36 sahne / 8 dk · 48 sahne · 13.09.2026) —
   BURADAKİ MERCEKLER KOŞULUR, AMA FİLME DEĞİL BÖLÜME [KILAVUZ_REHBERI §2.6/§2.7]:

     Film TEK master olarak kurgulanır; QA için İKİ YARIM MASTER ihraç edilir
     (6 dk: S00-S17 + S18-S35 · 8 dk: S00-S23 + S24-S47). On iki mercek her
     yarıya AYRI, temiz oturumda koşulur → 24 rapor. ⑬ UYUM bölümden etkilenmez.
     ① Rubriğin başına SPEC + tek satır beyan: "THIS FILE IS PART n OF 2 —
       scenes … — the film's ending/opening is NOT in this file." Beyansız
       koşu yarım makarayı EKSİK TESLİM sanır.
     ② rapor_kontrol.py … --bolum n/2 ZORUNLU: ①.9 yalnız BOLUM_n'i sayar,
       ①.11 uç kategorileri `—` yapar — baş bölümde ④ Ending · ⑫ Peak
       Placement · ⑫ Exit; son bölümde ④ Hook · ⑫ Hook Question · ⑫ Stakes;
       ikisinde ④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair.
       (FAZ kapısının kardeşi: faz ORTA segmenttir, bölüm UÇ segment.)
     ③ ② DEVAMLILIK bölüm sınırı çiftini göremez → SPEC B sınır satırı, elle kare.
     ⛔ Kesme listesi / yeniden sıralama bölüm raporundan UYGULANMAZ.
     ⬜ Bütün-film dörtlüsünün nasıl ölçüleceği sahip kararı bekliyor.
     Kayıt: ham `<FILM>_B1_<MERCEK>_HAM.md` · T satırı `**Film** B1` · matris `(B1)`.

3 GEÇİŞLİ SİSTEM       → UC_GECISLI_QA/ (bu klasörün altında, 04.09.2026'dan
                       beri — kapanan yatay_7_9_dk_filmler/'den taşındı).
                       ⛔ AYRI bir sistemdir: skorları yukarıdaki dört
                       merceğin tablolarıyla KARŞILAŞTIRILAMAZ. Faz
                       mimarisiyle yazılmış uzun filmler (10-20 dk hattı)
                       içindir; hangisinin koşulacağı hâlâ yazılı değil.
```

⛔ **Bir filme koşulan bütün merceklere AYNI dosya verilir.** Starless
Circle'da iki mercek 12 s'lik klibi, iki mercek 2:54'lük kurguyu ölçtü —
dört skor aynı satıra yazılamadı [DERS 75].


## 🧩 ÜRETİM SADAKATİ — ⑬ UYUM (sahne ↔ PROMPT · 11.09.2026)

> Yukarıdaki dörtlü PLANI ekrana karşı okur. Bu mercek **PROMPTU** okur: modele
> gerçekten gönderilen metni. Farkı tek cümlede: ⑨-⑫ "planda ne yazıyordu" der,
> ⑬ "o cümle promptta VAR MIYDI" der — ve kusurun sahibini söyleyen tek mercek odur.
>
> ```
> 🅐 MODEL SAPMASI  kilit promptta VARDI, ekran uymadı  → aynı promptla yeniden üret
> 🅑 PROMPT BOŞLUĞU kilit promptta HİÇ YOKTU            → aynı promptla üretmek parayı
>                                                          ikinci kez yakar
> ```
>
> ⛔ **MOD V YOKTUR.** Prompt metni girdinin kendisidir; olmadan koşu başlamaz
> (`rapor_kontrol.py` ①.11 GEÇERSİZ yazar).
> ⛔ **ÖLÇÜLEN FİLMİN PROMPTU GÜNCELLENMEZ.** Bu merceğin ürünü onarım siparişi
> değil, **SONRAKİ FİLMİN DERSİDİR**: 🅑 satırları LESSON ORDERS tablosuna, oradan
> kart G'ye, oradan yazım standardına gider.
> Makine yarısı önce koşar: `qa-isle/scripts/sahne_kapisi.sh <master> 10 <prompt_sayısı>`
> — ızgarayı ve sahne sayısını ölçer; 🚨 TESLİM UYUŞMAZLIĞI basarsa hiçbir mercek koşulmaz.

| Yapıştırılacak dosya | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/13_UYUM_QA_CRITIQUE_PROMPT.md` | ⑬ 🧩 UYUM | "ekrandaki sahne, o sahnenin PROMPTUNUN dediği şey mi — değilse kilit promptta var mıydı" | kurgu + sahne promptları (birebir) + SPEC + sahne_kapisi.sh çıktısı + üretim defteri = **MOD D** · ⛔ mod V YOK | 8 | `../FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` |

---

## 🧍🧭 HAREKET MANTIĞI VE YÖN — ⑭ HAREKET · ⑮ YÖN (14.09.2026 · sahip talebi)

> Sahibin cümlesi: *"filmlerde saçma sapan hareketler yapıyorlar, yanlış yere dönmek,
> ateş etmek vs."* Ölçüm: ① KARE'nin **Motion Quality** kategorisi 24 filmde düşüktü ve
> dersi yoktu; ⑦ olayın OKUNMASINI, ⑥ SAYIYI, ⑩ NİYETİ, ② AYNILIĞI ölçüyordu —
> "kol NEDEN kalktı" ve "vektör HEDEFE vardı mı" soruları kimsenin değildi.
>
> ```
> ⑭ HAREKET   kimlik testi: AMAÇ CÜMLESİ — "vizörü parlamadan korumak İÇİN sol kolunu
>             kaldırır". "İçin"i doldurulamayan hareket AMAÇSIZDIR. Kapalı etiket:
>             PURPOSEFUL · PURPOSELESS · LOOP · SLIDE · SPIN · PHANTOM · MISGRIP ·
>             ABANDONED · CONTRADICTION · PUPPET · DISSOCIATED · MISREACTION · OVERGESTURE
>             ⭐ PREMISE REGISTER önce: sıfır-g'de itişten sonra dönen beden hata değildir.
> ⑮ YÖN       kimlik testi: VEKTÖR CÜMLESİ — "0:01'de ekran-sağda gösterilen kapağa doğru
>             ekran-sağa döner"; cümlede "ama" varsa ISKA. Kapalı eşleşme: HIT · MISS ·
>             UNKNOWN · NO TARGET · FLIP. Hedefin yeri filmin KENDİ kurduğu yerdir (mod V
>             meşru); mod D'de SPEC C bloğunun ekran yönü kilitleriyle de kıyaslanır.
>             ⭐ Her satır EKRAN UZAYINDA (screen-left/right) — pusula kelimesi yok.
> ⭐ İKİSİNİN ÜRÜNÜ PROMPT ORDERS TABLOSU: her bulgu → sonraki filmin promptuna girecek
>   POZİTİF satır ("both boots stay planted"; "the hatch stays in the right third; he turns
>   to screen-right toward it"). Aynı etiket/desen ≥ 2 filmde → ders (kontrat §2b);
>   ders_frekans.py bu etiketleri "⬜ ⑭ / ⑮ — ders yok" satırında sayar.
> ⛔ Sınırlar tek cümle: ⑦ "ne oldu" · ⑥ "kaç saniye" · ⑩ "ne hissetti" · ② "aynı mı" ·
>   ⑨ "kamera nerede" · ⑭ "NEDEN yaptı" · ⑮ "DOĞRU YERE mi".
> ```

| Yapıştırılacak dosya | Mercek | Soru | Zorunlu girdi | Kat. | Skor tablosu |
|---|---|---|---|:--:|---|
| `_KAYNAK/14_HAREKET_QA_CRITIQUE_PROMPT.md` | ⑭ 🧍 HAREKET | "beden bunu neden yaptı — cevabı ekranda mı" | tam kurgu (+ A/C blokları = MOD D) | 8 | `../FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` |
| `_KAYNAK/15_YON_QA_CRITIQUE_PROMPT.md` | ⑮ 🧭 YÖN | "yönelmiş eylem hedefe, filmin hedefi koyduğu yere vardı mı" | tam kurgu (+ C bloğu ekran yönü kilitleri + A = MOD D) | 8 | `../FILM_QA_RAPORLARI/T15_YON_KALITE.md` |

Tetikleyici (risk tetikli sınıf, /4 paydasına girmez): ⑭ → ① Motion Quality ≤ 6 · uzun sabit
çekim · el işi yoğun sahne · sıfır-g / dönme yerçekimi · ⑦/⑩ OUT-OF-SCOPE "amaçsız hareket"
flag'i. ⑮ → sabit hedefe hareket/koşu/yanaşma (SPATIAL LOCK taşıyan film) · kovalamaca ·
ateş/atış/itki · ikinci figür · ② Spatial Geography ≤ 6. Makine çıktısı: PURPOSE STRING /
VECTOR STRING (sahne başına bir hane, uzunluk = kesme+1) — `rapor_kontrol.py` doğrular,
VERDICT'i kapalı listeyle kıyaslar (①.13).

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
| ① KARE | **C** | `02_HAM_RAPORLAR/<FILM>/<FILM>_KARE_HAM.md` | `T1_KARE_KALITE.md` |
| ② DEVAMLILIK | **E** | `02_HAM_RAPORLAR/<FILM>/<FILM>_DEVAMLILIK_HAM.md` | `T2_DEVAMLILIK_KALITE.md` |
| ③ SES | **E3** | `02_HAM_RAPORLAR/<FILM>/<FILM>_SES_HAM.md` | `T3_SES_KALITE.md` |
| ④ HİKAYE | **D** | `02_HAM_RAPORLAR/<FILM>/<FILM>_HIKAYE_HAM.md` | `T4_HIKAYE_KALITE.md` |
| ⑤ ARKA PLAN | **F** | `02_HAM_RAPORLAR/<FILM>/<FILM>_ARKA_PLAN_HAM.md` | `T5_ARKA_PLAN_KALITE.md` (matrise girmez) |
| ⑥ FİZİK | **F2** | `02_HAM_RAPORLAR/<FILM>/<FILM>_FIZIK_HAM.md` | `T6_FIZIK_KALITE.md` (matrise girmez) |
| ⑦-⑬ | **F3-F9** | `02_HAM_RAPORLAR/<FILM>/<FILM>_<MERCEK>_HAM.md` | `T7`…`T13` (matrise girmez) |
| ⑭ HAREKET · ⑮ YÖN | **F10 · F11** | `<FILM>_HAREKET_HAM.md` · `<FILM>_YON_HAM.md` | `T14_HAREKET_KALITE.md` · `T15_YON_KALITE.md` (matrise girmez · 14.09.2026) |

> 📁 **11.09.2026 — ham raporlar FİLM KLASÖRÜNDE durur:** `02_HAM_RAPORLAR/<FILM>/`.
> Dosya adı `<FILM>_<MERCEK>_HAM.md` — TEK biçim. ⛔ 12.09.2026: `_T<n>_` önekli
> (`<FILM>_T1_KARE_HAM.md` · 136 dosya), `_<n>_` önekli (THE_LEANING_ROOM · 8) ve `_MOD_x_`
> takma adlı (MOD_V=KARE · MOD_D=DEVAMLILIK · MOD_A=SES · MOD_H=HIKAYE · MOD_B=ARKA_PLAN · 14)
> dosyaların hepsi kanonik ada çevrildi, atıfları (01 kayıtları · RAPOR_KONTROL/RAPORLAR)
> güncellendi; yeni dosya bu öneklerle AÇILMAZ. Aynı merceğin tekrar koşusu depodaki
> kalıpla `<FILM>_<MERCEK>_2_HAM.md` (THE_FROST_LINE). `rapor_kontrol.py` merceği dosya
> adından değil İÇERİKTEN tanır, `sayac.sh` film adını KLASÖRDEN okur. Klasör dışına ham
> dosya konmaz.

> ⚠️ Eski ham rapor adları (`_TEKNIK_` · `_MANTIK_` · `_KARAKTER_` ·
> `_SENARYO_` · `_SHORTS_`) **değiştirilmez** — onlar arşivlenmiş
> rubriklerin çıktısıdır ve hangi aletle ölçüldükleri adlarından okunur.

> ✂️ **KESİK KOŞU (14.09.2026):** gelen metinde `SCORES SUMMARY` yoksa, skor hücresi
> yoksa ya da `MEDIA MISSING` / `INPUT MODE: MISSING` / `RUN NOT STARTED` geçiyorsa bu
> bir rapor DEĞİL, yarım koşudur (ölçüm: 336 mercek raporunun 54'ü). Ham klasöre
> `<FILM>_<MERCEK>_KESIK_HAM.md` adıyla kaydedilir — silinmez ama tabloya, ⑤ çapraz
> partisine ve `ders_frekans` sayımına girmez; aynı mercek yeniden koşulur.
> `rapor_kontrol.py` içerikten tanır (karar `KESİK`); `qa_saglik.py --ozet` sayar.

**Her kartın değişmez ilk adımları** (ayrıntı AGENTS.md §3, C/D/E ortak blok):

```
① SPEC KAPISI [D94]      planda SPEC vardı da mod V mi koşuldu? → ÖN KOŞU
② KİLİT ÇELİŞKİSİ [D96]  rapor, planda YAZILI bir kilide aykırı bulgu mu
                         veriyor? → bulgu listeden çıkar, deftere yazılır,
                         master'ın o saniyesi izlenerek çözülür
③ HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/ altına, DÜZENLEMEDEN — bu depoda
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

## 🎯 FİLME ÖZEL RUBRİKLER — ⛔ KALDIRILDI (11.09.2026)

```
`FILME_OZEL/` klasörünün TAMAMI silindi (21 girdi · 101 dosya · 6,8 MB):
  · <FILM>/PAKET_1..12 paketleri (betikle üretiliyordu)
  · THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md · THE_BLUE_DRIFT_QA_CRITIQUE_PROMPT.md
  · 00_YANLIS_POZITIF_DUVARI_SABLONU.md (filme özel rubrik yazma şablonu)
`qa-isle/scripts/rubrik_paketle.sh` de silindi.

KARAR: proje sahibi — "filme özel QA promptuna ihtiyacımız yok".
DAYANAK (deponun kendi ölçümü, D165 · 08.09.2026 "ÇALIŞMIYOR"):
  paket YOKKEN de VARKEN de operatör çıplak rubriği açtı —
  UPWARD FALL 8/8 · OPEN CIRCUIT 12/12 mercek mod V koştu.
  Paketin varlığı mod D'yi hiçbir zaman garanti etmedi.

BUNDAN SONRA: on iki mercek `_KAYNAK/` rubrikleriyle koşar; mod D'yi
taşıyan tek şey `<FILM>_QA_SPEC.md`'nin rubrikle BİRLİKTE yapıştırılmasıdır.
⛔ SPEC kaldırılmadı ve zorunluluğu aynen sürüyor.
Silinen dosyalar git geçmişinde durur; geri gerekiyorsa oradan alınır.
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
| Video — kamera kurulumu (plan lensi/mesafesi/açısı ekranda mı · lockoff · S0↔son kafiye çifti) | ✅ ⑨ KADRAJ — plan sadakati, koşul tetikli (06.09.2026) |
| Video — performans (niyet · seçim · bedel BEDENDE okunuyor mu) | ✅ ⑩ OYUNCULUK — plan sadakati (06.09.2026) |
| Video — ışık ve grade devamlılığı (anahtar yön · gölge · ısı · pratikler · bölge sınırları) | ✅ ⑪ IŞIK — plan sadakati (06.09.2026) |
| Açılış · paylaşım anları · çıkış (yayın ÖNCESİ tutundurma tahmini) | ✅ ⑫ HOOK — üç saniyelik DROP-OFF PREDICTION → 08_YAYIN_PERFORMANS_TABLOSU (06.09.2026); yayın SONRASI veri kapsam dışı kalır (aşağıda) |
| Video — hareketin MANTIĞI (amaçsız jest · döngü · kayma · sebepsiz dönüş · hayalet tutuş · kukla) | ✅ ⑭ HAREKET — risk tetikli, kapalı etiket seti + PROMPT ORDERS (14.09.2026) |
| Video — yön ve HEDEF (bakış/dönüş/gidiş/uzanma/nişan/ateş hedefe mi · 180° kırılması) | ✅ ⑮ YÖN — risk tetikli, HIT/MISS/UNKNOWN/NO TARGET/FLIP + PROMPT ORDERS (14.09.2026) |
| Video — dikey | ✅ ① KARE `FORMAT: DİKEY` + ④ HİKAYE dikey merdiveni |
| Video — 7-9 dk | ✅ 3 geçişli sistem (kendi klasöründe, ayrı skor evreni) |
| Montaj bütünlüğü (planlanan sahne ekranda var mı) | ✅ kurgu kapısı [D70/72/81] + ④ HİKAYE zirve kontrolü |
| Kapak / thumbnail | ⚠️ kısmi — ⑫ HOOK "kapak saniyesi" kategorisi filmdeki KAREYİ ölçer (06.09.2026); ayrı kapak görselinin 120 px testi elle |
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
   ⑫ HOOK bu satırı AÇMAZ: o mercek yayından ÖNCE üç saniyelik tahmin
   yazar; bu satır yayından SONRA gelen veriyi rubrikle puanlamayı
   yasaklar. İkisi aynı tabloda yan yana durur — veri tahmini kalibre
   eder, tahmin veriyi değil (06.09.2026 · D184).
```

⚠️ Bu satırları "eksik" sanıp yeniden açma — karar gerekçesiyle burada kayıtlı.

---

## 📝 DEĞİŞİKLİK KAYDI

```
14.09.2026  🧍🧭 ⑭ HAREKET + ⑮ YÖN AÇILDI — sahip talebi ("saçma sapan hareketler ·
            yanlış yere dönmek/ateş etmek"). ⑭ hareket mantığı (AMAÇ CÜMLESİ, 13
            kapalı etiket, PURPOSE STRING, 8 kategori) · ⑮ yön/hedef (VEKTÖR CÜMLESİ,
            HIT/MISS/UNKNOWN/NO TARGET/FLIP, VECTOR STRING, 8 kategori). İkisi de yeni
            çıktı sözleşmesiyle doğdu (tally/aritmetik yok, VERDICT kapalı liste
            tablonun altında) ve PROMPT ORDERS tablosu taşır (= sonraki filmin ders
            satırı). Betik: rapor_kontrol MERCEK_IMZA · MOD_D · NOVUM (premise) ·
            VERDICT_SOZLUK · dizi/sayım kapıları · t_tablo T14/T15 · qa_saglik ·
            ders_frekans "⬜ ⑭/⑮ — ders yok" · sayac rubrik globu. Kartlar AGENTS F10/F11.
            Boyut ⑭ 21,1 · ⑮ 20,6 KB. Henüz koşu yok — ilk koşu taban çizgisine eklenir.
14.09.2026  ⭐ ÇIKTI SÖZLEŞMESİ — model saymaz, betik sayar (QA çıktı reformu FAZ 1,
            TODO_QA_CIKTI_REFORMU.md). 13 rubrik + dikey ek: SEVERITY TALLY bölümü ·
            ARITHMETIC GATE · OVERALL SCORE satırları ÇIKTI; SCORES SUMMARY kuralı ⑤
            "do not total, average or tally"; "no in-scope source" → — (13'ünde tek
            kural; ⑦-⑫ "keeps 10/10" kalktı); VERDICT kapalı listesi tablonun ALTINA
            taşındı (başlıktan çıktı); tracking row son hücresi —. Betik: rapor_kontrol
            ①.13 HÜKÜM kapısı (VERDICT_SOZLUK tek kaynak) · ✂️ KESİK kararı (FAZ 0) ·
            govde_al künye düzeltmesi (mod "?" sahte bulgusu kapandı). Boyutlar:
            ① 25,5 · ④ 24,6 · ⑦ 22,8 · ⑧ 21,9 · ③ 20,2 · ② 20,0 · ⑥ 19,6 · ⑤ 17,0 ·
            ⑬ 15,6 · ⑨ 14,9 · ⑩ 14,6 · ⑪ 13,8 · ⑫ 13,7 KB (13/13 ≤ 25). Çıkarılan
            metin ARSIV_CIKTI_KURALLARI.md. ⚠️ Modelin uyumu depoda ölçülemez —
            sonraki 3 filmde qa_saglik.py --ozet (taban: CALISTIRMA_KAYITLARI 📉).
14.09.2026  ⭐ RUBRİK DİYETİ — ①-⑥ altı rubrik 25 KB tavanına indirildi (sahip kararı,
            reform FAZ 5): ① 59→25 KB · ② 37→19 · ③ 39→19 · ④ 48→24 · ⑤ 29→16 · ⑥ 32→19.
            Kategori adları/sırası, SCORES SUMMARY, başlık alanları, tracking row ve
            betiğin okuduğu her satır DONDURULDU (rapor_kontrol 13/13 mercek tanıyor);
            kesilen: tekrarlayan ⛔ kalıp paragraflar (tek satıra), anekdotlar, yinelenen
            SPECIFIC CHECK açıklamaları. Uzun hâller ARSIV_CIKTI_KURALLARI.md (ortak
            kalıp) + ARSIV_RUBRIK_DIYETI/ (altı rubriğin diyet-öncesi TAM kopyası).
            ① KARE'nin VERTICAL RULES A-D + kategori 12-14 metni _KAYNAK/1_KARE_DIKEY_EK.md
            oldu: DİKEY filmde rubriğin SONUNA yapıştırılır, yatayda yapıştırılmaz.
            Kart G adım 5: ders rubriğe yalnız ölçülebilir TEK SATIR olarak girer.
            İlk diyet-sonrası koşu T tablosunda 'diyet sonrası' işaretiyle kaydedilir.
13.09.2026  ⭐ BÖLÜM BİRİMLİ QA — 6 dk (36 sahne) ve 8 dk (48 sahne) hattı açıldı
            (sahip kararı · Kart H). Yazım 3-5 dk ile birebir aynı; TEK FARK on iki
            merceğin filme değil iki YARIM MASTERA ayrı koşulması (24 rapor).
            Kapı: rapor_kontrol.py --bolum n/m — ①.9 teslim kapısı yalnız BOLUM_n'i
            sayar, ①.11 BÖLÜM KAPISI uç kategorileri `—` yapar (D185'in yarım-film
            uzantısı: faz ORTA segment, bölüm UÇ segment). t_tablo `**Film** B1/B2`
            satırı. Sıfır filmle açıldı; maske ilk 6/8 dk koşusuyla sınanır.
            Tarif: yatay_6_dk_filmler/README.md · KILAVUZ_REHBERI §2.6/§2.7.

11.09.2026  🧩 ⑬ UYUM AÇILDI — SAHNE ↔ PROMPT (üretim sadakati sınıfı)
            Depoda dört kıyastan üçü koşuluyordu: plan↔prompt (prompt_kontrol),
            plan↔film (⑨-⑫), film↔film (①-⑧). Dördüncüsü — PROMPT↔KLİP — hiç
            koşulmuyordu ve bu yüzden hiçbir rapor kusurun SAHİBİNİ söyleyemiyordu.
            ⑬ onu sorar: kilit promptta mı yoktu (🅑), model mi uymadı (🅐)?
            ⛔ ÜRÜNÜ DERSTİR: ölçülen filmin promptu asla güncellenmez; 🅑 bulguları
            LESSON ORDERS olarak SONRAKİ filmin yazım standardına gider.
            Makine yarısı: qa-isle/scripts/sahne_kapisi.sh (ızgara · sahne sahne).
            Emsal: 18.08.2026 THE BLUE DRIFT tek-klip üretim kapısı (git geçmişinde).

11.09.2026  ⛔ FILME_OZEL/ KAPATILDI VE SİLİNDİ — proje sahibi kararı.
            21 girdi · 101 dosya · 6,8 MB; `rubrik_paketle.sh` de silindi.
            Filme özel QA promptu artık YAZILMIYOR: on iki mercek `_KAYNAK/`
            rubrikleriyle koşar ve MOD D'yi taşıyan tek şey operatörün
            `<FILM>_QA_SPEC.md`'yi rubriğin BAŞINA yapıştırmasıdır [D129].
            Dayanak D165'in kendi ölçümüdür (08.09 'ÇALIŞMIYOR'): paket VARKEN
            de OPEN CIRCUIT 12/12 ve UPWARD FALL 8/8 mercek mod V koştu —
            paket hiçbir zaman mod D'yi garanti etmedi. SPEC zorunluluğu SÜRÜYOR.

06.09.2026  ⛔ FAZ SATIRI — "hangi filme hangi mercekler"e FAZ mimarisi girdi
            [D185]. 10-20 dk hattında QA birimi FAZDIR ve her fazın kendi
            rubriği vardır; buradaki mercekler onun yedeği değildir. Rubriksiz
            faz denetlenmez. Genel mercek yine de koşulursa ④/⑨/⑫'nin film
            ölçekli dokuz kategorisi sayı taşımaz (rapor_kontrol ①.8) ve
            kesme listesi hiçbir fazda uygulanmaz.
            Vaka: YERÇEKİMİ F8 + F9, ardışık iki faz, aynı gün.

07.09.2026  🚨 TESLİM KAPISI — RAPORLAR BİRBİRİNİ DOĞRULAR, TESLİMİ DOĞRULAMAZ [D188]
            YERÇEKİMİ F10: plan 12 sahne, raporlar 11 klip — ve eksik olan,
            içerik eşlemesine göre FİLMİN SON KARESİ (S120 HELD FRAME).
            ON İKİ MERCEĞİN ON İKİSİ ayrışmayı oybirliğiyle onayladı.
            ⛔ Kapı hüküm vermez, ŞIKLARI AYIRIR: (a) eksik teslim mi
            (b) toplu sayım hatası mı — hakem ÖLÇÜMDÜR (`--olcum-sahne`).
            THE KEPT LIGHT'ta aynı kapı ateşledi ve orada şık (b) çıktı:
            plan 25, raporlar 20, ölçüm 25 — teslim tamdı.
            Hepsi aynı makarayı izliyor;
            mod V'de "eksik" demek yasak; ④'ün son-sahne kapısı MODE D ONLY.
            ⑤ ÇAPRAZ SAYIM KAPISININ KÖR NOKTASI: mutabakat ne kadar güçlüyse
            kayıt o kadar ikna edici görünür. Parti dışındaki tek referans
            PLANDIR → rapor_kontrol.py ①.9: plandaki `## 🎬 SAHNE n`
            başlıkları ↔ raporların çoğunluk sahne sayısı. Fark = parti
            GEÇERSİZ, kesme listesi UYGULANMAZ.
            ⭐ Aynı partide ⑤ ile ②'nin kapsam ÇAKIŞMASI da kapatıldı [D189]
            ve D110'a ilk betik kapısı takıldı (⑦ ORTAK DEFTER).

06.09.2026  🎯 PLAN SADAKATİ SINIFI AÇILDI — ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK
            Sekiz mercek THE KEPT LIGHT'ın 8 gerçek kusurunun 2'sini yazdı; kaçan
            üç üretim hatasının ortak yanı "plan X dedi, ekran Y gösterdi, planı
            ekrana karşı okuyan mercek yok"tu [D184]. Dört KOŞUL TETİKLİ mercek;
            dördü de MOD D'ye bağlı (SPEC'siz koşusu boş), ızgara/iskelet pakete
            gömülür (sayı sorulmaz, verilir), her biri ~350 satır. Skor tabloları
            T9-T12 açıldı; rapor_kontrol.py SETUP/GAZE/KEY DIRECTION STRING
            uzunluğunu, ⑨'da plan iskeletiyle farkı, ⑫'de üç saniyelik tahmini
            sayar. Görev kartları: AGENTS.md F5-F8. Tutanak: CALISTIRMA_KAYITLARI.md

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
