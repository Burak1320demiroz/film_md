# 🧷 <FILM_ADI> — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
varlık `UZAYLI_VARLIK` §4 · ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK → merkezî seçim → hook → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Metin çapası
> aynı CÜMLEYİ okutur, aynı NESNEYİ çizdirmez; modelin girdisi GÖRSELDİR.
>
> ⚠️ **BETİK DAVRANIŞI — 06.09.2026'da ÖLÇÜLDÜ, VARSAYIM DEĞİL:**
> `### 📸 IMAGE PROMPT` başlığı `prompt_kontrol.py`'nin BAŞLIK desenine UYAR;
> bu dosya DOSYA modunda normal imaj promptu gibi denetlenir (⑯ ⑮ ⑲ D79 ·
> uzunluk) — istenen budur. `## SAHNE n` başlığı TAŞIMADIĞI için KLASÖR
> modunun DİZİ kapılarına (⑩ kurulum · ⑪ açı · ⑬ tema) GİRMEZ.
> ⛔ **TEK KOŞUL: İngilizce prompt, başlıktan sonraki İLK çitli blok olmalı.**
> Künye bloğu araya girerse betik YANLIŞ bloğu ölçer ve anlamsız BLOCK verir.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
> ⛔ En az bir kutu işaretlenmeden paket yazılmaz; hiçbiri işaretlenmiyorsa
> dosya `⬜ BEKLİYOR` ile durur, SİLİNMEZ (§2.0 boş dosya kuralı).
> ⛔ Eski "iki insandan/araçtan fazlası" sayımı ÖLDÜ — kılavuz §1.
```
□ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: ⬜
□ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: ⬜
□ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: ⬜
□ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: ⬜
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: ⬜
□ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: ⬜
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: <FILM_ADI>          FORMAT: ⬜        ORAN: ⬜ 16:9 / 9:16
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: ⬜    SAHNE SAYISI: ⬜
SAYFA: ⬜   TOPLAM PANEL: ⬜   ARİTMETİK: ⬜ sayfa × ⬜ panel = ⬜
   ⛔ Bu toplam §2 tablosunun panel toplamına EŞİT olmalı (§7 ①)
İMAJ MODELİ + SÜRÜM: ⬜         TARİH: ⬜.⬜.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `<FILM_ADI>_KAPAK.md` (RK onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK S⬜ → merkezî seçim S⬜ → kapanış S⬜ → S0 → kalanı

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R⬜ | ⬜ | ⬜ | ⬜ | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R⬜ | ⬜ | ⬜ | ⬜ | 🟠 S⬜'den önce | | | ⬜ TASLAK |
| R⬜ | ⬜ | ⬜ | ⬜ | ⏳ sonra | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp
   karşılaştırılır (yanlış dosyayla üretim yapılmasın).
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| ⬜ | ⬜ | insan / araç / mekân / olay / canlı / prop | S⬜ | S⬜ | R⬜ | ⬜ |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Kod kanonu: kılavuz §2.
⛔ Risk sınıfı `ASTRONOT_DONANIM` eşya tablosundan alınır (burada tarif edilmez).
⛔ Envanterde olup sayfası olmayan varlık = çapasız varlık; sahnede yeniden
   tasarlanır. Sayfası olup hiçbir sahnede çağrılmayan = YETİM (§7 ②).
BELGEDE KALAN ↔ YALNIZ GÖRSELDE KİLİTLENEN ayrımı kılavuz §2 tablosundadır;
buraya yalnız SONUCU yazılır.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| ⬜ | K0 (temel) | — | S⬜ | — | R⬜ p⬜ |
| ⬜ | K1 | ⬜ | S⬜ | S⬜ | R⬜ p⬜ |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönülüyorsa gerekçe satırı: ⬜  [D147 · D84]
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en).
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişkidir. Bu dosyada
   hangisi seçildi ve NEDEN: ⬜
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S⬜ | ⬜ | R⬜ p⬜ | ⬜ | K⬜ | ⬜ |
```
⛔ "METNE DEVREDİLEN" BOŞ BIRAKILAMAZ — referansın taşıyamadığı her şey
   (anlık eylem, geçici yansıma, hareket) buraya yazılır [kılavuz §5.1].
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2). Dördüncü varlık
   kadraj dışına alınır ya da metne devredilir — PLAN kararıdır.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   ⚠️ Dört eski paket TERSİNİ yazıyor ve iddia ÖLÇÜLMEDİ; bu dosyanın
   seçtiği yükleme biçimi: ⬜  (kırpım / tam sayfa) · gerekçe: ⬜
