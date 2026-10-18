# 🎞️ THE_FURNACE_GATE — DİKEY FRAGMAN · 0:40 · 9:16

> Kural kaynağı: `kilavuzlar_ve_sistem_dosyalari/FRAGMAN_KILAVUZU.md` — **§2 SHORTS FRAGMAN KARTI** + §1 değişmezleri.
> Kaynak film 16:9, fragman 9:16 → §1.1: **kırpma yok, her çekim dikey oranda SIFIRDAN üretilir.**
> Fragman yeni bir film değildir: kendi konsepti, novum'u, hikâyesi yoktur. Tek işi filmin vaadini kurmak ve **cevabı vermeden bırakmaktır.**
> Üretim yolu filmle aynı (FILM.md künye): GPT Image (kare) → Gemini Omni 1.1 Flash (10 s video). Referanslar filmin referanslarıdır (FILM §3), ayrı referans üretilmez.
> Dosya klasör içi → film sayımına girmez (FRAGMAN §0). `PROMPTLAR/` dışında durur: `film_dogrula.py` ve `medya.py` o klasördeki her dosyayı film çekimi sayar.

```
BİÇİM     9:16 dikey · 0:40 · 4 sahne × 10 s · 8 çekim · 7 kesme (sahne içi 4 + sahne arası 3) · ekran metni 0.0 s · replik 0
SAHİP     "THE_FURNACE_GATE şu filmi birde 40 saniyelik dikey fragman hazırlayalım 4 sahne yani her sahneye max 1 cut koyabilirsin" (17.10.2026)
YORUM     sahne = 10 s'lik yuva; içinde en çok 1 kesme → sahne 1 ya da 2 çekim. Her çekim 10 s üretilir (sahip kuralı 08.10.2026),
          kurguda ZAMAN dilimi alınır; kadraj kırpılmaz, klibin içine kesme atılmaz (FRAGMAN §1.1b mantığı · §1.5).
MEKANİK   ⭐ KISKAÇ (§3)
SORU      "Kapı kapanmadan, ateş yetişmeden — gemi çıkabilecek mi?" (FILM §1 TEK SORU'nun ilk yarısı; film C89-C92'de cevaplar)
ÜRETİM    8 kare + 8 video, her biri en çok 2 deneme = en çok 32 üretim · yeni referans 0 (FILM §3: 1 · 2 · 5 · 6 · 7 · 8 · 10 · 12)
MEDYA     ~/film_medya/THE_FURNACE_GATE/fragman_dikey/{kare,ham,ses,cikti}/ (repoya girmez)
DURUM     KART v2 (Fable, 17.10.2026; v1 → `ODA/FR_kart_v1.md`, eleştiri `ODA/FR_izleyici_1.md` · `FR_dramaturg_1.md` · `FR_teknik-danisman_1.md`)
```

## 0. v1 → v2 (tur 1 birleştirme, Fable)

| Bulgu | Karar |
|---|---|
| Dramaturg B1 ÖLÜMCÜL: "turuncu mu söner, yeşil mi" filmin ortasında (S45-S47) cevaplanan, tahmin edilen soru | mekanik İKİ IŞIK → **KISKAÇ**; soru filmin gerçekten açık kalan sorusu: kapı ve ateş (§3) |
| Dramaturg B2 ÖLÜMCÜL: V4 kaynağı C48 (merkez seçim), kadraj filmde yok (§5 ④) | V4 kaldırıldı; son sahne C20 + C35 (ilk %40, filmde var). C44-C48 seçim/bedel duyurusu spoiler listesine girdi |
| Dramaturg B3 · teknik V4 ÖLÜMCÜL: amber güçlenmesi C69 tükenmesini ima eder | çekirdek yalnız V3a'da, temiz ve kullanılmamış; parlama yok |
| Dramaturg B4 · izleyici 3: fırın-gemi-kapsül bağı kurulmuyor | V1a tek dikey karede tuzağın üçü (ateş · gemi · kapı); V1a → V1b ileri hareketle "içeri" kesilir |
| Dramaturg B5-B6: renk dönüşümü okunur, yeşil sıralar iki kez | yeşil sıra bir kez (V1b); V2b yüz + cam kenarı, sıralar flu |
| Dramaturg B7 · izleyici 4: adam kopuk | V3b alarmda adam kırmızı lambadan kadına döner; V4a camda tek başına kapıya bakar |
| İzleyici 2: ilk 3 s'de insan yok | ölçek şoku (HOOK kılavuzu "dikeyin doğal silahı"): dev ark'ın kıçında küçük tug; insan 14 s'de (ILK_30 C02: en geç 10-20). Açılışta vizör yakın planı ILK_30 §6 yüksek risk → bilinçli |
| İzleyici 3-4: amber nesne kopuk | çekirdek kadının elinde (V3a) ve hemen ardından alarm (V3b): "çaldılar" okunur |
| Teknik ortak kurallar · V2b ÖLÜMCÜL vizör yansıması · V3a ÖLÜMCÜL el-nesne | §11 yazar kuralları (çekim başına ≤2 referans, panel adı, odak bandı, hareket 0,5 s'de başlar, vizör berrak, renk yönle) |
| Dramaturg B9: "mandal" kapının mandalını çağırır | V2a (çekirdek mandalı) çıktı |
| Prompt turu: TD tur 2 (ÖLÜMCÜL 2: V3b siren · V4b açılıyor okunması) · DV tur 1 (CİDDİ 11 · KÜÇÜK 14) | `ODA/FR_birlestirme_1.md`: V4b = V1a'dan düzenleme, kamera kilitli · lamba sabit, tek renk · fırın yönü sapma ⑨ · kepenk sırası · V2a kamera kilitli · V3a amber sabit · V4a derin odak |
| İzleyici tur 2 (`ODA/FR_izleyici_2.md`): 10-14 s turuncu tekrar, yeni bir şey söylemiyor · "mavi ışık nereden geliyor" | V2a ATEŞ → **KELEPÇE** dişi (C20 · C35: gemi kilitli) · V4a'da camın ardındaki kapı halkası okunur (bakış V4b'ye bağlanır). Tur 2 tek cümlesi "kapı da kapanıyor", soru "kapı kapanınca ne olacak?", "evet, izlerdim" ✅ |

## 1. BİLİNÇLİ SAPMALAR — format DNA'sından her sapma (FRAGMAN §1.7)

