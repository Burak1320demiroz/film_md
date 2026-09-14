# 🎭 OYUNCULUK YAZIM KILAVUZU — Niyet, Seçim, Bedel ve Sonrası BEDENE Nasıl Yazılır

> **Neden var (11.09.2026):** ⑩ OYUNCULUK merceği koşulan on filmin onu
> 2,0-6,3 bandında; dördü `THE CHOICE IS INVISIBLE` (Counted Turn 3,4 ·
> Bent Grass 4,6 · Green Ceiling 5,2 · Cracked Helmet 2,0). Tekrar eden
> desen hep aynı: manken · görev-var-niyet-yok · seçim anında değişmeyen
> gövde · kesmede sıfırlanan beden · nedensiz dolgu jesti (D202 ·
> ADAY-26/41/84/85). D202'nin çözümü tek cümleydi: *"mikro-beden
> hareketleri zorunlu yazılmalı."* Hangi kanal, hangi sayı, hangi sahneye,
> nereye — yazılı değildi. EFOR için bu sözlük var (D169 yedi kanal +
> betik ⑳); NİYET için yoktu. Bu dosya ⑩ rubriğinin **yazım tarafıdır**:
> rubrik ne okuyorsa, burası onu yazdırır. (`SES_VE_DIYALOG` ↔ `3_SES`
> nasıl çiftse, `OYUNCULUK_YAZIM` ↔ `10_OYUNCULUK` öyle çifttir.)
>
> **Ölçülmüş kök sebep:** deponun TIMELINE biçimi NEREDE ve NE'yi yazıyor
> ("2s — presses one button"), NASIL ve NEDEN'i hiç sormuyor. D169 bunu
> efor için ölçtü; niyet için aynı boşluk. Model yazılanı üretiyor: iş
> yapılıyor, kimse istemiyor.
>
> **Ne zaman okunur:** sahne çalışma dosyası yazılırken (`05_SAHNE_CALISMALARI`)
> ve TIMELINE yazılırken — her sahnede. QA_SPEC yazılırken ÇAPA ÜÇLÜSÜ (§2).
> `KARAKTER_KARTI_VE_DAVRANIS` §1 kartı önce yazılmış olmalı: kart NEYİ,
> bu dosya NASIL.
>
> **Kaynak:** `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 15
> (T15.0 · T15.1 ①② · T15.2 #15-24) + `10_OYUNCULUK` rubriği + D169 · D179 ·
> D202 + gözlem defteri adayları. Dış sayılar ETİKETLİDİR.

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① BU DOSYA EFOR DEĞİLDİR. D169 / ⑧ EFOR "beden ÖDEDİ mi" sorar; burası
   "beden İSTEDİ mi". Aynı sahne ikisinde de düşebilir — iki eksen, çifte
   fatura değil (kart F6 SINIR notu). Efor sözlüğü D169'da kalır ve
   buradan yalnız ATIF alır.

② BU DOSYA BÜTÇE DEĞİLDİR. Göz/el/nefes/yürüyüş YÜZDELERİ KARAKTER_VE_DUYGU
   §1-§6'dadır. Burası o bütçenin içine ne YAZILACAĞINI söyler.

③ SAYILAR İKİ SINIFTIR (T15.0):
   İZLEYİCİ EŞİĞİ  "izleyici X s'den sonra tereddüt okur" — etiketli
                   (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ · ⬜); ilk ⑩ mod D'de sınanır
   YAZIM SAYISI    "el mandaldan bir avuç uzakta iki saniye durur" — bu bir
                   iddia değil TASARIMDIR; D169'un "sayı yaz, sıfat değil"
                   kuralı gereği serbestçe verilir. Yazım sayısı bir eşiğe
                   dayanıyormuş gibi OKUNMAZ.

④ YÜZ ÇOĞU SAHNEDE YOKTUR ve bu bir kusur değildir (⑩ kanal kaydı:
   yüz "unavailable" → kat. 1 N/A). Bu dosya gövde/el/baş/tempo/mesafe
   yazar; yüz yalnız §7'de, vizör berrak CU'da.

⑤ MÜHÜR KORUNUR [D175]: hiçbir cümle eldiven/yaka/bot sınırında ANATOMİ
   tarif etmez ("tendons through the glove" çıplak deri üretti). Bütün
   kalıplar GİYSİ YÜZEYİNE yazılır: eldiven segmenti, kol kumaşı, omuz
   plakası, kask.

⑥ DAHA FAZLA OYUNCULUK DAHA İYİ DEĞİLDİR (⑩ desen ⑪): küçük ana büyük jest
   yazmak, hiç yazmamak kadar hatadır. §6 orantı kuralı her kanalı bağlar.

⑦ YENİ YASAK YOKTUR. Tek "yazılmaz" listesi §6'daki dolgu jestleridir ve
   o liste ölçülmüş arızadan (ADAY-85 · ⑩ desen ⑨) gelir.
```

