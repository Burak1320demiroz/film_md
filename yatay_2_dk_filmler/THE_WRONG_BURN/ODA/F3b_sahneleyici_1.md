# 🎭 THE_WRONG_BURN — Sahneleme · sahneleyici · tur 1

```
GİRDİ      FILM.md §1 · §4 (F3_yonetmen_4, 12 × 10 s, 12/12 Frames to Video) · KLIP_SURESI ölçülmedi
           · yönetmen ZİNCİR ADAYI: yok (F3_yonetmen_3 §4 altı) · teslim notu §5.3 (C08 bitiş karesi zorunlu, C10 önerilir)
KARAR      0 zincir. 11 dikişin 11'inde kesme bilgi taşıyor (zaman atlaması · bakış açısı · saklı durum değişimi).
           Bu karar P14'e bağlı değil: KLIP_SURESI ≥ 10 ölçülse de zincir kurulmaz.
EK         C08 ve C10 zincir dışı, iki kareli tek klip (Frames to Video ilk + son kare): bitiş kareleri §2b, delta kontrolü §4b.
           C07 için isteğe bağlı bitiş karesi önerisi (§2b, karar yönetmen + teknik-danisman).
REVİZYON   tur 1, cevaplanacak bulgu yok.
```

---

## 1. ZİNCİRLER

| Zincir | Çekimler | Halka | Yöntem | Neden zincir (kesintisizlik ne anlatıyor) |
|:--:|---|:--:|:--:|---|

**Zincir yok.** Gerekçe:

1. **Bu filmde anlam kesmenin içinde duruyor.** Filmin kuralına göre yörüngede sonuç dakikalar sonra ve ters yönde
   gelir (§1 KURAL). Bunu gösteren şey zaman atlamasıdır: C03/C04 · C06/C07 · C07/C08 · C11/C12. Kesintisiz
   akış, fiziğin "hemen ve doğrudan" işlediğini söylerdi; yani filmin söylediğinin tersini.
2. **Kritik durum değişimlerinin hepsi bilerek kesmeye konmuş** (T01 · T05 · T10):
   - kanca çözülüyor (C01/C02);
   - dönüş tamamlanıyor (C05/C06);
   - kavrama, atış, takılma (C09/C10);
   - Bram'ın kolu iniyor (C10/C11);
   - tutamağa varılıyor (C11/C12).

   Zincir bu anları kadraja geri sokardı. Bunlar da tam olarak bu kanalın kaynaşma, morf ve sebepsiz dönüş ürettiği anlardır.
3. **Ritim kesmeyle kuruluyor (H10).** Ölçek dizisinde arka arkaya iki eş ölçek yok. Zincir aynı objektif ve aynı
   seti gerektirir (delta bütçesi), bu yüzden kurulduğu her yerde bu diziyi düzleştirirdi.
