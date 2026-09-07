# 📺 apexaic — üç hesap, tek kanal

`kilavuzlar_ve_sistem_dosyalari/` **filmi nasıl yapacağını**, format klasörleri
**hangi filmi** yaptığını, `FILM_QA_RAPORLARI/` **filmin geçip geçmediğini**
tutar. Burası dördüncü soruyu tutar: **film QA'dan geçtikten sonra ne oluyor.**

```
Kanal:   Apex AI Cinema
Handle:  @apexaic   ← hedef, üçünde de aynı (bugün: @apex_aic · @apex_aic ·
                       apex_aic/apexaic — geçiş: KANAL_KIMLIGI §7.2)
Ürün:    16:9 uzay bilimkurgu kısa filmi (2-4 · 3-5 · 7-20 dk)
         + 9:16 dikey kesim / dikey shorts
Tez:     ⭐ HER FİLM BİR GERÇEK FİZİK KURALIYLA HESAPLAŞIR   (KANAL_KIMLIGI §2)
Durum:   ⚠️ CANLI KANAL — 225 video · 14.09.2025'ten beri · ölçülmemiş
         (timelapse_md/apexait'ten temel fark: orası açılış planı, burası
          temizlik + kimlik birliği + ilk ölçüm)
```

---

## 🗂️ YAPI — ortak kökte, platforma özel klasörde

```
apexaic/
├── README.md                     bu dosya · okuma sırası · açık işler
├── 00_KANAL_DENETIMI_VE_PLAN.md  📋 01.09.2026 denetimi: bulgular · sahip
│                                    kararları (S1-S12) · uygulama sırası
├── KANAL_KIMLIGI.md              ⭐ ÜÇÜNDE DE AYNI — tez · kanal negatif
│                                    çekirdeği · palet/logo · dil · Hakkında
├── YAYIN_PLANI.md                ⭐ ÜÇÜNDE DE AYNI — kadans · iki ayak
│                                    (film + fragman) · ortam sırası · playlist
├── CAPRAZ_YAYIN.md               ⭐ ÜÇÜNDE DE AYNI — iki master · huni ·
│                                    filigran · C2PA · yükleme sırası
├── POLITIKA_VE_RISK.md           ⭐ ÜÇÜNÜ DE — yanıltıcı metadata · inauthentic
│                                    content · AI beyanı · haklar · kriz kartları
├── DIS_SAYILAR.md                ⭐ TEK TABLO — üç platformun dış sayıları,
│                                    doğrulama tarihi, kaynak
├── APEXAIC_INTRO_PROMPT.md       10 sn logo introsu (image + video prompt)
│
├── youtube/     HESAP_KIMLIGI.md · PAKETLEME_SABLONU.md
├── instagram/   HESAP_KIMLIGI.md · PAKETLEME_SABLONU.md
└── tiktok/      HESAP_KIMLIGI.md · PAKETLEME_SABLONU.md
```

```
⛔ KÖKTEKİ HİÇBİR ŞEY PLATFORM KLASÖRÜNE KOPYALANMAZ.
⛔ HİÇBİR DIŞ SAYI DIS_SAYILAR.md DIŞINDA YAZILMAZ — platform dosyası
   "→ DIS_SAYILAR §n" der, sayıyı tekrar etmez.
⛔ YAPIŞTIRILABİLİR METİN BLOKLARINDA PLACEHOLDER YOK (<kadans>, [link]).
   Sebep: kanalın canlı açıklamalarında "[Kanal Linkini Buraya Ekle]"
   bulundu (00_KANAL_DENETIMI §2.1). Karar değişirse tek satır değişir.
```

---

## 📖 OKUMA SIRASI

