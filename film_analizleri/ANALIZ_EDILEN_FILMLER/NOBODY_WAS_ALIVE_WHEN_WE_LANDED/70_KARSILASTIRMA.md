# 📐 KARŞILAŞTIRMA — kaynak film ↔ bizim filmlerimiz

> **Neden yazıldı (16.08.2026):** Bu analizin seçkisi
> (`60_DERS_SECKISI.md`) iki filme uygulandı — THE HOLLOW COUNT ve
> THE LAST SHIFT — ve ilkinin ardından proje sahibinin tepkisi şu oldu:
> *"filme hiç benzemiyor, analizler yanlış mı oldu?"*
> Analizler yanlış değildi. **Seçki, filmin nasıl ÇEKİLDİĞİNİ taşıdı;
> ne olduğunu taşımadı.** Bu dosya farkı sayıyla gösterir.
>
> Buradaki bütün sayılar 66 parça raporunun kendi header satırlarından
> ve shot listelerinden toplandı — yeni bir koşu yapılmadı, model
> yorumuna dayanmıyor. Sayım tarifi §5'te.

---

## 1 · İKİ FİLM, ÖLÇÜLMÜŞ HÂLİYLE

| Ölçü | **Kaynak film** (69:20) | **Bizim yatay 2-4 dk** (41 dosya) | Fark |
|---|---|---|---|
| Toplam çekim | **468** | 12-18 (yeni iki film 23-24) | — |
| ASL (film düzeyi) | **8.9 s** · parça ort. 9.4 s · bant 5.8-21.7 | ~10 s (sabit ızgara) | ≈ eşit |
| **Çekim / dakika** | **6.8** | 6.0-7.6 | ✅ **eşit** |
| **Sahne** (mekân-zaman birimi) | **109** → dakikada 1.6, **her ~38 saniyede yeni sahne** | **1** — film boyunca tek mekân, tek yürüyüş | 🔴 **~40×** |
| Replik | **242** → **3.5 / dakika** | 12 filmin 7'sinde **0**; replikli 5 film: 5·7·8·9·13 | 🔴 |
| Kadro | 4 ana + çocuk + kalabalık asker | **1** (iki filmde 2) | 🔴 |
| Kamera hareketi | **%44 hareketli** (dolly/track 86 · handheld 54 · steadicam 24 · pan 18 · drone 7 · crane 5 · zoom 3 · tilt 3 · whip 2) | **%0** — 14/14 sabit kilitli kadraj | 🔴 |
| Kamera açısı | göz hizası %58 · **alçak %24** · yüksek %13 · omuz üstü / overhead / POV %5 | ~%100 göz veya göğüs hizası | 🔴 |
| Ölçek dağılımı | MS %24 · **CU %19** · **MCU %17** · WS %16 · EWS %9 · MWS %8 · **ECU %5** | sahne başına tek ölçek; **yüz kadrajı bilinçli olarak yasak** | 🔴 |
| Yapı | 5 perde (uyarı → yolculuk → koloni → gerçek → bedel) | tek yay | 🔴 |

---

## 2 · ⭐ ÜÇ GERÇEK FARK — geri kalanı bunlardan türüyor

### ① "SAHNE" kelimesi iki ayrı şeyi anlatıyor — ve fark burada saklandı

Bizde **sahne = çekim**. "14 sahneli film" dediğimiz şey, kaynak filmin
diliyle **14 çekimlik TEK sahnedir**: aynı ova, aynı ışık, aynı yürüyüş.

Kaynak filmde sahne = **mekân-zaman birimi** ve 69 dakikada 109 tane var.
Tek bir parçada (P19) 13 sahne sayıldı; P20'de 9. Yani seyirci her
yarım dakikada yeni bir yere gidiyor.

> **Ölçülmüş sonuç:** kesme hızımız kaynak filmle aynı (6.8 ↔ 6-7.6
> çekim/dakika). Eksik olan kesme değil, **MEKÂN DEĞİŞİMİ.** Bizim
> filmlerimiz hızlı kesilen tek bir sahnedir.

### ② Kaynak bir YÜZ filmi, bizimki bir MANZARA filmi

461 çekimin **%41'i** CU, MCU veya ECU — yani neredeyse yarısı bir
yüzün okunabildiği ölçekte. Bizim kamera bible'larımızda ise yazılı
kural şu: *"100mm ve üstü YOK: bu film yüze yaklaşmaz."*

Bu bir zevk farkı değil, bir **risk kararı**: D69 (klon), D91 (organ/
taraf sapması), D16 (face lock) yüze yaklaştıkça pahalılaşıyor. Yani
kaynak filmin duygusal kanalının yarısını üretim güvenliği için kapattık.

### ③ Kaynak filmin motoru İNSANLAR ARASI BİLGİ AKIŞI

