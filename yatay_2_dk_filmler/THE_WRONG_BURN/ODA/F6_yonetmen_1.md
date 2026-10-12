# F6 · yonetmen (eleştirmen modu, faz 6) · tur 1 — THE_WRONG_BURN

> Girdi: F6_kapak-tasarimcisi_1.md + FILM.md (§3 §4) + PROMPTLAR/G01.md (C04 Görsel). Soru: kapak anı filmde var mı, ışık ve ölçek filmle aynı mı? Ajanın cevabı aynen (Fable kaydı, 10.10.2026).

### B1 · CİDDİ · B anı yanlış zaman aralığına yazılmış. Filmin kendi iniş hızına göre B karesi ≈1–2 s'de oluşur, 2–4 s'de oluşmaz
KANIT    Kapak AN: "B: çekim C04, ≈2-4 s … noktanın kaskın belirgin altında ama Dünya'nın mavi kenarının ÜSTÜNDE". Yerleşim: kask "y %12-40", gövde "%30-100", ufuk "≈%50", nokta A'da "y ≈%28". FILM §4 C04: nokta "kaskıyla aynı hizadan başlıyor ve 0-7 s'de … iniyor; 7 s'de Sela'nın bel hizasının çok altında, Dünya'nın önünde". Bel kadrajın alt kenarında, yani y≈100. Bu yüzden nokta saniyede ≥10 puan iner: y 42'ye ≈1,4 s'de, ufka ≈2 s'de varır. 2–4 s aralığında nokta Dünya'nın önündedir. Kapak bu kareyi kendisi reddediyor ("Dünya'nın önüne düşerse gri tonlamada kaybolur").
NEDEN    Faz 9'da §3'teki "t = 2,0-4,0 s" ve R2'deki "ufku 2 s'den önce geçerse B düşer" kuralları birlikte uygulanınca, filmde var olan B karesi (≈1,2–1,9 s, yaklaşık 1 s'lik pencere) aranmaz ve B'ye yanlışlıkla "yok" denir.
ARIZA    yeni (kapak anı zamanlaması)
ÖNERİ    AN B → "C04 ≈1,0-2,0 s (film ≈0:31-0:32; nokta y %40-50)". §3 B → "t = 0,5-2,5 s, `--aralik 0.25`". R2 düşme koşulu → "nokta y %40'ı geçmeden ufka varırsa".

### B2 · CİDDİ · Kapak B için üretilecek still prompt'u, kapağın kaynağına koyduğu kuralla çelişiyor
KANIT    R3: "kare/C04.png yalnız iki seçenek de still olabilirse kullanılır. B için still yok." Buna karşın §1'de tam bir "### Kapak B" Görsel prompt'u var. A prompt'u da C04 Görsel'den farklı: "distinct", "Her helmet sits in the upper-left part", "A wide gap of black sky lies between…", sağ üst ve sağ alt boşluk cümleleri. Yani A still'i kare/C04.png ile aynı görüntü olmaz.
NEDEN    Bu promptlardan biri kapak olarak üretilip kullanılırsa kapak filmde olmayan bir kare olur. Kompozisyonu, ışığı ve ölçeği ayrı bir üretimden gelir. B'de bu, B1 yüzünden filmin hiç içermeyebileceği bir an demek.
ARIZA    yeni (kapak ↔ film kare ayrılığı)
ÖNERİ    İki bloğun başlığına şu satır eklensin: "MAKET: yalnız yerleşim ön izlemesi, yayına girmez; FINAL = C04 video karesi (§3)". Böylece kapak dosyası R3 ile çelişmez.

### B3 · KÜÇÜK · "Değişen tek şey nokta" iddiası filmde tam tutmuyor
KANIT    Kapak DEĞİŞKEN: "Değişen tek şey kehribar noktanın yüksekliği". Yerleşim tablosunda ufuk "aynı", nokta x "≈%74" iki seçenekte de aynı. FILM §4 C04 ise şöyle diyor: "ufuk yayı, aynı sürede kadrajda biraz aşağı iniyor" ve "Bram ışığı sağ ortadan sağ alta iner".
NEDEN    Gerçek karede A ile B arasında ufuk birkaç puan aşağıda, nokta biraz sağda olur. 1,5 s'de bu 160×90'da 1–2 piksel eder, ama tablo bunu "aynı" diye yazıyor ve R1 kırpma hesabı sabit x'e dayanıyor.
ARIZA    T11
ÖNERİ    Tablo: ufuk "A ≈%50 · B ≈%51-52 (film: iner)", nokta x "A ≈%74 · B ≈%75-78". R1 kırpması gerçek karede yeniden ölçülsün.

