# 📦 <FILM_ADI> — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

```
DENEY SORUSU   <örn. yüz mü, ölçek mi?>
DEĞİŞKEN       <yalnız biri: vaat türü · zamanlama · odak · ölçek>
SABİTLER       karakter tarifi (FILM.md §3) · dünya ışığı · figür sayısı
AN             A: çekim <Cxx> · B: çekim <Cxx> · (C: çekim <Cxx>, isteğe bağlı)   (plandan seçilir, "en güzel kare" aranmaz)
TEK İLİŞKİ     168×94 ve 120×68'de okunacak tek şey: <…>
BOŞ ALAN       sağ alt köşe (süre rozeti) + kapak yazısı için <konum %>
KAPAK YAZISI   <yok · 1-3 kelime; başlığı tekrar etmez; film adı yazılmaz>
VAAT SINIRI    kapaktaki her varlık filmde: <varlık → çekim> (KAPAK_VE_BASLIK_KILAVUZU §7)
YÜKLEME SIRASI A ilk (en güvenli: "kazanan yok" çıkarsa A kalır) · B · C
FİNAL          faz 9: aynı referanslarla ayrı kompozisyon (varsayılan) ya da gerçek kareden düzenleme
               → ~/film_medya/<FILM_ADI>/cikti/kapak_A.png · kareler.py kapak → izleyici/kapak/A/
```

### Kapak A
```text
<English image prompt — no text in image>
```

### Kapak B
```text
<English image prompt — no text in image>
```

### Kapak C (isteğe bağlı; A'dan tek değişkenle ayrışır)
```text
<English image prompt — no text in image>
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
