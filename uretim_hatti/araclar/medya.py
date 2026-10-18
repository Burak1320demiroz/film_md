#!/usr/bin/env python3
"""Medya alımı ve gerçek durum — ~/film_medya/<FILM>/ ile film klasörünü karşılaştırır (16.10.2026).

    python3 uretim_hatti/araclar/medya.py durum <film klasörü> [--yaz] [--medya <klasör>]
    python3 uretim_hatti/araclar/medya.py al    <film klasörü> [--yaz] [--medya <klasör>]
    python3 uretim_hatti/araclar/medya.py bol   <montaj.mp4> <film klasörü> [--esik 0.3] [--medya <klasör>]

durum  ref · kare · ham · ses · cikti klasörlerini FILM.md §3-§4, NOTLAR.md (DENEMELER · İŞARETLEME) ve timeline.json ile
       karşılaştırır: çekim başına kare · deneme · işaret · seçim; adı kurala uymayan dosyalar; kayıtsız denemeler;
       dosyalardan çıkan GERÇEK durum ↔ DURUM.md FAZ. --yaz → ODA/MEDYA_DURUMU.md (her koşuda yeniden üretilir, elle
       düzenlenmez). Fable her açılışta koşar (yeni-film §0): durum dosyadan okunur, hafızadan değil.
al     NOTLAR.md DENEMELER'de satırı olmayan her ham/Cxx_dN.* için satır yazar: süre · ses akışı · araç/mod (FLOW satırı) ·
       prompt (grup dosyası + p:<sha8>, çekimin BUGÜNKÜ prompt metninden) · girdi (EKLE satırındaki kare + referans no).
       Sonuç "⏳ işaret bekliyor" kalır; ✅/❌ sahibin işi. Aynı deneme iki kez eklenmez. --yaz yoksa yalnız gösterir.
       ref/ dosyalarının SHA-256 ilk 12'sini §3 Onay için yazar (FILM.md'ye yazmaz; Fable kopyalar).
bol    hat dışında yapılmış montajı kesmelerinden böler (ffmpeg scene): parça başına başlangıç · bitiş · süre · ilk/orta kare
       (analiz/montaj/<ad>/) · kare/Cxx.png varsa en benzer başlangıç karesi. QA'daki çekim numarası = kesme sırası, plan
       numarası değildir (16.10.2026: MAYDAY · SKY_CATCH QA numaraları kaymıştı) → NOTLAR.md MONTAJ EŞLEMESİ, Fable doğrular.

Dosya adları (uretim_hatti/README.md § Medya): ref/<No>.<AD>_v<k>.png · kare/Cxx.png · kare/Zk.n.png · ham/Cxx_dN.mp4 ·
ses/R01.wav … · cikti/taslak_*.mp4 · final.mp4. Medya kökü: --medya > künye MEDYA > ~/film_medya/<klasör adı>.
Medyayı değiştirmez, taşımaz, silmez; yalnız analiz/montaj/ altına kare yazar. Yalnız standart kütüphane + ffmpeg/ffprobe.
Çıkış kodu: 0 tamam · 1 bulunamayan girdi (film/montaj) ya da bol'da kesme yok · 2 kullanım.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import film_dogrula as fd   # noqa: E402  (bolum · tablo · bos · BASLIKLAR — yalnız okuma)

VIDEO = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}
GORSEL = {".png", ".jpg", ".jpeg", ".webp"}
SES = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg"}
HAM_AD = re.compile(r"^(C\d{2,3})_d(\d+)$")
KARE_AD = re.compile(r"^(C\d{2,3}|Z\d+\.\d+)$")
REF_AD = re.compile(r"^(\d+)\.([A-Za-z0-9_\-]+)_v(\d+)$")
DENEME = re.compile(r"\b(C\d{2,3})(?:_d|\s*\|\s*d?)(\d+)\b")


# ── okuma ──────────────────────────────────────────────────────────────────
def oku(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def medya_koku(klasor, film, zorla):
    if zorla:
        return Path(zorla).expanduser()
    m = re.search(r"^MEDYA\s+(\S+)", film, re.M)
    if m and "<" not in m.group(1):
        return Path(m.group(1)).expanduser()
    return Path.home() / "film_medya" / klasor.resolve().name


def cekim_listesi(film):
    """§4: [(no, mod)] sırasıyla."""
    return [(r[0], r[6] if len(r) > 6 else "") for r in fd.tablo(fd.bolum(film, fd.BASLIKLAR[3]))]


def referans_listesi(film):
    """§3: {No: (dosya kökü, sha)} — yalnız numaralı (10.10.2026) biçim."""
    b = fd.bolum(film, fd.BASLIKLAR[2]).split("\n### ", 1)[0]
    if not re.search(r"^\|\s*No\s*\|", b, re.M):
        return {}
    refs = {}
    for r in fd.tablo(b, r"^\|\s*\d+\s*\|"):
        if len(r) >= 3:
            m = REF_AD.match(Path(r[2].strip("` ")).stem)
            refs[r[0]] = ((f"{m.group(1)}.{m.group(2)}" if m else r[2].strip("` ")), r[4].strip() if len(r) > 4 else "")
    return refs


def prompt_bolumleri(klasor):
    """{Cxx: (dosya adı, gövde)} — PILOT.md önce, grup dosyaları üstüne yazar (F5 sürümü geçerlidir)."""
    dosyalar = sorted((klasor / "PROMPTLAR").glob("*.md"), key=lambda f: (not f.name.upper().startswith("PILOT"), f.name))
    bul = {}
    for f in dosyalar:
        for m in re.finditer(r"^## (C\d{2,3})(?=\s).*?(?=^## |\Z)", oku(f), re.M | re.S):
            bul[m.group(1)] = (f.name, m.group(0))
    return bul


def prompt_kimligi(govde):
    """p:<sha8> — çekimin Görsel + Video metninden; metin değişirse kimlik değişir."""
    bloklar = re.findall(r"```text\n(.*?)```", govde, re.S)
    return "p:" + hashlib.sha256("\n---\n".join(b.strip() for b in bloklar).encode()).hexdigest()[:8] if bloklar else "p:—"


def girdi(govde):
    bas = govde.split("### ", 1)[0]
    ekle = " ".join(re.findall(r"^(?:EKLE|KAYNAK)\s+(.*)$", bas, re.M))
    kare = re.findall(r"kare/([CZ][\d.]+)\.png", ekle)
    ref = re.findall(r"ref/(\d+)\.", ekle)
    parca = ([f"kare/{', '.join(dict.fromkeys(kare))}"] if kare else []) + ([f"ref {','.join(dict.fromkeys(ref))}"] if ref else [])
    return " + ".join(parca) or "—"


def flow_modu(govde):
    m = re.search(r"^FLOW\s+(.+)$", govde, re.M)
    return m.group(1).strip() if m else "?"


def tablo_satirlari(metin, baslik):
    """Bölümdeki ilk Markdown tablosu: (başlık hücreleri, [satır hücreleri], son satırın metindeki bitiş konumu)."""
    i = metin.find(baslik)
    if i < 0:
        return None, [], -1
    j = metin.find("\n## ", i + len(baslik))
    j = j if j > 0 else len(metin)
    ust, satirlar, son, konum = None, [], -1, i
    for s in metin[i:j].splitlines(keepends=True):
        konum += len(s)
        t = s.strip()
        if not t.startswith("|"):
            if ust is not None:
                break
            continue
        hucre = [h.strip() for h in t.strip("|").split("|")]
        if ust is None:
            ust = hucre
        elif not re.fullmatch(r"[\s:|-]+", t):
            satirlar.append(hucre)
        son = konum
    return ust, satirlar, son


def kayitli_denemeler(notlar):
    """NOTLAR DENEMELER'deki (Cxx, N) çiftleri — yer tutucu satır sayılmaz."""
    _ust, satirlar, _ = tablo_satirlari(notlar, "## DENEMELER")
    k = set()
    for r in satirlar:
        metin = " | ".join(r)
        if "<GG.AA>" in metin:
            continue
        m = DENEME.search(metin)
        if m:
            k.add((m.group(1), int(m.group(2))))
    return k


