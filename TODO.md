Oto plik który tworzy Henrich (ja, użytkownik).


+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.     
  - postFable Opus 
    - 2026-maj - poniższa paczka rozwiązań do:
      - zad 14 DONE
      - zad 19 DONE
        - wstaw też rysunek do treści, ale zrób go mniejszego na komputerach bo fable przesadził w poprzednich zadaniach



Prompt dla Opusa Zad 18, nie kasuj go:
Zrób w wszysskich twoich zadaniach tekst i katex sformatowanywa taki sposób jak u zadaniach fable
Zad 20 - Rozwiązanie interaktywne
- powiększ tyhc render prostych
- Spraw aby można było dojechać do 16 / 12 przesuwając te proste k i l
- zmień odcienie tych kolorów tak by można było je odróżnić.
- Zmień kolory prostych k, l oraz fragmentów n i m na zewnątrz tych równoległych na biały.
Inaczej mówiąc: kolorowe mają zostać tylko odcienki z oznaczoną długością, reszta biała

26.
- Punkt 2 -2 pokoloruj na biało
- Suwaki powinny być tym sammym kolorem z różnymi odcieniami co prosta k której równanie powinno być pod suwakami napisane w stylu 
"
k:   y = −1/3 x + 2  <- pokoloruj na odpowiednie odcienie fioletowego i biały

Prosta l przecina oś y-greków w punkcie: 

(0 , -4/3)  <- pokoloruj na niebiesko
"
33.2
Dorób piłeczkę na 0, 0 i przycisk do wystrzelenia jej



ARCHIWUM PROMPTÓW:

  Fable pracowało nad wybranymi zadaniami 1-13 i zrobiło nich:
    - Interaktywne rozwiązanie (widżet)
    - Zwykłe rozwiązanie
    - Podpowiedź

  Sprawdź jakie wskazówki zostawiło po sobie Fable. Zrób podobny do powyższego zestaw dla poniższego zadania. Wzoruj się na poprzednich. Korzystaj również z transktyptów oraz plików (w potrzebie zobaczenia grafiki) arkusz.pdf odpowiedzi.pdf tablica-wzorow.pdf itd.  
  
  Zad 19 - Rozwiązanie interaktywen:
  Możesz wzorować się na: 2024-grudzien zad 20
  Najważniejsze aby można było przesuwać punkt D.
  Dodatkowo opcjonalnie jak pójdzie głądko powyższe i będize działać na tip top to zrób przesuwanie punktu B. Oba mają się przesuwać tylko w obrębie łuku na który się znajdują. Punkt B może wejść w miejsce punkt A lub C, byle żeby dało się go z tamtąd wyciągnąć.
  
  Zadaj pytania doprecyzowujące i ruszaj do autonomiicznej pracki.
  PS: Zdaje mi się, że Fable pracował nad tym zadaniem, może nie odkończył i zostawił. sprawdź szybko przed zadaniem pytań. Potem dokładniej.



  

  Zad 14. - Rozwiązanie interaktywne:
  Stwórz układ współrzędnych z wydocznymi wykresami funkcji f i g (2 parabole). Powinien istnieć suwak zmieniający wartość domyślnie ustawioną na 1 w f(x+1) tak aby parabola g się przesuwała prawo-lewo (odwrotnie niż suwak zwiększa wartość w prawą). Zrób takiego css aby przy liczba suwak był bardziej na sztywno a nie zależny od np. napisu po lewej, bo podczas przesuwania suwaka i zmiany ilość znaków napisie suwak skacze lewa-prawa.
  Gdy dopracujesz doobrze powyższe to zrób dodatkowo, opcjonalnie: 
  Możliwość złapania za wykres funkcji i przesunięcia go, co daje ten sam efekt co przesunięcie suwaka w drugą stronę.



<br>


