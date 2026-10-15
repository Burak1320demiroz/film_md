# 🎬 THE_FURNACE_GATE — Fırın Kapısı

```
FILM           THE_FURNACE_GATE
FORMAT         yatay 16:9
HEDEF_SURE     16:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/THE_FURNACE_GATE/
URETIM         Google Flow (web) · QA Gemini uygulaması — sahip planı: görseller GPT Image, videolar Gemini görselden video 10 s (THE_FURNACE_GATE_16MIN_96_CLIPS.md §7); REPLİKLER OMNI'DE, VİDEODA (sahip kararı 13.10.2026) → Flow "Return silent videos" KAPALI
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `FIZIK_IDDIASI yok`: dökümhane, çekirdek, EMP ve purge kurmacadır (plan R12 · R16: "fictional"); belgesel fizik anlatımı yok.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` (sahibin verdiği plan, 13.10.2026, birebir; kökten bu klasöre taşındı, düzenlenmez).** §1-§7 oradan yerleştirildi;
> faz 1-4 ajan turu açılmadı (THE_PLANET_THIEF · THE_MAYDAY_SEA yolu). Fable'ın plandan türettiği tek şey biçim çevirisidir (sütunlar,
> numaralar, süreler, yatak/geçiş tabloları, sabit cümleler); olay, kompozisyon, replik ve tasarım planın kendisidir. Replik saniye ve süreleri Fable tahminidir.
> **Sahip kararları (13.10.2026):** (1) "Plan farklarını düzelterek başla" → planın hat kurallarıyla çatışan kalıpları F5 çevirisinde düzelir
> (NOTLAR KARARLAR); (2) "Model sesi: video konuşsun" → plan "konuşmalar kurguda eklenir" der, bütün replikler §5 Kaynak = **model sesi (…)**,
> video promptlarında birebir, Flow'da ses AÇIK; kurgu kaydı yedek.

---

## 1. HİKÂYE

```
LOGLINE   İki kardeş otomatik bir uzay dökümhanesinden güç çekirdeği çalmaya girer; hurdaya ayrılmış gemide dört bin canlı yolcu bulunca çekirdeği yakarak gemiyi kurtarır.
AMAÇ      Leon ve Rhea Vance tug'larını ark'a yanaştırıp yükleme köprüsünden foundry'nin prototip kasasına girer ve taşınabilir güç çekirdeğini çalar (sahne 5-27); sahne 11'den sonra amaç ark'ı ve içindeki dört bin uyuyanı kapıdan çıkarmaktır.
ENGEL     Kapanan üç kepenkli çıkış kapısı ve iki gantri kelepçesi (1, 20); güvenlik drone'u (28-32); yerel override kilitli, kapı sürücüsü ve kelepçe motoru enerjisiz (33-37); Rhea'nın sınıflayıcı geçmişi ve Dione'deki kesilen tether (39-43); güvenliğin yükleme hattını vurması (52-53); purge sisteminin köprüyü geri çekmesi (73-75); kurtarma uçuşunda drone ateşi (82).
KARAR     Sahne 11: çekirdeği alıp herkesi kurtarmak; sahne 36-47: kendileri kaçabilecekken çekirdeği tüketmeyi seçerler ("We lose the core. We take everyone."); sahne 76-79: Leon güvenli çıkışı bekletip Rhea'yı almak için geri döner ("Not this time.").
SONUÇ     Kapı mekanik mandalla açık kalır, iki kelepçe bırakılır (65-72); Leon Rhea'yı acil soketten alır (85-86); ark kapıdan geçer, tug onu izler, purge arkalarında başlar (89-92); dört bin sinyal sabit (93); iki gemi özgür uzayda (96).
BEDEL     Çalınan çekirdek kapıyı açarken tükenir ve kontrol odasında sönük kalır; kazanç yok · sahne 69 · 94
TEK SORU  "Leon ve Rhea dört bin uyuyanı fırına girmeden kapıdan çıkarabilecek mi — ve Leon bu kez kardeşini bırakacak mı?"
SEÇİM     Fable: sahip planı (tek aday, aday turu açılmadı) · 13.10.2026 · gerekçe: THE_FURNACE_GATE_16MIN_96_CLIPS.md + ODA/DURUM.md SAHİP CEVAPLARI
SAHİP     ONAY (planı kendisi verdi: "plana uyarak filmi yapalım"; "Plan farklarını düzelterek başla") · 13.10.2026
```

Açılış cümlesi (plan): "We came to steal a power core. We left with a ship full of people." · Kapanış: "Where now?" / "Somewhere they can wake up."
Gerilimin basamakları (plan §4): çekirdeğe ulaşma → yolcuların canlı olduğu → override planının bozulması → geçmiş ve bedel → iki ayrı noktada çalışma →
kapı ve kilitler → köprünün kaybı, yeniden yanaşma → kapıdan birlikte geçiş. Son bölüm yeni canavar ya da ikinci felaket açmaz.
Karakterler (plan §3): **Leon Vance, 38, pilot** — temkinli, alaycı, "Keep a way back."; Dione'de gemiyi korumak için Rhea'nın tether'ini kesti; dönüşümü: geri döner.
**Rhea Vance, 34, sistem mühendisi** — "I know machines."; sınıflayıcının ilk sürümünü tasarladı, insan-güvenlik vetosu sonradan kaldırıldı; dönüşümü: gerçeği söyler, çekirdeği tüketir, kurtarılmayı kabul eder.
Sekiz bölüm (plan §4): B1 C01-C12 Hurda sandıkları gemi · B2 C13-C24 Çekirdeğe giden yol · B3 C25-C36 Kolay plan bozulur · B4 C37-C48 Rhea'nın geçmişi ·
B5 C49-C60 İki ayrı rota · B6 C61-C72 Kapı ve iki kilit · B7 C73-C84 Geri dönme kararı · B8 C85-C96 Kapıdan birlikte geçmek.

