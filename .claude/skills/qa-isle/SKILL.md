---
name: qa-isle
description: QA raporu işleme akışı (AGENTS.md Kart C/D/E/E3/F/F2 + ortak kapılar ①-⑪). Bir QA/critique raporu yapıştırıldığında veya "rapor geldi", "kare/devamlılık/ses/hikaye/arka plan/fizik raporu" dendiğinde MUTLAKA kullan. Girdi: film klasörü ve varsa master video yolu.
allowed-tools: Bash(bash:*), Bash(python3:*), Bash(ls:*), Bash(ffprobe:*), Bash(ffmpeg:*), Read, Grep, Glob, Write, Edit
---

# QA raporu işleme — kapı sırası

Kaynak: AGENTS.md §3 "C/D/E/E3/F/F2'NİN ORTAK ADIMLARI" + merceğe özel kart.
Bu skill SIRAYI ve ⛔ satırlarını taşır; ayrıntı AGENTS.md'den okunur.
Çelişkide AGENTS.md kazanır. Skor yazmadan önce ilgili kapı defterleri
film kaydına yazılmış olmalıdır.

## 0. Mercek tespiti
Raporun başlık/kategori yapısından hangi mercek olduğunu belirle:
① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK ·
⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK · ⑬ UYUM ·
⑭ HAREKET · ⑮ YÖN (14.09.2026: hareket mantığı · yön/hedef — kart F10 · F11).
(①-④ zorunlu; ⑤-⑧ ve ⑭-⑮ risk tetikli; ⑨-⑫ KOŞUL tetikli plan sadakati; ⑬ üretim
tetikli — 00_README. `rapor_kontrol.py` merceği İÇERİKTEN tanır (MERCEK_IMZA).
⛔ ⑨-⑫ SPEC'siz koşulmaz, mod V satırı tabloya girmez; ölçüm HAM ZİNCİR
dediyse HİÇBİR mercek koşulmaz [D181 · D184])
Malzeme FRAGMAN ise → kapı ⑧: mercek yalnız ①, satır film tablolarına girmez.

## 1. ⑪ ÖLÇÜM KAPISI — sıraca en önce, master eldeyse

⛔ **⑪.0 ÖNCE KİMLİK [D160].** Dosya adı kimlik değildir; kapak kartı da değil.
Master yolu verilmediyse aynı ada uyan HER dosyayı listele ve ölç — farklı
SÜRE = farklı kurgu. Sonra kurgunun ORTASINDAN tek kare çıkar ve **BAK**:

```
ffmpeg -ss <süre/2> -i "$M" -frames:v 1 kimlik.jpg
```

Karedeki mekân/kostüm/nesne SPEC'in C bloğuna oturmuyorsa ⛔ koşu DURUR.
Hangi dosyanın ölçüldüğü film kaydına ve ham raporun künyesine YAZILIR.

```
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master_yolu>"        # sona "rms" ekleyebilirsin
```

- Betik koşulamadıysa (master yok / ffmpeg yok): "ölçüm yapılamadı" diye kaydet
  ve raporun süre/sahne sayılarını HİÇBİR kapıya sokma.
- SES KANALI: YOK + plan sesli → 🔴 TESLİM KUSURU: parti durur, master yeniden
  ihraç edilir, dört mercek yeniden koşulur [D136].
- Rapor ile ölçüm çelişirse ÖLÇÜM kazanır; o merceğin satırı ŞARTLI olur.
- Ölçüm, film kaydına "§ÖLÇÜM KAPISI" tablosu olarak yazılır.
- ⛔ Betik SONA **TESLİM SINIFI** satırı basar [D181]: LUFS sapması > 3 LU ya da
  kuyrukta ≥1,5 s donma → 🚨 **HAM ZİNCİR**. Filigran ve klip sayısı `⬜ GÖZ`/`⬜ SPEC`
  olarak açık kalır; biri 🔴 ise sınıf zaten HAM ZİNCİR'dir.
  **HAM ZİNCİR çıkarsa MERCEK KOŞULMAZ, rapor OKUNMAZ, satır YAZILMAZ.**
  Sıra: KURGU → ÖLÇÜM → MERCEK.
