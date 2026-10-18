# ✂️ SEÇİM VE KURGU KILAVUZU — denemeden filme: seç, bağla, doldur, kontrol et

> **Ne için:** dört filmde yanlış deneme seçildi (WRONG_BURN C11↔C12 — ⚠️ 16.10 düzeltme: seçim değil tasarım, ARASTIRMA/16 §D 3), eksen atladı (SKY C05→C06, C11→C12; QA no. → plan C04→C06, C12→C13), ters el geldi (SKY C17→C18; → plan C20 → planda olmayan insert),
> süre tutmadı (SKY 02:41 / 04:00), her 10 s'de ses koptu (PLANET); montaj hattın araçları dışında yapıldı (`ARASTIRMA/11` §B).
> Bu kılavuz sahibin medya koyduğu andan taslak filme kadar iş sırasını ve kararları verir.
> **Kim okur:** kurgucu · zincir-bekcisi · devamlilik · Fable · sahip (F7-F8). `klip-sec` skill'inin yöntem eki.
> **Kaynak:** `ARASTIRMA/ham/30` → `ARASTIRMA/13_SUZME_20261016.md` §B4. Tamamlayıcı: `GECIS_VE_SES_SUREKLILIGI.md` · `REPLIK_VE_KLIP_SESI_KILAVUZU.md` ·
> `GPT_IMAGE_OMNI_KILAVUZU.md` §3, §12, §15.
> **Tarih:** 16.10.2026.

---

## 1 · İş sırası

```
1 sahip medyayı koyar     ~/film_medya/<FILM>/ref/  kare/Cxx.png  ham/Cxx_dN.mp4  ses/R<nn>.wav
2 Fable ölçer ve bakar    ffprobe (süre, oran, fps) · kareler.py cikar (0,5-1 s) · kuyruk · freezedetect · kare incelemesi
3 karar önerisi           çekim başına §3 kararı + kullanılabilir aralık → NOTLAR İŞARETLEME (öneri, "Fable" yazılı)
4 sahip izler ve işaretler normal hızda; hareketi, ayağı, temas hissini, sesi sahip onaylar (§8)
5 timeline.json           seçilen aralıklar · gecis · yataklar · klip_sesi
6 kapılar                 kurgu.py kontrol + §9 (replikler hazır mı, klip sesi kapalı mı)
7 taslak                  kurgu.py taslak → kesmelerde kareler.py dikis → sahip + ≥2 gerçek izleyici
```
Montaj başka bir programda yapılırsa da **seçim ve aralıklar timeline.json'a yazılır**; aksi hâlde QA bulgusu çekime ve denemeye geri bağlanamaz.

---

## 2 · Bir denemeyi değerlendirmek

