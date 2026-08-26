# Zadanie 7, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.
Zadanie nie potrzebuje tablic, `formulasPage` jest puste i tak zostaje.

Wersja z 2026-08-21: **dwa etapy, każde równanie osobno** (polecenie Henricha). Poprzednia
wersja prowadziła oba równania równolegle w jednej klamrze; opis tamtej wersji został
w historii repo, a jej kod leży zakomentowany na dole `solutionZad7.py`.

Wersja z 2026-08-26: **czternaście kroków zamiast dwunastu**. W dwóch miejscach jeden krok
robił dwie rzeczy naraz, więc każde z nich rozbito na dwa: krok 4 wydziela samą regułę
znaku (\(a \cdot (-1)\) daje \(-a\)), a krok 10 samo uporządkowanie zapisu
(\(b \cdot 6\) daje \(6b\)). Projekt: `issues/projekt-zad7-2024-grudzien.md`.

## Treść

Para liczb \(x=-1\) i \(y=6\) jest rozwiązaniem układu

\[\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\]

Wartość wyrażenia \(a \cdot b\) jest równa:

- **A. \(-2\)** ← poprawna (`correctAnswerIndex: 0`)
- B. \(-0{,}5\)
- C. \(0{,}5\)
- D. \(2\)

## Kroki

Czternaście kroków, tyle samo linijek w rozwiązaniu opisowym. Etap pierwszy to wyliczenie
\(a\), etap drugi \(b\), etap trzeci ich iloczyn. Wyliczone \(a\) zostaje na górze kadru
przez cały drugi etap, więc na końcu obie wartości są na ekranie naraz i mogą zjechać
w jeden zapis.

### Etap 1, pierwsze równanie

| # | Zapis | Co się dzieje |
|---|---|---|
| 1 | \(\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\) | układ z zadania |
| 2 | \(ax + 3y = 20\) | bierzemy pierwsze równanie |
| 3 | \(a \cdot (-1) + 3 \cdot 6 = 20\) | podstawiamy \(x=-1\) i \(y=6\) |
| 4 | \(-a + 3 \cdot 6 = 20\) | sama reguła znaku: minus staje się znakiem wyrazu |
| 5 | \(-a + 18 = 20\) | sam rachunek: \(3 \cdot 6 = 18\) |
| 6 | \(-a = 2\) | 18 na prawą stronę |
| 7 | \(a = -2\) | obie strony przez \(-1\) |

### Etap 2, drugie równanie

| # | Zapis | Co się dzieje |
|---|---|---|
| 8 | \(x + by = 5\) | \(a=-2\) odjeżdża na górę, wjeżdża drugie równanie |
| 9 | \((-1) + b \cdot 6 = 5\) | to samo podstawienie co w kroku 3 |
| 10 | \(-1 + 6b = 5\) | sam porządek zapisu: liczba przed literą |
| 11 | \(6b = 6\) | \(-1\) na prawą stronę |
| 12 | \(b = 1\) | obie strony przez 6 |

### Etap 3, iloczyn

| # | Zapis | Co się dzieje |
|---|---|---|
| 13 | \(a \cdot b = (-2) \cdot 1\) | obie wartości schodzą się w jedną linijkę |
| 14 | \(a \cdot b = -2\) | mnożenie przez 1 nic nie zmienia |

Uwaga na pytanie: zadanie nie pyta o \(a\) ani o \(b\), tylko o **ich iloczyn**. To częste
miejsce na zgubienie punktu przez nieuwagę, dlatego mówi o tym wprost opis kroku 13.

## Dlaczego pozostałe odpowiedzi są złe

| Odp. | Skąd błąd |
|---|---|
| **A. \(-2\)** | **poprawna** |
| B. \(-0{,}5\) | policzenie \(a:b\) zamiast \(a\cdot b\), z pomyloną kolejnością |
| C. \(0{,}5\) | jak wyżej, dodatkowo zgubiony minus |
| D. \(2\) | zgubiony minus przy \(a\), np. przeczytanie \(-a=2\) jako \(a=2\) |
