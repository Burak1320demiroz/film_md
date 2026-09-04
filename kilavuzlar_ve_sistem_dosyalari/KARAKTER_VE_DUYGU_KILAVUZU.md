# 🧍‍♂️ KARAKTER VE DUYGU KILAVUZU — Kask Altında Bağ Kurma Mimarisi

> **Neden var (22.08.2026):** Hikaye tablosunun **Karakter** ve **Duygu Yayı**
> sütunları neredeyse her filmde 3-4 bandında. Buna rağmen kamera, fizik,
> hook, vuruş ve fragman için ayrı kılavuz varken izleyicinin karaktere
> BAĞLANMASI için tek satır yoktu. `SAHNE_DEVAMLILIK_KILAVUZU.md` karakteri
> TEKNİK olarak sabitler (aynı yüz, aynı seed); bu dosya o sabit figürün
> izleyiciyi neden umursatacağını sayıya çevirir.
>
> **Ne zaman okunur:** vuruş tablosundan sonra, SAHNE HARİTASI yazılırken.
> Buradaki bütçeler sahne haritasının satırlarına dağıtılır — üretimden
> sonra eklenemez.
> Kaynak: `araştırmalar/2.md` (22.08.2026 nörosinema araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① SAYILAR DIŞ ARAŞTIRMADAN GELİR, bu serinin ölçülmüş sonucu değildir.
   Test ölçütü nettir: Karakter ve Duygu Yayı sütunlarındaki 3-4 platosu.
   Bu kılavuza göre yazılmış filmlerde plato kırılmıyorsa kılavuz
   çalışmıyordur ve revize edilir — HOOK kılavuzunun §0③ ile aynı sözleşme.
   Gerçek izleyici tarafı: YAYIN_VE_PERFORMANS_KILAVUZU.md §6.

② KASK AÇILMAZ. Bu kılavuzun hiçbir maddesi ekipman kilidini gevşetmez
   [D37 · D57]: vizör açılmaz, kapanmaz, tonlanmaz, kaybolmaz. Yüz
   görünürlüğü vizörü AÇARAK değil, vizörün İÇİNİ AYDINLATARAK sağlanır.
   Bu ayrım kılavuzun en kritik cümlesidir — karıştırılırsa ekipman
   durumu bozulur ve teknik skor düşer.

③ BU KILAVUZ SAHNE SAYISI HARCAR. Bütçeler bedava değildir: tepki
   planına ayrılan her sahne, olay örgüsünden alınmış bir sahnedir.
   Vuruş haritası (SENARYO_VE_VIRAL_KAMERA §2) ile ÇAKIŞIRSA vuruş
   haritası kazanır — boş vuruş, dolu tepki planından pahalıdır.

④ ÖLÇÜLMÜŞ RİSK: gözyaşı, mikro ifade ve ıslak göz istemleri bu hatta
   AI bloom ve doku kaybı riskini artırır [D3 · D41]. Bütçe § 1'de
   gözyaşı ZORUNLU DEĞİLDİR; göz + bakış yönü zorunludur.
```

---

# 1. 👁️ GÖZ BÜTÇESİ — yüz kapalıyken bakılacak tek yer

**Mekanizma:** Yüz örtüldüğünde duygu tanıma doğruluğu %21-31 düşer ve
izleyici otomatik olarak GÖZ MERKEZLİ tarama stratejisine geçer. Göz
teması kurulan o kısa anda ayna nöron sistemi tetiklenir; kurulmazsa
kask bir nesnedir, karakter değil.

```
SAYISAL KİLİT
  □ GÖZ GÖRÜNÜRLÜĞÜ  ≥ toplam sürenin %12'si (hedef %15)
  □ TEK GÖZ PLANI    ≥ 1,5 s kesintisiz — daha kısası kaydolmaz
  □ YERLEŞİM         en yüksek duygusal kırılma yuvalarına:
                     orta nokta (midpoint) ve "her şey kayboldu" anı
```

**Prompta girecek blok** (vizör kilidini bozmadan göz açan tek yol):

```
VISOR INTERIOR LIGHT: The visor stays sealed, in place and unchanged for
the whole take — it never opens, closes, tints, clears or disappears.
Interior fill comes from the suit's own chest console at 15 cm below the
chin, throwing a low warm key onto the face INSIDE the sealed visor. Both
eyes, brow and upper cheek read clearly through the glass for the full
shot. The glass keeps a faint surface reflection and visible scratches;
it never becomes invisible. No lens flare, no glow bloom, no clean glass.
```

```
BAKIŞ YÖNÜ — duyguyu taşıyan tek ücretsiz değişken
  kaçınma duyguları (korku · hüzün · teslim)  → bakış KAÇIRILMIŞ
      "eyes cast down and to the left, never meeting the lens"
  yaklaşma duyguları (kararlılık · öfke · direnç) → bakış KİLİTLİ
      "eyes locked forward on the threat, unblinking for 2 seconds"
  ⚠️ Bakış yönü sahne haritasına YAZILIR. Yazılmayan bakış, ışığa döner
     [D104: en parlak ışık yön mıknatısıdır].
```

---

# 2. 🔁 KULESHOV DÖNGÜSÜ — lockoff'ta duygu buradan gelir

**Mekanizma:** Nötr yüze, komşu planın duygusal değeri atfedilir. Donuk
bir kask, sinemanın en güçlü "nötr yüzü"dür. A (karakter) → B (baktığı
şey) → A (tepki) dizisi izleyicinin beyninde duyguyu ZORUNLU olarak
üretir; kamera hiç hareket etmeden.

> ⭐ Bu depo için bedava avantaj: A-B-A üç AYRI SAHNEDİR, sahne içi kesme
> değildir. Tek çekim kuralı [D1] bozulmaz, ızgara bozulmaz — üç klip.

```
SAYISAL KİLİT
  □ DÖNGÜ SIKLIĞI   her 30 saniyede ≥ 1 tam A-B-A döngüsü
  □ TEPKİ PAYI      tüm kurgunun ≥ %25'i tepki/bakış planı
  □ DÖNÜŞ PLANI     B'den sonraki A ≥ 2 s (hedef 2-3 s)
                    daha hızlısı bağlamı bağlamadan keser
  □ B PLANI         karakterin baktığı şeyi TAM gösterir; yarım
                    gösterilen B, döngüyü çalıştırmaz
```

```
DÖNGÜ ŞABLONU — sahne haritasına üç satır olarak yazılır
  S(n)   A · karakter, sabit kadraj, bakış yönü YAZILI
  S(n+1) B · karakterin baktığı nesne/olay — POV değil, aynı uzamsal
           mantıkta ayrı kadraj (ekran yönü: UZAMSAL_HARITA kuralları)
  S(n+2) A' · aynı kurulum, DEĞİŞMİŞ tek bir şey (omuz düşer, el
           gevşer, baş eğilir) — değişen şey plana YAZILIR