- **Tek başına değil, komşularıyla:** önceki planın son kullanılabilir karesi → bu denemenin giriş karesi → sonraki planın başı.
  Işık yönü, hareket yönü, bakış, nesne durumu, kimin nerede olduğu (dünya yerleşimi) aynı mı.
  WRONG_BURN C11 tek başına hareketliydi; C12 ile yan yana konunca film "son iki sahne birbirini yalanladı" oldu.
  (⚠️ 16.10: C11'in promptu zaten istasyondan uzaklaşmayı istiyordu; çelişkinin kökü seçim değil plan + eksik replikler — ARASTIRMA/16 §E. İlke geçerli, örnek seçim hatası değil.)
- **Baş ve son:** ilk saniyelerde ısınma bozulması, son saniyelerde donma ya da erime olabilir (ölçülecek: `kareler.py kuyruk` + freezedetect).
- **Hikâyedeki işi:** çekim kartındaki "anlatacağı bilgi" bu denemede görünüyor mu. Görünmüyorsa güzel olsa da seçilmez.

---

## 3 · Beş karar

| Karar | Ne zaman | Not |
|---|---|---|
| **kullan** | aralık temiz ve komşularla uyumlu | aralık NOTLAR'a: `✅ 00.5–09.8` |
| **kırp** | temiz kısım var ama baş/son bozuk | ≥10 s gerekiyorsa §6 |
| **kareyi düzelt** | hata ilk karede (yüz, giysi, durum, oran) | `KIMLIK_VE_REFERANS` §6 → yeni deneme |
| **ara plana çevir** | ana öznenin yüzü bozuk ama ortam/nesne iyi; ya da çelişki örtülecek | insert, tepki planı, kesme noktasını kaydırma |
| **yeniden üret** | ana özne ya da ana olay bozuk; komşularla hiç bağdaşmıyor | AGENTS §4: aynı sebeple iki deneme bozuksa yaklaşım değişir |

**Karar ağacı (kısa):**
- Kimlik hatası **ana öznenin yüzünde ve süre boyunca** → yeniden üret (kareyi kontrol et). **Bir anlık** → o anı dışarıda bırakan aralık ya da tepki planı.
  **Arka planda/odak dışında** → kırp ya da ara plan.
- Nesne durumu çelişkisi: nesne **ana odak** → yeniden üret; **yan öğe** → kesmeyi nesnenin görünmediği âna kaydır ya da insert.
- Eksen ya da yön hatası → §4.
- Süre eksik → §6.
- Donan son → kırp; sonraki plana kesme ya da kısa karışım.
- Vakuma aykırı ya da istenmeyen ses → kurguda değiştir (`REPLIK` §4); görüntü yeniden üretilmez.

---

## 4 · Kesme sürekliliği

- **Eksen ve ekran yönü:** iki kişi/iki araç geniş planda bir kez yerleşir; ardışık planlarda aynı tarafta kalır. Eksen aşılacaksa yeni coğrafya görünür kurulur.
- **Yatay aynalama** (kurguda, maliyetsiz) eksen hatasını düzeltebilir — **yalnız** şu yoksa: tek taraflı rozet ya da işaret, yazı, tanınır kıyı/kıta,
  kimin **hangi eliyle** iş yaptığının kadrajda görünmesi (aynalama sağ eli sol yapar). SKY C18'deki ters el tersine bu yolla düzelebilir; C17 ile birlikte bakılır. (QA no.; C18 planda olmayan bir el insert'i, C17 = plan C20 — ARASTIRMA/16 §E.)
