# 🪐 THE RING LIGHT — FİLM QA KAYDI

> **Film:** THE RING LIGHT · 16:9 yatay · 2-4 dk · `yatay_2_4_dk_filmler_uzay/THE_RING_LIGHT/THE_RING_LIGHT_ORBITAL_DOCKING_FILM.md`
> **Plan:** 14 sahne (S0-S13) · 140 s · 0 kesme · 14/14 lockoff · 7 replik (7/7 gövdesiz AI)
> **Kurgu:** 144 s · 15 klip / 14 kesme — **14 sahne + 4 s jenerik kartı**
> **QA tarihi:** 12.08.2026 — dört koşu aynı gün: üç genel mercek **mod V**,
> bir de filmin KENDİ rubriği (durdu)
> **Ham raporlar:** `../02_HAM_RAPORLAR/THE_RING_LIGHT_{TEKNIK,SENARYO,KARAKTER,FILME_OZEL}_HAM.md`

---

## 📊 DÖRT KOŞUNUN DURUMU

| Mercek | Skor | Verdict | Koşu |
|---|:--:|---|---|
| 🔧 VIDEO (teknik) | **7.0/10** Ⓥ | REGENERATE (1 🔴) | ⛔ **ÖN KOŞU** — SPEC hazırdı, mod V koşuldu [D94] |
| 📖 SENARYO | **6.0/10** Ⓥ | REVISE STRUCTURE | ⛔ **ÖN KOŞU** — aynı sebep [D94] |
| 🧍 KARAKTER | **8.5/10** | DRIFTS BUT RECOVERABLE | ⚠️ ŞARTLI — pasaport filmin %14'ünden [D97] |
| ⭐ FİLME ÖZEL (MOD F) | — | **CLIP COUNT MISMATCH — RUN STOPPED** | **ölçüm YOK → DERS 93** |

```
⭐ Bu filmin QA'sı depodaki hiçbir filme benzemiyor: FİLMİN KENDİ RUBRİĞİ VARDI
   (12.08.2026'da yazıldı, kırk küsur sayısal kilidi gövdesinde taşıyor) ve
   koşuda TEK SATIR bile ölçmedi. Ölçen üç mercek ise filmin hiçbir kilidini
   bilmiyordu — çünkü planın §0.15'indeki HAZIR SPEC bloğu hiçbirine
   yapıştırılmadı.

   SONUÇ: elimizdeki üç skor "bu film tasarlandığı gibi mi çıktı" sorusunu
   ölçmüyor. Üçü de "bu kurgu kendisiyle çelişiyor mu" sorusunu ölçüyor.
```

---

## ⭐ ANA BULGU 1 — KURGU KAPISI İLK KEZ TAM GEÇTİ, SONRA 4 SANİYELİK KARTLA KAPANDI

Depoda D72/D81'den beri ölçülen kurgu kapısının (planın sahneleri kurguya
girdi mi, sırasıyla mı, doruk ekranda mı) **ilk tam geçişi** bu film:

| Kapı maddesi | Plan | Kurgu | Sonuç |
|---|---|---|---|
| Sahne sayısı | 14 | 14 sahne klibi | ✅ |
| Süre | 140 s | 140 s + 4 s kart | ✅ (sahne malzemesi) |
| Izgara | 14 × 10 s | üç raporun üçünde de 10 s'lik ızgara | ✅ |
| DORUK (S8 karotu bırakmak) | 1:20-1:30 | 📖 "S9 1:20-1:30 payload canister ejected" · 🔧 "canister ejection 1:26" | ✅ **ekranda** |
| TEMAS (S11) | 1:50-2:00 | 🔧 "docking collision at 1:56" | ✅ |
| İnsan vuruşu (S12 avuç avuca) | 2:00-2:10 | 🧍 "hand-hold 2:08" | ✅ |
| Final (S13 tünel) | 2:10-2:20 | 📖 "Int. Tunnel 2:10-2:20" | ✅ |
| İnsanlı sahne sayısı | 6 | 🧍 tabloda 6 sahne | ✅ |
| **Jenerik kartı** | **0 kare metin** | **2:20-2:24 "THE RING LIGHT" yanık kart** | 🔴 **İHLAL** |