## 2. TRETMAN

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §9 "Tam 96 kliplik zaman çizelgesi" (Yeni olay) + her klibin İngilizce diyaloğu birebir (sahne = klip); "Ne değişir" Fable çevirisi (plan §4 · §5 · klip devamlılık notları) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Fırın kapısındaki esir gemi. LEON (VO): "We came to steal a power core. We left with a ship full of people." | Başlığın vaadi ilk karede: fırınla kapı arasında tutsak gemi. |
| S2 | 0:10–0:20 | Hedef ve ilk risk. RHEA: "That ark is in the burn cradle." | Hedef ve risk: ark yakma beşiğinde. |
| S3 | 0:20–0:30 | İşin amacı. LEON: "The spare core is in the foundry. The ark is our way in." | İşin amacı: çekirdek foundry'de, ark giriş yolu. |
| S4 | 0:30–0:40 | Giriş yolu seçilir. RHEA: "Maintenance berth. Then the loading bridge." | Giriş rotası: bakım yuvası, sonra yükleme köprüsü. |
| S5 | 0:40–0:50 | Küçük gemi büyük gövdeye yaklaşır. | Küçük gemi dev gövdeye yaklaşır. |
| S6 | 0:50–1:00 | Yanaşma kilidi. RHEA (comms): "We're attached." | Tug ark'a kilitlenir; K80'e kadar orada kalır. |
| S7 | 1:00–1:10 | Ark'a giriş. LEON: "No crew. No greeting." | Ark'a girilir: mürettebat yok. |
| S8 | 1:10–1:20 | Yeşil ışıkların fark edilmesi. RHEA: "Those storage units are drawing life-support power." | "Depolama birimleri" yaşam desteği çekiyor. |
| S9 | 1:20–1:30 | Yolcuların kanıtı. RHEA (comms): "They're sleepers. Still alive." | Yolcular canlı: kriyo uyuyanlar. |
| S10 | 1:30–1:40 | Kurtarılacak sayı. RHEA: "Four thousand stable life signs." | Sayı: dört bin yaşam belirtisi. |
| S11 | 1:40–1:50 | İlk ahlaki karar. LEON: "We take the core, then open their clamps." / RHEA: "Then we take everyone." | İlk ahlaki karar: herkesi alacaklar. |
| S12 | 1:50–2:00 | Fırın işlemi sürüyor. RHEA (comms): "We have until the purge reaches this berth." | Süre sınırı: purge bu yuvaya ulaşana kadar. |
| S13 | 2:00–2:10 | Yol ayrımı ve plan. RHEA: "The core first. Then we separate the gate from its automation." | Plan: önce çekirdek, sonra kapıyı otomasyondan ayırmak. |
| S14 | 2:10–2:20 | Leon'un temkinli tavrı. LEON: "And keep a way back." | Leon'un temkini: geri dönüş yolu. |
| S15 | 2:20–2:30 | Araçların hazırlanması. RHEA: "Keep this for a sentry. Not for a door." | EMP yalnız drone için ayrılır. |
| S16 | 2:30–2:40 | Sentry tehlikesi kurulur. LEON (comms): "Security is still awake." | Güvenlik uyanık: drone tehdidi kurulur. |
| S17 | 2:40–2:50 | Kapalı yükleme hattını geçiş. RHEA: "Stay inside the pressure line." | Basınç hattının içinden foundry'ye geçilir. |
| S18 | 2:50–3:00 | İkinci yanaşma noktası önceden görünür. LEON (comms): "An emergency socket below us. Good to know." | Acil soket önceden görünür (finalin yolu). |
| S19 | 3:00–3:10 | Kontrol coğrafyası. RHEA: "Gate power here. Clamp release beside it." | Kontrol coğrafyası: kapı gücü ve kelepçe bırakma. |
| S20 | 3:10–3:20 | İki kilit bilgisi. LEON: "Two clamps. Releasing one won't free her." | İki kilit var: biri gemiyi kurtarmaz. |
| S21 | 3:20–3:30 | Mekanik mandalın kurulması. RHEA: "This catch holds the gate open, even if power dies." | Mekanik mandal: güç ölse de kapı açık kalır. |
| S22 | 3:30–3:40 | Rhea'nın bilgi fazlalığı. LEON: "You know this place." / RHEA: "I know machines." | Leon şüphelenir: Rhea burayı tanıyor. |
| S23 | 3:40–3:50 | Kasa kilidinin kesilmesi. RHEA: "The contract core is in here." | Kasa kilidi kesilir. |
| S24 | 3:50–4:00 | Güç çekirdeği görünür. LEON: "There's our fortune." / RHEA: "There's their chance." | Çekirdek görünür: servet mi, şans mı. |
| S25 | 4:00–4:10 | Çekirdeğin tutulduğu kilit. RHEA (comms): "Release catch." | Çekirdeği tutan kilit açılır. |
| S26 | 4:10–4:20 | Çekirdek çıkarılır. LEON (offscreen): "Careful. That's worth more than the tug." | Çekirdek çıkarılır. |
| S27 | 4:20–4:30 | Çekirdek taşıma güvenliği. RHEA: "The core is secure." | Çekirdek askıda güvende. |
| S28 | 4:30–4:40 | Hırsızlık tespit edilir. LEON (comms): "That woke the security grid." | Hırsızlık fark edilir: güvenlik ağı uyanır. |
| S29 | 4:40–4:50 | Drone kapıda. LEON: "Down." | Drone kapıda. |
| S30 | 4:50–5:00 | İlk ateş. | İlk ateş. |
| S31 | 5:00–5:10 | EMP kullanımı. RHEA: "Keep your visor down." | EMP etkinleşir. |
| S32 | 5:10–5:20 | Sentry devre dışı. | Drone devre dışı. |
| S33 | 5:20–5:30 | İlk kurtarma planı başarısız. RHEA: "Local override is locked out." | İlk kurtarma planı çöker: yerel override kilitli. |
| S34 | 5:30–5:40 | Kilit fiziksel olarak tutuluyor. RHEA: "And the clamp motor has no feed." | Kelepçe motorunda besleme yok. |
| S35 | 5:40–5:50 | Kapı daha çok kapanır. LEON (comms): "The way out is getting smaller." | Çıkış daralıyor. |
| S36 | 5:50–6:00 | Kaçış seçeneği var. LEON: "We can undock. The ark can't." / RHEA: "Then find another way." | Kaçış seçeneği var; yolcular kaçamaz. |
| S37 | 6:00–6:10 | Gerçek teknik engel. RHEA: "The gate drive is dead. The capture locks are still powered." | Gerçek engel: kapı sürücüsü enerjisiz. |
| S38 | 6:10–6:20 | Yanlış cargo sınıflaması. LEON: "How did a ship full of people become scrap?" | Soru: insanlarla dolu gemi nasıl hurda oldu. |
| S39 | 6:20–6:30 | Rhea gerçeği söyler. RHEA: "I wrote the original cargo classifier." | Rhea itiraf eder: sınıflayıcıyı o yazdı. |
| S40 | 6:30–6:40 | Tasarım ile suistimal ayrımı. RHEA: "It had a human-safety veto. Someone removed it." / LEON: "You knew the architecture." | Tasarım ile suistimal ayrılır. |
| S41 | 6:40–6:50 | Kaçmak yerine düzeltmek. RHEA: "I didn't know what they'd done. Now I do." | Rhea kaçmak yerine düzeltmeyi seçer. |
| S42 | 6:50–7:00 | Eski terk edilme konuşulur. RHEA (offscreen): "At Dione, you cut the tether with me on the other end." | Dione: eski terk ediliş açılır. |
| S43 | 7:00–7:10 | Aile çatışması somutlaşır. LEON: "The ship was breaking apart." / RHEA: "I survived. The trust didn't." | Aile çatışması somutlaşır: güven kaybolmuş. |
| S44 | 7:10–7:20 | Konuşmanın üstünde gerçek tehdit. LEON (VO): "I'm not making that choice again." | Konuşmanın üstünde gerçek tehdit büyür. |
| S45 | 7:20–7:30 | Çözümün bedeli. RHEA: "This core can force the gate open. The overload will consume it." | Bedel: aşırı yük çekirdeği tüketir. |
| S46 | 7:30–7:40 | İki ayrı görev. RHEA: "I feed the gate and release port. You take starboard from the ark." | İki ayrı görev: kapı + port / sancak. |
| S47 | 7:40–7:50 | Karar verilir. LEON: "We lose the core. We take everyone." | Karar: çekirdeği kaybedip herkesi almak. |
| S48 | 7:50–8:00 | Görev için ayrılırlar. RHEA: "No one gets cut loose." | Görev için ayrılırlar. |
| S49 | 8:00–8:10 | Leon acil komuta köprüsünde. LEON: "I'm on the ark. Starboard release is still dead." | Leon ark'ın acil komutasında. |
| S50 | 8:10–8:20 | Rhea yeniden güç odasında. RHEA: "I'll feed the captured bus. Keep main thrust off." | Rhea güç odasına döner. |
| S51 | 8:20–8:30 | Yardımcı yönetim devreye alınır. LEON: "Backup control is live." | Yedek kontrol açılır. |
| S52 | 8:30–8:40 | Güvenlik yükleme hattını kesmeye başlar. RHEA (comms): "They're sealing the loading route." | Güvenlik yükleme hattını kesmeye başlar. |
| S53 | 8:40–8:50 | Rhea siper alır. RHEA: "I'm inside. Stay on your station." | Rhea siper alır. |
| S54 | 8:50–9:00 | Pilotun tepki ve güveni. LEON: "I'm here." | Leon yerinde kalır: "buradayım". |
| S55 | 9:00–9:10 | Çıkış rotası önceden hazırlanır. LEON: "Straight exit course loaded. Holding until release." | Çıkış rotası önceden yüklenir (K88'in yolu). |
| S56 | 9:10–9:20 | Uzaktan ark bağlantısı korunur. RHEA: "I've kept the route link. We can send her through from the tug." | Uzaktan ark bağlantısı korunur. |
| S57 | 9:20–9:30 | Ark'ın motorları hazırdır. LEON (comms): "Station-keep ready. Main burn waiting." | Ark'ın motorları hazır. |
| S58 | 9:30–9:40 | Çekirdek girişe hazırlanır. RHEA: "Core seated." | Çekirdek yuvaya oturur. |
| S59 | 9:40–9:50 | Çekirdek tutucu kilidi. | Çekirdek kilitlenir. |
| S60 | 9:50–10:00 | Kapı gücü açılır. RHEA: "Gate feed on." | Kapı gücü açılır. |
| S61 | 10:00–10:10 | Enerji sabit hatta ilerler. LEON (comms): "I have clamp power." | Enerji sabit hatta ilerler. |
| S62 | 10:10–10:20 | Dev kapı açılmaya başlar. RHEA (comms): "Gate drive is moving." | Dev kapı açılmaya başlar. |
| S63 | 10:20–10:30 | Açılan çıkış görülür. LEON: "Clear aperture. Lock it before the core dies." | Açıklık temiz: mandal şart. |
| S64 | 10:30–10:40 | Mekanik mandala ulaşır. RHEA: "Mechanical catch." | Rhea mekanik mandala ulaşır. |
| S65 | 10:40–10:50 | Kapıyı açık kilitler. RHEA: "Catch engaged." | Kapı açık kilitlenir. |
| S66 | 10:50–11:00 | Mandala fiziksel kanıt. LEON (comms): "It'll hold without power." | Mandal fiziksel kanıt: güç olmadan tutar. |
| S67 | 11:00–11:10 | Birinci gemi kilidini bırakır. RHEA: "Port clamp releasing." | Port kelepçesi bırakılır. |
| S68 | 11:10–11:20 | Sol gantri açılır. | Sol (port) gantri açılır. |
| S69 | 11:20–11:30 | Çekirdek tükenir. RHEA (comms): "The core is going." | Çekirdek tükeniyor. |
| S70 | 11:30–11:40 | İkinci motorun güç teyidi. LEON: "Starboard motor live." | Sancak motoru canlı. |
| S71 | 11:40–11:50 | İkinci kilidi çeker. LEON: "Starboard releasing." | İkinci kilit çekilir. |
| S72 | 11:50–12:00 | Ark tamamen serbest kalır. LEON (comms): "Both clear. Come back to the ark." | Ark tamamen serbest. |
| S73 | 12:00–12:10 | Kurtarma bitti sanılırken köprü alarmı. RHEA: "Gate is locked open. The bridge is still on purge control." | Bitti sanılırken: köprü hâlâ purge denetiminde. |
| S74 | 12:10–12:20 | Yükleme köprüsü geri çekilir. | Yükleme köprüsü geri çekilir. |
| S75 | 12:20–12:30 | Rhea karşıda kalır. RHEA: "The bridge is gone." | Rhea karşı tarafta kalır. |
| S76 | 12:30–12:40 | Pilot terk etmeyi reddeder. LEON: "Get to the emergency socket. I'm coming back." | Leon terk etmeyi reddeder. |
| S77 | 12:40–12:50 | Mühendis acil iskelede bekler. RHEA: "Socket ready. I can't hold this position forever." | Rhea acil iskelede bekler (yan hava kilidi kesmede). |
| S78 | 12:50–13:00 | Ark güvenli beklemeye alınır. LEON: "Ark on hold. Exit course stays armed." | Ark beklemeye alınır, çıkış rotası korunur. |
| S79 | 13:00–13:10 | Pilot küçük gemisine döner. LEON: "Not this time." | Leon tug'a döner: "bu sefer değil". |
| S80 | 13:10–13:20 | Tug ark'tan ayrılır. | Tug ark'tan ayrılır. |
| S81 | 13:20–13:30 | Köprünün altından kurtarma uçuşu. | Köprünün altından kurtarma uçuşu. |
| S82 | 13:30–13:40 | Güvenlik ateşinden geçer. LEON: "Keep your head behind the blast rib." | Ateşin içinden geçer. |
| S83 | 13:40–13:50 | Rhea portu hazırlayıp korunur. RHEA: "Emergency collar live." | Rhea portu hazırlar. |
| S84 | 13:50–14:00 | İkinci yanaşma yaklaşması. LEON (comms): "Contact." | İkinci yanaşma. |
| S85 | 14:00–14:10 | Kurtarma bağlantısı kilitlenir. RHEA (comms): "Hard seal." | Kurtarma bağlantısı kilitlenir. |
| S86 | 14:10–14:20 | İki kardeş yeniden birlikte. RHEA: "You came back." / LEON: "We're not finished." | İki kardeş yeniden birlikte. |
| S87 | 14:20–14:30 | Foundry bağlantısından ayrılma. RHEA (comms): "We're clear. I still have the ark link." | Foundry'den ayrılırlar; ark bağlantısı elde. |
| S88 | 14:30–14:40 | Yolcu gemisine çıkış komutu. RHEA: "Sending the ark through." / LEON: "Take everyone." | Yolcu gemisine çıkış komutu gider. |
| S89 | 14:40–14:50 | Ark çıkışa ilerler. | Ark çıkışa ilerler. |
| S90 | 14:50–15:00 | Tug ark'ın ardından hızlanır. LEON: "Stay behind her hull." | Tug ark'ın ardından hızlanır. |
| S91 | 15:00–15:10 | Büyük gemi kapıdan çıkar. | Büyük gemi kapıdan çıkar. |
| S92 | 15:10–15:20 | Tug da kurtulur; purge arkada kalır. | Tug da kurtulur; purge arkada kalır. |
| S93 | 15:20–15:30 | Yolcuların güvenlik teyidi. RHEA: "All four thousand sleeper signals stable." | Yolcular güvende: dört bin sinyal sabit. |
| S94 | 15:30–15:40 | Çalınan çekirdeğin son hâli. LEON (VO): "No core. No payday." | Bedel: çekirdek yok, kazanç yok. |
| S95 | 15:40–15:50 | Yeni ortaklık. LEON: "Terrible salvage margin." / RHEA: "Good day to be thieves." | Yeni ortaklık: güven davranışla onarıldı. |
| S96 | 15:50–16:00 | Özgür iki gemi. RHEA (comms): "Where now?" / LEON (comms): "Somewhere they can wake up." | İki gemi özgür uzayda. |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §8 R01-R16, numaralandı (sahip kararı 10.10.2026: <No>.<AD>, özne başına tek sayfa). Prompt metinleri planda; hat biçimindeki sürüm PROMPTLAR/G01.md REFERANS PROMPTLARI'nda. Plan R03 (iki kişilik ana kare) KALDIRILDI: ikinci bir kimlik görseli = özne başına tek sayfa kuralına aykırı ve yüz kayması riski (T16); iki kişilik çekimler 1.LEON + 2.RHEA ile kurulur, "Leon solda, Rhea sağda" ilişkisi prompt cümlesinde taşınır. Panel adları Fable'ın (13.10.2026) — sekiz grup paralel yazıldığı için baştan sabit; G01 yazarı yeni panel ekleyebilir, adını değiştirmez. -->
| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Leon Vance — TEK SAYFA (plan R01): 38 yaş, zeytin ten, kısa koyu kahve saç, kahve gözler, kısa düzgün sakal, SOL şakakta küçük soluk yara; fildişi basınç giysisi, grafit göğüs dikişleri, lacivert omuz zırhı, üst kollarda dar YANIK TURUNCU bantlar, beyaz eldivenler, fildişi yaşam destek paketi, sol göğüste mavi-altın rozet (soyut şahin), bilek-iletişim birimi, kemerde grafit kesici + güvenlik tether'i; yuvarlak fildişi kask, TAMAMEN ŞEFFAF kapalı vizör. Paneller: `front full-length panel` · `back full-length panel` · `side full-length panel` · `face close-up panel` (¾, sol şakak yarası görünür) · `glove panel` (tek beyaz eldiven) · F5 birleştirme (14.10): `right-profile close-up panel` (sağ profil, yara görünmez) · tether SAĞ kalçada, kesici SOL kalçada; bilek-iletişim birimi SOL bilekte · KAYNAK 15 (araçlar) | `1.LEON_v1.png` | v1 | | ⬜ | C02 · C03 · C07 · C11 · C13 · C14 · C17 · C19 · C20 · C22 · C24 · C27 · C29 · C33 · C36 · C38 · C40 · C42 · C43 · C46 · C47 · C48 · C49 · C51 · C54 · C55 · C63 · C70 · C71 · C76 · C78 · C79 · C82 · C86 · C88 · C90 · C93 · C95 |
| 2 | Rhea Vance — TEK SAYFA (plan R02): 34 yaş, zeytin ten, yeşil gözler, kask içinde sıkı alçak koyu bakır örgü, çenenin SAĞ yanında küçük yara; inci beyazı basınç giysisi, grafit eklemler, lacivert bel panelleri, üst kollarda dar soluk TEAL bantlar, beyaz eldivenler, sol göğüste mavi-altın rozet (soyut geometrik güneş), göğüs rozetinin altında rijit grafit çekirdek-taşıma askısı; kemerde kesici, gri EMP diski, güvenlik tether'i, fildişi bilek bağlantısı; yuvarlak inci kask, TAMAMEN ŞEFFAF kapalı vizör. Paneller: `front full-length panel` (askı boş) · `back full-length panel` · `side full-length panel` · `face close-up panel` (¾, sağ çene yarası görünür) · `harness with core panel` (çekirdek göğüs askısında kilitli) · F5 birleştirme (14.10): `left-profile close-up panel` (sol profil, yara görünmez) · bilek bağlantısı SAĞ bilekte · gri disk "EMP" diye anılmaz (`grey disc panel`) · KAYNAK 10 (çekirdek) + 15 (araçlar) | `2.RHEA_v1.png` | v1 | | ⬜ | C02 · C04 · C07 · C08 · C10 · C11 · C13 · C15 · C17 · C19 · C21 · C22 · C23 · C24 · C26 · C27 · C31 · C33 · C34 · C36 · C37 · C39 · C40 · C41 · C43 · C45 · C46 · C48 · C50 · C53 · C56 · C58 · C60 · C64 · C65 · C67 · C73 · C75 · C77 · C83 · C86 · C88 · C90 · C93 · C95 |
| 3 | Kestrel kurtarma tug'ı dış (plan R04): geniş kısa fildişi kama, koyu grafit alt gövde, burunda tek dar turuncu bant, geniş füme-mavi kanopi, yan yana iki gömme yuvarlak arka itici, dört kısa rijit radyatör kanatçığı; burunda yuvarlak bakım yanaşma yakası, düz iç kapak, tek geniş menteşeli kelepçe; yazı yok. Paneller: `side view panel` (burun sağda) · `three-quarter panel` · `bow collar open panel` (kelepçe açık) · `bow collar locked panel` (kelepçe kapalı) | `3.KESTREL_v1.png` | v1 | | ⬜ | C05 · C06 · C12 · C44 · C57 · C80 · C81 · C84 · C87 · C89 · C92 · C96 |
| 4 | Kestrel kokpiti (plan R05): boş iki koltuklu kokpit; Leon'un lacivert pilot koltuğu SOLDA, Rhea'nın mühendis koltuğu SAĞDA; iki sabit grafit dikmeli geniş ön kanopi, fildişi tavan kabuğu, soyut camgöbeği ışıklı alçak grafit konsol (yazı yok); solda kısa çift kumanda ve tek geniş işaretsiz yanaşma-bırakma anahtarı, sağda küçük işaretsiz bilek bağlantısı yuvası; amber lambalar. Paneller: `wide interior panel` · `pilot side panel` (sol kumandalar + yanaşma anahtarı) · `engineer side panel` (bilek bağlantısı yuvası) · F5 birleştirme (14.10): `seats from the front panel` (kanopi tarafından geriye bakış: pilot koltuğu kare SAĞINDA, mühendis koltuğu SOLDA, arkada perde ve tavan kabuğu; kanopi görünmez) | `4.KOKPIT_v1.png` | v1 | | ⬜ | C02 · C03 · C04 · C36 · C37 · C38 · C39 · C40 · C41 · C42 · C43 · C45 · C46 · C47 · C79 · C82 · C86 · C88 · C90 · C93 · C95 |
| 5 | Furnace Gate dış coğrafyası (plan R06): mavi gaz devi çevresinde dev otomatik dökümhane; siyah C biçimli sabit işlem beşiği beyaz koloni ark'ını ekseninde tutar; ark burnunun önünde (SAĞDA) üç rijit radyal sürgülü kepenkli dev dairesel çıkış kapısı; ark kıçının arkasında (SOLDA) ağır patlama kaburgalarıyla ayrılmış turuncu fırın egzoz çukuru; ark'ı karşılıklı iki yandan tutan iki dev rijit gantri kelepçe kolu; ark'ın port yanından foundry kontrol omurgasına kısa teleskopik kapalı yükleme köprüsü; köprünün altında foundry tarafında küçük acil tug soketi. Paneller: `wide exterior panel` (kepenkler kısmen kapalı, iki kelepçe kilitli) · `gate open panel` (üç kepenk tamamen açık, mekanik mandal oturmuş) · `clamps open panel` (iki çene ark'tan açık) · `bridge and socket panel` (köprü + altında acil soket) | `5.FOUNDRY_v1.png` | v1 | | ⬜ | C01 · C02 · C12 · C20 · C35 · C41 · C44 · C46 · C57 · C62 · C68 · C72 · C81 · C89 · C90 · C91 · C92 · C96 |
| 6 | Wayfarer koloni ark'ı (plan R07): dev uzun koloni gemisi, yazı yok; fildişi segmentli silindirik omurga, grafit sırt rayları, altı alçak dikdörtgen kriyo-habitat bloğu, iki büyük mavi arka motor, geniş dar ön kanopi; kıça yakın SANCAK yanında küçük yuvarlak tug bakım portu; PORT yanında kısa kapalı teleskopik yükleme köprüsü; iki sabit dış gantri kelepçesi karşılıklı gövde flanşlarında; açıkta yolcu/yüz yok. Paneller: `side view panel` (burun sağda, kıç solda) · `stern panel` (motorlar + sancak tug portu) · `port side panel` (yükleme köprüsü bağlantısı) | `6.ARK_v1.png` | v1 | | ⬜ | C01 · C05 · C06 · C12 · C35 · C36 · C41 · C44 · C46 · C57 · C62 · C68 · C72 · C79 · C80 · C81 · C89 · C90 · C91 · C92 · C93 · C96 |
| 7 | Ark koridoru (plan R08): boş basınçlı koridor; fildişi duvarlar, grafit ızgara, sabit lacivert tırabzanlar, amber acil lambalar; yakın uçta yuvarlak tug-erişim hava kilidi, uzak uçta ark köprüsüne dikdörtgen kapı; yan gözlem penceresinden kapalı kriyo salonu; başka bir yan kapı kapalı foundry yükleme köprüsüne. Paneller: `wide corridor panel` · `junction panel` (yükleme köprüsü kapısı SOLDA, komuta kapısı uzak SAĞDA) · `cryo window panel` (pencere SOL duvarda) · F5 birleştirme (14.10): `junction panel`'de iki kapı AÇIK (yükleme köprüsü kapısı solda, komuta kapısı uzak sağda) | `7.KORIDOR_v1.png` | v1 | | ⬜ | C07 · C08 · C10 · C11 · C13 · C14 · C15 · C48 |
| 8 | Kriyo salonu (plan R09): dev basınçlı salonda boş görünür koridor; opak kömür kapaklı aynı rijit fildişi uyku kapsülleri sıra sıra; her yolcu gizli; her kapsülde soluk yeşil durum noktası, sabit lacivert raylar, zeminde ince soluk buhar; beden silueti, yüz, çocuk yok. Paneller: `aisle panel` · `pod close panel` | `8.KRIYO_v1.png` | v1 | | ⬜ | C09 |
| 9 | Yükleme köprüsü (plan R10): ark ile foundry arasında rijit teleskopik kapalı köprü; kare grafit basınç tüneli, bel hizası korkuluklar, ızgara zemin, güçlendirilmiş cam yanlar; ark kapağı SOLDA, foundry kapağı SAĞDA; orta tünel bölümü foundry gövdesine düz çekilebilir, iki rijit uç platform arasında kısa vakum boşluğu bırakır; foundry ucunun altında ayrı acil tug soketi ve kısa iskele. Paneller: `interior tunnel panel` · `exterior intact panel` · `exterior retracted panel` (vakum boşluğu, iki uç kapağı kapalı) · `end platform panel` (foundry ucu platformu, kapak penceresi) | `9.KOPRU_v1.png` | v1 | | ⬜ | C16 · C17 · C18 · C52 · C74 · C75 |
| 10 | Çekirdek kasası ve çekirdek (plan R11): boş prototip kasası, grafit duvarlar, iki rijit saklama beşiği, alçak amber lambalar; kullanılmamış taşınabilir yüksek yoğunluklu güç çekirdeği: kompakt dikdörtgen grafit kasa, fildişi köşe korumaları, tek rijit üst taşıma kulpu, amber cam merkez, yazı yok; tek geniş menteşeli tutucu mandallı açık beşikte; yanında boş eş rijit taşıma askısı; el yok. Paneller: `vault wide panel` · `cradle close panel` (mandal kulp üstünde kapalı) · `core object panel` (kullanılmamış, amber) · `core overheating panel` (amber merkez çok parlak, kasa ısı izli) · `core spent panel` (merkez karanlık, kasa yanık) · F5 birleştirme (14.10): `vault empty panel` (iki beşik açık ve BOŞ, mandallar dışarıda, askı yok) · `vault door and crate panel` (sol duvarda ağır grafit kasa kapısı + göğüs hizasında küçük mandal, zemine cıvatalı ≈1,2 m grafit sandık, kapı üstünde yuvarlak kırmızı acil lamba) · `vault wide panel`'de yedek askı YOK (askı tasarımı yalnız 2.RHEA'da) | `10.CEKIRDEK_v1.png` | v1 | | ⬜ | C23 · C24 · C25 · C26 · C27 · C28 · C29 · C30 · C31 · C32 · C45 · C50 · C58 · C59 · C60 · C61 · C69 · C73 · C94 |
| 11 | Güvenlik drone'u (plan R12): tamamen mekanik otonom endüstriyel nöbetçi; rijit kompakt grafit dikdörtgen gövde, tek dar yatay KIRMIZI sensör şeridi, iki gömme manevra jeti, kısa ön yayıcı; yüz, uzuv, pilot yok; mat çizik metal. Paneller: `drone side panel` · `drone front panel` (kırmızı şerit) · `drone inert panel` (karanlık, ızgara zeminde bütün) | `11.DRONE_v1.png` | v1 | | ⬜ | C16 · C29 · C30 · C32 · C52 · C82 |
| 12 | Kapı güç ve kontrol odası (plan R13): boş basınçlı foundry kapı-kontrol odası; arka güçlendirilmiş pencere çıkış irisine ve ark'a bakar; alçak konsolda taşınabilir çekirdeğe eş dikdörtgen giriş yuvası, geniş MAVİ kapı-güç kolu, geniş TEAL port-kelepçe bırakma kolu A, ayrı TURUNCU mekanik kapı-mandal kolu; hepsi sabit menteşeli, görünür uç durdurucu, etiket yok; yuvanın yanında küçük işaretsiz bara konnektörü; SOLDA yükleme köprüsüne kapı, SAĞDA acil tug soketine kısa yan hava kilidi. Paneller: `wide room panel` (üç kol dik, yuva boş) · `console close panel` (yuva + üç kol + bara) · `levers down panel` (üç kol aşağıda kilitli) · `gate-catch pawl panel` (pencere yanı kapı desteği, mekanik dişli çentikte) · F5 birleştirme (14.10): `input cradle open panel` (çekirdek giriş yuvasına oturmuş, tutucu mandal KALKIK) · `local-control pad panel` (geniş düz işaretsiz yerel kontrol pedi + üstünde küçük uyarı lambası) · sayfaya ek: yuva kenarında ağır sabit kontak şeritleri, kapı yanında yuvarlak kırmızı köprü uyarı lambası | `12.KONTROL_ODASI_v1.png` | v1 | | ⬜ | C19 · C20 · C21 · C22 · C33 · C34 · C50 · C53 · C56 · C58 · C59 · C60 · C61 · C64 · C65 · C66 · C67 · C69 · C73 · C94 |
| 13 | Ark acil komuta köprüsü (plan R14): ark'ın kıç servis bloğunda boş iki koltuklu acil komuta; geniş ön kanopi önde foundry çıkış kapısını gösterir; pilot koltuğu SOLDA, navigasyon konsolu SAĞDA; pilot konsolunun yanında tek geniş GÜMÜŞ sancak-kelepçe bırakma kolu B; SAĞDA işaretsiz bilek bağlantısı yuvası (düz çıkış rotası + station-keep); lacivert koltuklar, fildişi kabuk, soyut camgöbeği arayüz ışıkları, amber acil lambalar, yazı yok. Paneller: `wide bridge panel` · `pilot console panel` (gümüş B kolu dik, yedek güç anahtarı, bilek bağlantısı yuvası) · `lever B down panel` · F5 birleştirme (14.10): pilot konsolunun yanında sabit lacivert tutunma korkuluğu; bilek bağlantısı yuvasında sabit oturmuş fildişi bağlantı modülü (C55-C78 hep dolu) | `13.KOMUTA_v1.png` | v1 | | ⬜ | C49 · C51 · C54 · C55 · C63 · C70 · C71 · C76 · C78 |
| 14 | Acil servis iskelesi (plan R15): yükleme köprüsünün foundry ucunun altında; kontrol odası yan hava kilidinden küçük yuvarlak tug yanaşma soketine uzanan korkuluklu kısa rijit dış iskele, sabit manyetik bot plakası, tek tether bağlantı noktası; tek geniş menteşeli yaka kelepçesi, pille çalışan amber kılavuz lambalar; ağır patlama kaburgaları uzak turuncu fırın çukurundan korur, iskelede doğrudan alev yok. Paneller: `catwalk wide panel` · `socket close panel` (yaka kelepçesi açık) · `socket locked panel` (tug yakası oturmuş, kelepçe kapalı) · F5 birleştirme (14.10): soket gövdesinde geniş işaretsiz pil-güç anahtarı; menteşeli kelepçe SOKET yakasındadır (tug yakası düz) | `14.ISKELE_v1.png` | v1 | | ⬜ | C77 · C83 · C84 · C85 · C87 |
| 15 | Araç ve küçük aksesuarlar (plan R16, tek sayfa, dört nesne): kısa mavi uçlu kompakt grafit plazma kesici · tek rijit gümüş manyetik bağlantı bloklu sarılı lacivert güvenlik tether'i · amber göstergeli küçük mat gri kurgusal EMP diski · geniş fiziksel anahtarlı ve camgöbeği durum ışıklı işaretsiz fildişi bilek bağlantısı; yazı yok. Paneller: `cutter panel` · `tether panel` · `grey disc panel` (küçük mat gri kurgusal disk; "EMP" yazılmaz) · `wrist-link panel` | `15.ARACLAR_v1.png` | v1 | | ⬜ | C04 · C10 · C14 · C15 · C23 · C31 · C37 · C42 · C56 · C77 · C83 · C88 · C93 |

