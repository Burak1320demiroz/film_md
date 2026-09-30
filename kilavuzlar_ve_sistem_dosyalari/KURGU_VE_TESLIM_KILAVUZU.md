# ✂️ KURGU VE TESLİM KILAVUZU — Üretimden Yayına Son Kapı

> **Neden var (21.08.2026):** Deponun ölçülmüş en pahalı hataları promptta
> değil KURGUDA çıktı — yanık başlık kartı 6 vaka · Unbroken City'de doruk
> sahnesi kurguya girmedi · Last Shift'te 27 klibin ~17'si ekranda kaldı ve
> süre "tuttuğu" için kayıp görünmedi. Kuralları beş dosyaya dağılmıştı;
> bu dosya o kuralların **tek operasyonel adresidir**. Ders metinleri
> `DERSLER/07_KURGU_VE_ANLATI.md`'de kalır (D62 · 70 · 72 · 81 · 100 · 101),
> bu dosya onların kontrol listesi hâlidir.
>
> **Ne zaman okunur:** kurguya oturmadan önce ve teslimden önce. QA'dan
> önce gelir — kurgu kapısını geçmeyen filme koşulan QA ÖN KOŞU sayılır
> (`QA_PROMPTLARI/00_README.md` [D109]).

---

# 0. 📖 BİRİM SÖZLÜĞÜ — SAHNE ≠ ÇEKİM ≠ KLİP

> Last Shift'te dört QA merceğinin dördü de "14 = 14" sayıp geçti; ekranda
> 27 klibin ~17'si vardı [D101]. Sebep tanım değil, tanımsızlıktı — üç
> kelime üç ayrı şeydir ve hiçbir belge bunu tek yerde söylemiyordu:

```
SAHNE   (SCENE)    Planın dramaturji birimi. Sahne haritasının satırı.
                   "S7" dendiğinde kastedilen şey.

ÇEKİM   (SHOT /    Kesintisiz TEK kamera kurulumu. Sahne içi kesme
        SEGMENT)   kullanan filmde bir sahne birden çok çekimdir
                   (TEK_CEKIM §5.4: Dawn Front 14 sahne / 26 segment).
                   ASL bu birimle hesaplanır: süre ÷ çekim sayısı.

KLİP    (CLIP)     Üretimden çıkan VİDEO DOSYASI. Hattın sabit uzunluğu
                   vardır (~10 s / 8 s); planın çekimi kaç saniye olursa
                   olsun dosya bu uzunlukta gelir. Kırpma kurgunun işidir.
```

```
SABİT IZGARALI film   (sahne = çekim = klip; depodaki çoğunluk)
                      → üç sayı eşittir, tek satır sayım yeter.
DEĞİŞKEN film         (sahne içi kesme VEYA değişken çekim süresi)
                      → üç sayı üç ayrı şeydir; plan SPEC'i ÜÇ SATIR yazar:
                        SCENE COUNT: __  ·  SHOT COUNT: __  ·  CLIP COUNT: __
                      → eşit sanmak, en kalabalık birimi görmemektir [D101].
ÇOK KLİPLİ SAHNE film 🆕 22.09.2026 (yeni yatay filmler · COK_KLIPLI_SAHNE_KILAVUZU)
                      → sahne 2-6 klip · ÇEKİM = KLİP (klip içi kesme yok)
                      → SCENE COUNT ≠ CLIP COUNT · SHOT COUNT = CLIP COUNT
                      → kurgu kapısı ① KLİP sayar; ①c sahne sayısı PLAN'daki
                        SAHNE PLANI satırının uzunluğudur
```

---

# 1. ⛔ KURGU KAPISI — teslimden önce zorunlu [D70 · D72 · D101]

> Üretim kilitleri kurguyu bağlamaz — prompta yazılan hiçbir yasak, kurgu
> masasında alınan bir kararı engelleyemez. Kapı bu yüzden ayrı koşulur.

