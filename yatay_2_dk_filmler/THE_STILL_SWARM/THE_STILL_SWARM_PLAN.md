# 🎬 THE STILL SWARM — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur.

```
FORMAT:        yatay 2-4 dk (16:9)          [KILAVUZ_REHBERI §2.2]
ORTAM:         §3.1 VAKUM (yörünge · serbest düşüş · 0 g)
TÜR:           bilimkurgu   (tek açık dal — §4.1)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
               → plan 10,0 s VARSAYAR; ölçüm sapıyorsa QA_SPEC ızgarası yeniden hesaplanır
SAHNE SAYISI:  14  (S0–S13)      RUNTIME: 10 + 13 × 10 = 140 s = 2:20
LOGLINE:       Yörüngede donmuş bir enkaz bulutunun içinde hareket edebilmek
               için elindeki her şeyi fırlatmak zorunda kalan bir hurda
               operatörü, son fırlattığı şeyin geri geldiğini görür.
```

---

## 🎭 TEMA

```
TEMA: İLK-TEMAS
      — bu film, karşılık verildiğini anlamanın filmidir.
        (cümlede novum kelimesi geçmiyor — TEMA §9 son madde ✅)

MOTİF SAHNELERİ: S1 · S7 · S11 · S13
      TEMA §5 matrisi "İlk temas" satırının üçüncü derece indeksleri:
      ölçek uyuşmazlığı · yabancı ışık · gölgenin kendisi ·
      başın ani kalkışı + gövdenin donması (freeze)

      S1  ÖLÇEK UYUŞMAZLIĞI — 1,8 m figür ↔ 40 m kabuk; figür kadraj
          yüksekliğinin %9'u (kamera · ölçek indeksi)
      S7  YABANCI IŞIK — tek yönlü hüzme donmuş parçaların arasından
          kadrajın köşegeninde geçer; parça gölgeleri kadrajın yarısı
          kadar uzun (ışık indeksi)
      S11 GÖVDENİN DONMASI — karakter hücreyi ittikten sonra 2,0 saniye
          hiç kımıldamaz; yalnız omuz hattı 4 cm düşer (kinesik indeksi)
      S13 BAŞIN ANİ KALKIŞI + AVUÇ AÇILIŞI — nesne indeksi: geri gelen
          güç hücresi (nesne indeksi + kinesik)
```

```
⚠️ BİLİNÇLİ SAPMA — TEMA §4 SÜRE-TATMİN KURALI
   §4 "İlk Temas"ı DİKEY (anlık durum) sütununda listeler; bu film YATAY.
   SAPMA GEREKÇESİ (üç madde, hepsi ölçülebilir):
   ① §3c'nin kendi kaydı: 01.09.2026 itibarıyla hiç kullanılmamış TEK
     tema İLK TEMAS'tır ve çeşitlilik kuralı bir sonraki filmden onu ister.
   ② §4'ün cezası "SALT durum" filmine yazılmıştır ("olay örgüsüz entropi
     → seyreltilmiş uzatma"). Bu film salt durum değil: 14 sahnenin 14'ü
     kendi mini krizini taşır (UZAY_SENARYO §7 Gravity modeli), bir bedelli
     seçim ve İKİ başarısız deneme içerir [D158 B2a/B2b].
   ③ Panzehir sayısaldır: koda (merkezi seçimden sonraki sahne) = 2 sahne.
     D158'in eşiği 3-5; bu film 2'de kalır.
   ⛔ Bu sapma bir hipotezdir. Yayın verisi gelince TEMA §4 satırı ya
      doğrulanır ya bu film karşı-örnek olarak oraya yazılır.
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:   FİZİKSEL YASA (§1 birinci tercih — ihlal: momentumun korunumu)

NOVUM:        Bu bulutun içine giren her katı cisim, girdiği anda hızının
              tamamını kaybeder ve bulunduğu yerde asılı kalır. Hiçbir şeye
              çarpmaz, hiçbir şey onu tutmaz, hiçbir şey geri itmez.
              Etki-tepki hâlâ çalışır: iten geri savrulur, itilen durur.

NOVUM TAŞIYICISI:  30 cm çelik kelepçe × karakterin geriye fırlatma jesti
                   → kelepçe 2 metre gider ve mutlak durur, karakter ileri savrulur

TEK KARE (§4①):    S6 · 1:04 — fırlatılmış çelik kelepçe, karakterin
                   eldiveninden 2 metre ötede mutlak hareketsiz asılı; atış
                   kolu hâlâ uzanmış, gövdesi ters yöne kaymış. Kelepçe kadraj
                   yüksekliğinin 1/7'sini kaplar.
                   ⭐ Kare, §2'nin taşıyıcı nesnesini (çelik kelepçe) İÇERİR [D157①]
                   ⭐ Taşıyıcı kadrajın ≥1/10'unu kaplar [D157②]
                   ⭐ Değişim TEK KLİP içindedir (atış → durma → savrulma) [D157②]
                   ⭐ S6 kadrajında BAŞKA HİÇBİR ŞEY HAREKET ETMEZ [D157③]

KİNETİK BAĞIMSIZLIK (§4②):  ✅ Film 0 replik, 0 ekran metni, 0 dış ses taşır.
                   Kural yalnız üç eylemle kanıtlanır: dokun-durur (S2) ·
                   gaz ver-durur (S5) · fırlat-durur-savrul (S6).

BAŞLIK ŞEMASI (§4③):  "THE STILL SWARM" (3 kelime) — izleyiciye nereye
                   bakacağını söyler: kalabalık bir şeye, ve onun
                   hareketsizliğine. Paketlemede ikinci kez koşar.

İHLAL SAYISI (§3):  1. İkinci ihlal YOK; finaldeki çözülme birincinin
                    SONUCUDUR, ayrı bir kural değildir.
KABUK (§3):         tanıdık kalır — basınç giysisi, vizör, halat, kelepçe
                    kuşağı, hurda mekik. Yenilik yalnız ihlaldedir.

KURAL TEKRARI (§5): KURULUM   S0-S2 (bulut asılı · eldiven değer, parça durmaz)
                    DOĞRULAMA S5-S6 (gaz konisi durur · kelepçe durur)
                    SONUÇ     S10-S11 (kural karakterin bedelini belirler)
                    → 6 sahne · 4 farklı nesne (enkaz parçası · gaz · kelepçe ·
                      güç hücresi). Eşik: ≥3 sahne, ≥2 nesne ✅
                    ⛔ Bu altı sahne KURGU KAPISI'nın KESİLEMEZ listesindedir.
```

```
⛔ "UZAYLI" NASIL YAZILDI — kararın kaydı
   Kullanıcı talebi: uzaylı olsun. Depo kısıtı iki yerden geliyor:
     · KILAVUZ_REHBERI §4.1 / UZAY_SENARYO §3: "uzaylı ırklar" = uzay
       operası = ⛔ bu projede YAZILAMAZ
     · 02_RISK_KARTLARI KART 2 (canlı) 🔴 EN YÜKSEK: canlı kategorisi
       hiçbir filmde 5'i geçmedi; kartın kendi alternatifi "canlıyı
       neredeyse görünmez yaz — görünmeyen anatomi bozulmaz"
   KARAR: filmde uzaylı VARDIR ve filmin konusudur, ama ANATOMİ olarak
   hiçbir karede görünmez. Uzaylı, ekranda YAPTIĞI İŞLE vardır: enkazı
   tutan kural, ve finalde onu geri veren yön. Canlı karesi 0.
   ⛔ Prompt gövdesinde "creature", "alien", "being", "swarm" YAZILMAZ —
      film adındaki "swarm" yalnız BAŞLIKTA yaşar. Promptta karşılığı:
      "a shell of motionless fragments" / "held fragments".
      Sebep: model canlı ismini görünce anatomi çizmeye çalışır [D2 · D18].
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
⬜ UYGULANMAZ — bu film yatay 16:9. (KILAVUZ_REHBERI §2.1 dikey kartı)
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2.2)

| # | vuruş | % | sahne | not / boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | 0-5 | **S0** 0:00-0:04 | Kapanış imajıyla ÇİFT tasarlandı (§2.3-③) |
| 2 | Kurulum | 0-10 | **S0-S1** | Dünya (donmuş kabuk) + karakterin yetkinliği (halat işi) |
| 3 | Katalizör | ~10 | **S1** 0:12-0:14 | ⛔ ≤0:15 kapısı ✅ — mekiğin son konum ışığı söner |
| 4 | Tartışma | 10-25 | **S2-S3** | Meslek refleksi: dokunur, ölçer, sınırdan geçer |
| 5 | Orta nokta | ~50 | **S7** 1:10-1:20 | Sahte zafer: hedef görünür mesafede · bahis yükselir |
| 6 | Umut-önce-düşüş | kayıptan hemen önce | **S9** 1:30-1:40 | Merkeze varır, hücre elinin altında |
| 7 | Her Şeyin Kaybı | ~75 | **S10** 1:40-1:50 | SOMUT ve geri dönüşsüz: kuşak boşalır, 8 m içeride kalır |
| 8 | Final (doruk) | 85-99 | **S11-S13** | Doruk S11; kurguya girmek ZORUNDA [D62 · D72] |
| 9 | Kapanış imajı | 100 | **S13** 2:10-2:20 | Açılışın TERSİ: aynı kurulum, kural kırılmış |

```
§2.3 ÜÇ SERT KURAL
① KAMERA-TAŞIYICI TESTİ: "karakteri dronla değiştirsek ne kaybolur?"
   → Kaybolan şey filmin tamamı: bulutta ilerlemenin tek yolu bir insanın
     kendi kütlesini bölüp parça parça atmasıdır. Drone'un iticisi vardır
     ve bu bulutta iticinin işlemediğini S5 kanıtlar.
