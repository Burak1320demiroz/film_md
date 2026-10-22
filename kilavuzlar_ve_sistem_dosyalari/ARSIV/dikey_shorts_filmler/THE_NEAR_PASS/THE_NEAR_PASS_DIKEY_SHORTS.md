# 🌘 THE NEAR PASS — Yakın Geçiş

Dikey YouTube Shorts / Reels Production Document
Format: **9:16 (DİKEY)** | Sahne: 6 (Hook + 5 Ana Sahne) | Süre: Her sahne **10 saniye**, toplam **60 saniye**
Prompt yapısı: Her sahne için **1 görsel promptu + 2 video promptu** (A = T2V · B = I2V devam)
Kaynak: **özgün konsept** — kaynak film yok
Zaman ve yer: **Günümüzden uzak · ince atmosferli kayalık gezegen yüzeyi, gündüz** (promptlarda yer adı geçmez)
Tür: **Bilimkurgu / keşif — huşu** (aksiyon değil; `UZAY_SENARYO_KILAVUZU` §1 ince atmosfer kulvarı)
_"Gün burada batmaz — kapanır."_

---

## 🎯 BU SHORTS'UN TEK İŞİ

Kullanıcı talebi: **viral olacak, çok yakın uydusu olan bir gezegen.**
Bu dosya talebi küçültmüyor; **uyduyu modelin gerçekten çizebildiği tek
kanala** taşıyor. Depoda ölçülmüş gerçek şu: büyük, rijit, tek parça
gövdeler modelin en sağlam ürettiği nesnelerdir (THE QUIET IMPACT'in
gemi gövdeleri) — ama **serbest cismin hızlanması üretilmiyor**
[D127: THE IRON SLOPE, 25.08.2026]. O yüzden bu filmin uydusu
hızlanmıyor, **sabit hızda ve büyüyerek tırmanıyor**, ve ekranda
hareketi ölçen iki cetvel var: kendi eni, ve gökyüzüne çivilenmiş
yıldız.

```
KADIN                                 PALL (uydu)
──────────────────────────────        ──────────────────────────────
kemik rengi düzlükte duruyor          150 km yukarıda, saniyede 4.965 m
60 saniyede 8 metre yürüyor           60 saniyede gökyüzünde 23 derece
ellerinde hiçbir şey yok              ekranda 435 px'ten 325 px'e...
                                      hayır: 6,12°'den 12,48°'ye BÜYÜR
```

Filmin tek olayı bir tutulmadır — ama bu tutulma **yavaşça
kararmaz.** PALL yıldızdan 18 kat geniştir; gündüz **1,2 saniyede
kapanır**, **19,1 saniye** kapalı kalır, **0,94 saniyede** geri açılır.
Ve gölge düzlüğü **saniyede 5.351 metreyle** — bu havada Mach 23,7 —
süpürdüğü için **önünde hiçbir şey gelmez**: ne ses, ne rüzgâr, ne
uyarı. Kadın 19,1 saniyeliğine bastığı yeri göremez ve filmin tek
kararı budur.

**RİSK SAYIMI: 4 / 12** — Kart 3 (kask/vizör) · Kart 4 (ikinci figür,
her filmde) · Kart 5 (sayaç — **metinsiz/çevresel**) · Kart 9 (ışık
mıknatısı — kadranda TEK baskın ışık var).

> ⭐ **KART 6 (parçacık/toz/patlama) TETİKLENMİYOR — ve bu bir tasarım
> kararıdır:** toz bulutu 0 kare · duman 0 kare · alev 0 kare ·
> kıvılcım 0 kare · patlama 0 kare · düşen/uçuşan nesne 0 kare ·
> uydudan kopan enkaz 0 kare. Okra tozu düzlükte YATIYOR ve hiç
> kalkmıyor; kadın 8 metreyi ayağını sürümeden yürüyor. İlk taslakta
> PALL'ın kuyruğundan sızan ince bir toz filamenti vardı — **çıkarıldı**,
> çünkü depodaki en düşük tek skor parçacıktır (Low Power 2/10) ve
> ödülü zaten ikinci bir nesnenin taşıması gerekmiyordu: aynı ifşayı
> **çatlak ağı** taşıyor, ve çatlak rijit, sabit, yüksek kontrastlı bir
> yüzey detayıdır — modelin iyi ürettiği cinsten.
> Kart 1 (su — 0 kare), Kart 2 (canlı — 0 kare), Kart 6b (katmanlı
> dünya — tek düzlük, tek irtifa, tek ışık takvimi), Kart 7 (diyalog —
> 0 replik), Kart 10 (insansız sahne — 6/6 sahnede insan var) ve
> Kart 11 (değişken çekim süresi — 6 × 10,005 s sabit) konseptte yok.

> ⚠️ **DÜRÜST KAYIT — bu filmin bir numaralı riski kartlarda YOK:
> BÜYÜK GÖK CİSMİNİN EKRANDA HAREKET ETMESİ.** Bu, D127'nin aynısıdır,
> yalnızca nesne değişmiştir: THE IRON SLOPE'un paneli "her saniye
> +2,16 m/s" yazılı 12 promptun 12'sinde sabit ~0,15 m/s süzüldü ve
> film novum'suz çıktı. Buradaki karşı önlemler D127'nin çözüm
> maddelerinin birebir uygulamasıdır:
> ```
> ① SÜRE VE PİKSEL YAZ, AÇISAL HIZ YAZMA
>    ✅ "5. saniyede üst kenarı kadrajın tepesinden çıkar"
>    ✅ "10. saniyede alt kenarı, ayakta duran kadının boyu kadar yükselir"
>    ❌ "saniyede 0,22 derece tırmanır"   (ekranda görünmez)
> ② KENDİ ENİ CETVELDİR: her sahnede kendi eninin %34-55'i kadar yol
>    alır — altı sahnenin altısında, ve oran her sahnede BÜYÜR
> ③ İKİNCİ, SABİT CETVEL [D90]: yıldız kadrajda çivilidir. PALL'ın
>    ön kenarıyla arasındaki boşluk 236 → 159 → 67 → 0 piksel
> ④ İKİ HIZ AYNI KADRAJDA [D127③]: PALL ağır ağır tırmanır, ışık
>    1,2 SANİYEDE kapanır. Modelden ivme istenmiyor; FARKLI İKİ HIZ
>    isteniyor ve model bunu üretiyor
> ⑤ KABUL KRİTERİ, S0 KAPISINDA, MAKİNEYLE [D125]:
>    ffmpeg -i S0.mp4 -vf "select='eq(n\,0)+eq(n\,239)'" -vsync 0 k_%02d.png
>    iki karede PALL'ın alt kenarı ≥100 px (tasarım 132 px) farklı DEĞİLSE
>    ⛔ ÜRETİM DURUR. Negatif blok bu işi yapmaz [D59].
> ```
> **İkinci beklenen bozulma: modelin tutulmayı BULUT GÖLGESİ sanması** —
> yumuşak kenarlı, kadrajı yandan süpüren, renk kayması olan bir
> karartma. Fizik bunun tam tersini söylüyor: umbra düzlüğü saniyede
> 5,4 km'yle geçer, yani kenar 24 karede 220 metre yol alır — ekranda
> süpüren bir kenar YOKTUR, yalnız **seviye düşer**. Promptta pozitif
> yazılı: *"every edge in the frame stays exactly where it is; nothing
> moves and nothing sweeps across the ground; only the light level goes
> down."*
> **Üçüncü: taç/elmas yüzük/lens parlaması.** Burada fiziksel olarak
> imkânsız — PALL yıldızdan 18 kat geniştir, taç tamamen örtülür.
> Pozitif cümleyle kapatıldı: *"the rock's edge against the sky is a
> plain hard edge."*
> **Üretim S0'dan başlar**; PALL orada tırmanmıyorsa film üretilmez
> [D74 · IRON SLOPE emsali].

---

## ⏸️ BİLİNÇLİ SAPMALAR — sistem promptunun DNA'sından

`SHORTS_SISTEM_PROMPTU.md` §2 ve §3'ten dört madde bilerek esnetiliyor.
Emsaller: THE QUIET IMPACT (06.08.2026) · THE IRON SLOPE (24.08.2026).

```
DNA 3 — "Fiziksel imkansızlık = kanca"
SAPMA:  Bu filmde imkansızlık YOK. Novum ALGISAL: göz "gündüz yavaş
        biter" diye okur, ekranda 1,2 saniyede kapanan bir gündüz
        görür. Ekrandaki her sayı gerçek yörünge mekaniğidir ve
        §DÜNYA'da hesabıyla yazılıdır. Seride novumu tamamen gerçek
        fizik olan ÜÇÜNCÜ film (QUIET IMPACT · IRON SLOPE).

DNA 5 — "Huşu, korku değil. Tehlike yoktur."
SAPMA:  Tehlike VAR ama KÜÇÜK ve tamamen fizikseldir: ayaklarının
        dibinde 30 metre derinliğinde bir gerilme yarığı, ve 19,1
        saniye boyunca onu göremiyor. Panik 0 · koşu 0 · jump scare 0
        · temas 0 kare. Baskın valans HUŞU'dur; kaygı yalnız S4'ün
        3,0. saniyesinde, tek jestte yaşar.

LENS  — sistem promptu "32mm Cooke anamorphic" der. Bu filmde
        **24mm + 75mm, ikisi de KÜRESEL.** Sebep zevk değil GEOMETRİ:
        PALL 14,8°'den 37,9°'ye tırmanıyor ve 12,5° enine ulaşıyor;
        32mm'in 58,7°'lik dikey görüş alanı, figürü y=1436'nın üstünde
        tutarken bu yüksekliği kadraja ALAMIYOR (hesap §GÜVENLİ ALAN
        HARİTASI'nda). 24mm'in 73,7°'si alıyor. Anamorfik ve yatay
        parlama YASAK: hava 9 kPa, saçılma yok, pus yok — her parlama
        bir üretim artefaktıdır.

BİLEK EKRANI — sistem promptu "veriler bilek ekranından" der. Bu
        filmde HİÇBİR ekran yok [Kart 5]: üç sayacın üçü de fiziksel
        ve metinsizdir. Eller 6/6 boştur; tek ekipman jesti kaskın
        KENDİ lamba düğmesidir (elde tutulan bir alet değil).
```

---

## ⚠️ Genel Prodüksiyon Kuralları

1. **SIFIR KESME** — Her video **10 saniyelik**, kesintisiz tek çekim;
   her sahne AYRI üretilir [Ders 1]. `single continuous shot, 0 cuts`
   6 videonun 6'sında, her beat zaman damgalı.
2. **⛔ IZGARA ARAÇTAN YAZILIR [DERS 124]** — Bu dosyanın bütün zaman
   damgaları **ölçülmüş** bir klip süresine oturur:
   ```
   KLİP SÜRESİ = 10,005 s
   Kaynak: THE IRON SLOPE master ölçümü, 25.08.2026
           (6 kaynak klibin 6'sı da 10,005 s)
   sahne_başlangıcı(n) = (n − 1) × 10,005        [D115 formülü]
   toplam = 6 × 10,005 = 60,03 s · başlık kartı 0,0 s · kırpma 0,0 s
   ⛔ ÜRETİMDEN ÖNCE YENİDEN ÖLÇÜLÜR:
      ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
      Çıkan sayı 10,005 değilse bu dosyanın bütün zaman damgaları
      o sayıyla yeniden yazılır. 8 saniyelik ızgara 10 saniyelik
      araçta YAZILMAZ.
   NOT: Beatler 10,000 s ızgarasına yazıldı; altı klipte biriken
      fark 0,03 s'dir ve kurgu kapısının ±0,5 s toleransının içindedir.
   ```
3. **DİKEY SADAKAT (9:16) + GÜVENLİ ALAN** — Kadının hiçbir parçası
   `y=1436`'nın altına inmez. Bkz. **📱 GÜVENLİ ALAN HARİTASI**.
4. **İKİ LENS KİLİDİ — İKİSİ DE KÜRESEL** — Geniş/ölçek: **24mm**
   (S1, S2, S3, S4, S5). Sıkıştırma/kütle: **75mm** (yalnız S0).
   Anamorfik, yatay parlama ve zoom YASAK. Kamera yüksekliği ve
   mesafesi her promptta **metre** ile yazılır.
5. **⛔ KAMERA 6/6 TAM SABİT** — Üç kurulumun üçü de yere/kayaya
   oturtulmuş sabit kameradır; filmde tek kamera hareketi yoktur.
   Ölçek değişimi kameradan değil **Z ekseninden** gelir (S2'de kadın
   merceğe doğru 8 metre yürür) ve gökyüzündeki değişim tamamen
   PALL'ın kendi hareketidir.
6. **RENK DİLİ** — **Kükürt-kemik düzlük + demir okrası toz + kurşun-
   yeşil grafit kaya + sert beyaz-altın yıldız ışığı + BAKIR-BRONZ
   gezegen ışığı (kadranın tek doygun değeri, ve TAM 19,1 saniye
   yaşıyor) + derin çivit tutulma göğü.** Aksan: kadının dikişlerindeki
   **tozlu turkuaz** — kadrandaki tek soğuk doygun nokta, ve TAM 1 tane
   [D20 klon karşı önlemi].

   > ⚠️ **Palet çakışma denetimi — dürüst kayıt.** Soluk kayalık düzlük
   > + tek sert ışık + jilet gölge ailesi THE WRONG SHADOW (kireçtaşı
   > platosu) ile aynıdır; kaçınılmaz, çünkü ince atmosfer + küçük
   > yıldız bu görüntüyü zorunlu kılıyor. Ayırt eden iki karar:
   > **(a)** WRONG SHADOW'da hiçbir renk olayı yoktu — kadran baştan
   > sona aynı ışıktaydı. Burada filmin ortasında kadranın TAMAMI
   > sönüyor ve yerine **bakır** geliyor; bu, depodaki hiçbir dikey
   > filmde olmayan tek-olaylı palet kırılmasıdır.
   > **(b)** THE LOW MOON'un beyaz tuz düzlüğüne karşı buranın zemini
   > **kükürt-kemik** (sarımsı) ve **okra çizgili**; ikisi 120 px'te
   > birbirine karışmıyor.

7. **KARAKTER SADAKATİ** — 6 görsel promptun **6'sında da** aynı
   karakter bloğu birebir, kısaltmasız tekrarlanır [Ders 45]. Kask
   6/6 kapalı; vizör **optik olarak berrak**, sırt silueti **DÜZ** —
   ikisi de her promptun gövdesinde pozitif cümleyle [Ders 79].
8. **VİRAL ZAMANLAMA (Hook · 10 s ızgarasında)** — 0-2,5 sn merak
   (düzlükte duran kadın, üstünde büyük düz gri bir kütle — bulut ya da
   uçurum sanılır) → 2,5-6 sn ipuçları (kütlenin bir ALT KENARI var,
   kavisli, güneşli; üstünde oluklar) → 6-8,5 sn tam reveal (kütle
   TIRMANIYOR; 4,8. saniyede üst kenarı kadrajın tepesinden çıkar) →
   8,5-10 sn tek güçlü görüntü (alt kenar, kadının boyu kadar yükselmiş
   ve hâlâ yükseliyor).
9. **İKİ VİDEO PROMPTU — DEVAM KARESİ ZORUNLU** — Her sahnenin **A
   (T2V)** ve **B (I2V devam)** sürümü vardır. B, bir önceki sahnenin
   SON KARESİNDEN başlar ve karakteri/ortamı yeniden tarif ETMEZ.
10. **ELLER 6/6 BOŞ** — Alet yok, ölçüm cihazı yok, telefon yok, ekran
    yok. Tek ekipman jesti kaskın sol yanındaki lamba düğmesidir
    (S3'te açılır, S4'te kapanır) ve filmin merkezi seçimi odur.
