# ⚠️ THE_LAST_TOW — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S1-S12 (48/48) | THE_COLD_WELD · altı merceğin altısı kuralı adlandıramadı; ⑥ FLAGS rakip kural önerdi ("anahtar mıknatıslı mı?") · park edilen ders adayı: bütün kanıtlar YOKLUKTU | filmin kuralı ekranda hiç okunmaz; izleyici "hiçbir şey olmuyor" görür | kural her sahnede POZİTİF bir DEĞİŞİMLE kanıtlanır. Dört zorunlu kanıt klibi: K03 (tekmelenen anahtar saplanıp kalıyor) · K25 (kaynak kopuyor) · K37 (botlar kopuyor) · K44 (kafa değiyor ve kalıyor). Hiçbiri kesilemez — SPEC A'ya "bu dört klip kurgudan çıkarılamaz" satırı | ✅ |
| 2 | S8-S12 (K29-K48) | red defteri #3 PB (kask ÇIKARMA — bedenden bir şeyin çıkarılması; sözlükle çözülmedi, sahne baştan yazıldı) + #8/#9/#11 PK (`dead` · `body` · `corpse` negatif blokta bile tetikledi) | kabinden bir insan biçiminin çıkarılması: deponun sözlükle çözülemeyen tek red sınıfı | kabinden çıkan şey bir GİYSİDİR. Sözlük: `a sealed second pressure suit, upright, its visor dark`. ⛔ Film boyunca 0 kez: body · dead · corpse · remains · gövde. ⛔ Eylem "çıkarma" değil "taşıma": giysi düşer, o TUTAR, sonra kızağa BIRAKIR | ✅ |
| 3 | S1-S12 (48/48) | D138 · METİN YASAĞININ KAPSAMI: ölçü ve seri işareti ZEMİNE basıldı · kart §3.8'in kendi uyarısı: "modelin numara basmaya en yatkın olduğu yer işlenmiş metaldir" | zemin işlenmiş metal — filmin 1 numaralı riski | pozitif üç kalem her prompta: `the only marks on the metal are flat weld seams eight millimetres wide, rivet lines forty millimetres apart, and meteorite pits one to twenty centimetres across` + negatifte çekirdeğin metin cümlesi | ✅ |
| 4 | S7-S11 (K25 · K37 · K44) | D24 temas bütünlüğü · kart §3.8: "bağ ATOMİKTİR, GEOMETRİK DEĞİL — iki yüzey ayrı ayrı görünür kalır, aralarında NET sınır vardır; el metale eriyor/batıyor bir ÜRETİM HATASIDIR" | kaynak "erime" olarak render edilirse filmin kuralı yanlış kurulur ve üçüncü perde dayanaksız kalır | her kaynak klibinde pozitif sınır cümlesi: `the two surfaces stay separate with a clean visible boundary between them, nothing melts, nothing sinks in`. K44 iptal kapısıdır — tutmazsa kanıt K45'e taşınır | ✅ |
| 5 | S1-S12 (48/48) | D146 · üç ölçülmüş vaka (SKYLIGHT 1 filmde 3 kask · YERÇEKİMİ F2 · STANDING WIRE 24 klibin çoğunda kubbe vizör) | ⚠️ **referans paketi bu filmde YAZILMADI** (sahip kararı) → biçim kilidi YALNIZ metinde | vizör sayıyla: `a single flat front pane twenty-two centimetres wide and fourteen high, set inside a thick dark-grey rim`. ⛔ `seamless` · `bubble` · `dome` · `wraparound` kelimeleri 0 kez. Üretim kapısı: ikinci klipte kubbe görülürse ÜRETİM DURUR | ✅ |
| 6 | S9-S10 (K34-K40) | KRONOS ⑧ EFOR **WEIGHTLESS WORK** (en ağır 🔴): vakum patlamasında tek elle tutunma sonrası terleme/titreme/solunum değişimi yok; ağır kapı tek elle savrulurken gövde tepki kuvveti yok | 0,30 g'de bir giysinin ağırlığını tutmak "hafif" render edilirse doruk ölür | K40'ta üç kanal birden: omuz hattı 4 cm düşer · önkollar gövdeye yaklaşır · nefes ritmi vizörde iki kez kesilir. Ağırlık SAYIYLA: `the suit's mass presses on her forearms at chest height` + 0,30 g'de düşüş süresi 0,97 s | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S4-S6 (K13-K24) | KRONOS ⑫ HOOK **"LEAVES AT 00:48"** — 0:40-1:35 art arda prosedür sahneleri orta bölümü düşürdü (8 dk hattının ölçülmüş arızası) | bu filmin 2:00-4:00 bandı ölçme ve hizalama işi: prosedür riski | üç sahnenin üçü de SONUÇ değiştiriyor: S4 bıçağın ağzı gidiyor (kayıp) · S5 açının yanlış olduğu anlaşılıyor (kötü haber) · S6 kalıcı bir şey yapılıyor (bedel). ⏱️ ⑫ merceği bölüm 1 masterında ölçecek | ⬜ ölçüm |
| 2 | S1-S12 | KART 9 ışık mıknatısı [D104] · tek baskın ışık + hedefe hareket | kamera ışığa/hedefe yapışır, kompozisyon tek eksene iner | yıldızın diski 48/48 klipte KADRAJ DIŞI; kamera hedefin YANINA kurulur (azimut tablosu bunu zorluyor: 11 kurulumun azimutları 0-330° arasına dağılmış) | ⬜ ölçüm |
| 3 | K01-K02 | red defteri #2 YR — insansız sahne + uzun `NEGATIVE:` bloğu + "Exactly 0 human figures" = yapısal red | filmin ilk iki klibi insansız | bu iki klibin negatifi KISA (çekirdeğin 8 cümlesinden 5'i) ve sayım kurulmaz: `No people, no figures, no silhouettes of people.` | ⬜ üretimde |
| 4 | K43 | red defteri #13 PB — yan yana iki ön kol + tepeden makro + yüzsüz izolasyon → SAHNE İPTAL (sözcük değişimi YETMEDİ, kadraj değişti) | filmin en pahalı karesi aynı kompozisyon ailesine yakın | K43 = 85 mm · 1,1 m · yükseklik 1,25 m · göz hizası. ⛔ tepeden makro YAZILMAZ; eller ard arda değil ÜST ÜSTE değil, biri kadrajın solunda kesici, öteki çerçevede; ufuk kadrajda | ⬜ üretimde |
| 5 | S3 (K10) | D179 · uzak nesne ~60 piksel, ekranda okunmuyor | çekicinin feneri ufukta 18 mm lensle çizilirse okunmaz | fener 18 mm'de 10 m mesafede değil, ufukta tek bir parlak nokta olarak değil, **kenar çizgisinin üstünde 2° yükselen hareketli bir nokta** olarak yazılır; büyüklüğü eldivenin tırnağıyla kıyaslanır | ⬜ ölçüm |
| 6 | S12 (K46-K48) | D62 · montajda en çok düşen sahne FİNAL (×5 vaka) + THE_FROST_LINE: iki sahne eksik üretildi, biri KUYRUKTA | filmin son üç klibi kurgudan düşme riski en yüksek yerde | SPEC A'ya: "kuyruk 30 saniyedir ve filmin BEDELİDİR; K46-K48 kesilemez". ÜRETİM SIRASI K48'i dördüncü halkaya koyuyor — kuyruk erken üretiliyor | ⬜ üretimde |
| 7 | S1-S2 (K01-K07) | KART 6 · metalin üstünde 0 kare toz; toz yalnız regolitte | model metal zemine toz serper, sonra kaldırır | pozitif: `the metal is bare and swept clean by micrometeorite strikes; loose dust lies only on the regolith beyond the plates` | ⬜ ölçüm |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D215 · ADAY-7 kapanışı (ekran metni/filigran/konuşan ağız araç ayarıdır, prompt cümlesi değil) + KRONOS ⑤ (4 kollu filigran 0:00-4:00 tüm sahnelerde) | teslimde filigran ve kuyruk kartı | ÜRETİM DEFTERİ'nde üç kutu ilk klipten ÖNCE işaretlenir; SPEC E'ye köşe testi (`kose_SA.png`) + kuyruk kartı kapısı yazılır |
| D201 · vakumda güneş açısı komşu sahnede flip · D193 · ışık takvimi ölçülmedi | ışık yönü/yüksekliği sahne sahne kayıyor | ⭐ bu filmde ışık bir SAYAÇ: yıldız yüksekliği 2,3°'de SABİT, azimut sabit, hareket eden yalnız GÖLGE KENARI ve o tek yönde. 48/48 promptta aynı LIGHT çatısı, sahne başına yalnız kenarın mesafesi değişir |
| D209 · dünya çapası yok | gök/ufuk/yer imi her sahnede başka çıkıyor | üç çapa cümlesi film boyu birebir: `SKY: flat black, no stars, no gradient` · `HORIZON: a low regolith ridge forty metres high, its top edge sharp` · `LANDMARK: the long spine of the reef running across the frame` |
| D207 · şok/yorgunluk kesmede sıfırlanıyor (THE_AMBER_LATTICE S12→S13 "sudden reset… calm standing posture") | 36 klipte durum sıfırlanması | sahnenin 2.+ klibinde `CONTINUOUS ACTION:` satırı hem IMAGE hem VIDEO'da; sıfırlanamayanlar: poz · eldeki nesne · kir · kapağın durumu · yorgunluk işareti |
| D84 · nicelik sürüklenmesi metinle tutulamıyor | kir/hasar/toz seviyesi sahneler arasında zıplıyor | nicelik klip içinde SABİT; artış yalnız sahne SINIRINA yazılır ve yeni sahnenin ilk klibinde yeni değer olarak durur |
| D167 + red #15 · yedi kimlik özniteliği = "public figure" sınıflandırıcısı | kimlik yığını 48 promptta tekrarlanıyor | kimlik DÖRT öznitelik, aynı sırada; boy · ten rengi · saç · yaş 0 promptta. Ayırt etme yükü GEOMETRİDE (omuz kaburgası + kemerdeki kesici yuvası) |
| D175 + ㉑ · çıplak deri negatifi bölge saymıyor | eldiven-kol arası açık bilek | her uzuv adının ±12 kelimesinde bir örtü adı; negatifte üç bölge tek cümlede: `No bare skin anywhere — none above the collar, none at the wrists between glove and sleeve, none at the ankles between boot and leg.` |
| D110 · aynı oturumda koşulan mercekler birbirinin kopyasını üretiyor | QA tarafı | SPEC'e yazılır: her mercek AYRI ve TEMİZ oturumda; iki yarım mastera AYRI koşu + bölüm beyanı satırı [D129] |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | 🔴 **VAR ve bu filmde en yüksek risk** — referans paketi sahip kararıyla yazılmadı, yani kilit yalnız metinde | vizör dört sayıyla (22 × 14 cm pane · kalın koyu gri çerçeve · düz) + yasak kelime listesi + ikinci klipte elle kontrol · ÜRETİM DURUR kapısı |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT | ⚠️ VAR: giysi çok katmanlı naylon ve vakumda hiçbir şey dalgalanmaz | `fabric` kelimesi geçtiği her yerde durum fiiliyle kilitlenir: `the creased nylon holds its folds and does not move` · rüzgâr 0, hava 0 |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ✅ YOK — 11 kurulumun 11'i lens+mesafe çiftiyle tanımlı | 18 mm/9,0 m EWS'te 40 m'lik sırt kadraja giriyor; 100 mm/0,55 m ECU'da 19 mm'lik sap kadrajın üçte birini kaplıyor. Ölçüler kurulum tablosunda |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | ⚠️ VAR: çekicinin feneri (K10) ve sırtın tepesi | fener hareketli bir nokta olarak, büyüklüğü eldivenle kıyaslı yazılır; sırt siluetinin tepe çizgisi keskin ve kadrajın üst üçte birinde |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | 🔴 **VAR ve ciddi**: S7-S12'de iki gövde (kadın + ikinci giysi) ve ikisi de basınç giysisi | ayrım RENKLE DEĞİL GEOMETRİYLE: kadının omzunda kaburga hattı ve kemerinde kesici yuvası var; ikinci giysinin omzu DÜZ, kemeri YOK, vizörü koyu. Ayrıca kadın hep DİK ve hareketli, öteki hep aynı duruşta |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | ⚠️ VAR: 40 m sırt + 18 m levha dizisi maket okunabilir | negatif çekirdeğin ⑤'i (35 mm grain, no CGI/video-game look) + ölçek çapası: her geniş kadrajda insan gövdesi ya da 56 cm'lik anahtar referans olarak kadrajda |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ✅ YOK | YALNIZLIK'ın motif sahneleri sayıyla: S1 · S4 · S6 · S9 · S11 · S12 (6 sahne ≥ 3 alt sınır) |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ✅ YOK | BEDEL S11 · K43 (kesici) + S6 · K23 (çapa) + S12 · K46 (teslim) — üçü de klip numaralı |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | ⚠️ VAR ve bu filmde en kolay düşülecek tuzak: "kaynamaz" demek | ⛔ kaynak kuralı hiçbir promptta YASAK olarak yazılmaz. Pozitif asimetri: `bare metal that touches bare metal stays joined; the ceramic-coated boots, gloves and outer fabric do not join` |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | 🔴 **VAR**: ikinci giysi | ADLANDIRILMAZ, FORMU tarif edilir: `a sealed second pressure suit, upright, shoulders square, its visor dark` — beden/ölü/kalıntı sözcükleri yok |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ✅ YOK — replik 0 | SPEC A: `DIALOGUE LINES: 0 · RECORDED HUMAN 0`; ㉓ envanteri 0 tırnak sayacak |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | ⚠️ VAR: 48 klibin her biri bir durum değişimi taşıyor | değişim TEK ve KÜÇÜK: klip içinde bir eşik geçilir (bıçak durur · kenar dikişe değer · bir bot kopar), iki değişim aynı klipte yazılmaz. TIMELINE ≤3 satır, son satır SÜRDÜRME |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | ✅ YOK | 96 promptun her biri kendi kimlik dizisini, ışık satırını ve fizik satırını taşıyor; hiçbir prompt başka dosyaya atıf yapmıyor |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | ⚠️ İZLENECEK | SPEC E'nin altı kapısı yazılmadan ÖNCE `ffmpeg -filters` ile varlığı doğrulanır ve çıktı SPEC'e tarihle yazılır |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | ⚠️ VAR | üç bölge TEK cümlede ve satır sonunda bölünmeyecek biçimde yazılır (yaka · bilek · ayak bileği) |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | ✅ YOK | 1 numaralı risk = metal yüzeye basılan metin; pozitif biçimi ÜÇ SAYI taşıyor: 8 mm dikiş · 40 mm perçin aralığı · 1-20 cm çukur |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

