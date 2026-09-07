# 🎶 THE WHITE FLOOD — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR SALDIRI DEĞİL, BİR SEVİYE olarak okumalı —
    bir şeyin yükselmesi; sabırlı, kişisel olmayan, durmayan. Müzik ne
    uyarır ne kovalar; YÜKSELEN bir seviyenin altını çizer ve onunla
    birlikte kendi de yükselir."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14): 10 s sahne = 12 vuruş
              = tam 3 ölçü (4/4). Her sahne sınırı bir ölçü çizgisine düşer.
              Hook 9 s = 10,8 vuruş → hook TEK BAŞINA ölçüsüzdür ve S1'in
              ilk ölçü çizgisi 0:09'dadır (müziğin gerçek girişi).
SÜRE:         299 s = hook 9 s + 29 × 10 s
MÜZİKSİZ SAHNE: **S26 (4:19-4:29)** — ⛔ her filmde EN AZ BİR tane (§10).
              Merkezî seçim sahnesidir: dört eldiven kasanın sapını
              bırakırken müzik TAMAMEN kesilir; yalnız iki tutulan nefes
              kalır ve onlar da kasa kadrajdan çıktıktan SONRA salınır.
              ⛔ MÜZİK DORUKTAN ÖNCE SUSAR, DORUĞUN BAŞINDA DEĞİL
                [SES_VE_DIYALOG §6 · YANASMA §2.1]: katmanlar S25'in
                sonunda (4:19'dan önce) incelerek biter, sessizliğin fark
                edilmesi için 1-2 saniye bırakılır.
              İkincil müziksiz bant: S0'ın ilk 2 saniyesi (hook sesi —
              tek diegetik ses: halatın kuru sürtünmesi + tek nefes;
              erken müzik girişi elendi, HOOK §5 sıralaması).
SUB-BASS:     42 Hz temel + 84 / 126 / 168 Hz armonik eşlikçi (§15.1).
              MISSING FUNDAMENTAL: telefon sürücüsü 150 Hz altını fiziksel
              olarak üretmiyor; 42 Hz katmanı tek başına telefonda YOK
              hükmündedir. Üst armonikler yoğun yazılır, beyin temeli
              "duyduğunu" varsayar.
              ⚠️ VE BU FİLMDE İKİNCİ BİR SEBEBİ VAR: dünyanın kendisi ince
                atmosferde BOĞUK ve yüksek frekanssızdır (§3.2). Diegetik
                katman zaten üst uçtan yoksun; müzik o boşluğu doldurmaz,
                aynı bandı paylaşır.
VURUŞ NOKTASI: 4 tane (az olan güçlüdür)
              ① 0:13  S1 — beyaz kenar kaya çıkıntısını yutar (katalizör;
                            drone ilk kez kıpırdar)
              ② 1:59  S12 — çizginin üstü açılır (drone beşliye açılır —
                            filmin ilk gerçek genişlemesi)
              ③ 3:13  S19 — "no return" (bütün katmanlar tek vuruşta düşer)
              ④ 4:39  S28 — taraça (sessizlikten sonra tek sürekli ton
                            girer ve bir daha çözülmez)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno (v4 · instrumental)
GENRE: minimal orchestral drone / textural ambient, no percussion
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low sustained cello drone, bowed slowly, no vibrato — enters 0:09
  2. A single high sine tone, very quiet, one pitch, never moving —
     enters 0:29 and stays until 3:13
  3. Bowed double bass at 42 Hz with its own upper harmonics at 84, 126
     and 168 Hz played by cellos in unison — enters 1:59
  4. A cold second sustained note a minor second above the drone —
     enters 2:49 and only appears three times
  5. One low sustained tone alone — enters 4:39 and never resolves

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-9 s      (S0): silence, then nothing but room tone
  9-29 s     (S1-S2): cello drone alone, very low; one small movement
                      on the bar line at 0:13 and back
  29-79 s    (S3-S7): drone plus the high sine tone; no movement
  79-99 s    (S8-S9): the drone thins to almost nothing under the
                      two breathing channels
  99-119 s   (S10-S11): drone returns, slightly higher
  119-129 s  (S12): the drone opens into a fifth and holds — the film's
                    first real widening
  129-179 s  (S13-S17): the 42 Hz bass enters underneath with its
                    harmonics; everything else thins
  179-189 s  (S18): the cold second note, one long entry
  189-199 s  (S19): every layer drops together on one beat, leaving the
                    sine tone alone for four seconds, then nothing
  199-229 s  (S20-S22): bass alone, very quiet, rising by one step at 3:39
  229-249 s  (S23-S24): bass and drone together, tightening, no melody
  249-259 s  (S25): every layer thins out and is gone by the end of the cue
  259-269 s  (S26): TOTAL SILENCE — no music of any kind
  269-279 s  (S27): one low sustained tone enters at 2.0s into the cue
  279-299 s  (S28-S29): that tone alone, unresolved; at the very end it
                    stays exactly where it is and simply continues

SYNC RULE: every scene boundary lands on a bar line (72 BPM, 4/4, 10 s =
3 bars). No layer enters or leaves anywhere except on a bar line. The four
hit points are the only moments where two things change at once.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Diyalog kanalı temiz kalır: 16 repliğin hepsinde müzik
katmanı 6 dB iner ve replik bitince geri gelir (SES_VE_DIYALOG §3:
replikli sahnede yoğun ses olayı İSTENMEZ). Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO percussion, NO braam, NO riser, NO
reversed cymbal, NO whoosh, NO final chord, NO resolution.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