```
SHA-256: shasum -a 256 ~/film_medya/THE_FURNACE_GATE/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: her sayfanın panelleri yukarıda adlandırıldı; çekim anahtarı paneli adlandırır ("Reference 2 (the woman, harness with core panel)").
Plan eşlemesi: R01→1 · R02→2 · R03 kaldırıldı (→ 1 + 2) · R04→3 · R05→4 · R06→5 · R07→6 · R08→7 · R09→8 · R10→9 · R11→10 · R12→11 · R13→12 · R14→13 · R15→14 · R16→15.
Plan "aynı mekânda kabul edilen son kare başlangıç olabilir" (§7) → zincir değildir; her kare tek başına üretilir. Zincir yalnız sahneleme adımıyla
  (§F3b) ve SMOKE zincir testi sonrası kurulur; bu filmde zincir yok (§4 Zincir sütunu "—").

ORTAK GÖRÜNÜM (GECIS_VE_SES_SUREKLILIGI §1 — her görsel ve video promptunun sonunda birebir; plan stil cümlesinden, oran etiketi ve olumsuz kuyruk çıkarılmış):
  Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
MEKÂN IŞIĞI (birebir, mekân başına; §4 Risk sütununun yanındaki mekân §6 ORTAM YATAĞI ile aynı):
  DIŞ (foundry, ark, köprü dışı, soket dışı) — cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs ·
  KOKPİT — warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy ·
  KORİDOR — amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window ·
  KRİYO — readable amber aisle lamps, cool blue walls, and dim green status dots on every pod ·
  KÖPRÜ İÇİ — cool blue light through the reinforced glass sides and amber guide lamps along the rails ·
  KONTROL ODASI — amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window ·
  KASA — low amber lamps on graphite walls and the warm amber glow of the core's glass center (C23-C27, çekirdek kadrajda) ·
  KASA ALARM — low amber lamps on graphite walls and one dull red emergency lamp pulsing above the open doorway (C28-C32; F5 birleştirme 14.10) ·
  KOMUTA — cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy ·
  İSKELE — amber battery guide lamps along the catwalk, cold starlight, and a distant orange furnace glow beyond the blast ribs.
DIŞ DÜNYA (T18 — F5 birleştirme 14.10; açık uzayın göründüğü her dış görselde ve kanopiden/pencereden uzay görünen içte, ışık cümlesinden hemen önce birebir; uzayın görünmediği yakın ekte yazılmaz):
  Everything hangs in deep black space with sparse stars, and a huge curved blue gas giant fills the far background.
ROL SÖZLÜĞÜ (referans anahtarındaki parantez, sekiz grupta birebir): 1 man · 2 woman · 3 tug · 4 cockpit · 5 foundry · 6 ark · 7 corridor · 8 cryo hall ·
  9 loading bridge · 10 core and vault · 11 drone · 12 control room · 13 command bridge · 14 catwalk · 15 tools.
ORTAM SESİ (model sesi AÇIK film — aynı mekânın her VİDEO promptunda birebir; yatak yine kurguda, §6):
  DIŞ — The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static.
  KOKPİT — The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets.
  KORİDOR — The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor.
  KRİYO — The only ambient sound is a deep, steady refrigeration hum with a faint hiss of floor vapor.
  KÖPRÜ İÇİ — The only ambient sound is a thin pressurized tunnel hum with a faint creak of rigid metal.
  KONTROL ODASI — The only ambient sound is a deep industrial machinery hum through thick walls.
  KASA — The only ambient sound is a close, low electrical hum inside a sealed vault.
  KOMUTA — The only ambient sound is soft bridge ventilation and quiet, steady console electronics.
  İSKELE — The only ambient sound is close breathing inside a sealed helmet over a low, steady pressure tone.
SES KİMLİĞİ (model sesi — her replikte aynı kelimeler; konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, diğerinin ağzı kapalı yazılır):
  Leon — a low, dry adult man's voice, calm and guarded · Rhea — a clear, quick adult woman's voice, precise and controlled ·
  telsiz ekidir: "…, softened by a light suit-radio filter" · voice-over: "a low, dry adult man's voice, calm and guarded, as a calm voice-over" (F5 birleştirme 14.10: adsız; prompt gövdesinde Leon/Rhea adı yazılmaz).
KİMLİK TABANI (plan K02 kimlik cümleleri, adlar yerine "the man" / "the woman"; kadrajdaki kişi için tek parça, ekler ayrı cümle):
  the man — an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet.
  the woman — an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet.
Sabit tasarım (plan §5 · §13): ark burnu SAĞDA (çıkış kapısı), kıç SOLDA (fırın çukuru); kaçış yönü soldan sağa · tug ark'ın kıç SANCAK portuna bir kez yanaşır,
  C80'e kadar orada · Leon solda, Rhea sağda (mümkün oldukça; C48 kapı coğrafyası gereği ters) · vizörler bütün filmde kapalı ve şeffaf · kriyo kapakları opak, yolcu
  yüzü/çocuk yok · çekirdek: C26'da beşikten çıkar, C27-C57 Rhea'nın göğüs askısında, C58'den sonra kontrol odası giriş yuvasında, C69 tükenir, C94 aynı yuvada sönük ·
  kapı: üç rijit kepenk, C62 açılır, C65 mandaldan sonra kapanmaz · port kelepçesi C68, sancak C72 açılır · ark C89'dan önce çıkış yakması yapmaz · köprü C74'te rijit
  geri çekilir, iki uç kapağı kapalı · Rhea C77'de iskelede bot + tether ile bağlı, C86'da tug'da, tether iskelede kalır · purge, güvenlik ve kapı override'ı ayrı
  devreler · kokpit ve komutada kollar/anahtarlar: kullanılmış kol aşağıda kalır (plan klip devamlılık cümleleri).
F5 birleştirme (14.10, ODA/F5_fable_birlestirme_1.md): KOKPİT YÖNÜ — arkadan bakışta (C02 C36 C79 C90 C93) pilot/Leon SOLDA, Rhea SAĞDA, kanopi önde;
  önden bakışta (yüzler okunur) pilot/Leon kare SAĞINDA, Rhea SOLDA, kanopi görünmez (`seats from the front panel`); kanopide ark gereken yüzlü çekim arka ¾ kurulur ·
  ÜÇ BAĞLANTI CİHAZI — Rhea'nın bilek bağlantısı (SAĞ bilek; tug mühendis yuvasına takılır C04 C88 C93) · ark komutasının sabit bağlantı modülü (yuvada, C55-C78) ·
  Leon'un bilek-iletişim birimi (SOL bilek, işlevsiz süs) · kriyo penceresi koridorun SOL duvarında · sayfa üretim sırası: 10 ve 15 önce, 1 ve 2 onlardan KAYNAK alır.
```

