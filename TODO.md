Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.

  - Punktacja przy zadaniach może być przesunięta troszeczke w lewo (o 40px), bliżej zadań.


<br>


+ NIE REALIZUJ

  + UI
    - Przycisk "Rozwiązanie" w przypadku wielu rozwiązań powinien nazywać się "Rozwiązania" i mieć możliwość również rozwinięcia listy różnych rozwiązań: Zwykłe, Krok po kroku, Interaktywne... i każde z nich powinno mieć możliwość 
    (Okno "Zaznacz co masz w rozwiązaniu" spoilujące rozwiązanie — rozwiązane przy okazji redesignu zadań otwartych wyżej: box jest domyślnie zwinięty.)


    - Menu / Panel boczny:
      - Swipe/Przesunięcie w lewo powinno zwijać panel boczny (tylko na telefonie)
      - Przełączniki w stylu Motyw, Poprawność itd. są zbyt blade i wyglądają na nieaktywne/zablokowane
      - w trybie egzaminu Poprawność powinna być tak samo nieaktywna/zablokowana ja Punktacja
      - stan przełączników (np. ciemny, jasny, wł., wył., wszystko itd.) chyba jest napisany zbyt tłustą czcionką czy coś. Wyrazy wadają się nieostre, mają jakby bleeding/bloom effect.
      - Panel boczny: „Sprawdź wszystkie odpowiedzi" (#sprawdz-wszystkie) znika/pojawia się przy przełączaniu „Poprawność odpowiedzi" (natychmiast ↔ po „sprawdź") - panel przez to „skacze". Ma być zawsze widoczny: aktywny w „po sprawdź", wyszarzony/disabled w „natychmiast" — tak jak już jest zrobione w trybie egzaminu (setExamMenuDisabled w app/exam.js, można wzorować mechanizm). Potwierdzone na żywo 2026-07-27 przy okazji testów v0.08; ten sam temat co niżej w „INNE NOTATKI" (~linia 51) — jeden wpis wystarczy, ten wyżej jest teraz aktualny.

    - Spójność UI, sesja 2 (jeszcze NIE zrobione, ciąg dalszy sesji 1 [ZROBIONE 2026-07-27], było przydzielone dla Sonnet High). Szczegóły: issues/ui-spojnosc-etap2.md
      - Sesja 1 [ZROBIONE 2026-07-27] + 3 Twoje drobnice (cienie sidebara, ciemniejszy tekst przycisku stopki, tytuł 32%) — patrz done/03-2026-07-27.md i done/04-biezace.md. Do sprawdzenia na żywo (v0.07): stopka, przełącznik w obu motywach, panele PDF, kreska i strzałka sidebara, tytuł arkusza na telefonie.
      - 4 różne rozmiary fontu na karcie zadania — ujednolicić
      - Przyciski odpowiedzi (ABCD, P/F, punkty) bez podświetlenia na hover
      - Dwa różne style hover w menu (ramka vs tło) — wybrać jeden
      - Cień okienka podsumowania egzaminu wpisany na sztywno zamiast jako token
      - Dwa miejsca z ramką 2px zamiast standardowej 1px
      - Okienko podsumowania egzaminu bez zaokrąglonych rogów (reszta strony ma)
      - Marginesy bez spójnej skali (10/16/20/40/50/60/70/80px) — do sprawdzenia ostrożnie, na zrzutach
      - Karta zadania bez ramki/zaokrąglenia, reszta strony już zaokrąglona — decyzja Henricha
      - Landing i arkusz mają różne rozmiary fontu dla podobnych elementów + do sprawdzenia kontrast WCAG (issues/dark-mode-css-zmienne-landing.md)


<br>


+ TESTOWANIE HENRICH:

  Paczka z 2026-08-06 (Opus 5 Medium) — sprawdzone przeze mnie w headless Chromium (oba arkusze,
  oba motywy, 1400px i 390px), ale warto przeklikać na żywo, zwłaszcza na telefonie. Szczegóły
  zmian: done/04-biezace.md.

  - Widżety w ciemnym motywie: otwórz rozwiązania zadań z widżetem (1, 5, 9, 10, 12.1, 15, 18, 20, 30)
    i sprawdź, czy osie/liczby/opisy są czytelne na ciemnym płótnie. Potem PRZEŁĄCZ motyw przy
    otwartym widżecie — ma się przemalować od razu, bez odświeżania strony (także przy „auto",
    gdy zmienisz motyw systemu).

  - Wiersz przycisków pod zadaniem: Podpowiedź / Rozwiązanie / Zgłoś błąd / Pokaż wzory — czy
    kolejność i wygląd Ci pasują. Sprawdź zadanie BEZ wzorów (np. 8) i wyłącz „Zgłoś błąd pod
    zadaniem" w panelu bocznym — wiersz ma się rozłożyć równo na to, co zostało. Na telefonie
    przyciski łamią się po dwa w rzędzie.

  - Formularz zgłoszenia błędu: czy nadal otwiera się w karcie zadania nad tym wierszem i czy
    ponowne kliknięcie go zwija.

  - Zadania otwarte (główna zmiana): boks „Sprawdź obliczenia" ma być domyślnie ZWINIĘTY.
    Zaznaczanie kryteriów od razu podbija punkty zadania i sumę u góry; odznaczanie obniża.
    Sprawdź zad. 9 (kryterium warte 0 pkt zostaje szare) i zad. 19 lub 30 (4 kryteria).
    Po odświeżeniu strony punkty i zaznaczenia mają wrócić.

  - Zadania otwarte, czy treść kryteriów jest dla Ciebie OK merytorycznie — pisałem je jako
    kolejne progi z klucza CKE, alternatywy sklejone słowem „lub". Przy zadaniach 4-punktowych
    trzeba zaznaczyć wszystkie osiągnięte progi, żeby dostać komplet (patrz uwaga w moich
    notatkach na dole pliku).

  - Tryb egzaminu: boks „Sprawdź obliczenia" ma być niewidoczny w trakcie egzaminu, a po
    zakończeniu — komunikat w podsumowaniu odsyła teraz do tego boksu, nie do przycisków punktów.
    Wskaźniki „oceń się": kropka gaśnie po ROZWINIĘCIU boksu (nawet bez zaznaczeń — brak zaznaczeń
    to też ocena, na 0 pkt). Powiedz, jeśli wolisz inny warunek.


