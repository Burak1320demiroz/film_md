#!/usr/bin/env python3
"""
QA SAĞLIK — rubrik çıktılarının sağlığı, mercek başına, betikten [14.09.2026 · QA çıktı reformu FAZ 0]

NEDEN VAR: 13 rubriğin ürettiği 336 gerçek mercek raporunun %8'i GO çıktı (14.09.2026
ölçümü); geri kalanı deponun kendi çıkış kapısından geçemedi. "Rubrik yeterli mi"
sorusunun cevabı rubriğin metninde değil, rubriğin ÜRETTİĞİ raporların sayısındadır ve
o sayı bugüne kadar hiçbir yerde basılmıyordu. Bu betik onu basar; dosya yazmaz.

NE SAYAR (mercek başına, 02_HAM_RAPORLAR/*/*_HAM.md):
  n · mod D payı · rapor_kontrol kararı (GO / ŞARTLI / TEKRAR / GEÇERSİZ / ✂️ KESİK) ·
  tally = yazılı etiket (tally satırı olanlarda) · VERDICT satırı var (FAZ 1: sözlükte) ·
  rapor boyutu medyanı · 'no in-scope source' hücre payı
Karar, rapor_kontrol.main ile AYNI yoldan üretilir: SPEC film klasöründen, ⑤ çapraz kapı
parti başına (KESİK dışarıda), plan sahne sayısı [D188].

KULLANIM:
  python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --ozet      # sayac için, 15 satır
  python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --tam       # + sebepler + film listesi
  python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --film THE_HARD_DOCK

TABAN ÇİZGİSİ: 14.09.2026 kesiti CALISTIRMA_KAYITLARI.md'de. Diyet/sözleşme değişikliğinin
etkisi bu betiğin sonraki koşularıyla ölçülür — sayı belgeye elle yazılmaz.
"""
import re, sys, statistics, collections, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rapor_kontrol as rk

KOK = Path(__file__).resolve().parent.parent
HAM = KOK / "FILM_QA_RAPORLARI" / "02_HAM_RAPORLAR"
FORMATLAR = ("dikey_shorts_filmler", "yatay_2_dk_filmler", "yatay_4_dk_filmler",
             "yatay_8_dk_filmler", "yatay_16_dk_filmler",
             "yatay_32_dk_filmler", "yatay_64_dk_filmler")
ARSIV_ALET = re.compile(r"_(TEKNIK|MANTIK|KARAKTER|SENARYO|SHORTS)_HAM\.md$", re.I)
VERDICT = re.compile(r"^[ \t>*]*VERDICT\s*[:：]", re.M | re.I)
MERCEK_SIRA = ["① KARE", "② DEVAMLILIK", "③ SES", "④ HİKAYE", "⑤ ARKA PLAN", "⑥ FİZİK",
               "⑦ AKSİYON", "⑧ EFOR", "⑨ KADRAJ", "⑩ OYUNCULUK", "⑪ IŞIK", "⑫ HOOK", "⑬ UYUM",
               "⑭ HAREKET", "⑮ YÖN"]


def film_klasoru(ad):
    for f in FORMATLAR:
        d = KOK.parent / f / ad
        if d.is_dir():
            return d
    for arsiv_f in ("yatay_10_dk_filmler", "yatay_6_dk_filmler"):
        arsiv_d = KOK / "ARSIV" / arsiv_f / ad
        if arsiv_d.is_dir():
            return arsiv_d
    return None


def film_tara(klasor):
    """Bir filmin ham klasörü → rapor_kontrol kararları (main ile aynı yol)."""
    hams = [h for h in sorted(klasor.glob("**/*_HAM.md")) if not ARSIV_ALET.search(h.name)]
    if not hams:
        return []
    film_dir = film_klasoru(klasor.name)
    spec = None
    if film_dir:
        specs = sorted(film_dir.glob("*_QA_SPEC.md"))
        if specs:
            spec = specs[0].read_text(encoding="utf-8", errors="replace")
    sonuclar = []
    for h in hams:
        ilk = h.read_text(encoding="utf-8", errors="replace")
        faz = rk.faz_mi(film_dir, rk.govde_al(ilk)) if film_dir else None
        r = rk.rapor_denetle(h, spec, 10.0, 10.0, faz, None)
        r["spec_var"] = spec is not None
        r["boyut"] = len(ilk)
        r["verdict_var"] = bool(VERDICT.search(rk.govde_al(ilk)))
        sozluk = getattr(rk, "VERDICT_SOZLUK", None)
        r["verdict_sozlukte"] = rk.verdict_sozlukte(rk.govde_al(ilk), r["mercek"]) if sozluk else None
        sonuclar.append(r)
    tam = [r for r in sonuclar if r["karar"] != "KESİK"]
    if len(tam) >= 2:
        plan_sahne, plan_kaynak = rk.plan_sahne_sayisi(film_dir, None) if film_dir else (None, None)
        cb = rk.capraz(tam, None, plan_sahne, plan_kaynak)
        if any(b.seviye == "GEÇERSİZ" for b in cb):
            for r in tam:
                r["karar_tekil"] = r["karar"]
                r["karar"] = "GEÇERSİZ"
                r["parti"] = True
    return sonuclar


