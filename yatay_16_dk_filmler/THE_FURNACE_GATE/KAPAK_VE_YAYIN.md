# 📦 THE_FURNACE_GATE — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §14 "YouTube yayın paketi" (sahip, 13.10.2026). Plan TEK kapak tabanı promptu ve üç başlık adayı verir; başlangıç tercihi 1. başlık.
     Prompt plandan birebir; yalnız referans anahtarı `Reference <No> (<rol>)` öne alındı (plan R01 R02 R04 R06 R07 → 1 · 2 · 3 · 5 · 6), ilk "Use the attached…" cümlesi
     ve olumsuz kuyruk ("No generated text, letters, logos or watermark.") çıkarıldı (hat kuralı). F6 bu filmde açılmadı (sahip planı); F9'da kapak-tasarimcisi
     gerçek kareden final kapağı ve tek değişkenli B'yi türetir, 160×90 kontrolü izleyici yapar. -->

```
SAHİP PLANI    Kapak filmdeki iki kişi ve kurtarılacak ark'tan kurulur: Leon ve Rhea önde ortada, arkada iki dev kilit/kapı ile fırın ışığı arasında ark, kıçında küçük tug,
               ötede mavi gaz devi; mavi-amber kontrastı, okunur iki yüz, tek kurtarma hedefi; ek kişi ya da canavar yok.
BAŞLIKLAR      1 (plan tercihi): We Stole a Ship Before Its Passengers Became Fuel | Sci-Fi Film · 2: 4,000 People Were Marked as Scrap. We Had to Steal Their Ship. ·
               3: THE FURNACE GATE | Two Thieves. One Ship. Four Thousand Lives. (plan: "ölçülmüş performans sonuçları değildir")
DENEY SORUSU   F9'da: yüz mü (A: iki kardeş önde) · ölçek mi (B: ark kapıda, insan küçük) — tek değişken vaat odağı
AN             A: C01 coğrafyası (ark + kapı + fırın) + C86/C95 iki yüz (Leon solda, Rhea sağda) · ilk 30 s bağı: C01 aynı üçlü, C03 Leon'un yüzünde amber kapı ışığı
TEK İLİŞKİ     iki kardeşin yüzü ↔ arkalarında fırınla kapı arasında tutsak dev ark
BOŞ ALAN       sağ alt köşe sessiz (süre rozeti); plan "alt-orta başlık alanı" ister → kapak yazısı kararı F9'da
KAPAK YAZISI   PLANDAN SAPMA (hat kuralı, sahip onayı bekler): plan film adını "THE FURNACE / GATE" iki satır ortada ister; KAPAK_VE_BASLIK_KILAVUZU kapakta film adı yazmaz,
               yazı yok ya da başlığı tekrar etmeyen 1-3 kelime → F9'da kapak-tasarimcisi önerir, sahip seçer.
VAAT SINIRI    iki kardeş (bütün film) · ark kapıda (C01 · C62 · C89-C91) · fırın ışığı (C01 · C12 · C44 · C92) · küçük tug ark'ın kıçında (C05-C06 · C57) — hepsi filmde
REFERANS       Reference 1 (the man) · 2 (the woman) · 3 (salvage tug) · 5 (foundry) · 6 (colony ark)
YÜKLEME SIRASI A ilk (plan kapağı) · B F9'da
FİNAL          faz 9: aynı referanslarla ayrı kompozisyon ya da gerçek kareden düzenleme → ~/film_medya/THE_FURNACE_GATE/cikti/kapak_A.png · kareler.py kapak → izleyici/kapak/A/
```

### Kapak A — iki kardeş ve tutsak ark (plan kapak tabanı)
```text
Reference 1 (the man): take his face, the clear closed ivory helmet and the ivory suit with orange arm bands from it, using the face close-up panel. Reference 2 (the woman): take her face, the clear closed pearl helmet and the pearl suit with teal arm bands from it, using the face close-up panel. Reference 3 (salvage tug): take the small ivory wedge tug from it. Reference 5 (foundry): take the dark three-shutter exit ring, the cradle and the amber furnace glow from it, using the wide exterior panel. Reference 6 (colony ark): take the long ivory colony ark from it. Photorealistic cinematic film cover base, horizontal 16:9. Leon and Rhea are close in the central foreground, both in their exact elegant white pressure suits and clear sealed helmets; he has orange arm bands, she has teal bands, distinctly different faces. Behind them in the central background, the huge ivory colony ark sits between a dark three-shutter exit ring and distant amber furnace glow, with a small salvage tug near its stern. A vast curved blue gas giant provides scale beyond the foundry. Strong clean blue-versus-amber contrast, readable faces and one clear rescue target, coherent film-like composition, no extra people or monster. Keep both faces and a clean lower-middle title zone inside the central area for social-safe layout.
```

### Kapak B
```text
<F9: kapak-tasarimcisi — A'dan tek değişkenle (ölçek: ark kapıda, iki küçük figür) ayrışır>
```

Plan notu (kod bloğu dışında): TikTok/Instagram kırpımını gerçek önizlemede ayrıca kontrol et. Kapak yazısı plan tipografisiyle eklenirse "okunur kırık beyaz/altın,
üst ve alt kenardan uzakta, iki yüz ve geminin okunurluğunu örtmeden merkezde" (plan §14).

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
F9 kaynağı: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §14 — İngilizce açıklama, 3 hashtag (#SciFi #ShortFilm #SpaceAction), sabit yorum ("Would you have kept the core
and escaped — or gone back for the ship?"), kısa etiket listesi. Açıklamadaki "combining AI-generated imagery and video with story, editing and sound design" cümlesi
üretimin gerçekten kullandığı yöntemlerle F9'da eşlenir (model sesi replikleri dahil).
