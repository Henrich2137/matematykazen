Oto plik który tworzy Henrich (ja, użytkownik).


+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.

  - Posprzątaj w sekcji "DOPISANE PRZEZ CLAUDE-A" wg komentarzy henricha napisanych WIELKIMI LITERAMI. 
    - Punkty oznaczone jako "NA GÓRĘ" dopisz zgodnie z zasadami w podsekcji "HENRICH MÓWI "MA TO SENS", STĄD MOŻE WESPNĄ SIĘ JESZCZE WYŻEJ".
    - Z punktami oznaczonymi do archiwizacji zrób to co uważasz: todo/ issues/ lub inne pliki .md albo wyrzuć w zapomienie jeśli miałoby wprowadzać w błąd.

  - Odpraw poniższy punkt do done. To jest już zrobione:
    - panel boczny, lewy górny róg (po testach v32):
      - strzałka wychodzi nad welon tylko w ciemnym motywie — w jasnym dalej przygaszona
      - zdjąć biały prostokąt tła spod logo (Henrichowi nie leży); logo nie musi wychodzić
        nad welon, wystarczy sama strzałka — więc i problem przebijającej treści zadania znika
    HENRICH: TUTAJ TEŻ JUŻ JEST ZROBIONE, do odprawy

  - Dodatkowo: jeśli skończysz ładnie te wszystkie rzeczy do wykonaj poniższe punkty oznaczone jako "DODATKOWO"



<br>


+ NIE REALIZUJ, CZEKAJĄ W KOLEJCE:

  - Rozwiązanie krok po kroku:
    
    - Kroki mają za długie „czekania" na początku i na końcu filmu (wait() w Manimie) — wyciąć.
      Małe waity w środku kroku, między pojedynczymi animacjami, są okej. Najmocniej widać w zad. 1.

    - Zad. 1, kropki kroków: przy większej liczbie kroków niż mieści pasek ma być można
      przewijać (dziś sprawdzone tylko dla dziesięciu, które mieszczą się bez przewijania)
      - kropki są na granicy wygody dla kciuka na telefonie — rozważyć lekkie powiększenie
        (w v31 zrobione tylko marginesy boczne, rozmiar bez zmian)

  
  - usunąć całkowicie „solutionTextMore" — z wszystkich exercises.json i z template.html/JS,
    nie ma już żadnego odbiorcy
  
  DODATKOWO
  - Na telefonie, odczas odpalonego sidebara logo powinno być ono przygaszone, z tyłu i nieklikalne. Klijknięcie powinno powodować wyłączenie sidebara (bo pomiędzy jest welon czy coś)


<br>


+ TESTOWANIE HENRICH
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI.
<br> Mój telefon na chrome ma "okno": 485x945 

  - wczytywanie kroków (v33)

    - wejdź w „Rozwiązanie" w zad. 1 i przeklikaj ► kilka razy — kadr nie ma już ani pulsować, ani przygasać

    - poczekaj na krok przy słabym zasięgu — na dole filmu mają się pokazać trzy kropki, dopiero po pół sekundy

    - spamuj ► i ◄ — kropki nie powinny migać przy każdym kliknięciu

    - wejdź w zadanie, odczekaj kilka sekund przed kliknięciem „Rozwiązanie", potem przeklikaj kroki —
      powinny wchodzić natychmiast, bez czekania na film


<br>


+ DLA HENRICHA:

  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable


<br>


+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - nic