def isaretler(notlar):
    """İŞARETLEME + DENEMELER Sonuç: (Cxx, N) → ✅ | ❌."""
    isr = {}
    for baslik in ("## DENEMELER", "## İŞARETLEME"):
        _ust, satirlar, _ = tablo_satirlari(notlar, baslik)
        for r in satirlar:
            metin = " | ".join(r)
            if "<GG.AA>" in metin:
                continue
            m = DENEME.search(metin)
            if m and ("✅" in metin or "❌" in metin):
                isr[(m.group(1), int(m.group(2)))] = "✅" if "✅" in metin else "❌"
    return isr


def secilenler(klasor, medya):
    f = klasor / "timeline.json"
    try:
        tl = json.loads(oku(f) or "{}")
    except json.JSONDecodeError:
        return set(), ["timeline.json okunamadı"]
    kok = Path(str(tl.get("medya_kok") or medya)).expanduser()
    if not kok.is_absolute():
        kok = (klasor / kok).resolve()
    sec, sorun = set(), []
    for p in tl.get("parcalar", []) or []:
        d = str(p.get("dosya", ""))
        if not d or "<" in d:
            continue
        if not (Path(d).expanduser() if Path(d).expanduser().is_absolute() else kok / d).exists():
            sorun.append(f"timeline: {p.get('cekim', '?')} → {d} yok (şablon satırı ya da taşınmış dosya)")
        elif Path(d).suffix.lower() in VIDEO:
            sec.add(str(p.get("cekim", "")))
    return sec, sorun


