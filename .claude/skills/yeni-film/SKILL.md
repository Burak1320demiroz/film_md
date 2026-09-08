---
name: yeni-film
description: Yeni film yazma akışı (AGENTS.md Kart A). "Yeni film yazalım", "yeni bir shorts / uzay filmi", "film fikrim var" dendiğinde MUTLAKA kullan. TÜM dersler + TÜM kılavuzlar + QA raporları okunmadan analiz yazılmaz, analiz bitmeden film yazılmaz. Akış DÖRT soruyla başlar (konu · format · sahne sayısı · referans paketi); başka soru sorulmaz.
allowed-tools: AskUserQuestion, Bash(bash:*), Bash(python3:*), Bash(git status:*), Bash(ls:*), Bash(wc:*), Read, Grep, Glob, Write, Edit
---

# Kart A — Yeni film

Sıranın kaynağı AGENTS.md Kart A + `kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`.
Bu skill sırayı dayatır, içeriği kılavuzlardan okutur. Çelişkide AGENTS.md kazanır.

```
⏳ BU AKIŞ YAVAŞTIR VE YAVAŞ OLMASI TASARIMDIR (08.09.2026 · sahip kararı).
   ~100 dosya · ~42.000 satır zorunlu okuma + 5 film kaydı + sahne başına
   ayrı çalışma dosyası. Tek oturumda bitmeyebilir; bitmemesi normaldir.
   ⛔ "Zaman kazanmak için" hiçbir kapı atlanmaz, hiçbir tur örneklenmez,
     hiçbir dosya "muhtemelen ilgisiz" diye kapatılmaz.
   ⛔ Alt-ajan AÇILMAZ — bu akış tek bağlamda koşar. Okunanın kilide
     dönüşmesi bağlam gerektirir; özet dönen ajan kilidi getirmez.
   Ölçülmüş gerekçe: THE OPEN CIRCUIT hızlı yazıldı, zorunlu okuma listesinin
   DÖRDÜ hiç açılmadı ve 07.09.2026 denetimi sekiz bulgu çıkardı — biri
   filmin üssünü kadraja fiziksel olarak ALAMAYAN bir lens seçimiydi.
```

## Akışın haritası

```
0  DURUM        sayaç + git status
0.5 SORULAR     ⭐ DÖRT soru, tek turda — başka soru sorulmaz
1  KLASÖR       film klasörünü AÇ — analiz oraya yazılacak
2  OKU          TÜM ders · TÜM kılavuz · QA raporları     → 00_OKUMA_CIZELGESI
3  HASAT        okunanlardan bu filme düşen kilitler       → 01_QA_DERS_HASADI
4  KONSEPT      ortam/tür · risk · novum kapısı · B5       → 02_KONSEPT_VE_RISK
5  SIRALAMA     X sahnenin sırası · kurulum iskeleti       → 03_SAHNE_SIRALAMASI
6  UYARI        ölçülmüş arızalara bağlı uyarı notları     → 04_UYARI_NOTLARI
7  SAHNE SAHNE  her sahne için ayrı çalışma dosyası        → 05_SAHNE_CALISMALARI/
────────────────── analiz bitti, film YAZILMAYA başlanır ──────────────────
8  YAZ          PLAN → BIBLE → PROMPT
9  PAKET        referans paketi (isteğe bağlı) · QA_SPEC · QA paketi
10 KAPI         03_PLAN_ONCESI + prompt-kontrol skill'i
11 GÜNCELLE     matris · index · README · sayaç
```

---

