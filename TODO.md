Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.

  - Kroki mają za długie „czekania" na początku i na końcu filmu (wait() w Manimie) — wyciąć.
    Małe waity w środku kroku, między pojedynczymi animacjami, są okej. Najmocniej widać w zad. 1.

  - Wczytywanie filmów: albo pobierać je dużo wcześniej niż w chwili kliknięcia, albo zbić framerate.
    - pulsowanie kadru jest irytujące — wyrzucić je
    - zamiast niego prosta, minimalistyczna animacja na dole ekranu (trzy kropki albo kółko jak na YT),
      pokazująca się dopiero po ~500 ms
    - dziś pulsowanie miga przy każdej zmianie kierunku i przy spamowaniu ► wygląda, jakby strona
      ładowała się bez końca

  - Prefetch filmów nie działa (testowane na Chrome): przy czekaniu wykres sieci jest płaski, spajki
    pojawiają się dopiero przy klikaniu. W logach widać zapis do cache, ale odtwarzacz z niego nie
    korzysta.

  - Strona się wysypała przy szybkim spamowaniu next-step (Brave na Bazzite, kod błędu 5) — do
    odtworzenia i naprawy.

  - Zad. 1, kropki kroków: przy większej liczbie kroków niż mieści pasek ma być można
    przewijać (dziś sprawdzone tylko dla dziesięciu, które mieszczą się bez przewijania)
    - kropki są na granicy wygody dla kciuka na telefonie — rozważyć lekkie powiększenie
      (w v31 zrobione tylko marginesy boczne, rozmiar bez zmian)

  - usunąć całkowicie „solutionTextMore" — z wszystkich exercises.json i z template.html/JS,
    nie ma już żadnego odbiorcy

  - panel boczny, lewy górny róg (po testach v32):
    - strzałka wychodzi nad welon tylko w ciemnym motywie — w jasnym dalej przygaszona
    - zdjąć biały prostokąt tła spod logo (Henrichowi nie leży); logo nie musi wychodzić
      nad welon, wystarczy sama strzałka — więc i problem przebijającej treści zadania znika

  - Błędy w filmach — ZOSTAŁO (zad. 3, 5 i 6 poprawione w v30):
    - Zad 4. wygląda wzorowo, ale łamie zasadę ciągłości klatek: zielona szóstka zostaje
      na ostatniej klatce kroku 2, a krok 3 startuje czarny (SSIM 0,9990)
    - Zad 2, 7, 8 i 9 były robione tą samą metodą co 5 i 6, więc trzeba przejrzeć ich
      animacje; tools/styk-klatek.sh pokazuje, w których krokach nie zgadzają się styki
    - Zad 3 krok 6 kończy się szarym nawiasem domykającym; reszta przyciemnień już się
      rozjaśnia na końcu kroku

<br>


+ NIE REALIZUJ:
  - Ciemny motyw wymuszony ręcznie w panelu bocznym: rysunki/filmy mają przygasać jak przy
    „auto" — poprawka przy okazji v20, jeszcze bez potwierdzenia Henricha.
    issues/krok-po-kroku-v20-testy.md

  - Zadanie 2 — do sprawdzenia merytoryka kroków: krok 1 i 6 (wykładnik -1, potem 5,
    wynik \(5^4\)). issues/krok-po-kroku-v20-testy.md
    Punkt o za wąskich marginesach podpisu pod filmem odpadł sam: w v20 podpisu już nie ma,
    opis kroku siedzi w rozwijanym ROW 3. Zmierzone na telefonie 390 px — treść zadania ma
    24 px marginesu, film i ROW 3 po 25 px, czyli równo. Zostaje do przeklikania na żywo.

  - Zad. 10/11 na telefonie: pola/przyciski są już pod treścią zdania i jest czytelniej, ale brakuje
    odstępu między kolejnymi zdaniami (1, 2, 3…) — zlewają się w jeden blok.

  - Odwracanie kolorów grafik/wideo w dark mode (`--filtr-grafik-zadan`) działa tlyko w cześci (przeglądarek chyba)

  - Naprawić dziwne działanie odwracania kolorów grafik na niektórych przeglądarkach:
    - Pixel 7a GrapheneOS: 
      - Samsung Browser zmienia tło strony wedle własnego pomysłu a odwracanie kolorów w ogóle nie działa
      - na reszcie przeglądarek działa dobrze
    - Windows 10: działa w pełni na wszystkich najpopularniejszych przglądarkach
    - Bazzite: 
      - Chrome i Brave - brak matchu kolorów tła grafiki i ogólnego tła (prawopodobnie na skutenk dziwnego renderowania koloru tła na Bazzite)
      - na reszcie przeglądarek działa dobrze
    - Rozpoznanie i warianty naprawy: issues/dark-mode-inwersja-przegladarki.md