```
□ ① KLİP SAYISI  = plan CLIP COUNT        (SCENE COUNT DEĞİL)
□ ①b ÇEKİM SAYISI = plan SHOT COUNT       (sahne ≠ çekim olan filmde)
□ ①c SAHNE SAYISI = plan SCENE COUNT
     → üçü eşitse tek satır yeter; değilse ÜÇÜ DE ölçülür
     🆕 04.09.2026 · TEKNİK KUSURLA DÜŞEN KLİP — eşitlik iki yoldan
       birine bağlanır, üçüncü yol yoktur:
         (a) klip YENİDEN ÜRETİLİR ve sayı korunur, ya da
         (b) plan CLIP COUNT revize edilir ve §2 gerekçe tablosuna
             "teknik kusur · yerine ne kondu" satırı yazılır.
       Gerekçesi yazılmadan düşen klip kapıyı GEÇEMEZ — D100'ün açığı
       (10 klip sessizce düştü, süre tuttu) tam bu boşluktan girmişti.
□ ② TOPLAM SÜRE  = plan RUNTIME ± 2 s
     ⚠️ süre tek başına ALDATIR: Last Shift 174/190 "yaklaşık tuttu",
       10 klip eksikti [D100]. Süre maddesi ①'in yerine geçmez.
□ ③ EKRAN METNİ  = 0.0 s — jenerik, başlık kartı ve KAPAK ÇIKTISI dahil.
     Kapak ayrı dosyadır, klip zincirine KARIŞMAZ (6 vaka: Unbroken City
     2:40 · Banded Deep 3:00 · Last Shift 2:50 ...). Yazılı yasak altı
     kez tutmadı; tek çözüm bu satırın fiilen sayılmasıdır.
□ ④ CENTRAL CHOICE sahnesi ekranda VAR ve seçim ekranda TAMAMLANIYOR
□ ⑤ ASL = süre ÷ çekim sayısı → SPEC'teki hedef bandın İÇİNDE
     ⭐ BANDIN KAYNAĞI: KURGU_RITMI_VE_IHRAC_KILAVUZU.md §1 (22.08.2026).
       SPEC'te `TARGET ASL BAND` + `ASL CURVE` satırları aranır; sabit
       ızgaralı filmde band = klip süresidir ve gerekçe satırı olmalıdır.
□ ⑥ EN KISA ÇEKİM TESTİ: planın en kısa çekimi kurguda o uzunlukta mı?
     (Last Shift: planda 2.0 s, kurguda en kısa 10.0 s — bu tek satır,
      kayıp ritim modunu tek başına yakalar)
□ ⑦ DORUK SAHNESİ kurguda VAR (Unbroken City: S9 doruk kurguya girmedi
     ve üç mercek bunu üretimden SONRA buldu)
□ ⑧ PLAN↔KURGU EŞLEMESİ: her plan sahnesinin karşısına kurgudaki zaman
     kodu yazılır. Kayıp klip ANCAK bu eşleme elle yapılınca görünür —
     ②'deki süre kontrolü onu göstermez.
□ ⑨ SIRA KONTROLÜ [D81 · D118]: kurgudaki klip dizisi plan sırasıyla
     BİREBİR aynı mı? Özellikle SON ÜÇ KLİP elle doğrulanır — bozulan
     blok her vakada final bloğuydu. Hızlı araç: İNSAN ŞERİDİ — planın
     "insan var/yok" dizisi (örn. -111111111111-11111-) kurgudakiyle
     karşılaştırılır; rubrikler PRESENCE STRING çıktısını kendisi verir.
□ ⑩ KURULUM LİSTESİ [D81]: planın her Çehov halkası için KURULUM sahnesi
     kurguda var mı? Ödemesi kurguda olup kurulumu olmayan halka = kapı
     BATTI; eksik sahne eklenmeden teslim edilmez.
```

---

# 2. 💰 KIRPMA BÜTÇESİ [D100] — değişken çekim süreli her film

Hattın klibi sabittir (~10 s). 27 çekimlik bir plan ~270 s ham malzeme
demektir; hedef 190 s ise aradaki ~80 saniyeyi KİMİN, HANGİ klipten
alacağı yazılmazsa **kurgu kırpmaz, KLİP DÜŞÜRÜR** — ve süre yaklaşık
tuttuğu için kayıp görünmez.

