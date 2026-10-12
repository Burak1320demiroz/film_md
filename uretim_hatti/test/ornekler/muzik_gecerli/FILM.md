# 🎬 TEST — deneme

```
FILM           TEST_FILM
FORMAT         yatay 16:9
HEDEF_SURE     0:30
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/TEST_FILM/
```

## 1. HİKÂYE

```
LOGLINE   A pilot must dock blind.
AMAÇ      kenetlenmek
ENGEL     kamera kör
KARAR     mühendisin sesine güvenir
SONUÇ     kancalar kapanır
BEDEL     son yakıt · sahne 2
TEK SORU  kenetlenecek mi?
```

## 2. TRETMAN

| Sahne | Süre | Ne olur | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:12 | yaklaşma | |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Karakter — yüz + giysi | `1.KARAKTER_v1.png` | v1 | | ⬜ | C02 |
| 2 | Mekân — kokpit | `2.KOKPIT_v1.png` | v1 | | ⬜ | C02 |

## 4. ÇEKİM LİSTESİ

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | istasyon dev ve dönüyor | small ship approaches a huge rotating station | wide, locked | ship left to right | 10 | Text to Video | — | — | G01 | ⬜ | — | — | — |
| C02 | ekran karardı | the cockpit display goes black, her hand stays on the grip | MCU | — | 10 | Frames to Video | T06 → ekran yazısız | 1.KARAKTER · 2.KOKPIT | G01 | ⬜ | — | — | — |
| C03 | kenetlendi | four hooks close around the collar | wide exterior | — | 10 | Text to Video | — | — | G01 | ⬜ | — | — | — |

## 5. REPLİKLER

| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| 1 | C02 | 1.0 | mühendis | telsiz | HUMAN | "Stay with my voice." | 2 |

## 6. SES PLANI — model sesi kullanılmaz

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 | kokpit uğultusu · telsiz | — | |

### ORTAM YATAĞI
| Yatak | Mekân | Çekimler | Ne (İngilizce) | Seviye | Dosya |
|:--:|---|---|---|:--:|---|
| Y1 | kokpit | C01-C03 | low steady cockpit hum, no rhythm | −18 LUFS | ses/yatak_kokpit.wav |

### GEÇİŞ
| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | yatak sürer, J 1 s | aynı mekân |
| C02→C03 | karisim 0,5 | yatak çapraz 1 s | iç → dış |


## 7. MÜZİK PLANI
```
OKUMA        İzleyici bu filmi güven olarak okumalı.
MÜZİKSİZ     C02
VURUŞ/SUSMA  0:10 · 0:20
FLOW MUSIC   faz 8
```

### MÜZİK PROMPTU
```text
Create a thirty-second original cinematic score for a blind docking in orbit. Open with a single sustained low cello note and sparse soft pulses, hold back until the display dies at ten seconds, then fall silent for the voice, and return with one warm resolving chord as the hooks close. Dry, intimate, no reverb tails. [Instrumental] No vocals, no drums, no riser.
```

