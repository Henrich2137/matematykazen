# Tablica wzorów CKE — transkrypt

Transkrypt `wybrane_wzory_matematyczne.pdf` (CKE, 2022) rozbity na sekcje, żeby
model ładował tylko potrzebny fragment zamiast całych 31 stron.

**Jak używać:** znajdź temat w skorowidzu na dole → otwórz wskazany plik. Numer strony
podany przy każdym wzorze to strona PDF-a — ta sama, którą wpisuje się w
`formulasPage` w `exercises.json` (numeracja drukowana = fizyczna, bez przesunięcia).

**Przy ustalaniu `formulasPage` dla konkretnego zadania (nauka z błędów Sonneta, 2026-07-28,
patrz DONE/04-biezace.md):**
- Nie zgaduj strony z samego **tematu** zadania (np. "to stereometria więc str. 27") — sprawdź,
  jakiego wzoru **faktycznie** używa `hint`/`solutionText`/`solutionTextMore`. Zadanie może
  brzmieć jak dział X, a rozwiązanie po drodze używać tylko podstawowej definicji z działu Y
  (np. zad. 24 z 2024-grudzień: "kąt nachylenia ściany ostrosłupa" brzmi jak stereometria,
  ale liczy się go zwykłym `tg α` z trygonometrii [9.1], bez żadnego wzoru na objętość).
- Czytaj **pełną** treść zadania, nie tylko pierwsze zdanie (`question` bywa długie, z
  podpunktami/wieloma pytaniami w jednym obiekcie) — inaczej łatwo przeoczyć drugą połowę
  polecenia, która wymaga innego wzoru.
- Jeśli zadanie ma podzadania (`Zadanie N.1`, `N.2`, ...), sprawdź czy `formulasPage` intro
  (`Zadanie N.`) nie jest zbędne — czasem cała treść merytoryczna i tak jest w podzadaniach.
- "Wygląda jak ten sam wzór" ≠ "jest tym samym wzorem" — n-ty wyraz ciągu geometrycznego
  `aₙ = a₁·qⁿ⁻¹` (str. 9, [8.4]) i procent składany `Kₙ = K₀·(1+p/100)ⁿ` (str. 10, [8.10])
  są matematycznie tej samej postaci, ale w PDF-ie CKE to dwa **osobne, oddzielnie wypisane**
  wzory na dwóch różnych stronach — nie zakładaj, że jeden pokrywa drugi tylko dlatego, że
  wyglądają podobnie po podstawieniu `q = 1+p/100`.
- Jedno zadanie często wymaga wzorów z **więcej niż jednej** strony (np. Pitagoras + pole
  trapezu) — `formulasPage` na razie przyjmuje tylko jedną liczbę (patrz TODO.md, plan zmiany
  na `formulasPages`), więc wybierz stronę z wzorem **kluczowym/końcowym** dla rozwiązania,
  a resztę dopisz do TODO.md jako punkt do uzupełnienia po wdrożeniu wielu stron.