11. **⛔ EKRANDA METİN SÜRESİ = 0,0 SANİYE [Ders 61]** — Suit'te yama,
    bayrak, harf, rakam yok; kaskta işaret yok; düzlükte insan yapımı
    tek nesne yok. Metin yasağı prompt cümlesiyle değil **KONSEPTLE**
    kapatılmıştır: kadrajda yazı üretebilecek tek bir nesne yoktur.
12. **⛔ AĞIR ÇEKİM YOK [D12 · D44]** — Işığın kapanması (1,2 s) ve
    açılması (0,94 s) modeli slow-motion'a çeken iki andır. İkisi de
    her promptta SANİYEYLE yazılır ve `everything moves at normal
    speed, no slow motion, no speed ramp` satırı **6 görsel + 6 video
    promptunun hepsinde** vardır.
13. **⛔ SES OLAYI 0** — Gölge Mach 23,7'yle gelir: önünde hiçbir şey
    gelmez. Işık kapandığında **ses hiç değişmez** — dışarıda 9 kPa'da
    zaten duyulacak bir şey yoktur, içeride nefes ve fan sürer.
    Bu filmin en rahatsız edici kararı budur ve tamamen doğrudur.
14. **YÖNELİM KİLİDİ [UZAMSAL §5.1]** — Yıldız ve PALL her kadrajda
    **BATIDA**, yani kadrajın sol yarısında ya da ortasındadır; asla
    sağ 242 px şeridinde değil. Kadın hep batıya bakar. Yarık çizgisi
    her kadrajda **doğu-batı**, yani ekranda YATAY uzanır.

---

## 🧬 VİRAL MEKANİK — "ANAHTARLI GÜNDÜZ"

```
Bu shorts'un imkansızlığı bir canavar ya da büyü değil, İZLEYİCİNİN
ŞEMASINA aykırı çalışan GERÇEK YÖRÜNGE MEKANİĞİDİR: bir uydu yeterince
alçak ve yeterince büyükse, gündüz SÖNMEZ — KAPANIR.

KURALLARI (üç sahnede kurulur, iki sahnede kanıtlanır):
 · PALL BATIDAN DOĞAR. Eşzamanlı yörüngenin çok altında olduğu için
   gezegeni geçer; ufuktan ufuğa 8 dakika 5 saniye, günde 19 kez.
 · PALL YAKLAŞTIKÇA BÜYÜR. Ufukta 2,63°, tepede 19,67° — dört kat.
   Filmin penceresinde 6,12°'den 12,48°'ye: iki katına çıkar.
 · PALL DÜZGÜN TIRMANIR. Hızlanmaz, yavaşlamaz, salınmaz: her 10
   saniyede kendi eninin %34-55'i kadar yol alır ve bu oran her
   sahnede büyür (çünkü yaklaşıyor, ivmelendiği için değil).
 · IŞIK ANAHTARLIDIR. PALL yıldızdan 18 kat geniştir; yıldızın diski
   1,2 saniyede tamamen örtülür ve 19,1 saniye sonra 0,94 saniyede
   geri açılır. Asimetri gerçektir: PALL uzaklaşıyor.
 · GÖLGE HABER VERMEZ. Umbra düzlüğü saniyede 5.351 metreyle geçer —
   bu havada Mach 23,7. Sesten 24 kat hızlı gelen bir şeyin önünde
   hiçbir şey gelmez: ne uğultu, ne rüzgâr, ne yaklaşan bir çizgi.
   Kadraj tamamen sabit kalır ve YALNIZ SEVİYE DÜŞER.
 · KARANLIK YEREL DEĞİL, TOPLAMDIR. Umbra bandı 50,6 km geniş;
   kadının 1,7 metreden gördüğü ufuk 3,8 km. Yani görebildiği dünyanın
   TAMAMI kapanır — kenarını göremez.

İzleyicinin gözü ilk 2,5 saniyede "bulut" ya da "uçurum" der. 5.
saniyede kütlenin üst kenarı kadrajdan çıkar ve izleyici düzeltir: bu
bir kaya, ve HAREKET EDİYOR. O andan sonra geriye tek soru kalır:
yıldıza değdiğinde ne olacak?

Serinin önceki mekaniklerinden ayrı: süreksizlik değil (Winter Line),
eksik neden değil (Wrong Shadow), ölçek-hız uyuşmazlığı değil (Quiet
Impact), eksik serbestlik derecesi değil (Straight Line), yön tersinmesi
değil (Iron Slope). Buradaki mekanik GEÇİŞ SÜRESİ UYUŞMAZLIĞI:
gezegen ölçeğinde bir olayın insan refleksinden hızlı olması.
```

### Farklılaşma denetimi — depodaki üç akrabası

| Film | Ortak yüzey | Bu film neyi başka yapıyor |
|---|---|---|
| **THE LOW MOON** (dikey, 05.08) | "alçak uydu" fikri | Orada yörünge İNSAN ÖLÇEĞİNDE bir kurguydu: 6 m yarıçaplı çemberde 2 metrelik bir taş. Burada yörünge GERÇEK: 4.350 km, 5.504 saniye, 4.965 m/s — ve nesne bir dağ sırası büyüklüğünde. Low Moon'un sorusu "bu taş neden düşmüyor?", buranınki "bu şey neden bu kadar yakın?" |
| **THE WRONG SHADOW** (dikey, 06.08) | soluk plato + gölge fiziği | Orada NEDEN eksikti (kaynağı görünmeyen ikinci gölge). Burada neden kadranın ortasında duruyor ve ekranın üçte birini kaplıyor. Wrong Shadow gölgenin AÇISINI sayar; bu film gölgenin YOKLUĞUNU tek olayda getirir |
| **THE HALF SKY** (dikey, 05.08) | "gökyüzünde büyük şey" | Orada yukarı bakınca HİÇBİR ŞEY vardı (ışığı geri vermeyen bölge). Burada yukarı bakınca çok şey var — ve 19,1 saniyeliğine yalnız o var |

### Mekaniğin insani karşılığı

```
Kadın gezegen fotometristi — ışık ölçen biri. Aletleri düzlüğe gömülü
ve onlar bu geçişi zaten kaydedecek. Dışarıda YAYA olmasının tek
sebebi, aletlerin kaydedemediği şeydir: bunun neye BENZEDİĞİ.

Filmin ironisi şu: karanlıkta PALL'ı görebilmesi için kask lambasını
söndürmesi gerekir — ve lamba, ayaklarının dibindeki 30 metrelik
yarığın kenarını gösteren tek şeydir. Yakın olanı görmeyi bırakmadan
uzak olanı göremez. S4'ün 3,0. saniyesinde başparmağı düğmeye gider.
Bedel aynı karede: ışık dairesi söner, yarık çizgisi onunla birlikte
kaybolur, ve botları oldukları yerde kalır — 19,1 saniye boyunca
kendi bastığı yeri bilmeden.

Ve ödül geçicidir: bakır ışık 19,1 saniye yaşar. 57,31. saniyede
gündüz geri açılır, çatlak ağı soluk bir lekeye döner, PALL yeniden
düz gri olur. Bu dünya yukarıdaki şey hakkında gerçeği yalnız
kapalıyken söylüyor.
```

---

## 📖 Sabit Referanslar (Bibles)

### 👤 Character Bible

**Kimlik (yalnızca bu dosyada):** NEHİR ALP, 34, gezegen fotometristi.
Bu geçişi altı aydır aletlerin kaydından okuyor; ilk kez dışarıda,
yaya ve tek başına izliyor.

> ⚠️ **ÜRETİM UYARISI [Ders 34 / 45]:** Karakterin adı **hiçbir promptta
> yazılmaz.** Milliyet ifadesi kullanılmaz. Gerçek kurum, ülke, marka,
> bayrak hiçbir promptta geçmez. Köşeli parantez etiketi yasak.

**Tam tarif — 6 GÖRSEL promptun 6'sında da birebir, kısaltmasız tekrarlanır:**

```
A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small unlit lamp housing is moulded into the left side of the helmet ring. The suit carries no patch, no flag, no lettering, no digits and no symbol anywhere. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon.
```

**Hareket imzası (konsepte özgü):** Ölçüm alışkanlıkları, korku
refleksleri değil. Uzun uzun **durur**; ağırlığı topuklarında. Bir
ayağını ilerletmeden önce kabuğu **bir kez burnuyla tıklatır** —
çatlamış bir düzlükte çalışan birinin mesleki alışkanlığı. Çenesini
kaldırmaz, **başını arkaya yatırır.** Sağ eldiveni kaskın alnına
gidip gölge yapar — filmin ilk ve son jesti budur.

**⚠️ TURKUAZ KİLİDİ [sayısal · D58 · Kart 4]:** Filmde **TAM BİR insan
ve TAM BİR turkuaz dikiş takımı** vardır. Kadranda başka hiçbir insan
biçimi, yansıma, silüet ya da soğuk doygun renk yoktur; düzlük kükürt-
kemik, kaya kurşun-yeşil, suit mat kurşun grisidir. Diz/önkol/bot
burnundaki okra aşınma her sahnede aynı yerdedir [D42].

### 🌍 World Bible — SERRA ve PALL

> Promptlarda **hiçbir isim geçmez**; bu blok yalnızca dosya içi
> tutarlılık içindir. Aşağıdaki her sayı türetilmiştir ve
> §FİZİK DEFTERİ'nde hesabı vardır.

```
GEZEGEN (SERRA)
  yarıçap            4.200 km
  yüzey çekimi       0,62 g  =  6,08 m/s²
  dönme periyodu     31,0 saat
  atmosfer           ince CO₂–N₂, yüzeyde 9 kPa, 210 K
                     → ses hızı 226 m/s · saçılma yok · pus yok ·
                       gökyüzü gündüz bile koyu · gölgeler jilet keskin
  yüzey              kükürt-kemik rengi anhidrit kabuk, üstünde ince
                     demir okrası toz. Kabuk DOĞU-BATI uzanan düz
                     gerilme yarıklarıyla taranmış: 3-5 m genişlik,
                     20-40 m derinlik, kilometrelerce düz.
  yarıkların sebebi  günde 19 kez, her seferinde 19,1 saniyeliğine
                     kapanan gündüz. Termal şok kabuğu düz hatlarda
                     çatlatır. ⭐ Bu dünyanın JEOLOJİSİ NOVUM'UN
                     KENDİSİDİR — zemin, gökyüzünün imzasını taşıyor.
                     (İkincil katkı: PALL'ın kaldırdığı katı kaya
                     gelgiti, 48 dakikada bir ~17 cm.)
  ufuk               1,7 m göz yüksekliğinden 3,8 km

UYDU (PALL)
  şekil ve boyut     düzensiz TEK PARÇA kaya: 60 × 50 × 44 km
                     (ortalama çap 52 km) · yoğunluk 3.300 kg/m³
                     · uzun ekseni gezegene DÖNÜK (gelgit kilitli)
  yörünge yarıçapı   4.350 km  →  yüzeyden irtifa 150 km
  periyot            5.504 s  =  1 saat 31 dakika 44 saniye
  yörünge hızı       4.965 m/s · zemine göre 4.729 m/s
  doğuş yönü         BATI. Eşzamanlı yörüngenin altında olduğu için
                     gezegeni geçer: batıdan doğar, doğudan batar.
  ufuktan ufuğa      8 dakika 5 saniye · günde 19,3 doğuş
  görünen çap        ufukta 2,63°  ·  başucunda 19,67°
                     (başucunda Dünya'nın Ay'ından 37,8 KAT geniş)
  yüzeyi             çıplak, kırık kaya. REGOLİT YOK: gelgit farkı
                     (0,0678 m/s²) kendi çekiminden (0,0240 m/s²) 2,8
                     kat büyük — gevşek tanecik yüzeyde durmuyor.
                     Uzun paralel oluklar ve derin bir çatlak ağı.
  neden dağılmıyor   Roche sınırının (rijit: 6.150 km) İÇİNDE. Kendi
                     çekimi değil KAYA DAYANIMI tutuyor: gelgit
                     gerilmesi 5,81 MPa, bazaltın çekme dayanımının
                     (~10-30 MPa) hemen altında. Emsal gerçek:
                     Mars'ın Phobos'u da fluid Roche sınırının içinde
                     ve olukları bu yüzden var.
```

### ☀️ Lighting Bible — TEK YILDIZ, İKİ DURUM

```
YILDIZ
  görünen çap        0,55° (Dünya'dan Güneş'ten biraz büyük)
  bu geçişteki yeri  BATIDA, 29,7° yükseklikte, filmin 60 saniyesi
                     boyunca KIMILDAMAZ (gökyüzü 31 saatte döner:
                     60 saniyede 0,175° — ekranda 5 piksel)
  rengi              sert beyaz-altın
  gölgeler           jilet keskin, dolgusuz, MUTLAK siyah.
                     İnce hava saçılmıyor: gölgenin içinde hiçbir şey
                     görünmez. Kadının gölgesi düzlükte 2,98 m uzunda
                     ve filmin sonunda AYNI uzunlukta.

⭐ IŞIK TAKVİMİ — filmde TAM İKİ GEÇİŞ VAR [Kart 6b'nin karşıtı:
   katman yok, ama takvim yine de yazılı]

   00,00 - 36,09 s   TAM GÜNDÜZ. Seviye sabit. Gölgeler jilet.
   36,09 - 37,30 s   KAPANMA — 1,21 saniye. Seviye her yerde AYNI ANDA
                     düşer. Gölgeler kısalmaz, süpürülmez, yumuşamaz:
                     kontrast biter ve gölge diye bir şey kalmaz.
                     ⛔ Kadrajda hiçbir kenar yer değiştirmez.
   37,30 - 56,37 s   TAM TUTULMA — 19,07 saniye.
                     · gökyüzü: derin çivit, ufuk çevresinde ince
                       bronz bir kuşak (50 km ötedeki gündüzden gelen
                       kaçak ışık) — yıldız alanı YOK, 19 saniyede göz
                       karanlığa uyum sağlamaz
                     · düzlük: sönük, düz, renksiz
                     · PALL: BAKIR-BRONZ parlar. Işığı gezegenin
                       kendisinden alır ve o ışık yalnız gölge
                       bandının DIŞINDAKİ gündüzden gelir → disk
                       KENARINDA parlak, ORTASINDA koyu. Şiddet:
                       gündüzün ~%4'ü.
                     · taç yok, elmas yüzük yok, halka yok:
                       PALL yıldızdan 18 kat geniş, taç tamamen örtülü
   56,37 - 57,31 s   AÇILMA — 0,94 saniye. Kapanmadan YAVAŞ, çünkü
                     PALL uzaklaşıyor ve arka kenarı daha yavaş sıyırıyor.
   57,31 - 60,00 s   TAM GÜNDÜZ. Gölgeler tam olarak eski uzunluğunda
                     geri gelir. Bakır gider; PALL düz gri olur.

KASK LAMBASI (filmin tek yapay ışığı, ve tek ekipman jesti)
   38,60 - 43,00 s   AÇIK. Kabukta yaklaşık 2 metrelik sert beyaz bir
                     DAİRE. ⛔ HAVADA HÜZME YOK — 9 kPa'da saçılacak
                     hava yok; ışık yalnız yere düştüğü yerde var.
                     Zeminden seken ışık çenesini ve vizörün alt
                     kenarını aydınlatır.
   43,00 - 60,00 s   KAPALI. Bir karede söner.
```

### 🎥 Camera Bible

