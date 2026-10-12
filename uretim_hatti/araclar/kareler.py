#!/usr/bin/env python3
"""Videodan kare çıkarma, kontak sayfası ve küçültme — ajanların "görmesi" için.

    python3 uretim_hatti/araclar/kareler.py cikar <video> --hedef <klasör> [--aralik 1.0] [--sayfa]
    python3 uretim_hatti/araclar/kareler.py kucult <görsel> --boyut 160x90 --hedef <dosya>

cikar   her `--aralik` saniyede bir kare → <hedef>/01.png, 02.png … (sıra = zaman sırası)
        + <hedef>/zamanlar.txt (dosya → saniye). --sayfa: ayrıca sayfa_01.png … kontak
        sayfaları (4 sütun, her karenin altında zaman). Etiket için PIL gerekir; yoksa
        sayfa etiketsiz kurulur ve zamanlar.txt kullanılır.
kucult  kapak kontrolü için küçültülmüş kopya (160×90 · 320×180 …).
kapak   <görsel> --hedef <klasör>   mekanik kapak denetimi (12.10.2026, KAPAK_VE_BASLIK_KILAVUZU §4):
        yüzey boylarında kopyalar (360×202 mobil ana sayfa · 168×94 masaüstü önerilen · 120×68 mobil önerilen ·
        168×94 gri) + kapak.json. Tek resmî eşik çözünürlük: 1280×720 altı bir seçenek Test & Compare'de
        bütün seçenekleri 480p'ye düşürür. Öteki sayılar (parlaklık, ton aralığı, kenar yoğunluğu, sağ alt
        köşe) BAYRAKTIR, eşik kanalın kendi kapaklarında kalibre edilir; karar küçük kopyalara bakılarak verilir.

ZİNCİR (sahneleme · cekim-yaz §F7):
kare    <video> --t <sn|son> --hedef <png>   tek kare (A: son kare · A′: seçilen çıkış noktası)
dikis   <klip_i> <klip_i+1 | anahtar.png> --hedef <klasör> [--t-cikis sn]
        dikişin iki yanı: 4 karelik şerit (−2 −1 | 0 +1) + fark görüntüsü + SSIM/PSNR → dikis.json.
        ⚠️ SSIM yalnız BAYRAKTIR: pozlama/renk/kadraj sıçramasını ve donmayı yakalar, küçük alandaki
        el/eşya/yüz değişimini YAKALAMAZ. Karar şeride ve fark görüntüsüne bakılarak verilir.
kuyruk  <video>   freezedetect (bitiş karesine erken varıp donma) + scdet (gizli kesme/çözülme) özeti

⛔ İzleyici ajanına verilen klasörde yalnız kareler olur: dosya adları sıra numarasıdır,
film adı, çekim kodu ya da plan bilgisi taşımaz (ELESTIRI_PROTOKOLU · bağımsız göz).
Yalnız standart kütüphane + ffmpeg/ffprobe (+ isteğe bağlı PIL).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path


def sure(video):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "json", str(video)], capture_output=True, text=True, check=True).stdout
        return float(json.loads(out)["format"]["duration"])
    except (subprocess.CalledProcessError, KeyError, ValueError):
        return None


def cikar(a):
    video, hedef = Path(a.video).expanduser(), Path(a.hedef).expanduser()
    d = sure(video)
    if d is None:
        print(f"⛔ video okunamadı: {video}")
        return 1
    if hedef.exists() and any(hedef.glob("*.png")):
        print(f"⛔ {hedef} içinde zaten kare var — boş bir klasör ver (karışmasın)")
        return 1
    hedef.mkdir(parents=True, exist_ok=True)
    gen = a.genislik
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
                        "-vf", f"fps=1/{a.aralik},scale={gen}:-2", "-start_number", "1",
                        str(hedef / "%02d.png")], capture_output=True, text=True)
    if r.returncode:
        print(f"⛔ ffmpeg: {r.stderr.strip()}")
        return 1
    kareler = sorted(hedef.glob("[0-9]*.png"), key=lambda k: int(k.stem))   # 100.png, 11.png'den sonra gelir
    zaman = {k.name: round((i) * a.aralik, 2) for i, k in enumerate(kareler)}
    (hedef / "zamanlar.txt").write_text(
        "\n".join(f"{ad}\t{t:.2f}" for ad, t in zaman.items()) + "\n", encoding="utf-8")
    print(f"✅ {len(kareler)} kare · {d:.1f} s video · her {a.aralik} s → {hedef}")
    if a.sayfa:
        return sayfa(hedef, kareler, zaman)
    return 0


def sayfa(hedef, kareler, zaman, sutun=4, satir=4):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        Image = None
    adet = sutun * satir
    for s in range(0, len(kareler), adet):
        grup = kareler[s:s + adet]
        cikti = hedef / f"sayfa_{s // adet + 1:02d}.png"
        if Image is None:
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-start_number", str(s + 1),
                            "-i", str(hedef / "%02d.png"), "-frames:v", "1",
                            "-vf", f"tile={sutun}x{satir}", str(cikti)], check=False)
            continue
        ilk = Image.open(grup[0])
        w, h = ilk.size
        pay = 18
        tuval = Image.new("RGB", (w * sutun, (h + pay) * ((len(grup) + sutun - 1) // sutun)), "black")
        ciz = ImageDraw.Draw(tuval)
        for i, k in enumerate(grup):
            x, y = (i % sutun) * w, (i // sutun) * (h + pay)
            tuval.paste(Image.open(k).convert("RGB"), (x, y))
            t = zaman[k.name]
            ciz.text((x + 4, y + h + 3), f"{k.stem}  {int(t // 60):02d}:{t % 60:04.1f}", fill="white")
        tuval.save(cikti)
    print(f"✅ kontak sayfası: {(len(kareler) + adet - 1) // adet} adet {'(etiketli)' if Image else '(etiketsiz — zamanlar.txt)'}")
    return 0


def kucult(a):
    src, dst = Path(a.gorsel).expanduser(), Path(a.hedef).expanduser()
    try:
        g, y = (int(x) for x in a.boyut.lower().split("x"))
    except ValueError:
        print("⛔ --boyut GENxYUK (örn. 160x90)")
        return 2
    dst.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                        "-vf", f"scale={g}:{y}:flags=area", str(dst)], capture_output=True, text=True)
    if r.returncode:
        print(f"⛔ ffmpeg: {r.stderr.strip()}")
        return 1
    print(f"✅ {dst} ({g}×{y})")
    return 0


YUZEYLER = (("360x202", "mobil_ana_sayfa"), ("168x94", "masaustu_onerilen"), ("120x68", "mobil_onerilen"))


def _boyut(gorsel):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                              "stream=width,height", "-of", "json", str(gorsel)],
                             capture_output=True, text=True, check=True).stdout
        st = json.loads(out)["streams"][0]
        return int(st["width"]), int(st["height"])
    except (subprocess.CalledProcessError, KeyError, IndexError, ValueError):
        return None


def _istat(gorsel, vf):
    """vf zincirinden sonra signalstats → {YAVG, YLOW, YHIGH, YMIN, YMAX} (0-255)."""
    r = _ff(["-loglevel", "error", "-i", str(gorsel), "-vf",
             f"{vf},signalstats,metadata=mode=print:file=-", "-frames:v", "1", "-f", "null", "-"])
    d = {}
    for satir in r.stdout.splitlines():
        if "lavfi.signalstats." in satir and "=" in satir:
            k, v = satir.split("lavfi.signalstats.", 1)[1].split("=", 1)
            try:
                d[k] = float(v)
            except ValueError:
                pass
    return d


def kapak(a):
    src, hedef = Path(a.gorsel).expanduser(), Path(a.hedef).expanduser()
    b = _boyut(src)
    if b is None:
        print(f"⛔ okunamadı: {src}")
        return 1
    w, h = b
    hedef.mkdir(parents=True, exist_ok=True)
    uyari = []
    if w < 1280 or h < 720:
        uyari.append(f"{w}×{h} < 1280×720: Test & Compare bütün seçenekleri 480p'ye düşürür (answer/16391400)")
    if abs(w / h - 16 / 9) > 0.01:
        uyari.append(f"oran {w / h:.3f} ≠ 16:9")
    dosyalar = []
    for boy, ad in YUZEYLER:
        g, y = boy.split("x")
        d = hedef / f"{boy}_{ad}.png"
        _ff(["-loglevel", "error", "-y", "-i", str(src), "-vf", f"scale={g}:{y}:flags=area", str(d)])
        dosyalar.append(d.name)
    gri = hedef / "168x94_gri.png"
    _ff(["-loglevel", "error", "-y", "-i", str(src), "-vf", "scale=168:94:flags=area,format=gray", str(gri)])
    dosyalar.append(gri.name)
    kucuk = "scale=168:94:flags=area,format=gray"
    ton = _istat(src, kucuk)
    kenar = _istat(src, f"{kucuk},edgedetect=low=0.1:high=0.3")
    kose = _istat(src, f"{kucuk},edgedetect=low=0.1:high=0.3,crop=iw*0.25:ih*0.2:iw*0.75:ih*0.8")
    olcum = {
        "boyut": [w, h],
        "parlaklik_ort": round(ton.get("YAVG", 0), 1),
        "ton_araligi_p10_p90": round(ton.get("YHIGH", 0) - ton.get("YLOW", 0), 1),
        "kenar_orani": round(kenar.get("YAVG", 0) / 255, 3),
        "sag_alt_kose_kenar_orani": round(kose.get("YAVG", 0) / 255, 3),
    }
    bayrak = []
    if olcum["sag_alt_kose_kenar_orani"] > olcum["kenar_orani"]:
        bayrak.append("sağ alt köşe kapağın ortalamasından ayrıntılı: süre rozeti üstüne biner")
    if olcum["parlaklik_ort"] < 40:
        bayrak.append("çok koyu kapak: koyu arayüzde (#0F0F0F) kenarları kaybolabilir")
    if olcum["ton_araligi_p10_p90"] < 60:
        bayrak.append("dar ton aralığı: gri tonlamada özne zeminden ayrılmayabilir")
    (hedef / "kapak.json").write_text(json.dumps({"kaynak": str(src), "olcum": olcum, "uyari": uyari,
                                                  "bayrak": bayrak, "dosyalar": dosyalar},
                                                 ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"kapak: {src.name} · {w}×{h}")
    print(f"  parlaklık ort {olcum['parlaklik_ort']} · ton aralığı {olcum['ton_araligi_p10_p90']} · "
          f"kenar oranı {olcum['kenar_orani']} · sağ alt köşe {olcum['sag_alt_kose_kenar_orani']}")
    for u in uyari:
        print(f"⚠️ {u}")
    for bb in bayrak:
        print(f"🚩 {bb} (bayrak, eşik kalibre edilmedi)")
    print(f"✅ {hedef}/: {' · '.join(dosyalar)} · kapak.json — karar küçük kopyalara bakılarak verilir")
    return 0


def _ff(args):
    return subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *args], capture_output=True, text=True)


def _kare_cek(video, t, cikti):
    """t = 'son' → son kare; sayı → o saniyedeki kare. Başarıda True."""
    cikti.parent.mkdir(parents=True, exist_ok=True)
    if str(t) == "son":
        r = _ff(["-loglevel", "error", "-y", "-sseof", "-0.5", "-i", str(video), "-update", "1", str(cikti)])
    else:
        r = _ff(["-loglevel", "error", "-y", "-ss", f"{float(t):.3f}", "-i", str(video), "-frames:v", "1", str(cikti)])
    return r.returncode == 0 and cikti.exists()


def kare(a):
    v, h = Path(a.video).expanduser(), Path(a.hedef).expanduser()
    if sure(v) is None:
        print(f"⛔ video okunamadı: {v}")
        return 1
    if not _kare_cek(v, a.t, h):
        print(f"⛔ kare çıkarılamadı: {v} @ {a.t}")
        return 1
    print(f"✅ {h} ({'son kare' if a.t == 'son' else f't={float(a.t):.2f} s'})")
    return 0


def _son_iki(video, t_cikis, klasor):
    """çıkış noktasından önceki son iki kare (−2, −1)."""
    tmp = klasor / "_a"
    tmp.mkdir(parents=True, exist_ok=True)
    if t_cikis is None:
        r = _ff(["-loglevel", "error", "-y", "-sseof", "-0.4", "-i", str(video), str(tmp / "%03d.png")])
    else:
        bas = max(float(t_cikis) - 0.4, 0)
        r = _ff(["-loglevel", "error", "-y", "-ss", f"{bas:.3f}", "-i", str(video), "-t", f"{float(t_cikis) - bas:.3f}",
                 str(tmp / "%03d.png")])
    kareler = sorted(tmp.glob("*.png"))
    if r.returncode or not kareler:
        return None
    return kareler[-2:] if len(kareler) >= 2 else [kareler[-1], kareler[-1]]


def _ilk_iki(kaynak, klasor):
    if kaynak.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
        return [kaynak, kaynak]
    tmp = klasor / "_b"
    tmp.mkdir(parents=True, exist_ok=True)
    r = _ff(["-loglevel", "error", "-y", "-i", str(kaynak), "-frames:v", "2", str(tmp / "%03d.png")])
    kareler = sorted(tmp.glob("*.png"))
    if r.returncode or not kareler:
        return None
    return kareler[:2] if len(kareler) >= 2 else [kareler[0], kareler[0]]


def _benzerlik(x, y):
    """(ssim_all, psnr_avg) — y, x'in boyutuna ölçeklenir."""
    import re
    filtre = "[1:v][0:v]scale2ref[b][a];[a][b]{}"
    s = _ff(["-i", str(x), "-i", str(y), "-lavfi", filtre.format("ssim"), "-f", "null", "-"]).stderr
    p = _ff(["-i", str(x), "-i", str(y), "-lavfi", filtre.format("psnr"), "-f", "null", "-"]).stderr
    ms, mp = re.search(r"All:([\d.]+)", s), re.search(r"average:([\d.]+|inf)", p)
    return (float(ms.group(1)) if ms else None,
            (float("inf") if mp and mp.group(1) == "inf" else float(mp.group(1))) if mp else None)


