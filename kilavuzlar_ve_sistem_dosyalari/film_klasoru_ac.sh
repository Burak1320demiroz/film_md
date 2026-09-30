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
#           yatay_4_dk_filmler THE_QUIET_ANCHOR 24
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           yatay_6_dk_filmler THE_LONG_SHELF 36        # 13.09.2026 · 2 × 18
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           yatay_16_dk_filmler THE_STOLEN_SKY 96       # 19.09.2026 · 8 × 12 (§2.8)
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           yatay_32_dk_filmler THE_DEEP_ORBIT 192      # 22.09.2026 · 16 × 12 (§2.9)
#      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
#           yatay_64_dk_filmler THE_ENDLESS_EXPEDITION 384 # 22.09.2026 · 32 × 12 (§2.10)
#
#  ⛔ Var olan film klasörünün üstüne YAZMAZ.
#  ⛔ Sahne sayısı 02_KONSEPT_VE_RISK'in KLİP SÜRESİ ölçümünden gelir [D124];
#     bu betik onu doğrulamaz, yalnız damgalar.
#
#  --analiz-ekle  (11.09.2026 · THE SCOURED GLASS): 08.09 iskeletinden ÖNCE
#     açılmış bir film klasörüne YALNIZ 00_ANALIZ/ ekler. Var olan hiçbir
#     dosyaya dokunmaz; 00_ANALIZ zaten varsa çıkar. Sahne damgası
#     --sahne-guncelle ile ayrıca koşulur.
#  SAHNE_BASLANGIC=1 ortam değişkeni: damga S01'den başlar (S00 = hook
#     kuralı olmayan hatlar — 7-20 dk faz filmleri S1'den sayar).
#
#  ⭐ 14.09.2026 · REFORM FAZ 8-9 (sahip kararı · TODO_AKIS_VE_DERS_REFORMU.md):
#  · SAHNE_SAYISI > 8 → sahne başına dosya DAMGALANMAZ; 05_SAHNE_CALISMALARI/
#    00_SAHNE_TABLOSU.md N satırla üretilir (LOCKED_PULSE: 25 × 120 satır → 747 KB,
#    üretim 0 kare). ≤ 8 sahne (dikey) eskisi gibi S dosyası alır.
#  · --kilit-sahne <FMT> <FILM> <Snn> <ROL>  ROL ∈ HOOK NOVUM DORUK BEDEL FINAL:
#    o sahneye tam şablonla S<nn>_<ROL>.md damgalar (en çok 5; prompt_kontrol ㉚).
#  · 00_ANALIZ/00_HIKAYE_ONAYI.md şablondan kopyalanır — YENİ REJİM işaretidir:
#    prompt_kontrol.py bu dosyayı gören klasörde ㉕-㉚ kapılarını koşar.
#    --analiz-ekle bu dosyayı KOPYALAMAZ (eski film eski rejimde kalır — sahip kararı;
#    yeni rejime almak isteyen sahip dosyayı şablondan elle kopyalar).
#  · OKUMA_CEKIRDEGI.txt manifesti şablonda durur, film klasörüne kopyalanmaz
#    (okuma_cizelgesi.sh onu şablondan okur — tek kaynak).
#
#  ⭐ 22.09.2026 · ÇOK KLİPLİ SAHNE (sahip kararı · COK_KLIPLI_SAHNE_KILAVUZU.md):
#  · --sahne-plani "1 3 4 4 2 4 6"  sahne başına klip sayısı; 3. argüman (N) toplam
#    KLİP sayısıdır. Betik doğrular: toplam = N · her sahne 1-6 klip · hiçbir sahne
#    bölüm dosyası sınırını aşmaz. Damgalar: PLAN'a `SAHNE PLANI:` satırı (㉜ tetiği) ·
#    tabloya KLİP başına satır `| K01 | S01 | 1/3 · ⬜ |` · hikâye onayına SAHNE başına
#    satır `S1 (3 klip · 0:00–0:30) — ⬜` · bölüm dosyalarına `# 📍 SAHNE` / `## 🎬 KLİP`
#    iskeleti. Yalnız yeni klasör açarken ve yalnız yatay formatta.
#    Seçenek verilmezse betik bugünkü davranışı BİREBİR sürdürür.
#    Örnek: film_klasoru_ac.sh yatay_4_dk_filmler THE_QUIET_ANCHOR 24 --sahne-plani "1 3 4 4 2 4 6"
#
#  ⭐ 22.09.2026 · ÖN PLAN (sahip isteği · THE_FALSE_EARTH, ilk 32 dk film):
#  · yeni-film akışından ÖNCE sahibin tretmanı ve sahne planı taslağı
#    <FORMAT>/<FILM>/00_ON_PLAN/ altında hazırlanabilir. Klasörde YALNIZ
#    00_ON_PLAN/ varsa betik filmi onun üstüne açar ve ön planı dokunmadan
#    00_ANALIZ/00_ON_PLAN/'a taşır (başka herhangi bir dosya varsa ⛔ ZATEN VAR).
#    prompt_kontrol.py ATLA deseni 00_ON_PLAN yolunu atlar.
# ═══════════════════════════════════════════════════════════════════
set -u