- **Bakış:** A sağa bakıyorsa karşı plandaki B sola bakar. Bakış kayıyorsa kesme baş dönüşünün başladığı âna alınır.
- **Nesne durumu:** açılan kapak sonraki planda kapalı başlamaz. Çelişki → §3.
- **Işık ve renk:** sahne grubunda ortak son görünüm; sıçrama kesmede `karisim` 0,3-0,8 s ile yumuşar (`GECIS_VE_SES_SUREKLILIGI`).
- **Plansız parça yok:** çekim listesinde olmayan bir parça (WRONG_BURN C07b'deki istasyon duvarı) araya girmez.

---

## 5 · Ses sürekliliği (kurguda)

- Mekân başına **tek kesintisiz yatak** klip sınırlarını aşar (`timeline.json` `yataklar`); mekân değişiminde 1-1,5 s çapraz. PLANET'teki "her 10 s'de ses sıfırlanıyor" yatak kurulmadığı için oldu.
- Replik kesmeden önce ya da sonra taşar (J/L, ~0,5 s).
- Müzik kesmede kesilmez; susması gerekiyorsa karar ya da sonuç anında (MAYDAY 01:39'daki bıçak kesme).
- Klip sesi varsayılan kapalı (`REPLIK` §4).

---

## 6 · 10 saniyeyi doldurmak

Hat kuralı: her video parçası 10 s (sahip, 08.10.2026; `kurgu.py kontrol` denetler). Kullanılabilir aralık kısa kalırsa sırayla:

1. Aynı çekimin **başka denemesi**.
2. **Devam üretimi:** temiz son kareden aynı açıyla devam (`GPT_IMAGE_OMNI_KILAVUZU` §8 A) ya da Omni sahne uzatma (10 s adımlarla; resmî, `FLOW_GERCEKLERI` Ek 2) → uzatılmışın uygun aralığı.
3. **İki denemeyi birleştirmek:** aynı çekimin iki denemesinin temiz kısımları, kadrajdan geçen bir nesne ya da hareketin arkasında gizli kesmeyle. Dikiş `kareler.py dikis` ile bakılır.
4. **Sonuç planı:** olayın sonucunu gösteren yeni bilgi taşıyan plan (aynı parçanın içinde ya da çekim listesinde yeni çekim).

Yok: yavaşlatma, döngü, donmuş kare uzatma, bozuk görüntüyü bekletme. Görüntü değişmiyorsa ya konuşma yeni bilgi verir ya da beklemenin dramatik nedeni vardır.

---

## 7 · Mekanik kontroller (yerelde, ffmpeg)

| Kontrol | Komut / araç | Yakalar | Kaçırır |
|---|---|---|---|
| Süre, oran, fps | `ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:format=duration -of json <dosya>` | 3:2 kare, kısa klip | — |
| Donma | `ffmpeg -i <dosya> -vf freezedetect=n=0.001:d=1 -f null -` (varsayılan n 0.001, d 2 s) · `kareler.py kuyruk` | donan son, takılma | çok yavaş gerçek hareketi donma sanabilir |
| Gizli kesme | `ffmpeg -i <dosya> -vf scdet -f null -` · `kareler.py kuyruk` | klip içinde ani sahne değişimi | yavaş geçiş |
| Kesme dikişi | `kareler.py dikis` (SSIM/PSNR + şerit + fark) | renk/ışık/konum sıçraması | anlamsal çelişki (kim nerede) — bayrak, karar değil |
| Sessizlik | `ffmpeg -i <dosya> -af silencedetect=n=-50dB:d=0.5 -f null -` | ses boşluğu, yatağın kopması | sesin doğru olup olmadığı |
| Yükseklik | `kurgu.py yukseklik` | −14 LUFS · ≤ −1 dBTP | — |
| Timeline | `kurgu.py kontrol` · `kurgu.py liste --zaman` | eksik dosya, geçersiz aralık, 10 s parça, QA zaman kodu → çekim | — |

PySceneDetect, scikit-image, OpenCV makinede kurulu değil; ffmpeg karşılıkları yeter.

---

## 8 · Kim neyi görebilir

Fable videoyu oynatamaz; çıkarılmış kareleri (0,5-1 s aralık) ve ölçümleri okur. Son söz sahibin normal hızda izlemesidir (AGENTS §1 ⑤).

| Hata | Kareden (Fable) | Ölçümden | İnsan (normal hız) |
|---|:--:|:--:|:--:|
| Başka yüz, giysi/bant/bayrak, yazı | ✅ | ΔE₀₀ (bant, aracı eklenirse) | ✅ |
| Duman, damla, plansız mekân, fazladan figür | ✅ | — | ✅ |
| Nesne durumu çelişkisi, iki planın birbirini yalanlaması | ✅ (yan yana karelerle) | — | ✅ |
| Eksen, ters el, ışık yönü | ✅ | dikiş farkı (bayrak) | ✅ |
| Donma, gizli kesme | ◐ | ✅ freezedetect · scdet · kuyruk | ✅ |
| 1 s'den kısa bozulma, parmak erimesi | ✗ (aralık arası kaçar) | — | ✅ |
| Ayak kayması, ağırlıksızlık hissi, temasın inandırıcılığı, hız | ✗ | — | ✅ |
| Dudak senkronu, replik kelimeleri, ses kimliği | ✗ | sessizlik/düzey · (Whisper varsa kelime) | ✅ |
| Ritim, duygu, "anlaşılıyor mu" | ✗ | — | ✅ sahip + ≥2 gerçek izleyici |

Fable'ın kare incelemesi **öneri** üretir; sahibin işareti yerine geçmez. "AI izleyici simülasyonu" izleme formundaki gerçek izleyici satırının yerine yazılmaz.

---

## 9 · Taslağı izletmeden önce (kapı)

1. Her video parçası 10 s; `kurgu.py kontrol` ❌ yok.
2. Her çekimin seçilen denemesi ve aralığı NOTLAR'da; sahibin işareti var.
3. Replikler hazır ve yerinde (`REPLIK` §2'nin yedi maddesi).
4. Klip sesi yalnız model sesi repliği taşıyan parçalarda açık.
5. Mekân yatakları kesintisiz; kesmede ses sıçraması yok (sessizlik ölçümü + kulak).
6. Ardışık planlarda eksen, yön ve nesne durumu tutuyor (kareler yan yana).
7. Kimlik kabul listesi (`KIMLIK` §9) seçilen her çekimin kullanılan aralığında tutuyor.
8. Donma ve gizli kesme bayrakları bakıldı.
9. Açılış (C01-C03) sorunu ve vaadi sesi kapalıyken de okutuyor (`ILK_30_SANIYE_KILAVUZU`).
10. Sahip normal hızda baştan sona sesli izledi.

---

> **Bu dosya ne zaman değişir:** `kareler.py` / `kurgu.py`'ye yeni kontrol eklenince §7; ısınma/donma eğilimi ölçülünce §2. Kaynaksız satır girmez.
