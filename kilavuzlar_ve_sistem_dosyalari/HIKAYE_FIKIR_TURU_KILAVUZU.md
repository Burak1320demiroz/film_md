# 💡 HİKÂYE FİKİR TURU KILAVUZU — gerilim → aday havuzu → eleme → tek hikâye

> **Ne bu dosya:** `yeni-film` akışının **0.7a** adımında koşan **üretim yöntemi**.
> Hikâye onayına (0.7b) giden tek hikâyeyi, ilk akla gelenden değil, üç yöntemle
> açılmış bir havuzdan seçtirir. Kapı değildir: puan vermez, soru eklemez, ders
> taşımaz. Çıktısı sahibin düz Türkçe okuduğu bir hikâye + iki elenmiş adaydır.
>
> **Neden var (21.09.2026):** deponun kendi ölçümü aynı üç sebebi tekrar etti —
> istek yok · bedel/seçim yok · doruk/bitiş yok (`FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md`,
> `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` §0 "novum gösterisi", D158 · D202 · D211).
> Kanca skoru aynı bantta plato yaptı (`HOOK_VE_ILK_SAHNE` §0③). 14.09 kararı
> "kural eklemek kaliteyi artırmadı" dedi; HİKÂYE ONAYI kapısı hikâyeyi onaylatıyor ama
> **üretmiyor**. Bu dosya üretim tarafıdır: önce geniş, sonra dar.
>
> **Kaynak:** yöntem **Serge Shima — github.com/smixs/creative-director-skill**'den
> damıtılmıştır (CC BY 4.0, atıf zorunlu · eklenme 21.09.2026). Reklam brief alanları
> (marka · hedef kitle · tagline · medya), puan tabloları ve vaka kütüphanesi
> **alınmadı**; depoya yalnız sıra ve teknik taşındı (`SKILL_KULLANIM_KILAVUZU` §0①).
> Eleme sorularının biçimi (evet/hayır + kanıt, eşik gizli) **smixs/skill-conductor**
> BinEval yönteminden alındı (MIT).

---

# 0. ⚠️ SINIRLAR — bu kılavuz ne yapmaz

```
① PUAN YOK. Adaylara 1-10 verilmez, yüzde yazılmaz. 17/17 kapı imzası tam
   filmin hikâyesi vana tamiriydi; kendi kendine verilen puan ölçüm değildir.
   Eleme evet/hayır + tek satır kanıtla yapılır.
② SORU YOK. Dört soru + beşinci soru (hikâye onayı) değişmez; bu tur beşinci
   sorunun İÇİNİ doldurur, altıncı soru açmaz.
③ KİLİT YOK. Bu dosya ders, kilit, kapı numarası taşımaz; 0.7'nin "hiçbir
   ders/kılavuz/QA açılmadan" kuralının TEK istisnasıdır çünkü yöntemdir,
   içerik kuralı değildir. Ders ve kapı adım 2'den sonra gelir ve hikâyeyi
   İYİLEŞTİRİR, üretmez.
④ REKLAM BRIEF'İ YOK. Marka, hedef kitle yaşı, tagline, kanal planı sorulmaz.
   Bu bir film, kampanya değil.
⑤ ÇIKTI DÜZ TÜRKÇE. Sahip okur: D-numarası · "novum" · kurulum harfi ·
   "kilit" geçmez (㉙ jargon). Ders dili adım 4'te `02_KONSEPT_VE_RISK`'e gider.
```

---

# 1. NEREDE KOŞAR — akıştaki yeri

```
0.5 SORULAR  → dört cevap + sahibin konusu (+ AI seçtiyse sayaç 🎭 ve REHBER §8 gerekçesi)
0.7a FİKİR   → §2 gerilim → §3 havuz → §4 eleme → §5 duygu → §6 gözdeyi öldür   [BU DOSYA]
0.7b HİKÂYE  → A adayı §7 omurgayla tam yazılır → beşinci soru (§9)
1   KLASÖR   → 00_HIKAYE_ONAYI: onaylı metin + ADAYLAR bloğu
4   KONSEPT  → 02_KONSEPT §0⑥ fikir turu kaydı + §5 ÖN-OTOPSİ (§8)
```