---

# 1. ✍️ CÜMLE TESTİ — yazım anında, TIMELINE'dan önce

**Rubriğin tek yöntemi:** her sahne için izleyicinin söyleyeceği CÜMLE —
*"bu figür ne İSTİYOR / ne HİSSEDİYOR"* — önce ekrandan yazılır; cümle
"X yapar"sa sahne **TASK ONLY**'dir. Yazım tarafında aynı test TIMELINE'dan
ÖNCE koşulur:

```
SAHNE ÇALIŞMA DOSYASINA (her sahne · 05_SAHNE_CALISMALARI/Snn.md):
  İZLEYİCİ CÜMLESİ:  "⬜"   — 'seems / probably / sanırım' YASAK; gerekiyorsa
                             cümle en iyi hâlde PARTIAL'dır, yeniden yazılır
  TAŞIYAN KANAL:     ⬜ (§3 sözlüğünden 1-2 kanal — üçten fazla yazılmaz)
  TASK ONLY MU:      ⬜ evet/hayır — evetse BİLİNÇLİ mi (şeritte G harfi)

KOTA: TASK ONLY sahne sayısı ≤ sahne sayısının yarısı (KARAKTER_KARTI §4
şeridi G ≤ %50 ile aynı sayı). Dikeyde ≤ 2.
⛔ Cümlesi yazılamayan sahne PROMPTLANMAZ — cümle "hiçbir şey" ise ⑩ da
   "hiçbir şey" yazacaktır.
```

---

# 2. ⚓ ÇAPA ÜÇLÜSÜ — SEÇİM · BEDEL · FİNAL için ÖNCE/SONRA beden çifti

**Rubriğin tek testi:** üç çapa vuruşta öncesi/sonrası karesi dondurulur ve
bedendeki fark bir cümleyle yazılır; "hiçbir şey" ise vuruş ekrana
ulaşmamıştır ve hüküm skordan bağımsız `THE CHOICE IS INVISIBLE` olur.
Yazım tarafı bu çifti ÖNCEDEN yazar — ve nereye gideceğini bilir:

```
ÇAPA ÜÇLÜSÜ — QA_SPEC'e (⑩ mod D "CHOICE at · COST at · FINAL at" satırını
buradan okur; bugün SPEC'te yeri YOK — ⬜ şablona işlenmedi, plana ayrı blok)

CHOICE  S⬜ · ⬜ s   BEFORE: ⬜ (kayıtlı bir kanalda gövde)   AFTER: ⬜
COST    S⬜ · ⬜ s   BEFORE: ⬜                                AFTER: ⬜
FINAL   S⬜ · ⬜ s   BEFORE: ⬜                                AFTER: ⬜

KURALLAR
  □ BEFORE ve AFTER aynı KANALDA yazılır (omuz ↔ omuz, el ↔ el); iki
    farklı kanal karşılaştırılamaz
  □ Fark ADLANDIRILABİLİR: "omuz hattı iner", "el nesneyi bırakır",
    "kask nesneden uzağa döner" — "duruşu değişir" fark değildir
  □ Fark PLANDAN değil KADRAJDAN okunur: başlığı ve planı bilmeyen
    biri de söyleyebilmeli (⑩ kat. 6 üçüncü madde)
  □ CHOICE karesinde REDDEDİLEN NESNE kadrajdadır ve sonra da orada
    kalır (KARAKTER_KARTI §3) — seçim iki şeyden birini seçmektir
  □ KADRAJ ÖLÇEĞİ: fark kadrajın kısa kenarının ≥ ⅛'i kadar yer kaplar
    [D179 ③] — 40 m'den 14 cm'lik bir jest üç pikseldir

NEREYE YAZILIR — üç yer, üç zaman:
  İMAJ PROMPTU (t=0)      = BEFORE gövdesi, kelimesi kelimesine [D179 ①]
  VİDEO PROMPTU (klip içi) = BEFORE → AFTER geçişi, gövde FİİLİYLE (§3)
                            (gövde hareketi klip içinde yaşar — durum/nitelik
                             değişimi değil, HAREKET: en güçlü eksen)
  SONRAKİ SAHNENİN İMAJI  = AFTER gövdesi, 0,0 s satırı olarak (§5 kalıntı)
```

```
KARARIN GÖVDE İMZASI (kanal listesi UYGULAMA/ÖLÇÜLMÜŞ yön · milimetreler
İNMEDİ — T15.3): karar öncesi ↔ karar anı
  SALINIM      geniş, kararsız ağırlık  ↔  durur, ağırlık hedef ayağına oturur
  BAŞ          iki-üç yön arasında gezer ↔  nesneye KİLİTLENİR, bir daha dönmez
  OMUZ HATTI   kalkık, gergin            ↔  iner, düzleşir
  EL           yarım açık, asılı         ↔  biçim alır (kavrama/açma) ya da BIRAKIR
  NEFES        sık, sığ (omuz her seferinde kalkar) ↔ tek derin nefes, sonra sessiz
  → CHOICE çifti bu beşten EN AZ İKİSİNİ karşılıklı yazar. Beşini birden
    yazmak §6 orantı ihlalidir.
İngilizce çift (yazım sayıları tasarımdır):
  BEFORE: The helmet turns from the crate to the rope and back twice in
          four seconds; the right glove hangs half-open at hip height;
          the shoulders sit high.
  AFTER:  The helmet holds on the crate. The shoulders drop and stay down.
          The right glove closes and takes the crate handle; the rope
          stays on the ground where it was.
```

---

# 3. 📖 NİYET KANALI SÖZLÜĞÜ — sekiz kanal, İngilizce kalıplar

**Turun tek cümlesi (T15.5):** niyet hareketin SONUCUNDA değil BAŞINDA ve
ARASINDA yaşar — bakış eli önceler, ağırlık adımı önceler, jest sözü
önceler. Her gövde satırının ÖNÜNE bir hazırlık, ARASINA bir gecikme yazılır.
Sözlük D169'un efor sözlüğüyle aynı biçimdedir: kanal · mekanizma etiketi ·
kopyalanabilir kalıp (sayılar YAZIM SAYISIDIR).

