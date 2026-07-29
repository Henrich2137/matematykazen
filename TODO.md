Oto plik który tworzy Henrich (ja, użytkownik).

+ DO ZROBIENIA
<br> Jeżeli nie masz co robić, to rób stąd.

  - Watermark kodu?


<br>


+ NIE REALIZUJ

  + UI
    
    - Okno typu "Zaznacz co masz w rozwiązaniu" (np w zad 9.) powinno być jakoś schowane bo podpowiada, spoiluje uczniowi na starcie co ma zrobić.

    - Tło w niektórych widżetach jest białe w motywie darkmode. Należy zmienić kolory na taki które będą się zgadzać z motywem.

    - Przycisk zgłoś błąd powinien wyglądać podobnie do light buttonów

    - Punktacja przy zadaniach może być przesunięta troszeczke w lewo, bliżej zadań.

    - Zmienić tekst w przycisku "Pokaż potrzebne wzory" na "Pokaż wzory" lub "Potrzebne wzory".
      
    - Zadania otwarte, naliczanie punktów:
      - zamiast checkboxów powinny być przyciski z punktami do każdego zdania typu "Nierówność zapisana w postaci x2−6x−7≤0x2−6x−7≤0" (przykład z zad 9.) Dokładna punktacja jest w zasadach oceniania w pdf i od tego powinna zależeć ilość przycisków. (czeka na decyzję merytoryczną Henricha o punktacji za poszczególne przyciski, potem do przydzielenia modelowi)
      - ostateczna odpowiedź w zadaniach takich jak 8. i 9. po sprawdzeniu powinny być przyznane punkty użytkownikowi i automatycznie zaznaczony przycisk punktów

    - Menu / Panel boczny:
      - Swipe/Przesunięcie w lewo powinno zwijać panel boczny (tylko na telefonie)
      - Przełączniki w stylu Motyw, Poprawność itd. są zbyt blade i wyglądają na nieaktywne/zablokowane
      - w trybie egzaminu Poprawność powinna być tak samo nieaktywna/zablokowana ja Punktacja
      - stan przełączników (np. ciemny, jasny, wł., wył., wszystko itd.) chyba jest napisany zbyt tłustą czcionką czy coś. Wyrazy wadają się nieostre, mają jakby bleeding/bloom effect.
      - toggle wł/wył panel boczny powinien mieć zamienione ikonki strazłki zwiń/rozwiń
      - Panel boczny: „Sprawdź wszystkie odpowiedzi" (#sprawdz-wszystkie) znika/pojawia się przy przełączaniu „Poprawność odpowiedzi" (natychmiast ↔ po „sprawdź") - panel przez to „skacze". Ma być zawsze widoczny: aktywny w „po sprawdź", wyszarzony/disabled w „natychmiast" — tak jak już jest zrobione w trybie egzaminu (setExamMenuDisabled w app/exam.js, można wzorować mechanizm). Potwierdzone na żywo 2026-07-27 przy okazji testów v0.08; ten sam temat co niżej w „INNE NOTATKI" (~linia 51) — jeden wpis wystarczy, ten wyżej jest teraz aktualny.

    - Spójność UI, sesja 2 (jeszcze NIE zrobione, ciąg dalszy sesji 1 [ZROBIONE 2026-07-27], było przydzielone dla Sonnet High). Szczegóły: issues/ui-spojnosc-etap2.md
      - Sesja 1 [ZROBIONE 2026-07-27] + 3 Twoje drobnice (cienie sidebara, ciemniejszy tekst przycisku stopki, tytuł 32%) — patrz DONE/03-2026-07-27.md i DONE/04-biezace.md. Do sprawdzenia na żywo (v0.07): stopka, przełącznik w obu motywach, panele PDF, kreska i strzałka sidebara, tytuł arkusza na telefonie.
      - 4 różne rozmiary fontu na karcie zadania — ujednolicić
      - Przyciski odpowiedzi (ABCD, P/F, punkty) bez podświetlenia na hover
      - Dwa różne style hover w menu (ramka vs tło) — wybrać jeden
      - Przyciski Podpowiedź/Rozwiązanie/Wzory łamią się na telefonie (sztywne 30% szerokości)
      - Samoocena na telefonie: 5 przycisków układa się krzywo (2+2+1)
      - Cień okienka podsumowania egzaminu wpisany na sztywno zamiast jako token
      - Dwa miejsca z ramką 2px zamiast standardowej 1px
      - Okienko podsumowania egzaminu bez zaokrąglonych rogów (reszta strony ma)
      - Marginesy bez spójnej skali (10/16/20/40/50/60/70/80px) — do sprawdzenia ostrożnie, na zrzutach
      - Karta zadania bez ramki/zaokrąglenia, reszta strony już zaokrąglona — decyzja Henricha
      - Landing i arkusz mają różne rozmiary fontu dla podobnych elementów + do sprawdzenia kontrast WCAG (issues/dark-mode-css-zmienne-landing.md)


<br>


+ TESTOWANIE HENRICH:
  - nic


<br>


+ DLA HENRICHA:

  - Wykminić, jak zrobić grafiki do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

  - Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.


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

    - Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

    - Do sekcji „oceń się" z checkboxami powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu, jak to skomponować, aby miało sens.
    
    - W index.html dodać sekcję o autorze i link do Patronite




<br>


+ DOPISANE PRZEZ CLAUDA
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

  + SONNET DOPISAŁ:

    - Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie" (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

    - Formularz zgłoszenia na telefonie jest wysoki: 8 pigułek kategorii idzie po jednej na wiersz (~340 px), więc obowiązkowe pole opisu jest daleko w dole. Do rozważenia: dwie pigułki w rzędzie, skrócone nazwy albo opis nad kategoriami. (nie ma dramatu, jest w miare ok)


+ ZASADY DLA CLAUDE-A:

  - tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)

  - TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
  Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

  - Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

  - Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

  - Robiąc notatki w sekcji DO REALIZACJI Dopisane przez CLAUDA napisz jakim modelem jesteś i na jakim efforcie, Jeżeli czytasz notatki np Sonneta na low to ufaj im mniej niż tym zrobionym przez Opusa na High