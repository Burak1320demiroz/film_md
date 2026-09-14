# ✅ TODO — AKIŞ VE DERS REFORMU (açıldı 14.09.2026)

> **Kalıp:** `TODO_DERS_KILAVUZ_QA_KAPILARI.md` gibi — tarihli, ölçümlü, doğrulama
> komutlu çalışma listesi. Faz bitince kutu işaretlenir; kalıcı bilgi ilgili
> kılavuza/betiğe taşınır; **tüm fazlar bitince bu dosya silinir.**
> **Kural:** buraya sayı yazılan her satır **14.09.2026 kesitidir**; güncel
> sayı `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`.
> **Sahip kararı (14.09.2026):** 12 maddenin hepsi · rubrik diyeti 25 KB SERT, altı
> rubrik · yeni kapılar YALNIZ 14.09'dan sonra açılan klasörlerde (marker:
> `00_ANALIZ/00_HIKAYE_ONAYI.md`). Bu karar iki eski kararı tarihli olarak geri alır:
> 08.09.2026 "yavaş olması tasarımdır" (yeni-film) ve 01.09.2026 kontratının
> "kapısız ders yok / mod V'den film dersi yok" maddeleri.

---

## 🩺 TEŞHİS — ölçüm (THE_LOCKED_PULSE 13.09 + ders defteri)

```
① AKIŞ      yeni-film 126 dosya / ~42.000 satır zorunlu okuma; çizelgede 0 "—"
            (126/126 dosyadan kilit çıkmış = sahte kilit); klasör 747 KB, üretim 0 kare;
            26 film "yazımı tamam / 0 kare". Sahip hikâyeyi en sonda görüyor;
            "neden izlensin" kapısı yok — 17/17 imza, hikâye vana tamiri.
② PROMPT    IMAGE ort. 3.984 karakter / 719 kelime; %57'si her promptta AYNEN tekrar
            (Bible + negatif çekirdek); NEGATIVE %23; 10/10 insert promptu kadrajda
            olmayan yüzü tarif ediyor. Deponun ölçümü: tarif kilidi %0, sayısal %100.
③ DERSLER   205 dersin 90'ı alet dersi (08/09); son 25 dersin 16'sı QA makinesi
            hakkında; 93 ADAY kapısız (94 kayıt, ADAY-6 çift; 75'i 10.09'da dört
            filmden); 0 ders emekli; 00_HIZLI_REFERANS 21.08'de kalmış.
④ RUBRİK    6 rubrik 25 KB tavanın üstünde (① KARE 59 KB · ④ HİKAYE 48 · ③ SES 39 ·
            ② DEVAMLILIK 37 · ⑥ FİZİK 32 · ⑤ ARKA PLAN 29).
DÖNGÜ       QA bulgu → kapı + negatif cümle → prompt/akış uzar → film kapıya göre
            yazılır → QA yine bulgu. İki sorun tek döngü; reform iki ucu birden budar.
```

## 🔢 SABİTLER — tek yerde durur (kural ①)

```
KELIME_BANDI      image (100, 250) · video (120, 300) POZİTİF gövde kelimesi (NEGATIVE hariç — 14.09 FAZ 7 kalibrasyonu); üstü BLOCK, altı NOT   prompt_kontrol.py
TAVAN             4300 karakter (video, Veo) — değişmez                                prompt_kontrol.py
NEGATIF ÇEKİRDEK  8 sabit cümle + ≤3 sahneye özel → NEGATIVE ≤ 11 cümle              prompt_kontrol.py + KILAVUZ §5
KILIT_TAVANI      20 ders kilidi / film                                               prompt_kontrol.py
KILIT_SAHNE       5 rol: HOOK · NOVUM · DORUK · BEDEL · FINAL (≤8 sahnede hepsi)     film_klasoru_ac.sh
YASAYAN_TAVAN     40 film dersi                                                       sayac.sh
rubrik tavanı     25 KB                                                               sayac.sh
çizelge sahtelik  ✅ ≥ 15 ve "—" = 0 → BLOCK; "—" > %80 → FIX                         prompt_kontrol.py
ders terfi eşiği  ≥ 2 farklı film                                                     00_DERS_YAZIM_KONTRATI.md
rejim marker      00_ANALIZ/00_HIKAYE_ONAYI.md var → yeni rejim; yok → eski kapılar  prompt_kontrol.py rejim()
```

