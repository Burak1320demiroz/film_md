---
name: yeni-film
description: Yeni film yazma akışı (AGENTS.md Kart A). "Yeni film yazalım", "yeni bir shorts / uzay filmi", "film fikrim var" dendiğinde MUTLAKA kullan. Akış DÖRT soruyla başlar (konu · format · sahne sayısı · referans paketi), sonra hikâye hiçbir dosya okunmadan sohbette yazılır ve BEŞİNCİ soruyla sahibe onaylatılır (14.09.2026); onaysız klasör açılmaz. Yaşayan dersler + çekirdek kılavuzlar + QA raporları okunmadan analiz yazılmaz, analiz bitmeden film yazılmaz.
allowed-tools: AskUserQuestion, Bash(bash:*), Bash(python3:*), Bash(git status:*), Bash(ls:*), Bash(wc:*), Read, Grep, Glob, Write, Edit
---

# Kart A — Yeni film

Sıranın kaynağı AGENTS.md Kart A + `kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`.
Bu skill sırayı dayatır, içeriği kılavuzlardan okutur. Çelişkide AGENTS.md kazanır.

```
⭐ 14.09.2026 · SAHİP KARARI — "YAVAŞ OLMASI TASARIMDIR" (08.09.2026) GERİ ALINDI.
   Ölçüm (THE_LOCKED_PULSE, 13-14.09): 126 dosya / ~42.000 satır zorunlu okuma,
   çizelgede 126/126 satırdan "kilit" çıkmış, "—" SIFIR (= sahte işaretleme);
   25 sahne × 120 satırlık çalışma dosyası; film klasörü 747 KB, üretim 0 kare;
   17/17 kapı imzası tam, hikâye vana tamiri. Uzun akış kapıya göre optimize
   edilmiş film üretti, iyi film değil. Yeni bütçe (TODO_AKIS_VE_DERS_REFORMU):
     OKUMA     yaşayan 40 ders + ≤30 dosyalık manifest (okuma_cizelgesi.sh) —
               "—" yazmak MEŞRU, sıfır "—" sahtedir (prompt_kontrol ㉘)
     SAHNE     ≤8 sahne dosya başına · >8 sahne TABLO + 5 kilit sahne (㉚)
     KİLİT     film başına ≤20 (㉕)     PROMPT  IN FRAME + kelime bandı (① ㉖ ㉗)
     HİKÂYE    hiçbir dosya okunmadan sahibe onaylatılır (adım 0.7 · ㉙)
   DEĞİŞMEYEN: kapı atlanmaz · tur örneklenmez · alt-ajan açılmaz (okunanın
   kilide dönüşmesi bağlam ister). OPEN CIRCUIT dersi (dört dosya hiç açılmadı,
   sekiz bulgu) hâlâ doğru — cevabı "hepsini oku" değil, "doğru 30'u gerçekten oku".
   Yeni kapılar yalnız 14.09'dan sonra açılan klasörlerde (00_HIKAYE_ONAYI.md);
   eski klasörler eski kurallarla.
```

## Akışın haritası