```

> ⚠️ A' planında "aynı kadraj" demek, aynı kamerayı ve aynı ışığı yeniden
> yazmak demektir; prompt self-contained olduğu için kurulum blok olarak
> TEKRAR yazılır. Yeniden yazılmayan kurulum kayar.

---

# 3. ⏱️ İSİM · İSTEK · BEDEL — ilk %10'da kapanan sözleşme

**Mekanizma:** Empatinin başlaması için izleyicinin üç şeyi bilmesi
yeter: bu kim (rol), ne istiyor, başaramazsa ne kaybediyor. Üçü de
kapanmadan geçen her saniye, seyircinin "hedefi olan canlı" arketipiyle
sözleşme imzalamasını geciktirir.

```
SAYISAL KİLİT
  □ ÜÇÜ DE ilk %10'da kapanır — ekran metni YOK, diyalog ZORUNLU DEĞİL
  □ İSİM  = ROL demektir, ad değil. Ne olduğu kostüm/ekipmanla okunur
            (madenci mi, kurtarma ekibi mi, kaçak mı)
  □ İSTEK = kadrajda GÖRÜNEN bir hedef (kapı, araç, ışık, yön)
  □ BEDEL = kadrajda GÖRÜNEN bir sayaç (oksijen göstergesi, çatlak,
            düşen seviye, uzaklaşan araç)
  □ ORTA NOKTA %50'de: sahte zafer VEYA sahte yenilgi
