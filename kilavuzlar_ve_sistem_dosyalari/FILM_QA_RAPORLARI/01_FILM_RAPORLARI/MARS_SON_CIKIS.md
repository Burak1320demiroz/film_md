# 🔴 MARS_SON_CIKIS — FİLM KAYDI

> **Durum:** film ÜRETİLDİ, iki yarım master olarak QA'ya verildi (PART 1 · PART 2, her biri
> ~180 s) · **master ÖLÇÜLEMEDİ** ⛔ (yol verilmedi; ⑦ B1 künyesinde operatörün dosya adı
> `part 1 18 sahne yeni.mp4`) · **üretim defteri BOŞ** (teslim satırı ⬜, klip satırı yok)
> **Koşu:** 15.09.2026 · **on beş mercek × iki bölüm = 30 ham rapor** — 28'i mod V, ⑬ UYUM
> iki kez STEP −1'de DOĞRU DURDU (`INPUT MODE: MISSING` → ✂️ KESİK).
>
> ⛔ **HİÇBİR SKOR SATIRI HİÇBİR T TABLOSUNA GİRMEDİ.** `rapor_kontrol.py` iki bölümde de
> 14 🚨 GEÇERSİZ + 1 ✂️ KESİK. SPEC **VARDI**, operatör çıplak rubriği yapıştırdı [D129 ·
> **SPEC hazırken mod V koşulan film: 18**] · ⑨⑩⑪⑫ karantina [D190] · ⑤ kesme yayılımı ölçümsüz
> parti düşürdü [D107] · ①.9 teslim alarmı bir YAPI uyuşmazlığı (aşağıda §①.11).
>
> ⭐ **BU KAYDIN ÜRÜNÜ: 1 yeni ders (D217 ← ADAY-21) · 10 eski dersin sayacı +1 · 2 yeni aday
> (ADAY-94 · ADAY-95).** Bulguların çoğu PROMPTLA karşılaştırıldı (§BÖLÜM 1/2 "prompt"
> sütunu): ekrandaki hatanın kaynağı ya promptta YAZILMIŞTI ya promptta HİÇ YOKTU — ölçüm
> gerektirmeyen ders tarafı buradan çıktı. Ekran bulgularının sayısal tarafı ⬜ AÇIK.

---

## 📦 MALZEME

```
HAM            02_HAM_RAPORLAR/MARS_SON_CIKIS/ · 30 dosya
               MARS_SON_CIKIS_PART1_<MERCEK>_HAM.md (15) · MARS_SON_CIKIS_PART2_<MERCEK>_HAM.md (15)
               ⚠️ ad kalıbı `_B1_/_B2_` değil `_PART1_/_PART2_` — operatör böyle kaydetti; ham dosya
               YENİDEN ADLANDIRILMADI (kural ④). PART1 = BÖLÜM 1 · PART2 = BÖLÜM 2.
               ⑬ UYUM ×2: 154 B / 136 B — `INPUT MODE: MISSING` (prompt · SPEC · makine tablosu yok)
YARIM MASTER   BÖLÜM 1 = S01-S18 · 0:00-3:00 (film 0:00-3:00)
               BÖLÜM 2 = S19-S36 · 0:00-3:00 (film 3:00-6:00 · rapor tc + 3:00 = film tc)
PLAN           yatay_6_dk_filmler/MARS_SON_CIKIS/ · BOLUM_1 (S01-S12) · BOLUM_2 (S13-S24) · BOLUM_3 (S25-S36)
SPEC           MARS_SON_CIKIS_QA_SPEC.md — A · B · C · E blokları; PART GRID 3 × 12 × 120 s
BETİK          RAPOR_KONTROL/RAPORLAR/MARS_SON_CIKIS_B1_20260915_RAPOR_KONTROL.md · _B2_
```

## §⑪ ÖLÇÜM KAPISI — **KOŞULAMADI**

