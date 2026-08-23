# Odtwarzacz „krok po kroku" v20 — testy Henricha

Wynik pierwszego przejścia Henricha przez v20 (zad. 1/2/3, arkusz grudzień 2024) i
przez v19 (test kadru 16:9 na zad. 2). Pełna checklista z odpowiedziami — TODO.md
ma tylko skrót z odnośnikiem tutaj. Zebrane 2026-08-12 z TODO.md (sekcja
TESTOWANIE HENRICH), pochodzi z paczki Opus 5 High, 2026-08-11 (v20).

## Zad. 1/2/3 — nowy odtwarzacz (v20)

Rewersy są gotowe dla wszystkich trzech zadań, więc ◄ ma czym cofać.

- ✅ **KROPKI, wersja B przyjęta.** Rysunek Henricha (ROW 1) miał dwie sprzeczne
  linijki: „po skończeniu 3. kroku" sugerowało pełny pasek PO PRAWEJ od O, a
  „po obejrzeniu całości" PO LEWEJ. Zaimplementowane: gdy film dobiegnie końca, O
  przeskakuje na kropkę po prawej (`o o o~~~O o o` po skończeniu 3. kroku).
  Henrich: „OPISAŁEM WYŻEJ" — decyzja przyjęta, nie zmieniać bez wyraźnej prośby.

- ✅ **Klik w dowolną kropkę** → pierwsza klatka tego kroku, film zatrzymany;
  ostatnia kropka = stan końcowy (ostatnia klatka ostatniego filmu). Henrich: „DZIAŁA".

- 🟨 Otwarte, jeszcze bez odpowiedzi Henricha:
  - ◄ w środku filmu ma lecieć od tyłu i zatrzymać się na początku TEGO kroku;
    ◄ jeszcze raz (na pierwszej klatce) cofa cały poprzedni krok; na kropce 0
    jest wyszarzone.
  - Pasek postępu (teraz między kropkami, nie pod filmem) ma się OPRÓŻNIAĆ przy
    cofaniu.
  - ROW 2: ◄ / start-pauza w kółku / ► — kółko odróżnia „odtwórz" (▶) od
    „następny krok" (►); przyciski 44 px, sprawdzić kciukiem.
  - ROW 3 „Pokaż wyjaśnienie kroku" — pod nim całe pole `text` (opis + wzór);
    pod filmem NIE MA już stałego podpisu.
  - Panel boczny → „Prędkość filmów": ¼× ½× 1× 2× 4× (zapisane jako ułamki, bo
    lista stanów rozdziela przecinkiem i „0,25×" rozpadłoby się na dwa). Zmiana
    działa od razu na odtwarzanym filmie. Przy 4× obraz skokowy — zmierzone i
    zaakceptowane, patrz sekcja „Odtwarzanie 4× gubi klatki" w
    issues/rozwiazanie-krok-po-kroku-odtwarzacz.md.
  - Telefon: przesunięcie palcem w lewo/prawo = następny/poprzedni krok.
    Desktop: strzałki ← →.
  - Zad. 1 ma 10 kropek, zad. 3 ma 9 → strzałeczki ‹ › po bokach paska kropek
    powyżej siedmiu. Zad. 2 ma dokładnie 7 i strzałek mieć NIE powinno.
  - Dojście do ostatniego kroku NIE zaznacza już poprawnej odpowiedzi (zdjęte,
    zgodnie z prośbą).
  - Zad. 1 i 3 mają filmy jeszcze w starym kadrze 21:9 — nie są już wciskane w
    pudełko 16:9, kadr dopasowuje się do pliku (zniknął pas ok. 80 px nad/pod
    obrazem).

## Ciemny motyw (poprawka przy okazji v20)

🟨 Otwarte, bez odpowiedzi Henricha. Jeśli motyw WYMUSZONY ręcznie w panelu
bocznym (nie „auto"), rysunki i filmy mają być przygaszone tak samo jak przy
motywie z systemu — wcześniej przy ręcznym wyborze świeciły na biało, brakowało
jednej zmiennej w CSS. To najpewniej powód, dla którego analogiczny punkt z v15
mógł wyglądać na niezrobiony.

## Zad. 2, arkusz grudzień 2024 (v19) — test nowego kadru

Test SAMEJ rozdzielczości i osadzenia filmu (16:9, 1280×720, 120 fps, wzory
pomocnicze przeniesione z kadru do podpisu pod filmem) — bez kropek, przycisków
i rewersów, dodanych dopiero w v20 wyżej.

- ✅ Rozdzielczość/osadzenie 720p120fps. Henrich: „WYGLĄDA DOBRZE, ale czasem
  zajmuje 0,5 s doładowanie na początku, jest okej."
- ✅ Rozmiar filmu (komputer 608×342 zamiast 420×180, telefon 340×191 zamiast
  300×129, na telefonie na całą szerokość karty). Henrich: „WYGLĄDA DOBRZE".
- ✅ Kadr na telefonie mieści się razem z nawigacją („1 / 6" + strzałki), bez
  przewijania. Henrich: „JEST DOBRZE".
- ❌ **Podpis pod filmem na telefonie: za wąskie marginesy.** Henrich: „NA
  TELEFONIE JEST ZA SZEROKI TEN NAPIS, NIE MA MARGINESÓW ZA BARDZO Z LEWEJ I
  PRAWEJ, NA TELEFONACH TEN BOX W KTÓRYM SĄ ROZWIĄZANIA POWINIEN BYĆ TROSZKĘ
  SZERSZY ABY DAĆ WIĘCEJ MIEJSCA ELEMENTOM W ŚRODKU." → do zrobienia: poszerzyć
  kontener rozwiązania krok po kroku na telefonie (mniej marginesu z boków karty
  albo szerszy box), nie tylko zawinąć tekst.
- ❌ **Treść kroku 1/6 do weryfikacji — literówka w opisie zadania, nie
  potwierdzona w kodzie.** Poprzedni opis mówił o widocznym w kroku 1
  wykładniku \(-5\) i w kroku 6 wyniku \(5^4\). Henrich poprawia: „CAŁY CZAS
  MÓWISZ O WYKŁADNIKU -5 A TO PRZECIEŻ MA BYĆ -1, 5 I NA KONCU 4. WYKŁADNIK -
  mała liczba zapisana u góry po prawej od podstawy." Czyli: krok 1 pokazuje
  wykładnik \(-1\), gdzieś w kolejnych krokach podstawa \(5\), krok 6 wynik
  \(5^4\) — **nie** wykładnik „-5" jak wcześniej opisano. Do zrobienia:
  1. sprawdzić w `matura/2024-grudzien/exercises.json` (zad. 2) i w scenie
     `manimations/` jaka jest faktyczna treść przekształcenia,
  2. potwierdzić, że krok 1 rysuje wykładnik -1 (nie -5) i krok 6 kończy na
     \(5^4\),
  3. jeśli scena/dane rzeczywiście mają błąd, poprawić — jeśli to była tylko
     pomyłka w opisie/TODO, brak zmian w kodzie, tylko odnotować.
  Related: pułapka przytrzymania stanu końcowego opisana w
  manimations/README.md (punkt 0 workflow, „każdy krok musi kończyć się self.wait(0.25)")
  — to na niej opierało się pierwotne stwierdzenie o widoczności wykładnika.
