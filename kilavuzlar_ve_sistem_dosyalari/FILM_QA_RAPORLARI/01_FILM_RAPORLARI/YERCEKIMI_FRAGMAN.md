# 🌍 YERÇEKİMİ — YATAY FRAGMAN · QA KAYDI

> **Malzeme:** FRAGMAN (film değil; film sayımına ve T1-T4'e girmez [D111])
> **Koşu:** 04.09.2026 · operatör YEDİ rapor yapıştırdı.
> **⛔ YEDİDEN BEŞİ BU FRAGMANIN RAPORU DEĞİL.**
>
> ⛔ **HİÇBİR SKOR SATIRI TABLOYA GİRMEDİ** — ve sebebi alışılmış olan değil.
> ⑧ FRAGMAN MERCEK KAPISI [D111]: fragmanın merceği **① KARE**'dir.
> Bu partide ①'in yerinde başka bir filmin raporu duruyor → **fragmanın
> ZORUNLU merceği HİÇ KOŞULMADI.** Koşan iki mercek (⑤ ⑥) derin taramadır
> ve zaten matrise girmez.

---

## §⑦ PARMAK İZİ / ③ KİMLİK KAPISI — 🚨 **PARTİ KONTAMİNE**

| yapıştırılan rapor | künyesinde ne yazıyor | gerçekte hangi film |
|---|---|---|
| ① KARE | `duration 226s` · 22 sahne · 21 kesme · "Alien Forest" · knife · vine | 🚨 **THE UPWARD FALL** |
| ② DEVAMLILIK | `RUNTIME 03:46` · 22 sahne · "The Explorer" · Alien Forest | 🚨 **THE UPWARD FALL** |
| ③ SES | `RUNTIME 03:46` · 21 kesme | 🚨 **THE UPWARD FALL** |
| ⑦ AKSİYON | `FILM: the upward fall.mp4` · 03:46 · 22 sahne | 🚨 **THE UPWARD FALL** |
| ⑧ EFOR | `FILM: the upward fall.mp4` · 03:46 · 22 sahne | 🚨 **THE UPWARD FALL** |
| ⑤ ARKA PLAN | `gravity.mp4` · 02:25 · 14 sahne · 13 kesme | ✅ **BU FRAGMAN** |
| ⑥ FİZİK | `gravıty ıt holds one fragman.mp4` · 02:25 · 14 sahne | ✅ **BU FRAGMAN** |

```
③ KİMLİK KAPISI [D105] — iki metin-olmayan çapa arandı:
  ✅ ⑤: "Space Shuttle mid-distance" (S5) ↔ plan SAHNE 5 kaynağı
  ✅ ⑤/⑥: 14 sahne ↔ planın 14 vuruşu · 145 s ölçüm ↔ raporun 2:25'i
  🚨 ①②③⑦⑧: SIFIR çapa — beşi de orman, sarmaşık, bıçak ve 22 sahne anlatıyor
     → beşi de UNATTRIBUTED: skor satırı yazılmaz, bulgudan ders yazılmaz.
     Beşi ZATEN doğru filmin altında dosyalı (`THE_UPWARD_FALL_*_HAM.md`);
     bu klasörde ikinci kopya AÇILMADI.
```

⛔ **VE BETİK BU PARTİYİ AYAKTA TUTTU.** Yedisi birlikte `rapor_kontrol.py`'ye
verildiğinde çıktı şu:

```
⑪ ÖLÇÜM HAKEM: kesme = 13 (ölçüldü) · raporlar: ⑤ 13 · ⑥ 13 · ① 21 · ② 21 · ③ 21 · ⑧ 21 · ⑦ 21
⚠️ ⑤ ölçümden sapan mercek(ler): ① 21 · ② 21 · ③ 21 · ⑧ 21 · ⑦ 21
     parti AYAKTA — anlaşmazlık ölçümle çözüldü; yalnız sapan mercek şartlıdır
TOPLAM 7 rapor · 🚨 1 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 6 ŞARTLI · ✅ 0 GO
```

**"Sapan mercek" değil, BAŞKA FİLM.** 21↔13 ve 22↔14 bir sayım hatası değil,
bir kimlik hatasıdır; kapı ikisini ayırt etmiyor. → **[[D178]]**

---

## §⑪ ÖLÇÜM KAPISI — `olcum_kapisi.sh` · 04.09.2026 · **KOŞULDU**

```
MASTER:  /Users/dai/Downloads/gravıty ıt holds one fragman (1).mp4
         145,00 s · 3840x2160 · 30 fps · AAC stereo
İKİZ:    aynı adın 1080p kopyası — AYNI SÜRE (145,00 s), aynı kurgu [D160]
KİMLİK:  kurgunun ortasından kare (72 s) → beyaz/turuncu şeritli basınç
         giysisi, yörünge, enkaz · SPEC C bloğuna OTURUYOR ✅ (koşu devam)
```

| ölçüm | değer | plan (`YERCEKIMI_FRAGMAN_YATAY.md`) | sonuç |
|---|---|---|---|
| süre | **145,00 s** | 120,000 s (2:00) | ⛔ **+25 s** |
| gövde | **140 s** = 14 × 10,0 s | 100,000 s (14 vuruş, kırpma sonrası) | ⛔ **+40 s** |
| klip | **10,0 s** | **8,0 s NATIVE** (sapma ②, D124 açık kapısı) | ⛔ klip 2 s uzun |
| kırpma | **0 s uygulanmış** | §7 KIRPMA TABLOSU vuruş vuruş (−12 s) | ⛔ tablo hiç işlemedi |
| BLOK A | **YOK** — 5 s'de zaten SAHNE 1 | APEXAIC logo girişi 0:00-0:10 | 🔴 **BLOK EKSİK** |
| BLOK Z | **başlık kartı** 140,3-145,0 s (~4,7 s) | APEXAIC logo kapanışı 1:50-2:00 (10 s) | 🔴 **YANLIŞ BLOK** |
| ekran metni (gövde) | **0,0 s** ✅ | 0,0 s [sapma ③] | ✅ TUTTU |
| ses kanalı | **VAR** · sessizlik aralığı YOK | replik 2 (post) + nefes/cızırtı | ✅ kanal var |
| loudness | **I = −16,0 LUFS · Peak −0,3 dBFS** | −14 LUFS / −1,0 dBTP | ⚠️ 2,0 LU sessiz, tepe 0,7 dB yüksek |
| **filigran** | **YOK** ✅ (dört köşe, 6 örnek) | — | ✅ **TEMİZ** |
| kesme dedektörü | scene>0,3 → **0 kesme** (karanlık film körlüğü) | — | ızgara plandan okundu |

```
⛔ KUYRUKTAKİ KART: "GRAVITY / IT HOLDS ONE" — kapak görseli üstünde
   yanan başlık + tagline. Plan sapma ③ birebir şunu diyor:
   "Gövdede ekran metni 0,0 s — BAŞLIK KARTI YOK, altyazı yok [D70/72].
    Marka grafiği YALNIZ Blok A ve Blok Z'de yaşar."
   Teslimde Blok A hiç yok, Blok Z'nin yerinde APEXAIC logosu değil bir
   BAŞLIK KARTI var. → 🔴 D70/D72'nin 11. vakası, bu kez FRAGMANDA.
```

---

## §④ KURGU KAPISI — **ÖN KOŞU** · vuruş sayısı tuttu, ızgara tutmadı

```
a) klip sayısı  14 = 14  ✅
b) süre         140 s (kartsız) ≠ 100 s · Δ = +40 s  ⛔
c) sıra         şerit `-1111111111111` (14) ↔ plan KART 10 "SAHNE 1 insansız"
                → ⭐ ŞERİT TUTTU ve bu filmde ÖLÇÜYOR: tek-figürlü filmlerin
                  aksine burada baştaki `-` gerçek bir ayraç [D163'ün istisnası]
```

**Δ okuması:** 14 × 10,0 = 140. Planın 8,0 s'lik NATIVE ızgarası yerine 10 s
üretilmiş, ve §7 kırpma tablosu hiç uygulanmamış. Sapma ②'nin kendi açık
kapısı bunu öngörmüştü ve KOŞULMAMIŞ:

> *"⛔ D124 açık kapısı filmle ortak: ilk test klibi ffprobe ile ölçülür,
> 8,0 ± 0,2 dışıysa bu dosyanın kırpma tablosu ölçülen süreden yeniden
> hesaplanır."*

Ölçüm 10,0 s verdi; tablo yeniden hesaplanmadı, kurgu ham kliplerle yapıldı.

---

## §② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 6 madde · 4'ü KAREYLE KAPANDI

| # | ne ölçüldü | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | **81 s: 2 figür · 84 s: 3 FİGÜR · 88 s: 2 figür** — üçüncü gövde klip İÇİNDE doğuyor ve sönüyor | plan KART 4: "yalnız SAHNE 3 ve 9'da **kadro 2**" · filmde insan **2** | `s9_81/84/88.jpg` | 🔴 **FİLM SAPTI — KLİP İÇİ DUPLİKE** |
| 2 | BLOK A (APEXAIC girişi) yok | master zaman çizelgesi | 5 s karesi = SAHNE 1 | 🔴 **FİLM SAPTI** |
| 3 | kuyrukta başlık kartı | sapma ③ "başlık kartı yok" | `son_kare.jpg` | 🔴 **FİLM SAPTI** |
| 4 | klip 10,0 s | sapma ② "8,0 s NATIVE" | ffprobe + ızgara | 🔴 **FİLM SAPTI** |
| 5 | kask: geniş kavisli tek cam, beyaz kabuk — "dome/bubble" okumasına yakın | sapma ④ çapası: "clear front glass in a **bright metal rim**" · ⛔ dome/bubble yazılmaz [D146] | ⬜ 33 s ve 66 s kareleri çıkarıldı; parlak metal çerçeve OKUNMUYOR ama kabuk da kesintisiz değil | ⬜ **AÇIK** — ① KARE koşulmadan kapanmaz |
| 6 | replik duyulmadı (⑥: "nothing audible to me") · ses yatağı VAR, −16,0 LUFS, sessizlik aralığı 0 | sapma ⑤: 2 replik, post katmanı, 0:29 ve 0:43 | ⬜ ses katmanı bu kesimde eklendi mi? | ⬜ **AÇIK** — post durumu bilinmiyor |

⛔ **5 ve 6 AÇIK olduğu için o iki eksenden ders yazılmadı.**

---

## §⑩ ÖNERME KAPISI — düşen bulgular

| bulgu | getiren | planda kaynağı | karar |
|---|---|---|---|
| ⑥ `VERDICT: TWO GRAVITIES` · Gravity & Free Fall **3/10** | ⑥ | Filmin ortamı YÖRÜNGEDİR; ⑥'nın PREMISE REGISTER'ı `none` yazıyor ve mikro-yerçekimini bir "gravity" değeri gibi ölçüyor | ⚠️ **KISMEN DÜŞER** — "iki yerçekimi" hükmü düşer (tek ortam var). AYAKTA kalan tek bulgu **L3: parçacıkların vakumda yavaşlayıp durması** — bu gerçek ve ölçülmüş [D166'nın 3. vakası: mod V, novum/ortam kuralı registera yazılmamış] |
| ⑤ "S1 hatch texture boils" 🟡 | ⑤ | plan SAHNE 1: tek çekim, kamera sabit, insansız | ✅ **AYAKTA** — ① KARE'nin işi ama ① koşmadı; ⑤ kendi kapsamında haklı olarak yalnız 🟡 verdi |
| ⑤ "debris passes through the arm" 🟠 | ⑤ | — | ✅ **AYAKTA** · sahibi ① KARE → koşulmadı |
| ⑥ `SCORED CATEGORIES: 3` (9 kategoriden 6'sı ⚠️ PARTIAL) | ⑥ | fragman 145 s'dir; ⑥'nın kanıt tabanı yapısal olarak dar | ⚠️ **ÖLÇÜM DEĞİL** — 3 hücreli ortalama fragman için bilgi taşımaz; T6'ya satır YAZILMAZ |

**⑩ sonrası:**

| mercek | raporun toplamı | ⑩ sonrası | T tablosu |
|---|---|---|---|
| ⑤ ARKA PLAN | 9,1 | **9,1** | — (fragman satırı film tablosuna girmez [D111]) |
| ⑥ FİZİK | 4,6 | **—** (TWO GRAVITIES düştü · 3 hücre) | — |
| ① ② ③ ⑦ ⑧ | — | — | 🚨 UNATTRIBUTED |

---

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FRAGMAN: 14 vuruşun 14'ü teslim edildi (⭐ nadir), şerit plana birebir
   uydu, filigran YOK, gövdede ekran metni YOK. Ama ızgara 8 s yerine 10 s
   üretildi, kırpma tablosu hiç işlemedi, APEXAIC giriş bloğu yok ve
   kuyrukta yasaklı bir başlık kartı var. En ağırı: 84 s'de ÜÇÜNCÜ
   ASTRONOT — iki insanlı bir dünyada, tek klibin içinde.
2. QA: fragmanın ZORUNLU merceği (① KARE) hiç koşulmadı; yerinde başka bir
   filmin raporu duruyordu. 🔴 duplike bulguyu ⑤ kendi "SUBJECTS EXCLUDED"
   satırına "Three tethered astronauts" diye YAZDI — ve kapsamı gereği
   puanlayamadı. Kusur, kontaminasyonun açtığı boşluktan çıktı.
3. SİSTEM: bu partiden bir ders çıktı — **D178**: ölçüm hakemliği, YANLIŞ
   FİLMİN raporunu "sapan mercek" diye kurtarıyor.
```

---

## 📎 KANIT DOSYALARI (oturum scratchpad'i)

```
frag_grid.jpg        14 sahnenin ortası + kart, ızgara sırasıyla
s9_81/84/88.jpg      2 → 3 → 2 figür · klip içi duplike
yuzler.jpg           33/66/104/137 s — kimlik tek kişi okuyor (② koşmadı)
ikili_24.jpg         SAHNE 3: kadro 2 ✅ (plan KART 4)
kose_SA/SU/SoA/SoU   filigran YOK
son_kare.jpg         "GRAVITY / IT HOLDS ONE" başlık kartı
```
