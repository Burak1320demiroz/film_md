#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  OKUMA ÇİZELGESİ — "tüm dersleri ve tüm kılavuzları oku" cümlesini
#  SAYILABİLİR bir deftere çevirir
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR (08.09.2026 · sahip kararı):
#  "Okuma listeni çıkar ve o listedeki kılavuzları gerçekten aç" cümlesi
#  davranış değiştirmedi. THE OPEN CIRCUIT'in 07.09.2026 tam denetimi bunu
#  ölçtü: zorunlu okuma listesinin DÖRDÜ hiç açılmamıştı (UZAY_USSU ·
#  SAHNE_ZINCIRI · ACILIS_KAPANIS · ASTRONOT_DONANIM) ve sekiz bulgunun
#  hepsi o dört dosyadan çıktı — biri filmin üssünü kadraja fiziksel olarak
#  alamayan bir lens seçimiydi. Cümle değil, DEFTER kapatır.
#
#  Elle tutulan liste bayatlar (kural ①: sayı elle yazılmaz) — bu yüzden
#  çizelge dosya sisteminden ÜRETİLİR. Yeni bir kılavuz eklendiğinde bir
#  sonraki filmin çizelgesinde kendiliğinden ⬜ olarak belirir.
#
#  KULLANIM:
#      bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü> [--force]
#  ÇIKTI:
#      <film klasörü>/00_ANALIZ/00_OKUMA_CIZELGESI.md
#
#  ⛔ İşaretlenmiş çizelgenin üstüne yazmaz; ilerlemeyi ezmek için --force.
# ═══════════════════════════════════════════════════════════════════
set -u

F="${1:-}"; ZORLA="${2:-}"
[ -z "$F" ] && { echo "KULLANIM: okuma_cizelgesi.sh <film klasörü> [--force]"; exit 2; }
[ -d "$F" ] || { echo "⛔ klasör yok: $F"; exit 2; }
F="$(cd "${F%/}" && pwd)"
FILM="$(basename "$F")"
cd "$(dirname "$0")/.." || exit 1
K="kilavuzlar_ve_sistem_dosyalari"
Q="$K/FILM_QA_RAPORLARI"
OUT="$F/00_ANALIZ/00_OKUMA_CIZELGESI.md"

mkdir -p "$F/00_ANALIZ"
if [ -f "$OUT" ] && grep -q "✅" "$OUT" && [ "$ZORLA" != "--force" ]; then
  echo "⛔ $OUT işaretli satır taşıyor — ezilmedi."
  echo "   İlerlemeyi sıfırlamak istiyorsan: --force"
  exit 2
fi

TOPLAM_D=0; TOPLAM_S=0

satir() {   # satir <dosya> <kök-göreli-etiket>
  local f="$1" ad="$2" n
  [ -f "$f" ] || return 0
  n=$(wc -l < "$f" | tr -d ' ')
  TOPLAM_D=$((TOPLAM_D + 1)); TOPLAM_S=$((TOPLAM_S + n))
  printf '| ⬜ | `%s` | %s |  |\n' "$ad" "$n" >> "$OUT"
}

baslik() { printf '\n### %s\n\n| ⬜/✅ | dosya | satır | bu filme düşen kilit |\n|:--:|---|--:|---|\n' "$1" >> "$OUT"; }

{
printf '# 📖 %s — OKUMA ÇİZELGESİ\n\n' "$FILM"
printf '> Üretildi: `bash %s/okuma_cizelgesi.sh <film klasörü>` · %s\n' "$K" "$(date '+%d.%m.%Y %H:%M')"
printf '> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.\n'
printf '>\n'
printf '> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna\n'
printf '> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş\n'
printf '> bırakılmaz — boş hücre "okudum" ile "atladım" arasını ayırt ettirmez.\n'
printf '>\n'
printf '> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.\n'
printf '> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.\n'
} > "$OUT"

baslik "TUR 1 · DERSLER — hepsi (film dersleri 01-07 · alet dersleri 08-09 · gözlem)"
for f in "$K"/DERSLER/*.md; do satir "$f" "${f#$K/}"; done

baslik "TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk"
for f in "$K"/URETIM_ONCESI_ANALIZ/*.md; do satir "$f" "${f#$K/}"; done

baslik "TUR 3 · KILAVUZLAR — hepsi"
for f in "$K"/*.md; do satir "$f" "${f#$K/}"; done
for f in "$K"/DIS_FILM_ANALIZI/*.md; do satir "$f" "${f#$K/}"; done

baslik "TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı"
satir "$Q/00_INDEX.md"               "FILM_QA_RAPORLARI/00_INDEX.md"
satir "$Q/09_URETIM_RED_DEFTERI.md"  "FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md"
for f in "$Q"/0[3-8]_*.md; do satir "$f" "FILM_QA_RAPORLARI/$(basename "$f")"; done
for f in "$Q"/T*.md;        do satir "$f" "FILM_QA_RAPORLARI/$(basename "$f")"; done

RAPOR_N=$(ls -1 "$Q/01_FILM_RAPORLARI"/*.md 2>/dev/null | wc -l | tr -d ' ')
RAPOR_S=$(cat "$Q/01_FILM_RAPORLARI"/*.md 2>/dev/null | wc -l | tr -d ' ')
{
printf '\n### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (%s dosya · %s satır)\n\n' "$RAPOR_N" "$RAPOR_S"
printf '> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun\n'
printf '> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER\n'
printf '> filmlerde tekrar eder. En az **beş** kayıt açılır:\n'
printf '> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film\n'
printf '> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt\n'
printf '> ⑤ bu filmin konseptine en yakın kayıt.\n\n'
printf '| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |\n|:--:|---|---|---|\n'
printf '| ⬜ |  | ① aynı format |  |\n'
printf '| ⬜ |  | ② aynı ortam kartı |  |\n'
printf '| ⬜ |  | ③ aynı tema |  |\n'
printf '| ⬜ |  | ④ en düşük skor |  |\n'
printf '| ⬜ |  | ⑤ en yakın konsept |  |\n'
printf '\nTam liste: `ls %s/01_FILM_RAPORLARI/`\n' "$Q"
} >> "$OUT"

{
printf '\n---\n\n## 📊 ÇİZELGE ÖZETİ\n\n```\n'
printf 'ZORUNLU DOSYA:   %s\n' "$TOPLAM_D"
printf 'ZORUNLU SATIR:   %s\n' "$TOPLAM_S"
printf 'SEÇMELİ KAYIT:   5 / %s  (TUR 5)\n' "$RAPOR_N"
printf '```\n\n'
printf '⚠️ **Bu bir oturumluk iş değildir ve olmaması normaldir.** Okuma\n'
printf 'yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan\n'
printf 'devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.\n'
} >> "$OUT"

echo "✅ ÇİZELGE: $OUT"
echo "   $TOPLAM_D zorunlu dosya · $TOPLAM_S satır · + 5 seçmeli film kaydı ($RAPOR_N içinden)"
