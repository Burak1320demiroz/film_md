# 🎞️ MEŞHUR SAHNE KALIPLARI KILAVUZU — İkonik Sahne Anatomisi ve Aktarımı

> **Neden var (22.08.2026):** Sinema tarihinin hafızaya kazınmış sahneleri
> bu deponun kısıtlarına (kasklı tek karakter · diyalogsuz · metinsiz ·
> lockoff · 8-10 s blok) çevrilebilir kalıplar içeriyor; ama hangilerinin
> taşınabildiği, hangilerinin telif sınırına çarptığı hiçbir dosyada yoktu.
> Kaynak: `araştırmalar/10.md` (22.08.2026 derin araştırma raporu).
> Dış film ANALİZİ var olan bir filmi inceler; bu dosya sinema tarihinden
> damıtılmış HAZIR ÜRETİM kalıpları verir (yazım tarafı).
>
> **Ne zaman okunur:** sahne haritasında vuruşa görsel karşılık ararken;
> kapak anı seçilirken (`KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` ile birlikte).

---

# 1. ⚖️ BEŞLİ AĞIRLIK — sabit kameralı kasklı sahneyi ne taşır

Klasik sinema dinamizmi kamera hareketi + diyalogdan gelir; bu formatta
ikisi de yok. Sahne etkisini belirleyen beşlinin ölçülen ağırlıkları:

```
IŞIK                    %40   sert kontrast + tek baskın kaynak
SES                     %25   atmosfer + kask içi nefes + düşük frekans
KOMPOZİSYON / ÖLÇEK     %20   negatif alan, silüet, tek noktalı perspektif
SÜRE / İÇSEL HAREKET    %10   mikrodinamik: buğu, toz, yansıma değişimi
AÇI                      %5   DOĞRU SEÇİLMİŞ varsayımıyla kalan pay —
                              açı önemsiz değil; seçimi ayrı dosyada:
                              KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md
```

Işığın başat olmasının nedensellik zinciri: sert ışık yüz detayını
karanlığa gömer → modelin piksel yükü ve halüsinasyon riski düşer →
8-10 saniyelik sabit çekim tutarlı render edilir. Formül: **dominant tek
şekil + basit kenar ışığı (rim) + temiz arka plan.** Çoklu ışık kaynağı
yerine TEK belirgin kaynak = titreşimsiz sonuç.

İçsel hareket zorunludur: tamamen hareketsiz kompozisyon ya "fotoğraf"
donukluğuna ya doku sertleşmesine düşer. Her kalıba camda buğu, süzülen
toz, yansıyan ışık değişimi gibi bir mikrodinamik yazılır.

---

# 2. 🖼️ TEK KARE TESTİ — kapak karesi değeri

İkonik sahnelerin ortak özelliği tek kareye sıkışabilmeleridir: görsel
karmaşadan arınmış + beklenti ihlali (pattern interrupt — beyin anomaliyi
0.3 saniyede yakalar). Kapak adayı sahne şu formülü sağlamalı:

```
□ Merkezde NET SİLÜET (tek baskın şekil)
□ Rim light ile arka plandan ayrıştırma
□ Vizör camında İKİNCİ hikaye objesi yansır (gezegen, yapı, patlama ışığı)
□ Kadrajın kalanı yoğun negatif alan
□ Vizör içindeki yüz OKUNMAZ → bilgi boşluğu izleyiciyi videoda tutar
```

Sayılar (ilk 3 saniye kancası): izleyicinin %71'i kalma kararını ilk
3 saniyede verir; kaybın %50-60'ı bu penceredir; dikeyde hedef
izlenme/kaydırma (VVSA) oranı %70-90. Güçlü tek kare kancası ölçülen
etkiler: 30. saniye tutması %70+, ortalama izlenme +%58, etkileşim +%340.
**Kapak anı SENARYO aşamasında seçilir** — paketleme-senaryo bütünlüğünün
tamamı `araştırmalar/8.md` raporunda.

---

# 3. ✅⛔ TAŞINABİLİR — TAŞINAMAZ KALIPLAR

