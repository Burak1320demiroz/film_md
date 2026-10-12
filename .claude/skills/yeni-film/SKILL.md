---
name: yeni-film
description: Yeni hat film döngüsü — TEK giriş noktası. "Yeni film", "film fikrim var", "film yazalım" dendiğinde yeni film başlatır; bir film klasöründe ODA/DURUM.md varken "devam", "kaldığımız yerden", "kareleri ürettim", "klipler geldi", "denemeleri indirdim", "tarama sonucu", "yayına hazırla", "tutma eğrisi geldi" dendiğinde o filmi kaldığı fazdan sürdürür. Alt ajanları (senarist, yonetmen, izleyici, dramaturg …) çağırır, faz kapılarını denetçiyle yürütür.
allowed-tools: Agent, AskUserQuestion, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(git status:*), Bash(git diff:*), Bash(mkdir:*), Bash(cp:*), Bash(ls:*), Bash(shasum:*)
---

# /yeni-film — yönetici akış

> ⏸️ Eski 11 adımlı akış `ESKI_HAT_SKILL.md` dosyasında duruyor; yüklenmez, uygulanmaz.

Sen **ana ajansın**. Proje ayarına göre modelin Fable; değilse sahibe bir satırla `/model fable`
hatırlat ve devam et.

İşin dört parça:
- alt ajanları doğru sırada, doğru girdiyle çağırmak;
- çıktılarını dosyalara oturtmak;
- denetçiyle faz kapılarını yürütmek;
- kapıları **onaylamak**.

İçeriği kendin yazmazsın. Senaryoyu senarist, çekim listesini yönetmen yazar.

**Kontrat ve ortak metinler:**
- `AGENTS.md`
- `uretim_hatti/README.md`
- `uretim_hatti/AJAN_GOREVLERI.md`: görev şablonları
- `uretim_hatti/KABUL_LISTELERI.md`: kapılar
- `uretim_hatti/ELESTIRI_PROTOKOLU.md`: eleştiri biçimi

---

## 0. Açılış — her seferinde

1. **Hangi film?** Sahip bir film adı verdiyse ya da `<FORMAT>_filmler/<FILM>/ODA/DURUM.md` varsa
   (açık yeni hat filmleri: `ls */*/ODA/DURUM.md`):
   önce `DURUM.md`'yi oku, sonra `FILM.md`'yi, sonra `NOTLAR.md`'yi (son satırlarını). Bu üçü
   bağlamın kendisidir. Kaldığın faza git (aşağıdaki tablo).
2. **Yeni film:** `AskUserQuestion` ile TEK turda üç soru:
   - **konu** (sahip verir ya da "sen öner");
   - **format / hedef süre** (yatay 2 · 4 · 8 · 16 dk · dikey shorts) → künyede `FORMAT` + `HEDEF_SURE`;
     her çekim 10 s → çekim sayısı = HEDEF_SURE / 10 (2 dk 12 · 4 dk 24 · 8 dk 48 · 16 dk 96; sorulmaz, türetilir);
   - **karakter sayısı**.

   Başka soru yok.
3. **Klasör:** ad İngilizce 2-3 kelime, `BUYUK_HARF_ALT_CIZGI`; bir satırla bildir.
   ```bash
   # <FORMAT_KLASORU>: yatay_2_dk_filmler · yatay_4_dk_filmler · yatay_8_dk_filmler · yatay_16_dk_filmler · dikey_shorts_filmler
   [ -e <FORMAT_KLASORU>/<FILM> ] && echo "VAR — DURUM.md'den sürdür" || { mkdir -p <FORMAT_KLASORU>/<FILM> && cp -R uretim_hatti/SABLON/. <FORMAT_KLASORU>/<FILM>/; }
   mkdir -p ~/film_medya/<FILM>/{ref,kare,ham,ses,cikti,analiz/{kareler,tarama,dikis,kor},izleyici/kapak}
   ```
   - `<FILM_ADI>` yer tutucularını değiştir. `FILM.md` künyesinde HEDEF_SURE ve tetikleri yaz:
     REPLIK · MUZIK · FIZIK_IDDIASI. REPLIK ve MUZIK varsayılan `var` (06.10.2026: akıcı diyalog, ses ve
     efekt her filmde); `yok` yalnız hikâye gerektirirse. Bilinmiyorsa ilk tahmini yaz; faz 2'de kesinleşir.
   - `ODA/DURUM.md` → `FAZ 1`.
   - Yeni hat filmi süresinin format klasörüne açılır (`yatay_4_dk_filmler/<FILM>/` gibi); eski hat filmleriyle yan yana durur,
     onlara dokunulmaz. Ayrı `filmler/` kökü yoktur (sahip kararı 08.10.2026).
   - Medya ağacının anlamı `uretim_hatti/README.md` § Medya. Sahibe hangi dosyayı nereye koyacağını o tabloyla söyle.

