# 🌑 THE BLACK CRADLE — FİLM QA KAYDI

> **Film:** THE BLACK CRADLE · 16:9 yatay · 3-5 dk · `yatay_3_5_dk_filmler/THE_BLACK_CRADLE/`
> **Plan:** 26 sahne (S0-S24 + S19b) · 259 s (4:19) · 26 klip · 14 replik / 12 sahne
> (7 MACHINE + 7 HUMAN) · 14 sessiz sahne · 26/26 sabit lockoff · viral ara S4·S7·S15·S21
> **Kurgu (ölçülen):** 232 s · 🔧 raporu **21 kesme** saydı · diğer dört mercek **4 sahne** saydı
> **QA tarihi:** 17.08.2026 — **beş mercek aynı oturumda, beşi de mod V**
> **Ham raporlar:** `../02_HAM_RAPORLAR/THE_BLACK_CRADLE_{TEKNIK,SENARYO,MANTIK,KARAKTER,SES}_HAM.md`

---

## 📊 BEŞ KOŞUNUN DURUMU

| Mercek | Rapor skoru | Verdict | Koşunun geçerliliği |
|---|:--:|---|---|
| 🔧 VIDEO (teknik) | **6.0/10** Ⓥ | (rapor verdict yazmadı) | ⚠️ **ÖN KOŞU** — SPEC planda hazırdı, mod V koşuldu [D94 ×6] |
| 📖 SENARYO | ~~6.8/10~~ Ⓥ | ~~SHOOT WITH TRIMS~~ | 🚨 **GEÇERSİZ** — 23 kliplik filmi 4 sahne olarak haritalandırdı [D107] |
| 🧩 MANTIK | ~~5.6/10~~ | ~~FIXABLE IN EDIT~~ | 🚨 **GEÇERSİZ** — aynı 4 sahne + iki kapsam-dışı puan [D107 · D108] |
| 🧍 KARAKTER | ~~5.8/10~~ | ~~DRIFTS BUT RECOVERABLE~~ | 🚨 **GEÇERSİZ** — kendi kanıt tabanı eşiğini deldi [D97] + 4 sahne [D107] |
| 🔊 SES | ~~5.6/10~~ | ~~AUDIBLE DRIFT~~ | 🚨 **GEÇERSİZ** — 2/14 replik, register yarısı ters [kart E3 adım 2] |

```
⭐ BU KOŞUNUN TEK CÜMLESİ: film ölçülmedi, ÖLÇME ALETİ ÖLÇÜLDÜ.

Beş rapor aynı 232 saniyelik dosyaya koşuldu ve dosyanın kaç parçadan
oluştuğu konusunda ikiye bölündüler:
   🔧 VIDEO           → 21 kesme, zaman kodlarıyla listeledi  (~22 segment)
   📖🧩🧍🔊 diğer dördü → "SCENES OBSERVED: 4"

Dördünün sahne haritasında S3 = 1:25-2:50 (85 s) ve S4 = 2:50-3:52 (62 s)
diye iki "sahne" var. Bu hattın klip tavanı 10 saniyedir; 85 saniyelik tek
sahne bu boru hattında ÜRETİLEMEZ. Yani dört merceğin STEP 1 envanteri
fiziksel olarak imkânsız bir malzemeyi tarif ediyor — ve Yapı, Coğrafya,
Yıpranma, Ortam Devamlılığı puanlarının hepsi o envanterden türetildi.
```

---

## ⭐ ANA BULGU 1 — AYNI DOSYA, İKİ FARKLI SAHNE SAYISI [DERS 107]

| Mercek | Malzeme okuması | Sahne/kesme | En uzun tek "sahne" |
|---|---|:--:|:--:|
| 🔧 VIDEO | compilation edit, 232 s | **21 kesme** (zaman kodlu) | — |
| 📖 SENARYO | 232 s | **4 sahne** | 85 s (1:25-2:50) |
| 🧩 MANTIK | 232 s | **4 sahne** | 85 s |
| 🧍 KARAKTER | 232 s | **4 sahne** | 85 s |
| 🔊 SES | 232 s | **4 ortam bölgesi** | 85 s |

