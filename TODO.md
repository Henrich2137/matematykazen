Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.
  - Usprawnić Rozwiązanie krok po kroku, Ocena po testach:
    - Przycisk start/pauza zawsze powinien odpalać filmik w standardowym kierunku, nie reverse
    - od razu po kliknięciu cofnij powinna podświetlić sie kropka która okresla początek filmiku (ta po lewej, nie po prawej). Obecnie jest tak, że nieraz zaznacza się dopiero po skończonej animacji (jak dojdize do pooczątku filmiku)
    - cały bar (step-dots) tych kropek jest za szeroki, powinien być węższy o ok 20%
    - w zadaniu 3. widać strzałki (step-scroll) mimo, że cały bar (step-dots) się mieśći
    - wszystkie kreseczki (step-link), które są po lewej od kropki obecnego kroku powinny być zapełnione, jasne
    - kliknięcie step-prev i step-next podczas podtwarzania powinno przewijać do początku/początku następnego filmiku aby można było pominąć kroki przejść do następnego

    - Zmień cały styl przycisków steps-nav 
      - start/pauza jest krzywo, zamiast być na środku to jest lekko w lewo i w dół, wyjeb kółko, to nie spotify
      - step-prev i step-next maja zbyt ostre strzałki, daj jakieś inne


  - Zmień styl nazywania podfolderów tego typu z
    2024-grudzien/media/krok-po-kroku/ na 
    2024-grudzien/media/solution-step-by-step/
    zaktualizuj referencje itd.


  - SPRAWDŹ CZY TO NIE JEST JUŻ PRZYPADKIEM ROZWIĄZANE
    - Rozwiązanie krok po kroku — ZOSTAŁO Z TEGO TEMATU (reszta zrobiona w v20, patrz done/04-biezace.md):
      - Sceny zad. 1 i zad. 3 są wciąż w starym kadrze 21:9 (840×360, 60 fps). Odtwarzacz radzi sobie
        z obydwoma formatami naraz (bierze proporcje z pliku), więc to nie pali się — ale dopóki tego
        nie przerobisz, te dwa zadania nie mają zapasu klatek pod spowolnienie 0,25×.
        Po przerenderowaniu trzeba puścić `tools/rewersy.sh` jeszcze raz z `--nadpisz`.
      - Zad. 3 nie ma opisów kroków w danych (7 z 8 kroków ma puste "text"), więc przycisk
        „Pokaż wyjaśnienie kroku" pokazuje się tam tylko na ostatnim kroku.

+ NIE REALIZUJ:

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


