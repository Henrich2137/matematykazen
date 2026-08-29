#!/usr/bin/env bash
# Wyciąga z filmów „krok po kroku" klatki jako obrazki, żeby model mógł je OBEJRZEĆ.
#
# PO CO TO JEST. Model nie widzi plików mp4 — dla niego to ciąg bajtów. Widzi
# natomiast obrazki PNG. Jedyna droga do obejrzenia animacji prowadzi więc przez
# zamianę wideo na klatki. To domyka punkt 25 z manimations/README.md („obejrzyj
# klatki okiem"), który dotąd nie miał żadnego narzędzia: tools/styk-klatek.sh i
# tools/zielen-krokow.py mówią, ŻE coś jest nie tak, ale nie pokazują, JAK to wygląda.
#
# CZEGO TO NIE DA. Na klatkach widać stany zatrzymane: czy rachunek w kroku jest
# dobry, czy coś nachodzi na siebie, gdzie jest zieleń, dokąd wędrują glify.
# Nie widać płynności ani tempa — to zostaje do obejrzenia człowiekowi.
#
# TRZY TRYBY:
#   film   — jeden krok jako sekwencja co N-tej klatki, sklejona w jedną kratkę.
#            Widać RUCH. Wzory tym mniejsze, im gęstsza sekwencja.
#   stany  — pierwsza i ostatnia klatka KAŻDEGO kroku w zadaniu, czytelnie.
#            Widać tok rozwiązania i wszystkie styki naraz.
#   styk   — jedna para (koniec kroku N / początek N+1) w pełnej rozdzielczości
#            plus podbita różnica. Do użycia, gdy styk-klatek.sh zgłosi zastrzeżenie:
#            liczba SSIM mówi, że różnica jest, ale nie mówi GDZIE.
#
# UŻYCIE:
#   tools/klatki.sh film  <katalog> <nr-kroku> [--co 6] [--tokeny 2000] [--z-bezruchem]
#   tools/klatki.sh stany <katalog> [--poczatek|--koniec] [--tokeny 2500] [--strona 2]
#   tools/klatki.sh styk  <katalog> <nr-kroku>
#
#   <katalog> to .../media/zadN/solution-step-by-step
#
# DWA POKRĘTŁA I DLACZEGO AKURAT TE:
#   --co N     co którą klatkę brać. Film ma 120 klatek na sekundę, więc --co 6
#              daje 20 klatek na sekundę (ruch widać w zupełności), --co 30 daje
#              cztery klatki na sekundę, czyli mało obrazków, ale każdy duży i czytelny.
#   --tokeny N ile kontekstu wolno na to wydać. Koszt obrazka zależy WYŁĄCZNIE od
#              jego powierzchni (mniej więcej piksele/750), nie od tego, ile klatek
#              jest w środku. Skrypt dobiera więc wielkość kafelka tak, żeby zmieścić
#              się w budżecie: im więcej klatek, tym każda mniejsza. Gdy przy
#              --min-szer nie da się zmieścić wszystkiego, dzieli wynik na strony.
#
# BEZRUCH JEST ODSIEWANY (tryb `film`). Każdy krok kończy się przytrzymaniem obrazu,
# a Manim przytrzymuje też w środku — na zad. 9, krok 3 z 72 przerzedzonych klatek
# 44 były tą samą klatką. Powtórzenia lecą więc do kosza (ffmpeg `mpdecimate`), bo
# kosztują tyle samo co klatki z ruchem i nic nie pokazują. `--z-bezruchem` je zostawia,
# gdy naprawdę trzeba zobaczyć, ile czegoś stoi w miejscu.
#
# ALE WYRZUCONY CZAS MUSI BYĆ WIDAĆ, inaczej kratka kłamie: dwa sąsiednie kafelki
# wyglądają jak ciąg ruchu, a naprawdę dzieli je pół sekundy postoju. Stąd DWA
# oznaczenia na każdym kafelku trybu `film`:
#   - żółty podpis w lewym górnym rogu — CZAS W FILMIE w milisekundach, nie numer po
#     kolei. Skok w tych liczbach sam z siebie zdradza, że coś wypadło.
#   - pomarańczowy pasek „bezruch +X.XXs" na dole — ląduje na kafelku, na którym obraz
#     STAJE, i mówi, jak długo stoi. To jego treść wisi przez ten czas na ekranie.
# Ta sama lista przerw idzie na konsolę. Bez tych oznaczeń nie da się odróżnić
# „dwa ruchy pod rząd" od „ruch, pauza, ruch".
#
# WYNIK ląduje w /tmp/klatki/<zadanie>/ (tak jak zrzuty z tools/zrzuty.js lądują
# w /tmp/zrzuty/) — poza repozytorium, żeby nie zaśmiecać gita. Skrypt wypisuje
# ścieżki powstałych plików; to je otwiera się potem Read-em.

