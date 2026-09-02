# 🧬 ÖNERME VE NOVUM KILAVUZU — "Bunu Daha Önce Görmedim" Mühendisliği

> **Neden var (22.08.2026):** Hikaye tablosunun **Özgünlük** sütunu 13 geçerli
> satırın 6'sında 4/10. `UZAY_SENARYO_KILAVUZU.md` §1 novumu "bu projenin en
> çok ihmal ettiği kavram" diye açıyor ama **seçim kuralı** vermiyor: hangi
> novum tipi bu hatta üretilebilir, taşıyıcısı ne olur, hangi test reddeder.
> **D73 bu açığın faturasıdır** — novum türetilmiş bir optik fenomene (çift
> gölge) yüklendi ve 64 saniyede **sıfır kare** çıktı.
>
> **Ne zaman okunur:** KONSEPT aşamasında — vuruş tablosundan da sahne
> haritasından da ÖNCE. §4'teki üç kapı geçilmeden plan yazılmaz.
> Kaynak: `araştırmalar/7.md` (22.08.2026 bilişsel yabancılaştırma araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① SAYILAR DIŞ ARAŞTIRMADAN GELİR, bu serinin ölçülmüş sonucu değildir.
   Test ölçütü nettir: Özgünlük sütunundaki 4 platosu. Bu kılavuza göre
   yazılmış filmlerde plato kırılmıyorsa kılavuz çalışmıyordur ve revize
   edilir. Gerçek izleyici tarafı: YAYIN_VE_PERFORMANS_KILAVUZU.md §6.

② BU KILAVUZ KONSEPT REDDEDER. Tek işi budur. Reddedilen konsept plana
   dönüşmez ve maliyeti SIFIRDIR; aynı redde üretimden sonra varılırsa
   maliyeti bir filmdir. §4 kapılarında "sonra düzeltiriz" yoktur.

③ NOVUM ≠ ORTAM. Ortam kartı (KILAVUZ_REHBERI §3) fiziği verir; novum o
   fiziğin İÇİNDE tek bir kural ihlalidir. İkisi karıştırılırsa "vakumda
   yürüyen adam" novum sanılır — o yalnızca ortamdır ve izleyicide hiçbir
   tahmin hatası üretmez. Deponun Özgünlük 4'lerinin çoğu bu karışıklıktır.

④ MODEL FİZİĞE DİRENİR. Fiziksel yasa novumu en okunur tiptir ama Veo
   doğru fiziği üretmeye eğilimlidir; ihlal prompta SOMUT nesne + jest
   olarak yazılmazsa model kuralı sessizce düzeltir. D73'ün üretim tarafı
   tam olarak budur — istenen olay hiç render edilmedi.
```

---

# 1. 🎲 NOVUM TİPİ SEÇİMİ — beş tip, tek tablo

**Mekanizma:** Novum, kontrollü bir **tahmin hatasıdır**. İzleyicinin beyni
"bilimkurgu" şemasını çağırır, ekrandaki ihlali görür, yeni bir kuralla
çözer. Çözebilirse özgünlük hissi doğar; çözemezse hatayı hikâyeye değil
**yazılıma** atfeder ve terk eder. Tip seçimi, bu çözülebilirliğin seçimidir.

| Novum tipi | İlk 3 sn okunabilirlik | Thumb-stop potansiyeli | Bu hattaki risk | Karar |
|---|:--:|:--:|---|:--:|
| **Fiziksel yasa** (yerçekimi, sürtünme, entropi) | çok yüksek | > %60 | modelin fizik direnci (§0④) | ✅ **BİRİNCİ TERCİH** |
| **Ölçek** (makro/mikro çarpıtma) | yüksek | %50-60 | uzamsal tutarlılık kayması | ✅ **İKİNCİ TERCİH** |
| **İlişki** (birinin ötekinden istediği şey) 🆕 | yüksek | ⬜ ölçülmedi | ikinci insan/replik yasakları hiç sınanmadı | ✅ **ÜÇÜNCÜ TERCİH** |
| **Zaman** (asimetri, döngü, duraksama) | orta | %30-40 | entropi taşıyıcısı olmadan görünmez | ⚠️ **ŞARTLI** |
| **Algı** (simülasyon, yansıma, boyut) | düşük | %20-30 | senkron hatası "glitch" okunur | ⛔ **KAÇIN** |
| **Toplum** (distopya, teknokrasi) | çok düşük | < %15 | tek karakterde toplum gösterilemez | ⛔ **YASAK** |

> 🆕 **İLİŞKİ TİPİ — 02.09.2026'da eklendi, sahibin kararıyla.**
> **Neden eklendi (ölçüm):** bu tablo beş tip taşıyordu ve **beşi de
> insan-dışıydı**; novum tipi yazılmış 13 filmin 12'si "fiziksel yasa"
> dedi. İnsanın insana yaptığı bir şeyin novum olabileceği **seçenek
> olarak listede yoktu** — yani depo yapısal olarak insan hikâyesi
> yazamıyordu. Kayıt: `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md`
> §1.2 · §4④.
>
> ⛔ **VE "Toplum" satırının gerekçesi bu satırla ÇAKIŞIR:** o satır
> *"tek karakterde toplum gösterilemez"* diyordu — yani bir yasak (tek
> insan) ikinci bir yasağı doğuruyordu. Toplum ⛔ YASAK olarak KALIR
> (bir toplum tek filmde gösterilemez), ama İLİŞKİ toplum değildir:
> **iki kişi bir toplum değil, bir ilişkidir.**
>
> ⬜ **DÜRÜST SINIR:** bu satırın thumb-stop sütunu BOŞ ve öyle kalacak.
> Depoda ikinci insanlı ya da replikli ölçülmüş tek bir film yok
> (`06` §1.1: replik 0/79). Elimizde bulgu değil, **karar** var.
> İlk ölçüm `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md`'nin iki probudur;
> ikisi de koşulmadı. Prob koşulunca bu sütun doldurulur ve satırın
> kararı gerekirse DEĞİŞİR.

```
SAYISAL KİLİT
  □ SEÇİLEN TİP     fiziksel yasa VEYA ölçek VEYA ilişki
  □ ZAMAN NOVUMU    yalnız yüksek entropili SOMUT süreçle
                    (yanan / dökülen / ufalanan / paslanan bir şey)
                    — "karakterin durması" zamanı göstermez, hareketsizliktir
  □ TOPLUM NOVUMU   bu seride yapısal olarak imkânsız; arka plandaki
                    yıkıntı novum değil SET TASARIMIDIR
  □ İLİŞKİ NOVUMU   taşıyıcısı §2'ye göre yine SOMUT olmak zorundadır:
                    isteğin geçtiği NESNE + iki kişinin ona yaptığı
                    FARKLI jest. "Aralarında gerilim var" taşıyıcı DEĞİLDİR.
                    ⛔ İkinci insan kadrajdaysa POZİTİF ayrım yazılır
                      (boy · duruş · farklı yüz), yasak cümlesi değil —
                      yasak kopyayı yasaklar, TARİF kopyayı ortadan kaldırır.
```

---

# 2. 🔩 GÖRSEL TAŞIYICI — A NESNESİ × B JESTİ

**Mekanizma:** İnsan beyni dünyayı önce nesnelerin ağırlığı, sınırı ve o
nesneyle yapılabilecek eylem üzerinden kavrar. Soyut bir optik fenomen bu
eylem şemasıyla eşleşmez; nedensiz dalgalanan ışık, izleyicide "kurgusal
yasa" değil "render hatası" karşılığı bulur.

> ⛔ **MUTLAK KURAL:** Novum havaya, sise, ışık hüzmesine, renk kaymasına
> veya lens parlamasına **yüklenmez.** Çerçevedeki somut bir nesne ile
> karakterin kinetik jesti arasındaki **fiziksel etkileşimde** yaşar.

```
PLANA YAZILAN SATIR (BÖLÜM 0'a, konsept satırının hemen altına)

NOVUM TAŞIYICISI: <somut nesne> × <karakterin jesti> → <görünen ihlal>

örnek ✅  çelik elma × avuçtan havaya atış → yükselirken paslanır,
          avuca toz olarak döner            (fiziksel yasa · entropi)
örnek ✅  ölçüm çubuğu × zemine saplama    → çubuk zemine değince
          kendi boyunun on katına çıkar     (ölçek)
örnek ⛔  atmosfer × yok                    → "havada dalgalanan zaman"
          (taşıyıcı yok — model bunu ışığa çevirir, D73)

🆕 İLİŞKİ TİPİNDE TAŞIYICI — aynı kural, iki jest:

NOVUM TAŞIYICISI: <somut nesne> × <A'nın jesti> ↔ <B'nin FARKLI jesti>
                  → <görünen ayrılık>

örnek ✅  tek yedek hücre × biri onu beşiğe geri koyar ↔ öteki
          onu zemine bırakır → ikisi aynı anda uzanır, eller
          çarpışır, biri çeker                  (ilişki)
örnek ⛔  iki kişi × "gerginler"           → taşıyıcı yok; gerginlik
          bir NESNEDE görünmüyorsa ekranda iki kişi yan yana durur
```

**Depodaki kanıt:** D73'te novum çift gölge setiydi; taşıyıcı türetilmiş bir
optik fenomendi ve modelden hiç çıkmadı. Filmin doruğu sanılan kare (havada
dönen jalonlar) planın doruğu bile değildi — üretim hatasıydı. Taşıyıcı
somut olsaydı ihlal ya render edilir ya da PROMPT_KONTROL'de yakalanırdı.

---

# 3. ⚖️ MAYA EŞİĞİ — tanıdık kabuk, TEK yeni kural

**Mekanizma:** "En ileri ama kabul edilebilir." Tamamen tanıdık görüntü
tahmin hatası üretmez, beyin dikkati kapatır → kaydırma. Tamamen kuralsız
görüntü ise hata selini çözemez → bilişsel aşırı yük → "yapay zekâ arızası"
etiketi → aynı saniyede terk. İkisinin arası tek bir dar banttır.

```
SAYISAL KİLİT
  □ KABUK           tanıdık kalır: uzay giysisi, vizör, ekipman, alet
                    (şemayı tetikleyen taraf — buraya YENİLİK KOYULMAZ)
  □ İHLAL SAYISI    film başına 1
                    en fazla 2 — ve ikincisi birincinin SONUCU olmalı
  □ İHLAL DIŞI HER ŞEY normal fizikle davranır; ihlalin kanıtı, yanındaki
                    normalin kusursuz çalışmasıdır
```

> ⚠️ Aynı anda bükülen iki bağımsız kural, izleyicide iki ayrı hipotez
> açar; kısa formatta ikisi de kapanmaz ve film "rastgele" okunur. Deponun
> Özgünlük 4'lerinde en sık ikinci sebep budur (birincisi §2 taşıyıcı).

---

# 4. 🚪 ÜÇ KAPI — konsept buradan geçmeden plan yazılmaz

```
① TEK KARE TESTİ
   Filmden alınacak TEK donmuş karede izleyici anomaliyi 1 saniyede
   işaret edebiliyor mu?
   ✅ karakter suyun altında oturuyor ama etrafında ateş yanıyor
   ⛔ karakterin zihninden geçen boyut yolculuğu · yavaşça yayılan
      görünmez gaz (zaman VE hareket gerektiriyor → tek karede yok)

② KİNETİK BAĞIMSIZLIK TESTİ
   Kural kendini yalnız 8-10 s'lik sabit planlardaki EYLEMLERLE
   kanıtlayabiliyor mu — replik, dış ses, ekran metni olmadan?
   ✅ vizörde parçalanan Dünya yansırken karakterin kırık fincandan
      sakince içmesi
   ⛔ gezegenler arası ticaret anlaşmazlığı · geçmişte yaşanmış kayıp

③ BAŞLIK ŞEMASI TESTİ
   Önerme ≤5 kelimelik bir başlığa çevrilebiliyor ve o başlık izleyiciye
   NEREYE bakacağını söylüyor mu?
   ✅ "Ters Yerçekimi Yağmuru" → izleyici damlalara hazır girer
   ⛔ "Uzayda Yalnızlık" → şema tetiklemez, hiçbir yere bakmaz
```

> Üçü de ✅ değilse **konsept reddedilir.** Kapı ③ paketlemeyle ortaktır ve
> orada ikinci kez koşar: `PAKETLEME_VE_VAAT_KILAVUZU.md` §1.

---

# 5. 🔁 KURAL TEKRARI — novum gösterilmez, KANITLANIR

**Mekanizma:** Beyin kurduğu hipotez doğrulandıkça ödül alır. Novum tek
sahnede gösterilip bırakılırsa izleyici onu bir kaza sanır; ikinci ve
üçüncü kanıtta "bu evrenin yasası" olduğunu anlar ve tamamlanma oranı
buradan yükselir.

```
SAYISAL KİLİT
  □ KURULUM     ihlal ilk kez görünür                     (S0-S1 bandı)
  □ DOĞRULAMA   aynı ihlal FARKLI bir nesnede tekrarlanır (orta nokta)
  □ SONUÇ       ihlal karakterin bedelini belirler         (doruk)
  □ TOPLAM      ≥ 3 sahne · ≥ 2 farklı nesne
```

> ⚠️ **D49 · D73 birlikte okunur:** kurala aykırı TEK kare öncülü çökertir.
> Novum döngüsü kurguda bozulursa (sahne düşer, sıra değişir) film içerikte
> değil kurguda kaybeder — kapı `KURGU_VE_TESLIM_KILAVUZU.md` §1'dedir.

---

# 6. ⏱️ BİLİŞSEL ZAMAN ÇİZELGESİ → SAHNE YUVASI

| Saniye | Bilişsel aşama | Ekranda ne olmalı | Yuva |
|---|---|---|---|
| **0-3 sn** | şema aktivasyonu + tahmin hatası | ihlal **kadrajda görünür** — merkez veya üçte bir | S0 |
| **3-10 sn** | MAYA testi | karakter ihlale kinetik tepki verir (geri adım, düşen alet) | S0 sonu · S1 |
| **10 sn - orta** | yabancılaştırmanın derinleşmesi | aynı kural ikinci nesnede | doğrulama sahnesi |
| **doruk** | kuralın bedele dönüşmesi | ihlal karakterin seçimini belirler | doruk yuvası |

```
FORMATA ÇEVİRİ
  dikey shorts (6×8 s)   ihlal S0'da GÖRÜNÜR olacak — 8 saniye tek şans
  2-4 dk (~15 sahne)     kurulum S0-S1 · doğrulama ~S7 · sonuç ~S12
  3-5 dk (~25 sahne)     kurulum S0-S2 · doğrulama S8-S12 · sonuç S20+
  7-9 dk (5 faz)         her fazın kendi doğrulaması var; faz 1 kurar
```

> Bu tablo `HOOK_VE_ILK_SAHNE_KILAVUZU.md` §2'nin yerine geçmez; onun
> "0. kare sınavı" ve merak bandı kapıları aynen koşar. Buradaki ek şudur:
> **hook'un sakladığı şey novumun KENDİSİ olamaz** — saklanan, ihlalin
> SEBEBİDİR. İhlal ilk saniyede görünür, sebebi filmin sonunda [D71].

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Açıklayıcı ekran metni / "Yıl 2084" kartı ile önermeyi kurmak | Metin yasağı mutlak [D13 · D45]. Önerme görsel kanıtlanır; kanıtlanamıyorsa §4② reddeder. |
| Kapalı finalde "karakter kaskını çıkarır, yüzü görünür" | Ekipman durum kilidi [D37 · D57]: vizör açılmaz. Novumun çözümü yüz açılmasıyla verilemez. |
| Algı novumu için "ayna yansımasında 1 sn gecikme" | Modelin senkron hatası doğrudan glitch okunur; algı novumu zaten ⛔ bandında (§1). |
| POV çekimiyle öznel algı kırılması | POV, kameranın karakterin gözüne geçmesidir; lockoff gözlemci dilini bozar (KARAKTER_VE_DUYGU §2 ile aynı ret). |
| "Renk paleti kayması ile evren kuralını anlatmak" | §2 mutlak kuralı — taşıyıcısız novum. D73'ün tekrarı olur. |
| Fraktal/kaotik arka planla "yenilik" hissi | §3 aşırı ayırt edicilik bandı. Fraktal ölçek KAPAK tarafında kalır (`PAKETLEME_VE_VAAT` §2). |

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 7 maddesi

```
□ 1. NOVUM TİPİ yazıldı mı — fiziksel yasa / ölçek dışında bir tip
     seçildiyse gerekçesi plana yazıldı mı (§1)
□ 2. NOVUM TAŞIYICISI satırı plana girdi mi: <nesne> × <jest> → <ihlal>
□ 3. İhlal sayısı 1 mi (ikinci varsa birincinin sonucu mu) — §3
□ 4. TEK KARE TESTİ ✅ mi: hangi sahnenin hangi karesi işaret ediliyor
□ 5. KİNETİK BAĞIMSIZLIK TESTİ ✅ mi: replik/metin/dış ses olmadan
□ 6. BAŞLIK ŞEMASI TESTİ ✅ mi: ≤5 kelimelik başlık plana yazıldı mı
□ 7. Kural ≥3 sahnede, ≥2 farklı nesnede kanıtlanıyor mu (§5) —
     ve bu sahneler kurgu kapısının KESİLEMEZ listesinde mi
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/7.md                      bu kılavuzun kaynak araştırması (22.08.2026)
UZAY_SENARYO_KILAVUZU.md               §1 novum · §4 exposition tuzağı · §6 Çehov
HOOK_VE_ILK_SAHNE_KILAVUZU.md          §2 S0 kapıları · D71 merak perdesi
PAKETLEME_VE_VAAT_KILAVUZU.md          §1 kapak anı · başlık şeması testinin ikinci koşusu
KARAKTER_VE_DUYGU_KILAVUZU.md          ihlale verilen kinetik tepkinin bütçesi
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md    §2 vuruş haritası — çakışırsa o kazanır
KURGU_VE_TESLIM_KILAVUZU.md            §1 kurgu kapısı — kural tekrarı kurguda korunur
PROMPT_KONTROL/                        ihlalin prompta SAYI olarak girip girmediği
DERSLER/07_KURGU_VE_ANLATI.md          D49 · D73 tam metin
```
