# 🔍 THE STONE SKY — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_STONE_SKY_MOON_FILM.md`
> **Teknik QA (VIDEO_QA):** ✅ **4/10 Ⓥ** · 05.08.2026 · ham: `../02_HAM_RAPORLAR/THE_STONE_SKY_TEKNIK_HAM.md`
> **Mantık QA (MANTIK_QA):** ✅ **4.0/10** · 05.08.2026 · ham: `../02_HAM_RAPORLAR/THE_STONE_SKY_MANTIK_HAM.md`
> **Senaryo QA (SENARYO_QA):** ⚠️ **5/10 Ⓥ ŞARTLI** · 05.08.2026 · ham: `../02_HAM_RAPORLAR/THE_STONE_SKY_SENARYO_HAM.md`
> **Karakter QA (KARAKTER_QA):** ✅ **6/10** · 05.08.2026 · ham: `../02_HAM_RAPORLAR/THE_STONE_SKY_KARAKTER_HAM.md`
> ⭐ **KARAKTER_QA rubriğinin İLK çalıştırması** ve projede **dört mercekle
> aynı gün ölçülen ilk film.** Dördü de mod V / yalnız-video koştu; belge
> soruları aşağıda plan dosyasından cevaplandı.
>
> **Dört raporun ortak üç bulgusu:** ① 1:40 klon (dört rapordan üçünde
> BLOCKER — planın S10-B "klon sıcak noktası" uyarısının TAM kendisi),
> ② 2:10 gömülü başlık kartı ("THE STONE SKY" — planda yasak),
> ③ rover tasarım kayması 0:50 ↔ 1:45.

---

## 📼 KÜNYE — plan ↔ ekran

```
PLAN                          EKRAN (raporların ölçümü)
Süre        140 s             135 s                     −5 s
Sahne       14 × 10 s         12-13 blok sayıldı        eşleme aşağıda
Kesme       sahne sınırı 13   raporlar "çok kesme" saydı — 7'si PLANLI
            + planlı iç 7       sahne içi kesme (aşağıda, madde A)
Diyalog     5 replik / 3 sahne  2 konuşma gözlendi       −3 replik ⚠️
İnsan       tam 1 (21/21)     1:40'ta İKİ               🔴 ihlal
Metin       sıfır (no text)   2:10 başlık kartı         🔴 ihlal
```

---

## 🗺️ SAHNE EŞLEME — plan ↔ mantık raporunun envanteri

> Raporlar kendi numaralarını kullandı (mod V kuralı). Eşleme sonradan
> yapıldı; plan sahneleri 10'ar saniyelik ızgarada.

| Plan | İçerik (plan) | Rapor bloğu | Güven |
|---|---|---|:---:|
| S0 0:00-0:10 (kesme 5.0) | HOOK — matkap + çatlak | S1 0:00-0:04 + S2 0:05-0:09 | ✅ planlı kesme 0:05'te GÖRÜLDÜ |
| S1 0:10-0:20 | Küçük halka — ÇEHOV 1 | S3 0:10-0:19 "geysers erupt" | ⚠️ minyatür kural sahnesi büyük erüpsiyon gibi okunmuş |
| S2 0:20-0:30 (kesme 4.0) | KONİ PATLIYOR + binme | S4 0:20-0:29 "runs to rover" | ✅ |
| S3 0:30-0:40 | ⭐ VİRAL — taş sütunu, insansız | S5 0:30-0:39 "sky debris" | ✅ **kesilemez sahne** |
| S4 0:40-0:50 (kesme 5.0) | Dışa kaçış — ÇEHOV 2 | S6 0:40-0:55 sürüş | ✅ |
| S5 0:50-1:00 | Sütun sırtı geçiyor | S6 içinde erimiş | ⚠️ ayrı okunamadı |
| S6 1:00-1:10 (kesme 6.0) | DIŞ HALKA KAPANIYOR | S7 0:56-1:09 kabin/analiz | ⚠️ diyalog S6+S7'den buraya toplanmış |
| S7 1:10-1:20 | Hesap — AI analizi (nefes) | S8 1:10-1:29 "canyon dodging" | 🚨 nefes sahnesi yerine KANYON — planda kanyon YOK |
| S8 1:20-1:30 (kesme 3.0) | ⭐ DORUK — ters dönüş | S8/S9 içinde | 🚨 **ters dönüş ekranda OKUNMUYOR** (aşağıda madde E) |
| S9 1:30-1:40 | ⭐ VİRAL — içe koşu (tek çekim) | S9 1:30-1:35 "gap jump" | 🚨 planda uçurum atlayışı YOK (§0.14: sıçrama bilerek yok) |
| S10 1:40-1:50 (kesme 6.0) | Çatlak aracı yutuyor → yaya | S10 1:36-1:49 kaza + koşu | ✅ içerik ≈ · 🔴 **klon tam S10-B iniş anında** |
| S11 1:50-2:00 (kesme 5.0) | ÇİZGİ + BEDEL — karot eziliyor | S11 1:50-1:59 "rock geyser" | ⚠️ karotun ezilmesi raporlarda hiç geçmiyor |
| S12 2:00-2:10 | OVERVIEW — göz (kapak adayı) | — | 🚨 **bulunamadı** |
| S13 2:10-2:20 | FİNAL — gözün içinde, bekleyiş | S12 2:00-2:09 oturuş + 2:10 kart | 🚨 bekleyiş "yenilgi" okunmuş; kart planda YOK |

