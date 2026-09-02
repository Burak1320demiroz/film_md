# 🔁 ÇAPRAZ YAYIN — bir film, üç hesap

> Bu dosya **üçünde de aynı olan işi** tutar: iki master, huni, filigran
> yasağı, C2PA, güvenli alan, yükleme sırası. Platforma özel olan her şey
> `youtube/`, `instagram/`, `tiktok/` altındadır.
>
> ⚠️ §3.2'deki türetilmiş kırpma sayılarının KAYNAĞI bu dosyadır.

---

# 1. 🎞️ İKİ MASTER — ⛔ üç ayrı kurgu yok, bir tane de yetmez

timelapse_md'de tek master üç platforma gider (60 s dikey). Burada ürün
16:9 ve 3-17 dakika; **paketleme tek başına 16:9 klibi dikeyde kurtarmaz**
(`VIRAL_BASLIK` platform kuralları). O yüzden iki master, ikisi de kurgudan:

```
apexaic_<FILM>_master_16x9.mp4        → YouTube (film · fragman)
apexaic_<FILM>_vertical_9x16.mp4      → TikTok · Reels · YouTube Shorts
                                        (48 s ızgara kesimi VEYA dikey shorts)
apexaic_<FILM>_trailer_16x9.mp4       → YouTube   (≥7 dk filmlerde)
apexaic_<FILM>_trailer_9x16.mp4       → TikTok · Reels

· filigran YOK · platform logosu YOK · gömülü altyazı YOK · ekran metni YOK
· ihraç: KURGU_RITMI_VE_IHRAC §6 (DIS_SAYILAR §4)
· dikey kesim ayrı kurgu kararıdır: hook 0. karede, karakter alt, ölçek üst
  (KILAVUZ_REHBERI §2.1) — yatay kadrajı ortadan kırpmak kesim DEĞİLDİR
```

## 1.1 ⛔ Filigranlı yeniden yükleme yasak

```
⛔ TikTok'tan indirilen videoyu Reels'e / Shorts'a yükleme; tersini de.
⛔ Hiçbir platformun "diğerine paylaş" düğmesi kullanılmaz.
Üç yükleme de master dosyadan, NATIVE (uygulamanın kendi yükleyicisiyle).
Filigranı kaldırmanın maliyeti sıfır, filigranlı yüklemenin maliyeti tek yönlü.
```

## 1.2 ⚠️ Logo introsu — çözülmemiş çelişki   [S12]

```
APEXAIC_INTRO_PROMPT.md: "her filmin başına 10 saniyelik marka introsu".
HOOK_VE_ILK_SAHNE + YAYIN §2.0: YouTube Shorts'un tek kapısı 0. KARE;
yatayda ilk 3 saniye kritik.

→ DİKEY MASTERDA İNTRO YOK. Pazarlık yok: 0. kare filmin kancasıdır.
→ YATAY MASTERDA karar sahibin: (a) intro SONA (kapanış damgası — LOGO_STING
  BLOK Z zaten var) ← öneri  (b) başa ≤3 s kısaltılmış sting  (c) 10 s başa
  Ölçülmeden kural yazılmaz: YAYIN_PLANI §6.1 ⑤.
```

---

# 2. 🧬 METADATA VE C2PA — ⛔ temizleme

```
Veo/Flow çıktıları C2PA "Content Credentials" gömer. YouTube (27.05.2026'dan
beri otomatik), TikTok ve Meta bu imzayı OKUR ve kendiliğinden etiketler.

⛔ METADATA SİLİNMEZ.
   ① Kanalın adı "AI" diyor; saklayacak şey yok. Silmek tutarsızlık.
   ② TikTok'ta otomatik etiket üretici tarafından KALDIRILAMAZ; YouTube
      "öneri/para cezası yok" diyor (DIS_SAYILAR §1, §3).
⭐ DOĞRU HAMLE: her platformda ÖNCE KENDİN beyan et (POLITIKA_VE_RISK §3).
   Kendi beyanın senin cümlendir; otomatik etiket platformun.
```

---

# 3. 📐 GÜVENLİ ALAN

## 3.1 Dikey zarf

```
Üç platform da 1080×1920 alır, arayüzleri farklı yerleri kapatır.
KAPAK_FOTOGRAFI_MIMARISI §5 matrisi YouTube Shorts'a göre yazılı ve o zarf
diğer ikisini kapsıyor (DIS_SAYILAR §4 ⚠️). → dikey kesim promptlarında
platform başına ayrı kadraj hesabı YAPILMAZ. Ölçüm §3.3.
```

## 3.2 ⛔ Instagram profil ızgarası 3:4 — bu dosya kaynaktır

```
Instagram ızgarası 01.2025'ten beri 3:4 (DIS_SAYILAR §2). 9:16 Reels
kapağı ızgarada ortalanarak KIRPILIR:

   1080 genişlikte 3:4     →  1080 × 1440
   kesilen yükseklik        →  1920 − 1440 = 480
   üstten ve alttan         →  240 px
   IZGARADA GÖRÜNEN BANT    →  y = 240 … 1680

KURAL (yalnız Instagram kapak karesi seçimini bağlar, videoyu değil):
   karakter ve odak nesnesi y = 280…1640 bandında (240 + 40 pay).
   Dikey kompozisyon zaten "karakter alt, ölçek üst" — üst ölçek öğesinin
   TACI 280'in üstündeyse ızgarada kesilir; kapak karesi ona göre seçilir.
⚠️ timelapse_md/apexait bunu 4:5 / 285 px hesaplamıştı — eski ızgara.
   Oradaki "y=320" kuralı buraya taşınmadı.
```

