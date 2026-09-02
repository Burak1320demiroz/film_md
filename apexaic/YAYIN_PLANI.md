# 📡 YAYIN PLANI — Apex AI Cinema

> Bu dosya **ne zaman ne yayınlanacağını** tutar. Filmin nasıl yapılacağı
> kılavuzlarda, kanalın ne olduğu `KANAL_KIMLIGI.md`'de, gerçek sayılar
> `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md`'de. Buraya üretim
> bilgisi ve ölçüm satırı yazılmaz.

---

# 1. ⚖️ KADANS — hacim değil, istikrar   [S6]

```
ÖLÇÜLEN (01.09.2026, son 30 yükleme):  ≈ 6 / hafta, düzensiz —
   11 saatte 3 · sonra 3 gün · 8 gün · 10 gün · bir haftada 7.
   Aynı haftadaki 7 yükleme birbirini kaldırmadı: 2'si 9 B+, 5'i 400-900.
   Kanal bio'su "weekly" vaat ediyor; ikisi de birbirini tutmuyor.

ÖNERİ
   YATAY FİLM     2 / hafta · sabit gün + saat · Salı & Cuma 16:00 UTC
                  (ABD sabahı + Avrupa akşamı; ölçülüp değişir)
   FRAGMAN        her uzun film (≥7 dk) için, filmden 3 gün önce
   DİKEY KESİM    ≤ 1 / gün · yatay filmin kesimi · filmden 24-48 s sonra
   DİKEY SHORTS   (kendi başına yazılmış 9:16 film) dikey kesim kotasına
                  dahil — günde tek dikey

⛔ Kadans ARTIRMA kararı metrikten doğar (4 hafta tutturulmuş + 08
   tablosunda 3 filmde AVD ölçülmüş), hevesten değil.
⚠️ Kadans DÜŞÜRMEK hata değil. Cezalandırılan şey az yükleme değil,
   ŞABLON yükleme (POLITIKA_VE_RISK §2).
⭐ Stok yakıttır: 77 yazılmış film, ~24'ü yayında. Haftada 2 = bir yıllık
   yakıt. Hepsini bir ayda yayınlamak stoğu yakar (SERI §5.3).
```

---

# 2. 🦵 İKİ AYAK — film + fragman

`00_KANAL_DENETIMI` §2.3: kanalın en iyi iki sonucu THE SECOND SHIP filmi
(9,8 B) ve fragmanı (9 B). 10× medyan. Aynı hafta atılan diğer 5 yükleme
kaldırmadı. Bu, kanalın **ölçülmüş tek hunisi.**

```
AYAK 1 — YATAY FİLM                 ⭐ kanalın ürünü
   16:9 · 2-4 / 3-5 / 7-9 / 10-20 dk · YouTube'da yaşar
   Görevi: izlenme saati (YPP uzun form yolu — DIS_SAYILAR §1), arşiv, arama

AYAK 2 — FRAGMAN + DİKEY KESİM      ⭐ kanalın hunisi
   FRAGMAN  16:9 YouTube (FRAGMAN_KILAVUZU) + 9:16 kesimi TikTok/Reels
            → filme 3 gün önce kapı açar; kanal fragmanı adayı
   DİKEY    48 s ızgara / dikey shorts · TikTok · Reels · YouTube Shorts
            → "Full film on YouTube" (CAPRAZ_YAYIN §4 huni)
   Görevi: erişim, abone, tam filme trafik

⛔ timelapse_md'nin "yapım günlüğü" ayağı burada YOK: ürünümüz zaten uzun
   form; izlenme saati filmden gelir. Süreç anlatısı isteğe bağlı IG
   "Behind" highlight'ıdır (instagram/HESAP_KIMLIGI §7), ayak değil.
```

---

# 3. 🔀 SIRALAMA KURALI — ızgara için

`KANAL_KIMLIGI` §5.4: kapaklar metinsiz; kanal sayfası ızgarası ortamla
ayrışır. Buradan tek sert kural çıkar:

```
⛔ ARDIŞIK İKİ YÜKLEME AYNI ORTAM AİLESİNDEN OLAMAZ.

ORTAM AİLELERİ (KILAVUZ_REHBERI §3 ortam kartlarından)
   MARS       ince atmosfer · kızıl toz · mavi gün batımı          (§3.2)
   VAKUM      ay · kuyruklu yıldız · açık uzay · soğuk kaynak      (§3.1 · §3.8)
   YÖRÜNGE    istasyon · kenetlenme · dönme/itki yerçekimi        (§3.5 · §3.7)
   BULUT      kalın atmosfer · Venüs katmanı · yüzen habitat      (§3.4 · §3.6)
   ANOMALİ    monolit · halka · yaşayan vadi (ortamdan bağımsız)

İHLAL ÖRNEĞİ (01.09.2026): FROST LINE (Mars) → LAST CUSTODIAN (kızıl
   gezegen) → SKYLIGHT (Mars) — 3 günde üç Mars kapağı yan yana.
   Izgarada tek film gibi görünür; başlık bunu kurtarmaz.

Sebep ikili:
  ① kanal sayfası 6 ayrı iş gibi görünür (tıklama)
  ② POLITIKA §2 "videodan videoya çok az değişen" cümlesine karşı en
     görünür savunma ARDIŞIKLIKTIR — denetleyen de izleyen de sırayı görür.
```

