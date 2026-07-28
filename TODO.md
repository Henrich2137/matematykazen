Oto plik który tworzy Henrich (ja, użytkownik).

DO REALIZACJI
<br> Jeżeli nie masz co robić, to rób stąd.

- nic


NIE REALIZUJ

- Panel boczny: „Sprawdź wszystkie odpowiedzi" (#sprawdz-wszystkie) znika/pojawia się przy przełączaniu
  „Poprawność odpowiedzi" (natychmiast ↔ po „sprawdź") — panel przez to „skacze". Ma być zawsze widoczny:
  aktywny w „po sprawdź", wyszarzony/disabled w „natychmiast" — tak jak już jest zrobione w trybie
  egzaminu (setExamMenuDisabled w app/exam.js, można wzorować mechanizm). Potwierdzone na żywo
  2026-07-27 przy okazji testów v0.08; ten sam temat co niżej w „INNE NOTATKI" (~linia 51) — jeden
  wpis wystarczy, ten wyżej jest teraz aktualny.


Sonnet High:
Spójność UI, sesja 2 (jeszcze NIE zrobione — sprawdzone 2026-07-28, kod bez zmian od sesji 1). Sesja 1 była [ZROBIONE 2026-07-27], to jest jej ciąg dalszy. Każdy punkt niżej ma dokładniejszy opis (plik/linia/mechanizm) w issues/ui-spojnosc-etap2.md:

- W treści zadania są 4 różne rozmiary fontu na jednej karcie (odpowiedzi 18px, samoocena/pola 17px, textarea 16px) i różne paddingi. Ujednolicić do 2-3 stałych rozmiarów.

- Przyciski odpowiedzi (ABCD, prawda/fałsz, punkty samooceny) nie podświetlają się przy najechaniu myszką — reszta strony (pigułki, sidebar) tak. Dodać obramowanie przy hover.

- W różnych miejscach hover działa inaczej: raz przez ramkę (narożniki, panele), raz przez tło (sidebar). Ustalić jeden wzorzec i się go trzymać.

- Przyciski „Podpowiedź / Rozwiązanie / Pokaż potrzebne wzory" mają sztywną szerokość 30% każdy — na telefonie (390px) trzeci się łamie na 3 linie i wiersz wygląda krzywo.

- Na telefonie 5 przycisków samooceny „0-4 pkt" układa się nierówno: 2 + 2 + 1 z samotnym ostatnim na środku. Zrobić równą siatkę.

- Okienko podsumowania egzaminu i kropki wskaźników mają cień wpisany na sztywno zamiast użyć wspólnego tokenu — jeśli ma zostać mocniejszy cień niż reszta, nazwać go (`--shadow-modal`) zamiast wpisywać wartość w miejscu.

- Dwa miejsca nadal mają ramkę 2px zamiast standardowej 1px: przycisk „ukryj wskaźniki" i dolna linia pod rozwiązaniem krok po kroku. (W widżetach 2px zostaje celowo, tam koduje kolor.)

- Okienko podsumowania egzaminu jako jedyna „karta" na stronie ma ostre rogi zamiast zaokrąglonych jak wszędzie indziej.

- Marginesy w pasku/stopce/sekcjach to dziś przypadkowy zestaw wartości (10/16/20/40/50/60/70/80px) bez żadnej skali. Sprawdzić czy da się to ułożyć w spójny rytm — ale TYLKO po porównaniu zrzutów przed/po, bo to najbardziej widoczna wizualnie zmiana z całej listy.

- Karta zadania (całe zadanie na stronie) jest bez ramki i zaokrąglonych rogów, a wszystko dookoła po sesji 1 już jest zaokrąglone — sprawdzić czy przez to nie wygląda jak obcy element. Zmiana czysto kosmetyczna i odwracalna, decyzja należy do mnie (Henrich).

- Strona główna (landing) i sam arkusz mają różne rozmiary czcionek dla podobnych elementów (np. przycisk CTA 18px, nagłówek karty 17px, treść arkusza 16px) — ujednolicić. Przy okazji sprawdzić kontrast kolorów (WCAG) w zmiennych landingu, patrz issues/dark-mode-css-zmienne-landing.md.


Do przydzielenia:

- Zadania otwarte, naliczanie punktów:
  - zamiast checkboxów powinny być przyciski z punktami do każdego zdania typu "Nierówność zapisana w postaci x2−6x−7≤0x2−6x−7≤0" (przykład z zad 9.) Dokładna punktacja jest w zasadach oceniania w pdf i od tego powinna zależeć ilość przycisków. (czeka na decyzję merytoryczną Henricha o punktacji za poszczególne przyciski, potem do przydzielenia modelowi)
  - ostateczna odpowiedź w zadaniach takich jak 8. i 9. po sprawdzeniu powinny być przyznane punkty użytkownikowi i automatycznie zaznaczony przycisk punktów

- Tło w niektórych widżetach jest białe w motywie darkmode. Należy zmienić kolory na taki które będą się zgadzać z motywem.

- Przycisk zgłoś błąd powinien wyglądać podobnie do light buttonów

- Przesunięcie w lewo powinno zwijać panel boczny (tylko na telefonie)

<br>

TESTOWANIE HENRICH:
- telefon 2024 - wczytuje zadania ale wyświetla błąd. (issues/zadania-nie-renderuja-sie-mobile.md)

DLA HENRICHA:

- Obczaić analitykę, czyli śledzenie ilości i zaangażowania użytkowników. Warto rozważyć GoatCounter.

