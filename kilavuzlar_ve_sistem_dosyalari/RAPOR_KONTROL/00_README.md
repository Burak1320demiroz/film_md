# 🧮 RAPOR KONTROL — QA raporunun çıktı kapısı

> `prompt_kontrol.py` girdiyi (promptu) denetler; **bu betik çıktıyı (raporu)**.
> 01.09.2026'ya kadar çıktı tarafında tek satır kod yoktu; AGENTS ortak adımları
> aynı kontrolleri prose olarak taşıyordu ve bir partide altı raporun beşi kendi
> aritmetik kapısından geçemedi [D161]. Betik koşulmadan T tablosuna satır yazılmaz.

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
        <rapor.md> [<rapor.md> ...] [--film <film klasörü>] [--hook 10] [--klip 10] [--rapor] \
        [--olcum-kesme <n>] [--olcum-sahne <n>]     # ⑪ ölçümü hakem yapar
```

| ne ölçer | kaynak |
|---|---|
| SPEC var + ①/④/⑥ mod V → TEKRAR | D129 |
| n · Σ · Σ/n hücrelerden; iddiayla kıyas · "no in-scope source"+sayı → `—` · 0 replikte diyalog-yalnız hücre → N/A | D131 · D161 |
| SEVERITY TALLY ↔ yazılı 🔴🟠🟡 (timecode ile tekilleştirilmiş) | D161 |
| şerit uzunluğu = kesme+1 · ④ harita ↔ kesme sayısı (film boyu hücreler düşer) | D118 · D121 |
| kesme zaman kodları planın ızgarasına oturuyor mu (⑨) | D115 |
| SPEC sayaç yazarken ② "Counter N/A" → ölçüm boşluğu | D134 |
| birden çok rapor: kesme · sahne · şerit · replik · ⭐ SUSKUNLUK (film boyu iddia ↔ sahibin sessizliği) | D107 · D162 |
| `--bolum n/m` (6/8/16 dk): ①.9 yalnız o parçanın bölüm dosya(lar)ını sayar — k dosya / m parça tam bölünüyorsa parça n = dosyalar (n−1)k/m+1…nk/m (16 dk: 8/4 → 2 dosya; 8 dk 4×12 yazımı: 4/2 → 2 dosya), bölünmüyorsa uyarı + yalnız BOLUM_n (MARS 3×12↔2) · ①.11 maske BAŞ/ORTA/SON | §2.6 · §2.7 · §2.8 (19.09.2026) |

---

## 🔎 prompt_hata_analizi.py — ham bulgu × PROMPT METNİ [18.09.2026]

`rapor_kontrol.py` raporun KENDİ aritmetiğini denetler; bu betik raporun bulgusunu
**o sahnenin promptuna** bağlar ve kusurun sahibini sorar (🅐 model sapması /
🅑 prompt boşluğu). ⑬ UYUM merceğinin retrospektif hâlidir — ⑬ hiç koşmadığı için
(`FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` boş) arşiv bu betikle okundu.

```
python3 .../RAPOR_KONTROL/prompt_hata_analizi.py --ozet            # kapsam
                                                --film <FILM>      # tek film defteri
                                                --kilit <FILM>     # çekirdek cümle envanteri
                                                --sahne <FILM> <n> # promptun kendisi
                                                --regex-dene "<d>" # kapı önerisi ölçümü
                                                --yaz              # 10_ klasörüne defter