- Betik KUYRUK/BAŞ KART ŞÜPHESİ (freezedetect) ve `son_kare.jpg` de basar [D70/72 · 9 vaka];
  şüphe varsa kart kesilir ve ⑪ yeniden koşulur — kart S0↔son sahne eş kadraj çiftini öldürür.
- Betik **IŞIK TAKVİMİ İZİ** de basar [D193]: sahne başına YAVG (ort · min · son 2 s);
  `↑` takvim geri sardı · `⟳` klibin içinde geri yandı. Takvim monotonikse her işaret 🔴.
- Betik ayrıca LUFS/true peak (ihraç kilidi −14 / −1,0) ve KÖŞE TESTİ (`kose_SA.png`)
  basar: aynı köşede aynı ikon her örnekte → 🔴 FİLİGRAN, master yeniden ihraç [D150].
- Karanlık filmde kesme dedektörü kördür: ızgarayı silencedetect deliklerinden ve
  kart başından oku (10 s katına oturuyorsa ızgara odur); I-frame'lere bakma.
- Tartışmalı saniyelerin karesini ÇIKAR ve BAK (`select=eq(n,…),tile=3x3`) — kilit
  defterindeki ⬜ AÇIK madde ancak kareyle FİLM SAPTI / RAPOR UYDURDU'ya kapanır.

## 2. SPEC KAPISI — önkoşul [D129]

```
ls <FILM klasörü>/*_QA_SPEC.md
```