Master yolu verilmedi, depoda/diskte aranmadı (depo dışı). Kesme · sahne · süre · LUFS ·
filigran · ışık takvimi izi ÖLÇÜLMEDİ; raporların sayıları hiçbir kapıya hakem olarak
girmedi. ⑤ B2'nin *"cyan/white UI play icon bottom-right, 0:00-2:59"* bulgusu (tek mercek)
köşe testiyle kapanır — oynatıcı arayüzü mü, araç filigranı mı [D215] ⬜.

## §② SPEC KAPISI [D129] — **SPEC VARDI · 28/28 mod V**

Rubriklerin hiçbirine `MARS_SON_CIKIS_QA_SPEC.md` yapıştırılmadı (`SPEC BLOCK PROVIDED: no`).
①④⑥⑦⑧⑭⑮ → TEKRAR · ⑨⑩⑪⑫ → GEÇERSİZ/karantina · ②③⑤ tekil ŞARTLI/GO ama parti düştü.
Ders tarafı kontrat §4 (14.09.2026) ile açık: mod V bulgusu ADAY olur, eski dersin sayacını
artırır; ⑨-⑫ bulgusu yalnız ADAY'a destek diye yazılır, sayılmaz.

## §①.11 BÖLÜM KAPISI + §①.9 TESLİM — **YAPI UYUŞMAZLIĞI, EKSİK TESLİM DEĞİL**

```
PLAN / SPEC      3 bölüm dosyası × 12 sahne · SPEC PART GRID 3 × 120 s
6 dk README      QA birimi 2 yarım master × 18 sahne (KILAVUZ_REHBERI §2.6)
QA'YA VERİLEN    2 yarım master × ~180 s (on dört merceğin ortancası 179-180 s = 18 × 10 s)
BETİK            --bolum 1/2 · 2/2 ile koşuldu (uç kategoriler doğru maskelendi: B1 filmin
                 BAŞI, B2 filmin SONU) · ①.9 yalnız BOLUM_n'i saydı → "plan 12 / makara 18-20"
```

①.9'un 🚨 TESLİM ŞÜPHESİ'nin sebebi dosya bölünmesidir: bölüm dosyası sayısı (3) QA yarım
master sayısıyla (2) aynı değil. Süre ekseni 36 × 10 s'yi tutuyor. B2'de kesme sayısı 17-19:
S25 (görüş tüpü) üç kısa plana bölünmüş — `0:59-1:02 · 1:02-1:06 · 1:06-1:09` (② · ④ · ⑭ aynı
üç kesmeyi saydı); SPEC B `sahne içi kesme 0` → ⬜ ölçümle kapanır.
⚠️ Sistem notu (sahip kararı): 6 dk hattında film klasörü 3 bölüm dosyasıyla yazılırsa ①.9
her koşuda yanlış ateşler — ya bölüm dosyası = QA yarısı, ya `--bolum` sahne aralığı alır.

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 15.09.2026

