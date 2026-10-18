# 📨 AJAN GÖREVLERİ — ana ajanın alt ajanlara verdiği sabit görev metinleri

> Ana ajan (Fable) alt ajan çağırırken buradaki şablonu kullanır: `{…}` alanlarını
> doldurur, başka yorum, gerekçe ya da yönlendirme EKLEMEZ. Gerekçe eklemek
> eleştirmenin bağımsızlığını bozar (ELESTIRI_PROTOKOLU §2).
>
> Ortak alanlar:
> - `{FILM}` = film klasörü (örn. `yatay_4_dk_filmler/THE_X`)
> - `{FAZ}` = faz no
> - `{TUR}` = tur no
> - `{CIKTI}` = ajanın yazacağı dosya, `{FILM}/ODA/F{FAZ}_<ajan>_{TUR}.md`
>
> **Paralel çağrı:** aynı fazın eleştirmenleri TEK mesajda birlikte çağrılır.
> Her çağrı yeni bir örnek açar; ajan önceki konuşmayı görmez.

---

## 🗺️ AJAN HARİTASI — kim, hangi fazda, neyi okur, nereye yazar

`<t>` = tur. Yol `{FILM}/` (`<FORMAT>_filmler/<FILM>/`) köküne göredir.
- **Yazar:** yalnız kendi çıktısına `Write` eder. Sonucu ana ajan (Fable) `FILM.md` / `SAHNELEME.md` / `timeline.json`'a yerleştirir.
- **Eleştirmen:** `Write` yetkisi yok. Cevabını mesajla verir; ana ajan onu aynen `ODA/F<faz>_<ajan>_<t>.md`'ye kaydeder.
- Bütün ajanlarda `Agent` yasak: alt ajan alt ajan açamaz.
- `BT` = `uretim_hatti/BILINEN_TUZAKLAR.md` · `AL` = `ARIZA_LISTESI.md` · `EP` = `ELESTIRI_PROTOKOLU.md`.

