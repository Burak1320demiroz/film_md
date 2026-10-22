<!-- teknik-danisman (sonnet) F5 tur 1 G01 — cevabı AYNEN (alt ajan transkriptinden), 20.10.2026 -->

## TEKNİK DANIŞMAN · F5 tur 1 · DEAD_LAST G01 (C01–C08)

Önce çerçeve. Bu dosyada üç şey sorunun ortası: C03'te el-hücre teması, açılıştaki konuşan yüz (C01), ağız kadrajda repliklerin sessiz videoda ayrı kayıtla birleşmesi. ÖLÜMCÜL yok. Dokuz CİDDİ bulgu üretim kaybı getirir ve ikisi plan cümlesine dokunur. Plan cümlesini değiştiren her düzeltme sahibe gider ("plandan asla dışarı çıkma"); bunları "PLAN CÜMLESİ" diye işaretledim.

**Kontrol listesi özeti (çekim çekim):**
- T01 (el/beden-nesne): C03 (B1), C06 (B3). C06'nın risk sütunu FILM.md §4'te "—"; olmayan risk de bulgudur.
- T03/T13 (duman, toz, buhar, vakumda ses): G01'de yok. Videolar sessiz döner. C02'de tek "energy filaments" var, katı biçimde yazılmış.
- T06 (ekran, panel, yazı): C01, C02, C04, C05, C06 (B4–B6).
- T05/T09 (durum, panel): Needle sayfasında hücre-takılı tek panel var; hücresiz beşik ve kabin içi yok (B2).
- T15 (fazla kişi): C05 kalabalığı, C07'de beş araç (B6, B9). C04'te römorkör kabini bulanık, ikinci yüz yok.
- T08, T02, T10: yok.
- Açılış C01–C03: B8, B1, B4.
- Ağız kadrajda replik: C01, C04, C05, C06, C08 (B7).
- Model sesi repliği: film "model sesi KAPALI", yani (b), (c), (d), (e) uygulanmaz. (a) için B10.
- Kesme sürekliliği: B13 (kabin içi, Kalix omuz şeridi). C01'den C08'e ölçek ve açı farkı yeterli.
- Mod ↔ model: B11.
- Red riski: C01–C08'de şiddet/ölüm/milliyet kelimesi yok (Grep, referans bölümü hariç). Bedenden bir şey çıkarma yok. Yan yana iki ön kol, tepeden makro ya da yüzsüz izolasyon yok.

---