| mercek | B1 tekil | B1 mod · sahne · kesme | B2 tekil | B2 mod · sahne · kesme |
|---|---|---|---|---|
| ① KARE | ⛔ TEKRAR | V · ? · 17 | ⛔ TEKRAR | V · ? · 17 |
| ② DEVAMLILIK | ⚠️ ŞARTLI | — · 18 · 17 | ✅ GO | — · 20 · 19 |
| ③ SES | ⚠️ ŞARTLI 9,3 | — · ? · 22 | ⚠️ ŞARTLI 9,7 | — · ? · ? |
| ④ HİKAYE | ⛔ TEKRAR | V · 18 · 17 | ⛔ TEKRAR | V · 19 · 19 |
| ⑤ ARKA PLAN | ⚠️ ŞARTLI | — · 18 · 17 | ⚠️ ŞARTLI 6,4 | — · 20 · 19 |
| ⑥ FİZİK | ⛔ TEKRAR | V · 18 · 17 | ⛔ TEKRAR | V · 15 · 14 |
| ⑦ AKSİYON | ⛔ TEKRAR | V · 18 · 17 | ⛔ TEKRAR | V · 20 · 19 |
| ⑧ EFOR | ⛔ TEKRAR | V · 19 · 18 | ⛔ TEKRAR | V · 20 · 19 |
| ⑨ KADRAJ | 🚨 GEÇERSİZ | V · 18 · 17 | 🚨 GEÇERSİZ | V · 18 · 17 |
| ⑩ OYUNCULUK | 🚨 GEÇERSİZ | V · 17 · 17 | 🚨 GEÇERSİZ | V · 20 · 19 |
| ⑪ IŞIK | 🚨 GEÇERSİZ | V · 18 · 17 | 🚨 GEÇERSİZ | V · 20 · 19 |
| ⑫ HOOK | 🚨 GEÇERSİZ | V · 18 · 17 | 🚨 GEÇERSİZ | V · 18 · 17 |
| ⑬ UYUM | ✂️ KESİK | M | ✂️ KESİK | M |
| ⑭ HAREKET | ⛔ TEKRAR | V · 19 · 18 | ⛔ TEKRAR | V · 20 · 19 |
| ⑮ YÖN | ⛔ TEKRAR | V · 18 · 17 | ⛔ TEKRAR | V · 18 · 17 |
| **parti** | 🚨 **GEÇERSİZ** — ⑤ kesme yayılımı 5 > 1 (③ 22) · ①.9 | | 🚨 **GEÇERSİZ** — ⑤ kesme yayılımı 5 > 1 · ①.9 | |

`--olcum-kesme` / `--olcum-sahne` verilemedi (ölçüm yok) → parti ayakta tutulamadı.

## §⑤ ÇAPRAZ SAYIM — SPEC ile ekran üç eksende ayrışıyor

```
REPLİK   SPEC A `DIALOGUE LINES: 7` · PLAN replik tablosu 7 satır
         B1 promptlarında 21 tırnaklı dize · ③ B1 22 satır duydu (⑦ B1 "none", ⑫ B1 0 — iki mercek sessiz)
         B2: ③ 8-10 · ④ 10 · ⑥ 9 · ⑦ 12 · ⑧ 13 — tabloya girmeyen replikler üretildi → D203 (ters yön)
ŞERİT    SPEC B İNSAN ŞERİDİ `111…1` (36 × 1) · plan promptlarında `human count 0` sekiz sahne (S17 · S19 · S21 · S22 · S26 · S28 · S29 · S30)
         B2 çoğunluk `-1--111-1-1---111111` — SPEC şeridi plandan türetilmemiş
ÇAĞRI ADI S21 `"Kestrel, Horizon Station. Maintain approach vector."` — altı mercek altı farklı ad duydu:
         "Jesper" · "Gazprom" · "Gaspereau" · "Desolation" · "Desperaux" · "Disruptor"; B1 mercekleri
         "Kestrel"i doğru duydu. Ses motoru özel adı tek sahnede bozdu; duyulanlardan biri
         GERÇEK şirket adı (⑯ politika riski). Tek sahne · tek film → deftere düşmedi, burada gözlem.
```

---

## BÖLÜM 1 — S01-S18 (film 0:00-3:00)

