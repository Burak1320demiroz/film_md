# 🎬 <FILM_ADI> — <Türkçe alt başlık>

```
FILM           <FILM_ADI>
FORMAT         yatay 16:9
HEDEF_SURE     2:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/<FILM_ADI>/
URETIM         Google Flow (web) · QA Gemini uygulaması
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `REPLIK` ve `MUZIK` varsayılan **var**: filmlerde akıcı diyalog, ses ve efekt olur (sahip kararı, 06.10.2026).
> `yok` yalnız hikâye bunu istiyorsa, gerekçesi §5'in altına yazılarak.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.

---

## 1. HİKÂYE

```
LOGLINE   <tek cümle, ≤25 kelime>
AMAÇ      <karakterin EKRANDA yapmaya çalıştığı iş>
ENGEL     <ekranda görülen>
KARAR     <hangi sahnede, ne seçiyor>
SONUÇ     <nasıl bitiyor — ekranda görülen sonuç>
BEDEL     <neyi kaybediyor> · sahne <n>
TEK SORU  <"… olacak mı?">
SEÇİM     Fable: aday <A|B|C> · <tarih> · gerekçe: ODA/F1_secim.md
SAHİP     <ONAY | VETO → …> · <tarih>
```

## 2. TRETMAN

<!-- sahne başına bir satır; her satır öncekinden doğar (seçim ya da başarısız deneme) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | | |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Karakter — TEK SAYFA: önden tam boy · yandan · arkadan · yüz yakın ¾ · <durum: vizör açık> | `1.KARAKTER_v1.png` | v1 | | ⬜ | |
| 2 | Mekân — TEK SAYFA: <geniş · giriş · ayrıntı> · <ışık durumları> | `2.MEKAN_v1.png` | v1 | | ⬜ | |

```
SHA-256: shasum -a 256 ~/film_medya/<FILM_ADI>/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: bir karakterin açıları, yüz yakını ve durum değişimleri aynı görselde paneldir; "SELA_yuz",
"SELA_arka" gibi ikinci dosya açılmaz (film_dogrula hata). Yeni panel gerekirse sayfa yeniden üretilir, sürüm artar.
```

### KİMLİK CÜMLELERİ (16.10.2026 · F3p'de goruntu-yonetmeni yazar, pilot yoksa F5 G01 · Görsel promptta BİREBİR)

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | yüz | <a woman in her thirties with close-cropped black hair and a small scar under her left eye> |
| 1 | giysi + işaret | <a pearl-white pressure suit with one narrow teal band around each upper arm, the only marking on the suit> |
| 2 | nesne | <the core, a matte graphite box the size of a shoebox with one amber light on its top face> |

```
Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (5/5 filmde
kimlik kayması, ARASTIRMA/16 Y1-Y3). İşaret: sayı + taraf + konum + "the only marking". Nesne: biçim + ölçü + taraf.
film_dogrula DERS Y2: referansı eklenen çekimde hiçbir parçası birebir geçmeyen özneyi gösterir (uyarı).
ORTAK GÖRÜNÜM cümlesi (varsa) yalnız film boyu değişmeyeni taşır: kimlik + doku/stil. Işık, su, gezegen, ses mekân ya da çekim
cümlesine gider (DERS Y6).
```

## 4. ÇEKİM LİSTESİ

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | <izleyici ne öğreniyor> | <yalnız görülen: kim, ne yapıyor, ne değişiyor — "fark eder/anlar/karar verir" YOK> | <geniş dış plan, sabit> | <karakter soldan sağa> | 10 | Frames to Video | — | 1.KARAKTER · 2.MEKAN | G01 | ⬜ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE.
  Ritim süreyle değil çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
Flow modu: Frames to Video · Ingredients to Video · Text to Video (yalnız kimliksiz çekim).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir" (örn. T01 → temas kadraj dışı, sonrası C05).
Grup: PROMPTLAR/<Grup>.md (8-12 çekim). Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Zincir · Baş. karesi · Bitiş karesi: yönetmen "—" bırakır; sahneleme odası (§F3b) doldurur.
  Zincirli çekim: Zincir = Z1 · Baş. = Z1.0 · Bitiş = Z1.1 (B) — ya da Baş. = "son:C02" (A) / "t:C02@4.2" (A′).
  Zincirli çekim de 10 s'dir → zincir yalnız KLIP_SURESI ≥ 10 ölçülürse kurulur; zincir en çok 4 halka; her halka yeni bir bilgi taşır.
DELTA BÜTÇESİ (her halka, Zk.n → Zk.n+1): aynı objektif · ışık · set │ en çok bir basit kamera
  hareketi │ özne yalnız ulaşabileceği mesafede │ kadraja nesne/kişi girip çıkmaz │ el-nesne
  teması değişmez │ durum değişimi küçük ve tek. Aşılırsa model iki kareyi eritir (morf).
```