Ayrım modelin uzamsal/zamansal tutarlılık sınırından gelir; "lockoff"
kuralının varlık sebebi de budur (hareketli kamera = görünmeyen yüzeyin
uydurulması = erime/morphing).

```
✅ TAŞINIR (sabit kamera + kasklı tek karakterde güvenli)
   · Atmosferik optik: hacimsel ışık, sis, lens flare, su kostiği
     (caustics) — ışık fiziği modelde sağlam kodlu
   · Kask/vizör yansımaları — mimik zayıflığını maskeler + sahne dışı
     dünyayı anlatır (çevresel hikâye aynası)
   · Mikro fizik: savrulan kum, eriyen buz, süzülen kablo/enkaz,
     yerçekimsiz damla — sabit özne etrafında kaotik element

⛔ TAŞINMAZ (tek prompt bloğuna sığmaz — deneme parası yakar)
   · Kamera hareketi isteyen kalıplar: arc, tracking, push-in, 180° dönüş
   · Kurgu masası kalıpları: match cut, montaj geçişi — bunlar klipler
     ARASI iştir → TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md
   · Oyunculuk/mimik kalıpları: kask zaten yüzü kapatıyor; mimiğe
     dayanan sahnenin taşınacak bir anatomisi kalmaz
```

---

# 4. ⚖️ HOMAGE / KOPYA SINIRI — telif kuralı

Kural: telif FİKRİ ve STİLİ korumaz, yalnız somut İFADEYİ korur. Türün
zorunlu ögeleri (scènes à faire) kimsenin tekelinde değildir: astronot,
hava kilidi, neon yağmurlu distopik şehir, çorak gezegende yürüyen figür,
kriyo kapsülü — hepsi serbest.

```
⛔ PROMPTA YAZILMAZ (kopya sınırı — tescilli ifade):
   özel isim, marka, karakter, tescilli prop/tasarım adı
   ("HAL 9000", "Xenomorph", "H.R. Giger tarzı", "Weyland-Yutani",
    "Tatooine", film adı + "gibi/style of" kalıbı)
   → model ezberden üretir; çıktı tescilli ifadeye "büyük ölçüde
     benzer" çıkarsa yasal risk sende.

✅ YAZILIR (homage sınırı — sahneyi ikonik yapan matematik):
   ışık oranı · lens · atmosfer · renk ısısı · ölçek ilişkisi · kompozisyon
   "Blade Runner'daki Las Vegas gibi"  →  "dev mimari yıkıntılar arasında
   tek kasklı figür, ortamı kaplayan monokromatik turuncu toksik sis,
   karakter yalnız koyu silüet, simetrik kompozisyon"
```

§6'daki 20 kalıbın tamamı bu çeviri yapılmış hâliyle verilmiştir —
hiçbirinde özel isim yoktur, hepsi scènes à faire alanında kalır.

---

# 5. 🔊 SES KATMANI — kalıbın yarısı kulakta

Ağırlık tablosunda ses %25: görüntü ne kadar güçlü olursa olsun kask içi
nefes, cama çarpan toz çizilmesi, düşük frekanslı uğultu duyulmadan
illüzyon eksik kalır. İnsan duyma sınırına yakın derin bas (infrasound,
~19 Hz civarı) fizyolojik tekinsizlik/dread üretir — korku ve tehdit
kalıplarının standart yatağıdır. Algoritma tarafı: çevresel sesi olan
video, sessiz videodan üst sırada dağıtılır.

Bu yüzden §6'daki her kalıbın prompt bloğu bir `Audio:` cümlesi taşır.
Replik/ses YAZIM kuralları `SES_VE_DIYALOG_URETIM_KILAVUZU.md`'de,
müzik `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md`'de.

---

# 6. 🧱 20 KALIP — kopyala, çıpanı tak, üret

Kullanım: her blok TEK 8-10 saniyelik sahnedir. Karakter tarifini filmin
BIBLE çıpasıyla değiştir (kelimesi kelimesine — `SAHNE_DEVAMLILIK_KILAVUZU.md`),
negatif çekirdeği ekle, V2 iskeletine oturt.

## 6.1 İzolasyon ve ölçek (uzay boşluğu ailesi)