## 4. ÇEKİM LİSTESİ

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §10 K01-K96 (K = C, aynı numara). "Ekranda görünen" planın kendi İngilizce kompozisyon cümlesi ("Shot composition and initial state") → hareket cümlesi ("Main action") BİREBİR; çeviri yok, kayma olmasın. Hepsi görüntüden video (plan: GPT Image kare → Gemini/Flow). Referans: plan "Yüklenecek görsel referansları" numaralı (R03 → 1.LEON · 2.RHEA); fazla görünen referansı (örn. C01 10.CEKIRDEK) grup yazarı gerekçeyle çıkarır. Grup = plan bölümü: G01 C01-C12 · G02 C13-C24 · G03 C25-C36 · G04 C37-C48 · G05 C49-C60 · G06 C61-C72 · G07 C73-C84 · G08 C85-C96 -->
| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Fırın kapısındaki esir gemi | Extreme wide: the long colony ark is held in the foundry cradle, two clamps locked, three exit shutters partly closed. Orange furnace light grows behind the stern; blue gas giant beyond. → Slow lateral camera drift reveals the ark between furnace and exit; all large structures remain rigid. | aşırı geniş dış, yavaş yanal kayma | ark burnu sağda (çıkış kapısı), kıç solda (fırın) | 10 | Frames to Video | T18 gök cümlesi her dış planda birebir; dev yapılar rijit; model sesi Leon VO 2,0 s'den (plan "ilk saniyede" → ilk 2 s insan sesi yok, düzeltildi); plan R11 kasa referansı bu planda görünmüyor → G01 yazarı karar verir | 5.FOUNDRY · 6.ARK | G01 | ⬜ | — | — | — |
| C02 | Hedef ve ilk risk | Wide two-shot: Leon holds the tug controls left, Rhea reads her unmarked wrist-link right; the trapped ark fills the canopy. → Gentle cockpit push; Rhea lifts her eyes toward the ark, both remain seated. | geniş iki kişi, yumuşak itiş | Leon solda, Rhea sağda; ark kanopide | 10 | Frames to Video | T15 tam iki kişi; T16 yüzler 1.LEON · 2.RHEA (plan R03 ikili sayfa kaldırıldı); Rhea telsiz (K13 15.10: arkadan, ağız görünmez; ağız kapalı yazılı) | 1.LEON · 2.RHEA · 4.KOKPIT · 5.FOUNDRY | G01 | ⬜ | — | — | — |
| C03 | İşin amacı | Medium three-quarter on Leon, right glove on controls, reflected amber gate light across closed visor. → One small helmet turn toward Rhea off-camera. | orta ¾ Leon, küçük kask dönüşü | Leon sol koltukta, bakış sağa (Rhea kadraj dışı) | 10 | Frames to Video | T01 sağ eldiven kumandada ilk karede; Leon ağız kadrajda; ILK_30 §6 şeffaf vizörde yüz: yansıma durağan, yüz okunmazsa YEDEK (PROMPTLAR/G01 C03 notu) | 1.LEON · 4.KOKPIT | G01 | ⬜ | — | — | — |
| C04 | Giriş yolu seçilir | Medium on Rhea, wrist-link already connected to its fixed cradle, one cyan indicator on. → Her glove flips the single broad wrist-link toggle, no written interface. | orta Rhea, eldiven anahtarı çevirir | Rhea sağ koltukta | 10 | Frames to Video | T01 eldiven anahtarın üstünde başlar; T06 arayüzde yazı yok; Rhea ağız kadrajda | 2.RHEA · 4.KOKPIT · 15.ARACLAR | G01 | ⬜ | — | — | — |
| C05 | Küçük gemi büyük gövdeye yaklaşır | Wide side view: tug left, its bow collar aligned with the ark's starboard stern port, a short gap remaining. → Translate the rigid tug toward the port along one docking axis; stop at contact. | geniş yan dış, sabit; tug tek eksende | tug soldan sağa, ark kıç sancak portu sağda | 10 | Frames to Video | T01 temas son vuruşta, çarpma yok; T13 vakum (replik yok) | 3.KESTREL · 6.ARK | G01 | ⬜ | — | — | — |
| C06 | Yanaşma kilidi | Close on touching tug and ark collars; single hinged clamp open just above its latch. → Rotate the one clamp shut and hold; hulls remain rigid. | yakın dış ek plan, sabit | kelepçe yukarıdan aşağı | 10 | Frames to Video | T01 yakalar ilk karede temasta; tek hareket kelepçe; Rhea telsiz (kadraj dışı); T13 klip sesi yalnız replik penceresi | 3.KESTREL · 6.ARK | G01 | ⬜ | — | — | — |
| C07 | Ark'a giriş | Wide: both siblings already inside the open tug-access airlock, boots planted, corridor and cryo window ahead. → Short dolly reveals the empty corridor; Leon turns toward the side window. | geniş koridor, kısa dolly | Leon solda, Rhea sağda; Leon yan pencereye döner | 10 | Frames to Video | T10 uzun yürüyüş yok (giriş kesmede); T15 iki kişi; Leon ağız kadrajda | 1.LEON · 2.RHEA · 7.KORIDOR | G01 | ⬜ | — | — | — |
| C08 | Yeşil ışıkların fark edilmesi | Medium Rhea beside the cryo observation glass, closed pod rows behind it. → Rhea leans slightly toward the glass, keeping feet planted. | orta Rhea kriyo camının yanında | Rhea cama doğru hafifçe eğilir | 10 | Frames to Video | T10 ayaklar sabit; Rhea ağız kadrajda | 2.RHEA · 7.KORIDOR | G01 | ⬜ | — | — | — |
| C09 | Yolcuların kanıtı | Deep wide aisle: hundreds of opaque closed cryo pods, dim green lights, all people hidden. → Slow low track reveals repeating pod rows, no lids open. | derin geniş koridor, alçak yavaş takip | kamera sıralar boyunca ileri | 10 | Frames to Video | kapaklar opak; yolcu yüzü, siluet, çocuk yok (plan §13.1); T06 yazı yok; Rhea telsiz | 8.KRIYO | G01 | ⬜ | — | — | — |
| C10 | Kurtarılacak sayı | Close Rhea, unmarked wrist-link held at chest height; no legible display. → She looks from its cyan light back to Leon. | yakın Rhea, bilek cihazı göğüs hizasında | bakış cihazdan Leon'a (kadraj dışı) | 10 | Frames to Video | T06 ekran okunmaz, sayı yalnız replikte; Rhea ağız kadrajda | 2.RHEA · 7.KORIDOR · 15.ARACLAR | G01 | ⬜ | — | — | — |
| C11 | İlk ahlaki karar | Medium two-shot: Leon left, Rhea right, green pod lights beyond the window. → Leon pauses; Rhea holds his gaze, both remain still. | orta iki kişi | Leon solda, Rhea sağda; arkada yeşil kapsül ışıkları | 10 | Frames to Video | T12 küçük duraksama, donmaz; iki replik ağız kadrajda (Leon → Rhea) | 1.LEON · 2.RHEA · 7.KORIDOR | G01 | ⬜ | — | — | — |
| C12 | Fırın işlemi sürüyor | Wide rear-quarter of the ark: furnace trench glows behind, clamps hold, exit ahead remains partly closed. → One contained orange exhaust pulse rises behind blast ribs without striking the ark. | geniş dış arka-¾ | fırın çukuru solda/arkada, çıkış önde | 10 | Frames to Video | egzoz atımı kaburgaların arkasında kalır, gövdeye değmez; Rhea telsiz; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G01 | ⬜ | — | — | — |
| C13 | Yol ayrımı ve plan | Wide corridor: loading-bridge doorway left, ark command doorway far right; both already at the junction. → Rhea points once toward the loading doorway. | geniş koridor kavşağı | yükleme köprüsü kapısı solda, komuta kapısı uzak sağda; Leon solda, Rhea sağda | 10 | Frames to Video | tek işaret hareketi; Rhea telsiz (K13 15.10; ağız kapalı yazılı) | 1.LEON · 2.RHEA · 7.KORIDOR | G02 | ⬜ | — | — | — |
| C14 | Leon'un temkinli tavrı | Close Leon beside the loading doorway, cutter clipped to belt, closed visor readable. → He checks the existing tether anchor on his harness with one short grip. | yakın Leon | Leon köprü kapısının yanında | 10 | Frames to Video | T01 tether bağlantısı ilk karede elde, tek kısa kavrama; Leon ağız kadrajda; tether erken kurulur (plan) | 1.LEON · 7.KORIDOR · 15.ARACLAR | G02 | ⬜ | — | — | — |
| C15 | Araçların hazırlanması | Medium Rhea, core carry harness empty, cutter and grey EMP puck secured to belt. → She unclips the EMP puck into an already-open palm; one simple hand movement. | orta Rhea | — | 10 | Frames to Video | T01 avuç önceden açık, tek el hareketi; EMP kurgusal; Rhea ağız kadrajda | 2.RHEA · 7.KORIDOR · 15.ARACLAR | G02 | ⬜ | — | — | — |
| C16 | Sentry tehlikesi kurulur | Wide through bridge glass: one graphite sentry hovers outside near the foundry end, red sensor strip visible. → The rigid drone slides slowly across the outer window, no firing. | geniş, köprü camından dışarı | drone dış camın önünden yana kayar | 10 | Frames to Video | drone rijit, ateş yok; Leon telsiz | 9.KOPRU · 11.DRONE | G02 | ⬜ | — | — | — |
| C17 | Kapalı yükleme hattını geçiş | Wide: both already at the foundry end of the intact enclosed tunnel; ark hatch lies far left behind them. → Slow follow camera a short distance as they make two careful forward steps to the already-open foundry doorway. | geniş tünel, kısa takip | ark kapağı uzak solda, foundry kapısı sağda; ilerleme soldan sağa | 10 | Frames to Video | T10 iki kısa adım, koşu yok; Rhea telsiz (K13 15.10; ağız kapalı yazılı) | 1.LEON · 2.RHEA · 9.KOPRU | G02 | ⬜ | — | — | — |
| C18 | İkinci yanaşma noktası önceden görünür | Exterior wide on the foundry bridge end: emergency tug socket and catwalk clearly below it. → Slow downward tilt reveals the separate socket and side airlock, with bridge still intact. | geniş dış, yavaş aşağı tilt | köprü üstte, acil tug soketi altta | 10 | Frames to Video | iskele final için erken kurulur (plan); köprü sağlam; Leon telsiz; T13 | 9.KOPRU | G02 | ⬜ | — | — | — |
| C19 | Kontrol coğrafyası | Wide control room: both at entry, core cradle and three colored levers visible, exit iris through rear glass. → Short dolly toward the unoccupied control console. | geniş kontrol odası, kısa dolly | ikisi girişte; konsol önde, iris arka camda | 10 | Frames to Video | T09 üç kol dik, giriş yuvası boş; T06 etiket yok; Rhea telsiz (K13 15.10; ağız kapalı yazılı) | 1.LEON · 2.RHEA · 12.KONTROL_ODASI | G02 | ⬜ | — | — | — |
| C20 | İki kilit bilgisi | Medium Leon looking through rear window at two gantry clamp arms on opposite ark flanges. → Small eye-line turn from one arm to the other. | orta Leon, arka pencereye bakar | iki kelepçe kolu pencerede karşılıklı flanşlarda | 10 | Frames to Video | bakış bir koldan ötekine; Leon ağız kadrajda | 1.LEON · 5.FOUNDRY · 12.KONTROL_ODASI | G02 | ⬜ | — | — | — |
| C21 | Mekanik mandalın kurulması | Medium Rhea beside the upright orange gate-catch lever, hand hovering near it without contact. → Slow sideways camera slide reveals its fixed hinge and stop. | orta Rhea turuncu mandal yanında, yana kayan kamera | — | 10 | Frames to Video | T01 el temassız (bilinçli); kol şimdi çekilmez (K65); Rhea ağız kadrajda | 2.RHEA · 12.KONTROL_ODASI | G02 | ⬜ | — | — | — |
| C22 | Rhea'nın bilgi fazlalığı | Close two-shot at console, Leon left suspicious, Rhea right composed. → Leon turns slightly toward Rhea; she avoids his eyes. | yakın iki kişi, konsolda | Leon solda, Rhea sağda | 10 | Frames to Video | iki replik ağız kadrajda (Leon → Rhea); Rhea bakışını kaçırır | 1.LEON · 2.RHEA · 12.KONTROL_ODASI | G02 | ⬜ | — | — | — |
| C23 | Kasa kilidinin kesilmesi | Medium Rhea at vault entrance, cutter tip already against one small metal latch; Leon absent from frame. → One short blue cutter glow severs the existing small latch; door geometry stays fixed. | orta Rhea kasa girişinde | — | 10 | Frames to Video | T01 kesici ucu ilk karede mandalda; kapı geometrisi sabit; kesici insanlara karşı değil; Rhea ağız kadrajda | 2.RHEA · 10.CEKIRDEK · 15.ARACLAR | G02 | ⬜ | — | — | — |
| C24 | Güç çekirdeği görünür | Wide vault: door already open, both inside, unused core in its open storage cradle. → A restrained push reveals the amber core between the siblings. | geniş kasa, ölçülü itiş | çekirdek ikisinin arasında; Leon solda, Rhea sağda | 10 | Frames to Video | iki replik telsiz (K13 15.10; iki ağız kapalı yazılı) | 1.LEON · 2.RHEA · 10.CEKIRDEK | G02 | ⬜ | — | — | — |
| C25 | Çekirdeğin tutulduğu kilit | Close core cradle: broad retaining latch rests closed over the rigid carry handle; all power cell edges intact. → The one retaining latch rotates outward and stops; the core remains in place. | yakın beşik | mandal dışa döner | 10 | Frames to Video | el yok; tek mandal; Rhea telsiz | 10.CEKIRDEK | G03 | ⬜ | — | — | — |
| C26 | Çekirdek çıkarılır | Medium Rhea, both gloves already supporting the core's rigid handle and casing inside the open cradle. → Lift the single core a short distance clear of its supports; no regrip or body turn. | orta Rhea, iki eldiven çekirdekte | — | 10 | Frames to Video | T01/T02 kavrama ilk karede, tek kısa kaldırma; T09 tek çekirdek (askıda kopya yok); Leon kadraj dışı → telsiz | 2.RHEA · 10.CEKIRDEK | G03 | ⬜ | — | — | — |
| C27 | Çekirdek taşıma güvenliği | Two-shot: core already locked into Rhea's rigid chest carry harness; Leon at door, empty cradle behind. → Rhea checks one harness latch; Leon turns toward a rising red emergency lamp. | iki kişi | Leon kapıda solda, Rhea sağda; arkada boş beşik | 10 | Frames to Video | T09 çekirdek Rhea'nın göğüs askısında; kırmızı lamba yükselir; Rhea ağız kadrajda | 1.LEON · 2.RHEA · 10.CEKIRDEK | G03 | ⬜ | — | — | — |
| C28 | Hırsızlık tespit edilir | Wide empty vault axis: storage cradle empty, entrance open, amber lamps with one red emergency lamp. → The existing red lamp begins a slow pulse; no door changes. | geniş boş kasa ekseni | — | 10 | Frames to Video | T09 beşik boş, giriş açık; kırmızı lamba yavaş atar; Leon telsiz | 10.CEKIRDEK | G03 | ⬜ | — | — | — |
| C29 | Drone kapıda | Wide Leon already crouched behind a fixed heavy vault crate; one sentry hovers at the doorway, red strip aimed inward. → The drone slides a short distance into the doorway; Leon stays behind cover. | geniş Leon sandık arkasında | drone kapıda, kırmızı şerit içeri dönük | 10 | Frames to Video | drone rijit, kısa giriş; Leon ağız kadrajda | 1.LEON · 10.CEKIRDEK · 11.DRONE | G03 | ⬜ | — | — | — |
| C30 | İlk ateş | Close side view of the existing drone emitter; a fixed crate lies in its firing line, no human visible. → Emit one brief fictional blue-white pulse into the crate edge; small contained sparks, no explosion. | yakın yan, drone yayıcısı | atım yayıcıdan sandığa | 10 | Frames to Video | atış ve tepki ayrı planlarda (plan); küçük kıvılcım, patlama yok; insan yok; replik yok | 10.CEKIRDEK · 11.DRONE | G03 | ⬜ | — | — | — |
| C31 | EMP kullanımı | Medium Rhea crouched behind the same crate, core in chest harness; grey EMP puck already attached to a nearby metal support. → Her glove presses the puck's one broad activation pad; one amber indicator brightens. | orta Rhea sandık arkasında | — | 10 | Frames to Video | T01 EMP ilk karede destekte, tek basış; T09 çekirdek askıda; Rhea ağız kadrajda | 2.RHEA · 10.CEKIRDEK · 15.ARACLAR | G03 | ⬜ | — | — | — |
| C32 | Sentry devre dışı | Drone centered near doorway, rigid body, red strip already flickering; faint amber reflection from the puck. → Red strip fades and the intact drone lowers gently to the grated floor; no flying fragments. | drone ortada, kapıya yakın | drone yavaşça yere iner | 10 | Frames to Video | parçalanma yok, gövde bütün; replik yok | 10.CEKIRDEK · 11.DRONE | G03 | ⬜ | — | — | — |
| C33 | İlk kurtarma planı başarısız | Wide control room: Rhea with core in harness at console, Leon near gate window; core not yet inserted in bus. → Rhea touches the existing unmarked local-control pad once; fixed warning lamp stays red. | geniş kontrol odası | Rhea konsolda, Leon kapı penceresinin yanında | 10 | Frames to Video | T09 çekirdek askıda, yuva boş; uyarı lambası kırmızı kalır; Rhea ağız kadrajda | 1.LEON · 2.RHEA · 12.KONTROL_ODASI | G03 | ⬜ | — | — | — |
| C34 | Kilit fiziksel olarak tutuluyor | Close on Rhea's glove already around the teal clamp-A lever; lever still upright against a fixed mechanical lock. → One small resisted movement of the lever, then stop without bending it. | yakın Rhea'nın eldiveni teal kolda | — | 10 | Frames to Video | T01 el ilk karede kolda; kol bükülmez; yüz kadraj dışı → telsiz | 2.RHEA · 12.KONTROL_ODASI | G03 | ⬜ | — | — | — |
| C35 | Kapı daha çok kapanır | Wide ark and exit: both capture arms still locked; the three rigid shutters now narrow the exit farther. → Slide the three existing shutters a small distance inward; preserve every blade and ring. | geniş ark ve çıkış | üç kepenk içe kayar | 10 | Frames to Video | T09 üç rijit kepenk, iki kol kilitli; Leon telsiz; T13 | 5.FOUNDRY · 6.ARK | G03 | ⬜ | — | — | — |
| C36 | Kaçış seçeneği var | Two-shot back in tug cockpit, both seated, Rhea's core still in chest harness; tug remains docked to ark. → Leon looks at his controls, then at Rhea, without operating them. | iki kişi kokpitte | Leon solda, Rhea sağda | 10 | Frames to Video | T09 çekirdek askıda, tug bağlı; iki replik telsiz (K13 15.10: arkadan, ağızlar görünmez) | 1.LEON · 2.RHEA · 4.KOKPIT · 6.ARK | G03 | ⬜ | — | — | — |
| C37 | Gerçek teknik engel | Medium Rhea seated right, core in harness, wrist-link glowing abstract cyan. → She angles the wrist-link toward the canopy, no readable map. | orta Rhea sağ koltukta | bilek cihazı kanopiye dönük | 10 | Frames to Video | T06 harita yok; Rhea ağız kadrajda | 2.RHEA · 4.KOKPIT · 15.ARACLAR | G04 | ⬜ | — | — | — |
| C38 | Yanlış cargo sınıflaması | Close Leon, cryo green lights faintly reflected from the nearby ark corridor. → He looks toward Rhea offscreen. | yakın Leon | bakış sağa (Rhea kadraj dışı) | 10 | Frames to Video | Leon ağız kadrajda; plan "cryo green lights … from the nearby ark corridor" kokpitte → G04 yazarı ışık kaynağını kokpite uyarlar | 1.LEON · 4.KOKPIT | G04 | ⬜ | — | — | — |
| C39 | Rhea gerçeği söyler | Close Rhea behind clear visor, guarded face and teal arm band. → Her expression settles; no camera movement beyond a restrained push. | yakın Rhea, kontrollü itiş | — | 10 | Frames to Video | T12 küçük ifade değişimi; Rhea ağız kadrajda | 2.RHEA · 4.KOKPIT | G04 | ⬜ | — | — | — |
| C40 | Tasarım ile suistimal ayrımı | Medium two-shot, core between their sightlines in Rhea's harness. → Leon holds her gaze; Rhea remains still. | orta iki kişi | Leon solda, Rhea sağda; çekirdek bakış hattında | 10 | Frames to Video | iki replik ağız kadrajda (Rhea → Leon) | 1.LEON · 2.RHEA · 4.KOKPIT | G04 | ⬜ | — | — | — |
| C41 | Kaçmak yerine düzeltmek | Medium Rhea with the captured ark visible through canopy behind. → She turns her eyes toward the ark rather than Leon. | orta Rhea, kanopide ark | bakış Leon'dan arka plandaki ark'a | 10 | Frames to Video | Rhea ağız kadrajda | 2.RHEA · 4.KOKPIT · 5.FOUNDRY · 6.ARK | G04 | ⬜ | — | — | — |
| C42 | Eski terk edilme konuşulur | Close Leon, glove resting on a controls-side tether anchor attached to his harness. → He grips the anchor once, then relaxes. | yakın Leon, eldiven tether bağlantısında | — | 10 | Frames to Video | T01 el ilk karede bağlantıda; Rhea kadraj dışı → telsiz, Leon'un ağzı kapalı | 1.LEON · 4.KOKPIT · 15.ARACLAR | G04 | ⬜ | — | — | — |
| C43 | Aile çatışması somutlaşır | Two-shot: Leon left, Rhea right, both closed helmets, core secured. → Leon turns toward her, without dramatic grabbing or movement. | iki kişi | Leon solda, Rhea sağda | 10 | Frames to Video | iki replik ağız kadrajda (Leon → Rhea); dramatik tutma/hareket yok | 1.LEON · 2.RHEA · 4.KOKPIT | G04 | ⬜ | — | — | — |
| C44 | Konuşmanın üstünde gerçek tehdit | Rear wide ark: orange furnace trench brighter; hull still untouched behind blast ribs. → A low exhaust pulse illuminates the intact hull underside, then dims. | geniş arka ark | fırın çukuru arkada, daha parlak | 10 | Frames to Video | egzoz atımı gövdenin altını aydınlatır, değmez; Leon VO; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G04 | ⬜ | — | — | — |
| C45 | Çözümün bedeli | Medium Rhea with one glove on the core casing in her harness. → She touches its amber center guard once, no disassembly. | orta Rhea, eldiven çekirdek kasasında | — | 10 | Frames to Video | T01 tek dokunuş, söküm yok; Rhea ağız kadrajda | 2.RHEA · 4.KOKPIT · 10.CEKIRDEK | G04 | ⬜ | — | — | — |
| C46 | İki ayrı görev | Two-shot: Rhea gestures toward ark bow, Leon toward foundry side through canopy. → One short pointing gesture from each, separated in time. | iki kişi, kanopiden işaret | Rhea ark pruvasına, Leon foundry tarafına | 10 | Frames to Video | iki işaret zamanda ayrık; Rhea ağız kadrajda | 1.LEON · 2.RHEA · 4.KOKPIT · 5.FOUNDRY · 6.ARK | G04 | ⬜ | — | — | — |
| C47 | Karar verilir | Close Leon, controlled determined face, hands resting on controls. → One restrained nod. | yakın Leon | — | 10 | Frames to Video | tek ölçülü baş sallama; Leon ağız kadrajda | 1.LEON · 4.KOKPIT | G04 | ⬜ | — | — | — |
| C48 | Görev için ayrılırlar | Wide junction: Leon by ark-command doorway, Rhea by loading-bridge doorway, core in her harness. → They exchange one look and each makes one short step toward their already-open route. | geniş kavşak | Leon komuta kapısında (sağda), Rhea köprü kapısında (solda) — K13 kapı coğrafyası gereği, olağan "Leon solda" düzeninin tersi (T11) | 10 | Frames to Video | iki kısa adım; Rhea ağız kadrajda | 1.LEON · 2.RHEA · 7.KORIDOR | G04 | ⬜ | — | — | — |
| C49 | Leon acil komuta köprüsünde | Wide emergency ark bridge in the stern service block: Leon at pilot chair, silver release-B lever upright, gate ahead through canopy. → Short dolly behind the chair as Leon plants his boots and sets both gloves on the controls. | geniş komuta köprüsü, koltuğun arkasından kısa dolly | Leon sol pilot koltuğunda, kapı kanopide önde | 10 | Frames to Video | T09 gümüş B kolu dik; yüz arkadan → telsiz | 1.LEON · 13.KOMUTA | G05 | ⬜ | — | — | — |
| C50 | Rhea yeniden güç odasında | Medium Rhea already inside control room, unused core still in chest harness, input cradle empty. → She looks from the core to the blue power lever. | orta Rhea kontrol odasında | bakış çekirdekten mavi kola | 10 | Frames to Video | T09 çekirdek askıda, yuva boş; Rhea ağız kadrajda | 2.RHEA · 10.CEKIRDEK · 12.KONTROL_ODASI | G05 | ⬜ | — | — | — |
| C51 | Yardımcı yönetim devreye alınır | Close Leon's glove already on one broad backup-power toggle beside the pilot console. → Flip the one toggle; existing cyan console lights strengthen. | yakın Leon'un eldiveni yedek güç anahtarında | — | 10 | Frames to Video | T01 el ilk karede anahtarda; yüz kadraj dışı → telsiz | 1.LEON · 13.KOMUTA | G05 | ⬜ | — | — | — |
| C52 | Güvenlik yükleme hattını kesmeye başlar | Exterior side of intact bridge: one sentry at its foundry end, red sensor aimed at a fixed outer glass support. → One short fictional pulse strikes the support; contained sparks, no whole bridge break. | dış yan, sağlam köprü | drone köprünün foundry ucunda | 10 | Frames to Video | tek atım dış cam desteğine, köprü kırılmaz; Rhea telsiz; T13 | 9.KOPRU · 11.DRONE | G05 | ⬜ | — | — | — |
| C53 | Rhea siper alır | Wide Rhea already crouched behind the fixed console, core in harness; doorway pressure bulkhead closed behind her. → One near impact flashes beyond the doorway window; Rhea keeps her body behind the console. | geniş Rhea konsol arkasında | kapalı basınç perdesi arkada | 10 | Frames to Video | yakın darbe kapı penceresinin ötesinde; Rhea ağız kadrajda | 2.RHEA · 12.KONTROL_ODASI | G05 | ⬜ | — | — | — |
| C54 | Pilotun tepki ve güveni | Close Leon, eyes on the gate and suit radio, silver B lever still upright beside him. → He steadies one hand on the fixed rail rather than moving the ship. | yakın Leon | bakış kapıya; gümüş kol yanında | 10 | Frames to Video | Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G05 | ⬜ | — | — | — |
| C55 | Çıkış rotası önceden hazırlanır | Medium pilot console: Leon beside the unmarked wrist-link cradle, paired controls fixed, cyan geometric route shape without words. → His glove makes one short control-stick input and settles. | orta pilot konsolu | — | 10 | Frames to Video | T06 camgöbeği rota şekli, yazı/rakam yok; Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G05 | ⬜ | — | — | — |
| C56 | Uzaktan ark bağlantısı korunur | Close Rhea's wrist-link, cyan lamp stable, core visible on her harness at frame edge. → One broad link toggle engages; no digits or text. | yakın Rhea'nın bilek cihazı | çekirdek askıda kadraj kenarında | 10 | Frames to Video | T06 rakam yok; yüz kadraj dışı → telsiz | 2.RHEA · 12.KONTROL_ODASI · 15.ARACLAR | G05 | ⬜ | — | — | — |
| C57 | Ark'ın motorları hazırdır | Wide stern of ark: two engines have faint blue standby glows, both capture arms still locked; tug remains attached. → Existing engine glows settle at low idle without pushing the ark against clamps. | geniş arka ark | motorlar mavi bekleme ışığında; tug bağlı | 10 | Frames to Video | motorlar ark'ı kelepçelere itmez; Leon telsiz; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G05 | ⬜ | — | — | — |
| C58 | Çekirdek girişe hazırlanır | Medium Rhea, core already removed from harness and held just above matching input cradle with both gloves on rigid handles. → Lower the single core a short straight distance into the open cradle; no regrip. | orta Rhea, çekirdek giriş yuvasının üstünde | — | 10 | Frames to Video | T01 kavrama ilk karede, tek düz indirme; T09 askı boş, çekirdek bundan sonra odada; Rhea ağız kadrajda | 2.RHEA · 10.CEKIRDEK · 12.KONTROL_ODASI | G05 | ⬜ | — | — | — |
| C59 | Çekirdek tutucu kilidi | Close core fully seated in cradle, one broad retaining latch open above its casing. → Rotate the one latch closed to its fixed stop; casing stays rigid. | yakın yuva | mandal kapanır | 10 | Frames to Video | el yok; replik yok | 10.CEKIRDEK · 12.KONTROL_ODASI | G05 | ⬜ | — | — | — |
| C60 | Kapı gücü açılır | Close Rhea's glove already around the broad blue power lever, core latched beside it; blue lever upright. → Pull the one lever down to its stop; existing amber core light strengthens. | yakın Rhea'nın eldiveni mavi kolda | kol yukarıdan aşağı | 10 | Frames to Video | T01 el ilk karede kolda; yüz kadraj dışı → telsiz | 2.RHEA · 10.CEKIRDEK · 12.KONTROL_ODASI | G05 | ⬜ | — | — | — |
| C61 | Enerji sabit hatta ilerler | Close on latched core and fixed heavy bus contacts; amber center bright, surrounding metal unchanged. → One contained amber-cyan light pulse travels along existing contact strips; no new cable or arc. | yakın çekirdek ve bara kontakları | ışık atımı kontak şeritleri boyunca | 10 | Frames to Video | yeni kablo/ark yok; Leon telsiz | 10.CEKIRDEK · 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C62 | Dev kapı açılmaya başlar | Wide exit iris with three rigid shutters still partly closed, ark in foreground held by two clamps. → Slide the three existing shutters outward along their established radial tracks, opening the aperture. | geniş çıkış irisi | üç kepenk dışa açılır | 10 | Frames to Video | T09 rijit kepenkler kendi raylarında; Rhea telsiz; T13 | 5.FOUNDRY · 6.ARK | G06 | ⬜ | — | — | — |
| C63 | Açılan çıkış görülür | Medium Leon at bridge canopy: the gate is now fully open and normal starfield beyond is visible. → A slow push toward his visor and the unchanged open aperture. | orta Leon kanopide, itiş | kapı önde tamamen açık | 10 | Frames to Video | Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G06 | ⬜ | — | — | — |
| C64 | Mekanik mandala ulaşır | Medium Rhea beside the orange gate-catch lever, right glove already gripping it, gate fully open through rear window. → She braces her boots and holds the lever ready; no activation until the next shot. | orta Rhea turuncu mandalda | kapı arka pencerede tamamen açık | 10 | Frames to Video | T01 sağ eldiven ilk karede kolda; etkinleştirme bu planda yok; Rhea ağız kadrajda | 2.RHEA · 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C65 | Kapıyı açık kilitler | Close glove and orange catch lever at its upper stop, fixed hinge clearly visible. → Rotate the one orange lever downward to its locking stop, then hold. | yakın eldiven ve turuncu kol | kol aşağı | 10 | Frames to Video | yüz kadraj dışı → telsiz | 2.RHEA · 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C66 | Mandala fiziksel kanıt | Close window-side gate support: one broad mechanical pawl is already seated in its fixed notch, ring rigid, no hands. → Restrained camera push over the engaged pawl; nothing changes position. | yakın mandal dişlisi, ölçülü itiş | — | 10 | Frames to Video | el yok, hiçbir şey kımıldamaz; Leon telsiz | 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C67 | Birinci gemi kilidini bırakır | Close Rhea glove already gripping teal release-A lever, powered indicator cyan, lever upright. → Pull the single teal lever downward into a latched end stop. | yakın Rhea'nın eldiveni teal kolda | kol aşağı | 10 | Frames to Video | yüz kadraj dışı → telsiz | 2.RHEA · 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C68 | Sol gantri açılır | Wide on port gantry clamp: its broad rigid gripping jaw still around ark flange, opposite clamp visible locked deeper behind. → The one existing port jaw rotates outward and clears the hull; the opposite arm remains locked. | geniş port kelepçesi | port çenesi dışa döner; sancak kolu arkada kilitli | 10 | Frames to Video | T09 tek çene; replik yok; T13 | 5.FOUNDRY · 6.ARK | G06 | ⬜ | — | — | — |
| C69 | Çekirdek tükenir | Close latched portable core: amber center intensely bright, local casing heat-scored but fixed. → Let the contained glow peak and soften; no explosion or molten morphing. | yakın çekirdek | parlama zirve yapıp söner | 10 | Frames to Video | patlama/erime yok; Rhea telsiz | 10.CEKIRDEK · 12.KONTROL_ODASI | G06 | ⬜ | — | — | — |
| C70 | İkinci motorun güç teyidi | Medium Leon beside the silver release-B lever, one cyan readiness lamp now lit. → He checks the existing lamp and sets his glove on the grip. | orta Leon gümüş kolun yanında | — | 10 | Frames to Video | Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G06 | ⬜ | — | — | — |
| C71 | İkinci kilidi çeker | Close glove already wrapped around the upright silver B lever, fixed hinge and stop visible. → Pull the one lever down to its latched end stop. | yakın eldiven gümüş kolda | kol aşağı | 10 | Frames to Video | yüz kadraj dışı → telsiz | 1.LEON · 13.KOMUTA | G06 | ⬜ | — | — | — |
| C72 | Ark tamamen serbest kalır | Wide both ark flanges: port jaw already clear; starboard jaw still near hull; exit fully open and mechanically latched. → Rotate only the starboard jaw outward until both clamps are clear. The ark remains on station-keep. | geniş iki flanş | sancak çenesi dışa; port açık | 10 | Frames to Video | ark yerinde (station-keep); Leon telsiz; T13 | 5.FOUNDRY · 6.ARK | G06 | ⬜ | — | — | — |
| C73 | Kurtarma bitti sanılırken köprü alarmı | Medium Rhea at console, core now dark and scorched in its cradle; all three used levers down, hatch window beyond. → One existing red bridge-warning lamp begins pulsing; Rhea turns toward it. | orta Rhea konsolda | — | 10 | Frames to Video | T09 çekirdek sönük ve yanık, üç kol aşağı; kırmızı köprü lambası; Rhea ağız kadrajda | 2.RHEA · 10.CEKIRDEK · 12.KONTROL_ODASI | G07 | ⬜ | — | — | — |
| C74 | Yükleme köprüsü geri çekilir | Exterior wide: both rigid end platforms remain fixed, center telescoping section already slightly withdrawing toward foundry at right; end hatches closed. → Translate the single rigid center section farther into its foundry housing, widening the existing gap. No glass stretching or breaking. | geniş dış, köprü | orta segment sağa (foundry gövdesine) çekilir | 10 | Frames to Video | rijit kayma, cam esnemez/kırılmaz; replik yok; T13 | 9.KOPRU | G07 | ⬜ | — | — | — |
| C75 | Rhea karşıda kalır | Foundry-side end platform seen through its closed hatch window: Rhea inside, sealed helmet, vacuum gap and ark end beyond. → She plants one glove on the fixed hatch rim and looks across the gap. | Rhea kapak penceresinin ardında | vakum boşluğu ve ark ucu ötede | 10 | Frames to Video | Rhea ağız kadrajda (pencere ardında yüz) | 2.RHEA · 9.KOPRU | G07 | ⬜ | — | — | — |
| C76 | Pilot terk etmeyi reddeder | Close Leon at ark controls, gate open through canopy, clamp-B lever remains down. → He makes one decisive helmet turn toward the tug-access direction. | yakın Leon | kask tug erişim yönüne döner | 10 | Frames to Video | Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G07 | ⬜ | — | — | — |
| C77 | Mühendis acil iskelede bekler | Wide Rhea already outside at the sheltered service socket, boots on fixed magnetic plate; tether block attached to established rail anchor. → She tightens one short section of tether in her already-gripping glove; body stays anchored. | geniş Rhea dış iskelede | — | 10 | Frames to Video | T08 botlar manyetik plakada, tether bağlı; Rhea ağız kadrajda; T13 klip sesi yalnız replik penceresi | 2.RHEA · 14.ISKELE · 15.ARACLAR | G07 | ⬜ | — | — | — |
| C78 | Ark güvenli beklemeye alınır | Medium Leon beside the wrist-link cradle, station-keep control already selected, exit course retained. → One broad toggle click confirms hold; controls otherwise fixed. | orta Leon bilek bağlantı yuvasının yanında | — | 10 | Frames to Video | tek anahtar tıkı; Leon ağız kadrajda | 1.LEON · 13.KOMUTA | G07 | ⬜ | — | — | — |
| C79 | Pilot küçük gemisine döner | Wide tug cockpit: Leon already seated left; right seat empty, core absent; tug still on ark port. → His glove flips the broad docking-release toggle once. | geniş kokpit | Leon solda, sağ koltuk boş | 10 | Frames to Video | T15 tek kişi; çekirdek yok; Leon telsiz (K13 15.10: arkadan geniş) | 1.LEON · 4.KOKPIT · 6.ARK | G07 | ⬜ | — | — | — |
| C80 | Tug ark'tan ayrılır | Side view: tug collar already unlatched, a thin gap from ark starboard port; hulls intact. → Translate the rigid tug leftward away from the ark port, widening the existing gap; no stretching hoses. | yan dış | tug sola uzaklaşır | 10 | Frames to Video | hortum/esneme yok; replik yok; T13 | 3.KESTREL · 6.ARK | G07 | ⬜ | — | — | — |
| C81 | Köprünün altından kurtarma uçuşu | Wide foundry side: tug below the retracted loading bridge, emergency socket visible ahead near foundry control spine; ark held stationary behind. → Track the tug as it flies a single smooth arc toward the socket, maintaining rigid ship geometry. | geniş foundry yanı, takip | tug köprünün altından sokete yay çizer | 10 | Frames to Video | rijit gemi geometrisi; replik yok; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G07 | ⬜ | — | — | — |
| C82 | Güvenlik ateşinden geçer | Medium Leon in cockpit, glove on control stick; an existing sentry outside the canopy at distant frame edge. → One blue-white pulse passes outside the canopy without hitting it; Leon makes a small restrained control input. | orta Leon kokpitte | atım kanopinin dışından geçer | 10 | Frames to Video | kokpit kırılmaz, yaralanma yok; Leon ağız kadrajda | 1.LEON · 4.KOKPIT · 11.DRONE | G07 | ⬜ | — | — | — |
| C83 | Rhea portu hazırlayıp korunur | Medium Rhea behind the fixed blast rib, one glove already on the emergency socket's broad battery-power toggle; tether anchored. → Flip the one broad toggle, amber guide lamps brighten; she stays behind cover. | orta Rhea kaburga arkasında | — | 10 | Frames to Video | T01 eldiven ilk karede anahtarda; siper korunur; Rhea ağız kadrajda; T13 | 2.RHEA · 14.ISKELE · 15.ARACLAR | G07 | ⬜ | — | — | — |
| C84 | İkinci yanaşma yaklaşması | Side view: tug at left, bow collar aligned with the foundry emergency socket right, short gap, one clamp open. → Translate the tug rightward along the single docking axis until collars touch; clamp remains open in this shot. | yan dış | tug soldan sağa sokete | 10 | Frames to Video | temas son vuruşta, kelepçe açık kalır; Leon telsiz; T13 | 3.KESTREL · 14.ISKELE | G07 | ⬜ | — | — | — |
| C85 | Kurtarma bağlantısı kilitlenir | Close already-touching emergency collars, one broad hinged clamp open above its latch. → Rotate the one clamp shut and hold; no other parts move. | yakın yakalar | kelepçe kapanır | 10 | Frames to Video | T01 yakalar ilk karede temasta; Rhea telsiz; T13 | 14.ISKELE | G08 | ⬜ | — | — | — |
| C86 | İki kardeş yeniden birlikte | Wide tug cockpit: Leon left, Rhea already seated right, empty core harness, both helmets closed; foundry amber glow outside. → Rhea exhales and looks toward Leon; both remain seated. | geniş kokpit | Leon solda, Rhea sağda | 10 | Frames to Video | iki replik ağız kadrajda (Rhea → Leon); finalin duygusal merkezi; Rhea'nın geçişi kesmede | 1.LEON · 2.RHEA · 4.KOKPIT | G08 | ⬜ | — | — | — |
| C87 | Foundry bağlantısından ayrılma | Side tug/socket view: collar already unlatched, a thin separation gap, amber guides behind. → Translate the rigid tug backward clear of the socket; do not pull any tether or hose behind it. | yan dış | tug geri (sola) çekilir | 10 | Frames to Video | tether/hortum çekilmez (tether iskelede kaldı); Rhea telsiz; T13 | 3.KESTREL · 14.ISKELE | G08 | ⬜ | — | — | — |
| C88 | Yolcu gemisine çıkış komutu | Medium two-shot: Rhea glove already on the same wrist-link's broad hold toggle, Leon ready on controls; no readable display. → Rhea flips the one toggle to release the previously loaded exit course. | orta iki kişi | Leon solda, Rhea sağda | 10 | Frames to Video | T01 Rhea'nın eldiveni ilk karede anahtarda; iki replik ağız kadrajda (Rhea → Leon) | 1.LEON · 2.RHEA · 4.KOKPIT · 15.ARACLAR | G08 | ⬜ | — | — | — |
| C89 | Ark çıkışa ilerler | Wide: ark free of both gantry arms, nose toward fully open iris, blue rear engines bright; tug smaller behind and below. → Translate the one rigid ark forward toward the gate on a straight course; the tug holds position briefly. | geniş dış | ark soldan sağa kapıya | 10 | Frames to Video | rijit ark, düz rota; replik yok; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G08 | ⬜ | — | — | — |
| C90 | Tug ark'ın ardından hızlanır | Wide cockpit: ark rear engines visible ahead through canopy, both siblings seated, controls ready. → Leon advances the existing thrust control through one short arc; the forward view moves gently as the tug follows. | geniş kokpit | ark kanopide önde | 10 | Frames to Video | Leon telsiz (K13 15.10: arkadan) | 1.LEON · 2.RHEA · 4.KOKPIT · 5.FOUNDRY · 6.ARK | G08 | ⬜ | — | — | — |
| C91 | Büyük gemi kapıdan çıkar | Side-wide gate: ark already mostly beyond aperture, only stern engine section still inside; shutters fully open, mechanical catch engaged. → Move the rigid ark's stern clear of the gate. Preserve all hull blocks and the fixed aperture. | yan-geniş kapı | ark sağa, açıklıktan çıkar | 10 | Frames to Video | rijit gövde, sabit açıklık; replik yok; T13 | 5.FOUNDRY · 6.ARK | G08 | ⬜ | — | — | — |
| C92 | Tug da kurtulur; purge arkada kalır | Wide gate from outside: tug already at the outer lip, ark farther ahead; orange furnace glow behind blast ribs inside the foundry. → Move tug clear of the aperture while one contained purge exhaust pulse grows behind the fixed blast ribs, far from both ships. | geniş kapının dışından | tug dudaktan çıkar; purge arkada | 10 | Frames to Video | patlama/çöküş yok, tehlike geride; replik yok; T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G08 | ⬜ | — | — | — |
| C93 | Yolcuların güvenlik teyidi | Medium two-shot in cool starlight, unmarked wrist-link cyan; captured ark now ahead in free space. → Rhea checks the link and relaxes one shoulder; Leon steadies the controls. | orta iki kişi, soğuk yıldız ışığı | Leon solda, Rhea sağda; ark önde | 10 | Frames to Video | Rhea ağız kadrajda | 1.LEON · 2.RHEA · 4.KOKPIT · 6.ARK · 15.ARACLAR | G08 | ⬜ | — | — | — |
| C94 | Çalınan çekirdeğin son hâli | Close abandoned control-room cradle: the same spent scorched core remains latched, amber center dark, orange gate-catch lever down nearby. → Slow restrained push over the rigid inactive core, nothing explodes. | yakın terk edilmiş yuva | — | 10 | Frames to Video | patlama yok; sönük çekirdek aynı yuvada; Leon VO | 10.CEKIRDEK · 12.KONTROL_ODASI | G08 | ⬜ | — | — | — |
| C95 | Yeni ortaklık | Close two-shot: Leon left, Rhea right, calm faces inside closed visors; core harness empty, blue planet light. → Leon gives a small tired half-smile; Rhea meets his eyes. | yakın iki kişi | Leon solda, Rhea sağda | 10 | Frames to Video | iki replik ağız kadrajda (Leon → Rhea) | 1.LEON · 2.RHEA · 4.KOKPIT | G08 | ⬜ | — | — | — |
| C96 | Özgür iki gemi | Final extreme wide: liberated ivory ark and small salvage tug travel together away from the distant foundry, immense curved blue gas giant behind, no additional vessels. → Slow pullback preserves both rigid ships on the same safe course; no new threat or planet. | son aşırı geniş, yavaş geri çekilme | iki gemi birlikte foundry'den uzaklaşır | 10 | Frames to Video | yeni tehdit/gezegen/gemi yok; iki telsiz replik (kadrajda kimse yok); T13 | 3.KESTREL · 5.FOUNDRY · 6.ARK | G08 | ⬜ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE (96 × 10 s = 16:00).
  Ritim süreyle değil çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
