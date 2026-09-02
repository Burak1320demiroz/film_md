#!/bin/bash
# PROB ÖLÇÜM — 05_DIKEY_HAT_TESHISI §9.2'nin iki probunu MAKİNEYLE okur.
# Kullanım:  prob_olcum.sh A|B <klip.mp4>
# Çıktıdaki sayılar hükmün tek kaynağıdır [D125]: model bu sayıları SÖYLEMEZ.
# İnsan gözüne kalan maddeler ⬜ ile işaretlidir ve kare dosyası üretilir.
set -u
P="${1:-}"; M="${2:-}"
[ -z "$P" ] || [ -z "$M" ] && { echo "KULLANIM: prob_olcum.sh A|B <klip.mp4>"; exit 2; }
[ -f "$M" ] || { echo "HATA: dosya yok: $M"; exit 2; }
command -v ffprobe >/dev/null || { echo "HATA: ffprobe yok"; exit 3; }
OUT="${OUT_DIR:-$(dirname "$M")}"
B=$(basename "${M%.*}")

echo "═══════════════════════════════════════════════════════"
echo "  PROB $P · $M"
echo "═══════════════════════════════════════════════════════"

echo "── ① KÜNYE"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M")
WH=$(ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=x "$M")
FPS=$(ffprobe -v error -select_streams v -show_entries stream=r_frame_rate -of csv=p=0 "$M")
AUD=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M")
W=${WH%x*}; H=${WH#*x}
printf "   süre        %s s\n" "$DUR"
printf "   çözünürlük  %s" "$WH"
if [ "$W" -lt "$H" ]; then echo "  (DİKEY ✅)"; else echo "  (YATAY ⚠️ prob dikey istiyordu)"; fi
printf "   kare hızı   %s\n" "$FPS"
printf "   ses kanalı  %s\n" "${AUD:-YOK}"

echo "── ② KESME KAPISI [D1] — model kendi kesmesini uydurdu mu?"
CUTS=$(ffmpeg -hide_banner -nostats -i "$M" -filter:v "select='gt(scene,0.30)',showinfo" -f null - 2>&1 \
  | grep -oE "pts_time:[0-9.]+" | cut -d: -f2)
N=$(echo "$CUTS" | grep -c . )
[ -z "$CUTS" ] && N=0
if [ "$N" -eq 0 ]; then
  echo "   0 kesme  ✅ tek çekim korundu"
else
  echo "   $N kesme  🔴 D1 TETİKLENDİ — saniyeler:"; echo "$CUTS" | sed 's/^/      /'
fi

if [ "$P" = "A" ]; then
  echo "── ③ İKİ FİGÜR KAPISI ⬜ (makine sayamaz — CV kütüphanesi yok)"
  ffmpeg -hide_banner -loglevel error -y -i "$M" \
    -vf "fps=1/2,scale=360:-1,tile=5x1" -frames:v 1 "$OUT/${B}_PROBA_kareler.png" 2>/dev/null \
    && echo "   BAKILACAK: $OUT/${B}_PROBA_kareler.png  (0·2·4·6·8. saniye yan yana)"
  ffmpeg -hide_banner -loglevel error -y -ss 4 -i "$M" -frames:v 1 "$OUT/${B}_PROBA_takas.png" 2>/dev/null \
    && echo "   BAKILACAK: $OUT/${B}_PROBA_takas.png     (4. saniye — nesnenin el değiştirdiği an)"
  cat <<'EOF'
   ⬜ iki figür AYNI yüze mi sahip?          EVET → D20 HÂLÂ DOĞRU
   ⬜ üçüncü bir figür belirdi mi?           EVET → D20 HÂLÂ DOĞRU
   ⬜ boy/duruş farkı korunuyor mu?          HAYIR → kısmi klon
   ⬜ el teması eriyor / faz geçiyor mu?     EVET → ayrı bulgu [D24]
EOF
fi

if [ "$P" = "B" ]; then
  echo "── ③ SES KAPISI"
  if [ -z "$AUD" ]; then
    echo "   🔴 SES KANALI YOK — replik hiç üretilmemiş. PROB B DÜŞTÜ."
  else
    ffmpeg -hide_banner -nostats -i "$M" -af ebur128=peak=true -f null - 2>&1 \
      | grep -E "^\s+(I:|Peak:)" | sed 's/^/   /'
    echo "   konuşma penceresi (silencedetect −40dB / 0,20 s):"
    ffmpeg -hide_banner -nostats -i "$M" -af "silencedetect=noise=-40dB:d=0.20" -f null - 2>&1 \
      | grep -oE "silence_(start|end): [0-9.]+" | sed 's/^/      /' || echo "      (aralık yok — ses sürekli)"
  fi
  echo "── ④ AĞIZ HAREKETİ ↔ SES EŞLEŞMESİ (kare kare YDIF · ağız bölgesi)"
  echo "   kırpma: kadrajın orta-alt üçte biri (MOUTH_CROP ile değiştirilebilir)"
  CROP="${MOUTH_CROP:-iw/3:ih/6:iw/3:ih/2}"
  ffmpeg -hide_banner -nostats -i "$M" \
    -vf "crop=${CROP},signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 \
    | awk '/pts_time/{t=$0; sub(/.*pts_time:/,"",t); sub(/ .*/,"",t)}
           /YDIF=/{v=$0; sub(/.*YDIF=/,"",v); printf "      %6.2f s   YDIF %s\n", t, v}' \
    | awk 'NR%3==1' | head -40
  cat <<'EOF'
   OKUMA: YDIF, ağız bölgesinin bir önceki kareye göre değişimidir.
     · konuşma penceresi DIŞINDA YDIF yüksek  → ağız replik bitince
       oynamaya devam ediyor  🔴 D35 HÂLÂ DOĞRU
     · konuşma penceresi İÇİNDE YDIF düz      → ses var, ağız yok  🔴
     · YDIF tepesi konuşma penceresiyle örtüşüyor → ✅ D35 gevşetilebilir
   ⬜ İNSAN GÖZÜ: 3,0-4,5 s bandı — ağız replikten ÖNCE ve SONRA kapalı mı?
EOF
  ffmpeg -hide_banner -loglevel error -y -ss 2.8 -i "$M" -t 1.8 \
    -vf "fps=8,scale=240:-1,tile=5x3" -frames:v 1 "$OUT/${B}_PROBB_agiz.png" 2>/dev/null \
    && echo "   BAKILACAK: $OUT/${B}_PROBB_agiz.png  (2,8-4,6 s · 8 fps · 15 kare)"
fi

echo "── ⑤ METİN KAPISI ⬜ [D45] — altyazı/etiket belirdi mi?"
ffmpeg -hide_banner -loglevel error -y -i "$M" \
  -vf "fps=1,scale=300:-1,tile=5x2" -frames:v 1 "$OUT/${B}_metin.png" 2>/dev/null \
  && echo "   BAKILACAK: $OUT/${B}_metin.png"
echo "═══════════════════════════════════════════════════════"
