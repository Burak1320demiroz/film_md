---
name: cekim-yaz
description: Yeni hat faz 3p pilotu (16.10.2026), faz 5 (referans · başlangıç karesi · video promptları + Flow iş emri) ve faz 7 üretim döngüsü (kare denetimi, kareli animatik, başarısız çekimin yeniden tasarımı) prosedürü. /yeni-film tarafından dosya olarak okunur; sahip /cekim-yaz ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(shasum:*), Bash(ls:*), Bash(mkdir:*), Bash(cp:*)
---

# Çekim yaz — faz 3p · faz 5 · faz 7

Prompt yazım kuralları **goruntu-yonetmeni** ajanının dosyasındadır (`.claude/agents/goruntu-yonetmeni.md`);
burada tekrar edilmez. Burası ana ajanın prosedürüdür.

Faz döngüsü: `yeni-film` §2.

## §F3p — Pilot (16.10.2026 · tek yazım çağrısı + gerçek görüntü)

Amaç: bütün promptlar yazılmadan **filmin kendi riskini** gerçek görüntüyle denemek. Her filmde aynı liste değil
(SMOKE_TEST.md'nin 19 maddesinin 0'ı koşuldu; o dosya artık deney kataloğu: pilot gerekirse oradan madde alır, ör. P17 panel sayfası).
`DURUM.md` → `FAZ 3 · ADIM pilot` · `PILOT <çekimler>` (seçim: hikaye-odasi §F3 adım 7).

1. **goruntu-yonetmeni** (pilot modu, AJAN_GOREVLERI şablonu): `{CIKTI}` = `<FILM>/PROMPTLAR/PILOT.md`, sırasıyla:
   - `## KİMLİK CÜMLELERİ` — §3'teki **her** referans için kadraj parçası başına tek İngilizce cümle: yüz · giysi + işaret
     (sayı, taraf, konum, `the only marking`) · nesne/araç (biçim + ölçü + taraf). Fable tabloyu `FILM.md` §3
     `### KİMLİK CÜMLELERİ`'ne **birebir** kopyalar; bundan sonra her Görsel prompt onu kelime kelime taşır (film_dogrula DERS Y2).
   - `REFERANS PROMPTLARI` — yalnız pilot çekimlerinin referansları (özne başına tek sayfa).
   - pilot çekimlerinin `## Cxx` bölümleri (G dosyası biçimi) + `## FLOW İŞ EMRİ` (çekim başına 2 deneme).
   - `## PİLOT SORUSU` — çekim başına tek satır: bu denemenin cevaplayacağı soru ("iki eldiven aynı halkayı tutunca el kaynaşıyor mu?").
2. **Mekanik:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum cekim pilot` 0 hata. DERS satırı varsa F5 adım 4'teki gibi
   cevaplanır. Bu adımda yazılı eleştiri yok: gerçek görüntü eleştirmenin yerine geçer.
3. **Sahibe iş listesi, sonra dur:** pilot referansları → `ref/<No>.<AD>_v1.png` · kareler → `kare/Cxx.png` · her çekime 2 deneme →
   `ham/Cxx_d1.mp4`, `ham/Cxx_d2.mp4` (model sesi filminde sesli). Montaj yok. Beklerken F4 (ses + müzik) yürür.
4. **Dönüş:** `medya.py al <FILM> --yaz` → `medya.py durum <FILM> --yaz` → her deneme için
   `kareler.py cikar <deneme> --hedef ~/film_medya/<FILM>/analiz/kareler/<deneme>/ --aralik 0.5 --sayfa` → sahibin işareti (NOTLAR İŞARETLEME).
5. **Paralel eleştiri (tek mesaj):**
   - **devamlilik** (kare modu): referans sayfası ↔ başlangıç karesi ↔ deneme kareleri; kimlik cümlesinin tutan ve tutmayan parçası.
   - **teknik-danisman** (pilot modu): her PİLOT SORUSU'nun cevabı (kare adı ve zamanla) + bozulan her denemenin doğduğu yer.
6. **Karar tablosu** `ODA/F3p_pilot_karar.md` (Fable yazar, ajan çıktısı değil — karar):
   `çekim · soru · ne istendi (prompt alıntısı) · ne geldi (kare/zaman) · doğduğu yer · F5'e not · karar`. Karar dört türlü:
   - **GEÇTİ** → F5'te çekimin grubu PILOT.md bölümünü birebir taşır.
   - **PROMPT DEĞİŞİR** → nota göre yeniden yazılır; not aynı kelimeyi taşıyan bütün gruplara gider (kimlik cümlesi, yazı kilidi…).
   - **ÇEKİM DEĞİŞİR** → yonetmen yalnız o çekimi ve aynı riski taşıyanları yeniden tasarlar (1 çağrı, hikaye-odasi §F3).
   - **REFERANS DEĞİŞİR** → referans sayfası yeniden üretilir, sürüm artar.
   Not film içidir, hat kuralı olmaz (AGENTS §1 ④); iki ayrı filmin pilotu aynı şeyi gösterirse sahibe "kural olsun mu" diye sorulur.
