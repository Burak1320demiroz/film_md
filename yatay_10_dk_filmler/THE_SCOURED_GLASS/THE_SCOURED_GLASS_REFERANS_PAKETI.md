# 🧷 THE SCOURED GLASS — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6 · kimlik blokları `00_PLAN.md`
§KİLİTLİ BLOKLAR (BLOK A birebir).

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → S151 (seçim) → S140 (bedel) → FAZ 14 → S180 →
> S1 → S8 → kalanı [D168 · `00_PLAN` ÜRETİM SIRASI]. ⛔ FAZ_12-15 yazılmadan
> bu sıra koşamaz; o güne kadar bu paketle yalnız **FAZ 1'in tetik klipleri**
> (S8 novum · S10 yüz) ve test klibi üretilir.
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Bu filmde
> tutulmayacak üç biçim: **vizör geometrisi** (kubbe daveti), **mat şeridin
> köşesi ve boyu** (TUR 16 #15: I2V köşe şeridini kendiliğinden temizler),
> **sırt paketi** (D139: boş sırt doldurulur).
>
> ⚠️ **BETİK DAVRANIŞI — 06.09.2026'da ÖLÇÜLDÜ:** `### 📸 IMAGE PROMPT` başlığı
> `prompt_kontrol.py`'nin BAŞLIK desenine UYAR; bu dosya DOSYA modunda normal
> imaj promptu gibi denetlenir (⑯ ⑮ ⑲ D79 · uzunluk). `## SAHNE n` başlığı
> TAŞIMADIĞI için KLASÖR modunun DİZİ kapılarına GİRMEZ.
> ⛔ **TEK KOŞUL: İngilizce prompt, başlıktan sonraki İLK çitli blok.** Künye ve
> kabul sınavı promptun ALTINDA.
>
> 🎨 **12.09.2026 — TASARIM REVİZYONU v4 "KATMANLI SERT PANEL" (sahip onayı):** v1
> renkli/rozetli → v2 beyaz-grafit → v3 güvenlik turuncusu, üçü "sade/düz/eski" bulundu;
> teşhis: "corrugated" körük + "squared" kutu sırt kelimeleri Apollo/EMU çiziyordu.
> v4: yarı parlak İNCİ BEYAZI sert üst gövde + sculpted omuz/dirsek/kalça/diz kapakları ·
> aralarında GUNMETAL esnek eklem, dar koyu boşluk · omuz/bilek/kalçada FIRÇALANMIŞ
> GÜMÜŞ rulman halkası · tek aksan ELEKTRİK CYAN (panel kenarı çizgisi + SOL kol/uyluk
> bandı + kask içi) · ince KONTÜRLÜ gunmetal sırt (büyük, arkadan girişli kalır) · yama 3
> (SAĞ göğüs · SOL göğüs · SOL omuz kapağı gri/cyan) · eldiven inci beyazı, parmak sırtı
> gunmetal · kask değişmedi · T14.2 hacim korundu, "corrugated" bilinçli çıktı [D74] ·
> toz "rust-orange"a geri döndü. RA · RB · RC · RD p1 · RP p2 yeniden yazıldı; v1-v3
> notları silindi (aynı gün, üretim yok, §7.2 ① bedelsiz). ⛔ Gerçek logo/bayrak/harf
> YAZILMADI: okunur metin D45'te ölçülmüş sızıntı, gerçek ajans/ülke ⑯ MİLLİYET 32
> doğrulanmış red — "logo" bu depoda METİNSİZ GEOMETRİ + RENK + SAYILABİLİR ÖĞE demektir.
>
> 📅 **11.09.2026 — dosya açıldı.** Sahip talebi: *"sık kullanılanların
> referanslarını hazırlamalıyız, part 1'de kullanılanlarla başla ve part 1 her
> sahnenin referanslarını yaz."* Bu sürüm FAZ 1'in çağırdığı her paneli TAM
> yazar (20 panel), FAZ 2+'nın panellerini ⏳ ile listeler (5 panel + RE).

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: RA — tek adam,
   S1-S9 ve F9-F14 kasklı; yüz kanalı camın ardında, F8'den sonra camın ardında
   ve GİDEREK MAT (kademe 4+ → yüz yalnız RC seed'iyle tutulur)
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: vizör
   geometrisi (eliptik kubbe + görünür rim + yaka halkası) · MAT ŞERİT (köşe ·
   boy · kademe) · sırt paketi (arkadan girişli kare) · hava kilidi (kol solda,
   iki menteşe)
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: MODÜL (5,3 H
   dikey silindir) · GEZİCİ (F8) · YÜKSELİŞ ARACI (3,7 H, F8+)
□ T4 İNSAN DIŞI CANLI                                            — (yok)
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: CAM AŞINMA
   MERDİVENİ — 12 kademe, yalnız artar, 180 sahnenin ~170'inde kadrajda [D147]
□ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: — (üretim yok)
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE SCOURED GLASS   FORMAT: yatay 10-20 dk (uzun uç, 30:00)   ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 3840×2160 (sayfa) · kırpım ≥1080 kısa kenar
SAHNE SAYISI: 180 (FAZ 1: S1-S12)
SAYFA: 7 (RA · RB · RC · RD · RF · RO · RP) + ⏳ RE
TOPLAM PANEL: 20 TAM (bu sürüm) + 5 ⏳ (RC p4 · RD p4 · RO p3 · RO p4 · RP p2) + RE ⏳ (4)
ARİTMETİK: RA 4 + RB 4 + RC 3 + RD 3 + RF 3 + RO 2 + RP 1 = 20   (⏳'ler sayılmadı)
   ⛔ Bu toplam §2 tablosunun TAM satırlarına EŞİT olmalı (§7 ①)
İMAJ MODELİ + SÜRÜM: ⬜ (sahip: sayfaların üretileceği imaj motoru; künyeye yazılır)
VİDEO: OMNI 1.1 Flash (I2V, tek imaj = start frame)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
TARİH: 11.09.2026 (TASLAK)
KİMLİK BLOĞU: `00_PLAN` BLOK A BİREBİR (dört öznitelik: kırklarında · ince yapılı ·
   kısa koyu saç · dört günlük sakal — D167 tavanı). ⛔ Bu paket beşinci
   özniteliği EKLEMEZ; yüz RC seed'iyle kilitlenir, metinle değil.
KAPAK: ⛔ bu pakette DEĞİL → `THE_SCOURED_GLASS_KAPAK.md` (RA + RC onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları (aşağıdaki öncelikle) → test klibi (D124) → S8 + S10
> tetik → [FAZ_12-15 yazılınca] S151 → S140 → FAZ 14 → S180 → S1 → kalanı.

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| RA | ADAM, KASKLI | 4 | 3/4 tam boy · profil · SIRT (paket) · vizör ardı yüz CU | 🔴 ZORUNLU — ilk sayfa | | | ⬜ TASLAK |
| RO | CAM MERDİVENİ | 2 (+2 ⏳) | p1 K0 berrak · p2 K1 köşe yaması (S9-S12 çapası; S8 çıktısı buna karşı ölçülür) | 🔴 ZORUNLU — S8'den önce | | | ⬜ TASLAK |
| RB | GİYSİ DETAYI | 4 | göğüs kadranı · sağ eldiven + ped · sağ kalça yumuşak eklemi (açıklık) · KASK ÇIKIK (nesne) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RC | ADAM, KASKSIZ | 3 (+1 ⏳) | 3/4 · profil · yüz CU (S10 tetik çapası) · ⏳ p4 zımbalı kalça (F2'den önce) | 🔴 ZORUNLU — S10'dan önce | | | ⬜ TASLAK |
| RD | MODÜL | 3 (+1 ⏳) | dış tam boy + 1H şahidi · hava kilidi · iç çekirdek · ⏳ p4 erzak rafı (F2/S13'ten önce) | 🔴 ZORUNLU — S5'ten önce | | | ⬜ TASLAK |
| RF | DIŞ MEKÂN — TOZ OVASI | 3 | geniş kurulum · orta bağlam (modül uzakta) · zemin dokusu | 🟠 S3'ten önce | | | ⬜ TASLAK |
| RP | PROPLAR | 1 (+1 ⏳) | p1 silme pedi (eldivenle ölçek) · ⏳ p2 su tüpü (F2'den önce) | 🟠 S8'den önce | | | ⬜ TASLAK |
| RE | GEZİCİ + YÜKSELİŞ ARACI | ⏳ 4 | F8'den önce yazılır — bu sürümde YOK | ⏳ sonra | | | ⏳ |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: OMNI/imaj arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp
   karşılaştırılır (yanlış dosyayla üretim yapılmasın).
⭐ RF NEDEN VAR (07.09 listesinde yoktu): dış mekân FAZ 1'in 9/12 sahnesinde ve
   filmin ~%70'inde kadrajda; kılavuz §2 "Dış mekân RD ✅" sınıfıdır ve gezegenin
   TEK ışığı kimliğin kendisidir (§4.1). Modülün kodu 07.09'da RD alındığı için
   ova RF oldu; kod kanonu korunur.
⭐ RB p3 DEĞİŞTİ (07.09: "diz/omuz rulman eklemi"): rulman RA p1-p2'de zaten
   okunur; sağ kalçadaki AÇIKLIK S6-S9'da dört sahnede taşıyıcıdır ve biçimi
   metinle tutulmaz (delik → yırtık → yara sapması, red defteri #4). Yer değişti.
⭐ RB p4 DEĞİŞTİ (07.09: "kask iç cyan şerit"): cyan şerit RA p4 ve RO p1'de
   okunur; S10-S12'de kask ELDE/BENCH'TE bir NESNEDİR ve o hâlin paneli yoktu.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| RA | adam, kasklı (giysi + kask + sırt paketi) | insan | S1 | S180 | RA | kask/vizör (D79·D146) · sırt (D139) · yüz camdan (D95) |
| RB-p1 | göğüs kadranı (rakamsız) + iki göğüs yaması | prop (giysi üstü) | S1 | S180 | RB | metin/rakam sızıntısı (D45) · sayaç (metne devredilir) · yamada harf sızıntısı (KABUL: harf 0) |
| RA-L | GİYSİ LİVERY'Sİ v4: katmanlı sert panel (inci beyazı yarı parlak paneller + sculpted kapaklar / gunmetal eklem, koyu panel boşluğu / omuz-bilek-kalça gümüş rulman halkası) · tek aksan elektrik cyan (panel çizgisi + SOL kol/uyluk bandı) · 3 metinsiz yama (2 göğüs + SOL omuz kapağı) · ince kontürlü gunmetal sırt + cyan üçgen · inci beyazı eldiven, gunmetal parmak sırtı · körük YOK | giysi kimliği | S1 | S180 | RA · RB p1 | ⑯ milliyet/kurum yanlış-pozitifi (gerçek amblem yok) · ayna hatası (şerit SOL — ⑥ ölçer) · nokta SAYISI halüsinasyonu (① ölçer) |
| RB-p2 | sağ eldiven + silme pedi | prop | S2 | S151 | RB · RP | kısıtlı uzuv makrosu (red #13) · toz fiziği |
| RB-p3 | sağ kalça yumuşak eklemi, açıklık | giysi durumu | S6 | S9 | RB | tehlike sözlüğü (red #4) — "opening", asla wound/tear |
| RB-p4 | kask, ÇIKIK (nesne: elde / bench'te) | prop | S10 | F15 | RB | kask çıkarma PB (red #3) — çıkarma EYLEMİ hiçbir panelde yok |
| RC | adam, kasksız (yüz) | insan | S10 | S180 | RC | OMNI "public figure" yanlış-pozitifi (red #15) — ≤4 öznitelik, yüz seed'le |
| RD | yaşam modülü (dış · hava kilidi · iç çekirdek) | mekân | S5 | F8 (dış) · F15 (iç anı) | RD | maket/tilt-shift okuması · ölçek şahidi (1H) |
| RF | toz ovası + bazalt + tek güneş | dış mekân | S1 | S168 | RF | tekdüze renk (risk kartı) · gölge kenarı · mavi gök sızıntısı |
| RO | cam aşınma merdiveni (K0 → K12) | tekrar eden olay | S1 (K0) · S8 (K1) | S180 (K12) | RO | ⭐ 1 NUMARALI RİSK: şerit doğmaz / temizlenir / buğu okunur (D192) |
| RP-p1 | silme pedi | prop | S8 | S151 | RP | "cloth" → dalgalanma (D153) — rijit koyu gri ped |
| RP-p2 ⏳ | su tüpü (çizgisiz) | prop | S13 | F13 | RP | ölçek çizgisi = metin sızıntısı |
| RE ⏳ | gezici · yükseliş aracı | araç | F8 | F15 | RE | F8'den önce yazılır |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Kod kanonu: kılavuz §2.
⛔ Envanterde olup sayfası olmayan varlık = çapasız varlık; sahnede yeniden
   tasarlanır. Sayfası olup hiçbir sahnede çağrılmayan = YETİM (§7 ②).
   Bu sürümde YETİM: 0 (her TAM panel §5'te en az bir sahnede çağrılıyor).
BELGEDE KALAN (sayılabilir · yer belirten → prompta iner): katmanlı panel (paneller
   İNCİ BEYAZI · eklemler GUNMETAL · rulman halkası GÜMÜŞ omuz/bilek/kalça) · bant 2
   CYAN (SOL kol · SOL uyluk) · yama 3 (SAĞ göğüs · SOL göğüs · SOL omuz kapağı) · altın
   nokta 3 · üçgen 1 (sırt üstü) · cyan çizgi her panel kenarında ·
   eldiven BEYAZ · vizör 1 cam · rim 1 ·
   yaka halkası 1 · kadran: yeşil yay SOL, kırmızı SAĞ, iğne 1 · sırt paketi 1,
   kare, arkadan girişli · hava kilidi: kol SOL, menteşe 2 · şerit: köşe = yeşil
   yay tarafı ALT, 3 parmak × 1 el · açıklık 1, 2 parmak.
YALNIZ GÖRSELDE KİLİTLENEN (dokunsal · sürekli → prompta İNMEZ): yamaların nakış
   dokusu ("embossed embroidery" yalnız RB p1'de) · giysi yüzey dokusu · toz dağılımının kendisi · yüz kemik yapısı · göz aralığı · sakal
   dokusu · modül kaplamasının dikiş deseni · bazalt kırık yüzeyi.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| vizör camı | RO-K0 | — (berrak, seyrek tane) | S1 | — | RO p1 |
| vizör camı | RO-K1 | köşe yaması 3 parmak × 1 el, kenar keskin | S8 (klip içi, D157 tek istisna) | S8 → S9 | RO p2 |
| vizör camı | RO-K5/6 ⏳ | alt yarı mat, göz hattı açık | F8 | faz sınırı | RO p3 ⏳ |
| vizör camı | RO-K11/12 ⏳ | %88-95 mat, yüz yalnız siluet | F13 | faz sınırı | RO p4 ⏳ |
| kask | RA (TAKILI) ↔ RB p4 (ÇIKIK, nesne) | durum ÇİFTİ, iki ayrı sayfa | S1 / S10 | kesmede (S9→S10) | RA · RB p4 |
| sağ eldiven avucu | RB p2 = K0 temiz | → K1 avuç + parmak içi pas rengi | S2 (klip içi) | S2 → S3 | **metne devredilir** (renk hâli; D146'nın OPTİK yarısı metinle 6/6 tuttu) |
| sağ kalça | RB p3 (AÇIKLIK) → RC p4 ⏳ (ZIMBALI) → kabuk → iz | giysi açıklığı → deri yarığı kapalı | S6 · S12 | S6 (kesmede) · S11 (klip içi) | RB p3 · RC p4 ⏳ |
| çene izi | RC p3 = K0 temiz yüz | → K1 kuru koyu çizgi (başparmak boyu) → K2 kabuk (F2+) | S10 | S10 (start frame'de var) | **metne devredilir** (çizgi + renk, ≥100 px) |
| sakal | RC p3 = 4 gün | 5 kademe, ≤3 cm, faz sınırında (SAKAL TOKENİ) | S10 | F2 · F5 · F8 · F12 | **metne devredilir**; F8'den sonra RC yeniden üretilir (§7.2 ①) |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönülüyorsa gerekçe satırı: YOK (dönüş yok) [D147 · D84]
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en):
   RO p1 ↔ RO p2 aynı kask makrosu, tek fark köşe yaması.
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişkidir. Bu dosyanın
   seçimi: RO sayfasında K0 ve K1 YAN YANA (p1 · p2) — çünkü S8'in kabul sınavı
   tam olarak bu ikisinin farkını ölçer; kırpım yüklenir, sayfa değil (§4.3).
⭐ S8 KURALI [⑳b · D179]: S8'in START FRAME'i RO-K0'dır (değişimin ÖNCESİ);
   RO-K1 paneli S8 çıktısının KABUL ÖLÇÜSÜ ve S9-S12'nin ÇAPASIDIR. S8 çıktısı
   K1 paneliyle uyuşmazsa S8 yeniden üretilir, panel değişmez (üstünlük §7.3).
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME — FAZ 1 (S1-S12)

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S1 | DIŞ · gün · güneş EKRAN-SAĞ | `RA p4` (vizör ardı yüz) · `RO p1` (K0) | üstten ECU, 100 mm | K0 · kask T | dış camda toz kabuğu + göz hizasında tek temiz bant · göz kapakları aralık · çenenin nefesle kalkışı · iğne KIRMIZI (kadraj dışı) |
| S2 | DIŞ · gün · güneş ÖNDE | `RB p2` (sağ eldiven, K0 temiz) · `RF p3` (zemin dokusu) | CU yan, 85 mm | K0 → avuç PAS (klip içi) | avuç toza basar, tanecik dökülmez · kol kadraj dışına devam eder (tek parça giysi) · bazalt ön planda |
| S3 | DIŞ · gün · güneş EKRAN-SOL-arkada | `RA p1` (3/4 tam boy) · `RF p1` (geniş kurulum) | EWS üst açı, 24 mm, 18 m | K0 | figür 1/8 · gövde çukuru + iki sürüklenme çiziği · tam tur · MODÜL KADRAJDA DEĞİL · ufukta iz yok |
| S4 | DIŞ · gün · güneş ARKADA (ön ışık) | `RA p2` (profil) · `RF p2` (orta bağlam) | WS profil, 24 mm, 12 m | K0 | telsiz basışı (sol eldiven göğüse) · tereddüt 1 s · kask 1° iner · ses POST |
| S5 | DIŞ · gün · güneş EKRAN-SAĞ-önde | `RA p3` (SIRT) · `RD p1` (modül tam boy) · `RF p2` | MS arkadan, 35 mm | K0 | modül ekran-SAĞ üçte bir, tabanı ufukta, kadrajın 1/9'u · kaskın sağa dönüşü · sırt paketinin sağ kenarı rim |
| S6 | DIŞ · gün · güneş ÖNDE-sol | `RB p3` (kalça açıklık) · `RA p2` (sağ flank) | MCU sağ yan, 50 mm | K0 · açıklık AÇIK | buhar ipliği (arkadan aydınlık, bir el yüksekliğinde biter) · sol avuç bastırır · iğne KIRMIZI |
| S7 | DIŞ · gün · güneş EKRAN-SOL | `RB p1` (kadran) · `RB p2` (eldiven — avuç PAS) | CU tepe 60°, 85 mm | K0 · iğne KIRMIZI ortada | iğne konumu (SAYAÇ: panelde yeşil, metinde kırmızı) · iki tıklatma · iğne SABİT · kask alt kenarı üstte |
| S8 | DIŞ · gün · güneş ARKADA (ön ışık) | `RA p4` (vizör ardı yüz) · `RO p1` (K0 = start) · `RP p1` (ped) | MCU cephe, 50 mm, 1,3 m | **K0 → K1 (klip içi)** | ped tek geçiş · şeridin doğuşu (3 parmak × 1 el, kenar keskin) · memnun baş sallama · ⛔ KABUL: çıktı şeridi `RO p2` ile aynı köşe, aynı boy |
| S9 | DIŞ · gün · güneş EKRAN-SAĞ | `RD p2` (hava kilidi) · `RA p1` (3/4, aksama) · `RO p2` (K1) | MS alçak 15°, 35 mm | K1 · kask T | soldan sağa aksayan yürüyüş · sağ el kalçada · kol iner, kapak bir el açılır · toz perdesi OTURUR · ufuk yok |
| S10 | İÇ · pratik, alttan | `RC p3` (yüz CU) · `RC p1` (kasksız 3/4) · `RB p4` (kask ÇIKIK, elde) | MCU, 50 mm | K1 (kask elde) · tek mühür | çene izi (sol, başparmak boyu) · ilk maskesiz nefes · kask kadraj dışına konur · omuz düşük · ⛔ KABUL: yüz `RC p3` ile yan yana (D68) |
| S11 | İÇ · pratik, soldan | `RC p1` (kasksız, oturur) · `RD p3` (iç çekirdek) | CU tepe 70°, 85 mm | K1 · yarık AÇIK (BEFORE) | avuç boyu deri yaması · yarık + zımba · üç sıkış · omuz yüksek → düşük · ⛔ referans yok — ⑳b: panel AFTER'ı (zımbalı) taşıyamaz |
| S12 | İÇ · pratik, alttan | `RC p3` (yüz) · `RD p3` (çekirdek) · `RB p4` (kask bench'te, şerit lense) | MCU 28 mm, doğrudan lens | K1 · tek mühür | replik 112,0-119,0 · dudak senkronu · eldiven kırışır · omuz düşük, sağ el kalçada · çene izi · altyazı 0 |
```
⛔ "METNE DEVREDİLEN" BOŞ BIRAKILAMAZ — referansın taşıyamadığı her şey
   (anlık eylem, geçici yansıma, hareket) buraya yazılır [kılavuz §5.1].
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2) — yukarıda hiçbir satır
   3'ü aşmaz. RF'nin ışık fazı her sahnede AYNI (gün, batı güneşi); ekran tarafı
   kameradan türer — RF paneli güneşi EKRAN-SOL-arkada taşır (S3 kanonu); başka
   taraflı sahnelerde RF yalnız zemin/gök/bazalt kimliği içindir, ışık yönü
   PROMPTA yazılır (LIGHTING satırı, δ tablosu).
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   ⚠️ Dört eski paket TERSİNİ yazıyor ve iddia ÖLÇÜLMEDİ; bu dosyanın seçtiği
   yükleme biçimi: KIRPIM · gerekçe: RO sayfasında K0 ve K1 yan yana durur —
   tam sayfa yüklenirse S1-S7'ye K1 şeridi bulaşır (§3 ② riski). İlk A/B koşusu
   S8'de yapılır ve sonucu buraya yazılır.
· OMNI referans çağırma söz dizimi ⚙️ SINANMAMIŞ — sahip ilk üretimde arayüzü
  yazar. Etiket KOD olur (RA · RO), asla özel ad [D34].
· FAZ_01 dosyasındaki `🎯 REFERANS` satırları bu tablonun kopyasıdır (11.09'da
  eşitlendi); ayrışırsa tablo düzeltilir.
```

## 6. 📸 REFERANS SAYFALARI
> ⛔ **İngilizce prompt BAŞLIKTAN SONRAKİ İLK çitli bloktur.** Künye ve kabul
> sınavı promptun ALTINA yazılır. Her sayfa 16:9, dört eşit panel (RF · RO · RP:
> üç ya da iki panel — aşağıda yazılı), nötr orta gri oluk, sayfada YAZI 0.
> ⛔ Kimlik sayfalarında (RA · RC) ışık NÖTR stüdyo; MEKÂN sayfalarında (RD · RF)
> ışık FİLMİN KENDİ IŞIĞI [kılavuz §4.1].

### 📸 IMAGE PROMPT — SAYFA RA · ADAM, KASKLI
```
A single photorealistic 16:9 character reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. The same one man appears in every panel, identical in every
detail; the backdrop in every panel is a plain flat neutral mid-grey
seamless studio wall with no horizon and no props; the lighting in every
panel is one even neutral white key from the upper screen-right, a soft
neutral fill from screen-left, and a small local light inside the helmet
that keeps the face readable at every head angle. Exactly one human
figure per panel, human count one in each.

THE SUBJECT (identical in all four panels): Exactly one human being. A
lean man in his forties, close-cropped dark hair, four days of dark
stubble on his jaw. He wears a bulky new-generation planetary pressure
suit built from layered hard-shell panels: a semi-gloss pearl-white
rigid upper torso shell, sculpted pearl-white hard caps over the
shoulders, elbows, hips and knees, gunmetal-grey soft articulated
joints between the panels, a narrow dark gap and a brushed-silver
bearing ring at each shoulder, wrist and hip, and shoulders half again
as wide as his own. One thin electric-cyan line runs along every panel
edge; one bold electric-cyan band wraps all the way around the LEFT
upper arm and one around the LEFT thigh. Three textless patches sit on
the white chest shell — a round badge with a thick metallic silver
chevron on dark navy on the RIGHT, a black hexagon with three gold dots
and one turquoise semicircle on the LEFT, a patch split diagonally into
matte grey and electric cyan on the LEFT shoulder cap — with no letters
on any of them. A slim contoured rear-entry backpack, matte gunmetal
with bevelled edges, follows the curve of his back from the collar ring
to the waist, one cyan triangle on a silver square panel on its top
face. A palm-sized mechanical needle gauge is set flat on the centre of
the white chest shell between the two patches: a plain dial with a green
arc on the left and a red arc on the right, one black needle, and no
numerals, no marks and no lettering of any kind. His helmet is a white
elliptical bubble with a single curved
front glass, optically clear with no tint and no mirror coating, so his
face is fully readable through it; a visible white rim frames the glass,
a closed collar ring seals it to the suit, one thin highlight runs along
the top edge of the pane, and a thin cyan strip light runs inside the
helmet rim. The gloves are pearl-white with gunmetal knuckle panels;
everywhere below the knee the suit is caked in fine rust-orange dust.
The glass carries no
matte patch, no band and no scratch anywhere. The back of the suit is
one continuous pearl-white panel from collar to waist, and the slim
contoured rear-entry backpack, matte gunmetal, follows the curve of it,
its hatch seam running straight down the middle, the cyan triangle on
its silver top panel; the pack is as wide as his shoulders and reaches
from the collar ring to the small of his back. Every patch is embossed
embroidery, each with one geometric motif and no lettering.

PANEL 1 (top-left): full body, three-quarter front, standing straight
on both boots, arms held slightly away from the body, gloves open and
empty, expression calm and neutral, eyes open and level; helmet to boots
in frame, the rust-orange dust ending in a clean line at the knees; the
pearl-white torso shell and sculpted caps over gunmetal joints, the
silver bearing rings at the shoulders, wrists and hips, the thin cyan
panel lines, the cyan band on the LEFT upper arm and LEFT thigh and the
three chest and shoulder patches all readable.
PANEL 2 (top-right): full body, exact left-side profile facing
screen-left, same stance; the gunmetal backpack reads as one slim
contoured slab following the back, the collar ring and the helmet rim
read as two closed circles, the chest gauge sits flat on the white torso
shell, the cyan LEFT arm and LEFT thigh bands face the lens, the
gunmetal joints and silver bearing rings between the white panels.
PANEL 3 (bottom-left): full body seen directly from behind: the one
continuous pearl-white back panel with the matte gunmetal contoured
rear-entry backpack following its curve, the hatch seam straight down
its middle, the cyan triangle on the silver panel on its top face, the
white shoulder caps over gunmetal joints either side, the cyan band
around the LEFT upper arm and LEFT thigh, the collar ring closing the
helmet to the suit; dust only below the knees.
PANEL 4 (bottom-right): close-up of the helmet and face, three-quarter
front, eyes open and level, mouth closed: the visor is a distinct clear
glass surface with one thin highlight along its top edge, the white rim
frames it all the way round, the closed collar ring sits below it, the
cyan strip glows inside the rim; the four days of stubble and the
close-cropped hair fully readable through the glass.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutters. No
readable text, letters, digits, numbers or symbols on any surface,
patch or dial. Exactly one human figure per panel, no duplicates within
a panel. Identical face, bone structure and eye spacing in all four
panels. The visor never becomes tinted, mirrored, opaque or frameless
and never disappears; no dome, no fishbowl, no frameless bubble. The
suit stays bulky and rigid, no skin-tight look, no leather look, no
superhero silhouette. No letters on any patch; no real-world flag, no
real agency or brand logo; no emblem beyond the three patches and the
backpack triangle named; the stripes stay on the LEFT side only. No
hose, no cable, no antenna, no second pack. Zero condensation, zero
fog, zero frost inside the visor. 0% bloom, no glow filter, no lens
flare, no waxy or smoothed skin, no airbrushing. No CGI or video-game
look. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş (S3)   p2 · profil — siluet (S4 · S6)
               p3 · SIRT — paket POZİTİF tarifli [D139] (S5)   p4 · vizör ardı yüz CU [D146] (S1 · S8)
⛔ "seamless visor" YAZILMADI: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANEL yokluk listesi değil MALZEME: "one continuous pearl-white panel …
   backpack high and flat on it" — D79'un düz-sırt kuralının BİLİNÇLİ istisnası
   (FAZ_01 §BİLİNÇLİ SAPMALAR ③: gezegen giysisi, arkadan girişli paket TASARIM).
⛔ Kimlik cümlesi = 00_PLAN BLOK A BİREBİR + "no band" cümlesi (K0) + sırt cümlesi
   (S5 promptuyla aynı) — ⑬ bayt aynılığı için `diff` ile sınanır.
```
```
KABUL SINAVI (RA) — dört alan ZORUNLU [D144]:
  KABUL:      p1-p4 dördünde de: vizör 1 cam + görünür rim + yaka halkası (3/3) ·
              p3'te sırt paketi 1, GUNMETAL, kontürlü (kutu değil), dikiş ortada, üstte
              1 cyan üçgen · paneller İNCİ BEYAZI / eklemler GUNMETAL, aralarında koyu
              boşluk · omuz-bilek-kalçada GÜMÜŞ halka (3 çift) · panel kenarlarında ince
              cyan çizgi · kadran: yeşil SOL / kırmızı SAĞ · rakam 0 · bant yalnız SOL kol
              + SOL uyluk, CYAN · yama 3 (sağ göğüs şevron · sol göğüs altıgen 3 nokta ·
              SOL omuz kapağı köşegen) ve hiçbirinde HARF yok · toz diz altında kalıyor
              · yüz p4'te camın ardından okunuyor · KÖRÜK YOK (eklem düz kumaş)
  RET:        kubbe/çerçevesiz vizör · ayna/tint · ikinci paket, hortum, anten ·
              kadranda rakam · toz dizden yukarı · p3'te boş sırt ya da altın ünite ·
              dört panelde farklı yüz · yamada harf/gerçek logo/bayrak · şerit SAĞ
              tarafa geçmiş ya da iki tarafta · altıgende 3'ten farklı nokta · tulum/
              süper kahraman silueti (T14.2) · körüklü/Michelin eklem (Apollo) · kutu
              sırt · eklemler beyaz ya da paneller koyu · rulman halkası yok
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "vizör kaç parça cam?" → "bir" ·
              "göğüste yeşil yay hangi tarafta?" → "sol" · "sırtında ne var?" → "koyu gri
              ince bir paket" · "giysi ne renk?" → "beyaz, eklemleri koyu" · "omuzda
              metal halka var mı?" → "var" · "mavi/cyan bant hangi kolda?" → "sol" ·
              "altıgen yamada kaç nokta?" → "üç" · "yamalarda yazı var mı?" → "yok"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S1-S9 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 4 (BLOK A ile aynı;
     kesin boy · ten · yüz biçimi · yüz işareti YOK) — betik FIX verirse gerekçe
     00_PLAN D167 kapısı: dördü de planın seçtiği dört; beşinci yazılmaz.
  ⑦b GRİ TON ⚙️: `ffmpeg -i RA_p4.png -vf hue=s=0 RA_p4_gri.png` — rim, yaka halkası
     ve kadran yayları renksiz de ayrılıyor mu (yay ayrımı yalnız renkse RET → yaylar
     farklı GENİŞLİKTE yeniden: yeşil dar, kırmızı geniş)
  ⑧ 120 px: p1'i 120 px'e indir — kask + kontürlü sırt + gümüş halkalar siluet okunuyor mu
```

### 📸 IMAGE PROMPT — SAYFA RO · CAM AŞINMA MERDİVENİ (K0 · K1)
```
A single photorealistic 16:9 reference sheet, maximum resolution,
divided into two equal panels side by side by one thin neutral mid-grey
gutter. Both panels show the same helmet on the same man from exactly
the same camera position, the same distance and the same lens, at eye
level, near-frontal; the backdrop in both panels is a plain flat neutral
mid-grey seamless studio wall; the lighting in both panels is one even
neutral white key from directly behind the camera, full front light, so
the glass and the face read flat and clear, plus a small local light
inside the helmet. Exactly one human figure per panel, human count one
in each. The two panels are identical in every respect except the one
difference stated below.

THE SUBJECT (identical in both panels): the head and shoulders of a
lean man in his forties, close-cropped dark hair, four days of dark
stubble on his jaw, inside a white elliptical helmet with a single
curved front glass held in a visible white rim, a closed collar ring
sealing it to the rigid white upper torso shell of a bulky planetary
pressure suit; one thin highlight runs along the top edge of the pane
and a thin cyan strip light runs inside the helmet rim. The glass is
optically clear with no tint and no mirror coating and the face is
fully readable through it, eyes open and level, mouth closed. A palm-
sized mechanical needle gauge sits flat on the chest plate at the bottom
of the frame: a plain dial with a green arc on the left and a red arc
on the right, one black needle standing in the green arc, no numerals,
no marks, no lettering. A sparse scatter of fine rust-orange grains
lies on the outside of the glass.

PANEL 1 (left) — STATE ZERO: the glass is clear everywhere. No matte
patch, no band, no scratch anywhere on the pane; 0 droplets, 0 cracks,
0 fog, 0 reflections.
PANEL 2 (right) — STATE ONE: identical to panel 1 in every respect
except this: one matte abraded band sits at the lower corner of the
glass on the same side as the green arc of the chest dial, the
screen-LEFT lower corner, running level, three finger-widths tall and a
hand's length long, its upper edge sharp; the band is chalky matte,
micro-abraded, flat and dull, with 0 droplets, 0 cracks, 0 fog and 0
reflections in it; the glass keeps its exact shape, the rest of the pane
stays clear, and the face stays fully readable above the band.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutter. No
readable text, letters, digits or symbols on any surface or dial.
Exactly one human figure per panel. Identical face, helmet, rim, collar
ring, lighting and framing in both panels; nothing else differs. The
visor never becomes tinted, mirrored, opaque or frameless; no dome, no
fishbowl. The band in panel 2 is never a reflection, never fog, never
condensation, never a crack, never a smear of liquid; it never reaches
the eyes. Zero condensation, zero fog, zero frost inside the visor. 0%
bloom, no glow filter, no lens flare, no soft focus. No CGI or
video-game look. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU — S8'DEN ÖNCE   PANEL: 2 (+2 ⏳)   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · K0 berrak (S1-S7 · S8 START)   p2 · K1 köşe yaması (S9-S12 çapası · S8 KABUL ölçüsü)
               ⏳ p3 · K5/6 alt yarı mat (F8-F10) — F8'den önce yazılır, aynı kadraj
               ⏳ p4 · K11/12 %88-95 mat, yüz siluet (F13-F15) — F12'den önce
⭐ 1 NUMARALI RİSKİN ARACI [D192 · TUR 16 #15]: şerit metinle tutulmadı (YERÇEKİMİ F2
   emsali: geometri 0/6); bu iki panel farkın kendisidir. Sayı cümlesi 00_PLAN
   KİLİT 1 ⑤ ile BİREBİR ("three finger-widths tall and a hand's length long, its
   upper edge sharp; 0 droplets, 0 cracks, 0 fog, 0 reflections").
⛔ DURUM ÇİFTİ KURALI: aynı kadraj · aynı ışık · aynı mesafe · TEK FARK — bu sayfanın
   iki paneli o kuralın kendisidir; ±%3'ten fazla kadraj kayması RET.
```
```
KABUL SINAVI (RO) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de cam üzerinde mat alan 0 · p2'de mat alan TAM 1, sol alt köşede,
              seviye, kenarı keskin; yüksekliği yüz-göreli üç parmak, boyu bir el ·
              p1↔p2 farkı yalnız şerit (yüz, rim, ışık, kadraj aynı) · yüz p2'de okunur
  RET:        şerit sağ köşede / gözlere ulaşıyor / tüm cam matlaşmış · şerit buğu, damla,
              yansıma ya da çatlak okunuyor · p1'de de bir leke var · iki panelde yüz farklı
  YABANCI GÖZ: soru: "sağdaki camda ne var?" → "sol alt köşede mat bir yama" ·
              "kaç tane?" → "bir" · "soldaki camda?" → "hiçbir şey"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S8-S12 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 4 (BLOK A'nın dördü)  ⑦b GRİ TON: şerit renksiz de ayrılıyor mu
     (mat/parlak farkı renk değil, parlaklık — geçmeli)
  ⑧b KRİTİK AYRINTI: p2 kırpımı S9'un 5 m/35 mm kadrajına indirildiğinde şerit ≥12 px
     sürüyor mu (hesap: kask ~0,35 m/2,9 m kadraj → kask 130 px, şerit ~15 px ✓ sınırda)
```

### 📸 IMAGE PROMPT — SAYFA RB · GİYSİ DETAYI
```
A single photorealistic 16:9 equipment reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. Every panel is a close-up of one detail of the same bulky
white planetary pressure suit worn by the same one man; the backdrop in
every panel is a plain flat neutral mid-grey seamless studio wall with
no horizon and no props; the lighting in every panel is one even neutral
white key from the upper screen-right and a soft neutral fill from
screen-left, product lighting, everything sharp. At most one human
figure per panel, and only the part of him named in that panel.

THE SUIT (identical in all four panels): layered hard-shell panels —
semi-gloss pearl-white rigid upper torso shell and sculpted pearl-white
hard caps over the shoulders, elbows, hips and knees; gunmetal-grey soft
articulated joints between the panels with a narrow dark gap; a
brushed-silver bearing ring at each shoulder, wrist and hip; one thin
electric-cyan line along every panel edge; fine rust-orange dust caked
everywhere below the knee; pearl-white gloves with gunmetal knuckle
panels; one electric-cyan band around the LEFT upper arm and one around
the LEFT thigh. No lettering anywhere on the suit; no real-world flag,
no real agency or brand logo.

PANEL 1 (top-left): the chest plate seen from directly in front at
chest height, filling the frame: in the centre a palm-sized mechanical
needle gauge set flat on the rigid pearl-white shell — a plain white dial
with a green arc on the left and a red arc on the right, one black
needle standing in the middle of the green arc, no numerals, no marks
and no lettering; a raised white rim around the dial; a thin line of
rust-orange dust lying in the seam of the rim. On the RIGHT chest,
screen-left of the gauge, a textless round badge: a thick metallic
silver chevron on a dark navy background, embossed embroidery. On the
LEFT chest, screen-right of the gauge, a textless hexagonal patch:
black, with three distinct gold dots in a row and one turquoise
semicircle below them, embossed embroidery. The sculpted pearl-white
shoulder caps with their thin cyan edge lines, the silver shoulder
bearing rings, and the lower edge of the collar ring at the top corners
of the frame; the diagonal grey-and-cyan patch on the LEFT shoulder cap
just inside the top screen-right corner.
PANEL 2 (top-right): his right glove alone, palm turned to the lens,
the gunmetal forearm joint with its brushed-silver wrist bearing ring
and thin cyan edge line running out of the frame at screen-left, one
continuous suit joined to the body beyond the frame; the glove is
pearl-white, clean, with articulated finger joints and gunmetal knuckle
panels on its back; flat
on the open palm lies
a stiff dark grey wiping pad the size of the palm, a dense rigid
rectangular block with rounded corners that keeps its shape.
PANEL 3 (bottom-left): his right hip seen from the right side at hip
height: the lower edge of the sculpted pearl-white hip cap and its
silver bearing ring above, the gunmetal soft joint of the hip below it
with a thin cyan line along the panel edge; in that soft joint sits exactly one
opening, two finger-widths wide, its edges curled outward, a pale dried
ring on the gunmetal joint around it; every other surface of
the suit intact; the left glove enters from the top of the frame,
fingertips resting beside the opening.
PANEL 4 (bottom-right): the helmet alone, off the man, held low in two
pearl-white gloved hands at chest height, seen from the front: a white
elliptical bubble with a single curved front glass held in a visible
white rim, its open neck ring tipped a little toward the floor, a thin
cyan strip light lit inside the rim, one thin highlight along the
top edge of the pane; the glass clear with no matte patch, no band and
no scratch; nothing and no one inside it; the white gloved hands and
the gunmetal sleeves run out of the bottom of the frame.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutters. No
readable text, letters, digits, numbers or symbols on any surface,
patch or dial; no numerals on the gauge; no letters on any patch; no
real-world flag, no real agency or brand logo; exactly three patches on
the suit — two on the chest, one on the LEFT shoulder cap — and none
elsewhere. No face in any panel; exactly
one human being's suit parts appear and no second person, human count
at most one per panel. The wiping pad is rigid and flat — it does not fold, drape, fray or flutter.
The helmet in panel 4 is empty and off the body; no head inside it. The
opening in panel 3 is a single small gap in a gunmetal joint — nothing
spreads from it, nothing runs, no liquid. No patch on the hip, the
glove or the helmet — the three patches sit on the torso only. 0%
bloom, no glow filter, no lens flare, no soft focus. No CGI
or video-game look. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · göğüs kadranı makro (S1 · S6 · S7)   p2 · sağ eldiven + ped, K0 temiz (S2 · S7 · S8)
               p3 · sağ kalça yumuşak eklemi, açıklık (S6-S9)   p4 · KASK ÇIKIK, nesne (S10 · S12)
⛔ SAYAÇ KURALI: iğne panelde YEŞİL yaydadır (temel); her sahnenin iğne konumu
   METNE devredilir (kılavuz §3 SAYAÇ satırı) — panel kadranın BİÇİMİNİ kilitler,
   değerini değil.
⛔ p3 SÖZLÜĞÜ: "opening" · "soft joint" · "pale dried ring" (gunmetal üstünde koyu halka okunmaz) — wound/tear/hole/leak/
   torn/fabric hiçbir yerde [red defteri #4 · UZAY_USSU §6].
⛔ p4: kask ÇIKARMA eylemi yok, kask zaten çıkmış bir NESNE (red defteri #3 · B6).
   Bu panel S10'un "helmet already off, held low in both gloved hands" start
   frame'inin çapasıdır; S12'de bench'te.
⚠️ p2/p3 kısıtlı uzuv makrosu (red #13): her ikisinde de kol/eklem KADRAJ DIŞINA
   devam eder ("one continuous suit joined to the body beyond the frame").
```
```
KABUL SINAVI (RB) — dört alan ZORUNLU [D144]:
  KABUL:      p1 yeşil yay SOL · kırmızı SAĞ · iğne 1 · rakam 0 · şevron rozeti kadranın
              ekran-solunda (sağ göğüs) · altıgen ekran-sağında, nokta 3 · yamalarda harf 0 ·
              p2 ped koyu gri, dik-
              dörtgen, eldivenden ayrışıyor (siluet testi) · p3 açıklık TAM 1, iki parmak ·
              p4 kask boş, rim + yaka halkası + cyan şerit görünür, cam berrak
  RET:        kadranda rakam/çentik · ped açık gri ya da kumaş gibi kıvrılmış · p3'te
              birden çok açıklık ya da yırtık/yara okuması · p4'te kaskın içinde baş ·
              herhangi bir panelde yüz
  YABANCI GÖZ: "kadranda kaç iğne?" → "bir" · "altıgende kaç nokta?" → "üç" · "rozette
              yazı var mı?" → "yok" · "eldivendeki şey ne renk?" → "koyu gri" ·
              "kalçada kaç delik?" → "bir" · "kaskın içinde kim var?" → "kimse"
  SONUÇ:      ⬜ (geçmezse ilgili panel yeniden · o paneli çağıran sahneler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 0 (yüz yok)   ⑦b GRİ TON: p1 yaylar renksiz ayrılmıyorsa RET
  ⑧ 120 px: p2'de ped eldivenden ayrılıyor mu (D78 siluet testi)
```

### 📸 IMAGE PROMPT — SAYFA RC · ADAM, KASKSIZ (İÇ)
```
A single photorealistic 16:9 character reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters; the fourth panel, bottom-right, is left as plain empty
mid-grey wall. The same one man appears in the three filled panels,
identical in every detail; the backdrop in every panel is a plain flat
neutral mid-grey seamless studio wall with no horizon and no props; the
lighting in every panel is one even neutral white key from the upper
screen-right and a soft neutral fill from screen-left, shadows soft,
skin texture and pores readable. Exactly one human figure per filled
panel, human count one in each.

THE SUBJECT (identical in all filled panels): Exactly one human being.
A lean man in his forties, close-cropped dark hair, four days of dark
stubble on his jaw, bare-headed. He wears the lower body and the rigid
pearl-white upper torso shell of a bulky planetary pressure suit, its
collar ring open at the neck and empty — the helmet is off and out of
frame; both gloves stay on. The suit is a bulky new-generation
planetary pressure suit built from layered hard-shell panels: a
semi-gloss pearl-white rigid upper torso shell, sculpted pearl-white
hard caps over the shoulders, elbows, hips and knees, gunmetal-grey
soft articulated joints between the panels, a narrow dark gap and a
brushed-silver bearing ring at each shoulder, wrist and hip, and
shoulders half again as wide as his own. One thin electric-cyan line
runs along every panel edge; one bold electric-cyan band wraps all the
way around the LEFT upper arm and one around the LEFT thigh. Three
textless patches sit on the white chest shell — a round badge with a
thick silver chevron on dark navy on the RIGHT, a black hexagon with
three gold dots and one turquoise semicircle on the LEFT, a patch split
diagonally into matte grey and electric cyan on the LEFT shoulder cap —
with no letters on any of them; a slim contoured rear-entry backpack,
matte gunmetal, following the curve of his back. The gloves are
pearl-white with gunmetal knuckle panels. A palm-sized mechanical
needle gauge flat
on the centre of the white chest shell between the two patches, a plain
dial with a green arc on the left and a red arc on the right, one black
needle, no numerals, no marks, no lettering. Everywhere below the knee
the suit is caked in fine rust-orange dust. His face
is clean: no marks, no lines, no dust on the skin. Expression calm and
neutral, eyes open and level, mouth closed.

PANEL 1 (top-left): full body, three-quarter front, standing straight,
arms slightly away from the body, gloves open and empty, the open
collar ring reading as a white circle around the base of the neck.
PANEL 2 (top-right): head and shoulders, exact left-side profile facing
screen-left: the line of the jaw, the close-cropped hair, the open
collar ring, the pearl-white shoulder cap over its silver bearing ring.
PANEL 3 (bottom-left): close-up of the bare face, three-quarter front,
from the top of the head to the open collar ring, eyes open and level
into the lens, mouth closed: the four days of stubble, the cropped hair
and the skin texture fully readable; nothing on the face.
PANEL 4 (bottom-right): empty plain mid-grey wall, nothing in it.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutters. No
readable text, letters, digits, numbers or symbols on any surface,
patch or dial. Exactly one human figure per filled panel, no duplicates.
Identical face, bone structure, eye spacing and hairline in all three
filled panels — the same man as the helmeted reference. No helmet
anywhere in the sheet. The gloves never come off. No letters on any
patch; no real-world flag, no real agency or brand logo; no emblem
beyond the three patches named; stripes on the LEFT side only. 0%
bloom, no glow filter, no lens flare, no waxy or smoothed
skin, no airbrushing, no beauty retouch. No CGI or video-game look.
Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU — S10'DAN ÖNCE   PANEL: 3 (+1 ⏳)   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · kasksız 3/4 tam boy (S10 · S11 · S12)   p2 · profil (F2 günlükleri dışı)
               p3 · yüz CU — S10 TETİK ÇAPASI [D68] (S10 · S12 · 24 günlük)
               ⏳ p4 · sağ kalça, zımbalı kapalı yarık (S12'den sonra, F2-F5 kabuk merdiveni) —
                  POLİTİKA §3.2 makro riski: önce S11 üretilir; geçerse S11'in son karesi
                  çapa olur ve panel GEREKMEYEBİLİR. Bu sürümde boş panel.
⛔ YÜZ SEED KURALI [D167 · red #15]: yüz bu sayfanın seed'iyle kilitlenir; sahne
   promptlarına ten, boy, yüz biçimi, yüz işareti EKLENMEZ. Öznitelik 4.
⛔ RA ile AYNI ADAM: RA p4 (camın ardındaki yüz) ve RC p3 yan yana bakılır (⑦);
   kemik yapısı / göz aralığı / saç çizgisi farklıysa İKİSİ DE yeniden.
⛔ Çene izi (S10+) bu sayfada YOK — durum, metne devredilir (§4).
```
```
KABUL SINAVI (RC) — dört alan ZORUNLU [D144]:
  KABUL:      üç panelde aynı yüz · sakal 4 gün (kısa, düzgün) · eldivenler takılı ·
              yaka halkası açık ve boş · kask hiçbir panelde yok · yüzde iz 0
  RET:        farklı yüz/yaş · sakal uzun ya da yok · eldiven çıkmış · kask kadrajda ·
              yüzde çizgi/iz · pürüzsüzleştirilmiş cilt · dördüncü panelde figür
  YABANCI GÖZ: RA p4 ile yan yana: "bu aynı adam mı?" → "evet" · "kaç günlük sakal?" →
              "birkaç günlük" · "eldiven var mı?" → "var"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden · S10-S12 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 4   ⑦ İKİ FİGÜR: RA p4 ↔ RC p3 aynı kişi testi
  ⑧ 120 px: p3 120 px'te bir yüz okunuyor mu (S1 kapak sınavının aynısı)
```

### 📸 IMAGE PROMPT — SAYFA RD · YAŞAM MODÜLÜ (dış · hava kilidi · iç)
```
A single photorealistic 16:9 location reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters; the fourth panel, bottom-right, is left as plain empty
mid-grey. Panels 1 and 2 are exterior views lit by the location's own
single light; panel 3 is an interior lit only by its own practical
lamps. Exactly one human figure appears, in panel 1 only, as a scale
witness.

THE MODULE (identical in panels 1 and 2): a vertical cylindrical
habitat module standing on a rust-orange dust plain, bone-white, its
outer skin thick quilted rigid insulation with grey dust lying in every
seam, as tall as five men standing one on top of another and about as
wide as it is tall at the base, with a flat top; its base caked in
rust-orange dust. One round hatch, taller than a man, sits in the
flank at ground level, with a long metal lever on the screen-LEFT side
of the hatch at chest height and two hinges on the screen-RIGHT side;
one hatch only. No flag, no logo, no lettering, no antenna, no window.

PANEL 1 (top-left): wide exterior, eye level, the whole module from
footing to flat top inside the frame with sky above it; the suited man
of the film — bulky planetary pressure suit of layered pearl-white
hard-shell panels over gunmetal joints, a cyan band around the LEFT
upper arm and LEFT thigh, a slim contoured matte gunmetal backpack,
white elliptical
helmet with a clear front glass — standing at its
foot beside the hatch, facing the lens, as a scale witness, his helmet
reaching only to the lower rim of the hatch. The sky is a pale
butterscotch haze, yellow and brown, no clouds, no blue; one small hard
sun sits low, about fifteen degrees above the horizon, to screen-LEFT
and behind the camera, and every shadow falls to screen-RIGHT with a
razor edge, the insides of the shadows cold slate blue, never black.
Angular black basalt rocks scattered on the plain.
PANEL 2 (top-right): the hatch alone, straight on, low angle from just
above the ground: the round hatch filling most of the panel, its rim
raised a finger's width from the quilted flank, the long metal lever on
the screen-LEFT side at chest height, the two hinges on the
screen-RIGHT side, rust-orange dust lying along the bottom of the hatch
seam; the same single sun to screen-LEFT, shadows to screen-RIGHT, slate
blue cores; no horizon in the panel — the quilted wall fills it edge to
edge.
PANEL 3 (bottom-left): interior, eye level, looking at the core: inside
a pressurised habitat, a vertical cylindrical space with a rigid
bone-white central core and thick quilted inflatable outer walls
curving up and over; bundled grey cable looms run down the core; a
short bone-white bench juts from the core at knee height; the wall
panel of the core beside the bench is smooth and unmarked. Lighting is
practical only — two warm work lamps mounted low on the core and one
cool cyan strip along the floor — so the light comes from below and the
ceiling stays in darkness. Fine rust-orange dust has settled into every
seam and every horizontal edge. No person in this panel.
PANEL 4 (bottom-right): empty plain mid-grey, nothing in it.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutters. No
readable text, letters, digits, numbers or symbols on any surface; no
flag, logo, patch or emblem on the module — the witness figure keeps
his suit's own three textless patches. No tilt-shift or toy-model look; the far
edge of the module is as sharp as the near edge. Insulation and covers
are rigid and taut. Only one hatch, only one lever. No window, no
antenna, no dish, no second structure. No blue sky, no
clouds, no stars. No light from above in panel 3, no ceiling fill, no
screens, no interface. Exactly one human figure in panel 1 and none
elsewhere. 0% bloom, no glow filter, no lens flare, no soft focus. No
CGI or video-game look. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU — S5'TEN ÖNCE   PANEL: 3 (+1 ⏳)   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · dış tam boy + 1H şahidi (S5 · S9 arka plan)   p2 · hava kilidi (S9)
               p3 · iç çekirdek, bench, ÇENTİK DUVARI BOŞ (S10 · S11 · S12)
               ⏳ p4 · erzak rafı, 4 sıra × 10 gümüş paket (S13'ten önce) — bu sürümde boş
⛔ ÖLÇEK ŞAHİDİ [⑪]: p1'de adam kadrajda — modül 5,3 H; "as tall as five men"
   gövde-göreli, metre YOK [UZAY_USSU §1 · D138].
⛔ HAVA KİLİDİ GEOMETRİSİ (belgede kalan, prompta inen): kol SOL · menteşe 2 SAĞ ·
   kapak 1. S9'un promptu bununla çelişirse PANEL kazanır (§7.3).
⛔ p3 IŞIK = BLOK B2 BİREBİR (iç sahnelerin ışığı); "çentik duvarı BOŞ" = smooth and
   unmarked wall panel (F2'de ilk çizik atılır; kademe metne devredilir).
```
```
KABUL SINAVI (RD) — dört alan ZORUNLU [D144]:
  KABUL:      p1 modül tam boy kadrajda + adam kapak rimine kadar · kapak 1, kol SOL,
              menteşe 2 SAĞ · pencere/anten/bayrak 0 · p2 ufuk yok · p3 ışık alttan,
              tavan karanlık, bench var, duvar boş
  RET:        modül maket/oyuncak okunuyor · birden çok kapak · kol sağda · pencere ·
              gökte mavi · p3'te tavandan ışık ya da ekran/yazı · p1'de ikinci figür
  YABANCI GÖZ: "kapı kaç tane?" → "bir" · "kol hangi tarafta?" → "sol" · "içerideki ışık
              nereden geliyor?" → "aşağıdan"
  SONUÇ:      ⬜ (geçmezse ilgili panel yeniden · S5 · S9 · S10-S12 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: p1 şahit için 0 (yalnız giysi)   ⑧c ÖLÇEK: p1'de 1H şahidi ✓
```

### 📸 IMAGE PROMPT — SAYFA RF · DIŞ MEKÂN — TOZ OVASI
```
A single photorealistic 16:9 location reference sheet, maximum
resolution, divided into three equal vertical panels side by side by
thin neutral mid-grey gutters. All three panels show the same place
under the same single light. No human figure in any panel, no
structure, no track, no footprint.

THE PLACE (identical in all three panels): The surface of a cold desert
world. A rust-orange plain of very fine dust, scattered with angular
black basalt rocks, runs to a low eroded massif on the far horizon. The
sky is a pale butterscotch haze, yellow and brown, with no clouds and
no blue anywhere in it. One small hard sun sits low, about fifteen
degrees above the horizon, to screen-LEFT and behind the camera, and
every shadow falls to screen-RIGHT with a razor edge; the insides of
the shadows read cold slate blue, never black. The air is thin and
still; nothing in it moves. No vegetation, no water, no snow, no ice.

PANEL 1 (left) — WIDE ESTABLISHING: wide lens, eye level, the horizon
in the lower fifth of the frame, the massif a low broken line on it,
the plain empty from edge to edge, a few basalt rocks in the middle
distance, the sky filling the upper four fifths.
PANEL 2 (centre) — MID CONTEXT: normal lens, eye level, the horizon at
one third from the bottom; a cluster of angular black basalt rocks
about knee height in the foreground at screen-LEFT throwing razor-edged
shadows to screen-RIGHT with slate-blue cores; the plain running back
to the massif.
PANEL 3 (right) — GROUND TEXTURE: close, steep downward angle onto the
ground, no horizon: the very fine rust-orange dust lying in a smooth
unbroken skin, one fist-sized angular black basalt rock half sunk in
it, its razor shadow to screen-RIGHT, a shallow curved groove in the
dust beside it where something rested and was lifted away; the dust
in the groove lies where it fell.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutters. No
readable text, letters, digits or symbols anywhere. No human figure,
human count zero; no structure, no footprint, no track, no flag. No
blue sky, no clouds, no stars, no second sun, no moon. No wind, no
blowing dust, no dust in the air, no haze on the ground. No water, no
ice, no plants. The sun never appears on the screen-RIGHT side. 0%
bloom, no glow filter, no lens flare, no soft focus. No CGI or
video-game look. Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S3'TEN ÖNCE   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · geniş kurulum (S3)   p2 · orta bağlam (S4 · S5)   p3 · zemin dokusu (S2)
⛔ ORTAM = BLOK B1 BİREBİR, güneş tarafı S3 kanonunda (EKRAN-SOL-arkada) — bu
   sayfanın TEK amacı zemin/gök/bazalt kimliğidir; sahne başına güneş tarafı
   PROMPTTAN gelir (δ tablosu), panelden değil. ⛔ Ters taraflı sahnede (S1 · S5 ·
   S9 güneş SAĞ) RF ile prompt çelişir mi? Hayır: gölge yönü zeminin kimliği değil,
   ışık satırıdır — VEO §6B: referansla çelişen ışık yazılmaz, ama burada referans
   IŞIK değil DOKU için yükleniyor. İlk çelişki üretimde görülürse RF yalnız S3 · S4
   · S7'ye (güneş SOL) yüklenir, diğerlerine yüklenmez — gerekçe buraya yazılır.
⛔ TEKDÜZE RENK RİSKİ (02_RISK_KARTLARI): kırmızı-turuncu havuz — bazalt siyahı ve
   arduvaz gölge içi bu sayfada ölçülür (SPEC KAPI 3 YMAX−YMIN ≥110 aynı panele koşar).
```
```
KABUL SINAVI (RF) — dört alan ZORUNLU [D144]:
  KABUL:      gökte mavi 0 · gölge kenarı keskin, içi arduvaz mavisi (siyah değil) ·
              havada toz 0 · p1 ufuk alt beşte birde · p3'te ufuk yok · figür/yapı/iz 0
  RET:        mavi gök · yumuşak/çift gölge · havada toz perdesi · su/buz/bitki · ayak izi
              · ikinci güneş ya da ay
  YABANCI GÖZ: "gök ne renk?" → "sarı-kahve" · "gölgelerin içi?" → "mavi" · "havada
              bir şey var mı?" → "yok"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden · S3 ÜRETİLMEZ; S1-S2 RF'siz üretilebilir)
  ⑲ KİMLİK YIĞINI: 0   KAPI 3 KONTRAST: `ffmpeg -i RF_p2.png -vf signalstats -f null -` YMAX−YMIN ≥110
```

### 📸 IMAGE PROMPT — SAYFA RP · PROPLAR (silme pedi)
```
A single photorealistic 16:9 prop reference sheet, maximum resolution,
divided into two equal panels side by side by one thin neutral mid-grey
gutter. Both panels show the same one object on a plain flat neutral
mid-grey seamless surface under even neutral product lighting, one soft
key from the upper screen-right and a clean fill, everything sharp. No
face, no body, no second object.

THE OBJECT (identical in both panels): a stiff dark grey wiping pad, a
dense rigid rectangular block with rounded corners, as long as a man's
palm and a little narrower, about a finger thick, matte, with a fine
even grain on its faces; it keeps its shape and does not bend. One face
carries a thin dusting of fine rust-orange grains along one edge.

PANEL 1 (left): the pad alone, three-quarter view from slightly above,
lying flat on the grey surface, its thickness and rounded corners
readable, its shadow crisp to screen-RIGHT.
PANEL 2 (right): the same pad lying flat on the open palm of a
pearl-white gloved right hand with articulated finger joints, the hand
entering from the bottom of the frame, the gunmetal forearm joint with
its silver wrist bearing ring running out of the frame — one continuous
suit joined to a body beyond the frame; the pad
covers most of the palm, the fingertips clear beyond its far edge.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension lines,
panel titles or watermarks anywhere on the sheet or in the gutter. No
readable text, letters, digits, numbers or symbols on any surface. The
pad is never a folded cloth, never a sponge, never a towel, never pale
grey, never white; it does not fold, drape, fray, curl or flutter. No
face, no head, no second hand, no second object; human count zero in
panel 1 and at most one gloved hand in panel 2, no second person. 0%
bloom, no glow
filter, no lens flare, no soft focus. No CGI or video-game look.
Photorealistic, 35mm film grain.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S8'DEN ÖNCE   PANEL: 1 tam (2 görünüm) (+1 ⏳)   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · silme pedi — yalnız · eldivende (S8 · S31 · S94 · F10 · S151)
               ⏳ p2 · su tüpü — şeffaf silindir, çizgisiz, dereceli değil, su/hava sınırı tek
                  okuma (S13'ten önce) — bu sürümde yok
⛔ D78 SİLUET TESTİ: bedel nesnesi BEYAZ ELDİVENDEN ve beyaz kask camından ayrışmalı
   → KOYU gri (07.09'un "pale grey cloth"u 11.09'da değişti; sözlük D153/UZAY_USSU §6).
   ⚠️ Livery v4'te ön kol eklemi GUNMETAL: ped avuçta durur, kol kadraj dışına çıkar —
   ped ↔ kol ayrımı bu sayfada ölçülmez, ped ↔ eldiven/cam ölçülür (S8'de ped camın önündedir).
⛔ NEGATIVE'de "cloth/towel/sponge" YALNIZ yasak listesinde — kılavuz kuralı
   "fabric/cloth prompt gövdesine girmez"; negatifte durması red defteri #2
   (uzun negatif) sınırında kısa tutuldu. Sızarsa negatiften de silinir.
```
```
KABUL SINAVI (RP) — dört alan ZORUNLU [D144]:
  KABUL:      ped koyu gri (eldivenden ve zeminden ayrışıyor) · dikdörtgen, köşeler
              yuvarlak, rijit · p2'de eldivenli elde, kol kadraj dışına devam ediyor
  RET:        açık gri/beyaz · kıvrılmış/katlanmış/püsküllü · sünger okuması · ikinci nesne
  YABANCI GÖZ: "bu ne?" → "koyu gri bir blok/ped" · "kaç tane?" → "bir"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden · S8 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 0   ⑦b GRİ TON: ped eldivenden renksiz de ayrılıyor (koyu ↔ beyaz) ✓ beklenir
```

### ⏳ SAYFA RE · GEZİCİ + YÜKSELİŞ ARACI — F8'DEN ÖNCE
```
Bu sürümde YAZILMADI (FAZ 1'de kadrajda değil). Yazılacağı gün: FAZ_08 promptundan
önce. Kaynak: 00_PLAN RECURRING ENTITY (gezici 3,2 × 2,7 × 2,0 H, ön cam tek parça,
4 tekerlek, üstte panel · araç 3,7 H, basamak "rungs a hand-span apart", en alt
basamak "chest-high", kapak "crouch through"). Reçete: araç 4-5 kare (ön · profil ·
tepe · 3/4 üst · basamak/kapak makro) + 1H şahidi [⑧c].
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_SCOURED_GLASS_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
□ ① PANEL ARİTMETİĞİ  §1 künye 20 = §2 TAM satırları (4+2+4+3+3+3+1 = 20) ✓ yazımda
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var · YETİM 0 · ⏳ paneller §5'te ÇAĞRILMIYOR ✓
□ ③ 120 PX TESTİ      RA p1 (inci beyazı panel / gunmetal eklem ayrımı + gümüş halka + SOL cyan bant + kontürlü sırt) · RC p3 (yüz) · RB p2 (ped ↔ eldiven)
□ ③b AMBLEM HARF 0    RB p1 büyütülür: üç yamada harf/rakam/gerçek logo = 0; altıgende nokta = 3 [D45 · ⑯]
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                      + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146] — RA p4 · RO p1/p2
□ ⑥ D79/D139 SIRT     sırt POZİTİF tarifli: kontürlü paket, dikiş ortada — RA p3 (istisna ③)
□ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1 (RA · RC · RO · RD p1)
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — RA p4 (rim/yaka) · RB p1 (yaylar)
                      · RO p2 (şerit) · RP (ped ↔ eldiven) — önce fiilen koşulur
□ ⑧ DURUM ÇİFTİ       RO p1 ↔ p2 aynı kadraj · aynı ışık · ±%3 · tek fark şerit
□ ⑨ ⑲ KİMLİK YIĞINI   RA 4 · RO 4 · RC 4 · diğerleri 0 (betik FIX verirse gerekçe D167 kapısı)
□ ⑩ ⑳b DEĞİŞİM        S8'in start frame'i RO p1 (ÖNCE) ✓ · S11'e AFTER paneli yüklenmiyor ✓
□ ⑪ ÖLÇEK ŞAHİDİ      RD p1'de 1H (kasklı adam) kadrajda ✓ yazımda
□ ⑫ SEED / SHA KAYDI  hangi panel hangi seed ve özet — §2 tablosuna YAZILDI
□ ⑬ BAYT AYNILIĞI ⚙️  RA kimlik cümlesi ↔ 00_PLAN BLOK A `diff` — İKİ BİLİNÇLİ FARK:
                      ① EXCEPT cümlesi RA'da "no band" cümlesiyle değişik (K0 sayfası;
                      S1-S9 promptu EXCEPT cümlesini taşır) ② livery RA/RC'de TAM (turkuaz
                      yarım daire · gümüş panel · nakış dokusu), BLOK A'da SAYILABİLİR KISA
                      biçim (kılavuz §2: dokunsal bilgi görselde; sahne promptu 4300 tavanı)
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · 11.09.2026: ⛔ 0 BLOCK · ⚠️ 1 FIX = yalnız "D79 bloğu eksik: sırt ünitesi" — bilinçli istisna (FAZ_01 §③, RA p3 pozitif sırt) + uzunluk notu (image bandı "karar bekliyor")
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
✅ Tetikleyici kontrolü işaretlendi (T1 · T2 · T3 · T5)
✅ Envanter · merdiven · eşleme (FAZ 1, S1-S12) yazıldı
✅ Sayfa blokları yazıldı: RA · RO · RB · RC · RD · RF · RP (20 panel)
⏳ RC p4 · RD p4 · RO p3 · RO p4 · RP p2 — F2 / F8 / F12'den önce
⏳ RE — F8'den önce
⬜ Kabul kapısı koşulmadı, seed boş — İMAJ MODELİ künyeye yazılmadı (sahip)
⬜ §5 tablosu F2-F15 için faz faz uzar (her faz dosyasıyla birlikte)
⬜ A/B: kırpım mı, tam sayfa mı — S8'de ilk koşu, sonuç §5'e
```