② SEÇİMİN BEDELİ NESNEDİR, CÜMLE DEĞİL: vazgeçilen şey kadrajda görünen
   60 cm'lik güç hücresidir (S11). Tema yapısaldır.
③ AÇILIŞ-KAPANIŞ ÇİFTİ: S0 kurulum A · mutlak hareketsiz kabuk.
   S13 kurulum A · aynı kabuk, tek fark: her parça harekette.
   İki imaj yan yana konduğunda değişim tek bakışta okunur ✅
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU (§4) — tanıdık sahne + TEK anormal öğe.
                 TEK tip; ikinci tip bindirilmedi.
                 ⚠️ §4'ün risk notu: "anomali türetilmiş fenomense (gölge,
                    yansıma) tek-kare fizibilite kapısı ŞART [D73]".
                    Bu filmde anomali SOMUT KATI CİSİMDİR (enkaz parçaları),
                    türetilmiş fenomen değil → o kapı tetiklenmez.

0. KARE (§2.1):  Sol üçte birde halata tutunmuş figür (kadraj yüksekliğinin
                 %9'u), sağ üçte ikide 40 m'lik donmuş enkaz kabuğu.
                 ÖRÜNTÜ KESİNTİSİ: tek güçlü fikir (dağılmayan enkaz) +
                 tek anlam ipucu (halattaki insan). İkinci fikir yok.
                 120 PX TESTİ: 120 px'e indirildiğinde okunması gereken TEK
                 şey — küçük insan silueti ↔ devasa tanecikli kabuk kontrastı.
                 ⛔ Test MAKİNEYLE koşulur (§8): kare 120 px'e indirilir,
                    kontrast/entropi ölçülür. Kapak dosyasında komut yazılı.

HAREKETİN ORTASINDA (§2.2): S0'ın ilk cümlesi süren bir eylemi tarif eder —
                 karakter halat boyunca ZATEN kayıyor; eylemin başlangıcı
                 kadraj öncesinde kalır.

S0 SORUSU:       "Neden hiçbiri hareket etmiyor?"
                 ⭐ Soru kadrajın İÇİNDE cevaplanabilir hâle getirildi:
                   aynı karede HAREKET EDEN bir şey var (karakterin kayışından
                   kopan tek toz zerresi, onunla birlikte sürükleniyor).
                   Kontrast olmadan izleyici hareketsizliği fark edemez.

3. SANİYE (§2.5): 0:03'te ekranda ilk kareden FARKLI bilgi var —
                 karakter halattan bir kelepçe çözer, kelepçe kuşağı görünür.

S1 İKİNCİ BİLGİ: Ölçek büyür ve YÖN doğar: kabuk sanıldığından derin
                 (20 m yarıçap) ve içinde, merkeze yakın, gri bir kutu var.
                 Soru DEĞİŞİR: "neden donmuş?" → "içine girmek zorunda mı?"

İLK 2 SN SESİ (§5): TEK DİEGETİK SES — kask içi nefes + halatın gövdeden
                 iletilen gerilme sesi. Müzik 0:00'da GİRMEZ; en erken
                 0:04'te (ipucu beat'i) girer. Erken müzik girişi elendi
                 (§5⑥: ölçülen en kötü seçenek).
                 Sub-bass'a 90-160 Hz oktav eşlikçisi ZORUNLU (§5④).

BİLGİ ASİMETRİSİ (§3.1):
   DRAMATİK İRONİ · taşıyıcı ① ARKA PLAN OKUR · asimetri anı 1:14 (S7)
   İzleyici tepeden görür: karakterin arkasında bıraktığı kelepçeler
   kusursuz DÜZ bir hat oluşturmuştur. Karakter ileriye bakmaktadır ve
   kask periferisi arkayı kapatır.
   KAPANIŞ: karakter S12'de öğrenir (2:00-2:10).
   SAKİNLİK KORUNUR: karakterin paniklediği kare sayısı = 0.
   ⚠️ S0-S1 BİLGİ EŞİTLİĞİ bandındadır (karakter de bilmiyor); ironi
      S7'de İKİNCİ bir olgu üstünden açılır — çözmeye çalıştığı şey değil,
      çözerken ARKASINDA bıraktığı şey.
```

---

## 🔚 FİNAL VE PAYLAŞIM  (`FINAL_VE_PAYLASIM_KILAVUZU.md` §8)

```
FİNAL TİPİ:      TERSİNE DÖNÜŞ (TWIST) + DÖNGÜ  (§2 karar kuralı: 2-4 dk →
                 TWIST veya MUĞLAK, döngü opsiyonel)
                 TWIST: kuralın kendisi kırılır — bulut çözülür ve YÖN doğar.
                 Mekânın doğası değişir: tutan bir yer değil, cevap veren biri.

AÇILIŞ SORUSU:   TEK — "Neden hiçbiri hareket etmiyor?" (§1: soru sayısı 1)
AÇIK KALAN SORU: 1 — "Ne istiyor?" (0 = kapalı final bedeli · 2+ = aldatılma)