# ── --sahne-guncelle: sahne sayısı 03_SAHNE_SIRALAMASI'nda değişince ────
#    Var olan klasöre EKSİK S dosyalarını damgalar. Var olan dosyaya
#    DOKUNMAZ — sahne çalışması saatler süren bir iştir, ezilmez.
GUNCELLE=0; ANALIZ_EKLE=0; KILIT_SAHNE=0; ARGS=(); SAHNE_PLANI=""; BEKLE_PLAN=0
for a in "$@"; do
  if [ "$BEKLE_PLAN" -eq 1 ]; then SAHNE_PLANI="$a"; BEKLE_PLAN=0; continue; fi
  case "$a" in
    --sahne-plani)    BEKLE_PLAN=1 ;;
    --sahne-guncelle) GUNCELLE=1 ;;
    --analiz-ekle)    ANALIZ_EKLE=1 ;;
    --kilit-sahne)    KILIT_SAHNE=1 ;;
    *) ARGS+=("$a") ;;
  esac
done
BASLANGIC="${SAHNE_BASLANGIC:-0}"
case "$BASLANGIC" in ''|*[!0-9]*) BASLANGIC=0 ;; esac
set -- ${ARGS[@]+"${ARGS[@]}"}
TABLO_ESIGI=8   # > 8 sahne → tablo + 5 kilit sahne dosyası (prompt_kontrol.py KILIT_SAHNE_ESIGI ile aynı)

# ── --kilit-sahne: >8 sahnelik filmde beş kilit sahneye tam çalışma dosyası ──
if [ "$KILIT_SAHNE" -eq 1 ]; then
  FMT="${1:-}"; FILM="${2:-}"; SNN="${3:-}"; ROL="${4:-}"
  if [ -z "$FMT" ] || [ -z "$FILM" ] || [ -z "$SNN" ] || [ -z "$ROL" ]; then
    echo "KULLANIM: film_klasoru_ac.sh --kilit-sahne <FORMAT_KLASORU> <FILM_ADI> <Snn|Knn> <ROL>"
    echo "ROL:      HOOK · NOVUM · DORUK · BEDEL · FINAL   (her rol bir kez)"; exit 2
  fi
  cd "$(dirname "$0")/.." || exit 1
  K="kilavuzlar_ve_sistem_dosyalari"; SAB="$K/FILM_KLASOR_SABLONU"
  HEDEF="$FMT/$FILM"; CS="$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI"
  [ -d "$CS" ] || { echo "⛔ klasör yok: $CS"; exit 2; }
  case "$ROL" in HOOK|NOVUM|DORUK|BEDEL|FINAL) ;; *) echo "⛔ ROL ∈ HOOK NOVUM DORUK BEDEL FINAL — verilen: $ROL"; exit 2;; esac
  # 22.09.2026: çok klipli sahne filminde rol KLİBE bağlanır → K<nn>
  case "$SNN" in S[0-9][0-9]|S[0-9][0-9][0-9]|K[0-9][0-9]|K[0-9][0-9][0-9]) ;; *) echo "⛔ sahne S<nn> ya da klip K<nn> biçiminde: S20 · K20"; exit 2;; esac
  NN="${SNN#[SK]}"
  VAR_ROL=$(ls -1 "$CS"/[SK]*_"$ROL".md 2>/dev/null | head -1)
  [ -n "$VAR_ROL" ] && { echo "⛔ $ROL rolü zaten damgalı: $VAR_ROL — her rol bir kez."; exit 2; }
  [ -e "$CS/${SNN}_$ROL.md" ] && { echo "⛔ ZATEN VAR: $CS/${SNN}_$ROL.md"; exit 2; }
  SABS="$CS/00_SAHNE_CALISMA_SABLONU.md"
  [ -f "$SABS" ] || SABS="$SAB/00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_CALISMA_SABLONU.md"
  sed -e "s/<NN>/$NN/g" -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" \
      -e "1s/SAHNE ÇALIŞMASI/KİLİT SAHNE · $ROL · SAHNE ÇALIŞMASI/" "$SABS" > "$CS/${SNN}_$ROL.md"
  ROLLER=$(ls -1 "$CS"/[SK]*_*.md 2>/dev/null | sed -e 's/.*_//' -e 's/\.md$//' | tr '\n' ' ')
  echo "✅ KİLİT SAHNE · $FILM $SNN → $ROL   ($CS/${SNN}_$ROL.md)"
  echo "   damgalı roller: ${ROLLER}— beşi de (HOOK NOVUM DORUK BEDEL FINAL) damgalanmadan prompt_kontrol ㉚ FIX verir"
  exit 0
