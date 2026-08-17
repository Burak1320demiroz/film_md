# 🧪 GOOGLE COLAB — ÜRETİM MOTORU BÖLÜMÜ (ARAŞTIRMA)

> **Bu bölüm ne değildir:** film yazma kılavuzu. Senaryo, sahne, tür, fizik
> kuralları **`../kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`**'de kalır.
>
> **Bu bölüm nedir:** yazılmış `.md` filmi **Colab'daki bir GPU üzerinde açık
> ağırlıklı modellerle** görüntüye çevirme yolunun araştırması. Colab MCP,
> donanım katmanları, model adayları, kural ve riskler burada durur.
>
> **Durum (11.08.2026):** ⚠️ **CLI kurulu ve çalışıyor, ücretsiz T4 ölçüldü,
> tek kare üretilmedi.** Kalan tek engel: FLUX.1-dev kapılı depo için HF token.
> Bu bölümün tamamı **web araştırmasıdır** — her dosya kaynağını gösterir.
> Resmî doküman geldiğinde çelişen her satır doc'a göre düzeltilir.

---

## 🧭 SINIR — ne buraya, ne oraya

```
FİLM TARAFI                          MOTOR TARAFI (bu klasör)
──────────────────────────           ──────────────────────────
ne anlatılıyor                       hangi model, hangi VRAM
sahne haritası, süre, diyalog        çözünürlük/en-boy, klip limiti
negatif çekirdek, kamera dili        Colab kuralları, kredi/CU maliyeti
QA rubrikleri                        oturum kopması, kuantizasyon, seed API'si

→ kilavuzlar_ve_sistem_dosyalari/    → colab/klavuzlar/
```

Bir bilgi ikisine de uyuyorsa **film tarafında** durur; burada yalnızca ona
işaret edilir. Aynı bilgiyi iki yerde tutmak, birini yanlış tutmaktır.

---

## 📦 KLASÖR

```
colab/
├── README.md          ← BU DOSYA · bölümün kapısı + karar özeti
└── klavuzlar/
    ├── 00_README.md                ⭐ indeks + doluluk + açık sorular
    ├── 01_BAGLANTI_YOLLARI.md      Colab CLI (birincil) + MCP · komut haritası
    ├── 02_DONANIM_VE_MALIYET.md    VRAM 16→96 GB · CU · Veo API ile kıyas
    ├── 03_MODEL_ADAYLARI.md        video + görsel model kartları · VRAM · 9:16
    └── 04_KURALLAR_VE_RISKLER.md   Colab FAQ yasakları · webui kısıtı · kopma
```

---

## 🔌 ÜÇ CÜMLEDE FİKİR

1. **Colab CLI** (Google, Haziran 2026) terminalden runtime açar ve yerel
   script'i **Colab'ın GPU'sunda** koşturur: `colab run --gpu L4 uretim.py`,
   sonra `colab download`. GPU'yu bayrakla seçebiliyoruz — **16 GB'dan 96 GB'a
   kadar** (→ `02`). Ajan yolu bu; `Colab MCP` (Nisan 2026) ikincil.
2. Colab'ın GPU'sunda **açık ağırlıklı** video/görsel modelleri koşarsak
   (LTX-2.3, Wan 2.2, Z-Image, FLUX.2 klein) saniye başına ödeme yerine
   **saat başına GPU** ödemiş oluruz — kaba hesapla klip başına 10× daha ucuz.
3. Bedeli: kalite/talimat-uyumu Veo seviyesinde değil, kurulum bize kalır,
   ücretsiz katman 12 saat/90 dk limitleriyle ve kopan oturumlarla gelir.

> 📌 Mevcut hat **Veo 3.1 Fast** (`VEO_3_1_FAST_...KILAVUZU.md`). Colab onun
> yerine geçmez — **üçüncü hat** (ikincisi `../higgsfield/`). Farkı: Veo ve
> Higgsfield kapalı servis, Colab **bizim elimizde çalışan model**.

---

## ✅ BU DEPO İÇİN GERÇEK KAZANÇ — neden bakmaya değer

Colab'ın çekiciliği ucuzluk değil, deponun **üç kronik sorununa** doğrudan
dokunması:

