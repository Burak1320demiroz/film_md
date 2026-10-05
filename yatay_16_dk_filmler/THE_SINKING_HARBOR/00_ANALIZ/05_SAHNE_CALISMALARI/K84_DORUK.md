# 🔬 S21 · K84 — KİLİT KLİP · DORUK · SAHNE ÇALIŞMASI · THE_SINKING_HARBOR

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları + `00_SAHNE_TABLOSU.md`'nin K84 satırı.

---

## 🪪 KİMLİK

```
SAHNE:      S21  ·  KLİP: K84  ·  ROL: 4/4 BEDEL       BAŞLIK: SONDA AYRILIR
BÖLÜM:      THE_SINKING_HARBOR_BOLUM_7.md
ZAMAN:      830 s → 840 s     ⛔ FORMÜLLE [D122]: (n−1) × 10 s · n = 84
VURUŞ:      BIRAKMA        B5 SATIRI: ENGEL (çözülür)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Üç kilometrelik sonda limandan uzaklaşır; çekilmeyen katman gevşer ve enerjisiz metal ucu bırakır.
BAŞTA:           sonda limandan sarkıyor, üç bağlantı açık, katman ucu hâlâ sarıyor
SONDA:           sonda limandan AYRILMIŞ ve aşağı gidiyor; katmanın kıvrımları gevşemiş, uç serbest
⛔ KLİP İÇİ DEĞİŞİM: VAR — ayrılmanın kendisi klibin olayı
   Seçim: ② klip İÇİNDE, KADRAJI TERK SÜRESİYLE [D127]
   Gerekçe: İvme yazılmaz; sondanın ucu altıncı saniyede kadrajın alt kenarını geçer ve onuncu saniyede tamamen gider. Ölçen kenar kadrajın ALT sınırıdır [LOSS OF LIFT madde 6: batan altta oturur ve alt kenardan çıkar].
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  S        İŞARET: dönüş K69 (ara 15 klip → yeniden tanıtım)

LENS:           24 mm     MESAFE: 14.000 m     YÜKSEKLİK: liman ekseni
ÖLÇEK:          EWS        AÇI TİPİ: eye level
KADRAJ ENİ:     21.000 m      ⛔ HESAPLANDI — kadraja alınacak nesne liman gövdesi 48 km (taşar) · sonda 3 km
                          Sığıyor mu: liman TAŞAR (bilinçli, ölçek şahidi ③) · sonda 3 km → 549 px
ANA NESNE PİKSEL: liman taşar · sonda 549 px   ⛔ ≥100 px [D179] → GEÇTİ ✅
ÖNCEKİ KLİPLE:  ölçek kademesi K83 MWS → K84 EWS = 2 kademe ✅ · sonda platformu → liman ekseni, mekân DEĞİŞTİ   → bant içi: bant içi ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — insansız 17 klipten biri
AYRIM EKSENİ:   — (insan yok)
GİREN NESNE:    ayrılmış sonda (yeni bir nesne değil, yeni bir KONUM)
ÇIKAN NESNE:    ⭐ sonda — GERİ BELİRMEZ (sahibin §8 süreklilik kaydı)
TAŞINAN NESNE:  katman K95'te sakinleşmiş hâliyle geri döner · liman K94'te gömülür
⛔ BİÇİM KİLİDİ: VAR — sonda ve liman biçimi metinle tutulmuyor → referans paketi sayfaları KAPI 0
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      gevşeyen amber, kubbe 2/6; sondanın enerji hattı KESİLDİ, ucunda ışık YOK (K83'ün sonucu)
PALET:     gevşeyen amber — S20'nin (amber + vizör buğusu) paletinden FARKLI ✅
SES:       derin ritim YAVAŞLAR; zafer müziği HENÜZ tamamlanmaz (sahibin cümlesi)
MÜZİK:     var — çözülmeye başlar ama tamamlanmaz; tamamlanma K93'te
FİZİK:     1,00 g · bırakılan 3 km'lik gövde aşağı gider, kadrajı 6. saniyede terk eder · su YOK
```

## 🎙️ REPLİK

```
REPLİK:    — (replik YOK)
İŞLEV:     — (replik yok; doruk sessiz okunur)
AĞIZ:      — (insan yok)
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
YÜZ:       — (⭐VİRAL değil)
HAREKET:   — (⭐VİRAL değil)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| **D127** | ivme yazılmaz, kadrajı terk SÜRESİ yazılır | *by the sixth second its lower end has crossed the bottom frame line, and by the tenth it is gone; it does not return* |
| **D157** | novumun SONUCU — kural bedele dönüşür | Katman çekilmediği için gevşer; bu, K34/K38'in üçüncü kanıtı |
| **D38** | hasar SAYILI ve SINIRLI | Liman gövdesi SAĞLAM, yalnız iki kolon kararsız; sürekli enkaz saçılması 0 |
| **D62** | KESİLEMEZ listesinde | Doruk — kurgu kapısı bu klibi arar |
| **D56** | su YOK | ⛔ "sonda aşağı iner, katman bırakır" — en yakın su okuması "denizaltı dalışı". `dive` · `sinks` · `submerge` 0 kez; `is drawn down` + MEDIUM LOCK |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | ⛔-1 SU | MEDIUM LOCK + `no submarine` negatif cümlesi | ✅ |
| 2 | ⛔ | ⛔-6 alçalma yönü (LOSS OF LIFT madde 6: rapor sondayı DÜŞÜYOR okudu) | ⭐ Burada sonda GERÇEKTEN aşağı gidiyor ve bu DOĞRU; yön nesneye bağlı: *down past the cloud boundary that fills the lower third* | ✅ |
| 3 | ⛔ | ⛔-5 K4 dışında anatomi sayısı yazılmaz | Bu klip K3 SİLUET → katmanın kıvrımı tarif edilir, SAYISI yazılmaz | ✅ |
| 4 | ⚠️ | ⚠️-10 part sınırı K72↔K73 ölçülmüş; K84↔K85 bölüm sınırı | Ardışık çift ölçüldü: EWS→MWS 2 kademe ✅ | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR — insan yok. ⚠️ `tissue` · `wound` · `organ` 0 kez; katman `the dark living layer`
NÖTR TARİF:  ayrılma MEKANİK olarak yazılır: üç bağlantı açık, enerji hattı kesik, gövde kendi ağırlığıyla gider
POZİTİF KİLİT: `the folds of the dark layer slacken and let the unpowered metal end go` — bırakma POZİTİF
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — sonda 549 px · liman taşar (ölçek şahidi)
☑ ardışık çift K83→K84 = 2 kademe ✅ · bölüm sınırı K84↔K85 ölçüldü ✅
☑ kurulum harfi S + dönüş işareti yazıldı
☑ ⛔ uyarıların dördü de kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil
→ THE_SINKING_HARBOR_BOLUM_7.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
