# 🌾 THE BENT GRASS — FİLM KAYDI

> **Durum:** film üretildi ve birleştirildi · **master ÖLÇÜLMEDİ** 🚨 · **parti GEÇERSİZ**
> **Koşu:** 09.09.2026 · **on bir mercek** (① ② ③ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫) — ④ HİKAYE koşmadı.
>
> 🚨 **PARTİ GEÇERSİZ — ①.9 TESLİM KAPISI [D188].** Plan 14 sahne, dokuz mercek
> 13 saydı. `rapor_kontrol.py`: **11 rapor · 11 GEÇERSİZ.**
> ⛔ **T1-T12 tablolarına HİÇBİR SATIR YAZILMADI.**
> ⛔ Kesme listesi · REMOVE reçetesi · yeniden üretim **UYGULANMAZ** —
> önce eksik sahne adıyla saptanır, soru ÜRETİM masasına geçer.

---

## 📦 MALZEME

```
MASTER:    VERİLMEDİ — depoda .mp4/.mov/.mkv yok
SPEC:      THE_BENT_GRASS_QA_SPEC.md ✅ VAR
PAKET:     QA_PROMPTLARI/FILME_OZEL/THE_BENT_GRASS/ ✅ VAR (12 paket)
PLAN:      14 sahne (BOLUM_1 S0-S6 · BOLUM_2 S7-S13) · 140,0 s · kart YOK
           SCREEN TEXT kilidi: 0,0 s · SETUP SEQUENCE: A B A A D E D E F F G G B A
           İNSAN ŞERİDİ: 11111-111111--   (14 hane)
RAPORLARDA: 13 sahne · 130 s gövde + 4-6 s başlık kartı
           İNSAN ŞERİDİ: 11111-111111-    (13 hane · planın şeridi EKSİ SON HANE)
```

---

## §⑪ ÖLÇÜM KAPISI

```
🚨 ÖLÇÜM YAPILAMADI — master yolu verilmedi, depoda video dosyası yok.
   olcum_kapisi.sh koşmadı. Kimlik kapısı (⑪.0) koşmadı.

⛔ Raporların süre / sahne / kesme sayıları HİÇBİR KAPIYA SOKULMADI [skill §1].
⛔ Filigran ekseni ÖLÇÜLMEDİ — 11 raporun 11'i 0 yazabilir, bu ölçüm değildir [D177].
⛔ Ses kanalı ÖLÇÜLMEDİ — aşağıdaki replik ayrışması hakemsiz kaldı.

HAKEM EKSİK. Gereken tek komut:
   bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"
   → sonra: rapor_kontrol.py --olcum-sahne <n> --olcum-kesme <n> --olcum-filigran VAR|YOK
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py`

Tam çıktı: `RAPOR_KONTROL/RAPORLAR/THE_BENT_GRASS_20260909_RAPOR_KONTROL.md`

```
TOPLAM 11 rapor · 🚨 11 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 0 ŞARTLI · ✅ 0 GO

tekil kararlar (parti düşmeden ÖNCE):
  ✅ GO       ③ SES · ⑧ EFOR
  ⚠️ ŞARTLI   ① KARE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑨ KADRAJ ·
              ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK
  🚨 GEÇERSİZ ② DEVAMLILIK (aritmetik fabrike)
```

---

## 🚨 TESLİM KAPISI — partiyi düşüren madde [D188 · 2. film]

```
PLAN                     MAKARA
14 sahne                 13 sahne
140,0 s                  130 s gövde + 4-6 s kart
başlık kartı: YOK        2:10'da başlık kartı VAR (yanmış metin)
SCREEN TEXT: 0,0 s       kart 4-6 s ekran metni taşıyor
şerit 11111-111111--     şerit 11111-111111-      ← planın şeridi, SON HANE eksik
iskelet 14 harf          ⑨ SETUP STRING 13 hane
```

⭐ **Eksik sahne ADIYLA:** ⑦ AKSİYON tek başına yazdı —
*"S12 (0 humans, 3 creatures) appears to be missing entirely, as the edit jumps
straight from S11 to the close-up of the creature's feet (S13)."*
Yani planın **S12'si (HALKA — 0 insan · 3 gövde · KAPALI gümüş halka)** makarada
yok; S13'ün toynağı S12'nin yuvasında oturuyor.

⛔ Bu, SPEC'in FİNAL VURUŞ KANITI'nı da düşürür: *"AYAKTA DURAN AÇIK BOŞ KASA ·
128,0 s · TAM 1 tane · aynı karede KAPALI gümüş halka + TAM 3 gövde"* — halka
karesi makarada değil. ② ayrıca kasayı 2:02'de **KAPALI** gördü (1:48'de açık).

