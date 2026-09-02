# 📋 THE FROST LINE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün
> eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR
> (THE SKYLIGHT: altı mercek, altısı mod V — 8. film; bu film 9. olmasın).

> ⛔ **ÖLÇÜM SATIRI DA YAPIŞTIRILIR [Ders 137]:** ⑪ ölçüm kapısının
> `SES KANALI: VAR/YOK · −x LUFS · tepe −y dBTP` satırı rubriğin künyesine
> eklenmeden ses ekseni ÖLÇÜLMEMİŞTİR.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU yapıştırılır            MOD D
④ 📖 HİKAYE      → A BLOĞU yapıştırılır                MOD D
② 🔗 DEVAMLILIK  → ⛔ HİÇBİR ŞEY (baseline: videodan sahne envanteri
                                  + karakter pasaportu)
③ 🔊 SES         → ⛔ HİÇBİR ŞEY (baseline: kurgudan ses defteri)
                   + ⑪ ölçüm satırı künyeye [D137]

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: tünel ölçüleri /
                   ışık takvimi · ekran yönü · sabit çevre nesneleri
                   (kaburgalar · yataklar · perde · üs · gemi) [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · basınç · jet ·
                   yama · sarkma takvimi · kırağı hattı)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük
   tasarımdır.
⛔ ② ve ③'e belge vermek yasaktır — eksikliği değil, TASARIMI bozar.
   FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⛔ Her mercek AYRI ve TEMİZ sohbette [D110].
⛔ Dördüne de AYNI video dosyası verilir [D75] — filigransız, kartsız,
   −14 LUFS master [D150 · D70/72 · KURGU_RITMI §6].
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE FROST LINE
FORMAT:               3-5dk
RUNTIME:              249 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:          25  (S0-S24)
REVIEW INPUT:         video only

LOGLINE (intended):   A man who has grown food alone on Mars for nine years — beside a modern four-module base and the tall lander that brought him, which stands dusted on its pad and is never approached — is sweeping dust off his greenhouse tunnel when the crown seam of its oldest section splits
                      and the escaping air stands up as a white jet of
                      ice. He runs to it, not to the shelter; an outside
                      patch is blown off in a second, an inside patch
                      holds but the seam keeps tearing beyond it; as the
                      whole tunnel's roof sags and the frost line
                      crosses into his living sections, he pulls down
                      the old bulkhead membrane and clamps it, sealing
                      his oldest plants to their death to save the rest
                      — then plants new seed in the dead row and goes
                      back to sweeping.
THEME (intended):     Identity — castaway or gardener. Sentence:
                      "A castaway counts days; a gardener counts rows."
                      (⛔ NOT the trade pattern [TEMA §3c] — the sentence
                      names a distinction, not a sacrifice.)
THEME SCENES:         S2 (runs to the garden, not the hatch) · S8/S13/
                      S20/S23 (split frame: two worlds, one membrane) ·
                      S9 (glove passes a leaf without touching) · S21
                      (looks at his own hand, hand to helmet rim) · S22
                      (plants seed) · S24 (back to sweeping)
INTENDED EMOTION:     tension and physical urgency (S0-S20), then a
                      settled, unjudged calm — not triumph, not grief.
                      The viewer arrives asking "why is it snowing out
                      of a greenhouse?", stays asking "can he save it?",
                      leaves asking "he killed his oldest plants to save
                      the rest — would I?"
ENDING TYPE:          OPEN (visual dilemma) + seed payoff — S24 mirrors
                      S0: same frame, same man, same brush; the jet is
                      gone, the far third of the tunnel collapsed and
                      white. His fate is CLEAR (alive, two thirds of the
                      garden alive); the open question is the white
                      third. Open questions at the end: 1.

PROTAGONIST:          grower, male, 52, unnamed in prompts.
                      Wants: to keep the garden alive — visibly, the
                      green rows.
                      Fears: nothing performed — no panic in any frame;
                      his only hesitation is S18 (two seconds).
ANTAGONIST/FORCE:     no villain — nine years of wear in one seam, and
                      the pressure difference between 30 kPa inside and
                      0.7 kPa outside. Nothing attacks; the air leaves.
CENTRAL CHOICE:       S20 — he throws the clamp bar on the bulkhead
                      membrane: in the same shot the membrane bellies
                      toward the dying section, the last green vine
                      behind it turns white, and the roof over his own
                      section stops sagging and tightens.

