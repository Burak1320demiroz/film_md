# 🧾 THE_COUNTED_RIVET — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu (51 dosya · 5 satır `—`).
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> **Tavan gerekçesi:** `02_RISK_KARTLARI` risk sayımı **7/14** verdi (≥5) →
> kilit tavanı ≤20 devrede. Malzeme azaltılmadı; tavanı aşan kilitler §1b'de
> gerekçesiyle duruyor.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (tavan 20 · sayım: 20)

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — köşeli parantezli etiket gövdeye girmez.

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D157 | taşıyıcı çok küçük · hafıza istiyor · aynı promptta rakip olay → altı mercek novumu anmadı | Taşıyıcı **çelik şerit**tir ve kadrajın en az onda birini kaplar; kanıtlandığı klipte kadrajda başka hiçbir şey hareket etmez. TEK KARE cümlesi şeridin ve perçin başının ADINI taşır | S5 (kanıt klibi) · S3 · S6 |
| D179 | imaj promptu değişimin SONRASINI yazdı; bedel 40 m'den 3 piksel oldu | Her IMAGE promptu 0,0 saniyeyi yazar. S5'in imajı bağ HENÜZ YERİNDE hâlini taşır; video 2,0 s'de çeker. Bedeli taşıyan değişim kadrajın kısa kenarının **en az 1/8'i** kadar yer kaplar → S5 ve S7 yakın plan | S5 · S7 · (her sahnenin 1. klibi) |
| D202 | beş filmde seçim bedende okunmadı — `THE CHOICE IS INVISIBLE` | ÇAPA ÜÇLÜSÜ: **iki eldiven** kanalı üçünde de aynı. ÖNCE mandal kolunda ↔ SONRA şeritte (S5) · ÖNCE dokuz mandalda ↔ SONRA boşta (S7). Dolgu jesti yazılmaz | S5 · S7 |
| D206 | yedi filmde efor fiili var, ödeme kanalı yok — `NOBODY PAYS` | Her efor klibinde en az bir **saniyeli ödeme satırı**: `4,0 s — her grip locks and the lacing stops for half a second`. Ödeme sonraki klibe taşınır | S2 · S3 · S5 · S7 |
| D207 | darbe/yorgunluk kesmede sıfırlandı — dört film | Yorgunluk sahne başına tek sayı, ardışık düşüş en çok bir kademe. S5'ten sonra hiçbir klip dik ve dinlenmiş bedenle açılmaz; durum satırı önceki klibin SONUNU kelimesi kelimesine taşır | S5 → S6 → S7 |
| D138 | metin yasağı kostüme yazıldı, ölçü zemine yazıldı → halkanın içine "11 metres" basıldı | Metin yasağı KAPSAMLI: giysi + plaka + perçin + mandal + şerit. ⛔ Şeride çentik, gradasyon, ölçek işareti YAZILMAZ — ölçü aleti en riskli yüzeydir. Ölçüler SPEC'te; promptta gövde-göreli (`wider than her shoulders`) | 24/24 klip |
| D175 | "through the glove" çıplak ön kol ürettirdi; çıplak-deri yasağı tek bölgeliydi | Çıplak-deri negatifi **üç bölge birden** (yaka · bilekler · ayak bilekleri), 24/24 promptta. Saydamlık tarifi yok; zorlanma giysinin yüzeyinde | 24/24 klip |
| D146 | "seamless visor" bir filmde üç kask ürettirdi; dört vakada da tutmadı | Vizör **tek düz pane + görünür kalın koyu çerçeve + derin yaka halkası**. `seamless · bubble · dome · sphere` sıfır kez. ⚠️ Referans paneli yazılmıyor → bu kilidin tek ölçülmüş aracı kapalı | 24/24 klip · risk 04_UYARI'da |
| D139 | düz sırt kilidi altı sahnenin beşinde tuttu; kamera arkaya geçen tek sahnede düştü | Kamera sırtı gören klipte yokluk cümlesi POZİTİF yüzeye çevrilir: `the back of the suit is one continuous sculpted surface from collar to hip, closed and smooth, and it carries nothing` | arkadan çekilen 2 klip (S4 · S7) |
| D209 | gök, ufuk, yer imi her sahnede yeniden tarif edildi → her sahnede başka dünya | ⚠️ **UYARLANDI** — ortam kartı ufku ve zemini kaldırıyor. Üç çapa: ① üstte kaynaksız parlak kubbe, güneş diski sıfır kare ② aşağıda okra derinlik, ufuk çizgisi yok ③ yer imi plakanın kendisi ve bir perçin başı. Üçü her klipte BİREBİR | 24/24 klip |
| D210 | kapanış açılışın kamera cümlesini taşımadı; sabit kamera klip sonunda kendiliğinden yaklaştı | K01 ile K24 **aynı kurulum harfi ve birebir aynı kamera cümlesi**. Her TIMELINE'ın son satırı `hold — the frame does not move`; CAMERA satırı `absolutely zero camera movement` | K01 ↔ K24 · 24/24 klip |
| D211 | ilk 10 saniyede soru yok, son 10 saniyede çıkış yok — dört film | K01 soruyu sorar: çene kapanıyor, içindeki yüzey hiç kavis yapmıyor. İlk 30 saniyede kurulum klibi en çok iki. Son kare adlandırılmış nesne: kesilmiş son mandal ucu; statik siyah sıfır saniye | K01 · K02-K03 · K24 |
| D213 | eylemin en pahalı üç saniyesi kadraj kenarına ya da sonraki klibe düştü | Her temaslı klipte üç satır aynı klipte: TEMAS · DEĞİŞİM · SONUÇ (sonuç ≥1 s kadrajda). Temas noktası kadrajın dış üçte-birinde olamaz | mandal · bağ · şerit geçen 14 klip |
| D214 | "self-contained" Bible'ın tamamını prompta soktu; kadrajda olmayan yüz tarif edildi | Her promptun ilk satırı `IN FRAME:`; SUBJECT yalnız kadrajdakini tarif eder. Yüz yalnız yüzün konu olduğu **1 klipte** (K19 · ECU) yazılır, kalan 23'te vizör `optically clear` der ve durur | 24/24 klip |
| D200 | altı filmde aynı kadrajda iki yerçekimi | SPEC'te tek değer: **0,904 g**. Nötr yüzerlik POZİTİF kuralla yazılır (`floats in neutral buoyancy and is settling at a constant rate; it never hovers, never hangs motionless, never rises`). Bırakılan her nesne saniyeli düşüş satırı taşır | 24/24 klip |
| D141 | klip vardı, vuruş yoktu; kurgu kapısının üç satırı da geçti | SPEC B `FİNAL VURUŞ KANITI`: kesilmiş **dokuz mandal ucu**, son klipte, sayılabilir 9 adet. Yoksa final teslim edilmemiştir | K24 |
| D192 | filmin bir numaralı riski yalnız sıfatla korundu; doruğun boşalması şimşek geldi | Bir numaralı risk: şeridin DÜZ olduğunun okunmaması. Pozitif biçim sayıyla: `the batten lies against the plate and nowhere along its length is there a gap of light wider than the glove is thick` | S5 · SPEC göz kapısı |
| D123 | film sıfır kare şiddet taşıyordu; onu yasaklayan cümleler iki doruğu reddettirdi | NEGATIVE'de şiddet/tehlike sözlüğü sıfır. Malzeme TARİF edilir: bağ **çekilir**, kesilmez; asit `an even matte bloom spreading along the opened hem` olarak yazılır | S5 · S7 · 24/24 negatif |
| D169 | 25 sahnelik fiziksel iş filminde zorlanma sözlüğü tek sahnede vardı | Efor kanalı **giysinin yüzeyinde**: `the glove's ribbed segments tighten over the tendons` · `the sleeves pull tight at the elbows`. 0,904 g Dünya gibidir → `normal human pace, real time` yazılır | S2 · S3 · S5 · S7 |
| D216 | üç filmde ses kurguda yapıldı, plana hiç yazılmadı | MUZIK katman tablosu: sahne başına aktif katman ≤4 · her kesmede yoğun karbondioksit oda tonu köprüsü ≥0,2 s · kesmede dijital sıfır sıfır kare | film boyu |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar ve etiketi uymayanlar

