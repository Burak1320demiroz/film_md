# 🧾 THE_CRACKED_HELMET — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| DERS 7 | Ardışık sahnelerde kamera açısı ve ölçek tekrarı | Ardışık iki sahnede en az 1 kademe ölçek farkı ve ≥45° açı farkı kilitlenecek | S00-S11 tamamı |
| DERS 37/57 | Kask/maske kinesik ve vizör belirsizliği | Vizör durum beklentisi şeride yazılacak, el teması vekilliği S04 ve S08'de uygulanacak | S04, S08 |
| DERS 45 | Promptların self-contained olmaması / Bible atfı | Tüm promptlar self-contained yazılacak, "BIBLE'a bak" veya `[DERS n]` etiketi taşımayacak | S00-S11 promptları |
| DERS 124 | Izgaranın tahmini yazılması | Klip süresi Veo native araç ölçümünden (~10 sn) ızgaraya düşürülecek | PLAN, SPEC |
| DERS 146 | Biçim kilidinin metinle tutulamaması | Kask vizörü çatlağı ve basınç giysisi referans paketi ile görsel kilitlenecek | REFERANS_PAKETI, S00-S11 |
| DERS 176 | Çift zemin tarifi çelişkisi | Aynı prompt içinde zeminin dokusu (obsidyen minerali) tek net cümleyle tarif edilecek | S00, S02, S05, S07 |
| DERS 179 | I2V start frame bedel zamanlaması | Kask çatlağı t=0 anından itibaren vizör üzerinde sabit kılcal geometrik hat olarak kilitlenecektir | S00-S11 start frames |
| DERS 180 | Mutlak sessizliğin metinle istenmesi | Sessizlik metin yerine ses yatağında telsiz statiği ve valf tıslaması ile kurulacak | S00, S03, S10, S11 |
| DERS 192 | Doruğun boşalması riski | Sahne 09 doruğunda polimerleşen reçine reaksiyonu ve basınç sabitlemesi görünür kilitlenecek | S08, S09 |
| DERS 193 | Monotonik ışık takvimi ölçümsüzlüğü | Işık değişimi (mor zemin mineral ışıması vs tek yönlü güneş) sahne haritasında belirginleşecek | S01-S11 |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_MIRROR_FAUNA` | T9 KADRAJ | Kamera yaklaşmasında öznenin kadraj dışına taşması | Kamera hareketleri 35mm anamorfik lens ölçeğinde kadraj payı ≥%25 kilitlenerek yazılacak |
| `THE_FROST_LINE` | T1 KARE | İnce atmosferde vizör yansımasında ikinci ışık kaynağı oluşması | Işık kaynağı tek yönlü güneş ve ikincil zemin ışıması olarak ayrıştırılacak |
| `THE_OPEN_CIRCUIT` | T4 HİKAYE | Bedelin fiziksel olarak bedende ve eylemde ödenmemesi | Kask sızıntısıyla düşen oksijen sayacı ve titreyen parmaklar bedeli fiziksel taşıyacak |
| `THE_SINKING_STAKE` | T2 DEVAMLILIK | Donanım cepleri ve göğüs paneli sayısının sahneler arası kayması | Göğüs kontrol paneli tek tip dikdörtgen modül ve 3 kontrol ışığıyla kilitlenecek |
| `THE_KEPT_LIGHT` | T8 EFOR | Ekipman tamir eyleminin hareketsiz kalması ve motorun eylemi üretmemesi | Tamir eylemi "iki elin reçine modülünü kılcal çatlağa hizalayıp sıkması" olarak pozitif aksiyon yazılacak |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika Kelime) | Kask kırılması / cam patlaması / yaralanma ifadeleri | Kask vizöründe kılcal hava sızıntı hattı ve jet buhar gazı tarif edilecek | S00, S01 (Kask hasarı) |
| YR (Yapısal Red) | Kısıtlanan solunum / boğulma tasvirleri | Basınç modülü uyarısı ve düşen dijital gösterge sayısı tarif edilecek | S03, S04 (Oksijen düşüşü) |
| TK (Tehlike Çerçevesi) | Aşırı panik ve bedensel çırpınma | Karakterin soğukkanlı ve metodik eforu, stabil el hareketleri kullanılacak | S08, S09 (Tamir anı) |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        10 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   DERS 179 (I2V t=0 Bedel Kilit) · DERS 176 (Çift Zemin Çelişkisi) · KART 12 (Kask Sızıntısı Red Riski)
```
