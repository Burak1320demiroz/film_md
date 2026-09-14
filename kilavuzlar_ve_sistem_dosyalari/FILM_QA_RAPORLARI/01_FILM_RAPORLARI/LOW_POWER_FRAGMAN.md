# 🔋 LOW POWER — FRAGMAN DİKEY · Film QA Kaydı

> Oluşturma: 20.08.2026 · tek mercek (SHORTS_QA), MOD B + INPUT MODE V (belgesiz).
> Kaynak dosya: `yatay_4_dk_filmler/LOW_POWER/LOW_POWER_FRAGMAN_DIKEY.md`
> Ham rapor: `02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_FRAGMAN_SHORTS_HAM.md`
> Kaynak filmin kaydı: [`LOW_POWER.md`](LOW_POWER.md) (teknik QA tek sahneye koşulmuş · senaryo QA geçersiz)
> ⚠️ Bu kaydın ana çıktısı **skor değil, ÜÇ SAPMA + BİR PARMAK İZİ ŞÜPHESİDİR.**

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 📱 SHORTS_QA | ✅ **DOĞRU MERCEK** · Ⓥ mod V · ⚠️ ÖN KOŞU | **skor yok** — rapor n/10 yazmadı | `..._FRAGMAN_SHORTS_HAM.md` |
| 📖 SENARYO_QA | ⛔ koşulmaz [D111 · §0] | — | — |
| 🎨 diğer | ❌ | — | — |

```
KÜNYE (fragman dosyası)  6 vuruş (V0-V5) × 8,000 s = 48,0 s ± 0 · 0 kesme ·
                         0 replik · 6/6 TAM LOCKOFF · ekran metni 0,0 sn ·
                         mekanik ÖRTÜLME · insan sayımı 0/1/1/1/1/1 ·
                         YÜZ yalnız 3 karede (V1·V3·V4) · V2 ve V5'te yüz
                         kadraj DIŞINDA · anahtara TEMAS 0 kare ·
                         sıra: V0 ızgara → V1 fırça → V2 geri dolma →
                         V3 MAVİ → V4 YEŞİL → V5 ANAHTAR (soru + loop)
KURGU (raporun bildirdiği) 64 s · 7 segment · sahneler tam 10'ar saniye ·
                         sonda 4 s "split-screen BAŞLIK KARTI" ve kartta
                         yazı: "KEEP THE LIGHT ON. SOMETHING ELSE GOES DARK."
                         sıra: S0 ızgara → S1 fırça → S2 geri dolma →
                         S3 SERA → S4 KADRANLAR → S5 MAVİ → S6 KART
DOSYA DURUMU             `LOW_POWER_FRAGMAN_DIKEY.md` · ÜRETİM NOTLARI:
                         "yazıldı, üretilmedi (20.08.2026)" · KAPI KAYDI'nın
                         7 kapısının 7'si ⛔ KOŞULMADI. Belge ile ortada
                         dolaşan kurgu birbirini yalanlıyor.
```

---

## 🚨 TEK CÜMLELİK HÜKÜM

**Mercek ilk kez doğru seçildi ve kapılar ilk kez düzgün işledi — ama ölçülen
kurgu BELGENİN KURGUSU DEĞİL: yedi segment, 10 saniyelik klipler, sona
eklenmiş bir başlık kartı ve son üç vuruşu YER DEĞİŞTİRMİŞ bir sıra.**
Fragmanın mekanik merdiveni (ÖRTÜLME) bu sırayla çalışmaz, kapanış vuruşu
soru değil manzara olur ve §2'de ZORUNLU olan loop dikişi fiziksel olarak
imkânsız hale gelir. Üstüne, raporun künyesi (64 s · 7 segment · ~10 s sahne ·
sonda kart) bu rubriğin son üç koşusunun künyesiyle **birebir aynıdır** —
DERS 112 parmak izi kapısı açılır ve süre/segment sayısı hiçbir kapıya
girdi sayılmaz.

---

## ✅ ⑧ FRAGMAN MERCEK KAPISI [D111] — GEÇTİ (depoda İLK)

