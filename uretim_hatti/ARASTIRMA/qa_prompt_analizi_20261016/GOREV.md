# GÖREV — yeni hat QA bulgusu × prompt karşılaştırması (salt okuma) · 16.10.2026

Depo: /Users/dai/github/apex_md/film_md . Depoda HİÇBİR dosyayı değiştirme, oluşturma, silme. Git yazma komutu yok.
Yalnız şu klasöre yazarsın: /private/tmp/claude-501/-Users-dai-github-apex-md-film-md/b06345a6-7f47-4316-aa8e-0c0ce79d5610/scratchpad/qa16/
Çıktı: o klasörde `<FILM>.md` (tek dosya).

## Amaç
Filmin ham QA raporundaki her kusur bulgusunu, o çekimin GÖRSEL (başlangıç karesi) ve VİDEO promptuyla birebir karşılaştır:
prompt kusuru önleyebilir miydi, prompt kusuru davet mi etti, prompt doğru yazılmışken model mi tutmadı, yoksa QA mı yanıldı?
Amaç prompt YAZIMI için ders çıkarmak; hikâye eleştirisi değil.

## Okunacaklar (film klasörü: <F>)
1. `<F>/ODA/HAM_QA_RAPORU.md` — TAMAMI. (Ham çıktı; Anlatım Testi · İzleme formu · Süreklilik · Tarama.)
2. `<F>/ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU.md` varsa — yalnız bağlam; onun "kök neden" cümleleri KANIT DEĞİL (promptlara bakılmadan yazıldı).
3. `<F>/NOTLAR.md` — TARAMA/SÜREKLİLİK/DENEMELER tabloları varsa (hangi deneme, hangi prompt sürümü, hangi ref yüklendi).
4. `<F>/FILM.md` — §3 ORTAK GÖRÜNÜM / kimlik cümleleri, §4 çekim listesi (Cxx → anlatılan bilgi, ekranda görünen). Tasarım kararlarını buradan öğren.
5. Promptlar: `<F>/PROMPTLAR/G0x.md` (`## Cxx` → `### Görsel` / `### Video`). AYRICA klasörde sahibin kendi paketi varsa
   (`THE_SKY_CATCH.md`, `THE_FURNACE_GATE_16MIN_96_CLIPS.md` gibi) onu da aç: üretimde HANGİSİNİN kullanıldığını
   kanıtla belirle (NOTLAR, rapordaki içerik hangi metne uyuyor, `ODA/SAHIP_PLANI.md`). Belirlenemiyorsa ikisini de alıntıla ve "sürüm: ?" yaz.
6. Sınıflama sözleşmesi: `uretim_hatti/QA_OKUMA_KILAVUZU.md` §1 (karar ağacı S1-S4, sınır vakaları). Ona uy.
7. Hat kuralları bağlamı (gerekince): `AGENTS.md` §2-§3, `uretim_hatti/BILINEN_TUZAKLAR.md`, `.claude/agents/goruntu-yonetmeni.md`.

## Zaman → çekim
Bu QA'lar sahibin hat dışı montajı üzerinde koşuldu; `timeline.json` montajla aynı olmayabilir. Çekim hep 10 s.
- Önce rapordaki çekim/kesme numarasına ve İÇERİĞE bak; içerik o çekimin promptuyla uyuşmuyorsa komşu çekimi dene
  ("çapa: içerik" notu). Hiçbirine uymuyorsa 🅓. Aralık verilmişse başlangıç alınır.
- Montaj kısaltılmışsa (ör. 4 dk film ~2:41) zaman aritmetiği yapma; içerikle eşle ve bunu yöntem notuna yaz.

## Sınıf (QA_OKUMA_KILAVUZU §1)
🅐 model sapması (prompt doğru hâli açıkça istedi/kusuru açıkça yasakladı — ALINTILA) · 🅑 prompt boşluğu (gereken nitelik o çekimin
promptunda YOK; başka çekimde yazılı olması yetmez) · 🅑+ prompt daveti (promptun kendi ifadesi kusuru çağırdı ya da Görsel↔Video↔kimlik
çelişti — ALINTILA) · 🅒 QA yanıldı (tasarım kararı, kusursuz şey) · 🅓 eşlenemedi.
⭐ Video promptu karede olanı yeniden tarif etmek zorunda değil; karede doğru olan nitelik "istenmiş" sayılır.
⭐ Videoyu göremiyorsun: S1 (kusur gerçekten var mı) için rapora güven, ama raporlar arası çelişki varsa yaz; "insan doğrulaması: ?" kalır.

