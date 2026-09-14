# 🪙 THE COLD WELD — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası
> operatörde · ⑥ raporunun künyesinde `the cold weld.mp4` yazıyor, tam yol
> ve çözünürlük YOK. **Master bu oturumda depoda yoktur.**
> **Ölçüm:** 01.09.2026 · **altı mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES
> · 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK) — **altısı da mod V.**
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T6'YA GİRMEDİ — VE BU KEZ İKİ AYRI KAPIDAN.**
> ① SPEC kapısı: `THE_COLD_WELD_QA_SPEC.md` **VARDIR** ve altı raporun
> altısı `INPUT MODE: V` yazıyor → koşu TEKRARLANIR [D129].
> ⑤ ÇAPRAZ SAYIM kapısı: kesme sayıları 14/14/16/16/14/14 → **fark 2 > 1
> → partinin TÜM satırları 🚨 GEÇERSİZ** [D107]. İki kapının ikisi de
> tek başına yeterlidir; ikisi birden koştu.
> **SPEC yazılmış olduğu hâlde mod V koşulan film sayısı artık 9.**
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve
> SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır
> [qa-isle §1]. Kare/ses doğrulaması gereken her satır ⬜ AÇIK.
>
> ⛔ **BULGUDAN DERS YAZILMADI.** Parti ASKIDA (⑪: filigran · kuyruk kartı ·
> −18,1 LUFS) ve ② defterinde ⬜ AÇIK madde varken bulgudan ders yazmak
> yasaktır. *(01.09 akşam düzeltmesi: bu satır önce "⑤ geçersiz parti" diyordu;
> o gerekçe ⑪ ölçümüyle düştü, yasak MASTER gerekçesiyle sürüyor — aşağıda ⑤.)* Bu koşunun ürettiği iki ders
> (**D161 · D162**) filmin bulgularından değil, **ALETİN KENDİSİNDEN**
> çıktı ve ikisi de master olmadan, yalnız yapıştırılan metinden
> doğrulanabilir.
>
> ⭐ **BU KOŞUNUN İKİ POZİTİF ÖLÇÜMÜ VAR ve ikisi de askıdaki partiden sağ
> çıkar [D121]: ŞERİT ve IZGARA.** Aşağıda ④'te.

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · 155 s / ~2:35 (raporlardan; ÖLÇÜLMEDİ) · 16:9
          + 2:30-2:35 BAŞLIK KARTI (sahne dışı malzeme, ~5 s)
MERCEK:   ① KARE 5,1 · ② DEVAMLILIK 8,8 (fabrike) · ③ SES 6,0 · ④ HİKAYE 5,6
          · ⑤ ARKA PLAN 5,0 · ⑥ FİZİK 6,2   (altısı da mod V + parti 🚨 → tabloya GİRMEZ)
HAM:      ../02_HAM_RAPORLAR/THE_COLD_WELD_{KARE,DEVAMLILIK,SES,HIKAYE,ARKA_PLAN,FIZIK}_HAM.md
PLAN:     ../../../yatay_2_dk_filmler/THE_COLD_WELD/THE_COLD_WELD_METAL_REEF_FILM.md
SPEC:     ✅ VAR — .../THE_COLD_WELD_QA_SPEC.md (A/B/C blokları)
          ⛔ operatöre VERİLMEDİ — SPEC ile film AYNI GÜN yazıldı
OTURUM:   ⚠️ kopya deseni YOK [D110]: altı raporun bulgu listeleri, kapsam
          sınırları ve severity sayıları ayrışıyor; ② ve ④ birbirinin
          tersini söylüyor (② 8,8 "tutuyor" · ④ 5,6 "yapıyı revize et").
```

---

## ⑪ ÖLÇÜM KAPISI — ⛔ KOŞULAMADI

```
master yolu verilmedi · olcum_kapisi.sh koşulmadı
→ süre · kesme ızgarası · SES KANALI VARLIĞI · LUFS · KÖŞE TESTİ: HİÇBİRİ ÖLÇÜLMEDİ

⛔ BUNUN İKİ SOMUT BEDELİ VAR VE İKİSİ DE BU KAYITTA DURUYOR:
① FİLİGRAN [D150]: ⑤ arka plan raporu 15/15 sahnede "static cyan triangle
   mark, bottom right" yazdı ve 0:00-2:29 aralığını verdi. Bunu KAPATACAK
   tek şey köşe testidir (`kose_SA.png`) ve koşulamadı. → ⬜ AÇIK
② SES KANALI [D136]: ③ "AUDIO STATE: B" dedi — yani ses VAR ama replik yok.
   Bu bir DİNLEME BEYANIDIR, ölçüm değil. ffprobe koşulmadı. → ⬜ AÇIK
   (Plan tamamen sessiz bir film + ses tasarımı yazıyor; ③'ün duyduğu
    drone/temas dokusu plana UYUYOR, ama doğrulanmadı.)

MASTER ELE GEÇTİĞİNDE İLK KOŞULACAK KOMUT:
  bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>" rms
```

---

## ③ KİMLİK KAPISI — ✅ GEÇTİ (metin olmayan dört çapa)

```
① VURUŞ     S0: insansız kadraj, metal levhanın üstünde DİK duran anahtar
            → planın S0 hook'u birebir (② "Wrench on metal panel · Present: none")
② SAYISAL   İNSAN ŞERİDİ `-11111111111111` — planın §0.9 şeridiyle BİREBİR
            (üç ayrı mercek bağımsız üretti: ② ⑤ ⑥)
③ ÇEVRE     "SKY/CEILING: empty black" 15/15 sahnede (⑤) → planın
            "flat black sky, no stars, no gradient" kilidi
④ COĞRAFYA  S12-S14: eğik levha · üstünde yatan gövde · levhanın regolite
            inmesi (⑤ S13-S15 · ⑥ L6) → planın ÇEHOV 5 ödemesi

⛔ EKRANDAKİ YAZI ÇAPA SAYILMADI: ② ve ④ filmin adını başlık kartından
   okudu ("the cold weld" / "THE COLD WELD"). Kimlik bu satırdan DEĞİL,
   yukarıdaki dörtten kuruldu [D105].