+ TESTOWANIE HENRICH:

  - NOWY ODTWARZACZ KROK PO KROKU (v20) — zad. 1, 2 i 3, arkusz grudzień 2024.
    Rewersy są już dla wszystkich trzech zadań, więc ◄ ma czym cofać.

    - KROPKI: jest ich o jedną więcej niż filmów. Sprawdź, czy kropka „obecna" stoi tam, gdzie
      się spodziewasz. PRZYJĄŁEM WERSJĘ B z Twojego rysunku ROW 1, bo dwie linijki rysunku
      przeczą sobie nawzajem: „po skończeniu 3. kroku" masz pełny pasek PO PRAWEJ od O, a
      „po obejrzeniu całości" pełny pasek PO LEWEJ od O. Zrobiłem tak, że gdy film dobiegnie
      końca, O przeskakuje na kropkę po prawej (czyli linijka „po skończeniu 3. kroku"
      wyglądałaby u mnie `o o o~~~O o o`). Jeśli chciałeś odwrotnie — powiedz, to jedna zmiana.
    - Kliknij w dowolną kropkę: ma przenieść do PIERWSZEJ klatki tego kroku i zostawić film
      zatrzymany. Ostatnia kropka = stan końcowy, czyli ostatnia klatka ostatniego filmu.
    - ◄ w środku filmu: ma polecieć od tyłu i zatrzymać się na początku TEGO kroku. ◄ jeszcze
      raz (już na pierwszej klatce): ma cofnąć cały poprzedni krok. Na kropce 0 ◄ jest wyszarzone.
    - Pasek postępu jest teraz między kropkami, nie pod filmem — przy cofaniu ma się OPRÓŻNIAĆ.
    - ROW 2: ◄ / start-pauza w kółku / ►. Kółko jest po to, żeby „odtwórz" (▶) nie wyglądał
      identycznie jak „następny krok" (►). Sprawdź kciukiem, czy trafiasz — mają po 44 px.
    - ROW 3 „Pokaż wyjaśnienie kroku" — pod nim siedzi całe pole "text" (opis + wzór), zgodnie
      z Twoją odpowiedzią. Pod filmem NIE MA już żadnego zawsze widocznego podpisu.
    - Panel boczny → „Prędkość filmów": ¼× ½× 1× 2× 4×. Napisałem ułamkami, bo lista stanów
      rozdziela je przecinkiem i „0,25×" rozpadłoby się na dwa. Zmiana działa od razu na
      odtwarzanym filmie. Przy 4× obraz jest skokowy — to znane i zmierzone, nie usterka.
    - Na telefonie: przesuń palcem po filmie w lewo (następny) i w prawo (poprzedni).
      Na komputerze strzałki ← → na klawiaturze.
    - ZAD. 1 ma 10 kropek, ZAD. 3 ma 9 — powyżej siedmiu włączają się strzałeczki ‹ › po bokach
      paska kropek. Zad. 2 ma dokładnie 7 i strzałek mieć NIE powinno.
    - Dojście do ostatniego kroku NIE zaznacza już poprawnej odpowiedzi (zdjęte, jak prosiłeś).
    - Zad. 1 i 3 mają filmy jeszcze w starym kadrze 21:9. Nie są już wciskane w pudełko 16:9 —
      kadr dopasowuje się do pliku, więc zniknął pas ok. 80 px nad i pod obrazem.

  - CIEMNY MOTYW, osobna poprawka przy okazji: jeśli WYMUSISZ ciemny w panelu bocznym (nie
    „auto"), rysunki i filmy mają być teraz przygaszone tak samo jak przy motywie z systemu.
    Wcześniej przy ręcznym wyborze świeciły na biało — brakowało jednej zmiennej w CSS.
    To najpewniej powód, dla którego punkt o świecącym wideo z v15 mógł wyglądać na niezrobiony.

  - Zadanie 2, arkusz grudzień 2024 (v19) — TEST NOWEGO KADRU. Filmy są teraz 16:9, 1280×720,
    120 fps, a wzory pomocnicze wyszły z kadru do podpisów pod filmem. To jest test SAMEJ
    rozdzielczości i osadzenia filmu — kropek, przycisków i rewersów jeszcze nie ma.

    - Film ma być zauważalnie WIĘKSZY: na komputerze 608×342 zamiast 420×180, na telefonie
      340×191 zamiast 300×129. Na telefonie film wychodzi teraz na całą szerokość karty.
    - Sprawdź, czy kadr nie jest za wysoki na telefonie — czy nawigacja („1 / 6" ze strzałkami)
      mieści się na ekranie razem z filmem, bez przewijania.
    - KROK 1 i KROK 6, po zatrzymaniu się filmu: w kroku 1 ma być widoczny wykładnik \(-5\),
      w kroku 6 wynik \(5^4\). Przeglądarka potrafi zatrzymać obraz kilka klatek przed końcem
      pliku i wtedy gubi ostatni dorysowany element — dołożyłem przytrzymanie stanu końcowego,
      ale to trzeba obejrzeć na prawdziwym telefonie.
    - Pod każdym filmem jest teraz podpis ze wzorem, który wcześniej był animowany w kadrze
      po prawej stronie. Sprawdź, czy się dobrze czyta i czy nie jest za długi.

  - Kontener: firewall + Playwright + read-only `.vscode` (2026-08-10). WYMAGA **Rebuild Container**
    (zwykłego, bez `--no-cache`) — bez tego nic z tego nie zadziała. Po przebudowie, w terminalu
    W KONTENERZE:

    - `dig +short github.com` → ma zwrócić adresy. Jeśli w logu firewalla widać „UWAGA: DNS nie
      działa po zawężeniu", zawężenie bramy poszło źle — patrz `.devcontainer/README.md`,
      sekcja „Diagnostyka".
    - `curl -m 5 http://192.168.1.1` → ma NIE przejść (timeout albo „Connection refused"). Wcześniej
      otwierał panel routera. To samo dotyczy SMB (445) i drukarki (631).
    - `git push` / `npm ping` / `curl -sI https://cke.gov.pl` → mają nadal działać.
    - `bash .devcontainer/verify-firewall.sh` → ma zakończyć się sukcesem.
    - `touch .vscode/test` → ma odbić się o „Read-only file system" (to jest cel, nie błąd).
    - Playwright: `NODE_PATH=/usr/local/share/npm-global/lib/node_modules node -e "require('playwright').chromium.launch().then(b=>b.close()).then(()=>console.log('OK'))"`
      → „OK". Potem zrzut arkusza przez `tools/zrzuty.js`; polski tekst ma być widoczny, nie puste
      prostokąty.

  - VS Code na hoście: przy otwarciu folderu ma się już NIE pytać „Allow Automatic Tasks in Folder?",
    tylko po cichu zrobić `git pull --ff-only`.

  - Backup `~/backup-vscode-flatpak/` (8 kB) po skasowanych danych flatpakowego VS Code — do
    usunięcia, gdy uznasz, że już niepotrzebny. Dwa ustawienia istniały tylko tam i świadomie
    ich nie przeniosłem (`chat.viewSessions.orientation`, `chat.agent.sandbox.enabled`).
    Cały przepis — jak znaleźć takie sieroty i czego przy nich pilnować — w
    `issues/flatpak-osierocone-dane.md`.


<br>


+ DLA HENRICHA:

  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable
  
<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:
  
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

  + ULEPSZANIE WORKFLOW (skopiowane z NOTATKI_USERA)
    - Schedule adversarial review lub /code-review
    - Stworzyć/pobrać potrzebne mi skille do tego projektu
    - wyłączyć skróty które powodują, że przeklikuje pytanie podczas pisania prompta

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
      - `CONTRIBUTING.md` (punkt 2 zgody na licencjonowanie wkładu
      - stopki plikach html

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

+ DO ZROBIENIA HOŚCIE (POZA KONTENEREM)

  - dopisać pythona do extentions aby był też po rebuildzie itd.