set -uo pipefail

CZCIONKA=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
PIKSELE_NA_TOKEN=750   # przybliżenie: obrazek kosztuje mniej więcej powierzchnia/750
SZER_ZRODLA=1280       # nadpisywane odczytem z pliku

tryb=${1:-}
[ -n "$tryb" ] || { sed -n '2,45p' "$0" | sed 's/^# \?//'; exit 2; }
shift

katalog=""
krok=""
co=6
tokeny=""
min_szer=426
strona=1
ktore=oba
bezruch=pomin
wzmocnienie=25

while [ $# -gt 0 ]; do
    case "$1" in
        --co)          co=$2; shift 2 ;;
        --tokeny)      tokeny=$2; shift 2 ;;
        --min-szer)    min_szer=$2; shift 2 ;;
        --strona)      strona=$2; shift 2 ;;
        --poczatek)    ktore=poczatek; shift ;;
        --koniec)      ktore=koniec; shift ;;
        --z-bezruchem) bezruch=zostaw; shift ;;
        --wzmocnienie) wzmocnienie=$2; shift 2 ;;
        -*)         echo "Nieznany przełącznik: $1" >&2; exit 2 ;;
        *)          if [ -z "$katalog" ]; then katalog=$1; else krok=$1; fi; shift ;;
    esac
done

[ -d "$katalog" ] || { echo "brak katalogu: $katalog" >&2; exit 2; }

# Nazwa zadania do nazwy katalogu wyjściowego: .../media/zad9/solution-step-by-step -> zad9
nazwa=$(basename "$katalog")
[ "$nazwa" = "solution-step-by-step" ] && nazwa=$(basename "$(dirname "$katalog")")
WYJSCIE=${WYJSCIE:-/tmp/klatki/$nazwa}
mkdir -p "$WYJSCIE"

ROBOCZY=$(mktemp -d)
trap 'rm -rf "$ROBOCZY"' EXIT

plik_kroku() { echo "$katalog/step$1.mp4"; }

lista_krokow() {
    find "$katalog" -maxdepth 1 -name 'step*.mp4' ! -name '*reverse*' -printf '%f\n' \
        | sed 's/^step\([0-9]*\)\.mp4$/\1/' | sort -n
}

liczba_klatek() {
    ffprobe -v error -count_frames -select_streams v:0 \
        -show_entries stream=nb_read_frames -of csv=p=0 "$1" 2>/dev/null | tr -d '\r'
}

# Dobiera siatkę i wielkość kafelka pod zadany budżet tokenów.
# Wejście: $1 = ile klatek, $2 = budżet w tokenach, $3 = wymuszona liczba kolumn (0 = dobierz)
# Wyjście: zmienne KOL, WIE, TW, TH
uklad() {
    local n=$1 budzet=$2 wymus_kol=$3
    if [ "$wymus_kol" -gt 0 ]; then
        KOL=$wymus_kol
    else
        # Kafelek ma proporcje 16:9, więc kwadratowy arkusz wychodzi przy kol ≈ 0,75·√n.
        KOL=$(awk -v n="$n" 'BEGIN{k=int(0.75*sqrt(n)); if(k<1)k=1; if(k*k*16/9<n)k++; print k}')
    fi
    WIE=$(( (n + KOL - 1) / KOL ))
    local powierzchnia=$(( budzet * PIKSELE_NA_TOKEN ))
    # powierzchnia = KOL*WIE * TW² * 9/16  ->  TW = √(16·P / (9·KOL·WIE))
    TW=$(awk -v p="$powierzchnia" -v k="$KOL" -v w="$WIE" -v maks="$SZER_ZRODLA" \
        'BEGIN{t=sqrt(16*p/(9*k*w)); if(t>maks)t=maks; t=int(t/2)*2; if(t<80)t=80; print t}')
    TH=$(( (TW * 9 / 16 / 2) * 2 ))
}

case "$tryb" in