→ KOŞU ATTRIBUTED. Ham raporlar bu filmin altına dosyalandı.
```

---

## ④ KURGU KAPISI — ÖN KOŞU (⑪ koşmadığı için), ama ⑨ İKİ SATIRI KURTARDI

```
a) klip sayısı = SCENE COUNT   ⬜ AÇIK — ölçülmedi. Raporlar: ② 15 · ⑤ 15 ·
                               ⑥ 15 · ④ 8. Üçe bir; ④'ün haritası aşağıda düştü.
b) süre = RUNTIME ± 2 s        ⬜ AÇIK — ölçülmedi. Rapor 155 s; kart 5 s
                               düşülünce gövde 150 s = planın RUNTIME'ı ✅ (rapor bazlı)
c) SIRA = İNSAN ŞERİDİ         ✅ DOĞRULANDI — aşağıda
```

### ⭐ c) ŞERİT EKSENİ — GEÇERSİZ PARTİDEN SAĞ ÇIKAN BİRİNCİ ÖLÇÜM [D121 · D135]

```
plan (§0.9)   -11111111111111
② DEVAMLILIK  -11111111111111   ✅ birebir
⑤ ARKA PLAN   -11111111111111   ✅ birebir
⑥ FİZİK       -11111111111111   ✅ birebir
① KARE        111111111111111   🚨 15 hane, baştaki `-` YOK
④ HİKAYE      -1111111          🚨 8 hane

D135 gereği sapan mercek ÖNCE KENDİ envanteriyle karşılaştırıldı:
· ①'in kendi kayıtlarında insansız bir sahne HİÇ geçmiyor — ama S0'ı üç
  mercek insansız gördü ve ① de "CUTS: 0:10..." ile ilk bloğu ayırdı.
  ①'in şeridi kendi kesme listesiyle çelişiyor → ①'in şeridi 🚨.
· ④'ün şeridi kendi 8 sahnelik haritasıyla tutarlı — ama o harita kendi
  16 kesme sayımıyla çelişiyor → kaynak harita, şerit değil.

⭐ SONUÇ: ÜÇ BAĞIMSIZ MERCEK PLANIN ŞERİDİNİ BİREBİR ÜRETTİ.
   Kurgunun SIRASI doğrulanmıştır: 15 klip, plandaki sırada, S0 insansız.
   Eksik sahne yok, fazla sahne yok, kuyrukta kayıp yok [D62/D72 taraması temiz].
```

### ⭐ ⑨ HİZALAMA KAPISI — İKİNCİ ÖLÇÜM (master açılmadan koşar)

```
Izgara PLANDAN alındı: sahne başlangıcı(n) = n × 10 s · S0 = 0

  n    plan     ①'in kesmesi     Δ
  1     10 s        0:10        0 s
  2     20 s        0:20        0 s
  3     30 s        0:29       −1 s
  4     40 s        0:40        0 s
  5     50 s        0:50        0 s
  6     60 s        0:59       −1 s
  7     70 s        1:10        0 s
  8     80 s        1:19       −1 s
  9     90 s        1:29       −1 s
 10    100 s        1:39       −1 s
 11    110 s        1:49       −1 s
 12    120 s        1:59       −1 s
 13    130 s        2:10        0 s
 14    140 s        2:19       −1 s

max |Δ| = 1 s  →  ⭐ IZGARA OTURUYOR.
15. sahne 140-150 s · KART 150-155 s.

⭐ BUNUN İKİ SONUCU VAR:
① ①'in zaman kodları UYDURULMAMIŞTIR. Uydurulmuş zaman kodları 10 saniyelik
   ızgaraya 14 kez üst üste oturmaz [D115].
② ④'ÜN 8 SAHNELİK HARİTASI ÖLÇÜMLE ÇÜRÜDÜ. ④'ün "S2 = 0:10-0:50 (40 s)"
   bloğu, ızgarada DÖRT ayrı klibin birleşimidir; "S3 = 0:50-1:20" ÜÇ klip.
   ④'ün kendi rubriği bunu yasaklıyor ("en kısa kesme aralığının iki
   katından uzun blok → böl ve yeniden say") ve ④ kendi 16 kesme sayısını
   yazdıktan sonra 8 sahne yazdı.
   → ④'ün Yapı · Tempo · Duygu Yayı · Final · Tutundurma hücreleri
     OLMAYAN BİR FİLME verildi. Kesme listesi UYGULANMAZ.
```

---

## ⑤ ÇAPRAZ SAYIM KAPISI — ⑪ ile YENİDEN HÜKÜM (01.09.2026 · akşam)

```
mercek          kesme   sahne   şerit               replik
① KARE            14      —     111111111111111     none
② DEVAMLILIK      14     15     -11111111111111     none
③ SES             16      —     —                   none (0 replik)
④ HİKAYE          16      8     -1111111            none
⑤ ARKA PLAN       14     15     -11111111111111     —
⑥ FİZİK           14     15     -11111111111111     none