def olc(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
                        "-of", "json", str(p)], capture_output=True, text=True)
    try:
        j = json.loads(r.stdout or "{}")
    except json.JSONDecodeError:
        return None
    akis = j.get("streams", [])
    if not akis:
        return None
    v = next((s for s in akis if s.get("codec_type") == "video"), {})
    return {"sure": float(j.get("format", {}).get("duration") or 0), "ses": any(s.get("codec_type") == "audio" for s in akis),
            "boyut": f"{v.get('width')}x{v.get('height')}" if v else "?"}


def dosyalar(d, uzanti):
    return sorted(f for f in d.iterdir() if f.is_file() and f.suffix.lower() in uzanti) if d.is_dir() else []


# ── durum ──────────────────────────────────────────────────────────────────
def tara(klasor, medya_zorla=None):
    film = oku(klasor / "FILM.md")
    notlar = oku(klasor / "NOTLAR.md")
    medya = medya_koku(klasor, film, medya_zorla)
    cekimler = cekim_listesi(film)
    nolar = [c for c, _ in cekimler]
    refs = referans_listesi(film)
    adsiz = []

    ref_var = {}
    for f in dosyalar(medya / "ref", GORSEL):
        m = REF_AD.match(f.stem)
        if m:
            ref_var.setdefault(m.group(1), []).append(f)
        else:
            adsiz.append(f"ref/{f.name} → ref/<No>.<AD>_v<k>.png")
    kare_var = set()
    for f in dosyalar(medya / "kare", GORSEL):
        if KARE_AD.match(f.stem):
            kare_var.add(f.stem)
        else:
            adsiz.append(f"kare/{f.name} → kare/Cxx.png")
    ham = {}
    for f in dosyalar(medya / "ham", VIDEO):
        m = HAM_AD.match(f.stem)
        if m:
            ham.setdefault(m.group(1), []).append((int(m.group(2)), f))
        else:
            adsiz.append(f"ham/{f.name} → ham/Cxx_dN.mp4")
    for d in ham.values():
        d.sort()
    ses = dosyalar(medya / "ses", SES)
    cikti = dosyalar(medya / "cikti", VIDEO)
    taslak = [f for f in cikti if f.stem.startswith("taslak")]
    final = [f for f in cikti if f.stem.startswith("final")]
    montaj = [f for f in cikti if f not in taslak and f not in final]

    kayit = kayitli_denemeler(notlar)
    isr = isaretler(notlar)
    sec, tl_sorun = secilenler(klasor, medya)
    denemeler = {(c, n) for c, d in ham.items() for n, _ in d}
    return {
        "film": film, "medya": medya, "cekimler": cekimler, "nolar": nolar, "refs": refs, "ref_var": ref_var,
        "kare_var": kare_var, "ham": ham, "ses": ses, "taslak": taslak, "final": final, "montaj": montaj, "adsiz": adsiz,
        "kayit": kayit, "isr": isr, "sec": sec, "tl_sorun": tl_sorun, "denemeler": denemeler,
        "kayitsiz": sorted(denemeler - kayit), "dosyasiz": sorted(kayit - denemeler),
        "durum_faz": (re.search(r"^FAZ\s+(\d+)", oku(klasor / "ODA" / "DURUM.md"), re.M) or [None, None])[1],
        "durum_adim": (re.search(r"^ADIM\s+(\S+)", oku(klasor / "ODA" / "DURUM.md"), re.M) or [None, "—"])[1],
    }


