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
- ⛔ Sınırları: bu skill'ler SPEC sistemini, 8 saniyelik klip ızgarasını ve
  negatif çekirdeği BİLMEZ. Ürettikleri prompt depo iskeletine oturtulur,
  yasaklar eklenir, sonra Kart P koşulur (§0-③).
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

---

# 3. AKIŞTAKİ YERİ — hangi adımda hangi skill

```
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
/prompt-kontrol yatay_2_4_dk_filmler_uzay/THE_X        ⛔ klasör, tek bölüm değil
/qa-isle dikey_shorts_filmler/THE_X ~/masaustu/THE_X_master.mp4
/yayin-takip THE_X once

"S7'nin promptunu Veo JSON formatına çevir"                → video
"Audit this prompt: <prompt>"                              → video (D modu)
"Bu sahne için 6 kareli animatic keyframe seti yaz"        → image → video
"Kapak için metinsiz sinematik imaj promptu yaz: <sahne>"  → image
"Bu film için TikTok/Shorts açıklaması yaz"                → social
"Kapak A/B deneyi kur: <iki kapak>"                        → ab-testing
```

---

# 5. BAKIM

```
□ GÜNCELLEME   npx skills update        (kilit dosyası: kökteki skills-lock.json)
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
