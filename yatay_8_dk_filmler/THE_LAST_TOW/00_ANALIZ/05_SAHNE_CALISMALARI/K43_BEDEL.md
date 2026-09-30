# 🔬 K43 — KİLİT KLİP · BEDEL · SAHNE ÇALIŞMASI · THE_LAST_TOW

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları. Bu dosya bitmeden bu klibin promptu yazılmaz.

---

## 🪪 KİMLİK

```
KLİP:       K43  ·  SAHNE S11 (3/5 · KARAR)      BAŞLIK: KAMA
BÖLÜM:      THE_LAST_TOW_BOLUM_2.md
ZAMAN:      420,0 s → 430,0 s     ⛔ FORMÜLLE: klip başlangıcı(n) = (n−1) × 10,0 s
VURUŞ:      merkezî seçim + BEDEL — filmin en pahalı karesi
B5 SATIRI:  BEDEL ③ (kesici)
⭐VİRAL:    hayır — ölçüt taşımıyor (yüz kadrajda yok, hareket düşük)
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Kesici kafası açıklığın önünden boşluğa giriyor ve 19 mm'ye oturuyor.
BAŞTA:           kör kesici sağ eldivende, açıklık 4 mm kalmış ve kapanmaya devam ediyor
SONDA:           kafa boşlukta, 19 mm'lik sapı iki yüzeye dayanmış; el hâlâ üstünde
⛔ KLİP İÇİ DEĞİŞİM: VAR — bir eşik geçiliyor (bu rejimde her klip bir
   değişim taşır; ölçülmüş en zayıf eksen, T2V-CompBench 0,0687)
   Seçim: ② ARA DURUM cümlesi prompta yazılıyor
   Gerekçe: ⭐ değişim bir SEÇİMDİR ve kadrajda tamamlanıyor: alet elden çıkıp yapıya geçiyor. Kaynama ANI bu klipte YOK — o K44'e bölündü (temas iki klibe bölünür, §3.6)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  D        İŞARET: dönüş K37
LENS:           85 mm     MESAFE: 1,1 m     YÜKSEKLİK: 1,25 m
ÖLÇEK:          CU (4)        AÇI TİPİ: göz hizası
KADRAJ ENİ:     0,47 m      ⛔ HESAPLANDI (36 mm / f × mesafe)
                          kadraja alınacak nesne kesici kafası 0,46 m + açıklık — kadrajı çapraz dolduruyor → SIĞIYOR ✅
ANA NESNE PİKSEL: 410 px   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  ölçek kademesi 1 (MS 3 → CU 4) · azimut 80°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1
AYRIM EKSENİ:   n/a (tek gövde, yalnız eldivenler kadrajda)
GİREN NESNE:    —
ÇIKAN NESNE:    kesici kafası — bu klipten sonra bir daha kadına dönmüyor
TAŞINAN NESNE:  kesici K01'den beri kemerde; K16'da ağzı gitti; burada yapıya geçiyor
⛔ BİÇİM KİLİDİ: kesici kafası: 46 cm uzun, sapı 19 mm, çıplak koyu çelik, ağzı körelmiş — dört ölçü, film boyu aynı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      çerçeve levhası 370 K'de parlıyor, açıklığın içi gölgede; sınır kadrajda net, dolgu 0
           ışık takvimi: gölge kenarı dikişe güverteyi geçmiş — çerçeve 23 mm büyümüş · monotonik ✅ (tek yön)
PALET:     IŞIK   ⛔ önceki sahneyle aynı değil
SES:       çerçevenin gerilme sesi gövdeden; tek tık — kafanın oturması
MÜZİK:     var — tek katman, K44'te SUSUYOR (filmin hard mute noktası)
FİZİK:     0,30 g · hard vakum · metalin üstünde 0 kare toz · gölge mutlak
           siyah, dolgu 0 · pas 0 · kıvılcım 0 · dışarıda ses yok
```

## 🎙️ REPLİK

```
REPLİK:    — (film boyu 0 replik)
İŞLEV:     — ⛔ boş replik yazılmadı, SİLİNMİŞ sayılmaz: SPEC'te sayıyla 0
AĞIZ:      okunmuyor — ağız vizör ardında ve film boyunca konuşmuyor
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
— (ölçütü taşımıyor: yüz yok, hareket düşük. ⛔ Filmin en önemli karesi olması onu ⭐VİRAL yapmaz [§2.4])
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D202 | merkezî seçim bedende okunur | eldiven kesiciyi BIRAKIYOR, el boş geri çekiliyor (K45) |
| D206 | bedel bedende | K44-K48'de kemerdeki yuva BOŞ ve siluette görünür |
| red #13 | tepeden makro + yüzsüz izolasyon = SAHNE İPTAL | 85 mm · 1,1 m · göz hizası; eller ard arda değil, biri kesicide biri çerçevede; ufuk kadrajda |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 4 | ⚠️ | #13 PB kompozisyon reddi (U-4) | makro yazılmadı; kadraj göz hizasında ve ufuk içinde | ✅ |
| 1 | ⛔ | kural pozitif olayla kanıtlanır (U-1) | bu klip HAZIRLIK; kanıt K44'te (temas iki klibe bölündü) | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⚠️ evet — sınıf PB: yüzsüz yakın kadrajda iki eldiven ve bir alet
NÖTR TARİF:  `her right glove brings the blunt cutter head to the gap and sets the nineteen-millimetre shank between the two faces` — iş tarifi, tehdit sözlüğü yok
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilit: `the two faces stay separate with a clean visible boundary; the shank rests between them`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 410 px ≥ 100
☑ önceki kliple ardışık çift bant içi (✅)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları gerekmedi
→ hepsi ✅ → THE_LAST_TOW_BOLUM_2.md'ye bu klibin IMAGE + VIDEO promptu yazılabilir
```
