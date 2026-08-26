# 🔍 THE DAWN FRONT — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_DAWN_FRONT/THE_DAWN_FRONT_PLANET_FILM.md`
> **Teknik QA (VIDEO_QA):** ✅ **4/10 · REGENERATE** · 05.08.2026 · ham rapor
> `../02_HAM_RAPORLAR/THE_DAWN_FRONT_TEKNIK_HAM.md`
> **Mantık QA (MANTIK_QA):** ✅ **3.0/10 · STRUCTURAL** · 05.08.2026 · ham rapor
> `../02_HAM_RAPORLAR/THE_DAWN_FRONT_MANTIK_HAM.md`
> **Senaryo QA (SENARYO_QA):** ⛔ kapı — `INPUT MISSING` ile durdu (doğru
> davranış; plan dosyası koşuya eklenmemişti). Video + plan ile yeniden koşulacak.
>
> ⭐ **Teknik koşu, projenin ilk dolu-SPEC'li dış model koşusu:** SPEC plan
> dosyasından `THE_DAWN_FRONT_VIDEO_QA_TEK_DOSYA.md` paketine gömüldü,
> kapı ihlalsiz geçti. Ondan önceki SPEC'siz teknik koşu (bütün alanlar
> UNVERIFIABLE) GEÇERSİZ sayıldı ve tabloya girmedi — ama bulguları
> (0:45 el-direksiyon füzyonu · 0:55 yüz morphu · 2:20 başlık kartı)
> geçerli iki raporla örtüşüyor: çapraz doğrulama.
>
> ⚠️ **Kurgu sürümü belirsizliği:** mantık raporu 145 s'lik "_2.mp4"ü,
> teknik rapor 141 s'lik bir videoyu ölçtü. Plan 140 s. Bulgular işlenirken
> hangi kurgunun güncel olduğu doğrulanmalı.

---

# 🔧 TEKNİK QA

## 📋 KÜNYE

```
RUBRİK:        THE_DAWN_FRONT_VIDEO_QA_TEK_DOSYA.md (VIDEO_QA + gömülü SPEC)
QA TARİHİ:     05.08.2026 · model: Gemini
GİRDİ:         video (141 s) + tek dosya paketi
SPEC BLOĞU:    ✅ DOLU — plan §0.10/§0.16 + bible'lardan gömülü
GENEL SKOR:    4/10
KARAR:         REGENERATE (8 🔴 BLOCKER)
GEÇERLİLİK:    ✅ geçerli, ⚠️ sahne-varlık tablosu şartlı (aşağıda)
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Karakter | 4/10 | 0:48 yüz morphu · 1:42 planlanmamış sırt tüpü |
| Ölçek ve Fizik | 3/10 | Moloz ~1g düşüyor (plan 0.28g) · 8° yatma kalıcı değil |
| Kamera ve Kesme | 3/10 | Yaygın tracking (26/26 lockoff planlıydı) · S1/S2'de plansız kesme |
| Işık | 4/10 | Duvar tepesi ATEŞLE aydınlanıyor · güneş sayacı 1:52'de geri gidiyor |
| Çevre | 4/10 | 🚨 Duvar ŞELALE gibi akıyor — sıfır-sıvı sözleşmesi çökmüş |
| Parçacık ve Malzeme | 3/10 | Bacada alev · kuru-gaz kuralı tamamen kırık |
| Ses | 5/10 | Boğuk akustik kaybolmuş · sesler kesmelerle senkron değil |
| Sahne-Beat Varlığı | 4/10 | S6/S7/S9/S10/S12 beat'leri okunmuyor (⚠️ şartlı) |
| Negatif İhlal | 8 | Ateş · sıvı · yüz morphu · film içi metin (2:04) · kesme |
| Hareket | 5/10 | Jello/warp · koşu 0.28g adımı taşımıyor |

## 🚨 EN AĞIR ÜÇ BULGU

```
0:20  🔴  Duvar su gibi akıyor (şelale) — filmin fizik sözleşmesinin çekirdeği
0:48  🔴  Yüz yaşlanıyor, kemik yapısı değişiyor — kimlik kaybı
1:42  🔴  Sırt tüpü beliriyor — Bible "NO back tank" diyordu
```

## ⚠️ SAHNE-VARLIK TABLOSU NEDEN ŞARTLI

Rapor süreyi 141 s (plan ±1 s) ölçüyor ama 6 sahneyi "Present: No"
işaretliyor. 14 slotluk kurguda 6 sahne gerçekten yoksa süre ~80 s olurdu.
Doğru okuma büyük olasılıkla: **slotlar dolu, içerik kaymış** — model her
sahne için klip üretmiş ama S6 (motor kapatma), S9 (tekerlek çökmesi),
S10 (geri vites SEÇİMİ), S12 (overview) beat'leri kliplerin içinde yok.
Süre kontrolü içerik kontrolü değildir (Ders 62'nin orta-film hâli).
Kurgu elle doğrulanmadan "sahne yok" cümlesi kesinleşmez.

---

# 🧩 MANTIK VE DEVAMLILIK QA

## 📋 KÜNYE

```
RUBRİK:        MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — 8 kategori
QA TARİHİ:     05.08.2026
GİRDİ:         yalnızca video (145 s · "_2.mp4") — rubrik doküman istemiyor
BASELINE:      SELF-CONSISTENCY
GENEL SKOR:    3.0/10
KARAR:         STRUCTURAL PROBLEM
GEÇERLİLİK:    ✅ GEÇERLİ — kapı yok, kurala uygun koşu
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | 7/10 | Parçacık ağırlığı sahneler arası oynuyor |
| Sayaç Mantığı | N/A | 🚨 Sayaç HİÇ gözlenmedi — planın ayna sayacı ekrana çıkmamış |
| Mekan Coğrafyası | 7/10 | Gemi (lander) S17'de bir kez belirip kayboluyor |
| Zaman-Işık | **9/10** | ⭐ Serinin en yüksek zaman-ışık skoru — güneş takvimi tutmuş |
| **Kostüm-Prop** | **1/10** | 🚨 Yüz ×3 · suit ×4 · yük ×4 değişiyor |
| Nedensellik | 4/10 | 1:14'te sebepsiz kanayan yanak yarası |
| Nicelik | 2/10 | Tank sayısı 1→2→1→0→1 gidip geliyor |
| Kurulum-Terk | 7/10 | Lander tanıtılıp hiç kullanılmıyor |