---

## ✅ FAZ 0 — İSKELE + SAYIM AYRIMI (2.4)

- [x] Bu dosya açıldı · `TODO_DERS_KILAVUZ_QA_KAPILARI.md` FAZ 4/5'e "taşındı" notu (14.09.2026)
- [x] `sayac.sh` 📚: film dersi (01-07) · alet dersi (08-09) ayrı sayım (+ çift numara notu)
- [x] Doğrulama: `sayac.sh` → benzersiz 205 aynı · film 117 · alet 90 (60/61/62 iki grupta)

## ✅ FAZ 1 — DERS KONTRATI (2.1)

- [x] `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b FİLM DERSİ ŞABLONU: `**FREKANS:**` (≥2 film) +
      `**DEĞİŞEN SATIR:**` (tek satır) + KAPI (LİSTE yeter) + TEKRAR — başlığın hemen altında
- [x] §3 emeklilik = YAŞAYAN listesinden çıkış · §4 mod V bulgusu → ADAY (MOD etiketi), ≥2 filmde
      ders; UNATTRIBUTED → ne ders ne aday · §6 şablon
- [x] `AGENTS.md` Kart G adım 0/1a (konum tek gelenek) · adım 5 (rubriğe yalnız ölçülebilir tek
      satır; 25 KB aşılmaz) · "yaşayan listeye girer, biri çıkar"
- [x] `.claude/skills/qa-isle/SKILL.md` L90-94 (mod V ⑨-⑫ → ADAY üretir) · L141 aynen
- [x] `sayac.sh` 🧭: FREKANS/DEĞİŞEN SATIR taşıyan film dersi sayısı
- [x] Doğrulama: `sayac.sh` 🧭 yeni satırı basıyor · kontrat §2b/§4 tarihli

## ✅ FAZ 2 — ADAY DEFTERİNİ BOŞALT → YENİ DERSLER (2.3)

- [x] `GOZLEM_DEFTERI.md` yapı: ADAY-6 çifti → 6a/6b · ADAY-61 ayraç · ADAY-30 "kesik kayıt"
- [x] ~11 yeni film dersi D206+ (K1 EFOR/BEDEL · K2 YORGUNLUK SIFIRLAMA · K5 ÇEVRE MORPH ·
      K6 KOSTÜM/KİMLİK · K7 KAFİYE+PUSH-IN · K8 HOOK/KART · K9 TEMPO PLATOSU · K11 ELİPS ·
      K12 KADRAJ DIŞI TARİF · K13a METİN/FİLİGRAN · K13b SES MİKS) yeni şablonla
- [x] Mevcut derse FREKANS + DEĞİŞEN SATIR + TEKRAR: K3 → D202 · K4 → D193 · K10 → D200 · K14 → D151
- [x] Terfi eden ADAY başlığı `## ✅ ADAY-n` + `**DURUM:** → D2xx` · K15 (süreç) kalır
- [x] `03_FIZIK_VE_HAREKET.md` D192 içine giren D198/D200 düzeltmesi + KAPI/TEKRAR satırları
- [x] `LESSONS_LEARNED.md` DERS DİZİNİ satırları
- [x] Doğrulama: `sayac.sh` ders 216 · boşluk yok · `uniq -d` yalnız 60 61 62 · açık ADAY 7 (84 terfi + 7/93 kapalı)

## ✅ FAZ 3 — YAŞAYAN DERS LİSTESİ (2.5)

