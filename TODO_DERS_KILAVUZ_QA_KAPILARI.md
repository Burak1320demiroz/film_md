# ✅ TODO — DERS · KILAVUZ · QA KAPILARI (açıldı 01.09.2026)

> **Kalıp:** `TODO_TEMA_VE_ACI_KAPILARI.md` gibi — tarihli, ölçümlü, doğrulama
> komutlu çalışma listesi. Faz bitince kutu işaretlenir; kalıcı bilgi ilgili
> kılavuza/betiğe taşınır; **tüm fazlar bitince bu dosya silinir.**
> **Kural:** buraya sayı yazılan her satır **01.09.2026 kesitidir**; güncel
> sayı `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → 🧭 bloğu.
> **Sıra:** fazlar leverage'a göre; ⛔ = başkasına bağlı, ⏳ = ölçüm bekliyor.

---

## 🩺 TEŞHİS — dört cümle, dördü de ölçülmüş

```
① DERSLER    ders bir METİN; modeli yalnız KAPI durdurur. 162 dersin 99'u hiçbir
             plan/prompt/QA kapısında değildi; D45+ 118 dersin etkisi hiç ölçülmedi
             (mod D = 0); yazıldıktan sonra 9 kez tekrarlayan ders vardı; emekli
             edilen ders 0. Bir ders sabah yazılıp AYNI GÜN yazılan filme ulaşmadı
             (D157 → THE COLD WELD).
② KILAVUZLAR okunmak için yazılmış, hiçbir şey okumuyor: 34 dosya · 838 KB · ~286k
             token; "her filmde okunacaklar" 19 dosya · 332 KB · ~113k token;
             25/34 kılavuzun adı hiçbir betik/listede yok; REHBERİ 1442 satır
             ("içerik anlatmaz" diyen dosya); DÜRÜST KAYIT 11 dosyada — düzeltme
             SİLMİYOR, altına EKLİYOR.
③ QA         ölçüm aleti kendi çıktısını denetlemiyordu: 6 rapor/5'i kendi
             aritmetik kapısından geçemedi; rubrikler 244 KB; T1-T4'te 2/77 film;
             SPEC yazılıyken mod V koşulan film 9; plan aşamasında "izleyici bu
             kuralı anlar mı" diye soran rubrik YOK (PROMPT_QA'da novum 0 kez).
④ YAYIN      08_YAYIN_PERFORMANS_TABLOSU 0 satır. Bütün alet bir VEKİLE (rubrik)
             karşı kalibre; vekil gerçek izleyiciyle hiç karşılaştırılmadı.
