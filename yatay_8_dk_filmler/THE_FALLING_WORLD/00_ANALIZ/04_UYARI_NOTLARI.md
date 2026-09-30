# ⚠️ THE_FALLING_WORLD — UYARI NOTLARI

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
| 1 | S16 | YERÇEKİMİ F1 S8 — deponun TEK ÇÖZÜLEMEYEN reddi (üç yazım, üçü de düştü) | yüzsüz izolasyon + kısıtlanmış uzuv aynı karede; opak vizörün panzehiri (berrak vizör) bu filmde YOK | TURUNCU aynı karede kalır (kompozisyonla izolasyon kapatılır) · sonuç MANŞETTE okunur · ölçek MS ve daha geniş · yara/kan/acı sözlüğü ne pozitifte ne NEGATIVE'de · kanıt S17'de malzemede · iki yenilgide kamera taşınır | ✅ kapatıldı (02 §6 + iskelet L) |
| 2 | S02 · S39 · S42 | 09_URETIM_RED_DEFTERI — PK sınıfı (alet + insan gövdesi yakın kadrajda) | kesici üç sahnede insan gövdesine yakın; red sınıfının tam profili | alet NÖTR adlandırılır · ayrılma anı NESNEDE çerçevelenir (kayış ayrılır ve düşer / sarı kol ayrılır ve düşer) · gövdeye yakın kadraj YOK: S02 = B (0,35 m sandık), S42 = Y (0,08 m halka) — ikisinde de kadrajın merkezi NESNE | ✅ kapatıldı (02 §5 KART 12) |
| 3 | 48/48 | KRONOS_SON_SINYAL — aynı format, İKİ bölümde ikinci figür KOPYALANDI | filmin tamamı iki figürlü; kopyalanma bu deponun 8 dk formatında ölçülmüş | konum kilidi her prompta (BEYAZ sol üçte bir · TURUNCU sağ üçte bir, merkez çizgisi geçilmez) · `Exactly two human characters, no duplicates, no third person.` her NEGATIVE'de · P4 probu ilk gün, kabul edilmeden bölüm üretimi başlamaz | ✅ kapatıldı (03 §4b) |
| 4 | S01 · S04 · S31 · S38 · S42 · S44 | D146 — biçim kilidi METİNLE tutulmuyor (3 kask 1 filmde) | ÜÇ hat aynı kelimeyle okunuyor: ince sarı ortak halat · ince gri sandık kayışı · kalın siyah servis bağlantısı | R3 HAT AİLESİ referans sayfası KAPI 0 · her promptta hattın KALINLIĞI + RENGİ + NEREYE BAĞLI olduğu birlikte yazılır · S38'de üç hat da aynı karede, ayrım AÇIYLA | ✅ kapatıldı (02 §5b) |
| 5 | S41 · S42 | D192 / A5 — 1 numaralı risk yalnız SIFATLA korunmuş | "hangi hat kesiliyor" okunmazsa filmin anlamı TERSİNE döner | A5 beş sayılı kilit (iki kol 20° / 55°, fark ≥35° · halka ≥120 px · alet halkadan 15 cm · üst kola 40 cm'den yakın değil · ayrılan uç 0,5 s) — beşi de VIDEO promptunun gövdesine ve TIMELINE'ına girer | ✅ kapatıldı (02 §5 A5) |
| 6 | S47 · S13 | KART 10 — insansız sahne + uzun NEGATİF blok = yapısal red | S47'de kadrajda insan gövdesi yok; S13'te insan payı çok küçük | bu iki sahnenin NEGATIVE bloğu <900 karakter, çekirdek cümleler kısaltılmış biçimde · insana ait negatif cümleler (çıplak deri · yüz morfu) DÜŞER | ✅ kapatıldı (02 §5 KART 10) |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | 48/48 | D124 · THE_LOCKED_PULSE / SUSMAYAN_NOBETCI açık maddesi | 10 s bir VARSAYIM; motor 10 s vermezse müzik ve bölüm zamanları kayar | ilk kabul klibinde `ffprobe` ölçümü, URETIM_DEFTERI §0'a yazılır; sapma varsa MUZIK saniyeleri + YAYIN_PAKETI bölüm zamanları yeniden hesaplanır | ⬜ üretimde |
| 2 | S11↔S12 · S23↔S24 · S35↔S36 | yatay_8_dk README — QA birimi BÖLÜM | ② DEVAMLILIK merceği bölüm sınırı çiftlerini yarım masterda YAN YANA göremez | üç çift QA_SPEC 🅑 B bloğuna EŞ KADRAJ satırı olarak yazılır ve ELLE kareyle denetlenir (03 §3'te ◆ ile işaretli, üçü de bant içi) | ⬜ QA_SPEC'e |
| 3 | S05-S06 · S10 · S13 · S18 · S30 · S35 · S45 | KART 6 · §3.2 ince atmosfer | toz VAKUM gibi davranırsa (asılı kalırsa) ortam kartı bozulur; perde olursa kadrajı yer | toz SÜTUN hâlinde ve 0,30 g'de YAVAŞ ama KESİN oturur; miktar sayıyla yazılır (ör. "three dust columns"), "cloud of dust" YASAK | ⬜ prompt yazımında |
| 4 | S07 · S33 | KART 5 — ekran/sayaç/metin | gösterge rakam üretirse ㉑ okunur metin kapısı düşer | gösterge tek RENK lekesi (S07 kırmızı · S33 iki yeşil); NEGATIVE'de okunur metin yasağı zaten çekirdekte | ⬜ prompt yazımında |
| 5 | S14-S18 · S33 · S40 · S43-S46 | KART 6b — katmanlı dünya, ışık takvimi | altı palet arasında ışık sıçraması; güneş yönü bölgeler arası kayarsa dünya bölünür | güneş yönü film boyu SABİT (sol üstten, kadraj dışı) · galeri tek sarı servis lambası + yarıktan tek dilim · kabin kendi 4500K kaynağı; her promptta ışık YÖNÜ yazılır | ⬜ prompt yazımında |
| 6 | S20-S22 · S25-S28 | KART 13 — yapı ölçeği ve tekrar eden birim | devrilmiş kafes direk maket okunursa sahne çöker | birim sayıyla kilitli: kafes gözü 0,6 m · direk 14 m · sekiz bölüm · insan boyu daima referans; "no miniature read" negatifi her dış kurulumda | ⬜ prompt yazımında |
| 7 | S00 · S17 · S29 · S41 · S43 · S46 | D196 + KART 12 — temas yalnız bedel sahnesinde | 6 temas sahnesi kural sapmasıdır | sapma D74 olarak kayıtlı (02 §7b altı · 03 §4b TEMAS ENVANTERİ); her temas sahnesinde SINIR CÜMLESİ (eldiven kabuğu ↔ sert manşet, sıfır ten) | ✅ kayıtlı, üretimde ölçülür |
| 8 | S40 | D202 kalıbı — kadrajda olmayan ikinci insan | AYRILIK sahnesinde BEYAZ kadrajda yok; ikinci insan "yok" okunabilir | telsiz sesi + GERGİN sarı hat kadrajın alt kenarından çıkar (ikinci insanın FİZİKSEL izi kadrajda kalır); ayrıca kadrajda BOŞ KOLTUK | ⬜ prompt yazımında |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| §5.2 opak vizör dalı | D79 vizör cümlesi ile ÇELİŞKİ — iki karşıt cümle aynı prompta girerse model ikisini de yarım uygular | D79 cümlesi HİÇ yazılmaz; her promptta TEK pozitif cümle: vizör tamamen opak, hiçbir açıdan yüz/göz/ten yok. `IN FRAME:` satırına `face` yazılmaz |
| Politika imzası ⑥ (yüz kapatan ekipman = anonimlik imzası) | panzehiri (berrak vizör) bu filmde kullanılamıyor → imza 48/48 sahnede açık | ÖLÇÜLMÜŞ TELAFİ: her karede ÇEVRESEL ÇAPA — figür daima tanınabilir bir yapı/araç/gemi parçasıyla aynı karede; hiçbir kare "boşlukta yüzsüz gövde" değil. 24 kurulumun 24'ünde çapa optik aritmetiğinde adlandırıldı |
| D169 — basınçlı giyside SIFIR EFOR (KRONOS ⑧ NOBODY PAYS) | 0,30 g'de hareket kolay görünürse bedel okunmaz | her VIDEO promptunda EFOR satırı: yük alan uzuv adlandırılır (S17'den sonra DAİMA sağ kol) + gövdenin karşı hareketi; "effortless" ve "smoothly" sözlükten çıkarıldı |
| D45 — ders etiketi gövdeye yazılıyor | `[LESSON n]` / `[D174]` gibi etiketler prompta sızarsa ㉑ düşer | 20 ders kilidi PLAN'da ETİKETLİ, promptta ETİKETSİZ; kilit metni cümleye dönüşür |
| OMNI 1.1 Flash — tırnak yasağı + tek başlangıç karesi | promptta tırnak kalırsa motor metni ekrana YAZAR | 8 replik post-dub; VIDEO promptunda tırnak YOK, `AUDIO:` satırında replik TARİF edilir · zincir modu ① (tek başlangıç karesi) — mod ② sahip kararına bırakıldı (K2) |
| OMNI — durağan kare kuralı | IMAGE karesi düşme ANINI gösterirse video "donmuş düşüş" üretir | her IMAGE karesi DENGELİ: yerde iki destek noktası VEYA yük almış tek kavrama. S25/S37/S41 gibi asılı sahnelerde kare "tutuş ZATEN yük altında" anını gösterir, düşüşün kendisini DEĞİL |
| SAHNE_DOLULUGU — kilit fiili ACTIVITY/ACCOMPLISHMENT olmalı | 48 kilit cümlesinden biri STATE fiiliyle yazılırsa o klip 10 saniye boyunca durur | yasak sözcükler (still · motionless · frozen · settles · comes to rest · then stops · nothing else moves · waits) tek başına kullanılmaz; her sahnede ÜÇ FAZ (yüklü giriş · direnç · SÜRDÜRME) + tek ortam saati + zemin bağı cümlesi |
| ㉕ KİLİT TAVANI = 20 | 11/14 risk tetiklendi → tavan devrede | PLAN `## 🔒 DERS KİLİTLERİ` bloğu TAM 20 satır; dışarıda kalan 20 kilit `UYGULANMAYAN KİLİTLER`e gerekçeyle (01_QA_DERS_HASADI §1b'den birebir) |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | 🔴 VAR — iki giysi + üç hat + araç + gemi | 4 referans sayfası KAPI 0 (R1-R4); giysi cümlesi her IMAGE promptuna BİREBİR; R1 iki durumlu (hasarsız S00-S15 / bantlı manşet S16-S47) |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | 🟡 RİSK — basınçlı giysi + ince atmosferde rüzgâr yok ama model dalgalandırabilir | `fabric`/`cloth` sözcükleri promptta HİÇ geçmez; giysi `shell` · `panel` · `ribbed section` ile tarif edilir; her NEGATIVE'de sert kabuk cümlesi |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ✅ YAPILDI — 24/24 kurulum | 03 §4 kurulum kartlarında her harfin kesir hesabı yazılı; B ve G mesafeleri hesap SONUCU düzeltildi (0,8→1,2 m · 1,2→2,5 m) |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | ✅ YOK — en dar okuma 112 px | H kurulumu hesap sonucu 300 m'den 60 m'ye çekildi (34 px → 171 px); ana nesne 24/24 kurulumda ≥100 px |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | 🔴 VAR — ayrım RENKLE kurulu (beyaz ↔ turuncu) ve P4 galeri karanlık | ayrım ÜÇ kanalda birden: RENK + OMUZ GEOMETRİSİ (kobalt mavi kare omuz ↔ siyah yuvarlak üst kol) + KONUM KİLİDİ (sol/sağ üçte bir). P4 sahnelerinde (S14-S18) omuz silueti kadrajda daima ışığa karşı |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | 🟡 RİSK — direk, galeri, taş ocağı büyük yapı | "no miniature read, no tilt-shift" her DIŞ kurulumda; hiçbir dış kurulumda yapıya sığ alan derinliği yok |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ✅ YOK — tema 6 sahneye indeksli | GÜVEN motifi S00 · S02 · S24 · S29 · S41 · S46'da nesne indeksiyle (uzatılan el / gerilen hat); B3 ≥3 şartı 6 ile karşılandı |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ✅ YOK — beş bedel, beşi de numaralı | S02 numuneler · S13 araç · S16 sol kol · S41 kendi tutuşu · S43 ortak hat. B5 satırı asıl bedeli S16 olarak taşır |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | 🔴 RİSK — kesici üç sahnede var | kesme/yara/acı sözlüğü NEGATIVE'de BİLE yazılmaz; ayrılma POZİTİF ve NÖTR cümleyle tarif edilir ("the grey strap parts and drops away") |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | 🔴 RİSK — aynı kalem | alet adlandırılmaz, FORMU tarif edilir: "a short flat tool on the outside of his left forearm"; hiçbir promptta kesici sözcüğünün karşılığı geçmez |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ✅ YOK — 8 repliğin 8'i formülle | `replik(S_n) = n × 10 s + TIMELINE ofseti`; 03 §5 tablosunda her satırda hesap açık yazılı |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | 🔴 VAR — 48 klibin 48'inde durum değişiyor | her VIDEO promptunda TIMELINE ≤3 satır ve BAŞ ≠ SON; SAHNE_DOLULUGU üç fazı (yüklü giriş · direnç · sürdürme) her klipte; 9 KÜME klibinde değişim İKİ klibe yayılır |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | 🟡 RİSK — 4 referans sayfası var | referans sayfası ÜRETİM için (başlangıç karesi), METİN için değil: her promptta giysi/araç/hat cümleleri TAM yazılır; "as in the reference" ifadesi YASAK |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | ⬜ ÜRETİMDE — QA_SPEC yazılırken denetlenecek | QA_SPEC'e yazılan her ffmpeg/ffprobe komutu önce `-filters` ile VARLIĞI doğrulanır; doğrulanmayan komut SPEC'e girmez |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | 🟢 DÜŞÜK — bu filmde ten HİÇ görünmüyor | çıplak deri negatifi yine de tam ve TEK satırda; opak vizör + basınçlı giysi sayesinde ten yüzeyi fiziken yok, ama cümle kısaltılmaz |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | ✅ YOK — beş sayılı kilit yazıldı | 02 §5 A5: 20° / 55° / ≥35° / ≥120 px / 15 cm / 40 cm / 0,5 s / 3 s. Beşi de S42 promptunun gövdesine girer, NEGATIVE'e değil |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (6/6 ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (8 satır)
✅ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 — 4 satır 🔴,
   4 satır 🟡, 7 satır ✅/🟢, 1 satır ⬜ üretimde)
→ üçü de ✅ — 05_SAHNE_CALISMALARI/ AÇILABİLİR
```