7. **Kapı:** `denetci` (Ö + F3p) → Fable. `DURUM.md` → F4 bittiyse `FAZ 5`, değilse `FAZ 4`.
   Sahip "pilot yok" derse: AŞILAN KAPILAR'a yaz; KİMLİK CÜMLELERİ'ni F5'te G01 yazar.
Bütçe: 3-4 çağrı (yazım · devamlilik · teknik-danisman · gerekirse yonetmen); metin tavanına (30) sayılmaz.

## §F5 — Promptlar (tavan 2 tur)

1. **Gruplar (16.10.2026: önce G01, sonra paralel):** `FILM.md` §4'teki `Grup` sütunu (8-12 çekim), grup başına bir **goruntu-yonetmeni**.
   - **Önce G01 tek başına.** Görev: G01 çekimleri + `REFERANS PROMPTLARI` (pilotta üretilmiş referanslar hariç; **özne başına tek sayfa**,
     açılar/yüz/durumlar panel, 10.10.2026) + pilot notu (`ODA/F3p_pilot_karar.md`). Pilot koşulmadıysa G01 ayrıca `## KİMLİK CÜMLELERİ`
     yazar → Fable `FILM.md` §3'e kopyalar. G01'in eleştirisi (adım 2) ve turu kapanır.
   - **Sonra kalan gruplar tek mesajda paralel.** Her görev metni `PROMPTLAR/G01.md`'yi örnek grup olarak verir: kimlik, işaret, yazı
     kilidi, mekân ışığı ve ortak görünüm cümleleri oradan **birebir** kopyalanır.
     Neden: FURNACE'ta paralel yazılan G03 rozet konumunu 4 çekimde yazdı, G04 0/12; rozet kaymalarının 4/4'ü G04'te (ARASTIRMA/16 Y1).
   - Pilot çekimi hangi gruptaysa o grup PILOT.md bölümünü taşır (GEÇTİ → birebir · PROMPT DEĞİŞİR → nota göre).
   - `{CIKTI}` = `<FILM>/PROMPTLAR/<grup>.md`.
   - Zincirli çekimlerin anahtar kareleri (`SAHNELEME.md` §2) o zincirin ilk çekiminin grubunda
     `## Zk.n` bölümleri olarak yazılır (yıldız düzeni). Bir zincir iki gruba bölünmez.
2. **Paralel eleştiri**, grup başına:
   - **devamlilik:** o grubun dosyası + `FILM.md` §3. Kendi dosyasındaki **8 soruyu** çekim çekim cevaplar (DO-CONFIRM: yokluk da bulgudur).
   - **teknik-danisman:** yalnız risk sütunu dolu çekimler.

   Bütün gruplar bittikten sonra **devamlilik**'e bir **gruplar arası** geçiş daha:
   tüm `PROMPTLAR/*.md` + §3. Yalnız kimlik/dünya/ışık cümlelerini karşılaştırır.
3. **Tur:** ÖLÜMCÜL bulgu → ilgili grubun goruntu-yonetmeni'ne revizyon. Ajan dosyayı kendisi günceller.
   ⛔ Revizyon ya da birleştirme geçişinden ÖNCE ana ajan önceki sürümü saklar: `cp <FILM>/PROMPTLAR/<grup>.md <FILM>/ODA/F5_goruntu-yonetmeni_<tur>_<grup>.md` (denetci Ö4 farkı buna bakar; iki filmde unutuldu: WRONG_BURN · PLANET_THIEF).
