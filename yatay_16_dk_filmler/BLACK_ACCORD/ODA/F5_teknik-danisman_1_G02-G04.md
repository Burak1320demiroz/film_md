<!-- teknik-danisman (sonnet) · F5 tur 1 · eser PROMPTLAR/G02.md · G03.md · G04.md (ilk sürüm) · risk sütunu dolu 14 çekim · 18.10.2026 · ajan cevabı aynen -->

Faz 5 tur 1, teknik-danisman. Kapsam: BLACK_ACCORD G02 · G03 · G04, FILM.md §4'te risk sütunu dolu 14 çekim (C13 C17 C23 · C25-C29 C31 · C37 C38 C40 C45 C47). Dosyamda numaralı soru listesi yok. Yazarın "8 SORU" tabloları soru-cevap olarak ayrıca değerlendirilmedi.

### B1 · CİDDİ · 10 s klip, Frames to Video ile varsayılıyor
YER       G02-G04 bütün Video blokları (7-10 s vuruşu) · FILM.md satır 8 `KLIP_SURESI ölçülmedi`
KANIT     `7-10 s: The drift eases closer and the gold light slides along his bronze armour…` (C13). `uretim_hatti/FLOW_GERCEKLERI.md:30`: Frames to Video "4 · 6 · 8 s". Satır 180: "Aracın verdiği 10 s klip" → ÇÜRÜTÜLDÜ. Satır 164: P14 ölçülecek.
ETKİ      Flow'dan 8 s gelirse her promptun son vuruşu kesilir. C23'te kaldırılan levhanın duruşu, C38'de ışığın üçüncü atımı, C40'ta itişin sönümü kaybolur.
DOĞDUĞU   araç
KURAL     FLOW_GERCEKLERI.md:164 [ARAÇ] · SMOKE P14
ARIZA     yeni (mod ↔ model)
DÜZELTME  P14 ölçülmeden G02-G04 video gönderme. 8 s çıkarsa her promptta son iki vuruşu birleştir: `6-8 s: … as the drift eases closer.` Replikler ≤5 s olduğu için ses payı güvende.

### B2 · CİDDİ · C23: levhanın alınması kadrajda ve düz masada
YER       C23 Video 0-6 s · Görsel
KANIT     `lies flat on the table surface in front of Silex's seat` · `The hand slips beneath the edge of the slab and lifts it slowly until it rests flat on the open palm`
ETKİN     El ile levha kaynaşır. Masaya yatan düz bir levhanın altına el sokulamaz, model bu hareketi eritir. Bu T01'in en kötü hâlidir: temas anı ana eylem.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR §B sıra 1 (temas anı gösterilmez, an kesmeyle atlanır) [ARAÇ]. Planın kendi çözümü: "kesmeyle sadeleşir".
ARIZA     T01
DÜZELTME  Notta yazılı YEDEK'i varsayılan yap. Alma anı C22→C23 kesmesinde kalır.
          Görsel: `lies flat on the table surface … a hand's width to the right of the slab` → `rests on the open right palm a hand's width above the table surface` (C25 başlangıç karesiyle aynı poz).
          Video: `as the open right hand glides along the table surface toward the … slab` → `while the open right palm holds the … slab level`
          `3-6 s: The hand slips beneath … lifts it slowly …` → `3-6 s: The palm holds the slab level`
          Bu C25 başlangıcına doğrudan bağlanır.

### B3 · CİDDİ · C28: küpü çekmek 0-7 s boyunca parmak temasıdır
YER       C28 Görsel + Video 0-7 s
KANIT     `the fingertips of his right hand rest against the far edge of the octagonal body` · `his right hand slides back across the table, drawing the palm-sized black octagonal body toward his seat`
ETKİN     Nesne eline yapışır ya da el nesnenin içinden geçer. Parmak uçları uzak kenarda olduğu için çekmek bir kavrama gerektirir, "kavrama yok" notuyla çelişir.
DOĞDUĞU   hareket
KURAL     BILINEN_TUZAKLAR §B sıra 1 [ARAÇ]. Plan: "karmaşık parmak hareketi gerekirse kesmeyle sadeleşir".
ARIZA     T01 · T09 (K1)
DÜZELTME  Çekme C27→C28 kesmesinde olur (C27 kadrajında K1 yok). Görsel: `a forearm's length in front of his seat` → `a hand's width in front of his seat`.
          Video: `his right hand slides back across the table, drawing the … octagonal body toward his seat` → `his right hand rests against the far edge of the octagonal body`.
          4-7 s'deki `comes to rest on the table close in front of him` cümlesini çıkar.