def gercek_durum(s):
    n, den = len(s["nolar"]), len([c for c in s["nolar"] if c in s["ham"]])
    if s["final"]:
        return 9, f"F8 bitti — cikti/{s['final'][0].name} var → F9 paket"
    if s["taslak"]:
        return 8, f"F8 seçim + kurgu — {len(s['taslak'])} taslak var"
    if s["montaj"]:
        return 8, f"F8 — hat dışı montaj var ({', '.join(f.name for f in s['montaj'])}) → medya.py bol ile hatta al"
    if s["ham"]:
        return 7, f"F7 üretim — {den}/{n} çekim denendi"
    if s["kare_var"] or s["ref_var"]:
        return 7, "F7 başı — referans/kare var, video yok"
    return None, "medya yok"


def ozet_satirlari(s):
    n = len(s["nolar"])
    kare_gerek = [c for c, mod in s["cekimler"] if mod == "Frames to Video"]
    ref_eksik = [ad for no, (ad, _sha) in s["refs"].items() if no not in s["ref_var"]]
    sha_bos = [no for no, (_ad, sha) in s["refs"].items() if no in s["ref_var"] and fd.bos(sha)]
    secili_ok = len([c for c in s["nolar"] if any(s["isr"].get((c, k)) == "✅" for k, _ in s["ham"].get(c, []))])
    faz, metin = gercek_durum(s)
    satir = [f"GERÇEK DURUM  {metin}"]
    df = s["durum_faz"]
    if faz is not None and df is not None and int(df) < faz:
        satir.append(f"⚠️  DURUM.md FAZ {df} · ADIM {s['durum_adim']} — dosyalar daha ileriyi gösteriyor ({metin}): DURUM'u dosyaya göre güncelle")
    elif faz is not None:
        satir.append(f"   DURUM.md FAZ {df} · ADIM {s['durum_adim']}")
    satir += [
        f"ref      {len([r for r in s['refs'] if r in s['ref_var']])}/{len(s['refs'])}"
        + (f" · eksik: {' '.join(ref_eksik)}" if ref_eksik else "") + (f" · §3 SHA boş: {' '.join(sha_bos)}" if sha_bos else ""),
        f"kare     {len([c for c in kare_gerek if c in s['kare_var']])}/{len(kare_gerek)} (Frames to Video çekimleri)",
        f"ham      {len(s['denemeler'])} deneme · {len(s['ham'])}/{n} çekim denendi",
        f"ses      {len(s['ses'])} dosya",
        f"cikti    taslak {len(s['taslak'])} · final {'var' if s['final'] else 'yok'}"
        + (f" · hat dışı montaj {len(s['montaj'])}" if s["montaj"] else ""),
        f"kayıt    DENEMELER {len(s['denemeler']) - len(s['kayitsiz'])}/{len(s['denemeler'])} deneme kayıtlı"
        + (" → medya.py al" if s["kayitsiz"] else "")
        + f" · işaretli {len([d for d in s['denemeler'] if d in s['isr']])}/{len(s['denemeler'])}",
        f"timeline {len(s['sec'])}/{n} çekim seçili",
        f"TESLİM   ref {len([r for r in s['refs'] if r in s['ref_var']])}/{len(s['refs'])} · denenen {len(s['ham'])}/{n} · "
        f"✅ {secili_ok}/{n} · timeline {len(s['sec'])}/{n} · taslak {'var' if s['taslak'] else '—'} · "
        f"final {'var' if s['final'] else '—'}",
    ]
    for a in s["adsiz"]:
        satir.append(f"⚠️  adı kurala uymayan: {a}")
    for c, k in s["dosyasiz"]:
        satir.append(f"⚠️  NOTLAR DENEMELER'de {c} d{k} var, ham/{c}_d{k}.* yok")
    satir += [f"⚠️  {x}" for x in s["tl_sorun"]]
    return satir


