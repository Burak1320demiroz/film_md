# 🎭 THE_FALSE_SUN — Sahneleme

> Tek sabit kamera kokpit sahnelemesi (`ODA/SAHIP_PLANI.md` §2 ve §9 kaynaklı).
> Bütün film aynı konum, aynı lens ve aynı sabit kadrajda akar.
> Flow'un iki anahtar kareli B zinciri yerine Gemini Omni 1.1 Flash sahne uzatma / son kareden devam yöntemi
> ve gerektiğinde GPT Image onarım karesi kullanılır.

---

## 1. ZİNCİRLER

| Zincir | Çekimler | Halka | Yöntem | Neden zincir (kesintisizlik ne anlatıyor) |
|:--:|---|:--:|:--:|---|

> Not: Flow B zinciri kurulmamıştır. Bütün film tek kamerada sahne uzatma / son kareden devam ile akar (aşağıda §5).

## 2. ANAHTAR KARELER

| Kare | Zincir | Poz / konum | Kamera | Işık | Nesne durumu | Kaynak | Dosya (`kare/`) |
|:--:|:--:|---|---|---|---|---|---|
| Master | — | Nia sol üçte birde koltukta; sağ el gümüş reaktör kolunda ON, sol el turuncu yem kolunda dik | 28mm sabit göz hizası, sol duvara cıvatalı | Mavi gölgeler, acil camgöbeği, amber küre ışığı | Reaktör ON, yem kolu dik, yem dışarıda YOK | ref/1.NIA · ref/2.KOKPIT · ref/3.KURE_VE_YEM | `Master.png` |

## 3. MEKÂN HARİTASI

```
        +-------------------------------------------------------+
        |                    ÖN CAM (KANOPİ)                    |
        |  [Gerçek Beyaz Güneş]             [Amber Sahte Güneş] |
        |  (sol üst, sabit)                 (sağ üst, yaklaşır) |
        |                                                       |
        |        | Dikme 1 |                 | Dikme 2 |        |
        |                                                       |
        |          [Mavi-gri Gaz Devi Kavisi (altta sabit)]     |
        +-------------------------------------------------------+
                    \                               /
                     \       ALÇAK GRAFİT KONSOL   /
                      +---------------------------+
                      | [Turuncu Kol] [Gümüş Kol] |
                      | (sol el)      (sağ el)    |
                      +---------------------------+
                     /                             \
                    /    [Pilot Koltuğu: Nia]       \
                   /     (sol üçte birlik alan)      \
  [KAMERA] =======+
  (sol duvarda
   sabit 28mm)
```

| Öğe | Konum / Kadraj Alanı | Rol / Durum |
|---|---|---|
| Kamera (C01–C12) | Kokpit sol duvarına cıvatalı, koltuğun biraz önünde | 28mm sabit göz hizası, derin odak, hareket/zoom YOK |
| Pilot (Nia Ward) | Kadrajın sol üçte birlik alanı | Koltukta oturur, ayağa kalkmaz, kapalı şeffaf vizör |
| Konsol | Kadrajın alt üçte biri | İki büyük kontrol kolu görünür |
| Reaktör kolu | Pilotun sağ elinde, kısa düz ray | C01–C02: ON (ileri) · C03'ten sonra: OFF (geri) |
| Yem kolu | Pilotun sol elinde, sabit menteşe | C01–C06: DİK · C07'den sonra: AŞAĞI |
| Gerçek güneş | Ön camın sol üst köşesi | Küçük beyaz ışık; 12 çekim boyunca aynı yerde sabit |
| Gaz devi gezegen | Ön camın alt bölümü | Kavisli mavi-gri gezegen çizgisi; görüşü korunur |
| Amber küre | Ön camın sağ üst bölümü | C01–C07 yaklaşır; C08–C09 yeme döner; C10–C12 uzaklaşır |
| Yem kapsülü | Ön camın sağ altından dışarı çıkar | C08'de belirir; C09–C11 sağ üste uçar; C12'de kadraj dışı |

## 4. DELTA KONTROLÜ — durum değişimleri

| Çekim | Başlangıç Durumu | Tek Ana Hareket | Bitiş Durumu | Kontrol / Durum |
|:--:|---|---|---|---|
| C01 | Reaktör ON, Yem DİK, Küre uzakta | Amber küre yavaşça yaklaşmaya başlar | Küre biraz daha yakın | Kamera kilitli, pilot yerinde |
| C02 | Küre yakın, kollar yerinde | Nia kaskını sağ üstteki küreye çevirir | Bakış kürede | İki el kumandalarda |
| C03 | Reaktör ON, kask küreye dönük | Sağ el gümüş kolu OFF durağına çeker | Reaktör OFF, ışıklar camgöbeği | El kolda kalır, uğultu söner |
| C04 | Reaktör OFF, loş camgöbeği | Amber küre yaklaşmayı sürdürür ve büyür | Küre camda büyük, yansıma parlak | Pilot hareketsiz, kamera sabit |
| C05 | Küre büyük, reaktör OFF | Nia bakışını küre ile konsol arasında gezdirir | Bakış konsolda | Kolların durumu değişmez |
| C06 | Nia konsola bakıyor | Nia bakışını turuncu kola indirip cama döner | Bakış ön camda | Turuncu kol dik, hazır lambası açık |
| C07 | Turuncu kol dik | Nia sol elindeki turuncu kolu aşağı indirir | Yem kolu AŞAĞI | El kolda kalır; fırlatıcı kadraj dışı |
| C08 | Yem kolu AŞAĞI, küre büyük | Mavi-beyaz kapsül sağ alttan dışarıda belirir | Kapsül sağ üste ilerler | Gemi içinde nesne yok |
| C09 | Kapsül sağ üst rotada | Amber küre yanal hareketle yeme doğru döner | Küre yem rotasına oturur | İki nesne ayrı, birleşmez |
| C10 | Küre kapsülün peşinde | İki nesne sağ üste doğru uzaklaşır | İki nesne küçülür | Beyaz güneş ve gezegen sabit |
| C11 | Nesneler sağ üst kenarda küçük | İki nesne kenara yaklaşır; Nia omuzlarını indirir | Gerilim hafifler | Reaktör kapalı kalır |
| C12 | Nesneler kenara teğet | Küre ve yem camın sağ üst kenarından çıkar | Yalnız gerçek güneş kalır | Temiz nefes; strateji tamamlanır |

## 5. ZİNCİR DIŞI ÇEKİMLER

| Çekim | Neden geleneksel Flow zinciri değil |
|:--:|---|
| C01–C12 | Bütün film tek bir kokpit kamerasında, tek mekânda ve tek açıda geçer. Flow'un iki anahtar kareli B zinciri yerine Gemini'de önceki klibin son karesinden devam / sahne uzatma yöntemi kullanılır. Gerekirse her klip için hazırlanan GPT Image onarım karesi uygulanır. Bu sayede Flow zincir kısıtlamalarına takılmadan tam kadraj sürekliliği korunur. |
