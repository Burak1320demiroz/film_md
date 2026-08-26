# 🪜 THE IRON SLOPE — Demir Yokuş

Dikey YouTube Shorts / Reels Production Document
Format: **9:16 (DİKEY)** | Sahne: 6 (Hook + 5 Ana Sahne) | Süre: Her sahne 8 saniye, toplam 48 saniye
Prompt yapısı: Her sahne için **1 görsel promptu + 2 video promptu** (A = T2V · B = I2V devam)
Kaynak: **özgün konsept** — kaynak film yok
Zaman ve yer: **Vakum + itki yerçekimi · 320 metrelik kargo gemisinin dış gövdesi, sürekli yanma altında** (ortam kartı `KILAVUZ_REHBERI` §3.5 — promptlarda yer adı geçmez)
Tür: **Bilimkurgu / hayatta kalma aksiyonu** (sert uzay gerilimi kulvarı — `UZAY_SENARYO_KILAVUZU` §1'in bilinçli seçimi)
_"Motor yandığı sürece, uzayın bir aşağısı var."_

---

## 🎯 BU SHORTS'UN TEK İŞİ

Kullanıcı talebi: **uzayda geçen, viral, bol aksiyonlu bir dikey short.**
Bu dosya talebi küçültmüyor — **aksiyonu modelin gerçekten çizebildiği
kanala taşıyor.** Depoda ölçülmüş gerçek: ateş/duman/patlama en düşük
skorların kaynağı (Parçacık 2/10 · Kaleida çevre 4.5/10); büyük katı
gövde ve **balistik düşüş** ise modelin en sağlam ürettiği hareketler
(THE QUIET IMPACT · THE SHORT WAY DOWN kanıtları). Bu filmin bütün
aksiyonu düşen rijit parçalardan ve tek bir tırmanıştan geliyor:

```
ADAM                                GEMİ
────────────────────────            ────────────────────────
dışarıda, merdivende                sürekli yanmada: 0,220 g
saniyede yarım metre tırmanıyor     her gevşek parça KIÇA doğru düşüyor:
yukarıda: hava kilidi, 14 metre       saniyede 2,16 m/s hız kazanarak,
aşağıda: turuncu jantlı uçurum        dümdüz bir çizgide
```

Uzayda yokuş vardır: **"yukarısı" pruva, "aşağısı" motordur** [ortam
kartı 3.5]. Hasarlı bir montaj bandından kopan her parça — üç panel ve
bir anten latisi — onun yanından geçip o uçuruma düşer. Film, adamla
hava kilidi arasındaki 14 metreyi ve bantta kalan gevşek parça sayısını
sıfıra kadar sayar.

**RİSK SAYIMI: 4 / 12** — Kart 3 (kask/vizör) · Kart 4 (ikinci figür,
her filmde) · Kart 5 (sayaç — **metinsiz/çevresel**) · Kart 9 (ışık
mıknatısı, **zayıflatılmış**).

> ⭐ **KART 6 (parçacık/toz/patlama) TETİKLENMİYOR — ve bu bir tasarım
> kararıdır:** toz 0 kare (vakum, kaynak yok) · duman/alev/kıvılcım 0
> kare (motor yalnız kadraj DIŞI turuncu ışık olarak var) · egzoz konisi
> 0 kare · çarpma ekranda 0 kare (düşen her şey kadrajdan ya da kaçış
> noktasına düşer, hiçbir şey ekranda bir yere çarpmaz) · düşen her
> parça RİJİT ve TEK parçadır, kopuş temiz makaslamadır. Kart 1 (su),
> Kart 2 (canlı), Kart 7 (diyalog), Kart 6b (katmanlı dünya), Kart 10
> (insansız sahne) ve Kart 11 (değişken çekim süresi) konseptte yok.

> ⚠️ **DÜRÜST KAYIT — bu filmin bir numaralı riski kartlarda YOK:
> TIRMANAN GÖVDENİN EKLEMLENMESİ.** 48 saniyenin ~40 saniyesi kesintisiz
> merdiven tırmanışıdır; bu, D18'in (yürüyüş eklemlenmesi) dikey
> akrabasıdır ve bir tırmanış filminde ELENEMEZ. Bütçelendi:
> ```
> TEK HAREKET TİPİ   yalnız basamak tırmanışı — sıçrama, sallanma,
>                    halatla kayma, duvar yürüyüşü 0 kare
> HER PROMPTTA       "each glove releases, rises, closes on the next
>                    rung and takes weight; each boot lifts, sets and
>                    takes weight — never sliding, never gliding"
> HIZ SAYILI         0,5 m/s (S2'de 0,7 m/s'ye çıkar) — ağır çekim
>                    mıknatısına karşı her promptta m/s
> KADRAJ             el/ayak ekstrem yakın planı YOK — eklem detayı
>                    en fazla MCU'da (S4), orada da yük yüzde değil
>                    elde: karabiner jesti
> ```
> İkinci beklenen bozulma: **D23 (sıfır-g süzülme) tuzağının tersi** —
> model uzay görünce gövdeyi YÜZDÜRÜR. Ortam kartı 3.5 bunu yapısal
> olarak kapatıyor (hiçbir kare sıfır-g'de değil; tek istisna S5'in
> 2,2 saniyelik yanma arası ve orada da eller merdivende). Her promptta
> ağırlık POZİTİF yazılır: "his boots stay planted on the rungs."
> **Üretim S0'dan başlar**; panel orada ona çarpar, kavis çizer, süzülür
> ya da ağır çekime girerse film üretilmez [LOW MOON emsali].

---

## ⏸️ BİLİNÇLİ SAPMALAR — sistem promptunun DNA'sından

`SHORTS_SISTEM_PROMPTU.md` §2'nin ilkelerinden üçü bilerek esnetiliyor;
THE QUIET IMPACT (06.08.2026) ve THE STRAIGHT LINE (23.08.2026) emsalleri:

```
DNA 3 — "Fiziksel imkansızlık = kanca"
SAPMA:  Bu filmde imkansızlık YOK. Novum ALGISAL: göz "uzay = düşüş yok"
        diye okur, ekranda 48 saniye boyunca taş gibi düşen parçalar
        görür. Gerçek fizik: 0,220 g sürekli itki [ortam kartı 3.5,
        THE UPHILL DARK'ın doğrulanmış sayıları]. Seride novumu tamamen
        gerçek fizik olan İKİNCİ film (ilki THE QUIET IMPACT).

DNA 5 — "Huşu, korku değil. Tehlike yoktur."
SAPMA:  Tehlike VAR ve merkezdedir. Karşılığı: panik 0 — adam bir
        teknisyen gibi davranır: test eder, sayar, karar verir, tırmanır.
        Jump scare 0 · gore 0 · temas 0 kare.

DNA 7 — "Karakter her sahnede duraksar."
SAPMA:  Duraksama filmde İKİ yerde: S3'te 1,5 s (latis tepesinde durma)
        ve S4'te 2,0 s (karabiner kararı). Toplam 3,5 s / 48.

LENS  — sistem promptu "32mm Cooke anamorphic" der. Vakumda anamorfik
        YASAK [KILAVUZ_REHBERI §3.1: atmosferik saçılma yok] → bütün
        lensler KÜRESEL: 32mm + 75mm (Quiet Impact emsali).

BİLEK EKRANI — sistem promptu "veriler bilek ekranından" der. Bu filmde
        HİÇBİR ekran yok [Kart 5]: sayaçların üçü de fiziksel/metinsiz.
```

---

## ⚠️ Genel Prodüksiyon Kuralları

1. **SIFIR KESME** — Her video 8 saniyelik, kesintisiz tek çekim; her
   sahne AYRI üretilir [Ders 1]. `single continuous shot, 0 cuts`
   6 videonun 6'sında, her beat zaman damgalı.
2. **DİKEY SADAKAT (9:16) + GÜVENLİ ALAN** — Karakterin hiçbir parçası
   `y=1436`'nın altına inmez. Bkz. **📱 GÜVENLİ ALAN HARİTASI**.
3. **İKİ LENS KİLİDİ — HEPSİ KÜRESEL** — Gövde ekseni (aşağı/yukarı
   bakış): **32mm** (S0, S1, S3, S5). Yan sıkıştırma/karar: **75mm**
   (S2, S4). Anamorfik ve yatay parlama YASAK [§3.1]. Kamera mesafesi,
   gövdeden yüksekliği ve bakış ekseni her promptta **metre** ile yazılır.
4. **⛔ KAMERA 6/6 TAM SABİT — gemiye vidalı** — Üç kurulumun üçü de
   gövdeye/vinç koluna kelepçeli sabit kameradır; filmde tek kamera
   hareketi yoktur. Sarsıntının fiziksel gerekçesi de budur: kamera
   geminin parçasıdır, gemiyle birlikte ivmelenir.
   ```
   ① Z EKSENİ      adam merceğe doğru tırmanır (S0, S5) ya da mercekten
                   uzaklaşır (S1, S3); ölçek kamera kımıldamadan değişir
   ② KADRAJI KESEN GEÇİŞ   düşen parçalar kadrajı üstten alta kat eder;
                   sabit kamera bir KAPIDIR, düşüş içinden geçer
   ③ SES           dışarıda mutlak sessizlik; tek ses gövdeden eldivene
                   İLETİLEN gürültü + kask içi nefes
   ```
5. **RENK DİLİ** — **Vakum siyahı + yoğun keskin yıldız alanı + jilet
   beyazı yan güneş + çıplak duman grisi gövde kaplaması + KAR BEYAZI
   suit + alt kenarlarda derin motor turuncusu (kadrandaki tek doygun
   değer) + vizör içi sıcak konsol ışığı + hava kilidi penceresinin
   küçük sıcak noktası.**

   > ⚠️ **Palet çakışma denetimi — dürüst kayıt.** Vakum + keskin gölge
   > fiziği HALF SKY ve QUIET IMPACT ile aynıdır (aynı ortam ailesi,
   > kaçınılmaz). Ayırt edici iki karar: **(a)** seride karakter hep
   > doygun renk aksanıyla ayrışıyordu (oksit kırmızısı, kobalt, hardal);
   > bu dosyada karakter renkle değil **PARLAKLIKLA** ayrışır — kar
   > beyazı suit, kadranın en parlak nesnesi. Tek doygun renk tehdidin
   > rengidir: motor turuncusu, ve yalnız kadraj kenarında bir JANT
   > olarak yaşar. **(b)** Quiet Impact'in kadranı pas kahvesi gezegen
   > ışığıyla yıkanıyordu; burada gezegen yok, kadran siyah-beyaz-gri
   > üzerine tek turuncu çizgidir.
6. **KARAKTER SADAKATİ** — 6 görsel promptunun **6'sında da** aynı
   karakter bloğu birebir, kısaltmasız tekrarlanır [Ders 45]. Kask 6/6
   kapalı; vizör **optik olarak berrak**, sırt silueti **DÜZ** — ikisi
   de her promptun gövdesinde pozitif cümleyle [Ders 79 — bible'da
   yazmak iki filmde YETMEDİ].
7. **VİRAL ZAMANLAMA (Hook)** — 0-2sn merak (yıldızların önünde merdiven
   tırmanan adam — sakin, neredeyse sıradan) → 2-5sn ipuçları (öndeki
   bant titriyor, iki cıvata kopup DÜŞÜYOR, panel dışa yatıyor) → 5-7sn
   tam reveal (panel kopar ve açık uzayda taş gibi, hızlanarak, dümdüz
   AŞAĞI düşer) → 7-8sn tek güçlü görüntü (panel 1,4 m yanından geçer;
   adam basamaklara yapışmış, başı düşüşü izliyor).
8. **İKİ VİDEO PROMPTU — DEVAM KARESİ ZORUNLU** — Her sahnenin **A
   (T2V)** ve **B (I2V devam)** sürümü vardır. B, bir önceki sahnenin
   SON KARESİNDEN başlar ve karakteri/ortamı yeniden tarif ETMEZ.
   Bkz. **🔗 DEVAM ZİNCİRİ**.
9. **ELLER 6/6 MERDİVENDE** — Alet yok, silah yok, telefon yok, ekran
   yok. Tek nesnesi vücudundaki tether şerididir ve filmin merkezi
   seçimi onu bırakmaktır.
10. **⛔ EKRANDA METİN SÜRESİ = 0,0 SANİYE [Ders 61]** — Gövde kaplaması
    ÇIPLAK metaldir: işaret, yazı, seri numarası, ok, şerit yok. Suit'te
    yama, bayrak, harf yok. Hava kilidi penceresi boş sıcak ışıktır.
    Metin yasağı prompt cümlesiyle değil KONSEPTLE kapatılır: kadrajda
    yazı üretebilecek tek bir nesne yoktur.
11. **⛔ AĞIR ÇEKİM YOK — 1 NUMARALI ÜRETİM KURALI [D12 · D44]** —
    Düşüş, geçiş ve kopma: üçü de modeli slow-motion'a çeker. Her hız
    ve ivme SAYIYLA yazılır (tırmanış 0,5 m/s · düşen parça her saniye
    +2,16 m/s) ve `everything moves at normal speed, no slow motion,
    no speed ramp` satırı **6 görsel + 6 video promptunun hepsinde**.
12. **⛔ TEMAS 0 KARE** — Düşen hiçbir parça adama değmez; geçiş
    mesafeleri metreyle yazılır (1,4 · 1,2 · 0,8 · 1,1 · 1,0 m).
    Gerilim çarpmadan değil **GEÇİŞTEN** gelir; ekranda hiçbir çarpma
    anı yoktur.
13. **⛔ ATEŞ / DUMAN / TOZ / KIVILCIM 0 KARE** — Motor yalnız kadraj
    dışından gelen turuncu jant ışığıdır; egzoz konisi hiçbir kadraja
    girmez. Kopuşlar temiz makaslamadır: parça bütün, kenar düz.
14. **YÖNELİM KİLİDİ [UZAMSAL §5.1]** — Geminin yönü her promptta
    yazılıdır: **pruva kadrajın yukarısı / kamera arkası, kıç ve
    motorlar her zaman alt kadraj çizgisinin çok ötesinde ve asla
    görünmez.** "Aşağı" üç kurulumda da aynı yöne düşer: kadrajın altına.

---

## 🧬 VİRAL MEKANİK — "UZAYDA AŞAĞI VAR: AŞAĞISI MOTOR"

```
Bu shorts'un imkansızlığı bir canavar ya da büyü değil, İZLEYİCİNİN
ŞEMASINA aykırı çalışan GERÇEK FİZİKTİR: sürekli itki altındaki gemide
her serbest cisim kıça doğru düşer — a = 0,220 g [ortam kartı 3.5].

KURALLARI (her sahnede aynı, beş farklı nesnede kanıtlanır):
 · DÜŞÜŞ DÜMDÜZDÜR. Kopan parça gövde hattına paralel, ölü düz bir
   çizgide iner; kavis yok, yalpalama yok, süzülme yok.
 · DÜŞÜŞ HIZLANIR. Her saniye +2,16 m/s: ilk saniyede 1 metre,
   üçüncü saniyede toplam ~10 metre, beşincide ~27 metre.
 · SES YOKTUR. Kopma yalnız gövdeden eldivene İLETİLEN boğuk bir
   gürültüdür; parça serbest kaldığı an tamamen sessizdir.
 · ADAM AĞIRDIR. Botlar basamaklara basar, tether şakül gibi asılır.
   Uzay burada bir yüzme havuzu değil, bir UÇURUM YÜZEYİDİR.
 · MOTOR = YERÇEKİMİ. Turuncu jant ışığı yandığı sürece aşağı vardır.
   S0'da yarım saniyelik bir kesinti (tohum) bunu fısıldar; S5'te
   2,2 saniyelik yanma arası bunu KANITLAR: ışık söner, ağırlık gider.

İzleyicinin gözü ilk 2 saniyede "astronot tırmanıyor" der. 5. saniyede
panel kopar ve DÜŞER — izleyici düzeltir: bu yüzen bir adam değil, bir
uçurumdaki adam. O andan sonra geriye tek soru kalır: merdiven mi önce
biter, tırmanış mı?

Serinin önceki mekaniklerinden ayrı: süreksizlik değil (Winter Line),
eksik neden değil (Wrong Shadow), ölçek-hız uyuşmazlığı değil (Quiet
Impact), eksik serbestlik derecesi değil (Straight Line). Buradaki
mekanik YÖN TERSİNMESİ: "uzayda düşüş yok" şeması, 48 saniye boyunca
düşüş sayan bir ekranla çarpışır.
```

### Mekaniğin insani karşılığı

```
Adam dış gövde teknisyeni — bu merdiveni yüzlerce kez, ağırlıksız,
parmak ucuyla çıkmış biri. Filmin acı ironisi: onu öldürmeye çalışan
şey (yanma) aynı zamanda botlarını basamakta tutan şeydir. S5'te motor
2,2 saniyeliğine sustuğunda bunu görür: düşüş biter, ama tırmanışın
anlamı da askıya alınır — sonra ikisi birden geri gelir. Tek kararı
S4'te verilir ve tek jestle gösterilir: başparmağı karabineri açar,
onu düşmekten koruyacak tek şeyi geride bırakır — çünkü şerit sıkışmış
ve tepesinde tek bağla asılı 6 metrelik bir latis vardır. Zamanı
korunmaya tercih eder. Kazanır. Ve yukarı kadar korumasız tırmanır.
```

---

## 🔗 DEVAM ZİNCİRİ — altı sahne, tek kesintisiz tırmanış

> Kaynak: `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` §5 (perde) +
> `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §6. ⭐ Bu filmde perde bedava
> gelir: kadrajı kapatacak şey zaten sürekli DÜŞMEKTEDİR — bir panel,
> bir ray parçası, bir anten çubuğu.

```
PRENSİP:  SAHNE N son 0,5 saniyede kadraj düşen bir parçayla KAPANIR
          SAHNE N+1 ilk 0,5 saniyede AYNI parçayla kapalı başlar ve
          parça aynı yönde (aşağı) kadrajdan çıkar.
          Kurguda iki klip bu kapalı anda 3-5 kare bindirilir.

⭐ COĞRAFYA NOTU: üç kamera da GEMİYE SABİTTİR ve hiç taşınmaz.
   Değişen tek şey adamın merdivendeki konumudur: C kamerasından
   uzaklaşır (S1→S3), A kamerasına yaklaşır (S0→S5). Üç kamera,
   tek merdiven, tek yön: yukarı.
```

| Kesme | Tip | Kapatan / köprü |
|:--:|:--:|---|
| S0→S1 | SERT + J-köprü | Panel kaçış noktasına küçülür; kopmanın gövdeye yayılan titremesi S1'in ilk saniyesine sarkar |
| S1→S2 | PERDE | Kopan 3 m'lik ray parçası C merceğinin 0,6 m yanından geçer, koyu kütlesi kadrajı doldurur → S2 aynı koyu kütleyle kapalı açılır, alt kadrajdan çıkar |
| S2→S3 | SERT + J-köprü | Adam kadrajın üstünden çıkar, boş gövde duvarı 0,5 s tutulur; latisin derin iniltisi kesmeden önce başlar |
| S3→S4 | PERDE | Kopan anten çubuğu C merceğinin 0,2 m önünden geçer, ince koyu çizgisi kadrajı doldurur → S4 aynı çizgiyle açılır, yarım saniyede düşer |
| S4→S5 | SERT + J-köprü | Son karede şakül gibi asılı beyaz şerit; son bağın ilk lif çıtırtısı (iletilen) kesmeden önce duyulur |
| S5→S0 | **döngü** | Kurulum A'ya kurulum A ile dönülür: aynı kadraj ailesi, aynı ışık durumu (turuncu jant yanık), aynı jest |

> Bilinçli sert kesme sayısı 3 (≤3 ✅) ve üçü de J-köprülü; perde 2/5.
> Ses köprülü kesme oranı 3/5 = %60 ✅ [KURGU_RITMI §3].

### ⚠️ B SÜRÜMÜ İÇİN BAŞLANGIÇ KARESİ — pratik not

Perde tamamlandığı an kadraj bilgisizdir; I2V modeline bilgisiz kare
vermek çapayı öldürür. B sürümünün başlangıç karesi perdenin
TAMAMLANDIĞI kare değil, ondan ~0,3 saniye ÖNCEKİ karedir; B promptu
perdenin kalanını kendi ilk yarım saniyesinde tamamlar.

### Kurulum ve açı yayı (A-C-B-C-B-A)

| S | Kurulum | Lens | Ölçek | Kamera konumu | Bakış ekseni | Hareket |
|:--:|:--:|:--:|:--:|---|---|:--:|
| S0 | **A** | 32mm | MFS (adam 14 m) | hava kilidi yanı, gövdeden 0,5 m | gövde ekseni boyunca AŞAĞI (kıça) | TAM SABİT |
| S1 | **C** | 32mm | GENİŞ (adam 8,5 m) | ray kelepçesi, başlangıcın 6 m altı, gövdeden 0,4 m | gövde ekseni boyunca YUKARI (pruvaya) | TAM SABİT |
| S2 | **B** | 75mm | MS (7 m) | katlı vinç kolunun ucu, gövdeden 7 m | gövde yüzüne YAN | TAM SABİT |
| S3 | **C** | 32mm | GENİŞ (adam 11 m) | S1 ile aynı | YUKARI | TAM SABİT |
| S4 | **B** | 75mm | MCU (7 m) | S2 ile aynı | YAN | TAM SABİT |
| S5 | **A** | 32mm | MFS→MCU (4→2 m) | S0 ile aynı | AŞAĞI | TAM SABİT |

```
KURULUM SAYISI: 3 (A · B · C) — A iki, B iki, C iki kez.
✅ ACI_YAYI §4 bandı: 6 sahnelik filmde ≥3 kurulum, tavan 3 — TAM BANT.
   Ardışık iki sahne hiçbir yerde aynı kurulumu paylaşmıyor ✅
   Açı farkları: A↔C gövde ekseninde 180°, B ikisine 90° — ≥45° ✅

KULESHOV DÖNGÜSÜ (KARAKTER_VE_DUYGU §2): S2 (B · adam, bakış yukarı
   kadraj çizgisine atılır) → S3 (C · baktığı şey: latisin kopup
   yakalanışı, TAM gösterilir) → S4 (B · A′: aynı kurulum, değişen tek
   şey — eli karabinere gider). A ve A′ AYNI kurulumda ✅ sapma yok;
   dönüş planı 8 s ≥ 2 s ✅
```

---

## 🥁 VURUŞ TABLOSU VE PLAN SATIRLARI

| Sahne | Sn | Vuruş (DIKEY_MIKRO_DRAMA §1) | Bu filmde |
|:--:|:--:|---|---|
| **S0** | 00-08 | Algısal şok | Tırmanışın ortasında açılış. Bir gövde paneli kopar ve açık uzayda taş gibi, hızlanarak AŞAĞI düşer; 1,4 m yanından geçer |
| **S1** | 08-16 | Kışkırtıcı engel | **Aşağı yol da düşüyor**: botlarının altındaki 3 m'lik ray parçası kopup mercekten geçer. İniş diye bir seçenek kalmaz |
| **S2** | 16-24 | Z-ekseni tepkisi | İkinci panel kadrajı 0,4 saniyede keser; adamın temposu 0,5'ten 0,7 m/s'ye çıkar — cevap panik değil HIZ |
| **S3** | 24-32 | Görsel dönüm / ikinci şok | **LATİS**: 6 metrelik anten latisi kopar, devrilen direk gibi süpürülür ve tepesinin 0,8 m üstünde İKİ bağla yakalanıp asılı kalır — tehdit artık rastgele değil, NİŞANLI |
| **S4** | 32-40 | Kriz | Tether sıkışmış runner'da TAKILIR; son panel 1,1 m öteden geçer; bağlardan biri kopar. Adam karabineri açar — **korunmayı zamana takas eder** |
| **S5** | 40-48 | Doruk + döngü | Son bağ kopar: latis 1,0 m yanından, iki saniye boyunca kayarak geçer. Sonra **motor susar**: turuncu söner, botlar basamaktan kalkar, şerit kıvrılır — 2,2 saniye sonra yanma geri döner, botlar oturur, tırmanış sürer |

```
BOŞ VURUŞ       0 — altı sahnenin altısı da olay taşır
GENİŞ KURULUM   0 sahne
İKİNCİ ŞOK      S3 ✅ (latisin devrilip yakalanışı)
ÇÖZÜLÜM         yok — S5 döngüye devreder (hava kilidine giriş GÖSTERİLMEZ)
DURAKSAMA       filmde TOPLAM 3,5 saniye (S3'te 1,5 · S4'te 2,0)
```

### Plan satırları

```
TEMA: UMUT  (TEMA_MUHENDISLIGI §3-4 · dikey-uyumlu "anlık durum" teması)
      Tek cümle testi: "Bu film, her şey düşerken tırmanmaya devam
      etmek hakkında." — cümlede novum kelimesi yok ✅
      İndeksler (§5): başın hedefe/ışığa dönüşü (S1 · S5) · avucun bir
      sonraki basamağa açılışı (S0 · S1 · S2 · S3 · S4 · S5 — her sahne) ·
      soğuk kadranda iki sıcak nokta: hava kilidi penceresi (hedef) ve
      vizör içi konsol (yüz)
      ⚠️ Sapma kaydı [D74]: §5'in umut satırı sıcak sızıntıyı YANDAN
      önerir; bu filmde sıcak değer ÜSTTEDİR (hedefin kendisi) ve
      İÇERİDEDİR (konsol ışığı). Payoff (§6): final karesinde hedef
      ışığı NETLEŞMEDEN kesilmez — S5 sonunda hava kilidi halkası
      merceğin 2 m yanında ve nettir ✅

NOVUM TİPİ: FİZİKSEL YASA — ALGISAL (ONERME_VE_NOVUM §1 birinci tercih;
      ihlal edilen kural İZLEYİCİNİN ŞEMASIDIR, fizik değil. Gerçek
      fizik novumu emsali: THE QUIET IMPACT)
NOVUM TAŞIYICISI: kopan gövde paneli × adamın basamaklara kenetlenip
      geçişi izlemesi → panel açık uzayda taş gibi "aşağı" düşer,
      küçülerek HIZLANIR
      ⭐ Taşıyıcı KATI ve BİRİNCİL bir nesnedir [D73 tuzağı elendi].
İHLAL SAYISI: 1 algısal kural ("uzayda aşağı var"); ekranda gerçek
      fizik ihlali 0. Diğer her şey normal fizik: keskin gölgeler,
      sessizlik, ağırlık, düz düşüş çizgileri. ⭐ Kuralın kanıtı,
      yanındaki normalin kusursuz çalışmasıdır [§3 maya eşiği].
KURAL KANITI: 6 sahne, 5 farklı nesne —
      panel (S0 · S2 · S4) · ray parçası (S1) · anten çubuğu (S3) ·
      latis (S5) · tether şakülü + adamın kendi ağırlığı (S4 · S5)
      [ONERME_VE_NOVUM §5: ≥3 sahne, ≥2 nesne ✅]
ÜÇ KABUL TESTİ [ONERME §4]:
      ① TEK KARE: donmuş karede merdivendeki adam + yanında DÜŞEN
        panel + yıldızlar → anomali 1 saniyede işaret edilir ✅
      ② KİNETİK BAĞIMSIZLIK: kural yalnız eylemle kanıtlanır — düşen
        parçalar, gergin şakül, çöken/yükselen botlar; replik 0 ✅
      ③ BAŞLIK ŞEMASI: "Uzayda her şey düşüyor" (4 kelime) → izleyici
        düşen şeylere bakar ✅

HOOK TİPİ: IN MEDIAS RES  (HOOK §4 · aksiyon konseptlerinin tipi)
      Tipin kayıtlı riski: "bağlam borcu birikir — S1'in ikinci
      bilgisi bağlam TAKSİDİ olarak tasarlanır." Ödendi: S1 hem
      tehlikeyi büyütür hem NEDENİ söyler (aşağı yol düştü → yukarı
      zorunlu; aşağıda zaten yalnız motor var).
S0 SORU CÜMLESİ: "Uzayın ortasında bu panel neden taş gibi düştü?"
S1 İKİNCİ BİLGİSİ: düşen şey artık rastgele parça değil, YOLUN KENDİSİ —
      soru büyür: "merdiven ondan önce mi bitecek?"
İLK 2 SANİYENİN SESİ: TEK diegetik doku — gövdeden eldivene iletilen
      alçak, sürekli yanma gürültüsü; üstünde tek nefes. Müzik 2,5
      saniyede girer. [HOOK §5①]

TOHUM BİLGİ: S0 · 0:05,8 · 0,4 saniye · taşıyıcı: kaçış noktasındaki
      turuncu jantın yarım saniyeden kısa kararıp geri gelmesi.
      ⛔ Adam tepki vermez, kamera vurgulamaz. [FINAL §3 penceresi
      5-7 sn ✅ · süre ≤2 s ✅ · çevrede ✅]
GERİ DÖNÜŞ: S5 · 44,4 s — kararma TAMAMLANIR: turuncu söner, gürültü
      susar, ağırlık gider. Tohumun bulunduğu yere (kaçış noktasının
      jantına) görsel dönüş ✅

FİNAL TİPİ: DÖNGÜ + TWIST  (FINAL §2 · dikeyde döngü zorunlu ✅)
      TWIST: "aşağı" bir MOTORDUR — 2,2 saniyeliğine kapanır ve film
      boyunca savaşılan yerçekiminin bir yanma programına bağlı olduğu
      görülür. Sonra ikinci kademe ateşlenir: yokuş geri gelir.
AÇIK KALAN SORU SAYISI: 1 — "hava kilidine varacak mı?"
İKİLEM (FINAL §4): ① bedel kadrajda ve kendi eliyle: karabineri açar,
      onu düşüşten koruyacak tek şeyi geride bırakır ② aldığı şey
      tartışmalı: korunma yerine ZAMAN — tek bağla asılı latisin
      altından korumasız geçer ③ kamera yargısız: 6/6 lockoff,
      vurgu planı yok.
PAYLAŞIM SAHNESİ: S4 · KAYGI (huşu DEĞİL — filmin imzası tek valanstır)
      75mm sıkıştırma + tek bağda asılı 6 m latis + sıkışan tether +
      2,0 saniyelik karar + bir kez kopan nefes ritmi.
      ⚠️ S5'in 2,2 saniyelik ağırlıksızlığı huşu değil, ASKIYA ALINMIŞ
      KAYGIDIR — tek valans korunur.

LOOP SATIRI (SENARYO_VE_VIRAL §5 + DIKEY_MIKRO_DRAMA §5):
      KİNESİK RESET — S0 ilk jest: adam basamağı kavrar, başı sağ
      omzunun üstünden aşağı bakıştan öne döner. S5 son jest: adam
      basamağı kavrar, başını sağ omzunun üstünden aşağı çevirir.
      48. saniyede hareket sürüyor; poz yok, donma yok, jenerik yok.
      Kurulum (A), kadraj ailesi, ışık durumu (turuncu jant yanık),
      palet ve yön aynı. Döngü filmin ANLAMIDIR: yanma bitmedi —
      kademe değişti; tırmanış sürüyor.

KAPAK ANI (PAKETLEME §1): S0 · 0:05-0:06 · sol-orta üçte birde beyaz
      tırmanan figür (y %35-58, kadranın en parlak nesnesi), sağında
      düşen panel (ondan küçük ve küçülüyor — mesafe okunur), üstte
      bant + latis silüeti (y %10-30), altta kaçış noktası ve turuncu
      jant (y ~%82) · tek kaynak: sol kadraj dışı sert güneş · odak:
      düşen panelin keskin silueti.
      Kaynak blok 0:00-0:10 ✅ · KESİLEMEZ listesinde ✅
KULLANILAN ODAK (PAKETLEME §2): ② yüksek kontrastlı silüet (kar beyazı
      figür, siyah boşluk önünde) + ③ fraktal ölçek (aşağı doğru
      küçülerek tekrarlayan kaplama levhası ve basamak ritmi).
      ⛔ Odak ① (vizör yansıması) UYGULANAMAZ: vizör sıfır-yansıma
      kilidiyle yazılı [D79].

MERKEZİ SEÇİM: S4 · 5,2-6,2 sn (film 37,2-38,2) — başparmağın
      karabiner kapısını açması. Seçim EKRANDA tek jestle tamamlanır;
      bedel AYNI SAHNEDE görünür: şerit şakül gibi asılı kalır, adam
      korumasız tırmanır [D72]. (Orta nokta 24 s = S3 sınırı; seçimin
      S4'te olması STRAIGHT LINE emsaliyle aynı yuvadır.)

ÖRÜNTÜ KIRICI KAPISI (KURGU_RITMI §2)
| S | ölçek | palet | ses dokusu |
|:--:|---|---|---|
| S0 | MFS (aşağı bakış) | gri gövde + turuncu jant + beyaz figür | iletilen yanma gürültüsü + nefes + iki cıvata tıkırtısı |
| S1 | GENİŞ (yukarı bakış) | siyah boşluk + hava kilidi sıcak noktası ilk kez büyük | yalnız nefes + basamak tuğları → kopma titremesi |
| S2 | MS (75mm yan) | kar beyazı suit kadranı kaplar, güneş traşlar | hızlanan nefes ritmi + runner klikleri + geçen panelin MUTLAK sessizliği |
| S3 | GENİŞ + üstte kütle | latis silüeti yıldız alanını böler | derin metal iniltisi (iletilen) → dış mutlak sessizlik, nefes hızlanır |
| S4 | MCU (75mm) | vizör içi sıcak ten + beyaz + flu latis | ses DARALIR: yalnız nefes + fan + karabiner tık'ı |
| S5 | MFS→MCU (aşağı bakış) | turuncu SÖNER — filmin tek palet olayı — sonra döner | kayan latisin iletilen gürültüsü → tam diegetik boşluk (nefes+fan) → gürültü döner |
Üç sütunun üçü de her ardışık çiftte değişiyor ✅

SES KÖPRÜLERİ (KURGU_RITMI §3): J-köprü S0→S1, S2→S3, S4→S5 ·
      PERDE S1→S2, S3→S4 · bilinçli sert kesme 3 (≤3 ✅), üçü de
      köprülü · köprü oranı 3/5 = %60 ✅
      Ambiyans yatağı TEK parçadır ve DİEGETİKTİR: gövdeden iletilen
      alçak yanma gürültüsü + kask içi fan; 48 saniyede tek kesinti
      var ve o kesinti FİLMİN TWIST'İDİR (44,4-46,6). Kesinti sırasında
      nefes + fan sürer — mutlak dijital sıfır 0,0 saniye [D83].
```

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

### ⭐ GÖVDE EKSENİ, DİKEY KADRAJIN DOĞAL DOSTUDUR

```
Bir geminin omurgası yatay bir nesnedir — ama EKSENİNDEN bakıldığında
dikeydir: kaçış noktası kadranın dibinde (A) ya da tepesinde (C),
kaplama ve basamak ritmi izleyicinin gözüne kadar gelir.

  A KURULUMU (aşağı bakış)          C KURULUMU (yukarı bakış)
  ÜST 1/4   yakın gövde + kilit     ÜST 1/3   hava kilidi ışığı + bant
  ORTA      adam — güvenli bant     ORTA      adam
  ALT 1/4   uzak kaplama + turuncu  ALT 1/4   yakın kaplama
            jant (figür girmez)

⭐ DIKEY_MIKRO_DRAMA §3'ün üç derinlik katmanı bedava:
  ÖN PLAN   hasarlı bant / yakın basamaklar ve kaplama taneleri
  ORTA PLAN adam — izleyicinin kilitleneceği katman
  ARKA PLAN sığ odakta küçülen kaplama ritmi + yıldız alanı
```

### Sahne sahne denetim

| Sahne | Reveal nesnesi | Adamın bandı | Reveal bandı |
|:--:|---|:--:|:--:|
| S0 | düşen panel | y %35-58 | %58-70 (küçülür) |
| S1 | kopan ray parçası | y %34-52 | %55-85 (büyür) |
| S2 | kadrajı kesen panel | y %20-72 | %30-58 (0,4 s geçiş) |
| S3 | asılı latis | y %50-72 | %8-46 |
| S4 | tek bağ + şakül şeridi | y %16-74 | latis sol şerit · şakül %66-74 |
| S5 | kayan latis + sönen jant | y %28-64 (büyür) | %40-72 → küçülür |

**Her görsel promptun COMPOSITION satırına eklenen zorunlu cümle:**

```
No part of the figure falls into the bottom quarter of the frame.
```

---

## 📖 Sabit Referanslar (Bibles)

### 👤 Character Bible

**Kimlik (yalnızca bu dosyada):** DEMİR ARAS, 34, yörünge kargo hattı
dış-gövde teknisyeni. Bu merdiveni yüzlerce kez ağırlıksız çıkmış; ilk
kez ağırlıkla çıkıyor. Acil sakınma yanması başladığında bant onarımının
ortasındaydı.

> ⚠️ **ÜRETİM UYARISI [Ders 34 / 45]:** Karakterin adı **hiçbir promptta
> yazılmaz.** Milliyet ifadesi kullanılmaz. Gerçek kurum, ülke, marka,
> bayrak hiçbir promptta geçmez. Köşeli parantez etiketi yasak.

**Tam tarif — 6 GÖRSEL promptun 6'sında da birebir, kısaltmasız tekrarlanır:**

```
A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon.
```

**Hareket imzası (konsepte özgü):** Teknisyen refleksleri, korku
refleksleri değil. Nefes ritmi **iki basamakta bir** — ritim yalnız
S4'te bir kez kopar. Yük vermeden önce her basamağı **bir kez çeker**
(meslek alışkanlığı). Arkasına bakarken gövdesini döndürmez, yalnız
başını sağ omzunun üstünden çevirir ve tırmanışı kesmez.

**⚠️ BEYAZ KİLİDİ [sayısal · D58 · Kart 4]:** Filmde **TAM BİR insan ve
TAM BİR beyaz suit** vardır. Kadranda başka hiçbir beyaz gövde, yansıma
ya da insan biçimi yoktur; kaplama mat gri, düşen parçalar koyu gridir.
Diz/önkol/bot burnundaki gri aşınma her sahnede aynı yerdedir [D42].

### 🚢 Ship / World Bible — SÜREKLİ YANMADA KARGO GEMİSİ

```
GEMİ:     320 metrelik insansız-ağırlıklı kargo gemisi; acil sakınma
          yanmasında. PRUVA her kadrajda yukarı/kamera arkası yönündedir;
          KIÇ VE MOTORLAR her zaman alt kadraj çizgisinin çok ötesinde
          ve ASLA GÖRÜNMEZ. Egzoz konisi 0 kare — motor yalnız alt
          kenarlardan gelen derin turuncu jant ışığıdır.
İTKİ:     0,220 g (a = 2,16 m/s²) — THE UPHILL DARK'ın doğrulanmış
          sayıları [ortam kartı 3.5]:
          serbest kalan parça 1 saniyede 1,08 m · 3 saniyede 9,7 m ·
          5 saniyede 27 m yol alır; hız her saniye +2,16 m/s.
          Yanma İKİ KADEMELİDİR: kademe arası boşluk 2,2 saniye
          (S5'in twist'i — gerçek çok-yanmalı manevra mimarisi).
GÖVDE:    çıplak, boyasız, İŞARETSİZ gri metal kaplama — hiçbir levha,
          yazı, ok, numara yok [Kart 5 çözümü: metin yasağı KONSEPTLE].
          Kaplama MAT: yansıma üretmez [D20].
MERDİVEN: çift raylı servis merdiveni, basamak aralığı 0,4 m, omurga
          kaplaması boyunca dümdüz. Tırmanış hızı 0,5 m/s (S2'de 0,7).
HAVA KİLİDİ: adamın 14 m üstünde; küçük yuvarlak penceresinden sıcak
          iç ışık — kadrajdaki iki sıcak noktadan biri (öbürü konsol).
HASARLI BANT: hava kilidinin 3-6 m altında, gövdeyi enine kesen eski
          ekipman montaj bandı. Üstünde başlangıçta GEVŞEK: 3 gövde
          paneli (her biri 2,0 × 1,2 m, düz gri metal) + 1 anten
          latisi (6,0 m, açık kafes). Küçük parçalar (cıvata, 1,5 m
          anten çubuğu) sayaca girmez, promptta sayılıdır.
TETHER:   2,4 m beyaz düz şerit; göğüs halkası ↔ ray üstünde kayar
          runner. Runner S4'te bükülmüş braketin altında SIKIŞIR.
          Gergin şerit DÜZDÜR [D26]; bırakıldığında runner'dan şakül
          gibi dümdüz aşağı sarkar (ortam kartı 3.5 kanıt nesnesi).
SES:      dışarıda mutlak sessizlik. Duyulan her şey GÖVDEDEN İLETİLİR:
          alçak sürekli yanma gürültüsü (eldiven/bot teması), kopma
          iniltileri, basamak tuğları. Serbest düşen parça SESSİZDİR.
          Kask içi: nefes (HUMAN register) + alçak fan.
SU / CANLI / ARAÇ TRAFİĞİ / GEZEGEN: 0 kare.

⚠️ MERKEZİ TAKVİM — PARÇA, MESAFE, JANT (sahne başına yazılır)
  S    BANTTAKİ GEVŞEK PARÇA     HAVA KİLİDİ    GEÇİŞ MESAFESİ / OLAY
  S0   3 → 2 (panel #1 düşer)      14 m          1,4 m — panel geçer
  S1   2 (ray parçası ayrıca)      12 m          ray mercekten 0,6 m
  S2   2 → 1 (panel #2 düşer)       9 m          1,2 m — kadrajı keser
  S3   1 (latis DEVRİLİR, asılır)   7 m          tepe boşluğu 0,8 m
  S4   1 → tek bağ (panel #3 düşer) 6 m          1,1 m — panel geçer
  S5   1 → 0 (latis düşer)          4 → 2 m      1,0 m — latis geçer

  ⭐ Üç sayaç, üçü de metinsiz [Kart 5]:
     ① BANTTAKİ GEVŞEK PARÇA: 3 → 2 → 1 → 0 (dramatik saat)
     ② HAVA KİLİDİ MESAFESİ: 14 → 12 → 9 → 7 → 6 → 2 m (umut hattı)
     ③ TURUNCU JANT: yanık → S0'da 0,4 s kararır (tohum) → S5'te
        söner ve geri döner (twist)

Her görsel promptta zorunlu iki satır:
"nothing touches him at any point; the nearest passing object misses
him by [X] metres"
"the ship's bow is beyond the top of frame / behind the camera and the
stern with its engines lies far beyond the bottom frame edge, never
visible"
```

### 💡 Lighting Bible — JİLET GÜNEŞ + KADRAJ DIŞI MOTOR JANTI

```
KAYNAKLAR (adıyla yazılır, asla "cinematic lighting" denmez) [Ders 33]:
  · SERT GÜNEŞ: kadrajın SOL DIŞINDA, gövdeye yandan vurur. Vakum:
    gölgeler jilet kenarlı ve MUTLAK SİYAH, dolgu YOK [§3.1].
    ⛔ Güneş diski hiçbir sahnede kadraja girmez [Ders 3].
  · MOTOR JANTI: kıçtaki motorlardan gelen derin turuncu ışık — yalnız
    alt kadraj kenarından, yalnız aşağı bakan kenarları çizer. Ortam
    kartı 3.5'in tek meşru "dolgu" istisnası: kaynak, dolgu değil.
    Egzoz/alev 0 kare. S0'da 0,4 s kararır (tohum), S5'te 44,4'te
    söner ve 46,6'da geri döner (twist).
  · VİZÖR İÇİ KONSOL: çene altı 15 cm'den sıcak alçak anahtar —
    yüzü camın İÇİNDE okutur [KARAKTER_VE_DUYGU §1 bloğu]. Vizör
    kilidi değişmez: cam kapalı, berrak, yansımasız.
  · HAVA KİLİDİ PENCERESİ: küçük sıcak nokta — hedefin ışığı.

⚠️ [Ders 41 / 3 / 29] Beyaz suit + sert güneş = bloom riski. Suit ve
   kaplama MAT yazılır; "glowing/radiant/shimmering" hiçbir promptta
   geçmez; hale, parlama ve ışık huzmesi yasaktır (vakumda huzme
   fiziksel olarak da yanlıştır — saçacak ortam yok).

⚠️ [Ders 104 · KART 9] IŞIK MIKNATISI — YAPISAL OLARAK ZAYIFLATILDI.
   Baskın kaynak (güneş) hareket eksenine DİKTİR: kimse ışığa doğru ya
   da ışıktan uzağa gitmiyor. İkincil kaynak (turuncu jant) hedefin
   TERSİ yöndedir ve kadraj dışıdır. Yine de dört kanal her promptta:
     ① hedef-dilim + yön: hedef hava kilidi, kadranın üst kenarında /
        merceğin yanında — kamera A kurulumunda HEDEFTEDİR
        (kaçış basamağı [UZAMSAL §6.8] S0 ve S5'te önceden uygulandı)
     ② omuz hattı: omuzlar merdivene kare
     ③ ışığa göre poz: "the hard sunlight rakes across him from frame
        left"
     ④ yön negatifi: "he never turns toward the light, never reverses,
        no direction change"

ZEMİN KİLİDİ [Ders 48]: "the plating texture, the rung spacing and the
direction of the razor-edged shadows are identical to the previous
scene; only his height on the ladder and the number of loose pieces
have changed."
```

### 🎥 Camera Bible

```
LENS KİLİDİ — çekim başına tam olarak bir KÜRESEL lens:
  32mm → S0, S1, S3, S5   (gövde ekseni: aşağı/yukarı bakış)
  75mm → S2, S4           (yan sıkıştırma / karar)
MESAFE + KONUM KİLİDİ: her promptta metre olarak.
HAREKET SÖZLÜĞÜ:
  ⭐ HAREKET YOK. 6 sahnenin 6'sı TAM LOCKOFF; üç kamera da gövdeye/
  vinç koluna kelepçelidir ve gemiyle birlikte ivmelenir.
  El kamerası, sarsıntı, pan, tilt, dolly, zoom, hız rampası YASAK.
  Her video promptunda: "absolutely zero camera movement".
75MM'NİN İŞİ [KAMERA_ACISI §4]: tele sıkıştırma tehdidi YAKINLAŞTIRIR —
  S4'te tek bağla asılı latis, omzunun hemen üstündeymiş gibi yığılır.
  Yalnız S2 ve S4'te; S0/S1/S3/S5'teki 32mm gerçek derinliği geri verir.
HAREKET SÜNGERİ [KAMERA_ACISI §6②]: sabit kadraj donmasın diye her
  sahnede kadraj İÇİ mikro hareket yazılır — vizörün alt kenarında
  nefes buğusu, sallanan tether şeridi, titreyen bant parçaları,
  turuncu jantın nabzı.
  ⛔ Parçacık yok: toz, kıvılcım, duman kadraja giremez [Kart 6 sıfırı].
SABİT KLİP SÜRESİ: her video promptu tam 8 saniye, tek kesintisiz çekim.
```

### 🧗 Motion Bible — düşüşün ve tırmanışın sayıları

```
TIRMANIŞ         0,5 m/s (S2'de 0,7 m/s) · iki basamakta bir nefes ·
                 her eldiven ve bot: bırakır-kalkar-kavrar-yük alır;
                 kayma, süzülme, sıçrama 0 kare
DÜŞÜŞ İVMESİ     2,16 m/s² — SABİT ve HER PARÇADA AYNI:
                 1 s → 1,08 m (2,2 m/s) · 2 s → 4,3 m (4,3 m/s) ·
                 3 s → 9,7 m (6,5 m/s) · 5 s → 27 m (10,8 m/s)
DÜŞÜŞ ÇİZGİSİ    gövde hattına paralel, ÖLÜ DÜZ; kavis, yalpalama,
                 takla, yön değişimi, süzülme, asılı kalma 0 kare
GEÇİŞLER         panel S0: 1,4 m · panel S2: 1,2 m · panel S4: 1,1 m ·
                 latis S5: 1,0 m · latisin tam boyu adamı ~2 saniyede
                 geçer (hızlanarak)
KOPUŞ            temiz makaslama: parça bütün kalır, kenar düz;
                 kırılma, parçalanma, saçılma 0 kare
LATİS DEVRİLMESİ (S3) kök bağlantısında pivot, ~2,3 saniyede 90° —
                 devrilen direk gibi; iki bağda YAKALANIR ve asılı kalır
AĞIRLIKSIZLIK    yalnız S5 · 44,4-46,6 (2,2 s): botlar basamaktan bir
                 el genişliği kalkar, eller merdivende KALIR; şakül
                 şeridi düz çizgisini kaybedip yavaşça kıvrılır; düşen
                 latis hız KAZANMAYI bırakır, kazandığı hızla uzaklaşır
                 [D23 tetiklenemez: gövde bağlı, serbest süzülme yok]
DURAKSAMA        filmde TOPLAM 3,5 saniye (S3'te 1,5 · S4'te 2,0)
```

### 🚫 Negative Bible

```
Kesme yok. Sarsıntı yok. El kamerası yok. Kamera hareketi yok.
Ağır çekim yok. Hız rampası yok. Minyatür/oyuncak görünüm yok.
CGI havası yok. Hava fırçalı cilt yok. Elde alet yok, silah yok.
Metin yok. Filigran yok. İkinci insan yok, yansıma yok.

KONSEPTE ÖZGÜ EKLER:
TEMAS YOK: düşen hiçbir parça adama, merdivene önünde durduğu yere değmez.
KAVİS YOK: düşen parça yörüngesi eğrilmez, yalpalamaz, takla atmaz.
SÜZÜLME YOK: hiçbir nesne asılı kalmaz, yüzmez, sürüklenmez (S5'in
  2,2 saniyelik yanma arası hariç — orada da eller merdivendedir).
SIRT ÜNİTESİ YOK: sırt silueti DÜZ [D79]. Vizör berrak, yansımasız.
ATEŞ/DUMAN/TOZ/KIVILCIM YOK: egzoz konisi ve alev 0 kare; motor yalnız
  kadraj dışı turuncu jant ışığı. Çarpma anı ekranda 0 kare.
GÜNEŞ DİSKİ kadraja girmez. Gezegen yok, ay yok, ikinci gemi yok.
Ekran yok, gösterge yok, HUD yok. Kaplamada işaret/yazı yok.
```

**Negatif bloklara eklenecek kuyruk (her görsel promptun sonuna):**

```
no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark
```

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

```
🔴 EN YÜKSEK RİSK — kartlarda yok, bu dosyada tanımlandı

① TIRMANAN GÖVDENİN EKLEMLENMESİ [D18 akrabası]
        ~40 saniye kesintisiz tırmanış. Bütçe: tek hareket tipi ·
        hız m/s ile sayılı · "each glove releases, rises, closes on
        the next rung and takes weight; each boot lifts, sets and
        takes weight — never sliding, never gliding" 12 promptta ·
        el/ayak ekstrem yakın planı yok.

② SIFIR-G REFLEKSİ — model uzay görünce gövdeyi YÜZDÜRÜR [D23 tersi]
        Ortam kartı 3.5 yapısal panzehir: hiçbir kare sıfır-g'de değil
        (S5'in 2,2 saniyesi hariç, orada eller merdivende). Her
        promptta pozitif ağırlık cümlesi: "his boots stay planted on
        the rungs" + tether şakülü kanıt nesnesi.

KART 3 / D5 / D37 / D79   KASK-VİZÖR-SIRT
        HELMET STATE SCHEDULE: kapalı 6/6, açık 0. D79 çift bloğu
        (düz sırt + berrak vizör) her promptun GÖVDESİNDE — bible'da
        yazmak iki filmde yetmedi.
KART 4 / D20 / D69   İKİNCİ FİGÜR VE KLON
        HUMAN COUNT LOCK her promptta: TAM 1 insan, TAM 1 beyaz suit.
        Yansıtıcı yüzey 0 (mat kaplama, berrak cam). D69'un iki sıcak
        noktası 0 kare: araç biniş/inişi yok, loş iç mekâna giriş yok —
        film hava kilidinin 2 m ÖNÜNDE biter, kapıdan geçiş gösterilmez.
KART 5 / D9 / D13 / D34 / D45 / D50   EKRAN / SAYAÇ / METİN
        Ekran ve yazı üretebilecek nesne 0 — sayaç üç metinsiz kanalda
        (parça · mesafe · jant). "no text" ile çelişen içerik yok [A1].
KART 9 / D104   IŞIK MIKNATISI — zayıflatıldı
        Güneş harekete dik + jant kadraj dışı + kamera A kurulumunda
        hedefte. Dört kanal yine de her promptta (Lighting Bible).

🟡 ORTA RİSK

D12 / D44   AĞIR ÇEKİM — bu filmin en olası tek hatası.
        Düşüş ve geçişler slow-motion çeker. "No slow motion, no speed
        ramp, everything at normal speed" 12 promptta + her hız sayılı.
D26   TETHER/ŞERİT — gergin şerit DÜZ; kısa (2,4 m), yassı dokuma;
        gevşek hâli yalnız S5 twist kanıtında ve yavaş kıvrılma olarak
        sayılı (2 saniyede tek kıvrım).
D31 / D38   RİJİT PARÇA — çarpma ekranda 0 kare; kopuş temiz; parça
        bütün; latis kafesi bükülmez.
D16   YÜZ MORPH — yüz 6 sahnede vizör içinde ve tek. Karşı önlem:
        blok 6/6 birebir + "photographed as a real person".
D42 / D58   VARLIK SÜREKLİLİĞİ — basamak aralığı 0,4 m · panel
        2,0 × 1,2 m · latis 6,0 m · aşınma yerleri · şakül konumu:
        göründüğü her sahnede aynı sayıyla.
D3 / D29 / D41   BLOOM — mat yüzeyler; hale/parlama/huzme yasak;
        güneş diski 0 kare; "glow" ailesi pozitif gövdede 0 kez.
D71   REVEAL — analog perde yok: panel S0'da kadraj İÇİNDE kopar.
        Saklanan novum değil SEBEPTİR (motorun kapanabileceği) [D71
        + ONERME §6 uyumu].

⬛ HER PROMPTTA

D59   POZİTİF İSİMLENDİRME — yasakların yanına pozitif hâl: "its path
        is a dead straight line down the hull, gaining speed every
        second" · "his boots stay planted on the rungs".
D34 / D45   isim yok · köşeli parantez yok · milliyet yok.
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

## 🎬 SAHNE 0 — KANCA: TAŞ GİBİ

_"Uzayın ortasında bir panel koptu. Ve düştü."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 0 of 6. Solo male hull technician hard sci-fi survival film. MAXIMUM VIRAL WRONG-GRAVITY SHOCK.
Lens: 32mm spherical, f/4, ISO 800.
Camera Distance: Fixed mount clamped to the hull beside the airlock ring, 0.5 metres off the plating, looking straight down the hull axis; the climbing man is approximately 14 metres from the lens.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. A slim white tether strap runs from his chest ring down to a runner on the ladder rail below him. He has pressed himself flat against the rungs mid-climb, head turned to follow something that is falling past him.

ENVIRONMENT / BACKGROUND: The bare outer hull of a 320-metre cargo ship under a steady main-engine burn. The camera looks down the hull axis: the ship's bow is behind the camera, and the stern with its engines lies far beyond the bottom vanishing point, never visible. A twin-rail service ladder with rungs every 0.4 metres runs from under the lens straight down the flat spine plating to that vanishing point, which is rimmed deep orange by engine light from far below the frame edge. The plating is bare unpainted grey metal with no marking and no lettering of any kind. In the near foreground a damaged equipment-mounting band crosses the hull; EXACTLY TWO loose hull panels and one six-metre lattice antenna boom still hang on it, quivering. Dense sharp stars fill the black space on both sides of the hull.

THE VIRAL MOMENT / REVEAL: A third hull panel, 2.0 by 1.2 metres of bare grey metal, has torn off the band and is FALLING — dropping away from the lens straight down the hull line, flat against the plating, passing 1.4 metres to frame right of the climbing man, visibly accelerating, shrinking toward the orange-rimmed vanishing point. Beside the stars, in open space, it falls like a stone. Nothing touches him at any point; the nearest passing object misses him by 1.4 metres.

COMPOSITION: Vertical 9:16. The climbing man sits just left of centre between roughly thirty-five and fifty-eight percent of frame height, held clear of the outer right eighth. The falling panel reads at roughly fifty-eight to seventy percent at frame right, already smaller than him and getting smaller. The damaged band with its two remaining panels and the lattice boom fills the upper foreground between roughly ten and thirty percent. The hull runs to a vanishing point at roughly eighty-two percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only far plating and the orange rim.

LIGHTING: Hard white sunlight rakes across the hull from outside frame left; every shadow is razor-edged and absolutely black, with no fill in the shadow sides. His face reads through the clear visor, keyed warm by the chest console. Deep orange engine light from far below the bottom frame edge rims only the downward-facing edges of the plating and the falling panel. The white suit is the brightest object in the frame. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn, so every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second — about one metre in the first second, almost ten by the third — on a dead straight line, never curving, never drifting sideways, never hovering. Hard vacuum: no dust, no haze, no sound. He weighs about a fifth of his Earth weight and his boots stay planted on the rungs. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm spherical, on a fixed mount clamped to the hull beside the airlock ring, 0.5 metres off the plating, looking straight down the hull axis; the ship's bow is behind the camera, the stern far beyond the bottom vanishing point. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — A man in a snow-white hard-shell EVA suit is already mid-climb on a twin-rail service ladder, 14 metres from the lens, coming up the hull toward the camera at a steady half metre per second, his head returning to the front from a glance down over his right shoulder. His suit has a completely flat back and an optically clear visor; his face is fully readable through the glass and each exhale briefly fogs its lower edge. The bare grey hull runs away below him to a vanishing point rimmed deep orange.
At 1.5s — In the near foreground a damaged mounting band crosses the hull, holding two loose panels and a six-metre lattice boom. Two shorn bolts drop off the band and fall away down the hull line in dead straight lines, shrinking and gaining speed.
At 3s — The nearest panel, two metres of bare grey metal, tips outward and hangs quivering on its last bolt row.
At 5s — The panel tears free and FALLS: it drops away from the lens straight down the hull line, flat against the plating, visibly accelerating.
At 5.8s — The deep orange rim at the vanishing point dips dark for less than half a second and returns. He does not react to it.
At 7.3s — The panel passes 1.4 metres to frame right of the climbing man at about five metres per second. Nothing touches him. He flattens himself against the rungs.
By 8s — The panel is a shrinking dot far below him, still gaining speed. He takes the next rung and turns his head down over his right shoulder, following it. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image.
The camera stays perfectly locked off for the whole 8 seconds — it never pans, never tilts, never moves, never shakes. The man keeps climbing the ladder up the hull toward the lens at a steady half metre per second, each glove releasing, rising, closing on the next rung and taking weight, each exhale briefly fogging the lower edge of his clear visor. In the near foreground two shorn bolts drop off the damaged band and fall away down the hull line in dead straight lines. The nearest loose panel tips outward, quivers on its last bolt row, then tears free and falls away from the lens, flat against the plating, visibly gaining speed; it passes about a metre and a half to frame right of him and shrinks toward the orange-rimmed vanishing point far below. The deep orange rim dips dark for less than half a second and returns; he does not react to it. He flattens himself against the rungs, then takes the next rung and turns his head down over his right shoulder, following the falling panel.
Every falling object moves on a dead straight line, never curving, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed hull mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 1 — AŞAĞI YOL DÜŞTÜ

_"İniş diye bir seçenek yoktu. Artık yok."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 1 of 6. Solo male hull technician hard sci-fi survival film.
Lens: 32mm spherical, f/4, ISO 800.
Camera Distance: Fixed mount clamped to the ladder rail six metres below the man's starting position, 0.4 metres off the plating, looking straight up the hull axis; the climbing man is approximately 8.5 metres from the lens.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. A slim white tether strap runs from his chest ring down to a runner on the ladder rail. He is climbing away from the lens, boots set on the rungs, head turned down over his right shoulder to look past the camera at the hole below him.

ENVIRONMENT / BACKGROUND: The bare outer hull of a 320-metre cargo ship under a steady main-engine burn, seen looking up the hull axis: the ship's bow is beyond the top of frame and the stern with its engines lies far behind the camera, below the bottom frame edge, never visible. The twin-rail service ladder climbs from the lens up the flat spine plating; high in the frame, the small round porthole of the airlock ring carries a warm interior light, 12 metres above the man. Between him and the airlock, the damaged mounting band still holds EXACTLY TWO loose panels and one six-metre lattice antenna boom. The plating is bare unpainted grey metal with no marking of any kind. Dense sharp stars fill the black space on both sides of the hull.

THE VIRAL MOMENT / REVEAL: Between the climbing man and the lens, a three-metre section of ladder rail with four rungs has just torn out of the hull and is falling toward the camera — flat and straight, growing in frame, about to pass 0.6 metres to frame left of the lens. Where it tore away, four shorn stubs stand in the plating: the way back down the ladder no longer exists. Nothing touches him at any point; the falling rail section is below him and moving away from him.

COMPOSITION: Vertical 9:16. The climbing man sits between roughly thirty-four and fifty-two percent of frame height, held clear of the outer right eighth. The falling rail section reads large at roughly fifty-five to eighty-five percent at frame left, sharp-edged and growing. The damaged band and the hanging lattice boom stack between roughly fourteen and thirty percent; the warm porthole light sits at roughly six to ten percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near plating and the dark mass of the falling rail.

LIGHTING: Hard white sunlight rakes across the hull from outside frame left; razor-edged, absolutely black shadows, no fill. His face reads through the clear visor, keyed warm by the chest console; the airlock porthole is the second warm point in a cold frame. Deep orange engine light rims only the downward-facing edges, entering from below the bottom frame edge. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn: every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second, on a dead straight line, never curving, never drifting, never hovering. Hard vacuum: no dust, no haze, no sound. He weighs about a fifth of his Earth weight; his boots stay planted on the rungs and each glove closes fully on its rung before taking weight. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm spherical, on a fixed mount clamped to the ladder rail, 0.4 metres off the plating, looking straight up the hull axis; the ship's bow is beyond the top of frame, the stern far behind the camera. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — The up-view opens: the man in the white suit is 8.5 metres above the lens, climbing away up the twin-rail ladder toward the warm porthole light of the airlock high in the frame. A low shudder from the last tear is still shivering through the ladder, felt more than heard. His suit has a completely flat back and an optically clear visor.
At 1.5s — He tugs the next rung hard, twice, before trusting it with his weight. It holds. Two rungs per breath; the exhale fogs the lower edge of the glass.
At 3s — A rung bracket rocks under his glove. He shifts his grip wider and keeps climbing at half a metre per second.
At 5.3s — Below his boots — between him and the lens — a three-metre section of ladder rail with four rungs shears out of the hull and falls toward the camera, flat and straight, visibly gaining speed. Four shorn stubs remain in the plating.
At 6.5s — He looks down over his right shoulder, past the lens, at the hole it left. The way back down no longer exists. He turns back up and climbs.
By 8s — The falling rail section reaches the lens, passes 0.6 metres to frame left of it, and its dark mass fills the frame completely for the final half second. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the closing frame of the previous shot, the up-view along the ladder with the man climbing away above the lens.
The camera stays perfectly locked off for the whole 8 seconds — it never pans, never tilts, never moves, never shakes. He climbs away from the lens toward the warm porthole light high in the frame, two rungs per breath, tugging the next rung twice before trusting it. A rung bracket rocks under his glove and he shifts his grip wider. Then, below his boots and between him and the lens, a three-metre section of ladder rail with four rungs shears out of the hull and falls toward the camera, flat and straight, visibly gaining speed, leaving four shorn stubs in the plating. He looks down over his right shoulder at the hole it left, turns back up and keeps climbing. In the final half second the falling rail passes just beside the lens and its dark mass fills the frame.
Every falling object moves on a dead straight line, never curving, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed rail mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 2 — TEMPO

_"Cevabı panik değil. Hız."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 2 of 6. Solo male hull technician hard sci-fi survival film.
Lens: 75mm spherical, f/2.8, ISO 800, shallow depth of field.
Camera Distance: Fixed mount at the tip of a folded cargo crane arm, 7 metres off the hull face, level with the man, looking side-on at the hull; the bow direction is up the frame, the stern direction down the frame.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. A slim white tether strap runs from his chest ring down to a runner sliding on the ladder rail below him. He is climbing at full drive, one arm reaching high, jaw set, torso square to the ladder.

ENVIRONMENT / BACKGROUND: The sheer hull face of a 320-metre cargo ship under a steady main-engine burn, seen side-on and compressed by the long lens into a flat grey wall of bare unpainted plating with no marking of any kind. The twin-rail service ladder crosses the frame vertically, rungs every 0.4 metres. Black space and dense sharp stars edge the frame. The bow direction is up the frame; the stern and engines lie far down the frame line, never visible.

THE VIRAL MOMENT / REVEAL: EXACTLY ONE loose hull panel, 2.0 by 1.2 metres of bare grey metal, is crossing the frame from top to bottom 1.2 metres beyond him — flat, sharp-edged, mid-fall on a dead straight line parallel to the ladder, gone in under half a second. His climb does not stop for it: his tempo has RISEN. Nothing touches him at any point; the nearest passing object misses him by 1.2 metres.

COMPOSITION: Vertical 9:16. The man fills the frame between roughly twenty and seventy-two percent of frame height, just left of centre, held clear of the outer right eighth. The crossing panel reads as a dark slab at roughly thirty to fifty-eight percent at frame right, sharply rendered, not blurred. The ladder rails run the full height of the frame. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only plating and the lower ladder.

LIGHTING: Hard white sunlight rakes across him from outside frame left; razor-edged, absolutely black shadows, no fill. The white suit is the brightest object in the frame; his face reads through the clear visor, keyed warm by the chest console. A thin deep orange rim of engine light enters only at the very bottom frame edge. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn: every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second, on a dead straight line, never curving, never drifting, never hovering. Hard vacuum: no dust, no haze, no sound. He climbs at 0.7 metres per second; each glove releases, rises, closes on the next rung and takes weight; each boot lifts, sets and takes weight — never sliding, never gliding. His boots stay planted on the rungs. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm spherical, on a fixed mount at the tip of a folded cargo crane arm, 7 metres off the hull face, level with the man, looking side-on at the hull; the bow direction is up the frame, the stern direction down the frame. Shallow depth of field. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — The frame opens filled by the dark torn rail section, which drops out of the bottom of frame within half a second and reveals a tight side view: the man in the white suit climbing the twin-rail ladder on the sheer grey hull wall, seven metres from the lens.
At 1.5s — His rhythm is exact: two rungs per breath, each exhale fogging the lower edge of the clear visor, the white tether runner clicking up the rail below him. His suit has a completely flat back.
At 2.8s — A shudder runs through the hull into his gloves. He freezes for half a beat, gloves locked on the rungs.
At 3.5s — A loose hull panel CROSSES the frame from top to bottom 1.2 metres beyond him, flat and sharp, on a dead straight line parallel to the ladder, gone in under half a second. It makes no sound at all. Nothing touches him.
At 4.5s — His tempo rises from half a metre per second to 0.7: reach, close, pull, step, without a single wasted motion.
At 6.5s — He throws one look up along the hull toward the top edge of frame, where the lattice boom waits beyond the frame line, then drives on.
At 7.2s — He climbs out through the top of frame; the empty grey wall and the ladder hold for the final half second. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the closing frame of the previous shot, almost entirely filled by the dark falling rail section close to the lens.
In the first half second that dark mass drops out of the bottom of frame, and the camera then holds, perfectly locked off on the crane arm, with absolutely zero movement for the remaining seven and a half seconds. The tight side view shows the man climbing the twin-rail ladder on the sheer grey hull wall, two rungs per breath, the tether runner clicking up the rail below him. A shudder runs through the hull into his gloves and he freezes for half a beat. Then a loose hull panel crosses the frame from top to bottom just beyond him, flat and sharp, on a dead straight line parallel to the ladder, gone in under half a second, in total silence. His tempo rises: reach, close, pull, step, faster now but never sloppy. He throws one look up along the hull toward the top edge of frame, then climbs out through the top of frame, leaving the empty grey wall and the ladder for the final half second.
Every falling object moves on a dead straight line, never curving, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed crane-arm mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 3 — LATİS (ikinci görsel şok)

_"Tehdit artık rastgele değil. Nişanlı."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 3 of 6. Solo male hull technician hard sci-fi survival film. MAXIMUM VIRAL WRONG-GRAVITY SHOCK.
Lens: 32mm spherical, f/4, ISO 800.
Camera Distance: Fixed mount clamped to the ladder rail, 0.4 metres off the plating, looking straight up the hull axis; the climbing man is approximately 11 metres from the lens.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. A slim white tether strap runs from his chest ring down to a runner on the ladder rail. He is frozen mid-climb, both boots set, gloves locked on the rungs, head tipped back to look at the thing hanging above him.

ENVIRONMENT / BACKGROUND: The bare outer hull of a 320-metre cargo ship under a steady main-engine burn, seen looking up the hull axis: the ship's bow is beyond the top of frame, the stern with its engines far behind the camera below the bottom frame edge, never visible. The twin-rail service ladder climbs the flat spine plating, rungs every 0.4 metres. The warm porthole light of the airlock sits high in the frame, 7 metres above the man. The plating is bare unpainted grey metal with no marking of any kind. Dense sharp stars fill the black space on both sides of the hull. On the damaged band, no loose panels remain.

THE VIRAL MOMENT / REVEAL: The six-metre lattice antenna boom has torn its outboard mounting and swung down through ninety degrees like a felled mast — and STOPPED, caught on two root struts. It hangs tip-down directly over the ladder line, swaying by centimetres, its open latticework black against the starfield, its tip 0.8 metres above his helmet. The threat is no longer random: everything still hanging above him hangs over his only path. Nothing touches him at any point.

COMPOSITION: Vertical 9:16. The hanging lattice boom dominates the upper frame between roughly eight and forty-six percent of frame height, tip pointing down at the man. The man sits between roughly fifty and seventy-two percent, small under it, held clear of the outer right eighth. The warm porthole light reads at roughly five to eight percent, beyond the lattice. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only near plating and the lower ladder.

LIGHTING: Hard white sunlight rakes across the hull from outside frame left; razor-edged, absolutely black shadows, no fill. The lattice reads as a hard black silhouette edged with thin white sun lines. His face reads through the clear visor, keyed warm by the chest console. Deep orange engine light enters only from below the bottom frame edge. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn: every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second, on a dead straight line, never curving, never drifting, never hovering. The boom pivoted on its root fitting in about two seconds and was caught rigidly; it does not bend and does not shed pieces except one thin antenna whip. Hard vacuum: no dust, no haze, no sound. His boots stay planted on the rungs. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm spherical, on a fixed mount clamped to the ladder rail, 0.4 metres off the plating, looking straight up the hull axis; the ship's bow is beyond the top of frame, the stern far behind the camera. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — The up-view opens: the man in the white suit is eleven metres above the lens, mid-climb toward the warm porthole light of the airlock high in the frame. A deep metallic groan is conducted through the ladder into his gloves, heard as a muffled shudder inside the suit.
At 1.5s — The six-metre lattice antenna boom tears its outboard mounting and swings down through ninety degrees like a felled mast, its tip sweeping down the hull line straight at the ladder.
At 3.2s — Two root struts catch it. The lattice STOPS, hanging tip-down directly over the ladder, its tip 0.8 metres above his helmet, swaying by centimetres. The whole ladder shivers under his gloves. He is frozen, both boots set.
At 4.5s — Outside the suit there is absolute silence; inside, only his breath, faster now.
At 5.5s — He starts climbing again — beside it. The ladder passes 0.4 metres from the hanging latticework; his shoulder clears it by a hand's width. Each glove releases, rises, closes on the next rung and takes weight.
At 6.8s — A thin antenna whip, one and a half metres long, snaps off the boom's tip and falls toward the camera on a dead straight line, gaining speed.
By 8s — The whip passes 0.2 metres from the lens and its thin dark line fills the frame for the final half second. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the up-view along the ladder, the man climbing high above the lens toward the warm porthole light.
The camera stays perfectly locked off for the whole 8 seconds — it never pans, never tilts, never moves, never shakes. A deep metallic groan shivers through the ladder. The six-metre lattice antenna boom tears its outboard mounting and swings down through ninety degrees like a felled mast, its tip sweeping down the hull line straight at the ladder — and two root struts catch it. It hangs tip-down directly over the ladder, swaying by centimetres, its tip just above his helmet. He freezes, both boots set, head tipped back. Then he starts climbing again, beside it, his shoulder clearing the black latticework by a hand's width. Near the end a thin antenna whip snaps off the boom's tip and falls toward the camera on a dead straight line, gaining speed; in the final half second it passes just in front of the lens and its thin dark line fills the frame.
Every falling object moves on a dead straight line, never curving, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed rail mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 4 — KARABİNER (kriz · merkezi seçim)

_"Korunmayı zamana takas etti."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 4 of 6. Solo male hull technician hard sci-fi survival film.
Lens: 75mm spherical, f/2.8, ISO 800, shallow depth of field.
Camera Distance: Fixed mount at the tip of a folded cargo crane arm, 7 metres off the hull face, level with the man, looking side-on at the hull; the bow direction is up the frame, the stern direction down the frame.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. He has stopped at the end of his taut white tether strap, which runs from his chest ring down to a runner jammed under a bent rail bracket; his right thumb rests on the karabiner gate at his chest ring, his eyes down on it, his mouth open on a broken breath.

ENVIRONMENT / BACKGROUND: The sheer hull face of a 320-metre cargo ship under a steady main-engine burn, seen side-on and compressed by the long lens: a flat wall of bare unpainted grey plating with no marking of any kind, the twin-rail ladder crossing the frame vertically. The hanging lattice boom fills the left eighth of the frame in soft shallow focus, its black struts out of focus but unmistakable, 0.4 metres from his shoulder. Black space and dense sharp stars edge the frame. The bow direction is up the frame; the stern and engines lie far down the frame line, never visible.

THE VIRAL MOMENT / REVEAL: Everything above him now hangs by ONE fitting: of the two root struts holding the lattice, one has just snapped with a conducted crack, and the boom has dropped thirty centimetres and caught again. The last loose hull panel is a dark rush at the frame edge, mid-fall, passing 1.1 metres beyond him. And his answer is the film's central choice: the thumb on the karabiner gate — trading his only protection for time. Nothing touches him at any point.

COMPOSITION: Vertical 9:16. The man fills the frame between roughly sixteen and seventy-four percent of frame height, his helmet and chest ring in the sharpest plane, his face readable between roughly twenty-six and forty percent. The taut white tether runs from his chest down toward the bottom frame edge, leaving frame before the bottom quarter. The lattice occupies the left eighth, soft. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only defocused plating and the strap's exit line.

LIGHTING: Hard white sunlight rakes across him from outside frame left; razor-edged, absolutely black shadows, no fill. His face reads clearly through the clear visor, keyed warm by the chest console — the warmest light in the film so far. A thin deep orange rim of engine light enters only at the very bottom frame edge. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn: every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second, on a dead straight line, never curving, never drifting, never hovering. The taut tether strap is dead straight under load. Hard vacuum: no dust, no haze, no sound. His boots stay planted on the rungs. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm spherical, on a fixed mount at the tip of a folded cargo crane arm, 7 metres off the hull face, level with the man, looking side-on at the hull; the bow direction is up the frame, the stern direction down the frame. Shallow depth of field. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — The frame opens filled by a thin dark antenna whip, which drops out of the bottom of frame within half a second and reveals a close side view: the man in the white suit beside the hanging lattice, its black struts soft at frame left, his face readable through the clear visor.
At 1s — He climbs half a metre and the white tether strap comes TAUT, stopping his reach mid-air. He pulls the runner twice with his left hand: it is jammed under a bent rail bracket.
At 2.4s — The last loose hull panel falls past 1.1 metres beyond him, a dark rush crossing the frame in under half a second. On its heels a conducted CRACK: one of the two root struts holding the lattice snaps. The lattice drops thirty centimetres and catches. Everything above him now hangs by one fitting.
At 3.2s to 5.2s — He goes completely still for two full seconds. His eyes drop to the karabiner on his chest ring, rise to the lattice, drop again. His breathing breaks once, then resets.
At 5.6s — His right thumb flicks the karabiner gate open. The strap slips off the chest ring, swings down and hangs from the jammed runner: a dead-straight white plumb line pointing down the hull.
At 6.2s — He climbs past the bent bracket, unprotected, into the shadow of the hanging lattice; the gap between his shoulder and the latticework is 0.4 metres. The sound narrows to breath and the faint suit fan.
By 8s — He is still climbing when the frame ends; the white strap hangs rigid and dead straight below him. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, never hovering, and nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the closing frame of the previous shot, crossed by the thin dark antenna whip close to the lens.
In the first half second the whip drops out of the bottom of frame, and the camera then holds, perfectly locked off on the crane arm, with absolutely zero movement for the remaining seven and a half seconds. The close side view shows the man beside the hanging lattice, its black struts soft at the left edge, his face readable through the clear visor. He climbs half a metre and his white tether strap comes taut, stopping his reach mid-air; he pulls the runner twice — jammed under a bent rail bracket. The last loose panel falls past just beyond him, a silent dark rush, and on its heels a conducted crack: one of the two root struts snaps, the lattice drops thirty centimetres and catches. He goes completely still for two full seconds, eyes moving between the karabiner on his chest ring and the lattice, his breathing breaking once. Then his thumb flicks the karabiner gate open; the strap slips off, swings down and hangs from the jammed runner as a dead-straight white plumb line. He climbs past the bent bracket, unprotected, the gap between his shoulder and the latticework less than half a metre, and he is still climbing when the frame ends.
Nothing touches him. His boots stay planted on the rungs. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed crane-arm mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 5 — YANMA ARASI (doruk + twist + döngü)

_"Düşüş bitti. İki saniyeliğine her şey bitti."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 5 of 6. Solo male hull technician hard sci-fi survival film. MAXIMUM VIRAL SHOCK.
Lens: 32mm spherical, f/4, ISO 800.
Camera Distance: Fixed mount clamped to the hull beside the airlock ring, 0.5 metres off the plating, looking straight down the hull axis; the climbing man is approximately 4 metres from the lens.

SUBJECT: A 34-YEAR-OLD MAN, an orbital hull technician — light brown skin with clearly visible pore texture, sweat beading at the hairline, dark eyes narrowed with effort, thick dark eyebrows, two days of dark stubble, a small old burn scar on the left jaw, chapped lips parted for breathing, natural facial asymmetry. Photographed as a real person, not CGI. He is 1.78 metres tall and wiry. He wears a snow-white hard-shell EVA suit with a completely FLAT back — no backpack, no tank, no hose, no cable, no rear housing of any kind. The visor is optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; his face is fully readable through it at every head angle, lit from inside by a low warm key from the small chest console fifteen centimetres below his chin, and each exhale briefly fogs the lower edge of the glass. The suit is plain matt white with scuffed dark-grey knees, forearms and boot toes that stay identical in every scene, and it carries no patch, no flag, no lettering, no digits and no symbol anywhere. His white gloves have grey palms and hold only the ladder rungs — no tool, no phone, no weapon. His chest ring is EMPTY — no tether hangs from it. He is flat against the rungs, head turned to follow the huge thing sliding past him.

ENVIRONMENT / BACKGROUND: The bare outer hull of a 320-metre cargo ship, seen looking down the hull axis: the ship's bow is behind the camera, the stern with its engines far beyond the bottom vanishing point, never visible. The edge of the airlock ring enters the frame margin near the lens. The twin-rail service ladder runs from under the lens down the flat spine plating. Far down the ladder a white strap hangs from a jammed runner. The plating is bare unpainted grey metal with no marking of any kind. Dense sharp stars fill the black space on both sides of the hull.

THE VIRAL MOMENT / REVEAL: The last root fitting has sheared and the whole six-metre lattice antenna boom is sliding straight down the hull line, 1.0 metres to frame left of the ladder, already below him and gaining speed, its open black latticework framing him for a moment as it passes. Below it waits the orange-rimmed vanishing point. Nothing touches him at any point; the passing lattice misses him by 1.0 metres.

COMPOSITION: Vertical 9:16. The man fills the frame between roughly twenty-eight and sixty-four percent of frame height, growing toward the lens, held clear of the outer right eighth. The sliding lattice reads between roughly forty and seventy-two percent at frame left, its far end shrinking. The white strap is a thin line at roughly sixty-six to seventy-four percent. The vanishing point sits at roughly eighty-two percent, rimmed deep orange. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only far plating, the strap's lower line and the orange rim.

LIGHTING: Hard white sunlight rakes across the hull from outside frame left; razor-edged, absolutely black shadows, no fill. His face reads through the clear visor, keyed warm by the chest console. Deep orange engine light from far below the bottom frame edge rims the downward-facing edges and the sliding lattice. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

PHYSICS: The ship is under a steady 0.22 g burn: every loose object falls straight down the hull line toward the stern, gaining 2.16 metres per second of speed each second, on a dead straight line, never curving, never drifting, never hovering. The six metres of lattice take about two seconds to slide past him, faster at the tail than at the tip. Hard vacuum: no dust, no haze, no sound. His boots stay planted on the rungs. Everything moves at normal speed.

NEGATIVE: HUMAN COUNT LOCK: exactly one human being appears in this frame — the climbing technician in the white suit. no second astronaut, no duplicate of him, no human reflection, no contact between any falling object and his body, no touching, no tumbling end over end, no curving fall, no sideways drift, no floating debris, no hovering, no swirling dust, no dust, no smoke, no fire, no sparks, no explosion, no debris field, no shattering, no bending ladder, no backpack, no tank, no hose, no cable on his back, no visor tint, no mirror coating, no slow motion, no speed ramp, no motion blur trails, no camera shake, no lens flare, no visible sun disc, no visible engine plume, no atmospheric haze, no planet, no moon, no second ship, no bloom, no glow filter, no halo, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT — A SÜRÜMÜ (T2V)

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm spherical, on a fixed mount clamped to the hull beside the airlock ring, 0.5 metres off the plating, looking straight down the hull axis; the ship's bow is behind the camera, the stern far beyond the bottom vanishing point. Absolutely zero camera movement. Real-time motion at normal playback speed throughout.

At 0s — The down-view opens: the man in the white suit is four metres from the lens, climbing toward the camera; beside him the six-metre lattice boom hangs on its last fitting. His chest ring is empty; far below, a white strap hangs dead straight from the rail. The vanishing point far down the hull is rimmed deep orange.
At 0.8s — The last fitting shears with a crack he feels through his gloves. The lattice begins to slide straight down the hull line, 1.0 metres to frame left of the ladder.
At 1.2s to 2.8s — The full six metres of open black latticework slide past him, gaining speed the whole way; his head tracks it while his body stays flat on the rungs. Nothing touches him.
At 3.5s — The lattice shrinks toward the orange-rimmed vanishing point, still gaining speed, and is gone among the far plating.
At 4.4s — The deep orange rim at the vanishing point dies completely, and the faint rumble in the ladder stops with it. His boots drift a hand's width off the rung while his gloves keep hold; far below the white strap begins to curl very slowly.
At 5.5s — Only his breath and the faint fan. He looks down at his own drifting boots.
At 6.6s — The rumble returns through the ladder, the orange rim relights, and his boots settle back onto the rung.
At 7.2s — He takes the next rung — the edge of the airlock ring is now two metres from the lens — and turns his head down over his right shoulder as the shot ends mid-motion. No cuts within the shot.

HUMAN COUNT LOCK: exactly one human being in this shot — the climbing technician in the white suit; no second figure, no reflection. Every falling object moves on a dead straight line down the hull, never curving, never drifting, and nothing touches him. Everything moves at normal speed. No slow motion, no speed ramp. No bloom, no glow filter, no lens flare, no visible sun disc, no visible engine plume. No readable text anywhere.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

### 🎥 VİDEO PROMPT — B SÜRÜMÜ (I2V · DEVAM KARESİ)

```
The scene begins exactly as the provided image — the down-view from beside the airlock ring, the man climbing toward the lens with the lattice boom hanging on its last fitting beside him.
The camera stays perfectly locked off for the whole 8 seconds — it never pans, never tilts, never moves, never shakes. The last fitting shears with a crack he feels through his gloves, and the whole six-metre lattice slides straight down the hull line a metre from the ladder, gaining speed the whole way; his head tracks it while his body stays flat on the rungs, and it shrinks toward the orange-rimmed vanishing point and is gone. Then the orange rim dies completely and the constant faint rumble stops with it: his boots drift a hand's width off the rung while his gloves keep hold, and far below the white strap loses its dead-straight line and begins to curl very slowly. For two seconds, only his breath and the faint fan. He looks down at his own drifting boots. Then the rumble returns, the orange rim relights, his boots settle back onto the rung, and he takes the next rung — the airlock ring edge now close to the lens — turning his head down over his right shoulder as the shot ends mid-motion.
Nothing touches him. Everything moves at normal speed — no slow motion, no speed ramp.
Camera: fixed hull mount, absolutely zero movement, no shake, no drift, no zoom.
No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. Photorealistic live-action cinematography.
```

---

## 🎶 MÜZİK PROMPTU (Tek Global Tema — 48 sn)

Araç: Suno / Udio · tek parça · 48 saniye · söz yok, geleneksel melodi yok.
Tempo **120 BPM**: 8 saniyelik sahne = tam 16 vuruş = 4 ölçü — her sahne
sınırı bir ölçü çizgisine oturur (GOOGLE_FLOW_MUSIC §14 hizalama).

```
48-second instrumental survival cue, no vocals, no lyrics, no traditional melody, 120 BPM, mechanical and patient. NO DRUM KIT AND NO CYMBALS — the only percussive events are three deep sub-bass drops fired on story impacts, never as musical accents. THREE LAYERS ONLY: 1. THE BURN: a low continuous engine-room drone with a slow pulse on beats one and three, completely unchanging in pitch and level — it is the ship's burn, and it must feel like a room tone with a heartbeat. 2. THE CLIMB: a dry, damped, plucked four-note ascending cell, one cell per bar, that shifts UP one scale step at the start of every 8-second scene — six scenes, six rungs of a musical ladder, never resolving. 3. THE DROPS: a single deep 45 Hz sub-bass drop doubled by a 110 Hz harmonic so it survives a phone speaker, fired exactly three times: at 5.0 seconds, at 26.0 seconds and at 40.8 seconds.

Dynamic arc: 0.0-2.5s no music at all, only a faint conducted mechanical bed. Layer 1 enters at 2.5s and locks; layer 2 enters at 8.0s with the second scene. 16-24s layer 2 tightens to double-time cells while layer 1 stays identical. 24-32s layer 2 thins to single held notes under the second drop's long decay. 32-40s the cell climbs its highest steps, sparse, with silence between notes. At 40.8s the third drop lands. At 44.4s EVERYTHING STOPS DEAD — layer 1 cuts mid-pulse as if the power itself failed, and for 2.2 seconds there is NO MUSIC AT ALL. At 46.6s layer 1 alone returns exactly as it began, same pitch, same level, unresolved, and CUTS flat at 48.0s with no fade, no cadence and no final chord, so it butts straight onto the opening beat.

Mood: mechanical, vertical, unglamorous, patient. No triumph, no horror sting, no release. Reference feel: the tectonic low-register patience of Jóhann Jóhannsson and the dry single-cell repetition of Mica Levi. Do not quote, sample or reproduce any melody, motif or lyric from either.

NO vocals, NO lyrics, NO choir, NO screams, NO orchestral swell, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO horror stinger, NO jump-scare hit, NO drum kit, NO snare, NO cymbals, NO guitar, NO field recording.
```

> **Yapı filmi birebir izler.** Katman 1 = motor: 44,4'te motorla
> birlikte ÖLÜR ve 46,6'da motorla birlikte döner — müziğin ana katmanı
> twist'in diegetik kaderini paylaşır. Katman 2 = tırmanış: her sahnede
> bir basamak yukarı, hiç çözülmez. Üç sub darbe üç kopuştur: panel
> (5,0) · latisin yakalanışı (26,0) · son bağ (40,8).
> ⭐ **44,4-46,6 TAM 2,2 SANİYE MÜZİKSİZDİR** [MUSIC §10 ·
> KARAKTER_VE_DUYGU §5.3 "her şey kayboldu" yuvası]: ağırlıksızlık
> sessizlikte geçer; geriye yalnız nefes ve kask fanı kalır — mutlak
> dijital sıfır 0,0 saniyedir [D83]. 48'de kadans yok: parça düz
> kesilir ve 0:00'ın ilk vuruşuna oturur (loop kuralı ③).

---

## 🖼️ KAPAK PROMPTU (1080×1920)

⚠️ **Bu görsel videoya GİRMEZ** — yalnızca thumbnail [Ders 61].

> **Kaynak an: S0 · 0:05-0:06.** 120 px'te okunması gereken şey İKİ
> ŞEKİL VE BİR ÇİZGİDİR: ortada asılı duran küçük BEYAZ bir figür,
> yanında ondan ayrık, DÜŞEN koyu bir dikdörtgen, ve ikisinin altında
> daralarak turuncu bir çizgiye inen gri gövde hattı. Sorulacak soru
> iki şeklin YÖN FARKIDIR: *biri neden düşüyor, öbürü neden düşmüyor?*

```
Cinematic photorealistic vertical cover image, 1080x1920, 9:16. The bare outer hull of a 320-metre cargo ship under a steady main-engine burn, seen from a fixed camera beside the airlock ring looking straight down the hull axis; the ship's bow is behind the camera and the stern with its engines lies far beyond the bottom vanishing point, never visible.

A 34-year-old male hull technician in a snow-white hard-shell EVA suit clings to a twin-rail service ladder 14 metres below the camera, pressed flat against the rungs, his head turned toward the thing falling beside him. His suit has a completely flat back — no backpack, no tank, no hose — and an optically clear visor through which his face is readable, lit warm by his chest console. The suit is plain matt white with scuffed dark-grey knees and carries no patch, no flag, no lettering anywhere.

Passing 1.4 metres beside him, a bare grey hull panel, 2.0 by 1.2 metres, is in mid-fall — dropping straight down the hull line toward the stern, flat against the plating, visibly smaller than him and shrinking, on a dead straight line. In open space, beside dense sharp stars, it falls like a stone.

The plating is bare unpainted grey metal with no marking of any kind. A damaged mounting band with one hanging six-metre lattice boom crosses the upper foreground. The hull runs down to a vanishing point rimmed deep orange by engine light from far below the frame edge.

COMPOSITION: The white figure sits just left of centre between roughly thirty-five and fifty-eight percent of frame height; the falling panel between roughly fifty-eight and seventy percent at frame right; the orange-rimmed vanishing point at roughly eighty-two percent. Nothing story-critical falls in the top 254 pixels, the bottom 484 pixels, or the right 242 pixels; those bands are covered by platform UI.

LIGHTING: Hard white sunlight rakes across the hull from outside frame left; razor-edged, absolutely black shadows, no fill. The white suit is the brightest object in the image; the deep orange rim is the only saturated colour. No bloom, no glow filter, no lens flare, no halo, no visible sun disc, no visible engine plume, no atmospheric haze.

NEGATIVE: Exactly one human being, no second astronaut, no duplicate, no human reflection, no mirrors. No contact between the panel and his body, no touching. No curving fall, no tumbling, no floating debris, no hovering. No dust, no smoke, no fire, no sparks, no explosion, no debris field. No backpack, no tank, no hose, no visor tint, no mirror coating. No slow-motion trails, no motion blur streaks. No planet, no moon, no second ship. Not miniature, no CGI look, no waxy skin. No bloom, no glow filter, no lens flare, no halo. No text, no letters, no digits, no flag, no logo, no patch, no HUD overlay, no watermark.

Output: 9:16, 1080x1920, no text, no watermark.
```

**120 px testi:** küçültüldüğünde okunması gereken tek şey → *gri bir
şeridin üstünde asılı KÜÇÜK BEYAZ bir leke, hemen yanında ondan ayrık
KOYU bir leke, altlarında turuncu bir çizgiye daralan koyu boşluk.*
İki leke birbirine değiyorsa, ya da beyaz leke gri kadranda
ayrışmıyorsa kapak başarısızdır, yeniden üret. Bu kapağın tek işi
**yön farkını** göstermektir: biri tutunuyor, biri düşüyor.

> Kapak denetimi 120 px posta pulu testiyle elle yapılır (KAPAK_QA
> rubriği 12.08.2026'da kaldırıldı).

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ

**Başlık alternatifleri (≤40 karakter):**

```
1. Uzayda her şey düşüyor
2. Motor yandığı sürece aşağı var
3. Uzayda yokuş
```

**Açıklama (ilk satır kancadır):**

```
Uzayda düşemezsin sanıyordun.
Motor çalıştığı sürece geminin bir "aşağısı" var — ve o, dışarıda
merdivende yakalandıysan, bir uçurumdur. 48 saniye, tek nefes.
#uzay #astronot #bilimkurgu #shorts #ai
```

**Sabitlenecek yorum:** "Sabit 0,22g itkideki bir gemiden bıraktığın
cıvata 3 saniyede 9,7 metre 'düşer' — yerçekimi değil, gemi ona doğru
hızlanıyor. Filmdeki her düşüş bu hesapla yazıldı; ekranda imkânsız
olan hiçbir şey yok. 🔩"

### 🤐 SPOILER BÜTÇESİ — dört yüzey, tek bütçe [D114 · PAKETLEME §5]

| Yüzey | Ne verir | Ne vermez |
|---|---|---|
| Başlık | evrenin kuralını: uzayda her şey düşüyor | latisi, tether seçimini, motorun susacağını |
| Kapak | S0'ın fiziksel anını: adamın yanından düşen panel | latisi, şakülü, yanma arasını |
| Fragman | **yok** — bağımsız dikey film (DIKEY_MIKRO_DRAMA §6) | — |
| Açıklama | kuralın mekanizmasını doğal cümleyle: motor = aşağı | S4'ün kararını, S5'in twist'ini, döngüyü |

```
TEK CÜMLE TESTİ: dört yüzey yan yana konduğunda bir yabancı, filmi
izlemeden hikâyenin sonunu tek cümleyle söyleyebiliyor mu?
→ HAYIR. Dördü de "uzayda aşağı var" der; hiçbiri adamın korunmasını
  bıraktığını, latisin son bağını ya da motorun 2,2 saniyeliğine
  susup ağırlığı götürdüğünü söylemez. ✅ bütçe tutuyor.
```

---

## 🔒 Master Cinema Lock

```
Photorealistic live-action cinematography, Kodak Vision3 color science,
natural 35mm film grain, no digital sharpening. Vertical 9:16 native
framing. One spherical lens per shot (32mm or 75mm) — no anamorphic,
no horizontal flare; camera position stated in metres. ABSOLUTELY ZERO
CAMERA MOVEMENT IN ALL SIX SHOTS — every camera is hard-mounted to the
ship and accelerates with it; no pan, no tilt, no dolly, no zoom, no
handheld, no shake. Single continuous 8-second takes, 0 cuts.
Real-time motion at normal playback speed throughout — no slow motion,
no speed ramp, ever; every speed and acceleration is stated in metres
per second. The ship is under a steady 0.22 g burn: every loose object
falls straight down the hull line toward the stern on a dead straight
line, gaining 2.16 metres per second of speed each second — never
curving, never drifting, never hovering; nothing ever touches the man,
and the minimum passing distance in the film is 0.8 metres. Exactly one
human in every frame, in the film's only white suit, with a completely
flat back and an optically clear, unreflective visor that never opens,
closes or tints. Hard vacuum: absolute silence outside the suit, no
dust, no smoke, no fire, no sparks, no visible engine plume, no
atmospheric haze; razor-edged, absolutely black shadows with no fill;
the sun disc never enters frame. The hull plating is bare, unpainted
and unmarked, so no text of any kind appears on screen at any moment.
```

---

## 📋 QA SPEC — AYRI DOSYADA [Ders 117]

> ⛔ SPEC bir DOSYADIR, bölüm değil. Bu filmin QA SPEC'i:
> **`THE_IRON_SLOPE_QA_SPEC.md`** (bu klasörde, filmin yanında).
> QA anında operatörün eline iki dosya verilir: rubrik + o SPEC.
> Buraya kopyalanmaz — bir sayıyı iki yerde tutmak, birini yanlış
> tutmaktır [AGENTS kural ①].

---

## ✅ Tutarlılık Kontrol Listesi

```
□ Karakter bloğu 6 görsel promptta birebir aynı mı?
□ "Scene N of 6" 6 promptun 6'sında doğru mu?
□ Banttaki gevşek parça sayısı 3→2→2→1→1→0 akışını izliyor mu
  (S0 sonrası 2+latis · S2 sonrası 1+latis · S4 sonrası yalnız latis)?
□ Hava kilidi mesafesi 14-12-9-7-6-4 m sırasını izliyor mu?
□ Geçiş mesafeleri 1,4 / 0,6(mercek) / 1,2 / 0,8(tepe) / 1,1 / 1,0 m
  promptlarda yazılı mı?
□ "dead straight line" + "never curving, never drifting, never
  hovering" 12 promptun 12'sinde var mı?
□ "gaining 2.16 metres per second of speed each second" ya da sayısal
  eşdeğeri her düşüş tarifinde var mı?
□ "nothing touches him" 12/12 var mı?
□ "his boots stay planted on the rungs" ağırlık cümlesi her promptta
  var mı (S5'in 2,2 saniyelik istisnası sayılı mı)?
□ HUMAN COUNT LOCK cümlesi 6 görsel + 6 video promptunda var mı?
□ "completely flat back" + "optically clear" [D79] her promptta var mı?
□ "No slow motion, no speed ramp" 12 promptun 12'sinde var mı?
□ Hızlar m/s cinsinden yazılı mı (0,5 · 0,7 tırmanış · +2,16/s düşüş)?
□ "absolutely zero camera movement" 6 video promptunun 6'sında var mı?
□ Pruva/kıç yönelim cümlesi her promptta var mı [UZAMSAL §5.1]?
□ Güneş diski, egzoz konisi, gezegen hiçbir kadraja giriyor mu? (hayır)
□ Toz, duman, kıvılcım, çarpma anı hiçbir promptta var mı? (olmamalı)
□ Hiçbir figür alt 1/4'e ya da sağ şeride giriyor mu?
□ Basamak aralığı (0,4 m), panel (2,0×1,2 m), latis (6,0 m), aşınma
  yerleri göründüğü her sahnede aynı mı? [D42 · D58]
□ DEVAM ZİNCİRİ: her kesmenin iki yakası da promptlara yazıldı mı?
□ B (I2V) promptları karakteri/ortamı yeniden tarif ETMİYOR mu?
□ Üretim S0'dan başladı mı? Panel düşüşü temiz çıkmadan devam edilmedi mi?
□ Tohum (S0 0:05,8 jant kararması) ve karşılığı (S5 44,4) yazılı mı?
```

---

## ✅ ÜRETİM ÖNCESİ KONTROL — 12 madde (03_PLAN_ONCESI_KONTROL_LISTESI)

```
ÜRETİM ÖNCESİ KONTROL — THE IRON SLOPE            tarih: 24.08.2026

A1 ✅ "no text" ile ekran içeriği aynı dosyada YOK — kaplama işaretsiz,
      suit yamasız, pencere boş ışık: kadrajda yazı üretebilecek TEK
      BİR NESNE YOK. Sayaç metinsiz üç kanalda: gevşek parça sayısı ·
      hava kilidi mesafesi · turuncu jant [Kart 5 çözümü]
A2 ✅ sahne sayısı: başlık 6 = blok 6 = "Scene N of 6" 6
A3 ✅ süre: 6 sahne × 8 s = 48 s = iddia edilen süre
A4 ✅ yasaklı sahne tipi taraması yapıldı:
      · araç/kapak biniş-inişi [D69] → hava kilidine GİRİŞ GÖSTERİLMEZ;
        film kapının 2 m önünde döngüye devreder
      · loş iç mekâna giriş [D69] → film tamamen dış gövdede
      · aynalı/yansıtıcı yüzey [D20/D69] → kaplama MAT, vizör sıfır
        yansıma, ayna/cam/su 0 kare
      · türetilmiş optik fenomen novum [D73] → taşıyıcı KATI (panel,
        ray, latis); jant ışığı taşıyıcı DEĞİL, sayaç/tohum kanalı
      · yokluk novum [D76] → değil: kural her sahnede GÖRÜNÜR bir
        düşüşle kanıtlanıyor
      · jenerik/başlık kartı [D34/D70/D72] → 0 saniye
B1 ✅ doruk anı S5'in İÇİNDE tarif edildi (son bağ + latis geçişi +
      yanma arası + geri dönüş, tek çekimde ve zaman damgalı);
      iki sahne arasına düşmüyor
B1b ✅ katmanlı dünya YOK — tek ortam, tek ışık; güneş 48 saniyede
      kımıldamaz. Kart 6b tetiklenmiyor
B2 ✅ bedelli seçim S4; kayıp AYNI SAHNEDE görülüyor (şakül gibi asılı
      kalan şerit + korumasız tırmanış) ve S5'te kalıcı (göğüs halkası
      boş, şerit aşağıda)
C  ✅ 6 sayısal kilit yazıldı:
      insan (1 × 6 sahne · beyaz suit TAM 1) ·
      kask (kapalı 6/6 · D79 düz sırt + berrak vizör her promptta) ·
      ölçü (basamak 0,4 m · panel 2,0×1,2 m · latis 6,0 m · şerit
            2,4 m · hava kilidi 14 m · geçişler 1,4/1,2/1,1/1,0/0,8 m) ·
      yerçekimi (0,220 g · 2,16 m/s² · 1s=1,08 m · 3s=9,7 m ·
            5s=27 m · yanma arası 2,2 s) ·
      sıvı (0 kare) · canlı (0 kare)
D  ✅ risk sayımı: 4/12 — EŞİĞİN ALTINDA. Kart 3 · 4 · 5 · 9.
      Kart 6 tetiklenmiyor (toz/duman/alev/çarpma 0 kare — tasarım
      kararı); Kart 1/2/7/6b/10/11 konseptte yok.
      ⭐ Gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı:
      TIRMANAN GÖVDENİN EKLEMLENMESİ (D18 akrabası) + sıfır-g refleksi.
E  ✅ QA SPEC ayrı dosyada: THE_IRON_SLOPE_QA_SPEC.md [D117]
```

---

## 🚪 KAPI KAYDI [DERS 74]

> Kaydı olmayan kapı, koşulmamış kapıdır. Aşağıdaki satırlar üretim
> ilerledikçe DOLDURULUR; boş kalan satır "geçti" anlamına gelmez.

| Tarih | Kapı | Ölçülen | Sonuç |
|---|---|---|---|
| 24.08.2026 | prompt_kontrol.py | 12 prompt (6 image + 6 video A) + 6 B sürümü | ✅ **GO · 0 BLOCK · 0 FIX** (ilk koşu 1 FIX verdi: S4 video 2.712; kısaltıldı) |
| — | **Tek-kare fizibilite [D73]** — S0 görsel promptu tek başına | düşen panel tek karede "düşüyor" okunuyor mu; adamla arasındaki boşluk görünüyor mu | ⬜ **KOŞULMADI** |
| 24.08.2026 | **S0-önce üretim kapısı** — panel düşüşü | panel adama çarpıyor mu · kavis çiziyor mu · **süzülüyor mu** · ağır çekime giriyor mu · adam yüzüyor mu | 🔴 **KOŞULMADI — VE DÜŞECEKTİ.** 25.08'de master ölçüldü: panel gövdeye göre **sabit ~0,15 m/s** süzülüyor, 10 saniyenin sonunda hâlâ kadrajda (kilit: 3. sn 9,7 m). Kapının kendi cümlesi "film üretilmez" diyordu; altı sahne üretildi [D74 tekrarı] |
| — | Tırmanış kapısı [D18 akrabası] — S1 ve S2 | her eldiven/bot kalkıyor-kavrıyor-yük alıyor mu; kayma var mı | ⬜ **KOŞULMADI** — koşulsaydı geçerdi: tırmanış eklemlenmesi ekranda tutan tek şey oldu |
| — | Devrilme kapısı — S3 (latis) | latis pivotla mı iniyor; iki bağda YAKALANIP asılı kalıyor mu; bükülme/parçalanma var mı | ⬜ **KOŞULMADI** |
| — | Karabiner kapısı — S4 (merkezi seçim) | jest okunuyor mu; şerit runner'dan ŞAKÜL gibi düz mü sarkıyor | 🔴 **DÜŞTÜ** — şerit 0:58'de S biçiminde kıvrık; şakül kilidi tutmadı (itki yerçekiminin ikinci kanıt nesnesi) |
| — | Yanma arası kapısı — S5 (filmin en pahalı karesi) | jant sönüyor ve DÖNÜYOR mu; botlar kalkıp OTURUYOR mu; şakül kıvrılıyor mu; adam serbest süzülmeye geçiyor mu | 🔴 **DÜŞTÜ** — 0:58'de jant YANIYOR ve şerit aynı anda kıvrık; twist ekranda yok |
| — | Klon kapısı [D20/D69] | ikinci insan biçimi ya da yansıma var mı | ✅ **GEÇTİ** — altı sahnede tek insan (insan şeridi 111111) |
| — | 120 px kapak testi | beyaz leke / koyu leke / turuncu çizgi ayrışıyor mu | ⬜ **KOŞULMADI** |
| 25.08.2026 | Kurgu kapısı [D70/72] | 6 klip · 48,0 s · ekran metni 0,0 sn | 🔴 **DÜŞTÜ** — 6 klip ✅ · **65,0 s** (6 × 10,005 s klip) 🔴 · ekran metni **4,97 s** başlık kartı 🔴 [D124 · D70'in üçüncü vakası] |
| 25.08.2026 | ⑪ ÖLÇÜM KAPISI [D125] | süre · kesme ızgarası · sessizlik · en-boy | ✅ koşuldu — sayılar QA kaydında: `../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_IRON_SLOPE.md` |
| 25.08.2026 | Negatif blok kapısı | `no planet` · `no patch, no logo` · `zero camera movement` | 🔴 **ÜÇÜ DE DELİNDİ** — S2'de gezegen kadrajın alt üçte birinde · göğüste kırmızı/mavi arma · S2'de kamera kayıyor [D59] |

> ⛔ **25.08.2026 · ÜRETİM SONUCU: FİLM YAYINLANMAZ.** Sebep süre ya da kart
> değil, **novum'un ekrana gelmemesidir** — dosyanın kendi cümlesiyle: "üretim
> S0'dan başlar; panel orada çarpar/kavis çizer/süzülürse film üretilmez."
> Panel süzüldü. Yeniden üretim yapılacaksa düşüş kilidi **DERS 127**'nin
> metniyle yazılır (ivme değil, kadrajı terk etme süresi) ve ızgara aracın
> ölçülen klip süresine göre kurulur [DERS 124]. Tam kayıt ve altı mercekli
> QA: `../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_IRON_SLOPE.md`

### 📏 PROMPT UZUNLUKLARI — dürüst kayıt (24.08.2026)

```
VIDEO (A sürümü, 6 prompt)   2.236 - 2.586 karakter
  → §7 hedef bandının (2.000-2.600) İÇİNDE, 6/6. Veo tavanının
    (~4.300) çok altında. İlk koşuda S4 videosu 2.712 ile bandın
    üstündeydi; kuyruk artıkları ve tasvir tekrarı kısaltıldı,
    sayısal kilitlere DOKUNULMADI.

IMAGE (6 prompt)             5.023 - 5.651 karakter
  → ⚠️ Betiğin bandı (1.700-2.100) hiçbir filmle uyuşmuyor ve betik
    bunu "bulgu değil GÖZLEM" sayıyor; emsaller THE QUIET IMPACT
    (4.577-5.644) ve THE STRAIGHT LINE (5.421-5.669) üretildi/
    reddedilmedi. Bu dosya o emsallerin bandında ve bu kayda geçirilir.
  ⛔ İLK RED GELİRSE KISALTMA SIRASI — bu sırayla, tek tek:
    ① NEGATIVE kuyruğundaki kalan çiftler ("no smoke" yanında
      "no fire" vb. birleşiği)                          → ~50 karakter
    ② karakter bloğunun yüz-detay cümlesi (kaş, yara izi, dudak)
                                                        → ~170 karakter
    ③ ENVIRONMENT'taki yıldız/plating tekrarı           → ~110 karakter
    ⛔ SAYISAL KİLİTLER (ivme, mesafeler, ölçüler, yörünge cümlesi,
      ağırlık cümlesi) HİÇBİR KOŞULDA KISALTILMAZ — bu filmde sayılar
      fiziğin kendisidir.
```

> **Üretim sırası:** ① **S0** (düşen panel — novumun ilk kanıtı) →
> ② S5 (latis geçişi + yanma arası — en pahalı kare) → ③ S3 (devrilme)
> → ④ S4 (karabiner) → ⑤ S1 → ⑥ S2.
> S0 temiz çıkmadan hiçbir sahne üretilmez.

---

**THE IRON SLOPE — Demir Yokuş**
_"Motor yandığı sürece, uzayın bir aşağısı var."_