```
① BAKIŞ — kask önce döner, el sonra gider          ÖLÇÜLMÜŞ (bakış eli önceler)
   "The helmet turns to the latch first. A full second later the right
    glove lifts toward it."
   ⛔ baş ve el AYNI anda başlarsa refleks/plansız okunur (ÖNERİ) — yalnız
     irkilme sahnesinde bilerek yazılır
   ⛔ bakış ışığa değil NESNEYE [D104]; GAZE STRING plana yazılır (O/A/D/U)

② AĞIRLIK — ağırlık harekete ÖNCE kayar             ÖLÇÜLMÜŞ (erken postür düzeltmesi)
   "The weight goes to the rear boot; then the front boot lifts."
   "He leans onto the left boot before the arm reaches across."
   (D169 GÖVDE/BACAK kanalı efor içindir; burada aynı hareket NİYET
    hazırlığıdır — ikisi aynı cümlede olabilir, fatura ayrıdır)

③ TEREDDÜT — dur, sonra git                         ÖLÇÜLMÜŞ (biçim) · eşik ⬜
   durma-yeniden başlama:
   "The glove stops a palm's width from the handle, holds for two seconds,
    then closes on it."
   yarım uzanma-geri çekilme:
   "The glove goes twenty centimetres toward the switch, stops, and comes
    back to the thigh."
   yanlış başlangıç (ağırlık öne, geri):
   "The weight rocks onto the front boot and settles back; the boot never
    lifts."
   yörünge sapması:
   "The hand curves wide of the valve, then straightens to it."
   ⛔ tereddüt bir OLAYA bağlıdır (§6): önünde gördüğü bir şey olmalı
   ⬜ eylem içi duraklama bandı (ÖNERİ · rapor): ~0,2-0,5 s tereddüt
     okunur; ~0,8 s üstü DONMA okunabilir → 0,8 s'den uzun duraklama
     yalnız nefes/salınım eşliğinde yazılır (§4)

④ BIRAKMA — bırakmak açmak değildir                 ÖLÇÜLMÜŞ (sunma yavaş biter)
   "The fingers open one at a time; the rope slides out of the glove and
    the hand stays open for a second before it drops."
   "He does not throw the cup. The arm lowers and the water runs out."
   sunma/uzatma (birine): yavaşlama fazı uzun —
   "She holds the rope out at arm's length; the hand slows to a stop and
    waits there."  (hızlı biten uzatma "fırlatma" okunur)

⑤ TEMPO — kontrast, "en yavaş" değil                UYGULAMA (iki yönlü)
   "The fourth reach is slower than the first."      (D169 KADANS ile aynı)
   "The second press is quicker and shorter than the first."
   ⭐ Kural: en önemli jest ÇEVRESİNDEN FARKLI tempoda — ya en yavaş ya
     aniden en hızlı (yavaş filmde 100 ms'lik buton = şok). Aynı hızda
     akan film "düz" okunur (⑩ desen ⑤).

⑥ MESAFE — nesneye yakınlık bir sayaçtır            ÖLÇÜLMÜŞ (⑩ proximity kanalı)
   "He stops one step short of the hatch and stays there for the rest of
    the take."
   "Each of the three approaches ends closer: two metres, one metre, a
    hand's width."

⑦ NEFES — görünür, omuz hattında                    ÖLÇÜLMÜŞ · ZATEN VAR (KARAKTER §4.2)
   "The suit's shoulders rise once, slowly, and settle."
   "Short shallow pulls; the shoulders lift each time."
   ⚠️ Gerçek basınç giysisinde GÖĞÜS genişlemesi dışarıdan okunmaz
     (rapor 1'in kendi kaydı) — nefes OMUZ HATTINA yazılır, göğse değil
     (ÖNERİ; KARAKTER_VE_DUYGU §4.2'nin "omuz + göğüs" satırına not)

⑧ KALINTI — olayın izi bir sonraki satıra taşınır   UYGULAMA (süreklilik pratiği)
   "The arm comes down slower than it went up."
   "He stays bent at the hip for the rest of the take; the shoulders do
    not come back up."
   → §5 anti-RESET: bir sonraki sahnenin 0,0 s satırı bunu devralır
```

```
LABAN EŞLEMESİ (UYGULAMA · LMA çaba nitelikleri) — kart satırı → İngilizce
  TEREDDÜT   Indirect · Sustained · Bound   "the hand wanders toward it,
             slow, held back"
  KARAR      Direct · Sudden · Free/Strong  "the hand goes straight to it
             in one movement and closes"
  RET        Bound + geri                   "the shoulders pull in; the
             glove withdraws to the chest"
  UYUM       Free + ileri                   "the whole body leans into it"
  ⛔ Laban KELİMELERİ prompta girmez (model "sustained" okumaz); eşleme
    yazara sözlük seçtirir, cümle §3 kalıbıyla yazılır.
```

---

# 4. ⏱️ TEMPO HARİTASI VE TUTULAN DURGUNLUK

