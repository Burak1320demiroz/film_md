# 📚 YERÇEKİMİ — FAZ 8 / AYRILIS · QA DERSLERİ VE AKSİYON

```
Koşu    06.09.2026 · Gemini · makara ~99-100 s · 10 segment
Ham     ../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
        02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ08_8MERCEK_HAM.md
Mod     ⚠️ V — SPEC yok · ÇIPLAK RUBRİK [D129] → T tablolarına GİREMEZ
⛔ FAZ_08_QA_PROMPT.md KOŞULMADI. Onun yerine _KAYNAK/ altındaki genel
   sekiz mercek koşuldu — ve bu, bu koşunun en pahalı kararıdır
   (aşağıda "YANLIŞ ALET" bölümü).
```

---

# 🔴🔴 BİRİNCİ BULGU — MAKARA 10 KLİP, İKİ SAHNE ÜRETİLMEMİŞ

Sekiz merceğin sekizi de aynı sahne haritasını verdi. Harflerle:

```
S1=G(S85) S2=C(S86) S3=L(S87) S4=I(S88) S5=B(S89)
S6=E(S90) S7=J(S91) S8=A(S92) S9=K(S95) S10=F(S96)

⛔ EKSİK: H (S93 İLK SARSINTI) · D (S94 DALGA İKİ)
```

**S94 bu fazın TAŞIYICISIDIR.** Dosyanın kendi üretim sırası onu
1. sıraya koyuyor ve şunu yazıyor:

> *"SONUÇ: çıkmazsa S95-S96 üretilmez; faz durur."*

**S95 ve S96 üretildi.** Kapı belgede duruyor, üretimde bağlamadı.

```
NE KAYBEDİLDİ — dördü de tek sahnede duruyordu:
 ① DORUK RAMPASININ BAŞI (%77,5)
 ② ⭐ ÇEHOV 5 ÖDEMESİ — S22'nin "doksan dakika" hesabı. Ödenmedi.
    (J/S91 kısmî ödeme yapıyor: camdan geçen çizgiler. Ama dalganın
     istasyonu vurduğu an ekranda YOK.)
 ③ ŞOK BANDI 1 — S93 ECU → S94 WS, üç kademe. İkisi de yok, bant yok.
 ④ MUTLAK SESSİZLİK BIÇAĞI (KİLİT 38) — filmin bütün ses tasarımı bu
    on saniye için biriktirilmişti.
⭐ TEK İYİ HABER: şok bandı HARCANMADI. Filmde hâlâ ≤2 hakkı var ve
   S102 tek başına ikisini de taşıyabilir. Bütçe aşılmadı, eksik kaldı.
```

⛔ **VE MAKARA SIRALI ÜRETİLMİŞ** (S85→S96, karıştırılmamış). Bu
yüzden bu makarada **kör geçişin sıra testi zaten koşulamazdı** —
karıştırılmamış bir makara D164'ün A geçişine verilemez.

---

# 🔴 İKİNCİ BULGU — ÜÇ REPLİK DUYULDUĞU İDDİASI ⚠️ ŞÜPHELİ

```
İDDİA (① kare merceğinden başlayarak altı raporda):
  0:52 "Trajectory confirmed."            · ekranda ağız oynuyor
  1:24 "Sequence initiated."               · ekranda ağız oynuyor
  1:35 "Trajectory nominal, separation complete."
  Register: HUMAN · konuşan: A · sahnede.

⛔ AMA ⑥ FİZİK MERCEĞİ, AYNI OTURUMDA VE DAHA ÖNCE:
  "LINES HEARD: none — nothing audible to me"
```

🔴 **KONTAMİNASYON [DERS 110].** Sekiz mercek AYNI SOHBETTE koşuldu.
İlk mercek ses duymadı; ikinci mercek üç cümle duydu; sonraki beşi
aynı cümleleri aynı zaman kodlarıyla, aynı sahne haritasıyla, aynı
presence string'iyle tekrarladı. **Bu sekiz ölçüm değil, bir ölçüm ve
yedi kopyadır.**

