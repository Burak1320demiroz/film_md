# 🧪 THE_LAST_GATE — QA SPEC

> QA rubriğinin BAŞINA bu dosya yapıştırılır [D117]. Kanonik hikâye kaynağı
> `00_ANALIZ/00_ON_PLAN/THE_LAST_GATE_KAPSAMLI_PLAN.md` (sahip · 30.09.2026).
> ⛔ Üretim 0 kare — aşağıdaki E bloğu dışındaki her ölçüm ⬜ ÖLÇÜLMEDİ durumundadır.

---

# A · KOŞU BEYANI

```
FILM:            THE_LAST_GATE  ·  yatay 16 dk  ·  96 klip × tam 10,000 s = 960,000 s
GRID:            klip başlangıcı(n) = (n−1) × 10,000 s  ·  hook K01–K04 96'nın İÇİNDE, ayrı değil
CLIP COUNT:      96 (zaman çizgisi)  ·  ÜRETİLEN KLİP 92  ·  PROMPT 184
                 K01–K04 kurgu bloğudur: kaynak kliplerden kesilir, yeni kare üretilmez
SCENE COUNT:     25   ⛔ SCENE COUNT ≠ CLIP COUNT · SHOT COUNT = CLIP COUNT (çok klipli sahne rejimi)
SAHNE PLANI:     4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
DIALOGUE LINES: 32   (+1 post-dub ad satırı: K18'in tek adlık repliği promptta cümleye çevrildi [D34])
VO LINES:        4    (H1–H4 · yalnız K01–K04 kurgu bloklarında · promptta 0 kez)
KIRPMA / SABİTLEME: ham klip ARAÇTAN ölçülür [D124]; kurguya alınan birim 24 fps'te TAM 240 kareye
                 sabitlenir. Zaman kodları YENİDEN HESAPLANMAZ; sapma bu satırla kapanır.
                 ⬜ ÖLÇÜM: ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
MOTOR:           I2V — her klip kendi onaylı başlangıç karesinden · son kare zinciri YOK
TEMA:            DAYANIŞMA (aday etiket) — "Kendi çıkışını söken, herkesin çıkışını kurmuş olur."
THEME SCENES:    S06 · S08 · S17 · S18 · S25
```

## PART GRID — QA birimi PART (§2.8) + TAM FİLM

| koşu | klip | süre | bölüm dosyası | maske (①.11) | durum |
|---|---|---|---|---|:--:|
| PART 1 | K01–K24 | 0–240 s | BOLUM_1 + BOLUM_2 | BAŞ: ④ Ending · ⑫ Peak · ⑫ Exit `—` | ⬜ |
| PART 2 | K25–K48 | 240–480 s | BOLUM_3 + BOLUM_4 | ORTA: ④ Hook VE Ending · ⑫ dörtlü `—` | ⬜ |
| PART 3 | K49–K72 | 480–720 s | BOLUM_5 + BOLUM_6 | ORTA: aynı | ⬜ |
| PART 4 | K73–K96 | 720–960 s | BOLUM_7 + BOLUM_8 | SON: ④ Hook · ⑫ Hook Question · ⑫ Stakes `—` | ⬜ |
| **TAM FİLM** | K01–K96 | 960 s | sekizi birden | maske YOK · ③ SES kabulü YALNIZ burada | ⬜ |

```
RUBRİK BAŞINA TEK SATIR BEYAN [D129]:
  "THIS FILE IS PART n OF 4 — clips Kxx-Kyy — the film's opening/ending is NOT in this file."
  TAM FİLM: "THIS FILE IS THE FULL FILM — 96 clips."
BÜTÜN-FİLM DÖRTLÜSÜ (④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair): part koşularında `—`,
  TAM FİLM koşusunda SAYI taşır.
KOMUTLAR:  olcum_kapisi.sh <part master>  ×4 + tam master ×1
           sahne_kapisi.sh <part master> 10 24  ×4
           rapor_kontrol.py <ham…> --film yatay_16_dk_filmler/THE_LAST_GATE --bolum n/4   ⛔ ZORUNLU
           rapor_kontrol.py <ham…> --film yatay_16_dk_filmler/THE_LAST_GATE               (TAM FİLM)
```