**🔴 BLOCKER: 5 · 🟠 MAJOR: 2 · 🟡 MINOR: 0**

## 📖 FLAGS CEVAPLARI (özet — tam hâli ham raporda)

```
Kanonik yüz?    Bible 45 yaş/kırık burun/kırçıl sakal — 3 farklı yüz İHLAL
Kanonik yük?    1 × 0.9 m karot silindiri, hiç inmiyor — tüm varyantlar drift
Yara planlı mı? Hayır — planda yaralanma yok, Ders 42 sınıfı halüsinasyon
```

---

# 🔀 MERCEKLERİN KESİŞİMİ — üç koşu, aynı üç arıza

```
YÜZ MORPHU        teknik 0:48 · mantık 0:07/0:55/1:20 · geçersiz koşu 0:55
EKİPMAN DRIFT     teknik 1:42 sırt tüpü · mantık tank 1→2→0 · suit çizgileri
FİLM İÇİ METİN    teknik 2:04 · mantık 2:20 (out-of-scope satırı)
```

İki geçerli merceğin bağımsız bulduğu bir şey daha var ve en pahalısı bu:
**filmin iki omurgası ekranda yok.** Ayna sayacının üçüncü vuruşu (S8 "tam
dolu") iki raporda da yok; S10 geri vites SEÇİMİ hiçbir raporda okunmuyor
("driver simply drives and parks"). Sayaçsız ve seçimsiz hâliyle bu, planın
filmi değil — kovalamaca görüntüleri.

---

# 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 67 (yeni)  Kelime yasağı yetmiyor — İSTENEN GÖRÜNTÜNÜN kendisi
                  yasak malzemeyi çağırıyor (duvar→şelale, 600°C ızgara→alev)
□ DERS 68 (yeni)  Sahne içi kesme mimarisi tutmadı → PLAN B (§0.20) devrede
□ Ders 16/55      Bible dolu ve birebirdi, yüz yine tutmadı — üçüncü kanıt
□ Ders 42         Yıpranma sürüklenmesi kanlı yaraya kadar büyüdü (1:14)
□ Ders 50 örüntüsü Ayna sayacı üçüncü vuruş ekranda yok — kronometre kayıp
□ Ders 13/34/45   Film içi metin (2:04) — kapanış kartı DEĞİL, ihlal
□ ÜRETİM KARARI   Yeniden üretim PLAN B ile: 26 segment AYRI klip,
                  kesme kurguda (plan §0.20 zaten yazmıştı; S0 test adımı
                  atlanmıştı — bu sefer atlanmayacak)
□ SENARYO QA      video + PLAN dosyasıyla koşulacak (INPUT MISSING doğruydu)
□ KURGU SÜRÜMÜ    141 s vs 145 s — hangisi güncel, doğrulanacak
```
