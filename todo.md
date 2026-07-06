Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)


<br><br><br>


<h3>TO-DO, DO REALIZACJI, PODZIELONE NA PRIORYTET</h3>


WYSOKI PRIORYTET:
(pusto — wszystkie punkty z 2026-07-06 zrealizowane, patrz raport niżej i todoDONE.md)



NISKI PRIORYTET (drobne porządki, dobre na krótką sesję):
(pusto — cztery punkty porządkowe z 2026-07-06 zrealizowane, patrz todoDONE.md)

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

- (FABLE 2026-07-06) RAPORT Z SESJI — do przeklikania przez Henricha:
  1) KaTeX działa OFFLINE (zvendorowany do vendor/katex/, ~600 KB). Cała matematyka
     w exercises.js (treści, odpowiedzi, podpowiedzi, rozwiązania, komentarze kroków)
     przepisana na KaTeX — 422 wzory, wszystkie zweryfikowane automatycznie
     (katex.renderToString, 0 błędów). BONUS: wzory-obrazki w zad 2, 6, 7, 8 i 10
     (definicja funkcji) też są teraz KaTeXem — obrazki zostały tylko tam, gdzie są
     prawdziwe rysunki (wykresy/figury). Nieużywane PNG zostawiłem na dysku.
  2) W pasku jest przycisk ⋯ ("więcej opcji"): w okienku są "pokaż/schowaj wszystkie
     rozwiązania", "widok punktów" i NOWY "resetuj punktację" (czyści zapisany postęp
     i przeładowuje stronę — to samo co przycisk na dole arkusza). Okienko zamyka się
     po kliknięciu gdziekolwiek poza nim.
  3) Migotanie filmików: zrobiony podwójny bufor — stary krok wisi na ostatniej
     klatce, aż nowy film ma zdekodowaną pierwszą klatkę, dopiero wtedy podmiana.
     WYMAGA TWOJEGO TESTU WZROKOWEGO (w testach automatycznych działa, ale "czy miga"
     widać tylko okiem).
  4) Przyciski odpowiedzi: dłuższe wzory (przedziały, ułamki) poszerzają przycisk
     zamiast łamać się na dwie linie; krótkie liczby trzymają równą siatkę.
  5) Sprawdzone w przeglądarce (Playwright): punktacja, PF, multiSelect, fillIn
     (zad 10 i 29), zapis/odczyt postępu, menu ⋯, reset, kroki wideo, KaTeX w
     krokach — wszystko działa; suma punktów arkusza dalej 50.
  Jeśli KaTeX gdzieś będzie brzydko wyglądał (rozmiar czcionki wzorów ustawiłem na
  1.08em w style.css, reguła .katex) — dopisz punkt, łatwo doregulować.

- (FABLE 2026-07-06, własna inwencja) Strona jest teraz RESPONSYWNA: breakpointy
  1024/900/720/560px (szczegóły w ARCHITECTURE.md). Na telefonie (sprawdzone od
  360px wzwyż): pasek przechodzi na dwa rzędy, karta zadania wypełnia ekran,
  filmiki i wykresy się skalują, szerokie wzory dostają własny poziomy scroll,
  zero poziomego scrolla całej strony. Badge punktów na ekranach < ~1010px
  przenosi się do prawego górnego rogu karty (wcześniej wisiał 120px za kartą).
  DO OBEJRZENIA na prawdziwym telefonie — testowałem tylko w przeglądarce
  z symulowaną szerokością. Dodałem też ikonkę "M" do index.html (była tylko
  w arkuszu).

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