```
□ SPEC'e iki satır:   RAW FOOTAGE: __ klip × __ s = __ s
                      TRIM BUDGET: __ s
□ KIRPMA TABLOSU (plan §0.18) — klip başına tek satır:
    | klip | ham | kurguda | nereden kırpılır | BOZULMA KARESİ |
    | S11-Ç1 | 10,0 s | 2,5 s | baştan 1,0 · sondan 6,5 (botlar çıkınca) | 7,4 s |
  Tablosu olmayan değişken süreli plan, SABİT ızgaralı plan sayılır.
  🆕 BOZULMA KARESİ (04.09.2026 · TUR 11) — kırpma noktasının İKİNCİ
    ölçütü. Bugüne kadar "nereden kırpılır" sütununu yalnız yuva mantığı
    dolduruyordu [KURGU_RITMI §1.1]. İkinci ölçüt klibin KENDİ çöküşüdür:
    uzuv erimesi, arka plan kayması, tekrar eden birimin dalgalanması ya
    da ince çizginin titremeye başladığı İLK KARE. O kareden sonrası
    kullanılamaz — yuva "kırpılmaz" dese bile.
    ⛔ BU SÜTUN SABİT IZGARALI FİLMLERDE DE DOLDURULUR. Model çöküşü
      ızgaradan bağımsızdır; kırpma tablosu olmayan film bu satırı
      §1 kapısında (madde ⑥'nın yanında) yazar.
    ⛔ SAYI YAZILMAZ, İZLENİR. TUR 11 raporu bozulmayı "3-4. saniyede
      başlar, sabit planda 7-8'e uzar" diye verdi; hiçbir benchmark
      saniye cinsinden bozulma eşiği yayımlamıyor ve o üç sayının
      kaynağı yok. Bu sütun her klip için ELLE ölçülür; boş bırakılan
      satır "bozulma yok" demektir ve bu bir iddiadır, varsayılan değil.
    ⭐ Sınıf sıralaması (mekanizması doğrulanmış, zamanlaması değil):
      en kırılgan = ince çizgi · yazı · tekrar eden birim (ızgara, çit,
      delik dizisi) → sonra yüz ve el → en dayanıklı = kumaş, toz, duman.
      Gerekçe (sıkıştırma oranları ve kaynak TEK YERDE:
      `KILAVUZ_REHBERI.md` §5④): 3D nedensel VAE kodlamasında yüksek
      frekanslı ince detay kayboluyor.
      ⚠️ Buradaki "dayanıklılık" yalnız YÜKSEK FREKANSLI DETAY KAYBI
        eksenidir. Tozun kendi arızası ayrı eksende yaşıyor
        (D143 toz şelalesi · D39 "swirl" — `KILAVUZ_REHBERI` §7);
        tozlu klip bu satır yüzünden güvenli sayılmaz.
□ 🆕 DÜŞEN HER KLİBİN KARŞISINDA GEREKÇE + HALKA ETİKETİ VAR:
    | düşen klip | gerekçe | halka | yerine ne kondu |
  Beş kesme gerekçesinden (süre/tempo · tekrar · bilgi fazlalığı ·
  teknik kusur · doruk kaybı) bu hatta MEŞRU olan tek tanesi TEKNİK
  KUSURDUR — modeli çöken klip zaten kullanılamaz. Geri kalanı kapıda
  tutulur ve çözüm sahneyi geri koymaktır (aşağıdaki D70/72 satırı).
  Halka etiketi (ara · açıklama · terminal bedel) ve bu ayrımın PLAN
  tarafındaki karşılığı: `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` §6.
  ⚠️ D100'de kurgu 10 klibi hiçbir gerekçe yazmadan düşürdü; bu satır
    o boşluğu kapatır, kapıyı GEVŞETMEZ.
  ⭐ BÜTÇE HANGİ YUVAYA HARCANIR: KURGU_RITMI_VE_IHRAC_KILAVUZU.md §1.1
    (kanca ve çözülme kırpılmaz · oryantasyon ve doruk öncesi kırpılır).
□ 5 s altı çekim planlayan sahne "üretimde değil KURGUDA doğar" etiketi
  taşır; üretim kapısı o sahneyi ham hâliyle onaylar.
□ DÜŞEN KLİBİN BİLGİSİ METNE DÖNÜŞTÜRÜLEMEZ [D70/72]: sahne düştüyse
  çözüm sahneyi geri koymaktır, yanık alt yazı değil (Last Shift 2:50
  kartı tam böyle doğdu).
```