<br>


+ DLA HENRICHA:

  - Wykminić, jak zrobić grafiki do zadań do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

  - Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

  - pokminić sobie dydaktycznie nad arkuszem aby zadać robotę Fable
  
<br>


+ INNE NOTATKI, DO PRZEKMINIENIA:

  - "Pokaż potrzebne wzory" powinien mieć możliwośc wyboru wielu podpunktów?, kropek?, a formulasPage w zadaniach powinien się zmienić na formulasPages (s na końcu). Powinno być wiele lokacji wzorów do przywołania pod jednym zadaniem. 
    - Zad 9. dopisać str 7 (wyróżnik Δ, obok już wpisanej str 8 ze wzorem na x1,x2)
    - Zad 11. dopisać str 16 (pole trójkąta [10.4])
    - Zad 17. dopisać str 18 (podzadania 17.1/17.2 mają już str 11)
    - Zad 19. dopisać str 20 (pole trapezu [10.17], obok już wpisanej str 17 z podobieństwem trójkątów)
    - Zad 24. dopisać str 27 (jest tam rysunek ostrosłupa, obok już wpisanej str 11 z tangensem)
    - Zad 30. dopisać str 26 (pole całkowite prostopadłościanu [12.2], obok już wpisanej str 8 z wierzchołkiem paraboli)

  + UI:

    - "Wskaźniki" (oceń się):
      - Przycisk "Wskaźniki" powinien się nazywać "Wskaźniki zad. do oceny" lub coś w tym stylu, samo wskaźniki mało mówi. 
      - Póki co niech będą defaultowo wyłączone
      - Zmień ich styl na bardziej spójny z resztą np czarne/szare kółka lub żółte cyfry. Obecnie wyglądają zbyt nachalnie.
      - na telefonie powinny być:
        - ALBO: niewidzialne, wtedy opcja w menu powinna być szara z wybranym
        - ALBO: widoczne przyklejone do prawej strony z lekkim marginesem. powinny też być odpowiednio małe aby nie zasłaniały treści.

      - Czy zmiena wielkości okienka PDF w każdym rogu i krawędzi byłaby skomplikowana do implementacji

      - Strona na telefonie wygląda jakby była przybliżona (troche jakby na komputerze naklikać Ctrl + = albo Ctrl + ScrollUP) ale może to jest tylko u mnie.

    - Przycisk "Sprawdź wszystkie odpowiedzi" powinien być umieszczony jako podpunkt pod "Poprawność"?

    - Do sekcji „oceń się" z checkboxami powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu, jak to skomponować, aby miało sens. (Częściowo załatwia to zwijany box z DO ZROBIENIA — wrócić do tematu po tamtej zmianie.)


  + ULEPSZANIE WORKFLOW (skopiowane z NOTATKI_USERA)
    - Schedule adversarial review lub /code-review
    - Stworzyć/pobrać potrzebne mi skille do tego projektu
    - uruchomienie całego VS Code w Dev Container (Docker) z uwagi, że /sandbox coś nie działa chyba w rozszerzeniu Claude Code


  - W index.html dodać sekcję o autorze i link do Patronite

  - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)
  
  - Dodać link do licencji widoczny w stopce czy coś. i jakiś copyright (czy left)czy coś

  - Po kliknięciu prevStepButton animacja powinna odpalać się od tyłu (jeżeli to możliwe aby odtwarzać animacje od tyłu, można też renderować każdą od tyłu)

  - Funkcjonalność otwierania tablicy wzorów w nowej karcie o raz Dodać przełącznik "miejsce otwarcia: nowa karta / wew. okienko" pod "Otwórz tablice wzorów"