```
İLK KEZ OKUYORSAN
  1. 00_KANAL_DENETIMI_VE_PLAN.md   kanal bugün ne hâlde · ne kararlaştı
  2. KANAL_KIMLIGI.md               kanal ne · neyi reddediyor
  3. POLITIKA_VE_RISK.md            ⭐ kanalı ne öldürür
  4. YAYIN_PLANI.md                 ne zaman ne yayınlanıyor
  5. CAPRAZ_YAYIN.md                bir film üç hesaba nasıl gidiyor

YÜKLEME GÜNÜ — elinde tutacağın iki dosya
  · CAPRAZ_YAYIN.md §7              (çapraz kontrol listesi)
  · <platform>/PAKETLEME_SABLONU §5 (o platformun listesi ve metinleri)

ESKİ VİDEOLARI TEMİZLİYORSAN
  · 00_KANAL_DENETIMI §8 (sıra) + youtube/PAKETLEME_SABLONU (hedef biçim)
```

## 🧭 ÜÇ HESAP, ÜÇ AYRI İŞ

```
YouTube    ⭐ ürünün evi: tam film · arşiv · arama · para ayağı   → youtube/
TikTok     keşif: dikey kesim + fragman → tam filme huni          → tiktok/
Instagram  vitrin: dikey kesim + kare seti + "gönder" sinyali     → instagram/

⛔ Üçünde aynı metni paylaşmak çapraz yayın değildir. Bugün TikTok'ta
   YouTube açıklamaları caption olarak duruyor; sonucu 146 takipçi
   (00_KANAL_DENETIMI §2.2 D).
```

---

## ⛔ BU KLASÖR NE DEĞİL

```
· Üretim kılavuzu DEĞİL. Prompt, negatif çekirdek, kapak üretimi, ihraç
  ayarları → kilavuzlar_ve_sistem_dosyalari/. Buraya kopyalanmaz.
· Film klasörü DEĞİL. Filmler format klasörlerinde yaşar.
· QA DEĞİL. Yayın kapısı AGENTS.md Kart B/Y; paketlemeden ÖNCE koşar.
· Ölçüm tablosu DEĞİL. Gerçek izleyici sayıları
  FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md'ye yazılır (Kart Y).
· Sayı kaynağı DEĞİL — tek istisna DIS_SAYILAR.md (platformların sayıları)
  ve KANAL_KIMLIGI §5.1 (palet — LOGO_STING v2'den devralınmış).
```

---

## 🔲 AÇIK İŞLER

```
□ KARARLAR      00_KANAL_DENETIMI §9 — S1…S12 (handle · tagline · dil ·
                kadans · tez · YPP durumu …). Kararsız satır varsayılan
                öneriyle yazıldı; karar değişirse KANAL_KIMLIGI'nde tek
                satır değişir.
□ TEMİZLİK      30 açıklama + 5 başlık (00_KANAL_DENETIMI §2.1, §8)
□ HANDLE        @apexaic üç platformda müsait mi → KANAL_KIMLIGI §7.2 takvimi
□ LOGO/BANNER   Λ avatar + banner tek dosyadan üç platforma (KANAL_KIMLIGI §5)
□ KANAL SAYFASI fragman · bölümler · playlist'ler (youtube/HESAP_KIMLIGI §3)
□ TİKTOK        Business hesap (link) · yalnız dikey (tiktok/HESAP_KIMLIGI)
□ İLK ÖLÇÜM     bir sonraki yükleme = Kart Y'li ilk satır (/yayin-takip)
□ DOĞRULAMA     DIS_SAYILAR'daki ⚠️ satırlar uygulamadan doğrulanmadı
```

---

## 🔍 apexait'TEN NE ALINDI, NE DÜZELTİLDİ — eleştiri kaydı (01.09.2026)

Kaynak: `../../timelapse_md/apexait/` (10 dosya). İskelet oradan; aşağıdaki
satırlar orada gördüğümüz ve burada **bilinçli değiştirdiğimiz** şeyler.

**Devralınan güçlü yanlar:** kök = ortak / platform = yalnız fark; "kopyalama"
yasağı; her platforma bir rol; tez = fikir reddetme kapısı; kanal negatif
çekirdeği "ne kaybettiğimiz" sütunuyla; politika riski sıralı; doldurulmuş
örnek + spoiler testi; sabit cevaplar; yükleme kontrol listeleri.