<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:
  
  Przed Fable:
    - Obgadać z Opusem czy używać Fable z superpowers, subagentami itd.
      - Subagentci: Czy powinienem puścić Fable mając duży zapas limitu aby Opusy i Sonnety będące subagentami mogły z niego korzystać odciążając fable?

  - Fable:
    - Interaktywne rozwiązania matury 2026
    - Lista checkboxów "Sprawdzanie rozwiązania"
    - Weryfikacja poprawności matematycznej
    - Usprawnienie struntury projektu
    - Analiza kosztów długoterminowych - Symulacja: co się stanie przy 1k, 10k, 100k użytkowników na danym stacku (koszty, limity, throttling)
    - Punkty krytyczne (failure points)
    
    

  + Zweryfikować poprawność matematyczną:

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

    - poprawność matematyczna treści w arkuszu — rozwiązania krok po kroku (zad. 1–9,
      komplet po v27) i ich opisy pod filmem

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
    - rozkminić, poszukać, poinstalować, pouczyć się - pluginy różne:
      - frontend-design@claude-plugins-official DONE
      - superpowers DONE
    - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy
      - jak mam przeprowadzić test DONE

  + UI

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
        - Samsung Browser zmienia tło strony wedle własnego pomysłu, a odwracanie kolorów w ogóle nie działa
        - na reszcie przeglądarek działa dobrze
      - Windows 10: działa w pełni na wszystkich najpopularniejszych przeglądarkach
      - Bazzite:
        - Chrome i Brave — brak matchu kolorów tła grafiki i ogólnego tła (prawdopodobnie na skutek dziwnego renderowania koloru tła na Bazzite)
        - na reszcie przeglądarek działa dobrze
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
    
    - FAZA 2.3
      - WKLEJ NP. DOT. MATEMATYKAZEN.PL
    
    - FAZA 3.
      - WKLEJ CO TAM PODPASUJE

    - WKLEJ TU INNE OZNACZONE "NA GÓRE"
  
  
  + SONNET DOPISAŁ:

    - Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie"
      - (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.
      DO SKRÓCENIA, NA GÓRE
      
  + Sonnet 5, high — paczka drobiazgów UI (v15, 2026-08-10):

    - Dwa z pięciu punktów tej paczki nie były w spec docu, tylko dopisane obok niego w TODO.md
      z pytajnikiem/bez konkretnej decyzji projektowej. Zrobiłem je własnym osądem, warto zerknąć:
      „Sprawdź wszystkie odpowiedzi" jako podpunkt pod „Poprawność" — przeniosłem 1:1 wzorem
      Zegara/Wskaźników pod egzaminem (ta sama klasa `.sidebar-sub`, teraz uogólniona z
      `.sidebar-ustawienie.sidebar-sub` na `.sidebar-sub` żeby działała też na `.sidebar-akcja`).
      Pigułki formularza zgłoszenia — wybrałem jednolite `flex: 1 1 calc(50% - 4px)` (zawsze dwie
      w rzędzie, długie nazwy łamią się na dwie linijki) zamiast różnicować szerokość per pigułka —
      prostsze i zgodne z „nie przekombinuj" z TODO, ale to była moja decyzja, nie Twoja specyfikacja.
      DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI


  + Opus 5, medium

    - Gdy Henrich zdecyduje się upublicznić imię i nazwisko, trzeba podmienić pseudonim `Henrich2137` na dane osobowe w poniższych miejscach. CLA na pseudonim jest słabsze dowodowo niż na nazwisko.
      - `LICENSE.md` (linie 1–2: copyright + Required Notice)
      - `CONTRIBUTING.md` (punkt 2 zgody na licencjonowanie wkładu)
      - stopki w plikach html
    DO SKRÓCENIA, NA GÓRE

    - Gdy ruszy domena matematykazen.pl, podmień URL w `LICENSE.md:2` (Required Notice — ta linia jest kopiowana przez każdego redystrybutora) i `README.md`; w OVERVIEW.md domena jest już opisana jako plan Fazy 2.
    DO SKRÓCENIA, NA GÓRE

  + Opus 5, high — devcontainer, 2026-08-06:

    - Sprawdzić nowy devcontainer na Kubuntu/Dockerze. Zmiany testowałem tylko pod rootless podmanem na Bazzite; `docker exec --privileged` działa tak samo, ale nie miałem jak tego odpalić.
    DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

    - VS Code wpuszcza do kontenera socket ssh-agenta, gpg-agenta, X11 i Waylanda oraz podpina git credential helper hosta — omija to firewall (to nie jest ruch sieciowy). Wyłączalne tylko częściowo: `dev.containers.mountWaylandSocket: false` i `dev.containers.gitCredentialHelperConfigLocation: "none"` (uwaga: to drugie zabierze pushowanie po HTTPS bez tokena w kontenerze). Dla ssh-agenta i X11 rozszerzenie nie ma przełącznika — sprawdziłem package.json wersji 0.463.0.
    DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

    - `sudo` w kontenerze przestało działać (świadomie, `--cap-drop=ALL` bez wyjątków). Jeśli okaże się potrzebne do czegoś realnego, trzeba dodać `--cap-add=SETUID --cap-add=SETGID` — ale NIE `NET_ADMIN`, bo to znów pozwoli rozbroić firewall od środka.
    DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

    - Świadomie NIEdomknięta dziura w firewallu, do ewentualnej decyzji: dozwolone domeny (GitHub, npm) są z natury kanałem na dane — nie da się usunąć bez odcięcia gita. (Punkt o przepuszczonej bramie/panelu routera zniknął stąd 2026-08-10 — brama jest już zawężona do samego portu 53, patrz `.devcontainer/README.md`, sekcja „Brama: `/24` → `/32` → tylko port 53".)
    DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

  + OPUS DOPISAŁ (Opus 5, medium) — po paczce z 2026-08-06:

    - Zadania otwarte bez `gradingCriteria` w danych nadal renderują stare przyciski „0..N pkt" (awaryjna ścieżka w app/render.js). Dziś takich zadań nie ma — przy wpinaniu NOWEGO arkusza trzeba pamiętać o kryteriach, inaczej zadanie po cichu wróci do starego UI.
    DO SPRAWDZENIA

    - `finalAnswer.label` w exercises.json nie ma już odbiorcy (renderer je ignoruje). Zostawione we wszystkich arkuszach — do decyzji, czy kiedyś wyczyścić dane.
    DO SPRAWDZENIA

    - Kryteria dla zadań 4-punktowych są kaskadą progów z klucza CKE, więc uczeń, który zaznaczy tylko „poprawny wynik", dostanie 1 pkt zamiast 4. Do przemyślenia, czy zaznaczenie wyższego progu nie powinno automatycznie zaznaczać niższych.
    NA GÓRĘ

  + OPUS DOPISAŁ (Opus 5, medium) — 2026-08-07, narzędzia:

    - Skille superpowers są już wpięte (scope project, jadą z repo) — szczegóły w CLAUDE.md, sekcja „Claude Code — plugins / skills". Widać je dopiero PO RESTARCIE sesji Claude Code. Z punktu „Stworzyć/pobrać potrzebne mi skille" zostaje więc już tylko „stworzyć": własne skille pod ten projekt (np. wpinanie nowego arkusza, weryfikacja formulasPage).
    DO SPRAWDZENIA, PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

    - Dwa punkty z „ULEPSZANIE WORKFLOW" wyglądają na zrobione i chyba należą do done/ — zostawiam decyzję Tobie, bo to Twoja sekcja: „uruchomienie całego VS Code w Dev Container" (zrobione 2026-08-06) i część „pobrać skille" (2026-08-07).
    DO PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI


  + OPUS DOPISAŁ (Opus 5, medium) — 2026-08-09, kontener:

    - Gdy `matematykazen.pl` ruszy: odkomentować wpis w `CONTENT_DOMAINS` w `.devcontainer/init-firewall.sh` (dziś domena nie istnieje w DNS) i przy okazji poprawić `Required Notice:` w LICENSE.md, które wciąż wskazuje na GitHub Pages.
    NA GÓRĘ

  + OPUS DOPISAŁ (Opus 5, high) — 2026-08-11, odtwarzacz krok po kroku (v20):

    - Decyzje, które podjąłem sam, bo nie było ich w Twoich punktach — do ewentualnej korekty:
      - kropka „obecna" przeskakuje na prawą po dobiegnięciu filmu (patrz TESTOWANIE wyżej); JUŻ CHYBA NIE
      - odcinki między kropkami mają zawsze cienką kreskę, a wypełnia się tylko ten bieżący;
      - krok bez opisu w danych w ogóle nie pokazuje przycisku ROW 3, zamiast otwierać pustkę.
    JEST OKEJ, DO PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI


    - Nazwa rewersu NIE jest w exercises.json — odtwarzacz dokłada `reverse` przed rozszerzeniem
      nazwy z pola `src`. Wpinając nowy arkusz pamiętaj, żeby puścić `tools/rewersy.sh`, inaczej
      ◄ nie ma czego odtworzyć (przy braku pliku krok po prostu nie cofnie się animacją).


    - `python3 -m http.server` NIE nadaje się do pracy nad wideo: nie obsługuje żądań zakresowych,
      więc przewijanie filmu cicho nie działa i wygląda to jak błąd w kodzie. Kosztowało mnie to
      sporo szukania nieistniejącej usterki. Dopisane do CLAUDE.md i issues/krok-po-kroku-produkcja.md.
      ZAPISZ W WIDOCZNYM MIEJSCU DLA SIEBIE NP W README MANIMATIONS CZY COS

    - Chromium z Playwrighta w chmurowym kontenerze NIE ODTWARZA H.264 (brak kodeka), a Chrome
      nie da się doinstalować, bo firewall blokuje dl.google.com. Logikę odtwarzacza sprawdziłem
      na kopiach WebM, a same pliki mp4 osobno przez ffmpeg/SSIM. Czego NIE dało się u mnie
      sprawdzić: realnego odtwarzania tych konkretnych mp4 w przeglądarce i zachowania na telefonie.
      - SPROSTOWANIE 2026-08-12 (Opus 5, high): w kontenerze LOKALNYM H.264 odtwarza się bez
        problemu — sprawdzone na plikach arkusza. Ograniczenie dotyczyło tylko chmury.
    DO PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

  + FABLE DOPISAŁ (Fable 5, po paczce 4 „Spójność UI etap 2", 2026-08-09):

    - W jasnym motywie --text-faint-2 (#909090, 3.3:1) i --text-faint-3 (#999, 2.8:1) są poniżej WCAG AA (4.5:1) przy 13–14px tekstach (etykiety „miejsce na notatki"/samooceny, uchwyty paneli PDF). Paczka 4 poprawiła tylko --text-faint (mierzone elementy landingu i stopek); te dwa tokeny do decyzji — przyciemnienie zmieni sporo drobnych etykiet naraz.
    NIC Z TEGO NIE ROZUMIEM, NIE WYGLĄDA NA SPECJALNIE ISTOTNE, DO PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI

    - Cienie kropek wskaźników (0 1px 4px w exam.css) świadomie zostały poza tokenem — dwa drobne, powiązane znaczeniowo wystąpienia; tokenizować dopiero, gdyby doszło trzecie.
    DO PRZENIESIENIA / ARCHIWIZACJI / WYRZUCENIA I/LUB AKTUALIZACJI


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

