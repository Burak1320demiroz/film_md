# TODO — YATAY 16 DK FORMATI + THE_STOLEN_SKY (ÇALINAN GÖKYÜZÜ)

> **Yazıldı:** 19.09.2026 · **REV 2:** 10 maddelik eleştiri + 5 küçük düzeltme · **REV 3 (aynı gün):**
> ikinci eleştirinin 7 maddesi — deneme/kalan sahne sayımı · ortam TEK TEK çekime · kara delik kontrol
> cümlesi · part ses raporu · P1 yedek çözümü · P6 kaydı · karar kaynağı etiketi (§7 REV 3 satırları).
> REV 2'de değişenler: ① tam-film incelemesi eklendi ② zor çekim denemeleri ve
> taslak referanslar PROMPT YAZIMININ ÖNÜNE alındı ③ "tam 10 s" koşulu gevşetilmiyor ④ replik
> iki ayrı kayıt ⑤ ortam çekimin FİZİKSEL HACMİNE göre ⑥ kara delik dünya-göreli ⑦ figür sınırı
> çekimin anlatması gereken ilişkiye göre ⑧ Bor'un ölümü V59–V60 birlikte okunur ⑨ onay yükü
> düşürüldü — sabit kararlar sorulmaz ⑩ ardışık çift / sürdürme kuralları mekanik uygulanmaz.
>
> Kaynak: `ilk_deneme/` dört dosya · AGENTS.md Kart A/H · KILAVUZ_REHBERI §2.0/§2.7 ·
> `yatay_8_dk_filmler/README.md` · THE_FALLING_WORLD / KRONOS_SON_SINYAL emsalleri · betikler.
>
> **Sahibin kararı:** 2/4/6/8 dk merdiveninin BEŞİNCİ basamağı. **96 sahne × 10 s = 16:00 ·
> 8 BÖLÜM dosyası × 12 sahne · QA 4 PART × 24 sahne + 1 TAM-FİLM incelemesi.**
>
> Bu dosya görev planıdır; film dosyası değildir. 19.09.2026: klasör betikle açıldı, dosya
> `THE_STOLEN_SKY/00_ANALIZ/00_TODO_GOREV_PLANI.md` olarak buraya taşındı. **DURUM (20.09.2026 gece):** FAZ 0 ✅ · FAZ 1 ✅ · **FAZ 2 ✅** (00_ANALIZ altı adım kapalı: çizelge 97 ✅/13 — · hasat 20 kilit ·
> konsept + 9 SAPMA + 4 kart · sıralama 96 satır + iskelet 20 harf/9 küme/DÖNÜŞ %33,3 D74 · uyarı 10 ⛔ + 12 ⚠️ · tablo 96 satır + 5 kilit dosya;
> prompt_kontrol 0 BLOCK). **20.09.2026 (akşam) — sahip "8 bölümde de promptlar yok" dedi → sıra değişti:** T5.1 PLAN ✅ · **T5.2 96 sahnenin 192 promptu ✅ (8 BOLUM, üreteçten — `06_PROMPT_URETECI/`)** · T3.1 taslak referans paketi ✅ (6 sayfa TASLAK) · QA_SPEC A·B·C·E ✅ · klasör modu **0 BLOCK · 10 FIX** (9 × D79 opak vizör tasarım-kaynaklı, düşer · 1 × DÖNÜŞ %37,5 D74). SIRADAKİ: T3.3 DENEMELER P1–P6 (sahip üretir) → ⏸ 2 → FAZ 4 animatik → deneme sadeleştirmeleri b*.py'ye işlenip yeniden üretim.
> 🔶 AÇIK: S67 repliği (D217) · DÖNÜŞ sapması kabul.

---

## 0. ÇALIŞMA SIRASI — sahibin önerdiği sıra, plan bunun üstüne kurulu

```
SABİT KARARLAR  →  TASLAK REFERANSLAR  →  ALTI DENEME (P1–P6)  →  16 DK ÖN KURGU
      →  KALAN PROMPTLAR  →  ÜRETİM  →  PARÇA KONTROLLERİ (4 PART)  →  TAM FİLM (görüntü · ses · hikâye)

DURMA NOKTALARI — her faz sonunda değil, yalnız çözülemeyen kararda:
  ⏸ 1  FAZ 1 sonu: karar tablosu tek mesaj — SABİT ve UYGULAMA TERCİHİ satırları bildirilir, YENİ karar
        isteyen satırlar (Q1–Q4) cevap bekler; cevapsızlık onay SAYILMAZ (§3.8)
  ⏸ 2  FAZ 3 sonu: altı denemenin sonucu — hangi sahne sadeleşir (bu karar sahibin)
  ⏸ 3  FAZ 4 sonu: ön kurgu — anlaşılmayan mekân / uzun açıklama / zayıf duygu listesi
  ⏸ 4  FAZ 8: parça raporları + tam-film raporu — kesme/yeniden sıralama sahibin
```

---

## 1. TEK BAKIŞTA — sayılar ve eşleme

```
SÜRE           96 × 10,000 s = 960,000 s = 16:00 — SABİT. Ham klip ölçülür (D124), kurguya alınan
               birim seçilen kare hızında TAM 10 s'e sabitlenir (24 fps → 240 kare · 30 fps → 300 kare).
               Zaman kodları yeniden hesaplanmaz; sapma KIRPMA TABLOSU ile kapatılır [D100 kalıbı].
               Final 960 s (±0). Tahliye koridoru 60 s = V88–V93 birebir.
YAZIM BİRİMİ   8 BÖLÜM dosyası × 12 sahne (THE_STOLEN_SKY_BOLUM_1 … _BOLUM_8)
QA BİRİMİ      4 PART × 24 sahne = 4:00 (THE_HARD_DOCK'un on iki mercekle ölçüldüğü ölçek)
               PART n = BOLUM_(2n−1) + BOLUM_(2n)   +   TAM-FİLM incelemesi (ayrı koşu, §3 FAZ 8)
SAHNE NO       sahibin V<n>'i = deponun S<n−1>'i (THE_FALLING_WORLD eşlemesi: V01 = S00)
SEKANS         sahibin "S01–S24 uzun sahne"leri depoda SEK01–SEK24 — betiğin `## 🎬 SAHNE n`
               sayımıyla çakışmasın (depoda tek harf "S" klip demektir)