Dakikada 3.5 replik, dört karakter, bir tanık, bir çevirmen. Filmin
zirvesi (P16) bir manzara değil bir **konuşmadır**: çocuk konuşur,
makine çevirir, ekip anlar. Bizim hattımızda replik = Kart 7 = dudak-
fonem riski; çözümümüz "replikler gövdesiz makineden gelir, insanlar
hiç konuşmaz" oldu.

> Üç fark tek cümlede: **kaynak filmi film yapan üç şeyin (mekân
> değişimi · yüz · konuşma) üçü de bizim risk kartlarımızda kırmızı.**
> "Tema aynı olsun" isteği, teknik olarak "üç kartı birden aç" demektir.
> Yapılabilir — ama plan seviyesinde ödenir, prompt seviyesinde değil.

---

## 3 · ⛔ ANALİZ SİSTEMİNİN KENDİ SORUNLARI

> Klasör iyi kurulmuş ve raporlar gerçekten yüksek çözünürlüklü
> (shot listeleri kullanılabilir durumda). Sorunlar üretimde değil,
> **çıkarımda ve kapsamda.**

```
🔴 1. SEÇKİ YALNIZ PROMPTA ÇEVRİLEBİLENİ ALDI
   60_DERS_SECKISI'nin süzgeci açıkça yazılı: "(b) sayısal kilide
   çevrilebilen". Bu süzgeç kamera cümlelerini geçirdi (A1-A4),
   ama filmin GERÇEK ölçülerini — sahne/dakika, kadro, replik
   yoğunluğu, ölçek dağılımı — elemiş oldu; çünkü onlar prompt
   cümlesi değil PLAN SAYISIDIR.
   Sonuç: seçki "nasıl çekilir" öğretti, "ne çekilir" öğretmedi.
   İki saha denemesinin ikisi de tam bu boşluğa düştü.
   → ÇÖZÜM: §4'teki ÖLÇÜ KARTI seçkiye eklenir.

🔴 2. ÖLÇÜM HATASI: "LOCKOFF ESTETİĞİ"
   50_TAM_FILM_ANALIZI §3: "Baskın hareket: static (13/20 partta) —
   lockoff estetiği". PART BAŞINA baskınlık doğru, ama ÇEKİM PAYI
   şunu diyor: 461 çekimin 257'si statik (%55.7), 204'ü hareketli
   (%44.3). Film lockoff çekilmiş DEĞİL.
   Bu cümle "kaynak film de bizim gibi sabit çekiyor" diye okunuyor
   ve iki filmimizin kamera bible'ı doğrudan buna dayandırıldı.
   → ÇÖZÜM: §3'e çekim payı satırı eklenir, "lockoff estetiği"
     ibaresi "statik ağırlıklı ama %44 hareketli" olarak düzeltilir.

🟡 3. n = 1 · VE O DA YANLIŞ BANTTAN
   Tek analiz edilen film 69 dakikalık bir ENSEMBLE. Bizim üretim
   bandımız 2-4 ve 3-5 dakika. Sahne ekonomisi, kadro, perde yapısı
   bu uzunluktan taşınmıyor — yalnız kadraj dersleri taşınıyor
   (nitekim taşınan da tam olarak o oldu).
   → ÇÖZÜM: ikinci film 2-10 dakikalık bir kısa olmalı.

🟡 4. KAYNAK FİLM MUHTEMELEN AI ÜRETİMİ
   Künye "Dreamina" jeneriğini kaydediyor. Bu bir AVANTAJ (bizim
   kısıtlarımızla çalışan biri 69 dakika çıkarmış) ama bir UYARI:
   filmin kendi zaafları — kimlik erozyonu, taraf değiştiren yara izi,
   ödenmemiş üç kurulum — bizim zaaflarımızın aynısı. Emsal değil,
   akran. Ders çıkarırken "o yapabildiyse doğrudur" denemez.

🟡 5. VERİ KİRLİLİĞİ HÂLÂ DURUYOR
   66 raporun 63'ünde header "(not supplied)". Üç part kendine sahte
   part numarası uydurdu (P07·P09·P18), P09 timecode bile uydurdu.
   Süreç dersi yazıldı ama VERİ temizlenmedi: 91_SENTEZ_PAKETI bu
   raporlardan kuruldu ve sentez ondan koşulacak.
   Ayrıca shot listelerinde hücre kayması var: "over-shoulder" ve
   "POV" bazı raporlarda HAREKET sütununa yazılmış (2+4 satır) —
   sayım yaparken elle ayıklandı.

🟡 6. EKSİK KOŞULAR
   · 99_SENTEZ_RAPORU hiç koşulmadı → 50_TAM_FILM_ANALIZI tek okuma,
     karşılaştırması yok (oysa README ikinci okumayı öngörüyor).
   · 🧍 KARAKTER merceği 20 partın yalnız 5'ine koşuldu — README'nin
     kendi kuralına aykırı ("ya bütün partlara ya hiç"), ve en değerli
     bulgu (partlar ARASI kimlik erozyonu) tam da bu yüzden yarım.
```

---

