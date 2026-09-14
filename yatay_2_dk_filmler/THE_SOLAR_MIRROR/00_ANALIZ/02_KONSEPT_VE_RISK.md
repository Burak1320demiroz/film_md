# 🔬 THE_SOLAR_MIRROR — KONSEPT VE RİSK ANALİZİ

> **Kaynak:** `KILAVUZ_REHBERI.md` §2.2 · `ONERME_VE_NOVUM_KILAVUZU.md` · `02_RISK_KARTLARI.md`

---

## 1. SAHİBİN TALEBİ VE KONSEPT TANIMI

Güneş Aynası dizisinin HELIOSTAT S04 segmentinde bakımdaki astronot Mara, segmentin yüzeyinde anomali keşfeder: ayna, bulunduğu bölgedeki elektromanyetik alanın 30 saniye sonraki optik konfigürasyonunu yansıtmaktadır. Mara aynada 30 saniye gelecekte mekiğinin güneş odak ışınıyla vurulduğunu görür. Real-time 30 saniyede mekiğe ulaşır, tether'ını çözer, kendi acil oksijen rezervini pnömatik RCS aktüatörüne bağlayarak mekiği itkiyle rotasından kaydırır ve mekiği kurtarır. Ancak oksijeni bittiği ve savrulduğu için kendi hayatını feda etmiş olur.

---

## 2. FORMAT, ORTAM VE PARAMETRELER

| Parametre | Değer | Gerekçe / Standart |
|---|---|---|
| **Format** | `yatay_2_dk_filmler` | 16:9 yatay sinematik format (§2.2) |
| **Süre / Sahne** | 12 sahne × 10 s = 02:00 (120 s) | §2.2 alt bandı (12-18 sahne) |
| **Klip Üretim** | 10 s (8 s Veo 3.1 + 2 s extend) | Veo 3.1 araç standardı [D124] |
| **Ortam Kartı** | §3.1 Vakum / Alçak Yörünge | Sıfır atmosfer, süzülme, termal radyasyon |
| **Tür** | Bilimkurgu (Sert Uzay Gerilimi) | Novum mühendisliği odaklı tek dal |

---

## 3. KONSEPT KAPISI (ÜÇ KABUL TESTİ)

```
[✅] TEST 1 — TEK KARE TANIMI
     "Dev Güneş Aynası segmenti (HELIOSTAT S04) önünde bakımdaki astronot Mara ve uzakta süzülen servis mekiği."
     Taşıyıcı nesne: HELIOSTAT S04 faz-konjugasyon aynası.

[✅] TEST 2 — KİNETİK BAĞIMSIZLIK
     Ayna statik bir dekor değildir; 30 saniye geleceğin optik projeksiyonunu sürekli dinamik olarak yansıtır.
     Sisteme dışarıdan enerji girmesiyle (RCS müdahalesi) görüntü dalgalanarak yeniden konverge olur (decoherence/reconvergence).

[✅] TEST 3 — BAŞLIK ŞEMASI
     "THE_SOLAR_MIRROR" — İngilizce 3 kelime, BUYUK_HARF_ALT_CIZGI. Novum nesnesinin doğrudan adıdır.
```

---

## 4. TEMA VE B5 HİKÂYE OMURGASI

### TEMA
> **Geleceği görmek özgürlük vermez. Yalnızca bedeli kimin ödeyeceğini seçme fırsatı verir.**

### B5 DÖRTLÜSÜ
1. **İSTEK:** HELIOSTAT S04 takılma arızasını gidermek ve mekikteki mürettebata emniyetle katılmak.
2. **ENGEL:** Solenoid aktüatör EM doygunluğu nedeniyle yanıt vermemektedir; uplink kopmuştur; tracking drift mekiğin LOX tankına kilitlenmiştir; zaman kısıtı tam 30 saniyedir.
3. **BEDEL (+ SAHNE NO):** 
   - S4'te tether kilidini bilinçli çözmek (savrulma bedeli).
   - S5'te acil suit O₂ rezervini pnömatik RCS hattına diverte etmek (hayat bedeli).
4. **MUHATAP:** Telsizden gelen mürettebat sesleri + Aynadaki 30s gelecekteki kendi cansız bedeni.

---

## 5. RİSK KARTLARI VE MALZEME DEĞERLENDİRMESİ

`02_RISK_KARTLARI.md` uyarınca malzeme ve ortam riskleri:

1. **Risk 1 — Vakum ve Yörünge Fiziği (§3.1):** Yerçekimi yok; momentum korunur. Sıfır-g momentum kilidi (D198) zorunludur.
2. **Risk 2 — Ayna Yüzeyi ve Yansıma Dynamics:** Aynada gelecek görüntüsünün fotogerçekçi optik kırılmayla işlenmesi, CGI hissinden kaçınılması.
3. **Risk 3 — Kask Vizörü Opaklığı (D197):** Kask camının şeffaf kalması, yüz ifadesinin sürekli okunabilmesi.
4. **Risk 4 — Vakumda Işık Hüzmesi:** Güneş odağı ışınının vakum boşluğunda çizgi olarak görünmemesi; sadece çarptığı çelik yüzeydeki ergime ile belli olması.
5. **Risk 5 — Metin & HUD Yasağı:** HUD verilerinin prompt metinlerine girmemesi; kurguda overlay olarak eklenmesi.

**Sonuç:** Malzeme azaltılmasına gerek yoktur. Senaryo 3 tur revizyonla optimize edilmiş, riskler kontrol altına alınmıştır.
