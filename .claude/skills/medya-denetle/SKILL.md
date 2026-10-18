---
name: medya-denetle
description: Yeni hat medya alımı (16.10.2026) — ~/film_medya/<FILM>/ altındaki referans, kare, deneme, ses ve montajı film klasörüyle karşılaştırır; NOTLAR DENEMELER'i yazar, DURUM'u dosyalardaki gerçek duruma getirir; hat dışında yapılmış montajı kesmelerinden bölüp plan çekimlerine eşler ve filmi kaldığı yerden hatta geri alır. /yeni-film açılışta dosya olarak okur; sahip /medya-denetle <FILM> ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(ls:*), Bash(mkdir:*), Bash(shasum:*)
---

# Medya denetle — medyayı hatta almak

**Neden (AGENTS §0 HAT v2):**
- 5 yeni hat filminin 5'inde de `~/film_medya/<FILM>/` boş, NOTLAR DENEMELER boş kaldı.
- Montaj hat dışında yapıldı; DURUM montajdan sonra hâlâ F7'deydi.
- QA raporlarının çekim numarası montajın kesme sırasıydı, plan numarası değil: MAYDAY'de hat C05 montajda yok, rapordaki C05 = hat C06.
- Sonuç: hiçbir kusurda "model mi tutmadı, referans mı yüklenmedi, yanlış deneme mi seçildi" sorusu cevaplanamadı.

Fable videoyu izleyemez. Bu skill hareketi değerlendirmez; dosyaları, kayıtları ve kareleri hizalar. Hareket kararı yine
sahibin işaretine, Gemini taramasına ve kare sayfalarına dayanır (AGENTS §1 ⑤).

## 1. Sahibe tek liste (bırakacağı yer)

| Ne | Nereye | Ad |
|---|---|---|
| referans sayfaları | `ref/` | `<No>.<AD>_v<k>.png` (FILM §3 No) |
| başlangıç kareleri | `kare/` | `Cxx.png` |
| denemeler — kullanılmayanlar dahil | `ham/` | `Cxx_dN.mp4` |
| replik · efekt · müzik | `ses/` | `R01.wav` · `E01.wav` · `muzik_v1.wav` |
| hat dışında yapılmış montaj | `cikti/` | `montaj_<GGAA>.mp4` (`taslak_` / `final` ile başlamaz) |
| QA raporu (metin) | film klasörü `ODA/HAM_QA_RAPORU.md` | — |

- Adı bilinmeyen dosya (`Gemini_Generated_Video_….mp4`) olduğu gibi bırakılır; adım 2 yeniden adlandırma listesi verir.
- Hangi referansın yüklendiğini, hangi metnin yapıştırıldığını sahip bilmiyorsa "bilmiyorum" der. Uydurulmaz.

## 2. Al

```bash
python3 uretim_hatti/araclar/medya.py durum <FILM> --yaz      # gerçek durum → ODA/MEDYA_DURUMU.md
python3 uretim_hatti/araclar/medya.py al <FILM> --yaz         # kayıtsız her deneme → NOTLAR DENEMELER
```
- **Adı kurala uymayan** dosyalar → sahibe `eski ad → yeni ad` listesi. Sahip yeniden adlandırınca adım 2 tekrar koşulur.
- `al`'ın **SHA** satırları → FILM §3 SHA sütunu (Fable, Edit). "DEĞİŞMİŞ" yazıyorsa referans sürümü artar.
- DENEMELER'deki `p:sha8` promptun **bugünkü** metnidir. Sahip başka bir metin yapıştırdıysa (kendi paketi, elle değişiklik) o satırın
  Prompt hücresine `sahip metni: <kaynak>` yazılır. SKY_CATCH'te sahibin paketi ile hattın F5 metni farklıydı ve fark sınıflamayı değiştirdi.
- İşaret (✅ aralık / ❌ neden → doğduğu yer) sahibin işidir; Fable boş bırakır, sahibe listeler.

## 3. Hat dışı montaj

```bash
python3 uretim_hatti/araclar/medya.py bol ~/film_medya/<FILM>/cikti/<montaj>.mp4 <FILM>
```
Çıktı `analiz/montaj/<ad>/bolum.md`: kesme sırası · zaman · ilk kare · en benzer başlangıç karesi.
1. Fable her parçanın `NN_ilk.png` / `NN_orta.png` karesini `kare/Cxx.png` ve çekimin "ekranda görünen" tarifiyle karşılaştırır.
   Benzerlik önerisi karar değildir.
2. NOTLAR **MONTAJ EŞLEMESİ** tablosu: kesme sırası · zaman · plan çekimi · deneme · nasıl doğrulandı. Belirlenemeyen parça `?` kalır.
3. Montajda olmayan plan çekimleri ve planda olmayan parçalar (ara parça, uzatma, tekrar) ayrı satır.
4. QA raporu varsa: her bulgunun `Cxx`'i bu tablodan plan çekimine çevrilir. Çeviri yapılmadan sınıflama yapılmaz
   (`uretim_hatti/QA_OKUMA_KILAVUZU.md`).
5. **kurgucu** (F8 modu, 1 çağrı): eşlemeden montajı `timeline.json` olarak geri kurar (dosya · giriş · çıkış), `kurgu.py kontrol`.
   Bundan sonra düzeltme hat içinde yapılır: yeniden üretilen çekim, kaydırılan kesme, kapatılan klip sesi.

## 4. DURUM ve teslim

- GERÇEK DURUM satırı DURUM `FAZ`'ından ilerideyse `FAZ · ADIM · SIRADAKI` düzeltilir; FAZ GÜNLÜĞÜ'ne `medya alımı: <satır>`.
- Montaj + QA varsa sıradaki iş çoğunlukla F8 (QA → düzeltme listesi) ya da F9 (paket).
- Sahibe **TESLİM** satırı ve eksik listesi (ref · kare · denenen · ✅ · timeline · taslak · final).

## 5. Yasak

- Medyayı silmek, taşımak ya da üzerine yazmak. Yalnız `analiz/` altına yazılır.
- Kullanılan referansı, denemeyi ya da prompt sürümünü tahminle doldurmak. Bilinmeyen `?` kalır.
- Benzerlik önerisini kareye bakmadan eşleme saymak.
- Görsel, video ya da ses dosyasını repoya koymak.

**Bütçe:** ajan çağrısı yok (Fable + araçlar); timeline'ı geri kurmak kurgucu ile 1 çağrı.

**İlk sınama** (dış eleştirinin önerisi, 16.10.2026): montajı bitmiş bir filmi medyasıyla bu skill'den geçir.
Öneri THE_WRONG_BURN: 12 çekim, tam döngüden geçti, sorunları biliniyor. Üç şey sınanır:
- sistem doğru durumu tanıyor mu;
- QA numaralarını plan çekimine çeviriyor mu;
- kaldığı yerden yayın paketine kadar gidiyor mu.