---

# 3. 🎨 GÖRSEL BİRLİK — tek grade + tek gren [TEK_CEKIM §8]

```
□ Tüm klipler TEK grade altında toplanır; üstüne TEK gren katmanı.
  Klip başına ayrı gren YASAK — iki klip birleşince gren yapısı ve renk
  sıcaklığı farkı, perde olsa bile hissedilir.
□ Gizli geçiş noktasında 2-6 karelik çapraz bindirme; daha uzunu "geçiş"
  olarak görünür, daha kısası atlar.
□ Hız ince ayarı en çok %2-4; fazlası hareketi yapaylaştırır.
  (Ayrıntı ve gizli geçiş şartları: TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md
   §6-8. Sahne içi kesmeli filmde kesme/ihlal ayrımı: aynı dosya §5.4.)
```

---

# 4. 🔊 SES SÜREKLİLİĞİ KURGUDA [D83]

```
□ Ortam yatağı klip sınırında ÖLMEZ — kurgu boyunca TEK PARÇA serilir.
  "Müziksiz sahne" SESSİZ sahne değildir; mutlak dijital sıfır = hata
  (Cold Burn'de 20 saniyelik sıfır çıktı — D83'ün kaynağı).
□ Hiçbir kesmede seviye sıçraması duyulmaz; müzik cümle ortasında
  kesilmez, kuyruklar yumuşatılır.
□ Replik altındaki efekt yatağı duck edilir; anlık katman sayısı 3-4'ü
  geçiyorsa önce yatak kısılır.
□ Teslimden önce doruk/temas bölgesi KULAKLA dinlenir.
□ SES_QA yalnız TAM KURGUYA koşulur — ölçtüğü şeylerin çoğu kesmelerin
  ARASINDA yaşar; tek klip koşusu geçersizdir (rubrik kuralı).
  Bulguların çoğu MİKS SEANSI işidir, yeniden üretim değil (Cold Burn:
  5 bulgunun 4'ü miksle kapandı).
  Yazım tarafı: SES_VE_DIYALOG_URETIM_KILAVUZU.md
```

---

# 5. 📦 TESLİM SIRASI — kapıdan yayına

```
1. KURGU KAPISI (§1)  — geçmeden aşağısı başlamaz
2. QA mercekleri      — teknik / senaryo / mantık (+ karakter / ses)
                        (akış ve kartlar: AGENTS.md §3 · C-E3)
3. MÜZİK              — GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §7-19
4. KAPAK              — ayrı dosya, zincire girmez (§1 madde ③)
5. PAKETLEME          — VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
                        ⚠️ spoiler kapısı PAKETLEMEDE DE koşulur [D114]:
                        başlık, açıklama, kurgu — üç yüzeyin üçü de.
                        Fragman "short film" diye satılmaz.
                        + seri/başlık mimarisi: SERI_VE_KANAL_STRATEJI §3
6. İHRAÇ              — KURGU_RITMI_VE_IHRAC_KILAVUZU.md §6   🆕 22.08.2026
                        1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
                        ⛔ sesi DÜŞÜK teslim etmek en pahalı hata:
                        platform yüksek sesi kısar, düşüğü YÜKSELTMEZ
7. YAYIN              — YAYIN_VE_PERFORMANS_KILAVUZU.md       🆕 22.08.2026
                        ⛔ tablo satırı yayından ÖNCE açılır
                        (AGENTS.md kart Y)
```

---

# 6. 📚 KAYNAKLAR

```
DERSLER/07_KURGU_VE_ANLATI.md        D62 · 70 · 72 · 83 · 100 · 101 · 114 tam metin
DERSLER/08_QA_SURECI.md              D81 (sıra+kurulum) · D109 · D118 (insan şeridi)
TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md §5.4 sahne içi kesme · §8 kurguda yapılanlar
SES_VE_DIYALOG_URETIM_KILAVUZU.md    yazım tarafı ses kararları
GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §14 tempo-sahne hizası · §16 seslilik/teslim
QA_PROMPTLARI/00_README.md           kurgu kapısı → QA ön koşul ilişkisi [D109]
KILAVUZ_REHBERI.md §6                akıştaki yeri (adım 5.5) · §7 tuzaklar
```
