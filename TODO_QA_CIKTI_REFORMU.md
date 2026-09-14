# ✅ TODO — QA ÇIKTI REFORMU (açıldı 14.09.2026)

> **Kalıp:** `TODO_AKIS_VE_DERS_REFORMU.md` gibi — tarihli, ölçümlü, doğrulama komutlu
> çalışma listesi. Faz bitince kutu işaretlenir; kalıcı bilgi kılavuza/betiğe taşınır.
> **Kural:** buraya yazılan her sayı **14.09.2026 kesitidir**; güncel sayı
> `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --ozet`.
> **Sahip kararı (14.09.2026):** 8 maddenin hepsi · her faz bitince DURULUR, sonraki faz
> sahibin onayıyla başlar · commit sahibin.
> **⛔ DEĞİŞMEYEN SİSTEM:** sahip filmi üretir → rubrik dosyasını (SPEC ile) DIŞ MODELE
> sırayla verir → gelen metni ajana iletir. Dış model betik koşamaz, dosya göremez. Her
> madde üç katmandan birine düşer: RUBRİK METNİ (modelin gördüğü) · PAKET (sahibin
> yapıştırdığı tek dosya, betik üretir → pano) · BETİK (ajanın koştuğu).

---

## 🩺 TEŞHİS — ölçüm (14.09.2026 · qa_saglik.py · 336 mercek raporu · 41 film)

```
KARAR      tekil GO 26 (%7) · ŞARTLI 114 · TEKRAR 85 · GEÇERSİZ 57 · ✂️ KESİK 54
           ⑤ çapraz sonrası (tabloya giren): GO 3 · parti düşen film 25/41 — mercekler
           kesme/sahne sayısında anlaşamıyor; canlı T tablosunda 14/105 film
GİRDİ      mod D %12; SPEC varken mod V 112 koşu; ⑨-⑫ %70 geçersiz (mod V = boş);
           ⑬ UYUM 0 geçerli koşu (üretim defteri boş); 63 film SPEC'siz
SÖZLEŞME   tally = yazılı etiket 99/241 (%41); SCORED/SUM/OVERALL aritmetik 16 fabrike +
           21 yuvarlama; ⑦-⑫ "no in-scope source keeps 10/10" → ⑦ ort 8,3 (hücrelerinin
           %32'si kaynaksız, 62'si 10/10) — ①-⑥ "→ —" diyor; iki kural
HÜKÜM      56 farklı VERDICT metni; 13 rubriğin 13'ü kapalı liste tanımlıyor, betik denetlemiyor
KESİK      54 raporda skor hücresi yok (medya yüklenmemiş / çıktı kesilmiş) — ham sayılıyordu
SAPMA      aynı film+mercek tekrar farkı medyan 0,9 · maks 7,0; rapor medyanı 6,5 KB
DERS       128 film dersinin 53'ü bir merceğe dayanıyor (336 rapordan)
```

## 🔢 SABİTLER — tek yerde

```
KESIK_IZI / kesik_mi()   SCORES SUMMARY yok · 0 hücre · MEDIA MISSING / INPUT MODE: MISSING /
                         RUN NOT STARTED → karar KESİK                        rapor_kontrol.py
SKOR_BASLIK              SCORES? SUMMARY (tekil de okunur)                     rapor_kontrol.py
VERDICT_SOZLUK           mercek → kapalı hüküm listesi (FAZ 1)                 rapor_kontrol.py
kaynaksız hücre          "no in-scope source" → — (13 rubrikte tek kural, FAZ 1) rubrik + betik
MERCEK BÜTÇESİ           SPEC D BLOĞU (FAZ 3) + qa_paketle.sh --liste
ölçüm sapması            ±1,3 — OVERALL ders gerekçesi olamaz (FAZ 5)
taban çizgisi            CALISTIRMA_KAYITLARI.md 📉 (qa_saglik --ozet kesiti)
```

---

## ✅ FAZ 0 — TABAN ÇİZGİSİ + KESİK KOŞU (madde 5 + ölçüm) — BETİK

- [x] `RAPOR_KONTROL/qa_saglik.py` (`--ozet` · `--tam` · `--film`) — rapor_kontrol yolundan (⑤ çapraz dâhil,
      KESİK dışarıda); tekil ve ⑤-sonrası karar · mod D% · tally=etiket · VERDICT · boyut · kaynaksız hücre; 3 s
