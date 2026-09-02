# 🔚 FİNAL VE PAYLAŞIM KILAVUZU — Son Sahne Hangi Davranışı Satın Alır

> **Neden var (22.08.2026):** Hikaye tablosunda **Tutundurma** hiçbir filmde
> 6.5'i geçmiyor; **Final** sütununda Blind Return 3, Last Shift 3, Ring Light
> 4, Cold Burn 4 var. `HOOK_VE_ILK_SAHNE_KILAVUZU.md` filmin ilk iki sahnesini
> yönetiyor, **son sahnesini yöneten hiçbir belge yoktu.** Oysa izlenme
> algoritmaya izlenme olarak değil; paylaşım, yorum ve tekrar izleme olarak
> döner — ve bu üç davranışın üçünü de FİNAL TİPİ belirler.
>
> **Ne zaman okunur:** vuruş tablosundan sonra, sahne haritası yazılırken —
> §3 tohum bilgisi ilk %10-15'lik dilime yerleşir, yani final kararı filmin
> BAŞINI da değiştirir. Üretimden sonra eklenemez.
> Kaynak: `araştırmalar/8.md` (22.08.2026 final tasarımı ve davranış araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① SAYILAR DIŞ ARAŞTIRMADAN GELİR, bu serinin ölçülmüş sonucu değildir.
   Test ölçütü: Final ve Tutundurma sütunları. Ölçüm tarafı
   YAYIN_VE_PERFORMANS_KILAVUZU.md §2'de; eşikler orada TEK kez durur,
   bu dosya onları tekrarlamaz.

② DEPONUN DÜŞÜK FİNAL SKORLARININ ÇOĞU KURGUNUN PUANIDIR [D62 · D72].
   Bu kılavuz iyi bir final TASARLATIR; o finalin kurguya girmesini
   sağlayan kapı ayrıdır (KURGU_VE_TESLIM §1). İyi tasarlanmış ama
   kurguya girmemiş final, kötü finalden daha pahalıdır.

③ LOOP BU DOSYADA İCAT EDİLMİYOR. Kusursuz döngünün üretim kuralları
   SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md §5'te (5 madde) ve dikey tarafı
   DIKEY_MIKRO_DRAMA_KILAVUZU.md §5'te. Burada yalnız KARAR var: hangi
   film hangi final tipini alır.

④ MUĞLAKLIK BEDAVA DEĞİLDİR. Muğlak final yorum getirir ama boşluk
   fazla açılırsa izleyici aldatıldığını hisseder ve paylaşmaz. §1'deki
   güven bandı bu kılavuzun en sık ihlal edilecek maddesidir.
```

---

# 1. 📉 BİLGİ BOŞLUĞU BANDI — merak ters U'dur

**Mekanizma:** Merak, bilgisizlikten değil **kısmi bilgiden** doğar. İzleyici
hiçbir şey anlamıyorsa merak etmez (savunmaya geçer); her şeyi anlıyorsa da
merak etmez (doyar). Merak, izleyicinin anlama güveni orta bandtayken zirve
yapar. Bu seride güven ayarının tek aracı **kadrajda ne gösterildiğidir** —
replik ve metin yok.

| Boşluk hacmi | İzleyici güveni | Tepki | Ekrandaki karşılığı |
|---|:--:|---|---|
| çok dar (her şey açık) | yüksek | sıkılma → anında kaydırma | karakter yürüyor, olay yok, sonuç belli |
| **optimum** | **orta** | **merak, açık döngü** | **ipucu görünür, sonuç gizli** |
| çok geniş (rastgele) | düşük | aşırı yük → orta nokta terki | bağlantısız olaylar, nedensiz kopukluk |

```
SAYISAL KİLİT
  □ AÇILIŞ SORUSU   ilk 3 saniyede izleyicinin zihninde TEK net soru
                    oluşmalı ("vizöre neden dışarıdan farklı ışık
                    vuruyor?") — soru sayısı 1, iki değil
  □ CEVAP DAĞILIMI  cevap ardışık parçalara bölünür; her 8-10 s'lik
                    blok yeni ve SINIRLI bir görsel ipucu taşır
  □ AÇIK KALAN      film bitince cevaplanmamış soru sayısı: 1
                    (0 = kapalı final bedeli · 2+ = aldatılma hissi)
```

---

# 2. 🎬 FİNAL TİPİ SEÇİMİ — dört tip, dört davranış

**Mekanizma:** Son saniyeler izleyicinin motor davranışını satın alır.
Algoritma bu davranışları eşit saymaz: **paylaşım > kaydetme > yorum >
beğeni.** Paylaşım, izleyicinin kendi itibarını içeriğe kefil etmesidir;
bu yüzden en pahalı ve en değerli sinyaldir.

| Final tipi | Tetiklediği mekanizma | Aldığı davranış | Bu hattaki uygulanabilirlik |
|---|---|---|---|
| **Kapalı** (çözümlenmiş) | bilişsel doyum, kapanış | anında kaydırma | ⛔ tek başına kullanılmaz |
| **Muğlak** (açık uçlu) | anlam üretme, çelişki | **yorum** + kalma süresi | ✅ ikilem görsel kurulursa |
| **Tersine dönüş** (twist) | yüksek uyarım, valans kayması | **paylaşım** + kaydetme | ✅ tohum bilgi varsa |
| **Döngü** (loop) | Zeigarnik — tamamlanmamış görev | **tekrar izleme** | ✅ dikeyde zorunlu, yatayda seçenek |

```
KARAR KURALI — plana "FİNAL TİPİ" satırı yazılır

  dikey shorts (48 s)   DÖNGÜ zorunlu · üzerine TWIST eklenebilir
  2-4 dk                TWIST veya MUĞLAK · döngü opsiyonel
  3-5 dk                TWIST + tohum bilgi (en yüksek getiri)
  7-9 dk                MUĞLAK — uzun formda twist'in bedeli, izleyicinin
                        7 dakikalık yatırımının boşa çıkma riskidir
  fragman               hiçbiri — fragmanın işi çözmemektir (FRAGMAN §1.2)
```

> ⚠️ **Kapalı final yasak değil, bedelli.** Seride bir filmin kapanması
> gerekiyorsa (seri kapanışı, tematik zorunluluk) kapalı final yazılır ve
> plana bedeli not edilir: bu film paylaşım değil, güven satın alır.

---

# 3. 🌱 TOHUM BİLGİ — finalin faturası filmin başında ödenir

**Mekanizma:** Twist veya döngü, ancak finali meşru kılan bir **önceden
ekilmiş ipucu** varsa tekrar izleme üretir. Tohum yoksa izleyici finali
"ucuz kandırma" sayar ve terk eder. Tohum aşırı belirgin verilirse boşluk
anında kapanır ve merak hiç doğmaz. Doğru yer dardır ve hesaplanabilir.

```
SAYISAL KİLİT
  □ YERLEŞİM     filmin ilk %10-15'lik dilimi
  □ SÜRE         2 saniyeyi geçmez — görünür ama anlamlandırılamaz
  □ TAŞIYICI     çevrede: duvarda titreyen bir şey, vizörde asimetrik
                 yansıma, zeminde tekrarlayan bir iz
                 ⛔ karakterin bakışıyla vurgulanmaz (vurgu = cevap)
  □ GERİ DÖNÜŞ   final, tohumun BULUNDUĞU yere görsel olarak geri döner
```

| Format | Toplam | Tohum penceresi | Not |
|---|:--:|:--:|---|
| dikey shorts | 48 s | **5-7 sn** (S0 sonu / S1 başı) | hook kapandıktan hemen sonra |
| 2-4 dk | ~150 s | **15-22 sn** | ~S2 |
| 3-5 dk | ~250 s | **25-38 sn** | ~S3 |
| 7-9 dk | ~480 s | **48-72 sn** | faz 1 içinde |

> Çalışma belleği 40-50 saniye sonra o kareyi net hatırlamaz — tekrar izleme
> tam olarak bu hatırlayamamadan doğar. Tohum çok net verilirse izleyici
> hatırlar ve başa sarmaz.

---

# 4. ⚖️ YORUM: İKİLEM MI, YEM Mİ

**Mekanizma:** Algoritma yorum sayısını değil **yorum derinliğini** okur:
kullanıcıların birbirine cevap verdiği uzun iplikler ödüllendirilir; kısa,
tekrarlayan, bağlamsız yorumlar "düşük kalite" etiketlenir. Bu seride yorum
yemi zaten teknik olarak imkânsızdır (ekran metni yok, seslenme yok) — geriye
tek meşru yol kalır: **görsel ahlaki/mantıksal ikilem.**

```
İKİLEM İNŞASI — üç şart birden

  ① Karakter, kadrajda görünen bir BEDELİ kendi eliyle ödüyor
     (yedek hücre · oksijen · görüş · zaman)
  ② Karşılığında aldığı şey izleyiciye TARTIŞMALI geliyor
     (bir makine, bir bitki, bir yabancı, bir kayıt)
  ③ Film bu tercihi ONAYLAMIYOR da KINAMIYOR da — kamera yargısız

  ✅ sonuç: izleyici kutuplaşır, birbirine cevap verir, iplik uzar
  ⛔ ikilem repliğe veya karta bağlanırsa: metin yasağı ihlali [D45]
```

> Deponun elindeki en yakın örnek **CENTRAL CHOICE** yuvasıdır (Blind Return
> S11: görüşü nefese takas). O sahne zaten bir ikilemdi; skoru düşüren şey
> ikilemin yokluğu değil, **bedelin taşıyıcı kodasının kurguda bozuk blokta
> kalmasıydı.** İkilem kurulur, bedel GÖRÜLÜR, ikisi de kurguya girer.

---

# 5. 💥 PAYLAŞILAN DUYGU — huşu veya kaygı, ikisinin arası değil

**Mekanizma:** Paylaşımı yüksek uyarımlı duygular tetikler: huşu, hayranlık,
kaygı, öfke. Düşük uyarımlı duygular (hüzün, tatmin, sükûnet) izlettirir ama
paylaştırmaz. İzleyici paylaşırken içeriği değil **kendi kimliğini** yayınlar.

> ⭐ **27.08.2026 — DOĞRULANDI VE AYRIŞTIRILDI (araştırma 3).**
> Bu bölümün "huşu VEYA kaygı, ikisi zıt valanstadır" kuralı ayakta.
> Yeni olan şu: **iki kol aynı davranışı satın almıyor.** Xi vd. (2024),
> *International Journal of Electronic Commerce*, 102.031 Douyin videosu —
> ayrık duygular etkileşimi bölüyor:
>
> | Duygu | Satın aldığı davranış |
> |---|---|
> | **Huşu / hayranlık** | **Paylaşım** (huşu içerikleri ~%34 daha hızlı yayılıyor) |
> | **Kaygı / gerilim** | **Kaydetme + yorum** — paylaşım DEĞİL |
> | **Şaşkınlık** | **Yorum + tekrar izleme** |
> | Hüzün | üçünü de birden baskılıyor (paylaşım −%16) |
>
> **Karar kuralı buradan çıkar:** hangi kolun seçileceği estetik değil,
> **hangi metriğin istendiği** sorusudur.
> ```
> Paylaşım istiyorsan          → HUŞU yuvası (ve final tipi TWIST, §2)
> Yorum ve kaydetme istiyorsan → KAYGI yuvası (ve final MUĞLAK, §2)
> Tekrar izleme istiyorsan     → ŞAŞKINLIK (ve final DÖNGÜ, §2)
> ```
> ⚠️ **VE BERGER-MILKMAN MODELİNİN KISA VİDEODA ÇÖKEN YANI:** "düşük
> uyarım viraliteyi öldürür" tezi kısa dikey formatta geçersiz. Düşük
> uyarımlı içerik (ASMR sınıfı) bilişsel yükü düşürüyor, kaydırmayı
> yavaşlatıyor, döngüye giriyor ve algoritma bunu ödüllendiriyor.
> Yani deponun sakin kaydı erişimi öldürmüyor — **paylaşım yerine
> tekrar izleme satın alıyor.** Bu meşru bir stratejidir ama plana
> yazılması gerekir; farkında olunmadan seçilirse film "kimse
> paylaşmadı" diye başarısız sanılır.

```
SAYISAL KİLİT — her filmde en az bir PAYLAŞIM SAHNESİ

  □ HUŞU YUVASI     ölçek kontrastı 1:10 + tek yönlü hüzme ışık
                    (KARAKTER_VE_DUYGU §5.1 ile aynı sahne olabilir)
  □ VEYA KAYGI YUVASI  daralan mekân + vizör içinde sayaç/renk dönüşü
                    + ritmik nefes (SES_VE_DIYALOG §5 ortam yatağı)
  □ KONUM           doruk yuvası veya bir önceki sahne — finalin
                    içinde DEĞİL (final tipi ayrı iş yapar)
```

> ⚠️ Aynı sahne hem huşu hem kaygı taşıyamaz; ikisi zıt valanstadır ve
> izleyici hangisini paylaştığını bilemez. Filmin imzası ikisinden biridir.

---

# 6. 🧩 TWIST + DÖNGÜ BİRLEŞİMİ — en yüksek getirili kombinasyon

```
YAPI
  0-3 sn        açılış sorusu (tek soru) · ihlal kadrajda görünür
  %10-15        tohum bilgi ekilir (§3)
  orta          novum ikinci nesnede doğrulanır (ONERME_VE_NOVUM §5)
  doruk         paylaşım sahnesi: huşu VEYA kaygı (§5)
  son 2 kesme   twist — mekânın/ölçeğin doğası değişir
  son kare      ilk kareye görsel + işitsel oturur (döngü)

SONUÇ ZİNCİRİ
  twist  → paylaşım      (yüksek uyarım)
  döngü  → tekrar izleme (Zeigarnik)
  tohum  → başa sarma    (doğrulama ihtiyacı)
  ikilem → yorum ipliği  (kutuplaşma)
```

> ⛔ **Jenerik kartı bu yapının katilidir** [D70 · SENARYO_VE_VIRAL §5④]:
> hem metin ihlali, hem son kare ile ilk kare arasındaki bağın ölümü.

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Kapalı finalde "karakter kaskını/vizörünü çıkarır, yüz görünür" | Ekipman durum kilidi [D37 · D57]. Kapanış vizör AÇILARAK verilemez; karşılığı vizör içi aydınlatmadır (KARAKTER_VE_DUYGU §1). |
| Yorum tetiklemek için ekranda soru/çağrı | Metin yasağı mutlak [D13 · D45]. Yorum yalnız §4 görsel ikilemiyle alınır. |
| "Part 2" beklentisi yaratan yarım bırakma | Dikey içerik bağımsız olmak zorunda (DIKEY_MIKRO_DRAMA §6): dönüşüm oranı düşük, yarım bırakılan hikâye izleyici kaybettirir. |
| Twist için ani renk/palet kırılması | Novum taşıyıcı kuralı (ONERME_VE_NOVUM §2) — twist somut nesne/ölçek değişimiyle verilir, palet kaymasıyla değil. |
| Muğlaklığı "hiç cevaplamayarak" büyütmek | §1: açık kalan soru sayısı 1. İki ve üzeri, aldatılma hissi ve paylaşım kaybı demektir. |
| Yorumları okurken videonun arkada dönmesine güvenmek | Bu bir dağıtım davranışı; plana yazılabilir bir tasarım kararı değil. Ölçümü YAYIN_VE_PERFORMANS'ta. |

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 8 maddesi

```
□ 1. FİNAL TİPİ satırı plana yazıldı mı (§2 karar kuralı)
□ 2. Açılış sorusu TEK mi — ilk 3 saniyede hangi soru doğuyor
□ 3. Film bitince açık kalan soru sayısı 1 mi
□ 4. TOHUM BİLGİ hangi sahnede, kaç saniye, hangi taşıyıcıda (§3)
□ 5. Final, tohumun bulunduğu yere görsel olarak dönüyor mu
□ 6. İKİLEM üç şartı da sağlıyor mu — bedel kadrajda görünüyor mu (§4)
□ 7. PAYLAŞIM SAHNESİ belirlendi mi: huşu mu kaygı mı (ikisi değil)
□ 8. Final sahnesi kurgu kapısının KESİLEMEZ listesinde mi [D62]
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/8.md                      bu kılavuzun kaynak araştırması (22.08.2026)
HOOK_VE_ILK_SAHNE_KILAVUZU.md          §6 vaat-teslim · ilk iki sahne (bu dosyanın karşı ucu)
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md    §5 kusursuz döngü — üretim kuralları
DIKEY_MIKRO_DRAMA_KILAVUZU.md          §5 dikeyde döngü mimarisi · §6 bağımsızlık
ONERME_VE_NOVUM_KILAVUZU.md            §5 kural tekrarı — twist'in meşruiyeti
KARAKTER_VE_DUYGU_KILAVUZU.md          §5 huşu / hüzün-umut · bedel görünürlüğü
SES_VE_DIYALOG_URETIM_KILAVUZU.md      §5 ortam yatağı — kaygı yuvasının nefes hattı
KURGU_VE_TESLIM_KILAVUZU.md            §1 kurgu kapısı — finalin ekrana girmesi
YAYIN_VE_PERFORMANS_KILAVUZU.md        §2 eşikler · §6 geri besleme (sayılar orada durur)
FRAGMAN_KILAVUZU.md                    §1.2 spoiler kapısı — final fragmana girmez
DERSLER/07_KURGU_VE_ANLATI.md          D62 · D70 · D72 tam metin
```
