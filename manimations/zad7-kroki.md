# Zadanie 7 — kroki rozwiązania do sprawdzenia

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.
Zadanie nie potrzebuje tablic — `formulasPage` jest puste i tak zostaje.

## Treść

Para liczb \(x=-1\) i \(y=6\) jest rozwiązaniem układu

\[\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\]

Wartość wyrażenia \(a \cdot b\) jest równa:

- **A. \(-2\)** ← poprawna (`correctAnswerIndex: 0`)
- B. \(-0{,}5\)
- C. \(0{,}5\)
- D. \(2\)

## Proponowane kroki

Siedem kroków, osiem kropek. Oba równania idą **równolegle**, jedno pod drugim — to jest
sedno tego zadania: nie ma tu żadnego układu do rozwiązywania, są dwa niezależne równania
z jedną niewiadomą każde.

### Krok 1 — zapisujemy układ

\[\begin{cases} ax + 3y = 20 \\ x + by = 5 \end{cases}\]

*Opis:* Zapisujemy układ z zadania. Niewiadome to tutaj \(a\) i \(b\), a nie \(x\) i \(y\) — te akurat znamy.

### Krok 2 — podstawiamy \(x=-1\) i \(y=6\)

\[\begin{cases} a \cdot (-1) + 3 \cdot 6 = 20 \\ (-1) + b \cdot 6 = 5 \end{cases}\]

*Opis:* Skoro para \(x=-1\), \(y=6\) jest rozwiązaniem, to po podstawieniu oba równania muszą być prawdziwe.

### Krok 3 — liczymy iloczyny liczbowe

\[\begin{cases} -a + 18 = 20 \\ -1 + 6b = 5 \end{cases}\]

*Opis:* Liczymy, co się da: \(3\cdot 6=18\) w pierwszym, \(b\cdot 6=6b\) w drugim.

### Krok 4 — liczby na prawą stronę

\[\begin{cases} -a = 2 \\ 6b = 6 \end{cases}\]

*Opis:* Przenosimy liczby na prawą stronę, zmieniając im znak: \(20-18=2\) oraz \(5+1=6\).

### Krok 5 — wyliczamy \(a\) i \(b\)

\[\begin{cases} a = -2 \\ b = 1 \end{cases}\]

*Opis:* Pierwsze równanie mnożymy przez \(-1\), drugie dzielimy przez 6.

### Krok 6 — wstawiamy do szukanego iloczynu

\[a \cdot b = (-2) \cdot 1\]

Uwaga na pytanie: zadanie nie pyta o \(a\) ani o \(b\), tylko o **ich iloczyn**. To częste
miejsce na zgubienie punktu przez nieuwagę.

*Opis:* Zadanie pyta o \(a\cdot b\), a nie o samo \(a\) czy \(b\) — wstawiamy obie wyliczone wartości.

### Krok 7 — wynik

\[a \cdot b = -2\]

*Opis:* \((-2)\cdot 1 = -2\) — odpowiedź **A**.

## Dlaczego pozostałe odpowiedzi są złe

| Odp. | Skąd błąd |
|---|---|
| **A. \(-2\)** | **poprawna** |
| B. \(-0{,}5\) | policzenie \(a:b\) zamiast \(a\cdot b\), z pomyloną kolejnością |
| C. \(0{,}5\) | jak wyżej, dodatkowo zgubiony minus |
| D. \(2\) | zgubiony minus przy \(a\) — np. przeczytanie \(-a=2\) jako \(a=2\) |