```

## 📊 BAŞLANGIÇ ÖLÇÜMÜ — 01.09.2026 kesiti (bitişte aynı tablo yeniden basılır)

| ölçüm | 01.09.2026 | hedef (bitiş) | nereden okunur |
|---|:--:|:--:|---|
| KAPI satırı olan ders | 12 / 162 | yeni ders %100 · dokunulan eski %100 | sayac 🧭 |
| ⛔ ÇALIŞMIYOR damgalı ders | 4 | her biri "→ araca çevrildi" | sayac 🧭 |
| mod D koşusu (02/ ham) | 0 | ≥ 3 | sayac 🧭 |
| kapısız kılavuz (adı betik/listede yok) | 25 / 34 | zorunlu 19'un 19'unda KAPI KARTI | Faz 2 doğrulama |
| zorunlu okuma listesi | 19 dosya · 332 KB | faz başına ≤ 4 dosya · ≤ 60 KB | Faz 3 doğrulama |
| rubrik hacmi | 244 KB (6/6 tavan üstü) | ≤ 150 KB (6/6 ≤ 25 KB) | sayac 🧭 |
| T1-T4'te geçerli satırı olan film | 2 / 77 | ≥ 5 | sayac 🔍 |
| D70/72 · D129 tekrar sayacı | 9 · 9 | durdu (araç sonrası 0 yeni vaka) | DERSLER TEKRAR satırı |
| yayın tablosu | 0 satır | 1 film + tutundurma eğrisi | 08_YAYIN_PERFORMANS_TABLOSU |
| ⑪ koşulmuş film | 1 (Cold Weld · 01.09) | her üretilen filmde | 01_FILM_RAPORLARI §⑪ |

---

## ✅ FAZ 0 — BUGÜN YAPILDI (01.09.2026)

- [x] **`RAPOR_KONTROL/rapor_kontrol.py`** — QA raporunun çıktı kapısı (n·Σ·ort · tally ·
      kaynaksız hücre · şerit · ⑨ ızgara · ④ harita · ② sayaç boşluğu · ⑤ çapraz +
      SUSKUNLUK). 12 rapora koşuldu: elle bulunanların tamamı + elden kaçan 3.
- [x] **`qa-isle/scripts/rubrik_paketle.sh`** — rubrik + SPEC mercek başına tek dosya;
      mod D VARSAYILAN (D129 · 9 film). Cold Weld paketleri hazır.
- [x] **`olcum_kapisi.sh` → KUYRUK/BAŞ KART** (freezedetect + `son_kare.jpg`) — D70/72 9. vaka.
- [x] **`prompt_kontrol.py` ⑭ NOVUM TAŞIYICI (D157) · ⑮ SIRT POZİTİF (D139)** — 128 dosyada
      kalibre; karar değişen tek dosya (FROST LINE PART_A, gerçek bulgu).
- [x] **`DERSLER/00_DERS_YAZIM_KONTRATI.md`** — dört kader · KAPI/TEKRAR satırları ·
      ≥3 tekrar → ⛔ ÇALIŞMIYOR + dönüştürme borcu · geriye dönük tasnif YOK.
- [x] **`DERSLER/GOZLEM_DEFTERI.md`** — ADAY-1 (yoklukla kanıtlanan kural, kapatma komutlarıyla).
- [x] 12 derse KAPI satırı; D70·D72·D94·D129 ⛔ ÇALIŞMIYOR → araca çevrildi.
- [x] **`sayac.sh` 🧭 DERS → KAPI bloğu** (kapılı ders · ÇALIŞMIYOR · aday · mod D · son 5
      film dersi · rubrik hacmi).
- [x] AGENTS (§1 · ①.5 · ⑤ beşinci satır · ⑪ · kart B · kart G · §7) · REHBERİ §6 (5.7 ·
      7d · 8) · `qa-isle` · `yeni-film` skill'leri · TEMA §3c bayat liste düzeltmesi.
- [x] D161 · D162 yazıldı (alet dersleri); D161'in ① abartısı düzeltildi.

---

## ✅ FAZ 0b — POLİTİKA / ÜRETİLEBİLİRLİK HATTI (01.09.2026, aynı gün)

> Tetikleyici: üretim reddi. Depo 14 redi 27 dosyaya yazmış, hiçbir yerde
> toplamamıştı; kelime ekseninin kapısı yoktu ve "betik göremez" deniyordu.

- [x] **`FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md`** — red sayılarının TEK sayaçı.
      14 vaka geriye dönük (6 kelime · 4 kompozisyon · 1 yapısal · 3 teknik parti).
      Açılış bulgusu: **13/14 satırda MOTOR yazmıyor · 2 satırda SONUÇ yok.**
- [x] **`POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`** — depodaki **ilk KAPI KARTLI kılavuz**
      (Faz 2'nin şablonu, sahada denenmiş hâli). §2 sözlük · §3 kompozisyon ·
      **§4 AKSİYON BÜTÇESİ + anlam maliyeti** (05_DIKEY_HAT §3'ün panzehiri) · §5 merdiven.
- [x] **`prompt_kontrol.py` ⑯ POLİTİKA SÖZLÜĞÜ** — D123'ün "betik göremez" satırı
      KELİME ekseninde yanlıştı. 140 kayıtta kalibre; dört yanlış-pozitif sınıfı
      kapatıldı (wound→gemi gövdesi · skeleton→oran tarifi · stab→müzik terimi ·
      "drives his"→kendi uzvu). **Kararı değişen dosya 0** — kapı bugün üretim
      durdurmuyor, bilgi üretiyor (`POLITIKA_BANDI_KARARA_BAGLI = True`).
- [x] **`PROMPT_QA_CRITIQUE_PROMPT.md` §3c KOMPOZİSYON YÜZEYİ** — betiğin
      göremediği tek eksen, dört soru (YERCEKIMI F1 S8'den).
- [x] **`02_RISK_KARTLARI` KART 12** (payda 12→13) · **`03_PLAN_ONCESI` B6** ·
      **`FILM_KLASOR_SABLONU/FILM_PLAN.md` POLİTİKA SATIRI** · `sayac.sh` 🚫 bloğu.
- [x] **Çelişki kapatıldı:** `SAHNE_DEVAMLILIK_KILAVUZU` karakter çapası örneği
      *"Turkish woman"* öğretiyordu, §7 milliyeti yasaklıyordu. Örnek düzeltildi —
      ama kopyası **üç filmin canlı promptlarında duruyor** (defter §3, açık borç).
- [x] `KILAVUZ_REHBERI` §7'nin "prompt_kontrol.py bunu göremez ve göremez de"
      satırı **yerine yazıldı** (altına eklenmedi — Faz 3 eksiltme kuralı).
- [ ] ⏳ **Ders YAZILMADI, bilerek** [kart Y sırası: veri → belge → ancak tekrarlarsa ders].
      D123 zaten var; bu tur onu KAPIYA çevirdi. Yeni ders ancak ⑯ kapısı
      tetiklendiği hâlde red gelirse yazılır.

**Açık borç (bu fazdan çıkan):**
- [ ] Üç filmin promptlarından milliyet ifadesini çıkar: `THE_DEAD_APPROACH` (16 geçiş) ·
      `THE_KALEIDA_CRASH` (14) · `THE_HOLLOW_STATION` (2) — ⑯ üçünde de BLOCK veriyor
- [ ] ⏳ Defterde ≥5 MOTOR'lu vaka birikince `POLITIKA_BANDI_KARARA_BAGLI` kapanır,
      T1 BLOCK'a çıkar ve §6 motor tablosu dolar

---

## ✅ FAZ 0c — TUR 3 DIŞ ARAŞTIRMA SÜZÜLDÜ (01.09.2026, aynı gün)

> Dört motor için dört derin araştırma koşuldu. **On iddia elendi, on yedisi girdi.**
> Elek: `04_ARASTIRMA_BULGULARI.md` **TUR 3** — kural buradan okunmaz, kuralın
> NEREDEN geldiği buradan okunur.

- [x] **`04_ARASTIRMA_BULGULARI` TUR 3** — T3.1 dört hüküm · T3.2 **girmeyenler**
      (filtre atlatma teknikleri · `photorealistic`→`3D animation` önerisi ·
      jailbreak oranları · payda bizim olmayan red oranları · iki raporun
      birbiriyle çelişen spec'leri) · T3.3 uygulama kaydı · T3.4 üç açık çelişki.
- [x] **`POLİTİKA §1.0` (yeni)** — mekanizmanın ADI bulundu: filtre ŞİDDETİ değil
      **OLASILIĞI** puanlıyor; denetim **ÜÇ KATMANLI** (depo ortadakini bilmiyordu);
      ücretli kademe filtreyi gevşetmiyor (bir hipotez öldü).
- [x] **`POLİTİKA §1` mesaj ağacı DÜZELTİLDİ** — *"Sorry, something went wrong"*
      her zaman teknik değil: **üretim görünür şekilde ilerleyip sonda düştüyse
      maskeli ÇIKTI reddidir.** Defterde `İLERLEDİ` sütunu açıldı.
      ⛔ RING LIGHT (3 red / 0 başarı) geriye dönük çözülemez: o gün bu soru sorulmadı.
- [x] **`POLİTİKA §3` iki yeni kompozisyon imzası** — ⑥ yüzü kapatan ekipman
      (anonimlik imzası) · ⑦ kırmızı ton yoğunluğu + yakın plan.
      **İkisi de bu deponun VARSAYILAN malzemesi ve şimdiye kadar hiç sayılmadı.**
      + **§3.2 kadraj genişliği bir politika değişkenidir** (ECU→WS risk merdiveni).
- [x] **`POLİTİKA §5` iki değişiklik** — basamak **2.5 SESSİZ KOŞU** (diyalog ayrı
      ses denetim dalı açıyor; teşhis bedava) · basamak **6 I2V YENİDEN YAZILDI**.
- [x] **`POLİTİKA §6` motor tablosu doldu** + §6.1 seçim kuralı + §6.2 iki maliyet
      gerçeği (reddedilen üretim kredi iade ETMİYOR).
- [x] **`KILAVUZ_REHBERI §7`** — I2V reçetesi ve mesaj tablosu düzeltildi (yerine yazıldı).
- [x] **`02_RISK_KARTLARI` KART 12** — dört malzeme daha (kask · kırmızı ton ·
      kalabalık · diyalog), üçü varsayılan malzeme.
- [x] **`prompt_kontrol.py`** — `naked` eklendi (`naked eye` muaf, kalibrasyon ⑤);
      D79 vizör bulgusu artık üretilebilirlik gerekçesi de taşıyor.
      ⛔ `shot`/`fire`/`strike` **EKLENMEDİ**: ölçüm 3.605 · 496 · 154 geçiş —
      eklenseydi her video promptu yanlış bayrak yerdi.
- [x] **D123'e KAPI + TEKRAR satırı ve DIŞ DOĞRULAMA** — ders kontratına uygun.

**⛔ EN ÖNEMLİ ÜÇ CÜMLE (yeni film yazan buradan okusun):**
```
① I2V bir KURTARMA değil RİSK TAKASI. Kompozisyon reddine I2V uygulamak,
   reddedilen kadrajı ikinci bir denetime sokmaktır.
② KASK + KIRMIZI IŞIK + KALABALIK + DİYALOG — dördü de bu deponun
   varsayılan malzemesi ve dördü de politika yüzeyi taşıyor. Hiçbiri
   yasak değil; hepsi PLANDA SAYILIR (KART 12).
③ "Üretim ilerledi mi?" sorusu, red gelince sorulacak İLK sorudur.
   Cevabı sonradan hatırlanamaz.
