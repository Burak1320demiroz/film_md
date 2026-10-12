#!/usr/bin/env python3
"""Yeni hat araçlarının regresyon testi — tek komut.

    python3 uretim_hatti/test/kos.py            # hepsi
    python3 uretim_hatti/test/kos.py -v         # her testin çıktısını da bas

Ne sınar:
  film_dogrula.py  ornekler/ altındaki geçerli ve kasıtlı bozuk film klasörleri (çekim 10 s · numaralı referans anahtarı ·
                   10 s vuruş planı dahil) · yanlış alarm cümleleri
  izleyici_kanca   izinli kare ✅ · repo dosyası / ham / ../ kaçışı ⛔
  kurgu.py         kontrol (parça 10 s) · liste --kesmeler · taslak · ses kırpma · zincir sırası · yukseklik (−14 LUFS)
  kareler.py       cikar (100+ kare sırası) · dikis (doğru ↔ yanlış dikiş SSIM) · kuyruk (donma · gizli kesme) ·
                   kapak (yüzey kopyaları · 480p uyarısı · sağ alt köşe bayrağı)

Video ve ses REPOYA GİRMEZ: test medyası ffmpeg ile geçici klasörde üretilir ve test bitince silinir.
Örnekler yalnız metindir (uretim_hatti/test/ornekler/). Çıkış kodu: 0 hepsi geçti · 1 en az bir test düştü.
Bir araç değiştiğinde önce bu betik koşulur; beklenen değer değiştiyse nedeni bu dosyada yazılır.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

KOK = Path(__file__).resolve().parents[2]
ARAC = KOK / "uretim_hatti" / "araclar"
ORNEK = Path(__file__).resolve().parent / "ornekler"
sys.path.insert(0, str(ARAC))

sonuclar = []
AYRINTI = False


def kos(*args, girdi=None):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, input=girdi)
    return r.returncode, r.stdout + r.stderr


def test(ad, kosul, cikti=""):
    sonuclar.append((ad, bool(kosul)))
    print(f"{'✅' if kosul else '⛔'} {ad}")
    if (AYRINTI or not kosul) and cikti:
        print("   " + cikti.strip().replace("\n", "\n   ")[:1500])


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], check=True)


# ── film_dogrula ────────────────────────────────────────────────────────────
# (klasör, bölüm, beklenen hata sayısı, çıktıda geçmesi gereken parçalar)
FILM_ORNEKLERI = [
    ("gecerli", [], 0, []),
    ("sure_bozuk", [], 2, ["her çekim 10 s", "10 s'nin katı"]),   # 08.10.2026: çekim 10 s · HEDEF_SURE 10'un katı
    ("zincir_gecerli", [], 0, []),
    ("zincir_bozuk", [], 18, ["halka", "EKLE"]),
    ("prompt_metin_bozuk", ["--bolum", "prompt"], 5,
     ["meta etiket 'Scene 1 of 3'", "film geneli ifade", "başka çekime atıf", "konuşma/ses tarifi", "diyor ama"]),
    # 10.10.2026 sahip kararı: numaralı referans (ref/<No>.<AD>_v1.png · "Reference <No>" anahtarı) + 10 s vuruş planı;
    # yalnız §3'te "No" sütunu olan yeni biçim filmlerde (gecerli/diyalog_gecerli eski biçim → ⚠️ ile atlanır)
    ("referans_gecerli", [], 0, ["yapı geçerli"]),
    ("referans_bozuk", [], 12,
     ["biçim <No>.<AD>_v<k>.png", "biçim <No>.<AD>", "9 numaralı referans yok", "10 s zaman planı yok", "TEK referans sayfasında",
      "'KOKPIT' adını taşıyor", "'Reference 2' anahtarı yok", "'Reference 3' yazıyor ama", "0'da başlamalı",
      "10 s'de bitmeli", "en az 2 s", "donan bitiş"]),
    # 12.10.2026 sahip kararı: Kaynak "model sesi (…)" → replik Video promptunda birebir (Omni konuşur), konuşma tarifi o
    # blokta serbest, tavan 8 s (diyalog_gecerli C03) · eksik birebir ve 9 s model sesi hata (diyalog_bozuk replik 4)
    ("diyalog_gecerli", [], 0, []),
    ("diyalog_bozuk", [], 6,
     ["en çok 5 s", "en çok 8 s (kurguda eklenen ses)", "en çok 8 s (model sesi", "replik birebir yok", "konuşma/ses tarifi"]),
    # 12.10.2026 sahip kararı: MUZIK var → §7 MÜZİK PROMPTU ```text bloğu (yeni biçimde hata, eskide uyarı); §6 yatak/geçiş uyarı
    ("muzik_gecerli", [], 0, ["yapı geçerli"]),
    ("muzik_bozuk", ["--bolum", "muzik"], 1, ["MÜZİK PROMPTU bloğu yok", "ORTAM YATAĞI tablosu yok"]),
    ("yayin_gecerli", ["--bolum", "yayin"], 0, []),
    ("yayin_bozuk", ["--bolum", "yayin"], 6,
     ["Türkçe karakter", "karakter sayısı yanlış", "tam 3", "#viral", "sabit bloğu", "araç/CGI"]),
]

TEMIZ = ["Shot on 35mm with fine film grain.", "No dialogue, no music.", "She works without speaking.",
         "There is no one else on the deck; the astronaut kneels.",
         "The camera keeps the same height and lens throughout this shot.",
         "A thin hiss of gas leaves the valve.", "The panel's open mouth faces the camera.",
         "He steps back and the hatch swings open."]


def film_dogrula_testleri():
    for klasor, bolum, beklenen, parcalar in FILM_ORNEKLERI:
        kod, out = kos(ARAC / "film_dogrula.py", ORNEK / klasor, *bolum)
        m = re.search(r"⛔ (\d+) hata\s*$", out.strip())
        sayi = int(m.group(1)) if m else (0 if "✅ yapı geçerli" in out else -1)
        eksik = [p for p in parcalar if p not in out]
        test(f"film_dogrula {klasor}: {beklenen} hata · çıkış {1 if beklenen else 0}",
             sayi == beklenen and kod == (1 if beklenen else 0) and not eksik,
             out + (f"\n(eksik parça: {eksik})" if eksik else ""))
    import film_dogrula as f
    yanlis = []
    for s in TEMIZ:
        f.hata.clear()
        f.metin_kontrol("T", "Video", s)
        if f.hata:
            yanlis.append(f"{s} → {f.hata}")
    test(f"film_dogrula yanlış alarm: {len(TEMIZ)} temiz cümle, 0 hata", not yanlis, "\n".join(yanlis))
    # ağız kadrajdaki replik: iki biçim de geçer (07.10.2026, SMOKE P9'a kadar), yokluğu yakalanır
    sonuc = []
    for metin_, beklenen in [('She looks up and says, "Stay with my voice."', 0),
                             ("She looks up and says: Stay with my voice.", 0),
                             ("She looks up and whispers.", 1)]:
        f.hata.clear()
        f.metin_kontrol("T", "Video", metin_, agiz=["Stay with my voice."])
        if len(f.hata) != beklenen:
            sonuc.append(f"{metin_} → {f.hata}")
    test("film_dogrula ağız repliği: tırnak ve iki nokta geçer, yokluğu yakalanır", not sonuc, "\n".join(sonuc))


# ── izleyici kancası ───────────────────────────────────────────────────────
def kanca_testleri():
    ev = Path.home() / "film_medya" / "TEST_FILM"
    durumlar = [(ev / "izleyici" / "taslak_1" / "01.png", 0), (ev / "izleyici_kapak" / "k.png", 0),
                (KOK / "AGENTS.md", 2), (ev / "ham" / "C01_d1.mp4", 2),
                (Path(f"{ev}/izleyici/../ham/C01_d1.mp4"), 2)]
    hatali = []
    for yol, beklenen in durumlar:
        kod, out = kos(ARAC / "izleyici_kanca.py",
                       girdi=json.dumps({"tool_name": "Read", "tool_input": {"file_path": str(yol)}}))
        if kod != beklenen:
            hatali.append(f"{yol} → {kod} (beklenen {beklenen}) {out}")
    test(f"izleyici_kanca: {len(durumlar)} yol (2 izin · 3 engel)", not hatali, "\n".join(hatali))


# ── kurgu.py ───────────────────────────────────────────────────────────────
def kurgu_testleri(t):
    (t / "ham").mkdir()
    (t / "kare").mkdir()
    (t / "ses").mkdir()
    for i, kaynak in enumerate(["testsrc", "smptebars", "rgbtestsrc"], 1):
        ffmpeg("-f", "lavfi", "-i", f"{kaynak}=duration=12:size=320x180:rate=24",
               "-f", "lavfi", "-i", f"sine=frequency={300 * i}:duration=12", "-shortest",
               "-pix_fmt", "yuv420p", t / "ham" / f"C0{i}_d1.mp4")
    ffmpeg("-f", "lavfi", "-i", "color=c=gray:size=320x180", "-frames:v", "1", t / "kare" / "C04.png")
    ffmpeg("-f", "lavfi", "-i", "sine=frequency=440:duration=2", t / "ses" / "R01.wav")
    temel = {"film": "TEST", "medya_kok": str(t), "cozunurluk": "320x180", "fps": 24,
             # 08.10.2026: her video parçası 10 s; görsel parça (C04 png, karartma gibi) serbest
             "parcalar": [{"cekim": "C01", "dosya": "ham/C01_d1.mp4", "giris": 1.0, "cikis": 11.0},
                          {"cekim": "C02", "dosya": "ham/C02_d1.mp4", "giris": 0.0, "cikis": 10.0},
                          {"cekim": "C04", "dosya": "kare/C04.png", "giris": 0, "cikis": 2.0},
                          {"cekim": "C03", "dosya": "ham/C03_d1.mp4", "giris": 2.0, "cikis": 12.0}],
             "ses": [{"dosya": "ses/R01.wav", "baslangic": 3.0, "kazanc_db": -3, "solma": 0.2},
                     {"dosya": "ham/C02_d1.mp4", "baslangic": 2.5, "kazanc_db": 0,
                      "giris": 1.0, "cikis": 2.5, "solma": 0.1}]}

    def yaz(ad, veri):
        p = t / ad
        p.write_text(json.dumps(veri), encoding="utf-8")
        return p

    tl = yaz("timeline.json", temel)
    kod, out = kos(ARAC / "kurgu.py", "kontrol", tl)
    test("kurgu kontrol: geçerli timeline (10 s parçalar + görsel parça + kırpılmış ses) → 0", kod == 0 and "32.00 s" in out, out)

    kisa = json.loads(json.dumps(temel))
    kisa["parcalar"][1]["cikis"] = 8.0
    kod, out = kos(ARAC / "kurgu.py", "kontrol", yaz("kisa.json", kisa))
    test("kurgu kontrol: 8 s video parçası → 1 (her çekim 10 s)", kod == 1 and "her çekim 10 s" in out, out)

    kod, out = kos(ARAC / "kurgu.py", "liste", tl, "--kesmeler")
    test("kurgu liste --kesmeler: 3 kesme, CUT LIST", kod == 0 and "CUT LIST" in out and
         len(re.findall(r"^\d+\s+\d\d:\d\d\.\d", out, re.M)) == 3, out)

    bozuk = json.loads(json.dumps(temel))
    bozuk["ses"].append({"dosya": "ses/R01.wav", "baslangic": 1.0, "kazanc_db": 0, "giris": 2.0, "cikis": 1.0})
    kod, out = kos(ARAC / "kurgu.py", "kontrol", yaz("bozuk_ses.json", bozuk))
    test("kurgu kontrol: ters ses aralığı → 1", kod == 1 and "geçersiz" in out, out)

    zincir = json.loads(json.dumps(temel))
    zincir["parcalar"][0]["zincir"] = "Z1"
    zincir["parcalar"][3]["zincir"] = "Z1"
    kod, out = kos(ARAC / "kurgu.py", "kontrol", yaz("zincir.json", zincir))
    test("kurgu kontrol: arası bölünmüş zincir → 1", kod == 1 and "zincir" in out.lower(), out)

    # eksik dosya zamanı kaydırmaz: C02 yoksa 21.0 s hâlâ C04'te (10 + 10 = 20 → C04 20-22), kod 1 + uyarı
    eksik = json.loads(json.dumps(temel))
    eksik["parcalar"][1]["dosya"] = "ham/YOK.mp4"
    kod, out = kos(ARAC / "kurgu.py", "liste", yaz("eksik.json", eksik), "--zaman", "00:21")
    test("kurgu liste --zaman: eksik dosya sonraki zamanları kaydırmaz, hatayı gösterir",
         kod == 1 and "→ C04" in out and "dosya yok" in out, out)

    taslak = t / "cikti" / "taslak.mp4"
    kod, out = kos(ARAC / "kurgu.py", "taslak", tl, "-o", taslak)
    test("kurgu taslak: 32 s, sesli", kod == 0 and "süre 32.0" in out and "ses var" in out, out)

    # 12.10.2026: klipler arası geçiş (karisim → xfade fade · karartma → fadeblack; film geçiş süresi kadar kısalır),
    # mekân başına kesintisiz ortam yatağı (klipleri aşar, kısa kaynak döngülenir), model sesi için klip sesi
    ffmpeg("-f", "lavfi", "-i", "anoisesrc=color=brown:duration=5:amplitude=0.2", t / "ses" / "yatak.wav")
    gecis = json.loads(json.dumps(temel))
    gecis["parcalar"][1]["gecis"] = {"tur": "karisim", "sure": 0.5}
    gecis["parcalar"][1]["klip_sesi"] = True
    gecis["parcalar"][3]["gecis"] = "karartma 1.0"
    gecis["yataklar"] = [{"dosya": "ses/yatak.wav", "baslangic": 0, "bitis": 20, "kazanc_db": -12, "gecis": 1.0},
                         {"dosya": "ses/yatak.wav", "baslangic": 19, "bitis": 30.5, "kazanc_db": -12, "gecis": 1.0}]
    tlg = yaz("gecis.json", gecis)
    kod, out = kos(ARAC / "kurgu.py", "kontrol", tlg)
    test("kurgu kontrol: geçişli timeline (karışım 0,5 + karartma 1,0 → 30,5 s) · yatak 2 · klip sesi 1 → 0",
         kod == 0 and "30.50 s" in out and "yatak: 2" in out and "klip sesi: 1" in out and "döngülenir" in out, out)
    kod, out = kos(ARAC / "kurgu.py", "liste", tlg)
    test("kurgu liste: geçiş sütunu (karisim 0.5s · karartma 1.0s)", kod == 0 and "karisim 0.5s" in out and "karartma 1.0s" in out, out)
    kod, out = kos(ARAC / "kurgu.py", "taslak", tlg, "-o", t / "cikti" / "gecis.mp4")
    test("kurgu taslak: geçişli 30,5 s, sesli (xfade + yatak + klip sesi)", kod == 0 and "süre 30.5" in out and "ses var" in out, out)
    bozukg = json.loads(json.dumps(temel))
    bozukg["parcalar"][2]["gecis"] = {"tur": "silme", "sure": 0.5}
    bozukg["parcalar"][3]["gecis"] = {"tur": "karisim", "sure": 4.0}
    kod, out = kos(ARAC / "kurgu.py", "kontrol", yaz("gecis_bozuk.json", bozukg))
    test("kurgu kontrol: bilinmeyen geçiş türü + 4 s geçiş → 1", kod == 1 and "kesme | karisim | karartma" in out and "0.2–2.0 s" in out, out)

    final = t / "cikti" / "final.mp4"
    kod, out = kos(ARAC / "kurgu.py", "yukseklik", taslak, "--uygula", "-o", final)
    m = re.search(r"sonra: (-?[\d.]+) LUFS · tepe (-?[\d.]+) dBTP", out)
    test("kurgu yukseklik --uygula: −14 ±1 LUFS · ≤ −1 dBTP",
         kod == 0 and m and abs(float(m.group(1)) + 14) <= 1 and float(m.group(2)) <= -0.7, out)
    kod, out = kos(ARAC / "kurgu.py", "yukseklik", final)
    test("kurgu yukseklik (ölçüm): final hedefte", kod == 0 and "hedefte" in out, out)


# ── kareler.py ─────────────────────────────────────────────────────────────
def kareler_testleri(t):
    ffmpeg("-f", "lavfi", "-i", "testsrc=duration=120:size=160x90:rate=5", "-pix_fmt", "yuv420p", t / "uzun.mp4")
    kod, out = kos(ARAC / "kareler.py", "cikar", t / "uzun.mp4", "--hedef", t / "uzun_k", "--aralik", "1")
    zaman = (t / "uzun_k" / "zamanlar.txt").read_text() if (t / "uzun_k" / "zamanlar.txt").exists() else ""
    test("kareler cikar: 120 kare, 100.png = 99 s (sayısal sıra)", kod == 0 and "100.png\t99.00" in zaman,
         out + zaman[-120:])

    ffmpeg("-f", "lavfi", "-i", "testsrc=duration=12:size=320x180:rate=24", "-pix_fmt", "yuv420p", t / "tam.mp4")
    ffmpeg("-i", t / "tam.mp4", "-t", "6", t / "a.mp4")
    ffmpeg("-ss", "6", "-i", t / "tam.mp4", t / "b.mp4")
    ffmpeg("-f", "lavfi", "-i", "mandelbrot=size=320x180:rate=24", "-t", "6", "-pix_fmt", "yuv420p", t / "baska.mp4")
    ssim = {}
    for ad, b in (("dogru", "b.mp4"), ("yanlis", "baska.mp4")):
        kod, out = kos(ARAC / "kareler.py", "dikis", t / "a.mp4", t / b, "--hedef", t / f"dikis_{ad}")
        m = re.search(r"SSIM ([\d.]+)", out)
        ssim[ad] = float(m.group(1)) if m else None
    test(f"kareler dikis: doğru dikiş SSIM ≥ 0,8 ({ssim['dogru']}) · yanlış ≤ 0,6 ({ssim['yanlis']})",
         ssim["dogru"] is not None and ssim["yanlis"] is not None and ssim["dogru"] >= 0.8 and ssim["yanlis"] <= 0.6)

    ffmpeg("-f", "lavfi", "-i", "testsrc=duration=4:size=320x180:rate=24",
           "-vf", "tpad=stop_mode=clone:stop_duration=2", "-pix_fmt", "yuv420p", t / "donan.mp4")
    kod, out = kos(ARAC / "kareler.py", "kuyruk", t / "donan.mp4")
    m = re.search(r"kuyruk donması ([\d.]+) s", out)
    test("kareler kuyruk: son 2 s donma bulunur", kod == 0 and m and 1.5 <= float(m.group(1)) <= 2.5, out)

    ffmpeg("-i", t / "a.mp4", "-i", t / "baska.mp4", "-filter_complex", "[0:v][1:v]concat=n=2:v=1[v]",
           "-map", "[v]", "-pix_fmt", "yuv420p", t / "gizli_kesme.mp4")
    kod, out = kos(ARAC / "kareler.py", "kuyruk", t / "gizli_kesme.mp4")
    m = re.search(r"gizli kesme/çözülme şüphesi (\d+)", out)
    test("kareler kuyruk: gizli kesme bulunur", kod == 0 and m and int(m.group(1)) >= 1, out)

    # kapak (12.10.2026, KAPAK_VE_BASLIK_KILAVUZU §4): yüzey kopyaları · 480p uyarısı · sağ alt köşe bayrağı
    ffmpeg("-f", "lavfi", "-i", "color=c=black:s=1280x720,drawbox=x=480:y=200:w=320:h=320:color=orange:t=fill",
           "-frames:v", "1", t / "sade.png")
    ffmpeg("-f", "lavfi", "-i", "mandelbrot=size=640x360", "-frames:v", "1", t / "kucuk.png")
    ffmpeg("-f", "lavfi", "-i", "color=c=gray:s=1280x720", "-f", "lavfi", "-i", "testsrc=size=320x144",
           "-filter_complex", "[0:v][1:v]overlay=960:576", "-frames:v", "1", t / "kose.png")
    kod, out = kos(ARAC / "kareler.py", "kapak", t / "sade.png", "--hedef", t / "kapak_sade")
    var = [f.name for f in (t / "kapak_sade").glob("*.png")] if (t / "kapak_sade").exists() else []
    test("kareler kapak: 4 yüzey kopyası + kapak.json, 1280×720'de 480p uyarısı yok, köşe bayrağı yok",
         kod == 0 and len(var) == 4 and (t / "kapak_sade" / "kapak.json").exists()
         and "480p" not in out and "sağ alt köşe kapağın" not in out, out)
    kod, out = kos(ARAC / "kareler.py", "kapak", t / "kucuk.png", "--hedef", t / "kapak_kucuk")
    test("kareler kapak: 640×360 → Test & Compare 480p uyarısı", kod == 0 and "480p" in out, out)
    kod, out = kos(ARAC / "kareler.py", "kapak", t / "kose.png", "--hedef", t / "kapak_kose")
    test("kareler kapak: ayrıntılı sağ alt köşe → süre rozeti bayrağı", kod == 0 and "sağ alt köşe kapağın" in out, out)


def main():
    global AYRINTI
    ap = argparse.ArgumentParser(description="yeni hat araçları regresyon testi")
    ap.add_argument("-v", action="store_true", help="her testin çıktısını bas")
    AYRINTI = ap.parse_args().v
    film_dogrula_testleri()
    kanca_testleri()
    with tempfile.TemporaryDirectory(prefix="uretim_hatti_test_") as d:
        t = Path(d)
        (t / "kurgu").mkdir()
        (t / "kareler").mkdir()
        try:
            kurgu_testleri(t / "kurgu")
            kareler_testleri(t / "kareler")
        except subprocess.CalledProcessError as e:
            test(f"test medyası üretilemedi (ffmpeg): {e}", False)
    gecen = sum(1 for _, ok in sonuclar if ok)
    print(f"\n{gecen}/{len(sonuclar)} test geçti")
    return 0 if gecen == len(sonuclar) else 1


if __name__ == "__main__":
    sys.exit(main())
