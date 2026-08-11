# Rozwiązania krok po kroku — nowy kształt

Data: 2026-08-11
Status: **wdrożone w v20** — paczki A, C i rewersy z B są zrobione dla wszystkich
trzech zadań z krokami (zad. 1, 2 i 3). Otwarte zostaje przerenderowanie scen
zad. 1 i 3 do nowego kadru (paczka D poza zadaniem 2) oraz skrypt cięcia sceny
na kroki z paczki B. Przebieg i pomiary: `done/04-biezace.md`, wpis z 2026-08-11.

Uwaga do treści niżej: kilka decyzji doprecyzował potem Henrich w TODO.md i to
one obowiązują — pod filmem NIE ma zawsze widocznej linijki podpisu (całe pole
`text` chowa się pod przyciskiem ROW 3), a nazwy plików to `stepN.mp4` +
`stepNreverse.mp4`, nie `krokN.mp4` / `krokN-rewers.mp4`.

## Skąd to się wzięło

Punkt wyjścia: pomiar dzisiejszego stanu na zadaniu 2, nie wyobrażenie o nim.

| Ekran | Film na stronie | Zapas rozdzielczości | Dostępna szerokość |
|---|---|---|---|
| Telefon 390 px | 300 × 129 px | 8,4× za dużo | 374 px |
| Telefon 360 px | 270 × 116 px | 9,3× za dużo | — |
| Tablet 768 px | 420 × 180 px | 4,0× za dużo | — |
| Desktop 1440 px | 420 × 180 px | 2,0× (dobrze) | **608 px** |

Wnioski, które przestawiły cały projekt:

- **Rozdzielczość nigdy nie była problemem.** Na telefonie jest ośmiokrotny zapas
  pikseli. Problemem jest kadr 21:9 — przy szerokości 300 px zostaje 129 px
  wysokości, a treść i tak zajmuje lewą ⅓, bo prawe ⅔ trzyma miejsce na wzór
  pomocniczy (w kroku 1 puste).
- **Ten sam wzór złożony w KaTeX w treści zadania jest czytelniejszy niż jego
  kopia w filmie tuż pod spodem.** To najmocniejszy argument, że rzecz jest
  w kadrze i w tym, co w nim siedzi.
- **Na desktopie film jest mały z powodu jednej linijki CSS** (`width: 420px`
  w `.solution-step-by-step-container video`), przy 608 px dostępnych. 188 px
  marnuje się bez żadnego powodu technicznego.

## Decyzje

### Kadr i materiał

- **16:9, 1280×720, 120 fps.** 1280 pokrywa telefon przy DPR 3 (potrzeba 900 px)
  i desktop przy DPR 2 (840 px) z zapasem, a przy okazji jest standardowym 720p.
- **120 fps to zapas pod spowolnienie**, nie pod płynność przy 1×. Spowolnienie
  nie dorysowuje klatek, tylko trzyma je dłużej: przy materiale 60 fps tryb
  0,25× wygląda jak 15 fps, a to właśnie ten tryb ma służyć przyglądaniu się
  przekształceniu.
- **Zmierzone, nie założone** (render próbny + odtwarzanie w Chromium):
  plik 1280×720/120 fps waży 39 kB wobec 20 kB dzisiejszego 840×360/60 fps —
  czyli 2×, nie 10×. Kodek zapisuje się jako H.264 High **Level 4.2** (tyle
  wymaga 720p120; starsze dekodery sprzętowe mają tu granicę).
  Odtwarzanie: 1× i 0,25× — czas co do setnej sekundy, 6 zgubionych klatek na
  240–480. **4× — 218 zgubionych klatek na 720** (dekoder musi przerobić
  480 kl./s); film dobiega do końca, ale skokowo. Przy 60 fps tego efektu nie ma.
  Uznane za akceptowalne, bo 4× to tryb „przewiń", nie „oglądaj".
  **Ograniczenie tego pomiaru:** Chromium bez ekranu, w kontenerze, na procesorze
  desktopowym. Telefon i Safari nie zostały sprawdzone — do zweryfikowania na
  prawdziwym urządzeniu przy pierwszej okazji.
- **Sceny trzeba przeliczyć, nie tylko przestawić config.** Dzisiejsze
  `font_size=120` i `shift(LEFT*4.5)` są dobrane pod stary kadr; treść ma być
  wyśrodkowana, a rozmiar czcionki ustalony na nowo.

### Co jest w kadrze, a co obok

- **W filmie zostaje wyłącznie przekształcenie działania.**
- **Wzór pomocniczy wychodzi z filmu** do rozwijanego opisu kroku, **domyślnie
  zwiniętego**. Zyski: kadr może się zwęzić, wzór staje się zaznaczalny,
  wyszukiwalny i czytany przez czytnik ekranu, a widok domyślny jest
  minimalistyczny.