```
ÜÇ KURULUM, ALTI ÇEKİM, SIFIR HAREKET.
Üçü de yere/kayaya oturur. Hiçbir çekimde pan, tilt, dolly, zoom,
elde çekim ya da sarsıntı yoktur.

A  24mm küresel · lens yerden 0,90 m · kadının DOĞU-GÜNEYDOĞUSUNDA
   20 m (S1) / 24 m (S3, S5) · batıya ve yukarı bakar
   → geniş: düzlük + ufuk çizgisi + küçük figür + PALL + yıldız
B  24mm küresel · lens yerden 0,25 m (kabuğun üstüne yatırılmış) ·
   kadının GÜNEYİNDE 22 m · kuzeybatıya ve yukarı bakar
   → gökyüzü baskın: figür kadrajın alt bandında, PALL büyük ve solda
C  75mm küresel · lens yerden 0,90 m · kadının GÜNEYDOĞUSUNDA 45 m ·
   kuzeybatıya bakar
   → sıkıştırma: PALL'ın kütlesi kadrajın üstünü doldurur ve TAŞAR

AZİMUT FARKLARI (ACI_YAYI §4: ≥45°)
   A ↔ B  ≈ 68°  ✅      A ↔ C  ≈ 45°  ✅      B ↔ C  ≈ 45°  ✅
PALL ve yıldız her kurulumda BATIDA, yani kadrajın sol yarısında ya da
ortasında — sağ 242 px şeridine hiçbir sahnede girmiyor ✅
```

> ⛔ **PUSULA BU BLOKTA KALIR — PROMPTA GEÇMEZ [UZAMSAL §6.1].**
> Yukarıdaki doğu/batı/kuzey/güney sözcükleri **yalnızca bu dosyada,
> insan için** vardır: üç kameranın birbirine göre gerçekten nerede
> durduğunu tarif ederler. **Promptların 18'inin 18'inde aynı bilgi
> EKRAN UZAYINA çevrilmiştir** — "frame left", "frame centre-left",
> "left to right across the frame", "beyond the left edge of the
> frame". Sebep ölçülmüş: `prompt_kontrol.py` ilk koşuda bu dosyaya
> **BLOCK** verdi ve gerekçesi tek cümleydi — *model pusula bilmez;
> "22 metres south of the woman" cümlesi her üretimde yazı-turadır.*
> Aynı sebeple hiçbir promptta çapasız `toward` yoktur: hedefin ekran
> dilimi her zaman AYNI cümlededir.

### 🚫 Negative Bible

> ⚠️ **D123 uygulaması:** Bu filmde şiddet, temas, yara, kalabalık
> YOKTUR ve negatif blok bu kavramları prompta SOKMAZ. Yasak yerine
> **malzeme tarif edilir**; negatif blok yalnız üretim artefaktlarını
> ve sayısal kilitleri korur.

```
Sabit taban (6 görsel promptun 6'sında):
  exactly one human being · no second figure · no duplicate ·
  no human reflection · no mirrors ·
  no visible beam of light in the air · no volumetric shafts ·
  no lens flare · no bloom · no glow filter · no halo ·
  no ring of light around the rock · no corona · no diamond ring ·
  no cloud · no haze · no mist · no fog · no atmospheric scattering ·
  no dust cloud · no blowing dust · no smoke · no fire · no sparks ·
  no debris · no falling objects · no meteor · no trail · no comet tail ·
  no ring system · no second moon · no star field · no aurora ·
  no perfectly spherical moon · no smooth moon · no cratered-sphere look ·
  no miniature look · no CGI look · no waxy skin · no airbrushed skin ·
  no slow motion · no speed ramp · no motion blur trails ·
  no camera shake · no focus breathing · no zoom · no vignette ·
  no colour grade shift · no day-for-night look ·
  no backpack · no tank · no hose · no cable · no visor tint ·
  no mirror coating · no tool in her hands ·
  no text · no letters · no digits · no flag · no logo · no patch ·
  no HUD overlay · no watermark
```

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| Ders | Risk | Bu dosyadaki karşılık |
|:--:|---|---|
| **127** 🔴 | ivme prompta yazılır, ekrana gelmez | Açısal hız HİÇ yazılmıyor. Yerine: süre + piksel + kendi eni + sabit cetvel (yıldız). S0 kapısı makineyle ölçülüyor |
| **124** 🔴 | plan 8 s'ye yazılır, araç 10 s üretir | Izgara ölçülmüş klip süresinden (10,005 s) kuruldu; §Genel Kural 2'de ölçüm komutu yazılı |
| **125** 🔴 | ölçülebilen sayıyı modele sorma | Üç kapının üçü de `ffmpeg`/`ffprobe` ile koşuyor: piksel farkı, ortalama parlaklık, süre |
| **123** 🔴 | yasak, yasakladığı kavramı prompta sokar | Negatif blok yalnız artefakt koruyor; şiddet/temas kelimeleri hiç geçmiyor |
| **59** 🔴 | negatif blok işi yapmaz, isim kazandırır | Her kilit POZİTİF cümleyle de yazılı (hareket, seviye, kenar, ağırlık) |
| **73** 🟠 | novum türetilmiş fenomene yüklenmez | Taşıyıcı KATI ve BİRİNCİL: 52 kilometrelik kaya. Işık olayı taşıyıcı değil, kayanın SONUCU |
| **74** 🔴 | yazılan kapı koşulmaz | §KAPI KAYDI tablosu; üretim S0'dan başlar ve S0 düşerse durur |
| **45 / 34** 🟠 | promptta etiket/isim → ekranda yazı | İsim yok, köşeli parantez yok, ekran yok, kadrajda yazı üretebilecek nesne yok |
| **79** 🟠 | vizör/sırt bible'da yazmak yetmiyor | "optically clear" + "completely FLAT back" 12 promptun 12'sinde gövdede |
| **20 / 58** 🟠 | ikinci figür, klon, yansıma | HUMAN COUNT LOCK + turkuaz TAM 1 + vizör sıfır yansıma + düzlükte yansıtıcı yüzey 0 |
| **42** 🟡 | aşınma yerleri sahne sahne kayıyor | Okra aşınma: diz, sol önkol, iki bot burnu — 6/6 sabit |
| **12 / 44** 🔴 | model hızlı olayı ağır çekime çeker | Kapanma 1,21 s ve açılma 0,94 s her promptta saniyeyle; `no slow motion` 12/12 |
| **90** 🟠 | olayı ÖLÇEN bir kenar koy | İki cetvel: PALL'ın kendi eni + gökyüzüne çivili yıldız |
| **61** 🟠 | kapak görüntüsü videoya girmez | Kapak ayrı bölümde, videoya girmez |
| **83** 🟡 | mutlak dijital sessizlik | 60 saniyenin 60'ında nefes + fan var; mutlak sıfır 0,0 saniye |
| **18** 🟡 | yürüyen gövdenin eklemlenmesi | Filmde TOPLAM 8 metre yürüyüş var (S2, 1,1 m/s, 7,3 saniye). Tek hareket tipi, düz hat, koşu 0 kare |
| **69** 🟠 | araç iniş/kalkış · loş iç mekân · aynalı yüzey | Üçü de 0 kare: araç yok, iç mekân yok, yansıtıcı yüzey yok |

---

## 🥁 VURUŞ TABLOSU VE PLAN SATIRLARI

| Sahne | Sn | Vuruş (DIKEY_MIKRO_DRAMA §1) | Bu filmde |
|:--:|:--:|---|---|
| **S0** | 00-10 | Algısal şok | Düz gri bir kütle kadrajın üstünü dolduruyor. Kavisli bir ALT KENARI var. 4,8. saniyede üst kenarı kadrajın tepesinden çıkar: bu bir bulut değil, **tırmanan bir kaya** |
| **S1** | 10-20 | Kışkırtıcı engel | Geniş kadraj ölçeği verir: düzensiz, uzatılmış, oluklu bir kaya — ve tam üstünde küçük, sert bir yıldız. **Aralık kapanıyor** (236 → 159 px) |
| **S2** | 20-30 | Z-ekseni tepkisi | Kadın merceğe doğru 8 metre yürür ve düzlüğün BİTTİĞİ yerde durur: kadrajı boydan boya kesen, mutlak siyah bir çizgi. Aralık 67 px |
| **S3** | 30-40 | Görsel dönüm / temas | **36,09'da kayanın kenarı yıldızı ısırır. 37,30'da gündüz kapanmıştır.** 1,21 saniye. Hiçbir kenar kımıldamaz; yalnız seviye düşer. 38,60'ta lamba yanar |
| **S4** | 40-50 | Kriz + **MERKEZİ SEÇİM** | 43,00'te başparmağı lambayı söndürür — bedel aynı karede: yarık çizgisi kaybolur. 3 saniye sonra PALL bakır rengiyle karanlıktan çıkar; ön kenarındaki çatlak ağı AÇILIR |
| **S5** | 50-60 | Doruk + döngü | **56,37'de gündüz geri açılır — 0,94 saniyede.** Jilet gölgeler tam eski uzunluğunda döner, bakır gider, çatlak ağı soluk bir lekeye iner. Botları hâlâ çizginin üstünde. Sağ eldiven alnına kalkar: S0'ın ilk jesti |

```
BOŞ VURUŞ       0 — altı sahnenin altısı da olay taşır
GENİŞ KURULUM   0 sahne (S1 geniş ama olay taşıyor: aralık kapanıyor)
İKİNCİ ŞOK      S4 ✅ (bakır ışık + açılan çatlak ağı)
ÇÖZÜLÜM         yok — S5 döngüye devreder
DURAKSAMA       filmde TOPLAM 4,6 saniye (S2'de 1,4 · S4'te 3,2)
```

### Plan satırları

```
TEMA: TANIKLIK  (TEMA_MUHENDISLIGI §3-4 · dikey-uyumlu "anlık durum" teması)
      Tek cümle testi: "Bu film, bir şeyi görebilmek için başka bir
      şeyi görmekten vazgeçmek hakkında." — cümlede novum kelimesi
      yok ✅
      İndeksler (§5): başın arkaya yatışı (S0 · S1 · S5) · eldivenin
      alna kalkışı (S0 · S5) · bot burnunun kabuğu tıklatması (S2) ·
      kadranda tek sıcak nokta yok — sıcak değer FİLMİN ORTASINDA
      GELİR (bakır) ve sonunda ALINIR
      Payoff (§6): tanıklığın karşılığı S4'te ekranda gösterilir
      (çatlak ağı açılır) ve S5'te geri alınır — kadın hiçbir şeyi
      yanında götürmez ✅

NOVUM TİPİ: FİZİKSEL YASA — ALGISAL (ONERME_VE_NOVUM §1 birinci tercih;
      ihlal edilen kural İZLEYİCİNİN ŞEMASIDIR, fizik değil.
      Emsaller: THE QUIET IMPACT · THE IRON SLOPE)
NOVUM TAŞIYICISI: 52 kilometrelik tek parça kaya × kadının onu
      izlemesi → kaya tırmanır, büyür, yıldızı örter, gündüzü kapatır
      ⭐ Taşıyıcı KATI ve BİRİNCİL bir nesnedir [D73 tuzağı elendi].
      Işık olayı taşıyıcı DEĞİL, taşıyıcının sonucudur.
İHLAL SAYISI: 1 algısal kural ("gündüz yavaş biter"); ekranda gerçek
      fizik ihlali 0. Diğer her şey normal fizik: jilet gölgeler,
      sessizlik, sabit ağırlık, düz yürüyüş. ⭐ Kuralın kanıtı,
      yanındaki normalin kusursuz çalışmasıdır.
KURAL KANITI: 6 sahne, 3 farklı kanal —
      PALL'ın kendi tırmanışı (S0 · S1 · S2 · S3 · S4 · S5) ·
      yıldız aralığının kapanması (S1 · S2 · S3) ·
      ışık seviyesinin iki geçişi (S3 kapanma · S5 açılma)
      [ONERME_VE_NOVUM §5: ≥3 sahne, ≥2 kanal ✅]
ÜÇ KABUL TESTİ [ONERME §4]:
      ① TEK KARE: donmuş karede düzlükteki küçük figür + kadrajın
        üstünü dolduran oluklu kaya kütlesi → anomali 1 saniyede
        işaret edilir ✅
      ② KİNETİK BAĞIMSIZLIK: kural yalnız görüntüyle kanıtlanır —
        tırmanan kenar, kapanan aralık, sönen seviye; replik 0 ✅
      ③ BAŞLIK ŞEMASI: "Bu ay 150 kilometre yukarıda" (5 kelime) →
        izleyici gökyüzüne bakar ✅

HOOK TİPİ: YANLIŞ TANIMA  (HOOK §4 · algısal novumların tipi)
      Tipin kayıtlı riski: "izleyici ilk 2 saniyede yanlış şeyi
      okuduğu için ATLAYABİLİR." Ödendi: yanlış okuma 2,5 saniyeden
      uzun sürmez — 2,8'de kavisli alt kenar ve oluklar girer,
      4,8'de üst kenar kadrajdan çıkar.
S0 SORU CÜMLESİ: "Bu şey bulut değil. O zaman ne ve neden yükseliyor?"
S1 İKİNCİ BİLGİSİ: kayanın üstünde bir YILDIZ var ve aralık kapanıyor
      — soru büyür: "değdiğinde ne olacak?"
İLK 2,5 SANİYENİN SESİ: TEK diegetik doku — kask içi nefes + fan
      uğultusu. Dışarısı sessiz. Müzik 2,5 saniyede girer. [HOOK §5①]

TOHUM BİLGİ: S0 · 06,2-07,0 s · 0,8 saniye · taşıyıcı: PALL'ın ön
      kenarındaki SOLUK, yıkanmış çatlak ağı — tepeden gelen düz
      ışıkta neredeyse okunmaz.
      ⛔ Kadın tepki vermez, kamera vurgulamaz. [FINAL §3 penceresi
      10 s ızgarasında 6-9 sn ✅ · süre ≤2 s ✅ · çevrede ✅]
GERİ DÖNÜŞ: S4 · 46,0-49,0 s — bakır ışık aynı kenarı YALAYARAK
      geçer ve ağ derin, gölgeli yarıklara açılır. Tohumun bulunduğu
      yere (ön kenar) görsel dönüş ✅

FİNAL TİPİ: DÖNGÜ + GERİ ALMA  (FINAL §2 · dikeyde döngü zorunlu ✅)
      GERİ ALMA: gündüz döner ve kanıtı siler — çatlak ağı soluk bir
      lekeye iner, bakır gider. Kadın hiçbir şey kazanmamıştır;
      yalnızca görmüştür. Ve 90 dakika sonra yine olacaktır.
AÇIK KALAN SORU SAYISI: 1 — "bir daha bakmak için 90 dakika mı
      bekleyecek, yoksa çizginin üstünden çekilecek mi?"
İKİLEM (FINAL §4): ① bedel kadrajda ve kendi eliyle: başparmağı
      lambayı söndürür, ayaklarının dibindeki 30 metrelik yarığı
      göremez hâle gelir ② aldığı şey tartışmalı: 19 saniyelik bir
      görüntü, ve o görüntü geri alınıyor ③ kamera yargısız: 6/6
      lockoff, vurgu planı yok, yakın plan yok.
PAYLAŞIM SAHNESİ: S3 · HUŞU (filmin imzası tek valanstır)
      24mm geniş + yıldızın ısırılması + 1,21 saniyede kapanan bir
      dünya + hiç değişmeyen ses.
      ⚠️ S4'ün 3,0. saniyesindeki lamba jesti huşu değil KAYGIDIR ve
      TAM 0,4 saniye sürer; tek valans korunur.

LOOP SATIRI (SENARYO_VE_VIRAL §5 + DIKEY_MIKRO_DRAMA §5):
      KİNESİK RESET — S0 ilk jest: sağ eldiven kaskın alnından
      İNİYOR (gölge yapmayı bitiriyor). S5 son jest: sağ eldiven
      kaskın alnına ÇIKIYOR. 60. saniyede hareket sürüyor; poz yok,
      donma yok, jenerik yok. Kurulum farklı (S5 = A, S0 = C) ama
      JEST, ışık durumu (tam gündüz), palet ve yön aynı. Döngü filmin
      ANLAMIDIR: geçiş bitmedi — 90 dakika sonra yenisi var.

KAPAK ANI (PAKETLEME §1): S0 · 09-10 s · altta kükürt-kemik düzlük
      şeridi ve y %67-75'te küçük figür, ortada jilet keskin ufuk
      çizgisi, y %20'den yukarısı tamamen kayanın kütlesi ·
      tek kaynak: kadraj dışı sert yıldız · odak: kayanın kavisli
      alt kenarı. Kaynak blok 00-10 ✅ · KESİLEMEZ listesinde ✅
KULLANILAN ODAK (PAKETLEME §2): ② yüksek kontrastlı silüet (koyu
      kütle, açık düzlük) + ④ ölçek uyuşmazlığı (insan / dağ sırası).
      ⛔ Odak ① (vizör yansıması) UYGULANAMAZ: vizör sıfır-yansıma
      kilidiyle yazılı [D79].

MERKEZİ SEÇİM: S4 · 42,8-43,2 sn — başparmağın lamba düğmesine
      basması. Seçim EKRANDA tek jestle tamamlanır; bedel AYNI
      SAHNEDE görünür (ışık dairesi ve yarık çizgisi söner) ve
      S5'te kalıcıdır (botlar çizginin üstünde, oynamamış) [D72].
      (Orta nokta 30 s = S2/S3 sınırı; seçimin S4'te olması
      IRON SLOPE ve STRAIGHT LINE emsalleriyle aynı yuvadır.)

ÖRÜNTÜ KIRICI KAPISI (KURGU_RITMI §2)
| S | ölçek | palet | ses dokusu |
|:--:|---|---|---|
| S0 | ÇOK SIKI (75mm, kütle taşar) | kurşun-yeşil kütle + kemik şerit | yalnız nefes + fan |
| S1 | GENİŞ (24mm, 20 m) | kemik düzlük + beyaz-altın yıldız ilk kez | nefes + tek vurulmuş metal ton |
| S2 | GENİŞ→ORTA (Z ekseni, 30→22 m) | kadranı kesen MUTLAK SİYAH çizgi ilk kez | nefes hızlanır + bot tıkırtısı |
| S3 | GENİŞ (24mm, 24 m) | **seviye çöker** — filmin birinci palet olayı | ses HİÇ DEĞİŞMEZ (filmin en sert kararı) |
| S4 | GENİŞ ALÇAK (24mm, 0,25 m) | **BAKIR** — filmin tek doygun rengi | ses daralır: nefes + düğme tık'ı |
| S5 | GENİŞ (24mm, 24 m) | gündüz geri gelir, bakır GİDER | nefes yavaşlar + tam doku döner |
Üç sütunun üçü de her ardışık çiftte değişiyor ✅
```