```
0  DURUM        sayaç + git status
0.5 SORULAR     ⭐ DÖRT soru, tek turda — başka soru sorulmaz
0.7 HİKÂYE      ⭐ hikâye sohbette yazılır, sahip ONAYLAR — dosya açılmadan (14.09)
1  KLASÖR       film klasörünü AÇ — analiz oraya yazılacak · onaylı hikâye → 00_HIKAYE_ONAYI
2  OKU          yaşayan 40 ders · çekirdek manifest · QA    → 00_OKUMA_CIZELGESI
3  HASAT        okunanlardan bu filme düşen kilitler ≤20    → 01_QA_DERS_HASADI
4  KONSEPT      ortam/tür · risk · novum kapısı · B5       → 02_KONSEPT_VE_RISK
5  SIRALAMA     X sahnenin sırası · kurulum iskeleti       → 03_SAHNE_SIRALAMASI
6  UYARI        ölçülmüş arızalara bağlı uyarı notları     → 04_UYARI_NOTLARI
7  SAHNE SAHNE  ≤8: dosya başına · >8: TABLO + 5 kilit     → 05_SAHNE_CALISMALARI/
────────────────── analiz bitti, film YAZILMAYA başlanır ──────────────────
8  YAZ          PLAN → BIBLE → PROMPT
9  PAKET        referans paketi (isteğe bağlı) · QA_SPEC
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
| 2 | Hangi format? | `Format` | ① dikey shorts 9:16 ② yatay 12 sahne · 2 dk ③ yatay 24 sahne · 4 dk ④ yatay uzun — 36 sahne · 6 dk / 48 sahne · 8 dk / 7-20 dk faz (④'te hangisi olduğu seçeneğin açıklamasında sorulur; kullanıcı "Diğer"e yazar — AskUserQuestion dört seçenekle sınırlı, 13.09.2026) |
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

**Soru 3 — varsayılanlar formattan gelir** (`KILAVUZ_REHBERI` §2.1-§2.7):
dikey shorts **6** (Hook + 5, §2.1 sabiti) · 12-sahne modül merdiveni
(13.09.2026 sahip beyanı): 2-4 dk **12** · 3-5 dk **24** (2 × 12; 25'li eski
kayıt kartta tarihli) · 6 dk **36** (2 × 18) · 8 dk **48** (2 × 24) · 7-20 dk
faz hattı kartın bandından. 6/8 dk'da yazım 3-5 ile birebir aynıdır; tek fark
QA birimi BÖLÜMDÜR (`yatay_6_dk_filmler/README.md`). ⛔ Bandın DIŞINA çıkılıyorsa
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
⭐ **Tek tarihli istisna (14.09.2026 · sahip kararı): BEŞİNCİ soru — hikâye onayı,
adım 0.7.** Bu bir mülakat sorusu değil, bir KAPIDIR: sahip hikâyeyi en sonda
değil en başta görür. Altıncı soru yoktur.

## 0.7 HİKÂYE — ⭐ dosya okunmadan yazılır, sahip ONAYLAR (14.09.2026)

**Neden:** THE_LOCKED_PULSE 17/17 kapı imzasıyla yazıldı, hikâyesi vana tamiriydi
ve sahip onu en sonda gördü — "neden izlensin" sorusunu soran kapı yoktu. Dersler
ve kılavuzlar hikâyeyi İYİLEŞTİRİR, hikâyeyi ÜRETMEZ; kapıya göre yazılan hikâye
kapıya benzer. Bu yüzden hikâye **hiçbir ders/kılavuz/QA kaydı açılmadan**, dört
sorunun cevabından ve sahibin konusundan yazılır.

**Ne yazılır (sohbete, düz Türkçe — D-numarası · "novum" · kurulum harfi ·
"kilit" YASAK; sahip okur, ajan değil):**

```
LOGLINE        ≤ 25 kelime, tek cümle
NEDEN İZLENİR  izleyiciyi sona kadar tutan TEK soru ("… olacak mı?")
BEDEL          karakter neyi kaybediyor, hangi sahnede (sahne numarasıyla;
               "anlamak / fark etmek" bedel değildir)
SAHNELER       sahne sayısı kadar satır: S0 … Sn, satır başına ≤ 15 kelime,
               olay dili — kim · ne yapıyor · ne değişiyor
```

**Beşinci soru — `AskUserQuestion`, tek soru, üç seçenek:**

```
① ONAY        → adım 1'e geçilir; onaylı metin klasör açılınca
                00_ANALIZ/00_HIKAYE_ONAYI.md'ye işlenir, ONAY satırı tarihlenir
② DEĞİŞTİR    → sahip "Diğer"e notunu yazar; hikâye o nota göre YENİDEN yazılır
                (yama değil), aynı biçimde tekrar sorulur — NOT satırına tur kaydı
③ RED         → yeni hikâye (aynı konu, başka olay); tekrar sorulur
⛔ En çok 3 tur. Üçüncü turda da RED → konu değişir: soru 1'e dönülür
   ("AI karar versin" seçildiyse depoda ikinci en az işlenmiş tema).