> ⛔ **FİNAL ÇÖZÜLMEZ.** Loop satırı (§5③) bunu gerektiriyor: müzik son
> saniyede kadans yapmaz, tek alçak katmanda kalır ve 0:00'a akar.
> Kadanslı bir final "bitti" sinyalidir ve döngüyü öldürür.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
⭐ DEPO KAYDI: replik olan film 0 / 81. Bu film o sayıyı 1 yapıyor.
   Merdiven basamağı: **1-2** (kadraj dışı ses + tek yönlü kayıt).
   BASAMAK 3 (ekranda konuşan ağız) KULLANILMADI — PROB B koşulmadı.

REGISTER:      HUMAN 14 · MACHINE 2 · UNCLEAR 0
               (UNCLEAR yazım tarafında YASAKTIR — §1)
REPLİK SAYISI: 16 · konuşan ağzın okunduğu kare **0** · dış ses/anlatıcı 0
               · ekran metni 0,0 s · replikli sahne 9 / sessiz sahne 21
KANAL:         14 replik TELSİZ (iki gövde arası) · 2 replik KASK İÇİ
               sentetik giysi sesi. Register EKRANDAN okunur: telsiz
               bandının filtresi ile kask içi sesin filtresi AYRIDIR ve
               ikisi hiç karışmaz.
BEDENLEŞTİRME [§1a.1]: **YOK** — hiçbir sahnede kamera konuşan ağza dönmez.
               Karar bilinçlidir ve şu: bu filmde iki ses de BEDENLİDİR
               (ikisi de kadrajda ve yüzleri okunur), bedensiz olan tek
               şey AĞIZDIR. Chion'un kuralı sese yazıldı; burada aynı
               kural GÖRÜNTÜ tarafına uygulanıyor — duygu gözden okunur,
               ve ⭐VİRAL kapısının YÜZ satırı zaten gözü ölçüyor.
               ⛔ Bu bir bütçe kısıtı DEĞİL tasarımdır ve tasarım
                 olduğunun kanıtı bu satırın PLANDA yazılı olmasıdır.
İLK İNSAN SESİ: S2 · 0:21 · öncesindeki kesintisiz sessizlik **21 saniye**
               [§1a.2] · denk geldiği vuruş: KURULUM sonu, katalizörden
               hemen sonra — dünyanın kuralı görsel olarak kurulduktan
               SONRA ilk insan sesi gelir.
SAYI KURALI:   [D82] sayı söyleyen HER replik gövdesiz MACHINE'dedir:
               S7 (1:12) ve S19 (3:13). 14 insan repliğinde sayı, birim,
               yüzde, süre YOKTUR — tarandı ve sıfırdır.
SÖZ DAĞILIMI:  uzun figür 7 · geniş figür 7 · MACHINE 2 — tekelleşme yok.
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122] —
               replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti.
               16 kaydın 16'sı QA_SPEC B bloğunda formülle doğrulandı.
```

### 🎚️ DİEGETİK SES KATMANLARI — sahne dokusu takvimi

```
S0-S3    kuru halat sürtünmesi · kırağı kabuğunun altında bot ·
         çok alçak, geniş, BOĞUK havza tonu (üst uç yok) · tek nefes
S4-S7    kabuk kırılması · kayış gıcırtısı · kasanın kuru sürtünmesi ·
         S5'te kristalin ince kuru tıkırtısı (kırağının kendi sesi)
S8-S11   iki nefes kanalı, biri hızlı biri yavaş · telsiz taşıyıcı
         hışırtısı · S11'de tıkırtı SUSAR ve o sessizlik duyulur
S12-S15  açık alan: neredeyse hiçbir şey · çok ince hava · adım sesi
         kayada sertleşir (kabuk değil kaya)
S16-S20  buzun kendi alçak gıcırtısı · eldiven buzda · çekiç sesi
         ince atmosferde TINISIZ (metal çınlamaz)
S21-S25  efor nefesi · halat · kaya · S22'de tıkırtı GERİ GELİR
S26      MUTLAK SESSİZLİK + kasa kadrajdan çıktıktan sonra iki nefes
S27-S29  ritmik nefes → tek alçak ton · S28'de varlığın tek sesi
         (ağır bir halatın yük alması gibi, bir kez) · S29'da aynı ses
         uzakta ve müzik çözülmeden devam eder

⛔ İNCE ATMOSFER KURALI [KILAVUZ_REHBERI §3.2]: bu dünyada ses BOĞUK,
   ZAYIF ve YÜKSEK FREKANSSIZDIR (240 m/s). Hiçbir dış ses net değildir;
   net duyulan her şey ya gövdeden iletilir ya telsiz kanalındadır.
   ⛔ "Uzay sessizliği" YAZILMAZ — bu vakum değil, ince atmosfer.
⛔ ORTAM YATAĞI [D83]: hiçbir sahne dijital sıfır değildir. S26'nın
   "mutlak sessizliği" bile iki nefes taşır — mutlak dijital sıfır
   teslim edilemez hata sınıfıdır.
⛔ TELEFON HOPARLÖRÜ [HOOK §5④]: hook sesinin taşıyıcısı 90 Hz üstündedir;
   ilk iki saniyenin nefesi ve halat sürtünmesinin üst armonikleri o
   bandı doldurur.
```