## SAHİBİN DÖRT SORUSU — TAM FİLM raporu cevaplamak zorunda

```
① 00:40'ta izleyici hedefi ve büyük engeli söyleyebiliyor mu?      ⬜
② 04:00'te Mara'nın neden diğerlerini seçtiği anlaşılıyor mu?      ⬜
③ 08:00'de vaat edilen büyük gemi ayrılışı görülüyor mu?           ⬜
④ 12:00'de neden araç gerektiği açık mı · 16:00'da kimlerin nasıl kurtulduğu anlaşılır mı?  ⬜
```

## ⚠️ YANLIŞ POZİTİF DUVARI — rapor bunları KUSUR YAZMAZ

```
① SCENE COUNT (25) ≠ CLIP COUNT (96) — çok klipli sahne rejiminin TASARIMIDIR.
② K01–K04'te aynı görüntülerin sonra tekrar gelmesi — özet açılış TASARIMDIR (kapsamlı plan §9).
③ Aynı çerçevenin iki kez gelmesi (K05↔K08 · K49↔K64↔K69 · K85↔K96) — eş kadraj çifti, DEĞİŞİMİ
   görünür kılmak için (YANASMA §1.3). Tekrar DEĞİL.
④ K05'te büyük açıklığa dönülmesi — hook ileri görüntüdür, K05 kronolojik başlangıçtır.
⑤ Rozetlerin YAZISIZ görünmesi — deponun metinsiz amblem dili (ASTRONOT_DONANIM §3): rozetin
   görünür TASARIMI var (üç kanat · pusula · iki çubuk · üç parça · köşeli), yalnız HARF yok.
   Renk ve ince ayrıntı POST katmanında bindirilir (SAPMA 1).
⑥ Ön kol çiziğinin K16'dan sonra her karede olması — devamlılık kilidi, kusur değil.
⑦ 0,40 g / dönme yerçekimi ARANMAZ — gemi dönmez, film boyunca TEK rejim mikrogravitedir.
⑧ Muhafızların K34 ve K60'ta "kaybolması" — kapakla ayrıldılar, ikisi de ayakta ve basınçlı bölmede.
⑨ Gölgelerin mutlak siyah OLMAMASI — gezegen/liman yansıması var (kapsamlı plan §6 kararı).
⑩ Kurulum sayısının 7-9 olması ve DÖNÜŞ'ün %40 altında kalması — ölçülmüş ve GEREKÇELİ sapma
   (PLAN §⑩④). Rapor "kesmeler kafa karıştırıyor" DERSE bulgu meşrudur; sayı tek başına kusur değil.
```

---

# B · KURGU KAPISI

```
GRID:            (yukarıda)                 CLIP COUNT: 96 · 960,000 s ±0
SAHNE İÇİ KESME: 71 (25 sahnenin içinde)    SAHNE SINIRI: 24
BÖLÜM SINIRI:    7 çift — K12↔K13 · K24↔K25 · K36↔K37 · K48↔K49 · K60↔K61 · K72↔K73 · K84↔K85
PART SINIRI:     3 çift — K24↔K25 · K48↔K49 · K72↔K73
                 ⛔ ② DEVAMLILIK bunları hiçbir part masterda yan yana GÖREMEZ → ELLE KARE:
                 ffmpeg -sseof -0.05 -i <part n> -frames:v 1 son.png
                 ffmpeg -i <part n+1> -frames:v 1 ilk.png     → yan yana bakılır
İNSAN ŞERİDİ
PLAN: ----1--1---1112171221314-36-41--33338----1--3-11-3---31-2624311-222--12251-1--5--11-33-33-----23
      (klip başına kadrajdaki İNSAN sayısı · `-` = 0 insan · K01–K04 kurgu bloğu, yeni kare 0)
VARLIK ŞERİDİ (Veyr · insan sayacına GİRMEZ):
      -----------------------VVV-VV---VVVV--------V----VV--V-----VV------V---V-----V------VV-VV------V
YÜZ ŞERİDİ (vizör ardında yüz kadrajda):
      -------------F---F-F-F--F----------F--------F-F--F---F------F-----------------F-----F--F------FF
      ölçüldü: 16/92 klip yüz taşıyor
SIRT ŞERİDİ (sırt kadrajda · D139 pozitif panel cümlesi bu kliplerde):
      ----B--B----B------------B--------B------B------------B-------B------B-B---B-----BB-B-----------
      ölçüldü: 14/92 klip sırt taşıyor
FİNAL VURUŞ KANITI: K92 · 0,0–10,0 s — son transfer aracının BURNU, GÖVDESİ ve KIÇ UCU daralmış
      açıklıktan tamamen geçer ve klip kıç ucu çıkana kadar KESİLMEZ; çevresinde ince açık pay
      kalır, alan kenarına temas YOKTUR. Bu kanıt yoksa doruk yoktur.
DÖNGÜ KANITI: K96 ↔ K85 — aynı araç içi kadraj; K85'te üçü yerleşir, K96'da el kalkar.
⭐ KESİLEMEZ KLİPLER: K11 (dört kenet) · K16 (çizik) · K23 (karar) · K32 (bedel) · K69 (sığmaz) ·
   K80 (ilk çıkış) · K89 (yerel kol) · K92 (doruk) · K93 (kapanış) · K95–K96 (selam)
```