- Wykminić, jak zrobić grafiki do dark mode, można np. masowo odwrócić kolory i zmienić krzywą tak, aby zamiast czarnego tła był odpowiedni kolor szarego. (Tańszy tymczasowy fix: CSS filter na `.question img`/wideo — patrz issues/dark-mode-obrazki-wideo.md)

- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.


<br>


INNE NOTATKI, DO PRZEKMINIENIA:
- "Wskaźniki" (oceń się):
  - Przycisk "Wskaźniki" powinien się nazywać "Wskaźniki zad. do oceny" lub coś w tym stylu, samo wskaźniki mało mówi. 
  - Póki co niech będą defaultowo wyłączone
  - Zmień ich styl na bardziej spójny z resztą np czarne/szare kółka lub żółte cyfry. Obecnie wyglądają zbyt nachalnie.

- Czy zmiena wielkości okienka PDF w każdym rogu i krawędzi byłaby skomplikowana do implementacji

- Strona na telefonie wygląda jakby była przybliżona (troche jakby na komputerze naklikać Ctrl + = albo Ctrl + ScrollUP) ale może to jest tylko u mnie.

- Przycisk "Sprawdź wszystkie odpowiedzi"
  - Powinien być cały czas widoczny. Gdy "Poprawność" jest ustawiona na 'po "sprawdź"' to powinien się uaktyniać, a gdy "natychmiast" to być szary, nieaktywny. Nie chcę aby menu skakało po przełączaniu "Poprawność"
  - Opcjonalnie: powiniowinien być umieszczony jako podpunkt pod "Poprawność"

- W trybie egzaminy "Punktacja" powinna pokazywać wył. ale pod spodem pamiętać to co było ustawione w ćwiczeniach. Nie powinno być widać punktów na egzaminie 

- wskaźniki "oceń się" na telefonie powinny być:
  - ALBO: niewidzialne, wtedy opcja w menu powinna być szara z wybranym
  - ALBO: widoczne przyklejone do prawej strony z lekkim marginesem. powinny też być odpowiednio małe aby nie zasłaniały treści.

- Przekminić i dodać zasadę dotyczącą tłumaczenia mi (Henrichowi) rzeczy (jak mam przeprowadzić test, jak wygląda projekt itd.)

- dodanie rozwiązań do matury 2026

- Na telefonie pdfy się nie ładują (tablica i zasady oceniania). (to nie będzie problem po zmianie na pdf otwierane na zewnątrz stronki, jeśli tamto będzie działać to można usunąć ten wpis)
  - Podczas naprawy warto sprawić, aby odpalały się one nie w okienku, ale wypełniały całą stronę z krzyżykiem w rogu.
  - Jeżeli nie uda się tego naprawić, to należy usunąć tę funkcjonalność z wersji mobilnej.

- Do sekcji „oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu, jak to skomponować, aby miało sens.

- Pokminić nad kolejnością przycisków w menu

- W index.html dodać sekcję o autorze i link do Patronite


<br><br>


<h3>DO REALIZACJI Dopisane przez CLAUDA</h3>
Szczegóły (pliki, linie, mechanizm) każdego punktu są w issues/ — patrz issues/README.md.

SONNET DOPISAŁ:
- Uzupełnić `formulasPage` w 2024-grudzień — brakuje w zad. 7, 8, 10, 11, 12, 20 (6 z 35), więc nie mają przycisku „Pokaż potrzebne wzory". Do decyzji merytorycznej: część pewnie faktycznie nie wymaga tablic, ale zad. 8 (otwarte) warto sprawdzić.

- Tryb testowy dla zgłaszania błędów (app/report.js): przycisk „Wyślij zgłoszenie" zamieniony na „Wyślij zgłoszenie lokalnie" (np. pod `?test-zgloszenie=1`, wzorem `?test-egzamin=1`), który loguje payload do konsoli/localStorage zamiast robić fetch do Formspree — żeby testować całą ścieżkę (walidacja, honeypot, throttling, toast) bez zużywania miesięcznego limitu 50 zgłoszeń.

- Formularz zgłoszenia na telefonie jest wysoki: 8 pigułek kategorii idzie po jednej na wiersz (~340 px), więc obowiązkowe pole opisu jest daleko w dole. Do rozważenia: dwie pigułki w rzędzie, skrócone nazwy albo opis nad kategoriami.

- Link „zgłoś błąd" jest na samym dole karty, a formularz otwiera się nad przyciskami Podpowiedź/Rozwiązanie — czyli powyżej miejsca kliknięcia. Działa, ale warto sprawdzić na żywo, czy ten skok nie dezorientuje; ewentualnie doscrollować formularz do widoku po otwarciu.


ZASADY dla Ciebie Claude:

- tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do bieżącego pliku pod DONE/ — patrz DONE/README.md i CLAUDE.md.)

- TEN PLIK MA BYĆ SLEEK — krótkie hasła, jedno-dwa zdania na punkt. Żadnych ścian tekstu. Szczegóły (mechanizm, pliki, linie) idą do issues/ albo DONE/, a tu zostaje jedna linijka z odnośnikiem.
 Drogi Claudzie, jeżeli zmieniasz ten plik to wklejaj do odpowiedniej sekcji na dole

- Zawsze sprawdzaj, testuj czy wprowadzone przez ciebie zmiany działają zanim zrobisz ostatni commit.

- Zadania powinny być oddzielone pustą linijką, chyba, że są to podzadania i składają się na jedno duże zadanie.

- Robiąc notatki w sekcji DO REALIZACJI Dopisane przez CLAUDA napisz jakim modelem jesteś i na jakim efforcie, Jeżeli czytasz notatki np Sonneta na low to ufaj im mniej niż tym zrobionym przez Opusa na High