fi

FMT="${1:-}"; FILM="${2:-}"; N="${3:-}"; BOLUM="${4:-}"
if [ -z "$FMT" ] || [ -z "$FILM" ] || [ -z "$N" ]; then
  echo "KULLANIM: film_klasoru_ac.sh <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]"
  echo "FORMAT:   dikey_shorts_filmler · yatay_2_dk_filmler · yatay_4_dk_filmler ·"
  echo "          yatay_8_dk_filmler · yatay_16_dk_filmler ·"
  echo "          yatay_32_dk_filmler · yatay_64_dk_filmler"
  exit 2
fi
cd "$(dirname "$0")/.." || exit 1
K="kilavuzlar_ve_sistem_dosyalari"
SAB="$K/FILM_KLASOR_SABLONU"

[ -d "$FMT" ]  || { echo "⛔ format klasörü yok: $FMT"; exit 2; }
[ -d "$SAB" ]  || { echo "⛔ şablon yok: $SAB"; exit 2; }
ON_PLAN=0
if [ "$GUNCELLE" -eq 0 ] && [ "$ANALIZ_EKLE" -eq 0 ]; then
  # 22.09.2026 · ÖN PLAN (THE_FALSE_EARTH): klasörde YALNIZ 00_ON_PLAN/ varsa film
  # onun üstüne açılır; 00_ON_PLAN/ dokunulmadan 00_ANALIZ/00_ON_PLAN/'a taşınır.
  if [ -d "$FMT/$FILM/00_ON_PLAN" ] && \
     [ -z "$(ls -A "$FMT/$FILM" | grep -v -e '^00_ON_PLAN$' -e '^\.DS_Store$')" ]; then
    ON_PLAN=1
  else
    [ -e "$FMT/$FILM" ] && { echo "⛔ ZATEN VAR: $FMT/$FILM — üstüne yazılmadı."; \
                             echo "   Sahne sayısı değiştiyse: --sahne-guncelle · eski klasöre analiz: --analiz-ekle"; exit 2; }
  fi
else
  [ -d "$FMT/$FILM" ] || { echo "⛔ --sahne-guncelle / --analiz-ekle için klasör VAR olmalı: $FMT/$FILM"; exit 2; }
fi
case "$FILM" in
  *[!A-Z0-9_]*) echo "⛔ AD BİÇİMİ: BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok · boşluk yok"; exit 2;;
esac
case "$N" in ''|*[!0-9]*) echo "⛔ SAHNE_SAYISI bir sayı olmalı: $N"; exit 2;; esac
[ "$N" -lt 2 ] && { echo "⛔ SAHNE_SAYISI ≥ 2"; exit 2; }