```
Malzeme FRAGMAN · mercek SHORTS_QA (dikey) ✅ · MATERIAL TYPE: TEASER beyan
edildi ✅ · §14 "Note: Scored as a TEASER" yazdı ✅

⭐ Bu, D111/113'ün yamasının İŞE YARADIĞININ ilk kanıtıdır: Cold Burn
fragmanına SENARYO_QA koşulmuştu ve rubrik fragmanı film sanmıştı.
Bu koşuda rubrik teaser'ı tanıdı ve §14'te "borç bırakmayı" kusur olarak
faturalandırmadı — tam tersine soruyu iletmiş saydı.
```

---

## ✅ ③ KİMLİK KAPISI [D105] — GEÇTİ (3/2 çapa)

> Kural: ham rapor bir film adının altına dosyalanmadan önce, raporun sahne
> listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir. Kartın yazısı
> çapa DEĞİLDİR ve bu koşuda kanıt sayılmadı.

```
ÇAPA 1 — VURUŞ:  rapor S2 "POV close-up, finger tracing line in panel dust"
                 ↔ V2: 100mm makro, 0,6 m, taze tozda parmakla çizilen ve
                 iki kenardan dolan çizgi. Belgeye özgü, metin dışı, başka
                 hiçbir filme uymayan kare.
ÇAPA 2 — VURUŞ:  rapor S4 "hands near analog gauges" ↔ V5: iki özdeş 12 cm
                 kadran, aralarında tek ağır anahtar, el anahtara DEĞMİYOR.
ÇAPA 3 — ÇAPA BLOĞU: rapor "White/orange spacesuit with backpack" +
                 "Red fleece over grey coveralls" ↔ belgenin suit ve iç
                 kıyafet çapa blokları (bordo polar + gri-bej termal tulum).

SONUÇ: 3/2 çapa. Koşu ATIFLIDIR — UNATTRIBUTED değil.
```

**Yine de kimlik ≠ uygunluk:** altı anlatı vuruşunun altısı da belgede var,
ama **sırası bozuk** ve kurguda **yedinci bir segment** var — o segment
hiçbir belgede geçmiyor ve belge onu iki ayrı yerde açıkça yasaklıyor.

---

## 🚨 ⑦ ÇAPRAZ FİLM PARMAK İZİ KAPISI [D112] — ŞÜPHE AÇILDI

> Kural: mod V raporlarında, AYNI rubriğin son iki koşusunun künyesi yan yana
> konur (SÜRE · SEGMENT · ORTALAMA SAHNE SÜRESİ · kart saniyesi). Üçü de ±%5
> içinde aynıysa rapor işlenir ama **süre ve sahne sayısı hiçbir kapıya girdi
> sayılmaz.**

| Koşu | SÜRE | SEGMENT | ORT. SAHNE | KART |
|---|---|---|---|---|
| 06.08.2026 · THE FIRST MORNING · SHORTS_QA | 64 s | — | — | jenerik kartı ✅ |
| 06.08.2026 · THE WRONG SHADOW · SHORTS_QA | 64 s (73,0 künye) | — | — | jenerik kartı ✅ |
| 17.08.2026 · THE BLACK CRADLE FRAGMAN · SHORTS_QA | 63 s | ~7 | ~10 s | başlık kartı 0:58 ✅ |
| *(17.08.2026 · COLD BURN FRAGMAN · SENARYO_QA)* | *62 s* | *7* | *~9 s* | *başlık posteri* |
| **20.08.2026 · LOW POWER FRAGMAN · SHORTS_QA** | **64 s** | **7** | **~10 s** | **kart 4 s, 1:00** |

```
63 → 64 s      = %1,6 fark   ✓ ±%5 içinde
7 → 7 segment  = aynı        ✓
~10 → ~10 s    = aynı        ✓
kart → kart    = ikisinde de var, ikisi de SONDA

🚨 ÜÇÜ DE TUTUYOR → PARMAK İZİ ŞÜPHESİ AÇILDI.
   Rapor işlenir. Ama SÜRE ve SEGMENT SAYISI hiçbir kapıya girdi sayılmaz.
   Operatör dosyanın KENDİ süresini okur ve kurgu kapısını O SAYIYLA koşar.

⚠️ Bu artık dört koşuluk bir desendir ve D70'in ("kurgu 64 s + jenerik
   kartı") beşinci vakasıdır. İki okuma var ve ikisi de mümkün:
   (a) OPERATÖR DESENİ — her teslimde aynı editör alışkanlığı: klip
       süresi belgeden değil kaynak filmden alınıyor ve sona kart ekleniyor.
   (b) RAPOR DESENİ — rubrik/model künyeyi ÖLÇMÜYOR, önceki koşudan
       taşıyor. Tam 10'ar saniyelik bloklar bunun tipik imzasıdır.
   ⛔ İkisini ayırmanın maliyeti ~1 dakikadır: dosyanın gerçek süresini ve
      klip sınırlarını OKU. Bu yapılmadan bu koşudan ders yazılmaz.
```