**K1 · Hava kilidinde cenin** — ölçek kırılır, karakter rahimdeki bebek
gibi; hortum göbek bağı okunur (yeniden doğuş metaforu).
```
Medium wide shot. A lone astronaut in a heavy white spacesuit curled in a fetal position, floating slowly in a dark, metallic cylindrical airlock. Static lock-off tripod camera. Harsh, cool, high-contrast rim lighting from a single overhead clinical LED. Deep shadows, generous negative space. No subtitles, zero on-screen text. Audio: heavy, rhythmic, echoing breathing inside a helmet over a very low-frequency ambient drone. No dialogue.
```

**K2 · Boşluktaki nokta** — tek noktalı perspektif + zifiri boşluk;
siyah arka plan modelin render yükünü sıfırlar, titreme önlenir.
```
Extreme wide shot. A tiny, silhouetted astronaut floating tethered against the infinite, pitch-black void of deep space. Static lock-off camera. A single, distant, blinding star casts harsh bright light on one edge of the suit. Cinematic scale, 1-point perspective, absolute isolation. No subtitles. Audio: deep, unsettling sub-bass rumble, a subtle heartbeat fading in and out, extreme quiet.
```

**K3 · Vizörde gezegen** — yüz yerine camdaki yansıma anlatır; mikro
hareket buğudan gelir.
```
Extreme close-up shot of a scratched astronaut helmet visor. Static lock-off camera. The face inside is completely hidden in darkness. The curved glass clearly reflects a massive, glowing blue gas giant planet. Slow condensation forming on the cold glass. Sharp focus. No subtitles. Audio: faint, high-pitched crackle of dead radio static, slow muffled inhales.
```

**K4 · Monolitik karşılaşma** — alt açı + ölçek kontrastı: nesnenin
yüceliği karşısında insan ezilir.
```
Low angle wide shot. A helmeted figure stands motionless at the base of a towering, featureless black geometric structure. Static camera. Ground-level thick mist. Diffused atmospheric lighting from behind the structure creating a halo effect. Scale contrast, epic composition. No subtitles. Audio: a low, continuous industrial hum mixed with gravel crunching under a heavy boot.
```

**K5 · Vizörde hız tüneli** — soyutlama: hız hissi yalnız yansıyan ışıkla
verilir, kask sabit kalır.
```
Extreme close-up of a perfectly round, dark helmet visor. Static lock-off camera. The visor reflects streaks of psychedelic, abstract neon light warping at hyperspeed, shifting rapidly in color. The helmet itself remains completely still in darkness. Slow-motion reflection. No subtitles. Audio: an escalating, dissonant synthesized tone rising in pitch without resolving.
```

## 6.2 Atmosferik distopya ve teknolojik çürüme

**K6 · Toksik turuncu sis** — hacimsel sis arka plan detayını gizler:
silüet öne çıkar, render yükü düşer.
```
Wide shot. A lone character wearing an enclosed scavenger helmet standing perfectly still in vast, empty desert ruins. Static lock-off camera. Dense, monochromatic toxic orange volumetric fog fills the entire scene. The character is a dark silhouette against the orange haze. Swirling dust. No subtitles. Audio: howling desolate wind driving sand against metal, muffled under the heavy helmet.
```

**K7 · Neon yağmuru** — camgöbeği/macenta kontrastı teknolojik hüzün;
damlalar hazır mikrodinamik.
```
Medium high-angle shot. A figure in a high-tech glossy black helmet looking down. Static lock-off camera. Heavy, continuous rain bouncing realistically off the helmet visor. Lit by out-of-frame pulsing neon cyan and magenta city lights. Wet, highly reflective surfaces, moody cyberpunk. No subtitles. Audio: heavy rain on hard plastic, distant muffled city sirens, damp isolated atmosphere.
```

**K8 · Su kostiği** — görünmeyen su yüzeyinden yansıyan dalgalı ışık;
sabit karede zamanın aktığı hissini tek başına taşır.
```
Medium full shot. A person in a sleek metallic visor sitting completely still in a brutalist concrete room. Static lock-off camera. The only illumination is golden caustic light reflecting from an unseen pool of water, rippling slowly across the concrete walls and the character's armor. Symmetrical composition. No subtitles. Audio: slow, rhythmic dripping of water in a vast echoing concrete chamber, eerie silence otherwise.
```

