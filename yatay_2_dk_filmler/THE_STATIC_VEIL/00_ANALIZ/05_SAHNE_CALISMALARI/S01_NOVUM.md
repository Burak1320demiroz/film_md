# 🔬 S01 — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · THE_STATIC_VEIL

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
SAHNE:      S01            BAŞLIK: Kör Eden Yapışma
BÖLÜM:      THE_STATIC_VEIL_BOLUM_1.md
ZAMAN:      10.0 s → 20.0 s       ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      Dünyanın Kurulması    B5 SATIRI: ENGEL
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Astronot kılavuz rayı boyunca ilerlerken havalanan elektrostatik toz altın aynalı kask vizörüne yapışarak camı yer yer kaplar.
BAŞTA:           Astronotun kask vizörü tertemiz altın yansıtıcı ayna; adımlar ritmik ve tempolu.
SONDA:           Kask vizörünün yüzeyi ince gri toz tabakasıyla kaplanmış, altın parıltı matlaşmaya başlamış.
⛔ KLİP İÇİ DEĞİŞİM: YOK (tozların vizöre yapışma birikimi klip boyunca kesintisiz sürdürülür)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  B        İŞARET: ilk kullanım

LENS:           50mm     MESAFE: 3.5 m     YÜKSEKLİK: 1.6 m
ÖLÇEK:          MS       AÇI TİPİ: Göz Hizası (arkadan 3/4)
KADRAJ ENİ:     3.2 m    ⛔ HESAPLANDI (§5.2) — astronot üst gövde ve baş 1.2 m
                          Sığıyor mu: evet
ANA NESNE PİKSEL: 480 px   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S00(EWS, düşük zemin) → S01(MS, göz arkadan): ölçek 2 kademe · azimut 60° → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (her karede aynı)
AYRIM EKSENİ:   beyaz sert kompozit giysi, koyu gri körük eklemler, altın yansıtıcı küresel vizör
GİREN NESNE:    astronot sol kadrajdan girer
ÇIKAN NESNE:    yok
TAŞINAN NESNE:  vizördeki ilk toz birikimi → S02'de eldivenle silinmeye çalışılacak
⛔ BİÇİM KİLİDİ: Referans paketi sayfa R1 (Astronot giysisi ve kask)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Sert düşük açılı güneş, kaskın sağ omzunda teğet parlama, derin siyah gölgeler
PALET:     Parlak beyaz kompozit, koyu gri karbon eklemler, altın vizör yansıması, mat gri zemin
SES:       Bot tabanından kask içine iletilen ritmik boğuk adım titreşimi + sakin nefes alıp veriş
MÜZİK:     yok
FİZİK:     0.16g Ay kütleçekimi: adımlar yaylanan ve hafif yavaş; toz partikülleri elektrostatik çekimle vizöre yapışır
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       altın aynalı vizör yüzeyinde ilk kez beliren gri toz lekeleri
HAREKET:   yavaş adımlarla ilerlerken havada asılı tozların vizöre doğru hızlanıp elektrostatik olarak yapışması
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D139 | Düz sırt pozitif yüzey kilidi | The back of the suit is one continuous smooth panel from collar to hip, carrying nothing |
| D208 | Giysi kimliği dizisi | White heavy pressurized space suit, dark grey flexible carbon fiber accordion joint seals, gold reflective spherical visor |
| D16 | Yüz morphing engelleme | Gold reflective visor completely conceals the human face under specular reflection |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | D139 kamera arkadayken boş sırt | Pozitif düz sırt cümlesi prompt gövdesine eklendi | ✅ |
| 2 | ⚠️ | D42 toz birikimi devamlılığı | S1'de ilk %10'luk toz birikimi net tanımlandı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  Kask vizörüne elektrostatik toz yapışması
POZİTİF KİLİT: Fine grey regolith dust adheres electrostatically to the gold visor surface
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px (480px)
✅ önceki sahneyle ardışık çift bant içi (2 kademe, 60° azimut)
✅ kurulum harfi + işaret satırı yazıldı (B · ilk kullanım)
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ olduğu için THE_STATIC_VEIL_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