---

## 🔗 DEVAM ZİNCİRİ — altı sahne, tek kesintisiz geçiş

> Kaynak: `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` §5 (perde) +
> `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §6.
> ⭐ Bu filmde perde bedava gelir: **kadrajı kapatacak şey KARANLIĞIN
> KENDİSİDİR.** S3'ün son 1,4 saniyesi ve S4'ün ilk saniyesi neredeyse
> tamamen siyahtır; tek ortak nesne kabuktaki 2 metrelik ışık dairesidir.

```
PRENSİP:  SAHNE N son karesinde kadraj neredeyse tamamen karanlıktır ve
          içinde TEK bir tanınabilir nesne durur (lamba dairesi).
          SAHNE N+1 aynı nesneyle, aynı karanlıkta açılır.
          Kurguda iki klip bu karanlık anda 3-5 kare bindirilir.

⭐ COĞRAFYA NOTU: üç kamera da YERE OTURUR ve hiç taşınmaz. Değişen tek
   şey kadının konumudur: S2'de B merceğine doğru 8 metre yürür ve
   S3-S5 boyunca aynı noktada durur. Üç kamera, tek düzlük, tek yön:
   batı.
```

| Kesme | Tip | Kapatan / köprü |
|:--:|:--:|---|
| S0→S1 | SERT + ölçek tersinmesi | 75mm'in taşan kütlesi → 24mm'in bütün kayası. J-köprü: müziğin vurulmuş metal tonu kesmeden 0,6 s önce girer |
| S1→S2 | SERT + azimut değişimi (68°) | Kadın kadrajda aynı büyüklükte kalır (20 m → 30 m ama lens ve açı değişir); göz figüre kilitli kalır |
| S2→S3 | SERT + azimut değişimi (68°) | S2 son karesinde bot burnu çizginin üstünde; S3 ilk karesinde aynı bot, aynı çizgi, yandan |
| S3→S4 | **PERDE (karanlık)** | S3 son 1,4 s: kadraj karanlık, tek nesne 2 m'lik ışık dairesi → S4 aynı daireyle, aynı karanlıkta açılır |
| S4→S5 | **PERDE (karanlık)** | S4 son karesi: bakır disk ve mutlak koyu düzlük → S5 aynı bakır diskle açılır |
| S5→S0 | **döngü** | Aynı jest (eldiven alında), aynı ışık durumu (tam gündüz), aynı palet, aynı yön |

```
Bilinçli sert kesme sayısı 3 (≤3 ✅) · perde 2/5
Ses köprülü kesme: müziğin "anahtarlı" durumu S3→S4→S5 boyunca tek
   sürekli sub-bass notasıdır (2 kesme) + S0→S1 J-köprü = 3/5 = %60 ✅
   [KURGU_RITMI §3]
```

### ⚠️ B SÜRÜMÜ İÇİN BAŞLANGIÇ KARESİ — pratik not

Perde tamamlandığı an kadraj bilgisizdir; I2V modeline neredeyse siyah
bir kare vermek çapayı öldürür. **S4 ve S5'in B sürümlerinin başlangıç
karesi perdenin ortası değil, içinde lamba dairesinin (S4) ya da bakır
diskin (S5) net okunduğu karedir** — S3'ün 39,4. saniyesi ve S4'ün
49,4. saniyesi. B promptu kalan yarım saniyeyi kendi başında tamamlar.

---

## 📱 GÜVENLİ ALAN HARİTASI (9:16 · 1080×1920)

Kaynak: `kilavuzlar_ve_sistem_dosyalari/KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §5
evrensel matrisi · denetleyen rubrik: `QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md`
(FORMAT: DİKEY — 12-14. kategoriler)

```
┌──────────────────────────────┐ y=0
│  ÜST KÖR NOKTA  200-254 px   │      sekmeler, profil
├──────────────────────────────┤ y=254
│                          │S │
│                          │A │
│        GÜVENLİ ALAN      │Ğ │      sağ 242 px: beğen/paylaş/yorum
│                          │  │
│                          │242
├──────────────────────────────┤ y=1436   ⛔ BURADAN AŞAĞISI GÖRÜNMEZ
│  ALT KÖR NOKTA    484 px     │      açıklama, müzik, CTA
└──────────────────────────────┘ y=1920
```

### ⭐ LENSİ GEOMETRİ SEÇTİ — hesap

```
Dikey 9:16 kadrajda 1920 piksel şu kadar dereceye karşılık gelir:
   32mm küresel → 58,7°  →  32,7 px/derece
   24mm küresel → 73,7°  →  26,05 px/derece
   75mm küresel → 27,0°  →  71,1 px/derece

KISIT 1  Ayakta duran figürün TAMAMI y 1280-1436 bandında olmalı.
         Bant 156 px. 24mm'de bu 5,99°'dir → figür lensten en az
         1,70/tan(5,99°) = 16,2 m uzakta olmalı.
KISIT 2  Figürün botları y=1436'da ise kadrajın MERKEZİ, botlardan
         18,27° (24mm) yukarıdadır → kadrajın ÜST KENARI botlardan
         18,27 + 36,85 = 55,1° yukarıda.
KISIT 3  PALL S5'in sonunda 37,87° yükseklikte ve 12,48° enindedir:
         üst kenarı 44,1°'de.

   32mm'de kadrajın üst kenarı botlardan yalnız 43,9° yukarıda kalır
   → PALL'ın üstü KESİLİR. 24mm'de 55,1° → PALL bütün kadraja girer.

⇒ Lens tercihi değil, ÖLÇÜ. Sistem promptunun 32mm'i bu filmde
  fiziksel olarak çalışmıyor ve sapma §BİLİNÇLİ SAPMALAR'da kayıtlı.
```

### Sahne sahne denetim

| Sahne | Kurulum | Reveal nesnesi | Reveal bandı (y) | Kadının bandı (y) |
|:--:|:--:|---|:--:|:--:|
| S0 | C · 75mm | PALL'ın alt kenarı | 0-521 → 0-385 (taşar) | 1282-1436 |
| S1 | A · 24mm | PALL + yıldız (aralık) | PALL 838-1013 → 761-955 · yıldız 594 | 1282-1436 |
| S2 | B · 24mm | kadrajı kesen siyah çizgi | PALL 820-1014 → 728-945 · çizgi ~1390 | 1225-1363 |
| S3 | A · 24mm | yıldızın ısırılması + kapanma | PALL 681-898 → 569-815 · yıldız 605 | 1282-1436 |
| S4 | B · 24mm | bakır disk + çatlak ağı | 608-854 → 460-741 | 1298-1436 |
| S5 | A · 24mm | bakır disk → düz gri disk | 421-702 → 227-553 | 1282-1436 |

> ⚠️ **DÜRÜST KAYIT — TEK KABUL EDİLMİŞ SAPMA:** S5'in son karesinde
> PALL'ın disk üstü y=227'ye çıkar, yani üst kör noktanın (0-254)
> 27 pikseline girer. Sebep geometriktir ve kaçınılmazdır: 37,9°
> yükseklikte, 12,5° eninde bir cisim, figürü y=1436'nın üstünde tutan
> hiçbir dikey kadrajda tamamen güvenli alanda duramaz. **Azaltım:**
> ödülün kendisi — ön kenardaki çatlak ağı — S4 ve S5'te y 460-741
> bandına yerleştirildi; üst kör noktaya giren şey diskin boş
> arka kenarıdır. Alt çeyrek ve sağ şerit kuralları 6/6 sahnede
> ihlalsizdir.

**Her görsel promptun COMPOSITION satırına eklenen zorunlu cümle:**

```
No part of the figure falls into the bottom quarter of the frame.
```

---

## 📐 EKRAN SAYAÇLARI — üçü de metinsiz [Kart 5]

```
KANAL 1 — PALL'IN TIRMANIŞI VE BOYU   (birincil; D127'nin cevabı)

  S  yükseklik      görünen en     ekranda en    tırmanış    kendi eninin
  ──────────────────────────────────────────────────────────────────────
  S0 14,84°→17,00°  6,12°→6,73°   435→478 px    +154 px      %34
  S1 17,00°→19,57°  6,73°→7,45°   175→194 px     +67 px      %36
  S2 19,57°→22,68°  7,45°→8,34°   194→217 px     +81 px      %39
  S3 22,68°→26,54°  8,34°→9,43°   217→246 px    +101 px      %43
  S4 26,54°→31,45°  9,43°→10,79°  246→281 px    +128 px      %49
  S5 31,45°→37,87°  10,79°→12,48° 281→325 px    +167 px      %55
  (S0 75mm, diğerleri 24mm — px değerleri lensle birlikte okunur)

  ⭐ Oran her sahnede BÜYÜR: %34 → %55. Bu bir ivme değil, YAKLAŞMANIN
    perspektif sonucudur — ve modelden ivme istemediği için üretilebilir.

KANAL 2 — YILDIZ ARALIĞI              (sabit cetvel; D90)

  S1 başı   236 px        S2 başı   159 px        S3 başı    67 px
  S1 sonu   159 px        S2 sonu    67 px        36,09'da    0 px  ⛔
  ⭐ Her adım bir öncekinden büyük: 77 → 92 → 67 → temas.
    S0'da yıldız kadraj dışıdır (75mm) — sayaç S1'de başlar.

KANAL 3 — IŞIK SEVİYESİ               (ikili; TAM İKİ GEÇİŞ)

  00,00-36,09  tam gündüz    │ jilet gölge, kadının gölgesi 2,98 m
  36,09-37,30  KAPANMA 1,21s │ seviye düşer, hiçbir kenar oynamaz
  37,30-56,37  tutulma 19,07s│ bakır disk, bronz ufuk kuşağı, gölge yok
  56,37-57,31  AÇILMA 0,94s  │ gölgeler AYNI uzunlukta geri gelir
  57,31-60,00  tam gündüz    │ bakır gitti, disk düz gri
```

> ⛔ **ÜÇÜNÜN DE ORTAK KURALI:** hiçbiri rakamla, ekranla, göstergeyle
> ya da yazıyla anlatılmaz. Kadrajda yazı üretebilecek tek bir nesne
> yoktur [Kart 5 · D50 çözümü: yasak KONSEPTLE kapatılır].

---

## 🧮 FİZİK DEFTERİ — her sayının hesabı

> Bu bölüm QA için değil, **dürüstlük için** vardır: aşağıdaki
> sayıların hiçbiri uydurulmadı, hepsi iki girdi sayısından türedi
> (gezegen yarıçapı ve yüzey çekimi).

```
① GM = g·R² = 6,08 × (4,200×10⁶)² = 1,0725×10¹⁴ m³/s²
   M = GM/G = 1,607×10²⁴ kg  ·  ortalama yoğunluk 5.178 kg/m³

② YÖRÜNGE (a = 4.350 km)
   T = 2π√(a³/GM) = 5.504 s = 1 sa 31 dk 44 sn
   v = 2πa/T = 4.965 m/s
   ekvatorda zemin hızı = 2πR/31sa = 236 m/s
   → gölgenin zemine göre hızı (dikey) 4.729 m/s

③ SİNODİK VE GÖRÜNÜRLÜK
   T_sin = 1/(1/5.504 − 1/111.600) = 5.790 s
   → günde 111.600/5.790 = 19,3 doğuş
   ufuk yarı-açısı = arccos(R/a) = 15,09°
   → ufuktan ufuğa (2×15,09/360)×5.790 = 485 s = 8 dk 05 sn

④ GÖRÜNEN ÇAP  (yarı-çap 26 km)
   ufukta eğik mesafe 1.132 km → 2·arctan(26/1132) = 2,63°
   başucunda 150 km          → 2·arctan(26/150)  = 19,67°
   (Dünya'nın Ay'ı 0,52° → başucunda 37,8 kat geniş)

⑤ ROCHE VE DAYANIM
   rijit Roche = 1,26·R·(ρ_gez/ρ_uydu)^⅓ = 6.150 km   → a bunun İÇİNDE
   akışkan Roche = 2,44·R·(…)^⅓ = 11.909 km
   gelgit farkı = 2GM·R_uydu/a³ = 0,0678 m/s²
   kendi çekimi = G·M_uydu/R_uydu² = 0,0240 m/s²   → 2,8 kat küçük
   → gevşek tanecik tutunamaz (REGOLİT YOK)
   gerilme ≈ ρ·Δa·R = 3.300 × 0,0678 × 26.000 = 5,81 MPa
   → bazaltın çekme dayanımının (~10-30 MPa) altında: kaya olarak
     ayakta, ama çatlak ağıyla. Gerçek emsal: Phobos.

⑥ TUTULMA (yıldız 0,55°, bu geçişte 29,7° yükseklikte)
   ilk temas          36,09 s
   tam örtülme        37,30 s   → kapanma süresi 1,21 s
   örtülme biter      56,37 s   → TAM TUTULMA 19,07 s
   son temas          57,31 s   → açılma süresi 0,94 s
   ⭐ Asimetri gerçek: PALL uzaklaşıyor, arka kenarı daha yavaş sıyırıyor

⑦ GÖLGENİN ZEMİN HIZI
   umbra bandı = 52 km − 2×150×tan(0,275°) = 50,6 km
   eğik geçişte iz uzunluğu = 50,6/sin(29,7°) = 102 km
   → 102.000 m / 19,07 s = 5.351 m/s
   ses hızı (9 kPa, 210 K, CO₂-N₂) ≈ 226 m/s  →  MACH 23,7
   ⇒ gölgenin önünde hiçbir şey gelemez.

⑧ KATI KAYA GELGİTİ
   U = G·M_uydu·R²/a³ = 3,47 m²/s²  → denge yüksekliği 0,572 m
   × Love sayısı h₂ ≈ 0,3  →  ~17 cm, 48 dakikada bir
   (yarıkların ikincil sebebi; birincil sebep termal şok)

⑨ TUTULMADA UYDUNUN AYDINLANMASI
   Gezegen, uydudan bakıldığında gökyüzünün 150°'sini kaplar
   (yarı-açı = arcsin(R/a) = 74,9°). Ama uydunun tam altındaki zemin
   GÖLGEDEDİR; ışık yalnız 25-50 km ötedeki gündüzden, yalayarak gelir.
   → disk KENARINDA parlak, ORTASINDA koyu · şiddet gündüzün ~%4'ü
   ⭐ Bu, filmin en özgün görüntüsüdür ve tamamen gerçektir.
```