# Bölüm sayısı FORMATTAN gelir, tercih değil [§2.0] — override edilebilir.
if [ -z "$BOLUM" ]; then
  case "$FMT" in
    dikey_shorts_filmler|yatay_2_dk_filmler|yatay_4_dk_filmler) BOLUM=2 ;;
    # 13.09.2026 · 12-sahne modül merdiveni: 36 = 18 + 18 · 48 = 24 + 24 (§2.6 / §2.7)
    yatay_6_dk_filmler|yatay_8_dk_filmler) BOLUM=2 ;;
    # 19.09.2026 · beşinci basamak: 96 = 8 × 12 (§2.8) — QA parçası 2 dosyadır (4 PART)
    yatay_16_dk_filmler) BOLUM=8 ;;
    # 22.09.2026 · altıncı ve yedinci basamaklar (§2.9 / §2.10)
    yatay_32_dk_filmler) BOLUM=16 ;;
    yatay_64_dk_filmler) BOLUM=32 ;;
    *) BOLUM=2; echo "⚠️  $FMT için bölüm sayısı FAZ sayısı kadardır (§2.0)."
       echo "   Varsayılan 2 kullanıldı — faz sayısı farklıysa 4. argümanla ver." ;;
  esac
fi

HEDEF="$FMT/$FILM"

# ── --sahne-plani doğrulaması (22.09.2026) — klasöre dokunmadan ÖNCE ──
PLAN_LISTE=""; SAHNE_ADET=0
if [ "$BEKLE_PLAN" -eq 1 ] || { [ -n "$SAHNE_PLANI" ] && [ -z "$(echo "$SAHNE_PLANI" | tr -d ' ')" ]; }; then
  echo "⛔ --sahne-plani bir değer ister: --sahne-plani \"1 3 4 …\""; exit 2
fi
if [ -n "$SAHNE_PLANI" ]; then
  { [ "$GUNCELLE" -eq 1 ] || [ "$ANALIZ_EKLE" -eq 1 ]; } && { echo "⛔ --sahne-plani yalnız YENİ klasör açarken verilir"; exit 2; }
  case "$FMT" in dikey_*) echo "⛔ çok klipli sahne rejimi yalnız yatay formatta (sahip kararı 22.09.2026)"; exit 2;; esac
  [ "$N" -le "$TABLO_ESIGI" ] && { echo "⛔ çok klipli sahne rejimi > $TABLO_ESIGI klip ister (verilen $N)"; exit 2; }
  PLAN_LISTE=$(echo "$SAHNE_PLANI" | sed -e 's/[|,]/ /g' -e 's/·/ /g' | tr -s ' ' | sed -e 's/^ //' -e 's/ $//')
  TOP=0
  for k in $PLAN_LISTE; do
    case "$k" in *[!0-9]*) echo "⛔ SAHNE PLANI yalnız sayı taşır: '$k'"; exit 2;; esac
    { [ "$k" -lt 1 ] || [ "$k" -gt 6 ]; } && { echo "⛔ S$((SAHNE_ADET + 1)) $k klip — bant 1-6 (1 klip yalnız gerekçeyle)"; exit 2; }
    TOP=$((TOP + k)); SAHNE_ADET=$((SAHNE_ADET + 1))
  done
  [ "$TOP" -ne "$N" ] && { echo "⛔ SAHNE PLANI toplamı $TOP ≠ klip sayısı $N"; exit 2; }
  if [ $((N % BOLUM)) -eq 0 ]; then
    PAY=$((N / BOLUM)); CUM=0; SNO=0
    for k in $PLAN_LISTE; do
      SNO=$((SNO + 1)); ONCE=$CUM; CUM=$((CUM + k))
      if [ $((ONCE / PAY)) -ne $(((CUM - 1) / PAY)) ]; then
        echo "⛔ S$SNO (K$((ONCE + 1))-K$CUM) bölüm sınırını aşıyor — bölüm başına $PAY klip; her bölüm tam sahnelerle biter"; exit 2
      fi
    done
  else
    echo "⚠️  $N klip $BOLUM bölüme eşit bölünmüyor — bölüm sınırı denetimi atlandı (prompt_kontrol ㉜③ yine ölçer)"
  fi
fi

