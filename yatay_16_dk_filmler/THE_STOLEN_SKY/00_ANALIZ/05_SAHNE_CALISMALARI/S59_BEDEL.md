# 🔬 S59 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_STOLEN_SKY

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ. ⛔ Bu dosyada PROMPT YOKTUR.
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md` + `00_96_KLIP_PROMPT_HAZIRLIK.md` S59 bloğu.
> **Yazıldı:** 20.09.2026.

---

## 🪪 KİMLİK

```
SAHNE:      S59 (sahibin V60)   BAŞLIK: Kayıp
BÖLÜM:      THE_STOLEN_SKY_BOLUM_5.md
ZAMAN:      590.000 s → 600.000 s   FORMÜLLE [D122]: hook(0) + n × 10,000 (n = S numarası)
VURUŞ:      her şeyin kaybı (%62)               B5 SATIRI: BEDEL ⭐ (Bor ölür) · AYRILIK sonucu
⭐VİRAL:    hayır — opak vizör, YÜZ satırı yazılamaz (SAPMA 3); hareket enerjisi: kaldıraç yükselir · silah düşer · gövde kayar (orta)
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Kaldıraç yükselirken Serrak Bor'u vurur; silah yere düşer, gövde kasadan kayar, durum ışığı söner — Mara kafes telinin ardından görür.
BAŞTA:           kaldıraç yeni yükselmeye başlamış; tel kafes ön planda; Bor kasaya yaslı (topal, silah boş), Serrak üç gövde boyu ötede kolu kalkık; Mara'nın eldiveni tele bastırılmış
SONDA:           Bor kadrajın altında kaybolmuş (kaldıraç yükseldi); son görülen hâli: gövde kasanın dibinde, silah zeminde, göğüs lambası sönük; Mara'nın eli telde
⛔ KLİP İÇİ DEĞİŞİM: VAR (durum ışığı söner) → ② ARA DURUM YASAĞI + hareket: asıl hareket silahın düşüşü ve gövdenin kayışı (D213 üç satır); ışık son 1 s'de tek adımda söner (`goes dark, and stays dark`), yanıp sönme/solma yok; kaldıraç yükselişi sürekli hareket
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  R        İŞARET: ilk kullanım (tek R)
CAMERA (birebir): medium shot through the fine metal mesh of the lift cage, 35mm spherical lens, the camera rises with the cage

