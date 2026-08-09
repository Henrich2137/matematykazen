Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.

  - Paczka drobiazgów UI (hover panelu / kontrolki odpowiedzi na telefonie / dark mode
    grafik) — omówione i doprecyzowane w rozmowie z Sonnetem, spec:
    [docs/superpowers/specs/2026-08-09-paczka-ui-drobiazgi-design.md](docs/superpowers/specs/2026-08-09-paczka-ui-drobiazgi-design.md).

    - Usunąć dynamiczny podgląd „wartość → następna" (np. „wszystkie → wypełnione") z hoveru
      przycisków panelu (Wskaźniki/Punktacja/Motyw), bo odejmuje intuicyjności — Henrich, v14.
      Zamiast tego obecnie wybrana opcja ma być widoczna cały czas, niezależnie od hoveru.
      (`.wartosc-podglad`, `app/state.js:91-100`)
      Kod archiwizowany w issues/, nie po prostu skasowany.

    - Kontrolki odpowiedzi (pole „ostateczna odpowiedź"/fill-in, przyciski P/F) na telefonie:
      NIE zwykłe zmniejszenie szerokości/marginesów — pivot na layout pionowy (treść nad,
      kontrolka pod), z mniejszym marginesem z lewej i przesunięciem w prawo/mniejszym
      marginesem z prawej. Szczegóły w spec.

    - Zrobić grafiki do zadań do dark mode: pełne odwrócenie kolorów (świadomie zaakceptowany
      kompromis — kolorowe elementy wyjdą w zamienionych barwach), dotyczy też wideo.
      Startowa wartość filtra wyliczana z jasności `--bg`, potem dostrojona empirycznie.
      (Tańszy tymczasowy fix opisany też w issues/dark-mode-obrazki-wideo.md.)

    - Przycisk "Sprawdź wszystkie odpowiedzi" powinien być umieszczony jako podpunkt pod "Poprawność"? (podobnie jak to wygląda z opcjami dot. trybu egzaminu)

    - Formularz zgłoszenia na telefonie jest wysoki: 8 pigułek kategorii idzie po jednej na wiersz (~340 px), więc obowiązkowe pole opisu jest daleko w dole. Do rozważenia: dwie pigułki w rzędzie szczególnie te gdzie są krótkie nazwy. Nie przekombinuj tego. zrób tak aby na pewno działało, nie musi być idealnie. Niektóre pigułki mogą być po prostu mniejsze czy coś.

<br>


+ NIE REALIZUJ

  - nic


<br>


+ TESTOWANIE HENRICH:

  - nic


<br>


+ DLA HENRICHA:

  - Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

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

  - Przycisk "Rozwiązanie" w przypadku wielu rozwiązań powinien nazywać się "Rozwiązania" i mieć możliwość również rozwinięcia listy różnych rozwiązań: Zwykłe, Krok po kroku, Interaktywne
  Każdy z tych elementów byłby przyciskiem. 
    - Domyślnie: gdy istnieje rozwiązanie "krok po kroku" to "zwykłe" powinno być zwinięte i vice versa
    - Możliwość zmiany powyższego w ustawieniach: "Widoczność zwykłego rozwiązania: gdy brakuje krok po kroku, zawsze, nigdy

  - Przycisk "Zresetuj ustawienia" z popup-em do potwierdzenie. Podświetlajacy się na czerwono po najechaniu i widoczny na dole side panelu aby przypadkiem go nie kliknąć.
  - Wsparcie, donate-y itd.

    - W index.html dodać sekcję o autorze i link do Patronite
    - Na githubie w ustawieniach repo też można coś podpiąć chyba ale trzeba sprawdizć czy byłoby to fair.

  - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

  - Po kliknięciu prevStepButton animacja powinna odpalać się od tyłu (jeżeli to możliwe aby odtwarzać animacje od tyłu, można też renderować każdą od tyłu)

  - Funkcjonalność otwierania tablicy wzorów w nowej karcie oraz Dodać przełącznik "miejsce otwarcia: nowa karta / wew. okienko" pod "Otwórz tablice wzorów"

  - sprawdzić merytorykę arkuszy (na końcu, przed rozpowszechnieniem)

  - wysyłanie całego localStorage przez użytkownika podczas zgłaszania błędu jest a bit scatchy też troche niebezpiczne

<br>


+ DOPISANE PRZEZ CLAUDA
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

  + SONNET DOPISAŁ:

    - Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie" 
      - (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

    


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

    - Świadomie NIEdomknięte dziury w firewallu, do ewentualnej decyzji: (1) brama `/32` jest przepuszczona, więc z kontenera widać panel WWW routera — zostawione, bo zawężanie tego groziło zepsuciem DNS; (2) dozwolone domeny (GitHub, npm) są z natury kanałem na dane — nie da się usunąć bez odcięcia gita.


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

  + FABLE DOPISAŁ (Fable 5, po paczce 4 „Spójność UI etap 2", 2026-08-09):

    - W jasnym motywie --text-faint-2 (#909090, 3.3:1) i --text-faint-3 (#999, 2.8:1) są poniżej WCAG AA (4.5:1) przy 13–14px tekstach (etykiety „miejsce na notatki"/samooceny, uchwyty paneli PDF). Paczka 4 poprawiła tylko --text-faint (mierzone elementy landingu i stopek); te dwa tokeny do decyzji — przyciemnienie zmieni sporo drobnych etykiet naraz.

    - Cienie kropek wskaźników (0 1px 4px w exam.css) świadomie zostały poza tokenem — dwa drobne, powiązane znaczeniowo wystąpienia; tokenizować dopiero, gdyby doszło trzecie.

+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ — patrz done/README.md i CLAUDE.md.)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.
  Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DO REALIZACJI Dopisane przez CLAUDA napisz jakim modelem jesteś i na jakim efforcie, Jeżeli czytasz notatki np Sonneta na low to ufaj im mniej niż tym zrobionym przez Opusa na High
