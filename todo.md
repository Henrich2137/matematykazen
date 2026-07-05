Nowy plik który tworzy Henrich (ja, użytkownik). Podczas Sprawdzania nowej wersji strony utworzonej przez fable (claude/project-improvements-exercises...)

(Zasada: tu są TYLKO otwarte punkty. Zrobione wpisy [DONE]/[ZROBIONE] przenoszone są do todoDONE.md — patrz CLAUDE.md.)


FEEDBACK FABLE (2026-07-05) do prośby "sprawdź poprawność rozwiązań i oceń":

- zad 17.1: [OPUS DID WELL] — treść, rysunek (zad17/zad17.png) i rozwiązanie są ZGODNE.
  Kąt prosty jest przy A (AB i AC to przyprostokątne), przeciwprostokątna to BC = 8,
  więc sin(∠ABC) = AC/BC = √15/8 — odp. D, potwierdzona w oficjalnym kluczu CKE
  (odp.txt: "Rozwiązanie D"). Nie było czego poprawiać.

- zad 12 i 17 oddzielenie od podzadań: [OPUS DID POORLY] — wstęp 12 był wklejony w treść
  12.1, a wstęp 17 (z rysunkiem) w 17.1. POPRAWIONE PRZEZ FABLE (2026-07-05): 12 i 17 są
  teraz osobnymi, "pustymi" elementami exercises (maxScore: 0 — bez odpowiedzi, punktów,
  podpowiedzi i rozwiązań), a 12.1/12.2/17.1/17.2 zaczynają się od własnego numeru jak
  w arkuszu (usunięte też powtórki treści "Dana jest ta sama funkcja/trójkąt").

- przyciski w 12.2: [OPUS DID WELL] — okno przesuwne już działa: gdy komplet odpowiedzi
  jest zaznaczony, klik nowej odpowiedzi automatycznie podmienia najdawniej wybraną,
  więc nic nie trzeba ręcznie odklikiwać. Osobne pole numberOfCorrectAnswers nie jest
  potrzebne — liczbę wymaganych odpowiedzi wyznacza długość correctAnswerIndices
  i skrypt obsługuje dowolną ich liczbę.

- zad 29 tabela: [OPUS DID WELL] — tabela w exercises.js jest zgodna z oryginałem CKE:
  książki 4–8, liczby uczniów 5, 8, 12, 13, 12 (średnia 6,38, mediana 6,5 jak w kluczu).


<br><br><br>


<h3>TO-DO, DO REALIZACJI, PODZIELONE NA PRIORYTET</h3>


ŚREDNI PRIORYTET:
- Renderowanie LATEX zamiast wpisywania tagów sub i sup które wyglądają brzydko oraz
  wklejania zdjęć, które się słabo skalują z UI i ciężko się zmienia ich barwy.
  (FABLE 2026-07-05: proponuję KaTeX + rozszerzenie auto-render. Potrzebna decyzja
  Henricha: CDN (najprościej, ale wymaga internetu przy nauce) czy pliki zvendorowane
  do repo (~1,5 MB, działa offline). Do tego dochodzi migracja treści wszystkich zadań
  na \( ... \) — duża robota na osobną sesję, najlepiej razem z planowaną migracją
  exercises.js → exercises.json.)

NISKI PRIORYTET:
- [CZĘŚCIOWO 2026-07-04/05] filmiki nie powinny migać podczas przełączania → jest preload
  następnego kroku, a pasek postępu jest teraz płynny (requestAnimationFrame); jeśli
  przełączanie kroków nadal miga, następny krok to trzymanie dwóch elementów video
  i podmiana widoczności (wymaga testu wzrokowego — Fable nie jest w stanie tego ocenić
  bez przeglądarki).

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

- (FABLE 2026-07-05) Do przeklikania przez Henricha — nowe rzeczy z tej sesji:
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
