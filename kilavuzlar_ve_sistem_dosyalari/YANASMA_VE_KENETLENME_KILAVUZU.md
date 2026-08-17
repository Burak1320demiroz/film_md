# 🛰️ YANAŞMA VE KENETLENME KILAVUZU

> İki gövdenin birbirine yanaştığı ve kenetlendiği sekanslar (docking,
> berthing, iniş aracı ↔ ana gemi) için **vuruş/kompozisyon reçetesi**
> ve **ses/dramaturji kalıbı**. Bu kılavuz geometri KİLİDİNİN kendisini
> anlatmaz — o iş `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` §4-5'te
> durur ve burada tekrarlanmaz. Buranın işi: hangi kadrajın güvenli
> olduğu ölçüldü, hangi ses/dramaturji kararı üç filmde de aynı çıktı —
> onları bir daha türetmemek.
>
> Eklenme: 17.08.2026 · **Kanıt tabanı üç film:** THE COLD BURN
> (5 mercek QA + fragman) · THE RING LIGHT (4 koşu, kurgu kapısını tam
> geçen ilk film) · THE BLACK CRADLE (S4 V1/V2/V3 üretim ölçümü →
> DERS 104 · uzamsal kılavuz Sürüm 3).
>
> **Kapsam notu (dürüst kayıt):** Bu ilk sürüm iki bölümdür — §1
> kompozisyon seti, §2 ses/dramaturji. Planlanan ama henüz YAZILMAMIŞ
> bölümler sonda listelidir (§9); oradaki bilgiler şimdilik adres
> verilen kaynaklarda yaşamaya devam eder.

---

# 1. 🎥 GÜVENLİ KOMPOZİSYON SETİ — yanaşmanın altı vuruşu

## 1.1 Tek ilke: iki gövdeyi aynı kareye koyan her kadraj risklidir

```
ÖLÇÜLEN GERÇEK [DERS 104 · D32 · D78]:
İki gövde aynı karede = model üç şeyi birden yazı-turaya atabilir:
ORAN (iki aracı yakın boyda çizer — Cold Burn 65 m gemisi lander
boyunda okundu), YÖN (hangi uç önde — burnu çevirir) ve DİZİLİM.
Tek gövdeli kadrajda bu sınıfların hiçbiri var olamaz.

ÇÖZÜM RİSKİ YOK ETMEK DEĞİL, HAPSETMEKTİR (risk kartı ilkesinin
kadraj karşılığı): altı vuruşluk set, iki-gövdeli kareyi TEK vuruşa
(V3 oran karesi) hapseder. Kalan beş vuruş tek gövde + insan
kadrajlarıdır ve bu hata sınıflarına yapısal olarak kapalıdır.

D104'ÜN YANAŞMA KARŞILIĞI — kanıtlı güvenli kompozisyon:
KAMERA HEDEFTE SABİT DURUR, ARAÇ KAMERAYA DOĞRU GELİR.
Yaklaşan aracın "kameraya doğru" gelmesi modelin frontal refleksiyle
HİZALIDIR (nötr çekim, uzamsal §6.3/§6.8) — refleks doğru cevabı
üretir. Kanıt: Black Cradle S21 + Ring Light temas kadrajı tuttu;
kameraya paralel (yandan) eksende ise Black Cradle S4 iki kez battı.
```

## 1.2 ⭐ VURUŞ SETİ TABLOSU — güvenli kadraj / riskli kadraj

> Sıra dramaturjik sıradır; her satır "kamera nerede durur" sorusunun
> ölçülmüş cevabıdır. Lens/mesafe kalıpları küreseldir (anamorfik yasak).