# ---------------------------------------------------------------- film -------
film)
    [ -n "$krok" ] || { echo "podaj numer kroku: tools/klatki.sh film <katalog> <nr>" >&2; exit 2; }
    plik=$(plik_kroku "$krok")
    [ -f "$plik" ] || { echo "brak pliku: $plik" >&2; exit 2; }
    : "${tokeny:=2000}"

    SZER_ZRODLA=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$plik")
    wszystkie=$(liczba_klatek "$plik")

    # Bezruch wycinamy DOMYŚLNIE. Każdy krok kończy się przytrzymaniem (self.wait),
    # więc bez tego połowa kratki to ta sama klatka w kółko — zapłacone i nic nie wnosi.
    # Zmierzone na zad. 9, krok 3: 72 klatki po przerzedzeniu, z czego 44 identyczne.
    if [ "$bezruch" = pomin ]; then odsiew="mpdecimate,"; else odsiew=""; fi

    # PRZEBIEG NA SUCHO. Potrzebne są z niego dwie rzeczy: ile klatek zostanie po
    # odsianiu (bo dopiero wtedy da się dobrać siatkę pod budżet) i KIEDY dokładnie
    # każda z nich siedzi w filmie. `showinfo` wypisuje `pts_time` każdej klatki,
    # która przeszła przez filtry; `mpdecimate` zachowuje oryginalne znaczniki czasu,
    # więc luka między kolejnymi wypisanymi czasami to dokładnie wyrzucony bezruch.
    mapfile -t czasy < <(ffmpeg -i "$plik" -fps_mode passthrough \
        -vf "select='not(mod(n\,$co))',${odsiew}showinfo" -f null - 2>&1 \
        | grep -o 'pts_time:[0-9.]*' | cut -d: -f2)

    wybrane=${#czasy[@]}
    [ "$wybrane" -gt 0 ] || { echo "nie udało się odczytać klatek z $plik" >&2; exit 1; }
    uklad "$wybrane" "$tokeny" 0

    # Odstęp między sąsiednimi klatkami PRZED odsianiem: co ile sekund powinny po sobie
    # następować, gdyby nic nie wypadło. Wszystko wyraźnie dłuższe to przerwa w ruchu.
    fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$plik" \
        | awk -F/ '{print ($2?$1/$2:$1)}')
    krok_czasu=$(awk -v c="$co" -v f="$fps" 'BEGIN{print c/f}')

    # Przerwy zbieramy do dwóch rzeczy naraz: do wypisania na konsoli i do znaczników
    # na samych kafelkach. Bez znacznika kratka kłamie — dwa sąsiednie kafelki wyglądają
    # jak ciąg ruchu, a naprawdę dzieli je pół sekundy bezruchu.
    przerwy=""
    filtry_przerw=""
    for ((i = 0; i < wybrane - 1; i++)); do
        luka=$(awk -v a="${czasy[i]}" -v b="${czasy[i+1]}" 'BEGIN{print b-a}')
        # Próg 2,5-krotności zwykłego odstępu: mniejsze wahania to zaokrąglenia
        # znaczników czasu, a nie postój.
        czy=$(awk -v l="$luka" -v k="$krok_czasu" 'BEGIN{print (l > 2.5*k) ? 1 : 0}')
        [ "$czy" = 1 ] || continue
        opis=$(awk -v l="$luka" 'BEGIN{printf "%.2f", l}')
        przerwy+=$(printf ' %ss(+%ss)' "${czasy[i]}" "$opis")
        # Znacznik ląduje na kafelku, na którym obraz STAJE, bo to jego treść wisi
        # przez tę chwilę na ekranie. eps = pół zwykłego odstępu, żeby trafić w jedną klatkę.
        eps=$(awk -v k="$krok_czasu" 'BEGIN{print k/2}')
        od=$(awk -v t="${czasy[i]}" -v e="$eps" 'BEGIN{print t-e}')
        do_=$(awk -v t="${czasy[i]}" -v e="$eps" 'BEGIN{print t+e}')
        filtry_przerw+=",drawtext=fontfile=$CZCIONKA:text='bezruch +${opis}s':x=4:y=h-th-4:fontsize=FS:fontcolor=white:box=1:boxcolor=0xc06000@0.85:boxborderw=2:enable='between(t\,$od\,$do_)'"
    done

    # Podpis kafelka to CZAS W FILMIE, nie numer po kolei. Przy odsianym bezruchu numer
    # po kolei nie mówi nic o tym, ile czasu minęło; czas mówi, i skok w czasie sam
    # zdradza postój nawet bez pomarańczowego znacznika.
    #
    # W milisekundach, bo `%{pts:flt}` wypisuje sześć miejsc po przecinku („0.200000"),
    # a drawtext nie ma formatu z zadaną liczbą miejsc dla ułamka.
    fs=$(awk -v t="$TW" 'BEGIN{f=int(t/22); if(f<9)f=9; if(f>28)f=28; print f}')
    filtry_przerw=${filtry_przerw//FS/$fs}
    # Wariant z bezruchem ma własną nazwę, żeby nie nadpisywał odsianego i żeby dało się
    # oba porównać obok siebie.
    wynik="$WYJSCIE/film-krok$krok-co$co$([ "$bezruch" = zostaw ] && echo -pelny).png"

    ffmpeg -v error -y -i "$plik" -fps_mode passthrough -vf \
      "select='not(mod(n\,$co))',${odsiew}scale=$TW:$TH,drawtext=fontfile=$CZCIONKA:text='%{eif\:t*1000\:d}ms':x=4:y=4:fontsize=$fs:fontcolor=yellow:box=1:boxcolor=black@0.6:boxborderw=2${filtry_przerw},tile=${KOL}x${WIE}:margin=4:padding=3:color=0x303030" \
      -frames:v 1 "$wynik" || exit 1

    echo "krok $krok: $wszystkie klatek w pliku, co $co daje $(( (wszystkie + co - 1) / co )), po odsianiu bezruchu $wybrane"
    echo "siatka ${KOL}x${WIE}, kafelek ${TW}x${TH} (źródło ${SZER_ZRODLA} szer.)"
    if [ -n "$przerwy" ]; then
        echo "wyrzucony bezruch (oznaczony na kafelkach):$przerwy"
    else
        echo "bez przerw w ruchu"
    fi
    echo "$wynik"
    ;;

# --------------------------------------------------------------- stany -------
stany)
    : "${tokeny:=2500}"
    mapfile -t kroki < <(lista_krokow)
    [ "${#kroki[@]}" -gt 0 ] || { echo "brak plików stepN.mp4 w $katalog" >&2; exit 2; }

    SZER_ZRODLA=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$(plik_kroku "${kroki[0]}")")

    # Ile klatek zmieści się na stronie przy zadanym minimum czytelności.
    na_strone=$(awk -v p="$((tokeny * PIKSELE_NA_TOKEN))" -v m="$min_szer" \
        'BEGIN{n=int(p/(m*m*9/16)); if(n<2)n=2; print n}')
    [ "$ktore" = oba ] && na_strone=$(( na_strone / 2 * 2 ))   # para na krok nie może się rozjechać

    # Wypis klatek do pobrania, z podpisem, który poleci na obrazek.
    opisy=()
    for k in "${kroki[@]}"; do
        [ "$ktore" != koniec ]   && opisy+=("$k:poczatek")
        [ "$ktore" != poczatek ] && opisy+=("$k:koniec")
    done

    ile=${#opisy[@]}
    stron=$(( (ile + na_strone - 1) / na_strone ))
    [ "$strona" -ge 1 ] && [ "$strona" -le "$stron" ] || { echo "strona poza zakresem (jest $stron)" >&2; exit 2; }

    od=$(( (strona - 1) * na_strone ))
    tej_strony=("${opisy[@]:$od:$na_strone}")

    if [ "$ktore" = oba ]; then uklad "${#tej_strony[@]}" "$tokeny" 2
    else uklad "${#tej_strony[@]}" "$tokeny" 0; fi

    # Podpis wpalamy przy wyciąganiu klatki, w pełnej rozdzielczości, bo w przebiegu
    # sklejającym wszystkie kafelki dostają ten sam filtr i nie da się ich rozróżnić.
    fs_zrodlo=$(awk -v t="$TW" -v s="$SZER_ZRODLA" 'BEGIN{f=int(16*s/t); if(f<14)f=14; print f}')
    i=0
    for opis in "${tej_strony[@]}"; do
        nr=${opis%%:*}; ktora=${opis##*:}
        plik=$(plik_kroku "$nr")
        i=$(( i + 1 ))
        cel=$(printf '%s/kl_%03d.png' "$ROBOCZY" "$i")
        # Koniec bierzemy z -sseof (od tyłu), tak jak w manimations/README.md przy
        # sprawdzaniu styku — ostatnia klatka to ta, która zostaje na ekranie.
        if [ "$ktora" = koniec ]; then przed=(-sseof -0.05); else przed=(); fi
        ffmpeg -v error -y "${przed[@]}" -i "$plik" -frames:v 1 -vf \
          "drawtext=fontfile=$CZCIONKA:text='krok $nr $ktora':x=10:y=10:fontsize=$fs_zrodlo:fontcolor=yellow:box=1:boxcolor=black@0.6:boxborderw=6" \
          "$cel" || exit 1
    done

    wynik="$WYJSCIE/stany-$ktore-str$strona.png"
    ffmpeg -v error -y -framerate 1 -i "$ROBOCZY/kl_%03d.png" -vf \
      "scale=$TW:$TH,tile=${KOL}x${WIE}:margin=4:padding=3:color=0x303030" \
      -frames:v 1 "$wynik" || exit 1

    echo "kroki: ${#kroki[@]}, klatek do pokazania: $ile, na stronę: $na_strone"
    echo "strona $strona z $stron, siatka ${KOL}x${WIE}, kafelek ${TW}x${TH}"
    if [ "$stron" -gt 1 ]; then
        reszta=$(seq 1 "$stron" | grep -vx "$strona" | tr '\n' ' ')
        echo "pozostałe strony: --strona ${reszta% }"
    fi
    echo "$wynik"
    ;;

# ---------------------------------------------------------------- styk -------
styk)
    [ -n "$krok" ] || { echo "podaj numer kroku: tools/klatki.sh styk <katalog> <nr>" >&2; exit 2; }
    nast=$(( krok + 1 ))
    a=$(plik_kroku "$krok"); b=$(plik_kroku "$nast")
    [ -f "$a" ] || { echo "brak pliku: $a" >&2; exit 2; }
    [ -f "$b" ] || { echo "brak pliku: $b (krok $krok jest ostatni?)" >&2; exit 2; }

    ffmpeg -v error -y -sseof -0.05 -i "$a" -frames:v 1 "$ROBOCZY/a.png" || exit 1
    ffmpeg -v error -y -i "$b" -frames:v 1 "$ROBOCZY/b.png" || exit 1

    para="$WYJSCIE/styk-$krok-$nast.png"
    roznica="$WYJSCIE/styk-$krok-$nast-roznica.png"

    ffmpeg -v error -y -i "$ROBOCZY/a.png" -i "$ROBOCZY/b.png" -filter_complex \
      "[0:v]drawtext=fontfile=$CZCIONKA:text='koniec kroku $krok':x=10:y=10:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6:boxborderw=6[l];
       [1:v]drawtext=fontfile=$CZCIONKA:text='poczatek kroku $nast':x=10:y=10:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6:boxborderw=6[p];
       [l][p]hstack=inputs=2" "$para" || exit 1

    # Różnicę trzeba podbić MOCNO. Przy SSIM rzędu 0,9999 gołe odjęcie daje obraz
    # nie do odróżnienia od czerni, a chodzi właśnie o to, żeby zobaczyć, GDZIE siedzi
    # (CLAUDE.md: „liczba nie mówi, GDZIE jest różnica"). `eq=contrast` tu nie
    # wystarcza — mnożenie przez `geq` owszem.
    ffmpeg -v error -y -i "$ROBOCZY/a.png" -i "$ROBOCZY/b.png" -filter_complex \
      "[0:v][1:v]blend=all_mode=difference,format=gray,geq=lum='min(255,lum(X,Y)*$wzmocnienie)'" \
      "$roznica" || exit 1

    # Bez tej liczby nie wiadomo, czy jasne miejsca na obrazku różnicy to realny
    # rozjazd, czy sam szum kodera podbity dwudziestopięciokrotnie.
    maks=$(ffmpeg -v error -i "$ROBOCZY/a.png" -i "$ROBOCZY/b.png" -lavfi \
        "[0:v][1:v]blend=all_mode=difference,format=gray,signalstats,metadata=print:key=lavfi.signalstats.YMAX:file=-" \
        -f null - 2>/dev/null | awk -F= '/YMAX/{print $2}' | head -1)
    # Bez -v error, bo filtr ssim wypisuje wynik dopiero na poziomie „info".
    ssim=$(ffmpeg -i "$ROBOCZY/a.png" -i "$ROBOCZY/b.png" \
        -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep -o 'All:[0-9.]*' | head -1)

    echo "styk $krok/$nast  ${ssim:-(ssim nieodczytane)}  najjaśniejszy piksel różnicy: ${maks:-?}/255"
    echo "  (kilka jednostek = szum kodera H.264; kilkadziesiąt = realny rozjazd)"
    echo "  różnica wzmocniona x$wzmocnienie"
    echo "$para"
    echo "$roznica"
    ;;

*)
    echo "nieznany tryb: $tryb (film | stany | styk)" >&2
    exit 2
    ;;
esac