# ── yalnız 00_ANALIZ ekleme modu (eski klasöre iskelet) ─────────────
if [ "$ANALIZ_EKLE" -eq 1 ]; then
  [ -e "$HEDEF/00_ANALIZ" ] && { echo "⛔ ZATEN VAR: $HEDEF/00_ANALIZ — dokunulmadı."; exit 2; }
  cp -r "$SAB/00_ANALIZ" "$HEDEF/00_ANALIZ" || exit 1
  rm -f "$HEDEF/00_ANALIZ/00_OKUMA_CIZELGESI.md" "$HEDEF/00_ANALIZ/OKUMA_CEKIRDEGI.txt"
  # 14.09.2026: eski klasör ESKİ rejimde kalır — yeni rejim işareti kopyalanmaz (sahip kararı)
  rm -f "$HEDEF/00_ANALIZ/00_HIKAYE_ONAYI.md" "$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md"
  find "$HEDEF/00_ANALIZ" -name "*.md" -type f -exec sed -i '' \
       -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" {} +
  bash "$K/okuma_cizelgesi.sh" "$HEDEF" > /dev/null 2>&1 \
    && CIZ="✅ üretildi" || CIZ="⛔ ÜRETİLEMEDİ — elle koş"
  echo "✅ 00_ANALIZ EKLENDİ · $HEDEF/00_ANALIZ  (var olan film dosyalarına dokunulmadı)"
  echo "   OKUMA ÇİZELGESİ: $CIZ"
  echo "   REJİM: eski (00_HIKAYE_ONAYI.md kopyalanmadı) — yeni rejime almak sahibin kararı:"
  echo "          cp $SAB/00_ANALIZ/00_HIKAYE_ONAYI.md $HEDEF/00_ANALIZ/"
  echo "   Sahne damgası için: SAHNE_BASLANGIC=1 bash $0 $FMT $FILM <N> --sahne-guncelle"
  [ "$GUNCELLE" -eq 0 ] && exit 0
fi

# ── yalnız sahne damgalama modu ────────────────────────────────────
if [ "$GUNCELLE" -eq 1 ]; then
  CS="$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI"
  SABS="$CS/00_SAHNE_CALISMA_SABLONU.md"
  [ -f "$SABS" ] || SABS="$SAB/00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_CALISMA_SABLONU.md"
  mkdir -p "$CS"
  # 14.09.2026: hikâye onayı satırları da tamamlanır — eksik S satırı son S satırının altına
  HIK="$HEDEF/00_ANALIZ/00_HIKAYE_ONAYI.md"
  if [ -f "$HIK" ]; then
    EKSIK=""; i="$BASLANGIC"; SON=$((BASLANGIC + N))
    while [ "$i" -lt "$SON" ]; do
      grep -q "^S$i " "$HIK" || EKSIK="${EKSIK}S$i — ⬜\n"
      i=$((i + 1))
    done
    if [ -n "$EKSIK" ]; then
      awk -v s="$EKSIK" '
        /^S[0-9]+ / { son = NR } { satir[NR] = $0 }
        END { for (k = 1; k <= NR; k++) { print satir[k]; if (k == son) printf "%s", s } }' "$HIK" > "$HIK.tmp" \
        && mv "$HIK.tmp" "$HIK"
      echo "⚠️  HİKÂYE ONAYI: eksik sahne satırları eklendi — sahne sayısı değişti, YENİDEN ONAY gerekir (㉙: satır = sahne)"
    fi
  fi
  TAB="$CS/00_SAHNE_TABLOSU.md"
  if [ "$N" -gt "$TABLO_ESIGI" ] || [ -f "$TAB" ]; then
    # 14.09.2026: >8 sahne → tablo; eksik satırlar tamamlanır, var olan satıra dokunulmaz
    if [ ! -f "$TAB" ]; then
      sed -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" \
          "$SAB/00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md" > "$TAB"
    fi
    YENI=0; VAR=0; i="$BASLANGIC"; SON=$((BASLANGIC + N))
    while [ "$i" -lt "$SON" ]; do
      NN=$(printf "%02d" "$i")
      if grep -q "^| S$NN |" "$TAB"; then VAR=$((VAR + 1)); else
        printf '| S%s | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |\n' "$NN" >> "$TAB"
        YENI=$((YENI + 1))
      fi
      i=$((i + 1))
    done
    TOPLAM=$(grep -c "^| S[0-9]" "$TAB")
    echo "✅ SAHNE TABLOSU · $FILM — $YENI yeni satır · $VAR zaten vardı · tabloda toplam $TOPLAM"
    [ "$TOPLAM" -gt "$N" ] && echo "⚠️  Tabloda $N sahneden FAZLA satır var — sıralamadan düşen sahne satırları ELLE silinir (㉚ satır = sahne ister)."
    exit 0
  fi
  YENI=0; VAR=0; i="$BASLANGIC"; SON=$((BASLANGIC + N))
  while [ "$i" -lt "$SON" ]; do
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

