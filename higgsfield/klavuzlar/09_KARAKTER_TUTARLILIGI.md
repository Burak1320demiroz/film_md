# 🧬 KARAKTER TUTARLILIĞI — SOUL ID

> **Kaynak:** Kullanıcının hazırladığı araştırma raporu — *"Higgsfield AI
> Ekosisteminde Hatasız Görüntü ve Video Üretimi"* (sohbete yapıştırıldı)
> **Alındığı tarih:** 03.08.2026
> **Doğrulama:** ❌ denenmedi — hiçbir karakter eğitilmedi
> **Kapsam:** Karakterin sahneler arası **kimlik** sabitliği.
> **CEVAPLAMADIĞI şeyler:** eğitilen kimliğin video modellerinde de geçerli
> olup olmadığı (rapor Soul 2.0 **görsel** üretiminden bahsediyor; video
> tarafına taşınıp taşınmadığı belirsiz), kredi maliyeti, kimlik başına
> saklama süresi, **kıyafet/ekipmanın** kimlikle birlikte kilitlenip
> kilitlenmediği.

---

## 🎯 NEDEN BU DOSYA ÖNCELİKLİ

`00_README.md` öncelik listesinde 3. sırada — ama depodaki ölçüm bunu
**1. sıraya** taşıyor:

```
MANTIK QA'sı yapılmış 7 filmin KOSTÜM-PROP skorları:
  Deep Pressure 1/10 · Inversion 2/10 · Kaleida 2/10 · Holding Field 3/10
  Tidal Hunt 3/10 · Canopy World 4/10 · Last Archive 3/10
  → Yedi filmin yedisinde de 4'ün altında. Depodaki EN DÜŞÜK kategori.

Ders 8 · 16 · 37 · 55 · 57 — beş ders bu tek soruna yazıldı ve
hiçbiri kategoriyi 4'ün üstüne çıkarmadı.
```

Şu anki çözümümüz **metin**: `SUIT IDENTITY LOCK` bloğu 28 promptun 28'ine
birebir kopyalanıyor (Ders 55). Bu bir çözüm değil, bir **telafi** — ve
ölçüm telafinin yetmediğini söylüyor.

Rapor, sorunun kökünü doğru koyuyor: *metinsel tanımlama belirli bir kişiyi
değil bir TİPİ betimler; model her üretimde o tipi yeniden yorumlar.*
Tek referans görsel daha iyi tutar ama uzun dizilerde (40+ sahne) yavaşça
kayar. Bizim 7-9 dk formatımız tam olarak 75 imajlık bir zincir.

---

## 🧪 SOUL ID NEDİR — rapordan

Belirli bir kişinin fotoğraflarıyla eğitilen, kalıcı bir **kimlik katmanı**
("dijital çapa"). Eğitildikten sonra stil, ışık, kamera açısı veya prompt ne
olursa olsun kilitli yüz otomatik uygulanıyor.

```
GİRDİ        en az 20 yüksek kaliteli fotoğraf
             farklı açılardan · tutarlı ışıkla
EĞİTİM       ~3-5 dakika
ÖĞRENDİĞİ    yüz yapısı · cilt tonu · saç dokusu · vücut oranları
ÇIKTI        Soul 2.0 ile yapılan her üretimde otomatik uygulanan kimlik
```

**Veri kalitesi kuralları (rapor):**

```
❌ KULLANMA   yüze düşen ağır gölge · güneş gözlüğü · kesilmiş yüz hattı
              · karmaşık arka plan · 4-5 aydan eski fotoğraf
✅ ZORUNLU    en az 1 adet TAM BOY fotoğraf (vücut oranı doğruluğu için)
KURAL         "Garbage in, garbage out" — veri kalitesi, veri miktarından
              önemli. Model kişinin bugünkü hâlini değil, REFERANSTAKİ
              hâlini takip eder.
```

---

## ⚠️ BİZİM İÇİN ÜÇ SORUN — rapor bunları çözmüyor

### 1. Bizim karakterimiz gerçek bir insan değil

Soul ID'nin girdisi **gerçek bir kişinin 20 fotoğrafı.** Depodaki karakterler
kurgusal ve yalnızca metinde var (`Dr. Sena Aydın`, `Dr. Kaya Uçan`, `Selin`).

