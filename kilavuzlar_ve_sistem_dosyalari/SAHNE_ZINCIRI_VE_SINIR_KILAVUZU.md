# 🔗 SAHNE ZİNCİRİ VE SINIR KILAVUZU — İki Sahnenin Arasında Ne Var

> **Ne zaman okunur:** sahne haritası yazılırken — plan dosyası
> doldurulmadan önce, `ONERME_VE_NOVUM` ve `06_HIKAYE_HATTI_TESHISI`
> geçildikten sonra. Bu dosya sahnenin İÇİNİ değil, iki sahnenin
> ARASINI yazar.
>
> **Neden var:** `06_HIKAYE_HATTI_TESHISI` §0 — *"depo hikâye yazmıyor,
> novum gösterisi yazıyor."* Depo her sahnenin promptunu yazıyor ama
> sahneyi sahneye bağlayan mekanizma hiçbir dosyada yoktu. 25 sahnelik
> bir filmde **24 sınır** vardır; depo bunların **üçünü** kapıyla
> tutuyordu — ve üçüncüsü tam olarak bir sınır kapısı bile değil:
> S0 çıkış testi (`HOOK` §2.5) ve S1 tırmandırma (`HOOK` §3) sınırı
> ölçer; final vuruş kanıtı [D141] klibin İÇİNİ ölçer (belirli bir
> saniyede ekranda bulunan/bulunmayan nesne). Kalan sınırlar GÖRSEL kapılarla
> ölçülüyordu — ölçek, palet, ses dokusu, açı. Hiçbiri *"bu sahne
> bittiğinde hangi soru açık kaldı"* diye sormuyordu.
>
> **Kaynak turu:** TUR 11 · süzme kaydı
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 11 ·
> ham metin `URETIM_ONCESI_ANALIZ/TUR11_HAM_RAPORLAR/`.

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuza NE İNMEDİ

```
① BU DOSYADAKİ HİÇBİR SAYI DIŞ RAPORDAN GELMEDİ.
   TUR 11'in birinci raporu sekiz film için zaman damgası verdi
   (00:48:15 · 01:25:10 · 00:04:30 · 00:32:40 · 00:15:20 · 00:08:15 ·
   00:02:10 · 00:26:40). Sekizinin hiçbiri doğrulanmadı ve en az beşi
   filmde OLMAYAN bir sahneyi tarif ediyor. Damgaların tamamı düştü.

② İKİ SATIR "İZLEYİCİ ÖLÇÜMÜ" ETİKETİ TAŞIYORDU VE ÖLÇÜM DEĞİLDİ.
   Rapor Buried satırına "Klostrofobi SCL tavanı", Gravity satırına
   "Deri iletkenliği" yazdı; kendi kaynak listesinde o iki filmi ölçen
   tek bir çalışma yok (listedeki kalemler TV Tropes, Collider,
   Phillymag). Tipoloji indi, etiketler inmedi.

③ RAPORUN GÖZ İZLEME İDDİASI TERSİNE ÇEVRİLDİ — ve tersi daha yararlı.
   Rapor "sabit planda fiksasyon uzar, dikkat eşzamanlılığı artar"
   dedi. Smith & Mital (2013, Journal of Vision 13(8)) bunun TERSİNİ
   ölçtü: dinamik sahneler statik sahnelere kıyasla daha yüksek dikkat
   eşzamanlılığı ve daha UZUN fiksasyon üretir (serbest izlemede 339 ms
   vs 290 ms); bakış hareket noktalarında kümelenir.
   → Çıkan kural raporun istediğinin tersi: kesmesiz 8-10 saniyelik
     sabit plan bakışı KENDİLİĞİNDEN toplamaz. §1'in dayanağı budur.

④ İKİ ŞABLON REDDEDİLDİ.
   Raporun "6 sahnelik" ve "25 sahnelik" blok şablonları "izleyici
   ölçümleri baz alınarak" diye sunuldu; ölçüm yok, raporun tasarımı.
   Ayrıca 25'liğin 3. bloğu (S11-15 · "aksiyon durur, karakter baygın")
   deponun EN SERT ÖLÇÜLMÜŞ arızasının reçetesidir: THE PAYLOAD'da
   merkezî seçimden sonraki 13 sahnede kahramanın bedelli seçimi 0'dır
   ve QA Karakter 2/10 verdi [D158]. İnmedi.

⑤ İKİNCİ KEZ İNMEYENLER — hepsi zaten yazılı, her biri kendi adresiyle:
   sahne sonunda kelimelerle sorulabilir soru → HOOK §2.5 ·
   sonraki sahnenin BÜYÜTME görevi → HOOK §3 ·
   Loewenstein kısmi bilgi → HOOK §2.3 ·
   izleyicinin karakterden öne geçmesi (dramatik ironi) → HOOK §3.1 ·
   hipotez-doğrulama ödülü → ONERME_VE_NOVUM §5 ·
   durağan blokta mikro-değişim → TEMA_MUHENDISLIGI §8 · MESHUR_SAHNE §1 ·
   foveal merkez → ACILIS_KAPANIS_CIFTI §2.1 ·
   sayacın tek karede kanıtı → D78 ·
   "hiçbir şey olmuyor" şikâyetinin sebebi → 04 §TUR 4 · T4.1/13.

⑥ İNEN TEK ŞEY: SORU/CEVAP TAKSONOMİSİ VE SINIR DİSİPLİNİ.
   Beş soru tipi, dört cevap tipi, ardışık tekrar yasağı ve sınır
   satırı. Etiketi ÖNERİ'dir — raporun kendi tasarımıdır, ölçüm değil.
   Kısıtların hiçbirini ihlal etmez ve mevcut bir kapının
   (`KURGU_RITMI` §2 örüntü kırıcı) birebir anlatı ikizidir.
   ⛔ Hiçbiri üretimde sınanmadı. İlk uygulamada ölçülür.
```