| # | bulgu | mercek · tc | prompt (kaynak) | ders |
|---|---|---|---|---|
| 1 | Açılış 10 s'de soru yok — kasa freni "prosedür" okunuyor | ④ Hook 6 · 0:01 · (⑫ 3 karantina) | S01 başlığı `Kanca: Freni tut`; prompt freni · pimi yazıyor, tehdidi değil | **D211** +1 |
| 2 | Replik ekranda olanı söylüyor ("Electrical fire behind service hatch") | ④ Dialogue 6 · 1:31 | replik tablosu İŞLEV: `Durum bilgisi` · `Ölçüm` · `Tamamlama` | **D217** (ADAY-21 terfi) |
| 3 | Dört ayrı arıza art arda okunuyor — montaj/kontrol listesi etkisi | ④ Structure 6 · 1:00-1:50 · (⑫ Plateau 5 karantina) | zincir PLANDA var (S08 kanal yalıtımı yanıyor → S10 kapak arkasında ark → S11 şalter, yangın kanalda sürüyor) ama her halka başka yerde, başka nesnede; bağ yalnız replikte (`fire is in the duct`) | **ADAY-94** |
| 4 | İs yıpranması S15'te sıfırlandı · S18'de önceden olmayan kan lekesi | ② · 2:05 → 2:22 · 2:52 | SPEC C `YIPRANMA … S14 yangın isi (S15-S36 boyu)` İLAN ETTİ; S15 IMAGE yalnız `dirty off-white EVA suits` — isin yeri yok · S14 IMAGE `suit plate intact` | **D42** +1 |
| 5 | Kapı S13'te plandan önce tamamen indi (S14 planı `hangs 15 cm above threshold`) · Aras S15'te iki bacağına basarak koşuyor | ② 🟠 2:09/2:10 · ⑧ 2:00-2:29 | S15 IMAGE `clutches his injured left arm … uneven, painful stride` YAZIYORDU — durum taşındı, film sıfırladı | **D207** (B2 kanıtıyla birlikte) |
| 6 | Turuncu omuz yaması S1 sol → S9 sağ omuz | ② 🟠 0:08 / 1:21 | SPEC C KİMLİK DİZİSİ yama konumunu yazmıyor (yalnız renk + askı) | **D208** +1 |
| 7 | Kapının gövdeye temas noktası kadrajda okunmuyor | ⑦ 🟠 B25 2:08 | S13 teması `7.0s - 10.0s`'ye koymuş, SONUÇ satırı yok | **D213** +1 |
| 8 | Kapı panelinde bozuk yazı "RESTRICGET FLTACK" | ① 🔴 2:08 · ⑤ 2:09 | S13 promptunda yazı yok — motorun tehlike-kapısı alışkanlığı; NEGATIVE metin yasağı var | ⬜ (D215 alanı · ölçüm) |
| 9 | Boşta beden: kupa sonrası boş havada parmak (PHANTOM) · hedefsiz 180° dönüş (SPIN) · kapıdan kaçarken el sallama (OVERGESTURE) | ⑭ 0:37 · 1:16 · 1:55 | S08 `3.0s - 7.0s` satırında bedene fiil yok; dönüş tam o pencerede | **ADAY-95** |
| 10 | Söndürücü yere sıkılıyor, kıvılcım kapı dikişinde yukarıda (AIM PAST) | ⑮ 🟡 1:30 | S10 köpüğü kapı DİBİNE, arkı anahtar deliğine yazıyor + replik `Foam won't reach the core` — ıska PLANLI | düşer (§⑩) |
| 11 | S12 temiz koridor → S13 alevli kapak · S14 iç koridor → S15 Mars yüzeyi, hava kilidi yok | ② 🔴 1:58/2:01 · 2:18/2:20 | bölüm dosyalarında sınır satırı (End/Start) yok (grep 0) | — (SAHNE_ZINCIRI §5; aday açılmadı) |
| 12 | Konuşurken kapalı ağız | ③ 🟡 0:10 · 0:54 | S02 `Aras (Radio)` · S06 `Aras:` — ikisinde de ağız kadrajda | — (D215 üçüncü kutusu) |

⑥ B1 `PHYSICS HOLDS` 9 × 10/10 ↔ ① B1 🟠 0:33 "liquid pours at 1G Earth rate" — iki mercek aynı
dökmeyi zıt okudu; ölçümsüz karar yok. ⑪ B1 (karantina): S11 şalter kararttı → S12 şerit ışıkları
tam yanık · S05 kırmızı alarm S06'da söndü — SPEC C IŞIK TAKVİMİ "monotonik" · ADAY'a destek değil,
yalnız kayıt [D190].

## BÖLÜM 2 — S19-S36 (film 3:00-6:00)

