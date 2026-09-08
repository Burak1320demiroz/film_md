#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  FİLM KLASÖRÜ AÇ — iskeleti kur, sahne çalışma dosyalarını damgala,
#  okuma çizelgesini üret
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR:
#  İskelet TEK YERDE tanımlı (KILAVUZ_REHBERI §2.0) ve kopyalanabilir hâli
#  FILM_KLASOR_SABLONU/. Ama kopyalama TARİF olarak dört ayrı belgeye
#  yazılmıştı (AGENTS Kart A · §2.0 · şablon README · yeni-film skill) ve
#  dördü de birbirinden kayabiliyordu. 00_SABLON_README'nin kendi cümlesi:
#  "Nesre yazılmış yapı uygulanmıyor, kopyalanabilir yapı uygulanıyor."
#  Bu betik o cümlenin kopyalama adımına uygulanmış hâlidir.
#
#  KULLANIM:
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
#  ÖRNEK:
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           yatay_3_5_dk_filmler THE_QUIET_ANCHOR 25
#
#  ⛔ Var olan film klasörünün üstüne YAZMAZ.
#  ⛔ Sahne sayısı 02_KONSEPT_VE_RISK'in KLİP SÜRESİ ölçümünden gelir [D124];
#     bu betik onu doğrulamaz, yalnız damgalar.
# ═══════════════════════════════════════════════════════════════════
set -u

# ── --sahne-guncelle: sahne sayısı 03_SAHNE_SIRALAMASI'nda değişince ────
#    Var olan klasöre EKSİK S dosyalarını damgalar. Var olan dosyaya
#    DOKUNMAZ — sahne çalışması saatler süren bir iştir, ezilmez.
GUNCELLE=0; ARGS=()
for a in "$@"; do
  case "$a" in --sahne-guncelle) GUNCELLE=1 ;; *) ARGS+=("$a") ;; esac
done
set -- ${ARGS[@]+"${ARGS[@]}"}

FMT="${1:-}"; FILM="${2:-}"; N="${3:-}"; BOLUM="${4:-}"
if [ -z "$FMT" ] || [ -z "$FILM" ] || [ -z "$N" ]; then
  echo "KULLANIM: film_klasoru_ac.sh <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]"
  echo "FORMAT:   dikey_shorts_filmler · yatay_2_4_dk_filmler_uzay · yatay_3_5_dk_filmler · yatay_10_20_dk_filmler"
  exit 2
fi
cd "$(dirname "$0")/.." || exit 1
K="kilavuzlar_ve_sistem_dosyalari"
SAB="$K/FILM_KLASOR_SABLONU"

[ -d "$FMT" ]  || { echo "⛔ format klasörü yok: $FMT"; exit 2; }
[ -d "$SAB" ]  || { echo "⛔ şablon yok: $SAB"; exit 2; }
if [ "$GUNCELLE" -eq 0 ]; then
  [ -e "$FMT/$FILM" ] && { echo "⛔ ZATEN VAR: $FMT/$FILM — üstüne yazılmadı."; \
                           echo "   Sahne sayısı değiştiyse: --sahne-guncelle"; exit 2; }
else
  [ -d "$FMT/$FILM" ] || { echo "⛔ --sahne-guncelle için klasör VAR olmalı: $FMT/$FILM"; exit 2; }
fi
case "$FILM" in
  *[!A-Z0-9_]*) echo "⛔ AD BİÇİMİ: BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok · boşluk yok"; exit 2;;
esac
case "$N" in ''|*[!0-9]*) echo "⛔ SAHNE_SAYISI bir sayı olmalı: $N"; exit 2;; esac
[ "$N" -lt 2 ] && { echo "⛔ SAHNE_SAYISI ≥ 2"; exit 2; }

# Bölüm sayısı FORMATTAN gelir, tercih değil [§2.0] — override edilebilir.
if [ -z "$BOLUM" ]; then
  case "$FMT" in
    dikey_shorts_filmler|yatay_2_4_dk_filmler_uzay|yatay_3_5_dk_filmler) BOLUM=2 ;;
    *) BOLUM=2; echo "⚠️  $FMT için bölüm sayısı FAZ sayısı kadardır (§2.0)."
       echo "   Varsayılan 2 kullanıldı — faz sayısı farklıysa 4. argümanla ver." ;;
  esac
fi

HEDEF="$FMT/$FILM"