kesme yayılımı = 2   ⛔ fark > 1  → TÜM SATIRLAR 🚨 GEÇERSİZ
sahne yayılımı = 7   ⛔
şerit           4 ✅ / 2 🚨   (yukarıda ④'te çözüldü)
replik          6/6 AYNI: 0 replik  ✅  → replik ekseni doğrulandı [D121]

⭐ ③ ve ④ neden 16 saydı: ikisi de başlık kartının GİRİŞİNİ ve ÇIKIŞINI
   ayrı kesme saymış olabilir (14 gövde sınırı + 2 kart sınırı = 16).
   ✅ HİPOTEZ KAPANDI — ⑪ koşuldu: 14 gövde kesmesi + kart = 15 klip (§⑪.1).
```

### ⚖️ YENİDEN HÜKÜM — ölçüm hakem oldu

Bu bölüm ilk yazıldığında ⑪ HENÜZ KOŞULMAMIŞTI ve kendi koşulunu yazmıştı:
*"⑪ olmadan kapanmaz"*. ⑪ aynı gün koşuldu; koşul karşılandı.

AGENTS §3: **"Rapor ile ölçüm çelişirse ÖLÇÜM kazanır."** Anlaşmazlık
çözülmüşken partiyi kesme yayılımından toptan düşürmek, ölçümü yok saymaktır.
`rapor_kontrol.py` bunu yapamıyordu — ölçüm girişi YOKTU; eklendi
(`--olcum-kesme` / `--olcum-sahne`). Ölçümle koşulduğunda:

```
python3 .../rapor_kontrol.py <6 ham rapor> --olcum-kesme 14 --olcum-sahne 15

  🚨 1 GEÇERSİZ  ·  ⚠️ 4 ŞARTLI  ·  ✅ 1 GO      (önce: 6 GEÇERSİZ)

② DEVAMLILIK  🚨 GEÇERSİZ  aritmetik fabrike (n=13 Σ=115 iddia; hücreler n=12 Σ=108)
④ HİKAYE      ⚠️ ŞARTLI    kesme 16 ≠ ÖLÇÜM 14 · sahne 8 ≠ 15 · şerit 8 hane
③ SES         ⚠️ ŞARTLI    kesme 16 ≠ ÖLÇÜM 14 · 3 hücre kaynaksız → düzeltilmiş 5,0
① KARE        ⚠️ ŞARTLI    tally (3,2,1) ≠ yazılı (3,2,2)
⑥ FİZİK       ⚠️ ŞARTLI    tally (0,1,3) ≠ yazılı (0,1,1)
⑤ ARKA PLAN   ✅ GO        n·Σ·ort tutuyor
```

⛔ **SONUÇ DEĞİŞMEDİ, GEREKÇESİ DEĞİŞTİ.** Hiçbir satır T tablosuna GİRMEZ —
ama artık "kesme yayılımı" yüzünden değil, **§⑪'in bulduğu üç teslim kusuru**
yüzünden: filigran (6/6 örnek) · kuyruk kartı · −18,1 LUFS. Geçersiz master'ı
ölçen skor, kapıdan geçse de anlamsızdır. Master yeniden ihraç edilene kadar
parti askıdadır [D136 · D150].

⭐ **BU BÖLÜMÜN KENDİSİ BİR DERSTİR:** kapı, elindeki en iyi kanıtı
kullanamıyorsa yanlış tarafa hata yapar — burada altı raporun beşini
gereksiz yere düşürdü. Ölçüm varken ölçümsüz hüküm verilmez.

---

## ⑦ ÇAPRAZ FİLM PARMAK İZİ KAPISI — ✅ GEÇTİ

```
AYNI GÜN, AYNI ALTI MERCEK, İKİ FİLM:

                  THE PAYLOAD (01.09)      THE COLD WELD (01.09)
süre              246 s / 04:06            155 s / 02:35
sahne             24                       15
kesme             23-24                    14-16
ort. sahne        ~10 s                    ~10 s
başlık kartı      4:00-4:06 (6 s)          2:30-2:35 (5 s)
replik            4                        0

Süre ve sahne sayısı %5 bandının çok dışında → 🚨 PARMAK İZİ ŞÜPHESİ YOK.
İki rapor partisi iki AYRI filmi ölçmüş [D112 temiz].

⭐ AMA İKİ PARTİ AYNI ÜÇ İMZAYI TAŞIYOR VE ÜÇÜ DE FİLMİN DEĞİL HATTIN:
① Her iki teslimin SONUNA başlık kartı eklenmiş — iki planın ikisi de
   "ekran metni 0,0 s" yazıyor. Kart bir film kusuru değil, TESLİM
   ADIMININ VARSAYILANIDIR. [D70/D72 zincirinin 8. ve 9. vakası]
② Her iki partide de SPEC VARDI ve altı merceğin altısı mod V koşuldu.
③ Her iki partide de ~10 s'lik ızgara kesmelerden geri okunabiliyor.
```

---

## ② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 12 madde, 9'u ⬜ AÇIK

| # | rapor ne dedi (timecode) | hangi kilit (§) | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | ① 1:50 🟠 "heavy metal plates float upwards against gravity" | §0.12 FREE BODY LOCK: levha **0,35 m YÜKSELİR**, 0,9 m yana gider, 0,70 s'de oturur | plana bakıldı | ⛔ **RAPOR UYDURDU — yükselme PLANLIDIR** → ⑩'da düştü |
| 2 | ⑤ 1:09↔1:39 🟠 "flat horizon becomes vertical wall" | §0.9 S8 = DUVAR (4,0 × 9,0 m, dikey) | plana bakıldı | ⛔ **RAPOR UYDURDU — duvar PLANLI** → ⑩'da düştü |
| 3 | ⑥ L1 "wrench stands upright, zero recoil — fails real physics" | §0.2 NOVUM: anahtar levhaya KAYNAMIŞ | plana bakıldı | ⛔ **RAPOR UYDURDU — filmin novum'unun ta kendisi** → ⑩'da düştü |
| 4 | ⑥ L6 "kneels on incline without sliding — infinite friction" | §0.12: 22° eğim · 0,30 g · seramik bot. tan 22° = 0,40 | hesaplandı | ⛔ **RAPOR UYDURDU — 0,40 sürtünme katsayısı sıradan** → ⑩'da düştü |
| 5 | ⑥ FLAGS "no dust from falling panels" | §0.12 DUST LOCK: resifte **0 kare toz** | plana bakıldı | ⛔ **RAPOR UYDURDU — tozsuzluk TASARIM** → ⑩'da düştü |
| 6 | ② "Counter Logic N/A — no tracked numerical counters present" | SPEC C bloğu: **ÜÇ sayaç** (ışık çizgisi 34→0 m · AVUÇ 2→0 · yamalar 31→33) | — | ⬜ **AÇIK — ÖLÇÜM BOŞLUĞU [D134]**, yokluk değil |
| 7 | ② passport: "white gloves with dark grey circular palms" 14/14 sahnede DEĞİŞMEDEN | §0.10 SAYAÇ B: S1-S5 iki avuç PARLAK → S6 sağ KARANLIK → S14 ikisi de KARANLIK | kare gerek (0:60 · 2:20) | ⬜ **AÇIK — filmin ANA SAYACI hiçbir mercekte görünmedi** |
| 8 | hiçbir rapor S8'in **31 parlak diskini** anmadı; ② "wall buttons", ⑤ "massive vertical wall" | §0.10 SAYAÇ C · §0.19 TOHUM ödemesi | kare gerek (1:20-1:30) | ⬜ **AÇIK** |
| 9 | ① 0:10 🔴 "airborne footsteps/clanking in vacuum" | §0.12 SES: dışarıda 0 ses, duyulan her şey **TEMASTIR** (gövdeden iletilir) | ses gerek | ⬜ **AÇIK — temaslı ses ile havadan ses ayrımı kulakla yapılır** |
| 10 | ① 1:31 🔴 "wrench head clips through the metal bolt" | §0.12: temas RİJİT, sınır NET, kaynak ATOMİK | kare gerek | ⬜ AÇIK |
| 11 | ⑥ "wrench ~25 cm → ~80 cm" | §0.12 WRENCH LOCK: **56 cm**, tek ölçü | kare + cetvel gerek | ⬜ AÇIK (⑥ cetvel adlandırmadı → Kart F2: cetvelsiz FAIL düşer) |
| 12 | ① 2:20 🟠 "dropped disc lacks low-g momentum" | §0.9 S14: disk KOPMAZ, DÜŞMEZ — levhaya gömülü KALIR | kare gerek | ⬜ AÇIK — rapor olayı yanlış okumuş olabilir |

```
⛔ 9 ⬜ AÇIK madde var → bulgudan ders yazılmaz, yeniden üretim siparişi
   verilmez, kesme listesi uygulanmaz. Defter master ele geçince kapanır.
```

---

## ⑩ ÖNERME KAPISI — 5 bulgu DÜŞTÜ, puanlar geri verildi

```
| mercek | raporun toplamı | ⑩ sonrası | ayakta sayı taşıyan hücre |
| ① KARE   | 5,1 | — | Fizik ve Çevre hücrelerinin tek kaynağı düşen bulgu (1:50);
|          |     |   | Diyalog hücresi 0 replikli filme 3/10 verdi → N/A olmalı.
|          |     |   | Kalan hücrelerin kaynağı ⬜ AÇIK → **satır `—`**
| ② DEVAM. | 8,8 | — | toplam zaten FABRİKE (aşağıda D161) → **`—`**
| ③ SES    | 6,0 | — | 4 hücrenin 3'ü "no in-scope source" ile numaralanmış →
|          |     |   | kendi kuralı gereği sayısız; kalan 1 hücre ortalama değil → **`—`**
| ④ HİKAYE | 5,6 | — | film boyu hücrelerin tamamı OLMAYAN bir haritadan → **`—`**
| ⑤ ARKA P.| 5,0 | — | Horizon hücresinin tek kaynağı düşen bulgu; kalanlar ⬜ AÇIK → **`—`**
| ⑥ FİZİK  | 6,2 | — | Impact · Scale · Material hücrelerinin kaynağı düşen ya da
|          |     |   | cetvelsiz bulgu → **`—`**

⭐ ALTI MERCEĞİN ALTISI DA `—` — sıfır hücreli ortalama ölçüm değildir [D130/D131].
   Parti zaten askıda; bu satır o kararı ikinci bir yoldan doğruluyor.
```

---

## 🚩 PARK EDİLEN DERS ADAYI — ⬜ AÇIK, master gelince kapanır

```
ADAY BAŞLIK: "YOKLUKLA KANITLANAN KURAL EKRANDA OKUNMUYOR"

GÖZLEM (raporlardan, doğrulanmamış):
  Altı merceğin ALTISI da filmin novum'unu adlandırmadı.
  · ④'ün izleyici cümlesi: "investigates impossible physical anomalies"
  · ⑥ FLAGS: "Is the wrench supposed to be highly MAGNETIZED?"  ← rakip kural
  · ② passport avuç diskini GÖRDÜ ama durum değişimini hiç kaydetmedi
  · hiçbir rapor 31 diskli duvarı, avucun kopmasını ya da S12'nin
    bilerek kaynamasını anmadı

HİPOTEZ: bu filmdeki kanıtların TAMAMI birer OLUMSUZLAMADIR —
  düşmeyen anahtar · kalkmayan avuç · kaymayan levha · yapışmayan bot.
  Video "bir şeyin olmaması"nı "hiçbir şey olmaması" diye render eder.
  Planın §0.14 A4 satırı D76'yı (yokluk novumu) "kapalı" saydı çünkü
  novum DÜNYADA bir varlıktır (kaynak). Ama EKRANDA her kanıtı bir yokluk.
  → A4 kapısı yanlış soruyu soruyor: "novum bir yokluk mu?" değil,
    "novumun her KANITI bir yokluk mu?"

⛔ NEDEN DERS DEĞİL: parti ASKIDA (geçersiz master) ve defterde 9 ⬜ AÇIK var. Bulgudan
   ders yazmak yasak [⑤ · ②]. Ayrıca hipotezi çürütecek tek şey master'dır:
   avuç kopuşu (S6, 0:60-0:70) ve duvar (S8, 1:20-1:30) EKRANDA VARSA
   hipotez yanlıştır ve sorun okuma değil ÜRETİMDİR.

KAPATMA PROSEDÜRÜ (master gelince, ~2 dakika):
  ffmpeg -ss 66 -i "$M" -frames:v 1 s6_avuc.jpg      → disk kopuyor mu, geride kalıyor mu
  ffmpeg -ss 85 -i "$M" -frames:v 1 s8_duvar.jpg     → duvarda kaç parlak disk var
  ffmpeg -ss 122 -i "$M" -frames:v 1 s12_avuc.jpg    → avuç levhaya BASIYOR mu
  üçü de VARSA  → ders "okunmadı" değil "mercekler göremedi" olur → D151 ailesi
  biri YOKSA    → ders "yoklukla kanıtlanan kural" olur → yeni ders, ONERME §4'e kapı
```

---

## 📊 SKOR SATIRLARI

```
⛔ T1 · T2 · T3 · T4 · T5 · T6 — HİÇBİRİNE SATIR YAZILMADI.
   Gerekçe iki katlı: ① SPEC kapısı (mod V) + ⑤ çapraz sayım (fark 2).
   00_INDEX tamlık matrisinde THE COLD WELD satırı **0/4** KALIR.
```

---

## 🎬 ÜRETİM TARAFINA ÇIKAN İKİ ZORUNLU İŞ (skordan bağımsız, ikisi de kesin)

```
① BAŞLIK KARTI 2:30-2:35 KALDIRILIR.
   Planın §0.17'si "ekran metni 0,0 saniye" yazıyor; altı raporun ALTISI
   kartı gördü. Bu, D70/D72 zincirinin 8. vakasıdır ve AYNI GÜN THE PAYLOAD'da
   9. vakası çıktı (4:00-4:06). Kart kurgunun SONUNDA olduğu için sahne
   şeridini bozmadı [D120] — silmek tek bir kırpmadır.
   ⭐ Ve kart, S0↔S14 EŞ KADRAJ çiftini öldürür: filmin son karesi levhadaki
      disk olmalı, "THE COLD WELD" yazısı değil (§0.19 açılış-kapanış çifti).

② KÖŞE TESTİ KOŞULUR — ⑤ 15/15 sahnede sağ altta sabit bir işaret bildirdi.
   bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"
   İşaret doğrulanırsa master YENİDEN İHRAÇ EDİLİR [D150]; filigranlı master
   master değildir ve dört merceğin dördü onu ölçmemiş sayılır.
```

---

## 🔗 BU KOŞUDAN ÇIKAN DERSLER

```
D161 — RAPORUN KENDİ ARİTMETİĞİ DOĞRULANMIYOR (6 raporun 5'i kendi kapısından geçemedi)
D162 — ⑤ YALNIZ MUTABAKATI ÖLÇÜYOR; BİR MERCEĞİN SUSKUNLUĞU ÖLÇÜLMÜYOR (filigran vakası)

⛔ YENİ DERS YAZILMAYANLAR — hepsi mevcut derslerin N'inci vakasıdır:
   · SPEC var, mod V koşuldu           → D129, 9. film
   · teslimin sonunda başlık kartı     → D70/D72, 8. vaka
   · sabit köşe işareti                → D150, 2. vaka (fixi zaten var: ⑪ köşe testi)
   · novum mercekler tarafından okunmadı → D157/D151 ailesi · ⬜ AÇIK, yukarıda park edildi
```

---

## ①.5 BETİK KOŞUSU — `rapor_kontrol.py` (01.09.2026 · bu partiden doğan araç)

> Yukarıdaki kapı defterleri ELLE koşuldu; aynı gün yazılan betik aynı altı
> rapora koşuldu ve elle bulunanların tamamını + elden kaçan ikisini buldu.
> Tam çıktı: `RAPOR_KONTROL/RAPORLAR/THE_COLD_WELD_20260901_RAPOR_KONTROL.md`

```
① KARE        TEKRAR   · tally (3,2,1) ≠ yazılı (3,2,2)  ← elden KAÇMIŞTI (iki 🟡: 0:50 · 0:30)
② DEVAMLILIK  GEÇERSİZ · n=13 Σ=115 iddia, hücreler n=12 Σ=108 · Counter N/A ↔ SPEC üç sayaç
              · tally (0,3,4) ≠ yazılı (0,1,2)           ← tally farkı da elden KAÇMIŞTI
③ SES         ŞARTLI   · 3 hücre "no in-scope source" + sayı → `—`; kalan tek hücre 5,0
④ HİKAYE      TEKRAR   · harita 8 ↔ kesme 16 → Yapı/Yay/Final/Tutundurma `—` · şerit 8 ≠ 17
⑤ ARKA PLAN   GO       · partideki tek temiz rapor
⑥ FİZİK       TEKRAR   · tally (0,1,3) ≠ yazılı (0,1,1)
⑤ ÇAPRAZ      ⚠️ kesme yayılımı 2 → ⑪ HAKEM: ölçüm 14 · sapan ③ ④ tekil ŞARTLI
              (parti ayakta) · şerit çoğunluk `-11111111111111` (3),
              sapan ① ④ · replik 6/6 = 0 ✅ · 🚨 SUSKUNLUK: ⑤ film boyu köşe işareti, ① sustu
TABLOYA GİRECEK SAYI: altı mercek için `—`
```

**Yeniden koşu için hazır:** `QA_PROMPTLARI/FILME_OZEL/THE_COLD_WELD/PAKET_1..6_*.md`
(rubrik + SPEC tek dosya, mod D varsayılan — `rubrik_paketle.sh` ile üretildi).
Master ele geçince sıra: `olcum_kapisi.sh <master>` (kuyruk kartı + köşe + ses kanalı)
→ altı paket temiz oturumda → `rapor_kontrol.py <6 rapor> --film … --rapor`.

---

# ⑪ ÖLÇÜM KAPISI — KOŞULDU (01.09.2026 · Faz 1)

> Yukarıdaki bütün ⬜ AÇIK maddeler bu koşuyla kapandı ya da yerini bildi.
> **Bu bölüm rapor kaynaklı DEĞİLDİR — master'dan ölçülmüştür.**

## ⑪.0 KİMLİK [D160] — ✅ GEÇTİ

```
AYNI ADA UYAN İKİ DOSYA — ikisi de ölçüldü (⑪.0b):
  ~/Downloads/the cold weld (1).mp4    3840×2160 · 30 fps · 155,075 s · 223 MB  ← MASTER
  ~/Downloads/the cold weld.mp4        1280× 720 · 30 fps · 155,075 s ·  39 MB
  Aynı SÜRE = aynı kurgu, iki ihraç. İhraç kilidi 1440p+ [KURGU_RITMI §6] →
  ölçüm ve QA MASTER (4K) üzerinden yapılır. Raporların hangisini gördüğü
  BİLİNMİYOR — künyelerinde çözünürlük yok (D160'ın kendi vakası).

KİMLİK KARESİ (kurgunun ortası, 77,5 s) → SPEC C bloğuna karşı:
  tek canlı insan ✅ · kapalı kask + optik ŞEFFAF vizör, yüz okunur ✅
  soluk kemik beyazı giysi ✅ · çıplak metal levha zemin ✅
  gök tek düz SİYAH, yıldızsız ✅ · iniç SAĞ üçte birde, burnu yukarı ✅
  → altı çapanın altısı tutuyor · KOŞU DEVAM
```

## ⑪.1 KURGU KAPISI ④ — ⭐ ÜÇ SATIRIN ÜÇÜ DE GEÇTİ

```
KESME IZGARASI (ölçüldü, rapordan değil):
  eşik 0,30 → 10,03 20,03 30,03 40,03 50,03 60,03 70,07 80,07 90,07
              100,07 110,07 120,07 130,07 ····· 150,10        (13 + kart)
  eşik 0,15 → aynı + 140,10                                    (14 + kart)
  ⚠️ S13→S14 geçişi 0,30 eşiğinde GÖRÜNMÜYOR: iki sahne birbirine fazla
     benziyor (ACI_YAYI §3 ardışık çift bandı ekranda tutmamış). Betiğin
     kendi notu bunu söylüyordu; eşiği düşürünce kesme çıktı.

a) KLİP SAYISI  14 kesme + 1 = 15 klip  = planın SCENE COUNT'u 15    ✅
b) SÜRE         gövde 150,10 s (kart hariç) = plan 150 s ± 2         ✅
c) SIRA         şerit -11111111111111 (üç mercek bağımsız) = plan    ✅
⭐ Raporların "14 / 16" kavgası çözüldü: 14 gövde kesmesi + kart kesmesi = 15
   sınır. 16 diyen iki mercek kartın giriş VE çıkışını saymış (hipotez
   doğrulandı, ⑤ defterindeki ⬜ AÇIK kapandı).