| # | apexait'te | Sorun | apexaic'te |
|:--:|---|---|---|
| 1 | `youtube/` POLITIKA + PAKETLEME; IG/TT HESAP + PAKETLEME; YouTube hesap kartı YOK (KANAL_KIMLIGI §7'ye dağılmış) | Asimetri. README "politika üçünü de ilgilendirir" diyor ama dosya tek platform klasöründe | `POLITIKA_VE_RISK.md` kökte; üç klasörde aynı iki dosya |
| 2 | Dış sayılar 3 tabloda + 2 istisna = 5 yer (README kendisi sayıyor) | "Sayı iki yerde tutulmaz" kuralına beş istisna → kural yok | `DIS_SAYILAR.md` tek tablo, platform sütunu, tarih, kaynak |
| 3 | Instagram ızgara **4:5 / 285 px** → "taç y=320" kuralı 3 dosyaya yayılmış (CAPRAZ §3.2 · IG HESAP §3 · IG PAKETLEME §5) | Izgara 01.2025'ten beri **3:4** (1080×1440 → 240 px). ⚠️ diye işaretlenmiş — doğru disiplin — ama türetilmiş kural yanlış sayıdan doğup çoğaltılmış | 3:4 tek yerde (`CAPRAZ_YAYIN` §3); diğerleri oraya bakar |
| 4 | Bio metinlerinde `<kadans>` placeholder | Apex AI Cinema'nın CANLI açıklamalarında `[Kanal Linkini Buraya Ekle]` bulundu: placeholder yapıştırılabilir metinden sızar | Yapıştırılabilir bloklarda placeholder yok; varsayılan yazılır, karar dosyası işaret eder |
| 5 | YouTube hashtag 10-12 (+ `#shorts`) | Başlık üstünde yalnız 3 görünür; `#shorts` algılama için gerekmiyor; 15 üstü hepsini siliyor (kanalda oldu) | 3 hashtag, kademe 1→3 |
| 6 | "Platformlar arası link/CTA yok" (CAPRAZ §4) | 60 s tek-master format için doğru; 3-17 dk filmde dikey kesim tam filme HUNİ olmak zorunda. Kural formata bağlı, öyle etiketlenmemiş | Huni açık: TikTok/IG → YouTube (`CAPRAZ_YAYIN` §4) |
| 7 | "Ölçüm satırını aç" (YAYIN_PLANI §6.1) — tablo dosyası yok | Satır nereye yazılacak belirsiz | `08_YAYIN_PERFORMANS_TABLOSU` zaten var; Kart Y |
| 8 | Açılış 3 film AYNI GÜN (YAYIN_PLANI §4) vs POLITIKA §1.4 "günde birden fazla yükleme yasak" | İç çelişki; istisna etiketlenmemiş | Kanal açık, açılış bloğu yok; kadans `YAYIN_PLANI` §1 |
| 9 | Biyografi sınırı "⚠️ doğrula" (150/80) | Bilinen sayılar; doğrulanabilirdi | Doğrulandı, `DIS_SAYILAR` |
| 10 | İki dilli beyan (EN+TR) her caption'da | Oradaki §9.8 kuralı gereği meşru; TikTok'ta görünen ~100 karakterin çeyreği | Tek satır EN; TR yalnız sabit yorumda seçenek (S3) |
| 11 | Uzun form = "yapım günlüğü" (ikinci ayak) | Bize gerekmiyor: ürünümüz zaten uzun form. İkinci ayak bizde FRAGMAN (ölçülmüş: SECOND SHIP fragman 9 B) | `YAYIN_PLANI` §2 |

```
⭐ apexait'e geri taşınabilecek üç düzeltme: #2 tek sayı tablosu ·
   #3 Instagram 3:4 · #8 açılış istisnası. Bu depoya dokunulmadı;
   sahip isterse ayrı iş.
```