```
⭐ Cold Burn (12/30 sahne) ve Blind Return (S15 yok, S16↔S17 ters) ile aynı
   kapıdan geçen bu film HİÇBİR SAHNESİNİ KAYBETMEDİ. Düşük hikaye skorunun
   kökü bu kez kurgu kaybı DEĞİL — Third Dune'un açtığı kontrol grubu bu
   filmle ikinci kez doğrulandı.

🔴 Tek kurgu ihlali jenerik kartı: D70/72 zincirinin 5. VAKASI
   (Unbroken City 2:40 · Starless Circle 2:50 · Stone Sky 2:10 ·
    Third Dune 4:00 · Ring Light 2:20).

⛔ VE BU FİLMDE UYARI İKİ YERDE BİRDEN YAZILIYDI:
   §5 KAPAK: "Kapak çıktısı film kurgusuna ASLA eklenmez [Ders 72]"
   §0.18 ⑦ KURGU KAPISI: "ekran metni = 0.0 sn (jenerik/başlık kartı
     DAHİL — kapak dosyası klip zincirine KARIŞMAZ)"
   Yani bu kez eksik cümle yok; D84'ün kurgu tarafı: YAZILI KONTROL
   MADDESİ, KOŞULMADIĞI SÜRECE KONTROL DEĞİLDİR. Kapının maddesi
   ancak MEKANİK olarak ölçülürse tutar — ve onu ölçecek alet
   (filme özel rubrik) tam bu kartın yüzünden durdu.
```

**Ve asıl bedel:** o 4 saniyelik kart klip sayısını 15'e çıkardığı için filmin
kendi rubriği `CLIP COUNT MISMATCH` ile durdu. Bilinen, ucuz, kurguda 4
saniyede düzelen bir hata, filmin **tek gerçek ölçüm aletini** susturdu.
→ **DERS 93**

---

## ⭐ ANA BULGU 2 — KİLİT ÇELİŞKİSİ DEFTERİ (4 açık madde)

Üç mod V raporu, planın YAZILI kilitlerine aykırı dört olay bildirdi. Rapordan
hangisinin doğru olduğu **çözülemez**: ya film saptı (Ring Walker örüntüsü) ya
rapor uydurdu (Low Power örüntüsü). İkisinin de emsali bu depoda var.