## Doğduğu yer (tek seç)
kare (başlangıç karesi zaten yanlış olmalı: görsel promptu/ref) · hareket (video sırasında doğdu) · seçim · kurgu (sıra/tekrar/eksik/ses montajı) ·
anlatım · ses (klip sesi/replik) · araç (filigran vb.) · —

## Tür (tek seç)
yüz/kimlik · giysi/işaret/arma/bant · ekipman/nesne biçimi · el-nesne · yön/180°/koltuk · klon/fazla kişi · istenmeyen yazı/bayrak ·
parçacık/duman/alev/sıvı · ortama aykırı ses · replik tekrarı/ses · dünya/arka plan · ışık · yerçekimi/fizik · kamera/kadraj ·
durum sıfırlanması (kesmede) · hikâye/anlatım · diğer

## Çıktı biçimi — `<FILM>.md`
```
# <FILM>
KAYNAK: ham rapor bölümleri (hangileri var) · izlenen dosya/süre · bulgu satırı n / tekil n
PROMPT SÜRÜMÜ: hangi prompt dosyası üretimde kullanılmış, kanıtı (ya da "?")
Yöntem notları: eşleme sorunları, montajın plandan farkı (kısa).

## BULGULAR
| # | çekim | rapor (bölüm · zaman) | bulgu (≤15 kelime) | tür | sınıf | promptta ne yazıyor — Görsel / Video (≤25 kelime birebir alıntı ya da "YOK") | doğduğu yer | not (≤15 kelime) |

## ÖZET
sınıf sayıları (tekil) · 🅑 oranı = (🅑+🅑+)/(🅐+🅑+🅑+) payda ile · en sık 5 tür · doğduğu yer sayıları.

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız; en az 6 çekimi baştan sona oku)
Her madde: çekim(ler) + birebir alıntı + neden kusur. Bak: Görsel↔Video çelişkisi · kimlik/giysi cümlesinin çekimden çekime
kelime farkı (fark eden kelimeleri göster) · sayısız/belirsiz giysi tarifi ("stripes", "patch") · iki karakterde taraf/koltuk
tanımının olmaması ya da çelişmesi · mimari çapa yokluğu · ekran/yazı daveti · vakumda ses/alev/duman çağıran kelime ·
diyalog/replik tekrarı çağıran yapı (aynı cümle iki promptta / iki konuşana) · meta etiket (Cxx, Scene n) · çok uzun prompt (karakter say) ·
zihinsel ifade · görünmeyen şeye atıf · referans anahtarı ("Reference n") ile rolün tutarlılığı.

## HAT KURALLARI BU FİLMDE (her biri: kaç çekimde yazılı · yine de bulgu çıktı mı, kaç)
ORTAK GÖRÜNÜM cümlesi birebir · "Reference <No>" anahtarı · asimetrik işaret (hangi kol, kaç bant) · koltuk/taraf ·
10 s vuruş planı · model sesi/replik satırı · vakum ses/parçacık kuralı · yazı/bayrak olumlu kilidi ("the only marking").

## DERS ADAYLARI (en çok 8)
Her biri: "Prompt yazarken: …" tek cümle + dayandığı bulgu #'leri + bu filmde kaç bulguyu kapatırdı + zaten hat kuralı mı (hangi dosya) yoksa yeni mi.
Kural değil, aday: sahip karar verir. Model sapması (🅐) olan yerde "prompta ekle" deme; müdahale yerini yaz.
```

Kurallar: Tahmin etme; okumadığın bulguya hüküm yazma; sayıları kendin say; alıntı birebir (çeviri yok). Türkçe yaz, alıntılar İngilizce kalır.
Bitince mesaj olarak yalnız şunu dön: dosya yolu + 6 satırlık özet (prompt sürümü, sınıf sayıları, en sık 3 tür, en çarpıcı 2 prompt kusuru alıntısıyla, en güçlü 2 ders adayı).