<br>


+ TESTOWANIE HENRICH
<br> Claude zapisuje małymi literami. HENRICH ZAPISUJE WIELKIMI LITERAMI.

  v32 — reszta po odbiorze (Opus 5, medium):

  - wejdź na telefonie w dowolne zadanie otwarte (np. zad. 3) i rozwiń wszystko naraz
    - ramka „sprawdzanie obliczeń", pole na notatki, rozwiązanie i formularz zgłoszenia błędu
      mają teraz jedną wspólną szerokość, wcześniej dwie pierwsze były węższe
    - przy okazji zerknij na zadania zamknięte: przyciski A/B/C/D są odrobinę szersze,
      sprawdź czy nic nie wychodzi poza ekran


  kontener — dopiero PO Rebuild Container (Opus 5, medium):

  - otwórz w kontenerze dowolny plik `.py` z `manimations/`
    - kolorowanie i podpowiedzi mają działać od razu, bez doklikiwania rozszerzenia

  - ~~w terminalu kontenera: `ls -ld ~/.cache` ma pokazać właściciela `node`~~ — sprawdzone
    z sesji 14.08 po przebudowie: właściciel `node`, zapis działa. EACCES z chrome-devtools-mcp
    zniknął, ale plugin zatrzymuje się teraz na braku samego Chrome'a — patrz OPUS DOPISAŁ niżej

  - ~~w terminalu kontenera: `claude mcp list`, wpis `github`~~ — sprawdzone z sesji 14.08:
    `github` ✔ Connected, zmienna `GITHUB_PERSONAL_ACCESS_TOKEN` ustawiona, `gh` zalogowany
    z wolumenu (nie trzeba było logować się ponownie). Przy pierwszym wywołaniu potrafi
    zwrócić „tools fetch failed — timeout"; drugie przechodzi



<br>


+ DLA HENRICHA:


  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable


<br>


+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - plugin frontend-design działa, ale jego włącznik siedzi w `.claude/settings.local.json`
    (poza gitem) — do decyzji, czy przenieść do `.claude/settings.json`, żeby jechał z repo
    jak superpowers (`issues/claude-code-pluginy.md`)


<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:
  
  + Zweryfikować poprawność:
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

  + ULEPSZANIE WORKFLOW (skopiowane z NOTATKI_USERA)
    - Schedule adversarial review lub /code-review
    - Stworzyć/pobrać potrzebne mi skille do tego projektu
    - wyłączyć skróty które powodują, że przeklikuje pytanie podczas pisania prompta
    - rozkminić, poszukać, poinstalować, pouczyć się - pluginy różne:
      - frontend-design@claude-plugins-official czy jakoś tak
      - superpowers

  Przed Fable:
    - Obgadać z Opusem czy używać Fable z superpowers, subagentami itd.
      - Subagentci: Czy powinienem puścić Fable mając duży zapas limitu aby Opusy i Sonnety będące subagentami mogły z niego korzystać odciążając fable?

    
  - Fable:
    - Analiza kosztów długoterminowych - Symulacja: co się stanie przy 1k, 10k, 100k użytkowników na danym stacku (koszty, limity, throttling)
    - Punkty krytyczne (failure points)
    - Weryfikacja poprawności matematycznej
    - Lista checkboxów "Sprawdzanie rozwiązania"
    - Interaktywne rozwiązania matury 2026
    - Usprawnienie struntury projektu


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


  - "Pokaż potrzebne wzory" powinien mieć możliwośc wyboru wielu podpunktów?, kropek?, a formulasPage w zadaniach powinien się zmienić na formulasPages (s na końcu). Powinno być wiele lokacji wzorów do przywołania pod jednym zadaniem. 
    - Zad 9. dopisać str 7 (wyróżnik Δ, obok już wpisanej str 8 ze wzorem na x1,x2)
    - Zad 11. dopisać str 16 (pole trójkąta [10.4])
    - Zad 17. dopisać str 18 (podzadania 17.1/17.2 mają już str 11)
    - Zad 19. dopisać str 20 (pole trapezu [10.17], obok już wpisanej str 17 z podobieństwem trójkątów)
    - Zad 24. dopisać str 27 (jest tam rysunek ostrosłupa, obok już wpisanej str 11 z tangensem)
    - Zad 30. dopisać str 26 (pole całkowite prostopadłościanu [12.2], obok już wpisanej str 8 z wierzchołkiem paraboli)


  - Przycisk "Zresetuj ustawienia" z popup-em do potwierdzenie. Podświetlajacy się na czerwono po najechaniu i widoczny na dole side panelu aby przypadkiem go nie kliknąć.
  - Wsparcie, donate-y itd.

    - W index.html dodać sekcję o autorze i link do Patronite
    - Na githubie w ustawieniach repo też można coś podpiąć chyba ale trzeba sprawdizć czy byłoby to fair.

  - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

  
  - sprawdzić merytorykę arkuszy (na końcu, przed rozpowszechnieniem)

  - wysyłanie całego localStorage przez użytkownika podczas zgłaszania błędu jest a bit scatchy też troche niebezpiczne

