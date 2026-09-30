# 🔬 S16 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_FALLING_WORLD

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
SAHNE:      S16  (sahibin V17'si)      BAŞLIK: Kiriş
BÖLÜM:      THE_FALLING_WORLD_BOLUM_2.md      DRAMATİK SAHNE: D4 · Yana yatan galeri (S14-S18)
ZAMAN:      160 s → 170 s       ⛔ FORMÜLLE [D122]: sahne(n) = n × 10 s
VURUŞ:      ④ Tartışma bandı içinde BEDEL SAHNESİ
B5 SATIRI:  BEDEL③ — BEYAZ'ın sol kolu işlevini kaybeder ve film boyunca geri KAZANMAZ
⭐VİRAL:    HAYIR
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Gevşeyen kiriş BEYAZ'ın sol önkolunu sıkıştırır; kol artık yük taşımaz.
BAŞTA:           kiriş tavanda gevşemiş, BEYAZ sol eliyle korkuluğa tutunuyor
SONDA:           kiriş inmiş, sol manşet iki yüzey arasında, eklem halkası dönmüyor
⛔ KLİP İÇİ DEĞİŞİM: VAR — ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687).
   Seçim: ② ARA DURUM YASAĞI cümlesi prompta yazılır
   Gerekçe: bedelin ödenmesi bu klibin İŞİDİR; sınıra taşınırsa bedel kadraj dışında kalır [D206]
   ARA DURUM YASAĞI: the beam comes down once and stays down; it never lifts, never settles twice
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  L        İŞARET: ilk kullanım (kümesi S17 ile)
⛔ S17 bu kurulumun KÜMESİDİR: "continues the previous clip from its exact
last frame — the same position, height and lens as Scene 16."
LENS:           35 mm     MESAFE: 2,5 m     YÜKSEKLİK: chest height
ÖLÇEK:          medium shot        AÇI TİPİ: profile
KADRAJ ENİ:     2,57 m      ⛔ HESAPLANDI (§5.2): kesir = boyut × odak ÷ (mesafe × sensör)
                          Kadraja alınacak nesne kiriş kesiti 0,4 m + sol manşet 0,15 m + TURUNCU'nun omzu — 2,57 m üçünü birden alır
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: manşet 0,15 m → %10,4 kare yüksekliği = 112 px ✅ (eşik 100 px)   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S15 (K · MLS · low angle · 0°) → S16 (L · MS · profile · 90°) = 1 kademe + 90° ✅ bant içi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   2 — BEYAZ sol üçte bir (manşet kirişin altında) · TURUNCU sağ üçte bir, BEYAZ'a DOĞRU hareket halinde
⛔ FİLM BOYU KİLİT: BEYAZ kadrajın SOL üçte birinde · TURUNCU SAĞ üçte birinde;
   merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
AYRIM EKSENİ:   ÜÇ kanal birden — ① RENK (kirli beyaz + kobalt mavi omuz ↔ yanık
                turuncu + siyah üst kol) ② OMUZ GEOMETRİSİ (köşeli geniş sırt ünitesi
                ↔ dar dikdörtgen sırt ünitesi) ③ KONUM (sol ↔ sağ üçte bir).
                ⛔ Yalnız RENK yetmez — P4 galeri karanlıktır ve RENK burada en zayıf kanaldır; ayrımı ışığa karşı OMUZ SİLUETİ taşır