```
PLANLANAN 14 SAHNE:  11 izlenebildi · S5 belirsiz · S12 (overview) BULUNAMADI
PLANSIZ İÇERİK:      kanyon kovalamacası · uçurum atlayışı · başlık kartı
DERS 62 ÖRÜNTÜSÜ:    filmin son planlı görüntü bloğu yine sorunlu — S12/S13
                     yerine oturuş + başlık kartı (4. vaka: Ring Walker,
                     Holding Field, The Herd, şimdi Stone Sky)
```

---

## 📖 FLAGS FOR DOCUMENT CHECK — dört raporun soruları, plan cevapları

### A · TEKNİK — "vakum mu, ince atmosfer mi?" (0:00)
**Cevap: İNCE ATMOSFER.** World Bible: %1.4 basınçlı azot; ses "thin and
muffled" taşınır, toz 40 saniyede çöker. → Dışarıda duyulan ses ve asılı toz
**tasarım gereği.** Raporun "sound in apparent vacuum" bulgusu ve buna bağlı
Diyalog/Ses kesintisi **düşer.** Ama "debris columns FREEZE" (0:30) düşmez —
plan "settles, never hovers" der; donma yine ihlaldir.

### B · TEKNİK — "kesmeler tanımlı bir kurgu mu?" (0:05)
**Cevap: EVET, hem de saniyesi yazılı.** Plan §0.16: 14 sahne sınırı + 7
planlı sahne içi kesme: S0 5.0 · S2 4.0 · S4 5.0 · S6 6.0 · S8 3.0 ·
S10 6.0 · S11 5.0. Raporun gördüğü 0:05 kesmesi **S0'ın planlı 5.0s
kesmesinin ta kendisi**; 0:09/0:19/0:30 sahne sınırları. → Teknik raporun
"0:05 🔴 BLOCKER hard cut" bulgusu ve Kamera 3/10'un kesme bileşeni
**GEÇERSİZ** (Ders 61 örüntüsü — mod V'de kesme yargısı belgesizdi; rapor
soruyu doğru sordu ama BLOCKER da yazdı). Listede OLMAYAN kesme raporlanmadı.

### C · TEKNİK — "yürüyüş mü, düşük-g sıçrayışı mı?" (1:36)
**Cevap: KOŞU — uzun, ALÇAK, DÜZ adımlar** (adım 3 m, yükseklik 0.5 m,
"full real-world speed"). Ağır çekim ve süzülme §0.14 ile yasak. → Raporun
"moonwalk/slide" bulgusu **GERÇEK ihlal**, MAJOR doğru.

### D · SENARYO — "S4 (gök taşları) viral ara sahne mi?" (0:30)
**Cevap: EVET.** Plan S3 = viral, insansız taş sütunu, §0.10: "KESİLEMEZ".
→ Kesim listesindeki "S4'ü kes" reçetesi **REDDEDİLDİ** (Kaleida emsali —
üçüncü kez: dokümansız eleştirmen viral arayı stall sanıyor).