4. **Kesintisizliğin anlam taşıyabileceği tek aday dikişler** C02/C03 (ateşleme kesilmeden sürüyor, titreme C03'e
   taşıyor) ve C08/C09 (yaklaşma ve ıska tek nefeste). İkisi de delta bütçesini aşıyor (§5'te ayrıntı). İkisinde de
   kesme ayrıca bir bilgi taşıyor: C02/C03'te bedeli gösteren insert, C08/C09'da uzanmış kolun kesmede kurulması.
   Bu ikisi aksiyonda kesmedir (match on action), zincir değil.
5. **A′ uygulanamıyor.** A′ halkası 3-6 s'ye kısalır; hat kuralı her çekim 10 s (sahip, 08.10.2026). Bu filmde
   A′'ye gerek doğuran bir dikiş de yok.

## 2. ANAHTAR KARELER

<!-- Yıldız düzeni: her Zk.n, Zk.0 + referanslardan görsel düzenlemeyle üretilir; bir öncekinden DEĞİL.
     Anahtar kare "durağan an"dadır: adım bitmiş, el temastan ayrılmış, kol inmiş — hareket ortası değil. -->
| Kare | Zincir | Poz / konum | Kamera | Işık | Nesne durumu | Kaynak | Dosya (`kare/`) |
|:--:|:--:|---|---|---|---|---|---|

Zincir yok, dolayısıyla Zk kare de yok.

### 2b. Zincir dışı bitiş kareleri: tek klip, Frames to Video ilk + son kare

Bunlar zincir karesi değil, tek klibin ikinci karesi. Klipler arası dikiş yok. Yine de aynı iki kural uygulanır:
- **Durağan an:** her bitiş karesi olayın bittiği yerde durur.
- **Yıldız düzeni:** bitiş karesi kendi çekiminin başlangıç karesinden ve referanslardan düzenlenir.

| Kare | Durum | Poz / konum | Kamera | Işık | Nesne durumu | Kaynak | Dosya (`kare/`) |
|:--:|:--:|---|---|---|---|---|---|
| C08 bitiş | **zorunlu** (teknik F3 B6 · yönetmen §5.3) | Başlangıç karesiyle aynı. Sela küçük, profilden, sola dönük, aynı duruşta. Bram'ın silueti Sela'nın yüzünün tam önünde, aynı hizada, BRAM_kontrolsuz duruşunda (uzuvlar yarı açık). Siluetin boyu başlangıçtakiyle aynı ya da en çok ~%10 büyük (§4b). | Başlangıçla aynı: çok geniş, profil, sabit. Objektif, konum ve yükseklik değişmez. | Tek fark ışık. Güneş Dünya'nın kenarından ayrılmış: kenarla arasında kendi çapı kadar boşluk var. Beyaz ışık yayılmış. Turuncu-mavi bant **soluk ama görünür**, kadrajdan çıkmıyor. Bram güneşe karşı koyu. Kaskında ve omuz hattında ince parlak kenar, kehribar nokta yanık. | **Dünya üstte**, yayın kadrajdaki yeri başlangıçla piksel düzeyinde aynı. Sela'nın ayaklarının altında siyah boşluk. | C08 başlangıç karesi + DUNYA_dogus_ust_v1 (ışık düzenlemesi) | `C08_bitis.png` |
| C10 bitiş | **önerilir** (yönetmen §5.3). Kalkış tutmazsa bitiş karesi = başlangıç karesi ve ayılma seste kalır (tretman §4 yedeği). | Bram kadrajın sağ yarısında, sırtı ve sol yanı ¾. Kontrolsüz duruşun aynısı; tek fark sol kol. Sol kol yana ve yukarı açık, omuz hizasının biraz üstünde, eldiven açık, kıpırtısız (kalkış bitmiş, 4,5 s sonrası). Sağ kol ve bacaklar başlangıçla aynı. | Başlangıçla aynı: orta, Bram tekli, sol arkadan ¾, Bram'a kilitli. | Başlangıçla aynı: güneş solda, ufka yakın. Dünya loş, ince aydınlık yay var. | Kanca ezik çanta çerçevesinde, aynı yerde. İp sol alt köşeye dümdüz ve gergin iniyor; kol ipin yukarısında, arada açık boşluk. **Fon: §4b'deki karara göre ya başlangıçla aynı ya da yazılı yönde birkaç derece kaymış.** | C10 başlangıç karesi + BRAM_kolkalkik_v1 (yalnız sol kol düzenlemesi) | `C10_bitis.png` |
| C07 bitiş | **isteğe bağlı öneri.** Karar yönetmen + teknik-danisman. | Sela'nın yüzü üstte, küçük, sola dönük, gözleri aşağıda (başlangıçla aynı). Sağ eldiven sol kenara yakın, göğüs hizasında, parmaklar başlangıçtaki açık duruşta, kıpırtısız (açılma bitmiş, 4,5 s sonrası). Kumanda kutusuyla temas yok. | Başlangıçla aynı: yakın-orta, önden, hafif üstten, sabit. | Başlangıçla aynı: gece, ay ışığı yok. Yüz yalnız şehir ışıklarının vizördeki yansımasıyla aydınlanıyor. | Bilekte dört yuvadan biri soğuk beyaz yanıyor, üçü karanlık; kadrajda okunur. Kehribar nokta alt kenarın sağ yarısında, başlangıçla aynı yerde. Eldivene sıcak ışık düşmüyor. | C07 başlangıç karesi + BILEK_1-3_v1 (el konumu düzenlemesi) | `C07_bitis.png` |

Notlar:
- **Ölçülmemiş varsayım.** Flow'un bitiş karesini tutup tutmadığı bu depoda ölçülmedi (SMOKE zincir testi madde 1,
  FLOW_GERCEKLERI §9). Bitiş kareleri zincir olmasa da bu teste bağlı.
  - C10 testin (a) durumuna ("küçük poz değişimi") birebir uyuyor. Testin ilk denemesi olarak kullanılabilir.
  - Test sonuçlanmadan C08 ve C10 yalnız başlangıç karesiyle de üretilebilir. Liste bunu yedekleriyle taşıyor (C08:
    başlangıçta Dünya üstte kilitli; C10: kalkış düşerse ayılma seste).