Flow modu: Frames to Video · Ingredients to Video · Text to Video (yalnız kimliksiz çekim).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir". Model sesi: "ağız kadrajda" = konuşanın yüzü kadrajda (≤5 s), "telsiz" = konuşan kadraj dışı ya da yüzü görünmüyor.
Grup: PROMPTLAR/<Grup>.md (12 çekim). Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Zincir · Baş. karesi · Bitiş karesi: bu filmde zincir yok ("—"); sahneleme adımı açılmadı (plan her klibi ayrı kare olarak üretir).
DELTA BÜTÇESİ (her halka, Zk.n → Zk.n+1): aynı objektif · ışık · set │ en çok bir basit kamera
  hareketi │ özne yalnız ulaşabileceği mesafede │ kadraja nesne/kişi girip çıkmaz │ el-nesne
  teması değişmez │ durum değişimi küçük ve tek. Aşılırsa model iki kareyi eritir (morf).
```

### AÇILIŞ — ilk 30 saniye (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2 · plandan, Fable)

| Saniye | Çekim | Sorun ya da beklenmedik hareket | İnsan (beden · el · yüz) | Replik · ekran yazısı | Kapak bağı | Sesi kapalı okunur mu |
|---|:--:|---|---|---|---|:--:|
| 0-10 | C01 | dev beyaz ark iki kelepçe arasında tutsak; önde kepenkler kısmen kapalı, arkada büyüyen turuncu fırın ışığı; kamera yanal kayar | yok | R01 Leon VO 2,0 s'den (hook) · yazı yok | vaadin dünyası: ark + kapı + fırın (kapak tabanı aynı üçlü) | evet (tutsak gemi ve fırın görünür) |
| 10-20 | C02 | tug kokpitinden ark kanopiyi doldurur; Rhea gözünü ark'a kaldırır | iki yüz, şeffaf vizör | R02 "That ark is in the burn cradle." | — | evet (altyazıyla) |
| 20-30 | C03 | Leon'un kaskına yansıyan amber kapı ışığı; amaç söylenir | yüz ¾ | R03 "The spare core is in the foundry. The ark is our way in." | kapak anı parçası: Leon'un yüzü + amber kapı ışığı (kapak iki yüz + ark) | evet (altyazıyla) |

```
İlk 30 s'de yok: logo · "sunar" kartı · siyah ekran · karartmadan açılma · saf manzara · görüntüde yazı ·
  kalabalık · hızlı kamera · karmaşık el-nesne teması · kusurlu ama "gerekli" çekim.
