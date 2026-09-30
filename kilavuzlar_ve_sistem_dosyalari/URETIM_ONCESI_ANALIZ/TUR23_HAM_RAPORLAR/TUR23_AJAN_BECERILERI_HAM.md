# 🧾 TUR 23 — AJAN BECERİLERİ · HAM (21.09.2026)

> Sahibin 21.09.2026 tarihli derin araştırma raporu + oturuma yapıştırılan üç üst-kaynak
> GitHub README'si (coreyhaines31/marketingskills · smixs/skill-conductor ·
> smixs/creative-director-skill), birebir. Süzülmüş hâli `04_ARASTIRMA_BULGULARI` §TUR 23;
> karar ve envanter `SKILL_KULLANIM_KILAVUZU.md` §2.3 · §2.4 · §6.
> ⛔ Kural (04 §②): kılavuz kuralı buradan okunmaz; burası kaynağın kaydıdır.
> Raporun üç cümlesi süzgeçte düzeltildi (04 §TUR 23 ①); metin burada düzeltilmeden durur.

---

# 🎬 Otonom Ajan Becerileri ve Senaryo / Dramaturji Boru Hattı Mimarisi

> **Tarih:** 21.09.2026 · **Kaynak:** Derin araştırma raporu (TUR 22 sonrası)
>
> **Bu dosya ne:** Sanal Film Ekibi mimarisinin **senaryo, dramaturji, kalite
> kontrol ve dağıtım** ayağındaki açık kaynak skill envanteri ve risk matrisi
> referansıdır. Video/görsel ve ses üretim araçları (image, video prompt,
> FFmpeg, ElevenLabs, C2PA) bu belgede YER ALMAZ — o katman promptlarla
> sahip tarafından elle yürütülür.
>
> **Depo kuralı:** Skill SIRAYI ve TEKNİĞİ taşır; İÇERİK kuralı depo
> belgelerinindir. Çelişkide: `AGENTS.md` → depo kılavuzu → skill
> (`SKILL_KULLANIM_KILAVUZU.md` §0).

---

# 1. MİMARİ GENEL BAKIŞ — Ajan Kapsamındaki Departmanlar

Aşağıdaki tablo tam 7 departmanlı Sanal Film Ekibi'ni gösterir.
**Bu belgede yalnız ajan becerisiyle desteklenen departmanlar yer alır**;
görsel/ses üretim ve teknik kurgu katmanı sahip tarafından promptlarla
yürütüldüğü için kapsam dışıdır.

|  #  | Departman                 | Ajan Kapsamında mı? | Açıklama                                                        |
| :-: | ------------------------- | :-----------------: | --------------------------------------------------------------- |
|  1  | **Senaryo & Dramaturji**  |         ✅          | Beat sheet, kanca analizi, eylem/süre oranı, diyalog alt metni  |
|  2  | Sinematografi & Prompt    |         ⛔          | _Sahip tarafından promptlarla yürütülür_                        |
|  3  | Devamlılık & Çapalama     |         ⛔          | _Sahip tarafından promptlarla yürütülür_                        |
|  4  | Ses Tasarımı & Müzik      |         ⛔          | _Sahip tarafından promptlarla yürütülür_                        |
|  5  | Kurgu & Teknik Yönetim    |         ⛔          | _Sahip tarafından promptlarla yürütülür_                        |
|  6  | **Kalite Güvencesi (QA)** |         ✅          | BinEval ikili puanlama, `rapor_kontrol.py` doğrulaması          |
|  7  | **Dağıtım & Büyüme**      |         ✅          | YT / TikTok A/B testleri, viral analiz, retention optimizasyonu |

---

# 2. MEVCUT VE HAZIR AÇIK KAYNAK SKİLL'LER

## 2.1 smixs/creative-director-skill

```
npx skills add smixs/creative-director-skill
```

| Alan      | Değer                    |
| --------- | ------------------------ |
| Lisans    | CC BY 4.0 (atıf zorunlu) |
| Departman | 1 · Senaryo & Dramaturji |
| Uyumluluk | Claude Code / Cursor     |

SIT, TRIZ, Yanal Düşünme ve bisosrasyon metodolojileriyle senaryo kancası ve
McKee dramaturjisi kurgular. **571 ödüllü kampanya kütüphanesi** ve duygu
hiyerarşisi matrisi ile açılış kancasındaki izleyici tutundurma oranlarını
üst seviyeye çıkarır.

**Ne işe yarar (depodaki karşılık):**

- `yeni-film` (Kart A) aşamasında konsept ve hook fikirlerini zenginleştirme
- `HOOK_VE_ILK_SAHNE_KILAVUZU.md` ile birlikte çalışarak dramatik ironi ve
  kanca tipolojisi kurgulama
- `ONERME_VE_NOVUM_KILAVUZU.md`'deki novum tipi ve taşıyıcı satırı testleri
  için kreatif girdi üretme

## 2.3 smixs/skill-conductor

```
github.com/smixs/skill-conductor
```

| Alan      | Değer                            |
| --------- | -------------------------------- |
| Lisans    | MIT                              |
| Departman | 6 · Kalite Güvencesi             |
| Uyumluluk | Claude Code CLI / Python runtime |

BinEval ikili puanlama sistemiyle metinsel çıktıları **kalibre edilmiş
yargıç modeller** üzerinden kaliteden geçirir. QA akışında
`rapor_kontrol.py` ile birlikte çalışabilir.

**Ne işe yarar (depodaki karşılık):**

- `qa-isle` (Kart C-F) akışında rubrik çıktılarının bağımsız denetçi
  model tarafından doğrulanması
- `RAPOR_KONTROL/rapor_kontrol.py` ile birlikte QA raporlarının
  n·Σ·ort yeniden hesabı ve tally kontrolü

## 2.4 coreyhaines31/marketingskills

```
npx skills add coreyhaines31/marketingskills
```

| Alan      | Değer                        |
| --------- | ---------------------------- |
| Lisans    | MIT                          |
| Departman | 7 · Dağıtım & Viralite       |
| Uyumluluk | Claude Code / Codex / Cursor |

**46+ pazarlama becerisi** içerir. Sosyal medya retention analizi,
YouTube/TikTok başlık/kapak A/B testleri ve virallik optimizasyonu sunar.