```

## ⑪.2 🔴 ÜÇ TESLİM KUSURU — üçü de ÖLÇÜLDÜ

```
① FİLİGRAN — DOĞRULANDI [D150 · 2. vaka]
   Sağ alt çeyrekte, 25 s'de bir alınan ALTI örneğin ALTISINDA aynı yerde
   aynı şekil: siyah daire içinde cyan "play" üçgeni.
   KONUM (4K): merkez ≈ (3450, 1800) · çap ≈ 120 px
               sağ kenardan %10,2 · alt kenardan %16,7 İÇERİDE
   ⛔ ⑤ ARKA PLAN bunu 15/15 sahnede bildirdi; sahibi ① KARE görmedi ve
      kendi negatif kutusunu işaretlemedi → **D162'nin SUSKUNLUK kapısı
      ilk gerçek vakasında DOĞRULANDI** (kapı bu partiden doğmuştu).
   ⛔ KIRPMAYLA UCUZA ÇIKMAZ: ikon köşeden %10/%17 içeride. Temizlemek
      kadraj genişliğinin ~%12'sini götürür ve inici SAĞ ÜÇTE BİRDEN
      çıkarır — filmin ekran yönü kilidi (§0.13 Kart 9) bozulur.
      ⑤'in önerdiği "%3 crop" YETMEZ; ölçüldü.
      Gerçek seçenekler: (a) kaynakta filigransız yeniden ihraç,
      (b) post'ta içerik-farkındalıklı temizleme, (c) kabul + kayıt.
      ⛔ (c) D150'ye aykırıdır: filigranlı master master değildir.

