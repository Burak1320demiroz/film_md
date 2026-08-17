# 🪨 THE BANDED DEEP — FİLM QA KAYDI

> **Plan:** `yatay_2_4_dk_filmler_uzay/THE_BANDED_DEEP_CANYON_PLANET_FILM.md`
> **Format:** 16:9 · 2-4 dk · bilimkurgu (keşif) · ince atmosfer (kanyon, %2)
> **Plan özeti:** 16 sahne × 10 s = 160 s · 0 sahne içi kesme · tamamen sessiz ·
> viral S1·S6·S15 · doruk S10 · CENTRAL CHOICE S9 · insansız S0-S2/S14-S15

---

## 🔭 MERCEK DURUMU (14.08.2026)

| Mercek | Durum | Skor | Geçerlilik |
|---|---|:--:|---|
| 🔧 TEKNİK | koşuldu — mod V | Ⓥ 4.9 | ⛔ **ÖN KOŞU** [D94] — SPEC planda hazırdı, verilmedi |
| 📖 SENARYO | koşuldu — mod V | Ⓥ 7.4 | ⛔ **ÖN KOŞU** [D94] — kesme listesi UYGULANMAZ |
| 🧩 MANTIK | koşulmadı | — | ❌ |
| 🔊 SES (ops.) | koşuldu — STATE B | 6.2 | ✅ geçerli koşu (girdi: tam kurgu ✓, ses var ✓) — bulgular miks işi |
| 🧍 KARAKTER (ops.) | koşulmadı | — | ❌ |

**Üç koşu da AYNI 186 s kurguyu ölçtü** (D75 ✅ — Starless Circle arızası
tekrarlamadı). Ham raporlar: `02_HAM_RAPORLAR/THE_BANDED_DEEP_{TEKNIK,SENARYO,SES}_HAM.md`
+ rubrik dışı segment analizleri `_SEGMENT_ANALIZ_HAM.md`.

---

## 🚪 KURGU KAPISI [D72] — dört madde kontrolü

Plan ızgarası: 16 klip × 10 s = 160 s · ekran metni 0.0 sn · CENTRAL CHOICE
ekranda. Kurgu (raporlardan ölçülen):

```
① KLİP SAYISI    12 çekim (CAMERA raporu) ≠ plan 16          ⛔ İHLAL
② SÜRE           186 s ≠ 160 ±2 s (ASL 15.5 s ≠ 10 s ızgara) ⛔ İHLAL
③ EKRAN METNİ    3:00-3:06 yanık başlık kartı "THE BANDED
                 DEEP" — üç rapor bağımsız gördü             ⛔ İHLAL
④ CENTRAL CHOICE S9 cıvata+ip inişi ekranda VAR (1:43-2:01) ✅
                 AMA bedel zinciri ve final YOK (aşağıda)
```