**K9 · Kırmızı alarm** — tek renkli strobo anksiyete üretir; karanlık
göz bölgesini gizleyip modeli rahatlatır.
```
Close-up shot. A pilot in a bulky retro-sci-fi helmet. Static lock-off camera. The scene is bathed in harsh, flashing red emergency strobe light from an off-screen control panel. Deep shadows. The red light reflects rhythmically on the dark visor. Gritty high-contrast chiaroscuro, tense mood. No subtitles. Audio: a low, rhythmic warning klaxon muffled through a thick helmet, with heavy stressed breathing.
```

**K10 · Süpüren yeşil ışık** — alttan/yandan dönerek süpüren tarama
ışığı: hedef olma hissi + klostrofobi.
```
Close-up on a dark helmet. Static lock-off camera. The inside of the visor is dimly illuminated by a sweeping green scanning light, casting slow moving green shadows across the lower half of the hidden face. Total darkness surrounds the helmet. Tense, claustrophobic atmosphere. No subtitles. Audio: high-pitched, rhythmic mechanical pinging, getting slightly faster.
```

## 6.3 Zamanlama, boyut ve fiziksel kuvvet

**K11 · Ufukta su duvarı** — sabit ön plan + yavaş ilerleyen arka plan
tehdidi: kaçınılmazlık.
```
Full shot. An astronaut standing knee-deep in a shallow, perfectly calm body of water stretching to the horizon. Static lock-off camera. In the distant background, a colossal, impossibly high wall of water is slowly moving forward. Overcast, diffuse cool grey lighting. Imminent tension. No subtitles. Audio: the deafening, slow, building roar of massive rushing water in the distance, overwhelming everything else.
```

**K12 · Fırtınaya karşı** — görünmez kuvvete yaslanan beden; partikül
sistemi sahneyi taşır.
```
Medium wide shot. A character in a heavily armored suit and scratched visor leaning forward against an unseen force. Static lock-off camera. A violent, thick brown sandstorm completely obscures the background. Sand particles whipping past the lens at high speed. Flat, diffused, harsh lighting. No subtitles. Audio: violent high-pitched wind screaming against metal, sand scraping across the glass visor.
```

**K13 · Çözülen kriyo kapsülü** — buzun fiziksel erimesi = doku değişimi;
uyanış hissi tek blokta.
```
Top-down medium close-up shot of a cryogenic pod. Static lock-off camera. Inside, a figure wearing a tight, clear respiratory mask lies still. Frost and ice physically melting off the glass lid of the pod. Cold, sterile, bluish fluorescent light flickering slightly. High-tech medical aesthetic. No subtitles. Audio: a sharp hiss of depressurizing gas, then the cracking of thawing ice and a sudden gasp.
```

**K14 · Vizörde yanan yıldız** — kör edici kaynak + anamorfik parlama:
huşu ve saplantı.
```
Close-up shot of a golden reflective space helmet. Static lock-off camera. The visor reflects an impossibly bright, massive burning yellow star filling the entire reflection. The light is so intense it creates anamorphic lens flares across the frame. Intense heat aesthetic, awe-inspiring. No subtitles. Audio: a deep sustained bass rumble vibrating through the suit, with the crackle of thermal expansion.
```

**K15 · Kırılan gerçeklik** — havada yağ filmi gibi ışık kırılmaları;
çevrenin kendisi bozulur, karakter sabit.
```
Medium shot of a helmeted figure. Static lock-off camera. The air around the character is filled with shimmering, rainbow-colored, oil-slick-like refractions. The environment seems to subtly warp and distort behind the clear visor. Psychedelic, ethereal lighting, uncanny atmosphere. No subtitles. Audio: soft, crystal-like chiming that feels out of place, over a low unnatural drone.
```

## 6.4 Yabancılaşma, tehdit ve sessiz yıkım

