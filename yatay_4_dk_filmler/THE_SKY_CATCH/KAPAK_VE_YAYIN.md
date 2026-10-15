# 📦 THE_SKY_CATCH — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

<!-- kaynak: ODA/SAHIP_PLANI.md §8 "YouTube yayın paketi" (sahip, 14.10.2026). Plan ÜÇ başlık/kapak adayı verir (A · B · C) ve A'yı başlangıç tercihi yapar;
     YouTube Studio A/B/C testi için üçü de hazır tutulur.
     Promptlar plandan birebir; referans anahtarı `Reference <No> (<rol>)` eklenmiştir. -->

```
SAHİP PLANI    Üç aday, başlangıç seçimi A. A — dev Dünya üzerinde düşen beyaz kabin, yanında küçük kurtarma gemisi (48 STILL INSIDE) ·
               B — uzay boşluğunda iki araç arasında süzülen Sana Cruz (THE LAST CAR) ·
               C — açık C yakalama çerçevesi ve açılmış çekme kolunun mekanik yakın planı (NO DOCKING RING).
               Kapaklarda AI yazı üretmez; kısa İngilizce ek yazı kurguda boş merkeze veya sol üste eklenir. Sağ alt köşe süre rozeti için sessiz bırakılır.
BAŞLIKLAR      A: 48 People Were Falling to Earth. We Had One Ship. · B: The Space Elevator Broke With 48 People Inside · C: We Couldn't Dock With the Falling Car
AN             A: C01/C15 kompozisyonu (Dünya + kabin + KITE) · B: C10 (Sana iki araç arasındaki boşlukta süzülürken) · C: C16 (çerçeve ve çekme kolu teması)
TEK İLİŞKİ     A: dev Dünya ve düşen kabin ↔ küçük kurtarma gemisi (ölçek kontrastı) · B: uzay boşluğundaki kırılgan insan ↔ iki dev metal araç · C: açık yakalama çenesi ↔ yapısal çekme kolu
BOŞ ALAN       sağ alt köşe sessiz (süre rozeti); üst merkez kısa başlık/yazı için temiz
REFERANS       A: Reference 3 (rescue tug) · Reference 4 (passenger capsule) · B: Reference 2 (engineer) · Reference 3 · Reference 4 · C: Reference 3 · Reference 9 (deployed tow bar)
FİNAL          faz 9: gerçek kareden ~/film_medya/THE_SKY_CATCH/cikti/kapak_A.png (B ve C test için kapak_B.png, kapak_C.png)
```

### Kapak A — Düşüş ve tek kurtarma gemisi (sahip tercihi)
```text
Reference 3 (rescue tug): take the compact graphite-and-ivory rescue tug with its open C-shaped nose frame from it. Reference 4 (passenger capsule): take the rigid ivory-and-graphite elevator car with amber glowing windows and broken upper mount from it. A highly readable cinematic YouTube thumbnail, horizontal 16:9. A rigid ivory-and-graphite passenger elevator capsule with softly glowing amber opaque windows, a short broken upper guide stem and damaged primary capture collar, and a small external service ledge on its lower left side. The passenger pressure hull stays sealed. No passengers are visible. Large on the right, descending above an enormous curved blue Earth; the short broken upper mount is plainly visible. KITE, a compact graphite-and-ivory rescue tug with a small blue two-seat cockpit canopy, a small side airlock above the nose frame, one permanently visible C-shaped nose capture frame with a single hinged closing jaw, and two fixed ventral recovery thrusters mounted below the tug clear of the passenger hull. Smaller on the left, approaching to rescue it with its open nose frame. Strong ivory silhouettes against dark space, blue-and-amber contrast, few visual elements. No flames, faces in passenger windows, extra ships or cables. Leave a clean dark upper-center region for three words added later. Keep the bottom-right visually quiet for the player duration badge.
```

### Kapak B — İki araç arasındaki tehlikeli geçiş
```text
Reference 2 (engineer): take her face, the clear closed visor and the pearl-white suit with teal arm bands from it. Reference 3 (rescue tug): take the hull and open airlock from it. Reference 4 (passenger capsule): take the elevator car from it. A cinematic YouTube thumbnail, horizontal 16:9. Sana Cruz, a 33-year-old female rescue engineer with warm brown skin, dark eyes and black hair secured inside her helmet, wearing an elegant pearl-white pressure suit with teal upper-arm bands, a triangular teal-and-silver engineer badge with no lettering, magnetic boots, and a closed clear helmet visor. Large enough to recognize in the center-left foreground, already suspended midway across a small stable gap between KITE's airlock at left and the passenger capsule's external service ledge at right. One controlled safety tether, closed visor, calm determined face. Huge curved blue Earth below, ivory suits and hulls, restrained amber windows, clean readable silhouettes. Only one astronaut visible, no passengers or flames. Leave dark upper center for an editorial title. Keep the bottom-right visually quiet for the player duration badge.
```

### Kapak C — Kurtarma bağlantısı detayı
```text
Reference 3 (rescue tug): take the open C-shaped nose capture frame with its single hinged jaw from it. Reference 9 (deployed tow bar): take the thick rectangular tow bar with its squared lug from it. A cinematic YouTube thumbnail, horizontal 16:9. Extreme foreground close-up of KITE's open C-shaped nose capture frame at left, aligned just short of the squared end of the capsule's thick rectangular emergency tow bar at right. The frame has one hinged closing jaw. The rigid tow bar extends from the intact passenger capsule pressure hull. Enormous curved blue Earth in the lower background, bright ivory hull edges, dark space, clean mechanical geometry, strong separation. No spark, explosion, people, extra arms or text. Leave dark upper center for a short editorial title. Keep the bottom-right visually quiet for the player duration badge.
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Tüm YouTube Studio metinleri (İngilizce başlık seçenekleri, açıklama iskeleti, 3 hashtag, etiketler, sabit yorum ve vaat denetimi) `YAYIN_PAKETI.md` dosyasındadır.
Denetim: `python3 uretim_hatti/araclar/film_dogrula.py yatay_4_dk_filmler/THE_SKY_CATCH --bolum yayin`.
