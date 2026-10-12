# F3b · denetci (faz 3 kapısı, ADIM sahneleme · kısa kapanış) — THE_WRONG_BURN

> Girdi: KABUL_LISTELERI Ö + F3b · ODA/F3b_sahneleyici_1.md · SAHNELEME.md · FILM.md §4 zincir sütunları · DURUM.md · NOTLAR.md · film_dogrula --bolum cekim sahneleme. Ajanın cevabı aynen (Fable kaydı, 09.10.2026).

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** zorunlu eleştiriler | ✅ | Kısa kapanışın koşulları sağlanıyor. Yönetmen zincir adayı yazmadı: `ODA/F3_yonetmen_4.md:58` "ZİNCİR ADAYI: yok". Sahneleyici de zincir önermedi: `ODA/F3b_sahneleyici_1.md:6` "KARAR 0 zincir". Bu durumda `sahneleme-odasi/SKILL.md:25-26` adımı kısa kapatıyor ve `:51` "Zincir yoksa 2" çağrı diyor. Bu fazda zorunlu eleştirmen yok. Yazar dosyası yerinde: `ODA/F3b_sahneleyici_1.md` (git status'ta `??`). |
| Ö2 **M** GİRDİ satırı, "EKSİK" yok | ✅ | `F3b_sahneleyici_1.md:4-5` "GİRDİ FILM.md §1 · §4 (F3_yonetmen_4, …) · KLIP_SURESI ölçülmedi · yönetmen ZİNCİR ADAYI: yok …". Satırda "EKSİK" geçmiyor. |
| Ö3 ÖLÜMCÜL/CİDDİ bulgulara cevap | ✅ (boş) | Bu adımda eleştiri yok, yani cevaplanacak bulgu da yok. `F3b_sahneleyici_1.md:10` "REVİZYON tur 1, cevaplanacak bulgu yok." |
| Ö4 KABUL'ler uygulandı mı | ✅ (KABUL yok, yerleştirme birebir) | Bu adımda KABUL yok. Yerleştirmeyi kontrol ettim: `SAHNELEME.md` §1 (23-48), §2/2b (50-80), §4/4b (94-120) ve §5 (122-148), `F3b_sahneleyici_1.md` 15-128 ile satır satır aynı. Şablona göre tek ek §3'teki Fable yorumu (`SAHNELEME.md:84-89`). "§4 SÜTUNLARI" (sahneleyici 136-149, 12/12 "—") `FILM.md:99-110` son üç sütunda 12/12 "—" olarak duruyor. |
| Ö5 RED gerekçeleri | ✅ (boş) | RED yok. |
| Ö6 açık ÖLÜMCÜL yok | ✅ | `ODA/DURUM.md:19-25` AÇIK ÖLÜMCÜL tablosunda faz 3 sahneleme satırı yok. Faz 3'ün tek ÖLÜMCÜL'ü olan B1 "✅ tur 2'de kapandı". |
| Ö7 **M** DURUM.md güncel | ✅ | `DURUM.md:8-14`: FAZ 3 · ADIM sahneleme · TUR 1 · AJAN_CAGRI 33/50 · SIRADAKI "sahneleyici ✅ … → denetci (Ö + F3b) → Fable → FAZ 4". Sayacı ayrıca saydım: `NOTLAR.md` AJAN GÜNLÜĞÜ'nde 34 satır var (82-115). Bunlardan biri sayılmayan yeniden çağrı (satır 95), geriye 33 kalıyor; son satır F3b/1 sahneleyici (115). |
| F3b.1 **M** film_dogrula cekim sahneleme | ✅ | `python3 uretim_hatti/araclar/film_dogrula.py yatay_2_dk_filmler/THE_WRONG_BURN --bolum cekim sahneleme` çıktısı: "film: … · bölüm: cekim sahneleme · çekim: 12 / ✅ yapı geçerli", EXIT=0. Bilmen gereken bir şey var: `film_dogrula.py` içindeki `sahneleme()` zincir yoksa hemen dönüyor (`if not zincirler: return`). Yani bu filmde zincir alt maddeleri (halka, dikiş, delta, KLIP_SURESI) hiç sınanmadı. Bu yüzden zincir yokken F3b.6'yı elle denetledim, aşağıda. |
| F3b.2 zincir gerekçesi / H01 | ✅ (uygulanmaz) | `SAHNELEME.md:25-26` §1 tablosu boş, 28-48'de "Zincir yok" gerekçesi var. |
| F3b.3 teknik-danisman delta/morf ÖLÜMCÜL | ✅ (uygulanmaz) | Halka yok (`SAHNELEME.md:99` "Zincir yok, dolayısıyla halka da yok"). Kısa kapanışta teknik-danisman çağrılmıyor (SKILL.md:25-26, 51). Açık bir teknik bulgu da yok. |
| F3b.4 mekan-haritacisi mesafe/süre/180° | ✅ (uygulanmaz) | §3 boş ve gerekçesi yazılı: `SAHNELEME.md:84-85` "zincir yok (§1) → mekan-haritacisi çağrılmadı … zincir açılırsa bu bölüm o turda doldurulur". |
| F3b.5 izleyici anahtar kare akışı | ✅ (uygulanmaz) | Zk anahtar karesi yok: `SAHNELEME.md:57` "Zincir yok, dolayısıyla Zk kare de yok." |
| F3b.6 zincir yoksa §5'te bütün çekimler gerekçeli | ✅ | `SAHNELEME.md:126-139` §5 tablosunda C01'den C12'ye 12 satır var ve her birinde dikişe özgü bir gerekçe yazılı. Örnek: C05 "C05/C06 kesmesi saklı bir durum değişimi taşıyor: dönüşün kalanı"; C12 "Final. Çıkış dikişi yok." |

Notlar (kapıyı bloklamıyor; bunlar içerik önerisi değil, süreç gözlemi):
1. **Kararı bekleyen ama kimseye gitmeyen sorular var.** Sahneleyici iki soruyu bu adımda hiç çağrılmayan ajanlara yöneltti, ama hiçbir dosyada bunlar için bir karar kaydı yok (`NOTLAR.md` KARARLAR 61-74, `DURUM.md`):
   - C10 fon kayması, (i) ya da (ii): `SAHNELEME.md:109` "yönetmen ve mekan-haritacisi için; … karar sizin".
   - C07 bitiş karesi olacak mı: `SAHNELEME.md:69` "Karar yönetmen + teknik-danisman".

   Buna bağlı olarak `FILM.md:108` C10 satırında çelişki duruyor. "Ekranda görünen" sütunu "fon … çekim boyunca birkaç derece kayıyor" diyor, Risk sütunu ise "sağ kol, bacaklar, ip ve fon aynı" diyor. Bu çelişki F5'e taşınacak; kimin karar vereceği şu an hiçbir yerde yazılı değil.
2. `DURUM.md` FAZ GÜNLÜĞÜ'nde (43-57) sahneleyici çağrısı için bir F3b/1 satırı yok. En son kayıt "ADIM sahneleme açıldı (kısa kapanış bekliyor)". Ö7'nin zorunlu dört alanı tam olduğu için bunu ❌ saymadım.
3. Daha önce de söylediğim gibi, zincir yokken F3b.1'in mekanik kontrolü fiilen hiçbir şeyi sınamıyor (`sahneleme()` erken dönüyor). §5'in kapsamı da mekanik olarak sınanmıyor.

```
FAZ 3 KAPISI (ADIM sahneleme) · THE_WRONG_BURN
MEKANİK ❌   yok
YARGI ❌     yok
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: yok)
```

---

## Fable kararı (09.10.2026)

**F3b (ADIM sahneleme) KAPANDI.** Aşılan kapı yok. Faz 3 bütünüyle kapandı → `FAZ 4 · ADIM —`.

Denetci notları:
1. **Kararı bekleyen iki soru → F5'e adresli gidiyor** (NOTLAR KARARLAR):
   - **C10 fon kayması:** FILM §4 C10 satırının Risk hücresi zaten "iki karenin farkı yalnız sol kol; … fon aynı" diyor. Fable: C10 iki kareli (başlangıç + bitiş) üretilirse sahneleyici (i) geçerlidir: bitiş karesi başlangıçla aynı fonla üretilir, video promptunda fon kayması yazılmaz. Yalnız başlangıç karesiyle üretilirse §4 "Ekranda görünen" metni (yavaş kayma) olduğu gibi kalır. Karar F5'te goruntu-yonetmeni'nin iş emrinde iki satır olarak görünür; teknik-danisman F5 eleştirmeni olarak sınar. FILM §4 C10 metni değişmez (yönetmen eseri; çelişki F5 iş emrinde çözülür, F5 girdi notu).
   - **C07 bitiş karesi:** yönetmen istemedi (§5.3 yalnız C08 zorunlu, C10 önerilir). Varsayılan: C07 yalnız başlangıç karesiyle. Sahneleyici'nin §2b tarifi F5'te goruntu-yonetmeni'ne **seçenek** olarak verilir; teknik-danisman F5'te "el açılması kadrajda okunur mu" sorusuyla karar verir. Fable içerik seçmez.
2. **FAZ GÜNLÜĞÜ F3b satırı** → bu kapanışla yazıldı (DURUM).
3. **film_dogrula zincir yokken §5 kapsamını sınamıyor** → hat gözlemi, NOTLAR'a; araç değişikliği sahibin kararı (yeni-film hattı dosyası, bu film içinde dokunulmaz). Sahip listesine girdi.

F4 girdisi (sahneleyici'den): H01 kuyrukları (7-10 s süren hareket) kurgu ve sesle kapanır: C05 sessizlik · C07 hışırtı · C10 nefes ve söz · C12 nefes (SAHNELEME §5 okuma notları).