def dikis(a):
    ai, bi = Path(a.klip_i).expanduser(), Path(a.sonraki).expanduser()
    h = Path(a.hedef).expanduser()
    h.mkdir(parents=True, exist_ok=True)
    if sure(ai) is None or not bi.exists():
        print(f"⛔ okunamadı: {ai if sure(ai) is None else bi}")
        return 1
    sol, sag = _son_iki(ai, a.t_cikis, h), _ilk_iki(bi, h)
    if not sol or not sag:
        print("⛔ dikiş kareleri çıkarılamadı")
        return 1
    serit, fark = h / "dikis_serit.png", h / "dikis_fark.png"
    yuk = 360
    r1 = _ff(["-loglevel", "error", "-y", "-i", str(sol[0]), "-i", str(sol[1]), "-i", str(sag[0]), "-i", str(sag[1]),
              "-filter_complex",
              "".join(f"[{i}:v]scale=-2:{yuk},setsar=1[s{i}];" for i in range(4)) +
              "[s0][s1][s2][s3]hstack=inputs=4", "-frames:v", "1", str(serit)])
    r2 = _ff(["-loglevel", "error", "-y", "-i", str(sol[1]), "-i", str(sag[0]), "-filter_complex",
              "[1:v][0:v]scale2ref[b][a];[a][b]blend=all_mode=difference,eq=contrast=3", "-frames:v", "1", str(fark)])
    ssim, psnr = _benzerlik(sol[1], sag[0])
    sonuc = {"klip_i": str(ai), "sonraki": str(bi), "t_cikis": a.t_cikis, "ssim": ssim, "psnr": psnr,
             "serit": str(serit) if not r1.returncode else None, "fark": str(fark) if not r2.returncode else None}
    (h / "dikis.json").write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
    for d in (h / "_a", h / "_b"):
        if d.exists():
            for f in d.glob("*.png"):
                f.unlink()
            d.rmdir()
    print(f"dikiş: SSIM {ssim if ssim is not None else '?'} · PSNR {psnr if psnr is not None else '?'} dB")
    print(f"  şerit (−2 −1 | 0 +1): {sonuc['serit']}\n  fark: {sonuc['fark']}")
    print("  ⚠️ SSIM bayraktır, karar değildir — şeride ve fark görüntüsüne bak.")
    return 0