⛔ **İKİ ŞIK VAR ve rapordan ayrılamaz:** (a) makara eksik teslim edildi ·
(b) on bir mercek de yanlış saydı. Merceklerin birbirini doğrulaması hiçbirini
elemez. Hakem ölçümdür ve ölçüm yok.

---

## §⑤ ÇAPRAZ KAPI — künye öbekleri

⛔ **Bu partide mercekler bağımsız değil, İKİ OTURUM hâlinde** [D110 · 5. vaka]:

| öbek | mercekler | süre | kart | kesme | ses ekseni |
|---|---|---|---|---|---|
| **1** | ① ② ③ ⑤ ⑥ | 2:14 | 2:10-2:14 (4 s) | 13 (②③⑤⑥) · 12 (①) | "nothing audible to me" |
| **2** | ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ | 2:16 | 2:10-2:16 (6 s) | 12 | "room tone present" |

Aynı dosya, **iki kuyruk uzunluğu, iki ses durumu**. Betik ②+⑤+⑥ için
ORTAK DEFTER ŞÜPHESİ bastı; ikinci öbeğe aynı testi uygulamadı → [[ADAY-14]].

### ⛔ REPLİK EKSENİ — hakemsiz çelişki

```
⑦ AKSİYON  · ⑩ OYUNCULUK    → LINES HEARD: 4   (aynı oturum · BİREBİR aynı transkript)
   1:41 "We are ready, proceed eleven."
   1:44 "Emptied on the mark."
   1:45 "Copy that, looks clean, setting it down now."
   1:48 "And that is all of it."
⑧ ⑨ ⑪ ⑫ (aynı oturum)      → "none — room tone present"
① ② ③ ⑤ ⑥ (öteki oturum)   → "none — nothing audible to me"
③ SES — EKSENİN SAHİBİ      → "NO VERDICT — NOTHING MEASURED" (0 kategori puanlandı)
```

⚠️ Betiğin "9 mercek 0 dedi, 2 mercek 4 dedi" okuması **yanıltıcıdır**: bölünme
mercege göre değil OTURUMA göre. SPEC `DIALOGUE LINES: 0 · HUMAN 0 / MACHINE 0`
diyor ve promptlarda **AUDIO bloğu 0 · tırnak içinde replik 0**. → [[ADAY-10]]
güncellemesi (hipotez karşı vaka aldı) · **kapanışı 10 saniyelik dinleme.**

### ⑬ KURULUM EKSENİ — hiçbir kapının bakmadığı çelişki

```
② repeat map   B: S1,S2,S7,S9,S10 · C: S3,S8 · D: S4,S6      (9 kurulum)
⑨ SETUP STRING A B ? ? D E ? ? F ? G ? A                      (S2·S3·S7·S9·S11 MISS)
```
İkisi aynı anda doğru olamaz. → [[ADAY-15]]

---

## 📊 SKOR ÖZETİ — ⛔ HİÇBİRİ TABLOYA GİRMEDİ