4. **Mekanik kontrol:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum cekim sahneleme prompt`
   (meta etiket · ≤4.300 karakter · her çekimin promptu · iş emri · **referans anahtarı** `Reference <No>` ↔ `ref/<No>.<AD>` ·
   **10 s vuruş planı** `a-b s`; ikisi sahip kararı 10.10.2026, yalnız §3'ü numaralı yeni filmlerde; eski biçimde ⚠️ ile atlanır).
   **DERS uyarıları (16.10.2026, HİPOTEZ — AGENTS §1b):** `⚠️ DERS Yn` satırları kapı değildir ama cevapsız kalmaz.
   - Revizyon turu açılacaksa satırlar eleştirilerle aynı görev metnine girer (ayrı çağrı yok); yazar düzeltir ya da gerekçe yazar.
   - Tur açılmayacaksa Fable her satıra `ODA/F5_uyari_cevaplari.md`'de karar yazar: `Ders · çekimler · düzeltilecek (tek revizyon
     çağrısı) | gerekçe (ör. "C14 atmosferli liman, 'mist' doğru")`. Denetçi KABUL F5.11'de bakar.
5. **Kapı:** `denetci` (Ö + F5) → Fable. `FILM.md` §4 Durum sütunu → ✍️.
6. **Sahibe iş listesi (faz 7 başlangıcı):** önce Flow proje ayarları (21.10.2026'dan beri yeni filmde model sesi AÇIK; model sesi KAPALI eski filmde Return silent videos AÇIK; **model sesi AÇIK filmde**
   — `FILM.md` §5'te Kaynak = model sesi varsa — Return silent videos **KAPALI**, replik klipten gelir (12.10.2026) · Visible watermarking KAPALI;
   iş emri şablonunun başı), sonra yalnız **referans kareleri**. Hangi prompt, hangi
   dosya adıyla (`~/film_medya/<FILM>/ref/1.KARAKTER_v1.png …` — numara §3'ten; Flow'a yüklerken `EKLE` satırındaki sırayla).
   Model sesi AÇIK filmde ilk video denemesi SMOKE P18'dir (iki replikli çekim + alıcıdan ses çekimi).

## §F7 — Üretim döngüsü (sahip Flow'da üretir; Fable yalnız kare kanıtıyla onaylar)

```
⭐ HER DÖNÜŞTE (16.10.2026): medya.py al <FILM> --yaz (yeni denemeler DENEMELER'e, p:sha8 + girdi) → medya.py durum <FILM> --yaz
                 (gerçek durum ↔ DURUM; adı kurala uymayan dosyalar sahibe). Kayıt olmadan işaretleme ve seçim başlamaz.
7a REFERANS      sahip ref/ karelerini üretir (dosya adı <No>.<AD>_v1.png, §3'teki numarayla) → SHA-256: medya.py al çıktısı (ya da
                 shasum -a 256 <dosya> | cut -c1-12)
                 → devamlilik (kare modu): referanslar birbiriyle ve kimlik tablosuyla tutarlı mı
                 → Fable onaylar → FILM.md §3 Onay ✅ (dosya + SHA). Referans değişirse sürüm artar.
7b KARELER      sahip zincir dışı çekimlerin kare/Cxx.png'lerini ve zincirlerin anahtar karelerini
                 (kare/Zk.n.png — yıldız düzeni: Zk.0 + referanslardan) üretir
                 → devamlilik (kare modu): film boyu kimlik — kare adıyla bulgu
                 → zincir-bekcisi (mod 1, zincir başına bir çağrı): anahtar kareler referansla ve
                   birbiriyle; delta bütçesi → Fable onaylar ya da kareyi yeniden ister.
7c ANİMATİK      kareler timeline.json'a (görsel parça; zincirde Zk.0, Zk.1 … halka süresi kadar) → kurgu.py taslak
                 → kareler.py cikar … --hedef ~/film_medya/<FILM>/izleyici/animatik_<n>/
                 → izleyici (KARE modu) → klip-sec §F7'deki karşılaştırma. Kritik bilgi tutmuyorsa
                   video üretmeden önce çekim listesi revize edilir (hikaye-odasi §F3'e dön).
7d AÇILIŞ + RİSKLİ  önce C01-C03 (12.10.2026, ILK_30_SANIYE_KILAVUZU §6: deneme hakkı en çok onlarda; kare kapısında
                 filigran · logo · yazı · el kaynaşması · yüz bozulması · kimlik kayması aranır, biri varsa açılışta kullanılmaz),
                 sonra risk sütunu dolu çekimler: sahip 2 deneme üretir ve işaretler (klip-sec §F7).
7e KALANLAR      Flow iş emri sırasıyla. Zincir halkaları Frames to Video'da başlangıç + bitiş karesiyle
                 (B) ya da önceki klibin çıkış karesiyle (A′: kareler.py kare <önceki> --t <sn>).
7f DİKİŞ         her zincir için, bütün halkaları ✅ işaretlenince:
                 kareler.py dikis <halka_i> <halka_i+1> --hedef ~/film_medya/<FILM>/analiz/dikis/<Zk>_<i>/
                 kareler.py kuyruk <halka> (donan kuyruk · gizli kesme) + kareler.py cikar <halka> --aralik 1
                 → zincir-bekcisi (mod 2, zincir başına bir çağrı) → her dikiş için:
                   TAMAM · KIRP n kare · YENİDEN ÜRET · A′ / A+ · KESMEYE ÇEVİR (≥45° farklı açıdan yeniden)
                 → kararlar NOTLAR.md'ye; SSIM tek başına karar değildir.
```

**Başarısız çekim döngüsü:** sahibin ❌ işareti + notu (varsa karesi `kareler.py` ile çıkarılır).
1. **teknik-danisman** (faz 7 modu): hatanın doğduğu yer (kare · hareket · seçim · kurgu · anlatım) + yeniden tasarım önerisi.
2. Yer **kare** ise 7b'ye dön. **Hareket** ise **goruntu-yonetmeni** (faz 7 modu) yalnız o çekimi
   yeniden tasarlar: hareketi sadeleştir, çekimi böl, anı kesmeyle atla ya da modu değiştir.
3. **Bütçe kuralı:** iki deneme aynı sebeple bozuksa üçüncüsü aynı promptla istenmez. Yaklaşım
   değişir, 2 deneme daha. Hâlâ olmuyorsa çekim yeniden tasarlanır ya da çekim listesinden çıkar
   (yonetmen'e sor; bilgi başka çekime taşınır).
