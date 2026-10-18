# 🎞️ THE_FURNACE_GATE — DİKEY FRAGMAN · 0:40 · 9:16

> Kural kaynağı: `kilavuzlar_ve_sistem_dosyalari/FRAGMAN_KILAVUZU.md` — **§2 SHORTS FRAGMAN KARTI** + §1 değişmezleri.
> Kaynak film 16:9, fragman 9:16 → §1.1: **kırpma yok, her çekim dikey oranda SIFIRDAN üretilir.**
> Fragman yeni bir film değildir: kendi konsepti, novum'u, hikâyesi yoktur. Tek işi filmin vaadini kurmak ve **cevabı vermeden bırakmaktır.**
> Üretim yolu filmle aynı (FILM.md künye): GPT Image (kare) → Gemini Omni 1.1 Flash (10 s video). Referanslar filmin referanslarıdır (FILM §3), ayrı referans üretilmez.
> Dosya klasör içi → film sayımına girmez (FRAGMAN §0). `PROMPTLAR/` dışında durur: `film_dogrula.py` ve `medya.py` o klasördeki her dosyayı film çekimi sayar.

```
BİÇİM     9:16 dikey · 0:40 · 4 sahne × 10 s · 7 çekim · 6 kesme (sahne içi 3 + sahne arası 3) · ekran metni 0.0 s · replik 0
SAHİP     "THE_FURNACE_GATE şu filmi birde 40 saniyelik dikey fragman hazırlayalım 4 sahne yani her sahneye max 1 cut koyabilirsin" (17.10.2026)
YORUM     sahne = 10 s'lik yuva; içinde en çok 1 kesme → sahne 1 ya da 2 çekim. Her çekim 10 s üretilir (sahip kuralı 08.10.2026),
          kurguda ZAMAN dilimi alınır; kadraj kırpılmaz, klibin içine kesme atılmaz (FRAGMAN §1.1b mantığı · §1.5).
MEKANİK   ⭐ İKİ IŞIK (§3)
SORU      "Turuncu mu söner, yeşil mi?" — çalınan çekirdek mi, uyuyan gemi mi?
ÜRETİM    7 kare + 7 video × en çok 2 deneme = en çok 21 üretim · yeni referans 0 (FILM §3: 1 · 2 · 5 · 6 · 7 · 8 · 10)
MEDYA     ~/film_medya/THE_FURNACE_GATE/fragman_dikey/{kare,ham,ses,cikti}/ (repoya girmez)
DURUM     KART v1 (Fable, 17.10.2026) → eleştiri turu → promptlar
```

## 1. BİLİNÇLİ SAPMALAR — format DNA'sından her sapma (FRAGMAN §1.7)

| # | Kılavuz | Bu fragman | Gerekçe |
|:--:|---|---|---|
| ① | §0 dikey klip 8 s | 10 s üretim, kurguda 3,5-10 s dilim | sahip kuralı (her çekim 10 s) + sahip isteği 40 s / 4 sahne; toplam 40 s, 24-48 s bandının içinde |
| ② | §2.1 vuruş = klip | 4 vuruş (sahne) · 7 çekim | sahip: sahne içi en çok 1 kesme. Her çekim yine ayrı klip; kesme klip ARALARINDA (§1.5) |
| ③ | §1.3c kaynak lens/kadraj | 7 çekimin hepsi dikey yeniden kadraj | 9:16 sıfırdan üretim zorunlu (§1.1); her satırın "kaynak → yeni" gerekçesi §4 tablosunda |
| ④ | FILM §3 sabit tasarım "kaçış yönü soldan sağa" | V1a'da eksen DİKEY: fırın aşağıda, gemi yukarıda | dikeyin kazancı dikey nesnedir (§1.1); fragmanda kapı ve kaçış görünmez, sol-sağ ilişkisi kurulmaz → filmle çelişki doğmaz |
| ⑤ | FILM §3 ORTAM SESİ (model sesi AÇIK film) | video promptunda ses cümlesi YOK | fragmanda klip sesi kullanılmaz (replik 0); ses kurguda: müzik + FILM §6 yatakları. Omni sesi atılır |
| ⑥ | plan açılış VO "We came to steal a power core. We left with a ship full of people." | kullanılmaz | cümlenin ikinci yarısı SONUÇTUR (spoiler §2); dikeyde replik 0 varsayılan (§1.6) |
| ⑦ | §1.3 mekanik sicili | İKİ IŞIK sicile YAZILMADI | eski kılavuzlar düzenlenmez (CLAUDE.md); kayıt bu dosyada + NOTLAR KARARLAR |
| ⑧ | SHORTS_SISTEM_PROMPTU prompt kalıbı (lens kilidi, "Kamera Mesafesi") | filmin G01 biçimi | çapalar kaynak filmden birebir (§1.4): Reference <No> anahtarı, KİMLİK TABANI, MEKÂN IŞIĞI, DIŞ DÜNYA, ORTAK GÖRÜNÜM; güvenli alan cümlesi eklenir (§5) |