def cekim_tablosu(s):
    t = ["| Çekim | Mod | Kare | Denemeler | İşaret | Timeline |", "|:--:|---|:--:|---|---|:--:|"]
    for c, mod in s["cekimler"]:
        den = s["ham"].get(c, [])
        isr = " ".join(f"{s['isr'][(c, k)]}d{k}" for k, _ in den if (c, k) in s["isr"])
        t.append(f"| {c} | {mod} | {'✅' if c in s['kare_var'] else ('—' if mod != 'Frames to Video' else '⬜')} | "
                 f"{' '.join(f'd{k}' for k, _ in den) or '—'} | {isr or ('⏳' if den else '—')} | {'✅' if c in s['sec'] else '—'} |")
    return t


def durum(a):
    klasor = Path(a.klasor)
    if not (klasor / "FILM.md").exists():
        print(f"⛔ {klasor}/FILM.md yok")
        return 1
    s = tara(klasor, a.medya)
    print(f"film: {klasor} · medya: {s['medya']}{'' if s['medya'].is_dir() else ' (klasör yok)'}")
    ozet = ozet_satirlari(s)
    print("\n".join(ozet))
    tab = cekim_tablosu(s)
    print("\n".join(tab))
    if a.yaz:
        f = klasor / "ODA" / "MEDYA_DURUMU.md"
        f.parent.mkdir(exist_ok=True)
        f.write_text(f"# 📦 MEDYA DURUMU — {klasor.name}\n\n> `medya.py durum --yaz` üretir ({dt.datetime.now():%d.%m.%Y %H:%M}); "
                     f"elle düzenlenmez, her koşuda yeniden yazılır. Medya: `{s['medya']}`.\n\n```\n" + "\n".join(ozet)
                     + "\n```\n\n" + "\n".join(tab) + "\n", encoding="utf-8")
        print(f"→ {f}")
    return 0


