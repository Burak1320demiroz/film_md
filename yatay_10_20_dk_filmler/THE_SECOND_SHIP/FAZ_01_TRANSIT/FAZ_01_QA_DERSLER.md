# 📚 FAZ 1 / TRANSİT — QA DERSLERİ VE AKSİYON RAPORU

> Koşu: 07.08.2026 · Model: Gemini · Girdi: 10 sahnelik derleme reel (100 s)
> Rubrik: `FAZ_01_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ01_HAM.md`
>
> **Raporun skoru 5.4/10 — ama bu sayı OLDUĞU GİBİ OKUNMAZ.** Yedi RED'in
> dördü tek bir kurgu hatasına, biri rubriğin kendi hatasına iniyor.
> Gerçek üretim kusuru üç sahnede: S9, S10, S3.

---

## 1. BULGULARIN KÖK NEDEN AYRIŞTIRMASI

| # | Bulgu | Sahne | Sınıf | Aksiyon |
|---|-------|-------|-------|---------|
| 1 | İçerik rotasyonu (4×RED) | S4→S7 | 🎬 **KURGU** | yeniden dizilim — render YOK |
| 2 | Kasksız baş (RED) | S9 | 🤖 **ÜRETİM** | yeniden üretim |
| 3 | Shockwave + bloom (RED) | S10 | 🤖 **ÜRETİM** | yeniden üretim |
| 4 | Yara izi sağ kaşta (YELLOW) | S3 | 🤖 **ÜRETİM** | karar bekliyor (§2.3) |
| 5 | Çiftler özdeş değil (YELLOW) | S2 | 🤖 **ÜRETİM** | kabul edilebilir |
| 6 | "Dev ay ölçek veriyor" (RED) | S1 | 📋 **RUBRİK** | rubrik yamalandı (§3.1) |

---

## 2. ÜRETİM BULGULARI — tek tek

### 2.1 🔴 S4–S7 İÇERİK ROTASYONU — en büyük bulgu, en ucuz düzeltme

Raporun deseni net bir rotasyon:

```
pozisyon 4 (0:30) → S7 içeriği (konsoldaki adam)
pozisyon 5 (0:40) → S4 içeriği (koridor)
pozisyon 6 (0:50) → S5 içeriği (iki kişilik kokpit)
pozisyon 7 (1:00) → S6 içeriği (amber şerit makrosu)
```

Yani **S7 klibi 4. sıraya konmuş, S4-S5-S6 birer kaymış.** Dört içerik de
mevcut ve model hepsini "verified" diye tarif ediyor — klipler doğru
üretilmiş, yerleri yanlış. Bu bir NLE dizilim hatası; dört sahnenin
yeniden render'ı GEREKMEZ.

⚠️ Ders 65 uyarısı (denetçi yanılabilir): dizilimi düzeltmeden önce klip
dosya adlarını timeline sırasıyla YAN YANA doğrula. Rotasyon Gemini'nin
okuma hatası da olabilir — 30 saniyelik bir kontrol, dört sahnelik bir
"düzeltmeyi" yanlış yere yapmaktan ucuz.

Zincir etkisi: PHASE CHAIN 3/10 ve skorun çöküşü büyük oranda bu tek
hatadan. Dizilim düzeltilince rapor yeniden koşulmadan skora bakılmaz.

### 2.2 🔴 S9 KASKSIZ BAŞ — Ders 79'un dördüncü vakası

Prompt kaskı açıkça içeriyordu (`integrated helmet with a fully
transparent seamless visor` — hem imaj hem video promptunda). Model yine
de düşürdü. Bu, "bible'daki kilit tutmuyor" dersinin (79) bir adım ötesi:
**prompt gövdesindeki kilit de tek cümleyle tutmayabiliyor.**

Yeniden üretim şart (kurgu kurtaramaz — KİLİT 1 anlatıyı taşıyor: S14'te
hayatta kalmalarını mühür açıklıyor).