| # | Kılavuz | Bu fragman | Gerekçe |
|:--:|---|---|---|
| ① | §0 dikey klip 8 s | 10 s üretim, kurguda 4-6 s dilim | sahip kuralı (her çekim 10 s) + sahip isteği 40 s / 4 sahne; toplam 40 s, 24-48 s bandının içinde |
| ② | §2.1 vuruş = klip | 4 vuruş (sahne) · 8 çekim | sahip: sahne içi en çok 1 kesme. Her çekim yine ayrı klip; kesme klip ARALARINDA (§1.5) |
| ③ | §1.3c kaynak lens/kadraj | 8 çekimin hepsi dikey yeniden kadraj | 9:16 sıfırdan üretim zorunlu (§1.1); her satırın "kaynak → yeni" gerekçesi §4 tablosunda |
| ④ | FILM §3 sabit tasarım "kaçış yönü soldan sağa" | V1a · V4b'de eksen DERİNLİK + YUKARI: fırın önde-aşağıda, kapı uzakta-yukarıda | dikeyin kazancı dikey eksendir (§1.1); fragmanda sol-sağ ilişkisi kurulmaz, filmin ekran yönüyle çelişki doğmaz |
| ⑤ | FILM §3 ORTAM SESİ (model sesi AÇIK film) | video promptunda ses cümlesi YOK | fragmanda klip sesi kullanılmaz (replik 0); ses kurguda: müzik + FILM §6 yatakları. Omni sesi atılır |
| ⑥ | plan açılış VO "We came to steal a power core. We left with a ship full of people." | kullanılmaz | cümlenin ikinci yarısı SONUÇTUR (spoiler §2); dikeyde replik 0 varsayılan (§1.6) |
| ⑦ | §1.3 mekanik sicili | KISKAÇ sicile YAZILMADI | eski kılavuzlar düzenlenmez (CLAUDE.md); kayıt bu dosyada + NOTLAR KARARLAR. Akrabası: YAKLAŞMA · KAPANAN KAPILAR (başka filmler; bu filmin ilk fragmanı, §1.3b koşulmaz) |
| ⑨ | FILM §3 MEKÂN IŞIĞI DIŞ "… a warm orange furnace glow from frame-left behind heavy blast ribs" birebir | cümle birebir kalır; V1a V2a V4b'de ardına tek yön cümlesi: "In this vertical view the furnace glow lies in the lower-left of the frame behind the ribs and edge-lights the hull from below." | dikeyde fırın alt-solda; çapa bozulmadan kadraj cümleye uydurulur (DV D1 · TD tur 2 (5); `ODA/FR_birlestirme_1.md`) |
| ⑧ | SHORTS_SISTEM_PROMPTU prompt kalıbı (lens kilidi, "Kamera Mesafesi") | filmin G01 biçimi | çapalar kaynak filmden birebir (§1.4): Reference <No> anahtarı, KİMLİK TABANI, MEKÂN IŞIĞI, DIŞ DÜNYA, ORTAK GÖRÜNÜM; güvenli alan cümlesi eklenir (§5) |

Kaynak filmin ölçüm durumu: hatta medya 0 (referans 0/15). Sahibin hat dışı taslağı (taslak_01, B2-B3) Gemini ile tarandı (NOTLAR TARAMA · SÜREKLİLİK ·
ANLATIM, 16.10.2026); fragmana taşınan dersleri §11'de. Kare üretimi filmin referans onayına (F7a, SHA) bağlıdır.

## 2. ⛔ SPOILER KAPISI — fragmanda ASLA olmayacak kareler (kurguda madde madde 0 kare)

Vuruşlar filmin ilk %70'inden (C01-C67). En ileri kaynak **C35 = %36** ✅

```
⛔ kokpit itirafı · sınıflayıcı · Dione · tether (C37-C43) — omurga sırrı
⛔ çözümün bedeli · karar · ayrılma (C45-C48: "The overload will consume it" · "We lose the core. We take everyone.") — MERKEZ SEÇİM
⛔ çekirdeğin giriş yuvasına konması · kapı gücü · enerji hattı (C58-C61) — ÇÖZÜMÜN MEKANİZMASI
⛔ kapının açılması · açık kapı · mandal · kelepçelerin bırakılması (C62-C72) — çözüm · 5.FOUNDRY `gate open panel` ve `clamps open panel` hiçbir promptta adlandırılmaz
⛔ çekirdeğin aşırı parlaması / tükenmesi / sönük çekirdek (C69 · C73 · C94) — BEDEL · 10.CEKIRDEK `core overheating` ve `core spent` panelleri hiçbir promptta adlandırılmaz
⛔ köprünün geri çekilmesi · Rhea'nın karşıda kalması · Leon'un dönüşü · iskele · ikinci yanaşma (C73-C88) — DORUK, karakterin kaderi
⛔ ark'ın kapıdan çıkışı · purge · özgür iki gemi · "dört bin sinyal sabit" (C89-C96) — FİNAL
⛔ "four thousand" ya da herhangi bir sayı · film adı · yazı — ekranda 0, seste 0
⭐ SORU kurulur, cevaplanmaz: fragman kepenkler kapanırken kesilir; kapının açıldığı hiçbir kare yok.
```

## 3. ⭐ MEKANİK — KISKAÇ

```
Dikey kare bir tuzaktır: AŞAĞIDA ATEŞ, YUKARIDA KAPI, ARADA UYUYANLAR.
Her sahne tuzağın bir dişini sıkar; sahne içi tek kesme dişle içerideki hayat arasında atlar.

  S1  tuzak    V1a ateş + gemi + kapı TEK karede (ateş nefes alır)   → V1b içeride: yeşil noktalı kapsüller (tuzakta ne var)
  S2  KELEPÇE  V2a dev gantri çenesi gövde flanşını kavramış, fırın ışığı çeneye vurur → V2b içeride: bir kadın kapsüllerin camında (birisi biliyor)
  S3  ALARM    V3a kadın çekirdeği beşikten kaldırır (neden buradalar) → V3b kırmızı lamba yanıp söner, adam lambadan kadına döner (tuzak onları fark etti)
  S4  KAPI     V4a adam camdan dışarı bakar                          → V4b üç kepenk içeri kayar; kesilir (loop → V1a)

Soru: kapı kapanmadan, ateş yetişmeden gemi çıkabilecek mi? Cevap (C89-C92) 0 kare.
Mekanik filmi özetlemez: drone, kokpit konuşmaları, plan, kardeşlerin geçmişi yok. Her vuruş yalnız bir diş sıkar.
```

## 4. VURUŞ / KAYNAK EŞLEME

