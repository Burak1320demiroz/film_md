# ⚠️ THE_SOLAR_MIRROR — UYARI NOTLARI VE ARIZA DENETİMİ

> **Kaynak:** `01_QA_DERS_HASADI.md` × `03_SAHNE_SIRALAMASI.md`

---

## 1. HASAT × SIRALAMA KESİŞİM UYARILARI

1. **S00 & S11 (Açılış/Kapanış Kafiyesi):** Setup A kadrajı S00 ve S11'de birebir aynı lens (35mm), aynı açı ve aynı HELIOSTAT S04 konumuyla çekilmelidir. S11'de Mara mekiğe bağlı değildir, boşlukta küçücük süzülür. Kadraj sapması YASAK (D197 / Rhyme Broken riski).
2. **S01 (Pürmüz Ateşlenmesi):** Plazma kesici belden ayrılırken sıfır-g momentum kuralına (D198) kesinlikle uyar. Alet doğrusal bir hatta savrulur, havada asılı durmaz veya akışkan gibi dönmez.
3. **S02 (Aynadaki Tehdit):** Aynadaki yansımada mekiğin LOX tankı net görünmeli, ama gerçek mekiğe bakıldığında üzerinde hiçbir ışık hüzmesi bulunmamalıdır. Çift durumun görsel ayrımı %100 net olmalıdır.
4. **S03–S06 (Real-Time 30s Geri Sayım):** Real-time 30 saniyelik sayaç S03'ün başlangıcından (00:55) S06'nın sonuna (01:25) kadar tam 30.0 saniye sürmelidir. Zaman sıkıştırma veya atlama yapılmaz.
5. **S05 (O₂ Divert ve RCS Ateşleme):** Solenoid aktüatör basınçla açılırken suit fanının sesi değişir. Kask vizörü (D197) %100 şeffaf kalmalı, Mara'nın gözlerindeki kararlılık (D202) okunmalıdır.
6. **S06 (Işının Geçişi):** Vakumda lazer/güneş ışını hava jeti gibi GÖRÜNMEZ. Huzme vakumda boşlukta çizilmez; yalnız çarptığı çelik truss yapısında turuncu-beyaz ergime üreterek varlığını kanıtlar.

---

## 2. TEKRAR EDEN ARIZA TABLOSU DENETİMİ

| Arıza Kalemi | Bu Filme Düşen Risk | Uygulanacak Kesin Önlem / Cevap |
|---|---|---|
| **🔴 Kask Vizör Opaklaşması** | Yörünge ışığında vizörün aynaya/siyaha dönüşmesi. | Negative prompt'a `tinted visor, mirrored visor, opaque helmet glass` eklenir. Positive prompt'a `optically clear zero-tint glass` yazılır. |
| **🔴 Sıfır-G Asılı Kalma** | Savrulan aletin veya astronotun durağan kalması. | Continuous linear vector ve linear momentum keyword'leri eklenir; `hovering, floating still` kelimeleri yasaklanır. |
| **🔴 Güneş Açısı Sapması** | Sahneler arası Güneş ışığının yön değiştirmesi. | 1 km'lik HELIOSTAT dizisinde Güneş açısı tüm promptlarda `harsh parallel orbital sunlight from top-right (45 deg)` olarak sabitleştirilir. |
| **🔴 HUD Metninin Videoya Girmesi** | Prompt'a HUD metni yazılması sonucu videoda saçma harfler çıkması. | Prompt metinlerine HİÇBİR rakam veya HUD kelimesi yazılmaz. Metinler post-kurgu overlay olarak kurgu aşamasında eklenir. |
| **🔴 Işının Vakumda Çizilmesi** | Lazer ışınının uzay boşluğunda fosforlu çizgi gibi görünmesi. | Prompt'a `no visible beam in vacuum, invisible focal ray` yazılır. Etki yalnız hedef çelik yapıdaki ergime ile gösterilir. |
| **🔴 Plastik/Balmumu Ten Dokusu** | Kask içindeki yüzde fotogerçekçilik kaybı. | `35mm film grain, visible skin pores, sweat beads, fatigue lines` eklenir; `airbrushed, CGI, render` yasaklanır. |
| **🔴 Ağız Hareketi / Lip-Sync Hatası** | Telsiz konuşmasında ekranda ağız kıpırdaması. | Replikler yalnız kask içi telsiz hoparlörü karakteratiğinde işlenir. Mara konuşurken kadraj gözlere veya nesneye kilitlenir. |
| **🔴 Obje Kaybolması/Değişimi** | Plazma kesici veya harness straps'in klipler arası değişmesi. | Referans paketi hazırlığı ile harness ve plazma kesici görsel seed ile çapalanır. |
| **🔴 Sorumsuz İkinci İnsan** | Kadrajda ikinci astronot belirmesi. | Negative prompt'a `second astronaut, clone, multiple people` zorunlu eklenir. |
| **🔴 Dünya/Arka Plan Warping** | Dünyanın yörünge eğriliğinin sahneler arası erimesi. | Arka planda Dünya yasağı: Arka plan derin uzay (deep space), yıldızlar ve dev Güneş Aynası dizisidir. |
| **🔴 Patlama / Alev Efekti** | Vakumda alev yumağı oluşması. | Patlama ve alev YASAK. Yalnızca turuncu-beyaz akkor metal ergimesi ve kristalize gaz fışkırması kullanılır. |
| **🔴 Bayrak / Logo İhlali** | Suit üzerinde bayrak belirmesi (Politika red). | Negative prompt'a `flag, agency logo, mission patch, text, numbers` yazılır. |
| **🔴 Kask İçi Aşırı Işık (Glow)** | Kask içi LED'lerin yüzü kör etmesi. | Kask içi ışıklandırma subtle dim HUD reflection ile sınırlanır, yüzü patlatmaz. |
| **🔴 Tether Kararsızlığı** | Tether ipinin uzayda elastik yay gibi sallanması. | Tether gergin çelik kablo olarak tanımlanır; S04'te kilidi açılınca karabina boşlukta serbest süzülür. |
| **🔴 Mekiğin Aşırı Hızlı İtmesi** | RCS ateşlemesinde mekiğin jet gibi fırlaması. | Mekik devasa kütledir (Orbital Service Shuttle); RCS ateşlenince ağır, milimetrik ve ataletli kayma gösterir. |
| **🔴 Finalde Belirsiz Bedel** | Mara'nın durumunun muğlak kalması. | S10'da kask içi HUD'da O₂ tükenmesi + S11'de mutlak kask içi sessizlik ile bedel %100 netleştirilir. |