```
⛔ DOĞRULANMADAN DERS YAZILMAZ. Tek komut:
   ffprobe -v error -select_streams a -show_entries stream=codec_name,channels -of csv=p=0 <makara>
   · ses akışı YOKSA → altı rapor da halüsinasyon; kayıt DERS 110'a düşer
   · ses akışı VARSA → aşağıdaki dört kilit birden kırılmış demektir
```

**Eğer replikler gerçekse kırılan dört şey:**

```
① KASK TAKVİMİ — kasksız sahnede replik 0. A KONUŞUYOR ve ağzı ekranda.
② REGISTER — defterdeki üç replik de MACHINE; duyulan HUMAN.
③ METİN — üçünün hiçbiri defterdeki cümle değil. Uydurma.
④ OKSİJEN ZİNCİRİ — son halka ("THREE PERCENT") söylenmiyor.
   62→41→23→11→6→? zincir ekranda da seste de kapanmamış olur.
⭐ Ve bu, F7'nin altyazı bulgusunun aynı kökten devamıdır: model klibe
  kendi diyaloğunu yazıyor. F7'de yazıya, F8'de (belki) sese.
```

---

# 🔴 ÜÇÜNCÜ BULGU — HALKA YİNE YOK

```
② devamlılık merceği, birebir:
  "0:30 vs 1:10 — Black wrist cuff with indicator is present;
   later arm is plain white sleeve."
```

0:30 = I (S88). Promptta orada halka var: *"a slim ring of six square
amber segments with one lit and five matte black."*
Ekranda: **"turuncu göstergeli siyah bir bilek bandı"** — altı segment
değil, sayılabilir bir sayaç değil. Ve 1:10'da yok.

```
F7 : 12 klip · halka 0 görülme
F8 : 10 klip · halka 1 belirsiz görülme
⛔ FİLMİN EN UZUN SAYACI (S8'den S96'ya, altı adım) EKRANDA YOK.
```

⭐ **AÇIK MADDE ③ CEVAPLANDI ve cevabı beklediğimden kötü:** halka
"sabit mi yanıp sönüyor mu" diye sormuştum. Cevap: **halka okunmuyor.**
Yanıp sönme sorusu anlamsız — sayılacak segment yok. KİLİT 39 ile
promptlar arasındaki çelişki (ÜÇ NOT ②) böylece TEORİK bir çelişki
olarak kalıyor; pratikte ikisi de ekranda yok.

---

# 🔴 DÖRDÜNCÜ BULGU — S85'İN IŞIK ÇELİŞKİSİ ÜRETİME GİRDİ

Üretimden önce ÜÇ NOT ①'de yazmıştım: S85 IMAGE promptunun SCENE
satırı `"in hard new sunlight"` diyor, aynı promptun diğer üç bloğu ve
fazın ışık takvimi `tek amber lamba` diyor.

```
⑤ arka plan merceği, S1 için: "FOCUS: Sharp on speaker grill, soft on
   shadow edges · EDGES: Dark shadow on right edge"
   → loş okunuyor, sert beyaz DEĞİL.
✅ Yani SCENE satırı ekranda kazanmamış; amber kazanmış.
⚠️ Ama satır dosyada duruyor ve bir sonraki üretimde kazanabilir.
   ⭐ S77 ↔ S85 EŞLEŞTİRİLMİŞ KADRAJ ÇİFTİ bu satıra bağlı: iki klip
     arasındaki tek değişken SES olmalı. Bu koşuda çift TUTTU.
```

---

# 🔴🔴 BEŞİNCİ BULGU — YANLIŞ ALET KULLANILDI, ve bedeli ölçülebilir

Sekiz genel mercek, faza özgü rubriğin yerine koşuldu. Sonuç: **üç
YANLIŞ POZİTİF, ve fazın taşıyıcı kilidinin HİÇ ÖLÇÜLMEMESİ.**

## Yanlış pozitifler — üçü de belgede AÇIKÇA yazılı tasarım