| Sahne | Saniye | Çekim | Rol | Kaynak (FILM §4) | Ekranda görünen | Dikey kadraj · kaynak → yeni (§1.3c) | Referans (≤2, panel) |
|:--:|:--:|:--:|---|---|---|---|---|
| S1 | 0,0-4,0 | V1a | HOOK + AFİŞ | C01 · C12 | alçak açı: önde-aşağıda ağır patlama kaburgalarının arkasında turuncu fırın ışığı yerinde kabarır; üstte dev fildişi ark'ın kıçı beşikte, gövdesi derinliğe ve yukarıya uzanır; en yukarıda üç kepenkli dev dairesel çıkış kapısı kısmen kapalı; kıçın yanında küçük tug (ölçek) | kaburgalar ve ışık y %55-75 · kıç y %35-55 · kapı halkası y %8-28, x %20-65 · C01 aşırı geniş yan + C12 arka-¾ → alttan derin perspektif; gerekçe: tuzağın üç parçası tek dikey eksende | 5.FOUNDRY `wide exterior panel` · 6.ARK `stern panel` |
| S1 | 4,0-10,0 | V1b | — | C09 | diz hizasından kapsül koridoru: iki yanda ~7'şer opak kapaklı kapsül, her birinde soluk yeşil nokta; yavaş ileri takip | kaçış noktası x ≈ %40, y ≈ %35 · C09 yatay derin → dikey derin; gerekçe: sıra dikeyde boydan okunur | 8.KRIYO `aisle panel` |
| S2 | 10,0-14,0 | V2a | KELEPÇE | C20 · C35 | dev rijit gantri kolu kadrajın üstünden iner; geniş tutma çenesi ark'ın fildişi gövde flanşını sımsıkı kavrar; kamera çene boyunca yavaş süzülür; fırının turuncu ışığı aşağıdan çenenin kenarına bir kez yerinde kabarıp vurur ve çekilir; çene, kol, gövde kımıltısız | çene orta bant, x sol-orta · C20 (camdan kollar) + C35 (kollar kilitli) → alttan orta-yakın dış; gerekçe: yeni diş — gemi kilitli (izleyici tur 2: ateş tekrarı yeni bilgi vermiyordu) | 5.FOUNDRY `wide exterior panel` · 6.ARK `side view panel` |
| S2 | 14,0-20,0 | V2b | — | C08 | kadın (orta plan, sol profil) koridorun sol duvarındaki kriyo gözlem camının önünde; camın ardında yeşil noktalar flu; belinden cama hafifçe eğilir; yeşil ışık kaskının yan kenarında | cam kadraj solunda boydan · kask y %25-45 · C08 orta yatay → orta dikey; gerekçe: yüz güvenli bantta, sıralar V1b'de zaten gösterildi | 2.RHEA `left-profile close-up panel` · 7.KORIDOR `cryo window panel` |
| S3 | 20,0-25,0 | V3a | ALARM | C26 | kasada kadının iki eldiveni çekirdeği (kulpu + kasa kenarı, kavrayış kurulu) beşikten birkaç santim düz yukarı kaldırır; amber cam merkez; göğüs askısı boş | eller + çekirdek y %52-70 · yüz y %22-40 · C26 orta yatay → orta dikey; gerekçe: el-nesne-yüz tek dikey eksende | 2.RHEA `front full-length panel` · 10.CEKIRDEK `core object panel` |
| S3 | 25,0-30,0 | V3b | — | C27 · C28 | kasa kapısı: üstünde tek kırmızı acil lamba yavaşça yanıp sönmeye başlar; adam (orta plan) kapının yanında lambaya bakar, sonra başını birkaç derece kadraj soluna (kadına) çevirir | lamba y %15-25 · adamın kaskı y %30-50 · C27 iki kişi → tek kişi; gerekçe: iki yüz tek dikey karede kimlik ve klon riski (taslak C48) | 1.LEON `face close-up panel` · 10.CEKIRDEK `vault door and crate panel` |
| S4 | 30,0-34,0 | V4a | KAPI | C20 · C19 | kontrol odası: adam arka güçlendirilmiş camın önünde sağ profil; camın ardında dev dairesel kapının halkası ve üç kepengi yumuşak odakta ama tanınır; soğuk mavi kapı ışığı yüzüne düşer; bakışı yavaşça yukarı, halkaya kayar | kask y %25-45 · C20 orta → orta dikey; gerekçe: bakış V4b'ye bağlanır | 1.LEON `right-profile close-up panel` · 12.KONTROL_ODASI `wide room panel` |
| S4 | 34,0-40,0 | V4b | SORU | C35 | **V1a'nın AYNI kadrajı** (onaylı V1a karesinden düzenleme): kaburgalar, kıç, gövde, tug, gezegen yerinde; kepenkler yaklaşık yarı kapalı; kamera kilitli, üç eşit kepenk düz raylarında merkeze doğru kayar, açıklık daralır; kayış sürerken kesilir | V1a bantları · C35 geniş yan → V1a kadrajı; gerekçe: loop eşi iki ayrı üretimde tutmaz (TD tur 2 (3)); burun uydurma riski kalkar | `kare/V1a.png` (onaylı) · 5.FOUNDRY `wide exterior panel` |

Kişiler adla anılmaz (ekranda ad yok; promptta "the man" / "the woman"). İki kişi hiçbir karede birlikte değil (taslak_01 C48 klon dersi).

## 5. GÜVENLİ ALAN — 9:16 (SHORTS_SISTEM_PROMPTU güvenli alan haritası)

```
1080×1920 eşdeğeri: alt 484 px (y > %75) ve sağ 242 px (x > %78) arayüz altında; üst ~%12 sekmeler.
KURAL  · yüz, el, çekirdek, kapı halkası, lamba ve yeşil nokta kümelerinin odak kısmı y %8-72 · x %12-70 içinde (§4 tablo değerleri)
       · kişi çekimlerinde promptta birebir: "No part of the figure falls into the bottom quarter of the frame."
       · alt çeyrek yalnız önemsiz yüzey: kaburga dipleri, zemin, buhar, beşik dibi
       · kamera itişi hafif (≈ %12-15 ölçek): itiş alt bantta duran nesneyi alt çeyreğe iter
KAPAK  Shorts kapağı V1a karesidir: 120 px genişlikte elle test (FRAGMAN §2.2 ⑥) — ateş · gemi · halka ayrı öbekler
```

## 6. LOOP SATIRI (SENARYO_VE_VIRAL_KAMERA §5)

```
① KADRAJ  V4b = V1a'nın aynı kadrajı (V1a.png'den düzenleme): son karede kepenkler yarıdan fazla kapalı ve kayıyor
          → V1a ilk karesi: aynı açı, kepenkler üçte bir kapalı. Kesme yalnız kapının durumunu değiştirir.
② HAREKET V4b donmaz: kepenkler kayarken kesilir; V1a hareketle başlar (ışık kabarıyor).
③ SES     müzik kadansla bitmez; 39,0-40,0 düşük katman ya da 1 s sessizlik (besteci).
④ JENERİK yok — film adı platform başlığında yaşar.
⑤ IŞIK    V4b'nin açıklığı V1a'nınkinden dar → loop "aynı tuzağın yeni turu" okunur (§5 ⑤ kompozisyonla loop). Kepenk sırası: V1a üçte bir · V4a yarı · V4b yarı → daha dar (DV D5).
```

## 7. KURGU — kesim listesi (taslak; deneme seçildikten sonra kurgucu kesinleştirir)

| Çekim | Fragman saniyesi | Kliptan dilim (10 s klip) | Kesme |
|:--:|:--:|:--:|---|
| V1a | 0,0-4,0 | 0,0-4,0 | sert · kamera yukarı-ileri süzülürken |
| V1b | 4,0-10,0 | 0,0-6,0 | sert · S1 → S2 |
| V2a | 10,0-14,0 | 0,0-4,0 | sert · ışık tepedeyken |
| V2b | 14,0-20,0 | 0,0-6,0 | sert · S2 → S3 |
| V3a | 20,0-25,0 | 0,0-5,0 | sert · kaldırma bittikten sonra |
| V3b | 25,0-30,0 | 0,0-5,0 | sert · S3 → S4 |
| V4a | 30,0-34,0 | 0,0-4,0 | sert · bakış yukarı kayarken |
| V4b | 34,0-40,0 | 0,0-6,0 | loop → V1a · kepenkler kayarken |

Dilimler klibin başından alınır; promptlar ana hareketi 0,5 s'de başlatır ve dilimin İÇİNDE bitirir, klibin kalanı yedek kuyruktur (kurgucu kaydırabilir).
Hız rampası, ağır çekim, klip içi kesme yok.

## 8. SES + MÜZİK

```
YATAK   FILM §6 birebir, kurguda: V1a V2a V4b Y1 (dış, vakum: tasarım tonu) · V1b Y4 (kriyo) · V2b Y3 (koridor) · V3a V3b Y7 (kasa) · V4a Y6 (kontrol odası)
EFEKT   V3a beşikten kalkış (basınçlı iç, hafif metal sürtünme) · V3b alarm lambası (kasa içi düşük elektrik tıkırtısı; siren yok) · dışta gerçekçi ses yok
MÜZİK   tek cue, tek tırmanış (FRAGMAN §2) — besteci: kesmeler 4 · 10 · 14 · 20 · 25 · 30 · 34; 34-40 çözülmeden asılı; loop uyumlu son
REPLİK  0
```

