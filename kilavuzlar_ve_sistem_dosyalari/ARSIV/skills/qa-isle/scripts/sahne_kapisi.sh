#!/bin/bash
# SAHNE KAPISI ⑬ — sahne ↔ prompt uyum merceğinin MAKİNE YARISI (11.09.2026)
# Kullanım: sahne_kapisi.sh <master_video> [klip_saniye=10] [prompt_sayısı] [scdet_eşiği=5]
#
# olcum_kapisi.sh master'a BİR BÜTÜN olarak bakar; bu betik SAHNE SAHNE bakar.
# Çıktısı ⑬ rubriğine yapıştırılmak üzere markdown tablodur: merceğe "ekranda ne
# var" sorusunun SAYIYLA cevaplanabilen yarısını verir, model o yarıyı tahmin etmez.
#
# ⛔ IZGARA KAPISI: prompt_sayısı verilirse ve sahne sayısı tutmazsa TESLİM
#    UYUŞMAZLIĞI basılır, çıkış kodu 1 olur. O hâlde hiçbir mercek koşulmaz:
#    önce hangi makaranın ölçüldüğü kapanır [D188]. Ölçülen vaka THE_TETHERED_MASS:
#    plan 16 sahne yazıyordu, dört mercek makarada 32 sahne saydı.
#
# ⭐ YÖNTEM NOTU — neden scdet, neden select değil (11.09.2026 · ölçüldü):
#    Depodaki mevcut kesme sayımı `select='gt(scene,0.3)'` kullanıyor ve
#    olcum_kapisi.sh'in kendi notu "karanlık filmde kesme görmez" diyor. Sentetik
#    bir test makarasında (3 sahne, düz renkler) scene skoru 0,13 çıktı ve 0,3
#    eşiği İKİ kesmenin İKİSİNİ de kaçırdı — sahne sayısı 1 göründü. `scdet` aynı
#    dosyada iki kesmeyi de tam saniyesinde buldu (skor 5,1 ve 5,5). Sahne SAYISI
#    bu kapının ölçtüğü şey olduğu için birincil dedektör scdet'tir; ayrıca ızgara
#    BİLİNDİĞİ için her beklenen sınır ayrıca tek tek doğrulanır.
#
# FİLTRE KURU KOŞUSU [D142] — 11.09.2026 · ffmpeg 8.1:
#    scdet ✅ · freezedetect ✅ · signalstats ✅ · silencedetect ✅ · ffprobe ✅
#    vidstabdetect ❌ YOK → kamera sabitliği burada ÖLÇÜLMEZ (⑨ KADRAJ'ın işi)
set -u

M="${1:-}"
KLIP="${2:-10}"
BEKLENEN="${3:-}"
ESIK="${4:-5}"

if [ -z "$M" ]; then
  echo "KULLANIM: sahne_kapisi.sh <master_video> [klip_saniye=10] [prompt_sayısı] [scdet_eşiği=5]"
  exit 2
fi
[ -f "$M" ] || { echo "HATA: dosya bulunamadı: $M"; exit 2; }
command -v ffprobe >/dev/null 2>&1 || { echo "HATA: ffprobe yok"; exit 3; }
command -v ffmpeg  >/dev/null 2>&1 || { echo "HATA: ffmpeg yok"; exit 3; }

FILTRE_VAR() { ffmpeg -hide_banner -filters 2>/dev/null | grep -q " $1 "; }
FILTRE_VAR scdet || { echo "HATA: scdet filtresi YOK — bu kapı ölçemez [D142]"; exit 3; }

echo "== DOSYA =="
echo "$M"
command -v shasum >/dev/null 2>&1 && echo "SHA-256: $(shasum -a 256 "$M" | awk '{print $1}')"

echo
echo "== SÜRE / ÇÖZÜNÜRLÜK / FPS =="
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M")
WH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$M")
echo "süre: ${DUR} s · akış: ${WH}"
AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M")
if [ -z "$AUDIO" ]; then echo "SES KANALI: YOK  🔴 [D136] — ses ihraç edilmemiş olabilir"
else echo "SES KANALI: VAR"; fi