ON_PLAN_GECICI="$FMT/.${FILM}_ON_PLAN_GECICI"
if [ "$ON_PLAN" -eq 1 ]; then
  [ -e "$ON_PLAN_GECICI" ] && { echo "⛔ geçici klasör zaten var: $ON_PLAN_GECICI — elle bak"; exit 2; }
  mv "$HEDEF" "$ON_PLAN_GECICI" || exit 1
fi
cp -r "$SAB" "$HEDEF" || exit 1
rm -f "$HEDEF/00_SABLON_README.md" "$HEDEF/00_ANALIZ/OKUMA_CEKIRDEGI.txt"

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

# ── sahne çalışması: ≤8 sahne → S dosyaları · >8 sahne → tablo (14.09.2026) ──
CS="$HEDEF/00_ANALIZ/05_SAHNE_CALISMALARI"
SABS="$CS/00_SAHNE_CALISMA_SABLONU.md"
TAB="$CS/00_SAHNE_TABLOSU.md"
if [ -n "$PLAN_LISTE" ]; then
  # 22.09.2026: satır = KLİP · ikinci sütun sahnesi · üçüncü sütun sahne içi rolü
  awk '
    /^\| S \| OLAY/ { sub(/^\| S \|/, "| K | SAHNE | ROL n/N |"); print; bas = 1; next }
    bas == 1        { sub(/^\|:--:\|/, "|:--:|:--:|---|"); print; bas = 0; next }
    { print }' "$TAB" > "$TAB.tmp" && mv "$TAB.tmp" "$TAB"
  KNO=0; SNO=0
  for k in $PLAN_LISTE; do
    SNO=$((SNO + 1)); j=1
    while [ "$j" -le "$k" ]; do
      KNO=$((KNO + 1))
      printf '| K%02d | S%02d | %s/%s · ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |\n' "$KNO" "$SNO" "$j" "$k" >> "$TAB"
      j=$((j + 1))
    done
  done
  CALISMA="00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md ($N klip satırı · $SAHNE_ADET sahne) + 5 kilit klip dosyası
                   → bash $0 --kilit-sahne $FMT $FILM K<nn> <HOOK|NOVUM|DORUK|BEDEL|FINAL>"
elif [ "$N" -gt "$TABLO_ESIGI" ]; then
  i="$BASLANGIC"; SON=$((BASLANGIC + N))
  while [ "$i" -lt "$SON" ]; do
    printf '| S%s | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |\n' "$(printf "%02d" "$i")" >> "$TAB"
    i=$((i + 1))
  done
  CALISMA="00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md ($N satır) + 5 kilit sahne dosyası
                   → bash $0 --kilit-sahne $FMT $FILM S<nn> <HOOK|NOVUM|DORUK|BEDEL|FINAL>"
else
  rm -f "$TAB"
  i="$BASLANGIC"; SON=$((BASLANGIC + N))
  while [ "$i" -lt "$SON" ]; do
    NN=$(printf "%02d" "$i")
    sed "s/<NN>/$NN/g" "$SABS" > "$CS/S$NN.md"
    i=$((i + 1))
  done
  CALISMA="00_ANALIZ/05_SAHNE_CALISMALARI/S$(printf "%02d" "$BASLANGIC").md … S$(printf "%02d" $((SON - 1))).md"
fi
# ── hikâye onayı: sahne satırları damgalanır (14.09.2026 · FAZ 9) ─────────
HIK="$HEDEF/00_ANALIZ/00_HIKAYE_ONAYI.md"
REJIM="eski (00_HIKAYE_ONAYI.md şablonda yok)"
sure() { printf "%d:%02d" $(($1 / 60)) $(($1 % 60)); }
if [ -f "$HIK" ] && [ -n "$PLAN_LISTE" ]; then
  # 22.09.2026: satır = SAHNE, klip sayısı ve zaman aralığı satırda (㉙ ikisini de sayar)
  SATIRLAR=""; SNO=0; CUM=0
  for k in $PLAN_LISTE; do
    SNO=$((SNO + 1))
    SATIRLAR="${SATIRLAR}S$SNO ($k klip · $(sure $((CUM * 10)))–$(sure $(((CUM + k) * 10)))) — ⬜\n"
    CUM=$((CUM + k))
  done
  awk -v s="$SATIRLAR" '$0 == "<SAHNE_SATIRLARI>" { printf "%s", s; next } { print }' "$HIK" > "$HIK.tmp" \
    && mv "$HIK.tmp" "$HIK"
  REJIM="YENİ + ÇOK KLİPLİ SAHNE — prompt_kontrol.py ㉕-㉚ + ㉜ bu klasörde koşar; ONAY tarihli olmadan analiz yazılmaz (㉙)"