Müzik planı: `ODA/FR_besteci_1.md` (besteci tur 1, sonnet) — 120 BPM, D merkezli (D2 + D3 telefonda duyulur), kesmeler 0,5 s ızgarasında;
tek tırmanış, 34,0'da tek ağır darbe, 34-39 D–E♭–A asılı küme, 39-40 çıplak D drone, 40,0 sert kesme → 0,0 aynı D drone (loop dikişi duyulmaz;
seçenek B: 39-40 mutlak sessizlik). S2'nin müzik olayı (10-14 "ısı katmanı") V2a'da çeneye vuran tek fırın ışığına oturur (kart v2 KELEPÇE değişikliği).
Flow Music 40 s vermezse: dikiş 34,0 ya da 0-14 · 14-30 · 30-40 üç parça (besteci §6).

### MÜZİK PROMPTU — Flow Music'e yapıştırılır (besteci tur 1, 17.10.2026)
```text
Original dark cinematic sci-fi trailer cue, 40 seconds, 120 BPM, one continuous build, dry and close with no reverb tail. Open at 0s on a low D drone (D2 plus octave D3 so phones can hear it) at very low level, with a slow sub-bass machine pulse. Cello and double-bass pedal enters at 2s. Sparse metallic percussion hits land on cuts at 4s, 10s, 14s, 20s, 25s, 30s and 34s. Rising pressure to 34s with one single heavy hit, plus rare warm synth notes at 11s, 20s and 33s. From 34s to 39s hold an unresolved D-Eb-A cluster, no cadence, pulse slowing. At 39s drop to the bare low D drone only and hard cut at 40s, no fade-out, so the end loops into the quiet opening. No vocals, no recognizable melody from an existing film. [Instrumental]
```

## 9. ÜRETİM SIRASI (FRAGMAN §2.2)

```
0. Ön koşul: filmin referansları 1 · 2 · 5 · 6 · 7 · 8 · 10 · 12 üretilmiş ve onaylı (FILM §3 SHA) — film F7a
1. AFİŞ İLK: V1a (kapı — tuzağın üç parçası tek dikey karede okunmuyorsa fragman yoktur, kalan vuruşlara üretim harcanmaz) → dur, Fable + devamlilik bakar
2. SORU ikinci: V4b — karesi ONAYLI V1a.png'den düzenlemeyle (aynı kadraj, kepenkler yarı kapalı)
3. kalanlar: V3a (en riskli kişi çekimi; kavrayış kare kapısı) · V3b (siren riski) · V2b · V4a · V2a · V1b
Kare: 9:16 piksel — önce doğrudan 1152×2048 (kırpmasız); ChatGPT 1024×1536 verirse merkezden 864×1536 (yanlar 80'er px) — GPT_IMAGE_OMNI §13
Dosya: fragman_dikey/kare/V1a.png … · video fragman_dikey/ham/V1a_d1.mp4 · _d2.mp4 · Omni'ye yalnız kare yüklenir
```

## 10. KURGU KAPISI (FRAGMAN §1.2 · §2.2)

```
□ SPOILER LİSTESİ (§2) — her kalem 0 kare
□ TEK CÜMLE TESTİ — ilk kez izleyen biri tek cümleyle anlatır; cümlede cevapsız soru kalır
□ İMZA TESTİ — V1a (ateş · gemi · kapı tek dikey kare) kurguda var ve ters çevrilmemiş
□ PAKETLEME TESTİ — Shorts başlığı ve açıklaması olay dizisi anlatmaz (VIRAL_BASLIK_VE_ACIKLAMA_PROMPT TEASER modu); uzun film linki SABİT YORUMDA
□ çekim sayısı 8 · süre 40,0 s · ekran metni 0,0 s · güvenli alan (§5) · loop dikişi üst üste bindirilerek (§6)
```

## 11. YAZAR KURALLARI (teknik-danisman tur 1 + taslak_01 dersleri)

```
1. Referans: çekim başına ≤2, her biri panel adıyla; karede: "A single full-bleed vertical photograph of one scene; the references supply only identity and design."
2. Konum: odak §4 bantlarında; itiş hafif; pencere ve yeşil ışık SOLDA; baş dönüşü küçük (≤ ~20°), bakış + hafif baş eğme.
3. Işık: vizör berrak, gözler görünür; yeşil/amber yüze YANDAN ya da ALTTAN ve renk adıyla; vizörde en çok dar yansıma bandı.
   Dışta fırın ışığı kaburgaların ARKASINDA "swells in place" (C12 kalıbı); exhaust · rises · flames · fire · burst · plume · smoke yazılmaz
   (taslak C44: vakumda alev ve duman çıktı).
4. Hareket: tek ana hareket 0,5 s'de başlar, bitiş saniyesi yazılır, kare hareketin hazır durumunu gösterir; 10 s 2-4 vuruş, boşluksuz, son vuruş donmaz.
5. Çekirdek: kullanılmamış, temiz grafit kasa, fildişi köşe korumaları, amber cam merkez; boyutu §3 tarifi (taslak C26→C27: kutu göğüste küçüldü).
   V3a'da göğüs askısı BOŞ. Parlama/ısı kelimesi yok.
6. Kişi: KİMLİK TABANI birebir ("the man" / "the woman"); karede tek kişi; yürüme yok (taslak C48 klon).
7. Olumsuz cümle yok ("no X" tutmuyor) — tek istisna güvenli alan cümlesi. Prompt gövdesinde çekim kodu, büyük harfli etiket, başlık yok; kadrajda yazı/rakam yok.
8. Çapalar birebir: ROL SÖZLÜĞÜ anahtarı, MEKÂN IŞIĞI, DIŞ DÜNYA (uzay görünen dış karede), ORTAK GÖRÜNÜM her Görsel ve Video'nun sonunda. Ses cümlesi yok (sapma ⑤).
```

## 12. PROMPTLAR

> Kaynak: `ODA/FR_goruntu-yonetmeni_2.md` (goruntu-yonetmeni tur 2, sonnet; tur 1 `ODA/FR_goruntu-yonetmeni_1.md`), birleştirme `ODA/FR_birlestirme_1.md`.
> Eleştiri: `ODA/FR_teknik-danisman_2.md` · `ODA/FR_devamlilik_1.md`; yazarın KABUL/RED cevapları `_2.md` sonunda (RED: DV D10 · D25 — ikisi de V2a/V4b yeniden tasarımıyla düştü).
> Fable düzeltmesi (yerleştirmede, 17.10.2026): V4b Video 3-6,5 s'ye yıldız ipucu ("the stars … disappearing one by one behind the advancing blades") ve YEDEK kamera süzülmesi → kilitli kamera
> (süzülme + daralma "açılıyor" okunur, TD tur 2 V4b ÖLÜMCÜL) · V1b V3a Görsel'e "All surfaces are plain and unmarked." (DERS Y8) · V4a Video üçüncü "slowly" çıktı (DERS Y10: üç kez slow hareketi dondurur). V3b'de yazarın "the light always landing on the same places" sapması kabul (aynı anlam, "travelling" kelimesi yok).
> Mekanik kontrol (Fable, python): 16 blok ≤ 2.500 karakter · ORTAK GÖRÜNÜM her bloğun sonunda birebir · KİMLİK TABANI V2b V3a (kadın) V3b V4a (adam) birebir ·
> DIŞ DÜNYA V1a V2a V4a V4b · MEKÂN IŞIĞI DIŞ birebir + yön cümlesi V1a V2a V4b · vuruşlar 0-10 boşluksuz, 2-4 vuruş, her biri ≥ 2 s · yasak kelime 0 · ad 0 · ses cümlesi 0.