> ⚠️ Aşağıdaki iki grup karışmaz. **A grubu** bu filmde uygulanmıyor çünkü
> etiketi filmin malzemesine uymuyor. **B grubu** uygulanıyor ama tavan (20)
> dolduğu için ayrı satır almıyor — çoğu §5.1 negatif çekirdeğinin sekiz
> cümlesinin İÇİNDE zaten taşınıyor, yani filme özel bir karar gerektirmiyor.

**A — etiketi uymuyor, uygulanmıyor:**

| ders | neden bu filmde uygulanmadı |
|---|---|
| [D198] sıfır-g eksensel momentum | yerçekimi 0,904 g · kadrajda yüzen nesne yok |
| [D201] vakumda güneş açısı | vakum yok; kaynaksız kubbe ışığı, güneş diski sıfır kare |
| [D203] replik envanteri | film bilinçli sessiz — SPEC `DIALOGUE LINES: 0`, promptlarda tırnak 0 |
| [D217] replik görüneni söylüyor | replik yok |

**B — uygulanıyor, ayrı satır almıyor (negatif çekirdekte ya da başka kilidin içinde):**

| ders | nerede taşınıyor |
|---|---|
| [D1] tek çekim | çekirdek cümle ① + CAMERA satırı |
| [D34] [D45] [D215] ekran metni · prompt künyesi · araç ayarı | çekirdek cümle ④ + üretim defterinin üç kutusu |
| [D167] kimlik yığını ≤3 | karakter bloğu üç öznitelikle yazıldı; ölçü göreli |
| [D42] [D147] yıpranma | kir GLOBAL bitiş olarak yazıldı; SPEC C tek satır |
| [D176] kontrast garantisi | plakanın rengi TEK cümlede, WORLD bloğunda |
| [D174] yön nesneye bağlı | yön cümleleri perçin ve mandal adıyla yazılıyor |
| [D172] taşıyıcının askısı | sarkan hiçbir şey yok — bağ çıkarıldıktan sonra iki elde, serbest uç bırakılmıyor |
| [D208] kimlik dizisi | SPEC C tek satır (kask 24/24 kapalı · amblem 0 · şerit SOL · kir S5'ten) |
| [D212] ardışık aynı vuruş | vuruş sütununda ardışık tekrar 0 |
| [D180] planlı sessizlik | planlı mutlak sessizlik YOK; AUDIO satırı hiçbir klipte boş değil |
| [D78] sayaç tek karede | ölçek sayacının iki ucu S3'te aynı karede (eldiven ↔ perçin başı) |
| [D62] [D70] montajda düşen final | PLAN KESİLEMEZ LİSTESİ + kurgu kapısı üç sayı |
| [D193] ışık takvimi | ⚠️ yön+Kelvin yerine TEK parlaklık dizisi — gerekçe `02_KONSEPT` §ışık |
| [D16] yüz morph | yüz yalnız K19'da kadrajda; o tek klipte tek blok cümle, morf yüzeyi 1/24 |
| [D44] ağır çekim tuzağı | D169 satırının içinde (`normal human pace, real time`) |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| LOSS_OF_LIFT | ⭐ mod V'nin meşru okuması | **"sayaç semantiği geç kuruluyor"** — pirinç yay S2'de bir kez oynadı, S17'ye kadar hiç; izleyici çentiğin ne demek olduğunu doruğa kadar öğrenmedi | Ölçek sayacı **üç klipte** ilerler ve her ilerleme AYNI kanaldan okunur: S3'te çene boşluğu · S4'te sürüklenme süresi · S5'te şerit altındaki ışık. Üçü de kadrajda aynı iki nesneyle ölçülür |
| LOSS_OF_LIFT | ④ kurgu kapısı | 4:10-4:15 · 5 saniyelik başlık kartı — **8. vaka**; prompt yasağı 25/25 tuttu, kurgu masasında delindi | SPEC B `SCREEN TEXT: 0 s` + kurgu kapısında üç sayı; kapak çıktısı ayrı dizinde durur ve kurgu klasörüne girmez |
| LOSS_OF_LIFT | ④ insan şeridi | sayı ve süre geçti, **sıra geçmedi** — doruk ile insansız viral yuva yer değiştirmiş olabilir | İnsan şeridi 24 hane, hepsi `1` (insansız klip 0) → bu filmde şerit sırayı ölçemez; yerine **DAVRANIŞ ŞERİDİ** ve `ANCHOR BEATS` saniyeleri SPEC'e yazılır |
| THE_CRACKED_HELMET | ⑩ 2,0 · ⑨ 2,1 · ⑧ 1,0 | ölüm-kalım kararı sıfır tereddütle icra edildi · kafiye çifti kırıldı · 11 klibin 6'sında plansız yavaş kayma · 5/5 efor olayında sıfır ödeme | ÇAPA ÜÇLÜSÜ + K01↔K24 birebir kamera cümlesi + `absolutely zero camera movement` her klipte + her efor klibinde saniyeli ödeme |
| THE_CRACKED_HELMET | ② 2,0 · 4,0 | siyah ↔ beyaz giysi 12 sahnede 5 kez değişti; amblemler omuz ile sırt arasında ışınlandı; tamir edilen vizör çatlağı finalde sıfırlandı | Amblem SIFIR (0 yama) · tek renk bandı SOL pazu ve SOL uylukta 360° sarılı · açılan bağ deliği S5'ten sonra üç sahnede konumlu düz cümleyle birebir |
| THE_STATIC_SHADOW | ③ + ㉓ | SPEC yedi makine repliği ilan etti, 30 promptun hiçbirinde tırnak yoktu; ③ SES buna 9/10 verdi | SPEC `DIALOGUE LINES: 0` yazar ve promptlar 0 replik taşır — ilan ile gövde birbirini tutar. SPEC'in yedi makine çapası tek tek doldurulur |
| THE_LOCKED_PULSE | ⑤ + ① | 12 mercek geçersiz: kesme yayılımı 7 > 1, master ölçülmemiş, SPEC vardı ve mod V koşuldu | SPEC **ayrı dosya** olarak yazılır (plana gömülmez) ve QA'da rubriğe yapıştırılır; master ölçülmeden hiçbir skor tabloya girmez |
| THE_LOCKED_PULSE | reform ölçümü | 126/126 çizelge satırından "kilit" çıkmış, `—` sıfır (sahte işaretleme); 25 sahne × 120 satır çalışma dosyası; klasör 747 KB, üretim 0 kare | Bu filmin çizelgesinde 5 satır meşru `—`; sahne çalışması TABLO + 5 kilit klip dosyası; kilit tavanı 20 |
| THE_DRY_ANCHOR | ⭐ SPEC göz kapıları | SPEC'te 12 madde, her biri TEK KAREYLE kapanır ve saniyesi yazılı: *"64,0 s'de bir çizgi · 84,0 s'de ikinci · 114,0 s'de birleşmiş"* | Aynı biçim alınır: THE_COUNTED_RIVET'in SPEC'i **göz kapıları** taşır ve ölçek sayacının üç kademesi saniyesiyle yazılır |
| THE_DRY_ANCHOR | ①.9 teslim kapısı | plan 14 sahne, raporlar 13/12/11 sahne bildirdi — eksik sahne teslim edilmeden kesme listesi uygulanmaz | Kurgu kapısı üç birimi ayrı sayar: SCENE 7 · SHOT 24 · CLIP 24; üçü eşit değil, üçü de ölçülür |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **PB** | **bedenden bir şeyin çıkarılması** (kask/eldiven) | sahne baştan yazıldı: nesne sahneye ZATEN çıkmış girer, kimse hiçbir şey çıkarmaz; vuruş başka nesneye taşındı | ⛔ **S5 · 1 numaralı red riski.** Sahip onayıyla taşındı: şerit artık PLATFORMUN örtüsündedir, giysiye dokunulmuyor ve kesme yok — bağ ÇEKİLİYOR |
| **PK** | şiddet/tehlike sözlüğü, yasak olarak yazılmış bile olsa | yasak satırı SİLİNDİ, malzeme pozitif tarif edildi | S5 ve S7'nin negatif blokları: `wound · cut · damage · danger · burn` sıfır kez; asit `an even matte bloom` |
| **PK** | tek kişide yedi kimlik özniteliği üst üste, 25 promptta | kimlik yığını söküldü: boy GÖRELİ, ten/saç/yaş prompt gövdesinden çıktı | karakter bloğu üç öznitelikle yazılır; yüz yalnız K19'da kadrajda |
| **PK** | milliyet ifadesi | satır silindi, yalnız fiziksel tanım | 24/24 promptta milliyet · kurum · gerçek ad · marka sıfır |
| **YR** | insansız sahne + uzun NEGATIVE bloğu | NEGATIVE tek pozitif `Style:` satırına indi | **insansız klip 0** — 24/24 klipte en az eldivenler kadrajda; bu sınıf yapısal olarak kapalı |
| **PB** | yüzsüz izolasyon + kısıtlanmış uzuv (yan yana iki ön kol · tepeden makro) | kamera nesne hizasına alındı, uzuvlar ard arda ve farklı derinlikte dizildi | ⚠️ S5 iki eldiveni yan yana gösteren yakın plandır → kamera **nesne hizasına**, eldivenler ard arda, aralarına parlak çelik şerit |

```
⛔ POLİTİKA KURALI: nesne ADLANDIRILMAZ, FORMU tarif edilir; ve yasak cümlesi de
   YAZILMAZ — karşılığı POZİTİF kilittir. Sınıflandırıcı promptu BÜTÜN olarak okur:
   tek tek masum üç cümle birlikte reddedilebilir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet (tavan 20 · risk 7/14) + 19 satır §1b
QA ARIZASI:         10 adet (5 film kaydı)
RED SINIFI:          6 adet
⛔ EN PAHALI ÜÇÜ:
   ① S5'in politika yüzeyi — "bedenden bir şey çıkarma" sınıfı (3 ölçülmüş red)
     → sahip onayıyla platforma taşındı; yine de en riskli kare S5'tir
   ② ölçek sayacının geç kurulması — LOSS_OF_LIFT'in ölçülmüş zayıflığı,
     aynı ortam kartında, aynı sayaç mantığıyla
   ③ vizör ve mandal çenesi biçim kilidi — referans paneli yazılmıyor,
     D146'nın dört vakasının hiçbirinde metin tek başına tutmadı
```
