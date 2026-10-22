# 🎯 THE_PRICE_OF_HOME — QA Değerlendirme, Kurgu Kararları ve Dersler Raporu

> **Dosya:** `THE_PRICE_OF_HOME (2).mp4` (~03:19, 20 kesme)  
> **Tarih:** 2026-10-22  
> **Kapsam:** Sahibin ilettiği Anlatım Testi (A1–A4), İzleme Formu (A/B), Süreklilik Denetimi (26 bulgu) ve Teknik Tarama (15 bulgu).  
> **İlgili Kural:** `AGENTS.md` §1b (Kural Türleri), §3 (Hata Nerede Doğdu — Müdahale Oraya), §1 ④ (Hata kural olmaz, film notu olur).

---

## 1. YÜRÜTME ÖZETİ (EXECUTIVE SUMMARY)

* **Önerme ve Duygusal Çekirdek:** Eve (Dünya'ya) dönebilmek için aşkını ve hafızasını bedel ödeme fikri (*"The Price of Home"*) senaryo ve tema olarak son derece vurucu.
* **Kritik Kırılma ve Çelişki Noktaları:**
  1. **Finalin Trajediyi Yok Etmesi (A1 / 03:10):** 02:56'da Mara'nın *"Who are you?"* sorusu ve 03:00'da kristale hapsolan anılarla uzaylının iç çekişi çok güçlü bir dramatik zirvedir. Ancak hemen ardından gelen 03:10 sahnesinde iki astronotun hiçbir şey olmamış gibi birbirine sevgiyle ve neşeyle gülümsemesi bütün trajik bedeli sıfırlamakta, izleyicide kafa karışıklığı yaratmaktadır.
  2. **Açılışın Durağanlığı (A2 / 00:15 - 00:44):** İlk 45 saniye boyunca diyalog ve aksiyon olmadan karakterlerin konsol başında hareketsiz beklemesi izleyici terk riskini (A2) tavan yaptırmaktadır.
  3. **Kask Kaybolması ve Üçüncü Astronot (S1 / S4):** 00:41'de erkek astronotun kaskı tek çekimde yok olmakta (saçı ve sakalı görünmekte), 00:45'te fotoğraf sahnesinde arkada üçüncü bir astronot kaskı belirmektedir.
  4. **Ses ve Montaj Hataları (A4 / A3):** 00:58'de *"I'm trying to find a way"* cümlesi 2 saniye arayla iki kez üst üste binmekte; 01:19'daki diyalog müzik altında boğulmakta; 01:47'de müzik bıçak gibi kesilmektedir.

---

## 2. HATA NEREDE DOĞDU & MÜDAHALE HARİTASI (`AGENTS.md` §3)

| Sorun | Zaman | Hatanın Doğduğu Yer | Belirti | Müdahale Yolu |
|---|---|---|---|---|
| **Finaldeki çelişkili gülümseme** | 03:10 – 03:19 (C21) | **KURGU** | Hafıza kaybından sonra neşeli gülümseme gelmesi | **Kurguda C21 kesilip atılmalı.** Film 02:56 *"Who are you?"*, erkeğin yıkılışı ve 03:00 uzaylı/kristal planıyla kararmalıdır. |
| **Erkeğin kaskının yok olması** | 00:41 – 00:44 (C05) | **BAŞLANGIÇ KARESİ / PROMPT** | Erkek astronotun kasksız ve sivil saç/sakalla belirmesi | C05 karesi R01 Erkek Astronot referansıyla yenilenmeli (kask kapalı). |
| **Fotoğraf arkasında 3. astronot** | 00:45 (C06) | **BAŞLANGIÇ KARESİ** | Arka planda fazladan bir astronot gövdesi belirmesi | Başlangıç karesi temizlenmeli; kadrajda yalnız Mara ve Eli olmalı. |
| **Mükerrer replik hatası** | 00:58 – 01:02 (C07) | **KURGU / SES** | *"I'm trying to find a way"* sesinin iki kez üst üste çalması | Kurguda ikinci ses bloğu timeline'dan silinmeli. |
| **Diyaloğun müzik altında boğulması** | 01:19 – 01:21 (C09) | **SES MİKSİ** | Mara'nın fısıltısının müzik tarafından bastırılması | Müzik kanalına o saniyede ducking (-6 dB) uygulanmalı. |
| **Ani müzik kesilmesi** | 01:47 – 01:48 (C12) | **KURGU** | Orkestra müziğinin aniden kesilip solo yaylıya atlaması | İki müzik parçası arasına 1.5 saniyelik çapraz geçiş (crossfade) konmalı. |
| **Açılışta 30 sn hareketsiz bekleyiş** | 00:15 – 00:44 (C03-C05) | **KURGU** | Diyalogsuz ve aksiyonsuz uzun planlar | Kurguda C03 ve C04 planları 4–5'er saniyeye kırpılarak kanca öne çekilmeli. |
| **Uzaylının mor tenden beje dönüşmesi** | 03:00 (C20) | **PROMPT / REFERANS** | Mor derili Vey'in açık renk kemik başlıklı yaratığa dönmesi | C20 promptuna R03 Vey referansı birebir kilitlenmeli. |
| **Mara'nın kolunda Amerikan bayrağı** | 03:10 (C21) | **PROMPT / MODEL** | Sarı şerit yerine ABD bayrağının basılması | C21 atılınca kendiliğinden çözülür; gerekirse prompttan bayrak sildirilmelidir. |

---

## 3. KURGUCU İÇİN HEMEN YAPILACAKLAR (SIFIR MALİYETLİ REVİZYONLAR)

1. **Finali Düzelt (03:10 Planını At):**
   * 03:10'daki son gülümseme planı montajdan çıkarılmalı.
   * Kurgu sırası:
     - 02:50: Erkek astronot sevinçle ağlar.
     - 02:56: Mara ona döner ve soğukça sorar: *"Who are you?"*
     - Erkeğin yüzündeki gülümseme donar ve yıkılır.
     - 03:00: İstasyonda uzaylının önündeki kristal Mara'nın anılarıyla parlar, uzaylı gözlerini kapatıp derin bir nefes verir.
     - **Kararma (Fade to black) ve Başlık Kartı:** *The Price of Home*.  
     *(Bu kurgu filmi buruk, unutulmaz ve trajik bir başyapıta çevirir.)*
2. **Çift Repliği Temizle:**
   * 00:58 - 01:02 aralığındaki mükerrer *"I'm trying to find a way"* ses izi tek kopyaya düşürülmeli.
3. **Müzik Kesintisini Bağla:**
   * 01:47'deki 1 saniyelik boşluk ve orkestra sıçraması crossfade ile pürüzsüzleştirilmeli.
4. **00:15 - 00:44 Arasını Dinamikleştir:**
   * İlk 45 saniyelik donuk bekleme kurguda kısaltılarak izleyicinin filme girişi hızlandırılmalı.

---

## 4. ÖNCELİKLİ YENİDEN ÜRETİM LİSTESİ (REVİZYON)

* **1. Öncelik — C05 (00:41):** Erkek astronotun kaskının yok olduğu çekim kasklı referansla yeniden üretilmeli.
* **2. Öncelik — C06 (00:45):** Arkadaki 3. astronot hayaleti temizlenmeli.
* **3. Öncelik — C20 (03:00):** Uzaylı Vey'in mor teni ve orijinal kafa formu korunarak kristal sahnesi tazelenmeli.

---

## 5. FİLM İÇİ DERSLER (`AGENTS.md` §1 ④)

1. **Trajik Finallerde "Dengeleyici" Son Kare Tuzağı:** AI kurgularında model genellikle "mutlu son" üretme eğilimindedir. Trajik hafıza kaybının ardından karakterlerin tekrar gülümsemesi çatışmayı sıfırlar. Kurgucu senaryonun bedelini korumalıdır.
2. **Astronot Kaskı Sürekliliği:** Basınç tulumlarında model "yüz ifadesi göstermek" için kaskı spontane olarak çıkarma eğilimindedir. Promptta `helmet visor fully sealed, face seen through transparent glass visor` ifadesi kilitlenmelidir.
3. **Mükerrer Ses İzi Kontrolü:** Model sesiyle üretilen diyaloglarda kurgucu timeline'a atarken mükerrer dalga formlarını mutlaka denetlemelidir.