**K16 · Karanlığa fener** — kask feneri tek ışık kaynağı ve kompozisyonun
yönlendirici çizgisi.
```
Medium full shot. A person in a dark spacesuit facing away from the camera, looking into a pitch-black cavern. Static lock-off camera. The only light source is a powerful, focused beam from their helmet, cutting through the darkness and illuminating floating dust motes. No subtitles. Audio: complete silence broken only by heavy boots crunching on stone, echoing into a hollow space.
```

**K17 · Altın saatte yıkıntı** — nostaljik sıcak ışık × yok oluş
kontrastı: sessiz çürüme.
```
Wide shot. A small, heavily suited figure standing in the middle of colossal, rusted technological ruins. Static tripod lock-off camera. Warm, nostalgic golden hour sunlight filtering softly through the metallic debris. Long dramatic shadows on the ground. A sense of deep history and quiet decay. No subtitles. Audio: a gentle, mournful wind blowing through hollow metal tubes, a natural eerie wind-chime effect.
```

**K18 · Cam ardındaki gölge** — sisin sakladığı devasa organik silüet:
idrak sınırındaki tehdit.
```
Wide shot. A human in an orange hazmat suit and transparent face shield standing before a massive glass wall. Static lock-off camera. Behind the glass, thick swirling white mist hides a colossal, ambiguous organic shadow. Soft, diffused backlighting through the mist. Quiet awe. No subtitles. Audio: deep, resonant, slow guttural vibrations that physically rumble, against sharp nervous breathing.
```

**K19 · Süzülen enkaz** — sıfır yerçekimi mikro fiziği; karakter sabit,
parçalar ağır çekimde geçer.
```
Close-up on a space helmet. Static lock-off camera. The character is entirely still. Small pieces of metallic debris, shattered glass, and a single floating droplet of water drift in extreme slow motion across the foreground, passing in front of the visor. Harsh, cold cinematic lighting. No subtitles. Audio: near-total silence, only a muffled, frightened heartbeat.
```

**K20 · Vizörde toz yayı** — aynasal vizör sahne dışı aksiyonu yansıtır;
tek renk + sert gün ışığı.
```
Extreme close-up of a lunar helmet visor. Static lock-off camera. The pristine mirrored visor reflects a rover's wheels spinning, kicking up a slow, arching spray of fine grey dust against a black sky. Sharp, un-diffused sunlight. High-contrast monochrome grey with bright white highlights. No subtitles. Audio: the mechanical whine of an electric motor cutting through radio static.
```

---

# 7. ✅ KALIP KULLANIM KURALLARI

```
□ Kalıp VURUŞUN karşılığıdır, sahnenin değil — önce vuruş tablosu
  (SENARYO_VE_VIRAL §2), sonra vuruşa uyan kalıp
□ Karakter cümlesi filmin BIBLE çıpasıyla DEĞİŞTİRİLİR (kelimesi kelimesine)
□ Negatif çekirdek (KILAVUZ_REHBERI §5) her prompta aynen eklenir —
  kalıptaki "No subtitles" satırı çekirdeğin yerini TUTMAZ
□ Bir filmde aynı kalıp en fazla 1 kez; iki komşu sahne aynı aileden
  (6.1-6.4) olamaz — örüntü kırıcı kapısı [KURGU_RITMI §2]
□ Kapak adayı sahne §2 tek kare testinden geçmeli
□ Özel isim / marka / tescilli tasarım prompta GİRMEZ (§4)
□ Kalıba kamera hareketi EKLENMEZ — taşınabilirlik §3'e dayanır;
  hareket eklendiği an kalıp "taşınamaz" sınıfına düşer
```

---

# 8. 📚 KAYNAKLAR

```
araştırmalar/10.md                      ham rapor (22.08.2026) — ağırlık
                                        gerekçeleri, telif içtihatları
KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md    açı seçimi (bu dosyanın %5'i)
KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md    kapak üretimi (§2 testi ile birlikte)
SES_VE_DIYALOG_URETIM_KILAVUZU.md       Audio cümlelerinin yazım kuralları
TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md    klipler arası geçiş (taşınamaz
                                        montaj kalıplarının doğru adresi)
```