② KUYRUK KARTI — DOĞRULANDI [D70/D72 · 9. vaka]
   freezedetect: 150,10 s → SON (4,98 s donmuş kare).
   Kart içeriği: "THE COLD WELD / SOME THINGS SHOULD NOT EXIST" + kadraj.
   ⛔ Plan §0.17: ekran metni 0,0 saniye. Kart ayrıca §0.19'un
      AÇILIŞ-KAPANIŞ ÇİFTİNİ öldürüyor (son kare levhadaki disk olmalıydı).
   ⭐ ACI GÖZLEM: kartta kadın avucunda PARLAK DİSK tutuyor ve sağda ANAHTAR
      bir levhaya DİK saplanmış — yani kartı yapan kişi novumu ANLAMIŞ.
      Kart, filmin kendi anlatamadığını tek karede anlatıyor.

③ LOUDNESS — İHLAL [KURGU_RITMI §6 · ihraç kilidi −14 LUFS / −1,0 dBTP]
   ölçülen: I = −18,1 LUFS  ·  Peak = 0,0 dBFS
   → 4,1 LU sessiz VE tepe tavanda (−1,0 dBTP kilidi ihlal).
   Miks seansında düzeltilir; yeniden üretim gerekmez.

SES KANALI: VAR ✅ (ffprobe) · sessizlik aralığı YOK → ③'ün "AUDIO STATE: B"
beyanı ölçümle doğrulandı [D136/D137 kapalı].
```

## ⑪.3 🚩 ADAY-1 KAPANDI — HİPOTEZ **YANLIŞ** ÇIKTI

> `DERSLER/GOZLEM_DEFTERI.md` ADAY-1'in kapatma kuralı: *üçü de VARSA hipotez
> yanlış (sorun okuma), biri YOKSA hipotez doğru (sorun üretim).*

```
S6  AVUÇ MAKRO      65-66 s   ✅ VAR — 100mm makro, eldivenli el, zeminde
                              GÖMÜLÜ parlak dairesel disk, avuçta koyu gri daire
