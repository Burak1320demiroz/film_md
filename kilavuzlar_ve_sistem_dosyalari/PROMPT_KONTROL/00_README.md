# 🔎 PROMPT KONTROL — üretimden ÖNCE

> Bu klasör **girdiyi** denetler. Üretilmiş işin eleştirisi ayrı klasördedir:
> `../QA_PROMPTLARI/`. Aradaki fark maliyet: buradaki denetim **sıfır kare**
> harcar, oradaki denetim üretim bittikten sonra çalışır.

---

## 📦 İÇİNDEKİLER

| Dosya | Ne yapar | Kim koşar |
|---|---|---|
| `prompt_kontrol.py` | **sayar** — uzunluk, yasak kelime, negatif çekirdek imzası, sahne tutarlılığı | betik, yerel |
| `PROMPT_QA_CRITIQUE_PROMPT.md` | **yargılar** — kilit sayı mı tarif mi, hangi ders tetiklendi | rubrik, model |
| `RAPORLAR/` | betiğin `--rapor` çıktısı | — |

```
KULLANIM SIRASI — ikisi aynı şeyi ölçmez, ikisi de gerekir

  1. python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <film dosyası>
     → BLOCK ise: düzelt, tekrar koş. Buradan geçmeden 2'ye geçme.
  2. PROMPT_QA_CRITIQUE_PROMPT.md rubriğini modele ver
     → GO ise üretime geç.
```

Çıkış kodu: `0` = GO · `1` = FIX · `2` = BLOCK — betikten zincirlenebilir.

---

## 🧭 AKIŞTAKİ YERİ

`KILAVUZ_REHBERI.md` §6 adım **3.5**:

```
3.  PROMPT      image + video, self-contained
3.5 PROMPT QA   ← BURASI · maliyeti sıfır
4./5. ÜRETİM    önce imaj, onaylanınca video
```

---

## ⛔ NEDEN BİRİ BETİK, DİĞERİ RUBRİK

`../QA_PROMPTLARI/` rubrikleri **dış modelde, depoyu göremeden** koşar
(05.08.2026 kararı: *"göremediğin depoda dosya var deme"*). Bu denetimin
girdisi ise zaten depodaki `.md` dosyasıdır. Karakter saymak, yasak kelime
aramak ve `Scene N of X` karşılaştırmak modele sorulacak işler değil —
`sayac.sh` mantığı: **sayıyı elle tutan, yanlış tutar.**

Geriye modele sorulacak tek soru kalıyor ve rubrik yalnız onu soruyor:
*bu kilit gerçekten kilitliyor mu?*

---

## 📊 İLK KOŞU — 12.08.2026 · 69 film dosyası

Betik yazıldığı gün tüm depoya koşuldu. Amaç film düzeltmek değil,
**denetçiyi denetlemekti** — bilinen hataları bulabiliyor mu?

```
⛔ 3 BLOCK · ⚠️ 66 FIX · ✅ 0 GO
```

**Bilinen hataları buldu (doğrulama):**

```
✅ LOW_POWER_PART_B — eşik üstü 5 prompt
   §7 zaten yazıyordu: "~4.300 karakter → Veo hata veriyor (Low Power S5,
   S11 doğrulandı)". Betik aynı dosyada aynı sınıfı bağımsız buldu.

✅ THE_KALEIDA_CRASH — "Scene N of 13" ama dosyada 12 sahne başlığı
   03_PLAN_ONCESI_KONTROL_LISTESI A2'nin belgelenmiş vakası, birebir.
```

**Belgelenmemiş hatalar da buldu:**

```
🆕 Aynı sahne-sayısı hatası DÖRT filmde daha:
   THE_BURNING_WORLD · THE_FORGOTTEN_ARCHITECTS · THE_LAST_BLOOM ·
   THE_SILENT_EVENT_HORIZON — hepsi "Scene N of 10", hepsinde 13 sahne.
🆕 THE_DEAD_APPROACH — eşik üstü 9 prompt (depodaki en yüksek)
```

### ⚠️ İLK KOŞUNUN AÇTIĞI KARAR — image bandı

`§7`'nin image bandı (1.700-2.100) depodaki **hiçbir filmle uyuşmuyor**:

```
THE HOLDING FIELD    3.417 - 4.017
THE THIRD DUNE       2.732 - 4.154
THE QUIET IMPACT     4.577 - 5.644
```

Üçü de bandın en az bir katı üstünde. İki ihtimal var: ya bant bayat, ya
image promptu için hiç ölçülmedi (§7'nin cümlesi *"~4.300 karakter → **Veo**
hata veriyor"* — Veo video üretir). Karar verilene kadar betik image
uzunluğunu **gözlem** olarak yazar, üretim durdurmaz. Video tarafında ise
eşik ölçülmüştür ve BLOCK üretir.

⛔ Bu bant bir sayıdır ve sayının tek sahibi vardır. Karar verilince
`prompt_kontrol.py` başındaki `BANT` sözlüğü güncellenir — belgeye elle
yazılmaz.

### 🟡 İlk koşunun ikinci bulgusu — eski filmler

66 FIX'in büyük kısmı V1 dönemi filmlerden geliyor (negatif çekirdek imzası
eksik: 1.160 satır). Bu bir borç envanteri, acil iş listesi değil. **Betik
YENİ promptlar için kapıdır**; eski filmler ancak yeniden üretime girerken
buradan geçer.

---

## 🔧 BETİĞİ GÜNCELLERKEN

```
□ Yeni yasak kelime çıktı        → YASAK sözlüğü (ders numarasıyla)
□ Yeni sayısal eşik ölçüldü      → BANT / TAVAN
□ Yeni kilit çekirdeğe girdi     → KILITLER (kapsamıyla: image/video/ikisi)
□ Yeni yanlış pozitif sınıfı     → önce testi yaz: hangi film, hangi satır
```

⛔ **Yanlış pozitif, bulgu bulamamaktan pahalıdır.** Bu betiğin ilk sürümü
beş yanlış pozitif sınıfı üretti ve hepsi çalışan tasarımı bozmaya
yönlendiriyordu:

```
① satır sarması       "No\nreadable text" desenden kaçtı → 4 sahne haksız damga
② kesme işareti       "the lander's" tırnak sanıldı → replik dışarıda kaldı
③ tek çekim kilidi    durağan karede aranırsa her IMAGE promptu bayrak yer
④ Veo eşiği           video eşiği image promptuna uygulandı
⑤ BÜYÜK HARF vurgu    "showing ABSTRACT LIGHT" A1 ihlali sanıldı —
                      oysa o A1'in ÇÖZÜMÜ (D50)
```

Beşi de `prompt_kontrol.py` içinde gerekçesiyle yorumlanmıştır. Silme.
