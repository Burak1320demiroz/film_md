# QA × prompt analizi — yeni hattın 5 filmi (16.10.2026)

> **Ne:** yeni hatla yazılan beş filmin ham QA raporundaki her bulgunun, o çekimin Görsel ve Video promptuyla birebir karşılaştırılması.
> Beş ajanla yapıldı, film başına bir ajan; görev metni `GOREV.md`.
> Sınıflama sözleşmesi `uretim_hatti/QA_OKUMA_KILAVUZU.md` §1 v1.0; 06.10'daki eski hat analiziyle (`../qa_prompt_analizi_20261006/`) aynı.
>
> **Durum:** metin ajanların yazdığı gibidir; düzenlenmez. Sentez ve dersler `../16_QA_PROMPT_DERSLERI_20261016.md`'dedir.
> `GOREV.md`'deki yazma yolu o oturumun scratchpad klasörüdür; dosyalar oradan buraya kopyalandı.

| Dosya | Film | Ham satır → tekil | 🅐 | 🅑 | 🅑+ | 🅒 | 🅓 | 🅑 oranı |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `THE_WRONG_BURN.md` | 2 dk, tam ajanlı döngü | 84 → 48 | 14 | 14 | 7 | 12 | 1 | 21/35 = %60 |
| `THE_PLANET_THIEF.md` | 4 dk, sahibin planı | 89 → 66 | 10 | 32 | 16 | 8 | 0 | 48/58 = %83 |
| `THE_MAYDAY_SEA.md` | 4 dk, model sesi | 63 → 47 | 15 | 9 | 11 | 8 | 4 | 20/35 = %57 |
| `THE_SKY_CATCH.md` | 4 dk (montaj ~2:41) | 83 → 64 | 14 | 21 | 19 | 6 | 4 | 40/54 = %74 |
| `THE_FURNACE_GATE.md` | 16 dk, yalnız 2. parça C25-C48 | 71 → 44 | 9 | 18 | 5 | 12 | 0 | 23/32 = %72 |
| **toplam** | | **390 → 269** | **62** | **94** | **58** | **46** | **9** | **152/214 = %71** |

🅑 oranı = (🅑 + 🅑+) / (🅐 + 🅑 + 🅑+), sözleşme v1.0, sınıf sütunu.

**Okumadan önce:**
- 269 bulgunun hiçbiri insan gözüyle doğrulanmadı. Bütün sınıflar geçicidir.
- Beş filmin hiçbirinde hangi denemenin ve hangi referansın kullanıldığı kayıtlı değil (NOTLAR DENEMELER boş, `~/film_medya/<FILM>/` boş).
  Prompt sürümü içerikten çıkarıldı; PLANET_THIEF'te belirlenemedi.
- QA numaraları her filmde plan numarası değildir:
  - MAYDAY: montajda hat C05 yok, rapordaki C05… = hat C06….
  - SKY_CATCH: numaralar Gemini'nin kendi kesme sayımı; 5 plan çekimi montajda yok.
  - Analizler hat/plan numarasıyla yazıldı.