# ─── kesme taraması (scdet) ──────────────────────────────────────────
KESMELER=$(ffmpeg -hide_banner -i "$M" -filter:v "scdet=threshold=${ESIK},metadata=print" \
           -f null - 2>&1 | grep -oE "lavfi\.scd\.time=[0-9.]+" | cut -d= -f2 | sort -n | uniq)
KESME_N=$(printf "%s\n" "$KESMELER" | grep -c '[0-9]' || true)

IZGARA_N=$(awk -v d="$DUR" -v k="$KLIP" 'BEGIN{ printf "%d", int(d/k + 0.5) }')
TESPIT_N=$((KESME_N + 1))

echo
echo "== SAHNE SAYISI — İKİ KAYNAK =="
echo "  süreden türetilen : $IZGARA_N   (${DUR} s ÷ ${KLIP} s)"
echo "  kesmeden türetilen: $TESPIT_N   (${KESME_N} kesme + 1 · scdet eşiği ${ESIK})"
if [ "$IZGARA_N" -ne "$TESPIT_N" ]; then
  echo "  🔴 İKİ KAYNAK AYRIŞIYOR — ya ızgara sabit değil ya kesmelerin bir kısmı görülmüyor."
  echo "     Eşiği düşürüp tekrar koş (4. argüman), sonra gözle bir kareyle doğrula."
else
  echo "  ✅ iki kaynak aynı sayıyı veriyor"
fi

echo
echo "== IZGARA DOĞRULAMA — her beklenen sınırda kesme var mı =="
k=1
EKSIK=0
while [ "$k" -lt "$IZGARA_N" ]; do
  T=$(awk -v k="$k" -v s="$KLIP" 'BEGIN{ printf "%.2f", k*s }')
  YAKIN=$(printf "%s\n" "$KESMELER" | awk -v t="$T" 'BEGIN{best=""} /[0-9]/ {d=$1-t; if(d<0)d=-d; if(d<=0.5){ if(best==""||d<bd){best=$1;bd=d} }} END{print best}')
  if [ -n "$YAKIN" ]; then
    printf "  %7.2f s → kesme VAR (%s)\n" "$T" "$YAKIN"
  else
    printf "  %7.2f s → 🔴 KESME YOK — iki sahne birleşmiş ya da ızgara kaymış\n" "$T"
    EKSIK=$((EKSIK + 1))
  fi
  k=$((k + 1))
done
[ "$EKSIK" -eq 0 ] && echo "  ✅ beklenen sınırların hepsinde kesme var"

echo
echo "== IZGARA DIŞI KESME — beklenmeyen yerde kesilmiş mi =="
FAZLA=$(printf "%s\n" "$KESMELER" | awk -v s="$KLIP" '/[0-9]/ { t=$1; n=int(t/s+0.5); d=t-n*s; if(d<0)d=-d; if(d>0.5) printf "  %8.2f s → 🔴 ızgara dışı (en yakın kata uzaklık %.2f s)\n", t, d }')
if [ -n "$FAZLA" ]; then printf "%s\n" "$FAZLA"; else echo "  ✅ ızgara dışı kesme yok"; fi

echo
echo "== SAHNE TABLOSU (⑬ rubriğine yapıştırılacak) =="
echo
echo "| sahne | başlangıç | klip içi kesme | donma | YAVG | YMIN | not |"
echo "|---|---:|:--:|:--:|---:|---:|---|"

