# 🔬 K24 — KİLİT KLİP · FINAL · ÇALIŞMA · THE_COUNTED_RIVET

> ⛔ Başlık biçimi `# 🔬 K<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin birim başlığı deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `05_.../00_SAHNE_TABLOSU.md` satırı +
> `04_UYARI_NOTLARI.md`'nin bu klibe düşen satırları. Bu dosya bitmeden bu
> klibin promptu yazılmaz.
> 🆕 ÇOK KLİPLİ SAHNE (22.09.2026): kilit rol KLİBE bağlanır; klip bir SAHNENİN
> içindedir ve sahne kilidi (ışık · fizik · ses yatağı) sahne boyunca birebirdir.

---

## 🪪 KİMLİK

```
KLİP:       K24            SAHNE: S07 · 5/5 · BEDEL   BAŞLIK: KAPANIŞ
BÖLÜM:      THE_COUNTED_RIVET_BOLUM_2.md
ZAMAN:      230,0 s → 240,0 s       ⛔ FORMÜLLE [D122]: (n−1) × 10,0 s
VURUŞ:      ⑩ kapanış imajı (%95-100)
B5 SATIRI:  BEDEL — iki bedel de ödendi (S5 örtü bağı · S7 dokuz nokta)
⭐VİRAL:    hayır  → film boyu 0 ⭐viral klip; kapı iki kanalı birden istiyor ve
            bu estetikte tek klipte birleşmiyor [D74 gerekçesi · 03_SAHNE §2.4]
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Son mandal çenesi kesilmiş ve açık; plaka kadrajdan kesintisiz geçiyor ve kenarı hiçbir yerde görünmüyor.
BAŞTA:           son çene kesilmiş ve açık, iki eldiven iki yanında, plaka arkada aşağı doğru geçiyor
SONDA:           plaka hâlâ geçiyor, kenarı yok, lamba aynı dört saniyede atmaya devam ediyor
⛔ KLİP İÇİ DEĞİŞİM: VAR — plakanın kadrajdan geçmesi. Bu bir DURUM değişimi değil,
   sürekli bir GÖRELİ HAREKET ve filmin son cümlesi budur: bitmiyor.
   Seçim: ① sınıra taşınmadı — kapanış imajı hareketin İÇİNDE olmalı
   Gerekçe: statik siyah 0 saniye [D211]; son kare adlandırılmış bir nesne
   (kesilmiş çene) ve devam eden bir hareket taşıyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  B        İŞARET: dönüş — K01 (⭐ KAFİYE: işaret K22'yi değil K01'i gösterir)
⛔ dönüşse kamera metni BİREBİR kopyalanır + işaret satırı taşınır; bu rejimde
  KÜME YOKTUR (son kare zinciri kaldırıldı — ㉜)