⛔ ONAY olmadan klasör AÇILMAZ, hiçbir dosya okunmaz, hiçbir şey yazılmaz.
```

**Sonraki adımlarda:** `03_SAHNE_SIRALAMASI` / PLAN onaylı sahne satırlarından
sapıyorsa `00_HIKAYE_ONAYI.md` **SAPMA** bölümüne yazılır ve yeniden onay alınır
[D74 kalıbı]. Sahne sayısı değişirse `--sahne-guncelle` satırları tamamlar ve
YENİDEN ONAY gerekir. Kapı: `prompt_kontrol.py` ㉙ — ONAY tarihli · satır = sahne
sayısı · SAHNELER'de jargon yok; aksi BLOCK/FIX.

## 1. KLASÖR — analizden ÖNCE açılır, analiz İÇİNE yazılır

Dört sorunun cevabı doğrudan betiğin argümanlarıdır. Sahne sayısı sıralama
sırasında değişirse `--sahne-guncelle` ile tamamlanır. ⭐ Klasör açılınca ilk iş:
adım 0.7'nin onaylı metni `00_ANALIZ/00_HIKAYE_ONAYI.md`'ye işlenir (LOGLINE ·
NEDEN İZLENİR · BEDEL · betiğin damgaladığı `S0 — ⬜` satırları · `ONAY: <tarih> ·
sahip · TUR n/3`). Bu dosya klasörü YENİ REJİME sokar (`prompt_kontrol` ㉕-㉚).

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
     <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
```

Betik: şablonu kopyalar · dosyaları `<FILM>_<ROL>.md` yapar · ≤8 sahnede
sahne çalışma dosyalarını (`S00…Snn`) damgalar, >8 sahnede `00_SAHNE_TABLOSU.md`
üretir (N satır) · okuma çizelgesini üretir · `00_HIKAYE_ONAYI.md`'yi kopyalar
(yeni rejim işareti — 14.09.2026). Kilit sahneler sonra damgalanır:
`film_klasoru_ac.sh --kilit-sahne <FMT> <FILM> S<nn> <HOOK|NOVUM|DORUK|BEDEL|FINAL>`.
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

## 2. OKU — yaşayan dersler · çekirdek kılavuzlar · QA raporları

`00_ANALIZ/00_OKUMA_CIZELGESI.md` betikten üretildi. ⭐ 14.09.2026: liste artık
"hepsi" değil — **yaşayan 40 ders** (`DERSLER/00_YASAYAN_DERSLER.md`) + **çekirdek
manifest** (`FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt`, ≤30 dosya) + QA
raporları. Sayı çizelgenin özet bloğunda, buraya yazılmaz. Kural:

```
⛔ Her satır okununca ⬜ → ✅ yapılır VE "bu filme düşen kilit" sütunu doldurulur.
   Kilit çıkmadıysa "—" yazılır. Boş hücre "okudum" ile "atladım" arasını
   ayırt ettirmez ve bu depoda ayırt edilemeyen şey yapılmamış sayılır.
⭐ "—" MEŞRUDUR: ETİKETİ filme uymayan ders/kılavuz (kasksız filmde [kask])
   "—" ile geçilir, açılmaz. Her satırdan kilit çıkmaz — LOCKED_PULSE'ta
   126/126 satırdan çıkmıştı ve prompt_kontrol ㉘ bunu SAHTE sayar (BLOCK).
⛔ ⬜ kalan satır varken 4. adıma (KONSEPT) geçilmez (㉘ FIX).
```

Turlar ve neden bu sırada:

| tur | ne | neden önce |
|:--:|---|---|
| 1 | `DERSLER/00_YASAYAN_DERSLER.md` — 40 ders, ETİKET'i uyanın metni açılır | arızanın kendisi burada; 128 film dersinin tamamı değil, yaşayanlar (ders emekliliği = listeden çıkış) |
| 2/3 | **manifest** — `02_RISK_KARTLARI` · `03_PLAN_ONCESI` · `06_HIKAYE_HATTI` · `KILAVUZ_REHBERI` (§2.x format · §3 ortam · §4 tür · §5 · §7) · `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 · novum · tema · hook · açı yayı · viral · kurgu ritmi · politika · dört oyunculuk kılavuzu ([iki-insan]/[replik] etiketli olanlar filme uymuyorsa "—") · [kask] donanım + giysi · [replik] ses · [dikey] 05_DIKEY_HAT + mikro drama · [faz] faz mimarisi | kural burada, ders orada. Manifest dışı kılavuz HAVUZDUR: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre ek dosya gösterir; açtığını çizelgeye "havuzdan açıldı" satırıyla eklersin (tek elle-satır istisnası) |
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
- `02_RISK_KARTLARI` ⛔ PLAN'dan önce: **5+ risk çıkıyorsa KİLİT TAVANI ≤ 20** —
  malzeme azaltılmaz (14.09.2026: "malzeme azalt" LOCKED_PULSE'u vana tamirine
  indirdi); tavanı aşan kilit PLAN `UYGULANMAYAN KİLİTLER`e gerekçeyle; `prompt_kontrol` ㉕.
- ⭐ **B5 DÖRTLÜSÜ** — sahne haritasından ÖNCE [03_PLAN_ONCESI B5]:
  `İSTEK` (film başlamasa da var olan bir İŞ — "anlamak/görmek/fark etmek"
  DEĞİL) · `ENGEL` · `BEDEL` (**+ SAHNE no**) · `MUHATAP` (ikinci insan /
  kendi geçmiş kararı / kendi bedeni / ortamın kalıcı değişen parçası).
  ⭐ ASIL KAPI BEDEL'dir; sahne numarası taşımayan bedel boştur.
  İki insan varsa `AYRILIK` (B5b) zorunlu: AYNI FİKİRDE OLMADIKLARI an.
  Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — istek yok · bedel
  yok · muhatap yok [`04_ARASTIRMA_BULGULARI` TUR 4].
  ⛔ "ORTAM hasım değildir" kuralı 02.09'da GERİ ÇEKİLDİ; ortam meşru karşı güçtür.
- ⭐ **KARAKTER KARTI** — B5'ten hemen SONRA [`KARAKTER_KARTI_VE_DAVRANIS` §1 ·
  11.09.2026]: sekiz satır (ROL · İSTEK · BASKI TEPKİSİ · ALIŞKANLIK · SINIR ·
  ZAAF · TEL · İLK↔SON), her satırda SAHNE NUMARASI; başlık rol etiketi, özel
  ad yok. Bible GÖRÜNÜŞÜ, kart DAVRANIŞI kilitler — kart PROMPTA GİRMEZ.
  Gerekçe: Character Bible 43 satırdı, karakter 0 satırdı [`06` §1.4].
  İki insan varsa iki kart ≥3 davranış satırında AYRIŞIR + **İSTEK ÇAPRAZI**
  [`IKI_KISI_VE_AYRILIK` §2-§3]: B, A'dan hiçbir şey istemiyorsa figürandır.

## 5. SIRALAMA → `03_SAHNE_SIRALAMASI.md`

Vuruş tablosu → hook mimarisi → **X sahnenin sırası** → ardışık çift denetimi
→ kurulum iskeleti → replik yerleşimi → metinsiz sayaç → üretim sırası.

- İki bütçe sahne haritasında dağıtılır, üretimden SONRA eklenemez:
  `KARAKTER_VE_DUYGU` §6 + `KURGU_RITMI` §2 örüntü kırıcı (ardışık iki sahne
  aynı ölçek + palet + ses dokusunda olamaz).
- ⭐ Sahne haritasına ÜÇ satır daha [11.09.2026 · TUR 15]: **DAVRANIŞ ŞERİDİ**
  (G/T/D/K/B/R/S — G ≤ %50 · K'dan önce ≥1 D/T · K'dan sonra G gelmez)
  [`KARAKTER_KARTI` §4] · **TEMPO sütunu** (Y/N/H — düz çizgi olamaz, SEÇİM
  çevresinden farklı) [`OYUNCULUK_YAZIM` §4] · **KARAR MİMARİSİ** (reddedilen
  nesne kadrajda ve sonra da orada) [`KARAKTER_KARTI` §3].
  İki insan varsa **AYRILIK KARTI** (B5b'nin genişletilmiş hâli: hücre ·
  gecikme ≥0,7 s · mesafe/yön · kim solda · bedel) + **MESAFE EĞRİSİ** + FAZ
  FARKI (aynı saniyede aynı fiil YOK) [`IKI_KISI_VE_AYRILIK` §2 · §5 · §8].
  Replik varsa replik tablosunun YANINA **DEĞİŞ-TOKUŞ TABLOSU** (hamle · cevap
  kanal×içerik · gecikme · dinleyenin bedeni · DEĞİŞİM — DEĞİŞİM boş replik
  silinir) [`DIYALOG_SAHNESI_VE_MUHATAP` §2-§3].
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
- ⭐ **SAPMA** (14.09.2026): sıra ya da olay `00_HIKAYE_ONAYI.md`'nin sahne
  satırlarından ayrılıyorsa oradaki SAPMA bölümüne yazılır ve sahibe yeniden
  onaylatılır — onaylı hikâye analizle "düzeltilmez", değişirse yeniden onaylanır.

## 6. UYARI NOTLARI → `04_UYARI_NOTLARI.md`

Hasat × sıralama. Her satır ÜÇ şeyi birden taşır: **hangi sahne · hangi
ölçülmüş kayıt · ne yapılacak.** ⛔ Kaynağı olmayan uyarı yazılmaz —
"dikkat edilmeli" bir uyarı değildir.

Şablondaki **tekrar eden arıza tablosunun HER satırı** tek tek cevaplanır
(bugün 16 satır; tablo yeni denetim geldikçe BÜYÜR — sayı belgeye yazılmaz); "bu filmde yok" cevabı da GEREKÇE ister. ⛔ 🔴 satırları
kapanmadan sahne çalışmasına geçilmez.

## 7. SAHNE SAHNE ÇALIŞMA → `05_SAHNE_CALISMALARI/` — ≤8 sahne dosya · >8 sahne TABLO

⭐ **14.09.2026:** sahne sayısı 8'i geçiyorsa sahne başına 120 satırlık dosya
YAZILMAZ (LOCKED_PULSE: 25 × 120 satır, üretim 0 kare). Betik `00_SAHNE_TABLOSU.md`
üretti: sahne başına **bir satır**, 11 sütun (OLAY BAŞ→SON · B5 · KURULUM · OPTİK
eni/px · **IN FRAME** · TAŞIYICI · IŞIK·SES·FİZİK · REPLİK · KİLİT/UYARI · İZLEYİCİ
CÜMLESİ · KAPI) — her hücre tek satır, boş hücre yok ("—"). Yalnız **5 kilit sahne**
tam dosya alır: `film_klasoru_ac.sh --kilit-sahne <FMT> <FILM> S<nn> <ROL>` —
HOOK · NOVUM · DORUK · BEDEL · FINAL, her rol bir kez. `prompt_kontrol` ㉚: satır
sayısı = sahne sayısı, beş rol dosyası var. ≤8 sahnede (dikey) eskisi gibi her
sahne dosya alır. IN FRAME sütunu doğrudan promptun ilk satırı olur (㉖).

Kilit sahne dosyasında (ve ≤8 sahnede her dosyada), filme ve **filmin konusuna** göre:
olay (BAŞTA/SONDA ayrı) · B5 bağı · **optik aritmetiği** (kadraj eni · nesne
sığıyor mu · ana nesne ≥100 px) · kurulum harfi + işaret · devamlılık
taşıyıcıları · ışık/ses/fizik · replik · ⭐VİRAL'in YÜZ+HAREKET satırları ·
o sahneye düşen kilitler ve uyarılar · politika satırı ·
⭐ **İZLEYİCİ CÜMLESİ** ("bu figür ne istiyor" — seems/probably YASAK) +
taşıyan niyet kanalı (≤2) + TASK ONLY mu [`OYUNCULUK_YAZIM` §1 · §3] ·
**kart bağı** (bu sahne kartın hangi satırını taşıyor; boşsa "—")
[`KARAKTER_KARTI` §10] · replikli sahnede **DEĞİŞİM SATIRI** (BAŞ ≠ SON) +
dinleyen tepki planı tipi [`DIYALOG_SAHNESI` §5-§6] ·
⭐ **SON 3 s** (7-10. saniyede beden ne yapıyor — süreç fiiliyle) + **ölü sahne
beş sorusu** (fiil sınıfı · direnç · tek kilit · sınır · çevre saati)
[`SAHNE_DOLULUGU` §1 · §6 · 15.09.2026].

```
⛔ Bir sahnenin ÇALIŞMA DOSYASI (ya da tablo satırı KAPI ✅) kapanmadan o
   sahnenin PROMPTU yazılmaz.
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