> Depodaki mevcut durum: `social`, `ab-testing`, `content-strategy`
> skill'leri zaten `skills-lock.json`'da kurulu.

**Ne işe yarar (depodaki karşılık):**

- `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` ile başlık/açıklama üretimi
- `YOUTUBE_VIRAL_SANS_KILAVUZU.md`'deki VİRAL KART ve 7/14/28 gün
  ölçüm döngüsü
- `yayin-takip` (Kart Y) akışında `once → 24 → 48 → 72 → geri-besleme`
  döngüsünün veri kaynağı

---

# 3. ENTEGRASYON VE RİSK YÖNETİM MATRİSİ

Dışarıdan entegre edilen açık kaynak becerilerin stüdyonun özgün kuralları
olan **Negatif Çekirdek** ve depo standartları ile çelişmesini önlemek
amacıyla koruma mekanizmaları.

## 3.1 Koruma Kuralları

```
Kural 1 ─ ÇIKTI FİLTRESİ
    Dış skill'lerden dönen ham metinler doğrudan film dosyasına
    yazılmaz; depo iskeletine oturtulur ve yasaklar eklenir.

Kural 2 ─ PROMPT-KONTROL ZORUNLULUĞU
    Hiçbir dış skill çıktısı, prompt-kontrol (Kart P) koşulmadan
    üretime girmez. Negatif çekirdek, metin yasağı, süre/klip
    ızgarası ve SPEC zorunluluğu aynen geçerlidir.

Kural 3 ─ PUANLAMA KAPILARI
    skill-conductor yaklaşımında BinEval ikili kontrol →
    her çıktı bağımsız denetçi modeller tarafından doğrulanır.
```

## 3.2 Risk Matrisi

| Risk Kategorisi                  | Potansiyel İhlal                                                                                                        | Ciddiyet  | Önleme Mekanizması                                                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Senaryo Kuralı Çelişkisi**     | Dış skill'in deponun dramaturji kurallarını (negatif çekirdek, tema mühendisliği, novum tipi) atlayarak içerik üretmesi | 🔴 Yüksek | Skill çıktısı `KILAVUZ_REHBERI.md` §5 negatif çekirdeğe ve `ONERME_VE_NOVUM_KILAVUZU.md` kabul testlerine karşı koşulur |
| **Hook / Retention Uyumsuzluğu** | `creative-director-skill`'in ürettiği kanca yapısının deponun 1.6 s kanca süresi ve dramatik ironi kuralıyla çelişmesi  | 🟠 Orta   | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` §3.1 dramatik ironi kontrolü; depo kuralı kazanır                                       |
| **Vuruş Haritası Sapması**       | `fountain`'ın hesapladığı eylem/diyalog oranının deponun sahne doluluğu eşikleriyle uyuşmaması                          | 🟡 Düşük  | `SAHNE_DOLULUGU_KILAVUZU.md` eşikleri referans alınır; araç ölçüm yapar, karar kılavuzundur                             |
| **Pazarlama Dili Sızması**       | `marketingskills`'in Türkçe olmayan veya depo standardı dışı başlık/açıklama üretmesi                                   | 🟠 Orta   | Çıktı `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` formatına ve `apexaic/<platform>/PAKETLEME_SABLONU.md` şablonuna oturtulur   |
| **Telif ve Referans İhlali**     | Yetkisiz marka logosu veya telifli amblemlerin senaryo metnine sızması                                                  | 🔴 Yüksek | `REFERANS_PAKETI_KILAVUZU.md` doğrulaması; onaylı amblem kütüphanesi dışındakilerin negatif çekirdeğe eklenmesi         |

---

# 4. DEPODAKI MEVCUT DURUM VE BOŞ ALANLAR

| Departman           | Depodaki Mevcut Araç                     | Kurulu Skill                               | Eksik / Araştırılacak                                                |
| ------------------- | ---------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| 1 · Yazım / Konsept | `yeni-film` (Kart A sarmalayıcısı)       | —                                          | `creative-director-skill` (dramaturji), `fountain` (senaryo analizi) |
| 6 · Kalite Kontrol  | `qa-isle` (Kart C-F), `rapor_kontrol.py` | `qa-isle`                                  | `skill-conductor` (BinEval yargıç model)                             |
| 7 · Paketleme       | `VIRAL_BASLIK`, `PAKETLEME_VE_VAAT`      | `social`, `ab-testing`, `content-strategy` | Shorts viral analizörü                                               |

---

# 5. SONUÇ

Bu belge, `creative-director-skill` ve `fountain` gibi senaryo/dramaturji
odaklı ajan becerilerinin, `skill-conductor` kalite kapısı ve
`marketingskills` dağıtım optimizasyonu ile birlikte çalışarak film
yazım sürecini güçlendirmesini hedefler.

Video, görsel, ses üretimi ve teknik kurgu katmanları sahip tarafından
promptlarla yürütüldüğü için bu belgede yer almaz.

> ⛔ **Depo kuralı hatırlatması:** Bu belgedeki hiçbir dış skill çıktısı,
> `prompt-kontrol` (Kart P) koşulmadan film dosyasına girmez.
> Negatif çekirdek, metin yasağı, süre/klip ızgarası ve SPEC
> zorunluluğu aynen geçerlidir (`SKILL_KULLANIM_KILAVUZU.md` §0).