---

# 1. 📍 BİRİM SINIRDIR — ve değişim sınırda olur, klibin İÇİNDE değil

Depo sahneyi birim sayar. Zincirin birimi sahne değil, **iki sahnenin
arasındaki sınırdır.**

```
6 sahnelik film    →  5 sınır
25 sahnelik film   → 24 sınır      ← depo bunların 3'ünü kapıyla tutuyordu
120 sahnelik film  → 119 sınır
```

**Ve sınırın nerede olacağı bir tercih değil, motorun ayarıdır.**

```
⭐ DEĞİŞEN NİTELİK, ÖLÇÜLMÜŞ EN ZAYIF KATEGORİDİR.
   Bir niteliğin klip İÇİNDE durum değiştirmesi (dynamic attribute
   binding), ölçülen yedi eksenin en kötüsüdür: model başlangıç
   durumunu ya da bitiş durumunu donduruyor, ikisini birden
   donduruyor, ya da arada morfoloji bozuyor.
   ⭐ SAYI VE KAYNAK TEK YERDE: `KILAVUZ_REHBERI.md` §7
     ("DEĞİŞEN NİTELİK" bloğu · 04.09.2026).           [ÖLÇÜLMÜŞ]

→ SONUÇ: "lamba yanar", "buğu birikip çözülür", "kapak açılır",
  "renk döner" gibi DURUM DEĞİŞİMİ tek klibe yazılmaz.
  Durum A bir klipte, durum B bir sonraki klipte durur.
  Değişim KESMEDE olur.

→ VE BU, SINIR DİSİPLİNİNİ ZORUNLU KILAR: hikâyenin ilerlemesi
  zaten klip sınırına düşmek zorundadır. Ölçülmüş kısıt şudur:
  değişim klip İÇİNDE üretilemiyor. Değişimin NEREYE yazılacağı
  ise ayrı bir sorudur ve §7①'e bağlıdır.

✅ [ORTAM] VE [STİL] DEĞİŞİMİ DE SERBEST — 04.09.2026 sahip kararı.
   ACI_YAYI §7③'ün kapsamı daraltıldı: yasak MODELİN uydurduğu kaymayı
   kapsıyor, yazarın PLANLADIĞINI değil. Üç şart birden aranır:
   (a) değişim sahne haritasında yazılı ve TEK değişken · (b) sınırda
   olur, klip içinde değil · (c) iki promptta o blok birebir aynı
   kelimelerle, yalnız o değişkenle farklı yazılır. Üçü yoksa kural
   eski hâliyle geçerlidir. Ayrıntı: §7① · ACI_YAYI §7③.
```

Klibin İÇİ ise boş bırakılamaz:

```
⛔ SABİT PLAN BAKIŞI KENDİLİĞİNDEN TOPLAMAZ [§0③].
   Kadrajda tek bir sürekli HAREKET (durum değişimi değil — hareket)
   plan boyunca sürmelidir: bir el yavaşça kapanır, toz tek yönde
   akar, gövde ağırlık aktarır. Hareket biterse bakış arka plana
   kayar ve kalan saniyeler fotoğraf donukluğuna düşer.
   Hareket ↔ durum değişimi ayrımı: MESHUR_SAHNE_KALIPLARI §1
   (içsel hareket) · KAMERA_ACISI (hareket süngeri).
   ⚠️ KAMERA_ACISI'ndaki "subtle mist" ve "particles floating"
     örnekleri HOOK §2.4 perde yasağına ve çekirdeğin "never
     hovering" satırına takılır; süngeri yukarıdaki örneklerle doldur.
```

---

# 2. ❓ AÇILAN SORU — sahne sonunda kalan beş tip

Kısıt gereği (tek insan · replik yok · okunur metin yok · kesme yok)
soru karakterin geçmişine değil, **fiziksel mevcudiyete ve çevresel
nedenselliğe** bakar. Beş tip, deponun kendi sözlüğüne oturur:

| # | Soru tipi | Neyi asılı bırakır | Depodaki karşılığı |
|:--:|---|---|---|
| ① | **EYLEMİN SONUCU** | figürün uyguladığı gücün başarıya ulaşıp ulaşmadığı | `06` İSTEK · D158 çözüm bloğu B2b (başarısız deneme sayısı) |
| ② | **NESNENİN AKIBETİ** | kritik bir aracın bütünlüğü ya da konumu | `ASTRONOT_DONANIM` §8 eşya · D58 tekrar eden varlık |
| ③ | **MEKÂNIN SIRRI** | çevresel bir unsurun figüre ne yapacağı | ortam kartları `KILAVUZ_REHBERI` §3 |
| ④ | **BEDENİN SINIRI** | fizyolojik dayanıklılığın kırılma noktası | `KARAKTER_VE_DUYGU` §4 · D169 zorlanma kanalı |
| ⑤ | **ZAMANIN DOLMASI** | dışsal bir sayacın tükenişi | `06` BEDEL · D78 sayacın tek karede kanıtı |

```
⛔ SORU CÜMLESİ PLANA YAZILIR, EKRANA YAZILMAZ.
   S0 için bu kural zaten var (HOOK §2.5 çıkış testi). Burada S2'den
   sona kadar genelleşiyor: her sahne satırının karşısında izleyicinin
   KELİMELERLE sorabildiği ama cevaplayamadığı bir cümle durur.
   Cümle yazılamıyorsa o sınır boştur.

⛔ ⑤ ZAMANIN DOLMASI GÖSTERGEYE YAZILAMAZ.
   Sayaç kadrajda okunur bir değerle gösterilemez [D138 · 03 §A1:
   "no text" ile gösterge İÇERİĞİ aynı planda varsa PLAN BOZUK].
   Sayaç metin değil DURUM olarak taşınır: bir ışığın rengi, suyun
   seviyesi, gölgenin boyu, kalan parçanın sayısı, bir kolun açısı.
   ⚠️ "İbrenin yeri" ancak kadranda çentik, skala ya da rakam
     OLMADAN kullanılabilir — çekirdek bunları adıyla yasaklıyor
     ("no scale marks, no graduation ticks") ve D138 vakası tam bu
     sınıftandır. Metinsiz alarm görselliği: `ASTRONOT_DONANIM` §5.
```

---

# 3. ↩️ CEVAP — sonraki sahnenin verdiği dört tip

| # | Cevap tipi | Ne yapar | Ne zaman |
|:--:|---|---|---|
| ⓐ | **KISMİ CEVAP** | cevap verir ama yeni ve daha dar bir problem doğurur | varsayılan · zincirin taşıyıcısı |
| ⓑ | **CEVAP YERİNE YENİ SORU** | sonucu kadraj dışında bırakır, daha acil bir tehdit belirir | tırmanışta |
| ⓒ | **CEVABIN ERTELENMESİ** | bilgi askıya alınır, izleyici aradaki boşluğu kurar | ⚠️ şartlı — aşağıya bak |
| ⓓ | **CEVABIN YANLIŞ ÇIKMASI** | kurulan fiziksel hipotez geçersiz kılınır | dönüş noktalarında |
| — | **DÜZ CEVAP** | soru tam ve rahatlatıcı biçimde kapanır | nefes durağı · bütçesi §4'te |

