#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KAPI ADRESİ ÇÖZÜCÜ — sayac.sh 🧭 bloğunun alt ölçümü.   [05.09.2026]

NEDEN VAR: kontrat "kapısı olmayan ders, ders değildir" diyor ve sayaç KAPI
satırını SAYIYOR — ama kapının işaret ettiği betik jetonu / liste maddesi
hiçbir yerde ARANMIYOR. Ölçüm (05.09.2026): D179'un kapısı
`prompt_kontrol.py ⑳b DEĞİŞİM KAPISI` diye yazılı, betikte ⑳b geçiş sayısı 0.
Ders "kapılı" sayılıyor, kapı yok.

    Depo kapıyı SAYIYOR, ÇÖZMÜYOR.

Bu betik her KAPI satırının adresini fiilen açar:
  BETİK · `<dosya>` <JETON>   → dosya var mı + jeton o dosyada birebir geçiyor mu
  LİSTE · `<dosya>` <madde>   → dosya var mı + madde o dosyada geçiyor mi
  KARAR / ARŞİV               → çözülecek adres yok, ÇÖZÜM ARANMAZ
  ⬜ AÇIK                     → ders kapısının olmadığını kendi söylüyor

⛔ Bu betik DÜZELTMEZ, yalnız ölçer (kontrat §5: geriye dönük tasnif yok).
"""
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
D = KOK / "kilavuzlar_ve_sistem_dosyalari" / "DERSLER"

# jeton adayları: daireli sayı (⑳b · ①.5 gibi ekleriyle) · --bayrak · BÜYÜK HARFLİ ad
DAIRELI = r"[①-⑳㉑-㉟⓪]"
JETON = re.compile(
    rf"({DAIRELI}[a-z]?(?:\.\d+)?)"                     # ⑭ · ⑳b · ①.5
    r"|(--[a-zçğıöşü-]+)"                               # --olcum-filigran
    r"|\b([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ0-9/]{2,}(?:\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ0-9/]{1,})*)\b"  # KÖŞE TESTİ
)
# jeton sayılmayacak büyük harfli gürültü
YOKSAY = {"KAPI", "BETİK", "LİSTE", "KARAR", "ARŞİV", "AÇIK", "SPEC", "QA", "MOD",
          "TEK", "VAR", "YOK", "DEĞİL", "AYNEN", "EN", "VE", "İKİ", "YENİ", "TAM",
          "PUAN", "GEÇİŞ", "NOT", "DUR", "OK", "PDF", "MD", "PY", "SH"}


def _dosyalar(satir):
    return [m for m in re.findall(r"`([^`]+)`", satir)]


UZANTI = (".py", ".sh", ".md", ".json", ".txt")


def _yol_coz(ad):
    """Backtick içindeki adı depoda gerçek bir dosyaya çöz.

    ⛔ Yalnız DOSYA GİBİ GÖRÜNEN dizge denenir. Backtick regex de (`\\bsuit\\b`),
    bayrak da (`--olcum-filigran`), çıktı dosyası da (`son_kare.jpg`), jeton da
    (`NOVUM`) taşıyabiliyor; hepsini "hedef dosya" saymak 14 hayaletin 9'unu
    UYDURMUŞTU (05.09.2026 ilk koşusu).
    """
    parcalar = ad.strip().split()
    if not parcalar:
        return None
    ad = parcalar[0].strip("`'\"").rstrip(",;:")
    if not ad or ad.endswith("/") or "\\" in ad or ad.startswith("--"):
        return None
    if not ad.endswith(UZANTI):
        # skill adı olabilir: `yeni-film` → .claude/skills/yeni-film/SKILL.md
        sk = KOK / ".claude" / "skills" / ad / "SKILL.md"
        return sk if sk.is_file() else None
    aday = [KOK / ad, KOK / "kilavuzlar_ve_sistem_dosyalari" / ad,
            KOK / "kilavuzlar_ve_sistem_dosyalari" / "URETIM_ONCESI_ANALIZ" / ad,
            KOK / ".claude" / "skills" / ad]
    for p in aday:
        if p.is_file():
            return p
    ad2 = pathlib.PurePath(ad).name
    if "." in ad2:
        for p in KOK.rglob(ad2):
            if ".git" not in p.parts:
                return p
    return None


def _jeton_bul(satir, dosya_adlari):
    kuyruk = satir
    for a in dosya_adlari:
        kuyruk = kuyruk.replace(f"`{a}`", " ")
    for m in JETON.finditer(kuyruk):
        j = (m.group(1) or m.group(2) or m.group(3) or "").strip()
        if not j or j in YOKSAY:
            continue
        if m.group(3) and all(w in YOKSAY for w in j.split()):
            continue
        return j
    return None


def coz(satir):
    """→ (durum, ayrıntı).  durum: ÇÖZÜLDÜ · HAYALET · ADRESSİZ · AÇIK · KARAR"""
    g = satir.split("**KAPI:**", 1)[1].strip() if "**KAPI:**" in satir else satir
    if "⬜ AÇIK" in g:
        return "AÇIK", "ders kapısının olmadığını kendi söylüyor"
    kader = g.split("·")[0].strip().split()[0] if g.split() else ""
    if kader.startswith(("KARAR", "ARŞİV")):
        return "KARAR", f"{kader} — çözülecek makine adresi yok"

    ham = _dosyalar(g)
    hedefler, ic_jeton = [], []
    for a in ham:
        p = _yol_coz(a)
        if p:
            hedefler.append((a, p))
            # `prompt_kontrol.py ⑯ POLİTİKA SÖZLÜĞÜ` → kuyruk da jetondur
            kuyruk = a.strip()[len(a.strip().split()[0]):].strip()
            if kuyruk:
                ic_jeton.append(kuyruk)
        else:
            ic_jeton.append(a.strip())          # dosya değil → jeton adayı
    if not hedefler:
        return "ADRESSİZ", "KAPI satırında çözülebilir hedef dosya yok"

    jeton = _jeton_bul(g, ham)
    adaylar = [j for j in ([jeton] + ic_jeton) if j]
    if not adaylar:
        # kapı bütün betiği işaret ediyor olabilir (D125: "koşu sırasının EN BAŞI")
        return "DOSYA", f"{hedefler[0][0]} var; alt jeton iddia edilmemiş"

    metinler = []
    for a, p in hedefler:
        try:
            metinler.append((a, p.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            pass
    for j in adaylar:
        for varyant in _varyant(j):
            for a, t in metinler:
                if varyant in t:
                    return "ÇÖZÜLDÜ", f"{varyant} → {a}"
    # daireli kapı numarası (⑭ · ⑳b) ve bayrak KISA ama AYIRT EDİCİDİR —
    # "dosya düzeyi"ne düşürülmez, aksi hâlde D179'un ⑳b hayaleti görünmez olur.
    def zayif(j):
        return (len(j.split()) == 1 and len(j) < 5
                and not re.match(DAIRELI, j) and not j.startswith("--"))
    if all(zayif(j) for j in adaylar):
        return "DOSYA", f"{hedefler[0][0]} var; jeton ayırt edici değil ({adaylar[0]})"
    return "HAYALET", f"{adaylar[0]!r} hiçbir hedefte yok ({', '.join(a for a, _ in hedefler)})"


# tek başına ADRES olamayacak jenerik kelimeler — bunlar eşleşirse kapı çözülmüş
# SAYILMAZ. (05.09.2026: gevşek eşleme 'KAPISI' kelimesini bulup D175 ve D176'yı
# "çözüldü" saydı; oysa ikisinin de kapısı betikte YOK. Gevşek çözücü, çözmediğini
# çözdü sanan bir kapıdır — düzeltmeye çalıştığımız arızanın ta kendisi.)
JENERIK = {"KAPI", "KAPISI", "KAPISINA", "MERCEK", "ÜRETİM", "TEST", "TESTİ",
           "SATIR", "SATIRI", "BLOK", "BLOĞU", "KANAL", "KANALI", "YÜZEY",
           "SIRA", "SIRASI", "DEĞİŞİM", "SES", "VAR", "YOK", "MOD", "LİSTE"}
# ad sonundaki jenerik kuyruk atılıp ayırt edici baş denenebilir: MÜHÜR KAPISI → MÜHÜR
KUYRUK_EK = ("KAPISI", "TESTİ", "SATIRI", "BLOĞU", "KANALI", "KAPI")


def _varyant(j):
    """Jetonun aranabilir hâlleri — YALNIZ ayırt edici olanlar.

    ⛔ Tek jenerik kelimeye düşen eşleme YOK. Bir kapı ancak kendi ADIYLA
    bulunursa çözülmüş sayılır; 'KAPISI' kelimesini bulmak kapıyı bulmak değildir.
    """
    def ayirt(x):
        x = x.strip()
        return bool(x) and x.upper() not in JENERIK

    if ayirt(j):
        yield j
    for ek in KUYRUK_EK:                      # MÜHÜR KAPISI → MÜHÜR
        if j.upper().endswith(" " + ek):
            bas = j[: -(len(ek) + 1)].strip()
            if ayirt(bas):
                yield bas
    if "/" in j:                              # KUYRUK/BAŞ KART ŞÜPHESİ → KUYRUK
        for parca in j.split("/"):
            if len(parca.strip()) >= 4 and ayirt(parca):
                yield parca.strip()
    if j.startswith("--"):
        yield j.split()[0]                    # `--olcum-filigran VAR|YOK` → --olcum-filigran
        yield j.lstrip("-").split()[0]


def tara():
    kayit = []
    for f in sorted(D.glob("0[1-9]_*.md")):
        ders = "?"
        for satir in f.read_text(encoding="utf-8", errors="replace").split("\n"):
            m = re.match(r"^##\s.{0,4}\s*DERS\s+(\d+)\s*:", satir)
            if m:
                ders = m.group(1)
            elif satir.startswith("**KAPI:**"):
                # ⛔ YALNIZ TEK SATIR okunur. Devam satırlarını birleştirmek denendi
                # (05.09.2026) ve ÖLÇÜMÜ BOZDU: gövde metni jetonlarla eşleşip
                # doğrulanmış beş hayaleti "çözüldü" gösterdi, ⬜ AÇIK 2'den 7'ye çıktı.
                # Bilinen bedel: KAPI satırı saran ders (D124) HAYALET görünür.
                durum, ayrinti = coz(satir)
                kayit.append((int(ders) if ders.isdigit() else 0, f.name, durum, ayrinti))
    return kayit


if __name__ == "__main__":
    k = tara()
    say = {}
    for _, _, d, _ in k:
        say[d] = say.get(d, 0) + 1
    if "--tam" in sys.argv:
        for n, f, d, a in sorted(k):
            print(f"   D{n:<4} {d:<9} {a[:88]}")
        print()
    coz_n = say.get("ÇÖZÜLDÜ", 0) + say.get("DOSYA", 0)
    hay = say.get("HAYALET", 0) + say.get("ADRESSİZ", 0)
    print(f"   adresi ÇÖZÜLEN kapı           {coz_n} / {len(k)}")
    print(f"   ⛔ HAYALET / ADRESSİZ kapı     {hay}"
          + ("   ← kapı yazılı, adres yok: ders kapılı SAYILMAZ" if hay else ""))
    for n, f, d, a in sorted(k):
        if d in ("HAYALET", "ADRESSİZ"):
            print(f"      D{n} · {d} · {a[:78]}")
    if say.get("AÇIK"):
        print(f"   ⬜ AÇIK (kapı arayan ders)     {say['AÇIK']}")
    if say.get("DOSYA"):
        print(f"   · bunun {say['DOSYA']}'i DOSYA düzeyi (alt jeton iddia edilmemiş)")
    if say.get("KARAR"):
        print(f"   KARAR/ARŞİV (adres aranmaz)   {say['KARAR']}")
