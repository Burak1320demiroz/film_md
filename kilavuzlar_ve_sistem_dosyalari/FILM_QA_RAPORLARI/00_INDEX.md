# 📇 FİLM QA RAPORLARI — KONTROL LİSTESİ

> **Amaç:** Hangi filmin eleştirisi var, hangisinin yok — tek bakışta.
> **Veri kaynağı:** `LESSONS_LEARNED.md` (kalite tablosu + derslerin kaynak
> satırları) ve `yatay_10_20_dk_filmler/THE_SLOW_STONE/QA_RAPORU.md`
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
TOPLAM FİLM                86   ← kaynak her zaman sayac.sh'tir; betik artık
                                bu sayıyı kendisi karşılaştırıp ❌ basıyor
                                (07.09.2026: +1 → 85→86. THE OPEN CIRCUIT
                                yazıldı — yatay 3-5 dk, **SEKİZ dosya tam**
                                (REFERANS_PAKETI dâhil; §2.0 iskeletinin
                                sekizini birden taşıyan İLK film), QA paketi
                                SPEC ile birlikte üretildi [D165],
                                prompt_kontrol klasör modu 0 BLOCK · GO.)
                                (06.09.2026: +1 → 84→85. THE KEPT LIGHT
                                yazıldı — yatay 3-5 dk, yedi dosya tam,
                                QA paketi SPEC ile birlikte üretildi [D165],
                                prompt_kontrol klasör modu 0 BLOCK · GO.)
                                (05.09.2026: +1 → 83→84. THE STANDING WIRE
                                yazıldı — yatay 3-5 dk, yedi dosya tam,
                                QA paketi üretildi, prompt_kontrol 0 BLOCK.
                                Aynı gün daha önce: −1 → 84→83. AYNI GÜN AÇILIP
                                KAPANAN BANT: `dikey_20_25_dk_filmler/` sahip
                                kararıyla kaldırıldı (kart H2), tek filmi
                                THE OWED AIR ile birlikte. Bandın izi
                                bırakılmadı — KILAVUZ_REHBERI'ye format kartı
                                GİRMEDİ, sayac.sh FİLM_DIZIN listesinden
                                çıkarıldı, T tablosundaki satır kaldırıldı.
                                ⛔ Film hiçbir commit'te değildi: GERİ
                                ALINAMAZ — AGENTS.md §6 + kart H2 beşinci tur.
                                Aynı gün `film_analizleri/` de kaldırıldı;
                                o klasör sayıma zaten girmiyordu.)
                                (02.09.2026: −1 → 80→79. MÜKERRER KAYIT
                                KALDIRILDI, film silinmedi: THE ROSE COAT
                                iki yerde duruyordu — hem
                                `yatay_2_4_dk_filmler_uzay/THE_ROSE_COAT/`
                                içinde hem de format klasörünün KÖKÜNDE
                                `THE_ROSE_COAT_DUST_PLAIN_FILM.md` olarak
                                (26.08.2026'dan beri, commit 60e52f7). İki
                                dosya sondaki satır sonu dışında BİREBİR
                                aynıydı; kökteki kopya `git rm` ile
                                kaldırıldı, klasördeki kopya yerinde.
                                ⛔ Sebep KILAVUZ_REHBERI §2.0: sayaç format
                                klasörünün kökündeki HER .md girdisini bir
                                film sayar — depo bu yüzden bir haftadır
                                bir film fazla sayıyordu. Artık hiçbir
                                format klasörünün kökünde .md yok.)
                                (03.09.2026: +1 → 80→81. THE PRESSED FIELD —
                                yatay 2-4 dk · ince atm. (§3.2) · 10 sahne ×
                                10,0 s = 1:40 (sahip kısıtı; bant sapması
                                planda tek satır [D74]) · ⭐ depoda UZAYLI
                                VARLIK içeren İLK film ve
                                UZAYLI_VARLIK_TASARIM_KILAVUZU'nun ilk
                                uygulaması — varlık K0-K1 kademesinde,
                                gövde/uzuv/gölge 10/10 sahnede 0 KARE ·
                                TEMA İLK-TEMAS · 7 dosyalı klasör + QA
                                paketi (PAKET_1..8) yazımla aynı gün)
                                (02.09.2026: +1 → 79→80. THE LEANING ROOM —
                                yatay 2-4 dk · 🆕 VAKUM + İTKİ YERÇEKİMİ'nin
                                KABİN İÇİ dalı (§3.5) · depodaki ilk KASKSIZ
                                ve ilk tamamen ARAÇ İÇİ film (dış mekân
                                0 kare) · TEMA ENTROPİ · yedi dosyalı klasör
                                iskeleti (§2.0) tam; bu matriste 0/4 satırı
                                var)
                                (02.09.2026: +1 → 78→79. THE HEAVY SIDE —
                                dikey shorts · proje sahibi ekledi ·
                                ⛔ BU MATRİSTE HENÜZ SATIRI YOK: filmi
                                yazan/okuyan ajan satırı ekler; sayım
                                betiğe göre güncellendi, içerik
                                uydurulmadı)
                                (01.09.2026: +1 → 77→78. THE STILL SWARM —
                                yatay 2-4 dk · VAKUM / serbest düşüş 0 g ·
                                İLK TEMAS temasının depodaki ilk kullanımı ·
                                yedi dosyalı klasör iskeleti (§2.0) tam;
                                bu matriste 0/4 satırı var)
                                (01.09.2026: +1 → 76→77. THE COLD WELD —
                                yatay 2-4 dk · 🆕 VAKUM + TEMİZ METAL
                                (soğuk kaynak, KILAVUZ_REHBERI §3.8 bu
                                filmle açıldı) · FILM + QA_SPEC; bu
                                matriste 0/4 satırı var)
                                (31.08.2026: +1 → 75→76. THE PAYLOAD —
                                yatay 3-5 dk · Mars toz fırtınası → alçak
                                yörünge · ayrılış/insan-makine sınırı;
                                PLAN + PART_A/B + KAPAK + QA_SPEC; bu
                                matriste 0/4 satırı var)
                                (29.08.2026: +2 → 73→75. Biri THE FROST LINE
                                (aşağıda), öbürü THE HEAVY SIDE (dikey shorts
                                klasörü — AYNI GÜN, AYRI OTURUMDA açıldı ve bu
                                satır yazılırken git'te izlenmiyordu; matris
                                satırını o dosyanın sahibi yazar, burada yalnız
                                SAYIMA girdi — THE THIN ROOF / SKYLIGHT emsali)
                                (29.08.2026: THE FROST LINE —
                                yatay 3-5 dk · Mars · sera tüneli dikiş
                                kaçağı, aksiyon/kimlik; PLAN + PART_A/B +
                                KAPAK + QA_SPEC; bu matriste 0/4 satırı var)
                                (28.08.2026: +1 → 72→73. YERÇEKİMİ —
                                yatay 10-20 dk klasörünün İKİNCİ filmi
                                (vakum/alçak yörünge · 120 × 8 s = 16:00 ·
                                Gravity 2013 yapı sökümünden, 04_ARASTIRMA
                                §TUR 2); ADIM 1 planı + ADIM 2 README
                                yazıldı, referans paketi/fazlar/SPEC
                                sırada — bu matriste 0/4 satırı var)
                                (27.08.2026: +2 → 70→72. Biri THE THIN ROOF
                                (dikey shorts · Mars · bu matriste 0/4 satırı
                                var), öbürü THE SKYLIGHT (yatay 3-5 dk ·
                                Mars · AYNI GÜN, AYRI OTURUMDA yazıldı ve
                                bu satır yazılırken hâlâ devam ediyordu —
                                matris satırını o dosyanın sahibi yazar,
                                burada yalnız SAYIMA girdi. İki film aynı
                                jeolojik olguyu birbirinden habersiz seçti;
                                çakışma kaydı THE THIN ROOF dosyasının
                                başındadır)
                                (26.08.2026: ZOMBİ TÜRÜ KAPANDI — kart H2,
                                depo yalnız UZAY filmleri. Dört film
                                kaldırıldı ve dördü de matristen düştü:
                                THE HELD HEAT · THE LAST SPAN (klasörle
                                birlikte) · THE SHORT WAY DOWN ·
                                THE STRAIGHT LINE (dikey shorts içinde
                                duruyorlardı — tür klasöre eşit değil),
                                74→70. ⚠️ THE LAST SPAN'ın QA kaydı ve
                                7 ham raporu KASITLI OLARAK DURUYOR
                                (kural ④) ama artık bir METODOLOJİ
                                kaydıdır: skor üretmez, bu matrise
                                girmez, kıyas tabanı sayılmaz
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
                                DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_
                                SECKISI.md ona atıf veriyor) −1 → net değişim yok,
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
                                22.08.2026: dikey hatta zombi kartı
                                geri açıldı — THE WARM FLOOR yazıldı,
                                aynı gün THE SHORT WAY DOWN ile
                                DEĞİŞTİRİLDİ (atmosferik gerilimden
                                bina içi kaçışa); net değişim +1,
                                64→65 · 23.08.2026: THE STRAIGHT LINE
                                yazıldı (dikey shorts — aynı türün
                                AÇIK YOL denemesi; Short Way Down
                                SİLİNMEDİ, ikisi de duruyor çünkü
                                yatay THE LAST SPAN birincisine
                                esaslı atıf veriyor), 66→67 ·
                                24.08.2026: THE IRON SLOPE yazıldı
                                (dikey shorts — vakum+itki kartının
                                [§3.5] DİKEY hattaki ilk filmi; risk
                                4/12; SPEC ayrı dosyada [D117] — tek
                                dosyalı formatta ilk ayrı SPEC dosyası,
                                sayaç onu film saymaz), 67→68 ·
                                25.08.2026: THE ROSE COAT yazıldı
                                (2-4 dk uzay · 13 sahne · deponun
                                İKİNCİ iki figürlü uzay filmi; SPEC
                                ayrı dosyada [D117], sayaç onu film
                                saymaz), 68→69 ·
                                25.08.2026: THE NEAR PASS yazıldı
                                (dikey shorts — çok yakın uydu; klasörün
                                ilk 60 saniyelik dosyası ve D124'ten
                                sonra ızgarası ARAÇTAN yazılan ilk film;
                                risk 4/12; SPEC ayrı dosyada [D117],
                                sayaç onu film saymaz), 69→70 ·
                                26.08.2026: THE BRIGHT TETHER ve
                                THE OPEN SEAM yazıldı (ikisi de dikey
                                shorts, aynı kullanıcı brief'inin
                                sonraki turları) +2, ve aynı gün
                                yatay_2_4_uzay ile _zombi klasörlerine
                                bu oturumun DIŞINDAN birer dosya
                                girdi +2 → 70→74. ⚠️ THE NEAR PASS ve
                                THE BRIGHT TETHER aynı brief'in
                                üstü çizilmiş turlarıdır ve silinme
                                kararı proje sahibindedir; THE BRIGHT
                                TETHER'ın SPEC dosyası YOK, yani
                                "yazımı tamam" sayılmaz [kart A])
✅ QA VERİSİ OLAN          33   (31.08: THE FROST LINE film kaydı açıldı 32→33 ·
                                ⚠️ ara düzeltme: 28-29.08'de açılan THE THIN
                                ROOF ve THE SKYLIGHT kayıtları bu satıra hiç
                                işlenmemişti, 30→32 farkı burada kapatıldı ·
                                %43 — 25.08: THE IRON SLOPE eklendi
                                (altı mercek koşuldu, altısı da ⛔ ön
                                koşu; tamlık matrisi ❌ KALIR — ölçüm
                                yapıldı, UYGUNLUK ölçülmedi), 29→30 ·
                                film kaydı sayısı 30, ama biri
                                THE_BLACK_CRADLE_FRAGMAN: fragman film
                                sayımına girmez, 29+32 = 61 korunur ·
                                17.08: THE BLACK CRADLE kaydı açıldı,
                                beş mercek — dördü 🚨 GEÇERSİZ [D107])
❌ ELEŞTİRİSİ OLMAYAN      42   (31.08 uzlaştırma: THE FROST LINE ✅'ye geçti;
                                29-31.08'de yazılan FROST LINE ve PAYLOAD bu
                                satıra hiç +'lanmamıştı — doğru durum:
                                matris satırlı 75 filmden 33 ✅ + 42 ❌ = 75,
                                +1 THE HEAVY SIDE (matris satırı sahibinde) =
                                76, betikle tutar · %59 — 28.08: YERÇEKİMİ
                                eklendi, 42→43
                                (30 + 43 = 73) · 17.08: THE UPHILL DARK ve
                                THE BLUE DRIFT eklendi · 20.08: LOSS OF
                                LIFT eklendi · 22.08: THE BORROWED WEIGHT
                                ve THE SHORT WAY DOWN eklendi · 23.08:
                                THE LAST SPAN ve THE STRAIGHT LINE
                                eklendi · 24.08: THE IRON SLOPE eklendi ·
                                27.08: THE SKYLIGHT ve THE THIN ROOF eklendi ·
                                25.08: THE IRON SLOPE ÇIKTI — üretildi ve
                                ölçüldü, 39→38 · 25.08: THE ROSE COAT
                                eklendi (yazıldı, üretilmedi), 38→39 ·
                                30 + 39 = 69)

⭐ 23.08.2026 · SAYAÇ BETİĞİ İKİ YERDEN DÜZELTİLDİ (sayac.sh):
   ① `yatay_2_4_dk_filmler_zombi/` klasör listesine eklendi — 12.08'de
      silinmişti, kart H ile geri açıldı (65 → 66, THE LAST SPAN)
   ② `*_QA_SPEC.md` sayımdan DÜŞÜLDÜ — D117'den beri tek dosyalı
      formatlarda filmin yanında bir SPEC dosyası duruyor ve o bir
      film değildir (klasörlü formatlarda SPEC zaten film klasörünün
      içinde ve sayıma girmiyordu). Bu düzeltme olmadan zombi klasörü
      2 film sayıyordu.

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
                                · 120-122 The Borrowed Weight 🆕 24.08 —
                                dört merceğin İLK koşusu; üçü de ÖLÇME ALETİ
                                dersi: kart eşiği süreye bağlıydı (120) ·
                                şerit/replik Δ eğrisi kurguyu master açmadan
                                kuruyor (121) · kapının referans sayısı elle
                                yazılmıştı (122)
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
>
> 🔬 **DERİN TARAMA (24.08.2026): ⑤ ARKA PLAN · ⑥ FİZİK bu matrise
> GİRMEZ.** Risk tetikli koşulurlar, skorları `T5_ARKA_PLAN_KALITE.md` /
> `T6_FIZIK_KALITE.md` tablolarında ayrı durur ve T1-T4 ile
> karşılaştırılmaz. Payda /4 kalır — 6→4 kararı geri alınmadı.
> Ne zaman koşulacağı: `../QA_PROMPTLARI/00_README.md` derin tarama
> bölümü · görev kartları AGENTS.md F / F2.

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
| **The Upward Fall** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 02.09 · yatay 3-5 dk · **kalın atmosfer (3,2 atm · 0,42 g) dev orman gezegeni** · 25 sahne / 50 prompt / 4:09 · 0 replik · 0 kesme · 25/25 lockoff · novum FİZİKSEL YASA (ölen doku 0,6 m/s ile yukarı gider — Arşimet, anti-gravite değil) · TEMA FEDAKÂRLIK · risk 6/13 · ⭐ KART 2 yapısal çözüm: kanopi hayvanı YÜRÜMEZ, tek eksende hareket eder; 4 sahnede görünür, tam gövde hiç görünmez, temas 0 kare · ✅ prompt_kontrol.py klasör modu 0 BLOCK · GO · SPEC AYRI DOSYADA + `QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/` paketi ÜRETİLDİ [D165] → **MOD D koşulacak** · ⏳ üretim yok · 🔧 **REVİZYON 1 (02.09.2026 · sahip talebi: "modern donanımlı siyah astronot kıyafeti, kullanmasa da kılıfında silahı bulunsun"):** giysi mat zeytin-griden **MODERN MAT SİYAHA** çevrildi (sert siyah gövde kabuğu · grafit ribli uzuvlar · grafit diz/dirsek plakaları) ve sağ uyluğa **kapalı sert kılıf** eklendi. ⭐ İKİ YENİ RİSK, İKİSİ DE KİLİTLİ: ① **POLİTİKA** — `weapon`/`gun` prompt_kontrol'ün **T1** sözlüğündedir ("meşru kullanımı yok", red defterinde 40 geçiş), bu yüzden POLİTİKA §2'nin kuralı birebir uygulandı: **nesne ADLANDIRILMADI, formu tarif edildi** [D67] — *"a hard black case rides flat on the right thigh, flap fastened shut, a short ribbed grip standing out of it"*; `weapon/gun/pistol/sidearm/holster` 50 promptun 50'sinde **0 geçiş**, ve yasak cümlesi de yazılmadı ("never drawn/aimed" = D123 tuzağı) — karşılığı POZİTİF kilit *"the case stays fastened and flat; his hands stay on his work"*; kılıf **25/25 sahnede KAPALI**, çıkarılan/doğrultulan 0 kare, anlam maliyeti tablosuna 3 yeni satır girdi. ② **KOYU-ÜSTÜNE-KOYU** (kartlarda olmayan risk; Blind Berth'in "iki siyah gövde"sinin bu filmdeki hâli): ayrım RENK değil MALZEME — mat gövde kabuğu ↔ grafit yarı-parlak uzuvlar, ve zemin SOLUK GRİ olduğu için figür koyu/arka plan açık; 8 sahnede siluet cümlesi + **QA_SPEC E bloğu KAPI ⑦** (signalstats YMAX−YMIN ≥ 110, ffmpeg 8.1 ile doğrulandı). ⭐ Siyah KASK yüzü karartıyordu → **kask içi halka ışığı** Character Bible'a girdi ve tek cümlede üç kapıyı besledi: D79 devamlılık · ⭐VİRAL §2.4 yüz kanalı · POLİTİKA §3 imza ⑥ (yüzü kapatan ekipman = anonimlik imzası; okunur yüz red riskini düşürür). ⭐ **ÇEHOV BORCU ödendi** [UZAY_SENARYO §6]: silah hiç kullanılmıyor ama S19 · 6,0 s'de adamın eli bir an kılıfa DEĞİP kaba dönüyor — kullanmamak bir SEÇİM olarak ekranda; doruğu S22'de kesici alet taşıyor. ✅ Revizyon sonrası klasör modu yeniden koşuldu: **0 BLOCK · GO**, ⑯ politika sözlüğü T1 temiz; yeni bloklar promptları uzatınca (image 4.146'ya çıkmıştı) WORLD/NEGATIVE sadeleştirildi → image 2.496-3.913 · video 2.266-2.772 | · 🔴 **04.09.2026 · SEKİZ MERCEK KOŞULDU — SEKİZİ DE MOD V → MATRİS 0/4 KALDI.** SPEC **VE** mod-D paketi (`FILME_OZEL/THE_UPWARD_FALL/PAKET_1..8`) İKİSİ DE VARDI; operatör yine çıplak rubriği yapıştırdı → **[D165] 2. vaka, arıza yer değiştirdi: "paket yok" değil "paket var, rubrik açılıyor"**; SPEC yazılıyken mod V koşulan film sayısı **12** [D129]. `rapor_kontrol.py`: 🚨 1 GEÇERSİZ (⑦ AKSİYON — iddia n=7 Σ=66, hücreler n=8 Σ=76: **fabrike aritmetik** [D161]) · ⛔ 4 TEKRAR · ⚠️ 2 ŞARTLI · ✅ 1 GO; 4 raporda SEVERITY TALLY ≠ yazılı etiket, ①'de 4 hücre "no in-scope source"+sayı → `—` [D131] (5,8 → 4,8). ⭐ **⑪ ÖLÇÜM KAPISI KOŞULDU** (master: `~/Downloads/the upward fall (1).mp4` · 225,11 s · 3840x2160 · 30 fps · AAC 48 kHz) ve partiyi ölçüm taşıdı: 🔴 **ÜÇ TESLİM KUSURU** — ① üretici filigranı (cyan "▷" sağ alt çeyrek, **7/7 örnek · 225/225 saniye**) **sekiz merceğin sekizinde bulgu 0**, ⑤ 20 sahneye `EDGES: Clean` yazdı → [D150] **3. vaka, ⛔ ÇALIŞMIYOR** · ② kuyrukta 220,13-225,11 arası **başlık kartı** — üstelik KAPAK görseli (kahverengi ceket + baloncuk kask), filmin mat siyah kostümüyle çelişiyor [D70/D72 **10. vaka**] · ③ **−16,1 LUFS / peak 0,0 dBFS** (kilit −14 / −1,0). 🔴 **SES VAR, SEKİZ MERCEK "nothing audible to me" DEDİ** — silencedetect tek aralık bulmadı [D137 **5. vaka**]; ③ hiçbir kategoriye sayı koymadı → ses ekseni ÖLÇÜLMEDİ. 🔴 **④ KURGU KAPISI ÖN KOŞU: 22 sahne × 10,0 s = 220 s (+5 s kart) ≠ planın 25 sahne / 249 s'i — 3 sahne eksik ve biri S24: DORUK + KAPANIŞ + TWIST + KAPAK KARESİ.** 211-219 s kareleri çıkarıldı ve BAKILDI: son sahne ince çamlıkta yere oturmuş adam + arkada park etmiş araç; köprü yok, dört uzuv yok, avuçtaki parça aşağı basmıyor → **FİNAL VURUŞ KANITI BULUNAMADI** [D141] ve **DÖNGÜ KIRIK** (ilk kare 40 m'lik gövdeler + kahverengi lif zemin ↔ son kare ince çam + kül zemin). ÜRETİM SIRASI plana **yazılmıştı** ("1. DORUK S24") ve yine teslim edilmedi → [D168] 2. vaka: liste PLANI bağlıyor, TESLİMİ bağlamıyor. ⑤ ÇAPRAZ: kesme ekseni 8/8 doğrulandı (21); sahne ekseninde **ölçüm azınlığı doğruladı** (22 — ② ⑧ ①), çoğunluk (21) yanıldı → [D173]'ün tersi vaka. ② kilit çelişkisi defteri **11 madde · 9'u KAREYLE KAPANDI (FİLM SAPTI) · 2'si ⬜ AÇIK** → ⑩'da düşen bulgular: "knife appears with no source" (planda YAZILI tool) · "TWO GRAVITIES" (iki hız SPEC'te kilit) · "ash/snow biome" (promptun kendi çelişkisi, aşağıda). ⭐ **BU KOŞUNUN ÜRÜNÜ ÜÇ DERS + BİR ADAY, üçü de KAREDEN/ÖLÇÜMDEN çıktı: D175** (mührü [D169]'un kendi ÖNKOL cümlesi deldi — `the forearm tendons stand out through the glove` **çıplak deri** ürettirdi, 195-198 s dört karede; çıplak-deri yasağı yalnız `above the collar` yazıyordu → üç bölgeli negatif + mühür kapısı) **· D176** (SPEC'in KAPI ⑦ KONTRAST önlemi promptun LIGHT bloğuna `the pale grey floor` yazdı, WORLD bloğu `deep dry mat of fallen fibre` diyordu → model ilk yarıda birine, ikinci yarıda ötekine sadık kaldı ve üç mercek bunu "biyom sıçraması" sanıp S20/S21'i kesmeyi önerdi — **kalite kapısının kendisi devamlılık kusuru üretti**) **· D177** ([D162] SUSKUNLUK kapısı **sıfır iddiada ateşlenmez**: sekizi birden susunca kapının sorusu yok → `rapor_kontrol.py`'ye `--olcum-filigran` / `--olcum-lufs` bayrakları, ve `olcum_kapisi.sh` çıktısı ①.5'in ÖNKOŞULU) **· ADAY-8** (WORLD bloğu canlıyı bütün tarif edince tek-uzuv kadrajı iki BACAK üretti, 186 s — `UZAYLI_VARLIK_TASARIM_KILAVUZU` §5'e kural olarak indi, ders için 3 vaka bekleniyor). ⛔ **KESME LİSTESİ / REMOVE REÇETESİ / YENİDEN ÜRETİM SİPARİŞİ UYGULANMADI** [D129]. Sıradaki iş: master **filigransız + kartsız + −14 LUFS** yeniden ihraç · S24 (ve S17/S18) üretimi · sonra sekiz mercek **MOD D** yeniden koşulur. Film kaydı: `01_FILM_RAPORLARI/THE_UPWARD_FALL.md` · ham raporlar: `02_HAM_RAPORLAR/THE_UPWARD_FALL_*_HAM.md` (8 dosya)
| **The White Flood** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 04.09 · yatay 3-5 dk · 🆕 **İNCE ATMOSFER + SOĞUK HAVA GÖLÜ** (§3.2 türevi · 11 kPa · 0,62 g · azot) — kar gezegeni, dağ dünyası · **30 sahne / 60 prompt / 4:59** (sahne sayısı sahibin açık izniyle 25→30; 40 yazılmadı çünkü 6:39 eder ve 3-5 dk bandının DIŞINA çıkar) · novum FİZİKSEL YASA (soğuk AŞAĞIDA durur ve 2,0 cm/s yükselir — sıcaklık tersinmesi, Antarktika Dome A −98 °C ölçümüyle temellendirildi) · TEMA **KİMLİK** (S9·S18·S26·S29) · risk **7/13** · ⭐ **DEPONUN İLK ÇOK REPLİKLİ FİLMİ: 16 replik** (HUMAN 14 / MACHINE 2) — ⚠️ *düzeltme 04.09: replikli İLK film THE HEALING GROUND (4 replik, aynı gün, daha erken); bu film 16 replik + iki insanla ilk* — diyalog merdiveni BASAMAK 1-2, **konuşan ağzın okunduğu kare 0**; BASAMAK 3 kullanılmadı (PROB B koşulmadı) → replik olan film 0/81 sayısı 1 oluyor [06 §4b] · ⭐ **İKİ İNSAN TASARIM**: HUMAN COUNT LOCK **tam 2 × 30/30**, ayrım dört eksende (kırmızı şerit SAĞ ↔ elektrik mavisi SOL · boy · kişisel eşya) [ASTRONOT_DONANIM §2] · **AYRILIK S8** (B5b — uzatılan halat ALINMAZ; kanal temas reddi + yön) · ⭐ KART 2 yapısal çözüm: varlık YÜRÜMEZ, kökü kayadadır, yer değiştirme 0 m; 8 sahnede görünür, **4'ü buzun içinde DONMUŞ ve HAREKETSİZ**, temas 0 kare · KART 1 (sıvı) ve KART 6 (zerre) TASARIMLA sıfıra indirildi: kar YAĞMAZ, kırağı yerinde büyür, sıvı 0 sahne · ✅ **prompt_kontrol.py klasör modu 0 BLOCK · GO** (60 prompt; ⑯ politika sözlüğü **T1 0 · T2 0**) · üç bilinçli sapma yazılı (video uzunluğu 19 prompt bant üstü · image 30/30 · dosya başına kurulum 9) · SPEC AYRI DOSYADA + `QA_PROMPTLARI/FILME_OZEL/THE_WHITE_FLOOD/` paketi ÜRETİLDİ [D165] → **MOD D koşulacak** · ⏳ üretim yok · üretim sırası [D168]: S28 → S26 → S29 → S0 → S1·S7·S11 → kalanı |
| **The Open Circuit** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 07.09 · yatay 3-5 dk · **MARS GECESİ + BÖLGESEL TOZ CEPHESİ** (§3.2 · 610 Pa · 0,379 g) + §3.10 türevi basınçlı iç hacim · **25 sahne / 50 prompt / 4:09** · ⭐ novum FİZİKSEL YASA: **Mars fırtınası İTMEZ, YÜKLER** — depo bu fiziği iki filmde ölçmüştü, bu film onu novum'a çevirdi · patlamalar BASINÇ OLAYI ve **hava sesi taşımadığı için SESSİZ** (deponun ilki) · beş elektriksel olay · ⭐ **deponun en çok replikli filmi: 22 replik / 14 sahne** (HUMAN 16 / MACHINE 6) — ekranda okunan konuşan ağız **0 kare** · TEMA **UMUT** (S4·S16·S19·S24) · **AYRILIK S11 → S17'de TERSİNİR** · BEDEL S19 (canlı hat kesilir, son iki şerit aynı karede söner) · DORUK S22 (kıvılcım ilk kez AŞAĞI, toprağa) · risk **8/13** — beş kart TASARIMLA sıfırlandı (su · canlı · **ekran/sayaç/metin** · **insansız sahne** · değişken süre) · KURULUM İSKELETİ yazılı: dönüş %40 · küme 2 · şok 1 · ✅ prompt_kontrol.py klasör modu **0 BLOCK · GO** (koşuda 9 bulgu yakalanıp düzeltildi) · 📦 REFERANS PAKETİ 4 sayfa / 18 panel, dosya modu GO, ⬜ dört sayfa ONAY bekliyor (KAPI 0) · 🎵 MUZIK ✅ (HARD MUTE 193,0-195,0 [D180]) · 📣 YAYIN_PAKETI ✅ · 🧪 SPEC ayrı dosyada [D117] + E bloğu 4 makine kapısı **ffmpeg 8.1 ile fiilen kuru koşuldu** [D142]; `vidstabdetect` KURULU DEĞİL → kapı yazılmadı, ikame kondu · QA paketi ÜRETİLDİ [D165] → **MOD D koşulacak** · ⭐ **ÜRETİM KAPILARI D144 BİÇİMİNDE YAZILDI — 7 kapı, dördü de alanlı (KABUL / RET / YABANCI GÖZ / SONUÇ), SONUÇ ⬜×7** ve her KABUL satırı promptta FİİLEN VAR OLAN bir cümleye karşılık geliyor · **ÜRETİM KOŞU TABLOSU** (14 satır, operatörün eline geçen sıra) planda · ⛔ **KAPI 1 = S22 İPTAL KAPISI**: kıvılcım kayıştan aşağı inmiyorsa film ÜRETİLMEZ · 5-13 arası bitmeden dizi sırasına geçilmez (filmin SONU ve KURALI önce üretilir — SINKING STAKE'in durduğu yerin tersi) · 🔎 **07.09.2026 · TAM DENETİM (tüm kılavuzlar + 189 ders + red defteri) — SEKİZ BULGU DÜZELTİLDİ:** film hızlı yazılmıştı ve zorunlu okuma listesinin DÖRDÜ açılmamıştı (UZAY_USSU · SAHNE_ZINCIRI · ACILIS_KAPANIS · ASTRONOT_DONANIM). ① **optik aritmetiği hiç yapılmamış** — 5 kurulumun 5'i tutmuyordu; en ağırı F (85mm/14 m) dört modüllük ~64 m'lik üssü fiziksel olarak KADRAJA ALAMIYORDU (kadraj eni 5,9 m) ve '22° aşağı' 19 m kamera yüksekliği istiyordu → §5.2 formülüyle yeniden hesaplandı (F 24mm/47 m · C 1,4 m · H 2,8 m · B 4,4 m · G uzak figür 4,3 m) · ② **'fabric' 17× + 'cloth' 24×** — kılavuzun açıkça yasakladığı kelimeler [D59·D153]; model onları kumaş sanıp DALGALANDIRIR ve bu filmin fizik imzası 'hiçbir şey kıpırdamaz'dı → 'woven webbing band' · ③ **gece + renk çapası**: 20/25 sahne gece ve ayrımın TAMAMI renkti, üstelik iki SICAK renk (turuncu+sarı) → ASTRONOT_DONANIM §2'nin ikilisine çekildi (turuncu SAĞ + elektrik mavisi SOL) ve her iki-figürlü prompta **SİLUET ÇAPASI** cümlesi girdi; RA sayfasına gri tonlama kabul sınavı eklendi (`hue=s=0`, ffmpeg ile kuru koşuldu [D142]) · ④ UZAY_USSU §6 **[YÜZEY ÜSSÜ · MARS] negatif bloğu hiç yoktu** (0 geçiş) — en pahalı eksik satır **maket/tilt-shift okuması**, dört yapı planı olan bir filmde · ⑤ **AÇILIŞ-KAPANIŞ ÇİFT KARTI yoktu** ve plan 'LOOP' diyordu; 3-5 dk bandı KAFİYE bandıdır → kart yazıldı, çift S0↔S22 (tek değişken: kıvılcımın YÖNÜ, foveal merkez), S23-S24 koda olarak gerekçelendi · ⑥ **SAHNE_ZINCIRI'nin 9 maddesinin 9'u eksikti** → 24 sınırın 24'ü için açık soru + soru tipi + cevap tipi + sınır satırı yazıldı (ardışık aynı cevap tipi 0 · düz cevap 3/24 = %12,5 · ⓒ erteleme tek sınırda, ödemesi 2 sınır sonra kadrajda) · ⑦ **klip içi durum değişimi** — ölçülmüş EN ZAYIF eksende (T2V-CompBench 0,0687) dokuz klip vardı; üçü SINIRA taşındı, kalan dördüne **ARA DURUM YASAĞI** yazıldı ve depo içi çelişki (D157/D179 ↔ SAHNE_ZINCIRI §1) açıkça kaydedildi · ⑧ **S18 okunurluk**: düğüm kapağı 47 m'de ~60 pikseldi [D179'un tam arızası] → **yeni kurulum D (35mm · 12 m · üst açı 9°)**, kapak ~104 px. ✅ Denetim sonrası prompt_kontrol klasör modu yine **0 BLOCK · GO** (50 prompt) ve referans paketi de GO. Denetimi GEÇENLER ve kapanmayan dört borç PLAN §DENETİM KAYDI'nda. · ⏳ üretim yok |
| **The Healing Ground** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 04.09 · yatay 2-4 dk · 🆕 **KRİYOJENİK ORTA BASINÇ (§3.9 — kart bu filmle açıldı)**: 95 K · 0,90 bar N₂+CH₄ · 0,38 g · güneş diski 0 kare · zemin CANLI bir örtü · sıvı 0 kare · 14 sahne / 28 prompt / 2:19 (9 s hook + 13 × 10 s) · 0 kesme · 14/14 lockoff · novum FİZİKSEL YASA (zemin sıcak olanın üstünü kapatır; ortam sıcaklığındaki nesneye dokunmaz — kural 4 sahnede, 3 nesnede kanıtlanıyor, biri TERS kanıt) · TEMA **İLK-TEMAS** · CENTRAL CHOICE S11 (ısıtıcıyı kapatır; bedel AYNI karede: vent tüyü söner) · DORUK S12 · risk **6/13** (malzeme 5 + KART 12) · ⭐ **DEPONUN İLK GÖRÜNEN UZAYLISI** — `UZAYLI_VARLIK_TASARIM_KILAVUZU`'nun ilk uygulaması: VARLIK ŞERİDİ `10102133310244`, tam anatomi 2 sahnede, temas 1 karede, orbit yasağı korunuyor · ⭐ **4 REPLİK** — depoda replikli film 0/79'du; dördü de KADRAJ DIŞI TEK YÖNLÜ KAYIT (KART 7 merdiveni basamak 2), ekranda konuşan ağız 0 kare, sayı söyleyen replik 0 [D82], replik zamanları ızgara formülüyle doğrulandı [D122] · ⭐ KART 5 bilinçli KAPATILDI: gösterge/ekran/kadran 0 kare, sayaç ÇEVRESEL (vent tüyü 40 cm → 0, monotonik) · ✅ `prompt_kontrol.py` klasör modu **0 BLOCK · 0 FIX · GO** · SPEC AYRI DOSYADA + `QA_PROMPTLARI/FILME_OZEL/THE_HEALING_GROUND/` PAKET_1..8 ÜRETİLDİ [D165] → **MOD D koşulacak** · ⭐ **04.09.2026 — FİLM ÜRETİLDİ, KURGULANDI, ÖLÇÜLDÜ.** master `the healıng ground.mp4` 145,09 s (ikizi 4K, aynı süre) · gövde 140,00 s = 14 × 10,0 s · **yedi mercek koşuldu (③ SES yok), yedisi de MOD V** → `rapor_kontrol.py`: 🚨 1 GEÇERSİZ (②, aritmetik fabrike) · ⛔ 5 TEKRAR (①④⑥⑦⑧, D129) · ⚠️ 1 ŞARTLI (⑤ 9,0) · **HİÇBİR SATIR HİÇBİR T TABLOSUNA GİRMEDİ** [D129 + D150] · **SPEC + PAKET varken mod V koşulan film: 13** (THE UPWARD FALL ile AYNI GÜN, arka arkaya) · 🔴 **ÜÇ TESLİM KUSURU, THE UPWARD FALL'ınkinin AYNISI:** filigran ✦ sağ altta 5/5 örnek [D150] · kuyrukta 4,99 s yanan başlık kartı (üstelik görseli filmin dünyası değil — turuncu gök + dev gezegen + siyah giysi) [D70/D72] · true peak −0,4 dBTP (kilit −1,0) · ⚠️ ızgara 9 s hook yerine **10 s** ihraç edildi → bütün replikler +1 s kaydı · 🔴 **DORUK TESLİM EDİLMEDİ:** S12'nin 2 s MUTLAK SESSİZLİĞİ yok — ses profili 125-128 s'de −20,4 dB (filmin SESLİ seviyesi), gerçek sessizlik doruktan 5 s SONRA (130-141 s, −27…−35 dB) · 🔴 **BEDEL SAHNESİ ÜRETİLMEDİ:** S11'in İMAJ promptu video promptunun 10. saniyesini tarif ediyor (imaj "no vapour plume at his hip, cover standing open" ↔ video "0.0s — a plume stands at his hip"); I2V'de imaj t=0'dır, model söndüremeyeceği tüyü DİSKE koyup onu söndürdü — göğüs kapağı hiç açılmadı, anahtar hiç görünmedi (kare 111 ↔ 119) · 🔴 kuyruk kartı **DÖNGÜ KANITINI öldürdü** (S0 ↔ S13 eş kadraj çifti kartın arkasında) · 🟠 S4'te **kopuk eldiven**: prompt "the glove rests open on the floor" dedi, model kolu düşürdü → tek insanlı filmde ikinci mürettebat gibi okunuyor · ⭐ **⑤ ÇAPRAZ KAPI — replik ekseni ikiye bölündü:** ①②⑧ aynı üç repliği aynı zaman kodlarıyla yazdı, ⑥⑦④ "nothing audible to me" dedi; ölçüm ①②⑧'i doğruladı (ses kanalı VAR, üç zaman kodunun üçü de ses bandında tepe) → ④'ün "silent film → Diyalog N/A" hücresi ölçüm değil SAĞIRLIK · ⭐ **⑥ ve ⑦ hiçbir şey ölçmeden tam not verdi:** D131 uygulanınca ikisinde de TEK HÜCRE KALMADI (⑦'nin 10,0'ı deponun en yüksek mercek skoruydu) · ⭐ **④ HİKAYE 3,0/10 — sayı düşer, TEŞHİS DÜŞMEZ:** "no thematic cost is paid" + "no peak located" + "ends by stopping" üçü de ⑩ ÖNERME KAPISINDAN GEÇTİ; üçü de yukarıdaki üç teslim/üretim kusurunun tarifi. Buna karşılık ④'ün KESME LİSTESİNİN ÜÇ SAHNESİNİN ÜÇÜ DE SPEC'te ⛔ KESİLEMEZ yazıyor (S7 ⚡İRONİ · S8 ⭐VİRAL#1 · S10 ⭐VİRAL#2) ve çubuk bulgusu filmin TOHUMUNU kesiyordu → hepsi ⑩'dan DÜŞTÜ. ⛔ **KESME LİSTESİ / REMOVE REÇETESİ / YENİDEN ÜRETİM SİPARİŞİ UYGULANMADI** [D129]. **DERSLER (Kart G koşuldu):** **D179** imaj promptu değişimin SONRASINI yazmaz — I2V'de imaj t=0'dır; kapı `prompt_kontrol.py` ⑳b DEĞİŞİM KAPISI + bedel taşıyıcısı kadrajın kısa kenarının ≥1/8'i (06_METIN_VE_PROMPT_DILI) · **D180** planlı sessizlik KURGUDA hard mute ile kesilir, video modelinden istenmez — **TEKRAR 1**, THE UPWARD FALL ile iki vaka; ③ SES rubriği §9'a "A DECLARED SILENCE IS A DELIVERY ITEM" bloğuyla yamandı (07_KURGU_VE_ANLATI) · **ADAY-9** kolu yazılmayan eldiven KOPUK doğar (vaka 1, ders için ≥2 bekleniyor) · tekrar sayaçları: D129 12→**13** · D150 3→**4** · D70/D72 10→**11**. Sıradaki iş: master **filigransız + kartsız + −1,0 dBTP + S12 hard mute** yeniden ihraç · S11 ve S4 yeniden üretim · sonra sekiz mercek **MOD D**. Film kaydı: `01_FILM_RAPORLARI/THE_HEALING_GROUND.md` · ham raporlar: `02_HAM_RAPORLAR/THE_HEALING_GROUND_*_HAM.md` (7 dosya) |
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
| **The Slow Light** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 15.08 · 2-4 dk · ince atm. (🆕 YILDIZINA KİLİTLİ GEZEGEN — sabit alacakaranlık, zaman akmıyor) · **depoda novum'u ÇALIŞAN BİR CİHAZ olan ilk film**: 600 karanlık röle direği arasında altı yıldır yanıp sönen tek verici; sinyal 12 ışık yılı gidecek, şu an yolun yarısında · 16 × 10 s = 2:40, 0 kesme, 16/16 sabit lockoff, 3 viral ara (S1·S6·S15), tamamen sessiz · ⚠️ risk 4/9 (kask · ikinci figür · sayaç · toz); iki 🔴 kart (su·canlı) SIFIR — gezegen kuru ve ovayı boşaltan güç 0 kare · ⭐ **dış film analizinden tema devri**: `kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı) (66 rapor) — ulaşmayan mesaj ironisi, çizgi halinde alan görünmez güç; devralınan 11 ders §0.19'da satır satır işaretli · üç sayaç metinsiz (⭐ NABIZ ARALIĞI 3.0→9.0→3.0 s dramatik saat · ızgara yoğunluğu · güç hücresi) · doruk S11 = kendi güç hücresini ölülerin vericisine takmak, bedel AYNI karede (kask lambası söner) · üretim S11→S6→S9→S0 kapılarıyla başlar · ✅ prompt_kontrol.py: **0 BLOCK**, 32/42 prompt tavanın altında; tek FIX (uzunluk) gerekçesi §0.14b'de yazılı |
| **The Last Shift** | ⛔ön koşu Ⓥ5.0 | ✅ 5.0 ⚠️ | ❌ | ⛔ön koşu Ⓥ6.0 | **1/4** 🆕 16.08 · **+🧍 6.0 IDENTITY BREAK** — DÖRT mercek aynı gün, aynı 174 s kurgu (D75 ✅), ama 🔧/📖 **mod V** — SPEC §0.15'te hazırdı [**D94 ×6**] · ⛔ **deponun ilk SAHNE ≠ ÇEKİM ölçümü ve kurgu kapısının yeni delik yeri:** plan 14 sahne / **24 çekim / 27 klip / 190 s / ASL 7.9**, kurgu **17 × 10 s + 4 s kart = 174 s** → dört mercek de 14 segment saydı ve dördü de DOĞRU saydı; kapının 1. maddesi (klip = SCENE COUNT) 14=14 diye ✅ verdi → **DERS 101** · ~10 klip ekranda yok (**S5 İFŞA 1 — altmış bir çift bot, VİRAL** · S8 şaftlar · **S11'in dört çekimlik tek aksiyon ritmi**) çünkü 27 klip × 10 s = 270 s ham malzemenin 80 s'lik kırpma bütçesi hiçbir belgeye yazılmadı; kurgu kırpmak yerine klip düşürdü ve süre "tuttu" → **DERS 100** · 🔴 **2:50 yanık başlık kartı = D70/72 zincirinin 7. VAKASI** ve kartın alt satırı §5.3 KAPAK tipografisidir (düşen sahnenin bilgisi yazıya döndü) · 🔴 2:09 çıplak el–plaka kaynaşması (D11/D28, SPEC'ten bağımsız, AYAKTA) · ⛔ **BEŞ ÜRETİM KAPISININ BEŞİ DE KAYITSIZ** (BÖLÜM 4.1 tablosu boş, DURUM hâlâ "ÜRETİM BAŞLAMADI") ve raporların bulguları kapı 1-2-3-4'ün tam üstüne düştü → **D74 ×2**; tek tutan KAPI 5: **birleşik hold (20 s'lik S7) depoda ilk kez denendi ve TUTTU** · ⛔ kilit çelişkisi defteri **7 ⬜ AÇIK** [D96] · ✅ **D89 · D95 · D97 bu koşuda TUTTU** (mühür sayımı · mühürlü kask kanıtı · kanıt tabanı eşiği) · 🧩 Sayaç N/A ama planda üç sayaç var (D78 ×4) · yeni dersler: **100-103** |
| ~~**The Last Shift** (plan satırı)~~ | | | | | **0/4** 🆕 16.08 · 2-4 dk · 🆕 solunabilir ama SPORLU atmosfer, KAPALI HAVA (0.9 g / 0.8 atm; güneş diski ve sert gölge 0 kare) · ⭐ **deponun DIŞ FİLM ANALİZİNDEN HİKÂYE ve KAMERA GRAMERİ devralan ilk filmi** — `kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı) (66 rapor). Hollow Count aynı analizden yalnız YÖNTEMİ almıştı; bu dosya konuyu ve ölçülmüş kamera profilini alıyor, part-sahne eşlemesi §0.1b'de satır satır · ⛔ **SABİT 10 s SAHNE IZGARASI YOK:** 14 sahne · **24 çekim** · 27 klip · 190 s (3:10) · **ASL 7.9 s** (kaynak 9.0 · bant 5.76-21.7) · 10 kesme · 24/24 sabit kilitli kadraj · üç ritim modu §0.9b'de (A olay/kanıt 2 çekim · B yalnızlık tek çekim 10-20 s · C aksiyon YALNIZ S11: 4 çekim / 9 s / ASL 2.25) · ⭐ **ESİRGEME HARİTASI §0.9c** — sekiz zirvenin sekizinde kameranın NE VERMEDİĞİ yazılı (yakın plan · ters açı · tepki çekimi yok); rubriğe uyarı SPEC'te · ⭐ **birleşik hold** (iki klip = tek çekim, S7 20 s · S10 16 s · S13 18 s) depoda ilk kez · ölçek yayı 75mm ECU → 30 km EWS · **2 insan + 13 replik, hepsi gövdesiz makine** (8 kask AI + 5 çevirmen kutusu); iki figür de HİÇ konuşmaz, kadro kilidi üç kanalda (boy 1.66↔1.88 · suit rengi · bant tarafı) · ⭐ **insan sayısı bir SAYAÇTIR**: 2 → 1 → 0; ölüm 0 kare, ceset/kan/patlama 0 kare · toplu ölüm **61 çift botla** anlatılır · ⭐ **yaratık bütçesi**: 1 çekim · 3.0 s · tek uzuv · 300 m · gövde/baş/göz 0 kare (kaynak filmin A2 dersi) · ⚠️ **risk 6/9 — eşiğin ÜSTÜNDE** (canlı · kask · 2 insan · toz · katmanlı dünya · diyalog), gerekçesi §0.8'de ve **HAZIR DÜŞÜŞ planı §0.8b'de** (uzuv→gölge · S11 4→2 çekim · AI replikleri düşer; hiçbiri yeniden yazım gerektirmez) · üretim BEŞ kapıyla başlar (iki figür → parsel → uzuv → eşleştirme → birleşik hold) · 🧍 KARAKTER_QA bu filmde opsiyonel DEĞİL · ✅ prompt_kontrol.py: **0 BLOCK**, 51/51 prompt tavanın altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi §0.14b'de · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Hollow Count** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 15.08 · 2-4 dk · ince atm. (🆕 EVAPORİT TERASI / ÇÖKME HAVZASI, %4 basınç) · **novum gerçek jeoloji: yürünen zemin bir TAVANDIR** — çözünmüş tuz boşluğunun tavanı, kusursuz düz bir çizgi hâlinde, 20 saniyede bir 2 m levha vererek çöküyor (düşüş 14 m / 2.0 s, 0.7 g'de doğrulandı) · 14 × 10 s = 2:20, **16 segment · 2 kesme (yalnız S11)**, 14/14 sabit çerçeve, 5 viral ara (S0·S3·S5·S11·S13), tamamen sessiz (0 replik) · ⚠️ risk 4/9 (kask · ikinci figür · toz · katmanlı dünya); iki 🔴 kart (su·canlı) SIFIR ve **YAPAY IŞIK 0** (S13 jeti dışında) — Starless Circle'ın "model fazladan ışık icat ediyor" riski yapısal olarak elendi · ⭐ **dış film analizinin İKİNCİ saha denemesi** (`kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı), 66 rapor): devralınan 13 dersin hangi sahneye indiği §0.19'da satır satır yazılı — A1 sırttan ifşa (S8, 10 s hold, yüz 0 kare) · A3 toplu ölüm **60 boş diskle** (ceset/rakam 0) · B4 **eşleştirilmiş kadraj çifti S2↔S12** (aynı SETUP/CAMERA, tek değişken: her şey yok) · B5 **hız kartı S11** (deponun ilk kez SADECE tırmandırma için kullanılan kesmesi, filmin %79-86 aralığı) · B1 tersine çevrildi: uyarı GECİKMEDİ, kapı 90 saniyede kapandı — insanlar zaten aşağıdaydı · üç sayaç metinsiz (kazık sayısı 12→0 = dramatik saat · çizgi uzunluğu 40 m→9 km→iki havza · ayak izi hattı, dönüşte yok) · doruk S9 = tek atımlık kap iki yuvadan **vince** giriyor (kapı yuvası boş kalır); bedel S12 · final **çözüm değil GENİŞLEME** (çizgi ikinci havzaya girer) · ⛔ D69 ① kaydı planda: biniş/kalkış 0 kare · dört üretim kapısı + Plan B'leri §BÖLÜM 4'te · ✅ prompt_kontrol.py: **0 BLOCK**, 32/42 prompt tavanın (4.300) altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi ve ilk-red protokolü §0.14b'de · ⛔ SPEC bloğu dosyanın içinde (§0.15) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **Yerçekimi** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 28.08.2026 · yatay 10-20 dk (formatın İKİNCİ filmi) · vakum / alçak yörünge 410 km + F10 Dünya atm. zemin · 120 × 8 s = 16:00 · 3 perde × 10 faz (3-4-3) · kulvar SERT UZAY GERİLİMİ (novum yok, DURUM — UZAY_SENARYO §1 karar noktası bilinçli) · yapı kaynağı Gravity (2013) sökümü (`URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 2) · TEMA: FEDAKÂRLIK (S30 · S43 · S84 · S117) · iki karakter + feda S43 (5:36 = %35,0; gövdenin son karesi S45) — tür kartı sapması yazılı · kadro "2" 14/120 · **39 replik** (A 6 · B 16 · MACHINE 14 · KONTROL 2 · ÇOBAN 1 — sayının tek yeri README §REPLİK LİSTESİ), kasksız replik 0, ekranda ağız 0 · insansız 13 (İNSAN ŞERİDİ README §3) · su 0 · ateş 0 · canlı 0 (proje sahibi azaltımı) · risk 7/12 tetiklendi → çekirdek 5/12 tam eşik · doruk S94-96 rampası + S102 imza (yerçekimi yağmuru) · final KAPALI + held frame (bedel notu planda) · ⭐ **31.08.2026 DURUM — 120/120 SAHNE YAZILDI, 10/10 FAZ prompt_kontrol GO (0 BLOCK · 0 FIX), 240 prompt (120 imaj + 120 video)**; yazılan dosyalar: 00_PLAN + README + REFERANS_PAKETI + FAZ_01…FAZ_10 · ⛔ **AMA FİLM HAZIR DEĞİL — dört eksik:** ① D124 ölçüm kapısı açık (`00_PLAN.md` · `KLİP SÜRESİ = ____`, ffprobe ile dolmadan tek kare üretilmez) · ② **MUZIK_ALTERNATIFLERI.md ✅ 31.08** — beş alternatif (kayıtsız nabız / düşen hat / iki ses / doksan dakika / önce sessizlik), her biri §17 künyesi + iki blok İngilizce üretim promptu + kabul/ret kapısı; ⭐ **tarama bulgusu: filmin müziği tam ortasında ölüyor** — on faz dosyasının ses defterleri üst üste konunca S61-S96 = **36 ardışık müziksiz sahne (4:48)** çıktı ve başlangıcı S61 = 8:00 = orta nokta (hiçbir tek dosyada yazılı değildi); S2-S60 arası (58 sahne) müzik durumu ise hiç tanımlanmamıştı — alternatiflerin ayrıştığı yer orası · ⭐ `04_ARASTIRMA §TUR 2 ②`nin **sub-bass ↔ telefon hoparlörü** açık maddesi KAPANDI (kaynak çelişkisi 300-400 Hz ↔ 150 Hz → sıkı taraf seçildi + missing-fundamental yığını 100/150/200 Hz **taşıyıcı** seviyede, yedek değil) · ⚠️ F9'un "F7'nin sessizliğinden sonra ilk müzik" cümlesi yanlış çıktı (sessizlik F6/S61'de başlıyor) — düzeltme kaydı alternatifler dosyasında · MUZIK_VE_SES.md ❌ seçim bekliyor · ③ **KAPAK.md ✅ 31.08 yazıldı** (iki alternatif: A yüz-öncelikli lansman = S42 yüzü + S45 ölçeği · B = planın kendi S1 kapak anı, Plan B; ⭐ **tipografi ölçüsü kılavuzdan DEĞİL testten türetildi** — §4'ün atıfsız "60-80 punto"su 1280 px tuvalde 120 px posta pulu testini geçmiyor, versal 78 px geri hesaplandı; ⛔ emsal `THE_SECOND_SHIP/KAPAK.md`'nin "seamless visor"ı D146'yı çiğniyor, KOPYALANMADI; ⚠️ açık karar: kapaktaki isim — "GRAVITY" yapı kaynağıyla çakıştığı için elendi) · ④ **YERCEKIMI_QA_SPEC.md ❌ → [D117] gereği film "yazımı tamam" DEĞİL** · ayrıca REFERANS_PAKETI'nin 9 sayfa / 15 panelinin **0'ı üretildi** (seed kutuları boş, 7 sayısal kapı hiç koşulmadı) ve planın `SUREKLILIK_LEDGERI.md` satırı dosyasız duruyor (işlevi README incillerinde — ya yazılacak ya gerekçeyle silinecek [D74]) · matris bu yüzden **0/4** kalır: T1-T4 üretim sonrası ölçümlerdir, yazım GO'su onların yerine geçmez · ⭐ **31.08 ÜRETİM BAŞLADI (proje sahibi F1'i çekti)** → `FAZ_01_GOREV/FAZ_01_QA_PROMPT.md` yazıldı: faza özel rubrik (sahne tablosu S1-S12 · iki kimlik pasaportu · ayrışma kilidi orange/navy + sırt · vakum fiziği · ⭐ **INTENDED listesi** — emsalde bir koşu ayın VARLIĞINI kırmızı işaretleyip raporu yakmıştı, burada durmuş saat/gökteki çizgi/kimsenin bakmaması/süzülen cıvata önceden muaf yazıldı) · 12 skor kategorisi, vizör geometrisi AYRI kategori [D146] · ⭐⭐ **IZGARA SABİT YAZILMADI:** emsal Second Ship rubriği 10 s'yi varsayıyordu, bu rubrik STEP -1'de toplam ÷ 12 yaptırıp klip süresini ÖLÇTÜRÜYOR ve bütün zaman kodlarını o ölçümden türetiyor → **bu koşu D124 kapısının cevabını da üretir** · ⛔ faz koşuları T1-T4'e GİRMEZ | · 🔴 **04.09.2026 · YATAY FRAGMAN QA — PARTİ KONTAMİNE.** Operatör YEDİ rapor yapıştırdı; **BEŞİ (① ② ③ ⑦ ⑧) THE UPWARD FALL'ın raporuydu** (künyelerinde `FILM: the upward fall.mp4` · 226 s · 22 sahne), yalnız ⑤ ARKA PLAN ve ⑥ FİZİK gerçekten fragmana koşulmuştu (145 s · 14 sahne · 13 kesme). → ⑧ FRAGMAN MERCEK KAPISI [D111]: fragmanın ZORUNLU merceği **① KARE hiç koşmadı**; koşan iki mercek derin taramadır ve zaten matrise girmez. ⛔ **VE `rapor_kontrol.py` PARTİYİ AYAKTA TUTTU**: ⑪ hakemliği beş raporu "ölçümden sapan mercek" sayıp ⚠️ ŞARTLI verdi — 21↔13 kesme ve 22↔14 sahne bir sayım hatası değil KİMLİK hatasıdır → **[D178]** (⑤'e BÜYÜKLÜK TESTİ + MERCEK YOKLAMASI). ⭐ **⑪ ÖLÇÜM KAPISI KOŞULDU** (`~/Downloads/gravıty ıt holds one fragman (1).mp4` · 145,00 s · 3840x2160 · 30 fps · AAC): ✅ **filigran YOK** (dört köşe, 6 örnek — Upward Fall'ın tersi) · ✅ gövdede ekran metni 0,0 s · ✅ şerit `-1111111111111` planın KART 10'una (SAHNE 1 insansız) BİREBİR uydu — tek-figürlü filmlerin aksine burada şerit gerçekten ölçüyor. 🔴 Buna karşılık: klip **10,0 s** üretilmiş (plan sapma ② **8,0 s NATIVE**; D124 açık kapısı "ilk klibi ffprobe ile ölç" diyordu, koşulmadı) · §7 KIRPMA TABLOSU **hiç uygulanmamış** (gövde 140 s ≠ 100 s) · **BLOK A (APEXAIC girişi) YOK** · Blok Z'nin yerinde **"GRAVITY / IT HOLDS ONE" BAŞLIK KARTI** (plan sapma ③: "başlık kartı yok") → [D70/D72 **11. vaka**] · loudness −16,0 LUFS / −0,3 dBFS (kilit −14 / −1,0). 🔴 **VE PARTİNİN EN AĞIR KUSURU KAPSAM BOŞLUĞUNDAN ÇIKTI: 84 s'de ÜÇÜNCÜ ASTRONOT** — 81 s'de 2 figür, 84 s'de 3, 88 s'de yine 2; klip İÇİNDE doğan ve sönen bir duplike. Filmde insan 2, plan KART 4 "kadro 2" yazıyor. ⑤ ARKA PLAN bunu GÖRDÜ ve kendi `SUBJECTS EXCLUDED` satırına "Three tethered astronauts" diye yazdı — sonra kapsamı gereği DOĞRU davranıp özneyi puanlamadı; sahibi ① ve ② hiç koşmadı. ⑩'da düşen: ⑥'nın `TWO GRAVITIES` hükmü (PREMISE REGISTER `none` — yörünge ortamı kural sanıldı, [D166] 3. vaka); ayakta kalan tek fizik bulgusu L3 (vakumda yavaşlayıp duran parçacıklar). ② kilit defteri **6 madde · 4'ü KAREYLE KAPANDI · 2'si ⬜ AÇIK** (kask çapası · post replik katmanı). ⛔ Sıradaki iş: kartı kes + APEXAIC A/Z bloklarını koy + 84 s'yi yeniden üret; sonra **① KARE MOD D** koşulur. Kayıt: `01_FILM_RAPORLARI/YERCEKIMI_FRAGMAN.md` · ham: `02_HAM_RAPORLAR/YERCEKIMI_FRAGMAN_{ARKA_PLAN,FIZIK}_HAM.md` (yalnız 2 — beşi doğru filmin altında dosyalı)
| **The Skylight** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **29.08.2026 · ALTI MERCEK KOŞULDU, MATRİS YİNE DE 0/4** — SPEC dosyası klasörde HAZIRDI, altısına da verilmedi [D129 · 8. film]: koşuların tamamı ÖN KOŞU, hiçbir satır sayı taşımıyor. ⭐ **Ölçüm kapısı ⑪ İLK KEZ TAM KOŞULDU:** 315,155 s · 30 fps · ses VAR (AAC 253 kbit/s · −17,0 LUFS · tepe −0,0 dBTP — ihraç kilidi dışı) ama 6/6 mercek "nothing audible" dedi [D137 · 3. vaka] · kesme dedektörü karanlık filmde kör (1/33), ızgara ses deliklerinden okundu: **hook 10 s KIRPILMAMIŞ · 31 klip ≠ 33** (2 oda sahnesi eksik, aday S11+S14) · 5:10-5:15 **KAPAK tipografili kart** [D70/72 zinciri] · 🔴 **üretici filigranı 315/315 s, altı mercek görmedi** [D150] · kareyle doğrulanan: klon S13 (2:07) · toz şelalesi S3/S6 · kanyon S26 · alev/bacak S28 · üç kask · kir sıfırlanması · cıvata S31 · ✅ S20 sönüş EKRANDA (④ "no peak" = rapor) · ✅ S32 final ekranda · ⑥ g≈3,8 m/s² planı doğruladı · kilit defteri 21 madde: **15 kapalı / 6 ⬜** · film kaydı: [→](01_FILM_RAPORLARI/THE_SKYLIGHT.md) · **DERS 143 · 144 · 145 · 146 · 147 · 148 · 149 · 150** · sonraki tur: filigransız master → yeniden üretim (sahip onayı) → MOD D · ⛔ tamlık matrisi ❌ KALIR · — — — 🆕 27.08.2026 · 3-5 dk (⭐ 28.08: +PART_C AYRILIŞ → 33 sahne / 5:29, format sapması kayıtlı [D74]; çift kapanış S24/S32; kalkış fiziği sayıyla; 6 viral; SPEC güncellendi; kapak anı S30'a taşındı — ⚠️ PAKETLEME §1 sapması kayıtlı, S0 Plan B; 🎵 MUZIK ✅ 2 cue 48/120 BPM + 3 sessizlik penceresi, tek çözülme S32) · ince atm. (Mars 0.38 g · Arsia lav tüpü: 180 m çap / 60 m tavan / 40 m gök deliği) · yatay hattın ilk yeraltı filmi (⚠️ AYNI GÜN dikey hatta THE THIN ROOF bağımsız olarak aynı jeolojik olguyu seçti — çakışma kaydı iki film dosyasında, karar sahibin) · novum ÖLÇEK — fizik ihlali yok (fener 25 m ↛ duvar 90 m · taş 1,2 m → 0,8 s) · TEMA: ZAMAN — ışık sütunu odanın tek saati, S20 klip İÇİNDE söner (monotonik takvim) · 25 × 10 s = 4:09 · 0 kesme · 25/25 lockoff · TAM SESSİZ (replik 0 · MACHINE 0) · insansız 0 (İNSAN ŞERİDİ 25×1) · sayaçlar metinsiz: sütun eğimi · cairn 1→4 · rakamsız pusula (iğne durmaz — Mars gerçeği) · 4 viral S3·S13·S19·S20 + S0 eski kapak anı (→ Plan B 28.08) · eş kadraj S0↔S24 · S2↔S23 · S6↔S18 · risk 5/12 (eski ölçekle 3/9) · ✅ prompt_kontrol 2× GO / 0 BLOCK · ⛔ SPEC AYRI DOSYA (`THE_SKYLIGHT_QA_SPEC.md`) — **MOD D koşulacak, mod V ön koşudur [D94/D117]** · üretim kapıları: S0 → S3 (toz cümlesi) → S5 (karanlık pozlama) → S20 |
| **The Frost Line** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 29.08 · 3-5 dk · İnce atm. (🆕 **MARS SERA TÜNELİ** — Arcadia Planitia, 32 m şişirilebilir ETFE tünel, 3 bölüm, içi 30 kPa hipobarik: kask İÇERİDE de kapalı) · Bilimkurgu (hayatta kalma AKSİYONU / kimlik) · **YAZIM PAKETİ TAM: PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117]** — 25 sahne / 50 prompt (25/25 I2V) · sahip talebi: *daha aksiyonlu · yemek yetiştiren, uzun zamandır Mars'ta hayatta kalan adam · ultra gerçekçi* · novum GERÇEK FİZİK: kaçak KAR yağdırır, havasız kalan yaprak BEYAZLAR (dikiş×avuç S4 · dış yama 1 s'de uçar S5 / iç yama tutar S10 · yaprak klip içinde beyazlar S15·S19·S20) · TEMA: KİMLİK — depoda ilk ("Kazazede günleri sayar; bahçıvan sıraları.") · üç metinsiz sayaç (kar sütunu · tavan sarkması · yeşil sıra 9→6) · doruk S20 = kelepçe + zar şişer + son yeşil beyazlar + tavan gerilir aynı klipte · KAPAK ANI S0 · 0:07 (PAKETLEME §1 bandında) · final MUĞLAK + tohum · TAM SESSİZ · 25/25 lockoff · ⚠️ **risk 7/12 — eşiğin üstünde, kabul edilmiş maliyet** (buz/kırağı KATI, sıvı 0 kare); 5 üretim kapısı D144 biçiminde · SPEC E bloğu: 9 makine kapısı kuru koşuyla doğrulandı (ffmpeg 8.1) [D142] · ✅ prompt_kontrol 0 BLOCK, video 25/25 bandın içinde · 🏗️ 29.08: höyük → MODERN ÜS (4 modül + düğüm) + 120 m'de MODERN İNİŞ GEMİSİ, yalnız arka plan (S0·S2·S24), biniş 0 · 🎵 MUZIK ✅ 29.08 (CUE A 72 BPM S1-S12 · CUE B 120 BPM S13-S18 + kelepçe darbesi 3:24.0 + koda; 3 sessizlik) · ⛔ SPEC dosyada — **MOD D koşulacak**; mod V koşulursa satır YAZILMAZ [D129] · ⚡ **31.08.2026 · ÜRETİLDİ + ALTI MERCEK KOŞULDU (⑥ iki kez), ALTISI DA MOD V — SATIR YOK [D129 · 9. film].** Teslim 23 klip + 5,1 s KAPAK kartı = 235,2 s · **720p (!)** · 30 fps — plan 25 / 249 s: **S12 + S23 EKSİK** (tohum kutusunun Çehov kurulumu kayıp — S22 ödemesi kurulumsuz; iç geniş ayna hiç yok) · hook 9'a KIRPILMAMIŞ · sahip beyanı "1 eksik", ölçüm 2 diyor · ⑪ ölçüm: **ses VAR** (AAC 253 kbit/s · −21,5 LUFS · tepe −0,1 dBFS — ihraç kilidi dışı) ama 6/6 mercek "nothing audible" [D137 · 4. vaka]; ③'ün 4 🔴'lı "mutlak sessizlik" raporu ölçümle GEÇERSİZ; yatak 0-230 s kesintisiz [D83 ✓] · 🔴 üretici filigranı "▷" 235/235 s [D150 · 2. vaka — ① ve ⑤ bu kez GÖRDÜ: Thin Roof yamaları İŞLEDİ ✅] · ⭐ kareyle: **S5 yama uçuşu (t56) + S15/S19 klip içi beyazlama (t141→147 · t181→187) EKRANDA — mercekler görmedi/TERSİNE okudu** (④ S19'a "healthy leaf payoff" dedi, ⑤ plume'u "hata" sandı) → **D151** · ⛔ **S20 DORUK VURUŞU EKRANDA YOK** (çubuk 8 s havada, mühür/şişme/beyazlama yok — E7-b FAIL) · S24'te FIRÇA YOK, çökük film BRANDA nesnesi çıktı (E6 FAIL) → **D152/D153** · S6 erken TAM çöküş (bir karış sarkma yerine — raporların "dış çökük ↔ iç sağlam" 🔴'ının tek kaynağı) · sırt ünitesi yuva 13 [D139 · 2. vaka] · kırağı İKİ yönde dalgalı [D147 · 2. vaka] · vizör okunmaz [D95 · 2. vaka] · iki yerçekimi (kristal 11,1 ↔ adım 4,0 m/s²; adım planın 0,38 g'sini doğruladı) → **D154** · üretim kapıları YAZILIYDI, SONUÇ ⬜×5 — koşulmadan 23 klip üretildi [D144 · 2. vaka] · kilit defteri 18 madde: **13 kapalı / 5 ⬜** · film kaydı: [→](01_FILM_RAPORLARI/THE_FROST_LINE.md) · **DERS 151 · 152 · 153 · 154** · sonraki tur: S12/S23 üretimi + S20·S24·S6·S0 yeniden (kapı kayıtları doldurularak) + filigransız/kartsız/−14 LUFS/≥1440p master → MOD D · ⛔ tamlık matrisi ❌ KALIR · ⚡⚡ **01.09.2026 · İKİNCİ PARTİ — ALTI MERCEK YİNE MOD V, SATIR YİNE YOK [D129 · aynı filmde 2. kez].** Kurgu değişmedi (23 klip · 235,2 s); ihraçtan biri düzeldi: **4K (3840×2160) ihraç var** ✅ ama filigran · kart · −21,2 LUFS / tepe −0,1 DURUYOR [D150 · 3. vaka]. ⭐ ③ SES bu kez sesi **DUYDU** (AUDIO STATE B — 1. partinin "mutlak sessizlik"i düzeldi) ✅ · 🔴 **⑪ ölçüm bir KİMLİK arızası buldu: `~/Downloads`'ta "the frost lıne" adlı BEŞ dosyanın İKİSİ (245,120 s) THE PAYLOAD'un gövdesi + BU FİLMİN kapak kartı** → **D160** · 🔴 **dört mercek aynı YANLIŞ bulguyu birebir aynı cümleyle yazdı** ("3:23 parmak vizörden geçiyor" — kare t202/t203/t204: el vizörün ÖNÜNDE, füzyon YOK); yanlış 🔴 ①'in REGENERATE'ini taşıyordu → **D159** · kareyle KAPANAN iki yeni ihlal: plan S5'te de sırt harness'ı (t52/t57) [D139 · 3. vaka] · **plan S22'de tohum EKİLMEDEN önce yatakta çimlenmiş filiz sırası** (t217/t219 — SPEC "filiz 0 kare") [D156 · 2. vaka] · belgeyle açılan ihlal: iç sahnelerde **PEMBE LED yetiştirme şeridi** (SPEC "yapay lamba/LED 0 kare"; ⑤ envantere yazdı, bulgu yapamadı) · ③'ün duyduğu "high-altitude wind" SPEC'in "rüzgâr 0" kilidine aykırı · ④'ün kesme listesindeki 7 adayın 7'si yük taşıyor (ORTA NOKTA S10 · "MAY NOT BE CUT" viral S19 · karakterin tek tereddüdü S18) → UYGULANMADI [D129] · kilit defteri 2. parti: 25 madde, **18 kapalı / 6 ⬜ / 1 yarı** · **DERS 159 · 160** |
| **The Payload** | ⚠️Ⓥ | ⚠️Ⓥ | ⚠️Ⓥ | ⚠️Ⓥ | **0/4** 🚨 01.09 ÜRETİLDİ + ALTI MERCEK MOD V — hepsi ÖN KOŞU [D129, 8. film]: SPEC VARDI, VERİLMEDİ; T tablolarına satır YAZILMADI · ①4,5 ②6,0 ③8,4 ④3,4 ⑤6,2 ⑥5,5 (hiçbiri geçerli değil) · ⑪ ölçüm KOŞULAMADI (master operatörde) · ⭐ İNSAN ŞERİDİ planla BİREBİR (111111111111011101010010) ve 24 sahne tuttu — ama planın SIFIR kilitlerinin BEŞİ de düştü: replik 0→4 · ekran metni 0→başlık kartı + "PHASE 1" göğüste + "EVA" sırtta · klon 1:40 · kasa 9→8 · müziksiz pencere 3→0 · novum (amortisör bandı) hiçbir mercekte YOK, ④ taşıyıcı sahneleri kesme listesine yazdı · sahip: "hikayesi berbattı" ↔ ④ 3,4/10 · **DÖRT YENİ DERS: D155-D158** · D155 reçetesi prompt paketine uygulandı (PHASE/EVA temizliği, 0 BLOCK) · kayıt `01_FILM_RAPORLARI/THE_PAYLOAD.md` · yeniden üretim sırası kayıtta · (yazım paketi 31.08 · 3-5 dk · İnce atm. (🆕 **MARS TOZ FIRTINASI CEPHESİ** — 2 km yüksek, 40 km/s, kuvvet SIFIR) → vakum/0g (alçak Mars yörüngesi) · Bilimkurgu (ayrılış / insan-makine sınırı) · **YAZIM PAKETİ TAM: PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117]** — 24 sahne (12+12) / 48 prompt (24/24 I2V) / 239 s = 3:59 · sahip talebi: *Mars · 24 sahne · part 1 fırtına + hazırlık · part 2 kalkış + yıldızlararası gemiye kenetlenme* · novum GERÇEK FİZİK: **kütle bütçesi korunur** — tekne kişi değil kütle taşır (amortisörün parlak bandı: iki parmak → bir el → yine iki parmak) · TEMA: İNSAN-MAKİNE SINIRI — depoda ilk ("Makine kimi taşıdığını bilmez; yalnız ne kadar taşıdığını bilir.") · üç metinsiz sayaç (12 panel sırası söner · mastın 3 eşit adımı · amortisör bandı) · CENTRAL CHOICE S7-S10: dokuz yıllık numuneyi toza dizip yerine kendi bedenini koyar (LOW POWER'ın fedakârlık kalıbının tersi) · doruk S20 temas T+6.0, dış ses 0 · kenet S21 tam 4 kelepçe · insansız 6 sahne (KART 10 maliyeti kayıtlı) · TAM SESSİZ · risk 7/12 (eşiğin üstünde, gerekçeli) · ✅ prompt_kontrol 0 BLOCK / 0 FIX / 3 GO, video 24/24 bandın içinde · SPEC E bloğu: 11 makine kapısı ffmpeg 8.1 kuru koşusuyla doğrulandı [D142] · 🎵 **İKİ MÜZİK ✅ 31.08**: A-SKOR (anempatik sayım — 72 BPM'de sahne başına 12 vuruş, on ikincisi hiç çalınmaz; doruk 32.5 s müziksiz; tek çözülme 3:55.0 lomboz) + V2 VİRAL (120 BPM, 2:03.0 ateşleme düşüşü, 22 s doruk sessizliği, dikey kesit pencereleri) — kurguya TEK skor girer · ⛔ SPEC dosyada — **MOD D koşulacak**; mod V koşulursa satır YAZILMAZ [D129] · ⚡ **01.09.2026 · MASTER BULUNDU [D160]:** dosya `~/Downloads` içinde **THE FROST LINE adıyla** duruyordu (`the frost lıne .mp4` 720p + `the frost lıne  (1).mp4` 4K · ikisi de **245,120 s**) — bu yüzden ⑪ hiç koşulamamıştı. Kimlik kanıtı: göğüste basılı **"PHASE 1"** (D155'in kaynağı · kare t15) + kasaları toza dik dizen adam + 24 × 10 s ızgara. ✅ ÖLÇÜLDÜ: gövde 240,13 s (24 klip) + kart 4,99 s · ⛔ **hook 10 s — 9'a KIRPILMAMIŞ** · 🔴 **kuyruktaki kart BU FİLMİN DEĞİL: ekranda "THE FROST LINE" yazıyor** · yapılacak: dosyayı yeniden adlandır → kartı çıkar → hook kırp → ⑪'in kalanını koş |
| **The Borrowed Weight** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **24.08.2026 — DÖRT MERCEĞİN İLK KOŞUSU, PARTİ 🚨 GEÇERSİZ** (⑤ çapraz sayım: kesme 26/24/24/25, fark 2 · sahne 24 vs 11) — dört skor da YAZILMADI, hücreler ❌ KALDI. SPEC AYRI DOSYA olarak hazırdı, dördüne de verilmedi [**D94/D117 ×7**] · ⛔ kurgu kapısı 3/3 ihlal: 26 klip ≠ 25 · 264 s ≠ 249 ± 2 · insan şeridi tutmuyor. ⭐ **Partinin gerçek çıktısı skor değil KURGU ARİTMETİĞİ**: ① ve ②'nin insan şeritleri insansız yuvanın MUTLAK yerinde anlaştı (3:40-3:50, planda 3:09-3:19 → Δ +31 s ≈ +3 klip) → teslim kurgusu 26 yuva = **ilk perdede +3 fazla klip** (biri S2 klibinin kopyası: aynı replik 0:23 ve 0:33'te) + **kuyrukta −2 eksik sahne** + 4 s **yasaklı başlık kartı** (SCREEN TEXT 0.0 s kilidi) = 264 s ✓. ⛔ **En ağır ⬜ AÇIK madde: planın S24 TWIST finali (ova boşalmış) hiçbir raporda yok** — ④ finali "işini bitirir ve dinlenir" okudu ve düz duygu yayı yazdı; olmayan bir finali eleştirdi [D72/D62]. Tekrarlayan dersler: **D119** (② dört hücre "no in-scope source" + 7/10 → yazdığı 4.9, tablosu 6.0) · **D105/D65** (④ film adını yanan karttan okudu) · **D83** (ortam yatağı 4 klip sınırında ölü) · **D78** (iki metinsiz sayaç hiçbir mercekte okunmadı). Yeni dersler: **D120** kart eşiği · **D121** Δ eğrisi · **D122** planın replik çizelgesi (S2/S10 bir yuva geç yazılmıştı, DÜZELTİLDİ). Kayıt: `01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md` · 🆕 22.08 · 3-5 dk · ince atm. (adsız gri ova, %1.2 bar / 0.92 g, sürekli örtü — güneş diski 0 kare, gölgesizlik fizik) · 🆕 **depoda ilk novum-İNSANDA filmi**: yerden kesilen parça tüyleşir, ağırlığı taşıyana geçer ve GERİ VERİLMEZ — kural 6 sahnede 5 katı nesneyle kanıtlanır [ONERME §5]; tema fedakârlığın fiziği ("kalan her şey, ağırlığını birinin taşıdığı şeydir") · 25 × 10 s = 4:09 · 0 kesme · 25/25 lockoff · 4 viral ara (S5·S13·S19·S23) + S0 kapak anı · **TWIST + tohum** [FINAL 3-5 dk kuralı]: S1/S3 tohumları → S24'te ova BOŞ (hafifleyen her şey gece rüzgârının malı; kasa KENETLİ olduğu için kalır — içerik 0 kare, bilinçli muğlak) · sayaçlar metinsiz: İZ DERİNLİĞİ 2→23 cm monotonik · adım 9→5 (eş kadraj S6↔S18, tek değişken yük) · rakamsız kantar (ibre 2.→9.→dip, S16'da geride bırakılır) · cyan nabız 2 s (ölü ikiz kasa 0 nabız) · **4 replik, hepsi MACHINE** (S2·S10·S21·S22; sahibin şartı: AI sesi insana yapışmasın — dördü de AĞIZ-DIŞI kadraj + "he never speaks" gövde kilidi + düz sentetik register [D82]; HUMAN 0) · 23/23 kask kapalı, ara durum 0, giyme 0 · ⚠️ risk 5/9 TAM EŞİKTE (kask · ikinci figür · sayaç · toz · MACHINE diyalog); su · canlı · katman SIFIR · **çekirdek-kayma çakışması** çözümlü [D59 · LOSS hovering emsali]: statik yasağı iki özneye bölündü ("only the lightened pieces creep leeward, on the ground"), S1 üretim kapısı — geçmeden S13 üretilmez · lander YÖNELİM KİLİDİ (burun gömülü, kuyruk göğe, kapak yüzü sola) 25 sahnede sabit [uzamsal §5.1] · ✅ prompt_kontrol: PART_A 26 + PART_B 24 + KAPAK 2 prompt — **0 BLOCK**; FIX yalnız gerekçeli uzunluk (tavan 4300 aşımı 0), kayıt PART_A ⑨ / PART_B ⑧ · ⛔ SPEC ayrı DOSYA (THE_BORROWED_WEIGHT_QA_SPEC.md) — **MOD D koşulacak, mod V ön koşudur [D94/D117]** · üretim kapıları: S0 (paradoks+gri ayrışma) → S1 (kayma) → S5 (ölçek) → S20 (doruk) |
| **The Iron Slope** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **25.08.2026 · ÜRETİLDİ, ALTI MERCEK KOŞULDU, MATRİS YİNE DE 0/4** — altısı da mod V (SPEC dosyası depoda yoktu) ve kurgu kapısı ④(b) düştü (süre 65,0 s ≠ 48,0 ± 2): ölçülen şey filmin PLANA UYGUNLUĞU değil, kendisiyle tutarlılığıdır. ⭐ **Master ölçümü:** 6 × 10,005 s klip + 4,97 s başlık kartı · kesme ızgarası 10,03…60,03 · dosyada sessizlik YOK (🔊'ün 🔴 BLOCKER'ı uydurma) · S2'de YASAKLI GEZEGEN kadrajın alt üçte birinde (⑤ arka plan merceği görmedi) · göğüste yasaklı arma · S2'de kamera kayıyor (6/6 lockoff tutmadı) · ⛔ **serbest panel sabit ~0,15 m/s süzülüyor (kilit: 3. sn 9,7 m) → NOVUM EKRANA GELMEDİ**, 📖 bunu bağımsız olarak "THE ONE THING NOTHING ELSE DOES: none found" diye yazdı · film kaydı: [→](01_FILM_RAPORLARI/THE_IRON_SLOPE.md) · **DERS 124 · 125 · 126 · 127** · sonraki tur MOD D (SPEC 25.08'de yeniden yazıldı) · — — — 🆕 24.08 · dikey shorts · 🆕 vakum + itki yerçekimi (§3.5 kartının DİKEY hattaki ilk filmi — 0,220 g sürekli yanma, THE UPHILL DARK'ın doğrulanmış sayıları) · **novum ALGISAL ve tamamen gerçek fizik** (Quiet Impact emsalinin ikinci koşusu): "uzayda aşağı var — aşağısı motor"; kopan her parça kıça doğru 2,16 m/s² ile, ölü düz çizgide, hızlanarak düşer · 6 × 8 s = 48 s, 0 kesme, 0 replik, ekran metni 0,0 sn (kaplama işaretsiz — yasak KONSEPTLE kapalı) · **6/6 TAM LOCKOFF**, üç kurulum da gemiye kelepçeli (sarsıntısızlığın fiziksel gerekçesi) · devam zinciri: 2 perde + 3 J-köprülü sert kesme; her sahnenin I2V DEVAM sürümü var · sayaç metinsiz ÜÇ kanal: banttaki gevşek parça 3→0 · hava kilidi mesafesi 14→2 m · turuncu motor jantı (S0'da 0,4 s kararma = tohum) · ⭐ risk 4/12 — Kart 3·4·5·9; **Kart 6 TASARIMLA kapatıldı** (toz/duman/alev/kıvılcım/çarpma 0 kare; düşen her şey rijit tek parça) · gerçek risk kartlarda yok ve dosyada tanımlı: **tırmanan gövdenin eklemlenmesi** [D18 akrabası] + sıfır-g refleksi (D23 tersi — ortam kartı yapısal panzehir) · merkezi seçim S4 37,2-38,2: karabineri açar, korunmayı zamana takas eder; bedel aynı karede (şakül gibi asılı şerit + korumasız tırmanış) · doruk S5: 6 m latis 1,0 m yanından ~2 saniyede geçer, sonra **MOTOR SUSAR** — 2,2 s yanma arası: jant söner, botlar kalkar, şakül kıvrılır (twist = tohumun karşılığı); 46,6'da ikinci kademe ateşlenir, döngü kapanır (kinesik reset: S5 son jest = S0 ilk jest) · tema UMUT ("her şey düşerken tırmanmaya devam etmek") · üretim S0'dan başlar; panel orada çarpar/kavis çizer/süzülürse film üretilmez · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX** (ilk koşu 1 FIX: S4 video 2.712 → kısaltıldı); video 2.236-2.586 bandın içinde, image 5.023-5.651 emsal bandında · ⛔ **SPEC AYRI DOSYADA: `THE_IRON_SLOPE_QA_SPEC.md`** [D117] — MOD D koşulacak, mod V ön koşudur [D94] |
| **The Near Pass** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 25.08 · dikey shorts · 🆕 ince atmosferli kayalık gezegen yüzeyi (9 kPa · 0,62 g · saçılma yok, gölgeler dolgusuz) · **ÇOK YAKIN UYDU — kullanıcı talebi** · novum ALGISAL ve tamamen gerçek yörünge mekaniği (Quiet Impact / Iron Slope emsallerinin ÜÇÜNCÜSÜ): *"gün batmaz, KAPANIR"* — 52 km'lik tek parça kaya 150 km irtifada, 4.965 m/s, **batıdan doğuyor**, ufuktan ufuğa 8 dk 05 sn, günde 19 geçiş, görünen çap 2,63°→19,67° (başucunda Dünya'nın Ay'ından 37,8 kat geniş); yıldızdan 18 kat geniş olduğu için gündüz **1,2 s'de kapanıyor · 19,1 s kapalı · 0,94 s'de açılıyor** ve gölge **Mach 23,7** ile geldiği için **ışık kapanırken ses hiç değişmiyor** · **6 × 10 s = 60 s** — ⭐ **D124'ten sonra ızgarası ARAÇTAN yazılan ilk film** (klip süresi 10,005 s künyede, ölçüm komutu dosyada) · 0 kesme, 0 replik, ekran metni 0,0 sn (düzlükte insan yapımı tek nesne yok — yasak KONSEPTLE kapalı) · **6/6 TAM LOCKOFF**, üç kurulum da yere oturuyor; ölçek Z ekseninden (S2'de 8 m yürüyüş) · devam zinciri: 2 perde (perde = KARANLIĞIN kendisi) + 3 sert kesme · ⭐ **D127'nin ilk karşı tasarımı:** açısal hız HİÇ yazılmadı — tırmanış süre + piksel + KENDİ ENİ olarak yazıldı (her sahnede kendi eninin %34→%55'i, oran monoton büyüyor) + ikinci sabit cetvel gökyüzüne çivili yıldız (aralık 236→159→67→0 px); **S0 kapısı ffmpeg ile koşulur [D125]** — 0 ve 10. saniye karelerinde alt kenar farkı <100 px ise film ÜRETİLMEZ · sayaç metinsiz ÜÇ kanal: PALL'ın boyu/yüksekliği · yıldız aralığı · ışık seviyesi (ikili, tam iki geçiş) · risk **4/12** (Kart 3·4·5·9); **Kart 6 TASARIMLA kapatıldı** — toz/duman/enkaz/düşen cisim 0 kare (ilk taslaktaki toz filamenti çıkarıldı) · gerçek risk kartlarda yok ve dosyada tanımlı: **büyük gök cisminin ekranda hareket etmesi** [D127 tekrarı] + tutulmanın BULUT GÖLGESİ olarak üretilmesi · merkezi seçim S4 42,8-43,2: kask lambasını söndürür — bedel aynı karede (ışık dairesi ve 30 m'lik yarığın çizgisi birlikte söner) · ödül S4: uydu **BAKIR** yanar, kenarda parlak ortada koyu (ışık yalnız gölge bandının dışındaki gündüzden yalayarak geliyor) ve S0'ın tohumu — soluk çatlak ağı — derin yarıklara AÇILIR · doruk S5: ışık 0,94 s'de döner ve **kanıtı siler** · final DÖNGÜ + GERİ ALMA, kinesik reset (S5 son jest = S0 ilk jest) · lens 24mm + 75mm KÜRESEL — 32mm geometrik olarak çalışmıyor, hesabı dosyada · ⭐ **prompt_kontrol.py ilk koşuda ⛔ BLOCK:** 12 promptta dünya-uzayı yön kelimesi (pusula); hepsi ekran uzayına çevrildi → ikinci koşu **GO · 0 BLOCK / 0 FIX**, video 2.402-2.594 bandın içinde, image 5.486-5.857 (emsal bandının 188 karakter üstünde, gerekçesi dosyada) · ⛔ **SPEC AYRI DOSYADA: `THE_NEAR_PASS_QA_SPEC.md`** [D117] — filmle AYNI GÜN indi |
| **The Open Seam** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 26.08 · dikey shorts · 🆕 **OKYANUS DÜNYASI** (karasız, 60 km küresel okyanus + 60 m BERRAK tek-kristal buz kabuğu · 8 kPa N₂+CO₂ · 1,08 g) · ⭐ **deponun İLK ÜÇ AYLI filmi ve ilk ÜÇ IŞIK KAYNAKLI kadranı** — ARDE 7,04° kendi lavıyla yanan turuncu (Roche'un 166 km dışında; gelgit ısınması 66 W/m² = Io'nun 26 katı) · NIVE 2,33° keskin mavi-beyaz · VELUM 1,86° kenarsız menekşe-gül · güç oranı 5:3:1 · novum ALGISAL, **ZEMİN TERSİNMESİ**: "üstünde durduğun şey bir tavan" · taşıyıcı KATI ve BİRİNCİL (cam kabuk) · **6 × 10 s = 60 s**, ızgara araçtan [D124], 0 kesme, 0 replik, ekran metni 0,0 sn, **6/6 TAM LOCKOFF** (kamera film boyunca yere iner: 0,90→0,22→0,90→0,45→0,22→0,90 m), TEK LENS 24mm · sayaç metinsiz ÜÇ kanal: **üç gölgenin yelpazesi** 35°→3°→**−4°** (ortadaki gölge 2,52 m ile 6/6 sabit referans; hiçbir gölge nötr gri değil — her biri onu YAPMAYAN iki ayın renginde) · **üç kordonun derinliği** turuncu 10 m / menekşe 29 m / mavi-beyaz 60 m'yi geçip suya girer · **dikiş** 0,15→1,4→2,8 m · **KEŞİF üç adımda ve gözle:** çatlaklar düz değil YAY (sikloid, Europa'da gözlenmiş) → üç yay ailesi kesişiyor → kesişmede kabuk 9 m ve dikiş nefes alıyor · üç gelgit 41,4+5,1+8,2 m → hizalı 54,7 m · ⛔ **KART 1 (🔴) DOSYANIN MERKEZİNDE ve SAYIYLA BÜTÇELENDİ** — su 2/6 sahnede, 14,0 s, temas **0 kare**, en yakın 1,5 m, dalga/kırışık/sprey/damla/köpük/akıntı **0 kare** (ölü durgun ayna), **suda insan yansıması 0 kare** [D20], donma yalnız S5'te ve YÜZEY değişimi olarak [D14] · ⭐ **KART 9 YAPISAL OLARAK KAPALI**: tek baskın ışık yok, ÜÇ var · Kart 6 tetiklenmiyor (buz ufalanmıyor — bloklar YANAL ATIMLA kayıyor: 1,2 m/0,5 s · 2,2 m/1,1 s) · risk **4/12** · merkezi seçim S3 (dudağa diz çökmek; bedel aynı karede: levha 6° yatıp 40 cm düşer, üç gölge bire iner) · doruk S4 (arada cam olmadan açık okyanus + suda üç renkli disk) · final DÖNGÜ + GERİ ALMA · ⚠️ gerçek 1 numaralı risk kartlarda yok: **berrak buzun cam gibi üretilmemesi**; beş maddelik karşı önlem + S0 kapısı ffmpeg ile · ⚠️ film gerçek zamanlı DEĞİL (117 dk'dan altı an, gerekçe dosyada) · sert kesme 5 (bandın üstünde, bilinçli) ama **5/5 ses köprülü** · ✅ prompt_kontrol.py **GO · 0 BLOCK / 0 FIX, İLK KOŞUDA** (video 2.175-2.433 · image 5.742-5.965) · ⛔ **SPEC AYRI DOSYADA: `THE_OPEN_SEAM_QA_SPEC.md`** [D117] — filmle aynı gün |
| **The Thin Roof** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 27.08 · dikey shorts · 🆕 **MARS** — ince atmosfer (610 Pa · 0,379 g · 243 K), toz sıyrılmış kömür grisi bazalt kaldırımı, geç ikindi (§3.2 ortam kartının DİKEY hattaki ilk filmi) · kullanıcı talebi: *"Mars'ta geçen baya gerçekçi bir dikey shorts"* · ⭐ **DEPONUN İLK DRAMATİK İRONİ FİLMİ** — `HOOK` §3.1 27.08'de eklendi ve 16 dikey filmin 16'sı farkında olmadan "YOK" yazmıştı; burada taşıyıcı **② ZEMİN OKUR**, asimetri anı **0:22,4**, karakterin paniklediği kare sayısı **0** (panik yasağı engel değil MEKANİZMA) · novum ALGISAL ve tamamen gerçek jeoloji/geometri (Quiet Impact · Iron Slope · Near Pass emsallerinin DÖRDÜNCÜSÜ): *"eğri, ancak yukarıdan eğridir"* — 5,8 m yarıçaplı halka çatlağın görünen 2,0 m'lik yayı **8,7 cm** sapar; 0,40 m göz yüksekliğinde DÜZ, 9,00 m'den KAPALI HALKA okunur · **6 × 10,005 s = 60,03 s**, ızgara araçtan [D124], 0 kesme, 0 replik, ekran metni 0,0 sn (kadrajda ekran/gösterge/alet YOK — yasak KONSEPTLE kapalı) · **6/6 TAM LOCKOFF** · ⭐ **AÇI TİPİ NOVUMUN TAŞIYICISI** ve THE NEAR PASS'in açık maddesinin (6/6 alt açı) yapısal çözümü: üç kurulum = üç yükseklik = üç açı tipi — 0,35 m **ALT AÇI** (S0·S5) · 1,55 m **GÖZ HİZASI** (S1·S3) · 9,00 m **ÜST AÇI** (S2·S4), dizilim A-B-C-B-C-A · pit 74 × 61 m, taban 46 m ve **hiçbir kurulumdan görünmez** (ışın hesapları dosyada: A 2,57 m · B 25,5 m · C 41,4 m — "dip gösterilmemiş" bulgusu YANLIŞTIR) · ⭐ **GÖLGE İÇİ DOLGU ilk kez bir KAPI:** Mars saçılma yapar, gölgeler yumuşak kenarlı ve İÇİ DOLUDUR [§3.2]; deponun son beş filmi vakumdu ve "mutlak siyah" yazıyordu — E bloğunda **ffmpeg ile ölçülüyor** (YAVG < 18/255 → sahne reddedilir) · sayaç metinsiz ÜÇ kanal: kenara mesafe 3,4→1,1→0,9→0,7→1,9→7,4 m · 62 mm'lik çakıl (durur → 25° sallanır 38,4 → 0,40 m'yi 3,6 s'de 0,060 m/s² ile yuvarlanır 43,2-46,8 → çatlağa girer) · halkanın kadrajda okunabilirliği · risk **4/12** (Kart 3·4·5·9); **Kart 6 TASARIMLA kapatıldı** — Mars filmi olmasına rağmen hareket eden tek toz tanesi yok; ilk taslaktaki "kayayı fırçalama" jesti ÇIKARILDI ve el yuvası **düz avuç basınç testine** çevrildi (S3, kadraj payı ≥%28), risk 5/12 → 4/12 · gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı: **kavisin üretilmesi** (A/B promptlarında DÜZ, C promptlarında KAPALI HALKA — zıt talimat aynı prompta girmiyor) + **gölge içi dolgunun kaybolması** · ⛔ **ÜRETİM SIRASI NORMAL DEĞİL: S2 İLK ÜRETİLİR** — halka orada kapanmıyorsa diğer beş sahne üretilmez · tema **YALNIZLIK** (TEMA §3c moratoryumundan sonra HİÇ KULLANILMAMIŞ listeden ilk seçim; tek cümle TAKAS kalıbı DEĞİL) · merkezi seçim S4 48,1-49,3: yüzükoyun uzanma — bedel aynı karede, göğüs konsolu kayaya kapanır ve yüz tek sıcak çene kenarına iner (vizör beklenti satırı **④ YANSIMA DOLAR**; vizör durumu 6/6 birebir aynı, değişen 0 kare) · doruk S5 56,5-58,0: **ayağa kalkar** ve gördüğü şeyin sebebi ışık değil KENDİ GÖZ YÜKSEKLİĞİDİR (0,40 → 1,62 m); aynı hatta üç çöküntü daha (210 · 480 · 790 m), ufuk 3,31 km · final **DÖNGÜ + TWIST**, kinesik reset (60,03 = 0,00) · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX** (ilk koşu 1 FIX: açı TİPİ 2 + nesne-göreli taraf ×4 + çapasız toward ×2 + uzunluk ×3 — kapı kaydı dosyada); video 2.537-2.600 bandın TAM içinde, image 5.960-6.455 (emsallerin üstünde; sebebi ve kısaltma sırası dosyada, karakter bloğu KISALTILMAZ [D45]) · ⛔ **SPEC AYRI DOSYADA: `THE_THIN_ROOF_QA_SPEC.md`** [D117] — filmle AYNI GÜN indi · E bloğunda ÜÇ makine kapısı [D125]: gölge dolgusu · kamera sabitliği (vidstabdetect) · kurgu kapısı; **dördüncü kapı (halka) makineyle koşulamaz ve bu dürüst kayıttır** | · ⛔ **28.08.2026 · ÜRETİLDİ, ALTI MERCEK KOŞULDU, MATRİS YİNE DE 0/4** — altısı da mod V, oysa `THE_THIN_ROOF_QA_SPEC.md` YAZILMIŞ VE HAZIRDI: ortak adım ① gereği hiçbir T tablosuna satır girmedi [D129] ve **SPEC hazırken mod V koşulan film sayısı 7'ye çıktı.** ⭐ **Master ölçümü:** 65,030 s · 720×1280 · 30 fps · **AAC ses VAR** (−17,3 LUFS) — buna rağmen altı raporun altısı da *"no audio information at all"* yazdı, ③ bunun üstüne STOP bloğu bastı → **D137**. Kurgu kapısının üç satırı da GEÇTİ (6=6 · 60,033 s = 60,03 ± 0,5 · şerit `111111`) ve film yine de finalini teslim etmedi → **D141**. ⭐ **18 severity bulgusunun 4'ü gerçek**, 6'sı ⑩'da/ölçümde düştü, 5'i ⬜ açık; **filmin ölçülmüş 6 gerçek ihlalinin 6'sı da raporlarda YOK** — halkanın içine yazılmış "11 metres" (D138) · sırt ünitesi (D139) · klibin ilk 0,3 s'sinde doğan klon (D140) · havada çakıl · üretilmemiş twist · ölmüş döngü + 4,997 s başlık kartı. ✅ **Halka kapısı GEÇTİ**: 22,41 s'te halka 9 m'den kapalı bir daire olarak okunuyor — filmin 1 numaralı riski tuttu. SPEC'in E bloğundaki üç makine kapısı İLK KEZ koşuldu; gölge dolgusu kapısı **S1'de düştü** (en koyu blok 3/255), kamera sabitlik kapısı kurulu olmayan bir filtreye yazıldığı için koşulamadı → **D142**. Kayıt: `01_FILM_RAPORLARI/THE_THIN_ROOF.md`
| **The Heavy Side** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 29.08 · dikey shorts · 🆕 **VAKUM + DÖNME YERÇEKİMİ** — yarıçapı 9,00 m olan, hiç basınçlandırılmamış bir dönme modülünün iç güvertesi; dönme periyodu 60 saniyede 13,00 s → 8,00 s, ağırlık 202 N → 533 N (2,64×). **`KILAVUZ_REHBERI` §3.7 ortam kartı bu filmle AÇILDI** (§3.1'in alt kartı, §3.5 emsali) · kullanıcı talebi tek kelimeydi: ***aksiyonlu*** · ⭐ **deponun İLK DÖNME YERÇEKİMİ filmi ve İLK ENTROPİ TEMALI filmi** (TEMA §3c'nin HİÇ KULLANILMAMIŞ listesinden; tek cümle TAKAS kalıbı DEĞİL: *"biriktirilmiş her şeyin er geç dağılması"* — göbek fren volanının açısal momentumu halkaya dağılıyor, volan durdukça halka hızlanıyor; ekrandaki karşılığı volanın çentiği: S2'de 1,5 tur / 10 s, S4'te yarım tur, S5'te DURUYOR) · novum **FİZİKSEL YASA**, ihlal 1, tamamen gerçek mekanik (Quiet Impact · Iron Slope · Thin Roof emsallerinin BEŞİNCİSİ): **a = (v ± u)² / R** — aynı güvertede aynı adım, iki yönde iki farklı ağırlık · ⭐ **filmin ekseni bir EŞİTSİZLİK ve daha çok çabalamak durumu KÖTÜLEŞTİRİYOR**: ileri sıçrayışın matematiksel tavanı wR/(2v) = **1,97 m**, geçilecek boşluk **3,50 m**; S1'de üç adımlık koşu ağırlığı 270 N'dan 621 N'a çıkarıyor ve diz katlanıyor · çözüm güvertenin ALTINDAN el ele geçiş, doruk **kendini hafifletmek**: asılıyken 499 N, gövdeyi ters yöne 3,00 m/s salladığı **0,9 saniyelik pencerede 157 N** — kendini o pencerede yukarı atıyor · dramatik ironi taşıyıcı **② ZEMİN OKUR**, asimetri anı **0:24,6** (beş kayıp cıvata, beşi de yuvasından 60 cm AYNI yöne yatmış; o kendi botlarına bakıyor), panik 0 kare · ikinci görsel şok S3: kendi bıraktığı 62 mm'lik cıvata 0,97 s'de düşüp **62 cm yana** iniyor (kiriş/atalet hesabı dosyada) · merkezi seçim S4 40,4-41,6: emniyet halatını açmak — bedel AYNI karede (serbest uç 58 cm yana iner) · final **DÖNGÜ + TWIST**: merdivene tırmandıkça Coriolis onu yandan itiyor — **merdiven dümdüz, gövdesi 11,7° eğik**, ve açı yukarı çıktıkça büyüyor · **6 × 10,005 s = 60,03 s**, ızgara araçtan [D124], 0 kesme, 0 replik, ekran metni 0,0 sn, 6/6 TAM LOCKOFF · kurulum A-B-C-B-C-A, 3 açı tipi (alt · göz hizası · üst), ölçek merdiveni WS·MS·WS·CU·WS·EWS · lens kilidi **24 mm + 75 mm küresel** (32 mm geometrik olarak yetmiyor — halkanın kapanışı kadraja sığmıyor, hesap dosyada) · risk **4/12** (Kart 3·4·5·9); **Kart 6 tasarımla kapalı** (vakum + işlenmiş metal: toz/duman/kıvılcım/enkaz/yıldız 0 kare) ve **Kart 9 YAPISAL olarak kapalı** (yıldız dönme EKSENİNDE ve kadraj dışında; adamın bütün hareketi eksene DİK — ışığa doğru koşmak güverteden çıkmak demek; ⭐ aynı karar altı klibin ışık sürekliliğini FİZİKLE garanti altına alıyor) · ⛔ **İLK TASLAKTAN ÇIKARILAN ŞEY DERSİ KAPATTI:** halkanın etrafında altı uzun sıçrayış (her biri 1,87 s havada, 7,7 m) ÇIKARILDI — 60 saniyenin 16'sında havada duran gövde D23 + D12/D44'ün doğrudan tetikleyicisidir; yerine güverte altı el ele geçiş kondu ve havada geçen TOPLAM süre **2,1 saniyeye** indi (THE THIN ROOF'un fırçalama jestini çıkarmasının kardeşi) · ⚠️ gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı: **güvertenin başın üstünde KAPANMASI** (model "koridor" görünce düz koridor üretir — "corridor/tunnel/hallway/trench" kelimeleri 18 promptun hiçbirinde geçmiyor; kapanma her promptta SAYIYLA ve KANITIYLA yazılı) ve **gölge içine dolgu girmesi** · ⭐ **E bloğundaki gölge kapısı THE THIN ROOF'un TERSİDİR**: orada YAVG < 18/255 reddediyordu (Mars, saçılma var), burada **YAVG > 16/255 reddediyor** (vakum, dolgu yok) — eşik filmden okunur, hafızadan değil · ⛔ **ÜRETİM SIRASI: S0 İLK** (halka kapanmıyorsa film üretilmez), sonra S4 (delikten aşağı bakan kadrajda gövde güvertenin ALTINDA mı) · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX** (ilk koşu 1 FIX: nesne-göreli taraf + metin yasağının KAPSAMI [D138] — kapı kaydı dosyada); video 2.474-2.580 bandın TAM içinde, image 6.438-6.670 (**depodaki en yüksek değer**; sebebi ve kısaltma sırası dosyada) · ⭐ **PROMPT_QA rubriği üç GERÇEK bulgu verdi ve biri depoda YENİ bir vakadır:** aksan renginin adı **"oxblood"** idi ve 18 promptun 14'ünde POZİTİF tarifin içinde geçiyordu — YASAK LİSTESİ TUZAĞI'nın [REHBER §7] ilk **RENK ADI** vakası; sınıflandırıcı "no" önekini değil KELİMEYİ okur, renk **"deep maroon"** yapıldı. Ayrıca karakter bloğundaki **"no weapon"** silindi (0 kare silah taşıyan bir yasak, koruduğu şeyi üretilemez kılar) ve video promptlarına **açı sözlüğü** (LOW-ANGLE / EYE-LEVEL / HIGH-ANGLE) eklendi — imaj promptlarında vardı, videolarda yalnız YÜKSEKLİK yazılıydı ve model kelimeyi okur · ⛔ **SPEC AYRI DOSYADA: `THE_HEAVY_SIDE_QA_SPEC.md`** [D117] — filmle AYNI GÜN indi |
| **The Tall Shore** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 14.08 · 2-4 dk · ince atm. (🆕 KURU OKYANUS HAVZASI, 0.09 atm) · **ÖLÇEK filmi: 9.000 m'lik kıyı basamağından 1.100 km'lik tuz havzasına iniş** · 18 × 10 s = 3:00, 0 kesme, 18/18 sabit lockoff, 4 viral ara (S3·S7·S10·S15) · ⚠️ **risk 6/9 — depodaki en yüksek sayım ve EŞİĞİN ÜSTÜNDE**, gerekçesi ve azaltma planı planda yazılı: iki 🔴 kart (su·canlı) SIFIR, gerçek ağırlık Kart 7'de · ⛔ **depo standardından bilinçli sapma: kadın ÜÇ KEZ konuşuyor** (Ring Light/Blind Return 0 insan repliği) — karşı önlem TURN LOCK (sahne başına tek konuşmacı, 9 replikli sahnenin 9'unda) + AI sahnelerinde ağız kapalı + kadın sahnelerinde 75mm · ⭐ **HAZIR DÜŞÜŞ planda yazılı**: S2 üretim kapısı batarsa kadının üç repliği düşer, üç AI repliğiyle değişir, risk 6/9 → 5/9 (yeniden yazım gerekmez) · dört metinsiz sayaç: zaman SESLİ + mesafe YEDİ SEKİ + perspektif SIRT SAYISI (9→7→5→3→2→1, monotonik) + geri sayım GÖLGE ETEĞİ (25 m/dk) · ölçek mekanizması **HAVA PERSPEKTİFİ** sayısal kilidi (10 km'de kontrast dörtte bir düşer) — Cold Burn'ün dok kapısının panzehiri · doruk S13 (26 kg'lık kanıtı tuza gömmek; bedel aynı sahnede, S17'de kadrajda duruyor) · kask 18/18 kapalı, durum değişimi 0 · Canopy World'ün battığı madde (katmanlı dünya ışık takvimi) bu filmin omurgası: LAYER LIGHT SCHEDULE irtifaya göre sıralı ve monotonik · ⚠️ **PROMPT_KONTROL betiği FIX döndü** (36/46 prompt, ⛔ 0 BLOCK; tek bulgu UZUNLUK: 14/18 video promptu bandın 30-490 karakter üstünde, tavanın çok altında) — üretimden önce kapatılacak, yol filmin BÖLÜM 3'ünde yazılı · ⛔ SPEC bloğu dosyanın içinde (§0.16) — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Uphill Dark** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 17.08 · 3-5 dk · 🆕 **VAKUM + İTKİ YERÇEKİMİ (0.220 g)** — depoda ilk alt-ortam: vakumun bütün kuralları geçerli ama "her şey süzülür" kuralı GEÇERSİZ, her şey DÜŞER · ⭐ **novum: uzayda düşmek var** — 210 m'lik yıldızlararası gemi kalkış yanmasını durduramaz, yanındaki her serbest cisim kıça doğru 2.16 m/s² ile düşer; novum'un üç kanıtı da KATI NESNE (sarkan kordon · düşen kovan · düşen yük), türetilmiş optik fenomen [D73] ya da yokluk [D76] DEĞİL · 25 sahne (Hook 9 s + 24 × 10 s = 4:09), 0 kesme, 25/25 sabit lockoff, 4 viral ara (S4·S10·S19·S23), **0 replik** · ⚠️ risk 4/9 (kask · ikinci figür · sayaç · parçacık); iki 🔴 kart (su·canlı) SIFIR · ⭐ **D23 (sıfır-g rijitliği) YAPISAL OLARAK ELENDİ** — film boyunca hiçbir kare sıfır yerçekiminde değil; kural değil KARAR ile kapatıldı [AGENTS §8] · ⭐ **ikisi de 25/25 sahnede kemerli ve oturuyor** → biniş/iniş/yürüme 0 kare [D69 ①] · dört metinsiz sayaç: PENCERE MERDİVENİ (gemi gövdesinin hangi bölümü pencerede) · SARKAN KORDON (itki var mı) · KARTUŞ YUVALARI 6→0 · YÜK KIZAĞI 40 dolu→40 boş · aritmetik filmin kendisi: 3 tırmanış × 40 m = 120 m ama radyatör kanadı tırmanış 2'yi 12 s erken kestirir (22 m) → 16 m AÇIK, 0 kartuş · CENTRAL CHOICE S19 (%75.7) = 900 kg yükü bırakmak, bedel AYNI KAREDE (kırk karot düşerken gövde pencerede kaymaya başlar) · doruk S21 temas 0.20 m/s (3:37.9 = **%87.5**, bant içi) · turuncu TAM ÜÇ YERDE (iki skafandr · yük kayışı · atma kolu) ve S19'dan sonra kadrajdaki tek turuncu iki insandır · ⭐ **REFERANS PAKETİ 5 SAYFA × 4 PANEL** (varlık başına tek sayfa; 17.08.2026'da 13 tek görselden indirildi, iki durum çifti aynı sayfada) · ✅ prompt_kontrol.py: **0 BLOCK**, 50/50 prompt tavanın (4.300) altında; tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi + İLK RED PROTOKOLÜ PART_A §Üretim Notları'nda · ⛔ SPEC bloğu planın içinde — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Blue Drift** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 17.08 · 3-5 dk · **YAZIM TAMAM:** PLAN + PART_A + PART_B + KAPAK + **REFERANS_PAKETI (5 sayfa × 4 panel, Uphill Dark formatı; üç durum çifti aynı sayfada)** — 50 film promptu + 2 kapak; prompt_kontrol 0 BLOCK (A/B FIX yalnız uzunluk, gerekçeli · KAPAK ✅ GO) · üretim KAPI 0 (referans sayfaları + §4 devamlılık kapısı) → S21 → S15 → S4 → S0 sırasıyla başlar · 🆕 ortam: mavi devin KIRAĞI UYDUSU (azot buzu, 0.4g, gece yüzü YALNIZ mavi planetshine ile aydınlık) — **palet üçlemesinin kapanışı: beyaz (Cold Burn) → siyah (Black Cradle) → MAVİ** · ⭐ **novum: ölü aracın YAKALANIŞI** — perde kenarı iticileri öldürür, araç balistik; depodaki beş yanaşma filminde manevrayı hep küçük araç yapıyordu, ilk kez YAKALAYAN ANA GEMİDİR ("katedral pervaneye gelir") ve doruk EDİLGENDİR · tehdit depoda ilk kez GÖKTEN iner: plazma perdesi (aurora, taban 90°→40°, yalnız mavi-menekşe — YEŞİL NEGATİFTE) · 25 sahne × 10 s = 4:09 (standart, sapma yok), 0 kesme, 25/25 lockoff, 4 viral ara (S4·S7·S15·S21) · 16 replik / 13 sahne — 10 MACHINE (KERTE ana gemidedir, S9-S11 bağlantı kopuk = atışma yapısal imkânsız [D82]) · CENTRAL CHOICE S14 = kabin havasını itki olarak harcamak (6 düz puf ile despin; bedel S16 mekanik ibrede %40) · doruk S21 yakalayış %84-88 (sahibi KERTE: "Tuttum.") · ⚠️ risk 5/9 TAM EŞİKTE; iki 🔴 kart (su·canlı) SIFIR, ateş/patlama 0 kare · kartlarda olmayan iki risk yazılı: MAVİ-ÜSTÜ-MAVİ (beş mavi ton/doku skalası + amber istisna ailesi + HAZIR DÜŞÜŞ) ve AURORA KLİŞESİ · üretim S21→S15→S4→S0 kapılarıyla başlar · ⛔ SPEC bloğu planın içinde — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **Loss of Lift** | ❌ | 🚨 ~~8/6~~ | ❌ | ⛔ön koşu Ⓥ7.0 | **0/4** 🆕 20.08 · ⚡ **21.08 ÜRETİLDİ + 3 QA KOŞUSU — hepsi ÖN KOŞU, matris 0/4 KALDI** [D94/117]: SPEC planın 738. satırında hazırdı, üç koşu da mod V · üç rapor AYNI oturumdan, AYNI 26 satırlık haritayı paylaşıyor → tek ölçümün üç kılıfı [D110] · 🧩 iki koşu 🚨 GEÇERSİZ (aynı defter, 8/10 ve 6/10, ikisi de kendi hücrelerinin ortalaması değil → **D119**) · 📖 Ⓥ7.0 ŞARTLI (diyalog **9/10** ve özgünlük 8/10 — tek replik ve novum tuttu; yapı 5/10 sıra şüphesine bağlı) · ⛔ kurgu kapısı: sayı ✅ (26−1 kart=25) süre ✅ (255−5=250≈249) **SIRA ⛔ insan şeridi slot 19/20 ters → doruk yanlış yuvada olabilir, master 3:09-3:29 izlenecek** → **D118** · 🔴 4:10-4:15 başlık kartı = ekran metni kilidi 0.0 s ihlali, D70/72 zincirinin 8. vakası · kilit çelişkisi defterinde **6 madde ⬜ AÇIK** (~1,5 dk seyretme) → içerik dersi YAZILMADI · kayıt: `01_FILM_RAPORLARI/LOSS_OF_LIFT.md` · 🆕 `LOSS_OF_LIFT_QA_SPEC.md` yazıldı, sıradaki koşu MOD D · 3-5 dk · 🆕 ortam: **VENÜS BULUT KATMANI — sürekli bulut / nötr yüzerlik** (0.53 bar CO2, 0.904 g, bağıl rüzgâr 0-2 m/s, güneş diski YOK, zemin YOK) · yeni ortam kartı önerisi (§3.6) planın içinde · ⭐ **LOW POWER'ın kardeşi olarak sipariş edildi** — aynı motor (tek kişi · sessiz-yavaş-durdurulamaz tehdit · tek sayı · iki renk · devretme teması · tek yanlış-umut beati), tamamen yeni malzeme: güç yerine KALDIRMA, toz yerine ASİT, karanlık yerine AŞAĞI · ⭐ **konu seçimi LOW POWER'ın ölçülmüş iki dip skorunu yapısal olarak siliyor**: toz 0 kare → D39 tetiklenemez · gölgesizlik fizik → D41'in yanlış teşhis zemini yok · asit kirletmez AĞARTIR, yıpranma TAM 3 sabit bölge → D42 yüzeyi daralır · novum katı gövde (yüzen istasyon) — türetilmiş optik [D73] ya da yokluk [D76] DEĞİL · 25 sahne (Hook 9 s + 24 × 10 s = 4:09) standart, 0 kesme, 25/25 sabit lockoff, 4 viral ara (S5 zarfın sırtı · S13 varmayan yağmur · S19 tek mor · S23 iki ışık) · **1 replik** (S22, ağız kadraj dışı — bu istasyonda konuşmak da nefestir; D35 yüzeyi 0) · dört metinsiz sayaç: PİN YAYI (24 çentik × 250 m, ibre 7→13) · BUĞU (S3 var → S18 yok) · KAÇAK ISLIĞI · SONDA FENERİ (4 s'de 1 nabız) · aritmetik filmin kendisi: kaçak 322 kg/s → batış 30 m/s; kalan TEK tüp 600 kg = zarfa 1,9 saat / **70 metre**, ya da 12 m'lik sondayı doldurup kolonu 61 km'ye — asidin ÜSTÜNE — çıkarmaya TAM yeter · CENTRAL CHOICE S20 (%79-83) = kolu sonda borusuna atmak, bedel AYNI KAREDE (takviye susar, ibre yeniden düşer) · S0↔S24 açılış-kapanış çifti (tek gövde iniyor ↔ iki gövde, zıt yön) · ⚠️ risk 5/9 TAM EŞİKTE (kask · ikinci figür · sayaç · katmanlı dünya · tek replik); **su · canlı · parçacık SIFIR** (toz/ateş/patlama/egzoz 0 kare) — tek replik düşerse 4/9 · kartlarda olmayan iki risk yazılı: OKRA-ÜSTÜ-OKRA (beş dokulu ton skalası + HAZIR DÜŞÜŞ) ve **"HOVERING" ÇAKIŞMASI** (negatif çekirdek yasaklıyor, filmin gövdesi gerçekten yüzüyor → yasak parçacıkta kalır, gövdeye POZİTİF cümle [D59]) · LAYER LIGHT SCHEDULE (KART 6b) irtifa + güneş fazıyla sahne sahne yazılı ve monotoniklik gerekçesi kayıtlı · üretim S0 (hovering/ölçek kapısı) → S5 → S20 → S8 sırasıyla başlar · ⛔ YAZIM TAMAM (20.08): PLAN + PART_A + PART_B — 25 sahne / 50 prompt, çapa blokları iki dosyada da üreteçten bayt bayt aynı (parafraz avcısı 0 şüphe ×2), insanlı 21 video I2V + kompakt karakter kilidi, tek replik S22 (telsiz, ağız kadraj dışı → D35 yüzeyi 0), 7 eş kadraj çifti, S20 bedel kanalı D90 adaptasyonu (boru terlemesi + ıslık takası) kayıtlı; prompt_kontrol ×2: 0 BLOCK / FIX yalnız uzunluk (tavan aşımı 0; maks video A 3.846 / B 3.799); KAPAK ✅ GO (20.08 · A: yüz %60 + S13 varmayan yağmur, bakış merakın kendisine · B: S24 aynası, insansız; iki promptta metin 0, D79/D95 negatifte, sağ alt rozet köşesi boş; prompt_kontrol 0 BLOCK / 0 FIX) · MUZIK ✅ (20.08 · tek tempo 48 BPM = tam 2 ölçü/sahne; skor filmin kaldırma gazı — katman katman sökülür, yalnız CUE C'de eklenir; alçalan motif S23'te TERS dönüp tamamlanır; sessizlik penceresi 3:19-3:49 = doruk+bedel+tek replik müziksiz, S20 ıslık takası çıplak; iç yatak D83 tek parça; fener 4 s ↔ ölçü 5 s kasıtlı off-grid [§13]) · **YAZIM PAKETİ TAM: PLAN + PART_A + PART_B + KAPAK + MUZIK** · üretim S0→S5→S20→S8 kapılarıyla başlayabilir |
| **The Rose Coat** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **26.08.2026 · BEŞ MERCEK KOŞULDU, MATRİS YİNE DE 0/4** — SPEC dosyası filmin klasöründe HAZIRDI ve beşine de verilmedi [D129]: koşuların tamamı ÖN KOŞU, hiçbir satır sayı taşımıyor. ⭐ **Ölçüm kapısı ⑪ KOŞULMADI** — master ölçülmedi, aşağıdaki her sayı raporunki. ⛔ 🔴 KAPALI TEK MADDE: **2:10-2:15 başlık kartı** = `SCREEN TEXT 0.0 s` ihlali, dördü de aynı in-out'u verdi [D70/72/120]. ⬜ **EN PAHALI AÇIK MADDE:** dört mercek 2:00-2:09'da bir MERDİVEN TIRMANIŞI bildiriyor, plan `BİNİŞ 0 kare` diyor ve planlı final S12 (iki sırt, iki renk) — doğruysa film FİNALİNİ KAYBETMİŞ. ⛔ ④'ün kesme listesindeki beş adayın beşi de yük taşıyan sahne; ikisi `KESİLEMEZ` viral, biri filmin DORUĞU + KAPAK KARESİ. ② `no counter present` dedi — filmde ÜÇ metinsiz sayaç var. ⑤'in altı hücresinin dördü tek bir tasarım kararından (pada mesafe 600→0 m). ③ `AUDIO ABSENT` — plan 11 sahnede müzik yazıyor. Kilit çelişkisi defteri: **10 madde, 8'i ⬜ AÇIK**, operatör iş listesi ~4 dk master. film kaydı: [→](01_FILM_RAPORLARI/THE_ROSE_COAT.md) · **DERS 129 · 130 · 131 · 132 · 133 · 134 · 135 · 136** · sonraki tur MOD D · ⛔ tamlık matrisi ❌ KALIR — ölçüm yapılmadı, ölçme aleti ölçüldü · — — — 🆕 25.08 · 2-4 dk · ince atm. (%1,2 basınç · 0,40 g · 🆕 GÜL RENGİ TOZ OVASI, 40 saatlik gün) · ⭐ **deponun İKİNCİ iki figürlü uzay filmi** (birincisi THE LAST SHIFT) ve ilki, ikinci figürün SÜS DEĞİL MEKANİZMA olduğu film: novum "kendi sırtına ulaşamamak"tır ve tek kişiyle KURULAMAZ — bu yüzden §4.1 bilimkurgu kartının "tek kâşif, hep yalnız" kilidi bilerek kırıldı, bedeli §0.8b'de **altı satırlık İKİ FİGÜR BÜTÇESİ** olarak yazıldı (zombi kartının altı satırlık bütçe emsali ilk kez BAŞKA bir riske uygulandı) · ⭐ novum: morötesiyle yüklenen toz her yüzeye yapışır ve yalnız ARTAR (0,25 mm/dakika); giysinin ısı attığı tek yer sırttaki düz gömme radyatör panelidir ve omuz eklemi ona 40 derece YETİŞMEZ · 13 × 10 s = 130 s (2:10), **0 kesme, 13/13 sabit lockoff**, 0 replik (tamamen sessiz), 3 viral ara (S3·S7·S11) · ⭐ **palet filmin SAYACIDIR**: iki giysi kadrajdaki tek DOYGUN renktir, dünya ise soluk tebeşir gülü; sırtlar kaplandıkça giysi dünyanın rengine döner (beş görsel durum, 0→9 mm) — ayrım TONDA değil DOYGUNLUKTA, bu yüzden post'ta doygunluk oynanmaz · doruk S11 = fırçadaki son 20 darbe, **bedel AYNI karede** (fırçalayan figürün kendi sırtı kadrajda ve ova rengi; fırça 8.5 s'de vurulur ve hiçbir şey dökülmez) · aritmetik doruk: 50 darbe kaldı, gemi paneli 30 · ötekinin sırtı 20 · kendi sırtı 14 ister · final GENİŞLEME + görsel ikilem, ⛔ **biniş ve kalkış 0 kare [D69]** · üç sayaç metinsiz (pada mesafe 600→0 m · sırt rengi · fırçanın kılları) · beş Çehov'un beşinin de ödeme sahnesi numaralı · ⚠️ **risk 5/12 TAM EŞİKTE**; elenen kartlar su · canlı · gösterge · diyalog · kamera · kesme · ışık mıknatısı (Kart 9 YAPISAL elendi) — kalan ağırlığın tamamı Kart 3 (iki kask) + Kart 4 (iki figür) + Kart 6 (toz) · ⭐ **D79 GEREKÇELİ UYARLANDI**: sırt paneli bir ÜNİTE değil giysiye GÖMÜLÜ düz bir yüzeydir, silüet 13/13 sahnede düz kalır (§0.13 ②) · ✅ prompt_kontrol.py: **0 BLOCK**, araç yönelim kapısı ilk koşuda açıldı ve kapatıldı; FIX yalnız uzunluk (imaj 1.855-3.569 · video 2.173-3.996, tavan 4.300) ve ⛔ dürüst kayıt: en uzun iki prompt LAST SPAN'in tavanının üstünde, ilk redde kısaltılacak yer §0.14b'de yazılı · ⛔ SPEC AYRI DOSYA (`THE_ROSE_COAT_QA_SPEC.md`) — **MOD D koşulacak, mod V ön koşudur [D94/D117]** |
| **The Cold Weld** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **01.09.2026 · ⑪ ÖLÇÜM KAPISI KOŞULDU — master 4K/155,075 s; KURGU KAPISI 3/3 GEÇTİ (15 klip = plan · gövde 150,10 s · şerit birebir) ve novumun ÜÇ KANITI DA EKRANDA (avuç makrosu 65 s · diskli duvar 100-120 s · doruk 122 s) — ama ÜÇ TESLİM KUSURU: 🔴 FİLİGRAN doğrulandı (sağ alt çeyrek 6/6 örnek; %3 crop yetmez, temizlik kadrajın %12'sini götürür) [D150 2. vaka] · 🔴 kuyruk kartı 150,10 s→SON [D70/72 9. vaka] · 🔴 loudness −18,1 LUFS / 0,0 dBFS. **MOD D KOŞUSU DURDURULDU** — filigranlı master master değildir; altı temiz oturum harcanmadan kapı durdu. 🚩 ADAY-1 KAPANDI (hipotez YANLIŞ: kanıtlar ekranda, sorun OKUMA → D151'in 2. vakası; ② otuz bir diski "wall BUTTONS" sandı). ⭐ YENİ DERS **D163**: S8-S11 BLOK TAKASI (anahtar ↔ duvar) insan şeridini hiç bozmadan geçti — şerit tek figürlü filmde SABİTTİR ve sıra eksenini ÖLÇMEZ; kapısı ⑪ SAHNE IZGARASI. Tam kayıt §⑪. **ÖNCEKİ KOŞU (altı mercek, mod V):** MATRİS YİNE DE 0/4 — İKİ AYRI KAPIDAN DÜŞTÜ.** ① SPEC kapısı: `THE_COLD_WELD_QA_SPEC.md` VAR ve altı raporun altısı `INPUT MODE: V` → koşu TEKRARLANIR [D129]; **SPEC yazılıyken mod V koşulan film sayısı 9.** ⑤ ÇAPRAZ SAYIM: kesme sayıları 14/14/16/16/14/14 → fark 2 > 1 → **parti 🚨 GEÇERSİZ** [D107]. ⑪ ÖLÇÜM KAPISI KOŞULAMADI (master depoda yok) → süre/sahne sayıları hiçbir kapıya girmedi. Film kaydı: `01_FILM_RAPORLARI/THE_COLD_WELD.md` (② kilit çelişkisi defteri **12 madde · 9 ⬜ AÇIK** · ⑩'da 5 bulgu DÜŞTÜ: kopan levhanın yükselmesi · S8 duvarı · anahtarın dik durması · 22° eğimde kaymama · tozsuzluk — beşi de PLANDA YAZILI). ⭐ **GEÇERSİZ PARTİDEN İKİ ÖLÇÜM SAĞ ÇIKTI [D121]:** ① üç bağımsız mercek planın İNSAN ŞERİDİNİ birebir üretti (`-11111111111111`) → kurgunun SIRASI doğrulandı, eksik sahne yok; ② ⑨ hizalama kapısı ①'in 14 kesme zaman kodunu planın 10 s ızgarasına oturttu (max |Δ| = 1 s) → zaman kodları uydurulmamış **ve ④ HİKAYE'nin 8 sahnelik haritası ölçümle çürüdü** (kendi 16 kesme sayısıyla çelişiyor; Yapı/Tempo/Yay/Final/Tutundurma hücreleri olmayan bir filme verildi, kesme listesi UYGULANMAZ). 🔴 **İKİ ZORUNLU ÜRETİM İŞİ:** (a) 2:30-2:35 başlık kartı kaldırılır — plan ekran metni 0,0 s der, D70/D72'nin 8. vakası ve AYNI GÜN Payload'da 9.'su çıktı; kart ayrıca S0↔S14 eş kadraj çiftini öldürüyor; (b) köşe testi koşulur — ⑤ 15/15 sahnede sağ altta sabit işaret bildirdi, sahibi ① görmedi [D150 · D162]. 🚩 **PARK EDİLEN DERS ADAYI:** altı merceğin altısı da filmin novum'unu adlandırmadı (⑥ 'is the wrench MAGNETIZED?' diye sordu, ② avuç sayacını hiç izlemedi, hiçbiri 31 diskli duvarı anmadı) — hipotez: bu filmdeki kanıtların tamamı OLUMSUZLAMA; kapatma prosedürü film kaydında, master gelince ~2 dk. ⭐ **BU KOŞUNUN ÜRÜNÜ İKİ DERS — D161 (rapor aritmetiği kapısı: 6 raporun 5'i kendi kapısından geçemedi, ② fabrike toplam bastı) · D162 (⑤ mutabakatı ölçüyor, SUSKUNLUĞU ölçmüyor)**; ikisi de bulgudan değil ALETTEN çıktı, ikisi de master olmadan doğrulanabilir · 2-4 dk · 🆕 **VAKUM + TEMİZ METAL / SOĞUK KAYNAK** (havasız ay · 0,30 g · gölge içi mutlak siyah · yıldız 4,2° EKRAN-SOLDA sabit) — `KILAVUZ_REHBERI` §3.8 bu filmle açıldı · **novum gerçek uzay mühendisliği:** oksitsiz iki metal yüzey temas ettiği anda ATOMİK olarak birleşir, bu yüzden otuz yıl önce düşen gemi enkaz değil TEK BİR METAL RESİFTİR; ikinci kural birincinin SONUCUDUR (ışık çizgisi geçtikçe levhalar ısınıp uzuyor ve dikişler kopuyor) · 15 × 10 s = 150 s (2:30), **0 kesme**, 15/15 sabit lockoff, 3 viral ara (S3·S9·S13), **0 replik** — tamamen sessiz · ⭐ **DEPONUN EN YÜKSEK AÇI ÇEŞİTLİLİĞİ: 8 kurulum / 7 AÇI TİPİ** (göz hizası · alt · üst · tepe · profil · OTS · eğik; POV yok). Önceki en yüksek 4'tü ve o film kaldırılmıştı; 26.08 taramasında 107 dosyanın 43'ü 3 tipin ALTINDAYDI → `TODO_TEMA_VE_ACI_KAPILARI.md` E fazının YATAY karşılığı · ⭐ **TEMA: YALNIZLIK** — temanın depodaki ilk YATAY kullanımı (dikey THE THIN ROOF 27.08'den sonra ikinci film; §3c'nin "hiç kullanılmamış" listesi BAYAT çıktı ve düzeltmesi film dosyasının §0.18'ine yazıldı), tema cümlesi §3c'nin TAKAS KALIBINDA DEĞİL; 4 sahne indeksi (S3 boşluk · S8 yankı · S12 içe kapanma · S14 tekil kaynak) · üç metinsiz sayaç: ışık çizgisi mesafesi 34→0 m (monotonik dramatik saat) · **avuç durumu 2→0** (filmin ana sayacı, iki kalemlik bedel) · resifteki yamalar 31→33 — ⭐ sayaç B düşerken sayaç C tam o kadar YÜKSELİR · doruk S12 (son avucunu BİLEREK levhaya kaynatır), bedel aynı karede · CENTRAL CHOICE S12 · final MUĞLAK + görsel ikilem, ⛔ biniş 0 kare [D69] · ⭐ S0 ↔ S14 eş kadraj (aynı kurulum A: bir metal yüzey ve ona kaynamış tek yabancı nesne — biri anahtar, öteki bir avuç diski) · risk **5/12** tam eşikte, malzeme azaltma turu §0.8b'de yazılı (uzun sıçrayışlar · ikinci kâşif · giysi hasarı ÇIKARILDI) · **sıçrama 0 kare / havada geçen süre 0,0 s → D23 yapısal olarak tetiklenemez** · ✅ prompt_kontrol.py: **0 BLOCK**, ⑩ kurulum · ⑪ açı · ⑬ tema kapılarının üçü de GEÇTİ; tek FIX uzunluk (video 2.800-3.866, tavan 4.300), gerekçe §0.14b · ⛔ SPEC AYRI DOSYA `THE_COLD_WELD_QA_SPEC.md` — **MOD D koşulacak, mod V ön koşudur [D94]** |
| **The Still Swarm** | ❌ | ❌ | ❌ | ❌ | **0/4** ⛔ **02.09.2026 · SEKİZ MERCEK KOŞULDU (deponun ilk 8 mercekli partisi) — SEKİZİ DE MOD V → MATRİS 0/4 KALDI.** ① SPEC kapısı: `THE_STILL_SWARM_QA_SPEC.md` VAR ve mod D zorunlu beş merceğin beşi `INPUT MODE: V` → koşu TEKRARLANIR [D129]; **SPEC yazılıyken mod V koşulan film sayısı 10.** `rapor_kontrol.py` çıkış 2 · ⛔ 5 TEKRAR · ⚠️ 2 ŞARTLI · ✅ 1 GO; 8 raporun 7'sinde SEVERITY TALLY ≠ yazılı etiketler → REGENERATE / IDENTITY BREAK / SUBJECT DUPLICATE / REWRITE PREMISE hükümlerinin hiçbiri uygulanmadı [D161 2. vaka]. ⑪ ÖLÇÜM KAPISI KOŞULAMADI (master depoda yok) → süre/sahne sayıları hiçbir kapıya girmedi [D125 3. vaka]. ② kilit çelişkisi defteri **8 madde · 8'i ⬜ AÇIK** → **bulgudan ders YAZILMADI**; adaylar `DERSLER/GOZLEM_DEFTERI.md` ADAY-6'da. ⑩'da DÜŞEN bulgular: "tether'la ilerleme" · "0:59'da halat kayboldu" · "0:59 gizli kesme" (o bir SAHNE SINIRI) · "0 g mi?" — dördü de PLANDA YAZILI; ④'ün kesme listesi UYGULANMAZ (dört adaydan biri **S6 = NOVUM TAŞIYICISI + TEK KARE**). ⭐ **GEÇERSİZ PARTİDEN ÜÇ ÖLÇÜM SAĞ ÇIKTI [D121]:** şerit (7 mercek `1111111111111`) · replik (8 mercek 0) · **⑨ ızgara: 12 kesme planın 10 s ızgarasına oturdu, max |Δ| = 1,0 s → zaman kodları uydurulmamış — ve ızgara İLK 13 YUVAYA oturuyor: 14'üncü yuvada (S13 · final vuruş + twist + loop) BAŞLIK KARTI var.** 🔴 İki teslim kusuru adayı: başlık kartı (plan: ekran metni 0,0 s · kart 0 kare [D70/72]) ve 1:59-2:09'da dört merceğin bildirdiği İKİNCİ FİGÜR (SPEC: insan tam 1 · 14/14 · yansımada 0 · gölgede 0 — KART 4). **Kapatan iki komut film kaydında** (`olcum_kapisi.sh` + `ffmpeg -ss 64` TEK KARE). ⭐ **BU KOŞUNUN ÜRÜNÜ İKİ DERS — D165** (araç yazıldı, koşacak kart yoktu: QA paketi artık Kart A §4'te, filmin YAZIMINDA üretilir) **· D166** (novum'u olan film mod V'de ölçülemez: ⑥ PREMISE REGISTER'a filmin TÜRÜNÜ yazdı, KURALINI değil — ve paketin ⑥ süzgeci NOVUM'u Türkçe birim sözcüğü yüzünden zaten düşürüyordu; süzgeç KAYIT seçecek biçimde düzeltildi + `rapor_kontrol.py` ①.6 NOVUM kapısı eklendi, ⑥⑦⑧'de ateşledi, novum'suz filmde ateşlemedi); ikisi de bulgudan değil ALETTEN çıktı. Film kaydı: `01_FILM_RAPORLARI/THE_STILL_SWARM.md` · paket: `QA_PROMPTLARI/FILME_OZEL/THE_STILL_SWARM/` (8 dosya, üretildi). **YAZIM KAYDI (01.09.2026):** 2-4 dk · **VAKUM / serbest düşüş 0 g** (§3.1; deponun ilk 0 g 2-4 dk filmi) · 14 × 10 s = 2:20, **0 kesme**, 14/14 sabit lockoff, 3 viral ara (S7·S11·S13), **0 replik** — tamamen sessiz · **novum fiziksel yasa:** 40 m'lik enkaz kabuğuna giren her katı cisim hızının tamamını 0,15 s'den kısa sürede kaybeder ve bulunduğu yerde asılı kalır; etki-tepki çalışmaya devam ettiği için ilerlemenin tek yolu KÜTLE ATMAKTIR (gerçek fizik: Tsiolkovsky 1903 · SAFER 1994 · Kessler 1978 filmin TERSİNİ söyler ve açıklamada öyle yazılı) · NOVUM TAŞIYICISI 30 cm çelik kelepçe × geriye fırlatma jesti → TEK KARE S6 · 1:04, taşıyıcı kadrajın 1/7'si, rakip olay 0 kare [D157 ①②③ üçü de uygulandı] · ⭐ **TEMA: İLK TEMAS** — TEMA_MUHENDISLIGI §3c'de "hiç kullanılmamış" olarak kalan TEK tema; 4 sahne indeksi (S1 ölçek uyuşmazlığı · S7 yabancı ışık · S11 gövdenin donması · S13 avuç açılışı) · ⚠️ §4 süre-tatmin kuralına BİLİNÇLİ SAPMA (İlk Temas dikey sütununda listeli, bu film yatay): gerekçe üç maddeyle planda, panzehir sayısal (koda 2 sahne · başarısız deneme 2 · bedelli seçim 1) [D158 B2a/B2b] · metinsiz sayaç: kuşaktaki 8 kelepçe → 7 → 5 → 2 → 0, monotonik, ekran metni 0,0 s [KART 5 iki yönlü çözüldü] · doruk S11 = geldiği şeyi (güç hücresi) fırlatmak — bedel AYNI karede, paylaşım sahnesi HUŞU, ölçek 1:11 · final TWIST + LOOP; S0 ↔ S13 eş kadraj çifti **D153 protokolüyle** yazıldı (S13 imajı S0'ın ONAYLI karesinden image-edit ile türetilir, fark listesi tam 3 madde) · ⛔ **uzaylı ANATOMİ olarak 0 kare**: KART 2 (canlı, hiçbir filmde 5'i geçmedi) ve UZAY_SENARYO §3 uzay operası yasağı birlikte elendi — varlık yalnız kuralla ve S13'te 300 parçayı aynı anda tek yöne çevirmesiyle vardır; "creature/alien/swarm" hiçbir prompt gövdesinde geçmez · risk **4/13** (kask · ikinci figür · sayaç · parçacık; KART 12 ayrı sayıldı ve dört önlemin dördü de TELAFİLİ) · 7 kurulum / **6 açı tipi**, 2 bilinçli ölçek şoku · ✅ prompt_kontrol.py klasör modu: **0 BLOCK** · 28 prompt · ⑬ tema · ⑭ novum taşıyıcı · ⑮ sırt pozitif · ⑯ politika kapılarının dördü de GEÇTİ (T1 0 · şiddet fiili 0 · milliyet 0) · ⛔ SPEC AYRI DOSYA `THE_STILL_SWARM_QA_SPEC.md` — üretimden sonra **MOD D koşulacak** |
| **The Sinking Stake** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 02.09.2026 · 3-5 dk · 🆕 **AZOT KARI OVASI / YILDIZSIZ DÜNYA** — süper kütleli kara deliğin çevresinde ~30 r_s, zemin katı azot 44 K, atmosfer azot buharı ~15 µbar, 0,40 g, **rüzgâr 0 · sıvı 0 kare** (azotun bu basınçta sıvı fazı yok) · sahip talebi: *"karadeliğe yakın karla kaplı gezegen, iki astronot, full beyaz bol donanımlı kıyafet, beyaz modern uzay gemisi, bağlandıkları yıldızlararası gemi de beyaz"* · **25 × 10 s = 4:09** (9 s hook + 24 × 10 s), 0 kesme, 25/25 sabit lockoff, 4 viral ara (S8·S12·S16·S20), **0 replik** — tamamen sessiz; dış mekânda ses YOK (15 µbar ses taşımaz), duyulan her şey giysi içinden · **novum fiziksel yasa:** zemine bırakılan sıcak her şey karı doğrudan gaza çevirip kendi çukurunu kazar ve iner — hiçbir şey durduğu yerde kalmaz (gerçek fizik: Triton/Voyager 2 1989 ~38 K · Pluto/New Horizons 2015 ~44 K · azotun yüzey basıncında sıvı fazı yok · Europa buz kabuğu için tasarlanan termal probların iniş yöntemi) · **NOVUM TAŞIYICISI beyaz kazık ayağı × iki eldivenle bastırma jesti** → TEK KARE S0 · 0:04; taşıyıcı ECU'da kadrajın ~%40'ı, değişim TEK KLİP içinde, rakip olay 0 kare [D157 ①②③ üçü de uygulandı] · kural 7 sahnede 6 farklı nesneyle kanıtlanır · ⭐ **TEMA: ZAMAN** — *"Burada hiçbir iz kendi başına kalmaz; kalan her iz, biri onu orada bırakmayı SEÇTİĞİ içindir."* ⛔ §3c takas kalıbı DEĞİL (sebep cümlesi); 4 sahne indeksi (S3 nesne · S12 kinesik · S21 kamera · S24 ışık) · ⭐ **depoda İKİ İNSANLI ilk 3-5 dk filmi** — ve sahip "full beyaz" istediği için ayırt etme kanalı RENK DEĞİL GEOMETRİ (boy 188↔165 · göğüs boyunduruğu↔düz göğüs · dört cep↔sarılı halat); REFERANS_PAKETI bu yüzden yazıldı ve RK1↔RK2 için dört maddelik ayırt etme sınavı kondu · metinsiz sayaç: iniş bacağında GÖRÜNEN teleskopik kademe **3 (S4) → 2 (S11) → 1 (S18)**, monotonik; filmde ekran/kadran/gösterge CİHAZI HİÇ YOK → **KART 5 iki yönden de düşer** ve A1 çelişkisi yapısal olarak imkânsız · ⭐ **D158'in iki sayımı yazılı:** merkezi seçim S19 (3:09 — çekirdeği beşikten kaldırmak, bedel geminin tek yedeği) · **seçimden SONRAKİ seçim S22** (kazığı bilerek yatırıp sütunu gösteren hendek bırakmak) · koda 5 sahne · başarısız deneme 2 (S5-S6 plaka tutmaz · S12 dikilen kazık devrilir) · hook YANLIŞLIK KOMPOZİSYONU, katalizör 0:14 · tohum S3 · 0:31-0:33 (2 s, bakışla vurgulanmadan) → geri dönüş S16 · S24 · final **TWIST + tohum**: son karede İKİ sütun, ilk gelenler onlar değildi · ⭐ FİNAL VURUŞ KANITI **BULUNAN** [D141 · D76]: işaret bir DELİK değil, delikten çıkan DİKEY GAZ SÜTUNUDUR — 2 sütun + 1 hendek, 4:05'te sayılabilir · **14 kurulum / 5 açı tipi**, 2 bilinçli ölçek şoku (S19→S20 · S20→S21); ardışık her çift ≥1 kademe VE ≥45° azimut · eş kadraj çifti **YOK — bilinçli** [D153] · kir merdiveni 0 kademe (toz yok → D147 tetiklenmez → D155 riski yapısal olarak sıfır) · risk **7/13**, altısı malzeme çıkararak sıfırlandı (su fizikle imkânsız · canlı 0 · sayaç cihazı 0 · katmanlı dünya yok · diyalog 0 · sabit süre) · ⚠️ **beyaz üstüne beyaz** bu filmin kendi riski (giysi/kar/araç/gaz beyaz, tek kontrast siyah gök) → QA_SPEC E bloğuna filme özel **KAPI ③ KONTRAST KAPISI** yazıldı: her karede YMAX−YMIN ≥ 120, `signalstats` ile ölçülür; 120 px kapak testi HARD gate · ⭐ E bloğunun 4 makine kapısı **ffmpeg 8.1 ile 02.09.2026'da fiilen sınandı**; `vidstabdetect` bu makinede kurulu DEĞİL → kapı YAZILMADI, İKAME yazıldı [D142'nin ölçtüğü arızanın önlenmiş hâli] · ✅ prompt_kontrol.py klasör modu: **50 prompt · 0 BLOCK · 0 FIX · GO**; koşuda çıkan 9 bulgu düzeltildi (D123 `dead`/`blast`/`explosion` yığılması · D39 `swirl` · araç yönelim kilidi ×10 · çapasız `toward` ×4 · insan sayısı imzası ×30+) ve iki bilinçli sapma planın KAPI KOŞUSU bloğunda kayıtlı (kurulum 14 vs bant 13, üçü kapı zorunluluğu · video 1.704-3.374, tavan 4.300 aşılmadı, aritmetik gerekçe + ilk-red protokolü) · ⛔ SPEC AYRI DOSYA `THE_SINKING_STAKE_QA_SPEC.md` — üretimden sonra **MOD D koşulacak** · 🔧 **REVİZYON 1 (02.09.2026, sahip geri bildirimi: "sahne 4 ve sonrasında uzay mekiği çok kötü"):** araç tasarımı değişti ve **bedeli sıfır oldu** — üretilmiş dört sahnenin (S0-S3) hiçbirinde araç yoktu. İNİŞ ARACI dört bacaklı 9 m dikey araçtan **taşıyıcı gövde (lifting body) mekiğe** çevrildi: 14,0 × 9,0 m, kuyrukta yalnız 4,2 m, kanat ayrı parça DEĞİL — gövdenin kendisi kanat; küt burun, üç camlı dar pencere şeridi, iki yatık kanatçık, iki gömük sönük lüle, karından dört kısa strut (üç teleskopik kademeli sayaç KORUNDU). YILDIZLARARASI GEMİ 140 m omurgadan **kapalı halkaya**: kenar kenara on iki özdeş modül, 64 m çember, dördü radyatörlü ve 12/3/6/9 saat konumunda (yönelim kilidi). S4 kamerası 9 m → 4 m'ye indi, araç artık üçte iki profilden TAM BOY kadrajda. ⛔ **kopya sınırı korundu [MESHUR_SAHNE §4]:** sahibin referansı bir filmdi; film adı/marka/tescilli tasarım adı hiçbir prompta yazılmadı, tasarım GEOMETRİYE çevrildi ve gerçek donanıma bağlandı (NASA X-24A/X-24B · HL-10 · Dream Chaser · von Braun 1952 tekerlek · NASA Nautilus-X 2011) — kanalın "gerçek kural" tezi bozulmadı, YAYIN_PAKETI VERIFIED SCIENCE'a iki satır eklendi. ⚠️ dürüst kayıt: 15 µbar'da kanat işe yaramaz; bu bir çelişki değil, mekik seferin ATMOSFERLİ dünyalara da inen çok amaçlı aracıdır ve burada kanatları ölü ağırlıktır — filmin kuralıyla aynı cümle (hiçbir şey burada tasarlandığı işi yapamıyor); gerekçe planda, PROMPTTA AÇIKLANMAZ. ⭐ bedava kazanç **ÜÇ ÇEMBER MOTİFİ**: kara deliğin parlak halkası · geminin beyaz halkası · çekirdeğin açtığı yuvarlak ağız (10^11 : 10^2 : 10^-1; ilk ikisi S4 ve S23'te aynı karede). Yeni negatif kilitleri her araç sahnesinde: `the hull IS the wing — no bolted-on wings, no propellers, no rocket fins, not a tall vertical rocket` · `the distant ship stays a closed unbroken ring — no spine, no cylinder, no broken arc`. REFERANS_PAKETI RA 4→5 panel yeniden yazıldı (kabul sınavı: yandan oran 14:4,2 · üstten kanat gövdeden ayrı DEĞİL), RB 1→2 panel ve öncelik 🟡→🟠. ⛔ RA/RB onaylanmadan S4 üretilmez. ✅ revizyon sonrası prompt_kontrol.py klasör modu yine **0 BLOCK · GO**; koşuda ayrıca planın kendi başlığındaki bir arıza yakalandı (`### … VİDEO PROMPT …` başlığı betiğe planı prompt dosyası sandırıyordu — başlık yeniden adlandırıldı) · 🛑 **02.09.2026 · ÜRETİM YARIDA DURDU — FİLM KAPANDI.** 25 sahnenin ~14'ü üretildi; eksik 11 sahne ARDIŞIK ve filmin SONU (merkezi seçim S19 · doruk S21 · ikinci seçim S22 · twist S24 hiç üretilmedi). Durduran olay: 🔴 **yeni politika reddi** — motor **OMNI** · `"…can't depict some public figures"` · red defteri **vaka 15**. Tetikleyici ölçüldü: karakter bloğunda kişi başına YEDİ kimlik özniteliği (kesin boy · gövde · ten · saç rengi · saç biçimi · yüz işareti · yaş), iki kişide, 25 imaj promptunun 25'inde → "ünlüyü adını yazmadan tarif ederek isteme" kalıbı. ⛔ **8 mercek koşuldu ve 8'i de MOD V** → parti T tablolarına GİRMEDİ [D129]; sebep `QA_PROMPTLARI/FILME_OZEL/` paketinin hiç üretilmemesi [D165 · 2. vaka]. Mod V'nin bedeli ölçüldü: FİZİK ⑥ Ölçek **2/10** ve DEVAMLILIK ② Dünya Durumu **2/10** — ikisi de **filmin NOVUM'unu** (kazık kısalıyor) en büyük kusur diye puanladı [D166 · 2. vaka]. Mod V'yi SAĞ ATLATAN gerçek kusurlar: EFOR ⑧ **1,6/10 "NOBODY PAYS"** (4 efor olayı, 4'ünde de zorlanma sıfır — yazım kusuru, kendi belgemizden doğrulandı) · göğüs paketi S13'te değişti (referans paketi hiç üretilmedi) · S4/S10'da sabit kamerada İMKÂNSIZ yıldız izleri · iki yerçekimi [D154'ün öngördüğü arıza]. Sahip değerlendirmesi: *"hikayesi saçma sapan, ne mantıklı ilerleme var ne sahneler arası devamlılık"* — kaydedildi, skorla çürütülmedi [D158 emsali]. ⭐ **BU FİLMDEN ÜÇ DERS ÇIKTI: D167** (kimlik yığını → kapı ⑲) **· D168** (üretim sırası dramatik sıra değildir: doruk önce üretilir) **· D169** (0,40 g ağırlığı azaltır, ATALETİ azaltmaz → kapı ⑳). Ayrıca D165'in 2. vakası kapandı: kapı satırı AGENTS.md'de vardı, `yeni-film` SKILL dosyasında yoktu — eklendi. ⚠️ Film artık başka bir koşunun eklediği **⑰ B5 HİKÂYE OMURGASI** kapısından BLOCK alıyor (69 filmin 69'u alıyor) — o kapı bu koşunun ürünü değildir, susturulmadı. Kayıt: `01_FILM_RAPORLARI/THE_SINKING_STAKE.md` |
| **The Leaning Room** | 🚨 | 🚨 | 🚨 | 🚨 | **0/4** ⛔ **02.09.2026 · SEKİZ MERCEK KOŞULDU, PARTİ 🚨 GEÇERSİZ — 8/8 MOD V.** SPEC de QA paketi de VARDI ve aynı gün üretilmişti; operatör paketi değil çıplak rubriği yapıştırdı → `rapor_kontrol.py`: **8 rapor · 8 GEÇERSİZ · 0 GO** [D129 · **SPEC yazılıyken mod V koşulan film sayısı 9 → 10**]. ⭐ **⑪ ÖLÇÜM KAPISI KOŞULDU ve HAKEMLİK ETTİ** — master 4K/125,000 s/30 fps; kesme 11 ✅ sahne 12 ✅ ses kanalı VAR ✅ filigran YOK ✅, ve raporların kesme/sahne/replik eksenlerini DOĞRULADI. ⛔ **ÜÇ TESLİM KUSURU:** 🔴 kuyruk kartı 120,0-125,0 s (freezedetect + silencedetect ile makineyle doğrulandı; plan SCREEN TEXT 0,0 s der) [D70/D72'nin **10. vakası**] · 🔴 loudness **−32,0 LUFS** (kilit −14, 18 LU altında) [ihraç kilidinin 2. vakası] · 🔴 sekiz merceğin sekizi **24 fps varsaydı, dosya 30 fps** → hesapladıkları her süre %25 kaymış. ⭐ **ASIL BULGU — NOVUM EKRANA GELDİ, MERCEKLER GÖRMEDİ.** Kare 2280-2340 (1:16-1:18) çıkarıldı ve BAKILDI: sarkaç lamba altı karede kesintisiz, tek yönde, salınmadan yatıyor ve duruyor — kural çalışıyor. Üç mercek (① ③ ⑥) bunu *"an object falls diagonally UPWARDS, defying the established 1g"* diye 🔴 BLOCKER saydı; ⑥ ve ⑧'in PREMISE REGISTER'ı `Earth-normal 1g` yazdı → **D166'nın İLK TEKRARI** (mercek filmin türünü yazar, kuralını kusur sayar). ⑩ ÖNERME KAPISI'nda **yedi bulgunun beşi DÜŞTÜ**; ④'ün kesme listesi planın iki VİRAL ARA sahnesini (S4 · S9 · ⛔ KESİLEMEZ, ikisi de novumun insansız kanıt sahnesi) hedefliyordu ve UYGULANMADI. 1:55 karesi: pirinç gövdede **İKİ EZİK** yan yana, sayılabilir — D141'in FİNAL VURUŞ KANITI **BULUNAN**; dört mercek onu hiç anmadı ve ④ *"the ending stops"* yazdı [D151'in 3. vakası]. ⛔ **AYAKTA KALAN ÜRETİM KUSURLARI (kareyle doğrulandı):** 🔴 **novumun YÖNÜ ters** — S7'de lamba SCREEN-LEFT'e yatıyor, siyah daire SCREEN-RIGHT'ta, S9'da eşyalar SCREEN-RIGHT korkulukta → **YENİ DERS 174** (yön koordinata değil kadrajdaki NESNEYE bağlanır; D104'ün tersi) · 🔴 **taşıyıcının kordonu ayrı bir ÇEKME HALATINA döndü** (S3/S5/S8; S8'de pirinç karşı ağırlıklar takılmış) ve sekiz merceğin SEKİZİ filmi *"pulls ropes to shift the cosmos"* diye özetledi → **YENİ DERS 172** (rakip olay değil, taşıyıcının kendi ASKISI novumun yerine geçti) · 🟠 konsol morfu: düz pirinç çark ↔ parmaklıklı gemi dümeni → **D128'in tekrarı** (temalı sette jenerik ad arketipe çöker) · 🟠 S8 planın odası değil · 🟠 S0'da pencere yansımasında ikinci figür. ⭐ **VE BİR KAPI ARIZASI:** `rapor_kontrol.py` ⑤ ŞERİT kapısı çoğunluğu (`1111-1111-1-`, 4 mercek) doğru sayıp **tek DOĞRU merceği (① KARE, `1111-1111-11`) 🚨 sapan ilan etti**; 1:55 karesi ①'i doğruluyor (kadın odak dışı, arkada, kadrajda) → **YENİ DERS 173** (odak dışı figürde çoğunluk ortak kör noktayı paylaşır; sapma oyla değil KAREYLE çözülür). ⛔ TEKRAR KOŞUDAN ÖNCE ZORUNLU: kart kesilir · −14 LUFS yeniden ihraç · S7 yön düzeltmesiyle, S3/S5/S8 kordon düzeltmesiyle yeniden üretilir. Film kaydı: `01_FILM_RAPORLARI/THE_LEANING_ROOM.md` · ham raporlar `02_HAM_RAPORLAR/THE_LEANING_ROOM_1..8_*_HAM.md` · 2-4 dk · 🆕 **VAKUM + İTKİ YERÇEKİMİ — KABİN İÇİ DALI** (§3.5): dışarısı vakum (§3.1 aynen; toz/duman/alev/rüzgâr/sıvı/canlı 0 kare), içerisi basınçlı bir salon; ağırlık YALNIZ itkiden gelir → **D23 yapısal olarak tetiklenemez** · sahip talebi: *"12 sahne, lüks uzay gemisi, modern ve lüks giyimli kadın, karadelik ve gezegen yakın geçişleri, sadece seyahat, hep içeriden sürüş kamerası"* · **12 × 10 s = 2:00**, 0 kesme, 12/12 sabit lockoff, 2 viral ara (S4 · S9), **0 replik** — tamamen sessiz; dışarıda ses YOK, duyulan her şey gövdeden iletilir · ⭐ **kamera 12/12 sahnede geminin İÇİNDE — depoda dış mekânı 0 kare olan ilk film** · ⭐ **depodaki İLK KASKSIZ uzay filmi**: basınçlı kabin, kısa kollu; D5 (vizör kalıcılığı), D79 (sırt ünitesi) ve **ölçülmüş en net başarısızlık kartı KART 3** üçü birden tetiklenemez. Açtığı yeni risk dürüstçe kayıtlı: 120 saniye boyunca fotogerçekçi bir yüz ekranda (DIKEY_MIKRO_DRAMA §6.1'in ceza kutusu) — karşı önlem malzeme değil DUYGU REGİSTERİ: kadın kırılgan değil YETKİN, Character Bible'ın son cümlesi *"she is working, not enduring"* · **novum fiziksel yasa:** bu gemide "aşağı" zemin değil sürücünün ittiği yöndür — dönmek yana itmektir, yana itmek odayı yatırmaktır (gerçek fizik: hissedilen aşağı toplam ivmenin tersidir; şakül bir ivmeölçerdir ve ilk dönüş göstergeleri tam olarak böyle çalışıyordu) · **NOVUM TAŞIYICISI tavandan sarkan pirinç sarkaç lamba × kadının onu eliyle düşeye itip bırakması** → TEK KARE cümlesi taşıyıcının ADINI içeriyor [D157①]; taşıyıcı ECU kurulumunda kadrajın tamamı ve değişim TEK KLİP içinde [D157②]; iki kanıt sahnesinde (S4 · S9) kadrajda başka hiçbir şey hareket etmiyor [D157③] · kural 6 sahnede 3 nesneyle kanıtlanır (lamba · pirinç anahtar · kadının kendi ağırlığı) · **θ = arctan(yanal/eksenel) = 0° → 4° → 22° → 68° → 3°**, dördü de aritmetikle doğrulandı; 68°'de ağırlık seyrin **2,67 katı** ve bu gövdede okunur (koltuğa çöküş + kemer gerginliği) · ⛔ ivme değil SÜRE ve MESAFE yazıldı [D127]: S8'de anahtar göğüs hizasından, camdan 2,0 m uzakta bırakılır, cama **0,8 s**'de ulaşır ve yolda **0,8 m** alçalır · ⭐ **TEMA: ENTROPİ** — *"Bir oda bir kez düzeltilir; ikinci kez tam düzelmez."* ⛔ §3c takas kalıbı DEĞİL, geri alınamazlık cümlesi; 4 sahne indeksi (S2 nesne · S8 nesne · S10 kinesik · S11 nesne+ışık) ve **B2'nin bedel sahnesi S8 bu listede** · metinsiz sayaç ÜÇ KANAL ve **gemide 0 ekran · 0 kadran · 0 gösterge** — bilgi taşıyan tek şey sarkacın açısıdır: **dinlenme açısı 0°→0°→0°→3° MONOTONİK ve geri dönmez** · masadaki gevşek eşya 6→6→5→3→0→4 (iki eşya kanepenin altında kalıcı kayıp) · pruva camındaki halkalı varış nokta→okunur disk · ⭐ **D158'in iki sayımı planda:** merkezi seçim **S7 · 1:12** (dümeni sonuna açar, dar çizgiyi seçer) · **seçimden SONRAKİ seçim 2** (S10 üçüncü kütlede geniş hattı sürer · S10 sarkacı düzeltmemeyi seçer — elini altından geçirir, dokunmaz) · koda 4 sahne (3-5 bandının içinde) · **başarısız deneme 2** (S6 lambayı eliyle düşeye iter, bırakınca 0,9 s'de geri döner · S8 eşyaları toplamaya uzanır, parmak ucu yetişmez) · hook GÖRSEL ANOMALİ — ihlal 0. karede, saklanan şey ihlal değil SEBEBİ [D71]; katalizör **0:13** (≤0:15) · tohum S2 · 0:22 (lambanın gövdesindeki ESKİ ezik, ≤2 s, bakışla vurgulanmadan) → geri dönüş S11'de YENİSİYLE yan yana, yani final "bir kez bozdu" değil **"her seferinde bozuyor"** der · final **MUĞLAK** + görsel ikilem: oda düzeldi, gösterge düzelmedi · ⭐ FİNAL VURUŞ KANITI **BULUNAN** [D141]: 1:53'te kadrajda **2 ezik** sayılabilir (biri mat ve eski, biri parlak ve yeni) · açılış-kapanış çifti bilinçli KAPANIŞ KONTRASTIDIR, döngü değil (S0 oda + doğru gösterge ↔ S11 lamba + yalan gösterge) · **6 kurulum / 5 açı tipi**, dizi A-D-B-F-E-F-B-A-C-B-F-E, 1 bilinçli ölçek şoku (S6→S7 MS→EWS, merkezi seçim) · ⛔ **EKRAN YÖNÜ TEK KİLİT ve 12/12 sahnede geçerli:** kamera hiçbir sahnede kıça bakmaz, sancak penceresi 12/12 SCREEN-RIGHT, yatma 12/12 screen-right, ters dönüş 0 · eş kadraj **S2 ↔ S6 ↔ S9** (aynı B kurulumu) ve [D153] gereği S6/S9 imajları S2'nin ONAYLI karesinden ≤3 maddelik fark listesiyle image-edit ile türetilir · KART 6b ışık takvimi 12 satır yazıldı (kaynak her sahnede DEĞİŞİR çünkü kaynak yolun üstündeki kütledir; 11 ardışık çiftin 11'inde palet değişir) · KART 9 dört kanal S2 · S5 · S7 · S8 promptlarında · risk **7/13** — dördü her filmde açık sabit kart, üçü filmin omurgası; **iki 🔴 kart (su · canlı) ve KART 3 SIFIR** · ✅ **prompt_kontrol.py klasör modu: 24 prompt · 0 BLOCK · iki bölüm dosyası da GO**, video 24/24 bantta (2.206-2.603) · ⚠️ klasör seviyesindeki tek FIX **D79 ve YANLIŞ POZİTİFTİR**: film 0 kask taşır, kapı `kask/vizör` dizgesini yalnız PLAN'ın Türkçe "YOK" satırlarında görüyor (bölüm dosyalarında 0 kez geçiyor, `grep` ile doğrulandı) — gerekçe planın KAPI BETİĞİ bloğunda ve **kapıya "0 kask" kaçışı gerektiği GOZLEM_DEFTERI adayı** · ⛔ SPEC AYRI DOSYA `THE_LEANING_ROOM_QA_SPEC.md` + **QA paketi SPEC ile birlikte üretildi** [D165] — üretimden sonra **MOD D koşulacak** · 🎵 MUZIK ✅ (72 BPM, 10 s = tam 3 ölçü; S9 tamamen sessiz, S6'da 1:01'de müzik kesilir) · 📣 YAYIN_PAKETI ✅ tamamen İngilizce · ⏳ üretim yok |
| **The Pressed Field** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 03.09.2026 · 2-4 dk (10 sahne · 1:40) · ince atm. (§3.2 · 0,38 g) · ⭐ **`UZAYLI_VARLIK_TASARIM_KILAVUZU`nun İLK UYGULAMASI ve deponun uzaylı varlık içeren ilk filmi** — varlık K0-K1 kademesinde, gövde/uzuv/gölge **0 KARE** (KART 2'nin bozulma mekanizması yapısal olarak elendi) · tema **İLK TEMAS** · novum fiziksel yasa: geçilen yerde toz kalıcı olarak taşa sıkışır ve sıkışma yayılır; tek kare kanıtı S6 (iki özdeş çubuk, biri dize kadar gömülü öteki yüzeyde ve ucu bükülmüş) · doruk S7 = kendi ölçüm hattını SÖKÜP uyarı halkası yapmak (bedel aynı sahnede) · final vuruş kanıtı BULUNMAYAN nesnedir: 94,0 s'de kadrajda bot izi **sıfır**, S0'da aynı kurulumda **iki** idi · 10 × 10,0 s, 0 kesme, 0 replik, 10/10 lockoff, ekran metni 0,0 s · risk 7/13 (ayrıştırması planda) · ⭐ depoda ilk kez **PLANTED DETAIL** (bilinçli tohum) kilidi yazıldı, S1 · 13,5-15,0 s · ✅ prompt_kontrol.py klasör modu **GO — 0 BLOCK / 0 FIX** (20/20 prompt) · ⛔ SPEC ayrı dosyada + QA paketi PAKET_1..8 yazımla aynı gün üretildi [D117 · D165] |
| **The Standing Wire** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 05.09.2026 · 3-5 dk · İNCE ATMOSFER (§3.2 · 0,42 g · ~1,0 kPa · adsız gezegen, 9 km'lik yarık + masif rafı) → VAKUM (§3.1) → **BASINÇLI İÇ HACİM (§3.10 — deponun bu kartla yazılan İLK filmi)** · sahip talebi: *yatay 3-5 dk · gezegende başlasın · dev dağları ve kanyonları olsun · yıldızlararası uzay üssüne yanaşma olsun* · **YAZIM PAKETİ TAM: PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC [§2.0 yedi dosya · D117]** — 25 sahne (13+12) / 50 prompt (25/25 I2V) / 9 + 24×10 = **249 s = 4:09** (§2.3 kartını izler; klasör README'si 24 der, çelişki depoda duruyor ve bu film KARTI seçti) · novum FİZİKSEL YASA, gerçek mühendislik: **bu telin gerilimi yukarıdandır ve nettir** — ona bağlanan her şey yükselir, bağlı olmayan her şey 0,42 g ile düşer (uzay asansörü mekaniği · Tsiolkovsky 1895 · Artsutanov 1960 · Pearson 1975) · taşıyıcı **TEL × kadının ona bir cisim asması**, TEK KARE testi aynı nesneyi adlandırır [D157] · **TEMA: UMUT** — depoda 2. kullanım ve §4'ün YATAY bandındaki ilk kullanımı; sapma gerekçesiyle kayıtlı [D74] (§4 UMUT'u dikey sayar; bu filmde UMUT sürecin ÖDEMESİ, tutulan durum değil) · tema cümlesi TAKAS KALIBINDA DEĞİL [§3c] · 4 sahne indeksi (S11 yandan sıcak sızıntı · S17 avucun açılışı · S19 başın ışığa dönüşü · S24 ışık eldivenin üstünde) · **metinsiz sayaç: telin kesik ucu ↔ göz hizası farkı**, monotonik, S9'da başabaş geçer · CENTRAL CHOICE **S17**: üzengiyi iki elle tutmak için yıllar önce kendi sardığı tel halkasını bırakır — bedel aynı karede, S24'te boş askıyla ikinci kez ödenir · doruk **S22 · TEMAS 6,0 s = 225,0 s** (formülle hesaplatıldı [D122]) · kenet S23 tam 4 kelepçe, üçüncüsü yarım saniye duraksar · yanaşma seti V1·V2·V5·V6 — **V3 oran karesi ve V4 kapı vuruşu YOK ve ikisinin de gerekçesi yazılı**: iki gövdeli geniş kare 0 kare [KART 4 · D32], taşıyıcının motoru olmadığı için 'motorların karardığı an' yapısal olarak yok · ⭐ **0 motor · 0 nozzle · 0 egzoz · 0 alev · 0 kalkış** — KART 6'nın en pahalı kolu ve D148 yapısal olarak kapandı · TAM SESSİZ (insan 0 · makine 0 · telsiz 0) · insansız 2 sahne (S21 · S23, KART 10 reçetesi uygulandı ve maliyeti kayıtlı) · 25/25 lockoff · 0 kesme · 4 viral (S3·S12·S17·S18, dördü de YÜZ+HAREKET ölçütünü taşır [§2.4]) · açılış-kapanış KAFİYE çifti S0↔S24, değişen tek değişken telin çizgisi (düz → tek kavis) · final TWIST + tohum: S2'de barakada tek BOŞ ASKI (2 s, periferik) → S24'te altı askı, beşi dolu · risk **8/14** eşiğin üstünde, kabul edilmiş maliyet ve azaltma turu yazılı · 🎵 MUZIK ✅ (48 BPM · 10 s = tam 2 ölçü · ızgara sıfırı 9,0 s · **KURGUDA HARD MUTE 214,0-239,0 s** ızgaradan hesaplatıldı ve üç eşikte ölçülecek [D180]) · ✅ **prompt_kontrol.py KLASÖR MODU: 0 BLOCK · film klasörü GO** (ilk koşu BLOCK verdi; B5 · tema indeksi · novum taşıyıcı · ⑮ sırt · ⑱ yönelim · ⑯ politika · metin kapsamı · ⑧ efor kapılarının hepsi kapatıldı — kayıt PLAN 📏) · açık kalan tek uyarı S21/S23'ün negatif çekirdeği ve o KART 10'un REÇETESİDİR · ✅ **QA PAKETİ ÜRETİLDİ** `QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8` [D165] · SPEC E bloğu: 7 makine kapısı, beş ffmpeg filtresi + ffprobe **8.1 ile kuru koşuda DOĞRULANDI** [D142] · ⛔ SPEC AYRI DOSYA — **MOD D koşulacak; mod V koşulursa satır YAZILMAZ [D129]** · 🎬 **ÜRETİLDİ 05.09.2026 · QA KOŞULDU · 🚨 PARTİ GEÇERSİZ** → `01_FILM_RAPORLARI/THE_STANDING_WIRE.md`. Sekiz mercek (Gemini, tek oturum), sekizi de mod V [D129] **ve** master ÜRETİCİ FİLİGRANI taşıyor (6/6 örnek, ölçümle doğrulandı) [D150 5. vaka · D177 kapısı ilk kez ATEŞLEDİ] → hiçbir satır T tablosuna girmez, hiçbir reçete uygulanmaz. ⑪ ÖLÇÜM: **245,141 s / 24 klip** — plan 249,0 s / 25 klip; hook kırpması (10→9 s) yapılmamış, **bir klip eksik** (insansız yanaşma vuruşu — şeritten okundu: plan `…1-1-1`, ekran `…1-11`) [D118 · D163]; kuyrukta **5,0 s başlık kartı** (ekran metni kilidi 0 s) [D70/D72 12. vaka]; **−35,5 LUFS** (kilit −14); planlı hard mute 214-239 s TESLİM EDİLMEDİ [D180 2. vaka, ilk ölçülmüş]. ✅ EKRANDA TUTAN: final vuruşu (askılar, sonuncusu BOŞ · 236 s), novum kapanışı (tel S24'te sarkıyor), sırt ünitesiz düz siluet [D79], tek insan. ⛔ EKRANDA DÜŞEN: vizör **KUBBE** çıktı (SPEC: tek düz panel) [D146 3. vaka → ⛔ ÇALIŞMIYOR + dönüştürme borcu]. 🔴 YENİ DERSLER: **D183** (ham zincir master değildir) · **D182** (sayılabilir nesne dizisi "kalabalık" değildir — filmin twist'ini 8/8 mercek saymadı, ② onu kusur sanıp silmeyi önerdi). Ayrıca ADAY-10 (0 replikli filmde 4 cümle, bantla ölçüldü, KULAKLA kapanacak) ve ADAY-11 (yazılı zorlanma kanalı ekranda yok). ➡️ SIRA: master yeniden ihraç → kart kes → eksik klip → hook kırp → mute aç → 0:50-1:00 dinle → QA mod D tekrar |
| **The Kept Light** | ❌ | ❌ | ❌ | ❌ | **0/4** 🆕 06.09.2026 · 3-5 dk · **VAKUM (§3.1) + §3.5 alt kartı (ASILI/STATİK YERÇEKİMİ)** — üs bir kayanın ALT yüzüne asılı, kayanın uzak yüzündeki motorlar onu bir kara deliğin üstünde SABİT tutuyor; statik gövde tam yerel ağırlığı hisseder (0,40 g) ve motorlar hiçbir karede kadrajda değil (0 alev · 0 egzoz · 0 kıvılcım). ⛔ §3.10 TETİKLENMEZ: üssün İÇİ de vakumdur, kask 25/25 kapalı, havadan taşınan ses 0 kare · sahip talebi: *"karadeliğin yanında bir üste geçen 25 sahneli bir film"* · **YAZIM PAKETİ TAM: PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC [§2.0 yedi dosya · D117]** — 25 sahne (13+12) / 50 prompt (25/25 I2V) / 9 + 24×10 = **249 s = 4:09** (§2.3 kartını izler; klasör README'si 24 der, çelişki depoda duruyor ve bu film KARTI seçti) · novum **FİZİKSEL YASA**: kapağın altına bırakılan hiçbir şey düşmesini BİTİRMEZ — her nesne aynı yönde inmeye devam eder, indikçe daha az iner, ağır olan durmadan önce daha çok yol alır, ve aşağı giden hiçbir şey yukarı gelmez · taşıyıcı **KELEPÇE × eldivenli avucun kapak ağzında açılması**, TEK KARE testi AYNI nesneyi adlandırır [D157] · ihlal sayısı 1 ve gerekçesi ekranda hiç söylenmez · **TEMA: ZAMAN** — *"Burada hiçbir şey geçmişe geçmez; bıraktığın her şey bugünde kalır ve birikir."* ⛔ takas kalıbı DEĞİL [§3c] · 6 motif sahnesi (S1 nesne · S10 kamera+ışık · S15 nesne · S19 kinesik · S21 ışık · S24 nesne+ışık) ve **B2'nin bedel sahnesi S21 bu listede** · ⚠️ DÜRÜST KAYIT: ZAMAN'ı 02.09'da THE SINKING STAKE de kullandı ve o da bir kara deliğin yanında geçiyor — etiket aynı, CÜMLE ZIT (orada hiçbir iz kalmaz, burada bırakılan her şey kalır); iki film aynı temanın iki ucu ve bu bilinçli · **metinsiz sayaç ÜÇ KANAL, 0 ekran · 0 kadran · 0 gösterge**: çerçevede kalan kelepçe 5→4→3→2→1→0 (her D kurulumunda SAYILABİLİR [D78]) · ağzın altındaki yeni parlak nesne 1→2→3→4→5→6 · modülün yatma açısı düz→tek köşe; üçü de monotonik ve geri dönmez · **CENTRAL CHOICE S19 · 3:09** (son kelepçeyi keser, aşağıdaki tek ışığın hattı o pimden geçmesine rağmen) → **BEDEL S21'de EKRANDA** (209-219 s: lamba çok aşağıda, konisi öteye bakıyor, arada asılı hiçbir şey aydınlanmıyor) · başarısız deneme 2 (S16-S17 hattı çeker, bir parmak yükselmez · S18 halkayı pimin başından geçiremez) · **seçimden SONRAKİ seçim 2** (S22 sapı bırakmaz · S23-S24 kendi lambasını bırakır) [D158] · ⭐ **DRAMATİK İRONİ — deponun bu aracı bilerek kullandığı ilk yatay filmi**: taşıyıcı ① ARKA PLAN OKUR, asimetri anı 0:31 (tohum), derinleşme S13, kapanış S14; panik kare sayısı 0 [HOOK §3.1] · **0 replik** (insan 0 · makine 0 · telsiz 0) ve gerekçesi üç maddeyle yazılı — "en güvenli" iddiası DEĞİL [KART 7'nin 02.09 kaydı] · **insansız sahne 0** → KART 10 yapısal olarak tetiklenmez · **KART 9 SIFIR**: kadrajda uzak/baskın tek ışık yok, iki yatak lambası PRATİK ve TEPEDE, bekçi hiçbir sahnede bir ışığa doğru yürümez · 25/25 lockoff · 6 kurulum / 5 açı tipi · **KURULUM İSKELETİ yazılı** (A E D C C D C B C D F D C D C B C C B C E E D C A) → **küme 3/2 ✅ · dönüş %60/40 ✅** [ACI_YAYI §3 🕰️ · §4b — deponun bu satırı yazan İLK filmi] · bilinçli şok 2/2 (S0→S1 kozmik keşif · S19→S20 doruk) · açılış-kapanış **KAFİYE** çifti S0↔S24, konum kilidi tutuyor, değişen tek değişken **avuçtan çıkan şey** (eskimiş kelepçe → bekçinin kendi YANAN lambası) · final **TWIST + tohum** (tohum S3 · 0:31 · 2 s · bakışla vurgusuz → S14'te bulunur, S15'te makroda ödenir) · **FİNAL VURUŞ KANITI BULUNAN [D141]: 4:07'de ağzın altında ALTI parlak nesne sayılabilir** (beş kelepçe + lamba; sap sayıya girmez) · risk **9/14** eşiğin üstünde ve dürüst okuması yazılı (dördü sabit kart · üçü filmin omurgası · iki 🔴 kart SIFIR: su ve canlı) · 🎵 MUZIK ✅ (72 BPM · 10 s = tam 3 ölçü · müziksiz sahne S0 · S1 · S21 · **KURGUDA HARD MUTE 209,0-219,0 s** ızgaradan hesaplatıldı ve üç eşikte ölçülecek [D180]) · 📣 YAYIN_PAKETI ✅ tamamen İngilizce · ✅ **prompt_kontrol.py KLASÖR MODU: 50 prompt · 0 BLOCK · film klasörü GO** (ilk koşuda 2 BLOCK vardı — çıplak-deri negatifinin "above the collar" ibaresi satır sonunda BÖLÜNÜYORDU ve ㉑ kapısı 2/3 bölge sayıyordu; ayrıca ⑳ zorlanma · yön çapası · ⑯ politika yoğunluğu kapatıldı) · ⚠️ **açık kalan tek uyarı BİLİNEN YANLIŞ POZİTİFTİR**: dosya modunda ⑩④ iskeletin 25 harfini bölüm dosyasının 13/12 promptuyla karşılaştırıyor — bölünmüş filmde kaçınılmaz, geçerli koşu KLASÖR MODUDUR · ✅ **QA PAKETİ SPEC İLE BİRLİKTE ÜRETİLDİ** `QA_PROMPTLARI/FILME_OZEL/THE_KEPT_LIGHT/PAKET_1..8` [D165] · SPEC E bloğu: 5 makine kapısı, ffmpeg **8.1 ile kuru koşuda DOĞRULANDI** [D142] · ⛔ SPEC AYRI DOSYA — **MOD D koşulacak; mod V koşulursa satır YAZILMAZ [D129]** · ⭐ **06.09.2026 — FİLM ÜRETİLDİ, KURGULANDI, ÖLÇÜLDÜ.** master `~/Downloads/the kept lıght (1).mp4` · **255,133 s · 3840×2160 · 30 fps · ses VAR** (ikizi 720p, AYNI süre → aynı kurgu, ihraç kilidini tutmayan kopya) · gövde **250,13 s = 25 × 10,0 s** + 5,0 s kuyruk kartı · **SEKİZ mercek koşuldu, sekizi de MOD V** — ⛔ PAKET_1..8 KLASÖRDE DURUYORDU ve operatöre VERİLMEDİ: D165 "paket yoksa çıplak rubrik yapıştırılır" diyordu, burada paket VARDI ve yine çıplak rubrik yapıştırıldı → **SPEC + PAKET varken mod V koşulan film: 14** · `rapor_kontrol.py` (⑪ bayraklarıyla): **🚨 8 GEÇERSİZ · 0 GO** → **HİÇBİR SATIR HİÇBİR T TABLOSUNA GİRMEDİ** [D129 + D150] · 🔴 **DÖRT TESLİM KUSURU:** filigran ▷ sağ altta **6/6 örnek** [D150 · 5. vaka] · kuyrukta **5,0 s yanan başlık kartı** (donmuş 250,1-254,9 · kapak görseli + "THE KEPT LIGHT") [D70/D72 · 12. vaka] · **PLANLI MUTLAK SESSİZLİK TESLİM EDİLMEDİ** — 209-219 s bandında ÜÇ eşikte de (−50/−40/−30 dB) sessizlik YOK; dosyadaki tek aralık 176,5-178,4 s [D180 · TEKRAR 2] · loudness **−16,4 LUFS / +0,9 dBFS** (kilit −14 / −1,0 → true peak KIRPIYOR) · ⚠️ **KIRPMA TABLOSU uygulanmamış**: S0 10,0 s ham → 9,0 s kurguda yazıyordu, 10,0 s ihraç edildi → bütün ızgara sabit **+1,0 s** kaydı · ⭐ **SAĞ ÇIKAN ÜÇ ÖLÇÜM [D121]:** İNSAN ŞERİDİ `1111111111111111111111111` plana BİREBİR (25/25) — ② ve ⑦ iki yuvaya yanlış `-` koydu, ölçüm düzeltti · IZGARA 25 klip × 10,0 s, sahne düşmemiş · **FİNAL VURUŞ KANITI TESLİM EDİLDİ [D141]: 248,0 s`de ağzın altında ALTI parlak nesne SAYILDI** (beş kelepçe + bekçinin YANAN lambası) — filmin twist`i ekranda var · ⛔ buna karşılık **KAFİYE ÇİFTİ BOZUK**: S0 tepeden CU (kurulum A), S24 ağzın ALTINDAN alt açı → aynı kurulum/ölçek değil; üstüne kuyruk kartı çifti ikinci kez öldürdü · ⭐ **⑩ ÖNERME KAPISI — HEM DÜŞÜRDÜ HEM AÇTI:** ⑥ FİZİK`in `TWO GRAVITIES` hükmü DÜŞTÜ (PREMISE REGISTER `none`; novum SPEC`te yazılı [D166 · 4. vaka]) ve ⑥`nın hücrelerinin çoğu kaynaksız kaldı → `—`. **AMA aynı kapı novumun SINIR cümlesini sordu ve sınır KIRIK çıktı:** SPEC "kapağın ÜSTÜNDE bırakılan alet güverteye ÇARPAR" diyor; 65-69,9 s kare adımlamasında bırakılan kesici **~3 saniye havada kalıp güverteye hiç çarpmadan yatayda kayıp ağza giriyor** → SPEC`in "İHLAL SAYISI: 1" kilidi kırıldı. **Bu bulguyu sekiz merceğin hiçbiri yazmadı; ⑥ en yakınına geldi ve YÖNÜ TERS yazdı ("drift up").** → **DERS 183** · ⭐ **④ HİKAYE 4,5/10 — sayı düşer VE TEŞHİS DE DÜŞER (Healing Ground`un tersi):** rapor 24 kesme SAYDI ama 25 sahneyi **7 bloğa** ezdi (rubriğin kendi "iki kat" kuralını 6 kat aştı) → merkezî seçim S19 ile bedeli S21 aynı blokta boğuldu, "protagonist gives up nothing" ve "no low point" cümleleri o ezilmiş haritadan çıktı, final "pencereden bakıyor" diye okundu. Kesme listesinin iki adayının ikisi de kilide çarpıyor: birinci blok **S4 (KESİLEMEZ)**, ikinci blok **S19 (DORUK + VİRAL, KESİLEMEZ)** → ⑩`da DÜŞTÜ. ⛔ **KESME LİSTESİ / REMOVE REÇETESİ / YENİDEN ÜRETİM SİPARİŞİ UYGULANMADI** [D129] · ⑤ ARKA PLAN`ın iki çevre bulgusu KAREYLE DOĞRULANDI (45 s`de sol üst duvar KAYA + sağ duvara cıvatalı TEK koni lamba; komşu karelerde düz metal + tavanda İKİ disk) → S4 yeniden üretilir · ⚠️ ⑤ ARKA PLAN 20/20 sahnede "EDGES: Clean" yazdı; kadraj kenarı KENDİ mülkü ve orada filigran duruyor → 9. kategorisi kareyle yanlışlandı (D162`nin TERSİ: sahibi ① konuştu, komşu tersini söyledi) · ② kilit defteri **14 madde · 10`u KAREYLE KAPANDI (5 FİLM SAPTI · 3 RAPOR UYDURDU · 2 çevre) · 4`ü ⬜ AÇIK** · ⛔ Sıradaki iş: master **filigransız + kartsız + hook kırpmalı + 209-219 hard mute + −14 LUFS/−1,0 dBTP** yeniden ihraç · **S24 · S4 · S6 (66-70 s)** yeniden üretim · sonra sekiz mercek **MOD D**. Film kaydı: `01_FILM_RAPORLARI/THE_KEPT_LIGHT.md` · ham raporlar: `02_HAM_RAPORLAR/THE_KEPT_LIGHT_*_HAM.md` (8 dosya) |
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

# 🛰️ 7-20 dk — 3 film (1 ✅ / 2 ❌)

> ⚠️ **04.09.2026 · kart H2 — İKİ BÖLÜM BİRLEŞTİ.** `yatay_7_9_dk_filmler/`
> kaldırıldı ve bandı 10-20 kartına katıldı (`KILAVUZ_REHBERI` §2.4 → §2.5).
> THE_SLOW_STONE satırı buraya taşındı; klasörü artık
> `yatay_10_20_dk_filmler/THE_SLOW_STONE/`.
> ⛔ **THE_WAKING_GROUND satırı SİLİNDİ** — o film depoda hiç yoktu, yalnız
> adı geçiyordu (§2.4 dürüst kaydı, 21.08.2026). Boş satır bir borç gibi
> duruyordu; olmayan filmin ❌'i ölçüm açığı değildir.

| | Film | Kapsam | Skor | Ders | Dosya |
|:--:|---|:---:|:---:|:---:|---|
| ✅ | THE_SLOW_STONE | Full ×4 rapor | 5/10 | 2 | 🪨 bandın **kısa ucu** (48 × 10 s = 8:00) ve bu hattın **tek üretilmiş filmi** · [→](01_FILM_RAPORLARI/THE_SLOW_STONE.md) ✅ tam rapor |
| ❌ | YERCEKIMI | yazım sürüyor · **skor yok** | — | — | 🆕 28.08.2026 · 120 sahne × 8 s = 16:00 (format varsayılanı, 10 s sapması alınmadı) · `00_PLAN.md` + `README.md` ✅ · **29.08: S1-S60 — filmin TAM YARISI yazıldı. `FAZ_01_GOREV/` S1-S12 ✅ + `FAZ_02_DALGA/` S13-S24 ✅ + `FAZ_03_HALAT/` S25-S36 ✅ (perde dönüşü 1) + `FAZ_04_FEDA/` S37-S48 ✅ (feda %35,0 · viral ara #2 · ölçek 1:10 · ilk kasksız kare + ilk oda tonu) + `FAZ_05_ISTASYON/` S49-S60 ✅ (ORTA NOKTA %50 sahte zafer · filmde ilk kez HAVA: 12/12 oda tonu · Çehov 6 ekildi) + `FAZ_06_KAPSUL/` S61-S72 ✅ (**filmin TEK Overview sahnesi S68** · viral ara #3 · Çehov 1 ödendi · filmin en dar fazı: 12 sahnenin 11'i CU ya da daha yakın, tek geniş plan Overview'un kendisi) + `FAZ_07_SES/` S73-S84 ✅ (**PERDE II KAPANDI** · işaretli halüsinasyon · CENTRAL CHOICE + perde dönüşü 2 tek çekimde · müzik 0/12) + `FAZ_08_AYRILIS/` S85-S96 ✅ (Perde III · **dalga 2 + ŞOK BANDI 1** · mutlak sessizlik bıçağı · Çehov 5 ve 6 ödendi) + `FAZ_09_DUSUS/` S97-S108 ✅ (**İMZA ÇEKİM S102 YERÇEKİMİ YAĞMURU + ŞOK BANDI 2** · giriş alevsiz, yalnız renk ve titreşim) + `FAZ_10_ZEMIN/` S109-S120 ✅ (**S117 SAAT KURULUR — Çehov 2 ödendi, TEMA tamamlandı** · S118 alt açı filmde ilk ve tek · **S120 held frame**); **onu da prompt_kontrol GO — 120/120 SAHNE TAM** (24×10 prompt, 0 BLOCK; F3 İLK koşuda GO; kurulum üst bandı NOT'u gerekçeli [D74]) · `REFERANS_PAKETI.md` ✅ (6 sayfa × 4 panel — Uphill Dark biçimi; sağlam↔hasarlı çiftleri aynı sayfada; RC p3 klon kapısı; **RG p4 takvimi F5'ten F4'e çekildi** — S48 iç mekândır, eski takvim yanlıştı) · ⭐ klasör düzeni **FAZ_NN_AD/** (Second Ship emsali; format kartının PERDE_N/ düzeninden bilinçli sapma [D74]) · README'de özel ad (S21/S47/S78 "Arat") repliklerden ÇIKARILDI [D34]** · ⚠️ **F4 yazılırken FİZİK DÜZELTMESİ: istasyon dönüşü 2°/s → 6°/s.** Feda fiziği hesaplandı ve sayı yetmedi: 2°/s'de 12 m halatın ucundaki 120 kg'a düşen merkezcil kuvvet ~2 N'dur (≈200 g) ve bir halat katını bottan sökmez — o sayıyla sahne, kopyalanmayacağı yazılı olan Gravity ihlalinin ta kendisi olurdu. 6°/s'de ~16 N sürekli çekiş çıkar; aynı kuvvet gövdeye yakın olan A'ya ~2 N düşer → **feda karakterden değil KONUMDAN doğar.** Hiçbir prompt değişmedi (promptlarda rakam zaten yasak); halat sayacı da 3→2→1 yerine **3→2→tutar** oldu: kalan iki katın tutması B'nin hesabının kanıtıdır · ⚠️ **F5 bir PLAN ÇELİŞKİSİNİ kapattı** (yazım kapısının kurala karşı çalıştığı ikinci vaka): 00_PLAN §Faz 5 "S55: A çağrı yapar, statik döner" diyordu; 00_PLAN §Kadro ise "kasksız sahnede replik 0" der ve S55 kasksızdır. İkisi aynı anda doğru olamaz. **Çağrı kaldı, ses gitti:** A telsiz düğmesine iki kez basar — telsizde bu "orada mısın?" demektir ve cevap gelmez. Kural kurtarıldığı gibi sahne de büyüdü, üstelik S76-81 halüsinasyon fazına bir tohum bıraktı · ⚠️ **betiğin ikinci dil kuralı öğrenildi:** yasak kelime bağışlaması YALNIZ olumsuzlama bağlamında ve 40 karakterlik pencerede geçerlidir — `nothing swirls` bağışlanmaz, `never swirls` bağışlanır (\bno|not|never|zero|without\b); beş cümle yeniden yazıldı · ⚠️ **D79 kapısı kasksız bir fazda da çalıştı** ve gerçek bir eksik buldu: dosyada "helmet" geçiyordu (kasksızlığı anlatmak için) ama vizör cümlesi yoktu; kask S49'un arka planına kondu (boş, odak dışı, dönerek) — hem kapı kapandı hem S48'den süreklilik kazanıldı · ⭐ **F6'da bir FİZİK HATASI FAZIN EN İYİ FİKRİNE DÖNDÜ** — depoya yazılmaya değer vaka: taslak S62'de "eller kucağa DÜŞER (0g'de yavaş)" diyordu. 0g'de el düşmez; serbest bırakılan kollar nötr duruşa, göğsün önüne YÜKSELİR. Düzeltme sahneyi kurtarmakla kalmadı, anlamını verdi: **A çökmek ister ve bedeni izin vermez** — ellerini kucağına bastırır, eller geri kalkar, iki kez dener, üçüncüde denemez. Filmin adı YERÇEKİMİ'dir ve burada onun eksikliği bir DUYGUYU imkânsız kılıyor · ⚠️ **Overview'un ölçek maddesi iç mekânda uygulanamaz ve bu yazıldı** [D74]: UZAY_SENARYO §8 "karakter karenin 1/20'si" der, ama S68 2,4 m'lik bir koninin içinde geçer ve hiçbir iç kadraj bunu veremez. Karşıtlık figür-kare değil **MEKÂN-PENCERE** kuruldu: kadrajın tamamı loş dar bir kutu, içinde otuz santimlik bir delik, o delikte bir gezegen — pencerenin küçüklüğü sahnenin içeriği. Diğer dört madde (hareketsizlik · sessizlik · geriye bakış · süre) birebir; filmin literal 1:10 kareleri zaten S1/S45/S115/S120'de · ⚠️ **araç yönelim kapısı iç mekânda da çalıştı**: kapsülün iç coğrafyası (kapak sağ, lomboz sol) Türkçe kilitlerde yazılıydı ama İNGİLİZCE prompta hiç girmemişti · ⚠️ **F7'de README ile Bible ÇELİŞTİ ve kural ① uygulandı**: F7 tablosu S84'te "halka yanıp sönerek DOLAR" diyordu; Equipment Bible'ın oksijen takvimi S84'ü **1/6**, MACHINE zinciri **%6** diyor. Halka dolamaz — açılan AKIŞTIR, seviye değil. Tablo düzeltildi (sayı tek yerde yaşar) · ⭐ **bir KISIT fazın en iyi sahnesini verdi (S82)**: kask takvimi "kasksız sahnede replik 0" der, yani A halüsinasyona CEVAP VEREMEZ. Kısıt doğru karar çıktı — ölüyle konuşan karakter halüsinasyonu gerçek sayar, konuşmayan onu KULLANIR; dudaklar açılmaya yeltenir, açılmaz, cevap parmakların bacakta sayması olur · ⭐ **halüsinasyon meşruiyeti üç kanaldan işaretli**: miks (ses hoparlörden değil, filtresiz, her yönden) · **görüntü (S77: kamera sesin kaynağına gider ve kaynak boştur)** · gövdesizlik (B ekranda 0 kare) · ⚠️ **D138 kapsam kalıbı BİREBİR yazılır**: "on any display, PANEL, surface, patch or sign" araya kelime soktuğu için kapıyı geçmiyor; doğrusu "on any display, surface, patch or sign" · ⚠️ depoda ilk kez bir video promptu bandın **ALTINA** düştü (S73 = 1.952): fazın en sessiz sahnesi, sekiz saniyede tek nefes — uyarı haklıydı, 0g durağanlık kilidi eksikti · ⭐ **30.08 DENETİMİ VE TOPLU DÜZELTME — depoda ilk kez bir film yazım ortasında derslere karşı ölçüldü:** 84 imaj + 84 video promptu LESSONS_LEARNED ve kılavuzlara karşı sayıldı, yedi boşluk bulundu ve altısı aynı gün kapatıldı. **COMPOSITION bloğu 0 → 84/84** (lockoff bir filmde kadrajı kontrol eden tek araç; emsal THE HEAVY SIDE — "ekran-sol" yön verir, konum vermez) · **D127 sayısal hareket**: "sabit hızla" 76 kez yazılıydı, sayı 3 kez → 31 sahnede hareket **kadraj oranı + süre** olarak yazıldı ("kadrajı altı saniyede geçer"), ve bu çeviri İKİ TUTARSIZLIK ortaya çıkardı (S52 ve S63'ün lomboz beat'leri 6°/s ile çelişiyordu — düzeltildi; S68 Overview hesapla DOĞRULANDI: cam 7,4° görüyor, Dünya diski 140°, yani camda 23 saniye kalıyor) · **D146 vizör**: 51 kaskın 51'i ölçüsüzdü → düz dikdörtgen ön cam 24×16 cm + görünür metal çerçeve · **D139 sırt**: 67 yokluk kilidi vardı, pozitif tarif 1, kamera 33 kez arkadaydı → sırt pozitif tarifle yazıldı · **D123**: 0 kare gözyaşı taşıyan filmde "no tears" 24 kez geçiyordu → silindi · **D144**: referans paketinin kabul/ret kapıları 2 sayısal eşikten **7 kapıya** çıkarıldı (her biri KABUL · RET · YABANCI GÖZ · SONUÇ satırlı) · ⛔ **KAPANMAYAN TEK BOŞLUK — D124:** ızgara hâlâ ölçülmedi. 00_PLAN'a doldurulmayı bekleyen `KLİP SÜRESİ = ____` satırı ve ffprobe komutu kondu; format kartına da (`yatay_10_20_dk_filmler/README.md`) **dürüst kayıt** düşüldü: kartın "8 saniye = Veo native" satırının hiçbir ölçüm atfı yok ve D124 ile doğrudan çelişiyor, bu hattın hiçbir filmi henüz üretilmediği için 8 saniye burada hiç ölçülmedi · ⚠️ ayrıca denetim, planın 12 risk kartının 12'sinin de ÜRETİM tarafı olduğunu ve **filmin en büyük riskinin hiçbir listede olmadığını** buldu: S58-S84 = 27 ardışık sahne tek kapsül konisinde, A'nın son repliği S45 (sonrası 75 sahne / 10:08 sessiz), F9-F10 diyalog 0 → üçü de 00_PLAN'a **kart-dışı anlatı riski** olarak beyan edildi · ⭐ **120 SAHNENİN 120'Sİ YAZILDI VE ONU DA GO ALDI** — dört Çehov zinciri ödendi (oksijen S71 · saat S117 · doksan dakika S94 · iniş roketi S95), TEMA'nın dört motif sahnesi yazıldı (S30·S43·S84·S117), iki şok bandı harcandı (S94·S102), Overview tam bir adet (S68) · MUZIK_VE_SES / KAPAK / `YERCEKIMI_QA_SPEC.md` ❌ (sırada) · ⛔ **VE HEPSİNDEN ÖNCE D124 KAPISI:** `00_PLAN.md`'deki `KLİP SÜRESİ = ____` ffprobe ile doldurulmadan üretim başlamaz · ⛔ SPEC yazılmadan "yazımı tamam" sayılmaz [D117] · ⭐ **01.09 ÜRETİM: F1 ve F2 çekildi, ikisi de KARIŞIK SIRADA** → faz rubrikleri sıradan bağımsız kadraj kataloğuna çevrildi. **F2'de rubrik İKİYE BÖLÜNDÜ** (`FAZ_02_QA_PROMPT.md`: A kör geçiş / B katalog geçişi, iki AYRI sohbet) çünkü F1'in ③ kimlik kapısı UNATTRIBUTED düşmüştü — rubrik tarifleri önden verdiği için rapordaki "çapa"lar yankıydı. **A geçişi sekiz yankısız çapa üretti** (biri SAYISAL: söylenmemiş halka 4/6'yı doğru saydı) → ③ F2'de ✅ GEÇTİ · ⭐ **karışık sıra ölçüye çevrildi: SIRA SKORU = 8/12** ve dört sapmanın hepsi iki sebebe indi — (a) S18'in halat kopuşu kör izleyiciye HİÇ görünmedi, (b) savrulma bloğunun tek ayırıcısı oksijen halkası ve halka yalnız tek klipte okunuyor → **film boyu sayaç okunurluğu sorunu** (F3-F10 kararı) · 🔴 **F2'nin asıl sonucu ÖLÇÜLDÜ: vizör kilidi METİNLE tutulamıyor** — "24 by 16 centimetres" + "visible bright metal frame" dokuz promptta yazılı, kubbe çıkan altı klibin BEŞİNDE tam tarif vardı, altısı da kubbe çıktı; tek çare RA p4 referans paneli (0/15 üretilmiş) · F2 kusurları: kubbe vizör 6 klip · mekik burnu ters 5 klip (tek doğru E — burun kadraj dışı, yön kompozisyonu taşıyor) · Seg 3 = Seg 2 birebir kopya · Seg 9'da hayalet yüz · enkaz D↔J çelişiyor (RD p2 yok) · **C (S15, viral #1) HİÇ ÜRETİLMEDİ** · ham raporlar `02_HAM_RAPORLAR/YERCEKIMI_FAZ02_{KOR,KATALOG}_HAM.md`, kapı defterleri film kaydında KOŞU 2 · ⛔ faz koşuları T1-T4'e GİRMEZ |
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

# 🧟 ZOMBİ · 2-4 dk — ⏸️ TÜR KAPANDI (26.08.2026 · kart H2)

> Depo yalnız **UZAY** filmleri içindir. Klasör ve dört zombi filminin
> dördü de kaldırıldı: THE HELD HEAT · THE LAST SPAN (zombi klasörü) ·
> THE SHORT WAY DOWN · THE STRAIGHT LINE (dikey shorts içindeydiler —
> **tür klasöre eşit değil**, kapatırken tüm format klasörleri taranır).
>
> Tür kartı silinmedi, `KILAVUZ_REHBERI §4.2`'de ⏸️ RAFTA duruyor.
> Bu bölüm bir SAYIM bölümü değil, bir kapanış kaydıdır — payda ve
> tamlık matrisi artık bu türü içermez.
>
> ⚠️ THE LAST SPAN'ın film kaydı ve 7 ham raporu KASITLI OLARAK duruyor
> (kural ④). Bir METODOLOJİ kaydıdır: skor üretmez, matrise girmez,
> kıyas tabanı sayılmaz → `01_FILM_RAPORLARI/THE_LAST_SPAN.md`
>
> Arşiv (depo dışı): `film_md_ZOMBI_ARSIV_2026-08-26.tar.gz`

# 📱 DİKEY SHORTS — 15 film (3 ✅ / 12 ❌)

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
| ❌ | THE_SHORT_WAY_DOWN_DIKEY_SHORTS | 🆕 23.08.2026 · yazıldı, üretilmedi (liste 25.08'de güncellendi) |
| ❌ | THE_STRAIGHT_LINE_DIKEY_SHORTS | 🆕 23.08.2026 · dikey hattın ilk ZOMBİ konsepti · yazıldı, üretilmedi (liste 25.08'de güncellendi) |
| ✅ | THE_IRON_SLOPE_DIKEY_SHORTS | 🆕 24.08.2026 · vakum + itki yerçekimi (§3.5), novum "uzayda aşağı var" · **25.08: ÜRETİLDİ + ALTI MERCEK koşuldu, altısı da mod V** → 🔧 Ⓥ5,5 · 🔗 Ⓥ5,9 · 🔊 🚨geçersiz · 📖 Ⓥ2,6 · 🖼️ Ⓥ3,8 · ⚖️ Ⓥ7,5 · ⛔ hepsi ÖN KOŞU (SPEC dosyası yoktu) · ⭐ **koşunun çıktısı skor değil ÖLÇÜM:** master 65,0 s / 6 × 10,0 s klip / 4,97 s başlık kartı; serbest parça hızlanmıyor → **novum ekrana gelmedi** · **DERS 124-125-126-127** · [→](01_FILM_RAPORLARI/THE_IRON_SLOPE.md) |

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
□ 🔴 DOSYA TEMİZLİĞİ — 2 dakika, en ucuz iş [D160 · 01.09.2026]
  `~/Downloads/the frost lıne .mp4` ve `the frost lıne  (1).mp4` (245,120 s ·
  720p + 4K) **THE FROST LINE DEĞİL, THE PAYLOAD'dur** — üstelik kuyruğunda
  THE FROST LINE'ın kapak kartı duruyor. Payload'ın kaydı "master yok" diyordu;
  master buradaydı ve yanlış ad yüzünden hiç ölçülmemişti.
    → `the payload.mp4` olarak yeniden adlandır
    → THE FROST LINE kartını Payload kurgusundan çıkar (zaten çıkacaktı)
    → Payload hook 10 → 9 s kırp · ⑪'in kalanını koş (ses · LUFS · filigran)
□ 🔊 THE FROST LINE — MİKSTE DÜZELİR (yeniden üretim GEREKMEZ) [kart E3 · 2. parti]
    · dış yatakta RÜZGÂR VAR, SPEC "rüzgâr 0" der → rüzgâr katmanı çıkar,
      yerine "ince tıslama" (③ bunu yatak sanıp EQ sıçramasını bulgu yazdı)
    · 1:00 çöküş sesi hafif — ağır LFE + yırtılan polimer + kaçan basınç
    · 1:59 plastik açılma SFX'i ~12 kare geç — sola kaydır
    · 0:29/0:39 rüzgâr EQ sıçraması — tek yatak serilirse kendiliğinden gider
    · ⬜ AÇIK, sahip DİNLER: üç müziksiz pencere (0:00-0:09 · 3:07-3:20 ·
      3:24-3:39) yerinde mi, 3:24,0'daki kelepçe darbesi var mı
□ 🎬 THE FROST LINE — YENİDEN ÜRETİM GEREKTİRİR (2. parti eki, 1. partinin
  listesine ek üç madde):
    · plan S22: tohum EKİLMEDEN önce yatakta çimlenmiş filiz OLMAYACAK
      ("filiz 0 kare" — t217/t219 ihlali gösteriyor)
    · iç sahneler: PEMBE LED yetiştirme şeridi YOK ("yapay lamba/LED 0 kare")
    · plan S5: sırt DÜZ — harness yok (t52/t57; D139 pozitif yüzey tarifi
      sırtı gören HER kadraja yazılır, yalnız yuva 13'e değil)
□ 📦 THE FROST LINE — İHRAÇ: 4K ✅ geldi; filigran · kart · −21,2 LUFS /
  tepe −0,1 dBFS · kırpılmamış hook DURUYOR
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
| `../QA_PROMPTLARI/_KAYNAK/1_KARE_QA_CRITIQUE_PROMPT.md` | ① sahne içi · 11 kategori + 3 dikey anahtar |
| `../QA_PROMPTLARI/_KAYNAK/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | ② sahneler arası · 13 kategori (gövde 1-6 · dünya 7-13) |
| `../QA_PROMPTLARI/_KAYNAK/3_SES_QA_CRITIQUE_PROMPT.md` | ③ 9 kategorili ses merceği — yalnız kurgu |
| `../QA_PROMPTLARI/_KAYNAK/4_HIKAYE_QA_CRITIQUE_PROMPT.md` | ④ dramaturji · 10 kategori |
| `../QA_PROMPTLARI/ARSIV_6_MERCEK/` | ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ; bu depodaki 83 ham rapor onlarla üretildi |
| `../QA_PROMPTLARI/UC_GECISLI_QA/` | 3 geçişli QA sistemi |
| `../../yatay_10_20_dk_filmler/THE_SLOW_STONE/QA_RAPORU.md` | tek tam QA raporu |