```
⚠️ ⓒ ERTELEME BU HATTA SINIRLIDIR VE SEBEBİ ÖLÇÜLMÜŞTÜR.
   Depoda GÖSTERİLMEYEN ŞEY FİLMDE YOKTUR: 03 §B1 en yüksek gerilim
   anının iki sahnenin ARASINA düşmesini arıza sayar; D141 "sahne var,
   vuruş yok" vakasını ölçtü; kurgu kapısı ⑦ doruğun kurguda bulunmasını
   şart koşuyor (Unbroken City S9 · D72).
   → Erteleme yalnız ARA halkada ve yalnız BİR sınırda kullanılır;
     ertelenen cevap en geç iki sınır sonra ÖDENİR ve ödeme kadrajda
     görünür. Doruğun ve bedelin cevabı ASLA ertelenmez.
```

---

# 4. 🔁 ZİNCİR KURALI — ardışık iki sınırda aynı cevap tipi olmaz

Bu, `KURGU_RITMI` §2'nin anlatı ikizidir. Orada kural şudur: *ardışık
iki sahne aynı ölçek + aynı palet + aynı ses dokusunda olamaz.* Burada:

```
⛔ SAHNE HARİTASI KAPISI — ANLATI SÜTUNU
   Ardışık İKİ sınır aynı CEVAP TİPİNİ kullanamaz.
   Eşik İKİ'dedir — `KURGU_RITMI` §2'nin görsel kapısıyla aynı yerde.

   Örüntü kırıcı iki eksende birden çalışır ve ikisi de şarttır:
     GÖRSEL eksen  → ölçek · palet · ses dokusu   [KURGU_RITMI §2]
     ANLATI ekseni → cevap tipi                    [bu dosya]
   İkisi ayrı eksendir ve görsel kırıcı anlatı örüntüsünü kapatmaz.
   Deponun 18 dikey filminde anlatı ekseni tek tiptir [05 §2.3 · §2.4];
   o filmlerde GÖRSEL kırıcının koşulup koşulmadığı ölçülmedi.
```

**DÜZ CEVAP BÜTÇESİ** — bant deponun kendi kararıdır, raporun bulgusu
değildir; rapor sayı vermedi:

```
□ Düz cevap SINIRLARIN en çok ~%12-15'inde kullanılır ve ikisi yan
  yana gelmez. Bütçe yüzdeyle yazılır, sayı format kartından türetilir
  [HOOK §1.1 ile aynı kural]: 6 sahne → 5 sınır → 1 · 12-18 sahne →
  11-17 sınır → 2 · 25 sahne → 24 sınır → 3 · 60 sahne → 7 ·
  120 sahne → 15.
□ Düz cevap kurulum bloğuna YIĞILMAZ. Kalibrasyon ayrı sahnelere
  harcanmaz, soru açan sahnenin İÇİNDE yapılır: karakter taşı
  kaldırırken taşın altından bir sonraki soruyu doğuran şey görünür.
  ⭐ Gerekçe deponun kendi bandıdır: katalizör %10-15 [HOOK §1.1];
    25 sahnelik bir filmde 5 sahnelik saf kurulum bloğu %20'dir —
    bandın dışında (tabanın 2, tavanın 1,3 katı).
  ⚠️ Bu üç satır ⚙️ SINANMAMIŞ — ilk uygulamada ölçülür.
```

---

# 5. ✍️ SINIR SATIRI — plana yazılan tek satırlık çift

Depo her sahnenin promptunu yazıyor; iki sahnenin ARASINDAKİ bağı
hiçbir yerde metin olarak yazmıyordu. En yakın şey `ACILIS_KAPANIS_CIFTI`
§3'ün yalnız İLK↔SON kare çifti ve `SENARYO_VE_VIRAL` §6'nın geometrik
eşleşmesiydi.

```
SAHNE HARİTASINA İKİ SÜTUN + BİR SATIR

| S | … | açık kalan soru (tip) | sonrakinin cevabı (tip) |
| S7 | … | ② nesnenin akıbeti     | ⓐ kısmi cevap           |

SINIR SATIRI (İngilizce, plana yazılır, prompta değil):
  End:   <S7'nin son saniyesinde kadrajda ne duruyor>
  Start: <S8'in ilk karesinde kadrajda ne duruyor>
```