## 4 · ⭐ ÖLÇÜ KARTI — analiz sistemine eklenecek dördüncü adım

> Bu tablo yeni bir model koşusu gerektirmiyor. Üç merceğin header
> satırları zaten şu dört sayıyı üretiyor: `SHOTS · ASL · SCENES ·
> DIALOGUE LINES`. Tek yapılacak iş onları bir yere toplamak.
> Bugün elle yapıldı, beş dakika sürdü ve seçkinin göremediği üç farkı
> buldu.

```
ÖLÇÜ KARTI — her analiz edilen film için doldurulur

  süre ....................... 69:20
  toplam çekim ............... 468        → çekim/dakika  6.8
  ASL ........................ 8.9 s      → bant 5.8-21.7
  toplam sahne ............... 109        → sahne/dakika   1.6
  saniye/sahne ............... 38 s
  toplam replik .............. 242        → replik/dakika  3.5
  kadro (adlandırılmış) ...... 4 + 1 tanık + figüran
  hareket payı ............... statik %56 · hareketli %44
  açı payı ................... göz %58 · alçak %24 · yüksek %13 · diğer %5
  ölçek payı ................. yakın (ECU+CU+MCU) %41 · orta %32 · geniş %25
  perde sayısı ............... 5

⭐ BİZİM FİLM İÇİN AYNI KART — plan yazılırken doldurulur ve
   kaynak filmin kartıyla YAN YANA konur. Hangi satırı bilinçli
   olarak farklı bıraktığımız planda yazılı olmalı; yazılı değilse
   o satır bir karar değil, bir ihmaldir.
```

---

## 5 · SAYIM TARİFİ (tekrar üretilebilir)

```bash
cd film_analizleri/ANALIZ_EDILEN_FILMLER/<FILM>/

# çekim ve ASL
grep -hoE "SHOTS: *[0-9]+" PARCA_*_KAMERA.md
grep -hoE "ASL: *[0-9.]+s"  PARCA_*_KAMERA.md

# sahne ve replik
grep -hoE "^SCENES: *[0-9]+"        PARCA_*_OLAY.md
grep -hoE "DIALOGUE LINES: *[0-9]+" PARCA_*_OLAY.md

# hareket / açı / ölçek payı (shot listelerinin sütunları)
grep -h "^| [0-9]" PARCA_*_KAMERA.md | awk -F'|' '{print tolower($6)}' | sort | uniq -c   # hareket
grep -h "^| [0-9]" PARCA_*_KAMERA.md | awk -F'|' '{print tolower($5)}' | sort | uniq -c   # açı
grep -h "^| [0-9]" PARCA_*_KAMERA.md | awk -F'|' '{print toupper($4)}' | sort | uniq -c   # ölçek

# header kirliliği
grep -l "not supplied" PARCA_*.md | wc -l
```

---

## 6 · SONUÇ VE SIRADAKİ ADIM

```
SORUN TEK CÜMLEDE
  Analiz doğru; seçki eksik. Filmin KADRAJINI aldık, EKONOMİSİNİ
  almadık — ve bir filmi o filme benzeten şey ekonomisidir:
  kaç mekân, kaç kişi, dakikada kaç replik, ne kadar yakın.

⭐ AÇILIŞ SIRASI — "kaynak filme benzesin" istendiğinde hangi kart
   önce açılır (ucuzdan pahalıya, üretim riskine göre):
   1. MEKÂN DEĞİŞİMİ   en ucuz. Kimlik riski yok, devamlılık riski
                       yönetilebilir. En büyük benzerlik kazancı.
   2. ÖLÇEK / AÇI      orta. Alçak açı ve omuz üstü bedava; yakın
                       plan pahalı (kimlik).
   3. REPLİK           pahalı (Kart 7). Gövdesiz makine sesi ucuz
                       versiyonu; ağız oynayan insan repliği pahalı.
   4. KADRO ve YÜZ     en pahalı (Kart 4 + D69/D91). En sona bırakılır.

SIRADAKİ ADIM
  1. Bu dosyadaki iki düzeltme 50_TAM_FILM_ANALIZI'ye işlenir
     (çekim payı satırı · "lockoff estetiği" ibaresi).
  2. 60_DERS_SECKISI'ne TAŞINABİLİRLİK sütunu eklenir: her ders
     hangi süre bandında çalışır. (B1 = 18 partlık ironi motoru
     2:20'de çalışmaz; A1 = sırttan çekim her bandda çalışır.)
  3. İkinci film seçilirken 2-10 dakikalık bir kısa alınır ve
     ÖLÇÜ KARTI ilk günden doldurulur.
  4. Eksik koşular: 99_SENTEZ + KARAKTER (P01-P08, P15-P20).
```

> ⛔ **Bu dosya ders üretmez.** Buradaki bulgular LESSONS_LEARNED'a
> ancak AGENTS.md görev kartı G ile ve bir üretim ölçümünden sonra
> girer. Şu an elde iki yazılmış, sıfır üretilmiş film var.
