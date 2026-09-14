# ⚠️ THE_BENT_GRASS — UYARI NOTLARI

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
| 1 | S0 · S13 | D73 · THE WRONG SHADOW (novum hiç render edilmedi → hikâye 3.0) | Filmin novum'u tek görsel olguya bağlı: ezilen otun dalgayla hareket ETMEMESİ. Render edilmezse 14 sahnenin 14'ü boşa yazılır | Novum bir DURUM DEĞİŞİMİ değil, bir HAREKETSİZLİK olarak yazılır: "the flattened line does not move while the wave crosses it" — kadraj içinde başka her şey hareket eder. İPTAL KAPISI 1 buraya bağlı | ✅ yazıldı |
| 2 | S5 · S7 · S11 · S12 · S13 | D2 · D18 · THE MIRROR FAUNA 00:20 (bacak yüzeyde kaydı) | Dört ayaklı canlının lokomosyonu deponun ölçülmüş en pahalı arızası | Her canlı promptunda: "each leg lifts clear of the grass and sets down again, one at a time; the body rises and falls with the step" + temas kanıtı (bastığı yerde ot ezilir). ⛔ "walks / moves across" tek başına YAZILMAZ | ✅ yazıldı |
| 3 | S5 · S7 · S11 · S12 | D192 · ADAY-8 · MIRROR FAUNA (uzuv sayısı 4-6 arası oynadı) | Uzuv sayısı ve gövde sayısı kesmeler arası değişiyor | POZİTİF SAYIM: "exactly four jointed legs, one body, one pair of dark eyes low on the front wedge" — 14/14 promptta BİREBİR. ⛔ "no extra limbs" biçimi YASAK (D123) | ✅ yazıldı |
| 4 | tüm iki figürlü sahneler (S1 · S4 · S6 · S7 · S8 · S9 · S10 · S11) | D86 · THIRD DUNE 0:10↔0:20 · ROSE COAT bot rengi | İki gövdenin sol-sağ sırası ve ayrımı kırılıyor | ① dizilim cümlesi: "the RED-STRIPE figure stays on the screen-left side of the pair and the BLUE-STRIPE figure on the screen-right side; their left-right order never swaps" ② ayrım DÖRT kanalda (şerit rengi+kolu · sırt silueti · bilek · eşya) | ✅ yazıldı |
| 5 | S2 (araç kadrajda) · S12 | D69 · D77 · STARLESS CIRCLE S14 · ROSE COAT 2:00 | Biniş/iniş hareketi klon üretiyor | Biniş, iniş, merdiven, rampaya adım: **0 kare.** S12'de rampa KAPALI olarak görünür; kapanma anı kadrajda YOK | ✅ yazıldı |
| 6 | 14/14 | D79 · D95 · D146 · STARLESS CIRCLE (Ekipman 4/10) | Vizör kubbeleşiyor/aynalanıyor, yüz kayboluyor | "optically clear, zero tint, zero mirror coating; the face stays fully readable at every head angle" + "flat back with a single vertical spine seam" 14/14 promptta | ✅ yazıldı |
| 7 | 14/14 | D48 · THE STONE SKY (kanyon planda yoktu) · D145 | "grass" Dünya çayırını çağırıyor; model ovaya kanyon/uçurum ekliyor | ① biyom sabiti: tek tür ot, diz hizası, soluk altın-yeşil ② HORIZON LOCK: "flat to the horizon in every direction — no cliff, no canyon, no ridge, no rock outcrop" ③ Dünya bitkisi ADIYLA negatifte | ✅ yazıldı |
| 8 | S10 | 03_PLAN_ONCESI B5 · KALEIDA · RING WALKER (Karakter 4/10 ×3) | Bedel sahne numarası taşımazsa "umursamadım" | BEDEL = kasanın boşaltılması ve ovada bırakılması · **S10** · ekranda tek karede görünür (boş kasa ayakta durur) | ✅ yazıldı |
| 9 | S11 | KART 12 · POLİTİKA §3 imza ⑤ (gövdeye yönelen kuvvet) · red defteri PB | Canlı-insan yakınlığı red sınıfı açabilir | §6'daki nötr kare tarifi birebir kullanılır: hayvan bir gövde boyu ötede DURUR, temas yok, kuvvet vektörü insana yönelmez, kırmızı ton yok | ✅ yazıldı |
| 10 | S12 · S13 | KART 10 · red defteri YR (insansız sahne + uzun NEGATIVE → yapısal red) | İnsansız koda yapısal red profilinde | Koda sahnelerinde NEGATIVE bloğu KISALTILIR; "Exactly 0 human figures" biçimi YAZILMAZ, boş kadraj VARLIK olarak tarif edilir | ✅ yazıldı |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S1 · S12 | D179 · optik aritmetiği | 32 mm/30 m'de figür kare yüksekliğinin %10'u (~108 px) — sınırın hemen üstünde | Mesafe 30 m'nin ÜSTÜNE çıkarılmaz; çıkarılırsa figür okunmaz hâle gelir | ⚠️ izlenecek |
| 2 | S5 | UZAY_USSU §5.3 · D179 | Uzak banttaki sürü ~25 px — birey okunmaz | **Bilinçli**: S5 birey değil HAT gösterir ("one dark unbroken line along the horizon"); sayım S7'ye bırakılır | ⚠️ bilinçli |
| 3 | S4 · S11 | SENARYO_VE_VIRAL §2.4 (⭐VİRAL = YÜZ + HAREKET) | Viral ara sahne yüz taşımazsa kapı düşer | İki viralde de vizör ardındaki yüz okunur + kadrajda tek büyük hareket (dalga / hayvanın adımı) | ⚠️ izlenecek |
| 4 | S8 | D43 · MIRROR FAUNA 01:11 (el-nesne kaynaşması) | Eldivenli el otlara değiyor — temas morfu sıcak noktası | "a clear structural boundary between the glove and the stems — no merging, no phasing; five fingers throughout" | ⚠️ izlenecek |
| 5 | S9 · S10 | D104 · BLACK CRADLE S4 (ışık mıknatısı + frontal refleks) | Araca doğru yürüyüş, baskın ışığa doğru dönme refleksini tetikler | Kamera hedefin yanında değil YÜKSEKTE (F) ve figürler kameraya dönmez; dört kanallı ışık-yön kilidi yazılır | ⚠️ izlenecek |
| 6 | S6 → S7 | D109 · bölüm sınırı da ardışık çifttir | Bölüm sınırında devamlılık kopabilir | S7'nin 0 s beat'i S6'nın son karesindeki gövde pozisyonunu, saatini ve yönünü TEKRAR yazar | ⚠️ izlenecek |
| 7 | 14/14 | D147 · D84 · THIRD DUNE (toz 42 promptta yazılıydı, kırıldı) | Suit yıpranması sıfırlanıyor | Üç kademeli MONOTONİK çizelge (K0 temiz → K1 diz ve manşetlerde gümüş ot tozu → K2 + göğüs ve önkol); kademe DEĞİŞİMİ sahne SINIRINDA | ⚠️ izlenecek |
| 8 | S11 | GOOGLE_FLOW §10 · YANASMA §2.1 | Müzik doruğun başında susarsa sessizlik fark edilmez | Müzik **S10'un son 2 saniyesinde** biter; S11 müziksiz açılır | ⚠️ kurguya |
| 9 | S12 | D141 · FİNAL VURUŞ KANITI | Final vuruşu kanıtsız kalır | Kanıt: **tek karede kapalı gümüş halka + TAM ÜÇ gövde + ayakta duran boş kasa** · 128,0 s | ⚠️ SPEC'e |
| 10 | tümü | D124 · D115 | Izgara elle yazılırsa kesme saatleri tutmaz | Izgara ÖLÇÜLÜR: `olcum_kapisi.sh` · kesme(n) = 10,0 × n; sapma varsa ölçüm hakemdir | ⚠️ üretimden sonra |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D45 · D138 · D155 | Prompt iskeleti ekrana sızıyor (etiket, ölçü, ad) | Prompt gövdesinde köşeli parantez, karakter adı, metre/derece/f-sayısı YOK; kamera MESAFESİ muaf |
| D70 · D72 · D120 (5+ film) | Jenerik/başlık kartı kurguya giriyor | Ekran metni **0,0 sn**; kart kurguya EKLENMEZ; film adı platform başlığında yaşar |
| D83 · COLD BURN (yatak her kesmede öldü) | "Müziksiz" sahne dijital sessizliğe düşüyor | Ortam yatağı TEK PARÇA serilir: kuru ot hışırtısı sürekli zemin; teslimden önce temas bölgesi kulakla dinlenir |
| D129 · D165 (12 film mod V koştu) | SPEC hazır olduğu hâlde çıplak rubrik koşuluyor | QA_SPEC yazılır yazılmaz `rubrik_paketle.sh` koşulur; operatöre PAKET klasörü verilir |
| §3.3 kartının dürüst kaydı | Bu ortamın DOĞRULANABİLİR referans filmi YOK | Bu film o kartın ilk referansı olacak: ortam satırları PLAN'da tek blokta ve SPEC'te sayıyla; ilk ölçümden sonra karta işlenecek |
| D167 · ⑲ | Kişi başına ≥4 öznitelik politika reddi getirdi (SINKING STAKE) | Kişi başına EN ÇOK 3 öznitelik; ayrım biyometriden GEOMETRİYE (şerit · sırt · bilek) |
| KART 8 · ACI_YAYI | Kurulum tekrarları metinle taşınmazsa iskelet ekrana gelmez | Aynı harfin kamera metni BİREBİR kopyalanır + işaret satırı ("the same position, height and lens as Scene N") |
| D157 · D172 | Novum taşıyıcısı adlandırılmazsa kaybolur | Taşıyıcı nesnenin adı ("the flattened silver line") 14/14 promptta geçer |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | ✅ **VAR ve referans paketi YAZILMIYOR** — risk tam üstümüzde | Üç kilit metne indirildi ve 14/14 promptta BİREBİR: anatomi sayımı · vizör/sırt cümlesi · rol şeridi. Üretimde ilk üç klip yan yana bakılır (⑨ kare çıkarma göz kapısı) |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT | ✅ VAR — filmde ot ve giysi kumaşı birlikte | Ot için `fabric/cloth/blanket` YAZILMAZ; ot POZİTİF ve KATI adla: "stiff dry stalks". Giysi için "sealed suit surface" — dalgalanan kumaş tarifi yok |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ✅ YAPILDI — B 60 m'den 30 m'ye, G 5 m'den 7 m'ye çekildi | Sahne başına kesir `05_SAHNE_CALISMALARI/`'da; ana nesne ≥%10 kare yüksekliği (≥108 px) |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | ✅ VAR — S5'te sürü ~25 px | **Bilinçli**: S5 birey değil HAT gösterir; birey sayımı S7'de (90 m · ~111 px) yapılır |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | ⚠️ KISMEN — film tamamen GÜNDÜZ, renk okunur | Yine de renk TEK kanal değil: sırt silueti (düz ↔ tek dikdörtgen paket) + bilek (kronograf ↔ çıplak) + eşya (kasa ↔ yok) ayrımı taşır. Gri tonda da ayrışır (⑦b) |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | ✅ VAR — geniş ova + iniş aracı maket okumasına açık | Her geniş plana: "no tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame; the far edge of the plain is as sharp as the near grass". ⛔ Vakum negatif bloğu YAPIŞTIRILMAZ |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ✅ önlendi | ZAMAN teması ÜÇ sahne indeksiyle: S2 (dört gümüş kare = geçmiş bir iniş) · S8 (kalkmayan saplar) · S13 (aynı iz, başka ayak) |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ✅ önlendi | BEDEL · **S10** — kasanın boşaltılması ve bırakılması; sonucu S12'de ayakta duran boş kasa olarak GÖRÜNÜR |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | ✅ risk VAR (canlı + yakınlık) | Yasak cümlesi hiçbir promptta yok; karşılığı POZİTİF kare tarifi (§1 satır 9). NEGATIVE bloğu politika sözcüğü TAŞIMAZ |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | ✅ önlendi | Canlı `alien/creature/beast` diye adlandırılmaz; FORM yazılır: "a four-legged grazing animal, dark charcoal-violet, shoulder just above the standing figure's helmet" |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ❌ **BU FİLMDE YOK — gerekçe:** 0 replik | Yerine sahne başlangıçları formülle: sahne(n) = 10,0 + (n−1)×10,0; SPEC'te hesaplatılır |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | ✅ **BU FİLMİN EN BÜYÜK YAPISAL RİSKİ** | Değişimler SINIRA taşındı: iz oluşumu S0↔S1 sınırında · sürünün yaklaşması S5↔S7↔S11 sınırlarında · yeni hattın oluşması S9↔S10 sınırında · rampa durumu S11↔S12 sınırında. Klip İÇİNDE hiçbir nesne durum değiştirmez |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | ✅ önlendi | 14 promptun 14'ü self-contained; karakter/ova/canlı blokları tam ve birebir tekrar eder |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | ⚠️ SPEC yazılırken | E bloğundaki her kapı KURU KOŞUYLA doğrulanır (`ffmpeg -hide_banner -filters \| grep -q " <filtre> "`), DOĞRULANDI satırı + İKAME yazılır |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | ✅ VAR — eldiven/manşet sınırı S3 · S8 · S10'da kadrajda | Üç bölge tek satırda ve bölünmeden: "no bare skin at the wrist, no bare skin at the neck, no bare skin at the ankle — the suit is sealed at every joint" |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT · A5 | ✅ SAYIYA çevrildi | 1 numaralı risk = canlı anatomisi/lokomosyonu → "exactly four jointed legs, one body, one pair of eyes; each leg lifts and sets down one at a time" (4 · 1 · 2 · birer birer) |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (10/10 ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (10 satır)
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 — "yok" cevabı
  tek satırda ve gerekçeli: madde 11, film sessiz)
→ üçü de ✅ → 05_SAHNE_CALISMALARI/ açılabilir
```
