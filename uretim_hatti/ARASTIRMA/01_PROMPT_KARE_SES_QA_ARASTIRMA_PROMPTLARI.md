# 🔬 01 — PROMPT · KARE · SES · QA · BEŞ DERİN ARAŞTIRMA PROMPTU (06.10.2026)

> **Durum:** ✅ KOŞULDU — 06.10.2026. Ham: `ham/01…05_*_HAM.md` · süzme: `02_SUZME_20261006.md` (16 kaynak doğrulandı; indirmeler sahip onayı bekliyor).
> **Neden:** 12 filmin ham QA'sı (yaklaşık 300 rapor, 698 tekil bulgu) sahne sahne promptlarla karşılaştırıldı:
> - gerçek kusurların %56'sı promptta doğuyor;
> - bulguların %31'i QA yanılgısı.
>
> Kapatılabilen kısmı `film_dogrula.py` ve ajan kurallarına girdi (06.10.2026). Bu beş prompt kalan soruları sorar: kodla kapanmayan ya da yeni hattın henüz hiç denemediği konular.
>
> **Nasıl koşulur:** her prompt **tek başına** çalışır. Kod bloğunu kopyala, derin araştırma aracına yapıştır, başka hiçbir şey verme: bu depo, film adları ve raporlar verilmez. Araç depoyu görürse deponun dilini tekrar eder, dışarıdan bilgi getirmez. Eski hattın TUR 22 ve TUR 24 kuralı da buydu.
>
> **Sıra:** bağımsız. ⭐ 1 numara, Flow zincir testinden (`../SMOKE_TEST.md`) **önce** koşulursa testi daha ucuza kurar.

| # | konu | kapattığı yer |
|:--:|---|---|
| 1 | **BAŞLANGIÇ + BİTİŞ KARESİ** — Flow'da iki kare arası üretim ve zincir | `SAHNELEME.md` · sahneleme-odasi · zincir-bekcisi · SMOKE_TEST zincir bölümü |
| 2 | **TEK PROMPTUN OKUNUŞU** — çelişki, olumsuz cümle, etiket, atıf, uzunluk | goruntu-yonetmeni · `film_dogrula.py` |
| 3 | **BAŞLANGIÇ KARESİ TASARIMI** — görselden videoya devir | goruntu-yonetmeni · devamlilik · teknik-danisman |
| 4 | **İSTENMEYEN KONUŞMA + KURGUDA SES** — model sesi ve uzay ses tasarımı | ses-tasarimcisi · kurgucu · `kurgu.py` |
| 5 | **GEMINI İLE VİDEO QA'NIN GÜVENİLİRLİĞİ** | `QA_PROMPTLARI/TARAMA.md` · `ANLATIM_TESTI.md` · klip-sec |

> **Zaten yazılı, koşulmamış bir dosya var:** `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/24_NANO_BANANA_2_GORSEL_URETIM_ARASTIRMA_PROMPTLARI.md` (4 prompt). Görsel modelin kendisini soruyor: kimlik, jeton sızıntısı, düzenleme. Anahtar kare zinciri görsel düzenlemeyle kurulduğu için o dosya da koşulmaya değer. Burada aynı soru yeniden sorulmadı; 3 numara yalnız görselden videoya **devri** sorar.

---

# 1️⃣ BAŞLANGIÇ + BİTİŞ KARESİ — iki kare arasında ne üretilir, zincir nerede kopar