elif [ -f "$HIK" ]; then
  SATIRLAR=""; i="$BASLANGIC"; SON=$((BASLANGIC + N))
  while [ "$i" -lt "$SON" ]; do SATIRLAR="${SATIRLAR}S$i — ⬜\n"; i=$((i + 1)); done
  awk -v s="$SATIRLAR" '$0 == "<SAHNE_SATIRLARI>" { printf "%s", s; next } { print }' "$HIK" > "$HIK.tmp" \
    && mv "$HIK.tmp" "$HIK"
  REJIM="YENİ — prompt_kontrol.py ㉕-㉚ bu klasörde koşar; ONAY tarihli olmadan analiz yazılmaz (㉙)"
fi

# ── çok klipli sahne: PLAN satırı + bölüm iskeleti (22.09.2026) ────────
if [ -n "$PLAN_LISTE" ]; then
  PLANF="$HEDEF/${FILM}_PLAN.md"
  awk -v p="$PLAN_LISTE" '
    /^BÖLÜM KESİĞİ:/ && !y {
      print "SAHNE PLANI: " p
      print "                 ⭐ ÇOK KLİPLİ SAHNE (22.09.2026) — sahne başına klip sayısı; toplam ="
      print "                   CLIP COUNT. BU SATIR ㉜ KAPISINI AÇAR ve ⑩④ KÜME hedefini kapatır"
      print "                   (zincir yok). Değişirse bölüm dosyalarındaki 📍 başlıkları + tablo +"
      print "                   hikâye onayı birlikte değişir. Kılavuz: COK_KLIPLI_SAHNE_KILAVUZU.md"
      y = 1 }
    { print }' "$PLANF" > "$PLANF.tmp" && mv "$PLANF.tmp" "$PLANF"
  grep -q "^SAHNE PLANI: " "$PLANF" || echo "SAHNE PLANI: $PLAN_LISTE" >> "$PLANF"
  PAY=$(( (N + BOLUM - 1) / BOLUM )); B=1; KNO=0; SNO=0; CUM=0
  set -- $PLAN_LISTE
  while [ "$B" -le "$BOLUM" ]; do
    BF="$HEDEF/${FILM}_BOLUM_$B.md"
    SINIR=$((B * PAY)); [ "$B" -eq "$BOLUM" ] && SINIR=$N
    ILK_K=$((KNO + 1)); ILK_S=$((SNO + 1)); GOVDE=""
    while [ "$#" -gt 0 ] && [ $((CUM + $1)) -le "$SINIR" ]; do
      k=$1; shift; SNO=$((SNO + 1))
      GOVDE="${GOVDE}# 📍 SAHNE $(printf %02d $SNO) — ⬜ AD  ($k klip · $(sure $((CUM * 10)))–$(sure $(((CUM + k) * 10))))\n\n"
      GOVDE="${GOVDE}> SAHNE KİLİDİ: ⬜ mekân · ışık · ses yatağı · kir/hasar durumu (Türkçe özet — prompta girmez)\n"
      [ "$k" -eq 1 ] && GOVDE="${GOVDE}> TEK KLİP GEREKÇESİ: ⬜ (yalnız HOOK ya da geçiş)\n"
      GOVDE="${GOVDE}\n"
      j=1
      while [ "$j" -le "$k" ]; do
        KNO=$((KNO + 1))
        GOVDE="${GOVDE}## 🎬 KLİP $(printf %02d $KNO) — S$(printf %02d $SNO) · $j/$k · ⬜ ROL — ⬜ BAŞLIK\n\n"
        if [ "$j" -eq 1 ]; then
          GOVDE="${GOVDE}*(V3 iskeleti — Clip $KNO of $N. · sahne başı: CONTINUOUS ACTION YAZILMAZ)*\n\n"
        else
          GOVDE="${GOVDE}*(V3 iskeleti — Clip $KNO of $N. · IMAGE ve VIDEO'da CONTINUOUS ACTION: satırı ZORUNLU · LIGHT/PHYSICS/AUDIO ilk cümlesi sahnenin 1. klibiyle BİREBİR)*\n\n"
        fi
        j=$((j + 1))
      done
      GOVDE="${GOVDE}---\n\n"
      CUM=$((CUM + k))
    done
    awk -v g="$GOVDE" -v ik="$(printf %02d $ILK_K)" -v sk="$(printf %02d $KNO)" \
        -v is="$(printf %02d $ILK_S)" -v ss="$(printf %02d $SNO)" '
      NR == 1 { sub(/\(S0 – S⬜\)|\(S⬜ – S⬜\)/, "(K" ik " – K" sk " · S" is " – S" ss ")"); print; next }
      /^---$/ && !kes { print "> ⭐ **22.09.2026 · ÇOK KLİPLİ SAHNE:** birim başlığı `## 🎬 KLİP n` · sahne başlığı tek `#` ile"
                        print "> `# 📍 SAHNE n — AD  (k klip · aralık)` · son kare zinciri YOK — her klip kendi IMAGE promptundan ·"
                        print "> sahnenin 2.+ klibi `CONTINUOUS ACTION:` taşır · kapı ㉜ (`COK_KLIPLI_SAHNE_KILAVUZU.md`)."
                        print; print ""; printf "%s", g; kes = 1; next }
      !kes { print }' "$BF" > "$BF.tmp" && mv "$BF.tmp" "$BF"
    B=$((B + 1))
  done