Sapma: plan hook'u "ilk saniyede" ister → kılavuz "ilk 2 s insan sesi yok" ile çatışır; sahip "plan farklarını düzelterek başla" dedi → R01 2,0 s'den başlar.
C01 insan taşımaz ama saf manzara değildir: tutsak ark + kapanan kapı + fırın = sorun ilk karede (plan "büyük ölçekli olay görünür").
```

**SMOKE P18 ses kimliği (F5 birleştirme 15.10):** model sesi klipten klibe aynı kalmalı. İlk karşılaştırma klipleri:
- ağız kadrajda: Leon C03 · C07 · C11, Rhea C04 · C08 · C10;
- telsiz kalıbı: Rhea C02 · C06 · C13;
- voice-over: C01.

Ses kimliği kayarsa üretime geçilmez: §3 SES KİMLİĞİ cümlesi aynı kalır, aynı prompt yeniden denenir. Telsize çevrilen replikler (K13: R02 R13 R17 R19 R25 R26 R36 R37 R79 R89) §5 Kaynak sütununda.

## 5. REPLİKLER

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §11 "İngilizce diyalog kayıt listesi" + her klibin "İngilizce ses / diyalog" satırı BİREBİR (95 replik). Kaynak sahip kararıyla model sesi; saniye ve süre Fable tahmini (≈2,9 kelime/s). -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 2.0 | LEON | model sesi (voice-over) | HUMAN | We came to steal a power core. We left with a ship full of people. | 5.5 |
| R02 | C02 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | That ark is in the burn cradle. | 2.5 |
| R03 | C03 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | The spare core is in the foundry. The ark is our way in. | 5.0 |
| R04 | C04 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Maintenance berth. Then the loading bridge. | 2.5 |
| R05 | C06 | 7.5 | RHEA | model sesi (telsiz) | HUMAN | We're attached. | 1.0 |
| R06 | C07 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | No crew. No greeting. | 1.5 |
| R07 | C08 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Those storage units are drawing life-support power. | 2.5 |
| R08 | C09 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | They're sleepers. Still alive. | 1.5 |
| R09 | C10 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Four thousand stable life signs. | 2.0 |
| R10 | C11 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | We take the core, then open their clamps. | 3.0 |
| R11 | C11 | 5.0 | RHEA | model sesi (ağız kadrajda) | HUMAN | Then we take everyone. | 1.5 |
| R12 | C12 | 2.0 | RHEA | model sesi (telsiz) | HUMAN | We have until the purge reaches this berth. | 3.0 |
| R13 | C13 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | The core first. Then we separate the gate from its automation. | 4.0 |
| R14 | C14 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | And keep a way back. | 2.0 |
| R15 | C15 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Keep this for a sentry. Not for a door. | 3.5 |
| R16 | C16 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Security is still awake. | 1.5 |
| R17 | C17 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | Stay inside the pressure line. | 2.0 |
| R18 | C18 | 1.5 | LEON | model sesi (telsiz) | HUMAN | An emergency socket below us. Good to know. | 3.0 |
| R19 | C19 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | Gate power here. Clamp release beside it. | 2.5 |
| R20 | C20 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Two clamps. Releasing one won't free her. | 2.5 |
| R21 | C21 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | This catch holds the gate open, even if power fails. | 3.5 |
| R22 | C22 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | You know this place. | 1.5 |
| R23 | C22 | 3.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | I know machines. | 1.5 |
| R24 | C23 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | The contract core is in here. | 2.5 |
| R25 | C24 | 1.5 | LEON | model sesi (telsiz) | HUMAN | There's our fortune. | 1.5 |
| R26 | C24 | 3.5 | RHEA | model sesi (telsiz) | HUMAN | There's their chance. | 1.5 |
| R27 | C25 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | Release catch. | 1.0 |
| R28 | C26 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Careful. That's worth more than the tug. | 2.5 |
| R29 | C27 | 2.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | The core is secure. | 1.5 |
| R30 | C28 | 1.5 | LEON | model sesi (telsiz) | HUMAN | That woke the security grid. | 2.0 |
| R31 | C29 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Down. | 1.0 |
| R32 | C31 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Keep your visor down. | 1.5 |
| R33 | C33 | 2.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Local override is locked out. | 2.0 |
| R34 | C34 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | And the clamp motor has no feed. | 2.5 |
| R35 | C35 | 1.5 | LEON | model sesi (telsiz) | HUMAN | The way out is getting smaller. | 2.5 |
| R36 | C36 | 1.5 | LEON | model sesi (telsiz) | HUMAN | We can undock. The ark can't. | 2.5 |
| R37 | C36 | 4.5 | RHEA | model sesi (telsiz) | HUMAN | Then find another way. | 1.5 |
| R38 | C37 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | The gate drive has no power. The capture locks are still powered. | 4.0 |
| R39 | C38 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | How did a ship full of people become scrap? | 3.5 |
| R40 | C39 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | I wrote the original cargo classifier. | 2.5 |
| R41 | C40 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | It had a human-safety veto. Someone removed it. | 3.0 |
| R42 | C40 | 5.0 | LEON | model sesi (ağız kadrajda) | HUMAN | You knew the architecture. | 1.5 |
| R43 | C41 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | I didn't know what they'd done. Now I do. | 3.5 |
| R44 | C42 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | At Dione, you cut the tether with me on the other end. | 4.5 |
| R45 | C43 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | The ship was breaking apart. | 2.0 |
| R46 | C43 | 4.0 | RHEA | model sesi (ağız kadrajda) | HUMAN | I survived. The trust didn't. | 2.0 |
| R47 | C44 | 1.5 | LEON | model sesi (voice-over) | HUMAN | I'm not making that choice again. | 2.5 |
| R48 | C45 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | This core can force the gate open. The overload will consume it. | 4.5 |
| R49 | C46 | 2.0 | RHEA | model sesi (ağız kadrajda) | HUMAN | I feed the gate and release port. You take starboard from the ark. | 5.0 |
| R50 | C47 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | We lose the core. We take everyone. | 2.5 |
| R51 | C48 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | No one gets cut loose. | 2.0 |
| R52 | C49 | 1.5 | LEON | model sesi (telsiz) | HUMAN | I'm on the ark. Starboard release is still locked. | 3.5 |
| R53 | C50 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | I'll feed the captured bus. Keep main thrust off. | 3.5 |
| R54 | C51 | 3.0 | LEON | model sesi (telsiz) | HUMAN | Backup control is live. | 1.5 |
| R55 | C52 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | They're sealing the loading route. | 2.0 |
| R56 | C53 | 2.0 | RHEA | model sesi (ağız kadrajda) | HUMAN | I'm inside. Stay on your station. | 2.5 |
| R57 | C54 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | I'm here. | 1.0 |
| R58 | C55 | 4.0 | LEON | model sesi (ağız kadrajda) | HUMAN | Straight exit course loaded. Holding until release. | 2.5 |
| R59 | C56 | 2.5 | RHEA | model sesi (telsiz) | HUMAN | I've kept the route link. We can send her through from the tug. | 5.0 |
| R60 | C57 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Station-keep ready. Main burn waiting. | 2.0 |
| R61 | C58 | 5.0 | RHEA | model sesi (ağız kadrajda) | HUMAN | Core seated. | 1.0 |
| R62 | C60 | 3.5 | RHEA | model sesi (telsiz) | HUMAN | Gate feed on. | 1.5 |
| R63 | C61 | 1.5 | LEON | model sesi (telsiz) | HUMAN | I have clamp power. | 1.5 |
| R64 | C62 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | Gate drive is moving. | 1.5 |
| R65 | C63 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Clear aperture. Lock it before the core fails. | 3.0 |
| R66 | C64 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Mechanical catch. | 1.0 |
| R67 | C65 | 4.0 | RHEA | model sesi (telsiz) | HUMAN | Catch engaged. | 1.0 |
| R68 | C66 | 1.5 | LEON | model sesi (telsiz) | HUMAN | It'll hold without power. | 1.5 |
| R69 | C67 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | Port clamp releasing. | 1.5 |
| R70 | C69 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | The core is going. | 1.5 |
| R71 | C70 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Starboard motor live. | 1.5 |
| R72 | C71 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Starboard releasing. | 1.0 |
| R73 | C72 | 6.5 | LEON | model sesi (telsiz) | HUMAN | Both clear. Come back to the ark. | 2.5 |
| R74 | C73 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Gate is locked open. The bridge is still on purge control. | 4.0 |
| R75 | C75 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | The bridge is gone. | 1.5 |
| R76 | C76 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Get to the emergency socket. I'm coming back. | 3.0 |
| R77 | C77 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Socket ready. I can't hold this position forever. | 3.0 |
| R78 | C78 | 3.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Ark on hold. Exit course stays armed. | 2.5 |
| R79 | C79 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Not this time. | 1.5 |
| R80 | C82 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Keep your head behind the blast rib. | 2.5 |
| R81 | C83 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Emergency collar live. | 1.5 |
| R82 | C84 | 6.0 | LEON | model sesi (telsiz) | HUMAN | Contact. | 1.0 |
| R83 | C85 | 6.0 | RHEA | model sesi (telsiz) | HUMAN | Hard seal. | 1.0 |
| R84 | C86 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | You came back. | 1.5 |
| R85 | C86 | 3.5 | LEON | model sesi (ağız kadrajda) | HUMAN | We're not finished. | 1.5 |
| R86 | C87 | 1.5 | RHEA | model sesi (telsiz) | HUMAN | We're clear. I still have the ark link. | 3.0 |
| R87 | C88 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Sending the ark through. | 1.5 |
| R88 | C88 | 3.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Take everyone. | 1.0 |
| R89 | C90 | 1.5 | LEON | model sesi (telsiz) | HUMAN | Stay behind her hull. | 1.5 |
| R90 | C93 | 1.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | All four thousand sleeper signals stable. | 2.5 |
| R91 | C94 | 1.5 | LEON | model sesi (voice-over) | HUMAN | No core. No payday. | 1.5 |
| R92 | C95 | 1.5 | LEON | model sesi (ağız kadrajda) | HUMAN | Terrible salvage margin. | 1.5 |
| R93 | C95 | 3.5 | RHEA | model sesi (ağız kadrajda) | HUMAN | Good day to be thieves. | 2.0 |
| R94 | C96 | 2.0 | RHEA | model sesi (telsiz) | HUMAN | Where now? | 1.0 |
| R95 | C96 | 3.5 | LEON | model sesi (telsiz) | HUMAN | Somewhere they can wake up. | 2.0 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
        model sesi (telsiz | voice-over | ağız kadrajda) → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda
        üretir (sahip kararı 12.10.2026); ≤ 8 s (ağız kadrajda ≤ 5 s); klip sesi filme girer (timeline klip_sesi), kurgu kaydı yedek
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik
Bant dışı gerekçe: 95 replik > 70. Plan iki konuşan karakterin filmidir (üçüncü ses yok); replikler kısa (ortalama ≈5 kelime) ve 85 klibe yayılır,
  her biri tek eylem ya da tepkiye bağlı (plan §6 "replikler on saniyenin tümüne yayılmaz"). Sahip planı birebir korunur.
Konuşma ve ses profilleri: §3 SES KİMLİĞİ (diyalog-yazari açılmadı — sahip planı). Plan notu: "Offscreen", "comms" ve "VO" yeni karakter değildir.
Rakam yok: sayılar sözle yazılı ("Four thousand", "All four thousand") — dudak senkronu için (film_dogrula uyarısı).
```