```
Bu bir yorum farkı değil, bir SAYIM çelişkisidir ve tek başına raporlardan
görülür — master'a bakmaya gerek yok, maliyeti sıfır.

BEDELİ, kalem kalem:
· 📖 Yapı 6/10 · Duygu Yayı 6/10 · Final 8/10 · Tutundurma 7/10
     → dördü de "4 sahnelik film" varsayımının puanı
· 📖 "umut anı yok, bedelli seçim yok"  → filmin S17 İPTALİ ve S18 BEDELİ
     85 saniyelik tek "yörünge sahnesi"nin içinde eridi
· 🧩 Coğrafya · Zaman-Işık · Kurulum → 4 mekân üstünden ölçüldü, planda
     yörünge/rıhtım tarafı tek başına 10+ sahne
· 🧍 pasaport 2 karakter × 1'er sahne → WEAR TIMELINE tek satır
· 🔊 ortam haritası 4 satır → "kesmelerde yatak ölüyor mu" sorusu (bu
     merceğin ana sorusu) hiç sorulmamış oldu
```

⭐ **Ve dört rapor birbirinden bağımsız değil:** 🧩 ile 🔊 raporlarının severity
tally'si birebir aynı (`🔴1 🟠2 🟡3`), üç rapor aynı iki zaman kodunu (1:09 ·
1:45) aynı saniye tahminiyle (~0.4 s) taşıyor. Aynı oturumda arka arkaya koşulan
mercekler birbirinin defterini devraldı → **DERS 110**.

---

## ⭐ ANA BULGU 2 — TEK GÖZLEM, DÖRT TABLO [DERS 108]

D102 "hiçbir gözlem iki kez faturalanmaz" kuralı **rapor İÇİNDE** çalışıyor;
raporlar ARASINDA çalışmıyor. Bu koşuda iki gözlem, dört ayrı tabloya düştü:

| Gözlem | 🔧 VIDEO | 🧩 MANTIK | 🧍 KARAKTER | 🔊 SES | Sahibi (rubriklerin kendi kapsam listesine göre) |
|---|:--:|:--:|:--:|:--:|---|
| **1:09 dudak senkronu ~0.4 s** | §8 🟠 (5/10) | Nedensellik **5/10** (−5) | Ses **5/10** (−5) | Performans **5/10** (−5) | 🔧 VIDEO §8 — üç rubriğin de ❌ listesi bunu VIDEO'ya veriyor |
| **1:45 vakumda motor gürültüsü** | §8 🔴 | Fizik **4/10** (−6) | (OUT-OF-SCOPE'a yazdı ✅) | SFX **4/10** (−6) + Miks 7/10 | 🔧 VIDEO §8 — "sound in vacuum → VIDEO_QA" iki rubrikte YAZILI |

**Çapraz fatura düzeltmesi** (kapsam-dışı kaynaklar hücrelerden düşürülünce):

| Mercek | Rapor skoru | Kapsam-dışı düşüşler | Düzeltilmiş okuma |
|---|:--:|---|:--:|
| 🧩 MANTIK | 5.6 | Fizik 4→kaynaksız · Nedensellik 5→kaynaksız | **~8.4** |
| 🔊 SES | 5.6 | Performans 5 · SFX 4 · Miks 7 → hepsi 1:45/1:09 kaynaklı | **~8.8** |
| 🧍 KARAKTER | 5.8 | Ses 5/10 → SES_QA koşulduğu için N/A olmalıydı | **~6.2** |

```
⛔ Bu düzeltilmiş sayılar TABLOYA GİRMEZ — dördü de hâlâ 4 sahnelik
   fiction'ın puanı. Buradaki değer şudur: raporların bildirdiği hasarın
   büyük kısmı FİLMİN değil, FATURALAMANIN eseridir. İki gözlem, üç
   mercekte 8 kategoriyi aşağı çekti.
```

---

## ⭐ ANA BULGU 3 — QA, KURGU KAPISINDAN GEÇMEMİŞ MALZEMEYE KOŞULDU [DERS 109]

Filmin kendi kapı defteri (`THE_BLACK_CRADLE_PART_A.md` · KAPI KAYITLARI, 17.08.2026)
şunu yazıyor:

```
17.08.2026 · ÜRETİM DURUMU: S0-S14 üretildi (operatör onayı).
17.08.2026 · S15 (kapı 1) · ÜRETİM ÖNCESİ V2 — deneme V2 promptuyla yapılır.
17.08.2026 · S16 video · 3 RED ("I encountered an error" ×3, 0 başarı)
```

Yani depo kaydına göre **kapı 1 (S15) henüz geçilmemiş**, S16 üç kez reddedilmiş.
Ölçülen kurgu ise 232 saniye — ~23 klip. İki ihtimalden hangisi doğruysa iş ona göre:

| İhtimal | Ne demek | Kapanış eylemi (operatör) |
|---|---|---|
| **A** — S15+ üretildi, kapı defteri güncellenmedi | Defter bayat → **D74'ün 3. vakası** | Kapı satırlarını yaz; hangi klipler var, say |
| **B** — Kurgu S0-S14'ün üstüne başka malzeme aldı | Ölçülen dosya filmin kendisi değil | Master'ın klip sayımı (1 dk) |

**Her iki hâlde de KURGU KAPISI koşulmamış:** kapı 26 klip / 259 s ±2 s / ekran
metni 0.0 s / S17 + S21 ekranda diyor; ölçülen 232 s ve ~22 kesme ikisini de
tutmuyor. **Kapıdan geçmemiş kurguya koşulan QA, filmin değil kurgunun puanını
üretir** — bu depoda Cold Burn (0/3), Banded Deep (3/4), Last Shift (klip kaybı)
ile üç kez ölçüldü; bu dördüncü vaka.

---

## ⛔ KİLİT ÇELİŞKİSİ DEFTERİ [DERS 96]

Raporların, planda **YAZILI** bir kilide aykırı bulguları. Hangisinin doğru olduğu
rapordan çözülemez; **master'ın o saniyesi izlenerek** kapanır. Açık madde varken
bu bulgulardan ders yazılmaz, yeniden üretim siparişi verilmez.

| # | Rapor ne dedi (timecode) | Hangi kilit | Çözüm eylemi (~10 sn/madde) | Sonuç |
|:--:|---|---|---|---|
| 1 | 🔧🔊🧍 0:30 ve 1:09 — **ağız görünüyor, oynuyor**, dudak senkronu kayıyor | Plan §KART 3 + KURGU KAPISI: insanlı 13 sahnede kask KAPALI, kokpit ARKADAN, lomboz SIRTTAN, **"insan ağzı okunan kare 0"** | 0:28-0:33 ve 1:07-1:13'ü izle: ağız kadrajda mı | ⬜ AÇIK — kilit tutuyorsa üç raporun dudak-senkron bulgusu **yapısal olarak imkânsız** |
| 2 | 🔊 0:30 "Şafak hattı…" repliği **ekrandaki kadına** atfedildi | Plan §DİYALOG: S2 repliği **MİRA**'nındır; MİRA GÖVDESİZ ve sayı söyleyen her replik MACHINE'dir [D82 sigortası] | 0:30'da ses telsiz filtreli mi, ağız oynuyor mu | ⬜ AÇIK — doğrulanırsa **D82'nin 2. vakası** (Cold Burn'de aynısı olmuştu) |
| 3 | 🧍🧩 "reflective **gold-tinted** face shield" | Plan §KARAKTER: tek parça **optik berrak** panoramik vizör, renklendirme YOK, yansıma YOK [D79 · D95] | 0:15-0:50'de vizör camına bak | ⬜ AÇIK |
| 4 | 🧍 "**off-white / grey** pressure suit" ↔ 🔧 "**dark matte** tactical suit" | Plan §KARAKTER: **mat kömür siyahı** sert kabuk + turkuaz (pilot) / amber (mühendis) çizgi | 0:17'de suit rengi | ⬜ AÇIK — ⚠️ iki rapor birbirini de yalanlıyor; 🔧'ün "orange/teal accent lines" okuması kilide **birebir uyuyor** |
| 5 | 📖🧩🧍🔊 yüzeyde **kadın**, kokpitte **erkek pilot** (ayrı sahnelerde) | Plan: **PİLOT = kadın** (turkuaz) · **MÜHENDİS = erkek** (amber); ikisi S0-S5 yüzeyde BİRLİKTE, S5-S11 kabinde BİRLİKTE | 1:05-1:25'te kabinde kaç kişi var | ⬜ AÇIK |
| 6 | 🔧🧩 "dawn sunlight", "ambient fill bleed", "thin atmospheric haze" yüzeyde | Plan §DÜNYA: **gece yüzü**, albedo ~%1, **TAM 5 yapay kaynak**, dolgu YOK, gölgeler mutlak siyah — filmin ışık imzası | 0:00-1:00: ışık lamba havuzlarından mı geliyor | ⬜ AÇIK — kilit kırıldıysa filmin 1 numaralı görsel tezi kırılmış demektir |
| 7 | 📖🧩🧍 final "**Hangar Bay** / enclosed industrial dock", 2:50-3:52 | Plan: rıhtım **AÇIK YUVA** (açık altıgen kafes omurga üstünde), kapalı hangar depoda YOK; S23 basınçlı güverte ama 10 s | 2:50 sonrasını izle: kapalı hangar mı, açık kızak yuvası mı | ⬜ AÇIK |
| 8 | 🔧🧩🔊 1:45 **vakumda motor gürültüsü** | PART_B prompt AUDIO satırları: *"None — hard vacuum silence"* · *"No exterior sound — hard vacuum"* | 1:40-2:10'u dinle | ⬜ AÇIK — doğrulanırsa **mikste kapanır**, yeniden üretim yok |
| 9 | 🧍 "EVA suit → **internal flight suit**" kostüm değişimi | Plan: film boyunca **TEK suit**; kostüm değişimi yok, yalnız S23'te kask çıkar | 1:05-1:25'te suit aynı mı | ⬜ AÇIK |
| 10 | 🔊 **2 replik** duyuldu | Plan: 14 replik / 12 sahne; yalnız S0-S14 bandında bile 7 replik var | ses master'ını dinle: kaç replik duyuluyor | ⬜ AÇIK |
| 11 | 🧩 `COUNTER CURVE: NONE` | Plan: **dört metinsiz sayaç** — şafak seti 2°→10° · 8 segmentlik rezerv · üç amber ışık üçgeni · dört kelepçe | — (ölçüm kaybı, film hatası değil) | 🔁 **D78'in 5. vakası** |

```
⛔ KURAL (D96): defter kapanmadan bu maddelerden ders yazılmaz, yeniden üretim
   siparişi verilmez. Kapanış maliyeti: master'da 10 zaman kodu, ~3 dakika.
```

---

## ✅ D87 KAPISINDA DÜŞEN BULGULAR — "bu değişim filmin önermesi mi?"

| Rapor bulgusu | Belge cevabı | Karar |
|---|---|---|
| 🧩🧍 "1:05 — yüzeyden kokpite geçiş çekimi yok" (Coğrafya −3 · Kesme −4) | **PLANLI.** §A4 yasaklı sahne denetimi: S5 BİNİŞ'te kapak/merdiven hareketi **kadraj DIŞI** [D69 ①]; S4 gövde rayını kavramayla biter, S5 kabinde kayışla açılır | **DÜŞTÜ** |
| 🧩 "0:55 vs 1:30 — şafak ışığından sert güneşe sıçrama" (Zaman-Işık −3) | **PLANLI ve tek geçiş.** S8 IŞIK SINIRI: araç terminatörün üstünden geçer, gece → motor ışığı → sert güneş ekseni **monotoniktir** (B1b) | **DÜŞTÜ** |
| 📖 "umut anı yok, bedelli seçim yok, duygusal dip yok" | **HEPSİ PLANDA VE PART B'DE:** umut-önce-düşüş %66→%72 (S15-S16 → S17 İPTAL), CENTRAL CHOICE S17, bedel S18'de tek yanan segmentte GÖRÜLÜR | **DÜŞTÜ** — mercek 85 s'lik tek "yörünge sahnesi" gördüğü için ölçemedi |
| 📖 "Özgünlük 6/10 — Interstellar/First Man arketipi" | Filmin novum'u **kör KIÇ ÖNDE yanaşma**; raporun okumasında bu olay hiç geçmiyor | **DÜŞTÜ** — ölçüm kaybı |
| 📖 zirve 1:45'te (yörünge geçişi) | Plan: **DORUK S21 TEMAS**, %85-88 bandında, sahnenin İÇİNDE 6.0 s'de | **DÜŞTÜ** |
| 🧩 "0:55 matkap kapatılmadan bırakıldı" (Kurulum −2) | S3 TOPLAMA planlı: ekipman kutulanıyor, karot kutusu S4'te mühendisin elinde, S23'te yuvasında | **KISMEN DÜŞTÜ** — kapanış çekimi planda yok, açık iplik |

---

## ⭐ FLAGS FOR DOCUMENT CHECK — CEVAPLAR

### 🔧 VIDEO_QA
**S1. "Vakumda ses stilize bir tercih mi, sıkı bilimkurgu mu?"**
→ **SIKI FİZİK.** PART_B'nin yörünge sahnelerinde AUDIO satırı birebir *"None — hard
vacuum silence"* / *"No exterior sound — hard vacuum. Only the radio channel."*
Duyulan dış gürültü ihlaldir ve **mikste kapanır** (defter madde 8).

**S2. "Yüzeydeki yürüyüş/koşu ultra düşük yerçekimi mi?"**
→ **HAYIR.** Yüzey **0.8g** ve **GERÇEK ZAMAN** [D44]: insan temposu Dünya'yla aynı
okunur, ağır çekim yok. Süzülme/kayma bir ihlaldir, tasarım değil. (Ayrıca 0g yalnız
S8 sonrası; iki rejim S8 dışında hiç karışmaz.)

### 📖 SENARYO_QA
**S1. "S1 viral ara mı, kurulum mu — 0:35-1:00 kesilebilir mi?"**
→ 🚫 **KESME LİSTESİ UYGULANMAZ.** Viral aralar **S4 · S7 · S15 · S21** ve dördü de
KESİLEMEZ. Raporun birinci sırası (0:35-1:00) 26 kliplik ızgarada S3-S5 bandına düşer
ve **S4 ŞAFAK DUVARI'nı** (viral #1) içerir. → D94 örüntüsünün 4. vakası
(Third Dune · Ring Light · Last Shift · bu film).

**S2. "Zirve 1:45 mi, kokpitte planlı bir ikilem mi vardı?"**
→ **Zirve S21 (TEMAS)**, plan yüzdesi %85-88. 1:45 ızgarada S10-S11 (karşılaşma +
karar) civarıdır. Filmin bedelli seçimi **S17**, bedeli **S18**.

**S3. "Son planlı sahne hangar dock mu?"**
→ **HAYIR.** Son sahne **S24 FİNAL**: yörüngeden çok geniş — füzyon tahriki yanıyor,
rıhtımda lander **burnu dışarıda**, altta kömür hilali ve jilet inceliğinde terminatör
çizgisi (açılış S0'ın aynası). Kapalı hangar planda hiç yok.

### 🧩 MANTIK_QA
**S1. Vakum sesi** → yukarıda (sıkı fizik).
**S2. "S1-S2 arası kapak/temizlik çekimi planlı mıydı?"** → **HAYIR, bilinçli boşluk**
[D69 ① · A4]. Bulgu düştü.
**Ek:** `COUNTER CURVE: NONE` — planda **dört** metinsiz sayaç var → D78 ×5.

### 🧍 KARAKTER_QA
**S1. "1:05'teki ani geçiş için ara çekim planlı mıydı?"** → Hayır (yukarıda).
**S2. "İki karakter aynı aracın ekibi mi, ardışık bakış açıları mı?"**
→ **AYNI ARACIN İKİ KİŞİLİK EKİBİ.** Pilot AZRA (kadın, 1.70 m, **turkuaz** çizgi) ve
mühendis DENİZ (erkek, 1.84 m, **amber** çizgi); solda pilot, sağda mühendis, tek kabin.
Raporun "ayrı sahnelerde ayrı kişiler" okuması plana uymuyor → defter madde 5.

### 🔊 SES_QA — ⭐ REGISTER DOĞRULAMASI (kart E3 adım 2)

| Replik | Rapor register | Plan register | Sonuç |
|---|---|---|---|
| 0:30 "Şafak hattı bin iki yüz metrede…" | MACHINE · ON-SCREEN, ağız oynuyor | **MACHINE (MİRA, GÖVDESİZ)** | register ✅ · **atıf 🔴** — MİRA'nın gövdesi yok |
| 1:09 "Kalkıyoruz. Sıkı tutun." | MACHINE | **HUMAN (PİLOT, kask telsizi)** | register 🔴 ters |

```
⛔ SONUÇ: raporun "Atıf 8/10" ve "Sentetik 8/10" hücreleri, planın D82'ye karşı
   yazdığı sigortanın tam üstündeki iki repliği ölçtü ve ikisini de yanlış
   sınıfladı. Bu iki hücreden bulgu ALINMAZ, ders YAZILMAZ.
   ✅ Buna karşılık plandaki register haritası ALET olarak çalıştı: raporun
   hatası ancak plan sayesinde görülebildi (D82'nin amacı buydu).
```

---

## 📋 ONARIM LİSTESİ

### Ölçüm borcu — önce bunlar (film dosyalarına dokunulmaz)
```
1. ⭐ MASTER'IN KLİP SAYIMI (~1 dk): kaç klip, toplam kaç saniye?
      Kapı ölçütü: 26 klip · 259 s ±2 s · ekran metni 0.0 s · S17 ve S21 ekranda.
2. ⭐ KİLİT ÇELİŞKİSİ DEFTERİ: 10 zaman kodu, ~3 dk. Defter kapanmadan
      yeniden üretim siparişi YOK, ders YOK.
3. ⭐ PART_A KAPI KAYITLARI'nı güncelle — S15/S16 ve sonrası ne oldu [D74].
4. ⭐ Kapı geçtikten sonra beş mercek **MOD D** ile tekrar koşulur (plan
      §QA SPEC BLOĞU birebir yapıştırılır). Mod D bu depoda hâlâ hiç denenmedi.
5. ⭐ Her mercek AYRI, TEMİZ oturumda koşulur — bu koşuda dört rapor
      birbirinin defterini devraldı [DERS 110].
```

### Kurguda düzelir (yeniden üretim YOK) — defter kapanınca
```
6. ⬜ 1:45 vakum sesi doğrulanırsa: dış gürültü sustur, gövde uğultusuna indir.
7. ⬜ 1:09 dudak senkronu doğrulanırsa: ağız zaten kadrajda olmamalı — bu bir
      miks işi değil, kadraj ihlalidir (defter madde 1).
8. ⬜ Klip eksiği doğrulanırsa: eksik klipleri kurguya geri koy (26 klip / 259 s).
```

### Yeniden üretim gerektirir (defter kapandıktan SONRA)
```
9.  ⬜ Vizör tonu (madde 3) · suit rengi (madde 4) · yüzey ışık bütçesi (madde 6)
       doğrulanırsa ilgili klipler yeniden üretilir — üçü de filmin görsel imzası.
10. ⬜ Kapalı hangar finali (madde 7) doğrulanırsa S24 yeniden üretilir.
```

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

| № | Başlık | Kaynak |
|:--:|---|---|
| **105** | Aynı dosyaya koşulan mercekler farklı sahne sayısı bildirdi — çapraz sayım kapısı | 🔧 21 kesme ↔ 📖🧩🧍🔊 4 sahne |
| **106** | D102 rapor içinde çalışıyor, raporlar arasında çalışmıyor — tek gözlem dört tabloya faturalandı | 1:09 ×4 tablo · 1:45 ×3 tablo |
| **107** | Kurgu kapısından geçmemiş malzemeye QA koşuldu; kapı defteri kurgudan geride | PART_A kapı kayıtları ↔ 232 s kurgu |
| **108** | Aynı oturumda arka arkaya koşulan mercekler bağımsız ölçüm değildir — ortak defter | 🧩 ve 🔊 severity tally'si birebir aynı |
| 🔁 94 | SPEC planda hazırdı, yine mod V koşuldu — **6. vaka**; kesme listesi yine viral araya girdi (4. vaka) | 📖 kesme listesi 0:35-1:00 |
| 🔁 96 | Kilit çelişkisi defteri **11 madde ⬜ AÇIK** — deponun en kalabalık defteri | tüm mercekler |
| 🔁 97 | Kanıt tabanı eşiği rubrikte YAZILI olduğu hâlde delindi (yüz ~%11 / 1 sahne, sütun yine puanlandı) | 🧍 |
| 🔁 78 | Dört metinsiz sayaç ekranda okunmadı — **5. vaka** | 🧩 `COUNTER CURVE: NONE` |
| 🔁 74 | Kaydı olmayan/güncellenmeyen kapı koşulmamış kapıdır — **3. vaka** | PART_A kapı defteri |
| ✅ 82 | Plandaki register haritası ALET olarak çalıştı: raporun register hatası ancak onunla görüldü | 🔊 kart E3 adım 2 |
| ✅ 65 | `FILM: (not supplied)` — dört rapor doğru yazdı (🔧 hiç FILM satırı yazmadı) | tüm mercekler |
| ✅ 75 | Beş mercek AYNI dosyayı ölçtü — malzeme kapısı tuttu | 232 s ×5 |
