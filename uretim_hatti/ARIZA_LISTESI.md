# 📉 ARIZA LİSTESİ — ölçülmüş arıza sınıfları (eleştirmenlerin ortak sözlüğü)

> **Kaynak:** 05.10.2026 ham QA analizi. 78 film klasörü, 853 geçerli rapor, çekirdek dört
> merceği tam olan 49 film. Raporları bir yapay zekâ (Gemini) yazdı: sayılar "ne sık
> raporlandı"yı gösterir, kesin ölçüm değildir. Teknik sayımın yeniden koşulabilir hâli:
> `python3 uretim_hatti/araclar/ham_rapor_say.py`.
> **Kullanım:** eleştiri bulgusunun `ARIZA` satırı buradaki kodu yazar (H03, T01 …).
> Liste kural değildir; yeni madde yalnız sahibin kararıyla eklenir.

---

## H · HİKÂYE ARIZALARI

Kaynak: hikâye raporlarının "en çok zarar veren üç şey / izleyici nerede bırakır / bitiş"
bölümleri, 52 film. Alt sınır sayımıdır.

| Kod | Arıza | Film | Belirti | Panzehir |
|---|---|:--:|---|---|
| H01 | Tekrar eden / boş çekim | 28/52 | aynı eylem ikinci kez, aynı kadraj, yeni bilgi yok, uzun yürüyüş | her çekim TEK yeni bilgi taşır; bilgisi olmayan çekim çıkar |
| H02 | Film bitmiyor, duruyor | 27/52 | kesik final, eylem ortasında başlık kartı, sonuçsuz son kare | son sahne bir SONUÇ gösterir: istek alındı ya da bedel ödendi |
| H03 | Yürüme / sürükleme / tırmanma dolgusu | 24/52 | yolculuk, varışın önüne geçer | yolculuk tek çekimde, kesmeyle kısaltılır |
| H04 | Prosedür / bakım hikâyesi | 16/52 | kol çekme, düğme, cıvata, kayış — sonuçsuz iş dizisi | iş bir İSTEĞE hizmet eder ve sonucu görünür; iş hikâyenin kendisi değildir |
| H05 | Neden-sonuç kopuk | 13/52 | sebepsiz patlama, birden beliren üçüncü kişi, mekân sıçraması | her olayın görünür bir sebebi ve görünür bir sonucu var |
| H06 | Amaç / risk / bedel yok | 13/52 | "kimse bir şey istemiyor", başarısızlığın bedeli bilinmiyor | AMAÇ ekranda bir iş, BEDEL sahne numarasıyla |
| H07 | Doruk yok | 11/52 | "no peak located" | tek bir merkez seçim anı; öncesi ona hazırlar |
| H08 | Yavaş açılış | 10/52 | ilk 10-20 sn manzara, sorun yok | ilk karede bir sorun ya da beklenmedik hareket |
| H09 | Görüneni anlatan replik | 9/52 | "Visor breach" vizör kırıldıktan hemen sonra | replik yeni bilgi verir ya da silinir |
| H10 | Tekdüze ritim (her çekim 10 s) | 8/52 | "slide show", "assembly-line" | çekim süresi seçilen aralık kadardır (2-8 s) → 08.10.2026 sahip kararı: çekim 10 s sabit; ritim çekim içi hareket + kadraj/ölçek değişimiyle |
| H11 | Özgün bir şey yok | 6/52 | "could not find one" | tek kare testi: anomali tek karede gösterilebilmeli |
| H12 | Karakter boş | 5/52 | "camera-carrier", "unaffected robots" | karakter bir şey ister, bir şeyi kaybeder, bunu beden diliyle gösterir |

Hikâye kararları (49 tam film): **yapıyı yeniden kur 17** · **önermeyi baştan yaz 4** ·
kırparak çek 11 · olduğu gibi çek 4 · karar satırı yok 13.

---

## T · TEKNİK ARIZALAR (ekranda)