## 0. DURUM — ilk 60 saniye

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh     # gerçek durum, elle sayı yok
git status --short                               # temiz mi başlıyorsun
```

Sayacın **🧭 DERS → KAPI** bloğuna bak: son yazılan dersler hangi kapıya
bağlanmış. Bir ders sabah yazılıp aynı gün yazılan filme ulaşmadı
[D157 → THE COLD WELD, 01.09.2026]; kapı görünürlüktür.

## 0.5 SORULAR — ⭐ DÖRT soru, TEK turda, `AskUserQuestion` ile

⛔ **Dördü tek çağrıda sorulur.** Peş peşe tek tek sormak sorgu yorgunluğudur
ve bu skill'in açıkça yasakladığı şeydir. ⛔ Bu dördünden başka soru sorulmaz —
gerisi karttan, kılavuzdan ve okumadan çıkar.

| # | soru | başlık | seçenekler |
|:--:|---|---|---|
| 1 | Filmin konusu ne olsun? | `Konu` | ① **AI karar versin** — sayaç `🎭 TEMA DAĞILIMI` + `KILAVUZ_REHBERI` §8 matrisi okunur, depoda **EN AZ işlenmiş** tema/ortam seçilir ② **Konuyu ben vereceğim** (kullanıcı "Diğer"e doğrudan konuyu yazabilir) |
| 2 | Hangi format? | `Format` | ① dikey shorts 9:16 ② yatay 2-4 dk ③ yatay 3-5 dk ④ yatay 7-20 dk |
| 3 | Kaç sahne? | `Sahne` | ① **formatın kartındaki varsayılan** ② bandın üst ucu ③ ben belirteceğim ("Diğer"e sayı) |
| 4 | Referans paketi yazılsın mı? | `Ref. paketi` | ① **Yazılsın** ② **Yazılmasın** ③ **Analiz karar versin** |

**Soru 1 — "AI karar versin" seçilirse:** konu havadan seçilmez. Sayaç zaten
0. adımda koştu; `🎭 TEMA DAĞILIMI` en az kullanılan temayı, §8 matrisi hangi
ortam kartlarının ve hangi novum tiplerinin tükendiğini söyler. Seçim **depoda
eksik olandan** yapılır ve gerekçesi `02_KONSEPT_VE_RISK.md`'ye yazılır.
⛔ Konu cümlesinde replik/diyalog geçiyorsa o da kaydedilir — replikli film ayrı
bir kapı zinciri açar (`SES_VE_DIYALOG` §1a-§2a + `DIALOGUE_CRITIQUE_PROMPT`).

**Soru 2 — format sorulmak ZORUNDA.** Betiğin birinci argümanı odur ve tek
başına dört şeyi belirler: bölüm sayısı · süre bandı · sahne sayısı bandı ·
hangi ortam/format kartının açılacağı. Konudan türetilemez.

**Soru 3 — varsayılanlar formattan gelir** (`KILAVUZ_REHBERI` §2.1-§2.5):
dikey shorts **6** (Hook + 5, §2.1 sabiti) · yatay 3-5 dk **25** (9 s + 24×10 s
= 4:09) · 2-4 dk ve 7-20 dk kartın bandından. ⛔ Bandın DIŞINA çıkılıyorsa
sahibin açık izni gerekir ve plana gerekçe yazılır [D74] — THE WHITE FLOOD 30
sahneye böyle çıktı, 40 YAZILMADI çünkü 6:39 eder ve başka bir karta geçerdi.

**Soru 4 — üç seçeneğin karşılığı:**
```
① YAZILSIN        <FILM>_REFERANS_PAKETI.md yazılır ve KAPI 0 olur:
                  sayfası ONAYLI olmayan varlığın sahnesi üretilmez [D168].
② YAZILMASIN      dosya SİLİNMEZ, ⬜ BEKLİYOR durur; PLAN'a TEK SATIR
                  gerekçe yazılır [D74 kalıbı] — sessizce atlanmaz.
③ ANALİZ KARAR VERSİN  02_KONSEPT_VE_RISK'te REFERANS_PAKETI_KILAVUZU §1'in
                  ALTI tetikleyicisi tek tek ölçülür (T1 kask/vizör ·
                  T2 biçim kilidi · T3 oran · T4 insan dışı canlı ·
                  T5 tekrar eden olay · T6 dönen varlık) ve sonuç yazılır.
```
⚠️ Karar sahibindir ama kayıt duruyor: T1 bu deponun neredeyse her filminde
doğru, ve D146'nın üç ölçülmüş vakası paketsiz filmlerde biçim kilidinin
metinle TUTULMADIĞINI gösterdi (SKYLIGHT 1 filmde 3 kask · YERÇEKİMİ F2 ·
STANDING WIRE 24 klibin çoğunda kubbe vizör).

**SORULMAYANLAR — ve neden:**
```
FİLM ADI        sorulmaz, TÜRETİLİR. Depo kalıbı: İngilizce 2-3 kelime,
                BUYUK_HARF_ALT_CIZGI (THE_OPEN_CIRCUIT · THE_WHITE_FLOOD).
                Öneri klasör açılırken tek satırla bildirilir; beğenilmezse
                değiştirmek ucuzdur, sormak bir tur pahalıdır.