TOHUM BİLGİ (§3): YER: S2 · 0:26-0:28 (filmin %19'u — 2-4 dk penceresi 15-22 s;
                    ⚠️ 26 s pencerenin 4 s dışında. GEREKÇE: pencere 150 s'lik
                    filme göre yazılı, bu film 140 s; ve tohumun taşıyıcısı S2'nin
                    ikinci beat'i. Sapma bilinçli ve tek satır olarak burada.)
                  SÜRE: 2,0 saniye — görünür ama anlamlandırılamaz
                  TAŞIYICI: çevrede — arka planda, odak dışında, üç enkaz
                    parçası kusursuz bir hizada duruyor. Aralarındaki mesafe eşit.
                  ⛔ Karakterin bakışıyla VURGULANMAZ (vurgu = cevap)
                  GERİ DÖNÜŞ: S12 ve S13 aynı hizaya görsel olarak döner —
                    o hiza, karakterin kendi bıraktıklarının uzantısıdır.

PAYLAŞIM SAHNESİ (§5): **HUŞU** — S11 (doruk yuvası)
                  Karakter kadraj yüksekliğinin %11'i; arkasında yüzlerce
                  donmuş parça; tek yönlü hüzme ışık. Ölçek kontrastı ≥1:10.
                  Bu plan TAM BİR KLİP (10 s), kırpılmaz.
                  ⛔ Aynı sahne KAYGI taşımaz — filmin imzası huşudur.
                  → §5 karar kuralı: paylaşım isteniyor → HUŞU + final TWIST ✅

İKİLEM (§4):      ① Karakter kadrajda görünen bir bedeli kendi eliyle ödüyor:
                     60 cm'lik güç hücresini fırlatıyor — geri dönüşünün
                     tek yakıtı odur ve onsuz mekik ölü kalır.
                  ② Karşılığında aldığı şey tartışmalı: hayatta kalmak,
                     ama işi yarım — ve verdiği şeyi VEREN bir şey var.
                  ③ Kamera yargısız: film seçimi ne onaylar ne kınar.
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` ve `KURGU_RITMI §2`
> örüntü kırıcı — ardışık iki sahne aynı ölçek + palet + ses dokusunda olamaz.

### Kurulum sözlüğü (7 kurulum · `ACI_YAYI §4` bandı: 14/2 = 7 ✅)

| kod | ölçek | açı tipi | lens | mesafe | kamera pitch | azimut* |
|---|---|---|---|---|---|---|
| **A** | EWS (1) | göz hizası | 32mm | 60 m | 0° | 90° |
| **B** | WS (2) | üst açı | 35mm | 18 m | +25° | 60° |
| **G** | MS (3) | profil | 50mm | 6 m | 0° | 115° |
| **D** | CU (4) | omuz üstü (OTS) | 75mm | 1,6 m | 0° | 15° |
| **E** | ECU (5) | göz hizası (makro) | 100mm | 0,8 m | 0° | 150° |
| **F** | EWS (1) | tepe / kuşbakışı | 24mm | 45 m | +90° | 90° |
| **H** | EWS (1) | alt açı | 32mm | 25 m | −25° | 140° |

```
* AZİMUT: eksen hattına göre. 0° = kamera karakterin ARKASINDA (mekik tarafı),
  180° = karakterin ÖNÜNDE (bulut tarafı). Kamera 14 sahnenin 14'ünde eksenin
  AYNI tarafında kalır — 180° kuralı hiç geçilmez [ACI_YAYI §3 uyarısı:
  "açı değişir, coğrafya değişmez"].

AÇI TİPİ SAYISI: 6  ≥3 ✅   (göz hizası · üst açı · profil · OTS · tepe · alt açı)
KURULUM SAYISI:  7 tasarımda · betik 8 sayıyor
  ⛔ GEREKÇE [D74 — kaydı olmayan kapı koşulmamış kapıdır]:
     Tasarımda yedi kurulum var (yukarıdaki tablo) ve bant tavanı 14/2 = 7.
     `prompt_kontrol.py` klasör modunda 8 sayıyor; fark, S13'ün image
     promptunun D153 protokolü gereği "the same frame as the approved opening
     still" cümlesiyle açılmasından gelir — betik o cümleyi ayrı bir kurulum
     imzası okuyor. Kadrajın kendisi S0 ile BİREBİR aynıdır ve zaten öyle
     olmak ZORUNDADIR: eş kadraj çifti filmin loop kararıdır.
     Yani sapma ölçüm tarafındadır, tasarım tarafında değil — ve düzeltmesi
     D153'ü bozmak olurdu. Bilinçli, tek satır, burada.
ABARTI EŞİĞİ [KAMERA_ACISI §5]: üst açı +25° (15-30 bandı ✅) ·
                 alt açı −25° (15-30 bandı ✅) · tepe +90° (ayrı açı, meşru ✅) ·
                 dutch KULLANILMADI. 45-60° ölü bölgesine giren satır YOK.
```

### Diziliş

```
A · B · G · D · E · D · G ‖ F · B · G · D · H · B · A
S0  S1  S2  S3  S4  S5  S6   S7  S8  S9  S10 S11 S12 S13
                        ‖ = BÖLÜM KESİĞİ (S6 ↔ S7)

ARDIŞIK AYNI KURULUM: 0 ✅
ŞOK BANDI (2+ ölçek kademesi): 2 ✅ — tavanı aşmıyor
   ① S6→S7  MS(3) → EWS(1)  Δ2 · pitch 90°  — ORTA NOKTA + bölüm kesiği
   ② S10→S11 CU(4) → EWS(1) Δ3 · azimut 125° + pitch 25° — DORUK,
      filmin EN YÜKSEK kontrast sıçraması [ACI_YAYI §9] ✅
DÖNGÜ KARARI: S0 ve S13 aynı kurulum (A) — bilinçli, loop satırıyla tutarlı
BÖLÜM KESİĞİ: S6 (G · MS · profil) ↔ S7 (F · EWS · tepe)
   Δ2 ölçek kademesi VE 90° pitch farkı ✅ — bölüm sınırı da ardışık bir ÇİFTTİR
```

### Harita

| S | başlık | olay | kurulum | palet | ses dokusu | bütçe / not |
|---|---|---|---|---|---|---|
| **S0** | DURAN DUVAR | Halat boyunca kayarak ilerler; sağdaki 40 m kabuk mutlak hareketsiz. Kayışından kopan tek toz zerresi onunla sürüklenir. 0:03'te kuşaktan kelepçe çözer | **A** EWS · göz hizası | P1 dış · sert yan ışık, mutlak siyah gölge | nefes + halat gerilmesi (gövdeden) | ölçek kontrastı %9 · yürüyüş/duruş · HOOK |
| **S1** | İÇERİDE BİR ŞEY VAR | Kabuğun derinliği açılır; 20 m içeride gri kutu. Mekiğin son konum ışığı 0:12'de söner. Kuşaktaki 8 kelepçe sayılabilir | **B** WS · üst açı | P1→P2 · mekik ışığı sönerken palet soğur | nefes + mekik gövde tıkırtısı, sonra sessizlik | ⭐ TEMA S1 · İSİM-İSTEK-BEDEL kapanır ≤0:15 · KATALİZÖR |
| **S2** | SINIR | Eldiven kabuğun dış parçasına değer; parça kımıldamaz, itiş karakteri geri savurur | **G** MS · profil | P2 sınır · kenar ışığı | eldiven-metal teması (gövdeden) | el bütçesi · ⭐ TOHUM 0:26-0:28 (arka planda üç hizalı parça) · NOVUM KURULUM |
| **S3** | GEÇİŞ | Kabuktan içeri geçer; geçtiği anda hızı sıfırlanır, halat gevşer | **D** CU · OTS | P2→P3 iç | halatın gevşemesi + tek nefes | ⛔ OTS → SIRT POZİTİF cümlesi ZORUNLU [D139] |
| **S4** | SAYAÇ | Kask lambası açılır. Kuşaktaki sekiz kelepçe tek tek okunur; birini çözer | **E** ECU · makro | P3a · kask lambası dar koni | toka klik + nefes | el ≥%15 · kişisel eşya ≥%5 (kuşak = mesleğin nesnesi) · göz bütçesi |
| **S5** | İŞLEMEYEN İTKİ | Göğüs tüpünü açar; gaz düz koni hâlinde 1 m gider ve DURUR. Karakter kımıldamaz | **D** CU · OTS | P3b · gaz konisi beyaz, sonra donuk | tüp valfi + gövdeden tıslama, sonra kesilir | ⭐ BAŞARISIZ DENEME #1 [D158 B2b] · NOVUM DOĞRULAMA · OTS → sırt cümlesi |
| **S6** | İLK ATIŞ | Kelepçeyi geriye fırlatır: 2 m gider, mutlak durur; karakter ileri savrulur. **8→7** | **G** MS · profil | P3a | atış hışırtısı (giysiden) + nefes | ⭐⭐ NOVUM TAŞIYICISI · TEK KARE (1:04) · ⛔ kadrajda başka hiçbir şey hareket etmez [D157③] |
| **S7** | HAT | Tepeden: karakter ilerler; ARKASINDA üç kelepçe kusursuz düz bir hat. O ileriye bakar. **7→5** | **F** EWS · tepe | P3c · hüzme köşegen, gölgeler uzun | boşluk + yavaş nefes | ⭐ TEMA S7 · ORTA NOKTA · DRAMATİK İRONİ asimetri anı 1:14 · ölçek kontrastı 1:10 · ŞOK #1 |
| **S8** | GERİLEN HALAT | Halatı çeker: gerilir, düzleşir, hiçbir şey olmaz. Sonra KOPAR — kopan uç mutlak durur, kıvrılmaz | **B** WS · üst açı | P3b | halat gerilme + kopma darbesi (gövdeden), sonra sessizlik | ⭐ BAŞARISIZ DENEME #2 · D26 halat fiziği kilidi |
| **S9** | MERKEZ | Merkeze varır. Güç hücresi elinin altında. Etrafında yüzlerce donmuş parça | **G** MS · profil | P4 merkez · hüzme daralır | yalnız nefes | umut-önce-düşüş · göz bütçesi (vizör içi aydınlatma) |
| **S10** | SIFIR | Hücreyi alır; kalan iki kelepçeyi fırlatır, 3 m ilerler ve durur. Kuşak boş. Hâlâ 8 m içeride. **2→0** | **D** CU · OTS | P4 · kask lambası kısılır | ⛔ MÜZİK TAMAMEN SUSAR — yalnız yalıtılmış nefes [KARAKTER §5.3 · D83: mutlak sıfır YOK] | HER ŞEY KAYBOLDU yuvası · el + göz · OTS → sırt cümlesi |
| **S11** | BEDEL | Hücreye bakar, sonra iki eliyle iter. Hücre 2 m gider, durur. Karakter geriye savrulur. 2,0 s hiç kımıldamaz; omuz hattı 4 cm düşer | **H** EWS · alt açı | P4→P3 · hüzme yeniden açılır | itiş + tek uzun nefes bırakma | ⭐⭐ DORUK · CENTRAL CHOICE · PAYLAŞIM SAHNESİ (HUŞU) · TEMA S11 · ŞOK #2 · ölçek 1:11 |
| **S12** | HAT GÖRÜNÜR | Kabuğun dışında mekiğe tutunur; tutunmak için kuşağı çözüp bırakır. Geriye bakar: sekiz kelepçe + hücre + kuşak, hepsi tek düz hat | **B** WS · üst açı | P2 sınır | mekik gövdesine temas + nefes | ⭐ İKİNCİ SEÇİM [D158 B2a] · karakter ÖĞRENİR · ironi kapanır · Kuleshov A′ |
| **S13** | KARŞILIK | Bulut çözülür: yüzlerce parça aynı anda, aynı hızda mekiğe doğru. En önde güç hücresi. Avucunu açar. Hücre avucuna 1 m kala kesme | **A** EWS · göz hizası | P1 dış · ilk sahnenin ışığı | tek alçalan nefes + hücrenin gövdeye yaklaşan uğultusu | ⭐ TWIST · KAPANIŞ İMAJI · TEMA S13 · LOOP |

### Örüntü kırıcı denetimi (`KURGU_RITMI §2` kapısı)

| çift | ölçek | palet | ses dokusu | sonuç |
|---|---|---|---|---|
| S0→S1 | EWS→WS ✅ | P1→P1/P2 (mekik ışığı söner) ✅ | halat→gövde tıkırtısı ✅ | geçti |
| S1→S2 | WS→MS ✅ | P2 ✅ | tıkırtı→eldiven teması ✅ | geçti |
| S2→S3 | MS→CU ✅ | P2→P3 ✅ | temas→halat gevşemesi ✅ | geçti |
| S3→S4 | CU→ECU ✅ | P3→P3a (lamba yanar) ✅ | gevşeme→toka klik ✅ | geçti |
| S4→S5 | ECU→CU ✅ | P3a→P3b ✅ | klik→valf tıslaması ✅ | geçti |
| S5→S6 | CU→MS ✅ | P3b→P3a ✅ | tıslama→atış hışırtısı ✅ | geçti |
| S6→S7 | MS→EWS ŞOK① | P3a→P3c ✅ | hışırtı→boşluk ✅ | geçti (işaretli) |
| S7→S8 | EWS→WS ✅ | P3c→P3b ✅ | boşluk→halat kopması ✅ | geçti |
| S8→S9 | WS→MS ✅ | P3b→P4 ✅ | kopma→yalnız nefes ✅ | geçti |
| S9→S10 | MS→CU ✅ | P4 (lamba kısılır) ✅ | nefes→MÜZİK SUSAR ✅ | geçti |
| S10→S11 | CU→EWS ŞOK② | P4→P3 ✅ | nefes→itiş ✅ | geçti (işaretli) |
| S11→S12 | EWS→WS ✅ | P3→P2 ✅ | itiş→mekik teması ✅ | geçti |
| S12→S13 | WS→EWS ✅ | P2→P1 ✅ | temas→uğultu ✅ | geçti |

```
MAKRO ÖRÜNTÜ KIRICI (her 3-4 sahnede mekân/tempo değişimi):
  S3 mekân değişir (dışarı → kabuğun içi) · S7 tempo değişir (tepeden,
  geniş nefes) · S9 mekân değişir (kabuk → merkez) · S12 mekân değişir
  (merkez → dışarı, mekik) ✅
```

### Kuleshov döngüleri (`KARAKTER_VE_DUYGU §2` · hedef ≥5 örtüşen döngü)

```
① S1 (A · bakış yönü yazılı) → S2 (B · baktığı parça, tam gösterilir) → S3 (A′ · omuz hattı değişir)
② S4 (A) → S5 (B · gaz konisi) → S6 (A′ · atış öncesi duruş)
③ S6 (A) → S7 (B · hat, tepeden) → S8 (A′ · halata giden el)
④ S9 (A) → S10 (B · boş kuşak) → S11 (A′ · itiş sonrası donma)
⑤ S11 (A) → S12 (B · geriye bakış, hat) → S13 (A′ · avuç açılışı)
→ 5 döngü · dönüş planı ≥2 s ✅ · tepki payı: S3·S6·S8·S11·S13 = 5/14 = %36 ≥%25 ✅
⛔ Hiçbiri POV DEĞİL — B planı aynı uzamsal mantıkta ayrı kadrajdır [KARAKTER §7]
```

### Bütçe denetimi (`KARAKTER_VE_DUYGU §6` · 2-4 dk sütunu)

| bütçe | hedef | bu filmde | sahne |
|---|---|---|---|
| 👁️ göz görünürlüğü ≥%12 | ~2 sahne | 3 sahne = %21 | S4 · S9 · S13 (vizör içi aydınlatma bloğu ZORUNLU) |
| 🔁 tepki planı ≥%25 | ~4 sahne | 5 sahne = %36 | S3 · S6 · S8 · S11 · S13 |
| ✋ el / mikro-jest ≥%15 | ~2 sahne | 3 sahne = %21 | S2 · S4 · S10 |
| 🚶 tam boy yürüyüş/duruş ≥%10 | ~2 sahne | 2 sahne = %14 | S0 · S7 |
| 🎒 kişisel eşya ≥%5 | ~1 sahne | 2 sahne = %14 | S4 · S12 (kelepçe kuşağı — S0'dan S12'ye altı sahnede görünür, tek nesne [D58]) |
| 🌌 ölçek kontrastı 1:10 | 1 sahne | 2 sahne | S7 (1:10) · S11 (1:11, ≥10 s tam klip, kırpılmaz) |
| 🔁 Kuleshov döngüsü | ≥5 | 5 | yukarıda |

### İSİM · İSTEK · BEDEL (`KARAKTER_VE_DUYGU §3` · ≤0:15)

```
İSİM (rol)  hurda/kurtarma operatörü — kostümden okunur: kelepçe kuşağı,
            omuzda halat makarası, dizlikte aşınmış kanca yuvası.  → S0 0:00
İSTEK       kadrajda GÖRÜNEN hedef: kabuğun 20 m derinindeki gri kutu
            (mekiğin yedek güç hücresi, 60 × 40 cm).                → S1 0:11
BEDEL       kadrajda GÖRÜNEN sayaç: kuşaktaki sekiz çelik kelepçe.  → S1 0:13
ORTA NOKTA  %50'de sahte zafer (hedef görünür mesafede).            → S7
⛔ Üçü de 0:15'ten önce kapanır; ekran metni 0,0 s, replik 0.
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** sabitlenir ve her IMAGE promptuna
> tam yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).

