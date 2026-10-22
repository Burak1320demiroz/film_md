# 🎞️ FRAGMAN KILAVUZU — soruyu kurar, cevabı vermez

> **Ne için:** fragman filmi özetlediğinde çöktü (Slow Tide · Slow Stone: altı vuruşta bütün film), kurgusu ya da paketi hikâyeyi tamamladığında
> filme giden yolu sildi (D106 Black Cradle · D114 Cold Burn). Kanalın ölçülmüş tek hunisi film + fragmandır (SECOND_SHIP: film 9,8 B · fragman 9 B,
> `KANAL/YAYIN_PLANI` §2), ama hatta fragman kılavuzu yoktu; hattın tek fragmanı (THE_FURNACE_GATE, 17.10.2026) kuralını eski kılavuzdan aldı.
> **Kim okur:** Fable (fragman kartı) · goruntu-yonetmeni · dramaturg · izleyici · teknik-danisman · devamlilik · besteci · kurgucu · yayin · sahip.
> **Kaynak:** eski `FRAGMAN_KILAVUZU` (559 satır) + `PAKETLEME_VE_VAAT` §5 → `ARASTIRMA/24_SUZME_PAKETLEME_VE_YAYIN_20261021.md`. Sahip kararı 21.10.2026.
> **Emsal:** `yatay_16_dk_filmler/THE_FURNACE_GATE/THE_FURNACE_GATE_FRAGMAN_DIKEY.md` (dikey · 0:40 · 4 sahne · 8 çekim · ODA'da `FR_*` eleştirileri).
> **Tarih:** 21.10.2026.

**Kural türü (AGENTS §1b):** **KANITLI** satırlar en az iki kayıtlı vakaya dayanır; uygulanır. **HİPOTEZ** ve **VAKA** satırları uygulanır ya da gerekçe yazılır.
Fragman ne zaman, hangi süreyle, hangi oranda yapılır: **sahibin kararı**. Fragman filmin akışında (F1-F10) bir faz değildir; film F5'i kapattıktan sonra istenir.

---

## 1 · Ne olduğu, nasıl üretildiği

- **Fragman yeni bir film değildir.** Kendi konsepti, novumu, hikâyesi yoktur; yeni sahne ya da varlık yazılmaz. Her vuruşun **kaynak çekimi** (Cnn) tabloda
  gösterilir; kaynağı olmayan vuruş yazılmaz. Kimlik ve dünya cümleleri filmden **birebir**, referanslar filmin referanslarıdır (ayrı referans üretilmez).
- **Oran değişirse kırpma yok** — VAKA, geometri (Cold Burn): 16:9 kareden 9:16 kesilince figür ya da nesne dışarıda kalır. Dikey fragmanın her çekimi dikey
  oranda **sıfırdan** üretilir; vuruş seçimini oran belirler (dikeyde yukarı-aşağı, derinlik; yatayda yan yana, ufuk). Kaynak kadrajdan sapma §5 sapma tablosuna.
- **Oran aynıysa** (16:9 film → 16:9 fragman) fragman filmin onaylı denemelerinden kurulur; yeni üretim 0 — VAKA (Second Ship · Last Gate; yayın ölçümü yok).
- **Çekim 10 s üretilir; kurguda baştan zaman dilimi alınır** — sahip emsali (FURNACE, 17.10.2026: "40 saniye, 4 sahne, her sahneye en çok 1 kesme"):
  sahne = 10 s'lik yuva, içinde 1 ya da 2 çekim. Kadraj kırpılmaz; klibin içine kesme, hız rampası, ağır çekim, donma yok. Prompt ana hareketi **0,5 s'de başlatır
  ve dilimin içinde bitirir**; klibin kalanı yedek kuyruktur. Film sözleşmesinin "10 s kullanılır" kısmı fragmana uygulanmadı; başka bir biçim sahibin kararıyla.
- Fragman dosyası film klasöründe, `PROMPTLAR/` **dışında** durur (`<FILM>_FRAGMAN_<ORAN>.md`): `film_dogrula.py` ve `medya.py` o klasördeki her dosyayı film
  çekimi sayar. Medya `~/film_medya/<FILM>/fragman_<oran>/{kare,ham,ses,cikti}/`.

---

## 2 · Tek mekanik — özet değil (KANITLI)

Slow Tide ve Slow Stone'un dikey türevleri filmi altı vuruşta yeniden anlattı; FURNACE v1'in mekaniği filmin ortasında cevaplanan bir soruydu (dramaturg B1, ÖLÜMCÜL).

- Fragmanın **tek mekaniği** olur ve her vuruş onun bir basamağıdır. Mekanik bir cümleyle yazılır: "her vuruş tuzağın bir dişini sıkar" (FURNACE · KISKAÇ).
- Vuruş sayısını mekanik belirler: basamak yoksa vuruş da yok. "Bir manzara daha" dolgu vuruşu fragmanı özete çevirir.
- Eski sicil (mekanik adayları, aynı filme ikinci fragmanda tekrar edilmez): SAYIM · CEVAP · KUSUR YOK · KAPANAN KAPILAR · TERS KURALLAR · ÖRTÜLME · TERAZİ ·
  EKSİLME · DARALMA (sayı geri sayar) · KISKAÇ · ÖLÇEK · TAKVİM · YAKLAŞMA.
- **Soru** bir cümleyle yazılır ve filmin **gerçekten açık kalan** sorusudur; ortada cevaplanan ya da kolay tahmin edilen soru fragmanı taşımaz. Film bu soruyu
  cevaplar (vaat sınırı: fragman filmde olmayan bir vaat kuramaz).

---

## 3 · Spoiler kapısı — kurguda ve pakette (KANITLI)

D106: mercek fragman kurgusunu "iki kişi kutuyu alır, kalkar, istasyona kenetlenir" diye özetledi ve bunu başarı saydı. D114: kurgu testi geçti, açıklama metni olay
dizisini verdi ve fragman "short film" diye satıldı; izleyici filmi izlediğini sandı.

- Fragman dosyasının başında **"fragmanda asla olmayacaklar"** listesi: doruk ve çözümü · merkez seçimin sonucu · bedel · final ve kapanış imajı · omurga sırrı ·
  karakterin kaderi · novumun **mekanizması** (görüntüsü girebilir) · ekranda ve seste sayı, film adı, yazı. Vuruşlar filmin ilk ~%70'inden (HİPOTEZ; FURNACE en ileri
  kaynak %36).
