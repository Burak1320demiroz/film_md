# 📋 THE BORROWED WEIGHT — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün
> eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU yapıştırılır            MOD D
④ 📖 HİKAYE      → A BLOĞU yapıştırılır                MOD D
② 🔗 DEVAMLILIK  → ⛔ HİÇBİR ŞEY (baseline: videodan sahne envanteri
                                  + karakter pasaportu)
③ 🔊 SES         → ⛔ HİÇBİR ŞEY (baseline: kurgudan ses defteri)

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: mesafe/ölçek sayacı ·
                   ekran yönü · sabit çevre nesneleri [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · oran · hız · süre)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük tasarımdır.
   Ama YAKLAŞMA filminde mesafe sayacı verilmezse ⑤ tasarlanmış yaklaşmayı
   "geometri sürüklenmesi" yazar ve tablosunun tamamı ⑩'dan düşer [D133].

⛔ ② ve ③'e belge vermek yasaktır — eksikliği değil, TASARIMI bozar.
   O iki merceğin değeri filmin kendisiyle çelişip çelişmediğini
   ölçmesinde; ölçüte plan verilirse ölçüt kaybolur.
   FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.

⛔ Her mercek AYRI ve TEMİZ sohbette [D110].
⛔ Dördüne de AYNI video dosyası verilir [D75].
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE BORROWED WEIGHT
FORMAT:               3-5dk
RUNTIME:              249 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:          25  (S0-S24)
REVIEW INPUT:         video only

LOGLINE (intended):   A lone loadmaster clearing a crashed cargo line on a
                      wind-scoured grey plain lifts wreck after wreck,
                      knowing each piece he lifts leaves its weight in his
                      body — and on the night he frees the sealed beacon
                      case, learns that everything he lightened belongs to
                      the wind, and only what is heavy stays.
THEME (intended):     What remains is what someone carried the weight of.
                      ⚠️ TAKAS kalıbı (TEMA_MUHENDISLIGI §3c): "X için
                      Y feda edilir". Kalıp arka arkaya en çok 2 filmde.
THEME SCENES:         🚨 YAZILMAMIŞ (26.08.2026 ölçümü)
                      §5 temayı MOTİFE, motifi SAHNEYE bağlar; burada
                      tema tek cümle olarak var, sahne eşlemesi yok.
                      CENTRAL CHOICE (S20) tek bağlantı ve o da bedeli
                      anlatıyor, motifi değil.
                      ⛔ Sonradan türetme [03_PLAN_ONCESI B3].
INTENDED EMOTION:     a willing trade, not a tragedy — the viewer arrives
                      asking "how is he this strong?", stays asking "will
                      he lift one more?", leaves rereading the strength as
                      the cost.
ENDING TYPE:          twist + ambiguous fate (the plain empties overnight;
                      his survival is not shown; the case contents are
                      never shown — 0 frames)

PROTAGONIST:          loadmaster, male, 47, unnamed in prompts.
                      Wants: to free and raise the beacon case.
                      Fears: not the weight — stopping before it is done.
ANTAGONIST/FORCE:     no villain — the rule itself: lifted weight transfers
                      to the lifter and is never returned; the night wind
                      that takes everything lightened.
CENTRAL CHOICE:       S20 — lifting the final 3×3 m cover plate, knowing it
                      ends his walking. Cost lands IN THE SAME SHOT: boots
                      drive 19 cm deep, a star of cracks spreads.

DIALOGUE LINES:       4 — all MACHINE (suit AI status calls, chest speaker;
                      the man never speaks; mouth out of frame in all four)
SILENT SCENES:        21
VIRAL INTERSTITIALS:  S5 · S13 · S19 · S23   ⛔ THESE MAY NOT BE CUT
COVER/THUMBNAIL:      S0 paradox MCU — huge beam on one shoulder, boots
                      sunk deep, face readable. Promise: "how — and why is
                      he sinking?"
TITLE:                THE BORROWED WEIGHT — the weight is borrowed FROM the
                      wreck BY the man; the counter is footprint depth.
LIBRARY CONTEXT:      3-5 dk shelf siblings: LOW POWER · LOSS OF LIFT ·
                      THE COLD BURN · THE THIRD DUNE. This film differs:
                      no resource countdown — the threat is the character's
                      own chosen rule; first physics-law novum living IN
                      the human body.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      25 · 0 sahne içi kesme
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok; gerekçe: 25×10 s
                 tek-çekim disiplini, tek kurgu müdahalesi S0 kırpması) [D74]
GRID:            sahne başlangıcı(n) = 9 s + (n−1) × 10 s
RUNTIME:         249 s   (Hook 9 s + 24 × 10 s)
RAW FOOTAGE:     250 s · TRIM BUDGET: 1 s (yalnız S0 10→9)
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı YOK
CAMERA:          25/25 sabit lockoff
                 ⛔ KLİP İÇİ karar; sahneler ARASI kurulumu SETUP
                 SEQUENCE anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE:  🚨 YAZILMAMIŞ (26.08.2026 ölçümü)
                 Video promptlarının 25'inde sahne bazlı kamera
                 geometrisi (lens · yükseklik · mesafe) OKUNABİLİR
                 biçimde yok; 13 sahnelik PART_A taramasında yalnız
                 1 sahnede açı sözlüğünden bir kelime bulundu (profil).
                 ⛔ Bu satırı sonradan TÜRETME. Kurulum kaydı plandan
                 gelir; promptta yoksa kurulum kararı da alınmamıştır
                 (yazılmayan kurulumu model seçer). Bu, filmin ölçülen
                 EN BÜYÜK açığıdır ve yeniden üretim gerektirmez —
                 sonraki filmde plana yazılır.
                 ⚠️ Mevcut EŞ KADRAJ satırı (S0↔S24 · S4↔S16 · S6↔S18 ·
                 S1↔S21 · S8↔S23) kasıtlı kadraj TEKRARIDIR ve kurulum
                 ÇEŞİTLİLİĞİNİN kanıtı değildir — tersi.
