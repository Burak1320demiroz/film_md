# 🧪 SMOKE TEST — ajanlı döngünün ilk canlı denemesi

> **16.10.2026 — rolü değişti (AGENTS §2 F3p):** P1-P19'un hiçbiri koşulmadı; her filmde aynı uzun listeyi koşmak tutmadı.
> Bu dosya artık **deney kataloğudur**: her filmin pilotu (F3p, 1-3 çekim) kendi riskine uyan maddeyi buradan alır
> (ör. P14 10 s yolu · P17 panel sayfası · P18 model sesi · P19 ortak görünüm). Sonuç yine bu dosyanın sonuna yazılır.
> **Zincir bölümü** zincir açılacak filmde ön koşul olarak kalır (F3b).

> **Neden ayrı dosya:** ajan tanımları (`.claude/agents/`) oturum açılırken yüklenir.
> 05.10.2026'da kurulumu yapan oturumda yeni ajanlar ilk denemede çağrılamadı ("Agent type
> 'izleyici' not found"); oturum sürerken sonradan yüklendiler. Tam test yine de **yeni bir
> oturumda** (ana model Fable) koşulur. Sonuçlar bu
> dosyanın sonuna yazılır.

## Zaten doğrulananlar (05.10.2026, kurulum oturumu)

> 07.10.2026'dan beri aşağıdaki araç testlerinin hepsi tek komutla yeniden koşulur:
> `python3 uretim_hatti/test/kos.py` (sayı betiğin son satırında; 08.10.2026: 25). Örnekler `uretim_hatti/test/ornekler/`, medya geçici üretilir.

- 18 ajanın frontmatter'ı: ad = dosya adı · model beklenenle aynı · `Agent` yasak ·
  eleştirmenlerde `Write` yok · `maxTurns` var.
- `kurgu.py`: kontrol / liste / `--zaman` / taslak.
  - Görsel parça (animatik) çalışıyor; model sesi atılıyor (replik dışı −91 dB).
  - Bozuk timeline'da çıkış 1; sessiz taslakta ses akışı yok.
- `kor_ab.py`: karıştır / aç; aynı hedefe ikinci karıştırma reddediliyor.
- `kareler.py`: çıkar (+ etiketli kontak sayfası) / küçült (160×90).
- `film_dogrula.py`:
  - şablonda 15 eksik buldu;
  - geçerli örnekte 0 hata;
  - bozuk örnekte 5/5 kasıtlı hatayı buldu (zihinsel fiil, 7 s replik, 4.698 karakter, `C03` meta etiket, iş emri eksik);
  - insan repliğinde rakam uyarısı çalışıyor.
- `izleyici_kanca.py`: izinli kare ✅, repo dosyası ⛔, `ham/` ⛔, `../` kaçışı ⛔ (kanca betiği tek başına).
- `film_dogrula.py` prompt metni kontrolleri (06.10.2026):
  - Kasıtlı bozuk örnekte 5/5 tür bulundu: sıra numarası, başka çekime atıf, film geneli ifade, konuşma tarifi, "insan yok" + kişi göndermesi.
  - 8 temiz cümlede yanlış alarm 0.
  - Eski hattın 2.913 promptunda bulunanlar: atıf 45 filmde, konuşma 18 filmde, film geneli 17 filmde, insansız çelişki 4 filmde. Okunan örneklerin hepsi gerçek kusur.

- 06.10.2026 · diyalog, ses ve yayın:
  - `kurgu.py`:
    - ses parçası kaynak aralığıyla kırpıldı (`giris`/`cikis`) ve yumuşatıldı (`solma`); klibin kendi sesinden 1,5 s'lik replik doğru saniyede çaldı;
    - geçersiz aralık reddedildi (çıkış 1);
    - `yukseklik`: −22,4 → −14,0 LUFS, tepe −4,9 dBTP, 48 kHz, video kopyalandı.
  - `film_dogrula.py` replik:
    - ağız kadrajdaki replik tırnakla birebir geçerse geçerli;
    - bozuk örnekte 4/4 hata yakalandı (ağızda 6 s, telsizde 9 s, eksik tırnak, başka klipte ses tarifi);
    - bant ve rakam uyarıları çalışıyor.
  - `film_dogrula.py --bolum yayin`:
    - doldurulmuş paket 0 hata;
    - bozuk pakette 6/6 hata (Türkçe karakter, yanlış karakter sayısı, 4 hashtag, yasaklı hashtag, eksik sabit blok satırı, etikette araç adı);
    - eksik QUIET seçeneği uyarı veriyor.

