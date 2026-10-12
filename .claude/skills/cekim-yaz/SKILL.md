---
name: cekim-yaz
description: Yeni hat faz 5 (referans · başlangıç karesi · video promptları + Flow iş emri) ve faz 7 üretim döngüsü (kare denetimi, kareli animatik, başarısız çekimin yeniden tasarımı) prosedürü. /yeni-film tarafından dosya olarak okunur; sahip /cekim-yaz ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(shasum:*), Bash(ls:*), Bash(mkdir:*), Bash(cp:*)
---

# Çekim yaz — faz 5 · faz 7

Prompt yazım kuralları **goruntu-yonetmeni** ajanının dosyasındadır (`.claude/agents/goruntu-yonetmeni.md`);
burada tekrar edilmez. Burası ana ajanın prosedürüdür.

Faz döngüsü: `yeni-film` §2.

## §F5 — Promptlar (tavan 2 tur)

1. **Gruplar:** `FILM.md` §4'teki `Grup` sütunu (8-12 çekim). Her grup için bir **goruntu-yonetmeni**
   çağrısı; grupları **tek mesajda paralel** çağır.
   - `{CIKTI}` = `<FILM>/PROMPTLAR/<grup>.md`.
   - İlk grup ayrıca `REFERANS PROMPTLARI` bölümünü yazar (FILM.md §3'teki referanslar; **özne başına tek sayfa**, açılar/yüz/durumlar panel, 10.10.2026).
   - Zincirli çekimlerin anahtar kareleri (`SAHNELEME.md` §2) o zincirin ilk çekiminin grubunda
     `## Zk.n` bölümleri olarak yazılır (yıldız düzeni). Bir zincir iki gruba bölünmez.
2. **Paralel eleştiri**, grup başına:
   - **devamlilik:** o grubun dosyası + `FILM.md` §3.
   - **teknik-danisman:** yalnız risk sütunu dolu çekimler.

   Bütün gruplar bittikten sonra **devamlilik**'e bir **gruplar arası** geçiş daha:
   tüm `PROMPTLAR/*.md` + §3. Yalnız kimlik/dünya/ışık cümlelerini karşılaştırır.
3. **Tur:** ÖLÜMCÜL bulgu → ilgili grubun goruntu-yonetmeni'ne revizyon. Ajan dosyayı kendisi günceller.
   ⛔ Revizyon ya da birleştirme geçişinden ÖNCE ana ajan önceki sürümü saklar: `cp <FILM>/PROMPTLAR/<grup>.md <FILM>/ODA/F5_goruntu-yonetmeni_<tur>_<grup>.md` (denetci Ö4 farkı buna bakar; iki filmde unutuldu: WRONG_BURN · PLANET_THIEF).
4. **Mekanik kontrol:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum cekim sahneleme prompt`
   (meta etiket · ≤4.300 karakter · her çekimin promptu · iş emri · **referans anahtarı** `Reference <No>` ↔ `ref/<No>.<AD>` ·
   **10 s vuruş planı** `a-b s`; ikisi sahip kararı 10.10.2026, yalnız §3'ü numaralı yeni filmlerde; eski biçimde ⚠️ ile atlanır).
5. **Kapı:** `denetci` (Ö + F5) → Fable. `FILM.md` §4 Durum sütunu → ✍️.
6. **Sahibe iş listesi (faz 7 başlangıcı):** önce Flow proje ayarları (model sesi KAPALI filmde Return silent videos AÇIK; **model sesi AÇIK filmde**
   — `FILM.md` §5'te Kaynak = model sesi varsa — Return silent videos **KAPALI**, replik klipten gelir (12.10.2026) · Visible watermarking KAPALI;
   iş emri şablonunun başı), sonra yalnız **referans kareleri**. Hangi prompt, hangi
   dosya adıyla (`~/film_medya/<FILM>/ref/1.KARAKTER_v1.png …` — numara §3'ten; Flow'a yüklerken `EKLE` satırındaki sırayla).
   Model sesi AÇIK filmde ilk video denemesi SMOKE P18'dir (iki replikli çekim + alıcıdan ses çekimi).

## §F7 — Üretim döngüsü (sahip Flow'da üretir; Fable yalnız kare kanıtıyla onaylar)

```
7a REFERANS      sahip ref/ karelerini üretir (dosya adı <No>.<AD>_v1.png, §3'teki numarayla) → SHA-256: shasum -a 256 <dosya> | cut -c1-12
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