| Mercek | Mod | İddia | Betik düzeltmesi | Verdict | Karar |
|---|:--:|:--:|:--:|---|:--:|
| ① KARE | D | 8.4 | **5.3** (6 hücre `—`) | REGENERATE | GEÇERSİZ |
| ② DEVAMLILIK | — | 9.1 | **5.5** · Σ fabrike (n=11/Σ=101 ↔ 12/111) | DRIFTS BUT RECOVERABLE | GEÇERSİZ |
| ③ SES | — | N/A | — (0 kategori) | NO VERDICT — NOTHING MEASURED | GEÇERSİZ |
| ⑤ ARKA PLAN | V | 9.6 | **8.0** (7 hücre `—`) | FIELD HOLDS | GEÇERSİZ |
| ⑥ FİZİK | D | 9.8 | **9.0** (7 hücre `—`) | PHYSICS HOLDS | GEÇERSİZ |
| ⑦ AKSİYON | D | 10.0 | **—** (9 hücrenin 9'u `no in-scope source`) | ACTION READS | GEÇERSİZ |
| ⑧ EFOR | D | 4.0 | 4.0 (düzeltme yok) | WEIGHTLESS WORK | GEÇERSİZ |
| ⑨ KADRAJ | D | 6.1 | **1.0** (4 hücre `—`) | SETUP BROKEN | GEÇERSİZ |
| ⑩ OYUNCULUK | D | 4.6 | 4.6 | THE CHOICE IS INVISIBLE | GEÇERSİZ |
| ⑪ IŞIK | D | 6.5 | **4.0** (3 hücre `—`) | KEY WALKS | GEÇERSİZ |
| ⑫ HOOK | D | 5.2 | 5.2 | HOOK MISSING | GEÇERSİZ |
| ④ HİKAYE | — | **KOŞMADI** | — | — | zorunlu eksen ölçülmedi [D111] |

⭐ **⑦ AKSİYON 10,0/10 yazdı ve dokuz hücresinin dokuzu `no in-scope source`.**
D131 düzeltmesinden sonra puan taşıyan hücre **sıfır** — "ACTION READS" bir
ölçüm değil, boş bir tablodur.

---

## ⬜ AÇIK KİLİT DEFTERİ — kareyle kapanacak

| # | madde | kaynak | durum |
|---|---|---|---|
| ⬜1 | Başlık kartı gerçekten var mı, kaç saniye (4 mi 6 mı)? | iki öbek çelişiyor | AÇIK |
| ⬜2 | Makarada 13 klip mi 14 mü? Eksik olan S12 (HALKA) mi? | ⑦ vs plan | AÇIK |
| ⬜3 | 1:38-1:52'de konuşma VAR mı? | ⑦⑩ vs ③ | AÇIK — **10 sn dinleme** |
| ⬜4 | Ses kanalı var mı, ortam yatağı 14/14 serili mi? [D83·D136] | ③ "nothing measured" | AÇIK |
| ⬜5 | Üretici filigranı 0 kare mi? [D150·D177] | ölçülmedi | AÇIK |
| ⬜6 | S6'da şerit KIRMIZI mı MAVİ mi? | ② 🟠 MAJOR | AÇIK |
| ⬜7 | S3'teki bilek saati sonraki sahnelerde var mı? | ② 🟠 MAJOR | AÇIK |
| ⬜8 | 2:02'de kasa AÇIK mı KAPALI mı? (final vuruş kanıtı) | ② 🟠 MAJOR | AÇIK |
| ⬜9 | S2/S3/S7'de key ışık gerçekten kayıp/ters mi? | ⑪ vs ⑥ ("14/14 PASS") | AÇIK |
| ⬜10 | S7'de orta canlıda kaynaşmış/5. bacak var mı? | ①⑤ 🟠 MAJOR | AÇIK |

⛔ **⑩ ÖNERME KAPISI + SINIR SORUSU [D183]:** "ezik ot geri kalkmıyor / dalga ile
hareket etmiyor" bir devamlılık hatası DEĞİL, filmin kuralıdır. Bu koşuda hiçbir
mercek bunu kusur yazmadı ✅ — ama kuralın **nerede bittiği** kareyle sınanmadı.

---

## 🔬 ⑥ vs ⑪ — aynı eksen, ters hüküm

```
⑥ FİZİK  "SCREEN DIR | Sun LEFT, Shadows RIGHT | S0-S12: Shadows point right
          14/14 scenes | Δ 0 | PASS"          ← kendi künyesi 13 sahne diyor
         "LIGHT CALENDAR | S0 1,5× GÖVDE → S13 3× GÖVDE | ölçülen: S0 1.5x body
          → S12 ~3x LEG height | Δ 0 | PASS"  ← iki AYRI cetvel, fark 0
⑪ IŞIK   S2 key KAYBOLDU · S3 key 9→3 TERS DÖNDÜ · S7 key KAYBOLDU
          3 ışık sıçraması · 6,5/10 · "KEY WALKS"
```
⑥'nın "measured on screen" sütunu SPEC'in kendi paydasını taşıyor. → [[ADAY-13]]

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

| # | ders | kapı | doğrulandı |
|---|---|---|---|
| **D194** | ⑨⑩⑪ dizisini rubrik boşluklu yazar, betik boşluksuz okur — D184'ün kapısı üç mercekte birden koşmadı | BETİK · `gozlem_dizi()` + 3 rubrik | ✅ yamandı, kapı ateşledi |
| **D195** | ⑳ ZORLANMA penceresi tek zaman-çizelgesi biçimine çapalıydı — 4 filmde hiç açılmadı | BETİK · `EFOR_PENCERE` | ✅ yamandı, 9 yeni bulgu |

**TEKRAR işaretlenen dersler:** D188 (→2) · D110 (→5) · D111 (→2) · D161 (→3 parti)
**Gözlem defteri:** ADAY-10 güncellendi (hipotez karşı vaka aldı) · ADAY-13 · ADAY-14 · ADAY-15 açıldı

---

## ⛔ SONRAKİ ADIM — sırası değişmez

```
1. MASTER'ı ver → olcum_kapisi.sh koş  (kimlik + süre + kesme + LUFS + filigran + kart)
2. ⬜1 ve ⬜2'yi kareyle kapat: makarada 13 klip mi 14 mü, eksik olan hangisi
3. ⬜3'ü kulakla kapat: 1:38-1:52 dinle
4. rapor_kontrol.py'yi --olcum-sahne / --olcum-kesme / --olcum-filigran ile TEKRAR koş
5. ④ HİKAYE merceğini koş (zorunlu küme eksik)
6. Ancak bundan sonra: T tablosu satırları · kesme listesi · yeniden üretim
```