· Flow çağırma: `@R⬜` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun kopyasıdır; ayrışırsa
  tablo düzeltilir. Sayfası ⏳ olan sahne "ÜRETİLMEZ" damgası taşır.
```

## 6. 📸 REFERANS SAYFALARI
> Blok her sayfa için olduğu gibi tekrarlanır. R1 biçim örneğidir; kopyalarken
> içindeki metin SİLİNİR, iskelet kalır.
> ⛔ **İngilizce prompt BAŞLIKTAN SONRAKİ İLK çitli bloktur** (yukarıdaki
> ölçüm notu). Künye ve kabul sınavı promptun ALTINA yazılır.

### 📸 IMAGE PROMPT — SAYFA R1 · ⬜  *(biçim örneği — yarı dolu)*
```
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey
seamless backdrop, even neutral key light with soft fill.

Exactly one human character — no clones, no second person. A ⬜ standing
straight and facing the lens, sealed in a ⬜ pressure suit. A ⬜ band is
wrapped all the way around the RIGHT forearm. The visor is optically clear
glass with zero tint, zero mirror coating and zero reflection, held in a
visible ⬜ frame, and the face is fully readable through it AT EVERY HEAD
ANGLE. The back of the suit is one continuous smooth panel from collar to
hip, unbroken, carrying nothing — one smooth surface with a single flat
vertical seam down its centre. Fixed wear that never moves: ⬜ · ⬜.

NEGATIVE: [KILAVUZ_REHBERI §5 negatif çekirdek TAM METİN] ⬜ · no backpack,
no tank, no hose, no rear housing of any kind · no panel gutters, no labels,
no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: ⬜ oran, ⬜ çözünürlük, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş   p2 · profil — siluet hattı
               p3 · SIRT — düz siluet [D79/D139]   p4 · vizör ardı yüz CU [D146]
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — model boş sırtı DOLDURMAK zorundadır;
   panelin işi ona ne KOYACAĞINI söylemektir: yasak değil MALZEME [D123 · D139].
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      ⬜ (sayı ya da ikili test)
  RET:        ⬜
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: ⬜ · doğru cevap: ⬜
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S⬜ ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = ⬜
     ⚠️ ≥4 olursa `prompt_kontrol.py` ⑲ **FIX** verir (BLOCK değil) ve
     politika reddi riski doğar [D167]: boy·ten·saç·yaş·yüz'den EN ÇOK ÜÇÜ.
```

### 📸 IMAGE PROMPT — SAYFA R⬜ · ⬜
```
⬜ İNGİLİZCE IMAGE PROMPT

NEGATIVE: [KILAVUZ_REHBERI §5 negatif çekirdek TAM METİN] ⬜

Output: ⬜ oran, ⬜ çözünürlük, no text, no watermark.
```
```
ÖNCELİK: ⬜   PANEL: ⬜   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜
PANEL LİSTESİ: p1 · ⬜   p2 · ⬜   p3 · ⬜
KABUL SINAVI: KABUL ⬜ · RET ⬜ · YABANCI GÖZ ⬜ · SONUÇ ⬜ · ⑲ öznitelik ⬜
```
*(blok her varlık için tekrarlanır — R3 · R4 · …)*

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `<FILM_ADI>_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
□ ① PANEL ARİTMETİĞİ  §1 künye toplamı = §2 tablo toplamı
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var mı · çağrılmayan sayfa
                      (YETİM) 0 mı · yoksa gerekçesi yazılı mı
□ ③ 120 PX TESTİ      panel 120 px'e inince şu ⬜ öğe hâlâ ayırt ediliyor
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                      + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146]
□ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0 AMA yüzey POZİTİF tarifli
□ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — ayrım yalnız renge
                      dayanıyorsa panel reddedilir (önce fiilen sınanır)
□ ⑧ DURUM ÇİFTİ       §4'teki her çift aynı kadraj · aynı ışık yönü · ±%3
□ ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik ≤3 (betik: FIX)
□ ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin SONRASINI yazmıyor [D179]
□ ⑪ ÖLÇEK ŞAHİDİ      yapı panelinde 1H (kasklı gövde) kadrajda mı
□ ⑫ SEED / SHA KAYDI  hangi panel hangi seed ve özet — §2 tablosuna YAZILDI
□ ⑬ BAYT AYNILIĞI ⚙️  paketteki kimlik bloğu ile sahne promptu `diff` temiz mi
□ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ⬜ (⑯ ⑮ ⑲ D79)
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
⬜ Tetikleyici kontrolü işaretlenmedi     ⬜ Envanter · merdiven · eşleme boş
⬜ Sayfa blokları yazılmadı (R⬜ …)        ⬜ Kabul kapısı koşulmadı, seed boş
```