KLİP SÜRESİ     sorulmaz, ARAÇTAN ÖLÇÜLÜR [D124] — tercih değil, aracın ayarı.
ORTAM · TÜR     sorulmaz, konudan + §3/§4 kartlarından çıkar.
TEMA · NOVUM    sorulmaz, 02_KONSEPT'in kapılarından çıkar.
HOOK · VURUŞ    sorulmaz, 03_SIRALAMA'da kılavuzdan çıkar.
```
⛔ Bu listeye soru EKLEME. Her ek soru kullanıcıyı açık uçlu mülakata çeker;
akışın uzunluğu OKUMADAN gelmeli, sorgudan değil.

## 1. KLASÖR — analizden ÖNCE açılır, analiz İÇİNE yazılır

Dört sorunun cevabı doğrudan betiğin argümanlarıdır. Sahne sayısı sıralama
sırasında değişirse `--sahne-guncelle` ile tamamlanır.

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
     <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
```

Betik: şablonu kopyalar · dosyaları `<FILM>_<ROL>.md` yapar · sahne çalışma
dosyalarını (`S00…Snn`) damgalar · okuma çizelgesini üretir.
⛔ Elle `cp/mv/rm` YAPILMAZ — iskelet tek yerde tanımlı (`KILAVUZ_REHBERI` §2.0)
ve kopyalama adımı da tek yerde: bu betik.

```
KLASÖR:
  <FILM>_PLAN · BOLUM_1..n · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC
  (+ <FILM>_REFERANS_PAKETI — isteğe bağlı, §9)
  00_ANALIZ/  ← 2-7 arası bütün iş buraya, ayrı .md dosyalarına
```

⛔ Format klasörünün köküne .md bırakma — sayaç kökteki her girdiyi BİR FİLM sayar.
⛔ Eski filmler yeniden bölünmez/adlandırılmaz; iskelet YENİ filmler içindir.
⛔ `<FILM>_YAYIN_PAKETI.md` **tamamen İngilizce** (kanal kararı §3.3);
   `⬜ AFTER THE CUT` alanları kurgudan önce doldurulmaz.

## 2. OKU — TÜM dersler, TÜM kılavuzlar, QA raporları

`00_ANALIZ/00_OKUMA_CIZELGESI.md` betikten üretildi ve içinde bugün
**~100 zorunlu dosya / ~42.000 satır** var. Kural tek:

```
⛔ Her satır okununca ⬜ → ✅ yapılır VE "bu filme düşen kilit" sütunu doldurulur.
   Kilit çıkmadıysa "—" yazılır. Boş hücre "okudum" ile "atladım" arasını
   ayırt ettirmez ve bu depoda ayırt edilemeyen şey yapılmamış sayılır.
⛔ ⬜ kalan satır varken 4. adıma (KONSEPT) geçilmez.
```

Turlar ve neden bu sırada:

| tur | ne | neden önce |
|:--:|---|---|
| 1 | `DERSLER/` — hepsi (01-07 film · 08-09 alet · GOZLEM_DEFTERI) | arızanın kendisi burada |
| 2 | `URETIM_ONCESI_ANALIZ/` — hepsi | ⛔ **`05_DIKEY_HAT_TESHISI` dikey filmde ZORUNLU** · `02_RISK_KARTLARI` plandan önce · `06_HIKAYE_HATTI_TESHISI` B5'in kaynağı |
| 3 | Kök kılavuzlar — hepsi + `DIS_FILM_ANALIZI/` | kural burada, ders orada |
| 4 | `FILM_QA_RAPORLARI/` — index · red defteri · T tabloları · kalite tabloları | ölçülmüş sonuç |
| 5 | `01_FILM_RAPORLARI/` — **5 kayıt SEÇİLİR ve seçim gerekçelenir** | ① aynı format ② aynı ortam kartı ③ aynı tema ④ en düşük skor ⑤ en yakın konsept |

⭐ **QA raporları bu turun en pahalı yarısıdır.** Kılavuz ne yapılması
gerektiğini, QA kaydı ne olduğunu söyler. `09_URETIM_RED_DEFTERI.md` deponun
politika/red konusundaki **tek sayacıdır** — hangi sınıf hangi motorda düştü
ve hangi çözüm GERÇEKTEN geçti orada yazıyor.

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; bağlam dolarsa
kaldığı satırdan devam edilir. Çizelge bu yüzden dosyadır, bellek değil.

