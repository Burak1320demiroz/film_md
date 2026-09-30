# 🔬 S09 — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · THE_STATIC_VEIL

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
SAHNE:      S09            BAŞLIK: Kıvılcım ve Bedel
BÖLÜM:      THE_STATIC_VEIL_BOLUM_2.md
ZAMAN:      90.0 s → 100.0 s      ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      Bedel (Doruk)         B5 SATIRI: BEDEL
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Astronot kask bataryasını çelik pilon şasesine çarpar; anlık parlayan beyaz-mavi elektrik arkı elektrostatik tozu vizörden savurur, kask göstergeleri ve göğüs LED'leri tamamen söner.
BAŞTA:           Kask vizörü %80 matlaşmış, göğüs LED'leri zayıf yanıyor, eldiven bataryayı kavramış.
SONDA:           Şiddetli mikro-ark parlamış, vizörün önünde 2 cm'lik temiz görüş deliği açılmış, tüm kask ve giysi göstergeleri kalıcı olarak sönmüş.
⛔ KLİP İÇİ DEĞİŞİM: YOK (darbe, ark parlaması ve sönüş tek dinamik vuruş zincirinde tamamlanır)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  D        İŞARET: dönüş S6

LENS:           50mm     MESAFE: 2.0 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          MCU      AÇI TİPİ: Göz Hizası (yandan)
KADRAJ ENİ:     1.8 m    ⛔ HESAPLANDI (§5.2) — astronot, pilon ve batarya 1.2 m
                          Sığıyor mu: evet
ANA NESNE PİKSEL: 540 px   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S08(CU, üst açı) → S09(MCU, göz yandan): ölçek 1 kademe · azimut 45° → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (her karede aynı)
AYRIM EKSENİ:   beyaz kompozit giysi, çelik pilon, anlık beyaz-mavi ark
GİREN NESNE:    batarya şaseye çarpar
ÇIKAN NESNE:    savrulan gri toz partikülleri
TAŞINAN NESNE:  vizörde açılan küçük temiz görüş alanı → S10'da fener montajında kullanılacak
⛔ BİÇİM KİLİDİ: Referans paketi sayfa R1 ve R2
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      0.3 saniyelik şiddetli beyaz-mavi elektriksel ark parlaması, ardından zifiri gölgeye geri dönüş (LED'ler sönük)
PALET:     Göz alıcı beyaz-mavi elektriksel parlama, mat gri regolit, zifiri siyah derin uzay
SES:       Sert metalik çarpma darbesi + kask içinde elektronik kapanış bipi ve ani ölümcül sessizlik
MÜZİK:     yok (doruğun saf sessizliği ve mekanik şoku)
FİZİK:     Vakumda yangın ve duman yoktur; elektriksel deşarj anında dağılır, serbest kalan tozlar radyal fırlar
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       anlık çakan parlak elektriksel ark ışığının altın vizörde ve kask çemberinde parlayışı, ardından tüm göstergelerin kararması
HAREKET:   bataryanın pilona sertçe vurulması, radyal toz fırlaması ve astronotun omuzlarının çaresizce geriye düşmesi
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D192 | 1 numaralı risk süresi sayıyla | Brief white-blue electrical discharge lasting under 0.3 seconds |
| D206 | Bedel bedende okunmalı | The status indicators on the chest pack go completely dark; the astronaut slumps back slightly in silence |
| D213 | Aksiyon kadraj içi temasta | The contact of the battery against the steel pylon occurs dead-center in the frame |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | PB S9 patlama/yangın yasağı | Yangın, alev ve duman engellendi; 0.3s beyaz-mavi nötr ark olarak tarif edildi | ✅ |
| 2 | ⚠️ | D193 ışık takvimi | S9'da sönen kask ekranları ve LED'ler S10 ve S11'de kesinlikle kapalı kalacak | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   evet   sınıf: PB (Patlama/Bomba riski önleme)
NÖTR TARİF:  A heavy pressurized space glove strikes a small rectangular battery module against a steel pylon bracket, producing a brief white-blue electrical discharge under 0.3 seconds that clears fine grey powder from the visor before all suit status lights go dark.
POZİTİF KİLİT: Brief electrical arc under 0.3 seconds, no smoke, no fire, indicators turn dark
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px (420px)
✅ önceki sahneyle ardışık çift bant içi (2 kademe, 60° azimut)
✅ kurulum harfi + işaret satırı yazıldı (D · dönüş S6)
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı (nötr PB tarifi hazır)
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ olduğu için THE_STATIC_VEIL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
