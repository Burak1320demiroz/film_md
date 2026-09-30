# 📚 YERÇEKİMİ — FAZ 2 / DALGA · QA DERSLERİ VE AKSİYON

```
Koşu      01.09.2026 · iki mühürlü geçiş (A kör + B katalog), Gemini
Ham       ../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
          02_HAM_RAPORLAR/YERCEKIMI_FAZ02_{KOR,KATALOG}_HAM.md
Defter    .../01_FILM_RAPORLARI/YERCEKIMI.md § KOŞU 2
Mod       ⚠️ V — SPEC yok [D129] · master yok [⑪] → film-dersi YAZILAMAZ,
          adaylar DERSLER/GOZLEM_DEFTERI.md ADAY-2/3/4'e düştü
Sisteme   D164 yazıldı (08_QA) · D146 TEKRAR 2 aldı ve çözümü ÇÜRÜDÜ
```

---

# ⛔ PROJE SAHİBİ KARARI — 01.09.2026

```
"geri dönüş yapmıcaz"

→ FAZ 2 OLDUĞU GİBİ KALIR. Yeniden üretim YOK.
→ Aşağıdaki kusurlar artık KUSUR DEĞİL, FİLMİN OLGUSUDUR.
→ Sonraki fazların bunlara UYMASI gerekir; düzeltmesi değil.
```

Bu karar üç şeyi kalıcı yapar. Her biri sonraki fazlar için bir KURALDIR:

---

## ① 🔴 FİLMİN VİZÖRÜ ARTIK KUBBEDİR

```
ÖLÇÜM: F2'nin 12 klibinden 6'sında yüz okunur; ALTISINDA DA kubbe.
       Bunların BEŞİNDE promptta tam tarif ölçüleriyle vardı:
       "flat rectangular front glass measuring 24 by 16 centimetres,
        held in a visible bright metal frame the width of a finger"
       Belgede yazılı olan, ekranda 0/6 tuttu.
```

⭐ **Kilidin iki yarısı vardı ve ayrıştılar:**

| yarı | ne diyordu | sonuç |
|---|---|---|
| GEOMETRİ | düz dikdörtgen cam + görünür metal çerçeve | **0/6 — kaybetti** |
| OPTİK | berrak, tonsuz, aynasız, yüz okunur | **6/6 — kazandı** |

Dramayı taşıyan yarı tuttu. Kör denetçi de doğruladı: *"yakın çekimlerde yüzü
net görünüyor."* Filmin ihtiyacı olan buydu.

**KURAL — F3'ten itibaren:** vizör kubbedir, ve bu bilinçlidir. Prompt
cümlesini değiştirmek ŞART DEĞİL (zaten okunmuyor) ama belgelerin filmle
kavga etmemesi için REFERANS_PAKETI RA sayfası bir not almalı. ⛔ F3'te
kimse "düz cam" üretmeye çalışmamalı — üretebilirse bu sefer **o** süreklilik
hatası olur, çünkü film 24 sahnedir ve 24'ünde kubbe vardır.

---

## ② 🔴 MEKİĞİN BURNU F1 ve F2'DE EKRAN-SAĞA BAKIYOR

```
12 promptun 12'sinde yazılı: "nose pointing screen-left"
Ekranda: 5 klipte SAĞ, 1 klipte SOL.
⭐ Doğru çıkan tek klip (E/S17), burnun kadraj DIŞINDA olduğu ve yönü
   açık kargo kapağının taşıdığı klipti.
```

**Teşhis:** yön kilidi ancak kadrajda **yük taşıdığında** tutuyor. Uzak bir
siluet olduğunda model kendi önyargısına dönüyor.

**KURAL:** mekik F3-F10'da yok (kontrol edildi). Ama aynı mantık **istasyona**
uygulanacak: istasyonun yönü uzak siluetle değil, kadrajda iş yapan bir
parçayla (airlock kapağı, kapsül konisi) tanımlanmalı.

---

## ③ 🔴 İKİ SAHNE HİÇ ÜRETİLMEDİ — VE BİRİ ÖLÇEK YAYINI KIRIYOR

```
S8  (F1) — proje sahibi İPTAL etti (politika reddi)
S15 (F2) — üretilmedi; onun yerine S14 İKİ KEZ üretilmiş (Seg 2 = Seg 3)
           → operatör kayması, model hatası değil

Kullanılabilir klip: F1 11/12 · F2 11/12
Boş yuva: 2 × 8 s = 16 s → 16:00 yerine 15:44
```

⛔ **S15'in yokluğu yalnız bir delik değil, ÖLÇEK YAYI İHLALİ:**

```
S14  WS(2) · göz hizası     ┐
S15  EWS(1) · alt açı 20°   │ ← YOK
S16  WS(2) · üst açı 20°    ┘

S15 olmadan komşu çift:  S14 WS → S16 WS
   ölçek farkı  0 kademe   (ACI_YAYI §3: ≥1 şart)
   açı farkı   20°         (§3: ≥45° şart)
   → İKİ ölçüt de düşüyor; betik BLOCK verir.
```

