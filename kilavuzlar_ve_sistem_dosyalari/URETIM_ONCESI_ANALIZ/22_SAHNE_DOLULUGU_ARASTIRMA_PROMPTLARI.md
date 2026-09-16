# 🔬 22 — SAHNE DOLULUĞU ARAŞTIRMA PROMPTLARI (15.09.2026)

> **Ne bu dosya:** 48 × 10 s'lik yeni yatay film (`yatay_8_dk_filmler/`)
> yazılmadan ÖNCE kurulacak tek kılavuz için ÜÇ derin araştırma promptu.
> Her biri **altı cümledir**, her cümle **tek satırdır** ve **salt prompt**
> çalışır — kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> | # | konu | kurulacak kılavuzun bölümü (çalışma adı `SAHNE_DOLULUGU_KILAVUZU.md`) |
> |:--:|---|---|
> | 1 | **MOTOR** — eylem üç saniyede bitiyor: video motorlarının zaman davranışı | §4 MOTOR TARİF BİÇİMİ · §5 ÖLÇÜM (hareket profili eşiği) |
> | 2 | **ZANAAT** — sabit uzunlukta bir planı ne doldurur: sinema · animasyon · reklam | §3 DOLGU KAYNAKLARI · §2 ZAMAN BÜTÇESİ |
> | 3 | **SENARYO BİRİMİ** — 10 saniyelik sahne nasıl yazılır: fiil sınıfı · iskelet · 48 birim | §1 FİİL SINIFI · §2 10 s İSKELETİ · §6 ÖLÜ SAHNE KONTROLÜ |
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-21'in gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin sorunu (15.09.2026) — *"10 saniyenin sahnelerinin
> bazılarında 3 saniyede iş bitiyor, kalan 7 saniye boş geçebiliyor, boş boş
> durabiliyorlar."* Ve 48 × 10 s = 480 s'lik film bu birimden 48 tane ister;
> boş kalan her 7 s, filmin %70'idir. Teşhis depodan ölçüldü (15.09.2026
> kesiti; betik `doluluk_olcum.py`, aynı klasörde, depo kökünden koşulur):
>
> ```
> video prompt: 1440 · dosya: 133 · biçim: çıplak 0s — 624 · TIMELINE: 381 · MOTION (…): 243 · zaman damgasız düzyazı 127 · aralık / at n s 65
> vuruş satırı ayrıştırılan prompt: 584
>   son vuruşu durgunluk kelimesi taşıyan: 343 (59%)
>   t ≥ 5 s vuruşları: 1413 · durgunluk kelimeli: 652 (46%)
>   son güçlü gövde fiilinin zamanı: <5 s 65 (11%) · 5-8 s 61 (10%) · ≥8 s 402 (69%) · güçlü fiil yok 56 (10%)
> durgunluk kalıbı geçen prompt: "motionless" 141 · "stands still" 50 · "nothing else moves" 26 · "holds still" 23 · "stays still" 14 · "then stops" 13 · "nothing else in frame moves" 4 · "remains still" 3 · "frozen in place" 1
> ```
>
> ① Depo zaman damgasını ZATEN yazıyor (1440 promptun 1313'ü damgalı) ve
>    promptların %69'unda son güçlü fiil 8. saniyeden sonra — yani sorun
>    "vuruş yazılmamış" değil. İki hipotez kalıyor ve ikisi de ÖLÇÜLMEDİ:
>    (a) motor geç damgaları okumuyor, eylemi öne yığıp bitiriyor;
>    (b) geç vuruşlar zayıf — son vuruşların %59'u durgunluk kelimesi
>    taşıyor ("settles · holds · stays · nothing else moves"), yani plan
>    son üç saniyeyi kendi eliyle boşaltıyor. 1 numaralı prompt (a)'yı,
>    3 numaralı prompt (b)'yi sorar; ikisi çapraz okunur.
> ② QA korpusu aynı şeyi görüyor ama adı yok: `02_HAM_RAPORLAR/` içinde
>    "remains static" 10 raporda · "dead air" 6 · "plateau" 31 · segment
>    tarifi *"She breathes, but otherwise, nothing happens"* · ④ Hook
>    hücresi *"starts inside the threat, but static for 10s"*. Hiçbir mercek
>    "ölü saniye" saymıyor; ⑭ HAREKET amaçsız HAREKETİ etiketler, hareket
>    YOKLUĞUNU değil.
> ③ Kural var, yöntem yok: `SAHNE_ZINCIRI_VE_SINIR` §1 *"klibin içi boş
>    bırakılamaz — tek sürekli hareket plan boyunca sürmeli"* tek paragraf;
>    `OYUNCULUK_YAZIM` §4 tutulan durgunluğu yalnız S (sükûnet) sahnesi için
>    üçlüyle yazıyor. Depoda "moving hold", "stage business", "overlapping
>    action", "ikincil eylem" kelimeleri **hiçbir kılavuzda geçmiyor**
>    (`grep -liE` 0 dosya). `IMAGE_VIDEO_PROMPT_TEMPLATES` V3'ün kilit
>    örneği *"turns exactly one quarter, then stops, and nothing else in
>    frame moves"* — boşluğu şablon kendisi emrediyor.
> ④ Üretilmiş KLİP hiç ölçülmedi: `sahne_kapisi.sh` kesme sayar,
>    `olcum_kapisi.sh` ışık ölçer; saniye başına hareket enerjisi ölçen
>    betik yok. Yukarıdaki sayılar PROMPTUN sayılarıdır, klibin değil.
>
> **KOŞU KAYDI:** ✅ **TUR 19 koşuldu — 15.09.2026, aynı gün.** 3/3 rapor
> `TUR19_HAM_RAPORLAR/` (birebir; künye §⚠️: kaynak listesi yok, sayı katmanı
> çürük) → `04_ARASTIRMA_BULGULARI.md` §TUR 19 (süzme) → `../SAHNE_DOLULUGU_KILAVUZU.md`
> (sayısız yazıldı) → sıradaki: yatay_8_dk filmi. ⬜ altı araştırmasız aday
> (aşağıda) sahip kararı bekliyor. ⚠️ Kaynak listesi İSTENİR; gelmezse
> `00_KUNYE.md`'ye yazılır (TUR 15/17 dersi). Rapor motor tablosu getirirse
> motor adı ve tarihi olmayan satır inmez.

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR 19 (süzme kaydı) →
         SAHNE_DOLULUGU_KILAVUZU.md → dokunduğu yerler:
         IMAGE_VIDEO_PROMPT_TEMPLATES V3 kilit örneği + TIMELINE satırı ·
         KILAVUZ_REHBERI §2.0 iskelet (sahne satırına "son 3 s" hücresi) ·
         SAHNE_ZINCIRI §1 "klibin içi" paragrafı → işaretçi ·
         OYUNCULUK_YAZIM §4 (tutulan durgunluk üçlüsü → kılavuza bağlanır) ·
         00_SAHNE_TABLOSU sütun adayı ("son 3 s ne gösterir") ·
         prompt_kontrol kapı adayı ㉛ DOLULUK (yalnız yeni rejim) ·
         ⑭ HAREKET rubriği: ilk koşudan ÖNCE hareket YOKLUĞU satırı adayı ·
         makine kapısı adayı hareket_profili.sh (saniye başına enerji) ·
         yatay_8_dk_filmler/README (üretim öncesi doluluk kapısı satırı).
         Süzme kaydı ÜÇ liste tutar: GİRDİ · GİRMEDİ + NEDEN ·
         GEOMETRİYE ÇEVRİLDİ.

⛔ BU ARAŞTIRMA "DAHA ÇOK HAREKET" DEĞİLDİR.
   Aranan şey kıpırtı değil MEKANİZMA + EŞİK + TEST: bir bedenin işi
   bitince gözün kaç saniye sonra kadrajı terk ettiği, tutulan bir planı
   neyin "dolu" neyin "ölü" okuttuğu, hangi fiil sınıfının ekranda kaç
   saniye taşıdığı, motorun geç damgayı hangi biçimde okuduğu. Dolu ≠
   hareketli: saati çalışan tutulmuş plan doludur, koşan ama amaçsız
   beden boştur (⑭'ün alanı). Soru şudur: SANİYE 4-10'DA GÖZ NE YAPAR.
   "Şu sahne akıcıydı" diyen ama hangi öğe/kaç saniye/neden demeyen
   kaynak süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — deneysel / korpus / benchmark / hakemli ölçüm
   (b) UYGULAMA — yönetmen, kurgucu, animatör, storyboard sanatçısı,
       reklam yönetmeni, prompt mühendisi, motor belgesi
   (c) ÖNERİ    — raporun kendi tasarım önerisi
   Kaynaksız (a) düşer; (b) ancak iki bağımsız uygulayıcı aynı şeyi
   söylüyorsa iner; (c) yalnız ⬜ HİPOTEZ etiketiyle iner.
   TUR 17'nin dersi: sayı katmanı çürük gelirse kılavuz SAYISIZ yazılır.

⛔ KOPYA SINIRI — film, oyuncu ve animatör adı ARAŞTIRMA promptunda OLUR,
   ÜRETİM promptuna İNMEZ [MESHUR_SAHNE_KALIPLARI §4 · 17_ ve 21_'in usulü].
   Süzmede her bulgu GEOMETRİYE ve MEKANİZMAYA çevrilir ("Keaton'ın
   kapı vuruşu" → "işi biten el ikinci bir dirençle karşılaşır") ve
   04 §TUR 19 "GEOMETRİYE ÇEVRİLDİ" listesini tutar.

⛔ ÖNCEKİ TURLARLA VE MEVCUT KILAVUZLARLA ÇAKIŞMA ("ZATEN VAR").
   • DEĞİŞEN NİTELİK klip içinde üretilemez — ölçülmüş en zayıf eksen
     (KILAVUZ_REHBERI §7 · SAHNE_ZINCIRI §1): "kapak açılır", "lamba
     yanar", "buğu çözülür" tek klibe yazılmaz, A durumu bir klipte B
     durumu sonrakinde, değişim KESMEDE olur. Üç prompt da bunu KISIT
     olarak verir; doluluğun kaynağı olarak "klip içinde durum değişimi"
     öneren çözüm işaretlenip elenir. Doluluk HAREKET ve SÜREÇTEN gelir.
   • Tutulan durgunluk üçlüsü (nefes · sabit bakış hedefi · tek
     mikro-ayar) ve "still / motionless / frozen / does not move tek
     başına yazılmaz" (T15.2 #24 donmuş özne yanlılığı) → OYUNCULUK §4.
     2 ve 3 bunu SORMAZ; üçlünün kaç saniye taşıdığını sorar.
   • Tempo haritası Y/N/H (≥3 değişim · ardışık üç aynı harf yok),
     COST sonrası yavaş açılış → OYUNCULUK §4. 3 tempo dağılımını sormaz.
   • Aynı vuruş ardışık sahnede tekrarlanmaz · aynı klip kurguda iki kez
     kullanılmaz → D212. Sorulmaz.
   • Sahne SINIRI: açılan soru / cevap tipleri, sınır satırı → SAHNE_ZINCIRI
     §2-§5. 3 sınırı değil birimin İÇİNİ sorar.
   • Kırpma bütçesi, ASL eğrisi, örüntü kırıcılar, doruk öncesi rampa →
     KURGU_RITMI §1-§5; hook kırpması plana KIRPMA TABLOSU ile yazılır
     [D100]; klip süresi araçtan ölçülür [D124]. "Klibi kısa kes" bir
     KURGU kararıdır, bu turun sorusu değil; ızgara 48 × 10 s sabittir.
   • Efor fiili → gövde tepkisi (zorlanma kanalı ⑳) · niyet kanalı
     sözlüğü sekiz kanal → OYUNCULUK §3 · ⑳. 3 efor yazımını sormaz.
   • Kamera hareketi tipleri kapalı liste (fixed lockoff · push-in ·
     pull-back · slow orbit · tilt · lateral track · crane-rise · vertical
     track) → TEMPLATES. Kamera "dolgu" olarak yalnız bu listeden sorulur.
   • Hook'un ilk 10 s'si ve finalin son 10 s'si → HOOK · FINAL ·
     ACILIS_KAPANIS_CIFTI. Sorulmaz; 48 birimin ORTASI sorulur.
   • Timestamp promptu Veo kılavuzunda yalnız DİYALOG için geçiyor
     (`[00:03-00:08]`) — hareket için ölçülmedi; 1 bunu sorar, ZATEN VAR
     değildir.
   • Deponun ölçülmüş KARARLARI promptlarda kısıt olarak durur: tek sahne
     tek kilit, SAYIYLA (V3) · pozitif gövde 120-300 kelime (§7) · replik
     azlığı ve tek insan (§1) · yüzeyde okunur yazı yok [D34 · D45] ·
     "glow/bloom" yasak [D3 · D29] · "never hovering" çekirdek satırı.
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Motor 3. saniyeden sonraki damgayı okumuyor", "eylem bitince model
   donduruyor", "son vuruş fiil taşırsa klip dolar", "süreç fiili
   (hauling, crossing) noktasal fiilden (grabs, turns) iyi tutar",
   "ikinci görev boşluğu doldurur", "saati çalışan tutulmuş plan yeter"
   bu deponun TASARIM ADAYLARIDIR, kanıtlanmış yasa değil — üç prompt da
   İKİ YÖNLÜ yazıldı (tek vuruşlu 10 s'nin tuttuğu, eklenen işin gürültü
   olduğu, damganın çalıştığı ve çöktüğü vakalar da istenir). Üretim
   kısıtları hipotez değil FİLTREDİR ve her promptun beşinci cümlesinde
   açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 3 : 3'ün "bu fiil sınıfı 10 s taşır" dediği biçimi 1 "motor bunu
           3 s'ye yığıyor" diyorsa iki satır da ⬜ HİPOTEZ, sayısız iner;
           kılavuza yalnız İKİSİNİN de tuttuğu fiil biçimi iner.
   2 ↔ 3 : 2'nin zanaat zaman bütçesi (hazırlık/eylem/tepki/yerleşme
           saniyeleri) 3'ün iskeletiyle çelişirse iskelet 2'ye göre
           yeniden bölünür; 3'ün iskeleti tek başına inmez.
   1 ↔ 2 : 2'nin dolgu kaynağı (moving hold, ikincil eylem, çevre saati)
           1'e göre motorda ARIZA üretiyorsa (hover, döngü, kayan ayak)
           o kaynak "motorda yazılamaz" etiketiyle iner, kılavuza
           öneri olarak girmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Motor** — öne yığma, tamamlanınca ne yaptığı, damga uyumu, hareket sönümü, tarif biçimi | Damga yazılıyor ama klip 3 s'de bitiyor (hipotez a — ölçülmedi); Veo kılavuzu damgayı yalnız replik için biliyor; "then stops / nothing else moves" 43 promptta; üretilmiş klip hiç ölçülmedi | Kılavuz §4 MOTOR TARİF BİÇİMİ · §5 ÖLÇÜM eşiği (hareket_profili adayı) · TEMPLATES V3 kilit örneği · prompt_kontrol ㉛ adayının kelime listesi |
| 2 | **Zanaat** — moving hold, iş (business), ikincil eylem, çevre saati, tepki süresi, tutulan planın toleransı, 10 s'lik planın zaman bütçesi | Depoda bu kelimeler yok; SAHNE_ZINCIRI §1 "tek sürekli hareket" diyor ama neyin kaç saniye taşıdığını söylemiyor; tutulan durgunluk üçlüsü ⬜ 2,5 s hipotezi (T15.1 ④) | Kılavuz §3 DOLGU KAYNAKLARI tablosu · §2 ZAMAN BÜTÇESİ · OYUNCULUK §4'e işaretçi · ⑭ rubriği hareket-yokluğu satırı |
| 3 | **Senaryo birimi** — fiil sınıfı (noktasal/süreç), 10 s iskeleti, "geç gir erken çık"ın sabit klibe uyarlanması, ikinci görev, 48 birimde ölü sahne kontrolü | Son vuruşların %59'u durgunluk kelimesi taşıyor — plan son 3 s'yi kendi boşaltıyor (hipotez b); 00_SAHNE_TABLOSU'nda "son 3 s" hücresi yok; yazım anında ölü sahneyi yakalayan soru yok | Kılavuz §1 FİİL SINIFI · §2 10 s İSKELETİ · §6 ÖLÜ SAHNE KONTROLÜ · 00_SAHNE_TABLOSU sütunu · yeni-film sahne yazım adımı · ㉛ kapısının kuralı |

> ⚠️ **1 ile 3, 2 ile 3, 1 ile 2 birbirini denetler** (yukarıdaki çapraz
> okuma). Bir raporun getirdiği eşik ötekinde tutmuyorsa kılavuza ancak
> ⬜ HİPOTEZ etiketiyle iner, sayısız iner.

---

# 1️⃣ MOTOR — eylem üç saniyede bitiyor: video motorları on saniyelik klibin zamanını nasıl dağıtır

```
Yapay zekâ video motorlarının (Veo 3.1 ve Veo 3.1 Fast, Gemini Omni, Kling, Sora 2, Runway Gen-4, Wan, Hailuo ve benzerleri) tek promptla istenen bir eylemi 8-10 saniyelik klibe nasıl dağıttığını araştır: eylemin ilk saniyelere yığılıp erken tamamlanması (öne yığma), tamamlandıktan sonra öznenin ne yaptığı (donma, döngü, boş salınım, sürüklenme, uydurulmuş yeni eylem), hareket enerjisinin klip boyunca sönümü, görüntüden-videoya ile metinden-videoya arasındaki fark — benchmark ve değerlendirme çalışmaları (VBench dinamik derece ve zamansal tutarlılık, EvalCrafter, T2V-CompBench, zamansal prompt uyumu ölçen çalışmalar), sistematik topluluk ölçümleri ve motor belgeleri; motor sürümü, tarih ve kaynak ile.
Zaman damgalı tarif biçimlerinin uyumunu ölç: "0s — … 4s — … 8s —" satırları, "[00:03-00:08]" etiketleri, "first … then … finally" sıralaması, "throughout / for the whole clip" süre beyanı, hız ve oran beyanı ("one full swing every four seconds", "walks the length of the corridor in ten seconds"), başlangıç ve bitiş karesi çifti — hangi biçimin hangi zaman çözünürlüğünde tutulduğu, geç damgalara uyumun erken damgalara göre düşüp düşmediği, vuruş sayısının (iki ile beş) sonucu değiştirip değiştirmediği, ölçülmüş ya da sistematik gözlemlenmiş; iki yönlü — damganın çalıştığı belgelenmiş vakalar ile çöktüğü vakalar, kaynak ve tarihle.
Fiil ve cümle biçimini sök: süreç fiilleri ("keeps hauling", "walks the length of", "works the seal loose") ile noktasal fiiller ("grabs", "turns", "notices") arasında hareketin klibin son üçte birine taşınma farkı, "continues / does not stop / at the same rate" gibi devam beyanlarının etkisi, ikincil hareket cümlelerinin (nefes, kumaş, kayış, toz, gölge) ve kamera hareketi cümlesinin ana eylem bitince kadrajı canlı tutup tutmadığı ve bunun ölçülmüş bedeli (sürüklenme, morfoloji bozulması, fazla uzuv, kayan ayak, döngü artığı, zorlanınca "havada süzülme"), hangi kelimelerin donmuş özne yanlılığını ("still", "motionless", "holds") hangilerinin aşırı hareketi tetiklediği — motor ve tarihle.
Uygulayıcı tarafını topla: yapay zekâ ile kısa film üreten yönetmenlerin, prompt kılavuzlarının ve motor belgelerinin "karakter işi bitirip öylece duruyor" sorunu için verdiği belgelenmiş çözümler — eylemin ortasından seçilen başlangıç karesi, uzatma (extend) zinciri ile kısa klip, negatif promptun harekete etkisi, tohum ve rehberlik ayarları, 10 s yerine 5-8 s üretip kurguda kullanma, promptun sonuna yazılan "kapanış durumu" cümlesi — her çözümün hangi motorda, hangi tarihte, ne oranda işe yaradığı ve neyi bozduğu.
Kritik kısıt: hedef klipler on saniyelik kesmesiz sabit kamera planlarıdır (varsayılan kilitli tripod, kamera hareketi kapalı bir listeden), her klip onaylı bir başlangıç karesinden görüntüden-videoya tek promptla üretilir ve başka belgeye atıf yapamaz, pozitif metin bandı dardır, her sahnede tek bir sayılı hareket kilidi vardır, klip içinde durum değişimi (kapak açılır, lamba yanar) ölçülmüş olarak güvenilmezdir ve kesmeye yazılır, karakter çoğunlukla tek ve sessizdir, kadrajda okunur yazı ve HUD bulunamaz, "still / motionless / frozen" kelimeleri tek başına yasaktır, klip süresi araçtan gelir ve 10 s sabittir — bu yüzden daha kısa klip, ikinci karakter, replik, ara kesme, kadraj değişimi, çok planlı prompt ya da klip içi durum değişimi öneren çözümleri işaretleyip ele; tek bedenle, sabit kamerayla, kilitli 10 s'nin SON DÖRT SANİYESİNİ canlı tutan biçimleri öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) MOTOR ZAMAN DAVRANIŞI tablosu — motor, sürüm ve tarih, öne yığma gözlendi mi, tamamlanınca ne yaptığı, damga uyumu ve çözünürlüğü, hareket sönümü, görüntüden-videoya farkı, kaynak ve etiket; (b) TARİF BİÇİMİ tablosu — biçim, 5-10. saniyeye etkisi, artefakt bedeli, motor, İngilizce tek satırlık kalıp, kaynak ve etiket; (c) ARIZA tablosu — arıza (donma, döngü, boş salınım, uydurulmuş eylem, sürüklenme, süzülme), tetikleyen tarif, önleyen tarif, motor, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ ZANAAT — sabit uzunlukta bir planı ne doldurur: ana eylem bitince göz kadrajda neden kalır

```
Yönetmenlik ve blocking, kurgu, animasyon ve reklam yapımı pratiğinden, sabit uzunluktaki bir planı ana eylem bittikten sonra neyin doldurduğunu topla: sahne işi (stage business), ikincil eylem, örtüşen eylem ve izleyen hareket (overlapping action, follow-through), yerleşme ve "hareketli tutuş" (moving hold), tepki vuruşu, hazırlık (anticipation), planın sonunda cevaplanan soru, gerekçeli kamera hareketi, kadrajdaki çevre saati (sallanan kayış, damlayan su, yürüyen gölge, dönen çark), giriş ve çıkışlar — yönetmen, kurgucu, animasyon ilkesi metinleri (Disney'in on iki ilkesi, Richard Williams ve benzerleri), saniyesine kadar yazılan 6-10-15 saniyelik reklam filmleri, uzun plan ve yavaş sinema pratiği; kaynak, tarih ve tür ile ve her öğenin ekranda KAÇ SANİYE taşıdığı.
Tutulan planda izleyici dikkatini ölç: görünür bir işi olmayan bir beden karşısında izleyicinin dikkatinin kaç saniye sonra özneyi terk ettiği (film üzerinde göz izleme çalışmaları, ortalama plan süresi ve izlenme literatürü, kurgu yazınındaki "ölü zaman", animasyondaki tutuş uzunluğu kuralları — kaç kareden uzun tutuş "ölü" okunur), hangi mikro-olayların dikkati sıfırladığı (nefes, bakış kayması, ağırlık aktarımı, el ayarı, ses), saati çalışan tutulmuş plan ile saatsiz tutulmuş plan arasındaki fark — hakemli ölçüm ile uygulayıcı pratiği ayrı sütunlarda, örneklem ve etki büyüklüğüyle.
On saniyelik bir planın zaman bütçesini uygulamadan çıkar: storyboard ve animatik zamanlamasının (exposure sheet, beat board, timing chart) hazırlık-eylem-tepki-yerleşmeyi saniyeye nasıl böldüğü, reklam yönetmeninin on saniyelik birimi nasıl yazdığı, animatörün 240 karelik planı nasıl paylaştırdığı, bir tepkinin ekranda kaç saniye tutulduğu, on saniyeye kaç vuruş sığdığı, oyuncuya verilen "ikinci görev"in ne olduğu; iki yönlü — durgunluğun İÇERİĞİN kendisi olduğu ve işe yaradığı belgelenmiş planlar (tutulan tepki, dehşet, saatli bekleyiş) ile eklenen işin gürültüye dönüştüğü eleştiri vakaları, eleştirinin kendi sözcükleriyle.
Tek beden, replik yok, sabit kamera hâlini ayrıca sök: sessiz sinema ve fiziksel komedi işi (Keaton, Tati ve benzerleri), pandomim ve dans zamanlaması, tek planlı portre ve gözlemci belgesel, ekranda prosedürel iş (tamir, yemek, zanaat, ip düğümü) — yalnız bir çalışanı on saniye boyunca okunur ve canlı tutan şeyin ne olduğu: görünür ilerlemesi olan iş, direnç (ağırlık, sürtünme, takılma), alet kullanımı, nefes, ikinci deneme, sonuçla ilişkisi; kaynak ve mekanizmayla.
Kritik kısıt: hedef, yapay zekâ ile üretilen on saniyelik kesmesiz sabit kamera planlarıdır, karakter çoğunlukla tek ve sessizdir, klip içinde kesme ve kurgu kurtarması yoktur ve ızgara 48 × 10 s sabittir, kamera hareketi kapalı bir listeden seçilir, klip içinde durum değişimi (nesne belirir ya da kaybolur, kapak açılır) ölçülmüş olarak güvenilmezdir ve bu yüzden doluluk HAREKET ve SÜREÇTEN gelmek zorundadır, bütün klip için pozitif metin bandı yaklaşık iki yüz kelimedir, kadrajda okunur yazı yoktur, "still / motionless / frozen" tek başına yazılmaz — bu yüzden çok karakterli iş, replik, beliren ve kaybolan aksesuar, yeniden kadrajlayan kesme, ara plan (insert) ve klip içi durum değişimi öneren çözümleri işaretleyip ele; tek cümlenin emredebildiği ve sabit kameranın gösterebildiği öğeleri öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) DOLGU KAYNAĞI tablosu — öğe (moving hold, sahne işi, ikincil eylem, çevre saati, tepki, kamera hareketi ve benzeri), tek başına taşıdığı saniye, mekanizma (göz neden kalır), gürültüye dönme riski, İngilizce tek satırlık yazılabilir kalıp, kaynak ve etiket; (b) ZAMAN BÜTÇESİ tablosu — on saniyelik planın bölünmesi (hazırlık / eylem / tepki / yerleşme ya da süreç / kesinti / sonuç), her parçanın saniyesi, hangi pratikten, kaynak ve etiket; (c) TUTULAN PLAN tablosu — tutulan plan tipi, içinde ne çalışır (saat), tolerans saniyesi, hangi koşulda "ölü" okunur, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ SENARYO BİRİMİ — on saniyelik sahne nasıl yazılır: fiil sınıfı, birim iskeleti, kırk sekiz birimde ölü sahne kontrolü

```
Sabit uzunluktaki birimler için senaryo ve storyboard yazım pratiğini topla: on saniyelik bir birimin mikro-yapısı (sıfırıncı saniyede açılan soru, onuncu saniyede cevaplanan ya da ertelenen soru), "geç gir, erken çık" ilkesinin sabit uzunluktaki klibe uyarlanması (kesme eylem hâlâ sürerken düşer, sonraki birim eylemin sonrasından başlar), vuruş biriminin tanımı ve on saniyeye kaç vuruş sığdığı, birimin ortasına yerleştirilen kesinti ya da komplikasyon, sonuç vuruşu — senaryo kılavuzları, storyboard sanatçıları, animasyon hikâye departmanları, reklam senaryosu, dikey kısa dizi yazımı ve çizgi roman panel zamanlaması (McCloud ve benzerleri); kaynak, tarih ve tür ile.
Fiilin dilbilimini ekran zamanına bağla: sözlüksel görünüş sınıfları (Vendler: durum / etkinlik / tamamlama / erişme; telik ile atelik; noktasal ile süreli) ve her sınıfın ekranda kaç saniye taşıdığı — "turns", "grabs", "notices", "reaches" gibi bir anda biten fiiller ile "hauls", "crosses", "works the seal loose", "climbs the ladder" gibi görünür ilerlemesi olan fiiller arasındaki fark, senaryo eylem satırının bir erişmeyi nasıl tamamlamaya çevirdiği (direnç, aşamalar, alet, mesafe, ağırlık), senaryo biçimi araştırmalarının ("bir satır bir saniye" kuralı) ve animatik zamanlamasının fiil seçiminin plan süresini nasıl öngördüğüne dair kanıtı; ölçülmüş ve uygulama ayrı sütunlarda.
Sahneyi ilerlemesi görünen bir iş olarak yazmayı sök: prosedürel ve yetkinlik yazımı (tamir, geçiş, geri sayım, mühürleme), bir işin ekranda görünen aşamaları, kısmi tamamlama ve ikinci deneme, birimin içindeki direnç ve bedel, aynı anda süren birincil ve ikincil görev, sıfırıncı saniyede ekilip dokuzuncu saniyede ödeyen tohum; iki yönlü — tek vuruşlu on saniyenin saf tutuş olarak çalıştığı belgelenmiş planlar (tepki, dehşet, saatli bekleyiş) ve onları çalıştıran koşullar ile "iş ekleme"nin sahneyi bozduğu vakalar.
Kırk sekiz birimlik tasarımı sor: 48 × 10 s'lik bir senaryonun hareketli birimlerle tutulan birimleri nasıl sıraladığı, storyboard ve animatik ekiplerinin üretimden önce "ölü paneli" nasıl yakaladığı (zamanlama geçişi, panelin oynanarak okunması, saatli animatik), senaryo aşamasında ölü planı öngören kontrol sorularının neler olduğu (görünür ilerleme yok, yalnız noktasal fiil, ikinci görev yok, çevre saati yok, sonuç yok), reklam ve animasyon stüdyolarının bir paneli hangi gerekçeyle reddettiği; ve yapay zekâ dönemi pratiği — 8-10 saniyelik üretimler için klip başına senaryo yazan yapımcıların klip şablonları ve doluluk için bildirdikleri yöntem, kaynak ve tarihle.
Kritik kısıt: birimler tam on saniyedir ve kırk sekizi hook dâhil sekiz dakikalık bir film yapar, her birim onaylı bir başlangıç karesinden tek promptla üretilen kesmesiz sabit kamera klibidir, karakter çoğunlukla tek ve sessizdir, klip içinde durum değişimi ölçülmüş olarak güvenilmezdir ve değişim birimler ARASINA yazılır, her birimde tek bir sayılı hareket kilidi vardır, tempo haritası (yavaş / normal / hızlı, en az üç değişim, ardışık üç aynı yok) ve ardışık aynı vuruş yasağı zaten vardır ve sorulmuyor, hook ve final kılavuzları zaten vardır ve sorulmuyor — bu yüzden replikle taşınan birim, birim içi montaj, değişken klip süresi, ara plan, ikinci karakter ve klip içi durum değişimi öneren çözümleri işaretleyip ele; üretimden ÖNCE bir senaryo kontrolünün uygulayabileceği yazılabilir birim iskeleti ve fiil kuralını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) FİİL SINIFI tablosu — sınıf, İngilizce örnekler, tek başına taşıdığı ekran saniyesi, bittikten sonra bedenin ne yaptığı, süreli biçime yeniden yazım kalıbı (İngilizce), kaynak ve etiket; (b) ON SANİYE İSKELETİ tablosu — iskelet çeşidi (hazırlık / ilerleme / sonuç, kesintili süreç, tohum ve ödeme, saatli tutuş ve benzeri), saniye bölünmesi, son üç saniyenin ne gösterdiği, hangi sahne tipinde kullanıldığı, İngilizce tek satırlık kalıp, kaynak ve etiket; (c) ÖLÜ SAHNE KONTROLÜ tablosu — senaryo aşamasında sorulan soru, "hayır" cevabının neyi öngördüğü, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

## ⬜ ARAŞTIRMA BEKLEMEDEN YAPILABİLECEKLER — sahip kararı, hiçbiri yapılmadı

> Aşağıdakiler TUR 19'un cevabına bağlı DEĞİL; teşhisin ①-④ satırından
> doğrudan çıkıyor. Kılavuz yazılırken yeniden sıralanır; sahip "yap"
> demeden hiçbiri depoya girmez.

```
1. HAREKET PROFİLİ (makine kapısı adayı)  ⬜
   hareket_profili.sh <klip|master> [klip süresi] — ffmpeg kare farkı ile
   saniye başına hareket enerjisi; her 10 s'lik klipte eşiğin altında kalan
   ARDIŞIK saniye sayısı = "ölü saniye". Bugün üretilmiş klibin doluluğu
   HİÇ ölçülmüyor (teşhis ④); prompt sayıları klibi temsil etmiyor.
   Eşik TUR 19 §1'den (motor sönüm eğrisi) kalibre edilir; betik önce
   sayıyı basar, eşiği sonra alır. sahne_kapisi.sh kalıbı.

2. ㉛ DOLULUK KAPISI (prompt_kontrol · yalnız yeni rejim)  ⬜
   TIMELINE'ın t ≥ 7 s vuruşlarında en az bir gövde fiili yoksa → FIX;
   "still / motionless / frozen / then stops / nothing else moves" cümlede
   tek başına → FIX (OYUNCULUK §4 bunu ⛔ diyor, kapısı yok; ölçüm %59).
   Fiil listesi TUR 19 §3 FİİL SINIFI tablosundan gelir; o gelene kadar
   doluluk_olcum.py'nin GUCLU listesi geçici sözlüktür.

3. TEMPLATES V3 KİLİT ÖRNEĞİ  ⬜
   "turns exactly one quarter, then stops, and nothing else in frame
   moves" → ORAN kilidine çevrilir ("completes one full swing every four
   seconds" — aynı dosyadaki ikinci örnek zaten öyle). Tek satır; ama
   yeni-film bu örneği kopyalıyor.

4. 00_SAHNE_TABLOSU SÜTUNU  ⬜
   "SON 3 s" hücresi: sahnenin 7-10. saniyesinde beden ne yapar (fiil).
   Hücre boşsa ya da fiil noktasalsa sahne yazılmadan yakalanır; ㉚ zaten
   tabloyu sayıyor, sütunu da sayabilir.

5. ⑭ HAREKET RUBRİĞİ — ilk koşudan ÖNCE  ⬜
   MOTION LEDGER'a hareket YOKLUĞU satırı (in–out · "no purposeful motion"
   · saniye). ⑭ amaçsız hareketi etiketliyor, boş saniyeyi değil; kategori
   adları ilk koşuyla donar, o yüzden pencere şimdi.

6. BÖLÜM SAYISI — yatay_8_dk_filmler/README 2 × 24 diyor, sahip 4 × 12 dedi  ⬜
   Karar: (a) README kalır, 4 modül 2 bölüm dosyasına yazılır ·
   (b) README 4 × 12'ye açılır (film_klasoru_ac.sh bölüm sayısı, QA birimi
   çeyrek master?, --bolum n/4, sayac). Film yazılmadan karar gerekir.
```