def tara(film=None):
    t0 = time.time()
    hepsi = []
    for d in sorted(HAM.iterdir()):
        if not d.is_dir() or (film and d.name != film):
            continue
        for r in film_tara(d):
            r["film"] = d.name
            hepsi.append(r)
    return hepsi, time.time() - t0


def yuzde(a, b):
    return f"{100 * a // b:3d}%" if b else "  —"


def ozet(hepsi, sure, tam=False):
    mercekli = [r for r in hepsi if r["mercek"] in MERCEK_SIRA]
    disi = len(hepsi) - len(mercekli)
    kar = collections.Counter(r["karar"] for r in mercekli)
    tekil = collections.Counter(r.get("karar_tekil", r["karar"]) for r in mercekli)
    filmler = {r["film"] for r in mercekli}
    parti_dusen = {r["film"] for r in mercekli if r.get("parti")}
    print(f"   {len(mercekli)} mercek raporu · {len(filmler)} film · {disi} mercek dışı dosya (faz/kapak/kapı) · "
          f"tarama {sure:.0f} s")
    print(f"   tekil karar : ✅ GO {tekil['GO']} ({yuzde(tekil['GO'], len(mercekli)).strip()}) · ⚠️ ŞARTLI {tekil['ŞARTLI']} · "
          f"⛔ TEKRAR {tekil['TEKRAR']} · 🚨 GEÇERSİZ {tekil['GEÇERSİZ']} · ✂️ KESİK {tekil['KESİK']}")
    print(f"   ⑤ çapraz sonrası (tabloya giren): ✅ GO {kar['GO']} · ⚠️ ŞARTLI {kar['ŞARTLI']} · 🚨 GEÇERSİZ {kar['GEÇERSİZ']} "
          f"— parti düşen film {len(parti_dusen)} / {len(filmler)} [D107 · D121]")
    go_film = {r["film"] for r in mercekli if r["karar"] == "GO"}
    print(f"   en az bir GO raporu olan film {len(go_film)} / {len(filmler)}")
    print("   ── mercek ──            n   modD    GO  ŞART  TEKR  GEÇ  KESİK  tally=etk  VERDICT  boyut  kaynaksız")
    for m in MERCEK_SIRA:
        rr = [r for r in mercekli if r["mercek"] == m]
        if not rr:
            print(f"   {m:14s}         0   —      koşulmamış")
            continue
        k = collections.Counter(r["karar"] for r in rr)
        modd = sum(1 for r in rr if r["mod"] == "D")
        tallyli = [r for r in rr if r["karar"] != "KESİK" and r.get("tally")]
        tally_ok = sum(1 for r in tallyli if tuple(r["tally"]) == (r["yazili"]["🔴"], r["yazili"]["🟠"], r["yazili"]["🟡"]))
        canli = [r for r in rr if r["karar"] != "KESİK"]
        if canli and canli[0].get("verdict_sozlukte") is not None:
            v_ok = sum(1 for r in canli if r["verdict_sozlukte"])
            v_et = "sözlük"
        else:
            v_ok = sum(1 for r in canli if r["verdict_var"])
            v_et = "satır"
        boy = statistics.median(r["boyut"] for r in rr) / 1000
        hucre = [c for r in canli for c in r.get("rows", [])]
        kayn = sum(1 for c in hucre if rk.KAYNAKSIZ.search(c.get("issue") or ""))
        print(f"   {m:14s} {len(rr):5d}  {yuzde(modd, len(rr))}  {k['GO']:4d}  {k['ŞARTLI']:4d}  {k['TEKRAR']:4d}  "
              f"{k['GEÇERSİZ']:3d}  {k['KESİK']:5d}   {yuzde(tally_ok, len(tallyli))}      {yuzde(v_ok, len(canli))} {v_et:6s} "
              f"{boy:4.1f}KB  {yuzde(kayn, len(hucre))}")
    if tam:
        sebep = collections.Counter()
        for r in mercekli:
            for b in r["bulgular"]:
                if b.seviye in ("GEÇERSİZ", "TEKRAR", "ŞARTLI", "KESİK"):
                    sebep[(b.seviye, re.sub(r"\d+([.,]\d+)?", "n", b.baslik)[:60])] += 1
        print("   ── en sık sebepler ──")
        for (sv, bs), n in sebep.most_common(20):
            print(f"      {n:3d}  [{sv}] {bs}")
        print("   ── film başına (GO / toplam) ──")
        pf = collections.defaultdict(lambda: [0, 0])
        for r in mercekli:
            pf[r["film"]][1] += 1
            pf[r["film"]][0] += r["karar"] == "GO"
        for f, (g, t) in sorted(pf.items(), key=lambda x: (-x[1][0], x[0])):
            print(f"      {f:28s} {g:2d} / {t:2d}")


def main():
    args = sys.argv[1:]
    film = args[args.index("--film") + 1] if "--film" in args else None
    hepsi, sure = tara(film)
    if film:
        for r in hepsi:
            print(f"   {r['karar']:9s} {r['mercek']:14s} {r['yol'].name}")
    ozet(hepsi, sure, tam="--tam" in args)


if __name__ == "__main__":
    main()