| Ajan | Model | Rol | Faz | Zorunlu okur | Yazar modunda çıktı → yerleşeceği yer |
|---|:--:|---|---|---|---|
| senarist | opus | yazar | 1 · 2 | BT · AL | `ODA/F1_senarist_<t>.md` (3 aday) · `ODA/F2_senarist_<t>.md` → FILM §1-§2 |
| diyalog-yazari | opus | yazar · eleştirmen (F4) | 2 · 4 | BT | `ODA/F2_diyalog-yazari_<t>.md` → FILM §5 + konuşma/ses profilleri |
| dramaturg | opus | eleştirmen | 1 · 2 · 8 | AL (H) · EP | — |
| izleyici | sonnet | eleştirmen | 1 · 2 · 3 · 3b · 6 · 7 · 8 · 9 | **hiçbir dosya** — yalnız görev metni ya da `~/film_medya/<FILM>/izleyici*/` kareleri (kanca) | — |
| yonetmen | opus | yazar (F3 · F3p yeniden tasarım) · eleştirmen (F1 · 3b · 6) | 1 · 3 · 3b · 3p · 6 | BT · AL | `ODA/F3_yonetmen_<t>.md` → FILM §4 |
| sahneleyici ⏸️ | opus | yazar (yalnız zincir açıkken) | 3b | BT · AL · `SABLON/SAHNELEME.md` | `ODA/F3_sahneleyici_<t>.md` → SAHNELEME §1 §2 §4 §5 + FILM §4 zincir sütunları |
| mekan-haritacisi ⏸️ | sonnet | yazar · eleştirmen (yalnız zincir açıkken) | 3b | EP · FILM §4 | `ODA/F3_mekan-haritacisi_<t>.md` → SAHNELEME §3 |
| teknik-danisman | sonnet | eleştirmen | 3 · 3b · 3p · 5 · 7 | BT · AL (T) · EP | — |
| goruntu-yonetmeni | sonnet | yazar | 3p (PILOT.md + KİMLİK CÜMLELERİ) · 5 (G01 önce) · 7 (yeniden tasarım) | BT · FILM §3-§4 · örnek grup G01 · pilot notu | `PROMPTLAR/PILOT.md` · `PROMPTLAR/<GRUP>.md` (doğrudan) |
| devamlilik | sonnet | eleştirmen (F5: 8 soru tablosu) | 3p · 5 · 7 | BT §B §C · EP · FILM §3-§4 | — |
| zincir-bekcisi ⏸️ | sonnet | eleştirmen (yalnız zincir açıkken) | 7 (7b · 7f) | BT §B · EP · SAHNELEME §2 §4 | — |
| ses-tasarimcisi | sonnet | yazar (F4) · eleştirmen (F2) | 2 · 4 | BT · FILM §4-§5 (F2'de §4 yok: tretman + §5) | `ODA/F4_ses-tasarimcisi_<t>.md` → FILM §6 (+ kayıt, efekt, ortam listeleri ODA'da) |
| besteci | sonnet | yazar (koşullu: MUZIK var) | 4 · 8 | FILM §1-§5 | `ODA/F4_besteci_<t>.md` → FILM §7 · `ODA/F8_besteci_<t>.md` (Flow Music promptu) |
| kurgucu | sonnet | yazar (F8 · hat dışı montajın timeline'ı) · eleştirmen (F3 kurgu gözü · F4) | 3 · 4 · 8 | BT §B §D · FILM §4-§5 · NOTLAR | `ODA/F8_kurgucu_<t>.md` → `timeline.json` (Bash: kurgu.py · kareler.py · medya.py) |
| kapak-tasarimcisi | opus | yazar | 6 · 9 | BT §A §C · FILM · `SABLON/KAPAK_VE_YAYIN.md` | `ODA/F6_kapak-tasarimcisi_<t>.md` → KAPAK_VE_YAYIN §1 |
| yayin | sonnet | yazar (F9) · eleştirmen (F6) | 6 · 9 | kanal şablonları · `SABLON/YAYIN_PAKETI.md` | `YAYIN_PAKETI.md` (doğrudan) |
| bilim-danismani | sonnet | eleştirmen (koşullu: FIZIK_IDDIASI var) | 2-3 (inandırıcılık) · 9 (doğrulama) | EP · web | — |
| denetci | opus | süreç denetçisi | her kapı | KABUL_LISTELERI · EP · fazın ODA dosyaları | — (Bash: `film_dogrula.py` · `kurgu.py`) |

Medya yolları (`kare/` · `ham/` · `analiz/` · `izleyici/` …): `uretim_hatti/README.md` § Medya.

---

## YAZARLAR (Write alır, yalnız {CIKTI}'ya yazar)

### senarist
```
Faz {FAZ}, tur {TUR}. Film klasörü: {FILM}.
Brif: {KONU} · format {FORMAT} · hedef süre {SURE} · karakter sayısı {KARAKTER}.
{TUR>1 ise: Önceki eserin: {ONCEKI_CIKTI}. Eleştiriler: {ELESTIRI_DOSYALARI}. Her bulguya KABUL/RED ile cevap ver.}
Görev: {F1: üç hikâye adayı | F2: seçilen aday {ADAY} için sahne sahne tretman}.
Çıktıyı yalnız şu dosyaya yaz: {CIKTI}. Başka dosyaya yazma. Sonunda dosya yolunu ve 3 satırlık özet ver.
```

### diyalog-yazari
```
Faz 2, tur {TUR}. Tretman: {FILM}/ODA/F2_senarist_{N}.md. Hedef süre: {SURE} · replik bandı: {BANT}.
Görev: akıcı diyalog — replik tablosu (çekim · saniye · konuşan · kaynak · kayıt · metin · süre) + alışveriş NEDEN satırları + konuşma ve ses profilleri.
Çıktı: {CIKTI}. Yalnız oraya yaz.
```

### yonetmen
```
Faz {FAZ}, tur {TUR}. {F1: Üretilebilirlik görüşü — adaylar: {ADAY_DOSYASI} (eleştirmen modu, Write kullanma, cevabı mesajla ver)
                       | F3: Onaylı tretman: {TRETMAN}; replikler: {REPLIK} — çekim listesi yaz}
{TUR>1 ise: önceki: {ONCEKI_CIKTI} · eleştiriler: {ELESTIRI_DOSYALARI} · KABUL/RED ile cevap ver.}
Çıktı (F3): {CIKTI}.
```

### goruntu-yonetmeni
```
Faz 5 (ya da 7 yeniden tasarım), tur {TUR}. Çekim listesi: {FILM}/FILM.md §4 (altındaki notlar bloğu dahil).
Kimlik tablosu: {FILM}/FILM.md §3 (### KİMLİK CÜMLELERİ dahil). Bu görevde yalnız şu çekimler: {CEKIMLER} (grup {GRUP}).
{G01 değilse: Örnek grup: {FILM}/PROMPTLAR/G01.md — kimlik, işaret, yazı kilidi, mekân ışığı ve ortak görünüm cümlelerini oradan birebir al.}
{Pilot koştuysa: Pilot notu: {FILM}/ODA/F3p_pilot_karar.md · pilot bölümü: {FILM}/PROMPTLAR/PILOT.md (bu gruptaki pilot çekimleri: {PILOT_CEKIMLERI}).}
{Revizyonsa: eleştiriler: {ELESTIRI_DOSYALARI} · film_dogrula DERS satırları: {DERS_SATIRLARI} — her birine KABUL/RED ya da düzelt/gerekçe.}
{F7 ise: reddedilen deneme notu: {RET_NOTU} · hatanın doğduğu yer: {YER}.}
Çıktı: {FILM}/PROMPTLAR/{GRUP}.md (prompt + Flow iş emri satırları + ## 8 SORU tablosu). Yalnız oraya yaz.
```
```
PİLOT MODU · Faz 3p. Çekim listesi: {FILM}/FILM.md §4 · kimlik tablosu: §3. Pilot çekimleri: {PILOT_CEKIMLERI} (gerekçe: {PILOT_GEREKCE}).
Görev: kendi dosyandaki "Pilot modu" — KİMLİK CÜMLELERİ (bütün referanslar) · REFERANS PROMPTLARI (yalnız pilotunkiler) · pilot çekimleri ·
FLOW İŞ EMRİ (çekim başına 2 deneme) · PİLOT SORUSU.
Çıktı: {FILM}/PROMPTLAR/PILOT.md. Yalnız oraya yaz.
```

### ses-tasarimcisi · besteci · kapak-tasarimcisi · yayin · kurgucu
```
Faz {FAZ}, tur {TUR}. Girdiler: {GIRDI_DOSYALARI}. {Faz 8 kurgucu: işaretleme: {FILM}/NOTLAR.md · tarama: {TARAMA} · kare sayfaları: {KARE_KLASORU}}
Görev: {GOREV_CUMLESI — ajanın kendi dosyasındaki "Çıktı" bölümü}.
Çıktı: {CIKTI}. Yalnız oraya yaz.
```

### sahneleyici
```
Faz 3 · adım sahneleme, tur {TUR}. Film: {FILM}. Çekim listesi: {FILM}/FILM.md §4 · KLIP_SURESI: {KLIP_SURESI}.
Yönetmenin zincir adayları: {ZINCIR_ADAYLARI veya "yok"}.
{TUR>1 ise: önceki: {ONCEKI_CIKTI} · eleştiriler: {ELESTIRI_DOSYALARI} · KABUL/RED ile cevap ver.}
Çıktı: {CIKTI} (SAHNELEME §1, §2, §4, §5 + "§4 SÜTUNLARI"). Yalnız oraya yaz.
```

### mekan-haritacisi
```
YAZAR MODU · Faz 3 sahneleme, tur {TUR}. Sahneleme taslağı: {SAHNELEYICI_CIKTI}. Çekim listesi: {FILM}/FILM.md §4.
Görev: SAHNELEME §3 mekân haritası. Çıktı: {CIKTI}. Yalnız oraya yaz.
```
```
ELEŞTİRMEN MODU · Faz 3 sahneleme, tur {TUR}. Eser: {SAHNELEYICI_CIKTI} + {HARITA_CIKTI}. KLIP_SURESI: {KLIP_SURESI}.
Her halka için mesafe/süre · 180° · görünürlük. ELESTIRI_PROTOKOLU biçimi; dosya yazma.
```

---

## ELEŞTİRMENLER (Write yok — cevabı mesaj olarak verir; ana ajan aynen {CIKTI}'ya kaydeder)

### dramaturg · teknik-danisman · devamlilik · bilim-danismani
```
Faz {FAZ}, tur {TUR}. Eleştireceğin eser: {ESER_DOSYASI}.
{TUR>1 ise: önceki bulgular: {ONCEKI_ELESTIRI} · yazarın cevapları: {CEVAPLAR} · yalnız değişen kısım: {DEGISEN}.}
uretim_hatti/ELESTIRI_PROTOKOLU.md biçimiyle eleştir (v2: YER · KANIT · ETKİ · DOĞDUĞU · KURAL · ARIZA · DÜZELTME).
Dosyanda bu faz için numaralı soru listesi varsa hepsini cevapla. Gerekçe verilmedi; yalnız eseri değerlendir.
```
```
PİLOT · Faz 3p (devamlilik kare modu · teknik-danisman pilot modu). Pilot dosyası: {FILM}/PROMPTLAR/PILOT.md.
Kareler: referans {~/film_medya/<FILM>/ref/…} · başlangıç {kare/Cxx.png} · deneme kare sayfaları {analiz/kareler/<deneme>/sayfa_NN.png}.
Sahibin işareti: {FILM}/NOTLAR.md İŞARETLEME. Kendi dosyandaki "Faz 3p" bölümüne göre cevap ver; görmediğin hareket için "görülmedi".
```
```
KURGU GÖZÜ · Faz 3, tur {TUR} (kurgucu, eleştirmen modu). Çekim listesi: {FILM}/FILM.md §4 · replikler: §5.
Kendi dosyandaki "Eleştirmen modu (faz 3 — kurgu gözü)" 7 sorusunu sırayla cevapla. Dosya yazma.
```

### zincir-bekcisi
```
MOD 1 (anahtar kareler) · Zincir {ZK}. Kareler: {~/film_medya/<FILM>/kare/Zk.0.png …}. Referanslar: {ref/…}.
Tarifler: {FILM}/SAHNELEME.md §2 · delta: §4. ELESTIRI_PROTOKOLU biçimi.
```
```
MOD 2 (dikişler) · Zincir {ZK}. Her dikiş için klasör: {~/film_medya/<FILM>/analiz/dikis/<Zk>_<i>/} (dikis_serit.png ·
dikis_fark.png · dikis.json). Kuyruk raporları: {KUYRUK_CIKTILARI}. Orta kareler: {KARE_KLASORLERI}.
Her dikişe tek karar: TAMAM · KIRP n · YENİDEN ÜRET · A′/A+ · KESMEYE ÇEVİR — kanıtıyla.
```

### izleyici — ⛔ en katı şablon
Ana ajan bu metne **hiçbir şey eklemez**:
- film adı, tür, tema, "amaç şu" gibi yönlendirme verilmez;
- dosya yolu verilmez (kare modu hariç).

```
METİN MODU
Aşağıda bir kısa filmin ekranda görünenleri sırayla yazılı. Daha fazlasını bilmiyorsun.
---
{YALNIZ "ekranda görünen" SÜTUNU, çekim sırasıyla, numarasız ya da yalnız sıra numarasıyla;
 replik varsa yalnız duyulan metin: "(ses) …"}
---
Kendi dosyandaki soruları cevapla.
```
```
KARE MODU
Şu dosyalardaki kareleri sırayla aç ve bak: {~/film_medya/<FILM>/izleyici/taslak_<n>/01.png …}.
Bunlar bir kısa filmden sırayla alınmış karelerdir. Başka hiçbir dosyayı açma.
Kendi dosyandaki soruları cevapla.
```
```
LOGLINE MODU (Faz 1)
Üç kısa film fikri:
A) {LOGLINE_A}
B) {LOGLINE_B}
C) {LOGLINE_C}
Hangisini izlerdin, hangisini geçerdin, neden? Kendi dosyandaki "fikir" sorularını cevapla.
```
```
KAPAK MODU (Faz 6 / 9)
{Faz 6: kapak tarifleri — yalnız görünen: "…" | Faz 9: dosyalar: ~/film_medya/<FILM>/izleyici/kapak/<A|B|C>/168x94_masaustu_onerilen.png ve 120x68_mobil_onerilen.png}
Kendi dosyandaki "kapak" sorularını cevapla.
```

### denetci
```
Faz {FAZ} kapısı. Film: {FILM}. Kabul listesi: uretim_hatti/KABUL_LISTELERI.md (Ö + F{FAZ}).
Fazın ODA dosyaları: {ODA_LISTESI}. Fazın eseri: {ESER}. Önceki sürüm: {ONCEKI_SURUM}.
{F5 ise: DERS uyarı cevapları: {FILM}/ODA/F5_uyari_cevaplari.md (varsa).} {FAZ ≥ 3p ise: medya.py durum <FILM> çıktısını kanıt koy.}
Her maddeye ✅/❌ + kanıt. Sonunda: KAPANABİLİR | KAPANAMAZ (mekanik: … / yargı: …).
```
