# 🎶 THE STANDING WIRE — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR YOL olarak okumalı — bir tuhaflık, bir arıza
    ya da bir tehdit olarak değil. Tel korkutmaz; ÇAĞIRIR."

TEMPO:        48 BPM — sahne uzunluğuna HİZALI (§14)
              48 BPM'de vuruş 1,25 s · 4/4 ölçü 5,0 s · 10 s sahne = TAM 2 ÖLÇÜ
              Izgara sıfırı 9,0 s (S1'in başı). Her sahne sınırı bir ölçü
              çizgisine düşer: 9 + n×5 (n = 0…48).
SÜRE:         249 s = hook 9 s + 24 × 10 s
              Müzik 9,0 s'de girer, 249,0 s'de biter → çalınan 240 s = 48 ölçü
MÜZİKSİZ SAHNE: S0 (0-9 s) · S21 · S22 · S23 (209-239 s)
              ⛔ §10 en az bir tane ister; burada dört tane var ve ikisi
                doruğun kendisidir [YANASMA §2.1: temasın sesi YOKTUR]
SUB-BASS:     41 Hz temel + 82 ve 123 Hz oktav/beşli eşlikçileri
              (§15.1a MISSING FUNDAMENTAL: 82+123+164 Hz yeterince güçlü
               konursa telefon hoparlöründe beyin 41 Hz'i İŞİTİR)
VURUŞ NOKTASI: 2 tane — az olan güçlüdür (§13)
              ① 169,0 s (S17 başı · ölçü 32) — katman DÜŞER, eklenmez
              ② 239,0 s (S24 başı · ölçü 46) — filmin TEK çözülmesi
              ⛔ Halkanın bırakıldığı an (173,0 s) BİLEREK vurgusuzdur:
                mickey-mousing yasağı (§13) ve bedelin sessiz kalması.
```

---

## 📋 §17 FİLM MÜZİĞİ KÜNYESİ

```
FİLM:                 THE STANDING WIRE · 249 s · 25 sahne (hook 9 s + 24×10 s)
NOVUM OKUMASI:        "İzleyici bu görüntüyü BİR YOL olarak okumalı."
                      ⛔ Tehdit değil, arıza değil, gizem değil. Tel bir
                        merdivendir ve müzik onu öyle çerçeveler.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ: EMPATİK — ama OLAYA değil IŞIĞA bağlı.
                      Skor tırmanışı takip etmez; İRTİFAYI takip eder.
                      Katmanlar ışık takvimiyle birlikte açılır ve
                      kapanır (C bloğu IŞIK TAKVİMİ). Bu yüzden S17'de
                      bedel ödendiğinde müzik TEPKİ VERMEZ, yalnız
                      incelir — kadın kaybetti, irtifa kaybetmedi.
TEMPO:                48 BPM → sahne başına 2 ölçü (§14 tablosu)
TONALİTE:             D doryen. ÇÖZÜLMEZ. Film boyunca tonik (D) hiçbir
                      ölçünün başına düşmez; tek çözülme 239,0 s'dedir
                      ve tam olarak bir kez olur.
SESSİZLİK SAHNESİ:    S21 · S22 · S23  (müzik 214,0 s'de biter — doruğun
                      başlangıcından 5 s önce; §11 ITPRA + YANASMA §2.1'in
                      "doruktan ÖNCE susar" kuralı)
ÇÖZÜLMEYEN CÜMLE:     S17'de (169,0 s) yarım kalır — üst yaylı hattı bir
                      yükselen dörtlünün ortasında kesilir ve o cümle
                      239,0 s'ye kadar tamamlanmaz.
KAPANIŞ:              fade out YOK. 249,0 s'de ölçü çizgisinde KESME.
FREKANS TABANI:       sub 41 Hz + oktav eşlikçileri 82 Hz ve 123 Hz
KATMANLAR:            4 katman — aşağıda, sahne aralıklarıyla
LUFS HEDEFİ:          −14 nihai · −17 müzik yatağı
REVERB KARARI:        ⭐ ÜÇ AYRI KARAR, ortam kartıyla birebir:
                      S1-S18  ince atmosfer → KISA, kuru-yakın oda (0,8 s),
                              çünkü 1,0 kPa'da ses taşımaz
                      S19-S23 vakum → müzik zaten YOK (214 s'den sonra);
                              214 s'ye kadarki S19-S20 bandında reverb
                              TAMAMEN KURU (0 s) — dış dünya sessiz
                      S24     basınçlı iç hacim → kısa, sıkı, küçük oda
                              (0,4 s) — hava geri geldi
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (Suno v4 alternatif)
GENRE: sparse cinematic ambient / minimal orchestral, no percussion
TEMPO: 48 BPM, 4/4, strict grid, no rubato, no ritardando

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. LOW DRONE (9 s) — a bowed double bass sustaining D, doubled by a
     quiet companion tone one and two octaves higher so the weight
     survives on a phone speaker; the low fundamental adds depth on
     headphones but is never the only carrier of the emotion.
  2. HIGH SUSTAIN (59 s) — one glass-harmonica-like tone entering on A,
     very quiet, never rising in pitch, never vibrato.
  3. PULSE (119 s) — a single muted plucked string on every second beat,
     dry and close, no reverb tail, no crescendo.
  4. UPPER LINE (139 s) — a solo viola line that climbs a fourth and
     stops before completing it; it never resolves until the coda.

DYNAMIC SPREAD — sahne ızgarasıyla birebir (ölçü = 5,0 s):
    0-9    s (S0)      SESSİZLİK — müzik yok. Hook sessiz açılır.
    9-59   s (S1-S5)   yalnız katman 1. −24 LUFS. Hareketsiz.
   59-119  s (S6-S11)  katman 2 girer. −20 LUFS. Hâlâ hareketsiz.
  119-139  s (S12-S13) katman 3 girer. −18 LUFS. İlk nabız.
  139-169  s (S14-S16) katman 4 girer, dörtlüyü tırmanmaya başlar. −17 LUFS.
  169-179  s (S17)     ⭐ katman 4 CÜMLENİN ORTASINDA KESİLİR ve geri
                        gelmez. Katman 3 durur. Kalan: 1 ve 2. −22 LUFS.
                        ⛔ Bu bir vuruş noktasıdır ama bir VURGU değildir:
                          düşen halkaya hiçbir ses eşlik etmez.
  179-214  s (S18-S20) yalnız katman 1 ve 2, giderek incelir. −26 LUFS.
  214-239  s (S21-S23) ⭐ MUTLAK SESSİZLİK. Müzik yok, yatak yok.
  239-249  s (S24)     katman 1, 2 ve 4 birlikte döner; katman 4 yarım
                        kalan dörtlüyü TAMAMLAR ve D'ye çözülür — filmin
                        tek çözülmesi. −16 LUFS. 249,0'da ölçü
                        çizgisinde keser. Fade out yok.

SYNC RULE: the grid starts at 9.0 s and every bar line falls on a scene
boundary (9 + n × 5.0 s). Nothing in the score reacts to any event on
screen: no stings, no swells timed to movement, no hits on impacts. The
score follows altitude, not action.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO taiko, NO choir, NO trailer hits.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔇 SESSİZLİK KARARI [⛔ DERS 180 — bıçak KURGUDADIR]

```
⛔ PLANLI SESSİZLİK VİDEO MODELİNDEN İSTENMEZ. Veo'nun yerel sesi mutlak
   sessizlik teslim etmiyor; iki film üst üste doruğunu bu yüzden kaybetti
   (THE UPWARD FALL · THE HEALING GROUND, 04.09.2026). Bıçak kurgudadır.

KURGUDA HARD MUTE:  sn 214,0 – 239,0     (25 s)
  ⛔ Bu iki sayı IZGARADAN HESAPLATILDI, elle yazılmadı:
     214,0 = 9,0 + 41 × 5,0   (ölçü 41 · S21'in başından 5 s önce)
     239,0 = 9,0 + 46 × 5,0   (ölçü 46 · S24'ün tam başı)
  Kapsadığı sahneler: S21 (209-219) · S22 (219-229) · S23 (229-239)
  ⭐ Mute S21'in İÇİNDE başlar, S22'nin başında değil — sessizliğin fark
    edilmesi 1-2 saniye ister (müzik kılavuzu §10 · YANASMA §2.1).

⛔ MUTE TEK BAŞINA YETMEZ — MİKS DE SUSAR:
   214,0-239,0 arasında yalnız müzik değil, ORTAM YATAĞI da kesilir.
   Kalan tek kanal kask içi nefestir ve o da −34 dB'nin altındadır.
   Gerekçe: bu bant zaten VAKUMDUR (C bloğu ATMOSFER) — dış ses fiziksel
   olarak sıfırdır. Sessizlik burada bir efekt değil, bir doğruluktur.

⛔ TESLİMDEN ÖNCE ÖLÇÜLÜR — ÜÇ EŞİKTE [D180 ③]:
   rapor_kontrol.py --olcum-sessizlik 214-239
   silencedetect −50 / −40 / −30 dB
   Aralık üç eşiğin hiçbirinde çıkmıyorsa 🔴 TESLİM KUSURU ve master
   YENİDEN İHRAÇ edilir. Komut QA_SPEC E bloğu KAPI ②'de.
   ⭐ Ölçüm filmin sessiz DİBİNİ de raporlar (saniye + dB): "sessizlik yok"
     ile "sessizlik var ama beş saniye geç" farklı kusurlardır.

⛔ KESİLEMEZ: 214,0-239,0 bandı kurguda kısaltılamaz. Kısalırsa doruk
   filmin gürültülü anlarından biri olur — D180'in iki vakası tam budur.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      YOK — bu filmde diegetik yapay ses kullanılmıyor.
               HUMAN 0 · MACHINE 0 · TELSİZ 0.
REPLİK SAYISI: 0
REPLİK ZAMANLARI: uygulanmaz (0 replik). Formül yine de burada durur ve
   bir replik eklenirse koşar [D122]:
   replik(S_n) = 9 s hook + (n−1) × 10 s klip + promptun TIMELINE ofseti
   Elle yazılan her kayıt formülle DOĞRULANIR.

⛔ KART 7 (diyalog) BU FİLMDE YAPISAL OLARAK DÜŞER: konuşacak muhatap yok
  (tek insan) ve söylenecek sayı yok (gösterge yok). Kadraj dışı ses bile
  bir KAYNAK ister; kaynak uydurmak novumun yanına ikinci bir açıklanmamış
  şey koyar [ONERME §3: ihlal sayısı 1].

⚠️ Bu "sessizlik en güvenlidir" DEMEK DEĞİLDİR — o damga 02.09.2026'da
  kartından kaldırıldı, çünkü kanıtı bir N/A'ydı. Bu bir TASARIM kararıdır.
```

### ORTAM YATAĞI — ses dokusu merdiveni (örüntü kırıcı üçüncü sütun)

```
Yatak TEK PARÇA serilir, kliplere bölünmez [D83]. Klip sınırında ölmez.

  S0-S3    (0-39 s)     geniş, alçak hava tonu + çakıl · en dolu bant
  S4-S12   (39-129 s)   ince hava tonu + eldiven/kaya + nefes
  S13-S18  (129-179 s)  neredeyse yok — yalnız giysi ve nefes
  S19-S20  (179-209 s)  DIŞ SES SIFIR — yalnız kask içi
  S21-S23  (209-239 s)  MUTLAK SESSİZLİK (hard mute)
  S24      (239-249 s)  fan yatağı GİRER — hava geri geldi

⭐ Merdiven MONOTONİK olarak incelir ve tek bir yerde geri döner: S24.
  O dönüş filmin "vardı" cümlesidir ve müziğin çözülmesiyle aynı karede.
⛔ Teslimden önce temas bölgesi (219-229 s) KULAKLA dinlenir. Dijital
  mutlak sıfır ile planlı sessizlik farklı şeylerdir; Cold Burn'de 20 s'lik
  dijital sıfır miks hatası çıktı [D83]. Burada mutlak sıfır İSTENİYOR ve
  bu bilinçli — ölçüm o yüzden üç eşikte koşuyor.
```

## 🧪 KONTROL

```
□ §17 künyesi ÖNCE yazıldı ✅
□ Tempo sahne ızgarasına hizalı: 48 BPM → 10 s = 2 ölçü ✅
□ Izgara sıfırı ve her sınır ölçü çizgisinde (9 + n×5) ✅
□ Müziksiz sahne ≥1: dört tane (S0 · S21 · S22 · S23) ✅
□ Sub-bass tek taşıyıcı DEĞİL — oktav eşlikçileri yazıldı [§15.1a] ✅
□ Vuruş noktası 2 · ikisi de ölçü çizgisinde · bedel anı vurgusuz [§13] ✅
□ KURGUDA HARD MUTE satırı var ve sayılar ızgaradan hesaplatıldı [D180 ①] ✅
□ Ölçüm komutu ve üç eşik yazıldı [D180 ②③] ✅
□ Reverb kararı ortam kartıyla birebir (üç ayrı karar) ✅
□ Çözülme İNSAN sahnesinde, temasta değil [YANASMA §2.1] ✅
□ Fade out yok, ölçü çizgisinde kesme ✅
```