---

## ⚠️ ④ KURGU KAPISI [D109] — ÖNCE AYIKLA, SONRA SAY [D93]

```
① AYIKLAMA: S6 (1:00-1:04) = 4 s · statik kart · ekranda METİN taşıyor ·
   hiçbir vuruşun parmak izini taşımıyor → SAHNE-DIŞI MALZEME.
   Kurgunun SONUNDA olduğu için: kayda tek satır — "kart 4 s" —
   🔴 loglanır [D70/72] ve sayımın DIŞINDA tutulur.

② SAYIM (karttan sonra):
   a) klip sayısı  6  =  planın vuruş sayısı 6        ✅ TUTUYOR
   b) süre        60 s vs plan 48,0 s = +12 s        ❌ ±2 s bandının dışında

③ ⛔ AMA ⑦ NEDENİYLE bu iki satır kapıya girdi SAYILMAZ. Kurgu kapısı
   bu koşuda KOŞULAMADI — koşulabilmesi için dosyanın kendi süresi okunmalı.

SONUÇ: koşu ÖN KOŞU'dur.
· satır tabloya ⚠️ ŞARTLI girer (bu koşuda zaten skor yok),
· film boyuna bakan kategoriler SAYI TAŞIMAZ: §13 · §14 · §15,
· kesme listeleri ve yeniden üretim siparişleri UYGULANMAZ.
```

---

## ⚠️ ⑨ HİZALAMA KAPISI [D115] — TUTMADI

```
Izgara PLANDAN alınır: sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
Plan: 8 s hook + 8 s klip → 0 · 8 · 16 · 24 · 32 · 40   (bitiş 48,0)
Rapor:                        0 · 10 · 20 · 30 · 40 · 50 (+ kart 60)
Δ:                            0 · +2 · +4 · +6 · +8 · +10   → DOĞRUSAL KAYMA

Sessiz film testi: raporun blokları ardışık ızgara dilimlerinin birleşimi mi?
HAYIR. Doğrusal kayma tek bir şeyi gösterir: kurgu 8 s değil 10 s klip
kullanmış. 10 s KAYNAK FİLMİN klip süresidir; fragman 8 s NATIVE üretilecekti
ve belgede "extend YOK, dikiş YOK" yazıyor.

⚠️ İkinci okuma (D112): rapor ızgarayı ÖLÇMEDİ, VARSAYDI. Tam 10'ar saniyelik
   yedi blok, ölçülmüş bir kurgudan çok varsayılmış bir ızgaraya benziyor.
```

---

## 📒 ② KİLİT ÇELİŞKİSİ DEFTERİ [D96]

> Raporun, belgede YAZILI bir kilide aykırı her bulgusu bulgu listesinden
> ALINIR ve buraya yazılır. Çözüm eylemi = master'ın o saniyesini izlemek
> (~10 sn iş). Sonuç = FİLM SAPTI / RAPOR UYDURDU / ⬜ AÇIK.

