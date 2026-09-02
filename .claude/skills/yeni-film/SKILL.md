---
name: yeni-film
description: Yeni film yazma akışı (AGENTS.md Kart A). "Yeni film yazalım", "yeni bir shorts / uzay filmi", "film fikrim var" dendiğinde MUTLAKA kullan. Kılavuz okumadan film yazılmaz, risk kartları okunmadan plan yazılmaz. Girdi: format ve film adı (verilmediyse sor).
allowed-tools: Bash(bash:*), Bash(git status:*), Read, Grep, Glob, Write, Edit
---

# Kart A — Yeni film

Sıranın kaynağı AGENTS.md Kart A + `kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`.
Bu skill sırayı dayatır, içeriği kılavuzlardan okutur. Çelişkide AGENTS.md kazanır.

## 0. İlk 60 saniye
- `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → gerçek durum
- `git status --short` → temiz mi başlıyorsun

## 1. OKU — yazmadan önce, sırayla
0. `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → **🧭 bloğundaki son 5 FİLM dersini (01-07) AÇ.**
   Bir ders sabah yazılıp aynı gün yazılan filme ulaşmadı [D157 → THE COLD WELD, 01.09.2026];
   kapı görünürlüktür. Alet dersleri (08/09) bu listeye girmez.
1. `KILAVUZ_REHBERI.md` — dört soruyu sırayla cevapla, okuma listeni çıkar ve
   o listedeki kılavuzları GERÇEKTEN aç.
2. `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`
   — ⛔ PLAN YAZILMADAN ÖNCE. 5+ risk çıkıyorsa malzeme azalt.
3. KILAVUZ_REHBERI §8 matrisinden en yakın filmi şablon olarak aç
   (⚠️ matris bayat olabilir — AGENTS §6 kaydı).

## 2. KLASÖR — iskelet tek yerde tanımlı: `KILAVUZ_REHBERI.md` §2.0
```bash
cp -r kilavuzlar_ve_sistem_dosyalari/FILM_KLASOR_SABLONU <FORMAT_KLASORU>/<FILM_ADI>
cd <FORMAT_KLASORU>/<FILM_ADI> && rm 00_SABLON_README.md
for f in FILM_*.md; do mv "$f" "<FILM_ADI>${f#FILM}"; done
```
- Yedi dosya: `PLAN · BOLUM_1 · BOLUM_2 · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC`
  (+ `REFERANS_PAKETI` — iki insandan/araçtan fazlası varsa zorunlu).
- Bölüm sayısı formattan gelir: dikey/2-4/3-5 → 2 · 7-9 ve 10-20 → faz sayısı kadar.
- ⛔ Format klasörünün köküne .md bırakma — sayaç kökteki her girdiyi BİR FİLM sayar.
- ⛔ Eski filmler yeniden bölünmez/adlandırılmaz; iskelet YENİ filmler içindir.
- Adlandırma `<FILM>_<ROL>.md` · `BUYUK_HARF_ALT_CIZGI` · Türkçe karakter yok.
- Sahne başlıkları `## 🎬 SAHNE <n> — BAŞLIK` (kural ② — başlıksız dosya sayımdan düşer)
  ve YALNIZ bölüm dosyalarında; PLAN'da prompt bulunmaz.
- `<FILM>_YAYIN_PAKETI.md` **tamamen İngilizce** yazılır (kanal kararı §3.3);
  `⬜ AFTER THE CUT` alanları kurgudan önce doldurulmaz.

## 3. YAZ — PLAN → BIBLE → PROMPT sırasıyla
Sahne haritası yazılırken dağıtılır, üretimden SONRA eklenemez:
- İki bütçe: `KARAKTER_VE_DUYGU_KILAVUZU.md` §6 + `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §2
  (örüntü kırıcı: ardışık iki sahne aynı ölçek + palet + ses dokusunda olamaz).
- TEMA satırı + EN AZ 3 sahne indeksi (`TEMA_MUHENDISLIGI_KILAVUZU.md` §3 → §5 → §9);
  indekssiz tema dekoratiftir.
- ⭐ B5 DÖRTLÜSÜ — sahne haritasından ÖNCE yazılır [03_PLAN_ONCESI B5]:
  `İSTEK` (film başlamasa da var olan bir iş — "anlamak/görmek/fark etmek" DEĞİL) ·
  `ENGEL` (bunu ne engelliyor) · `BEDEL` (alırsa ne kaybediyor **+ SAHNE no**) ·
  `MUHATAP` (eylemin yankısı nerede görünüyor: ikinci insan / kendi geçmiş kararı /
  kendi bedeni / ortamın kalıcı değişen parçası).
  ⭐ ASIL KAPI BEDEL'dir; sahne numarası taşımayan bedel boştur.
  İki insan yazıyorsan `AYRILIK` (B5b) zorunlu: AYNI FİKİRDE OLMADIKLARI an.
  Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — istek yok · bedel yok ·
  muhatap yok [`URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` TUR 4].
  ⛔ "ORTAM hasım değildir" kuralı 02.09'da GERİ ÇEKİLDİ; ortam meşru karşı güçtür.
- ⭐ `⭐VİRAL` işaretli her sahne İKİ satır taşır [SENARYO_VE_VIRAL_KAMERA §2.4]:
  `YÜZ` (vizör ardında hangi ifade değişiyor) + `HAREKET` (kadrajda ne hızlanıyor).
  Ölçütsüz VİRAL etiketi düşer — koparılabilirliğin iki sürücüsü budur (hakemli).
- ⭐ Replik varsa `SES_VE_DIYALOG_URETIM_KILAVUZU.md` §1a ÖNCE okunur:
  kadraj dışı sesin üç gerekçesi + bedenleştirmenin (ağzı gösterme) doruğa
  saklanması. Ekranda konuşan ağız İKİ riski birden açar: lip-sync + AI damgası.
- Sahne-kurulum dizisi: `ACI_YAYI_VE_SEKANS_KILAVUZU.md` §3 güvenli bant
  (ardışık çift: ≥1 ölçek kademesi VE ≥45°) · §4 kurulum sayısı · açı TİPİ sayısı ≥3.
- Her prompt self-contained (kural ③) — "BIBLE'a bak" atfı yasak.

## 4. QA_SPEC — yazım paketinin son parçası
`<FILM>_QA_SPEC.md` film klasörüne yazılır (A/B/C blokları + TARGET ASL satırları).
⛔ Replik zamanları ve doruk saati HESAPLANMAZ, HESAPLATILIR [D122]:
`replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti`.
Yazılan her kayıt formülle doğrulanır; sapma varsa paket TAM DEĞİLDİR.
⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz.

⛔ **VE SPEC TEK BAŞINA YETMEZ — QA PAKETİ DE BURADA ÜRETİLİR [D165]:**
```bash
bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü>
  → kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..8
