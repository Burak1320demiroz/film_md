# 🎬 THE SINKING STAKE — FİLM KAYDI

**Tarih:** 02.09.2026 · **Format:** yatay 3-5 dk · **Durum:** ⛔ ÜRETİM YARIDA DURDU

---

## ⛔ ÖZET — ÜÇ AYRI ARIZA ÜST ÜSTE BİNDİ

```
① ÜRETİM  · yeni bir POLİTİKA REDDİ üretimi durdurdu (red defteri vaka 15)
② SIRA    · referans paketi (RA/RB/RK1/RK2/RG) HİÇ ÜRETİLMEDİ → çapa yok
③ ÖLÇÜM   · 8 merceğin 8'i MOD V koştu → parti T tablolarına GİREMEZ [D129]
```

Sahibin değerlendirmesi (02.09.2026): *"filmin hikayesi saçma sapan, ne bir
mantıklı ilerleme var ne de sahneler arası devamlılık."*
⛔ Bu cümle kaydedilir ve mercek skoruyla ÇÜRÜTÜLMEZ [D158 emsali].

---

## 🚦 KAPI KOŞUSU

### ⑪ ÖLÇÜM KAPISI — ⛔ KOŞULAMADI
```
Master depoda YOK. `find . -iname "*SINKING*" (mp4|mov|mkv)` → 0 sonuç.
SONUÇ: raporların SÜRE ve SAHNE SAYISI değerleri HİÇBİR KAPIYA girmedi.
       Sekiz raporun sekizi de süreyi "~145 s ESTIMATED" yazıyor — yani
       hiçbiri ölçmedi, hepsi saydı. [D125 · 4. vaka]
⛔ Bu kapı koşulmadan kesme listesi, süre ihlali ve eksik sahne iddiası
  DOĞRULANAMAZ.
```

### ① SPEC KAPISI — ⛔ PARTİ DÜŞTÜ [D129]
```
ls yatay_3_5_dk_filmler/THE_SINKING_STAKE/*_QA_SPEC.md → VAR
Sekiz raporun ilk satırı → INPUT MODE: V  (8/8)

SONUÇ: koşu TEKRARLANIR. Ham raporlar 02/'ye düşer; T2/T3/T4/T5/T6
       tablolarına SATIR YAZILMAZ; kesme listesi, REMOVE reçetesi ve
       yeniden üretim önerileri UYGULANMAZ. ŞARTLI diye almak da yasak.

⭐ SEBEP ZİNCİRİ — ve zincirin ilk halkası YAZIM TARAFINDA:
   `QA_PROMPTLARI/FILME_OZEL/THE_SINKING_STAKE/` YOK.
   AGENTS.md Kart A "⛔ QA'DAN ÖNCE, SIRAYLA (01.09.2026)" satırı
   `rubrik_paketle.sh` koşmasını ZORUNLU tutuyor; koşulmadı.
   Paket olmayınca operatörün elinde ÇIPLAK RUBRİK kaldı, çıplak rubrik
   mod V koşar.
⛔ **BU İKİNCİ VAKA.** THE STILL SWARM (01.09) sekiz merceği tam olarak
   bu sebeple mod V koştu ve D165 o gün yazıldı. Ders yazıldı, ertesi gün
   yazılan film onu okumadı — D157'nin deseni, ders → araç kanalında.
   ⚠️ `.claude/skills/yeni-film/SKILL.md` §4 QA_SPEC'te BİTİYOR; paket
     üretimi o dosyada YOK. Ders AGENTS.md'ye indi, SKILL'e inmedi.
```

### ③ KİMLİK KAPISI — ✅ GEÇTİ (metin olmayan iki çapa)
```
çapa 1 · sayısal kilit: sekiz raporun sekizi de 14 kesme + 145 s + 2:20
         başlık kartı bildirdi — kesme yayılımı 0 [D107 ✅]
çapa 2 · vuruş: "hands press into snow" (S8) · "pull cylinder with tether"
         (S13) — ikisi de planın sahne haritasında yazılı
→ eşleşme 2 ✅ · parti ATFEDİLDİ (ama SPEC kapısından düştü)
```

