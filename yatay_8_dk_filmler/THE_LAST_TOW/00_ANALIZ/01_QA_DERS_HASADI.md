# 🧾 THE_LAST_TOW — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D59** | yasak isim kazanır; "yokluk listesi" modele o nesneyi çizdirir | ⭐ **bu filmin bir numaralı kilidi.** Kaynak kuralı hiçbir promptta YASAK olarak yazılmaz; POZİTİF asimetri yazılır: `bare metal that touches bare metal stays joined; ceramic-coated boots, gloves and fabric do not join` | 48/48 |
| **D78** | sahneler arası anlatım okunmuyor — sayaç tek karede kanıtlanmadı | üç sayaç kadrajda ÖLÇÜLEBİLİR: ışık çizgisinin dikişe mesafesi (metre) · dikişteki açıklık (parmak genişliği) · kesicinin kemer yuvasında olup olmaması | S1-S12 · her sahnede en az biri |
| **D84** | nicelik (kir, hasar, toz seviyesi) metinle tutulamıyor | nicelik klip içinde SABİT; artış yalnız SAHNE SINIRINDA yazılır ve yeni sahnenin ilk klibinde yeni değer olarak durur | sahne sınırları: S1↔S2 … S11↔S12 |
| **D127** | ivme yazılınca model hızlandırıyor | ivme sayısı YAZILMAZ; düşüşler SÜRE + MESAFE ile yazılır (1,40 m → 0,97 s · 0,60 m → 0,63 s @ 0,30 g) | S8 · S10 · S11 |
| **D138** | metin yasağının KAPSAMI eksik — ölçü ve seri işareti zemine basıldı | ⭐ bu filmin zemini **işlenmiş metaldir** ve modelin numara basmaya en yatkın olduğu yüzey burasıdır. Pozitif karşı cümle her prompta: `the only marks on the metal are weld seams, rivet lines and meteorite pits` | 48/48 |
| **D139** | düz sırt kilidi yalnız sırt görünmezken tutuyor | sırt görünen her klipte: `the back of the suit is one continuous sculpted surface from collar to hip, closed and smooth` + sırt ünitesi yasağı negatifte | sırt görünen 9 klip |
| **D141** | klip var, vuruş yok — twist ve döngü ekranda yoktu | **kafiye çifti K01 ↔ K48**: aynı kurulum, aynı mercek, aynı yükseklik; tek fark ışık ve resifteki yeni işaret. Bu çift SPEC B'ye yazılır, niyette kalmaz | K01 · K48 |
| **D146** | "seamless visor" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı | vizör SAYIYLA: tek düz ön pane, 22 × 14 cm, kalın koyu gri çerçeve içinde, yüz camdan tamamen okunur. ⚠️ referans paketi yazılmadığı için biçim kilidi YALNIZ metinle tutuluyor → ilk iki klipte elle kontrol | 48/48 · kontrol K21 ve K43'te |
| **D151** | filmin novum vuruşları ekrandaydı, mercekler göremedi/ters okudu | ⭐ **§3.8'in park edilmiş ders adayının karşılığı.** Kural her sahnede bir **POZİTİF OLAYLA** kanıtlanır (kopan dikiş · kopan bot · kapanan açıklık · yapışan kafa) — hiçbir sahne kuralı yalnız bir YOKLUKLA kanıtlamaz | S1'de bir, S7-S11'de dört |
| **D157** | novumun taşıyıcısı TEK KARE testini geçmiyor | TEK KARE cümlesi taşıyıcının ADINI taşıyor: *"uçan bir levhanın üstünde dik duran çelik anahtar"* | K01 · K03 |
| **D167** | yedi kimlik özniteliği üst üste = ünlü tarifi (red defteri #15) | kimlik DÖRT öznitelik, her promptta aynı sırada; boy · ten rengi · saç · yaş **0 promptta** (PLAN'da kalır) | 48/48 |
| **D175** | "through the glove" deriyi çizdirdi | çıplak deri 0 kare; her uzuv adının ±12 kelimesinde bir örtü adı (`sleeve` · `cuff` · `glove` · `ring` · `shell`) | 48/48 |
| **D193** | ışık takvimi ölçülmedi — şeritler klip içinde geri yandı | ⭐ **filmin omurgası.** Yıldız yüksekliği 12 sahnede TEK YÖNDE artar (S1 −2° → S12 +9°) ve hiçbir sahnede geri dönmez; her sahnenin ışık satırı derece ve gölge uzunluğu taşır | S1-S12 · sahne başına bir satır |
| **D201** | vakumda güneş açısı komşu sahnede flip etti | tek yıldız, tek azimut (sahne boyunca kadrajda aynı yönden); yükseklik yalnız ARTAR | 48/48 |
| **D202** | merkezî seçim ve bedel bedende okunmuyor | K43'te seçim bedende: eldiven kesiciyi BIRAKIR ve kesici kadrajda dikişte kalır, el boş olarak geri çekilir | K43 |
| **D206** | bedel bedende ödenmiyor — 7 film | bedelin bedendeki izi: K44'ten sonra kemerdeki kesici yuvası BOŞ ve 5 klipte görünür | K44-K48 |
| **D207** | şok/yorgunluk kesmede sıfırlanıyor | sahnenin 2.+ klibinde `CONTINUOUS ACTION:` satırı (IMAGE ve VIDEO), sıfırlanamayanlar listesiyle: poz · eldeki nesne · kir · kapak durumu · yorgunluk | 36 klip |
| **D209** | dünya çapası yok — gök/ufuk/yer imi her sahnede başka | üç çapa cümlesi film boyu birebir: GÖK boş siyah · UFUK regolit sırtı · İM resifin sırtı | 48/48 |
| **D213** | aksiyon elipsi — temas/değişim/sonuç kadraj dışı | temas iki klibe bölünür: N hazırlık (temas yok ya da ilk 2 s'de kurulu) · N+1 sonuç; hiçbir klipte temas "oluşmaz" | S4 · S6 · S9 · S11 |
| **D215** | ekran metni/filigran/konuşan ağız araç ayarıdır | üç kutu üretim defterinde, ilk klipten ÖNCE işaretlenir: altyazı KAPALI · filigran YOK · konuşan ağız kadraj dışı | ÜRETİM DEFTERİ |

**DERS KİLİDİ: 20 / 20 (tavan dolu).**

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D34 · jenerik metni | D138'in kapsamı bunu içeriyor (ekranda 0 karakter); ayrı kilit satırı tavanı boşa harcar |
| D45 · prompt iskeleti sızıyor | aynı gerekçe: D138'in metin yasağı + araç ayarı kutusu (D215) ikisi birden kapatıyor |
| D210 · kafiye çifti ve lockoff niyette kaldı | D141 satırı kafiye çiftini zaten SPEC'e bağlıyor; `locked-off` kelimesi 48 CAMERA satırının hepsinde |
| D124 · klip süresi | kilit değil ÖLÇÜM RANDEVUSU — `02_KONSEPT_VE_RISK`'te ⬜ açık madde olarak duruyor, araçtan ölçülecek |
| D203 · D217 · D180 | replik 0 — bu filmde tetiklenmiyor (D180'in sessizlik yasağı MUZIK dosyasında kaydedildi) |
| D198 | sıfır-g yok; 0,30 g tek rejim (D200 satırı bunu zaten kilitliyor) |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| **THE_COLD_WELD** | ① ② ③ ④ ⑤ ⑥ · altısı | ⭐ **altı merceğin altısı filmin kuralını adlandıramadı.** ⑥ FLAGS rakip bir kural önerdi: *"Is the wrench supposed to be highly MAGNETIZED?"* Park edilen hipotez: o filmdeki bütün kanıtlar YOKLUKtu (düşmeyen anahtar · kalkmayan avuç · kaymayan levha · yapışmayan bot) ve video "bir şeyin olmaması"nı "hiçbir şey olmaması" diye render ediyor | kural her sahnede bir **DEĞİŞİMLE** kanıtlanır: S7 dikiş KOPAR · S10 botlar KOPAR · S11 açıklık KAPANIR · S11 kesici YAPIŞIR. Hook'taki dik anahtar (yokluk kanıtı) tek başına bırakılmaz — K03'te aynı anahtar TEKMELENİR ve kaymaz yerine **saplanıp kalır** (kartın (c) kanıtı, pozitif olay) |
| **THE_COLD_WELD** | ② DEVAMLILIK | filmin ANA SAYACI (avuç disklerinin kararması: 2 → 1 → 0) hiçbir mercekte görünmedi; ② pasaportu eldiveni 14/14 sahnede "değişmedi" diye yazdı | sayaç küçük bir prop detayı olmayacak: ① ışık çizgisi **kadrajın yarısını** kaplayan bir sınır · ② dikişteki açıklık yakın planın konusu · ③ kesicinin yokluğu bir SİLUET farkı (kemerde boşluk) |
| **KRONOS_SON_SINYAL** | ⑫ HOOK | **"LEAVES AT 00:48"** — 0:40-1:35 arası art arda şalter/panel prosedür sahneleri izleyici düşüşü yarattı (8 dk hattının ölçülmüş orta-bölüm arızası) | ölçüm ve hizalama bloğu (S4-S6 · 2:00-4:00) prosedür olarak yazılmıyor: S4 BAŞARISIZ DENEME (bıçak durur), S5 kötü haber (açı yanlış), S6 BEDEL (çapa kalıcı olarak yapışır). Üç sahnenin üçü de sonuç değiştiriyor |
| **KRONOS_SON_SINYAL** | ⑨ KADRAJ · ⑤ ARKA PLAN | ⑨ **RHYME BROKEN**: ilk kare (iç MCU) ile son kare (dış EWS) kafiye kurmuyor · ⑤ 4 kollu AI filigranı 0:00-4:00 tüm sahnelerde | kafiye çifti K01↔K48 planda ve SPEC'te sayıyla (aynı mercek, aynı yükseklik, aynı mesafe) · filigran araç ayarı kutusuyla kapatılıyor ve köşe testi SPEC E'ye yazılıyor |
| **THE_FROST_LINE** | ⑪ ölçüm | **iki sahne EKSİK üretildi** (S12 · S23) ve biri kuyrukta kayboldu; altı mercek ses kanalını "yok" sandı, ölçüm −21,5 LUFS buldu | üretim defteri klip başına satır taşıyor (48 satır) + teslim satırında SHA-256 ve ffprobe çıktısı; `sahne_kapisi.sh` çıktısı ⑬'e verilmek üzere saklanıyor |
| **THE_ROSE_COAT** | ④ HİKAYE 2,3 | duygu yayı **1/10**: 13 sahne olay taşıyordu, seçim taşımıyordu; ④'ün kesme listesi filmin doruğunu ve kapak karesini kesiyordu | 12 sahnenin 12'si ya SEÇİM ya BAŞARISIZ DENEME; S4 ve S9 bilerek başarısız. SPEC A'ya "bu filmin doruğu K43'tür, kesilmez" satırı |
| **THE_BORROWED_WEIGHT** | ② DEVAMLILIK | taşınan yükün KONUMU cümlede yoktu, yalnız varlığı vardı → yük sahneler arasında yer değiştirdi | prop çapası: kızağın, kesicinin ve ikinci giysinin konumu göründüğü her klipte AYNI kelimelerle yazılır |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **YR** yapısal red | insansız sahne + uzun `NEGATIVE:` bloğu + "Exactly 0 human figures" | NEGATIVE kısaltıldı, tek pozitif `Style:` satırına indi | **K01 · K02 · K03** insansız (resif + anahtar). Bu üç klibin negatifi KISA yazılır ve "0 insan" cümlesi kurulmaz — `No people, no figures, no silhouettes of people.` |
| **PB** kompozisyon | **bedenden bir şeyin ÇIKARILMASI** eylemi (kask çıkarma) — sözlükle çözülmedi, sahne baştan yazıldı | eylem hiç yapılmadı: nesneler baştan ayrı | ⭐ **S8-S11'in tamamı.** Çözüm tasarımdadır: kabinden çıkarılan şey bir BEDEN değil, **mühürlü ve ayakta duran ikinci bir basınç giysisidir** — film hiçbir yerde beden/ölü/gövde demez, giysinin vizörü koyu ve okunmazdır, yüzü yoktur. Böylece `Exactly one human character` cümlesi 48/48 promptta DOĞRU kalır |
| **PK** kelime | `dead` · `body` · `corpse` · `decay` — negatif blokta bile tetikledi (SLOW STONE · LAST SPAN) | sözlük tamamen arındırıldı, malzeme TARİF edildi | yukarıdaki kararın sözlük ayağı: `a sealed second pressure suit, upright, its visor dark` — bu altı kelimenin hiçbiri listede yok |
| **PK** kelime | yedi kimlik özniteliği üst üste → "public figure" sınıflandırıcısı | kimlik yığını söküldü, yüz yalnız konu olduğu sahnelerde tarif edildi | kimlik 4 öznitelik; yüz yalnız 6 klipte tarif edilir, 42 klipte vizör `optically clear` der ve durur |
| **PB** kompozisyon | yan yana iki ön kol + tepeden makro + yüzsüz izolasyon → **SAHNE İPTAL** (sözlük yetmedi) | kadraj değişti: nesneler ard arda, ray hizası | **K43** (dikişe sokulan kesici) tepeden makro yazılmaz: 85 mm, 0,48 m, alçak-25° açı — eller ard arda, ufuk kadrajda |
| **TK** teknik | aynı oturumda 0 başarı → sebep prompt değil üretim tarafı | 3. yeniden yazımdan ÖNCE PROB koşusu | üretim sırası kuralı: ilk kabul satırı K43 değilse ikinci klip üretilmez |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet  (tavan dolu · 6 satır §1b'de gerekçeyle bekliyor)
QA ARIZASI:         7 adet   (5 film kaydından)
RED SINIFI:         6 adet   (YR 1 · PB 2 · PK 2 · TK 1)
⛔ EN PAHALI ÜÇÜ:
   ① KURAL EKRANDA OKUNMUYOR — §3.8'in tek filminde altı merceğin altısı kuralı
     adlandıramadı; sebep bütün kanıtların YOKLUK olması [D151 · D59]
   ② İKİNCİ GİYSİ POLİTİKA YÜZEYİ — "bedenden bir şey çıkarma" sözlükle çözülmeyen
     tek sınıf; çözüm tasarımda (giysi bir nesnedir, beden değildir) [red #3 · #8 · #11]
   ③ İŞLENMİŞ METAL ZEMİNE BASILAN METİN — modelin en yatkın olduğu yüzey [D138]
```
