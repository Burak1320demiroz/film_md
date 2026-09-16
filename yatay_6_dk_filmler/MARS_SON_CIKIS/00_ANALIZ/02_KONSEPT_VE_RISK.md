# 🧠 MARS_SON_CIKIS — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi — Mars yaşam alanından tahliye ve yörüngedeki ana gemiye manuel kenetlenme gerilimi
② FORMAT:   yatay 6dk → kart §2.6 · bölüm sayısı 3
③ SAHNE:    36 sahne → 3 bölüm × 12 sahne × 10 saniye = 360 saniye
④ REFERANS PAKETİ: YAZILIR — Kask, vizör, donanım ve Kestrel/Horizon araçları kilitlenecek.
⑤ HİKÂYE ONAYI: `00_HIKAYE_ONAYI.md` ONAY ✅ 15.09.2026 · sahip · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "yatay 6 dk filmler için bir film yapalım 3 bölüm her bölüm 12 sahne ve her sahne 10 saniye. Mars'ta geçen aksiyonlu ilk bölüm, sorunlar çıkıp acil tahliye edilen 2. bölüm ve yörüngedeki yıldızlararası ana gemiye kenetlenilen 3. bölüm."
REPLİK: var — Telsiz ve kokpit içi aksiyon diyalogları (İngilizce).
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Mars'ta büyük patlama / yangın | Low-density Mars atmosferinde patlama ateşi dalgası olmaz | Servis kabininde elektrik arızası, ark parlaması ve yoğun siyah duman | Mars atmosferik basıncına ve güvenli içerik politikasına uygun tarif |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 6dk → §2.6 kartı
ORTAM:         Mars Yüzeyi (Habitat) + Mars Yörüngesi (Uzay)
TÜR:           bilimkurgu · dal: fiziksel hayatta kalma gerilimi
KLİP SÜRESİ:   10,000 s
SAHNE SAYISI:  36    RUNTIME: 360 s = 36 × 10 s
BÖLÜM SAYISI:  3     (Bölüm 1: 1-12, Bölüm 2: 13-24, Bölüm 3: 25-36)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Otomatik navigasyon kaybında iki kişinin optik hizalama ve manuel itici kontrolüyle bağıl kenetlenmeyi tamamlaması.
NOVUM TAŞIYICISI:    Kestrel kenetlenme halkası × manuel itici füzyonu → bağıl hız sönümleme
① TEK KARE:          Kestrel kenetlenme halkasının Horizon port kılavuz pimlerine 1,5 metre kala 0.15 m/s bağıl hızla yaklaşması ve S29'da teması
② KİNETİK BAĞIMSIZLIK: ✅ Görsel olarak hız azalması, hizada hizalanma ve mekanik kilitlerin oturması diyalogsuz okunur.
③ BAŞLIK ŞEMASI:     MARS: SON ÇIKIŞ — LAST EXIT
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — Tamamlayıcı Eylem ve Güven
▸ tanım cümlesi — Güven, birinin bütün işi tek başına yapması değil, iki kişinin birbirinin eksik kaldığı fiziksel hareketi tamamlamasıdır.
▸ depoda kaç kez kullanıldı — 1 (bu film)
▸ motif kanalları — kasa frenleme pimi · yaralı sol kol askısı · manuel kenetlenme leveri
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mv | kalan risk |
|---|:--:|---|---|:--:|
| R1: Kask / Vizör | Evet | İki astronot kasklı | Yarı saydam vizör ve iç kask ışığı kondu | Düşük |
| R2: Dar İç Mekân | Evet | Habitat servis kabini ve Kestrel kokpiti | 28mm/35mm lens sınırı kondu | Düşük |
| R3: Uzay Yanaşması | Evet | Kestrel - Horizon kenetlenmesi | Görsel çapa omurga ve port haritası kondu | Orta |
| R4: Kol Yaralanması | Evet | Aras S14'te kolundan sakatlanır | Sol kol askı kayışına sabitlendi | Düşük |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192]

```
1 NUMARALI RİSK:  Manuel Kenetlenme Yaklaşma Hızı ve Eksen Sapması
POZİTİF BİÇİMİ:   S26'da 7,5 metre mesafe; S28'de 1,5 metre mesafede 0,15 m/sn bağıl hız; S29'da fiziki temas (1,5m->0m); S31'de 3 mekanik mandal kilitlenmesi.
```

```
TETİKLENEN RİSK:  4 / 12
EŞİK:             5
EŞİĞİN ALTINDA:   Kilit tavanı ≤ 20 uygulanabilir.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | Evet | Lena & Aras astronot giysileri |
| T2 | biçim kilidi METİNLE tutulmayan varlık | Evet | Kestrel fırlatma aracı (~18m) |
| T3 | oranı sözle yazılamayan nesne | Evet | Horizon ana gemisi (~540m) |
| T4 | insan dışı canlı | Hayır | — |
| T5 | tekrar eden insan dışı olay | Hayır | — |
| T6 | bir varlık tekrar tekrar dönüyor | Evet | Kestrel & Horizon |

```
KARAR: YAZILIR — KAPI 0 gereği MARS_SON_CIKIS_REFERANS_PAKETI.md hazırlanacak.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S10 (Servis kabininde elektrik yangını)
NÖTR TARİFİ:         Koyu mat gri paneller arkasında turuncu elektrik ark parlamaları ve havalandırma Izgarasından çıkan yoğun siyah duman yükselişi.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI

```
İSTEK:   Mars habitatını yaklaşan Güneş parçacık fırtınasına hazırlamak ve numune toplamak.
ENGEL:   Servis kabinindeki elektrik arızasının sığınak hava sistemini yakması ve otomatik yakınlaşma navigasyonunun bozulması.
BEDEL:   Aras'ın sol kolunun S13/S14 yangın kapısında ezilmesi ve S14-S36 boyunca askıda kalması (Kapatılamaz Bedel), Mars habitatı ve fiziksel numunelerin S15'te terk edilmesi.
MUHATAP: İkinci insan (Lena & Aras ortaklığı).
AYRILIK: S14 (Yangın kapağı inerken Aras'ın kurtarılması anı).
```

---

## ✅ KAPI

```
✅ konsept kapısı ①②③ üçü de tam
✅ risk sayımı (4/12) yazıldı ve kilit tavanı doğrulandı
✅ B5 dörtlüsü tam, BEDEL sahne numarası (S14, S16) taşıyor
→ 03_SAHNE_SIRALAMASI.md yazılabilir.
```