+ NIE REALIZUJ, CZEKAJĄ W KOLEJCE:

  - Rozwiązanie krok po kroku:
    
    - Kroki mają za długie „czekania" na początku i na końcu filmu (wait() w Manimie) — wyciąć.
      Małe waity w środku kroku, między pojedynczymi animacjami, są okej. Najmocniej widać w zad. 1.

    - Zad. 1, kropki kroków: przy większej liczbie kroków niż mieści pasek ma być można
      przewijać (dziś sprawdzone tylko dla dziesięciu, które mieszczą się bez przewijania)
      - kropki są na granicy wygody dla kciuka na telefonie — rozważyć lekkie powiększenie
        (w v31 zrobione tylko marginesy boczne, rozmiar bez zmian)

  
  - usunąć całkowicie „solutionTextMore" z wszystkich exercises.json i z template.html/JS
    (sprawdzone 2026-08-15: to NIE jest martwy kod. app/render.js nadal go renderuje,
    przycisk „pokaż więcej" działa, a niepustą treść ma jeszcze 10 zadań w 2024-grudniu.
    Usunięcie oznacza więc świadome skasowanie działającej funkcji plus przepisanie
    tych 10 rozwiązań, a nie samo sprzątanie)

  - to samo do decyzji z „finalAnswer.label": renderer je ignoruje (świadomie, od 2026-08-06),
    a pole nadal siedzi w danych wszystkich arkuszy


<br>


+ TESTOWANIE HENRICH
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI.
<br> Mój telefon na chrome ma "okno": 485x945 

  - poprawki po Twoich uwagach do zad. 20, 26 i 33.2 (v57)

    - zad. 20: rysunek większy, a proste k, l, m i n są teraz szare; kolorowe zostały tylko cztery odcinki z wypisaną długością

    - zad. 20: odcinki przy prostej k mają dwa odcienie błękitu, przy l dwa odcienie żółci; sprawdź, czy da się je rozróżnić także w ciemnym motywie

    - zad. 20: przeciągnij k do końca w lewo (ma dojść do 16) i l do końca w prawo (do 12)

    - zad. 26: punkt (2, -2) jest czarny, oba suwaki fioletowe w dwóch odcieniach, a pod nimi stoi równanie prostej k w tych samych barwach

    - zad. 26: wynik dla prostej l jest niebieski, pod zdaniem „Prosta l przecina oś y-greków w punkcie:"

    - zad. 33.2: kliknij „wystrzel piłeczkę"; ma lecieć po torze dokładnie tyle sekund, ile mówi zadanie, z licznikiem czasu przy niej

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


<br>


+ DLA HENRICHA:

  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable


<br>


+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - sprawdzić devcontainer na Kubuntu/Dockerze — testowany był tylko pod rootless podmanem na Bazzite (opis środowiska: .devcontainer/README.md)