### V1a — Ateş, gemi ve kapı tek dikey karede

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V1a.png
DİLİM     kurguda klipten 0,0-4,0 s
```

> Not: Kaynak C01 + C12, alttan derin perspektife çevrildi (kart sapma ④). Kaburgalar ve en güçlü fırın ışığı ALT-SOLDA (DV D1), kıç merkezin biraz sağında, tug kıçın sağ yanında, kapı halkası üst kenardan uzak ve biraz solda. Halka koyu grafit yapı, açıklığı siyah uzay; gaz devi ayrı cümlede arka planın sağ altında yumuşak eğri parıltı (halka–gezegen karışmasın, TD T01). Kepenkler yaklaşık üçte bir kapalı (V4a yarı, V4b yarı → sıra doğru yönde).
> Işık karede soluk başlar, ilk 3 s içinde yaklaşık iki katına çıkar (4 s dilimde okunur). Vuruşlar 0-2,5 · 2,5-6 · 6-10. Bu kare V4b'nin tabanıdır: ONAYLANMADAN V4b karesi üretilmez.

#### Görsel
```text
Reference 5 (foundry): take the heavy black blast ribs, the orange furnace trench and the huge circular exit gate with its three rigid radial sliding shutters from it, using the wide exterior panel. Reference 6 (ark): take the stern with its two big blue rear engine housings and the long ivory segmented hull from it, using the stern panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Low-angle vertical view on a 35 mm lens from just below the foundry's blast ribs, the camera looking steeply up and forward in strong perspective. Across the lower band of the frame, weighted toward the lower left, the heavy black blast ribs stand rigid in straight rows, and the orange furnace trench glows behind them at a faint glow, strongest at the frame's left edge. In the middle band, slightly right of centre, the ark's stern hangs rigid with its two dark blue rear engine housings, and its long ivory segmented hull recedes upward from the stern toward the distance. 1 small salvage tug, a broad short ivory wedge with a single narrow orange nose band, is docked at the ark's starboard stern port on the right-hand side of the stern, small against the hull. In the upper third of the frame, clear of the very top edge and slightly left of centre, the colossal circular exit gate, a dark graphite structure, stands with its three rigid radial sliding shutters about one third closed around a wide circular opening that shows black space; the blue gas giant lies far behind it as a soft curved glow at the lower right of the background. The bottom quarter of the frame holds only the dark bases of the ribs, and all surfaces are plain and unmarked. The frame holds only the ribs, the ark, the tug, the exit gate and the planet. Everything hangs in deep black space with sparse stars, and a huge curved blue gas giant fills the far background. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. In this vertical view the furnace glow lies in the lower-left of the frame behind the ribs and edge-lights the hull from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-2.5 s: The camera drifts very slowly upward and forward along the ark from the first moment, and at about 0.5 s the orange furnace glow behind the heavy blast ribs at the lower left begins to swell in place from a faint glow to about twice its strength within the first three seconds, lighting the rim of each rib. 2.5-6 s: The swell reaches the underside of the ark's stern and the small docked tug, a warm orange edge-light on the ivory hull from below, while the glow itself stays behind the ribs; the ribs, the hull, the tug and the three one-third-closed shutters of the exit gate stay rigid. 6-10 s: The glow eases back behind the ribs and the drift carries on upward along the ivory hull toward the circular exit gate. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): kamera kilitli kalır (yalnız ışık hareket eder); ilk vuruş: "0-2.5 s: The camera holds its low angle while at about 0.5 s the orange furnace glow behind the heavy blast ribs at the lower left begins to swell in place."

---

### V1b — Tuzağın içinde uyuyanlar var

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/8.KRIYO_v1.png · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V1b.png
DİLİM     kurguda klipten 0,0-6,0 s
```

> Not: Kaynak C09 (çözülmüş, en güvenli). Dikeyde diz hizası; kaçış noktası kart değeriyle (x≈%40, y≈%35) kelimelerle yazıldı (DV D6). Sıra sayısı ~7/yan (erime riski); yeşil nokta her cümlede "dim green". Alt çeyrek yalnız zemin ve buhar.
> Vuruşlar 0-3 · 3-6 · 6-10, yavaş alçak ileri takip baştan sürer; kapaklar açılmaz.

#### Görsel
```text
Reference 8 (cryo hall): take the rows of identical rigid ivory sleeping pods with opaque charcoal lids, the dim green status dots, the navy rails and the pale floor vapor from it, using the aisle panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Deep vertical view on a 28 mm lens at knee height along the central aisle of a huge pressurized cryo hall, the aisle running from the lower centre of the frame toward a vanishing point slightly left of centre, about a third of the way down the frame. About 7 identical rigid ivory sleeping pods stand in a row on each side of the aisle, each with an opaque, sealed charcoal lid and one dim green status dot, each between fixed navy rails, receding in strong perspective toward the dim distance; the rows continue as soft shapes beyond the seventh pod. Every sleeper stays completely hidden inside its sealed pod, and the hall holds only the pods, the rails and the lamps. The bottom quarter of the frame shows only the plain floor with thin pale vapor lying along it. All surfaces are plain and unmarked. The light is readable amber aisle lamps, cool blue walls, and dim green status dots on every pod. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-3 s: A slow low track glides forward at knee height down the central aisle from the first moment, the sealed pods sliding past on both sides, each dim green status dot gliding by in turn. 3-6 s: The track continues and the repeating rows of sealed pods draw steadily past toward the vanishing point, every lid sealed and every dot dim green. 6-10 s: The track carries on deeper into the hall and more rows open ahead in the dim distance while the thin pale floor vapor drifts slowly along the aisle. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): yan başına sıra sayısı ~5'e iner (sıraların erimesi); kare promptunda "About 7" yerine "About 5".

---