### 👤 Character Bible — kelimesi kelimesine çapa

```
A woman in her late thirties, warm medium-brown skin with visible pores and
a healed 2 cm scar along the left jaw, dark brown hair cropped close to the
scalp, brown eyes. She wears a bone-grey pressure suit with a matte, lightly
scuffed surface, a fitted collar ring, and a wide canvas tool belt across the
hips carrying short steel clamps in open loops. Her gloves are the same
bone-grey with worn dark-grey palms. The helmet visor is optically clear
glass with zero tint, zero mirror coating and zero reflection of the
environment; her face is fully readable through it in every frame, at every
head angle. The suit has no back-mounted unit: no backpack, no tank, no hose,
no cable, no rear housing of any kind — the back of the suit is one
continuous smooth panel from collar to hip, unbroken, carrying nothing.
```

```
⛔ MİLLİYET YAZILMAZ [SAHNE_DEVAMLILIK §2.1 · 01.09.2026 düzeltmesi ·
   POLİTİKA §7 DOĞRULANMIŞ red]. Çapa fiziksel tanımdır.
⛔ ÖZEL AD YAZILMAZ [D34 · D45]. Karakterin adı yoktur ve olmayacaktır.
⛔ KISALTMA YOK [D155②]: "EVA suit" / "MAV" / "PHASE n" hiçbir promptta
   geçmez. Giysi adı: "pressure suit". Kir merdiveni SPEC'in C bloğunda
   yaşar, prompt gövdesine ETİKET olarak inmez [D155①].
⛔ PROMPT GÖVDESİNDE BÜYÜK HARFLİ DİZGE YOK [D155③] — kapitaller yalnız
   NEGATIVE bloğunda ve TIMELINE fiillerinde.
```

**Yıpranma haritası — sabit, göç etmez [D42]:**

```
① sol ön kolun dış yüzü: 6 cm'lik açık gri sürtünme izi
② sağ dizlik: kanca yuvasının etrafında koyu gri aşınma halkası
③ göğüs plakasının sol alt köşesi: 3 cm çentik
Üç bölge FİLM BOYUNCA SABİT. Yeni iz eklenmez, mevcut iz büyümez.
```

**Vizör içi aydınlatma bloğu** (yalnız göz bütçesi sahnelerinde — S4 · S9 · S13):

```
The visor stays sealed, in place and unchanged for the whole take — it never
opens, closes, tints, clears or disappears. Interior fill comes from the
suit's own chest console 15 cm below the chin, throwing a low warm key onto
the face inside the sealed visor. Both eyes, brow and upper cheek read
clearly through the glass for the full shot. The glass keeps a faint surface
reflection and visible scratches; it never becomes invisible. No lens flare,
no glow bloom, no clean glass.
```

### 🌍 World Bible

```
YER        Alçak yörünge değil — yıldızlar arası boşlukta değil: soğuk bir
           gaz devinin dış halka boşluğunda, hiçbir gövdeye yakın olmayan
           bir nokta. Serbest düşüş: 0 g, her karede.
OLAY       Sekiz gün önce burada bir kargo taşıyıcısı parçalandı. Enkazı
           dağılmadı: 40 metre çapında küresel bir KABUK hâlinde asılı kaldı.
           Kabuk sekiz gündür milimetre kımıldamadı.
KABUK      dış çapı 40 m · kabuk kalınlığı 6 m · merkezde 20 m yarıçaplı
           boşluk. Parça sayısı KADRAJ BAŞINA yazılır (aşağıdaki sayısal
           kilit listesi) — model şişirmesin.
PARÇALAR   panel dilimleri (0,4-2,0 m), bükülmüş destek çubukları, kopmuş
           kayışlar, tek tek civatalar. Hepsi aynı soluk metal ailesinden:
           mat açık gri, kenarlar soğuk ve yırtık.
MEKİK      9 m boyunda tek kişilik hurda mekiği, kabuktan 60 m uzakta.
           İki konum ışığı: soluk beyaz. S1 0:12'de ikisi de söner ve
           filmin geri kalanında sönük kalır.
IŞIK       TEK baskın kaynak: uzak bir yıldız, kadrajın sağ üst köşesinden,
           kabuğun ARKASINDAN ve biraz yanından. Sert, paralel, beyaz.
           Gölgeler MUTLAK SİYAH, jilet gibi keskin kenarlı. Dolgu ışığı YOK.
           İkinci pratik ışık: kask lambası (S4-S11), dar beyaz koni.
SES        Dışarıda ses YOK. Duyulan her şey gövdeden iletilir veya kask
           içindedir. Reverb YOK — kuru miks (vakum).
LENS       KÜRESEL. Anamorfik yatay parlama YASAK — vakumda atmosferik
           saçılma yok, parlama fiziksel olarak yanlış [SİNEMATOGRAFİK §11].
```

```
⛔ IŞIK MIKNATISI YAPISAL OLARAK ELENDİ [KART 9 · D104]
   Kartın tuzağı: "kadrajda TEK baskın ışık varken model hareketli özneyi
   ONA döndürür". Bu filmde yıldız, karakterin HEDEFİYLE aynı yöndedir
   (kabuğun arkasında). Model refleksiyle özneyi ışığa döndürürse DOĞRU
   cevabı üretmiş olur. Kartın dört kanallı panzehirine gerek kalmadı;
   riski prompt değil KOMPOZİSYON kaldırdı.
   ⚠️ Dönüş yolunda (S12-S13) yön tersine döner ve ışık arkada kalır —
      o iki sahnede yön negatifi ve omuz hattı derecesi promptta YAZILIR.
```