⭐ **RUBRİK + SPEC, TEK MESAJDA — SPEC BAŞTA.** `QA_PROMPTLARI/_KAYNAK/` altındaki
rubriği aç, `<FILM>_QA_SPEC.md`'yi rubriğin BAŞINA yapıştır; koşu ancak böyle mod
D'dir [D129]. SPEC yapıştırılmadıysa operatör çıplak rubrik koşmuştur ve rapor T
tablosuna GİRMEZ (THE STILL SWARM'da sekiz mercek böyle mod V koştu).
⭐ 14.09.2026 rubrik diyeti: ①-⑥ 25 KB'ın altında; DİKEY filmde ① KARE'nin SONUNA
`_KAYNAK/1_KARE_DIKEY_EK.md` de yapıştırılır (sıra: SPEC → rubrik → dikey ek). Yatayda
yapıştırılmaz. Kesilen uzun kurallar `QA_PROMPTLARI/ARSIV_CIKTI_KURALLARI.md`'de.

⛔ **FİLME ÖZEL PAKET KALDIRILDI [11.09.2026 · proje sahibi kararı]:**
`QA_PROMPTLARI/FILME_OZEL/` ve `scripts/rubrik_paketle.sh` depodan silindi.
Gerekçe deponun kendi ölçümüdür — D165 08.09'da "ÇALIŞMIYOR" işaretlendi: paket
VARKEN de on iki merceğin on ikisi mod V koştu (OPEN CIRCUIT). Mod D'yi taşıyan
şey paket değil, SPEC'in yapıştırılmasıdır.

⛔ **⑬ UYUM'UN MOD V'Sİ YOKTUR [11.09.2026].** Diğer her mercek videoya bakıp bir
şey söyleyebilir; bu söyleyemez — sahne↔prompt karşılaştırmasının bir tarafı yoksa
karşılaştırma da yoktur. Dört girdi zorunludur: kurgu · sahne promptları (BİREBİR) ·
`<FILM>_QA_SPEC.md` · `sahne_kapisi.sh` çıktısı + üretim defteri satırları.
Önce makine yarısı koşar; 🚨 TESLİM UYUŞMAZLIĞI basarsa hiçbir mercek koşulmaz:
```
bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh <master> 10 <prompt_sayısı>
```
⭐ ⑬'ün çıktısı kesme listesi değil DERS SİPARİŞİDİR: 🅑 (prompt boşluğu) satırları
sonraki filmin kilidine dönüşür. ⛔ Ölçülen filmin promptuna DOKUNULMAZ.

⛔ **⑨-⑫ MOD V'DE GEÇERSİZDİR, TEKRAR DEĞİL [D190].** Plan sadakati merceği
belgesiz koşunca ekrandan bir plan türetir ve türettiği plan ekrana her zaman
uyar: ⑫ makarada olmayan doruğa "peak placement 9/10" verdi. Rapor karantinaya
girer — T9-T12'ye satır yok, 00_INDEX hücresi ❌, hiçbir bulgusu DERS/sipariş
üretmez. Betik bunu kendisi verir. ⭐ 14.09.2026: bulgu **ADAY olabilir** —
`GOZLEM_DEFTERI`'ne `**MOD:** V · ⑨-⑫ (plan uydurma riski)` etiketiyle düşer; ≥ 2
filmde tekrarlarsa ders olur [kontrat §4]. Ders yasağı sürer, aday yasağı kalktı.

⛔ **①.10 GÖZ KAPILARI [D191].** Betik `--film` ile koşunca SPEC'in F bloğunu
⬜ listesi olarak basar. Bunlar filmin kendi kapılarıdır ve hiçbir merceğin
kapsamında değildir; her biri TEK KAREYLE kapanır. Açık ⬜ madde varken parti
kapanmaz.

SPEC VARSA ve raporun ilk satırı `INPUT MODE: D` değilse → koşu TEKRARLANIR:
ham rapor 02'ye düşer, T tablosuna SATIR YAZILMAZ, kesme listesi / REMOVE
reçetesi / yeniden üretim UYGULANMAZ. ŞARTLI diye tabloya almak da yasak.

## 2b. ①.5 RAPOR KONTROL BETİĞİ [D161 · D162] — ⑤'ten ÖNCE, elle değil

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
        <ham raporlar…> --film <film klasörü> [--hook 10 --klip 10] --rapor \
        [--olcum-kesme <n>] [--olcum-sahne <n>]      # ⑪ ölçüldüyse ZORUNLU
```
⭐ **⑪ ölçümü hakemdir.** Ölçüm bayrakları verilmezse kesme yayılımı > 1 partiyi
toptan düşürür [D107]; ölçüm verilince parti ayakta kalır, yalnız sapan mercek
şartlı olur. Ölçüm yoksa bayrağı UYDURMA.
⛔ **①.9 TESLİM KAPISI [D188]** — `--film` verildiğinde betik planın
`## 🎬 SAHNE n` başlıklarını SAYAR ve raporların çoğunluk sahne sayısıyla
karşılaştırır. Fark varsa parti GEÇERSİZ: **merceklerin birbirini doğrulaması
teslimi doğrulamaz**, hepsi aynı makarayı izler ve eksik makara oybirliğiyle
onaylanır. O zaman kesme listesi / REMOVE reçetesi / yeniden üretim UYGULANMAZ;
önce hangi sahnenin makarada olmadığı adıyla yazılır ve soru ÜRETİM masasına
geçer (YERÇEKİMİ F10: plan 12, makara 11, eksik olan filmin son karesiydi).

⛔ **①.11 BÖLÜM KAPISI [13.09.2026 · KILAVUZ_REHBERI §2.6/§2.7]** — film
`yatay_6_dk_filmler/` ya da `yatay_8_dk_filmler/` altındaysa QA birimi BÖLÜMDÜR:
on iki mercek iki yarım mastera AYRI koşulur ve betik **`--bolum 1/2`** /
**`--bolum 2/2`** ile çağrılır. Bayraksız koşu ①.9'u yanlış ateşler (plan 36,
makara 18). Bayrakla ①.9 yalnız `<FILM>_BOLUM_n.md`'yi sayar; uç kategoriler
(baş bölümde final, son bölümde hook, ikisinde bütün-film dörtlüsü) `—` olur.
`--rapor` çıktısı `<FILM>_B<n>_<tarih>_RAPOR_KONTROL.md`, `--t-tablo` satırı
`**<Film>** B<n>` olur. ② sınır çiftini göremez → SPEC B sınır satırı elle
kareyle kapanır. Kesme listesi bölüm raporundan UYGULANMAZ.