## 3. HASAT → `01_QA_DERS_HASADI.md`

Çizelgenin kilit sütunu üç tabloya taşınır: **ders kilitleri · QA arızaları ·
red defteri sınıfları.** ⛔ Sıfır satırla 4. adıma geçilmez — 189+ ders ve 52
film kaydının hiçbirini tetiklemeyen konsept yoktur, hasat yapılmamıştır.

⛔ Ders metni kopyalanmaz, **bu filmde ne yapılacağı** yazılır. Kilit prompta
ETİKETSİZ girer — `[LESSON n]` gövdeye yazılmaz [D45].

## 4. KONSEPT VE RİSK → `02_KONSEPT_VE_RISK.md`

- Sahibin talebi **birebir** yazılır. Fizikle çelişiyorsa yeniden tanımlanır ve
  sapma AÇIKÇA kaydedilir [D74] — emsal: OPEN CIRCUIT'in "fırtınalı/patlamalı"ı.
- Format · ortam kartı (§3) · tür (§4.1) · **klip süresi ARAÇTAN ÖLÇÜLÜR** [D124].
- Konsept kapısı ①TEK KARE ②KİNETİK BAĞIMSIZLIK ③BAŞLIK ŞEMASI — üçü ✅ değilse
  konsept REDDEDİLİR, sıralama yazılmaz. ⛔ TEK KARE cümlesi taşıyıcı nesnenin
  ADINI içerir [D157].
- Tema: `TEMA_MUHENDISLIGI` §3 sekizlisi → §5 matrisi → §9. ⛔ TANIM cümlesi,
  TAKAS kalıbı değil [§3c moratoryumu].
- `02_RISK_KARTLARI` ⛔ PLAN'dan önce: **5+ risk çıkıyorsa malzeme azalt** —
  prompt iyileştirmek bu deponun ölçtüğü kadarıyla işe yaramıyor.
- ⭐ **B5 DÖRTLÜSÜ** — sahne haritasından ÖNCE [03_PLAN_ONCESI B5]:
  `İSTEK` (film başlamasa da var olan bir İŞ — "anlamak/görmek/fark etmek"
  DEĞİL) · `ENGEL` · `BEDEL` (**+ SAHNE no**) · `MUHATAP` (ikinci insan /
  kendi geçmiş kararı / kendi bedeni / ortamın kalıcı değişen parçası).
  ⭐ ASIL KAPI BEDEL'dir; sahne numarası taşımayan bedel boştur.
  İki insan varsa `AYRILIK` (B5b) zorunlu: AYNI FİKİRDE OLMADIKLARI an.
  Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — istek yok · bedel
  yok · muhatap yok [`04_ARASTIRMA_BULGULARI` TUR 4].
  ⛔ "ORTAM hasım değildir" kuralı 02.09'da GERİ ÇEKİLDİ; ortam meşru karşı güçtür.

## 5. SIRALAMA → `03_SAHNE_SIRALAMASI.md`

Vuruş tablosu → hook mimarisi → **X sahnenin sırası** → ardışık çift denetimi
→ kurulum iskeleti → replik yerleşimi → metinsiz sayaç → üretim sırası.

- İki bütçe sahne haritasında dağıtılır, üretimden SONRA eklenemez:
  `KARAKTER_VE_DUYGU` §6 + `KURGU_RITMI` §2 örüntü kırıcı (ardışık iki sahne
  aynı ölçek + palet + ses dokusunda olamaz).
- Sahne-kurulum dizisi: `ACI_YAYI` §3 güvenli bant (ardışık çift ≥1 ölçek
  kademesi VE ≥45°) · §4 kurulum sayısı · **açı TİPİ sayısı ≥3**.
- ⭐ **KURULUM İSKELETİ satırı** — sahne sayısı kadar harf (`A A B C B C D E E C D A`).
  12+ sahnede iki sayı: **KÜME ≥2** · **DÖNÜŞ ≥%40**. 6-11 sahne ve dikey muaf.
  ⛔ Aynı harfin kamera metni BİREBİR kopyalanır ve işaret satırını taşır —
  model iskeleti görmez, metni görür [§7 ⑥]. **Bu satır PLAN'a yazılmazsa
  `prompt_kontrol` ⑩④ kapısı hiç KOŞMAZ.**
