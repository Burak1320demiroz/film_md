# 🧠 THE_SHADOW_LINE — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     GÖLGE ÇİZGİSİ / THE SHADOW LINE (uzay istasyonunda hareket eden ölümcül Güneş gölge hattı ve hayatta kalma) [sahip onayladı]
            GEREKÇE: depoda FEDAKÂRLIK teması ve Güneş istasyonu dış yüzey hayatta kalma novum'u ile aksi dramaturji eksikliği.
② FORMAT:   yatay_2_dk_filmler → kart §2.2 · bölüm sayısı 2
③ SAHNE:    13 (S00-S12) → 13 × 10 sn = 130 saniye
            Gerekçe [D74]: S00 Hook sahnesi eklendi, toplam dramaturjik döngüyü tam oturması için 13 sahneye çıkarıldı.
④ REFERANS PAKETI: YAZILSIN
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "GÖLGEYE SIĞIN (The Solar Ignition / The Shadow Line) aksiyonlu 2 dakikalık uzay hayatta kalma filmi."
REPLİK: yok (kinesik anlatım, kask içi nefes ve mekanik sesler)
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Plazma patlamasında yangın dumanı çıkması | Uzay vakumunda oksijen ve duman süzülmesi olamaz | Güneş radyasyonu metal yüzeyde turuncu akkor parlama ve termal gaz çıkışı üretir | Uzay fiziği kuralı D200 |
| Eldivenle vizör silme | Vakumda kask dışı buğulanmaz, eldiven sert altın vizörü çizemez | Mühendis elini şakağına götürüp kask içi iletişim/valf düğmesine basarak kask içi havalandırmayı çalıştırır | Fiziksel doğruluk ve mantık kuralı |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay_2_dk_filmler → §2.2 kartı
ORTAM:         Uzay / Güneş İstasyonu Dış Yüzeyi (§3.1 Uzay Vakum Kartı)
TÜR:           bilimkurgu · dal: uzayda hayatta kalma / zamana karşı yarış
KLİP SÜRESİ:   10 s (her sahne 10 saniye)
SAHNE SAYISI:  13 (S00-S12) RUNTIME: 130 saniye
BÖLÜM SAYISI:  2 (BOLUM_1: S00-S06, BOLUM_2: S07-S12)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Güneş plazma ışığı temas ettiği her esnek malzemeyi saniyeler içinde yok eder; gölge hattı kaydıkça sığınacak alan daralır.
NOVUM TAŞIYICISI:    Astronot esnek giysi eklemleri × Güneş plazma bıçağı → termal erime ve yanık
① TEK KARE:          Kadrajı çaprazlamasına kesen bıçak gibi keskin turuncu plazma ışığı ile zifiri siyah gölge sınırı (S00).
② KİNETİK BAĞIMSIZLIK: Replik olmadan, eldivenin ışığa temasıyla yükselen termal buhar ve mühendisin gölgeye panikle kaçışı ile novum doğrudan gösterilir.
③ BAŞLIK ŞEMASI:     THE SHADOW LINE (3 kelime)
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — FEDAKÂRLIK
▸ tanım cümlesi — İnsanın hayatta kalmak ve sistemi kurtarmak için kendi bedeninden bilinçli olarak vazgeçmesi.
▸ depoda kaç kez kullanıldı — 4 kez
▸ motif kanalları — parmak kilitlenmesi (kinesik) · altın vizör yansıması (ışık) · manuel soğutma mandalı (nesne)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| R1 (Uzay Giysisi) | ✅ | Astronot sürekli kadrajda | ✅ Referans paketi ve visual seed ile sabitlendi | Düşük |
| R2 (Güneş Işığı) | ✅ | Blinding plazma kontrastı | ✅ Promptta ışık vektörü ve gölge hattı sayıyla yazıldı | Orta |
| R3 (Mekanik Mandal) | ✅ | Soğutma valfi emniyet mandalı | ✅ Toggle latch biçimi net tanımlandı | Düşük |
| R4 (El Yanığı) | ✅ | Eldiven parmaklarının kavrulması | ✅ Alev değil termal kararma ve duman olarak tarif edildi | Düşük |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  Güneş Plazma Işığı Gölge Hattı Kontrastı ve Açısı
POZİTİF BİÇİMİ:   Kadrajı 45 derece açıyla sol-alttan sağ-üstem kesen, 0.5 saniyede 10 cm sağa kayan bıçak keskinliğinde turuncu-siyah gölge sınırı.
```

```
TETİKLENEN RİSK:  4 / 4
EŞİK:             5
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — yalnız soru ④ "analiz karar versin" ise

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | Mühendis astronot uzay giysisi (S00-S12) |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | Soğutma valfi ve emniyet mandalı (S09-S11) |
| T3 | oranı sözle yazılamayan nesne | — | |
| T4 | insan dışı canlı | — | |
| T5 | tekrar eden insan dışı olay | ✅ | Gölgeli hat kayması (S00, S06) |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | Astronot ve istasyon gövdesi |

```
KARAR: YAZILIR (THE_SHADOW_LINE_REFERANS_PAKETI.md)
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S10 (Mühendisin elini plazma ışığına uzatarak emniyet mandalını kaldırdığı kare)
NÖTR TARİFİ:         "Heavy pressurized space glove fingers exposed to intense orange light beam, thermal vapor rises from carbon fiber joint seams"
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   İstasyon soğutma sistemini manuel olarak devreye sokup erimeyi durdurmak.
ENGEL:   Soğutma valfinin emniyet mandalı direkt Güneş plazma ışığı altında sıkışmış durumdadır.
BEDEL:   Mühendis elini bilinçli olarak ölümcül plazma ışığına uzatır; eldiven eklemleri erir ve parmakları yumruk şeklinde kilitlenir (S10).
MUHATAP: Kendi bedeni ve istasyonun soğutma mekanizması.
AYRILIK: S10 (Mühendisin kendi eline bakıp acı dolu kararı aldığı an).
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı ve eşik kararı verildi
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S10)
→ üçü de ✅ ise 03_SAHNE_SIRALAMASI.md yazılabilir
```