---

## ⚙️ SAHNE PROMPTLARI — okuma notu

```
Her sahnenin ÜÇ bloğu vardır:
  📸 GÖRSEL PROMPT              → önce bu üretilir ve ONAYLANIR
  🎥 VİDEO PROMPT — A SÜRÜMÜ    → T2V. Referans görsel yoksa kullanılır.
  🎥 VİDEO PROMPT — B SÜRÜMÜ    → I2V DEVAM. Bir ÖNCEKİ sahnenin son
                                   karesinden başlar; karakteri, ortamı
                                   ve ışığı YENİDEN TARİF ETMEZ.
```

---

## 🎬 SAHNE 0 — KANCA: BULUT DEĞİL

_"İki buçuk saniye bir bulut sandı. Sonra kenarı göründü."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 0 of 6. Solo female planetary photometrist science-fiction discovery film. MAXIMUM VIRAL SCALE SHOCK.
Lens: 75mm spherical, f/5.6, ISO 200.
Camera Distance: Fixed low tripod resting on the crust, lens 0.90 metres above the ground, 45 metres from the woman, aimed slightly up and framed so that she stands at frame centre-left and the rock fills the frame above her; the horizon sits just below her waist in frame.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small unlit lamp housing is moulded into the left side of the helmet ring. The suit carries no patch, no flag, no lettering, no digits and no symbol anywhere. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon. She stands still with her weight on her heels, three-quarters away from the lens, her head tipped back, her right glove just lowering from the brow of the helmet.

ENVIRONMENT / BACKGROUND: A flat sulphur-bone coloured crust plain under a thin, almost airless sky. Fine iron-ochre dust lies still in the low places; nothing is blowing. The plain runs to a dead flat horizon with no hills, no buildings and no equipment of any kind. The sky above the horizon is a deep, dark daylight blue, far darker than an Earth sky, with no cloud, no haze and no visible stars.

THE VIRAL MOMENT / REVEAL: Filling the entire frame from just above her head to the top edge and continuing past it, the underside of an ENORMOUS irregular rock hangs in the sky — sixty kilometres long, not a sphere, a lopsided lead-green grey monolith with its long axis pointed down at the plain. Its lower limb is a long shallow curve with a hard sunlit rim, and clean dark sky shows beneath it. Long parallel grooves rake across its face, with old shallow craters between them; along its leading edge a pale, washed-out network of hairline cracks is barely readable in the flat light. Its top is beyond the top of the frame. It is not glowing, not transparent and not soft-edged: it is a solid, matte, sunlit stone at close range, and it reads as far too large and far too near.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-seven and seventy-five percent of frame height, small against the plain. The horizon is a razor-hard line at roughly seventy-one percent. Everything above roughly twenty-seven percent of frame height is the rock. The band between the horizon and the rock's lower limb is clean dark sky. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near crust and ochre dust. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: A single small fierce white-gold star, well outside the top of frame, rakes the plain from beyond the left edge of the frame. Every shadow on the crust is razor-edged and absolutely black with no fill of any kind — the thin air scatters nothing, so shadow interiors are pure black. Her shadow lies 2.98 metres long across the crust. The rock's underside carries the same hard light: bright sunlit rims, absolutely black shadow inside every groove and crater. Her face reads through the clear helmet glass. No bloom, no glow filter, no lens flare, no halo, no visible star disc, no haze.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals, so there is no scattering, no mist, no dust in suspension and no sound outside the suit. The rock is a natural satellite 150 kilometres overhead in a real orbit, and it is climbing the sky steadily, gaining height and apparent size at the same time; it is rigid, single-piece and matte, and it neither rotates nor tumbles. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 75mm spherical, on a fixed low tripod resting on the crust, 0.90 metres above the ground, 45 metres from the woman, aimed slightly up so she stands at frame centre-left and the rock fills the frame above her. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — A woman in a matt lead-grey surface suit stands still on a flat sulphur-bone crust plain, three-quarters away from the lens, her head tipped back, her right glove just lowering from the brow of her clear bubble helmet. Above the razor-hard horizon, a vast flat matte grey mass fills the frame from just above her head to the top edge. At first read it could be overcast, or a cliff face.
At 2.0s — Her glove settles at her side. Nothing else in the frame moves. Her shadow lies long and absolutely black across the crust.
At 2.8s — The mass resolves: it has a LOWER EDGE, a long shallow curve with a hard sunlit rim, and clean dark sky beneath it. Long parallel grooves and old shallow craters rake across its face. It is a single enormous piece of stone hanging over the plain.
At 4.8s — Its upper edge climbs out of the top of the frame and does not come back.
At 6.2s — Along its leading edge a pale washed-out network of hairline cracks passes through the light for about eight tenths of a second, barely readable. She does not react to it and the camera does not move toward it.
At 8.0s — She tips her head further back to follow it. Her boots do not move.
By 10s — The rock's lower edge has risen by almost the full height of the standing woman, and it is still rising at exactly the same steady rate. It never tumbles, never rotates, never drifts sideways. No cuts within the shot. Hard cut to Scene 1.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. The rock is rigid, matte, single-piece and lopsided, and its motion is a single steady climb in a straight line, with no tumbling and no rotation. Its apparent size grows slightly as it climbs. The star stays outside the frame and its light never changes level. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no haze, no blowing dust. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · AÇILIŞ KARESİ)