- [x] `DERSLER/00_YASAYAN_DERSLER.md` ≤ 40 satır (D · başlık · ETİKET · DEĞİŞEN SATIR · dosya) +
      GİRİŞ/ÇIKIŞ DEFTERİ + seçim kuralı (① yeni dersler ② TEKRAR ≥1 ③ KAPI'lı ④ en yeni)
- [x] `sayac.sh` 🧭: YASAYAN n/40 (>40 ⛔) · her D var mı · `00_HIZLI_REFERANS` arşiv notu
- [x] Doğrulama: sayaç 40/40 ✅ · her D çözülüyor

## ✅ FAZ 4 — FREKANS BETİĞİ (2.2) + QA'NIN İKİ SATIRI (2.7)

- [x] `RAPOR_KONTROL/ders_frekans.py` (`--ozet` / `--tam` · mod D/V ayrı · VERDICT ve düşük
      kategori × farklı film · KUME_SOZLUK → D numarası) — dosya yazmaz
- [x] `sayac.sh` 🔁 BULGU FREKANSI bloğu
- [x] `qa-isle/SKILL.md` kayıt zinciri: film kaydında `## 🔁 DERS DÖNÜŞÜ` (TEKRAR · ADAY) —
      ÜÇ SATIRLIK SONUÇ'tan önce · `AGENTS.md` ortak adım ①.12
- [x] `rapor_kontrol.py --film`: 01 kaydında bölüm yoksa NOT · `sayac.sh` sayımı
- [x] Doğrulama: `--ozet` bilinen sayılarla tutuyor (NOBODY PAYS 13 · TWO GRAVITIES 12) ·
      `rapor_kontrol.py --film yatay_4_dk_filmler/THE_HARD_DOCK` eski karar aynı + yeni NOT

## ✅ FAZ 5 — RUBRİK DİYETİ (2.6) — 6/6 ≤ 25 KB, SERT

> ⏸️ 14.09.2026 sahip: "faz 5 başlamadan bir ara verelim". Yapılan: altı rubriğin diyet-öncesi
> tam kopyası `ARSIV_RUBRIK_DIYETI/<n>_..._DIYET_ONCESI_2026-09-14.md`; ① KARE'nin sıkıştırılmış
> TASLAĞI `ARSIV_RUBRIK_DIYETI/1_KARE_DIYET_TASLAGI_2026-09-14.md` (≈ 24 KB, dikey ek dosyasına
> atıf yapıyor — ek henüz yazılmadı). `_KAYNAK/` altı rubrik DEĞİŞMEDİ (① geri yüklendi).
> Devam: taslağı `_KAYNAK/`'a al + `1_KARE_DIKEY_EK.md` yaz + ②-⑥.

- [x] `QA_PROMPTLARI/ARSIV_CIKTI_KURALLARI.md` (ortak kalıp, tek kopya) ·
      `QA_PROMPTLARI/ARSIV_RUBRIK_DIYETI/<n>_<AD>_DIYET_ONCESI_2026-09-14.md` (altı rubriğin diyet-öncesi TAM
      kopyası — kesilen her satır orada; ayrı _KESILEN dosyası yazılmadı, kopya yeterli)
- [x] DONDURULAN: kategori adları/sırası · SCORES SUMMARY tablosu · başlık alanları · tracking
      row · `MERCEK_IMZA` ifadeleri · `BOLUM_SONU` başlıkları · PREMISE REGISTER
- [x] ① 59 → 25 KB (+ `1_KARE_DIKEY_EK.md`) · ④ 48 → 24 · ③ 39 → 19 · ② 37 → 19 · ⑥ 32 → 19 · ⑤ 29 → 16 (ölçüldü 14.09)
- [x] `QA_PROMPTLARI/00_README.md` DEĞİŞİKLİK KAYDI · `CALISTIRMA_KAYITLARI.md` rubrik bölümleri ·
      qa-isle dikey ek satırı
- [x] Doğrulama: `sayac.sh` rubrik hacmi 6/6 ≤ 25 KB ⚠️ yok · `rapor_kontrol.py` 13/13 mercek tanınıyor

## ✅ FAZ 6 — KİLİT TAVANI (1.5)

- [x] `02_RISK_KARTLARI.md` L552-569 + 7 kopya: "5+ risk → malzeme azalt" → "kilit tavanı ≤ 20;
      malzeme azaltılmaz; dışarıda kalan kilit PLAN'a gerekçeyle" (KART 12 istisnası kalır)
- [x] `FILM_PLAN.md` + `01_QA_DERS_HASADI.md`: ≤ 20 satır + `### ⛔ UYGULANMAYAN KİLİTLER`
- [x] `prompt_kontrol.py` ㉕ KİLİT TAVANI (`bolum_al` yardımcısı; yeni rejim)
- [x] Doğrulama: LOCKED_PULSE eski rejim çıktısı aynı (yalnız "rejim: eski" satırı eklendi) · scratch yeni-rejim kopyası: ㉕ "39 ders kilidi (37 D + 2), tavan 20" → FIX
- [x] ⏸️ 14.09.2026 sahip: "faz 6 bitince ara verelim" — durdu. NOT: ㉖-㉚ + kelime bandı + rejim() KODU da aynı yamada
      prompt_kontrol.py'ye girdi ve sınandı (㉖ yüz BLOCK · ㉘ çizelge sahte BLOCK · ㉙ ONAY ⬜ BLOCK · ㉚ tablo/rol FIX);
      yeni rejim klasörü olmadığı için depoda ETKİSİZ. FAZ 7-9'un kalan işi belge/şablon/betik tarafıdır.

## ✅ FAZ 7 — PROMPT BÜTÇESİ (1.3)

- [x] `prompt_kontrol.py`: `rejim()` · ① kelime bandı (yeni rejim) · ㉖ IN FRAME (+ ⑮ koşullu) ·
      ㉗ negatif ≤ 11 cümle · klasör modunda per-prompt ihlaller DOSYA düzeyi toplu bulgu (14.09, FAZ 6 yamasıyla)
- [x] `KILAVUZ_REHBERI.md` §5 → §5.1 ÇEKİRDEK 8 cümle (video 8 · image 7; 886 karakter, eski 1.650) ·
      §5.2 sahneye özel ≤3 (D79 vizör/sırt IN FRAME'e göre · diyalog · risk) · §5.3 tam liste PLAN'a ·
      §6 adım 3 · §7 kelime bandı + "tek kaynak prompt_kontrol.py" · TUR 11 kapanış notu (①② kapandı, ③④ açık)
- [x] `IMAGE_VIDEO_PROMPT_TEMPLATES.md` V3 bölümü (IN FRAME · üçüncü satır tek kilit · START FRAME) + S0
      doldurulmuş örnek; V2 "eski rejim" etiketi · `FILM_BOLUM_1/2.md` iskelet · `FILM_PLAN.md` Bible notu +
      Negative Bible = havuz · `AGENTS.md` kural ③ · `FAZ_DOSYASI_SABLONU` · `FILM_REFERANS_PAKETI` (muaf notu) ·
      `PROMPT_KONTROL/00_README` iki rejim notu
- [x] `yeni-film/SKILL.md` adım 8 · `prompt-kontrol/SKILL.md` §3 (yeni rejim bulgu → çözüm satırları)
- [x] `prompt_kontrol.py` iki kalibrasyon (14.09): ① kelime bandı **POZİTİF gövdeye** (NEGATIVE öncesi) uygulanır —
      8 cümlelik çekirdek 139 kelime, toplam bant içinde sayılsaydı sahneye 100 kelime kalırdı; NEGATIVE'in kendi
      tavanı ㉗, toplamın tavanı TAVAN · ㉗ `Output:` satırını saymaz. ⚠️ sahip vetosuna açık (tek sabit).
- [x] Doğrulama: LOCKED_PULSE (eski rejim) çıktı FAZ 6 ile BİREBİR aynı · scratch yeni-rejim kopyası:
      ① 43 prompt bütçe üstü BLOCK (image 486-628 · video 373-459 kelime pozitif gövde) + ㉖ 50 + ㉗ 50 (14-22 cümle) ·
      S0 çifti V3 iskeletine çekildi → IMAGE 4.382 → 2.392 karakter (247 kelime) · VIDEO 3.845 → 2.477; çift için
      0 bulgu, sayaçlar 42/48/48'e düştü. Gözlem: 24mm WS kurulum sahnesi sıkı yazımla 250-270 kelimeye geliyor —
      ilk yeni-rejim filmde bant kalibre edilir (KELIME_BANDI tek yerde).

## ✅ FAZ 8 — SAHNE TABLOSU (1.4) + OKUMA LİSTESİ (1.2)

- [x] `00_SAHNE_TABLOSU.md` şablonu (11 sütun, satır başına sahne; IN FRAME sütunu promptun ilk satırı) ·
      `film_klasoru_ac.sh`: >8 sahne → tablo N satır, S dosyası yok · `--kilit-sahne <FMT> <FILM> S<nn> <ROL>`
      (rol ∈ 5, her rol bir kez, başlığa rol yazılır) · `--sahne-guncelle` tabloya eksik satır ekler ·
      `--analiz-ekle` 00_HIKAYE_ONAYI/00_SAHNE_TABLOSU/manifest KOPYALAMAZ (eski film eski rejim) ·
      ana kopya manifesti klasöre bırakmaz · özet: ÇALIŞMA/REJİM satırları + SIRA'ya 00_HIKAYE_ONAYI
      (şablon dosyası FAZ 9'da gelir; betik "varsa kopyalar")
- [x] `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` — 24 satır: 20 her filmde + [dikey] 2 + [faz] 2;
      [kask]/[replik]/[iki-insan]/[referans] görünür etiket · `okuma_cizelgesi.sh` TUR 1 = yaşayan liste
      (40 satır, ETİKET sütunu) · TUR 2/3 = manifest ([dikey]/[faz] yoldan süzülür) · özet YAŞAYAN/MANİFEST
      satırları · "—" meşru notu. ⚠️ ölçüm: yatay film için 20 dosya / ~10.500 satır (KILAVUZ_REHBERI 2.256
      satırın ~1.200'ü okunur; hedef 10.000'in kıyısında) — sahip vetosuna açık liste
- [x] `prompt_kontrol.py` ㉘ çizelge sahtelik · ㉚ sahne tablosu (14.09, FAZ 6 yamasıyla)
- [x] `yeni-film/SKILL.md` "yavaş tasarım" bloğu → tarihli geri alma + bütçe tablosu · harita 0.7/2/3/7 ·
      adım 1 betik açıklaması · adım 2 OKU turları · adım 7 tablo/kilit sahne · `AGENTS.md` Kart A aynası
      (blok · KLASÖR · adım 0 · adım 5) · `00_ANALIZ_README.md` (0.7 satırı, 0/1/3/5 güncel) ·
      `00_SABLON_README.md` · şablon `00_OKUMA_CIZELGESI.md` yer tutucu metni · `KILAVUZ_REHBERI` §2.0 iskelet
- [x] Doğrulama: `film_klasoru_ac.sh yatay_6_dk_filmler ZZ_TEST 36` → tablo 36 satır ✅ · çizelge 40 ders +
      20 manifest ✅ · `--kilit-sahne … S20 DORUK` → `S20_DORUK.md` (120 satır, başlık "KİLİT SAHNE · DORUK") ·
      ikinci DORUK reddedildi · `38 --sahne-guncelle` → +2 satır · scratch yeni-rejim kopyasında ㉘: hepsi ✅ +
      "—"=0 → BLOCK · 7 ⬜ → FIX · 30 "—" → sessiz; ㉚: 24 satır/25 sahne FIX + eksik BEDEL FIX · 25 + 5 rol → sessiz ·
      test klasörü silindi (test artefaktı, film değil)

## ✅ FAZ 9 — HİKÂYE ONAYI (1.1)

- [x] `FILM_KLASOR_SABLONU/00_ANALIZ/00_HIKAYE_ONAYI.md` şablonu — LOGLINE ≤25 · NEDEN İZLENİR · BEDEL (sahne no) ·
      `## SAHNELER` (`<SAHNE_SATIRLARI>` → betik `S0 — ⬜` … damgalar) · `ONAY: ⬜ <gg.aa.yyyy> · sahip · TUR ⬜/3` +
      NOT · SAPMA. Jargon yasağı yalnız SAHNELER bölümünde ölçülür (㉙ `bolum_al`); başlık notu serbest.
- [x] `film_klasoru_ac.sh`: yeni klasörde `<SAHNE_SATIRLARI>` N satırla damgalanır (REJİM satırı "YENİ" olur) ·
      `--sahne-guncelle` eksik S satırlarını son S satırının altına ekler + "YENİDEN ONAY" uyarısı ·
      `--analiz-ekle` dosyayı kopyalamaz (FAZ 8)
- [x] `yeni-film/SKILL.md`: frontmatter açıklaması · "⛔ soru ekleme" yasağına tarihli tek istisna · yeni
      **0.7 HİKÂYE** bölümü (neden · ne yazılır · beşinci soru ① ONAY ② DEĞİŞTİR ③ RED · en çok 3 tur · üçüncü
      RED → konu değişir · onaysız klasör açılmaz) · adım 1 (onaylı metin dosyaya) · adım 5 SAPMA · "yazımı
      tamam" ilk kutu `HİKÂYE ONAYI ✅` · adım 10 18 madde
- [x] `AGENTS.md` Kart A: SORULAR'a istisna satırı + yeni `HİKÂYE — 0.7` bloğu · §1 harita ve KONTROL ET 18 madde
- [x] `03_PLAN_ONCESI_KONTROL_LISTESI.md`: başlık geçmişi (17 → 18) · **A0 — HİKÂYE ONAYI VAR MI** (A1'den önce, 5 kutu +
      gerekçe) · TEK SAYFALIK ÖZET A0 satırı · İMZA 18 · KAYNAK tablosu A0 satırı
- [x] `00_ANALIZ_README.md` 0.7 satırı (FAZ 8'de girdi) · `02_KONSEPT_VE_RISK.md` §0 ⑤ HİKÂYE ONAYI (kapılar onaylı
      hikâyeyi sessizce bozamaz; ders dili buraya, onay dosyasına değil) · `KILAVUZ_REHBERI` §2.0 iskelet (FAZ 8'de girdi)
- [x] `prompt_kontrol.py` ㉙ (14.09, FAZ 6 yamasıyla) HİKÂYE ONAYI
- [x] Doğrulama: `film_klasoru_ac.sh yatay_4_dk_filmler ZZ_TEST 24` → 24 `S — ⬜` satırı, REJİM: YENİ; `26 --sahne-guncelle`
      → +2 satır + uyarı · scratch 25 sahnelik kopyada ㉙: şablon hâli → BLOCK ×2 (ONAY ⬜ · 26 ≠ 25) · tarihli + 25
      satır → sessiz · "novum" → FIX · test klasörü silindi

## ✅ FAZ 10 — BELGELER + DOĞRULAMA + BELLEK

- [x] `AGENTS.md` §1 harita (00_YASAYAN · kontrat · HIZLI_REFERANS havuz · sayac/film_klasoru_ac/okuma_cizelgesi ·
      00_ANALIZ yeni dosyalar · ders_frekans · ARSIV_RUBRIK_DIYETI · ARSIV_CIKTI_KURALLARI · 1_KARE_DIKEY_EK) ·
      §6 reform kaydı satırı (açık kalanlar) · §7 doğrulama bloğu (`ders_frekans.py --ozet` · rejim satırı) ·
      §8 DÖRDÜNCÜ KARAR: BÜTÇE · `YAPI_GRAFI.md` (iki rejim · borç 3 · kılavuz haritası düğümleri · RAPOR_KONTROL ·
      BETİKLER) · `KILAVUZ_REHBERI` §1 "havuz" notu + [manifest] etiketleri · §6 2.5 (18 madde, A0) ·
      `RAPOR_KONTROL/00_README` (DERS DÖNÜŞÜ NOT + ders_frekans bölümü) · PROMPT_KONTROL/00_README (FAZ 7'de)
- [x] Tam doğrulama (14.09 15:34): `sayac.sh` → ders 216 (film 128 · alet 90) · film 105 · YAŞAYAN 40/40 ✅ ·
      FREKANS/DEĞİŞEN 14 · rubrik 12/12 ≤ 25 KB · 🔁 blok basıyor · `prompt_kontrol.py` eski rejim ×4
      (LOCKED_PULSE · HARD_DOCK · HALF_SKY · STATIC_SHADOW) FAZ 6 öncesi betikle BİREBİR aynı (+ rejim satırı) ·
      ⭐ ilk GERÇEK yeni-rejim klasörü `yatay_2_dk_filmler/THE_SHADOW_LINE` (sahibin paralel oturumu, 13:24-13:53):
      ㉕-㉚ temiz, tek bulgu 12 video promptu 120 kelimenin altında (NOT) · `rapor_kontrol.py --film HARD_DOCK`
      karar aynı + ①.12 NOT · `ders_frekans.py --tam` dersleşmemiş: Motion Quality 24 · Causality & Knowledge 12 ·
      Focus Honesty 5 · `film_klasoru_ac.sh` üç mod (aç · --sahne-guncelle · --kilit-sahne) + --analiz-ekle
      (eski rejim korunuyor) — test klasörleri silindi · `git status`: commit yok, sahibin
- [x] Bellek: `akis-ders-reformu-durum.md` + MEMORY.md satırı
- [x] Sahip raporu (aşağıda) · commit'e hazır (tip `kilavuz:`)

## 📣 SAHİP RAPORU — 14.09.2026 · veto noktaları

1. **YAŞAYAN 40** — `DERSLER/00_YASAYAN_DERSLER.md` ilk liste (seçim kuralı dosyada). Çıkan/giren varsa
   GİRİŞ/ÇIKIŞ defterine.
2. **OKUMA_CEKIRDEGI** — 24 satırlık manifest (20 + [dikey] 2 + [faz] 2). Yatay film ~10.500 satır;
   KILAVUZ_REHBERI'nin tamamı sayılıyor, ~1.200'ü okunuyor. Çıkarılacak/eklenecek dosya sahibin.
3. **8 cümlelik çekirdek** — KILAVUZ §5.1 (886 karakter; beş betik imzası + el/sınır + parçacık + ekipman).
   Bant POZİTİF gövdeye uygulanıyor (NEGATIVE hariç) — plan metninde belirsizdi, FAZ 7'de böyle
   kalibre edildi; toplam bant istenirse `KELIME_BANDI` tek yerde.
4. **Rubrik kesikleri** — `ARSIV_RUBRIK_DIYETI/` diyet-öncesi tam kopyalar; kategori listelerine dokunan
   kısım diyet-öncesi tam kopyayla `diff` alınarak görülür. Skor kayması olursa CALISTIRMA_KAYITLARI "diyet sonrası" etiketi.
5. **Yazılan ADAY kümeleri** — D206-D216 (11 ders); K15 süreç kümesi yazılmadı; 7 ADAY açık.
+ Kalibrasyon: image bant üst ucu 250 — WS kurulum sahnesi sıkı yazımla 250-270; THE_SHADOW_LINE'da
  video promptları 82-141 kelime (alt uç 120 NOT veriyor). İlk yeni-rejim filmden sonra iki sayı da
  tek yerde ayarlanır.
+ Dersleşmemiş üç örüntü (ders_frekans): Motion Quality (24 film) · Causality & Knowledge (12) ·
  Focus Honesty (5) — ders yazımı sahip kararı (Kart G, FREKANS zaten ≥2).
+ Bu dosya: tüm kutular ✅. Silme kararı commit sonrası sahibin (kalıcı bilgi kılavuzlara/betiklere indi;
  AGENTS §6 satırı dosya silinince silinir).

---

## 🚫 YAPILMAYACAKLAR

- Commit atılmaz; her faz "commit'e hazır" bırakılır.
- Ders silinmez (arşive iner) · ham QA çıktısı silinmez · rubrikten kesilen metin arşive gider.
- Eski film klasörlerine dokunulmaz; yeni kapılar yalnız yeni rejim klasörlerinde koşar.
- Kategori adları, SCORES SUMMARY biçimi ve betiğin okuduğu satırlar değişmez (T tabloları karşılaştırılabilir kalır).
- Sayı belgeye elle yazılmaz; tavanlar tek yerde (yukarıdaki tablo) durur.
