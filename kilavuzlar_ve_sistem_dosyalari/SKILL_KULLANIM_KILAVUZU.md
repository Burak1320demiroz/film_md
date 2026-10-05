# 🧰 SKILL KULLANIM KILAVUZU — Ajan Skill Envanteri ve Akıştaki Yeri

> **Neden var (27.08.2026):** `.claude/skills/` katmanı kuruldu — görev
> kartlarının sarmalayıcıları + seçilmiş dış skill'ler. Hangi skill ne zaman
> devreye girer, elle nasıl çağrılır, depo kurallarıyla çelişirse ne olur —
> tek liste burasıdır. AGENTS §1 haritası buraya işaret eder; envanter başka
> belgeye kopyalanmaz.
>
> **Ne zaman okunur:** yeni oturumda skill'lerin ne yaptığını hatırlamak
> gerektiğinde · yeni skill kurulacağında/kaldırılacağında (§5) · bir skill
> çıktısının depo kuralıyla çeliştiği görüldüğünde (§0).

---

# 0. DEĞİŞMEZ ÖNCELİK KURALI

```
① Skill SIRAYI ve TEKNİĞİ taşır; İÇERİK kuralı depo belgelerinindir.
   Çelişkide öncelik: AGENTS.md → depo kılavuzu → skill.
② Hiçbir skill commit atmaz, tabloya elle sayı yazmaz, ham raporu düzenlemez.
③ Dış skill çıktısı depo standartlarından MUAF DEĞİLDİR: negatif çekirdek,
   metin yasağı, süre/klip ızgarası, SPEC zorunluluğu aynen geçerli.
   Dış skill'in yazdığı hiçbir prompt, Kart P (prompt-kontrol) koşulmadan
   film dosyasına girmez.
④ Skill'ler oturum başında yüklenir — kurulum/değişiklik sonrası yeni
   oturum açılır.
```

---

# 1. KART SARMALAYICILARI — depo yapımı

Kartın kendisi AGENTS.md'dedir; skill yalnız sırayı dayatır.

| Skill | Kart | Kendiliğinden tetik | Elle çağrı |
|---|---|---|---|
| `yeni-film` | A | "yeni film yazalım / film fikrim var" | `/yeni-film <format> <FILM_ADI>` |
| `prompt-kontrol` | P | "üretime geçelim / promptlar hazır" — ⛔ tek kare üretmeden | `/prompt-kontrol <FİLM KLASÖRÜ>` ⛔ tek bölüm dosyası değil (klasör modu · REHBER §2.0) |
| `qa-isle` | C·D·E·E3·F·F2 + ortak kapılar ①-⑪ | QA raporu yapıştırıldığında | `/qa-isle <film klasörü> [master yolu]` |
| `yayin-takip` | Y | ⛔ YOK — yalnız elle (bilinçli tasarım) | `/yayin-takip <FILM> once\|24\|48\|72\|geri-besleme` |