---

# C · SAYISAL VE KİMLİK KİLİTLERİ

```
NOVUM:       SON GEÇİT — sabit halkanın içindeki etkin açıklık merkeze doğru MONOTONİK küçülür ve
             bu film süresince bir daha açılmaz. TAŞIYICI: açıklığın parlak kenarı × gövdenin
             sabit dairesel kesiti. TEK KARE: K69.
NOVUM SAYACI (metinsiz · monotonik · geriye BÜYÜMEZ):
             K49 gövdeden çok geniş → K64 hâlâ geniş → K69 gövdeden DAR → K87 takip araçlarından
             DAR → K92 araçtan bir parça geniş → K93 SIFIR
             ⛔ Rapor bu sırada bir geri büyüme görürse novum çökmüştür — BLOCKER.
KASK:        5 kimliğin 5'inde film boyunca KAPALI · vizör optik BERRAK, sıfır tint, yüz okunur
             [D79] · kubbe vizör 0 kare · opak/aynalı vizör 0 kare · kask çıkarma 0 kare
             ⛔ Vizör biçimi referans paketi R01–R06 ile karşılaştırılır; kubbe görülürse ÜRETİM DURUR.
SIRT:        sırt kadrajdaki 14 klipte tek parça düz panel [D139] · sırt ünitesi/tank 0 kare
KİMLİK DİZİSİ (pilot · her klipte aynı sırayla):
             ① saten kırık-beyaz seramik göğüs kabuğu ② eklemlerde şampanya altını çerçeve
             ③ sağ göğüste ÜÇ kabartma boş kaburga ④ TEK boyun halkası ⑤ ağır beyaz eldiven
AYIRT ETME (geometri · renk ikinci):
             omuz kaburgası 3 · boyun halkası insan 1 / Veyr 2 · parmak insan 5 / Veyr 4 ·
             vizör geniş (ekip) / dar (komutan) · kol bandı tek koyu kırmızı (komutan) ·
             omuz şeridi gri (ekip sorumlusu) · kol işareti kırmızı sağ/sol (G1/G2)
YOLCU SAYIMI (kapsamlı plan §8.2 · plan kontrolünün istediği "241 kişi"):
             240 tutsak = 239 yetişkin insan (Lina ve Edda dâhil) + erişkin Veyr
             + Mara (dışarıdan gelen kurtarıcı) = KURTULAN TOPLAM **241**
             M01–M15 her birinde 10 → 150 · M16–M23 her birinde 11 → 88 · M24'te 3
             K73'te Edda'nın raporu: M01–M23'te **238** yerleşti (150 + 88); M24'e 3 kişi
             ⛔ Promptta SAYI YAZILMAZ — kadrajda en çok 8 insan görünür; 241 bir
               MANİFEST sayısıdır ve post katmanında grafik olarak durur (plan §12.1).
BIRAKMA PROGRAMI (plan §8.3): M01 13:18 · sonraki her araç +4 s ·
             bırakma zamanı = 13:18 + 4 × (modül no − 1) · M24 **14:50**
             ortak yaklaşma/alan geçişi 24 s · M01 13:42 · M03 13:50 · M24 15:14
             ⭐ K80 sekizinci saniyesinde M01 ayrılır (klip 13:10–13:20) — TIMELINE'da yazılı
GEÇİT ÇİZELGESİ (plan §8.1 · azalan, geriye BÜYÜMEZ · promptta GEOMETRİK):
             K49 16 km · K52 ~9 km · K56 5 km · K61 ~1.200 m · K64 900 m (gemi sığar) ·
             K68 600 m · K69 420 m (SIĞMAZ) · K76 120 m · K80 ~80 m · K84 32 m ·
             K87 18 m (F1/F2 de geçemez) · K90 ~12 m · K92 8 m (6 m araç geçer) · K93 **0**
MONOTONİK SAYAÇLAR (üçü de geriye dönmez):
             ① açıklık: K49 → K93 sıfır
             ② ön kol çiziği: K16'da doğar, K17–K96 kadrajda, hiç ARTMAZ ve hiç KAYBOLMAZ
             ③ rayda kalan araç: 24 → K80'de 23 → … → K90'da 0
HAREKET KİLİDİ: film boyunca TEK rejim MİKROGRAVİTE. Bot güverteye kilitlenir, gövde raydan
             çekilir, bırakılan cisim aldığı hareketi sürdürür ve kendi ekseninde yavaş döner.
             ⛔ Yürüyen gövde + süzülen eşya AYNI KAREDE 0 kez. ⛔ İtki/darbe klipleri (K54 · K66)
             göreli hareketi ARACIN ivmesine bağlar, yerçekimi değişimine DEĞİL.
EKRAN YÖNÜ:  kaçış ekseni ekran solundan sağa · gövdenin burnu ekran sağına · geçit ekran sağında ·
             gezegenin fırtına lekesi ve gövdenin üst kaburgası aynı sahnede yön değiştirmez
İKİ GÖVDELİ GENİŞ KARE (V3): film boyunca TAM İKİ — K06 ve K92
⭐VİRAL ARA SAHNE: hedef YAZILMADI. Adaylar tek tek ÖLÇÜLECEK (yüz + duygu değişimi VE yüksek
             hareket enerjisi · §2.4): K20 · K22 · K45 · K54 · K61 · K67 · K85 · K96.
             ⚠️ Bu film §2.3'ün "bağımlı değişken yüz taşıyan klip sayısıdır" hipotezinin İLK
             berrak-vizörlü testidir: 16/92 klip yüz taşıyor (THE_LAST_TOW 5/48 ölçtü, sonuç 3).
```

