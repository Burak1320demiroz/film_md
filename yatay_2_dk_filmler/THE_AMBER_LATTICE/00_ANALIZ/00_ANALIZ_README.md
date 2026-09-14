# 🔬 00_ANALIZ — yazımdan ÖNCEKİ iş burada durur

> **Bu klasör filmin defteridir, filmin kendisi değildir.** Buradaki hiçbir
> dosya bir üretim promptu taşımaz ve hiçbiri kapı betiklerine girmez.
> Film dosyaları (`PLAN` · `BOLUM_*` · `KAPAK` · `MUZIK` · `YAYIN_PAKETI`
> · `QA_SPEC`) klasörün BİR ÜST seviyesinde, doğrudan film klasöründe durur.

**Neden ayrı bir klasör (08.09.2026 · sahip kararı):** analiz nesre yazılınca
yapılmıyordu. Bu deponun D117'de ölçtüğü şey burada da geçerli — *blok
okunmuyor, dosya okunuyor*. Okuma turu, QA hasadı, sahne sıralaması ve uyarı
notları PLAN'ın içine gömüldüğünde plan 1.200 satır oluyor ve kimse geri
dönüp bakmıyor. Ayrı dosya, görünür borçtur.

---

## Sıra — üstten aşağı, atlanmaz

| # | dosya | ne yapar | bitmeden geçilmez |
|:--:|---|---|---|
| 0 | `00_OKUMA_CIZELGESI.md` | TÜM ders + TÜM kılavuz + QA raporu okuma defteri | ⬜ kalan satır varken 1'e geçilmez |
| 1 | `01_QA_DERS_HASADI.md` | okunanlardan BU filme düşen kilitler | 0 satırla 2'ye geçilmez |
| 2 | `02_KONSEPT_VE_RISK.md` | konsept · ortam/tür kartı · risk kartları · novum kapısı | konsept kapısı ✅ olmadan 3'e geçilmez |
| 3 | `03_SAHNE_SIRALAMASI.md` | X sahnenin sırası — olay · vuruş · kurulum harfi | 4'ün girdisidir |
| 4 | `04_UYARI_NOTLARI.md` | sıralamanın tetiklediği ölçülmüş arızalar | ⛔ satırı açıkken 5'e geçilmez |
| 5 | `05_SAHNE_CALISMALARI/` | sahne başına bir dosya — konuya özel çalışma | hepsi ✅ olmadan PROMPT yazılmaz |

Beşi bittikten SONRA film yazımı başlar: `THE_AMBER_LATTICE_PLAN.md` → BIBLE → `THE_AMBER_LATTICE_BOLUM_*.md`.

---

## ⛔ Kapı betiklerine girmeme kuralı

`prompt_kontrol.py`'nin `ATLA` deseni `00_ANALIZ` içeren her yolu atlar
(08.09.2026'da eklendi). Bunun **bozulmaması** için bu klasörde:

```
⛔ "## ... SAHNE <n>" biçiminde başlık YAZILMAZ.
   Betiğin SAHNE_BASLIK deseni budur; klasör adı değişirse ya da desen
   gevşerse bu dosyalar sahne sanılır ve 05_SAHNE_CALISMALARI ayrı bir
   FİLM olarak sayılır. Sahne başlığı burada `## 🔬 S<nn> — ...` yazılır.
⛔ Satır başında "TEMA:" YAZILMAZ.
   sayac.sh'nin tema dağılımı film klasörünü ÖZYİNELEMELİ tarar; buradaki
   bir aday tema satırı gerçek temayla birlikte iki kez sayılır.
   Burada tema `▸ tema adayı — <ad>` biçiminde yazılır (iki nokta YOK).
⛔ "### 📸 GÖRSEL PROMPT" / "### 🎥 VİDEO PROMPT" başlıkları YAZILMAZ.
   Prompt yalnız bölüm dosyalarında bulunur (§2.0).
```

---

## ⛔ Boş dosya silinmez

`⬜ BEKLİYOR` satırıyla durur. Var olan boş dosya görünür borçtur;
olmayan dosya borç değil, unutmadır [§2.0].