<br>


+ DOPISANE PRZEZ CLAUDA
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

  + SONNET DOPISAŁ:

    - Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie" (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

    - Formularz zgłoszenia na telefonie jest wysoki: 8 pigułek kategorii idzie po jednej na wiersz (~340 px), więc obowiązkowe pole opisu jest daleko w dole. Do rozważenia: dwie pigułki w rzędzie, skrócone nazwy albo opis nad kategoriami. (nie ma dramatu, jest w miare ok)


  + OPUS DOPISAŁ (Opus 5, medium):

    - Gdy Henrich zdecyduje się upublicznić imię i nazwisko, trzeba podmienić pseudonim `Henrich2137` na dane osobowe w dwóch miejscach: `LICENSE.md` (linie 1–2: copyright + Required Notice) i `CONTRIBUTING.md` (punkt 2 zgody na licencjonowanie wkładu). CLA na pseudonim jest słabsze dowodowo niż na nazwisko.

    - Gdy ruszy domena matematykazen.pl, podmień URL w `LICENSE.md:2` (Required Notice — ta linia jest kopiowana przez każdego redystrybutora) i `README.md`; w OVERVIEW.md domena jest już opisana jako plan Fazy 2.


  + OPUS DOPISAŁ (Opus 5, high) — devcontainer, 2026-08-06:

    - Sprawdzić nowy devcontainer na Kubuntu/Dockerze. Zmiany testowałem tylko pod rootless podmanem na Bazzite; `docker exec --privileged` działa tak samo, ale nie miałem jak tego odpalić.

    - VS Code wpuszcza do kontenera socket ssh-agenta, gpg-agenta, X11 i Waylanda oraz podpina git credential helper hosta — omija to firewall (to nie jest ruch sieciowy). Wyłączalne tylko częściowo: `dev.containers.mountWaylandSocket: false` i `dev.containers.gitCredentialHelperConfigLocation: "none"` (uwaga: to drugie zabierze pushowanie po HTTPS bez tokena w kontenerze). Dla ssh-agenta i X11 rozszerzenie nie ma przełącznika — sprawdziłem package.json wersji 0.463.0.

    - `sudo` w kontenerze przestało działać (świadomie, `--cap-drop=ALL` bez wyjątków). Jeśli okaże się potrzebne do czegoś realnego, trzeba dodać `--cap-add=SETUID --cap-add=SETGID` — ale NIE `NET_ADMIN`, bo to znów pozwoli rozbroić firewall od środka.

    - Świadomie NIEdomknięte dziury w firewallu, do ewentualnej decyzji: (1) brama `/32` jest przepuszczona, więc z kontenera widać panel WWW routera — zostawione, bo zawężanie tego groziło zepsuciem DNS; (2) dozwolone domeny (GitHub, npm) są z natury kanałem na dane — nie da się usunąć bez odcięcia gita.


  + OPUS DOPISAŁ (Opus 5, medium) — po paczce z 2026-08-06:

    - Zadania otwarte bez `gradingCriteria` w danych nadal renderują stare przyciski „0..N pkt" (awaryjna ścieżka w app/render.js). Dziś takich zadań nie ma — przy wpinaniu NOWEGO arkusza trzeba pamiętać o kryteriach, inaczej zadanie po cichu wróci do starego UI.

    - `finalAnswer.label` w exercises.json nie ma już odbiorcy (renderer je ignoruje). Zostawione we wszystkich arkuszach — do decyzji, czy kiedyś wyczyścić dane.

    - Kryteria dla zadań 4-punktowych są kaskadą progów z klucza CKE, więc uczeń, który zaznaczy tylko „poprawny wynik", dostanie 1 pkt zamiast 4. Do przemyślenia, czy zaznaczenie wyższego progu nie powinno automatycznie zaznaczać niższych.

+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod done/ — patrz done/README.md i CLAUDE.md.)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo done/, a tu zostaje jedna linijka z odnośnikiem.
  Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DO REALIZACJI Dopisane przez CLAUDA napisz jakim modelem jesteś i na jakim efforcie, Jeżeli czytasz notatki np Sonneta na low to ufaj im mniej niż tym zrobionym przez Opusa na High