```
① ① KARE: "1:30 — Capsule thruster plumes render as RIGID SOLID CONES
   instead of expanding gas" → 🟠 MAJOR
   ⛔ Belge: "dört DÜZ koni, keskin kenarlı, hızla incelerek biter
     [D36]. ⛔ Kabarma, kıvrılma, mantar, duman YOK."
   → Ekranda DOĞRU olan şey kusur yazıldı.

② ⑧ EFOR: "0:15 — bare-hand dexterity in thick pressurized GLOVES"
   → 🟠 MAJOR
   ⛔ Belge: A S48-S120 arası ELDİVENSİZDİR (eldivenler kemerde).
   → Mercek olmayan bir eldiveni kusur yazdı.

③ ① KARE + ⑧ EFOR: "debris hangs without momentum" → 🟠
   ⛔ Belge: parçalar DÜZ ÇİZGİDE SABİT HIZLA gider; ivme YOK.
   ⑥ FİZİK bunu doğru okudu ("constant velocity is correct for inert
     debris"), ① ve ⑧ kusur yazdı. Aynı olay, üç mercek, iki karar.
```

## Ölçülmeyen şey — ve bu daha pahalı

```
⛔ I (S88) IŞIK GEÇİŞİ HİÇBİR MERCEK TARAFINDAN ÖLÇÜLMEDİ.
   Fazın en kırılgan tek karesi: güneş bir saniyeden kısa sürede
   varmalı, ara ton 0 kare, bloom 0. KABUL/RET ölçütü dosyada
   SAYIYLA yazılı (0-1 s karanlık · 1-2 s sert beyaz).
   Sekiz merceğin hiçbiri bu soruyu sormadı, çünkü hiçbiri bu fazı
   bilmiyordu. FAZ_08_QA_PROMPT.md üç ayrı yerde soruyor.

⛔ AYNI ŞEKİLDE ÖLÇÜLMEYENLER:
   · kapsül ekran-SOLA mı gidiyor (KİLİT 41 eksen kilidi)
   · dört lülenin ışık atıp atmadığı
   · S87'nin dört ikonunun harfe dönüşüp dönüşmediği (metin tuzağı)
   · parmağın panele TAM İKİ KEZ dokunup dokunmadığı
   · kemerin dört hareketi tek sırayla mı yapıldığı
```

⭐ **VE ④ HİKAYE MERCEĞİ BİR FAZ MAKARASINI FİLM SANDI:** 3,5/10 ·
"REWRITE PREMISE" · "kanca yok, tema yok, paylaşılabilir an yok". Yüz
saniyelik bir faz, yirmi dakikalık bir filmin doruk rampasıdır; kanca
S1'dedir, tema S117'dedir. **Bir faz makarasına hikâye merceği
koşulmaz.** Rubriğin PARTIAL RUN kapısı bunu yakalayamadı çünkü
"length class (not supplied)" idi ve taban uygulanmadı.

```
⭐ KURAL — F9 ve F10 makaraları geldiğinde:
   FAZ MAKARASINA KOŞULACAK OLAN, O FAZIN KENDİ İKİ MÜHÜRLÜ
   RUBRİĞİDİR (FAZ_09_QA_PROMPT.md · FAZ_10_QA_PROMPT.md).
   Genel sekiz mercek TAM KURGUYA koşulur, faza değil.
   ⛔ Ve her mercek TEMİZ OTURUMDA [DERS 110].
```

---

# 🟢 TUTAN KİLİTLER — F9-F10'da BOZMA

Yanlış pozitifleri ayıkladıktan sonra geriye ölçülmüş ve tutmuş
kilitler kalıyor:

```
✅ TEK KİŞİ            "CHARACTERS TRACKED: 1" · duplike 0
✅ AYNI YÜZ            "Identity 10/10" — iki yüz kadrajı arasında sapma yok
✅ KASKSIZ             10/10 klipte kask yok
✅ İNSANSIZ KLİPLER    presence string "-111-1-11-" → 4 klipte insan yok,
                       Kart 10 uygulandı ve tuttu
✅ SERT GÜNEŞ REJİMİ   "hard sunlight phase reads effectively"
✅ DÜZ ÇİZGİ FİZİĞİ    ⑥ fizik: sabit hız, eğrilme 0, ivme 0
✅ ALEV/DUMAN 0        hiçbir mercek yanma, duman, kıvılcım bildirmedi
✅ MAKRO KARARLILIK    "interior control panel macro shots hold
                       exceptional detail, no swimming textures"
✅ KAMERA              10/10 kilitli (D'nin push-in'i zaten üretilmedi)
```

---