| # | bulgu | mercek · tc (film) | prompt (kaynak) | ders |
|---|---|---|---|---|
| 1 | Askı S20-S34 SAĞ kolda, S36'da SOL · kadın giysisinde yalnız S33'te lacivert plaka | ② 🔴 0:10→2:50 (3:10→5:50) · 🟠 2:20 | SPEC C `Sol Kol Askısı S14-S36` + S20 `injured left arm` YAZILIYDI — FİLM SAPTI | **D208** +1 |
| 2 | Kasklar S33'te elde → S34'te yeniden takılı | ② 🔴 2:20/2:30 (5:20/5:30) | S34 IMAGE ve VIDEO promptu kask durumunu HİÇ yazmıyor, TIMELINE yalnız kapı | **D207** +1 |
| 3 | İstasyonda 1g yürüyüş / oturma · vakumda RCS gazı buhar gibi kıvrılıyor | ⑥ 🟡 2:21 · ⑭ 🟠 SLIDE 2:22 · ① ⑤ ⑥ 0:04/1:12 | SPEC C `Yörüngede 0.00g` + Physics Bible `true zero-gravity float` ↔ S33-S36 `steps across the threshold` · `sit together on the bench` · `rests her hands in her lap` | **D200** +1 → ⛔ ÇALIŞMIYOR |
| 4 | S21'de Dünya yörüngesi arka planı ↔ S36 penceresinde Mars diski | ⑤ 🟠 0:25/2:55 | DÜNYA ÇAPASI "Kızıl Mars ufku" yörünge promptlarına inmedi (S19 `deep space`) | **D209** +1 |
| 5 | Kokpit ekranında yanmış yazı/sayı · "RADIATION DOSIMETER" etiketi · dozimetre ekranı bloklara çöktü | ① 🔴 0:41 · 2:41 · ⑤ 🟠 2:44 | S23 `5 m/s … 25 meters` · S31 `"HARD LOCK" indicator lamps` · S32 `"PASSAGE CLEAR"` · S35 `count down … 450 millisieverts per hour` | **D138** +1 |
| 6 | Telemetri repliği göstergenin söylediğini okuyor | ④ Dialogue 8 · 0:02-0:30 | S19 `"Orientation aligned. Horizon locked."` | **D217** (2. kanıt) |
| 7 | Kadrajdaki bedene iş yok: hava kilidinde nedensiz gövde sallanması (SPIN) · son sahnede omza uzanan el havaya iniyor (MISS) | ⑭ 🟡 2:34 (5:34) · ⑮ 🟠 2:54 (5:54) | S34 `IN FRAME: full body`, TIMELINE üç satırı da KAPI · S36 `the room settles into deep peaceful silence … fades out` | **ADAY-95** |
| 8 | Yanaşma mekanizması üç açıda üç farklı tasarım (halka → pim yakası → dört pençe) | ⑤ 🔴 0:35 · 1:15 · 1:55 | S22 `circular docking port` · S26 `three … guide pins` · S30 `three heavy steel mechanical latches` — mekanizma parça parça, her sahnede başka parça; film pim 4→3, pençe 4 (plan 3); REFERANS_PAKETI paneli üretildi mi ⬜ | ⬜ (ADAY-2 alanı — referans paneli; ikinci vakası değil, panel durumu bilinmiyor) |
| 9 | Hava kilidine girişte ekran yönü kesmede terslendi (FLIP) | ⑮ 🔴 2:20 (5:20) | S33 promptunda yön cümlesi yok | — (tek bulgu) |
| 10 | Kalın basınçlı eldivenle ince ayar düğmesi çıplak el gibi dönüyor | ⑧ 🟡 1:06 | S25 `rotate the mechanical reticle ring` — direnç satırı yok | — (D169 alanı; sayılmadı) |

⑨ B1/B2 `RHYME BROKEN` — mercek İLK ve SON kareyi çift saydı; SPEC `EŞ KADRAJ S01↔S31` ve
`DÖNGÜ KANITI S01 kasa pimi ↔ S31 kenetlenme leveri` — belgesiz mercek yanlış çifti ölçtü, bulgu
DÜŞER (plan uydurma · D190). ④ B2 Ending 9/10 ↔ ⑫ B2 Exit & Return 4/10 — final için mercekler
ayrıştı; D211'in son-10-s satırına sayılmadı.

