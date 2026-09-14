# 🧪 THE_CRACKED_HELMET — KONSEPT VE RİSK ANALİZİ

> **Girdi:** `01_QA_DERS_HASADI.md` kilitleri + `KILAVUZ_REHBERI.md` format/ortam/tür kartları.
> **Çıktı:** Konsept doğrulaması, Novum testi, B5 dramaturji zinciri ve Risk haritası.

---

## 1. 📐 FORMAT VE ORTAM PARAMETRELERİ

```
FİLM ADI:       THE_CRACKED_HELMET
FORMAT:         Yatay 2-4 dk (16:9) · yatay_2_dk_filmler
TÜR:            Bilimkurgu (Uzay / Yabancı Gezegen Yüzeyi)
ORTAM KARTI:    §3.2 İnce Atmosfer / Gezegen Vakumu (Ders 39, 41)
KLİP SÜRESİ:    10.0 saniye (Veo native araç ölçümü [D124])
SAHNE SAYISI:   12 Sahne (S00 - S11)
TOPLAM SÜRE:    120.0 saniye (02:00)
BÖLÜM BÖLÜMÜ:   BOLUM_1: S00 - S05 (6 sahne) · BOLUM_2: S06 - S11 (6 sahne)
```

---

## 2. 🚦 KONSEPT KABUL KAPISI (ÜÇ TEST)

| Test | Durum | Gerekçe / İfade |
|---|:--:|---|
| **① TEK KARE** | ✅ PASSED | Film tek bir görsel imajla özetlenebilir: *"Astronotun kırık kask vizöründeki sızdıran kılcal çatlak ve üzerine sürülen amber rengi polimerleşen mineral reçinesi."* |
| **② KİNETİK BAĞIMSIZLIK** | ✅ PASSED | Görsel ve hareket arka plan mekanı olmadan da çalışır: Kaskın içinden dışarı fışkıran gaz buharı ve dijital basınç sayacının düşüşü hareketin kendisidir. |
| **③ BAŞLIK ŞEMASI** | ✅ PASSED | `THE_CRACKED_HELMET` şemaya uygundur (İngilizce, BUYUK_HARF_ALT_CIZGI, 2-3 kelime). |

---

## 3. 🧪 NOVUM VE TEMA MÜHENDİSLİĞİ

```
TEMA:              YALNIZLIK VE İRADENİN DİRENCİ (Tek insan novumu)
NOVUM TİPİ:        Fiziksel Yasa / Malzeme Reaksiyonu
NOVUM TANIMI:      Gezegendeki obsidyen mineral damarlarından elde edilen kristalize reçinenin, vakum ortamında basınç farkıyla anında polimerleşerek vizör ile metal kask birleşim noktasında sızdırmazlık sağlaması.
TAŞIYICI SATIRI:   [NOVUM TAŞIYICISI: Astronotun sağ elinde tuttuğu obsidyen reçine çubuğu ve vizör çatlağında anında katılaşan amber tüpü]
```

### Novum Üç Kabul Testi
1. **Ekran Sadakati:** Reçinenin kılcal çatlağa sürüldüğü an kabarcıklanıp saydam amber şeridine dönüşmesi ekranda fiziksel olarak görülür.
2. **Dünya Bağımsızlığı:** Dünya atmosferinde gerçekleşmeyen, vakum ve ince atmosfer basıncına özgü bir malzeme kuralıdır.
3. **Bedel Karşılığı:** Reçineyi çıkarmak ve doğru açıyla sürmek dondurucu ortamda ağır bedel ve titreyen eller gerektirir.

---

## 4. 🎭 B5 DRAMATURJİ DÖRTLÜSÜ (HİKÂYE HATTI KİLİDİ)

> `06_HIKAYE_HATTI_TESHISI.md` uyarısı: İSTEK bir "anlamak/görmek" değil, somut bir İŞTİR. ASIL KAPI BEDEL'DİR.

```
1. İSTEK:     Kırılan vizördeki hava sızıntısını durdurmak, oksijen kaybını sabitlemek ve kaçış modülüne ulaşana kadar canlı kalmak.
2. ENGEL:     Sürekli düşen kask içi basıncı (04:12 -> 00:30 bar uyarısı) ve dondurucu vakumun reçineleşme süresini daraltması.
3. BEDEL:     [SAHNE 08/09] Astronotun titreyen ve donan parmaklarıyla kask vizöründeki gaz sızıntısına karşı kızgın reçine çubuğunu sürerken oksijen yutkunması ve vizörün buğulanması.
4. MUHATAP:   Çakılan kaçış modülünün sönmüş motor enkazı ve sarp mor obsidyen kayalığı.
```

---

## 5. 🛡️ POLİTİKA SATIRI VE RİSK KARTLARI (B6 / KART 12)

```
POLİTİKA SATIRI (B6): [Nötr vizör basınç göstergesi tarifi, gaz buharı jet spreyi tarifi, fiziksel kan/patlama kelimeleri YOKTUR]
RİSK KARTLARI:        KART 12 (Kısıtlanmış solunum / kask hasarı / ağır efor)
RISK TEDBİRİ:         Vizör hasarı kan veya bedensel yaralanma olarak değil; cam yüzeyindeki ince örümcek ağı kılcal çizgileri ve dışarı çıkan beyaz buhar spreyi olarak pozitif formda prompta yazılır.
```
