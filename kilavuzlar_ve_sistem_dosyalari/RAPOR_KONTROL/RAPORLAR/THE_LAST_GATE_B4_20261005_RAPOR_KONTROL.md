# 🧮 RAPOR KONTROL — THE_LAST_GATE · BÖLÜM 4/4

> **Tarih:** 05.10.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_LAST_GATE_PART4_1_KARE_HAM.md` | GEÇERSİZ | None/None/None | 9/57/6.33 | 8/48/6.0 | — |
| ② DEVAMLILIK | `THE_LAST_GATE_PART4_2_DEVAMLILIK_HAM.md` | GEÇERSİZ | None/None/None | 12/90/7.5 | 12/90/7.5 | — |
| ③ SES | `THE_LAST_GATE_PART4_3_SES_HAM.md` | GEÇERSİZ | None/None/None | 9/90/10.0 | 0/0/None | — |
| ④ HİKAYE | `THE_LAST_GATE_PART4_4_HIKAYE_HAM.md` | GEÇERSİZ | None/None/None | 10/41/4.1 | 7/30/4.3 | — |
| ⑤ ARKA PLAN | `THE_LAST_GATE_PART4_5_ARKA_PLAN_HAM.md` | GEÇERSİZ | None/None/None | 9/58/6.44 | 9/58/6.4 | — |
| ⑥ FİZİK | `THE_LAST_GATE_PART4_6_FIZIK_HAM.md` | GEÇERSİZ | None/None/None | 8/80/10.0 | 0/0/None | — |
| ⑦ AKSİYON | `THE_LAST_GATE_PART4_7_AKSIYON_HAM.md` | GEÇERSİZ | None/None/None | 9/90/10.0 | 0/0/None | — |
| ⑧ EFOR | `THE_LAST_GATE_PART4_8_EFOR_HAM.md` | GEÇERSİZ | None/None/None | 7/7/1.0 | 7/7/1.0 | — |
| ⑨ KADRAJ | `THE_LAST_GATE_PART4_9_KADRAJ_HAM.md` | GEÇERSİZ | None/None/None | 5/33/6.6 | 3/23/7.7 | — |
| ⑩ OYUNCULUK | `THE_LAST_GATE_PART4_10_OYUNCULUK_HAM.md` | GEÇERSİZ | None/None/None | 9/61/6.78 | 9/61/6.8 | — |
| ⑪ IŞIK | `THE_LAST_GATE_PART4_11_ISIK_HAM.md` | GEÇERSİZ | None/None/None | 7/40/5.71 | 7/40/5.7 | — |
| ⑫ HOOK | `THE_LAST_GATE_PART4_12_HOOK_HAM.md` | GEÇERSİZ | None/None/None | 8/55/6.88 | 5/36/7.2 | — |
| ⑬ UYUM | `THE_LAST_GATE_PART4_13_UYUM_DURDURULDU.md` | KESİK | None/None/None | None/None/None | None/0/None | — |
| ⑭ HAREKET | `THE_LAST_GATE_PART4_14_HAREKET_HAM.md` | GEÇERSİZ | None/None/None | 8/80/10.0 | 0/0/None | — |
| ⑮ YÖN | `THE_LAST_GATE_PART4_15_YON_HAM.md` | GEÇERSİZ | None/None/None | 8/80/10.0 | 8/80/10.0 | — |

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — 1 hücre düzeltildi<br>Camera 9/10 → — (issue: "23 clean scene cuts across c" — kusur yok, sayı taşıyamaz) [D186]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ② DEVAMLILIK — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **NOT** — ⛔ BÖLÜM SINIRI KÖR NOKTASI [§2.6]<br>② sınır çiftini (son sahne ↔ sonraki bölümün ilk sahnesi) hiçbir yarım masterda yan yana GÖREMEZ. Çift SPEC B'nin sınır satırından ELLE KAREYLE kapanır (①.10 göz kapısı kalıbı); kapanmadan parti kapanmaz.
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur
- **ŞARTLI** — PRESENCE STRING 17 hane, kesme+1 = 23<br>şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — 9 hücre düzeltildi<br>Speaker Attribution 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Synthetic Voice Tells 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Voice Identity Continuity 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Delivery vs Performance 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Turn-Taking & Acoustics 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Ambience Continuity 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · SFX Causality & Sync 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Mix Hierarchy & Levels 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186] · Music & Silence 10/10 → — (issue: "None" — kusur yok, sayı taşıyamaz) [D186]

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — BÖLÜM KAPISI — 3 kategori BÖLÜM 4/4'de ölçülemez [§2.6]<br>SON bölüm — filmin BAŞI bu dosyada değil · sayı taşıyamaz: Hook · Structure & Pacing · Retention Risk. Bu hücreler `—` olur, ortalama yeniden hesaplanır; kesme listesi ve yeniden sıralama UYGULANMAZ (kesme filmin kurgusudur, bölüm raporunun yetkisi değil).
- **ŞARTLI** — 3 hücre düzeltildi<br>Hook 5/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6] · Structure & Pacing 3/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6] · Retention Risk 3/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑤ ARKA PLAN — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑥ FİZİK — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — 8 hücre düzeltildi<br>Ballistics & Trajectories 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Impact & Momentum 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Material Behaviour 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Particles & Atmosphere 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Scale & Measurement 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Rates & Timing 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Light & Shadow Physics 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186] · Human Biomechanics 10/10 → — (issue: "no deductions" — kusur yok, sayı taşıyamaz) [D186]
- **ŞARTLI** — PRESENCE STRING 25 hane, kesme+1 = 24<br>şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· medium / environment      [microgravity / orbital space flight near gas giant] capabilit…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — 9 hücre düzeltildi<br>Beat Anatomy 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Spatial Geography Under Motion 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Threat Vector & Approach 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Contact Legibility 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Consequence Visibility 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Camera's Contract with the Action 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Agency & Intent 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · The Stakes Object 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Physical Tempo & Escalation 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑧ EFOR — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· gravity / medium [microgravity / spacecraft interior] what the body wears [pressurised f…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — Fatigue Accumulation 1/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "-9 · Capability remains completely unchanged across 24 scene" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Recovery Curve Honesty 1/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "-9 · Curve remains at baseline zero despite continuous suit " · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — COST CURVE sabit (0) ama efor olayı var<br>iş yapıldıysa borç ya artar ya toparlanır; düz eğri ÖLÇMEDİ demektir
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑨ KADRAJ — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **ŞARTLI** — BÖLÜM KAPISI — 1 kategori BÖLÜM 4/4'de ölçülemez [§2.6]<br>SON bölüm — filmin BAŞI bu dosyada değil · sayı taşıyamaz: Rhyme Pair. Bu hücreler `—` olur, ortalama yeniden hesaplanır; kesme listesi ve yeniden sıralama UYGULANMAZ (kesme filmin kurgusudur, bölüm raporunun yetkisi değil).
- **ŞARTLI** — 2 hücre düzeltildi<br>Rhyme Pair 1/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6] · Screen Geometry 9/10 → — (issue: "Stable horizon lines and sub" — kusur yok, sayı taşıyamaz) [D186]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑩ OYUNCULUK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — Gaze Direction 8/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "🟢 Bakış yönleri genel olarak panellere, hedefe ve mürettebat" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Proportion 7/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "🟡 Görevlerin büyüklüğü ile jest boyutları genel olarak denge" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑪ IŞIK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — In-Clip Stability 7/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Klipsiz içi belirgin ışık dalgalanması gözlemlenmedi" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑫ HOOK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **ŞARTLI** — BÖLÜM KAPISI — 3 kategori BÖLÜM 4/4'de ölçülemez [§2.6]<br>SON bölüm — filmin BAŞI bu dosyada değil · sayı taşıyamaz: Hook Question · Stakes by the First Share Moment · Plateau. Bu hücreler `—` olur, ortalama yeniden hesaplanır; kesme listesi ve yeniden sıralama UYGULANMAZ (kesme filmin kurgusudur, bölüm raporunun yetkisi değil).
- **ŞARTLI** — Format Fit 9/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "🟡 16:9 sinematik oran temiz, yanık metin veya kapatıcı görse" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — 3 hücre düzeltildi<br>Hook Question 8/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6] · Stakes by the First Share Moment 6/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6] · Plateau 5/10 → — (bölüm 4/4: bu uç dosyada yok) [§2.6]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑬ UYUM — KESİK
- **GEÇERSİZ** — ⑬ UYUM mod M koşulmuş → KOŞU DEĞİL [11.09.2026]<br>Bu merceğin mod V'si yoktur: sahne↔prompt karşılaştırmasının bir tarafı eksikse karşılaştırma da yoktur. T13'e satır girmez, ders siparişi üretmez. Koşu dört girdiyle tekrarlanır: kurgu · sahne promptları (birebir) · QA_SPEC · sahne_kapisi.sh çıktısı + üretim defteri satırları.
- **TEKRAR** — SPEC dosyası VAR, rapor mod M → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **KESİK** — KESİK KOŞU — INPUT MODE: MISSING<br>Koşu değil: medya yüklenmemiş / çıktı yarıda kesilmiş. Tabloya girmez, partiyi düşürmez, frekansa girmez; aynı mercek YENİDEN koşulur. Yeni gelen kesik çıktı `<FILM>_<MERCEK>_KESIK_HAM.md` adıyla kaydedilir [14.09.2026].

## ⑭ HAREKET — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **ŞARTLI** — 8 hücre düzeltildi<br>Purpose Legibility 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Locomotion Sense 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Turn & Rotation Logic 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Hands & Object Handling 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Loop & Repetition 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Commitment & Completion 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Body Coherence 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186] · Reaction Sense 10/10 → — (issue: "—" — kusur yok, sayı taşıyamaz) [D186]
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑮ YÖN — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **NOT** — BÖLÜM 4/4 girdisi — SON bölüm — filmin BAŞI bu dosyada değil<br>bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir
- **NOT** — ⑨ ızgara OTURUYOR — 23 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ⑤ ÇAPRAZ KAPI
- **GEÇERSİZ** — ⑤ KESME YAYILIMI 8 > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]<br>① KARE 23 · ② DEVAMLILIK 22 · ③ SES 15 · ④ HİKAYE 23 · ⑤ ARKA PLAN 23 · ⑥ FİZİK 23 · ⑦ AKSİYON 23 · ⑧ EFOR 23 · ⑨ KADRAJ 23 · ⑩ OYUNCULUK 23 · ⑪ IŞIK 23 · ⑫ HOOK 23 · ⑭ HAREKET 23 · ⑮ YÖN 23
        ⭐ ÇÖZÜMÜ: master'ı ölç (olcum_kapisi.sh) ve --olcum-kesme <n> ile yeniden koş — ölçüm hakemdir, parti ayakta kalır [AGENTS §3]
- **ŞARTLI** — ⑤ sahne sayıları ayrışıyor: ② DEVAMLILIK 22 · ④ HİKAYE 24 · ⑤ ARKA PLAN 23 · ⑥ FİZİK 24 · ⑦ AKSİYON 24 · ⑧ EFOR 24 · ⑨ KADRAJ 24 · ⑩ OYUNCULUK 24 · ⑪ IŞIK 24 · ⑫ HOOK 24 · ⑭ HAREKET 24 · ⑮ YÖN 24
- **NOT** — ⑤ süre ekseni doğrulandı — 14 mercek, ortanca (14 mercek) 239 s (±23.9)
- **NOT** — ①.9 teslim ekseni doğrulandı — plan 7 sahne (24 klip) sahne, 10 merceğin çoğunluğu 24 [D188] · kaynak: THE_LAST_GATE_PLAN.md
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `11-1-11--11-11-11-------` (9 mercek); sapan: ① KARE, ② DEVAMLILIK, ⑥ FİZİK, ⑮ YÖN<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **ŞARTLI** — ⑤ replik sayıları ayrışıyor: ① KARE 8 · ② DEVAMLILIK 10 · ③ SES 9 · ④ HİKAYE 10 · ⑥ FİZİK 9 · ⑦ AKSİYON 10 · ⑧ EFOR 10 · ⑨ KADRAJ 8 · ⑩ OYUNCULUK 8 · ⑪ IŞIK 8 · ⑫ HOOK 10 · ⑭ HAREKET 10 · ⑮ YÖN 8<br>alıntı kimin yanıldığını söyler; LINES HEARD satırları yan yana okunur
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