def kuyruk(a):
    import re
    v = Path(a.video).expanduser()
    d = sure(v)
    if d is None:
        print(f"⛔ video okunamadı: {v}")
        return 1
    fz = _ff(["-i", str(v), "-vf", f"freezedetect=n=-60dB:d={a.donma}", "-map", "0:v:0", "-f", "null", "-"]).stderr
    basl = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", fz)]
    sure_l = [float(x) for x in re.findall(r"freeze_duration: ([\d.]+)", fz)]
    donmalar = list(zip(basl, sure_l + [d - b for b in basl[len(sure_l):]]))
    sc = _ff(["-i", str(v), "-vf", f"scdet=threshold={a.esik}", "-map", "0:v:0", "-f", "null", "-"]).stderr
    kesmeler = [(float(t), float(s)) for s, t in re.findall(r"lavfi\.scd\.score: ([\d.]+), lavfi\.scd\.time: ([\d.]+)", sc)]
    print(f"video: {v.name} · {d:.2f} s")
    kuyruk_donma = next((s for b, s in donmalar if abs(b + s - d) < 0.25), 0.0)
    for b, s in donmalar:
        print(f"  donma {b:.2f}–{b + s:.2f} s ({s:.2f} s){'  ← KUYRUK' if abs(b + s - d) < 0.25 else ''}")
    for t, s in kesmeler:
        print(f"  sahne değişimi şüphesi {t:.2f} s (skor {s:.1f})")
    if not donmalar and not kesmeler:
        print("  donma ve sahne değişimi şüphesi yok (bu, 'temiz' demek değildir)")
    print(f"ÖZET: kuyruk donması {kuyruk_donma:.2f} s · gizli kesme/çözülme şüphesi {len(kesmeler)}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="kare çıkarma · kontak sayfası · küçültme")
    alt = ap.add_subparsers(dest="komut", required=True)
    c = alt.add_parser("cikar")
    c.add_argument("video")
    c.add_argument("--hedef", required=True)
    c.add_argument("--aralik", type=float, default=1.0, help="saniye (varsayılan 1)")
    c.add_argument("--genislik", type=int, default=320, help="kare genişliği px (varsayılan 320)")
    c.add_argument("--sayfa", action="store_true", help="kontak sayfası da üret")
    c.set_defaults(fn=cikar)
    k = alt.add_parser("kucult")
    k.add_argument("gorsel")
    k.add_argument("--boyut", default="160x90")
    k.add_argument("--hedef", required=True)
    k.set_defaults(fn=kucult)
    kp = alt.add_parser("kapak")
    kp.add_argument("gorsel")
    kp.add_argument("--hedef", required=True)
    kp.set_defaults(fn=kapak)
    kk = alt.add_parser("kare")
    kk.add_argument("video")
    kk.add_argument("--t", default="son", help="saniye ya da 'son'")
    kk.add_argument("--hedef", required=True)
    kk.set_defaults(fn=kare)
    dk = alt.add_parser("dikis")
    dk.add_argument("klip_i")
    dk.add_argument("sonraki", help="sonraki halkanın videosu ya da anahtar kare görseli")
    dk.add_argument("--hedef", required=True)
    dk.add_argument("--t-cikis", type=float, default=None, help="A′: klip i'nin çıkış noktası (saniye)")
    dk.set_defaults(fn=dikis)
    ku = alt.add_parser("kuyruk")
    ku.add_argument("video")
    ku.add_argument("--donma", type=float, default=0.5, help="en kısa donma süresi (s)")
    ku.add_argument("--esik", type=float, default=10.0, help="scdet eşiği (0-100)")
    ku.set_defaults(fn=kuyruk)
    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
