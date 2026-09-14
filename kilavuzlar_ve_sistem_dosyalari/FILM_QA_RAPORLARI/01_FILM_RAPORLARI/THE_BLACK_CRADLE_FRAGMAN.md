# 🌑 THE BLACK CRADLE — FRAGMAN · Film QA Kaydı

> Oluşturma: 17.08.2026 · tek mercek (SHORTS_QA), MOD V (belgesiz) koşuldu.
> Kaynak dosya: `yatay_4_dk_filmler/THE_BLACK_CRADLE/THE_BLACK_CRADLE_FRAGMAN.md`
> Ham rapor: `02_HAM_RAPORLAR/THE_BLACK_CRADLE/THE_BLACK_CRADLE_FRAGMAN_SHORTS_HAM.md`
> ⚠️ Bu kaydın ana çıktısı **skor değil, ATIF DENETİMİDİR** — aşağıya bak.

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 📱 SHORTS_QA | 🚨 Ⓥ mod V · **ATIF DOĞRULANMADI** | ~~6.5/10~~ · REGENERATE | `..._FRAGMAN_SHORTS_HAM.md` |
| 📖 SENARYO_QA | ❌ | — | — |
| 🎨 KAPAK_QA | ❌ | — | — |

```
KÜNYE (fragman dosyası)  6 vuruş (V0-V5) × 8 s = 48,0 s ± 0 · 0 kesme ·
                         0 replik · 6/6 lockoff · ekran metni 0,0 sn ·
                         mekanik TERS KURALLAR · imza: KIÇ ÖNDE yanaşma ·
                         temas/kenetleme fragmanda YOK (spoiler kapısı)
KURGU (ölçülen)          63 s · 7 segment · sahneler ~10 s · sonda 5 s'lik
                         başlık kartı ("THE BLACK CRADLE" + uydurma tagline
                         "SOME DOCKS ARE BUILT FOR NO RETURN") · S5'te
                         BURUN ÖNDE yanaşma · kokpitte HUD grafikleri
D94 NOTU                 ⛔ SPEC bloğu fragman dosyasında YAZILI (§QA SPEC
                         BLOĞU) — rubriğe yapıştırılmadı. Mod V ÖN KOŞUDUR:
                         tamlık matrisi hücresi ❌ kalır, kesme/REMOVE
                         reçeteleri UYGULANMAZ. D94'ün 7. vakası.
D74 NOTU                 ⛔ Fragman dosyası "kaynak film üretilip kurgu
                         kapısından geçmeden bu fragman ÜRETİME ALINMAZ"
                         diye yazıyor. Kaynak film 0/4 mercek, S0-S14
                         üretilmiş. Kapı yazılıydı, koşulmadı — D74'ün
                         2. vakası (ilki Wrong Shadow).
```

---

## 🚨 TEK CÜMLELİK HÜKÜM

**Bu rapor, THE BLACK CRADLE fragmanını ölçmüş olamaz — ve raporu fragmana
bağlayan tek kanıt, filmin kendi en ağır ihlalidir.** Rapor kuralına uyup
`FILM: (not supplied)` yazdı [D65 ✅]; dosyaya "THE BLACK CRADLE fragmanı" adını
veren şey, ekranda yanan başlık kartındaki yazıdır — rubriğin modele okumasını
yasakladığı tam o kare. Altı vuruşun eşlemesi tutmuyor (aşağıdaki tablo): üçü
sırası bozuk, ikisi hiç yok, iki çekim HİÇBİR belgede geçmiyor ve tagline depoda
hiçbir dosyada yok. Skor bu yüzden tabloya **skor olarak** girmez.
→ **DERS 105.**

---

## 🧭 EŞLEME TABLOSU — fragman vuruşları ↔ raporun sahneleri

| Fragman | Ne olacaktı | Raporda | Durum |
|:--:|---|---|---|
| V0 hook | ŞAFAK DUVARI · kameraya koşu · 2 insan · kara ova | S3 @ 00:30 "Surface Extraction" | ⚠️ var ama **4. sırada** (hook değil) |
| V1 | KALKIŞ · 4 karın jeti · gövde yatay · bacaklar 4,5 s'de | S4 @ 00:38 "VTOL Launch" | ⚠️ var, ~10 s |
| V2 | YILDIZSIZ YER · 120 m gemi KULE gibi, yıldız örten siluet | — | ❌ yok |
| V3 | DÖNÜŞ · 180° yaw, kıç öne | — | ❌ yok |
| V4 afiş | GERİ GERİ · kıç yukarı · **temas YOK** | S5 @ 00:48 "Station Docking" | 🚨 **BURUN ÖNDE** — imzanın tersi |
| V5 kapanış | GÖZLER · 75mm yüz · ağız kapalı · metin yok | S2 @ 00:20 "Cockpit Close-Up" | 🚨 **3. sırada** + HUD + dudak hareketi |
| — | — | S0 "Orbital Station" (00:00) | 🚨 hiçbir belgede yok |
| — | — | S1 "Planet Approach" (00:10) | 🚨 hiçbir belgede yok |
| — | ekran metni 0,0 sn | S6 başlık kartı (00:58) | 🔴 yasaklı |

