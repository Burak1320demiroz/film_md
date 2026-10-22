# F4 · ses-tasarımcısı · tur 1 — DEAD_LAST

```
GİRDİ    DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md ("Ses, kamera ve ritim" · 48 klip tablosu · C01-C06 "Kurgu notu" satırları · "İlk 10, 30 ve 60 saniye" ·
         ortak hareket cümlesi "Sound and clean dialogue may be added in editing") · FILM.md §3 (devamlılık) · §4 (çekim listesi hazır; sahneleme/AÇILIŞ tablosu) ·
         §5 (50 replik) · §6 (sahne tablosu plandan) · GECIS_VE_SES_SUREKLILIGI.md · ILK_30_SANIYE_KILAVUZU §5
KURAL    Sahip varsayılanı: plandan dışarı çıkılmaz. Her çekimin efekti, planın o satırında görülen/yazılan olaydır (hücre kilidi, kanat kopması, motor arızası,
         dron atışı, kapak, kilit çemberleri…). Planda olmayan hiçbir ses olayı uygulanmadı; öneriler "PLAN DIŞI ÖNERİ" listesinde (uygulanmaz).
         Model sesi KAPALI: videonun sesi atılır; replik + efekt + ortam + müzik kurguda (plan: "Dialogue is the assigned performance text, not a claim that the
         selected video model produces audio"). Flow ayarı: "Return silent videos" AÇIK.
ÇIKTI    ORTAM satırı · seviye çerçevesi · ses motifleri · SAHNE TABLOSU (48) · ORTAM YATAĞI (6) · GEÇİŞ (47 kesme) · SES PROFİLLERİ · KAYIT LİSTESİ (50) ·
         §5 DÜZELTMELERİ · EFEKT LİSTESİ (48/48) · final miks hedefi · besteci notu · PLAN DIŞI ÖNERİ · açık noktalar
```

## ORTAM

```
ORTAM   Yörünge yarış arenası; kadro uzaylı, kask yok. Plan: "Uzay dış planlarının sesleri sinemasal ses tasarımıdır; gerçek boşluk akustiği diye sunulmaz"
        ve FIZIK_IDDIASI yok → vakum kuralı yerine plan geçerli: dış geniş planlar sinemasal ses taşır (üç sektörün işitsel kimliği), ama PATLAMA SESİ YOK
        (plan: "Büyük patlama sesini sürekli yükselterek Axi'nin cümlesini örtme"; C42: "Bütün arena veya gezegenler patlamaz"). Dış plan sesleri aracın gövdesinden/kokpit
        camından duyulur gibi işlenir: alçak-orta ağırlıklı, tizler kısık, kuru; yarış hızı yüksek ses basıncından değil, perde ve yankıdan gelir.
        Kokpit ve römorkör kabini = basınçlı iç hacim: hava ses taşır, yakın, kuru; yatak ritimsiz uğultu. Kalp atışı gibi düzenli ritim YATAĞA GİRMEZ
        (ritim yalnız müzikten gelir). İç planlarda (kokpit/kabin yüz portreleri) yatak aynı dosyadan alçak-geçiren süzgeçle kısılır (~2,5 kHz, −3 dB): dış-iç sürekliliği.
        Üç sektörün işitsel kimliği (plan): KÖKLER = tok geçiş ve motor yankıları (Y3) · ASILI OKYANUS = basınçlı su ve boğuk uğultu (Y4) ·
        METAL FIRTINASI = küçük metal geçişleri ve keskin yakın sürtünmeler (Y5). Altı yatağın hepsi AYNI alçak taban drone'u (ortak temel perde) üzerine kurulur:
        sektör değişiminde taban sürer, yalnız üst doku değişir (Y→Y çaprazı kulakta kopma yaratmaz).
        Telsiz: kayıtta motor/ortam gürültüsü YOK (mikrofon kabinde); bant geçiren ~300-3400 Hz, hafif bozulma, başta ve sonda squelch tıkı.
        Sessizlik yalnız planlı üç yerde, hiçbiri dijital sıfır değil (−30 LUFS altı yok):
          1) C02 0,0-1,2 s "düşük frekans boşluğu" (plan C02 Kurgu notu: "Müzik yerine ilk anda kısa bir düşük frekans boşluğu bırak");
          2) C42 ≈6,5 s: iki besleme drone'u keskin ve KALICI kesilir (güç kesildi; bir daha dönmez; zafer bu eksiklikle duyulur);
          3) C46 0,0-2,5 s: tribünde "suskunluk" (plan: "suskunluk sonrası ayağa kalkar"), Y6 −26'ya iner.
MODEL SESİ  KAPALI → mekân başına "ortam ses cümlesi" yazılmaz (film_dogrula konuşma/ses tarifini hata sayar). goruntu-yonetmeni video promptlarına ses cümlesi eklemez.
```

## Ses seviyesi çerçevesi (kısa-dönem LUFS; final −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumlu)

```
replik          −15…−16 (telsiz −16, kokpit/oda −15)        yatak (replik yokken) −18…−22          yatak (replik altında) −21…−23
efekt zemin     −20…−26                                      efekt vurgu (planın "belirgin" olayları) −10…−16
müzik yatağı    −16…−18 (replik yokken) · replik altında −6…−9 dB · C01'de YOK (ILK_30 §5) · C02'de boşluktan sonra çok düşük zemin
Dinamik aralık korunur: C42 aşırı yük darbesi (≈ −10) ile C43-C47 sakinliği (−24…−30) arasındaki fark ezilmez. Kalibrasyon: kurgu.py yukseklik <taslak> --uygula.
Stereo: telsiz ve replik merkez (mono güvenli). C37-C42'de Raka SOL (amber, alçak-sıcak), Thren SAĞ (camgöbeği, yüksek-soğuk) — arkadan bakan kamera yönü (plan). C41'de çift sol/sağ simetri mono toplamda da eşit seviyede kalır.
```

## Ses motifleri (aynı örnek, farklı yerlerde; süreklilik)

| Motif | Örnek | Geçtiği çekimler |
|---|---|---|
| KLİK ailesi | ışık-sönme tıkı (kısa, temiz elektrik) ve hücre kilidi kliği (tok, metalik); aynı örnek ailesi, ikincisi daha ağır | C02 sonu → C03 (plan: "şehir ışıklarının sönmesi ve sonraki hücre kilidinin klik sesi birbirine bağlanabilir") |
| KANAT | sağ fren kanadı açılışı: kısa hidrolik tıslama + metalik kilit + hava freni sürüklenmesi | C12 ve C40 (plan: "C12'de kurulan sağ fren hareketi") — AYNI örnek |
| AKIŞ İZİ | pürüzsüz, kararlı elektromanyetik parıltı vınlaması | C16 · C23 · C31 · C44 (plan: C16 gösterilir, C23 planlanır, C31 ve C44'te yeniden kullanılır) |
| BESLEME | iki paralel besleme drone'u: sol sıcak-alçak (amber), sağ yüksek-soğuk (camgöbeği) | C19 · C37-C42 (C42'de ölür, geri gelmez) |
| TELSİZ | squelch açılış/kapanış tıkı + bant geçiren süzgeç | 29 telsiz repliği |
| TEK MOTOR | arızalı Fang'in düzensiz vınlaması (sağ arka kapalı) | C14 → C21 · C39 (hasar C14'ten C48'e sürer) |
| İKİ MOTOR | Bastion'un üç motorlu homurtusunun iki motorluya düşmüş hâli | C29 → C35 · C44 |

## SAHNE TABLOSU (FILM §6 biçimi, köprüler dolu)

