# 📋 THE_FALLING_WORLD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_FALLING_WORLD_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ⚠️ **DİKEY FİLMDE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI — artık MAKİNE KAPISI
> DEĞİL.** Bu başlığı yalnız `rubrik_paketle.sh` okuyordu (aile: yatay/dikey) ve
> o betik 11.09.2026'da silindi. Başlık yazım geleneği olarak KALABİLİR; hiçbir
> betik ona bakmaz, yokluğu artık sessiz bir arıza üretmez.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri (hedef dilimi · hareket yönü · eksen) + A  MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⭐ 14.09.2026: ⑭/⑮ için C bloğuna yazılacak satırlar — `HAREKET KİLİDİ:` (eller/ayaklar/baş ne
   yapar, "tek jest" kuralı) ve `EKRAN YÖNÜ:` (hedef hangi dilimde · figür hangi yöne · eksen
   çizgisi — screen-left/right, pusula yok). Yoksa iki mercek çıkarımla koşar ve bunu yazar.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_FALLING_WORLD
FORMAT:            horizontal 16:9 · 8 minutes · 48 scenes · 4 part files
RUNTIME:           480 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       48
PART GRID:         B1 = S00-S11 · 12 clips · 0-120 s · B2 = S12-S23 · 12 clips · 120-240 s ·
                   B3 = S24-S35 · 12 clips · 240-360 s · B4 = S36-S47 · 12 clips · 360-480 s
                   QA her BÖLÜME AYRI koşar; rubriğe SPEC'le birlikte
                   "THIS FILE IS PART n OF 4 — scenes S.. to S.., .. to .. seconds" beyanı yapıştırılır.
                   BOUNDARY PAIR S11↔S12 · S23↔S24 · S35↔S36 — üçü de elle kareyle kapanır.
THEME:             TRUST — the man who carries his partner at the start hands his own life to him at the end
THEME SCENES:      S00 S02 S24 S29 S41 S46     (6 ≥ 3 ✅)
INTENDED EMOTION:  held breath — will the ground last long enough for both of them
ENDING TYPE:       closed with one open end — both men are aboard, the planet keeps going
PROTAGONIST:       unnamed — identified only by suit colour; no proper name appears in
                   any prompt, any Bible or this SPEC [D34]
CENTRAL CHOICE:    S41 — he lets go of the sill and puts his weight in the other man's glove
DIALOGUE LINES:    0 in the clips · POST-DUB LINES: 8 · register: HUMAN 8 / MACHINE 0
                   ⛔ No line is produced inside any clip: the prompts carry no quotation
                   marks (OMNI rule) and no mouth is ever in frame (opaque panes).
                   The eight lines are dubbed onto the master; their seconds are in
                   THE_FALLING_WORLD_MUZIK.md, computed with the grid formula [D122].
SILENT SCENES:     40 of 48
VIRAL INTERSTITIALS: S00 · S13 · S25 · S35 · S41 · S45  ⛔ THESE MAY NOT BE CUT
TITLE:             promises a physical problem with a deadline — a planet coming apart under two people
LIBRARY CONTEXT:   KRONOS_SON_SINYAL · BENI_HATIRLAMA · SUSMAYAN_NOBETCI (same 8 min shelf) ·
                   YERCEKIMI (two-figure precedent) · THE_LAST_SPAN (closest concept)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      48
SHOT COUNT:      48 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s sabit   ASL CURVE: düz — ızgara sabit
                 GEREKÇE [D74]: sahibin sert kısıtı "48 sahne × 10 saniye = 8 dakika".
                 Ritim ASL ile değil KURULUM DEĞİŞİMİ ve TEMPO ŞERİDİ ile taşınır
                 (03_SAHNE_SIRALAMASI §2 tempo satırı: en uzun tek-harf serisi 3).