- Liste **kurguda** madde madde koşulur: her kalem 0 kare.
- **Tek cümle testi** kurguya ve pakete birlikte: izleyici ajanına yalnız fragmanın ekranda görünen tarifi, başlığı ve açıklaması verilir; "bu film ne anlatıyor"
  sorusuna **tamamlanmış** bir hikâye söylüyorsa fragman çökmüştür. Cevapta açık bir soru kalmalıdır.
- **İmza testi** (VAKA, Second Ship): fragmanın sattığı tek görüntü (afiş vuruşu) kurguda var ve tersine dönmemiş (kıç önde yanaşma burun önde çıkmamış).
- **Paket:** başlıkta ve açıklamada olay dizisi ("X olur, sonra Y") yok; fragman "short film" diye satılmaz, "trailer"/"teaser" der. Spoiler bütçesi dört yüzeydir:
  başlık · kapak · fragman · açıklama birbirini tekrar etmez, tamamlar (`yayin` vaat denetimi).
- Ekran metni 0: başlık kartı ve jenerik kurguya girmez (KANITLI, D70 · `KURGU_SES_VE_MUZIK_KILAVUZU` §1).

---

## 4 · Ses, müzik, döngü (HİPOTEZ)

- **Replik:** dikey fragmanda 0 · yatayda en çok 2. Replik filmin klibinden, model sesiyle gelir ve o da spoiler kapısından geçer (doruğu anlatan cümle girmez).
- **Müzik:** tek parça, tek tırmanış (besteci, F8 biçimi). Son vuruştan önce **susar**; soru karesi sessiz kalır. Ses yatağı kesmelerde kopmaz (`GECIS` §2).
- **Dikey döngü:** son kare ilk kareye diker; döngüde bir şey değişmiş olur (FURNACE: V4b'de kepenk açıklığı V1a'dan dar → "aynı tuzağın yeni turu").
- Dikey güvenli alan ve dikey kapak: `KANAL/CAPRAZ_YAYIN` §3 · `kapak-tasarimcisi` 8.