```
⭐ SINIR SATIRI I2V ZİNCİRİNE DOĞRUDAN HİZMET EDER.
   Start satırı, o sahnenin başlangıç karesinin ne olması gerektiğini
   söyler — ve başlangıç karesi görünümün en güçlü çapasıdır
   [VEO §6B]. Ama uyarı: I2V'de METİNLE verilen eylem/dinamik
   talimatına uyum zayıftır; ölçümde kazancın tamamı dinamik ve
   hareket eksenlerinde çıktı — sayılar §10'da.          [ÖLÇÜLMÜŞ]
   → Çapa GÖRÜNÜMÜ tutar, EYLEMİ tutmaz. Sınırdaki değişim
     başlangıç karesinin KENDİSİNE yazılır, metne bırakılmaz.

⛔ SINIR SATIRI PROMPT GÖVDESİNE KOPYALANMAZ.
   Prompt tek sahneyi anlatır; "bir önceki sahnede şu olmuştu" cümlesi
   modele geçmiş vermez, yalnız o cümlenin ismini çizdirir [D59].
```

---

# 6. ✂️ HANGİ CEVAP HİÇ YAZILMAZ — sahne haritasının anlatı kapısı

Bu bölüm TUR 11'in birinci ve ikinci raporunun ÇAPRAZ okumasından
çıktı; iki raporun hiçbirinde yazmıyor, yan yana konunca çıkıyor.

```
⛔ ÖNCE SINIRI ÇİZ: BU BÖLÜM PLAN MASASINDADIR, KURGU MASASINDA DEĞİL.
   Deponun kuralı yerinde duruyor ve gevşetilmiyor: plana yazılı klip
   kurguda düşemez; düşen klip = kapı BATTI
   [KURGU_VE_TESLIM §1 ① ⑧ ⑩ · D70 · D72 · D100].
   Aşağıdaki üçlü, bir klibi ATMANIN değil, o cevabı plana HİÇ
   YAZMAMANIN ölçütüdür.
```

```
AYIRT EDİCİ SORU — sahne haritası yazılırken, her sınır için:
  "Bu sınırın taşıyacağı cevap zincirin HANGİ halkasına ait?"

ARA HALKA    → cevabı PLANA YAZMA. O sınır ⓑ olur (cevap yerine
               yeni soru) ve itki güçlenir. Yazılmayan cevap
               kurguda aranmaz; sonradan kesilen cevap aranır.
               Vaka: Alien'ın koza sahnesi 1979 vizyon kurgusundan
               tempo gerekçesiyle çıkarıldı (2003 yönetmen kurgusunda
               kısaltılarak geri kondu) — ama bu bir KURGU vakasıdır
               ve bizim çıkardığımız ders yazım tarafındadır: o sahne
               hiç yazılmasaydı film aynı yere varırdı.     [İKİNCİL]

AÇIKLAMA     → PLANA HİÇ GİRMEZ. Sonucun İZAHI bir sahne hak etmez;
               sonucun KENDİSİ hak eder.
               Vaka: The Shining'in hastane epiloğu (Ullman'ın Wendy ve
               Danny'yi ziyareti, sarı top) ABD gösteriminden hemen
               sonra tüm kopyalardan çıkarıldı — yani stüdyo kopyaları
               kesildi, çünkü plan onu yazmıştı.           [İKİNCİL]

TERMİNAL     → HER ZAMAN YAZILIR VE HER ZAMAN EKRANA GELİR.
BEDEL          Burada deponun kendi ÖLÇÜMÜ var, dış vakaya gerek yok:
               Unbroken City'de S9 doruk kurguya girmedi ve üç bağımsız
               mercek bunu üretimden SONRA buldu [D72 — D62 sınıfının
               beşinci tekrarı · kurgu kapısı ⑦]; Last Shift'te 27
               klibin 17'si ekranda kaldı ve süre tuttuğu için kayıp
               görünmedi [D100].                             [ÖLÇÜLMÜŞ]
```