Notlar:
- `qa-isle`'nin ölçüm betiği: `.claude/skills/qa-isle/scripts/olcum_kapisi.sh
  <master> [rms]` — ⑪ ÖLÇÜM KAPISI'nın dört komutu tek koşuda.
- `yayin-takip` satır yazmadan önce alanları gösterir ve ONAY bekler;
  geriye dönük satır ancak 🚨 GEÇERSİZ işaretiyle açılır.

---

# 2. DIŞ SKILL'LER

## 2.1 `image` + `video` — visual-skills (smixs)

**Lisans: CC BY 4.0, atıf ZORUNLU.** Bu skill'lerden kılavuzlara damıtılan
her kurala tek satır eklenir: `Kaynak: Serge Shima — github.com/smixs/visual-skills`

- **`video`** — AI video promptu yazar, denetler, storyboard'a döker.
  Zorunlu okuma sırası kendi içinde: dramaturji → evrensel kurallar →
  TEK model dosyası (bizim hat: `references/veo.md`). Çıktı vermeden önce
  kendi çift kapısını koşar (6 maddelik dramaturji + plan başına 3 detay).
  Çıktı modları: tek prompt · çoklu klip (süreklilik bloklu) · storyboard
  tablosu · **prompt audit** · yönetmen treatment'ı · **Veo JSON**.
- **`image`** — imaj promptu yazar (ilk kare, kapak, karakter sayfası,
  storyboard keyframe). Model seçer: Nano Banana (gerçek mekân grounding,
  uç en-boy oranları) vs GPT Image 2 (metin disiplini, koruma-kritik edit).
  Keyframe çıktıları `video` skill'ine beslenir — imaj-önce-video akışımızla
  birebir.
- ⚠️ Model lehçesi örneği (skill dosyalarından okunur, ezberden yazılmaz):
  Nano Banana lens sayılarını (50mm, f/1.8) YOK SAYAR; GPT Image 2'de
  "stunning/epic/masterpiece" kaliteyi DÜŞÜRÜR.
- ⛔ Sınırları: bu skill'ler SPEC sistemini, klip ızgarasını (süre araçtan
  ölçülür [D124]) ve negatif çekirdeği BİLMEZ. Ürettikleri prompt depo
  iskeletine oturtulur, yasaklar eklenir, sonra Kart P koşulur (§0-③).

### ⭐ 30.09.2026 · İKİSİNİN OTO-TETİĞİ KAPATILDI — yerel değişiklik

§0① *"çelişkide depo kazanır"* bir **doktrindi**, mekanik koruma değildi. Ölçüm:
dokuz skill'den `disable-model-invocation` taşıyan yalnız `yayin-takip`'ti, ve bu
ikisinin tetiği **deponun günlük işinin birebir tanımıydı.**

```
video  tetik: "create, improve, audit, or split prompts for AI video generators …
               shares a prompt and asks to fix it"
       ⭐ kendiliğinden ateşlerse getirdiği iki şey depoyla ÇATIŞIR:
         ① kendi "Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS"
            sırası ↔ deponun zorunlu okuması `yeni-film` adım 2'dir
         ② "Default … Multi-shot narrative or fast montage drama → Seedance"
            ↔ depo hattı §2.1'de `references/veo.md` olarak SABİT
image  tetik: "image prompt · storyboards · character sheets · blog covers"
       ⭐ `references/models.md`: "50mm / f-stop / ISO YAZMA" (NBP lehçesi)
          ↔ deponun Camera Bible'ı tam lens sayıları üstüne kurulu
          (emsal: THE_LAST_GATE 16 kurulum, hepsi `NNmm lens` ile başlar)
```

**Yapılan:** her iki `SKILL.md` frontmatter'ına `disable-model-invocation: true`
eklendi + gövdenin başına YEREL DEĞİŞİKLİK bloğu (CC BY 4.0'ın "değişikliği
belirt" yükümlülüğü burada karşılanır). Skill'ler **silinmedi, kısıtlanmadı** —
`/video` · `/image` ile ya da adıyla tam güçle çağrılır; yalnız artık **çağrılmadan
devreye girmez.** §4'ün örnek çağrıları bu yüzden açık biçime çevrildi.

⛔ **`skills-lock.json`'a DOKUNULMADI** ve dokunulmayacak. İki sebep:
```
① Lock'un computedHash'i dosyanın ham sha256'sı DEĞİL (30.09 ölçümü: ikisi de
   farklı çıktı, dosyalar 02.09'dan beri hiç değişmemişken). Şema bilinmiyor →
   oraya yazılacak sayı DOĞRULANAMAZ. Bu depoda doğrulanamayan sayı yazılmaz.
② İşimize geliyor: lock eski hash'i tuttuğu için `npx skills update` dosyayı
   "yerel değiştirilmiş" görür. Hash'i güncellemek, bir sonraki güncellemenin
   bu kararı SESSİZCE ezmesi demekti.