```

**Format karşılıkları** (ızgaradan hesaplanır, elle yazılmaz):

| Format | Toplam | İsim-istek-bedel kapanışı | Orta nokta |
|---|:--:|:--:|:--:|
| **dikey shorts** | 6 × 8 s = 48 s | ≤ 4,8 s → **hook klibinin içinde** | 24 s → S3/S4 sınırı |
| **yatay 2-4 dk** | 12-18 × 10 s | ≤ 15 s → **S1 bitmeden** (HOOK §katalizör kapısıyla aynı) | S7-S9 |
| **yatay 3-5 dk** | 25 × 10 s (hook 9 s) | ≤ 25 s → **S3 bitmeden** | S13 |
| **yatay 7-9 dk** | 60 × 8 s | ≤ 48 s → **S6 bitmeden** | S30 |

> ⚠️ Bu tablo bir HESAP çıktısıdır. Format kartındaki sahne sayısı
> değişirse tablo yeniden hesaplanır — `KILAVUZ_REHBERI.md` §2 tek kaynaktır.

---

# 4. 🫀 VEKİL KANALLAR — yüz yokken bedene devredilen bütçe

Kamera hareket etmiyorsa ve yüz kapalıysa, kinestetik empatinin tamamı
kadraj İÇİNDEKİ bedene devredilir. Dördü de ayrı bütçedir ve dördü de
sahne haritasında yer kaplar.

## 4.1 ELLER — yüzden sonraki en güçlü kanal (≥ %15)

Nesneyi kavrayan, titreyen, tereddüt eden el; izleyicinin kendi motor
korteksini ateşler. Kask duyguyu iletemediğinde sıkılan yumruk iletir.

```
□ BÜTÇE: toplam sürenin ≥ %15'i el / mikro-jest / haptik temas kadrajı
□ Bu kadraj AYRI SAHNEDİR (insert), sahne içi kesme değil
□ Elin YAPTIĞI iş plana yazılır: neyi tutuyor, ne kadar sıkıyor, titriyor mu
```

```
HAND INSERT: Locked-off close shot on the gloved hands only, no face in
frame. The fingers tighten on the rail until the glove fabric creases,
hold for 2 seconds, then release one finger at a time. Scratches, dust
staining and wear on the gloves are identical to every other scene.
```

## 4.2 NEFES — otonom sinir sistemine doğrudan hat (≥ %20)

Kask, izole eden bir bariyer değil, karakterin iç ritmini dışarı taşıyan
bir yankı odasıdır. İzleyici duyduğu nefes ritmiyle bilinçdışı senkronize
olur: hızlanan nefes kalp ritmini yükseltir, yavaşlayan nefes rahatlatır.

```
□ BÜTÇE: gerilim/çaresizlik/sessizlik bloklarının ≥ %20'sinde kask içi
         nefes NET ve YALITILMIŞ bir katman olarak duyulur
□ KATARZİS KİLİDİ: final rahatlamasında tempo dakikada 6 nefese iner
         → 10 saniyede 1 nefes = TAM BİR KLİPTE TEK NEFES
