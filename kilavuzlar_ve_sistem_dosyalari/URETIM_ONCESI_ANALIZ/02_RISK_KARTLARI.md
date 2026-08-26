# 🃏 RİSK KARTLARI — plan yazmadan önce oku

> **Kullanım:** Filmin içinde ne var? Aşağıdan o kartları seç. Her kart
> geçmiş veriden **ne bozulacağını**, **kaç filmde bozulduğunu** ve
> **planın hangi satırını yazman gerektiğini** söyler.
> **Kaynak:** Kart 1-8: 01.08.2026 kesiti (11 QA raporu + 50 ders).
> Kart 9-11: 21.08.2026'da eklendi (D104 · yapısal red vakaları ·
> D70/72/100/101). Tahmin yok, hepsi ölçülmüş.
> ⚠️ Eski filmlerin `n/9` skorları 9 kalemlik sürümle ölçüldü ve YENİDEN
> YAZILMAZ; 21.08.2026 sonrası filmler `n/12` yazar.

---

## ⚡ 30 SANİYELİK KULLANIM

```
1. Filmin malzeme listesini çıkar:  su · canlı · diyalog · parçacık ·
                                    sıfır-g · patlama · kask · sayaç · ikinci figür ·
                                    tek baskın ışık + hedefe hareket ·
                                    insansız sahne · değişken çekim süresi
2. Karşılık gelen kartları oku
3. Her kartın "PLANA YAZ" bloğunu plan dosyasına KOPYALA
4. "SAHNEDEN ÇIKAR" uyarısı olan malzemeyi gerçekten çıkarmayı düşün
```

---

# 🔴 KART 1 — SU / SIVI

```
RİSK SKORU:  🔴 EN YÜKSEK
KANIT:       Tidal Hunt Fizik 2/10 (serinin en düşüğü) · Hollow Station
             Fizik 4/10 · Slow Tide Fizik 3/10
İLGİLİ DERS: 7 · 14 · 24 · 39
```

**Ne bozulur:** Su donar (Ders 14), sıvı temasında el erir (Ders 24),
toz suyun altındaymış gibi süzülür (Ders 39).

```
⛔ SAHNEDEN ÇIKAR:  Çıplak el ↔ sıvı teması. Bu kombinasyon 4 filmde
                    4 kez bozuldu. Eldivenli temas veya temassız plan.

✅ PLANA YAZ:       LIQUID CONTACT SCHEDULE — 13 sahnenin kaçında sıvıya
                    dokunuluyor: [sayı]. Hangi sahnelerde: [S numaraları].
                    Diğer tüm sahnelerde sıvı yalnızca ARKA PLANDA.
```

---

# 🔴 KART 2 — CANLI / HAYVAN

```
RİSK SKORU:  🔴 EN YÜKSEK
KANIT:       Canlı kategorisi 11 filmin yalnız 5'inde ölçüldü,
             ortalama 3.90, hiç 5'i geçmedi
İLGİLİ DERS: 2 · 18 · 28
```

**Ne bozulur:** Anatomi kare kare değişir (Ders 2), hayvan kayarak
yürür (Ders 18), parlayan canlıya temasta geometri erir (Ders 28).

```
⛔ SAHNEDEN ÇIKAR:  Yakın planda yürüyen çok bacaklı canlı.
                    Tidal Hunt'ın 2/10'u tam olarak bu.

✅ PLANA YAZ:       CREATURE ANATOMY LOCK — bacak sayısı [n], baş [1],
                    kuyruk [n]. Her adımda ayak kalkar-basar-iter.
                    Canlı [n] sahnede görünür, [n] tanesinde uzak planda.

💡 ALTERNATİF:      Kaleida'nın Prizma Hayalet'i çözümü buldu: canlıyı
                    "neredeyse görünmez" yaz. Görünmeyen anatomi bozulmaz.
```

---

# 🟠 KART 3 — KASK / VİZÖR / EKİPMAN

```
RİSK SKORU:  🟠 YÜKSEK — ve ÖLÇÜLMÜŞ EN NET BAŞARISIZLIK
KANIT:       Inversion Kostüm 2/10 · Kaleida Kostüm 2/10 ·
             Tidal Hunt Kostüm 3/10 — üç MANTIK raporunun üçünde de en dip
İLGİLİ DERS: 5 · 8 · 37
```

