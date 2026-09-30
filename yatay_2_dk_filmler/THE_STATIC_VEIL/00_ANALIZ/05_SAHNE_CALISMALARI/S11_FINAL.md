# 🔬 S11 — KİLİT SAHNE · FINAL · SAHNE ÇALIŞMASI · THE_STATIC_VEIL

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
SAHNE:      S11            BAŞLIK: Fenerle Dönüş
BÖLÜM:      THE_STATIC_VEIL_BOLUM_2.md
ZAMAN:      110.0 s → 120.0 s     ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      Kapanış / Tamamlama   B5 SATIRI: MUHATAP
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Monte edilen optik fener güçlü amber ışığıyla krater zeminini aydınlatırken, kask göstergeleri tamamen sönmüş astronot derin gölgeye doğru yavaş adımlarla yürüyerek uzaklaşır.
BAŞTA:           Fener yeni kilitlenmiş, zemin karanlık.
SONDA:           Fener sabit geniş amber konisiyle krater yamacını aydınlatıyor; astronot kadrajın derinliklerinde kararmış silüetiyle karanlığa karışıyor.
⛔ KLİP İÇİ DEĞİŞİM: YOK (fenerin yanışı ve uzaklaşma yürüyüşü kesintisiz sürdürülür)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: dönüş S0 (tam kafiye)

LENS:           24mm     MESAFE: 12.0 m     YÜKSEKLİK: 0.4 m
ÖLÇEK:          EWS      AÇI TİPİ: Düşük Açı (zemin hizası)
KADRAJ ENİ:     16.0 m   ⛔ HESAPLANDI (§5.2) — pilon, fener ışık konisi ve yürüyen figür 12.0 m
                          Sığıyor mu: evet
ANA NESNE PİKSEL: 240 px (pilon ve astronot)   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S10(ECU, detay üst açı) → S11(EWS, düşük açı): ölçek 4 kademe · azimut 75° → bant içi: ✅ (bilinçli final şoku ve rahatlama)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (her karede aynı)
AYRIM EKSENİ:   beyaz kompozit giysi arkadan silüet, yanan amber optik fener
GİREN NESNE:    yok
ÇIKAN NESNE:    astronot kadraj derinliğinde karanlığa uzaklaşır
TAŞINAN NESNE:  yanan optik fener (S00'da sönüktü, burada yanıyor — kafiye tek değişkeni)
⛔ BİÇİM KİLİDİ: Referans paketi sayfa R1 ve R2
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Optik fenerin sıcak amber ışık demeti krater zeminini teğet aydınlatır; astronotun kask ve göğüs göstergeleri zifiri kapalı
PALET:     Sıcak amber fener ışığı, zifiri siyah derin gölge, mat gri regolit zemini
SES:       Giderek uzaklaşan ve azalan boğuk bot adımı titreşimleri → mutlak nihai sessizlik
MÜZİK:     yok (sessizliğin onurlu ağırlığı)
FİZİK:     0.16g Ay kütleçekimi: yavaş ve kararlı adımlar; fener ışığı vakumda saçılmadan keskin bir koni oluşturur
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       arkadan çekim (kask göstergeleri tamamen sönük, kapkaranlık kask ensesi)
HAREKET:   yanan fenerin altında astronotun kararmış göstergelerle yalnız ve kararlı yürüyüşü (görev tamamlandı ama bedel ödendi)
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D210 | S0 kafiye çifti lockoff tripod | The exact same position, height and 24mm lens as Scene 0; only difference is the lit beacon |
| D211 | S11 final vuruşu ve çıkış | The beacon shines bright amber into the crater; mission resolved at personal cost |
| D139 | Arkadan çekimde düz sırt kuralı | The back of the suit is one continuous smooth panel from collar to hip, carrying nothing |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | D139 kamera arkada boş sırt | Pozitif düz sırt cümlesi eklendi | ✅ |
| 2 | ⚠️ | D193 ışık takvimi | Kask ekranları ve LED'ler tamamen kapalı tutuldu | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  Astronotun yanan fenerin yanından krater yamacına doğru yürümesi
POZİTİF KİLİT: The astronaut walks slowly away from the glowing beacon into the crater shadow
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px (240px)
✅ önceki sahneyle ardışık çift bant içi (4 kademe, 75° azimut, gerekçelendirildi)
✅ kurulum harfi + işaret satırı yazıldı (A · dönüş S0 tam kafiye)
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ olduğu için THE_STATIC_VEIL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