```
The scene begins exactly as the provided image.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. The woman's right glove lowers from the brow of her helmet and settles at her side, and after that she stands completely still with her head tipped back, only her breath fogging the lower left edge of the helmet glass. The enormous grey rock overhead climbs steadily and in a dead straight line: its upper edge leaves the top of the frame at about five seconds, and by ten seconds its lower edge has risen almost the full height of the standing woman. It grows very slightly larger as it climbs. It never tumbles, never rotates, never drifts sideways and never stops. Along its leading edge a pale washed-out network of hairline cracks passes through the light for less than a second at about six seconds; she does not react to it. Her shadow on the crust stays exactly the same length and the light level never changes. Late in the shot she tips her head a little further back to follow the rock, without moving her boots.
Everything moves at normal speed — no slow motion, no speed ramp. Nothing falls, nothing blows, nothing glows.
Camera: fixed low tripod on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 1 — ÖLÇEK: ÜSTÜNDE BİR YILDIZ VAR

_"Geniş kadraj iki şey verdi: kayanın bütünü, ve nereye gittiği."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 1 of 6. Solo female planetary photometrist science-fiction discovery film.
Lens: 24mm spherical, f/8, ISO 200.
Camera Distance: Fixed low tripod resting on the crust, lens 0.90 metres above the ground, 20 metres from the woman, aimed at her back and up, framed so that she stands at frame centre-left with the rock and the star above her in the left half of the frame; the horizon sits at roughly seventy-one percent of frame height.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small unlit lamp housing is moulded into the left side of the helmet ring. The suit carries no patch, no flag, no lettering, no digits and no symbol anywhere. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon. She stands small and still at the bottom of the frame, facing away from the lens toward frame left, head tipped back.

ENVIRONMENT / BACKGROUND: A flat sulphur-bone coloured crust plain running to a dead flat horizon, with fine iron-ochre dust lying still in the low places and no hills, buildings or equipment anywhere. Long straight tension fractures cut the crust in dead straight lines running left to right across the frame; the nearest of them is far behind her and reads as a thin absolutely black line. The sky is a deep, dark daylight blue with no cloud, no haze and no visible stars.

THE VIRAL MOMENT / REVEAL: The whole satellite is now in frame and it is not a sphere — a lopsided lead-green grey monolith about sixty kilometres long, its long axis pointed down at the plain, hanging a third of the way up the sky and reading roughly seven degrees wide, more than thirteen times the width of a full moon seen from Earth. Long parallel grooves rake across it and a pale washed-out network of hairline cracks lies along its leading edge. Directly above it, clear of its upper edge by a narrow strip of dark sky, sits a small fierce white-gold star — and the strip between them is visibly narrower than the rock is wide.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-seven and seventy-five percent of frame height. The horizon is a razor-hard line at roughly seventy-one percent. The rock sits centre-left between roughly forty and fifty-three percent, the star at roughly thirty-one percent directly above it. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near crust and ochre dust. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: One small fierce white-gold star, high in the left half of the frame, is the only light source in the world. Every shadow on the crust is razor-edged and absolutely black with no fill of any kind; shadow interiors are pure black because the thin air scatters nothing. Her shadow lies 2.98 metres long across the crust. The rock carries the same hard light: bright sunlit rims and absolutely black shadow inside every groove and crater. No bloom, no glow filter, no lens flare, no halo, no haze.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals: no scattering, no mist, no suspended dust, no sound outside the suit. The satellite is 150 kilometres overhead in a real orbit and it crosses the whole sky in eight minutes; in this shot it climbs steadily on a dead straight path toward the star, which sits directly above it in the upper left of the frame, gaining apparent size as it comes, without tumbling, rotating or drifting sideways. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 24mm spherical, on a fixed low tripod resting on the crust, 0.90 metres above the ground, 20 metres from the woman, aimed at her back and up, so she stands at frame centre-left with the rock and the star above her in the left half of the frame. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — Wide. A woman in a matt lead-grey surface suit stands small and still near the bottom of the frame on a flat sulphur-bone crust plain, facing away from the lens toward frame left, head tipped back. The horizon is a razor-hard line. A third of the way up the sky hangs the whole satellite: a lopsided lead-green grey monolith about sixty kilometres long, not a sphere, its long axis pointed down at the plain. Directly above it, clear of its upper edge, sits a small fierce white-gold star.
At 2.5s — Nothing on the ground moves. Every shadow on the crust is razor-edged and absolutely black; her own shadow lies long and unmoving.
At 5.0s — The gap between the rock's upper edge and the star has closed by about a quarter. The rock has grown very slightly larger.
At 7.5s — The long parallel grooves across the rock are clearly readable now, and along its leading edge a pale washed-out network of hairline cracks passes through the light.
By 10s — The gap between the rock's upper edge and the star has closed to about two thirds of what it was, and it is a narrower strip than the rock is wide. The rock has climbed steadily the whole time, in a dead straight line, without tumbling, rotating or drifting sideways. No cuts within the shot. Hard cut to Scene 2.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. The rock is rigid, matte, single-piece and lopsided; its motion is one steady climb on a straight path toward the star, which sits directly above it in the upper left of the frame, and it grows slightly larger as it climbs. The star stays exactly where it is in frame and its light level never changes; every shadow on the crust stays exactly the same length. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no haze, no blowing dust. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the wide view with the woman small at the bottom of the frame and the whole rock in the sky beneath the star.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. The woman stands completely still with her head tipped back; only her breath fogs the lower left edge of her helmet glass. The rock climbs steadily toward the star in a dead straight line and grows very slightly larger as it climbs, so the strip of dark sky between its upper edge and the star narrows continuously through the shot until it is clearly thinner than the rock is wide. Its long parallel grooves become more readable, and the pale washed-out crack network along its leading edge passes through the light. It never tumbles, never rotates, never drifts sideways and never stops. The star stays exactly where it is and the light level never changes: every shadow on the crust holds exactly the same length for the whole shot.
Everything moves at normal speed — no slow motion, no speed ramp. Nothing falls, nothing blows, nothing glows.
Camera: fixed low tripod on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 2 — KENAR: DÜZLÜK BURADA BİTİYOR

_"Sekiz metre yürüdü ve zeminin bittiği yerde durdu."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 2 of 6. Solo female planetary photometrist science-fiction discovery film.
Lens: 24mm spherical, f/8, ISO 200.
Camera Distance: Fixed camera laid on the crust, lens 0.25 metres above the ground, 22 metres from the woman, aimed steeply up past her, framed so that she stands at frame centre-left and the rock sits high at frame left; the horizon sits low in the frame just under her boots.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small unlit lamp housing is moulded into the left side of the helmet ring. The suit carries no patch, no flag, no lettering, no digits and no symbol anywhere. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon. She has just stopped walking, standing square with her boot toes right at the edge of the fracture, head tipped back.

ENVIRONMENT / BACKGROUND: A flat sulphur-bone coloured crust plain seen from ground level, so the crust grain and the still iron-ochre dust read large in the near foreground. A straight tension fracture four metres wide and thirty metres deep runs left to right across the whole width of the frame just in front of her boots, dead straight and horizontal in frame; from this low angle it reads as an absolutely black line with clean hard lips, and nothing inside it is visible. Beyond her the plain runs to a dead flat horizon. The sky is a deep, dark daylight blue with no cloud, no haze and no visible stars.

THE VIRAL MOMENT / REVEAL: High to frame left, the lopsided lead-green grey monolith now reads roughly eight degrees wide and has climbed to nearly a quarter of the way up from the horizon toward the zenith; the strip of dark sky between its upper edge and the small fierce white-gold star above it is now thinner than a third of the rock's own width. Grooves and craters cover its face and the pale washed-out crack network lies along its leading edge. The black fracture line and the pale sunlit plain meet in a single hard edge across the frame, and the woman stands exactly on it.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-four and seventy-one percent of frame height, standing on the black fracture line which crosses the full width of the frame at roughly seventy-two percent. The rock sits at frame left between roughly thirty-eight and fifty-three percent, the star at roughly thirty-four percent above it. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near crust grain and ochre dust. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: One small fierce white-gold star, high in the left half of the frame, is the only light source. Every shadow on the crust is razor-edged and absolutely black with no fill; her shadow lies 2.98 metres long. The inside of the fracture is pure black with no visible floor and no reflected light of any kind. The rock carries bright sunlit rims and absolutely black groove shadows. No bloom, no glow filter, no lens flare, no halo, no haze.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals: no scattering, no mist, no suspended dust, no sound outside the suit — she walks at 1.1 metres per second without raising a single grain of dust. The satellite is 150 kilometres overhead in a real orbit and climbs steadily on a dead straight path toward the star, which sits directly above it at frame left, gaining apparent size as it comes, without tumbling, rotating or drifting sideways. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 24mm spherical, camera laid on the crust with the lens 0.25 metres above the ground, 22 metres from the woman's final position, aimed steeply up past her, so she stands at frame centre-left and the rock sits high at frame left. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — Ground-level wide. The crust grain and still ochre dust read large in the near foreground. A woman in a matt lead-grey surface suit stands thirty metres away, small, and begins walking straight toward the lens at the bottom of the frame at a steady 1.1 metres per second, her boots setting flat and taking weight, raising no dust at all. High to frame left the lopsided grey rock hangs beneath a small fierce white-gold star.
At 3.0s — Between her and the lens the plain ends: a straight tension fracture, four metres wide and thirty metres deep, runs left to right across the entire width of the frame, dead straight and horizontal, as an absolutely black line with clean hard lips. Nothing inside it is visible.
At 5.5s — She grows in frame as she comes, without the camera moving. Her pace does not change.
At 6.6s — She stops. Her right boot toe taps the crust once before she sets her weight, and stands square with her boot toes on the black line.
At 8.0s — She tips her head back. Above her the rock has climbed another notch and the strip of dark sky between its upper edge and the star is now thinner than a third of the rock's own width.
By 10s — She holds absolutely still on the lip. The rock is still climbing at the same steady rate. No cuts within the shot. Hard cut to Scene 3.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. She walks in a dead straight line at one steady pace, each boot lifting, setting and taking weight, never sliding and never gliding, and she raises no dust. The rock is rigid, matte, single-piece and lopsided; its motion is one steady climb on a straight path toward the star, which sits directly above it at frame left, growing slightly larger, with no tumbling and no rotation. The star stays exactly where it is and the light level never changes. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no haze, no blowing dust. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the ground-level view with the woman small in the distance and the black fracture line crossing the frame in front of her.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. She walks straight toward the lens at the bottom of the frame at a steady 1.1 metres per second, each boot lifting, setting flat and taking weight, never sliding, never gliding, raising no dust at all, and she grows in frame as she comes without the camera moving. She stops at the lip of the fracture, taps the crust once with her right boot toe before setting her weight, and stands square with her boot toes right on the black line. Then she tips her head back and holds absolutely still. Above and to frame left, the rock climbs steadily and in a dead straight line, growing very slightly larger, so the strip of dark sky between its upper edge and the star narrows through the shot until it is thinner than a third of the rock's own width. The rock never tumbles, never rotates, never drifts sideways. The star stays exactly where it is and the light level never changes: every shadow on the crust holds exactly the same length.
Everything moves at normal speed — no slow motion, no speed ramp. Nothing falls, nothing blows, nothing glows.
Camera: fixed camera laid on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 3 — TEMAS: GÜNDÜZ KAPANIYOR

_"Bir buçuk saniye. Hiçbir kenar kımıldamadı; yalnız seviye düştü."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 3 of 6. Solo female planetary photometrist science-fiction discovery film. MAXIMUM VIRAL SWITCHED-DAYLIGHT SHOCK.
Lens: 24mm spherical, f/8, ISO 200.
Camera Distance: Fixed low tripod resting on the crust, lens 0.90 metres above the ground, 24 metres from the woman, aimed at her side and up, framed so that she stands at frame centre-left with the rock and the star above her in the left half of the frame; the horizon sits at roughly seventy-one percent of frame height.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small lamp housing is moulded into the left side of the helmet ring and it is lit, throwing a hard white disc of light about two metres across on the crust at her boots. She stands in profile to the lens, boot toes on the lip of the fracture, head tipped back, her right glove just coming away from the side of her helmet.

ENVIRONMENT / BACKGROUND: A flat sulphur-bone coloured crust plain, now unlit — flat, dim and colourless, with the still iron-ochre dust drained of hue. The straight tension fracture, four metres wide and thirty metres deep, runs left to right past her boots, dead straight and horizontal in frame, and is invisible except where the lamp disc crosses it, reading there as a black bar through the middle of the light. Beyond her the plain runs to a dead flat horizon. The sky is deep indigo with a thin bronze band all the way around the horizon and no visible stars.

THE VIRAL MOMENT / REVEAL: The sixty-kilometre monolith now sits a third of the way up the sky, roughly nine degrees wide, and it has taken the star: the sky where the star was is simply covered by stone. Its edge against the sky is a plain hard edge with no ring of light around it and no glare of any kind. The plain, which a moment ago carried razor-hard black shadows, now carries none — nothing moved, nothing swept across the ground, the light simply went. The only lit thing left in the world is a two-metre disc of crust at her boots.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-seven and seventy-five percent of frame height, with the lamp disc at her boots at roughly seventy-four percent. The rock sits centre-left between roughly thirty and forty-two percent. The horizon is a soft edge at roughly seventy-one percent with the bronze band along it. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only unlit crust. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: The star is completely covered, so there is no direct light in the scene at all. The plain is lit only by the thin bronze band around the horizon, fifty kilometres away: dim, flat, colourless. The helmet lamp throws a hard white disc of light about two metres across on the crust, with NO visible beam in the air above it — the thin atmosphere scatters nothing. Light bouncing back off the crust lifts her chin and the lower edge of her helmet glass. The rock overhead is a dark shape against a slightly less dark sky, just beginning to carry a faint copper edge. No bloom, no glow filter, no lens flare, no halo, no corona, no ring of light around the rock.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals: no scattering, no mist, no suspended dust, no sound outside the suit. The satellite is 150 kilometres overhead and 52 kilometres wide, which is eighteen times the width of the star, so the star's disc is covered completely and instantly with no ring, no corona and no partial glare. The shadow crosses the plain at more than five kilometres per second — more than twenty times the local speed of sound — so nothing precedes it: no wind, no sound, no advancing line on the ground. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no corona, no ring of light around the rock, no diamond ring, no glare, no perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no day-for-night colour grade, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 24mm spherical, on a fixed low tripod resting on the crust, 0.90 metres above the ground, 24 metres from the woman, aimed at her side and up; she stands at frame centre-left, the rock and the star above her at frame left. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — Wide, in full daylight. A woman in a matt lead-grey surface suit stands in profile at the lip of a black tension fracture, head tipped back. Every shadow on the crust is razor-edged and absolutely black. A third of the way up the sky, the lopsided grey rock climbs steadily toward a small fierce white-gold star directly above it at frame left; the strip of dark sky between them is thinner than a quarter of the rock's width.
At 3.0s — The strip has closed to a hairline. Nothing on the ground has changed.
At 6.1s — The rock's leading edge reaches the star and takes the first bite out of it.
At 6.1s to 7.3s — Over one and two tenths of a second the daylight goes out. The light LEVEL drops everywhere in the frame at once. Every edge stays exactly where it is: nothing moves, nothing sweeps across the ground, no shadow slides or shortens, no colour shifts. The razor-black shadows simply stop existing. The sound does not change at all.
At 7.3s — Full dark. The plain is dim, flat and colourless; the sky deep indigo with a thin bronze band around the horizon; the rock a dark shape with a plain hard edge and no ring of light.
At 8.6s — Her right glove rises to the left side of her helmet and the lamp comes on: a hard white disc of light about two metres across on the crust at her boots, with no visible beam in the air. The black line runs through the middle of the disc.
By 10s — She stands lit only by the bounce off it, head still back. The rock keeps climbing at the same steady rate. No cuts within the shot. Hard cut to Scene 4.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. The rock is rigid, matte, single-piece and lopsided; its motion is one steady climb, no tumbling, no rotation. The daylight ends as a level change, not a moving shadow: no line crosses the ground, no edge sweeps, no vignette. Everything moves at normal speed. No slow motion, no speed ramp. No corona, no ring of light, no bloom, no lens flare, no haze. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the wide daylight view with the woman in profile at the lip of the fracture and the rock at frame left climbing toward the star directly above it.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. She stands completely still, head tipped back. The rock climbs steadily and in a dead straight line at frame left until its leading edge reaches the star directly above it and covers it. Over the following one and two tenths of a second the daylight goes out: the light level drops everywhere in the frame at the same time, every edge stays exactly where it is, nothing moves and nothing sweeps across the ground, no shadow slides or shortens, no colour shifts, and the razor-black shadows on the crust simply stop existing. The plain becomes dim, flat and colourless; the sky becomes deep indigo with a thin bronze band all around the horizon; the rock becomes a dark shape with a plain hard edge and no ring of light around it. Then her right glove rises to the left side of her helmet and a lamp comes on, laying a hard white disc of light about two metres across on the crust at her boots with no visible beam in the air, the black fracture line running straight through the middle of it. She holds still, lit only by the bounce, head still tipped back, while the rock keeps climbing at the same steady rate.
Everything moves at normal speed — no slow motion, no speed ramp. Nothing falls, nothing blows. No corona, no ring of light, no lens flare.
Camera: fixed low tripod on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 4 — SÖNDÜRME: MERKEZİ SEÇİM

_"Yukarıdakini görmek için, bastığı yeri görmekten vazgeçti."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 4 of 6. Solo female planetary photometrist science-fiction discovery film. MAXIMUM VIRAL PLANET-LIT ROCK SHOCK.
Lens: 24mm spherical, f/2.8, ISO 3200.
Camera Distance: Fixed camera laid on the crust, lens 0.25 metres above the ground, 22 metres from the woman, aimed steeply up past her, framed so that she stands at frame centre-left and the rock sits high at frame left.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small lamp housing is moulded into the left side of the helmet ring and it is now unlit. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon. She stands square at the lip of the fracture, head tipped fully back, her right glove just falling away from the side of her helmet.

ENVIRONMENT / BACKGROUND: A flat crust plain in total shadow, seen from ground level: dim, flat and almost colourless, with only enough light to read the crust grain in the near foreground. The straight tension fracture runs left to right past her boots, dead straight and horizontal in frame, and is now completely invisible — an unreadable part of an unreadable plain. Beyond her the plain runs to a dead flat horizon carrying a thin bronze band all the way around. The sky is deep indigo with no visible stars.

THE VIRAL MOMENT / REVEAL: Filling the upper left of the frame, the sixty-kilometre monolith glows COPPER-BRONZE — and it is brightest around its rim and darkest through its middle, because the only light reaching it comes from the daylight beyond the shadow band, fifty kilometres away and grazing in from every side. In that raking copper light the pale network of hairline cracks along its leading edge has opened into a system of deep, shadowed fissures running across the rock: it is a single piece of stone with a crack pattern through it. Its edge against the sky is a plain hard edge with no ring of light around it.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-eight and seventy-five percent of frame height. The copper rock sits at frame left between roughly thirty-two and forty-four percent, with the opened fissure system along its leading edge at roughly thirty-eight to forty-four percent — the payoff detail is held well clear of the top and bottom bands. The bronze horizon band runs at roughly seventy-eight percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only unlit crust grain. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: There is no direct light in the scene. The rock overhead is lit only by planetshine at roughly four percent of daylight, copper-bronze, bright at the rim and dark through the middle. The plain is lit only by the thin bronze band around the horizon. For the first three seconds a hard white disc of lamp light about two metres across lies on the crust at her boots, with no visible beam in the air; then it goes out in a single frame and the frame's only light is the copper above. No bloom, no glow filter, no lens flare, no halo, no corona, no ring of light around the rock.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals: no scattering, no mist, no suspended dust, no sound outside the suit. The satellite is 150 kilometres overhead and its near face is lit by the planet below, which fills a hundred and fifty degrees of its sky — but the ground directly beneath it is in shadow, so the light arrives only at grazing angles from beyond the shadow band, which is why the disc is rim-bright and centre-dark. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no corona, no ring of light around the rock, no diamond ring, no glare, no perfectly spherical moon, no smooth moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no day-for-night colour grade, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 24mm spherical, camera laid on the crust with the lens 0.25 metres above the ground, 22 metres from the woman, aimed steeply up past her, so she stands at frame centre-left and the rock sits high at frame left. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — Total shadow. The only lit things in the frame are a hard white disc of lamp light about two metres across on the crust at the woman's boots, the underside of her chin, and a thin bronze band all the way around the horizon. Above and to frame left, a shape darker than the sky.
At 2.4s — She tips her head fully back. Against the bright disc at her feet, the sky above her reads as nothing at all.
At 3.0s — Her right glove touches the left side of her helmet and the lamp goes OUT in a single frame. The white disc and the black fracture line inside it vanish together. Her boots do not move.
At 4.0s — The frame is almost entirely dark, with only the bronze horizon band left.
At 6.0s — The rock comes up out of the dark: a copper-bronze glow across the upper left of the frame, brightest around its rim and darkest through its middle.
At 8.0s — In that raking copper light the pale crack network along its leading edge has opened into a system of deep, shadowed fissures running across the stone.
By 10s — The copper is at its strongest and the fissure system is fully readable. The rock is still climbing at the same steady rate; her boots have not moved. No cuts within the shot. Hard cut to Scene 5.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. The rock is rigid, matte, single-piece and lopsided; its motion is one steady climb with no tumbling and no rotation. The lamp goes out in a single frame — it does not dim, fade or flicker — and there is no visible beam in the air at any point. The copper light rises only as the image itself becomes readable; nothing in the sky brightens or pulses. Everything moves at normal speed. No slow motion, no speed ramp. No corona, no ring of light, no bloom, no glow filter, no lens flare, no haze, no blowing dust. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the dark ground-level view with the white lamp disc on the crust at her boots and the bronze band around the horizon.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. She tips her head fully back. Then her right glove touches the left side of her helmet and the lamp goes out in a single frame: the white disc on the crust and the black fracture line inside it vanish together, and her boots stay exactly where they are. For about two seconds the frame is almost entirely dark, with only the thin bronze band around the horizon. Then the rock overhead comes up out of the dark as a copper-bronze glow across the upper left of the frame, brightest around its rim and darkest through its middle, and in that raking light the pale crack network along its leading edge opens into a system of deep, shadowed fissures running across the stone. The rock keeps climbing steadily and in a dead straight line the whole time, never tumbling, never rotating, never drifting sideways. She does not move her boots.
Everything moves at normal speed — no slow motion, no speed ramp. The lamp does not dim, fade or flicker; there is no visible beam in the air. No corona, no ring of light, no lens flare.
Camera: fixed camera laid on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 5 — GERİ AÇILMA: DÖNGÜ

_"Işık geri geldi ve kanıtı sildi. Doksan dakika sonra bir daha olacak."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 5 of 6. Solo female planetary photometrist science-fiction discovery film.
Lens: 24mm spherical, f/8, ISO 200.
Camera Distance: Fixed low tripod resting on the crust, lens 0.90 metres above the ground, 24 metres from the woman, aimed at her side and up, framed so that she stands at frame centre-left with the rock and the star above her in the left half of the frame; the horizon sits at roughly seventy-one percent of frame height.

SUBJECT: A 34-YEAR-OLD WOMAN, a planetary photometrist — warm olive skin with clearly visible pore texture and a light scatter of freckles across the nose and cheekbones, dark brown eyes with faint shadows beneath them, thick dark eyebrows, a small pale scar through the right eyebrow, a chapped lower lip, natural facial asymmetry, dark hair pulled back with two loose strands stuck to her right temple. Photographed as a real person, not CGI. She is 1.70 metres tall. She wears a matt lead-grey soft-shell surface suit with dusty teal accent seams running down the outer arms and along the hip line, and a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. Fine ochre dust is ground into the knees, the left forearm and both boot toes in exactly the same places in every scene. Her helmet is a single clear bubble of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her face is fully readable through it at every head angle, and each exhale briefly fogs the lower left edge of the glass. A small unlit lamp housing is moulded into the left side of the helmet ring. The suit carries no patch, no flag, no lettering, no digits and no symbol anywhere. Her grey gloves are completely empty — no tool, no phone, no instrument, no weapon. She stands in profile at the lip of the fracture with her boot toes still exactly on the black line, head tipped back, her right glove rising to the brow of her helmet.

ENVIRONMENT / BACKGROUND: A flat sulphur-bone coloured crust plain back in full daylight, with fine iron-ochre dust lying still in the low places and razor-hard black shadows returned to exactly the lengths they had before. The straight tension fracture, four metres wide and thirty metres deep, runs left to right past her boots, dead straight and horizontal in frame, as an absolutely black line across the frame, and her boot toes are on its lip. Beyond her the plain runs to a dead flat horizon. The sky is a deep, dark daylight blue with no cloud, no haze and no visible stars.

THE VIRAL MOMENT / REVEAL: High to frame left, the sixty-kilometre monolith is now roughly twelve degrees wide — more than twenty times the width of a full moon seen from Earth — and it has moved past the star, which burns clear of its trailing edge again. In the returned daylight the rock is flat grey once more: the copper is gone and the fissure system that was legible a second ago has washed back into a pale, almost unreadable smear along its leading edge. It is still climbing.

COMPOSITION: Vertical 9:16. The woman stands at frame centre-left between roughly sixty-seven and seventy-five percent of frame height, standing on the black fracture line which crosses the frame at roughly seventy-two percent. The rock sits at frame left between roughly twelve and twenty-nine percent, with the pale washed-out crack smear along its leading edge at roughly twenty-four to twenty-nine percent. The star burns at roughly thirty-two percent, clear of the rock's trailing edge. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near crust and ochre dust. Nothing story-critical sits in the right eighth of the frame.

LIGHTING: One small fierce white-gold star, high in the left half of the frame, is the only light source again. Every shadow on the crust is razor-edged and absolutely black with no fill; her shadow lies 2.98 metres long, exactly as it did at the start of the film. The inside of the fracture is pure black. The rock carries bright sunlit rims and absolutely black groove shadows, with no copper anywhere. No bloom, no glow filter, no lens flare, no halo, no haze.

PHYSICS: Surface gravity is 0.62 g. The air is thin, 9 kilopascals: no scattering, no mist, no suspended dust, no sound outside the suit. The satellite is 150 kilometres overhead in a real orbit; it crosses the whole sky in eight minutes and will cover the star again in about ninety minutes. It climbs steadily on a dead straight path, gaining apparent size as it comes, without tumbling, rotating or drifting sideways. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the woman in the lead-grey suit. no second figure, no duplicate of her, no human reflection, no mirrors, no corona, no ring of light around the rock, no perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris, no falling objects, no visible beam of light in the air, no volumetric shafts, no lens flare, no bloom, no glow filter, no halo, no vignette, no backpack, no tank, no hose, no cable, no visor tint, no mirror coating, no tool in her hands, no slow motion, no speed ramp, no motion blur trails, no camera shake, no focus breathing, no zoom, no miniature look, no CGI look, no waxy skin, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 24mm spherical, on a fixed low tripod resting on the crust, 0.90 metres above the ground, 24 metres from the woman, aimed at her side and up; she stands at frame centre-left, the rock and the star above her at frame left. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — Total shadow, wide. A woman in a matt lead-grey surface suit stands in profile, unlit, on a dim colourless plain, head tipped back. High to frame left the enormous lopsided rock glows copper-bronze, bright at its rim and dark through its middle, with a system of deep shadowed fissures running along its leading edge. A thin bronze band rings the horizon.
At 3.0s — The fissure system is at its most legible. Nothing on the ground moves.
At 6.4s — The star's edge comes clear of the rock's trailing edge.
At 6.4s to 7.3s — Over nine tenths of a second the daylight comes back. The light LEVEL rises everywhere in the frame at the same time. Every edge in the frame stays exactly where it is: nothing moves, nothing sweeps across the ground, no shadow slides. The razor-edged black shadows return to exactly the lengths they had at the start, and her own shadow lies 2.98 metres long across the crust again.
At 7.6s — In the returned daylight the copper is gone. The rock is flat grey and the fissure system has washed back into a pale, almost unreadable smear along its leading edge. Her boot toes are still exactly on the black fracture line; she has not moved them.
At 8.8s — Her right glove rises to the brow of her helmet.
By 10s — The glove is at the brow, shading her eyes, and the rock is still climbing at the same steady rate. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot; no second figure, no reflection. The rock is rigid, matte, single-piece and lopsided; its motion is one steady climb with no tumbling and no rotation. The daylight returns as a level change, not as a moving shadow: no line crosses the ground, no edge sweeps, no vignette opens, no colour grade shifts. Everything moves at normal speed. No slow motion, no speed ramp. No corona, no ring of light, no bloom, no glow filter, no lens flare, no haze, no blowing dust. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the dark wide view with the woman unlit in profile and the copper-lit rock high to frame left.
The camera stays perfectly locked off for the whole 10 seconds — it never pans, never tilts, never moves, never shakes. She stands completely still, head tipped back, while the copper rock climbs steadily and in a dead straight line and the fissure system along its leading edge stays legible. Then the star comes clear of the rock's trailing edge and over nine tenths of a second the daylight comes back: the light level rises everywhere in the frame at the same time, every edge stays exactly where it is, nothing moves and nothing sweeps across the ground, and the razor-edged black shadows return to exactly the lengths they had at the start of the film. The copper is gone; the rock is flat grey and the fissure system washes back into a pale, almost unreadable smear along its leading edge. Her boot toes are still exactly on the black fracture line and she has not moved them. Late in the shot her right glove rises to the brow of her helmet to shade her eyes, and the rock is still climbing at the same steady rate as the shot ends.
Everything moves at normal speed — no slow motion, no speed ramp. Nothing falls, nothing blows. No corona, no ring of light, no lens flare.
Camera: fixed low tripod on the ground, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎶 MÜZİK PROMPTU (Tek Global Tema — 60 sn)

Araç: Suno / Udio · tek parça · 60 saniye · söz yok, geleneksel melodi yok.
Tempo **96 BPM**: 10 saniyelik sahne = tam 16 vuruş = 4 ölçü — her sahne
sınırı bir ölçü çizgisine oturur (GOOGLE_FLOW_MUSIC §14 hizalama).
Toplam 24 ölçü.

```
60-second instrumental cue, no vocals, no lyrics, no traditional melody, 96 BPM, patient and unsentimental. NO DRUM KIT, NO SNARE, NO CYMBALS, NO RISER, NO WHOOSH, NO BRAAM. THREE LAYERS ONLY: 1. THE PLAIN: a low continuous drone, completely unchanging in pitch and level, with no swell and no vibrato — it is the room tone of an almost airless world. 2. THE CLIMB: one dry struck metal tone, once per bar, damped, no reverb tail, which shifts UP one scale step at the start of every ten-second scene — six scenes, six steps, never resolving. 3. THE SWITCH: a single sustained 42 Hz sub-bass note doubled by an 84 Hz harmonic so it survives a phone speaker.

