# 🔬 S08 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_STATIC_VEIL

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
SAHNE:      S08            BAŞLIK: Kasktan Söküm
BÖLÜM:      THE_STATIC_VEIL_BOLUM_2.md
ZAMAN:      80.0 s → 90.0 s       ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      Bilinçli Karar        B5 SATIRI: BEDEL
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Zayıf arkın yetersiz kaldığını gören astronot, kaskın harici batarya modülüne uzanır; tereddütle duraksadıktan sonra bataryayı klipsinden çözer.
BAŞTA:           Kask bataryası göğüs harness kayışına kilitli, yeşil güç gösterge LED'i yanıyor.
SONDA:           Batarya modülü eldiven içinde serbest, kask göstergelerine giden spiral kablo gergin.
⛔ KLİP İÇİ DEĞİŞİM: YOK (karar ve sökme tek akıcı süreç olarak sürdürülür)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  C        İŞARET: KÜME 2 (dönüş S07)

LENS:           85mm     MESAFE: 1.2 m     YÜKSEKLİK: 1.7 m
ÖLÇEK:          CU       AÇI TİPİ: Hafif Üst Açı
KADRAJ ENİ:     0.9 m    ⛔ HESAPLANDI (§5.2) — kask ve batarya bloğu 0.6 m
                          Sığıyor mu: evet
ANA NESNE PİKSEL: 720 px   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: KÜME 2 bölünmüş tek çekim devam klibi (S07 ile aynı kamera) → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (her karede aynı)
AYRIM EKSENİ:   beyaz sert kompozit, matlaşmış gri kask vizörü, siyah dikdörtgen batarya modülü
GİREN NESNE:    astronotun sağ eldiveni göğüs hizasına yükselir
ÇIKAN NESNE:    yok
TAŞINAN NESNE:  sökülen batarya modülü → S09'da pilon şasesine vurulacak
⛔ BİÇİM KİLİDİ: Referans paketi sayfa R1 (Batarya ve göğüs bağlantısı)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Pilon kenarından gelen dolaylı sert yansıma + göğüs panelindeki son yeşil LED parıltısı
PALET:     Mat gri vizör, soluk yeşil LED noktası, siyah batarya gövdesi, beyaz kompozit
SES:       Kask içi hızlı ve gergin nefes alışverişi + mekanik klipsin metalik klik sesi
MÜZİK:     yok
FİZİK:     0.16g Ay kütleçekimi: el hareketinde mikro-tereddüt, batarya ağırlıksız gibi ama kütle eylemsizliğiyle taşınır
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       matlaşmış kask camı arkasında kafa eğimiyle beliren tereddüt ve çaresizlik ifadesi
HAREKET:   eldivenin batarya klipsi üzerinde 1 saniye titreyip duraksaması, ardından kararlılıkla çekip çıkarması
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D202 | Karakterin seçimi bedende okunmalı | The astronaut hesitates with trembling gloved hand on the battery latch before pulling it free |
| D206 | Bedel kararı bedende hissedilmeli | Deliberate posture of sacrifice; tense shoulders, heavy breathing inside helmet |
| D175 | Eldiven kalın kompozittir | Heavy insulated pressure glove grasps the small rectangular battery module |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | D202 seçim bedende görünmeli | Tereddütlü duraksama ve kararlı söküş kinesik olarak yazıldı | ✅ |
| 2 | ⚠️ | D123 asla yasak fiil kullanılmaz | Pozitif eylem ve tutuş cümleleriyle tarif edildi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  Kask harici bataryasının mekanik klipsten sökülmesi
POZİTİF KİLİT: A heavy pressurized space glove unlatches a small black battery pack from the chest harness
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px (560px)
✅ önceki sahneyle ardışık çift bant içi (2 kademe, 45° azimut)
✅ kurulum harfi + işaret satırı yazıldı (A · dönüş S4)
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ olduğu için THE_STATIC_VEIL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