GRID:            sahne başlangıcı(n) = n × 10 s   (hook S0'ın İÇİNDE; hook 10 s · klip 10 s)
RUNTIME:         480 s = 08:00
RAW FOOTAGE:     48 kabul klibi × 10 s = 480 s · TRIM BUDGET: 0 s (ızgara sabit)
SCREEN TEXT:     0,0 saniye
CAMERA:          48 / 48 sabit lockoff (araç içi iki kurulum araca monte — kameranın
                 kendi hareketi sıfır)
SETUP SEQUENCE:  A B B A C E E C F G F F I I K K L L K M N O N P R M Q M Q R S T S U V V W W X W U X Y Z Z S Z H
KURULUM İSKELETİ: A B B A C E E C F G F F I I K K L L K M N O N P R M Q M Q R S T S U V V W W X W U X Y Z Z S Z H
KÜME:            9 küme ≥2 ✅ — S1-S2 · S5-S6 · S10-S11 · S12-S13 · S14-S15 · S16-S17 ·
                 S34-S35 · S36-S37 · S43-S44
DÖNÜŞ:           20 / %41,7 ≥%40 ✅ — S2 S3 S6 S7 S10 S11 S13 S15 S17 S18 S22 S27 S28 S32
                 S35 S37 S39 S41 S44 S46
ANGLE ARC:       4 açı TİPİ ≥3 ✅ — low angle · high angle · eye level · profile
KURULUM SAYISI:  24 (48 sahne bandının tavanı 24 — tavanda)
DORUK:           S41 → the off-white glove leaves the sill and his weight goes into the
                 orange glove (sahne başlangıcı 410 s · kapak anı 414 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Yazılan her kayıt formülle DOĞRULANIR; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   cabin lights in the ship's flank · 478 s · tam 2 · BULUNAN
   ⛔ ikinci sayım: gemi kadraj eninin 1/3'ünü GEÇMEZ (gerçekleşen %8,9)
   ⛔ tek karede sayılabilir ve adı konabilir olmalı; "final duygusu" değil
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: ilk kare ↔ son kare — aynı kurulum · ölçek · ışık · jest mi
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111111111111111111111--1-
       (1 = insan var · - = insansız · sahne başına bir karakter · S00-S47)
       İNSANSIZ: S45 (kalkış · gemi) · S47 (kapanış · gemi) — ikisinde de kadrajda
       insan gövdesi yok; NEGATIVE blokları <900 karakter ve "no human figures"
       kalıbı YAZILMADI [KART 10 · yapısal red profili]
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         2 — off-white suit SOL üçte bir · burnt-orange suit SAĞ üçte bir · 48/48
              merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
KASK          KAPALI ve TAMAMEN OPAK — 48/48, istisna YOK.
              ⛔ D79 SAPMASI [PLAN D74 ③]: vizör tasarım gereği opaktır, "optik berrak"
              cümlesi HİÇ yazılmadı ve yazılmayacak; sahibin sert kısıtı.
              ⛔ D79/D139 SAPMASI [PLAN D74 ⑦]: İKİ FARKLI SIRT ÜNİTESİ var ve kalıcı —
              kimlik taşıyıcısıdır. D139'un asıl talebi karşılandı: sırt POZİTİF yüzey
              cümlesiyle yazıldı (bir sürekli kaburgalı yüzey) ve ünite onun ÜSTÜNE monte;
              NEGATIVE'de sırt çantası / hortum / kablo yasağı duruyor.
NOVUM         KURAL: bu dünyada kimse kendini kurtaramaz; her kurtuluş, birini bağlayan
              hattın BAŞKASI tarafından ayrılmasıdır.
              TAŞIYICI: sarı emniyet halatı
              İHLAL: S39'da BEYAZ kendi hattına uzanmayı dener ve UZANAMAZ — kural burada
              ihlal edilemez olduğunu gösterir; S42'de kural TURUNCU'nun elinde işler.
              KURULUM S01-S02 · DOĞRULAMA S25-S27 · SONUÇ S42 (2 nesne, 3 sonuç)
YERÇEKİMİ     0,30 g — dış ve iç hacimde AYNI [PLAN D74 ②]
ATMOSFER      İNCE (§3.2) — ses VAR ama boğuk ve yüksek frekanssız; toz SÜTUN hâlinde
              yavaş ama KESİN oturur; gölge kenarları YUMUŞAK (vakum değil)
EKRAN YÖNÜ    hedef hep SAĞDA (gemi yönü) · ilerleme SOLDAN SAĞA — 47/48 sahnede sabit;
              tek istisna S06 (araç sağa kırıp ocağa iner, OLAY gerekçeli), S08'de yön döner
SAYAÇ         iki kanal, ikisi de monotonik:
              ① KAYBEDİLEN ZEMİN S05 → S10 → S13 → S18 → S30 → S35 → S45 (7 kademe, geri dönüş yok)
              ② ÇALIŞAN TUTUNMA NOKTASI 2 kol (S00-S15) → 1 kol (S16-S36) → 1 el (S37-S40) → 0 (S41)
EŞ KADRAJ     S11↔S12 (F→I · 1 kademe · mekân değişir) · S23↔S24 (P→R · 1 kademe · 70°) ·
              S35↔S36 (V→W · 2 kademe · 90°) — üçü de BÖLÜM SINIRI, elle kareyle denetlenir
DÜNYA ÇAPASI  3/3 — W1 zemin · W2 ufuk · W3 gökteki merceklenmiş halka; üçü BİREBİR
              18 geniş dış promptta (A S0 S3 · E S5 S6 · F S8 S10 S11 · I S12 S13 ·
              M S19 S25 S27 · S S30 S32 S45 · X S38 S41 · H S47); dar dış promptlarda
              yalnız W1; iç hacimde hiçbiri (㉖ uyumu) [D209]
YIPRANMA      BEYAZ 3 sabit bölge (sol manşet · sağ diz · sırt altı) · TURUNCU 2 (iki diz)
              kir merdiveni tek yönlü, geri dönmez; kademe S13 ve S25 [D42]
KİMLİK DİZİSİ kask K (kapalı) × 48 — sahne başına harf: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
              amblem YOK (her iki giyside) · giysi rengi kirli beyaz + kobalt mavi omuz ↔
              yanık turuncu + siyah üst kol · kir bölgesi S00'dan itibaren ·
              HASAR BAŞLANGICI S16 (sol manşet ezik + gümüş bant S17'den) — geri dönmez [D208]
IŞIK TAKVİMİ  MONOTONİK ✅ — tek güneş sol üstten, kadraj dışı, 48/48 sabit; ardışık sahne
              arası fark ≤30° ve ≤500 K. Galeri (S14-S18) tek sarı servis lambası + yarıktan
              tek soğuk dilim. Kabin 4500K tek panel.
SES REGISTER  HUMAN 8 · MACHINE 0 — sekizi de telsizden, post-dub, klipte üretilmez
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI ①        KLİP SÜRESİ — her kabul klibi 10,0 s mi [D124 · açık madde K3]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$K"
DOĞRULANDI    ✅ ffprobe 8.1 (homebrew) · 18.09.2026 — ffprobe kurulu ve koşuyor
İKAME         gerekmez (ffprobe her kurulumda var)

KAPI ②        EKRAN METNİ — masterda okunur metin 0,0 s mi
KOMUT         ffmpeg -hide_banner -i "$M" -vf "cropdetect=limit=24:round=2" -f null - 2>&1 | tail -5
              (+ elle: 48 karede metin taraması)
DOĞRULANDI    ✅ ffmpeg 8.1 · 18.09.2026 · cropdetect VAR
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         filtre yoksa 48 kareye elle bakılır (sahne başına 1 kare, 10 s ızgarasıyla)

KAPI ③        DONMUŞ KLİP — SAHNE_DOLULUGU ihlali (10 s boyunca duran klip)
KOMUT         ffmpeg -hide_banner -i "$K" -vf "freezedetect=n=0.003:d=2" -f null - 2>&1 | grep freeze
DOĞRULANDI    ✅ ffmpeg 8.1 · 18.09.2026 · freezedetect VAR
              ffmpeg -hide_banner -filters | grep -q " freezedetect " || kapıyı yeniden yaz
İKAME         filtre yoksa her klibin 0,0 / 5,0 / 9,5 s kareleri karşılaştırılır

KAPI ④        GİZLİ KESME — klip içinde sahne değişimi var mı [D1]
KOMUT         ffmpeg -hide_banner -i "$K" -vf "scdet=threshold=10" -f null - 2>&1 | grep lavfi.scd
DOĞRULANDI    ✅ ffmpeg 8.1 · 18.09.2026 · scdet VAR
              ffmpeg -hide_banner -filters | grep -q " scdet " || kapıyı yeniden yaz
İKAME         filtre yoksa blackdetect ile kesme aranır (VAR, doğrulandı)

KAPI ⑤        FİNAL VURUŞ KANITI — 478. saniyede tam 2 kabin ışığı [D141]
KOMUT         ffmpeg -ss 478 -i "$M" -frames:v 1 kanit_S47.jpg   → BAK ve SAY
DOĞRULANDI    ✅ ffmpeg 8.1 · 18.09.2026
İKAME         gerekmez
```
