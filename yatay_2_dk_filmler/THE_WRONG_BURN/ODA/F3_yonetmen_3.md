# THE_WRONG_BURN — F3 · yönetmen · tur 2 BİRLEŞTİRME GEÇİŞİ · çekim listesi son hâl (A "Arkanı Dön")

```
GİRDİ      FILM.md §1 · §2 · §3-§5 iskeleti · ODA/F3_yonetmen_2.md (önceki, tam) ·
           eleştiri: F3_teknik-danisman_2.md (ÖLÜMCÜL 0 · CİDDİ B1-B5 · KÜÇÜK B6-B9) ·
           F3_izleyici_2.md + F3_animatik_2.md (Fable: yönetmene yeni madde yok)
OKUNDU     uretim_hatti/araclar/film_dogrula.py: ZIHINSEL + META desenleri, cekim() denetimi (bu tur)
           BILINEN_TUZAKLAR · ARIZA_LISTESI (T) · GOSTERIM_COZUMLERI · FLOW_GERCEKLERI §1 §9: tur 2'de okundu,
           bu turda yeniden okunmadı
FABLE      mod 12/12 "Frames to Video" ve "10 s yolu: P14" notu değişmez · olaylar 0-7 s · gösterge 4/4
           seçeneği F5/F7'ye ertelendi · kural ölçüsü 1 gerekçeyle bırakıldı · eleştirmenler yeniden çağrılmaz
FORMAT     12 çekim × 10 s = 2:00 · tek grup G01 · S<n> = C<nn>
ÇIKTI      §4 tablosu FILM.md §4'e birebir (14 sütun; son üçü "—") · §3 referanslar FILM.md §3'e · §5 notlar
```

## 0. CEVAPLAR (F3_teknik-danisman_2.md)

- **B1 CİDDİ · C06 ışığın yeri: KABUL.** C06'dan "sağ omuz" ibaresi hem Ekranda görünen hem Taraf/yön sütunundan
  çıktı. Işık artık yalnız ekran terimiyle yazılıyor: "kadrajın sağ üstünde, başının arkasında ve derinde, yüzünün
  baktığı yönün karşı tarafında". Başlangıç karesinde de ışık ekranın sağında. Aynı kusur C11'de de vardı
  ("istasyon sağ omzunun üstünde"); o da ekran terimine çevrildi. Bütün tabloya bir yazım kuralı kondu (§1 karar 6):
  yalın "sağ/sol" yalnız ekran tarafını anlatır. Vücut tarafı yalnız uzuv adında ("sağ eldiven", "sağ bilek") ve
  kamera konumunda ("Sela'nın sol arkasından") geçiyor.
- **B2 CİDDİ · C09 "mesafe sabit": KABUL.** Cümle silindi. Bram'ın yolu artık düz bir hat: eldivenin ötesinden ve
  yukarısından soldan sağa geçiyor. Başlangıçta eldivenden iki insan boyu uzakta. En yakın nokta yolun ortasında
  (~3,5 s) ve orada bile arada bir insan boyu açık boşluk var. Yol kolun hizasından geçmiyor ve eldiveni merkez
  alan bir yay çizmiyor. Bu yüzden ıskanın taşıyıcı karesi 3,5 s'deki en yakın nokta oluyor. İlk kare de ıskayı
  okutuyor, çünkü boşluk orada daha büyük.
- **B3 CİDDİ · C09 kamera tarafı: KABUL, yol (a).** Kamera Sela'nın **sol arkasına** alındı. Kanca ve bilek
  göstergesi C09'dan çıktı (`KANCA_yumrukta_v1` referansı listeden düştü, `BILEK_1-3_v1` yalnız C07'de kaldı).
  **Neden (a):**
  1. Ekran yönü kendiliğinden tutuyor. C06-C11 boyunca Sela sola bakıyor. Sol arka ¾ kamerada "sola ve derine bakış"
     geometrinin doğal sonucu; C04'ün (sağ arka ¾, sağa ve derine) aynası. Çekim C06-C11 yön zincirini bozmuyor.
  2. (b) Sela'nın gövdesini derine, yalnız kaskını sola çevirmeyi istiyor. Bu giysi de kask da filmde tek parça
     (bilim B6: kask göğse düşmez; aynı kural kaskın gövdeden ayrı dönmesini de dışarıda bırakır). "Yalnız kask
     döner" fiziksel karşılığı olmayan bir boyun burulmasıdır ve modelin kaynaşma örüntüsüne düşer.
  3. Iskayı taşıyan uzuv (uzanmış sol kol ve açık eldiven) kameraya en yakın ve kadrajdaki en büyük şey oluyor.
     Tek bilgi en okunaklı yerde duruyor.
  4. İki figür ve hareket olan bir çekimden iki risk çıkıyor: el-nesne teması (yumruktaki kanca, T01) ve okunacak
     gösterge (T06/T09).
  **Bedeli:** tretman S9'daki "sağ elinde kanca" hazırlığı ve tur 2'deki "kalan tek ışık yerine ip" imgesi gitti.
  Bunun kabul edilebilir olmasının nedeni animatik tur 2'de görünüyor. Kanca yumruktayken bile izleyici "Bram'ı nasıl
  yakaladı?" diye sordu, yani bu görüntü o soruyu kapatmıyordu. Cevabı C10'un ilk karesi verdi: "Kanca … takılmış …
  Bram'ı yakaladı" (C10 ✅). Araç C02'de kuruluyor (kanca boşta, ip kısa). Atış C09/C10 kesmesinde, silkinme sesiyle
  geçiyor. Sonucu C10'un ilk karesinde görünüyor (T14). Tretmandan sapma §5 not 5'te.
- **B4 CİDDİ · C10 kol hareketi arkadan görünmez: KABUL, önerilen yol.** İki kolun göğse toplanması düştü. Yerine
  tek hareket geldi: kameraya yakın **sol kol yavaşça yana ve yukarıya kalkıyor**, omuz hizasının biraz üstünde duruyor
  (2,0-4,5 s). Eldiven açık kalıyor. Yeni durum karesi `BRAM_kolkalkik_v1`, `BRAM_kontrolsuz_v1`'in aynısı; tek fark
  sol kol. Sağ kol, bacaklar, ip ve fon iki karede aynı. İp çantadan kadrajın **sol alt köşesine** iniyor, kol ipin
  yukarısında kalıyor. Böylece tek uzuv hareketi ipten de gövdeden de uzakta.
  **Neden bu yol, öbür ikisi değil:**
  1. *Kamerayı Bram'ın önüne almak:* vizör opak olduğu için yüz sorunu çıkmazdı. Ama sırttaki kanca-çanta bağı
     gövdenin arkasında kalırdı. C10'un bilgisinin ilk yarısı ("kanca tuttu") kaybolurdu. İki kolu göğse toplamak
     da el-el ve el-göğüs kaynaşması (T01) olarak kalırdı.
  2. *Hareketi kaldırıp ayılmayı seste bırakmak:* KABUL ölçüsü 3 iki animatikte de ✗ çıktı. Görüntü desteği gerekli.
     Ses yalnız yedek.
  3. Seçilen hareket filmde Bram'ın C01'den beri ilk kendi hareketi. Gövdeden uzağa, yavaş ve tek uzuvla oluyor.
     Toparlanma soluğu (3,6) ve söz (4,0) inişin değil kalkışın ortasına düşüyor.
  **C11-C12'deki duruş:** teknik "aynı duruma çevir" diyordu. Bunu kısmen uyguladım. Kalkık kolu ikinci gün doğumuna
  kadar (C12, ≈ 80 dk sonra) havada tutmak sebepsiz bir poz olurdu. C11 ve C12'de Bram **dik, kolları iki yanında**:
  bu, `BRAM_v1`'in temel duruşu, ek referans gerektirmiyor. Kontrolsüz duruştaki yarı açık uzuvlardan açıkça ayrılan,
  bilinçli bir duruş. Değişim C10/C11 kesmesinde. "Kolları göğsüne toplanmış" tarifi bütün tablodan çıktı.