⭐ **①.12 DERS DÖNÜŞÜ [14.09.2026 · kontrat §4]** — film kaydı `## 🎯 ÜÇ SATIRLIK
SONUÇ`'tan hemen önce `## 🔁 DERS DÖNÜŞÜ` bölümü taşır: `TEKRAR: D<n> — <bulgu> ·
sayaç +1 → <dosya>` (ya da `TEKRAR: yok`) ve `ADAY: ADAY-<n> — <tek cümle> · MOD: D/V`
(ya da `ADAY: yok — <gerekçe>`). Betik `--film` ile koşunca bölümü arar, yoksa NOT
basar. TEKRAR satırı yazılınca ilgili dersin `**TEKRAR:**` sayacı +1 alır; aday
`GOZLEM_DEFTERI`'ne düşer, ≥ 2 filmde tekrarlayınca ders olur (Kart G).

⭐ **①.13 HÜKÜM + ✂️ KESİK [14.09.2026 · QA çıktı reformu]** — rubrikler artık tally /
toplam / OVERALL İSTEMEZ: model hücre + etiketli timecode + tablonun altında kapalı
listeden tek `VERDICT:` yazar; betik etiketleri sayar, ortalamayı hücrelerden hesaplar,
hükmü `VERDICT_SOZLUK` ile kıyaslar (yok / sözlük dışı → ŞARTLI; frekans sayımına
girmez). Eski raporlarda tally/OVERALL varsa yine kıyaslanır. SCORES SUMMARY'siz /
hücresiz / `MEDIA MISSING` çıktı → `KESİK` (koşu değil; `_KESIK_HAM.md`, yeniden koşulur).
Sağlık: `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --film <FILM>`.

n·Σ·ort · tally · şerit · ⑨ ızgara · ④ harita↔kesme · ② sayaç boşluğu · çoklu
raporda ⑤'in altı satırı (SUSKUNLUK · SÜRE dahil [D205]). **KESİK / GEÇERSİZ / TEKRAR → T tablosuna
satır YAZILMAZ; ŞARTLI → düzeltilmiş ortalama Ⓥ ⚠️ girer.** Betik çıktısı film
kaydına "①.5 BETİK KOŞUSU" olarak yapıştırılır.

## 3. ③ KİMLİK KAPISI (①'den önce koşulur)
Raporun sahne listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir
(bir vuruş + bir sayısal kilit). Ekrandaki yazı çapa DEĞİLDİR.
Eşleşme < 2 → UNATTRIBUTED: ham rapor korunur, SKOR SATIRI YAZILMAZ, ders yazılmaz,
**aday da yazılmaz** (film kimliği belirsiz — 14.09.2026 kontrat §4'ün tek istisnası).

## 4. ④ KURGU KAPISI
Önce sahne-dışı malzemeyi ayıkla (süre ölçüt değildir; kurgu ortasındaysa koşu durur).
Sonra üç satır doğrula: klip sayısı = SCENE COUNT · süre = RUNTIME ±2s ·
sıra = İNSAN ŞERİDİ [D118]. Tutmayan varsa "değil" deyip durma — Δ'yı OKU
(AGENTS ④'teki prosedür: insansız yuva eşleme → fazla/eksik klip → replik ekseni);
koşu ÖN KOŞU olur, film boyu kategoriler sayı taşımaz.

## 5. Çapraz kapılar
- Aynı dosyaya birden çok mercek koşulduysa → ⑤: sayım + replik (`LINES HEARD`)
  + şerit (`PRESENCE STRING`) satırları yan yana yazılır.
- Mod V raporlarında → ⑦ parmak izi kapısı (son iki koşunun künyesi yan yana).
- Plan eldeyse → ⑨ hizalama: ızgara PLANDAN alınır,
  `sahne başlangıcı(n) = hook + (n−1) × klip`.

## 6. Merceğe özel kart
AGENTS.md'de ilgili kartı AÇ ve uygula: C(①) · D(④) · E(②) · E3(③) · F(⑤) ·
F2(⑥) · F3(⑦) · F4(⑧) · F5(⑨) · F6(⑩) · F7(⑪) · F8(⑫).
Kartların ⛔ ön satırları: ① FORMAT kapısı · ② iki yarı + doküman verilmez ·
③ AUDIO STATE + register doğrulaması · ⑤ özne kapısı · ⑥ mod kapısı +
cetvelsiz FAIL düşer · ⑨ kare-önce + kafiye çifti · ⑩ kanal kaydı (kask
kapalı → yüz N/A) + cümle kapısı · ⑪ ortam yasası + planlı sınır PASS ·
⑫ kesme ÖNERMEZ + üç saniye tahmin → 08 yayın tablosu. ⑩ ÖNERME KAPISI her mercekte: bulgu planın logline +
sahne haritası + kilit listesine karşı okunur; düşen bulgunun puanı geri verilir,
toplam yeniden hesaplanır, kalanlar SPEC C-bloğuna göre yeniden sıralanır.
⛔ **⑩ DÜŞÜRDÜKTEN SONRA SINIRI SORAR [D183].** Novum yüzünden düşen her bulgu
için SPEC'in NOVUM bloğundaki `⛔` cümlesi (kuralın nerede BİTTİĞİ) okunur ve
KAREYLE sınanır — `rapor_kontrol.py` ①.7 o cümleyi ekrana basar. Kept Light'ta
düşen "TWO GRAVITIES" hükmünün altında sınanmamış bir SINIR İHLALİ duruyordu.

## 7. Kayıt zinciri — sırası değişmez
1. HAM rapor OLDUĞU GİBİ → `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/<FILM>/<FILM>_<MERCEK>_HAM.md` (film klasörü · kural ④ · 11.09.2026'dan beri klasörlü).
   ⭐ 14.09.2026 — ✂️ **KESİK KOŞU:** çıktıda `SCORES SUMMARY` yoksa / skor hücresi yoksa / `MEDIA MISSING` · `INPUT MODE: MISSING` · `RUN NOT STARTED` varsa bu bir rapor değil, yarım koşudur: `<FILM>_<MERCEK>_KESIK_HAM.md` adıyla kaydedilir (silinmez), tabloya/frekansa/partiye girmez, aynı mercek yeniden koşulur. `rapor_kontrol.py` içerikten tanır (karar `KESİK`, çıkış 2); eski dosyalar yeniden adlandırılmaz.
   Bölüm koşusunda (6/8 dk hattı): `<FILM>_B1_<MERCEK>_HAM.md` · `<FILM>_B2_<MERCEK>_HAM.md`; film kaydı TEK dosya, `## BÖLÜM 1` / `## BÖLÜM 2` başlıkları; 00_INDEX matrisinde `**<FILM>** (B1)` · `(B2)` iki satır.