```
1. NEGATİF ÇEKİRDEK GERÇEKTEN ÇALIŞIR
   Açık modeller ayrı bir "negative prompt" girdisi alır. Deponun negatif
   çekirdeği bugün prompt metnine gömülü bir dilek listesi; orada kurala döner.

2. SEED GERÇEKTEN SEED
   Aynı seed + aynı girdi = aynı kare. SAHNE_DEVAMLILIK_KILAVUZU'nun seed
   çapası kapalı serviste bir temenni, açık ağırlıkta deterministik.

3. KARAKTER/KOSTÜM İÇİN LoRA
   Depodaki EN DÜŞÜK ölçülen kategori Kostüm-Prop (7 MANTIK raporunun
   7'sinde 4/10 altı). LoRA = karakteri modele öğretmek; Soul ID gibi kapalı
   bir kimlik katmanı değil, bizim eğittiğimiz ağırlık.
   → klavuzlar/03_MODEL_ADAYLARI.md §KARAKTER HATTI
```

Buna karşılık **sessiz film** tercihimiz burada risk değil avantaj: LTX-2.3 ses
üretebiliyor ama ses kanalını atmak bizim elimizde (Higgsfield'de native ses
bir riskti — bkz. `../higgsfield/klavuzlar/02_MODEL_KARTLARI.md`).

---

## 🖥️ KULLANILABİLEN VRAM — kısa cevap

```
T4    14.6 GB  ✅ ÖLÇÜLDÜ 11.08.2026 · ücretsiz katman verdi
               bf16 emülasyon (11× yavaş) · FP8 yok · sistem RAM 12.7 GB
L4    24 GB   ücretli · video için ALT EŞİK
A100  40 / 80 GB
H100  80 GB
G4    96 GB   RTX PRO 6000 Blackwell · 2026'da eklendi · en yüksek
```

⚠️ Bayrakla istemek garanti değil: Pro kullanıcısının A100 isteyip L4 aldığı
kayıtlı (colabtools #5342/#6013). Her oturumun ilk hücresi VRAM'i yazdırır.
Ayrıntı ve CU maliyeti → `klavuzlar/02_DONANIM_VE_MALIYET.md`.

---

## 🚧 KARARA ENGEL OLAN SORULAR — 09.08 güncellemesi

**Colab CLI bulgusu üç sorudan ikisini kapattı** (GPU seçimi: `--gpu`,
dosya indirme: `colab download`). Kalanlar:

```
□ 10+ dakikalık iş hayatta kalıyor mu?  ← KALAN EN KRİTİK
     CLI'da "otomatik keep-alive" ve geçici iş koşucusu var ama süre sınırı
     belgelenmemiş. Terminal kapanınca iş devam ediyor mu → BİLİNMİYOR.

□ Ücretsiz T4 video üretebilir mi?
     16 GB sınırda, ama T4 Turing: bf16 ve FP8 yok — modern video
     modellerinin düşük-VRAM kısayolları bu ikisine dayanıyor.
     Beklenti: ücretsiz katman GÖRSEL için, video L4'ten başlıyor.

□ L4 · H100 · G4 kaç CU/saat yakıyor?
     Hiçbir kaynakta yok. Maliyet planının tamamı L4 satırına bağlı.
     → klavuzlar/02_DONANIM_VE_MALIYET.md
```

---

## ▶️ SIRADAKİ ADIM

```
1. ✅ Araştırma yapıldı → 4 kılavuz + bu kapı (08–09.08.2026)
2. ⏭️ KURULUM — `uv tool install google-colab-cli`
      (01_BAGLANTI_YOLLARI.md §KURULUM). Kurulmadan hiçbir satır doğrulanamaz.
3. ⏭️ İLK ÜÇ ÖLÇÜM:
      · GPU adı + gerçek VRAM yazdır (colab run --gpu T4)
      · 10+ dakikalık iş hayatta kalıyor mu
      · Z-Image / FLUX.2 klein ile TEK GÖRSEL + colab download — en ucuz doğrulama
4. ⏭️ TEK SAHNE DENEMESİ — bir dikey shorts sahnesi (9:16, 10 s).
      Sebep: LTX-2.3'ün 9:16 + 10 s tarifi zaten bizim shorts kalıbımız.
      Aynı prompt, iki motor (Veo çıktısı elimizde), tek değişken.
5. ⏭️ Sonuç ne olursa olsun `klavuzlar/04_KURALLAR_VE_RISKLER.md`'ye yazılır
6. Commit'i proje sahibi atar (AGENTS.md §5)
```

> ⚠️ **Hiçbir film Colab'a taşınmaz** — yukarıdaki üç soru cevaplanana kadar.
> Yarım bilgiyle hat değiştirmek, mevcut Veo hattını da bozar.