```
⚠️ Yine de `npx skills update` koşulduktan sonra **bu iki frontmatter satırı
kontrol edilir** — yoksa geri eklenir (§5).
- Not: marketingskills'in eski `video` skill'i (araç kataloğu) bu kurulumla
  DEĞİŞTİRİLDİ — 27.08.2026. Gerekirse `npx skills add
  coreyhaines31/marketingskills --skill video` ile geri gelir (ad çakışır,
  ikisi bir arada durmaz).

## 2.2 `social` · `ab-testing` · `content-strategy` — marketingskills (coreyhaines31)

- Üçü de işe başlamadan `.agents/product-marketing.md`'yi okur — kanal
  kimliği dosyası; ⬜ alanları sahip doldurur, boş kaldıkça skill soru sorar.
- **`social`** — platform metinleri, hook kalıpları, paylaşım planı.
  `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` ile çelişirse depo promptu kazanır.
- **`ab-testing`** — kapak/başlık deney tasarımı, örneklem disiplini.
  Kart Y'nin TEK DEĞİŞKEN KİLİDİ (ilk 48 saat: kapak VEYA başlık) bu
  skill'in "tek değişken" ilkesiyle aynı — birlikte kullanılır.
- **`content-strategy`** — seri/kanal içerik planı;
  `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` ile yan yana okunur.

⚠️ **İZLENECEK (30.09.2026): üçünün oto-tetiği AÇIK BIRAKILDI — ama `social` sürtünüyor.**
Tetik listesinde `"viral content"` · `"video hook"` · `"short-form video"` ·
`"Shorts"` geçiyor; bunlar deponun ⭐viral bandı, `HOOK_VE_ILK_SAHNE` kılavuzu ve
dikey shorts hattıyla aynı kelimeler. `video`/`image` kapatıldı (§2.1) ama bu üçü
kapatılmadı, çünkü ürettikleri şey **film dosyasına girmiyor** — `<FILM>_YAYIN_PAKETI.md`'ye,
yani §3'te yazılı çok daha geç bir aşamaya giriyor; yanlış ateşlerse çıktı bariz
biçimde konu dışı olur ve fark edilir. `video`/`image`'in riski başkaydı: **doğru
görünen ama negatif çekirdeği atlayan prompt.** Ölçüm: `social` film yazımı sırasında
kendiliğinden ateşlerse buraya satır yazılır ve o da kapatılır.

## 2.3 `creative-director` — smixs (⭐ DAMITILDI, KURULMADI · 21.09.2026)

**Lisans: CC BY 4.0, atıf ZORUNLU.** Sahip kararı (21.09.2026): skill depoya
kurulmadı; yöntemi `HIKAYE_FIKIR_TURU_KILAVUZU.md`'ye damıtıldı ve `yeni-film`
adım 0.7a olarak akışa girdi. Atıf satırı o kılavuzun başlığında:
`Kaynak: Serge Shima — github.com/smixs/creative-director-skill`.

- **Alınan:** gerilim cümlesi (insight) · üç kategoriden yöntem rotasyonu
  (SIT · SCAMPER · bisosiyasyon · ters beyin fırtınası · PO…) · ilk üç fikir
  ısınma · gerilim testi · duygu kademesi (sıradan / belirli / çift-duygu) ·
  gözdeyi öldür · hikâye omurgası (Story Spine, Pixar kuralları) · ön-otopsi.
- **Alınmayan:** reklam brief alanları (marka · hedef kitle · tagline · medya) ·
  1-10 puan tabloları ve HumanKind/Grey skalaları · vaka kütüphanesi (üst kaynakta
  yüzlerce reklam kampanyası kartı — film için doyum ölçüsü olarak
  `KILAVUZ_REHBERI` §8 matrisi kullanılır).
- **Neden kurulmadı:** üst kaynak yüzlerce reklam vaka dosyası taşır; skill
  runtime'da yüklendiğinde akışı kampanya brief'ine çeker; lisans damıtmaya izin
  verir (visual-skills → VEO kılavuzu §6B emsali). İstenirse `npx skills add
  smixs/creative-director-skill -g` ile depo DIŞINA kurulabilir; kılavuz değişmez.
- ⛔ `image`/`video` skill'leri "fikir yoksa creative-director'a git" der; bu
  depoda o kapı `yeni-film` 0.7a'dır, skill değil.

## 2.4 `skill-conductor` — smixs (GLOBAL KURULDU · 21.09.2026 · MIT)

- **Ne yapar:** yalnız **SKILL.md dosyalarını** ölçer (CREATE · IMPROVE · VALIDATE ·
  REVIEW · OPTIMIZE · PACKAGE); film ya da QA çıktısını DEĞİL. 21.09 araştırma
  raporundaki "rapor_kontrol.py ile QA doğrulaması" kullanımı yanlış okumaydı.
- **Alınan:** BinEval biçimi — evet/hayır soru + kanıt, eşik yargıca söylenmez
  (`HIKAYE_FIKIR_TURU` §4 eleme soruları bu biçimdedir).
- **Kurulum:** sahip kararıyla (21.09.2026, ikinci soru) **depo DIŞINA**:
  `~/.claude/skills/skill-conductor` (`npx skills add smixs/skill-conductor -g`);
  `skills-lock.json` değişmedi. `uv` Homebrew'la kuruldu; betikler `uv run` ister.
  Betikler kurulmadan okundu: ağa çıkan tek şey `claude -p` (OPTIMIZE / tetik
  testi), gerisi yerel. Duman testi geçti.
- **İlk ölçüm (deterministik sorular, `yeni-film`):** üç "hayır" — tetik ifadesi
  (araç İngilizce "Use when" kalıbı arıyor; Türkçe tetik var) · negatif tetik yok
  ("şunun için kullanma" satırı) · gövde aracın uzunluk sınırının üstünde. Süreç-sızması
  denetimi İngilizce kalıba bakar; description'ın adım sayması sahibin gözüyle
  değerlendirilir. Tam VALIDATE (yargıç soruları) **sahip koşar**, bulgular ayrı iş.
- **Kullanım:** `/skill-conductor VALIDATE .claude/skills/yeni-film` · üçüncü taraf
  skill kurmadan önce `REVIEW` (§5 "okunmadan kurulmaz" kuralının makine karşılığı).
  ⛔ Film, prompt, QA raporu için çağrılmaz.

---

# 3. AKIŞTAKİ YERİ — hangi adımda hangi skill

```
FİKİR        yeni-film 0.7a  (HIKAYE_FIKIR_TURU — creative-director'dan damıtıldı;
   │          gerilim → havuz → eleme → üç aday → sahip onayı; skill değil, kılavuz)
   ▼
