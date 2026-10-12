"""analiz/<FILM>.md BULGULAR tablolarını birleştirir: hüküm · tür · kapanma (12 film)."""
import re, collections
from pathlib import Path

D = Path(__file__).parent
FILMLER = ["THE_LAST_GATE", "THE_STOLEN_SKY", "THE_LAST_TOW", "THE_SLOW_RAIN", "GUNES_MEZARI", "THE_STILL_POINT",
           "THE_INWARD_FALL", "THE_BRITTLE_EDGE", "THE_STATIC_VEIL", "THE_LISTENING_WORLD", "THE_COUNTED_RIVET",
           "THE_SIGNAL_KEEPERS"]
HUK = {"🅑+": "🅑+", "🅐": "🅐", "🅑": "🅑", "🅒": "🅒", "🅓": "🅓"}

def hukum(h):
    h = h.strip()
    for k in ("🅑+", "🅐", "🅑", "🅒", "🅓"):
        if h.startswith(k):
            return k
    return None

hepsi = []
for f in FILMLER:
    p = D / f"{f}.md"
    if not p.exists():
        print("YOK", f); continue
    t = p.read_text(encoding="utf-8")
    m = re.search(r"## BULGULAR(.*?)\n## ", t, re.S)
    for s in m.group(1).splitlines():
        if not s.startswith("|") or re.match(r"^\|\s*-", s) or s.startswith("| S |"):
            continue
        c = [x.strip() for x in s.strip().strip("|").split("|")]
        if len(c) < 7:
            continue
        h = hukum(c[4])
        if not h:
            continue
        sid = "🔴" if "🔴" in c[1] else ("🟠" if "🟠" in c[1] else "—")
        hepsi.append(dict(film=f, sid=sid, mercek=c[2], tur=c[3].lower(), huk=h, prompt=c[5], kap=c[6].lower(), not_=c[7] if len(c) > 7 else ""))

C = collections.Counter
print(f"satır {len(hepsi)} · 🔴 {sum(x['sid']=='🔴' for x in hepsi)} · 🟠 {sum(x['sid']=='🟠' for x in hepsi)}")
print("\n── film × hüküm ──")
for f in FILMLER:
    x = [r for r in hepsi if r["film"] == f]
    c = C(r["huk"] for r in x)
    pay = (c["🅑"] + c["🅑+"]) / max(1, c["🅐"] + c["🅑"] + c["🅑+"])
    print(f"{f:22s} n{len(x):4d}  🅐{c['🅐']:3d} 🅑{c['🅑']:3d} 🅑+{c['🅑+']:3d} 🅒{c['🅒']:3d} 🅓{c['🅓']:3d}  prompt payı %{100*pay:.0f}  QA payı %{100*c['🅒']/max(1,len(x)):.0f}")
c = C(r["huk"] for r in hepsi)
print(f"{'TOPLAM':22s} n{len(hepsi):4d}  🅐{c['🅐']:3d} 🅑{c['🅑']:3d} 🅑+{c['🅑+']:3d} 🅒{c['🅒']:3d} 🅓{c['🅓']:3d}  prompt payı %{100*(c['🅑']+c['🅑+'])/(c['🅐']+c['🅑']+c['🅑+']):.0f}  QA payı %{100*c['🅒']/len(hepsi):.0f}")
print("\n── tür (toplam · 🔴 · 🅐 / 🅑 / 🅑+ / 🅒 · film) ──")
def norm(t):
    t = t.replace("kask/giysi/ekipman kayması", "kask/giysi/ekipman").replace("arka plan/dünya çapası", "arka plan/dünya")
    return t.split("(")[0].strip()
for t, n in C(norm(r["tur"]) for r in hepsi).most_common(22):
    x = [r for r in hepsi if norm(r["tur"]) == t]
    h = C(r["huk"] for r in x)
    print(f"{n:4d} 🔴{sum(r['sid']=='🔴' for r in x):3d}  🅐{h['🅐']:3d} 🅑{h['🅑']:3d} 🅑+{h['🅑+']:3d} 🅒{h['🅒']:3d}  film{len({r['film'] for r in x}):3d}  {t}")
print("\n── kapanma ──")
for k, n in C(r["kap"].split("(")[0].strip() for r in hepsi).most_common(10):
    print(f"{n:4d}  {k}")
print("\n── 🔴 kapanma ──")
for k, n in C(r["kap"].split("(")[0].strip() for r in hepsi if r["sid"] == "🔴").most_common(8):
    print(f"{n:4d}  {k}")