### E · SENARYO — "plan bir doruk ilan ediyor mu? 1:36 mı?" 
**Cevap: HAYIR — doruk 1:36 kaza değil, S8 (1:20-1:30) TERS DÖNÜŞ.**
Planın tamamı şu okumaya kurulu: kadın kaçamayacağını HESAPLAR ve bilerek
tehlikenin kaynağına döner (tek güvenli yer koninin dibi — "göz"). Raporun
tek cümlesi *"you cannot outrun a dying planet / resigns to fate"* —
**planın anlamının TERSİ.** İzleyicinin gözünde seçim yok, yenilgi var.
Ters dönüş jesti (direksiyon sola, güç kolu ileri — 3 saniyelik doruk)
ekranda okunmamış. Karakter 4/10 ve Tema 4/10 skorları büyük ölçüde bu
kayıp doruğun puanı → satır bu yüzden de ŞARTLI.

### F · SENARYO — "son planlı sahne 2:00'daki oturuş mu?"
**Cevap: HAYIR.** Plan S12 = OVERVIEW (kapanan halka + temiz göz, kapak
adayı), S13 = gözün İÇİNDE bekleyiş (held frame). Ekranda overview yok,
final "yenilgiyle oturma + başlık kartı" olarak bitmiş. Oturuş S13'ün
bekleyişi olabilir ama overview olmadan "gözde güvende" bilgisi
kurulamıyor → oturuş çaresizlik okunuyor. **Ders 62'nin 4. vakası.**

### G · MANTIK — "kanyon planda var mı?" (1:10-1:35)
**Cevap: YOK.** Plan coğrafyası: düz ova + 400 m sırt + koni. Kanyon,
uçurum ve atlama **model icadı** (Ders 48 — biyom sıçraması — bu filmde de).
Plan S10'da araç 1.2 m'lik ÇATLAĞA saplanır ve 5 m içinde durur; uçmaz.
→ Coğrafya 4/10 bulgusu doğru ve plan da aynı fikirde.

### H · MANTIK — "taşlar yukarı S3, aşağı S8 — çelişki mi?" 
**Cevap: ÇELİŞKİ DEĞİL, FİLMİN NOVUM'U.** Balistik: 40 m/s ile çıkan taşlar
+51 s'den itibaren halka hâlinde geri düşer (dış kenar önce). Yukarı-sonra-
aşağı tam olarak tasarım. → Fizik 5/10'un bu bileşeni düşer; **ama** raporun
gördüğü "dust floats vs rover falls fast" karışık-yerçekimi okuması ayrı ve
gerçek bir üretim sorunu (0.11 g tek değer olmalıydı).

### I · MANTIK + KARAKTER — "rover'ın doğru tasarımı hangisi?"
**Cevap: Rover Bible:** 3.0 × 1.7 m köşeli monokok, 4 × 0.8 m ağ tekerlek,
arka gömme kızakta **0.9 m koyu gri karot silindiri + iki turuncu kayış.**
0:50'deki "dev turuncu tanklar" da 1:45'teki "boş kasa" da spec değil;
kayma çift yönlü. Üstelik plana göre karot S11-B'de TAŞLA EZİLEREK bedel
sahnesini kurar — raporlarda karot hiç görülmemiş → bedel zinciri
(karot + araç kaybı) ekranda kurulmuyor olabilir. Elle doğrulanmalı.

### J · KARAKTER — "göğüs ünitesi düz mü, kutu mu?"
**Cevap: Bible: "scuffed dark grey hard-shell chest pack holding a FLAT
integrated rebreather"** — düz, gömme sırt-nefes ünitesi. 0:05'teki kabarık
kutu spec dışı; EQUIPMENT FRAME LOCK ("kesmede hiçbir ekipman değişmez")
zaten bunu açıkça yasaklıyordu. → MAJOR doğru, üstelik kilit yazılıydı ve
tutmadı.

### K · KARAKTER — "bilek sembolü (sarı/turuncu artı) spec'te var mı?" (0:56)
**Cevap: YOK.** Bible: "a narrow dark band... a slow abstract amber pulse
**and nothing else**." Okunabilir sembol Risk Kartı 5 / no-text ailesine
girer → gerçek ihlal, klip yenilenirse bilek bandı soyut nabza döner.

---

## 📊 DÖRT MERCEĞİN SKORLARI