### 4b. 🆕 BU FİLMİN AÇTIĞI ADAY SATIR — şablona önerilecek

```
ADAY: "KURALIN BÜTÜN KANITLARI YOKLUK — video 'olmayan bir şeyi'
       'hiçbir şey' diye render ediyor"
KAYNAK: THE_COLD_WELD (01.09.2026) · altı mercek / altı kaçırma; park edilmiş
        ders adayı hâlâ ⬜ AÇIK (master gelmedi)
NEDEN ADAY: ikinci vakası bu film olacak ve bu film karşı önlemi TASARIMDA
        aldı (dört pozitif kanıt klibi). İki vaka olunca satır tabloya girer.
⛔ Bugün DERS YAZILMAZ: THE_COLD_WELD partisi askıda (geçersiz master) ve
  ② defterinde 9 ⬜ AÇIK madde var; bulgudan ders yazmak yasak.
```

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının 6/6'sı kapatıldı (durum ✅)
☑ 🟡 ⚠️ satırlarının 7'si QA_SPEC'e ölçüm olarak taşınacak şekilde ⬜ işaretlendi
☑ tekrar eden arıza tablosunun 16/16 satırı cevaplandı (3 satır 🔴 VAR ·
  6 satır ⚠️ VAR · 7 satır ✅ YOK, her biri gerekçeli)
→ üçü de ✅ → 05_SAHNE_CALISMALARI/ açılabilir
```
