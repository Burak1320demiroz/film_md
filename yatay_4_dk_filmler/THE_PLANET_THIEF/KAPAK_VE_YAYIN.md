# 📦 THE_PLANET_THIEF — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

<!-- kaynak: ODA/SAHIP_PLANI.md "Kapak taslağı" + "Thumbnail image prompt" (sahip, 10.10.2026). Plan tek kapak verir; hat A/B tek değişken ister →
     A = planın kapağı (birebir, olumsuz kuyruk çıkarılmış); B = F6'da kapak-tasarimcisi tek değişkenle türetir (sahip isterse). F6 bu filmde henüz açılmadı. -->

```
SAHİP PLANI    Yatay 16:9; solda büyük, tanınır Dünya; sağda gezegenden büyük kara geminin amber ağız halkası; ön planda küçük beyaz
               astronot silueti. İçerideki diğer gezegenler ve yapay güneş kapakta gösterilmez. Görsel üretiminde yazı isteme; film adını
               düzenlemede büyük ve okunaklı ekle. Ana öğeleri dış kenarlardan uzak tut; sağ alt köşede YouTube süre etiketi için boşluk bırak.
KAPAK YAZISI   THE PLANET THIEF (düzenlemede eklenir; ek uzun cümle yok — "başlık merakı, görüntü ölçeği taşır")
AN             planın kapağı C01/C18 kompozisyonudur (Dünya solda, giriş sağda, küçük astronot ölçek); gerçek kare adayı: C01 ya da C18 (F9'da ölçülür)
TEK İLİŞKİ     Dünya ↔ ondan büyük açık ağız (ölçek)
BOŞ ALAN       üst orta siyah boşluk (başlık) · sağ alt köşe sessiz (süre rozeti)
REFERANS       Reference 4 (black ark) · Dünya 4.ARK sayfasında
```

### Kapak A (sahip planı, birebir; olumsuz kuyruk çıkarıldı)
```text
Reference 4 (black ark): take the colossal black cylindrical ark, its open circular intake with the narrow amber rim, and Earth with its familiar continents from it. A bold cinematic science-fiction thumbnail. The intact blue Earth dominates the left half, with familiar continents and a bright thin atmospheric rim. On the right, the colossal black ark's open circular intake is visibly much larger than Earth, its narrow amber rim cutting through the darkness. Broad transparent amber tractor arcs pull toward the intake. A tiny ivory-suited adult astronaut silhouette near the lower center provides human scale. One strong simple visual relationship, deep black negative space at the upper center, clear contrast, sharp planetary detail. The lower-right corner stays visually quiet.
```
Plan notu (kod bloğu dışında): iç kasa ve yapay güneş kapakta yok; görselde yazı, logo, filigran istenmez.

### Kapak B
```text
<F6'da: tek değişkenle (ölçek ya da zamanlama) A'dan türetilir — sahip isterse>
```

```
DENEY SORUSU   <F6: örn. ölçek mi (Dünya küçük, ağız dev) · yakınlık mı (Dünya ağzın eşiğinde, C18/C21)?>
DEĞİŞKEN       <yalnız biri: vaat türü · zamanlama · odak · ölçek>
SABİTLER       karakter tarifi (FILM.md §3) · dünya ışığı · figür sayısı
AN             A: çekim <Cxx> · B: çekim <Cxx>   (plandan seçilir, "en güzel kare" aranmaz)
TEK İLİŞKİ     160×90'da okunacak tek şey: <…>
BOŞ ALAN       sağ alt köşe (süre rozeti) + başlık katmanı için <konum %>
FİNAL          faz 9: gerçek kare → ~/film_medya/THE_PLANET_THIEF/cikti/kapak_A.png
```

### Kapak A
```text
<English image prompt — no text in image>
```

### Kapak B
```text
<English image prompt — no text in image>
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