```
KAYNAK FİLM DE EŞLEŞMİYOR: 26 sahnelik THE BLACK CRADLE yüzeyde BAŞLAR
(S1 KAROT); "gezegene iniş/yaklaşma" sahnesi filmde de yoktur. Filmin
tamamının önermesi KÖR + KIÇ ÖNDE yanaşmadır (S11 KARAR · S12 DÖNÜŞ ·
S21 TEMAS); raporun gördüğü burun önde kenetlenme iki belgeye birden aykırı.
TAGLINE: "SOME DOCKS ARE BUILT FOR NO RETURN" depoda HİÇBİR dosyada geçmiyor
(grep 17.08.2026) — paketleme metni bile bizim değil.
```

---

## 📓 KİLİT ÇELİŞKİSİ DEFTERİ [D96] — ⛔ 8 madde ⬜ AÇIK

> Kural: ⬜ AÇIK madde varken bu merceğin skoru ŞARTLI, **bulgudan ders
> yazılmaz**, yeniden üretim siparişi verilmez. Çözüm eylemi = master'ın
> o saniyesini izlemek (~10 sn iş). Aşağıdaki 8 bulgu bu yüzden bulgu
> listesinden ALINDI ve buraya taşındı.

| # | rapor ne dedi (timecode) | hangi kilit | çözüm eylemi | sonuç |
|:--:|---|---|---|---|
| 1 | "Station Docking" — burun önde hizalanma (00:48) | V4 NEGATIVE: `Never nose-first — the canopy end never faces the berth` + filmin imzası | 00:48-00:58 izle: kıç mı burun mu önde | ⬜ AÇIK |
| 2 | Kokpitte cyan HUD grafikleri (00:20) | Negatif çekirdek ×6: `no HUD, no text, no digits` | 00:20-00:29 izle | ⬜ AÇIK |
| 3 | Dudak açılması / mikro-morph (00:23) | V5: `Her lips stay closed and do not move` + Kural 9 (0 replik) | 00:23-00:25 izle | ⬜ AÇIK |
| 4 | Kayan/süzülen koşu adımı (00:30) | V0: `real sprint, real time, grounded, weighted` · 0.8g [D44] | 00:30-00:38 izle | ⬜ AÇIK |
| 5 | Partikül egzozunun aniden yok olması (00:41) | V1: `settles within 3 seconds`, balistik yay | 00:39-00:42 izle | ⬜ AÇIK |
| 6 | Rıhtım geometrisinin ölçek kayması (00:48) | Ana gemi çapa bloğu: 120 m · 15× lander [D32] | 00:48-00:56 izle | ⬜ AÇIK |
| 7 | Sahne süreleri ~10 s | Kural: her vuruş TAM 8 s · toplam 48,0 ± 0 | kurgu zaman çizelgesi | ⬜ AÇIK |
| 8 | S0 statik açılış, kamera "hafif drift" | 6/6 TAM LOCKOFF — drift de yasak | 00:00-00:02 izle | ⬜ AÇIK |

> ⛔ **Sekizinin de ön koşulu madde 0'dır: bu master fragman mı?** Eşleme
> tablosu tutmadığı için sekiz maddenin hiçbiri "film saptı" diye
> okunamaz — önce malzemenin kimliği çözülür, sonra defter işlenir.

---

## 🔎 FLAGS FOR DOCUMENT CHECK — CEVAPLAR (fragman + plan dosyasından)

**1. "Kurgu 63 s (6 sahne + 5 s kart); belge 48 s mi diyor?"**
BELGE 48,0 s ± 0 DİYOR ve kurgu kapısının 1. maddesi budur. Sahne süresi
tam 8 s'tir, ~10 s değil. Ayrıca kart: Kural 8 → **ekran metni 0,0 saniye,
başlık/jenerik kartı dahil**; aynı yasak 6 promptun 6'sının NEGATIVE'inde
(`no title card`) ve KURGU KAPISI'nda ayrı satır olarak yazılı.
→ D70/D34/D61 zincirinin dikey hattaki **3. vakası** (First Morning 64 s,
Wrong Shadow 64 s, bu 63 s). Üçünde de aynı imza: ~10 s sahne + sondaki kart.