### ④ KURGU KAPISI — ⛔ ÖN KOŞU
```
klip sayısı  14  ↔  SCENE COUNT 25   ✗  Δ = −11
süre        ~145 s ↔ RUNTIME 249 s   ✗  Δ = −104 s
şerit    11111111111111 ↔ 2222222222222221022222120  ✗ (14 ↔ 25 hane)

Δ OKUNDU: eksik olan 11 sahne ARDIŞIKTIR ve filmin SONUDUR (S15-S24
kuşağı + kart). Rapor sahne haritası planla sırayla eşleşiyor:
  rapor S9  "massive circular crater"        = plan S11 THE BOWL (10 m çanak)
  rapor S11 "pull cylinder with tether"      = plan S13 PULLING IT BACK
  rapor S12 "male views female in distance"  = plan S14 THE HORIZON AGAIN
  rapor S13 "CU of male looking forward"     = plan S15 READING IT
→ üretilen malzeme PLANIN İLK ~%60'IDIR, sırası doğrudur, ve
  **MERKEZİ SEÇİM (S19 · 3:09) · DORUK (S21 · 3:29) · TWIST (S24 · 3:59)
  hiç üretilmemiştir.**
⛔ Film boyu kategoriler (Yapı · Duygusal Yay · Final · Retention) SAYI
  TAŞIYAMAZ: var olmayan üçüncü perde ölçülemez.
```

---

## 🔬 BULGU TASNİFİ — mod V'yi hangi bulgu SAĞ ATLATIR

### ⛔ A. DÜŞEN BULGULAR — ⑩ ÖNERME KAPISI: bunlar filmin NOVUM'udur

```
① FİZİK ⑥ · Scale 2/10 · "cylinder is ~2.5 m tall vs ~0.5 m tall" 🔴
② DEVAMLILIK ② · World State 2/10 · "tall pole vs knee-high stump" 🔴
③ HİKAYE ④ · Premise 2/10 · "object of focus changes, viewer confused"
④ AKSİYON ⑦ · Stakes Object 4/10 · "stakes object changes from small
   cased cylinder to large towed mass"

⭐ KAZIK KISALIYOR ÇÜNKÜ FİLMİN TAMAMI BUNUN ÜSTÜNE KURULU.
   Plan: 2,40 m kazık · S1 üçte bir gömülü · S2 yarısı · S3 son üçte biri ·
   S12 devrilir · S13 yatay çekilir. NOVUM: "sıcak olan iner."
   Dört mercek filmin KURALINI en büyük kusuru olarak puanladı.

⛔ FİZİK raporunun kendi kapısı bunu yakalardı:
   `PREMISE REGISTER: none` yazdı — ve rubriğin kendi uyarısı şudur:
   *"if the film has a central behaviour you scored as its worst defect,
     and your register is empty, you have almost certainly scored the
     film's premise."*
   Register boş çünkü SPEC verilmedi. [D166 · 2. vaka]

→ Bu dört bulgunun PUANI GERİ VERİLİR. Mod D koşusunda yeniden sorulur.
```

### ✅ B. AYAKTA KALAN BULGULAR — SPEC'ten bağımsız, gerçek