DIALOGUE LINES:       0 — the film is fully silent (human 0 · machine 0)
SILENT SCENES:        25
AUDIO REGISTER:       HUMAN: breath only (all scenes) · MACHINE: 0
MUSIC (post, 29.08):  2 cues — CUE A "BASINÇ" 72 BPM S1-S12 (0:09-2:09) · CUE B "MÜHÜR" 120 BPM S13-S18 (2:09-3:07) + one damped hit at 3:24.0 (clamp) + coda S22-S24 (3:39-4:09, only resolution 3:59). NO MUSIC: 0:00-0:09 · 3:07-3:20 · 3:24-3:39 — beds continuous, no digital zero [D83/D136]. Source: THE_FROST_LINE_MUZIK.md
VIRAL INTERSTITIALS:  S0 · S3 · S13 · S19 · S20 · S24   ⛔ MAY NOT BE CUT
COVER/THUMBNAIL:      S0 at 0:07 — the white jet standing over the
                      tunnel's far end, the tiny man at the near end
                      with his brush. Promise: "snow from a greenhouse on
                      Mars, and one man." Inside the 0:00-0:10 band.
                      Plan B = S3/S4 (jet and palm) · Plan C = S13.
TITLE:                THE FROST LINE — the film's own counter: the line
                      of frost that moves from the seam to the leaves,
                      from the old section to the joint, and stops at
                      the sealed membrane; the final frame is that line.
LIBRARY CONTEXT:      3-5 dk shelf siblings: LOW POWER (Mars, woman,
                      greenhouse keeper, dust storm, sacrifice — log
                      lines) · THE SKYLIGHT (Mars, lava tube, time) ·
                      LOSS OF LIFT · THE BORROWED WEIGHT · THE COLD
                      BURN. This film differs: the crisis is SUDDEN and
                      loud (a seam, minutes), the greenhouse is
                      hypobaric (helmet closed inside), the cost is a
                      CHOICE (pruning a section), the theme is identity,
                      not sacrifice; no countdown, no gauge, no voice.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      25 · 0 sahne içi kesme
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok; gerekçe: 25×10 s
                 tek-çekim disiplini, tek kurgu müdahalesi S0 kırpması)
                 [D74 gerekçe satırı]
GRID:            sahne başlangıcı(n) = 9 s + (n−1) × 10 s
RUNTIME:         249 s   (Hook 9 s + 24 × 10 s) — 4:09
RAW FOOTAGE:     250 s · TRIM BUDGET: 1 s (yalnız S0 10→9)
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı, KAPAK
                 çıktısı YOK; filigran 0 kare [D150]
CAMERA:          25/25 sabit lockoff · klip içi pan/tilt/zoom/dolly 0
SETUP SEQUENCE:  12 kurulum, plandan [ACI_YAYI §4 — promptlarda lens ·
                 yükseklik · mesafe okunur biçimde yazılı]:
                 A 24mm üs seti 3 m/45 m EWS üst (S0·S24) · B 40mm
                 göğüs/3 m MS göz (S1·S11·S18) · C 32mm bel/8 m WS
                 profil (S2) · D 35mm omuz/1.5 m OTS (S5·S16) · D2 35mm
                 kapıda 1.2 m MS göz (S7) · E 50mm göz/1 m CU (S8·S12·
                 S21) · Fi 50mm diz/0.8 m CU alt (S4·S15·S19) · Fl 28mm
                 diz/3 m MS alt (S3·S20·S22) · G 24mm 0.4 m/9 m WS alt
                 (S6·S10·S13·S23) · G1 35mm göğüs/4 m MS arkadan (S9) ·
                 I 35mm kaburga 3 m/3 m MS üst (S14) · I' 24mm kaburga
                 3 m/6 m WS üst (S17)
SCALE LADDER:    EWS·MS·WS·MS·CU·MS·WS·MS·CU·MS·WS·MS·CU·WS·MS·CU·MS·WS·
                 MS·CU·MS·CU·MS·WS·EWS — her kesme tam 1 kademe; iki
                 bilinçli ŞOK: S0→S1 · S12→S13