**Ne bozulur:** Kask/vizör sahneler arasında açılıp kapanır. Tarif kilidi
(`ALWAYS VISIBLE`) iki filmde de tutmadı; sayısal kilit Slow Stone'da tuttu.

```
❌ YAZMA:    "Visor ALWAYS VISIBLE in every frame"
             (Inversion satır 135 ve 408'de yazılıydı — tutmadı)

✅ PLANA YAZ: HELMET STATE SCHEDULE — 13 sahne.
              Kapalı: S0-S12 (13 sahne).  Açık: 0 sahne.
              Vizörsüz kare bir üretim hatasıdır, tasarım değil.
```

---

# 🟠 KART 4 — İKİNCİ FİGÜR RİSKİ (her filmde var)

```
RİSK SKORU:  🟠 YÜKSEK
KANIT:       Kaleida 1:25 klon · Tidal Hunt 0:00 ve 1:49 iki kâşif
İLGİLİ DERS: 20
```

**Ne bozulur:** Tek kişilik filmde model ikinci bir insan çiziyor —
özellikle **gemi iniş/kalkış** sahnelerinde. İki örneğin ikisi de
"araçtan inme / araca binme" anında.

```
✅ PLANA YAZ: HUMAN COUNT LOCK — bu filmde tam 1 insan var, 13 sahnenin
              13'ünde. Mürettebat yok, pilot yok, yansıma yok, gölge yok.
              İniş ve kalkış sahnelerinde gemi UZAKTAN çekilir; rampada
              kimse görünmez.

⚠️ ÖZEL UYARI: Bu hata en çok İLK ve SON sahnede çıkıyor — yani izleyicinin
               filmi bırakma kararı verdiği iki karede.
```

---

# 🟠 KART 5 — EKRAN / SAYAÇ / METİN

```
RİSK SKORU:  🟠 YÜKSEK — iki yönlü, ikisi de tehlikeli
KANIT:       Dead Approach 2:10 · Inversion 2:12 · Tidal Hunt sayaç yok
İLGİLİ DERS: 9 · 13 · 34 · 45 · 50
```

**İki yönlü risk — bu kartın en önemli tarafı:**

```
YÖN 1 (fazlalık)  model ekrana anlamsız yazı ekler         → Ders 13/34/45
YÖN 2 (eksiklik)  "no text" yasağı ANLATIMI de siler        → Ders 50 🚨
```

Tidal Hunt'ta sayaç filmin omurgasıydı; `NEVER text` yasağı yüzünden ekrana
hiç çıkmadı ve film "bir kadın koşuyor"a döndü. Plan kendi içinde çelişiyordu.

```
✅ PLANA YAZ: Sayaç/gösterge metinle DEĞİL, fizikle anlatılır — 3 kanal:
              · su çizgisi / gölge boyu gibi ÇEVRESEL bir ölçek
              · ekranda kapanan halka, sönen segment (sayı yok, DOLULUK var)
              · her sahnede bir sonraki adım: S0 %100 → S12 %0, 13 adım

🚨 KONTROL:   Plan dosyasında "no text" ve "reads 6:00:00" aynı anda var mı?
              Varsa plan kendi kendisiyle çelişiyor ve model YASAĞI seçer.
```

---

# 🟡 KART 6 — PARÇACIK / TOZ / PATLAMA

```
RİSK SKORU:  🟡 ORTA-YÜKSEK — ama HİÇ DÜZGÜN ÖLÇÜLMEDİ
KANIT:       Low Power Parçacık 2/10 (projenin en düşük tek skoru) ·
             Dead Approach 4/10 · Kaleida'da hiç ölçülmedi (patlama filmi!)
İLGİLİ DERS: 10 · 21 · 30 · 31 · 36 · 39
```

```
⛔ SAHNEDEN ÇIKAR:  Vakumda duman/egzoz kıvrımı (Ders 36) — vakumda duman
                    dağılır, kıvrılmaz. Model her seferinde atmosfer çiziyor.

✅ PLANA YAZ:       PARTICLE GRAVITY LOCK — yerçekimi [0.38g].
                    Düşen parçacık [n] saniyede [n] metre yol alır,
                    düz yay çizer, havada asılı kalmaz, yön değiştirmez.

🚨 UYARI:           Bu kategori kalite tablosunda YOK. Projenin en düşük
                    skoru (2/10) hiçbir özet tabloda görünmüyor.
```

---