<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:

  - Treść w 2026-maj
    - treść zadań ✅
    - Zmiejszyć na komputerach (nie zmiejszać rozdzielczości bo będą nieostre) screenshoty grafik
    - uzupełnić screenshoty grafik
    - Rozwiązania
      - Krok po kroku - jeszcze nie ruszone
      - Zwykłe tylko w wybranych z zad 1-13 są zrobione, w reszcie trzeba zrobić
      - Interaktywne
        - W wybranych z zad 1-19 są ✅
        - W wybranych z zad 20-33
          - Zad 20 - możliwość przesuwania k i l lewa-prawa. Pozostają na sztywno pod tym samym kątem i równoległe do siebie
          - Zad 26 - Układ współrzędnych i na nim opisan sytuacja. Punkt (2, -2) na sztywno trzyma prostą l. Proste l podąża nachyleniem tak że jest zawsze równoległa do k. Suwaki:
            - prosta k: współczynnik a, domyślnie -1/3
            - prosta k: współczynnik b, domyślnie +2
          - Zad 27 i 28 czeka aż będzie mi się chciało przekminić 3D
          - Zad 33.1 - Zapisz w Rozwiązaniu zwykłym, że rozwiązanie interaktywne na oba można znależć pod 32.2 
          - Zad 33.2 - Układ współrzędnych z parabolą przyczepioną do (0, 0). Suwak zmieniający b domyślnie równe 14,7 zakres: <0; 29,4> co 2,45 Tylko zrób aby nie skakał.

        

  - Fable:
    - matura/2024-grudzień
      - Rozwiązania interaktywny
        - Wybrane zadania z zakresu 1-13 zrobione (dodatkowo mają też Podpowiedzi i Rozwiązanie zwykłe)
        - Wybrane zadania z zakresu 14-33 do zrobienia przez Opusa na podstawie spuścizny Fable

    - Interaktywne rozwiązania matury 2026
    - Lista checkboxów "Sprawdzanie rozwiązania"
    - Weryfikacja poprawności matematycznej
    - Usprawnienie struntury projektu
    - Analiza kosztów długoterminowych - Symulacja: co się stanie przy 1k, 10k, 100k użytkowników na danym stacku (koszty, limity, throttling)
    - Punkty krytyczne (failure points)
    
    

  + Zweryfikować poprawność matematyczną 2024-grudzien:
    - Błędy w filmach — ZOSTAŁO (zad. 3, 5 i 6 poprawione w v30):
      - Zad 4. wygląda wzorowo, ale łamie zasadę ciągłości klatek: zielona szóstka zostaje
        na ostatniej klatce kroku 2, a krok 3 startuje czarny (SSIM 0,9990)
      - Zad 2, 7, 8 i 9 były robione tą samą metodą co 5 i 6, więc trzeba przejrzeć ich
        animacje; tools/styk-klatek.sh pokazuje, w których krokach nie zgadzają się styki
      - Zad 3 krok 6 kończy się szarym nawiasem domykającym; reszta przyciemnień już się
        rozjaśnia na końcu kroku

    - Zadanie 2 — do sprawdzenia merytoryka kroków: krok 1 i 6 (wykładnik -1, potem 5,
    wynik \(5^4\)). issues/krok-po-kroku-v20-testy.md
    Punkt o za wąskich marginesach podpisu pod filmem odpadł sam: w v20 podpisu już nie ma,
    opis kroku siedzi w rozwijanym ROW 3. Zmierzone na telefonie 390 px — treść zadania ma
    24 px marginesu, film i ROW 3 po 25 px, czyli równo. Zostaje do przeklikania na żywo.

    - Zad 9 -> Sprawdzanie obliczeń -> Pierwszy checkbox

    - Poprawić 2024-grudzien: Rozwiązania krok po kroku (zad. 1–9, komplet po v27) i ich opisy pod filmem:

      - opisy pod filmami (v29, 51 sztuk, wg zasad z manimations/README.md): krótkie linijki,
        wzory w osobnych wierszach, bez wstępów typu „zaczynamy od…”, bez myślników/podkreśleń
        poza wzorami — sprawdzić brzmienie i czy nic nie ucieka poza ekran na telefonie

      - zad. 1
        - Rozwiązanie krok po kroku:
          - krok 2 — Twój przykład, na nim wzorowana reszta opisów (v29), przeczytać najpierw

      - zad. 3
        - Rozwiązanie krok po kroku:
          - kroki 2, 4 i 6 — przyciemniona część zapisu ma się rozjaśniać PRZED końcem kroku (v30)

      - zad. 5
        - Rozwiązanie krok po kroku (przerobiona od zera w v30):
          - krok z pierwiastkowaniem — sprawdzić wyjaśnienie, dlaczego bierzemy tylko wartość dodatnią
          - 60 000 ma zjechać POD kreskę ułamka, a \((1+p)^2\) przesuwa się w lewo (nie znika/pojawia)
          - całość (razem z zad. 6) — czy ruch znaków zgadza się z rachunkiem; kolor tylko na tym,
            co się faktycznie zmienia, gaśnie przed końcem filmu

      - zad. 6
        - Rozwiązanie krok po kroku (przerobiona od zera w v30):
          - teraz SIEDEM kroków zamiast sześciu (skracanie rozbite na dwa: najpierw \((x+1)\),
            potem \(x\) z \(x^2\)) — czy tak jest lepiej, czy wrócić do sześciu
          - krok 4 — skracane \((x+1)\) przekreślane na czerwono, jak na kartce, dopiero potem znikają

      - zad. 7
        - Rozwiązanie krok po kroku:
          - oba równania układu jadą jedno pod drugim przez cały film — sprawdzić, czy klamra
            z dwoma równaniami nie jest za mała na telefonie

      - zad. 9
        - Rozwiązanie krok po kroku:
          - film robi sam rachunek, NIE rysuje paraboli (widżet niżej już ją pokazuje interaktywnie)
            — czy to dobry podział, czy parabola ma być też w filmie


  + ULEPSZANIE WORKFLOW
    - Schedule adversarial review lub /code-review
    - wyłączyć skróty które powodują, że przeklikuje pytanie podczas pisania prompta
    - stworzyć własne skille pod ten projekt (np. wpinanie nowego arkusza, weryfikacja
      formulasPage) — gotowe pluginy są już wpięte

  + UI

    - Zmiejsz szerokość przycisków P i F (Prawda i Fałsz) na komputerach

    - "Wskaźniki" (oceń się):
      - Przycisk "Wskaźniki" powinien się nazywać "Wskaźniki zad. do oceny" lub coś w tym stylu, samo wskaźniki mało mówi. 
      - Póki co niech będą defaultowo wyłączone
      - Zmień ich styl na bardziej spójny z resztą np czarne/szare kółka lub żółte cyfry. Obecnie wyglądają zbyt nachalnie.
      - na telefonie powinny być:
        - ALBO: niewidzialne, wtedy opcja w menu powinna być szara z wybranym
        - ALBO: widoczne przyklejone do prawej strony z lekkim marginesem. powinny też być odpowiednio małe aby nie zasłaniały treści.

    - Przycisk "Rozwiązanie" w przypadku wielu rozwiązań powinien nazywać się "Rozwiązania" i mieć możliwość również rozwinięcia listy różnych rozwiązań: Zwykłe, Krok po kroku, Interaktywne
    Każdy z tych elementów byłby przyciskiem. 
    - Domyślnie: gdy istnieje rozwiązanie "krok po kroku" to "zwykłe" powinno być zwinięte i vice versa
    - Możliwość zmiany powyższego w ustawieniach: "Widoczność zwykłego rozwiązania: gdy brakuje krok po kroku, zawsze, nigdy

    - Funkcjonalność otwierania tablicy wzorów w nowej karcie oraz Dodać przełącznik "miejsce otwarcia: nowa karta / wew. okienko" pod "Otwórz tablice wzorów"

    - Czy zmiena wielkości okienka PDF w każdym rogu i krawędzi byłaby skomplikowana do implementacji

    - Strona na telefonie wygląda jakby była przybliżona (troche jakby na komputerze naklikać Ctrl + = albo Ctrl + ScrollUP) ale może to jest tylko u mnie.

    - Przekminić i postprzątać trzy rodzaje tekstu które dodają tylko bałaganu w rozwiązaniu.

    - Zad. 10/11 na telefonie: zdania i przyciski P/F
      - brakuje odstępu między kolejnymi zdaniami (1, 2, 3…). Zlewają się w jeden blok
      - są za bardzo przyklejone do lewej. Powinny się formatować jak reszta treści zadania.

    - Odwracanie kolorów grafik/wideo w dark mode (`--filtr-grafik-zadan`) działa nierówno między przeglądarkami:
      - Pixel 7a GrapheneOS:
        - Samsung Browser zmienia tło strony wedle własnego pomysłu, a odwracanie kolorów w ogóle nie działa. Świadomie odpuszczone: ta przeglądarka przemalowuje gotowy render, nasz CSS nie ma jak jej dosięgnąć
        - na reszcie przeglądarek działa dobrze
      - Windows 10: działa w pełni na wszystkich najpopularniejszych przeglądarkach
      - Bazzite:
        - ~~Chrome i Brave, brak matchu tła grafiki i tła strony~~ ZAMKNIĘTE 2026-08-16: to Bazzite/Wayland, nie strona. Na Windowsie wszystko gra, więc nie ma czego naprawiać w kodzie
        - Firefox jako jedyny nie zawraca odcienia po v49 (wygląda jak stary goły invert), choć Chrome na tej samej maszynie tak. Kolejność sprawdzania: numer wersji w rogu → about:support (czy rysuje karta graficzna) → profil koloru i HDR
      - rozpoznanie i warianty naprawy: issues/dark-mode-inwersja-przegladarki.md


  - "Pokaż potrzebne wzory" powinien mieć możliwośc wyboru wielu podpunktów?, kropek?, a formulasPage w zadaniach powinien się zmienić na formulasPages (s na końcu). Powinno być wiele lokacji wzorów do przywołania pod jednym zadaniem. 
    - Zad 9. dopisać str 7 (wyróżnik Δ, obok już wpisanej str 8 ze wzorem na x1,x2)
    - Zad 11. dopisać str 16 (pole trójkąta [10.4])
    - Zad 17. dopisać str 18 (podzadania 17.1/17.2 mają już str 11)
    - Zad 19. dopisać str 20 (pole trapezu [10.17], obok już wpisanej str 17 z podobieństwem trójkątów)
    - Zad 24. dopisać str 27 (jest tam rysunek ostrosłupa, obok już wpisanej str 11 z tangensem)
    - Zad 30. dopisać str 26 (pole całkowite prostopadłościanu [12.2], obok już wpisanej str 8 z wierzchołkiem paraboli)


  - Przycisk "Zresetuj ustawienia" z popup-em do potwierdzenie. Podświetlajacy się na czerwono po najechaniu i widoczny na samym dole side-bar-a.
  
  - Wsparcie, donate-y itd.
    - W index.html dodać sekcję o autorze i link do Patronite
    - Na githubie w ustawieniach repo też można coś podpiąć chyba ale trzeba sprawdizć czy byłoby to fair.

  - wysyłanie całego localStorage przez użytkownika podczas zgłaszania błędu jest a bit scatchy też troche niebezpiczne