# ── yalnız sahne damgalama modu ────────────────────────────────────
if [ "$GUNCELLE" -eq 1 ]; then
  CS="$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI"
  SABS="$CS/00_SAHNE_CALISMA_SABLONU.md"
  [ -f "$SABS" ] || SABS="$SAB/00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_CALISMA_SABLONU.md"
  mkdir -p "$CS"
  YENI=0; VAR=0; i=0
  while [ "$i" -lt "$N" ]; do
    NN=$(printf "%02d" "$i")
    if [ -f "$CS/S$NN.md" ]; then VAR=$((VAR + 1)); else
      sed -e "s/<NN>/$NN/g" -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" \
          "$SABS" > "$CS/S$NN.md"
      YENI=$((YENI + 1))
    fi
    i=$((i + 1))
  done
  FAZLA=$(ls -1 "$CS"/S[0-9][0-9].md 2>/dev/null | wc -l | tr -d ' ')
  echo "✅ SAHNE DAMGASI · $FILM — $YENI yeni · $VAR zaten vardı · klasörde toplam $FAZLA"
  [ "$FAZLA" -gt "$N" ] && echo "⚠️  Klasörde $N sahneden FAZLA dosya var — sıralamadan düşen sahneler ELLE silinir."
  exit 0
fi

cp -r "$SAB" "$HEDEF" || exit 1
rm -f "$HEDEF/00_SABLON_README.md"

# ── film dosyaları: FILM_*.md → <FILM>_*.md ────────────────────────
for f in "$HEDEF"/FILM_*.md; do
  [ -e "$f" ] || continue
  mv "$f" "$HEDEF/${FILM}_$(basename "${f#"$HEDEF"/FILM_}")"
done

# ── bölüm dosyaları: formatın istediği sayıya tamamla ──────────────
if [ "$BOLUM" -gt 2 ]; then
  i=3
  while [ "$i" -le "$BOLUM" ]; do
    cp "$HEDEF/${FILM}_BOLUM_2.md" "$HEDEF/${FILM}_BOLUM_$i.md"
    i=$((i + 1))
  done
elif [ "$BOLUM" -eq 1 ]; then
  rm -f "$HEDEF/${FILM}_BOLUM_2.md"
fi

# ── sahne çalışma dosyaları: S00 … S(N-1) ──────────────────────────
CS="$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI"
SABS="$CS/00_SAHNE_CALISMA_SABLONU.md"
i=0
while [ "$i" -lt "$N" ]; do
  NN=$(printf "%02d" "$i")
  sed "s/<NN>/$NN/g" "$SABS" > "$CS/S$NN.md"
  i=$((i + 1))
done

# ── yer tutucular ──────────────────────────────────────────────────
find "$HEDEF" -name "*.md" -type f -exec sed -i '' \
     -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" {} +

# ── okuma çizelgesi ────────────────────────────────────────────────
bash "$K/okuma_cizelgesi.sh" "$HEDEF" > /dev/null 2>&1 \
  && CIZ="✅ üretildi" || CIZ="⛔ ÜRETİLEMEDİ — elle koş"

# ── bölüm dağılımı önerisi (§2.0: 3-5 dk = 13 + 12) ────────────────
YARI=$(( (N + 1) / 2 ))

cat <<OZET

═══════════════════════════════════════════════════════
  🎬 $FILM — klasör açıldı
═══════════════════════════════════════════════════════
  YOL:            $HEDEF
  SAHNE:          $N        BÖLÜM: $BOLUM
  BÖLÜM ÖNERİSİ:  S0-S$((YARI - 1)) ($YARI) · S$YARI-S$((N - 1)) ($((N - YARI)))
                  ⛔ bölüm SINIRI da ardışık bir ÇİFTTİR (≥1 ölçek + ≥45°)
  ÇALIŞMA DOSYASI: 00_ANALIZ/05_SAHNE_CALISMALARI/S00.md … S$(printf "%02d" $((N - 1))).md
  OKUMA ÇİZELGESİ: $CIZ

  ⛔ SIRA — atlanmaz:
     00_ANALIZ/00_OKUMA_CIZELGESI.md   TÜM ders + TÜM kılavuz + QA raporu
     00_ANALIZ/01_QA_DERS_HASADI.md    bu filme düşen kilitler
     00_ANALIZ/02_KONSEPT_VE_RISK.md   konsept kapısı · risk · B5
     00_ANALIZ/03_SAHNE_SIRALAMASI.md  $N sahnenin sırası
     00_ANALIZ/04_UYARI_NOTLARI.md     ölçülmüş arızalara bağlı uyarılar
     00_ANALIZ/05_SAHNE_CALISMALARI/   sahne sahne çalışma
     → ANCAK SONRA ${FILM}_PLAN.md yazılır.

  ⛔ REFERANS PAKETİ: dosya klasörde \`⬜ BEKLİYOR\` durumunda.
     İSTEĞE BAĞLI (08.09.2026 · sahip kararı) — yazılmazsa PLAN'a
     tek satır gerekçe. Yazılırsa KAPI 0'dır: onaysız sayfanın
     varlığı geçtiği hiçbir sahne üretilmez.

  ⛔ COMMIT ATILMAZ — yalnız proje sahibi atar.
═══════════════════════════════════════════════════════
OZET