```
OLASI YOL     Önce görsel modelle (Nano Banana Pro / Seedream) aynı
              karakterin 20 farklı açıdan portresi üretilir, sonra o set
              Soul ID'ye eğitim verisi olarak verilir.
              → Rapor bu yolu TARİF ETMİYOR. Denenmeden bilinmez.
RİSK          Üretilmiş görsellerden eğitilen kimlik, üretim hatalarını da
              öğrenir. 20 karenin 3'ünde çene kaymışsa, kimlik o kaymayı
              içselleştirir.
```

### 2. Bizim sorunumuz yüz değil, KIYAFET

Ölçülen bozulmaların çoğu yüzde değil ekipmanda: kask açılıp kapanıyor,
tüp beliriyor, vizör tintleniyor, kir yer değiştiriyor (Ders 37, 42, 55, 57).
Rapor Soul ID'nin **yüz + cilt + saç + vücut oranı** öğrendiğini söylüyor;
**kostümü öğrendiğini söylemiyor.**

```
⛔ Soul ID kurulsa bile SUIT IDENTITY LOCK metni KALDIRILMAZ.
   Kimlik katmanı yüzü çözerse, kıyafet hâlâ metinle taşınır.
   → Test: aynı Soul ID ile iki üretim yap, kıyafetten hiç bahsetme.
     Kıyafet aynı çıkıyorsa metin bloğu kısaltılabilir; çıkmıyorsa duruyor.
```

### 3. Video tarafında geçerli mi

Rapor Soul ID'yi **Soul 2.0 görsel üretimi** bağlamında anlatıyor. Bizim
sorunumuz iki klip ARASINDA. Kimlik katmanı video modeline (Kling/Veo)
aktarılamıyorsa, kazanç yalnızca 7-9 dk formatının anahtar karelerinde olur —
ki orası da zaten kritik nokta.

---

## 📝 EĞİTİMSİZ ALTERNATİF — rapordan, hemen uygulanabilir

Kimlik eğitmeden, prompt üzerinden sabitleme için rapor şunu söylüyor:
referans görsele **ek olarak** metne **spesifik ve statik** yüz detayları
yerleştir.

```
❌ ZAYIF   "34 yaşında bir kadın"          → bir TİP tarif eder
✅ GÜÇLÜ   "yüksek elmacık kemikleri, sağ kaşta kısa soluk yara izi,
            derin yerleşimli kahverengi gözler"  → bir KİŞİ tarif eder
```

**Bu depoda zaten yapılıyor** — `THE_HOLDING_FIELD` suit bloğu tam olarak bu
biçimde yazılı (sağ kaşta yara izi, geniş yassı burun, çatlak dudak). Yani
raporun "eğitimsiz en iyi yöntem" dediği şey bizim mevcut tabanımız.

```
SONUÇ: Soul ID bir YÜKSELTME olurdu, bir düzeltme değil.
       Mevcut yöntemimiz raporun tavsiye ettiği tavanda çalışıyor
       ve ölçüm o tavanın 3/10 olduğunu söylüyor.
```

---

## ✅ KURULUMDAN SONRA TEST PLANI — 4 adım

```
1. Bir karakterin 20 portresi görsel modelle üretilir (tek stil, tek ışık,
   farklı açılar, 1 tam boy). Üretim hatası olan kare AYIKLANIR.
2. Soul ID eğitilir. Süre ve kredi maliyeti not edilir.
3. TEST A — kimlik: aynı Soul ID ile 5 farklı ışık/açıda üretim.
   Yüz kayıyor mu?
4. TEST B — kostüm: aynı Soul ID, kıyafetten HİÇ bahsetmeyen prompt.
   Kıyafet sabit kalıyor mu?
   → B'nin cevabı, `SUIT IDENTITY LOCK` bloğunun kaderini belirler.
```

Sonuç ne çıkarsa çıksın **film tarafına** yazılır:
`LESSONS_LEARNED.md` (yeni ders) ve `SAHNE_DEVAMLILIK_KILAVUZU.md` (çapalama
yöntemi). Bu dosya yalnızca aracı anlatır.