- **Pod filmem zostaje jedna zawsze widoczna linijka podpisu** — nazwa czynności
  („zamieniamy pierwiastek na potęgę"). Bez niej zwinięty krok nie mówi nic
  o tym, co się w nim dzieje.

### Interfejs

Kolejność w pionie: **film → podpis → kropki → przyciski → zwinięty opis.**
Rozwijany opis na samym dole, żeby jego otwarcie nie spychało nawigacji.

- **Kropki zamiast licznika „2 / 6"** — wyrównane od lewej do prawej pod filmem,
  klikalne, w trzech stanach: odwiedzony / bieżący (dokładnie jeden) /
  nieodwiedzony.
- **Kropek jest o jedną więcej niż filmów.** To nie detal, tylko model:
  **kropka = stan działania, film = przejście między stanami.** Stąd wynika
  reszta — „wstecz zatrzymuje się na pierwszej klatce" znaczy „lądujesz dokładnie
  na kropce", a kliknięcie kropki pokazuje nieruchomą klatkę tego stanu.
- **Trzy przyciski**: ◄ poprzedni krok / ‖ start-pauza / ► następny krok.
  Pole dotyku ≥ 44 px (dzisiejsze strzałki są mniejsze).
- **Przesuwanie palcem** w lewo/prawo na telefonie, **klawiatura ← →** na
  desktopie.
- **Prędkość 0,25×–4× w panelu bocznym**, nie przy filmie. Tanie: dzisiejsze
  `podepnijSterowanieWideo()` ustawia `playbackRate` w jednym miejscu.
- **Szerokość**: na desktopie film wykorzystuje całe dostępne 608 px zamiast
  420; na telefonie ścinamy padding (dziś 16 px karty + 20 px panelu na stronę).

### Odtwarzanie wstecz

- **Przeglądarki nie odtwarzają wideo do tyłu** (ujemna prędkość nie działa),
  więc rewers to **osobny plik**.
- **Rewersu nie renderuje Manim** — robi go `ffmpeg -vf reverse` z gotowego
  pliku. Jedna linijka w skrypcie, a wynik nie może się rozjechać z wersją do
  przodu, bo powstaje z niej samej.
- Logika ◄: stojąc w środku kroku — leci rewers od bieżącej klatki i zatrzymuje
  się na kropce z lewej; stojąc już na kropce — cofka o cały krok, też
  w rewersie.

### Pliki i katalogi

```
matura/2024-grudzien/media/zad2/
├── krok-po-kroku/
│   ├── krok1.mp4
│   ├── krok1-rewers.mp4
│   └── ...
└── zad2rys.png          ← rysunki zostają na wierzchu
```

- Podfolder jest konieczny, bo rewersy podwajają liczbę plików (zadanie 2 to
  12 filmów zamiast 6, dziś wymieszanych z rysunkami).
- **`krok-po-kroku/`, nie `solutions/step-by-step/`** — pośredni katalog
  `solutions/` miałby przez długi czas jedno dziecko; drugi rodzaj rozwiązania
  dołoży się obok, nie pod spodem. Nazwa po polsku, bo taka jest w interfejsie
  i w `TODO.md`, a dzisiejsze `zad2rozw_step1` jest w pół drogi między językami.
- **Nazwy plików bez prefiksu** (`krok1.mp4`) — katalog już mówi, że to kroki
  zadania 2.
- **`manimations/` zostaje na wierzchu repo, nie idzie pod arkusze.** Decyzja
  Henricha: produkcja ma być oddzielona od statycznej strony, żeby przyszła
  gałąź hostingowa nie ciągnęła za sobą źródeł animacji.

## Podział na paczki

Projekt dotyka czterech niezależnych warstw, każdej o innym sposobie testowania.

| Paczka | Zakres | Status |
|---|---|---|
| **A. Dane i pliki** | katalogi `media/zadN/krok-po-kroku/`, nazwy `stepN.mp4`, migracja istniejącego | **zrobione (v20)** |
| **B. Potok renderu** | `manim.cfg` na 16:9/720p/120 fps, konwencje scen po wyjęciu wzoru, skrypt: kroki + rewersy + kopiowanie na miejsce | **rewersy zrobione** (`tools/rewersy.sh`); cięcie sceny na kroki wciąż ręczne |
| **C. Odtwarzacz** | kropki, przyciski, swipe, klawiatura, rewers, prędkość w ustawieniach, szerokość i marginesy | **zrobione (v20)** |
| **D. Przerobienie scen** | nowy kadr i nowy podział treści | zad. 2 zrobione; **zad. 1 i 3 wciąż 21:9** |

Kolejność jest wymuszona: odtwarzacz z kropkami i rewersem nie ma czego
odtwarzać, dopóki rewersy nie istnieją. Zadanie 2 idzie pierwsze jako pilot —
zanim pod nowy kadr przerobione zostaną pozostałe sceny, Henrich ogląda wynik
na telefonie i potwierdza, że 16:9 to właściwy wybór.

## Poza zakresem (świadomie)

- Pełny ekran — kadr jest mały i wektorowy, nie ma czego powiększać.
- Pasek przewijania filmu — kroki trwają 1–2 s.
- `prefers-reduced-motion` (pokazanie ostatniej klatki zamiast animacji) —
  zgłoszone, nieprzedyskutowane, do rozstrzygnięcia przy paczce C.