Yeniden üretimde prompta eklenecek çift kilit (S9 için):
```
Her helmet is ON for every frame from first to last. The scene contains
no bare head, no removed helmet, no helmet resting on the console — the
integrated helmet with its fully transparent seamless visor stays sealed
on her head for all ten seconds.
```
⚠️ `FAZ_01_TRANSIT.md` bu raporla DEĞİŞTİRİLMEDİ (üretilmiş fazın
dosyası üretimle eşleşik kalıyor). Yukarıdaki blok, S9 yeniden üretilirken
prompta elle eklenir; tutan sürüm sonra dosyaya işlenir.

### 2.3 🟡 S3 YARA İZİ SAĞ KAŞTA — flip önerisini KÖRÜ KÖRÜNE UYGULAMA

Gemini'nin önerisi "yatay flip". Riskli:

```
Flip neyi düzeltir:  yara izi sağ → sol ✓
Flip neyi bozar:     bakış yönü (frame right → left) — S3'ün beat'i
                     "eyes off to frame RIGHT on a display"
                     push-in geometrisi ve konsol tarafı ayna olur
                     S8/S9'daki kokpit yön sürekliliğiyle çelişebilir
```

Karar için önce şu soruya cevap gerek (raporun kendi FLAG'i): **yara izi
tüm sahnelerde mi sağda, yalnız S3'te mi?** Model pasaport bölümünde
genel olarak "scar on RIGHT eyebrow" yazdı — S5/S8/S9'daki hâlini tek tek
raporlamadı.
- Her yerde sağdaysa → üretim zinciri tutarlı, REFERANS_PAKETI plakası
  kontrol edilir; plaka da sağ gösteriyorsa hata plakada doğmuş demektir
  ve düzeltme kararı (plakayı mı, bible'ı mı esas al) proje sahibinindir.
- Yalnız S3'teyse → S3 yeniden üretilir; flip kullanılMAZ.

### 2.4 🔴 S10 SHOCKWAVE + BLOOM — yasak kelime yetmedi

Prompt `no bloom, no shockwave, no explosion` yasaklarını taşıyordu;
model yine de patlama çizdi. Ders 59 mantığı burada da geçerli: **yasak
cümle değil, kompozisyon tetikliyor** — "gece yüzeyinde büyüyen parlak
ışık" kompozisyonunun kendisi patlama çekicisi.

Yeniden üretimde yasağa POZİTİF hâl eklenir:
```
The light NEVER brightens — it only widens. Its brightness at 10s is
identical to its brightness at 0s. The edge stays a hard, clean circle
that grows like an iris opening, two percent of frame height per second,
with zero halo and zero atmospheric glow around it.
```
(Sayısal kilit: tarif değil sayı — AGENTS kart G ②.)

### 2.5 🟡 S2 ÇİFTLER — kabul edilebilir

"Strict identical symmetry" eksik. Sahnenin işlevi (çiftlerin FARK
EDİLMESİ ama vurgulanmaması) görüntüde çalışıyorsa yeniden üretim
gerekmez. Novum ilk ipucunu S32+ zaten yeniden kuruyor. Karar: kareye
bakıp "çift" okunuyor mu — okunuyorsa GREEN say, bırak.

---

## 3. RUBRİK BULGULARI — rubrik de denetlendi, iki açık çıktı

### 3.1 S1 "ay" bulgusu kısmen SAHTE POZİTİFTİ → rubrik yamalandı

S1 promptu ayı bilinçli içeriyor (sahnenin tek ışık kaynağı; dünya
bible'ında da var). Rubriğin S1 satırı ise "no light source" diyordu —
prompt ile rubrik çelişiyordu ve model rubriğe uydu. **Ders 63 uygulandı:
kaynak rubrik önce yamalandı** — S1 satırı artık ayın varlığını değil
yalnız BOYUTUNU denetliyor (eşik: ay diski kadraj genişliğinin ~1/10'u).

Kalan gerçek soru: ay gerçekten "giant" mı? Kareye bakılır —
eşiği aşıyorsa S1 yeniden üretilir ve promptaki çelişkili ifade
düzeltilir: `one large pale moon hangs high, small and cold` cümlesi
"large" ile "small"u aynı anda söylüyor; yeniden üretimde
`one pale moon hangs high and distant, its disk small` yazılır.

### 3.2 Tek-sahne modu yoktu → FAZ_02 rubriğine eklendi

Faz 2 koşusu `MATERIAL GATE FAILED - measured 0 s, 0 segments` döndü.
**Kapı doğru çalıştı** (Ders 75'in koruması: yetersiz malzeme
puanlanmadı) — eksik olan moddu: operatör sahneleri tek tek veriyor,
rubrik yalnız 100 saniyelik reel tanıyordu. `FAZ_02_QA_PROMPT.md`
07.08.2026'da iki moda ayrıldı: `AUDIT TARGET: FULL REEL` ya da
`AUDIT TARGET: S13` gibi. Faz 3–8 rubrikleri bu iki modla doğacak.

### 3.3 Çalışan taraflar (değiştirme)

Sınır kesmeleri raporlanmadı (Ders 61 koruması tuttu) · numaralandırma
kaymadı (Ders 66) · skor kendi tablosundan üretildi (Ders 62) · FLAGS
bölümü gerçekten en değerli iki soruyu üretti (dizilim + yara izinin
kaynağı).

---

## 4. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ Timeline'da klip adlarını sırayla doğrula (30 sn)
     → rotasyon gerçekse S7 klibini 7. sıraya, S4-S5-S6'yı yerine çek
2. □ S9'u §2.2'deki çift kilitle yeniden üret (kask)
3. □ S10'u §2.4'teki sayısal kilitle yeniden üret (iris açılması)
4. □ Yara izi taraması: S5·S8·S9 karelerinde iz hangi kaşta?
     → REFERANS_PAKETI plakasıyla karşılaştır, §2.3'e göre karar ver
5. □ S1 karesine bak: ay diski kadraj genişliğinin 1/10'unu aşıyor mu?
     → aşıyorsa S1'i düzeltilmiş ay cümlesiyle yeniden üret
6. □ Dizilim + yeniden üretimler bitince reel'i YENİDEN KOŞ
     → 5.4 skoru çöpe; geçerli skor ikinci koşunun skorudur
7. □ İkinci koşu raporu gelince: bu dosya güncellenir, Faz 2 sahne
     raporlarıyla birlikte Faz 3-8 güncellemesi yapılır
```

---

## 5. FAZ 3–8'E TAŞINACAK ÖN DERSLER

> Nihai liste Faz 2 sahne raporları gelince çıkar. İlk koşudan şimdiden
> taşınabilir dört ders:

```
① KURGU KAPISI (faz sürümü) — reel QA'ya gitmeden önce klip adı ↔
  timeline sırası kontrol listesi. Bu koşunun 7 RED'inin 4'ü buydu.
  → Faz 3-8 rubriklerinin Türkçe sarmalına "birleştirmeden önce" adımı
    olarak girer.

② KASK ÇİFT KİLİDİ — tek cümlelik kask kilidi üretimde delindi.
  İnsan yüzü olan her sahnenin yeniden üretiminde §2.2 bloğu kullanılır;
  Faz 3-8'de üretim sonrası ilk göz kontrolü: kask var mı?

③ IŞIK-BÜYÜMESİ SAHNELERİ — "büyüyen/parlayan ışık" kompozisyonu yasak
  kelimeye rağmen patlamaya kayıyor. Faz 3-8'de bu sınıftaki her sahne
  (girdap hızlanması, kule ışıkları, kalkış) sayısal büyüme kilidi +
  "never brightens, only widens" pozitif hâlini taşımalı.

④ FLIP KURTARMASI SINIRI — yatay flip tek insanlı sahnede bile bakış
  yönünü ve mekân geometrisini bozar; iki insanlıda (renkler yer
  değiştirir) tamamen imkânsız. Kurgu kurtarma listelerine "flip" ancak
  yön-nötr kadrajlarda yazılır.
```

---

> **Bu dosya ne zaman güncellenir:** ikinci koşu raporu geldiğinde (§4
> madde 6-7) ve yara izi taramasının sonucu belli olduğunda (§2.3).