- **B5 CİDDİ · C07 elin iniş hedefi: KABUL.** El artık aşağı inmiyor. Kumanda kutusundan yana, gövdesinden uzağa,
  kadrajın sol kenarına doğru açılıyor ve göğüs hizasında, sol kenara yakın duruyor (2,0-4,5 s). Kehribar nokta alt
  kenarın sağ yarısına alındı, yani elin yolunun karşı köşesinde. El kadrajın içinde kalıyor, nokta ile el
  birbirinden uzak. Bilekteki dört yuva hareketten sonra da kadrajda. "Kumandadan çekiliyor" okuması korunuyor: el
  temastan uzağa, ama yine kadrajın içinde gidiyor.
- **B6 KÜÇÜK · 7-10 s cümleleri 8 s klipte karşılıksız: KABUL (F5'e kayıt).** Tablo değişmedi (Fable: mod ve P14 notu
  sabit). Her satırda "7-10 s'de …" (C08 ve C12'de "6-10 s'de …") Ekranda görünen sütununun **son cümlesi** ve başka
  hiçbir yerde geçmiyor. Bu yüzden F5'te tek bir kesimle ayrı "uzatma / 10 s" satırına taşınabilir. 8 s promptuna
  yalnız ondan önceki cümleler gider (§5 not 1).
- **B7 KÜÇÜK · "sallanıyor / asılı": KABUL.** C01: "korkuluktan uzanmış, çok yavaş kendiliğinden kayıyor". C12:
  "korkuluktan uzanmış, yerinde duran saçaklı kopuk uç". KAPAK referans tarifi de aynı biçimde.
- **B8 KÜÇÜK · C08 başlangıç karesi ile bant: KABUL.** Bant başlangıç karesinde zaten parlak, güneş kenara değiyor.
  Hareket yalnız "güneş kenardan ayrılıyor, beyaz ışık yayılıyor, bant soluyor".
- **B9 KÜÇÜK · referans tarifinde olumsuz cümleler: KABUL.** §3 "Her referansın taşıması gerekenler" olumlu
  geometriyle yeniden yazıldı: "düz, mat, işaretsiz yüzey", "yan yana dört yuvarlak yuva", "kaskın içi karanlık ve
  sade", "bel halkası çıplak metal", "kolla ip arasında açık boşluk". Referans tablosundaki "yüz yok" etiketi
  "vizör opak ve yansıtıcı" oldu. Yasaklar yalnız tablonun Risk sütununda. Tek istisna §3'ün son maddesi: o madde
  görüntüyü değil prompt metnini anlatıyor ("dosya adındaki sayılar prompta yazılmaz").
- **KORU ×4: korundu.** C07'de el temastan uzakta başlıyor ve uzağa gidiyor (hedef değişti, yön değişmedi) · C01/C12
  aynı korkuluk ilişkisi · C09/C10 kesmesinde atış ve takılma · C04 sağ arka ¾.
- **KAPSAM DIŞI:** C07'nin "harcamıyor" fiili "Anlatacağı TEK bilgi" sütununda. Ekranda görünen sütununda yok ve
  ZIHINSEL deseninde de yok; dramaturg alanı, değiştirmedim. C11'de istasyonun küçülmesi film içi bir görüntü, fizik
  iddiası değil (bilim tur 1 notu; F9 never-claimed).

### İzleyici + animatik (F3_izleyici_2.md · F3_animatik_2.md)

- Fable kaydı gereği yönetmene yeni madde yok. Kararlar aynen uygulandı:
  - Gösterge 4/4 seçeneği F5/F7'ye ertelendi (§5 not 6).
  - Kural ölçüsü 1 gerekçeyle bırakıldı.
  - C11 tıslaması F4'te belirgin olacak (§5 not 4).
- İki değişiklik izleyici bulgularına dolaylı olarak dokunuyor:
  - C08 silueti artık kontrolsüz duruşta (kollar yarı açık), C09 ile aynı. Bu "Bram sandım, emin değilim" okumasına
    ikinci bir bağ ekliyor: aynı siluet bir sonraki çekimde yakından görünüyor.
  - C10'daki tek kol kalkışı ölçü 3'ün ("ayıldı") görüntü tarafı. F7'de gerçek karede sınanacak.

## 1. YÖNETMEN KARARLARI (tur 2'den değişenler kalın)

1. Olay penceresi 0-7 s. 7-10 s'de yalnız süren hareket ya da duruş var. **Bu kısım Ekranda görünen sütununun son
   cümlesi (teknik B6).** 7 s sonrasına taşan ses (C04 replik 7 · C05 sessizlik · C07 nefes · C12 nefes) kurgu işi.
2. Kritik olaylar kesmeyle bölündü: bedel C02 → C03 → C04 · karar C05 → kesme → C06 → C07 · yakalama C08 → C09 →
   **kesme: kancanın kavranması, atış, takılma, silkinme, dönüşün durması** → C10. Kadrajda üretilen tek duruş
   değişimi **C10'daki tek kol kalkışı**: iki durum karesiyle sınırlı, farkı tek uzuv ve yedeği var.
3. Gösterge Sela'nın sağ bileğinde. Yanan yuva soğuk beyaz, boş yuva karanlık. Kadrajda göründüğü çekimler:
   C03 (2/2) · C07 (1/3) · C12 (0/4). **C09'dan çıktı (teknik B3 (a)).** Değişim hep kadraj dışında.
4. Sela'nın vizörü berrak, Bram'ın vizörü opak. Bram'ın yüzü hiç görünmüyor. Kask ve giysi tek parça; kask gövdeden
   ayrı dönmez.
5. C01 ile C12 aynı kadraj ilişkisinde (kapak tarafı, korkuluk, kopuk uç, sıcak ışık).
6. **Yön yazımı (teknik B1):** Ekranda görünen ve Taraf/yön sütunlarında yalın "sağ/sol" yalnız ekran tarafı. Vücut
   tarafı yalnız uzuv adında (sağ eldiven, sol kol, sağ bilek) ve kamera konumunda ("Sela'nın sol arkasından")
   geçiyor. Ekran yönleri:
   - Sela C02-C05'te sağa, C06-C11'de sola bakıyor.
   - Bram'ın ışığı C02-C05'te sağda. **C06'da kadrajın sağ üstünde, Sela'nın arkasında.** C07'de alt kenarın sağ
     yarısında.
   - Bram C08'de solda, Sela'nın önünde. C09'da soldan sağa geçiyor. C10-C11'de sağda, arkada.
   - İstasyon C11'de sağ kenarda.
   - Güneş C02-C11 boyunca solda.
7. Mod: 12/12 Frames to Video. İnsansız çekim yok.
8. Ölçek dizisi (H10):
   1. geniş
   2. orta profil
   3. yakın insert
   4. orta-geniş ¾ sağ arka
   5. yakın ¾ ön
   6. orta ¾ ön
   7. yakın-orta
   8. çok geniş profil
   9. **orta-yakın ¾ sol arka (omuz üstü)**
   10. orta, Bram tekli, ¾ sol arka
   11. geniş yandan
   12. yakın-derin
   Arka arkaya aynı ölçek yok. C09 ile C10'da kamera iki ayrı figürün sol arkasında. Bu sayede Sela solda, Bram sağda
   yerleşimi kesme üstünden korunuyor (T11).
9. Bağlar: C02 ↔ C04 aynı kadraj ilişkisinde (kural bağı). **C08 ↔ C09 aynı siluet duruşunda (kontrolsüz).**
   C02 kanca boşta → C10 kanca çantada (araç → sonuç, T14). **Bram'ın duruş sırası: dik (C01) → kontrolsüz (C08-C10
   başı) → tek kol kalkık (C10 sonu) → dik (C11-C12).**