- Replik varsa `SES_VE_DIYALOG_URETIM` §1a + §2a: kadraj dışı sesin üç
  gerekçesi + bedenleştirmenin (ağzı gösterme) doruğa saklanması. Ekranda
  konuşan ağız İKİ riski birden açar: lip-sync + AI damgası. Replik tablosu
  **İŞLEV sütunu** taşır; işlevsiz replik silinir. ⛔ Saniyeler
  HESAPLANMAZ, HESAPLATILIR [D122].
- ⛔ **ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168]:**
  `DORUK → merkezî seçim → kapanış imajı → S0 → kalanı`
  (referans paketi yazıldıysa ilk halka odur). Üretim her an durabilir
  (red · kota · motor · gün); baştan üretirsen elde hep KURULUM kalır ve
  kurulum kendini savunamaz. **THE SINKING STAKE tam böyle durdu: 25 sahnenin
  14'ü üretildi, eksik 11'i ARDIŞIK ve filmin SONUYDU.**
- ⛔ **İPTAL KAPISI** yazılır: hangi sahne tutmuyorsa film üretilmez.

## 6. UYARI NOTLARI → `04_UYARI_NOTLARI.md`

Hasat × sıralama. Her satır ÜÇ şeyi birden taşır: **hangi sahne · hangi
ölçülmüş kayıt · ne yapılacak.** ⛔ Kaynağı olmayan uyarı yazılmaz —
"dikkat edilmeli" bir uyarı değildir.

Şablondaki **tekrar eden arıza tablosunun HER satırı** tek tek cevaplanır
(bugün 16 satır; tablo yeni denetim geldikçe BÜYÜR — sayı belgeye yazılmaz); "bu filmde yok" cevabı da GEREKÇE ister. ⛔ 🔴 satırları
kapanmadan sahne çalışmasına geçilmez.

## 7. SAHNE SAHNE ÇALIŞMA → `05_SAHNE_CALISMALARI/S00.md … Snn.md`

Filme ve **filmin konusuna** göre, sahne başına bir dosya. Her dosyada:
olay (BAŞTA/SONDA ayrı) · B5 bağı · **optik aritmetiği** (kadraj eni · nesne
sığıyor mu · ana nesne ≥100 px) · kurulum harfi + işaret · devamlılık
taşıyıcıları · ışık/ses/fizik · replik · ⭐VİRAL'in YÜZ+HAREKET satırları ·
o sahneye düşen kilitler ve uyarılar · politika satırı.

```
⛔ Bir sahnenin ÇALIŞMA DOSYASI kapanmadan o sahnenin PROMPTU yazılmaz.
⛔ 00_ANALIZ içinde "## ... SAHNE <n>" başlığı ve 📸/🎥 prompt başlığı
   YAZILMAZ — kapı betiği o desenleri sahne ve prompt sanar.
   (prompt_kontrol'ün ATLA deseni 00_ANALIZ'i atlar; kural yine de geçerli.)
```

⭐ En pahalı üç kalem burada yakalanır, çünkü başka hiçbir yerde
yakalanmıyor: ① **optik aritmetiği** — OPEN CIRCUIT'te beş kurulumun beşi
tutmuyordu, biri 64 m'lik üssü 5,9 m'lik kadraja alıyordu · ② **okunurluk** —
47 m'deki nesne ~60 piksel [D179] · ③ **klip içi durum değişimi** — ölçülmüş
EN ZAYIF eksen (T2V-CompBench 0,0687); ya sınıra taşınır ya ARA DURUM YASAĞI yazılır.

---

## 8. YAZ — PLAN → BIBLE → PROMPT

Analizin çıktısı film dosyalarına taşınır; **yeniden düşünülmez, taşınır.**

- `<FILM>_PLAN.md` — konsept · TEMA + ≥3 sahne indeksi · B5 · vuruş tablosu ·
  hook · sahne haritası · **KURULUM İSKELETİ satırı** · Bible'lar · sayısal
  kilitler · politika satırı · **ÜRETİM SIRASI**. ⛔ PLAN'da prompt bulunmaz.
- Sahne başlıkları `## 🎬 SAHNE <n> — BAŞLIK` (kural ②) ve YALNIZ bölüm
  dosyalarında; başlıksız dosya sayımdan düşer.
