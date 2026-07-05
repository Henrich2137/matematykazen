Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

do zrobienia:
- coś ty wymyślił za ikonke w title xd? Wywal to jeśli nie jest potrzebne, nie podoba mi się ta ikonka, możesz ewentualnie spróbować z inną, czarno-białym M. Jeśli nie to stworze własne logo lub żadne

- zad 17.1 rozwiązanie się nie zgadza z treścia zadania ponieważ kąt ABClezy przy wierzchołku B
- zad 12 powinno by oddzielone od 12.1
- przyciski w 12.2 nie działają intuicyjnie, trzeba je odklikiwać. Jeżeli uznasz, że jest to proste w implementacji to zrób tak aby ostatni zaznaczony przycisk był tym który automatycznie się odznaczy przy wybraniu nowego. Jeśli uznasz, że to zbyt skomplikuje kod i narazi go na błędy to dodaj lepszą ikonkę zaznaczenia, która będzie sugerować, że trzeba go odznaczyć lub komunikat lub animacje poszerzenia krawędzi która pojawi się po kliknięciu na inną odpowiedź cza, należy albo zmienić to zadanie na otwarte, albo w każdy zadaniu w exercises.js dodać element numberOfCorrectAnswers (lub nazwany jakoś lepiej jesli masz pomysł) który domyslnie byłby równy 1, a jeśli byłby równy więcej to skrypt w pliku matematykazen.html powinien umieć obsłużyć większą ilość poprawnych odpowiedzi
- w 29 jest źle tabela zrobiona, jest dużo mało kolumn, a liczby uczniów powinny być następujące: 5, 8, 12, 13, 12

inne pomysły (NIE REALIZUJ):
- Renderowanie LATEX zamiast wpisywania tagów sub i sup które wyglądają brzydko oraz wklejania zdjęć, które się słabo skalują z UI i ciężko się zmienia ich barwy.
- sprawdzić co by było gdybym wpisał ujemnął wartość w playback rate czy jakoś tak
- do sekcji oceń się powinno być dodane kryteria sukcesu dopiero po kliknięci urozwiązania lae jeszcze nie mam pomysłu jak to skomponować aby miało sens
- dodać przełącznik trybów: luźne ćwiczenie/test. Obecnie rozwijamy tryb luźnego ćwiczenia w którym są podpowiedzi, na bieżąco widać czy zaznaczona odpowiedź jest prawdziwa, można od razu włączyć rozwiązania itd. W trybie testu uczeń mógby zaznaczać odpowiedzi lub zapisywać sobie odpowiedzi do zadań otwortych w wyznaczonym miejscu, a dopiero na końcu mógłyby je sprawdzić, byłby też licznik czasu itd.
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


Chwalenie claude:
- ładne zrobiłeś rozwiązanie do zadania 5 z procentem składanym
- fajny pomysł z tym, że im więcej punktów masz tym bardziej zielone są


NOWE PUNKTY TODO ZAPISYWANE PRZEZ CLAUDE:

--- Weryfikacja zgodności z arkuszem PDF (2026-07-05, sesja: sprawdzenie exercises.js vs "arkusze PDF/") ---
Porównałem cały exercises.js z arkuszem (matematyka-2024-grudzien-probna-podstawowa.pdf)
i kluczem (…-odpowiedzi.pdf). Tekst obu PDF-ów wyciągnąłem przez `pdftotext -layout`
do arkusze PDF/arkusz.txt oraz arkusze PDF/odp.txt (zostawione na przyszłość).

WYNIK: wszystkie 30 odpowiedzi zgadza się z oficjalnym kluczem CKE. Treści też się
zgadzają. Jedyna realna rozbieżność:

- [DO POPRAWKI] Zad 29 — tabela w exercises.js NIE zgadza się z arkuszem.
  * Arkusz CKE: 5 kolumn — książki {4, 5, 6, 7, 8}, uczniowie {5, 8, 12, 13, 12} (suma 50).
  * exercises.js (obecnie): 6 kolumn — książki {4..9}, uczniowie {7,8,10,14,6,5} (wersja odtworzona).
  * Obie wersje dają średnią 6,38 i medianę 6,5, więc odpowiedzi są OK, ale sama tabela
    jest zmyślona. Podmienić <table class="data-table"> w zad 29 na oryginał: usunąć kolumnę
    "9", nagłówek książek = 4,5,6,7,8, liczby uczniów = 5,8,12,13,12. Zaktualizować też
    solutionText (rozpiskę średniej 4·5 + 5·8 + 6·12 + 7·13 + 8·12 = 319) — wynik 319/50 = 6,38
    się nie zmienia. Po podmianie punkt "Zad 29 tabela" można zdjąć z todo2.md i todo3.md.

- [OK, potwierdzone z kluczem] Punktacja zadań otwartych zgadza się z arkuszem:
  zad 3 (0-2), 8 (0-3), 9 (0-2), 10 (0-4), 19 (0-4), 26 (0-2), 28 (0-2), 29 (0-2), 30 (0-4).
  Suma całego arkusza = 50 pkt. Zgadza się z maxTotalScore liczonym z maxScore.

- [DO ROZWAŻENIA] Zad 12 w arkuszu to jedno zadanie z trzema podpunktami (12.1, 12.2, 12.3)
  poprzedzonymi wspólnym wprowadzeniem (parabola: wierzchołek (3,0), przechodzi przez (0,-9)).
  W exercises.js 12.1/12.2/12.3 to osobne wpisy, każdy powtarza wprowadzenie — spójne z
  konwencją "multi-part = osobne wpisy", ale pokrywa się z uwagą użytkownika wyżej
  ("zad 12 powinno być oddzielone od 12.1"). Rozważyć wizualne zgrupowanie 12.1-12.3.

- uzupełnij tutaj, zedytuj ten tekst
- jeśli masz pomysły jakieś