- [x] `rapor_kontrol.py`: `KESIK_IZI` · `kesik_mi()` · karar **KESİK** (✂️; tablo-yok dalı buna döndü) · `SKOR_BASLIK`
      "SCORE SUMMARY" toleransı · KESİK ⑤ çaprazına girmez · TOPLAM satırı · çıkış 2
- [x] `t_tablo.py` KESİK satır yazmaz · `ders_frekans.py` KESİK'i atlar (başlıkta sayar) · `sayac.sh` GEÇERSİZ
      PARTİ awk KESİK'i geçerli saymaz + ✂️ satırı + yeni **🩺 QA SAĞLIK** bloğu
- [x] Kayıt kuralı `<FILM>_<MERCEK>_KESIK_HAM.md` (yalnız yeni gelenler; eski 54 dosya yeniden adlandırılmadı,
      içerikten tanınır): `qa-isle/SKILL.md` kayıt zinciri adım 1 · `QA_PROMPTLARI/00_README` 🤖 bloğu ·
      `RAPOR_KONTROL/00_README`
- [x] `CALISTIRMA_KAYITLARI.md` 📉 TABAN ÇİZGİSİ 14.09.2026 — `qa_saglik --ozet` çıktısı olduğu gibi; izlenecek dört sayı
- [x] Doğrulama: FAZ 0 öncesi betikle 365 rapor karşılaştırıldı — 281 aynı · 82 GEÇERSİZ→KESİK (54 mercek + 28 mercek
      dışı) · 2 GEÇERSİZ→TEKRAR/ŞARTLI ("SCORE SUMMARY" tekil başlık artık okunuyor — istenen tolerans) · GO 26 aynı ·
      `ders_frekans --ozet` "✂️ 86 kesik sayılmadı" · `sayac.sh` 🩺 bloğu basıyor

## ✅ FAZ 1 — ÇIKTI SÖZLEŞMESİ (madde 1 · 2 · 6) — RUBRİK METNİ + BETİK