```
✅ KURGU MASASINA DÜŞEN TEK ŞEY: ETİKET.
   Düşen her klibin karşısına hangi halkaya ait olduğu yazılır
   [KURGU_VE_TESLIM §2 gerekçe tablosu]. Beş kesme gerekçesinden bu
   hatta meşru olan tek tanesi TEKNİK KUSURDUR — modeli çöken klip
   zaten kullanılamaz ve o klip YENİDEN ÜRETİLİR. "Tekrar" ve "bilgi
   fazlalığı" gerekçeleri kurgu masasında geçersizdir; onların yeri
   yukarıdaki plan kapısıdır ve orada zaten ödenmiştir.
```

# 7. ⚔️ DEPO İÇİ ÇAKIŞMALAR — üçü açık, biri sahibin kararı

```
① ✅ KAPANDI — SINIRDAKİ DEĞİŞİM ↔ ACI_YAYI §7③ (04.09.2026)
   ACI_YAYI §7③ "sahneden sahneye yalnız [KAMERA] değişir" diyordu ve
   03 §B5 MUHATAP seçenek 4 (ortamın kalıcı değişen parçası) bununla
   çelişiyordu. Sahip kararı: §7③'ün KAPSAMI DARALDI — yasak MODELİN
   uydurduğu kaymayı kapsar [D47 · D48], yazarın PLANLADIĞINI değil.
   Kural artık ACI_YAYI §7③'te üç şartıyla yazılı; bu dosya onu
   tekrarlamaz, adres verir. Çelişki kapandı.
   ⚠️ Ayakta kalan tek uyarı ÖLÇEK: "sınırda tek değişken" ifadesi
     `ACILIS_KAPANIS_CIFTI` §2'nin FİLM ölçeğindeki tek değişken
     kuralından türetilmiştir ve o ölçekte ⚙️ SINANMAMIŞTIR.

② SINIRDA GÖSTERGE OKUNMASI ↔ METİN YASAĞI
   Raporun bağ örneklerinden biri bir göstergenin kırmızıya dönmesiyle
   kuruluyordu. Gösterge sınır taşıyıcısı olabilir, ama yalnız
   METİNSİZ DURUM olarak: renk, ibre yeri, yanıp sönme.
   Okunur değer yazılırsa plan bozuktur [03 §A1 · D138].
   ⚠️ Ve ışığın YANMASI bir durum DEĞİŞİMİDİR — §1 gereği tek klibe
     yazılmaz; sönük durum bir klipte, yanık durum sonrakinde durur.

③ RAPORUN BLOK YÜZDELERİ ↔ DEPONUN BANDI
   Rapor kurulumu %20'ye, dibi %40'a koydu; deponun bandı çok daha
   dar (katalizör: HOOK §1.1). Sıkı olan taraf durur — ama iki dürüst
   kayıt gerekli: (a) deponun o bandı da sınanmamıştır
   (HOOK §0①: hiçbir film yayınlanmadı); (b) "her şeyin kaybı"
   vuruşu için depoda ÜÇ farklı sayı yaşıyor
   (`KILAVUZ_REHBERI` §2.5 · `SENARYO_VE_VIRAL` §2.2 ·
   YERÇEKİMİ 00_PLAN §Oran doğrulaması) ve tek eve indirilmesi
   sahibin kararıdır. İki sınanmamış şablon çarpıştı; "ölçtük" denemez.
```

---

# 8. ✅ KONTROL LİSTESİ — 9 plan maddesi + 1 kurgu maddesi

```
SAHNE HARİTASI YAZILIRKEN
 □ 1. Her sahne satırının karşısında AÇIK KALAN SORU cümlesi var mı
      (kelimelerle sorulabilen, cevaplanamayan)
 □ 2. Her sorunun TİPİ işaretli mi (① eylem · ② nesne · ③ mekân ·
      ④ beden · ⑤ zaman)
 □ 3. Her sınırın CEVAP TİPİ işaretli mi (ⓐ ⓑ ⓒ ⓓ ya da düz)
 □ 4. ⛔ Ardışık iki sınırda aynı cevap tipi YOK
 □ 5. Düz cevap bütçesi aşılmadı (sınırların ~%12-15'i · §4 tablosu)
 □ 6. ⓒ erteleme en çok bir sınırda ve ödemesi ≤2 sınır sonra kadrajda
 □ 7. SINIR SATIRI (End: / Start:) her sınır için yazıldı
 □ 8. ⛔ Hiçbir klibin İÇİNDE durum değişimi istenmiyor — değişimler
      sınıra düştü (§1 · dynamic attribute binding); sınıra düşen
      değişim [ORTAM]/[STİL] bloğuna dokunmuyor (§7①)
 □ 9. ⑤ ZAMAN sorusu kullanıldıysa sayaç METİNSİZ durum olarak taşınıyor

KURGU MASASINDA
 □ Düşen her klibin karşısında HALKA etiketi var (ara · açıklama ·
   terminal bedel) ve terminal bedel düşmedi   [KURGU_VE_TESLIM §1 ⑦]
```