```

`rapor_kontrol`'ün yardımcılarını (`govde_al` · `alan` · `mercek_bul` · `skor_tablosu` ·
`kesik_mi`) içe alır. ⛔ `--yaz` verilmedikçe **dosya yazmaz**.
Çıktısı: `../FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/`

**Çıkış:** 0 GO · 1 ŞARTLI · 2 TEKRAR/GEÇERSİZ/✂️ KESİK. `--rapor` → `RAPORLAR/<FILM>_<tarih>_RAPOR_KONTROL.md`.

> ✂️ **KESİK (14.09.2026 · QA çıktı reformu FAZ 0):** `SCORES SUMMARY` yok / skor hücresi yok /
> `MEDIA MISSING` · `INPUT MODE: MISSING` · `RUN NOT STARTED` → karar `KESİK`: koşu değil,
> yarım çıktı. Tabloya girmez (`t_tablo`), ⑤ çapraz partisine girmez (yarım raporun sahne/kesme
> sayısı partiyi düşüremez), `ders_frekans` saymaz, `sayac` "geçerli satır" saymaz. Yeni gelen
> kesik çıktı `<FILM>_<MERCEK>_KESIK_HAM.md` adıyla kaydedilir; eski dosyalar yeniden adlandırılmaz,
> ayrım içerikten (`kesik_mi`). `SCORE SUMMARY` (tekil) başlığı da okunur (`SKOR_BASLIK`).

## 🩺 `qa_saglik.py` — rubrik çıktılarının sağlığı, mercek başına (14.09.2026)

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --ozet    # sayac 🩺 bloğu (≈3 s)
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --tam     # + en sık sebepler + film başına GO/n
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --film THE_HARD_DOCK
```

Her ham raporu `rapor_denetle` + film başına `capraz` ile (main'in yolu) geçirir; mercek
başına n · mod D% · tekil ve ⑤-sonrası karar · tally = etiket · VERDICT · boyut medyanı ·
kaynaksız hücre payı basar. Dosya yazmaz. Taban çizgisi (14.09.2026 kesiti):
`QA_PROMPTLARI/CALISTIRMA_KAYITLARI.md` 📉 bölümü — rubrik/sözleşme değişikliğinin etkisi
sonraki koşularla oradan okunur.

> ⭐ **14.09.2026 (reform FAZ 4):** `--film` verildiğinde betik
> `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/<FILM>.md` kaydında `## 🔁 DERS DÖNÜŞÜ`
> bölümünü arar (TEKRAR: D<n> · ADAY: … · MOD) — yoksa **NOT** (eski kayıtlar kırılmaz).
> QA'nın ders sistemine borcu bu iki satırdır (`qa-isle` kayıt zinciri · AGENTS ①.12).

## 🔁 `ders_frekans.py` — hangi örüntü kaç filmde tekrarlıyor (14.09.2026)

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/ders_frekans.py --ozet   # ilk 10 · sayac 🔁 bloğu
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/ders_frekans.py --tam    # tamamı
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/ders_frekans.py --esik 3 # ≥3 filmde tekrarlayanlar
```

`02_HAM_RAPORLAR/*/*_HAM.md` tarar (rapor_kontrol'ün `govde_al` / `skor_tablosu`
yardımcılarıyla): dosya başına film · mercek · mod (D/V) · `VERDICT` · ≤6/10
kategoriler. Çıktı: (a) VERDICT × **farklı film** sayısı, (b) düşük kategori ×
farklı film, (c) `KUME_SOZLUK` ile o örüntünün dersi var mı (D numarası) yoksa
"⬜ dersi yok". Mod D/V ayrı sütun. **Dosya yazmaz** — sayı tek yerde (sayac).
Ders terfi eşiği ≥ 2 farklı film (`00_DERS_YAZIM_KONTRATI` §2b): tek filmde görülen
bulgu ADAY kalır, bu betik "ikinci film"i gösterir. Yeni örüntü çıkınca
`KUME_SOZLUK`'a satır eklenir (ders yazıldığında, ders numarasıyla).

⛔ Betik **bulgunun doğruluğunu** ölçmez — o iş kare/ses ister (⑪ ölçüm kapısı,
② kilit defteri). Ölçtüğü tek şey raporun kendi içinde ve partinin kendi arasında
tutup tutmadığıdır. Rubrik metnine kural EKLENMEZ; kural buraya, çıktı kapısına
gelir (rubrik hacmi: `sayac.sh` 🧭).
