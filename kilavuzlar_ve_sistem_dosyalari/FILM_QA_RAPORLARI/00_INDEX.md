# 📇 FİLM QA RAPORLARI — KONTROL LİSTESİ

> **Amaç:** Hangi filmin eleştirisi var, hangisinin yok — tek bakışta.
> **Veri kaynağı:** `LESSONS_LEARNED.md` (kalite tablosu + derslerin kaynak
> satırları) ve `yatay_7_9_dk_filmler/THE_SLOW_STONE/QA_RAPORU.md`
> **Oluşturma:** 31 Temmuz 2026

```
✅ = QA verisi var, bu klasörde dosyası var
❌ = eleştirisi YOK — QA raporu verilmeyi bekliyor
```

> ⚠️ **✅ işaretli 11 dosya geri-çıkarımdır (reverse-extraction).**
> Sadece The Slow Stone'un orijinal QA raporu dosya olarak duruyor. Diğer 11
> filmin ham QA raporu kaybolmuş; elimizde sadece derslere yazılan özetler var.

> 🆕 **31.07.2026 — İlk SENARYO QA'ları sisteme girdi: THE RING WALKER (5/10
> şartlı) ve LOW POWER (🚨 geçersiz SPEC).** İki ham rapor da
> `02_HAM_RAPORLAR/` altında **korundu** — veri kaybı zinciri bu raporlarla
> kırıldı. Hikaye puanları teknik tablodan ayrı tutuluyor:
> [`03_HIKAYE_KALITE_TABLOSU.md`](03_HIKAYE_KALITE_TABLOSU.md)
>
> Tablolardaki **Kapsam** sütunu teknik (VIDEO_QA) geçişi gösterir.
> Senaryo QA'sı olan filmler ayrıca 📖 ile işaretlidir.

---

# 🔢 SAYIM

```
TOPLAM FİLM                65   ← kaynak her zaman sayac.sh'tir; betik artık
                                bu sayıyı kendisi karşılaştırıp ❌ basıyor
                                (12.08.2026: zombi+savaş filmleri silindi,
                                59→57 · 13.08.2026: THE PLUMB LINE ve
                                THE BLIND BERTH yazıldı sonra ikisi de
                                silindi — net değişim yok, 57'de kaldı ·
                                14.08.2026: THE BANDED DEEP yazıldı +1;
                                ayrıca betik 58 sayarken INDEX 57 diyordu —
                                önceden kalan 1'lik fark bu güncellemeyle
                                kapatıldı, 57→59 · 15.08.2026: THE SLOW
                                LIGHT yazıldı, 59→60 · 15.08.2026:
                                THE HOLLOW COUNT yazıldı +1, ama
                                ⛔ THE SLOW LIGHT'IN DOSYASI DEPODA YOK
                                (`yatay_2_4_dk_filmler_uzay/THE_SLOW_
                                LIGHT_RELAY_FIELD_FILM.md` hiçbir
                                commit'te ve çalışma ağacında yok; hem
                                bu INDEX hem KILAVUZ_REHBERI §8 hem de
                                film_analizleri/.../60_DERS_SECKISI ona
                                atıf veriyor) −1 → net değişim yok,
                                60'ta kaldı. Dosya bulunur/yeniden
                                yazılırsa sayı 62 olur ·
                                16.08.2026: THE LAST SHIFT yazıldı,
                                60→61 · 16.08.2026: THE BLACK CRADLE
                                planı yazıldı (3-5 dk klasörü), 61→62 ·
                                16.08.2026: THE BLACK CRADLE FRAGMAN
                                yazıldı (dikey shorts), 62→63 ·
                                17.08.2026: THE BLACK CRADLE FRAGMAN 2
                                yazıldı ve AYNI GÜN silindi — birinci
                                fragmanın varlığı unutulmuştu; imzayı
                                (geri geri yanaşma) satan FRAGMAN 1
                                tutuldu. Net değişim yok, 63'te kaldı ·
                                17.08.2026: FRAGMAN 1 kaynak filmin
                                klasörüne taşındı (Second Ship emsali) —
                                dikey klasörden çıktı, artık film
                                sayımına girmez, 63→62 · 17.08.2026:
                                THE COLD BURN'ün dikey klasördeki
                                fragmanı (ÖLÇEK MERDİVENİ) SİLİNDİ —
                                filmin tek fragmanı kaynak film
                                klasöründeki KAPANAN KAPILAR dosyasıdır
                                ve sayıma girmez, 62→61 · 17.08.2026:
                                THE UPHILL DARK yazıldı (3-5 dk klasörü:
                                PLAN + PART_A + PART_B + KAPAK +
                                REFERANS_PAKETI), 61→62 · 17.08.2026:
                                THE BLUE DRIFT planı yazıldı (3-5 dk
                                klasörü — Cold Burn/Black Cradle
                                ailesinin MAVİ üçüncüsü), 62→63 ·
                                20.08.2026: LOSS OF LIFT planı yazıldı
                                (3-5 dk klasörü — LOW POWER'ın kardeşi,
                                Venüs bulut katmanı), 63→64 ·
                                21.08.2026: THE WAKING GROUND klasörü
                                depodan silindi (AGENTS §6'da "5 faz
                                dosyası yok" diye açık olarak duruyordu;
                                geriye kalan 3 dosya da kaldırıldı),
                                64→63 · 22.08.2026: THE BORROWED
                                WEIGHT yazıldı (3-5 dk klasörü) —
                                betik 64 sayarken INDEX 63 diyordu,
                                fark bu satırla kapatıldı, 63→64 ·
                                22.08.2026: THE SHORT WAY DOWN yazıldı
                                (dikey shorts — zombi kartı dikey
                                hatta geri açıldı), 64→65. Aynı gün
                                yazılan THE WARM FLOOR bu dosyayla
                                DEĞİŞTİRİLDİ (atmosferik gerilimden
                                kaçış aksiyonuna); net değişim yok,
                                65'te kaldı)
✅ QA VERİSİ OLAN          29   (%48 — film kaydı sayısı 30, ama biri
                                THE_BLACK_CRADLE_FRAGMAN: fragman film
                                sayımına girmez, 29+32 = 61 korunur ·
                                17.08: THE BLACK CRADLE kaydı açıldı,
                                beş mercek — dördü 🚨 GEÇERSİZ [D107])
❌ ELEŞTİRİSİ OLMAYAN      36   (%55 — 17.08: THE UPHILL DARK ve
                                THE BLUE DRIFT eklendi · 20.08: LOSS OF
                                LIFT eklendi · 22.08: THE BORROWED WEIGHT
                                ve THE SHORT WAY DOWN eklendi, 29 + 36 = 65)

TAM QA RAPORU OLAN          2   (The Slow Stone · Ring Walker senaryo geçişi)
KALİTE TABLOSUNDA OLAN     11   (The Last Crossing QA edildi ama tabloya girmedi)
6/10 VE ÜSTÜ ALAN FİLM      0

📖 SENARYO QA'SI OLAN      15   (Black Cradle Ⓥ 🚨 GEÇERSİZ 🆕 17.08 — mercek
                                23 kliplik kurguyu DÖRT SAHNE saydı (aynı
                                dosyada VIDEO_QA 21 kesme); 85 s'lik "sahne"
                                bu hatta üretilemez → DERS 107. Belge
                                kontrolünde üç iddia düştü (bedelli seçim
                                S17'de VAR · umut anı VAR · zirve S21) ·
                                kesme listesi UYGULANMAZ, 1. sırası
                                KESİLEMEZ viral ara S4
                                · Last Shift Ⓥ 6.0 🆕 16.08 — ⛔ ÖN KOŞU [D94],
                                Diyalog 9/10 tablonun en yükseği (13/13 gövdesiz
                                makine replik); Karakter 4 ve Kanca 4 belge
                                kontrolünde DÜŞTÜ (esirgeme haritası + ECU açılış
                                §0.15'te yazılıydı) → DERS 102 · kesme listesi
                                UYGULANMAZ, 1. sırası KESİLEMEZ viral ara
                                · Banded Deep Ⓥ 7.4 🆕 14.08 — ⛔ ÖN KOŞU [D94],
                                tablonun en yüksek mod V skoru ama finalsiz
                                kurgunun puanı (S12-S15 ekranda yok)
                                · Ring Walker · Low Power · Kaleida Crash · Inversion
                                · Stone Sky Ⓥ · Unbroken City Ⓥ · Wrong Shadow Ⓥ
                                🆕 06.08 — dikey hattın ilk senaryo satırı, 3.0
                                serinin en düşüğü, çoğu kurgunun puanı
                                · Starless Circle 🚨 GEÇERSİZ — mercek 12 s'lik
                                TEK KLİBİ film gibi puanladı → DERS 75
                                · Blind Return Ⓥ 4.0 🆕 07.08 — DERS 75
                                kapısının İLK BAŞARILI koşusu; satırın yarısı
                                kurgunun puanı → DERS 81
                                · Cold Burn Ⓥ 4.0 🆕 09.08 — kurgu kapısının
                                4 maddesi birden ihlal, ilk kez; skorun büyük
                                kısmı 18 eksik sahnenin puanı
                                · Third Dune Ⓥ 7.0 🆕 11.08 — ⭐ TABLONUN EN
                                YÜKSEK MOD V SKORU ve kontrol grubu: planın
                                25 sahnesi kurguya girdi, skor 4-5 bandından
                                7.0'a çıktı → düşük hikaye skorlarının kökü
                                içerik değil KURGU KAYBI (D72/81 doğrulandı).
                                ⚠️ kesme listesi UYGULANMAZ: iki öneri de
                                viral ara sahneye giriyor, biri ORTA NOKTA
                                REVEAL'ini siliyor
                                · Ring Light Ⓥ 6.0 🆕 12.08 — kurgu kapısını
                                TAM geçen ilk film (14/14 sahne + doruk
                                ekranda) ve skor yine 6.0: kayıp yokken de
                                mod V bandı değişmiyor. Final 4/10 filmin
                                değil KURGUNUN puanı — 2:20 jenerik kartı
                                held frame finali "teaser"a çevirdi.
                                ⚠️ kesme listesi UYGULANMAZ: 1. sıra planın
                                KESİLEMEZ viral arası S2)

📱 SHORTS QA'SI OLAN        3   (First Morning Ⓥ 6.0 · Wrong Shadow Ⓥ 5.6 —
                                ikisi de REGENERATE, ikisinde de 64 s kurgu +
                                jenerik kartı → 05_SHORTS_KALITE_TABLOSU.md
                                06.08'de AÇILDI; rubrik borcu kapandı
                                · Black Cradle — Fragman 🚨 ~~6.5~~ 🆕 17.08:
                                skor GEÇERSİZ, ölçülen nesnenin KİMLİĞİ
                                doğrulanmadı — raporu fragmana bağlayan tek
                                kanıt yanan başlık kartıydı, 6 vuruşun 6'sı
                                tutmadı → DERS 105 · DERS 106. Üçüncü kez
                                aynı imza: ~10 s sahneler + sondaki kart)
📖 İKİ RUBRİKLE ÖLÇÜLEN     4   (Inversion'ın teknik QA'sı YOK — yalnız hikaye)
📖 DOĞRULANMIŞ HİKAYE SKORU 0   (4 ŞARTLI · 1 GEÇERSİZ — beşi de dokümansız çalıştı)

🧩 MANTIK QA'SI OLAN       14   (Black Cradle 🚨 GEÇERSİZ 🆕 17.08 — 4 sahnelik
                                envanter [D107] + Fizik ve Nedensellik
                                hücrelerinin kaynağı kapsam dışı [D108];
                                düzeltilmiş okuma ~8.4 · Sayaç yine N/A,
                                planda DÖRT sayaç (D78 ×5)
                                · Last Shift 5.0 🆕 16.08 ⚠️ ŞARTLI — Sayaç yine
                                N/A, planda ÜÇ çevresel sayaç vardı (D78 ×4);
                                Coğrafya bulgusunun yarısı D87'de düştü
                                (checkerboard = filmin novum'u)
                                · Kaleida 4.0 · Inversion 3.0 · Tidal Hunt 4.0
                                Last Archive 5.0 · Canopy World 5.0
                                Deep Pressure 3.0 🚨 planı olmayan tek film
                                Holding Field 4.0 🚨 öncül ters render edildi
                                The Herd 4.0 🚨 iki bulgusu belge kontrolünde çürüdü
                                Dawn Front 3.0 🆕 Kostüm-Prop 1/10 · Zaman-Işık 9/10 rekor
                                Stone Sky 4.0 · Unbroken City 8.0 🆕 serinin
                                en yüksek mantık skoru
                                Starless Circle 5.5 🆕 Nicelik 1/10 klon ·
                                Sayaç yine N/A — planda DÖRT çevresel sayaç
                                · Blind Return 4.0 🆕 07.08 — dört MAJOR'ın
                                dördü belge kontrolünde kimlik değiştirdi:
                                kök neden kurgu (S15 yok + S16↔S17 ters)
                                → DERS 81
                                · Cold Burn 7.0 🆕 09.08 — serinin en yüksek
                                2. mantık skoru · Sayaç N/A ⚠️ planda İKİ
                                kanal vardı (D78 ×3) · Nicelik 10/10 rekor
                                · Third Dune 7.0 🆕 11.08 — ⭐ SAYAÇ İLK KEZ
                                10/10 (fırtına duvarı; D78'in üç başarısız
                                vakasından sonra çalışan ilk çevresel sayaç)
                                ⚠️ Coğrafya 4/10 ŞARTLI: üç MAJOR'ın ikisi
                                belge kontrolünde düştü — araç gömülmesi
                                filmin ORTA NOKTASI, çanak planlı S22
                                → DERS 87)
🧩 GEÇERSİZ/ŞARTLI MANTIK   1   (Black Cradle 17.08 — ilk geçersiz mantık satırı;
                                sebep rubrik değil ÖLÇÜM: sahne sayımı çelişkisi
                                + kapsam dışı faturalama [D107 · D108])
🧍 KARAKTER QA'SI OLAN      8   (Black Cradle 🚨 GEÇERSİZ 🆕 17.08 — kanıt tabanı
                                eşiği DELİNDİ: yüz 1/4 sahne · ~%11 süre, sekiz
                                sütunun yedisi yine puanlandı (D97 ×2); Ses
                                sütunu SES_QA koşulduğu hâlde puanlandı [D108]
                                · Stone Sky 6/10 🚨 IDENTITY BREAK — rubriğin
                                İLK koşusu → 06_KARAKTER_KALITE_TABLOSU.md açıldı
                                · Unbroken City 8/10 🆕 ikinci koşu, kimlik tuttu
                                · Starless Circle 6/10 🚨 IDENTITY BREAK — klon
                                gemiye BİNİŞ sahnesinde, DERS 69'un 3. vakası
                                · Blind Return 4/10 DRIFTS 🆕 07.08 — klonsuz;
                                üç MAJOR'ın üçü belge kontrolünde düştü/kurguya
                                devredildi; pasaport sırt ünitesi + çift lamba
                                yakaladı → DERS 79 ×3
                                · Cold Burn 6/10 DRIFTS 🆕 09.08 — klonsuz;
                                pasaport iki suitte de sırt ünitesi yakaladı
                                (D79 ×4, üretim zinciri şerhli); Ses sütunu
                                →🔊 işaretçi — kart E3 ilk kez uygulandı
                                · Third Dune 7/10 DRIFTS 🆕 11.08 — klonsuz
                                (iki karakterli ikinci koşu, D69/77 yine
                                tekrarlamadı) · Yıpranma 3/10'un sebebi ilk
                                kez EKSİK CÜMLE DEĞİL: toz takvimi + bant
                                rengi + sırt yasağı 42 promptta yazılıydı,
                                üçü de kırıldı → DERS 84 · D79 ×5
                                · Ring Light 8.5/10 ⚠️ 🆕 12.08 — tablonun
                                en yüksek skoru ve en zayıf tabanı: yüz
                                yalnız 20 s / 144 s görünüyor, dört sütun
                                filmin %14'ünden yazıldı → DERS 97 · Ses
                                sütunu planın yasakladığı bir ekran
                                repliğine puan verdi (N/A olmalıydı) ·
                                Kostüm 4/10 tek ayakta bulgu: S12↔S13 suit
                                sapması · klonsuz, Sayı 10/10)
🔊 SES QA'SI OLAN           3   (Black Cradle 🚨 GEÇERSİZ 🆕 17.08 — 2 replik
                                duyuldu, plan 14 diyor; register yarı yarıya
                                ters (MİRA'nın repliği ekrandaki kadına
                                atfedildi = D82 sınıfı) · ✅ plandaki register
                                haritası ALET olarak çalıştı
                                · Banded Deep 6.2 SOUNDTRACK HOLDS 🆕 14.08 —
                                STATE B, 0 replik tasarım; ilk beş kategori
                                N/A; üç bulgu da miks işi, yeniden üretim yok
                                · Cold Burn 5.0 AUDIBLE DRIFT 🆕 09.08 —
                                rubriğin İLK koşusu, yazıldığı gün →
                                07_SES_KALITE_TABLOSU.md bu koşuyla AÇILDI.
                                İlk koşunun örüntüsü: ATIF 9, ORTAM 3 —
                                doğru ses doğru bedenden çıkıyor, yatak her
                                kesmede ölüyor → DERS 82-83. Register
                                haritası planla çelişti: 7 HUMAN / 0 MACHINE,
                                plan "hepsi telsiz + gövdesiz EKO" diyordu)
🎯 ÜÇ MERCEKLE DE ÖLÇÜLEN   7   (⭐ Black Cradle 17.08 BEŞ raporlu İKİNCİ film
                                (Cold Burn'den sonra) — ama beşi AYNI OTURUMDA
                                koşuldu ve birbirinin defterini devraldı, yani
                                beş bağımsız ölçüm DEĞİL [DERS 110]
                                · Kaleida Crash · Stone Sky · Unbroken City ·
                                Starless Circle · Cold Burn · Third Dune —
                                Stone Sky/Unbroken/Starless 🧍 ile DÖRT
                                raporlu; ⭐ Cold Burn 🧍+🔊 ile BEŞ raporlu
                                İLK film; Third Dune DÖRT raporlu (🔊 koşusu
                                girdisiz kaldı → geçersiz, D80'in 2. vakası);
                                Starless Circle'ın 📖 satırı GEÇERSİZ)

📏 İKİ KEZ ÖLÇÜLEN FİLM     1   (Canopy World: 4/10 → 3/10)
📏 ÖLÇÜM SAPMASI          ±1.3  ⚠️ tablodaki 1.5'tan küçük farklar GÜRÜLTÜ

🆕 QA'DAN ÇIKAN YENİ DERS  40   (45 senaryo · 46-50 mantık · 51-54 QA'nın kendisi
                                55-58 mantık — Deep Pressure · 59 Holding Field
                                60-62 The Herd — üçü de ÖLÇME ALETİ hatası
                                ⚠️ 60-62 numaraları İKİ ders bloğunda çakışık
                                63-66 QA aleti · 67-68 Dawn Front
                                · 69 Stone Sky — klon sıcak noktası 🆕 05.08
                                · 70-71 First Morning — kurgu kapısı + analog perde
                                · 72 Unbroken City — kurgu kapısı yataya
                                · 73-74 Wrong Shadow — novum taşıyıcısı +
                                kapı kaydı 🆕 06.08
                                · 75-79 Starless Circle — mod V malzeme kapısı ·
                                yokluk novum'u · dersin plana akmaması ·
                                sahneler arası anlatım · bible↔çekirdek 🆕 06.08
                                · 80-81 Blind Return — medya kapısı ·
                                kurgu kapısı v2 (sıra + kurulum) 🆕 07.08
                                · 82-83 Cold Burn — ses mimarisi tersine döndü ·
                                ortam yatağı/ses kapısı 🆕 09.08, ikisi de
                                SES_QA'nın İLK koşusundan
                                · 84-87 Third Dune 🆕 11.08
                                · 88-92 Second Ship Faz 7 🆕 12.08
                                · 93-99 Ring Light 🆕 12.08 — yedisi de
                                ÖLÇME ALETİ dersi: filme özel rubrik jenerik
                                kartıyla sustu (93) · SPEC hazırken mod V'nin
                                bedeli (94) · görünmez kilit (95) · kilit
                                çelişkisi defteri (96) · kanıt tabanı (97) ·
                                sayım kutusunun yuttuğu blocker (98)
                                ⚠️ bu satırdaki 40 sayısı BAYAT — gerçek
                                kaynak LESSONS_LEARNED.md ders dizinidir)
🚫 GİRDİSİZ ÇALIŞTIRMA      4   (01.08 — üç mercek, 0 geçerli skor ·
                                07.08 Blind Return VIDEO_QA — videosuz koşu
                                REGENERATE verdikti yazdı → DERS 80)
```