Dynamic arc, and this is the whole point of the piece: from 0.0 to 36.1 seconds layers 1 and 2 run exactly as described, absolutely steady, with no build and no anticipation of any kind — the music must not warn the listener that anything is coming. At 36.1 seconds layers 1 and 2 CUT OUT COMPLETELY over one and two tenths of a second, not by fading but by dropping in level while layer 3 comes up underneath them, and from 37.3 seconds there is nothing but the single sustained sub-bass note, unchanging, for nineteen seconds. At 56.4 seconds that note CUTS and layers 1 and 2 return over nine tenths of a second at exactly the level, pitch and position they had before, as if they had never stopped — layer 2 resumes on the step it would have reached. The piece runs on unchanged to 60.0 seconds and CUTS flat with no fade, no cadence and no final chord, so it butts straight onto the opening beat.

Mood: geological, patient, indifferent. No triumph, no dread, no horror sting, no release. Reference feel: the unhurried low-register patience of Jóhann Jóhannsson and the dry, unresolved single-cell repetition of Mica Levi. Do not quote, sample or reproduce any melody, motif or lyric from either.

NO vocals, NO lyrics, NO choir, NO orchestral swell, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO horror stinger, NO jump-scare hit, NO drum kit, NO snare, NO cymbals, NO guitar, NO piano, NO field recording, NO build-up before the 36-second mark.
```

> **Yapı filmi birebir izler ve TEK BİR İŞ YAPAR: müzik de anahtarlıdır.**
> Katman 1 ve 2, gündüzle birlikte 36,1'de kapanır ve gündüzle birlikte
> 56,4'te açılır — aynı sürelerde (1,21 s ve 0,94 s), aynı asimetriyle.
> ⛔ **36. saniyeden önce hiçbir yükselme, hiçbir gerilim işareti YOK.**
> Bu filmin tezi haber verilmemesidir; müziğin haber vermesi tezi öldürür.
> Katman 2 = tırmanış: her sahnede bir basamak yukarı, hiç çözülmez ve
> tutulmadan sonra **kaldığı basamaktan** devam eder — 19 saniye
> yokluğunda da tırmanış sürdü.
> ⭐ Diegetik yatak müzikten AYRIDIR ve 60 saniyenin 60'ında çalışır:
> kask içi nefes + fan uğultusu. Işık kapandığında bu yatak **hiç
> değişmez** — mutlak dijital sıfır 0,0 saniyedir [D83].

---

## 🖼️ KAPAK PROMPTU (1080×1920)

⚠️ **Bu görsel videoya GİRMEZ** — yalnızca thumbnail [Ders 61].

> **Kaynak an: S0 · 0:09-0:10.** 120 px'te okunması gereken şey ÜÇ
> ŞEYDİR: altta açık renk ince bir zemin şeridi, ortada jilet keskin
> düz bir çizgi, ve o çizginin üstünde kadranın tamamını dolduran KOYU
> BİR KÜTLE — kütlenin alt kenarı kavisli. Şeritte küçük, dik, açık
> renk bir leke: insan. Sorulacak soru ölçüdür: *bu insan neyin
> altında duruyor?*

```
Cinematic photorealistic vertical cover image, 1080x1920, 9:16. A flat sulphur-bone coloured crust plain under a thin, almost airless sky, seen from a low camera 0.90 metres above the ground, 45 metres from a lone standing figure, in hard raking light from a single small fierce white-gold star outside the frame.

A 34-year-old woman in a matt lead-grey soft-shell surface suit with dusty teal accent seams stands small on the plain, three-quarters away from the lens, head tipped back. Her suit has a completely flat back — no backpack, no tank, no hose — and her helmet is a single clear bubble of optically clear glass through which her face is readable, with no tint and no mirror coating. Fine ochre dust is ground into her knees and boot toes. The suit carries no patch, no flag and no lettering anywhere. Her gloves are empty. Her shadow lies long and absolutely black across the crust.

Filling the entire frame from just above her head to the top edge and continuing past it, the underside of an enormous irregular rock hangs in the sky — sixty kilometres long, not a sphere, a lopsided lead-green grey monolith with its long axis pointed down at the plain. Its lower limb is a long shallow curve with a hard sunlit rim, and clean dark sky shows beneath it. Long parallel grooves rake across its face with old shallow craters between them, and a pale washed-out network of hairline cracks lies along its leading edge. It is solid, matte and sunlit — a stone at close range, not a glow and not a haze.

COMPOSITION: The woman sits at frame centre-left between roughly sixty-seven and seventy-five percent of frame height. The razor-hard horizon runs at roughly seventy-one percent. Everything above roughly twenty-seven percent of frame height is the rock; between the horizon and the rock's lower limb there is a clean band of dark sky. Nothing story-critical falls in the top 254 pixels, the bottom 484 pixels, or the right 242 pixels; those bands are covered by platform UI.

LIGHTING: One small fierce white-gold star outside the frame rakes the plain from beyond the left edge of the frame. Every shadow is razor-edged and absolutely black with no fill, because the thin air scatters nothing. The rock carries bright sunlit rims and absolutely black groove shadows. No bloom, no glow filter, no lens flare, no halo, no haze, no visible star disc.

NEGATIVE: Exactly one human being, no second figure, no duplicate, no human reflection, no mirrors. No perfectly spherical moon, no smooth moon, no glowing moon, no transparent moon, no ring system, no second moon, no star field, no aurora. No cloud, no haze, no mist, no dust cloud, no blowing dust, no smoke, no fire, no sparks, no debris. No visible beam of light in the air, no lens flare, no bloom, no glow filter, no halo, no vignette. No backpack, no tank, no hose, no visor tint, no mirror coating, no tool in her hands. Not miniature, no CGI look, no waxy skin. No text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.

Output: 9:16, 1080x1920, no text, no watermark.
```

**120 px testi:** küçültüldüğünde okunması gereken tek şey →
*altta ince açık bir şerit, üstünde jilet düz bir çizgi, çizginin
üstünde kadranı dolduran koyu kütle ve kütlenin kavisli alt kenarı;
şeritte tek küçük dik leke.* Kütle "bulut" gibi yumuşak görünüyorsa ya
da alt kenarı düz çıktıysa kapak başarısızdır, yeniden üret. Bu kapağın
tek işi **ölçü uyuşmazlığını** göstermektir: bir insan, ve üstünde bir
dağ sırası.

> Kapak denetimi 120 px posta pulu testiyle elle yapılır (KAPAK_QA
> rubriği 12.08.2026'da kaldırıldı).

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ

**Başlık alternatifleri (≤40 karakter):**

```
1. Bu ay 150 kilometre yukarıda      (31)
2. Gün burada 1,2 saniyede kapanıyor (35)
3. Günde 19 kez batan gökyüzü        (28)
```

**Açıklama (ilk satır kancadır):**

```
Bu gezegende gündüz batmaz — kapanır.
Uydusu 150 kilometre yukarıda ve saniyede 5 kilometre gidiyor:
batıdan doğuyor, gökyüzünü 8 dakikada geçiyor ve günde 19 kez
yıldızın önünden geçiyor. Işık 1,2 saniyede gidiyor, 19 saniye
sonra 0,94 saniyede geri geliyor. 60 saniye, tek nefes.
#uzay #gezegen #bilimkurgu #shorts #ai
```

**Hashtag paketi (11):**

```
GENİŞ   #shorts #uzay #bilimkurgu
NİŞ     #astronomi #gezegen #tutulma #astrofizik #yapayzekafilm
KONSEPT #yakıngeçiş #rochesınırı #phobos
```

**Sabitlenecek ilk yorum (arkasındaki gerçek bilim, tek blok):**

```
Mars'ın uydusu Phobos gerçekten batıdan doğar, gökyüzünü dört saatte
geçer ve günde iki kez doğar — çünkü Mars'ın kendi dönüşünden hızlı
dönüyor. PALL onun sıkıştırılmış hâli: 150 km irtifa, 8 dakikada
ufuktan ufuğa, günde 19 doğuş. Roche sınırının içinde olduğu için
kendi çekimi değil KAYA DAYANIMI tutuyor onu (gelgit gerilmesi
5,81 MPa, bazaltın çekme dayanımının hemen altında) — olukları ve
çatlak ağı bu yüzden var, tıpkı Phobos'un olukları gibi. Filmdeki
her sayı bu hesapla yazıldı; ekranda imkânsız hiçbir şey yok. 🌘
```

### 🤐 SPOILER BÜTÇESİ — dört yüzey, tek bütçe [D114 · PAKETLEME §5]

| Yüzey | Ne verir | Ne vermez |
|---|---|---|
| Başlık | evrenin ölçüsünü: uydu 150 km yukarıda | tutulmayı, bakır ışığı, lamba kararını, döngüyü |
| Kapak | S0'ın ölçü şokunu: insan ve üstündeki kütle | yıldızı, tutulmayı, karanlığı, çatlak ağını |
| Fragman | **yok** — bağımsız dikey film (DIKEY_MIKRO_DRAMA §6) | — |
| Açıklama | kuralın mekanizmasını: 19 kez, 1,2 saniye | kadının ne yaptığını, lambayı, çatlak ağını, bedeli |

```
TEK CÜMLE TESTİ: dört yüzey yan yana konduğunda bir yabancı, filmi
izlemeden hikâyenin sonunu tek cümleyle söyleyebiliyor mu?
→ HAYIR. Dördü de "uydu çok yakın ve gündüzü kapatıyor" der; hiçbiri
  kadının lambayı söndürdüğünü, kayanın karanlıkta BAKIR yandığını,
  ön kenardaki çatlak ağının açıldığını ya da ışığın geri gelip
  kanıtı sildiğini söylemez. ✅ bütçe tutuyor.