Girdi yalnız 0.5'in cevapları ve sahibin konusudur. AI konu seçtiyse doyum
bilgisi zaten elde (sayaç 🎭 + `KILAVUZ_REHBERI` §8); sahip konu verdiyse §8
matrisi yalnız §4⑤ doyum sorusu için açılır — başka hiçbir dosya açılmaz.

---

# 2. GERİLİM CÜMLESİ — hikâyeden önce tek cümle

```
<karakter> <iş> istiyor, ama <engel>, çünkü <neden>.
```

- **İş**, film başlamadan var olan somut bir eylemdir: dikmek · taşımak · kapatmak ·
  geri getirmek · teslim etmek. "Anlamak · görmek · fark etmek" iş değildir
  (`03_PLAN_ONCESI` B5 KAPI 1 — gerekçe orada, burada tekrar edilmez).
- **Engel** üç tipten biridir ve tipi yazılır:
  `insanî` (karakterin kendi bedeni/geçmiş kararı) · `ortam` (fizik, kalıcı değişen parça) ·
  `ilişki` (ikinci insan, aynı fikirde olmadıkları an — `ONERME_VE_NOVUM` §1 İLİŞKİ satırı).
- **Neden** cümleyi tazeler: "çünkü" kısmı silinince cümle hâlâ doğruysa neden yoktur.
- **Tazelik testi:** bu cümle konuya bakışı yeniliyor mu? Konunun ilk akla gelen
  cümlesiyse (uzayda yalnız adam hayatta kalmak istiyor ama oksijen bitiyor) — geç,
  §3 yöntemleri zaten bunu kırmak için var.

Gerilim cümlesi sohbete yazılır; hikâye onaylanınca `02_KONSEPT` §0⑥'ya iner ve
B5 İSTEK/ENGEL satırlarının tohumu olur. Yayın varsa VİRAL KART'ın "TEST EDİLECEK
TEK HİPOTEZ" satırı da budur (`YOUTUBE_VIRAL_SANS` §4).

---

# 3. ÜÇ YÖNTEM, SEKİZ-ON İKİ LOGLINE — havuz

Her turda **üç ayrı kategoriden birer yöntem** seçilir; aynı yöntemle bütün adaylar
üretilmez. Yöntem adı sohbete yazılmaz, adım 4 kaydına yazılır.

| kategori | yöntem | film için tek satırlık uygulama |
|---|---|---|
| **yapısal** | SIT · çıkarma | ortamın vazgeçilmez sayılan bir parçasını sil (yedek tüp yok · pencere yok) — hikâye ne olur |
| yapısal | SIT · bölme | tek nesneyi/işi ikiye böl, iki yere koy (giysinin yarısı içeride, yarısı dışarıda) |
| yapısal | SIT · görev birleştirme | bir nesneye ikinci bir iş yükle (anten aynı zamanda bastondur) |
| yapısal | SIT · öznitelik bağımlılığı | iki değişkeni bağla (ışık azaldıkça halat kısalır) |
| yapısal | SCAMPER · ters çevir / uyarla | işin yönünü tersle (kurtaran kurtarılan olur), başka meslekten ödünç al |
| **çağrışım** | bisosiyasyon | iki alakasız düzlemi çarpıştır (uzay yürüyüşü × düğün töreni) |
| çağrışım | rastgele giriş | rastgele somut nesne seç (dikiş makinesi) — konuya zorla bağla |
| çağrışım | zorlanmış bağlantı | konunun nesnesini başka bir günlük ritüelle eşle (basınç kontrolü × ninni) |
| **tersine** | ters beyin fırtınası | "bu film nasıl kesin sıkıcı olur" listesini yaz, her maddeyi tersle |
| tersine | en kötü fikir | en saçma öneriyi yaz, içindeki kullanılabilir çekirdeği al |
| tersine | PO kışkırtma | mantıksız bir "PO" cümlesi kur (PO: kask içeriden açılır) — sonuçlarını izle |

```
□ Her yöntemden 3-4 logline → toplam 8-12. Logline ≤ 25 kelime, olay dili
  (kim · ne yapıyor · ne değişiyor) — 00_HIKAYE_ONAYI LOGLINE biçimiyle aynı.
□ ⭐ İLK ÜÇ ISINMADIR. Silinmez, işaretlenir; seçim beşinciden sonrakilerden
  yeğlenir. İlk akla gelen fikir sıralamanın değil belleğin fikridir.
□ Her logline gerilim cümlesine bağlanır: hangi engel, hangi tip. Bağlanmayan
  logline "ilginç" olsa da havuza girmez.
```

