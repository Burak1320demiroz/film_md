# 🧠 THE_BURNING_ENTRY — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     Sahip verdi (2 dakikalık acil atmosfer girişi, tek iticiyle kanyon inişi ve çakılma aksiyonu)
② FORMAT:   Yatay 2-4 Dk (§2.2) → bölüm sayısı: 2 (BOLUM_1: S00-S05, BOLUM_2: S06-S11)
③ SAHNE:    12 sahne (12 x 10s = 120s runtime)
④ REFERANS PAKETI: YAZILIR — T1 kask/vizör/basınç giysisi + pilot mekiği var. KAPI 0 referans paketi doldurulacaktır.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "2 dakikalık 12 sahne acil atmosfer girişi aksiyonu. Pilot uzay gemisiyle giderken hasar alıp acil iniş yapsın. Tamir sahnesi yok. Her 10 saniyede daha kötü bir şey olsun."
REPLİK: Yok — sözel replik kullanılmayacaktır; yalnız nefes, kalp atışı ve kokpit mekanik sesleri.
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| S00'da HUD ekranında "ALTITUDE LOSS – 00:47" metni | Modelin video üzerine kompoze harf/overlay (prompt bleed) basma riski | HUD göstergesi kokpit içine entegre ışıklı telemetry gösterge paneli ve dijital geri sayım sayacı olarak tarif edilir; video overlay metni basılmaz | D34 / D159 kuralı: Yapay zeka harf çorbası ve overlay yazısı yasaktır |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        Yatay 2-4 Dakika (§2.2)
ORTAM:         §3.5 Yörünge / Atmosfer Girişi / Yabancı Gezegen Kanyon Zemini (S00-S02 yörünge kokpit, S03-S05 re-entry, S06-S11 kanyon iniş)
TÜR:           Bilimkurgu / Acil Hayatta Kalma Aksiyonu (§4.1)
KLİP SÜRESİ:   10 saniye (Veo 3.1 araç limiti)
SAHNE SAYISI:  12 sahne
RUNTIME:       120 saniye (12 x 10s)
BÖLÜM SAYISI:  2 bölüm
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Yörünge bozulumu yaşayan tek kişilik acil iniş mekiğinin, tek çalışan iticiyle dev alien kanyon kuleleri arasında 3 kademeli çakılma manevrası.
NOVUM TAŞIYICISI:    Hasarlı pilot mekiği x tek çalışan itici roket → çakılma rotasından zorunlu kanyon inişi.
① TEK KARE:          Alevler içindeki mekik, kanyonun dev kaya kuleleri arasından tek iticiyle kanyona doğru süzülür.
② KİNETİK BAĞIMSIZLIK: Mekiğin eksen etrafında dönmesi (spin), vizördeki mikro-çatlak ve 3 kademeli zemin teması replik olmadan görsel olarak kanıtlanıyor.
③ BAŞLIK ŞEMASI:     THE BURNING ENTRY
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — BEDEL
▸ tanım cümlesi — Fiziksel hayatta kalma mücadelesi en sert atmosferik kuvvette bile pes etmemektir.
▸ depoda kaç kez kullanıldı — 8 kez (bash sayac.sh TEMA DAĞILIMI)
▸ motif kanalları — Nesne (çatlayan vizör, tek itici kolu) · Kinesik (kasılan parmaklar, soluk buğusu) · Kamera (G-kuvveti sarsıntısı, spin kadrajı) · Işık (turuncu plazma parıltısı, kanyon alacakaranlığı)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| Kask vizörü cam çatlağı | EVET | S04'te başlayan mikro-çatlağın S11'e kadar sürmesi | EVET (Çatlak konumu sol göz hizasında 3cm tek çizgi olarak kilitlendi) | Düşük |
| Atmosfer girişi plazma alevleri | EVET | S03-S05 atmosfer sürtünme alevleri | EVET (DYNAMIC FIRE kuralı ile kaotik sürekli hareket yazıldı) | Düşük |
| Mekik eksen etrafında dönme (spin) | EVET | S05 rotasyon | EVET (CONTINUITY LOCK ile tek eksenli kesintisiz dönüş tanımlandı) | Orta |
| S11 Dev Gölge finali | EVET | Kanyondaki devasa varlık gölgesi | EVET (Uzaylı anatomisi tarif edilmedi; yalnız masif yavaş kanyon gölgesi K0 yazıldı) | Düşük |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  Vizör Cam Çatlağının Kaybolması veya Şekil Değiştirmesi (Devamlılık Arızası)
POZİTİF BİÇİMİ:   Sol vizör polikarbonat yüzeyinde tam olarak 3 santimetre uzunluğunda, 0.5 milimetre genişliğinde tek bir sabit kılcal çizgi çatlağı.
```

```
TETİKLENEN RİSK:  4 / 5
EŞİK:             5
EŞİĞİN ALTINDA:   Malzeme azaltımına gerek duyulmadı.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — yalnız soru ④ "analiz karar versin" ise

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | EVET | Pilot kaskı ve acil iniş giysisi (S00-S11) |
| T2 | biçim kilidi METİNLE tutulmayan varlık | EVET | Pilot mekiği gövdesi ve kokpit kumanda paneli (S00-S11) |
| T3 | oranı sözle yazılamayan nesne | HAYIR | — |
| T4 | insan dışı canlı | HAYIR | (S11'de yalnız gölge var, canlı çizilmiyor) |
| T5 | tekrar eden insan dışı olay | EVET | Atmosfer girişi plazma sürüklemesi (S03-S05) |
| T6 | bir varlık tekrar tekrar dönüyor | EVET | Acil iniş mekiği (12 sahnenin 12'sinde var) |

```
KARAR: YAZILIR — THE_BURNING_ENTRY_REFERANS_PAKETI.md KAPI 0 olarak hazırlanacaktır.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S08 (Üç kademeli çakılma ve kanyon teması)
NÖTR TARİFİ:         Mekik alt gövdesi masif kaya yüzeyine temas eder, kinetik sürtünme ile kıvılcım ve toz bulutu yayarak yan tarafa doğru kayar; pilot emniyet kemeri içinde sabit kalır.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Yörünge bozulumundan sağ çıkıp mekiği yabancı gezegen kanyon zeminine kontrollü çakarak durdurmak.
ENGEL:   Atmosferik plazma sürüklemesi, çözülen mekik ekseni, iki iticiden birinin sönmesi, irtifa kaybı ve dev kaya sütunları.
BEDEL:   S02'de aşırı G-kuvvetinde kasılan parmaklar, S04'te vizörün çatlamasıyla panik klostrofobisi, S07'de tek iticiyi manuel tutma eforu, S08-S09'da 3 kademeli darbe sarsıntısı.
MUHATAP: Mekiğin bozulan mekanik kumanda paneli ve yabancı gezegen atmosferik kuvveti.
AYRILIK: Yok (tek kişilik acil hayatta kalma filmi).
```

---

## ✅ KAPI

```
✅ konsept kapısı ①②③ üçü de ✅
✅ risk sayımı yazıldı (4/5) ve eşik kararı verildi
✅ B5 dörtlüsü tam, BEDEL sahne numaraları (S02, S04, S07, S08, S09) taşıyor
→ Üçü de ✅ olduğu için 03_SAHNE_SIRALAMASI.md yazılabilir.
```