## Yeni oturumda koşulacaklar (~10-15 ajan çağrısı)

1. `/agents` listesinde 18 ajan görünüyor mu, modelleri doğru mu?
2. **İzleyici + kanca:**
   - Görev: `~/film_medya/SMOKE_TEST/izleyici/kare_test/` içindeki 4 kareyi oku ve ayrıca `AGENTS.md`'yi açmayı dene.
   - Beklenen: kareleri anlatır; `AGENTS.md` kanca tarafından engellenir.
   - İzin sorusu çıkmamalı (`additionalDirectories`).
3. **Eleştirmen yazamaz:** dramaturg'a "şu dosyaya yaz" de. Beklenen: Write aracı yok.
4. **Dramaturg kalibrasyonu:** kasıtlı bozuk bir hikâye ver: bakım işi dizisi, bitişi yok, amaç yok.
   Beklenen: H04, H02 ve H06 ÖLÜMCÜL.
5. **Oyuncak film** `/yeni-film` ile:
   - `yatay_2_dk_filmler/SMOKE_TEST`, hedef 0:30, 3 çekim (her çekim 10 s).
   - Tur tavanını bu test için 1'e indir (DURUM.md'ye not düş).
   - Yalnız faz 1-3.
   - Sahip vetosu sorusu gerçekten gelmeli.
6. **Gerçek model ve araç kontrolü:** ajan transkriptlerinde (`~/.claude/projects/…`, salt okuma)
   `model` alanı ve çağrılan araçlar. Ajanın kendi beyanına güvenme.
7. **Sürdürme:** faz 2'den sonra oturumu kapat; yeni oturumda "SMOKE_TEST devam" → faz 3'ten sürmeli.
8. Sonuçları aşağıya yaz. Sapma varsa ilgili ajan ya da skill düzeltilir.
   `SMOKE_TEST` klasörünün kalıp kalmayacağı sahibe sorulur.

## Zincir testi — Flow (sahibin işi, ≈12 üretim) · ⛔ zincirli ilk üretimden ÖNCE

Flow'un başlangıç + bitiş karesi davranışı bu depoda hiç denenmedi. Sahneleme odası zincir
planını yazabilir, ama bu test sonuç tablosuna yazılmadan zincirli halka üretilmez.

1. **Yetenek:**
   - Frames to Video bitiş karesini kabul ediyor mu, hangi modelde?
   - Klip süresi (→ `KLIP_SURESI`), fps, çözünürlük, ses, kredi:
     `ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of compact <klip>`.
2. **Dört başlangıç/bitiş çifti × 2 deneme:**
   - (a) küçük poz değişimi;
   - (b) özne ~1 m yer değiştiriyor, kamera sabit;
   - (c) %20 kamera itmesi;
   - (d) kadraja bir kişi giriyor. Bu delta bütçesi ihlalidir; morfu görmek için.
3. **Her klip için:**
   - ilk kare ↔ başlangıç ve son kare ↔ bitiş benzerliği: `kareler.py dikis <klip> <bitiş.png>`;
     başlangıç için `kareler.py kare <klip> --t 0` + `dikis`;
   - `kareler.py kuyruk <klip>` (donan kuyruk, gizli kesme);
   - sahibin işareti: **morf / kesme / tamam**.