| Mercek | Skor | Karar | En düşük kategori |
|---|:---:|---|---|
| 🔧 Teknik Ⓥ | 4/10 | REGENERATE | Karakter + Kamera 3 (Kamera kesme bileşeni geçersiz — madde B) |
| 🧩 Mantık | 4.0/10 | STRUCTURAL PROBLEM | Nicelik 1 (klon) · Kostüm-Prop 2 (rover) |
| 📖 Senaryo Ⓥ | 5/10 | REVISE STRUCTURE | Karakter/Tema/Diyalog/Özgünlük 4 |
| 🧍 Karakter | 6/10 | IDENTITY BREAK | Sayı-Ayrışma 1 (klon) |

**Kapsam sınırı çalıştı:** klon dört raporda da görüldü ama yalnız kendi
merceklerinde puanlandı; mantık ve karakter raporları kesme/metin/lip-sync'i
puanlamadan out-of-scope satırına bıraktı. Çift sayım yok.

---

## 🚨 ANA BULGULAR — birleştirilmiş

```
1. 🔴 KLON — 1:40, araçtan İNİŞ anı (S10-B)
   Plan bu segmenti Risk Kartı 4'ün "klon sıcak noktası" ilan etmiş,
   HUMAN COUNT LOCK + "the seat behind her is EMPTY" yazmıştı. YİNE OLDU.
   → Öngörü doğru, metin kilidi yetersiz → DERS 69 (yeni).
   Ucuz kurtarma: iki koşucunun geniş planı kesilir (~2 s), tek başına
   koştuğu kadraj kalır.

2. 🔴 BAŞLIK KARTI — 2:10, "THE STONE SKY" gömülü metin
   Negatif çekirdek "no title card" 21 segmentte yazılıydı → Ders 34'ün
   3. vakası (Dead Approach · Inversion · Stone Sky). Kart kurguda kesilir;
   başlık paketleme aşamasında kapakla verilir.

3. 🔴 ROVER KAYMASI — 0:50 ↔ 1:45 farklı araç + karot hiç görülmemiş
   Recurring Entity kartı (Ders 58) her segmentte yazılıydı; yine tutmadı.
   Dawn Front Kostüm-Prop 1/10 ile aynı örüntü: dosya dolu, model uymuyor.
   Bedel zinciri (karot ezilir) ekranda kurulamıyorsa S11 yeniden üretilir.

4. 🚨 DORUK OKUNMUYOR — ters dönüş (S8) izleyiciye "yenilgi" olarak geçmiş
   Filmin tek cümlesi tersine dönmüş: "geometriyi okuyup kaynağa dön" →
   "kaçamadı, pes etti". S12 overview'un yokluğu bunu kilitliyor: göz +
   temiz merkez görüntüsü olmadan oturuş güvenlik değil çaresizlik okunur.
   → S12 üretilip kurguya girmeden film yayınlanmaz.

5. 🟠 Gölge yönü 0:00 ↔ 0:50 ters — plan güneşi SAĞDA sabitler (AXIS LOCK);
   S6 klibi aynaysa çevirme çözer, değilse yeniden üretim.
6. 🟠 Kabarık göğüs kutusu 0:05 (madde J) · 🟠 karışık yerçekimi okuması
   (madde H) · 🟡 oturuşta ani kir 2:06 (tek yön kuralı) · 🟡 bilek sembolü
   0:56 (madde K).
```

---

## 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 69 (yeni)   Klon sıcak noktası: biniş/iniş HAREKETİ kadraja alınmaz
                   → LESSONS_LEARNED ✅ yazıldı
□ DERS 34 tekrarı  Planlanmamış başlık kartı — 3. vaka
□ DERS 48 tekrarı  Kanyon icadı — düz ova planına rağmen
□ DERS 61 örüntüsü Mod V'de planlı kesme BLOCKER sayıldı (madde B) —
                   rubrik soruyu sordu AMA severity de yazdı; skor düşürücü
□ DERS 62 4. vaka  Son planlı sahneler (S12 overview) ekranda yok
□ DERS 65 ihlali   KARAKTER_QA raporu film adını başlık kartından okudu
                   (rubrikte kural yazılıydı — çalıştırma kaydına işlendi)
□ Karar: kurgu kurtarma listesi → klon geniş planı kes · başlık kartını kes ·
  S6 ayna kontrolü · S12 overview üret · S11 karot doğrula
```