GİREN NESNE:    düşen kiriş · sol manşet hasarı (KALICI, S47'ye kadar)
ÇIKAN NESNE:    sol kolun yük taşıma işlevi — KALICI
TAŞINAN NESNE:  sarı halat (S04'ten) · gümüş bant TURUNCU'nun bel kitinde (S17'de çıkacak)
⛔ BİÇİM KİLİDİ: METİNLE TUTULMUYOR [D146] → referans sayfası ŞART: R1 BEYAZ — ⭐ BU SAHNE R1'İN DURUM SINIRIDIR: S00-S15 hasarsız manşet,
   S16-S47 ezik manşet + gümüş bant. İki durum aynı sayfada, ayrı satırda
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      P4 tek sarı servis lambası (sağ üstte, kadraj içinde) + yarıktan gelen tek soğuk dilim (sol arkada) — İKİ kaynak, ikisi de kadrajda gerekçeli
           ışık takvimi: tek güneş film boyu SABİT saat yönünde (sol üst, kadraj
           dışı); ardışık sahne arası fark ≤30° ve ≤500 K · monotonik: ✅
PALET:     P4 galeri içi
           ⛔ önceki sahneyle aynı değil: S15 de P4'tü; örüntü kırıcı ÖLÇEK (MLS→MS) ve AÇI TİPİ (low angle→profile) üzerinden tutuyor
SES:       Y4 — kapalı hacim, gövdeden iletilen metal gerilmesi + kask içi nefes
           ⛔ önceki sahneyle aynı doku değil: S15 de Y4'tü ama doku değişiyor: S15 geniş metal kayması, S16 TEK kısa metal teması + ardından nefesin kesilmesi
MÜZİK:     YOK — bedel sahnesi müziksiz; ilk giriş S18'de
FİZİK:     §3.2 İNCE ATMOSFER + 0,30 g [D74 kaydı]. 0,30 g: kiriş 1,5 m'lik yolunu ≈1,0 s'de alır. Kiriş kütlesi ağırlığına rağmen YAVAŞ iner ama momentumunu korur — durduğunda geri sekmez.
```

## 🎙️ REPLİK

```
REPLİK:    R2 · 166 s · konuşan BEYAZ · REGISTER kısık, tek nefeste
           EN: Left cuff is locked.  ·  TR: "Sol manşet kilitlendi."
İŞLEV:     BEDEL③'ü MALZEME diliyle ilan eder — GÖRÜNMEYENİ taşır (eklem
           artık dönmüyor); durum bilgisi DEĞİL [D217]
AĞIZ:      okunmuyor — opak vizör; replik post-dub, promptta tırnak YOK
```

## ⭐VİRAL

```
⭐VİRAL DEĞİL — ve bu bir KARAR: bedel sahnesi ⭐ etiketi almaz çünkü ⭐'ın
ölçütü YÜZ + HAREKET'tir; burada yüz kapalı ve hareket TEK ve KISA.
Etiketi zorlamak D192 kalıbıdır (sıfatla korunan risk).
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D175 | Mühür korunur: anatomi hiçbir cümlede eldiven/manşet sınırında tarif edilmez | hasar YÜZEYDE: ezik dış kabuk + dönmeyen eklem halkası. "through the glove/cuff" ifadesi YASAK |
| D202 | Çapa üçlüsünün COST ayağı — adlandırılabilir BEFORE/AFTER gövde çifti | BEFORE: sol eldiven korkulukta kapalı · AFTER: sol kol gövdeye yapışık, yük SAĞ kolda |
| D206 | BEDEL EĞRİSİ: sol kol S16'dan sonra hiçbir karede yük taşımaz | S17-S47'nin 31 sahnesinde sol kol pasif; her bedel hücresi `<kanal> @ <saniye>` yazılır |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | YERÇEKİMİ F1 S8 — deponun TEK ÇÖZÜLEMEYEN reddi: yüzsüz izolasyon + kısıtlanmış uzuv | TURUNCU aynı karede ve hareket halinde (izolasyon kompozisyonla kapatılır) · ölçek MS, yakın plan YOK · sonuç manşette · yara/kan/acı sözlüğü ne pozitifte ne NEGATIVE'de | ✅ |
| 2 | ⛔ | D123 — yasağı yazmak kavramı sahneye sokar | "no injury", "not crushed" gibi hiçbir cümle yazılmaz; pozitif karşılığı: the cuff shell dents inward and the joint ring stops turning | ✅ |
| 3 | ⚠️ | İKİ YENİLGİ KURALI — bu kare iki kez düşerse üçüncü YAZIM denenmez | kamera taşınır: kiriş ve manşet TURUNCU'nun omzu üstünden, aynı L mesafesinde | ✅ hazır |
| 4 | ⚠️ | KART 6b — P4'ün iki ışık kaynağı sıçrama yapabilir | iki kaynak da kadrajda ve gerekçeli: servis lambası sağ üstte, yarık dilimi sol arkada; S17'de İKİSİ DE aynı yerde kalır (küme) | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⛔ EVET — BU FİLMİN EN RED-RİSKLİ KARESİ
SINIF:       YR (yüzsüz izolasyon + kısıtlanmış uzuv) + MÇ (malzeme çarpışması)
NÖTR TARİF:  ① ikinci figür kadrajda KALIR ② sonuç METALDE okunur, gövdede değil
             ③ ölçek daima MS veya daha geniş ④ yara/kan/acı/ezilen uzuv sözlüğü
             HİÇBİR yerde ⑤ hasarın tek kanıtı S17'nin gümüş bandıdır
⛔ YASAK CÜMLE YAZILMAZ. POZİTİF KARŞILIĞI:
  the loosened beam comes down across his left cuff and holds it between two
  surfaces; the outer shell of the cuff dents inward and the joint ring stops
  turning while his right arm takes the whole load.
⛔ PROB KLİBİ: P2 — ilk gün üretilir, kabul edilmeden B2 üretimi başlamaz.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve manşet 0,15 m → %10,4 kare yüksekliği = 112 px ✅ (eşik 100 px)
✅ önceki sahneyle ardışık çift bant içi
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL değil — gerekçesi yazıldı
→ hepsi ✅ — THE_FALLING_WORLD_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu YAZILABİLİR
```