### 🎥 Camera Bible

```
Her klip içinde kamera hiç hareket etmez: zoom yok, pan yok, tilt yok,
track yok, kesme yok, sürüklenme yok. Sabitlik emri her video promptunda
İKİ KEZ yazılır — cümle başında ve sonunda [KAMERA_ACISI §6①].
Sahneler ARASINDA kurulum değişir ve bu ZORUNLUDUR [KART 8 kapsam bloğu].

HAREKET SÜNGERİ [KAMERA_ACISI §6②]: kadrajda her zaman bir mikrodinamik
vardır ve o ASLA donmuş parçalar değildir — vizör iç yüzeyinde nefes
buğusunun kenardan büyümesi, kask lambası konisinde tek tek geçen zerreler,
karakterin kayışının serbest ucunun 0 g'de yavaş sürüklenmesi.
⛔ Süngersiz sabit kadraj fotoğraf donukluğuna düşer.
```

### 💡 Lighting Bible

```
P1  DIŞ         uzak yıldız, sağ üstten, sert paralel beyaz; mutlak siyah
                gölge; mekiğin iki soluk beyaz konum ışığı (yalnız S0-S1)
P2  SINIR       kabuk kenarındaki parçalar keskin kenar ışığı alır; arka
                plan mutlak siyah; ön yüzler yarı karanlık
P3  İÇ          yıldız ışığı kabuk boşluklarından TEK YÖNLÜ hüzmeler hâlinde
                girer; parça gölgeleri uzun ve keskin
  P3a  kask lambası açık, dar beyaz koni
  P3b  gaz/kopma olayı kadrajda beyaz bir olay yüzeyi ekler
  P3c  tepeden: hüzme kadrajın köşegeninde, gölgeler kadrajın yarısı boyunda
P4  MERKEZ      hüzmeler daralır; ana ışık kask lambasıdır; çevre neredeyse
                tamamen siyah, yalnız en yakın parçaların kenarları okunur

⛔ ANTI-BLOOM: 0% bloom, no glow filter, no soft focus, no dreamy haze.
⛔ "cinematic lighting" YAZILMAZ [D33] · "glowing / radiant / shimmering /
   ethereal" YAZILMAZ [D29].
⛔ KIRMIZI YOK. Deponun `DEEP EMERGENCY RED` kalıbı bu filmde hiç
   kullanılmaz — POLİTİKA §3 imza ⑦ (kırmızı yoğunluk + yakın plan) böylece
   hiç tetiklenmez. Palet gri-beyaz-siyah; tek sıcak nokta vizör içi dolgudur.
```

### ⚙️ Physics Bible

```
YERÇEKİMİ       0 g — serbest düşüş, 14 sahnenin 14'ünde.
SIFIR-G MİKRO   Süzülen beden rijit DEĞİLDİR [D23]: eksen dönüşü yavaş ve
HAREKET         sürekli, serbest uzuv gecikmeli sürüklenir, kayış ucu
                gövdeden bağımsız hareket eder.
ETKİ-TEPKİ      Newton 3 çalışır: iten geri savrulur. Kütle oranı yazılır —
                4 kg kelepçe, 1,2 m/s ile atılır; 96 kg giyimli kütle
                0,05 m/s ile ters yöne gider (ilerleme klip başına ~0,5 m).
İHLAL           Kabuğun içine giren katı cisim hızının TAMAMINI kaybeder ve
(NOVUM)         durur. Yavaşlama süresi 0,15 saniyeden kısadır — çarpma yok,
                sıçrama yok, titreme yok, yön değiştirme yok.
                Duran cisim SONSUZA KADAR durur; hiçbir sahnede yeniden
                hareket etmez — S13 hariç, ve orada HEPSİ birden hareket eder.
HALAT           Gergin halat DÜZ bir çizgidir [D26]; katı cisim çarpışmasına
                uyar, kıvrılmaz, elastik dalga taşımaz. Koptuğunda kopan uç
                geri fırlamaz — bu bulutta durur.
PARÇACIK        Kabuğun İÇİNDE serbest zerre YOKTUR (hepsi durmuştur).
                Zerre yalnız karakterin KENDİ etrafında bulunur: kask
                lambası konisinde tek tek sayılabilir, birkaç düzineyi
                geçmez, her biri ayrı bir nokta olarak okunur, saniyede
                yarım metre hızla düz bir yay çizer [D143 · D30].
                ⛔ perde/şelale/duman/kıvrım YOK; "swirl" YAZILMAZ [D39].
VAKUM           Dış ses 0 · egzoz/gaz düz keskin koni, kıvrılmaz, kabarmaz
                [D36] · rüzgâr yok · toz asla yere oturmaz (yer de yok).
```

### 🚫 Negative Bible

> `KILAVUZ_REHBERI` §5 negatif çekirdek **TAM METİN** her prompta yapıştırılır.
> Filme özel ek üç satır aşağıda; ikisi POZİTİF yazılmıştır [D59].

```
NEGATİF ÇEKİRDEK (§5 tam metin):
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly one human character — no duplicates, no clones, no second
person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure throughout. Equipment and
clothing identical to the description — no drift, no gear appearing or
disappearing mid-shot. Dirt and wear staining stays fixed and never shifts.
No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not on
the ground, the rock, the ice or any natural surface in the frame. Nothing
in this world has been measured, labelled, marked out or annotated by
anyone: no scale marks, no graduation ticks, no survey markers, no engraved
or painted characters of any kind. No subtitles, no captions, no burned-in
dialogue text, no title card, no end card, no credits, no watermark. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers, rigid-body collision throughout. All particles
obey the stated gravity with continuous physical momentum — never hovering,
never frozen, never swirling or flowing like liquid. Environment static and
stable — no melting terrain, no warping topology, no swimming texture. No
Unreal Engine look, no CGI aesthetic, no video game aesthetic.
Photorealistic with 35mm film grain.

+ D79 KASK BLOĞU (her prompta):
The suit has no back-mounted unit: no backpack, no tank, no hose, no cable,
no rear housing of any kind — the back of the suit is one continuous smooth
panel from collar to hip, unbroken, carrying nothing. The visor is optically
clear glass with zero tint, zero mirror coating and zero reflection of the
environment; her face is fully readable through it in every frame, at every
head angle.

+ FİLME ÖZEL ÜÇ SATIR (ikisi pozitif):
① No anamorphic flare, no horizontal streak flare — spherical lens only.
② POZİTİF: The held fragments are ordinary torn hull metal — flat panels,
   bent struts, loose bolts and cut strap ends. Every one of them is a dead
   object with a plain machined shape; nothing in this field has limbs,
   joints, a head, eyes, a face or any part that could belong to a living
   thing, and nothing grows, opens, folds or reaches.
③ POZİTİF: The star is a single hard white point source outside the frame
   on the upper right; every shadow it casts is absolutely black with a
   razor edge, and no second light fills those shadows.
```