---

# 4. GERİLİM TESTİ + BEŞ ELEME SORUSU — evet/hayır + kanıt

Önce **gerilim testi:** aday çözümsüz bir gerilim taşıyor mu — her şey temiz
çözülüyorsa özgünlük zayıftır; hikâye çözülmeyen boşlukta yaşar. Sonra her aday
beş soruya **evet/hayır + tek satır kanıt** ile cevap verir. Eşik söylenmez;
kaç "evet" gerektiği yazılmaz — beşi de evet olmayan aday elenir, gerekçesi
tek satırdır.

| # | soru | kanıt biçimi | adres (kural orada) |
|:--:|---|---|---|
| ① | **TEK KARE** — durdurulmuş bir karede anormallik parmakla gösterilir mi | "<nesne> <hâlde>" cümlesi, nesnenin ADI var | `ONERME_VE_NOVUM` §4① · D157 |
| ② | **İSTEK** — karakter film başlamadan var olan bir İŞ mi yapıyor | fiil: dikmek/taşımak/kapatmak… | `03_PLAN_ONCESI` B5 KAPI 1 |
| ③ | **BEDEL** — geri dönmez bir kayıp adlandırılabiliyor mu | "<ne> kaybediyor, <hangi sahnede>" | `03_PLAN_ONCESI` B5 KAPI 2 · D206 |
| ④ | **MUHATAP** — eylemin bir yankısı var mı (ikinci insan / kendi geçmiş kararı / kendi bedeni / ortamın kalıcı değişen parçası) | muhatap adı + ne cevap veriyor | `03_PLAN_ONCESI` B5 · `06_HIKAYE_HATTI` §4 |
| ⑤ | **DOYUM** — depoda aynı olay örgüsü var mı; gezegen/ortam değişince aynı film mi | §8 matrisinde en yakın iki film + FARK cümlesi | `KILAVUZ_REHBERI` §8 · `YOUTUBE_VIRAL_SANS` §2 m.15 |

```
⛔ Kanıt sütunu boş bırakılmaz; "evet" tek başına cevap değildir.
⛔ Aday elenirken yöntemi suçlama — elenen loglineların yarısı ısınma olur, normaldir.
□ Kalanlardan ÜÇ aday: A (önerilen) · B · C. Üçten az kaldıysa §3'e dönülür,
  aynı yöntemler DEĞİL başka üçlü.
```

---

# 5. DUYGU ADI — üç kademe

Aday, izleyicinin **son karede** hissettiği duyguyla adlandırılır. Tema değil
(tema tek kelimedir ve `TEMA_MUHENDISLIGI` §3'ten adım 4'te seçilir), duygu.

| kademe | örnek | test |
|---|---|---|
| **sıradan** | mutlu · üzgün · kızgın · korkmuş · şaşkın | tek kelimeyle söylenebiliyor → unutulur |
| **belirli** | nostaljik · meydan okuyan · korunmacı · vakur · tanık olmuş · özleyen · kabullenmiş | "mutlu/üzgün" ile değiştirilince cümle bozuluyor |
| **çift-duygu** | buruk gurur · savunmacı umut · vakur yas · isteksiz iyimserlik · yüce dehşet · alaycı içtenlik · kırılgan meydan okuma | aynı anda iki zıt his; izleyici "buna kelime bulamamıştım" der |

```
□ A adayı ÇİFT-DUYGU taşır. Taşımıyorsa A, B'yle yer değiştirir ya da §3'e dönülür.
□ Duygu adı sohbete yazılmaz (sahip düz hikâye okur); adım 4 kaydına yazılır.
□ Tema ile duygu aynı kelime olamaz: "yalnızlık" tema, "vakur yas" duygu.
```

---

# 6. GÖZDEYİ ÖLDÜR — A'ya karşı argüman

A seçildikten sonra ona **üç satır karşı argüman** yazılır: bu film neden
izlenmez, neden sıradan, neden üretilemez. Karşı argüman hikâyeden güçlüyse A
düşer, B yükselir; tur tekrar etmez, karşı argüman B'ye de yazılır.

