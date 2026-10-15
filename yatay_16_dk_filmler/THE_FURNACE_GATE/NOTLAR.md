# 📒 THE_FURNACE_GATE — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|
| <GG.AA> | C01 | d1 | Frames to Video | p1 | ✅ kullanılabilir 01.2–04.6 | |
| <GG.AA> | C01 | d2 | Frames to Video | p1 | ❌ el tokaya eriyor 03.1 → hareket | |

```
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

## RED (üretim reddi)

| Tarih | Çekim | Mesajın BİREBİR metni | İlerleyip sonda mı düştü | Değişen şey | Sonuç |
|---|:--:|---|:--:|---|:--:|

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

| Tarih | Video / kare modu | Zaman | Çekim (`kurgu.py liste`) | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması |
|---|---|---|:--:|---|---|:--:|:--:|

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 13.10.2026 | Film sahibin hazır planından kurulur; plan `THE_FURNACE_GATE_16MIN_96_CLIPS.md` klasörde birebir (kökten taşındı, SHA-1 597df296…), FILM.md §1-§7 ve KAPAK_VE_YAYIN §1 oradan yerleşti; faz 1-4 ve 6 ajan turu açılmadı (DURUM AŞILAN KAPILAR). Fable'ın türettikleri: referans numaraları (1.LEON · 2.RHEA · 3.KESTREL · 4.KOKPIT · 5.FOUNDRY · 6.ARK · 7.KORIDOR · 8.KRIYO · 9.KOPRU · 10.CEKIRDEK · 11.DRONE · 12.KONTROL_ODASI · 13.KOMUTA · 14.ISKELE · 15.ARACLAR) ve panel adları, grup bölümü (G01-G08 = plan bölümleri, 12'şer çekim), replik saniye/süre tahmini (≈2,9 kelime/s), replik kaynağı (düz etiket → ağız kadrajda; comms/offscreen ve yüzü kadrajda olmayan 8 çekim C34 C49 C51 C56 C60 C65 C67 C71 → telsiz; VO → voice-over), §3 ORTAK GÖRÜNÜM / MEKÂN IŞIĞI / ORTAM SESİ / SES KİMLİĞİ / KİMLİK TABANI cümleleri, §6 yatak Y1-Y9 ve 95 kesmelik geçiş taslağı (karışım yalnız C95→C96), §4 AÇILIŞ tablosu. §4 "Ekranda görünen" planın İngilizce kompozisyon + hareket cümlesi birebir (çeviri kayması olmasın). | Sahip: "plana uyarak filmi yapalım" + "Plan farklarını düzelterek başla" + "sonrasında filmi yapmaya başla" (THE_PLANET_THIEF · THE_MAYDAY_SEA yolu). Sekiz grup paralel yazılacağı için panel adları ve sabit cümleler baştan Fable'da sabitlendi (MAYDAY F5 dersi: panel adları G01'e bağlıydı, CİDDİ bulgu). |
| 13.10.2026 | **Replik kaynağı model sesi (sahibin seçimi):** plan "Konuşmalar ve müzik kurguda ayrı eklenir … No spoken dialogue" der; vizörler şeffaf ve 95 repliğin çoğu kadrajdaki karakterin ağzından → bütün replikler §5 Kaynak = model sesi (…), video promptlarında birebir; Flow'da ses AÇIK; timeline'da replik taşıyan parçalar `klip_sesi: true`; kurgu kaydı yedek. Dış (vakum) kliplerde klip sesi yalnız replik penceresinde (MAYDAY T13 kararı). | Sahip (AskUserQuestion 13.10.2026): "Model sesi: video konuşsun". Kurguda eklenen ses kadrajdaki dudakları kıpırdatmaz. |
| 13.10.2026 | **Plandan sapmalar ("plan farklarını düzelterek başla"; olaylar korunur):** (1) plan R03 iki kişilik ana kare kaldırıldı → iki kişilik çekimler 1.LEON + 2.RHEA, "Leon solda, Rhea sağda" prompt cümlesinde (özne başına tek sayfa · T16) · (2) R01 hook VO 0 s → 2,0 s (ILK_30 "ilk 2 s insan sesi yok") · (3) plan prompt kalıpları F5'te kalkar: olumsuz kuyruk ("No readable text…", "No new people…", "No spoken dialogue…"), araç/oran etiketi ("horizontal 16:9", "10 seconds", "Animate the uploaded scene still as the first frame" — zincir dili), "Use the attached reference images only…" (yerine `Reference <No> (<rol>)` anahtarı), çekim atfı ("after K55", "after K65", "the same … as") · (4) video promptu tek "Main action" → 10 s 2-4 vuruş planı (ilk vuruş hareketli) + model sesi replikleri + ortam ses cümlesi · (5) plan §7 "kabul edilen son kare başlangıç olabilir" → zincir yok, her kare tek başına · (6) kapakta film adı yazısı (plan "THE FURNACE / GATE") → KAPAK_VE_BASLIK kuralı film adı yazmaz, F9'da sahip seçer · (7) C48'de taraflar ters (Leon sağda komuta kapısında) — plan kapı coğrafyası, sapma değil not. | Hat kuralları: film_dogrula M (meta · atıf · zincir dili · konuşma · 10 s planı · referans anahtarı) · PROMPT_HATA_ATLASI (olumsuz blok ters etki) · ILK_30_SANIYE_KILAVUZU · KAPAK_VE_BASLIK_KILAVUZU · AGENTS.md özne başına tek sayfa. Sahip "hayır" derse plan metnine dönülür. |
| 14.10.2026 | F5 birleştirme (§2c, tur açılmadı; 4 eleştiri ÖLÜMCÜL 0 · CİDDİ 33 · KÜÇÜK 39): Fable kararları K1-K19 + grup satırları → `ODA/F5_fable_birlestirme_1.md`. FILM §3 Fable güncelledi: `full-length` panel adları · DIŞ DÜNYA cümlesi · ROL SÖZLÜĞÜ · adsız VO · "EMP" yok (`grey disc panel`) · yeni paneller (Leon sağ profil · Rhea sol profil · kokpit önden · vault empty · vault door and crate · input cradle open · local-control pad) · KASA ALARM ışığı · kokpit yönü kuralı · üç bağlantı cihazı · tether sağ kalça · sayfa sırası 10/15 önce. FILM §5: R21 R38 R52 R65 metni (sahip), 22 replik saniyesi (K8). Çatışan öneriler: gök cümlesi D1-B2 birleşik biçim seçildi; kokpit önden panelinde pilot kare SAĞINDA (T1-B5 fiziği; D1-B1'in 'pilot solda' panel tarifi RED); tether SAĞ kalça (C42 mevcut düzeni; T1-B15 'sol' RED); temas: hareket kısa vuruşta kalır + YEDEK sonuç karesi (T2-B1 'hareketi ekrandan al' KISMEN — plan olayı korunur, C60 ilk deneme). | Ölçülmüş tuzaklar (BILINEN §A §C, T01 T06 T09 T11 T18) ve sekiz paralel grubun ortak sözleşmesi; sahip cevapları 14.10. |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 13.10.2026 | F5/1 | goruntu-yonetmeni (G01) | sonnet | FILM §3 §4 §5 + plan §10 K01-K12 + §8 R01-R16 (biçim çevirisi görevi) | PROMPTLAR/G01.md | ✅ 15 referans sayfası (FILM §3 panel adları; KAYNAK bağımlılığı 3→4 · 6→5 · 7→8 · 10→12 · 9→14) + 12 çekim + iş emri; replik biçimi iki nokta, vuruşun son cümlesi; ses/kimlik cümleleri §3 birebir; gök cümlesi `Everything hangs in deep black space with sparse stars.` (kendi önerisi) · kamera sözleşmesi: iki kişilik geniş arkadan, teklilerde Leon bakışı sağa, Rhea sola; bilek bağlantısı Rhea SAĞ, Leon SOL bilekte · `body` yazılmadı · son raporu oturum limitinde kesildi (dosya tam, mekanik ✅) |
| 13.10.2026 | F5/1 | goruntu-yonetmeni (G02) | sonnet | FILM §3 §4 §5 + plan §10 K13-K24 (biçim çevirisi görevi) | PROMPTLAR/G02.md | ✅ 12 çekim + iş emri; EKLE iki parçalı (KARE referansları · VİDEO yalnız kare); ad yerine the man/the woman; rozet tarafı ayrı cümle · gök cümlesi önerisi `Deep black space with sparse stars surrounds the foundry, and a huge curved blue gas giant fills the far background.` (Fable'a, hizalanmak üzere) · risk: C14 · C15 · C23 el-nesne teması önce; C17 profilde konuşma, C24 iki konuşanlı geniş plan dudak okunurluğu · son rapor limitte kesildi (dosya tam) |
| 13.10.2026 | F5/1 | goruntu-yonetmeni (G04) | sonnet | FILM §3 §4 §5 + plan §10 K37-K48 (biçim çevirisi görevi) | PROMPTLAR/G04.md | ✅ 12 çekim (hepsi replikli) + iş emri; kokpit kamerası koltuklara bakar, kanopi ve ark yalnız C41 · C46'da; 'Exactly N visible adults' → `the two of them are the only people in the cockpit` · risk: R38 metninde `dead` (red kelimesi, replik değişmez); C42 · C45 temas, C40 · C43 · C46 iki kişilik ağız senkronu; C46 5,0 s ve C48 geniş planda ağız sınır vaka · son rapor limitte kesildi (dosya tam) |
| 13.10.2026 | F5/1 | goruntu-yonetmeni (G06) | sonnet | FILM §3 §4 §5 + plan §10 K61-K72 (biçim çevirisi görevi) | PROMPTLAR/G06.md | ✅ 12 çekim + iş emri; vuruş iskeletleri çeşitli; kollar harf etiketiyle anılmaz ("clamp-A" · "release-B" kadraja basılabilir) → renk + konum; gök cümlesi `Deep black space with sparse stars surrounds the foundry.` · risk: C68 · C72 dev yapı ¾ kompozisyon, C70 eldiven son vuruşta kola oturur (temas); C65 · C67 · C71 kurulu temasla başlar, kaynaşırsa kesmeye bölünür · son rapor limitte kesildi (dosya tam) |
| 13.10.2026 | F5/1 | goruntu-yonetmeni (G07) | sonnet | FILM §3 §4 §5 + plan §10 K73-K84 + §13 (biçim çevirisi görevi) | PROMPTLAR/G07.md | ✅ 12 çekim + iş emri; temas gerektiren harekette kare temasla başlar (plan §7); "body stays anchored" → "boots stay planted"; §3'te ayrı gök cümlesi yok dedi (dış ışık cümlesi içinde) · sapma: §4 Referans'tan C78 → 10.CEKIRDEK, C79 → 5.FOUNDRY · 10.CEKIRDEK · 15.ARACLAR çıkarıldı (gerekçe Not'ta) · risk: C74 rijit köprü ve C84 ikinci yanaşma önce sınanır; C75 ark ucu pencereden, C79 profilde ağız, C77 geniş planda dudak · son rapor limitte kesildi (dosya tam) |
| 13-14.10.2026 | F5/1 | goruntu-yonetmeni (G03 · G05 · G08) — kesinti | sonnet | aynı görev | — | ⛔ oturum limiti (13.10 23:2x, 14.10 07:40), uyku kesintisi, takılma (600 s) → SendMessage devamıyla (çağrı sayılmaz) 14.10'da tamamlandı |
| 14.10.2026 | F5/1 | goruntu-yonetmeni (G03) | sonnet | FILM §3 §4 §5 + plan §10 K25-K36 (biçim çevirisi görevi) | PROMPTLAR/G03.md | ✅ 12 çekim, 11 replik + iş emri; `full-body` yerine `full-length panel` (red kelimesi) · KASA ışığının ikinci yarısı yalnız çekirdek kadrajdayken (C25-C27 · C31) → §3 varyantı önerisi · tug C35'te kadraj dışı (C12 · C44 aynı soru) · çıkarılan referanslar: C27 C28 → 15 · C33 C34 → 10 · C36 → 5 · 10 · risk: sandık (C29-C31) hiçbir referansta yok; C25 menteşe tarafı; C36 arkadan kamera, yaralar/dudak; boş kadrajda telsiz (C25 C28 C35); C30 · C32 önce sınanır |
| 14.10.2026 | F5/1 | goruntu-yonetmeni (G05) | sonnet | FILM §3 §4 §5 + plan §10 K49-K60 (biçim çevirisi görevi) | PROMPTLAR/G05.md | ✅ 12 çekim, 11 replik + iş emri; kollar renkle anılır; gök cümlesi G06 ile aynı · risk: R52 `dead` (birebir replik); `full-body panel` adı; C49 arkadan eldiven teması; C58 tek kulp iki eldiven; C52 vakumda kıvılcım; C53 geniş planda ağız · Fable'a: C58/C60 replik saniyesi ≈5,0/≈3,5; Rhea bilek bağlantısı SOL ön kolda (G01 SAĞ ile çelişir); C54 sabit korkuluk 13.KOMUTA'da yok; çıkarılan referanslar C50 C55 → 15 · C53 C55 C56 → 10 |
| 14.10.2026 | F5/1 | goruntu-yonetmeni (G08) | sonnet | FILM §3 §4 §5 + plan §10 K85-K96 (biçim çevirisi görevi) | PROMPTLAR/G08.md | ✅ 12 çekim, 13 replik + iş emri; `full-length` tarifi · kokpit iki kurulum (C86 C88 C95 önden · C90 C93 arka-yan) · çıkarılan referanslar C86 → 5 · 6 · 10 · 15, C93 → 5, C95 → 10 · 15 · risk: C85 tug yakası yalnız metinle; C89 panel seçimi; gök cümlesi §3'te yok; C95→C96 karışım ↔ replik çakışması; C94 VO cümlesinde "Leon" adı (§3 SES KİMLİĞİ'nden, Fable hatası); C85 · C91 önce sınanır |
| 14.10.2026 | F5/1 | teknik-danisman (C01-C48) | sonnet | G01-G04 + FILM §3 §4 §5 | ODA/F5_teknik-danisman_1_G01-G04.md | ÖLÜMCÜL 0 · CİDDİ 7 (B1 "EMP" kısaltması sayfa 2 · 15 · C31 · B2 C03 açılış: şeffaf vizör + 5 s dudak + kayan yansıma · B3 temas değişimi kare içinde, C04 C26 C31 C33 C34'te yedek yok · B4 boş kasa kareleri çekirdekli panele bağlı → `vault empty panel` · B5 kokpit yönü: önden kamerada pilot solda + kanopi arkada çelişkisi · B6 C12'de tug yok · B7 38 replik ağız kadrajda, ses kimliği tutmazsa yedek senkron bozar) · KÜÇÜK 12 (B8 arkadan/geniş planda dudak · B9 vizörde kayan yansıma · B10 `body` · B11 C01 VO'da ad · B12 payoff son saniyede · B13 ilk replik 1,0 s · B14 kriyo penceresi üç yerde · B15 tether tarafı · B16 "crouching person" · B17 "rises" · B18 R38 `dead`, R21 `dies` · B19 gök cümlesi) · KORU yedek notları, fırın ışığı, ortam cümleleri · TUR KAPANABİLİR · 15 tur sınırı → SendMessage devamıyla yazdı (sayılmaz) |
| 14.10.2026 | F5/1 | devamlilik (C49-C96) | sonnet | G05-G08 + G01 REFERANS + FILM §3 §4 §5 | ODA/F5_devamlilik_1_G05-G08.md | ÖLÜMCÜL 0 · CİDDİ 8 (B1 C56 bilek sol ↔ sayfa sağ · B2 C64 baş sola ↔ sağ çene yarası · B3 C68/C72 yakın-uzak kelepçe çelişkisi · B4 gök cümlesi üç biçim, 10 dış karede yok · B5 tamamlanma repliği eylemden önce C65 C72 C85 · B6 vuruş iskeleti tekrarı, 4 vuruş yok · B7 Leon sağ profil, Rhea sol yüz paneli yok · B8 `body` 9 promptta) · KÜÇÜK 9 (B9 rol etiketleri · B10 adlar C64 C70 · B11 sayfada olmayan nesneler · B12 komuta bilek yuvası C55 boş ↔ C78 dolu · B13 C84/C85 kelepçe hangi yakada · B14 C91 panel · B15 "EMP" · B16 EKLE biçimi · B17 §4/§3 referans uyuşmazlığı 9 çekim) · KORU ortak görünüm 24/24, ortam sesi 48/48, ışık · TUR KAPANABİLİR · 20 tur sınırı → SendMessage devamıyla yazdı (sayılmaz) |
| 14.10.2026 | F5/1 | devamlilik (C01-C48) | sonnet | G01-G04 + FILM §3 §4 §5 | ODA/F5_devamlilik_1_G01-G04.md | ÖLÜMCÜL 0 · CİDDİ 10 (B1 kokpit kamera yönü aynalı, `seats from the front panel` yok, C41/C46 kanopi arkada · B2 gök cümlesi · B3 C12 tug yok · B4 kriyo penceresi üç yerde + junction kapısı açık hâli panelsiz · B5 çekirdek/araçlar/bilek iki sayfada ayrı tasarlanıyor → sayfa sırası 10 · 15 önce + KAYNAK · B6 kasa kapısı, sandık, kırmızı lamba, kontrol pedi sayfada yok · B7 "EMP" · B8 VO adı ve farklı tarif · B9 `says:` sonrası betimleme C27 C36 · B10 vuruş iskeleti tekrarı) · KÜÇÜK 7 (rol sözlüğü · §3/§4 referans uyuşmazlığı · tether tarafı · KASA ışık varyantı + alarm lambası · küçük çelişkiler C17 C20 C29 C41 C02 · C28→C29 ve C16→C17 aynı eksen · temas yedekleri) · KORU ortak görünüm, kimlik tabanı, ortam sesi, replikler birebir · TUR KAPANABİLİR · limit sonrası SendMessage devamı (sayılmaz) |
| 14.10.2026 | F5/1 | teknik-danisman (C49-C96) | sonnet | G05-G08 + G01 REFERANS + FILM §3 §4 §5 | ODA/F5_teknik-danisman_1_G05-G08.md | ÖLÜMCÜL 0 · CİDDİ 8 (B1 sürekli temas + hareket 13 çekim → kare sonucu gösterir, video kamera + ışık · B2 C52 vakumda kıvılcım taşıyıcı an; C89 motor parlaklığı · B3 C86 C88 C95 iki ağız kadrajda → önce C86, karışırsa GOSTERIM Örnek C (sahip kararı) · B4 panel durumu ↔ istenen durum C59 C64 C91 (C72) · B5 bilek sol/sağ · B6 gök cümlesi · B7 §5 saniye R59 R61 R62 R82 R94 · B8 "EMP") · KÜÇÜK 11 (`body`/`dead`/`dies` + replik önerisi "still locked" · "fails" · vizörde ışık · rijit yapıda kamera · tether yerçekimi · C55 rota şekli · C90 arkadan yüz · görünmeyen yara · C91→C92 aynı ölçek · C58 efor · 10 s ölçülmedi + G07 EKLE biçimi · §3 kullanan çekimler) · KORU telsizde yüz yok, ortam sesi, kilitli kamera · TUR KAPANABİLİR · limit sonrası SendMessage devamı (sayılmaz) |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G08 (yeni ajan) | sonnet | ODA/F5_goruntu-yonetmeni_2_G08.md §K + K-GENEL + FILM §3 §5 | PROMPTLAR/G08.md (tam yeniden) · §K'ya "Uygulama 15.10" | §K uygulandı, uygulanamayan yok · C86/C88/C95 YEDEK notu · C90 R89 telsiz · Fable'a: §5 R84 R85 R87 R88 R92 R93 saniye, R89 Kaynak telsiz, §3/§4 referans EKLE'den |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G01 (yeni ajan) | sonnet | K-GENEL + G01-1 + D1/T1 + tur-1 yedeği ↔ güncel G01 | ODA/F5_goruntu-yonetmeni_2_G01.md | K1-K19 ve G01-1/2/3 dosyada uygulanmış · tek açık: 2.RHEA Reference 15 panel listesi (ajanın verdiği eski→yeni metin Fable'ca birebir yerleştirildi: prompt + iş emri sıra 4) · G01-2 C08 KISMEN · Fable'a: R12 1,5→2,0 · R02 Kaynak telsiz · §4 Referans farkları C01 C02 C03 C04 C07 C12 |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G04 (yeni ajan) | sonnet | ODA/F5_goruntu-yonetmeni_2_G04.md §K + K-GENEL + FILM §3 §5 | PROMPTLAR/G04.md (tam yeniden) · §K'ya "Uygulama 15.10" | §K uygulandı, uygulanamayan yok · R38 yeni metin `says:` · K19 kokpit yönü · K10 YEDEK C42 C45 · risk C46 R49 vuruş sınırı, C46/C48 ağız okunurluğu (okunmazsa telsiz) · çapraz: C36 arka → C37 ön kokpit ekran düzeni ters (§6 açı farkı) · film_dogrula cekim+prompt ✅ 0 hata |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G02 (yeni ajan) | sonnet | K-GENEL + G02-1/2 + D1/T1 + tur-1 yedeği ↔ güncel G02 | ODA/F5_goruntu-yonetmeni_2_G02.md | çoğu karar dosyada uygulanmış · BEKLİYOR: C13 C17 C19 C24 ağız kapalı + sağ bilek, C13 sağ kol, C17 eşit adım + DIŞ DÜNYA, C15 kısa çekiş → ajanın birebir eski→yeni metni Fable'ca yerleştirildi 13/13 · Fable'a: §5 Kaynak R13 R17 R19 R25 R26 telsiz · §4 Referans farkları C15 C18 C19 C20 |
| 15.10.2026 | — | Fable | — | sayaç düzeltmesi | ODA/DURUM.md | AJAN_CAGRI 18'e yanlış çekilmişti (G03 başlatılınca doğrusu 17); G07 ile 19 |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G03 (yeni ajan) | sonnet | K-GENEL + G03-1/2 + D1/T1 + tur-1 yedeği ↔ güncel G03 | ODA/F5_goruntu-yonetmeni_2_G03.md | kararların hepsi dosyada uygulanmış · açık 3 düzeltme (C30 `dies away`→`fades away` · C27 not çelişkisi · C36 `tug docked` ikinci gemi riski) ajanın birebir metniyle Fable'ca yerleştirildi 3/3 · Fable'a: §5 R29 R33 1,5→2,5 · R36 R37 Kaynak telsiz · §4 Referans farkları C27 C28 C33 C34 C36 · risk C29 drone varış saniyesi, C33 ağız küçük, KASA ALARM cümlesine drone şerit eki (C29 C30 C32) |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G05 (yeni ajan) | sonnet | K-GENEL + G05-1 + D2/T2 + tur-1 yedeği ↔ güncel G05 | ODA/F5_goruntu-yonetmeni_2_G05.md | kararların çoğu dosyada uygulanmış · R52 yeni metin · C60 YEDEK + ilk deneme · K10 ≤3 s C56 C58 açıktı → ajanın birebir metni Fable'ca yerleştirildi 2/2 · K17 C52 C57 değmez · Fable'a: §5 R54 1,5→3,0 · R56 1,5→2,0 · R58 1,5→4,0 · §4 Referans farkları C50 C53 C55 C56 |
| 15.10.2026 | F5/1b | goruntu-yonetmeni G07 (yeni ajan) | sonnet | K-GENEL + G07-1 + D2/T2 + tur-1 yedeği ↔ güncel G07 | ODA/F5_goruntu-yonetmeni_2_G07.md | kararların çoğu uygulanmış · U1-U7 (K18 bilek C73 C77 C78 C83 · K10 YEDEK C74 C84 + iş emri) ajanın birebir metni Fable'ca yerleştirildi 7/7 · Fable'a: §5 R78 1,5→3,5 · R79 telsiz · kelepçe yakası 3.KESTREL↔14.ISKELE AÇIK RİSK → F7 kare kapısı C80 C84 |
| 15.10.2026 | F5/1b | Fable (mekanik) | — | 8 §K raporu + PROMPTLAR EKLE | FILM §3 §4 §5 | §5 saniye R12 R29 R33 R49 (Fable: vuruş sınırı) R54 R56 R58 R78 R84 R85 R87 R88 R92 R93 · Kaynak telsiz R02 R13 R17 R19 R25 R26 R36 R37 R79 R89 · §4 Referans 33 çekimde EKLE'den türetildi · §3 Kullanan çekimler EKLE'den · §4 sonuna SMOKE P18 notu · film_dogrula hepsi ✅ (uyarı: 95 replik, gerekçe §5'te) |
| 15.10.2026 | F5/kapı | denetci | sonnet | KABUL Ö + F5 · F5 ODA · PROMPTLAR · FILM §3-§5 | ODA/F5_denetci_1.md | ❌ yok · KAPANAMAZ (kanıt eksik, 20 tur sınırı) · doğrulanamayan: Ö3-Ö5 G04-G08, Ö2 EKSİK kelimesi yorumu, F5.4 FLOW satırı, F5.6 F5.7 F5.8 F5.10 · SendMessage devamı (sayılmaz) |
| 15.10.2026 | F5/kapı | denetci (devam) | sonnet | doğrulanamayan maddeler | ODA/F5_denetci_2.md | KAPANABİLİR · mekanik ❌ yok · yargı ❌ F5.10 (§4 Risk C03 vizör, C02 eski hücre) → Fable düzeltti (+ telsiz hücreleri) · DOĞRULANAMADI F5.7 F5.8-C74 F5.2 → AŞILAN KAPILAR · **F5 KAPANDI** (Fable) |