---

# D · POLİTİKA VE ÜRETİLEBİLİRLİK

```
ŞİDDET SÖZLÜĞÜ (negatif blok DÂHİL · ⑯): gore · blood · corpse · wound · injury · kill · dead ·
  victim · weapon · gun · rifle · explosion · blast · flames · smoke · panic · trapped → 0/184
ÇOCUK SÖZLÜĞÜ: child · kid · boy · girl · young → 0/184
ÖZEL AD: Mara · Lina · Veyr · Edda · Aster · Neris → 0/184 prompt [D34]
METRİK ÖLÇÜ: NESNE/ÖLÇEK ölçüsü 0/184 — gemi boyu, açıklık çapı ve gezegen çapı promptta YOK,
  ölçek GEOMETRİK ilişkiyle yazılıyor [D138]. ⚠️ CAMERA satırı lens/mesafe/yükseklik ölçüsü
  TAŞIR ("85mm · 1.2 m from the helmet · height 1.55 m") — bu deponun standart kamera
  geometrisidir ve D138'in yüzey-işareti kalıbına girmez (kapı temiz)
MİLLİYET · GERÇEK KURUM · BAYRAK · RÜTBE HARFİ → 0/184
KALABALIK: "crowd" · "mass of figures" → 0/184 [red defteri #8]. İnsan kütlesi SAYILI ve AYRI:
  en büyük tek kadraj 8 insan (K37) · panik/koşma 0 klip · 31 klipte insan 0
İNSANSIZ KLİP: 31 klip · NEGATIVE bloğu < 900 karakter [⑯b · Cold Burn S8 yapısal red profili]
SİLAH: adlandırılmaz — "a short dark handheld unit" · atış PANELE/SİPERE gider, gövdeye 0 kez
PATLAMA: sayılı ve yerel [D38] · ateş topu · şok dalgası · mantar bulutu · gri toz sütunu 0 kare
```