## 3.3 ⭐ Ölçüm — söylentiyle değil, kaplamayla

```
1. İlk dikey kesimi üç platforma da yükle.
2. Her platformda kendi telefonundan ekran görüntüsü al.
3. Üç görüntüyü 1080×1920'ye ölçekle, üst üste koy.
4. Arayüzün kapattığı en geniş dikdörtgeni işaretle.
5. §3.1 zarfından DARSA → o platform artık zarfın kendisidir; KAPAK_FOTOGRAFI
   §5 matrisine tek satır iner (Kart G — veri → belge → ders sırası).
6. Aynıysa DIS_SAYILAR §4'e "ölçüldü · <tarih>" yazılır, ⚠️ kalkar.
```

---

# 4. 🔗 HUNİ VE LİNK POLİTİKASI — timelapse_md'nin TERSİ

```
timelapse_md/apexait §4: "platformlar arası link/CTA koyma" — 60 s tek
master için doğru. Burada ürün 3-17 dk ve YALNIZ YouTube'da yaşıyor; dikey
kesim ve fragman tam filme GÖNDERMEK için var. Kural formata bağlıdır.

TikTok / Reels / Shorts caption   →  "Full film on YouTube — link in bio."
                                     (tek satır, caption sonunda)
YouTube açıklaması                →  IG/TikTok yalnız CREDITS bloğunda ADRES
                                     olarak; "beni TikTok'ta da takip et" yok
Bio linki                         →  apexaic.com (üçünde aynı) → site
                                     YouTube'a yönlendirir; yoksa kanal linki
⛔ "Watch till the end" hiçbir yerde (ortası zayıf sinyali)
⛔ "Follow for part 2" — filmin ikinci parçası yok, film bitiyor
⚠️ TikTok bio linki 1.000 takipçi ister → Business hesap (tiktok/HESAP §2)
```

---

# 5. 🕐 YÜKLEME SIRASI VE ZAMANI

```
UZUN FİLM (≥7 dk):
   G−3   fragman 16:9 → YouTube  ·  fragman 9:16 → TikTok + Reels (native)
   G     film 16:9 → YouTube, kadans saatinde (YAYIN_PLANI §1)
   G+1   dikey kesim → YouTube Shorts → TikTok → Reels (aynı gün, saat arayla)
KISA FİLM (2-5 dk):
   G     film → YouTube
   G+1   dikey kesim → Shorts → TikTok → Reels
SIRA GEREKÇESİ  Shorts: arşiv/arama kalıcılığı · TikTok: ilk 24 saat en sert
   · Reels: kapak elle seçilir (§3.2), en son
⚠️ Sıra ve G+1 varsayımdır; 3 filmde YAYIN_PLANI §6.1 ile sınanır.
```

---

# 6. 🧩 NE ORTAK, NE PLATFORMA ÖZEL

| Katman | Ortak mı | Nerede yaşıyor |
|---|---|---|
| Yatay master · fragman | ✅ (yalnız YouTube'a gider) | film klasörü |
| Dikey master | ✅ üçüne aynı dosya | film klasörü |
| Tez · negatif çekirdek · kitle | ✅ | `KANAL_KIMLIGI` §2-4 |
| Avatar · palet · AI beyan cümlesi · link sırası | ✅ | `KANAL_KIMLIGI` §5, §7 |
| Handle (@apexaic) | ✅ | `KANAL_KIMLIGI` §7.2 |
| Kadans · ortam sırası · playlist adları | ✅ | `YAYIN_PLANI` |
| Banner | ⛔ yalnız YouTube (IG highlight / TikTok sabit kapak aynı görselden) | `KANAL_KIMLIGI` §5.3 |
| Bio metni | ⛔ platforma özel | `<platform>/HESAP_KIMLIGI` §2 |
| Başlık / caption / hashtag / sabit yorum | ⛔ platforma özel | `<platform>/PAKETLEME_SABLONU` |
| AI beyanı kutusunun yeri | ⛔ platforma özel | `POLITIKA_VE_RISK` §3 |
| Para ayağı | ⛔ yalnız YouTube | `youtube/HESAP_KIMLIGI` §5 |
| Kapak karesi seçimi | ⚠️ IG'de bant kuralı | §3.2 |
| Dış sayılar | ✅ tek tablo | `DIS_SAYILAR` |

---

# 7. ✅ ÇAPRAZ YAYIN KONTROL LİSTESİ

```
□ 0  ⛔ Kart B tamam mı (QA + ihraç + 00_INDEX "üretildi")
□ 1  ⛔ Kart Y kimlik satırı AÇILDI mı — yayından ÖNCE (/yayin-takip once)
□ 2  İki master var mı — dikey kesim gerçekten kesim mi, kırpma mı
□ 3  Master filigransız, logosuz, ekran metinsiz mi (intro kararı §1.2)
□ 4  C2PA/metadata SİLİNMEDİ mi
□ 5  Üç platformda AI beyanı KENDİ ELİNLE işaretlendi mi (POLITIKA §3)
□ 6  Instagram kapak karesi: odak y=280…1640 bandında mı (§3.2)
□ 7  Üç yükleme de native mi
□ 8  Sıra §5'e uyuyor mu · ortam sırası YAYIN_PLANI §3 ihlal yok mu
□ 9  Üçünde caption/açıklama O platformun şablonundan mı (kopya değil)
□ 10 Huni satırı dikeylerde var, YouTube'da dışarı gönderen CTA yok mu (§4)
□ 11 ⛔ Tek değişken kilidi: ilk 48 saatte kapak VEYA başlık
```