```
□ RAHATSIZ EDİCİ > RAHAT. Kimseyi rahatsız etmeyen hikâye kimseyi tutmaz —
  bedel gerçekten canını yakıyor mu, yoksa "üzgün hissediyor" mu (SENARYO §2.3).
□ ÖZGÜLLÜK. Karakteri ya da ortamı değiştir (başka gezegen, başka meslek):
  hikâye aynen çalışıyorsa bu hikâyeye ait bir şey yoktur.
□ TEK CÜMLE. A tek cümleyle anlatılamıyorsa hikâye değil plandır.
```

Karşı argümanın sonucu düz Türkçe olarak `00_HIKAYE_ONAYI` ADAYLAR bloğuna
(elenen adayların "neden"i) ve adım 4 kaydına iner.

---

# 7. HİKÂYE OMURGASI → SAHNELER

A adayı, sahne sayısı kadar satıra **nedensellik zinciriyle** açılır. İskelet
(Story Spine): *bir zamanlar · her gün · ama bir gün · bunun yüzünden (×n) ·
ta ki sonunda · o günden beri*. Sahne haritası değildir — satırların birbirini
**doğurmasını** garanti eden iskelettir.

| format | iskeletin kullanılan kısmı | not |
|---|---|---|
| dikey (6 sahne) | yalnız **ama bir gün → bunun yüzünden ×3 → ta ki sonunda** | S0 çatışmanın içinden açılır; "bir zamanlar / her gün" yoktur |
| 12 sahne | tam iskelet; "her gün" tek sahne | kurulum bütçesi `HOOK` §8 (açılış bütçesi) |
| 24 · 36 · 48 sahne | "bunun yüzünden" zinciri uzar | ⛔ her halka bir SEÇİM ya da BAŞARISIZ DENEME taşır; art arda iki halka aynı vuruş olamaz |

```
⛔ VURUŞ ZAMANLAMASI BURADAN ÇIKMAZ. Katalizör saniyesi, her şeyin kaybı,
   doruk yeri SENARYO_VE_VIRAL_KAMERA §2 vuruş haritasındadır; bu iskelet
   yalnız "sonraki satır öncekinden doğuyor mu" sorusunu cevaplar.
□ Sahne satırı ≤ 15 kelime, olay dili — 00_HIKAYE_ONAYI SAHNELER biçimi.
□ Kontrol (Pixar kuralları, dört madde):
   mücadele > başarı  · en az bir BAŞARISIZ DENEME var (D158 B2b) ·
   son satır ilk yazılır (sona doğru yazılan hikâye durmaz, biter — D141) ·
   karakterin bir fikri var (tepki veren değil seçen — D202)
□ "bunun yüzünden" satırında olay dışı sözcük (anlar, hisseder, fark eder)
   varsa satır olay değildir; yeniden yazılır (D213: temas · değişim · sonuç).
```

---

# 8. ÖN-OTOPSİ — adım 4'te, `02_KONSEPT_VE_RISK` §5

Hikâye onaylandıktan ve okuma bittikten sonra (adım 4), konsept kapılarından
önce: **film çekildi ve izlenmedi — neden?** Beş arıza modu, her biri olasılık ×
etki (düşük/yüksek); yüksek × yüksek hücre ya önlem alır ya konsepti öldürür.

| arıza modu | soru | adres |
|---|---|---|
| **kanal tezi** | "her film bir gerçek fizik kuralıyla hesaplaşır" tezine oturuyor mu | `apexaic/README.md` tez · `.agents/product-marketing.md` |
| **politika / red** | motorun düşürdüğü bir sınıfa giriyor mu | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` · `POLITIKA_VE_URETILEBILIRLIK` |
| **üretim tek-hata noktası** | tek bir varlık/olay tutmazsa film çöküyor mu (biçim kilidi, kask, metin) | `REFERANS_PAKETI` §1 tetikleyiciler · D146 |
| **tutundurma** | ilk on saniyede soru var mı, son on saniyede çıkış var mı | D211 · `HOOK` §2 S0 çıkış testi |
| **doyum** | §4⑤'in cevabı hâlâ geçerli mi — analiz sırasında yakın bir film çıktı mı | `KILAVUZ_REHBERI` §8 |

```
KARAR: GO / REVİZE / ÖLDÜR
   REVİZE → ne değişiyor tek satır; onaylı metne dokunuyorsa 00_HIKAYE_ONAYI
            SAPMA + yeniden onay (adım 5 kuralı).
   ÖLDÜR  → 0.7'ye dönülür, B adayı yazılır; tur sayacı devam eder (en çok 3).
