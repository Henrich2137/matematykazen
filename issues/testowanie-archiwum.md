# Archiwum sekcji TESTOWANIE HENRICH (do v62)

Pełna lista wpisów testowych z TODO.md, taka jak wyglądała 2026-08-20, zanim
została skrócona do dwudziestu punktów. Powód skrócenia: sekcja urosła do
dwudziestu paczek z wersji od v33 do v62 i przestała być listą do przeklikania,
a Henrich w codziennym korzystaniu ze strony i tak natrafił na większość rzeczy,
które tu stoją.

**Co zostało w TODO.md:** dwadzieścia punktów, których NIE da się natrafić
przypadkiem: ciemny motyw, skrajne położenia suwaków, blokady przeciągania,
zachowanie przy słabym łączu i rzeczy widoczne tylko na telefonie.

**Co jest tutaj:** wszystko pozostałe, głównie sprawdziany typu „czy widżet
w ogóle wstaje" i „czy odczyt pokazuje to, co powinien" - rzeczy, które przy
zwykłym rozwiązywaniu zadania rzucają się w oczy same.

Jeśli kiedyś trzeba będzie przejść arkusz zadanie po zadaniu (np. przed
otwarciem na szerszą publiczność), ta lista jest gotowym scenariuszem.

---

+ TESTOWANIE HENRICH
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI.
<br> Mój telefon na chrome ma "okno": 485x945 

  - postoje na początku filmów krok po kroku (v62)

    - zad. 1 krok 9, zad. 2 krok 6 i zad. 3 krok 5 są o sekundę krótsze, bo film rusza od razu zamiast stać nieruchomo na wejściu; sprawdź, czy nie ruszają teraz za szybko

    - przejdź te trzy kroki tam i z powrotem strzałkami: obraz na styku kroków ma być ten sam, bez przeskoku

    - w pozostałych krokach czekania nie ruszałem, bo siedzą w środku kroku albo są animacją gaszenia koloru; powiedz, czy któryś z nich nadal się dłuży
    WYGLĄDA DOBRZE
  - przyciski arkuszy na stronie głównej (v61)

    - oba przyciski mają teraz jednakową szerokość 520 px i napisy „Rozwiąż arkusz CKE, maj 2026" oraz „Rozwiąż arkusz próbny CKE, grudzień 2024" - powiedz, czy te napisy są dla Ciebie ok, bo to moja propozycja, nie Twoje polecenie

    - na telefonie przycisk ma się zwęzić do szerokości ekranu; sprawdź, czy drugi napis mieści się w jednej linijce (na Twoim oknie 485 px mieści się, na wąskim 360 px łamie się po przecinku i tak ma być)

    - puste akapity między przyciskami zniknęły, odstęp robi teraz margines - sprawdź, czy przyciski nie są za ciasno albo za luźno

  - koniec „pokaż więcej" i nowa kolejność rozwiązań (v60)

    - rozwiń „Rozwiązanie" w dowolnym zadaniu z filmem (2024-grudzień zad. 1, 2, 3) - najpierw ma być film krok po kroku, dopiero pod nim tekst rozwiązania, a na końcu widżet

    - przycisku „Pokaż więcej" nie ma już nigdzie w rozwiązaniach - jeśli gdzieś wyskoczy, coś zostało

    - w ośmiu zadaniach 2024-grudnia w tekście rozwiązania siedzi nagłówek „DAWNE POKAŻ WIĘCEJ" i pod nim doklejona dawna treść (zad. 3, 4, 6, 7, 8, 10, 19, 30) - to jest tymczasowe i celowo brzydkie, żeby było widać, gdzie trzeba zredagować tekst w jedną całość; powiedz, czy scalać to samemu, czy zostawiasz to sobie

    - zad. 1 i 2 tego arkusza nie miały wcześniej tekstu rozwiązania, więc dawna treść „pokaż więcej" weszła tam wprost, bez nagłówka - sprawdź, czy czyta się sensownie od pierwszego zdania

    - sprawdź, czy pod ostatnim blokiem rozwiązania nie ma zawieszonej poziomej kreski (osobno w zadaniu z samym tekstem, z samym widżetem i z filmem plus tekstem)

  - rozdział licencyjny widgets/ (v59) - zmieniły się ścieżki dwóch skryptów, więc trzeba sprawdzić, czy widżety w ogóle wstają

    - otwórz dowolny arkusz i rozwiń „Rozwiązanie" w zadaniu z widżetem (2024-grudzień zad. 1, 5 i 9) - widżet ma się narysować i reagować na przeciąganie

    - to samo na telefonie: pliki `widgets/_helpers.js` i `widgets/_registry.js` nazywają się teraz `app/widget-helpers.js` i `app/widget-registry.js`, więc znikła stara pułapka z podkreślnikiem na GitHub Pages; jeśli na telefonie widżety działają, ta pułapka jest zamknięta na dobre

  - poprawki po Twoich uwagach do zad. 20, 26 i 33.2 (v57)

    - zad. 20: rysunek większy, a proste k, l, m i n są teraz szare; kolorowe zostały tylko cztery odcinki z wypisaną długością

    - zad. 20: odcinki przy prostej k mają dwa odcienie błękitu, przy l dwa odcienie żółci; sprawdź, czy da się je rozróżnić także w ciemnym motywie

    - zad. 20: przeciągnij k do końca w lewo (ma dojść do 16) i l do końca w prawo (do 12)

    - zad. 26: punkt (2, -2) jest czarny, oba suwaki fioletowe w dwóch odcieniach, a pod nimi stoi równanie prostej k w tych samych barwach

    - zad. 26: wynik dla prostej l jest niebieski, pod zdaniem „Prosta l przecina oś y-greków w punkcie:"

    - zad. 33.2 (v58): pociskiem jest teraz biało-czarna piłka nożna, przycisk „Wystrzel piłeczkę" stoi w ramce po lewej od suwaka, a licznik czasu pod nim

    - zad. 33.2: kliknij przycisk; piłka ma lecieć po torze dokładnie tyle sekund, ile mówi zadanie (przy 14,7 to 3 s), a napis na przycisku zmienia się na „Leci…" bez skakania układu

    - zad. 33.2: w trakcie lotu przycisk jest zablokowany, a ruszenie suwaka sprowadza piłeczkę na ziemię

    - rozwiązania opisowe wszystkich moich zadań (14, 19, 20, 26, 33.1, 33.2) mają teraz krótkie wprowadzenie do wzoru i jednostki poza wzorem, jak u Fable

  - zadania 20, 26, 33.1 i 33.2 w arkuszu 2026-maj: nowy komplet podpowiedź + rozwiązanie + widżet (v56)

    - zad. 20: przesuwaj prostą k, potem l; wszystkie cztery długości mają się zmieniać, ale oba ułamki w odczycie zostają równe

    - zad. 20: sprawdź, czy da się chwycić każdą prostą osobno i czy żadna nie przechodzi przez punkt O

    - zad. 26: rusz suwakiem b i popatrz, że wynik ani drgnie, a rusza się tylko fioletowa prosta k

    - zad. 26: rusz suwakiem a i sprawdź, czy przy -1/3 zapala się ptaszek, a wynik pokazuje się ułamkiem -4/3, nie liczbą 0,33

    - zad. 33.1: to jedyne z tej paczki bez widżetu; w rozwiązaniu ma być zdanie odsyłające do wykresu pod zad. 33.2

    - zad. 33.2: przesuń suwak na sam koniec i na sam początek; przy zerze ma się pojawić zdanie, że piłeczka nie została wyrzucona

    - zad. 33.2: to jedyny wykres w projekcie z różnymi jednostkami na osiach (sekundy i metry), więc kratka NIE jest kwadratowa; oceń, czy tak jest czytelnie

  - zad. 19 w arkuszu 2026-maj: nowy komplet podpowiedź + rozwiązanie + widżet (v52, odczyt i podpisy poprawione w v54)

    - odczyt pod rysunkiem to teraz jedna linijka \(50° · 2 = 100° = 70° + 30°\), a wszystkie cztery liczby mają iść za punktami przy przeciąganiu

    - obie miary kątów przy środku (70° i 30°) siedzą po zewnętrznej stronie swoich łuków

    - przeciągnij punkt D po dużym łuku: kąt przy nim ma cały czas pokazywać 50°, nawet gdy D dojedzie do końca łuku

    - spróbuj wciągnąć D na dolny łuk, między A i C: ma się tam nie dać wejść, punkt zatrzymuje się kawałek przed A albo C

    - przeciągnij punkt B: kąty przy środku mają się zmieniać, ale ich suma zostaje 100°, a przy 30° zapala się zielony ptaszek

    - dociągnij B aż do A i sprawdź, czy da się go stamtąd wyciągnąć z powrotem; to samo od strony C

    - na telefonie: czy da się trafić palcem w D i w B, gdy stoją blisko siebie

  - poprawki zad. 14 po Twoich uwagach (v52)

    - rozwiązanie zwykłe ma teraz więcej krótkich linijek i przerwy między krokami

    - karta „przesunięcie": strzałka siedzi pod wierzchołkami, a pod nią jest sama liczba, bez dopisku o kierunku

    - karta „rozwarcie": suwak chodzi od −2 do 2, więc parabola potrafi się odwrócić ramionami w dół; przy skrajnych wartościach zamiast kropki na osi y pojawia się trójkącik, bo wartość ucieka poza rysunek

  - rysunki z arkusza w treściach zadań (v52)

    - zadania 18, 19, 20, 21 i 31 w maju mają teraz rysunki; wcześniej w 19, 20 i 31 był połamany obrazek, a w 18 i 21 nie było go wcale

    - rysunki są mniejsze (limit 380 px, v53): zerknij na zad. 12 i 13, czy teraz wyglądają lepiej

    - na telefonie ten sam limit 380 px zmniejszył rysunki bardziej niż w v52; sprawdź, czy nie są już za małe pod palcem

    - zad. 31 ma wyjątek (v55): dwa diagramy klas stoją obok siebie na komputerze, a na telefonie jeden pod drugim, każdy na całą szerokość karty

  - zad. 14 w arkuszu 2026-maj: nowy komplet podpowiedź + rozwiązanie + widżet (v51)

    - otwórz rozwiązanie zad. 14 i na zakładce „przesunięcie" pociągnij suwak w obie strony: parabola g ma jechać w lewo przy plusie, a w prawo przy minusie

    - złap palcem samą parabolę g i przeciągnij ją w bok: suwak ma jechać razem z nią, a wykres nie powinien przeskakiwać pod palec

    - przeciągnij powoli po pustym miejscu płótna, z dala od krzywych: nic nie powinno się ruszyć

    - przełącz na zakładkę „rozwarcie" i szukaj a, przy którym g trafia w pomarańczowy pierścień: przy 0,5 ma zapalić się zielony ptaszek

    - na tej samej zakładce chwyć ramię paraboli i pociągnij w górę i w dół: rozwarcie ma zmieniać się płynnie, a wartość nie uciekać do końca suwaka

    - przełączaj zakładki tam i z powrotem: rysunek nie powinien podskakiwać w pionie

  - suwaki we wszystkich widżetach przestały skakać w bok (v51, zmiana wspólnego CSS)

    - zad. 13.1 w maju: rusz suwakiem a przez wartości ujemne i dodatnie, suwak ma stać w miejscu, a zmieniać się ma tylko napis po lewej

    - na telefonie sprawdź, czy suwak mieści się w karcie i nie wychodzi poza jej prawą krawędź: zad. 2, 11 i 13 w maju oraz zad. 5, 15 i 30 w grudniu

  - kolory rysunków i filmów w ciemnym motywie (v49)

    - włącz ciemny motyw i otwórz zad. 10 w arkuszu 2024-grudzień: wykres powinien być fioletowy, a nie zielony jak dotąd

    - w tym samym motywie odpal rozwiązanie krok po kroku zad. 2 (2024-grudzień): zielone piątki mają być zielone, wcześniej wychodziły różowe

    - obejrzyj kilka zwykłych czarno-białych rysunków CKE: tam nie powinno się zmienić nic, także tło wokół rysunku ma dalej zlewać się ze stroną (żadnej czarnej ramki)

    - zerknij na telefonie, czy filmy nie zaczęły szarpać: filtr jest o jedno działanie dłuższy niż był

    - w ciemnym motywie `x` w widżetach jest teraz błękitny, a nie pomarańczowy (v50): otwórz zad. 8, 10, 12 lub 13 i sprawdź, czy przeciągany punkt, suwak i wzór mają tę samą barwę co niebieskie oznaczenia w filmie

  - poprawki widżetów maja po Twoich uwagach (v48)

    - 12.1 zdanie 2: prawa prosta dochodzi teraz do 5,5, lewa do −4; pomarańczowy punkt maksimum większy, kreska do osi y mocniejsza (pomarańczowa przerywana); „4" w odczycie też pomarańczowa

    - 12.2 zdanie 1: w tytule dopisane, że ten widok nie jest interaktywny

    - 12.2 zdanie 2: kropka z osi y usunięta, prostą ciągniesz w dowolnym miejscu płótna

    - suwaki i przeciąganie w widżetach wykresowych (zad. 8, 10, 12, 13) są płynne (krok 0,05 zamiast 0,25), z przyciąganiem do wartości z zadania; sprawdź, czy suwaki w 13.1 i 13.2 przestały dziwnie skakać

  - zad. 13 w 2026-maj: rysunek + widżety 13.1 i 13.2 (v47)

    - w treści zad. 13 rysunek prostej z kątem α wycięty z arkusza (media/zad13/zad13rys.png)

    - 13.1: dwa suwaki, a niebieski i b żółty; żółty punkt na osi y da się przeciągać (zmienia b)

      - przesuń a na plus: prosta rośnie, łuk kąta α maleje poniżej 90°, w odczycie „a > 0"

      - odczyt: wzór f(x) = ax + b z kolorami oraz znaki a i b (pod zdania P/F)

    - 13.2: suwak a; trójkąt przy kącie α jak w tablicach (s. 11, definicja dla dowolnego kąta)

      - przy a = −1,5: pionowa przyprostokątna „y = 3" (żółta), pozioma „x = −2" (niebieska, w lewo), odczyt tg α = y/x = 3/(−2) z ✓

      - minus ma wychodzić z ujemnego x, nie z y; komentarz pod odczytem tłumaczy znak

      - przesuń a na plus: trójkąt przeskakuje na prawą stronę, x > 0 i tangens dodatni

    - kratka we wszystkich wykresach zad. 12 i 13 ma być kwadratowa (poprawka po Twojej uwadze)

    - na telefonie: przeciąganie punktu b palcem w 13.1; motyw przełączony przy otwartych widżetach

    - pliki wspólne: template.html (tag script i wersja), widgets/_registry.js, widgets/_helpers.js (wgWysokoscKwadratowa), style/sheet.css (etykiety suwaków), widgets/README.md

  - zad. 12 w 2026-maj: rysunek + widżety 12.1 i 12.2 z zakładkami (v46)

    - w treści zad. 12 ma być wykres łamanej wycięty z arkusza CKE (nowy plik media/zad12/zad12rys.png); sprawdź, czy w ciemnym motywie odwraca kolory jak inne grafiki

    - 12.1, widżet z dwiema zakładkami „Zdanie 1." / „Zdanie 2."

      - zakładka 1: przeciągnij poziomą prostą; punkty przecięcia z wykresem i odczyt x = ...; przy y = 3 pojawia się ✓ i jedno rozwiązanie x = 1

      - zakładka 2: przeciągnij pionowe proste; pod nimi zapis przedziału, pomarańczowy punkt maksimum z kreską do osi y; przy [2, 3] ✓ i wartość 4

    - 12.2, widżet z dwiema zakładkami

      - zakładka 1 (bez sterowania): pas i zielony odcinek na osi y pokazują zbiór wartości [−2, 4]

      - zakładka 2: prosta y = c, sterowanie punktem na osi y albo suwakiem; zielony przedział na osi x z pustymi/pełnymi kółkami; przy c = 1 ✓ i (−1, 4)

      - podnieś c powyżej 3: prawy koniec przedziału ma się domknąć na 2 (pełne kółko), np. (1,5, 2⟩ dla c = 3,5

    - obie karty: przełączanie zakładek przy otwartym widżecie i zmiana motywu; na telefonie sprawdź przeciąganie prostych palcem

    - pliki wspólne: template.html (tag script i wersja), widgets/_registry.js, widgets/_helpers.js (nowe klocki wgZakladki/wgUklad/wgRysujUklad), style/sheet.css (style zakładek), widgets/README.md

  - zad. 11 w 2026-maj, widżet wg Twojego opisu (v45)

    - kliknij „Podpowiedź": oznaczenie niewiadomych i przepis na układ równań; oceń, czy nie zdradza

    - kliknij „Rozwiązanie": układ równań na starcie, podstawienie n = 200 − u, wynik u = 78

    - widżet: niski wykres (prosta, nie parabola, bo kwota po kosztach jest liniowa względem n) z zieloną przerywaną linią „zostało: 4 665 zł", suwak n w kolorze niewiadomej

      - przesuń suwak na 122: punkt trafia w zieloną linię, a pod spodem „6220 zł − 25% = 4665 zł" dostaje ✓

      - rachunek pod suwakiem ma stać w kolumnach (n pod n, u pod u, wyniki pod sobą) i nie skakać przy przewijaniu suwaka, sprawdź też na telefonie

      - przełącz motyw przy otwartym widżecie: przemalowanie od razu

    - pliki wspólne: template.html (tag script i wersja), widgets/_registry.js

  - zad. 10 w 2026-maj, trzecie (ostatnie) zadanie od Fable (v44)

    - kliknij „Podpowiedź": przepis na nierówność kwadratową; oceń, czy pomaga, a nie zdradza

    - kliknij „Rozwiązanie": wzory na starcie, przenoszenie na jedną stronę, delta, pierwiastki −4/3 i 2, przedziały na zewnątrz

    - widżet: parabola 3x² − 2x − 8 z zielonymi promieniami rozwiązań na zewnątrz pierwiastków, punkt ruszasz klikiem w oś lub przeciąganiem

      - przeciągnij punkt palcem na −4/3: podstawienie w odczycie przechodzi na ułamek −4/3 (nie −1,33) i pojawia się ✓

      - między pierwiastkami (np. x = 1) ma być ✗, na zewnątrz ✓

      - na telefonie: czy punkt da się złapać palcem

      - przełącz motyw przy otwartym widżecie: przemalowanie od razu

    - drobne z tej samej wersji (v44)

      - zad. 2: strzałki między słupkami skrócone, nie kleją się do rogów; w odczycie „suma odsetek: ..."

      - zad. 8: trzecia linijka rozwiązania po nowemu („Wystarczy, że któryś z nawiasów..."), tytuł widżetu z marginesem od separatora (wszystkie widżety, też w 2024-grudniu)

    - pliki wspólne: template.html (tag script i wersja), widgets/_registry.js, style/sheet.css (margines tytułu widżetu)

  - zad. 2 w 2026-maj po drugiej rundzie poprawek (v43)

    - podpowiedź: tylko wzór, bez zdania o odsetkach

    - suwak startuje na 6,0% i jest niebieski (kolor niewiadomej), w ciemnym motywie pomarańczowy; „p = 6,0%" w odczycie w tym samym kolorze

    - między słupkami strzałki z kwotami „+ 600 zł" / „+ 636 zł", przerywana linia bazowa na poziomie 10 000 zł

    - odczyt pod suwakiem: trzy linijki z oddechem (jak w zwykłym rozwiązaniu), ostatnia „odsetki: 600,00 zł + 636,00 zł = 1236,00 zł" zielenieje przy 6%

    - słupki i czcionka w nich trochę większe niż w v42

  - zad. 8 w 2026-maj, drugie zadanie od Fable (v43)

    - kliknij „Podpowiedź": pytanie o zerowanie nawiasów; oceń, czy pomaga, a nie zdradza

    - kliknij „Rozwiązanie": trzy kolumny (nawias nad swoim rozwiązaniem), pod nimi suma −3 + m − 2 = 0, na końcu m = 5 i odpowiedź C; sprawdź, czy kolumny mieszczą się na telefonie

    - widżet: oś liczbowa z punktami −3, −2 i m (wszystkie jednym fioletem), bez suwaka; x ruszasz klikając w oś lub przeciągając punkt

      - przeciągnij x palcem na −3, −2 albo m: w odczycie widać zerujący się nawias, obliczony iloczyn i „0 = 0" z ✓

      - poza rozwiązaniem ostatnia linijka to np. „−288 = 0" z ✗

      - na telefonie: czy punkt da się złapać palcem i czy da się trafić w −3 i −2 obok siebie

      - liczby pod osią zeszły niżej, kropka nie powinna ich zasłaniać (to samo w zad. 1 i 9 w 2024-grudniu)

      - przełącz motyw przy otwartym widżecie: przemalowanie od razu

    - zmienione pliki wspólne dla wszystkich arkuszy: template.html (tag script i wersja), widgets/_registry.js, style/sheet.css (większy odczyt pod każdym widżetem), widgets/osLiczbowa.js i widgets/nierownoscKwadratowa.js (liczby pod osią niżej); przeklikaj dla pewności zad. 1, 5 i 9 w 2024-grudniu

  - zad. 5 w 2024-grudzień po przeróbce (v40)

    - suwak ma być fioletowy, nie systemowy niebieski (dotyczy też suwaków w zad. 10, 15 i 30)

    - linia celu ma być zielona przerywana, była czerwona

    - ustaw suwak na 6,4 procent: „p = 6,4%" w odczycie ma zzielenieć, a pod spodem NIE ma dochodzić druga linijka

    - rozwiązanie opisowe ma być linijka po linijce, wzór tylko na starcie; przycisk „pokaż więcej" ma zniknąć

    - linijki pod wzorem mają stać wyśrodkowane, w jednej kolumnie pod nim; tak samo w zad. 9

  - zad. 9 w 2024-grudzień, rozwiązanie opisowe (v40)

    - to samo co w zad. 5: linijka po linijce, wzory na starcie, bez „pokaż więcej"

  - widżet zad. 9 w 2024-grudzień po przeróbce na wzorzec dla Fable (v36)

    - kliknij w puste miejsce na osi, nie w sam punkt — punkt ma tam skoczyć (na komputerze działa, na telefonie nie sprawdzone)

    - przeciągnij punkt palcem — sprawdź, czy da się w niego trafić i czy nie ucieka poza ekran

    - punkt na osi ma trzymać kolor podstawiania niezależnie od tego, czy nierówność wychodzi; o wyniku mówi dopiero ✓ albo ✗ w drugiej linijce pod spodem

    - w drugiej linijce kolorowe mają być tylko liczby, które weszły na miejsce x — nawiasy, „− 6" i „≤ 7" zostają czarne

    - przełącz motyw przy otwartym widżecie — kolory mają się przemalować od razu, bez odświeżania strony

    - kolor podstawiania jest inny w każdym motywie: w jasnym niebieski, w ciemnym pomarańczowy — sprawdź, czy oba są dobrze widoczne

  - pluginy Claude Code po ponownej instalacji (2026-08-15)

    - żeby plugin `github` zaczął działać, zaloguj `gh` w kontenerze: wpisz `! gh auth login` — bez tego wtyczka zwraca HTTP 400

    - loguj się PRZED restartem sesji Claude Code, nie po — zmienna z tokenem czytana jest tylko przy starcie

    - po restarcie sprawdź `claude mcp list` — `github` i `chrome-devtools` mają być „✔ Connected"

    - w nowej sesji sprawdź `/skills` — ma być widoczny `frontend-design` i sześć skilli `chrome-devtools`


  - zadanie startowe VS Code robi teraz fetch zamiast pulla

    - otwórz repo w kontenerze i sprawdź w Source Control, czy pojawia się licznik „↓N" — czyli fetch przy starcie zadziałał

    - repo ma się już nie „rozjeżdżać" samo: po otwarciu kontenera `git status` ma być czysty, bez wysypu zmian, których nie robiłeś

    - scalanie robisz teraz sam: gdy widzisz „↓N", klikasz pull (najlepiej na hoście)


  - wczytywanie kroków (v33)

    - wejdź w „Rozwiązanie" w zad. 1 i przeklikaj ► kilka razy — kadr nie ma już ani pulsować, ani przygasać

    - poczekaj na krok przy słabym zasięgu — na dole filmu mają się pokazać trzy kropki, dopiero po pół sekundy

    - spamuj ► i ◄ — kropki nie powinny migać przy każdym kliknięciu

    - wejdź w zadanie, odczekaj kilka sekund przed kliknięciem „Rozwiązanie", potem przeklikaj kroki —
      powinny wchodzić natychmiast, bez czekania na film


  - logo przy otwartym panelu bocznym (v34)

    - otwórz panel na telefonie — logo ma być przygaszone, jakby leżało pod przyciemnieniem

    - dotknij logo przy otwartym panelu — panel ma się zamknąć, strona główna ma się NIE otworzyć

    - strzałka obok logo ma dalej zamykać panel jednym dotknięciem