| # | Rapor ne dedi | Hangi kilit | Çözüm eylemi | Sonuç |
|:--:|---|---|---|---|
| 1 | §13 CAUSALITY: "S3'te kollar aşağıda, S4'te eller zaten panelde — yaklaşma ve kaldırma atlanmış" (0:37 vs 0:40) | Belge: her vuruş AYRI kliptir, kesme klip ARALARINDA yaşar [D68]; vuruşlar ardışık AN değildir, fragman filmi yeniden anlatmaz [§5 ①] | — (belgeden okunur) | **BULGU DÜŞER** — rubrik altı ayrı lockoff vuruşu arasında eylem sürekliliği aradı. D106'nın teaser sürümü, bu kez §13'te |
| 2 | §14 QUESTION TRANSMITTED · HIGH + NO NARRATION NEEDED · HIGH | Rubriğin kendi kuralı §14: "does it transmit visually, **without text or a caption doing the work**?" · belge: ekran metni 0,0 sn | Kart çıkarılıp 60 s'lik kurgu yeniden izlenir | **⬜ AÇIK · SKOR KİRLİ** — izleyici özeti ("choose between oxygen and food") kartın cümlesinin ("KEEP THE LIGHT ON…") parafrazı. Kart varken bu iki HIGH birlikte verilemez |
| 3 | §1 face morph — S4 (0:40) dahil | Belge V5: yalnız el + defokus çene, **gözler kadraj DIŞINDA**, yüz okunmaz | 0:40-0:49 izlenir: yüz okunuyor mu? | **⬜ AÇIK** — okunuyorsa FİLM SAPTI (kilit ihlali), okunmuyorsa rapor kadrajı yanlış okudu |
| 4 | §3 "push-in camera move" — S3 (0:30) | Belge: **6/6 TAM LOCKOFF**, "the camera does not move at all", V4 sabit | 0:30-0:39 izlenir: kamera hareket ediyor mu? | **⬜ AÇIK → yüksek olasılıkla FİLM SAPTI** (rapor hareketi tarif ediyor) |
| 5 | §5 "S0'da beyaz modüler KUBBELER" | Belge: yedi soluk beyaz-bej **SİLİNDİRİK** modül, yarı gömülü, "ridges, not buildings"; kubbe YOK | 0:05 izlenir | **⬜ AÇIK → yüksek olasılıkla FİLM SAPTI** — istasyon çapası tutmamış; S0↔S5 uyuşmazlığı zaten ikinci kanıt |
| 6 | BASELINE: "Gravity: 1g" | Belge: 0.38g, altı vuruşun altısında | dış vuruşlar izlenir | **⬜ AÇIK** — bulgu değil ama ağır gözlem: hareket Mars gibi okunmuyor |
| 7 | §11 HOOK: "dust storm **rolling in**" | Belge V0: fırtına gelmiyor, ZATEN var; olay güneşin bir kademe sönmesi | 0:00-0:08 izlenir | **⬜ AÇIK** — kurguda gelen bir fırtına cephesi varsa FİLM SAPTI (Mars'ta cephe devirmez, siler) |

---

## ✅ GEÇERLİ KALAN BULGULAR — defterden geçenler

> Bunlar belgedeki bir kilidin İHLALİDİR; rapor işini yapmıştır.

```
🔴 BLOCKER · S6 1:00-1:04 · BAŞLIK KARTI
   Belge iki ayrı yerde yasaklıyor: "Başlık kartı, jenerik kartı, kapak
   karesi kurguya GİRMEZ. İstisna yok." + "ekran metni 0,0 sn" [D70/72].
   Ayrıca kart, güvenli alanın alt 484 px bandına yazı koyuyor (§10) ve
   §14'ün skorunu kirletiyor (defter #2). D70'in BEŞİNCİ vakası.

🟠 MAJOR · S2 0:20-0:29 · TOZ SIVI GİBİ ("magnetic paste")
   ⭐ BELGENİN 1 NUMARALI RİSKİ AYNEN GERÇEKLEŞTİ. Belge şunu yazmıştı:
   "Projenin ölçülmüş en düşük tek skoru bu filmin parçacık skorudur (2/10)
   ve ham bulgu birebir 'dust drifting like zero-g underwater fluid'tir.
   Bu fragmanın mekaniği o malzemedir." Üç katmanlı karşı önlem YETMEDİ.
   → KAPI 2 (Mekanik kapısı) ⚠️ ŞARTLI BATTI (şartlı, çünkü ⑦ açık).

🟠 MAJOR · S2 0:22 · TEMAS ERİMESİ (eldiven panelin içinden geçiyor)
   Belge: "clear structural contact — no merging, no phasing" [D17/38].
   Aynı klipte İKİNCİ batma. V2 bu kurgunun en bozuk klibi.

🟠 MAJOR · S1 0:10 · VIDEO-GAME / UNREAL ENGINE GÖRÜNÜMÜ
   Negatif çekirdek ihlali: "no CGI look, no Unreal Engine look".

🟡 MINOR · S1 0:13 · süzülen fırça hareketi (0.38g ağırlık hissi yok)
🟡 MINOR · S1 vs S5 · suit detayı kayması (sırt ünitesi biçimi, göğüs)
   → Belge bunu ayrıca kilitlemişti: "dust pattern on her shoulders and
     chest does not change between frames" (kaynak filmin ölçülmüş
     karakter bulgusu). Kısmen tutmamış.
```

---

## 🧭 EŞLEME TABLOSU — fragman vuruşları ↔ raporun sahneleri

| Belge | Ne olacaktı | Raporda | Durum |
|:--:|---|---|:--:|
| V0 | IZGARA · 32mm · 12,5 m · lockoff · insan 0 | S0 0:00-0:09 | ✅ yerinde |
| V1 | FIRÇA · 32mm · 6 m · insan 1 | S1 0:10-0:19 | ✅ yerinde |
| V2 | GERİ DOLMA · 100mm makro · yüz kadraj dışı | S2 0:20-0:29 "POV close-up" | ✅ yerinde · ⛔ iki ağır bulgu |
| V3 | **MAVİ** (afiş) — 4. sırada | S5 0:50-0:59 | 🔄 **SIRA BOZUK: 6. sıraya kaydı** |
| V4 | **YEŞİL** — 5. sırada | S3 0:30-0:39 | 🔄 **SIRA BOZUK: 4. sıraya kaydı** |
| V5 | **ANAHTAR** (soru + loop) — 6. ve SON | S4 0:40-0:49 | 🔄 **SIRA BOZUK: 5. sıraya kaydı** |
| — | (belgede YOK, iki yerde YASAK) | S6 1:00-1:04 KART | 🔴 **belgede yok** |

### 🚨 SIRA BOZULMASININ ÜÇ SONUCU — rapor bunu göremez (mod V, SPEC yok)

```
① MEKANİK MERDİVENİ KIRILDI. Belge sırayı gerekçelendirmişti: "ışık
   örtüldü" basamağı (V3 mavi), "örtülmeyen tek yer" basamağından (V4
   yeşil) ÖNCE gelmek ZORUNDADIR — yoksa merdiven ters döner. Kurguda
   yeşil önce geliyor, mavi sonra: izleyici önce kurtuluşu, sonra kaybı
   görüyor. ÖRTÜLME mekaniği bu sırayla kurulmaz.

② FRAGMAN BORÇLA DEĞİL MANZARAYLA BİTİYOR. Kapanış vuruşu artık gün
   batımı; dokunulmamış anahtar (soru vuruşu) sondan bir önceye düştü.
   §2.1'in "V6 SORU" basamağı kayboldu.

③ LOOP DİKİŞİ YOK OLDU — ve loop dikey fragmanda ZORUNLUDUR [§2].
   Belge dikişi ölçüyle kurmuştu: V5'in iki özdeş kadranı ile V0'ın en
   yakın iki gömülü paneli, ikisi de %55 yükseklikte, ikisi de kadraj
   genişliğinin ~%30'u. Son klip gün batımı olduğu için bu çakışma
   fiziksel olarak imkânsız.

⚠️ Rapor bu üçünü de bulamaz ve bulmaması KUSURU DEĞİLDİR: INPUT MODE V,
   SPEC verilmedi. §14 bu yüzden "sıra doğru mu" diye sormadı, yalnız
   "soru ulaştı mı" diye sordu — ve kartın yardımıyla ulaştı sandı.
```

---

## ⚠️ ① SPEC KAPISI [D94] — SEKİZİNCİ VAKA

```
Fragman dosyasında `📋 QA SPEC BLOĞU` HAZIRDI (20.08.2026'da yazıldı) ve
koşu yine MOD V yapıldı. Bedeli sayısaldır:
· §12 "concept-specific negatives" listesi BOŞ koştu — belgenin filme özel
  yasakları (temiz panel 0 kare · sera dışında yeşil 0 kare · anahtara
  temas 0 kare · ibre hareket etmez) hiç sorulmadı.
· §13 PROGRESSION LADDER'ı SPEC'ten alamadı, kendi uydurdu ("Mars storm
  hits → Interior power checked → Exterior aftermath → Final choice") —
  ve o merdiven belgenin merdiveni DEĞİL.
· §1 yüz bulgusu, "V5'te yüz olmamalı" kilidini bilmeden yazıldı.

→ SPEC verilseydi bu koşu ÖN KOŞU değil TAM KOŞU olurdu ve yukarıdaki
  sıra bozulmasını rubrik KENDİSİ yakalardı.
```

---

## 📌 HÜKÜM VE SONRAKİ ADIMLAR

```
SKOR SATIRI: YAZILMADI.
  Üç ayrı sebep, üçü de tek başına yeterli:
  ① rapor kategori skoru (n/10) üretmedi — QUALITY TABLE ROW yok
  ② ⑦ parmak izi şüphesi açık — süre/segment kapıya girmiyor
  ③ ① SPEC kapısı + ④ kurgu kapısı → ön koşu
  → `05_SHORTS_KALITE_TABLOSU.md`'ye satır GİRMEZ [D65: başarısız
    çalıştırma tabloya satır yazamaz].
  → `00_INDEX.md`'ye satır AÇILMAZ (fragman film sayımına girmez).

KESME LİSTESİ / YENİDEN ÜRETİM SİPARİŞİ: UYGULANMAZ (ön koşu).

⛔ SIRADAKİ ADIM OPERATÖRE AİT — ~5 dakika, sıfır maliyet:
  1. Dosyanın GERÇEK süresini ve klip sınırlarını OKU (⑦ bunu şart koşuyor).
     Süre 60 s ve klipler 10'ar saniyeyse → kurgu belgeye göre üretilmemiş.
     Süre 48 s ve klipler 8'er saniyeyse → RAPOR künyeyi uydurdu ve
     D112 iki farklı film için üst üste doğrulanmış olur.
  2. Defterdeki 5 ⬜ AÇIK maddeyi izle (toplam ~50 saniyelik iş):
     0:05 · 0:30 · 0:40 · 0:00-0:08 · dış vuruşların yerçekimi.
  3. KARTI SİL. Tek başına iki BLOCKER ve §14'ün skorunu kirletiyor.
  4. Sırayı belgeye döndür: … → MAVİ → YEŞİL → ANAHTAR. Bu bir kurgu
     işidir, yeniden üretim istemez ve loop dikişini geri getirir.
  5. V2'yi yeniden üret (toz + temas, iki ağır bulgu aynı klipte).
     İkinci deneme de batarsa belgedeki PLAN B çalıştırılır:
     mekanik tozdan GÖLGEYE taşınır, risk 5/9 → 4/9 iner.
  6. Sonra SPEC bloğu ile MOD D koşusu yap — depoda mod D hâlâ hiç
     denenmedi ve bu dosya buna hazır.
```

---

## 🆕 DERS ADAYI — numara SAHİBİNE ait

> ⚠️ Numara verilmedi: LESSONS_LEARNED'de en yüksek numara 116 ve sahibin
> commit'lenmemiş ders çalışması açık. Onaylanırsa metin buraya girer:
> `LESSONS_LEARNED.md` + `DERSLER/` ilgili tematik dosya + bu kaydın linki.

```
ADAY DERS — "FRAGMAN KURGUSU BELGENİN SIRASINI DEĞİL FİLMİN SIRASINI ALIYOR"

Gözlem: iki fragman teslimi üst üste aynı üç sapmayı yaptı —
  (a) klip süresi belgeden (8 s) değil KAYNAK FİLMDEN (10 s) alındı,
  (b) sona başlık kartı eklendi [D70'in 4. ve 5. vakası],
  (c) vuruş sırası belgenin MEKANİK gerekçesini değil filmin
      KRONOLOJİSİNİ izledi (Low Power: sera ve kadranlar, gün
      batımından önceye alındı — çünkü filmde öyle).
Sebep tahmini: fragman dosyası kaynak filmin klasöründe duruyor ve
  operatör kurguyu filmin alışkanlıklarıyla kuruyor. Fragmanın kendi
  ızgarası (8 s) ve kendi sırası (mekanik merdiveni) belgede yazılı ama
  KURGU MASASINDA kimse okumuyor.
Karşı önlem önerisi: FRAGMAN_KILAVUZU §2.2'nin kurgu kapısına iki satır:
  □ KLİP SÜRESİ = fragmanın kendi süresi (dikeyde 8 s), kaynak filminki DEĞİL
  □ VURUŞ SIRASI = belgenin mekanik merdiveni; kaynak filmin sahne
    numaraları sıralamayı BELİRLEMEZ (fragman kronoloji izlemez)
  ve loop dikişi maddesi zaten var — ama sıra bozulunca ÖNCE o ölür.
```