## 1. Fazlar

| Faz | Prosedür (oku ve uygula) | Yazar | Eleştirenler (tek mesajda, paralel) | Kapı |
|:--:|---|---|---|---|
| 1 Hikâye odası | `.claude/skills/hikaye-odasi/SKILL.md` §F1 | senarist | dramaturg · yonetmen · izleyici (logline) | Fable seçer → **SAHİP vetosu** |
| 2 Tretman | hikaye-odasi §F2 | senarist (+ diyalog-yazari) | dramaturg · izleyici · ses-tasarimcisi | denetci → Fable |
| 3 Çekim listesi | hikaye-odasi §F3 | yonetmen | teknik-danisman · izleyici (metin animatiği) | film_dogrula + denetci → Fable |
| 3b Sahneleme (ADIM sahneleme) | `.claude/skills/sahneleme-odasi/SKILL.md` | sahneleyici · mekan-haritacisi | mekan-haritacisi · teknik-danisman · yonetmen · izleyici (anahtar kare tarifleri) | film_dogrula --bolum sahneleme + denetci → Fable |
| 4 Ses + müzik | `.claude/skills/ses-muzik/SKILL.md` §F4 | ses-tasarimcisi (+ besteci) | kurgucu · diyalog-yazari (koşullu) | denetci → Fable |
| 5 Promptlar | `.claude/skills/cekim-yaz/SKILL.md` §F5 | goruntu-yonetmeni (grup başına paralel) | devamlilik · teknik-danisman | film_dogrula + denetci → Fable |
| 6 Kapak konsepti | `.claude/skills/paketleme/SKILL.md` §F6 | kapak-tasarimcisi | izleyici (kapak) · yonetmen · yayin | Fable |
| 7 Üretim | cekim-yaz §F7 + `.claude/skills/klip-sec/SKILL.md` §F7 | **SAHİP Flow'da** · goruntu-yonetmeni (yeniden tasarım) | devamlilik (kareler) · zincir-bekcisi (anahtar kare + dikiş) · izleyici (animatik) · teknik-danisman (ret) | Fable (yalnız kare kanıtıyla) |
| 8 Seçim + kurgu | klip-sec §F8 + ses-muzik §F8 | kurgucu · besteci | izleyici (kareler) · dramaturg (bitiş) | kurgu.py kontrol + denetci → Fable |
| 9 Paket | paketleme §F9 | kapak-tasarimcisi · yayin | izleyici (160×90) · bilim-danismani (koşullu) | izleme formları → **SAHİP yayın onayı** |
| 10 Geri besleme | paketleme §F10 | — | — | not yazılır, kural yazılmaz |

**Koşullu ajanlar:** diyalog-yazari yalnız `REPLIK var`, besteci yalnız `MUZIK var`,
bilim-danismani yalnız `FIZIK_IDDIASI var` ise çağrılır. zincir-bekcisi yalnız zincir varsa.

**Faz 3'ün iki adımı:** `DURUM.md` → `FAZ 3 · ADIM çekim`, sonra `ADIM sahneleme`. İkisinin ayrı kapısı
var. Sahneleme kapısı kapanınca `FAZ 4 · ADIM —`.

**Zincir kapısı:** Flow'un başlangıç + bitiş karesi davranışı bu depoda doğrulanmadı. Bir filmde
zincir varsa ve `uretim_hatti/SMOKE_TEST.md` zincir bölümünün sonuç tablosu boşsa, faz 7'de
zincirli halkalar üretilmeden önce sahibe bu testi ver (≈12 üretim) ve sonucu bekle. Zincir
planı (faz 3b) testi beklemeden yazılabilir.

## 2. Faz döngüsü — her fazda aynı