---

# E · MAKİNE KAPILARI

```
DOĞRULANDI: prompt_kontrol.py 30.09.2026 · yatay_16_dk_filmler/THE_LAST_GATE · 184 prompt ·
            ⛔ 0 BLOCK · ⚠️ gerekçeli FIX (aşağıda) · image 101-246 · video 199-261 kelime

① kelime bandı        ✅ image 101-246 (100-250) · video 199-261 (120-300) — bant aşımı 0
㉖ IN FRAME           ✅ 184/184 promptta ilk satır
㉗ negatif tavanı     ✅ hiçbir blok 11 cümleyi geçmiyor
㉜ çok klipli sahne   ✅ plan toplamı 96 = 96 KLİP başlığı · beyan 25/25 doğru · zincir dili 0 ·
                      CONTINUOUS ACTION sahnenin 2.+ klibinde 68/68 klip (136 prompt) · LIGHT/PHYSICS/AUDIO birebir
㉙ hikâye onayı       ✅ ONAY 30.09.2026 · 25 sahne satırı · klip toplamı 96 · jargon 0
㉚ sahne tablosu      ✅ 96 klip satırı · 5 kilit klip dosyası (K01 · K32 · K49 · K92 · K96)
㉕ kilit tavanı       ✅ 20/20 ders kilidi + 7 UYGULANMAYAN satırı
㉔ SPEC tamlık        ✅ 7/7 makine çapası dolu (bu dosya)
⑩① ardışık kurulum   ✅ 0 çift — 92 klipte ardışık aynı kurulum yok
⑯ politika sözlüğü   ✅ TAM TARAMA 30.09.2026: 40 tetikleyici kelimenin HEPSİ 0/184 —
                      gore · blood · corpse · wound · dead · body/bodies · kill · injur · victim ·
                      weapon · gun · explosion · flames · smoke · panic · trapped · crowd · child …
                      ⭐ "crowd" ve "mass of bodies" NEGATİFİN İÇİNDEN de silindi [D123 · red #8]:
                      yerine malzeme tarifi ("spaced apart with clear deck between them")
⑰ B5                 ✅ İSTEK · ENGEL · BEDEL (klip no ile) · MUHATAP · AYRILIK
⑭ novum taşıyıcı     ✅ taşıyıcı TEK KARE satırında (K69)
D34 özel ad          ✅ "Mara" 0/184
D79 vizör/sırt       ✅ 7/8 bölüm dosyasında iki cümle de var

⚠️ GEREKÇELİ FIX — üretim durdurmaz, PLAN'da yazılı:
  ⑩④ DÖNÜŞ %8-33 (hedef %40) ve kurulum sayısı 7-9 (üst bant 6) · 7 bölüm dosyası
     → gerekçe PLAN §⑩④: on bir ayrı mekân + kapsamlı plan §13'ün açık talimatı.
       ÖLÇÜM RANDEVUSU: TAM FİLM ⑫ HOOK + ④ HİKAYE merceği.
  D79 vizör cümlesi BOLUM_1'de yok → K05-K12'de yüz taşıyan klip YOK (kurgu blokları + dış
     yanaşma); ㉖ gereği kadrajda olmayan yüz tarif EDİLEMEZ. Yapısal, düzeltilmez.
  ㉘ okuma çizelgesi → adım 2'de kapatıldı (aşağıya bak).
```

## ⬜ ÜRETİMDEN SONRA ÖLÇÜLECEK

```
⬜ klip süresi (ffprobe · ilk kabul klibi)        ⬜ 4 PART masterı + tam master
⬜ 12 mercek × 4 PART = 48 rapor + TAM FİLM ④⑫③  ⬜ ⑬ UYUM tek koşu
⬜ 3 part sınırı elle kare                        ⬜ ⭐viral 8 adayın ölçümü
⬜ POST-DUB replik tablosu (anlaşılırlık · zamanlama · senkron)
⬜ T01–T08 odaklı testlerin sonucu → URETIM_DEFTERI
```