Yüksek × yüksek satır, 02_KONSEPT §5 risk kartı tablosuna kart olarak iner.
```

---

# 9. ÇIKTI BİÇİMİ — sohbete ne yazılır, dosyaya ne iner

**Sohbete (0.7b · düz Türkçe · sahip okur):**

```
GERİLİM        tek cümle (§2)
A — <başlık>   LOGLINE · NEDEN İZLENİR · BEDEL · SAHNELER S0…Sn   ← tam
B — <başlık>   logline · neden izlenir · bedel                     ← üç satır
C — <başlık>   logline · neden izlenir · bedel                     ← üç satır
A'YA KARŞI     üç satır (§6) — ve neden yine de A
ELENENLER      aday başına tek satır (logline kısaltması · hangi soru hayır)
```

**Beşinci soru** (`AskUserQuestion`, tek soru, dört seçenek):
`① ONAY (A)` · `② ADAY B'yi tam yaz` · `③ ADAY C'yi tam yaz` · `④ RED — üçü de olmaz`.
DEĞİŞTİR notu "Diğer"e yazılır (mevcut davranış). B/C seçilince o aday §7 ile tam
yazılır ve aynı soru tekrar sorulur. **En çok üç tur**; üçüncü RED → konu değişir.

**Dosyaya (klasör açılınca):**

```
00_HIKAYE_ONAYI.md   onaylı A + ADAYLAR bloğu (B, C: logline · neden elendi — düz Türkçe;
                     satırlar "B —" / "C —" ile başlar, S-ile değil)
02_KONSEPT §0⑥      gerilim cümlesi · engel tipi · duygu adı (kademe) · üç yöntem ·
                     doyum (en yakın iki film + fark) · öldürülen gözde (karşı argüman, sonuç)
02_KONSEPT §5       ÖN-OTOPSİ tablosu + KARAR (§8)
```

---

# 10. ⛔ YAPILMAYACAKLAR

```
⛔ Puan, yüzde, "9/10" — hiçbiri yazılmaz.
⛔ Beşinci sorudan başka soru sorulmaz; "hangi yöntem" sahibe sorulmaz.
⛔ Marka · hedef kitle · tagline · medya planı alanları açılmaz.
⛔ Isınma (ilk üç) fikir aday diye sunulmaz; sunulacaksa §4'ü geçmiş olmalı.
⛔ Ders, kılavuz, QA raporu açılmaz — yalnız bu dosya ve (sahip konu verdiyse
   doyum için) REHBER §8 matrisi.
⛔ Üçten fazla tur yok; ÖLDÜR kararı da turdan sayılır.
⛔ Bu dosyanın hiçbir satırı prompta yazılmaz; hikâye PLAN ve prompt iskeletine
   adım 8'de, kendi kurallarıyla iner.
```

---

# 11. ÖLÇÜM — bu kılavuz çalışıyor mu

Kılavuzun başarısı burada değil, QA tablosunda okunur: fikir turuyla yazılan
filmlerin `T4_HIKAYE_KALITE` ④ satırlarında **Kanca · Karakter · Final** ve
`T12_HOOK_KALITE` ⑫ değerleri, öncekilerin plato bandıyla (`HOOK` §0③)
karşılaştırılır. Üç film ölçülmeden yargı verilmez; skor aynı bantta kalırsa
kılavuz çalışmıyordur ve §3 yöntem havuzu ya da §4 soruları değişir — yeni
kural eklenmez. Yayın varsa `08_YAYIN_PERFORMANS_TABLOSU` geri-beslemesi
(kart Y, 14. gün) bu dosyayı revize eder; sıra veri → belge → (tekrarlarsa) ders.

Açık iş kaydı: `AGENTS.md` §6 "FİKİR TURU" satırı.
