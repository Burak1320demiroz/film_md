# ✅ TEMA VE AÇI KAPILARI — UYGULAMA KAYDI

> **Durum (01.09.2026 · KAPANDI):** A · B · C · D fazları UYGULANDI.
> **E fazı DEVREDİLDİ** → `TODO_DERS_KILAVUZ_QA_KAPILARI.md` Faz 1.
> Gerekçe: E'nin istediği şey (pilot film + mod D geri beslemesi) yeni
> kaydın Faz 1'iyle AYNI iştir; iki dosyada iki ayrı kutu tutmak, ikisinin
> de sahipsiz kalmasıdır. Bu dosya artık TARİHSEL KAYITTIR — A-D fazlarının
> ne yaptığı burada durur, açık iş burada TUTULMAZ.
>
> **Teşhis neydi:** Tema ve kamera-açısı kuralları 22.08.2026'da yazıldı
> (`TEMA_MUHENDISLIGI` · `KAMERA_ACISI_PSIKOLOJISI` · `ACI_YAYI_VE_SEKANS`)
> ve dört gün boyunca **hiçbir kapıda ölçülmedi**. Sistem neyi ölçüyorsa onu
> optimize etti: kesmeyi ve fiziği ölçüyordu, temayı ve açıyı değil.
> Kamera monotonluğu bir kural eksikliği değil, lockoff kararının sahneler
> ARASINA sessizce genellenmesiydi.

---

## 📊 ÖNCE / SONRA

```
                                  ÖNCE (26.08 sabahı)        SONRA
tema denetimi (betik)             0                          2 denetim
açı denetimi (betik)              0                          3 denetim
plan öncesi listede tema/açı      0 madde / 12               2 madde / 14
QA_SPEC'te tema + kurulum         0/8 dosyada ikisi birden   8/8
kurulum envanteri (QA rubriği)    hiçbir mercekte            ② DEVAMLILIK ölçüm satırı
ÜÇ KAPI akışta                    okuma listesinde           §6 adım 0,5
tema dağılımı sayımı              yok                        sayac.sh 🎭 bloğu
```

**Kapının ilk taraması (107 dosya, yeni denetimler):**

```
61  ⛔ TEMA satırı yok                    ← kapı açılmadan önceki durumun ölçüsü
45  ·  kurulum sayısı üst bandın üstünde  (gözlem — yatay filmlerin örüntüsü)
43  ⚠️ açı TİPİ < 3                       ← ASIL BULGU
22  ⚠️ açı hiç yazılmamış (§6 sözlüğü yok)
16  ⚠️ tema < 3 sahne indeksi
14  ⛔/⚠️ ardışık iki sahne aynı kurulum
 8  ⚠️ kurulum çeşitliliği bandın altında
```

⭐ **En öğretici sonuç iki sayının AYRIŞMASI:** dikey shorts az kurulum +
az açı tipi üretiyor; yatay filmler ÇOK kurulum ama yine az açı tipi
(THE ROSE COAT: 13 sahne · 13 kurulum · **2 açı tipi**). Yani depo ölçek
ve mesafe çeşitlendiriyor, AÇI çeşitlendirmiyor. Tek sayıyla bakılsa bu
görünmezdi.

---

## ✅ A — TASARIM KARARI DARALTILDI (klip içi ↔ sahneler arası)

- [x] `02_RISK_KARTLARI.md` KART 8 → "⛔ KAPSAM — BU KARAR KLİP İÇİDİR"
      bloğu + risk toplamı satırına kapsam uyarısı
- [x] `03_PLAN_ONCESI_KONTROL_LISTESI.md` D maddesi → kapsam cümlesi
- [x] `01_DERS_ETKINLIK_RAPORU.md` §5 → kapsam bloğu + **iki sayı
      ayrıştırıldı**: `3→8` ardışık sıçrama, `2→8` tablo min→max
      (ikisi de doğru, aynı şey değil — artık hangisi olduğu yazılı)
- [x] Risk paydası düzeltildi: 12 soru listeleniyordu, payda gövdede
      `/9` özette `/8` yazıyordu → `/12` + kalibrasyon uyarısı
      (5+ eşiği 9 soruluyken ölçülmüştü, korundu)