### B4 · CİDDİ · C17: altı figürden beşinin kafası promptta yok, hareket fazla
YER       C17 Görsel + Video 4-10 s
KANIT     Görsel: `At the far head chair, Nith wears a long ivory formal coat…`, `At the bronze-red chair position, Vekh wears bronze formal military armour…`, Silex ve Orun için de yalnız giysi. Video: `Nith turns his head … Ishra's shoulders ease … Vekh's bronze armour catches the gold light … Nem's shoulders rise and fall … Orun's amber eyes move`
ETKİN     Yüzsüz küçük figürlerin kafaları referanssız (yüklenen yalnız 7 ve 8) uydurulur. Aynı kadrajda beş eşzamanlı mikro hareket altı figürü klonlar ya da kaynaştırır. Orun'un gözleri o ölçekte okunmaz.
DOĞDUĞU   metin
KURAL     BILINEN_TUZAKLAR §B sıra 9 [ARAÇ]; ARIZA T15
ARIZA     T15
DÜZELTME  Her figüre bir kafa cümlesi ekle, aynı uzunlukta:
          `Nith wears` → `Nith, with a polished jet-black head and one bone-white brow ridge, wears`
          Vekh: `a rust-red armoured head`
          Silex: `a frosted amethyst faceted head`
          Orun: `a moss-green layered head`
          Video: `and Orun's amber eyes move toward the far head chair` çıkar. En çok iki figür hareket etsin (Nith başı, Nem nefesi); Ishra ve Vekh yalnız ışık alsın.
          Reference 8 çıkarılabilir: kara delik zaten Reference 7'nin camında, istasyon sızma riski de biter (ref sayfası 8 istasyon içerir).

### B5 · CİDDİ · C37: "diagram" kelimesi yazı ve rakam çağırır
YER       C37 Görsel, ilk cümle
KANIT     `Extreme close detail of a minimalist comparison diagram made only of thin glowing lines and bars on plain unmarked surfaces`
ETKİN     "diagram" modele eksen etiketi, sayı ve çentik çağrıştırır. Yazılar sonradan eklenecek, kare yeniden üretilirse bütçe gider.
DOĞDUĞU   metin (prompt kelimesi)
KURAL     BILINEN_TUZAKLAR §B sıra 2, §C (prompt kelimesi kadraja basılır) [ARAÇ]
ARIZA     T06
DÜZELTME  `a minimalist comparison diagram made only of thin glowing lines and bars on plain unmarked surfaces` → `two thin glowing light bars and one fine hairline on a plain unmarked matte near-black surface`
          Video'daki `Sound: quiet chamber ventilation…` salon sesidir, grafik çekiminde yersiz. Yatağı kurguda ver (not zaten Y1 diyor).

### B6 · CİDDİ · C45: kılıf masa kenarının üstünde isteniyor
YER       C45 Görsel
KANIT     `At the lower frame edge just above the table rim, the holstered blaster remains closed in its holster at his right hip.` + `Vekh seated … behind the black hexagonal table … hands are below the crop`
ETKİN     Oturan birinin kalçası masa kenarının altındadır. Model silahı masaya koyar ya da çıkarır. C59'daki "çekilir" anı önceden bozulur (T09). Silah cümlesi iki kez geçtiği için salience artar.
DOĞDUĞU   kare
KURAL     Planın kendi notu: "masa kenarı üstündeki konum üretimde sorgulanır" (G04 C45 notu) · BILINEN_TUZAKLAR §B sıra 5
ARIZA     T09
DÜZELTME  `At the lower frame edge just above the table rim, the holstered blaster remains closed in its holster at his right hip.` cümlesini sil. Kılıf zaten giysi cümlesinde; görünürlük C13'ün köşe kadrajında kanıtlandı. İstenirse C13 kadrajı tekrarlanır.

### B7 · KÜÇÜK · C40 ve C31: disk yaylarına "hareket" yazılmış
YER       C40 Video 3-7 s · C31 Video 7-10 s
KANIT     `the lensed golden arcs glide slowly past the dark shadow in parallax` (C40) · `the lensed golden arcs of the disk shift slowly behind the formations` (C31)
ETKİN     Diskin şekli 10 s içinde bozulur ya da kara delik ikinci kez belirir. Hareketi yalnız kamera taşımalı.
DOĞDUĞU   hareket
KURAL     — · ARIZA T18 (tek kara delik)
ARIZA     T18
DÜZELTME  C40: `glide slowly past the dark shadow in parallax` → `hold their shape around the dark shadow`
          C31: `shift slowly behind the formations` → `hold steady behind the formations`; `tiny medical craft drift a little within the corridor` → `tiny medical craft wait at the corridor edge`.
          C31 sonundaki `no atmospheric engine or explosion sound` plan cümlesi birebir; model sesi kurguda atılacağı için Y2 yatağı zorunlu.

### B8 · KÜÇÜK · C38: "sönük ışık" karede görünmez
YER       C38 Görsel + Video 0-3 s
KANIT     `one small signal light on its bow, still unlit` · `the small signal light on its bow switches on and pulses once`
ETKİN     Aşırı geniş planda sönük küçük bir ışık çizilmez. Video var olmayan bir ışığı yoktan yakar (belirip kaybolma).
DOĞDUĞU   kare
KURAL     —
ARIZA     T09
DÜZELTME  `still unlit` → `glowing very faintly`; `switches on and pulses once with a steady pale amber glow` → `brightens and pulses once with a steady pale amber glow`.