## 6. SES PLANI — model sesi yalnız §5 replikleri için (Omni); ortam, efekt ve müzik kurguda

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §12 "Müzik ve ses yayı" (bölüm başına, birebir) + §6 "J/L ses geçişleri". F4 ses-tasarimcisi açılmadı (sahip planı); yatak ve geçiş tabloları Fable'ın plandan çevirisi, F8 kurgucu kesinleştirir. -->
| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| B1 · C01-C12 | Y1 · Y2 · Y3 · Y4 yatak · replikler klipten (model sesi) · Kozmik ölçek, düşük metalik ritim, ilk docking temas/kelepçe, hayatta kalanların yeşil ışıklarında müziğin incelmesi. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B2 · C13-C24 | Y1 · Y3 · Y5 · Y6 · Y7 yatak · replikler klipten (model sesi) · Kısa heist pulse'ları, köprü ortamı, case/çekirdek mekanik detayları. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B3 · C25-C36 | Y1 · Y2 · Y6 · Y7 yatak · replikler klipten (model sesi) · Kısa sentry atışı, siper etkisi, EMP'de dar ses kırılması; başarısız override'da gerilim. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B4 · C37-C48 | Y1 · Y2 · Y3 yatak · replikler klipten (model sesi) · Müzik geri çekilir; iki kişinin sözleri, nefes ve uzaktaki purge uğultusu öne çıkar. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B5 · C49-C60 | Y1 · Y6 · Y8 yatak · replikler klipten (model sesi) · Bölünen rotalarda kontrollü ritim; bridge darbesi, kapalı kapakta uzak etki, core yerleştirme. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B6 · C61-C72 | Y1 · Y6 · Y8 yatak · replikler klipten (model sesi) · Büyük kapı hareketinin düşük frekansı, mandalın kuru kilit sesi, iki clamp motoru; sönmeye başlayan core. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B7 · C73-C84 | Y1 · Y2 · Y5 · Y6 · Y8 · Y9 yatak · replikler klipten (model sesi) · Geri çekilen bridge'in mekanik sesi, nefes, rescue uçuşunda hızlanan ama replikleri örtmeyen ritim. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |
| B8 · C85-C96 | Y1 · Y2 · Y6 yatak · replikler klipten (model sesi) · İkinci docking, kısa rahatlama, ark motorlarının büyümesi, geçişte müziğin açılması; finalde sade iki karakter. | mekân değişiminde yatak çapraz 1 s, J/L 1 s | plan §12 |