### V2a — Gemi kilitli

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V2a.png
DİLİM     kurguda klipten 0,0-4,0 s
```

> Not: C44 değil; kart v2 izleyici tur 2: 10-14 s turuncu tekrar. V2a KELEPÇE dişi. Kaynak C20 · C35 (iki gantri kolu kilitli); açılan ya da kalkan çene yok, `clamps open panel` anılmaz.
> Çene iki yarım + ince dikiş, flanşın iki yüzüne bastırılmış, koyu çene ↔ açık flanş renkle ayrık (TD T03: kaynaşma/açılma riski). Kol düz dikey. Kamera KİLİTLİ (hareket = fırın ışığı); kamera süzülmesi yedekte. Kaburgalar ve ışık alt-solda. Işık tepesi 2-4 s (kurgu 4 s'de keser). Vuruşlar 0-2 · 2-4 · 4-7,5 · 7,5-10.

#### Görsel
```text
Reference 5 (foundry): take the enormous rigid gantry clamp arm with its broad gripping jaw locked on the ark, the heavy black blast ribs and the orange furnace trench from it, using the wide exterior panel. Reference 6 (ark): take the long ivory segmented hull with its external hull flange from it, using the side view panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Medium-close low-angle vertical view on a 35 mm lens from below, the camera looking up at the ark's ivory hull. One enormous rigid gantry clamp arm of black graphite descends in a straight vertical line from above the top edge of the frame, and its broad black graphite gripping jaw, two distinct jaw halves with a thin visible seam between them, rests pressed against both faces of the ark's ivory hull flange in the middle band of the frame, slightly left of centre, the dark jaw and the pale flange sharply separated in colour. The ark's long ivory segmented hull runs away to the right and upward behind the jaw. In the lower left of the frame the tops of the heavy black blast ribs stand rigid in a row, the orange furnace trench glowing behind them. The bottom quarter of the frame holds only the dark bases of the ribs, and all surfaces are plain and unmarked. The frame holds only the clamp arm, the hull, the ribs and the planet. Everything hangs in deep black space with sparse stars, and a huge curved blue gas giant fills the far background. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. In this vertical view the furnace glow lies in the lower-left of the frame behind the ribs and edge-lights the hull from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-2 s: The camera holds its low angle, and at about 0.5 s the orange furnace glow behind the blast ribs at the lower left starts to swell in place, lighting the rim of each rib. 2-4 s: The swell reaches its fullest by about 3 s, one warm orange edge-light from the lower left across the lower edge of the jaw, while the glow itself stays behind the ribs. 4-7.5 s: The edge-light on the jaw eases back to a faint rim as the glow settles behind the ribs. 7.5-10 s: The glow rests as a faint rim behind the ribs while the clamp arm, the jaw and the ark stay rigid in cold starlight, the two jaw halves staying pressed on the flange from first to last second. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): kamera yavaş süzülür. Değişen cümle (ilk vuruş): "0-2 s: The camera glides slowly along the gripping jaw toward frame-left from the first moment, and at about 0.5 s the orange furnace glow behind the blast ribs at the lower left starts to swell in place, lighting the rim of each rib."

---

### V2b — Birisi tuzağın içindekileri biliyor

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V2b.png
DİLİM     kurguda klipten 0,0-6,0 s
```

> Not: Kaynak C08. Sol profil (`left-profile close-up panel`): kriyo penceresi koridorun SOL duvarında, kadın cama bakar; sağ yanak, çene ve yara kameradan tamamen uzak, yüz kadraj soluna bakıyor (aynalama önlemi). Kadraj belden yukarı (alt çeyrek, DV D11). Yeşil yalnız vizörde ince kenar yansıması + kask kabuğunun üst kenarında ince rim (vizör tarafı değil, DV D12).
> Eğilme belden, ayaklar sabit, 0,5 s'den başlar. Vuruşlar 0-3,5 · 3,5-7 · 7-10.

#### Görsel
```text
Reference 2 (woman): take her face, the clear pearl helmet and the pearl pressure suit from it, using the left-profile close-up panel. Reference 7 (corridor): take the reinforced cryo observation window in the left wall, the ivory wall and the navy handrail from it, using the cryo window panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Medium vertical shot on a 50 mm lens at eye level in the corridor, from her helmet down to her waist, the cryo observation window running along the corridor's left wall at frame-left, a navy handrail on the ivory wall behind her. No part of the figure falls into the bottom quarter of the frame. She stands in left profile facing the window, her helmet in the upper-middle band of the frame, her right cheek and chin, with its small scar, turned fully away from the camera, her face pointing to frame-left: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. Her harness is empty, her teal bands circle both upper arms, and her badge sits on her left chest toward the camera. Her visor stays clear with her eyes and face fully visible and evenly lit, a thin soft green reflection along its outer edge. Beyond the window glass, softly out of focus, rows of closed ivory pods each carry one dim green status dot. The bottom quarter of the frame shows only the plain corridor floor, and all surfaces are plain and unmarked. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-3.5 s: The camera begins a slow push-in toward her profile from the first moment, and at about 0.5 s she leans a little from the hips toward the window glass, her boots planted. 3.5-7 s: She settles at the glass with her helmet tilted slightly toward the dim green status dots beyond it, the green light resting as a thin rim along the upper edge of her helmet shell, above the visor, while her eyes stay visible through the clear visor. 7-10 s: The push-in carries on slowly and her gaze moves gently along the rows of dim green dots beyond the glass. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): vizörde yansıma yok; yeşil yalnız cam ardında ve kask kabuğunun üst kenarında. Değişen cümle: "Her visor stays clear with her eyes and face fully visible and evenly lit, and the green light falls only as a thin rim along the upper edge of her helmet shell."

---

### V3a — Çekirdek beşikten kalkar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/2.RHEA_v1.png · ref/10.CEKIRDEK_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V3a.png
DİLİM     kurguda klipten 0,0-5,0 s
```

> Not: Kaynak C26. En riskli kişi çekimi (el-nesne). Kavrayış ilk karede kurulu: bir eldiven kulpta, öteki kasa kenarının altında; kaldırma 0,5-3,5 s tek kısa düz; göğüs askısı BOŞ. Mandal açık, kulptan uzakta kare solunda (TD T05/T09, DV D15). Çekirdek kompakt dikdörtgen, iki eldiveni dolduracak boyda, tek üst kulp (DV D16). Amber DERİNLEŞMESİ çıktı: ışık sabit (DV D14, kart B3).
> Vuruşlar 0-3,5 · 3,5-7 · 7-10 (kaldırma dilimde biter).

#### Görsel
```text
Reference 2 (woman): take her face, braid, pearl suit and empty chest harness from it, using the front full-length panel. Reference 10 (core and vault): take the compact graphite core with its ivory corner guards, amber glass center and rigid carry handle from it, using the core object panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Medium vertical shot on a 50 mm lens, the camera at chest height facing her across an open graphite storage cradle whose one broad hinged retaining latch is swung open at frame-left, clear of the carry handle, the cradle's rim at the lower middle of the frame. No part of the figure falls into the bottom quarter of the frame. She stands facing the camera and bending slightly forward over the cradle, her helmet in the upper-middle band and her hands and the core in the middle band: an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She wears white gloves, her teal bands circle both upper arms, her badge sits on her left chest, and an ivory wrist-link sits on her right wrist. Her gaze is lowered through the clear visor to the core, her lips closed and the small scar on her right chin visible. One white glove is already wrapped around the core's single rigid top carry handle and the other white glove is cupped under the casing's edge, the compact rectangular unused graphite core, wide enough to fill both gloved hands, still seated in the cradle with its amber glass center glowing; its casing is clean graphite with ivory corner guards. The carry harness on her chest is empty. The bottom quarter of the frame shows only the plain cradle base and the grated floor. All surfaces are plain and unmarked. The light is low amber lamps on graphite walls and the warm amber glow of the core's glass center. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-3.5 s: The camera begins a slow, shallow push-in from the first moment, and at about 0.5 s she braces her arms under the core and lifts the single core a few centimeters straight up out of the cradle, both gloves keeping the same grips, her forearms tensing as the casing clears its supports; the lift is complete by about 3.5 s. 3.5-7 s: She holds the core steady above the cradle, her shoulders settling under its weight, and the amber glass center holds its steady warm light on the ivory corner guards and the underside of her chin while her visor stays clear and her eyes stay visible. 7-10 s: The push-in carries on slowly as her chest settles under the weight, the core resting in her two gloved hands and her chest harness empty. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme, C26 yedeği): kare sonucu gösterir, çekirdek beşiğin birkaç cm üstünde, iki eldiven kulpta ve kasa kenarında; video yalnız kamera itişi + sabit amber. Değişen cümle (0-3.5 s vuruşu): "0-3.5 s: The camera begins a slow, shallow push-in from the first moment as she draws her shoulders under the weight of the core held a few centimeters above the cradle, both gloves keeping the same grips."

---

