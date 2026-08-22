# 🎚️ KURGU RİTMİ VE İHRAÇ KILAVUZU — Hook'tan Sonraki Her Saniye

> **Neden var (22.08.2026):** `KURGU_VE_TESLIM_KILAVUZU.md` §1 madde ⑤
> *"ASL = süre ÷ çekim sayısı → SPEC'teki hedef bandın İÇİNDE"* diyor —
> ama o bandın NE OLDUĞUNU söyleyen hiçbir belge yoktu. Aynı şekilde
> §2 kırpma tablosu istiyor, kırpmanın HANGİ yuvadan yapılacağını
> söylemiyor. Ve teslim edilen dosyanın ses/görüntü sayıları hiçbir
> yerde yazılı değildi. Bu dosya o üç boşluğun kaynağıdır.
>
> **İş bölümü — karıştırma:**
> ```
> KURGU_VE_TESLIM_KILAVUZU.md   KAPI  → "geçti mi?"  (sayım, kontrol, teslim sırası)
> BU DOSYA                      KAYNAK → "hangi sayıya göre?" (ritim tasarımı + ihraç)
> ```
>
> **Ne zaman okunur:** ① sahne haritası yazılırken (ASL bandı SPEC'e
> girer) ② kurguya oturmadan önce ③ ihraçtan önce.
> Kaynak: `araştırmalar/3.md` (22.08.2026 derin araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — sabit ızgara ile araştırmanın çatışması

```
① BU DEPONUN ASL'Sİ SABİTTİR VE ANLATI BANDININ ÜSTÜNDEDİR.
   Araştırmanın ölçtüğü optimal anlatı bandı 4-8 s; bu hattın sabit
   ızgarası 8 s (shorts · 7-9 dk) ve 10 s (2-4 · 3-5 dk) — yani bandın
   tavanında veya üstünde. Araştırmanın "belgesel/eğitim" olarak
   etiketlediği yer burasıdır.
   → Bu bilinçli bir seri kimliğidir (tek çekim · lockoff · sahne = klip)
     ve TEK KARE ÜRETMEDEN değiştirilemez.
   → Maliyeti ölçülmemiştir. Ölçülecek yer: YAYIN_VE_PERFORMANS §4
     (orta bölüm çöküşü eğrisi). Gerçek veri gelene kadar sabit ızgara
     KORUNUR; bu dosya sabit ızgarayı bozmaz, İÇİNDE çalışır.

② EĞRİ YALNIZ DEĞİŞKEN FİLMDE VARDIR.
   Sabit ızgaralı filmde (sahne = çekim = klip) ASL matematiksel olarak
   sabittir ve §1 eğrisi UYGULANAMAZ. Eğri, kırpma bütçesi olan filmin
   aracıdır [D100 · D101]. Sabit ızgaralı filmde ritmi taşıyan şey ASL
   değil, §2'deki KADRAJ İÇİ değişkenlerdir.

③ İHRAÇ SAYILARI (§6) DIŞ KAYNAKTIR AMA ÇATIŞMASIZDIR.
   Kodek, bitrate, LUFS ve true peak değerleri platform davranışına
   dayanır ve deponun hiçbir kuralıyla çelişmez — doğrudan uygulanır.
   Bu dosyanın en düşük riskli, en yüksek getirili bölümü budur.
```

---

# 1. 📐 ASL EĞRİSİ — kırpma bütçesi nereye harcanır

**Mekanizma:** İzleyici sabit bir ritme saniyeler içinde alışır; alıştığı
an aktif işlemeyi bırakır. Orta bölüm terkinin tek yapısal sebebi budur.
Eğri, kırpma bütçesini rastgele değil YUVAYA göre dağıtır.

```
YUVA (yüzde bandı)     HEDEF ASL      NE YAPILIR
─────────────────────────────────────────────────────────────────
① KANCA        0-%10    en kısa       ızgarada tek klip → kırpılmaz,
                                      ritim KADRAJ İÇİNDEN gelir (§2)
② ORYANTASYON  %10-30   4-6 s         ham klipler ~%40 kırpılır
③ ORTA BÖLÜM   %30-65   DALGALI       ⭐ en kritik yuva:
                                      3 kısa (2-3 s) → 1 uzun (7-8 s)
                                      sabit ASL YASAK
④ DORUK ÖNCESİ %65-85   İVMELENEN     her kesmede %20-30 kısalt:
                                      3 s → 2,5 → 2 → 1,5 → 1 → 0,5
                                      ⛔ bu rampa 10-15 s'yi AŞMAZ
⑤ ÇÖZÜLME      %85-100  8+ s          klipler TAM uzunlukta bırakılır,
                                      kırpma yok — duygusal karşılık
```

```
SPEC'E YAZILACAK İKİ SATIR (kurgu kapısı madde ⑤ bunu ölçer)
  TARGET ASL BAND: __ s – __ s        (film geneli)
  ASL CURVE:  ①__ ②__ ③__ ④__ ⑤__    (yuva başına hedef)

⛔ SABİT IZGARALI FİLMDE bu iki satır şöyle yazılır:
  TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, bilinçli sapma)
  Gerekçe satırı ZORUNLU [D74: kaydı olmayan kapı koşulmamış kapıdır].
```

## 1.1 Kırpma bütçesi dağıtım örneği

> `KURGU_VE_TESLIM_KILAVUZU.md` §2 tablosunun "nereden kırpılır"
> sütununu bu eğri doldurur.

```
18 klip × 10 s = 180 s ham · hedef 150 s → TRIM BUDGET 30 s

  ① kanca      S1        10 s → 10,0 s   (kırpma 0)
  ② oryantasyon S2-S5     40 s → 24,0 s   (klip başına ~4 s kırpma)
  ③ orta       S6-S12     70 s → 62,0 s   (3 kısa + 1 uzun dalgası)
  ④ doruk önü  S13-S16    40 s → 24,0 s   (ivmelenen rampa)
  ⑤ çözülme    S17-S18    20 s → 20,0 s   (kırpma 0)
                          ────────────────
                          180 s → 140 s + hook payı ≈ hedef
```

⚠️ Kırpma, klip DÜŞÜRMEK değildir. Süre tuttuğu için kayıp görünmez —
Last Shift'te tam bu oldu [D100]. Kırpma tablosu klip başına tek satır
yazılır; satırı olmayan klip kırpılmamış sayılır.

---

# 2. ⚡ ÖRÜNTÜ KIRICILAR — lockoff'ta hangileri mümkün

**Mekanizma:** Beyin aynı kadraja, aynı palete, aynı ritme saniyeler
içinde alışır. Alışma anında retention kırılır. Örüntü kırıcı, dikkati
zorla sıfırlar.

```
SIKLIK KİLİDİ
  MİKRO  her 10-15 s'de bir  → ölçek veya ışık değişimi
  MAKRO  her 30-40 s'de bir  → mekân veya tempo değişimi

SABİT IZGARADA KARŞILIĞI (klip süresi 8-10 s)
  MİKRO = HER KESME bir örüntü kırıcı TAŞIMAK ZORUNDA
  MAKRO = her 3-4 sahnede bir mekân/tempo değişimi
```

| Kırıcı | Bu seride | Nasıl |
|---|:--:|---|
| **Plan ölçeği sıçraması** | ✅ | Geniş → ekstrem yakın sert kesme. Lockoff bozulmaz, sadece kadraj değişir. En ucuz ve en güçlü araç. |
| **Renk/ışık paleti dönüşümü** | ✅ | Desatüre soğuk blok → doygun kırmızı acil aydınlatma. Işık kilidi bozulmaz, sahne kartına yazılır. |
| **Ses dokusunun değişmesi** | ✅ | Ambiyans katmanının karakteri değişir (uğultu → basınç tıslaması). §3 ile birlikte çalışır. |
| **Mekân değişimi** | ✅ | Makro kırıcı. Ekran yönü kuralları geçerli (UZAMSAL_HARITA). |
| **Öznenin kadrajdan çıkması/girmesi** | ✅ | Boş kadraja giriş, lockoff'un kendi dili. |
| **Kamera dili değişimi (handheld'e geçiş)** | ❌ | Negatif çekirdek: no camera shake / no handheld. |
| **Whip pan · crash zoom zinciri** | ❌ | Çekim başına tek sürekli hareket kuralı (SENARYO_VE_VIRAL §1'de zaten reddedildi). |
| **Hız rampası (speed ramp)** | ❌ | Kurguda hız ince ayarı en çok %2-4 [KURGU_VE_TESLIM §3]. |

```
⛔ SAHNE HARİTASI KAPISI: ardışık İKİ sahne aynı ölçekte + aynı palette
   + aynı ses dokusundaysa örüntü kırıcı YOKTUR. Sahne haritası
   yazılırken üç sütun yan yana okunur:
     | sahne | ölçek | palet | ses dokusu |
   Üçü de değişmeyen ardışık çift = orta bölüm çöküşünün mimarisi.
```

---

# 3. 🔊 SES KÖPRÜLERİ — kliplerin arasındaki tutkal

**Mekanizma:** Ayrı üretilmiş iki klip arasında ışık, doku ve konum
farkı kaçınılmazdır. Görsel kopukluğu maskeleyen tek şey sestir: beyin
işitsel ipucunu görsel değişimden ÖNCE alırsa, iki klibi aynı uzam-zaman
sürekliliğinin parçası kabul eder.

> ⭐ Bu bölüm bu dosyanın **sürtünmesiz** kısmıdır: hiçbir üretim kısıtı
> yok, tamamen kurgu masasında yapılır, tek kare yeniden üretim
> gerektirmez. Cold Burn'ün Ortam **3/10** skoru ve `AUDIBLE DRIFT`
> teşhisi doğrudan burayı işaret ediyor.

```
① AMBİYANS YATAĞI — TEK PARÇA
   Kurgunun tamamına TEK ambiyans serilir; klip sınırında ölmez,
   sıfırlanmaz, seviye sıçraması yapmaz [D83 · KURGU_VE_TESLIM §4].
   Yatak kesilirse beyin bunu HATA veya mekân değişimi sayar.

② J-CUT (ses önden girer) — varsayılan geçiş
   Sonraki sahnenin sesi, mevcut görüntü hâlâ ekrandayken 1,0-1,5 s
   ÖNCE girer. Beyin görsel değişime hazırlanır; kopukluk kamufle olur.
   → ORYANTASYON ve ORTA BÖLÜM yuvalarında VARSAYILANDIR.

③ L-CUT (ses arkadan sarkar)
   Mevcut sahnenin sesi (yankı kuyruğu, makine rezonansı, replik sonu)
   yeni görüntünün üstüne 0,5-1,5 s taşar.
   → ORTA BÖLÜM ve ÇÖZÜLME yuvalarında kullanılır.

④ SERT KESME (ses ve görüntü aynı karede)
   Yalnız BİLİNÇLİ şok için: doruk vuruşu, ani kesinti, sistem ölümü.
   Filmin geneline yayılırsa her kesme bir mikro-şoktur ve yorgunluk
   birikir.
```

```
SAYISAL KİLİT
  □ Ambiyans kesintisi: 0 kesme
  □ Mutlak dijital sıfır: 0 saniye  (müziksiz ≠ sessiz [D83])
  □ J/L-cut oranı: kesmelerin ≥ %60'ı ses köprülü
  □ Sert kesme: film başına ≤ 3 bilinçli vuruş, hepsi plana YAZILI
```

---

# 4. 🥁 MÜZİK VURUŞUNA KESME (BEAT-CUTTING) — iki yerde, sadece iki

```
✅ KANCA yuvasında        enerji kurar
✅ DORUK ÖNCESİ son 5 s'de  metrik montajla birlikte
❌ Filmin geneline yayılırsa: beyin ritmi çözer, sürpriz ölür, kurgu
   mekanikleşir ve retention düşer. Anlatı bloklarında kesme müziğin
   vuruşunda değil, VURUŞ ARALARINDA veya harekette yapılır (cut on action).

TEMPO HİZASI: müzik BPM'i sahne uzunluğuna hizalanır — bu depoda zaten
  sayısal kilit olarak var: GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU §14
  (10 s sahne → 48/72/96/120/144 BPM).
```

---

# 5. 🎬 DORUK ÖNCESİ RAMPA — 8 s'lik klipten 0,5 s'lik kesme çıkar mı

```
ÇIKAR — ama SPEC'e önceden yazılırsa.
  Hat 8-10 s klip üretir; 0,5-2 s'lik kesmeler KURGUDA doğar.
  Bu sahneler plana "üretimde değil KURGUDA doğar" etiketiyle yazılır
  [KURGU_VE_TESLIM §2] ve üretim kapısı onları HAM hâliyle onaylar.

⛔ ÜÇ SINIR
  ① Rampa 10-15 saniyeyi aşmaz — aşarsa yorgunluk yaratır, gerilim değil.
  ② Rampanın içindeki her kesme yine bir SAHNE sınırıdır; sahne İÇİ
     kesme değildir [D1]. Yani rampa, planda ayrı sahneler olarak durur.
  ③ Rampadan sonra ÇÖZÜLME uzun planlarla gelir (8+ s). Rampa ile
     biten film, izleyiciyi karşılıksız bırakır.
```

---

# 6. 📦 İHRAÇ KONTROL LİSTESİ — sayılar

> Platform yüklenen her dosyayı yeniden sıkıştırır. Bu tablo, yeniden
> sıkıştırmadan en az zararla çıkmak içindir. Değerler dış kaynaktır (§0③).

## 6.1 GÖRÜNTÜ

| Parametre | Yatay 16:9 | Dikey 9:16 | Gerekçe |
|---|---|---|---|
| **Çözünürlük** | 2560×1440 veya 3840×2160 | 1440×2560 veya 2160×3840 | ⭐ 1080p yüklenen dosya düşük kaliteli kodeğe düşer. 1440p ve üzeri, platformu daha iyi kodeğe zorlar — kaynak 1080p olsa bile ölçeklenerek ihraç edilir. |
| **Kare hızı** | kaynağa sadık | kaynağa sadık | Ara değerleme (resampling/interpolation) YAPILMAZ. Progressive scan. |
| **Sarmalayıcı / kodek** | MP4 · H.265 (HEVC) veya H.264 | aynı | Sunucuya daha temiz master gider. |
| **Bit hızı** | 45-60 Mbps | 35-45 Mbps | Yeniden sıkıştırmaya karşı kalite tamponu. Gren ve ince doku burada hayatta kalır. |
| **Renk uzayı** | BT.709 / Rec.709 (Gamma 2.4) | aynı | SDR dönüşümünde renk kayması ve soluklaşmayı önler. |

## 6.2 SES

| Parametre | Değer | Gerekçe |
|---|---|---|
| **Kodek** | AAC-LC (veya Opus) | Platformun kayıpsıza en yakın işlediği format. |
| **Kanal / bit hızı** | Stereo 384 kbps · 5.1 için 512 kbps | Ambiyans yatağının frekans yoğunluğu ve LFE burada korunur. |
| **Örnekleme hızı** | 48 kHz | Senkron kaymasını (drift) önler. |
| **Integrated loudness** | **−14 LUFS** (kabul bandı −14 … −15) | ⭐ Platform hedefi −14 LUFS. Daha yüksek miks ZORLA KISILIR ve dinamik aralık ezilir. |
| **Max true peak** | **−1,0 dBTP** (veya −1,5) | Örnekler arası tepe noktaları yeniden kodlamada çatlamaya döner. |

```
⛔ EN ÖLÜMCÜL HATA: SESİ DÜŞÜK TESLİM ETMEK.
   Platform yüksek sesi kısar ama DÜŞÜK SESİ YÜKSELTMEZ. −19 LUFS
   teslim edilen bir film, kendinden önceki içeriğe göre cılız kalır;
   illüzyon çöker ve izleyici çıkar.
   Doğrulama: yayından sonra videoda "Stats for nerds" → Content
   Loudness değeri −1,0 dB ile 0,0 dB arasında olmalı. Pozitifse miks
   yüksek, çok negatifse miks düşük.
   → Bu değer YAYIN_VE_PERFORMANS tablosuna ilk 24 saatte yazılır.
```

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Kanca yuvasında ASL 1,5-2,5 s | Sabit ızgarada hook TEK kliptir (8-10 s). Karşılığı §2 kadraj içi yoğunluk + HOOK §2.2 "hareketin ortasında açılış". Değişken filmde §1 eğrisi bunu kısmen karşılar. |
| "İlk 30 sn'de 19 görsel değişiklik" | Sabit ızgarada 30 s = 3-4 klip. Fiziksel olarak imkansız. |
| Pattern interrupt olarak handheld / kamera sarsıntısı | Negatif çekirdek: no camera shake, no handheld. §2'de ✅ işaretli beş kırıcı bunun yerine geçer. |
| Speed-ramp ile sahne hızlandırma | Kurguda hız ayarı en çok %2-4 [KURGU_VE_TESLIM §3]; fazlası hareketi yapaylaştırır. Çözüm kırpma (§1.1). |
| Tüm filme yayılan beat-cutting | §4: öngörülebilirlik tuzağı. Yalnız kanca ve doruk öncesi son saniyeler. |
| Geçiş efektleri (crossfade/dissolve) ile yumuşatma | Sahne sınırı yalnız sert kesmedir; gizli geçiş ayrı ve şartlı bir tekniktir (TEK_CEKIM_VE_GIZLI_GECIS §5-8). Ses köprüsü (§3) bu işi görüntüye dokunmadan yapar. |

---

# 8. ✅ KONTROL LİSTESİ

```
SAHNE HARİTASI YAZILIRKEN
 □ SPEC'e TARGET ASL BAND + ASL CURVE satırları yazıldı
   (sabit ızgaraysa gerekçe satırı da yazıldı)
 □ Değişken filmse KIRPMA TABLOSU yuvalara göre dolduruldu (§1.1)
 □ Ardışık iki sahne aynı ölçek + palet + ses dokusunda DEĞİL (§2 kapısı)
 □ Makro örüntü kırıcı her 3-4 sahnede bir var
 □ Doruk rampası varsa o sahneler "kurguda doğar" etiketli

KURGU MASASINDA
 □ Ambiyans yatağı tek parça — 0 kesinti, 0 mutlak sıfır
 □ Kesmelerin ≥%60'ı J-cut veya L-cut
 □ Sert kesme sayısı ≤ 3 ve hepsi planda yazılı
 □ Beat-cutting yalnız kanca + doruk öncesi son 5 s
 □ Doruk rampası ≤ 15 s ve sonrası uzun planla çözülüyor
 □ ⭐ KURGU KAPISI koşuldu → KURGU_VE_TESLIM_KILAVUZU §1 (10 madde)

İHRAÇ ÖNCESİ
 □ Çözünürlük 1440p+ (kaynak 1080p olsa bile ölçeklendi)
 □ Bitrate bandında · BT.709 · kare hızı kaynağa sadık
 □ Ses: 48 kHz · AAC 384 kbps · −14 LUFS · −1,0 dBTP
 □ Kulakla dinlendi: doruk ve temas bölgesi (KURGU_VE_TESLIM §4)

YAYINDAN SONRA
 □ Stats for nerds → Content Loudness −1,0 … 0,0 dB aralığında mı
 □ Değer 08_YAYIN_PERFORMANS_TABLOSU.md satırına yazıldı
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/3.md                     bu kılavuzun kaynak araştırması (22.08.2026)
KURGU_VE_TESLIM_KILAVUZU.md           KAPI tarafı: birim sözlüğü · 10 maddelik kapı · teslim sırası
TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md  §5 sahne sınırı grameri · §6-8 gizli geçiş şartları
SES_VE_DIYALOG_URETIM_KILAVUZU.md     ses yazım tarafı · register
GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md  §14 tempo-sahne hizası · §16 seslilik
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md   §1 reddedilen kurgu teknikleri · §5 loop · §6 sahne sınırları
KARAKTER_VE_DUYGU_KILAVUZU.md         tepki planı bütçesi — ASL eğrisiyle aynı sahneleri harcar
YAYIN_VE_PERFORMANS_KILAVUZU.md       §4 terk noktasının eğri tarafı · Content Loudness kaydı
DERSLER/07_KURGU_VE_ANLATI.md         D83 ses sürekliliği · D100 kırpma · D101 birim ayrımı
```