- [x] 13 rubrik (betikle, `scratchpad/faz1_rubrik.py`; dikey ekte tally/aritmetik yoktu): başlık bloğundan ARITHMETIC
      GATE + OVERALL (STORY) SCORE (+ ④ N/A LEDGER'ın OVERALL parçası) çıktı · `## SEVERITY TALLY` bölümü çıktı ·
      SCORES SUMMARY kuralı "OVERALL = mean …" → ⑤ "DO NOT TOTAL, AVERAGE OR TALLY — the library's script counts" ·
      ⑦-⑫ "keeps 10/10" → `—` ortalamaya girmez · VERDICT bloğu (öncelik kuralları dâhil) başlıktan tablonun ALTINA
      ("Write the verdict UNDER the table … exactly one of") · tracking row `**_/10**` → `—` · ⑦/⑧ "OVERALL SCORE
      line reads N/A" → VERDICT · ⑬ SCORED/SUM/DIVISION/OVERALL bloğu + kontrat notu yeniden. Kategori adları/sırası
      dokunulmadı; satırlar 78-85 kolona sarıldı.
- [x] `rapor_kontrol.py`: `VERDICT_SOZLUK` (13 mercek; ⑦ ⑧ N/A hükümleri eklendi; ⑬ None) · `verdict_normal/oku/
      sozlukte` (tire/köşeli/kalın/nokta normalize; `LEAVES AT n s` ve `mm:ss`) · ①.13 HÜKÜM kapısı (yok / sözlük
      dışı → ŞARTLI) · tally yokken NOT bile basılmaz · **`govde_al` düzeltmesi:** `---` künyeyi değil raporun kendi
      başlık bloğunu kapatıyorsa atlanmıyor (33 "mod ?" TEKRAR + 14 GEÇERSİZ sahte bulguydu; artık mod V/D okunuyor) ·
      başlık yorumu · `ders_frekans` kanonik hüküm sayımı + "⚠️ sözlük dışı" satırı (24 rapor) · `qa_saglik` VERDICT
      sütunu sözlükten (82-100 %) · `sayac` rubrik globuna 13 eklendi
- [x] `00_README` SALT PROMPT bloğu + DEĞİŞİKLİK KAYDI · `CALISTIRMA_KAYITLARI` 📜 bölümü (betik sonrası kesit) ·
      `ARSIV_CIKTI_KURALLARI` §14.09 (26 kesilen parça, rubrik başına) · `qa-isle` §2b ①.13/KESİK paragrafı
- [x] Doğrulama: rubrik 13/13 ≤ 25 KB (sayaç; ① 24 KB) · `mercek_bul` 13/13 · reform öncesi betikle 365 rapor:
      274 aynı · 82 → KESİK · 5 GO → ŞARTLI (VERDICT satırı yok — ①.13) · 4 karar govde_al düzeltmesiyle yer değiştirdi
      (mod ? → V) · tekil GO 21 / parti sonrası 2 · `qa_saglik` VERDICT sözlükte ① 87 · ② 100 · ⑥ 93 · ⑫ 88 % ·
      ⚠️ modelin yeni sözleşmeye uyumu depoda ölçülemez — sahibin sonraki 3 filminde `qa_saglik --ozet`

## ✅ ARA İŞ (FAZ 1 → 2 arası · 14.09.2026 · sahip talebi) — ⑭ HAREKET + ⑮ YÖN

> *"filmlerde saçma sapan hareketler yapıyorlar, yanlış yere dönmek, ateş etmek vs. — 14 ve 15
> QA promptlarını hazırla, tespit edelim, ders çıkarabilelim."*

- [x] `_KAYNAK/14_HAREKET_QA_CRITIQUE_PROMPT.md` (21,1 KB) — hareket mantığı: AMAÇ CÜMLESİ · MOTION LEDGER ·
      13 kapalı etiket (PURPOSELESS · LOOP · SLIDE · SPIN · PHANTOM · MISGRIP · ABANDONED · CONTRADICTION ·
      PUPPET · DISSOCIATED · MISREACTION · OVERGESTURE) · 14 bilinen desen · 8 kategori · PURPOSE STRING ·
      PROMPT ORDERS tablosu · hüküm listesi · PREMISE REGISTER (sıfır-g dönüşü hata değil)
- [x] `_KAYNAK/15_YON_QA_CRITIQUE_PROMPT.md` (20,6 KB) — yön/hedef: VEKTÖR CÜMLESİ · TARGET LEDGER ·
      HIT/MISS/UNKNOWN/NO TARGET/FLIP · 14 desen (180° kırılması · sırtını dönme · boşa ateş · yanlış tarafa
      uzanma · kaçarken tehlikeye koşma · göç eden kapı …) · 8 kategori · VECTOR STRING · ekran uzayı kuralı ·
      PROMPT ORDERS · hüküm listesi
- [x] Sınırlar yazıldı: ⑦ ne oldu · ⑥ kaç saniye · ⑩ ne hissetti · ② aynı mı · ⑨ kamera · ⑭ NEDEN · ⑮ DOĞRU YERE Mİ
- [x] Betik: `rapor_kontrol.py` MERCEK_IMZA ⑭⑮ (15/15 rubrik kendi imzasına çözülüyor; "LESSON ORDERS" ⑬ imzasıyla
      çakışmasın diye bölüm adı PROMPT ORDERS) · MOD_D_MERCEKLER · NOVUM_MERCEKLER · VERDICT_SOZLUK · PURPOSE/VECTOR
      STRING = kesme+1 · MOVEMENTS ≥ PURPOSELESS · ACTS MISSED beşlisi = ACTS LOGGED · `t_tablo` T14/T15 sütun
      haritası · `qa_saglik` MERCEK_SIRA · `ders_frekans` KUME_SOZLUK "⬜ ⑭ / ⑮ — ders yok" · `sayac` rubrik globu 1[0-5]
- [x] Tablolar `T14_HAREKET_KALITE.md` · `T15_YON_KALITE.md` (boş, T7 kalıbı) · AGENTS §1 harita + **F10 · F11** kartları ·
      qa-isle mercek listesi + zincir (T13/T14/T15 + PROMPT ORDERS → ADAY/ders) · `00_README` bölüm + KAPSAM + ajan
      tablosu + DEĞİŞİKLİK KAYDI · `CALISTIRMA_KAYITLARI` bölümü · SPEC şablonu yönlendirme satırları (`HAREKET KİLİDİ:` ·
      `EKRAN YÖNÜ:` C bloğuna)
- [x] Doğrulama: sentetik ⑭ ve ⑮ raporu → mercek tanındı, VERDICT sözlükte, diziler kesme+1 tuttu, D186 kaynaksız
      hücre kapısı çalıştı (ŞARTLI) · 15 rubrik ≤ 25 KB · FAZ 3 D bloğu bütçesine ⑭/⑮ satırı eklenecek
- ⚠️ Gerçek koşu yok — ilk koşu: `rapor_kontrol.py <rapor> --film <FILM>`; ham ad `<FILM>_HAREKET_HAM.md` /
      `<FILM>_YON_HAM.md`; PROMPT ORDERS satırları tek filmde ADAY, ikinci filmde ders (kontrat §2b)

## FAZ 2 — PAKET + GİRİŞTE DURDURMA (madde 3) — PAKET + RUBRİK METNİ

- [ ] `kilavuzlar_ve_sistem_dosyalari/qa_paketle.sh <film> <mercek>` → stdout (`| pbcopy`) · `--dizin` (depo dışı) ·
      `--liste` · `--bolum n/2` · ① dikeyde dikey ek · SPEC yoksa ⑨-⑬ üretmez
- [ ] ⑨ ⑩ ⑪ ⑫ STEP 0: SPEC bloğu yoksa tek satır STOP · `00_README` çalıştırma tarifi · AGENTS ortak adım ① ·
      `qa-isle` §2 · `SKILL_KULLANIM`
- [ ] Doğrulama: HARD_DOCK ① paketi · HALF_SKY ① dikey ek · SPEC'siz ⑨ red · paket boyutu

## FAZ 3 — MERCEK BÜTÇESİ (madde 4) — PAKET + ŞABLON

- [ ] `FILM_QA_SPEC.md` şablonu **D BLOĞU — MERCEK BÜTÇESİ** · `02_RISK_KARTLARI` kart→mercek tablosu (tek kaynak) ·
      `prompt_kontrol` ㉔ D çapası (yalnız yeni rejim)
- [ ] `qa_paketle --liste` (D bloğu yoksa çekirdek 4; `--mercek` ile aşım, başlığa BUDGET OVERRIDE) · `sayac` bütçe satırı ·
      `00_README` KAPSAM ⑦ ⑧ ⑬ · `yeni-film` 9b · Kart A
- [ ] Doğrulama: `--liste` eski/yeni SPEC · scratch D bloğu

## FAZ 4 — ⑬ UYUM ÇALIŞIR (madde 8) — PAKET + BETİK + KART B

- [ ] `qa_paketle.sh <film> 13 --kapi <sahne_kapisi çıktısı>` — defter TESLİM ⬜ / klip < prompt / kapı yok → RED;
      geçerse SPEC + `<<<SCENE_PROMPTS` (🎥 bloklar birebir) + `<<<MACHINE_TABLE` + rubrik · `--bolum`
- [ ] `sayac` "⑬ BEKLİYOR" · AGENTS Kart B sırası (defter → sahne_kapisi → paket) · `qa-isle` zinciri T13 · F9 · `00_README` ⑬
- [ ] Doğrulama: scratch film → paket · boş defter → red · sayac satırı

## FAZ 5 — SAYI TABLODAN, KARAR BULGUDAN (madde 7) — BETİK + KONTRAT

- [ ] `rapor_kontrol.yazdir` sapma bandı satırı · 13 T dosyasına tek satır · kontrat §2b · Kart G adım 0 · `qa-isle` ①.12
- [ ] `ders_frekans` üçüncü tablo: etiketli (timecode'lu) bulgu × farklı film
- [ ] Doğrulama: `--ozet` üç tablo

## FAZ 6 — BELGELER · DOĞRULAMA · BELLEK

- [ ] AGENTS §1 harita (qa_saglik · qa_paketle · KESİK) · §7 doğrulama · §8 tek cümle · YAPI_GRAFI · README'ler · SKILL_KULLANIM
- [ ] Tam doğrulama (sayac · qa_saglik · rapor_kontrol 44 klasör · qa_paketle üç mod · prompt_kontrol regresyon) · git status
- [ ] Bellek `qa-cikti-reformu-durum.md` + MEMORY.md · sahip raporu (taban + 4 veto: kart→mercek eşlemesi · SCORES kalıbı ·
      eski filmde bütçe varsayılanı · KESİK = yeniden koşulacak)

---

## 🚫 YAPILMAYACAKLAR

- Commit atılmaz; her faz "commit'e hazır" bırakılır ve sahibin onayı beklenir.
- Ham çıktı silinmez, yeniden adlandırılmaz (KESİK ayrımı içerikten; yalnız YENİ gelen kesik çıktı `_KESIK_` alır).
- Kategori adları · `MERCEK_IMZA` · `BOLUM_SONU` başlıkları · tracking row değişmez (T tabloları karşılaştırılabilir kalır).
- Rubrik ≤ 25 KB; rubriğe Türkçe not / tarih / D-numarası / depo yolu girmez (salt prompt).
- Dış modelden betik koşması / dosya okuması istenmez; sahibin yapıştırma döngüsü kaldırılmaz.
- Depoya paket dosyası yazılmaz (11.09 kararı) — paket panoya/depo dışına.
