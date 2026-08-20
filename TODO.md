Oto plik który tworzy Henrich (ja, użytkownik).


+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.     
  
  - Nic



WZÓR PROMPTU DLA OPUSA POST-FABLE:

  Fable pracowało nad wybranymi zadaniami 1-13 i zrobiło  wnich:
    - Interaktywne rozwiązanie (widżet)
    - Zwykłe rozwiązanie
    - Podpowiedź

  Sprawdź jakie wskazówki zostawiło po sobie Fable. Zrób podobny do powyższego zestaw dla poniższego zadania. Wzoruj się na poprzednich. Korzystaj również z transktyptów oraz plików (w potrzebie zobaczenia grafiki) arkusz.pdf odpowiedzi.pdf tablica-wzorow.pdf itd.  
  
  Zadaj pytania doprecyzowujące i ruszaj do autonomiicznej pracy.


<br>


+ NIE REALIZUJ, CZEKAJĄ W KOLEJCE:

  - Rozwiązanie krok po kroku:
    - Zad. 1, kropki kroków: przy większej liczbie kroków niż mieści pasek ma być można
      przewijać (dziś sprawdzone tylko dla dziesięciu, które mieszczą się bez przewijania)
      - kropki są na granicy wygody dla kciuka na telefonie — rozważyć lekkie powiększenie
        (w v31 zrobione tylko marginesy boczne, rozmiar bez zmian)

  - to samo do decyzji z „finalAnswer.label": renderer je ignoruje (świadomie, od 2026-08-06),
    a pole nadal siedzi w danych wszystkich arkuszy

  - w ośmiu zadaniach grudnia (3, 4, 6, 7, 8, 10, 19, 30) w rozwiązaniu siedzi nagłówek „DAWNE POKAŻ WIĘCEJ" i doklejona pod nim dawna treść; celowo brzydkie, żeby było widać, gdzie zredagować tekst w jedną całość. Scalać samemu czy zostawiasz to sobie

<br>


+ TESTOWANIE HENRICH
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI.
<br> Mój telefon na chrome ma "okno": 485x945
<br> Próg wejścia jest wysoki, patrz ZASADY DLA CLAUDE-A niżej. Archiwum dawnych list: issues/testowanie-archiwum.md.

  - nic

<br>


+ DLA HENRICHA:

  - nic


<br>


+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - nic


<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:

  - Arkusz 2026-maj
    - treść zadań ✅
    - grafiki (wykresy, rysunki itd.) - chyba wszystkie, ale trzeba sprawdzić
    - odpowiedzi i poprawene odpowiedzi (dla zamkniętych) ✅
    - Sprawdzania rozwiązań - nie ruszone
    - Rozwiązania
      - Krok po kroku - jeszcze nie ruszone
        - gdy powstaną: niebieskie oznaczenia w filmie mają w ciemnym motywie wyjść
          w tej samej barwie co przeciągany punkt i suwak w widżecie (zad. 8, 10, 12, 13).
          W widżetach już się zgadza, film przechodzi przez filtr, więc sprawdź
          tools/odwroc-kolor.py przed renderem
      - Zwykłe - zrobione tylko w wybranych zadaniach, w reszcie trzeba zrobić
      - Interaktywne ✅ - zostają zad. 27 i 28 i czekają na przekminke o widżetach 3D


  - Arkusz 2024-grudzien:

    - Zad 9 -> Sprawdzanie obliczeń -> Pierwszy checkbox
      (sprawdzone 2026-08-20: trzy kryteria zgadzają się z kluczem CKE co do punktów,
      pierwsze jest za 0 pkt celowo, bo klucz daje punkt dopiero za pierwiastki.
      Napisz, co Ci w nim nie pasowało, bo w samym wpisie tego nie ma)
      PO CO JEST ZDANIE PIERWSZE SKORO NIE DAJE ONO PUNKTÓW?

    - Poprawić 2024-grudzien: Rozwiązania krok po kroku (zad. 1–9, komplet po v27) i ich opisy pod filmem:

      - opisy pod filmami (v29, 51 sztuk, wg zasad z manimations/README.md): krótkie linijki,
        wzory w osobnych wierszach, bez wstępów typu „zaczynamy od…”, bez myślników/podkreśleń
        poza wzorami — sprawdzić brzmienie i czy nic nie ucieka poza ekran na telefonie

      - zad. 1
        - Rozwiązanie krok po kroku:
          - krok 2 — Twój przykład, na nim wzorowana reszta opisów (v29), przeczytać najpierw

      - zad. 3
        - Rozwiązanie krok po kroku:
          - krok 6 — przyciemniona część zapisu ma się rozjaśniać PRZED końcem kroku;
            w krokach 2 i 4 już się rozjaśnia (sprawdzone 2026-08-20 stykami klatek), w 6 nie

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