> 📏 **31.07.2026'da ölçülen en önemli sayı ±1.3.** Canopy World aynı
> rubrikle ikinci kez ölçüldü ve kategoriler 2 puana kadar oynadı
> (Karakter 7→5, Işık 6→4). Bu, kalite tablosunun filmleri **birbiriyle
> sıralayamayacağı** anlamına geliyor: "Kaleida 4.5 > Hollow 4.0" artık
> geçerli bir cümle değil. Büyük farklar (Kamera 8 vs ortalama 4.2) ve
> çok filmli örüntüler (Fizik 11/11 ≤5) etkilenmiyor.
> Ayrıntı: `../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` §6b

> ⚠️ **Yukarıdaki sayılar elle yazıldı.** Doğrulamak için:
> `bash ../sayac.sh` — dosya sisteminden hesaplar, hiçbir belgeye güvenmez.

---

# 🎯 QA TAMLIK MATRİSİ — her film kaç mercekle ölçüldü

> **Soru:** Bir filmin QA'sı tam mı, eksik mi?
> **Cevap:** **Dört mercek var** (22.08.2026'dan beri):
> ① 🔧 KARE · ② 🔗 DEVAMLILIK · ③ 🔊 SES · ④ 📖 HİKAYE. Payda **/4**.

```
✅ ölçüldü, geçerli      ⚠️ ölçüldü ama ŞARTLI/kısmi
🚨 ölçüldü, GEÇERSİZ     ❌ hiç ölçülmedi
⛔ ön koşu               ölçüldü sayılmaz (SPEC hazırdı, mod V koşuldu)
⚠️ eski                  arşivlenmiş rubrikle ölçüldü — ham rapor duruyor,
                        ama yeni mercekle yeniden koşulmadı
```

> ## ⚠️ BU MATRİSTEKİ HER DOLU HÜCRE ESKİ SİSTEMİN ÖLÇÜMÜDÜR
>
> 22.08.2026'da altı mercek dörde indi ve altı rubriğin hepsi arşive girdi
> (`../QA_PROMPTLARI/ARSIV_6_MERCEK/`). Bu matristeki mevcut değerler o
> arşivlenmiş aletlerle alındı. Sütunların yeni adlarla anılması eski
> ölçümü yeni ölçüm yapmaz.
>
> **En önemli şerh ② sütununda:** eski sistemde mantık ve karakter AYRI
> merceklerdi ve karakter merceği OPSİYONELDİ. Bu sütundaki ✅'lerin çoğu
> yalnız **dünya yarısının** ölçümüdür — gövde yarısı (kimlik, kostüm,
> yıpranma, ekipman) hiç ölçülmemiştir. Yeni ② mercek ikisini birden
> ister; dolayısıyla o hücreler bugünün paydasında **yarım ölçümdür.**
>
> ```
> ⛔ HİÇBİR FİLM HENÜZ 4/4 DEĞİL — dört merceğin hiçbiri henüz
>    hiçbir filme koşulmadı. Yeni koşu geldiğinde hücre değeriyle
>    birlikte "⚠️ eski" işareti düşer.
> ```
>
> Eski skorların yaşadığı tablolar da aynı gün kapandı; yeni satırlar
> `T1_KARE_KALITE.md` · `T2_DEVAMLILIK_KALITE.md` · `T3_SES_KALITE.md` ·
> `T4_HIKAYE_KALITE.md` dosyalarına yazılır.

| Film | ① 🔧 KARE | ② 🔗 DEVAMLILIK | ③ 🔊 SES | ④ 📖 HİKAYE | Tamlık |
|---|:---:|:---:|:---:|:---:|:---:|
| **Kaleida Crash** | ✅ 4.5 | ✅ 4.0 | ❌ | ⚠️ 5.1 | **3/4** ⭐ |
| **The Inversion** | ❌ | ✅ 3.0 | ❌ | ⚠️ 5.0 | 2/4 |
| **Tidal Hunt** | ✅ 3.0 | ✅ 4.0 | ❌ | ❌ | 2/4 |
| **Ring Walker** | ✅ 5.0 | ❌ | ❌ | ⚠️ 5.0 | 2/4 |
| **The Last Archive** | ⚠️ 4.0 | ✅ 5.0 | ❌ | ❌ | 2/4 |
| **The Dawn Front** | ✅ 4.0 | ✅ 3.0 | ❌ | ⛔ kapı | **2/4** 🆕 ilk dolu-SPEC'li dış koşu |
| **Canopy World** | ✅ ×2 | ✅ | ❌ | ❌ | 2/4 |
| **Low Power** | ⚠️ 4.0 | ❌ | ❌ | 🚨 geçersiz | 1/4 |
| **Deep Pressure** | ❌ | ✅ 3.0 | ❌ | ❌ | 1/4 🚨 plan dosyası yok |
| Dead Approach | ✅ 3.0 | ❌ | ❌ | ❌ | 1/4 |
| Deep Root | ✅ 5.0 | ❌ | ❌ | ❌ | 1/4 |
| Hollow Station | ✅ 4.0 | ❌ | ❌ | ❌ | 1/4 |
| Orphan Bloom | ✅ 5.0 | ❌ | ❌ | ❌ | 1/4 |
| Slow Tide | ✅ 5.0 | ❌ | ❌ | ❌ | 1/4 |
| The Slow Stone | ✅ 5.0 | ❌ | ❌ | ❌ | 1/4 |
| Last Crossing | ⚠️ 4.0 | ❌ | ❌ | ❌ | 1/4 |
| The Holding Field | ⛔ kapı | ✅ 4.0 | ❌ | ⛔ kapı | 1/4 🚨 öncül ters render |
| The Herd | 🚨 geçersiz | ✅ 4.0 | ❌ | 🚨 geçersiz | 1/4 🚨 iki mercek plan dosyasını aramadı |
| The Second Ship | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 10-20 dk · plan+bible+senaryo+kapak+müzik, faz dosyaları yok |
| ~~**The Herd** (plan satırı)~~ | | | | | 🆕 2-4 dk · kalın atmosfer · risk 6/9, üretim S3 ile başlar (ölçüm satırı yukarıda) |
| **The Half Sky** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 dikey shorts · vakum/yörünge · risk 4/9 · ⛔ SPEC bloğu dosyanın içinde yazılı |
| **The Stone Sky** | ✅Ⓥ 4.0 | ✅ 4.0 | ❌ | ⚠️Ⓥ 5.0 | **3/4** 🆕 05.08 · **+🧍 6.0 IDENTITY BREAK** — DÖRT raporlu ilk film · dördü de mod V, belge cevapları film kaydında · 🔴 klon S10-B (DERS 69) · 🔴 başlık kartı 2:10 (Ders 34 ×3) · 🚨 S12 overview kurguda yok (Ders 62 ×4) |
| **The Winter Line** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 dikey shorts · günümüz Dünya (2026) · risk 2/9 · ✅ 6 prompt Veo eşiği altında · ⛔ SPEC bloğu dosyanın içinde yazılı |
| **The Low Moon** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 dikey shorts · ince atm. (solunabilir) · kart riski 2/9, gerçek risk: sürekli hareket eden merkez nesne · ✅ 6 prompt Veo eşiği altında · ⛔ SPEC bloğu dosyanın içinde yazılı |
| **The Unbroken City** | ✅Ⓥ 5.0 | ✅ 8.0 | ❌ | ⚠️Ⓥ 5.0 | **3/4** 🆕 06.08 · **+🧍 8.0** — DÖRT raporlu İKİNCİ film (dördü mod V, belge cevapları film kaydında) · 🧩 8.0 serinin en yüksek mantık skoru · 🔴 klon 0:40 (DERS 69 tekrar — yeni sıcak nokta: loş iç mekân) · 🔴 yanık başlık 2:40 = kapak promptu başlığı sızdı · 🚨 doruk S9 seçimi kurguda YOK (Ders 62 ×5) → **DERS 72** · kurgu 165 s ≠ plan 160 s |
| **The First Morning** | ✅Ⓥ 6.0 📱 | ❌ | ❌ | ❌ | **1/4** 🆕 06.08 · 📱 SHORTS_QA (16 kategorili tek rubrik) mod V — **rubriğin İLK GEÇERLİ koşusu** · REGENERATE: 64 s kurgu + jenerik kartı → **DERS 70-71'in kaynağı** · film kaydı henüz yazılmadı |
| **The Wrong Shadow** | ✅Ⓥ 5.6 📱 | ❌ | ❌ | ⚠️Ⓥ 3.0 | **2/4** 🆕 06.08 · 📱+📖 aynı gün, ikisi mod V · REGENERATE (3 BLOCKER) · 🚨 **NOVUM EKRANA HİÇ GİRMEDİ** — çift gölge 64 s'de sıfır kare; dönme jalonlara transfer oldu → **DERS 73-74'ün kaynağı** · DERS 70 ikinci vaka (64 s + "THE DEVIL'S DOUBLE" kartı) · belge cevapları film kaydında |
| **The Starless Circle** | ⚠️Ⓥ 5.7 | ✅ 5.5 | ❌ | 🚨 geçersiz | **2/4** 🆕 06.08 · **+🧍 6.0 IDENTITY BREAK** — DÖRT raporlu ÜÇÜNCÜ film, ama **iki mercek 12 s'lik tek klibe, iki mercek 2:54'lük kurguya koşuldu** → 📖 satırı GEÇERSİZ (**DERS 75**), 🔧 satırı ŞARTLI (klip kimliği doğrulanmadı: çanak yok, yıldız yok, 12 s ≠ 10 s) · 🔴 klon 2:10 gemiye BİNİŞ sahnesinde = DERS 69'un 3. vakası, ders yazıldıktan bir gün sonra plana eklenen sahnede (**DERS 77**) · 🔴 2:50 yanık kart "THE CIRCLE WITH NO STARS" = KAPAK PROMPTU A'nın başlık satırı, Unbroken City ile birebir aynı zincir (DERS 72 2. vaka) · 🚨 novum nesneleşti: "yıldızsız daire" → "black sphere" (**DERS 76**) · dört çevresel sayaç + bedel nesnesi ekranda okunmadı (**DERS 78**) · sırt ünitesi + aynalı vizör bible'a rağmen geri geldi (**DERS 79**) · üç üretim kapısının kaydı yok (DERS 74 2. vaka) |
| ~~**The Starless Circle** (plan satırı)~~ | | | | | 2-4 dk · ince atm. GECE · risk 4/9 · 18×10 s = 3:00, 0 kesme, 4 viral ara, sessiz keşif — Unbroken City'nin ters aynası · 06.08: S14 biniş + S15 fırlatma + S16-S17 uzay viral kodası eklendi (S15-S17 insansız) · gerçek riskler kartlarda yok: gece pozlaması + yıldızsız daire (üretim S1→S0→S10 kapılarıyla başlar, koda en sona) · ✅ 36 prompt Veo eşiği altında · ⛔ SPEC bloğu dosyanın içinde yazılı (§0.15) |
| **The Blind Return** | 🚨 girdisiz | ✅ 4.0 | ❌ | ⚠️Ⓥ 4.0 | **2/4** 🆕 07.08 · **+🧍 4.0 DRIFTS** — üç mercek AYNI 169 s kurguyu ölçtü (Starless Circle arızası tekrarlamadı), 🔧 koşusuna ise video hiç yüklenmedi ve rapor yine de REGENERATE yazdı → **DERS 80** · üç merceğin "yapısal çöküş" bulgusunun kökü KURGU: S0-S14 plan ızgarasına saniyesi saniyesine oturuyor, sonra **S15 (Çehov 4) yok + S16↔S17 ters + kalkış görünmüyor** → **DERS 81** · doruk S11 kurguda VAR, ekran metni 0 ✅ (yanık kart zinciri ilk kez kırıldı) · 🧍 pasaport: sırt ünitesi + çift lamba + sağ uylukta tüp (bible: SOL) → DERS 79 ×3 · belge cevapları film kaydında |
| ~~**The Blind Return** (plan satırı)~~ | | | | | 2-4 dk · ince atm. Mars FIRTINA İÇİ · risk 5/9 TAM EŞİKTE · 18×10 s, 0 kesme, 8 replik hepsi SUIT AI (kadın hiç konuşmaz) · gerçek riskler kartlarda yok: fırtına loşluğuna icat ışık + laminer toz + vizör durum değişimi (çatlak→köpük→yeni vizör takvimli) + kalkış egzozu · üretim S6→S11→S4 kapılarıyla başlar · ✅ 36 prompt Veo eşiği altında · ⛔ SPEC bloğu dosyanın içinde yazılı (§0.15) |
| **The Cold Burn** | ✅Ⓥ 5.0 | ✅ 7.0 | ⚠️ eski | ⚠️Ⓥ 4.0 | **3/4** 🆕 09.08 · **+🧍 6.0 DRIFTS +🔊 5.0** — ⭐ **BEŞ raporlu İLK film + SES_QA'nın İLK koşusu** (beşi mod V, beşi AYNI 225 s kurgu — D75 ✅, belge cevapları film kaydında) · 🚨 **KURGU KAPISININ 4 MADDESİ BİRDEN İHLAL (ilk kez):** ekranda 12/40 sahne · 225 s ≠ 299 s · 3:40 yanık kart · CENTRAL CHOICE (S19) + DORUK (S26) + planlı final (S29) YOK → senaryo skoru büyük ölçüde kurgunun puanı · 🚨 **ses mimarisi tersine döndü:** EKO silindi, telsiz replikleri ekrandaki ağızlara devredildi (**DERS 82**) · 🔴 20 s mutlak sessizlik 1:20-1:40 (**DERS 83**) · 🧩 7.0 = serinin 2. en yüksek mantık skoru · klonsuz (D69 tekrarlamadı) · sırt ünitesi ×2 suit (D79 ×4 şerhli) · yakıt göstergesi ekranda yok (D78 ×3) · ❓ üretim PART_A/B promptlarıyla mı yapıldı — cevapsız, onarım planı film kaydında |
| **The Third Dune** | ✅Ⓥ 4.0 | ✅ 7.0 | ⚠️ eski | ⚠️Ⓥ **7.0** | **3/4** 🆕 11.08 · **+🧍 7.0 DRIFTS** — DÖRT mercek AYNI 245 s kurguyu ölçtü (D75 ✅), 🔊 koşusuna video yüklenmedi → geçersiz (**D80 ×2**) · ⭐ **📖 7.0 = tablonun en yüksek mod V hikaye skoru** ve sebebi kayıtlı: planın 25 sahnesi kurguya GİRDİ (25 klip · CENTRAL CHOICE S17 · DORUK S21 ekranda) — kurgu kapısı 3/5 geçti, Cold Burn'ün 0/4'ünün kontrol grubu · ⭐ 🧩 Sayaç ilk kez **10/10** (fırtına duvarı — D78'in çalışan ilk vakası) · ⚠️ 🧩 Coğrafya 4/10 ŞARTLI: üç MAJOR'ın ikisi belge kontrolünde düştü, araç gömülmesi filmin orta noktası (**DERS 87**) · 🔴 **üç çapa da promptta YAZILIYDI ve üçü de kırıldı** (toz takvimi · bant rengi · sırt yasağı, 42 promptta) → **DERS 84**, D79 ×5 · 🔴 4:00 yanık başlık kartı = kapak başlığının kurguya sızması (**D70/72 ×4**, kurgudan çıkarılınca kapanır) · ⚠️ 🔧 raporunun prompt reçetesi fabrikasyon çıktı → **DERS 85** · klonsuz · SPEC bloğu planda hazırdı, yine mod V koşuldu (operatör kuralı ② ×3) |
| ~~**The Cold Burn — Fragman** (plan satırı)~~ | | | | | 🆕 09.08 · dikey shorts · **klasörün ilk fragmanı** (kaynak film yukarıdaki satır) · filmin ilk %70'inden 6 vuruş; doruk S26 ve final S29 bilinçli olarak dışarıda · risk 5/9 · açık alev 0 kare · 6/6 lockoff · ⛔ SPEC bloğu dosyanın içinde yazılı (ölçüm satırı aşağıda) |
| **The Black Cradle — Fragman** | 🚨 | ❌ | ⚠️ eski | ❌ | **0/4** (📱 koşuldu ama ATFEDİLEMEDİ — 17.08, mod V; skor tabloya üstü çizili girdi, matris hücresi ❌ KALIR [D94 ön koşusu + D105 kimlik kapısı]. Film kaydı: `01_FILM_RAPORLARI/THE_BLACK_CRADLE_FRAGMAN.md`) 🆕 16.08 · dikey 9:16 teaser · ⭐ 17.08: dosya kaynak filmin KLASÖRÜNE taşındı (`yatay_3_5_dk_filmler/THE_BLACK_CRADLE/THE_BLACK_CRADLE_FRAGMAN.md` — Second Ship emsali) ve film SAYIMINA GİRMEZ · mekanik TERS KURALLAR · 6 vuruş, ilk %70'ten; temas/iptal/final dışarıda · 0 replik · 6/6 lockoff · risk 4/9, gerçek risk siyah-üstü-siyah · ⛔ kaynak film kurgu kapısından geçmeden üretime alınmaz · ⛔ SPEC bloğu dosyanın içinde yazılı |
| **The Cold Burn — Fragman** | ❌ | ❌ | ❌ | 🚨 | **0/4** (📖 koşuldu ama **YANLIŞ MERCEK** — 17.08, mod V Ⓥ6.0; skor HİÇBİR tabloya girmedi, matris hücresi ❌ sayılır. Film kaydı: `01_FILM_RAPORLARI/THE_COLD_BURN_FRAGMAN.md`) 🆕 17.08 · dikey 9:16 teaser, kaynak filmin klasöründe (`yatay_3_5_dk_filmler/THE_COLD_BURN/THE_COLD_BURN_FRAGMAN_DIKEY.md`), film SAYIMINA GİRMEZ · mekanik KAPANAN KAPILAR · 6 vuruş × 8 s = 48 s, 0 kesme, 6/6 lockoff, 0 replik, YÜZ 0 kare · 🚨 **fragmanın merceği SHORTS_QA'dır — `FRAGMAN_KILAVUZU` §0 SENARYO_QA'yı yasaklar, ama yasak yalnız kılavuzda yaşıyordu** → **DERS 111** (kardeş rubrik taraması; D106 aynı gün tek rubriğe işlenmişti) · 🚨 rapor 62 s / 7 segment / 0:58 başlık kartı bildirdi — Black Cradle fragman koşusuyla **birebir aynı geometri** → **DERS 112** (mod V'de süre ölçüm değil çıktıdır) · 🟡 yazılı YÜZ KİLİDİ "karakter 4/10" diye faturalandı → **DERS 113** (`N/A`, düşük puan değil) · 🟡 aynı oturumun paketleme metni fragmanın tüm yayını tek cümlede verdi → **DERS 114** · ✅ KİMLİK KAPISI [D105] GEÇTİ (V3 eldiven-konsol + insan sayımı 2/0/0/1/0/0) · ⛔ kilit çelişkisi defteri **7 ⬜ AÇIK** — dosya "üretilmedi" diyor, elde 62 s kurgu var; önce hangi belgenin bayat olduğu çözülür · ⛔ KAPI KAYDI'nın 5 kapısı da KOŞULMADI [D74] · ⛔ SPEC bloğu dosyanın içinde hazırdı, yapıştırılmadı [D94 ×8] |
| **The Ring Light** | ⛔ön koşu Ⓥ7.0 | ❌ | ❌ | ⛔ön koşu Ⓥ6.0 | **0/4** 🆕 12.08 · ⛔ **iki hücre de ön koşu, ölçülmedi sayılır [DERS 94]:** SPEC planda hazırdı, mod V koşuldu · **+🧍 8.5 ⚠️** — dört koşu aynı gün: üç genel mercek **mod V**, filmin KENDİ rubriği (MOD F) `CLIP COUNT MISMATCH` ile **DURDU** → 40+ sayısal kilidin hiçbiri ölçülmedi (**DERS 93**; sebep: kurguya eklenen 4 s'lik jenerik kartı, klip 14→15) · ⭐ **KURGU KAPISINI TAM GEÇEN İLK FİLM:** planın 14 sahnesinin 14'ü, 10 s ızgarada, doğru sırada — doruk S8 (1:26 karot bırakma), temas S11 (1:56), S12 avuç avuca (2:08), S13 tünel ekranda · 🔴 tek kurgu ihlali **2:20 yanık başlık kartı** = D70/72 zincirinin **5. vakası** (⛔ yasak İKİ yerde yazılıydı — §5 kapak + §0.18 ⑦ kurgu kapısı "ekran metni = 0.0 sn, jenerik kartı DAHİL"; yazılı madde koşulmadığı için tutmadı) · 🚨 **SPEC planda hazırdı, yine mod V koşuldu** (operatör kuralı ② ×4) ve bedeli ilk kez kalem kalem ölçüldü → **DERS 94** · ⛔ **KİLİT ÇELİŞKİSİ DEFTERİ 4 AÇIK MADDE** (İngilizce insan repliği ↔ 7/7 gövdesiz AI · açık vizör ↔ 14/14 mühürlü kask · kıvılcım/şarapnel ↔ ATEŞ 0 kare · vakumda hava sesi) — rapordan çözülemez, master kontrolüyle kapanır → **DERS 96** · ⬜ filmin ADINI taşıyan olay (S9 tutulma → halka ışığı, 1:30-1:40) üç raporun hiçbirinde anılmıyor · ⬜ sayaç A'nın sıfırı ("Sıfır.", S11) duyulan replik listesinde yok · 🧍 tek ayakta bulgu: **S12↔S13 suit sapması** (yeniden üretim) · klonsuz (D69/77 planda hiç açılmadı) · 🚫 kesme listesi UYGULANMAZ (1. sıra = S2 viral arası) · yeni ders: **93-99** (99: prompt nesri sese sızdı — "Shadow entry and exit" S4-B promptunun PHYSICS satırı, replik sanıldı) |
| ~~**The Ring Light** (plan satırı)~~ | | | | | 🆕 11.08 · 2-4 dk · 🆕 vakum (halkalı gaz devi yörüngesi, 0 g) · **Cold Burn PART_B yanaşma zincirinden türetilen bağımsız film** — gemi yanmıyor, ateş 0 kare, dönüş 2°/s pasif termal rulo · risk 5/9 TAM EŞİKTE · 14×10 s = 2:20, 0 kesme, 14/14 lockoff, 2 viral ara (S2·S9) · **7 replik hepsi gövdesiz AI; iki insan da HİÇ konuşmaz** (D82'nin yapısal panzehiri) · kask 14/14 kapalı, durum değişimi 0 · iki metinsiz sayaç: 8 gözlü darbe göstergesi + güneş saati gölgesi · doruk S8 (karotu bırakmak) · ⛔ **D69 ① kaydı planda: biniş hareketi 0 kare, film eşiğe varmadan biter** · üretim S11→S8→S9→S1 kapılarıyla başlar · ✅ 28 prompt Veo bandının içinde · ⛔ SPEC bloğu dosyanın içinde yazılı (§0.15) |
| **The Blind Berth** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 12.08 · 2-4 dk · vakum (kızıl ay yörüngesi, 0 g) · **deponun ilk GERİ GERİ yanaşma filmi ve ilk ÜÇ İNSANLI filmi** — hedef 340 m'lik ölü, ışıksız YILDIZLARARASI GEMİ (dead matte siyah + oksit kırmızısı), araç 17 m'lik GLOSS SİYAH kurye; gemi kıç önde giriyor, pilot hedefi hiçbir karede görmüyor · 12 × 10 s = 120 s, 0 kesme, 12/12 lockoff, 2 viral ara (S2·S7) · **6 replik hepsi gövdesiz AI; üç insan da HİÇ konuşmaz**, bilgi üç gövdeden geçiyor ve 1.1 s gecikme ekranda kanıtlanıyor (D82 panzehiri) · kask 12/12 kapalı, durum değişimi 0 · iki metinsiz sayaç: bant merdiveni (derinlik) + üç pirinç pim (hiza) · doruk S8 (çanağı katlamak = eve giden bağlantıyı kapatmak), bedel aynı karede duyuluyor, yatık çanak S9-S10'da kalıcı görsel kanıt · ⛔ **1 numaralı üretim riski İKİ SİYAH GÖVDE** — ayrım malzeme: hedef DEAD MATTE (ışığı yutar), kurye GLOSS (speküler + titanyum kenar + 4 tezgâh lambası); cümle 12 promptta, kanıt sahnesi S7 (üretim kapısı 2) · risk 5/9 — Kart 4 depodaki en ağır hâlinde (3 insan), beş katmanlı karşı önlem planda · ⛔ D69 ① kaydı planda: biniş/geçiş hareketi 0 kare, film kapak açılmadan biter · 🆕 **REFERANS PAKETİ 5 PANELLİ REFERANS / 17 panel** (R1 gemi 4 panel: dış-boğaz-boğaz içi-vestibül · R2 kurye 4 panel: yan-kıç-kabin-pasaj · R3/R4/R5 karakter başına 3 panel: önden-yandan-arkadan); sahnelerden ÖNCE üretilir, kurguya girmez · ⛔ panelli resim start frame olarak kullanılmaz (panel çizgisi/olası yazı videoya taşınmasın), I2V için panel tek başına kırpılır [D34/D45] · ✅ 24 promptun 24'ü Veo bandının içinde (ölçüldü: imaj 1.824-2.100 · video 2.516-2.597) · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Plumb Line** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 13.08 · 2-4 dk · vakum (metalli ay yüzeyi, 0.11 g) · **novum gerçek fizik: çekim treni** — ayın merkezinden geçen KUTUPSAL şaft; içine düşen her şey 84 dakikada bir geri geliyor ve her turda 60 cm daha az yükseliyor · 16 × 10 s = 160 s, 0 kesme, 16/16 lockoff, 2 viral ara (S2·S9) · ⭐ **0 REPLİK — deponun ikinci tamamen sessiz yatay filmi** (Unbroken City'den sonra); adamın telsizi ölü, sessizlik dekor değil ENGEL → dudak senkron riski 16/16 sıfır · kask 16/16 kapalı, durum değişimi 0 · iki metinsiz sayaç: duvara çakılan PİN DİZİSİ (derinlik, 60 cm aralık) + DÖNEN GÖLGE (zaman; 84 dk = 90°) · ⭐ ışık takvimi depoda ilk kez bir SEVİYE değil AÇI ekseni (kutupsal şaftın fizik sonucu) · doruk S12 = temas **0.0 m/s** (adam apeksinde durmuşken) ve filmin tek ses olayı: öteki nefes ilk kez gövdeden iletiliyor · CENTRAL CHOICE S8 (sondayı deliğe bırakmak) · ⛔ **ARAÇ 0 KARE** — gemi/iniş/biniş/kapak hiç yok, D69 ①'in iki sıcak noktası yapısal olarak elendi · risk **4/9** (eşiğin ALTINDA; su·canlı·diyalog kartları sıfır) · ⭐ S0 ↔ S15 loop çifti: aynı kurulum, yükselen şey insan → alet · ✅ **PROMPT_KONTROL betiği GO döndü** (32/42 prompt; video 2.277-2.596 bandın içinde, image bandı gözlem) · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Banded Deep** | ⛔ön koşu Ⓥ4.9 | ❌ | ⚠️ eski | ⛔ön koşu Ⓥ7.4 | **0/4** 🆕 14.08 · **+🔊 6.2 ✅** · ⛔ **üç koşu aynı gün, aynı 186 s kurgu (D75 ✅) ama 🔧/📖 mod V — SPEC §0.15'te hazırdı [D94 ×5]** · ⛔ kurgu kapısı 3/4 ihlal: 12 klip ≠ 16 · 186 ≠ 160 s · 3:00 yanık başlık kartı (D70/72 zincirinin 6. vakası) · S12-S15 kurguda YOK (bedel+fırlatma+final) → 📖 7.4 = tablonun en yüksek mod V skoru ama finalsiz kurgunun puanı · kilit çelişkisi defteri 5 ⬜ AÇIK (sırt [D79?] · toz şeritleri · gemi çıkışı [D69?] · plansız vizör CU · 1g) — ders yazımı D96 ile kilitli, master kontrolü bekliyor · 2-4 dk · ince atm. (🆕 KANYON, %2) · **STARLESS/UNBROKEN iskeletinin üçüncü ölçümü, eksen DİKEY** (980 m iniş) ve serinin en renkli GÜNDÜZ paleti · 16 × 10 s = 2:40, 0 kesme, 16/16 sabit çerçeve, 3 viral ara (S1·S6·S15) · ⭐ **0 REPLİK** — tamamen sessiz · novum = 940 m'de terazide dümdüz 20 cm kara katman (tek günün güncesi) · dört metinsiz sayaç: kuşak RENGİ + çizgi KALINLIĞI + güneş YAYI + ankraj DURUMU · doruk S10 (el ayası ölçümü), CENTRAL CHOICE S9 (tek cıvata; bedel S12 uzun yol + S13 boş yuva) · kask 11/11 kapalı · 5 sahne insansız (S0-S2 · S14-S15) · kara bant **DEAD MATTE kilidi** (D20/D69 ③) · ⛔ D69 ① kaydı planda: biniş-iniş 0 kare (S3/S13) · üretim S9→S10→S2→S0 kapılarıyla başlar · ✅ **PROMPT_KONTROL betiği GO döndü** (32/42; video 2.019-2.584 bandın içinde, image bandı gözlem) · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Slow Light** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 15.08 · 2-4 dk · ince atm. (🆕 YILDIZINA KİLİTLİ GEZEGEN — sabit alacakaranlık, zaman akmıyor) · **depoda novum'u ÇALIŞAN BİR CİHAZ olan ilk film**: 600 karanlık röle direği arasında altı yıldır yanıp sönen tek verici; sinyal 12 ışık yılı gidecek, şu an yolun yarısında · 16 × 10 s = 2:40, 0 kesme, 16/16 sabit lockoff, 3 viral ara (S1·S6·S15), tamamen sessiz · ⚠️ risk 4/9 (kask · ikinci figür · sayaç · toz); iki 🔴 kart (su·canlı) SIFIR — gezegen kuru ve ovayı boşaltan güç 0 kare · ⭐ **dış film analizinden tema devri**: `film_analizleri/.../NOBODY_WAS_ALIVE_WHEN_WE_LANDED` (66 rapor) — ulaşmayan mesaj ironisi, çizgi halinde alan görünmez güç; devralınan 11 ders §0.19'da satır satır işaretli · üç sayaç metinsiz (⭐ NABIZ ARALIĞI 3.0→9.0→3.0 s dramatik saat · ızgara yoğunluğu · güç hücresi) · doruk S11 = kendi güç hücresini ölülerin vericisine takmak, bedel AYNI karede (kask lambası söner) · üretim S11→S6→S9→S0 kapılarıyla başlar · ✅ prompt_kontrol.py: **0 BLOCK**, 32/42 prompt tavanın altında; tek FIX (uzunluk) gerekçesi §0.14b'de yazılı |
| **The Last Shift** | ⛔ön koşu Ⓥ5.0 | ✅ 5.0 ⚠️ | ❌ | ⛔ön koşu Ⓥ6.0 | **1/4** 🆕 16.08 · **+🧍 6.0 IDENTITY BREAK** — DÖRT mercek aynı gün, aynı 174 s kurgu (D75 ✅), ama 🔧/📖 **mod V** — SPEC §0.15'te hazırdı [**D94 ×6**] · ⛔ **deponun ilk SAHNE ≠ ÇEKİM ölçümü ve kurgu kapısının yeni delik yeri:** plan 14 sahne / **24 çekim / 27 klip / 190 s / ASL 7.9**, kurgu **17 × 10 s + 4 s kart = 174 s** → dört mercek de 14 segment saydı ve dördü de DOĞRU saydı; kapının 1. maddesi (klip = SCENE COUNT) 14=14 diye ✅ verdi → **DERS 101** · ~10 klip ekranda yok (**S5 İFŞA 1 — altmış bir çift bot, VİRAL** · S8 şaftlar · **S11'in dört çekimlik tek aksiyon ritmi**) çünkü 27 klip × 10 s = 270 s ham malzemenin 80 s'lik kırpma bütçesi hiçbir belgeye yazılmadı; kurgu kırpmak yerine klip düşürdü ve süre "tuttu" → **DERS 100** · 🔴 **2:50 yanık başlık kartı = D70/72 zincirinin 7. VAKASI** ve kartın alt satırı §5.3 KAPAK tipografisidir (düşen sahnenin bilgisi yazıya döndü) · 🔴 2:09 çıplak el–plaka kaynaşması (D11/D28, SPEC'ten bağımsız, AYAKTA) · ⛔ **BEŞ ÜRETİM KAPISININ BEŞİ DE KAYITSIZ** (BÖLÜM 4.1 tablosu boş, DURUM hâlâ "ÜRETİM BAŞLAMADI") ve raporların bulguları kapı 1-2-3-4'ün tam üstüne düştü → **D74 ×2**; tek tutan KAPI 5: **birleşik hold (20 s'lik S7) depoda ilk kez denendi ve TUTTU** · ⛔ kilit çelişkisi defteri **7 ⬜ AÇIK** [D96] · ✅ **D89 · D95 · D97 bu koşuda TUTTU** (mühür sayımı · mühürlü kask kanıtı · kanıt tabanı eşiği) · 🧩 Sayaç N/A ama planda üç sayaç var (D78 ×4) · yeni dersler: **100-103** |
| ~~**The Last Shift** (plan satırı)~~ | | | | | **0/4** 🆕 16.08 · 2-4 dk · 🆕 solunabilir ama SPORLU atmosfer, KAPALI HAVA (0.9 g / 0.8 atm; güneş diski ve sert gölge 0 kare) · ⭐ **deponun DIŞ FİLM ANALİZİNDEN HİKÂYE ve KAMERA GRAMERİ devralan ilk filmi** — `film_analizleri/.../NOBODY_WAS_ALIVE_WHEN_WE_LANDED` (66 rapor). Hollow Count aynı analizden yalnız YÖNTEMİ almıştı; bu dosya konuyu ve ölçülmüş kamera profilini alıyor, part-sahne eşlemesi §0.1b'de satır satır · ⛔ **SABİT 10 s SAHNE IZGARASI YOK:** 14 sahne · **24 çekim** · 27 klip · 190 s (3:10) · **ASL 7.9 s** (kaynak 9.0 · bant 5.76-21.7) · 10 kesme · 24/24 sabit kilitli kadraj · üç ritim modu §0.9b'de (A olay/kanıt 2 çekim · B yalnızlık tek çekim 10-20 s · C aksiyon YALNIZ S11: 4 çekim / 9 s / ASL 2.25) · ⭐ **ESİRGEME HARİTASI §0.9c** — sekiz zirvenin sekizinde kameranın NE VERMEDİĞİ yazılı (yakın plan · ters açı · tepki çekimi yok); rubriğe uyarı SPEC'te · ⭐ **birleşik hold** (iki klip = tek çekim, S7 20 s · S10 16 s · S13 18 s) depoda ilk kez · ölçek yayı 75mm ECU → 30 km EWS · **2 insan + 13 replik, hepsi gövdesiz makine** (8 kask AI + 5 çevirmen kutusu); iki figür de HİÇ konuşmaz, kadro kilidi üç kanalda (boy 1.66↔1.88 · suit rengi · bant tarafı) · ⭐ **insan sayısı bir SAYAÇTIR**: 2 → 1 → 0; ölüm 0 kare, ceset/kan/patlama 0 kare · toplu ölüm **61 çift botla** anlatılır · ⭐ **yaratık bütçesi**: 1 çekim · 3.0 s · tek uzuv · 300 m · gövde/baş/göz 0 kare (kaynak filmin A2 dersi) · ⚠️ **risk 6/9 — eşiğin ÜSTÜNDE** (canlı · kask · 2 insan · toz · katmanlı dünya · diyalog), gerekçesi §0.8'de ve **HAZIR DÜŞÜŞ planı §0.8b'de** (uzuv→gölge · S11 4→2 çekim · AI replikleri düşer; hiçbiri yeniden yazım gerektirmez) · üretim BEŞ kapıyla başlar (iki figür → parsel → uzuv → eşleştirme → birleşik hold) · 🧍 KARAKTER_QA bu filmde opsiyonel DEĞİL · ✅ prompt_kontrol.py: **0 BLOCK**, 51/51 prompt tavanın altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi §0.14b'de · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Hollow Count** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 15.08 · 2-4 dk · ince atm. (🆕 EVAPORİT TERASI / ÇÖKME HAVZASI, %4 basınç) · **novum gerçek jeoloji: yürünen zemin bir TAVANDIR** — çözünmüş tuz boşluğunun tavanı, kusursuz düz bir çizgi hâlinde, 20 saniyede bir 2 m levha vererek çöküyor (düşüş 14 m / 2.0 s, 0.7 g'de doğrulandı) · 14 × 10 s = 2:20, **16 segment · 2 kesme (yalnız S11)**, 14/14 sabit çerçeve, 5 viral ara (S0·S3·S5·S11·S13), tamamen sessiz (0 replik) · ⚠️ risk 4/9 (kask · ikinci figür · toz · katmanlı dünya); iki 🔴 kart (su·canlı) SIFIR ve **YAPAY IŞIK 0** (S13 jeti dışında) — Starless Circle'ın "model fazladan ışık icat ediyor" riski yapısal olarak elendi · ⭐ **dış film analizinin İKİNCİ saha denemesi** (`film_analizleri/.../NOBODY_WAS_ALIVE_WHEN_WE_LANDED`, 66 rapor): devralınan 13 dersin hangi sahneye indiği §0.19'da satır satır yazılı — A1 sırttan ifşa (S8, 10 s hold, yüz 0 kare) · A3 toplu ölüm **60 boş diskle** (ceset/rakam 0) · B4 **eşleştirilmiş kadraj çifti S2↔S12** (aynı SETUP/CAMERA, tek değişken: her şey yok) · B5 **hız kartı S11** (deponun ilk kez SADECE tırmandırma için kullanılan kesmesi, filmin %79-86 aralığı) · B1 tersine çevrildi: uyarı GECİKMEDİ, kapı 90 saniyede kapandı — insanlar zaten aşağıdaydı · üç sayaç metinsiz (kazık sayısı 12→0 = dramatik saat · çizgi uzunluğu 40 m→9 km→iki havza · ayak izi hattı, dönüşte yok) · doruk S9 = tek atımlık kap iki yuvadan **vince** giriyor (kapı yuvası boş kalır); bedel S12 · final **çözüm değil GENİŞLEME** (çizgi ikinci havzaya girer) · ⛔ D69 ① kaydı planda: biniş/kalkış 0 kare · dört üretim kapısı + Plan B'leri §BÖLÜM 4'te · ✅ prompt_kontrol.py: **0 BLOCK**, 32/42 prompt tavanın (4.300) altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi ve ilk-red protokolü §0.14b'de · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Borrowed Weight** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 22.08 · 3-5 dk · ince atm. (adsız gri ova, %1.2 bar / 0.92 g, sürekli örtü — güneş diski 0 kare, gölgesizlik fizik) · 🆕 **depoda ilk novum-İNSANDA filmi**: yerden kesilen parça tüyleşir, ağırlığı taşıyana geçer ve GERİ VERİLMEZ — kural 6 sahnede 5 katı nesneyle kanıtlanır [ONERME §5]; tema fedakârlığın fiziği ("kalan her şey, ağırlığını birinin taşıdığı şeydir") · 25 × 10 s = 4:09 · 0 kesme · 25/25 lockoff · 4 viral ara (S5·S13·S19·S23) + S0 kapak anı · **TWIST + tohum** [FINAL 3-5 dk kuralı]: S1/S3 tohumları → S24'te ova BOŞ (hafifleyen her şey gece rüzgârının malı; kasa KENETLİ olduğu için kalır — içerik 0 kare, bilinçli muğlak) · sayaçlar metinsiz: İZ DERİNLİĞİ 2→23 cm monotonik · adım 9→5 (eş kadraj S6↔S18, tek değişken yük) · rakamsız kantar (ibre 2.→9.→dip, S16'da geride bırakılır) · cyan nabız 2 s (ölü ikiz kasa 0 nabız) · **4 replik, hepsi MACHINE** (S2·S10·S21·S22; sahibin şartı: AI sesi insana yapışmasın — dördü de AĞIZ-DIŞI kadraj + "he never speaks" gövde kilidi + düz sentetik register [D82]; HUMAN 0) · 23/23 kask kapalı, ara durum 0, giyme 0 · ⚠️ risk 5/9 TAM EŞİKTE (kask · ikinci figür · sayaç · toz · MACHINE diyalog); su · canlı · katman SIFIR · **çekirdek-kayma çakışması** çözümlü [D59 · LOSS hovering emsali]: statik yasağı iki özneye bölündü ("only the lightened pieces creep leeward, on the ground"), S1 üretim kapısı — geçmeden S13 üretilmez · lander YÖNELİM KİLİDİ (burun gömülü, kuyruk göğe, kapak yüzü sola) 25 sahnede sabit [uzamsal §5.1] · ✅ prompt_kontrol: PART_A 26 + PART_B 24 + KAPAK 2 prompt — **0 BLOCK**; FIX yalnız gerekçeli uzunluk (tavan 4300 aşımı 0), kayıt PART_A ⑨ / PART_B ⑧ · ⛔ SPEC ayrı DOSYA (THE_BORROWED_WEIGHT_QA_SPEC.md) — **MOD D koşulacak, mod V ön koşudur [D94/D117]** · üretim kapıları: S0 (paradoks+gri ayrışma) → S1 (kayma) → S5 (ölçek) → S20 (doruk) |
| **The Short Way Down** | ❌ | ❌ | ❌ | **0/3** 🆕 22.08 · dikey shorts · Dünya atm. (günümüz, −4 °C, bitmemiş 14 katlı bloğun çekirdek merdiveni) · 🆕 **dikey hattın ilk ZOMBİ konsepti** — §4.2 tür kartı 12.08'de rafa kalkmıştı, dikey hatta geri açıldı (THE DULL EDGE'in savaş kartını kullanmaya devam etmesiyle aynı emsal) · ⭐ **depodaki ilk gerçek KOVALAMACA**: 48 saniyenin 48 saniyesi kaçış, boş vuruş 0 · ⭐ **klasörün ilk DEVAM ZİNCİRLİ dosyası**: 6 sahne tek kesintisiz iniş; 5/5 kesme gizli geçişle (perde) tasarlandı, her sahnenin ayrıca **I2V DEVAM sürümü** var — `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU` §5'in dikeydeki ilk uygulaması · 6 × 8 s = 48 s, 0 kesme, 5/6 tam lockoff, 0 replik, ekran metni 0,0 sn · novum tipi FİZİKSEL YASA, taşıyıcı KATI (korkuluk × üstünden aşma jesti → 12 m düşen gövde ayağa kalkar) — D73'ün türetilmiş-fenomen tuzağı yapısal olarak elendi · sayaç metinsiz: **MESAFE** 9→6→11→7→2,5→14 m · ⛔ **risk 6/12 EŞİĞİN ÜSTÜNDE ve dosyada kabul edilmiş maliyet olarak yazılı**; gerçek risk kartlarda yok: **düşüp ayağa kalkan gövde** (modelin dört bozulma modu: ağır çekim · yerde bırakma · beton patlatma · düşüşü hiç göstermeme) · azaltmalar sayısal: temas 0 kare / en yakın 2,5 m · yüz sayısı 1, takipçi yüzü 0 kare · takipçi YÜRÜME bütçesi TOPLAM 4,5 sn (D18'in yüzeyi 43,5 sn kısıldı) · yara/kan/silah/patlama/su 0 kare · fosforlu giysi TAM 1 (klon karşı önlemi) · doruk S5 = kadın onların yolunu kullanır, bedel aynı karede (5,5 m / sol bacak tutmaz) ve döngüye devredilir · final DÖNGÜ + TWIST, tohum S0 0:05-0:07 (ilk gövdenin iniş biçimi) · üretim S0'dan başlar · ✅ prompt_kontrol.py: **0 BLOCK / 0 FIX — GO** · ⛔ SPEC bloğu dosyanın içinde |
| **The Tall Shore** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 14.08 · 2-4 dk · ince atm. (🆕 KURU OKYANUS HAVZASI, 0.09 atm) · **ÖLÇEK filmi: 9.000 m'lik kıyı basamağından 1.100 km'lik tuz havzasına iniş** · 18 × 10 s = 3:00, 0 kesme, 18/18 sabit lockoff, 4 viral ara (S3·S7·S10·S15) · ⚠️ **risk 6/9 — depodaki en yüksek sayım ve EŞİĞİN ÜSTÜNDE**, gerekçesi ve azaltma planı planda yazılı: iki 🔴 kart (su·canlı) SIFIR, gerçek ağırlık Kart 7'de · ⛔ **depo standardından bilinçli sapma: kadın ÜÇ KEZ konuşuyor** (Ring Light/Blind Return 0 insan repliği) — karşı önlem TURN LOCK (sahne başına tek konuşmacı, 9 replikli sahnenin 9'unda) + AI sahnelerinde ağız kapalı + kadın sahnelerinde 75mm · ⭐ **HAZIR DÜŞÜŞ planda yazılı**: S2 üretim kapısı batarsa kadının üç repliği düşer, üç AI repliğiyle değişir, risk 6/9 → 5/9 (yeniden yazım gerekmez) · dört metinsiz sayaç: zaman SESLİ + mesafe YEDİ SEKİ + perspektif SIRT SAYISI (9→7→5→3→2→1, monotonik) + geri sayım GÖLGE ETEĞİ (25 m/dk) · ölçek mekanizması **HAVA PERSPEKTİFİ** sayısal kilidi (10 km'de kontrast dörtte bir düşer) — Cold Burn'ün dok kapısının panzehiri · doruk S13 (26 kg'lık kanıtı tuza gömmek; bedel aynı sahnede, S17'de kadrajda duruyor) · kask 18/18 kapalı, durum değişimi 0 · Canopy World'ün battığı madde (katmanlı dünya ışık takvimi) bu filmin omurgası: LAYER LIGHT SCHEDULE irtifaya göre sıralı ve monotonik · ⚠️ **PROMPT_KONTROL betiği FIX döndü** (36/46 prompt, ⛔ 0 BLOCK; tek bulgu UZUNLUK: 14/18 video promptu bandın 30-490 karakter üstünde, tavanın çok altında) — üretimden önce kapatılacak, yol filmin BÖLÜM 3'ünde yazılı · ⛔ SPEC bloğu dosyanın içinde (§0.16) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Uphill Dark** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 17.08 · 3-5 dk · 🆕 **VAKUM + İTKİ YERÇEKİMİ (0.220 g)** — depoda ilk alt-ortam: vakumun bütün kuralları geçerli ama "her şey süzülür" kuralı GEÇERSİZ, her şey DÜŞER · ⭐ **novum: uzayda düşmek var** — 210 m'lik yıldızlararası gemi kalkış yanmasını durduramaz, yanındaki her serbest cisim kıça doğru 2.16 m/s² ile düşer; novum'un üç kanıtı da KATI NESNE (sarkan kordon · düşen kovan · düşen yük), türetilmiş optik fenomen [D73] ya da yokluk [D76] DEĞİL · 25 sahne (Hook 9 s + 24 × 10 s = 4:09), 0 kesme, 25/25 sabit lockoff, 4 viral ara (S4·S10·S19·S23), **0 replik** · ⚠️ risk 4/9 (kask · ikinci figür · sayaç · parçacık); iki 🔴 kart (su·canlı) SIFIR · ⭐ **D23 (sıfır-g rijitliği) YAPISAL OLARAK ELENDİ** — film boyunca hiçbir kare sıfır yerçekiminde değil; kural değil KARAR ile kapatıldı [AGENTS §8] · ⭐ **ikisi de 25/25 sahnede kemerli ve oturuyor** → biniş/iniş/yürüme 0 kare [D69 ①] · dört metinsiz sayaç: PENCERE MERDİVENİ (gemi gövdesinin hangi bölümü pencerede) · SARKAN KORDON (itki var mı) · KARTUŞ YUVALARI 6→0 · YÜK KIZAĞI 40 dolu→40 boş · aritmetik filmin kendisi: 3 tırmanış × 40 m = 120 m ama radyatör kanadı tırmanış 2'yi 12 s erken kestirir (22 m) → 16 m AÇIK, 0 kartuş · CENTRAL CHOICE S19 (%75.7) = 900 kg yükü bırakmak, bedel AYNI KAREDE (kırk karot düşerken gövde pencerede kaymaya başlar) · doruk S21 temas 0.20 m/s (3:37.9 = **%87.5**, bant içi) · turuncu TAM ÜÇ YERDE (iki skafandr · yük kayışı · atma kolu) ve S19'dan sonra kadrajdaki tek turuncu iki insandır · ⭐ **REFERANS PAKETİ 5 SAYFA × 4 PANEL** (varlık başına tek sayfa; 17.08.2026'da 13 tek görselden indirildi, iki durum çifti aynı sayfada) · ✅ prompt_kontrol.py: **0 BLOCK**, 50/50 prompt tavanın (4.300) altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi + İLK RED PROTOKOLÜ PART_A §Üretim Notları'nda · ⛔ SPEC bloğu planın içinde — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Blue Drift** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 17.08 · 3-5 dk · **YAZIM TAMAM:** PLAN + PART_A + PART_B + KAPAK + **REFERANS_PAKETI (5 sayfa × 4 panel, Uphill Dark formatı; üç durum çifti aynı sayfada)** — 50 film promptu + 2 kapak; prompt_kontrol 0 BLOCK (A/B FIX yalnız uzunluk, gerekçeli · KAPAK ✅ GO) · üretim KAPI 0 (referans sayfaları + §4 devamlılık kapısı) → S21 → S15 → S4 → S0 sırasıyla başlar · 🆕 ortam: mavi devin KIRAĞI UYDUSU (azot buzu, 0.4g, gece yüzü YALNIZ mavi planetshine ile aydınlık) — **palet üçlemesinin kapanışı: beyaz (Cold Burn) → siyah (Black Cradle) → MAVİ** · ⭐ **novum: ölü aracın YAKALANIŞI** — perde kenarı iticileri öldürür, araç balistik; depodaki beş yanaşma filminde manevrayı hep küçük araç yapıyordu, ilk kez YAKALAYAN ANA GEMİDİR ("katedral pervaneye gelir") ve doruk EDİLGENDİR · tehdit depoda ilk kez GÖKTEN iner: plazma perdesi (aurora, taban 90°→40°, yalnız mavi-menekşe — YEŞİL NEGATİFTE) · 25 sahne × 10 s = 4:09 (standart, sapma yok), 0 kesme, 25/25 lockoff, 4 viral ara (S4·S7·S15·S21) · 16 replik / 13 sahne — 10 MACHINE (KERTE ana gemidedir, S9-S11 bağlantı kopuk = atışma yapısal imkânsız [D82]) · CENTRAL CHOICE S14 = kabin havasını itki olarak harcamak (6 düz puf ile despin; bedel S16 mekanik ibrede %40) · doruk S21 yakalayış %84-88 (sahibi KERTE: "Tuttum.") · ⚠️ risk 5/9 TAM EŞİKTE; iki 🔴 kart (su·canlı) SIFIR, ateş/patlama 0 kare · kartlarda olmayan iki risk yazılı: MAVİ-ÜSTÜ-MAVİ (beş mavi ton/doku skalası + amber istisna ailesi + HAZIR DÜŞÜŞ) ve AURORA KLİŞESİ · üretim S21→S15→S4→S0 kapılarıyla başlar · ⛔ SPEC bloğu planın içinde — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **Loss of Lift** | ❌ | 🚨 ~~8/6~~ | ❌ | ⛔ön koşu Ⓥ7.0 | **0/4** 🆕 20.08 · ⚡ **21.08 ÜRETİLDİ + 3 QA KOŞUSU — hepsi ÖN KOŞU, matris 0/4 KALDI** [D94/117]: SPEC planın 738. satırında hazırdı, üç koşu da mod V · üç rapor AYNI oturumdan, AYNI 26 satırlık haritayı paylaşıyor → tek ölçümün üç kılıfı [D110] · 🧩 iki koşu 🚨 GEÇERSİZ (aynı defter, 8/10 ve 6/10, ikisi de kendi hücrelerinin ortalaması değil → **D119**) · 📖 Ⓥ7.0 ŞARTLI (diyalog **9/10** ve özgünlük 8/10 — tek replik ve novum tuttu; yapı 5/10 sıra şüphesine bağlı) · ⛔ kurgu kapısı: sayı ✅ (26−1 kart=25) süre ✅ (255−5=250≈249) **SIRA ⛔ insan şeridi slot 19/20 ters → doruk yanlış yuvada olabilir, master 3:09-3:29 izlenecek** → **D118** · 🔴 4:10-4:15 başlık kartı = ekran metni kilidi 0.0 s ihlali, D70/72 zincirinin 8. vakası · kilit çelişkisi defterinde **6 madde ⬜ AÇIK** (~1,5 dk seyretme) → içerik dersi YAZILMADI · kayıt: `01_FILM_RAPORLARI/LOSS_OF_LIFT.md` · 🆕 `LOSS_OF_LIFT_QA_SPEC.md` yazıldı, sıradaki koşu MOD D · 3-5 dk · 🆕 ortam: **VENÜS BULUT KATMANI — sürekli bulut / nötr yüzerlik** (0.53 bar CO2, 0.904 g, bağıl rüzgâr 0-2 m/s, güneş diski YOK, zemin YOK) · yeni ortam kartı önerisi (§3.6) planın içinde · ⭐ **LOW POWER'ın kardeşi olarak sipariş edildi** — aynı motor (tek kişi · sessiz-yavaş-durdurulamaz tehdit · tek sayı · iki renk · devretme teması · tek yanlış-umut beati), tamamen yeni malzeme: güç yerine KALDIRMA, toz yerine ASİT, karanlık yerine AŞAĞI · ⭐ **konu seçimi LOW POWER'ın ölçülmüş iki dip skorunu yapısal olarak siliyor**: toz 0 kare → D39 tetiklenemez · gölgesizlik fizik → D41'in yanlış teşhis zemini yok · asit kirletmez AĞARTIR, yıpranma TAM 3 sabit bölge → D42 yüzeyi daralır · novum katı gövde (yüzen istasyon) — türetilmiş optik [D73] ya da yokluk [D76] DEĞİL · 25 sahne (Hook 9 s + 24 × 10 s = 4:09) standart, 0 kesme, 25/25 sabit lockoff, 4 viral ara (S5 zarfın sırtı · S13 varmayan yağmur · S19 tek mor · S23 iki ışık) · **1 replik** (S22, ağız kadraj dışı — bu istasyonda konuşmak da nefestir; D35 yüzeyi 0) · dört metinsiz sayaç: PİN YAYI (24 çentik × 250 m, ibre 7→13) · BUĞU (S3 var → S18 yok) · KAÇAK ISLIĞI · SONDA FENERİ (4 s'de 1 nabız) · aritmetik filmin kendisi: kaçak 322 kg/s → batış 30 m/s; kalan TEK tüp 600 kg = zarfa 1,9 saat / **70 metre**, ya da 12 m'lik sondayı doldurup kolonu 61 km'ye — asidin ÜSTÜNE — çıkarmaya TAM yeter · CENTRAL CHOICE S20 (%79-83) = kolu sonda borusuna atmak, bedel AYNI KAREDE (takviye susar, ibre yeniden düşer) · S0↔S24 açılış-kapanış çifti (tek gövde iniyor ↔ iki gövde, zıt yön) · ⚠️ risk 5/9 TAM EŞİKTE (kask · ikinci figür · sayaç · katmanlı dünya · tek replik); **su · canlı · parçacık SIFIR** (toz/ateş/patlama/egzoz 0 kare) — tek replik düşerse 4/9 · kartlarda olmayan iki risk yazılı: OKRA-ÜSTÜ-OKRA (beş dokulu ton skalası + HAZIR DÜŞÜŞ) ve **"HOVERING" ÇAKIŞMASI** (negatif çekirdek yasaklıyor, filmin gövdesi gerçekten yüzüyor → yasak parçacıkta kalır, gövdeye POZİTİF cümle [D59]) · LAYER LIGHT SCHEDULE (KART 6b) irtifa + güneş fazıyla sahne sahne yazılı ve monotoniklik gerekçesi kayıtlı · üretim S0 (hovering/ölçek kapısı) → S5 → S20 → S8 sırasıyla başlar · ⛔ YAZIM TAMAM (20.08): PLAN + PART_A + PART_B — 25 sahne / 50 prompt, çapa blokları iki dosyada da üreteçten bayt bayt aynı (parafraz avcısı 0 şüphe ×2), insanlı 21 video I2V + kompakt karakter kilidi, tek replik S22 (telsiz, ağız kadraj dışı → D35 yüzeyi 0), 7 eş kadraj çifti, S20 bedel kanalı D90 adaptasyonu (boru terlemesi + ıslık takası) kayıtlı; prompt_kontrol ×2: 0 BLOCK / FIX yalnız uzunluk (tavan aşımı 0; maks video A 3.846 / B 3.799); KAPAK ✅ GO (20.08 · A: yüz %60 + S13 varmayan yağmur, bakış merakın kendisine · B: S24 aynası, insansız; iki promptta metin 0, D79/D95 negatifte, sağ alt rozet köşesi boş; prompt_kontrol 0 BLOCK / 0 FIX) · MUZIK ✅ (20.08 · tek tempo 48 BPM = tam 2 ölçü/sahne; skor filmin kaldırma gazı — katman katman sökülür, yalnız CUE C'de eklenir; alçalan motif S23'te TERS dönüp tamamlanır; sessizlik penceresi 3:19-3:49 = doruk+bedel+tek replik müziksiz, S20 ıslık takası çıplak; iç yatak D83 tek parça; fener 4 s ↔ ölçü 5 s kasıtlı off-grid [§13]) · **YAZIM PAKETİ TAM: PLAN + PART_A + PART_B + KAPAK + MUZIK** · üretim S0→S5→S20→S8 kapılarıyla başlayabilir |
| **diğer 23 film** | ❌ | ❌ | ❌ | ❌ | **0/4** |

```
ÜÇ MERCEKLE DE ÖLÇÜLEN (3/3)    5 / 59     Kaleida Crash · Stone Sky
                                           · Unbroken City · Cold Burn
                                           · Third Dune
                                           (12.08.2026: 🎨 KAPAK merceği
                                           kaldırıldı, payda 4→3; "tam ölçüm"
                                           tanımı artık üç mercek)
İKİ MERCEKLE ÖLÇÜLEN            9          Inversion · Tidal Hunt · Ring Walker
                                           Last Archive · Canopy World · Dawn Front
                                           · Wrong Shadow
                                           · Starless Circle (📖 satırı geçersiz;
                                           dört rapor var, iki geçerli mercek)
                                           · Blind Return (🔧 girdisiz GEÇERSİZ;
                                           dört rapor var, iki geçerli mercek +🧍)
TEK MERCEKLE ÖLÇÜLEN           13
HİÇ ÖLÇÜLMEYEN                 32          (Ring Light'ın iki ön koşusu ölçüm
                                           sayılmaz — DERS 94; Banded Deep'in
                                           🔧/📖 koşuları da ÖN KOŞU, 🔊 ise
                                           /3 paydası dışı — üçü de matris
                                           ölçümü sayılmaz · 14.08)

🧍 KARAKTER_QA (4. mercek)      8 / 63     opsiyonel derin mercek — matrisin
                                           /3 paydasına girmez, film satırına
                                           "+🧍" olarak işlenir
                                           → 06_KARAKTER_KALITE_TABLOSU.md
🔊 SES_QA (5. mercek)           1 / 57     🆕 09.08 · opsiyonel derin mercek —
                                           paydaya GİRMEZ, film satırına "+🔊"
                                           olarak işlenir · yalnız TAM KURGU
                                           → 07_SES_KALITE_TABLOSU.md
                                           (Cold Burn koşusuyla AÇILDI)
```

> 🔊 **Altıncı mercek neden açıldı (09.08.2026).** Aşağıdaki **Bulgu 1**
> yıllardır aynı şeyi söylüyordu: rubrik 11 kategori ölçüyor, özet tablo 7
> sütun gösteriyor ve dışarıda kalan dördünden biri **Diyalog ve Ses.**
> Projenin bilinen iki 3/10'u (Low Power · Dead Approach) tam olarak oradan
> geldi ve hiçbir tabloda görünmedi. Sütun eklemek yetmezdi: ses hatalarının
> çoğu tek klipte duyulmaz — konuşmacı atfı, ses kimliği kayması ve ortam
> sesinin her kesmede ölmesi ancak kurgunun tamamı dinlenerek çıkar.
> Bu yüzden sütun değil MERCEK açıldı. Matrisin ana paydası değişmedi
> (o gün /4'tü; 12.08.2026'da KAPAK merceğinin kaldırılmasıyla /3 oldu).
> ⚠️ İlk koşan ajan için tek uyarı: rapor bir repliğe "yapay duruyor" derse,
> önce o repliğin MACHINE register'da olup olmadığına bak (kart E3 adım 2).
> Bu seride yapay ses çoğu zaman tasarımın kendisidir.

### Bu matristen çıkan üç şey

**1. Üç mercekle ölçülen yalnız 5 film var** ve beşinin de skorları 4-8
bandında dağınık. "Bu film QA'dan geçti" cümlesi hâlâ hiçbir film için
rahat söylenemiyor.

**2. Tek mercekle ölçülen 12 film, ölçülmemiş sayılmaya yakın.** VIDEO_QA tek
klibe bakıyor; sahneler arası kayma ve dramatik ölüm onun kör alanı. Tidal
Hunt teknikte 3/10 aldı, mantıkta 4.0 aldı — ikisi farklı şey söylüyor ve
tek başına hiçbiri filmi tarif etmiyor.

**3. Kapak denetimi artık rubriksiz.** KAPAK_QA rubriği bir kez bile
çalıştırılmadan 12.08.2026'da kaldırıldı; kapak kontrolü 120 px posta pulu
testiyle ELLE yapılır (kaynak: `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`).

---

> 📖 Hikaye skorları: [`03_HIKAYE_KALITE_TABLOSU.md`](03_HIKAYE_KALITE_TABLOSU.md)
> 🧩 Mantık skorları: [`04_MANTIK_KALITE_TABLOSU.md`](04_MANTIK_KALITE_TABLOSU.md)
> 📱 Shorts skorları: [`05_SHORTS_KALITE_TABLOSU.md`](05_SHORTS_KALITE_TABLOSU.md) 🆕 06.08
> Üç rubrik **üç farklı şeyi** ölçer — bir filmin üç skoru birbirini yordamaz.
> Tidal Hunt teknikte 3/10 ama mantıkta 4.0; Kaleida teknikte 4.5, hikayede
> 5.1, mantıkta 4.0.
>
> 🚨 **Kalite artık ders eklemekten değil, ölçüm merceği eklemekten geliyor.**
> Biriken dersler 11 filmde ortalamayı 5’in üstüne çıkarmadı. İki yeni mercek 4 filmde
> **6 yeni ders** üretti ve üçü hiçbir prompt cümlesiyle çözülmüyor —
> kurguda, planda veya sahne haritasında çözülüyor.

---

# 🚀 UZAY · 2-4 dk — 37 film (kaynak: `sayac.sh`)

> ⚠️ Bu tabloda **35 satır** var: `THE_HERD` ve `THE_UNBROKEN_CITY`'nin
> satırı hiç açılmamış (ikisi de aşağıdaki tamlık matrisinde duruyor).
> Satır durumu: 19 ölçüldü · 16 ❌ (13.08.2026 · THE BLIND BERTH silindi).

| | Film | Kapsam | Skor | Ders | Dosya |
|:--:|---|:---:|:---:|:---:|---|
| ✅ | THE_CANOPY_WORLD | Montaj **×2 +🧩** | 4/10 → **3/10** · **🧩5.0/10** | 8 | [→](01_FILM_RAPORLARI/THE_CANOPY_WORLD.md) ⭐ **İKİ KEZ ÖLÇÜLEN TEK FİLM** — sapma ±1.3 · 7 dersin kayıp timestamp'i geri geldi |
| ✅ | THE_DAWN_FRONT | Full **+🧩** | **4/10** · **🧩3.0/10** | **2** | [→](01_FILM_RAPORLARI/THE_DAWN_FRONT.md) 🔧🧩 ham rapor ✅ · ⭐ **ilk dolu-SPEC'li dış model koşusu** (tek dosya paketi) · 🚨 **DERS 67+68'in kaynağı** — duvar şelale, bacada alev, sahne içi kesme mimarisi tutmadı · 📖 ⛔ kapı (INPUT MISSING — doğru davranış) |
| ✅ | THE_DEAD_APPROACH | Montaj | **3/10** | 5 | [→](01_FILM_RAPORLARI/THE_DEAD_APPROACH.md) |
| ✅ | THE_DEEP_ROOT | Montaj | 5/10 | 3 | [→](01_FILM_RAPORLARI/THE_DEEP_ROOT.md) |
| ✅ | THE_HOLLOW_STATION | Full | 4/10 | 3 | [→](01_FILM_RAPORLARI/THE_HOLLOW_STATION.md) |
| ✅ | THE_KALEIDA_CRASH | Full **+📖+🧩** | 4.5/10 · **📖5.1/10 ⚠️** · **🧩4.0/10** | 3 **+2** | [→](01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md) 📖🧩 ham rapor ✅ · ⭐ **üç merceğin de uygulandığı ilk film** · 🚨 planda SAHNE 3 yok · **DERS 47+48'in kaynağı** |
| ✅ | THE_LAST_CROSSING | Montaj | 4/10 | 1 | [→](01_FILM_RAPORLARI/THE_LAST_CROSSING.md) 🚨 tabloda yok |
| ✅ | THE_ORPHAN_BLOOM | Full | 5/10 | 4 | [→](01_FILM_RAPORLARI/THE_ORPHAN_BLOOM.md) |
| ✅ | THE_RING_WALKER | Full **+📖** | 5/10 · **📖5/10 ⚠️** | 3 | [→](01_FILM_RAPORLARI/THE_RING_WALKER.md) 📖 ham rapor ✅ · **🚨 tutulma sahneleri montajda yok** |
| ✅ | THE_SLOW_TIDE | Montaj | 5/10 | 4 | [→](01_FILM_RAPORLARI/THE_SLOW_TIDE.md) |
| ✅ | THE_STARLESS_CIRCLE | Klip **+🧩+📖+🧍** | **5.7/10 Ⓥ⚠️** · **🧩5.5** · **📖~~4.1~~ 🚨** · **🧍6.0 🚨** | **5** | [→](01_FILM_RAPORLARI/THE_STARLESS_CIRCLE.md) 🔧📖🧩🧍 ham rapor ✅ ×4 · 🚨 **DERS 75-79'un kaynağı** · iki mercek 12 s klibe, iki mercek 2:54 kurguya koşuldu · 🔴 klon 2:10 (biniş — D69 ×3) · 🔴 yanık kart 2:50 = kapak promptu başlığı (D72 ×2) · 🚨 novum "black sphere" olarak çıktı |
| ✅ | THE_STONE_SKY | Comp **+🧩+📖+🧍** | **4/10 Ⓥ** · **🧩4.0** · **📖5/10 Ⓥ⚠️** · **🧍6.0 🚨** | **1** | [→](01_FILM_RAPORLARI/THE_STONE_SKY.md) 🔧🧩📖🧍 ham rapor ✅ ×4 · ⭐ **DÖRT raporlu ilk film + KARAKTER_QA'nın ilk koşusu** · 🚨 **DERS 69'un kaynağı** — klon, planın işaretlediği S10-B iniş noktasında · planlı 0:05 kesmesi BLOCKER sanıldı (Ders 61 örüntüsü, belge kontrolüyle düştü) |
| ✅ | THE_TIDAL_HUNT | Montaj **+🧩** | **3/10** · **🧩4.0/10** | 3 **+1** | [→](01_FILM_RAPORLARI/THE_TIDAL_HUNT.md) 🧩 ham rapor ✅ · 🚨 **DERS 50'nin kaynağı — sayaç ekrana hiç çıkmamış** |
| ✅ | THE_BLIND_RETURN | **🧩+📖+🧍** (🔧 girdisiz) | **🧩4.0** · **📖4.0 Ⓥ⚠️** · **🧍4.0** | **2** | [→](01_FILM_RAPORLARI/THE_BLIND_RETURN.md) 🔧🧩📖🧍 ham rapor ✅ ×4 · 🚨 **DERS 80+81'in kaynağı** — 🔧 koşusuna video yüklenmedi (REGENERATE verdikti geçersiz) · kurgu: S15 yok + S16↔S17 ters, üç mercek "yapısal çöküş" okudu · dört MAJOR'ın dördü belge kontrolünde kimlik değiştirdi |
| ❌ | THE_ABANDONED_ARMADA | — | — | — | — |
| ❌ | THE_BREATHING_STORM | — | — | — | — |
| ❌ | THE_BURNING_WORLD | — | — | — | — |
| 🧩 | THE_DEEP_PRESSURE | **mantık** | **🧩3.0/10** | **4** | [→](01_FILM_RAPORLARI/THE_DEEP_PRESSURE.md) 🧩 ham rapor ✅ · 🚨 **plan dosyası YOK — 13 sahnenin 2'si yazılı** · **DERS 55-58'in kaynağı** · Kostüm-Prop **1/10** = serinin en düşük kategorisi |
| ❌ | THE_ETERNAL_DUSK | — | — | — | — |
| ❌ | THE_ETERNAL_ENGINE | — | — | — | — |
| ❌ | THE_FIRST_BREATH | — | — | — | — |
| ❌ | THE_FORGOTTEN_ARCHITECTS | — | — | — | — |
| ❌ | THE_GLASS_ABYSS | — | — | — | — |
| ✅ | THE_HOLDING_FIELD | Mantık | **🧩4.0/10** | **+1** | [→](01_FILM_RAPORLARI/THE_HOLDING_FIELD.md) 🧩 ham rapor ✅ · 🚨 **DERS 59'un kaynağı — öncül ters render edildi** |
| 📖🧩 | THE_INVERSION | **senaryo + mantık** | — · **📖5.0/10 ⚠️** · **🧩3.0/10** | **3** | [→](01_FILM_RAPORLARI/THE_INVERSION.md) 📖🧩 ham rapor ✅ · 🚨 **DERS 45+46+49'un kaynağı** · **serinin en düşük mantık skoru** · teknik QA hiç yapılmadı |
| ✅ | THE_LAST_ARCHIVE | Comp **+🧩** | **4/10 ⚠️** · **🧩5.0/10** | 0 | [→](01_FILM_RAPORLARI/THE_LAST_ARCHIVE.md) 🔧🧩 ham rapor ✅ · ⭐ **ilk BLOCKER'sız mantık raporu** · 🔁 DERS 45'i genişletti · 🚨 planda 17 blok, kurguda 14 |
| ❌ | THE_LAST_BLOOM | — | — | — | — |
| ❌ | THE_MAGNETIC_TIDE | — | — | — | — |
| ❌ | THE_PULSE | — | — | — | — |
| ⚠️ | THE_RING_LIGHT | Kurgu 144 s **+📖+🧍** ⛔ üçü de ÖN KOŞU (⭐ filme özel rubrik DURDU) | **7.0/10 Ⓥ⚠️** · **📖6.0 Ⓥ⚠️** · **🧍8.5 ⚠️** | **7** | [→](01_FILM_RAPORLARI/THE_RING_LIGHT.md) 🔧📖🧍⭐ ham rapor ✅ ×4 · 🚨 **DERS 93-99'un kaynağı** · ⭐ kurgu kapısını TAM geçen ilk film (14/14 sahne, doruk ekranda) · 🔴 2:20 jenerik kartı filmin KENDİ rubriğini susturdu · ⛔ kilit çelişkisi defteri 4 açık madde |
| ❌ | THE_REMEMBERING_DUST | — | — | — | — |
| ❌ | THE_RESONANCE_FIELD | — | — | — | — |
| ❌ | THE_SILENT_EVENT_HORIZON | — | — | — | — |
| ❌ | THE_SPAGHETTI_TIDAL | — | — | — | — |
| ❌ | WHITE_SILENCE | — | — | — | — |

---

# 🎬 3-5 dk — 6 film (2 ✅ / 4 ❌)

| | Film | Kapsam | Skor | Ders | Dosya |
|:--:|---|:---:|:---:|:---:|---|
| ✅ | LOW_POWER | 🚨 tek sahne (S14) | 4/10 | 4 | [→](01_FILM_RAPORLARI/LOW_POWER.md) künye hatalı |
| ⚠️🚨 | THE_BLACK_CRADLE | ⛔ön koşu Ⓥ6.0 | 🚨 geçersiz | 🚨 geçersiz | ⭐ **17.08.2026 · BEŞ MERCEK, DÖRDÜ GEÇERSİZ — bu koşu filmi değil ÖLÇME ALETİNİ ölçtü.** Beşi de aynı 232 s kurguya, aynı oturumda, mod V koşuldu (**+🧍 🚨 geçersiz · +🔊 🚨 geçersiz**). 🔧 21 kesme saydı, diğer dört mercek **4 sahne** — 85 s'lik tek sahne 10 s klip tavanlı bu hatta üretilemez → **DERS 107** (parti geçersiz). Tek gözlem dört tabloya faturalandı (1:09 dudak senkronu ×4 · 1:45 vakumda ses ×3) → **DERS 108**; düzeltilmiş okumalar 🧩 ~8.4 · 🔊 ~8.8. Kurgu kapısı koşulmamış: 232 s / ~22 kesme ↔ kapı 26 klip / 259 s ±2 s, ve PART_A kapı defteri hâlâ 'S0-S14 üretildi' diyor → **DERS 109** + D74 ×3. Dört rapor birbirinin defterini devraldı (severity tally'leri birebir aynı) → **DERS 110**. ⛔ SPEC planda hazırdı, yine mod V (**D94 ×6**) · 🚫 kesme listesi UYGULANMAZ (1. sıra = KESİLEMEZ viral ara S4, D94 örüntüsü 4. vaka) · ⬜ **KİLİT ÇELİŞKİSİ DEFTERİ 11 AÇIK** [D96, deponun en kalabalık defteri]: ağız okunan kare (kilit: 0 kare) · MİRA repliğinin ekrandaki kadına atfı (D82) · altın vizör (kilit: optik berrak) · suit rengi (kilit: mat kömür siyahı) · rol/cinsiyet takası · yüzeyde şafak ışığı + dolgu (kilit: gece + TAM 5 yapay kaynak) · kapalı hangar finali (kilit: açık kızak yuvası + S24 yörünge) · vakumda ses (prompt: hard vacuum silence) · kostüm değişimi · 2/14 replik · Sayaç NONE (D78 ×5) · ✅ D75 tuttu (beş mercek aynı dosya), D82 register haritası ALET olarak çalıştı, D65 tuttu · kayıt: `01_FILM_RAPORLARI/THE_BLACK_CRADLE.md` · 🆕 16.08.2026 · PLAN + PART_A + PART_B yazıldı (⚠️ 17.08: 26 sahne × 10 s = 4:19, +S19b ara sahnesi · 52 prompt · prompt_kontrol 0 BLOCK, FIX yalnız uzunluk) · Cold Burn mantığının siyah tersi: kara gezegen + kara gemiler + kör KIÇ ÖNDE yanaşma · doruk S21 temas %85-88 · 0/4 mercek · KAPAK + referans paketi sırada · üretim S15 (siyah-üstü-siyah) kapısıyla başlar |
| ⚠️ | LOW_POWER — **senaryo QA** | 🚨 var olmayan 7 sahnelik kurgu | ~~7.0/10~~ | 0 | [→](02_HAM_RAPORLAR/LOW_POWER_SENARYO_HAM.md) GEÇERSİZ SPEC |
| ❌ | THE_RISING_SNOW | — | — | — | üretim aşamasında |
| ❌ | THE_UPHILL_DARK | — | — | — | 🆕 17.08.2026 · PLAN + PART_A + PART_B + KAPAK + **REFERANS_PAKETI (5 sayfa × 4 panel)** · 25 sahne × 10 s = 4:09, 0 kesme, 0 replik, 25/25 lockoff · 🆕 ortam: **vakum + 0.220 g itki yerçekimi** (novum: uzayda düşmek var) · risk 4/9 · doruk S21 temas %87.5 · merkezi seçim S19 (900 kg yük bırakılır, bedel aynı karede) · ✅ prompt_kontrol 0 BLOCK, 50/50 · üretim KAPI 0 (referans paketi) ile başlar |
| ⚠️🚨 | THE_BLUE_DRIFT | ⛔ön koşu ×5 · parti 🚨 geçersiz | 🚨 geçersiz | **2** | ⭐ **20.08.2026 · BEŞ MERCEK (🔧📖🧩🧍🔊), TEK OTURUM, HEPSİ MOD V — parti ⑤'ten geçmedi:** sahne sayıları 📖 10 · 🧩 15 · 🧍 15, film 25 segment → hiçbir tabloya skor yazılmadı, bulgudan ders yazılmadı (D107 ikinci vaka · D110 kopya). ⭐ **IZGARA GERİ ALINDI:** 16 planlı repliğin 14'ü, ızgara + prompt içi ofsetle hesaplanan saniyeye ±2 s oturdu → **SAHNE SIRASI DOĞRU**, tek şüphe S5/S6 (0:49-1:09, 20 s'lik tek kontrol); sahne şeridi 4:09'da bitiyor = planın RUNTIME'ı birebir; 4:09 sonrası ~5 s başlık kartı plana ait DEĞİL (D72 tekrarı). Dört bulgu planda yazılı TASARIM çıktı (S8 perde kenarı · S10 amber verici · S24 açık yakalama yuvası · telsizde kımıldamayan ağız) — biri filmin PLANLI FİNALİNİ kesmeyi önerdi → **DERS 115 + 116**. Kilit çelişkisi defteri: 21 madde ⬜ AÇIK, operatör iş listesi ~4 dk master. [→](01_FILM_RAPORLARI/THE_BLUE_DRIFT.md) 🔧📖🧩🧍🔊 ham rapor ✅ ×5 · sonraki tur MOD D (SPEC hazır) · ⛔ tamlık matrisi ❌ KALIR — ölçüm yapılmadı, ölçme aleti ölçüldü · — — — 🆕 17.08.2026 · YAZIM TAMAM: PLAN + PART_A + PART_B + KAPAK + REFERANS_PAKETI (5 sayfa × 4 panel) · 50 prompt + 2 kapak, prompt_kontrol 0 BLOCK / kapak ✅ GO · üretim KAPI 0 (referans) ile başlar · Cold Burn + Black Cradle ailesinin MAVİ üçüncüsü — mavi dev uydusu, planetshine, gökten inen plazma perdesi · novum: ÖLÜ ARACIN YAKALANIŞI (aktif taraf ilk kez ana gemi, doruk edilgen) · 25 sahne × 10 s = 4:09 standart · 16 replik (10 MACHINE) · merkezi seçim S14 (kabin havası = son itici, bedel ibrede) · doruk S21 %84-88 · risk 5/9 tam eşikte · ayrıntı tamlık matrisinde |
| ✅ | THE_COLD_BURN | **BEŞ mercek** 🔧🧩📖🧍🔊 | **5.0Ⓥ · 🧩7.0 · 📖4.0Ⓥ⚠️ · 🧍6.0 · 🔊5.0** | **2** | [→](01_FILM_RAPORLARI/THE_COLD_BURN.md) 🔧🧩📖🧍🔊 ham rapor ✅ ×5 · ⭐ **BEŞ raporlu ilk film + SES_QA ilk koşusu + DERS 82-83'ün kaynağı** · 🚨 kurgu kapısı 4/4 ihlal — ekranda 12/30 sahne, doruk/seçim/final yok · ❓ üretim zinciri doğrulanmadı |

---

# 🎞️ 7-9 dk — 2 film (1 ✅ / 1 ❌)

| | Film | Kapsam | Skor | Ders | Dosya |
|:--:|---|:---:|:---:|:---:|---|
| ✅ | THE_SLOW_STONE | Full ×4 rapor | 5/10 | 2 | [→](01_FILM_RAPORLARI/THE_SLOW_STONE.md) ✅ tam rapor |
| ❌ | THE_WAKING_GROUND | — | — | — | — |

---

# 🛰️ 10-20 dk — 1 film (0 ✅ / 1 ❌)

| | Film | Kapsam | Skor | Ders | Dosya |
|:--:|---|:---:|:---:|:---:|---|
| ❌ | THE_SECOND_SHIP | faz koşuları · **skor yok** | — | 7+8 (faz-içi) | 🆕 02.08.2026 · 120 sahne × 10s = 20:00 · plan + bible + senaryo + kapak + müzik + referans paketi · 05.08.2026: 10 faz × 10 sahne yapısı · **12.08.2026: Faz 7 üretildi ve koşuldu** → [F7 dersleri](../../yatay_10_20_dk_filmler/THE_SECOND_SHIP/FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md) · ham: [F6](02_HAM_RAPORLAR/THE_SECOND_SHIP_FAZ06_HAM.md) · [F7](02_HAM_RAPORLAR/THE_SECOND_SHIP_FAZ07_HAM.md) |

> ⚠️ Bu formatın ilk filmi. Sahne süresi 8s değil **10s** — format kartından
> bilinçli sapma, gerekçesi `THE_SECOND_SHIP/README.md` §1b.
> QA yapılırken SPEC bloğu 10 saniyeye göre doğrulanır.
>
> ⛔ **BU FİLMİN FAZ KOŞULARI SKOR TABLOLARINA GİRMEZ.** Faz rubrikleri
> (`FAZ_0N_QA_PROMPT.md`) `QA_PROMPTLARI/` ailesinden ayrı bir sistemdir —
> tek sahne değil, on sahnelik bir faz ölçerler; skorları buradaki
> tablolarla karşılaştırılamaz (AGENTS §6 "QA sistemi çatallı").
> Faz bulguları film klasöründeki `FAZ_0N_QA_DERSLER.md` dosyalarında durur.
>
> 📊 Faz koşuları: **F6 (11.08.2026)** reel · rapor yarım · skor yok ·
> **F7 (12.08.2026)** reel + sıra kayması · skor GEÇERSİZ (eşleme çöktü,
> [DERS 92]) · her ikisi de bulgu koşusu, taban koşusu değil.
> Üst üste iki koşu teslimat protokolü yüzünden taban üretemedi.
> Global derslere çıkanlar: **88 · 89 · 90 · 91 · 92**.

---

# 📱 DİKEY SHORTS — 12 film (2 ✅ / 10 ❌)

| | Film | Not |
|:--:|---|---|
| ❌ | THE_SLOW_TIDE_DIKEY_SHORTS | ⭐ yatay versiyonu QA edilmiş — **doğal kontrol grubu** |
| ❌ | THE_SLOW_STONE_DIKEY_SHORTS | ⭐ yatay versiyonu QA edilmiş (5/10) — ikinci kontrol grubu |
| ❌ | THE_SINKING_HOUR_DIKEY_SHORTS | 🆕 03.08.2026 · özgün konsept, kaynak film yok |
| ❌ | THE_DULL_EDGE_DIKEY_SHORTS | 🆕 04.08.2026 · **seride ilk savaş/tarihsel shorts** · özgün |
| ❌ | THE_HALF_SKY_DIKEY_SHORTS | 🆕 04.08.2026 · vakum/yörünge · özgün |
| ❌ | THE_WINTER_LINE_DIKEY_SHORTS | 🆕 05.08.2026 · **dikey hattın ilk günümüz-Dünya (2026) konsepti** · risk 2/9 · özgün |
| ❌ | THE_LOW_MOON_DIKEY_SHORTS | 🆕 05.08.2026 · insan ölçeğinde yörünge · **seride ilk sürekli hareketli merkez nesne** · özgün |
| ✅ | THE_FIRST_MORNING_DIKEY_SHORTS | 🆕 05.08.2026 · günümüz kapsülü Geç Kretase'ye düşer · **seride ilk megafauna — Kart 2 bilinçli ihlal** · üretim S4'ten başlar · özgün · 📱 **Ⓥ 6.0 REGENERATE** (06.08 — SHORTS_QA'nın ilk geçerli koşusu; 64 s kurgu + jenerik → DERS 70-71) |
| ✅ | THE_WRONG_SHADOW_DIKEY_SHORTS | 🆕 06.08.2026 · günümüz platosu, kaynaksız ikinci gölge seti · **Half Sky'ın tersi: fazla ışık, görünmez kaynak** · üretim S4'ten başlar · özgün · 📱 **Ⓥ 5.6** + 📖 **Ⓥ 3.0 REGENERATE** (06.08 — 🚨 novum ekrana hiç girmedi → DERS 73-74) |
| ❌ | THE_QUIET_IMPACT_DIKEY_SHORTS | 🆕 06.08.2026 · vakum/yörünge, iki geminin 12 m/s teması ve sonrasındaki sessizlik · **dikey hattın ilk aksiyon konsepti** · **novumu gerçek fizik olan ilk film** (Half Sky'ın tersi: yukarısı boş değil, dolu) · 0/3 mercek · üretim S4'ten başlar · özgün |
| ❌ | NINE_MINUTES_ROKET_YATAY_SHORTS | ⚠️ adı "YATAY" ama dikey klasöründe |
| ❌ | THE_WALKING_DAY_YATAY_SHORTS | ⚠️ adı "YATAY" ama dikey klasöründe |

---

# 📥 QA RAPORU GELDİĞİNDE

Bir filmin eleştirisini verdiğinde:

```
0. ÖNCE SPEC DOĞRULANIR ⛔ KAPI — raporun künyesi filmin PLAN dosyasıyla
   karşılaştırılır: sahne sayısı · süre · diyalog sayısı · sahne numaraları.
   Biri bile tutmuyorsa rapor GEÇERSİZ işaretlenir, skoru tabloya GİRMEZ.
   (Bu adım yoktu; 3 rapor bu yüzden uydurma bulgu üretti — Bulgu 7)
1. 01_FILM_RAPORLARI/<FILM_ADI>.md açılır (mevcut ✅ dosyalarla aynı şablon)
2. Yukarıdaki tabloda ❌ → ✅ çevrilir, skor ve ders sayısı yazılır
3. Skor tablosuna satır eklenir:
   · teknik QA  → LESSONS_LEARNED.md · KALİTE TAKİP TABLOSU
   · senaryo QA → 03_HIKAYE_KALITE_TABLOSU.md
   · mantık QA  → 04_MANTIK_KALITE_TABLOSU.md
3b. ⭐ MANTIK QA ise: FLAGS FOR DOCUMENT CHECK sorularının HER BİRİ plan
   dosyasından cevaplanır ve cevap ham rapora yazılır. Rubrik doküman
   istemediği için bu adım rubriğin ikinci yarısıdır — atlanırsa rapor
   yarım kalır. Tidal Hunt'ın iki sorusu Ders 20 ihlalini ve Bible'da
   yasaklanmış bir prop'u ortaya çıkardı.
4. Yeni ders varsa numaralandırılıp LESSONS_LEARNED.md'ye eklenir
   (senaryo QA kural olarak ders üretmez — dersler teknik hatalar içindir)
   ⚠️ İSTİSNA: senaryo QA'sının bulduğu şey EKRANDA GÖRÜNÜR bir teknik
   ihlalse ve plan dosyasıyla doğrulanabiliyorsa ders olur. Ders 45 böyle
   çıktı — The Inversion'ın teknik QA'sı hiç yapılmamıştı.
5. HAM RAPOR 02_HAM_RAPORLAR/ altına kaydedilir:
   · teknik  → <FILM_ADI>_HAM.md
   · senaryo → <FILM_ADI>_SENARYO_HAM.md
   ⚠️ Bu adım atlanırsa mevcut 10 filmdeki veri kaybı tekrarlanır
```

**Rapor verirken en değerli olan:** timestamp'li bulgu satırları
(`0:52 — Rappelling rope ignores collision physics`). Kategori skoru tek
başına ders çıkarmaya yetmiyor — mevcut 10 dosyanın sorunu tam olarak bu.

---

# 🚨 BU DERLEMEDEN ÇIKAN 7 BULGU

### 1. Kalite tablosu, en düşük skorları göstermiyor

QA rubriği **11 kategori** tanımlıyor. Kalite tablosunda **7 sütun** var.
Dışarıda kalan 4 kategori: Parçacık ve Malzeme · Diyalog ve Ses · Kare Çapası
Sadakati · Negatif İhlal.

Sonuç — projenin bilinen en düşük skorları tabloda **görünmüyor:**

| Film | Kategori | Skor | Tabloda? |
|---|---|:---:|:---:|
| Low Power | Parçacık ve Malzeme | **2/10** | ❌ |
| Low Power | Diyalog ve Ses | 3/10 | ❌ |
| Dead Approach | Diyalog ve Ses | 3/10 | ❌ |
| Dead Approach | Parçacık ve Malzeme | 4/10 | ❌ |
| Dead Approach | Negatif İhlal | 4 ihlal | ❌ |
| Ring Walker | Ölçek | 4/10 | ❌ sütun yok |

**2/10 projenin en düşük skoru ve hiçbir özet tabloda yer almıyor.**

### 2. Bir film QA edildi ama sisteme hiç girmedi

The Last Crossing: Compilation QA yapıldı, Genel 4/10 verildi, Ders 33 üretildi
— kalite tablosuna satır eklenmedi. 11 film üzerinden yapılan her ortalama
bu yüzden hatalı.

### 3. Ham veri 12 filmin 10'unda kayıp

Timestamp'li bulgu satırları sadece Orphan Bloom (3 satır) ve Dead Approach
(5 satır) için korunmuş. Diğer 10 filmde sadece kategori skoru var. Yani
derslerin çoğu **geri izlenemez** — hangi karede ne olduğu bilinmiyor.

### 4. En çok ders veren film, en az belgelenen film

Canopy World 8 ders üretti (44'ün %18'i) ve elimizde tek bir bulgu satırı yok.
Buna karşılık Tidal Hunt 3/10 alıp sadece 3 ders verdi. **Ders çıkarma
sistematik değil** — puanla ders sayısı arasında ilişki yok.

### 5. Bilinen künye hataları düzeltilmedi

- **Low Power (teknik):** SPEC bloğuna S14'e ait olmayan replik yazılmış;
  senaryoda S14 sessiz. Ders 40'ın (altyazı) geçerliliği bu yüzden şüpheli.
- **Low Power (senaryo, 31.07.2026):** SPEC 7 sahne / 254s / 1 monolog
  bildirmiş; film 25 sahne / 249s / 5 konuşmalı sahne. Rapor var olmayan bir
  kurguyu puanladı ve **filmde zaten çözülmüş iki şeyi eksiklik diye raporladı**
  (S17 umut beati, S6+S7 panel süpürme). → [ham rapor](02_HAM_RAPORLAR/LOW_POWER_SENARYO_HAM.md)
- **The Slow Stone:** 4 raporun 4'ü de boş SPEC ile çalıştı; ikisi var olmayan
  bir "Faz 5" için puan uydurdu. Karakter skoru doğrulanmamış.

### 8. 🚨 YENİ ARIZA TİPİ — RAPOR DOĞRU, FİLM SAPMIŞ (Ring Walker)

Bulgu 7 raporun uydurmasıydı. Bu, tam tersi: **rapor dürüst, film plandan
sapmış** — ve iş akışı bunu yakalayacak hiçbir adım içermiyordu.

| | Plan dosyası | Montajlanan video |
|---|---|---|
| Süre | 129 s | 115 s |
| Sahne | 13 | ~10 |
| **Tutulma (S7-S8)** | *"filmin duygusal zirvesi"* | ❌ **yok** |

Film, kendi dokümanının duygusal zirvesi olmadan monte edilmiş. Senaryo QA'sı
bunu **fark edemedi** çünkü doküman verilmemişti — yalnız video ile çalıştı.
Sonuç: Duygusal Yay 5/10 ve Yapı 5/10 puanları **hikayeye değil, eksik
montaja** ait. Satır bu yüzden ŞARTLI.

**Ortak kök — Low Power ile aynı yere çıkıyor:**

```
Low Power     rapor UYDURDU  ← SPEC plan dosyasından doldurulmadı
Ring Walker   film  SAPTI    ← doküman QA'ya girdi olarak verilmedi
              ↓
     İKİSİ DE: senaryo QA'sı plan dosyası olmadan çalıştırıldı
     → SENARYO QA DOKÜMANSIZ ÇALIŞTIRILMAZ (rubrik zaten "video + doküman" diyor)
```

Ayrıca bu, **teknik QA'nın hiç bakmadığı** bir hata sınıfı: montaj bütünlüğü.
11 teknik rapor kare içindeki hataları arıyor; hiçbiri "planlanan sahne
ekranda var mı?" diye sormuyor.

### 9. 🚨 KURGU, PLANA İKİ ZIT YÖNDEN SAPIYOR — VE KİMSE ÖLÇMÜYOR

Ring Walker eksik monte edilmişti. The Inversion'ın tersi çıktı:

| | Plan | Kurgu | Fark | Arıza |
|---|---|---|---|---|
| **Ring Walker** | 129 s / 13 sahne | 115 s | **−14 s** | doruk sahnesi (tutulma) hiç yok |
| **The Inversion** | 130 s / 13 sahne | 167 s | **+37 s** | 30 s tekrar + planlanmamış jenerik kartı |

The Inversion'ın fazla 37 saniyesi hesaplanabiliyor:

```
S8  su damlası tekrarı     10 s   (S4'ün kopyası)
S9  tether tekrarı         10 s   (S5'in kopyası)
S10 yaratık geçişi tekrarı 10 s   (S6/S7 kopyası)
S17 jenerik kartı           5 s   (planda YOK)
                          ─────
                           35 s ≈ +37 s
```

**Fazla sürenin tamamı tekrar ve planlanmamış karttır — tek saniye yeni
anlatı yok.** Rapor bunu "redundant visual loop" diye hikaye kusuru saydı ve
Yapı'ya 4/10 verdi. Aslında senaryo değil **kurgu** hatası; puan yanlış yere
yazılmış oluyor.

İki film aynı formatta, aynı hafta, aynı hata sınıfının iki yüzü. Bunu ölçen
tek yer `MANTIK_QA §1` (Plan ↔ Edit Conformity). Inversion'da çalıştırıldı ve
aynı 40 saniyelik tekrar döngüsünü bağımsız olarak buldu (3.0/10) — **iki
rubriğin aynı hatayı iki farklı adla bulması, bulgunun doğrulanmasıdır.**
Ring Walker'da henüz çalıştırılmadı.

### 6. Kapsam karşılaştırılabilir değil

4 film "Montaj", 4 film "Full", 1 film "tek sahne", 1 film "4 rapor × full".
Aynı tabloda toplanmış skorlar **aynı şeyi ölçmüyor.**

### 7. 🚨 SPEC HATASI TEK SEFERLİK DEĞİL — SİSTEMİK

Dört bağımsız QA çalıştırması, iki farklı rubrikle, aynı biçimde bozuldu:

| Çalıştırma | Hata | Sonuç |
|---|---|---|
| The Slow Stone ×4 | SPEC boş | var olmayan "Faz 5" puanlandı |
| Low Power teknik | SPEC'te yanlış replik | Ders 35/40 yanlış sahneye atfedilmiş olabilir |
| Low Power senaryo | SPEC'te yanlış sahne sayısı/süre | 7 sahnelik hayali bir film puanlandı |
| Ring Walker senaryo | doküman verilmedi | montajdaki eksik sahne fark edilmedi |
| Kaleida Crash senaryo | doküman verilmedi | 2 viral ara sahne + tek tehlike sahnesi kesme listesine yazıldı |
| Inversion senaryo | **"plan doc unsupplied" dedi — oysa dosya depoda** | +37 s kurgu dolgusu ve karakter adı doğrulanamadı |
| "The Inverted" teknik · 01.08 | **kapıyı okudu, kendine muafiyet yazdı** — SPEC videodan dolduruldu | doğrulanmamış alanlardan 3 🔴 BLOCKER · filmin öncülü hata sayıldı |
| "The Inverted" senaryo · 01.08 | doküman verilmedi — **aranmadı da** | kapı tuttu, çıktı yok (tek doğru davranış) |
| "The Inverted" mantık · 01.08 | **video verilmedi**, rubrikte girdi-yok protokolü yok | sıfır blocker'lı boş rapor iskeleti üretildi |

> 🚨 **01.08.2026 — üç mercek arka arkaya, üçü de girdisiz çalıştı. Geçerli
> skor: 0/3.** Bu üç satırın hiçbiri kalite tablolarına girmeyecek.
> Yeni olan: kapı artık **eksik değil, pazarlık konusu.** VIDEO_QA raporu
> kapıyı alıntıladı, "dosyalar verilmediği için görsel kanıttan dolduruyorum"
> dedi ve puanlamaya devam etti — SPEC videodan doldurulunca inceleme
> döngüsel hale geliyor, film kendi kendisiyle karşılaştırılıyor.
> Ayrıca rapordaki **FILM adı kütüphanede yok:** "The Inverted" diye bir film
> yok, en yakın eşleşme `THE_INVERSION_PLANET_FILM.md` — ve o dosya raporun
> üç BLOCKER'ını da çürütüyor (ters yerçekimi ve saç yönü **tasarım gereği**,
> satır 114-116 / 150-158; buna karşılık raporun 🟠 saydığı elde-tablet
> satır 133 **HANDS ALWAYS EMPTY** ile gerçek bir ihlal).
> → Ders 51-54 (`../LESSONS_LEARNED.md`)

> 🚨 **Inversion satırı diğerlerinden farklı ve daha kötü:** önceki dört
> çalıştırmada doküman *verilmemişti*; burada rapor dokümanın **var olmadığını
> varsaydı.** Kapı yazıldıktan sonraki ilk çalıştırma da kapıyı atladı.
> Kapı bir prompt satırı olarak yeterli değil — **çalıştırmadan önce plan
> dosyasının yolu elle verilmeli.**

**Ortak nokta: hiçbirinde künye plan dosyasıyla karşılaştırılmadı.**
Model, eksik veya yanlış künyeyi "bilmiyorum" diye raporlamak yerine
tamamlıyor. Bu, rubriğin değil **iş akışının** açığı: doğrulama adımı yoktu.
→ `VIDEO_QA` ve `SENARYO_QA` promptlarına zorunlu **STEP 0 — SPEC DOĞRULAMA
KAPISI** eklendi (31.07.2026). Uyuşmazlıkta rapor puanlanmadan durur.

**En pahalı sonucu:** Low Power senaryo raporu, filmde **zaten var olan iki
şeyi** eksiklik diye raporladı (S17 umut beati · S6+S7 panel süpürme).
Doğrulanmamış QA yalnızca yanlış ölçmez — **düzgün çalışan tasarımı
bozmaya yönlendirir.**

---

# 📋 YAPILACAKLAR

```
□ 🔴 THE BLUE DRIFT: 4:09-4:14 başlık kartı kurgudan ÇIKARILIR — plan iki
  yerde yasaklıyor (D72 ×7). Kart gidince kurgu kapısı 4/4 kapanır:
  25 klip · 249 s · ekran metni 0.0 sn. Dört mercekteki 🔴/🟠 da düşer
□ 🔴 THE BLUE DRIFT: KİLİT ÇELİŞKİSİ DEFTERİ — 21 madde ⬜ AÇIK, toplam
  ~4 dakikalık master işi. Sırasıyla:
    0:49-1:09  S5/S6 sırası (sıra denetiminin tek açığı)
    0:22·1:33·2:13·2:43·3:39  KERTE sentetik mi, insan sesi mi (D82 sorusu)
    2:12-2:18 · 1:45-1:51 · 2:20-2:26 · 3:19-3:25  replik metinleri
      (kırk/bir · itici/verici · avanis/havanız · pencere/metre)
    2:38-2:47 · 3:20-3:30  replik tekrarları
    0:39-0:49 · 2:59-3:09 · 1:39-1:49 · 0:09-0:19 · 2:29-2:39  el/ikiz/gaz
    3:49-3:59  yüz durumu (🔧 "morph" der, 🧍 "temiz" der — zıt)
□ ⛔ THE BLUE DRIFT: 🧩 raporunun 1 numaralı reçetesi UYGULANMAZ — "4:00
  çekimini kes" filmin PLANLI FİNALİNİ (S24) siler. 📖'ün kesme listesi de
  uygulanmaz: 1:30-1:45 filmin dönüm noktası (S9) + umut vuruşudur (S10)
□ THE BLUE DRIFT: defter kapanınca mercekler MOD D koşulsun — SPEC planın
  §QA SPEC BLOĞU'nda hazır. ⭐ Depoda mod D hâlâ hiç denenmedi; SPEC'i
  hazır olduğu hâlde mod V koşulan film sayısı bu filmle 6 oldu (D94)
□ THE BLUE DRIFT: K1-K4/K7 kapanırsa ders adayları yazılır — Türkçe repliğin
  üretimde bozulması (sayı/kişi/anahtar sözcük) · replik tekrarı · D82
  sigortasının prompt gövdesinde yazılıyken tutmaması
□ 🔴 THE THIRD DUNE: 4:00 yanık başlık kartı KURGUDAN ÇIKARILIR — üretim
  hatası değil, kapak başlığının kurguya eklenmesi (D70/72 ×4). Tek 🔴
  bu adımla kapanır, yeniden üretim gerekmez
□ 🔴 THE THIRD DUNE: SES_QA 245 s kurgu ile YENİDEN koşulsun (girdisiz koşu
  geçersiz — D80 ×2). Kritik soru: S1'in ÇOBAN repliği (MACHINE, gövdesiz)
  ekranda kadın astronota mı atanmış? Register tablosu planda hazır (D82)
□ 🟠 THE THIRD DUNE: yeniden üretim adayları — 2:10 (mor bant yok) ·
  2:40+2:50 (toz sıfırlanmış suitler) · 1:50 (eldiven-kum) · 2:51
  (anahtar-bacak) · 3:30 (derin krater → sığ süpürme çanağı, S22 metni
  zaten doğru). ⚠️ Promptlar DEĞİŞTİRİLMEZ, cümleler doğru — D84
□ 🟠 THE THIRD DUNE: klip süreleri tek tek ölçülsün — 245 s ≠ 249 s;
  en olası sebep iki klipte 2 s extend uygulanmamış olması
□ THE THIRD DUNE: 📖 raporunun KESME LİSTESİ UYGULANMAZ — iki öneri de
  viral ara sahneye giriyor (S3 · S12), ikincisi orta nokta REVEAL'ini
  siler. "Kum taşınıyor" repliği de kesilmez (yarım alıntı)
□ THE THIRD DUNE: bir sonraki turda 🔧 ve 📖 MOD D koşulsun — SPEC bloğu
  planın 856. satırında hazır, üç yanlış bulgu mod D'de imkânsızdı
□ 🔴 THE BLIND RETURN: kurgu onarımı — S15 kurguya eklenir (üretilmediyse
  üretilir: Çehov 4 yedek vizör + "forty hours" repliği), S16↔S17 sırası
  düzeltilir (çıkış ÖNCE, kalkış SONRA) — DERS 81'in kaynağı
□ 🔴 THE BLIND RETURN: 2:30-2:39 klibi doğrulansın — kalkışın kendisi
  (ateşleme 5.5 s + koni + yükseliş) klipte var mı? Yoksa S17 yeniden
□ 🔴 THE BLIND RETURN: VIDEO_QA GERÇEK kurgu dosyasıyla koşulsun (girdisiz
  koşu geçersiz — DERS 80); SPEC §0.15'ten → MOD D. Özel bakılacaklar:
  S11 köpük dokusu · toz akış yönü (SAĞ→SOL ihlali adayı) · S4 kumaş ·
  S17 biniş anı klon taraması (D69) · lamba TEK mi · tüp SOL uylukta mı
□ 🟠 THE BLIND RETURN: D79 çekirdek cümlesi ("flat back silhouette…")
  36 prompta eklensin; sırt ünitesi/çift lamba görünen klipler yeniden
  üretim adayı (D79'un 3. vakası)
□ THE BLIND RETURN: S8 (soluk disk) ve S9 ("forty meters" repliği) kurguda
  var mı — iki mercek de 1:20-1:40'ı tek blok okudu, doğrulanmalı
□ THE BLIND RETURN: kurgu onarımından sonra SENARYO_QA MOD D ile tekrar
  (mevcut Ⓥ satırının yarısı kurgunun puanı)
□ 🚨 THE STARLESS CIRCLE: 🔧 ve 📖 merceklerine HANGİ DOSYA yüklendi?
  12 s · çanaksız · yıldızsız · kayaya temas — plan 10 s klip, ufka kadar
  çanak, yoğun yıldız alanı diyor. Yanlış dosyaysa iki satır da silinir
□ 🚨 THE STARLESS CIRCLE: senaryo QA'sı TAM KURGU (174 s) + BÖLÜM 0 ile
  tekrar koşulsun — mevcut satır 12 s klibin puanı, GEÇERSİZ (DERS 75)
□ 🔴 THE STARLESS CIRCLE: 2:50 başlık kartı kurgudan çıkarılsın —
  "THE CIRCLE WITH NO STARS" kapak promptu A'nın başlık satırı (D72 ×2)
□ 🔴 THE STARLESS CIRCLE: S14 (biniş) yeniden üretilsin — biniş HAREKETİ
  kadraj dışına, DERS 69 ① gereği; kurgu kurtarması iki figürlü kadrajı keser
□ 🔴 THE STARLESS CIRCLE: S12 (PRE-DAWN) yeniden üretilsin — tek sahne hem
  gece→gündüz sıçramasını hem görünmeyen bedeli (boş kalça yuvası) çözer
□ THE STARLESS CIRCLE: KAPI 2 (daire testi) sonucu kayda geçirilsin; daire
  nesneleşmeye devam ederse dosyadaki Plan B uygulansın (D74 · D76)
□ 🚨 THE DAWN FRONT: PLAN B ile yeniden üretim — 26 segment AYRI klip,
  kesme kurguda (Ders 68 · plan §0.20). Bu kez S0 test adımı ATLANMAZ:
  S0 temiz çıkmadan kalan sahneler üretilmez
□ 🚨 THE DAWN FRONT: duvar/baca yeniden üretiminde Ders 67 Katman 1
  pozitif tarifi eklensin; şelale/alev TEKRARLARSA malzeme değişir
  (Risk Kartı 6) — üçüncü kez aynı görüntü istenmez
□ THE DAWN FRONT senaryo QA'sı video + PLAN dosyasıyla koşulsun
  (ilk koşu INPUT MISSING ile doğru şekilde durdu)
□ THE DAWN FRONT: kurgu sürümü doğrulansın — teknik rapor 141 s,
  mantık raporu 145 s ("_2.mp4") ölçtü; hangisi güncel?
□ THE DAWN FRONT: 2:04'teki film içi metin doğrulansın (kapanış kartı
  değilse Ders 13/34/45 ihlali — klip yeniden üretilir)
□ 🚨 THE INVERSION: 2:12'deki ekran metni ("Dr. Kaya Uçan...") — o klip
  yeniden üretilsin. Plan metni zaten yasaklıyordu; sorun prompt biçiminde
  (Ders 45). Prompt'taki [BIBLE] etiketleri ve "CAMERA: 75mm, f/5.6" satırı
  düz cümleye çevrilmeden tekrar üretilmesin
□ THE INVERSION: +37 s kurgu dolgusu (S8-S10 tekrarları + jenerik kartı)
  kurgudan çıkarılsın → 130 s plana döner, format tabanı korunur
□ THE INVERSION: planlanan S10 (DÖNÜŞ: GEMİ DEMİR) kurguda bulunamadı —
  doğrulansın
□ THE INVERSION teknik QA'sı hiç yapılmadı — VIDEO_QA çalıştırılsın
□ Ring Walker ve Inversion için MANTIK_QA çalıştırılsın (plan↔kurgu tablosu)
□ The Last Crossing için kalite tablosuna satır ekle
□ Kalite tablosuna 3 sütun ekle: Parçacık · Kare Çapası · Negatif
  (Diyalog sütunu artık gerekmiyor — 09.08'de ayrı mercek açıldı: SES_QA)
□ 🔊 SES_QA sıradaki koşular: ① THE BLIND RETURN (169 s kurgu elde, 8 replik
  hepsi SUIT AI → register kapısının ikinci testi — Cold Burn'de harita
  planla çelişti, Blind Return'de MACHINE ağırlıklı ilk koşu olur)
  ② LOW POWER ③ THE DEAD_APPROACH (ikisi Diyalog ve Ses 3/10 — D35/D40
  kaynakları) — ✅ ilk koşu 09.08'de yapıldı (Cold Burn), 07 tablosu açıldı
□ 🔴 THE COLD BURN — ÜRETİM SORUSU önce: kurgu PART_A/B promptlarıyla mı
  üretildi? Kapı kayıtları (S12·S21·S22·S25) nerede? [D74] Cevap gelmeden
  yeniden üretim başlamaz (D79 ×4 şerhi de bu cevaba bağlı)
□ 🔴 THE COLD BURN miks seansı (yeniden üretim GEREKTİRMEZ — D83):
  1:20-1:40 yatak serilir · 0:50 delik kapanır · 3:00 yangın yatağı
  -6 dB duck · kokpit repliklerine telsiz EQ geri · müzik kuyrukları
□ 🔴 THE COLD BURN kurgu: 3:40 başlık kartı çıkarılır (metni doğrula —
  "THE COLD BURN" ise kapak başlığı sızması, D72 zinciri 3. vaka)
□ 🔴 THE COLD BURN eksik omurga (üretim sorusu cevaplandıktan sonra):
  S19 CENTRAL CHOICE · S26 DORUK · S29 FİNAL öncelikli; ardından
  S13-S14 · S16-S17 · S20 · S22-S23 · S27-S28 · S12 vakum fiziğiyle
  yeniden (sessiz patlama) · EKO geri getirilir [D82]
□ THE COLD BURN plan içi tutarsızlık: §QA SPEC "12 replik + S28 konuşmalı"
  ↔ DIALOGUE SCHEDULE "14 replik / 11 sahne, S28 sessiz" — plan düzeltilsin
□ Ders 21 (statik ateş) kategorisini Çevre → Parçacık olarak düzelt
□ Low Power'ı dolu SPEC ile tekrar QA et — Ders 40 doğrulanmalı
□ Low Power SENARYO QA'sını doğru SPEC ile tekrar çalıştır
  (25 sahne · 249s · 5 konuşmalı sahne · viral S5/S14/S19/S23 · seçim S20)
□ Her QA çalıştırmasından önce SPEC bloğu filmin PLAN dosyasından doldurulsun
  — serbest hatırlamayla değil (3 raporun 3'ü bu yüzden bozuldu)
□ THE_KALEIDA_CRASH_PLANET_FILM.md: "13 SAHNE" diyor ama 12 blok var,
  SAHNE 3 hiç yok (S2 → S3.5). 12 promptun 12'si "Scene N of 13" diyor.
  → numaralandırma mı düzelecek, eksik S3 mü yazılacak: içerik kararı
□ 🚨 THE_TIDAL_HUNT: sayaç metinsiz kanala taşınsın (Ders 50) — plan dosyası
  kendi içinde çelişiyor: satır 285 "NEVER text" · satır 338 "reads 6:00:00"
□ 🚨 THE_TIDAL_HUNT: S8.5 yazılsın — dalganın çarptığı an hiçbir sahnede yok,
  filmin doruğu iki sahne arasına düşmüş (senaryo boşluğu, kurgu değil)
□ THE_TIDAL_HUNT: S1 ve S10 yeniden üretilsin — film SOLO, iki kâşif Ders 20
□ THE_TIDAL_HUNT senaryo QA'sı yapılsın — dalga boşluğunu bağımsız bulmalı
□ Kaleida Crash senaryo QA'sını PLAN DOSYASIYLA tekrar çalıştır
  (12 sahne · ~120s · sessiz · viral ara sahneler S3.5 ve S6.5)
□ 2-4 dk filmlerinin planlarına "karakter neyi kaybediyor?" sorusu eklensin
  — iki bağımsız senaryo raporu da Karakter'e 4/10 verdi, ikisi de aynı
  gerekçeyle: bedelli seçim yok
□ 🚨 RING WALKER: tutulma sahneleri (S7-S8) neden montajda yok — üretilmedi mi,
  üretildi de düştü mü? Plan 129s/13 sahne, video 115s. Cevap bulunmadan
  hikaye satırı ŞARTLI kalır
□ Ring Walker senaryo QA'sını tutulmalı kurgu + doküman ile tekrarla
□ Ring Walker videosundaki "title card" doğrulansın — bilinçli mi, yoksa
  Ders 9 / Ders 34 tekrarı mı?
□ Senaryo QA artık DOKÜMANSIZ çalıştırılmasın — iki raporun ikisi de
  yalnız videoyla çalıştı ve ikisi de kullanılamaz çıktı
□ The Slow Stone Geçiş 2'yi dolu SPEC ile tekrar çalıştır — karakter skoru
□ Ders 33'ün başlığını Türkçeleştir (biçim tutarlılığı)
□ Ders 11 ↔ 24 ↔ 43 (temas morphu) birleştirilebilir mi incele
□ Ders 23 ↔ 33 (sıfır-g momentum) örtüşmesini incele
□ THE_SLOW_TIDE dikey versiyonunu QA et — format karşılaştırması için
□ Her yeni QA raporunun HAM DOSYASI bu klasöre kaydedilsin (ders özeti yetmez)
```

---

# 🔗 İLGİLİ DOSYALAR

| Dosya | İçerik |
|---|---|
| `03_HIKAYE_KALITE_TABLOSU.md` | senaryo QA skorları (teknikten ayrı tablo) |
| `04_MANTIK_KALITE_TABLOSU.md` | mantık/devamlılık QA skorları — üçüncü mercek |
| `06_KARAKTER_KALITE_TABLOSU.md` | 🆕 karakter kimlik/devamlılık skorları — opsiyonel derin mercek |
| `07_SES_KALITE_TABLOSU.md` | 🆕 ses/diyalog skorları — 09.08'de Cold Burn ilk koşusuyla açıldı |
| `08_YAYIN_PERFORMANS_TABLOSU.md` | 🆕 22.08 · **gerçek izleyici koşuları** — yukarıdakileri bir MODEL doldurur, bunu VERİ doldurur. Bu matrise sütun AÇMAZ (QA merceği değil); çakışma hâlinde bu tablo üstündür |
| `../YAYIN_VE_PERFORMANS_KILAVUZU.md` | 🆕 22.08 · o tabloyu besleyen kılavuz — karar matrisi, sinyal/gürültü eşiği, geri besleme yolu |
| `02_HAM_RAPORLAR/` | ham QA çıktıları — özetlenmemiş |
| `../LESSONS_LEARNED.md` | ders arşivi + ⛔ KAPALI teknik kalite tablosu (→ T1) |
| `T1_KARE_KALITE.md` · `T2_DEVAMLILIK_KALITE.md` · `T3_SES_KALITE.md` · `T4_HIKAYE_KALITE.md` | ⭐ **22.08'den beri CANLI dört tablo** — yeni skorlar buraya yazılır |
| `../QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md` | ① sahne içi · 11 kategori + 3 dikey anahtar |
| `../QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | ② sahneler arası · 13 kategori (gövde 1-6 · dünya 7-13) |
| `../QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md` | ③ 9 kategorili ses merceği — yalnız kurgu |
| `../QA_PROMPTLARI/4_HIKAYE_QA_CRITIQUE_PROMPT.md` | ④ dramaturji · 10 kategori |
| `../QA_PROMPTLARI/ARSIV_6_MERCEK/` | ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ; bu depodaki 83 ham rapor onlarla üretildi |
| `../../yatay_7_9_dk_filmler/kilavuzlar/kalite_kontrol/` | 3 geçişli QA sistemi |
| `../../yatay_7_9_dk_filmler/THE_SLOW_STONE/QA_RAPORU.md` | tek tam QA raporu |