## 4. ÇEKİM LİSTESİ — FILM.md §4'e birebir

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Bram'ın ipi koptu ve sıcak ışıklı kapaktan (ev) uzağa sürükleniyor; korkuluğa bağlı kalan yalnız Sela. | Kameraya en yakın düzlemde açık kapağın kenarı ve korkuluk. Korkulukta iki ip ucu var: Sela'nın kancası kilitli ve kıpırtısız; yanında Bram'ın ipinin saçaklı kopuk ucu korkuluktan uzanmış, çok yavaş kendiliğinden kayıyor. Kapağın içinden gelen düz, sıcak ışık korkuluğa ve iki uca vuruyor. Solda Sela istasyonun dış yüzeyinde, korkuluğun yanında; iki eldiveni çekimin başından tutamakta, kaskı sağa dönük. Arkada dönen radyatör kolu 0-6 s'de yavaşça geri çekiliyor ve duruyor. Sağda, kolun önünde küçük, beyaz giysili, mavi omuz bantlı Bram dik duruşta, düz bir çizgide, yavaşça uzaklaşıyor; kaskında kehribar işaret lambası, sırt çantasının yanı ezik. Güneş tepede, Dünya altta ve tamamen aydınlık. 7-10 s'de Bram aynı hızla uzaklaşmayı sürdürüyor. | geniş · derin · sabit; kamera kapak tarafında, korkuluk ve kapak kenarı önde (C12 ile aynı ilişki) | Sela solda, sağa bakar · Bram sağda, sağa ve derine uzaklaşır · Dünya altta · güneş tepede (zenit) · istasyon: kapak kamera tarafında, radyatör kolu arkada | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (kolun çekilmesi 0-6 s; 7-10 s yalnız süren sürüklenme) · T01 çarpma ve kopma çekimden önce; uç baştan serbest, korkuluğa el değmez, Sela'nın elleri baştan tutamakta ve kıpırdamaz · T08 kopuk uç vakumda: rüzgârda sallanma ya da aşağı sarkma yazılmaz, yalnız çok yavaş kendiliğinden kayma (teknik B7) · T09 iki ip ucu başlangıç karesinde, kanca sabit · T10 Bram'ın tek hareketi düz sürüklenme, dönmez (F1 B8) · T06 istasyon yüzeyi panelsiz ve yazısız, kapak içi düz sıcak ışık, ekran yok · T15 iki kişi küçük ve ayrık, bantlar ayrı (turuncu/mavi) · T13 replik 1 telsiz, kurguda | SELA_v1 · BRAM_v1 · KAPAK_iki_uc_v1 · ISTASYON_v1 · DUNYA_gunduz_alt_v1 | G01 | ⬜ | — | — | — |
| C02 | Sela, Bram'ın sesine rağmen ona doğru ateşleyip yaklaşıyor; Bram ipin yetişemeyeceği kadar uzakta. | Sela yandan, sağa dönük, belden yukarısı ve kalçası kadrajda. Sağ eldiveni göğüsteki kumanda kutusunu çekimin başından kavramış. Giysisi çekimin başından sağa doğru itiliyor ve hafifçe titriyor; titreme çekim boyunca aynı kalıyor. Önünde, sağda, kadrajın öbür ucunda Bram'ın kehribar ışığı 0-7 s'de küçük bir noktadan belirgin bir parıltıya büyüyor ve uzak bir parıltı olarak kalıyor. Kalçasının yanında kendi ipi kısa, gevşek bir kıvrım hâlinde süzülüyor; ucundaki kanca boşta. Berrak vizörün ardında dudakları kapalı. Güneş yüksekte, hafif solda; Dünya altta, tamamen aydınlık. 7-10 s'de titreme ve ışığın yavaş büyümesi aynı biçimde sürüyor. | orta · yandan, profil (Sela'nın sağ yanından) · sabit | Sela sağa bakar ve sağa ilerler · Bram ışığı sağda, uzakta, büyür · Dünya altta · güneş yüksek, zenitten ≈10° geride (hafif sol üst) · istasyon kadraj dışı, solda | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (ışığın büyümesi; titreme çekim boyunca süren tek düzenli hareket, C03'e taşar) · T03 soğuk gaz görünmez: itki titreme ve büyüyen ışıkla okunur, tıslama kurguda · T01 kumanda tutuşu baştan kurulu, el kıpırdamaz · T08 ip kısa ve kıvrımlı, sarkmaz; sarkarsa yedek kadraj bel üstüdür, kanca kadraj dışında kalır ve "ip kısa" desteği düşer (bilgi kalır) · T05 kancanın korkuluktan çözülmesi kesmede, durum karesi KANCA_bosta · T06 bilek göstergesi kumanda kutusunun arkasında, okunmaz · AĞIZ dudaklar kapalı, replik 2 telsiz | SELA_v1 · KANCA_bosta_v1 · DUNYA_gunduz_alt_v1 | G01 | ⬜ | — | — | — |
| C03 | O ateşleme gazın yarısına mal oldu: dört yuvadan ikisi yanıyor (yanan = kalan). | Sela'nın sağ bileği ve ön kolu kameraya yakın, kadrajın ortasında; eldivenin üst kenarı alt kenardan dışarı çıkıyor. Bilekte yan yana dört yuva var: soldaki ikisi soğuk beyaz yanıyor, sağdaki ikisi karanlık. İlk 1,6 saniyede ön kol hafifçe titriyor; 1,6 s'de titreme duruyor ve kol hareketsiz kalıyor. Arkada, odak dışında, Dünya'nın tamamen aydınlık yüzü sağdan sola yavaşça kayıyor. Işık bileğe sol üstten, yandan vuruyor. 7-10 s'de Dünya aynı hızla kaymayı sürdürüyor. | yakın insert · bilek · sabit; derinlikte Dünya | bilek ortada, eldiven alt kenardan çıkar · Dünya arkada, sağdan sola kayar · güneş zenitten ≈30° geride, sol üst | 10 | Frames to Video | 10 s yolu: P14 · olay 1,6 s (titremenin durması); Dünya'nın kayması çekim boyunca süren tek düzenli hareket · T06 gösterge dört yazısız ışık noktası; prompta sayı, sayı kelimesi ve replik girmez · T05/T09 nokta durumu başlangıç karesinden (BILEK_2-2), çekim boyunca sabit; model tutmazsa denemeler arasından seçilir, prompta cümle eklenmez · T01 eldiven ve kumanda kadraj dışında · T03 itkinin sonu titremenin durmasıyla ve kurgudaki tıslama kesilmesiyle okunur · AĞIZ vizör kadraj dışı, replik 3-4 telsiz ve kask içi | SELA_v1 · BILEK_2-2_v1 · DUNYA_gunduz_alt_v1 | G01 | ⬜ | — | — | — |
| C04 | Ona doğru yakan Sela yükseldi ve geride kaldı: Bram'ın ışığı da Dünya'nın kenarı da ondan aşağı iniyor. | Sela kadrajın solunda, sağ arkasından ¾ görünüyor, belden yukarısı kadrajda: kaskının arkası, sağ omzu ve turuncu bandı. Sağa ve derine bakıyor, kıpırtısız. Önünde, kadrajın sağ ortasında Bram'ın kehribar ışığı kaskıyla aynı hizadan başlıyor ve 0-7 s'de tek yönde aşağıya, Dünya'nın parlak yüzüne doğru iniyor ve küçülüyor; 7 s'de Sela'nın bel hizasının çok altında, Dünya'nın önünde küçük bir nokta. Kadrajın alt yarısında Dünya'nın tamamen aydınlık yüzü var; ince mavi kenarı, yani ufuk yayı, aynı sürede kadrajda biraz aşağı iniyor. Işık soldan ve yatığa yakın geliyor: kaskın ve omzun sol üst kenarı parlak, sağ yüzü Dünya'nın yansımasıyla yumuşak aydınlık. 7-10 s'de nokta aynı yönde çok yavaş inmeyi sürdürüyor. | orta-geniş · Sela'nın sağ arkasından ¾ · sabit; C02 ile aynı taraf, kamera arkaya ve geriye alındı | Sela solda, sağa ve derine bakar · Bram ışığı sağ ortadan sağ alta iner · Dünya altta, ufuk yayı iner · güneş zenitten ≈65° geride: solda, yatığa yakın · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (ışığın inişi ve ufkun inişi, aynı yönde ve aynı sürede) · T14/T11 ışık tek yönlü, yalnız aşağı ve küçülerek; kadrajdan çıkmaz, geri gelmez (F1 B4) · T07 ufkun inişi kamera eğimi gibi okunabilir: kamera sabit yazılır, Sela kadrajda aynı yerde kalır; ufkun inişi bozulursa düşer, bilgi ışığın inişine kalır · T18 güneş açısı promptta açık; "uzun gölge" yazılmaz, zemin uydurulmaz (bilim B3); zaman ışığın yönünden okunur (C02 tepeden → C04 soldan, yatık) · T04 yıldızlar sönük beyaz, tek renkli nokta kehribar · AĞIZ kamera kaskın arka ¾'ünde, vizörün kenarı bile kadraja girmez (replik 5-6-7) | SELA_v1 · DUNYA_gunduz_alt_v1 | G01 | ⬜ | — | — | — |
| C05 | Takasın karşısında Sela gözlerini kapatıyor ve ışıktan dönüyor. | Sela'nın yüzü yakından, ¾ önden, berrak vizörün ardında. Bakışı sağa, kadrajın sağ kenarındaki küçük kehribar noktaya dönük. Yüzü alttan Dünya'nın loş, mavi-gri yansımasıyla aydınlanıyor; kask kenarında soldan ve arkadan soğuk beyaz, ince bir kenar ışığı var. Dudakları kapalı. 0-5,5 s'de bakış noktada kalıyor. ~5,6 s'de gözleri kapanıyor. ~6,0-7,0 s'de gözleri kapalıyken omzu ve kaskı birlikte noktadan sola, küçük bir açıyla dönüyor ve duruyor. 7-10 s'de yüz yarı dönük, gözler kapalı, kıpırtısız; kehribar nokta sağ kenarda aynı yerde. | yakın · yüz, ¾ önden · sabit | Sela sağa bakar → gözler kapanır → kask ve omuz birlikte sola döner · kehribar nokta sağ kenarda, sabit · Dünya altta, alacakaranlık (yalnız yansıması) · güneş zenitten ≈85° geride: solda arkada, yataya yakın · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (gözler 5,6 · dönüş 6,0-7,0; 7-10 s duruş, sessizliği ses taşır) · T12 gözlerin kapanması filmin tek yakın tepki anı · T10 dönüş küçük, tek yönlü ve 7 s'de durur; dönüşün kalanı C05/C06 kesmesinde (F1 B2); kask gövdeyle birlikte döner · T16 yüz SELA_v1 başlangıç karesinden · T06 kask içinde ışık ve ekran yok, yüz dış ışıkla aydınlanır · T04/T18 kenar ışığı soğuk beyaz, sıcak renk yalnız kehribar nokta (bilim B5) · AĞIZ dudaklar "might" boyunca da kapalı (replik 8 telsiz 0,3-6,0, ardından 4,0 s sessizlik) | SELA_v1 · DUNYA_alacakaranlik_alt_v1 | G01 | ⬜ | — | — | — |
| C06 | KARAR: Sela ışığa sırtını dönmüş ateşliyor; Bram'ın ışığı arkasında küçülüyor. | Sela dönmüş: yüzü kadrajın soluna bakıyor, kameraya ¾ önden. Alçak güneş soldan vizöre vuruyor, parlaması yüzünün alt yarısını örtüyor. Kehribar ışık kadrajın sağ üstünde, başının arkasında ve derinde, yüzünün baktığı yönün karşı tarafında. Sağ eldiveni göğüsteki kumanda kutusunu çekimin başından kavramış. ~3,7 s'de giysisi tek ve sert bir itişle sola sarsılıyor; 3,7-7 s'de kadrajın sağ üstündeki kehribar ışık küçülüyor. Altta Dünya'nın alacakaranlık yüzü: güneş tarafında, solda aydınlık bir yay, gerisi loş. 7-10 s'de Sela aynı duruşta, ışık sağ üstte küçük bir nokta. | orta · önden ¾ · sabit | Sela sola bakar (dönüş kesmede; atalet kilidi başlar) · Bram ışığı kadrajın sağ üstünde, Sela'nın arkasında ve derinde, küçülür; başlangıç karesinde de sağda · Dünya altta, aydınlık yay solda · güneş zenitten ≈100° geride: solda, alçak, Dünya'nın kenarına yakın · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (sarsıntı 3,7 · küçülme 3,7-7) · T11 ışığın yeri yalnız ekran terimiyle: kadrajın sağ üstü, başın arkası, yüzün baktığı yönün karşısı; vücut tarafı ("omuz") yazılmaz (teknik B1) · T10/T05 dönüş kadrajda yok; çekim dönmüş başlar, sırt çantası sırtta · T03 soğuk gaz görünmez: tek sarsıntı ve küçülen ışık, tıslama kurguda 3,7 s'de · T01 kumanda tutuşu baştan kurulu · T08 atalet kilidi başlar, Sela C11'e kadar kendiliğinden dönmez · AĞIZ güneş parlaması yüzün alt yarısını örter (replik 9 kask içi 1,2-3,0) | SELA_v1 · DUNYA_alacakaranlik_alt_v1 | G01 | ⬜ | — | — | — |
| C07 | Kehribar nokta alt kenara kaydı, ama Sela kalan son ışığı düzeltmeye harcamıyor: el kumandadan çekiliyor. | Gece. Kadrajın üst kısmında Sela'nın yüzü küçük, sola dönük; gözleri aşağıda, kadrajın alt kenarındaki kehribar noktada. Yüzü yalnız aşağıdaki şehir ışıklarının vizördeki yansımasıyla soluk aydınlanıyor; vizörün alt yarısı şehir ışıklarını yansıtıyor. Solda ve önde Dünya'nın karanlık yüzü ve şehir ışıkları. Kehribar nokta alt kenarın sağ yarısında, göğüs hizasının çok altında. Kadrajın ortasında sağ eldiveni, göğsündeki kumanda kutusundan bir avuç uzakta, açık ve durgun; bileğindeki dört yuvadan biri soğuk beyaz yanıyor, üçü karanlık. 0-2 s'de el orada kalıyor. ~2,0-4,5 s'de el kumanda kutusundan yana, gövdesinden uzağa, kadrajın sol kenarına doğru yavaşça açılıyor ve göğüs hizasında, sol kenara yakın duruyor; parmaklar aynı açık duruşta, bilekteki dört yuva kadrajda. 4,5-7 s'de el orada, kıpırtısız. 7-10 s'de el sol kenarda, kehribar nokta alt kenarın sağ yarısında, ikisi de sabit. | yakın-orta · yüz üstte, el ve bilek ortada · önden, hafif üstten · sabit | Sela sola bakar, gözleri aşağıda · el kadrajın ortasından sol kenara açılır, göğüs hizasında kalır · Bram noktası alt kenarın sağ yarısında, elin yolunun karşı köşesinde · Dünya solda ve önde, gece yüzü · güneş Dünya'nın arkasında · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (elin açılması 2,0-4,5) · T01 temas yok: el başlangıç karesinde bir avuç uzakta, tek hareket temastan uzağa; parmak biçimi değişmez, yumruk düştü (tur 1 B4) · T01/T04/T09 elin hedefi kadraj içinde ve noktadan uzak: göğüs hizası, sol kenara yakın; alt kenara ve noktaya inmez, sıcak ışık eldivene geçmez (teknik B5) · T09/T06 gösterge başlangıç karesinde okunur (BILEK_1-3), hareketten sonra da kadrajda, sabit ve yazısız; kask içinde ekran ya da ışık kaynağı yok (F1 B6) · T18 gece, ay ışığı yok (bilim B5); aynı dünya cümlesi · T04 tek renkli nokta kehribar, yıldızlar sönük beyaz · AĞIZ yüz küçük ve üst kısımda, alt yarısı yansımayla örtülü; ağız okunursa kadraj değişir, replik 10 ağza çevrilmez | SELA_v1 · BILEK_1-3_v1 · DUNYA_gece_v1 | G01 | ⬜ | — | — | — |
| C08 | Ses haklıydı: Sela hiç dönmedi, Dünya başının üstüne geçti ve gün doğarken Bram tam önünde. | Yandan, çok uzaktan. Sela küçük, sola dönük, aynı duruşta. Dünya'nın yayı kadrajın üst yarısını dolduruyor, Sela'nın başının üstünde; ayaklarının altında siyah boşluk. Solda, Dünya'nın kenarında ince turuncu-mavi bir bant çekimin başından parlıyor ve güneş kenara değiyor. 0-6 s'de güneş kenardan ayrılıyor, beyaz ışık yayılıyor ve bant soluyor. Sela'nın yüzünün tam önünde, aynı hizada, güneşin önünde küçük ve koyu bir astronot silueti var: kask, omuzlar, yanlara yarı açık iki kol ve iki bacak. Kaskında ve omuz hattında ince parlak bir kenar, kaskın ortasında kehribar nokta. Siluet 0-6 s'de hafifçe büyüyor. 6-10 s'de ışık ve iki figür sabit. | çok geniş · profil · sabit | Sela sola bakar · Bram solda, yüzünün önünde, güneşe karşı · Dünya üstte (yay) · güneş solda, Dünya'nın kenarından doğuyor (ilerleme yönü) · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-6 s (güneşin ayrılması ve siluetin büyümesi) · T11/T18 bilginin kendisi Dünya'nın üstte olması: başlangıç ve bitiş karesinin ikisinde de Dünya üstte; bu çekimde BİTİŞ KARESİ ZORUNLU (sahneleme odasına); iki kare arasındaki fark yalnız ışık ve siluetin boyu · T18 bant başlangıç karesinde zaten parlak, güneş kenarda; hareket yalnız ayrılma ve yayılma (teknik B8) · T18 Bram güneşe karşı koyu, önden aydınlanmaz (bilim B7); siluetin kimliğini kehribar nokta taşır · T05 siluet BRAM_kontrolsuz duruşunda (uzuvlar yarı açık), C09 ile aynı; dönüş yazılmaz · T15 iki küçük, ayrık figür · T04 güneşin yanında yıldız yok ya da sönük; turuncu-mavi bant yalnız doğuş anında | SELA_v1 · BRAM_v1 · BRAM_kontrolsuz_v1 · DUNYA_dogus_ust_v1 | G01 | ⬜ | — | — | — |
| C09 | Iska: kontrolsüz dönen Bram, Sela'nın uzanmış elinin bir insan boyu ötesinden geçiyor. | Sela'nın sol arkasından ¾. Kadrajın solunda, kameraya en yakın düzlemde Sela'nın sol omzu, turuncu bandı ve sol kolu var: kol çekimin başından omzundan sola, yukarıya ve derine uzanmış, açık eldiveni boşlukta duruyor. Kaskının arkası kadrajın alt ortasında, sola ve derine dönük. Kadrajın üst yarısında Dünya'nın loş yüzü, solda güneş tarafında ince aydınlık bir yay. Mavi bantlı Bram sol üstte, derinde, açık eldivenin iki insan boyu ötesinde: kolları ve bacakları nötr bir duruşta yarı açık ve donuk, figür kendi çevresinde çok yavaş dönüyor; sırtındaki çantanın ezik, bükülmüş çerçevesi görünüyor, kaskındaki kehribar lamba yanıyor. 0-7 s'de Bram düz bir hatla, eldivenin ötesinden ve yukarısından soldan sağa süzülüyor. ~3,5 s'de eldivene en yakın noktada; aralarında Dünya'nın loş yüzü önünde bir insan boyu açık boşluk var. 7 s'de Bram sağ üstte, Sela'nın kaskının gerisinde ve yukarısında. Sela baştan sona kıpırtısız. 7-10 s'de Bram'ın yavaş dönüşü ve süzülüşü aynı biçimde sürüyor. | orta-yakın · Sela'nın sol arkasından ¾, omuz üstü · sabit | Sela sola ve derine bakar (C06-C11 ekran yönüyle aynı) · sol kol kameraya en yakın, sola-yukarı-derine uzanmış · Bram sol üstten sağ üste, eldivenin ötesinden ve yukarısından geçer · Dünya üstte, aydınlık yay solda · güneş solda, ufka yakın · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (Bram'ın geçişi; en yakın nokta ~3,5 s); Sela'da hareket yok · T01/T15 uzanma hareketi yok: sol kol başlangıç karesinde uzanmış ve boşlukta · T01/T10 Bram'ın yolu düz bir hat: başlangıçta iki insan boyu, en yakın noktada bir insan boyu, hiçbir noktada daha yakın değil; eldiveni merkez alan yay çizmez, kolun hizasından geçmez; "mesafe sabit" yazılmaz (teknik B2) · T11 kamera Sela'nın sol arkasında, Sela sola ve derine bakar; kask gövdeyle tek parça, ayrı dönmez (teknik B3, yol a) · T01 kanca ve sağ el kadrajda yok: kavrama, atış ve takılma C09/C10 kesmesinde (silkinme sesi kurguda) · T06/T09 gösterge kadrajda yok (son okunuşu C07) · T10 Bram'ın dönüşü tek eksenli ve çok yavaş (7 s'de çeyrek turdan az), uzuvların duruşu değişmez · T05 BRAM_kontrolsuz durum karesi; kask figürle tek parça, göğse düşmez (bilim B6) · AĞIZ Sela'nın yüzü kadraj dışı (kaskın arkası), hat sessiz | SELA_v1 · BRAM_v1 · BRAM_kontrolsuz_v1 · DUNYA_alcak_ust_v1 | G01 | ⬜ | — | — | — |
| C10 | Kanca tuttu ve Bram ayılıyor: ipin ucunda bağlı, ilk kez kendi kolunu kaldırıyor. | Bram tek başına, kadrajın sağ yarısında; sırtı ve sol yanı kameraya ¾, sol omzundaki mavi bant görünüyor. Sırtındaki çantanın ezik, bükülmüş çerçevesine kanca ilişmiş ve kıpırtısız; kancadan Sela'nın ipi dümdüz ve gergin olarak aşağıya ve sola, kadrajın sol alt köşesine uzanıyor. Bram başlangıçta kontrolsüz duruşta: kolları ve bacakları yarı açık, figür sabit, dönüş durmuş. ~2,0-4,5 s'de sol kolunu yavaşça yana ve yukarıya kaldırıyor; kol omuz hizasının biraz üstünde, ipin yukarısında duruyor, eldiveni açık. Kolla ip arasında açık boşluk var. Sağ kolu ve bacakları aynı yarı açık duruşta. Arkada Dünya'nın loş yüzü ve ince aydınlık yayı çekim boyunca birkaç derece kayıyor. İp çekim boyunca düz ve gergin. 7-10 s'de kol yukarıda ve kıpırtısız, fon aynı yavaşlıkta kaymayı sürdürüyor. | orta · Bram tekli · sol arkasından ¾ · kamera Bram'a kilitli, fon birkaç derece kayar | Bram sağda, ip sol alt köşeden çıkar (Sela solda, kadraj dışı) · sol kol yana-yukarı, kadrajın sol üstüne doğru · Dünya fonda, yavaşça kayar · güneş soldan, ufka yakın · istasyon kadraj dışı | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (kolun kalkışı 2,0-4,5; nefes 3,6 ve söz 4,0-6,0 kurguda) · T01 kanca-çanta teması başlangıç karesinde kurulu ve değişmez; takılma kesmede; eller ipe ve kancaya değmez · T01/T10 tek uzuv hareketi kameraya yakın sol kolda ve gövdeden uzağa; kol omuz hizasının biraz üstünde durur, ip sol alt köşeye iner, kol ipin yukarısında kalır; iki kolu göğse toplama düştü (el-el ve el-göğüs kaynaşması, teknik B4) · T08 ip baştan gergin ve düz; ne takılma ne gerilme anı var · T05 başlangıç BRAM_kontrolsuz, bitiş BRAM_kolkalkik: iki karenin farkı yalnız sol kol; sağ kol, bacaklar, ip ve fon aynı (sahneleme odası bitiş karesini değerlendirir) · T10 iki hareket: fonun yavaş kayması ve kolun kalkışı; kalkış bozulursa düşer, ayılma seste kalır (tretman §4 yedeği) · T15 kadrajda tek kişi · AĞIZ Bram arkadan, vizör görünmez (replik 11 telsiz) | BRAM_v1 · BRAM_kontrolsuz_v1 · BRAM_kolkalkik_v1 · KANCA_cantada_v1 · DUNYA_alcak_ust_v1 | G01 | ⬜ | — | — | — |
| C11 | Kural ikinci kez, kimse söylemeden: Sela eve sırtını dönüp son ışığı yakıyor. | Geniş, yandan, hafif arkadan. Sela kadrajın sol yarısında, sola dönük. Onun arkasında, kadrajın ortasının sağında, dümdüz ve gergin ipin ucunda Bram var: dik, kolları iki yanında. Bram'ın ötesinde, kadrajın sağ kenarına yakın, uzakta küçük istasyon ve açık kapağının geniş, sıcak ışığı. Dünya üstte ve loş, solda ince aydınlık bir yay. ~2,5 s'de Sela'nın giysisi sola sarsılıyor; ip gergin kalıyor ve Bram'ı arkasından çekiyor; ikisi birlikte kısa ve yumuşak bir sarsıntıyla sola ilerliyor. 3-7 s'de ikisi birlikte yavaşça sola süzülüyor, sağ kenardaki istasyon biraz küçülüyor. 7-10 s'de süzülüş aynı biçimde sürüyor. | geniş · yandan, hafif arkadan · sabit | Sela sola bakar ve sola ilerler · Bram kadrajın sağ yarısında, Sela'nın arkasında, ipin ucunda · istasyon kadrajın sağ kenarına yakın, Bram'ın ötesinde, küçük, küçülür (C06'da ışığın durduğu taraf: ekranın sağı) · Dünya üstte · güneş solda, ufka yakın | 10 | Frames to Video | 10 s yolu: P14 · olaylar 0-7 s (sarsıntı 2,5; birlikte ilerleme 2,5-7) · T03 soğuk gaz görünmez: sarsıntı ve ipin ikinci figürü taşımasıyla okunur · T11 yerler yalnız ekran terimiyle; "sağ omuz üstünde" yazılmaz (teknik B1) · T05 Bram dik, kollar iki yanında (BRAM_v1 temel duruşu); kolun inişi C10/C11 kesmesinde · T15 iki figür küçük ve ayrık, arada gergin ip, bantlar ayrı · T06 istasyon uzakta, küçük ve yazısız; kapak yalnız sıcak ışık · T04 iki sıcak ışık ayrı tutulur: kapak geniş ve yumuşak, kehribar küçük nokta · T01 kumanda tutuşu baştan kurulu, bu ölçekte el okunmaz · T09 gösterge görünmez: 1→0 kadraj dışında, sonucu C12'de · T13 tık, nefes, tıslama ve gülüş kurguda | SELA_v1 · BRAM_v1 · KANCA_cantada_v1 · ISTASYON_v1 · DUNYA_alcak_ust_v1 | G01 | ⬜ | — | — | — |
| C12 | Sonuç: ikisi başladıkları kapakta; eve hiç gaz kalmadan döndüler. | Kamera kapağın içinden dışarıya bakıyor. En önde kapak kenarı ve korkuluk; korkulukta Bram'ın ipinin saçaklı kopuk ucu korkuluktan uzanmış, yerinde duruyor; kapağın sıcak ışığı korkuluğa ve uca vuruyor. Sela'nın sağ eldiveni kapak kenarındaki tutamağı çekimin başından kavramış ve kıpırtısız; bileğindeki dört yuvanın dördü de karanlık. Ön kolu kesintisiz biçimde kameradan uzağa, omzuna uzanıyor. Sela kadrajın sol yarısında; sırtı ve kaskının arkası kameraya dönük, turuncu bantlı, kapağın sıcak ışığı sırtına vuruyor. Derinde, sağda, bir ip boyu ötede, daha küçük, sırtı kameraya dönük mavi bantlı Bram, dik, kolları iki yanında; kanca çantasının çerçevesinde, ip Sela'nın belinden ona dümdüz uzanıyor. İkisinin arasında açık boşluk. Kadrajın alt kenarında Dünya'nın ince, parlak ufuk çizgisi; önlerinde, derinde güneş doğuyor ve 0-6 s'de ışık yayılıyor. 6-10 s'de ışık ve iki figür sabit, ikisi de derine bakıyor. | yakın-derin · kapaktan dışarıya · sabit; C01 ile aynı korkuluk ve kopuk uç ilişkisi | Sela solda ve önde; Bram sağda ve derinde (bir ip boyu); ikisi sırttan derine bakar · güneş derinde, ufukta doğuyor · istasyon kamera tarafında (kapak, tutamak, korkuluk) · Dünya altta, yalnız ufuk çizgisi | 10 | Frames to Video | 10 s yolu: P14 · olay 0-6 s (ışığın yayılması) · T01 tutamak teması baştan kurulu ve değişmez; varış anı kadrajda yok, darbe sesi ilk karede kurguda · T01 eldiven, ön kol ve omuz bağı kesintisiz görünür (kopuk el riski) · T08 kopuk uç sarkmaz, rüzgârda oynamaz: korkuluktan uzanmış ve yerinde (teknik B7); ip görünür kalır, bağ olmasa Bram kapağın önünde sebepsiz durur · T15 benzer iki giysi ayrık: Sela önde ve büyük, Bram bir ip boyu derinde ve küçük, aralarında ufuk önünde açık boşluk; bantlar ayrı; yüz ve ağız yok · T05 Bram dik, kollar iki yanında (BRAM_v1), C11 ile aynı · T06 gösterge 0/4 yazısız; kapak içi düz sıcak ışık, yazı ve ekran yok · T09 korkuluk ve kopuk uç C01'in referansından (KAPAK_tek_uc) · T18 ikinci gün doğumu; ışık rengi C08'e eşlenir | SELA_v1 · BRAM_v1 · KAPAK_tek_uc_v1 · BILEK_0-4_v1 · KANCA_cantada_v1 · DUNYA_ikinci_dogus_alt_v1 | G01 | ⬜ | — | — | — |

ZİNCİR ADAYI: yok. Ardışık her çiftte ya ölçek değişiyor (H10) ya da kesme bir durum değişimini saklıyor:
C02/C03 gösterge · C05/C06 dönüş · C06/C07 saat · C09/C10 kancanın kavranması, atış, takılma ve dönüşün durması ·
C10/C11 Bram'ın duruşu · C11/C12 son ışık ve varış. Kesintisiz akış bu bilgileri yutardı. KLIP_SURESI ölçülmedi;
zincir için ≥ 10 s gerekiyor (P14).

## 3. GEREKEN REFERANSLAR — FILM.md §3'e

| Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|---|---|:--:|---|:--:|---|
| Karakter — Sela, yüz + giysi | `SELA_v1.png` | v1 | | ⬜ | C01-C09 · C11 · C12 |
| Karakter — Bram, giysi, vizör opak ve yansıtıcı, temel duruş dik | `BRAM_v1.png` | v1 | | ⬜ | C01 · C08 · C09 · C10 · C11 · C12 |
| Mekân — kapak + korkuluk, iki ip ucu | `KAPAK_iki_uc_v1.png` | v1 | | ⬜ | C01 |
| Mekân — kapak + korkuluk, yalnız kopuk uç | `KAPAK_tek_uc_v1.png` | v1 | | ⬜ | C12 |
| Mekân — istasyon dış | `ISTASYON_v1.png` | v1 | | ⬜ | C01 · C11 |
| Dünya — tam aydınlık, Dünya altta | `DUNYA_gunduz_alt_v1.png` | v1 | | ⬜ | C01-C04 |
| Dünya — alacakaranlık, Dünya altta, aydınlık yay solda | `DUNYA_alacakaranlik_alt_v1.png` | v1 | | ⬜ | C05 · C06 |
| Dünya — gece yüzü, şehir ışıkları | `DUNYA_gece_v1.png` | v1 | | ⬜ | C07 |
| Dünya — gün doğumu, Dünya üstte | `DUNYA_dogus_ust_v1.png` | v1 | | ⬜ | C08 |
| Dünya — loş, Dünya üstte, güneş tarafında ince aydınlık yay | `DUNYA_alcak_ust_v1.png` | v1 | | ⬜ | C09 · C10 · C11 |
| Dünya — ikinci gün doğumu, ufuk çizgisi alt kenarda | `DUNYA_ikinci_dogus_alt_v1.png` | v1 | | ⬜ | C12 |
| Durum — bilek 2 yanan / 2 boş | `BILEK_2-2_v1.png` | v1 | | ⬜ | C03 |
| Durum — bilek 1 yanan / 3 boş | `BILEK_1-3_v1.png` | v1 | | ⬜ | C07 |
| Durum — bilek 0 / 4 | `BILEK_0-4_v1.png` | v1 | | ⬜ | C12 |
| Durum — kanca boşta, ip kısa ve gevşek kıvrımlı | `KANCA_bosta_v1.png` | v1 | | ⬜ | C02 |
| Durum — kanca ezik çanta çerçevesinde, ip tam boy, düz ve gergin | `KANCA_cantada_v1.png` | v1 | | ⬜ | C10 · C11 · C12 |
| Durum — Bram kontrolsüz: uzuvlar nötr yarı açık, çok yavaş dönüyor | `BRAM_kontrolsuz_v1.png` | v1 | | ⬜ | C08 · C09 · C10 (baş) |
| Durum — Bram tek kol kalkık: kontrolsüz duruş + sol kol yana-yukarı (YENİ, teknik B4) | `BRAM_kolkalkik_v1.png` | v1 | | ⬜ | C10 (son) |

```
SHA-256: shasum -a 256 ~/film_medya/THE_WRONG_BURN/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
```

ÇIKTI (tur 2'de vardı, artık yok): `KANCA_yumrukta_v1` (teknik B3 yol a: C09'da kanca yok) · `BRAM_toplanmis_v1`
(teknik B4: yerine C10 sonunda `BRAM_kolkalkik_v1`, C11-C12'de `BRAM_v1` temel duruşu). Tur 1'den beri yok:
`IP_toplanmis_v1` · `BRAM_baygin_v1` · `BRAM_dik_v1`. 18 referans → 18 referans (bir çıktı, bir girdi; biri birleşti:
C11-C12 durumu artık `BRAM_v1`'in kendisi).

**Her referansın taşıması gerekenler (olumlu geometriyle; teknik B9)**
- **SELA_v1:** Kadın, çaylak. Beyaz giysi, iki omzunda turuncu bant. Berrak vizör; kaskın içi karanlık ve sade, yüz
  yalnız dış ışıkla aydınlanır. Göğüste düz, mat, işaretsiz kumanda kutusu. Sağ bilekte yan yana dört yuvarlak yuva
  (durumu BILEK karelerinde). Bel halkasından kısa ip ve kanca, sırtta sırt çantası. Kask ve giysi tek parça.
  Yüz, C05'in yakın ölçeğini taşıyacak netlikte (T16).
- **BRAM_v1:** Erkek. Beyaz giysi, iki omzunda mavi bant. Kaskta kehribar işaret lambası, hep yanık. Vizör opak,
  ayna gibi yansıtıcı. Sırtta yanı ezik, çerçevesi bükülmüş çanta; bükük çerçeve arkadan ve yandan açıkça görünür
  (C09 · C10 · C12). Bel halkası çıplak metal. **Temel duruş:** dik, kollar iki yanında, bacaklar bitişik
  (C01 · C11 · C12).
- **BRAM durumları:** Kask ve giysi tek parça; kask hep gövdeyle aynı yöne bakar.
  - `kontrolsuz`: kollar ve bacaklar mikro yerçekimindeki nötr duruşta yarı açık, eller gevşek ve açık.
  - `kolkalkik`: kontrolsuz karesinin aynısı, tek fark sol kol. Sol kol yana ve yukarıya açık, omuz hizasının biraz
    üstünde, eldiven açık; ip çantadan aşağıya iner, kolla ip arasında açık boşluk.
  - İki kare aynı kamera konumu, ışık ve fonla üretilir. Böylece C10'un başlangıç ve bitiş kareleri arasında tek
    fark kalır.
- **KAPAK kareleri:** İkisi aynı kamera konumundan; C01 ile C12'nin önü aynı. Korkuluk, saçaklı uç ve tutamak düz,
  mat, işaretsiz metal. Saçaklı uç korkuluktan uzanmış, yerinde duruyor. Kapağın içi düz, sıcak, yumuşak ışıkla dolu;
  iç duvarlar sade ve mat.
- **ISTASYON_v1:** Dış yüzey düz, mat, işaretsiz beyaz. Dönen radyatör kolu. Açık kapağın sıcak ışığı (T06; BILINEN §C).
- **DUNYA kareleri:** Her dış çekimde aynı dünya cümlesi (T18). Yıldızlar sönük ve beyaz; renkli tek nokta Bram'ın
  lambası (C08'in doğuş bandı ve kapak ışığı dışında). Güneş açısı çekim başına promptta açık yazılır.
  Bilim-danışmanının tablosu (t, C01 = 0 dk):

  | Çekim | t (dk) | Güneş | Dünya kare |
  |---|:--:|---|---|
  | C01 | 0 | tepede (zenit) | tam aydınlık, altta |
  | C02 | ≈ 2 | yüksek, zenitten ≈ 10° geride | tam aydınlık, altta |
  | C03 | ≈ 6 | zenitten ≈ 30° geride (sol üst) | tam aydınlık, altta |
  | C04 | ≈ 16 | zenitten ≈ 65° geride: solda, yatığa yakın | tam aydınlık, altta |
  | C05 | ≈ 21 | zenitten ≈ 85° geride, yataya yakın (solda arkada) | alacakaranlık |
  | C06 | ≈ 25 | zenitten ≈ 100° geride, Dünya kenarına ≈ 10° kala | alacakaranlık |
  | C07 | ≈ 45 | gece, güneş Dünya'nın arkasında; ay ışığı yok | gece |
  | C08 | ≈ 62 | Dünya kenarında doğuyor, ilerleme yönünde (solda) | doğuş, üstte |
  | C09-C11 | 64-70 | solda, ufka yakın | loş, üstte, ince yay |
  | C12 | ≈ 152 | ikinci doğuş, derinde, ufukta | ufuk çizgisi alt kenarda |

  "Geride" = Sela'nın C02-C05'teki bakış yönünün tersi; ekranda solda.
- **DUNYA_ikinci_dogus_alt_v1:** Işığın rengi ve güneşin boyu DUNYA_dogus_ust_v1 ile aynı. Yalnız yönelim farklı
  (istasyonda Dünya altta).
- **BILEK kareleri:** Sağ bilek. Yan yana dört yuvarlak yuva; yanan yuva soğuk beyaz nokta, boş yuva karanlık;
  yuvaların çevresi düz, mat ve işaretsiz.
- **Prompt metni için (görüntü tarifi değil):** Dosya adlarındaki sayılar ve bütün referans kodları prompt gövdesine
  yazılmaz (BILINEN §C).

```
DURUM SIRASI (sahneleme ve devamlılık)
SELA_kanca     korkulukta C01 · boşta C02 (C03-C09 kadraj dışı; kavrama ve atış C09/C10 kesmesinde) · çantada C10-C12
İP             kısa kıvrım C02 · tam boy, düz, gergin C10-C12 (C10'da sol alt köşeye iner)
BILEK          2/2 C03 · 1/3 C07 · 0/4 C12 · değişim hep kadraj dışında
BRAM           dik, düz sürüklenme C01 · kehribar nokta C02-C07 · siluet, kontrolsüz C08 · kontrolsüz C09-C10 baş ·
               tek kol kalkık C10 son · dik, kollar iki yanında C11-C12 · lamba hep yanık, çanta hep ezik
SELA_yönelim   Dünya altta C01-C05 · atalet kilidi C06-C11 (dönüş C05/C06 kesmesinde)
SELA_kol (C07) başta kumandanın bir avuç önünde → sonda sol kenarda, göğüs hizasında
```

## 5. NOTLAR — Fable ve sahneleme odası için

1. **10 s yolu (P14, sahipte).** Tablo hangi sonuç çıkarsa çıksın üretilebilir: bilgi 0-7 s'de.
   - **(a) Veo 8 s + Lite uzatma** (eklenen süre ve kalite BİLİNMİYOR): Frames to Video 0-8 s klibi üretir, bütün
     olaylar onun içinde biter. Uzatma yalnız "süren hareketi" taşır. **Teknik B6:** her satırda Ekranda görünen
     sütununun son cümlesi ("7-10 s'de …"; C08 ve C12'de "6-10 s'de …") uzatma metnidir. F5'te ayrı satıra taşınır,
     8 s promptuna girmez.
   - **(b) Omni karelerden video 10 s çıkarsa** (P11 · P6): mod sütunu yine Frames to Video; değişiklik yalnız model
     satırında olur, Fable kararı.
   - **(c) Omni Ingredients durum karesini tutmuyorsa:** hiçbir durum çekimi (C03 · C07 · C08 · C09 · C10 · C12)
     Ingredients'a bırakılmaz.
   - Olay bitişleri: C01 6,0 · C02 7,0 · C03 1,6 · C04 7,0 · C05 7,0 · C06 7,0 · C07 4,5 · C08 6,0 · C09 7,0 (en yakın
     nokta 3,5) · C10 4,5 · C11 7,0 · C12 6,0 s. Kurgu her çekimi 7 s'ye kadar kısaltabilir; ama hat kuralı 10 s, bu
     yalnız acil durum yedeği.
2. **F3 KABUL ölçüleri ↔ çekimler:**
   - "ona doğru gitti → üstüne çıktı → geride kaldı": C02'de ışık önünde, göz hizasında büyüyor → C03 2/2 → C04 aynı
     kadraj ilişkisi, ışık ve ufuk aşağı iniyor. Fable: metinde gerekçeyle bırakıldı, F7/F8'de karede sınanır.
   - "ona sırtını dönüyor": C05'te kadrajda yalnız kehribar nokta var. C06'da ışık kadrajın sağ üstünde, başın
     arkasında.
   - "baygındı, ayıldı": C08-C09'da kontrolsüz, yarı açık uzuvlu, yavaş dönen figür. **C10'da dönüş durmuş, sol kol
     yavaşça kalkıyor; nefes ve söz kalkışın içinde.**
   - "S12'nin kapağı S1'in kapağı": C01 ile C12 aynı kadraj ilişkisinde, aynı korkuluk referansıyla.
3. **Sahneleme odasına:**
   - C08'de bitiş karesi zorunlu (iki karede de Dünya üstte).
   - C10'da bitiş karesi önerilir (`BRAM_kolkalkik`). İki kare arasında tek fark sol kol. Kalkış tutmazsa bitiş
     karesi başlangıçla aynı olur ve ayılma seste kalır.
   - Zincir adayı yok.
4. **F4 ses tasarımına (görüntü saniyeleri):**
   - C05: gözler 5,6'da kapanıyor; tutulan nefes burada bırakılır; 6-10 s sessizliği korunur.
   - C07: "Bram?" 1,5'te, elin açılmasından hemen önce; Bram'ın yarım nefesi 3,0'da, açılmanın ortasında.
   - C09: kol hareketi yok, kanca kadrajda yok. Atışın tek izi kesmedeki silkinme sesi (gövdeden, kesmenin 0,2-0,3 s
     önünde). Bu ses artık atışın ekrandaki tek karşılığı; belirgin olmalı.
   - C10: sol kol 2,0-4,5'te kalkıyor, toparlanma soluğu 3,6'da, söz 4,0'da. Üçü aynı hareket olarak okunmalı.
   - C11: tıslama 2,5'te belirgin olmalı (Fable notu, animatik tur 2: metinde ateşleme fark edilmedi).
5. **Tretmandan görüntü sapmaları (FILM §2 yeniden yazılmaz; Fable kaydı için):**
   - S1: kopuk uç "sallanıyor" yerine "korkuluktan uzanmış, çok yavaş kendiliğinden kayıyor" (teknik B7).
   - S4: "gölgeler uzamış" yerine ışığın yönü (soldan, yatık); ek olarak ufkun inmesi (bilim B3, animatik C04).
   - S5: göğsün yükselmesi düştü; gözler ve dönüş öne alındı (teknik tur 1 B1 · B8).
   - S6: "kehribar ışık sağ omzunun üstünde, arkasında" yerine "kadrajın sağ üstünde, başının arkasında". Vücut
     tarafı ekran tarafına çevrildi, anlam aynı: ışık onun arkasında (teknik B1).
   - S7: "ay ışığı" düştü (bilim B5). "El kumandaya gidiyor, yumruk oluyor" yerine "kumandanın bir avuç önündeki el
     yana, gövdeden uzağa açılıyor ve göğüs hizasında, kadrajın içinde duruyor" (teknik tur 1 B4 · tur 2 B5).
   - S8: bant başlangıçta parlak, hareket yalnız güneşin ayrılması (teknik B8). Siluetin duruşu kontrolsüz
     (uzuvlar yarı açık), S9 ile aynı.
   - S9: "kaskı göğsüne düşmüş" yerine kontrolsüz, yavaş dönen figür (bilim B6). "El uzanıyor" yerine el baştan
     uzanmış (teknik tur 1 B2). **"Sağ elinde kanca, kol atış için geriye gidiyor" düştü; kamera Sela'nın sol
     arkasında, kanca ve gösterge kadrajda yok, atış kesmede (teknik B3 yol a).** "Bir gövde boyu" yerine "bir insan
     boyu", Bram'ın yolu düz ve en yakın noktası yolun ortasında (teknik B2).
   - S10: "kaskı göğsünden kalkıyor" ve tur 2'nin "kollarını göğsüne topluyor"u yerine **"sol kolunu yana ve yukarıya
     kaldırıyor"** (bilim B6 · teknik B4). "İki figür ortak merkez çevresinde dönüyor" yerine Bram tekli, kamera ona
     kilitli, fon kayıyor.
   - S11: "istasyon sağ omzunun üstünde" yerine "kadrajın sağ kenarında, Bram'ın ötesinde" (teknik B1 kuralı). Bram
     dik, kolları iki yanında.
   - S12: "iki kask yan yana" yerine önde Sela, bir ip boyu derinde Bram, ip görünür (teknik tur 1 B7). "Dünya kadraj
     dışı" yerine alt kenarda ufuk çizgisi (bilim B4). Kopuk uç "asılı" yerine "korkuluktan uzanmış, yerinde"
     (teknik B7).
   - Hepsi tretmanın niyetini (bedel, ıska, baygın → ayılır, aynı kapak) başka bir görüntüyle taşıyor. Hiçbir
     replik, sahne sırası ya da ekran yönü değişmedi. Tek anlam kaybı S9'daki kanca hazırlığı. C02 (araç) + kesme sesi +
     C10 ilk karesi (sonuç) bunu karşılıyor. Animatik tur 2'de C10 "yakaladı" diye okundu.
6. **Ertelenen seçenek (Fable kararı: F5/F7):** C02'de gösterge 4/4 görünür (durum karesi `BILEK_4-0`), C06'da 2/2.
   İkisi de çekim boyunca sabit, düşüş kesmede. Gerçek karede C03'ün "yanan = kalan" okuması tutmazsa açılır.
   C02 tablosu bugünkü hâliyle kalıyor (gösterge kumanda kutusunun arkasında).
7. **İki kişinin aynı karede olduğu çekimler bilgi gereği var:** C01 · C08 · C09 · C11 · C12. Hepsinde biri küçük ya da
   biri sırttan ve uzakta. C10 tekli. Giysiler hiç değmiyor; tek temas kanca-çanta (C10-C12) ve o da baştan kurulu.
   C09'da iki figür arasındaki en küçük boşluk bir insan boyu.

```
YAPILMADI  film_dogrula.py --bolum cekim koşulmadı (bu ajanda kabuk yok). Tablo betiğin cekim() kurallarına göre
           kuruldu: 12 satır × 14 sütun · süre 10 · mod "Frames to Video" · hücre içinde "|" yok · "Ekranda görünen"de
           ZIHINSEL deseninin kökleri yok (reali[sz]e · notice · decide · understand · remember · feel · want · plan ·
           know · think · fark ed · anlar · anlıyor · karar ver · hatırl · hisseder · düşünür · ister · istiyor ·
           bilir). "plan" sözcüğü tablonun hiçbir hücresinde geçmiyor ("toplanmış" da tablodan çıktı). Elle tarandı,
           regex koşulmadı; FILM.md §4'e taşındıktan sonra Fable koşar.
           B1, B3, B4 ve B5 için sol-sağ geometrisi elle çıkarıldı (ekran ekseninde yön vektörleriyle), Flow'da kare
           denenmedi (FLOW_KREDI 0). C10'daki tek kol kalkışının, C09'daki düz yolun ve yavaş öz dönüşün modelde
           tutup tutmadığı ölçülmedi; üçünün de yedeği satırda yazılı.
           C11-C12'de Bram'ın "dik, kollar iki yanında" duruşu bilim-danışmanına sorulmadı (eleştirmenler kapalı).
           Takımlı giysinin nötr duruşu yarı açıktır; bu duruş kas gücü ister. Görüntüde "bilinçli" okuması için
           seçildi, fizik iddiası değil.
           Bilim-danışmanının güneş açıları elle hesaplanmış değerler, betikle doğrulanmadı (kendi notu).
```