### V3b — Tuzak onları fark etti

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/1.LEON_v1.png · ref/10.CEKIRDEK_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V3b.png
DİLİM     kurguda klipten 0,0-5,0 s
```

> Not: Kaynak C27 + C28, tek kişi. ÖLÜMCÜL siren riski (TD T02): lamba sabit, tek renk, yerinde kabarıp söner; ışık yerleri hep aynı (sweeping/washing/travelling kelimeleri çıktı). Kırmızı yalnız kask tepesinde ve duvarda, yüz ve vizör amber lambalarla. Karede "lamba düşük sabit parıltıda". Sandık çıktı (panel adı kalır: kapı + lamba içinde).
> Bakış lambadan göz hizasına iner ve kasa boyunca kadraj soluna gider (kadın kadrajda değil). Vuruşlar 0-2 · 2-4,5 · 4,5-10; kurgu 5 s'de keser.

#### Görsel
```text
Reference 1 (man): take his face, the pale left-temple scar, the clear ivory helmet and the ivory pressure suit from it, using the face close-up panel. Reference 10 (core and vault): take the graphite vault wall, the heavy graphite door leaf swung open against the wall and the round red emergency lamp above the doorway from it, using the vault door and crate panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Medium vertical shot on a 50 mm lens at chest height inside the vault, from his helmet down to his chest. No part of the figure falls into the bottom quarter of the frame. He stands at frame-centre beside the open doorway in the vault's left wall, in three-quarter view with his face angled toward frame-left, his helmet in the middle band of the frame: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His orange bands circle both upper arms, his badge sits on his left chest, and his clear visor shows his eyes and beard plainly while his gaze is directed up and to the left at the lamp. The round red emergency lamp on the wall above the doorway sits in the upper band of the frame. The lamp is lit at a low steady glow, its dull red light resting only on the crown of his helmet and the graphite wall beside it, his face and visor lit by the low amber lamps. The heavy graphite door leaf stands swung open against the wall. The bottom quarter of the frame shows only the plain grated floor, and all surfaces are plain and unmarked. The light is low amber lamps on graphite walls and one dull red emergency lamp pulsing above the open doorway. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-2 s: The camera begins a slow push-in from the first moment, and at about 0.5 s the round red emergency lamp above the doorway starts to pulse: the lamp itself stays fixed in place and its single dull red glow swells and fades on the spot, lighting the doorway frame and the wall beside it evenly each time, the light always landing on the same places, while his eyes rest on the lamp. 2-4.5 s: His gaze drops from the lamp to eye level and travels across the vault toward frame-left as his helmet turns a few degrees the same way, the lamp pulsing steadily in its place. 4.5-10 s: The push-in carries on slowly as the lamp keeps pulsing on the spot and his eyes stay directed toward frame-left. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): baş sabit, yalnız bakış kayar. Değişen cümle (ikinci vuruş): "2-4.5 s: His gaze drops from the lamp to eye level and his eyes move across the vault toward frame-left while his helmet stays almost still."

---

### V4a — Adam kapıya bakıyor

```
FLOW      Frames to Video
EKLE      KARE (Görsel): ref/1.LEON_v1.png · ref/12.KONTROL_ODASI_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V4a.png
DİLİM     kurguda klipten 0,0-4,0 s
```