---

## 5 · Akış — kim, ne zaman

FURNACE biçimi (ODA'da `FR_*` dosyaları):

| Adım | Kim | İş |
|---|---|---|
| 1 Kart | Fable | biçim (oran · süre · sahne · çekim) · sahibin cümlesi · mekanik · soru · spoiler listesi · vuruş/kaynak eşleme · **bilinçli sapmalar** (eski kılavuzdan ya da filmden her sapma + gerekçe) |
| 2 Kart eleştirisi | dramaturg · izleyici · teknik-danisman | dramaturg: soru gerçekten açık mı, mekanik özet mi, spoiler · izleyici: **bu bir fragmandır** bağlamıyla, yalnız ekranda görünen tarif · teknik: model riski |
| 3 Promptlar | goruntu-yonetmeni | filmin kimlik cümleleri birebir; çekim başına referans paneli; hareket 0,5 s'de başlar, dilim içinde biter |
| 4 Prompt eleştirisi | devamlilik · teknik-danisman | 8 soru · ÖLÜMCÜL riskler |
| 5 Müzik | besteci | tek prompt, kesme noktaları, son vuruştan önce sus |
| 6 Üretim | sahip | **afiş vuruşu ve soru vuruşu önce** (afiş çıkmıyorsa fragman yok); her çekim en çok 2 deneme |
| 7 Kurgu | kurgucu | kesim listesi (dilim · kesme) · kurgu kapısı: spoiler listesi 0 kare · ekran metni 0 · döngü dikişi · tek cümle testi (§3) |
| 8 Paket | yayin | trailer başlığı, filmin linki, vaat denetimi (§3 paket satırı) |

- Fragmana **senaryo merceği koşulmaz** (VAKA, Cold Burn: rubrik fragmanı film sandı, tasarımını kusur saydı). Hatta karşılığı: her eleştirmen görev metninde
  "bu bir fragmandır, filmi anlatmak zorunda değildir" bağlamını alır.
- Yayın sırası ve kanal tarafı: fragman filmden 3 gün önce, caption "Full film on YouTube" (`KANAL/YAYIN_PLANI` §1-2 · `CAPRAZ_YAYIN` §4-5).

---

## 6 · Aynı filme ikinci fragman (VAKA, Second Ship üç teslim · Cold Burn)

Dördü birden sağlanırsa yazılır, her kardeşe karşı **ayrı ayrı**:

1. **Mekanik farklı** (aynı mekaniğin ikinci çekimi varyanttır).
2. **Kaynak çekim kesişimi 0** (vuruş/kaynak tabloları yan yana).
3. **Kadraj kesişimi 0:** aynı özne, benzer lens ve mesafe iki fragmanda olmaz; olursa ikincisi yeniden kadrajlanır ve sapma tablosuna yazılır.
4. **Soru farklı.** Kardeşin afiş karesi ikincinin spoiler listesine girer: teslimler birbirinin sattığı görüntüyü satmaz.

Bedava gelenler: kimlik cümleleri, referanslar, spoiler listesi. Müzik ancak rejim değiştirdiği saniyeler de aynıysa yeniden kullanılır.

---

> **Ölçüm:** bu kılavuzla yazılan ilk fragmanda — izleyici ajanı kurgu tarifinden ve paketten hikâyeyi tamamlayabiliyor mu (§3) · dramaturg mekaniği tek cümleyle
> söyleyebiliyor mu (§2) · yayından sonra fragmandan filme geçiş (`IZLEYICI_VERISI` trafik kaynakları). **Sahibe açık:** §1'deki 10 s dilim biçimi fragman
> varsayılanı mı. **Bu dosya ne zaman değişir:** yalnız yeni kayıtlı vakayla ya da sahip kararıyla.