```
Google Flow'daki güncel Veo sürümünün (Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası; karşılaştırma için Kling, Runway, Luma, Hailuo, Wan ve Sora'nın ilk-son kare modları) "başlangıç karesi + bitiş karesi" verilerek video üretme özelliğini araştır: hangi modelde ve hangi Flow modunda (Frames to Video, Ingredients to Video) iki kare birlikte kabul ediliyor, üretilen klibin süresi, kare hızı, çözünürlüğü ve en-boy oranı ne, iki karenin çözünürlük ya da en-boy oranı farklıysa ne oluyor, kredi maliyeti ne — resmî belge, sürüm notu, model kartı, yöntemi yazılı bağımsız test ve uygulayıcı raporlarıyla; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: model iki kare arasını nasıl dolduruyor (gerçek hareket mi üretiyor, yoksa iki görüntüyü birbirine eritip "morf" mu yapıyor), hangi tür farkta morfa geçiyor (küçük poz değişimi, öznenin bir metre yer değiştirmesi, kameranın %20 yaklaşması, kadraja yeni bir kişi ya da nesne girmesi, ışık ya da renk değişimi, el ile nesne arasındaki temasın değişmesi), bitiş karesine erken varıp son saniyelerde donma ya da geri sarılma davranışı var mı, ara karelerde kimlik (yüz, giysi, kask) kayması nerede başlıyor, video promptunun iki kare arasındaki hareketi ne kadar yönlendirebildiği — tutan ve çöken vakalar birlikte.
Zinciri ayrıca sor: bir klibin son karesini dışa alıp sonraki klibin başlangıç karesi yapmanın (gerçek son kare zinciri) her halkada sıkıştırma, renk ve kimlik kaybı biriktirip biriktirmediği, kaç halkadan sonra kaymanın gözle görülür olduğuna dair ölçüm, bunun yerine bütün anahtar kareleri önceden görsel modelle tek bir ana kareden düzenleyerek üretmenin (her anahtar kare aynı ana kare + referanslardan, bir öncekinden değil) kaymayı önleyip önlemediği, son kare yerine klibin ortasından seçilmiş bir karenin kullanılması ve dışa alınan karenin görsel modelle referansa göre tazelenmesinin belgelenmiş sonuçları, dikişte (bir klibin sonu ile sonrakinin başı) hareket hızı ve kamera hareketi sürekliliğinin nasıl korunduğu.
Pratik tarafı topla: ilk-son kare modunu kullanan yapay zekâ film ekiplerinin anahtar kare hazırlama yöntemleri (aynı objektif, aynı ışık, "durağan an" seçimi, iki kare arasına tek bir hareket koyma), dikişi gizlemek için kullanılan kurgu teknikleri (birkaç kare kırpma, dikişi bir kesmeyle değiştirme, ses köprüsü), dikişin görünür olup olmadığını ölçmek için kullanılan nesnel yöntemler (SSIM, PSNR, optik akış sıçraması, fark görüntüsü) ve bunların göz kararıyla ne kadar örtüştüğü, kaç denemede bir kullanılabilir halka çıktığına dair sayısal veri.
Kritik kısıt: kullanım yeri, Google Flow web arayüzünde üretilen, aracın verdiği sabit süreli (8 ya da 10 saniye) fotogerçekçi uzay bilimkurgu klipleridir; karakter basınç giysili ve kasklıdır; bir filmde en çok iki-üç zincir ve zincir başına en çok dört halka vardır; anahtar kareler aynı araçtaki görsel modelle üretilip düzenlenir; video promptu tek İngilizce metindir ve "previous clip / last frame" gibi zincir dili promptta kullanılmaz, kareler arayüzden eklenir; VFX kompozit, rotoskop, kare kare rötuş, optik akışla ara kare üretimi ve hız rampası YOKTUR, yalnız kesme, kırpma ve ses miksi vardır — bu yüzden bu araçları öneren çözümleri "hat dışı" diye işaretle ama silme, arayüz ve kurgu ile uygulanabilir olanları öne al.
Çıktıyı dört tablo ve iki liste olarak ver: (a) YETENEK tablosu — model, sürüm, Flow modu, iki kare kabulü, süre, kare hızı, çözünürlük, en-boy, kredi, kaynak ve etiket; (b) DELTA tablosu — iki kare arasındaki fark türü, morf riski (düşük/orta/yüksek), belirtisi, önleyen anahtar kare kararı, kaynak ve etiket; (c) ZİNCİR tablosu — yöntem (gerçek son kare, seçilmiş ara kare, tazelenmiş kare, önceden üretilmiş anahtar kareler), halka başına kayma, kopma noktası, kaynak ve etiket; (d) DİKİŞ tablosu — ölçüm yöntemi, eşik değer varsa değeri, göz kararıyla uyumu, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bunları açıklamalı

```
DEPONUN TASARIMI (05.10.2026, test edilmedi):
  B (varsayılan)  anahtar kare zinciri, yıldız düzeni: her Zk.n = Zk.0 + referanslardan görsel düzenleme
  A / A′ / A+     gerçek son kare · seçilmiş çıkış karesi (halka 3-6 sn) · referansla tazelenmiş kare
  delta bütçesi   aynı objektif/ışık/set · en çok bir basit kamera hareketi · kadraja giren-çıkan yok ·
                  el-nesne teması değişmez · durum değişimi küçük ve tek
  ölçüm           kareler.py dikis: sentetik testte doğru dikiş SSIM 0,91 · yanlış 0,33 — gerçek klipte
                  hangi değerin "görünür sıçrama" olduğu BİLİNMİYOR