ARDIŞIK ÇİFT   95 çift = 88 bölüm içi + 7 bölüm-dosyası sınırı (sınır çiftler 95'in İÇİNDEDİR)
```

| Bölüm dosyası | Depo sahne | Sahibin V | Film zamanı | Sekanslar | QA PART |
|---|---|---|---|---|---|
| BOLUM_1 — Gökyüzü kapandı | S00–S11 | V01–V12 | 00:00–02:00 | SEK01 (30 s) · SEK02 (50) · SEK03 (40) | **PART 1** |
| BOLUM_2 — Kuleyi ele geçirmek | S12–S23 | V13–V24 | 02:00–04:00 | SEK04 (40) · SEK05 (30) · SEK06 (50) | **PART 1** |
| BOLUM_3 — Alçaktan git | S24–S35 | V25–V36 | 04:00–06:00 | SEK07 (50) · SEK08 (40) · SEK09 (30) | **PART 2** |
| BOLUM_4 — Düşmanın kapısı | S36–S47 | V37–V48 | 06:00–08:00 | SEK10 (40) · SEK11 (50) · SEK12 (30) | **PART 2** |
| BOLUM_5 — Dört kişiden üçe | S48–S59 | V49–V60 | 08:00–10:00 | SEK13 (50) · SEK14 (30) · SEK15 (40) | **PART 3** |
| BOLUM_6 — Güç el değiştiriyor | S60–S71 | V61–V72 | 10:00–12:00 | SEK16 (40) · SEK17 (50) · SEK18 (30) | **PART 3** |
| BOLUM_7 — Karşı saldırı | S72–S83 | V73–V84 | 12:00–14:00 | SEK19 (50) · SEK20 (30) · SEK21 (40) | **PART 4** |
| BOLUM_8 — Bir dakikalık gökyüzü | S84–S95 | V85–V96 | 14:00–16:00 | SEK22 (30) · SEK23 (60) · SEK24 (30) | **PART 4** |

```
PART SINIR ÇİFTLERİ (② DEVAMLILIK hiçbir part masterda yan yana göremez → ELLE KARE, ①.10 göz kapısı)
  S23 ↔ S24   V24 hangardan alçak çıkış  →  V25 dar uçuş yolu          (K-1 dış plan · kafes yukarıda)
  S47 ↔ S48   V48 geçit kapanır, Serrak   →  V49 örtüşen kalkanlar       (T3 platformu)
  S71 ↔ S72   V72 kapıdaki baskı          →  V73 dar koridor çatışması   (rezerv odası dış kapağı)
PART MASKESİ (rapor_kontrol ①.11 · --bolum n/4) — yalnız TEKNİK devamlılık için
  PART 1 = BAŞ → Ending · Peak · Exit `—`   ·   PART 2, 3 = ORTA → Hook ve Ending ikisi `—`
  PART 4 = SON → Hook · HookQ · Stakes `—`
  Structure · Retention · Plateau · Rhyme: part koşularında `—`, TAM-FİLM koşusunda SAYI TAŞIR
  (8 dk hattının ⬜ seçeneği (a) bu filmde uygulanır: ④ ve ⑫ + ③ SES tam master'a ayrı koşu)
```

---

## 2. OKUNAN DOSYALARIN ÖZETİ — film nasıl olacak

### 2.1 Hikâye (sahibin ANA_PLAN'ından, değiştirilmeden)

- **Dünya:** kara deliğe yakın kurgusal NEREV-4; insan kolonisi üstün teknolojili VEYRA
  işgali altında; Yörünge Kafesi gemilerin kaçışını keser. Yüzeyde atmosfer var.
- **Hedef:** dört kişilik ekip (Mara komutan · Rey pilot · Ada mühendis · Bor ağır silah)
  T3 kulesinin YEREL REZERVİNİ ele geçirip 60 s tahliye koridoru açacak; E-1 ve E-2 çıkacak.
- **Teknoloji kuralları (sınırları baştan sabit):** yönlü kalkan · geçiş kapısı (fiziksel
  işaretleyici; kapanınca çıkmış asker silinmez) · Yörünge Kafesi (alçak uçuş mümkün) · alan
  yedeklemesi (kule patlatmak işe yaramaz) · servis anahtarı (iptal edilebilir) · yerel kontrol
  modülü (TEK kullanım) · sıçrama sürücüsü (kafes içinde çalışmaz).
- **Tek rezerv, gerçek seçim:** ya C-0'a imha darbesi ya 60 s koridor. V17 kurulum · V68
  doğrulama · **V85 seçim** ("Koridoru aç.").
- **Bedel:** V60 Bor öldürülür · K-1 sağ yönlendirme bileziği V30'da hasar alır, finale kadar
  kalır · koloni geride bırakılır · Serrak hayatta.
- **Final:** V88–V93 koridor (14:30–15:30, 6 klip = 60 s) · V94 kapanış + K-1 sıçrar · V95 boş
  koltuğun kemeri · V96 üç gemi birlikte.
- **Tema (sahibin cümlesi):** güç ve sorumluluk — intikam fırsatına sahip olduğunda yaşayanların
  geleceğini seçebilmek.
- **8 replik:** V11 · V12 · V15 · V54 · V59 · V68 · V83 · V85.
- **Sert kısıt:** vizörler TAMAMEN OPAK; yüz/göz/ağız 0 kare.

### 2.2 Sahibin "dikkat.md"si → plana giren 10 kural

| # | Sahibin maddesi | Bu planda nereye düşer |
|---|---|---|
| 1 | teknoloji açıklaması hikâyeyi boğmasın; üç cümle yeter | 02_KONSEPT "izleyicinin bilmesi gereken üç cümle" + 8 replik dışına açıklama yok |
| 2 | Bor'a ölümünden önce bağlanalım (kemer kontrolü) | KARAKTER KARTI Bor · alışkanlık → V19 (S18) ya da V24 (S23) kemer jesti; V95 kafiyesi |
| 3 | kara delik görsel vaadi; finalde mekanizma olmasın | Dünya Bible kuşbakışı harita (dünya-göreli yön) + ⑨ KADRAJ kilidi |
| 4 | insanlar kazanınca uzaylılar zayıflamasın | 03_SIRALAMA "görünür sebep" sütunu (açı · örtü · anahtar · konum · enerji) |
| 5 | her videoya taşıyabileceğinden fazla olay yükleme | tabloda BASKIN EYLEM sütunu · POLITIKA §4 aksiyon bütçesi |
| 6 | her 10 s'de hareket yeniden başlamasın | SAHNE_ZINCIRI sınır satırı + gerçek son kare zinciri (motor kararı Q1) |
| 7 | 16 dk ön kurgu | **FAZ 4** (promptlardan ÖNCE, denemelerden SONRA) |
| 8 | en zor çekimleri önce dene | **FAZ 3** altı deneme P1–P6 (promptlardan ÖNCE) |
| 9 | küçük ekranda okunabilirlik | TASLAK REFERANSLAR (FAZ 3) + KAPAK 120 px testi |
| 10 | değişikliklerin devamını takip et | PLAN "SABİT REFERANSLAR" bloğu + SPEC B kalıcı hasar zinciri |

---

## 3. KARARLAR — üç sınıf: SABİT (sorulmaz) · GEREKÇELİ (bildirilir) · GERÇEK SORU

### 3.1 SABİT — sahip zaten karar verdi, yeniden sorulmaz; yalnız depoya SAPMA kaydı yazılır [D74]

| # | Karar | Deponun kuralı | Kayıt |
|---|---|---|---|
| S1 | Konu, 16 dk, 96 video, 8 bölüm, 4 QA part | — | plan |
| S2 | Vizör tamamen opak, yüz 0 kare | D79 sapması — THE_FALLING_WORLD emsali var | ⭐VİRAL YÜZ satırı yazılamaz; oyunculuk beden/eldiven/nefes; prompt_kontrol D79 FIX'i BEKLENEN |
| S3 | Üstün teknolojili uzaylı ORDUSUYLA savaş (askerler · avcılar · komuta gemisi · Serrak) | `UZAYLI_VARLIK` ① TEK VARLIK · `UZAY_SENARYO` §3 uzay operası yasağı · §4.3 SAVAŞ ⏸️ RAFTA | Tarihli istisna kaydı UZAYLI_VARLIK §①'e + 02_KONSEPT SAPMA. Kalabalık yine yok: figür sayısı çekimin anlatması gereken İLİŞKİYE göre (§3.4) |
| S4 | Kan gösterilmez; kayıp "durum ışığı söner" DAHİL ama TEK BAŞINA DEĞİL (sahibin V60 notu + eleştiri 8) | SAVAŞ kartı kilitleri (isabet anı/ceset/kan 0) | §3.5 Bor'un ölümü okuma tablosu; şiddet sınırlarının KAYNAĞI ayrı ayrı yazılır (§3.5 alt tablo) |
| S5 | Her video tam 10 s; final 960 s; koridor 60 s | D124 "ızgara araçtan" | Ham ölçüm + kurguda tam 10 s'e sabitleme; zaman kodları SABİT. Kurgu kapısı 960 s ±0 (README'ye böyle yazılır; 8 dk'nın ±2 s toleransı bu formatta YOK) |
| S6 | Sahne sırası sahibinindir | 03_SIRALAMA "sıralama yazılır" | sıralama TAŞINIR, yeniden düşünülmez; SAPMA yalnız kurgu bedeliyle |

### 3.2 GEREKÇELİ — ajan karar verir, tabloyla bildirir; itiraz gelirse değişir

| # | Karar | Gerekçe |
|---|---|---|
| G1 | **Referans paketi YAZILIR, 6 sayfa:** ① dört insan tek sayfa (siluet + rol şeridi + ekipman) ② Veyra asker + Serrak (ANATOMY LOCK, tek tasarım) ③ K-1 üç durum (sağlam / V30 sağ bilezik / V91 arka çıkıntı kopuk) ④ E-1 · E-2 · C-0 ⑤ Veyra avcı + işaretleyici drone + kalkan/portal/kafes ÜÇ AYRI ŞEKİL ⑥ T3 kulesi + hangar + rezerv odası | `REFERANS_PAKETI_KILAVUZU` §1 altı tetikleyicinin hepsi ateşler; sahip FALLING_WORLD'de "8-9 değil 4" dedi — burada varlık sayısı 3 kat; 6 en az sayı. **TASLAK hâli FAZ 3'te** (denemeden önce), onaylı hâli FAZ 5'te |
| G2 | **Tema etiketi SORUMLULUK (aday, §3b)** · TANIM cümlesi: *"Gücü eline alan, onu kime borçlu olduğunu da seçer."* | §3'te yok → aday etiket izinli (GÜVEN emsali); takas biçiminde yazılmadı (§3c moratoryum). Son iki filmin kalıbı FAZ 2'de kontrol edilir |
| G3 | **Kilit sahne dosyaları:** HOOK S00 (V01) · NOVUM S16 (V17 tek rezerv) · BEDEL S59 (V60) · **DORUK S84 (V85 dramatik seçim)** · FINAL S94 (V95). **S92 (V93 son tırmanış) = FİZİKSEL DORUK**, tabloda genişletilmiş satır + deneme P4/P5 onu kapsar | ㉚ beş rol bir kez; iki doruk iki işlevle AYRI kaydedilir (eleştiri küçük düzeltme 2) |
| G4 | **Post-dub replik 8, prompt içinde 0** — SPEC A iki satır: `DIALOGUE LINES: 0 (image/video prompts)` · `POST-DUB LINES: 8 (final audio master)` | OMNI kılavuzu tırnak yok; ㉓ prompt tırnağını sayar → 0 tutar. Sekiz replik denetim DIŞINDA KALMAZ: FAZ 8 tam-film SES koşusu + replik anlaşılırlık/zamanlama tablosu (§3 FAZ 8 T8.6) |
| G5 | **Ortam çekimin FİZİKSEL HACMİNE göre**, aralığa göre değil → §3.3 hacim tablosu | eleştiri 5: V95 kabin = basınçlı iç hacim, vakum değil |
| G6 | **Kara delik + ışık/gölge DÜNYA-GÖRELİ** — PLAN'da kuşbakışı harita (pusula), promptta o çekimin kamera yönünden HESAPLANMIŞ ekran konumu | eleştiri 6; prompt_kontrol pusula kelimesini prompta sokmaz (NEAR_PASS BLOCK vakası) — hesap PLAN'da, sonuç promptta |
| G7 | **Ardışık çift bandı (≥1 ölçek + ≥45°) sekans içi DEVAM kliplerine uygulanmaz** — ACI_YAYI KÜME izni (aynı harf ardışık); yalnız sekans/bölüm geçişlerine uygulanır | eleştiri 10; aynı hareketi sürdüren çekim kesilmez |
| G8 | **Son 3 s sütunu beş sınıf:** SONUÇ · TEPKİ · KARAR · BİLİNÇLİ BEKLEYİŞ · SÜRDÜRME — kontrol sorusu *"bu süre izleyiciye ne kazandırıyor?"* ("yeni hareket var mı?" değil) | eleştiri 10; SAHNE_DOLULUGU'nun amacı ölü sahne, aracı "sürdürme" — amaç korunur, araç mekanik uygulanmaz; kılavuza tarihli not |
| G9 | **ORAN SETİ:** katalizör V12 (S11 · %12) · feda V60 (S59 · %62) · seçim V85 (S84 · %88) · fiziksel doruk V93 (S92 · %97) · çözüm V95–96 | §2.7 "plana yüzde satırı"; §2.5 bantlarıyla sınanır, sapma gerekçeli; 16 dk'da ölçüm yok → TAM-FİLM koşusu bunu ilk kez ölçer |
| G10 | **Araştırma turu TUR 23 (3 prompt, `26_` dosyası) FAZ 3 ile PARALEL koşar**, promptları beklemez; sonuçları FAZ 5 kalan promptlara girer | 3 açık başlık (§6); tur ile denemeler aynı soruya iki kaynaktan bakar |

### 3.3 GERÇEK SORULAR — sahibe taşınacaklar (FAZ 1 · tek mesaj)

| # | Soru | Öneri |
|---|---|---|
| Q1 | **Motor:** OMNI 1.1 Flash I2V (ilk/son kare zinciri = sahibin "gerçek son kare" kuralı) mi, Veo 3.1 mi, ikisi de (deneme sonucuna göre)? | ✅ **OMNI 1.1 Flash I2V** — kaynak: sahip onayı · 19.09.2026 · AskUserQuestion |
| Q2 | **NEREV-4 yerçekimi ve basınç sayısı** — her promptta aynı yazılacak (§5.1b) | ✅ **0,9 g · 1,0 atm** (§3.4'ün tarihli uyarlaması) — kaynak: sahip onayı · 19.09.2026 |
| Q3 | **Kare hızı** (kurgu birimi tam 10 s = kaç kare) | ✅ **24 fps → 240 kare** (96 × 240 = 23.040 kare) — kaynak: sahip onayı · 19.09.2026 |
| Q4 | `yatay_10_20_dk_filmler` → `yatay_10_dk_filmler` yeniden adlandırması AYRI İŞ — bu planın kapsamı değil, yalnız bildirilir | ⬜ bildirildi, cevap gelmedi — AÇIK (uygulama tercihi: dokunulmadı) |

### 3.4 Figür sınırı — İLİŞKİ planları (S3'ün uygulaması)

> Kural: yakın/orta planda 1–2 insan + en çok 1 Veyra. **İstisna = çekimin anlatması gereken
> ilişki iki figürü birlikte ister.** Bu planlar KARARLI kamera + tek eylem ile yazılır.

| Sahne | İlişki | Neden birlikte görünmeli |
|---|---|---|
| S25 (V26) | iki Veyra avcısı: biri arka, biri ön | "iki yönden sıkıştırma" tek figürle okunmaz |
| S40 (V41) | iki asker sırt sırta, kalkan açıları kapanıyor | düşmanın İLK uyarlaması — taktiğin bittiği an |
| S47 (V48) | Serrak + iki muhafız ilerliyor | pusu ölçeği; Serrak'ın ayırt edici zırhı ikisinin yanında |
| S48 (V49) | **örtüşen iki kalkan** (kararlı genel plan) | uyarlamanın güçlü biçimi — eleştiri 7'nin örneği |
| S49 (V50) | iki muhafız + araya düşen yük | geometrinin bölünmesi sebep-sonuç tek planda |
| S57–S59 (V58–V60) | Bor + yaklaşan muhafızlar + Serrak | ölümün okunabilirliği (§3.5) |
| S89–S90 (V90–V91) | E-2 + Veyra avcısı + K-1 | "K-1 araya girer" iki araç birlikte gerekir (sahibin notu) |

### 3.5 Bor'un ölümü — V59–V60 birlikte okunur (S4'ün uygulaması)

| Klip | Okunması gereken | Görsel kanıt (kan yok, isabet anı kadraj dışı) |
|---|---|---|
| S58 (V59) "Git." | Bor hareket edemiyor; Mara ulaşmaya çalıştı; Bor tutuşu BIRAKTI | Mara'nın eldiveni Bor'un koluna değer → Bor kolu çeker, silahı yeniden kaldırır; sağ diz zırhı hasarlı, yük kasasına yaslı |
| S59 (V60) Kayıp | **Serrak'ın darbesi Bor'a ULAŞTI** · Bor'un bedeni son eylemi bırakıyor · Mara'nın uzanan eli kafesin ardında kalıyor | (1) Serrak'ın silah kolu Bor'a dönük, atış parlaması; (2) Bor'un gövdesi kasadan kayar, ağır silah elinden yere düşer (ses); (3) giysinin durum ışığı söner — üç işaret birlikte; (4) Mara'nın eldiveni tel kafese bastırılmış, kaldıraç yükselmeye devam eder |
| S61 (V62) sonrası | ölüm KESİN | telsiz kanalı sessiz; boş koltuk V95; Bor 0 kare / 0 ses |

Şiddet sınırlarının KAYNAĞI (üçü ayrı):

| Sınır | Kaynağı | Durum |
|---|---|---|
| isabet anı kadraj dışı · ceset/kan 0 · silah markası/bayrak yok | **depo tercihi** — §4.3 SAVAŞ kartı kilitleri | uygulanır |
| hangi karelerin gerçekten red aldığı | **üretim deneyimi** — `09_URETIM_RED_DEFTERI.md` (14+ vaka) | FAZ 2'de okunur; bu filme düşen sınıf 02_KONSEPT B6'ya |
| sağlayıcının GÜNCEL RESMÎ kuralı (silah · ölüm · çatışma) | **araç kuralı — kaynak belgesi** (politika sayfası URL + okunma tarihi) | FAZ 2'de bulunur, `02_KONSEPT` B6'ya kaynak satırı; bulunamazsa "resmî kaynak yok" yazılır. ⛔ Bir denemenin kabul/red sonucu bu satırı DOLDURMAZ |
| bu çekimin üretim denemesi sonucu | **deneme kaydı** — P6 (S59 · S38 nötr tarifi) | FAZ 3'te dolar: motor · tarih · prompt · kabul/red · red metni. Yalnız bu iki karenin sonucudur, genel kural kanıtı değildir; red gelirse 09_URETIM_RED_DEFTERI'ne satır |

### 3.6 Ortam — çekimin geçtiği FİZİKSEL HACİM (G5)

> Bu tablo HACİMLERİ tanımlar; hangi çekimin hangi hacimde geçtiği **96 satırlık
> 00_SAHNE_TABLOSU'nda tek tek** yazılır (T2.6 HACİM sütunu). Aralık ataması KALDIRILDI —
> REV 2'nin aralıkları S04 (hangar mı kabin mi), S44/S60 (gezegen iç mekânı mı C-0 mı) ve
> S85'i (listelenmemiş) yanlış/eksik bırakmıştı. Gerçek ortam GEÇİŞİ olan çekimde BAŞ ve SON
> hacmi ayrı yazılır; PHYSICS/AUDIO satırı ikisini de taşır.

| Hacim | Ortam kartı | Yerçekimi / basınç / ses | Örnek (tek çekim) |
|---|---|---|---|
| NEREV-4 yüzeyi (dış cephe, siper, uçuş koridoru, T3 çatısı) | §3.4 KALIN ATMOSFER ya da §3.3'ün tarihli yeniden açılışı — Q2 sayısıyla | Q2 · dış ses meşru (ateş, enkaz, motor) | S00 · S24 · S77 |
| İnsan yapısı iç hacim: yeraltı hangar · servis koridoru · geçiş istasyonu · T3 platformu · rezerv odası · kuru servis havuzu | §3.10 BASINÇLI İÇ HACİM (gezegen g) | Q2 g · kapalı hacim yankısı · dış çatışma boğuk | S08 · S36 · S62 · **S85** (rezerv odası — REV 2'de eksikti) |
| K-1 kabini — yerde / yüzeyde uçuşta | §3.10 (gezegen g + itki) | kabin sesi · dış ses boğuk | **S04** (V05: K-1 hangarda yerde — KABİN, hangar değil) · S30 |
| K-1 kabini — sıçrama sonrası | §3.10 basınçlı, **mikro-g** (itki yoksa); kabin havasızsa AYRICA kurulur, kurulmadı → basınçlı | kabin fanı · nefes · dış ses YOK | **S94** |
| C-0 komuta odası (Veyra) | §3.10 türevi — Veyra iç hacmi (Veyra g/p kararı PLAN'da) | Veyra ses paleti | S09 · **S44** · **S60** (V61 varış tarafı) · S64 · S70 |
| Dış uzay — kafes sınırının dışı | §3.1 VAKUM | dış ses yok; yalnız kabin/telsiz perspektifi | S93 · S95 |

Geçişli çekimler (BAŞ → SON hacim ayrı yazılır): S23 (hangar → yüzey) · S31 (uçuş → servis havuzu)
· S45–S47 (istasyon → geçit → T3 platformu) · **S60** (T3 sabit geçit → C-0) · S86 (çatı → K-1 kabini)
· S92 (kafes altı atmosfer → vakum sınırı). Liste tablo yazılırken tamamlanır; burada örnektir.

`PHYSICS:` / `AUDIO:` satırı her promptta o hacmin değerini taşır; aynı hacimde AYNI sayı.

### 3.7 Kara delik ve ışık — dünya-göreli (G6)

```
PLAN (UZAMSAL_HARITA kuşbakışı):  kara delik ışıklı halkası = pusula yönü <X> (T3 batı çıkışında;
                                   halkanın yönü buna göre seçilir, bir kez) · gölge yönü ters
PROMPT:                            o çekimin kamera yönü → halka ekranda nerede (sağ üst / sol üst /
                                   kadraj dışı) HESAPLANIR ve ekran uzayında yazılır; pusula kelimesi prompta girmez
KONTROL:                           ⑨ KADRAJ + ⑪ IŞIK: her çekimde ÜÇ girdi birlikte — dünya-göreli yön ·
                                   kamera yönü · görüş alanı (lens) → beklenen sonuç ÜÇ hâlden biri:
                                   halka ekranın <şu> tarafında / KADRAJ DIŞINDA (ışık-gölge yönü yine
                                   tutarlı) / kısmen kenarda. Tabloya "KAMERA YÖNÜ (pusula)" + "HALKA:
                                   konum|dışarıda" sütunu. ⛔ "ters açıda ters tarafa geçer" gibi otomatik
                                   sağ-sol şartı YOK — kamera döndüğünde halka kadraj dışında kalabilir.
```

### 3.8 Karar kaynağı etiketi — her kayıtta zorunlu

```
ÖNCEKİ KULLANICI TALEBİ   sahibin dosyaları/mesajlarında zaten yazılı (S1–S6, dikkat.md maddeleri)
                          → kayıt: "kaynak: sahip · <dosya/mesaj> · <tarih>"
UYGULAMA TERCİHİ          ajanın gerekçeli kararı (G1–G10) → kayıt: "kaynak: uygulama tercihi · gerekçe · <tarih>";
                          sahip görmüştür ama ONAYLAMAMIŞTIR — itiraz gelmemesi onaya ÇEVRİLMEZ
YENİ KULLANICI ONAYI      sahibin açık cevabı (Q1–Q4 · ⏸ 2/3/4 kararları · hikâye onayı)
                          → kayıt: "kaynak: sahip onayı · <tarih> · <cümle birebir>"
⛔ Cevapsız soru "uygulama tercihi" olarak DEVAM EDEBİLİR (iş durmaz) ama etiketi ONAY olmaz;
   PLAN SAPMA bölümünde ⬜ AÇIK kalır.
```

---

## 4. GÖREVLER — faz faz

> ⬜ yapılacak · 🔶 sahip kararı · ✅ bitti. Durma yalnız §0'daki dört noktada.

### FAZ 0 — FORMAT AÇILIŞI (Kart H)

| # | Görev | Dosya | Durum |
|---|---|---|---|
| T0.1 | KILAVUZ_REHBERI **§2.8 YATAY 16 DK — 96 SAHNE · 8 BÖLÜM · QA 4 PART + TAM FİLM** kartı: §2.7 kalıbı; "yazım §2.3 ile aynı; fark: QA birimi PART (2 bölüm dosyası = 1 part) + tam-film koşusu"; viral ara 24'te 4 → 96'da 16; kurgu kapısı 960 s ±0; dürüst kayıt: sıfır filmle açıldı | `KILAVUZ_REHBERI.md` §2.8 · §2.0 bölüm listesi `yatay 16 dk 8` | ✅ |
| T0.2 | `yatay_16_dk_filmler/README.md` — format tablosu · süre hesabı (tam 10 s sabitleme kuralı) · iskelet BOLUM_1…8 · QA bloğu: 4 part koşusu + beyan satırı "THIS FILE IS PART n OF 4 — scenes Sxx–Syy" + **TAM-FİLM koşusu** (④ ⑫ ③ + replik tablosu) + maske tablosu + üç sınır çifti + kayıt etiketi P1–P4/FULL | `yatay_16_dk_filmler/README.md` | ✅ |
| T0.3 | `film_klasoru_ac.sh`: `yatay_16_dk_filmler) BOLUM=8 ;;` + kullanım örneği | `film_klasoru_ac.sh` | ✅ |
| T0.4 | `sayac.sh` dört listeye `yatay_16_dk_filmler` · AGENTS §1 harita · YAPI_GRAFI (⚠️ `yatay_10_20` eski ad düzeltmesi AYRI İŞ — Q4, buraya karışmaz) | `sayac.sh` · `AGENTS.md` · `YAPI_GRAFI.md` | ✅ |
| T0.5 | `rapor_kontrol.py --bolum n/m`: part↔dosya eşlemesi (k dosya / m part → PART n = dosyalar (n−1)k/m+1 … nk/m) — şu an yalnız BOLUM_n sayıyor, ①.9 yanlış ateşler · `--bolum full` ya da bayraksız tam-master koşusu için maske YOK · `t_tablo.py` `**Film** B3/B4/FULL` anahtarı DOĞRULA · `RAPOR_KONTROL/00_README` | `rapor_kontrol.py` · `t_tablo.py` | ✅ |
| T0.6 | `00_INDEX.md` yeni bölüm "YATAY 16 dk · 96 sahne · 8 BÖLÜM · QA 4 PART + TAM" (beş satır: B1–B4 + FULL) · şablon SPEC `PART GRID` n part + `FULL` satırı · `qa-isle` + `yeni-film` SKILL format listesi | `00_INDEX.md` · şablon SPEC · iki SKILL | ✅ |
| T0.7 | Kontrol: `bash sayac.sh` yatay_16 satırı; `git status` | — | ✅ |

### FAZ 1 — SABİT KARARLAR (tek mesaj · ⏸ 1)

| # | Görev | Durum |
|---|---|---|
| T1.1 | Kart A dört sorusu KAPI olarak tek turda geçilir (cevaplar §3.1'den: konu sahibin · 16 dk · 96 · referans YAZILIR) — mülakat değil | ✅ |
| T1.2 | Hikâye onayı (0.7): 96 satır sahibin V satırlarından ≤15 kelime; LOGLINE · NEDEN İZLENİR · BEDEL. Hikâye ÜRETİLMEZ, taşınır | ✅ |
| T1.3 | §3.2 uygulama tercihleri + §3.3 dört gerçek soru AYNI mesajda. Tercihler BİLDİRİLİR ve `uygulama tercihi` etiketiyle kaydedilir; Q1–Q4 CEVAP BEKLER — cevapsızlık onay değildir (§3.8) | ✅ (19.09.2026 · hikâye ONAY TUR 1/3 + beş not uygulandı · Q1–Q3 cevaplandı) |
| T1.4 | `00_HIKAYE_ONAYI.md` (betik damgalar; ONAY tarihli · sahip · TUR n/3) → yeni rejim. Her karar satırı KAYNAK etiketi taşır (§3.8) | ✅ |

### FAZ 2 — KLASÖR · OKUMA · ANALİZ (Kart A 1–6, sıkıştırılmış)

| # | Görev | Durum |
|---|---|---|
| T2.1 | `bash film_klasoru_ac.sh yatay_16_dk_filmler THE_STOLEN_SKY 96` → 8 BOLUM · 96 satırlık `00_SAHNE_TABLOSU` · çizelge · HIKAYE_ONAYI kopyası. **Sonra** `git mv`: `ANA_PLAN` → `THE_STOLEN_SKY/00_ANALIZ/00_SAHIP_ANA_PLAN_96_VIDEO.md` (KRONOS emsali) · README + dikkat + araştırma → `00_ANALIZ/00_SAHIP_NOTLARI.md` · bu TODO → `00_ANALIZ/00_TODO_GOREV_PLANI.md` · 96 klip dosyası → `05_SAHNE_CALISMALARI/00_96_KLIP_PROMPT_HAZIRLIK.md` · `ilk_deneme/` silindi (dosyalar git'te yoktu → düz mv) | ✅ |
| T2.2 | Beş kilit dosya: `--kilit-sahne … S00 HOOK · S16 NOVUM · S59 BEDEL · S84 DORUK · S94 FINAL` (G3) | ✅ |
| T2.3 | Okuma çizelgesi: yaşayan 40 ders ("—" meşru) · manifest ≤30 · havuzdan: SAVAS_SENARYO · UZAYLI_VARLIK · UZAY_USSU (T3 ölçek 1H) · SAHNE_DOLULUGU · PROMPT_HATA_ONLEME (19.09 zorunlu) · OMNI/VEO (Q1) · POLITIKA §4 · **09_URETIM_RED_DEFTERI** (§3.5 kaynak satırı) · UZAMSAL_HARITA (G6) | ✅ |
| T2.4 | Beş QA kaydı: THE_FALLING_WORLD (sahip-yazımı, opak) · THE_HARD_DOCK (24 × 10 s ölçek) · MARS_SON_CIKIS (①.9 yapı uyuşmazlığı) · THE_STATIC_SHADOW (13 mercek geçersiz) · KRONOS_SON_SINYAL (%93 🅑 kapsama düşüşü) | ✅ |
| T2.5 | `01_QA_DERS_HASADI` (≤20 kilit) · `02_KONSEPT_VE_RISK` (SAPMA satırları S2–S6 · ortam §3.6 tablosu · konsept kapısı · TEMA G2 · B5: İSTEK iki gemiyi çıkarmak · ENGEL kafes+kalkan+yedekleme+Serrak · BEDEL S59 + S84 · MUHATAP Serrak · AYRILIK Rey S55 / Bor S58 · 4 KARAKTER KARTI · risk kartları · **B6 en red-riskli 5 kare + nötr tarif:** S59 · S38 · S22 · S51 · S90 · ORAN SETİ G9) · `03_SAHNE_SIRALAMASI` (sıra sahibinin; 88 + 7 ardışık çift — sekans içi devam MUAF G7; kurulum iskeleti 96 harf KÜME ≥2 DÖNÜŞ ≥%40; "görünür sebep" sütunu; replik 8 post-dub tablosu; ÜRETİM SIRASI: denemeler → S84 → S92 → S94/95 → S00 → S59 → sınır çiftleri → BOLUM_8 → BOLUM_1 → kalan; İPTAL KAPISI S84 · S59 · S00 · S22) · `04_UYARI_NOTLARI` | ✅ |
| T2.6 | `00_SAHNE_TABLOSU` 96 satır + ek sütunlar: BASKIN EYLEM · SON 3 s (beş sınıf G8) · KAMERA YÖNÜ pusula + HALKA konum/dışarıda (G6) · **HACİM — her çekim TEK TEK, geçişte BAŞ→SON** (§3.6) · PROMPT ✅ (kalan sayı buradan hesaplanır) · İLİŞKİ PLANI (§3.4) · SABİT REFERANSLAR (Bor 0 kare S60+ · K-1 S29→S33→S66→S68/S78/S92→S90 · Mara göğüs izi S03+ · Bor diz S51+ · E-2 yüzey S89+ · anahtar S39→S64 · Serrak konumu) | ✅ |

### FAZ 3 — TASLAK REFERANSLAR + ALTI DENEME P1–P6 (⏸ 2) — promptlardan ÖNCE

```
ERKEN YAZILAN SAHNELER (benzersiz kimlik):
  kilit 5      S00 · S16 · S59 · S84 · S94
  deneme       P1 S48 · P2 S01 · P3 S02 (ya da S20) · P4 S68 · P5 S90 · P6 S59 (kilitle ortak) + S38
  = 11 sahne (P3 tek sahne) / 12 sahne (S02 VE S20) → 22 / 24 prompt (📸 + 🎥 ayrı sayılır)
  KALAN = 96 − erken yazılan benzersiz sahne = 85 / 84 — sayı ELLE TUTULMAZ, 00_SAHNE_TABLOSU'ndaki
  KAPI ✅ / PROMPT ✅ sütunlarından hesaplanır (grep ile; T2.6)
```

| # | Görev | Durum |
|---|---|---|
| T3.1 | **TASLAK referans paketi** (G1'in 6 sayfası, "TASLAK" damgalı): NB2/imaj promptları; küçük ekran siluet testi (dört insan + Veyra + K-1 ↔ avcı 120 px'te ayrışıyor mu) | ✅ 20.09 — `THE_STOLEN_SKY_REFERANS_PAKETI.md` R1–R6 (22 panel), kabul kapısı ⬜ (sayfalar üretilince) |
| T3.2 | Erken sahnelerin promptu: 5 kilit + 6–7 deneme sahnesi = **11/12 sahne × (📸 + 🎥) = 22/24 prompt** — V3 şablonu, PHYSICS/AUDIO sayılı; `prompt_kontrol.py` DOSYA modu bu promptlara (Kart P: tek kare üretmeden önce) | ✅ 20.09 — T5.2 ile birlikte 96/96 yazıldı (sahip talebi); deneme sahneleri S48 S01 S02 S68 S90 S59 S38 BOLUM dosyalarında |
| T3.3 | **DENEMELER — üretim:** P1 çoklu figür çatışma (S48 örtüşen kalkanlar, kararlı genel plan) · P2 kalkanın darbeyi yönlendirmesi (S01) · P3 geçitten çıkış (S02 / S20) · P4 hasarlı geminin uçuşu (S68 sabit açılı sağ itki) · P5 iki geminin birbirini koruması (S90) · **P6 red probu** (S59 ve S38 nötr tarifi — §3.5 araç kuralı) · Q1 iki motorsa ikisinde de. Her deneme: kabul/red + neyin okunmadığı + sadeleştirme önerisi → `URETIM_DEFTERI` §0b | ⬜ |
| T3.4 | TUR 23 paralel: `26_COKLU_FIGUR_VFX_UCUS_ARASTIRMA_PROMPTLARI.md` (3 prompt: çatışma okunurluğu · kalkan/portal/kafes VFX dili · hasarlı uçuş + iki gemi) → sahip koşar → `TUR23_HAM_RAPORLAR/` → `04_ARASTIRMA_BULGULARI` süzme (kılavuz gerekirse yazılır, FAZ 5'ten önce) | ⬜ |
| T3.5 | ⏸ 2 — deneme sonuçları sahibe: hangi sahne sadeleşir, hangi motor. **Sadeleştirme kuralı:** her denemenin KORUNACAK BİLGİSİ önce yazılır, sadeleştirme o bilgiye dokunmaz. P1 (S48): korunacak bilgi = *iki kalkanın birbirinin açığını kapattığı görülür* → sadeleştirme sırası: ① kamera hareketi kaldır (tam lockoff) ② arka planı boşalt ③ eşzamanlı üçüncü hareketi (Mara'nın atışı) sonraki klibe taşı ④ iki askeri yan yana sabit tut, yalnız kalkan açıları hareket etsin. ⛔ "tek asker + kalkan çizgisi" gibi ikinci figürü silen çözüm P1 için GEÇERSİZ — sorunu geri getirir. Diğer P'ler için korunacak bilgi: P2 sapan ateşin YÖNÜ · P3 işaretleyici ↔ kapı bağı · P4 sağ itki sabit açı = savrulma yönü · P5 K-1'in E-2 ile ateş arasına GİRDİĞİ. Kararlar ANA_PLAN'a dokunmaz, 02_KONSEPT SAPMA'ya yazılır | 🔶 |

### FAZ 4 — 16 DAKİKALIK ÖN KURGU (⏸ 3) — dikkat 7

| # | Görev | Durum |
|---|---|---|
| T4.1 | 96 referans karesi (taslak paket + deneme kareleri + basit çizim) × tam 10 s + geçici telsiz sesleri (8 replik dâhil) + geçici müzik → animatik 16:00 | ⬜ |
| T4.2 | Animatik değerlendirmesi (sahibin dört sorusu): hedef anlaşılıyor mu (V01–V12) · orta bölüm uzuyor mu (BOLUM_3–6) · Bor'un kaybı etkili mi (S58–S61) · final beklentiyi karşılıyor mu (S84–S95) · mekân coğrafyası okunuyor mu · açıklama uzun mu | ⬜ |
| T4.3 | ⏸ 3 — bulgular sahibe; sahne düzeyi değişiklik SAPMA olarak kaydedilir; kalan promptlar bu sonuçlara göre yazılır | 🔶 |

### FAZ 5 — KALAN PROMPTLAR + PAKET

| # | Görev | Durum |
|---|---|---|
| T5.1 | `THE_STOLEN_SKY_PLAN.md`: format · TEMA (G2) · NOVUM · B5 + 4 KART · vuruş · hook · sahne haritası 96 · ÇAPA ÜÇLÜSÜ (CHOICE S84 · COST S59 · FINAL S94) · AYRILIK · replik tablosu (post-dub, saniye HESAPLATILIR) · kurulum iskeleti · Bible'lar (İnsan ×4 · Veyra+Serrak · Araç ×5 · Dünya kuşbakışı harita · Mekân ×8 · Camera · Negative) · sayısal kilitler (Q2 g/p · 60 s · 20 s · V88 ilk kare 14:30) · ORAN SETİ · politika · ÜRETİM SIRASI · SAPMA · UYGULANMAYAN KİLİTLER · DENEME SONUÇLARI özeti | ✅ 20.09 (`plan.py` üretir; 4 KARAKTER KARTI 02_KONSEPT §7'de, PLAN'a kopyalanmadı — kart prompta girmez; DENEME SONUÇLARI ⬜ üretimden sonra) |
| T5.2 | Kalan **85/84** sahnenin 📸 + 🎥 promptu (film toplamı 192 prompt; kalan sayı tablodan hesaplanır, FAZ 3 kutusu): V3 + PROMPT_HATA_ONLEME §2 · PHYSICS/AUDIO hacme göre (§3.6) · IN FRAME ilk satır · kelime bandı · TIMELINE ≤3 satır, son 3 s beş sınıftan biri (G8) · tek baskın eylem · tırnak yok · yön ekran uzayında (G6 hesabı) · uzaylı arayüzünde okunur metin yok · devam klibi: gerçek son kare (motor Q1) · self-contained · insansız sahneler kısa NEGATIVE · deneme sonuçlarının sadeleştirmeleri uygulanmış | ✅ 20.09 — 96/96 × 2 = 192 prompt (sahip talebi ile öne alındı); ⚠️ deneme sadeleştirmeleri HENÜZ yok (P1–P6 sonrası b*.py düzeltilip yeniden üretilir) · G6 yön: nesne-göreli (D174, ekran uzayı yerine) |
| T5.3 | Onaylı **REFERANS PAKETİ** (TASLAK → ONAYLI; seed'ler; 96 satırlık sahne→referans eşlemesi; KAPI 0 [D168]) | ⬜ |
| T5.4 | **QA_SPEC** ㉔ yedi çapa: **A** GRID · `DIALOGUE LINES: 0 (prompts)` + `POST-DUB LINES: 8` · `PART GRID` 4 satır + `FULL 0–960 s` · CLIP COUNT 96 · KIRPMA/SABİTLEME satırı (ham → tam 10 s, fps Q3) · **B** İNSAN ŞERİDİ 4→3 · üç sınır çifti EŞ KADRAJ · FİNAL VURUŞ KANITI (S95: 3 insan gemisi tek karede; S94: kapatılan kemer 1 adet) · kalıcı hasar zinciri · ÇAPA ÜÇLÜSÜ · **C** belgesiz mercek kilitleri (üç şekil · halka yönü dünya-göreli · Veyra anatomi · ilişki planları) · **E** makine kapıları, her biri KOMUT · DOĞRULANDI (ffmpeg sürüm·tarih) · İKAME | ⬜ |
| T5.5 | `_MUZIK` (koridor 60 s tempo kilidi · S59 sonrası kask içi daralma) · `_KAPAK` ✅ 20.09 — A S00 tehlike · B S92 çıkış · TEK DENEY "göğe mi çıkışa mı" (FILM_KAPAGI_KILAVUZU; V93 yerine S92: kelepçe+kütük ve daralan kenarlar tek gövdede) · `_YAYIN_PAKETI` EN DRAFT · `_URETIM_DEFTERI` (§0 KAPI 0 + araç ayarı + animatik kaydı · §0b P1–P6 sonuçları · 96 satır üretim sırasıyla · TESLİM SATIRI) | ⬜ |

### FAZ 6 — KAPI + KAYIT

| # | Görev | Durum |
|---|---|---|
| T6.1 | `03_PLAN_ONCESI_KONTROL_LISTESI` 18 madde · `prompt_kontrol.py` KLASÖR modu (8 dosya birleşik) → 0 BLOCK; beklenen FIX'ler (D79 · figür imzası · dosya-modu iskelet) PLAN'a kayıtlı · `prompt_hata_analizi.py --kilit THE_STOLEN_SKY` `HİÇ YOK` satırı yoksa geç · DIALOGUE_CRITIQUE: prompt tarafı "NO DIALOGUE FOUND" BEKLENEN — bu bir başarı değil, KAPSAM sınırı; replik denetimi FAZ 8 T8.6'da | ⬜ |
| T6.2 | KILAVUZ_REHBERI §8 satırı · 00_INDEX beş satır (B1–B4 + FULL) 0/4 · README notu · TEMA §3b SORUMLULUK aday satırı · SAHNE_DOLULUGU'na G8 tarihli not · UZAYLI_VARLIK §① istisna notu · `bash sayac.sh` · hafıza · **commit SAHİBİN** | ⬜ |

### FAZ 7 — ÜRETİM (Kart B)

| # | Görev | Durum |
|---|---|---|
| T7.1 | İlk kabul klibinde ham süre `ffprobe` (D124 kaydı) → kurgu birimi tam 10,000 s'e sabitlenir (Q3 fps); KIRPMA satırı SPEC'e; **zaman kodları DEĞİŞMEZ** | ⬜ |
| T7.2 | Üretim sırası: S84 → S92 → S94/S95 → S00 → S59 → sınır çiftleri (S23/24 · S47/48 · S71/72) → BOLUM_8 → BOLUM_1 → kalan; her klip URETIM_DEFTERI satırı (prompt kaynağı · seed · deneme · kabul); KAPI 0 referans onayı | ⬜ |
| T7.3 | Kurgu: TAM master 96 × 10,000 s = 960,000 s (±0 · KURGU_VE_TESLIM kapısı) · koridor V88 ilk kare = 14:30,000 · **SESLİ master** (8 post-dub replik + müzik) · 4 PART master SESLİ masterdan kesilerek ihraç (QA aracı; sessiz/geçici sesli ihraç edilirse ③ partta `uygulanmadı`) · üç sınır çifti `ffmpeg -frames:v 1` yan yana | ⬜ |

### FAZ 8 — QA: PARÇA KONTROLLERİ + TAM FİLM (⏸ 4)

| # | Görev | Durum |
|---|---|---|
| T8.1 | **PART koşuları (teknik devamlılık):** her part ①–⑫ TEMİZ oturumda, SPEC + "THIS FILE IS PART n OF 4" [D129] → 48 rapor · ham `<FILM>_B<n>_<MERCEK>_HAM.md` · `rapor_kontrol.py … --bolum n/4` (T0.5) · maske §1. **③ SES kuralı:** part masterlar NİHAİ SESLİ masterdan kesilir (T7.3); öyle değilse (geçici ses / sessiz) part ③ hücresi `uygulanmadı` yazılır, ortalamaya girmez. Nihai ses kabulü her durumda FULL (T8.5) | ⬜ |
| T8.2 | ⑬ UYUM tek koşu, üretim defteri üzerinden (bölümden etkilenmez) | ⬜ |
| T8.3 | **TAM-FİLM koşusu (görüntü + hikâye):** ④ HİKAYE ve ⑫ HOOK tam master'a, SPEC + "THIS FILE IS THE FULL FILM — 96 scenes" beyanı; Structure · Retention · Plateau · Rhyme burada SAYI TAŞIR · rapor_kontrol maskesiz koşu · ham `<FILM>_FULL_<MERCEK>_HAM.md` · tablo satırı `**THE_STOLEN_SKY** FULL` | ⬜ |
| T8.4 | Tam-film hikâye kontrolünün dört sorusu (sahip): hedef anlaşılmış mı · orta bölüm uzuyor mu · Bor'un kaybı etkili mi · final hazırlanan beklentiyi karşılıyor mu — ④'ün kategorilerine ek satır olarak SPEC A'ya yazılır, rapor bunları cevaplamak zorunda | ⬜ |
| T8.5 | **TAM-FİLM SES koşusu:** ③ SES nihai sesli master'a — nihai sesin KABULÜ yalnız burada. Part ③ satırları (T8.1) teknik ön bulgudur, kabul değildir | ⬜ |
| T8.6 | **Replik tablosu denetimi:** 8 post-dub replik — sahne · hesaplanmış saniye · anlaşılırlık · dudak/kask uyumu (opak vizör: dudak yok, kask yönü + telsiz perspektifi) · zamanlama (görüntüdeki eyleme oturuyor mu) → ③ raporuna ek blok; `POST-DUB LINES: 8` bu tabloyla kapanır | ⬜ |
| T8.7 | Kayıt: `01_FILM_RAPORLARI/THE_STOLEN_SKY.md` — "## PART 1–4" + "## TAM FİLM" başlıkları · T1–T12 beş satır · 00_INDEX beş satır · ⛔ kesme/yeniden sıralama part raporundan uygulanmaz; TAM-FİLM raporundan sahip kararıyla uygulanır (⏸ 4) | ⬜ |
| T8.8 | Kart G: 16 dk ilk koşusunda ①.11 ORTA maskesi + tam-film koşusu SINANIR; §2.8 kartı ölçüme göre düzeltilir (önce belge revizyonu, sonra ders) | ⬜ |

---

## 5. SAHNE NASIL OLACAK — 96 birimin ortak yazım kalıbı

```
BİRİM         tam 10,000 s · tek çekim · tek baskın eylem · sonucu görünmeden kesilmez (sahip)
SON 3 s       beş sınıftan biri: SONUÇ · TEPKİ · KARAR · BİLİNÇLİ BEKLEYİŞ · SÜRDÜRME — soru:
              "bu süre izleyiciye ne kazandırıyor?" Tamamlanmış eylem uzatılmaz.
SEKANS İÇİ    aynı kamera + eylem + mekân sürüyorsa: önceki klibin GERÇEK SON KARESİ sonraki klibin
              başlangıç görseli (motor Q1). Yeni açıya geçiliyorsa aynı olay anını ve mevcut hasarları
              taşıyan yeni başlangıç karesi. Ardışık çift bandı bu kliplere UYGULANMAZ (G7).
SEKANS ARASI  SAHNE_ZINCIRI sınır satırı End(n)/Start(n+1); durum değişimi (hasar, kayıp, el
              değiştiren nesne) SINIRA yazılır; ölçek/açı bandı BURADA uygulanır.
FİGÜR         yakın/orta planda 1–2 insan + ≤1 Veyra; İLİŞKİ planlarında (§3.4) iki figür birlikte,
              kararlı kamera, tek eylem. Dört insan birlikte: V09 · V24 · V33 · V48 · V56.
              Savaş ölçeği: uzak araçlar + yapı hasarı + ses, kalabalık değil.
KAMERA ↔ FİZİK hızlı kamera → sade geometri; kalkan/portal olayı → kararlı kamera. İkisi aynı prompta yüklenmez.
ÜÇ ŞEKİL      kalkan = öne bakan kavis · portal = iki işaretleyici arasında sınırlı kapı ·
              kafes = gökyüzünde geniş amber örgü. Aynı ışık efekti üçü için kullanılmaz.
İNSAN BAŞARISI her başarıda görünür sebep: açı · örtü · anahtar · fiziksel konum · enerji sınırı.
KARA DELİK    dünya-göreli yön (PLAN haritası); ekrandaki yeri kamera yönünden hesaplanır; ışık/gölge aynı.
VİZÖR         opak siyah; parlaması, yansıması, kokpit ışığı yüzü açmaz; dudak senkronu gerektiren plan yok.
EKRAN METNİ   postta; uzaylı arayüzünde okunur metin üretilmez [D138].
FİZİK/SES     PHYSICS: <hacmin g · p — §3.6> · AUDIO: <hacmin ses yasası>; aynı hacimde aynı sayı.
KALICI OLAN   hasar, el değiştiren nesne, mühimmat, boş koltuk — devam klibi temiz giysi / sağlam araç göstermez.
REPLİK        prompt içinde 0; nihai filmde 8 (post-dub, EN); dinleyen klibinde metin yok; telsiz başka açıya taşınabilir.
```

---

## 6. SAHİBİN 20 ARAŞTIRMA BAŞLIĞI ↔ DEPO — iki ayrı sütun

> "Kaynak mevcut" bu filmde yöntemin çalıştığını kanıtlamaz. İkinci sütun FAZ 3 denemesi
> ya da FAZ 8 ölçümüyle dolar; şimdi hepsi ⬜.

| # | Başlık | Kaynak mevcut mu | Bu filmde deneme/ölçüm |
|---|---|---|---|
| 1 | YouTube bilimkurgu/aksiyon izleyicisi | apexaic KANAL_KIMLIGI · YAYIN_VE_PERFORMANS · 08 tablosu | ⬜ FAZ 8 sonrası yayın verisi |
| 2 | ilk 30 saniye | HOOK_VE_ILK_SAHNE · ⑫ | ⬜ animatik T4.2 + FULL ⑫ |
| 3 | 16 dk gerilim ritmi | KURGU_RITMI · §2.5 oran bantları (8 dk'ya kadar) | ⬜ FULL ④ Structure/Retention — 16 dk ilk ölçüm |
| 4 | kara delik bilimi | YOK — Bible varsayımı (G6) | ⬜ ⑪ IŞIK tutarlılığı |
| 5 | gezegen + koloni görsel tasarımı | UZAY_USSU (ölçek 1H) · TUR 18 dünya promptu | ⬜ T3.1 taslak referans |
| 6 | yüz göstermeden duygu | KARAKTER_VE_DUYGU · OYUNCULUK_YAZIM · FALLING_WORLD | ⬜ ⑩ OYUNCULUK |
| 7 | uzaylı anatomi/zırh/hareket | UZAYLI_VARLIK (tek varlık; asker/komutan ayrımı yok) | ⬜ T3.1 sayfa ② + P1 |
| 8 | teknoloji kurallarının anlaşılırlığı | ONERME_VE_NOVUM · sahibin tablosu | ⬜ animatik T4.2 |
| 9 | savaş davranışı, karşı hamle | SAVAS_SENARYO | ⬜ ⑦ AKSİYON |
| 10 | koreografi okunurluğu | ⑦ ⑮ rubrikleri · POLITIKA §4 — YAZIM kılavuzu YOK | ⬜ **P1 + TUR 23 ①** |
| 11 | mekân coğrafyası | UZAMSAL_HARITA | ⬜ animatik + ⑮ YÖN |
| 12 | araç tasarımı/ölçek/hareket | Vehicle Bible şablonu (⬜) · YANASMA — hasarlı uçuş YOK | ⬜ **P4 + P5 + TUR 23 ③** |
| 13 | kamera dili, ışık, kadraj | SINEMATOGRAFIK · KAMERA_ACISI · ACI_YAYI | ⬜ ⑨ ⑪ |
| 14 | araçların gerçek kapasitesi | OMNI · VEO kılavuzları · D124 | ⬜ **P1–P6 (Q1 motor)** |
| 15 | referans hazırlığı | REFERANS_PAKETI_KILAVUZU · 24_ NB2 promptları | ⬜ T3.1 siluet testi |
| 16 | uzun sahneyi 10 s'e bölme | SAHNE_ZINCIRI · SAHNE_DOLULUGU · TEK_CEKIM | ⬜ P2/P3 zincir + ② |
| 17 | VFX / fiziksel etkileşim | ⑥ FİZİK · D38 — kalkan/portal yazım dili YOK | ⬜ **P2 + P3 + TUR 23 ②** |
| 18 | devamlılık yönetimi | SAHNE_DEVAMLILIK · ② · SPEC B | ⬜ ② × 4 part + sınır çiftleri |
| 19 | ses/müzik/kurgu | SES_VE_DIYALOG · GOOGLE_FLOW_MUSIC · KURGU_VE_TESLIM | ⬜ FULL ③ + T8.6 |
| 20 | maliyet/deneme/yayın | URETIM_DEFTERI · PAKETLEME_VE_VAAT | ⬜ FAZ 3 deneme maliyeti kaydı |

---

## 7. REVİZYON KAYDI — eleştiriden ne değişti

| Eleştiri | Nerede kapandı |
|---|---|
| 1 tam-film kontrolü eksik | §1 maske notu · T8.3–T8.6 · T0.5/T0.6 FULL satırı |
| 2 zor çekimler geç | §0 sıra · FAZ 3 (deneme + taslak referans) ve FAZ 4 (animatik) FAZ 5'in önüne |
| 3 süre sapması 10 s'i gevşetiyor | S5 · T7.1 · T7.3 (960 s ±0) · SPEC KIRPMA satırı |
| 4 DIALOGUE 0 eksik beyan | G4 · T5.4 iki satır · T6.1 kapsam notu · T8.5–T8.6 |
| 5 V95 vakum hatası | §3.6 hacim tablosu (S94 basınçlı kabin) · G5 |
| 6 kara delik ekran koordinatı | G6 · §3.7 · tabloda KAMERA YÖNÜ sütunu |
| 7 tek Veyra sınırı | S3 · §3.4 ilişki planları |
| 8 Bor'un ölümü yalnız ışık | S4 · §3.5 (üç işaret + kaynak tablosu + P6 red probu) |
| 9 onay yükü | §3 üç sınıf · §0 dört durma noktası · FAZ 1 tek mesaj |
| 10 mekanik kurallar | G7 (devam klipleri muaf) · G8 (beş sınıf, "ne kazandırıyor") |
| 95 çift | §1: 88 bölüm içi + 7 sınır = 95 |
| DORUK S84/S92 | G3: S84 dramatik seçim (dosya) · S92 fiziksel doruk (tablo + P4/P5) |
| "kapalı" araştırma | §6 iki sütun |
| T0.7 klasör taşıma | T2.1'e alındı |
| sayaç eski ad | Q4 ayrı iş, kapsam dışı |

**REV 3 — ikinci eleştiri:**

| Eleştiri | Nerede kapandı |
|---|---|
| 1 deneme/kalan sayı | §0 · FAZ 3 kutusu (11/12 sahne · 22/24 prompt · kalan 85/84, tablodan hesaplanır) · T3.2 · T5.2 |
| 2 ortam aralıkları çakışıyor | §3.6 aralıklar kaldırıldı, hacim tanımı + tek çekim örnekleri; atama T2.6 HACİM sütununda tek tek, geçişte BAŞ→SON (S04 kabin · S44/S60 C-0 · S85 rezerv odası düzeltildi) |
| 3 kara delik kontrol cümlesi | §3.7: üç girdi (dünya yönü · kamera yönü · görüş alanı) → konum / kadraj dışı / kenar; otomatik sağ-sol şartı kaldırıldı |
| 4 part ses raporu | T7.3 partlar sesli masterdan · T8.1 ③ `uygulanmadı` kuralı · T8.5 kabul yalnız FULL |
| 5 P1 yedek çözümü | T3.5 korunacak bilgi + sadeleştirme sırası; ikinci figürü silen çözüm geçersiz |
| 6 P6 kural kanıtı değil | §3.5 iki ayrı satır: resmî kural kaynağı (FAZ 2) · deneme kaydı (P6) |
| 7 sessizlik ≠ onay | §3.8 üç etiket · ⏸ 1 · T1.3 · T1.4 |

### REV 4 — 20.09.2026 (akşam) · sahip: "8 bölümde de promptlar yok, neden hazırlamadın?"

```
· Sıra değişti: PLAN (T5.1) + 192 prompt (T5.2 + T3.2) + taslak referans (T3.1) + QA_SPEC aynı oturumda yazıldı; denemeler (T3.3) promptlardan SONRA koşacak
  ve sonuçları üretecin b*.py dosyalarına işlenip promptlar yeniden üretilecek (elle düzeltme yok).
· Üreteç: 00_ANALIZ/06_PROMPT_URETECI/ (common · render · plan · b1–b8) — aynı harf aynı CAMERA, aynı hacim aynı PHYSICS/AUDIO, çekirdek NEGATIVE birebir.
· prompt_kontrol klasör modu: 0 BLOCK · 10 FIX — 9 × D79 (opak vizör, betiğin kendi notu: tasarım gereği düşer) · 1 × DÖNÜŞ 36/96 %37,5 (D74 sapma).
· Sahibin ANA_PLAN dosyası köke `*_PLAN.md` deseniyle çakıştığı için 00_ANALIZ/00_SAHIP_ANA_PLAN_96_VIDEO.md'ye taşındı (içerik değişmedi).
· 00_HIKAYE_ONAYI: üç satırda "kilitler/kilitlenir" eş anlamlısıyla değiştirildi (㉙ jargon kapısı); olay değişmedi. 00_OKUMA_CIZELGESI: 8 "— (not)" hücresi salt "—" (㉘).
· 🔶 AÇIK: S67 repliği (D217) · denemeler P1–P6 · referans sayfalarının üretimi + kabul kapısı · KLİP SÜRESİ ölçümü (D124).
```

### REV 5 — 20.09.2026 (gece) · sahip: GEMS olayı KOMPLE KALDIRILDI

```
· Üç tur Gemini Gem denemesi (filme özel → ortak arama aracı → ortak yazar) sahip kararıyla depodan tamamen çıkarıldı:
  GEMS klasörleri · GEMINI_GEM_KILAVUZU · gem_sync.py · şablon · betik/ATLA/harita kayıtları yok.
· Kalan tek iz — o sırada bulunan, Gem'den bağımsız üreteç hatası: S02 · S35 · S47 · S72'de figür klip İÇİNDE giriyor, t=0
  karesinde yokken IMAGE NEGATIVE "exactly N tall figures" diyordu → render.py `veyra_img` · 4 sahne yeniden üretildi · 0 BLOCK · 10 FIX aynı.
```