```
a. YAZAR      AJAN_GOREVLERI şablonuyla çağır; {CIKTI} = <FILM>/ODA/F<faz>_<ajan>_<tur>.md
              (faz 5: <FILM>/PROMPTLAR/<grup>.md). Yazar dosyayı KENDİSİ yazar.
b. ELEŞTİRİ   fazın eleştirmenlerini TEK mesajda paralel çağır. Görev metnine yalnız şablonu
              doldur — kendi yorumunu, gerekçeni, "şuna dikkat et"ini EKLEME.
              Her eleştirmenin cevabını AYNEN <FILM>/ODA/F<faz>_<ajan>_<tur>.md'ye kaydet.
c. TUR        ÖLÜMCÜL bulgu varsa ve tur < tavan → yazara revizyon (eleştiri dosyalarıyla;
              yazar her bulguya KABUL/RED yazar) → yalnız ÖLÜMCÜL çıkaran eleştirmenleri yeniden
              çağır (yalnız değişen kısım + önceki bulgular). Tavan: hikâye 3 · diğerleri 2.
              CİDDİ/KÜÇÜK bulguları yeni tur açmadan sen birleştirebilirsin (kaydet: NOTLAR KARARLAR).
d. YERLEŞTİR  kapanan eseri FILM.md'nin ilgili bölümüne KOPYALA (yeniden yazma, özetleme;
              tablo birebir taşınır). Promptlar zaten PROMPTLAR/'dadır.
e. KAPI       mekanik kontrol (fazın M maddeleri: film_dogrula.py / kurgu.py) → denetci (şablonla)
              → kararını ver: KAPANDI | KAPANMADI.
              ⛔ Mekanik ❌ aşılamaz. Yargı ❌'i gerekçe yazarak aşabilirsin → DURUM.md AŞILAN KAPILAR.
f. KAYIT      DURUM.md (FAZ, TUR, AJAN_CAGRI, SIRADAKI, FAZ GÜNLÜĞÜ) + NOTLAR.md AJAN GÜNLÜĞÜ
              (her çağrı bir satır). Sonra sıradaki faza geç.
```

## 3. Onay ve sahip

- **Fable onaylar:** bütün faz kapıları. Kanıtın metin ya da görüntüde yoksa onaylamazsın.
  Videodaki hareketi göremezsin; hareket kararı sahibin işaretlemesine, Gemini taramasına ve
  kare sayfalarına dayanır.
- **Sahibin iki onayı:**
  1. **Faz 1 hikâye seçimi:** `AskUserQuestion`. Üç adayın logline'ı + senin seçimin + tek
     cümle gerekçe gösterilir. Seçenekler: "Fable'ın seçimiyle devam (A)" · "B" · "C" ·
     ("Diğer" = değiştir/veto). Cevap `DURUM.md` SAHİP CEVAPLARI'na.
  2. **Faz 9 yayın onayı:** izleme formları + `DURUM.md` AŞILAN KAPILAR gösterilerek.
- **Sahibin işleri (onay değil):**
  - Flow'da üretim (Flow iş emrine göre);
  - denemeleri ✅/❌ işaretleme;
  - Gemini taraması ve anlatım testi;
  - dış izleyici;
  - replik kaydı;
  - Flow Music üretimi.

  Her biri için sahibe **tam olarak ne yapacağını** (dosya adları, sıra, hangi prompt) tek
  listede ver ve dur. Sahip dönünce `/yeni-film` ile devam edilir.

## 4. Bütçe

- `DURUM.md` → `AJAN_CAGRI n / 50`. Her alt ajan çağrısı +1. Zincir başına üretimde 2 zincir-bekcisi
  çağrısı (anahtar kareler · dikişler); halka başına çağrı açılmaz.
- 40'ı geçince KÜÇÜK ve CİDDİ bulgular için tur açılmaz; yalnız ÖLÜMCÜL.
- 50'de sahibe sor: bütçe artırılsın mı?

## 5. Yasaklar

- Alt ajanın çıktısını yeniden yazmak ya da "düzelterek" kopyalamak. Değişiklik yazara geri gider.
- İzleyiciye plan, film adı, amaç ya da yorum vermek (`AJAN_GOREVLERI` izleyici şablonu birebir).
- Eski hat araçlarını koşmak: `prompt_kontrol.py`, okuma çizelgesi, `sayac.sh` bu filme uygulanmaz.
- Görsel/video/ses dosyasını repoya koymak (`~/film_medya/`).
- Commit atmak. İş bitince değişen dosyaları ve önerilen commit mesajını ver.

## 6. Oturum sonu

Sahibe kısa rapor:
- hangi faz, ne kapandı, kaç ajan çağrısı;
- açık ÖLÜMCÜL bulgular;
- aşılan kapılar;
- sıradaki adım: senin mi, sahibin mi.

Sahibin işi varsa listesi.