i=0
while [ "$i" -lt "$IZGARA_N" ]; do
  BAS=$(awk -v i="$i" -v k="$KLIP" 'BEGIN{ printf "%.1f", i*k }')
  IBAS=$(awk -v b="$BAS" 'BEGIN{ printf "%.2f", b+0.3 }')
  ISUR=$(awk -v k="$KLIP" 'BEGIN{ printf "%.2f", k-0.6 }')

  IC=$(ffmpeg -hide_banner -ss "$IBAS" -t "$ISUR" -i "$M" \
        -filter:v "scdet=threshold=${ESIK},metadata=print" -f null - 2>&1 \
        | grep -c "lavfi\.scd\.time=" || true)

  if FILTRE_VAR freezedetect; then
    DN=$(ffmpeg -hide_banner -ss "$IBAS" -t "$ISUR" -i "$M" \
          -vf "freezedetect=n=-60dB:d=2" -f null - 2>&1 | grep -c "freeze_start" || true)
    if [ "$DN" -gt 0 ]; then DONMA="🔴 VAR"; else DONMA="yok"; fi
  else
    DONMA="⬜"
  fi

  ORTA=$(awk -v b="$BAS" -v k="$KLIP" 'BEGIN{ printf "%.2f", b+k/2 }')
  YAVG="⬜"; YMIN="⬜"
  if FILTRE_VAR signalstats; then
    STAT=$(ffmpeg -hide_banner -ss "$ORTA" -i "$M" -frames:v 1 \
            -vf "signalstats,metadata=print" -f null - 2>&1)
    Y1=$(printf "%s" "$STAT" | grep -oE "YAVG=[0-9.]+" | head -1 | cut -d= -f2)
    Y2=$(printf "%s" "$STAT" | grep -oE "YMIN=[0-9.]+" | head -1 | cut -d= -f2)
    [ -n "$Y1" ] && YAVG="$Y1"; [ -n "$Y2" ] && YMIN="$Y2"
  fi

  NOT=""
  [ "$IC" -gt 0 ] && NOT="🔴 klip içinde kesme — 'single unbroken take' iddiası düştü"
  case "$YAVG" in
    ⬜) ;;
    *) awk -v y="$YAVG" 'BEGIN{ exit !(y+0 < 18) }' && NOT="${NOT}${NOT:+ · }🔴 YAVG<18 — gölge içi dolgu yok" ;;
  esac

  printf "| S%02d | %s s | %s | %s | %s | %s | %s |\n" "$i" "$BAS" "$IC" "$DONMA" "$YAVG" "$YMIN" "$NOT"
  i=$((i + 1))
done

echo
echo "== SESSİZLİK (silencedetect -60dB / 1.0 s) =="
if [ -n "$AUDIO" ] && FILTRE_VAR silencedetect; then
  ffmpeg -hide_banner -i "$M" -af "silencedetect=noise=-60dB:d=1.0" -f null - 2>&1 \
    | grep -E "silence_(start|end|duration)" | head -20 || echo "  (1 s'den uzun sessizlik yok)"
else
  echo "  (ses kanalı ya da filtre yok)"
fi

echo
echo "== ⛔ IZGARA / TESLİM KAPISI [D188] =="
echo "  ölçülen sahne (süreden) : $IZGARA_N"
echo "  ölçülen sahne (kesmeden): $TESPIT_N"
if [ -n "$BEKLENEN" ]; then
  BEKLENEN_SURE=$(awk -v n="$BEKLENEN" -v k="$KLIP" 'BEGIN{ printf "%.1f", n*k }')
  echo "  prompt sayısı           : $BEKLENEN   → beklenen süre ${BEKLENEN_SURE} s"
  if [ "$IZGARA_N" -ne "$BEKLENEN" ] || [ "$TESPIT_N" -ne "$BEKLENEN" ]; then
    echo "  ------------------------------------------------------------"
    echo "  🚨 TESLİM UYUŞMAZLIĞI — ölçülen makara plandaki film DEĞİL."
    echo "  ⛔ Hiçbir mercek koşulmaz, ⑬ dahil. Önce ŞU kapanır: hangi dosya ölçüldü?"
    echo "     İki şık: ① yanlış dosya ölçüldü  ② film plandan farklı üretildi."
    echo "     Cevap üretim defterinin TESLİM SATIRI'na yazılır, rapora değil."
    exit 1
  fi
  echo "  ✅ sahne sayısı prompt sayısıyla tutuyor — ⑬ koşabilir"
else
  echo "  prompt sayısı           : ⬜ VERİLMEDİ — kapı KOŞMADI"
  echo "  ⚠️ Üçüncü argüman: bölüm dosyalarındaki 🎥 VİDEO PROMPT sayısı."
  echo "     grep -c '### 🎥' <FILM>_BOLUM_*.md   ← toplamı ver"
  echo "     Bu kapı koşmadan ⑬'ün STEP 0'ı boştur."
fi

echo
echo "== SAHNE KAPISI BİTTİ =="