# 🔴 GERÇEK KUSURLAR — yanlış pozitifler ayıklandıktan sonra kalanlar

```
🔴 A (S92) 1:15 — başparmak kolun yüzeyine ERİYOR (el-yüzey füzyonu)
🟠 A↔K (1:10 vs 1:20) — kol çekişi kesme boyunca TEKRAR EDİYOR:
   CU'da tamamlanan çekiş, WS'te baştan başlıyor.
   ⛔ Ama bu kısmen kurgu kararıdır: A (S92) kolu ÇEKMEZ, K (S95)
     çeker. İki sahne yan yana kesilince "tekrar" okunuyor.
     ⭐ Aradaki İKİ SAHNE (S93 · S94) üretilmediği için komşu oldular.
     → Kusurun kökü eksik sahne, kesme değil.
🟠 C↔K (0:10 vs 1:20) — kemer tokası değişiyor: S86'da iri merkezî
   metal toka, S95'te düz kayışlar, toka yok.
   ⛔ Kemer bu fazın tek yönlü saatidir; donanımı değişiyor.
🟠 I↔J (0:30 vs 1:00) — aynı lomboz: önce düz yıldızlar, sonra
   "dev gezegen halkaları". J'nin şartnamesi PARALEL PARÇA ÇİZGİLERİ.
   ⛔ Çehov 5'in görsel ödemesi okunmadı.
🟡 B↔F (0:40 vs 1:30) — istasyon modül geometrisi kayıyor (RE p2
   üretilmediği için beklenen; F3 dersinin tekrarı).
🟡 1:26 — sarsıntıda "jello" warp (araç kusuru)
```

---

# 🔧 AKSİYON

```
🔴 ÜRETİLMESİ GEREKEN İKİ SAHNE
 ① S94 DALGA İKİ — fazın taşıyıcısı. Üretilmeden faz tamamlanmış
   sayılamaz: Çehov 5 ödenmemiş, doruk rampası başlamamış olur.
 ② S93 İLK SARSINTI — S94'ün şok bandının ilk yarısı. Tek başına
   üretilmesi anlamsız; S94 ile birlikte.
 ⛔ İkisi üretilene kadar F8 makarası "TAM" sayılmaz ve F9 makarası
   ona bağlanamaz (S96 → S97 köprüsü S94'ün varlığını varsayar).

🔴 TEK KOMUTLUK DOĞRULAMA — her şeyden önce
   ffprobe ... → makarada ses akışı var mı?
   Cevap "var" ise üç replik gerçektir ve kask takvimi kırılmıştır.

🟠 ÜÇÜNCÜ ADAY  A (S92) — başparmak füzyonu. Tek figürlü, ucuz.

🟡 ÜCRETSİZ, ÜRETİM GEREKTİRMEZ
 · S85 SCENE satırındaki "in hard new sunlight" silinir (bu turda
   yapılmadı — sahip kararı bekliyor; ekranda henüz kazanmadı).
 · F9/F10'a altı kapı yazıldı (bu turda YAPILDI).
 · DERS 110 ihlali CALISTIRMA_KAYITLARI'na düşer.

🔵 KABUL EDİLEBİLİR
 · istasyon geometrisi kayması · jello warp · lomboz manzarası
```

---

# ⭐ BU KOŞUNUN DEPOYA KAZANDIRDIĞI TEK BÜYÜK ŞEY

```
Sekiz genel mercek bir FAZ makarasına koşulduğunda:
  · üç yanlış pozitif üretti (tasarımı kusur yazdı)
  · fazın en kırılgan kilidini hiç ölçmedi
  · bir faz makarasını film sanıp 3,5/10 verdi
  · ve sekizi de aynı oturumda koşulduğu için tek bir raporun
    sekiz kopyası oldu

⭐ Faza özgü iki mühürlü rubrik (D164) tam olarak bu dört şey için
  yazılmıştı ve dördünü de kapatıyor: INTENDED listesi yanlış
  pozitifi, katalog girdisi ölçülmeyen kilidi, faz kapsamı hikâye
  yanılgısını, iki ayrı sohbet kontaminasyonu kapatır.
  ⛔ F9 ve F10 makaraları geldiğinde ÖNCE kendi rubriği koşulur.
```