# ── al ─────────────────────────────────────────────────────────────────────
def al(a):
    klasor = Path(a.klasor)
    if not (klasor / "FILM.md").exists():
        print(f"⛔ {klasor}/FILM.md yok")
        return 1
    s = tara(klasor, a.medya)
    pb = prompt_bolumleri(klasor)
    yeni = []
    for c, k in s["kayitsiz"]:
        f = dict(s["ham"][c])[k]
        o = olc(f) or {}
        ad, govde = pb.get(c, ("—", ""))
        yeni.append({
            "tarih": dt.datetime.fromtimestamp(f.stat().st_mtime).strftime("%d.%m"), "cekim": c, "deneme": f"d{k}",
            "mod": flow_modu(govde) if govde else "?", "prompt": f"{Path(ad).stem} · {prompt_kimligi(govde)}" if govde else "?",
            "girdi": girdi(govde) if govde else "?",
            "sure": (f"{o['sure']:.1f} s · {'ses var' if o.get('ses') else 'sessiz'} · {o.get('boyut', '?')}" if o else "okunamadı"),
            "sonuc": "⏳ işaret bekliyor", "kredi": ""})
    print(f"film: {klasor} · medya: {s['medya']} · kayıtsız deneme: {len(yeni)}")
    notlar_f = klasor / "NOTLAR.md"
    notlar = oku(notlar_f)
    ust, _satir, son = tablo_satirlari(notlar, "## DENEMELER")
    if ust is None:
        print("⛔ NOTLAR.md'de '## DENEMELER' tablosu yok (şablon: uretim_hatti/SABLON/NOTLAR.md)")
        return 1
    satirlar = []
    for d in yeni:
        hucre = []
        for h in ust:
            hl = h.lower()
            if hl.startswith("tarih"):
                hucre.append(d["tarih"])
            elif hl.startswith("çekim"):
                hucre.append(d["cekim"])
            elif hl.startswith("deneme"):
                hucre.append(d["deneme"])
            elif "mod" in hl or "araç" in hl:
                hucre.append(d["mod"])
            elif hl.startswith("prompt"):
                # eski şablonda (16.10.2026 öncesi) girdi ve süre sütunu yok → prompt sütununa eklenir
                eski = not any(x.lower().startswith(("girdi", "süre")) for x in ust)
                hucre.append(d["prompt"] + (f" · girdi: {d['girdi']} · {d['sure']}" if eski else ""))
            elif hl.startswith("girdi"):
                hucre.append(d["girdi"])
            elif hl.startswith("süre"):
                hucre.append(d["sure"])
            elif hl.startswith("sonuç"):
                hucre.append(d["sonuc"])
            else:
                hucre.append(d.get("kredi", ""))
        satirlar.append("| " + " | ".join(hucre) + " |")
    for s_ in satirlar:
        print(s_)
    for no, fl in sorted(s["ref_var"].items(), key=lambda x: int(x[0])):
        for f in fl:
            sha = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
            kayit = s["refs"].get(no, ("", ""))[1]
            durum_ = "§3 ile aynı" if kayit == sha else ("§3'e yaz" if fd.bos(kayit) else f"§3'te {kayit} — DEĞİŞMİŞ (sürüm artmalı)")
            print(f"ref/{f.name}  SHA {sha}  {durum_}")
    if a.yaz and satirlar:
        if not notlar.endswith("\n") and son == len(notlar):
            notlar += "\n"
        notlar_f.write_text(notlar[:son] + "\n".join(satirlar) + "\n" + notlar[son:], encoding="utf-8")
        print(f"→ {notlar_f}: DENEMELER'e {len(satirlar)} satır eklendi")
    elif satirlar:
        print("(yazmak için --yaz)")
    return 0


# ── bol ────────────────────────────────────────────────────────────────────
def _ff(args):
    return subprocess.run(["ffmpeg", "-hide_banner", "-nostdin", *map(str, args)], capture_output=True, text=True)


def kesmeler(video, esik):
    r = _ff(["-i", video, "-vf", f"select='gt(scene,{esik})',showinfo", "-an", "-f", "null", "-"])
    zaman = sorted(float(x) for x in re.findall(r"pts_time:([\d.]+)", r.stderr))
    birlesik = []
    for z in zaman:
        if not birlesik or z - birlesik[-1] > 0.5:
            birlesik.append(z)
    return birlesik


def kucuk(gorsel_ya_da_video, t=None):
    """32×18 gri piksel dizisi (benzerlik için)."""
    on = ["-ss", f"{t:.3f}"] if t is not None else []
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostdin", "-loglevel", "error", *on, "-i", str(gorsel_ya_da_video),
                        "-frames:v", "1", "-vf", "scale=32:18,format=gray", "-f", "rawvideo", "-"], capture_output=True)
    return list(r.stdout) if len(r.stdout) == 32 * 18 else None


def benzerlik(x, y):
    if not x or not y:
        return None
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sx = sum((a - mx) ** 2 for a in x) ** 0.5
    sy = sum((b - my) ** 2 for b in y) ** 0.5
    if sx < 1e-6 or sy < 1e-6:
        return 1.0 - sum(abs(a - b) for a, b in zip(x, y)) / (255.0 * n)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def zy(s):
    d, sn = divmod(max(s, 0.0), 60)
    return f"{int(d):02d}:{sn:04.1f}"