- Co zadawać Fable:
    - Rozwiązania interaktywne
    - Lista checkboxów "Sprawdzanie rozwiązania"
    - Weryfikacja poprawności matematycznej
    - Usprawnienie struntury projektu
    - Analiza kosztów długoterminowych - Symulacja: co się stanie przy 1k, 10k, 100k użytkowników na danym stacku (koszty, limity, throttling)
    - Punkty krytyczne (failure points)

  + ULEPSZANIE WORKFLOW
    - Schedule adversarial review lub /code-review
    - wyłączyć skróty które powodują, że przeklikuje pytanie podczas pisania prompta
    - stworzyć własne skille pod ten projekt (np. wpinanie nowego arkusza, weryfikacja
      formulasPage) — gotowe pluginy są już wpięte

  + UI

    - Umieścić linię na prawo od sidebara na warstwę pod oknami pdfów

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
        - Firefox jako jedyny nie zawraca odcienia po v49 (wygląda jak stary goły invert), choć Chrome na tej samej maszynie tak. Kolejność sprawdzania: numer wersji w rogu → about:support (czy rysuje karta graficzna) → profil koloru i HDR
        CHYBA TO JEST NIEAKTUALNE JUŻ
      - Iphone i Safari: nie sprawdzone
      - Reszta najpopularniejszych przeglądarek działa dobrze
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

  - Przy suwakach / sliderach w rozwiązaniach interaktywnych powinny być strzałki w lewo po lewe i po prawejktóre można klikać lub przytrzymywać również na telefonach, aby wartość suwaka. W stylu strzałek prev-step i next-step lub tych które pojawiają się prz yzaszerockich dotsach. 

  - Zwykłe rozwiązania powinny składać się z arraya / listy wielu sposobów / podejść. Jeżeli jest tylko jeden element to UI wyświetla go tak jak dotychczas. Jeśli więcej to robią się zakładki w stylu tych w widgetach.

  - dodać przycisk "pokaż zasady oceniania" na końcu "Sprawdzania obliczeń" który miałby podobną funkcjonalność co przycisk "Pokaż wzory" - otwierałby okienko i też by przenosił do odpowiedniej strony w PDF

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


  + OPUS 5 MEDIUM DOPISAŁ (2026-08-20, po rozdziale licencyjnym widgets/, patrz issues/licencja-premium.md):

    - rozdzielić treści premium z exercises.json do osobnego matura/<id>/premium.json, doładowywanego drugim fetchem i scalanego z bazowym. Dziś w jednym pliku siedzą wymieszane treści CKE, darmowe i przyszłe premium, więc nie da się ich objąć różnymi licencjami ani później zablokować serwerem. Zrobić to, ZANIM powstaną pierwsze treści premium, bo potem przenoszenie boli

    - uodpornić app/widget-registry.js na brak katalogu widgets/: dziś wymienia funkcje po nazwie, więc bez widżetów leci ReferenceError i zabiera całą stronę. Póki oba katalogi jadą razem, nic się nie dzieje, ale przy pierwszym wdrożeniu darmowej wersji bez widżetów strona po prostu nie wstanie

    - paywall wymaga hostingu, który potrafi sprawdzić, kto puka: GitHub Pages tego nie umie (i jego regulamin zabrania hostować tam płatnego serwisu). Kandydaci z darmowym progiem: Cloudflare Pages z Functions, Netlify, Vercel. Decyzja na Fazę 3, ale warto o niej wiedzieć wcześniej

    - przed pierwszą sprzedażą przemyśleć pseudonim: przy płatnych treściach do zgłoszenia DMCA i do dochodzenia praw potrzebne są prawdziwe dane (jest już osobny punkt wyżej, tu tylko podbicie priorytetu)


<br>


+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ (patrz done/README.md i CLAUDE.md)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DOPISANE PRZEZ CLAUDA, nie pisz tam dużo, technikalia należą do issues. Napisz jakim modelem jesteś i na jakim efforcie. Jeżeli czytasz notatki np. Sonneta Low to ufaj im mniej niż tym zrobionym przez Opusa na High

  - PRÓG WEJŚCIA DO SEKCJI TESTOWANIE HENRICH (zaostrzony 2026-08-20, bo sekcja urosła do 338 linijek i przestała być listą do przeklikania). Wpis wchodzi tam tylko wtedy, gdy przechodzi OBA sita naraz:

    - nie da się tego sprawdzić w sesji Claude-a (playwright, chrome-devtools-mcp, skrypty w tools/). Jeśli da się sprawdzić samemu, sprawdź i nie pisz o tym nic

    - Henrich NIE natrafi na to przypadkiem, korzystając ze strony normalnie. Ciemny motyw, skrajne położenia suwaków, blokady przeciągania, słabe łącze, telefon, wąskie okno: tak. „Czy widżet się rysuje", „czy odczyt pokazuje wynik", „czy rozwiązanie się rozwija": NIE, bo to widać przy pierwszym kliknięciu

    - Wpis, który nie przechodzi, ma dwa wyjścia i żadnym z nich nie jest „wpiszę na wszelki wypadek": albo sprawdzasz sam i milczysz, albo, gdy to naprawdę scenariusz do przejścia kiedyś, dopisujesz go do issues/testowanie-archiwum.md

    - Sekcja ma się mieścić na jednym ekranie, mniej więcej dwadzieścia punktów. Dokładając nowy wpis, wyrzuć albo zarchiwizuj któryś stary; nie dokładaj na sam koniec i nie zostawiaj rosnącego ogona

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

