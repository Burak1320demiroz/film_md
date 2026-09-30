# 🎶 GUNES_MEZARI — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR ŞEHRİN GÜNEŞİNİN KAFESTE TAŞINABİLİR OLMASI olarak
    okumalı." — ölçek novum'u; müziğin işi ölçeği DUYURMAK, gizemi büyütmek değil.

TEMPO:        72 BPM — 10 s klip = 12 vuruş = 4/4'te 3 tam ölçü. Sahne sınırları
              30 · 90 · 120 · 140 · 170 · 210 s, hepsi 10'un katı → 7/7 sahne
              sınırı bir ölçü çizgisine düşer (§14).
SÜRE:         240 s = filmin RUNTIME'ı (24 klip × 10,0 s · hook ayrı değil)
MÜZİKSİZ SAHNE: S3 (90-120 s · K10-K12) — ⛔ her filmde EN AZ BİR tane (§10).
              Gerekçe: filmin KANITI burada (K11 arşiv levhası) ve tek replik
              ikinci kez burada duyulur; müzik yorum katardı. K12'nin son
              2 saniyesi TAM SESSİZLİK ve bölüm sınırı oraya düşüyor.
SUB-BASS:     45 Hz + 90 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü 45 Hz'i
              hiç çalmaz; eşlikçi olmadan o katman telefonda YOK demektir)
VURUŞ NOKTASI: 3 tane — 120,0 s (sessizlikten geri giriş) · 170,0 s (alt uç
              ÇEKİLİR, çekirdek yatağından çıkarken) · 210,0 s (filmin TEK tam
              girişi; tiz katman ilk ve son kez burada duyulur).
              ⛔ Dördüncüsü yazılmaz: az olan güçlüdür.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow · Lyria (⬜ sürüm üretim gününde yazılır)
GENRE: slow orchestral drone, cathedral-scaled, no percussion
TEMPO: 72 BPM · 4/4 · one bar = 3.333 s · 10 s clip = 3 bars

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. sub drone 45 Hz with a 90 Hz octave companion, unwavering, no tremolo
  2. bowed double basses and cellos, long notes, audible bow noise
  3. slow struck metal — a heavy pipe struck once every 2 bars, dry, no reverb tail
  4. one high sustained bowed glass tone, entering ONCE at 210 s and never before

DYNAMIC SPREAD — klip ızgarasıyla birebir:
  0-30 s (S1 · K01-K03): layer 1 alone, −26 LUFS, no movement
  30-90 s (S2 · K04-K09): layer 1 + 2; the basses rise one whole tone at 60.0 s
  90-120 s (S3 · K10-K12): SILENCE — no music at all; room tone and the recording only
  120-140 s (S4 · K13-K14): layer 1 + 3 returns, struck metal every 2 bars
  140-170 s (S5 · K15-K17): layers 1 + 2 + 3, densest point of the film, −18 LUFS
  170-210 s (S6 · K18-K21): layer 1 withdraws at 170.0 s; 2 + 3 only, thin and high-passed
  210-240 s (S7 · K22-K24): full entry — layers 1 + 2 + 3 + 4; layer 4 alone over the
                            last 10 s, fading to silence by 240.0 s

SYNC RULE: every layer change lands exactly on a bar line, and every bar line at a
scene boundary (30 · 90 · 120 · 140 · 170 · 210 s) is a downbeat. No ramp crosses a cut.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     KAYITLI İNSAN SESİ — bu filmde suit AI ve telsiz YOK. Tek konuşan
              kaynak bir ACİL DURUM KAYDI: kadın film boyunca konuşmaz, ağzı
              berrak vizörün ardında görünür ve KAPALI kalır.
              ⛔ Kadraj içinde konuşan ağız 0 (⑨ kapısının ölçtüğü şey).
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
              ⚠️ BU FİLMDE band-pass'ın gerekçesi telsiz değil KAYIT: 300-3400 Hz,
              iki yerde atlama, son hecede kırpılma. §3.9: yoğun soğuk hava alt ucu
              yakın ve güçlü taşır, tizleri öldürür — kayıt bu yüzden boğuk duyulur.

KATMAN TABLOSU — ③ SES LAYER COUNT bunu ölçer:
| sahne | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S1 (K01-K03) | halka gerilmesi · kafes uğultusu · müzik L1 · kayıt (yalnız K03) | 4 | oda tonu 0,3 s |
| S2 (K04-K09) | ayak altında kuru kar · pelerin · rüzgâr (1-2 m/s) · müzik L1+L2 | 4 | oda tonu 0,3 s |
| S3 (K10-K12) | lamba vızıltısı · kayıt döngüsü · oda tonu | 3 | oda tonu 0,4 s |
| S4 (K13-K14) | fener menteşesi · kırağı çatlaması · müzik L1+L3 | 3 | oda tonu 0,3 s |
| S5 (K15-K17) | çekirdek nabzı · mühür kırılması · gemi lambaları · müzik L1+L2+L3 | 4 | oda tonu 0,3 s |
| S6 (K18-K21) | kızak buzda · yuvanın oturması · halkaların açılması · müzik L2+L3 | 4 | oda tonu 0,3 s |
| S7 (K22-K24) | taşın ısınması (çıtırtı) · nefes · müzik L1+L2+L3+L4 | 4 | oda tonu 0,3 s |
⛔ Hiçbir sahnede 5. katman yok. ⛔ Dijital sıfır 0 kare — K12'nin "tam sessizliği"
   müzik ve efekt sessizliğidir, oda tonu −60 dB'de AKAR (aksi hâlde kesme duyulur).

REPLİK SAYISI: 2 (ikisi de AYNI kayıt, aynı cümle — ikinci kez döngüde duyulur)
REPLİK METNİ:  "There are children here. Please give the light back."
               ⚠️ SAPMA KAYDI [D74 kalıbı]: sahibin tretmanı bu cümleyi TÜRKÇE yazdı
               ("Burada çocuklar var. Lütfen ışığı geri verin."). Promptta İNGİLİZCESİ
               duruyor çünkü ① kanal İngilizce (`apexaic/KANAL_KIMLIGI.md` §6) ② sesi
               üreten şey promptun kendisidir — Türkçe yazılsa araç Türkçe okurdu ve
               yayın paketiyle çelişirdi. Türkçe özgün cümle BURADA kayıtlı kalır;
               hikâye değişmedi, dil değişti.
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(K_n) = (n−1) × 10,0 s + promptun TIMELINE ofseti
   K03 → (3−1) × 10,0 + 4,0  = 24,0 s   (ilk kez, bozuk ve uzak)
   K10 → (10−1) × 10,0 + 0,0 = 90,0 s   (en yüksek burada; döngü iki kez başa döner)
   ⭐ İki kayıt da GUNES_MEZARI_QA_SPEC.md 🅐 ve 🅑 bloklarında aynı formülle yazılı;
   üçüncü bir yerde elle tekrarlanmaz.
```

## 🎚️ ÜRETİM GÜNÜNE KALAN

```
⬜ Lyria sürümü ve üretim tarihi          ⬜ −14 LUFS / −1,0 dBTP ölçümü (ebur128)
⬜ 45 Hz + 90 Hz eşlikçinin telefon hoparlöründe duyulma testi
⬜ Kaydın band-pass ayarı (300-3400 Hz) ve iki atlama noktasının yeri
⬜ 210,0 s'deki tek tam girişin kesmeye TAM oturduğunun ölçümü (ölçü çizgisi)
```
