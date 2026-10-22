# 🎯 MOONMOTHER — QA Değerlendirme, Kurgu Kararları ve Dersler Raporu

> **Dosya:** `moonmother (1).mp4` (03:55, 23 kesme + başlık kartı)  
> **Tarih:** 2026-10-22  
> **Kapsam:** Sahibin ilettiği Anlatım Testi (A1–A4), İzleme Formu (A/B), Süreklilik Denetimi (51 bulgu) ve Teknik Tarama (22 bulgu).  
> **İlgili Kural:** `AGENTS.md` §1b (Kural Türleri), §3 (Hata Nerede Doğdu — Müdahale Oraya), §1 ④ (Hata kural olmaz, film notu olur).

---

## 1. YÜRÜTME ÖZETİ (EXECUTIVE SUMMARY)

* **Anlatım ve Atmosfer Gücü:** Görsel dil, bazalt kıyı, bulutlar ve halkalı gezegen atmosferi son derece epik ve büyüleyici. Beyaz zırhlı koruyucunun küçük vatoz yavrusunu kurtarıp dev anneye ulaştırma çabası izleyiciyi duygusal olarak yakalıyor.
* **Kritik Kırılma Noktaları:**
  1. **Uzaylı Karakterde Çıplak İnsan Sesleri (T8 / A4):** Ağzı bile olmayan biyomekanik varlıktan 6 ayrı sahnede (01:52, 02:01, 02:13, 03:11, 03:17, 03:34) mikrofona çok yakın insan nefesi, hıçkırık ve *"Hmm"* mırıldanması gelmesi izleyicinin sahneye olan inancını kırıyor.
  2. **10 Saniyelik Blok Ses Kopmaları (S7):** Her 10 saniyelik klip kesmesinde okyanus dalgası ve ambiyans müziği aniden kesilip sıfırdan başlıyor (toplam 22 adet ses atlaması).
  3. **Yaratık Morfları ve Ölçek Sapmaları (S1 / S6 / T6):** Yavru vatoz 00:52'de aniden ejderha/yarasa kanatları açıyor; 02:06'da kafasından antenler fırlıyor. Dev anne yaratık gökyüzünde dağ/gezegen büyüklüğündeyken kıyıda birden küçük deniz canlısı ölçeğine iniyor.
  4. **Kurgusal Atlama (S5 / A1):** 03:10'da kıyıda kalıp elleriyle veda eden karakter, 03:20'de nasıl çıktığı gösterilmeden aniden dev yaratığın kanadına binmiş yükseliyor.

---

## 2. HATA NEREDE DOĞDU & MÜDAHALE HARİTASI (`AGENTS.md` §3)

| Sorun | Zaman | Hatanın Doğduğu Yer | Belirti | Müdahale Yolu |
|---|---|---|---|---|
| **İnsan nefes ve mırıldanma sesleri** | 01:52, 02:01, 02:13, 03:11, 03:17, 03:34 | **SES / KURGU** | Omni modelinin klip sesine insan nefesi basması | Kurguda video ses kanalı sessize alınır (mute); uzaylı ve yaratık için F4 ses kütüphanesinden organik efektler konur. |
| **Her kesmede sesin bıçak gibi kesilmesi** | 00:10, 00:20 ... 03:50 (tüm kesmeler) | **KURGU** | Timeline'da kesintisiz yatak olmaması | Timeline altına baştan sona uzanan kesintisiz okyanus dalgası + rüzgâr ambiyans yatağı ve müzik miksi serilir. |
| **Yavrunun ejderha kanatları açması** | 00:51 – 00:53 (C06) | **BAŞLANGIÇ KARESİ / PROMPT** | Vatoz anatomisinin bozulup yarasa kanadı türemesi | Başlangıç karesinde yavrunun pürüzsüz vatoz yüzgeçleri sabitlenmeli; promptta "bat/dragon wings" çağrıştıracak kelimeler temizlenmeli. |
| **Kafada beliren ışıklı antenler** | 02:06 – 02:09 (C13) | **BAŞLANGIÇ KARESİ** | Yerde yatan yavrunun kafasından salyangoz anteni çıkması | C13 başlangıç karesi R01 Yavru referans sayfasıyla üretilerek anten oluşumu engellenmeli. |
| **Dev yaratığın ölçek zıplaması** | 00:50 (C06) ve 02:23 (C15) | **PROMPT / HAREKET** | Gökyüzünde devasa olan yaratığın kıyıda küçülmesi | Promptta "colossal mountain-sized scale" ve kadraj uzaklığı (extreme wide shot) korunmalı. |
| **İskelenin kendi kendine yıkılması** | 01:30 – 01:38 (C10) | **KURGU / ANLATIM** | Karakter iskelede yokken kayanın köpük gibi uçması | C09 sonundaki karakter konumu ile C10 dalga çarpması arasına karakterin geri çekilme anı eklenmeli veya plan kısaltılmalı. |
| **Yavrunun düşüş kopukluğu** | 01:40 → 01:50 (C11 → C12) | **KURGU / SEÇİM** | Uçan yavrunun düşüş anı olmadan yerde bitkin yatması | C11'in son saniyelerinde yavrunun irtifa kaybedip dalgalara yaklaştığı aralık seçilmeli veya C12 girişi yumuşatılmalı. |
| **Kanada ani biniş atlaması** | 03:10 → 03:20 (C20 → C21) | **KURGU / HAREKET** | Kıyıda veda ederken aniden kanatta oturur halde havalanma | C20 ile C21 arasına karakterin kanadın sırtına adım attığı 1-2 saniyelik bir ara hareket/kare eklenmeli. |