2. Film kaydı → `.../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/<FILM>.md` (kapı defterleri buraya).
   ⭐ 14.09.2026: kaydın sondan bir önceki bölümü `## 🔁 DERS DÖNÜŞÜ` (TEKRAR · ADAY) — ①.12.
3. ⛔ `rapor_kontrol.py` GEÇERSİZ/TEKRAR dediyse bu adım ATLANIR. Skor satırı DOĞRU tabloya: ① → T1 · ② → T2 ·
   ③ → T3 · ④ → T4 · ⑤ → T5 · ⑥ → T6 · ⑦ → T7 · ⑧ → T8 · ⑨-⑫ → T9-T12 ·
   ⑬ → T13 · ⑭ → T14 · ⑮ → T15 (14.09.2026)
   (⑨-⑫'de mod V satırı YOKTUR; ⑬'ün mod V'si yoktur). Geçerlilik işareti: ✅ / ⚠️ ŞARTLI / 🚨.
   ⭐ ⑭/⑮ raporunun PROMPT ORDERS tablosu adım 5'in ham maddesidir: aynı etiket/desen
   ≥ 2 filmde → ders (kontrat §2b); tek filmde → GOZLEM_DEFTERI ADAY (MOD etiketiyle).
4. `.../FILM_QA_RAPORLARI/00_INDEX.md` sayım + tamlık matrisi.
5. Yeni ders çıktıysa → AGENTS.md Kart G.
6. Commit ATILMAZ — "commit'e hazır" diye raporla.

## Mazeret çürütme

| İçinden geçen düşünce | Gerçek |
|---|---|
| "Rapor çok detaylı, ölçüme gerek yok" | Altı mercek aynı yanlış kesme listesini verdi; komut satırında cevabı duran soru modele sorulmaz [D125]. |
| "SPEC var ama bu mod V koşusunu da işleyeyim" | İşlenir ama tabloya girmez; ŞARTLI diye almak onu yapılmış saymaktır [D129]. |
| "Bulgu çok mantıklı, plana bakmak vakit kaybı" | Dört mercek filmin PLANLI FİNALİNİ kesmeyi önerdi [⑩]. |
| "Skorlar yakın, aynı kabul edilebilir" | 1.5'tan küçük fark GÜRÜLTÜDÜR (kural ⑥); kapılar eşikle koşulur, hisle değil. |
