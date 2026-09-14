# 📋 THE_GREEN_CEILING — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretir: `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar; ad değişirse üçü birden körleşir.

> ⛔ **DİKEY FİLMSE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI ZORUNLUDUR**
> (08.09.2026'da ölçüldü). `rubrik_paketle.sh` filmin ailesini TEK bir satırla
> tespit ediyor:
> `AILE="yatay"; grep -qE "^## .*SAHNE SPESİFİKASYONU" "$SPEC" && AILE="dikey"`
> Başlık yoksa dikey film **YATAY sanılır** ve paket her merceğe YANLIŞ bloğu
> verir (① KARE'ye A+B+UYARI yerine A, ④ HİKAYE'ye B yerine A+UYARI…).
> ⚠️ Arıza SESSİZDİR: betik hata vermez, `aile: yatay` yazıp geçer — koşu
> sonunda kimse yanlış belgeyle bakıldığını fark etmez.
> Kontrol: betiğin son satırında `aile: dikey` yazdığını GÖZLE doğrula.
> ⭐ **BU FİLM YATAYDIR** (yatay_4_dk_filmler · 16:9) — o başlık bu dosyada
> BİLEREK YOKTUR ve eklenmemelidir; eklenirse paket yanlış bloğu dağıtır.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_GREEN_CEILING
FORMAT:            yatay 16:9 · 3-5 dk kartı (KILAVUZ_REHBERI §2.3)
RUNTIME:           249 seconds (title card: YOK — screen text lock 0,0 s)
SCENE COUNT:       25   (9 s hook + 24 × 10,0 s · klip süresi ARAÇTAN ölçüldü [D124])
THEME:             ENTROPİ — "Bu ormanda zemin hiçbir şeyi tutmaz."
                   ⛔ TANIM cümlesi; TAKAS kalıbı değil [TEMA §3c]
THEME SCENES:      S1 · S9 · S19 · S24     ⛔ en az üç (yazılmayan tema dekoratif)
                   kanallar: NESNE · KİNESİK (açık avuç) · IŞIK. KAMERA kanalı
                   bilerek BOŞ — 25/25 lockoff.
INTENDED EMOTION:  KAYGI (filmin imzası) · paylaşım yuvası S21'de HUŞU
                   ⛔ Aynı sahne ikisini birden taşımaz.
ENDING TYPE:       TWIST + TOHUM BİLGİ · son plan tipi NESNE EKİ (§2.2)
                   kapanış bütçesi S22-S24 = 3 sahne = %12 (band %8-12) ✓
                   açık kalan soru: 1
PROTAGONIST:       komutan — iki mürettebattan uzun olanı, kelepçeyi açan
                   (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S19 · 189 s · 3:09 — üç kasadan biri bırakılır
                   ⛔ HESAPLATILDI [D122]: 9 + (19−1) × 10 = 189 s
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
                   SES DURUMU **STATE B** — sessiz ve TASARIMLI; ses kanalı VAR
                   ve DOLU. ⛔ "AUDIO ABSENT" ile karıştırılmaz [D136].
SILENT SCENES:     müziksiz sahne 1 → **S21** (209-219 s). Müzik 207,5 s'de
                   BİTER (sahne başlamadan 1,5 s önce). ⛔ Sessiz DEĞİL
                   müziksiz: nefes sürer, motor sahnenin son 1,5 s'sinde
                   kesilir [D83]. ⛔ Kurguda HARD MUTE, video modelinden
                   İSTENMEZ [D180] → E BLOĞU KAPI ③.
VIRAL INTERSTITIALS: S9 (KAYGI · 89 s) · S17 (KAYGI · 169 s) · S21 (HUŞU · 209 s)
                   ⛔ THESE MAY NOT BE CUT
                   ⭐ Üçü de YÜZ + HAREKET satırı taşır [SENARYO §2.4].
KESİLEMEZ (tam liste): S0 · S5 · S9 · S19 · S20 · S21 · S23 · S24
                   ⛔ S0 kapak anını taşır: düşerse elde tıklamayı karşılamayan
                     bir kapak kalır.
TITLE:             platform başlığı **"The Forest Falls Upward"** — izleyiciye
                   NEREYE bakacağını söyler, ne olduğunu söylemez. Kapak
                   HANGİ NESNE der; ikisi aynı şeyi tekrar etmez.
LIBRARY CONTEXT:   aynı raftaki kardeş film **THE UPWARD FALL** (02.09.2026) —
                   aynı ortam kartı (§3.4 · 3,2 atm · 0,42 g · kapalı kanopi),
                   ZIT kural: orada ölü doku ağırlığını kaybeder, burada zemin
                   bıraktığını yukarı verir. ⚠️ Mercek iki filmi karıştırırsa
                   ayrım şudur: orada tek astronot ve canlı sistem var, burada
                   iki mürettebat ve 0 canlı.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme **0**
TARGET ASL BAND: 9,96 s (249 ÷ 25) · ASL CURVE: **DÜZ — eğri YOK**
                 ⛔ GEREKÇE SATIRI [D74 · KURGU_RITMI §1]: bu film SABİT
                 IZGARALIDIR ve ızgara bir tercih değil ARACIN ölçüsüdür
                 [D124]. ASL eğrisi klip süresini değiştirmekle yapılır;
                 burada değişebilecek tek şey klip süresi DEĞİL, kurulum
                 dizisidir. Ritim bu yüzden ASL'den değil KURULUM
                 İSKELETİ'nden gelir: KÜME nefes verir, DÖNÜŞ tanıdıklık
                 verir, ölçek kademesi hızlanma hissini taşır.
                 ⛔ Merceğin "ASL sabit → ritim yok" bulgusu bu satır
                 yüzünden DÜŞER; kaynağı burada YAZILI.
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10,0 s klip
                 S0=0 · S5=49 · S9=89 · S12=119 · S13=129 · S17=169 ·
                 S19=189 · S20=199 · S21=209 · S22=219 · S23=229 · S24=239
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     50 prompt → 25 kabul edilen klip · TRIM BUDGET: 0,0 s
                 ⛔ Sabit ızgarada trim YOKTUR: klip 10,0 s'den uzunsa
                   KABUL EDİLMEZ, kırpılmaz — kırpma novum hızını bozar.
SCREEN TEXT:     0,0 saniye
                 ⛔ Kapak çıktısı ve TikTok ekran metni bu sayıma DÂHİL
                   DEĞİLDİR: ikisi de master'ın DIŞINDADIR [D70 · D72 · D34].
CAMERA:          0 pan · 0 tilt · 0 zoom · 0 track / **25 sahnenin 25'i sabit lockoff**
SETUP SEQUENCE:  A 32mm WS düz göz hizası 1,5 m 0° · B 75mm MS 3/4 60° ·
                 C 100mm MACRO düz 200° · D 32mm EWS ALT AÇI 0,4 m 250° ·
                 E 75mm MWS yan 110° · F 32mm WS ÜST AÇI 10 m 0° ·
                 G 50mm MCU arkadan omuz 0° · H 32mm MS yan cam 90° ·
                 I 32mm EWS yan 180° · J 50mm CU kol hizası 300° ·
                 K 32mm WS üç-çeyrek 30 m 150° (araç DIŞI · kalkış) ·
                 L 50mm MS raf hizası 90° · M 50mm MWS kamera HEDEFTE 20°
KURULUM İSKELETİ: A B A B D C D F F D E E E G K G H D H J H D I M L
                 ⛔ PLAN'daki satırla BİREBİR aynıdır; farklıysa biri yanlış.
KÜME:            2 ≥2 ✓  — #1 S7-S8 (F, iki klip) · #2 S10-S12 (E, üç klip)
DÖNÜŞ:           10 / 24 = **%41,7** ≥%40 ✓
                 S2←S0 · S3←S1 · S6←S4 · S8←S7 · S9←S6 · S11←S10 · S12←S11 ·
                 S15←S13 · S18←S16 · S20←S18
                 kayıt: S17←S9 (gap 8) ve S21←S17 (gap 4) dönüş SAYILMAZ
                 (kaynağından >3 sahne sonra) ama kamera metni yine BİREBİR
                 kopyalanır.
ANGLE ARC:       5 açı TİPİ ≥3 ✓ — düz göz hizası · ALT açı · ÜST açı · 3/4 ·
                 makro (+ "kamera hedefte" altıncı tip olarak sayılmadı)
KURULUM SAYISI:  13 (A-M) — ACI_YAYI §4 bandı 25 sahnede ≤12; ⚠️ BİR ÜSTÜNDE,
                 D74 gerekçesi PLAN §SAHNE HARİTASI'nda yazılı (10.09.2026:
                 kalkış vuruşu araç DIŞINDAN görülecek → K açıldı)
BİLİNÇLİ ŞOK:    1 ≤2 ✓ — S21→S22 (ortam sınırı: kalın atmosfer → vakum).
                 Ölçek kademesi BİLEREK korundu: iki EWS yan yana konunca
                 izleyici aynı ölçekte İKİ AYRI DÜNYA görür.
BÖLÜM KESİĞİ:    S12 ↔ S13 · köprü tipi IŞIK GEÇİŞİ (4200 K → 3200 K)
                 ⛔ Bölüm sınırı da ardışık bir ÇİFTTİR ve denetlenmiştir.
DORUK:           S21 → 209 s = 3:29 (sahne başlangıcı 209 s)
                 ⛔ HESAPLATILDI [D122]: 9 + (21−1) × 10 = 209

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Bu filmde replik 0'dır → tablo BOŞ. Boşluğun sebebi kayıt altındadır:
   KART 7 kapatıldı, bedeli ve telafisi PLAN'ın politika tablosunda yazılı.

FİNAL VURUŞ KANITI [D141]:
   nesne: **kelepçe** ve **yük kasası** · saniye: **245 s** ·
   kaç tane: **tam 3 kelepçe · tam 2 kasa** · **BULUNMAYAN** (üçüncü kelepçe
   kapalı ama BOŞ — eksik olan şey sayılabiliyor)
   ⛔ tek karede sayılabilir ve adı konabilir; "final duygusu" değil
   ffmpeg -ss 245 -i "$M" -frames:v 1 kanit.jpg   → BAK
   ⚠️ 245 s S24'ün içindedir (239-249 s); sahne sınırına düşmez.

DÖNGÜ KANITI: ⛔ BU FİLMDE DÖNGÜ YOK — çift tipi **KAFİYE** (§1: 3-5 dk bandı
   kafiye ister, döngü değil). Ölçülecek olan şudur:
   ilk kare (S0) ve son kare (S24) AYNI kompozisyon yuvasını taşır — açık avuç
   kadrajın SOL ALT üçte birinde. Kurulum, ölçek, ışık ve palet BİLEREK
   FARKLIDIR (A 32mm WS orman ↔ L 50mm MS kabin rafı).
   DEĞİŞEN TEK DEĞİŞKEN: ② NESNE — S0'da avucun ÜSTÜNDE bir levha VAR ve
   gidiyor, S24'te avucun ALTINDAKİ kelepçe BOŞ. Foveal merkezde. ✓
   ⛔ Mercek "ilk ve son kare aynı değil" derse bulgu DÜŞER: kaynağı burada.

⭐ SIFIR KİLİTLERİ [D156] — hepsi ÖLÇÜLEBİLİR, hiçbiri "dikkat edilecek":
   replik ................ 0     → ③ SES · ffprobe konuşma yok
   sahne içi kesme ....... 0     → ① KARE cat.6 · E BLOĞU KAPI ②
   ekran metni ........... 0,0 s → ① KARE cat.10 · E BLOĞU KAPI ⑤
   kamera hareketi ....... 0     → ⑨ KADRAJ cat.2 · E BLOĞU KAPI ②
   canlı (insan dışı) .... 0     → ⑤ ARKA PLAN
   patlama / alev topu ... 0 kare→ ⑦ AKSİYON
   su kütlesi ............ 0     → ⑥ FİZİK (damla VAR, kütle YOK)
   asılı toz perdesi ..... 0 kare→ ⑥ FİZİK cat.5
   biniş/iniş hareketi ... 0 kare→ ② DEVAMLILIK · her klibin ilk 0,6 s'si
   üçüncü figür / klon ... 0     → ② DEVAMLILIK cat.12
   milliyet/kurum/kişi adı 0     → ⑯ politika sözlüğü (betik)
   ⛔ Bir mercek bu satırlardan birini "eksik" diye yazarsa bulgu DÜŞER —
     eksiklik TASARIMDIR ve bedeli PLAN'ın politika tablosunda ödenmiştir.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  2 2 2 2 2 1 2 2 2 2 2 2 - 2 - 2 - - - 2 2 - - - 2
       (2 = iki figür · 1 = tek figür ya da tek uzuv · - = insansız)
       S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20 S21 S22 S23 S24

SAYIM: iki figürlü 16 sahne · tek uzuvlu 1 (S5) · insansız 8
       (S12 · S14 · S16 · S17 · S18 · S21 · S22 · S23)
⛔ Kurgu kapısı bu diziyi EKRANA KARŞI okur [D118 · D163]. Slot kayması
  doruğun yuvasını kaydırır: THE UPWARD FALL'da 19/20 ters çıktı ve ders
  oradan yazıldı.
⚠️ Doruk (S21) İNSANSIZDIR ve bu bilinçlidir — huşu yuvasında ölçek
  kontrastı 1:10, figür kadrajda olsa ölçek düşer.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 2 · film boyunca sabit. S5'te 1 uzuv, sekiz sahnede 0.
              ⭐ AYRIM EKSENİ GEOMETRİDİR, renk DEĞİL [D86 · D167]:
                komutan = uzun · DÜZ sırt + tek dikey dikiş + paket YOK ·
                  KIRMIZI şerit SAĞ önkol ve SAĞ uyluk · SOL bilekte analog
                  gösterge · screen-LEFT
                mühendis = kısa · DİKDÖRTGEN sırt bloğu + altında U profil
                  (silüet kare ve ağır okunur) · ELEKTRİK MAVİSİ şerit SOL
                  pazı ve SOL uyluk · bilekler çıplak takı yok · screen-RIGHT
              ⛔ Pencere başına EN ÇOK 3 kişi özniteliği [D167].
KASK          4 kutu lamba TAÇTA · vizör TEK ön cam, görünür çerçeve ve conta,
              optik BERRAK, sıfır tint, aynasız kaplama YOK, kubbe YOK, HUD YOK
              ⛔ `seamless` kelimesi 50 promptun 50'sinde 0 geçiş [D79·D95·D146]
              ⛔ Hiçbir sahnenin eylemi "çıkarmak" değil [D89] — vizör 25/25 kapalı
              ⚠️ D79'un "sırt ünitesi YOK" satırı bu filmde YALNIZ KOMUTAN için
                geçerlidir; mühendisin sırt bloğu AYRIM KİLİDİDİR ve 25/25
                sahnede aynıdır. İkisini aynı kurala sokan bulgu DÜŞER.
NOVUM         KURAL: kapalı kanopi bir kapak gibi çalışır; fırtına YATAY değil
              DİKEYDİR ve zemin bıraktığını geri vermez — YUKARI verir.
              İHLAL: yalnız BU. İhlal sayısı 1; yanındaki her şey (giysi, kask,
              iniş aracı, gemi, egzoz, kütle, atalet) NORMAL fizikle davranır.
              MEKANİZMA: Arşimet + sürükleme, anti-gravite DEĞİL — bu yüzden
              negatif çekirdeğin "never hovering" yasağıyla çakışmaz.
              TAŞIYICI: düz gri YÜK KASASI × avuçtan bırakma jesti [D157]
YERÇEKİMİ     0,42 g · 25/25 sahnede aynı
ATMOSFER      S0-S21: 3,2 atm ≈ 3,9 kg/m³ · solunamaz · §3.4 KALIN ATMOSFER
              S22-S24: vakum · §3.1
              ⛔ SINIR SAHNESİ S21'dir ve S21'de §3.4 GEÇERLİDİR (araç hâlâ
                atmosferin içindedir). "S21 vakum" bulgusu DÜŞER.
              §3.4 imzaları: toz HIZLI çöker ve KÜMELENİR (asılı perde 0 kare) ·
              gölge yumuşak kenarlı ama DERİN · dolgu ÇOK GÜÇLÜ ve motivasyonlu ·
              ses GÜÇLÜ/ALÇAK/YAKIN · egzoz KISA + KALIN koni (D36 TERSİNE) ·
              yatay rüzgâr YAVAŞ, kimseyi savurmaz · kaldırma GERÇEK
              §3.1 imzaları: toz 0 kare · gölge mutlak siyah · dolgu YOK ·
              dış ses 0 kare (yalnız gövdeden iletilen) · egzoz DÜZ KESKİN koni
EKRAN YÖNÜ    HEDEF hep **YUKARI** (kanopi → tavandaki açıklık → gemi);
              zemin işi ilerlemesi hep **SOLDAN SAĞA**.
              DİZİLİM: komutan screen-LEFT · mühendis screen-RIGHT — iki figürün
              birlikte olduğu **16 sahnenin 16'sında** sabit, ters dönüş 0.
              ⛔ Yön kadraj koordinatına değil KADRAJDAKİ NESNEYE bağlanır
                [D104 · D174]: "araca doğru" değil, "rampanın dibindeki rafa".
SAYAÇ         **çevresel · monotonik · 0 ekran · 0 rakam · 0 kadran** [D50·D78]
              kanopi ışık lekesi:
                S0-S1 = 15 · S2-S3 = 8 · S4-S5 = 3 · S6 = 1 · S7-S12 = 0
              ⛔ MONOTONİK: sayı hiçbir sahnede ARTMAZ. Klip İÇİNDE de
                değişmez — fark yalnız SAHNE SINIRINDA doğar [ara durum yasağı].
              ikinci kanal: tavandaki açıklık S17'de KÜÇÜK → S21'de kadrajı
                dolduruyor (aynı yönde, tek eksende)
EŞ KADRAJ     S0 ↔ S24 (çift · KAFİYE · konum kilidi: avuç SOL ALT üçte bir)
              + aynı harfin her tekrarı eş kadrajdır: A S0/S2 · B S1/S3 ·
              D S4/S6/S9/S17/S21 · E S10/S11/S12 · F S7/S8 · G S13/S15 ·
              H S16/S18/S20 · K tek kullanım (S14) → eş kadrajı YOK
              ⛔ Aynı harfte kamera metni BİREBİR kopyalanır + işaret satırı;
                metin farklıysa kurulum tutmaz.
YIPRANMA      **3 sabit bölge · MONOTONİK · kabinde SIFIRLANMAZ** [D42·D147·D84]
              K0 (S0-S3) kuru kabuk → K1 (S4-S9) kabuk üstünde kesintisiz ıslak
              parlaklık → K2 (S10-S24) ıslak parlaklık + eklemlerde koyu lif
              ⛔ Kapak kapandıktan sonra (S12) ıslaklık AZALMAZ. "Kabinde
                temizlendi" bulgusu DÜŞER — kilit budur.
IŞIK TAKVİMİ  **MONOTONİK · tek yönde** [D192 · D193]
              KANAL 1 kanopi: 15 → 8 → 3 → 1 → 0 (S0 → S7), sonra kapalı
              REJİM 2 kabin: S12'de kapak kapanır, 4200 K → 3200 K (bölüm köprüsü)
              REJİM 3 egzoz: S14'te araç DIŞINDA ikinci gerçek kaynak olarak
                doğar (kanopi dolgusu saat 12'de durur), S15'ten itibaren
                kabinde baskın kaynak olur, S18-S20'de zayıflar
              REJİM 4 vakum: S22'den itibaren TEK GÜNEŞ, sabit yön, sert gölge
              KAFİYE: S0'da kanopiden inen tek kaynak ↔ S24'te tavandan inen tek kaynak
              ŞİMŞEK: 1 deşarj · 0 dal · bilek kalınlığından İNCE · <0,2 s ·
                artık ışık 0,4 s · saat 12 yönünde (S4 · S6 · S9 · S17)
              ⛔ Şimşek POZİTİF biçimle yazıldı; "no lightning bolt" negatifi
                aynı sahnede YAZILMAZ [D192'nin ölçülmüş çelişkisi].
SES REGISTER  HUMAN 0 · MACHINE 0 (replik yok)
              ORTAM YATAĞI 4 bölge, kurguya TEK PARÇA serilir [D83]:
                Z1 orman S0-S9 · Z2 kabin S10-S13 · Z3 tırmanış S14-S21 ·
                Z4 vakum S22-S24
              sert ses kesmesi EN ÇOK 3 ve hepsi yazılı: S12 (dış ses kesilir) ·
                S21 sonu (motor kesilir) · S23 (temas knock'u)
              ⛔ Mutlak dijital sıfır bir HATADIR — nefes S21'de bile sürer.

⭐ ⑤ ARKA PLAN'a verilecek ÜÇ KİLİT [D133 — YALNIZ bu üçü]:
SABİT ÇEVRE ① en büyük arka plan nesnesi ADLANDIRILIR, ölçek şahidi yazılır:
              gövdeler — düz, dikey oluklu, ~20 gövde boyu çapında, kadrajın
              iki kenarından da çıkar; kapalı yaprak tavanı zeminden ~170
              gövde boyu yukarıda [D145 · D126]. Zemin TEK CÜMLE TEK RENK:
              kesintisiz koyu kırmızı-kahve düşmüş lif matı [D176], 25/25 aynı.
MESAFE/ÖLÇEK ② yürüyüş mesafesi: 10 saniyede ~10 m (0,42 g'de ~1,0 m/s) —
              S7 ve S8 aynı ÜST AÇI kurulumunda, iki figür arası mesafe S7'de
              sabit, S8'de AÇILIR; ölçek şahidi her iki karede de gövde çapıdır.
ÇEVRESEL SAYAÇ ③ yükselen nesne sayısı SAYILIR ve monoton azalır: S9 = tam 10
              yaprak levhası + 1 bot + 1 kazık · S16 = tam 6 · S18 = tam 3.
              Hepsi ~1 m/s sabit, kadrajı ≤3 s'de terk eder, 0 kare duraklama
              [D143 · D127].
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.
> ⛔ Aşağıdaki yedi kapının yedisi de **10.09.2026'da ffmpeg 8.1 ile KURU
> KOŞUYLA** çalıştırıldı (sentetik test klibi üstünde); komutlar kopyalanır,
> `$M` master dosyasıdır.
> ⚠️ **`vidstabdetect` BU MAKİNEDE YOK** — kuru koşu bunu yakaladı ve KAPI ②
> doğrudan İKAME ile yazıldı. D142'nin vakası tam buydu.

```
KAPI ①        SES KANALI VAR MI — STATE B'nin teslim kanıtı [D136]
KOMUT         ffprobe -v error -select_streams a -show_entries stream=codec_type \
                -of csv=p=0 "$M"
BEKLENEN      "audio"   ⛔ çıktı BOŞSA 🔴 TESLİM KUSURU — sessiz tasarım ile
              ses kanalı olmaması aynı şey DEĞİLDİR
DOĞRULANDI    ffprobe 8.1 · 10.09.2026 · kuru koşu çıktısı: audio
İKAME         ffprobe yoksa: ffmpeg -i "$M" 2>&1 | grep "Stream.*Audio"
```

```
KAPI ②        KAMERA SABİT Mİ + SAHNE İÇİ KESME VAR MI (tek kapı, iki ölçü)
KOMUT         ffmpeg -hide_banner -nostats -loglevel error -i "$M" \
                -filter:v "scdet=threshold=10,metadata=print:key=lavfi.scd.score:file=-" \
                -f null - | grep -B1 "score=[1-9]" > kesme.txt
BEKLENEN      Yüksek skorlu kare sayısı **TAM 24** ve hepsi ızgara sınırında
              (9 · 19 · 29 … 239 s, ±0,08 s). 25. bir spike = sahne İÇİ kesme
              ya da kamera sıçraması → 🔴. Izgara dışı spike YOK.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · kuru koşuda `lavfi.scd.score` satırları
              gerçekten basıldı (0.000 / 0.883 …)
İKAME         ⛔ `vidstabdetect` BU MAKİNEDE KURULU DEĞİL (kuru koşu:
              `ffmpeg -filters | grep vidstabdetect` → boş). Yerine ikinci
              ölçü olarak kare-arası fark:
                ffmpeg -hide_banner -nostats -loglevel error -i "$M" \
                  -filter:v "tblend=all_mode=difference,signalstats,\
metadata=print:key=lavfi.signalstats.YAVG:file=-" -f null - > fark.txt
              Lockoff filmde YAVG yalnız 24 ızgara sınırında sıçrar; sahne
              ortasında sıçrama = kamera hareketi. (Kuru koşu ✅)
```

```
KAPI ③        S21 GERÇEKTEN MÜZİKSİZ MÜ — planlı sessizliğin kanıtı [D180]
KOMUT         ffmpeg -hide_banner -nostats -i "$M" \
                -af "silencedetect=noise=-60dB:d=0.5" -f null - 2>&1 | grep silence
BEKLENEN      ⚠️ Bu kapı MUTLAK SESSİZLİK ARAMAZ — S21'de nefes ve (ilk 8,5 s)
              motor vardır. Beklenen: MÜZİK yatağının kesilmesi. Ölçü şudur:
                ffmpeg -hide_banner -nostats -loglevel error -i "$M" \
                  -af "astats=metadata=1:reset=1,ametadata=print:\
key=lavfi.astats.Overall.RMS_level:file=-" -f null - > rms.txt
              → 207,5 s'de RMS BASAMAK HÂLİNDE düşer (fade DEĞİL, tek kare
              içinde) ve 209-219 s bandı film ortalamasının belirgin altında
              kalır. ⛔ 207,5 s ± 0,2 s dışına düşerse doruk kaybedilmiştir —
              iki film üst üste tam bunu kaybetti.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · silencedetect kuru koşusu 1,0-2,5 s
              arasına gömülen sessizliği bildirdi (silence_start: 1.002729 ·
              silence_end: 2.517271); astats RMS satırları da basıldı
İKAME         Her ikisi de yoksa: 209 s ve 219 s'de 1'er saniyelik parça
              çıkarılır (ffmpeg -ss 209 -t 1 -vn -f wav) ve kulakla dinlenir
```

```
KAPI ④        LOUDNESS — teslim eşiği
KOMUT         ffmpeg -hide_banner -nostats -i "$M" -filter:a ebur128=peak=true \
                -f null - 2>&1 | tail -14
BEKLENEN      I ≈ −14 LUFS (±1) · LRA makul · true peak ≤ −1,0 dBTP
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · kuru koşu Summary bloğunu bastı
              (Integrated / LRA / Threshold satırları geldi)
İKAME         ebur128 yoksa: astats ile Overall.RMS_level ve Peak_level okunur
              ve hedefe göre elle kazanç verilir
```

```
KAPI ⑤        EKRAN METNİ 0,0 s — ölçü DEĞİL, GÖZ; ama örneklem MAKİNEYLE alınır
KOMUT         mkdir -p kare && ffmpeg -hide_banner -loglevel error -i "$M" \
                -vf "fps=1" kare/%03d.jpg
BEKLENEN      249 kare · içlerinde okunabilir harf/rakam/altyazı/başlık kartı/
              filigran **0 adet**. Köşe testi [D150]: her karenin dört köşesi
              de temiz.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · `fps=1` kare çıkarma kuru koşuda çalıştı
İKAME         ⛔ Metin tespiti için ffmpeg filtresi YOKTUR ve uydurulmaz.
              Bu kapı bilerek YARI-MAKİNEDİR: örneklemi makine alır, kararı
              insan verir. 249 kare bakılabilir bir sayıdır.
```

```
KAPI ⑥        KOYU-ÜSTÜNE-KOYU — siyah giysi + koyu orman zemini riski
KOMUT         ffmpeg -hide_banner -nostats -loglevel error -i "$M" \
                -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX:file=-" \
                -f null - > ymax.txt
              (aynı komut YMIN için de koşulur)
BEKLENEN      Her karede YMAX − YMIN ≥ **110**. Altına düşen kare = figür
              zeminden ayrılmıyor. ⚠️ S22-S24 (vakum) doğal olarak en yüksek
              farkı verir; risk S13-S21 kabin bloğundadır.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · YMAX satırları basıldı (232 · 216 …)
İKAME         signalstats yoksa: her sahneden 1 kare alınır ve histogram
              filtresiyle bakılır (ffmpeg -vf histogram)
```

```
KAPI ⑦        KLİP IZGARASI — 25 klip × 10,0 s (+ 9 s hook)
KOMUT         for f in klipler/*.mp4; do \
                printf "%s " "$f"; \
                ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"; \
              done
BEKLENEN      Hook klibi 9,0 s · kalan 24 klibin 24'ü 10,0 s (±0,05).
              Toplam = 249,0 s. ⛔ Uzun klip KIRPILMAZ, YENİDEN ÜRETİLİR.
DOĞRULANDI    ffprobe 8.1 · 10.09.2026 · kuru koşu 3,000000 döndürdü
İKAME         ffprobe yoksa: ffmpeg -i "$f" 2>&1 | grep Duration
```

```
⛔ SEKİZİNCİ BİR KAPI YAZILMADI VE SEBEBİ KAYITLI: "iki figürün ayrımı"
  makineyle ölçülemez. Ayrım GEOMETRİKTİR (düz sırt ↔ U profilli blok) ve
  hiçbir ffmpeg filtresi bunu saymaz. Bu eksen ② DEVAMLILIK merceğine MOD D
  ile verilir ve C BLOĞU'nun İNSAN satırı onun ölçüsüdür.
  ⭐ Uydurma kapı yazmak, kapıyı hiç yazmamaktan kötüdür [D142].
```
