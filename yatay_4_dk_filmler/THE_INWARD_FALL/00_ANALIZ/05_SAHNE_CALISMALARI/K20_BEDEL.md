# 🔬 S05 (K20) — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_INWARD_FALL

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
SAHNE:      S05 (K20 · 5/5 BEDEL)      BAŞLIK: Botların Terki
BÖLÜM:      THE_INWARD_FALL_BOLUM_2.md
ZAMAN:      190.0 s → 200.0 s     ⛔ FORMÜLLE [D122]: 0.0 + (20-1)*10.0
VURUŞ:      6 (Kriz / Bedel)      B5 SATIRI: BEDEL
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Teknisyen kordonu keser; manyetik botlar rayda bırakılarak sıfır-g boşluğuna fırlar.
BAŞTA:           Teknisyen son basamakta kordonun kesilmesiyle serbest kalır; manyetik kilitli ağır botları rayda bırakmak için mandalları çözer.
SONDA:           Botlar ray üzerinde kilitli kalırken teknisyenin hafifleyen gövdesi serbest ataletle merkez kovan açıklığına doğru süzülür.
⛔ KLİP İÇİ DEĞİŞİM: YOK (kesim K19 sonunda tamamlanmış, K20 serbest atalete geçiş sürecidir).
   Seçim: ① değişimi sahne sınırına taşı   Gerekçe: K21'de merkez kovanı tutamağını yakalama vuruşuna bağlanır
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  G        İŞARET: dönüş K16 — the same position, height and lens as Scene K16
LENS:           35 mm     MESAFE: 3.2 m     YÜKSEKLİK: 1.2 m
ÖLÇEK:          MLS       AÇI TİPİ: göz hizası (-90° azimut)
KADRAJ ENİ:     3.2 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne ve boşluk 2.6 m
                          Sığıyor mu: EVET
ANA NESNE PİKSEL: 290 px  ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: K19→K20 ölçek ECU→MLS (Δ=3) · azimut 45°→-90° (135°) → bant içi: EVET
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (isimsiz teknisyen)
AYRIM EKSENİ:   Grafit gri EVA tulumu, parlak turuncu reflektör, siyah kafes ve rayda terk edilmiş sarı emniyet botları
GİREN NESNE:    Yok      ÇIKAN NESNE: Terk edilen manyetik botlar (rayda kalır)
TAŞINAN NESNE:  Teknisyen gövdesi → sonraki K21'de merkez kovanına ulaşır
⛔ BİÇİM KİLİDİ: Referans Paketi R1 ve R2 kilitlendi [D146]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Mat grafit ve reflektif turuncu şeritler, keskin kask aydınlatması (axial skimming ışık 15°)
PALET:     Grafit gri, turuncu reflektör, siyah uzay boşluğu
SES:       Gerilen çelik tel çınlaması ardından aniden kesilen gerilim pufu ve kask içi derin soluk
MÜZİK:     yok
FİZİK:     0.2g neredeyse sıfır-g; kordon ve bot kütlesinden kurtulmuş gövdenin serbest radyal ataleti
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       —
HAREKET:   —
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D206 · Bedel Bedende | Karakter bedeli fiziksel araçla öder | "releases magnetic boot latches, leaving heavy boots locked on rail" yazılacak |
| D213 · Aksiyon Elipsi | Temas kesme ve sonuç ardışık planlarda | "severed tether drifts backward as body launches free into zero-g void" yazılacak |
| D175 · Çıplak Deri | Bot ayrılışında deri görünmez | "thick insulated thermal inner pressure socks fully sealed" belirtilecek |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | Kordon kesimi ve bot ayrılışı uzuv hasarı sanılabilir | Mekanik mandal çözülmesi ve botların rayda kalışı teknik dille yazıldı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR   sınıf: PK
NÖTR TARİF:  Teknisyen manyetik bot mandallarını mekanik olarak serbest bırakır; kalın izolasyonlu basınç çoraplarıyla merkez boşluğuna süzülür; kan veya bedensel hasar yoktur.
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilittir: Gövde sağlam tulum içinde tek parça halinde ağırlıksızlıkta süzülür.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil
→ hepsi ✅ ise THE_INWARD_FALL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
