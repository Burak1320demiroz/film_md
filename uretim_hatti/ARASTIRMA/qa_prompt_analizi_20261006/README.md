# QA × prompt analizi — 12 film (06.10.2026)

> **Ne:** 12 filmin ham QA raporlarındaki (geçersizler dahil) her 🔴/🟠 bulgunun, o sahnenin görsel ve video promptuyla karşılaştırılması.
> 6 sonnet ajanla yapıldı (görev metni: `GOREV.md`).
>
> **Nerede duruyordu:** yalnız oturum klasöründe. 07.10.2026'da sahip kararıyla buraya alındı. Metin olduğu gibidir; düzenlenmez.

| Dosya | İçerik |
|---|---|
| `GOREV.md` | ajanlara verilen görev ve sınıf sözlüğü (🅐 · 🅑 · 🅑+ · 🅒 · 🅓) |
| `<FILM>.md` (12) | film başına bulgu tablosu: rapor · zaman · sahne · bulgu · prompt alıntısı · hüküm · kapanma |
| `OZET_topla.txt` | `araclar/topla.py` çıktısı: hüküm, tür ve kapanma dağılımı |
| `korpus.json` · `araclar/korpus_say.py` | 773 ham rapor · 2.049 🔴/🟠 satırı · geçersiz rapor payı |
| `prompt_denetim.json` · `denetim_cikti.txt` · `araclar/prompt_denetim.py` | 50 film · 2.913 prompt üzerinde mekanik kalıp sayımı (NEGATIVE payı, çelişen özellikler, "Scene n of N" …) |
| `araclar/rules.py` · `locks.py` · `show.py` | yardımcı betikler (yollar oturum klasörüne göre yazılı) |

**Ana sayılar (06.10.2026):**
- 698 tekil bulgu;
- gerçek kusurun %56'sı prompta bağlı (248/443);
- %31 QA yanılgısı;
- 🔴/🟠 satırların %56'sı "geçersiz" raporlardan;
- NEGATIVE bloğu promptun ortalama %40'ı;
- "real skin pores" + "No bare skin" 19 filmde 784 promptta;
- "Scene n of N" 37 filmde.

**Kullanan:** `uretim_hatti/PROMPT_HATA_ATLASI.md` · `uretim_hatti/QA_OKUMA_KILAVUZU.md` · süzme `../04_SUZME_20261007.md`.

⚠️ 05.10.2026'daki 49 filmlik analizle sayılar karşılaştırılamaz:
- o analiz "ölümcül hatanın ~%17'si prompt metninden" dedi ve hatanın doğduğu yere göre sınıfladı;
- bu analiz prompt boşluğu ve davetine göre sınıflıyor.

Tek sınıflama sözleşmesi: `QA_OKUMA_KILAVUZU.md`.