4. **İki halkalı B zinciri** (a'dan):
   - sahip dikişi 1x hızda izler;
   - `kareler.py dikis halka1 halka2`'nin SSIM değeriyle karşılaştırılır;
   - bu, SSIM'in bu film tipinde hangi değerde "görünür sıçrama" dediğini kalibre eder.
5. **Üç halkalı A zinciri** (gerçek son kare): üçüncü halkada yüz ve giysi kayması var mı? B ile karşılaştır.
6. Sonuçlar aşağıdaki tabloya. Kayıtlı bir vaka olursa sahip onayıyla `BILINEN_TUZAKLAR.md`'ye.

## Araştırma denemeleri (PROB) — 07.10.2026, sahip onayı

> Kaynak: `ARASTIRMA/04_SUZME_20261007.md` §E. Ucuz tutulur: her deneme 2 üretim. P1-P8 (`02_SUZME_20261006.md` §E) hâlâ sahip onayı bekliyor.

| # | Soru | Deneme | Ölçüm |
|:--:|---|---|---|
| P9 | Ağız kadrajdaki konuşma tırnakla mı, iki noktayla mı yazılmalı? (Vertex ↔ Gemini API çelişkisi) | Aynı yakın plan, aynı replik: `says, "…"` ↔ `says: …` × 2 · ses AÇIK (dudak senkronu için) | Ekranda yazı çıkıyor mu · söylenen kelime doğru mu · dudak senkronu (sahip işareti) → kazanan biçim `goruntu-yonetmeni` + `film_dogrula`'ya |
| P10 | Flow Karakter özelliği kask ve giysi kimliğini malzemeden daha iyi tutuyor mu? | Aynı çekim: Karakter (1-2 görsel) ↔ malzeme × 2 · Lite ya da Fast | Kask/vizör tipi, omuz bandı rengi, eldiven; devamlılık işareti |
| P11 | Omni Flash 1.1 taslağı (360p → 720p 0 kredi) hareket ve kadraj denemesi için yeterli mi; 10 s seçeneği işe yarar mı? | Riskli bir çekim: Omni 360p taslak → beğenilirse aynı prompt Veo | Taslak ↔ final hareket benzerliği · kredi |
| P12 | Mondo Sónico ortam yatağı ve foley için kullanılabilir mi? | Bir sahnenin EFEKT LİSTESİ'nden iki satır | İzler ayrı mı · uzay kuralına uyuyor mu (vakumda ses yok) · ticari koşul |
| P13 | Veo'da olumsuz ifade ters etki yapıyor mu? | "no dust in the air" ↔ "the air is perfectly clear" × 2 | İstenmeyen öğe çıkıyor mu |
| P14 | **Her çekim 10 s** (sahip kararı 08.10.2026) Flow'dan nasıl alınır? Veo klibi en çok 8 s. | Aynı çekim: (a) Veo 8 s + Lite uzatma 2 s · (b) Omni Flash Ingredients 10 s · (c) Veo 8 s + başlangıç karesi aynı ikinci klip | Dosya süresi (`ffprobe`) · uzatma dikişinde sıçrama/donma (`kareler.py kuyruk`) · kredi · hangi yol `KLIP_SURESI` ≥ 10 veriyor → sonuç `goruntu-yonetmeni` iş emrine + `kurgucu`'ya; zincir ancak bundan sonra |
| P15 | **Referans anahtarı** (sahip kararı 10.10.2026): görsel promptun başındaki `Reference 1 (woman): take her face and suit from it.` cümlesi kimliği tutuyor mu, kadraja yazı basıyor mu (§C)? Flow'da malzeme `@` ile anılabiliyor mu? | Aynı kare, 2 referansla: anahtarlı ↔ anahtarsız × 2 · bir deneme de `@` anma varsa onunla | Yüz/giysi/mekân doğru referanstan mı geldi · ekranda "Reference" ya da rakam var mı · referans sırası değişince sonuç değişiyor mu → sonuç `goruntu-yonetmeni` anahtar cümlesine |
| P17 | **Tek referans sayfası** (sahip kararı 10.10.2026): çok panelli sayfa (önden · yandan · arkadan · yüz yakın · durum) kimliği tek görünüşlü referans kadar tutuyor mu; "using the back-view panel" denince doğru panel mi alınıyor; sayfaya yazı/ok basılıyor mu? | Aynı karakter: 5 panelli sayfa ↔ tek görünüşlü referans, aynı arkadan çekim × 2 | Kask/giysi/işaret kayması (devamlilik) · yanlış panel/poz · sayfada yazı → panel sayısı ve anahtar cümle `goruntu-yonetmeni`'ne |
| P16 | **10 s vuruş planı** (sahip kararı 10.10.2026): `0-3 s … 3-7 s … 7-10 s` yazılınca model aralıklara uyuyor mu, rakamlar kadraja basılıyor mu, tempo düzleşiyor mu? | Aynı çekim: planlı ↔ plansız × 2; bir deneme "From 0 to 3 s" sözlü biçimle | `kareler.py cikar --aralik 1` ile vuruş sınırlarında olay nerede · ekranda rakam · donan kuyruk (`kuyruk`) → vuruş biçimi ve sayısı `goruntu-yonetmeni` + `film_dogrula`'ya |
| P18 | **Model sesi replik** (sahip kararı 12.10.2026, THE_MAYDAY_SEA): Omni Flash 1.1 ses AÇIK iken video promptundaki `… says: <line>` repliği doğru kelimelerle, doğru sesle (erkek/kadın, telsiz) ve doğru anda söylüyor mu; alıcıdan gelen ses için kadrajdaki kişinin ağzı kapalı kalıyor mu; altyazı basıyor mu; iki klipte "aynı ses" ne kadar benziyor? | THE_MAYDAY_SEA C02 (iki replik, Mara ağız kadrajda) ve C12 (alıcıdan kadın ses, kimse yok) × 2; ses AÇIK (Return silent videos KAPALI); ek karşılaştırma (F5 teknik B6): C02 ↔ C13 Mara tonu · C03 ↔ C22 AI tonu | Kelime doğruluğu · ses cinsiyeti/filtresi · ağız hareketi (sahip işareti) · ekranda yazı · C02 ↔ C12 ↔ C13 ses benzerliği, C03 ↔ C22 AI benzerliği (sahibin kulağı; tutmazsa yedek kayıt o konuşanın BÜTÜN satırlarına genişler, replik tek kaynaktan) · klipten klibe oda tonu farkı → kazanan biçim ve "Omni ses taklidi yapamıyorsa kurgu kaydı" kararı `goruntu-yonetmeni` + `ses-tasarimcisi` + `FLOW_GERCEKLERI`'ne |
| P19 | **Kesme sürekliliği** (sahip, 12.10.2026: kesmeler keskin, arka ses kesmede komple değişiyor): aynı mekânın iki klibinde ortak görünüm cümlesi + mekân ışık cümlesi birebir yazılınca renk/doku sıçraması azalıyor mu; `karisim 0,5` kesmeyi yumuşatıyor mu; kesintisiz yatak kesmedeki ses atlamasını kapatıyor mu? | Aynı mekândan ardışık iki çekim: ortak cümle var ↔ yok × 2 · `kurgu.py taslak` kesme ↔ karisim 0,5 · yatak var ↔ yok | `kareler.py dikis` fark görüntüsü + SSIM · sahibin gözü (sıçrama var/yok) · sahibin kulağı (ses atlaması) → eşikler ve varsayılan geçiş türü `GECIS_VE_SES_SUREKLILIGI.md`'ye |

## Sonuçlar

| Tarih | Adım | Sonuç | Not |
|---|:--:|---|---|
| 05.10.2026 | 2 | ✅ | izleyici (canlı, sonnet): 4 kare izin sorusu çıkmadan okundu (`additionalDirectories` çalışıyor); `AGENTS.md` okuması kanca tarafından engellendi ("PreToolUse:Read hook error … izleyici yalnız ~/film_medya/<FILM>/izleyici*/ …"); anlamadığı yeri "anlamadım" dedi, tahmin etmedi |
| 05.10.2026 | — | ⬜ | sahneleyici · mekan-haritacisi · zincir-bekcisi bu oturumda yüklenmedi ("Agent type not found") — yeni oturumda denenecek |