### B4 · KÜÇÜK · SABİTLER referansın ışığını yanlış yazıyor
KANIT    SABİTLER: "DUNYA_gunduz_alt_v1: güneş solda yüksek". G01 REFERANS PROMPTLARI'nda DUNYA_gunduz_alt_v1 için: "The sun is directly overhead, just outside the top of the frame".
NEDEN    Referans tepeden ışık taşıyor, C04 ve kapak prompt'u soldan ışık istiyor. Final gerçek C04 karesi olduğu için ışık zaten filmle aynı olur, ama kapak "sol üst kenar parlak" vaadini referansın sağladığını varsayıyor.
ARIZA    T18
ÖNERİ    "dünya ışığı: DUNYA_gunduz_alt_v1 (ref'te güneş tepede; yön promptta: solda, ufkun üstünde, C04 Görsel ile birebir)".

### B5 · KÜÇÜK · Başlık katmanı tek sinyal öğesine fazla yakın
KANIT    Başlık katmanı "x %50-96 · y %5-22". Nokta A'da "x ≈%74 · y ≈%28". Kapak notu: "Nokta A'da başlık kutusunun ≈6 puan altında kalır".
NEDEN    160×90'da 6 puan yaklaşık 5 piksel eder. Görselin en kontrastlı katmanı (yazı), 1–2 piksellik tek sinyal noktasının hemen üstüne geliyor. A'da göz noktadan önce başlığa takılır.
ARIZA    yeni
ÖNERİ    Başlık katmanı y %4-16 olsun; noktayla arada ≥12 puan kalsın.

KORU: C04 seçimi. Kapak anı filmin kural görüntüsü ("S4 görüntü"). Film içinde %25–33'te duruyor ve iki anı aynı çekimin aynı kadrajından alıyor. A anı C04 Görsel'in "level with her helmet" başlangıç durumuyla birebir aynı, yani A filmde var. Işık ve ölçek de §3'teki "FINAL gerçek kare" ve R3'teki "aynı kaynak, aynı ölçekleme" kurallarıyla filme bağlanmış. R5'teki "kesilemez" notunu FILM §5 de destekliyor: replik 5–6–7 C04'ün 0,8 · 3,7 · 6,2 saniyelerinde, yani o 0–4 s kurguda zaten durmak zorunda.

KAPSAM DIŞI: FILM §4 C04 kendi içinde çelişiyor. "belden yukarısı kadrajda" ve "7 s'de bel hizasının çok altında" birlikte doğruysa nokta kadrajdan çıkar, oysa T14 "kadrajdan çıkmaz" diyor. Ayrıca FILM'deki "yatığa yakın, ≈65°" ile G01'deki "high at the left, well above the horizon" ışık tarifi birbirini tutmuyor.

```
ÖZET     ÖLÜMCÜL 0 · CİDDİ 2 · KÜÇÜK 3
KARAR    TUR KAPANABİLİR
GİRDİ    yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F6_kapak-tasarimcisi_1.md (tam) · yatay_2_dk_filmler/THE_WRONG_BURN/FILM.md (tam, §1-§7; §3 referanslar, §4 C01-C12, §5 replikler) · yatay_2_dk_filmler/THE_WRONG_BURN/PROMPTLAR/G01.md satır 1-508 (REFERANS PROMPTLARI, C04 Görsel + Video dahil) · uretim_hatti/ELESTIRI_PROTOKOLU.md · uretim_hatti/ARIZA_LISTESI.md (kod tablosu)
YAPILMADI  G01.md satır 509-712 (C11-C12, YAZAR NOTLARI) okunmadı, kapak anıyla ilgisiz · gerçek C04 videosu ve karesi henüz yok (faz 9): B penceresi ve 160×90 okunurluğu yalnız plan geometrisinden hesaplandı, ölçülmedi · KAPAK_VE_YAYIN.md ve IZLEYICI_VERISI §6 görev girdisi değil
```
