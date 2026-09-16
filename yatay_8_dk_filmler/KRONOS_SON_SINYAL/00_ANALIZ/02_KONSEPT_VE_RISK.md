# 🧠 KRONOS_SON_SINYAL — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI

```
① KONU:     sahip verdi (KRONOS: SON SİNYAL)
② FORMAT:   yatay_8_dk_filmler → kart §2.7 · bölüm sayısı 2
③ SAHNE:    48 → RUNTIME: 08:00 (48 sahne × tam 10 saniye)
④ REFERANS PAKETİ: YAZILIR (KRO_REF)
⑤ HİKÂYE ONAYI: `00_HIKAYE_ONAYI.md` ONAY ✅ 15.09.2026 · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ

```
TALEP: "Hasarlı bir yörünge istasyonunda iki astronot, Kestrel’in sekiz dakika ileride göndereceği yardım kaydını bulur; kayıtta Aras’ın kaybolduğu söylenmektedir."
REPLİK: var ("Mayday. Kronos. Aras is gone. Do not open the red hatch. Keep it closed.")
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Vakumda patlamalı kaybolma | İnsan vücudu saniyeler içinde patlamaz | B modülü ayrılır, Aras B'nin içinde kalır ve kaybolur | Fiziksel devamlılık ve gerçek uzay koşulları korunur |

## 2. 🗺️ KARTLAR

```
FORMAT:        yatay 10-20 dk / 8 dk → §2.7 kartı
ORTAM:         Uzay yörünge istasyonu (mikro yerçekimi)
TÜR:           bilimkurgu · dal: uzay dramı
KLİP SÜRESİ:   10 s  (araçtan ölçüldü)
SAHNE SAYISI:  48    RUNTIME: 08:00
BÖLÜM SAYISI:  2
```

## 3. 🧩 ÖNERME VE NOVUM

```
NOVUM:               Deneysel dış röle R, canlı kurtarma ses paketini tam 480 saniye geriye alıcı belleğine düşürür.
NOVUM TAŞIYICISI:    Alıcı ekranı RX × zaman damgası inceleme → 480 saniyelik zaman farkı kanıtı
① TEK KARE:          Alıcı ekranı RX üzerinde RECEIVED 12:00:00 ve SENT 12:08:00 saatlerinin aynı karede görünmesi.
② KİNETİK BAĞIMSIZLIK: ✅ Ekrandaki saat farkı ve zaman damgaları diyalog olmadan okunabilir.
③ BAŞLIK ŞEMASI:     KRONOS: SON SİNYAL ✅
```

## 4. 🎭 TEMA

```
▸ tema adayı — ZAMAN
▸ tanım cümlesi — Geleceğe dair bilgi, bir insanın başka bir insan için karar verme sorumluluğunu ortadan kaldırmaz.
▸ depoda kaç kez kullanıldı — 5
▸ motif kanalları — alıcı saati · vizör yansıması · kırmızı kapak
```

## 5. ⚠️ RİSK KARTLARI

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| Kask Vizör Morphing | Evet | İki kasklı astronot | Vizör ve kask içi aydınlatma kilitlendi | Yok |
| Mikro Yerçekimi Momentum | Evet | Süzülen halat ve bedenler | Doğrusal momentum kuralı eklendi | Düşük |
| Basınç Patlaması Abartı | Evet | Kapak açılması ve modül ayrılması | Mekanik piroteknik ayırma tarif edildi | Yok |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR

```
1 NUMARALI RİSK:  MİKRO_YERÇEKİMİ_MOMENTUM
POZİTİF BİÇİMİ:   Tüm serbest nesneler ve halat kadrajda en az 2 saniye kesintisiz doğrusal süzülme hareketi yapacaktır.
```

```
TETİKLENEN RİSK:  3 / 12
EŞİK:             5
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | Evet | Kestrel & Aras basınç giysileri |
| T2 | biçim kilidi METİNLE tutulmayan varlık | Evet | Kronos istasyon modülleri A ve B |
| T3 | oranı sözle yazılamayan nesne | Evet | Kırmızı kapak H-R ve alıcı RX |
| T4 | insan dışı canlı | Hayır | — |
| T5 | tekrar eden insan dışı olay | Hayır | — |
| T6 | bir varlık tekrar tekrar dönüyor | Evet | Kronos istasyonu dış görünümü |

```
KARAR: YAZILIR (KRO_REF)
```

## 6. 🛡️ POLİTİKA SATIRI

```
EN RED-RİSKLİ KARE:  S42
NÖTR TARİFİ:         İki modül arasındaki piroteknik kilitlerin ayrılması ve B modülünün uzay boşluğuna süzülmesi.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI

```
İSTEK:   Kestrel ve Aras'ın ikisini de hayatta tutmak; B ayrılırken A'yı yaşanabilir bırakmak.
ENGEL:   Gelecekten gelen kaydın korkusu; bozulmuş kumanda hattı; B dış gövde kaçağı.
BEDEL:   Kestrel'in Aras geri dönemeden B modülünü ayırması; Aras'ın kaybolması · S41-S43
MUHATAP: İkinci insan (Kestrel ve Aras birbirlerinin kararlarını değiştirir).
AYRILIK: S26 (Aras'ın B modülüne geçişi), S42 (Fiziksel modül ayrılması).
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı ve eşik kararı verildi
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor
→ 03_SAHNE_SIRALAMASI.md yazılabilir.
```