---

# 9. ⬜ BU KILAVUZUN KENDİ SINIRI

```
① TAKSONOMİ ÖLÇÜLMEDİ. Beş soru ve dört cevap tipi raporun kendi
   tasarımıdır (etiket: ÖNERİ). İç tutarlılığı sağlam ve kısıtlarla
   uyumlu; ama hiçbir film üzerinde sınanmadı.

② DÜZ CEVAP BANDI (~%12-15) DEPONUN KENDİ KARARIDIR. Rapor sayı
   vermedi; oran deponun kendi bütçe yazım kuralından türetildi
   [HOOK §1.1]. İlk iki filmde ölçülür ve gerekirse değişir.

③ SINIR SAYISI × MALİYET HESABI YAPILMADI. Sınır disiplini üretim
   maliyetini artırmaz (aynı klip sayısı) ama yeniden üretim riskini
   artırabilir: sınırdaki tek değişken tutmazsa iki klip birden
   yeniden üretilir. Bu risk ölçülmedi.

④ 120 KLİPLİK BANTTA ZİNCİR HİÇ DÜŞÜNÜLMEDİ. Rapor 6 ve 25 için
   şablon verdi (ikisi de reddedildi), 119 sınırlık bir zincirin
   anlatı karşılığını hiç yazmadı. 10-20 dk bandında bu dosya
   yalnız kural verir, yapı vermez.

⑤ ACI_YAYI §7③ ÇAKIŞMASI KAPANDI (04.09.2026 · §7①), ama kapanma
   bir ÖLÇÜM değil bir KARARDIR: plana yazılan tek değişkenin modelde
   gerçekten tuttuğu hiçbir filmde sınanmadı.
```

---

# 10. 📚 KAYNAKLAR

```
DEPO İÇİ (kural buradan gelir)
  06_HIKAYE_HATTI_TESHISI §0 · 05_DIKEY_HAT_TESHISI §2
  HOOK_VE_ILK_SAHNE §2.3 · §2.5 · §3 · §3.1 · §1.1
  FINAL_VE_PAYLASIM §1 (bilgi boşluğu bandı · cevap dağılımı)
  KURGU_RITMI_VE_IHRAC §2 (örüntü kırıcı — bu dosyanın görsel ikizi)
  KURGU_VE_TESLIM §1 ④ ⑦ · §2 · ACILIS_KAPANIS_CIFTI §2 · §3
  ACI_YAYI_VE_SEKANS §7 · MESHUR_SAHNE_KALIPLARI §1
  03_PLAN_ONCESI §A1 · §B1 · §B2 · §B5
  DERSLER: D47 · D48 · D58 · D59 · D62 · D72 · D78 · D100 · D138 · D141 · D158 · D169

DIŞ (üç ölçüm indi, üçü de birincil kaynakla doğrulandı)
  Smith & Mital 2013 · Journal of Vision 13(8) — serbest izlemede
    fiksasyon süresi ve dikkat eşzamanlılığı; sayılar §0③'te. [ÖLÇÜLMÜŞ]
  T2V-CompBench · CVPR 2025 — dynamic attribute binding en zayıf
    kategori; sayı `KILAVUZ_REHBERI.md` §7'de.            [ÖLÇÜLMÜŞ]
  Focal Guidance · arXiv 2601.07287 — HunyuanVideo-I2V VBench
    0,5185 → 0,5571 (+%7,44); kazanç Dynamic Attributes +%33,7 ve
    Human Motion +%33,9 eksenlerinde.                     [ÖLÇÜLMÜŞ]

KURAMSAL ZEMİN (sayı taşımaz)
  Carroll — erotetik anlatı · Bordwell — hipotez kurma
  Sternberg — gerilim (ileri) / merak (geri) / sürpriz (geçersizleşme)
  Brewer & Lichtenstein — Başlatıcı Olay → geciktirme → Sonuç Olayı
```