**Ekranda OLMAYAN plan sahneleri:** S12 (uzun yol — bedelin overview'u),
S13 (boş kalça yuvası + son bakış), S14 (fırlatma), S15 (final/viral 3 —
yukarı). Ayrıca S1 (payandalar virali) ve S7 (gölge kuşağı) kurguda net
seçilemiyor. **Filmin bedel yarısı ve açılış-kapanış aynasının kapanış
kanadı kurguya girmemiş** — Cold Burn deseninin (D72/81) tekrarı: senaryo
raporunun "Ends" okuması ve 7.4 skoru, finalsiz kurgunun puanıdır (rapor
planı bilmediği için 2:46'daki durak karesini final sandı).

**Fazladan sahne:** 1:13-1:28 vizör yansıması CU'su planda YOK (planda
vizör "yansımasız" kilitli — aşağıda defter #5).

---

## ⚖️ KİLİT ÇELİŞKİSİ DEFTERİ [D96]

> ⬜ AÇIK madde varken: skorlar ŞARTLI kalır, bu bulgulardan DERS YAZILMAZ,
> yeniden üretim siparişi verilmez. Çözüm eylemi = master'ın o saniyesini
> izlemek (~10 sn/madde).

| # | rapor ne dedi (timecode) | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | "white backpack" + "backpack strap" (baseline, 0:30+) | D79 sırt yasağı — plan/bible "flat back, no back-mounted unit" (32 promptta) | master 0:30-0:41 izle | ⬜ AÇIK — doğruysa D79'un 6. vakası |
| 2 | "Dust kicks up and hangs" (baseline) + iniş tozu "solid tentacle-like strings" (0:24) | §0.12 TOZ: etek 5 m/4 s oturur, her tane yay çizer | master 0:15-0:29 izle | ⬜ AÇIK — iki rapor (VIDEO+SES) bağımsız gördü, uydurma ihtimali düşük ama kayıt şart |
| 3 | "exits the vessel to explore" HAPPENED (EVENTS, 0:30) | D69 ① — plan A4: biniş-iniş hareketi 0 kare (S3 kadın gemiden 30 m uzakta açılır) | master 0:29-0:35 izle | ⬜ AÇIK — çıkış EKRANDA mı, yoksa raporun çıkarımı mı |
| 4 | "~1g walking gait" (baseline) | §0.12 yerçekimi 0.7 g | ölçülebilir değil — 0.7g/1g yürüyüşü gözle ayrışmaz | ⬜ AÇIK (muhtemelen ölçüm gürültüsü) |
| 5 | vizör yansıması CU'su (1:13-1:28, CAMERA shot 6) | D79 vizör kilidi: "zero mirror coating, zero reflection" | master 1:13 izle | ⬜ AÇIK — planda böyle bir sahne de YOK |
| 6 | müzik 0:00'da giriyor (SES music ledger: cue 00:00-03:06) | plan §3.2: "müzik 0:00'da GİRMEZ, S1'de girer" | kurgu/miks kaydı | **KURGU SAPTI** — miks seansında düzelir, yeniden üretim değil |
| 7 | yanık başlık kartı 3:00 | plan §0.14 A1 + kurgu kapısı: ekran metni 0.0 sn | üç rapor bağımsız teyit | **KURGU SAPTI** — D70/72 zincirinin **6. vakası** (UC · SC · Third Dune · Ring Light · Cold Burn'den sonra); kart kurgudan çıkarılınca kapanır |

---

## 📊 SKORLAR (üçü de tabloya işlendi)

- 🔧 `../LESSONS_LEARNED.md` teknik tablo: Karakter 6 · Fizik 4 · Kamera 6 ·
  Işık 6 · Çevre 6 · Canlı N/A · Hareket 5 → **Ⓥ 4.9/10 ⚠️** (Parçacık 3 ve
  Negatif 3 sütunsuz, ortalamaya dahil)
- 📖 `03_HIKAYE_KALITE_TABLOSU.md`: 7.0/8.0/7.5/7.0/8.0/N‑A/7.5/8.0/7.0/6.5
  → **Ⓥ 7.4/10 ⚠️ ŞARTLI** — tablonun en yüksek mod V skoru ama finalsiz
  kurgunun okuması
- 🔊 `07_SES_KALITE_TABLOSU.md`: Ortam 6 · SFX 5 · Miks 7 · Müzik 7, ilk beş
  kategori N/A (0 replik tasarım) → **6.2/10 SOUNDTRACK HOLDS**

---

## 🚩 FLAGS FOR DOCUMENT CHECK — plandan CEVAPLAR

| Rapor sorusu | Plandan cevap |
|---|---|
| (🔧) 14+ kesme plan sınırlarına oturuyor mu? | Plan 16 sahne = 15 meşru sınır. Kurguda 12 çekim var; sınır eşlemesi ancak master + plan yan yana yapılır. Sahne İÇİ kesme iddiası yok. |
| (🔧) Başlık kartı istendi mi? | HAYIR. Plan A1 ✅ "ekran metni yok"; kapak §5.3 "tipografi post'ta, prompt'a asla" — kart kurguya D70 ihlali olarak girmiş. |
| (🔊) Suit AI/log planlandı mı? | HAYIR — plan 0 replik, tamamen sessiz tasarım (§0.15 DIALOGUE LINES: 0). Sessizlik eksik değil. |
| (📖) S9 (2:26-2:45) planın doruğu mu? | EVET — plan doruk S10 "el ayası ölçümü / silme"; timecode birebir oturuyor. Ayrıca render eksiği VAR: raporun sorduğu "planned discovery effect" = el ayasının bandı TAM ölçmesi jesti; raporlar silmeyi görüyor, ölçme jestini anmıyor → master'da kontrol edilecek (D78 sınıfı aday). |
| (📖) S5 (1:13-1:28 vizör CU) viral ara mı? | HAYIR — viraller S1·S6·S15. Bu sahne PLANDA YOK (defter #5). Raporun CUT önerisi bu kez planla çakışmıyor ama ön koşuda liste zaten uygulanmaz. |
| (📖) Planın son sahnesi ekrandaki mi? | HAYIR — plan finali S15 (yukarı/ana gemi yıldızı). Ekrandaki son kare S11 sınıfı bir duraktır. Final kurguda YOK → Ending 8.0 ve "Ends" okuması finalsiz kurgunun puanı. |

---

## 📚 DERS DURUMU

**Yeni ders numarası AÇILMADI.** Gerekçe iki katmanlı:

1. **D96 kapısı:** en ağır bulguların hepsi (sırt ünitesi · toz şeritleri ·
   gemi çıkışı · vizör yansıması) plandaki yazılı kilitlere aykırı → defterde
   ⬜ AÇIK. Defter kapanmadan bulgudan ders yazılmaz.
2. **Tekrarlar zaten kayıtlı:** yanık başlık kartı = D70/72 (6. vaka, §7
   tuzaklar güncellendi) · sırt ünitesi = D79 (doğrulanırsa 6. vaka) ·
   finalsiz kurgu + ızgara ihlali = D72/81 · SPEC varken mod V = D94
   (5. vaka — AGENTS ortak adım ① listesi güncellendi).

**Defter kapanınca ders adayları (sırasıyla):**
- 🟡 ADAY-1: iniş/fırlatma toz eteği "katı şerit/dokungaç" üretiyor —
  sayısal etek kilidi (5 m/4 s) tek başına tutmadı; tanecik ölçüsü + sayı
  kilidi gerekebilir (kaynak: TEKNİK 0:24 🟠 + SES çapraz teyit).
- 🟡 ADAY-2: "planlanmamış sahne" sınıfı — kurguya planda olmayan çekim
  girdi (1:13 vizör CU). D72 kapısı klip SAYISINI sayıyor, klip KİMLİĞİNİ
  saymıyor.

---

## 🔧 YAPILACAKLAR (öncelik sırasıyla)

```
1. MASTER KONTROLÜ — defterin 5 açık maddesi (~1 dk toplam iş):
   0:15-0:29 toz · 0:29-0:35 çıkış · 0:30-0:41 sırt · 1:13 vizör CU · genel
2. KURGU ONARIMI (yeniden üretim DEĞİL):
   · başlık kartını çıkar (D70 — 6. vaka)
   · müziği S1 girişine kaydır (plan §3.2)
   · SES raporunun 3 miks maddesi: 12-kare ambiyans crossfade'leri (0:29,
     1:42) · eldiven Foley katmanı (2:02) · iniş gürlemesi değişimi (0:24)
3. EKSİK SAHNELER — S12-S15 (bedel + fırlatma + final) üretilip kurguya
   girmeden film teslim edilemez; S14 üç fazlı kalkış promptları hazır.
4. Master kontrolünden sonra: defter kapanır → ders adayları karara bağlanır
   → gerekiyorsa MOD D yeniden koşu (SPEC §0.15 kopyalanarak — D94).
```