<br>


+ DOPISANE PRZEZ CLAUDA
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

  + SONNET DOPISAŁ:

    - Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie"
      - (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

  + Sonnet 5, high — paczka drobiazgów UI (v15, 2026-08-10):

    - Dwa z pięciu punktów tej paczki nie były w spec docu, tylko dopisane obok niego w TODO.md
      z pytajnikiem/bez konkretnej decyzji projektowej. Zrobiłem je własnym osądem, warto zerknąć:
      „Sprawdź wszystkie odpowiedzi" jako podpunkt pod „Poprawność" — przeniosłem 1:1 wzorem
      Zegara/Wskaźników pod egzaminem (ta sama klasa `.sidebar-sub`, teraz uogólniona z
      `.sidebar-ustawienie.sidebar-sub` na `.sidebar-sub` żeby działała też na `.sidebar-akcja`).
      Pigułki formularza zgłoszenia — wybrałem jednolite `flex: 1 1 calc(50% - 4px)` (zawsze dwie
      w rzędzie, długie nazwy łamią się na dwie linijki) zamiast różnicować szerokość per pigułka —
      prostsze i zgodne z „nie przekombinuj" z TODO, ale to była moja decyzja, nie Twoja specyfikacja.


  + Opus 5, medium

    - Gdy Henrich zdecyduje się upublicznić imię i nazwisko, trzeba podmienić pseudonim `Henrich2137` na dane osobowe w poniższych miejscach. CLA na pseudonim jest słabsze dowodowo niż na nazwisko.
      - `LICENSE.md` (linie 1–2: copyright + Required Notice)
      - `CONTRIBUTING.md` (punkt 2 zgody na licencjonowanie wkładu)
      - stopki w plikach html

    - Gdy ruszy domena matematykazen.pl, podmień URL w `LICENSE.md:2` (Required Notice — ta linia jest kopiowana przez każdego redystrybutora) i `README.md`; w OVERVIEW.md domena jest już opisana jako plan Fazy 2.


  + Opus 5, high — devcontainer, 2026-08-06:

    - Sprawdzić nowy devcontainer na Kubuntu/Dockerze. Zmiany testowałem tylko pod rootless podmanem na Bazzite; `docker exec --privileged` działa tak samo, ale nie miałem jak tego odpalić.

    - VS Code wpuszcza do kontenera socket ssh-agenta, gpg-agenta, X11 i Waylanda oraz podpina git credential helper hosta — omija to firewall (to nie jest ruch sieciowy). Wyłączalne tylko częściowo: `dev.containers.mountWaylandSocket: false` i `dev.containers.gitCredentialHelperConfigLocation: "none"` (uwaga: to drugie zabierze pushowanie po HTTPS bez tokena w kontenerze). Dla ssh-agenta i X11 rozszerzenie nie ma przełącznika — sprawdziłem package.json wersji 0.463.0.

    - `sudo` w kontenerze przestało działać (świadomie, `--cap-drop=ALL` bez wyjątków). Jeśli okaże się potrzebne do czegoś realnego, trzeba dodać `--cap-add=SETUID --cap-add=SETGID` — ale NIE `NET_ADMIN`, bo to znów pozwoli rozbroić firewall od środka.

    - Świadomie NIEdomknięta dziura w firewallu, do ewentualnej decyzji: dozwolone domeny (GitHub, npm) są z natury kanałem na dane — nie da się usunąć bez odcięcia gita. (Punkt o przepuszczonej bramie/panelu routera zniknął stąd 2026-08-10 — brama jest już zawężona do samego portu 53, patrz `.devcontainer/README.md`, sekcja „Brama: `/24` → `/32` → tylko port 53".)


  + OPUS DOPISAŁ (Opus 5, medium) — po paczce z 2026-08-06:

    - Zadania otwarte bez `gradingCriteria` w danych nadal renderują stare przyciski „0..N pkt" (awaryjna ścieżka w app/render.js). Dziś takich zadań nie ma — przy wpinaniu NOWEGO arkusza trzeba pamiętać o kryteriach, inaczej zadanie po cichu wróci do starego UI.

    - `finalAnswer.label` w exercises.json nie ma już odbiorcy (renderer je ignoruje). Zostawione we wszystkich arkuszach — do decyzji, czy kiedyś wyczyścić dane.

    - Kryteria dla zadań 4-punktowych są kaskadą progów z klucza CKE, więc uczeń, który zaznaczy tylko „poprawny wynik", dostanie 1 pkt zamiast 4. Do przemyślenia, czy zaznaczenie wyższego progu nie powinno automatycznie zaznaczać niższych.


  + OPUS DOPISAŁ (Opus 5, medium) — 2026-08-07, narzędzia:

    - Skille superpowers są już wpięte (scope project, jadą z repo) — szczegóły w CLAUDE.md, sekcja „Claude Code — plugins / skills". Widać je dopiero PO RESTARCIE sesji Claude Code. Z punktu „Stworzyć/pobrać potrzebne mi skille" zostaje więc już tylko „stworzyć": własne skille pod ten projekt (np. wpinanie nowego arkusza, weryfikacja formulasPage).

    - Dwa punkty z „ULEPSZANIE WORKFLOW" wyglądają na zrobione i chyba należą do done/ — zostawiam decyzję Tobie, bo to Twoja sekcja: „uruchomienie całego VS Code w Dev Container" (zrobione 2026-08-06) i część „pobrać skille" (2026-08-07).

  + OPUS DOPISAŁ (Opus 5, medium) — 2026-08-09, kontener:

    - Gdy `matematykazen.pl` ruszy: odkomentować wpis w `CONTENT_DOMAINS` w `.devcontainer/init-firewall.sh` (dziś domena nie istnieje w DNS) i przy okazji poprawić `Required Notice:` w LICENSE.md, które wciąż wskazuje na GitHub Pages.

  + OPUS DOPISAŁ (Opus 5, medium) — 2026-08-14, po Rebuild Container:

    - `chrome-devtools-mcp` dalej nie otwiera strony, ale to JUŻ INNY BŁĄD niż EACCES — ten jest naprawiony (node sam założył sobie `~/.cache/chrome-devtools-mcp/chrome-profile`). Teraz leci „Could not find Google Chrome executable for channel 'stable' at /opt/google/chrome/chrome": w kontenerze nie ma Chrome'a, jest tylko Chromium Playwrighta (`/home/node/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome`). Plugin ma na to przełącznik `--executablePath` (plus `--headless`), ale jego `args` siedzą w cache'u pluginu poza repo (`~/.claude/plugins/cache/.../plugin.json`) i giną przy aktualizacji pluginu. Do decyzji: albo własny wpis serwera w repo (`.mcp.json`) z tymi flagami zamiast wersji z pluginu, albo doinstalowanie Chrome'a w Dockerfile (~150 MB obrazu, wymaga hosta). Szczegóły dopisane w `issues/chrome-devtools-mcp-cache-eacces.md`.

  + OPUS DOPISAŁ (Opus 5, high) — 2026-08-11, odtwarzacz krok po kroku (v20):

    - Decyzje, które podjąłem sam, bo nie było ich w Twoich punktach — do ewentualnej korekty:
      kropka „obecna" przeskakuje na prawą po dobiegnięciu filmu (patrz TESTOWANIE wyżej);
      odcinki między kropkami mają zawsze cienką kreskę, a wypełnia się tylko ten bieżący;
      krok bez opisu w danych w ogóle nie pokazuje przycisku ROW 3, zamiast otwierać pustkę.

    - Nazwa rewersu NIE jest w exercises.json — odtwarzacz dokłada `reverse` przed rozszerzeniem
      nazwy z pola `src`. Wpinając nowy arkusz pamiętaj, żeby puścić `tools/rewersy.sh`, inaczej
      ◄ nie ma czego odtworzyć (przy braku pliku krok po prostu nie cofnie się animacją).

    - `python3 -m http.server` NIE nadaje się do pracy nad wideo: nie obsługuje żądań zakresowych,
      więc przewijanie filmu cicho nie działa i wygląda to jak błąd w kodzie. Kosztowało mnie to
      sporo szukania nieistniejącej usterki. Dopisane do CLAUDE.md i issues/krok-po-kroku-produkcja.md.

    - Chromium z Playwrighta w chmurowym kontenerze NIE ODTWARZA H.264 (brak kodeka), a Chrome
      nie da się doinstalować, bo firewall blokuje dl.google.com. Logikę odtwarzacza sprawdziłem
      na kopiach WebM, a same pliki mp4 osobno przez ffmpeg/SSIM. Czego NIE dało się u mnie
      sprawdzić: realnego odtwarzania tych konkretnych mp4 w przeglądarce i zachowania na telefonie.
      - SPROSTOWANIE 2026-08-12 (Opus 5, high): w kontenerze LOKALNYM H.264 odtwarza się bez
        problemu — sprawdzone na plikach arkusza. Ograniczenie dotyczyło tylko chmury.

  + FABLE DOPISAŁ (Fable 5, po paczce 4 „Spójność UI etap 2", 2026-08-09):

    - W jasnym motywie --text-faint-2 (#909090, 3.3:1) i --text-faint-3 (#999, 2.8:1) są poniżej WCAG AA (4.5:1) przy 13–14px tekstach (etykiety „miejsce na notatki"/samooceny, uchwyty paneli PDF). Paczka 4 poprawiła tylko --text-faint (mierzone elementy landingu i stopek); te dwa tokeny do decyzji — przyciemnienie zmieni sporo drobnych etykiet naraz.

    - Cienie kropek wskaźników (0 1px 4px w exam.css) świadomie zostały poza tokenem — dwa drobne, powiązane znaczeniowo wystąpienia; tokenizować dopiero, gdyby doszło trzecie.

+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ (patrz done/README.md i CLAUDE.md)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DO REALIZACJI Dopisane przez CLAUDA napisz jakim modelem jesteś i na jakim efforcie, Jeżeli czytasz notatki np Sonneta na low to ufaj im mniej niż tym zrobionym przez Opusa na High

  - Wpisy w sekcji TESTOWANIE HENRICH piszesz prostym zdaniem, małymi literami (normalna polska ortografia, wielka litera tylko tam gdzie gramatycznie należy — początek zdania, nazwy własne). Bez nagłówków typu ORYGINALNY PUNKT / DOCELOWA WERSJA, bez CAPS LOCKA dla podkreślenia słów. Domyślnie jedna linijka: co kliknąć → czego się spodziewać, np. „kliknij next-step w trakcie odtwarzania filmu — powinien przeskoczyć do początku następnego filmu".
    - Gdy jeden punkt obejmuje kilka rzeczy do sprawdzenia naraz, rozbij go: krótka linijka wiodąca, pod nią zagnieżdżone podpunkty, po jednej rzeczy na podpunkt. Drugi poziom zagnieżdżenia tylko wtedy, gdy szczegóły dotyczą jednego konkretnego podpunktu, np.:

          - sprawdź wygląd przycisków
            - po bokach zaokrąglone daszki
            - na środku jeden przycisk odtwórz/pauza/restart
              - bez kółka
              - restart (zakręcona strzałka) pokazuje się tylko po dobiegnięciu filmu do końca
            - nakładane ikonki pauzy/restartu na filmie mają zniknąć

    - Pustą linijkę zostawiaj pod każdym punktem, a w długich listach pełnych podpunktów także pod podpunktami — żeby się nie zlewały w blok. W krótkiej liście paru jednolinijkowców nie trzeba.

