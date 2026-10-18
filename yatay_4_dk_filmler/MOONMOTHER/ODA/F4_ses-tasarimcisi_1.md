# F4 · ses-tasarimcisi · tur 1 — MOONMOTHER

> Bu dosya MOONMOTHER'ın ses planıdır. Yerleşim: §1 sahne tablosu, §2 ORTAM satırı, §6 ORTAM YATAĞI ve §7 GEÇİŞ `FILM.md` §6'ya taşınır; §3-§5 ve §8-§11 `ODA/`'da kalır.
> Saniyeler çekim içidir (0-10) ve **nominaldir**: `FILM.md` §4 vuruş planından alındı. Film saati = 10 × (Cxx − 1) + saniye (mutlak saniye yalnız §8'de).
> F8'de seçilen denemenin gerçek adım ve ışık anlarına ±0.3 s kaydırılır; ışık-nota eşleşmeleri (C02 C05 C17 C18 C20 C23) ±0.1 s'de kapanır.
> Seviye ölçeği: **0 dB = C22 dalga darbesinin tepesi** (filmin en yüksek anı). Yataklar ve müzik LUFS ile yazılır (kural 8). İki ölçek aynı sayı doğrusu değildir:
> yatağın altında kalan her efekt satırı yatağın üstünde duyulacak bantta (1-4 kHz) tutulur; F8'de kulakla doğrulanır. Mutlak seviye (−14 LUFS) son aşamada `kurgu.py yukseklik` ile kurulur.
> S<n> = plan C<n> = `FILM.md` Cxx. Bu filmde telsiz, kask ve vakum yoktur: telsiz filtresi, replik yerleşimi ve kask içi kuralları uygulanmaz.

## 0. KARAR ÖZETİ

```
MODEL SESİ     KAPALI (NOTLAR KARARLAR 16.10.2026). Gemini/Omni klibinin kendi sesi gelir ama kurguda atılır (timeline klip_sesi: false, varsayılan).
               F5 video promptlarına ses satırı da planın ortak ses kuyruğu da yazılmaz. Bütün ses (ortam, efekt, çağrı, müzik) bu planla kurguda kurulur.
               Planın 24 "Sound:" satırının 24'ü de §4-§5'e taşındı (§11 eşleme); düşen satır yok, değişen tek satır C05'in "warm" kelimesi (F2 ürün notu).
REPLİK         YOK. KAYIT LİSTESİ (§3) sözsüz canlı seslerin listesidir: Oru ve Anne çağrısı + Khev kliği. Hepsi tek kaynaktan.
ORTAM FİZİĞİ   Açık, nefes alınabilir, SES TAŞIYAN atmosfer (gece, deniz kıyısı). Vakum yok, kask yok, iç hacim yok; C24 de bulut tepelerinin üstünde ama atmosferin
               içinde (tretman: boş uzay yolculuğu yok). Rüzgâr, sörf, sprey, taş takırtısı DUYULUR: görüntü bunları gösteriyor, sessiz dalga görüntüyle çelişirdi.
               "İnce atmosfer boğukluğu" uygulanmaz (çağrılar camsı ve tizdir). Ölçek kuralı: büyük şey = alçak perde + yavaş atak + uzun bırakış.
KATMAN         K1 ortam yatağı · K2 efekt (foley + su + taş) · K3 çağrı (replik yerine canlı sesi) · K4 müzik. Sahne başına ≤4, hepsi tabloda.
ÇAĞRI KODU     1) ÜÇ NOTA = ÜÇ IŞIK. Çağrı yalnız ışık yanarken notalıdır; ışık önce, nota 0.05-0.1 s sonra. Işık sönükse nota yok:
                  C03 (üç ışık sönük) → tek ton · C16 (ışık sönük) → nota yok, tarama süpürmesi. C01'de ışıklar silüet ölçeğinde görünmez ama Oru'nun notaları duyulur.
               2) TEK KAYNAK. ORU_CAGRI_v1 bir kez üretilir; bütün Oru ve Anne çağrıları ondan işlenir, yeniden üretilmez (plan: "aynı kayıt veya aynı ses tasarımı").
               3) PERDE: D5 · G5 · A5 (587.3 · 784.0 · 880.0 Hz). Kanonik ritim: nota başları 0 / 0.9 / 1.8 s, üçüncü nota tutulur. Anne aynı notalar 2 oktav aşağıda
                  (D3 · G3 · A3 = 146.8 · 196.0 · 220.0 Hz). Besteci başka tonalite seçerse çağrı kaydı tek hamlede ≤3 st kaydırılır (formant sabit).
               4) IŞIĞA OTURMA. Işıklı çekimlerde nota başları o denemenin ışık başlarına oturur (nota nota yerleşim: oru_n1/n2/n3.wav); aralık değişse de SIRA ve ORAN
                  (kısa · kısa · uzun) korunur. Işıksız ya da silüet çekimlerde bütün cümle (oru_cagri_tam.wav) kanonik aralıkla yerleşir.
               5) AKRABALIK SESLE OKUNUR (F3 açık ÖLÜMCÜL: görüntü tek başına taşımıyor). C05'te anne SOĞUK: yalnız tek harmonikler, −25 cent düşük, boş salon yankısı.
                  C06'da SICAK: tam harmonikler, tam perde, aynı nota başları, iki oktav aşağıda üst üste: iki ses TEK SES gibi tınlar. Soğuk → sıcak = tanıma.
               6) CEVAP GECİKMESİ güveni taşır: C17→C18 arasında 9.2 s aranma (tonsuz dikkat) · C20'de örtüşme (anne beklemeden cevap verir). Bkz. §3.
KHEV SESİ      Klik + solungaç nefesi (kuru, kâğıtsı, insan olmayan). İnsan nefesi, iç çekişi, sesi yok. Plan: "tense inhaling click · clicking cry · pained chitin click".
SÖRF SAATİ     Su = film saati (FILM §1 ENGEL "Saat"). Sörf seviyesi çekim çekim yükselir (§5 satırları). İstisna C19: yüzgeç altında su DÜZLEŞİR, sörf −16'dan −28'e iner:
               "hızla gelen kütle sırt doğurur, alçalan kütle doğurmaz" kuralı kulakla da okunur. Sörf düzensizdir; periyodik darbe yok.
SERT KESMELER  Yalnız planlı: C13→C14 (0.25 s yatak-tek boşluk, iniş C14 0.0) · C10 7.0-8.6 müzik susar · C22 3.1-3.35 kükreme çöker (darbe öncesi nefes) · film sonu.
İLK 30 S       C01 0.0'da kapak gıcırtısıyla başlar (sorun duyuluyor); insan sesi yok (insan yok); müzik C01-C02'de yok, C03 2.0'da çok alçak girer; C01→C02'de yatak sürer.
```

## 1. SAHNE TABLOSU (FILM.md §6'ya taşınır)

K3 = çağrı (replik yerine). Köprü sütunu = o çekimden sonraki kesme. J = sonraki sesin önden girmesi, L = bu sesin taşması.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | K1 Y1 · K2 göz kapağı gıcırtısı 0-8.4 + Khev adımları 1.2 / 3.1 + omuz plakaları 3.6 · K3 Oru'nun üç ince ıslığı 4.6 (uzak) + anne nefesi 7.4 · K4 yok | **L 1.2 s:** anne nefesinin kuyruğu C02'ye | İlk ses 0.0'da kapak gıcırtısı: "ay" kımıldıyor, sorun duyuluyor. Çağrı → nefes: Oru üç nota söyler, gök notasız, devasa bir nefesle cevap verir (kod henüz kurulmadı: belirsiz). |
| S2 (C02) | K1 Y1 · K2 membran titremesi, kitin tıkları, Khev uzun nefes · K3 Oru çağrısı (titrek-ince) ışıklara oturur 3.2 / 4.6 / 6.0 · K4 yok | **J 1.2 s:** gök basıncı (tonsuz yükseliş) C02 8.8'den | 7.4-8.8 dinleme boşluğu: yalnız yatak. Işık = ses kodu burada öğretilir. |
| S3 (C03) | K1 Y1 · K2 yüzgeç havası (0-10, zirve 7.0) + okyanus rezonansı · K3 anne tek harmonik ton 5.6-9.4 (notasız, ışık sönük) · K4 L0 2.0'dan (çok alçak) | **L 1.0 s:** yüzgeç havası C04 0-1.0'a | Başlık (kurgu) C03 27-30 s'de: ses karşılığı yok, ton sürer. Ses: nefes → tek ton → (C05) üç nota: sesin açılışı kademeli. |
| S4 (C04) | K1 Y1 · K2 adım + sürtme 3.3, ikinci ayak 4.8-6.3, kemer tonu 5.6'dan, kabuk kıvrımı 7.7 · K3 uzak anne uğultusu (tonsuz) + Oru korku ıslığı 6.5 · K4 ince (L0, ıslıkta −9 dB) | **J 1.5 s:** dikkat şişmesi C04 8.5'ten (tonsuz) | Gölge sınırı ses sınırıdır: kemer tonu Khev'in ayakları çizgiyi geçtiği 6.0'da girer (kuru, kapalı, sol ağırlıklı). |
| S5 (C05) | K1 Y1 · K2 bulut telleri · K3 anne SOĞUK çağrı ışıklara 0.9 / 2.5 / 4.1 + üç ışık birlikte küme 5.0-7.0 + göz bebeği inişi sub kayması 7.2-9.6 · K4 yok | **L 0.8 s:** soğuk salon yankısı C06'ya | Cevap tınısı soğuk ve boş (akrabalık burada KANITLANMAZ). Müziksiz: ilk kez üç nota yalnız. |
| S6 (C06) | K1 Y1 · K2 esinti genişlemesi, Oru sağ yüzgeç membranı, boyun plakası · K3 Oru + anne SICAK üst üste 2.0-6.4 · K4 58.0'dan çok alçak şişme (besteci) | **J 1.0 s:** su kükremesi C06 9.0'dan | 60. saniye ödülü sesle: iki ses aynı notalarla iki oktav arayla üst üste, tek ses gibi. 6.8-10 boşluk: yalnız rüzgâr ve deniz. |
| S7 (C07) | K1 Y1 · K2 sırt kükremesi, basınç harmonikleri (0-4.5), gevşek taşlar, sprey · K3 anne durur: uzun hava bırakışı 4.2-6.0 · K4 nabız 6.0'dan (66.0) | **L 1.5 s:** sırt kükremesi C08'e | Anne durunca basınç harmonikleri kesilir: "kendini tutuyor" kulakta. Sırt tek ve geniş, sağdan sola yürür. Nabız saati sırtla birlikte başlatır. |
| S8 (C08) | K1 Y1 · K2 kemer tonu (kapalı), sörf çıkıntı kenarına vurur 2.2 / 4.8 / 8.0 (öncekinden yakın), kabuk · K3 Oru küçük çağrı 5.2 (ışık atımı) · K4 nabız | **Hareket üstünde:** ayak parmağı sesi C08 7.6 → C09 0.6'da adım | Üç seviye sesle de ayrılır: kemer altı kapalı ve kuru, geçit açık, çıkıntıya yakın sörf. |
| S9 (C09) | K1 Y1 · K2 iki ağır adım 2.0 / 5.0, kitin sürtünmesi, kemer tonu 0.8-2.3 solar, sörf yükselir, uzak sırt · K3 Oru ışık atımı 6.6 · K4 nabız yükselir | **J 1.0 s:** taş gıcırtısı C09 9.0'dan | Gölge sınırını geçince kapalı oda kapanır, açık sörf yükselir: "sığınağı bırakıyor" kulakta. |
| S10 (C10) | K1 Y1 · K2 öncü kıvrım (0-3.5), taş gıcırtısı genişler (→7.0), kırılma 7.2, düşüş 7.3-8.1, ağır su çarpması 8.1, sprey çöker · K3 yok · K4 nabız; 7.0-8.6 sessiz | **L 1.5 s:** çarpma ve sprey kuyruğu C11'e | Sebep (sırt) ve sonuç (kopuş) aynı çekimde sesle de bağlı. Kopuştan sonra boşluk: su çekilirken yatak çıplak duyulur. |
| S11 (C11) | K1 Y1 · K2 Oru kanat çırpışı, Khev ellerini uzatır, Khev uzun yavaş nefes, sörf · K3 Oru "umut → zayıf" çağrısı 1.0-6.6 · K4 nabız seyrelir, 6.6'da kırılır | **Köprü yok (kesme sesin üstünde):** düşen ıslık C11 9.9'da biter, Oru'nun iniş sesi C12 0.15'te | Motif kırılır: iki nota yükselir, üçüncü yükselmez çöker; yüzgeç taşımıyor. Düşüş kesmede, sesi iniş. |
| S12 (C12) | K1 Y1 · K2 iniş sesi, membran, Oru nefesi, sprey çizgisi, uzak ağır sörf · K3 Oru zayıf çağrı 1.4 ve 9.15 · K4 yok (en çok tek tutulan ton ≤ −30 LUFS) | **L 1.0 s:** 9.15'teki zayıf çağrı C13 1.0'a taşar | Fener sönükken çağrı da zayıf: ışık = ses yasası. Sprey kenarı Oru'ya ulaşmaz; ses de yalnız kenara kadar. |
| S13 (C13) | K1 Y1 · K2 Khev nefesi, boyun plakası, karar kliği 6.6, itiş sürtmesi 8.0, düşüş rüzgârı 8.1-9.7 · K3 Khev klik 6.6 (K2'ye yazıldı, bkz. §5) · K4 6.8'de susar | **Sert kesme (planlı):** rüzgâr 9.75'te biter, 0.25 s yalnız yatak, iniş C14 0.0 | DORUK. 7.0-7.9 Khev'in tuttuğu nefes: bu sürede yalnız yatak ve sörf. Kemere bakış sessiz, Oru'ya bakış çağrı kuyruğuyla (L). |
| S14 (C14) | K1 Y1 · K2 iniş darbesi 0.0 + plaka çatlağı 0.02 + gerilme gıcırtısı + acılı nefes · K3 Khev acı klik-trili 1.3 + Oru solgun notaları 7.2 / 8.6 · K4 yok | **L 0.8 s:** Khev nefesi ve Oru'nun solgun notası C15'e | BEDEL sesle işaretlenir: çatlak çıtırtısı (E25) bundan sonra sol bacağın her yük verme girişiminde duyulur (C15 C16 C20 C21). |
| S15 (C15) | K1 Y1 · K2 beşik teması, Oru nefesi, çatlak çıtırtısı 5.5, köpük yalaması 6.5-10 · K3 Oru zayıf-düzenli ıslık 0.8 / 1.9 / 3.0 · K4 yok | **J 0.8 s:** sörf yükselişi C15 9.2'den | Çağrı C12'den bir kademe canlı ama zayıf; köpük çizgisi sesle yaklaşır, saat işler. |
| S16 (C16) | K1 Y1 · K2 sörf kükremesi yükselir, doğrulma çabası, çatlak çıtırtısı, çöküş 4.2, rüzgâr kabarması · K3 anne TARAMA süpürmesi 0.8-3.2 (nota yok, cevap yok) + Khev acı klik 3.6 · K4 154.0'dan geri (nabızsız, gergin) | **Köprü yok:** C17 0.0'da sörf −2 dB iner (Khev'in alımı) | Anne arar ama ışıksız: nota yok, kod çalışmaz. 3.2'den sonra cevapsız 1 s: yatak ve sörf. |
| S17 (C17) | K1 Y1 · K2 sörf bedi büyür, sprey patlamaları · K3 Oru TAM çağrı ışıklara 3.3 / 4.6 / 5.9, N3 → 7.6 · K4 çağrı penceresinde yok | **L 1.2 s + J 1.6 s:** çağrı yankısı C18 0-1.2; anne dikkati (tonsuz) C17 8.4'ten | 7.6-10 dinleme boşluğu: çağrı yok, müzik yok, Khev sessiz; yalnız kabaran sırt. Filmin en açık Oru'su. |
| S18 (C18) | K1 Y1 · K2 sprey perdesi, sörf altta sürer, alt göz kapağı · K3 anne dikkat tonu (gezinir → D'ye kilitlenir 6.2) + anne SICAK cevap 6.8 / 8.0 / 9.2 · K4 178.0'dan sıcak dönüş (−9 dB) | **L 1.5 s:** N3 kuyruğu C19'a, yüzgeç rezonansına çözülür | Aranma → bulunma: perde gezinir, göz bebeği durunca kilitlenir, ilk nota ışıkla gelir. Güven burada başlar. |
| S19 (C19) | K1 Y1 · K2 yüzgeç rezonansı (D), membran gıcırtısı 5.0, sakin su yalaması, ufuk sırtı · K3 yok · K4 sıcak koruyucu uyum | **L 1.0 s:** yüzgeç rezonansı C20'ye | KURAL KULAKTA: yüzgeç inerken sörf 0.5-1.5 s'de −16 → −28 düzleşir, altında sakin yalama; uzak sırt ayrı ve alçak. |
| S20 (C20) | K1 Y1 · K2 Oru kanat çırpışı, konma, Khev kalkamama nefesi + çatlak çıtırtısı · K3 Oru PARLAK çağrı 6.9 / 7.7 / 8.5 + anne alçak cevap 9.0 / 9.9 / C21 0.8 · K4 pencerede −9 dB | **L 1.8 s:** anne cevabının 3. notası C21 0.8'de | Anne beklemeden cevap verir (Oru N3 üstüne örtüşür): aranma bitti. Cevap hissedilen alt perdede (D2-G2-A2). |
| S21 (C21) | K1 Y1 · K2 çaba kliği 0.35, taş→membran sürtmesi, çatlak çıtırtısı, rahatlama nefesi, köpük, damar parıltısı · K3 anne cevabının sonu 0.8 · K4 sıcak | **J 2.0 s:** dalga baskısı C21 8.0'dan | Zemin taştan canlı yüzeye geçer: sürtme sesi gritten yumuşak membrana döner. |
| S22 (C22) | K1 Y1 → Y2 çapraz 217-220 · K2 yüzgeç yükselişi, kükreme, DALGA 3.4, yayılan kükreme, sprey, su çekilir · K3 anne sabit alçak ton 6.6'dan · K4 212.8-217.6 yok | **L 1.5 s:** sprey kuyruğu C23'e | Film zirvesi 0 dB: yalnız boş kaya vurulurken. 3.1-3.35 darbe öncesi 0.25 s çöküş. Müzik yok: dalga müziktir. |
| S23 (C23) | K1 Y2 · K2 yüzgeç damar parıltısı, temas, rahat nefesler, uzaklaşan okyanus kalıntısı · K3 Oru TAMAMLANMIŞ ifade 3.2 / 4.2 / 5.2 · K4 çözülen uyum (−9 dB) | **J 1.0 s:** anne ön nefesi C23 9.0'dan | Khev'in nefesi filmde ilk kez düzenli: korkunun yerini güven alır. Çatlak çıtırtısı yok (yük vermiyor). |
| S24 (C24) | K1 Y2 (+ yüksek rüzgâr) · K2 yüzgeç esnemesi, uzak sörf solar, şafak parıltısı 8.8 · K3 anne motifi tamam 1.0 / 3.0 / 5.0 (N3 → 9.0) + Oru tek nota 6.0 · K4 final cümle | Çıkış yok (film sonu) | Yeni tehdit yok; doğal kuyruk. Son 1 s yatak solar, çağrı ve müzik kuyruğu 9.85'e dek doğal biter. |

## 2. ORTAM (FILM.md §6 satırı için)

```
Ortam: Açık, nefes alınabilir, ses taşıyan atmosfer (gece, deniz kıyısı). Vakum yok, kask yok, iç hacim yok; C24 bulut tepelerinin üstünde ama atmosferin içinde.
       Duyulan: rüzgâr, sörf, sprey, taş (hava ile taşınır) · kitin, membran, taş teması (temas) · Oru, Anne ve Khev'in sözsüz sesleri (canlı).
       Ölçek: dev şey alçak ve yavaş, küçük şey tiz ve hızlı. Telsiz ve replik yok. Ortam yatağı Y1 (kıyı) 0.0-220.0, Y2 (yüzgeç-hava) 217.0-240.0; dijital sıfır yok.
       Model sesi kullanılmaz (klip sesi atılır; ses kurguda).
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_1.md
```

## 3. KAYIT LİSTESİ (REPLİK yok: sözsüz canlı sesler, tek kaynak)

Ses aracı sahibindir; profil adları araçtan bağımsızdır. Ticari koşul: Flow Music ve Mondo Sónico çıktılarının ticari koşulu BİLİNMİYOR (`FLOW_GERCEKLERI` §6); araç seçimi sahibin.
`model` filtreli satır yok: ağız kadrajda replik yok. Filtre sütunu bu filmde mesafe profilidir: **YAKIN** (kuru, yansımasız) · **ORTA** (kısa açık hava yankısı, RT 1.2 s) · **UZAK** (4 kHz alçak geçiren, uzun yansıma) · **DEV** (RT 3-7 s, geniş stereo).
Üç profil, film boyu aynı: **ORU_CAGRI_v1** · **ANNE_CAGRI_v1** (ORU'dan türetilir) · **KHEV_KLIK_v1**.

| No | Metin (nota / ifade) | Konuşan | Ses profili | Ton | Hedef süre (s) | Filtre | Çekim · saniye |
|:--:|---|---|---|---|:--:|---|---|
| R01 | üç nota D5-G5-A5, ince, cümle | Oru | ORU_CAGRI_v1 | ince-uzak | 3.0 | UZAK | C01 · 4.6 |
| R02 | tonsuz devasa nefes | Anne | ANNE_CAGRI_v1 · nefes | boş-devasa | 3.8 (+1.2 L) | DEV | C01 · 7.4 |
| R03 | üç nota, ışığa oturur, titrek | Oru | ORU_CAGRI_v1 | titrek-ince | 4.2 | ORTA | C02 · 3.2 |
| R04 | tek derin harmonik ton (D3 + D2) | Anne | ANNE_CAGRI_v1 · ton | derin | 3.8 | DEV | C03 · 5.6 |
| R05 | uzak, tonsuz uğultu (D1-D2 bölgesi); 8.5'te dikkat şişmesi | Anne | ANNE_CAGRI_v1 · uğultu | uzak | 10 (+J 1.5) | DEV | C04 · 0.0 ve 8.5 |
| R06 | tek nota N1, kırılarak iner | Oru | ORU_CAGRI_v1 · korku | korkmuş | 0.7 | ORTA | C04 · 6.5 |
| R07 | üç nota ışığa oturur + küme (5.0-7.0) + sub kayma | Anne | ANNE_CAGRI_v1 · soğuk | boş-soğuk | 9.0 | DEV (soğuk salon RT 7 s) | C05 · 0.9 |
| R08 | Oru üç nota + Anne aynı üç nota üst üste | Oru + Anne | ORU_CAGRI_v1 + ANNE_CAGRI_v1 · sıcak | ince + sıcak | 4.4 | ORTA + DEV | C06 · 2.0 |
| R09 | küçük çağrı, kısa N3 | Oru | ORU_CAGRI_v1 · küçük | umutlu-ısrarlı | 1.8 | ORTA | C08 · 5.2 |
| R10 | küçük çağrı, ışık atımı | Oru | ORU_CAGRI_v1 · küçük | ısrarlı | 1.6 | ORTA | C09 · 6.6 |
| R11 | N1-N2 yükselir, N3 yükselmez çöker | Oru | ORU_CAGRI_v1 · umut→zayıf | umutlu → çöken | 5.8 | ORTA → UZAK | C11 · 1.0 |
| R12 | tek nota N1, nefesli, titrek | Oru | ORU_CAGRI_v1 · zayıf | kırılgan | 1.0 | YAKIN | C12 · 1.4 |
| R13 | tek nota N1, solgun | Oru | ORU_CAGRI_v1 · zayıf | solgun | 0.8 (+1.0 L) | YAKIN | C12 · 9.15 |
| R14 | gergin içe çekiş kliği | Khev | KHEV_KLIK_v1 | gergin | 0.4 | YAKIN | C13 · 6.6 |
| R15 | acı klik-trili: üç hızlanan klik, kesilir | Khev | KHEV_KLIK_v1 | kısıtlı-acılı | 0.9 | YAKIN | C14 · 1.3 |
| R16 | iki solgun nota | Oru | ORU_CAGRI_v1 · zayıf | solgun | 0.8 + 0.8 | YAKIN | C14 · 7.2 ve 8.6 |
| R17 | üç nota, zayıf ama düzenli | Oru | ORU_CAGRI_v1 · zayıf-düzenli | zayıf-canlanan | 3.0 | YAKIN | C15 · 0.8 |
| R18 | tonsuz yükselen süpürme, cevapsız biter | Anne | ANNE_CAGRI_v1 · tarama | arayan | 2.4 | DEV | C16 · 0.8 |
| R19 | acılı tek klik | Khev | KHEV_KLIK_v1 | acılı | 0.3 | YAKIN | C16 · 3.6 |
| R20 | üç nota ışığa oturur, tam bant, N3 uzun | Oru | ORU_CAGRI_v1 · tam | açık-kararlı | 4.3 | ORTA | C17 · 3.3 |
| R21 | tonsuz dikkat: şişme → gezinme → D'ye kilit | Anne | ANNE_CAGRI_v1 · dikkat | arayan → bulan | 8.4 + 6.2 | DEV | C17 · 8.4 → C18 · 6.2 |
| R22 | üç nota ışığa oturur, sıcak, N3 C19'a taşar | Anne | ANNE_CAGRI_v1 · sıcak | sıcak-devasa | 4.7 (+1.5 L) | DEV | C18 · 6.8 |
| R23 | üç nota parlak, hızlı aralık | Oru | ORU_CAGRI_v1 · parlak | neşeli-rahatlamış | 2.4 | ORTA | C20 · 6.9 |
| R24 | alt perdede üç nota (D2 G2 A2), hissedilen | Anne | ANNE_CAGRI_v1 · alçak | koruyucu | 2.6 | DEV | C20 · 9.0 → C21 · 0.8 |
| R25 | çaba kliği | Khev | KHEV_KLIK_v1 | çabalı | 0.3 | YAKIN | C21 · 0.35 |
| R26 | sabit alçak ton (D), vibratosuz | Anne | ANNE_CAGRI_v1 · ton | güvenli | 3.4 + Y2'ye akar | DEV | C22 · 6.6 |
| R27 | tamamlanmış ifade, üç nota ılık | Oru | ORU_CAGRI_v1 · tamamlanmış | huzurlu | 3.0 | YAKIN | C23 · 3.2 |
| R28 | motif tamam: üç nota yavaş, N3 tutulur | Anne | ANNE_CAGRI_v1 · sıcak | çözülmüş-engin | 8.0 | DEV | C24 · 1.0 |
| R29 | tek ince nota A5, anne N3'ü üstünde (oktav kaynaşması) | Oru | ORU_CAGRI_v1 · tamamlanmış | küçük-huzurlu | 1.2 | UZAK | C24 · 6.0 |

```
KAYIT NOTLARI
ORU_CAGRI_v1   Üretim promptu: a tiny alien creature's thin glassy three-note whistle call, notes D5 then G5 then A5 about 0.9 seconds apart, the last note held with slight vibrato,
               pure whistle tone with soft glass harmonics, dry close recording, no reverb, no music, no words.
               Araç perdeyi tutmazsa: üç nota ayrı üretilir ya da cam harmonika / ıslık sentezi ile kurulur; perde ölçülür (587.3 · 784.0 · 880.0 Hz). Çıktı dosyaları:
               oru_cagri_tam.wav (cümle, kanonik aralık) · oru_n1.wav · oru_n2.wav · oru_n3.wav (ışığa oturan çekimler için ayrı notalar, her biri 1.5 s kuyruklu).
ANNE_CAGRI_v1  Zincir: ORU_CAGRI_v1 → pitch −24 st · formant −8 st · atak 0.25 s · tutuş ×2 · bırakış 2 s · gövde katmanı (a bowed low organic tone with soft breathy formants, D2 G2 A2)
               −6 dB · reverb. SICAK: tam harmonikler, tam perde, açık hava RT 3.5 s, deniz yüzeyinden erken yansıma. SOĞUK (yalnız C05): yalnız tek harmonikler, −25 cent,
               RT 7 s, ön gecikme 120 ms, gövde katmanı yok. ALÇAK (C20): −12 st daha, yalnız hissedilen, −14.
               TELEFON PAYI: temel ≥ 140 Hz; 2. ve 3. harmonikler (290-660 Hz) çıplak duyulacak seviyede (kayıttan sonra telefon hoparlöründe dinlenir). Yalnız çok alçak bas yetmez.
KHEV_KLIK_v1   Üretim promptu: a dry restrained chitin click made by a large insect-like alien throat, low body around 200 hertz with a sharp tick, single, no human voice, close and dry.
               Varyantlar: gergin içe çekiş (yükselen, kısa) · acı klik-trili (üç hızlanan klik, kesilir) · acılı tek klik · çaba kliği (tek, ağır). Aynı oturumda, aynı mikrofon.
IŞIK ÖNCE      Çekim seçildikten sonra ışık başları kare kare okunur (kareler.py cikar, 24 fps); nota başı ışık başından 0.05-0.1 s sonra. Işık sırası soldan sağa = nota sırası.
```

### 3b. Çağrı durumları (yeni kayıt değil, işleme)

| Durum | Çekim | Ne değişir |
|---|---|---|
| ince-uzak | C01 | 4 kHz alçak geçiren, hafif tremolo, uzun yansıma, −20 |
| titrek-ince | C02 | tremolo %12 (5.5 Hz), hafif nefesli, orta mesafe, −10 |
| korku | C04 | yalnız N1; kırılarak iner (−5 st / 0.5 s) |
| küçük | C08 C09 | kanonik, N3 kısa (kuyruksuz), +20 cent yükselişle ısrarlı |
| umut → zayıf | C11 | N1-N2 12 cent yukarı eğimli; N3 yükselmez, −7 st / 2.2 s çöker, seviye −12 → −26 |
| zayıf | C12 C14 | −8 dB, nefesli, ±35 cent titrek; N2 geç ya da eksik |
| zayıf-düzenli | C15 | zayıf ama sıralı ve eşit aralıklı: C12'den "bir kademe canlı" |
| tam | C17 | tam bant, 3 kHz'de +2 dB, N3 uzun; üç ışık yanıkken cam üst harmonikleri (6.2-7.4) |
| parlak | C20 | tam + aralık 0.8 s (heyecan), yükselen son |
| tamamlanmış | C23 C24(Oru) | ılık: 4 kHz −3 dB, 700 Hz +2 dB; N3 vibratosuz, yumuşak iniş |

### 3c. Çağrı-cevap gecikmeleri (rule 6: kesme gecikmeyi yemez)

| Alışveriş | Gecikme | Bu planda | Anlamı |
|---|:--:|---|---|
| C01 Oru N3 sonu → anne nefesi | 0.1-0.2 s | 7.2 → 7.4 | hemen ve ağır, ama notasız: kod yok |
| C06 Oru + anne | 0 (örtüşür) | 2.0 / 2.05 | akrabalık: aynı anda aynı notalar |
| C17 Oru N3 sonu → anne ilk nota | **9.2 s** (167.6 → 176.8) | araya tonsuz dikkat, gezinme, kilit | aranma → bulunma; C16'nın cevapsız taraması bunun başlangıcı |
| C20 Oru N3 başı → anne ilk nota | **−0.5 s** (örtüşür) | 8.5 → 9.0 (N3 sürerken) | aranma bitti, cevap beklemeden gelir |

## 4. SES VARLIKLARI (E-kodları; §5 satırları bunlara bağlanır)

"Nereden" = tek satır İngilizce üretim ya da arama cümlesi. Hepsi kuru ve temiz üretilir, mesafe/yankı kurguda (§3 profilleri) verilir; ses ve müzik içermeyen kayıt istenir.

| Kod | Ad | Nereden |
|:--:|---|---|
| E01 | göz kapağı | `a colossal organic eyelid slowly peeling open, wet leather creaking over stone, very low and slow, enormous and far away, with a clear midrange creak texture, no voice, no music` |
| E02 | Khev adımı | `one heavy dry footstep of a large clawed biped on gritty basalt, close, fine grit crunch under a muffled thump, no echo, no voice` |
| E03 | kitin plaka | `a soft dry creak and slide of stiff ivory chitin armor plates shifting against each other, close and small, no voice` |
| E05 | anne nefesi | `an immense slow breath from the sky, hollow and low, a vast chamber of air with a faint throat resonance around 400 to 900 hertz, no pitch, no voice, no music` |
| E06 | anne tek ton | `one deep warm harmonic tone of an enormous creature, pitch D3 with a soft D2 underneath, slow swell and long release, bowed-string like texture, no vibrato, no words, no music` |
| E07 | yüzgeç havası | `a vast slow displacement of air as an immense wing rises, broad low rushing roar with midrange body, gradually rising, open air, no voice, no music` |
| E08 | okyanus rezonansı | `distant deep ocean resonance, sub-bass swell with soft irregular rolls, no rhythm, no voices` |
| E09 | ayak sürtmesi | `a dry scrape of a clawed foot sliding across gritty basalt, short, close` |
| E10 | Khev kliği | KHEV_KLIK_v1 (§3 notu) |
| E11 | membran titremesi | `tiny trembling flutter of a thin membrane fin, very quiet and delicate, close` |
| E12 | kemer tonu | `quiet room tone inside a sheltered stone alcove, dry low stone cavity resonance around 150 hertz, wind muffled outside, no echo, no voices` |
| E13 | sörf / sırt | `slow irregular heavy ocean surf on black rock, long swells and slow wash, no rhythm, no voices, no music` · tek sırt: `a single broad dark water ridge building and rolling shoreward, low growing roar with pressure, no foam crackle, no music` |
| E14 | gevşek taş | `loose pebbles and small stones rattling and jumping on rock, sparse and distant` |
| E15 | sprey | `fine sea spray hiss and soft splash droplets in open air, airy, no voices` |
| E16 | taş kopuşu | `a slow widening creak of a heavy stone slab tilting, then one sharp snap` · çarpma: `one heavy slab of rock hitting the sea with a huge splash and falling spray` |
| E17 | Oru kanadı | `soft slow flaps of a wide thin membrane wing, gliding small creature, delicate, close` |
| E18 | düşüş rüzgârı | `wind rushing past a falling body, descending pitch, about one and a half seconds, no voice` |
| E19 | iniş | `a heavy landing of a large biped on rock, one deep body thump with a short gritty skid and low resonance, close` |
| E20 | köpük / yalama | `foam and shallow water creeping over wet rock, soft hiss growing, then one wet slap` · sakin: `gentle water lapping softly under a surface, flat calm` |
| E21 | yüzgeç rezonansı | `a deep warm organic resonance of an immense living wing surface, soft harmonic hum around D, midrange warmth, slow swell, no voice, no music` |
| E22 | membran gıcırtısı | `a soft creak and flex of a huge warm living membrane, slow, gentle` |
| E23 | taştan membrana | `a gritty scrape on stone changing into a soft damp slide across warm living membrane, short` |
| E24 | dalga | `one enormous dark ocean wave hitting an empty rock ledge, a massive impact with sub-bass thump, then a wide spreading roar of water and spray, four seconds, no voices` |
| E25 | çatlak | `a single dry sharp crack of a hard shell plate, with a faint wet glass shimmer after it, close` · çıtırtı: `faint dry crackle of a cracked shell plate flexing, very small, close` |
| E26 | Khev nefesi | `a dry low papery exhale through gill slits of an alien, non-human, slow, close` |
| E27 | şafak parıltısı | `a tiny bright glass-like harmonic shimmer, warm and resolving, very quiet` |
| E28 | Oru nefesi | `very faint airy breathing of a tiny animal, irregular, close` |
| E29 | yüksek rüzgâr | `thin high-altitude wind, soft and airy, wide stereo, no harsh highs` |
| E30 | bulut telleri | `soft airy hiss of thin cloud strands passing, lateral, very quiet` |
| E31 | yüzgeç damarı | `a soft warm glassy tone swell as glowing veins pulse in a living wing, quiet, irregular` |
| E32 | Oru inişi | `a tiny soft thud and membrane scrape of a small soft body landing on stone` |
| E33 | tarama | `a slow low sweeping tone from an immense creature, airy and searching, a rising glide that ends unanswered, no notes, no words` |
| E34 | dikkat | `a slow pitchless low swell of attention from an immense creature, hollow air with slight pitch drift, no notes` |

## 5. EFEKT LİSTESİ (24/24 çekim)

Kaynak: **hava** (açık atmosferde taşınır: rüzgâr, su, taş) · **temas** (taş, kitin, membran teması) · **canlı** (sözsüz canlı sesi).
Y1 her çekimde sürer (§6; satırlara yazılmaz). Işık-nota satırları "ışığa oturur" diye işaretli. Seviye: 0 dB = C22 dalga tepesi; "yatağa" yazılanlar LUFS değil, ölçek dB'sidir.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|:--:|---|---|
| C01 | 0.0-8.4 | göz kapağı açılır: ıslak deri taş üstünde sürer gibi alçak yavaş gıcırtı; kapak ilerledikçe büyür (ilk ses) | temas | K2 | −20 → −12 | E01 |
| C01 | 1.2 · 3.1 | Khev'in iki adımı; ikincisi ayak basılıyken durur | temas | K2 | −22 · −20 | E02 |
| C01 | 3.6 | omuzlar kalkar, kollar Oru'yu sıkar | temas | K2 | −26 | E03 |
| C01 | 4.6 · 5.5 · 6.4 | Oru'nun üç ince ıslığı (uzak), N3 7.2'ye dek | canlı | K3 | −20 | R01 (ince-uzak) |
| C01 | 7.4-11.2 | anne: tek devasa alçak tonsuz nefes; 8.8-9.2 zirve; kuyruk C02 1.2'ye | canlı | K3 | −12 | R02 · E05 |
| C02 | 0.0-1.2 | anne nefesinin kuyruğu (C01'den) | canlı | K3 | −14 → −30 | R02 (L) |
| C02 | 0.8-3.0 | Oru'nun sol yüzgeci titrer | temas | K2 | −32 | E11 |
| C02 | 1.6 | Khev kolları beşiğe oturur: kuru plaka tıkı | temas | K2 | −28 | E03 |
| C02 | 3.2 · 4.6 · 6.0 | Oru'nun üç notası ışıklara oturur (titrek-ince), N3 7.4'e dek | canlı | K3 | −10 | R03 |
| C02 | 6.9-7.6 | Khev başını kaldırır: boyun plakası; 7.2 uzun nefes | temas | K2 | −28 | E03 · E26 |
| C02 | 7.4-8.8 | dinleme boşluğu: yalnız yatak | — | — | — | — |
| C02 | 8.8-10.0 | J: gök basıncı, tonsuz yükseliş (C03'e) | hava | K2 | −34 → −24 | E34 |
| C03 | 0.0-10.0 | yüzgeç havası: bulut kenarından yükselir, 7.0'da zirve, sonra sabit | hava | K2 | −22 → −12 | E07 |
| C03 | 0.0-10.0 | okyanus rezonansı (alt bant) | hava | K2 | −24 | E08 |
| C03 | 5.6-9.4 | anne tek derin harmonik ton (D3 + D2); notasız, ışık sönük | canlı | K3 | −14 | R04 · E06 |
| C04 | 0.0-1.0 | yüzgeç havası kuyruğu (C03'ten) | hava | K2 | −20 → −40 | E07 (L) |
| C04 | 0.0-10.0 | uzak yetişkin uğultusu (tonsuz); 8.5-10.0 −18'e yükselir (J) | canlı | K3 | −30 → −18 | R05 · E34 |
| C04 | 0.9 | ayak kalkışı: plaka çıtırtısı | temas | K2 | −28 | E03 |
| C04 | 3.3 | ayak bazalta basar, kuru sürtme | temas | K2 | −18 | E02 · E09 |
| C04 | 4.8-6.3 | ikinci ayak çekilir; 6.3'te basar | temas | K2 | −22 | E09 |
| C04 | 5.6-7.0 | kemer tonu girer (gölge sınırı 6.0); C08'e dek sürer | hava | K2 | yok → −28 | E12 |
| C04 | 6.5 | Oru'nun korku ıslığı: tek nota, kırılarak iner | canlı | K3 | −16 | R06 |
| C04 | 7.7-9.0 | ön kollar Oru'nun çevresinde kıvrılır: plaka sürtmesi | temas | K2 | −20 | E03 |
| C05 | 0.0-0.9 | J: dikkat şişmesi ilk nota ışığa açılır | canlı | K3 | −18 | E34 |
| C05 | 0.9 · 2.5 · 4.1 | anne SOĞUK çağrı, ışıklara oturur (−25 cent, tek harmonik, salon RT 7 s) | canlı | K3 | −9 | R07 |
| C05 | 5.0-7.0 | üç ışık birlikte: üç nota birlikte tınlar (D-G-A kümesi), zirve 5.4 | canlı | K3 | −8 | R07 |
| C05 | 7.2-9.6 | göz bebeği iner: alt oktava kayan tonsuz sub inişi | canlı | K3 | −24 | E34 (ters) |
| C05 | 0.0-10.0 | bulut telleri: yatay ince hışırtı | hava | K2 | −34 | E30 |
| C06 | 0.0-2.0 | açık hava genişlemesi: rüzgâr esintisi | hava | K2 | −26 | E29 |
| C06 | 1.2 | Oru sağ yüzgecini kaldırır | temas | K2 | −32 | E11 |
| C06 | 2.0 · 2.9 · 3.8 | Oru çağrısı (kanonik aralık) | canlı | K3 | −12 | R08 |
| C06 | 2.05 · 2.95 · 3.85 | anne SICAK çağrı: aynı notalar iki oktav aşağıda, üst üste; N3 6.4'e dek | canlı | K3 | −8 | R08 |
| C06 | 4.5-7.5 | Khev başını baştan kuyruğa çevirir: boyun plakası | temas | K2 | −30 | E03 |
| C06 | 6.8-10.0 | çağrılar bitti: yalnız rüzgâr ve deniz (boşluk) | — | — | — | — |
| C06 | 9.0-10.0 | J: su kükremesi başlar (C07'ye) | hava | K2 | −34 → −28 | E13 |
| C07 | 0.0-4.0 | sırt büyür: kükreme | hava | K2 | −32 → −18 | E13 (tek sırt) |
| C07 | 0.0-4.5 | basınç harmonikleri (tonsuz D1-A1 yığını) yükselir, 4.5'te kesilir | hava | K2 | −26 → −16 | E34 (alçak) |
| C07 | 1.0-10.0 | sprey sıçraması | hava | K2 | −28 | E15 |
| C07 | 1.8 · 2.7 · 3.4 · 6.5 · 8.2 | gevşek taş takırtıları (uzak) | hava | K2 | −28 | E14 |
| C07 | 4.2-6.0 | anne durur: uzun yumuşak hava bırakışı; basınç kesilir | canlı | K3 | −18 | E05 (kısa) |
| C07 | 6.0-10.0 | sırt tek başına ilerler (sağdan sola pan), −18 → −14; C08 1.5'e taşar | hava | K2 | −18 → −14 | E13 |
| C08 | 0.0-1.5 | sırt kükremesi kuyruğu | hava | K2 | −14 → −26 | E13 (L) |
| C08 | 0.0-10.0 | kemer tonu (kapalı, kuru) | hava | K2 | −28 | E12 |
| C08 | 1.0-4.0 | Khev başını çevirir: boyun plakası | temas | K2 | −32 | E03 |
| C08 | 2.2 · 4.8 · 8.0 | sörf çıkıntı kenarına vurur (öncekinden yakın) | hava | K2 | −24 | E13 |
| C08 | 5.2-7.2 | Oru küçük çağrı, ışık atımına oturur | canlı | K3 | −16 | R09 |
| C08 | 7.6 | Khev ayak parmağı gölge çizgisine basar | temas | K2 | −24 | E02 (yumuşak) |
| C09 | 0.6 · 3.6 | adım kalkışlarında kitin sürtünmesi | temas | K2 | −28 | E03 |
| C09 | 2.0 · 5.0 | iki ağır kuru adım (açık geçit, bazalt) | temas | K2 | −14 · −13 | E02 |
| C09 | 0.8-2.3 | kemer tonu solar (çizgi geçildi) | hava | K2 | −28 → yok | E12 (fade) |
| C09 | 0.0-10.0 | sörf yatağı yükselir (ana yükseliş 0-3 s) | hava | K2 | −26 → −18 | E13 |
| C09 | 6.5-10.0 | ufuktaki sırt: uzak alçak kükreme | hava | K2 | −26 → −22 | E13 (uzak) |
| C09 | 6.6 | Oru ışık atımı: küçük çağrı | canlı | K3 | −18 | R10 |
| C09 | 9.0-10.0 | J: taş gıcırtısı başlar (C10'a) | hava | K2 | −30 → −24 | E16 |
| C10 | 0.0-3.5 | sırtın öncü kıvrımı geçidin altına yükselir, taşı yalar | hava | K2 | −22 → −14 | E13 · E15 |
| C10 | 0.0-7.0 | taş gıcırtısı genişler (C09'dan sürer) | hava | K2 | −24 → −12 | E16 |
| C10 | 7.2 | kırılma: tek keskin çatlama | hava | K2 | −6 | E16 |
| C10 | 7.3-8.1 | levha düşer: taş sürtmesi ve dönmesi | hava | K2 | −14 | E16 |
| C10 | 8.1 | denize ağır çarpma + sprey | hava | K2 | −5 | E16 (çarpma) |
| C10 | 8.2-10.0 | sprey çöker, su çekilir (boşluk) | hava | K2 | −14 → −30 | E15 · E20 |
| C11 | 0.0-1.5 | çarpma ve sprey kuyruğu (C10'dan) | hava | K2 | −14 → −34 | E16 (L) |
| C11 | 0.4-4.5 | Oru'nun kanat çırpışı | temas | K2 | −22 | E17 |
| C11 | 1.0 · 2.0 | umutlu yükselen cıvıltı (N1, N2) | canlı | K3 | −10 | R11 |
| C11 | 3.3-6.6 | N3 yükselmez, çöker: inen zayıf ıslık | canlı | K3 | −12 → −26 | R11 |
| C11 | 4.5-7.2 | kanat çırpışı düzensizleşir (sol yüzgeç geride), uzaklaşır | temas | K2 | −22 → −34 | E17 |
| C11 | 4.7 | Khev'in elleri uzanır: kitin sürtmesi | temas | K2 | −28 | E03 |
| C11 | 3.0 · 7.8 | sörf vuruşları (çıkıntı kenarı) | hava | K2 | −24 | E13 |
| C11 | 6.6-9.9 | solgun inen ıslık (kadraj dışı); 9.9'da kesmeyle biter | canlı | K3 | −34 | R11 |
| C11 | 8.0-9.4 | Khev boş elleri görür: uzun yavaş nefes | canlı | K2 | −24 | E26 |
| C12 | 0.15 · 0.4-0.9 | Oru'nun inişi: küçük gövde + membran sürtmesi | temas | K2 | −26 | E32 |
| C12 | 1.4 | zayıf tek çağrı (N1), yüzgeç çabasıyla birlikte | canlı | K3 | −20 | R12 |
| C12 | 3.0 | yüzgeç geri düşer: yumuşak vuruş | temas | K2 | −28 | E32 |
| C12 | 4.0 · 4.6 · 5.7 | düzensiz sönük ışık atımları: soluk nota izleri | canlı | K3 | −34 | R12 (N1-N2 izleri) |
| C12 | 6.0-10.0 | Oru nefesi; 7.5'te yüzgeç bir kez titrer | temas | K2 | −30 · −32 | E28 · E11 |
| C12 | 6.5-10.0 | sprey çizgisi kenarda ilerler (Oru kuru) | hava | K2 | −30 → −26 | E15 |
| C12 | 0.0-10.0 | uzak ağır sörf; 2.5 ve 8.0'da vuruş | hava | K2 | −24 | E13 |
| C12 | 9.15 | ikinci zayıf çağrı (N1, solgun); C13 1.0'a taşar | canlı | K3 | −24 | R13 |
| C13 | 0.0-1.0 | Oru'nun zayıf çağrısının kuyruğu | canlı | K3 | −24 → −34 | R13 (L) |
| C13 | 0.8-2.8 | Khev dikkatli nefes | canlı | K2 | −26 | E26 |
| C13 | 3.0-4.2 · 4.5-5.6 | baş sola (kemer), sonra aşağı: boyun plakası | temas | K2 | −30 | E03 |
| C13 | 6.6 | gergin içe çekiş kliği (karar) | canlı | K2 | −18 | R14 · E10 |
| C13 | 7.0-7.9 | tutulan nefes: Khev sessiz, yalnız yatak ve sörf | — | — | — | — |
| C13 | 8.0 | itiş: pençe taşta sürter | temas | K2 | −12 | E09 |
| C13 | 8.1-9.7 | düşüş rüzgârı, alçalan perde; 9.75'te biter | hava | K2 | −16 → −30 | E18 |
| C13 | 9.75-10.0 | planlı boşluk: yalnız yatak (sert kesme öncesi) | — | — | — | — |
| C13 | 8.5-10.0 | ufuktaki sırt: yükselen alçak uğultu | hava | K2 | −28 | E13 (uzak) |
| C13 | 0.0-10.0 | sörf aşağıda, düzensiz | hava | K2 | −24 → −22 | E13 |
| C14 | 0.0 | iniş: gövde darbesi + kısa sürtme + alçak rezonans (kuyruk 0.6-1.4) | temas | K2 | −6 | E19 |
| C14 | 0.02 | sol kaval plakası çatlar: kuru çatlak + sönük cam parıltısı | temas | K2 | −10 | E25 |
| C14 | 1.0 · 2.4 | sol bacağa yük verme denemesi: gerilme gıcırtısı + çatlak çıtırtısı | temas | K2 | −22 | E03 · E25 (çıtırtı) |
| C14 | 1.3-2.2 | acı klik-trili (kısıtlı), kesilir | canlı | K3 | −14 | R15 · E10 |
| C14 | 3.0-4.2 | baş çatlağa eğilir: boyun plakası | temas | K2 | −30 | E03 |
| C14 | 3.5-6.0 | acılı düzensiz nefes; 7.0'da uzun, gevşeyen nefes (Oru'ya döner) | canlı | K2 | −24 · −26 | E26 |
| C14 | 5.0-10.0 | kadraj kenarından ince sis geçer | hava | K2 | −30 | E15 |
| C14 | 7.2 · 8.6 | Oru'nun solgun iki notası; 9.4'te üçüncü iz C15'e taşar | canlı | K3 | −32 · −26 | R16 |
| C14 | 0.0-10.0 | sörf çıkıntıya yakın | hava | K2 | −20 | E13 |
| C15 | 0.3 | beşik sıkılaşır: yumuşak kuru temas | temas | K2 | −28 | E03 |
| C15 | 0.8 · 1.9 · 3.0 | Oru zayıf ıslık, ışıklara oturur (düzenli, soluk) | canlı | K3 | −18 | R17 |
| C15 | 0.0-10.0 | Oru'nun yavaş nefesi | temas | K2 | −30 | E28 |
| C15 | 4.4 · 5.5 | ağırlık sağ yana: kitin; sol kaval plakası çıtırtısı | temas | K2 | −26 · −30 | E03 · E25 (çıtırtı) |
| C15 | 6.5-10.0 | köpük çizgisi yaklaşır: yalama büyür, 8.7'de ıslak tokat | hava | K2 | −30 → −22 | E20 |
| C15 | 8.0 | Khev başını köpüğe çevirir: boyun | temas | K2 | −30 | E03 |
| C15 | 9.2-10.0 | J: sörf yükselişi (C16'ya) | hava | K2 | −28 → −22 | E13 |
| C16 | 0.0-10.0 | sörf kükremesi sürekli yükselir | hava | K2 | −22 → −14 | E13 |
| C16 | 0.8-3.2 | anne tarama süpürmesi: nota yok, cevap yok; ardından 1 s yalnız yatak ve sörf | canlı | K3 | −16 | R18 · E33 |
| C16 | 0.0-2.0 | Khev duvarın tepesine bakar: boyun | temas | K2 | −32 | E03 |
| C16 | 2.2-3.6 | doğrulma çabası: ayak sürtmesi + gerilme nefesi | temas | K2 | −20 | E09 · E26 |
| C16 | 3.5 | sol bacak yük vermez: çatlak çıtırtısı | temas | K2 | −24 | E25 (çıtırtı) |
| C16 | 3.6 | acılı tek klik | canlı | K3 | −16 | R19 · E10 |
| C16 | 4.2 | çöküş: gövde kaya üstüne oturur (yumuşak iniş) | temas | K2 | −14 | E19 |
| C16 | 5.5-8.0 | dalga basıncı: rüzgâr kabarması; 6.1'de baş sağa döner | hava | K2 | −26 | E29 · E03 |
| C17 | 0.0-2.0 | sörf biraz iner (Khev'in alımı) | hava | K2 | −18 | E13 |
| C17 | 0.5-2.8 | baş kalkar, kollar sabit: plaka | temas | K2 | −30 | E03 |
| C17 | 3.3 · 4.6 · 5.9 | Oru TAM çağrı, ışıklara oturur; N3 7.6'ya dek, üç ışık yanıkken cam üst harmonikleri 6.2-7.4 | canlı | K3 | −8 | R20 |
| C17 | 3.0-7.6 | Khev sessiz (nefes tutuldu) | — | — | — | — |
| C17 | 7.6-10.0 | dinleme boşluğu: çağrı yok, müzik yok, sırt kabarır | hava | K2 | −16 → −13 | E13 |
| C17 | 8.2 · 9.0 | sprey patlamaları | hava | K2 | −22 | E15 |
| C17 | 8.4-10.0 | J: anne dikkati, tonsuz, yükselir | canlı | K3 | −30 → −20 | R21 · E34 |
| C18 | 0.0-1.2 | Oru çağrısının yankısı (C17'den) | canlı | K3 | −24 → −40 | R20 (L) |
| C18 | 0.0-3.0 | dikkat tonu gezinir (perde sürüklenir; boş terasa bakış) | canlı | K3 | −22 | R21 · E34 |
| C18 | 3.0-6.2 | ton daralır, göz bebeği durunca D'ye kilitlenir | canlı | K3 | −22 → −18 | R21 |
| C18 | 6.8 · 8.0 · 9.2 | anne SICAK cevap, ışıklara oturur; N3 C19 1.5'e taşar | canlı | K3 | −8 | R22 |
| C18 | 0.0-10.0 | sprey perdesi: yatay hışırtı; sörf altta sürer | hava | K2 | −32 · −16 | E30 · E13 |
| C18 | 9.6 | alt göz kapağı yumuşar: hafif ıslak iç çekiş | temas | K2 | −30 | E22 |
| C19 | 0.0-1.5 | anne N3 kuyruğu yüzgeç rezonansına çözülür | canlı | K3 | −14 | R22 (L) |
| C19 | 0.4-10.0 | yüzgeç rezonansı (D): 4-7 s'de zirve | temas | K2 | −26 → −14 | E21 |
| C19 | 0.5-1.5 | sörf −16 → −28 düzleşir; altında sakin yalama | hava | K2 | −28 | E20 (sakin) |
| C19 | 5.0-5.6 | yüzgeç çıkıntıyla aynı seviyeye oturur: membran gıcırtısı | temas | K2 | −22 | E22 |
| C19 | 7.0-10.0 | ufuk sırtı: çok uzak alçak uğultu (saat sürüyor) | hava | K2 | −30 → −26 | E13 (uzak) |
| C20 | 0.4-3.6 | Oru kanat çırpışı (sağlıklı ama sol geride) | temas | K2 | −24 | E17 |
| C20 | 3.8-5.6 | kısa süzülüş: çırpış yumuşar | temas | K2 | −26 | E17 |
| C20 | 5.8 | Oru yüzgece konar: ılık yüzeyde yumuşak "pat" | temas | K2 | −26 | E32 |
| C20 | 6.9 · 7.7 · 8.5 | Oru PARLAK çağrı (aralık 0.8), ışıklara oturur | canlı | K3 | −8 | R23 |
| C20 | 9.0 · 9.9 · C21 0.8 | anne alçak cevap (D2 G2 A2, hissedilen), Oru N3 üstüne örtüşür | canlı | K3 | −14 | R24 |
| C20 | 9.2 | Khev kalkmaya çalışıp kalkamaz: kısa nefes + çatlak çıtırtısı | canlı | K2 | −26 · −30 | E26 · E25 (çıtırtı) |
| C20 | 0.0-10.0 | yüzgeç rezonansı sürer | temas | K2 | −16 | E21 |
| C20 | 6.0-10.0 | ufuk sırtı çıkıntıya biraz yaklaşır | hava | K2 | −24 → −22 | E13 (uzak) |
| C21 | 0.35 | çaba kliği | canlı | K3 | −16 | R25 · E10 |
| C21 | 0.4-2.4 | taş sürtmesi yumuşak membrana döner; 2.6'da gövde yüzeye oturur | temas | K2 | −18 → −24 · −20 | E23 |
| C21 | 1.0-2.0 | sol bacak sürüklenirken çatlak çıtırtısı | temas | K2 | −28 | E25 (çıtırtı) |
| C21 | 0.0-10.0 | yüzgeç rezonansı (anne cevabının sıcaklığı) | temas | K2 | −16 | E21 |
| C21 | 3.8-7.0 | rahatlama nefesi (omuzlar nefesle kalkıp iner) | canlı | K2 | −24 | E26 |
| C21 | 3.5-7.0 | köpük çizgisi ilerler | hava | K2 | −30 → −24 | E20 |
| C21 | 7.2 · 8.9 | yüzgeç damarları sıcak ışıkla atar: iki yumuşak ton dalgası (düzensiz aralık) | temas | K2 | −24 | E31 |
| C21 | 8.0-10.0 | J: dalga baskısı yükselir (C22'ye) | hava | K2 | −28 → −18 | E24 (ön kükreme) |
| C22 | 0.0-3.0 | yüzgeç itişsiz yükselir: hava + membran | hava | K2 | −22 | E07 · E22 |
| C22 | 0.0-3.0 | kükreme −18 → −10 | hava | K2 | −18 → −10 | E24 (ön kükreme) |
| C22 | 3.1-3.35 | darbe öncesi 0.25 s çöküş (kükreme −8 dB) | hava | K2 | −8 dB | — |
| C22 | 3.4 | DALGA boş çıkıntıya çarpar: darbe + sub | hava | K2 | **0** | E24 |
| C22 | 3.4-7.0 | yayılan kükreme: −6 → −14 | hava | K2 | −6 → −14 | E24 |
| C22 | 6.6-10.0 | anne sabit alçak ton (D); Y2'ye akar | canlı | K3 | −14 | R26 · E06 |
| C22 | 7.0-10.0 | sprey dağılır; 8.0-10.0 su çekilir | hava | K2 | −14 → −28 · −24 | E15 · E20 |
| C22 | 8.0-10.0 | yükseliş rüzgârı | hava | K2 | −30 | E29 |
| C23 | 0.0-1.5 | sprey kuyruğu | hava | K2 | −28 → −40 | E15 (L) |
| C23 | 0.0-4.0 | uzaklaşan okyanus kalıntısı (aşağıda) | hava | K2 | −30 → −50 | E13 (uzak) |
| C23 | 0.0-10.0 | yüzgeç damar parıltısı, sis akışı | temas | K2 | −26 · −34 | E31 · E29 |
| C23 | 3.2 · 4.2 · 5.2 | Oru TAMAMLANMIŞ ifade (ılık, vibratosuz) | canlı | K3 | −18 | R27 |
| C23 | 3.6 | Oru'nun başı ön kola değer: kuru yumuşak temas | temas | K2 | −28 | E03 |
| C23 | 4.2 · 6.5-10.0 | Khev'in omuzları iner: uzun rahat nefes; sonra düzenli sakin nefes (filmde ilk düzenli) | canlı | K2 | −22 · −28 | E26 |
| C23 | 6.0-10.0 | Oru nefesi | temas | K2 | −34 | E28 |
| C23 | 9.0-10.0 | J: anne ön nefesi (C24'e) | canlı | K3 | −28 → −20 | E05 (kısa) |
| C24 | 0.0-10.0 | yüksek rüzgâr, geniş stereo; kıyı küçüldükçe açılır | hava | K2 | −34 → −28 | E29 |
| C24 | 0.0-3.0 | uzak sörf solar | hava | K2 | −40 → yok | E13 (uzak) |
| C24 | 1.0 · 3.0 · 5.0 | anne motifi tamam: yavaş üç nota, N3 9.0'a dek tutulur | canlı | K3 | −8 | R28 |
| C24 | 4.0 · 6.5 | yüzgeç hafif esner | temas | K2 | −30 | E22 |
| C24 | 6.0-7.2 | Oru'nun tek ince notası (A5), anne N3'ü üstünde: oktav kaynaşması | canlı | K3 | −22 | R29 |
| C24 | 8.8-9.8 | şafak kenarı bir kademe parlar: cam parıltısı | hava | K2 | −26 | E27 |
| C24 | 9.0-10.0 | doğal kuyruk; 9.85-10.0 kapanış tıkırtısını önleyen hızlı iniş | — | — | −40'a | — |

### 5b. Sörf saati (özet; satırlar yukarıda)

```
C01-C06   yatakta uzak okyanus (yok olarak sayılır)        C14  −20     C19  −28 (düz) ← kuralın kulaktaki yarısı
C07       −32 → −18 → −14 (tek geniş sırt)                  C15  −30 → −22 (köpük)   C20  −24 → −22 (uzak sırt)
C08       −24 (vuruşlar)                                    C16  −22 → −14           C21  −30 → −24, J: −28 → −18
C09       −26 → −18 · uzak sırt −26 → −22                   C17  −18 → −13           C22  −18 → −10 → 0 (3.4) → −6 → −14
C10       −22 → −14 → kopuş −5                              C18  −16                 C23  −30 → −50 (kalıntı)
C11 C12   −24                                               C13  −24 → −22           C24  −40 → yok
Sörf düzensizdir: vuruş aralıkları 6-14 s arasında değişir, hiçbir yerde periyodik darbe yok (tek istisna: yok).
Kurgu.py'de `ses` listesine 1 s `solma` ile parçalanmış segmentler olarak girer (ses/sorf_saat.wav, 150 s, döngüsüz; 30 s'lik beş üretim 3 s çapraz geçişle birleştirilir).
```

## 6. ORTAM YATAĞI (FILM.md §6'ya taşınır)

Mekân = ses mekânı. Kıyı (kemer, teras, geçit, alt çıkıntı, göğün altındaki göz planları) tek denizin ve tek rüzgârın altında olduğundan **tek yatak**tır; kemer altı, alt çıkıntıya yakın sörf ve yüzgeç rezonansı yatağın üstüne **K2 efekti** olarak biner (yatağı değiştirmez, kesmede "yeni oda" doğurmaz). İkinci yatak yalnız mekân gerçekten değişince: anne yüzgecinin üstü ve yukarısı.

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | KIYI: kemer · teras · geçit · alt çıkıntı · gök ve deniz (C05 C18 göz planları dahil) | C01-C22 (0.0-220.0) | `low steady night wind over black basalt and a vast slow ocean swell far away, soft irregular water wash on distant rocks, open air, no rhythm, no birds, no insects, no voices, no music, seamless loop` | −20 LUFS | `ses/yatak_kiyi.wav` |
| Y2 | YÜZGEÇ-HAVA: annenin yüzgecinin üstü, deniz sisinin üstü, bulut tepeleri | C22 7.0 - C24 (217.0-240.0) | `a very low warm living drone of an enormous organic body, soft membrane texture, thin high-altitude wind, faint ocean far below, slow irregular swells, no pulse, no heartbeat, no voices, no music, seamless loop` | −22 LUFS | `ses/yatak_yuzgec.wav` |

```
Y1  120 s'lik dikişsiz döngü ya da 220 s tek parça; rüzgârda ve uzak sörfte periyot yok. Stereo: iki kanal ilintisiz, sağ biraz ağır (deniz sağda). Mono toplamda ≤2 dB kayıp.
Y2  Perde D çevresinde (73-147 Hz); besteciyle tonalite onayı. Mono toplamda ≤2 dB kayıp.
Geçiş  Y1 → Y2: 217.0'da Y2 girer (1 s), Y1 219-220'de solar (1 s); 217-220 arası ikisi üst üste, çapraz geçiş C22 sonuna oturur. Dönüş yok.
       Sprey kuyruğu (K2, L 1.5 s) 221.5'e dek Y2 üstünde biter. Film sonu: Y2 son 1 s solar; çağrı ve müzik kuyruğu 239.85'e dek doğal.
timeline.json yataklar:
  {"dosya": "ses/yatak_kiyi.wav",    "baslangic": 0.0,   "bitis": 220.0, "kazanc_db": 0, "gecis": 1.0}
  {"dosya": "ses/yatak_yuzgec.wav",  "baslangic": 217.0, "bitis": 240.0, "kazanc_db": 0, "gecis": 1.0}
Yatak dosyaları −20 / −22 LUFS'ta hazırlanır; kazanç timeline'da değil dosyada. Dijital sıfır hiçbir yerde yok (Y1/Y2 örtüşmesi 217-220; ilk 1 s Y1 fade-in'i K2 göz kapağı gıcırtısı ve 1.2 adımı örter).
```

## 7. GEÇİŞ (FILM.md §6 taslağı · F8'de kurgucu kesinleştirir)

Ön karar (kurgucu F3): 23 kesmenin 23'ü `kesme`; sahip planı "düz kesmelerle 240 s" der ve her geçiş filmi süresi kadar kısaltır. Ses bunu kabul eder: süreklilik geçişle değil **köprüyle** sağlanır.

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz · L 1.2 s anne nefesi kuyruğu | XW → MC: ölçek sıçraması; yatak sürer (ILK_30 §5) |
| C02→C03 | kesme | Y1 · J 1.2 s gök basıncı (C02 8.8'den) | MC → XW; sessizlikten (dinleme) dev hareketine hazırlık |
| C03→C04 | kesme | Y1 · L 1.0 s yüzgeç havası; anne tonu 0.6 s taşar | kurgucu önerisi; yön tersi (Khev geri çekilir) sesle yumuşar |
| C04→C05 | kesme | Y1 · J 1.5 s dikkat şişmesi (C04 8.5'ten), ilk nota ışıkla | kurgucu önerisi; renk sıçraması (kemer gölgesi → amber göz) sesle köprülenir |
| C05→C06 | kesme | Y1 · L 0.8 s soğuk salon yankısı; açık hava genişlemesi | gövdenin açığa çıkışı kesmede; ses "kapalı salondan açık denize" |
| C06→C07 | kesme | Y1 · J 1.0 s su kükremesi (C06 9.0'dan) | aşırı benzer açı riski (B6): ses süreği taşır |
| C07→C08 | kesme | Y1 · L 1.5 s sırt kükremesi sörfe akar | açı büyük, ölçek aynı |
| C08→C09 | kesme (hareket üstü) | Y1 · adım sesi C08 7.6 → C09 0.6; kemer tonu C09 0.8-2.3 solar | Khev iki çekimde gölge çizgisinde: kesme hareketin üstüne |
| C09→C10 | kesme | Y1 · J 1.0 s taş gıcırtısı (C09 9.0'dan) | kurgucu önerisi; sebep-sonuç sesle bağlı |
| C10→C11 | kesme | Y1 · L 1.5 s su çarpması ve sprey kuyruğu | kurgucu önerisi; yolun kapanışı boş ellere akar |
| C11→C12 | kesme | Y1 · düşen ıslık 9.9'da kesilir, iniş sesi C12 0.15 | düşüş kesmede: ses öncesi-kesme-sonrası'nı bağlar |
| C12→C13 | kesme | Y1 · L 1.0 s Oru'nun zayıf çağrısı (C12 9.15) | kurgucu önerisi; Khev duyuyor, 0-2.5 s aşağı bakıyor |
| C13→C14 | kesme · **SERT SES KESMESİ (planlı)** | Y1 sürer · rüzgâr 9.75'te biter, 0.25 s yalnız yatak, iniş C14 0.0 | kurgucu önerisi; atlayış ve iniş kesmede, ses nedenle sonucu bağlar |
| C14→C15 | kesme | Y1 · L 0.8 s Khev nefesi ve Oru'nun solgun notası | jump-cut riski (B1): ses kesmeyi örter |
| C15→C16 | kesme | Y1 · J 0.8 s sörf yükselişi (C15 9.2'den) | saat sürüyor |
| C16→C17 | kesme | Y1 · bakış eşleşmesi; sörf C17 0.0-2.0'da −2 dB iner (Khev'in alımı) | sessizlik Oru'nun çağrısına yer açar |
| C17→C18 | kesme | Y1 · L 1.2 s Oru yankısı + J 1.6 s anne dikkati (C17 8.4'ten) | kurgucu önerisi (genişletildi): 9.2 s'lik aranma tonsuz dikkatle taşınır |
| C18→C19 | kesme | Y1 · L 1.5 s anne N3'ü yüzgeç rezonansına çözülür (aynı perde D) | cevap → köprü; ses "yüzgeç annenin sesidir" der |
| C19→C20 | kesme | Y1 · L 1.0 s yüzgeç rezonansı | B6 sınır kesmesi: ses sürekliliği taşır |
| C20→C21 | kesme | Y1 · anne cevabının 3. notası C21 0.8'e taşar | Oru'nun geçişi ve Khev'in geçişi iki ayrı bilgi, tek sesli cümle |
| C21→C22 | kesme | Y1 · J 2.0 s dalga baskısı (C21 8.0'dan) | kurgucu önerisi; saat |
| C22→C23 | kesme | Y1 → Y2 çapraz 217-220 · L 1.5 s sprey · anne sabit tonu sürer | tek yatak değişimi; kıyı geride kalır |
| C23→C24 | kesme | Y2 · J 1.0 s anne ön nefesi (C23 9.0'dan); rüzgâr geniş stereoya açılır | MC → XW kasıtlı ölçek sıçraması; ses genişleyerek taşır |

## 8. MÜZİK İÇİN SES KISITLARI (besteci planı bu bölüme göre revize edilir)

Besteci planı (`F4_besteci_1.md`) bu turda paralel yazılıyor; aşağıdaki sınırlar ona karşı sınanmadı. Mutlak saniye = 10 × (Cxx − 1) + saniye. Çağrı pencerelerinde müzik **−9 dB** altındadır ya da yoktur.

```
Replik yok; çağrı yokken müzik yatağı −16…−18 LUFS (kural 8), çağrı altında −9 dB (kural 6'nın karşılığı).

MÜZİKSİZ (zorunlu)
  0.0-22.0         C01 · C02 · C03'ün ilk 2 s: göz, ilk çağrı, tonsuz ses. Müzik 22.0'da çok alçak girer (ILK_30 §5; planın "sparse suspended tones").
  40.0-58.0        C05 · C06'nın ilk 8 s: soğuk çağrı, akrabalık anı, sıcak üst üste. Giriş 58.0'dan (çağrı bitti, anne yüzgeçlerini düzleştirirken), çok alçak şişme.
  97.0-98.6        C10 7.0-8.6: kırılma ve düşüş (hiçbir müzik vuruşu yok); 98.6'da tek alçak tutuş.
  126.8-154.0      C13 6.8 - C16 4.0: karar, atlayış, bedel, beşik. ~27 s. Sahibin planı: "karar, düşüş ve kitin çatlağı öne çıkar; müzik geri çekilebilir".
                   Müzik 154.0'da nabızsız, gergin dönüş (çöküş 154.2'den sonra).
  212.8-217.6      C22 2.8-7.6: dalga darbesi. Müzik yok: dalga müziktir. Dönüş 217.6'da anne tonu üstünde yumuşak.

ÇAĞRI PENCERELERİ (müzik ≤ −9 dB, tercih yok)
  51.8-57.0 (zaten müziksiz) · 75.0-77.4 C08 · 86.5-87.8 C09 · 100.8-107.0 C11 · 111.0-113.0 ve 119.0-120.0 C12 (en çok tek tutulan ton, ≤ −30 LUFS)
  162.8-168.0 C17 · 176.5-181.5 C18-C19 (178.0'dan sıcak dönüş) · 196.8-201.8 C20-C21 · 223.0-226.0 C23 · 230.8-239.0 C24 (müzik anne motifiyle birlikte söyler: çağrı üstte, harmoni altta)

MÜZİK ALANI (ses açısından serbest)
  22.0-40.0        C03 · C04 (korku ıslığı 36.5'te −9 dB)
  58.0-97.0        C06 sonu - C10 7.0'a dek; nabız 66.0'da başlar (C07 6.0: sırt "tek başına yürümeye" başlar, saat işler), anne durma bırakışı 64.2-66.0'da vuruş yok
  98.6-126.8       C10 sonu - C13 6.8; nabız 106.6'da (Oru kadraj dışına çıktığında) kırılır, C12'de yalnız tek tutulan ton
  154.0-212.8      C16 4.0'dan dalga öncesine; tırmanma C17-C18, sıcak dönüş 178.0, koruyucu uyum C19-C21
  217.6-240.0      C22 sonu - film sonu; C24'te çözülmüş son cümle, doğal kuyruk

ÇAĞRI PERDESİ  D5-G5-A5 / D3-G3-A3. Çağrı çekirdeği D-G-A (sus4 duygusu, çözülmemiş). Önerilen tonalite D; "tamamlanma" çağrının notasını DEĞİŞTİRMEZ,
               müziğin kadansı çağrının son notasını (A) tonik D'ye bağlar (C23 5.2 ve C24 5.0-9.0). Besteci başka tonalite seçerse çağrı kaydı ≤3 st kaydırılır.
BANT           Çağrı camsı: 600-4000 Hz. Anne: 140-900 Hz. Müziğin 600-4000 Hz orta bandı çağrı pencerelerinde çekilir (planın "generous space for creature calls").
               Müzikte düzenli nabız yalnız C07 6.0 - C11 6.6 aralığında olabilir (tehlike sahnesi); yatakta ve sörfte periyot olmadığı için nabız ayrı bir saat gibi duyulur.
```

**Ses → besteci referans noktaları (mutlak saniye):**

| Olay | Saniye |
|---|---|
| ilk ses: kapak gıcırtısı · Oru ıslıkları · anne nefesi | 0.0 · 4.6-7.2 · 7.4-9.2 |
| C02 çağrısı (ışıklara oturur) · basınç J | 13.2 / 14.6 / 16.0 · 18.8 |
| anne tek ton · başlık (kurgu, yazı) | 25.6-29.4 · 27-30 |
| korku ıslığı | 36.5 |
| C05 soğuk çağrı · küme · sub kayma | 40.9 / 42.5 / 44.1 · 45.0-47.0 · 47.2-49.6 |
| C06 iki çağrı üst üste · anne N3 biter · boşluk | 52.0-56.4 · 56.4 · 56.8-60.0 |
| anne durur (bırakış) · nabız başlar | 64.2-66.0 · 66.0 |
| Oru küçük çağrısı C08 · iki adım C09 | 75.2 · 82.0 / 85.0 |
| taş kırılması · ağır çarpma | 97.2 · 98.1 |
| C11 umut · çöküş · nabız kırılır | 101.0-102.0 · 103.3-106.6 · 106.6 |
| C12 zayıf çağrılar | 111.4 · 119.15 |
| karar kliği · itiş · iniş + çatlak | 126.6 · 128.0 · 130.0 |
| anne tarama · çöküş | 150.8-153.2 · 154.2 |
| Oru TAM çağrı · dinleme boşluğu | 163.3 / 164.6 / 165.9 · 167.6-170 |
| anne cevap (ışıkla) | 176.8 / 178.0 / 179.2 |
| yüzgeç oturur | 185.0 |
| Oru parlak · anne alçak cevap | 196.9 / 197.7 / 198.5 · 199.0 / 199.9 / 200.8 |
| dalga darbesi · anne sabit ton | 213.4 · 216.6 |
| Oru tamamlanmış ifade | 223.2 / 224.2 / 225.2 |
| anne motifi · Oru A5 · şafak | 231.0 / 233.0 / 235.0 · 236.0 · 238.8-239.8 |

## 9. FİNAL MİKS — YÜKSEKLİK HEDEFİ

```
HEDEF       −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumluluğu kontrol edilir.
YÖNTEM      1) taslağı kur (klipler sessiz + yataklar + `ses` parçaları + müzik)
            2) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4>                    (ölç)
            3) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4> --uygula -o final.mp4
            İki aşamalı, doğrusal: sıkıştırma yok; sessizlik ile darbe arasındaki fark ezilmez.
KISA VADE   Y1 −20 LUFS-S · Y2 −22 · Oru ve anne çağrı zirveleri ≈ −12 LUFS-S (yataktan ≥ +8 LU) · C22 dalga ≈ −8 LUFS-S · müzik çağrısız −16…−18, çağrı altında −9 dB.
ZİRVELER    C22 dalga (0) · C14 iniş (−6) · C10 kırılma (−6) ve çarpma (−5) · çağrı zirveleri (−8). −14'e çıkarken zirve tavana önce varırsa sıkıştırma EKLENMEZ;
            C22 / C14 / C10 efektleri kaynakta en çok 3 dB indirilir, çağrılar korunur.
DİKKAT      Film boyunca müzik yatağı integrated ölçümü taşır (C01-C03, C05-C06 ve C13-C16 müziksiz). Müziksiz bölümler yatak + efektle ~−22 LUFS-S'dir; ölçüm −15'in
            altında çıkarsa müzik yatağı +1…2 dB yükseltilir, sıkıştırma eklenmez. Sesi düşük teslim etmek en ölümcül hatadır: platform kısar, açmaz.
KORUNAN     C12 (≈ −26 LUFS-S, yalnız Oru'nun nefesi ve yatak) ile C22 darbesi (≈ −8 LUFS-S) arasındaki fark ve C19 sörf düşüşü (−16 → −28) ezilmez.
TELEFON     Düşük frekanslı her ses (anne, sörf, yüzgeç rezonansı, okyanus rezonansı) 300-2500 Hz'de ≥ −6 dB orta bant payı taşır; telefon hoparlöründe anne çağrısının
            C06 / C18 / C24'te duyulması şartı. Yatak −20 LUFS telefonda duyulmuyorsa +2 dB.
MONO        Y1 / Y2 ilintisiz stereo: mono toplamda ≤2 dB kayıp. Oru çağrıları merkez (±0.2, kadraj konumunu izler); anne gövde katmanı merkez, yalnız yankı geniş.
            Sörf ve kükreme sağ ağırlıklı (deniz sağda), kemer tonu sol, C07 sırtı sağdan sola yürür, C24 geniş.
SON KONTROL Final baştan sona kulaklıkta ve telefon hoparlöründe dinlenir. Oru'nun üç hâli (ince / zayıf / tam) ayırt edilmeli; anne SOĞUK (C05) ile SICAK (C06) farkı kulakla okunmalı.
```

## 10. DİNLEME ÖLÇÜLERİ (F8) VE AÇIK KARARLAR

1. **Akrabalık sesle okunuyor mu (C05 → C06):** F3'ün açık ÖLÜMCÜL'ü. F8 ANLATIM_TESTI sesli: "gökteki şey Oru'nun nesi?" Okunmazsa sırayla: C06'da anne +2 dB ve Oru −2 dB (kaynaşma), sonra C05'in soğuk hâli daha belirgin (−25 → −40 cent), son çare C06 çağrısının ikinci tekrarı (6.8-8.0 boşluğuna kısa üçüncü eşleşme).
2. **Işık-nota eşleşmesi (C02 C05 C17 C18 C20 C23):** ±0.1 s. Seçilen denemede ışık anları 24 fps kare kare okunur; ışık sırası soldan sağa değilse (model karıştırırsa) nota sırası ışığa uyarlanmaz, deneme değiştirilir.
3. **C13 → C14 sert kesme (0.25 s boşluk):** "kopuk" mu "nefes" mi? Kopuk duyulursa boşluk 0.1 s'ye iner; yumuşak duyulursa iniş 0.05 s öne alınır.
4. **C19 sörf düşüşü:** "kural" okunuyor mu (yüzgeç altındaki su neden sakin)? Okunmazsa düşüş 1.5 s'ye yayılır, sakin yalama +3 dB.
5. **C22 dalga:** tavan ve kırpma; −14 LUFS'a çıkarken (bkz. §9).
6. **Khev'in sesi:** klik + solungaç nefesi insan gibi duyuluyorsa (nefes) E26 daha kâğıtsı ve alçak yapılır; insan nefesi film boyu yok (plan: "insan bebek ağlaması ve anlaşılır konuşma yok").
7. **Telefon:** anne çağrısının C06 / C18 / C24'teki orta bandı (§3 TELEFON PAYI); duyulmuyorsa 2. harmonik +3 dB.
8. **C16 cevapsız tarama:** "cevapsız" mı yoksa "bitmeyen" mi duyuluyor? Bitmeyen duyulursa tarama bitişi 0.3 s daha keskin, sonra 1 s boşluk.

```
AÇIK KARARLAR (Fable'a)
1. Tonalite: çağrı çekirdeği D-G-A (önerilen tonalite D). Besteci planı gelince uyum; farklıysa çağrı kaydı ≤3 st kayar, karar Fable'ın.
2. C24'te Oru'nun tek ince notası (R29, oktav kaynaşması): planın "warm adult motif completes" cümlesine ek ses; olay eklemesi değil (görüntüde Oru yüzgeçte, ışıkları açık).
   Fable onaylamazsa satır düşer, hiçbir şey kaybolmaz. Sahip onayı gerekmez ama bilgi olarak PLANDAN SAPMA'ya eklenebilir.
3. Altyazı: FILM §5 "gerekmez", ILK_30 §4 otomatik altyazıdan kaçınmak ister (kurgucu açık soru 2). Ses etiketli altyazı dosyası istenirse bu planın çağrı adları etiket olur:
   [glassy three-note call] · [immense low breath] · [low resonance] · [wave impact]. Sahip kararı.
4. Y1 başlangıç fade-in'i: gecis 1.0 (varsayılan). İlk saniyenin sessiz kalması endişe yaratırsa Y1 gecis 0.5'e iner, K2 göz kapağı gıcırtısı aynı kalır.
5. Ses aracı: çağrılar perde tutan araç ister (§3 notu); yatak ve foley için Flow Mondo Sónico denenebilir (P12 ölçülmedi, ticari koşul BİLİNMİYOR) ya da lisanslı kütüphane. Araç sahibin.
```

## 11. PLANIN "Sound:" SATIRLARI → BU PLAN (eşleme)

| Çekim | Plan satırı (özet) | Bu planda | Değişiklik |
|:--:|---|---|---|
| C01 | üç camsı ıslık · devasa alçak cevap nefesi · orta frekans dokusu | §5 C01 4.6 R01 · 7.4 R02 · E01 gıcırtısı orta bantta | + kapak gıcırtısı (ilk ses) |
| C02 | ince üç nota · kitin tıkları · ölçülü kıyı rüzgârı | R03 · E03 · Y1 | — |
| C03 | geniş hava yer değiştirmesi · uzak okyanus rezonansı · bir derin harmonik ton | E07 · E08 · R04 | — |
| C04 | bir kuru ayak sürtmesi · korkmuş ıslık · devam eden uzak rezonans | E09 3.3 · R06 · R05 | — |
| C05 | aynı üç nota, geniş sıcak rezonanslı yetişkin tınısı | R07 SOĞUK | **"warm" → soğuk** (F2 ürün notu: S5 soğuk, S6 sıcak) |
| C06 | çağrılar üst üste, sonra okyanus ve rüzgâr için boşluk | R08 · 6.8-10 boşluk | — |
| C07 | büyüyen su kükremesi · basınç alçak harmonikleri · uzak taş takırtıları | E13 · E34 (alçak) · E14 | + annenin durma bırakışı |
| C08 | rüzgâr · uzak yaklaşan sörf · bir küçük çağrı | Y1 · E13 · R09 | + kemer tonu (kapalı) |
| C09 | iki ağır kuru ayak sesi · kitin sürtünmesi · yükselen uzak sörf | E02 · E03 · E13 | — |
| C10 | genişleyen taş gıcırtısı · keskin çatlama · ağır su çarpması | E16 | — |
| C11 | umutlu camsı cıvıltı → zayıf inen ıslık · kanat membranı | R11 · E17 | — |
| C12 | kırılgan çağrı · küçük membran hareketi · uzak ağır sörf | R12 · E32 · E13 | + ikinci çağrı 9.15 (L köprüsü için) |
| C13 | Khev'in gergin içe çekiş kliği · itiş sürtmesi · geçen rüzgâr | R14 · E09 · E18 | — |
| C14 | ağır iniş rezonansı · kuru kitin gıcırtısı · kısıtlı klik çığlığı | E19 · E25 · E03 · R15 | + plaka çatlağı |
| C15 | sessiz canlı nefesi · zayıf ıslık · kitine yumuşak temas | E28 · R17 · E03 | — |
| C16 | acılı kitin kliği · rüzgâr · sürekli artan sörf | R19 · E29 · E13 | + anne taraması (F2 önerisi) |
| C17 | sörf yatağı üstünde açıkta Oru çağrısı, sonra küçük dinleme boşluğu | R20 · E13 · 7.6-10 boşluk | — |
| C18 | geniş sıcak üç nota cevap, altta sörf sürer | R22 · E13 | + anne dikkat tonu (aranma) |
| C19 | derin sıcak organik rezonans · yumuşak membran gıcırtısı · yüzgeç altında su | E21 · E22 · E20 (sakin) | + sörf düşüşü (kural kulakta) |
| C20 | Oru'nun daha parlak üç notası, alçak anne rezonansı cevaplar | R23 · R24 | — |
| C21 | kısa çaba kliği · taştan membrana sürtme · sıcak anne rezonansı | R25 · E23 · E21 | — |
| C22 | tam bir su darbesi ve yayılan kükreme, sonra annenin sabit alçak tonu | E24 · R26 | + darbe öncesi 0.25 s çöküş |
| C23 | yumuşak tamamlanmış üç nota · sessiz biyolojik nefes · aşağıda solan okyanus | R27 · E26 · E28 · E13 (uzak) | — |
| C24 | sıcak yetişkin motifi tamamlanır, incelen rüzgâr ve uzak sörf, yumuşak doğal kuyruk | R28 · E29 · E13 (uzak) | + Oru'nun tek notası R29 (AÇIK KARAR 2) |

```
ÖZET     24/24 çekimde en az bir efekt satırı (sessiz çekim yok) · 29 kayıt satırı (replik yok; çağrı 25 + Khev 4) · 34 ses varlığı kodu · 2 yatak (Y1 Y2) · 23 geçiş (23 kesme)
         katman ≤4 her sahnede (K1 ortam · K2 efekt · K3 çağrı · K4 müzik) · model sesi: KAPALI · vakum: yok (açık atmosfer, ses taşır)
         planlı sert anlar: C13→C14 (0.25 s boşluk + iniş) · C10 7.0-8.6 müziksiz · C22 3.1-3.35 çöküş · film sonu
         F4 kontrol: F4.1 ortam ayrımı yazılı (vakum/iç hacim yok) ✅ · F4.2 kayıt listesi (sözsüz) ✅ · F4.5 her çekim efekt satırı + nereden ✅ · F4.4 model sesi kapalı ✅ ·
         F4.6 yatak + geçiş tabloları ✅ · F4.8 ilk 2 s insan sesi yok, C01 müziksiz, C01→C02 yatak sürer ✅ · F4.3 / F4.7 (müzik planı, MÜZİK PROMPTU) besteci dosyasında
GİRDİ    yatay_4_dk_filmler/MOONMOTHER/FILM.md §1-§5 (§4 çekim listesi saniye vuruşları, AÇILIŞ tablosu; §5 REPLİK yok)
         yatay_4_dk_filmler/MOONMOTHER/ODA/SAHIP_PLANI.md (ses ve müzik akışı, C01-C24 "Sound:" satırları)
         yatay_4_dk_filmler/MOONMOTHER/ODA/F3_kurgucu_1.md (soru 6 köprü önerileri; ön geçiş kararı; B1 B3 B6)
         yatay_4_dk_filmler/MOONMOTHER/ODA/F2_senarist_2.md (§3.3 üç ışık / üç nota tablosu; §5 F4'e ses önerileri) · ODA/F3_yonetmen_2.md · ODA/DURUM.md (AŞILAN KAPILAR, akrabalık ÖLÜMCÜL'ü)
         yatay_4_dk_filmler/MOONMOTHER/NOTLAR.md KARARLAR (model sesi KAPALI · REPLİK yok)
         uretim_hatti/REPLIK_VE_KLIP_SESI_KILAVUZU.md · GECIS_VE_SES_SUREKLILIGI.md · ILK_30_SANIYE_KILAVUZU.md §4-§5 · SECIM_VE_KURGU_KILAVUZU.md · FLOW_GERCEKLERI.md §4 §6 Ek 2
         uretim_hatti/araclar/kurgu.py (timeline şeması: ses · yataklar · solma) · yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_ses-tasarimcisi_2.md (biçim örneği)
YAPILMADI  kulakla dinleme ve gerçek take/ışık anı ölçümü (medya yok: 24 çekim ⬜; saniyeler FILM §4 vuruş planından ve planın Sound satırlarından) · kurgu.py kontrol / yukseklik
           koşulmadı (bu ajanda kabuk yok; taslak da yok) · film_dogrula koşulmadı · F4_besteci_1.md henüz yok (paralel yazılıyor; §8 ona karşı sınanmadı, çatışma Fable'a gider) ·
           ORU_CAGRI_v1 üretilmedi (araç perdeyi tutar mı bilinmiyor; §3 notundaki yedek yol) · C01-C03 ve çağrılı çekimlerde ışık-nota eşleşmesi seçilen denemede ölçülmedi (F8)
```