⛔ **Lockoff GERİ ALINMADI.** Klip içi lockoff (AGENTS §8'in üç kararından
biri) aynen duruyor. Değişen tek şey: sahneler ARASI kurulum değişimi
karardan muaf ve zorunlu — sahneler zaten ayrı kliplerde üretiliyor,
teknik riski sıfır (Slow Stone dersi).

## ✅ B — BETİĞE DÖRT DENETİM (`prompt_kontrol.py`)

- [x] **⑩ Kurulum çeşitliliği** — imza: lens + yükseklik + mesafe + ölçek
      + açı tipi. Ardışık ikili aynıysa BLOCK (zengin imza) / FIX (ince
      imza) · kurulum sayısı §4 bandının altındaysa FIX
- [x] **⑪ Açı sözlüğü** — KAMERA_ACISI §2'nin sekizlisi, desenler §6
      reçete sözcüklerinden. 6+ sahnede <3 tip → FIX
- [x] **⑫ Abartı eşiği** — dutch ≥35° BLOCK · kamera 45°+ yukarı pitch
      BLOCK · 45-60° aşağı pitch FIX
- [x] **⑬ Tema kapısı** — TEMA satırı yoksa BLOCK (dosyada + klasör
      komşularında arar) · <3 sahne indeksi varsa FIX
- [x] **Kalibrasyon: 107 dosya · 5 yanlış-pozitif sınıfı bulundu ve kapatıldı**

```
① "dish tilted at 70 degrees"  → çanak anten eğimi kamera eğimi sanıldı
② "angled 60 degrees to frame left" → karakterin gövde yönü kamera pitch'i sanıldı
③ [^.;] penceresi ondalık sayıda kopuyordu ("camera height 0.50 metres,
   pitched up 55 degrees") — GERÇEK bulgu kayboluyordu
④ "locked off at 12 metres" imzadan düşüyordu → 12 m ve 5 m'deki iki sahne
   "aynı kurulum" göründü, iki film haksız BLOCK yedi
⑤ tek çekimin ikiye bölünmüş hâli ("continues the previous clip from its
   exact last frame") monotonluk sanıldı → DEVAM_KLİBİ muafiyeti eklendi
⑥ "TEMAS:" (dokunma) tema beyanı sanıldı → TEMA'dan sonra harf gelemez
```

- [x] `PROMPT_QA_CRITIQUE_PROMPT.md` → yeni kategori 6 "AÇI VURUŞLA
      EŞLEŞİYOR MU" (betiğin ölçtüğü SAYININ anlam yarısı)

## ✅ C — KAPILAR

- [x] **C.1** `03_PLAN_ONCESI` → **B3 tema indeksi** + **B4 açı yayı**
      maddeleri · özet bloğu · KAYNAK tablosu · 12→14 (atıflar güncellendi:
      AGENTS §1 + kart A, KILAVUZ_REHBERI §6 adım 2.5)
      ⚠️ Film dosyalarındaki "12 madde" imzalarına DOKUNULMADI — onlar
      tarihsel kayıt, o filmler 12 maddeyle denetlendi
- [x] **C.2** QA_SPEC şablonu (D117 eki) → THEME + THEME SCENES +
      SETUP SEQUENCE + ANGLE ARC zorunlu; alanın yeri blok harfiyle değil
      MERCEKLE tarif ediliyor (harfler dosyadan dosyaya kayıyordu)
      → **8 SPEC dosyasının 8'i tamamlandı** (3'üne tema, 5'ine kurulum)
- [x] **C.3** `2_DEVAMLILIK` → STEP 1a sahne envanterine "Camera setup"
      sütunu + künyeye **SETUP INVENTORY ölçüm satırı** (skor değil ölçüm)
      + lockoff koruması gövdeye yazıldı
      ⚠️ Kategori 13'e YAZILMADI: o Çehov'un tüfeği (nesne kurulumu),
      kamera kurulumu değil. 1_KARE'ye de yazılmadı — kendi kapsam testi
      film-boyu bulguyu yapısal olarak dışlıyor
- [x] **C.4** `KILAVUZ_REHBERI` §6 → **adım 0,5 KONSEPT KAPISI** (ONERME §4
      ÜÇ KAPI artık numaralı adım; okuma listesi kapı değildir)