LENS:           50 mm     MESAFE: 1,2 m     YÜKSEKLİK: 1,15 m
ÖLÇEK:          CU        AÇI TİPİ: göz hizası (üç-çeyrek)
KADRAJ ENİ:     0,864 m      ⛔ HESAPLANDI: W = 2·d·tan(FOV/2) · FOV = 2·arctan(18/f)
                          KADRAJ YÜKSEKLİĞİ: 0,486 m (W·9/16)
                          kadraja alınacak nesne: mandal çenesi 0,30 m
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: 1333 px — K01 ile AYNI (kafiyenin ölçülebilir tarafı)   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ KLİPLE:  ölçek kademesi 1 (C MS → B CU) · azimut 75° (C 135° → B 60°)   → bant içi: ✅ bant içi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
IN FRAME:       hands   ⛔ kadrajda olmayan YAZILMAZ [㉖ · D214]
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 24/24 klipte rakamla ("Exactly one
                human character") · duplikasyon 0 · yansıyan insan 0 kare
AYRIM EKSENİ:   — (tek insanlı film; ikinci figür hiç kadraja girmiyor)
GİREN NESNE:    —
ÇIKAN NESNE:    mandal çenesi (film boyu taşınan nesne burada KESİLMİŞ olarak çıkar)
TAŞINAN NESNE:  mandal çenesi → K01'den · örtünün açık kenarı → K14'ten · plaka → K05'ten
⛔ BİÇİM KİLİDİ: eldiven geometrisi K01 ile BİREBİR aynı cümle. Sağ manşet
                halkasındaki mat aşınma (K14'ten) duruyor — K01'de YOKTU; iki
                kadraj arasındaki tek kalıcı fark bu ve BEDELİN kendisi
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      kubbe okra kademe 2 · gölgesiz, her yönden dolgu · güneş diski 0 kare
           takvim: 0 (S1-S5) → 1 (S6) → 2 (S7) · monotonik: ✅ · yalnız sahne
           sınırında değişir, klip içinde ASLA
PALET:     okra kubbe kademe 2 + koyu gri-yeşil plaka + kurşun grisi giysi
SES:       iki kademe kalın uğultu, bir kademe incelerek + çeliğin çelik üzerinde sürtünmesi + lamba, aynı dört saniyede
MÜZİK:     VAR → ÇEKİLİYOR: 234,0 s'de tek sönümlü darbe, 236,0 s'de alt uç gider, 239,0 s'de son tık. ⛔ Cue ÇÖZÜLMEZ — final akoru yok
FİZİK:     0,904 g · nötr yüzerlik POZİTİF kuralla · ⛔ FARKLI: platform plakadan ÇÖZÜLDÜ ve boyunca YÜKSELİYOR.
           PHYSICS satırı S7'nin üç klibinde BİREBİR aynı ve `never rises`
           yerine `rises slowly and steadily along it` diyor — çelişki değil,
           sahnenin kendi kilidi (㉜⑥). `The plate does not change shape`
           cümlesi çekirdeğin `terrain static` yasağını POZİTİF karşılıyor
           bırakılan nesne: eldiven boyu ≈ 0,33 s · rüzgâr 0 → hiçbir şey savrulmaz
```

## 🎙️ REPLİK

```
REPLİK:    YOK — film bilinçli sessiz · tırnak 0 karakter · `No dialogue.` AUDIO satırında
İŞLEV:     — (replik yok)
AĞIZ:      kadraj dışı
```

## ⭐VİRAL — işaretli klip DEĞİL

```
⛔ Bu klip ⭐VİRAL etiketi TAŞIMIYOR. Ölçüm: YÜZ ⛔ (IN FRAME: hands) · HAREKET ⛔ (plaka sabit hızda geçiyor,
   hızlanma yok — ve hızlanmaması filmin sonucudur)
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girdi |
|---|---|---|
| [D210] kapanış açılışı taşır | kamera cümlesi K01 ile BİREBİR · dönüş işareti K01'i gösteriyor · TIMELINE `hold` ile bitiyor | kamera satırı + 7,0 s |
| [D211] son 10 saniyede çıkış | son kare ADLANDIRILMIŞ nesne: kesilmiş mandal çenesi · statik siyah 0 s | kilit satırı |
| [D202] çapa üçlüsü ③ | ilk klipte bir çeneyi KAPATIR ↔ son klipte dokuzu KESMİŞ, aynı eldiven aynı kurulumda | iki klibin eldiven cümlesi birebir |
| [D141] final vuruş | dokuz kesik uç K23'te sayıldı; bu klip onun SONUCUNU taşır (plaka geçiyor) | TIMELINE |
| [D207] bedel sıfırlanmaz | omuzlar düşük, manşet aşınması yerinde | CONTINUOUS ACTION |
| [D175] mühür | çıplak-deri negatifi ÜÇ BÖLGE birden, tek cümlede | `No bare skin anywhere in frame — none above the collar, none at the wrist, none at the ankle.` |
| [D209] dünya çapası | üç çapa BİREBİR, 24/24 klipte | kubbe/okra derinlik/plaka+perçin cümleleri değişmeden |
| [D200] tek yerçekimi | tek değer, tek yerde | `Gravity is 0.904 g …` PHYSICS satırında |
| [D138] metin yasağı | ölçü aleti yüzeyine işaret YAZILMAZ | `No notches, no graduations, no scale marks and no tick lines …` |
| [D214] kadraj envanteri | yalnız IN FRAME'deki tarif edilir | ilk satır `IN FRAME:` · Bible'ın kalanı yok |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| ⛔7 | ⛔ | K01↔K24 kafiye çifti niyette kalır, kapanış yeni bir kurulum üretir | Kamera cümlesi B harfinin metniyle BİREBİR; dönüş işareti `— the same position, height and lens as Clip 1.` yani kafiyeyi ADRESLİYOR. IN FRAME ikisinde de `hands`. Tek kalıcı fark: manşetteki mat aşınma | ✅ |
| ⛔8 | ⛔ | Bedel kesmede sıfırlanır | Omuzlar düşük (K14'ten), manşet aşınması yerinde (K14'ten), kubbe kademe 2 (S6-S7'den), lamba aynı periyotta. Hiçbiri geri dönmüyor | ✅ |
| ⚠️5 | ⚠️ | Otomasyonun germe hareketi bir KUMANDA sanılır | Bu klipte otomasyon HİÇBİR ŞEY germiyor — yalnız lamba atıyor. Makine ritmi insanın kararından SONRA da sürüyor; tema-final indeksi budur | ✅ |
| ⚠️3 | ⚠️ | Işık takvimi geri sarar | Kademe 2, S7'nin beş klibinde birebir; son klipte de aynı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır — kesme bitti, kadrajda alet yok, temas metal-metal
NÖTR TARİF:  "The two-jawed clamp stands open on its parted neck, the cut face
             bright where the shear went through." ⛔ Sonuç tarif edildi, eylem
             değil [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: `the plate passes down through the frame with no edge in it` —
             filmin son iddiası bir yokluk cümlesi değil, bir HAREKET
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
✅ önceki klipe göre ardışık çift bant içi (✅ bant içi)
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı (yukarıdaki durum sütunu)
✅ politika satırı yazıldı
✅ ⭐VİRAL değil, gerekçesi ölçülü
→ PROMPT YAZILDI: `THE_COUNTED_RIVET_BOLUM_2.md` · KLİP 24
```