ANGLE ARC:       🚨 1 açı tipi ölçüldü (PROFİL). §2 en az 3 ister.
REPLİK ZAMANLARI (±2 s doğrulama [D115]):
                 S2  → 0:22   S10 → 1:43   S21 → 3:31   S22 → 3:45
                 (formülden: 9 + (n−1)×10 + prompt TIMELINE ofseti;
                  elle yazılmaz [D122] — 24.08.2026'da S2 ve S10 bir
                  yuva geç yazılmış hâlde bulundu ve düzeltildi)
DORUK:           S20 → 3:19-3:29 (sahne başlangıcı 199 s)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111-11111-11111
        │            │     └──── S20-S24 insanlı (doruk → final)
        │            └────────── S19 insansız (viral #3)
        └─────────────────────── S13 insansız (viral #2)
insansız 2 sahne: S13 · S19   ·   insanlı 23 sahne
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         tam 1 · 23 sahnede görünür · 2 sahne insansız (S13 · S19)
KASK          23/23 insanlı sahnede KAPALI · kasksız 0 · ara durum 0 ·
              giyme/çıkarma 0 kare · vizör optik berrak, yüz okunur,
              sırt ünitesi YOK — düz siluet [D79]
YÜZ ÖZEL      dört MACHINE replik sahnesinde (S2·S10·S21·S22) ağız
              KADRAJ DIŞI — "adam konuşuyor" bulgusu tasarım gereği
              İMKÂNSIZDIR; sentetik ses suit hoparlörüne aittir [D82]
NOVUM         yerden KESİLEN parça yüzey ağırlığının ~%3'üne iner,
              ağırlık taşıyana geçer ve GERİ VERİLMEZ. Hafiflemiş parça
              rüzgârda YERDE sürüklenir (havalanma 0, devrilme 0).
              İtme/manivela devri tetiklemez (S17 bunun kanıtı — plaka
              orada TAM ağırlıklıdır). Kayan enkaz bulgusu FİLMİN
              ÖNERMESİDİR, hata değil [D87/D116 önerme kapısı].
YERÇEKİMİ     0.92 g — Dünya temposu; düşen nesne normal düşer
              (S3 anahtar · S16 taş); ağır çekim 0 kare
ATMOSFER      ince (~%1.2 bar): ses boğuk · gölge yumuşak · toz 3-4
              saniyede TAM çöker · güneş diski 0 kare (sürekli örtü —
              gölgesizlik fiziktir, hata değil [D41 zemini yok])
RÜZGÂR        gündüz 1-2 m/s → gece 6-8 m/s · ekranda HEP SAĞDAN SOLA ·
              normal nesneyi asla devirmez/kıpırdatmaz
İZ SAYACI     2→4→6→8→11→14→19→23 cm (S1→S21) MONOTONİK — geri dönmez;
              izler asla silinmez (nem yok). S24'te izler DURUR.
ADIM SAYACI   S6: 9 adım/10 s ↔ S18: 5 adım/10 s — AYNI kadraj (32mm ·
              bel · 7 m · profil); tek değişken yük [eş kadraj çifti]
KANTAR        18 cm pirinç · 12 çentiği RAKAMSIZ · ibre S4: 2. çentik →
              S10: 9. çentik → S16: yay dibi · S16'da geride bırakılır
              (S18'den itibaren kemer BOŞ — kayıp değil, tasarım)
NABIZ         cyan · 2 saniyede 1 · her görünüşte aynı ritim · İSTİSNA:
              S15'teki ezik ikinci kasanın feneri ÖLÜ (0 nabız — tasarım)
KASA          46 cm mühürlü beyaz küp · içerik 0 kare (tasarım — muğlak
              final) · S22'de kızak tepesine KENETLENİR (kilit sesi)
LANDER        9 m · YÖNELİM KİLİDİ: burnu gömülü, kuyruğu göğe eğik,
              kapak yüzü ekran-soluna dönük — 25 sahnede sabit
EKRAN YÖNÜ    hedef/modül HEP SAĞDA · ilerleme soldan sağa · geriye
              bakış sola · rüzgâr ve kayan parçalar sağdan sola —
              25 sahnenin 25'inde tersine dönmez
EŞ KADRAJ     S0↔S24 · S4↔S16 · S6↔S18 · S1↔S21 · S8↔S23
SUIT YIPRANMA tam 3 sabit bölge: iki avuç koyu · sol omuz şeridi ·
              sağ baldır bandı — her karede aynı [D42]
IŞIK TAKVİMİ  S0-S9 gümüş-gri → S10-S12 ikindi → S13 günbatımı (kızıl
              istisna #1) → S14-S18 alacakaranlık/gece → S19-S21 gece →
              S22 gece sonu → S23-S24 şafak (kızıl #2-3) — MONOTONİK
SES REGISTER  HUMAN 0 · MACHINE 4 (S2·S10·S21·S22, suit hoparlörü,
              düz sentetik, radyo-ince) · müzik promptlarda 0 (post)
```