---

## §⑩ ÖNERME KAPISI — planla okunan / düşen bulgular

| bulgu | plan | karar |
|---|---|---|
| ② B1 "S1-S3 … Aura" · ③ "Arras" | PLAN karakter adı Lena / Aras | isimlendirme mercek duyumu — düşer |
| ⑮ B1 V11 1:30 AIM PAST (köpük yerde, ark yukarıda) | S10 köpük kapı dibine · ark anahtar deliğinden · `Foam won't reach the core` | PLANLI ıska — düşer |
| ⑥ B1 `GRAVITY: 3.7 m/s²` iç mekân dâhil · ⑧ B1 FLAG "habitat 0.38g mi 1.0g mi" | Physics Bible yalnız `MARS SURFACE (0.38g)` + `ORBIT (micro-g)`; habitat içi YAZILMAMIŞ | ⬜ planın açığı (D200 notuna eklendi) |
| ⑤ B2 FLAG "Earth orbit throughout or transit to Mars?" | film Mars yörüngesinde | FİLM SAPTI → D209 |
| ② B2 FLAG "sling side?" | SPEC C `Sol Kol Askısı` | FİLM SAPTI → D208 |
| ② B1 FLAG "lander docked to hab or freestanding?" | plan S15 yüzeyde rampa · bağ yazılmamış | ⬜ |
| ④ B1 FLAG "arıza dizisi montaj mı tek felaket mi?" | promptlar zinciri kuruyor (S08 → S10 → S11 `fire is in the duct`) ama halkalar farklı nesnede | → ADAY-94 |
| ⑨ B1/B2 RHYME BROKEN | EŞ KADRAJ S01↔S31 | düşer (yanlış çift) |

## 📋 FLAGS FOR DOCUMENT CHECK — plandan cevaplar

```
① B1 0:40 kadın astronot tavan tutamağına asılı — "zero-g/egzersiz?"  → S05 `pulls down the main shutter release lever` (plan) · bulgu değil
② B1 omuz yaması hangi kolda?                                        → SPEC yazmıyor (D208 notu: yama konumu kanala eklenmeli)
③ B1 0:10 · 0:54 replik kapalı ağızla — "iç telsiz mi?"               → S02 `(Radio)` · S06 oda repliği; ikisinde ağız kadrajda → D215 kutusu
⑧ B2 askılı kol S31 levere yardım edebilir mi?                        → plan: Lena çeker, Aras yaralı (S31) · bulgu değil
④ B2 dozimetre neden hızla düşüyor?                                   → S34 fırtına sığınağı kapısı + S35 (plan) · okunmadı, sebep kadrajda değil
```

---

## 🔁 DERS DÖNÜŞÜ

TEKRAR: D200 · D207 · D208 · D209 · D211 · D213 · D42 · D138 · D203 · D129 — sayaç +1 (on eski ders; D200 5. vakayla ⛔ ÇALIŞMIYOR → dönüştürme borcu)
- D200 — istasyon içi 1g yürüyüş/oturma (SPEC 0.00g) + vakumda buhar gibi RCS gazı · sayaç 4 → 5 → `DERSLER/03_FIZIK_VE_HAREKET.md`
- D207 — S33 kasklar elde → S34 takılı (S34 promptu durumu yazmıyor) · B1 yaralanma S15'te sıfırlandı (prompt taşıyordu) · 0 → 1 → `02_KARAKTER_VE_CANLI.md`
- D208 — askı SOL ilan edildi, SAĞ üretildi · yama omuz değiştirdi · S33 renk plakası · 0 → 1 → `05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md`
- D209 — Mars çapası yörünge promptlarına inmedi, S21 Dünya yörüngesi · 0 → 1 → `04_ISIK_VE_CEVRE.md`
- D211 — S01 "kanca" soru taşımadı (④) · 0 → 1 → `07_KURGU_VE_ANLATI.md`
- D213 — S13 kapı teması son üçte birde, sonuç yok (⑦) · 0 → 1 → `07_KURGU_VE_ANLATI.md`
- D42 — SPEC YIPRANMA ilan etti, S15'te sıfırlandı (②) · satır eklendi, 1 → `05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md`
- D138 — pozitif gövdede tırnaklı gösterge yazısı + gösterge rakamı → ekranda bozuk yazı (① ⑤) · satır eklendi, 1 → `06_METIN_VE_PROMPT_DILI.md`
- D203 — TERS YÖN: SPEC 7 replik, promptlar çok daha fazla; ㉓ sessiz · 1 → 2 → `06_METIN_VE_PROMPT_DILI.md`
- D129 (alet) — SPEC vardı, 28 koşu mod V · 17 → 18 film → `08_QA_SURECI.md`