S8  DİSKLİ DUVAR    ⭐ VAR ama 100-120 s'de (planın S10-S11 yuvasında):
                              dikey metal duvar, üstünde ONLARCA dairesel disk,
                              kadın elini duvara uzatıyor · geniş planı da var
S12 SON AVUÇ        122-125 s ✅ VAR — eğik levhada diz çöküş, kameraya SIRTI
                              dönük, el levhaya uzanıyor; sırt TEK PARÇA DÜZ
                              PANEL (D79/D139 tuttu ✅)

→ ÜÇÜ DE EKRANDA. "Yoklukla kanıtlanan kural" hipotezi ÇÜRÜDÜ.
→ Sorun ÜRETİM değil, OKUMA: kanıtlar ekrandaydı ve altı mercek üçünü de
  adlandırmadı. Bu **D151'in 2. vakası** (5. vuruş vakası), yeni ders değil.
⛔ VE OKUMA HATASININ BİÇİMİ ÖĞRETİCİ:
   ② DEVAMLILIK duvarı gördü → "Lunar Control Wall · interacting with wall
     BUTTONS" — otuz bir avuç diskini DÜĞME sandı.
   ⑤ ARKA PLAN duvarı gördü → "massive vertical wall" — üstündekileri hiç
     saymadı (kendi kategorisi ⑤ "sayım"dır).
   Yani mercek görmedi DEĞİL; YANLIŞ NESNE ADLANDIRDI. SPEC'in C bloğu
   "31 parlak disk" diyor ve o blok verilmedi (mod V) → D129'un maliyeti.