- Her prompt self-contained (kural ③) — "BIBLE'a bak" atfı yasak.
- Bölüm SINIRI da ardışık bir çifttir.

## 9. PAKET — referans · SPEC · QA paketi

### 9a. REFERANS PAKETİ — İSTEĞE BAĞLI (08.09.2026 · sahip kararı)

`REFERANS_PAKETI_KILAVUZU.md` §1'in altı tetikleyicisi okunur
(`T1` kask/vizör/basınç giysisi · `T2` biçim kilidi metinle tutulmayan varlık ·
`T3` oranı sözle yazılamayan nesne · `T4` insan dışı canlı · `T5` tekrar eden
insan dışı olay · `T6` tekrar tekrar dönen varlık).

```
⚠️ Paket artık ZORUNLU DEĞİL — yazılmaması filmi "yazımı tamam" olmaktan
   çıkarmaz. Ama tetikleyici doğruyken atlanıyorsa PLAN'a TEK SATIR gerekçe
   yazılır [D74 kalıbı]; sessizce atlanmaz.
⛔ Bu bir hafifletme değil, sahibin maliyeti üstlenmesidir. Kaydı duruyor:
   D146'nın üç ölçülmüş vakası (SKYLIGHT 1 filmde 3 kask · YERÇEKİMİ F2 ·
   STANDING WIRE 24 klibin çoğunda kubbe vizör) ve SINKING STAKE'in QA kaydı
   ("referans paketi HİÇ ÜRETİLMEDİ → çapa yok" + "göğüs paketi S13'te değişiyor").
⛔ Paket YAZILDIYSA kapı sertliğini korur: bir varlığın sayfası ONAYLI
   olmadan ve seed'i yazılmadan o varlığın geçtiği hiçbir sahne üretilmez
   [D168] — üretim sırasının ilk halkası odur.
⛔ Yazılmasa da dosya SİLİNMEZ, `⬜ BEKLİYOR` satırıyla durur.
⚠️ Yazıldıysa: İngilizce prompt `### 📸 IMAGE PROMPT` başlığından sonraki
   İLK çitli blok olmalı; künye araya girerse betik yanlış bloğu ölçer.
```

### 9b. `<FILM>_QA_SPEC.md` — yazım paketinin son parçası

A/B/C/E blokları + TARGET ASL BAND / ASL CURVE satırları (`KURGU_RITMI` §1;
sabit ızgaralı filmde gerekçe satırı ZORUNLU [D74]).

```
⛔ REPLİK ZAMANLARI VE DORUK SAATİ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n)   = hook + (n−1) × klip + promptun TIMELINE ofseti
   doruk başlangıcı = hook + (doruk_sahne − 1) × klip
   Yazılan her kayıt formülle doğrulanır; sapma varsa paket TAM DEĞİLDİR.
⭐ B bloğuna FİNAL VURUŞ KANITI satırı [D141]: tek karede BULUNAN ya da
   BULUNMAYAN, sayılabilir ve adı konabilir bir nesne + saniyesi + kaç tane.
   Kurgu kapısının dördüncü satırı bunu okur.
⭐ E bloğundaki her MAKİNE KAPISI KURU KOŞUYLA DOĞRULANIR [D142]:
     ffmpeg -hide_banner -filters | grep -q " <filtre> " || kapıyı yeniden yaz
   Her kapı üç satır taşır: KOMUT · DOĞRULANDI (<ffmpeg sürümü·tarih>) ·
   İKAME (filtre yoksa hangi ölçüm koşulur). DOĞRULANDI satırı olmayan kapı
   YAZILMAMIŞTIR — bir SPEC'in kamera kapısı kurulu olmayan bir filtreye
   yazılmıştı ve sessizce hiç koşmadı (`vidstabdetect`, iki filmde ölçüldü).
⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz.
```

### 9c. QA PAKETİ — SPEC yazılır yazılmaz, QA anında DEĞİL [D165]

```bash
bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <FORMAT_KLASORU>/<FILM_ADI>
```

Çıktı: `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..12`.
Betik 1 saniye sürer; SPEC değişirse yeniden koşulur, paket ELLE düzenlenmez.

⛔ **Bu klasör yoksa film "yazımı tamam" DEĞİLDİR** (SPEC ile aynı ağırlıkta).
Çıplak rubrik **mod V koşar** ve mod V koşusu T tablolarına GİREMEZ [D129].

```
⛔ DÜRÜST KAYIT — D165 08.09.2026'da "ÇALIŞMIYOR" İŞARETLENDİ (3. vaka).
   THE STILL SWARM (01.09 · paket YOK · 8 mercek mod V)
   THE SINKING STAKE (02.09 · paket YOK · 8 mercek mod V)
   THE UPWARD FALL (04.09 · paket VAR · 8 mercek yine mod V)
   THE OPEN CIRCUIT (08.09 · paket VAR · ON İKİ merceğin ON İKİSİ mod V)
   → Arıza YER DEĞİŞTİRDİ: "paket yok" değil, "paket var ama operatör
     rubriği açıyor". BORÇ AÇIK: paket rubriğin YANINA değil YERİNE
     geçmeli (`QA_PROMPTLARI/_KAYNAK/` çıplak rubrikleri kaldırılır).
   ⭐ Borç kapanana kadar adım YİNE ATILIR — paket olmadan mod D hiç
     mümkün değil — ama paketin varlığı mod D'yi GARANTİ ETMEZ.
     Bu satır "adım gereksiz" diye okunmaz; "adım yeterli değil" der.
```

⭐ Bu adımın bu dosyada durmasının kendi tarihi var: 02.09'da ders AGENTS.md
Kart A'da yazılıydı ama SKILL'de değildi ve atlandı — **ajan AGENTS.md'yi
değil bu skill'i okur.**

## 10. KAPI

- `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` 14 maddesi
  uygulanır (maliyeti sıfır, 11'i gerçek filmlerde gerçekten oldu).
- ⭐ Promptlar bitti, **TEK KARE üretilmedi** → `prompt-kontrol` skill'i koşulur.
  ⛔ Betiğe FİLM KLASÖRÜ verilir, tek bölüm dosyası değil. Çıktıda
  `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırı yoksa kapı koşmamıştır.
  Betik ⑭ NOVUM TAŞIYICI [D157] · ⑮ SIRT POZİTİF [D139] · ⑯ politika sözlüğü ·
  ⑰ B5 HİKÂYE OMURGASI · ⑳ zorlanma kanalı · ㉑ çıplak-deri negatifi de denetler.
- Replik varsa `PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md` (Kart P 2b).

**Bu skill'in bitişi o kapının başlangıcıdır; kapıyı atlayıp üretim önerme.**

## 11. GÜNCELLE + BİTİŞ

- `KILAVUZ_REHBERI` §8 film matrisine satır ekle.
- `FILM_QA_RAPORLARI/00_INDEX.md` tamlık matrisine "0/4" satırı.
- Klasörün README'si varsa film listesine ekle.
- `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → toplam film sayısı 1 arttı mı.
- **Commit ATILMAZ** (yalnız proje sahibi atar) — "commit'e hazır" diye raporla.

---

## "Yazımı tamam" tanımı

```
□ 00_ANALIZ'in altı adımı da kapalı (çizelgede ⬜ yok · uyarıların 🔴'ları
  kapalı · her sahnenin çalışma dosyası ✅)
□ PLAN · BOLUM_1..n · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC yazılı
□ QA_PROMPTLARI/FILME_OZEL/<FILM>/ klasörü ÜRETİLDİ
□ prompt-kontrol klasör modu koştu
⚠️ REFERANS_PAKETI listede DEĞİLDİR (08.09.2026) — yazılmadıysa PLAN'da
   tek satır gerekçe var mı, ona bakılır.
```

## Kaçınılacaklar

- **Sorgu yorgunluğu üretme.** Okuma ve analiz uzundur; *kullanıcıya sorulan*
  kısım kısadır. Format · film adı · konu — gerisi kılavuzdan ve karttan
  çıkar. Varsayım gerekiyorsa en fazla birkaç net soru sor, açık uçlu
  mülakata çekme.
- **Alt-ajan açma.** Bu akış tek bağlamda koşar.
- **Analizi film dosyalarına gömme.** 00_ANALIZ ayrı durur; plan 1.200 satır
  olduğunda kimse geri dönüp bakmıyor [D117'nin kalıbı].
- **Kapıyı "bu filmde gerekmez" diye atlama.** Gerekmediğini yazmak da
  kapının bir parçasıdır.