ANGLE ARC:       açı TİPİ 5: üst (A·I·I') · göz hizası (B·D2·E·G1) ·
                 alt (Fi·Fl·G) · omuz üstü (D) · profil (C·S18)
                 [KAMERA_ACISI §2 ✅]
EŞ KADRAJ (bilinçli afinite — tek değişken kuralı):
                 S0↔S24 (sütun var↔yok · tünel bütün↔üçte bir beyaz ·
                 aynı adam aynı fırça) · S13↔S23 (perde açık↔mühürlü
                 ve şişik) · S3↔S6 (yarık önkol↔adam boyu; ölçek
                 bilinçli farklı MS↔WS)
REPLİK ZAMANLARI: — (replik 0; hizalama kapısı ⑨ sessiz filmde ızgara
                 dilim birleşimiyle koşulur [D115])
KATALİZÖR:       S0 → 0:02.5 (jet fışkırır)
ORTA NOKTA:      S10 → 1:39-1:49 (başlangıç 99 s — formülden [D122];
                 iç yama tutar T+0-2 ≈ 1:39-1:41; dikiş yamanın ötesinde
                 açılır T+7 ≈ 1:46)
HER ŞEYİN KAYBI: S19 → 3:09-3:19 (başlangıç 189 s); yaprak beyazlar
                 T+2-8 ≈ 3:11-3:17
DORUK:           S20 → 3:19-3:29 (başlangıç 199 s — formülden [D122];
                 kelepçe T+5 ≈ 3:24; zar şişer T+5.5 ≈ 3:24.5; son yeşil
                 beyazlar T+6-9 ≈ 3:25-3:28; tavan gerilir T+7-9)
FİNAL VURUŞ KANITI [Ders 141]: tek kare 244 s (S24 · T+5):
                 · BEYAZ ÇÖKMÜŞ BÖLÜM: tünelin sağ üçte birinde 1 adet,
                   filmi yataklara çökmüş, kırağılı
                 · GERGİN BÖLÜM: sol üçte ikide 2 adet, süt beyazı,
                   yuvarlak
                 · KAR SÜTUNU: 0 adet (jet yok)
                 · FİGÜR: 1 adet, sol uçta, elinde FIRÇA (S0 ile aynı)
                 ffmpeg -ss 244 -i "$M" -frames:v 1 kanit.jpg
                 Kanıt: "sağda beyaz çökük, solda iki gergin, sütun sıfır,
                 fırça elde" — dördü sayılamıyorsa final teslim edilmemiştir.
                 DÖNGÜ: uygulanmaz (yatay) — S0/S24 aynı kurulum, aynı
                 jest; arkasına eklenen her kare (kart dâhil) 🔴 [D70/72].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111
       25 karakter — 25 İNSANLI, insansız 0. S0 · S24 (EWS) · S13 · S17
       · S23 (geniş) sahnelerinde figür KÜÇÜK ama VARDIR; S4 · S15 · S19
       el insertlerinde yalnız eldiven+önkol — yine 1. "figür yok"
       bulgusu bu sahnelerde envanter hatasıdır.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         tam 1 · 25/25 sahnede görünür · insansız 0 · araç 0 ·
              biniş/iniş 0 kare · airlock geçişi 0 kare (S7 dışarıda
              çarkta biter, S8 içeride başlar — kesme tasarımı) ·
              üs kapağına ve gemiye yaklaşma 0
KASK          25/25 KAPALI — İÇERİDE DE (sera 30 kPa, hipobarik; insan
              solunamaz) · kasksız 0 · ara durum 0 · giyme/çıkarma 0 kare
              · beyaz sert kabuk + TEK düz ön cam, görünür koyu çerçeve
              [D146] · cam optik berrak, renksiz, YANSIMASIZ — yüz okunur;
              sırt ünitesi YOK, sırt silueti DÜZ [D79]
YERÇEKİMİ     0.38 g — koşu (S2·S7) ve yürüyüş GERÇEK ZAMANLI, süzülme 0,
              zıplama 0, AĞIR ÇEKİM 0 [D44]; düşük g yalnız düşen fırçada
              (S1: 1.2 m → 0.8 s), tozda ve kristallerde
ATMOSFER      dış 0.7 kPa · −45 °C: ses boğuk, tizsiz, uzak · gölgeler
              zayıf/yumuşak (MEŞRU [D41]) · toz 3-4 s'de TAM çöker ·
              rüzgâr 0 — hiçbir şey kıpırdamaz, kumaş çırpmaz
              iç 30 kPa · 22 °C (bölüm 1 soğuyor): kaçak GÜR uğultu;
              hava ölü sakin — yaprak/sap hareketsiz (fan 0)
TÜNEL         32 × 4.5 × 3.2 m · 3 bölüm · kaburga her 2 m · 9 yatak
              (3+3+3) · setler 1 m · süt beyazı yarı saydam film · bölüm 1
              (ekran SAĞI ucu, en eski): bir düzine eski koyu kare yama ·
              bölüm 2 (orta): airlock kapağı ön yüzde · bölüm 3 (SOL uç)
              · birleşimde düşey koyu bant
ÜS            (29.08) tünelin sol ucundan 40 m ekran-solda · 4 beyaz yatay modül (8 m) + 6 m düğüm (çanak anten + direk) · dış yanlara regolit seti bankalı, üstünde koyu pencere şeridi · 2 radyatör paneli · ötesinde güneş tarlası · düğüm önünde airlock · dış ışık 0 · S0/S24 kamerası dış modülün setinde · hiç açılmaz, yanında figür 0
GEMİ          (29.08) üsün 120 m ötesinde ekran-SOL arka planda, pistte · 24 m dik mürettebat iniş aracı: açık-beyaz kompozit, küt burun, koyu ısı kalkanı bandı, 4 açık bacak (tozla ağarmış), 3 motor çanı, tek koyu şerit, kapalı kargo kapağı EKRAN-SAĞA (üse) bakar — 25/25 aynı yönelim · MAT, tozlu · yalnız S0 · S2 · S24 (arka plan) · hiç yaklaşılmaz, biniş 0, kalkış 0 · yazı/bayrak/logo 0 · yanında figür 0 · "gemi niye kalkmıyor" filmin sorusu değildir (önerme: onu getiren araç, dönüş yakıtı yok — söylenmez)
DİKİŞ         bölüm 1 tepe dikişi: 0.4 m (S0-S5) → 1.5 m (S6) → yamanın
              ötesinde +0.6 m (S10) → >2 m (S13+) — MONOTONİK, hiç
              kapanmaz, hiç kısalmaz; bulgusu FİLMİN ÖNERMESİDİR
JET           DÜZ beyaz, tünel yüksekliğinde (~4 m), yalnız tepede
              genişler · kıvrılma 0 · duman/buhar okunuşu 0 · kristaller
              düz iner, 3 s'de yerde · kırağı eteği 1 m · zeminde beyaz
              halka · S0-S6 dış sahnelerde VAR · S24'te YOK (sıfır)
              "jet duman gibi" bulgusu tasarım ihlalidir (KAPI ①)
YAMA          dış (S5): 40×40 cm, basınçla kaldırılır, kadrajı ≤1 s'de
              terk eder, düz yay, 3 m öteye · iç (S10): aynı kare, basınç
              onu DÜZ emer, tutar — sahne sonuna kadar yerinde kalır
SARKMA        (sayaç ①) S6 iki kaburga arası bir karış → S13 iki bölümde
              tepe bir karış → S17 bölüm 1 yataklara 1 m → S19 bölüm 2
              iplere değer → S20 bölüm 2 DURUR + bir karış GERİLİR (klip
              içi) → S23/S24 bölüm 1 tamamen çökük, 2-3 gergin.
              MONOTONİK — hiçbir sahnede tavan öncekinden yüksek değil
              (S20'den sonra bölüm 2 hariç: o bilinçli ters adım)
KIRAĞI HATTI  (sayaç ②) S3 dikiş çevresi → S4 sağ eldiven → S9 en yakın
              yapraklar → S15 tek yaprak KLİP İÇİNDE (2-8 s) → S17 çoğu
              asma → S19 sınır geçildi: bölüm 2 fasulyesi KLİP İÇİNDE →
              S20 son yeşil asma KLİP İÇİNDE (6-9 s) → S24 üçte bir beyaz.
              Yaprak yalnız yeşil→gri→beyaz gider, geri dönmez, düşmez.
YEŞİL SIRA    (sayaç ③) 9 → 6 (S20'den sonra) · S22 yeni tohum 6. sıra
              ucunda (4 tohum, gömülü) — filiz 0 kare
KIRAĞI/BUZ    KATI, matte, taneli ("fine salt") · sıvı su 0 kare · damla
              0 · birikinti 0 · ıslaklık 0 · parlama/glow 0 — "ıslak
              görünüyor" bulgusu ayakta, "buz yerine su" bulgusu ihlal
SUIT KIRAĞISI (S8+) ılık nemli havaya giren soğuk suit'in üstünde 3 s'de
              bağlar; KLİP İÇİNDE sabit; sahneler arası MONOTONİK
              (PHASE 3 → 4); dışarıda S24'te erimez
PERDE         sarı, sert, yarı saydam · tepede rulo · S13 yarıda sıkışır
              (kenarı bölüm 1'de asma ipine takılı) · S16 serbest · S20
              tabana + kelepçe (göğüs hizası) → BÖLÜM 1'e doğru ŞİŞER ve
              S20-S23 boyunca şişik kalır; geri sarkmaz
TOHUM KUTUSU  12 cm mat metal, YAZISIZ · S12 bölüm 1 rafından alınır,
              sol göğüs cebine · S22 açılır; S12'den önce 0 kare
FIRÇA         30 cm katlanır · S0 elde · S1'de düşer (kadraj dışı) ·
              S24 elde — aynı fırça (Çehov çifti)
EKRAN YÖNÜ    yaraya gidiş SOLDAN SAĞA (S2 · S9) · dönüş sağdan sola
              (S7 · S23) · yarık, sütun, bölüm 1, perde her sahnede
              SAĞDA/sağ geride · üs, gemi ve airlock SOLDA — 25/25 sabit
SUIT          kömür grisi + soluk turkuaz bantlar · yıpranma tam 3 sabit
              bölge (sol diz yaması · sağ önkol bandı sürtük · sol alt
              göğüs sıyrığı) [D42] + KİR MERDİVENİ 4 faz [D147]:
              PHASE 1 S0-S1 (yalnız bot) · PHASE 2 S2-S7 (diz+avuç kızıl;
              S4+ sağ eldiven kırağı) · PHASE 3 S8-S15 (suit ince kırağı)
              · PHASE 4 S16-S24 (eldiven+önkol kalın kırağı). Toz azalmaz,
              kırağı silinmez.
IŞIK TAKVİMİ  DIŞ (S0-S7 · S24): geç sabah, güneş ekran-sol-arkada,
              gölgeler ekran-sağa, karamela gök, güneş diski 0 kare ·
              İÇ: ılık-beyaz gölgesiz gün ışığı; bölüm 1 S13'ten itibaren
              soluk mavimsi beyaz → S17 ölü gri-beyaz; bölüm 2 ılık kalır
              · yapay lamba/LED 0 kare · MONOTONİK
SES REGISTER  HUMAN 0 · MACHINE 0 — konuşma yok; duyulan her şey nefes/
              kumaş/bot/film gıcırtısı/kaçak · dış: ince tıslama · iç:
              GÜR uğultu · S10 T+1-3 tıslamaya iner, T+7 döner · S20
              T+5.5 aniden boğuklaşır (perde ardı) · S21-S23 nefes +
              boğuk tıslama · S24 jet 0 · "eksik diyalog" bulgusu yazılamaz
              · müzik promptlarda 0 (post)
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142 — her kapı KOMUT · DOĞRULANDI · İKAME]

```
M="<master.mp4>"   ·   ffmpeg 8.1 · kuru koşu 29.08.2026: silencedetect ·
ebur128 · crop · tile · select · showinfo · astats · signalstats · scale ·
fps → hepsi `ffmpeg -hide_banner -filters` çıktısında VAR.

E1 SÜRE · EN-BOY · FPS
   KOMUT:      ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate "$M"
   KABUL:      249 ± 2 s · 16:9 · ≥1440p (ihraç kilidi)
   DOĞRULANDI: ffprobe 8.1 · 29.08.2026
   İKAME:      —

E2 SES KANALI + LUFS + TEPE  [D136 · D137 · KURGU_RITMI §6]
   KOMUT:      ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M"
               ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:"
   KABUL:      audio VAR · −14 ± 1 LUFS · tepe ≤ −1.0 dBTP
   DOĞRULANDI: ebur128 · ffmpeg 8.1 · 29.08.2026
   İKAME:      ebur128 yoksa: astats (RMS) + "ses kanalı var" satırı yeter
   → sonuç satırı rubriğin künyesine YAPIŞTIRILIR: SES KANALI: VAR · −x LUFS · tepe −y dBTP

E3 DİJİTAL SESSİZLİK  [D83 · D136]
   KOMUT:      ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
   KABUL:      0 aralık (yatak tek parça; S19-S21 müziksiz ama SESSİZ DEĞİL)
   DOĞRULANDI: silencedetect · ffmpeg 8.1 · 29.08.2026
   İKAME:      astats saniyelik RMS — −60 dB altı saniye 0 olmalı

E4 KESME IZGARASI (aydınlık film — scene>0.3 burada ÇALIŞIR: dış/iç
   kesmeleri sert, kızıl↔süt beyazı)
   KOMUT:      ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
   KABUL:      24 kesme · saniyeleri 9 + 10k (±0.3 s)
   DOĞRULANDI: select/showinfo · ffmpeg 8.1 · 29.08.2026
   İKAME:      eşik 0.3 → 0.15; yine az bulursa S7↔S8 (dış→iç) ve S23↔S24
               (iç→dış) sıçramaları ızgaranın iki sabit çapasıdır

E5 KÖŞE TESTİ — FİLİGRAN  [D150]
   KOMUT:      ffmpeg -i "$M" -vf "crop=360:240:iw-360:ih-240,fps=1/30,tile=6x2" -frames:v 1 kose_SA.png
               (dört köşe için crop x/y değiştirilir)
   KABUL:      12 örnekte aynı köşede aynı şekil YOK
   DOĞRULANDI: crop/fps/tile · ffmpeg 8.1 · 29.08.2026
   İKAME:      —

E6 FİNAL VURUŞ KANITI  [D141]
   KOMUT:      ffmpeg -ss 244 -i "$M" -frames:v 1 kanit_S24.jpg
   KABUL:      B bloğundaki dört sayılabilir öğe (beyaz çökük 1 · gergin 2 ·
               sütun 0 · fırçalı figür 1)
   DOĞRULANDI: ffmpeg 8.1 · 29.08.2026
   İKAME:      —

E7 DORUK KANITI — S20 içi
   KOMUT:      ffmpeg -ss 203 -i "$M" -frames:v 1 kanit_S20a.jpg   (T+4: kelepçe öncesi)
               ffmpeg -ss 208 -i "$M" -frames:v 1 kanit_S20b.jpg   (T+9: zar şişik, asma beyaz)
   KABUL:      a: zar düz, asma yeşil · b: zar şişik, asma beyaz, tavan gergin
   DOĞRULANDI: ffmpeg 8.1 · 29.08.2026
   İKAME:      —

E8 KIRAĞI HATTI — S15/S19 klip içi beyazlama (KAPI ③'ün teslim tarafı)
   KOMUT:      ffmpeg -ss 161 -i "$M" -frames:v 1 s15_a.jpg · ffmpeg -ss 167 -i "$M" -frames:v 1 s15_b.jpg
               ffmpeg -ss 191 -i "$M" -frames:v 1 s19_a.jpg · ffmpeg -ss 197 -i "$M" -frames:v 1 s19_b.jpg
   KABUL:      a yeşil · b beyaz (aynı yaprak, aynı kadraj)
   DOĞRULANDI: ffmpeg 8.1 · 29.08.2026
   İKAME:      crop+signalstats ile yaprak bölgesinin ortalama parlaklığı
               a→b artmalı (ffmpeg -ss <t> -i "$M" -frames:v 1 -vf
               "crop=w:h:x:y,signalstats" -f null - | grep YAVG)

E9 SARKMA SAYACI — S6 · S13 · S17 · S20 tavan yüksekliği (kareyle)
   KOMUT:      ffmpeg -i "$M" -vf "select='eq(n,1770)+eq(n,4170)+eq(n,5370)+eq(n,6270)',scale=640:-1,tile=2x2" -frames:v 1 sarkma.png
               (30 fps · S6 T+1=59 s · S13 T+1=139 s · S17 T+1=179 s · S20 T+9=209 s)
   KABUL:      tavan çizgisi kare kare AŞAĞI iner; yalnız S20 T+9 bir karış yukarı
   DOĞRULANDI: select/scale/tile · ffmpeg 8.1 · 29.08.2026
   İKAME:      fps farklıysa kare numaraları saniye × fps ile yeniden hesaplanır
```
