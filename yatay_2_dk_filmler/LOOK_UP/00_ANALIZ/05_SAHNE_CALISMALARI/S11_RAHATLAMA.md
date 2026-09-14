# 🔬 S11 — SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S11            BAŞLIK: BEŞ KİŞİ
BÖLÜM:      LOOK_UP_BOLUM_2.md
ZAMAN:      01:40 s → 01:50 s
VURUŞ:      Beş kişi kurtuluş payoff (%92) B5 SATIRI: İSTEK (ortak kurtuluşun rahatlaması)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Kabin yükselir; Noah Mara'nın bilek tutuşunu yavaşça gevşetir, ekip beş kişi olarak rahatlama nefesi alır.
BAŞTA:           Kabin içi yüksek gerilimli mücadele sonrasındaki sıkı tutuş.
SONDA:           Beş kişi kabin içinde güvende, bilek tutuşu gevşemiş, sakin nefes alınıyor.
⛔ KLİP İÇİ DEĞİŞİM: YOK
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  E         İŞARET: dönüş S06

LENS:           28mm            MESAFE: 3.0 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Wide            AÇI TİPİ: Eye level
KADRAJ ENİ:     2.5 m           Kadraja alacak nesne: Kabin içi beş astronot
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 240 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 90°   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (Mara, Cole, Jun, Eren, Noah kabin içinde eksiksiz)
AYRIM EKSENİ:   Mara (kask dikey şeridi), Noah (çapraz sarı şeritler), Eren (göğüs makarası), Cole (omuz plakaları), Jun (kol modülü)
GİREN NESNE:    yok                  ÇIKAN NESNE: yok
TAŞINAN NESNE:  Lift cabin in (S11) / out (S12)
⛔ BİÇİM KİLİDİ: Referans paketi R1 (5 astronot) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kabin içi parlak beyaz çalışma ışığı
PALET:     Kırık beyaz kabin duvarları + grafit tekstil giysiler
SES:       Boğuk dış gürültü + kabin havalandırma fanı + derin nefes
MÜZİK:     Sakinleşen ambient drone
FİZİK:     Mikro yerçekiminde asansör kabininin yumuşak dikey ivmelenmesi
```

## 🎙️ REPLİK

```
REPLİK:    01:47 s · konuşan Noah · REGISTER H
İŞLEV:     Rahatlama ("We made it.")
AĞIZ:      okunuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D79 | Vizör şeffaflığı | Closed clear visor reveals facial release and calm breath |
| D138 | Metin yasağı | Kabin duvarlarında ve göstergelerde hiçbir yazı yer almaz |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Beş astronotun tamamı tek kadrajda görünmeli | All five humans visible in 3x3m cabin space | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kasklı beş astronot basınçlı kabin içinde bir arada durur.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
[x] önceki sahneyle ardışık çift bant içi
[x] kurulum harfi + işaret satırı yazıldı
[x] uyarıların hepsi kapandı
[x] politika satırı yazıldı
→ hepsi ✅: LOOK_UP_BOLUM_2.md'ye S11 promptları yazıldı.
```
