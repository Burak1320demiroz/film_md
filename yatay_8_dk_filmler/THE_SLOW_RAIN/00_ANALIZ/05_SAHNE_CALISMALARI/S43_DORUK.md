# 🔬 S43 — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · THE_SLOW_RAIN

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
SAHNE:      S43            BAŞLIK: OTURUR
BÖLÜM:      THE_SLOW_RAIN_BOLUM_4.md
ZAMAN:      430,0 s → 440,0 s       ⛔ FORMÜLLE [D122]: hook S0 klibin içinde → n × 10 s (klip 10 s VARSAYIM, araçtan ölçülür)
VURUŞ:      DORUK               B5 SATIRI: İSTEK teslim
⭐VİRAL:    hayır  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Çekirdek yuvaya oturur (TEMAS · DEĞİŞİM · SONUÇ aynı klipte); klip gösterge sönükken biter — gösterge sınırda yanar
BAŞTA:           çekirdek kapağın önünde
SONDA:           yuvaya oturur (TEMAS · DEĞİŞİM · SONUÇ); iki eldiven bastırıyor; gösterge SÖNÜK kesilir
⛔ KLİP İÇİ DEĞİŞİM: VAR [VAR / YOK]
   VAR ise: ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687). İki seçenek:
   ① değişimi sahne SINIRINA taşı  ② ARA DURUM YASAĞI cümlesini prompta yaz
   Seçim: ① — gösterge değişimi S43→S44 SINIRINA taşındı; çekirdeğin oturması HAREKET (durum değil)   Gerekçe: SAHNE_ZINCIRI §1
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  L        İŞARET: küme S42
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           35 mm     MESAFE: 4.0 m     YÜKSEKLİK: 2.10 m
ÖLÇEK:          MS        AÇI TİPİ: high angle medium shot, three-quarter rear · az 135°
KADRAJ ENİ:     4.11 m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne çekirdek + yuva 0.6 m
                          Sığıyor mu: ✅   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: 560 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: ölçek kademesi 0 · azimut 0°   → bant içi: küme
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 × 48 (her karede aynı)
AYRIM EKSENİ:   tek figür — soluk gri giysi ↔ koyu zemin/koyu kanat; teal göğüs bandı   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    — (çekirdek yuvaya girer)        ÇIKAN NESNE: —
TAŞINAN NESNE:  çekirdek (S10'dan beri) → yuvada kalır
⛔ BİÇİM KİLİDİ: kask (düz pane + kalın koyu çerçeve) + çekirdek + yuva (S3 karesi) — referans paketi YOK (sahip); ilk onaylı kareler referans [D153/D154]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      tavan paneli 3200 K sabit, kırağı beyazı   (ışık takvimi: dış sabit pus dolgusu / iç 3200 K sabit · monotonik: değişmez; iç↔dış geçişleri OLAY)
PALET:     (küme S42) (küme — aynı vuruşun devam klibi)
SES:       (küme S42) + oturma tıkırtısı
MÜZİK:     yok — oturma tıkırtısı tek başına; S44'te müzik girer
FİZİK:     —   (kart §3.9: sıcak yüzeyde puf 0,5 m / 2 s · rüzgâr yok · gölge sığ · güneş diski 0)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (film sessiz tasarımlı)
İŞLEV:     —
AĞIZ:      — ağız kapalı, konuşma yok
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (3/4 arka, yüz yok; ⭐VİRAL değil)
HAREKET:   —
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D213 · D141 | TEMAS · DEĞİŞİM · SONUÇ aynı klipte; sonuç ≥1 s; FİNAL VURUŞ KANITI = gösterge (S44 açılış karesi, 1 adet) | '0.0s — the core is already in the mouth of the socket, both gloves on it, her weight over it · 3.0s — it drops the last hand's width and seats with a dull knock · 4.0-10.0s — she keeps pressing it down with both gloves; the socket lamp beside it stays dark through the last frame' |
| SAHNE_ZINCIRI §1 | gösterge klip içinde YANMAZ — S44'ün ilk karesinde yanık | End: 'core seated, lamp dark, both gloves pressing' · Start S44: 'the lamp is lit, a warm point beside the seated core' |
| D62 KESİLEMEZ · ÜRETİM SIRASI 3 | doruk kurguya girer; üretim sırasında S1 ve S15'ten hemen sonra | — |
| KART 5 | gösterge tek ışık noktası, rakam/çentik/ekran yok | 'a single small round lamp set into the socket rim, unlit' |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U-7 durum değişimi sınıra | gösterge S43 sönük / S44 yanık | ✅ |
| 2 | ⚠️ | U-sarı-4 sayaç a/b | S42 küme başı kırağı çizgisi tavana yakın (b-karesi) | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  —   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: 'the core seats with a dull knock and stays seated'
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
✅ önceki sahneyle ardışık çift bant içi (ya da şok gerekçeli)
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ — THE_SLOW_RAIN_BOLUM_4.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```

## 🔗 KART BAĞI · SON 3 s · ÖLÜ SAHNE BEŞ SORUSU (`KARAKTER_KARTI` §10 · `SAHNE_DOLULUGU` §6)

```
KART BAĞI:        İSTEK teslim · İLK↔SON'a köprü
İZLEYİCİ CÜMLESİ: oturmasını istiyor — bastırır, bırakmaz; klip sönük göstergeyle biter
TAŞIYAN KANAL:    AĞIRLIK + KALINTI   TASK ONLY: hayır
SON 3 s:          keeps both gloves on the seated core, pressing it down; the socket lamp is still dark at the cut
① FİİL   süreç ✅ (bastırır, oturtur)
② DİRENÇ ✅ (çekirdek son el genişliğinde takılır)
③ TEK KİLİT ✅ · TIMELINE ≤3 satır
④ SINIR  ✅ (End/Start sınır satırı sahne haritasında)
⑤ SAAT   ✅ (nefes (omuz) — iç mekân, dış saat yok; ikinci saat yok)
```