LENS:           35 mm     MESAFE: 2,0 m (tele) · Bor 5 m · Serrak 8 m     YÜKSEKLİK: 1,4 m → yükselir
ÖLÇEK:          MS (kafes ardı)        AÇI TİPİ: hafif yüksek (yükselen)
KADRAJ ENİ:     2,1 (tel düzlemi) · 5,1 (Bor düzlemi) m      HESAPLANDI (§5.2: eni ≈ mesafe × 36/odak) — kadraja alınacak nesne Bor gövdesi 0,7 m · silah 1,2 m · Serrak 0,7 m
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: Bor 176 · silah 300 · göğüs lambası 25 px ⚠️ → lamba TEK BAŞINA okunmaz, üç işaretin üçüncüsüdür (silah + gövde ana kanıt) px (1280 px eni)   ≥100 px ✅ [D179]
ÖNCEKİ SAHNEYLE: S58 (L · MCU · alçak) → R · MS · hafif yüksek yükselen: 1 kademe · ≥45° ✓
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 insan (Mara, el) + Bor (insan, kadrajda tam) + Serrak (Veyra) — HUMAN COUNT 2 + 1 Veyra   ⛔ film boyu KİLİT: sahne başına rakam (İNSAN ŞERİDİ tablodan); bu sahne 2 insan + 1 Veyra (S60'tan sonra Bor 0)
AYRIM EKSENİ:   grafit + hardal göğüs (Bor) ↔ kobalt eldiven (Mara, yalnız el) ↔ soluk seramik (Serrak); tel kafes ön plan keskin
GİREN NESNE:    —        ÇIKAN NESNE: BOR (0 kare / 0 ses S60–S95) · ağır silah (zeminde kalır)
TAŞINAN NESNE:  Mara'nın eldiveni (S58 kolda → S59 telde → S61 sıkılı yumruk) · kaldıraç (S52 · S61)
⛔ BİÇİM KİLİDİ: Veyra anatomi (sayfa ②) · Bor giysisi (sayfa ①) · kaldıraç tel kafesi (`fine mesh`, göz sayısı yazılmaz)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      platform tavan ışığı 4500 K + Serrak'ın kolundaki tek parlama (≤0,3 s, tek çizgi değil nokta) · takvim: platform sabit; S60 C-0 kehribar (planlı sıçrama, mekân değişir)
PALET:     koyu gri platform + hardal/grafit + kafes teli (S58 yakın L kobalt eldiven → S59 kafes dokusu: palet/doku değişir)
SES:       tek parlama · silahın zemine düşüşü (BELİRGİN, ana ses kanıtı) · sönme tonu · kaldıraç mekaniği · Mara'nın kask içi sesi DARALIR (kurguda; promptta AUDIO: kaldıraç + düşüş)
MÜZİK:     yok — sahibin "kask içi algı daralması" kurguda (D180: mutlak sessizlik modelden istenmez)
FİZİK:     0,9 g: silah `drops the height of the crate in half a second and stays where it lands`; gövde kayışı sürtünmeli; kaldıraç sabit hızla yükselir (`one hand-span per second`)
```

## 🎙️ REPLİK (varsa)

```
REPLİK: — (S58 «Git.» önceki klipte; bu klipte kanal sessiz)
```

## ⭐VİRAL — bu filmde etiket YOK (SAPMA 3)

```
YÜZ:       — (vizör opak; ifade değişimi yazılamaz)
HAREKET:   kaldıraç yükselir · silah düşer · gövde kayar (orta)
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER — etiket verilmedi; hareket satırı yalnız kayıt
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D141 · D202 | BEDEL üç işaret aynı klipte, saniyeli | 0–1 s parlama · 2–4 s gövde kayar + silah düşer · 8–9 s lamba söner · 10 s Bor kadraj dışı |
| D213 | TEMAS·DEĞİŞİM·SONUÇ ≥1 s | silah zeminde ≥1 s kadrajda kalır, kaldıraç onu aşağıda bırakır |
| D192 A5 | ölüm sayıyla POZİTİF | 02 §5 A5 cümlesi birebir |
| KART 12 · PB · U1-2 | kompozisyon reddi riski | kafes teli önde, figürler ARD ARDA (Bor 5 m, Serrak 8 m), göz hizasına yakın; uzak platform duvarı çapa; iki red → kadraj değişir, üçüncü yazım YOK; P6 denemesi |
| D207 · U1-6 | Bor topal, silah boş (S57/S58'den) | IMAGE SUBJECT: `weight on the left boot, right knee plate cracked, the long tool hanging empty` |
| D174 | yön nesneyle | `the tall figure's arm points at the broad figure by the crate` |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U1-2 ölüm okunmazsa bedel yok · red riski | üç işaret + nötr tarif + kadraj kuralı; İPTAL KAPISI | ✅ / ⏳ P6 |
| 2 | ⛔ | U1-5 ışık sönmesi nitelik değişimi | ışık son 1 s tek adım; ana hareket silah/gövde | ✅ |
| 3 | ⛔ | U1-10 eldiven-tel teması | temas ilk karede kurulu (eldiven telde), ara katman: tel | ✅ |
| 4 | ⚠️ | U2-9 kask + uzun tüp = silahlı okuma | tüp adlandırılmaz; uzak duvar çapa; Bor'un silahı yerde | ⏳ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   YÜKSEK · PB (kompozisyon) + PK (ölüm/silah sözlüğü) — filmin en red-riskli karesi (02 §6)
NÖTR TARİF:  ince metal tel ardından: geniş gri giysili figür kasaya yaslı; ötede uzun soluk-seramik figürün kolu kalkık; kolun ucunda tek kısa parlama; gri figürün gövdesi kasanın yanından aşağı kayar, uzun koyu alet eldivenlerinden zemine düşer; göğsündeki küçük lamba söner; kafes yükselir, platform kadrajdan çıkar
POZİTİF KİLİT (yasak cümlesi yerine): `a single brief flash at the end of the raised arm; the broad figure's torso slides down the side of the crate; the long dark tool drops from his gloves and lies on the deck; the small lamp on his chest goes dark and stays dark`
```

## 👁️ İZLEYİCİ CÜMLESİ · ÇAPA · SON 3 s (`OYUNCULUK_YAZIM` §1-§2 · `SAHNE_DOLULUGU` §6)

```
İZLEYİCİ CÜMLESİ:  komutan uzaklaşmak istemiyor; kafes onu götürüyor — eli teli sıkar, kaskı aşağıda kalan figürden ayrılmaz
TAŞIYAN KANAL:     KAVRAMA (eldiven tele bastırır) · BAKIŞ (kask aşağıya kilitli)
TASK ONLY MU:      hayır (B)
KART BAĞI:         Mara SINIR (arkadaşını bırakmaz → bırakmak zorunda kalır) · Bor İLK↔SON son yarısı
ÇAPA:              COST — BEFORE (S58 son kare): eldiven Bor'un kolunda, sonra boşta · AFTER (S61): yumruk kapalı, kask sessiz kanala dönük; aynı kanal (el) · fark kısa kenarın ≥⅛'i ✅ (el kadrajın 1/6'sı)
SON 3 s:           SONUÇ — Bor kadrajın altında kayboldu; Mara'nın eli telde, kask aşağıda; kaldıraç yükselmeyi SÜRDÜRÜR (`the cage keeps rising, the hand stays on the mesh`)
ÖLÜ SAHNE 5 SORU:  ① fiil: ETKİNLİK (yükseliş) + TAMAMLAMA (düşüş) ✅ ② direnç: kafes teli, Mara'nın eli ✅ ③ tek kilit ✅ ④ sınır: S60 Serrak döner (şok kesme, gerekçeli) ✅ ⑤ saat: kaldıraç yükselişi ✅
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi (ya da şok gerekçeli)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapama kararı taşıyor (U1-2 üretimde P6 ile sınanır)
☑ politika satırı yazıldı
☑ ⭐VİRAL yok — gerekçe yazıldı
→ THE_STOLEN_SKY_BOLUM_5.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir (FAZ 3 erken sahne)
```
