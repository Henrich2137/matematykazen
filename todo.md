Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)


<br><br><br>


<h3>TO-DO, DO REALIZACJI, PODZIELONE NA PRIORYTET</h3>


WYSOKI PRIORYTET:
- dodać przycisk trzech kropek który po kliknięciu otworzy okienko w który będą schowane przyciski: "pokaż/schowaj wszystkie rozwiązania" oraz "widok punktów"
- dodać przycisk resetuj punktacje



NISKI PRIORYTET:
- [CZĘŚCIOWO] Filmiki nadal migoczą, można spróbować zostawić stary filmik w tle aby został tam na ostatniej klatce i wyłączyć go dopiero przy następnym kroku, jeśli dobrze rozumiem to chyba własnie to opisałeś tutaj: następny krok to trzymanie dwóch elementów video i podmiana widoczności (wymaga testu wzrokowego).
- Zaimplementuj KaTeX zvendorowany do repo (offline) a jeśli się nie uda i będzie tworzyć dużo bagów to zrób KaTeX po stronie klienta

- Migracja treści wszystkich zadań w exercises.js z <sub> i <sup> i tym podobnych na KATEXa

NIE REALIZUJ, NA POTEM:
- do sekcji "oceń się" powinno być dodane kryteria sukcesu dopiero po kliknięciu
  rozwiązania. Ale jeszcze nie mam pomysłu jak to skomponować aby miało sens.




<br><br><br>


DLA UŻYTKOWNIKA:
- Przerenderować w Manimie ostatni krok zad 2 (zad2/zad2rozw_step6.mp4): klatka końcowa
  pokazuje 5⁻⁴, a poprawny wynik to 5⁴ (5⁻¹ · 5⁵ = 5⁴). Komentarz pod filmem tymczasowo
  prostuje błąd.
- Punkt o widżecie zad 1 urwał się w połowie zdania: "opcjonalnie: sprawić aby
  przesuwanie" — dokończ myśl, to zostanie zrobione (reszta punktu o zad 1 jest już
  zrealizowana).


<br><br><br>


NOWE PUNKTY TODO ZAPISYWANE PRZEZ CLAUDE:

- (FABLE 2026-07-05) Do przeklikania przez Henricha:
  1) zad 10 i 29 mają teraz prawdziwe pola do wpisywania odpowiedzi + przycisk "Sprawdź"
     (zielona/czerwona ramka pola; punkty po równo za każde pole). Nawiasy przedziałów
     można wpisywać jako ⟨⟩, [] albo <>, liczby z kropką lub przecinkiem (6.38 = 6,38) —
     normalizacja to ujednolica.
  2) postęp (odpowiedzi + punkty) zapisuje się w localStorage i wraca po odświeżeniu;
     na samym dole arkusza jest dyskretny przycisk "wyczyść zapisany postęp". Zapis
     unieważnia się sam, gdy zmieni się liczba zadań w exercises.js (celowo).
  3) w pasku jest przełącznik "pokaż/schowaj wszystkie rozwiązania" (otwiera też kroki
     wideo — przy "pokaż wszystkie" wystartuje kilka autoplayów naraz; jak to przeszkadza,
     dopisz punkt).
  4) po lewej przycisk "Pokaż zasady oceniania" (oficjalny PDF CKE z odpowiedziami).
  5) oba panele PDF są "odblokowane": przesuwanie za górny pasek, zmiana rozmiaru za
     narożnik ◢ w prawym dolnym rogu.
  6) widżety 1, 9, 12.1 i 18 delikatnie przyciągają punkt do miejsc z zadania (snap).
- (FABLE 2026-07-05) Odpowiedź na pytanie o ujemny playback rate: w UI nie ma już pola
  prędkości — playbackRate jest ustawiony na sztywno (1) w showStep(). Nawet gdyby było,
  przeglądarki nie odtwarzają wideo wstecz przy ujemnej wartości (Chrome/Firefox rzucają
  błąd albo ignorują) — nie ma czego zabezpieczać.