# 🟠 KART 6b — KATMANLI / BÖLGELİ DÜNYA (yeni)

```
RİSK SKORU:  🟠 YÜKSEK — sessiz, çünkü tek karede görünmüyor
KANIT:       Canopy World MANTIK QA — Zaman-Işık 5/10, Coğrafya 5/10
İLGİLİ DERS: 47 · 48
```

**Ne bozulur:** Film "her katmanın kendi ışığı var" diye tasarlanır; model
her sahneyi ayrı üretir ve bir sahne yanlış katmanın ışığıyla çıkar.
Tek klibe bakan teknik QA bunu göremez — hata iki sahne ARASINDA.

> 🚨 **Gerçek olay:** Canopy World'ün Kök Labirenti sahnesi. Lighting Bible
> `"cold blue-white light refracting through the crystal pools"` diyor,
> ekranda parlak güneşli bir dere var. Film 3.000m'den 0m'ye kesintisiz
> iniş; o sahne ışığıyla iniş hissini kırıyor.

```
✅ PLANA YAZ: LAYER LIGHT SCHEDULE — her sahnenin katmanı ve o katmanın
              ışığı tek tabloda, sahne numarasıyla:
              S2 Taç 3000m altın-yeşil direkt · S4 Sis 1000m gölgesiz beyaz
              · S6 Karanlık 200m yalnız biyolüminesans · S8 Kök 50m soğuk
              mavi-beyaz kırılma · S9 Zemin 0m amber-beyaz zemin parıltısı

⚠️ KONTROL:  Sahneleri irtifaya göre sırala ve ışık değerlerini alt alta oku.
             Sıralama monotonik değilse (parlak→karanlık→parlak) ya plan
             yanlış ya üretim. Canopy'de üretim yanlıştı.
```

---

# 🟡 KART 7 — DİYALOG

```
RİSK SKORU:  🟡 ORTA — ama tek diyaloglu film serinin en düşük puanını aldı
KANIT:       Dead Approach 3/10 (serinin en düşüğü) — ilk diyaloglu film
             Diyalog & Ses 3/10 · Low Power altyazı hatası
İLGİLİ DERS: 35 · 40
```

```
⛔ SAHNEDEN ÇIKAR:  Karşılıklı diyalog. Sıra alma = lip-sync çöküşü.

✅ PLANA YAZ:       Tüm replikler KAYIT (log) formatında, tek konuşmacı,
                    cevap beklenmiyor. Low Power'ın planı bunu doğru
                    çözmüş: "19 dakikalık gecikme nedeniyle kimse cevap
                    veremez → teknik kazanç: lip-sync çakışması yok."

💡 EN GÜVENLİ:      Sessiz film. Kaleida tamamen sessiz ve Diyalog
                    kategorisinden hiç puan kaybetmedi (N/A).
```

---

# 🟢 KART 8 — KAMERA (tek iyi haber)

```
RİSK SKORU:  🟢 ÇÖZÜLEBİLİR — projede çözülmüş TEK kategori
KANIT:       Low Power 8/10 (sabit lockoff) · Slow Stone 7/10 (ayrı üretim)
             Diğer 9 filmde 2-4 arası
İLGİLİ DERS: 1 · 22
```

```
✅ PLANA YAZ: CAMERA MOVE — fixed lockoff. Kamera hiç hareket etmez.
              Zoom yok, pan yok, tilt yok, track yok, kesme yok.

📈 KANIT:     Ders 1 (gizli kesme) 8/8 filmde tetiklendi. Tetiklenmediği
              tek yer: Slow Stone — çünkü 7-9 dk formatı sahneleri AYRI
              üretiyor, model kesme uydurmak zorunda kalmıyor.
              → Kesme sorunu bir prompt sorunu değil, MİMARİ sorunu.
```

