# 🧮 <FILM_ADI> — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> <FILM> S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon). ≤ 8 sahnelik filmde (dikey)
> bu dosya yoktur, her sahne dosya alır.
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var. Satırlar betik damgalar (`| S00 |` …); elle
> satır eklenmez/silinmez, sahne sayısı değişirse `--sahne-guncelle`.
>
> 🆕 **22.09.2026 · ÇOK KLİPLİ SAHNE** (`--sahne-plani` ile açılan yatay film): satır
> KLİP başınadır; betik başlığa iki sütun ekler ve satırları `| K07 | S03 | 2/3 · ⬜ |`
> biçiminde damgalar. **ROL n/N** sütununa kapsama şablonundaki rol yazılır (KURULUM ·
> EYLEM · TEPKİ · BELİRİŞ · MÜCADELE · TERSLİK · KARAR · BEDEL · DÖNÜŞ). Klibin
> `OLAY BAŞ → SON` hücresinin SON yarısı, aynı sahnedeki bir sonraki klibin
> `CONTINUOUS ACTION:` satırına kelimesi kelimesine iner [D207]. Aynı sahnenin
> `IŞIK · SES · FİZİK` hücreleri birebir aynıdır (sahne kilidi); "öncekiyle AYNI olamaz"
> kuralı yalnız SAHNELER ARASINDA geçerlidir. ㉚ SAHNE sütununu SAHNE PLANI'yla
> karşılaştırır. Kural: `COK_KLIPLI_SAHNE_KILAVUZU.md`.
>
> ⛔ Bu klasörde `## … SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ
> (kapı betiği o desenleri sahne/prompt sanar). Prompt yalnız bölüm dosyasında.

## Sütunlar — her hücre TEK satır, boş hücre yok ("—" yazılır)

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) | `03_SAHNE_SIRALAMASI` |
| **OLAY BAŞ → SON** | ne değişiyor: `<başta> → <sonda>`; klip içi değişim varsa `⚠️ARA` | çalışma şablonu 🎬 |
| **B5** | İSTEK / ENGEL / BEDEL / MUHATAP / AYRILIK — bu sahne hangi satırı taşıyor | `02_KONSEPT_VE_RISK` |
| **KURULUM** | harf + işaret (`B · dönüş S3`) · lens · mesafe · ölçek · açı tipi | `ACI_YAYI` §3-§4 |
| **OPTİK** | kadraj eni (m) · ana nesne (px) — ⛔ ≥100 px [D179]; sığmıyorsa `⛔` | `KILAVUZ` §5.2 hesabı |
| **IN FRAME** | face · hands · torso · legs · full body · back · none — promptun ilk satırı olur [㉖] | `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 |
| **TAŞIYICI** | devamlılık: giren/çıkan/taşınan nesne + önceki/sonraki sahne | çalışma şablonu 👤 |
| **IŞIK · SES · FİZİK** | üçü tek hücrede `·` ile; palet/ses dokusu öncekiyle AYNI olamaz | ortam kartı · `KURGU_RITMI` §2 |
| **REPLİK** | `—` ya da `<saniye> · konuşan · İŞLEV · ağız okunuyor/okunmuyor` | `DIYALOG_SAHNESI` §2-§3 |
| **KİLİT / UYARI** | bu sahneye düşen kilit(ler) D-no ile + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **İZLEYİCİ CÜMLESİ** | "bu figür ne istiyor" — seems/probably YASAK; ⭐VİRAL ise `YÜZ:` + `HAREKET:` | `OYUNCULUK_YAZIM` §1 · §3 |
| **KAPI** | ⬜ → ✅ satır tam ve optik tutuyor; ✅ olmadan o sahnenin promptu yazılmaz | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S03 · glove closes on wheel → wheel stopped, strap slack ·  ENGEL  ·  B · dönüş S1 · 35mm · 1,6 m · MCU · eye level
    · 1,1 m · 340 px  ·  hands, torso  ·  strap in (S02) / out (S05)  ·  neutral ceiling · hum + warble · 0,25 g
    · —  ·  D200 · D216 · U-4  ·  he wants the wheel to move, not to understand it  ·  ✅
```

---

## 📋 TABLO

| S | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|---|:--:|---|---|---|---|---|---|---|---|:--:|