```
Paket klasörü yoksa operatörün eline ÇIPLAK RUBRİK kalır, çıplak rubrik
**mod V koşar**, ve mod V koşusu T tablolarına giremez [D129].
⛔ **İKİ VAKA:** THE STILL SWARM (01.09) ve THE SINKING STAKE (02.09) —
ikisinde de sekiz merceğin sekizi mod V koştu, ikisinde de sebep BU
adımın atlanmasıydı. İkincisinde ders zaten yazılıydı ama bu dosyada
değildi: ajan AGENTS.md'yi değil bu skill'i okur.
⛔ Klasör yoksa film "yazımı tamam" sayılmaz — SPEC ile aynı ağırlıkta.

⛔ **ÜRETİM SIRASI PLANA YAZILIR VE DRAMATİK SIRA DEĞİLDİR [D168]:**
```
ÜRETİM SIRASI: referans paketi → DORUK → merkezi seçim → kapanış imajı → S0 → kalanı
```
Üretim her an durabilir (red · kota · motor · gün). Baştan üretirsen elde
hep KURULUM kalır ve kurulum kendini savunamaz — sahip konsepti hiç ekrana
gelmemiş bir doruk yüzünden reddeder. THE SINKING STAKE tam böyle durdu:
25 sahnenin 14'ü üretildi, eksik 11'i ARDIŞIK ve filmin SONUYDU.

⭐ **SPEC yazılır yazılmaz QA PAKETİ üretilir — burada, QA anında değil [D165]:**
```bash
bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <FORMAT_KLASORU>/<FILM_ADI>
```
Çıktı `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..8`.
⛔ Bu klasör yoksa film "yazımı tamam" DEĞİLDİR. Sebep: paket yalnız `qa-isle`
§2b'de tarif edilmişti; operatör QA anında skill değil RUBRİK açıyor ve çıplak
rubrik yapıştırıyor → THE STILL SWARM'da sekiz merceğin sekizi mod V koştu ve
hiçbiri tabloya giremedi. Betik 1 saniye sürer. SPEC değişirse yeniden koş.

## 5. KONTROL → KAPI
- `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`
  maddelerini uygula (maliyeti sıfır).
- ⭐ Promptlar bitti, TEK KARE üretilmedi → **prompt-kontrol skill'i koşulur.**
  ⛔ Betiğe FİLM KLASÖRÜ verilir, tek bölüm dosyası değil: film bölündüğünden
  beri dizi kapıları dosya sınırında körleşiyor ve klasör modu (01.09.2026)
  bölümleri birleştirip kapıları film boyunca koşuyor. Çıktıda
  `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırı yoksa kapı koşmamıştır.
  Betik 01.09.2026'dan beri ⑭ NOVUM TAŞIYICI (taşıyıcı nesne TEK KARE satırında mı — D157)
  ve ⑮ SIRT POZİTİF (kamera arkada/OTS ise pozitif sırt cümlesi — D139) da denetler.
  ⭐ 02.09.2026'dan beri ⑰ B5 HİKÂYE OMURGASI: İSTEK · ENGEL · BEDEL · MUHATAP
  satırları + "anlamak/görmek/fark etmek istek değildir" + BEDEL'in SAHNE numarası
  + iki insanlı filmde AYRILIK sahnesi. Kaynak:
  `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` · kapı: `03_PLAN_ONCESI` B5.
  Bu skill'in bitişi o kapının başlangıcıdır; kapıyı atlayıp üretim önerme.

## 6. GÜNCELLE + BİTİŞ
- KILAVUZ_REHBERI §8 film matrisine satır ekle.
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/00_INDEX.md` tamlık matrisine "0/4" satırı.
- Klasörün README'si varsa film listesine ekle.
- `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → toplam film sayısı 1 arttı mı.
- Commit ATILMAZ (yalnız proje sahibi atar) — "commit'e hazır" diye raporla.

## Kaçınılacaklar
- Sorgu yorgunluğu üretme: dört soru + risk kartı yeter; kullanıcıyı açık uçlu
  mülakata çekme, varsayım gerekiyorsa en fazla birkaç net soru sor.
- Alt-ajan açma; bu akış tek bağlamda koşulur.