Kaynak filmin ölçüm durumu: üretim 0 (referans 0/15, kare 0/96), QA yok. Fragman filmden ÖNCE yazıldı; kare üretimi filmin referans
onayına (F7a, SHA) bağlıdır — referanslar onaylanmadan fragman karesi üretilmez.

## 2. ⛔ SPOILER KAPISI — fragmanda ASLA olmayacak kareler (kurguda madde madde 0 kare)

Vuruşlar filmin ilk %70'inden (C01-C67). En ileri kaynak **C48 = %50** ✅

```
⛔ çekirdeğin giriş yuvasına konması · kapı gücü · enerji hattı (C58-C61) — ÇÖZÜMÜN MEKANİZMASI
⛔ kapının açılması · açık kapı · mandal · kelepçelerin bırakılması (C62-C72) — çözüm
⛔ çekirdeğin aşırı parlaması / tükenmesi / sönük çekirdek (C69 · C73 · C94) — BEDEL, sorunun cevabı
⛔ kokpit itirafı · sınıflayıcı geçmişi · Dione · tether (C37-C43) — omurga sırrı
⛔ köprünün geri çekilmesi · Rhea'nın karşıda kalması · Leon'un dönüşü · iskele · ikinci yanaşma (C73-C88) — DORUK, karakterin kaderi
⛔ ark'ın kapıdan çıkışı · purge · özgür iki gemi · "dört bin sinyal sabit" (C89-C96) — FİNAL
⛔ "four thousand" ya da herhangi bir sayı · film adı · yazı — ekranda 0, seste 0
⭐ SORU kurulur, cevaplanmaz: iki ışık aynı karede buluşur; hangisinin söneceği gösterilmez.
```

## 3. ⭐ MEKANİK — İKİ IŞIK

```
TURUNCU  yakar ve alınır   — fırın ışığı (dışarıda) · çekirdeğin amber camı (çalınan şey)
YEŞİL    uyur ve yaşar     — kapsüllerin durum noktaları (gemideki uyuyanlar)
KURAL    Her sahne iki ışığı bir adım daha YAKLAŞTIRIR; sahne içi kesme turuncudan yeşile atlar.
         Son sahnede iki ışık TEK KAREDE, aynı vizörde buluşur. Hangisinin söneceği cevapsız.
         ⭐ Filmin cevabı (çekirdek söner, yeşiller sabit kalır: C69 · C93 · C94) fragmanda 0 kare.

  S1  ayrı           turuncu DIŞARIDA (fırın gövdenin altında)  │ yeşil İÇERİDE (kapsül koridoru) — aralarında gövde
  S2  içeri girer    turuncu İÇERİDE (çekirdek kasada)           │ yeşil bir YÜZE değer (kadının vizörü)
  S3  ele geçer      turuncu ELDE (kadın çekirdeği kaldırır)     │ yeşil öteki YÜZDE (adamın vizörü)
  S4  buluşur        turuncu GÖĞÜSTE + yeşil YANINDA — kesmesiz, tek vizörde (AFİŞ + SORU)
```

Mekanik filmi özetlemez: soygunun adımları, drone, kapı, kardeş çatışması anlatılmaz. Her vuruş yalnız iki ışığın arasındaki mesafeyi kapatır.

## 4. VURUŞ / KAYNAK EŞLEME