□ REGISTER: nefes HUMAN'dır, MACHINE değil — ses defterine öyle yazılır
         (SES_VE_DIYALOG_URETIM_KILAVUZU register haritası; yanlış
         işaretlenen nefes SES_QA'da "sentetik" bulgusu üretir)
□ ⚠️ VAKUM İSTİSNASI DEĞİLDİR: dışarıda ses yoktur, kask İÇİ nefes
         diegetiktir ve duyulur. İkisi aynı sahnede çelişmez.
```

## 4.3 YÜRÜYÜŞ / DURUŞ — %84 doğrulukla okunan beden dili (≥ %10)

İzleyici, yalnız eklem hızına ve postüre bakarak duyguyu %84 doğrulukla
okur. Lockoff kadrajda karakterin kadraj içinde yürümesi, kameranın
yapamadığı hareketi yapar.

```
□ BÜTÇE: toplam sürenin ≥ %10'u TAM BOY (wide) yürüyüş/duruş kadrajı
□ Plana yazılan üç değişken:
     ADIM TEMPOSU   umutsuzluk = düzensiz ve ağır · kararlılık = düzenli
     GÖVDE AÇISI    omuz düşük / ağırlık merkezi önde
     BAŞ YÖNÜ       kask yere mi, hedefe mi bakıyor [D104 ile aynı kural]
□ Z ekseni tercih edilir (kadraj derinliğine yürüme): lockoff'ta ölçek
  değişimini bedava üretir
```

## 4.4 KİŞİSEL EŞYA — otobiyografik hafıza protezi (≥ %5)

Yıpranmış bir nesne, yüzün anlatabileceğinden fazlasını anlatır: çizikli
kask, eldivendeki kurumuş iz, bırakılmayan analog bir alet.

```
□ BÜTÇE: 1-2 spesifik nesne, toplam sürenin ≥ %5'inde KESKİN ODAKTA
□ Nesne TEK SAHNE İÇİN İCAT EDİLMEZ [D58 tekrar eden varlık kilidi]:
  birden fazla sahnede görünür ve her sahnede aynı sayısal kimlik
  kartıyla yazılır (renk, boyut, doku, hasarın YERİ)
□ Yıpranma sabittir, göç etmez [D42]
□ ⭐ Eşyanın KENDİSİ (ne olduğu, giysinin neresinde, fizik kuralları,
  İngilizce kalıbı, hangi vuruşu taşıdığı):
  ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md §8 (03.09.2026) —
  burası BÜTÇEYİ verir, orası ENVANTERİ
```

---

# 5. 💥 PAYLAŞILAN DUYGU — huşu, merak, hüzün-umut

Paylaşım kararı bilgiyle değil duyguyla verilir. Ölçülen üç tetikleyici,
bu serinin kısıtlarıyla ÇATIŞMAZ; üçü de lockoff'un doğal ürünüdür.

## 5.1 HUŞU = ölçek kontrastı

```
□ FİNAL İMAJ veya DORUK yuvasında karakter ile çevre arasında
  ≥ 1:10 görsel ölçek zıtlığı (karakter kadraj yüksekliğinin ≤ %10'u)
□ Bu plan ≥ 10 s ekranda kalır → TAM BİR KLİP, kırpılmaz
□ Statik + devasa + yalnız figür: lockoff bu etkiyi bozmaz, ÜRETİR
⚠️ Ölçek KONTRASTI, ölçek KİLİDİNİ bozmaz: nesnenin metre cinsinden
   kimliği sabit kalır (UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU ölçek kilidi).
   Değişen kadrajdır, nesnenin boyu değil.
```

## 5.2 MERAK = açıklanmayanın bütçesi

```
□ Filmin kurallarının TAMAMI açıklanmaz — izleyici desen arar, ekranı tarar
□ Diyalog, iç ses ve ekran metni yokluğu bu seride zaten var: bu bir
  eksiklik değil, merak motorunun yakıtıdır
□ En az 1 görsel anomali kurulur ve AÇIKLANMADAN bırakılır
⚠️ SINIR: açıklanmayan şey, PLANIN kendi kilidiyle çelişmez. Cevabı
   planda yazılı olan bir soru "gizem" değil, önerme ihlalidir
   (AGENTS ortak adım ⑩ · önerme kapısı).
⚠️ Merakın KAYNAĞI bu kılavuzun işi değil: novum seçimi ve kural
   kanıtlama → ONERME_VE_NOVUM_KILAVUZU.md. Bu bölüm yalnız novumun
   NE KADARININ açıklanmayacağını bütçeler.
```

## 5.3 HÜZÜN-UMUT = katarzisin ses mimarisi

```
□ "HER ŞEY KAYBOLDU" yuvasında müzik TAMAMEN kesilir — geriye yalnız
  yalıtılmış kask içi nefes kalır
  ⚠️ Bu SESSİZLİK DEĞİLDİR: mutlak dijital sıfır bir hatadır [D83].
     Ortam yatağı ve nefes akmaya devam eder, müzik susar.
□ FİNAL karar anında tek bir kreşendo ile işitsel ödül verilir
□ Müziksiz sahne zaten her filmde zorunlu (MUSIC §10) — bu kılavuz
  o sahnenin YERİNİ belirler: "her şey kayboldu" yuvası
```

---

# 6. 📋 SAHNE BÜTÇE TABLOSU — plana kopyalanır

> Yüzdeler ızgaraya çevrilmiş hâlleriyle. Bir sahne birden çok bütçeyi
> aynı anda taşıyabilir (el insertinde prop da olabilir); tablo TABAN
> gösterir, toplamı sahne sayısını aşmaz.

| Bütçe | shorts (6×8 s) | 2-4 dk (~15×10 s) | 3-5 dk (25×10 s) | 7-9 dk (60×8 s) |
|---|:--:|:--:|:--:|:--:|
| 👁️ göz görünürlüğü ≥%12 | ~1 sahne | ~2 sahne | 3-4 sahne | 7-9 sahne |
| 🔁 tepki planı ≥%25 | ~2 sahne | ~4 sahne | ~6 sahne | ~15 sahne |
| ✋ el / mikro-jest ≥%15 | ~1 sahne | ~2 sahne | ~4 sahne | ~9 sahne |
| 🚶 tam boy yürüyüş ≥%10 | ~1 sahne | ~2 sahne | ~3 sahne | ~6 sahne |
| 🎒 kişisel eşya ≥%5 | (insert içinde) | ~1 sahne | ~1 sahne | ~3 sahne |
| 🌌 ölçek kontrastı 1:10 | 1 sahne (final) | 1 sahne | 1 sahne | 1-2 sahne |
| 🔁 Kuleshov döngüsü | ≥1 döngü | her 30 s'de 1 → ≥5 | ≥8 | ≥16 |

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Kaskın şeffaflaşması / vizörün açılıp yüzün gösterilmesi | Ekipman durum kilidi [D37 · D57]: vizör açılmaz, tonlanmaz, kaybolmaz. Karşılığı §1'deki vizör İÇİ aydınlatmadır. |
| Gözyaşı ve ıslak mikro ifade zorunluluğu | Bu hatta AI bloom ve doku kaybı riskini artırır [D3 · D41]. Bütçeye ZORUNLU olarak girmedi; göz + bakış yönü zorunlu, gözyaşı opsiyonel. |
| "Güçlü diyalogla desteklenen açılış" | Replik bütçesi ve register haritası ayrı kısıt (SES_VE_DIYALOG_URETIM). İsim-istek-bedel bu seride GÖRSEL kodlanır (§3). |
| Doğrudan kameraya bakış (direct gaze to lens) | Kararlılık için TEHDİDE bakış kullanılır; merceğe bakmak dördüncü duvarı kırar ve bu serinin gözlemci kamera dilini bozar. |
| "Kuleshov için POV planı" | POV, kameranın karakterin gözüne geçmesidir; lockoff gözlemci dilini bozar. B planı POV DEĞİL, aynı uzamsal mantıkta ayrı kadrajdır (§2). |

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 8 maddesi

```
□ 1. Karakterin ROLÜ kostüm/ekipmanla ilk %10'da okunuyor mu
□ 2. İSTEK kadrajda görünen bir hedef mi (metin değil)
□ 3. BEDEL kadrajda görünen bir sayaç mı
□ 4. Göz bütçesi (%12) sahne haritasında yuvalara DAĞITILDI mı,
     ve o sahnelerde vizör içi aydınlatma satırı YAZILI mı
□ 5. Her 30 saniyede en az bir A-B-A döngüsü var mı; dönüş planı ≥2 s mi
□ 6. El · yürüyüş · eşya bütçeleri sahne haritasında yer buldu mu (§6)
□ 7. "Her şey kayboldu" yuvası belirlendi mi — müziğin sustuğu, nefesin
     kaldığı sahne bu mu
□ 8. Final/doruk yuvasında 1:10 ölçek kontrastı ve ≥10 s'lik tam klip var mı
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/2.md                      bu kılavuzun kaynak araştırması (22.08.2026)
SAHNE_DEVAMLILIK_KILAVUZU.md           karakterin TEKNİK sabitlenmesi (çapa, seed)
HOOK_VE_ILK_SAHNE_KILAVUZU.md          ilk iki sahne · katalizör kapısı (§3 ile aynı saat)
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md    §2 vuruş haritası — çakışırsa o kazanır
UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md  B planının ekran yönü · ölçek kilidi
SES_VE_DIYALOG_URETIM_KILAVUZU.md      nefes register'ı · replik bütçesi
GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md   §10 müziksiz sahne · katarzis kreşendosu
KURGU_RITMI_VE_IHRAC_KILAVUZU.md       tepki planlarının kurgudaki süresi
DERSLER/02_KARAKTER_VE_CANLI.md        karakter dersleri tam metin
DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md  D37 · D57 · D58 ekipman ve varlık kilitleri
```
