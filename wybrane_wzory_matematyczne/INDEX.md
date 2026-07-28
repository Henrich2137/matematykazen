# Tablica wzorów CKE — transkrypt

Transkrypt `wybrane_wzory_matematyczne.pdf` (CKE, 2022) rozbity na sekcje, żeby
model ładował tylko potrzebny fragment zamiast całych 31 stron.

**Jak używać:** znajdź temat w tabeli niżej → otwórz wskazany plik. Numer strony
podany przy każdym wzorze to strona PDF-a — ta sama, którą wpisuje się w
`formulasPage` w `exercises.json` (numeracja drukowana = fizyczna, bez przesunięcia).

**Konwencje:**
- Wzory w KaTeX, w tej samej konwencji co `exercises.json`: `\( ... \)` inline, `\[ ... \]` w osobnej linii — da się je kopiować do zadań bez przepisywania.
- ID w postaci `[sekcja.numer]`, np. `[2.6]`. Odwołania między wzorami przez to ID.
- Przy każdym wzorze pozycja na stronie (`góra` / `środek` / `dół`) — do szybkiego odnalezienia go wzrokiem w PDF-ie.
- Opisy słowne zachowane z oryginału CKE.
- **Pominięte:** sekcja 17 (tablica wartości funkcji trygonometrycznych, s. 34) — kilkaset odczytów, które model i tak zna; w razie potrzeby dokładnych wartości → s. 34 PDF-a.

| Sekcja | Temat | Strony | Plik |
|---|---|---|---|
| 1 | Wartość bezwzględna liczby | 4 | [01-wartosc-bezwzgledna.md](01-wartosc-bezwzgledna.md) |
| 2 | Potęgi i pierwiastki | 4–5 | [02-potegi-pierwiastki.md](02-potegi-pierwiastki.md) |
| 3 | Logarytmy | 5–6 | *(do zrobienia)* |
| 4 | Silnia. Współczynnik dwumianowy | 6 | *(do zrobienia)* |
| 5 | Wzór dwumianowy Newtona | 7 | *(do zrobienia)* |
| 6 | Wzory skróconego mnożenia | 7 | *(do zrobienia)* |
| 7 | Funkcja kwadratowa | 7–8 | *(do zrobienia)* |
| 8 | Ciągi | 9–10 | *(do zrobienia)* |
| 9 | Trygonometria | 11–14 | *(do zrobienia)* |
| 10 | Planimetria | 15–21 | *(do zrobienia)* |
| 11 | Geometria analityczna | 22–25 | *(do zrobienia)* |
| 12 | Stereometria | 26–27 | *(do zrobienia)* |
| 13 | Kombinatoryka | 28 | *(do zrobienia)* |
| 14 | Rachunek prawdopodobieństwa | 29–30 | *(do zrobienia)* |
| 15 | Parametry danych statystycznych | 31 | *(do zrobienia)* |
| 16 | Pochodna funkcji | 32–33 | *(do zrobienia)* |
| ~~17~~ | ~~Tablica wartości funkcji trygonometrycznych~~ | 34 | pominięta (patrz wyżej) |

## Skorowidz — szukaj tu, gdy zadanie dotyczy…

| Zagadnienie w zadaniu | Wzór | Strona |
|---|---|---|
| równanie/nierówność z wartością bezwzględną | [1.1], [1.4] | 4 |
| odległość na osi liczbowej | [1.1] | 4 |
| \(\sqrt{a^2}\), upraszczanie pierwiastka | [2.2] | 4 |
| pierwiastek zamieniany na potęgę | [2.5] | 5 |
| mnożenie/dzielenie/potęgowanie potęg | [2.6] | 5 |
| ujemny wykładnik, \(a^0\) | [2.4] | 5 |
| nierówność wykładnicza | [2.7] | 5 |
