# 🧠 THE_STILL_POINT — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi (Durgun Nokta / The Still Point)
② FORMAT:   yatay 4 dk        → kart §2.3 · bölüm sayısı 2
③ SAHNE:    24                → formatın varsayılanı (24 sahne × 10s = 240s modülü)
④ REFERANS PAKETİ: YAZILSIN
⑤ HİKÂYE ONAYI (14.09.2026): 00_HIKAYE_ONAYI.md ONAY 20.09.2026 · sahip · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "THE STILL POINT — DURGUN NOKTA: 24 sahne × 10 saniye = 4 dakika. Yatay 16:9. Tek astronot, tamamen opak vizör, diyalogsuz anlatım. Satürn manzaraları, dev bir dönen istasyon ve tek hamlede tamamlanması gereken bir kaçış."
REPLİK: yok
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Dönen halkadan kaçış | Doğrudan atlama teğet hızla savurur | Bakım arabasıyla ters sürüş yaparak teğet hız sıfırlanır | Novum fizik kuralına bağlandı |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 2-4 (4 dk modülü)            → §2.3 kartı
ORTAM:         §3.7 Vakum + Dönen Halka + 0g      → tetiklediği zorunlu satırlar: sert vakum, dönme fiziği, balistik süzülme
TÜR:           bilimkurgu · dal: sert bilimkurgu  → §4.1
KLİP SÜRESİ:   10.0 s
SAHNE SAYISI:  24    RUNTIME: 240.0 s = 24 × 10.0 s
BÖLÜM SAYISI:  2     (Bölüm 1: S00-S11; Bölüm 2: S12-S23)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Dönen halkadan ayrılan cisim teğet hızını korur; merkezdeki hareketsiz kaçış kapsülüne tek itişle ulaşmak için teğet hız ters yönde sürüşle sıfırlanmalıdır.
NOVUM TAŞIYICISI:    <bakım arabası> × <ters yönde sürüş> → <teğet hızın sıfırlanması>
① TEK KARE:          Bakım arabasının hız göstergesi 8 m/s değerindeyken arkadaki dönen kafesin teğetsel akışının durması ve merkez modülün kadrajda kilitlenmesi.
② KİNETİK BAĞIMSIZLIK: ✅ Kural tamamen görsel, replik ve dış ses olmadan kanıtlanıyor.
③ BAŞLIK ŞEMASI:     ✅ The Still Point / Durgun Nokta (≤ 5 kelime)
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — cesaret
▸ tanım cümlesi — Korkunun içinde rasyonel ve doğru hareketi bulmak.
▸ depoda kaç kez kullanıldı — 4 kez
▸ motif kanalları — turuncu anahtar (nesne) / ayak sabitleme ve fırlatma (kinesik) / dönen halka vs sabit merkez (kamera) / Satürn yansımaları (ışık)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| KART 3 (kask/vizör) | EVET | Astronot filmi | Opak siyah vizörle yüz morflaması yapısal olarak önlendi | düşük |
| KART 5 (sayaç) | EVET | Hız göstergesi | Analog kadran ve dış dünya referansı kullanıldı | orta |
| KART 8 (kamera lockoff) | EVET | Sahneler arası açı yayı | Güvenli bant ve kontrollü kamera hareketleri tasarlandı | düşük |
| KART 12 (politika) | EVET | Kasklı uzay giysisi | Teknik endüstriyel astronot kimliği kilitlendi | düşük |
| KART 13 (yapı ölçeği) | EVET | ORISON istasyonu | 1H gövde oranı ve anatomik ölçek kartı tanımlandı | orta |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  Dönen istasyon ile bakım arabasının bağıl yön karmaşası
POZİTİF BİÇİMİ:   Bakım arabası ray üzerinde 8,0 m/s hızla ilerlerken dönen istasyon iç kafesi ters yöne 0,08 rad/s hızla akar; merkezdeki sabit kaçış kapsülü kadraj merkezinde 0 px sapmayla tam sabit kalır.
```

```
TETİKLENEN RİSK:  5 / 13
EŞİK:             5
EŞİĞİN ÜSTÜNDEYSE: Eşikte (5); malzeme azaltmaya gerek yok, kilit tavanı ≤ 20 olarak sınırlandı.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | EVET | Nora EVA giysisi (S00-S23) |
| T2 | biçim kilidi METİNLE tutulmayan varlık | EVET | ORISON döner uzay istasyonu |
| T3 | oranı sözle yazılamayan nesne | EVET | Elektrikli bakım arabası |
| T4 | insan dışı canlı | HAYIR | — |
| T5 | tekrar eden insan dışı olay | EVET | Teğet fırlama ve serbest süzülme |
| T6 | bir varlık tekrar tekrar dönüyor | EVET | Turuncu İngiliz anahtarı ve Nora |

```
KARAR: YAZILIR
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S12
NÖTR TARİFİ:         Nora emniyet kilidini çözer ve bakım arabasını raydan çıkararak sakin ve kontrollü bir itişle boşluğa bırakır.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Kopan geçide rağmen merkezdeki kaçış kapsülüne ulaşmak ve istasyonu tahliye etmek.
ENGEL:   Dönen halkanın ürettiği 8 m/s teğet hızın doğrudan atlamayı ölümcül kılması.
BEDEL:   S12'de tek kaçış ve ulaşım aracı olan bakım arabasını raydan çıkarıp boşluğa bırakmak.
MUHATAP: Dönen ORISON istasyonunun mekanik dönüşü ve uzay boşluğunun eylemsizlik fiziği.
AYRILIK: —
```

---

## ✅ KAPI

```
✅ konsept kapısı ①②③ üçü de tamam
✅ risk sayımı yazıldı ve eşik kararı verildi (5/13)
✅ B5 dörtlüsü tam, BEDEL sahne numarası (S12) taşıyor
```