```
TEMPO HARİTASI — sahne haritasına bir sütun: Y (yavaş) · N (normal) · H (hızlı)
  □ Film düz çizgi olamaz: ≥3 tempo değişimi (dikeyde ≥1)
  □ CHOICE sahnesi çevresinden FARKLI (§3 ⑤ kontrast)
  □ COST sahnesinden sonraki sahne, COST'tan yavaş başlar (kalıntı)
  □ Ardışık üç sahne aynı harf olamaz (KURGU_RITMI örüntü kırıcıyla aynı mantık)

TUTULAN DURGUNLUK ≠ DONMA (ÖLÇÜLMÜŞ fizyoloji · UYGULAMA bağlı akış)
  Canlı beden hareketsizken de salınır ve nefes alır; mikro-hareket
  yokluğu "manken" okunur (⑩ desen ①). Güçlü durgunluk hareketi
  BASTIRARAK değil, BAĞLI AKIŞ + NEFESLE yazılır:
  ✗ "He holds absolutely still and waits. Nothing in the frame changes."
  ✓ "He holds still: the suit's shoulders rise once with a slow breath
     and settle, the helmet stays on the horizon, one glove closes and
     opens once at his side. Nothing else moves."
  □ Her S (sükûnet) sahnesinde ÜÇ şey yazılır: nefes (omuz) · sabit bakış
    hedefi · tek mikro-ayar (parmak/omuz)
  □ ⬜ 2,5 s'den uzun hareketsizlik yalnız bu üçlüyle yazılır (T15.1 ④
    donma sınırı — hipotez, ama iki raporda aynı yönde)
  ⛔ "still", "motionless", "frozen", "does not move" tek başına YAZILMAZ —
    model bunu resim gibi dondurur (T15.2 #24 frozen subject bias);
    olumsuz cümle tutmaz [D79 · REHBER §7] — ne YAPTIĞI yazılır
```

---

# 5. 🔄 SONRASI TAŞINIR — anti-RESET