| # | Rapor ne dedi | Hangi kilit | Çözüm | Sonuç |
|:--:|---|---|---|---|
| 1 | 🔧 2:14 "lip-sync drift · *Wait, there is something out there*" · 📖 2:10 "*We are entering the transfer tunnel now*" · 📖 replik listesinde "Shadow entry…", "Sonic warning…" | §0.11 **7 replik, 7/7 gövdesiz AI, iki insan da HİÇ konuşmaz; ekranda ağız YOK** · S12-S13 tamamen sessiz | master'ın 0:50-1:00 ve 2:00-2:24 aralığını **dinle**; ağız oynuyor mu, replik Türkçe mi | ⬜ AÇIK — ⭐ kısmi teşhis çıktı: **"Shadow entry" bir replik değil, S4-B promptunun PHYSICS satırıdır** (`grep` ile bulundu; aynı promptun AUDIO'su "No voices" diyor) → **DERS 99**, prompt nesri sese sızmış olabilir |
| 2 | 🧍 2:00 "visors up / retracted", "unhelmeted faces" · 🔧 "visors up/removed" | §0.12 **kask 14/14 TAKILI, vizör KAPALI ve MÜHÜRLÜ, durum değişimi 0** | 2:00'daki kareye bak: vizör çerçevesi görünüyor mu | ⬜ AÇIK — muhtemel sebep D95 (berrak vizör "vizör yok" okunuyor) |
| 3 | 🔧 1:56 "sparks and metal shards", "collision debris" | §0.12 **ATEŞ 0 kare** (kıvılcım dahil) · **PARÇACIK: tek serbest parçacık S11'deki 6-8 boya pulu** · temas 0.2 m/s, tek yumuşak yapısal şok | 1:55-1:58'i kare kare izle: kıvılcım mı, boya pulu mu | ⬜ AÇIK — doğrulanırsa 🔴 (mod V bunu 🟠 yazdı) |
| 4 | 🔧 1:04 · 1:28 · 1:56 "airborne sound in vacuum" 🔴 | §0.12 **dışarıda ses 0**; duyulan her şey gövdeden/telsizden gelir — S11 temas TOK'u ve S8 kol TOK'u **planlı ve meşrudur** | üç zaman kodunu dinle: kaynak gövde mi hava mı | ⬜ AÇIK — 1:56 büyük olasılıkla **meşru** (S11 temas TOK'u), 1:04 ve 1:28 gerçek ihlal adayı |

```
⛔ KURAL (DERS 96): bu defter kapanmadan hiçbir bulgusu "film hatası" olarak
   ders/onarım listesine geçmez. Üç tablo satırı da bu yüzden ⚠️ ŞARTLI.
```

---

## ⭐ ANA BULGU 3 — FİLMİN ADINI TAŞIYAN OLAY ÜÇ RAPORUN HİÇBİRİNDE YOK

Plan §0.10: S9 (1:30-1:40) filmin ışık rejimi değişimidir — güneş kademeli
olarak kapanır (1.5 / 3.5 / 5.0 s ısırıklar, 6.5 s'de son ışık gider), 7.0
s'de **halka ışığı** açılır ve S9-S13 boyunca tek dış ışık odur. Filmin adı da,
kapak adayı da, ikinci viral arası da budur.

```
🔧 raporun ışık envanteri (144 s'in tamamı için):
   "Light sources: Single primary hard directional source (sun)"
   Işık: 8/10 · faz değişimi, tutulma, altın dolgu — HİÇ ANILMIYOR.
📖 raporun sahne haritası 1:30-1:40 için:  "Ext. Orbit · final approach vector"
🧍 rapor 2:00 sonrası ışığı hiç tarif etmiyor.
```

İki okuma da mümkün ve ikisi de operatörün 10 saniyelik bir kontrolüyle
kapanır:

```
A) TUTULMA EKRANDA YOK / OKUNMUYOR  → filmin doruğundan sonraki en büyük
   vuruşu üretimde kayboldu. D62 ailesinin yeni vakası olur.
B) TUTULMA EKRANDA VAR              → üç mercek de filmin en güçlü 10
   saniyesini raporlamadı; bu da merceklerin körlüğüdür, filmin değil.
```

⬜ **AÇIK — master 1:30-1:40 izlenerek kapatılır.** (📖 raporun 0:50-1:00 için
yazdığı "shadow entry" repliği, tutulmanın **yanlış sahneye** düşmüş olma
ihtimalini de açık bırakıyor.)

---

## ⭐ ANA BULGU 4 — SAYAÇ A'NIN SIFIRI DUYULMUYOR

Plan: 8 → 0 giden darbe sayacının son değeri S11'de **"Sıfır."** repliğiyle
söylenir; §0.9'un tamamı bu tek kelimeye bağlıdır.

📖 raporun duyduğu 9 repliğin listesinde **"Sıfır." YOK.** Planın 7 repliğinden
6'sı listede (Sekiz darbe · Yük beşikte · İptal edildi · Her ötelemede · Beşik
boş · Yirmi metre), yerine listede olmayan üç İngilizce/yabancı replik var
(Shadow entry · Sonic warning · We are entering).

⬜ **AÇIK — master 1:52-1:55 dinlenerek kapatılır.** Kayıpsa: filmin iki
sayacından biri son değerini ekranda hiç söylememiş olur (D78 örüntüsü,
4. vaka).

---

## ⭐ FLAGS FOR DOCUMENT CHECK — CEVAPLAR

### 🔧 VIDEO_QA

**S1. "14 kesme planın sahne sınırlarıyla hizalı mı?"**
→ **EVET, 14 sahne sınırı planlıdır** (§0.8: 14 sahne × 10 s, sahne İÇİ kesme 0).
Ama kesme sayısı 14 değil **13 olmalıydı**: 14 klip = 13 sınır. 14. kesme
jenerik kartına ait. Klip zincirindeki hiçbir kesme ihlal değildir; **kart
ihlaldir**.

**S2. "2:00 ile 2:10 arasındaki suit değişimini doküman öngörüyor mu?"**
→ **HAYIR.** §0.12 ve CHARACTER BIBLE: iki suit de 14/14 sahnede aynıdır;
pas-kırmızısı bant = pilot (sol), çivit-mavisi bant = mühendis (sağ), sırt
DÜZ, durum değişimi yok. S12 → S13 arasında hiçbir kostüm değişikliği yoktur.
**🧍 raporun kostüm bulgusu AYAKTA** — gerçek üretim hatası, S13 yeniden
üretilir (çapa: S12'nin son karesi).

**S3. "Dış uzay SPEC'te vakum olarak tanımlı mı — dış SFX toptan ihlal mi?"**
→ **VAKUM, evet** (§0.12 SES: "Dışarıda ses SIFIRDIR"). Ama **toptan değil**:
gövdeden iletilen ve telsiz kanalından gelen ses meşrudur — S8'in kol TOK'u ve
S11'in temas TOK'u **planlı seslerdir** (§0.19 müzik notu: S11'de darbe durur,
yalnız gövde rezonansı kalır). Yani 1:56 büyük olasılıkla doğru sestir;
1:04 ve 1:28 (itki ve fırlatma gürültüsü, kamera dışarıda) ihlal adayıdır.
→ Kilit çelişkisi defteri madde 4.

**S4. "2:20'deki 'THE RING LIGHT' yazısı planlı bir post eklentisi mi?"**
→ **HAYIR — YASAK.** §0.12: `METİN 0 kare`. §5.3: tipografi **yalnız kapak
görselinde** kullanılır, "kapak çıktısı film kurgusuna ASLA eklenmez [Ders 72]".
🔴 **BLOCKER, kurguda 4 saniyede düzelir, yeniden üretim gerektirmez.**

**S5. "Konuşulan replikler senaryoyla birebir mi?"**
→ **HAYIR.** Plan 7 replik, hepsi Türkçe, hepsi gövdesiz AI (§0.11). Raporlarda
en az üç yabancı replik ve S11'in "Sıfır."ının yokluğu bildirildi.
→ Kilit çelişkisi defteri madde 1 ve Ana Bulgu 4.

### 📖 SENARYO_QA

**S1. "Film bilinçli olarak bir pilot/fragman mı? Final 'duruyor' gibi okundu."**
→ **HAYIR, bağımsız kısa filmdir.** §0.8: `YAPI = TEMA — S0 ↔ S13 çifti`; film
eşiğe varmadan, held frame ile biter ve bu **D69 ① gereği bilinçlidir** (biniş
hareketi 0 kare). §0.15 rubrik uyarısı bunu ayrıca yazıyor: "S13 held frame ile
biter — 'final tamamlanmamış' okuması düşer".
⚠️ **AMA:** raporun "duruyor" okumasının sebebi büyük ölçüde **jenerik kartı** —
film bir cliffhanger repliğinden karta kesiyor. Kart çıkarılınca bu okuma da
sınanabilir hale gelir. Final 4/10 puanı bu haliyle **filmin değil, kurgunun
puanıdır.**

**S2. "0:20-0:40 (raporun S3-S4'ü) viral ara sahne mi? Kesme listeme aldım."**
→ **EVET, 0:20-0:30 planın S2'sidir ve KESİLEMEZ** (§0.8: `VİRAL ARA S2 ve S9 —
bunlar KESİLEMEZ`). 0:30-0:40 ise S3'tür: filmin hareket devrini yapan sahne
(hareket gemiden yıldız alanına geçer) — "no new information" okuması yanlıştır,
sahnenin olayı tam olarak budur.
🔴 **KESME LİSTESİ UYGULANMAZ.** Raporun ilk iki sırası filmin iki viral
klibinden birini ve devir sahnesini siliyor; üstelik raporun kendi aritmetiği
119 s veriyor = **format tabanının altı** (2-4 dk = 120 s).

### 🧍 KARAKTER_QA

**S1. "Senaryo yanaşmadan sonra vizörlerin açılmasını öngörüyor mu?"**
→ **HAYIR — TERSİ.** §0.12 KASK TAKVİMİ: `S0-S13 kask TAKILI, vizör KAPALI ve
MÜHÜRLÜ. Durum değişimi 0. Kask hiçbir karede çıkmaz, vizör hiçbir karede
açılmaz.` Vizör "tek parça, optik berrak, RENKSİZ, kaplamasız, **yansımasız**"
tarif edilmiştir — yani yüz vizörün ARDINDAN tam okunur.
⭐ **Bu, raporun hatası olmayabilir: kilit, kendi kanıtını sildi.** Yansımasız,
renksiz, çerçevesi tarif edilmemiş bir vizör ekranda "vizör yok"tan ayırt
edilemez. Rapor da tam bunu sordu. → **DERS 95** (mühürlü durumun üç görünür
işareti sayısal olarak yazılır).

**S2. "0:10-1:50 arasındaki replikleri kim söylüyor?"**
→ **Hiçbir insan.** §0.11: 7 repliğin 7'si kabin hoparlöründen gelen **gövdesiz
sentetik sestir**; iki insan da filmde hiç konuşmaz, insanlı 6 sahnenin 4'ü
arkadan çekilir, yüzlerin göründüğü 2 sahnede (S12·S13) replik yoktur.
Bu, D82'nin **yapısal panzehiridir** — dudak senkron riski tasarım gereği 0'dır.
⚠️ Bu yüzden 🧍 raporun **Ses 9/10** puanı ("single on-screen spoken line
matches the physical body perfectly") planda var olmayan bir olaya verilmiştir:
sütun **N/A olmalıydı**. → **DERS 97**

---

## 📋 ONARIM LİSTESİ

### Kurguda düzelir (yeniden üretim YOK)

```
1. 🔴 2:20-2:24 jenerik kartını kurgudan ÇIKAR → süre 140 s, klip 14 olur,
      metin 0 kare olur, filme özel rubrik MOD F koşabilir hale gelir.
2. ⬜ 1:04 ve 1:28 dış ses katmanlarını incele; hava sesiyse sustur
      (gövde/telsiz katmanı kalır) — kilit çelişkisi defteri madde 4.
3. ⬜ Ses master'ı: S11'in "Sıfır." repliği yerinde mi; planlı olmayan
      İngilizce replikler kurguda mı yoksa üretimde mi bindi.
```

### Yeniden üretim gerektirir

```
4. 🟠 S13 (2:10-2:20) — suit tasarımı S12'den sapıyor (omuz/göğüs plakaları).
      Çapa: S12'nin son karesi. 🧍 raporun tek ayakta kalan bulgusu.
5. ⬜ (defter kapandıktan sonra) S11 kıvılcım/şarapnel doğrulanırsa: ATEŞ 0
      kare kilidi ihlali, sahne yeniden üretilir.
6. ⬜ (defter kapandıktan sonra) vizör/kask ve insan repliği doğrulanırsa:
      S12-S13 yeniden üretilir, D95 cümleleriyle.
```

### Ölçüm borcu

```
7. ⭐ Kart çıkarıldıktan sonra FİLME ÖZEL RUBRİK **MOD F** yeniden koşulur.
      Bu filmin gerçek QA'sı odur; yukarıdaki üç skor onun yerine geçmez.
8. ⭐ Üç genel mercek MOD D ile tekrarlanır (§0.15 SPEC bloğu yapıştırılarak).
      Mod D bu depoda hâlâ hiç denenmedi — operatör kuralı ② 4. ihlal.
```

---

## 📚 BU FİLMDEN ÇIKAN DERSLER

| № | Başlık | Kaynak |
|:--:|---|---|
| **93** | Filme özel rubrik 4 saniyelik jenerik kartıyla susturuldu | FİLME ÖZEL koşu |
| **94** | SPEC hazırken koşulan mod V, kilit ihlalini cila notuna indiriyor | 🔧 + 📖 |
| **95** | "Optik berrak, yansımasız vizör" ekranda "kask yok" okunuyor | 🧍 |
| **96** | Mod V bulgusu kilide aykırıysa "film mi saptı, rapor mı uydurdu" rapordan çözülemez | üç mercek |
| **97** | Karakter pasaportu filmin %14'ünden kuruldu, skor tamamına yazıldı | 🧍 |
| **98** | Negatif ihlal kutusu işaretlendi, bulguya dönmedi | 🔧 |
| **99** | Prompt nesri sese sızıyor — "Shadow entry and exit" tarif cümlesiydi, replik olarak duyuldu | 📖 replik listesi + `grep` |