Katmanlar ≤4: ortam · efekt · replik · müzik. Yatak adları: Y1 eski yarış/yörünge · Y2 hazırlık alanı · Y3 kökler · Y4 asılı okyanus · Y5 metal fırtınası/hasat kapısı · Y6 tribün.
Müzik hücrelerinde yalnız plan kelimesi ("Ortam ve müzik" = replik yok, müzik önde) ve ILK_30 kuralı yazıldı; notalar besteci F8'dedir. Replik altında müzik −6…−9 dB.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | ortam Y1 · efekt: Axi'nin küçük nefesi + çatlağın çok alçak gerilme sesi (ilk 2 s'de, patlama değil) · replik R01 (2,2 s'den) · müzik YOK | C01→C02: Y1 kesintisiz; gerilme sesi L 0,5 s | M01 yörünge · ilk 2 s insan sesi yok (ILK_30) · PREVIOUS RACE yazısı ses taşımaz |
| S2 (C02) | Y1 · efekt: 0,0-1,2 s düşük frekans boşluğu, sonra mavi enerji süzülmesi, ≈9,3 s ışık-sönme tıkı · replik R02 (makine, 3,0 s) · müzik: boşluktan sonra çok düşük zemin | C02→C03: Y1→Y2 çapraz 1,5 s; tık kuyruğu L 0,8 s | M01 yörünge · planlı sessizlik 1 |
| S3 (C03) | Y2 · efekt: eldivenli ellerin hücreyi indirişi, ≈4,2 s hücre kilidi kliği · replik R03 (telsiz) · müzik: zemin yükselir | C03→C04: Y2 sürer; kilit kuyruğu L 0,5 s | M02 hazırlık alanı · klik = C02 tıkının ağır akrabası |
| S4 (C04) | Y2 · efekt: kokpit nefes/kumaş, römorkör rölantisi · replik R04 (kokpit), R05 (telsiz) · müzik: replik altında | C04→C05: Y2 sürer; yayın uğultusu J 1,0 s | M02 hazırlık alanı |
| S5 (C05) | Y2 · efekt: beş şerit ışığı tıkları, uzak kalabalık dokusu · replik R06 (yayın) · müzik: sunucu altında seyrek | C05→C06: Y2 sürer; son tık L 0,5 s, kalabalık L 0,8 s'de kısılır | M02 hazırlık alanı · kalabalık = planın "ortam sesinden" |
| S6 (C06) | Y2 · efekt: kemer sıkılışı (≈0,7 s), kalkış titreşimi (6-10 s) · replik R07 (kokpit), R08 (telsiz) · müzik: sürer | C06→C07: Y2→Y3 çapraz 1,0 s; titreşim C07'ye J 1,5 s ile yükselir | M02 hazırlık alanı · bölüm 1 sonu |
| S7 (C07) | Y3 · efekt: beş aracın ateşlemesi ve fırlayışı, kök kemeri altı motor yankıları · müzik önde (plan: "Ortam ve müzik") | C07→C08: Y3 sürer; motor yankısı L 0,8 s | M03 kökler · replik yok · "tam birinci dakikada" |
| S8 (C08) | Y3 · efekt: yan camda Needle motoru, tok kök geçişi · replik R09 (kokpit), R10 (telsiz) · müzik: replik altında | C08→C09: Y3 sürer; yan motor drone'u L 0,5 s | M03 kökler |
| S9 (C09) | Y3 · efekt: kök boğazında sıkışan yankı, Fang'in içeri kapanışı · replik R11, R12 (telsiz) · müzik: sürer | C09→C10: Y3 sürer; motor perdesi sapması J 0,5 s | M03 kökler |
| S10 (C10) | Y3 · efekt: ≈4,0 s metal-metal sürtünme ve kanat ucunun kopması, savrulan parça, gövde gerilmesi · müzik önde | C10→C11: Y3 sürer; gövde gerilmesi L 1,0 s | M03 kökler · replik yok · planın ilk hasarı |
| S11 (C11) | Y3 · efekt: yana yatma gerilimi, kemer gıcırtısı, eğilen kökler, efor nefesi · replik R13 (telsiz), R14 (kokpit) · müzik: replik altında | C11→C12: Y3 sürer; gerilme gıcırtısı L 1,0 s (C12'de kanat sesiyle çözülür) | M03 kökler |
| S12 (C12) | Y3 · efekt: ≈3,5 s sağ fren kanadı (KANAT motifi), gerilmenin çözülüşü · müzik önde | C12→C13: Y3→Y4 çapraz 1,5 s (Y4 J 1,5 s) | M03 kökler · replik yok · bölüm 2 sonu |
| S13 (C13) | Y4 · efekt: asılı okyanus, yukarıda kırılan dalgalar (≈3,0 ve ≈7,5 s), su altı motor yankısı · müzik önde | C13→C14: Y4 sürer; dalga kuyruğu L 1,0 s, buhar J 0,8 s | M04 okyanus · replik yok |
| S14 (C14) | Y4 · efekt: buhar süpürmesi, motorun öksürüp sönmesi ve tek kıvılcım, TEK MOTOR vınlaması · replik R15, R16 (telsiz) · müzik: replik altında | C14→C15: Y4 sürer; arızalı motor L 0,8 s | M04 okyanus |
| S15 (C15) | Y4 · efekt: Fang'in yalpalayan motoru, Raka'nın kısa nefesi · replik R17 (kokpit), R18 (telsiz), R19 (kokpit) · müzik: replik altında | C15→C16: Y4 sürer; Fang vınlaması L 0,8 s, Needle motoru J 0,8 s | M04 okyanus |
| S16 (C16) | Y4 · efekt: Needle'ın öne süzülüşü, AKIŞ İZİ vınlaması, Fang'in dengelenişi · müzik önde | C16→C17: Y4 sürer; akış izi L 1,5 s | M04 okyanus · replik yok · pilot çekim |
| S17 (C17) | Y4 · efekt: Thren'in ağır nefesi, dengelenmiş Fang motoru (iz altında) · replik R20 (kokpit), R21 (telsiz) · müzik: replik altında | C17→C18: Y4→Y5 çapraz 1,5 s; Axi squelch tıkı J 0,8 s | M04 okyanus · bölüm 3 sonu |
| S18 (C18) | Y5 · efekt: römorkörün ağır itişi, kapı altı metal sürtünmeleri · replik R22 (telsiz) · müzik: replik altında | C18→C19: Y5 sürer; itiş L 1,0 s, besleme drone'u J 1,0 s | M05 kapı altı |
| S19 (C19) | Y5 · efekt: iki paralel besleme drone'u (BESLEME) · replik R23 (telsiz) · müzik: replik altında | C19→C20: Y5 sürer; drone L 1,0 s (kabin içinde kısık) | M05 kapı altı |
| S20 (C20) | Y5 · efekt: römorkör kabini röle tıkları · replik R24 (kabin, 4,5 s'den) · müzik: replik altında | C20→C21: Y5→Y4 çapraz 1,0 s (ortak taban); Fang vınlaması J 0,8 s | M05 kapı altı |
| S21 (C21) | Y4 · efekt: arızalı motor vınlaması (kokpit içi), Thren'in gergin nefesi · replik R25 (kokpit), R26 (telsiz) · müzik: replik altında | C21→C22: Y4 sürer; vınlama L 0,5 s | M04 okyanus |
| S22 (C22) | Y4 · efekt: hücre enerjisinin perde olarak alçalıp sönmesi · replik R27 (kokpit), R28 (telsiz) · müzik: replik altında | C22→C23: Y4 sürer; alçalan ton L 0,8 s, Halo motoru J 1,0 s | M04 okyanus |
| S23 (C23) | Y4 · efekt: ≈0,6 s kanal-açık tıkı, Halo merkez motoru, AKIŞ İZİ (kısık, 5-10 s) · replik R29 (kokpit) · müzik: replik altında | C23→C24: Y4 sürer; kanal tıkı J 0,3 s | M04 okyanus |
| S24 (C24) | Y4 · efekt: ≈0,7 s ortak kanalın açılışı, kokpit nefesi · replik R30 (kokpit) · müzik: replik altında | C24→C25: Y4 sürer; taşıyıcı hışırtı L 0,8 s | M04 okyanus · bölüm 4 sonu |
| S25 (C25) | Y4 · efekt: Sickle ince tek motor vınlaması, yatış süpürmesi · replik R31 (kokpit) · müzik: replik altında | C25→C26: Y4 sürer; yatış L 0,5 s, Bastion homurtusu J 1,0 s | M04 okyanus |
| S26 (C26) | Y4 · efekt: Bastion üç motorlu homurtu, Korv'un ağır soluğu · replik R32 (kokpit) · müzik: replik altında | C26→C27: Y4→Y6 çapraz 1,0 s; yayın uğultusu J 1,0 s | M04 okyanus |
| S27 (C27) | Y6 · efekt: ≈0,5 s Kalix'in parmakları korkuluğa değer · replik R33 (balkon) · müzik: replik altında | C27→C28: Y6→Y4 çapraz 1,0 s; Bastion yanal itişi J 1,0 s | M06 balkon · kalabalık = Y6 (plan) |
| S28 (C28) | Y4 · efekt: Bastion'un yanal kayışı, takip dronları vınlaması · replik R34 (telsiz) · müzik: replik altında | C28→C29: Y4 sürer; dron vınlaması L 0,8 s | M04 okyanus |
| S29 (C29) | Y4 · efekt: ≈3,0 s dron atışı, ≈3,2 s motor vuruşu, üç motordan iki motora düşüş (İKİ MOTOR) · müzik önde | C29→C30: Y4→Y5 çapraz 1,0 s; dron vınlaması L 1,2 s Y5'e taşar | M04 okyanus · replik yok |
| S30 (C30) | Y5 · efekt: Sickle'ın dronların önünden geçişi, metal yaprak şeridine giriş · replik R35 (telsiz) · müzik: replik altında | C30→C31: Y5 sürer; geçiş L 0,8 s, akış izi J 1,0 s | M05 metal fırtınası · bölüm 5 sonu |
| S31 (C31) | Y5 · efekt: AKIŞ İZİ, Sael'in yanması, demir yaprak geçişleri · müzik önde | C31→C32: Y5 sürer; akış izi L 0,8 s (cam parıltısına dönüşür) | M05 metal fırtınası · replik yok |
| S32 (C32) | Y5 · efekt: camdaki mavi iz parıltısı (çok kısık) · replik R36 (kokpit, 4,0 s'den) · müzik: replik altında | C32→C33: Y5 sürer; parıltı L 0,5 s, taşıyıcı J 0,5 s | M05 metal fırtınası · filmin açılışına dönüş |
| S33 (C33) | Y5 · efekt: kabin uğultusu, Axi'nin yavaş nefesi · replik R37 (kabin) · müzik: replik altında | C33→C34: Y5 sürer; kabin hum L 0,5 s, Sickle geçişi J 0,8 s | M05 metal fırtınası |
| S34 (C34) | Y5 · efekt: Sickle ve dron geçişi, iki yaprağın kapanışı (≈5,5 s), dronların düşmesi (≈6,0 s) · replik R38 (telsiz, 6,0 s'den) · müzik: replik altında | C34→C35: Y5 sürer; yaprak gıcırtısı L 1,0 s, Bastion itişi J 1,0 s | M05 metal fırtınası |
| S35 (C35) | Y5 · efekt: Bastion'un burnunu kapağa dayaması, İKİ MOTOR itişi · replik R39 (telsiz) · müzik: replik altında | C35→C36: Y5 sürer; itiş L 1,0 s, servis kolu J 0,5 s | M05 metal fırtınası |
| S36 (C36) | Y5 · efekt: servis kolu, ≈4,0 s kapak kilidi çözülür ve açılma gıcırtısı, çevrim yükselişi · replik R40 (telsiz) · müzik: replik altında | C36→C37: Y5 sürer; çevrim ve kapak gıcırtısı L 1,0 s, BESLEME drone'una dönüşür | M05 metal fırtınası · bölüm 6 sonu |
| S37 (C37) | Y5 · efekt: BESLEME (sol/sağ ayrık), iki aracın iki tünele ayrılışı · müzik önde | C37→C38: Y5 sürer; sol amber besleme J 0,8 s | M05 bakım ağzı içi · replik yok |
| S38 (C38) | Y5 · efekt: dar sol kanal yankısı (sol hoparlör), sol besleme · replik R41 (telsiz, 5,5 s'den) · müzik: replik altında | C38→C39: Y5 sürer; Thren squelch tıkı J 0,5 s | M05 bakım ağzı içi |
| S39 (C39) | Y5 · efekt: TEK MOTOR (sağ hoparlör, dar kanal yankısı), sağ besleme · replik R42 (telsiz) · müzik: replik altında | C39→C40: Y5 sürer; Fang öksürüğü L 0,5 s | M05 bakım ağzı içi |
| S40 (C40) | Y5 · efekt: ≈1,5 s sağ fren kanadı (KANAT, C12 örneği), iki motor perdesinin eşitlenmesi · replik R43 (telsiz) · müzik: replik altında | C40→C41: Y5 sürer; eşit perde (tek ton) L 1,0 s | M05 bakım ağzı içi |
| S41 (C41) | Y5 · efekt: ≈2,0 s çift hücre bırakma (sol/sağ simetrik), düşük güce iniş, iki hücrenin paralel süzülüşü · replik R44 (telsiz, 1,0 s) · müzik: replik altında | C41→C42: Y5 sürer; iki hücre perdeleri kesintisiz | M05 bakım ağzı içi · pilot çekim |
| S42 (C42) | Y5 · efekt: perdeler birleşir, ≈6,5 s aşırı yük darbesi, kilit çöküşü; BESLEME kalıcı kesilir · replik R45 (telsiz) · müzik önde | C42→C43: Y5 sürer; BESLEME YOK (planlı sert kesme); kilit çemberi açılışı J 0,5 s | M05 · planlı sessizlik 2 |
| S43 (C43) | Y5 · efekt: beş kilit çemberinin açılışı, hasat drone'unun sessizliğe inişi · müzik önde | C43→C44: Y5 sürer; son çember kuyruğu L 0,8 s | M05 · replik yok |
| S44 (C44) | Y5 · efekt: kapak basıncı, İKİ MOTOR, AKIŞ İZİ, düşük güçlü manevra motorları · replik R46 (telsiz) · müzik: replik altında | C44→C45: Y5 sürer; akış izi L 0,8 s | M05 |
| S45 (C45) | Y5 · efekt: ≈6,2 s römorkör kelepçesi açılır, ilk itiş · replik R47 (kabin, öneri), R48 (telsiz) · müzik: replik altında | C45→C46: Y5→Y6 çapraz 1,5 s; itici sesleri L 1,0 s | M05 · kamera Axi kokpitinde (plan) |
| S46 (C46) | Y6 · efekt: ayağa kalkış hışırtıları (2,5 s'den), yayın ekranının sönmesi (≈7,0 s) · müzik önde (suskunluktan sonra) | C46→C47: Y6→Y5 çapraz 1,0 s; yayın sönme kuyruğu L 1,0 s | M06 tribün · replik yok · planlı sessizlik 3 |
| S47 (C47) | Y5 · efekt: düşük güçlü Needle kokpiti, Raka'nın uzun nefes verişi · replik R49 (telsiz), R50 (kokpit) · müzik: replik altında | C47→C48: Y5 sürer; kokpit hum L 1,0 s, altı araç uğultusu J 1,0 s | M05 |
| S48 (C48) | Y5 · efekt: altı aracın birlikte uzaklaşması, uzun yumuşak sönme · müzik önde | Film sonu: Y5, efekt ve müzik son 1,5 s'de −40 LUFS'a iner (DEAD LAST yazısı sessiz); dijital sıfır yok | M05 · replik yok · süreye ek kart yok |

Katman sayımı: replikli sahnelerin çoğu 4 katman (ortam+efekt+replik+müzik); hiçbiri 4'ü aşmaz. S1'de müzik yok (3 katman). Çaprazlardaki iki yatak tek ortam katmanı sayılır.

## ORTAM YATAĞI (FILM §6'ya girecek tablo — mekân başına tek satır)

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | M01 Axi'nin eski dünyası (yörünge) — eski yarış kokpiti ve yörünge | C01-C02 | `deep low continuous drone of a sealed alien cockpit blending into vast empty space, soft air circulation hum, steady, no rhythm, no music, close and dry` | −21 LUFS (replik altında −23; C02 0,0-1,2 s'de −30) | `ses/yatak_eski_yaris.wav` (≥ 45 s) |
| Y2 | M02 hazırlık alanı | C03-C06 | `low steady hum of a large white orbital race dock, soft air handling, faint work-lamp electrical buzz, very distant muffled crowd, no rhythm, no music` | −20 LUFS | `ses/yatak_hazirlik.wav` (≥ 60 s) |
| Y3 | M03 asılı kökler (sektör 1: tok geçiş ve motor yankıları) | C07-C12 | `deep low steady resonance of a vast arena between giant hanging roots, heavy soft engine echoes far away, warm and wide, no rhythm, no music` | −19 LUFS | `ses/yatak_kokler.wav` (≥ 85 s) |
| Y4 | M04 gökteki okyanus (sektör 2: basınçlı su ve boğuk uğultu) | C13-C17 · C21-C26 · C28-C29 (üç aralık, arada Y5/Y6) | `deep pressurized water hum with a muffled low drone, a vast body of water hanging overhead heard through a hull, slow, steady, no rhythm, no music` | −21 LUFS (replik altında −23) | `ses/yatak_okyanus.wav` (≥ 200 s; sonraki aralıklarda dosyanın ilerleyen kısmı okunur, kesintisiz süren yatak hissi) |
| Y5 | M05 metal fırtınası ve hasat kapısı (sektör 3: küçük metal geçişleri ve keskin yakın sürtünmeler) | C18-C20 · C30-C45 · C47-C48 (üç aralık, arada Y4/Y6) | `fine steady shimmer of countless thin iron leaves drifting in a magnetic field, a low metallic hum with sharp thin edges, steady, no rhythm, no music` | −20 LUFS (replik altında −22; C44 sonrası −22) | `ses/yatak_hasat_kapisi.wav` (≥ 250 s) |
| Y6 | M06 uzaylı tribünü ve gözlemci balkonu | C27 · C46 | `large open stadium hall air with a vast quiet crowd of many alien species murmuring softly, rustles and low non-verbal hums, no words, no cheering, no rhythm, no music` | −22 LUFS (C46 0,0-2,5 s'de −26) | `ses/yatak_tribun.wav` (≥ 45 s) |

Notlar:
- Altı yatak aynı alçak taban drone'unu (ortak temel perde) taşır; üretimde önce taban, sonra her mekânın üst dokusu. Y→Y çaprazında taban sürer, kesme "oda değişimi" gibi duyulmaz.
- Y4 ve Y5 birer mekân sayıldı ama klip sırasında bölünüyor (C18-C20 arası, C26-C29 arası). Plan sektör kimliğini ve FILM §4 mekân sütununu izler; bu bölünme GEÇİŞ'te çaprazlarla (1,0-1,5 s) taşındı.
- Y3-Y5'te DÜZENLİ ritim yoktur. "Tok geçiş", "küçük metal geçişleri" yataktan değil, EFEKT LİSTESİ'nde ayrık olay olarak girer.
- İç plan (kokpit/kabin) çekimlerinde yatak alçak-geçiren süzgeçle kısılır; aynı dosya, ayrı yatak yazılmaz.

## GEÇİŞ (FILM §6'ya girecek tablo — 47 kesme · F8'de kurgucu kesinleştirir)

Dağılım: kesme 44 · karışım 3 (47'nin dörtte birinden az; toplam −1,7 s) · karartma 0 (planda siyah ekranla ayrılacak büyük zaman atlaması yok; ILK_30 ilk 30 s'de siyah ekran istemez). Her çaprazda iki yatak tek ortam katmanıdır.
Dikiş ölçümü (`kareler.py dikis`) F8'de her kesmede; aynı ölçek/aynı açı ikilileri için bayrak "C30→C31" (iki geniş plan art arda; ses köprüsü akış izidir) ve "C47→C48" (kokpit → geniş, ölçek farkı yeterli).

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz; C01 çatlak gerilimi L 0,5 s sönerken Y1 −30'a iner (plan: C02 0,0-1,2 s düşük frekans boşluğu); müzik yok | aynı dünya; kokpit içi yakın → yörünge geniş, felaketin sürmesi |
| C02→C03 | kesme | Y1→Y2 çapraz 1,5 s (Y2 J 1,0 s); C02 ≈9,3 s ışık-sönme tıkı ↔ C03 ≈4,2 s hücre kilidi kliği (KLİK ailesi); tık kuyruğu L 0,8 s | plan: ışıkların sönmesi ile kilit kliği birbirine bağlanır; önceki yarış → sıradaki yarış; siyah ekran yok |
| C03→C04 | kesme | Y2 sürer; eldiven/kilit kuyruğu L 0,5 s | aynı hazırlık alanı; sırt ve eller → Raka kokpit yakın, ölçek farkı |
| C04→C05 | kesme | Y2 sürer; yayın uğultusu ve uzak kalabalık dokusu J 1,0 s | kokpit → Kalix yayın portresi; yayın sesi önden girer |
| C05→C06 | kesme | Y2 sürer; son şerit ışığı tıkı L 0,5 s; kalabalık dokusu L 0,8 s'de kısılır | yayın → Raka kemer; ses yayın odasından kokpit yakınlığına geçer |
| C06→C07 | kesme | Y2→Y3 çapraz 1,0 s; kalkış titreşimi C07 0,0 s ateşleme darbesine J 1,5 s ile yükselir; müzik kesintisiz yükselir | bölüm 1→2, "tam birinci dakikada beş araç fırlıyor"; titreşim → fırlayış hareket üstünde; sert yatak kesmesi yok |
| C07→C08 | kesme | Y3 sürer; motor yankısı L 0,8 s; Fang kokpit uğultusu J 0,5 s | geniş fırlayış → Thren yakın; aynı yön akışı |
| C08→C09 | kesme | Y3 sürer; yan motor drone'u L 0,5 s; boğaz yankısı sıkışması J 1,0 s | yan yana → dar geçit; ölçek değişir |
| C09→C10 | kesme | Y3 sürer; motor perdesi sapması J 0,5 s | Thren çizgiyi kapatır → temas; darbe C10 içindedir (≈4,0 s), kesmeye düşmez |
| C10→C11 | kesme | Y3 sürer; gövde gerilmesi L 1,0 s; kemer gıcırtısı J 0,5 s | geniş hasar → Raka kokpit; neden-sonuç |
| C11→C12 | kesme | Y3 sürer; gerilme gıcırtısı L 1,0 s, C12 kanat sesiyle çözülür | kokpit → dış; tek düzeltme hareketi |
| C12→C13 | karisim 0,6 | Y3→Y4 çapraz 1,5 s (Y4 J 1,5 s: su basıncı uğultusu C12'nin son saniyesinde başlar; Y3 L 1,5 s su altına geçer) | bölüm 2→3, kök sektöründen okyanus altına; bakır-yeşil → koyu turkuaz renk/ışık sıçraması yumuşatılır |
| C13→C14 | kesme | Y4 sürer; dalga kuyruğu L 1,0 s; buhar J 0,8 s | geniş → Thren motoru, aynı sektör |
| C14→C15 | kesme | Y4 sürer; arızalı motor vınlaması L 0,8 s (C15'te yalpalayan Fang sesine bağlanır) | motor arızası → Raka'nın tepkisi; Fang'in sesi kesmeyi köprüler |
| C15→C16 | kesme | Y4 sürer; Fang vınlaması L 0,8 s; Needle motoru yükselişi J 0,8 s | karar → eylem; Needle öne geçer |
| C16→C17 | kesme | Y4 sürer; AKIŞ İZİ L 1,5 s (C17'de Fang'in dengelenmiş motoru altında kalır) | iz içinde dengelenme → Thren yakın |
| C17→C18 | karisim 0,5 | Y4→Y5 çapraz 1,5 s; Axi squelch tıkı J 0,8 s + Y5 metal dokusu J 1,0 s | bölüm 3 sonu; okyanus → kapı altı bakım güzergâhı, mekân ve ışık sıçraması yumuşatılır |
| C18→C19 | kesme | Y5 sürer; römorkör itişi L 1,0 s; BESLEME drone'u J 1,0 s | aynı mekân (kapı altı); römorkör → kontrol yapısı |
| C19→C20 | kesme | Y5 sürer; BESLEME L 1,0 s (kabin içinde kısık) | yapı geniş → Axi kabini; şema |
| C20→C21 | kesme | Y5→Y4 çapraz 1,0 s (ortak taban); Fang vınlaması J 0,8 s | diyalog sürekliliği Axi → Thren; mekân yatağı değişir, taban aynı |
| C21→C22 | kesme | Y4 sürer; vınlama L 0,5 s; hücre perde alçalışı J 0,5 s | Thren → Raka, paralel kokpitler |
| C22→C23 | kesme | Y4 sürer; alçalan hücre tonu L 0,8 s; Halo motoru J 1,0 s | Raka'nın kuru hücresi → Sael'in "Save your last burn" |
| C23→C24 | kesme | Y4 sürer; kanal-açık tıkı J 0,3 s; Halo motoru L 0,5 s | Sael → Raka ortak kanal |
| C24→C25 | kesme | Y4 sürer; taşıyıcı hışırtı L 0,8 s; Sickle vınlaması J 0,8 s | bölüm 4→5; karar → Veli'nin cevabı |
| C25→C26 | kesme | Y4 sürer; yatış süpürmesi L 0,5 s; Bastion homurtusu J 1,0 s | Veli → Korv; ölçek/renk farkı |
| C26→C27 | kesme | Y4→Y6 çapraz 1,0 s; yayın uğultusu J 1,0 s; Bastion homurtusu L 0,8 s | Korv'un kaygısı → Kalix teklifi; diyalog sürüyor |
| C27→C28 | kesme | Y6→Y4 çapraz 1,0 s; Bastion yanal itişi J 1,0 s | emir → seçim; hareket üstünde |
| C28→C29 | kesme | Y4 sürer; dron vınlaması L 0,8 s | seçim → bedel; dronlar sürer |
| C29→C30 | kesme | Y4→Y5 çapraz 1,0 s (ortak taban); dron vınlaması L 1,2 s Y5'e taşar | bedel → dronları çekmek; dron sesi köprü |
| C30→C31 | kesme | Y5 sürer; Sickle/dron geçişi L 0,8 s; AKIŞ İZİ J 1,0 s | bölüm 5→6; iki geniş plan art arda (jump cut riski, F8 dikiş ölçümü): ses köprüsü akış izi |
| C31→C32 | kesme | Y5 sürer; AKIŞ İZİ L 0,8 s cam parıltısına dönüşür | geniş → Raka kokpit yakın |
| C32→C33 | kesme | Y5 sürer; cam parıltısı L 0,5 s; kabin taşıyıcı J 0,5 s | Raka'nın sözü → Axi'nin cevabı |
| C33→C34 | kesme | Y5 sürer; kabin hum L 0,5 s; Sickle geçişi J 0,8 s | Axi'nin cevabı → Veli aksiyonu; ölçek |
| C34→C35 | kesme | Y5 sürer; yaprak gıcırtısı L 1,0 s; Bastion itişi J 1,0 s | Veli kurtuldu → Korv kapıyı tutuyor |
| C35→C36 | kesme | Y5 sürer; Bastion itişi L 1,0 s (kapı baskısı); servis kolu J 0,5 s | Korv tutuyor → Axi çevrimi başlatır; neden-sonuç |
| C36→C37 | kesme | Y5 sürer; çevrim yükselişi ve kapak gıcırtısı L 1,0 s BESLEME drone'una dönüşür; müzik kesintisiz | bölüm 6→7; kapak açıldı → ağız içi |
| C37→C38 | kesme | Y5 sürer; sol amber besleme (sol hoparlör) J 0,8 s | iki yol → Raka'nın sol hattı |
| C38→C39 | kesme | Y5 sürer; Thren squelch tıkı J 0,5 s | Raka'nın çağrısı → Thren'in cevabı (R41 → R42) |
| C39→C40 | kesme | Y5 sürer; Fang öksürüğü L 0,5 s; KANAT sesi C40 ≈1,5 s | Thren yetişemiyor → Raka yavaşlar |
| C40→C41 | kesme | Y5 sürer; eşit perde (tek ton) L 1,0 s hücre perdelerine geçer | eşitlenen hız → simetrik bırakma, hareket üstünde |
| C41→C42 | kesme | Y5 sürer; iki hücre perdeleri kesintisiz süzülür | aynı eylemin sürmesi (bırakma → varış) |
| C42→C43 | kesme | Y5 sürer; BESLEME ≈6,5 s'de kalıcı kesilir (planlı sert kesme); kilit çemberi açılışı J 0,5 s | bölüm 7→8; ışıklar söndü → kilitler açılıyor |
| C43→C44 | kesme | Y5 sürer; son çember kuyruğu L 0,8 s | kilitler açık → çıkış |
| C44→C45 | kesme | Y5 sürer; AKIŞ İZİ L 0,8 s | Sael'in izi → Axi'nin ayrılışı |
| C45→C46 | karisim 0,6 | Y5→Y6 çapraz 1,5 s; römorkör itici sesleri L 1,0 s tribün suskunluğuna erir | mekân sıçraması (römorkör → tribün); ışık/renk yumuşatılır |
| C46→C47 | kesme | Y6→Y5 çapraz 1,0 s; yayın sönme kuyruğu L 1,0 s; kokpit nefesi J 0,5 s | tribün → Raka; yarışın bittiği ses sakinliğiyle |
| C47→C48 | kesme | Y5 sürer; kokpit hum L 1,0 s; altı araç uğultusu J 1,0 s | yakın → geniş altı araç |

## SES PROFİLLERİ (plan "Voice" satırları + "Ses, kamera ve ritim" · film boyu aynı tını ve aksan)

- **RAKA-SES**: resolute adult female voice, quick but clear, no cartoon pitch. 16 replik.
- **THREN-SES**: controlled, deep-toned adult male voice, quick but clear, proud restraint. 6 replik.
- **AXI-SES**: calm, tired, thin adult male voice; sorrow held in, never a scream (C01). 15 replik.
- **SAEL-SES**: warm, androgynous adult voice, calm and protective. 2 replik.
- **KORV-SES**: low, hard but intelligible adult voice; anxious strength, not comedy. 3 replik.
- **VELI-SES**: quick, dry-humored adult female voice, light and mischievous. 3 replik.
- **KALIX-SES**: calm, threatening presenter-like adult male voice; ilk yarıda profesyonel sunucu kadar rahat (R06, R08, R33); R45'te aynı tını, kontrol kaybı: tempo yükselir, tonlama kırılır (planın "ilk gerçek kontrol kaybı"). 4 replik.
- **SİSTEM-SES**: flat, neutral synthetic voice, no emotion, no accent. 1 replik.

Dağılım: Raka 16 · Axi 15 · Thren 6 · Kalix 4 · Korv 3 · Veli 3 · Sael 2 · Sistem 1 = 50. Aynı kişi film boyu tek kaynaktan; ses aracı sahibindir, liste araçtan bağımsızdır.

## KAYIT LİSTESİ (FILM §5 · 50 replik)

Kayıt: HUMAN (R02 MACHINE). Hiçbir repliğin sesi klipten alınmaz; ağız kadrajda olanlar da kurguda ayrı kayıttan, klibin ağız hareketine F8'de hizalanır (plan: model sesi varsayılmaz). Filtre: `oda` = kokpit/kabin, yakın ve kuru; `telsiz` = bant geçiren ~300-3400 Hz + squelch tıkı başta/sonda, ortam gürültüsü yok; `makine` = düz yapay ses. "Beden önce, ses sonra": jest repliğin 0,1-0,3 s önünde. Alışveriş gecikmeleri korunur (aynı klipte 0,8 s). Saniye/süre FILM §5 tahminidir (düzeltilenler kalın); F8'de kayıtla kesinleşir.

| No | Metin | Konuşan | Ses profili | Ton | Hedef süre | Filtre | Yerleşeceği çekim + saniye |
|:--:|---|---|---|---|:--:|---|---|
| R01 | Please. My family's still there. | Axi | AXI-SES | yalvaran (bağırmadan) | 2,0 s | oda | C01 · **2,2 s** (FILM §5: 1,0) |
| R02 | Conversion complete. Booster fuel ready. | Sistem | SİSTEM-SES | yansız | 2,0 s | makine (görüntünün üstüne) | C02 · 3,0 s |
| R03 | That's my world in your booster. | Axi | AXI-SES | buruk | 2,5 s | telsiz | C03 · 1,0 s |
| R04 | Why are you still here? | Raka | RAKA-SES | şaşkın | 2,0 s | oda | C04 · 1,0 s |
| R05 | They don't let losers leave. | Axi | AXI-SES | durgun | 2,0 s | telsiz | C04 · 3,8 s |
| R06 | Five racers. Last place feeds the next race. | Kalix | KALIX-SES | rahat | 3,0 s | oda + kısa yayın yankısı | C05 · 1,0 s |
| R07 | Then I won't come last. | Raka | RAKA-SES | kararlı | 2,0 s | oda | C06 · 1,0 s |
| R08 | Everybody says that. | Kalix | KALIX-SES | soğuk | 1,5 s | telsiz | C06 · 3,8 s |
| R09 | Stay behind me. | Thren | THREN-SES | buyurgan | 1,5 s | oda | C08 · 1,0 s |
| R10 | That's the plan you brought? | Raka | RAKA-SES | alaycı | 2,0 s | telsiz | C08 · 3,3 s |
| R11 | Your planet isn't my problem. | Thren | THREN-SES | acımasız | 2,0 s | telsiz | C09 · 1,0 s |
| R12 | It will be if you hit me. | Raka | RAKA-SES | sert | 3,0 s | telsiz | C09 · 3,8 s |
| R13 | If you roll, eject the cell. Don't let it take the ship. | Axi | AXI-SES | ciddi | 4,5 s | telsiz | C11 · 1,0 s |
| R14 | Not yet. | Raka | RAKA-SES | gergin | 1,0 s | oda | C11 · 6,3 s |
| R15 | Outer engine's failing. | Thren | THREN-SES | kontrollü | 1,5 s | telsiz | C14 · 1,0 s |
| R16 | Hold the lower lane. | Raka | RAKA-SES | net | 1,5 s | telsiz | C14 · 3,3 s |
| R17 | I can pass him. | Raka | RAKA-SES | hırslı | 1,5 s | oda | C15 · 1,0 s |
| R18 | Yes. You can. | Axi | AXI-SES | sakin | 1,5 s | telsiz | C15 · 3,3 s |
| R19 | No. He's rolling. | Raka | RAKA-SES | kesin | 1,5 s | oda | C15 · 5,6 s |
| R20 | Why save me? That was your chance. | Thren | THREN-SES | şaşkın | 3,0 s | oda | C17 · 1,0 s |
| R21 | I'm racing you. Not burying you. | Raka | RAKA-SES | dürüst | 2,5 s | telsiz | C17 · 4,8 s |
| R22 | That gate isn't just timing you. Look beneath the finish lights. | Axi | AXI-SES | uyarıcı | 4,0 s | telsiz | C18 · 1,0 s |
| R23 | Crossing the finish arms the harvester. It already has your coordinates. | Axi | AXI-SES | ağır | 4,0 s | telsiz | C19 · 1,0 s |
| R24 | Two feeds. One cell in each. Same pulse. | Axi | AXI-SES | net | 3,0 s | oda | C20 · **4,5 s** (FILM §5: 1,0) |
| R25 | They'll seal before we get clear. | Thren | THREN-SES | gergin | 2,5 s | oda | C21 · 1,0 s |
| R26 | Unless someone holds the outer shutter. | Axi | AXI-SES | sakin | 2,5 s | telsiz | C21 · 4,3 s |
| R27 | Our cells are nearly dry. | Raka | RAKA-SES | endişeli | 2,0 s | oda | C22 · 1,0 s |
| R28 | Enough for the locks. Don't waste another burn. | Axi | AXI-SES | pratik | 3,0 s | telsiz | C22 · 3,8 s |
| R29 | Ride my wake. Save your last burn. I've got the lead. | Sael | SAEL-SES | sıcak | 4,0 s | oda | C23 · 1,0 s |
| R30 | Nobody crosses the line. We end the race. All five worlds stay alive. | Raka | RAKA-SES | kararlı | 5,0 s | oda | C24 · 1,0 s |
| R31 | Tell me where to fly. I'm tired of losing people. | Veli | VELI-SES | yorgun | 4,0 s | oda | C25 · 1,0 s |
| R32 | You'll kill us before he does. My world is waiting for me. | Korv | KORV-SES | tedirgin | 4,5 s | oda | C26 · 1,0 s |
| R33 | Ram the white ship. Your world goes free. Don't make me ask twice. | Kalix | KALIX-SES | tehditkâr | 5,0 s | oda + geniş balkon yankısı | C27 · 1,0 s |
| R34 | Find another executioner. I'm a pilot. | Korv | KORV-SES | dik | 2,5 s | telsiz | C28 · 1,0 s |
| R35 | Keep your eyes on me. I'm the interesting one. | Veli | VELI-SES | oyuncu | 3,5 s | telsiz | C30 · 1,0 s |
| R36 | We're still burning your world. I feel it every time I boost. | Raka | RAKA-SES | ağır | 4,5 s | oda | C32 · **4,0 s** (FILM §5: 1,0) |
| R37 | Then make it the last world they ever burn. Don't waste it. | Axi | AXI-SES | yorgun | 4,5 s | oda | C33 · 1,0 s |
| R38 | You're welcome. Try surviving it. | Veli | VELI-SES | alaycı | 2,0 s | telsiz | C34 · **6,0 s** (FILM §5: 1,0) |
| R39 | Go. I'm holding the door. Don't make me do this twice. | Korv | KORV-SES | sert | 4,0 s | telsiz | C35 · 1,0 s |
| R40 | Purge in ten. Both feeds together. No second attempt. | Axi | AXI-SES | odaklı | 3,5 s | telsiz | C36 · 1,0 s |
| R41 | I'm in position. Thren, where are you? | Raka | RAKA-SES | gergin | 3,0 s | telsiz | C38 · **5,5 s** (FILM §5: 1,0) |
| R42 | Can't match your speed. Outer engine's gone. I won't make the pulse. | Thren | THREN-SES | bastırılmış | 4,5 s | telsiz | C39 · 1,0 s |
| R43 | Then I match yours. Nobody gets left behind this time. | Raka | RAKA-SES | sakin | 4,0 s | telsiz | C40 · 1,0 s |
| R44 | Now. | Axi | AXI-SES | net | 1,0 s | telsiz | C41 · 1,0 s |
| R45 | Stop them! I gave you worlds! | Kalix | KALIX-SES | öfkeli (kontrol kaybı) | 2,5 s | telsiz + hafif kırpma | C42 · 1,0 s |
| R46 | Stay in my wake. All of you. Keep those engines low. | Sael | SAEL-SES | koruyucu | 4,0 s | telsiz | C44 · 1,0 s |
| R47 | Tell me your world is still there. | Axi | AXI-SES | kırılgan | 3,0 s | oda (kabin, ekran dışı; FILM §5 Kaynak: telsiz, aşağıda madde 6) | C45 · 1,0 s |
| R48 | All five. Axi, you're clear. | Raka | RAKA-SES | yumuşak | 2,0 s | telsiz | C45 · 4,8 s |
| R49 | Where do we go? | Axi | AXI-SES | umutlu | 1,5 s | telsiz | C47 · 1,0 s |
| R50 | Somewhere without a finish line. | Raka | RAKA-SES | huzurlu | 2,0 s | oda | C47 · 3,3 s |

Dağılım: oda 21 (R01, R04, R06, R07, R09, R14, R17, R19, R20, R24, R25, R27, R29, R30, R31, R32, R33, R36, R37, R47, R50) · telsiz 28 · makine 1 = 50.

Yerleşim denetimi: ağız kadrajda ≤ 5 s (R30 ve R33 tam 5,0 s, sınırda) · hiçbir replik bir geçiş (karışım) aralığına düşmez (C12→C13, C17→C18, C45→C46 kesmelerine en yakın replik ≥ 2,5 s uzakta) · aynı klipte aralıklar 0,8 s korunur (C04, C06, C08, C09, C11, C14, C15, C17, C21, C22, C45, C47).

## §5 DÜZELTMELERİ (FILM §5'e satır satır; yalnız saniye, metin ve süre aynı)

| No | Çekim | FILM §5 | Yeni | Neden |
|:--:|:--:|:--:|:--:|---|
| R01 | C01 | 1,0 s | **2,2 s** | ILK_30 §5: ilk 2 s insan sesi yok; açılış nefes + çatlak gerilimiyle. Replik 4,2 s'de biter. Risk: ağız kadrajda; videoda Axi'nin ağzı erken açılırsa F8'de kayıt ağız zamanına göre oturur. goruntu-yonetmeni C01 video promptunda ilk vuruşu (0-3 s) çatlağın ve Axi'nin nefesinin vuruşu yapar, ağız hareketini 2-3 s vuruşundan başlatır. |
| R24 | C20 | 1,0 s | **4,5 s** | Plan: Axi "iki enerji hattının basit şemasını işaret eder". Jest önce (işaret 4,1-4,4 s), ses sonra. Thren'in cevabıyla (C21 · 1,0 s) arası 7,0 s'den 3,5 s'ye iner. |
| R36 | C32 | 1,0 s | **4,0 s** | Plan: Raka önce "kabinin camındaki mavi enerji izine bakar" (0-4 s bakış), sonra söyler. Axi'nin cevabı (C33 · 1,0 s) ile arası 5,5 s'den 2,5 s'ye iner; filmin duygusal merkezi (R36→R37) sıkılaşır. |
| R38 | C34 | 1,0 s | **6,0 s** | "You're welcome. Try surviving it." dronlar rotadan düştükten sonra söylenen bir tepkidir; düşüş ≈6,0 s'de (yapraklar kapanır ≈5,5 s). 1,0 s'de söylenirse cümle olaydan önce gelir. goruntu-yonetmeni C34 vuruşunda kapanma/düşüşü 5-6 s'ye koyar. |
| R41 | C38 | 1,0 s | **5,5 s** | "Thren, where are you?" bir çağrıdır; cevap C39 · 1,0 s'de. Arayı 7,0 s'den 2,5 s'ye indirir (replik 8,5 s'de biter). "I'm in position" 5,5 s'de: Needle dar sol kanalda yerleştikten sonra. |

Aralığı değişmeyen ama zamanlaması video vuruşuna bağlı üç not (saniye değişikliği değil):
1. **C41 · R44 "Now." 1,0-2,0 s** — iki hücrenin bırakılışı "Now." sözünden SONRA olmalı (≥ 1,6 s; efekt ≈2,0 s). goruntu-yonetmeni C41 0-3 s vuruşunda bırakmayı 1,6 s'den önce koymaz.
2. **C45 · R47/R48** — kelepçe açılışı ≈6,2 s ("you're clear" sonrası); video vuruşunda 6-7 s.
3. **C42 · R45 1,0-3,5 s** — aşırı yük darbesi ≈6,5 s; hücreler kilitlere varmadan Kalix'in cümlesi biter.
4. **R47 Kaynak.** FILM §5 "telsiz — kadraj dışı" yazıyor; plan C45: "Axi gri servis römorkörünün bağlantı kelepçesini açar; kokpit camından özgür rotaya yönelen araçlar görülür." Kamera Axi'nin kabinindeyse Axi kendi ses odasında konuşur: Kaynak = **kabin (oda), ekran dışı**; yalnız R48 (Raka) telsiz olur. Kamera römorkör dışındaysa R47 telsiz kalır. Karar kamera/vuruş yazılınca (goruntu-yonetmeni) netleşir; kayıt listesinde varsayılan `oda`.

## EFEKT LİSTESİ (her çekim ≥1 satır; 48/48 — sessiz çekim yok)

Kaynak sütunu: **gövde** (yapı/kanat/kilit; temas aracın ya da kabinin içinden duyulur) · **hava** (kabin havası ya da planın sinemasal dış planı; gerçek boşluk akustiği diye sunulmaz) · **kokpit** (kabin içi, yakın ve kuru). Kask yok. "Saniye" tahminidir; olay zamanı klipten F8'de oturur. Seviye = kısa-dönem LUFS. Her satırın temeli planın o satırındaki olay ya da replik dışı yazılan ses kuralıdır.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|---|---|---|
| C01 | 0,0-2,0 | Axi'nin küçük, titrek nefesi (plan: "küçük bir nefes"); açılış sorunu insan sesi olmadan duyurur | kokpit | efekt | −22 | ara: `small shaky inhale breath adult close dry` |
| C01 | 0,0-2,0 | gezegen çatlağının çok alçak gerilme sesi: tek uzun sub-bas gıcırtı, patlama değil; replikten önce | hava | efekt | −18 | üret: `a very low slow groan of a huge structure beginning to split, felt more than heard, muffled through a cockpit window, no explosion, no impact` |
| C01 | 2,0-10 | çatlağın yavaş genişlemesi: aynı gerilme sesi kısık, replik altında | hava | efekt | −30 | aynı örnek, −12 dB kısık, kuyruk uzun |
| C01 | 6,0-9,0 | birkaç şehir ışığı kümesi sönerken çok hafif alçalan elektrik iç çekişi | hava | efekt | −34 | üret: `a faint falling electrical sigh as tiny lights dim, barely audible, soft` |
| C02 | 0,0-1,2 | düşük frekans boşluğu: Y1 −30'a iner, tek derin sub-bas çöküşü, müzik yerine (plan Kurgu notu) | hava | efekt | −24 | üret: `a deep sub-bass drop collapsing into near silence for one second, felt in the chest, no melody, no impact` |
| C02 | 1,2-9,0 | mavi enerjinin halkanın depolarına süzülmesi: akıcı, yükselen elektrik parıltısı | hava | efekt | −22 → −16 | üret: `a smooth continuous rising shimmer of blue energy flowing along filaments into a large reservoir, soft and wide, no explosion, no impact` |
| C02 | ≈9,3 | son şehir ışığı kümelerinin sönmesi: tek kısa elektrik tık-kapanma, KLİK ailesi (C03 kilit kliğinin hafif akrabası) | hava | efekt | −16 | üret: `a single soft electrical power-down tick, short and clean, with a very short falling hum` |
| C03 | 0,0-0,8 | C02 sönme tıkının kuyruğu | hava | efekt | −26 | C02 ışık-sönme tıkının kuyruğu, kısık |
| C03 | 0,5-4,0 | eldivenli ellerin hücreyi kızağın üstüne indirişi: eldiven-metal teması, ağır hücre | hava | efekt | −20 | üret: `gloved hands lowering a heavy energy cell onto a metal cradle, slow, close, dry, leather glove on metal` |
| C03 | ≈4,2 | hücre kilidi: tek net metalik klik + çok kısa elektrik titreşimi (plan: "one clear click"); KLİK ailesi | gövde | efekt | −13 | üret: `a single solid metallic latch click, clean and close, followed by a faint electrical thrum` |
| C03 | 4,5-6,0 | ellerin çekilişi: deri eldiven sürtünmesi | hava | efekt | −28 | ara: `leather glove slide off metal` |
| C04 | 0-10 | Needle kokpitinde Raka'nın nefesi ve kumaş kıpırtısı | kokpit | efekt | −26 | ara: `adult breathing close dry cockpit cloth movement small` |
| C04 | 0-10 | cam arkasında bulanık römorkörün alçak rölanti uğultusu | gövde | efekt | −30 | üret: `a small heavy maintenance tug idling at a distance, low steady thrum heard through a cockpit canopy, no rhythm` |
| C05 | ≈4,0-9,0 | beş yarış şeridi ışığının sırayla yanışı: beş yumuşak, eşit aralıklı elektrik açılma tıkı (plan: "sequentially once") | hava | efekt | −22 | üret: `five soft electrical power-on ticks one after another at even intervals, each slightly higher in pitch, short and clean` |
| C05 | 0-10 | uzak, çok farklı türden seyirci dokusu: kelime yok, alkış yok (plan: kalabalık ortam sesinden) | hava | efekt | −28 | üret: `distant murmur of a vast crowd of many different alien species, soft clicks and low hums, no intelligible words, far away, no cheering` |
| C06 | ≈0,5-0,9 | emniyet kemerinin son sıkılışı: ağ kayış gerilmesi + toka | gövde | efekt | −16 | ara: `harness strap pulled taut buckle tighten cockpit close dry` |
| C06 | 6,0-10 | kalkış titreşiminin yavaşça başlaması: alçak motor ısınma titreşimi, kokpit takırtısı (C07'ye J) | gövde | efekt | −26 → −18 | üret: `a deep engine spool-up vibration felt inside a cockpit, low and gentle at first, slowly rising, faint rattling of fittings` |
| C07 | 0,0-2,0 | beş aracın fırlayışı: ateşleme dalgası, ağır tok geçiş | hava | efekt | −13 | üret: `five alien racing craft launching in a rush along a magnetic ribbon, deep punchy engine ignition and a heavy fast pass, cinematic, no explosion` |
| C07 | 1,0-10 | kök kemerleri altında motor yankıları: uzaklaşan tok geçişler (sektör 1 kimliği) | hava | efekt | −22 | üret: `deep engine echoes under giant hanging roots, distant racing craft passes, low and heavy, no rhythm` |
| C07 | ≈4,0 · ≈8,0 | kök kemerinin yakın geçişi: tok hava süpürmesi, iki kez | hava | efekt | −24 | ara: `deep whoosh pass under large arch heavy low` |
| C08 | 0-10 | yan camda aynı yönde akan Needle'ın alçak sabit motor sesi | gövde | efekt | −24 | üret: `a racing craft gliding alongside, low steady engine drone heard through a cockpit canopy, close and dry` |
| C08 | ≈3,0 · ≈7,0 | dışarıdan iri bir kökün boğuk süpürmesi (tok geçiş) | hava | efekt | −26 | ara: `muffled heavy whoosh of a large object passing outside a cockpit low` |
| C09 | 0-6,0 | iki aracın dar kök boğazına girişi: yankının sıkışması | hava | efekt | −22 | üret: `two racing craft entering a narrow arch, engine echoes tightening and compressing, low heavy` |
| C09 | ≈4,0-6,0 | Fang'in çizgiyi içeri kapatması: motor perdesi yükselerek yanal süpürme | gövde | efekt | −18 | ara: `racing engine pitch rise lateral swerve close pass` |
| C10 | ≈4,0 | Fang'in yan korumasının Needle'ın sol ön fren kanadına vuruşu: ağır metal-metal sürtünme, ince kanat ucunun keskin çatlayıp kopması | gövde | efekt | −11 | üret: `a heavy metal-on-metal scrape followed by the sharp crack of a thin fin tip snapping off, close, hull-borne, dry, no explosion` |
| C10 | ≈4,3-5,5 | kopan parçanın savrulması: küçük metal tıngırtı, uzaklaşır | hava | efekt | −26 | ara: `small metal fragment tumbling away ting spinning` |
| C10 | ≈4,5-8,0 | yan yatan Needle'ın gövde gerilmesi: gıcırtı + takırtı | gövde | efekt | −20 | ara: `stressed metal groan and rattle craft hull yaw` |
| C11 | 0-10 | yana yatma: gövde gerilimi, kemer gıcırtısı, kokpit takırtısı | kokpit | efekt | −20 | üret: `airframe strain creak and rattle inside a cockpit as the craft rolls, harness creaking, tense and steady` |
| C11 | ≈2,0-5,0 · 7,0-9,0 | arka planda eğilen kökler: ağır süpürme | hava | efekt | −26 | ara: `muffled heavy whoosh of a large object passing outside a cockpit low` |
| C11 | 6,0-10 | Raka'nın efor nefesi | kokpit | efekt | −24 | ara: `effortful short breaths adult close` |
| C12 | ≈3,5 | Needle'ın sağlam sağ fren kanadının tek açılışı: kısa hidrolik tıslama, metalik kilit, hava freni sürüklenmesi — KANAT motifi (C40'ta aynı örnek) | gövde | efekt | −14 | üret: `a servo-driven brake fin unfolding with a short hydraulic hiss and a solid metallic lock, followed by a brief air-brake drag whoosh, single, close` |
| C12 | 3,5-7,0 | gerilmenin çözülüşü: gıcırtı sönerek motor sesi dengelenir (düz şeride oturuş) | gövde | efekt | −24 | üret: `stressed metal creaking easing away as an engine note settles into a steady tone` |
| C13 | ≈3,0 · ≈7,5 | havada asılı okyanus: yukarıda kırılan dalgaların boğuk, iri su gürültüsü (sektör 2 kimliği) | hava | efekt | −18 | üret: `a vast body of water hanging overhead, huge muffled waves breaking far above, heavy pressurized water groan, deep and slow, heard through a hull` |
| C13 | 0-10 | okyanus altında motor yankısı | hava | efekt | −24 | üret: `racing engine echoes under a giant water canopy, deep and soft, no rhythm` |
| C14 | 0-5,0 | su kenarından kopan yoğun buhar: hışırtılı sis süpürmesi | hava | efekt | −22 | ara: `dense steam rushing past hiss wash` |
| C14 | ≈1,0-3,2 | Thren'in sağ arka motorunun öksürüp sönmesi + tek kısa kıvılcım çıtırtısı (plan: "tek kısa kıvılcım") | gövde | efekt | −13 | üret: `a racing engine stuttering, coughing and dying with one short electric spark crackle, close, hull-borne, dry` |
| C14 | 3,2-10 | tek motorla dengesiz yalpa: TEK MOTOR vınlaması | hava | efekt | −22 | üret: `a damaged racing craft with one rear engine dead, uneven whining and an occasional sputter` |
| C15 | 0-10 | önde yalpalayan Fang'in düzensiz vınlaması, aralıklı öksürük | hava | efekt | −22 | C14 TEK MOTOR örneği |
| C15 | ≈5,0-5,6 | Raka'nın "No." öncesi kısa keskin nefesi | kokpit | efekt | −26 | ara: `short sharp inhale adult close` |
| C16 | ≈2,0-4,5 | Needle'ın Fang'in önüne süzülüşü: yumuşak yükselen whoosh + mavi manyetik parıltı | gövde | efekt | −16 | üret: `a racing craft sliding smoothly in front of another, soft rising whoosh and a swell of blue magnetic shimmer, close` |
| C16 | 4,0-10 | kararlı mavi akış izi: pürüzsüz, sabit elektromanyetik parıltı vınlaması — AKIŞ İZİ motifi | hava | efekt | −20 | üret: `a smooth steady electromagnetic shimmer hum of a magnetic wake, soft flowing, stable, no rhythm, no melody` |
| C16 | 3,0-6,5 | Fang'in düzensiz vınlamasının izde dengelenmesi | hava | efekt | −22 → −26 | üret: `an uneven engine whine settling into a steady stable tone` |
| C17 | 0-10 | Thren'in kokpitte nefesini toplaması: kontrollü, ağır nefes | kokpit | efekt | −24 | ara: `adult alien labored controlled breathing close in cockpit` |
| C17 | 0-10 | dengelenmiş Fang motoru, iz altında | hava | efekt | −26 | AKIŞ İZİ kısık + C16 dengelenmiş motor |
| C18 | 0-10 | gri römorkörün ağır ağır ilerleyişi: alçak itici uğultusu, çerçeve gıcırtısı | gövde | efekt | −18 | üret: `a heavy slow work tug moving through a metal maintenance corridor, low thruster rumble and creaking frame, close` |
| C18 | ≈3,0 · ≈7,0 | kapı altı metal yüzeylerde keskin yakın sürtünme (sektör 3 kimliği) | gövde | efekt | −26 | ara: `sharp close metal scrape thin pass` |
| C19 | 0-10 | iki paralel enerji beslemesi: sol sıcak-alçak, sağ yüksek-soğuk, sürekli elektrik drone'u — BESLEME motifi | hava | efekt | −24 | üret: `two parallel energy feeds humming steadily, one warm and low, one slightly higher and cooler, continuous electrical drone, no rhythm, no melody` |
| C20 | 0-10 | römorkör kabini: eskimiş kabinde röle tıkları ve alçak elektrik uğultusu | kokpit | efekt | −26 | üret: `a worn small maintenance tug cabin, faint relay ticks and a low electrical hum, close and dry` |
| C21 | 0-10 | Fang kokpitinde arızalı motorun düzensiz vınlaması (TEK MOTOR, kokpit içi) | kokpit | efekt | −24 | üret: `a damaged engine whining unevenly heard through a cockpit canopy, close` |
| C21 | ≈3,0 | Thren'in gergin nefesi | kokpit | efekt | −26 | ara: `short tense exhale adult close` |
| C22 | 0,0-4,0 | hücre ışığı zayıflarken enerji uğultusunun perdesinin alçalıp sönmesi | gövde | efekt | −22 → −32 | üret: `a soft energy hum slowly dropping in pitch and fading as a power cell runs low, close` |
| C22 | 0-10 | Raka'nın kokpiti: sakin nefes ve kumaş | kokpit | efekt | −28 | ara: `adult breathing close dry cockpit cloth movement small` |
| C23 | ≈0,6 | Sael'in iletişime katılışı: kısa kanal-açık tıkı (plan: "iletişime katılır") | hava | efekt | −20 | ara: `short radio channel open click chirp` |
| C23 | 0-10 | Halo'nun merkez motoru: sıcak, düzgün, sabit | gövde | efekt | −22 | üret: `a warm smooth single central engine drone, steady and powerful, heard through a cockpit canopy, close` |
| C23 | 5,0-10 | akış izi (Sael'in planı): AKIŞ İZİ kısık | hava | efekt | −28 | AKIŞ İZİ örneği, kısık |
| C24 | ≈0,7 | Raka'nın ortak kanalı açışı: kanal tıkı + hafif taşıyıcı hışırtı | hava | efekt | −20 | ara: `radio channel open click squelch short` |
| C24 | 0-10 | Raka'nın kokpiti: sakin nefes | kokpit | efekt | −28 | ara: `adult breathing close dry cockpit cloth movement small` |
| C25 | 0-10 | Sickle'ın ince, hızlı tek motor vınlaması; alt rotaya yatış anında yumuşak hava süpürmesi | gövde | efekt | −22 | üret: `a thin fast single-engine whine of a light craft banking smoothly, soft rush of air, heard through a cockpit canopy` |
| C25 | ≈1,0 | Veli'nin yatış anında kemer gıcırtısı | kokpit | efekt | −28 | ara: `harness strap creak small movement close` |
| C26 | 0-10 | Bastion'un üç motorlu alçak homurtusu, perde takırtısı | gövde | efekt | −20 | üret: `a heavy three-engine craft low steady rumble with a faint bulkhead rattle, heard through a cockpit canopy` |
| C26 | ≈6,0 | Korv'un ağır soluğu | kokpit | efekt | −24 | ara: `heavy slow exhale adult close deep` |
| C27 | ≈0,5 | Kalix'in parmaklarını korkuluğa koyuşu: sakin tek temas | gövde | efekt | −24 | üret: `fingertips resting on a smooth metal balcony rail, one quiet touch, close and dry` |
| C28 | ≈2,0-5,0 | Bastion'un Needle ile dronlar arasına yanal kayışı: hava süpürmesi + yükselen alçak motor homurtusu | hava | efekt | −18 | üret: `a heavy craft sliding sideways across a lane, low engine growl rising, strong air displacement` |
| C28 | 0-10 | takip dronları: küçük, hızlı, elektrikli vınlama | hava | efekt | −22 | üret: `small fast pursuit drones whining and buzzing, closing in, electrical whirr` |
| C29 | ≈3,0 | dronun kısa atışı: tek keskin enerji vuruşu | hava | efekt | −14 | üret: `a short sharp energy bolt zap from a small drone, single, clean` |
| C29 | ≈3,2-3,8 | atışın Bastion'un sağ arka motoruna çarpması: çatırtı + elektrik sızlaması | gövde | efekt | −11 | üret: `an energy bolt hitting an engine housing, a crack and electric sizzle, close, hull-borne` |
| C29 | 3,8-10 | üç motorlu homurtunun iki motorlu düzensiz homurtuya düşüşü — İKİ MOTOR | gövde | efekt | −20 | üret: `a heavy three-engine rumble dropping to an uneven two-engine rumble with a faint dying whine` |
| C30 | 0-5,0 | Sickle'ın dronların önünden geçişi: hızlı gümüş geçiş, peşinden dron vınlaması | hava | efekt | −18 | ara: `fast craft pass by with small drones following doppler` |
| C30 | 4,5-10 | kıvrılan metal fırtınası şeridine giriş: ince demir yaprakların keskin yakın sürtünmeleri | hava | efekt | −20 | üret: `thin iron leaves whipping past, light metallic ticks and sharp close scrapes, fast` |
| C31 | 0-10 | kararlı akış izi (Raka ve Thren arkada): AKIŞ İZİ | hava | efekt | −20 | AKIŞ İZİ örneği |
| C31 | 0-10 | Sael'in hızlandırıcısı önde: temiz, güçlü, sabit yanma | hava | efekt | −20 | üret: `a clean powerful steady booster burn ahead, rich low roar, no crackle` |
| C31 | 0-10 | manyetik demir yaprakların aralıklı küçük metal geçişleri | hava | efekt | −22 | ara: `small metal leaves passing light metallic ticks thin` |
| C32 | 0-10 | kabin camındaki mavi enerji izi: çok alçak, soğuk elektrik parıltısı | kokpit | efekt | −30 | üret: `a faint cool electrical shimmer on cockpit glass, low and steady` |
| C33 | 0-10 | römorkör kabini: alçak uğultu ve Axi'nin yavaş, yorgun nefesi | kokpit | efekt | −26 | ara: `slow tired breathing adult close quiet cabin` |
| C34 | 0-5,5 | Sickle'ın son iki dronu çekişi: hızlı geçiş + dron vınlaması | hava | efekt | −20 | C30 geçiş örneği |
| C34 | ≈5,5-6,5 | iki metal yaprağın birbirine yaklaşıp kapanması: ağır metal sürtünmesi, daralan aralık | hava | efekt | −14 | üret: `two huge metal leaf panels sliding together, heavy grinding as the gap narrows and closes` |
| C34 | ≈6,0-7,0 | dronların düşmesi: çarpma çıtırtısı + sönen vınlama | hava | efekt | −16 | üret: `two small drones crunching against metal and tumbling away, their whine fading` |
| C34 | 7,0-10 | Sickle'ın alt şeride dönüşü: ince, sakin vınlama | gövde | efekt | −26 | C25 Sickle örneği |
| C35 | 0-10 | Bastion'un burnunu dış kapağa dayaması: ağır metal basınç gıcırtısı | gövde | efekt | −16 | üret: `a heavy craft pressing its flat reinforced nose against a large metal shutter, deep straining metal groan, steady pressure` |
| C35 | 0-10 | iki sağlam motorun dengelenen itişi — İKİ MOTOR (dengeli) | gövde | efekt | −20 | C29 İKİ MOTOR örneği, daha düzgün |
| C36 | ≈1,0-4,0 | Axi'nin servis kolunu kullanması: küçük hidrolik mekanik kol | gövde | efekt | −18 | ara: `small hydraulic service arm movement mechanical` |
| C36 | ≈4,0-10 | temizleme çevrimi: büyük kapak kilidi serbest kalır, ağır açılma gıcırtısı + basınç tıslaması | gövde | efekt | −14 | üret: `a massive maintenance shutter beginning to open, heavy lock release, deep metal groan and pressure hiss, slow` |
| C36 | 5,0-10 | çevrimin alçak yükselen enerji ısınması | hava | efekt | −24 | üret: `a low rising purge cycle hum building, mechanical and steady` |
| C37 | 0-10 | iki besleme kanalı: sol amber alçak-sıcak, sağ camgöbeği yüksek-soğuk, stereo ayrık — BESLEME | hava | efekt | −22 | C19 BESLEME örneği, yakın |
| C37 | ≈2,0-5,0 | iki aracın iki ayrı tünele ayrılışı: motor sesleri sol ve sağa ayrılır, dar metal kanalda yankı | hava | efekt | −18 | üret: `two craft splitting into two separate narrow metal tunnels, engine sounds panning apart left and right with tight echoes` |
| C38 | 0-10 | Needle dar sol kanalda: duvara yakın sıkışık motor yankısı (sol hoparlör) | gövde | efekt | −22 | üret: `a craft in a narrow metal channel, tight close engine echo off the walls, steady` |
| C38 | 0-10 | sol (amber) besleme | hava | efekt | −26 | BESLEME örneği, yalnız sol |
| C39 | 0-10 | Fang tek motorla yavaş, öksürük aralıklı, dar kanal yankısı (sağ hoparlör) — TEK MOTOR | gövde | efekt | −20 | C14 TEK MOTOR örneği, dar kanal yankılı |
| C39 | 0-10 | sağ (camgöbeği) besleme | hava | efekt | −26 | BESLEME örneği, yalnız sağ |
| C40 | ≈1,5 | Needle'ın sağlam sağ fren kanadı kontrollü açılışı — KANAT (C12 örneği) | gövde | efekt | −14 | C12 KANAT örneği, aynı |
| C40 | 2,0-7,0 | Needle'ın motor perdesinin alçalıp Fang'in perdesiyle eşitlenmesi: iki ton tek tonda birleşir | gövde | efekt | −20 | üret: `a racing engine note smoothly descending in pitch until it matches a second engine note exactly, two tones merging into one` |
| C41 | ≈2,0 | iki mavi hücrenin tam aynı anda serbest kalması: çift net kilit çözülmesi, biri sol, biri sağ kanalda | gövde | efekt | −12 | üret: `two heavy latch releases at exactly the same instant, clean double clack, one hard-panned left and one hard-panned right` |
| C41 | 2,0-4,0 | ana motorların düşük güce inişi | gövde | efekt | −22 | üret: `racing engines dropping to a low-power quiet whine` |
| C41 | 2,2-10 | iki hücrenin paralel süzülüşü: iki yükselen vızıltı (sol alçak-amber, sağ yüksek-camgöbeği), halkalara yaklaştıkça perdeler birbirine yaklaşır | hava | efekt | −18 | üret: `two blue energy cells streaking in parallel toward two rings, two smooth rising whistle-hums panned left and right, converging in pitch` |
| C41 | 4,0-10 | araçların yan çıkışlara süzülüşü: düşük güçlü sakin motor | gövde | efekt | −26 | C44 düşük güç örneği |
| C42 | 0-6,5 | iki hücre perdesi yaklaşıp birleşir | hava | efekt | −18 | C41 paralel süzülüş örneğinin devamı, perdeler birleşir |
| C42 | ≈6,5 | aşırı yük darbesi: tek kalın küt darbe, iki ışığın birlikte sönüşü (arena patlamaz) | gövde | efekt | −10 | üret: `a massive electrical overload thump, one blunt heavy pulse, both lights collapsing together with a falling whine, hull-borne, no explosion` |
| C42 | 6,6-8,5 | kilit mekanizmalarının tek tek kilitlenip çökmesi, alçak drone ölür; BESLEME kalıcı kesilir | gövde | efekt | −22 → sessiz | üret: `mechanical locks seizing and clicking out one after another as a low electrical drone dies away to nothing` |
| C43 | ≈0,5-8,0 | beş kilit çemberinin açılması: derin metalik klunk + hafif basınç tıslaması | gövde | efekt | −14 | üret: `five heavy circular lock rings unlatching, deep metallic clunks with a soft pressure release hiss` |
| C43 | 0-8,0 | hasat bağlantılarının sönüşü: alçak drone yavaşça sessizliğe iner | hava | efekt | −24 → −40 | üret: `a low harvester energy drone winding down slowly to near silence` |
| C44 | ≈0,5-2,5 | gücü kesilen kapağın basıncı bırakışı: yavaş metal gıcırtısı + tıslama | gövde | efekt | −18 | üret: `a heavy depowered shutter releasing pressure with a slow metallic groan and soft hiss` |
| C44 | ≈2,5-6,0 | Korv'un iki sağlam motoru: Bastion'un geri çıkışı — İKİ MOTOR | gövde | efekt | −20 | C29 İKİ MOTOR örneği |
| C44 | 4,0-10 | Sael'in izi: AKIŞ İZİ kararlı | hava | efekt | −22 | AKIŞ İZİ örneği |
| C44 | 4,0-10 | Needle ve Fang'in düşük güçlü manevra motorları: sakin, ince | gövde | efekt | −26 | üret: `small low-power maneuvering engines, quiet steady hum` |
| C45 | ≈6,2 | römorkörün bağlantı kelepçesinin açılışı: ağır kilit çözülmesi + kısa pnömatik tıslama | gövde | efekt | −13 | üret: `a heavy docking clamp unlatching with a metallic clunk and a short pneumatic hiss, close` |
| C45 | 6,5-10 | römorkörün ölçülü ilk itişi, yavaş uzaklaşma | gövde | efekt | −22 | üret: `modest maintenance tug thrusters firing gently, slowly easing forward` |
| C46 | 2,5-7,0 | farklı türden seyircinin ayağa kalkışı: kabuk, kumaş, zırh hışırtıları; sözsüz yumuşak tepkiler; alkış ve bağırma yok | hava | efekt | −20 | üret: `a vast crowd of many different alien beings slowly rising to their feet, soft rustles of cloth, shell and carapace, quiet non-verbal murmurs, no words, no cheering` |
| C46 | ≈7,0-9,5 | Kalix yayınının kararması: büyük yayın ekranının hum'ı alçalarak söner | hava | efekt | −22 | üret: `a large broadcast screen powering down, its hum sinking into silence` |
| C47 | 0-10 | düşük güçlü Needle kokpiti: yumuşak güç uğultusu, sakin nefes | kokpit | efekt | −28 | üret: `a quiet low-power cockpit hum with relaxed breathing and faint electronic ticks, close and dry` |
| C47 | ≈0,5 | Raka'nın uzun nefes verişi | kokpit | efekt | −26 | ara: `long slow exhale adult close relief` |
| C48 | 0-10 | altı aracın birlikte uzaklaşması: düşük güçlü, katmanlı altı uğultu, uzaklaşıp sönen | hava | efekt | −24 → −34 | üret: `six craft with low-power engines gliding away together, soft layered hums receding into the distance, long gentle fade` |

Kapsam: 48/48 çekim. Her satır, planın o çekimdeki olayına ya da planın yazdığı ses kuralına dayanır (hücre kilidi, kanat kopması, sağ fren kanadı, motor arızası, dron atışı, kapak, kilit çemberleri, tribün). Sessiz çekim yoktur. Bu kokpit ve kabin yüz portrelerinde (C04, C17, C20-C27, C32, C33, C47) efekt satırı "oyuncunun nefesi / kabin hum'ı"dır: kasıtlı küçük bir zemin, ses olayı değil.

## Model sesi AÇIK ortam ses cümlesi (madde 7)

Uygulanmaz: model sesi KAPALI. goruntu-yonetmeni video promptlarına ses cümlesi yazmaz.

## Final miks hedefi

```
Final miks   −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumlu (telsiz ve replik merkez; C41 sol/sağ simetrik eşit seviye; mono toplamda hücre sesleri birbirini silmez)
Ölçüm        python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4> [--uygula -o final.mp4]
Dinamik      doğrusal düzeltme; C42 aşırı yük darbesi (≈ −10) ile C43-C47 sakinliği (−24…−30) ve C02 0,0-1,2 s boşluğu ezilmez. Sesi düşük teslim etmek en ölümcül hata.
Replik       −15…−16 LUFS(k); müzik replik altında −6…−9 dB; telsiz −16
Yatak        −18…−22 LUFS (replik yokken); müzik yatağı −16…−18 (replik yokken)
Açılış       0-2 s insan sesi yok · müzik C01'de yok · C01→C02'de yatak kopmaz · önizleme sessiz oynasa da okunur (felaket görüntüde)
Bitiş        Y5 + efekt + müzik son 1,5 s'de −40 LUFS'a iner; dijital sıfır yok; DEAD LAST yazısı sessiz
M&E          Diyalogsuz miks (müzik + efekt + yatak) ayrı dışa aktarılır; telsiz sürekliliği ve R01 kaydı aynı master'dan
```

## Besteci notu (F4 müzik taslağı için, FILM §7)

- Plan müzik kelimesi: "Ortam ve müzik" = C07 · C10 · C12 · C13 · C16 · C29 · C31 · C37 · C43 · C46 · C48 (replik yok, müzik önde).
- ILK_30: C01'de müzik yok; C02 0,0-1,2 s boşluktan sonra çok düşük zemin; C03'te ilk gerçek giriş; replik altında −6…−9 dB.
- Kesmede müzik kesilmez; müziksiz anlar yalnız plan: C01 ve C02 başı.
- C16 (akış izi), C40-C42 (eşit hız → aynı darbe) ve C46 (suskunluktan ayağa kalkış) doruk noktalarıdır; C42 darbesinde müzik de yok olmaz, yalnız alçalır (ses bölümünün sert kesmesi BESLEME drone'una aittir).
- Müzik promptu İngilizce, Flow Music'e yapıştırılır; besteci F8'de gerçek kesme noktalarıyla kesinleştirir.

## PLAN DIŞI ÖNERİ (UYGULANMADI — yalnız sahip/Fable kararıyla)

1. **Başlık ve yazı vuruşları.** PREVIOUS RACE (C01 ilk 2 s) · NEXT RACE (C03) · DEAD LAST (C48 son 1,5 s) yazılarına kısa alçak tık ya da bas vuruşu. Plan yazıyı kurguda ekler, ses yazmaz.
2. **C19 beş dünya bağlantı göstergeleri.** Beş yumuşak ping (plan yalnız görüntüyü tarif eder).
3. **C20 şema ve ikon belirişi.** Amber ve camgöbeği iki yumuşak arayüz tıkı (şema kurguda eklenir, ses planda yok).
4. **C11 hücre koruma kapağı.** Axi "eject the cell" derken kapak tıkı (planın "acil hücre bırakma özelliği kurulur" cümlesi görüntü tarif etmez).
5. **C42 sonrası tam sessizlik.** Aşırı yük darbesinden sonra 0,5 s ses ve müzikte tam boşluk (şu an yalnız BESLEME kesilir; sessizlik −30'un altına inmez).
6. **C48 son vuruş.** DEAD LAST anında tek alçak bas notası (müzik sonu besteciye aittir).
7. **C38 kırık sol fren kanadının hafif ıslığı.** Plan hasarı görüntüde okutur; ses yazılmaz.
8. **Geçiş türü.** C02→C03 için `karisim 0,5` (şu an `kesme`, ses eşleşmeli kesme); karar kurgucuda.

## Açık noktalar (Fable'a)

1. **§5 düzeltmeleri.** R01 (C01 · 2,2 s), R24 (C20 · 4,5 s), R36 (C32 · 4,0 s), R38 (C34 · 6,0 s), R41 (C38 · 5,5 s). Hepsi yalnız saniye. R01 ILK_30'dan zorunlu; diğer dördü performans sırası ve cevap aralığı (R24→R25 3,5 s · R36→R37 2,5 s · R41→R42 2,5 s) ve R38 için olay sonrası tepkidir. F5'in C20 / C32 / C34 / C38 video vuruşları bu saniyeleri izlemeli; G01'den sonraki grupta (G03-G05) bildirilmeli.
2. **R47 Kaynak** (kabin ↔ telsiz): kamera C45'te Axi'nin kabininden mi bakıyor? Plan "kokpit camından araçlar görülür" der; öyleyse R47 `oda`.
3. **Dış plan fiziği.** Bu film vakum kuralına bağlı değildir (plan: sinemasal ses, FIZIK_IDDIASI yok). Dış geniş planlarda ses var, ama patlama ve yüksek ses basıncı yok; gövde üzerinden duyulan alçak-orta ses. Sahip daha sessiz bir dış plan isterse yalnız C07, C13, C30, C34 ve C48 sadeleştirilir.
4. **Y4 ve Y5 bölünmesi.** FILM §4 C21-C26 ve C28-C29'u M04 (okyanus) olarak yazıyor (Fable türetmesi); C18-C20 ve C30'dan sonrası M05. C18-C26 diyalog bakımından aynı an olduğundan Y5→Y4→Y5 geçişleri dört kez yatağı çaprazlıyor. Ortak taban drone'u bunu gizler. Sahneleme/goruntu-yonetmeni C21-C26 mekânını M05'e alırsa Y4 tek parça (C13-C17, C28-C29) ve çapraz sayısı azalır; GEÇİŞ'te C20→C21 ve C29→C30 `kesme` olarak kalır, tek ek bayrak C26→C27 çaprazı.
5. **Saniyeler tahmindir.** Efekt ve köprü saniyeleri (hücre kliği ≈4,2 s, kanat kopması ≈4,0 s, aşırı yük ≈6,5 s…) gerçek klip çıkınca F8'de hareket anına oturur.
6. **C42 darbe seviyesi.** −10 LUFS(s) vurgu, final −14 LUFS integrated'ı aşmaz; `kurgu.py yukseklik` taslakta ölçer.
7. **Telsiz mantığı.** Kalix R45 (C42) telsizde hafif kırpılmış: ses profili aynı, yalnız performans değişir; telsiz kaydında motor/ortam yoktur, sahnenin motor/ortam sesi dinleyenin kabin yatağıdır.
8. **Ağız kadrajda 20 replik.** Kayıt ayrı olduğundan klibin ağzı ile F8'de hizalanır. C20, C21, C23-C27, C32 ve C33 yüz portrelerinde ağız hareketi ≥ 2 s tolerans taşır; R30 ve R33 (5,0 s) sınırdadır.
9. **Yatak üretimi.** Altı yatağın "ne" cümleleri kütüphane aramasına da uyar (örn. `pressurized water hum low drone`, `metal leaves shimmer drone`); ortak taban drone'unun yalnız bir kez üretilip altı yatağa katılması tavsiye edilir.
