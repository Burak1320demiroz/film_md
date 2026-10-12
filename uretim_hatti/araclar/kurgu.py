#!/usr/bin/env python3
"""timeline.json → kontrol · liste · taslak film.

    python3 uretim_hatti/araclar/kurgu.py kontrol <timeline.json>
    python3 uretim_hatti/araclar/kurgu.py liste   <timeline.json> [--zaman 01:23.5 | --kesmeler]
    python3 uretim_hatti/araclar/kurgu.py taslak  <timeline.json> [-o cikti.mp4]
    python3 uretim_hatti/araclar/kurgu.py yukseklik <video> [--uygula -o final.mp4]   # −14 LUFS · −1 dBTP

timeline.json (şablon: uretim_hatti/SABLON/timeline.json):
    medya_kok   medya klasörü (~ açılır); göreli dosya yolları buna göre çözülür
    parcalar    [{cekim, dosya, giris, cikis, zincir?, gecis?, klip_sesi?, klip_kazanc_db?}] — saniye, kaynağın
                içindeki aralık; her video parçası 10 s (cikis − giris; sahip kararı 08.10.2026), görsel parça (png) serbest;
                zincir (örn. "Z1") verilirse halkalar ardışık olmalı, dikişte ≤0,3 s kırpılır
                gecis (12.10.2026): BU parçaya girişteki geçiş — {"tur": "kesme"|"karisim"|"karartma", "sure": s}
                ya da "karisim 0.5"; karisim = çözülme (xfade fade), karartma = siyaha inip çıkma (fadeblack);
                geçiş süresi önceki parçayla örtüşür, film o kadar kısalır. Yok = kesme.
                klip_sesi (12.10.2026): true ise bu parçanın KENDİ sesi filme girer (model sesi replik, Omni);
                kök düzeyinde "klip_sesi": true hepsini açar. klip_kazanc_db o sesin kazancı.
    ses         [{dosya, baslangic, kazanc_db, giris?, cikis?, solma?}] — filmin saniyesine yerleşen ses
                parçaları; giris/cikis kaynağın içindeki aralık (ağız kadrajdaki replik için klibin kendi
                sesinden yalnız o replik alınır), solma = başta ve sonda yumuşak geçiş (s)
    yataklar    [{dosya, baslangic, bitis, kazanc_db, gecis?}] (12.10.2026) — mekân başına KESİNTİSİZ ortam
                yatağı; klip sınırlarını aşar, kaynak kısa ise döngülenir; gecis = baş/son solması (varsayılan 1 s);
                iki yatak örtüşürse çapraz geçiş kendiliğinden oluşur (uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md)

Taslakta modelin ürettiği ses ATILIR (AGENTS.md §2); yalnız `ses` + `yataklar` ve `klip_sesi: true` parçalar çalar.
Yalnız standart kütüphane + ffmpeg/ffprobe. Çıkış kodu: 0 tamam · 1 timeline hatası · 2 kullanım.
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path


def zaman_yaz(s):
    d, sn = divmod(max(s, 0.0), 60)
    return f"{int(d):02d}:{sn:04.1f}"


def zaman_oku(metin):
    parca = metin.split(":")
    if len(parca) > 3:
        raise ValueError(metin)
    toplam = 0.0
    for p in parca:
        toplam = toplam * 60 + float(p)
    return toplam


def yukle(yol):
    yol = Path(yol)
    try:
        tl = json.loads(yol.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"⛔ timeline okunamadı: {yol} — {e}")
    kok = Path(str(tl.get("medya_kok", "."))).expanduser()
    if not kok.is_absolute():
        kok = (yol.parent / kok).resolve()
    return tl, kok


def coz(kok, dosya):
    p = Path(str(dosya)).expanduser()
    return p if p.is_absolute() else kok / p


GORSEL = {".png", ".jpg", ".jpeg", ".webp"}
PARCA_SURESI = 10.0   # 08.10.2026 sahip kararı: her çekim 10 s (film_dogrula CEKIM_SURESI ile aynı)
GECIS_TUR = {"kesme", "karisim", "karartma"}
GECIS_SURE = (0.2, 2.0)   # s — 12.10.2026: klipler arası keskin kesmeye çözüm; daha uzunu 10 s'lik çekimi yer


def gecis_oku(p):
    """Parçanın `gecis` alanı → (tür, süre). Yok ya da kesme → ('kesme', 0.0)."""
    g = p.get("gecis")
    if not g:
        return "kesme", 0.0
    if isinstance(g, str):
        parca = g.split()
        tur, sure = parca[0], float(parca[1]) if len(parca) > 1 else 0.5
    else:
        tur, sure = str(g.get("tur", "kesme")), float(g.get("sure", 0.5))
    return tur, (0.0 if tur == "kesme" else sure)


def sure_olc(dosya):
    """(süre, video var mı, ses var mı) — okunamazsa None. Görsel: süre sınırsız (animatik karesi)."""
    if Path(dosya).suffix.lower() in GORSEL:
        return (float("inf"), True, False) if Path(dosya).is_file() else None
    try:
        cikti = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type",
             "-of", "json", str(dosya)],
            capture_output=True, text=True, check=True).stdout
        bilgi = json.loads(cikti)
        turler = {s.get("codec_type") for s in bilgi.get("streams", [])}
        return float(bilgi["format"]["duration"]), "video" in turler, "audio" in turler
    except (subprocess.CalledProcessError, KeyError, ValueError, json.JSONDecodeError):
        return None


def denetle(tl, kok):
    """(hatalar, uyarılar, parça satırları, toplam süre)"""
    hata, uyari, satir = [], [], []
    parcalar = tl.get("parcalar") or []
    if not parcalar:
        hata.append("parcalar listesi boş")
    t = 0.0
    for i, p in enumerate(parcalar, 1):
        ad = f"#{i} {p.get('cekim', '?')}"
        try:
            g, c = float(p["giris"]), float(p["cikis"])
            dosya = coz(kok, p["dosya"])
        except (KeyError, TypeError, ValueError):
            hata.append(f"{ad}: cekim/dosya/giris/cikis alanı eksik ya da sayı değil")
            continue
        # 12.10.2026: geçiş (bu parçaya giriş) + klip sesi
        try:
            tur, gs = gecis_oku(p)
        except (ValueError, AttributeError, IndexError):
            hata.append(f"{ad}: gecis alanı okunamadı — {{\"tur\": kesme|karisim|karartma, \"sure\": s}}")
            tur, gs = "kesme", 0.0
        if tur not in GECIS_TUR:
            hata.append(f"{ad}: gecis türü '{tur}' — kesme | karisim | karartma")
            tur, gs = "kesme", 0.0
        if gs and not GECIS_SURE[0] <= gs <= GECIS_SURE[1]:
            hata.append(f"{ad}: gecis süresi {gs} s — {GECIS_SURE[0]}–{GECIS_SURE[1]} s arası")
        if gs and i == 1:
            uyari.append(f"{ad}: ilk parçada gecis yok sayılır (önünde parça yok; açılış karartması görsel parçayla yapılır)")
            tur, gs = "kesme", 0.0
        if gs and gs >= max(c - g, 0):
            hata.append(f"{ad}: gecis {gs} s parçanın süresinden ({c - g:.2f} s) kısa olmalı")
        klip_sesi = bool(p.get("klip_sesi", tl.get("klip_sesi", False)))
        try:
            klip_kazanc = float(p.get("klip_kazanc_db", 0))
        except (TypeError, ValueError):
            hata.append(f"{ad}: klip_kazanc_db sayı değil")
            klip_kazanc = 0.0
        bas = max(t - gs, 0.0)
        ortak = {"no": i, "cekim": p.get("cekim", "?"), "zincir": p.get("zincir"), "dosya": dosya, "giris": g, "cikis": c,
                 "bas": bas, "son": bas + max(c - g, 0), "gecis": (tur, gs), "klip_sesi": klip_sesi, "klip_kazanc_db": klip_kazanc}
        # 07.10.2026: dosya eksik/bozuk olsa da parça timeline'da yer kaplar → zaman giris/cikis'ten ilerler,
        # yoksa sonraki bütün parçalar sessizce öne kayardı (QA zamanı yanlış çekime eşlenirdi).
        olcum = sure_olc(dosya) if dosya.exists() else None
        if olcum is None:
            hata.append(f"{ad}: dosya yok → {dosya}" if not dosya.exists()
                        else f"{ad}: ffprobe okuyamadı (bozuk video?) → {dosya}")
            satir.append({**ortak, "kaynak_sure": None})
            t = bas + max(c - g, 0)
            continue
        sure, video_var, ses_var = olcum
        if not video_var:
            hata.append(f"{ad}: dosyada görüntü akışı yok → {dosya}")
        if klip_sesi and not ses_var:
            hata.append(f"{ad}: klip_sesi true ama dosyada ses akışı yok (Flow 'Return silent videos' kapatılmış mıydı?)")
        if klip_sesi and tur != "kesme" and gs:
            uyari.append(f"{ad}: klip sesi açık ve geçiş {tur} — replik geçiş aralığına ({gs:.1f} s) düşmesin")
        if g < 0:
            hata.append(f"{ad}: giris {g} < 0")
        if c <= g:
            hata.append(f"{ad}: cikis ({c}) giristen ({g}) büyük olmalı")
        if c > sure + 0.01:
            hata.append(f"{ad}: cikis {c:.2f} s, kaynağın süresini ({sure:.2f} s) aşıyor")
        if sure == float("inf") and g != 0:
            uyari.append(f"{ad}: görsel parçada giris yok sayılır (kare cikis-giris süre tutulur)")
        if 0 < c - g < 0.5:
            uyari.append(f"{ad}: {c - g:.2f} s — yarım saniyeden kısa parça")
        # 08.10.2026 sahip kararı: her çekim 10 s → her video parçası 10 s (görsel parça — kare/karartma — serbest)
        if sure != float("inf") and c > g and abs((c - g) - PARCA_SURESI) > 0.05:
            hata.append(f"{ad}: {c - g:.2f} s — her çekim {PARCA_SURESI:g} s (sahip kararı 08.10.2026)")
        satir.append({**ortak, "kaynak_sure": sure})
        t = bas + max(c - g, 0)
    # ZİNCİR: aynı zincirin halkaları timeline'da ardışık durur; dikişte en çok küçük kırpma (sahneleme)
    DIKIS_PAY = 0.30   # s — ≈6 kare @24 fps; daha fazlası zincir içinde görünür sıçrama riski
    gorulen, onceki = set(), None
    for s in satir:
        z = s.get("zincir")
        if z and z in gorulen and (onceki is None or onceki.get("zincir") != z):
            hata.append(f"#{s['no']} {s['cekim']}: zincir {z} parçaları ardışık değil (araya başka parça girmiş)")
        if z and onceki is not None and onceki.get("zincir") == z:
            kuyruk = (onceki["kaynak_sure"] or 0) - onceki["cikis"]
            if onceki["kaynak_sure"] not in (None, float("inf")) and kuyruk > DIKIS_PAY:
                uyari.append(f"zincir {z}: #{onceki['no']} {onceki['cekim']} sonundan {kuyruk:.2f} s kırpılmış — "
                             f"dikişte sıçrama riski (A′ ise bilinçli olmalı)")
            if s["giris"] > DIKIS_PAY:
                uyari.append(f"zincir {z}: #{s['no']} {s['cekim']} başından {s['giris']:.2f} s kırpılmış — dikişte sıçrama riski")
        if z and onceki is not None and onceki.get("zincir") == z and s["gecis"][1]:
            hata.append(f"zincir {z}: #{s['no']} {s['cekim']} dikişinde {s['gecis'][0]} geçişi — zincir içinde yalnız kesme (dikiş)")
        if z:
            gorulen.add(z)
        onceki = s
    # YATAKLAR (12.10.2026): mekân başına kesintisiz ortam yatağı, klipleri aşar
    for j, y in enumerate(tl.get("yataklar") or [], 1):
        ad = f"yatak #{j}"
        try:
            dosya = coz(kok, y["dosya"])
            b0, b1 = float(y.get("baslangic", 0)), float(y.get("bitis", t))
            float(y.get("kazanc_db", 0))
            yg = float(y.get("gecis", 1.0))
        except (KeyError, TypeError, ValueError):
            hata.append(f"{ad}: dosya/baslangic/bitis/kazanc_db/gecis alanı eksik ya da sayı değil")
            continue
        if not dosya.exists():
            hata.append(f"{ad}: dosya yok → {dosya}")
            continue
        olcum = sure_olc(dosya)
        if olcum is None or not olcum[2]:
            hata.append(f"{ad}: ses akışı okunamadı → {dosya}")
            continue
        if not 0 <= b0 < b1:
            hata.append(f"{ad}: aralık {b0}–{b1} s geçersiz")
            continue
        if b1 > t + 0.05:
            uyari.append(f"{ad}: {b1:.1f} s'de bitiyor, film {t:.1f} s — sonu kesilecek")
        if not 0 <= yg <= (b1 - b0) / 2:
            hata.append(f"{ad}: gecis {yg} s — 0 ile yatağın yarısı ({(b1 - b0) / 2:.1f} s) arasında")
        if olcum[0] + 0.05 < b1 - b0:
            uyari.append(f"{ad}: kaynak {olcum[0]:.1f} s, yatak {b1 - b0:.1f} s — döngülenir; döngü dikişi duyulmayan bir kayıt seç")
    for j, s in enumerate(tl.get("ses") or [], 1):
        ad = f"ses #{j}"
        try:
            dosya, bas = coz(kok, s["dosya"]), float(s.get("baslangic", 0))
            float(s.get("kazanc_db", 0))
        except (KeyError, TypeError, ValueError):
            hata.append(f"{ad}: dosya/baslangic/kazanc_db alanı eksik ya da sayı değil")
            continue
        if not dosya.exists():
            hata.append(f"{ad}: dosya yok → {dosya}")
            continue
        olcum = sure_olc(dosya)
        if olcum is None or not olcum[2]:
            hata.append(f"{ad}: ses akışı okunamadı → {dosya}")
            continue
        try:
            g, c = float(s.get("giris", 0)), float(s.get("cikis", olcum[0]))
            float(s.get("solma", 0))
        except (TypeError, ValueError):
            hata.append(f"{ad}: giris/cikis/solma sayı değil")
            continue
        if not 0 <= g < c <= olcum[0] + 0.05:
            hata.append(f"{ad}: aralık {g}–{c} s geçersiz (kaynak {olcum[0]:.2f} s)")
            continue
        uzun = c - g
        if bas < 0 or (t and bas >= t):
            hata.append(f"{ad}: baslangic {bas} s filmin dışında (0 – {t:.1f} s)")
        elif bas + uzun > t + 0.05:
            uyari.append(f"{ad}: {bas + uzun:.1f} s'de bitiyor, film {t:.1f} s — sonu kesilecek")
    return hata, uyari, satir, t


def kontrol(args):
    tl, kok = yukle(args.timeline)
    hata, uyari, satir, toplam = denetle(tl, kok)
    print(f"film: {tl.get('film', '?')} · medya: {kok}")
    gecisli = sum(1 for s in satir if s["gecis"][1])
    klipli = sum(1 for s in satir if s["klip_sesi"])
    print(f"parça: {len(satir)} · ses: {len(tl.get('ses') or [])} · yatak: {len(tl.get('yataklar') or [])} · "
          f"geçiş (karışım/karartma): {gecisli} · klip sesi: {klipli} parça · toplam: {zaman_yaz(toplam)} ({toplam:.2f} s)")
    for u in uyari:
        print(f"⚠️  {u}")
    for h in hata:
        print(f"⛔ {h}")
    print("✅ timeline geçerli" if not hata else f"⛔ {len(hata)} hata — taslak üretilmez")
    return 1 if hata else 0


def liste(args):
    tl, kok = yukle(args.timeline)
    hata, _, satir, toplam = denetle(tl, kok)
    if args.zaman is not None:
        try:
            z = zaman_oku(args.zaman)
        except ValueError:
            print(f"⛔ zaman okunamadı: {args.zaman} (MM:SS ya da MM:SS.s)")
            return 2
        for s in satir:
            if s["bas"] <= z < s["son"] or (z == toplam and s is satir[-1]):
                kaynak = s["giris"] + (z - s["bas"])
                print(f"{zaman_yaz(z)} → {s['cekim']} · {s['dosya'].name} içinde {kaynak:.2f} s")
                for h in hata:               # eşleme giris/cikis'ten; ama timeline sağlam değil → görünür kalsın
                    print(f"⛔ {h}")
                return 1 if hata else 0
        print(f"⛔ {zaman_yaz(z)} filmin dışında (toplam {zaman_yaz(toplam)})")
        return 1
    if args.kesmeler:                       # QA_PROMPTLARI/SUREKLILIK.md'ye yapıştırılan blok
        print("CUT LIST")
        for i, (a, b) in enumerate(zip(satir, satir[1:]), 1):
            ayni = "SAME" if a.get("zincir") and a.get("zincir") == b.get("zincir") else "?"
            gecis = f"  {b['gecis'][0]} {b['gecis'][1]:.1f}s" if b["gecis"][1] else ""
            print(f"{i:<3d}{zaman_yaz(b['bas'])}  {a['cekim']} → {b['cekim']}  {ayni}{gecis}")
        print("\n# '?' satırlarını FILM.md §2/§4'e bakarak SAME (aynı yer, kesintisiz zaman) ya da NEW yap.")
        return 1 if hata else 0
    print(f"| # | film zamanı | çekim | zincir | geçiş | dosya | kaynak aralığı | süre |")
    print(f"|--:|---|---|:--:|---|---|---|--:|")
    for s in satir:
        gecis = f"{s['gecis'][0]} {s['gecis'][1]:.1f}s" if s["gecis"][1] else "kesme"
        print(f"| {s['no']} | {zaman_yaz(s['bas'])}–{zaman_yaz(s['son'])} | {s['cekim']} | {s.get('zincir') or '—'} | {gecis} | "
              f"{s['dosya'].name} | {s['giris']:.2f}–{s['cikis']:.2f} | {s['cikis'] - s['giris']:.2f} |")
    print(f"\ntoplam {zaman_yaz(toplam)} ({toplam:.2f} s)")
    for h in hata:
        print(f"⛔ {h}")
    return 1 if hata else 0


def taslak(args):
    tl, kok = yukle(args.timeline)
    hata, uyari, satir, toplam = denetle(tl, kok)
    for u in uyari:
        print(f"⚠️  {u}")
    if hata:
        for h in hata:
            print(f"⛔ {h}")
        print("⛔ timeline geçersiz — önce `kontrol` ile düzelt")
        return 1
    try:
        gen, yuk = (int(x) for x in str(tl.get("cozunurluk", "1920x1080")).lower().split("x"))
        fps = float(tl.get("fps", 24))
    except ValueError:
        print("⛔ cozunurluk 'GENxYUK', fps sayı olmalı")
        return 1

    cmd, filtre = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"], []
    for i, s in enumerate(satir):
        uzun = f"{s['cikis'] - s['giris']:.3f}"
        if s["dosya"].suffix.lower() in GORSEL:      # animatik: kare süre boyunca tutulur
            cmd += ["-loop", "1", "-framerate", str(fps), "-t", uzun, "-i", str(s["dosya"])]
        else:
            cmd += ["-ss", f"{s['giris']:.3f}", "-t", uzun, "-i", str(s["dosya"])]
        filtre.append(f"[{i}:v]scale={gen}:{yuk}:force_original_aspect_ratio=decrease,"
                      f"pad={gen}:{yuk}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps},format=yuv420p,settb=AVTB[v{i}]")
    if not any(s["gecis"][1] for s in satir[1:]):
        filtre.append("".join(f"[v{i}]" for i in range(len(satir))) + f"concat=n={len(satir)}:v=1:a=0[v]")
    else:
        # 12.10.2026: kesme → concat · karisim → xfade fade · karartma → xfade fadeblack; her geçiş filmi süresi kadar kısaltır
        cur, akan = "[v0]", satir[0]["cikis"] - satir[0]["giris"]
        for i, s in enumerate(satir[1:], 1):
            tur, gs = s["gecis"]
            uzun = s["cikis"] - s["giris"]
            if gs:
                filtre.append(f"{cur}[v{i}]xfade=transition={'fade' if tur == 'karisim' else 'fadeblack'}:"
                              f"duration={gs:.3f}:offset={akan - gs:.3f}[x{i}]")
                akan += uzun - gs
            else:
                filtre.append(f"{cur}[v{i}]concat=n=2:v=1:a=0[x{i}]")
                akan += uzun
            cur = f"[x{i}]"
        filtre.append(f"{cur}null[v]")

    ses_etiket = []
    sesler = tl.get("ses") or []
    for j, s in enumerate(sesler):
        k = len(satir) + j
        kaynak = coz(kok, s["dosya"])
        cmd += ["-i", str(kaynak)]
        ms = int(round(float(s.get("baslangic", 0)) * 1000))
        g = float(s.get("giris", 0))
        c = float(s["cikis"]) if "cikis" in s else sure_olc(kaynak)[0]
        solma = min(float(s.get("solma", 0)), (c - g) / 2)
        zincir = f"[{k}:a]atrim=start={g:.3f}:end={c:.3f},asetpts=PTS-STARTPTS"
        if solma > 0:
            zincir += f",afade=t=in:d={solma:.3f},afade=t=out:st={c - g - solma:.3f}:d={solma:.3f}"
        filtre.append(f"{zincir},aresample=48000,adelay=delays={ms}:all=1,"
                      f"volume={float(s.get('kazanc_db', 0))}dB[a{j}]")
        ses_etiket.append(f"[a{j}]")
    # 12.10.2026 klip sesi: model sesi replik taşıyan parçanın kendi sesi, filmdeki yerine (geçiş kaymaları dahil)
    for i, s in enumerate(satir):
        if s["klip_sesi"] and s["dosya"].suffix.lower() not in GORSEL:
            uzun = s["cikis"] - s["giris"]
            filtre.append(f"[{i}:a]atrim=0:{uzun:.3f},asetpts=PTS-STARTPTS,aresample=48000,"
                          f"afade=t=in:d=0.05,afade=t=out:st={uzun - 0.05:.3f}:d=0.05,"
                          f"adelay=delays={int(round(s['bas'] * 1000))}:all=1,volume={s['klip_kazanc_db']}dB[k{i}]")
            ses_etiket.append(f"[k{i}]")
    # 12.10.2026 ortam yatakları: mekân başına kesintisiz, klip sınırlarını aşar; örtüşen yataklar çapraz geçer
    yataklar = tl.get("yataklar") or []
    for j, y in enumerate(yataklar):
        k = len(satir) + len(sesler) + j
        kaynak = coz(kok, y["dosya"])
        cmd += ["-i", str(kaynak)]
        b0 = float(y.get("baslangic", 0))
        b1 = min(float(y.get("bitis", toplam)), toplam)
        uzun = b1 - b0
        yg = min(float(y.get("gecis", 1.0)), uzun / 2)
        zincir = f"[{k}:a]aloop=loop=-1:size=2147483647,atrim=0:{uzun:.3f},asetpts=PTS-STARTPTS,aresample=48000"
        if yg > 0:
            zincir += f",afade=t=in:d={yg:.3f},afade=t=out:st={uzun - yg:.3f}:d={yg:.3f}"
        filtre.append(f"{zincir},adelay=delays={int(round(b0 * 1000))}:all=1,volume={float(y.get('kazanc_db', 0))}dB[y{j}]")
        ses_etiket.append(f"[y{j}]")
    if ses_etiket:
        filtre.append("".join(ses_etiket) + f"amix=inputs={len(ses_etiket)}:normalize=0:duration=longest,apad[a]")

    cikti = Path(args.o).expanduser() if args.o else \
        kok / "cikti" / f"taslak_{dt.datetime.now():%Y%m%d_%H%M%S}.mp4"
    cikti.parent.mkdir(parents=True, exist_ok=True)
    cmd += ["-filter_complex", ";".join(filtre), "-map", "[v]"]
    cmd += ["-map", "[a]", "-c:a", "aac", "-b:a", "192k", "-ar", "48000"] if ses_etiket else ["-an"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-t", f"{toplam:.3f}",
            "-movflags", "+faststart", str(cikti)]
    sonuc = subprocess.run(cmd, capture_output=True, text=True)
    if sonuc.returncode != 0:
        print(f"⛔ ffmpeg hata verdi:\n{sonuc.stderr.strip()}")
        return 1
    olcum = sure_olc(cikti)
    print(f"✅ taslak: {cikti}")
    if olcum:
        print(f"   süre {olcum[0]:.2f} s (beklenen {toplam:.2f} s) · ses {'var' if olcum[2] else 'yok'}")
    return 0


HEDEF_LUFS, HEDEF_TEPE, HEDEF_LRA = -14.0, -1.0, 11.0   # ses-tasarimcisi teslim değerleri


def loudnorm_olc(dosya, filtre_ek=""):
    """ffmpeg loudnorm ölçümü → dict (input_i, input_tp, input_lra, input_thresh, target_offset)."""
    af = f"loudnorm=I={HEDEF_LUFS}:TP={HEDEF_TEPE}:LRA={HEDEF_LRA}{filtre_ek}:print_format=json"
    sonuc = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(dosya), "-af", af,
                            "-f", "null", "-"], capture_output=True, text=True)
    metin = sonuc.stderr
    i = metin.rfind("{")
    if sonuc.returncode != 0 or i < 0:
        return None
    try:
        return json.loads(metin[i:metin.rfind("}") + 1])
    except json.JSONDecodeError:
        return None


def yukseklik(args):
    """İki aşamalı DOĞRUSAL loudnorm: dinamik aralık korunur, bütün miks hedefe kaydırılır."""
    dosya = Path(args.video).expanduser()
    olcum = sure_olc(dosya)
    if olcum is None or not olcum[2]:
        print(f"⛔ ses akışı yok ya da okunamadı → {dosya}")
        return 1
    m = loudnorm_olc(dosya)
    if m is None:
        print("⛔ loudnorm ölçümü alınamadı")
        return 1
    print(f"ölçüm: {float(m['input_i']):.1f} LUFS · tepe {float(m['input_tp']):.1f} dBTP · "
          f"LRA {float(m['input_lra']):.1f} LU  (hedef {HEDEF_LUFS:g} LUFS · ≤ {HEDEF_TEPE:g} dBTP)")
    if not args.uygula:
        fark = float(m["input_i"]) - HEDEF_LUFS
        print("✅ hedefte" if abs(fark) <= 1 and float(m["input_tp"]) <= HEDEF_TEPE else
              f"⚠️  {fark:+.1f} LU fark — `--uygula -o <final.mp4>` ile düzelt")
        return 0
    cikti = Path(args.o).expanduser() if args.o else dosya.with_name(dosya.stem + "_lufs" + dosya.suffix)
    af = (f"loudnorm=I={HEDEF_LUFS}:TP={HEDEF_TEPE}:LRA={HEDEF_LRA}:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
          f"offset={m['target_offset']}:linear=true,aresample=48000")
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(dosya), "-af", af]
    cmd += (["-c:v", "copy"] if olcum[1] else []) + ["-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                                                     "-movflags", "+faststart", str(cikti)]
    sonuc = subprocess.run(cmd, capture_output=True, text=True)
    if sonuc.returncode != 0:
        print(f"⛔ ffmpeg hata verdi:\n{sonuc.stderr.strip()}")
        return 1
    son = loudnorm_olc(cikti)
    print(f"✅ final: {cikti}")
    if son:
        print(f"   sonra: {float(son['input_i']):.1f} LUFS · tepe {float(son['input_tp']):.1f} dBTP")
        if float(son["input_tp"]) > HEDEF_TEPE + 0.3:
            print("   ⚠️  doğrusal kaydırma tepeyi aştı — miksteki en yüksek anı (patlama/vuruş) kıs, tekrar koş")
    return 0


def main():
    ap = argparse.ArgumentParser(description="timeline.json → kontrol · liste · taslak · yükseklik")
    alt = ap.add_subparsers(dest="komut", required=True)
    k = alt.add_parser("kontrol", help="dosyalar ve aralıklar geçerli mi")
    k.add_argument("timeline")
    k.set_defaults(fn=kontrol)
    l = alt.add_parser("liste", help="film zamanı → çekim tablosu")
    l.add_argument("timeline")
    l.add_argument("--zaman", help="tek bir film zamanını çekime çevir (MM:SS.s)")
    l.add_argument("--kesmeler", action="store_true", help="SÜREKLİLİK promptu için kesme listesi bas")
    l.set_defaults(fn=liste)
    t = alt.add_parser("taslak", help="seçilen aralıklardan taslak film üret")
    t.add_argument("timeline")
    t.add_argument("-o", help="çıktı dosyası (varsayılan: <medya_kok>/cikti/taslak_<zaman>.mp4)")
    t.set_defaults(fn=taslak)
    y = alt.add_parser("yukseklik", help=f"ses yüksekliğini ölç / {HEDEF_LUFS:g} LUFS'a getir (iki aşamalı, doğrusal)")
    y.add_argument("video")
    y.add_argument("--uygula", action="store_true", help="ölçümü uygula ve yeni dosya yaz")
    y.add_argument("-o", help="çıktı (varsayılan: <ad>_lufs.<uzantı>)")
    y.set_defaults(fn=yukseklik)
    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