⭐ **S15 fazın EN UCUZ ve EN RİSKSİZ sahnesidir:** kadro 0, insan yok, vizör
yok, sayaç yok, hasar yok, referans bağımlılığı yok — yalnız gökyüzü ve
platformun kenarı. Üstelik **🔥 viral ara #1** ve tek kare testi karesi.

📌 **Kayıtta duruyor: "geri dönüş yok" kararı bu sahneyi de kapsıyorsa yuva
boş kalır ve ölçek yayı S14-S16'da kırık kalır.** Bunu bilerek kabul etmek
meşrudur (S8'de de öyle yapıldı); bilmeden kabul etmek değil.

---

# 🟢 TUTAN KİLİTLER — F3'te BOZMA

Bunlar ölçüldü ve çalıştı. İkisi kör geçişte, hiçbir şey söylenmeden onaylandı.

```
✅ DÜZ SIRT           kör denetçi: "sırtında kesinlikle hiçbir şey yok"
                      ⭐ F1 raporu tam tersini iddia etmişti — çürüdü
✅ SIFIR YAZI         12 klipte okunur tek karakter yok
✅ ENKAZ FİZİĞİ       düz çizgi · sabit hız · sağdan sola · alev 0 · duman 0
✅ HASAR TEK YÖNLÜ    hiçbir girdide onarım/geri dönüş yok
✅ TEK HAREKETLİ PLAN D'nin push-in'i doğru koştu, kalan 11 kilitli
✅ GÖK SAATİ          6 farklı gök durumu, 6'sı da doğru girdide
                      ⭐ filmin en iyi işleyen görsel zinciri — model al
✅ IŞIK YÖNÜ          üst ekran-sağ, kör geçiş bağımsız doğruladı
✅ DÖNÜŞ HIZI         ~18-20 s/tur, sabit, kendiliğinden yavaşlamıyor
```

---

# 🔴 KARE BEKLEYEN İKİ MADDE (kapanmadı)

```
① BAYRAK ÇELİŞKİSİ — kör geçiş adamda "US flag patch on the left shoulder"
   gördü; katalog geçişi metin kategorisine 10/10 verdi. Bayrak yasak
   (no flag / no insignia / no mission patch) + §7 gerçek kurum kuralı.
   ffmpeg -ss 84 -i <makara>.mp4 -frames:v 1 omuz.jpg

② MOMENTUM — K'de A'nın dönüşü dururken B'de karşı sarsıntı yok (yalnız
   katalog geçişi gördü → ŞÜPHELİ, tek geçiş).
   ffmpeg -ss 86 -i <makara>.mp4 -frames:v 1 tutus.jpg
```

---

# ⭐ SIRA SKORU — bu fazın kalıcı ölçüsü

```
8/12   (D↔E berabere sayılırsa 9/12 — eşzamanlı, kanıt yok)
```

Dört sapmanın hepsi iki sebebe indi ve ikisi de sonraki fazları bağlar:

**① S18'in halat kopuşu görülmedi** → kör denetçi o klibi hasar öncesine
koydu. Olay kadrajın alt-sağ kenarında, ince, 2. saniyede. Prompt tamdı;
**kadraj kararı eksikti.** → `GOZLEM_DEFTERI ADAY-4`

**② Savrulma bloğunun saati yok** → I·H·G birbirinden ayrılamadı; tek ayrım
oksijen halkası ve halka **yalnız tek klipte** okunuyor. → `ADAY-3`

⭐ **F3 bu ikinciyi ZATEN ÇÖZMÜŞ:** S30'da halka 4/6 → 3/6 ve S34'te şerit
1/4 → 0/4 **sahnenin İÇİNDE** düşüyor. Geçişi görmek iki ayrı okuma
ihtiyacını ortadan kaldırıyor. Bu tasarım kararı korunmalı ve F4-F10'a
yayılmalı.

---

# 🔧 F3'E GEÇMEDEN ÖNCE — TEK ZORUNLU MADDE

```
⛔ RE (İSTASYON DIŞ) SAYFASI ÜRETİLMEDİ.
   REFERANS_PAKETI RE başlığının kendi notu: "☐ · F3'ten önce"
   F3'ün 12 sahnesinin 7'si RE p2'ye ÇAPA veriyor:
     S27 uzak parıltı → S28 BİÇİM → S29 derinlikte net → S32 tam boy →
     S33 gövde yakın → S35 arkada büyür → S36 kadrajı doldurur
   Aynı nesnenin YEDİ farklı ölçeği. Referanssız yedi farklı istasyon
   demektir — F2'nin enkaz çelişkisinin (2 klip) üç buçuk katı.

ÇÖZÜM (F2'nin kendi reçetesinin aynısı): S32 İLK üretilir.
   Kadro 0 · insan yok · vizör yok · sayaç yok · replik kadraj dışı.
   Fazın en risksiz sahnesi ve tam olarak RE p2'nin kadrajı.
   Çıkan kare RE p2 YERİNE GEÇER, kalan altı sahne ona bakarak üretilir.
```