```
Ortam: dış uzay (Y1: C01 C05-C06 C12 C18 C35 C44 C52 C57 C62 C68 C72 C74 C80-C81 C84-C85 C87 C89 C91-C92 C96) dış ses yok — plan "External-space action
  effects are cinematic sound design": efektler tasarım, gövdeden ya da kaskın içinden · iç hacimler (kokpit · koridor · kriyo · köprü içi · kontrol · kasa · komuta)
  hava taşır · iskele (Y9) vakum, ses kaskın içinden.
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]. Plan §15: konuşmalar telefon hoparlöründe anlaşılır olmalı.
Kayıt + efekt listesi: F4 açılırsa ODA/F4_ses-tasarimcisi_<n>.md; şimdilik kaynak plan §12 ve klip hareket cümleleri.
Model sesi: her replik taşıyan parça timeline'da klip_sesi: true, klip_kazanc_db −3…−6 (klibin kendi uğultusu yatağın altında kalır); yatak her zaman kurgudan.
Vakumda ses (T13, THE_MAYDAY_SEA kararı): Y1 dış kliplerde klip_sesi AÇILMAZ; replik varsa klibin sesi `ses` parçası olarak yalnız replik penceresinde
  (giris/cikis = replik ±0,5 s, solma 0,1) yerleşir, kalan süre Y1 yatağı.
```

<!-- 12.10.2026 sahip kararı: klipler arası keskin kesme ve kesmede komple değişen arka ses → uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md. Yatak mekân başına TEK dosya, klip sınırlarını aşar (timeline yataklar). -->
### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | dış uzay (vakum; tasarım) | C01 · C05-C06 · C12 · C18 · C35 · C44 · C52 · C57 · C62 · C68 · C72 · C74 · C80-C81 · C84-C85 · C87 · C89 · C91-C92 · C96 | low steady non-diegetic pressure tone with a faint continuous bed of suit-radio static, no rhythm, no engine roar | −20 LUFS | yatak_dis.wav |
| Y2 | tug kokpiti | C02-C04 · C36-C43 · C45-C47 · C79 · C82 · C86 · C88 · C90 · C93 · C95 | soft steady cabin ventilation hum, close dry acoustic, faint electrical bed, no rhythm | −18 LUFS | yatak_kokpit.wav |
| Y3 | ark koridoru | C07-C08 · C10-C11 · C13-C15 · C48 | low steady ship ventilation hum, large pressurized metal corridor, faint distant life-support pumps, no rhythm | −18 LUFS | yatak_koridor.wav |
| Y4 | kriyo salonu | C09 | deep steady refrigeration hum with a faint hiss of floor vapor, very large cold hall, no rhythm | −18 LUFS | yatak_kriyo.wav |
| Y5 | yükleme köprüsü (iç) | C16-C17 · C75 | thin pressurized tunnel hum, faint creak of rigid metal under load, no rhythm | −18 LUFS | yatak_kopru.wav |
| Y6 | kapı kontrol odası | C19-C22 · C33-C34 · C50 · C53 · C56 · C58-C61 · C64-C67 · C69 · C73 · C94 | deep industrial machinery hum through thick walls, steady electrical bed, no rhythm | −18 LUFS | yatak_kontrol.wav |
| Y7 | prototip kasası | C23-C32 | close low electrical hum of a sealed vault, faint steady ventilation, no rhythm | −18 LUFS | yatak_kasa.wav |
| Y8 | ark acil komutası | C49 · C51 · C54-C55 · C63 · C70-C71 · C76 · C78 | soft bridge ventilation and quiet steady console electronics, no rhythm | −18 LUFS | yatak_komuta.wav |
| Y9 | acil servis iskelesi (vakum; kask içi) | C77 · C83 | close breathing inside a sealed helmet over a low steady non-diegetic pressure tone, no rhythm | −20 LUFS | yatak_iskele.wav |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

<!-- Fable taslağı plandan (13.10.2026): plan geçiş türü yazmaz ("J/L ses geçişleriyle diyalog bir sonraki görüntüye taşınabilir", §6) → bütün kesmeler kesme, yalnız final C95→C96 karışım (≤ ¼ kuralı içinde). Kurgucu F8'de kareler.py dikis ölçümüyle kesinleştirir. -->
| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C02→C03 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C03→C04 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C04→C05 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C05→C06 | kesme | Y1 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C06→C07 | kesme | Y1→Y3 çapraz 1 s; J 1 s | mekân değişimi |
| C07→C08 | kesme | Y3 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C08→C09 | kesme | Y3→Y4 çapraz 1 s; J 1 s | mekân değişimi |
| C09→C10 | kesme | Y4→Y3 çapraz 1 s; J 1 s | mekân değişimi |
| C10→C11 | kesme | Y3 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C11→C12 | kesme | Y3→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C12→C13 | kesme | Y1→Y3 çapraz 1 s; J 1 s | mekân değişimi |
| C13→C14 | kesme | Y3 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C14→C15 | kesme | Y3 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C15→C16 | kesme | Y3→Y5 çapraz 1 s; J 1 s | mekân değişimi |
| C16→C17 | kesme | Y5 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C17→C18 | kesme | Y5→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C18→C19 | kesme | Y1→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C19→C20 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C20→C21 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C21→C22 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C22→C23 | kesme | Y6→Y7 çapraz 1 s; J 1 s | mekân değişimi |
| C23→C24 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C24→C25 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C25→C26 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C26→C27 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C27→C28 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C28→C29 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C29→C30 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C30→C31 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C31→C32 | kesme | Y7 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C32→C33 | kesme | Y7→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C33→C34 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C34→C35 | kesme | Y6→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C35→C36 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C36→C37 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C37→C38 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C38→C39 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C39→C40 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C40→C41 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C41→C42 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C42→C43 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C43→C44 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C44→C45 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C45→C46 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C46→C47 | kesme | Y2 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C47→C48 | kesme | Y2→Y3 çapraz 1 s; J 1 s | mekân değişimi |
| C48→C49 | kesme | Y3→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C49→C50 | kesme | Y8→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C50→C51 | kesme | Y6→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C51→C52 | kesme | Y8→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C52→C53 | kesme | Y1→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C53→C54 | kesme | Y6→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C54→C55 | kesme | Y8 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C55→C56 | kesme | Y8→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C56→C57 | kesme | Y6→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C57→C58 | kesme | Y1→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C58→C59 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C59→C60 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C60→C61 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C61→C62 | kesme | Y6→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C62→C63 | kesme | Y1→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C63→C64 | kesme | Y8→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C64→C65 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C65→C66 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C66→C67 | kesme | Y6 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C67→C68 | kesme | Y6→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C68→C69 | kesme | Y1→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C69→C70 | kesme | Y6→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C70→C71 | kesme | Y8 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C71→C72 | kesme | Y8→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C72→C73 | kesme | Y1→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C73→C74 | kesme | Y6→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C74→C75 | kesme | Y1→Y5 çapraz 1 s; J 1 s | mekân değişimi |
| C75→C76 | kesme | Y5→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C76→C77 | kesme | Y8→Y9 çapraz 1 s; J 1 s | mekân değişimi |
| C77→C78 | kesme | Y9→Y8 çapraz 1 s; J 1 s | mekân değişimi |
| C78→C79 | kesme | Y8→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C79→C80 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C80→C81 | kesme | Y1 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C81→C82 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C82→C83 | kesme | Y2→Y9 çapraz 1 s; J 1 s | mekân değişimi |
| C83→C84 | kesme | Y9→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C84→C85 | kesme | Y1 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C85→C86 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C86→C87 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C87→C88 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C88→C89 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C89→C90 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C90→C91 | kesme | Y2→Y1 çapraz 1 s; J 1 s | mekân değişimi |
| C91→C92 | kesme | Y1 sürer | aynı mekân; ölçek/açı farkı F5'te denetlenir |
| C92→C93 | kesme | Y1→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C93→C94 | kesme | Y2→Y6 çapraz 1 s; J 1 s | mekân değişimi |
| C94→C95 | kesme | Y6→Y2 çapraz 1 s; J 1 s | mekân değişimi |
| C95→C96 | karisim 0,6 | Y2→Y1 çapraz 1,5 s; müzik açılır | final: kokpitten özgür uzaya açılma (plan K96 "finalde sade") |

## 7. MÜZİK PLANI

<!-- kaynak: THE_FURNACE_GATE_16MIN_96_CLIPS.md §12 "Müzik ve ses yayı" + "Orijinal müzik taslak promptu" birebir. F4 besteci açılmadı; F8'de gerçek kesme noktalarıyla kesinleşir. -->
```
OKUMA        İzleyici bu filmi endüstriyel ölçekte bir soygunun kurtarmaya dönüşmesi olarak okumalı: tehlike dev makine, kalp iki kardeşin güveni (plan §1 · §12).
MÜZİKSİZ     06:00–08:00 (B4) müzik geri çekilir; iki kişinin sözleri, nefes ve uzak purge uğultusu öne çıkar (plan) · kriyo salonunda yeşil ışıklarla müzik incelir (C09).
VURUŞ/SUSMA  00:00–02:00 kozmik ölçek, düşük metalik ritim, ilk yanaşma teması · 02:00–04:00 kısa heist nabızları · 04:00–06:00 drone atışı, EMP'de dar ses kırılması,
             başarısız override'da gerilim · 08:00–10:00 bölünen rotalarda kontrollü ritim · 10:00–12:00 kapının düşük frekansı, mandalın kuru kilidi, iki kelepçe motoru ·
             12:00–14:00 geri çekilen köprü, kurtarma uçuşunda hızlanan ama replikleri örtmeyen ritim · 14:00–16:00 ikinci yanaşma, kısa rahatlama, kapı geçişinde müzik açılır;
             finalde sade iki karakter — faz 8'de gerçek kesme noktalarıyla kesinleşir.
FLOW MUSIC   faz 8: ODA/F8_besteci_<n>.md. Plan notu: tek araçtan kusursuz 16 dakikalık çıkış ya da klip saniyelerine otomatik eşleme varsayılmaz; sekiz bölüm ayrı üretilip kurguda yerleşir.
```

<!-- 12.10.2026 sahip kararı (her filmde müzik promptu §7'de): planın "Orijinal müzik taslak promptu" birebir, F4 taslağı sayılır; F8'de besteci gerçek kesme noktalarıyla kesin sürümü altına yazar. -->
### MÜZİK PROMPTU — Flow Music'e yapıştırılır (plan taslağı, 13.10.2026)
```text
Original cinematic science-fiction heist and rescue score, structured as eight editable two-minute sections for a sixteen-minute film. Restrained low strings, metallic percussion, sub-bass machinery pressure and sparse warm synth harmonics. Begin with dangerous industrial scale and measured confidence; deepen into discovery of living passengers. Use short controlled tension for sentry action, thin the arrangement for two estranged adult siblings' confession, build a precise pulse for parallel gate and clamp work, then drive an urgent rescue flight. Finish with a restrained hopeful release as two ships escape. No vocals, no recognizable melody from an existing film. Leave space for concise radio dialogue and provide clean transitions; final scene timing is set in edit.
```