```

## ⑪.4 ⛔ YENİ BULGU — KURGU BLOK TAKASI, ŞERİT GÖRMEDİ

```
Izgara kareleri (sahne başlangıcı + 5 s) planın sahne haritasıyla eşlendi:

 sn   plan                              ekranda                        
  5   S0  HOOK: dik duran anahtar       dik duran anahtar, insansız    ✅
 15   S1  açılan boşluk                 kadın yürüyor, iniç sağda      ✅
 25   S2  bot köprüsü + TOHUM yaması    monolit + parlak küre          ✗ plan dışı
 35   S3  VİRAL 1: resif (tepe)         tepe geniş, figür küçük        ✅
 45   S4  botlar tutmaz                 yürüyüş, profil                ✅
 55   S5  sağ avuç (kayma)              diz çöküş, el uzatma           ✅
 65   S6  KOPUŞ makro                   makro el + gömülü disk         ✅
 75   S7  sırt: hat önde                ayakta, parçalanmış levhalar   ✅
 85   S8  DUVAR (31 disk)               ANAHTAR tutma                  ✗ TAKAS
 95   S9  VİRAL 2: duvar dağılır        makro el + anahtar             ✗ TAKAS
105   S10 anahtarı almak                DUVAR (diskli)                 ✗ TAKAS
115   S11 anahtar basamak olur          DUVAR geniş plan               ✗ TAKAS
125   S12 DORUK: son avuç               diz çöküş, sırtı dönük         ✅
135   S13 VİRAL 3: levha bırakılır      levhada yatıyor                ✅
145   S14 FİNAL: iki karanlık avuç      ayakta, levhaların yanında     ✅