> Not: Kaynak C20 + C19, dikeye çevrildi; adam tek başına, sağ profil (yara ve rozet uzak tarafta). Derin odak: yüz ve camın ardı eşit keskin; halka tam üç eşit rijit kepenk (üç koyu bıçak, üç ince açık dikiş), koyu grafit, dış kenarında ince soğuk mavi rim, açıklığı siyah uzay; yüzdeki mavi ışık camın ardındaki gaz devinden. Halka camın SOL yarısında (sağ şerit boş), kepenkler yaklaşık yarı kapalı (V4b'nin ilk durumu). Konsol ve kollar çıktı. Karede bakış camın alt kısmında.
> Bakış ~3,5 s'de yükselir, 4'te hâlâ yükseliyor (kurgu keser). Vuruşlar 0-4 · 4-7 · 7-10. D24 (göz hattı sağ-yukarı ↔ V4b halka solda) bilinçli kabul, loop önceliği. 10.CEKIRDEK eklenmez.

#### Görsel
```text
Reference 1 (man): take his face, the clear ivory helmet and the ivory pressure suit from it, using the right-profile close-up panel. Reference 12 (control room): take the rear reinforced window frame and the exit iris seen through it as a ring of three rigid radial shutters from it, using the wide room panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Medium vertical shot on a 50 mm lens at eye level inside the gate-control room, from his helmet down to his chest, the camera beside him. No part of the figure falls into the bottom quarter of the frame. He stands at frame-centre-left in right profile facing the rear reinforced window that fills the right side of the frame, his helmet in the upper-middle band, his pale left-temple scar turned away from the camera: an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. His orange bands circle both upper arms, and his badge sits on his left chest, out of sight on the far side. His clear visor shows his eyes and beard plainly, a thin soft blue reflection along its outer edge, his gaze directed at the lower part of the window glass, and the cool blue light on his cheek comes from the gas giant beyond the glass. Beyond the clear, transparent window glass, in deep focus with his face and the window beyond equally sharp, the colossal circular exit gate hangs in the upper part of the glass, toward the glass's left half, above and ahead of his face: a dark graphite ring made of exactly three equal rigid radial shutters, three clear dark blades with three thin pale seams between them, about half closed around a circular opening that shows black space, with a faint cool blue rim-light on its outer edge. The bottom quarter of the frame shows only the plain floor, and all surfaces are plain and unmarked. Everything hangs in deep black space with sparse stars, and a huge curved blue gas giant fills the far background. The light is amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-4 s: The camera begins a slow push-in toward his profile from the first moment, and at about 0.5 s his gaze lifts slowly from the lower glass toward the ring of the exit gate high in the window over about three seconds, his helmet tilting up a few degrees with it, his gaze still rising at 3.5 s. 4-7 s: His gaze settles on the ring and its three shutters beyond the glass, his eyes visible through the clear visor while the cool blue light rests on his cheek. 7-10 s: The push-in carries on toward his profile and his gaze stays lifted to the ring, the ring and the stars beyond the glass holding their places. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme): baş sabit, yalnız gözler yukarı kayar. Değişen cümle (ilk vuruş): "0-4 s: The camera begins a slow push-in toward his profile from the first moment, and at about 0.5 s his eyes lift slowly toward the ring of the exit gate high in the window while his helmet stays almost still."

---

### V4b — Kapı daralıyor, cevap yok

```
FLOW      Frames to Video
EKLE      KARE (Görsel, düzenleme): fragman_dikey/kare/V1a.png (onaylı) · ref/5.FOUNDRY_v1.png (yükleme sırası) · tuval 1152×2048 · VİDEO: yalnız fragman_dikey/kare/V4b.png
DİLİM     kurguda klipten 0,0-6,0 s
```

> Not: V4b V1a'dan düzenleme (TD loop önerisi): onaylı V1a karesi aynı kamera, aynı kıç, gövde, kaburgalar, tug, halkanın yeri ve çapı, gezegen; ark burnu YOK. Değişen tek şey kepenkler: yaklaşık yarı kapalı (V1a üçte bir, V4a yarı → V4b yarı ve kayarken daralır; açık kapı görünmez). V1a onaylanmadan üretilmez.
> Video: kamera kilitli (TD V4b ÖLÜMCÜL: büyüyen halka + daralan açıklık "açılıyor" okunmasın); üç eşit rijit kepenk düz raylarında merkeze doğrusal kayar, dış halka sabit, fırın kabarması yok. Vuruşlar 0-3 · 3-6,5 · 6,5-10; kayış klip boyunca sürer.

#### Görsel
```text
The first image is the base frame: keep its camera angle, the heavy black blast ribs, the ark's stern and long ivory hull, the 1 small salvage tug, the position and diameter of the exit gate, and the planet exactly as they are; the only change is that the three shutters of the exit gate now cover about half of the circular opening. Reference 5 (foundry): take the huge circular exit gate with its three rigid radial sliding shutters from it, using the wide exterior panel. A single full-bleed vertical photograph of one scene; the references supply only identity and design. Low-angle vertical view on a 35 mm lens from just below the foundry's blast ribs, the camera looking steeply up and forward in strong perspective. Across the lower band of the frame, weighted toward the lower left, the heavy black blast ribs stand rigid in straight rows, the orange furnace trench glowing behind them. In the middle band, slightly right of centre, the ark's stern hangs rigid with its two dark blue rear engine housings, and its long ivory segmented hull recedes upward toward the distance, the small salvage tug docked on the right-hand side of the stern. In the upper third of the frame, clear of the very top edge and slightly left of centre, the colossal circular exit gate, a dark graphite structure with a fixed outer ring, stands with its three equal rigid radial sliding shutters about half closed around a circular opening that shows black space; the blue gas giant lies far behind it as a soft curved glow at the lower right of the background. The bottom quarter of the frame holds only the dark bases of the ribs, and all surfaces are plain and unmarked. The frame holds only the ribs, the ark, the tug, the exit gate and the planet. Everything hangs in deep black space with sparse stars, and a huge curved blue gas giant fills the far background. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. In this vertical view the furnace glow lies in the lower-left of the frame behind the ribs and edge-lights the hull from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

#### Video
```text
0-3 s: The camera stays locked on the low angle from the first moment, and at about 0.5 s the three equal rigid shutters of the circular exit gate each slide in a straight line toward the centre along their straight radial tracks, three blades only, the outer ring fixed, each blade covering more of the circular opening with every second. 3-6.5 s: The shutters keep sliding steadily toward the centre and the circular opening narrows further, the stars seen through the opening disappearing one by one behind the advancing blades, while every blade keeps its shape and the outer ring stays fixed; the ark and the ribs stay rigid. 6.5-10 s: The shutters slide on toward each other and the opening grows narrower still while the ark, the tug and the ribs stay rigid. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

> YEDEK (ikinci deneme, Fable: kamera süzülmesi "açılıyor" okunur — TD tur 2 V4b ÖLÜMCÜL): kamera yine kilitli; kapanma yönü yıldızlarla ve daha yavaş kayışla işaretlenir. Değişen cümle (ilk vuruş): "0-3 s: The camera stays locked on the low angle from the first moment, and at about 0.5 s the three equal rigid shutters of the circular exit gate each begin to slide slowly in a straight line toward the centre, the stars seen through the opening disappearing one by one behind the advancing blades, the outer ring fixed."

---

### ÜRETİM İŞ EMRİ

> Her çekim: önce kare (GPT Image, 1152×2048, ref sayfaları yükleme sırasıyla), sonra Gemini Omni 1.1 Flash ile Frames to Video (yalnız kare, 10 s). V1a karesinden sonra DUR: Fable + devamlilik V1a'yı (ateş · gemi · halka ayrı öbekler, 120 px testi) onaylamadan kalan üretim harcanmaz. Referans sayfaları onaylı olmadan kare üretilmez (FILM F7a).

| Sıra | Çekim | İş | Dosya | Eklenecek referanslar | Not |
|:--:|:--:|---|---|---|---|
| 1 | V1a | Görsel | `fragman_dikey/kare/V1a.png` | ref/5.FOUNDRY_v1.png (wide exterior panel) · ref/6.ARK_v1.png (stern panel) | AFİŞ; sonra DUR, onay. V4b'nin tabanı |
| 2 | V1a | Frames to Video | `fragman_dikey/ham/V1a_d1.mp4` | yalnız kare/V1a.png | dilim 0,0-4,0 |
| 3 | V4b | Görsel (düzenleme) | `fragman_dikey/kare/V4b.png` | fragman_dikey/kare/V1a.png (ONAYLI) · ref/5.FOUNDRY_v1.png (wide exterior panel) | V1a onayından sonra; kamera/halka/gezegen V1a ile aynı |
| 4 | V4b | Frames to Video | `fragman_dikey/ham/V4b_d1.mp4` | yalnız kare/V4b.png | dilim 0,0-6,0; kamera kilitli |
| 5 | V3a | Görsel | `fragman_dikey/kare/V3a.png` | ref/2.RHEA_v1.png (front full-length panel) · ref/10.CEKIRDEK_v1.png (core object panel) | en riskli kişi çekimi; kavrayış kare kapısı |
| 6 | V3a | Frames to Video | `fragman_dikey/ham/V3a_d1.mp4` | yalnız kare/V3a.png | dilim 0,0-5,0 |
| 7 | V3b | Görsel | `fragman_dikey/kare/V3b.png` | ref/1.LEON_v1.png (face close-up panel) · ref/10.CEKIRDEK_v1.png (vault door and crate panel) | lamba kapı üstünde, üst bant; sandık kadrajda yok |
| 8 | V3b | Frames to Video | `fragman_dikey/ham/V3b_d1.mp4` | yalnız kare/V3b.png | dilim 0,0-5,0; lamba sabit konumda |
| 9 | V2b | Görsel | `fragman_dikey/kare/V2b.png` | ref/2.RHEA_v1.png (left-profile close-up panel) · ref/7.KORIDOR_v1.png (cryo window panel) | yara yönü: sağ çene kameradan uzak |
| 10 | V2b | Frames to Video | `fragman_dikey/ham/V2b_d1.mp4` | yalnız kare/V2b.png | dilim 0,0-6,0 |
| 11 | V4a | Görsel | `fragman_dikey/kare/V4a.png` | ref/1.LEON_v1.png (right-profile close-up panel) · ref/12.KONTROL_ODASI_v1.png (wide room panel) | halka camda üç kepenkle okunur olmalı; 10.CEKIRDEK eklenmez |
| 12 | V4a | Frames to Video | `fragman_dikey/ham/V4a_d1.mp4` | yalnız kare/V4a.png | dilim 0,0-4,0 |
| 13 | V2a | Görsel | `fragman_dikey/kare/V2a.png` | ref/5.FOUNDRY_v1.png (wide exterior panel) · ref/6.ARK_v1.png (side view panel) | KELEPÇE dişi; çene iki yarım + dikiş; `clamps open panel` kullanılmaz |
| 14 | V2a | Frames to Video | `fragman_dikey/ham/V2a_d1.mp4` | yalnız kare/V2a.png | dilim 0,0-4,0; kamera kilitli, ışık tepesi 2-4 s |
| 15 | V1b | Görsel | `fragman_dikey/kare/V1b.png` | ref/8.KRIYO_v1.png (aisle panel) | en güvenli çekim |
| 16 | V1b | Frames to Video | `fragman_dikey/ham/V1b_d1.mp4` | yalnız kare/V1b.png | dilim 0,0-6,0 |

Her kare ve video en çok 2 deneme (yedekler çekim bölümlerinde): 8 kare + 8 video × 2 = en çok 32 üretim.