```
🔴 EFOR ⑧ · 1,6/10 "NOBODY PAYS" — 4 efor olayı, 4'ünde de STRAIN SHOWN: none
   ⭐ BU YAZIM KUSURUDUR VE BENİMDİR. 25 sahnelik bir fiziksel iş filminde
     TIMELINE satırlarına zorlanma kanalı neredeyse hiç yazılmadı. Yalnız
     S13 "hard working breath / shoulders low" taşıyor; S0 · S5 · S8 · S13 ·
     S20 · S22'nin hiçbirinde önkol gerilmesi, kavrama titremesi, eldiven
     direnci, öne yüklenme yok. Kütle 0,40 g'de azalır, ATALET AZALMAZ.
   → mod D koşusunda da düşmez. Prompt tarafında düzeltilir.

🟠 DEVAMLILIK · göğüs paketi tasarımı S13'te değişiyor (iki kare cep →
   üç yatay kaburga) — KOSTÜM SÜRÜKLENMESİ.
   ⭐ REFERANS_PAKETI tam bunu önlemek için yazılmıştı ve HİÇ ÜRETİLMEDİ.

🟠 ARKA PLAN · S4 ve S10'da AĞIR DAİRESEL YILDIZ İZLERİ; diğer sahnelerde yok.
   ⭐ Sabit kamerada + kilitli dönüşlü gökte yıldız izi FİZİKSEL OLARAK
     İMKÂNSIZ. Bu saf üretim halüsinasyonudur, tasarım değil.

🟠 FİZİK · iki yerçekimi: kar ~1,0 m/s² ↔ patlayan döküntü ~0,2 m/s²
   ⭐ D154'ün birebir öngördüğü arıza ("her klip kendi yerçekimini atar").
     Planın panzehiri (olayın ilk onaylı karesi referans görsel olur)
     UYGULANMADI — çünkü S0 onayı → referans zinciri hiç kurulmadı.

🟡 KARE · 0:52 el kasa kapağının içinden geçiyor — SPEC'ten bağımsız
🟡 SES · ambiyans 0:30 · 1:00 · 1:30'da tamamen kesiliyor (klip sınırları
   ifşa oluyor) — kurgu tarafında düzeltilir, üretim değil
```

### ⚠️ C. YANIT BEKLEYEN — belgeye sorulacak, bulgu değil

```
· "eclipse ring bazı geniş planlarda yok" → kamera azimutu 000°'den
  saptığında disk kadraj dışına çıkar; PLAN bunu söylüyor, mercek bilmiyordu
· "S7'de kar yağıyor" → planda kar YAĞMAZ, süblimleşir; bu bir üretim
  sapması OLABİLİR, mod D koşusu ayıracak
```

---

## 📐 RAPOR ARİTMETİĞİ — ①.5 elle koşuldu (betik girdisi dosya, rapor sohbette)

```
sekiz raporun sekizinde de Σ ÷ n = yazılan ortalama  ✅
  ① 35,0÷7=5,0 ✅ · ② 58,0÷8=7,25→7,3 ✅ · ③ 23,0÷4=5,75→5,8 ✅
  ④ 30,0÷9=3,33 ✅ · ⑤ 50,0÷6=8,33 ✅ · ⑥ 31,0÷7=4,43 ✅
  ⑦ 40,0÷9=4,44 ✅ · ⑧ 10,0÷6=1,67 ✅
⚠️ TEK SAPMA — ① KARE tally: yazılı 🟠 3, hata kütüğünde 🟠 5
   (0:55 · 1:24 · 1:45 · 1:45 · 1:54). [D161 deseni · 3. vaka]
⭐ D161'den sonraki ilk parti: 8 raporun 8'i kendi aritmetiğinden GEÇTİ.
   Önceki partide 6'nın 5'i düşüyordu. Alet çalışıyor.
```

---

## 🚫 BU KOŞUDAN ÇIKMAYAN ŞEY

```
⛔ T2/T3/T4/T5/T6'ya SATIR YAZILMADI (SPEC kapısı).
⛔ Kesme listesi UYGULANMADI. ④'ün önerdiği kesmeler arasında S4 (planın
  1:10 ölçek kontrastı) ve S2 var; ikisi de plan sahneleri, biri
  🌌 ölçek bütçesinin TEK sahnesi.
⛔ Ders YAZILMADI — aday aşağıda, Kart G'ye girmeyi bekliyor.
```

---

## 🔴 DERS ADAYI — İKİ POLİTİKA KİLİDİ TERS YÖNE ÇEKİYOR

**Kaynak:** THE SINKING STAKE üretimi (02.09.2026) — red defteri vaka 15