```

**Açık borç (TUR 3'ten çıkan):**
- [ ] ⏳ **I2V ↔ T2V prob'u** (2 klip) — soru DEĞİŞTİ: artık "hangisi az reddediyor"
      değil, "takas bizim malzememizde hangi yöne çalışıyor"
- [ ] ⏳ **"no celebrities" çelişkisi** (T3.4 ①) — 2 kliplik prob: aynı sahne,
      biri ön bloklu biri bloksuz. Depo kuralı (D123) şu an geçerli
- [ ] ⏳ **BÖLGE sorusu** (T3.4 ② · defter §4⑤) — Türkiye `personGeneration`
      kısıtlı bölgede mi? Ölçümü ucuz: tek insan, tek kare, temiz prompt
- [ ] ⏳ Motor hipotezleri (NB2 esnek · OMNI ünlü-kişi yanlış-pozitifi ağır) —
      defterde 3 MOTOR'lu vaka biriktiğinde kendiliğinden test edilmiş olur

---

## 🟡 FAZ 1 — İLK MOD D · THE COLD WELD  (⑪ KOŞULDU 01.09.2026 · QA yarısı DURDU)

> Master bulundu (`~/Downloads/the cold weld (1).mp4` · 4K · 155,075 s) ve ⑪
> koşuldu. **QA yarısı bilerek koşulmadı: master geçerli değil.** Tam kayıt:
> `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_COLD_WELD.md` §⑪.

### ✅ ⑪ ÖLÇÜM — bitti

- [x] ⑪.0 KİMLİK: aynı ada uyan İKİ dosya ölçüldü (4K master + 720p); ortadan kare
      çıkarıldı, SPEC C bloğunun altı çapası da tuttu → koşu devam
- [x] ⑪.1 KURGU KAPISI **3/3 GEÇTİ**: 14 gövde kesmesi + kart = 15 klip = plan ·
      gövde 150,10 s = plan 150 ± 2 · şerit plana birebir
      ⭐ raporların "14 / 16" kavgası çözüldü (16 diyenler kartın iki sınırını saymış)
      ⚠️ S13→S14 kesmesi 0,30 eşiğinde görünmedi, 0,15'te çıktı — iki sahne fazla benziyor
- [x] 🔴 **FİLİGRAN DOĞRULANDI** [D150 · 2. vaka] — sağ alt çeyrek, 6/6 örnek, cyan
      "play" üçgeni; 4K'da merkez ≈(3450,1800), köşeden %10/%17 içeride.
      ⭐ ⑤ bildirmişti, sahibi ① susmuştu → **D162 SUSKUNLUK kapısı ilk vakasında
      doğrulandı** · ⛔ %3 crop yetmez, temizlik kadrajın %12'sini götürür
- [x] 🔴 **KUYRUK KARTI DOĞRULANDI** [D70/D72 · 9. vaka] — 150,10 s → SON (4,98 s)
- [x] 🔴 **LOUDNESS İHLALİ** — I = −18,1 LUFS · Peak = 0,0 dBFS (kilit −14 / −1,0)
- [x] ✅ SES KANALI VAR, sessizlik yok → ③'ün "AUDIO STATE: B" beyanı doğrulandı [D136/D137]
- [x] 🚩 **ADAY-1 KAPANDI — hipotez YANLIŞ**: üç kanıt da ekranda (avuç makrosu 65 s ·
      diskli duvar 100-120 s · doruk 122 s). Sorun üretim değil OKUMA → D151'in 2. vakası
- [x] ⭐ **YENİ BULGU → D163**: S8-S11 blok takası (anahtar ↔ duvar); insan şeridi
      tek figürlü filmde sabit olduğu için ④c "SIRA DOĞRULANDI" demişti
- [x] Araç düzeltmeleri koşu sırasında: köşe testi **dört çeyreğe** çevrildi (sabit
      360×240 filigranı kaçırıyordu) · **SAHNE IZGARASI** eklendi (D163'ün kapısı)
- [x] Kilit defterindeki 9 ⬜ AÇIK maddenin 2'si kapandı, 2'si daraldı, 5'i mod D'ye kaldı

### 📥 DEVRALINAN — eski TODO'nun E fazı (01.09.2026)

`TODO_TEMA_VE_ACI_KAPILARI.md` E fazı buraya taşındı; pilot film + mod D geri
beslemesi Faz 1'in işiyle aynıydı. Devirle gelen üç uyarı:

- [ ] THE NEAR PASS üretilmedi ve **6/6 sahnesi ALT AÇI (1 tip)** — pilot o
      olacaksa açı yayı ÖNCE düzeltilir (SPEC'inde 🚨 AÇIK MADDE)
- [ ] THE OPEN SEAM doruğu (S4) **açısız** yazılmış; ACI_YAYI §9 doruğa en
      yüksek kontrast sıçramasını şart koşar
- [ ] Pilotun hedefi **≥3 açı tipi** — eski şablonlar (HELD HEAT · LAST SPAN)
      zombi türüyle kaldırıldı, çeyrek uzay hattından ölçülecek
- [ ] Hiç kullanılmamış tema (`sayac.sh` 01.09): **ZAMAN · KİMLİK · İLK TEMAS**

### ⛔ QA YARISI — master yeniden ihraç edilene kadar KOŞULMAZ

> [D150] «filigranlı master master değildir ve mercekler onu ölçmemiş sayılır.»
> Bu master'a koşulacak altı mercek koşulduğu anda geçersiz olurdu.
> ⭐ Kapı işini yaptı: altı temiz oturum ve saatler harcanmadan durdu.

- [ ] ⭐ **TEK SEANS, DÖRT İŞ** (ölçümle gerekçelendirildi — film kaydı §⑪.7):
      ① S8-S11 blok takası plan sırasına alınır [D163] — klipler mevcut, yeniden üretim YOK
      ② kuyruk kartı 150,10-155,08 kesilir [D70/72]
      ③ **filigransız ihraç** — filigran ihraç adımından geliyor (ham Veo klibi GRİ
        SPARKLE taşıyor, master CYAN PLAY ÜÇGENİ ⇒ farklı kaynak, yani AYAR)
        ⛔ delogo test edildi: filigran gidiyor ama 175×175 yumuşak yama kalıyor,
           taneli zeminde görünür ve ⑤ onu yeniden yakalar → ikinci tercih
        ⛔ kırpma elendi: %12 genişlik, ekran yönü kilidi bozulur
      ④ loudness −14 LUFS / −1,0 dBTP'ye normalize
      ⭐ kart §0.19 açılış-kapanış çiftini de öldürüyor (son kare levhadaki disk olmalı)
- [ ] ⑪ YENİDEN koşulur (kart yok · filigran yok · loudness kilitte)
- [ ] `rubrik_paketle.sh <film> <yeni master>` → künyeye süre/çözünürlük girer [D160]
- [ ] Altı paket, altı TEMİZ oturum [D110], aynı dosya [D75] → `*_HAM_D.md`
      (mod V ham raporları KORUNUR, üstüne yazılmaz)
- [ ] `rapor_kontrol.py <6 rapor> --film … --rapor` · beklenti: ①④⑥ TEKRAR değil ·
      ⑤ kesme yayılımı ≤1 · ② Counter artık N/A değil
- [ ] Kalan 5 ⬜ AÇIK madde kareyle kapanır (havadan ses · anahtar faz · anahtar ölçeği ·
      avuç sayacı a/b çifti · sayaç okuması)
- [ ] T tablolarına satır (yalnız rapor_kontrol GO/ŞARTLI derse) · 00_INDEX ·
      **V↔D farkı tek sayı olarak film kaydına** — aletin gürültüsü ilk kez ölçülür
- [ ] Doğrulama: `sayac.sh` → mod D koşusu ≥ 1 · ⏳ listesinden Cold Weld düşer

## FAZ 2 — KILAVUZ KAPI KARTLARI  (bana ait · ~1 gün · gövdeye DOKUNULMAZ)

> 25/34 kılavuz kapısız. Çözüm ders kontratının kılavuz hâli: her kılavuzun
> BAŞINA 15 satırlık kart; gövde olduğu gibi kalır (ek'e döner). Ajan kartları
> okur (~34 × 15 satır), gövdeyi yalnız kart yollarsa açar.

- [ ] **Kart şablonunu yaz** → `kilavuzlar_ve_sistem_dosyalari/00_KILAVUZ_KAPI_KARTI_SABLONU.md`
  ```
  ## 🎫 KAPI KARTI — <kılavuz>            (01.09.2026 kontratı · gövde aşağıda, ek'tir)
  NE ZAMAN:   KONSEPT / PLAN / PROMPT / KURGU / QA          ← tek faz, birden çok olamaz
  KURAL 1:    <tek cümle, SAYILI>                → KAPI: BETİK prompt_kontrol ⑦ | LİSTE 03_PLAN B2 | KARAR | ARŞİV
  KURAL 2-5:  …                                  (5'ten fazla kural = kılavuz değil, kitap)
  OKUMA:      gövdeyi AÇ eğer: <tek koşul — örn. "filmde sıvı temas varsa">
  BİLİNEN YANLIŞ: <DÜRÜST KAYIT'ların tek satır özeti + son kullanma tarihi (Faz 3 ③)>
  ```
- [ ] **Zorunlu 19 kılavuza kart** (REHBERİ §1 listesi) — öncelik büyükten küçüğe:
      UZAMSAL (58 KB) · SINEMATOGRAFIK (32) · HOOK (21) · TEK_CEKIM (18) · MESHUR_SAHNE (18) ·
      TEMA (15) · ONERME · FINAL · PAKETLEME · KARAKTER_VE_DUYGU · KURGU_RITMI · KAMERA_ACISI ·
      ACI_YAYI · SES_VE_DIYALOG · SENARYO_VE_VIRAL · SAHNE_DEVAMLILIK · YANASMA · VEO · IMAGE_VIDEO_TEMPLATES
- [ ] **Her kart satırı için kapı kararı** — kural betiğe inebiliyorsa `prompt_kontrol.py`'ye
      denetim (⑯+), inemiyorsa 03_PLAN_ONCESI'ne kutu, ikisi de değilse ARŞİV. Yeni betik
      denetimi başına kalibrasyon: 128 dosyada kaç karar değişti (Faz 0 yöntemi).
- [ ] **Kalan 15 kılavuza kart** (format/ortam/tür ekleri + sistem dosyaları) — ikinci tur
- [ ] `sayac.sh` 🧭'ye iki satır: `KAPI KARTI olan kılavuz  n / 34` · `karta göre kapısız kural  n`
      (grep `^## 🎫 KAPI KARTI` · `→ KAPI: ARŞİV` sayımı)
- [ ] `yeni-film` §1: "kılavuzu aç" → "KARTINI oku; gövdeyi OKUMA koşulu tutuyorsa aç"
- [ ] Doğrulama: `grep -L "🎫 KAPI KARTI" kilavuzlar_ve_sistem_dosyalari/*.md` → boş (34/34)

---

## FAZ 3 — REHBERİ FAZ LİSTESİ + EKSİLTME KURALI  (~yarım gün)

> 113k token'lık "değişmez" liste bir liste değil, itiraf. REHBERİ kendi kuralını
> ("içerik anlatmaz") ihlal ediyor: 1442 satır, §7 tek başına 231.

- [ ] **§1 "Her filmde okunacaklar" → BEŞ FAZA böl**, faz başına ≤ 4 dosya:
      KONSEPT (ONERME · TEMA · UZAY_SENARYO · SENARYO_VE_VIRAL §2) ·
      PLAN (HOOK · FINAL · PAKETLEME · KARAKTER_VE_DUYGU · 02_RISK · 03_PLAN_ONCESI) ·
      PROMPT (TEMPLATES · KAMERA_ACISI · ACI_YAYI · UZAMSAL · VEO · negatif çekirdek) ·
      KURGU (KURGU_VE_TESLIM · KURGU_RITMI · MUSIC) · QA (qa-isle skill · RAPOR_KONTROL)
      → geri kalanı "REFERANS — tetikleyici varsa" (kart OKUMA koşuluyla)
- [ ] **§7 BİLİNEN TUZAKLAR'ın 231 satırını üçe ayır:** betiğe inen (prompt_kontrol ⑯+) ·
      listeye inen (03_PLAN_ONCESI / 02_RISK) · arşive inen (hikâye) — her tuzağa tek satır
      karar; gövde `URETIM_ONCESI_ANALIZ/06_TUZAK_ARSIVI.md`'ye taşınır (silinmez)
- [ ] **§8 film matrisi** → `sayac.sh`'den üretilen bir çıktıya ya da `00_INDEX`'e işaret;
      elle tutulan 73 satırlık matris bayatlıyor (AGENTS §6 zaten kaydetmiş)
- [ ] **EKSİLTME KURALI'nı yaz** (AGENTS §4 yazım standardına bir madde):
      "DÜRÜST KAYIT bölümü 30 günde ya kurala döner ya silinir. Düzeltme ALTINA eklenmez,
      YERİNE yazılır; eski hâl git'tedir." + `sayac.sh` 🧭: `30 günü geçmiş DÜRÜST KAYIT n`
      (git blame tarihinden)
- [ ] Doğrulama: REHBERİ §1 faz başına dosya sayısı ≤ 4 · REHBERİ satır sayısı ≤ 900

---

## FAZ 4 — İZLEYİCİ OKUMASI (plan aşaması, sıfır kare)  (~2 saat)

> Üretimden önce planı okuyan tek yargı rubriğinde "novum · izleyici · yokluk"
> 0 kez geçiyor. Hikâye merceği yalnız videoya koşuyor. Boşluk burası.

- [ ] `PROMPT_KONTROL/IZLEYICI_OKUMASI_PROMPT.md` — ≤ 10 KB, tek dosya, plan + promptlar girdi:
  ```
  1. NOVUM TEK KARESİ taşıyıcının kendisi mi? (D157 · ⑭ betiğin insan yarısı)
  2. Kanıtların en az biri POZİTİF bir OLAY mı — yoksa hepsi bir şeyin OLMAMASI mı? (ADAY-1)
  3. Bu 15 promptu okuyan biri dünyanın kuralını TEK CÜMLEYLE söyleyebilir mi? Cümleyi yaz.
  4. Bedel hangi promptta KADRAJDA? (sahne no + saniye; "hissediliyor" cevap değil)
  5. S0'ın sorusu S1'de BÜYÜYOR mu, tekrar mı ediyor? (HOOK §3 ①)
  ÇIKTI: GEÇ / DÜZELT + her soruya sahne numarası. Skor YOK — bu bir kapıdır, tablo değil.
  ```
- [ ] `prompt-kontrol` skill §2'ye ekle (PROMPT_QA_CRITIQUE'in yanına, yerine değil)
- [ ] AGENTS kart P + REHBERİ §6 adım 3.5'e tek satır
- [ ] İlk koşu: THE COLD WELD planına (retrospektif) — ADAY-1'i kâğıt üstünde yakalıyor mu?
- [ ] Doğrulama: bir sonraki yeni filmin §0.14b'sinde "İZLEYİCİ OKUMASI: GEÇ/DÜZELT" satırı