| # | Vuruş | Kamera nerede | Kadrajda ne var | Güvenlik | Kalıp | Kanıt |
|---|---|---|---|:--:|---|---|
| **V1** | **HEDEF REVEAL** | hedef gövdenin üstünde/yanında sabit | YALNIZ hedef: rıhtım/koni/kelepçe geometrisi; gövde kadrajı aşar (ölçek imâsı) | ✅ güvenli | 32mm · 10-15 m · nicelik sayıları yazılır (kol/kelepçe/ışık ADEDİ) | Black Cradle S13 · Cold Burn S15 |
| **V2** | **GÖZLEMCİ İÇERİSİ** | aracın içinde, bakan insanın ARKASINDA | insan sırttan + cam/lomboz + hedef yalnız IŞIK NOKTASI/siluet ölçeğinde | ✅ güvenli | 35mm · 1.2-1.5 m · cam yansımasız [D20] · ağız kadrajda değil | Black Cradle S14/S19 · Cold Burn S9/S16 |
| **V3** | **ORAN KARESİ** ⚠️ | eksene dik DEĞİL — hedef tarafına kaydırılmış geniş | iki gövde birden — SETİN TEK RİSKLİ VURUŞU | 🔴 riskli | 32mm geniş · zorunlu üçlü: ① oran CÜMLESİ ("one-fifteenth — a moth beside a cathedral" [D32/D78]) ② hangi-uç-önde cümlesi [uzamsal §5.1 ①] ③ kesir merdiveni [uzamsal §4.6] | Third Dune 25/25 tuttu · Cold Burn 65→140 m dersi · Black Cradle S15 |
| **V4** | **KAPI / SON YANIŞ** | eksenden 40-60 m abeam, hedef kadraj kenarında | araç + fren darbesi; motorların KARARDIĞI an | 🟡 orta | plume yönü kilidi [uzamsal §5.3.1] · "bundan sonra hiçbir motor ateşlemez" negatifi · MİRA/AI sayısı SESLE | Black Cradle S20 |
| **V5** | **TEMAS DETAYI** ⭐ | **HEDEFTE** — rıhtım ağzında / koninin yanında sabit | araç kadraja GİRER ve kameraya doğru oturur; temas sahnenin İÇİNDE [B1] | ✅ güvenli (D104 kompozisyonu) | 35mm · 12-15 m · temas hızı sayıyla (0.2 m/s) · rigid-body oturma ("2 cm settle, no bounce, no merging" [D17]) | Black Cradle S21 ✓ · Ring Light temas ✓ · Cold Burn S21 |
| **V6** | **KENET DETAYI** | kenet mekanizmasının karşısında makro | YALNIZ mekanizma: mandal/kelepçe sırayla kapanır | ✅ güvenli | 85mm · 3-8 m · NİCELİK TESTİ: "exactly FOUR clamps — no more, no fewer" · sıra + tek duraksama dramaturjisi | Black Cradle S22 · Cold Burn S22 (4 yaprağın 3'ü) |

```
SETİN OKUNMASI
· V1-V2 kurulumdur: hedefi ve GÖREN GÖZÜ tanıtır. V2'nin gizli işi
  büyük: "kim görüyor" sorusunu cevaplar — yanaşma bir bakış filmidir.
· V3 bir kez, en fazla iki kez kullanılır. Üç kez iki-gövdeli geniş
  kare isteyen plan, riski üç kez satın alıyordur — vuruşu V1 (yalnız
  hedef) veya V5 (kamera hedefte) ile değiştir.
· V4→V5 arasında zaman atlaması serbesttir (ölü süzülme dakikaları
  kesmeyle atlanır); sayı SESLE köprülenir ("kırk metre... süzülüyoruz").
· V5'te temas ANI sahnenin içindedir ve saniyesi yazılıdır ("contact
  at 6.0s"). İki sahne ARASINA düşen temas kurguyla kurtarılamaz
  [B1 — Tidal Hunt dersi].
· İptal (wave-off) vuruşu sete eklenirse V3 kadrajıyla çekilir ve
  ıraksama yayının EKRAN yönü yazılır (Black Cradle S17: yukarı-sol).
```

## 1.3 Kadraj çiftleri — tekrar mimarisi

```
Yanaşma dizisinin en ucuz güven kazancı: V2 kadrajı İKİ KEZ, birebir
aynı çerçeveyle kullanılır — ilkinde hiza BOZUK, ikincisinde OTURMUŞ
(Black Cradle S14↔S19: çarpık üçgen → eşkenar üçgen). Değişen tek
şey hizadır; izleyici farkı çerçeveden değil geometriden okur.
Aynı kalıp kokpit/bedel çifti için de geçerli (S16↔S18: 2 segment →
1 segment). Kural: çift kadrajda İKİNCİ promptun SCENE bloğu "the
same fixed framing as ..." diye açılır ve tek değişkeni adlandırır.
```

## 1.4 Ters yanaşma (kıç önde) eki

```
Kıç önde yanaşan araçta V3-V4-V5 vuruşlarının HER promptuna iki cümle:
① önde giden ucun adı: "its notched tail and dark engine nozzles
   LEAD; the canopy nose trails, pointing away from the target"
② negatif tersleme: hazır listedeki "no stern-first motion" ATILIR,
   yerine "never nose-first — the [canopy/bow] end never faces the
   target" yazılır [uzamsal §4.8/§5.6 uyarısı · DERS 104].
```

---

# 2. 🔊 SES VE DRAMATURJİ SAYFASI — üç filmde donan kararlar

> Bu bölüm yeni kural koymaz; Cold Burn → Ring Light → Black Cradle
> hattında ÜÇ KEZ aynı şekilde verilmiş kararları kalıba döker.
> Kaynak dersler: D82 (ses mimarisi) · D83 (ortam yatağı) · B1 (doruk
> sahne içinde) · kart E3 register kuralı.

## 2.1 Temasın sesi: YOKTUR — ve bu doruğun kendisidir

```
Vakumda dış mekanik ses SIFIR: temas, kelepçe, sürtünme duyulmaz.
Doruğun tek ses malzemesi TELSİZ YATAĞIDIR:
  · sabit, çok alçak taşıyıcı hışırtısı
  · iki insanın nefesi — temas anında YARIM SANİYE TUTULUR ve
    hemen sonra yavaşça bırakılır (sesin yokluğu, vurgunun kendisi)
  · varsa fısıltı onayı temasın SONRASINA düşer ("Rıhtımdayız."),
    aynı telsiz kanalında

D83 KAPISI — yatak klip sınırında ÖLMEZ:
Telsiz yatağı kliplere bölünmez; kurgu boyunca TEK PARÇA serilir.
Cold Burn'de 20 saniyelik dijital sıfır miks hatası çıktı (D83'ün
kaynağı); "müziksiz" sahne SESSİZ sahne değildir. Teslimden önce
temas bölgesi kulakla dinlenir: mutlak sıfır varsa yatak yeniden.

MÜZİK: doruktan ÖNCE susar, doruk sahnesinin başında değil
(sessizliğin fark edilmesi 1-2 saniye ister — müzik kılavuzu §10).
En güçlü biçimi diegetik gerekçeyle susmak: Black Cradle'da müzik
"Motorlar kapalı" repliğiyle, motorlarla BİRLİKTE kesilir. Çözülme
akoru temasta değil, İNSAN sahnesinde gelir (güverte/yüzler).
```

## 2.2 Replik mimarisi — sayı makinede, insan telsizde

```
① SAYI SÖYLEYEN HER REPLİK GÖVDESİZ AI'DADIR (mesafe, hız, yüzde,
   geri sayım). İnsana devredilemez — Cold Burn'ün ölçülmüş en pahalı
   hatası tam buydu (D82: EKO silindi, sayılar ekrandaki ağızlara
   geçti, lip-sync çöktü). Ring Light ve Black Cradle bu kuralı
   yapısal panzehir olarak taşıdı.
② İNSAN REPLİKLERİ kapalı kask telsizinden; konuşmalı kokpit ARKADAN
   çekilir, lombozdaki gözlemci SIRTTAN — ağız hiçbir karede okunmaz.
③ EN GÜVENLİ BİÇİM: kadrajda insan YOKKEN duyulan telsiz repliği
   (dış çekim + radyo kanalı — Cold Burn S19 emsali; Black Cradle
   iptal/kapı/fısıltı repliklerinin dördü de böyle).
④ TURN LOCK: her replik tek konuşmacı; karşılıklı atışma yok; aynı
   sahnede iki replik varsa sıra saniyeyle yazılır.
⑤ Kasksız sahnede tek kelime KONUŞULMAZ (kural üç filmde de aynı).
```

## 2.3 Dramaturji kalıbı — yanaşma bir güven/prosedür anlatısıdır

```
İPTAL PROSEDÜRDÜR [yetkinlik kuralı]:
İlk denemenin iptali (wave-off) hata değil, bilgiyle verilmiş
karardır — ve yanaşma yayının en ucuz "umut-önce-düşüş" vuruşudur.
BEDELİ GÖRÜNÜR OLMALIDIR: iptal bir kaynağı harcar (yakıt segmenti)
ve kayıp SONRAKİ sahnede fiziksel kanalda okunur (sönen segmentin
boş yuvası [D78 ①]). Üç filmde de CENTRAL CHOICE bu ailedendir:
Cold Burn S19 iptal · Ring Light S8 karotu bırakmak · Black Cradle
S17 iptal.

DORUK = TEMAS ANIDIR ve sahnenin İÇİNDE biter [B1]:
"prob koniye oturur" / "raylar kızağa oturur" cümlesi ve saniyesi
doruk sahnesinin promptunda YAZILIDIR. Temasın görsel imzası
DURGUNLUKTUR: 0.2 m/s'de hareket neredeyse okunmaz — gerilim hızdan
değil sabırdan gelir (Cold Burn'ün Interstellar ayrışması; üç filmin
ortak ton kararı).

GERİLİM KANALLARI METİNSİZDİR:
mesafe/hız yalnız AI sesinde · hiza GEOMETRİYLE (ışık üçgeni, hiza
kanadı, segment doluluğu) · ekranda rakam 0.0 saniye [kart 5].
Görsel kanal ile sesli kanal AYNI sayıyı söyler ve birbirini
doğrular (gösterge 2 yanık ↔ "yüzde dört" — D78 çift kanal kuralı).

ÇÖZÜLME KISA VE İNSANLIDIR:
kenet (V6) → gevşeme/fısıltı → ilk yüzler. Doruk sonrası kuyruk
2-3 sahneyi geçmez; kasksızlık yalnız basınçlı hacimde ve tek
sahnede açılır.
```

## 2.4 Hazır AUDIO satır kalıpları (kopyala-uyarla)

```
YAKLAŞMA (insanlı iç):  Low cabin hum; slow breathing on the radio
  channel; the synthetic line at Xs, heard only — never shown as
  text. No music.
DIŞ + TELSİZ REPLİĞİ:   No exterior sound — hard vacuum. Only the
  radio channel: faint carrier hiss and the single spoken line at
  Xs, heard only. No music.
TEMAS (doruk):          Hard vacuum — no exterior sound at all, even
  at contact. Only the radio channel's faint carrier hiss and two
  held human breaths that release, slowly, just after contact. No
  voice, no music.
KENET + ONAY:           ... faint carrier hiss, two slow breaths, and
  the whispered line at Xs, heard only — never shown as text.
```

---

# 9. 📌 PLANLANAN BÖLÜMLER — henüz yazılmadı, adresleri şimdilik şurası

```
§3 SAYISAL FİZİK ÇEKİRDEĞİ (tek tablo)   → şimdilik: film planlarının
   gerçekçilik çıpaları (Black Cradle çıpa 5-9) + uzamsal §5.3
§4 HANGİ-UÇ-ÖNDE TERSLEME TABLOSU        → şimdilik: uzamsal §4.8 +
   §5.6 uyarıları + bu dosya §1.4
§5 REFERANS PAKETİ + I2V TEMAS ZİNCİRİ   → şimdilik: Cold Burn
   REFERANS_PAKETI emsali + 7-9 dk formatının start/end mimarisi
§6 BETİK DENETİMLERİ (oran cümlesi /     → prompt_kontrol.py'ye
   uç cümlesi yoklaması)                    önerilecek; henüz kodda yok
```

> **Bu dosya ne zaman güncellenir**
> □ Yeni yanaşma filmi üretilip QA'dan geçince → §1 tablosuna kanıt
>   sütunu güncellenir; kadraj kararlarından biri batarsa satırı 🔴'ya
>   çevrilir ve sebep yazılır
> □ §9'daki bir bölüm yazılınca → buradan silinir, gerçek bölüm açılır
> □ Ses/dramaturji kararlarından biri bir filmde bilinçli DELİNİRSE →
>   §2'ye "bilinçli sapma" emsali olarak işlenir, kural gevşetilmez
