# 🎁 PAKETLEME VE VAAT KILAVUZU — Kapak Senaryoda Yazılır

> **Neden var (22.08.2026):** Bu hatta post-prodüksiyonda "vurucu kare"
> aranamaz. Yüz yok, mimik yok, kamera sabit, klipler 8-10 saniye. Kapak için
> gereken kompozisyon **senaryoda istenmemişse model onu tesadüfen üretmez.**
> Depoda kapak (`KAPAK_FOTOGRAFI_MIMARISI`) ve başlık/açıklama
> (`VIRAL_BASLIK_VE_ACIKLAMA_PROMPT`) kılavuzları var; ikisi de **teslim**
> tarafında duruyor. **D114** bu boşluğun faturasıdır: fragman spoiler kapısını
> geçti, açıklama metni aynı sırrı tek cümlede verdi — çünkü paketleme dört
> yüzeyli tek bir bütçe olarak hiçbir yerde planlanmıyordu.
>
> **Ne zaman okunur:** sahne haritası yazılırken — kapak anı bir SAHNE'dir ve
> yuvası burada ayrılır. Üretimden sonra eklenemez.
> Kaynak: `araştırmalar/5.md` (22.08.2026 senaryo odaklı paketleme araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① BU DOSYA SAYI TUTMAZ. CTR skalası KAPAK_FOTOGRAFI_MIMARISI §7'de,
   yayın sonrası eşikler YAYIN_VE_PERFORMANS §2'de durur ve burada
   TEKRARLANMAZ. Buradaki tek iş: senaryo aşamasında verilecek kararlar.

② KAPAK VE BAŞLIK YAPIMI BU DOSYADA DEĞİL. Renk, güvenli alan, 120 px
   testi, A/B → KAPAK_FOTOGRAFI_MIMARISI. Başlık/açıklama metninin
   yazımı → VIRAL_BASLIK_VE_ACIKLAMA_PROMPT. Bu dosya onlara HANGİ
   KAREYİ ve HANGİ VAADİ vereceğini belirler.

③ VAAT, SENARYONUN GÖRSEL OLARAK KARŞILAYABİLECEĞİNDEN BÜYÜK OLAMAZ.
   Yüksek tıklama + erken terk örüntüsü, düşük tıklamadan daha ağır
   cezalandırılır: sistem bunu memnuniyetsizlik olarak okur ve kanalın
   sonraki filmlerini de eler. Tek yönlü kapı — geri dönüşü yavaştır.

④ SPOILER BÜTÇESİ DÖRT YÜZEYLİDİR [D114]: başlık · kapak · fragman ·
   açıklama. Kapı bugüne kadar üç yüzeyde koşuyordu; dördüncüsü
   (açıklama) bu dosyada bağlanır.
```

---

# 1. 🖼️ KAPAK ANI — plana yazılan bir SAHNE

**Mekanizma:** Kapak karesi filmden çıkar; film de prompttan çıkar. Yani
kapağın ışığı, kompozisyonu ve kontrastı **prompt yazılırken** istenmiş
olmak zorundadır. Kapak anı ayrıca filmin ilk 10 saniyelik bloğundan
seçilir — böylece izleyicinin tıkladıktan sonra gördüğü ilk hareketli
görüntü kapakla aynı olur ve beklenti saniyesinde doğrulanır.

```
PLANA YAZILAN SATIR (BÖLÜM 0)

KAPAK ANI: S<n> · <saniye> · <kompozisyon> · <ışık> · <odak>

örnek ✅  S0 · 0:04 · üçte bir sağda kask silüeti, sol üçte ikide
          parçalanan gövde · tek kaynak sert yan ışık · odak: vizörde
          büyüyen yansıma

SAYISAL KİLİT
  □ KAYNAK BLOK     kapak anı 0:00-0:10 bandından seçilir
  □ KOMPOZİSYON     üçte bir kuralı veya altın oran — kadraj ortası DEĞİL
  □ KONTRAST        silüet arka plandan kopmuş; ton eşitliği ret sebebi
  □ PROMPT İZİ      bu sahnenin promptunda ışık ve kompozisyon SAYIYLA
                    yazılı mı (PROMPT_KONTROL bunu arar)
```

> ⚠️ Kapak anı sahnesi **kurgu kapısının KESİLEMEZ listesine** girer. Kapağı
> taşıyan sahne kurguda düşerse elde tıklamayı karşılamayan bir kapak kalır —
> D62/D100 örüntüsünün paketleme tarafı.

---

# 2. 🎯 YÜZSÜZ KAPAKTA ÜÇ ODAK

**Mekanizma:** İnsan beyni kapakta önce yüz ve bakış arar. Bu seride yüz yok.
Ama beyin, gözü olmayan bir figürün bile **nereye yöneldiğini** duruştan
okur ve dikkatini oraya kaydırır. Yüzün yerini üç çapa alır.

```
① VİZÖR YANSIMASI — bu formatın en güçlü silahı
   Yüzün olması gereken yer, hikâyenin kaynağına dönüştürülür: izleyicinin
   doğrudan göremediği tehdit vizörde yansır. Tek dar alanda hem karakter
   hem tehdit görünür.
   ⚠️ Yansıma vizörü AÇMAZ, tonlamaz [D37 · D57].

② YÜKSEK KONTRASTLI SİLÜET — form mesajın kendisi olur
   Aydınlık bir olayın önünde keskin hatlı karanlık figür. Silüetin
   kenarları, eksik olan gözlerin yerine görsel hiyerarşiyi kurar.

③ FRAKTAL ÖLÇEK — durağanlığı kıran ihtişam
   Sabit figürün arkasında karmaşık, kendini tekrarlayan devasa bir yapı
   (gemi mimarisi, biyom, yıkım). Figür ile arka plan arasındaki ölçek
   farkı keşif arzusu yaratır ve lockoff'un durağanlığını kırar.
   Ölçek oranı: KARAKTER_VE_DUYGU §5.1 ile aynı yuva kullanılabilir.
```

```
RET ŞARTI
  □ Karakter kadrajın ortasında BOŞLUĞA bakıyor — niyet belirsiz
  □ Ön plan ile arka plan aynı ton bandında — küçük ekranda ayrışmıyor
  □ Kapak, başlığın söylediğini görsel olarak TEKRAR ediyor (merak yok)
```

---

# 3. ⏱️ VAAT-TEYİT PENCERESİ — ilk 10 saniye

**Mekanizma:** İzleyici tıklarken zihnine bir beklenti seti yükler ve ilk
saniyelerde tek bir soru sorar: "doğru yere mi geldim?" Cevap görsel olarak
gecikirse çıkar. Bu seride cevabı sözle vermek imkânsızdır — yalnız kadraj
verebilir.

```
SAYISAL KİLİT
  □ TEYİT SÜRESİ    kapağın vadettiği unsur ekranda ≤ 10 saniye içinde
  □ AÇILIŞ YASAKLARI  yavaş manzara rampası · siyaha açılan uzun kararma
                    · logo/jenerik · konudan bağımsız genel çekim
                    (ikisi de zaten metin/kart yasağına takılır [D70])
  □ TON EŞLEŞMESİ   kapaktaki renk sıcaklığı, ışık yönü ve ölçek,
                    0:00-0:10 bloğuyla AYNI — farklıysa uyumsuzluk okunur
```

> Bu pencere `HOOK_VE_ILK_SAHNE_KILAVUZU.md` §2'nin yerine geçmez; hook
> merak kurar, bu bölüm **vaadi doğrular.** İkisi çakışırsa hook kazanır:
> teyit, hook'un sakladığı şeyi ifşa ederek yapılmaz — kapağın SÖZÜNÜ tutar,
> filmin SIRRINI vermez.

---

# 4. ⚖️ VAAT BÜYÜTME SINIRI

**Mekanizma:** Sıralama artık yalnız tıklamaya değil **memnuniyete** bakar.
Büyütülmüş vaat kısa vadede tıklama üretir, hemen ardından erken terk üretir;
sistem bu asimetriyi tıklama tuzağı olarak sınıflandırır ve videoyu değil
KANALI cezalandırır — sonraki filmler aday havuzunda elenir.

```
KARAR KURALI
  □ Başlıkta/kapakta belirtilen ANA OLAY, filmin ilk %25-40'lık diliminde
    GÖRSEL olarak sunulmalı
  □ Vaadin karşılığı filmin son saniyelerine saklanamaz
  □ Vaat, çekilmiş/planlanmış bir kadrajın karşılığı olmalı — "olsa iyi
    olurdu" bir görüntü vaat edilmez

ÖRÜNTÜ UYARISI
  yüksek tıklama + erken terk  →  memnuniyetsizlik cezası (kanal düzeyinde)
  düşük tıklama + yüksek izleme →  yalnız o filmin kaybı (düzeltilebilir)
  ⇒ ikisi eşit kötü değildir; şüphede kalınca vaat KÜÇÜK tutulur
```

---

# 5. 🤐 SPOILER BÜTÇESİ — dört yüzey, tek bütçe [D114]

**Mekanizma:** Başlık, kapak, fragman ve açıklama aynı bilgiyi verirse merak
boşluğu kapanır ve izlemek için sebep kalmaz. Dördü birbirini tekrar etmez,
**tamamlar.**

| Yüzey | Ne verir | Ne vermez |
|---|---|---|
| **Başlık** | merkezdeki soruyu/çatışmayı ≤5 kelimeyle | çözümü, sonucu, karakterin akıbetini |
| **Kapak** | başlığın sorusunun fiziksel/tehlikeli anını | başlığın metnini görsel olarak tekrar etmez |
| **Fragman** | atmosferi, çaresizliği, görsel kaliteyi; tansiyon zirvedeyken keser | doruğu, twist'i, finali (FRAGMAN §1.2) |
| **Açıklama** | evrenin kuralını doğal cümlelerle, bağlam | olay örgüsünü, sonu, fragmanın sakladığını |

```
TEK CÜMLE TESTİ — dördü de yazıldıktan sonra koşulur
  Dört yüzeyi yan yana koy. Bir yabancı, filmi izlemeden hikâyenin
  sonunu tek cümleyle söyleyebiliyor mu?
  ✅ HAYIR → bütçe tutuyor
  ⛔ EVET  → hangi yüzey fazla verdi, orası kısılır (D114'ün vakası:
             açıklama metni)
```

---

# 6. 🚪 KABUL-RET TESTLERİ — paket üretime girmeden

```
KAPAK KARESİ
  □ Vizörde net bir yansıma VAR ya da duruş belirgin bir hedefe yönelmiş
  □ Silüet ile arka plan arasında keskin kontrast var
  □ Kapaktaki kompozisyon, ölçek, palet ve ışık 0:00-0:10 bloğunda birebir var
  □ Kapak, başlığın soyut sorusunu fiziksel bir ana çeviriyor

BAŞLIK VE METAVERİ
  □ Başlık ≤5 kelime ve izleyiciye NEREYE bakacağını söylüyor
    (aynı test: ONERME_VE_NOVUM §4③ — orada konsept, burada paket)
  □ Başlıktaki ana olay ilk %25-40'ta görsel olarak var
  □ Açıklama doğal cümlelerle yazılmış; etiket yığını değil
  □ Tümü büyük harf, "ŞOK EDİCİ" kalıpları, abartı işareti yok
  □ Dört yüzey TEK CÜMLE TESTİ'ni geçiyor (§5)
```

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Kapak metnini bu dosyanın belirlemesi | Kapak üstü metin KAPAK_FOTOGRAFI_MIMARISI'nın işidir (0-3 kelimelik merak boşluğu + 120 px posta pulu testi). ⚠️ Karıştırma: metin yasağı [D13 · D45] filmin İÇİNE aittir, kapağa değil. Bu dosya yalnız hangi KARE olduğunu seçer. |
| "Yüzü göster, gözlerle bak" — en güçlü kapak çapası | Vizör açılmaz [D37 · D57]. Karşılığı §2'deki üç odaktır. |
| CTR / AVD eşik tablolarının bu dosyaya kopyalanması | Sayı iki yerde tutulmaz: KAPAK §7.1 ve YAYIN_VE_PERFORMANS §2 tek kaynaktır (§0①). |
| Fragmanı "ilk 30 saniyenin özeti" yapmak | Fragman kılavuzu farklı bir yapı tanımlıyor (dikey 3-6 / yatay 8-12 vuruş, tek mekanik). Çakışırsa FRAGMAN_KILAVUZU kazanır. |
| Dikey fragmanı yatay filme dönüşüm aracı saymak | Dönüşüm oranı bunu taşımıyor (DIKEY_MIKRO_DRAMA §6). Fragman yönlendirir, dönüşümü garanti etmez. |
| A/B test ile kapak seçimi | Yöntem KAPAK §7'de duruyor; ayrıca örneklem kuralı olmadan koşulmaz (YAYIN_VE_PERFORMANS §3). |

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 7 maddesi

```
□ 1. KAPAK ANI satırı plana yazıldı mı: sahne · saniye · kompozisyon ·
     ışık · odak (§1)
□ 2. Kapak anı 0:00-0:10 bandından mı seçildi
□ 3. O sahnenin promptunda ışık ve kompozisyon SAYIYLA yazılı mı
□ 4. Kapak anı kurgu kapısının KESİLEMEZ listesinde mi
□ 5. Üç odaktan hangisi kullanılıyor — vizör yansıması / kontrast silüet /
     fraktal ölçek (§2)
□ 6. Başlıkta vadedilen ana olay ilk %25-40'ta görsel olarak var mı (§4)
□ 7. Dört yüzey yazıldıktan sonra TEK CÜMLE TESTİ koşuldu mu (§5) —
     sonucu plana/teslim notuna yazıldı mı [D114]
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/5.md                      bu kılavuzun kaynak araştırması (22.08.2026)
KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md   kapak YAPIMI · §5 güvenli alan · §7 CTR skalası
                                       · kapak üstü 0-3 kelime kuralı orada durur
VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md     başlık/açıklama metninin yazımı
FRAGMAN_KILAVUZU.md                    §1.2 spoiler kapısı — çakışırsa o kazanır
HOOK_VE_ILK_SAHNE_KILAVUZU.md          §2 S0 · §6 vaat-teslim (çakışırsa hook kazanır)
ONERME_VE_NOVUM_KILAVUZU.md            §4③ başlık şeması testi — aynı testin konsept koşusu
KURGU_VE_TESLIM_KILAVUZU.md            §1 kurgu kapısı · §5 teslim sırası
YAYIN_VE_PERFORMANS_KILAVUZU.md        §2 eşikler · §3 örneklem · §6 geri besleme
PROMPT_KONTROL/                        kapak anı promptunda sayı var mı
DERSLER/07_KURGU_VE_ANLATI.md          D114 tam metin · D62 · D100
```
