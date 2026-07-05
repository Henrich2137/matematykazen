Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)


FABLE, SPRAWDŹ POPRAWNOŚĆ ROZWIĄZAŃ I DAJ FEEDBACK PONIŻEJ CZY AKCEPTUJESZ TE ZADANIA PRZY KAŻDYM Z NICH NAPISZ [OPUS DID WELL] [OPUS DID POORLY] oraz dopisz czy zostało poprawione ZROBIONE PRZEZ OPUSA:

- zad 17.1 rozwiązanie się nie zgadza z treścia zadania chyba

- zad 12 powinno by oddzielone od 12.1 (to zostało np źle zrobione, ponieważ 12 jest jakby wewnątrz 12.1 a ma być zupełnie oddzielny melementem exercises który jest jakby pustym zadaniem, bez odpowiedzi rozwiązań itd. 17 też jest do dupy zrobione, ten sam błąd)

- przyciski w 12.2 nie działają intuicyjnie, trzeba je odklikiwać. Jeżeli uznasz, że jest to proste w implementacji to zrób tak aby ostatni zaznaczony przycisk był tym który automatycznie się odznaczy przy wybraniu nowego. Jeśli uznasz, że to zbyt skomplikuje kod i narazi go na błędy to dodaj lepszą ikonkę zaznaczenia, która będzie sugerować, że trzeba go odznaczyć lub komunikat lub animacje poszerzenia krawędzi która pojawi się po kliknięciu na inną odpowiedź cza, należy albo zmienić to zadanie na otwarte, albo w każdy zadaniu w exercises.js dodać element numberOfCorrectAnswers (lub nazwany jakoś lepiej jesli masz pomysł) który domyslnie byłby równy 1, a jeśli byłby równy więcej to skrypt w pliku matematykazen.html powinien umieć obsłużyć większą ilość poprawnych odpowiedzi

- w 29 jest była źle tabela zrobiona, jest dużo mało kolumn, a liczby uczniów powinny być następujące: 5, 8, 12, 13, 12


<br><br><br>


<h3>TO-DO, DO REALIZACJI, PODZIELONE NA PRIORYTET</h3>


WYSOKI PRIORYTET:
- popraw 12 i 17 aby były oddzielne od swoich podzadań. (12.1 i 17.1)

ŚREDNI PRIORYTET:
- Renderowanie LATEX zamiast wpisywania tagów sub i sup które wyglądają brzydko oraz wklejania zdjęć, które się słabo skalują z UI i ciężko się zmienia ich barwy.

NISKI PRIOTYTET:

NIE REALIZUJ, NA POTEM:
- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.


- dodać przycisk "pokaż wszystkie rozwiązania, którego funkcjonalność przyda się przy powyższym punkcie
- w niektórych interaktywnych rozwiązaniach gdzie jest pewien punkt w którym pojawia się sytuacja taka jak w zadaniu możnaby zrobić tak aby łatwiej podczas przesuwania troszeczkę przyklejał się do odpowiedniego miejsca aby łatwiej było trafić na sytuacje opisanąw zadaniu.
- Powiększyć przycisk X w prawym górnym rogu tablicy i pogrubić samego X aby łatwiej było go zauważyć, można też dać jakąś ramkę lub cień
- zielone lub czerwone komentarze przy nteraktywnych rozwiązaniach można dać po br czy coś aby były w nast linijce mówie o czymś takim jak "✓ największe pole przy x = 24/13" w zad 30
- albo ulepszyć płynne przewijanie aby było rzeczywiście płynne albo wyłączyć tą opcje i zrobić tak jak było wcześniej czyli zwykłe skoki paska co pół sekundy czy coś takiego takie defaultowe. Teraz to wygląda jakby pod spodem było niepłynne a ktoś na siłe chciał to upłynić ale mu nie wyszło za bardzo i to męczy oko.
- w zad 1 w solutioInteractive nie widać, że niebieskei strzałki są inym elementem, zlewają sięw jedno. mozna by je troszke odsunąć od siebie i troszke skrócić. mozna tez wywalić -a. Zmienić kolor okna z 4 na zielony i tego z 7 (domyślnie) na niebieski. x mozna oznaczyć żółtym kolorem lub ciemnożółtym. Mozna dodać przycisk resetu. opcjonalnie: sprawić aby przesuwanie 
- dodać przycisk, "pokaż zasady oceniania" po lewej. Działałby on identycznie do przycisku "pokaż tablice wzorów", ale działałby po lewej stronie.
- zaznaczone odpowiediz powinnu mieć gruszy border dwukrotnie.
- nie widać dobrze minusa na tej czcionce ale miejmy nadzieje ze to sie poprawi jak wejdzie latex
- zapisywanie postępu do pliku cookie czy coś

<br><br><br>




DLA UŻYTKOWNIKA:
- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo prostuje błąd.

<br>

POZYTYWNY FEEDBACK DLA CLAUDE:
- ładne zrobiłeś rozwiązanie do zadania 5 z procentem składanym
- fajny pomysł z tym, że im więcej punktów masz tym bardziej zielone są
- sprawdzić co by było gdybym wpisał ujemnął wartość w playback rate czy jakoś tak



<br><br><br>



SPRAWDŹCZY PONIŻSZE SĄ ZROBIONE, JEŚLI NIE TO ZRÓB PRZENIEŚ DO todoDONE.md, 

ŚREDNI PRIORYTET:
- Zadania 19, 20, 29, 30 mają w arkuszu rysunki/tabelę ("zobacz rysunek") — zad 19 i 20 mają obrazki, do 30 warto dodać crop rysunku prostopadłościanu z arkusza (zad30/zad30.png) zgodnie z konwencją zadN/.


NISKI PRIORYTET:
- [CZĘŚCIOWO 2026-07-04] filmiki nie powinny migać podczas przełączania → dodany preload następnego kroku; jeśli dalej miga, następny krok to trzymanie dwóch video i podmiana widoczności.
- tablica-wzorów którą dało by się "odblokować" i przesuwać dowolnie jak sie chce i zmieniać rozmiar okna

- dodanie pól na własny tekst w zadaniach takich jak zadanie 10 w miejscach takich jak "..." i systemu sprawdzania odpowiedzi użytkownika czy pasuje chociaż do jednej wersji poprawnych odpowiedzi. Poniżej zadania powinien znajdować się przycisk sprawdź, po kliknięciu którego przy każdym z pól pojawi się oznaczenie na czerwono lub zielona w zależności od poprawności odpowiedzi. (moze być to w formie zmiany koloru ramki pola) — częściowo zastąpione samooceną (selfScore), ale docelowo warto zrobić prawdziwe pola.