```
⛔ KAPSAM — BU KARAR KLİP İÇİDİR (26.08.2026 daraltması)
              Yukarıdaki reçete tek klibin İÇİNİ bağlar. Sahneler ARASI
              kurulum değişimi karardan MUAF ve ZORUNLUDUR.
              Gerekçe yukarıdaki KANIT satırının kendisi: sahneler ayrı
              kliplerde üretiliyor, iki klibin farklı açıdan çekilmesinin
              gizli kesme riski SIFIR. Kamera skorunu kurtaran şey klip
              içi sadelikti; tek kurulum değil.
              Bant: ../ACI_YAYI_VE_SEKANS_KILAVUZU.md §3 (ardışık çift:
              ≥1 ölçek kademesi VE ≥45° açı farkı) · §4 (kurulum sayısı)
              Ölçen kapı: ../PROMPT_KONTROL/prompt_kontrol.py (kurulum
              çeşitliliği · açı sözlüğü) — eşikler orada, burada değil.

🚨 NEDEN DARALTILDI: karar sahneler arasına sessizce genellendi.
              26.08.2026 ölçümü: 187 film .md dosyasının 126'sı sabit-kamera
              kalıbı taşıyor (lockoff / no camera movement / static camera);
              en yeni dikey filmde 6 kamera satırının yalnız 3'ü benzersiz
              (üç sahne birebir aynı satır) ve üç kurulumun üçü de alttan
              bakıyor. Hiçbir kapı bunu ölçmüyordu.
              ⚠️ Bu iki sayı O GÜNÜN kesitidir; güncelini almak için
              prompt_kontrol.py'yi film klasörlerine koş.
```

---

# 🔴 KART 9 — TEK BASKIN IŞIK + HEDEFE HAREKET (ışık mıknatısı) 🆕 21.08.2026

```
RİSK SKORU:  🔴 YÜKSEK — dört kanallı panzehir bile bir vakada yetmedi
KANIT:       Black Cradle S4 (16.08.2026): İKİ ayrı red — astronotlar
             landera değil ŞAFAĞA koştu; prompt uzamsal kılavuza uygundu
             ve betik kapısından geçmişti. V3 (kamera hedefe taşındı)
             17.08'de İLK denemede geçti.
İLGİLİ DERS: 104
```

**Ne bozulur:** Kadrajda TEK baskın ışık kaynağı (şafak, patlama,
projektör) varken model hareketli özneyi ONA DÖNDÜRÜR — hedef ve yön
yazılıyken bile. Araç sahnesindeki karşılığı: burnu ışığa çevirir.

```
✅ PLANA YAZ:   DÖRT KANAL birden — hedef-dilim+yön · omuz hattı ·
                IŞIĞA GÖRE POZ ("their backs are to the light — it rims
                their back silhouettes") · yön negatifi ("no one runs
                toward the light, no direction reversal"). [UZAMSAL §6.7]
⛔ İKİ YENİLGİ KURALI: iki redden sonra üçüncü yeniden yazım YOK —
                kamera HEDEFE taşınır, hareket kameraya doğru kurulur
                (frontal refleks doğru cevaba dönüşür). [UZAMSAL §6.8]
⚠️ BETİK GÖREMEZ: yön kapısı konum+hareketi arar, YÖNELİMİ aramaz.
                Denetim insan gözüyle.
```

---

# 🟡 KART 10 — İNSANSIZ SAHNE + UZUN NEGATİF BLOK (yapısal red) 🆕 21.08.2026

```
RİSK SKORU:  🟡 ORTA — üretim başlamadan reddedilir; para değil GÜN yakar
KANIT:       Cold Burn S8 (07.08) · Ring Light S2/S4: aynı gün 3 red /
             0 başarı (12.08) · Third Dune: 5 red / 0 başarı (10-11.08)
İLGİLİ DERS: 59 · REHBER §7 "YAPISAL RED" bölümü
```

**Ne bozulur:** İnsansız sahnede uzun `NEGATIVE:` bloğu + "Exactly 0
human figures" kalıbı, istem sınıflandırıcısında "yerine getirilemez"
sayılıyor — yokluk listesi istek olarak okunamıyor. Aynı blok insanlı
sahnede sorun çıkarmıyor.

```
✅ PLANA YAZ:   insansız sahneler işaretlenir; onların promptunda
                NEGATIVE bloğu TEK pozitif Style satırına iner, boş
                kadraj VARLIK olarak tarif edilir ("the cabin around it
                is empty and unlit") [D59]
⛔ ÜÇÜNCÜ REDDE: prob BAŞA alınır (REHBER §7 adım 4 — tam metin orada);
                SIFIR BAŞARI varken prompt kısaltmak boşa emektir.
```

---

# 🔴 KART 11 — DEĞİŞKEN ÇEKİM SÜRESİ / SAHNE İÇİ KESME (kurgu riski) 🆕 21.08.2026