fi

# ── yer tutucular ──────────────────────────────────────────────────
find "$HEDEF" -name "*.md" -type f -exec sed -i '' \
     -e "s/<FILM_ADI>/$FILM/g" -e "s/<FILM>/$FILM/g" {} +

# ── ön plan geri yerine (yer tutucu sed'inden SONRA — sahip metnine dokunulmaz) ──
if [ "$ON_PLAN" -eq 1 ]; then
  mv "$ON_PLAN_GECICI/00_ON_PLAN" "$HEDEF/00_ANALIZ/00_ON_PLAN" && rm -rf "$ON_PLAN_GECICI"
  echo "📎 ÖN PLAN taşındı: $HEDEF/00_ANALIZ/00_ON_PLAN/"
fi

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
  BÖLÜM ÖNERİSİ:  $( [ -n "$PLAN_LISTE" ] && echo "çok klipli sahne — $N klip · $SAHNE_ADET sahne · plan: $PLAN_LISTE (bölüm dosyalarına damgalandı)" || echo "S0-S$((YARI - 1)) ($YARI) · S$YARI-S$((N - 1)) ($((N - YARI)))" )
                  ⛔ bölüm SINIRI da ardışık bir ÇİFTTİR (≥1 ölçek + ≥45°)
  ÇALIŞMA:        $CALISMA
  OKUMA ÇİZELGESİ: $CIZ  (yaşayan ders ≤ 40 + manifest — "—" meşru, ㉘)
  REJİM:          $REJIM

  ⛔ SIRA — atlanmaz:
     00_ANALIZ/00_HIKAYE_ONAYI.md      ⭐ ÖNCE: hikâye sahibe onaylatılır (ONAY tarihli) — ㉙
     00_ANALIZ/00_OKUMA_CIZELGESI.md   yaşayan dersler + çekirdek kılavuzlar + QA raporu
     00_ANALIZ/01_QA_DERS_HASADI.md    bu filme düşen kilitler (tavan 20 — ㉕)
     00_ANALIZ/02_KONSEPT_VE_RISK.md   konsept kapısı · risk · B5
     00_ANALIZ/03_SAHNE_SIRALAMASI.md  $N sahnenin sırası
     00_ANALIZ/04_UYARI_NOTLARI.md     ölçülmüş arızalara bağlı uyarılar
     00_ANALIZ/05_SAHNE_CALISMALARI/   ≤8 sahne: dosya başına · >8: tablo + 5 kilit sahne (㉚)
     → ANCAK SONRA ${FILM}_PLAN.md yazılır.

  ⛔ REFERANS PAKETİ: dosya klasörde \`⬜ BEKLİYOR\` durumunda.
     İSTEĞE BAĞLI (08.09.2026 · sahip kararı) — yazılmazsa PLAN'a
     tek satır gerekçe. Yazılırsa KAPI 0'dır: onaysız sayfanın
     varlığı geçtiği hiçbir sahne üretilmez.

  ⛔ COMMIT ATILMAZ — yalnız proje sahibi atar.
═══════════════════════════════════════════════════════
OZET