YAZIM        yeni-film  (KILAVUZ_REHBERI + kartlar + QA_SPEC)
   │
PROMPT       image  → ilk kare / kapak / karakter sayfası promptları
YAZIMI       video  → sahne (Veo) promptları · storyboard · audit
   │            ↳ çıktı depo iskeletine + negatif çekirdeğe oturtulur
   ▼
KAPI         prompt-kontrol  ⛔ tek kare üretmeden · betik + rubrik → GO/BLOCK
   │            ↳ rubrik adımında video skill'in "audit" modu yardımcı olabilir;
   │              kararı rubrik verir, skill değil
   ▼
ÜRETİM       (Kart B — skill'siz: imaj onayı → video → müzik → kapak → kurgu)
   ▼
QA           qa-isle  → ölçüm betiği + kapılar ①-⑪ + kayıt zinciri
   ▼
PAKETLEME    social (+ image: kapak varyantı) · ab-testing (deney tasarımı)
   │            ↳ çıktı `<FILM>_YAYIN_PAKETI.md`'ye TAMAMEN İNGİLİZCE yazılır
   │              (kural VIRAL_BASLIK · kanal metni apexaic/<platform>/
   │               PAKETLEME_SABLONU.md — sabit blok kopyalanmaz, yapıştırılır)
   ▼
YAYIN        yayin-takip  → once → 24/48/72 → geri-besleme
SERİ PLANI   content-strategy (SERI_VE_KANAL_STRATEJI ile)
```

---

# 4. ÖRNEK ÇAĞRILAR

```
/yeni-film dikey THE_SILENT_ORBIT
/prompt-kontrol yatay_2_dk_filmler/THE_X        ⛔ klasör, tek bölüm değil
/qa-isle dikey_shorts_filmler/THE_X ~/masaustu/THE_X_master.mp4
/yayin-takip THE_X once

⭐ 30.09.2026: video/image artık KENDİLİĞİNDEN ateşlemiyor (§2.1) — ADI YAZILIR.
/video  "S7'nin promptunu Veo JSON formatına çevir"
/video  "Audit this prompt: <prompt>"                        (D modu)
/image  "Bu sahne için 6 kareli animatic keyframe seti yaz"  → sonra /video
/image  "Kapak için metinsiz sinematik imaj promptu yaz: <sahne>"
        ⛔ Çıktı doğrudan film dosyasına GİRMEZ: depo iskeletine oturur,
           negatif çekirdek eklenir, sonra Kart P koşulur (§0③).

"Bu film için TikTok/Shorts açıklaması yaz"                → social      (oto-tetik AÇIK)
"Kapak A/B deneyi kur: <iki kapak>"                        → ab-testing  (oto-tetik AÇIK)
"Bu konu için fikir turu koş, üç aday çıkar"               → yeni-film 0.7a
                                                              (HIKAYE_FIKIR_TURU §2-§6)
```

---

# 5. BAKIM

```
□ GÜNCELLEME   npx skills update        (kilit dosyası: kökteki skills-lock.json)
               ⛔ KOŞUDAN SONRA: §2.1'in iki frontmatter satırı
               (`disable-model-invocation: true` → video · image) DURUYOR MU?
               Güncelleme onları ezerse geri eklenir; kayıt §2.1'dedir.
□ YEREL        Dış skill'in dosyası değiştirildiyse (30.09.2026 emsali):
  DEĞİŞİKLİK   ① gövdenin BAŞINA `> ⚠️ YEREL DEĞİŞİKLİK — <tarih>` bloğu —
                  ne · neden · kaydın adresi. CC BY 4.0 bunu ZORUNLU kılar
                  ("indicate if changes were made"), tercih değil.
               ② gerekçe bu kılavuza iner (§2.x), skill dosyasına değil.
               ③ ⛔ `skills-lock.json` GÜNCELLENMEZ — eski hash, güncellemenin
                  kararı sessizce ezmesini engelleyen tek işarettir. Ayrıca
                  lock'un hash şeması dosyanın ham sha256'sı değil; oraya
                  doğrulanamayan sayı yazılmaz.
               ⭐ Skill SİLMEK yerine oto-tetiği kapatmak: yetenek durur,
                  yalnız çağrılmadan devreye girmez. İlk tercih bu olsun.
□ YENİ SKILL   SKILL.md + varsa scripts/ OKUNMADAN kurulmaz (güvenlik +
               uygunluk). Kurulunca: bu kılavuza satır eklenir; AGENTS
               haritası DEĞİŞMEZ (harita buraya işaret eder).
□ KALDIRMA     klasör silinir + bu kılavuzdan satırı düşülür; ad çakışması
               notu varsa güncellenir.
□ ÖZEL SKILL   kart sarmalayıcıları depo dosyasıdır: kart değişirse
               sarmalayıcı da güncellenir — kartla skill'in çelişmesi
               "kaydı olmayan kapı"dır [D74 ruhu].
□ SAYI YOK     bu kılavuza da sayı yazılmaz; envanter LİSTEDİR, sayaç değil.
```

---

# 6. DEĞERLENDİRİLEN DIŞ SKILL'LER — 21.09.2026 araştırması (TUR 23)

> Sahibin 21.09.2026 tarihli "otonom ajan becerileri ve senaryo/dramaturji boru
> hattı" araştırma raporunun düzeltilmiş özeti. Ham üst-kaynak README'leri
> `URETIM_ONCESI_ANALIZ/TUR23_HAM_RAPORLAR/`; bulgu kaydı `04_ARASTIRMA_BULGULARI`
> TUR 23. Envanter TEK yerde durur (§5 kuralı) — kökteki kopya kaldırıldı.

## 6.1 Departman kapsamı

Sanal film ekibinin yedi departmanından yalnız üçü ajan becerisiyle desteklenir;
görsel/ses üretim ve kurgu katmanı sahip tarafından promptlarla yürütülür.

| departman | ajan kapsamı | depodaki karşılık |
|---|:--:|---|
| Senaryo & dramaturji | ✅ | `yeni-film` 0.7a fikir turu (`HIKAYE_FIKIR_TURU`) · HOOK · ONERME · TEMA |
| Sinematografi & prompt · devamlılık · ses · kurgu | ⛔ | sahip, promptlarla (kart B) |
| Kalite güvencesi | ✅ | `qa-isle` · `rapor_kontrol.py` · on iki çıplak rubrik |
| Dağıtım & büyüme | ✅ | `social` · `ab-testing` · `content-strategy` · `yayin-takip` (kart Y) |

## 6.2 Skill kararları

| skill | kaynak | lisans | karar | nerede |
|---|---|---|---|---|
| creative-director | smixs | CC BY 4.0 (atıf) | **damıtıldı, kurulmadı** | §2.3 · `HIKAYE_FIKIR_TURU_KILAVUZU` |
| skill-conductor | smixs | MIT | **global kuruldu** (depo dışı, 21.09 ikinci karar); BinEval biçimi alındı | §2.4 |
| banana-claude (Gemini imaj üretimi: generate · edit · compare · typeset) | AgriciDaniel | MIT | **kurulmadı** — ücretli Gemini API anahtarı ister, sahipte yok; Nano Banana elle promptla üretiliyor (`image` skill prompt yazar). Anahtar gelirse ilk iş: referans paketi sayfaları, sonra kapak üç aday | — |
| social · ab-testing · content-strategy | coreyhaines31/marketingskills | MIT | zaten kurulu; ek skill yok | §2.2 |
| `fountain` (raporda "senaryo analizi") | — | — | **tanımlanamadı** — depo/skill adı yok; sahip ad verirse açılır | — |

## 6.3 Raporda düzeltilen üç cümle

```
① skill-conductor "rapor_kontrol.py ile QA raporlarını doğrular" → HAYIR; yalnız
   SKILL.md dosyalarını ölçer (üst kaynağın kendi kapsam beyanı).
② "deponun 1.6 s kanca süresi" → depoda karar penceresi 1,7 s (HOOK §1); sayı
   burada da tekrar edilmez, adres verilir.
③ "marketingskills kurulacak" → üçü 02.09.2026'dan beri kurulu (skills-lock.json).
```

## 6.4 Koruma kuralları — §0 ile aynı, burada yalnız adres

```
ÇIKTI FİLTRESİ      dış skill'in ham metni film dosyasına girmez; depo iskeletine
                    oturur (0.7a çıktısı → 00_HIKAYE_ONAYI biçimi, §0①·③)
PROMPT-KONTROL      hiçbir dış çıktı Kart P koşulmadan üretime girmez (§0③)
PUANLAMA KAPILARI   ikili soru + kanıt, eşik gizli (BinEval biçimi) — puan yazılmaz
```

## 6.5 Risk matrisi (özet)

| risk | önleme | adres |
|---|---|---|
| senaryo kuralı çelişkisi (negatif çekirdek · tema · novum atlanır) | fikir turu çıktısı adım 4'te konsept kapılarından geçer; depo kuralı kazanır | `ONERME` §4 · `TEMA` §9 · `KILAVUZ_REHBERI` §5 |
| hook/tutundurma uyumsuzluğu | HOOK §3.1 dramatik ironi + §8 listesi; kılavuz sahibi HOOK | `HOOK_VE_ILK_SAHNE` |
| vuruş haritası sapması | zamanlama SENARYO §2'den; fikir turu yalnız nedensellik iskeleti verir | `HIKAYE_FIKIR_TURU` §7 ⛔ |
| pazarlama dili sızması | çıktı `VIRAL_BASLIK` formatına ve `apexaic/<platform>/PAKETLEME_SABLONU`'na oturur | §2.2 |
| telif / amblem sızması | referans paketi doğrulaması; onaylı amblem dışı negatif çekirdeğe | `REFERANS_PAKETI` |