def bol(a):
    video, klasor = Path(a.montaj), Path(a.klasor)
    if not video.exists():
        print(f"⛔ montaj yok: {video}")
        return 1
    film = oku(klasor / "FILM.md")
    medya = medya_koku(klasor, film, a.medya)
    o = olc(video)
    if not o:
        print(f"⛔ ffprobe okuyamadı: {video}")
        return 1
    kes = kesmeler(video, a.esik)
    sinir = [0.0] + kes + [o["sure"]]
    parcalar = [(b, s) for b, s in zip(sinir, sinir[1:]) if s - b > 0.05]
    hedef = medya / "analiz" / "montaj" / video.stem
    hedef.mkdir(parents=True, exist_ok=True)
    kareler = {f.stem: kucuk(f) for f in dosyalar(medya / "kare", GORSEL) if KARE_AD.match(f.stem)}
    n_plan = len(cekim_listesi(film))
    satir = [f"| Kesme sırası (QA no) | Başlangıç | Bitiş | Süre | İlk kare | En benzer başlangıç karesi | Not |",
             "|:--:|---|---|:--:|---|---|---|"]
    tsv = ["sira\tbaslangic\tbitis\tsure\tilk\torta\toneri\tbenzerlik"]
    for i, (b, s) in enumerate(parcalar, 1):
        ilk, orta = hedef / f"{i:02d}_ilk.png", hedef / f"{i:02d}_orta.png"
        for t, p in ((min(b + 0.1, s - 0.02), ilk), ((b + s) / 2, orta)):
            _ff(["-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", video, "-frames:v", "1", p])
        oneri, skor, not_ = "—", None, []
        if kareler:
            k = kucuk(video, min(b + 0.1, s - 0.02))
            puan = sorted(((benzerlik(k, v), ad) for ad, v in kareler.items() if v), key=lambda x: -(x[0] or -9))
            if puan and puan[0][0] is not None:
                skor = puan[0][0]
                fark = skor - (puan[1][0] or 0) if len(puan) > 1 else 1
                oneri = f"{puan[0][1]} ({skor:.2f})" + ("" if skor >= 0.5 and fark >= 0.05 else " ?")
        sure = s - b
        if sure < 8:
            not_.append("kısa — ara parça ya da kırpılmış çekim")
        elif sure > 12:
            not_.append("uzun — iki çekim birleşmiş olabilir (--esik düşür) ya da uzatma")
        satir.append(f"| {i} | {zy(b)} | {zy(s)} | {sure:.1f} | `{ilk.relative_to(medya)}` | {oneri} | {' · '.join(not_)} |")
        tsv.append(f"{i}\t{b:.2f}\t{s:.2f}\t{sure:.2f}\t{ilk.name}\t{orta.name}\t{oneri}\t{'' if skor is None else f'{skor:.3f}'}")
    (hedef / "bolum.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    (hedef / "bolum.md").write_text(f"# MONTAJ EŞLEMESİ — {video.name}\n\n> `medya.py bol` ({dt.datetime.now():%d.%m.%Y}) · "
                                    f"eşik {a.esik} · {len(parcalar)} parça · plan {n_plan} çekim. Öneri sütunu benzerliktir, "
                                    f"karar değil: Fable kareyle doğrular.\n\n" + "\n".join(satir) + "\n", encoding="utf-8")
    print(f"montaj: {video} · {o['sure']:.1f} s · {len(kes)} kesme → {len(parcalar)} parça · plan {n_plan} çekim · "
          f"başlangıç karesi {len(kareler)}")
    if n_plan and len(parcalar) != n_plan:
        print(f"⚠️  parça sayısı ({len(parcalar)}) ≠ plan çekim sayısı ({n_plan}): QA'daki 'Cxx' numaraları plan numarası DEĞİL — "
              f"eşlemeyi bu tablodan yap")
    print("\n".join(satir))
    print(f"→ {hedef}/bolum.md · bolum.tsv · NN_ilk.png · NN_orta.png")
    return 0 if kes else 1


def main():
    ap = argparse.ArgumentParser(description="medya alımı ve gerçek durum (16.10.2026)")
    alt = ap.add_subparsers(dest="komut", required=True)
    for ad, f in (("durum", durum), ("al", al)):
        p = alt.add_parser(ad)
        p.add_argument("klasor")
        p.add_argument("--yaz", action="store_true")
        p.add_argument("--medya")
        p.set_defaults(f=f)
    p = alt.add_parser("bol")
    p.add_argument("montaj")
    p.add_argument("klasor")
    p.add_argument("--esik", type=float, default=0.3)
    p.add_argument("--medya")
    p.set_defaults(f=bol)
    a = ap.parse_args()
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