Kaynak: 49 tam filmin bütün mercekleri; tekil olay = aynı film, aynı tür, aynı 5 saniye.
"Film 🔴" = en az bir ölümcül bulgu taşıyan film sayısı.

| Kod | Arıza | Film 🔴 | Nerede kapanır |
|---|---|:--:|---|
| T01 | El/beden-nesne kaynaşması, içinden geçme | 21/49 | KADRAJ: temas anı gösterilmez, öncesi/sonrası kesmeyle |
| T02 | Efor okunmuyor (ağırlık, direnç, yorgunluk) | 24/49 | KADRAJ + HAREKET: büyük beden hareketi, kısa çekim |
| T03 | Duman / toz / buhar / sıvı ortama aykırı | 22/49 | TASARIM: vakumda toz çıkaran eylem taşıyıcı an değil |
| T04 | Arka plan değişiyor, doku yüzüyor | 18/49 | REFERANS + aynı arka plan cümlesi |
| T05 | Kask / vizör / kıyafet / ekipman kayması | 18/49 | REFERANS + BAŞLANGIÇ KARESİ |
| T06 | Modelin ürettiği yazı / harf / rakam | 17/49 | TASARIM (okunacak ekran yok) + prompt kelimesi |
| T07 | Kamera kayması / gizli kesme / bölünmüş ekran | 15/49 | tek çekim + seçim |
| T08 | Yerçekimi tutarsız / sebepsiz süzülme | 15/49 | TASARIM: aynı kadrajda tek rejim |
| T09 | Eşya / araç / hasar sürekliliği | 12/49 | REFERANS + durum tablosu |
| T10 | Hareket bozuk (kayan ayak, sebepsiz dönüş) | 12/49 | HAREKET sadeleşir, çekim bölünür |
| T11 | Yön / ekran yönü / coğrafya | 12/49 | çekim listesinde taraf ve yön sütunu |
| T12 | Oyunculuk donuk | 12/49 | yakın plan yalnız tepki anında |
| T13 | Vakumda ses | 12/49 | KURGU: model sesi atılır |
| T14 | Aksiyonun hedefi / izi yok | 11/49 | hedef ve sonuç aynı çekimde ya da ardışık |
| T15 | Klon / fazla kişi | 9/49 | kadrajda en az kişi |
| T16 | Yüz / kimlik değişimi | 8/49 | REFERANS |
| T17 | Filigran / köşe logosu | 8/49 | ARAÇ AYARI + yeniden dışa aktarma |
| T18 | Gök / gece-gündüz / renk sıcaklığı değişimi | 8/49 | aynı dünya cümlesi her dış çekimde |
| T19 | Kurgu: tekrar eden bölüm, eksik doruk | 3/49 | `kurgu.py liste` + final izleme |

Ölümcül olayların düzelme yerine göre dağılımı: **kadraj/hareket %45** · referans görsel
%17 · prompt metni %17 · kurgu/ses/araç %8 · hikâye/açılış %5 · QA önyargısı %3.

---

## Q · QA ÖLÇÜMÜNÜN KENDİ ARIZALARI

| Kod | Arıza | Kanıt |
|---|---|---|
| Q01 | Prompta uyum hiç ölçülmedi | uyum merceği 20/20 koşuda "INPUT MISSING" |
| Q02 | Plan verilmeden ölçüldü | 462 rapor plansız · 144 planlı |
| Q03 | Sahibin kararını hata saydı | başlık kartı 17 filmde 🔴; normal kesme "Hard cut 🔴" |
| Q04 | Mercekler birbiriyle çelişti | INWARD_FALL: kare "ikinci yarı kopya", hikâye "olduğu gibi çek" |
| Q05 | Türkçe çıktı yumuşak olabilir | Türkçe 3 hikâye raporunun 2'si "olduğu gibi çek" (İngilizce 60'ta 2) |
| Q06 | Prompt uzunluğu fayda vermedi | 47 film: Spearman +0,26 (uzun → biraz daha çok hata) |