**2. "Başlık kartı bilinçli sapma mı?"**
HAYIR. Ne fragman dosyasında ne FRAGMAN_KILAVUZU'nda kart var; başlık
platformda yaşar. Üstelik karttaki tagline ("SOME DOCKS ARE BUILT FOR NO
RETURN") depoda hiç geçmiyor — model/kurgu kendi paketlemesini uydurup
yakmış. Wrong Shadow'da kart YANLIŞ FİLM ADI taşıyordu, burada DOĞRU ad +
UYDURMA tagline taşıyor: kart, kimlik kanıtı olarak da güvenilmezdir.
🔴 BLOCKER doğru.

**3. "S3'teki sert çanta planlı bir prop mu, üretim artefaktı mı?"**
PLANLI. V0 promptu birebir: mühendis `carrying a slim matte-black sample
case`; V0 NEGATIVE'i de rolü sabitler (`teal leads empty-handed, amber
trails with the case`). Kaynak filmde de karot kutusu vardır (S1/S3/S23).
→ **BULGU DÜŞER** [D87 — değişen şey filmin önermesiyse bulgu düşer].
"hands-empty EVA standard" bu filmin kuralı değildir.

**4. "S3'te gerekçesiz ön anahtar ışık" (🟠 MAJOR)**
BULGU DÜŞER [D87]. V0 ışık bütçesi tam olarak bunu yazar: `fronts lit only
by their own four lamps blazing toward camera` — iki kask + iki göğüs
lambası, toplam 5 kaynak. Ön yüzlerin aydınlık olması gerekçesizlik değil,
YAZILI GEREKÇEDİR; şafak sadece rim verir. Mod V merceği ışık bütçesini
göremediği için tersini varsaydı.

**5. "S3 → S4 nedensellik kırılması: biniş sahnesi yok" (🟠 MAJOR)**
BULGU DÜŞER — ve düşme sebebi ayrı bir ders. Biniş/iniş hareketi bu depoda
**kadraja alınmaz**: D69 (klon sıcak noktası) bunu yasaklar, kaynak filmin
S5 BİNİŞ satırında da yazılıdır ("kapak hareketi kadraj DIŞI — D69 ①"), V0
promptu da bitişi kilitler (`Hold — no boarding, no hatch`). Yani rubrik,
başka bir dersin zorunlu kıldığı boşluğu nedensellik hatası olarak faturaladı.
→ **DERS 106.**

**6. "Novum: 'Black Cradle' istasyon mu, araç mı, yüzey mi?"**
Hiçbiri: **kızak/rıhtım** (docking cradle) — ana geminin omurga ortasındaki
açık kızak yuvası. Fragmanın mekaniği bir novum değil TERS KURALLAR
merdivenidir; altıncı basamak (VARMAK = BAKMAMAK) tek soruyu bırakır.
⚠️ Raporun tek cümlesi ("iki kişi kutuyu alıp istasyona kenetlenir") tam
tersini söylüyor: hikaye TAMAMLANMIŞ okunuyor. Fragmanın işi borç bırakmaktı.

---

## 📊 SKOR — TABLOYA NASIL GİRDİ

```
6.5/10 · REGENERATE · 15 kategori · aritmetik kapısı DOĞRU (97,0 ÷ 15 = 6,47) ✅
        [D62a kapısı tuttu — rapor kendi tablosundan skoru üretebildi]

⛔ Satır 05_SHORTS_KALITE_TABLOSU'na 🚨 ATIF DOĞRULANMADI olarak, skoru
   ÜSTÜ ÇİZİLİ girer. Sebep skorun yanlış olması değil: ölçülen NESNENİN
   KİMLİĞİ doğrulanmamıştır. Operatör master'ın fragman kurgusu olduğunu
   doğrularsa satır ⚠️ ŞARTLI Ⓥ'ye döner (D94 ön koşusu olarak kalır).

RAPORUN EKSİK BÖLÜMLERİ (rubrik OUTPUT FORMAT'a göre): SCENE INVENTORY
(mod V'de zorunlu) · SEVERITY TALLY · PER-SCENE SPREAD · PROGRESSION LADDER
CHECK · LESSON MATCH · WHAT WORKED WELL · QUALITY TABLE ROW yazılmamış.
⭐ SCENE INVENTORY yazılsaydı eşleme çöküşü operatörün önüne raporun
   İÇİNDEN gelirdi — DERS 105'in çözümü bu bölümü kapıya bağlar.
```

---

## 🧭 SONRAKİ ADIMLAR (sırayla)

```
① MALZEME KİMLİĞİ [D105]: operatör master'ı açar ve tek soruya cevap verir —
   00:48'de araç KIÇI mı BURNU mu önde? Kıç önde ise malzeme fragmandır ve
   defterin 8 maddesi işlenir; burun önde ise malzeme fragman DEĞİLDİR,
   satır tablodan tamamen düşer ve koşu UNATTRIBUTED kaydedilir.
② Malzeme fragmansa: kurgu kapısı koşulmadan yeni mercek çalıştırılmaz —
   6 klip · 48,0 s ± 0 · metin 0,0 sn · spoiler kapısı 8 madde 0 kare.
③ Fragman ÜRETİME ALINMAZ [dosyanın kendi ön koşulu]: kaynak film üretilip
   kurgu kapısından geçmeden yeniden üretim siparişi yok — D74'ün 3. vakası
   olmasın.
④ SPEC bloğu dosyanın §QA SPEC BLOĞU bölümünde HAZIR: bir sonraki koşu
   MOD D'dir. Bu depoda mod D hâlâ hiç denenmedi.
```
