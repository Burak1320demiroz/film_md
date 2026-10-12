# GÖREV — QA bulgusu × prompt karşılaştırması (salt okuma)

Depo: /Users/dai/github/apex_md/film_md . Bu depoda HİÇBİR dosyayı değiştirme, oluşturma, silme.
Yalnız şu klasöre yazarsın: /private/tmp/claude-501/-Users-dai-github-apex-md-film-md/4420b9a5-2609-47a1-aab0-96521f803898/scratchpad/analiz/
Git komutu çalıştırma. `prompt_hata_analizi.py`'yi `--yaz` ile ÇALIŞTIRMA.

## Amaç
Sana verilen her film için ham QA raporlarındaki her 🔴/🟠 bulguyu, o sahnenin GÖRSEL (image) ve VİDEO
promptuyla karşılaştır: kusur promptta önlenebilir miydi, prompt kusuru davet mi etti, yoksa prompt doğru
yazılmışken model mi tutmadı, yoksa QA'nın kendisi mi yanıldı?

## Araçlar
```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/prompt_hata_analizi.py --film <FILM>        # bulgu → sahne listesi (stdout)
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/prompt_hata_analizi.py --sahne <FILM> <n>   # o sahnenin görsel+video promptu
```
Ham raporlar: `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/<FILM>/` — GEÇERSİZ / TEKRAR / mod V
sayılanlar DAHİL hepsini oku (sahip "geçersiz olanları da oku" dedi). `--film` listesi ⑨-⑫ mod V ve KESİK raporları
dışarıda bırakır: o raporlardaki 🔴/🟠 bulguları da elle ekle ve satırda `(listede yok)` diye işaretle.
Bulgunun bağlamı (tam cümle) için ham raporu aç; `--film` satırları kesik olabilir.
Filmin planı ve QA_SPEC'i film klasöründe (`<FILM>_PLAN.md`, `<FILM>_QA_SPEC.md`, hikâye onayı `00_ANALIZ/00_HIKAYE_ONAYI.md`):
bulgu bir tasarım kararını (novum, bilinçli sessizlik, opak vizör…) kusur sanıyorsa 🅒'dir.
Önceki analizlerin biçim örneği: `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/02_FILM_ANALIZLERI/THE_COLD_WELD.md`
Sınıf sözlüğü (🅑1-🅑15, 🅐1-🅐5, 🅒1-🅒3): `.../10_PROMPT_QA_ANALIZI/03_PROMPT_HATA_SINIFLARI.md` (19.09.2026, 34 film).
Senin filmlerin bu analizden SONRA yazıldı — yani 19.09 kurallarının işe yarayıp yaramadığını da ölçüyorsun.

## Hüküm
- 🅐 MODEL SAPMASI — prompt kusuru açıkça önlüyordu (alıntıla), model tutmadı
- 🅑 PROMPT BOŞLUĞU — gerekli cümle/sayı/kilit o sahnenin promptunda YOKTU (filmin başka sahnesinde olması yetmez)
- 🅑+ PROMPT DAVETİ — prompt kusuru bizzat çağırdı (ör. büyük harfli jeton yazıya basıldı, çelişen iki istek, vakumda ses tarif eden AUDIO, kadrajda okunacak ekran isteyip metni yasaklamak, yapılamaz hareket)
- 🅒 QA YANILDI — tasarım kararı / başlık kartı / SPEC'i bilmeyen mercek / kusursuz şeye kusur
- 🅓 EŞLENEMEDİ — sahne çapası belirsiz ya da rapor başka filmi anlatıyor

## Tür (tek seç)
el-nesne kaynaşması · istenmeyen yazı · ortama aykırı ses · parçacık/duman/toz · kask/giysi/ekipman kayması ·
kamera/kesme/kadraj · yerçekimi/süzülme · filigran · klon/fazla kişi · zemine geçme · yüz/kimlik · efor/beden ·
ışık · yön/180° · arka plan/dünya çapası · sayı/nesne sayısı · ses-görüntü uyumu · oyunculuk · hikâye/anlatım/kurgu · diğer

## Kapanma yeri (tek seç)
prompt · kadraj kararı · referans/panel · kurgu-ses · araç ayarı · hikâye/plan · QA

## Çıktı — her film için ayrı dosya: `analiz/<FILM>.md`
```
# <FILM>
KAYNAK: ham rapor n (geçerli k · mod V/GEÇERSİZ m · KESİK j) · bulgu n (🔴 a · 🟠 b)

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |

## ÖZET
hüküm sayıları · tür sayıları (en sık 5) · kapanma yeri sayıları

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız, en az 3 sahne oku)
Somut alıntıyla: kendi içinde çelişki · meta etiket (Scene n of N, S07, PHASE) · büyük harfli jeton ·
görsel ile video arasında çelişki · motorun gösteremeyeceği soyut/zihinsel ifade · her sahneye kopyalanmış
şişkin NEGATIVE bloğu (uzunluk karakter olarak) · ortama aykırı istek. Her madde: sahne + alıntı + neden kusur.

## 19.09 KURALLARI BU FİLMDE
🅑1 ses yasası · 🅑2/2a temas (nesne-nesne dahil) · 🅑3 giysi birebir · 🅑4 ortam sayısı+adı · 🅑5 efor oranı ·
🅑6 büyük harfli jeton yok · 🅑7 ekran/metin çelişkisi yok · 🅑8 dünya çapası · 🅑13 ışık saat yönü —
her biri: yazılı mı (kaç sahnede) · yine de bulgu çıktı mı (sayı).
```
Bitince mesaj olarak yalnız şunu dön: dosya yolları + film başına 5 satırlık özet (hüküm sayıları, en sık 3 tür,
en çarpıcı 2 prompt kusuru alıntısıyla). Tahmin etme: okumadığın bulguya hüküm yazma; sayıları kendin say.
