Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.


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

  - spraw aby przycisk do rozwijania side-bara był nad przyciemieniem tła na telefonie. Nie ma być przyciemiony aby użytkownik wiedział, że jest możliwy do kliknięcia.

  
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
<br> Claude zapisuje małymi litery. HENRICH ZAPISUJE WIELKIMI LITERAMI.

  - v22, odtwarzacz krok po kroku — poprawki z twoich testów v21, arkusz grudzień 2024

    - poklikaj zadania z krokami na telefonie i poobracaj ekran — czerwony baner
      „ResizeObserver loop completed with undelivered notifications" nie ma się już pojawić
      ani razu (to była moja regresja z v21, najmocniej wychodziła w zad. 3)

    - sprawdź trzy zachowania przycisku cofania
      - kliknięty w trakcie odtwarzania albo na pauzie w środku kroku — puszcza film od tyłu
        od tego samego miejsca
      - kliknięty jeszcze raz, gdy film już się cofa — doskakuje na pierwszą klatkę kroku
        i zatrzymuje się (wcześniej się zacinał)
      - kliknięty na pierwszej klatce — cofa poprzedni krok

    - otwórz zad. 1 na telefonie — wszystkie dziesięć kropek ma się zmieścić bez przewijania,
      więc strzałki po bokach paska nie powinny się w ogóle pokazać
      - przy okazji sprawdź, czy kropki nie zrobiły się za ciasne dla kciuka

    - przycisk „pokaż wyjaśnienie kroku" ma być wyśrodkowany, a rozwinięty tekst na telefonie
      ma mieć margines i nie kleić się do krawędzi ekranu

    - na telefonie ramka podokna (rozwiązanie, „sprawdzanie obliczeń", formularz zgłoszenia)
      siedzi 18 px od krawędzi zamiast 25 — zobacz, czy to nie za blisko

    - otwórz rozwiązanie z krokami pierwszy raz — w miejscu filmu ma pulsować delikatne tło,
      ale dopiero po chwili; przy szybkim łączu nie powinno mrugnąć ani razu


  - v23, odtwarzacz krok po kroku — kroki gubiły się przy wolnym łączu; wszystko poniżej
    najlepiej sprawdzić na telefonie na komórkowym internecie albo z włączonym dławieniem sieci

    - wciśnij ◄ kilka razy pod rząd — licznik, kropki i pasek mają się cofać po jednym kroku
      na kliknięcie i nigdy nie pokazywać czegoś innego niż film, który widzisz

    - kliknij kropkę daleko z przodu i patrz na kadr — stary obraz ma delikatnie pulsować
      (przygasać), dopóki nowy krok się nie wczyta
      - przy szybkim łączu nie powinno mrugnąć ani razu

    - wciśnij środkowy przycisk (odtwórz) w chwili, gdy krok się jeszcze wczytuje — film ma
      ruszyć sam, gdy tylko wejdzie, a nie stanąć na pierwszej klatce

    - poklikaj ► kilka razy szybko przy słabym zasięgu — kadr nie ma na moment gasnąć
      ani pokazywać obrazu dwa razy

    - przewijaj i cofaj do woli przez minutę, a potem zostaw stronę w spokoju — odtwarzacz
      nie ma zostać zawieszony na przygaszonym kadrze


  - v24, filmy krok po kroku — zad. 1 i 3 przerenderowane w nowym kadrze, zad. 4 zrobione od zera

    - zad. 1 i zad. 3: filmy mają być w kadrze 16:9 jak w zad. 2, bez czarnych pasów
      i bez zmiany wielkości liter w trakcie przekształcenia
      - treść przekształceń jest ta sama co wcześniej — porównałem klatka w klatkę,
        więc szukaj raczej wyglądu niż matematyki

    - zad. 3 ma teraz opisy pod filmem przy każdym z ośmiu kroków (wcześniej tylko przy
      ostatnim) — przeczytaj, czy się zgadzają z tym, co widać na filmie
      - wzory pomocnicze zniknęły z samego filmu i siedzą w opisach, tak jak w zad. 2

    - zad. 3, kroki 2, 4 i 6 zatrzymują się na zapisie w większości szarym, z czarnym tylko
      tym fragmentem, który się zmienił — to zachowanie sprzed moich zmian, ale teraz widać
      je dłużej; powiedz, czy ma tak zostać, czy na koniec kroku wszystko ma wracać do czerni

    - zad. 4 (logarytmy) ma nowe rozwiązanie krok po kroku, cztery kroki — sprawdź całość,
      to jedyne z tej paczki, którego wcześniej nie było
      - scenariusz, który zatwierdziłeś, leży w manimations/zad4-kroki.md

    - zad. 6 i zad. 8 też dostały rozwiązania krok po kroku (dwa zadania wybrane przeze mnie)
      - scenariusze do sprawdzenia merytoryki: manimations/zad6-kroki.md i zad8-kroki.md
      - zad. 8 jest otwarte na 3 pkt, więc kroki są ułożone pod klucz CKE: założenie \(x\ne1\)
        ma własny krok i zostaje pod równaniem do końca — zobacz, czy tak jest czytelnie
      - w obu na zielono podświetla się CAŁY ułamek, którego dotyczy krok, a nie sam
        zmieniany kawałek (przy \(\frac{}{}\) trudno o precyzyjniejsze) — powiedz, jeśli to
        za dużo koloru



  - v26, odtwarzacz krok po kroku — trzy rzeczy z twojego zgłoszenia

    - dojedź cofką do końca (poczekaj, aż film od tyłu sam się zatrzyma) i sprawdź dwa
      przyciski — koniec cofki ma się zachowywać dokładnie jak pierwsza klatka zwykłego filmu
      - ◄ ma zacząć cofać POPRZEDNI krok
      - ► ma odtworzyć TEN SAM krok do przodu, czyli to samo co środkowy przycisk

    - poklikaj szybko w jedną kropkę (zwłaszcza w pierwszą, w zad. 4) — odtwarzacz nie ma
      się zacinać na przygaszonym kadrze
      - u mnie stary kod stał tak 5,6 s, teraz 1,6 s, czyli tyle, ile trwa samo pobranie

    - wejdź na arkusz i poczekaj chwilę, nic nie klikając, potem otwórz rozwiązanie
      z krokami — filmy mają być już pobrane, więc przewijanie kropkami ma być natychmiastowe
      - pobieranie rusza, gdy zadanie wjedzie na ekran, a nie dopiero po kliknięciu
      - jeśli masz w telefonie włączony „oszczędzanie danych", pobierania celowo nie ma


  - v27, kolejne trzy rozwiązania krok po kroku — zad. 5, 7 i 9 (znów mój wybór)
    - po tej paczce kroki mają zadania 1–9, czyli komplet od początku arkusza
    - scenariusze do sprawdzenia merytoryki: manimations/zad5-kroki.md, zad7-kroki.md, zad9-kroki.md

    - zad. 5 (procent składany) — sprawdź zwłaszcza krok z pierwiastkowaniem: w opisie
      pod filmem tłumaczę, dlaczego bierzemy tylko wartość dodatnią

    - zad. 7 (układ z parametrami) — oba równania jadą jedno pod drugim przez cały film,
      żeby było widać, że to dwa niezależne rachunki, a nie układ do rozwiązywania
      - zobacz, czy klamra z dwoma równaniami nie jest za mała na telefonie

    - zad. 9 (nierówność kwadratowa, otwarte na 2 pkt) — film robi sam rachunek i NIE rysuje
      paraboli, bo tuż pod nim jest już widżet, który pokazuje ją interaktywnie
      - powiedz, czy to dobry podział, czy jednak parabola ma być też w filmie

    - w zad. 5, 7 i 9 klatka, na której krok się zatrzymuje, bywa w całości zielona
      (to wynik danego kroku) — ta sama wątpliwość co przy zad. 6 i 8, jedna decyzja
      załatwi wszystkie


  - kontener: firewall + Playwright + read-only `.vscode` (2026-08-10), wymaga zwykłego Rebuild Container (bez `--no-cache`) — bez tego nic z tego nie zadziała; po przebudowie, w terminalu w kontenerze:
    - `dig +short github.com` — ma zwrócić adresy (jeśli w logu firewalla widać „UWAGA: DNS nie działa po zawężeniu", zawężenie bramy poszło źle, patrz `.devcontainer/README.md`, sekcja „Diagnostyka").
    - `curl -m 5 http://192.168.1.1` — ma nie przejść (timeout albo „Connection refused"); wcześniej otwierał panel routera, to samo dotyczy SMB (445) i drukarki (631).
    - `git push` / `npm ping` / `curl -sI https://cke.gov.pl` — mają nadal działać.
    - `bash .devcontainer/verify-firewall.sh` — ma zakończyć się sukcesem.
    - `touch .vscode/test` — ma odbić się o „Read-only file system" (to jest cel, nie błąd).
    - playwright: `NODE_PATH=/usr/local/share/npm-global/lib/node_modules node -e "require('playwright').chromium.launch().then(b=>b.close()).then(()=>console.log('OK'))"` — ma wypisać „OK", potem zrzut arkusza przez `tools/zrzuty.js` ma pokazać polski tekst, nie puste prostokąty.



<br>


+ DLA HENRICHA:

  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable


<br>


+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - dopisać pythona do extentions aby był też po rebuildzie itd.

  - przy otwarciu folderu ma się już nie pytać „Allow Automatic Tasks in Folder?", tylko po cichu zrobić `git pull --ff-only`.

  - na bazzite: backup `~/backup-vscode-flatpak/` (8 kB) po skasowanych danych flatpakowego VS Code — do usunięcia, gdy uznasz, że już niepotrzebny (dwa ustawienia istniały tylko tam i świadomie ich nie przeniosłem: `chat.viewSessions.orientation`, `chat.agent.sandbox.enabled`); cały przepis w `issues/flatpak-osierocone-dane.md`.

<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:
  
  + ULEPSZANIE WORKFLOW (skopiowane z NOTATKI_USERA)
    - Schedule adversarial review lub /code-review
    - Stworzyć/pobrać potrzebne mi skille do tego projektu
    - wyłączyć skróty które powodują, że przeklikuje pytanie podczas pisania prompta
    - rozkminić, poszukać, poinstalować, pouczyć się - pluginy różne:
      - frontend-design@claude-plugins-official czy jakoś tak
      - superpowers
  + UI

    - "Wskaźniki" (oceń się):
      - Przycisk "Wskaźniki" powinien się nazywać "Wskaźniki zad. do oceny" lub coś w tym stylu, samo wskaźniki mało mówi. 
      - Póki co niech będą defaultowo wyłączone
      - Zmień ich styl na bardziej spójny z resztą np czarne/szare kółka lub żółte cyfry. Obecnie wyglądają zbyt nachalnie.
      - na telefonie powinny być:
        - ALBO: niewidzialne, wtedy opcja w menu powinna być szara z wybranym
        - ALBO: widoczne przyklejone do prawej strony z lekkim marginesem. powinny też być odpowiednio małe aby nie zasłaniały treści.

    - Czy zmiena wielkości okienka PDF w każdym rogu i krawędzi byłaby skomplikowana do implementacji

    - Strona na telefonie wygląda jakby była przybliżona (troche jakby na komputerze naklikać Ctrl + = albo Ctrl + ScrollUP) ale może to jest tylko u mnie.

  - "Pokaż potrzebne wzory" powinien mieć możliwośc wyboru wielu podpunktów?, kropek?, a formulasPage w zadaniach powinien się zmienić na formulasPages (s na końcu). Powinno być wiele lokacji wzorów do przywołania pod jednym zadaniem. 
    - Zad 9. dopisać str 7 (wyróżnik Δ, obok już wpisanej str 8 ze wzorem na x1,x2)
    - Zad 11. dopisać str 16 (pole trójkąta [10.4])
    - Zad 17. dopisać str 18 (podzadania 17.1/17.2 mają już str 11)
    - Zad 19. dopisać str 20 (pole trapezu [10.17], obok już wpisanej str 17 z podobieństwem trójkątów)
    - Zad 24. dopisać str 27 (jest tam rysunek ostrosłupa, obok już wpisanej str 11 z tangensem)
    - Zad 30. dopisać str 26 (pole całkowite prostopadłościanu [12.2], obok już wpisanej str 8 z wierzchołkiem paraboli)


  - Przycisk "Rozwiązanie" w przypadku wielu rozwiązań powinien nazywać się "Rozwiązania" i mieć możliwość również rozwinięcia listy różnych rozwiązań: Zwykłe, Krok po kroku, Interaktywne
  Każdy z tych elementów byłby przyciskiem. 
    - Domyślnie: gdy istnieje rozwiązanie "krok po kroku" to "zwykłe" powinno być zwinięte i vice versa
    - Możliwość zmiany powyższego w ustawieniach: "Widoczność zwykłego rozwiązania: gdy brakuje krok po kroku, zawsze, nigdy

  - Przycisk "Zresetuj ustawienia" z popup-em do potwierdzenie. Podświetlajacy się na czerwono po najechaniu i widoczny na dole side panelu aby przypadkiem go nie kliknąć.
  - Wsparcie, donate-y itd.

    - W index.html dodać sekcję o autorze i link do Patronite
    - Na githubie w ustawieniach repo też można coś podpiąć chyba ale trzeba sprawdizć czy byłoby to fair.

  - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

  - Funkcjonalność otwierania tablicy wzorów w nowej karcie oraz Dodać przełącznik "miejsce otwarcia: nowa karta / wew. okienko" pod "Otwórz tablice wzorów"

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

    - Po najbliższym Rebuild Container: zalogować się raz `gh auth login` — od teraz `~/.config/gh` siedzi w wolumenie `matematykazen-gh-config` i przeżywa przebudowy.

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

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ patrz done/README.md i CLAUDE.md.)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.
  Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

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