---

# 4. 🧹 TEMİZLİK TAKVİMİ — canlı 30 video

```
SIRA   00_KANAL_DENETIMI §8 (gün 0 → hafta 2)
HIZ    günde 3-5 video · yalnız METİN (başlık VEYA açıklama)
⛔ TEK DEĞİŞKEN KİLİDİ (Kart Y): bir videoda başlık değiştiyse aynı
   48 saatte kapağı DEĞİŞTİRME. 30 videoyu bir gecede değiştirmek, hangi
   değişikliğin ne yaptığını sonsuza dek bilinmez kılar.
HEDEF  youtube/PAKETLEME_SABLONU §8 (temizlik şablonu)
```

---

# 5. 🎬 SIRADAKİ FİLMLER — stoktan seçim

```
□ Stok: sayac.sh → 77 film; yayında olmayanlar seçilir
□ Seçim önceliği:
   ① SPEC'i olan + QA'dan geçmiş film (Kart B tamamlanmış)
   ② §3 sıralama kuralını bozmayan ortam
   ③ SERI §4.3 kütüphane taraması: en yüksek görüntülenmeli filmin
     ORTAM kartını paylaşan film → evren adayı, playlist'in 2. sırası
⛔ "Hazır olan her şeyi yükle" yok. Kadans §1.
⛔ Tez kapısı (KANAL_KIMLIGI §2.1) yeni film YAZILMADAN koşulur;
   yazılmış stok için THE SCIENCE bloğu yazılamıyorsa o film sıraya girmez.
```

---

# 6. 📊 ÖLÇÜM — Kart Y'nin yeri

```
NEREYE   FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md — satır YAYINDAN
         ÖNCE açılır (/yayin-takip <FILM> once). Geriye dönük satır GEÇERSİZ.
NE       YAYIN_VE_PERFORMANS §2.0 hiyerarşisi — üç platform üç ayrı sayı:
           YouTube Shorts → VSA (0. kare)      TikTok → tamamlanma oranı
           Reels → sends per reach             YouTube uzun → CTR + AVD
         ⭐ yatay filmde ek: fragman → film geçiş oranı (huni kanıtı)
NE ZAMAN 24 / 48 / 72 saat · terk saniyesi ızgara aritmetiğiyle sahneye
         çevrilir (Kart Y)
KURAL    Bir gözlem ÜÇ AYRI FİLMDE aynı yönde çıkmadan kural olmaz.
         Kural olunca: veri → BELGE revizyonu → (tekrarlarsa) ders (AGENTS §8)
```

## 6.1 Sınanacaklar — ölçülmeden kural yazılmayanlar

```
① uzun film + fragman hunisi (SECOND SHIP tek örnek — 3 filmde ölç)
② arama-niyetli başlık ("Why Solar Panels Fail on Mars" 1,4 B — tek örnek)
③ sessiz başlık > hype başlık (banned listesi buna dayanıyor; ölç)
④ TikTok yatay #LongerVideos desteği (DIS_SAYILAR §3) — tek değişkenle
⑤ 10 s logo introsu vs 0. kare kuralı (CAPRAZ_YAYIN §1.2) [S12]
⑥ Salı/Cuma 16:00 UTC saati
```

---

# 7. 🗂️ OYNATMA LİSTELERİ — YouTube (TikTok Playlist aynı adlar)

```
İZLEYİCİNİN ARADIĞI ADLA (insanlar "mars survival short film" arar, "ince
atmosfer" değil) — ortam aileleriyle (§3) birebir:
   Mars                         MARS
   Moons & Comets               VAKUM
   Stations & Docking           YÖRÜNGE
   Cloud Worlds                 BULUT
   Alien Worlds & Anomalies     ANOMALİ
   Feature Films                ≥10 dk (THE SECOND SHIP)
   Trailers                     fragmanlar

KURAL (SERI §5.1)
   □ her film TEK resmi seride · "resmi seri" ayarı işaretli
   □ playlist'in 1. sırası = en yüksek AVD'li film; en zayıf asla giriş değil
   □ tür dışı 2 video hiçbir listede değil (KANAL_KIMLIGI §3)
⛔ "Tez"e göre liste açılmaz (Yalnızlık · Entropi…): tez iç pusuladır,
   izleyicinin arama kelimesi değil.
```