⛔ S8-S11 bloğu: ANAHTAR bloğu ile DUVAR bloğu YER DEĞİŞTİRMİŞ.
   Sonuç: TOHUM (S2'nin tek yaması) → ödemesi (duvar) arası mesafe değişti,
   ve novumun ikinci nesnedeki kanıtı doruktan ÖNCE değil, doruğa BİTİŞİK
   geldi. ONERME §5'in "kurulum → doğrulama → sonuç" dizisi bozuldu.

⭐ VE HİÇBİR KAPI BUNU GÖREMEZDİ — bu bir ÖLÇÜM, suçlama değil:
   ④c İNSAN ŞERİDİ `-11111111111111`. S0 dışındaki 14 sahnenin 14'ü tek
   insanlı olduğu için şerit SABİT; blok takası şeridi hiç değiştirmez.
   D118 şeridi "kaç GÖVDE" diye sorar; içerik sırasını sormaz ve
   tek-figürlü filmde bu ekseni tamamen kör eder.
   → YENİ DERS: D163 (kapısı ⑪ ızgara karesi + SPEC sahne haritası).
```

## ⑪.5 ⛔ MOD D KOŞUSU **DURDURULDU** — master geçerli değil

```
Faz 1'in QA yarısı bilerek KOŞULMADI. Sebep tek satır [D150]:
  «filigranlı master master değildir ve mercekler onu ölçmemiş sayılır.»
Filigran ölçüldü ve doğrulandı; üstüne kuyruk kartı ve loudness ihlali var.
Bu master'a koşulacak altı mercek, koşulduğu anda geçersiz olurdu —
altı temiz oturum ve saatler.

⭐ KAPI TAM OLARAK İŞİNİ YAPTI: Faz 0'da yazılan üç aracın üçü de bu koşuda
   iş gördü — kuyruk kartını freezedetect, filigranı köşe testi (kalibre
   edildikten sonra), filigranın habercisini rapor_kontrol ⑤ SUSKUNLUK.

MOD D İÇİN ÖN KOŞUL — sırayla:
  1. Filigran kararı (sahibin): kaynakta filigransız ihraç / post temizleme
  2. Kuyruk kartı 150,10-155,08 kesilir → gövde 150,1 s kalır
  3. Loudness −14 LUFS / −1,0 dBTP'ye normalize edilir
  4. ⑪ yeniden koşulur (kart yok · filigran yok · loudness kilitte)
  5. rubrik_paketle.sh yeni master'la (künyeye süre/çözünürlük girer)
  6. Altı paket, altı temiz oturum → rapor_kontrol.py
```

## ⑪.6 ② KİLİT ÇELİŞKİSİ DEFTERİ — 9 ⬜ AÇIK maddenin durumu

| # | madde | ⑪ sonrası |
|---|---|---|
| 6 | ② "Counter Logic N/A" ↔ SPEC üç sayaç | ⬜ AÇIK kalır — sayaç EKRANDA var (disk, duvar), ② okumadı; mod D'de tekrar sorulur |
| 7 | avuç sayacı 2→0 hiçbir mercekte yok | ⚠️ KISMEN: avuç diski S6 makrosunda GÖRÜNÜYOR; parlak↔karanlık DEĞİŞİMİ tek karede ayırt edilemedi → mod D + a/b kare çifti [D151 çözümü] |
| 8 | 31 diskli duvar anılmadı | ✅ KAPANDI — duvar 100-120 s'de VAR; ②/⑤ gördü, YANLIŞ adlandırdı |
| 9 | ① "havadan ses" 🔴 | ⬜ AÇIK — ses kanalı var, sessizlik yok; temaslı↔havadan ayrımı kulakla, mod D'de |
| 10 | ① "anahtar levhadan geçiyor" | ⬜ AÇIK — kare gerek (1:31) |
| 11 | ⑥ "anahtar 25 cm → 80 cm" | ⚠️ S0'daki anahtar ile S8'deki anahtar ekranda GÖRÜNÜR biçimde farklı ölçekte; cetvel adlandırılmadığı için ⑥'nın FAIL'i yine düşer [Kart F2], ama bulgu ayakta → mod D |
| 12 | ① "düşen disk" 2:20 | ✅ KAPANDI — S14'te disk düşmüyor; kadın ayakta, levhalar yerinde |
| 1-5 | ⑩'da düşen beş bulgu | ✅ değişmedi — beşi de planda yazılı |

---

## ⑪.7 FİLİGRAN — KAYNAK TESPİTİ VE ÜÇ SEÇENEĞİN ÖLÇÜMÜ (01.09.2026)

```
TAM KONUM (4K)   merkez (3475, 1800) · çap 150 px · siyah daire içinde cyan
                 "play" üçgeni · oransal (0,905 · 0,833)
HER İKİ İHRAÇTA  4K master ve 720p ihraç — ikisinde de AYNI ikon, aynı oranda.

⭐ KAYNAK TESPİTİ — filigran KLİPTEN DEĞİL, İHRAÇTAN geliyor:
   ham Veo klibi (`~/Downloads/__second_single_unbroken (93).mp4`) sağ altta
   GRİ DÖRT KÖŞELİ SPARKLE taşıyor — üç örnekte de aynı yerde.
   Master'daki ikon ise CYAN PLAY ÜÇGENİ. İki farklı işaret ⇒ cyan üçgen
   üretim aracının değil, KURGU/İHRAÇ adımının filigranıdır.
   → Bu bir AYAR sorunudur: klipler ve kurgu sağlam, yalnız ihraç kirli.

SEÇENEKLERİN ÖLÇÜLMÜŞ MALİYETİ
 (a) FİLİGRANSIZ İHRAÇ   kadraj kaybı 0 · yeniden üretim 0 · yalnız ihraç ayarı
                         ⭐ ÖNERİLEN — kart kesme ve loudness ile AYNI seansta
 (b) delogo=x:3390 y:1715 w:175 h:175   TEST EDİLDİ (75 s metal · 105 s duvar ·
                         145 s regolit): filigran TAMAMEN gidiyor ✅ ama yerine
                         175×175 px YUMUŞAK YAMA kalıyor. Düz yüzeyde (duvar)
                         görünmez; TANELİ regolitte ve çentikli metalde GÖRÜNÜR.
                         ⛔ Yama her karede AYNI YERDE → ⑤ bunu "static soft
                         patch, bottom right" diye yeniden yakalar. Filigranı
                         bir artefaktla değiştirmek D150'yi kapatmaz.
 (c) KIRPMA              ikon köşeden %10,2 / %16,7 içeride → temizlik kadraj
                         genişliğinin ~%12'si. İniç SAĞ ÜÇTE BİRDEN çıkar,
                         §0.13 Kart 9 ekran yönü kilidi bozulur. ⛔ ELENDİ.
 (d) KABUL               ⛔ D150'ye aykırı: filigranlı master master değildir.
```

## ⑪.8 İKİ FİLİGRAN, İKİ KAYNAK — VE SAHTE 4K (01.09.2026)

```
KAYNAK KLİPLER BULUNDU — 15 klip, hepsi 10,005 s, 1280×720, sesli,
master'dan önce yazılmış (09:44-10:51 · master 10:53):
   13 × `_MOTION_—_Scene_of_*.mp4`              → ⛔ BEYAZ SPARKLE filigranı VAR
    2 × `Woman_{sliding,leaving}_..._202609011051.mp4` → ✅ FİLİGRAN YOK

⭐ İKİ AYRI FİLİGRAN, İKİ AYRI ADIMDA:
   ① üretim adımı  → beyaz sparkle (Veo/Flow ücretsiz katman) · 13/15 klipte
   ② ihraç adımı   → cyan "play" üçgeni · master'ın 15/15 sahnesinde
   Master'da sparkle görünmüyor, cyan üçgen görünüyor ⇒ birleştirme/upscale
   aracı kendi işaretini basıyor.
⭐ VE FİLİGRANSIZ ÜRETİM MÜMKÜN: iki klip aynı gün, aynı akışta, filigransız
   üretilmiş. Yani ① adımı bir AYAR/KATMAN sorunudur, teknik zorunluluk değil.

⛔ SAHTE 4K — ÖLÇÜLDÜ
   master 3840×2160 yazıyor; kaynak kliplerin hepsi 1280×720.
   66. saniyeden alınan 1:1 kesit (600×400 px) tamamen bulanık: gren yok,
   metal dokusu yok, kenarlar yumuşak. Bu upscale'dir, çözünürlük değil.
   → `KURGU_RITMI §6` ihraç kilidi (1440p+) SAYIYLA karşılanıyor, GÖRÜNTÜYLE
     karşılanmıyor. Upscale adımı çözünürlük katmıyor ama filigran taşıyor.

⛔ KAPSAM UYARISI — BU DEPO ÜRETİM YAPMAZ.
   Depo yalnız .md üretir: plan · promptlar · SPEC. Üretim, birleştirme ve
   ihraç PROJE SAHİBİNİN AYRI HATTINDA yapılır. Bu bölümdeki her şey bir
   ÖLÇÜMDÜR (ffprobe/ffmpeg ile okuma — ⑪ ölçüm kapısı, AGENTS ortak adım),
   bir üretim önerisi değildir.
   Ölçümün üretim hattına söylediği tek cümle: **filigranın ikisi de depo
   dışından geliyor ve ikisi de o hattın AYARIDIR** — ① üretim katmanı
   (2 klip zaten filigransız, yani mümkün), ② birleştirme/ihraç aracı.
   Depo tarafının işi bu ölçümü kaydetmek ve kapıyı tutmaktır: filigranlı
   master mod D'ye giremez [D150].
```