GEÇMİŞ:
  22.09.2026  zincir prompt DİLİYLE kuruluyordu ("continues the previous clip from its exact last frame")
              ve kaldırıldı. Dil sonradan bile promptlarda kaldı: THE_STILL_POINT · THE_LISTENING_WORLD ·
              THE_SLOW_RAIN'de aynı promptta hem "START FRAME: the approved still" hem "continues the
              previous clip" — iki zıt başlangıç emri.

CEVAPTAN BEKLENEN: delta bütçesinin hangi satırı ölçümle destekleniyor, hangisi hipotez; morfun
eşiği nerede; B'nin A'ya üstünlüğü belgelenmiş mi; SMOKE_TEST'in 4 çiftlik denemesi doğru soruyu mu soruyor.
```

---

# 2️⃣ TEK PROMPTUN OKUNUŞU — model çelişkiyi, olumsuz cümleyi, etiketi ve atfı nasıl okuyor

```
Google Flow'daki güncel Veo sürümünün (Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası; karşılaştırma için aynı araçtaki görsel model ve Kling, Runway, Luma, Sora) metin promptunu nasıl yorumladığını araştır: Flow'un ya da modelin promptu kullanıcıya göstermeden yeniden yazıp yazmadığı (prompt genişletme, "enhance" özelliği, güvenlik yeniden yazımı), metin kodlayıcının bir promptta kaç ayrı talimatı güvenle taşıyabildiği, prompt uzunluğu ile talimata uyum arasındaki ölçülmüş ilişki ve bir üst sınırdan sonra talimatların düşmesi, cümle sırasının (baştaki ve sondaki cümlenin) ağırlığı — resmî prompt kılavuzları, model kartları, hakemli çalışmalar (metinden videoya uyum, olumsuzlama anlama, bileşik talimat değerlendirmesi) ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: aynı promptta birbiriyle çelişen iki istek olduğunda (örneğin "yüz vizörün ardından okunuyor" ile "yakanın üstünde çıplak deri yok", "kalkan toz hiç yere inmez" ile "hiçbir şey havada asılı kalmaz", "tek ışık kaynağı" ile "yüze sıcak dolgu ışığı") modelin hangi tarafı seçtiği ya da ikisini karıştırıp karıştırmadığı, olumsuz cümlelerin ("no X, no Y, no Z") yasakladığı kavramı tersine çağırıp çağırmadığı, her prompta kopyalanan uzun bir olumsuz bloğun (promptun %40'ı) uyumu artırıp azalttığı, "CAMERA:", "PHYSICS:", "AUDIO:" gibi alan başlıklarının ve "Scene 7 of 12" gibi sıra numaralarının modele ne ifade ettiği, modelin göremeyeceği şeylere yapılan atıfların ("the same lens as Scene 3", "for the whole film", "as before") nasıl işlendiği — iki yönlü, tutan ve çöken vakalar birlikte.
Görüntüye basılan yazıyı ayrıca sor: promptta geçen hangi kelimelerin kadraja harf olarak basıldığı (büyük harfli kısaltmalar, özel adlar, sık tekrar eden ayırt edici bir kelime, düğme ya da etiket çağrıştıran fiiller, sıra numaraları), bir kelimenin tekrar sayısının bu riski artırıp artırmadığı, kadrajda ekran, kadran, harita ya da amblem istenirken "yazı yok" denmesinin sonucu, yazının metinsiz çözülmesinin (ışıklı çubuk, dolu yuva, renk değişimi) belgelenmiş etkisi.
Yazım standardını topla: soyut ya da zihinsel ifadelerin ("she realizes", "nod of comprehension", "registers something off-frame"), ölçülemeyecek kadar küçük sayısal hareketlerin ("her head turns one degree"), on saniye içinde zaman damgalı alt eylem dizilerinin (0.0s–3.5s …) ve kesin sayıların (mesafe, açı, yerçekimi değeri, ağırlık) modelde karşılığı olup olmadığı; pozitif, tek anlamlı ve kısa yazmanın uzun kural listesine göre ölçülmüş farkı; görüntüden videoya üretimde ilk karede zaten olanı video promptunda yeniden tarif etmenin etkisi.
Kritik kısıt: kullanım yeri, Google Flow'da tek İngilizce promptla üretilen, 8-10 saniyelik, kesmesiz, fotogerçekçi uzay bilimkurgu klipleridir; her klip ayrı üretilir ve model başka klipleri, filmin planını ya da önceki promptları görmez; karakter basınç giysili ve kasklıdır; ses modelden alınmaz, kurguda kurulur; VFX ve rötuş YOKTUR — bu yüzden ince ayar (fine-tuning), LoRA, API parametresi ya da özel kodlayıcı gerektiren çözümleri "hat dışı" diye işaretle ama silme, yalnız prompt metniyle uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) OKUNUŞ tablosu — prompt özelliği (çelişki, olumsuz cümle, uzun olumsuz blok, alan başlığı, sıra numarası, görünmeyen şeye atıf, soyut fiil, mikro sayı, zaman damgası, kesin sayı, tekrar eden kelime), modelin davranışı, ölçülmüş etkisi varsa sayısı, model ve sürüm, kaynak ve etiket; (b) YAZI SIZINTISI tablosu — tetikleyen kelime türü, örnek, risk, önleyen yazım, kaynak ve etiket; (c) YAZIM KURALI tablosu — kural, İngilizce doğru ve yanlış örnek, kanıt, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
ÇELİŞKİ → KUSUR (06.10.2026 analizi):
  "Dust lifts and never settles" + NEGATIVE "never hovering"  THE_BRITTLE_EDGE 24/24 · THE_LAST_TOW 48/48 promptta
                                                              → asılı toz bulguları. Cümle eski şablondan geliyor:
                                                              PROMPT_HATA_ONLEME_KILAVUZU satır 98 · 181
  "real skin pores and sweat" + "No bare skin"                19 film · 784 prompt (eski NEGATIVE çekirdeği)
  "warm 3200K fill on her face" + "there is no fill at all"   THE_LAST_TOW K07 K11 K17 K28 K40
OLUMSUZ BLOK      ortanca prompt payı %40 (50 film · 2.913 prompt) · eski TUR 22 ölçümü: temas cümlesi VARKEN
                  arıza %11,8 · YOKKEN %5,6 (RR 2,10) — "olumsuzlama kavramı çağırıyor" hipotezini destekliyor
UZUNLUK           prompt uzunluğu ↔ hata Spearman +0,26 (zayıf); uzatmak düzeltmedi
YAZI SIZINTISI    PHASE 1 · EVA · rose (139×) · S04 · ORION · SELECTOR · "release" 132× → "SUIT RELEASE / 500"
                  (THE_LAST_GATE K30) · başlık kartı (post) ≠ sızıntı
ATIF              "the same position, height and lens as Clip 5" 45 filmde; 0/1 tabanlı numaralar karışınca
                  yanlış kamera (THE_INWARD_FALL K19 · THE_STATIC_VEIL S8) — model zaten göremiyor
YENİ HAT KARARI   olumsuz blok yazılmaz · alan başlığı ve sıra numarası yazılmaz · video 1-3 cümle ·
                  ≤4.300 karakter (Veo hata eşiği) — cevap bu kararları destekliyor mu, çürütüyor mu?
```

---

# 3️⃣ BAŞLANGIÇ KARESİ TASARIMI — görselden videoya devirde kare neyi taşımalı

```
Google Flow'daki görüntüden videoya üretimde (güncel Veo sürümü, Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası; başlangıç karesi aynı araçtaki görsel modelle — Imagen ya da Gemini görsel modeli / "Nano Banana" — üretilir; karşılaştırma için Kling, Runway, Luma) başlangıç karesinin videoyu ne kadar ve nasıl kısıtladığını araştır: kimlik (yüz, giysi, kask), poz, kamera konumu, ışık yönü ve sahne düzeninin kareden videoya ne oranda taşındığı, video promptu kareyle çeliştiğinde hangisinin kazandığı, "Frames to Video" ile "Ingredients to Video" (referans görsellerle üretim) arasındaki fark ve hangi işte hangisinin seçilmesi gerektiği — resmî belge, model kartı, hakemli çalışma ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: başlangıç karesi bir eylemin bitmiş hâlini gösterdiğinde (kablo kesilmiş, kapak açılmış, araç hedefe varmış) modelin hareketi atlayıp atlamadığı, geri sarıp sarmadığı ya da donup donmadığı; karede tutuş ya da poz video promptunun istediği ilk eylemden farklıysa (karede kavrama, promptta dokunma) ne olduğu; kadrajda yalnız eller ya da gövdenin bir parçası varken modelin bedenin geri kalanını nasıl tamamladığı ve havada asılı eldiven, kolsuz el, tutanı olmayan nesne gibi arızaların tetikleyicisi; karede var olan küçük bir yazı, logo ya da kusurun videoda büyüyüp büyümediği.
Durağan anı ayrıca sor: hareketin başına yerleştirilecek "durağan an"ın (adım bitmiş, el temastan hemen önce ya da sonra, ağırlık dengede) nasıl seçildiği, temas noktasının karede görünür olmasının temas arızalarını azaltıp azaltmadığı, eylemin hangi evresinde başlayan karenin en temiz hareketi verdiği, kamera hareketi istenen klipte başlangıç karesinin kadrajının nasıl ayarlandığı (hareketin varacağı alan için boşluk bırakma).
Pratik tarafı topla: görsel promptun ve video promptunun iş bölümü (karede olanın video promptunda yeniden tarif edilmesinin etkisi), kareyi seçmeden önce yapılan kontroller (el sayısı, parmak, kask, yazı, ışık yönü, en-boy oranı ve çözünürlüğün video çıktısıyla aynı olması), aynı kareden birkaç video denemesi almanın ya da kareyi yeniden üretmenin hangisinin daha ucuz olduğuna dair veri, referans görsellerin (karakter sayfası, giysi sayfası) kimlik tutarlılığına ölçülmüş katkısı.
Kritik kısıt: kullanım yeri, Google Flow'da üretilen, 8-10 saniyelik, kesmesiz, fotogerçekçi uzay bilimkurgu klipleridir; karakter basınç giysili ve kasklıdır, eldivenle elle iş yapar (vana, kayış, karabina, kol, kablo); her klip ayrı üretilir ve kurguda kesilir; bir başlangıç karesi bir kez onaylanır ve o çekimin bütün denemelerinde kullanılır; VFX kompozit, maske, rotoskop ve rötuş YOKTUR, yalnız kesme ve ses miksi vardır — bu yüzden bu araçları öneren çözümleri "hat dışı" diye işaretle ama silme, kare seçimi ve prompt ile uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) DEVİR tablosu — karedeki öğe (kimlik, poz, kamera, ışık, sahne düzeni, yazı/kusur), videoya taşınma derecesi, kareyle prompt çeliştiğinde kazanan, model ve sürüm, kaynak ve etiket; (b) KARE KARARI tablosu — durum (eylemin bitmiş hâli, farklı tutuş, yalnız eller, tutulan nesne, kamera hareketi), arıza, doğru kare kararı, İngilizce görsel prompt kalıbı, kaynak ve etiket; (c) KONTROL LİSTESİ — kareyi onaylamadan önce bakılacak maddeler, her birinin hangi arızayı önlediği ve kanıtı, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
BİTMİŞ HÂL / FARKLI EYLEM (06.10.2026):
  THE_BRITTLE_EDGE S10   görsel "rests securely on the level terrace" ↔ video "rear wheels crest the lip"
                         → "çekme anı atlandı" 🔴
  THE_INWARD_FALL K19    "has severed the safety line completely" ↔ 0.0 s "blades bite into the jacket"
  THE_STILL_POINT S00    görsel "reaches forward toward a bracket" ↔ video "pulls backward toward the torso"
  THE_LISTENING_WORLD S5 görsel "grips the knurled knob" ↔ video "index finger taps the trigger four times"
YALNIZ ELLER / TUTANSIZ NESNE:
  THE_STOLEN_SKY S82     "The cobalt glove hangs a finger above the T-handle", gövde bağı yok → havada eldiven + kask 🔴 (3 mercek)
  THE_SIGNAL_KEEPERS K23 küre "held above" ama tutan yazılı değil → "hayali kavrama" 🔴
  THE_COUNTED_RIVET K13  IN FRAME: hands + "she leans back into it"
TEMAS (eski TUR 22): temas cümlesi yazılıyken de füzyon (THE_COUNTED_TURN 22/25 → 7 🔴) — çözüm kadraj kararı
YENİ HAT KURALI (06.10.2026): görsel = hareketin BAŞINDAKİ durağan an · tutanı kadrajda · kolun girdiği kenar yazılı.
CEVAPTAN BEKLENEN: bu kurallar ölçümle destekleniyor mu; "durağan an" nasıl seçilir; Frames ↔ Ingredients seçimi.
```

---

# 4️⃣ İSTENMEYEN KONUŞMA + KURGUDA SES — model sesi neden konuşuyor, uzay sesi kurguda nasıl kurulur

```
Google Flow'daki güncel Veo sürümünün (Veo 3.1 ve Ekim 2026 itibarıyla varsa sonrası) yerleşik ses üretimini araştır: ses üretiminin Flow'da kapatılıp kapatılamadığı, promptta istenmediği hâlde konuşma, mırıldanma, telsiz cümlesi ya da uydurma bir ad üretme davranışı, "No dialogue" gibi bir cümlenin bunu ölçülebilir biçimde önleyip önlemediği, promptta bir sesin tarif edilmesinin ("a voice over the radio", "she names her sister", "a radio channel opening on static") konuşma üretimini tetikleyip tetiklemediği, ses tarifinin GÖRÜNTÜYÜ de değiştirip değiştirmediği (ağız ve çene hareketi, kapalı kask içinde dudak oynaması, nefes buharı, konuşur gibi baş hareketi), vakumda ses gibi fiziğe aykırı seslerin hangi koşulda üretildiği — resmî belge, model kartı ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: ses ve görüntünün ortak mı ayrı mı üretildiği ve bunun sessiz bir klip istemeye etkisi, sessiz üretimin (ya da sesi sonradan atmanın) görüntüdeki konuşma izlerini temizleyip temizlemediği, kask içi ve opak vizörlü karakterde konuşma izinin nasıl göründüğü, dudak senkronu istenmeyen bir klipte ağız hareketini önlemenin belgelenmiş yolları (kadraj, kask, opak vizör, sırt çekimi, prompt yazımı) — iki yönlü, tutan ve çöken vakalar birlikte.
Kurgu tarafını ayrıca sor: model sesi tamamen atılıp bütün sesin kurguda kurulduğu bir yapay zekâ kısa film hattında uzay sahnesi ses tasarımının belgelenmiş kuralları (vakumda dış ses yokluğu, gövde ve giysi üzerinden iletilen ses, kask içi nefes ve telsiz, basınçlı kabin içi, ince atmosfer), bu kuralların bilinen uzay filmlerinde nasıl uygulandığı ve izleyicinin "sessizlik"i nasıl okuduğu, lisanslı efekt kütüphaneleri ile yapay zekâ ses efekti üreticilerinin (ve Google Flow / Google'ın müzik ve ses araçlarının) ticari kullanım koşulları, YouTube için yükseklik hedefi (LUFS) ve diyalog-efekt-müzik dengesinin ölçülmüş değerleri, sentetik ses ya da metinden sese ile kısa replik kaydının kanal politikası açısından durumu.
Pratik tarafı topla: on saniyelik sessiz klipleri birleştiren bir kurguda ses köprüsü, ortam yatağı ve kesme noktası seçimi, replik yerleştirmenin dikiş ve kesmeyle ilişkisi, sesin görüntüyle senkron kaymasını önleme, ffmpeg gibi açık araçlarla uygulanabilir bir miks ve yükseklik ölçüm akışı.
Kritik kısıt: kullanım yeri, Google Flow'da üretilen, 8-10 saniyelik, fotogerçekçi uzay bilimkurgu klipleridir; karakter basınç giysili ve kasklıdır, çoğunda vizör berrak, bazılarında opaktır; modelin ürettiği ses kurguda tamamen atılır ve bütün ses (ortam, efekt, nefes, telsiz, replik, müzik) kurguda eklenir; replikler kısa, az ve İngilizcedir; kurgu araçları ffmpeg ve bir masaüstü kurgu yazılımıdır, ses stüdyosu ve foley çekimi YOKTUR — bu yüzden stüdyo kaydı ya da özel donanım gerektiren çözümleri "hat dışı" diye işaretle ama silme, kütüphane, üretici ve açık araçlarla uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) MODEL SESİ tablosu — davranış (istenmeyen konuşma, uydurma ad, telsiz cümlesi, vakumda ses, ağız hareketi), tetikleyici, önleyen yöntem (prompt, kadraj, sessiz üretim, sonradan atma), ölçülmüş etkisi, model ve sürüm, kaynak ve etiket; (b) UZAY SESİ tablosu — ortam (vakum dışı, gövde iletimi, kask içi, basınçlı kabin, ince atmosfer), duyulması gereken, duyulmaması gereken, film örneği, kaynak ve etiket; (c) KURGU AKIŞI tablosu — adım, araç, hedef değer (LUFS, tepe, diyalog/efekt/müzik oranı), lisans koşulu, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
SES TARİFİ → KONUŞMA (06.10.2026):
  THE_LAST_GATE K18   "one word spoken … the pilot names her sister … No dialogue in this shot."
                      → PART1'in 13 içerikli raporundan 9'u "Elena." duydu; filmde böyle bir ad yok
  THE_LAST_GATE K87   "A withdrawal advisory on the enemy channel … No dialogue in this shot."
                      → "Withdrawal advisory on enemy channel… Abort the approach immediately"
  THE_STOLEN_SKY S61  "a radio channel opening on static and staying empty" + "No dialogue."
                      → "69... 48... Transfer request accepted" · S10 → "Roger, system se…"
VAKUMDA SES:  AUDIO satırı HİÇ YOK (KRONOS) → 4 🔴 · TAM YAZILI (SUSMAYAN) → 4 🔴 · THE_LAST_GATE 92/92 yazılı → 6 🔴
              ⇒ eski analiz: "kapanma yeri kurgu"; yeni hat model sesini atıyor (kurgu.py · -an; replik dışı −91 dB ölçüldü)
AÇIK SORU:    ses atılınca görüntüdeki konuşma izi (ağız, çene) de gidiyor mu? Ses tarifi görüntüyü değiştiriyor mu?
YENİ HAT KURALI (06.10.2026): video promptunda konuşma/ses tarifi yok (film_dogrula.py "konuşma/ses tarifi" kontrolü;
              eski 2.913 promptun 311'inde, 18 filmde bulundu).
```

---

# 5️⃣ GEMINI İLE VİDEO QA'NIN GÜVENİLİRLİĞİ — model neyi görebilir, neyi uydurur

```
Google Gemini'nin güncel sürümlerinin (Gemini uygulaması ve API'deki 2.5 / 3.x Pro ve Flash, Ekim 2026 itibarıyla güncel olanlar; karşılaştırma için GPT ve Claude'un görsel-video yetenekleri) video anlama yeteneğini, yapay zekâ ile üretilmiş videolardaki teknik hataları bulma işi açısından araştır: videonun saniyede kaç kare örneklenerek işlendiği ve bu örneklemenin kullanıcı tarafından değiştirilip değiştirilemediği (Gemini uygulamasında ve API'de ayrı ayrı), çözünürlük ayarının etkisi, bir saniyeden kısa süren bir hatanın (parmak erimesi, tek karelik sıçrama, kısa yazı belirmesi) yakalanma olasılığı, zaman damgası doğruluğu, video uzunluğu arttıkça ayrıntı kaybı ve bunun hangi sürede başladığı — resmî belge, model kartı, kıyaslama (video soru-cevap, zamansal konumlandırma, yapay video kusur tespiti) ve yöntemi yazılı bağımsız testlerle; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: modelin videoda olmayan olay, nesne ya da replik uydurma (halüsinasyon) oranı ve bunu artıran koşullar, sorudaki ya da verilen plandaki beklentiye göre görme eğilimi (plan verilince plana uyan şeyi görmek), puan istendiğinde kusur bulamadığı kategoriye en yüksek puanı verme ve puanların aynı videoda koşudan koşuya ne kadar oynadığı, fiziği doğru olanı kusur sayma (ince atmosferi vakum sanma, düşük yerçekimini "süzülme" kusuru sayma, sonradan eklenmiş başlık kartını üretim hatası sayma), aynı sohbette ikinci bir değerlendirme yapılınca birincinin kararlarını taşıma.
Protokolü ayrıca sor: hata bulma işinde videoyu kaç saniyelik parçalara bölmenin, video yerine kare kontak sayfası (etiketli küçük kareler ızgarası) vermenin, kapalı bir hata türü listesiyle ve güven derecesiyle sormanın, puan istememenin, "ne olmalı" bilgisinin (ortam, kişi sayısı, beklenen sessizlik) verilmesinin ve planın hiç verilmemesinin yanlış pozitif ve yanlış negatif oranlarına ölçülmüş etkisi; aynı videoyu iki bağımsız oturumda koşup kesişimi almanın değeri; modelin "bulamadım" cevabının ne kadar güvenilir olduğu.
Anlatı testini topla: hikâyeyi bilmeyen izleyici yerine modeli kullanmanın (videoyu izletip "ne oldu, karakter ne istedi, nerede kafan karıştı" diye sormanın) gerçek izleyici cevaplarıyla ne kadar örtüştüğüne dair çalışmalar, izleyicinin bırakma anını tahmin etme konusunda modelin belgelenmiş başarısı, kısa film ve YouTube Shorts tutma verileriyle karşılaştırma.
Kritik kısıt: kullanım yeri, Google Flow'da üretilmiş 8-10 saniyelik kliplerden kurgulanmış, 1-16 dakikalık fotogerçekçi uzay bilimkurgu kısa filmleridir; değerlendirme Gemini uygulamasına video yüklenerek ya da kare görselleri verilerek yapılır, sonuç insan tarafından doğrulanır ve son karar her zaman insan izlemesidir; yazılım geliştirme, kendi modelini eğitme ya da ücretli değerlendirme platformu YOKTUR, API yalnız basit betiklerle kullanılabilir — bu yüzden özel model eğitimi gerektiren çözümleri "hat dışı" diye işaretle ama silme, uygulama ve basit betiklerle uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) GÖRME SINIRI tablosu — özellik (kare örnekleme, çözünürlük, kısa hata yakalama, zaman damgası, uzunlukla ayrıntı kaybı), değer ya da davranış, uygulama/API farkı, model ve sürüm, kaynak ve etiket; (b) YANILGI tablosu — yanılgı türü (uydurma olay ya da replik, plana göre görme, puan şişirme, doğru fiziği kusur sayma, oturum taşıması), ölçülmüş oran, önleyen protokol adımı, kaynak ve etiket; (c) PROTOKOL tablosu — adım (parça uzunluğu, kontak sayfası, kapalı liste, güven derecesi, "ne olmalı" bloğu, plansız anlatı testi, çift oturum), etkisi, maliyeti, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ

```
ESKİ HATTIN QA KAYDI:
  725 mercek raporu · 58 film · tekil karar GO %11 · bölümler karşılaştırılınca tabloya giren GO 12
  12 filmin 698 tekil bulgusunun 214'ü (%31) QA YANILGISI (06.10.2026). Örnekler:
    · yanlış SPEC: THE_LAST_TOW bölüm 1'in 10 raporu THE_STATIC_VEIL SPEC'iyle koşmuş
    · doğru fizik = kusur: GUNES_MEZARI 0,90 bar atmosfer "vakum" sanıldı (4 satır) · THE_FALLING_WORLD 0,30 g "floaty"
    · başlık kartı (post) 🔴 "yazı" sayıldı: 14 film
    · kusursuz kategoriye 10/10: THE_LAST_GATE bölüm 4 ③ SES 9 hücrenin 9'u ("None" → 10/10)
    · aynı film iki kez: ±1,3 puan (T1_KARE_KALITE)
    · mercekler farklı uzunlukta master ölçtü: THE_STILL_POINT 187–245 s
    · videoda olmayanı anlatma ya da üretim ↔ repo uyuşmazlığı: THE_LISTENING_WORLD S2/S3'te 11 mercek promptta
      olmayan rampa ve gemi anlattı (hangisi olduğu doğrulanmadı)
    · yerçekimi ölçümü: THE_STOLEN_SKY'de QA 0,68–3,13 m/s² ölçtü, film 8,8 yazıyor — ölçüm mü model mi?
YENİ HAT TASARIMI: TARAMA (puansız, kapalı 11 tür, güven derecesi, "ne olmalı" bloğu, ≤90 sn parça) ·
                   ANLATIM_TESTİ (yalnız video, plan yok, yeni sohbet) · son söz insan (IZLEME_FORMU)
CEVAPTAN BEKLENEN: 90 sn sınırı doğru mu · kare örnekleme 1 fps ise kısa füzyon nasıl yakalanır (kontak sayfası?) ·
                   anlatı testi gerçek izleyiciyle ne kadar örtüşür.
```

---

## 📥 SONUÇ GELDİĞİNDE — kayıt zinciri

1. **Kaydet.** Ham cevap olduğu gibi `uretim_hatti/ARASTIRMA/ham/0n_<KONU>_HAM.md` dosyasına yazılır. Düzenlenmez.
2. **Süz (ana ajan).**
   - Her ÖLÇÜLMÜŞ satır için alıntı ve bağlantı aranır; yoksa satır UYGULAMA'ya iner.
   - Satırlar o promptun SINAMA SETİ'ne karşı okunur: depo vakasını açıklayan → KABUL · çelişen → RED + gerekçe · ilgisiz → NOT.
   - Eski hatta raporların aşağı yukarı üçte biri etiket sözleşmesini çiğnedi (TUR 22 · TUR 24). Etiket, alıntı ve bağlantıyla doğrulanmadan hiçbir sayı kural olmaz.
3. **İndir (sahip onayıyla).** KABUL satırları önce kapattığı yere iner: ajan kuralı, `film_dogrula.py` kontrolü, `QA_PROMPTLARI/`, `SMOKE_TEST.md`. Kanıtlı tuzak `BILINEN_TUZAKLAR.md`'ye yalnız sahip kararıyla girer.
4. **Yeni kılavuz yalnız gerekirse.** Bir konu kurala sığmıyorsa `uretim_hatti/KILAVUZ_<KONU>.md` açılır: kısa, kanıtlı, tek sayfa. Eski hattın kılavuzları (`kilavuzlar_ve_sistem_dosyalari/`) düzenlenmez.
5. **Bu dosyanın başındaki Durum satırı** ✅ KOŞULDU + tarih + ham dosya yolu ile güncellenir.
