# 🔬 S<NN> — SAHNE ÇALIŞMASI · MARS_SON_CIKIS

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> sahneye düşen satırları. Bu dosya bitmeden bu sahnenin promptu yazılmaz.

---

## 🪪 KİMLİK

```
SAHNE:      S<NN>            BAŞLIK: ⬜
BÖLÜM:      MARS_SON_CIKIS_BOLUM_⬜.md
ZAMAN:      ⬜ s → ⬜ s       ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      ⬜               B5 SATIRI: ⬜ [İSTEK/ENGEL/BEDEL/MUHATAP/AYRILIK]
⭐VİRAL:    ⬜ [evet/hayır]  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY VE 10 SANİYE EYLEM AKIŞI — hareketin zamana yayılımı

```
OLAY:            ⬜ (tek cümle, ne değişiyor)
BAŞTA:           ⬜ (0. saniyede durum)
SONDA:           ⬜ (10. saniyede durum)

⛔ 10 SANİYE EYLEM AKIŞI (EYLEM TABANLI ZAMANLAMA):
   0-3 s (Giriş/Başlangıç):  ⬜ (Örn: El kayışı tutar...)
   3-7 s (Gelişme/Aksiyon): ⬜ (Örn: Klips yuvaya oturur ve kilitlenir...)
   7-10 s (Sonuç/Geçiş):     ⬜ (Örn: Gövde sarsılır, yeni aksiyona hazırlanır...)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  ⬜        İŞARET: ⬜ [ilk kullanım / dönüş S⬜ / küme S⬜]
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           ⬜ mm     MESAFE: ⬜ m     YÜKSEKLİK: ⬜ m
ÖLÇEK:          ⬜        AÇI TİPİ: ⬜
KADRAJ ENİ:     ⬜ m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne ⬜ m
                          Sığıyor mu: ⬜   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: ⬜ px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: ölçek kademesi ⬜ · azimut ⬜°   → bant içi: ⬜
```

## 👤 KADRAJDAKİLER — devamlılık ve bedel taşıyıcıları

```
İNSAN SAYISI:   ⬜   ⛔ film boyu KİLİT: ⬜ (her karede aynı)
AYRIM EKSENİ:   ⬜   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    ⬜        ÇIKAN NESNE: ⬜
TAŞINAN NESNE:  ⬜   → önceki görüldüğü sahne S⬜ · sonraki S⬜
KAPATILAMAZ BEDEL: ⬜ (Örn: S14'te ezilen sol kol, S15-S36 boyu hareketsiz/askıda kilitli)
⛔ BİÇİM KİLİDİ: ⬜ [D146 — metinle tutulmuyorsa referans paketi sayfası şart]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      ⬜   (ortam kartının ışık takvimi: ⬜ · monotonik mi: ⬜)
PALET:     ⬜   ⛔ önceki sahneyle aynı olamaz [KURGU_RITMI §2 örüntü kırıcı]
SES:       ⬜   ⛔ önceki sahneyle aynı doku olamaz
MÜZİK:     ⬜ [var / yok — müziksiz sahne mi]
FİZİK:     ⬜   (ortam kartından bu sahneye düşen satırlar: ⬜)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    ⬜ · ⬜ s · konuşan ⬜ · REGISTER ⬜
İŞLEV:     ⬜   ⛔ boşsa replik SİLİNİR
AĞIZ:      ⬜ [okunuyor / okunmuyor] — bedenleştirme yalnız DORUKTA
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       ⬜   vizör ardında hangi ifade DEĞİŞİYOR
HAREKET:   ⬜   kadrajda ne HIZLANIYOR
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| ⬜ |  |  |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔/⚠️ |  |  | ⬜ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⬜   sınıf: ⬜ [PK/PB/YR/MÇ]
NÖTR TARİF:  ⬜   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: ⬜
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
□ OLAY tek cümleyle yazıldı, BAŞTA/SONDA durumları tanımlandı
□ 10 saniyelik EYLEM AKIŞI (0-3s, 3-7s, 7-10s) fiziksel hareket adımlarıyla yazıldı
□ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
□ önceki sahneyle ardışık çift bant içi (ya da şok gerekçeli)
□ kurulum harfi + işaret satırı yazıldı
□ sakatlık/bedel taşıyıcısı varsa S14-S36 devamlılığı sağlandı
□ ⛔ uyarıların hepsi kapandı
□ politika satırı yazıldı
□ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ ise MARS_SON_CIKIS_BOLUM_⬜.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