---

## ⏳ FAZ 5 — RUBRİK DİYETİ  (~1 gün · ENFORCEMENT kısmı hemen, ÖZ kısmı Faz 1'den sonra)

> Kural rubrik metnine değil çıktı kapısına gider; rubrik metnindeki
> "ARITHMETIC GATE / SCORES SUMMARY ①-⑤ / PRESENCE STRING / LINES HEARD / CUTS
> COUNTED / NON-SCENE" blokları altı dosyada tekrar ediyor ve model uymuyor.

- [ ] **Hemen:** altı rubrikte ORTAK ÇIKTI-KURAL bloklarını ölç (`grep -c` "ARITHMETIC GATE|EVERY SCORE CELL|PRESENCE STRING|LINES HEARD is a transcript|NON-SCENE MATERIAL is not") → toplam KB
- [ ] Her rubrikte o blokları **tek paragrafa** indir + "denetim: rapor_kontrol.py" satırı;
      eski blok `QA_PROMPTLARI/ARSIV_CIKTI_KURALLARI.md`'ye (silinmez). Rubrik self-contained
      kalır (model paragrafı görür, ayrıntı betikte).
- [ ] ⏳ **Faz 1 sonrası:** V↔D farkı ve ⑩'da düşen bulgu türlerine göre ÖZ kısmı budanır
      (hangi kategoriler hiç sayı üretmiyor · hangi SPECIFIC CHECK hiç tetiklenmiyor →
      CALISTIRMA_KAYITLARI'ndan sayılır)
- [ ] Doğrulama: `sayac.sh` 🧭 rubrik hacmi 6/6 ≤ 25 KB · `rapor_kontrol.py` Cold Weld D partisinde aynı sonuçları veriyor

---

## ⏳ FAZ 6 — DERS ETKİNLİK TABLOSU  (betik hemen · anlam ≥ 3 mod D'den sonra)

> `01_DERS_ETKINLIK_RAPORU` 44 derste dondu. Kapılar artık ders numarasıyla
> konuşuyor (`[D157]`); tetiklenme / tekrar oranı sayılabilir.

- [ ] `kilavuzlar_ve_sistem_dosyalari/DERSLER/ders_etkinlik.py`: kaynaklar
      `PROMPT_KONTROL/RAPORLAR/*` + `RAPOR_KONTROL/RAPORLAR/*` ("[Dnnn]" tetiklenme) ·
      `DERSLER/*.md` TEKRAR satırları (tekrar) · 01_FILM_RAPORLARI ("D\d+ ×n" vakalar)
      → tablo: ders · kapı · tetiklendi · tekrarladı · oran · karar (TUTUYOR / ⛔ ÇALIŞMIYOR / ÖLÇÜLMEDİ)
- [ ] `sayac.sh` 🧭'ye özet satır: `tetiklenen kapı n · tekrarlayan ders n · ölçülmemiş n`
- [ ] ⏳ ≥ 3 mod D sonrası ilk tablo → emeklilik kararları KONTRAT §3'e göre
- [ ] `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` → "44 ders kesiti (01.08) — güncel tablo betikten" notu
- [ ] Doğrulama: tablo betikten üretiliyor, elle satır yok

---

## ✅ FAZ 7 — BİLİNEN ÇELİŞKİLERİN TEMİZLİĞİ  (BİTTİ 01.09.2026)

> ⚠️ **Sekiz madde yazmıştım; ölçünce ÜÇÜ gerçek çıktı.** Üçü zaten
> düzeltilmişti (grep'im düzeltme METNİNİ çelişki sandı), biri veri bekliyor,
> biri kendiliğinden kapandı. Bu satır silinmiyor: **"çelişki" listesi de
> ölçülmeden yazılırsa bayat olur** — listeyi yazan da kapıdan geçmeli.

### Gerçek çıkan üçü — DÜZELTİLDİ

- [x] ⭐ `IMAGE_VIDEO_PROMPT_TEMPLATES` — **teşhis yanlıştı, bulgu daha ağırdı.**
      Sorun `[CHARACTER BIBLE]` etiketi değil (satır 120 onu bilerek tutuyor).
      Sorun: **şablonun doldurulmuş örneği karakterin ÖZEL ADINI üç yerde
      kullanıyordu** — "Dr. Ada Yıldırım" (SCENE) · "Ada" (SUBJECT) · "Ada"
      (MOTION) — oysa 82 satır yukarıda kendi kuralı duruyor: *"Karakterin
      ADINI prompt gövdesine yazmayın (Ders 45)"*. Her yeni film bu örnekten
      yazılıyor → şablon kendi dersini kopyalatıyordu.
      **Yapıldı:** üç ad → "A lone suited figure" / "The figure"; örneğin
      başına kuralın NEDEN uygulandığını gösteren blok kondu.
- [x] `KILAVUZ_REHBERI` §4.1 "Tek kâşif, **hep yalnız**" mutlak yazılmıştı;
      depoda 25 dosyada iki figür var ve THE_ROSE_COAT §0.8b altı satırlık
      ayrım bütçesiyle 12 sahne boyunca kadraj kilidini tutturmuştu.
      **Yapıldı:** "VARSAYILAN tek kâşif · ikinci figür YASAK DEĞİL, BÜTÇELİ —
      novum gerektiriyorsa + üç kanal (siluet·kostüm·hareket) yazıldıysa;
      emsal ROSE COAT §0.8b · gerekçesizse iki yarım karakter [Kart 4·D20·D69]".
- [x] Ölü film atfı — **4 değil 2 yerdeydi.** `KILAVUZ_REHBERI` §3.1 "Referans
      film" ve `UZAY_SENARYO` dosya listesi hâlâ **THE_WAKING_GROUND**'a
      yolluyordu (depoda yok). **Yapıldı:** ikisi de → **THE_COLD_WELD**
      (doğrulandı: HARD VACUUM, §3.1'in ortam kartına oturuyor).
      ⚠️ Dokunulmadı: LAST SPAN / HELD HEAT geçen 6 yer **tarihsel kayıt**
      (zombi rafı notları, matris satırları, "depoda YOK" uyarısı) — bunlar
      çelişki değil, dürüst kayıt.

### Gerçek çıkmayan üçü — İDDİA GERİ ÇEKİLDİ

- [x] ~~§7 IMAGE bandı "1.700-2.100"~~ → **çelişki yok.** Kılavuz zaten
      *"IMAGE bandı ÖLÇÜLMEDİ (21.08.2026 düzeltmesi)"* diyor; grep sayıyı o
      düzeltme metninin içinde buldu. Betik de uyumlu: `IMAGE_BANDI_KARARA_BAGLI`
      ile band aşımını **NOT** (gözlem) basıyor, BLOCK/FIX değil.
- [x] ~~`ACI_YAYI` §4 "yarısını geçmez" ↔ betik `n≥12`~~ → **uyuşuyor.**
      Kılavuz "12-18 sahne, oran korunur", betik `azami = ceil(n/2) if n>=12`.
      Aynı kural, iki dille yazılmış.
- [x] ~~`03_PLAN_ONCESI` A4 beşinci soru~~ → **gerekmiyor.** ADAY-1 kapandı ve
      hipotez YANLIŞ çıktı (üç kanıt da ekrandaydı); A4 olduğu gibi doğru.

### Veri bekleyen biri

- [ ] ⏳ `02_RISK_KARTLARI` 5+ eşiği (9 soruyken ölçüldü, payda 13'e çıktı).
      Metin zaten kendi durumunu yazıyor: *"bant yeniden ölçülene kadar 5+
      KORUNUR (yanlış tarafa hata yapar: fazla uyarır)"*. Kalibrasyon **mod D
      koşuları olmadan yapılamaz** → Faz 1'e bağlı, elle düzeltilmez.

### Devir

- [x] `TODO_TEMA_VE_ACI_KAPILARI.md` E fazı **kapatıldı ve Faz 1'e devredildi**;
      4 açık kutu `[→]` oldu, dosya tarihsel kayda çevrildi. Devir sırasında
      bir bayatlık düzeltildi: E.1'in "hiç kullanılmamış tema" listesi beş tema
      sayıyordu, ikisi artık kullanılıyor (`sayac.sh`: YALNIZLIK **3** ·
      İNSAN-MAKİNE **1**). Gerçekten boş olanlar: **ZAMAN · KİMLİK · İLK TEMAS**.

### 🔎 Doğrulama

```bash
# şablonun örneğinde özel ad kalmadı (❌ örnekleri hariç → 3 satır: D45 vakası)
grep -n "Ada\|Yıldırım" kilavuzlar_ve_sistem_dosyalari/IMAGE_VIDEO_PROMPT_TEMPLATES.md
grep -c "THE_WAKING_GROUND" kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md   # 1 (=depoda YOK kaydı)
grep -c "hep yalnız" kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md          # 0
grep -c "^- \[ \]" TODO_TEMA_VE_ACI_KAPILARI.md                                 # 0
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
        yatay_2_4_dk_filmler_uzay/THE_COLD_WELD/     # kılavuz düzeltmeleri kararı bozmadı mı
```

### 📐 Şablon hatasının yarıçapı — ÖLÇÜLDÜ (düzeltilmedi, film dosyaları bu fazda değişmez)

Şablon yanlış öğretiyorduysa kaç film onu kopyaladı? Ölçüm: unvanlı özel ad
(`Dr.`/`Cdr.`/`Capt.`…) **prompt gövdesinde** mi, yoksa yalnız plan düzyazısında
mı geçiyor — plan karakteri adıyla anabilir, D45 **gövdeyi** yasaklar.

```
⛔ prompt GÖVDESİNDE unvanlı ad (D45 ihlali) : 13 film
      26× THE_ETERNAL_DUSK      ← sistematik, tek film 26 geçiş
       5× THE_DEAD_APPROACH
       1× GLASS_ABYSS · ABANDONED_ARMADA · TIDAL_HUNT · RESONANCE_FIELD ·
          LAST_ARCHIVE · SLOW_TIDE · CANOPY_WORLD · … ve **THE_INVERSION**
✅ yalnız PLAN düzyazısında (meşru)          : 21 film
```

🚩 **THE_INVERSION listede.** D45'i DOĞURAN film (2:12'de ad ekrana etiket olarak
düştü) hâlâ örüntüyü taşıyor. Ders yazıldı, kapı kurulmadı, örüntü kaldı.

**Kontrata göre bunun kaderi belli:** D45 ≥3 kez tekrarladı → `00_DERS_YAZIM_KONTRATI`
"⛔ ÇALIŞMIYOR + dönüşüm borcu". Doğru çare **⑯ ÖZEL AD denetimi** olarak
`prompt_kontrol.py`'ye eklemektir — 13 dosyayı elle temizlemek değil; elle
temizlik 14.'yü engellemez. ⏳ Faz 2'nin kapı işine bağlandı.

> 📌 **Kenar bulgu (Faz 7 dışı, düzeltilmedi):** `yatay_2_4_dk_filmler_uzay/`
> kökünde `THE_ROSE_COAT_DUST_PLAIN_FILM.md` duruyor ve aynı dosya
> `THE_ROSE_COAT/` klasörünün içinde de var. `yeni-film` skill'i
> *"format klasörünün köküne .md bırakma — sayaç kökteki her girdiyi BİR FİLM
> sayar"* diyor → ROSE COAT muhtemelen **çift sayılıyor**. Silme işi sahibinin.

---

## ⛔ FAZ 8 — TEK YAYIN, TEK EĞRİ  (proje sahibinin kararı · aleti kalibre eden tek şey)

- [ ] Üretilmiş ve kurgu kapısını geçen bir film seç (aday: Cold Weld, Faz 1 sonrası)
- [ ] Kart Y akışı: yayınla → 24/72 saat/7 gün tutundurma eğrisi + paylaşım → `08_YAYIN_PERFORMANS_TABLOSU` ilk satır
- [ ] Eğriyi filmin rubrik skorlarının YANINA koy (film kaydına "vekil ↔ gerçek" tablosu):
      düşüş noktaları ④'ün RETENTION DROP-OFF tahminiyle örtüşüyor mu — **ilk kalibrasyon**
- [ ] Doğrulama: yayın tablosu ≥ 1 satır · TEMA §3b aday etiketler için kart Y yolu açılmış olur

---

## 🆕 06.09.2026 — PLAN SADAKATİ MERCEKLERİ ⑨-⑫ AÇILDI (D184) · İLK KOŞU BEKLİYOR

```
Sahibin sorusu "QA promptları yeni filmdeki hatayı azaltmaya yeter mi?" —
ölçülen cevap HAYIR: Kept Light'ta 8 gerçek kusurun 2'si raporda; kaçan üç
üretim hatası "plan X dedi, ekran Y gösterdi" ve planı ekrana karşı okuyan
mercek yoktu. Sahip dört eksen seçti; dördü açıldı (00_README 🎯 bölümü).
```

- [x] ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK kaynak rubrikleri (~350 satır)
- [x] rubrik_paketle.sh PAKET_9..12 · rapor_kontrol.py imza + dizi/tahmin kapıları
- [x] T9-T12 · AGENTS F5-F8 · kart B/Y · 00_README · skill'ler · sayac
- [ ] ⏳ **İLK KOŞU:** Kept Light kurgulanmış master (filigransız · kartsız ·
      hook kırpılmış · 209-219 hard mute · −14 LUFS) → ⑪ ölçüm → 12 mercek MOD D.
      ⑨'un S24 kafiyesini, ⑩'un S19/S21'i, ⑪'in S4'ü, ⑫'nin hook'u EKRANDAN
      yazıp yazmadığı ilk kez orada ölçülür. Rubriğin kendi hatası (sayım ·
      tally · mod) ancak o koşuda görünür.
- [ ] ⏳ ⑫ tahmini 08_YAYIN_PERFORMANS_TABLOSU'na → yayın → gerçek eğri →
      |Δ| ≤ 10 s. Aleti izleyiciye karşı kalibre eden ilk satır (Faz 8'in
      öncülü).
- [ ] ⬜ Faz 5 RUBRİK DİYETİ ile birleşir: ①②⑦⑧'in yakaladığı her şey ya
      ffmpeg'de ya ⑤⑥⑨⑪'de — ilk MOD D koşusundan sonra hangi eski merceğin
      düşeceği verilerle kararlaştırılır, önce değil.

## 🚫 YAPILMAYACAKLAR (bu listenin sınırı)

```
· Yedinci VİDEO merceği yazılmaz. Altı rubriğe paragraf eklenmez (Faz 5 çıkarır).
· 162 ders tek seferde tasnif edilmez; ders TEKRARLADIĞINDA ya da film DOKUNDUĞUNDA kart alır.
· Kılavuz GÖVDELERİ silinmez/kısaltılmaz — kart üste gelir, gövde ek olur (Faz 2).
· Ders numaraları değişmez. Eski ham raporlar, T tabloları, film dosyaları değişmez.
· Mod V partiden film-dersi yazılmaz; aday GOZLEM_DEFTERI'ne düşer (kontrat §4).
· Sayı hiçbir belgeye elle yazılmaz — bu dosya dâhil (yukarıdakiler tarihli kesittir).
· Commit atılmaz; her faz "commit'e hazır" bırakılır.
```

## ✅ FAZ 0d — OPERATÖR YOLU VE ÇIKTI UCU (04.09.2026)

> Tetikleyici: 8 ⛔ ÇALIŞMIYOR dersin sekizi de AYNI eklemde kırılıyordu —
> araç var, kural üç ayrı yerde ⛔ ile yazılı, ama **kapının durduğu yol ile
> operatörün eliyle gittiği yol farklı.** D94(6) → D129(13): her tekrarda daha
> kalın bir ⛔ eklendi ve sayaç arttı. Kural yazma yolu tükendi; bu faz kural
> değil DÜZEN değiştirir.

### ① ÇIPLAK RUBRİK ULAŞILAMAZ YAPILDI  [D129 · D94]

- [x] `QA_PROMPTLARI/{1..8}_*_QA_CRITIQUE_PROMPT.md` → **`QA_PROMPTLARI/_KAYNAK/`**
      (`git mv`). Kökte artık yalnız `00_README.md · FILME_OZEL/ · _KAYNAK/ ·
      CALISTIRMA_KAYITLARI.md · ARSIV_6_MERCEK/` var → operatörün klasörü açtığında
      yapıştırılabilir görünen tek şey **filme özel paket**.
- [x] `rubrik_paketle.sh` → `SRC="$R/_KAYNAK"` (8 okuma taşındı) · `sayac.sh` rubrik
      hacmi globu `_KAYNAK/` altına alındı. **Makine referansı kırığı: 0** (doğrulandı).
- [x] ⭐ **ASIL MEKANİZMA BULUNDU — AGENTS.md kartlarının kendisi yanlış dosyayı
      gösteriyordu.** Sekiz QA kartının sekizi de `**Rubrik:** QA_PROMPTLARI/<n>_...`
      diyordu; `qa-isle` "paketi kullan" derken aynı skill "çelişkide AGENTS.md
      kazanır" diyor. Sekizi de `FILME_OZEL/<FILM>/PAKET_<n>_<MERCEK>.md`'yi
      gösterecek şekilde düzeltildi + ⛔ ÇIPLAK RUBRİK YAPIŞTIRILMAZ satırı eklendi.
- [x] `QA_PROMPTLARI/00_README.md` ÇALIŞTIRMA TARİFİ yeniden yazıldı: adım 1 artık
      "tablodan rubrik seç" değil **"filmin paketini aç"**; SPEC'i elle kesip
      yapıştırma adımı KALKTI (paket onu zaten gömüyor). Üç tablonun ilk sütunu
      paket adına çevrildi.
- [x] `YAPI_GRAFI` depo haritası · `T1-T8` kaynak rubrik satırları · `00_INDEX` ·
      4 kılavuz · 2 README = **19 canlı yol** güncellendi.
      ⛔ **Geçmiş kayıtlara DOKUNULMADI** (`02_HAM_RAPORLAR/` · `01_FILM_RAPORLARI/` ·
      film dosyaları · `CALISTIRMA_KAYITLARI`): onlar o gün ne yapıştırıldığının
      kaydıdır, talimat değil.

### ④ "ÖLÇÜLDÜ" İLE "TABLOYA GİRDİ" AYRILAMAZ YAPILDI

- [x] **`RAPOR_KONTROL/t_tablo.py`** (yeni) + `rapor_kontrol.py --t-tablo`.
      Betik "▶ TABLOYA GİRECEK SAYI"yı zaten HESAPLIYOR ve elle kopyalanmasını
      bekliyordu; artık T satırını **kendisi yazar** (aynı film varsa yerine yazar).
      8 merceğin 8'i için İngilizce kategori → Türkçe sütun eşlemesi kuruldu.
- [x] ⛔ **Kapı reddediyor:** GEÇERSİZ/TEKRAR kararlı rapor satır YAZMAZ.
      mod V satırı Ⓥ, SPEC varken mod V koşulduysa ⛔ damgası alır.
- [x] ⛔ **Film adı YALNIZ klasörden gelir.** İlk koşu rapordaki `FILM` alanını
      kullandı ve bozdu: THE_PAYLOAD raporu "The Last Custodian.mp4",
      THE_LAST_SPAN raporu "The Last Stand" diyordu; adı okunamayan 6 rapor tek bir
      `**?**` satırında birbirinin üstüne yazıldı. Tablolar `git checkout` ile geri
      alındı, ad türetmesi klasöre bağlandı, koşu tekrarlandı. Kimliksiz satır artık
      hiç yazılmaz.

### 📊 GERİYE DÖNÜK KOŞUNUN ÖLÇÜMÜ — beklenen ile çıkan farklı

```
ölçülen                  önce      sonra
canlı sistemde film      2 / 83  → 7 / 83
tabloya işlenmemiş      16 film  → 11 film
yazılan satır                    → 14 (6 filmde, T2 · T3 · T5)
```

⛔ **ÖNEMLİ:** "16 filmlik birikmiş emek kırtasiye kaybıdır" TAHMİNİ YANLIŞ ÇIKTI.
81 ham rapor tarandı; **49'u kapıdan geçemedi** — 38'i **TEKRAR** (SPEC dosyası
filmin klasöründe dururken mod V koşulmuş = D129'un tam kendisi), 11'i ⑤ çapraz
kapısında parti GEÇERSİZ. Yani bekleyen 16 filmin çoğu *işlenmemiş* değil,
**işlenemez**: kayıp kırtasiye değil, D129 hasarı. Kırtasiye kaybı yalnız 5 filmdi.

**Açık borç (bu fazdan çıkan):**
- [ ] `THE_LAST_SPAN` — 7 ham raporu var, **depoda film klasörü YOK**. Kimliği
      doğrulanmadan satır yazılmadı (raporlar filmi "The Last Stand" diye anıyor).
- [ ] `THE_LEANING_ROOM` (8 mercek) · `THE_COLD_WELD` (6) · `THE_FROST_LINE` (13) ·
      `THE_BORROWED_WEIGHT` (4) — hepsi ⑤ çapraz kapısında parti GEÇERSİZ.
      Tabloya girmeleri için yeniden koşu gerekir, kırtasiye düzeltmesi yetmez.
- [ ] ⏳ **① hamlesinin ölçütü:** bir sonraki filmde **D129 sayacı 13'te kalmalı.**
      Kalmazsa kırık olan dosya düzeni değil, başka bir şeydir.
- [ ] ② `kosu.sh` (tek giriş, girdi eksikse `exit 1`) ve ③ `teslim.sh` (ihraç
      hattı kimlik kartı) YAZILMADI — karar verildi (sert DUR), sıradaki tur.

---

## ✅ FAZ 0e — KAPI ADRESİ ÇÖZÜLÜYOR (05.09.2026)

> Tetikleyici: kılavuz taramasının üç mercekli çürütmeden sağ çıkan iki
> konusundan biri — **"depo kapıyı SAYIYOR, ÇÖZMÜYOR."** Kontrat kapıyı
> zorunlu kılıyor, `sayac.sh` kapı satırını sayıyordu, ama kapının işaret
> ettiği betik jetonu / liste maddesi hiçbir yerde ARANMIYORDU.

### ÖLÇÜM ALETİ

- [x] **`kilavuzlar_ve_sistem_dosyalari/kapi_adres.py`** (yeni) — her `**KAPI:**`
      satırının adresini fiilen açar: BETİK jetonu hedef dosyada birebir aranır,
      LİSTE maddesi hedef listede aranır, KARAR/ARŞİV'de adres aranmaz.
      `sayac.sh` 🧭 bloğuna bağlandı; her görevin ilk 60 saniyesinde koşuyor.
- [x] ⛔ **İki kalibrasyon hatası ölçümle yakalandı ve düzeltildi:**
      ① İlk sürüm backtick içindeki her dizgeyi hedef dosya saydı — regex
      (`\bsuit\b`), bayrak (`--olcum-filigran`), çıktı dosyası (`son_kare.jpg`)
      ve jeton (`NOVUM`) dâhil; 14 hayaletin **9'unu UYDURDU.**
      ② Gevşetme sonrası `KAPISI` gibi jenerik kelimeler eşleşti ve
      **doğrulanmış iki hayaleti (D175 · D176) "çözüldü" gösterdi** — çözmediğini
      çözdü sanan bir çözücü, düzeltmeye çalıştığımız arızanın ta kendisi.
      Jenerik sözlük kapatıldı; daireli kapı numarası (⑭ · ⑳b) korundu.
- [x] ⛔ Çok satırlı KAPI okuması **denendi ve GERİ ALINDI**: gövde metni
      jetonlarla eşleşip beş hayaleti sakladı, ⬜ AÇIK 2'den 7'ye çıktı.
      Bilinen bedel dosyada yazılı (KAPI satırı saran ders HAYALET görünebilir).

### ALTI HAYALET KAPI İNŞA EDİLDİ

```
                                                   05.09 öncesi   sonra
adresi ÇÖZÜLEN kapı                                    —          28 / 35
⛔ HAYALET / ADRESSİZ                                   6            0
```

- [x] **⑳b DEĞİŞİM KAPISI** [D179] · `prompt_kontrol.py` — imaj promptu ile onu
      izleyen video promptu eşlenir; imaj değişimin SONRASINI yazıyorsa BLOCK.
      D179'un kaynak vakasını (THE HEALING GROUND · `vapour` tüyü) yakalıyor.
      Kalibrasyon: soyut ad listesi (fill · ground · surface …) 26 → 17 vaka.
- [x] **㉑ MÜHÜR KAPISI** [D175] · `prompt_kontrol.py` — üç alt denetim:
      saydamlık tuzağı (`through the glove`) · mühür sınırı uzvuna ANATOMİ
      ayrıntısı + ±12 kelimede örtü yok · çıplak-deri negatifi 3 bölgeden az.
      Kalibrasyon: `shoulder/arm/neck` çıkarıldı ve tetik uzvun ADI değil
      ANATOMİ AYRINTISI yapıldı → **720 → 40 vaka**.
- [x] **㉒ YÜZEY RENK KAPISI** [D176] · `prompt_kontrol.py` — IŞIK bloğu biyom
      düzlemine renk atıyorsa BLOCK. ⛔ Dersin yazdığı biçim ("aynı yüzey iki
      renk taşıyorsa") **D176'nın KENDİ VAKASINI kaçırıyordu** (orada renk
      cümlesi TEKTİ, sorun yazıldığı BLOKTU); asıl kural blok yetkisidir.
      İkinci alt denetim (iki HUE çatışması) kalibrasyonda ~180 kez ateşledi,
      çoğu meşru → **silindi, kapıya girmedi.**
- [x] **MERCEK YOKLAMASI** [D111] · `rapor_kontrol.py` — partide hangi zorunlu
      mercek HİÇ koşmadı (FİLM ①②③④ · FRAGMAN ①). D111'in 2. vakasını
      (YERÇEKİMİ FRAGMAN · eksik ① KARE) birebir yakalıyor.
- [x] **FİLİGRAN HAKEMLİĞİ** [D177] · `rapor_kontrol.py --olcum-filigran VAR|YOK`
      (+ `--olcum-lufs`) — verilmezse eksen "ÖLÇÜLMEDİ" ⚠️, `VAR` verilirse parti
      🔴 TESLİM KUSURU. ⑤ SUSKUNLUK kapısı mutabakatSIZLIĞI ölçüyordu; sekiz
      mercek birden susunca ateşlenemiyordu [D150 · 4 vaka].
- [x] **B5c ÜRETİM SIRASI** [D168] · `03_PLAN_ONCESI_KONTROL_LISTESI.md` —
      üretim sırası dramatik sıra olamaz; ilk üretilen sahne doruk ya da
      merkezî seçimdir. ⚠️ Madde PLANI bağlar, ÜRETİMİ bağlamaz (D168 2. vakası).

### KALİBRASYON KAYDI — kararı değişen dosya 6, altısı da GERÇEK BULGU

```
baseline (kapılar öncesi)   95 BLOCK · 21 FIX ·  9 GO
üç kapı eklendikten sonra   99 BLOCK · 19 FIX ·  7 GO
```

| dosya | ne ateşledi |
|---|---|
| THE_UPWARD_FALL BOLUM_1 · BOLUM_2 | ㉒ — **D175/D176'yı doğuran filmin ta kendisi** |
| THE_PRESSED_FIELD BOLUM_1 · BOLUM_2 | ㉑ `through the glove` ×2 — D175'in birebir mekanizması |
| LOW_POWER_FRAGMAN_DIKEY | ㉒ IŞIK bloğu `ground = brown/red` |
| THE_RISING_SNOW_PART_B | ㉒ IŞIK bloğu `walls = green` |

**Açık borç:**
- [ ] ⏳ **Ölçüt:** bir sonraki KAPI satırı yazıldığında `kapi_adres.py` onu
      ÇÖZÜLDÜ göstermeli. Hayalet sayısı 0'dan yükselirse kapı yazımı bozuktur.
- [ ] ⬜ AÇIK iki ders (kapı arayan) ve DOSYA düzeyi iki kapı (alt jeton iddia
      etmemiş) — kontrat §5 gereği geriye dönük tasnif YAPILMADI.
- [ ] ② `kosu.sh` (sert DUR) ve ③ `teslim.sh` — dünkü karar, hâlâ sırada.
- [ ] ⏸️ Kılavuz taramasının **hükümsüz** kümesi (MADDE VE TEMAS · güç 8) —
      üç merceği de harcama limitinde düştü; çürütülmedi, yargılanmadı.

---

## 🔎 BİTİŞ ÖLÇÜTÜ VE DOĞRULAMA

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh                       # 🧭: mod D ≥3 · rubrik 6/6 ≤25 KB · KAPI kartlı kılavuz 34/34
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py dikey_shorts_filmler yatay_2_4_dk_filmler_uzay yatay_3_5_dk_filmler yatay_10_20_dk_filmler | tail -3
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_COLD_WELD_*_HAM_D.md --film yatay_2_4_dk_filmler_uzay/THE_COLD_WELD
grep -L "🎫 KAPI KARTI" kilavuzlar_ve_sistem_dosyalari/*.md            # boş olmalı (Faz 2 bitince)
git status                                                          # commit sahibin
```

> **Bu dosya ne zaman silinir:** Faz 1-7 işaretli VE başlangıç tablosunun "hedef"
> sütunu `sayac.sh` ile doğrulanmış olduğunda. Faz 8 proje sahibinindir; onun
> satırı `08_YAYIN_PERFORMANS_TABLOSU`'na taşınır, burada beklemez.