YENİ DERS: **D217** REPLİK EKRANDA OLANI SÖYLÜYOR ← ADAY-21 (THE AMBER LATTICE + MARS_SON_CIKIS · ④ · ikisi de mod V) → `07_KURGU_VE_ANLATI.md` · `00_YASAYAN_DERSLER.md`'ye girdi, D72 çıktı (defterde gerekçe · sahip vetosuna açık)

ADAY: ADAY-94 — kriz zinciri planda var, kadrajda yok: halkalar farklı nesnede, izleyici dört ayrı arıza okudu (B1) · MOD: V · ④ ‖ ADAY-95 — kadrajdaki bedene TIMELINE satırında iş yazılmadı, model boşta dönme/boşa tutuş uydurdu (B2 + B1) · MOD: V · ⑭ ⑮ → `DERSLER/GOZLEM_DEFTERI.md`

> Bölüm başına bir aday (kontrat §4 "tek yeni aday" koşu başınadır; bu film iki bölüm koşusu).
> Deftere düşmeyen gözlemler ve gerekçesi: çağrı adı bozulması (tek sahne) · ⑮ AIM PAST / FLIP
> (tek bulgu) · yanaşma mekanizması morfu (referans paneli durumu bilinmiyor — ADAY-2'ye ikinci
> vaka sayılamaz) · ⑪ ışık takvimi (karantina).

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FİLM: 36 sahne iki yarım masterda tam süreyle teslim edildi; en ağır hatalar DURUM TAŞIMA
   (kask, askı tarafı, is, kapı) ve ORTAM KURALI (yörüngede 1g, Dünya gökyüzü) — ikisi de promptta
   ya yazılmamış ya yanlış yazılmış. Promptun kendisi ekrana yazı ve sayı istedi (HARD LOCK · 450 mSv).
2. QA: 30 koşu, sıfır tablo satırı — SPEC vardı ama yapıştırılmadı (18. film), master yok, ⑬ doğru
   durdu. ⑭ ve ⑮'in ilk gerçek koşusu: ikisi de okunur çıktı verdi, PROMPT ORDERS bir aday besledi.
3. DERS: D217 yeni (replik görüneni söylemez) · on eski dersin sayacı +1 · D200 ⛔ ÇALIŞMIYOR ·
   ADAY-94 (kriz zinciri) · ADAY-95 (işsiz beden). Yeni filmler için en ucuz üç satır: replik İŞLEV
   hücresi · her sahnenin IMAGE'ı önceki sahnenin SON durumunu yazar · ekrana yazı/sayı yazdırılmaz.
```

**Sıradaki iş (bu film):** master + defter teslim satırı → ⑪ ölçüm (`--olcum-kesme/--olcum-sahne`,
köşe testi) → on beş mercek SPEC başta MOD D, yarım master başına `--bolum n/2` → ⑬ için prompt +
defter + `sahne_kapisi.sh`. ⚠️ Bölüm dosyası sayısı (3) ile QA yarısı (2) uyuşmazlığı sahip kararı.