<br>


+ DOPISANE PRZEZ CLAUDE-A
<br> Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI, ZAZWYCZAJ NA KOŃCU PUNKTU.

  + HENRICH MÓWI "MA TO SENS", STĄD MOŻE WESPNĄ SIĘ JESZCZE WYŻEJ:

    - FAZA 2.3 — gdy ruszy matematykazen.pl:

      - podmienić URL w LICENSE.md:2 („Required Notice" — tę linijkę kopiuje każdy
        redystrybutor) oraz w README.md; dziś oba wskazują na GitHub Pages

      - odkomentować wpis matematykazen.pl w CONTENT_DOMAINS w .devcontainer/init-firewall.sh
        (dziś domeny nie ma w DNS)

    - FAZA 3.
      - WKLEJ CO TAM PODPASUJE

    - INNE:

      - kryteria zadań 4-punktowych to kaskada progów z klucza CKE, więc uczeń, który zaznaczy
        sam „poprawny wynik", dostanie 1 pkt zamiast 4 — czy wyższy próg ma sam zaznaczać niższe?

      - tryb testowy zgłaszania błędów pod ?test-zgloszenie=1 (wzorem ?test-egzamin=1): zapis
        do konsoli zamiast wysyłki, żeby testy nie zjadały limitu 50 zgłoszeń na miesiąc

      - gdy zdecydujesz się upublicznić imię i nazwisko: podmienić pseudonim Henrich2137
        w LICENSE.md, CONTRIBUTING.md i stopkach html — CLA na pseudonim jest słabsze
        dowodowo (issues/licencja-i-cla.md)


  (poniżej modele dopisują nowe punkty, każdy pod własnym nagłówkiem z modelem i effortem)

  + FABLE 5 MEDIUM DOPISAŁ (2026-08-15, sugestie architektoniczne po zad. 2 w 2026-maj; oceny: oszczędność kontekstu / koszt wdrożenia / wpływ na ryzyko błędów, 1 zwiększa - 5 zmniejsza):

    - pole `numer` (numer CKE) wprost w każdym wpisie exercises.json: znika pułapka „numer zadania ≠ pozycja w tablicy", skrypty i modele nie muszą czytać `question`. Oszczędność 3, koszt 2, ryzyko 5

    - gotowy skrypt tools/test-widzetu.js (argumenty: arkusz i numer zadania; klika „Rozwiązanie", robi zrzut w obu motywach, liczy .katex-error): dziś każdy model pisze taki skrypt od zera. Oszczędność 4, koszt 2, ryzyko 4

    - krótka ściąga schematu exercises.json
    - (2026-08-15, po całej sesji) sugestie do współpracy:

      - najlepiej działały zamówienia widżetów z przykładowym stanem liczbami (jak Twój szkic do zad. 11: „50 + 150 = 200..."). Taki opis od razu ustawia układ i oszczędza rundę poprawek

      - uwagi z testów zbierane w paczkę (jak przy v43 i v48) są tańsze niż pojedynczo; drobiazgi dorzucane w trakcie tury też działają dobrze

      - kolejne widżety wg gotowego wzorca może robić Opus: przewodnik widgets/PROJEKTOWANIE.md + notatka issues/fable-przekazanie-2026-maj.md są pisane właśnie pod to; Fable zostaw na nowe wzorce i trudniejszą merytorykę

      - sekcja TESTOWANIE HENRICH urosła do siedmiu paczek; po przeklikaniu warto od razu przenosić wpisy do done/, żeby TODO nie puchło
 (lista pól, typy, jeden przykładowy wpis, bez prozy): brief słusznie odradza ARCHITECTURE.md, ale wtedy schemat trzeba wyczytywać z cudzych wpisów. Oszczędność 4, koszt 2, ryzyko 3 (trzeba pilnować synchronizacji ze stanem kodu)


  + OPUS 5 MEDIUM DOPISAŁ (2026-08-16, po zmianie filtru grafik na invert + hue-rotate):

    - do sprawdzenia przy okazji nowych scen Manima: czysty żółty i czysta zieleń są za jaskrawe i po odwróceniu blakną (żółty `#ffcc00` wychodzi brązowy). `python3 tools/odwroc-kolor.py` teraz o tym ostrzega


<br>


+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ (patrz done/README.md i CLAUDE.md)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DOPISANE PRZEZ CLAUDA, nie pisz tam dużo, technikalia należą do issues. Napisz jakim modelem jesteś i na jakim efforcie. Jeżeli czytasz notatki np. Sonneta Low to ufaj im mniej niż tym zrobionym przez Opusa na High

  - do sekcji TESTOWANIE HENRICH wpisuj tylko NAJWAŻNIEJSZE rzeczy, których jednocześnie nie da się przetestować podczas sesji Claude-a (np. w playwrigcht, chrome-devtools-mcp itd.)

  - Wpisy w sekcji TESTOWANIE HENRICH piszesz prostym zdaniem, małymi literami (normalna polska ortografia, wielka litera tylko tam gdzie gramatycznie należy — początek zdania, nazwy własne). Bez CAPS LOCKA dla podkreślenia słów. Domyślnie jedna linijka: co kliknąć → czego się spodziewać, np. „kliknij next-step w trakcie odtwarzania filmu — powinien przeskoczyć do początku następnego filmu".
    - Gdy jeden punkt obejmuje kilka rzeczy do sprawdzenia naraz, rozbij go: krótka linijka wiodąca, pod nią zagnieżdżone podpunkty, po jednej rzeczy na podpunkt. Drugi poziom zagnieżdżenia tylko wtedy, gdy szczegóły dotyczą jednego konkretnego podpunktu, np.:
      - sprawdź wygląd przycisków
        - po bokach zaokrąglone daszki
        - na środku jeden przycisk odtwórz/pauza/restart
          - bez kółka
          - restart (zakręcona strzałka) pokazuje się tylko po dobiegnięciu filmu do końca
        - nakładane ikonki pauzy/restartu na filmie mają zniknąć

    - Podobną strukturę podpunktów do powyższej stosuj w całym tym pliku.

    - Pustą linijkę zostawiaj pod każdym punktem, a w długich listach pełnych podpunktów także pod podpunktami — żeby się nie zlewały w blok. Po całej długiej liście zrób dwie linijki odstępu. W krótkiej liście paru jednolinijkowców w środku nie trzeba, a nakońcu wystarczy jedna linijka.

    - między sekcjami ma się znaleźć taka przerwa:  2 puste linijki, <br> i 2 puste linijki:
"


<br>


"