```

---

## 🔒 Master Cinema Lock

```
Photorealistic live-action cinematography, Kodak Vision3 color science,
natural 35mm film grain, no digital sharpening. Vertical 9:16 native
framing. One spherical lens per shot (24mm or 75mm) — no anamorphic,
no horizontal flare; camera height and distance stated in metres.
ABSOLUTELY ZERO CAMERA MOVEMENT IN ALL SIX SHOTS — every camera rests
on the ground; no pan, no tilt, no dolly, no zoom, no handheld, no
shake. Single continuous 10-second takes, 0 cuts. Real-time motion at
normal playback speed throughout — no slow motion, no speed ramp, ever.
The satellite is a rigid, matte, single-piece, lopsided rock 52
kilometres across and 150 kilometres overhead; it climbs the sky in one
steady straight line, growing slightly larger as it comes, and it never
tumbles, never rotates, never drifts sideways and never stops. It is
eighteen times the width of the star, so when it covers the star there
is no corona, no ring of light and no glare — its edge against the sky
is a plain hard edge. Daylight ends and begins again as a LEVEL CHANGE
and never as a moving shadow: no line crosses the ground, no edge
sweeps, no vignette opens or closes, no colour grade shifts, and every
edge in the frame stays exactly where it is. Exactly one human in every
frame, in the film's only lead-grey suit with dusty teal seams, with a
completely flat back and an optically clear, unreflective helmet bubble
that never opens, closes or tints. The air is thin, 9 kilopascals:
razor-edged absolutely black shadows with no fill, no haze, no mist, no
scattering, no suspended dust, no visible beam of light in the air, and
no sound outside the suit. The plain carries no equipment, no marking
and no structure of any kind, so no text of any kind appears on screen
at any moment.
```

---

## 📋 QA SPEC — AYRI DOSYADA [Ders 117]

> ⛔ SPEC bir DOSYADIR, bölüm değil. Bu filmin QA SPEC'i:
> **`THE_NEAR_PASS_QA_SPEC.md`** (bu klasörde, filmin yanında).
> QA anında operatörün eline iki dosya verilir: rubrik + o SPEC.
> Buraya kopyalanmaz — bir sayıyı iki yerde tutmak, birini yanlış
> tutmaktır [AGENTS kural ①].

---

## ✅ Tutarlılık Kontrol Listesi

```
□ Karakter bloğu 6 görsel promptta birebir aynı mı?
□ "Scene N of 6" 6 promptun 6'sında doğru mu?
□ Klip süresi ÜRETİMDEN ÖNCE ffprobe ile ölçüldü mü [D124]?
  Ölçülen sayı 10,005 değilse bütün zaman damgaları yeniden yazıldı mı?
□ PALL'ın tırmanışı SÜRE + PİKSEL olarak yazıldı mı, açısal hız
  olarak DEĞİL [D127①]?
□ "its lower edge has risen almost the full height of the standing
  woman" ya da sayısal eşdeğeri her tırmanış tarifinde var mı [D127②]?
□ Yıldız aralığı sayacı S1-S2-S3'te sırayla daralıyor mu (236→159→67→0)?
□ Kapanma 1,2 s ve açılma 0,94 s promptlarda SANİYEYLE yazılı mı?
□ "the light level drops/rises everywhere at the same time" +
  "every edge stays exactly where it is" + "nothing sweeps across the
  ground" üçlüsü S3 ve S5'in üç promptunun üçünde de var mı?
□ "no corona, no ring of light, no diamond ring" S3-S4-S5'te var mı?
□ "no visible beam of light in the air" lambalı üç promptta var mı?
□ "rigid, matte, single-piece" + "never tumbles, never rotates, never
  drifts sideways" 12 promptun 12'sinde var mı?
□ HUMAN COUNT LOCK cümlesi 6 görsel + 6 video promptunda var mı?
□ "completely flat back" + "optically clear" [D79] her promptta var mı?
□ "No slow motion, no speed ramp" 12 promptun 12'sinde var mı?
□ "absolutely zero camera movement" 6 video promptunun 6'sında var mı?
□ Yürüyüş yalnız S2'de mi ve hızı (1,1 m/s) yazılı mı?
□ Toz, duman, kıvılcım, enkaz, düşen nesne hiçbir promptta var mı?
  (olmamalı — Kart 6 tasarımla kapatıldı)
□ Kadının gölgesi 2,98 m ve S0 ile S5'te AYNI mı [D42]?
□ Okra aşınma (diz, sol önkol, iki bot burnu) 6/6 aynı yerde mi?
□ Turkuaz dikiş TAM 1 kişide mi; kadranda başka soğuk doygun renk yok mu?
□ Hiçbir figür alt 1/4'e ya da sağ şeride giriyor mu?
□ Tohum (S0 06,2-07,0 · soluk çatlak ağı) ve karşılığı (S4 46,0-49,0 ·
  açılan yarıklar) yazılı mı?
□ Döngü jesti iki uçta da var mı (S0 eldiven alından İNİYOR ·
  S5 eldiven alna ÇIKIYOR)?
□ B (I2V) promptları karakteri/ortamı yeniden tarif ETMİYOR mu?
□ Üretim S0'dan başladı mı? PALL orada tırmanmadan devam edilmedi mi?
```

---

## ✅ ÜRETİM ÖNCESİ KONTROL — 12 madde (03_PLAN_ONCESI_KONTROL_LISTESI)

```
ÜRETİM ÖNCESİ KONTROL — THE NEAR PASS             tarih: 25.08.2026

A1 ✅ "no text" ile ekran içeriği aynı dosyada YOK — düzlükte insan
      yapımı tek nesne yok, suit yamasız, kask işaretsiz, ekran yok:
      kadrajda yazı üretebilecek TEK BİR NESNE YOK. Sayaç metinsiz üç
      kanalda: PALL'ın boyu/yüksekliği · yıldız aralığı · ışık seviyesi
      [Kart 5 çözümü]
A2 ✅ sahne sayısı: başlık 6 = blok 6 = "Scene N of 6" 6
A3 ✅ süre: 6 sahne × 10 s = 60 s = iddia edilen süre; ızgara ölçülmüş
      klip süresinden kuruldu [D124] ve ölçüm komutu §Genel Kural 2'de
A4 ✅ yasaklı sahne tipi taraması yapıldı:
      · araç/kapak biniş-inişi [D69] → araç 0 kare, film tamamen yaya
      · loş iç mekâna giriş [D69] → iç mekân 0 kare
      · aynalı/yansıtıcı yüzey [D20/D69] → vizör sıfır yansıma;
        düzlükte su, cam, metal, ayna 0 kare
      · türetilmiş optik fenomen novum [D73] → taşıyıcı KATI: 52 km'lik
        kaya. Işık olayı taşıyıcı değil, kayanın sonucu
      · yokluk novum [D76] → değil: kural altı sahnede de GÖRÜNÜR bir
        cisimle kanıtlanıyor
      · jenerik/başlık kartı [D34/D70/D72] → 0 saniye
      · insansız sahne [Kart 10] → 0 sahne
B1 ✅ doruk anı S5'in İÇİNDE tarif edildi (ışığın 0,94 saniyede geri
      gelmesi + kanıtın silinmesi + döngü jesti, tek çekimde ve zaman
      damgalı); iki sahne arasına düşmüyor
B1b ✅ katmanlı dünya YOK — tek düzlük, tek irtifa. Kart 6b
      tetiklenmiyor. Yine de IŞIK TAKVİMİ yazıldı (§Lighting Bible):
      iki geçiş, saniyesiyle
B2 ✅ bedelli seçim S4 · 42,8-43,2 s; kayıp AYNI SAHNEDE görülüyor
      (ışık dairesi ve yarık çizgisi birlikte söner) ve S5'te kalıcı
      (botlar çizginin üstünde, oynamamış) [D72]
C  ✅ 6 sayısal kilit yazıldı:
      insan (1 × 6 sahne · turkuaz TAM 1) ·
      kask (kapalı 6/6 · D79 düz sırt + berrak vizör her promptta) ·
      ölçü (uydu 60×50×44 km · irtifa 150 km · yarık 4 m × 30 m ·
            lamba dairesi 2 m · gölge 2,98 m · yürüyüş 8 m) ·
      yerçekimi (0,62 g = 6,08 m/s²) ·
      sıvı (0 kare) · canlı (0 kare)
D  ✅ risk sayımı: 4/12 — EŞİĞİN ALTINDA. Kart 3 · 4 · 5 · 9.
      Kart 6 tetiklenmiyor (toz/duman/enkaz/patlama 0 kare — tasarım
      kararı, ilk taslaktaki toz filamenti ÇIKARILDI);
      Kart 1/2/6b/7/10/11 konseptte yok.
      ⭐ Gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı:
      BÜYÜK GÖK CİSMİNİN EKRANDA HAREKET ETMESİ [D127 tekrarı],
      ve ikincisi: tutulmanın BULUT GÖLGESİ olarak üretilmesi
E  ✅ QA SPEC ayrı dosyada: THE_NEAR_PASS_QA_SPEC.md [D117]
```

---

## 🚪 KAPI KAYDI [DERS 74]

> Kaydı olmayan kapı, koşulmamış kapıdır. Aşağıdaki satırlar üretim
> ilerledikçe DOLDURULUR; boş kalan satır "geçti" anlamına gelmez.
> ⛔ IRON SLOPE'un kaydı bu tablonun neden var olduğunu gösteriyor:
> S0 kapısı yazılıydı, koşulmadı, ve düşecekti.

| Tarih | Kapı | Ölçülen | Sonuç |
|---|---|---|---|
| 25.08.2026 | prompt_kontrol.py | 12 prompt (6 image + 6 video A) + 6 B sürümü | ✅ **GO · 0 BLOCK · 0 FIX** — ilk koşu ⛔ **1 BLOCK** verdi: 6 görsel + 6 video promptunda **dünya-uzayı yön kelimesi** (doğu/batı/kuzey/güney). Hepsi ekran uzayına çevrildi; ayrıca 4 çapasız `toward` çapalandı, 6 video promptuna `no cuts within the shot` imzası eklendi, 2 video promptu banda çekildi |
| — | **⓪ KLİP SÜRESİ KAPISI [D124]** — tek test klibi | `ffprobe … format=duration` | ⬜ **ÜRETİMDEN ÖNCE.** 10,005 değilse bütün zaman damgaları yeniden yazılır |
| — | **① S0-ÖNCE ÜRETİM KAPISI — PALL TIRMANIYOR MU [D127 · D125]** | 0,0 ve 10,0 saniye karelerinde PALL'ın alt kenarının piksel farkı | ⬜ **≥100 px (tasarım 132 px) DEĞİLSE FİLM ÜRETİLMEZ.** Ayrıca üst kenar 6. saniyeye kadar kadrajı terk etmiş olmalı |
| — | Tek-kare fizibilite [D73] — S0 görsel promptu tek başına | tek karede "bu bir kaya ve çok yakın" okunuyor mu; kavisli alt kenar çıkıyor mu | ⬜ |
| — | **② ANAHTAR KAPISI [D125]** — S3, 6,1-7,3 s | düzlüğün ortalama parlaklığı 2,0 saniye içinde ≥%85 düşüyor mu; kadrajda süpüren bir kenar VAR MI | ⬜ **Yumuşak/süpüren/vinyet çıkarsa sahne reddedilir.** Ölçüm: `ffmpeg -i S3.mp4 -vf "crop=1080:200:0:1250,signalstats" -f null -` |
| — | **③ BAKIR KAPISI** — S4, 6,0-10,0 s | disk kenarı ORTASINDAN parlak mı; çatlak ağı açılıyor mu; düzlük aydınlanıyor mu (aydınlanmamalı) | ⬜ |
| — | Klon kapısı [D20/D69] | ikinci insan biçimi, silüet ya da yansıma var mı | ⬜ |
| — | Yürüyüş kapısı [D18] — S2 | her bot kalkıyor-basıyor-yük alıyor mu; kayma var mı; toz kalkıyor mu (kalkmamalı) | ⬜ |
| — | Döngü kapısı — S5 son karesi ↔ S0 ilk karesi | jest, ışık durumu ve palet eşleşiyor mu | ⬜ |
| — | 120 px kapak testi | açık şerit / jilet çizgi / koyu kütle ayrışıyor mu | ⬜ |
| — | Kurgu kapısı [D70/72/124] | 6 klip · 6 × ölçülen klip süresi ± 0,5 s · ekran metni 0,0 sn | ⬜ |
| — | ⑪ ÖLÇÜM KAPISI [D125] | süre · kesme ızgarası · sessizlik · en-boy | ⬜ |
| — | Negatif blok kapısı | `no second moon` · `no patch, no logo` · `zero camera movement` · `no ring of light` | ⬜ |

### 📏 PROMPT UZUNLUKLARI — dürüst kayıt (25.08.2026)

```
VIDEO (A sürümü, 6 prompt)   2.402 - 2.594 karakter
  → §7 hedef bandının (2.000-2.600) İÇİNDE, 6/6. Veo tavanının
    (~4.300) çok altında. İlk koşuda S2 ve S3 videoları 2.643 ve 2.873
    ile bandın üstündeydi; kuyruk artıkları ve tasvir tekrarı
    kısaltıldı, SAYISAL KİLİTLERE DOKUNULMADI.

IMAGE (6 prompt)             5.486 - 5.857 karakter
  → ⚠️ Betiğin bandı (1.700-2.100) depodaki hiçbir filmle uyuşmuyor ve
    betik bunu "bulgu değil GÖZLEM" sayıyor. Emsaller: THE QUIET IMPACT
    4.577-5.644 · THE STRAIGHT LINE 5.421-5.669 · THE IRON SLOPE
    5.023-5.651 — üçü de üretildi, hiçbiri uzunluktan reddedilmedi.
    ⚠️ DÜRÜST KAYIT: bu dosyanın TAVANI (S3 görseli, 5.857) emsallerin
    en yükseğinden 188 karakter YUKARIDA. Sebep S3'ün iki ışık durumunu
    (tam gündüz ve tam tutulma) aynı promptta taşımasıdır ve bu
    kısaltılamaz — sahnenin işi geçişin kendisidir.

⛔ İLK RED GELİRSE KISALTMA SIRASI — bu sırayla, tek tek:
  ① NEGATIVE kuyruğundaki ikiz çiftler ("no mist" yanında "no fog";
    "no meteor" yanında "no trail")                  → ~120 karakter
  ② karakter bloğunun yüz-detay cümlesi (kaş, yara izi, dudak)
                                                     → ~180 karakter
  ③ ENVIRONMENT'taki gökyüzü tekrarı (her promptta "deep, dark
    daylight blue with no cloud…")                   → ~90 karakter
  ⛔ SAYISAL KİLİTLER HİÇBİR KOŞULDA KISALTILMAZ:
    tırmanış cümlesi (süre + piksel + kendi eni) · kapanma 1,2 s ve
    açılma 0,94 s · "level change, not a moving shadow" üçlüsü ·
    "no corona, no ring of light" · mesafeler ve ölçüler.
    Bu filmde sayılar fiziğin kendisidir.
```

> **Üretim sırası:** ① **S0** (PALL tırmanıyor mu — novumun ilk ve tek
> ön koşulu) → ② S3 (anahtar — filmin en pahalı 1,2 saniyesi) →
> ③ S4 (bakır + çatlak ağı) → ④ S5 (geri açılma + döngü) → ⑤ S1 →
> ⑥ S2.
> **S0 temiz çıkmadan hiçbir sahne üretilmez** [D74 · IRON SLOPE emsali].

---

**THE NEAR PASS — Yakın Geçiş**
_"Gün burada batmaz — kapanır."_