### B1 · CİDDİ · C03 açılışın içinde karmaşık el-nesne teması
YER       C03 Video, G01.md:385 · C03 Görsel, G01.md:376
KANIT     `The two gloved hands lower the single blue cell into the existing dorsal cradle, lock it with one clear click and withdraw.` · `The loader's plain gloved hands leave the frame through the top edge.` · Görsel: `An alien loader's plain gloved hands hold one blue booster cell directly over the dorsal latch cradle`
ETKİ      0:20–0:30'da hücrenin beşiğe oturduğu an çekimin tamamıdır; parmak-hücre kaynaşması, hücrenin gövdeden geçmesi ya da ikinci hücre çıkarsa C03 açılışta kullanılamaz.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47 (§B sıra 1, 92 🔴; temas cümlesi 22/25 promptta yazılıyken 7 🔴) [ölçüm] · ILK_30_SANIYE_KILAVUZU.md:105 ("karmaşık el-nesne teması" kaçınılır) [UYGULAMA] · ORTAK HAREKET "at most one main physical action"
ARIZA     T01
DÜZELTME  Temas anı kadrajdan çıkarılır. Eller kadraj içinde kalırsa: ilk 2 s hücre elde ve beşiğin üstünde sabit. Sonra tek hareket, hücrenin yavaş inişi. Kilitlenme "click" ile değil, beşik kenetlerinin kapanıp ışığının yanmasıyla gösterilir.
          Birebir:
          `lock it with one clear click and withdraw` → `the cradle latches close around it and one small blue latch light comes on`
          `leave the frame through the top edge` → `are already out of frame above`
          Çekim sonunda elin kadraja girip çıkması (T05'in "kadraja giren/çıkan" kuralı) da böylece kalkar.
          Daha güvenli alternatif (PLAN CÜMLESİ, sahibe sorulur): başlangıç karesi hücre beşiğe oturmuş, eller tam çekilmek üzere. Hareket yalnız eller yukarı çıkarken kenetlerin kapanması. Temas kadrajda hiç yok.
          Düşük riskli karşılık (kılavuz §6): yavaş itme + nesne hareketi. Yani aracın sırtına doğru yavaş bir kamera itişi, hücre zaten yerinde.

### B2 · CİDDİ · 8.NEEDLE sayfasında C03/C04/C06'nın ihtiyaç duyduğu iki durum yok
YER       G01.md:85 (8.NEEDLE `PANELLER tek görünüş (plan V01) … sağlam`) · G01.md:376 (C03 Görsel) · G01.md:399, 452 (C04, C06 Görsel)
KANIT     8.NEEDLE: `One detachable blue booster fuel cell is fixed lengthwise on the dorsal spine in a visible emergency latch cradle.` C03 Görsel: `the cradle is still empty in this frame` · C04/C06: `take the shape of the one-pilot canopy from it`
ETKİ      C03 karesinde model sayfadaki oturmuş hücreyi de alıp elindeki hücreyle ikinci hücre üretebilir. Kabin içinde ise referans yoktur: Raka'nın kokpit iç görünüşü C04 ve C06'da sıfırdan uydurulur ve kesmede sıçrar.
DOĞDUĞU   referans
KURAL     FILM.md:140-141 (özne başına tek sayfa, durumlar panel) [SÖZLEŞME 10.10.2026] · SMOKE P17
ARIZA     T05 · T09
DÜZELTME  8.NEEDLE sayfası yeniden üretilir (sürüm v2) ve sayfaya iki panel eklenir: (1) beşik boş / hücre kalkık, (2) kabin içi kokpit. Sayfa çok panelli olunca modelin yanlış paneli alma riski doğar (SMOKE P17). Bu yüzden C03 ve C04/C06 kare promptlarına "take the panel showing …" cümlesi eklenir.
          `the cradle is still empty in this frame` → `take the empty latch cradle panel from it; the cradle is empty in this frame`
          Bu, planın "V01 tek görünüş" cümlesine panel ekler (PLAN CÜMLESİ, sahibe sorulur). Reddedilirse C03 kare kapısına "ikinci hücre yok" zaten yazılı, ama bu üretimde deneme harcatır.

### B3 · CİDDİ · C06 kemer çekme ve konuşma aynı anda; bu çekimin risk sütunu boş
YER       C06 Video, G01.md:461 · C06 Görsel, G01.md:452 · FILM.md:262 (risk "—")
KANIT     `Raka gives the restraint one final tightening pull and delivers her short vow.` · Görsel: `one simple chest restraint being pulled taut`
ETKİ      Elin kemeri kavrayıp çekmesi T01'dir. Aynı anda ağız senkronu istendiği için (iki ana eylem) el ya kemere gömülür ya da kemer çekilmez, yüz de bozulur.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR.md:47 · ORTAK HAREKET "at most one main physical action" · FILM.md:162 teknik-danışman maddesi [SÖZLEŞME/ölçüm]
ARIZA     T01
DÜZELTME  Eller kadraj dışında kalır; kemerin gerilmesi omuz ve çene hareketiyle okunur.
          `Raka gives the restraint one final tightening pull and delivers her short vow.` → `Raka's shoulders settle against the taut chest restraint and she delivers her short vow.`
          `one simple chest restraint being pulled taut` → `one simple chest restraint already pulled taut`
          FILM.md §4 C06 risk sütununa "T01 → kemer çekilmiş başlar, el kadrajda yok" yazılır.

### B4 · CİDDİ · C02 aynı promptta hem "sistem satırı görüntünün üstüne eklenir" hem "yazı ekleme" diyor
YER       C02 Video, G01.md:360 ve 362
KANIT     `Do not add in-shot captions, random extra characters …` ile `The flat system line is added over the image; no speaking face.`
ETKİ      "Line … added over the image" modele altyazı/yazı basma talimatı gibi okunur; açılışın (0:10–0:20) tek ekranına rastgele harf çıkar. Çelişki olunca ikisi de tutmaz.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:48 ("Aynı promptta hem ekran hem 'yazı yok' duramaz") · BILINEN_TUZAKLAR.md:73 [ölçüm]
ARIZA     T06
DÜZELTME  `The flat system line is added over the image; no speaking face.` → `No face appears.` (ses ve yazı kurguda; G01.md:8'deki karar zaten bu.)
          PLAN CÜMLESİ. Sahip kabul etmezse en azından "added over the image" kısmı silinir.

### B5 · CİDDİ · C01, C04, C06'da kokpit göstergesi hem anılıyor hem "okunmaz" deniyor
YER       C01 Görsel, G01.md:327 · C04 Görsel, G01.md:399 · C06 Görsel, G01.md:452
KANIT     C01: `One face, one planet, no readable cockpit display, no embedded caption.` · C04: `Dark controls without readable text, same pit light.` · C06: `Cool-blue light from the newly installed booster status reflection, no readable screen.`
ETKİ      "display", "controls", "status" kelimeleri modele okunacak panel fikri verir; kokpit kadrajlarında (T06 17/49) uydurma harf ve rakam çıkar. Olumsuz kelime bunu tutmaz.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:48 (tasarımla çöz: ekran yazısız ya da kadraja girmez) [ölçüm] · FILM.md:171 ("no X" eklemek tutmuyor, bu yüzden silme önerilir)
ARIZA     T06
DÜZELTME  C01: `no readable cockpit display, no embedded caption` → sil (kalan: `One face, one planet.`)
          C04: `Dark controls without readable text, same pit light.` → `Dark panels out of focus, same pit light.`
          C06: `Cool-blue light from the newly installed booster status reflection, no readable screen.` → `Cool-blue light falls across her face and the restraint.`
          Üçü de planın cümlesidir (PLAN CÜMLESİ).

### B6 · CİDDİ · C05 "broadcast / presenter" + "five symbols" yazı ve sayı üretir
YER       C05 Görsel, G01.md:426 · C05 Video, G01.md:435
KANIT     `dominates a broadcast portrait above the white starting dock` · `five simple abstract world-link symbols` · `calm presenter-like authority` · `The five background lane lights illuminate sequentially once; do not change their number.`
ETKİ      "broadcast" ve "presenter" altıyazı, kanal logosu ya da haber bandı çağırır. Beş sembol ve beş ışığın sırayla yanması da sayı kayması riski (beşi dörde ya da altıya çevirir). Arkada ayrıca altı türlü kalabalık var (T15).
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:48, 73 [ölçüm] · FILM.md:246 (sayı sabit) [TERCİH]
ARIZA     T06 · T15
DÜZELTME  `a broadcast portrait above` → `a vast projected portrait above`
          `calm presenter-like authority` → `calm ceremonial authority`
          Beş ışık sırayla yanma hareketi çıkarılır, sabit kalırlar:
          `The five background lane lights illuminate sequentially once; do not change their number.` → `The five background lane lights glow steadily.`
          PLAN CÜMLESİ. Sembol sayısı için F7 kare kapısı zaten "beş şerit ışığı ve beş simge" diyor; videoda sayılma hareketi olmazsa kapı yeterli.

### B7 · CİDDİ · Ağız kadrajdaki beş replik sessiz video + ayrı kayıtla; ağız zamanı hiçbir yerde sabitlenmemiş
YER       C01 Video, G01.md:336 · FILM.md:339 (R01 saniye 2.2) · C04 G01.md:408 · C05 G01.md:435 · C06 G01.md:461 · C08 G01.md:511
KANIT     C01: `0-5 s: … Axi speaks the assigned plea` (R01 kayıtta 2.2 s'de başlıyor, 2.0 s). FILM.md:12: `temiz replik ayrı kayıt, kurguda`; FLOW İŞ EMRİ: `Return silent videos AÇIK`
ETKİ      Model sessiz döndüğü için dudak zamanı modele göre rastgele; kayıt kurguda yerine konunca yakın planda ses ağızdan kayar. En görünür yer film açılışı (C01 yüz).
DOĞDUĞU   ses
KURAL     BILINEN_TUZAKLAR.md:57 (replik tek kaynaktan; ses kimliği kurgu) [ölçüm] · FILM.md:392 ("ağız kadrajda … son çare") [SÖZLEŞME]
ARIZA     yeni (ağız–ses eşleşmesi)
DÜZELTME  İki adım. (1) Kayıt, video seçildikten sonra klibin gerçek ağız zamanına göre alınır; §5 saniyeleri o zaman güncellenir (kurgu işi). (2) C01'de ağız ilk saniyelerde kapalı olsun diye vuruş bölünür:
          `0-5 s: One ten-second continuous shot with a restrained push toward Axi.` … `Axi speaks the assigned plea, with clear small mouth motion and no scream.` → `0-2 s: One ten-second continuous shot with a restrained push toward Axi; her lips rest closed. 2-5 s: Axi speaks the assigned plea, with clear small mouth motion and no scream.`
          Aynı biçimde C04/C05/C06/C08'de ilk vuruş ağzın açılacağı saniyeyi söylesin (C06: 1.0–3.0 s).

### B8 · CİDDİ · C01 açılışında konuşan yüz yakın planı + yüz yana dönük + dört yanak uzantısı + itme
YER       C01 Görsel, G01.md:327 · C01 Video, G01.md:336
KANIT     `Axi's exact smoke-gray face, amber eyes and four short cheek tendrils are close in the left foreground, turned toward a broad side window.` · Video: `a restrained push toward Axi … The push toward Axi and the widening fracture carry on to the end of the shot.`
ETKİ      Yüz profile döndüğünde dört uzantının yalnız yarısı görünür; model sayıyı bozar (kare kapısı "yanak uzantısı 4"). İtme yüzü büyüttükçe risk artar. Konuşan yüz yakın planı açılışta en riskli seçenek ve bu çekim aynı zamanda gezegen çatlaması, ışıkların sönmesi ve konuşmayı da taşıyor.
DOĞDUĞU   kare
KURAL     ILK_30_SANIYE_KILAVUZU.md:105-107 (kaçınılanlar: yüz yakın planı; düşük risk: geniş/orta plan, yavaş itme) [UYGULAMA] · FLOW İŞ EMRİ "plan pilotu 1"
ARIZA     T16 · T12
DÜZELTME  Pilot sonucuna göre iki seviye:
          (a) Tutarsa: yüz üç çeyrek, kameraya yarı dönük olsun ki dört uzantı da okunsun: `turned toward a broad side window` → `turned three-quarters toward the camera, her eyes on the broad side window`.
          (b) Tutmazsa düşük riskli karşılık: orta plan, Axi omuz üstü, gezegen penceredeki ana özne, itme yok. R01 telsiz gibi kadraj dışı kurguya alınır (§5 Kaynak değişir, sahibe sorulur). Bu halde B7'nin C01 kısmı da kalkar.

### B9 · CİDDİ · C07 beş araç, takip kamerası ve "hepsi kadrajda kalır" çelişiyor
YER       C07 Video, G01.md:488
KANIT     `0-3 s: The five craft launch from the black magnetic ribbon and race from left to right, with the camera tracking steadily alongside.` ve `7-10 s: Halo, Bastion and Sickle run far behind as small silhouettes, and all five craft stay in view.`
ETKİ      Kamera öndeki ikiliyi takip ederse "far behind" üç araç sola kadrajdan çıkar. Kadrajda kalmaları için de kamera geri çekilmeli, o zaman ikinci kamera hareketi doğar. Duran araçtan hızlanma + takip + beş sayı = model araç sayısını değiştirir.
DOĞDUĞU   hareket
KURAL     FILM.md:316-317 (kadraja giren/çıkan yok; en çok bir basit kamera hareketi) [SÖZLEŞME] · ORTAK HAREKET "at most one … restrained camera move"
ARIZA     T15 · T07
DÜZELTME  Başlangıç karesi araçlar yola çıkmış olsun, kamera tek hareket yapsın:
          `The five craft launch from the black magnetic ribbon and race from left to right, with the camera tracking steadily alongside.` → `The five craft, already moving along the black magnetic ribbon, race from left to right while the camera slowly pulls back to keep the whole pack in view.`
          Görsel: `sit on the black magnetic ribbon … ready to launch between the roots` → `race along the black magnetic ribbon toward the giant hanging plant roots`

### B10 · KÜÇÜK · Telsiz replikli çekimlerde kadrajdaki kişinin ağzı yalnız olumsuz cümleyle kapatılıyor
YER       C04 Video, G01.md:408 · C06 Video, G01.md:461 · C08 Video, G01.md:511 · C03 Video, G01.md:385
KANIT     `Do not make Raka mouth Axi's words.` · `only Raka's own line receives mouth movement` · `Axi's assigned sentence is heard off-screen.` (C03: kadrajda Axi yok)
ETKİ      Dialogue bloğu karşı tarafın cümlesini de taşıdığı için model kadrajdaki yüzü onu söylerken oynatabilir. C03'te de Axi adı modele ikinci karakter fikri verir.
DOĞDUĞU   metin
KURAL     FILM.md:392 [SÖZLEŞME] · BILINEN_TUZAKLAR.md:57
ARIZA     T15
DÜZELTME  C04: `Do not make Raka mouth Axi's words.` → `Her lips rest closed while Axi's words arrive over the radio.` (C06 ve C08'de aynı kalıp.) C03: `Axi's assigned sentence is heard off-screen.` → sil (ses kurguda). PLAN CÜMLESİ.

### B11 · KÜÇÜK · Tüm videolar "Ten-second" yazıyor, gerçek süre ölçülmedi
YER       C01–C08 Video ilk cümle · FILM.md:7 (`KLIP_SURESI ölçülmedi`) · G01.md:523
KANIT     `Ten-second single continuous shot` · FLOW_GERCEKLERI.md:30: Frames to Video `4 · 6 · 8 s`, Omni `süre ?`
ETKİ      8 s'lik Veo klibi gelirse 7-10 s vuruşlarındaki bitiş durumu (C06 "launch vibration", C03 hücrenin oturması) kesilir; iş emri C02–C08'i ölçüm öncesi üretmeyi zaten yasaklıyor.
DOĞDUĞU   araç
KURAL     SMOKE P14 · FLOW_GERCEKLERI.md:164 [ARAÇ]
ARIZA     T07
DÜZELTME  Her videonun son cümlesi (bitiş durumu) zamansız yazılmış kalsın (C04, C05 ve C07 böyle). C03 ve C06'da son vuruşun bitiş durumu da zamansız son cümleye taşınsın. Ölçümde <10 s çıkarsa C03 `0-7 s / 7-10 s` → `0-5.5 s / 5.5-8 s` (iş emri örneği). Ayrıca B1'in düzeltmesi kısa klipte de çalışır.

### B12 · KÜÇÜK · Kimlik cümlesinde olmayan eş anlamlılar (özne yeniden adlandırılıyor)
YER       C06 Görsel, G01.md:452 · C07 Görsel, G01.md:479 · C08 Görsel, G01.md:502
KANIT     C06: `white veined skin … cobalt suit and ivory collar` (KİMLİK: `Chalk-white matte skin … ivory neck seal`) · C07: `Needle is white-and-blue, Fang red-bronze` (KİMLİK: `slim ivory hull, cobalt accents`; `dark crimson hull with bronze side bumper rails`) · C08: `Raka's white craft`
ETKİ      "collar" ile "neck seal" iki ayrı parça olarak çizilebilir; "red-bronze" ile "dark crimson" renk kayması üretir.
DOĞDUĞU   metin
KURAL     FILM.md:246 (kısaltılmaz, yeniden adlandırılmaz) · film_dogrula DERS Y2 [SÖZLEŞME]
ARIZA     T16 · T09
DÜZELTME  C06: `ivory collar` → `ivory neck seal`; `white veined skin` → `chalk-white veined skin`. C07: `Needle is white-and-blue, Fang red-bronze` → `Needle is ivory-and-cobalt, Fang dark crimson-and-bronze`. C08: `Raka's white craft` → `Raka's ivory-and-cobalt Needle`. (C07 renk sırası PLAN CÜMLESİ.)

### B13 · KÜÇÜK · Kabin içi ve Kalix omuz şeridi için ortak cümle yok
YER       C04/C06 Görsel, G01.md:401, 454 · C08 Görsel, G01.md:504 · C05 Görsel, G01.md:426
KANIT     C04: `A headrest sits behind her head inside the compact canopy.` · C06: `A headrest sits behind her head.` · C08: `Behind Thren is his craft's single compact pilot canopy.` · C05: `crimson sash remain visible` (taraf yok; G01.md:572 Q1 de "uydurulmadı" diyor)
ETKİ      C04 ile C06 aynı kokpit iç mekânı, ama cümleler farklı; C08'de Thren'in kabini ilk kez çıkıyor ve C17, C21'de yeniden gerekecek. Kalix'in omuz şeridi tarafı C05, C27, C46'da klip başına değişir.
DOĞDUĞU   metin
KURAL     FILM.md:246-247 (İşaret: sayı + taraf + konum) · GECIS_VE_SES_SUREKLILIGI (ortak görünüm cümlesi) [SÖZLEŞME]
ARIZA     T04 · T09
DÜZELTME  C04 ve C06 için tek kabin cümlesi yazılır (`Inside Needle's compact one-pilot canopy, a pale headrest behind her head, dark panels out of focus.`) ve ikisinde de birebir kullanılır. Thren kabini için de bir tane yazılıp C08, C17, C21'de aynen geçer. Kalix için taraf kare onayından önce sahibe sorulur ve KİMLİK tablosuna işlenir (F7 notu zaten var, ama C05 kare onayından önce kapanmalı).

### B14 · KÜÇÜK · C08'de Needle "glides past" diyor, yan yana kalması isteniyor
YER       C08 Video, G01.md:511
KANIT     `Raka's white Needle glides past the side window in the same direction` ve `keeps gliding past the window`
ETKİ      "past" geçip kadrajdan çıkmak olarak okunur; plan "yan yana, aynı yönde" istiyor. Needle çıkarsa 7-10 s boşalır.
DOĞDUĞU   metin
KURAL     FILM.md:316 [SÖZLEŞME]
ARIZA     T07
DÜZELTME  `glides past the side window` → `holds position in the side window`; `keeps gliding past the window` → `stays in the side window`.

### B15 · KÜÇÜK · C02'de olumsuz cümleler nesne çağırıyor
YER       C02 Görsel, G01.md:353 · C02 Video, G01.md:362
KANIT     `no miniature planet inside a vial` · `rather than filling the screen with an undifferentiated explosion`
ETKİ      "vial" ve "explosion" kelimeleri prompta girer ve model onları çizer. Aynı sınıf: BILINEN_TUZAKLAR §A ("no blood" yazılsa bile kelime etkisi).
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR.md:29-30 (kelime reddi/etkisi kelimeyle çözülür) [ölçüm] · FILM.md:171 (no X tutmuyor)
ARIZA     T03
DÜZELTME  `no miniature planet inside a vial` → sil. `Keep the planet silhouette readable rather than filling the screen with an undifferentiated explosion.` → `Keep the planet silhouette readable against the dark space.` (PLAN CÜMLESİ.)

---

**KORU:**
- C02'nin kadrajı (geniş yörünge planı, kamera neredeyse sabit, insan yok): açılış için en düşük riskli seçim (ILK_30_SANIYE_KILAVUZU.md:106). B4/B15 yalnız metin temizliği.
- C01'in yavaş itmesi ve C05'in yavaş itmesi kılavuzdaki düşük riskli hareket türü.
- C07/C08'de hasar durumları açıkça yazılmış (iki sağlam kanat, iki aktif dış motor, üç aktif motor).

**F5'e not (diğer gruplar için, film içi):** Aynı riski taşıyan çekimler FILM.md §4'e göre şunlar. El-nesne teması: C10 (Fang yan koruması-kanat temas, kadraj dışı tutulmalı), C36 (Axi servis kolu), C41–C42 (hücre bırakma ve besleme halkasına ulaşma). Ekran/şema yazısı: C19, C20 (Axi iki hat şeması), C22 (hücre göstergesi). Konuşan yakın portre + telsiz Dialogue bloğu: C17, C21, C23–C27, C32, C33. C23–C24 gibi 4 s üstü replikler ağız kadrajda ve 5 s sınırını (FILM.md:392) zorluyor (R30 5.0 s, R33 5.0 s, R29 4.0 s). Needle hasar sayfası (20) ayrı dosya (sahip istisnası); 8'in paneller sorunu (B2) 20'yi de etkiler.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 9 · KÜÇÜK 6
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok). Ancak B1, B2, B3, B7 ve B8 üretim kaybı getirir; kabul veya gerekçeli red beklenir. Plan cümlesine dokunanlar (B1 alternatifi, B2, B4, B5, B6, B10, B15) sahibe gider.
GİRDİ    yatay_8_dk_filmler/DEAD_LAST/PROMPTLAR/G01.md (tamamı, 589 satır) · DEAD_LAST/FILM.md §1–§5 (satır 1–392; §6 sonrası okunmadı) · uretim_hatti/ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md T bölümü (satır 44–62) · ILK_30_SANIYE_KILAVUZU.md §6 (satır 93–108) · FLOW_GERCEKLERI.md (Grep ile mod/model/ses satırları). Kare ve video yok, yalnız metin okundu.
YAPILMADI  Kare/hareket incelemesi (üretim yok). `film_dogrula.py` çalıştırılmadı. ODA/F5_yazim_karari.md okunmadı (gerekçe verilmediği için görmezden gelindi). Videonun gerçek süresi ve Omni/Veo seçimi ölçülmedi (B11).