```
D79 (06.08.2026) her prompta şunu YAZDIRIYOR:
  "the face is fully readable through it in every frame, at every head angle"
  Sebep: aynalı vizör ve sırt ünitesi iki filmde üretildi; yokluk kilidi
  tutmadı, POZİTİF hâl tuttu.

KART 12 (01.09.2026) şunu SÖYLÜYOR:
  "KASK/VİZÖR → anonimlik/deepfake imzasına yakın okunuyor.
   ✅ Panzehir ZATEN VAR: D79 açık vizör kilidi."
  ve ayrıca:
  "KALABALIK → her yüz ÜNLÜ/yaş/deformasyon için TARANIR."

⭐ İKİSİ AYNI ANDA DOĞRU OLAMAZ.
  Açık vizör KAPALI YÜZ riskini (deepfake/anonimlik) düşürür ve
  TANINAN YÜZ riskini (public figure) YÜKSELTİR. Kart 12 birinci yönü
  biliyor, ikinci yönü bilmiyor ve panzehiri ikinci yönün TETİKLEYİCİSİ.

  Bu filmde ikisi çarpıştı: iki yüz × 25 promptta okunur vizör +
  kişi başına yedi kimlik özniteliği = "belirli bir gerçek kişiyi
  tarif ederek isteme" kalıbı. Model reddetti.

**ÇÖZÜM — YÜZ GÖRÜNÜRLÜĞÜ İLE KİMLİK TARİFİ AYRILIR:**
  ① VİZÖR AÇIK KALIR (D79 korunur) — risk vizörde değil, TARİFTEDİR.
  ② KİMLİK YIĞINI PROMPT GÖVDESİNDEN ÇIKAR. Kesin boy · ten rengi ·
     saç rengi · yaş: dördü de PLAN'da ve REFERANS PAKETİNDE yaşar,
     prompt gövdesinde YAŞAMAZ. Prompta yalnız SİLUET iner.
  ③ BOY GÖRELİ YAZILIR: "one is a head taller than the other" —
     "one hundred eighty-eight centimetres" hem kimlik özniteliğidir
     hem D138'in ölçü-etiket riskidir.
  ④ YÜZ TARİFİ YALNIZ YÜZÜN KONU OLDUĞU SAHNEDE. Bu filmde 4 sahne
     (göz bütçesi); kalan 21'de vizör "optically clear" der ve durur.
  ⑤ AYIRT ETME YÜKÜ GEOMETRİDE OLMALI, YÜZDE DEĞİL — bu filmde zaten
     öyleydi (göğüs boyunduruğu ↔ düz göğüs), yani yüz tarifi
     21 sahnede HİÇBİR İŞ YAPMADAN sınıflandırıcı yüzeyi üretiyordu.

⛔ BETİK TARAFINA ÖNERİ: prompt_kontrol.py ⑯'ya "kimlik yığını" sayacı —
   aynı cümle bölgesinde ≥4 kişi özniteliği (boy sayısı · ten · saç ·
   yaş · yüz işareti) varsa FIX.
```

---

## ⬜ AÇIK MADDELER

```
⬜ MOTOR sütunu (red defteri vaka 15) — sahip dolduracak, sonradan
   hatırlanamaz [defterin kendi kuralı]
⬜ İLERLEDİ sütunu — red anında mı düştü, ilerleyip sonda mı? [POLİTİKA §1.0②]
⬜ Ham raporlar 02_HAM_RAPORLAR/'a arşivlenecek (kural ④)
✅ ÜRETİM KARARI VERİLDİ (02.09.2026, sahip): **"dersleri çıkart ve filmi
   yarıda kaldı olarak işaretle."** Film KAPANDI; prompt onarımı yapılmadı,
   S16-S24 üretilmeyecek. Üç ders çıkarıldı (D167 · D168 · D169), iki kapı
   kuruldu (⑲ · ⑳), D165'in ikinci vakası kapandı.

⚠️ SONRADAN GELEN — bu koşunun ürünü DEĞİL: film artık başka bir koşunun
   02.09 15:18'de eklediği **⑰ B5 HİKÂYE OMURGASI** kapısından BLOCK alıyor
   ("İSTEK · ENGEL · MUHATAP satırı yok"). O kapı 69 filmin 69'unu düşürüyor
   ve `06_HIKAYE_HATTI_TESHISI.md` ile birlikte gelmiş. Susturulmadı,
   üstüne yazılmadı, burada kayda geçti.
```