- [x] **C.5** `AGENTS.md` kart A → tema satırı + sahne-kurulum dizisi adresleri
- [x] Kart G defteri: `CALISTIRMA_KAYITLARI.md` → rubrik yaması + kardeş
      tarama kaydı (ders YAZILMADI — AGENTS §8: kapı kurma, kural ekleme değil)

## ✅ D — TEMA ÇEŞİTLİLİĞİ

- [x] **§3c TAKAS KALIBI MORATORYUMU** — yazılı temaların **beşi** aynı
      kalıbın varyasyonu çıktı ("X için Y feda edilir"). Kural: arka arkaya
      en çok 2 film; üçüncüsü §3'ten kullanılmamış tema seçer
- [x] **§3b DEPODA DOĞMUŞ ETİKETLER** — TANIKLIK ve **ZEMİN** (ikincisi
      teşhiste yoktu) tabloya ⏸️ ADAY olarak kaydedildi.
      ⛔ Pazar/kuşak sütunları BOŞ bırakıldı: o tablo depoda bulunmayan bir
      araştırma raporundan geliyor, tahminle doldurmak tablonun tamamını
      tahmin seviyesine indirirdi. Tam satır olmanın yolu kart Y'dir
- [x] **D.3** `sayac.sh` → 🎭 TEMA DAĞILIMI bloğu (elle tablo yok, kural ①)

---

## ➡️ E — PİLOT + GERİ BESLEME · **DEVREDİLDİ**

Dört madde de `TODO_DERS_KILAVUZ_QA_KAPILARI.md` **Faz 1**'e taşındı
(01.09.2026). Orada sahibi var, burada yoktu.

- [→] **E.1** pilot film · devir · ⚠️ **taşınırken bir hata düzeltildi:**
      bu madde "hiç kullanılmamış tema" diye beş tema sayıyordu
      (Yalnızlık · Zaman · Kimlik · İnsan-makine · İlk temas). İkisi
      artık kullanılıyor — `sayac.sh` 01.09: **YALNIZLIK 3** (THE THIN
      ROOF · THE COLD WELD · +1), **İNSAN-MAKİNE 1**. Gerçekten
      kullanılmamış olanlar: **ZAMAN · KİMLİK · İLK TEMAS**.
      Ders: elle yazılmış "hiç kullanılmamış" listesi dört günde bayatlar
      — sayıyı `sayac.sh` verir, kutu vermez [kural ①].
- [→] **E.2** mod D koşusu · devir · depoda mod D sayısı **hâlâ 0**
- [→] **E.3** kıyas (kural ⑥: <1,5 puan farkı GÜRÜLTÜ) · devir
- [→] **E.4** sonuca göre revizyon; TEKRARLARSA ders (kart Y) · devir

### 📌 Devirle birlikte taşınan uyarılar

```
· THE NEAR PASS üretilmedi, 6/6 sahnesi ALT AÇI (1 tip) — pilot o film
  olacaksa açı yayı ÖNCE düzeltilir; SPEC'inde 🚨 AÇIK MADDE olarak duruyor.
· THE OPEN SEAM'in doruğu (S4) açısız yazılmış; ACI_YAYI §9 doruğa en
  yüksek kontrast sıçramasını şart koşar.
· ⏸️ THE HELD HEAT ve THE LAST SPAN 26.08.2026'da zombi türüyle kaldırıldı
  — yay şablonu olarak kullanılamaz. Pilotun hedefi ≥3 açı tipidir.
```

---

## 🔎 DOĞRULAMA (bu kayıt kapanmadan koşulur)

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh          # 🎭 bloğu basıyor mu
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
        dikey_shorts_filmler/THE_BRIGHT_TETHER/       # açı TİPİ 2 → FIX
git status                                            # commit'i SAHİBİ atar [AGENTS §5]
```

> ⚠️ 4 dosya hâlâ başlık standardı dışında (BREATHING_STORM · DEEP_PRESSURE ·
> ETERNAL_ENGINE · PULSE) — bu çalışmadan önce de öyleydi, AGENTS §6'da kayıtlı.
