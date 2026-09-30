# 📋 THE_STOLEN_SKY — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI. Operatör `QA_PROMPTLARI/_KAYNAK/`
> rubriğini açar ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_STOLEN_SKY_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik promptta ·
> opak vizör · sabit 10 s ızgara · metinsiz sayaç · Z zinciri) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu deseni arar.

> **Yazıldı:** 20.09.2026 (promptlarla aynı gün) · ⬜ alanlar üretimden sonra dolar (`⬜ AFTER THE CUT`).

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D   ⭐ 16 dk: 4 PART + FULL, her parça ayrı koşu
② 🔗 DEVAMLILIK  → C BLOĞU (Z zinciri · hasar merdiveni · eş kadraj)   MOD D
③ 🔊 SES         → A (post-dub tablosu) + C (hacim ses yasası)          MOD D (replik promptta 0 — tasarım)
④ 📖 HİKAYE      → A BLOĞU                          MOD D   ⭐ yalnız FULL koşusunda (PART'ta hikâye ölçülmez)
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri + A  MOD D
PART BEYANI (rubriğin başına): "THIS FILE IS PART n OF 4 — S{{24(n−1)}}–S{{24n−1}} · 24 clips · {{240(n−1)}}–{{240n}} s.
   Story gates are measured on the FULL run only. Boundary pairs S23↔S24 · S47↔S48 · S71↔S72 are closed by hand-frame."
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_STOLEN_SKY
FORMAT:            yatay 16 dk · 96 × 10,000 s · 8 BÖLÜM × 12 (KILAVUZ_REHBERI §2.8) · 16:9 · 24 fps · OMNI 1.1 Flash I2V
RUNTIME:           960,000 seconds (title card: NONE — screen text lock 0,0 s; bölüm adı yalnız kurguda mevcut görüntü üstüne, isteğe bağlı)
SCENE COUNT:       96 (S00–S95 · sahibin V01–V96 = S+1 · 24 sekans SEK01–SEK24)
PART GRID:         PART 1 = S00-S23 · 24 clips · 0-240 s (BOLUM_1+2) · PART 2 = S24-S47 · 24 clips · 240-480 s (BOLUM_3+4) ·
                   PART 3 = S48-S71 · 24 clips · 480-720 s (BOLUM_5+6) · PART 4 = S72-S95 · 24 clips · 720-960 s (BOLUM_7+8) ·
                   FULL = S00-S95 · 96 clips · 0-960 s. QA her parçaya AYRI koşar (①②③⑤⑥⑦⑧⑭⑮), ④⑫③-bütün yalnız FULL.
                   BOUNDARY PAIR: S23↔S24 (T→H) · S47↔S48 (E→E küme) · S71↔S72 (B→B küme) — elle kareyle kapanır (B BLOĞU EŞ KADRAJ).
THEME:             SORUMLULUK — "Gücü eline alan, onu kime borçlu olduğunu da seçer." (aday etiket, TEMA §3b tarihli satır FAZ 6)
THEME SCENES:      S18 · S59 · S81 · S84 · S94
INTENDED EMOTION:  intikam isteğinin yerini borcun alması — seçim anında rahatlama değil ağırlık (S84), final sessiz (S94)
ENDING TYPE:       KAPALI + BEDELLİ — iki gemi ve K-1 dışarıda (İSTEK karşılandı), Bor yok, Serrak hayatta, koloni geride (S95 hareketli bitiş, devam göndermesi yok)
PROTAGONIST:       unnamed — identified only by suit colour (dark cobalt, pale grey left-shoulder mark); no proper name appears in any prompt [D34]; kadro 4 → 3 (S59)
CENTRAL CHOICE:    S84 (840,0–850,0 s) — T-handle seçici koridor konumuna; saldırı çıkışının lambası söner, koridor lambası yanar (aynı kadraj)
                   ÇAPA ÜÇLÜSÜ: CHOICE S81/S84 (T-handle: eldiven üstte → seated) · FINAL S94 (kemer açık → kapalı) · BEFORE/AFTER tek nesne
DIALOGUE LINES:    0 (prompts) · POST-DUB LINES: 8 · register: HUMAN 8 / MACHINE 0 — hepsi akuzmatik (opak vizör, ağız 0 kare)
                   S10 104,0 kaptan (telsiz) · S11 117,0 Mara · S14 145,0 Ada · S53 533,0 Rey · S58 583,5 Bor · S67 674,0 Ada (🔶 metin sahip) · S82 821,0 kaptan · S84 841,5 Mara
SILENT SCENES:     88 / 96 (replik klip dışı; 96/96 klip müziksiz ve diyalogsuz üretilir — müzik yalnız kurguda, MUZIK dosyası)
VIRAL INTERSTITIALS: NONE — opak vizör, ⭐VİRAL YÜZ satırı yazılamaz (SAPMA 3); hareket enerjisi yüksek 16 sahne 00_OKUMA_CIZELGESI'nde listeli
                   ⛔ KESİLEMEZ: S00 · S13 · S22 · S59 · S84 · S87 · S92 · S93 · S94 · S95 (novum kuralı + iptal kapısı sahneleri)
TITLE:             THE STOLEN SKY — gök çalınmıştır: kalkış yok, sıçrama yok; film göğü 60 saniyeliğine geri alır ve tekrar kaybeder
LIBRARY CONTEXT:   yatay_16_dk_filmler/ (bu klasörün ilk filmi) · kardeş: THE_FALLING_WORLD (48 · opak vizör · OMNI I2V emsali) · BENI_HATIRLAMA · SUSMAYAN_NOBETCI (8 dk)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      96
SHOT COUNT:      96 · sahne içi kesme 0 (her klip tek çekim; küme klipleri bölünmüş tek çekimin devamı)
TARGET ASL BAND: 10,000 s sabit ızgara   ASL CURVE: düz (10,0 × 96)
                 GEREKÇE [D74]: sahip beyanı "her video tam 10 saniye" + OMNI I2V gerçek son kare zinciri (Z) sabit birim ister;
                 tempo değişimi klip İÇİNDE hareketin başlama anıyla kurulur (03 §0.4: ortadan açılan 9 · sonucu uzun taşıyan 6 · vuruşu geç 3)
GRID:            sahne başlangıcı(n) = 0 hook + n × 10,000 s klip  (n = S numarası, 0'dan) — S84 = 840,000 s · S87 = 870,000 s · S93 = 930,000 s
RUNTIME:         960,000 s ±0 (kurgu kapısı) · 23.040 kare @24 fps
RAW FOOTAGE:     960,0 s hedef (96 × 10,0) · ham ARAÇTAN ÖLÇÜLÜR (E KAPI ①) · TRIM BUDGET: 0 (kırpma yok)
KIRPMA:          ham klip ≠ 240 kare ise SON kareden kırpılır/uzatılmaz — 240 kareye sabitleme kurgu biriminde; Z klipleri kaynağının 240. karesinden başlar
SCREEN TEXT:     0,0 saniye (bölüm adı isteğe bağlı üst yazı — kurgu kararı, prompta girmez)
CAMERA:          96 / 96 tek çekim · sabit (lockoff/fixed) 74 · hareketli 22 (takip H M X R O W · pan T · push-in J · araç-sabit G)
SETUP SEQUENCE:  20 kurulum A–X (PLAN Camera Bible birebir) · dönüş "— the same position, height and lens as Scene N." · küme "continues the previous clip from its exact last frame — …"
KURULUM İSKELETİ: A B C B D E D B E J B C A A G C K W C E B D B T H E G N X W G N B D O O F F C D E E F D J F C E E E L C E C D E C B L R J F C D C D C B N B J B B D D B D P B N E L L F L C F A M P P F X Q G A
KÜME:            10 küme klibi — S13 · S35 · S37 · S41 · S48 · S49 · S72 · S74 · S82 · S90 (9 küme, en uzun 3 klip S47-S49)
DÖNÜŞ:           36 / 96 = %37,5 (prompt_kontrol ölçümü; hedef %40 — D74 SAPMA, PLAN UYGULANMAYAN KİLİTLER)
ANGLE ARC:       6 açı tipi (low angle · eye level · high angle · over-the-shoulder · from below/behind · profile)
DORUK:           S84 → merkezî seçim (840,000 s) · fiziksel doruk S92 (920,000 s) · bedel S59 (590,000 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 0 + n × 10,000 + promptun TIMELINE ofseti   →  104,0 · 117,0 · 145,0 · 533,0 · 583,5 · 674,0 · 821,0 · 841,5 (PLAN replik tablosu)
   Post-dub yerleşimi kurgu biriminde bu saniyelere; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   S94 · 946,0 s · kapalı kemer 1 adet (dört koltuk, üç dolu, dördüncü koltukta kemer KAPALI ve eldiven üstünde) · BULUNAN
   S95 · 958,0 s · insan gemisi 3 adet tek karede (yatay bant · iki dikey bant · kelepçe+güdük) · BULUNAN
   ffmpeg -ss 946 -i "$M" -frames:v 1 kanit_S94.jpg   → BAK ve SAY (kemer 1)
   ffmpeg -ss 958 -i "$M" -frames:v 1 kanit_S95.jpg   → BAK ve SAY (gemi 3)
DÖNGÜ KANITI: S00 ↔ S95 aynı harf A (aynı CAMERA cümlesi) · değişen tek değişken: örgüye çarpan 1 gemi ↔ örgünün dışında 3 gemi; ışık aynı kaynak (halka), jest yok
EŞ KADRAJ (elle kare): S23↔S24 (K-1 sağlam bilezik) · S33↔S62 (sağ panel kapalı, aynı iz) · S05↔S80 (hangar) · S47↔S48 · S71↔S72 (Z)
SAYAÇ (metinsiz, 4 kanal): koridor bandı KAPALI (S86 son kare) → AÇIK 2 gemi eni (S87 ilk kare 870,0) → 1,5 (S92) → KAPALI (S93 ilk kare 930,0) ·
   depo ışığı: dolu ikon S16 → sabit S63 → nabız S85 (tetik TIK = 850,8 s) · insan sayısı 4 → 3 (S59) → 3 + boş koltuk (S94) · K-1 hasarı K0 → K1 S29 → K2 S66 → K3 S90
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 - 1 1 - - 1 1 1 1 1 - 1 1 1 1 - - 1 - - - 1 - 1 1 1 1 1 1 1 1 1 1 1 1 - 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 - 1 1 1 1 1 1 1 - 1 - 1 1 1 1 1 1 - - 1 1 1 1 1 1 1 1 - - - - - - - 1 -
       (1 = kadrajda insan · - = insansız ya da yalnız Veyra/araç; S09 S44 S60 S70 Veyra-yalnız · S12 S13 S19 S24 S25 S27-S29 S31 S68 S77 S78 S87-S93 S95 araç/gök)
KADRO: 4 → 3 (S59 sonrası Bor 0 kare / 0 ses) — İNSAN SAYISI sahne başına PLAN sahne haritasında (0–4)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         4 (Mara kobalt · Rey turuncu · Ada kırık beyaz · Bor grafit/hardal) → 3 (S60+) · sivil ≤3 (S05 · S80) · kalabalık 0 · yüz 0 kare
KASK          vizör TAMAMEN OPAK mat siyah düz panel, kalın koyu çerçeve (SAPMA 3 — D79 "optik berrak" bu filmde UYGULANMAZ, ⑤/⑨ bunu ihlal yazamaz) ·
              sırt: Mara/Bor düz sürekli yüzey, hiçbir şey taşımaz; Rey tek dar düz ünite (≤ el kalınlığı); Ada tek düz dikdörtgen modül çerçevesi (S85'ten sonra BOŞ çerçeve)
NOVUM         Yörünge Kafesi: gökteki kehribar ÖRGÜ (lattice) kalkışı ve sıçramayı keser; altında alçak uçuş serbest; hasarlı hücreyi komşu kuleler ≤2 s'de kapatır (S13);
              tek kule kontrolde 60 s ters çevrilip 2 gemi eninde koridor açar (S87–S93). İHLAL: insan gemisi örgüye değince yana savrulur (S00) — sıçrama örgü DIŞINDA (S88 S91 S93).
              Aile türevleri: KALKAN (öne bakan kavis, 4 nokta ≤0,5 s'de yana sapar, 2 figür boyu) · PORTAL (iki nokta arası sınırlı kapı, drone ister) — ikinci ihlal DEĞİL.
              PREMISE REGISTER beklenir [D166]: S00 kurulum · S13 doğrulama · S87/S93 sonuç
YERÇEKİMİ     0,9 g (yüzey · iç · kabin · C-0) · 0 g yalnız S94 (tek serbest nesne: kemer ucu) · vakum S93 S95 (fragman düz çizgi)
ATMOSFER      1,0 atm nefes yoğunluğunda hava (§3.3 yeniden açılış) — toz ≤2 s çöker · gölge yumuşak-derin · duman/haze yükselir incelir · dış ses normal;
              S93/S95 vakum: dış ses 0, gölge mutlak siyah · S88/S92 üst atmosfer → vakum geçişi (ses incelir)
EKRAN YÖNÜ    NESNE-GÖRELİ [D174]: halka hep KULENİN ÜSTÜNDE (kamera kuleye bakıyorsa üst-orta; kule kadraj dışıysa halka üstte/köşede ya da dışarıda, ışığı gövdeden okunur) ·
              örgü hep halkadan YAKIN ve geometrik · koridor bandı kuleden yukarı, halkaya doğru · portal geçişi istasyon→platform aynı ekran yönü (S45/S46) ·
              K-1 sapması her uçuşta SAĞA (S30 S68 S77 S78 S86 S90–S93: 8/8 sabit) · konum kilidi Mara SOL · Bor SAĞ (S18–S58) · pusula kelimesi 0
SAYAÇ         monotonik 4 kanal (B bloğu SAYAÇ satırı) — koridor bandı 0 → 2 → 1,5 → 1 → 0 gemi eni · hasar merdiveni K0→K3 geri dönmez · kadro 4→3
EŞ KADRAJ     S00↔S95 (A) · S05↔S80 (E) · S33↔S62 (panel) · S23↔S24 · S47↔S48 · S71↔S72 (PART sınırları)
DÜNYA ÇAPASI  3/3 — ① black basalt ridges and angular worn human structures / curved Veyra surfaces · ② amber lattice (≤2 gemi eni aralık) + lensed ring (ayrı, daha küçük, sabit) ·
              ③ gölge halkadan uzağa, örgü gölge atmaz — World Bible BİREBİR, dış-mekân promptlarında sıfır sapma [D209]
YIPRANMA      4 sabit bölge [D42]: Mara sol göğüs uzun açık sıyrık (S03+) · Bor sağ diz zırhı çatlak (S51–S59) + boş hücre yuvaları (S57–S59) ·
              K-1 sağ bilezik eğik (S29) → kelepçe (S66) → arka güdük (S90) · E-2 sağ denge yüzeyi is (S89+) — hiçbiri geri dönmez
KİMLİK DİZİSİ kask K/- sahne başına: K K K K K K K K K - K K - - K K K K K - K K K K - - K - - - K - K K K K K K K K K K K K - K K K K K K K K K K K K K K K - K K K K K K K - K - K K K K K K - - K K K K K K K K - - - - - - - K -
              amblem: Mara SOL omuz açık gri işaret · Rey her iki üst kol beyaz bant · Ada turkuaz önkol · Bor hardal göğüs plakaları · kir: global, sıfırlanmaz ·
              hasar başlangıcı: S03 (Mara) · S29 (K-1) · S51 (Bor) · S66 (kelepçe) · S89 (E-2) · S90 (güdük) [D208]
IŞIK TAKVİMİ  mekân başına sabit (PLAN Lighting Bible): yüzey amber key + soğuk fill · hangar soğuk + tavan amber barları · kabin soğuk · T3 iç soğuk + depo kehribarı · C-0 alçak amber · vakum sert rim —
              klip içi ışık olayı yalnız planlı sınırlarda (S08 kapak · S12/S13 hücre · portal açılış/kapanış · S59 göğüs lambası · S84 iki lamba · S87/S93 bant) [D193 · D201]
SES REGISTER  HUMAN 8 (post-dub, akuzmatik) · MACHINE 0 · promptta "No dialogue. No music." 96/96 · hacim ses yasası: yüzey normal · iç kapalı yankı+fan · kabin hum · C-0 alçak kavisli tonlar · vakum dış ses 0
HAREKET KİLİDİ tek jest kuralı: S10 sıkılan eldiven · S11 kol K-1'e · S18 kayış tek çekiş · S58 eldiven boşta · S61 yumruk · S81 el kolun üstünde (dokunmaz) · S84 tek sürekli kol hareketi + tek klik · S94 kemer tek klik
POLİTİKA      en riskli S59 (nötr tarif PLAN'da) · S38 · S51 · S58 · S48 — kan/yara/ceset/silah adı 0; isabet = "hard impact light on ceramic, fades ≤0,5 s"; ölüm = üç işaret (alet düşer · gövde kayar · lamba söner)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır; doğrulama satırı olmayan kapı YAZILMAMIŞTIR.
> Doğrulama 20.09.2026 · ffmpeg/ffprobe 8.1 (homebrew) · `ffmpeg -hide_banner -filters` ile filtre varlığı sınandı: cropdetect · freezedetect · scdet · signalstats · blackdetect VAR.

```
KAPI ①        KLİP SÜRESİ — her kabul klibi 10,000 s / 240 kare mi [D124 · Q3]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$K" ; ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 "$K"
DOĞRULANDI    ✅ ffprobe 8.1 · 20.09.2026 — kurulu ve koşuyor; ilk kabul klibinin değeri PLAN KLİP SÜRESİ satırına yazılır
İKAME         gerekmez (ffprobe her kurulumda var)

KAPI ②        EKRAN METNİ — masterda okunur metin 0,0 s mi (bölüm üst yazısı hariç, o kurgu kararı)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "cropdetect=limit=24:round=2" -f null - 2>&1 | tail -5   (+ elle: 96 karede metin taraması, 10 s ızgarası)
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026 · cropdetect VAR
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         filtre yoksa 96 kareye elle bakılır (sahne başına 1 kare)

KAPI ③        DONMUŞ KLİP — SAHNE_DOLULUGU ihlali (10 s boyunca duran klip) — ⭐ 16 dk'da 96 klip: betik döngüsü
KOMUT         for K in *.mp4; do ffmpeg -hide_banner -i "$K" -vf "freezedetect=n=0.003:d=2" -f null - 2>&1 | grep -q freeze_start && echo "FREEZE $K"; done
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026 · freezedetect VAR
              ffmpeg -hide_banner -filters | grep -q " freezedetect " || kapıyı yeniden yaz
İKAME         filtre yoksa her klibin 0,0 / 5,0 / 9,5 s kareleri karşılaştırılır

KAPI ④        GİZLİ KESME — klip içinde sahne değişimi var mı [D1] (Z klipleri dâhil: küme sınırında scdet 0 beklenir)
KOMUT         ffmpeg -hide_banner -i "$K" -vf "scdet=threshold=10" -f null - 2>&1 | grep lavfi.scd
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026 · scdet VAR
              ffmpeg -hide_banner -filters | grep -q " scdet " || kapıyı yeniden yaz
İKAME         filtre yoksa blackdetect ile kesme aranır (VAR, doğrulandı)

KAPI ⑤        FİNAL VURUŞ KANITI — 946. saniyede kapalı kemer 1 · 958. saniyede insan gemisi 3 [D141]
KOMUT         ffmpeg -ss 946 -i "$M" -frames:v 1 kanit_S94.jpg ; ffmpeg -ss 958 -i "$M" -frames:v 1 kanit_S95.jpg   → BAK ve SAY
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026
İKAME         gerekmez

KAPI ⑥        KURGU SÜRESİ — master 960,000 s ±0 · 23.040 kare (16 dk kapısı, §2.8)
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M" ; ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 "$M"
DOĞRULANDI    ✅ ffprobe 8.1 · 20.09.2026
İKAME         gerekmez

KAPI ⑦        KORİDOR SAYACI — S87 ilk karesinde (870,0 s) bant AÇIK · S93 ilk karesinde (930,0 s) bant KAPALI · S86 son karesinde (869,96 s) KAPALI
KOMUT         ffmpeg -ss 869.96 -i "$M" -frames:v 1 s86_son.jpg ; ffmpeg -ss 870.0 -i "$M" -frames:v 1 s87_ilk.jpg ; ffmpeg -ss 930.0 -i "$M" -frames:v 1 s93_ilk.jpg   → BAK
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026 (kare çıkarma — filtre gerekmez)
İKAME         gerekmez

KAPI ⑧        GÖLGE İÇİ DOLGU — §3.3 atmosferde gölgeler mutlak siyah OLMAMALI (vakum sahneleri S93 S95 hariç): YAVG < 18/255 → sahne reddedilir
KOMUT         ffmpeg -hide_banner -i "$K" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG | head -3
DOĞRULANDI    ✅ ffmpeg 8.1 · 20.09.2026 · signalstats VAR
              ffmpeg -hide_banner -filters | grep -q " signalstats " || kapıyı yeniden yaz
İKAME         filtre yoksa gölge bölgesinden elle histogram
```

---

## ⬜ AFTER THE CUT — üretimden sonra dolar

```
KLİP SÜRESİ ÖLÇÜMÜ:     ⬜ (KAPI ① ilk kabul klibi) · MASTER: ⬜ s / ⬜ kare (KAPI ⑥)
DENEME KAYITLARI:       P1 S48 ⬜ · P2 S01 ⬜ · P3 S02 ⬜ · P4 S68 ⬜ · P5 S90 ⬜ · P6 S59+S38 ⬜ (URETIM_DEFTERI §0b)
PART KOŞULARI:          PART 1 ⬜ · PART 2 ⬜ · PART 3 ⬜ · PART 4 ⬜ · FULL ⬜ (FILM_QA_RAPORLARI/00_INDEX YATAY 16 dk satırları)
SINIR ÇİFTLERİ:         S23↔S24 ⬜ · S47↔S48 ⬜ · S71↔S72 ⬜ (elle kare)
```