- **P14 yolu (a) seçilirse** (Veo 8 s + Lite uzatma), bitiş karesi 8 s'nin son karesine oturur. Üç çekimde de olay
  8 s'den önce bitiyor (C07 4,5 · C08 6,0 · C10 4,5) ve sonrası durağan. Bitiş karesi uzatmanın da başlangıcı olur.
- **C05 yalnız başlangıç karesiyle kalmalı.** Bitiş karesi iki durum değişimini birden kilitlerdi: gözlerin kapanması
  ve dönüş. Üstelik filmin tek yakın yüz planı burası; morf en çok burada görünür.

## 4. DELTA KONTROLÜ — her halka

| Çekim | Zk.n → Zk.n+1 | Tek ana hareket | Mesafe / süre | Kamera hareketi | Giren/çıkan yok | Temas değişmez | Durum değişimi |
|:--:|:--:|---|---|---|:--:|:--:|---|

Zincir yok, dolayısıyla halka da yok.

### 4b. İki kareli tek klipler: başlangıç → bitiş

| Çekim | Baş. → Bitiş | Tek ana hareket | Mesafe / süre | Kamera hareketi | Giren/çıkan yok | Temas değişmez | Durum değişimi |
|:--:|:--:|---|---|---|:--:|:--:|---|
| C08 | baş. → C08 bitiş | Güneşin kenardan ayrılması ve ışığın yayılması | Güneş ≈ kendi çapı kadar / 0-6 s · siluet 0 ile ~%10 büyüme / 0-6 s | yok | ✅ (bant soluyor ama iki karede de var) | ✅ (temas yok) | ⚠ **Işık değişimi tek ve bilerek yapılıyor.** "Aynı ışık" maddesinin tek istisnası; bilginin kendisi bu. Siluetin büyümesi ikinci bir delta: ~%10'u geçerse ya da morf görülürse iki karede aynı boy yapılır. Bilgi kalır, çünkü Bram yine önünde. |
| C10 | baş. → C10 bitiş | Sol kolun yana ve yukarı kalkışı | El yolu ≈ 0,6-0,7 m / 2,5 s (2,0-4,5): ulaşılabilir | ⚠ **"Fon birkaç derece kayar"** (kamera Bram'a kilitli). Tek basit kamera hareketi sayılır, bütçe içinde. Ama yönü yazılı değil (bkz. not). | ✅ | ✅ (kanca-çanta sabit; eller ipe ve kancaya değmiyor) | Tek: sol kol |
| C07 (öneri) | baş. → C07 bitiş | Elin kumandadan yana, sol kenara açılması | El yolu ≈ 0,4-0,5 m / 2,5 s (2,0-4,5): ulaşılabilir | yok | ✅ | ✅ (iki karede de temas yok) | Tek: el konumu. Gösterge iki karede de 1/3. |

**C10 fon notu (yönetmen ve mekan-haritacisi için; liste değişikliği değil, karar sizin).** Referans tarifi ile
§4 metni çelişiyor:
- F3_yonetmen_3 §3 BRAM durumları: "iki kare aynı kamera konumu, ışık ve fonla üretilir";
- §4 Ekranda görünen: "fon çekim boyunca birkaç derece kayıyor".

İki kare aynı fonla verilirse model kaymayı ya üretmez ya da kaydırıp geri getirir. Geri getirmesi gizli kesme ya da
yüzme gibi okunur (T04 · T07). İki çıkış var:
- **(i) Önerim: fon kaymasını düşür.** İki kare aynı fonla üretilir. Çekimin tek bilgisi "Bram ayılıyor: kolunu
  kaldırıyor"; kayma bu bilgiye bir şey katmıyor ve kolla birlikte ikinci bir delta açıyor. Dönüşün durduğunu zaten
  C09'daki yavaş dönüşle yan yana gelmek söylüyor.
- **(ii) Kayma kalacaksa** bitiş karesinde fon aynı yönde birkaç derece kaydırılmış üretilir ve yön ekran terimiyle
  yazılır. Örnek: "Dünya'nın yayı kadrajda biraz aşağı/sağa iner". Şu anki metin yön vermiyor (T11).

## 5. ZİNCİR DIŞI ÇEKİMLER

Saatler bilim-danışmanının tablosundan (F3_yonetmen_3 §3, t: C01 = 0 dk).

| Çekim | Neden zincir değil |
|:--:|---|
| C01 | Kuruluş planı: sorun, sebep ve ev aynı karede (H08). **C01/C02 kesmesi** ≈ 2 dk'lık bir zaman atlaması taşıyor ve kancanın korkuluktan çözülmesini saklıyor (T01 temas anı · T05 durum karesi KANCA_bosta). Zincir için kancanın çözülmesi kadraja girmeliydi. Geniş → orta profil ölçek geçişi de objektif değiştiriyor. |
| C02 | **C02/C03 kesmesi bakış açısı değişimi**: profilden bilek insert'ine geçiliyor ve bedel tam o anda açığa çıkıyor. Gösterge C02'de kumanda kutusunun arkasında, okunmuyor. Bedeli izleyicinin önüne koyan şey insert'in kendisi. Kesintisizlik burada bir anlam taşıyabilirdi (ateşleme kesilmeden sürüyor, titreme C03'e taşıyor), ama bunu aksiyonda kesme (titremeden titremeye) zaten veriyor. Zincir delta bütçesini aşardı: orta profilden bilek insert'ine geçmek hem objektif değişimi hem de iki eksenli kamera yolu (itme + açı değişimi) ister. Bilek kumanda kutusunun arkasından kadraja girmek zorunda kalırdı. El-kumanda teması kadrajın içinde değişirdi (T01). |
| C03 | **C03/C04 kesmesi zaman atlaması** (≈ 10 dk; güneş zenitten ≈ 30°'den ≈ 65°'ye iniyor). Filmin kuralı bu boşlukta görünür: ters sonuç dakikalar sonra gelir. Kesintisiz akış sonucun hemen geldiğini söylerdi. Bu da kurala aykırı olurdu. Işık ve set değiştiği için bütçe de baştan aşılıyor. |
| C04 | **C04/C05 kesmesi bakış açısı değişimi ve ritim kırılması.** Kamera sağ arka ¾ orta-genişten ¾ ön yakına, Bram'ın sesinden Sela'nın yüzüne geçiyor. Takasın tepkisini ilk kez yüzde görüyoruz (T12: yakın plan yalnız tepki anında). Bu geçiş için kamera Sela'nın çevresinde ≈ 135° dönmeli ve ölçek iki basamak değişmeli. Bunlar iki kamera hareketi ve objektif değişimi demek. Arada ≈ 5 dk var; ışık gündüzden alacakaranlığa geçiyor. |
| C05 | **C05/C06 kesmesi saklı bir durum değişimi taşıyor:** dönüşün kalanı (T10, F1 B2). Kararın dramatik biçimi bu kesme: gözler kapalı, yarım dönüş → kesme → dönmüş ve ateşliyor. İzleyici dönüşün tamamlandığını görmez, sonucunu görür. Zincir vakumda gövdenin tam dönüşünü kadrajda isterdi (sebepsiz dönüş, kask-gövde ayrışması riski, T05/T10). Arada ≈ 4 dk ve ışık değişimi var (güneş ≈ 85°'den ≈ 100°'ye; C06'da vizöre parlama vuruyor). |
| C06 | **C06/C07 kesmesi zaman atlaması** (≈ 20 dk, alacakaranlıktan geceye). Frenin sonucu, Bram'ın gözle görülür biçimde uzaklaşması, ancak bu boşluktan sonra okunuyor. Işık rejimi tümden değişiyor; bütçe tanım gereği aşılıyor. |
| C07 | **C07/C08 kesmesi zaman atlaması** (≈ 17 dk, geceden gün doğumuna) ve ödülün açılışı. Sela dönmediği hâlde Dünya alttan üste geçiyor. Bilgi "dünya yer değiştirdi" ve bu yalnız kesmenin üstünden okunur. Kesintisiz akışta Dünya'nın kadrajda dönmesi gerekirdi: kamera kayması gibi okunurdu (T07) ve ses ile görüntü sözünü erken bozardı. Gece sessizliğinin (hışırtı) gün doğumuyla kesilmesi de bir ritim kırılması. |
| C08 | **C08/C09 kesmesi bakış açısı değişimi ve saklı durum değişimi.** Çok geniş profilden omuz üstü ¾ sol arkaya geçiliyor; ışık doğuştan loşa dönüyor (≈ 2 dk). Sela'nın sol kolunun uzanması kesmede, çünkü T01/T15 uzanma hareketi kadrajda yok. Kesintisizlik burada da anlam taşıyabilirdi: yaklaşma ve ıska tek nefeste. Ama zincir için kamera "çok geniş"ten "omuz üstü"ne gitmeli, Bram derinden eldivenin iki insan boyu ötesine kadar gelmeli ve kol kadrajda uzanmalı. Bu üç delta eder; morf kesin. Gerilimi zincir değil, C09'un kendi içindeki en yakın nokta (~3,5 s) taşıyor. |
| C09 | **C09/C10 kesmesi saklı bir durum değişimi taşıyor:** kancanın kavranması, atış, takılma, silkinme, dönüşün durması (T01, F3 yönetmen kararı 2). Atışın ekrandaki tek karşılığı kesmenin 0,2-0,3 s önündeki silkinme sesi. Bakış açısı da Sela'dan Bram tekliye geçiyor. Zincir, filmin en riskli el-nesne temasını kadrajın ortasına koyardı. |
| C10 | **C10/C11 kesmesi saklı durum değişimi ve ölçek değişimi.** Bram'ın kolu iniyor ve dik duruşa geçiyor (T05; durum sırası: tek kol kalkık → dik). Orta tekliden geniş ikiliye geçiliyor. İstasyon ve Sela kadraja giriyor; delta bütçesi bunu yasaklar: kadraja nesne ya da kişi girip çıkmaz. |
| C11 | **C11/C12 kesmesi zaman atlaması** (≈ 80 dk, ikinci gün doğumu). Son ışıktan sonra eve hiç pay kalmadan varılıyor ve tutamak teması kesmede kuruluyor (T01). Göstergenin 1'den 0'a inişi kadraj dışında kalıyor. Filmin kuralı ikinci kez bu boşlukta işliyor: istasyondan uzağa yak, sonra istasyonda ol. |
| C12 | Final. Çıkış dikişi yok. Giriş dikişi (C11/C12) yukarıda: zaman atlaması. C01 ile aynı kadraj ilişkisi zincirle değil, ayna kuruluşla bağlanıyor (aynı korkuluk, aynı kopuk uç, KAPAK referansları). |

**Okuma notları (değişiklik önerisi değil):**
- **Replik dikişleri.** Zincir olmadığı için hiçbir replik dikişin üstünden geçmiyor. En geç biten replik C04'teki 7.
  replik (6,2 + 2,8 = 9,0 s); çekimin içinde kalıyor.
- **H01 kuyrukları.** Her çekimin 7-10 s (C08 ve C12'de 6-10 s) kısmı bilinçli olarak "süren hareket" taşıyor (F3
  kararı 1, teknik B6). Bu H01 · H10 riskidir; ama zincirle çözülmez. Zincir bu kuyrukları bir sonraki çekime
  bağlayıp uzatırdı.
  - Riskin kapanma yeri kurgu ve ses (F4 · F8): C05'te sessizlik, C07'de hışırtı, C10'da nefes ve söz, C12'de nefes.
  - Kurgunun 7 s'ye kısaltma yedeği hat kuralı gereği yalnız acil durum içindir.

---

## §4 SÜTUNLARI

`FILM.md` §4'ün `Zincir · Baş. karesi · Bitiş karesi` sütunlarına (ana ajan kopyalar):

| çekim | Zincir | Baş. karesi | Bitiş karesi |
|:--:|:--:|:--:|:--:|
| C01 | — | — | — |
| C02 | — | — | — |
| C03 | — | — | — |
| C04 | — | — | — |
| C05 | — | — | — |
| C06 | — | — | — |
| C07 | — | — | — |
| C08 | — | — | — |
| C09 | — | — | — |
| C10 | — | — | — |
| C11 | — | — | — |
| C12 | — | — | — |

C08 ve C10'un (ve önerilirse C07'nin) bitiş kareleri bu sütunlara yazılmadı. Sütun zincirin sözleşmesi; zincir dışı
çekimde "—" kalır. Bu kareler §2b'de tarif edildi ve F5'te `goruntu-yonetmeni` iş emrine (Flow iş emri, EKLE satırı)
oradan geçer. `film_dogrula.py` zincirsiz çekimde bu sütunları okumuyor (`sahneleme()` zincir yoksa döner). Fable
sütunda görmek isterse kare dosya adı (`C08_bitis` · `C10_bitis`) yazılabilir; denetimi bozmaz.