```
RİSK SKORU:  🔴 YÜKSEK — üretim mükemmel olsa bile film kurguda kaybolur
KANIT:       Last Shift (16.08): 27 klipten ~17'si ekranda, süre
             "yaklaşık tuttuğu" için kayıp görünmedi; düşenler arasında
             İFŞA 1 ve tek aksiyon ritmi · yanık başlık kartı 6 vaka ·
             Unbroken City: doruk S9 kurguya girmedi
İLGİLİ DERS: 70 · 72 · 100 · 101
```

**Ne bozulur:** Hattın klibi sabit (~10 s); plan değişken çekim süresi
yazarsa ham malzeme > hedef süre olur ve talimatsız kurgu KIRPMAZ,
KLİP DÜŞÜRÜR. Sahne=çekim=klip olmayan filmde kapı tek birim sayarsa
kayıp görünmez.

```
✅ PLANA YAZ:   SPEC'e üç sayım (SCENE/SHOT/CLIP COUNT) + iki satır:
                RAW FOOTAGE: __ klip × __ s = __ s · TRIM BUDGET: __ s
                + §0.18 KIRPMA TABLOSU (klip başına: ham → kurguda →
                nereden kırpılır)
⛔ TESLİMDEN ÖNCE: 10 maddelik kurgu kapısı koşulur —
                ../KURGU_VE_TESLIM_KILAVUZU.md (tek adres)
```

---

# 📋 RİSK TOPLAMI — planı yazmadan önce doldur

```
FİLM: ______________________

□ Su/sıvı teması var mı?        → varsa KART 1, kaç sahnede: ___
□ Canlı var mı?                 → varsa KART 2, kaç sahnede: ___
□ Kask/vizör var mı?            → varsa KART 3 (her uzay filminde var)
□ İkinci figür riski            → KART 4 (HER filmde geçerli, atlanamaz)
□ Ekran/sayaç/gösterge var mı?  → varsa KART 5 — çift yönlü kontrol
□ Parçacık/toz/patlama var mı?  → varsa KART 6
□ Katmanlı/bölgeli dünya mı?    → varsa KART 6b — ışık takvimi şart
□ Diyalog var mı?               → varsa KART 7
□ Kamera hareketi var mı?       → KART 8 — kaldırabiliyor musun?
                                   ⛔ "kaldırdım" = KLİP İÇİ; sahneler
                                   arası açı yayı yine zorunlu (KART 8)
□ Tek baskın ışık + hedefe hareket? → varsa KART 9 — dört kanal + iki yenilgi kuralı
□ İnsansız sahne var mı?        → varsa KART 10 — NEGATIVE bloğu tek satıra
□ Değişken çekim süresi / sahne içi kesme? → varsa KART 11 — kırpma bütçesi

RİSK SAYISI: ___ / 12        ← payda YUKARIDAKİ SORU SAYISIDIR, sabit değil.
                                Kart eklenince payda da artar (bu liste tek kaynak).

⚠️ 5 ve üstü ise: film şu anki sistemle 5/10'un üstüne çıkamaz.
   Malzeme azaltmayı düşün. Kalite, daha iyi prompttan değil,
   DAHA AZ RİSKLİ SAHNEDEN geliyor — kanıt: Kamera 2→8 (tablo min→max;
   ardışık sıçrama karşılığı 3→8 · 01_DERS_ETKINLIK_RAPORU §5).

⚠️ EŞİK KALİBRASYONU AÇIK: "5+" bandı liste 9 SORULUYKEN ölçüldü; kart
   6b · 9 · 10 · 11 sonradan eklendi ve payda 12'ye çıktı. Aynı film şimdi
   mekanik olarak daha yüksek risk sayısı üretir. Bant yeniden ölçülene
   kadar 5+ eşiği KORUNUR (yanlış tarafa hata yapar: fazla uyarır).
```

---

# 🔬 BU KARTLARIN DAYANDIĞI TEK CÜMLE

> Talebi kaldırabildiğin kategori düzeliyor, kaldıramadığın düzelmiyor.

```
Kamera   talep kaldırıldı (lockoff)      → 2 → 8
Işık     talep kaldırılamadı             → 6 → 4, sabit
Fizik    talep kaldırılamadı             → hiç 5'i geçmedi
Canlı    talep kaldırılamadı             → hiç 5'i geçmedi
```

Ayrıntı: [`01_DERS_ETKINLIK_RAPORU.md`](01_DERS_ETKINLIK_RAPORU.md) §5
