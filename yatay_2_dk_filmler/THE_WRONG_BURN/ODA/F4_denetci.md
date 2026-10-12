# F4 · denetci (faz 4 kapısı) — THE_WRONG_BURN

> Girdi: KABUL_LISTELERI Ö + F4 · F4 ODA dosyaları (ses_1 · besteci_1 · kurgucu_1 · diyalog_1 · ses_2 · besteci_2) · FILM §5 §6 §7 · DURUM · NOTLAR · film_dogrula. Ajanın cevabı aynen (Fable kaydı, 09.10.2026).

FAZ 4 KAPISI · yatay_2_dk_filmler/THE_WRONG_BURN

Not: Film klasörünün tamamı git'te izlenmiyor (`?? yatay_2_dk_filmler/THE_WRONG_BURN/`), bu yüzden `git diff` kullanılamadı. Karşılaştırmayı iki yoldan yaptım: tur 1 ile tur 2 ODA dosyalarını yan yana okudum, FILM.md §6 ve §7'yi de `uretim_hatti/SABLON/FILM.md` §6 §7 ile karşılaştırdım.

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** | ✅ | yeni-film SKILL tablosu F4 eleştirmenlerini "kurgucu · diyalog-yazari (koşullu)" diye veriyor. Filmde REPLIK var. `ODA/F4_kurgucu_1.md` ve `ODA/F4_diyalog-yazari_1.md` mevcut. |
| Ö2 **M** | ✅ | kurgucu_1 satır 58: `GİRDİ ODA/F4_besteci_1.md (tam) · ODA/F4_ses-tasarimcisi_1.md (tam, §7 dahil) · FILM.md §1 · §2 · §4 · §5 …`. diyalog_1 satır 79-83'te GİRDİ dosya yollarıyla yazılı. Bütün F4 dosyalarında `grep EKSİK` sonucu boş. |
| Ö3 | ✅ | Kurgucu CİDDİ B1-B3 besteci_2 §1'de cevaplanmış: B1 KABUL, B2 KABUL, B3 KISMEN. KISMEN, açıkça ayrılmış KABUL ve RED parçalarından oluşuyor. K-B2'nin ses tarafı ses_2 §1'de KABUL. Diyalog CİDDİ B1-B6'nın hepsi ses_2 §1'de KABUL. Müziğe düşen B1, B5, B6 besteci_2 §1'de KABUL. |
| Ö4 | ✅ | Bütün KABUL'ler yeni sürümde bulundu. Ayrıntı aşağıdaki Ö4 dökümünde. |
| Ö5 | ✅ | Besteci B3 RED (−3 dB), kurgucunun kanıtına cevap veriyor: "kural 7 tabanı −6 dB; … altosunun … keman bandıyla çakışması". "0,9 s" RED'i kanıta karşı başka ölçü koyuyor: "39,2-40,1 … ve 46,0-50,0 (3,8-4,0 s çıplak)". B4 RED (OKUMA'dan "zafer değil"i çıkarmamak) da gerekçeli: "1,2 s'lik, orta-yoğunluklu … akor zafer için gereken süreyi … taşımaz". |
| Ö6 | ✅ | Açık ÖLÜMCÜL yok. kurgucu_1 `ÖZET ÖLÜMCÜL 0 · CİDDİ 3 · KÜÇÜK 3`, diyalog_1 `ÖZET ÖLÜMCÜL 0 · CİDDİ 6 · KÜÇÜK 4`. DURUM AÇIK ÖLÜMCÜL tablosunda F4 satırı yok. |
| Ö7 **M** | ✅ | DURUM: `FAZ 4` · `ADIM —` · `TUR 1` · `AJAN_CAGRI 40 / 50` · `SIRADAKI F4 kapı … → denetci (Ö + F4) → Fable → F5 …` · `SON_GUNCEL 09.10.2026 17:30`. Sayaç AJAN GÜNLÜĞÜ ile tutuyor: F1 7 + F2 14 + F3 11 + F3b 2 + F4 6 (satır 120-125) = 40. `film_dogrula --bolum durum` geçti. |
| F4.1 | ✅ | FILM §6 S1-S12'nin hepsi K1-K4, yani en çok 4 katman. Vakum dışı ↔ iç hacim ayrımı Ortam satırında yazılı: "Vakum dışı: dış ses yok … İç hacim ve ince atmosfer bu filmde yok (C12'nin açık kapağı dahil)". |
| F4.2 | ✅ | ses_2 §4 tablosunda metin · ses profili (BRAM_52_bariton / SELA_29_alto) · ton · hedef süre · filtre (+ seviye) 12/12 dolu. FILM §6: "Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_2.md". |
| F4.5 | ✅ | ses_2 §5'te C01-C12'nin her biri için satır var. Sessiz an gerekçeli: C04 "(ışığın ve ufkun inişi: kulakta karşılığı yok, bilinçli)". Her satırda Kaynak sütunu ve "Nereden" (İngilizce prompt ya da N-kayıt) dolu. Sahne başına ortam yatağı ses_2 §6'da S1-S12. Küçük not: C10 0-1,5 ve C11 2,6 satırları yeni bir prompt değil, mevcut bir varlığın türevine işaret ediyor ("C09 9,75 varlığının uzantısı"). |
| F4.3 | ❌ | Okuma cümlesi var, müziksiz an var (3 aralık), vuruş/susma noktaları var, kesme ilişkisi besteci_2 §4'te yazılı. Ama 106,0-110,0 (C11 6-10 s) aralığı için eserde ve kararda **üç ayrı değer** var: FILM §6 S11 `6,0-10,0 L3 yok` · FILM §7 `≈106,3 L1+L3 −12 dB'ye iner, kesilmez` · NOTLAR KARARLAR satır 63 `bestecinin yedeği **−18 dB varsayılan**`. Fable'ın kendi §6 yorum satırı (FILM satır 168) da kararla çelişiyor: `C11 106,3-111,2 −12 dB, F8 ölçer`. FILM §7'nin F8'e verdiği değer −12. Fable'ın −18 kararı FILM'e geçmemiş. |
| F4.4 | ✅ | FILM §6 başlığı "model sesi kullanılmaz"; Ortam: "Model sesi kullanılmaz (Return silent videos; ses kurguda)". ses_2 §0'da istisnanın filmde olmadığı yazılı: "ağız kadrajda replik bu filmde YOK". diyalog_1'in ağız kontrolü 12/12 temiz. |

**Ö4 dökümü (KABUL → yeni sürümdeki yeri)**
- **Kurgucu B1:** besteci_2 §3 "Mi3 165 Hz + La3 220 Hz taşıyıcı". "Telefonda 110 Hz duyulur" cümlesi silinmiş. Kural 5 artık KISMEN (§7).
- **Kurgucu B2 ve diyalog B1:** FILM §7 "(2) 60,0–96,8 s … " ve "60,0 L1 yay kalkar". FILM §6'da S7-S9 için "K4 yok".
- **Kurgucu B3 (KABUL kısmı):** FILM §7 "replik 6 sonu 35,3 + 0,1" ve "≈4,5 L1 girer". besteci_2 seviye tablosunda "replik 6 … L2 **−6**".
- **Kurgucu B4 (KABUL kısmı):** besteci_2 §4 "en yüksek yoğunluk **2**". Seviye tablosu 111,8-113,0'da L3 −4.
- **Kurgucu B5:** FILM §7 "14,6–30,0 L2 çok yavaş yükselir, 30,0'da … durur".
- **Kurgucu B6:** besteci_2 §4 satır 3'te yoğunluk "2". "(↗3)" kalmamış.
- **Diyalog B2:** FILM §6 S6 "tık 8,8 + hışırtı 8,8'den". S7 "başlangıç tıkı yok (hat 58,8'den beri açık)".
- **Diyalog B3:** FILM §6 S5 "4,5'te son alım → tutulur → 7,0'da bırakılır".
- **Diyalog B4:** FILM §6 S7 "'Bram?' altında −28". ses_2 §4'te Seviye sütunu −2 / −6.
- **Diyalog B5:** FILM §7 "≈113,0 KESME … 113,0–120,0 müziksiz".
- **Diyalog B6:** FILM §6 S11 "Sela alımı **1,5**". besteci_2 seviye tablosu 100,0-106,3 L3 −8.
- **Diyalog B7:** ses_2 §4 satır 3 "Cut it. You're climbing. …". FILM §5 satır 133 "Cut it. …".
- **Diyalog B8:** ses_2 Not 8 "YALNIZ ölçümde … varsayılan 0".
- **Diyalog B9:** ses_2 §5'te C05 ve C09 hücrelerinde "tutma yok".
- **Diyalog B10:** ses_2 Not 8 TON "C04'ten belirgin yorgun, dakikalar sonra".
- **§6 ve §7'nin birebir taşınması:** FILM §6 satır 155-166 + Ortam bloğu, ses_2 §2 + §3 ile aynı. FILM §7 satır 184-211, besteci_2 §2 ile aynı.

**Notlar (❌ değil):**
1. FILM §6'da eski plana kalmış iki atıf var: S1 "müzik 4,2'den (besteci)" ve S12 "tercih 113,2'de kesilir". Bunlar FILM satır 168'deki yorum ve NOTLAR karar (c) ile adreslenmiş.
2. FILM §5 satır 128'deki kaynak notu hâlâ `F2_diyalog-yazari_3.md §1, birebir` diyor. Oysa replik 3 artık kaynaktan farklı: kaynakta satır 148 "Cut it!". Değişikliğin kaydı NOTLAR satır 64'te ve diyalog_1'in "Fable kararı" bölümünde var, ama FILM'deki kaynak notunda yok.
3. DURUM FAZ GÜNLÜĞÜ'nde F4 için satır yok. Ö7 bunu istemiyor; yeni-film §2f KAYIT istiyor.
4. ses-muzik §F4 madde 5'teki sahip iş listesi (replik kaydı + efekt listesi, `R01.wav …` adlandırması) henüz DURUM'da ya da SIRADAKI'da yok. KABUL listesi bu maddeyi kapsamıyor.
5. Mekanik çıktı aşağıda. film_dogrula'da ses ya da müzik bölümü olmadığı için F4'ün kendi maddelerinin hiçbiri mekanik değil.

```
$ python3 uretim_hatti/araclar/film_dogrula.py yatay_2_dk_filmler/THE_WRONG_BURN --bolum kunye hikaye cekim replik sahneleme durum
film: yatay_2_dk_filmler/THE_WRONG_BURN · bölüm: cekim durum hikaye kunye replik sahneleme · çekim: 12
✅ yapı geçerli
EXIT=0
```

```
MEKANİK ❌   yok
YARGI ❌     F4.3: 106,0-110,0 müzik seviyesi eserde ve kararda tutarsız (§6 S11 "L3 yok" · §7 "−12 dB" · NOTLAR karar "−18 dB varsayılan"; FILM §6 yorum satırı kararla çelişiyor)
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: F4.3)
```

---

## Fable kararı (09.10.2026)

**F4 KAPANDI.** Aşılan kapı yok. Yargı ❌ F4.3 aşılmadı, kapatıldı:
- 106,0-110,0 için tek değer: **106,3'te L3 kesilir, L1 −18 dB sürer (kesilmez), 111,2'de L1 geri döner ve L3 yeniden girer.** İki yazarın kendi metinleriyle tutarlı yol: ses_2 §6 S11 / §9 "L3 yok" + besteci_2 §9 madde 4 yedeği (−18) ve "pedal kesilip yeniden girmez" kuralı. Değişiklik yazara geri gitti: besteci aynı çağrı içinde (SendMessage, sayılmadı) F4_besteci_2.md §1 ("Fable kararı 3"), §2, §3, §4, §9'u güncelledi; §1 B2 / §5 / §8'deki eski −12 ifadeleri yazarın notuyla geçersiz işaretli. FILM §7 bloğu yeni hâliyle yeniden yerleşti (fark yalnız VURUŞ/SUSMA 106,3 · 106,3-111,2 · 111,2-111,8 · yedek B satırları). FILM §6 Fable yorum satırı aynı değere çekildi.
- NOTLAR KARARLAR satırındaki "−18 varsayılan" kararı böylece hem FILM §6 hem §7 ile aynı.

Denetci notları: 1 → §6 yorum satırı (yukarıda) · 2 → FILM §5 kaynak notuna "Cut it." kaydı eklendi · 3 → FAZ GÜNLÜĞÜ F4 satırı yazıldı · 4 → sahip iş listesi (replik kaydı R01-R12 · sözsüz kayıt grupları · efekt E · ortam O; ses_2 §4-§6) F7 sahip listesine taşındı, DURUM SIRADAKI'da · 5 → film_dogrula'da ses/müzik bölümü yok, hat gözlemi (sahip).
