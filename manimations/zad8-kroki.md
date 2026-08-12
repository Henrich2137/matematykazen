# Zadanie 8 — kroki rozwiązania do sprawdzenia

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

To zadanie **otwarte, za 3 punkty**, więc kroki są ułożone tak, żeby pokrywały się z kluczem
CKE — każdy punkt z kryteriów ma swój krok:

| Kryterium z klucza | Punkty | Krok |
|---|---|---|
| Zapisane założenie (dziedzina): \(x \ne 1\) | 1 | krok 3 |
| Równanie bez ułamków, np. \(2(x+3)=x\) | 1 | krok 4 |
| Wynik \(x=-6\) i sprawdzenie, że należy do dziedziny | 1 | krok 7 |

## Treść

Rozwiąż równanie: \[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\] Zapisz konieczne założenie i obliczenia.

Wynik: \(x = -6\).

## Proponowane kroki

Sześć kroków, siedem kropek.

### Krok 1 — zapisujemy równanie

\[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\]

*Opis:* Zapisujemy równanie z zadania.

### Krok 2 — wyłączamy dwójkę w drugim mianowniku

\[\frac{x+3}{x-1} = \frac{x}{\color{green}{2x-2}} \;\longrightarrow\; \frac{x+3}{x-1} = \frac{x}{\color{green}{2(x-1)}}\]

To jest sedno tego zadania: po wyłączeniu dwójki widać, że **oba mianowniki to ten sam
nawias** \((x-1)\), tylko jeden ma przy sobie dwójkę.

*Opis:* W drugim mianowniku wyłączamy 2 przed nawias: \(2x-2=2(x-1)\). Teraz widać, że w obu mianownikach siedzi ten sam nawias \((x-1)\).

### Krok 3 — zapisujemy założenie (za to jest punkt)

Pod równaniem pojawia się \(x \ne 1\) i **zostaje tam do końca**.

Mianownik nie może być zerem, a \(x-1=0\) dla \(x=1\). Drugi mianownik \(2(x-1)\) zeruje się
dla tego samego \(x\), więc jedno założenie załatwia oba.

*Opis:* Mianownik nie może być zerem, więc \(x-1\ne 0\), czyli \(x\ne 1\). Bez tego zapisu klucz CKE odbiera punkt, nawet gdy wynik jest dobry.

### Krok 4 — mnożymy obie strony przez \(2(x-1)\) i ułamki znikają

\[\frac{x+3}{x-1} = \frac{x}{2(x-1)} \quad\Big/\cdot\ 2(x-1) \;\longrightarrow\; 2(x+3) = x\]

Po lewej \((x-1)\) skraca się i zostaje \(2(x+3)\); po prawej skraca się całe \(2(x-1)\)
i zostaje samo \(x\).

*Opis:* Mnożymy obie strony przez \(2(x-1)\) — mianowniki się skracają i zostaje równanie bez ułamków.

### Krok 5 — opuszczamy nawias

\[2(x+3) = x \;\longrightarrow\; 2x+6 = x\]

*Opis:* Opuszczamy nawias: \(2(x+3)=2x+6\).

### Krok 6 — porządkujemy stronami

\[2x+6 = x \;\longrightarrow\; 2x-x = -6\]

*Opis:* Iksy na lewo, liczby na prawo — każdy przeniesiony składnik zmienia znak.

### Krok 7 — wynik

\[2x-x = -6 \;\longrightarrow\; x = -6\]

I jeszcze jedno, o czym łatwo zapomnieć: \(-6 \ne 1\), więc wynik mieści się w dziedzinie
i jest rozwiązaniem równania.

*Opis:* Zostaje \(x=-6\). Sprawdzamy jeszcze założenie: \(-6\ne 1\), więc wynik należy do dziedziny — to jest rozwiązanie równania.

## Uwaga o tym, czego film NIE pokazuje

Film prowadzi przez rachunek. Nie pokazuje sprawdzenia przez podstawienie
(\(\frac{-6+3}{-6-1}=\frac{-3}{-7}=\frac{3}{7}\) i \(\frac{-6}{-14}=\frac{3}{7}\) ✓) — jest w
„Pokaż więcej" i nie jest wymagane przez klucz. Powiedz, jeśli uważasz, że warto dorobić
z tego ósmy krok.