### B9 · KÜÇÜK · C47: K1 yumuşak odakta ve itiş altında
YER       C47 Görsel + Video
KANIT     `In the soft-focus lower frame-left foreground … a single palm-sized black octagonal body` · `the pale amber triangular light … stays steady in the foreground` + push
ETKİN     Odak dışındaki ön plan nesnesi kamera ilerlerken şekil değiştirir. K1 referanssız, okunması gereken geri dönüş nesnesi. Sekizgen mi beşgen mi belli olmaz (K1 ↔ K2).
DOĞDUĞU   kare
KURAL     —
ARIZA     T09
DÜZELTME  `soft-focus lower frame-left foreground` → `sharp lower frame-left foreground`. Nem arkada net kalır, itiş `very small push` olur (`A gentle push` yerine).

### B10 · KÜÇÜK · C26 ve C25: konuşmayan 4 s'de model sesi
YER       C26 0-4 s · C25 0-10 s
KANIT     `whose mouth stays closed as his short rigid jaw plates tighten` (C26) · `the mouth seam staying closed` (C25)
ETKİN     Ses AÇIK film. Modelin ağız kapalı yüze kendi nefes ya da sesini koyma olasılığı var; R043 ve R045 kurguda binecek.
DOĞDUĞU   ses
KURAL     BILINEN_TUZAKLAR §B sıra 3, 11 [ARAÇ]
ARIZA     T13
DÜZELTME  Prompt değişmez. Kurguda C26 0-4,4 s ve C25'in tamamı ambians + R043/R045 ile ezilir. R043 (`We request a pause to recover our dead.`) Ishra'nın yeni cümlesi: model aynı sesi başka klipte veremez, planda yedek kayıt görülmedi. Cümlede `dead` var (BT §A kelime listesi): R043 video promptunda değil, kurguda kalmalı.

### B11 · KÜÇÜK · C29 → C28 bakış yönü eksik
YER       C29 Görsel
KANIT     `her gaze fixed on a point off-camera toward Orun's seat`
ETKİN     Kare yönü (frame-left/right) seçilmiyor. C28 Orun'un tepki kadrajıyla bakış ekseni uyuşmayabilir (jump cut).
DOĞDUĞU   kare
KURAL     —
ARIZA     yeni (kesme sürekliliği)
DÜZELTME  Kare onayında yön `toward frame-left/right` ile sabitlenir; C28 3/4 sağ önden → C29 tersi yön olmaz.

### B12 · KÜÇÜK · C27: iki şakak görünür
YER       C27 Görsel
KANIT     `seen almost head-on from across the table with both temples visible` · `receiver is fixed at the right temple`
ETKİN     Simetri çekimi alıcıyı sol şakağa da koyar (A12: tek alıcı).
DOĞDUĞU   kare
KURAL     —
ARIZA     T05
DÜZELTME  `with both temples visible` → `with the right temple toward frame-left`.
          `shelled` ve `weapons` (C27, C29) BT §A listesinde yok, HİPOTEZ: red gelirse yalnız o replik kayda geçer. Red durumunda lipsync için aynı hece sayılı `struck` ile ağız animasyonu üret, sesi kurguda koy.

KORU: C13 `avuç yukarı, parmaklar gevşek kıvrık` başlangıcı ve kılıfın sağ kalça köşe kadrajı (el çevirme yok); C23 Not'taki YEDEK; C25'in dinleme-hâli (ağız kapalı, replik yok); C37 çubukların eşit-kısa başlangıcı. Bu dördü doğru.

Temiz bulunan kontroller (promptlardan okundu): T03/T13 (C31 C38 C40 yalnız plan DIŞ ses cümlesi; vakumda toz/duman yok) · T05 su başlığı sabit (Ishra çekimleri C14 C19 C34 C44) · T08 tek rejim · T10/T02 zor beden hareketi yok · meta etiket, büyük harfli jeton, çekim kodu yok · açılış (C01-C03) bu listede değil · her blok ≤4.300 karakter (en uzun C17 ≈ 3.100).

KAPSAM DIŞI: FILM.md §4 C17 satırındaki "Taraf / yön" sütunu dış master metni taşıyor ("dört filo ayrı gruplar… A08 · A09"), salon çekimi için kopya hatası.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 5 (B1-B6 içinde B1 B2 B3 B4 B5 B6) · KÜÇÜK 6 (B7-B12)
KARAR    TUR KAPANABİLİR (ÖLÜMCÜL yok; B1-B6 yazar KABUL/RED ile cevaplamalı)
GİRDİ    FILM.md §1-§4 ve §5 (R043 R045 R047 R051 R067 R068 satırları) · PROMPTLAR/G02.md · G03.md · G04.md (tamamı) · ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md T bölümü · ILK_30_SANIYE_KILAVUZU.md §6 başlığı · FLOW_GERCEKLERI.md satır 29-31, 160-164, 180 · NOTLAR.md ve SAHNELEME.md içinde R043 araması (sonuç yok).
YAPILMADI  Kare sayfası görülmedi; hiçbir hareket için "tuttu" denemez, hepsi "görülmedi". Öteki eleştirmenlerin ODA dosyaları okunmadı (bağımsızlık). Dosya yollarındaki tam süre ölçümü (ffprobe) yapılamaz; B1 P14'e bağlı.