---

## 3. KURGUCU İÇİN HEMEN YAPILACAKLAR (SIFIR MALİYETLİ REVİZYONLAR)

1. **Klip Seslerini Sessize Al (Mute Klip Sesi):**
   * Video dosyalarının içinden gelen ortam seslerindeki mikrofona yakın insan nefesleri (`01:52`, `02:01`, `02:13`, `03:11`, `03:17`, `03:34`) timeline'da tamamen susturulmalı.
2. **Ambiyans Yatağı Döşe (`timeline.json` yataklar):**
   * Sahne boyunca kesintisiz akan 4 katmanlı ses kurgusu oluşturulmalı:
     - Katman 1: Derin okyanus dalgaları ve kıyı köpüğü.
     - Katman 2: Gece rüzgârı ve bazalt kaya yankısı.
     - Katman 3: Yavru ve annenin melodik çağrı sesleri (3 notalı biyolüminesans ışık çağrısı).
     - Katman 4: F4 besteci müzik miksi (kesmelerde kesilmeyen sürekli yaylı/synth dokusu).
3. **Durağan Yürüyüşü Kırp:**
   * `01:10 – 01:29` aralığındaki iki ardışık yürüyüş planı toplam 12–14 saniyeye indirilerek tempo artırılmalı.
4. **03:50 Başlık Kartı:**
   * Son 5 saniyedeki siyah başlık kartı aniden sessizliğe düşmemeli; müzik ve rüzgâr uğultusu yavaşça karararak (fade out) bitmeli.

---

## 4. ÖNCELİKLİ YENİDEN ÜRETİM LİSTESİ (REVİZYON)

* **1. Öncelik — C06 (00:50):** Yavrunun ejderha kanadı açması ve anne yaratığın ölçeğinin aşırı küçülmesi düzeltilmeli.
* **2. Öncelik — C13 (02:06):** Yerde yatan yavrunun kafasından fırlayan iki anten hatası başlangıç karesi düzeltilerek yeniden üretilmeli.
* **3. Öncelik — C21 (03:20):** Karakterin kanada biniş anını bağlayan ya da kanat üzerinde doğru başlangıç pozisyonunu veren temiz bir başlangıç karesiyle çekim tazelenmeli.

---

## 5. FİLM İÇİ DERSLER (`AGENTS.md` §1 ④)

1. **Uzaylı/Yaratık Filmlerinde Model Sesi Asla Kullanılmaz:** Ağzı olmayan varlıklara video üretim modelleri (Omni/Veo) insansı nefes ve ses halüsinasyonları eklemektedir. Bu tür projelerde video sesi daima kurguda atılmalı ve ses tasarımı tamamen harici kütüphaneden kurulmalıdır.
2. **Yaratık Anatomisi İçin Sabit Referans Şartı:** Vatoz benzeri canlılarda kanat/yüzgeç ayrımı modeller tarafından karıştırılmakta (kuş/ejderha kanadına dönüşmekte) ve anten gibi rastgele uzantılar türemektedir. Başlangıç karesi denetimi olmadan video üretimine geçilmemelidir.
3. **Mekân ve Gökyüzü Sürekliliği (Halkalı Gezegen):** Gökyüzündeki halkalı gezegenin bir sahnede olup bir sahnede yok olması, açılışta turuncu güneşe dönüşmesi gibi S4 hataları için her çekim promptunda gökyüzü çapa cümlesi (`Reference Sky`) korunmalıdır.