**Ölçülmüş arıza:** ADAY-26 (Amber Lattice: patlamadan sonraki kesmede sakin
manken) · ADAY-84 (Low Power: sera kaybının yorgunluğu S21'de yok) · ⑩
desen ⑧ THE RESET. **Mekanizma (UYGULAMA):** olay sonrası duruş üstel
söner; kesmede ANİ sıfırlanma zaman atlaması değil DEVAMLILIK HATASI okunur.
Zaman atladıysa onu mekân ya da ışık söyler, gövde değil.

```
KURAL — COST/D/R sahnesinden sonraki sahnenin İMAJ promptu (0,0 s)
kalıntı gövdeyi taşır:
  "0,0 s — he is already bent at the hip from the last scene, the right
   glove open at his side, shoulders down; he straightens over the first
   three seconds."
  □ Kalıntı en az bir kanalda (omuz · el · mesafe · tempo) ve klibin ilk
    ~3 s'sinde çözülür; anında dik duran figür RESET'tir
  □ GÖVDE SONUÇ BELLİ OLMADAN GEVŞEMEZ (⑩ desen ⑦): bir işin sonucu
    sonraki sahnede görülüyorsa, bu sahnenin son saniyesi gergin biter
  □ Zaman atlaması varsa (saatler sonra): kalıntı düşer ama YERİNE ışık
    takvimi / kir merdiveni [D147] değişir — ikisi de değişmiyorsa
    izleyici "reset" okur
  □ DAVRANIŞ ŞERİDİ kuralıyla aynı: K'dan sonra G gelmez (KARAKTER_KARTI §4)
```

---

# 6. 🎯 TETİK VE ORANTI — her jestin bir sebebi, her sebebin bir ölçüsü

```
TETİK KURALI (UYGULAMA · Meisner: dış dürtü yoksa hareket yok · ⑩ desen ④)
  Her jestin ÖNÜNDE kadrajda görünen bir olay vardır ve aynı TIMELINE'da
  yazılıdır: "the tether goes slack (3s) → the glove closes on nothing (4s)".
  Olaysız jest = duygu spreyi. Tereddüt de bir olaya bağlıdır: önünde
  gördüğü şey yazılır.

DOLGU JESTİ LİSTESİ — YAZILMAZ (ADAY-85 · ⑩ desen ⑨ · ölçülmüş)
  eldiven kontrolü · kaska dokunma · omuz silkme · "adjusts the suit" ·
  sebepsiz el kaldırma · kayışı çekiştirme (KARAKTER KARTI'nda ALIŞKANLIK
  olarak tanımlı ve ≥3 kez tekrarlanan jest bunun dışındadır — o dolgu
  değil kimliktir)

ORANTI (⑩ desen ⑪ · kat. 9)
  □ Jestin büyüklüğü olayın büyüklüğüyle ölçülür: küçük olay → tek kanal,
    küçük genlik; CHOICE/COST → iki kanal
  □ Filmin EN BÜYÜK jesti EN BÜYÜK anındadır — başka hiçbir sahnede
    ondan büyük jest yok (sahne haritasında işaretlenir)
  □ Bir sahnede ≤2 niyet kanalı; üç ve üstü "over-told" (⑩ ⑪)
  □ Duygu ADI prompta girmez ("afraid", "desperate" — SES §2a.2'nin gövde
    hâli); yalnız gövde fiili
```

---

# 7. 🙂 YÜZ KANALI — yalnız vizör berrak CU'da

```
□ Yüz kanalı yalnız KASK YOKKEN (basınçlı iç hacim, tek sahne) ya da
  vizör içi ışık satırı yazılı CU'da açılır (KARAKTER_VE_DUYGU §1 blok)
□ İfade OLAYLA değişir, takvimle değil (§6 tetik): "as the needle crosses
  into the red, the jaw sets"
□ Göz dikkatin gittiği yere: bakış hedefi TIMELINE'da nesnedir, kamera
  değil (⑩ desen ⑩ ACTING TO CAMERA — günlük kadrajı [SCOURED GLASS]
  tek istisna, tasarım gereği)
□ Kesme üstünde dondurulmuş ifade yok: CU'nun son saniyesi ile sonraki
  sahnenin 0,0 s'si aynı ifadeyi taşır ya da geçiş yazılır
□ ⭐ DORUKTA YÜZ AYIRT ETMEZ (TUR 11 · ZATEN VAR): doruk yükü omuz/gövde/ELE;
  yüz doruğun ÖNCESİNE ve SONRASINA (KARAKTER_VE_DUYGU §4.3)
```

---

# 8. 🧾 TIMELINE YENİDEN YAZIMI — deponun kendi sahnesiyle

**Kaynak:** THE SCOURED GLASS FAZ 1 · S4 "İLK REPLİK — CEVAPSIZ" — planın
kendi cümlesi *"ikinci basış kimin içindi?"* (niyet sahnenin özü). Mevcut
TIMELINE NEREDE/NE yazıyor; aşağıda aynı sahne §3 sözlüğüyle.

```
MEVCUT (özet)
  2s — His left glove lifts slowly …, travels to his chest plate and
       presses one button flat, then stays pressed and still.
  4s — His helmet tilts up a few degrees toward the far horizon. …
  6s — The glove lifts off the button and the arm falls slowly back to
       his side. He holds absolutely still and waits. Nothing in the
       frame changes.
  8s — The left glove rises again, presses the same button once, releases
       it immediately and drops away. No answer comes.

YENİDEN (aynı olay, aynı kurulum — yalnız gövde fiilleri)
  0s — He stands with the weight on both boots, arms at his sides. The
       suit's shoulders rise once with a breath and settle.
  1s — The helmet turns first: it lifts a few degrees to the far horizon
       and holds there.                                          [① BAKIŞ önce]
  2s — Only then does the left glove lift, slowly, to the chest plate.
       It stops a palm's width from the button for one second, then
       presses it flat and stays.                               [③ TEREDDÜT]
  4s — Behind the clear visor his jaw moves as he speaks; the glove
       stays pressed; the helmet does not leave the horizon.
  6s — The glove lifts off the button. The arm comes down slower than it
       went up.                                                  [⑧ KALINTI]
       He holds still: one more slow breath lifts the shoulders; the
       helmet drops one degree toward the ground and stays.     [§4 durgunluk · sessizlik cevap]
  8s — The glove goes back up quicker than before and presses the same
       button once, short, and drops away at once.              [⑤ TEMPO kontrastı]
  10s — Final frame: arms down, the helmet a degree lower than at 1s,
        the dust around the boots undisturbed.                 [⑧ fark adlandırılabilir]

İZLEYİCİ CÜMLESİ (§1): "Cevap beklemiyor ama yine de basıyor."
DEĞİŞİM (DIYALOG_SAHNESI §6): umut − (kask bir derece aşağıda) · ısrar +
```

```
TIMELINE YAZIM KURALLARI (T15.2 #24 · D169 · REHBER §7)
  □ Her zaman satırında EN AZ BİR gövde fiili (helmet turns · weight goes ·
    glove stops); "presses the button" tek başına konum satırıdır
  □ İKİ AŞAMALI EYLEM İKİ SATIRA BÖLÜNÜR: "stops, then reaches" tek satırda
    yazılırsa model tek harekete çöker — 2s dur · 3s git
  □ Somut fiil + saniye + mesafe/açı; soyut zarf ("hesitantly",
    "thoughtfully") ve derecesiz sıfat ("nervous", "calm") YAZILMAZ
  □ Olumsuz cümle tek başına tutmaz ("does not move") — ne YAPTIĞI yazılır
  □ Hazırlık ÖNCE, eylem SONRA: bakış → ağırlık → el → nesne (§3 sırası)
  □ Gövde cümleleri GİYSİ yüzeyinde kalır [D175]
```

---

# 9. 📋 NEREYE YAZILIR

```
SAHNE ÇALIŞMASI   İZLEYİCİ CÜMLESİ + TAŞIYAN KANAL + TASK ONLY (§1) — her sahne
PLAN              TEMPO sütunu (§4) sahne haritasına · ÇAPA ÜÇLÜSÜ (§2)
                  B5'in altına (⬜ FILM_PLAN şablonuna işlenmedi — kart G/P)
QA_SPEC           ÇAPA ÜÇLÜSÜ bloğu — ⑩ mod D'nin "ANCHOR BEATS: CHOICE __ ·
                  COST __ · FINAL __" satırı ve "THE CHOICE ON THE BODY"
                  önce/sonra karşılaştırması buradan okunur (⬜ şablona
                  işlenmedi; o zamana kadar SPEC'e elle blok)
PROMPT            TIMELINE §8 kurallarıyla; imaj = BEFORE (D179) · sonraki
                  imaj = AFTER (§5)
EFOR SAHNESİ      D169 kanalı + buradaki niyet kanalı aynı sahnede
                  olabilir — iki cümle, iki eksen
REPLİKLİ SAHNE    konuşanın/dinleyenin bedeni DIYALOG_SAHNESI §4 ile
İKİ İNSAN         faz farkı + cevap ızgarası IKI_KISI §2 · §4 ile

⬜ KAPI ADAYI — prompt_kontrol.py ㉒ NİYET KANALI (⑳ ZORLANMA'nın ikizi;
   YAZILMADI · GOZLEM_DEFTERI'ne aday olarak düşer):
   tetik: sahne başlığında "MERKEZÎ SEÇİM" / "BEDEL" / "FİNAL" ya da SPEC
          ÇAPA ÜÇLÜSÜ'nde geçen sahne numarası
   arama: video promptunun TIMELINE penceresinde (⑳'nin EFOR_PENCERE'si)
          §3 sözlüğünden ≥2 iz — örn.
          helmet/visor … turns|holds|drops · weight … (rear|front) boot ·
          stops … (palm|hand|centimetre) … then · fingers open one at a time ·
          slower|quicker than the (first|last) · shoulders (rise|drop|settle)
   sonuç: <2 iz → FIX "çapa sahnesinde niyet kanalı yok"
   ⚠️ ⑳'nin dersi [D195]: iki TIMELINE biçimi var; pencere ikisine de
     açılmalı, yoksa kapı sessizce GO der.
```

---

# 10. ✅ PLAN KONTROLÜ — bu kılavuzun 10 maddesi

```
□ 1.  Her sahnenin İZLEYİCİ CÜMLESİ yazıldı mı; TASK ONLY sayısı ≤ yarı mı
□ 2.  ÇAPA ÜÇLÜSÜ üç satır da dolu mu; BEFORE/AFTER aynı kanalda ve
      fark adlandırılabilir mi
□ 3.  CHOICE karesinde reddedilen nesne kadrajda mı; fark ≥ ⅛ kısa kenar mı
□ 4.  İmaj promptu BEFORE'u, sonraki sahnenin imajı AFTER'ı taşıyor mu
□ 5.  Her TIMELINE satırında ≥1 gövde fiili; iki aşamalı eylem iki satırda mı
□ 6.  Hazırlık sırası (bakış → ağırlık → el) çapa sahnelerinde yazılı mı
□ 7.  TEMPO sütunu düz çizgi değil mi; CHOICE çevresinden farklı mı
□ 8.  Her S sahnesinde nefes + sabit hedef + tek mikro-ayar var mı;
      "still/motionless/frozen" tek başına yok mu
□ 9.  COST/D/R'den sonraki sahnenin 0,0 s'si kalıntı taşıyor mu
□ 10. Dolgu jesti (eldiven/kask/omuz) yok mu; sahne başına ≤2 niyet kanalı mı;
      en büyük jest en büyük anda mı
```

---

# 11. 📚 KAYNAKLAR

```
URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md §TUR 15   süzme kaydı (T15.0 · T15.1 ①② · T15.2 #15-24 · T15.3)
URETIM_ONCESI_ANALIZ/TUR15_HAM_RAPORLAR/TUR15_1_NIYET_BEDENDE_HAM.md   ham rapor
QA_PROMPTLARI/_KAYNAK/10_OYUNCULUK_QA_CRITIQUE_PROMPT.md   bu dosyanın ölçüm ikizi (kanal kaydı · ledger · üç önce/sonra · desen ①-⑪)
DERSLER/07_KURGU_VE_ANLATI.md D202                          görünmez seçim (kök vaka)
DERSLER/02_KARAKTER_VE_CANLI.md D169                         efor sözlüğü (bu dosyanın efor ikizi) · D175 mühür
DERSLER/06_METIN_VE_PROMPT_DILI.md D179                      imaj t=0 · ⅛ kuralı
DERSLER/GOZLEM_DEFTERI.md ADAY-26 · 41 · 84 · 85              reset · tereddütsüz karar · dolgu jesti
KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md §1 · §3 · §4          kart (NEYİ) · karar mimarisi · davranış şeridi
KARAKTER_VE_DUYGU_KILAVUZU.md §1 · §4.2 · §4.3                vizör içi ışık · görünür nefes · dorukta yüz
IKI_KISI_VE_AYRILIK_KILAVUZU.md §2 · §4                      faz farkı · cevap ızgarası
DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md §4                    konuşan/dinleyen bedeni
SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md                           durum değişimi sınıra, hareket klibe
KILAVUZ_REHBERI.md §7                                        değişen nitelik (en zayıf eksen) · olumsuz cümle
PROMPT_KONTROL/prompt_kontrol.py ⑳                           ZORLANMA kapısı (㉒ adayının kalıbı)
yatay_10_20_dk_filmler/THE_SCOURED_GLASS/FAZ_01_UYANIS/FAZ_01_UYANIS.md S4   §8'in kaynak sahnesi
FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md · 01_FILM_RAPORLARI/THE_COUNTED_TURN.md · THE_GREEN_CEILING.md   ölçülmüş plato
```
