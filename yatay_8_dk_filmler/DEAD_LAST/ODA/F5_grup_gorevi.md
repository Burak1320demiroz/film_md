# F5 · G02-G06 görev metni (goruntu-yonetmeni, tur 1 · 20.10.2026)

Faz 5, tur 1. Film: `yatay_8_dk_filmler/DEAD_LAST` (repo kökü `/Users/dai/github/apex_md/film_md`).

**Girdiler**
- Çekim listesi: `FILM.md` §4, altındaki notlar bloğu dahil.
- Kimlik tablosu: `FILM.md` §3, `### KİMLİK CÜMLELERİ` dahil.
- Replikler: `FILM.md` §5. Kaynak ve saniye sütunları belirleyicidir.
- Örnek grup: `PROMPTLAR/G01.md`. Kimlik, kabin, ışık ve ortak görünüm cümlelerini oradan **birebir** al. Dosya düzeni de onunki.

**Plan.** Film sahibin hazır planından yapılıyor: `DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md`. Plandan dışarı çıkılmaz.

**Yazım kuralı:** `ODA/F5_yazim_karari.md`. Bu gruplardaki bütün çekimler "B" türüdür:
- Her çekim, plan tablosundaki satırın İngilizcesidir.
- Olay sütununun ve görsel devamlılık sütununun her cümlesi promptta bir karşılık bulur.
- Yeni olay, nesne, ışık ya da taraf eklenmez.

**Genel kurallar.** `ODA/F5_fable_birlestirme_1.md` KABUL K3-K9 her grupta geçerlidir:
- Vuruş sınırları §5 saniyelerine oturur.
- Dialogue bloğuna **yalnız** §5'te "ağız kadrajda" yazan satırlar girer. Telsiz ve makine satırları kurguda eklenir; `not` satırına yazılır.
- Kimlik sözcükleri birebir kullanılır, eş anlamlı yazılmaz.
- Her çekimde tek kamera hareketi olur. Sayılan araçların hepsi kadrajda kalır.
- Needle kabin cümlesi ve Thren kabin cümlesi G01'deki gibi birebir yazılır.
- Fang, Needle'ın solundadır (aracın kendi yönüne göre).

**Hasar ve referans durumu:**
- Needle C11-C48 arasında Reference 20'dir: sol ön fren kanadının ucu eksik.
- Fang C15-C48 arasında Reference 21'dir: sağ arka motoru karanlık.
- Bastion C30-C48 arasında Reference 22'dir: sağ motoru karanlık. C29'da hasarlanır.
- Hücreler plan "Hasar ve nesne devamlılığı" tablosuna göre durur.
- Plan pilotları: C16 (G02) ve C41 (G06).
- G06'ya planın C41 yedeği eklenir. Yedek, aynı 10 s birim içinde üç kaynak çekimden oluşur: sol kilit açılması, sağ kilit açılması, genel görünüm. `## C41Y` bloğu olarak yazılır; dosya adları `kare/ara/C41_y1-3.png` ve `ham/C41_d3-d5.mp4`.

**Uzunluk:**
- Görsel 2.000-3.200 karakter.
- Video 1.000-1.500 karakter.
- Tavan 4.300 karakter.

**Çalışma biçimi.** Verimli çalış: okumayı bu dosyalarla sınırla ve dosyayı birkaç Write/Edit çağrısında yaz.

**Kontrol.** Bitince repo kökünden şunu koş:

```
python3 uretim_hatti/araclar/film_dogrula.py yatay_8_dk_filmler/DEAD_LAST --bolum prompt
```

Kendi çekimlerinde hata kalmasın. Bash yoksa bu adımı atla ve 8 SORU'da belirt.

**Çıktı:** `PROMPTLAR/<GRUP>.md`. İçinde promptlar, FLOW İŞ EMRİ ve `## 8 SORU` tablosu bulunur; tabloda "Görsel kr · Video kr" sütunu olur. Yalnız bu dosyaya yaz. Bitince kısa raporu SubagentHandback ile ver.