- `<FILM>_PLAN.md` — konsept · TEMA + ≥3 sahne indeksi · B5 · **KARAKTER
  KARTI** (Character Bible'ın hemen ÜSTÜNE) · vuruş tablosu · hook · sahne
  haritası (+ DAVRANIŞ ŞERİDİ · TEMPO) · **ÇAPA ÜÇLÜSÜ** (SEÇİM/BEDEL/FİNAL
  önce-sonra beden çifti) · [iki insan] AYRILIK KARTI + mesafe eğrisi ·
  [replik] DEĞİŞ-TOKUŞ tablosu · **KURULUM İSKELETİ satırı** · Bible'lar
  (Character Bible = `ASTRONOT_DONANIM` §9 kimlik + `UZAY_GIYSISI_SINEMATIK_
  TASARIM` §11 görünüş — arketip seçilir, tek blok; 12.09.2026) ·
  sayısal kilitler · politika satırı · **ÜRETİM SIRASI**. ⛔ PLAN'da prompt bulunmaz.
- TIMELINE her satırda ≥1 GÖVDE FİİLİ; iki aşamalı eylem iki satıra ("stops"
  · "then reaches"); hazırlık önce (kask döner → ağırlık kayar → el gider);
  "still/motionless/frozen" tek başına YAZILMAZ; imaj promptu ÇAPA'nın
  BEFORE'unu, sonraki sahnenin imajı AFTER'ı taşır [`OYUNCULUK_YAZIM` §2 · §8 ·
  D179]. ⭐ DOLULUK [`SAHNE_DOLULUGU` §2 · §4 · 15.09.2026]: kilit fiili SÜREÇ
  (erişme ancak dirençle) · imaj bedeni YÜK ALTINDA (eylem başlamış) yazar ·
  TIMELINE ≤3 satır, son satır SÜRDÜRME — "settles / then stops / nothing else
  moves" yazılmaz · sahne başına tek çevre saati + zemin bağı cümlesi. Replikte konuşanın/dinleyenin bedeni + dinleyen klibinde replik metni
  YOK, "lips closed" VAR [`DIYALOG_SAHNESI` §4 · §7]. İki figürde KONUM KİLİDİ
  (sol/sağ üçte bir · never touch) + faz farkı [`IKI_KISI` §2 · §6].
- Sahne başlıkları `## 🎬 SAHNE <n> — BAŞLIK` (kural ②) ve YALNIZ bölüm
  dosyalarında; başlıksız dosya sayımdan düşer.
- Her prompt self-contained (kural ③) — "BIBLE'a bak" atfı yasak. ⭐ 14.09.2026:
  self-contained ≠ Bible'ın tamamı. **İskelet `IMAGE_VIDEO_PROMPT_TEMPLATES.md`
  V3 / `FILM_BOLUM_1.md`:** ① ilk satır `IN FRAME:` — kadrajda olan, sözlükten;
  yalnız o tarif edilir (insert'te yüz YOK · `face` yalnız yüz okunabilir
  kadrajda) [D214 · ㉖] ② üçüncü satır sahnenin TEK kilidi, sayıyla ③ POZİTİF
  gövde bütçesi image 100-250 · video 120-300 kelime, üstü BLOCK (①) ④ NEGATIVE
  = `KILAVUZ_REHBERI` §5.1 çekirdek (image 7 · video 8 cümle) + ≤3 sahneye özel
  (§5.2: D79 vizör/sırt IN FRAME'e göre · diyalog · risk kilidi), üstü FIX (㉗);
  tam liste PLAN Negative Bible'da ⑤ video Bible'ı tekrar etmez — tek satır
  `START FRAME:`; `CONTINUITY LOCKS` paragrafı yazılmaz. Sayılar betikte.
- Bölüm SINIRI da ardışık bir çifttir.

## 9. PAKET — referans · SPEC

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
⭐ ÇAPA ÜÇLÜSÜ bloğu [`OYUNCULUK_YAZIM` §2 · 11.09.2026]: CHOICE / COST /
   FINAL — sahne · saniye · BEFORE · AFTER (aynı kanalda, adlandırılabilir
   fark). ⑩ mod D'nin "ANCHOR BEATS" satırı ve "THE CHOICE ON THE BODY"
   testi buradan okunur. + DAVRANIŞ ŞERİDİ (İNSAN ŞERİDİ'nin altına) ·
   iki insanlıysa C bloğuna İNSAN 2 "kim solda" + iki GAZE STRING ·
   replikliyse DIALOGUE LINES'a "cevaplı/cevapsız + dinleyen kadrajı S_".
   ⬜ FILM_QA_SPEC şablonunda bu blokların yeri HENÜZ YOK — elle blok
   olarak yazılır; şablona işlenmesi kart G/P işi.
⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz.
```

### 9c. QA PAKETİ — ⛔ KALDIRILDI [11.09.2026 · proje sahibi kararı]

```
Bu adım artık YOKTUR ve koşulmaz:
  ⛔ `QA_PROMPTLARI/FILME_OZEL/` klasörü depodan SİLİNDİ
  ⛔ `qa-isle/scripts/rubrik_paketle.sh` betiği SİLİNDİ
Bu hat filme özel QA promptu üretmiyor. QA, `QA_PROMPTLARI/_KAYNAK/`
altındaki ON İKİ çıplak rubrikle koşar.

⭐ MOD D HÂLÂ ZORUNLU, TAŞIYICISI DEĞİŞTİ: operatör rubriği açar ve
  `<FILM>_QA_SPEC.md`'yi AYNI mesajda, rubriğin BAŞINA yapıştırır [D129].
  SPEC yapıştırılmazsa koşu mod V'dir ve T tablolarına GİREMEZ.

⛔ SPEC DOSYASI KALDIRILMADI — §9b hâlâ ZORUNLU: SPEC yoksa film
  "yazımı tamam" sayılmaz.

KARARIN DAYANAĞI DEPONUN KENDİ ÖLÇÜMÜDÜR [D165 · 08.09.2026 "ÇALIŞMIYOR"]:
   THE STILL SWARM  (01.09 · paket YOK · 8 mercek mod V)
   THE SINKING STAKE(02.09 · paket YOK · 8 mercek mod V)
   THE UPWARD FALL  (04.09 · paket VAR · 8 mercek YİNE mod V)
   THE OPEN CIRCUIT (08.09 · paket VAR · ON İKİ merceğin ON İKİSİ mod V)
   → Paketin varlığı mod D'yi hiç garanti etmedi; arıza paketin yokluğunda
     değil, operatörün ne yapıştırdığındaydı. Kaldırma bu ölçümün sonucudur,
     "zaman kazanmak" değil.
```

## 10. KAPI

- `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` 18 maddesi
  uygulanır (maliyeti sıfır, 12'si gerçek filmlerde gerçekten oldu) — A0 HİKÂYE
  ONAYI her şeyden önce: adım 0.7'nin kaydı yerinde mi (㉙ · 14.09.2026).
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
□ HİKÂYE ONAYI ✅ — 00_HIKAYE_ONAYI.md ONAY satırı tarihli, sahne satırı =
  sahne sayısı, SAPMA bölümü boş ya da yeniden onaylı (14.09.2026 · ㉙)
□ 00_ANALIZ'in altı adımı da kapalı (çizelgede ⬜ yok · uyarıların 🔴'ları
  kapalı · her sahnenin çalışma dosyası ✅ / tablo satırı KAPI ✅ + 5 kilit sahne)
□ PLAN · BOLUM_1..n · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC yazılı
□ KARAKTER KARTI + ÇAPA ÜÇLÜSÜ yazılı; iki insanlıysa AYRILIK KARTI;
  replikliyse DEĞİŞ-TOKUŞ tablosu (11.09.2026 · TUR 15)
□ prompt-kontrol klasör modu koştu — ㉓ REPLİK ENVANTERİ (SPEC replik sayısı = promptlardaki
  tırnaklı replik) ve ㉔ SPEC TAMLIK (yedi makine çapası dolu) temiz [D203 · D204 · 13.09.2026]
⚠️ <FILM>_URETIM_DEFTERI.md bu listede DEĞİLDİR: klasörle birlikte BOŞ doğar,
   üretim sırasında dolar (kart B). Yazımı tamam sayılmak için dolu olması
   gerekmez; ⑬ UYUM merceği için gerekir.
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