| Sahne | Saniye | Çekim | Rol | Işık | Kaynak (FILM §4) | Ekranda görünen | Dikey kadraj · kaynak → yeni (§1.3c) | Referans |
|:--:|:--:|:--:|---|:--:|---|---|---|---|
| S1 | 0,0-3,5 | V1a | HOOK | turuncu | C12 · C44 | ağır patlama kaburgalarının arasında turuncu fırın ışığı kabarır; üstte dev fildişi ark'ın kıçı siyah beşikte asılı, alt yüzü turuncuya boyanır | aşağıdan yukarı bakış: kaburgalar ve ışık orta bantta, kıç üst yarıda · C12 yan arka-¾ geniş → alttan dikey; gerekçe: dikey nesne + ışığın gövdeye uzanışı tek eksende | 5.FOUNDRY · 6.ARK |
| S1 | 3,5-10,0 | V1b | — | yeşil | C09 | diz hizasından kapsül koridoru: sıra sıra opak kapaklı kapsül, her birinde soluk yeşil nokta; yavaş ileri takip | kaçış noktası üst-orta bantta, sıralar iki yandan yukarı akar · C09 yatay derin → dikey derin; gerekçe: sonsuz sıra dikeyde boydan okunur | 8.KRIYO |
| S2 | 10,0-15,0 | V2a | KURULUM | turuncu | C25 | karanlık kasada açık beşikte çekirdek, amber cam merkez; kulpun üstündeki geniş mandal dışarı döner ve durur | yakın, çekirdek orta bantta · C25 yakın yatay → yakın dikey; gerekçe: tek nesne, dikeyde kadrajı doldurur | 10.CEKIRDEK |
| S2 | 15,0-20,0 | V2b | — | yeşil | C08 | kadın kriyo camının yanında; camın ardında yeşil noktalı kapsül sıraları; cama hafifçe eğilir, yeşil noktalar şeffaf vizöründe | orta-yakın (göğüs üstü), cam kadrajın bir yanında boydan · C08 orta yatay → orta-yakın dikey; gerekçe: yüz ve yansıma güvenli bantta | 2.RHEA · 7.KORIDOR |
| S3 | 20,0-25,0 | V3a | TIRMANIŞ | turuncu | C26 | kadının iki eldiveni çekirdeği kulpundan ve kasasından tutup beşikten kısa bir mesafe kaldırır; amber ışık vizörünü alttan aydınlatır | orta-yakın, çekirdek göğüs hizasında, yüz üstte · C26 orta yatay → dikey; gerekçe: el-nesne-yüz tek dikey eksende | 2.RHEA · 10.CEKIRDEK |
| S3 | 25,0-30,0 | V3b | — | yeşil | C11 (koridor, yeşil ışık) | adamın yakın planı, şeffaf vizöründe yandaki camdan yeşil ışık; başını kadraj dışında birine doğru yavaşça çevirir | yakın dikey · C11 orta iki kişi → tek kişi yakın; gerekçe: S3'ün iki yüzü (kadın turuncu, adam yeşil) ayrı karelerde | 1.LEON · 7.KORIDOR |
| S4 | 30,0-40,0 | V4 | AFİŞ + SORU | ikisi | C27 · C48 · C08 (fragman kadrajı) | kadın, çekirdek göğüs askısında kilitli, kapsül camının yanında; yüzü alttan amber, yandan yeşil; kamera yavaşça yaklaşır, kadın başını camdan çekirdeğe çevirir, amber ışık bir kez yavaşça güçlenir; yaklaşma sürerken kesilir | orta → yakın, kesmesiz · C48 kavşak geniş + C08 cam → yeni kompozisyon; gerekçe: iki ışığın tek vizörde buluştuğu tek kare (filmde bu kadraj yok; kavşak C48'de çekirdek göğüste, cam koridorun sol duvarında) | 2.RHEA · 7.KORIDOR · 10.CEKIRDEK |

Kişiler adla anılmaz (ekranda ad yok; promptta "the man" / "the woman"). Adam S3'e kadar görünmez; iki kardeşin ilişkisi fragmanda kurulmaz (sorunun parçası değil).

## 5. GÜVENLİ ALAN — 9:16 (SHORTS_SISTEM_PROMPTU güvenli alan haritası)

```
1080×1920 eşdeğeri: alt 484 px (y > 1436, karenin alt ~%25'i) ve sağ 242 px (~%22) arayüz altında kalır.
KURAL  · hiçbir yüz, el, çekirdek ya da yeşil nokta kümesinin odak kısmı alt çeyrekte ya da sağ şeritte durmaz
       · kişi çekimlerinde promptta birebir: "No part of the figure falls into the bottom quarter of the frame."
       · nesne / mekân çekimlerinde odak kadrajın orta ve sol-orta bantlarında yazılır; alt çeyrek zemin, buhar, kaburga dibi gibi önemsiz yüzeydir
KAPAK  Shorts kapağı V4 karesidir: 120 px genişlikte elle test (FRAGMAN §2.2 ⑥)
```

## 6. LOOP SATIRI (SENARYO_VE_VIRAL_KAMERA §5)

```
① KADRAJ  V4 son karesi: karanlık zeminde ortada parlayan amber dikdörtgen (çekirdeğin camı, iki koyu kenar arasında)
          → V1a ilk karesi: iki koyu kaburga arasında kabaran turuncu ışık. Grafik eşleşme: koyu dikey kenarlar + ortada sıcak ışık.
② HAREKET V4 donmaz: yaklaşma ve amber güçlenmesi sürerken kesilir; V1a hareketle başlar (ışık kabarıyor).
③ SES     müzik kadansla bitmez; 39,0-40,0 düşük katman ya da 1 s sessizlik (besteci).
④ JENERİK yok — film adı platform başlığında yaşar.
⑤ IŞIK    S4 içeride (koridor) ↔ S1 dışarıda (fırın): renk farkı tasarımdır — çalınan küçük ateş, dev ateşe kesilir.
```

## 7. KURGU — kesim listesi (taslak; deneme seçildikten sonra kurgucu kesinleştirir)

| Çekim | Fragman saniyesi | Kliptan dilim (10 s klip) | Kesme |
|:--:|:--:|:--:|---|
| V1a | 0,0-3,5 | 0,0-3,5 | sert · ışık kabarmasının ortasında |
| V1b | 3,5-10,0 | 0,0-6,5 | sert · S1 → S2 |
| V2a | 10,0-15,0 | 0,0-5,0 | sert · mandal durduktan sonra |
| V2b | 15,0-20,0 | 0,0-5,0 | sert · S2 → S3 |
| V3a | 20,0-25,0 | 0,0-5,0 | sert · kaldırma bittikten sonra |
| V3b | 25,0-30,0 | 0,0-5,0 | sert · S3 → S4 |
| V4 | 30,0-40,0 | 0,0-10,0 | loop → V1a |

Dilimler klibin başından alınır; promptlar ana hareketi dilimin İÇİNE koyar, klibin kalanı yedek kuyruktur (kurgucu kaydırabilir).
Hız rampası, ağır çekim, klip içi kesme yok.

## 8. SES + MÜZİK

```
YATAK   FILM §6 birebir, kurguda: V1a Y1 (dış, vakum: low steady non-diegetic pressure tone …) · V1b Y4 (kriyo) · V2a V3a Y7 (kasa) · V2b V3b V4 Y3 (koridor)
EFEKT   V2a mandal dönüşü (basınçlı iç, kuru metal tık) · V3a beşikten kalkış (hafif metal sürtünme) · dışta (V1a) gerçekçi ses yok, yalnız tasarım tonu
MÜZİK   tek cue, tek tırmanış (FRAGMAN §2) — besteci yazar: vuruşlar 3,5 · 10 · 15 · 20 · 25 · 30 kesmelerine oturur, 30-40 çözülmeden asılı, loop uyumlu son
REPLİK  0
```

## 9. ÜRETİM SIRASI (FRAGMAN §2.2)

```
0. Ön koşul: filmin referansları 1 · 2 · 5 · 6 · 7 · 8 · 10 üretilmiş ve onaylı (FILM §3 SHA) — film F7a
1. AFİŞ İLK: V4 (kapı — iki ışık tek vizörde okunmuyorsa fragman yoktur, kalan vuruşlara üretim harcanmaz) → dur, Fable + devamlilik bakar
2. HOOK ikinci: V1a
3. kalanlar: V1b · V2a · V2b · V3a · V3b
Kare: 9:16 piksel (1152×2048 ya da 864×1536; ChatGPT 1024×1536 verirse merkezden 864×1536, yanlar 80'er px) — GPT_IMAGE_OMNI §13
Dosya: fragman_dikey/kare/V1a.png … · video fragman_dikey/ham/V1a_d1.mp4 · _d2.mp4 · Omni'ye yalnız kare yüklenir
```

## 10. KURGU KAPISI (FRAGMAN §1.2 · §2.2)

```
□ SPOILER LİSTESİ (§2) — her kalem 0 kare
□ TEK CÜMLE TESTİ — ilk kez izleyen biri tek cümleyle anlatır; cümlede cevapsız soru kalır
□ İMZA TESTİ — V4 (iki ışık tek vizörde) kurguda var ve ters çevrilmemiş
□ PAKETLEME TESTİ — Shorts başlığı ve açıklaması olay dizisi anlatmaz (VIRAL_BASLIK_VE_ACIKLAMA_PROMPT TEASER modu); uzun film linki SABİT YORUMDA
□ çekim sayısı 7 · süre 40,0 s · ekran metni 0,0 s · güvenli alan (§5) · loop dikişi üst üste bindirilerek (§6)
```

## 11. PROMPTLAR

> Eleştiri turundan sonra yazılır (goruntu-yonetmeni). Çapalar FILM §3'ten birebir: Reference <No> (<rol>) anahtarı ROL SÖZLÜĞÜ'nden,
> KİMLİK TABANI, MEKÂN IŞIĞI, DIŞ DÜNYA, ORTAK GÖRÜNÜM. Video promptunda 10 s, 2-4 vuruş, ses cümlesi yok.