coreyhaines31
marketingskills
Repository navigation
Code
Issues
39
(39)
Pull requests
75
(75)
Agents
Discussions
Actions
Projects
Security and quality
Insights
coreyhaines31
marketingskills
Public
Go to file
t
T
coreyhaines31claude
coreyhaines31
and
claude
feat: ai-seo 2.5.0 — ChatGPT 5.6 format-volatility guidance (#579)
5b2c000
·
2 weeks ago
Name
.claude-plugin
feat: ai-seo 2.5.0 — ChatGPT 5.6 format-volatility guidance (#579)
2 weeks ago
.github
ci: auto-tag + GitHub Release on version bump
last month
scripts
feat: partners.json single source + sync script
last month
skills
feat: ai-seo 2.5.0 — ChatGPT 5.6 format-volatility guidance (#579)
2 weeks ago
tools
feat: publish Ploy as a live Skill Partner (Website) (#577)
3 weeks ago
.gitignore
fix: unpublish Converly until payment clears (#571)
3 weeks ago
AGENTS.md
fix: relabel release 2.9.0 -> 2.8.1 and document versioning convention (
2 months ago
CLAUDE.md
chore: add repo essentials and GitHub templates
8 months ago
CONTRIBUTING.md
docs: tools/PARTNERS.md — canonical partner-program rules & boundaries
last month
LICENSE
chore: add repo essentials and GitHub templates
8 months ago
README.md
feat: publish Ploy as a live Skill Partner (Website) (#577)
3 weeks ago
VERSIONS.md
feat: ai-seo 2.5.0 — ChatGPT 5.6 format-volatility guidance (#579)
2 weeks ago
partners.json
fix: ploy category → canonical grid name (#578)
3 weeks ago
validate-skills-official.sh
feat: add official skills-ref validation script
7 months ago
validate-skills.sh
feat: v2.0 skill renames and CRO consolidation (#291)
4 months ago
Repository files navigation
README
Contributing
MIT license
Marketing Skills for AI Agents
A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the Agent Skills spec.

Built by Corey Haines. Need hands-on help? Check out Conversion Factory — Corey's agency for conversion optimization, landing pages, and growth strategy. Want to learn more about marketing? Subscribe to Swipe Files. Want to get dangerously good at using AI for marketing? Check out AI Marketing Training. Want an autonomous AI agent that uses these skills to be your CMO? Try Magister.

New to the terminal and coding agents? Check out the companion guide Coding for Marketers.

Contributions welcome! Found a way to improve a skill or have a new one to add? Open a PR.

Run into a problem or have a question? Open an issue — we're happy to help.

Partners
The library is free and MIT-licensed. Verified Partners fund the work — vetted, disclosed tool integrations, listed alongside the neutral options and never influencing what the core skills recommend. The full rules and boundaries are in tools/PARTNERS.md. Become a partner →

◆ Converly — Conversion tracking / attribution. Server-side conversion tracking that fires when someone submits a form, books a meeting, or starts a chat — passing click IDs and identifiers for Enhanced Conversions (Google) and high EMQ match rates (Meta), across 100+ tools. CLI + MCP so your agent sets it up in minutes. → Integration guide

◆ Ploy — AI website & growth platform. AI marketing platform built around a Webflow-grade website builder — site optimization, SEO/AEO, visitor identification, and ad creative in one, with WebMCP to expose site actions to AI assistants. → Integration guide

What are Skills?
Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.

How Skills Work Together
Skills reference each other and build on shared context. The product-marketing skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

                            ┌──────────────────────────────────────┐
                            │          product-marketing           │
                            │    (read by all other skills first)  │
                            └──────────────────┬───────────────────┘
                                               │
    ┌──────────────┬─────────────┬─────────────┼─────────────┬──────────────┬──────────────┐
    ▼              ▼             ▼             ▼             ▼              ▼              ▼

┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│ SEO & │ │ CRO │ │Content & │ │ Paid & │ │ Growth & │ │ Sales & │ │ Strategy │
│ Content │ │ │ │ Copy │ │Measurement │ │Retention │ │ GTM │ │ │
├──────────┤ ├──────────┤ ├──────────┤ ├────────────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│seo-audit │ │cro │ │copywritng│ │ads │ │referrals │ │revops │ │mktg-ideas │
│ai-seo │ │signup │ │copy-edit │ │ad-creative │ │free-tools│ │sales-enable │ │mktg-psych │
│site-arch │ │onboarding│ │cold-email│ │ab-testing │ │churn- │ │launch │ │customer- │
│programm │ │popups │ │emails │ │analytics │ │ prevent │ │pricing │ │ research │
│schema │ │paywalls │ │social │ │ │ │community │ │competitors │ │ │
│content │ │ │ │video │ │ │ │lead-magnt│ │comp-profile │ │ │
│aso │ │ │ │image │ │ │ │co-mktg │ │directory │ │ │
│ │ │ │ │sms │ │ │ │ │ │prospecting │ │ │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └─────┬──────┘ └────┬─────┘ └──────┬──────┘ └─────┬─────┘
│ │ │ │ │ │ │
└────────────┴─────┬──────┴──────────────┴─────────────┴──────────────┴──────────────┘
│
Skills cross-reference each other:
copywriting ↔ cro ↔ ab-testing
revops ↔ sales-enablement ↔ cold-email
seo-audit ↔ schema ↔ ai-seo
customer-research → copywriting, cro, competitors
See each skill's Related Skills section for the full dependency map.

Available Skills
Skill Description
ab-testing When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program....
ad-creative When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad...
ads When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X,...
ai-seo When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers....
analytics When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions...
aso When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO...
attribution When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an...
churn-prevention When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or...
co-marketing When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use...
cold-email Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails,...
community-marketing Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a...
competitor-profiling When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions...
competitors When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when...
content-strategy When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also...
copy-editing When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the...
copywriting When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages,...
cro When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage,...
customer-research When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer...
directory-submissions When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for...
emails When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email...
events When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows,...
free-tools When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or...
image When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product...
influencer-marketing When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and...
launch When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user...
lead-magnets When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the...
marketing-council When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by...
marketing-ideas When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the...
marketing-loops When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a...
marketing-plan When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use...
marketing-psychology When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when...
offers When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing,...
onboarding When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also...
paywalls When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use...
popups When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also...
pricing When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions...
product-marketing When the user wants to create or update their product marketing context document. Also use when the user mentions...
programmatic-seo When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions...
prospecting When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or...
public-relations When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy...
referrals When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy....
revops When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes....
sales-enablement When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also...
schema When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user...
seo-audit When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO...
signup When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the...
site-architecture When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal...
sms When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts,...
social When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram,...
video When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use...
Installation
Option 1: CLI Install (Recommended)
Use npx skills to install skills directly:

# Install all skills

npx skills add coreyhaines31/marketingskills

# Install specific skills

npx skills add coreyhaines31/marketingskills --skill cro copywriting

# List available skills

npx skills add coreyhaines31/marketingskills --list
The CLI detects which agents you have installed and asks where to install. For Claude Code it installs into .claude/skills/; universal agents share .agents/skills/.

Tip

If you run the command from inside an agent session (e.g., asking Claude Code to install the skills for you), the CLI runs non-interactively and may only install to the universal .agents/skills/ directory, which Claude Code does not read. Pass the agent explicitly:

npx skills add coreyhaines31/marketingskills -a claude-code
Option 2: Claude Code Plugin
Install via Claude Code's built-in plugin system:

# Add the marketplace

/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills

/plugin install marketing-skills
Option 3: Clone and Copy
Clone the entire repo and copy the skills folder:

git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/\* .agents/skills/
Option 4: Git Submodule
Add as a submodule for easy updates:

git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
Then reference skills from .agents/marketingskills/skills/.

Option 5: Fork and Customize
Fork this repository
Customize skills for your specific needs
Clone your fork into your projects
Option 6: SkillKit (Multi-Agent)
Use SkillKit to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):

# Install all skills

npx skillkit install coreyhaines31/marketingskills

# Install specific skills

npx skillkit install coreyhaines31/marketingskills --skill cro copywriting

# List available skills

npx skillkit install coreyhaines31/marketingskills --list
Upgrading from v1.x to v2.0
v2.0 renames 17 skills and consolidates page-cro + form-cro into a single cro skill. If you installed the v1.x skills, you'll have stale old-name folders in your install directory after upgrading — the new skills install alongside the old ones, so you'll see both skills/page-cro/ and skills/cro/, etc. Clean them up:

# From the directory where you installed the skills (e.g., .agents/skills/ or .claude/skills/)

rm -rf page-cro form-cro \
 ab-test-setup analytics-tracking aso-audit competitor-alternatives \
 email-sequence free-tool-strategy launch-strategy onboarding-cro \
 paid-ads paywall-upgrade-cro popup-cro pricing-strategy \
 product-marketing-context referral-program schema-markup \
 signup-flow-cro social-content
Then reinstall the v2.0 skills via your usual method (e.g., npx skills add coreyhaines31/marketingskills).

Migrate the product marketing context file
In v2.0 the context file moved from .claude/ to .agents/ and was renamed from product-marketing-context.md to product-marketing.md. Move your existing context file:

mkdir -p .agents

# v2.0 file (or pre-v2.0 file with new name)

mv .claude/product-marketing.md .agents/product-marketing.md 2>/dev/null

# pre-v2.0 file with legacy name

mv .claude/product-marketing-context.md .agents/product-marketing.md 2>/dev/null
Skills will still check .claude/ and the legacy product-marketing-context.md filename as fallbacks, so nothing breaks if you don't migrate.

Full rename map
Old New
ab-test-setup ab-testing
analytics-tracking analytics
aso-audit aso
competitor-alternatives competitors
email-sequence emails
form-cro merged into cro
free-tool-strategy free-tools
launch-strategy launch
onboarding-cro onboarding
page-cro cro
paid-ads ads
paywall-upgrade-cro paywalls
popup-cro popups
pricing-strategy pricing
product-marketing-context product-marketing
referral-program referrals
schema-markup schema
signup-flow-cro signup
social-content social
Usage
Once installed, just ask your agent to help with marketing tasks:

"Help me optimize this landing page for conversions"
→ Uses cro skill

"Write homepage copy for my SaaS"
→ Uses copywriting skill

"Set up GA4 tracking for signups"
→ Uses analytics skill

"Create a 5-email welcome sequence"
→ Uses emails skill
You can also invoke skills directly:

/cro
/emails
/seo-audit
Skill Categories
Conversion Optimization
cro - Pages and forms
signup - Registration flows
onboarding - Post-signup activation
popups - Modals and overlays
paywalls - In-app upgrade moments
Content & Copy
copywriting - Marketing page copy
copy-editing - Edit and polish existing copy
cold-email - B2B cold outreach emails and sequences
emails - Automated email flows
social - Social media content
image - AI image generation, design tools, and optimization
SEO & Discovery
seo-audit - Technical and on-page SEO
ai-seo - AI search optimization (AEO, GEO, LLMO)
programmatic-seo - Scaled page generation
site-architecture - Page hierarchy, navigation, URL structure
competitors - Comparison and alternative pages
schema - Structured data
Paid & Distribution
ads - Google, Meta, LinkedIn ad campaigns
events - Webinars, conferences, sponsorships, speaking
ad-creative - Bulk ad creative generation and iteration
social - Social media scheduling and strategy
Measurement & Testing
analytics - Event tracking setup
ab-testing - Experiment design
Retention
churn-prevention - Cancel flows, save offers, dunning, payment recovery
Growth Engineering
co-marketing - Partner identification and joint campaigns
free-tools - Marketing tools and calculators
referrals - Referral and affiliate programs
Strategy & Monetization
marketing-ideas - 140 SaaS marketing ideas
marketing-psychology - Mental models and psychology
launch - Product launches and announcements
pricing - Pricing, packaging, and monetization
Sales & RevOps
revops - Lead lifecycle, scoring, routing, pipeline management
sales-enablement - Sales decks, one-pagers, objection docs, demo scripts
Contributing
Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

See CONTRIBUTING.md for guidelines on adding or improving skills.

License
MIT - Use these however you want.

Vercel OSS Program
About
Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

marketing-skills.com
Topics
Resources
Readme
MIT license
Contributing
Contributing
Activity
Stars
51.0k stars
Watchers
421 watching
Forks
7.7k forks
Report repository
Releases
45
(45)
v2.11.1 — ai-seo (2.4.0 → 2.5.0): new references/format-volatility.md — the citation-format volatil…
Latest
2 weeks ago

- 44 releases
  Sponsor this project
  @coreyhaines31
  coreyhaines31Corey Haines

buymeacoffee.com/coreyhaines
Learn more about GitHub Sponsors
Packages
No packages published
Contributors
24
(24)
@coreyhaines31
@claude
@njcameron
@Jiliac
@basseko
@bensabic
@CoopahG
@dgalarza
@berset
@marfert
@abhibavishi
@piersonmarks
@polnikale
@Ray0907

- 10 contributors
  Languages
  JavaScript
  93.9%
  HTML
  4.6%
  Shell
  1.5%

smixs
skill-conductor
Repository navigation
Code
Issues
1
(1)
Pull requests
1
(1)
Agents
Actions
Projects
Security and quality
Insights
smixs
skill-conductor
Public
Go to file
t
T
smixs
smixs
Update README.md
3c21d2f
·
last month
Name
.claude-plugin
chore: bump plugin version to 3.2.0
last month
assets
docs: add banner to README header
2 months ago
skills/skill-conductor
feat: evidence-based upgrade — form-matching, judge calibration, pres…
last month
.gitignore
chore: gitignore **pycache**
2 months ago
LICENSE
Initial release: Skill Conductor v1.0
7 months ago
README.md
Update README.md
last month
Repository files navigation
README
MIT license
Skill Conductor

Skill Conductor
A skill that creates, evaluates, and improves other skills. Meta-level.

Release License: MIT Install Claude Code

Architecture-first skill lifecycle: design → build → test → evaluate → package.

Most skill tools jump straight to "write SKILL.md." Conductor makes you choose the architecture first — because rewriting a wrong pattern costs more than writing it right.

Install

# skills.sh — installs into ~/.claude/skills

npx skills add smixs/skill-conductor

# Claude Code plugin

/plugin marketplace add smixs/skill-conductor
/plugin install skill-conductor@smixs
v3.2.0 — Evidence-based upgrade: form-matching, judge calibration, pressure testing
v3.1.0 — Gated self-update: held-out gate + edit budget (SkillOpt core)
v3.0.0 — BinEval scoring, English canon, dual-channel install
v3: SOP practices + smoke tests
v2: Anthropic's eval engine meets architecture-first design
Synthesized from
Anthropic Skill Creator — eval infrastructure, grader/comparator/analyzer agents, benchmark pipeline
The Complete Guide to Building Skills for Claude — architecture patterns, success metrics
Superpowers / writing-skills by Jesse Vincent — TDD approach, the "description trap" discovery, match-the-form-to-the-failure, the micro-test protocol, pressure scenarios and rationalization tables
Skills Best Practices by Minko Gechev — three-stage LLM validation, eval methodology
hamelsmu/evals-skills by Hamel Husain — critique-before-verdict judge outputs, borderline few-shot examples, judge calibration discipline
grafana/skills — skill-authoring — the pushy description pattern in production, judge score-variance discipline ("three consecutive local passes before shipping")
softaworks/agent-toolkit — skill-judge — the Expert/Activation/Redundant knowledge-delta taxonomy, directive loading triggers, the freedom-consequence test
neolabhq/context-engineering-kit — threshold-blind judges (never tell the judge the bar)
trailofbits/skills — skill-improver — the stop-hook pattern for unattended improvement loops (referenced, not implemented)
Methodology foundations
Standard Operating Procedures: A Writing Guide — Richard Stup, Penn State Extension. Format selection, hierarchical vs. flowchart procedures.
Procedure Writing: Principles and Practices — Wieringa, Moore & Barnes (Battelle Press, 1998). Imperative steps, removing modal weasel-words.
Toyota TWI (Training Within Industry) — the "Job Instruction" method: step → key point → why; the 5 Whys root-cause practice (Job Methods manual, The Roots of Lean).
McDonald's Operations Manual — the canonical 600+ page SOP system; checklists at the point of use. The manual itself is proprietary; it is documented in John F. Love's McDonald's: Behind the Arches.
Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement — the BinEval method behind Conductor's evaluation.
Guardrails Beat Guidance (5000+ Claude Code runs on SWE-bench) — rule polarity: helpful rules are negative constraints, harmful ones positive directives → Principle #10.
TICK: Generated Checklists Improve LLM Evaluation and Generation — checklist as spec + eval + feedback; refinement plateaus and degrades past 3–4 iterations → the 3-iteration cap.
CheckEval and Prosa — binary decomposition makes judges reproducible across model families → cross-family judge calibration.
Self-Preference Bias in Rubric-Based Evaluation — judges favor their own family even on binary rubrics → the out-of-family acceptance rule.
LLMs Cannot Self-Correct Reasoning Yet and BIG-Bench Mistake — self-correction needs an external gate; models fix errors well only when an external checker locates them → the gated self-update loop.
SkillJuror — progressive disclosure with explicit loading triggers beats both flat files and passive reference lists → directive loading rules.
SkillReducer — >60% of public skill-body text changes no agent behavior → the actionability test in Principle #9.
IFScale and Prompt Design at Scale — compliance collapses near 80 simultaneous rules; format matters less than rule count → the rule budget and MOC structure.
6 Modes
Mode What it does
CREATE Architecture selection → TDD baseline → scaffold → write → verify → refactor
IMPROVE Diagnose → eval loop → self-update loop (failing questions → targeted edits) → iterate
VALIDATE Structural checks + trigger testing + BinEval scoring
REVIEW Pass/fail quality gate for third-party skills before you install them
OPTIMIZE Auto-tune the description for accurate triggering with a train/test split
PACKAGE Validate structure + package as .skill for distribution
Architecture patterns
Choose before writing a single line:

Pattern Use when
Sequential workflow Clear step-by-step process
Iterative refinement Output improves with cycles
Context-aware selection Same goal, different tools by context
Domain intelligence Specialized knowledge beyond tool access
Multi-MCP coordination Workflow spans multiple services
Eval infrastructure
┌─────────┐
│ SKILL │
└────┬────┘
│
┌──────────┼──────────┐
│ │ │
┌────▼────┐ ┌──▼───┐ ┌───▼────┐
│ Grader │ │ A/B │ │Analyzer│
│ │ │Blind │ │ │
│assertions│ │compare│ │root │
│+ claims │ │ │ │cause │
└─────────┘ └──────┘ └────────┘
│ │ │
└──────────┼──────────┘
│
┌─────▼─────┐
│ Benchmark │
│ mean±std │
└───────────┘
Quality is scored with BinEval: binary yes/no questions per dimension, each answered with evidence; the skill passes when every critical question answers yes — not when a scalar clears a threshold.

Installation layout
skills/
└── skill-conductor/
├── SKILL.md
├── agents/
│ ├── grader.md
│ ├── comparator.md
│ ├── analyzer.md
│ └── bineval.md
├── eval-viewer/
│ ├── generate_review.py
│ └── viewer.html
├── references/
│ ├── patterns.md
│ ├── schemas.md
│ ├── sop-practices.md
│ ├── bineval-method.md
│ ├── quality-questions.md
│ ├── pressure-testing.md
│ └── runtime-setup.md
├── assets/
│ └── eval_review.html
└── scripts/
├── init_skill.py
├── eval_skill.py
├── run_eval.py
├── run_loop.py
├── improve_description.py
├── aggregate_benchmark.py
├── generate_report.py
├── package_skill.py
├── quick_validate.py
├── test_smoke.py
└── utils.py
Claude Code: the install commands above drop it into .claude/skills/. Auto-activates when the agent detects a skill-building task.

Key discovery
Never put process steps in the skill description. If your description says "exports assets, generates specs, creates tasks" — the model follows the description and skips the body. Tested experimentally.

# ✅ Good

description: Analyze design files for developer handoff. Use when user uploads .fig files.

# ❌ Bad - model follows this and ignores SKILL.md body

description: Exports Figma assets, generates specs, creates Linear tasks, posts to Slack.
License
MIT — see LICENSE.

About
Architecture-first skill lifecycle for AI agents. BinEval binary scoring with threshold-blind, cross-family-calibrated judges, gated self-update loop, pressure testing, 10 authoring principles grounded in empirical research.

t.me/aimastersme
Topics
Resources
Readme
MIT license
Activity
Stars
175 stars
Watchers
4 watching
Forks
19 forks
Report repository
Releases
3
(3)
v3.2.0 — Evidence-based upgrade: form-matching, judge calibration, pressure testing
Latest
last month

- 2 releases
  Packages
  No packages published
  Contributors
  2
  (2)
  @smixs
  smixsserge shima
  @claude
  claudeClaude
  Languages
  Python
  69.3%
  HTML
  30.7%

, smixs
creative-director-skill
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Security and quality
Insights
smixs
creative-director-skill
Public
Go to file
t
T
smixs
smixs
docs: add Creative Agency pack install command
ac06eb2
·
last month
Name
assets
docs: illustrate README with section screenshots (webp)
2 months ago
creative-director
Relicense MIT -> CC BY 4.0 with mandatory attribution
2 months ago
.mailmap
Creative Director Skill v2.0
5 months ago
LICENSE
Relicense MIT -> CC BY 4.0 with mandatory attribution
2 months ago
NOTICE
Relicense MIT -> CC BY 4.0 with mandatory attribution
2 months ago
README.md
docs: add Creative Agency pack install command
last month
README.ru.md
docs: add Creative Agency pack install command
last month
Repository files navigation
README
CC-BY-4.0 license
Creative Director Skill

There is no creativity in AI.
There are the methodologies of winners.
Креатива в AI нет. Есть методологии победителей.

🎬 Creative Director Skill
Claude Skill License: CC BY 4.0 Methods 20+ Case Library Version Website

🇷🇺 Читать на русском

cd-skill.com — full method breakdown, all 20 techniques and the pipeline
🌐 Full method breakdown, all 20 techniques and the pipeline → cd-skill.com

Created in collaboration with Paul Deadcough.

An AI creative director that generates advertising concepts using world-class methodologies, scores them against Cannes/D&AD-calibrated criteria, recursively refines until the quality threshold is reached, and calibrates every idea against a library of 571 legendary campaigns to detect saturation and ensure originality.

Not a brainstorming toy. A structured creative process that mirrors how top agencies (Droga5, Wieden+Kennedy, Mother) actually work — insight before ideas, methodology over free association, honest evaluation over flattery, calibration against the canon over invention from zero.

What's New in v2.0
571-case library with full Insight / Mechanic / Why-it-worked / Steal structure on every card
17-axis frontmatter schema — every card tagged across pattern (P01-P18), industry, format, emotion (Tier 1/2/3), budget, idea_type (Pollard 7-level), awards, and more
6 MOCs (Maps of Content) for fast lookup by pattern, emotion, format, industry, budget, and chronological index
4-point case library integration in workflow — priming before generation, originality empirical cap, RESTART case-soaking, pattern calibration before exit
3 maintenance scripts (Python via uv) — schema validation, MOC generation, graph wikilinks
Pollard 7-level idea taxonomy replacing the previous 3-level system
3-tier emotion hierarchy with 30+ specific emotion values
Activation toolkit with 9 formats and the Non-advertising vs Execution test
Pre-Mortem template before final delivery
Quality reviewed via skill-conductor: 41/50 production-grade (Discovery 7/10, Clarity 9/10, Efficiency 7/10, Robustness 8/10, Completeness 10/10).

What It Does
Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:

Pipeline: 5 phases from brief to idea — intake, insight, ideas, evaluate, articulate; phase 04 loops until the idea is strong

INTAKE — extracts the brief's DNA: product, audience, objectives, constraints + classifies the required idea level using Pollard 7-level taxonomy (business / brand / tagline / advertising / campaign / non_advertising / execution)
INSIGHT — mines consumer insights using 7 proven techniques (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
IDEATION — primes against the canon (scans 5-7 cases from the relevant MOC), then generates 8-12 ideas using 3 methods from different categories (structural × associative × disruptive), rotating between 20+ methodologies, with a Tension test on each
EVALUATE + REFINE — scores against 6 weighted criteria + HumanKind + Grey Scale, then recursively improves; Originality is capped empirically by case-library saturation (3+ canonical cases of the same mechanic → cap at 7); when stuck, RESTARTs through case-soaking (read 8-12 canonical cards, remix allowed); Pattern Calibration + Pre-Mortem before exit
ARTICULATE — outputs in a presentation-ready format (one-pager, top-3, campaign platform, or quick response)
You can also enter at any phase: jump to insight mining, evaluate an existing idea, or generate concepts from a known insight.

Why This Exists
Most AI "creative" tools generate ideas by free association — producing volume without structure. The result: hundreds of mediocre concepts that nobody can evaluate, often unknowingly recycling work that already exists.

The model returns averaged and overplayed — without insight and structure, AI runs like a production line stamping the same thing

This skill enforces the discipline that separates award-winning work from filler:

Insight-first — no ideation without a validated consumer tension
Structural methods — SIT, TRIZ, SCAMPER, Bisociation, Synectics, not "give me 10 ideas"
Empirical originality — every idea is checked against 571 real campaigns; if 3+ canonical cases use the same mechanic, originality is capped, not subjectively claimed
Honest scoring — calibrated against real Cannes winners, with anti-inflation rules
Recursive refinement — weak criteria get targeted improvement using different methods each pass
Case-soaking on plateau — when ideas plateau, the skill reads 8-12 canonical cards to re-train its sense for what a strong insight feels like; combining/remixing existing patterns is explicitly allowed (this is how Cannes-grade work is built)
Kill Your Darlings — the skill argues against its own favorite ideas to test their strength
Pre-Mortem — before delivery, simulates failure and surfaces the most likely failure modes
What's Inside
creative-director/
├── SKILL.md # Core skill — phase router + 5-phase workflow
├── assets/
│ └── output-templates.md # 4 presentation formats
├── scripts/ # Python via uv (PEP 723 inline deps)
│ ├── validate_schema.py # Frontmatter validation against tag-schema
│ ├── generate_mocs.py # Builds 6 MOCs from cards
│ └── generate_links.py # Adds Related sections (idempotent)
└── references/
├── tag-schema.md # Single source of truth — 17-axis frontmatter contract
├── idea-taxonomy.md # Pollard 7-level taxonomy
├── emotion-hierarchy.md # Tier 1/2/3 + 30+ specific emotion values
├── activation-toolkit.md # 9 activation formats + Non-ad vs Execution test
├── legendary-patterns.md # P01-P18 mechanics + Pre-Mortem template
├── methods-catalog.md # 20 creative methodologies as executable cards
├── method-selection-matrix.md # Task → method routing + rotation rules
├── insight-mining.md # 7 insight discovery techniques
├── scoring-calibration.md # Detailed rubrics + calibration anchors
├── creative-constitution.md # 3-layer evaluation system + feedback rules
├── storytelling-frameworks.md # 6 narrative frameworks for advertising
└── legendary-campaigns/ # 571-case library
├── README.md # Library guide
├── MOC-index.md # All 571 cards by year DESC
├── MOC-pattern.md # Grouped by P01–P18 (18 mechanics)
├── MOC-emotion.md # Grouped by emotion_tier (3 → 2 → 1)
├── MOC-format.md # Grouped by category (film/integrated/stunt_pr/...)
├── MOC-industry.md # Grouped by industry vertical
├── MOC-budget.md # Grouped by budget (low/medium/high)
└── cards/ # 571 individual cards (flat namespace)
└── {id}.md
Case Library
571 advertising campaigns from 1950–2025, tagged across 17 axes, with full structural analysis on every card.

571 award-winning cases inside — each card breaks down the insight, the execution, why it worked, and what to steal as method

Card structure
Each card has YAML frontmatter (17 axes — see references/tag-schema.md) + 4 sections:

Insight — the human truth the campaign exploits (one sentence)
Mechanic — what was actually executed
Why it worked — psychological / cultural / structural reason
Steal — pattern-level borrow strategy
Related — auto-generated wikilinks (pattern hub + 2 sibling cards + emotion match)
Tag schema (17 axes)
id, title, brand, agency, year, country, region, industry, pattern[] (P01–P18), category, idea_type (Pollard 7-level), involvement, channel, duration, goal[], budget, emotion[], emotion_tier (1/2/3), insight_domain, media_epoch, awards[], quality_score (HumanKind 1–10), scalability, risk.

18 patterns (P01–P18)
Format as Idea · Enemy or Conflict · Behavior Inversion · Brand as Activist · Cultural Hijack · Limitation as Power · Invisible Brand · Craft as Message · User as Co-Author · Serialization & Ritual · Absurd as Carrier · Social Experiment · Truth Telling · Product as Proof · Benefit Hyperbole · Long-form Drama · Design as Idea · Tech as Canvas

Lookup strategies

# Browse by axis — open the matching MOC

# Each line has inline-context (brand · year · format · emotion · budget · top_award)

# Filter by combination — ripgrep on frontmatter

rg -l "^budget: low$" cards/ | xargs rg -l "^emotion_tier: 3$"

# All P11 cases since 2020

rg -l "P11" cards/ | xargs rg -l "^year: 202"

# All canonical cases for QSR

rg -l "^industry: qsr$" cards/ | xargs rg -l "^quality: canonical$"
Saturation map (originality pressure)
Pattern Saturation Originality cap
P11 (Absurd as Carrier), P16 (Long-form Drama), P09 (User as Co-Author) high (>50 cases) ≤6 unless structurally new variant
P02, P10, P12, P14, P18 medium ≤7 if 3+ canonical use same mechanic
P01, P15 low room for novelty
This is empirical saturation, not subjective novelty.

Methodologies (20+)
20 methods to ideate in 6 groups — structural, association, inversion, perturbation, volume, bonus; every brief pulls one technique from different groups

Category Methods
Structural SIT/Goldenberg Templates, SCAMPER, TRIZ (10 principles), Morphological Analysis
Association Bisociation, Random Entry, Forced Connections, Synectics
Inversion Reverse Brainstorming, Worst Possible Idea, Provocation PO
Perturbation Oblique Strategies, Six Thinking Hats, Disney Creative Strategy
Volume Crazy 8s, Brainwriting 6-3-5, Starbursting
Bonus First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch
Evaluation System
6 weighted criteria — originality 0.25, strategic fit 0.20, emotion 0.20, craftability 0.15, scalability 0.10, simplicity 0.10; score 9 of 10 and human impact 7+ to advance

Three parallel scoring systems calibrated against real campaigns:

6 Weighted Criteria — Originality (0.25, empirically capped by case library), Strategic Fit (0.20), Emotional Response (0.20, Tier 1/2/3 hierarchy), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)
HumanKind Scale (Leo Burnett) — 1-10, from "Destructive" to "Changes the World"
Grey Scale (Grey Group) — 1-10, from "Toxic" to "Best in the World"
Anti-inflation rules: batch control, normal distribution enforcement, real analogues test, specificity test, time test, empirical saturation cap from case library.

Idea Taxonomy (Pollard 7-level)
Level When required Lifespan
business new venture, repositioning the entire company years
brand rebranding, brand platform — "what does the brand stand for?" 5–10+ years
tagline short phrase that crystallizes brand idea 5–10+ years
advertising central thought across all comms — recognizable without logo 3–5 years
campaign seasonal campaign, product launch, promo 3–12 months
non_advertising activation/utility/cultural object that lives without ads varies
execution one-off channel/format/mechanic days–weeks
Activation diagnostic: if brief mentions activation/stunt/utility — apply the test "remove the campaign, does it still have meaning?" → Yes = non_advertising / No = execution.

Emotion Hierarchy (Tier 1/2/3)
Tier 1 (forgettable): happy, sad, angry, afraid → score ≤ 6
Tier 2 (memorable): nostalgic, defiant, proud, ironic, etc. → score 6–8
Tier 3 (greatness): bittersweet pride, ironic sincerity, vulnerable defiance, etc. → score 8–10
Score 9+ requires Tier 3.
How Recursion Works
Generate ideas (3 methods, 8-12 ideas, primed against canon)
↓
Tension test on each idea
↓
Score top 3 (6 criteria + HumanKind + Grey, originality capped by saturation)
↓
Score ≥ 9? ──→ YES → Pattern Calibration + Pre-Mortem → Output
↓ NO
Identify weak criteria → Apply different method → Rescore
↓
Plateau? ──→ YES → RESTART via case-soaking
↓ (read 8-12 canonical cards, remix allowed)
↓ NO
Continue refinement
↓
5 passes? ──→ YES → Output best + honest assessment
Storytelling Frameworks
Story Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag's Pyramid · Monroe's Motivated Sequence · Pixar Rules · Hero's Journey (StoryBrand)

Installation
Via skills.sh — installs into any of 70+ supported agents:

npx skills add smixs/creative-director-skill # asks where to install
npx skills add smixs/creative-director-skill -g # globally, for all projects
npx skills update creative-director # update to latest
The full Creative Agency pack — creative-director, image and video in one command:

npx skills add https://skills.sh/p/nuK9jo3sTCZGB2Ul
Or manually (Claude Code):

git clone https://github.com/smixs/creative-director-skill.git
cp -r creative-director-skill/creative-director ~/.claude/skills/
After installation, restart Claude Code session (/clear or new session) to pick up the skill.

Claude Projects
Add the files to your Claude Project's knowledge base. Upload all files from creative-director/ — SKILL.md is the entry point, it references other files via [[wikilinks]].

Other AI Agents (Cursor, Windsurf, GPT, Gemini)
The skill works with any AI agent that supports structured instructions — the core logic is in markdown files, no platform lock-in. Copy the creative-director/ folder to your project or skills directory.

Maintenance Scripts
Three Python scripts (run via uv run, PEP 723 inline deps — no manual setup):

cd creative-director
uv run scripts/validate_schema.py # Validate all card frontmatter
uv run scripts/generate_mocs.py # Rebuild 6 MOCs from cards
uv run scripts/generate_links.py # Rebuild Related sections (idempotent)
Run pipeline: edit/add cards → validate → regenerate MOCs → regenerate links.

Usage Examples
Full creative cycle:

"Come up with a campaign for [brand]. Target audience: [who]. Budget: [range]. Channels: [where]."

Insight mining:

"Find a consumer insight for [category]. The brief says [context]."

Evaluate an existing idea:

"Evaluate this concept: [description]. The brief objective was [goal]."

Activation / non-advertising:

"Need a PR-stunt for [brand]. Low budget, must drive earned media in a week. Not a campaign — a one-shot activation."

Quick ideation:

"Need 5 concepts for [brand] social media posts about [topic]."

Next in the Pipeline
This skill delivers the idea and the script. To turn them into frames and footage, use the sibling repo visual-skills — two skills that pick up where this one stops: image writes art-director-grade prompts for keyframes, character sheets and storyboards (Nano Banana, GPT Image 2), video turns them into director-grade prompts for Seedance, Kling and Veo. Full chain: idea & script (this skill) → keyframes (image) → motion (video).

What It's Not For
Media planning or budget allocation
Production management
Brand identity / logo design
Final copywriting (it generates concepts, not polished copy)
Market research data collection
Brand positioning warmaps (use a dedicated positioning skill)
Limitations & Honest Notes
Auto-trigger in claude -p mode is unreliable. This is an advisory skill — when invoked through one-shot CLI, the model often answers creative briefs directly without consulting it. For consistent behavior in interactive sessions, invoke explicitly or share a detailed brief (>500 chars with structure).
571 source URLs are unverified. Library was built from public award-show indexes; verify links manually before citing in client work.
12 cards have confidence: low with verification_required: true — these should be cross-checked against external sources. The skill prefers quality: canonical cards for calibration.
Library is static. New campaigns from 2026+ are not auto-added; periodic manual extension required.
Credits
Created in collaboration with Paul Deadcough.

Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy + 7-level Taxonomy), Clayton Christensen (JTBD).

Creative Constitution based on the Voskresensky/IKRA approach.

Case library curated from D&AD, Cannes Lions, One Show, Webby, and Effie shortlists 1950–2025.

Author
Serge Shima — t.me/aimastersme · sergeshima.com · aimasters.me

License
CC BY 4.0 — use it, fork it, make better ads, commercially too. One hard rule: credit the author. Any copy or derivative — including skills assembled by AI agents from these files or the 571-case library — must keep the attribution line: Serge Shima — github.com/smixs/creative-director-skill. See LICENSE and NOTICE.

About
World-class creative director in a skill. Methodology-driven ideation (SIT, TRIZ, Lateral Thinking, bisociation) + a Cannes Lions evaluation engine, powered by a library of 571 legendary award-winning cases.

Topics
Resources
Readme
CC-BY-4.0 license
Activity
Stars
216 stars
Watchers
1 watching
Forks
53 forks
Report repository
Releases
1
(1)
v2.0 — Case library + workflow integration
Latest
5 months ago
Packages
No packages published
Contributors
2
(2)
@smixs
smixsserge shima
@claude
claudeClaude
Languages
Python
100%

yeni film akışına ekleyerek daha yarıcı hikayeli viral filmler cıkarmtk icin kulanalaım gerekli /plan planı hazırla