**Konwencje:**
- Wzory w KaTeX, w tej samej konwencji co `exercises.json`: `\( ... \)` inline, `\[ ... \]` w osobnej linii — da się je kopiować do zadań bez przepisywania (pamiętaj tylko o podwojeniu `\` przy wklejaniu do JSON-a).
- ID w postaci `[sekcja.numer]`, np. `[2.6]`. Odwołania między wzorami przez to ID.
- Przy każdym wzorze pozycja na stronie (`góra` / `środek` / `dół`) — do szybkiego odnalezienia go wzrokiem w PDF-ie.
- Opisy słowne zachowane z oryginału CKE. Wtrącenia własne (nie z tablicy) są w cytatach `>`.
- Przy figurach geometrycznych zamiast rysunku podana jest **legenda oznaczeń** — co znaczy każdy symbol we wzorze.
- **Nie wszystko z PDF-a tu jest** — patrz sekcja „Czego tu NIE MA" poniżej. Zanim uznasz, że tablica czegoś nie zawiera, sprawdź tę listę.

## Czego tu NIE MA — kiedy otworzyć PDF

Transkrypt pokrywa **cały tekst i wszystkie wzory** ze stron 4–33 (każdy punkt „•" z oryginału).
Trzy rzeczy zostały świadomie pominięte — jeśli potrzebujesz którejś z nich, otwórz
`../wybrane_wzory_matematyczne.pdf` na wskazanej stronie:

| Czego brak | Gdzie w PDF | Dlaczego pominięte |
|---|---|---|
| **Rysunki i wykresy** (figury geometryczne, wykresy funkcji, bryły) | s. 8, 11, 12, 15–28 | Transkrypt jest tekstowy. Zamiast rysunku podana jest **legenda oznaczeń** — co znaczy każdy symbol we wzorze. Do policzenia wzoru to wystarcza; do zrozumienia konfiguracji („który kąt jest oparty na którym łuku") — nie. Wzory z rysunkiem mają dopisek `Rysunek: PDF s. N`. |
| **Tablica wartości funkcji trygonometrycznych** (sekcja 17) | s. 34 | Kilkaset odczytów `sin`/`cos`/`tg` co 1°, których model i tak zna z pamięci. Kąty typowe dla matury (0°, 30°, 45°, 60°, 90°) są w [9.5]. |
| Okładka, zespół redakcyjny, spis treści, adresy OKE | s. 1–3, 35–36 | Brak treści matematycznej. |

**Nic poza tym nie zostało pominięte.** Kompletność sprawdzona 2026-07-28 przez wypisanie
wszystkich punktów „•" i nagłówków sekcji z PDF-a (strony 4–34) i porównanie ich jeden do
jednego z ID w transkrypcie.

## Sekcje

| Sekcja | Temat | Strony | Plik |
|---|---|---|---|
| 1 | Wartość bezwzględna liczby | 4 | [01-wartosc-bezwzgledna.md](01-wartosc-bezwzgledna.md) |
| 2 | Potęgi i pierwiastki | 4–5 | [02-potegi-pierwiastki.md](02-potegi-pierwiastki.md) |
| 3 | Logarytmy | 5–6 | [03-logarytmy.md](03-logarytmy.md) |
| 4 | Silnia. Współczynnik dwumianowy | 6 | [04-silnia-wspolczynnik-dwumianowy.md](04-silnia-wspolczynnik-dwumianowy.md) |
| 5 | Wzór dwumianowy Newtona | 7 | [05-wzor-dwumianowy-newtona.md](05-wzor-dwumianowy-newtona.md) |
| 6 | Wzory skróconego mnożenia | 7 | [06-wzory-skroconego-mnozenia.md](06-wzory-skroconego-mnozenia.md) |
| 7 | Funkcja kwadratowa | 7–9 | [07-funkcja-kwadratowa.md](07-funkcja-kwadratowa.md) |
| 8 | Ciągi | 9–11 | [08-ciagi.md](08-ciagi.md) |
| 9 | Trygonometria | 11–14 | [09-trygonometria.md](09-trygonometria.md) |
| 10 | Planimetria | 15–22 | [10-planimetria.md](10-planimetria.md) |
| 11 | Geometria analityczna | 22–26 | [11-geometria-analityczna.md](11-geometria-analityczna.md) |
| 12 | Stereometria | 26–28 | [12-stereometria.md](12-stereometria.md) |
| 13 | Kombinatoryka | 28 | [13-kombinatoryka.md](13-kombinatoryka.md) |
| 14 | Rachunek prawdopodobieństwa | 29–30 | [14-rachunek-prawdopodobienstwa.md](14-rachunek-prawdopodobienstwa.md) |
| 15 | Parametry danych statystycznych | 31–32 | [15-parametry-danych-statystycznych.md](15-parametry-danych-statystycznych.md) |
| 16 | Pochodna funkcji | 32–33 | [16-pochodna-funkcji.md](16-pochodna-funkcji.md) |
| ~~17~~ | ~~Tablica wartości funkcji trygonometrycznych~~ | 34 | pominięta (patrz wyżej) |

Uwaga: sekcje nie kończą się równo ze stronami — np. sekcja 8 (Ciągi) ma granice
na górze s. 11, a sekcja 10 (Planimetria) kończy się na górze s. 22. Dlatego przy
`formulasPage` warto kierować się stroną podaną przy **konkretnym wzorze**, a nie
zakresem sekcji.

## Skorowidz — szukaj tu, gdy zadanie dotyczy…

| Zagadnienie w zadaniu | Wzór | Strona |
|---|---|---|
| równanie / nierówność z wartością bezwzględną | [1.1], [1.4] | 4 |
| odległość na osi liczbowej | [1.1] | 4 |
| \(\sqrt{a^2}\), upraszczanie pierwiastka | [2.2] | 4 |
| pierwiastek zamieniany na potęgę | [2.5] | 5 |
| mnożenie / dzielenie / potęgowanie potęg | [2.6] | 5 |
| ujemny wykładnik, \(a^0\) | [2.4] | 5 |
| nierówność wykładnicza | [2.7] | 5 |
| równanie / działania na logarytmach | [3.1], [3.2] | 5 |
| logarytm o innej podstawie | [3.3] | 6 |
| silnia, upraszczanie \(\frac{n!}{k!}\) | [4.1] | 6 |
| symbol Newtona, „na ile sposobów wybrać" | [4.2], [13.2] | 6, 28 |
| rozwinięcie \((a+b)^n\) | [5.1] | 7 |
| \((a\pm b)^2\), \((a\pm b)^3\), \(a^2-b^2\) | [6.1], [6.3] | 7 |
| delta, miejsca zerowe, wzory na \(x_1, x_2\) | [7.1], [7.4] | 7, 8 |
| wierzchołek paraboli, postać kanoniczna | [7.3], [7.5] | 8 |
| suma / iloczyn pierwiastków (Viète) | [7.7] | 9 |
| postać iloczynowa funkcji kwadratowej | [7.6] | 9 |
| ciąg arytmetyczny — wyraz, suma | [8.1], [8.2] | 9 |
| ciąg geometryczny — wyraz, suma | [8.4], [8.5] | 9 |
| trzy liczby tworzą ciąg (warunek) | [8.3], [8.6] | 9, 10 |
| suma szeregu geometrycznego, \(|q|<1\) | [8.7] | 10 |
| procent składany, kapitalizacja odsetek, lokata | [8.10] | 10 |
| granica ciągu | [8.8], [8.11] | 10, 11 |
| sinus / cosinus / tangens w trójkącie prostokątnym | [9.1] | 11 |
| jedynka trygonometryczna | [9.4] | 12 |
| wartości \(\sin 30°\), \(\cos 45°\) itp. | [9.5] | 13 |
| wzory redukcyjne, \(\sin(90° - \alpha)\) | [9.8] | 14 |
| \(\sin 2\alpha\), \(\cos 2\alpha\) | [9.7] | 13 |
| twierdzenie Pitagorasa | [10.1] | 15 |
| twierdzenie sinusów / cosinusów | [10.2], [10.3] | 15 |
| pole trójkąta (wysokość, kąt, Heron) | [10.4] | 16 |
| trójkąt równoboczny — wysokość, pole | [10.6] | 16 |
| podobieństwo trójkątów, skala | [10.8], [10.23] | 17, 22 |
| twierdzenie Talesa | [10.10] | 18 |
| pole i obwód koła, wycinek koła, długość łuku | [10.11], [10.12] | 18, 19 |
| kąt wpisany i środkowy | [10.13] | 19 |
| styczna do okręgu, odcinki stycznych | [10.14], [10.15], [10.16] | 19, 20 |
| pole trapezu / równoległoboku / rombu / deltoidu | [10.17]–[10.20] | 20, 21 |
| okrąg opisany na czworokącie / wpisany w czworokąt | [10.21], [10.22] | 21, 22 |
| długość odcinka, środek odcinka | [11.1], [11.2] | 22 |
| równanie prostej (kierunkowe / ogólne) | [11.3], [11.6] | 23 |
| prosta przez dwa punkty | [11.5], [11.7] | 23 |
| proste równoległe / prostopadłe | [11.8], [11.9] | 24 |
| odległość punktu od prostej | [11.10] | 24 |
| równanie okręgu | [11.11] | 24 |
| wektory, działania na wektorach | [11.12] | 25 |
| symetrie, przesunięcie o wektor | [11.13] | 25 |
| środek ciężkości trójkąta | [11.15] | 26 |
| objętość / pole prostopadłościanu, graniastosłupa | [12.2], [12.3] | 26, 27 |
| ostrosłup — objętość | [12.4] | 27 |
| walec / stożek / kula | [12.5], [12.6], [12.7] | 27, 28 |
| permutacje, wariacje, kombinacje | [13.1]–[13.4] | 28 |
| prawdopodobieństwo klasyczne \(\frac{|A|}{|\Omega|}\) | [14.2] | 29 |
| zdarzenie przeciwne, suma zdarzeń | [14.1] | 29 |
| schemat Bernoullego, \(k\) sukcesów w \(n\) próbach | [14.3] | 29 |
| prawdopodobieństwo warunkowe, drzewko | [14.4], [14.5] | 30 |
| wartość oczekiwana | [14.7] | 30 |
| średnia arytmetyczna / geometryczna / ważona | [15.1], [15.2], [15.5] | 31 |
| mediana | [15.6] | 32 |
| wariancja, odchylenie standardowe | [15.7] | 32 |
| liczenie pochodnej | [16.1], [16.2] | 32, 33 |
| równanie stycznej do wykresu | [16.3] | 33 |