```
⚠️ ② NEDEN POZİTİF YAZILDI: "no creature, no alien, no monster" kalıbı
   sınıflandırıcıya kavramı SOKAR [D123] ve modele ne ÇİZECEĞİNİ söylemez
   [D59]. Yukarıdaki cümle aynı işi yapar ve iki riski birden kapatır.
⛔ NEGATIVE bloğu 900 karakteri geçen sahne YOKTUR — insansız sahnelerde
   blok TEK POZİTİF Style satırına iner [KART 10 · D59]. Bu filmde
   insansız sahne YOK (aşağıya bak), yani kart tetiklenmiyor.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. `03_PLAN_ONCESI` C bloğunun altı kilidi + bu filmin kendi kilitleri.

| kilit | sayı | risk kartı | sahne |
|---|---|---|---|
| **HUMAN COUNT LOCK** | tam 1 insan, 14 sahnenin 14'ünde. Mürettebat yok, pilot yok, ikinci siluet yok, yansımada ikinci figür yok, gölgede ikinci figür yok | KART 4 | S0-S13 |
| **HELMET STATE SCHEDULE** | kapalı S0-S13 (14 sahne) · açık 0 sahne · vizör optik berrak, tint 0, ayna kaplama 0 | KART 3 · D79 | S0-S13 |
| **İNSANSIZ SAHNE** | 0 sahne — 14/14 karakterli. Kart 10'un yapısal red profili hiç doğmaz | KART 10 | — |
| **YERÇEKİMİ** | 0 g · 14/14 sahne · düşen cisim yok, atılan cisim sabit hızla gider | KART 6 | S0-S13 |
| **KÜTLE ORANI** | kelepçe 4 kg · giyimli insan 96 kg · atış hızı 1,2 m/s → geri tepme 0,05 m/s → klip başına ilerleme ~0,5 m | KART 6 | S6 · S10 · S11 |
| **DURMA SÜRESİ** | giren cisim hızını 0,15 saniyeden kısa sürede tamamen kaybeder; çarpma 0, sıçrama 0, titreme 0 | novum | S2 · S5 · S6 · S10 · S11 |
| **KELEPÇE SAYACI** | 8 → 7 (S6) → 5 (S7) → 2 (S9) → 0 (S10). Monotonik, hiç artmaz. Metin 0,0 s — sayı yalnız kuşaktaki boş halkalardan okunur | KART 5 | S1·S4·S6·S7·S9·S10·S12 |
| **PARÇA SAYISI (kadraj başına)** | EWS: 240-300 ayrık parça, gerisi sığ odakta kütle · WS: 60-80 · MS: 18-24 · CU: 6-9 · ECU: 2-3. Model şişirmesin | KART 6 | tümü |
| **ZERRE SAYISI** | kask lambası konisinde aynı anda en fazla birkaç düzine zerre; her biri ayrı bir nokta; 0,5 m/s; arka yüzey hep görünür kalır | D143 | S4-S11 |
| **ÖLÇÜ** | kabuk dış çap 40 m · kabuk kalınlığı 6 m · iç boşluk yarıçapı 20 m · mekik boyu 9 m · mekik mesafesi 60 m · kelepçe 30 cm · güç hücresi 60 × 40 cm · karakter 1,8 m | KART 6b | tümü |
| **SIVI TEMASI** | 0 sahne — filmde sıvı yok | KART 1 | — |
| **CANLI ANATOMİSİ** | 0 kare. Filmde bacak/baş/kuyruk/uzuv taşıyan hiçbir varlık yoktur; parça sayımı yerine geçen kilit ② negatif bible satırıdır | KART 2 | — |
| **DİYALOG** | 0 replik · 14/14 sessiz sahne · ekran metni 0,0 saniye | KART 7 | — |
| **SAHNE İÇİ KESME** | 0 — 14/14 tek çekim, sabit lockoff. SHOT COUNT = CLIP COUNT = 14 | KART 11 | — |
| **ÖLÇEK KESRİ** | karakter kadraj yüksekliğinin: S0 %9 · S7 %10 · S11 %11 · S13 %8 | KARAKTER §5.1 | — |

```
⛔ SAHNE İÇİ KESME KARARI — GEREKÇE [D74: kaydı olmayan kapı koşulmamış kapıdır]
   TEK_CEKIM §5.4 aksiyon grameri (Mimari 2) bu formatta emsallidir
   (THE_DAWN_FRONT: 14 sahne · 26 segment · 12 kesme). BU FİLMDE KULLANILMADI.
   Sebep Mimari 2'nin kendi kayıtlı zayıflığıdır: "2. ve 3. segmentin
   REFERANS İMAJI YOK — kıyafet ve ölçek kayması riski kesmeden sonra artar."
   Bu filmin en kırılgan iki kilidi tam olarak kıyafet (KART 3) ve ölçek
   (parça sayısı · kabuk çapı) — ikisi de kesmeden sonra ölçülemez hâle gelir.
   TELAFİ: aksiyon kadrajın İÇİNE ve sahneler ARASI ölçek sıçramasına taşındı
   (2 bilinçli şok + 13 çiftin 13'ünde ölçek değişimi). Kesme sayısı 0 olduğu
   için KART 11 hiç tetiklenmez ve kırpma tablosu gerekmez.
```

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| **D157** | Tek kare testi novumun KENDİ taşıyıcısıyla koşulur; taşıyıcı kadrajın ≥1/10'u ve değişim tek klip içinde; novum sahnesinde ikinci olay yok | §NOVUM · S6 |
| **D158** | Merkezi seçimden sonraki seçim sayısı ≥1 · başarısız deneme ≥1 | B2a: S12 · B2b: S5 ve S8 |
| **D155** | Faz satırı ve büyük harfli kısaltma prompt gövdesine girmez | Character Bible uyarı bloğu |
| **D154** | Tekrarlayan olay bir varlıktır: kabul/ret ölçütü olayın göründüğü HER sahneye kopyalanır | "durma olayı" ölçütü S2·S5·S6·S10·S11 promptlarının hepsinde birebir |
| **D153** | Eş kadraj çiftinin ayna sahnesi, kaynak sahnenin ONAYLI karesinden türetilir; fark listesi ≤3 madde | S0 ↔ S13 çifti — üretim sırası ve fark listesi aşağıda |
| **D139** | Kamera arkada/OTS ise sırt POZİTİF yüzey cümlesiyle yazılır | S3 · S5 · S10 (OTS kurulumu D) |
| **D143** | Işık konisindeki toz ZERRE SAYISIYLA yazılır; perde/şelale yasak | Physics Bible · zerre kilidi |
| **D138** | Metin yasağının KAPSAMI yazılır; ölçü yüzey işaretine bitişik yazılmaz | negatif çekirdek tam metin · ölçüler SPEC'te |
| **D104** | Işık mıknatısı — burada YAPISAL olarak elendi (ışık hedefle aynı yönde) | World Bible ışık bloğu |
| **D123** | Yasak yazma, malzemeyi TARİF ET | negatif bible ② ve ③ pozitif yazıldı |
| **D26** | Gergin halat düz; katı cisim çarpışmasına uyar | Physics Bible · S8 |
| **D23** | Sıfır-g'de beden rijit değil | Physics Bible · her sahne |
| **D42** | Yıpranma sabittir, göç etmez | üç bölgeli yıpranma haritası |
| **D58** | Tekrar eden nesne her sahnede aynı sayısal kimlikle | kelepçe kuşağı 7 sahnede |
| **D69/D77** | Biniş-iniş hareketi kadraja alınmaz | ⛔ aşağıdaki A4 taraması |

### A4 — yasaklı sahne tipi taraması [D77]

```
□ araç/kapak/airlock BİNİŞ-İNİŞ hareketi   → S12'de karakter mekiğe TUTUNUR,
  binmez; kapak açılmaz, içeri girilmez. Biniş hareketi 0 kare. [D69 ①]
□ tek ışıklı loş iç mekâna GİRİŞ           → 0 sahne (film tamamen dışarıda)
□ aynalı-yansıtıcı yüzey önünde tek karakter → 0 sahne (vizör tint 0, ayna
  kaplama 0; mekik gövdesi mat) [D20 · D69]
□ novum'u TÜRETİLMİŞ optik fenomen taşıyor → HAYIR: taşıyıcı 30 cm çelik
  kelepçe, katı cisim [D73]
□ novum'u bir YOKLUK taşıyor               → HAYIR: ihlal bir OLAYDIR
  (hızın kaybı), yokluk değil [D76]
□ jenerik / başlık kartı / kapak çıktısı   → 0 kare [D34 · D70 · D72]
```

### D153 — eş kadraj çifti üretim protokolü (S0 ↔ S13)

```
① ÜRETİM SIRASI: önce S0 üretilir ve ONAYLANIR. S13'ün imajı, S0'ın onaylı
   karesi referans/başlangıç görseli alınarak üretilir (image-edit).
② FARK LİSTESİ — TAM ÜÇ MADDE, yalnız FARKLAR yazılır:
   · every fragment in the shell is now moving, all of them together, in
     the same direction and at the same speed, each one carrying a short
     motion trail toward screen-left — the SAME fragments, nothing new
     has entered the frame
   · the grey power cell is out in front of the field, closest to the
     woman, the SAME cell that was deep in the shell, not a second object
   · the woman now hangs against the shuttle hull with one open palm
     raised, the tool belt gone from her hips
③ ARKA PLAN SETİ (yıldız yönü · mekik konumu · kabuk çapı · kamera) FARK
   LİSTESİNE GİRMEZ = aynen kalır.
```

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S8 · 1:26 — halatın koptuğu an.
NÖTR TARİFİ:         "the taut line parts at the worn splice; the free end
                     travels forty centimetres and stops there, straight and
                     motionless, its cut fibres standing out from the core"
                     ⛔ "snaps", "whips", "lashes", "strikes her" YAZILMAZ —
                       kuvvet NESNEDEDİR, gövdeye yönelmez [POLİTİKA §4.1①]

İKİNCİ SIRADAKİ:     S11 · 1:56 — itiş jesti. Nötr tarifi: "she sets both
                     palms flat on the cell and extends her arms until they
                     lock; the cell leaves her hands at walking pace"
```

**Alınan her politika önlemi:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Patlama kadraja alınmadı — kargo taşıyıcısının parçalanması sekiz gün önce, kadraj dışında oldu | "felaketin anı" vuruşu; izleyici yıkımı görmüyor | **② malzeme sonucu**: yıkım, kesik kenarların KENDİSİNDE okunur — soğuk yırtılmış metal, kopmuş kayış uçları, bükülmüş destek çubukları. `explosion` / `blast` / `fire` kelimeleri hiçbir promptta geçmez |
| Kırmızı acil aydınlatma kalıbı kullanılmadı | deponun yerleşik gerilim paleti (POLİTİKA §3 imza ⑦'nin kaynağı) | **③ alet tepkisi**: gerilim renkten değil, mekiğin İKİ konum ışığının S1'de sönmesinden ve kask lambasının S10'da kısılmasından okunur. Metin 0, renk 0, yalnız doluluk |
| Gövdeye değen kuvvet 0 kare — hiçbir parça karaktere çarpmaz | "az kalsın" vuruşu | **① kütle-hız**: kuvvet vektörü hep NESNENİNDİR — kopan halat ucu, fırlatılan kelepçe, ayrılan güç hücresi. Karakter kuvvetin YANINDA durur, önünde değil [POLİTİKA §3 imza ⑤] |
| Uzaylı anatomi olarak hiç çizilmedi | "yaratığı görme" vuruşu | **① kütle-hız + ② malzeme sonucu**: varlık, S13'te 300 parçayı aynı anda aynı yöne çevirerek kendini gösterir. Anlam maliyeti sıfır değil ama ölçüldü: KART 2'nin canlı skoru hiçbir filmde 5'i geçmedi; bu film o skoru hiç riske atmaz ve karşılığında UZAY OPERASI yasağına da takılmaz |

```
⛔ TELAFİ sütunu boş DEĞİL — dördü de bir kanala taşındı.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
⛔ prompt_kontrol ⑯ üretimden önce koşulur (kelime ekseni);
   kompozisyon ekseni PROMPT_QA_CRITIQUE rubriğinde denetlenir.
```

---

## 📋 RİSK SAYIMI  (`02_RISK_KARTLARI.md` RİSK TOPLAMI · payda 13)

| # | soru | durum |
|---|---|---|
| 1 | Su/sıvı teması | ❌ yok |
| 2 | Canlı | ❌ 0 kare (uzaylı anatomi olarak hiç çizilmiyor — §NOVUM karar kaydı) |
| 3 | Kask/vizör | ✅ **VAR** → HELMET STATE SCHEDULE |
| 4 | İkinci figür riski | ✅ **VAR** (her filmde) → HUMAN COUNT LOCK |
| 5 | Ekran/sayaç/gösterge | ✅ **VAR** → kelepçe sayacı, metinsiz kanal |
| 6 | Parçacık/toz/patlama | ✅ **VAR** (parçacık) · patlama 0 kare → zerre sayısı kilidi |
| 6b | Katmanlı/bölgeli dünya | ❌ yok (tek katman, tek ışık kaynağı) |
| 7 | Diyalog | ❌ yok (0 replik — en güvenli sınıf) |
| 8 | Kamera hareketi | ❌ kaldırıldı (klip içi lockoff 14/14) |
| 9 | Tek baskın ışık + hedefe hareket | ❌ yapısal olarak elendi (ışık hedefle aynı yönde — World Bible) |
| 10 | İnsansız sahne | ❌ yok (14/14 karakterli) |
| 11 | Değişken çekim süresi / sahne içi kesme | ❌ yok (sabit 10 s · 0 kesme) |
| 12 | Politika yüzeyi | ✅ **VAR** → dört önlem, dördü de telafili |

```
RİSK SAYISI: 4 / 13     (kartlar 3 · 4 · 5 · 6 · 12 → 12 dahil 5, ama
                         KART 12 eşiği BAŞLATMAZ [kartın kendi kuralı])
   sayım: 3 · 4 · 5 · 6 = 4 malzeme riski  +  12 politika = ayrı sayılır
→ 4 risk: "dikkat, en riskli malzemeyi bir sahneye hapset" bandı.
   EN RİSKLİ MALZEME: parçacık (KART 6). Hapsedildiği yer: zerreler
   YALNIZ kask lambası konisinde var; kabuğun içinde serbest zerre 0.

⚠️ 9 SORULUK ESKİ SKALADA (kalibrasyon uyarısı — kartın kendi notu):
   kask · ikinci figür · sayaç · parçacık = 4/9. Eski filmlerle
   karşılaştırılabilir tek sayı budur.
```

---

## 🚪 PROMPT KAPISI KOŞULDU — 01.09.2026

```
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
        yatay_2_dk_filmler/THE_STILL_SWARM

SONUÇ: ⛔ 0 BLOCK · ⚠️ 2 FIX · ✅ 1 GO   (çıkış kodu 1)
       📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik · 28 prompt
       → dizi kapıları film boyunca koştu (klasör modu satırı çıktıda VAR)

GEÇEN KAPILAR
  ② yasak kelime 0 · ③ self-contained ✅ (0 BIBLE atfı) · ⑤ kilit varlığı ✅
  ⑤b yüzey işaretine bitişik ölçü 0 · ⑥ pusula kelimesi 0 · ⑦ çapasız toward 0
  ⑧ nesne-göreli taraf 0 · ⑨/⑫ abartı eşiği ✅ (+25 / −25 / +90 tepe)
  ⑩ ardışık aynı kurulum 0 · ⑪ açı tipi 6 (≥3) · ⑬ TEMA + 4 sahne indeksi ✅
  ⑭ NOVUM TAŞIYICISI → TEK KARE satırında "çelik kelepçe" geçiyor ✅ [D157]
  ⑮ SIRT POZİTİF → üç OTS sahnesinin (S3·S5·S10) üçünde de yazılı ✅ [D139]
  ⑯ politika sözlüğü → T1 0 · şiddet fiili 0 · milliyet 0 · kurum 0 ·
     yapısal red profili 0 (insansız sahne yok)

KALAN İKİ FIX — ikisi de uzunluk bandı, ikisi de gerekçeli:
  ① VIDEO 3.704-4.299 karakter · bant 2.000-2.600 · TAVAN 4.300
     ⛔ Tavanın ALTINDA — kanıtlı Veo red eşiği aşılmıyor. Bant üstü
     kalmasının sebebi aritmetiktir: negatif çekirdek + D79 kask bloğu +
     ekran-yönü kilidi tek başına ~1.900 karakter tutuyor ve üçü de
     pazarlık dışı. `IMAGE_VIDEO_PROMPT_TEMPLATES.md` bu çelişkiyi zaten
     kaydediyor ("uzunluk bandıyla aritmetik olarak çelişiyordu").
     Yapılan kısaltma: ilk yazımda 4.443-5.101 idi; kilitlere dokunmadan
     yaklaşık 800 karakter indirildi ve tavanın altına alındı.
  ② IMAGE 2.097-2.681 karakter · bant 1.700-2.100
     Betiğin kendi notu: "Bu bant depodaki hiçbir filmle uyuşmuyor; karar
     bekliyor." Image bandı ÖLÇÜLMEMİŞTİR, bulgu değil GÖZLEMDİR.

⛔ SIRADAKİ ADIM — PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md
   Betik kelime eksenini ölçer; KOMPOZİSYON ekseni (POLİTİKA §3'ün yedi
   imzası) betiğe inmez ve insan yarısında denetlenir.
```

### ✅ RUBRİK KOŞULDU — PROMPT_QA_CRITIQUE_PROMPT.md · 01.09.2026

```
KARAR: GO   ·   BETİK KARARI: FIX (çıkış kodu 1 · 0 BLOCK)

§1 KİLİT SAYIYA ÇEVRİLMİŞ Mİ — ⚠️ ÜÇ TARİF KİLİDİ BULUNDU VE DÜZELTİLDİ
   Eşik: "üç ve üzeri tarif kilidi → BLOCK". Tam eşikteydi; düzeltilmeseydi
   koşu BLOCK verirdi.
   ① "at a walking pace" · 14 geçiş  → "at about 1 metre per second"
      "at a slow walking pace"       → "at about 0.5 metres per second"
   ② "slow continuous axis drift" · 8 geçiş
                                     → "a slow axis roll of about 10 degrees
                                        per second"
   ③ "rolling slowly about her axis" → "at about 10 degrees per second"
   Ölçülmüş gerekçe: tarif kilidi %0 tuttu, sayısal kilit %100 tuttu
   [01_DERS_ETKINLIK_RAPORU §4].

§2 TETİKLENEN DERSLER — 🔴 tetikleyicinin üçü de KİLİTLİ
   🔴 canlı        → 0 kare · pozitif negatif cümlesi her promptta
   🔴 biniş/iniş   → 0 kare · S12'de "she never opens a hatch and never
                      climbs inside" [D69 ①]
   🔴 ayna yüzey   → vizör tint 0 / ayna kaplama 0 · mekik mat [D20 · D69]
   🟠 kask         → D79 iki cümlesi 28/28 promptta
   🟠 sayaç        → metinsiz kanal (kuşaktaki boş halkalar)
   🟠 ikinci figür → "Exactly one human character" 28/28
   🟡 parçacık     → kadraj başına parça sayısı yazılı
   🟡 sıfır-g      → mikro hareket sayıyla (10°/s eksen dönüşü) [D23]

§3 A1 ÇELİŞKİSİ — YOK ✅
   Dramatik bilgi: kelepçe sayacı 8→0. Kanalı GEOMETRİ (kuşaktaki sayılabilir
   boş halkalar), metin değil. Hiçbir promptta "reads/displays/shows" yok.

§3b YASAK LİSTESİ POLİTİKA MALİYETİ — ⚠️ BİR YIĞILMA BULUNDU VE TEMİZLENDİ
   `dead` · 14 geçiş, hepsi "stops dead" / "a dead straight line" deyimlerinde.
   Filmde 0 kare ölüm var → rubriğin kuralı: kelime SİLİNİR [D123].
   → "stops completely" · "a perfectly straight line" · "cutting off at 8s"
   Kalan: 0. Betik ⑯ sonucu: T1 0 · şiddet fiili 0 · milliyet 0 · kurum 0.
   ⚠️ `rigid-body collision` (15 geçiş) DOKUNULMADI: negatif çekirdeğin kendi
      cümlesidir ve T2 kalibrasyonu "body-lengths" ailesini zaten muaf tutar.

§3c KOMPOZİSYON YÜZEYİ — betiğin göremediği tek eksen, dört soru
   □ yüz yok + uzuv kadrajın konusu + makro üçü birden?
     → S4 (ECU makro, kuşak ve eller) bu imzaya EN YAKIN sahnedir
       [POLİTİKA §3 imza ①]. İki panzehir zaten yazılı: (a) çevresel çapa —
       "Behind the belt and out of focus: 3 fragments … and beyond them
       absolute black" [§3.2]; (b) 7. saniyede sealed visor kadraja girer ve
       YÜZ GÖRÜNÜR olur [imza ⑥ · D79 açık vizör kilidi].
       ⛔ Bu sahne üretimde İLK reddedilecek adaydır; red gelirse §5 merdiveni
         ve kamerayı nesne HİZASINA alma çözümü (parçaları ard arda diz).
   □ bedenden bir şey çıkarılıyor mu? → HAYIR ✅ ve bu bilinçli düzeltildi:
     kuşak S11'de ZATEN kolda ("the empty canvas tool belt now hooked over
     her left forearm and off her hips"), S12'de yalnız BIRAKILIR. Çıkarma
     eylemi 0 kare [POLİTİKA §3 imza ② · COLD BURN S28 iki kez reddedildi].
   □ kütle + kaçan tek kişi? → YOK ✅ (tek insan, kütle yok)
   □ konuşan yüz + kapital kimlik + tehlike? → YOK ✅ (0 replik, kapital blok yok)

§4 SELF-CONTAINED — ⚠️ ÇAPA TUTARSIZLIĞI BULUNDU VE DÜZELTİLDİ
   Üç uzak-çekim promptu (S7 · S11 image + video) çapayı kısaltmıştı: ten
   tonu ve saç yoktu. SAHNE_DEVAMLILIK §2.1: "aynı anlamda YETMEZ".
   → üçüne de "warm medium-brown skin, dark brown hair cropped close to the
     scalp" eklendi. 28/28 promptta çapa artık aynı aileden.
   ⚠️ AÇIK SORU (bulgu değil): S13 image promptu "the same frame as the
     approved opening still" ile açılıyor — bu bir ATIF gibi görünür ama
     D153'ün image-edit protokolüdür ve prompt atıf olmadan da tam tariftir.

§5 ÇEKİM TARİF EDİLMİŞ Mİ ✅
   28/28 promptta zaman damgaları toplam süreyi dolduruyor · her damgada
   görülen bir değişim var · doruk S11'in İÇİNDE (itiş 2s, durma 4s).

§6 AÇI VURUŞLA EŞLEŞİYOR MU — 11 sahne birebir, 3 gerekçeli sapma
   birebir: S2·S6·S9 epifani→göz hizası profil MS 50mm · S3 keşif→OTS ·
            S7 hiçlik→tepe XLS · S8·S12 yenilgi→üst açı · S0·S13 kurulum→EWS
   sapma ①: S1 katalizör, üst açı — gerekçe: karakter kabuğun karşısında
            küçülür, "korunmasız av olarak işaretleme" öngölgesi [ACI_YAYI §8.2]
   sapma ②: S10 her şey kayboldu, OTS CU — kılavuz üst açı LS der; kayıp
            burada bir NESNE kaybıdır (kuşak boşalır) ve LS onu okunmaz kılar
   sapma ③: S11 doruk, alt açı EWS — alt açı KARAKTERE değil KABUĞA verilir
            (kabuk üstte, karakter altta %11); ACI_YAYI §5'in kurban
            perspektifi kuralının doğru kullanımı
   □ sabitlik emri iki kez ✅ ("locked off" başta · "stays perfectly static,
     zero movement, no drift" sonda) [KAMERA_ACISI §6①]
   □ hareket süngeri 14/14 sahnede ✅ (kayış ucu · lamba konisindeki zerreler ·
     duran haze · hareket eden alan)

⭐ RUBRİK DIŞI AMA ÜRETİM İÇİN KRİTİK — SATIR SONU TİRE ONARIMI
   Sarma sırasında "screen-right" gibi tireli terimler satır sonunda
   bölünmüş ve iki ayrı sözcüğe dönüşmüştü ("screen- right"). 10 blokta
   onarıldı; ekran yönü kilidi artık her promptta bütün bir terim.
   Kalan bölünme: 0.
```

---

## 🎬 ÜRETİM SIRASI — en pahalı/riskli sahneden

```
1. S6   NOVUM TAŞIYICISI · TEK KARE. Kural burada doğar; tutmuyorsa film yok.
2. S11  DORUK + paylaşım sahnesi (huşu) + ölçek 1:11.
3. S13  TWIST — 300 parçanın eşzamanlı hareketi, filmin en zor tek kadrajı.
4. S0   HOOK · 2-3 varyant, farklı hook tipiyle DEĞİL (tek tip kararı), aynı
        tipin üç kompozisyonuyla; en iyisi seçilir ve film ONA kilitlenir
        [HOOK §7]. ⛔ S13 imajı S0'ın ONAYLI karesinden türetilir [D153].
5. S7   tepeden hat — dramatik ironinin tek taşıyıcısı.
6. kalan sahneler sırayla.
```

---

## ✅ ÜRETİM ÖNCESİ KONTROL — THE STILL SWARM            tarih: 01.09.2026

```
A1 □ "no text" ile ekran içeriği aynı dosyada YOK ✅
     Sayaç metinle DEĞİL fizikle anlatılıyor: kuşaktaki boş halkalar.
     Planda tek bir "reads / displays / shows the number" cümlesi yok.
A2 □ sahne sayısı: başlık 14 = blok 14 = "Scene N of 14" 14 ✅
A3 □ süre: 14 sahne × 10 s = 140 s = 2:20 = iddia edilen süre ✅
A4 □ yasaklı sahne tipi taraması yapıldı — altı tipin altısı da 0 sahne.
     Karar satırı: "S12: mekiğe TUTUNMA; biniş hareketi kadraj dışı — D69 ① gereği"
B1 □ doruk anı S11 İÇİNDE tarif edildi (1:50-2:00, itiş → durma → savrulma
     → 2,0 s donma); iki sahne arasına DÜŞMÜYOR ✅
B1b□ katmanlı dünya DEĞİL — ışık takvimi P1→P2→P3→P4→P3→P2→P1, monotonik
     bir yay çiziyor (dışarı→içeri→dışarı) ✅
B2 □ bedelli seçim S11; kayıp S11'in içinde ve S12'de GÖRÜLÜYOR (boş kuşak,
     hücre kabuğun içinde kalmış) ✅
B2a□ merkezi seçimden sonraki seçim sayısı: 1 (S12 kuşağı bırakma) ·
     koda 2 sahne (eşik 3-5'in altında) ✅ [D158]
B2b□ başarısız deneme sayısı: 2 (S5 gaz itkisi · S8 halat) ✅ [D158]
B3 □ TEMA: İLK TEMAS · motife döndüğü sahneler: S1, S7, S11, S13 (≥3 ✅)
     B2'nin bedel sahnesi (S11) bu listede ✅
B4 □ kurulum dizisi: A·B·G·D·E·D·G‖F·B·G·D·H·B·A · kurulum sayısı 7 ·
     açı tipi 6 · ardışık çiftler güvenli bantta · şok 2/2 ·
     derece satırları abartı bandında (+25 / −25 / +90 tepe) ✅
B6 □ POLİTİKA SATIRI: en red-riskli kare S8 · nötr tarifi yazıldı ·
     dört önlemin dördü de ÖNLEM/MALİYET/TELAFİ taşıyor · milliyet/kurum/
     gerçek kişi adı planda YOK ✅
C  □ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı · canlı) ✅
D  □ risk sayımı yapıldı: 4/13 (eski skalada 4/9) ✅
E  □ QA SPEC bloğu AYRI DOSYADA: THE_STILL_SWARM_QA_SPEC.md ✅ [D117]

SENARYO/KAMERA EK KONTROL (SENARYO_VE_VIRAL §7):
□ Vuruş tablosu dolduruldu, boş vuruş yok ✅
□ CENTRAL CHOICE S11; seçim "iki avucu hücreye koyup kolları kilitlenene
  kadar uzatma" jestiyle ekranda tamamlanıyor ✅
□ Novum taşıyıcısı birincil nesne (çelik kelepçe) — türetilmiş fenomen değil ✅
□ Açılış-kapanış imaj çifti yan yana yazıldı; değişim okunuyor ✅
□ LOOP SATIRI: S13'ün son beat'i (avuç açık, hücre 1 m ötede, HAREKET SÜRÜYOR)
  ile S0'ın ilk beat'i (aynı kurulum A, aynı ışık, halat boyunca süren kayma)
  aynı kadraj ailesinde. Son karede poz verilmez, dondurulmaz. Müzik son
  saniyede çözülmez — 1 saniyelik mutlak sessizliğe iner, sessizlik loop'lanır.
  ⛔ Jenerik/başlık kartı 0 kare [D70]
□ HOOK §8 yedi maddesi yukarıda dolduruldu ✅
```

---

## 🔗 BU FİLMİN OKUDUĞU DERSLER — son 5 FİLM dersi (sayaç 🧭 bloğu)

```
D153 EŞ KADRAJ ÇİFTİ      → S0↔S13 protokolü yazıldı (üretim sırası + 3 maddelik fark listesi)
D154 TEKRARLAYAN OLAY     → "durma olayı" kabul/ret ölçütü 5 sahnenin promptuna
                            BİREBİR kopyalanır; S6'nın onayı S2/S5/S10/S11'i KORUMAZ
D155 DEFTER ETİKETİ       → faz satırı ve kısaltma prompt gövdesinde YOK
D157 NOVUM TAŞIYICISI     → tek kare testi kelepçeyle koşuldu, kadrajın 1/7'si,
                            tek klip içinde, rakip olay 0
D158 BEDELDEN SONRA SEÇİM → koda 2 sahne · B2a 1 seçim · B2b 2 başarısız deneme
```