### AÇILIŞ — ilk 30 saniye (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2 · yonetmen F3'te doldurur)

| Saniye | Çekim | Sorun ya da beklenmedik hareket | İnsan (beden · el · yüz) | Replik · ekran yazısı | Kapak bağı | Sesi kapalı okunur mu |
|---|:--:|---|---|---|---|:--:|
| 0-10 | C01 | <ilk karede hareket hâlinde ne ters gidiyor> | <yok · beden · el · yüz> | <yok · tek kısa replik> | <vaadin dünyası: mekân · tehlike · ışık> | <evet/hayır> |
| 10-20 | C02 | <sorun nasıl büyüyor ya da karakter nasıl tepki veriyor> | <en geç burada> | <ilk replik> | — | <evet/hayır> |
| 20-30 | C03 | <cevapsız soru · bedel · sıkışma> | — | <başlık katmanı son 2-3 s'de mi> | <kapak anı ya da parçası burada mı; değilse gerekçe> | <evet/hayır> |

```
İlk 30 s'de yok: logo · "sunar" kartı · siyah ekran · karartmadan açılma · saf manzara · görüntüde yazı ·
  kalabalık · hızlı kamera · karmaşık el-nesne teması · kusurlu ama "gerekli" çekim.
Sapma serbest; gerekçesi bu tablonun altına tek satır yazılır.
```

## 5. REPLİKLER

<!-- REPLIK yok ise tablo boş kalır -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
        model sesi (telsiz | voice-over | ağız kadrajda) → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda
        üretir (sahip kararı 12.10.2026); ≤ 8 s (ağız kadrajda ≤ 5 s); klip sesi filme girer (timeline klip_sesi), kurgu kaydı yedek
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik
Konuşma ve ses profilleri: ODA/F2_diyalog-yazari_<n>.md
```

## 6. SES PLANI — model sesi kullanılmaz (istisna: §5 Kaynak = model sesi, yalnız replik)

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|

```
Ortam: <vakum dış: dış ses yok, yalnız gövdeden · iç hacim: hava taşır>
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_<n>.md (her çekim en az bir efekt satırı)
```

<!-- 12.10.2026 sahip kararı: klipler arası keskin kesme ve kesmede komple değişen arka ses → uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md.
     Yatak mekân başına TEK dosya, klip sınırlarını aşar (timeline.json yataklar). Geçiş kesme başına: kesme | karisim 0,3-0,8 s | karartma 0,5-1,5 s. -->
### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|

## 7. MÜZİK PLANI

<!-- MUZIK yok ise "yok — gerekçe" yazılır -->
```
OKUMA        İzleyici bu filmi ___ olarak okumalı.
MÜZİKSİZ     <hangi an(lar) ve neden>
VURUŞ/SUSMA  <saniyeler — faz 8'de gerçek kesme noktalarıyla kesinleşir>
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md
```

<!-- 12.10.2026 sahip kararı: her filmde müzik promptu burada durur. F4'te besteci taslağı, F8'de gerçek kesme noktalarıyla
     kesin sürüm (eski sürüm altına tarihle kalır, silinmez). İngilizce, tek parça, süre + açılış + yükseliş/susma + palet + [Instrumental] + YOK listesi.
     film_dogrula --bolum muzik: MUZIK var ise zorunlu (≥200 karakter, Türkçe karakter yok). -->
### MÜZİK PROMPTU — Flow Music'e yapıştırılır
```text
<İngilizce müzik promptu>
```
