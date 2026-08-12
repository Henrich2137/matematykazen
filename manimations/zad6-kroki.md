# Zadanie 6 — kroki rozwiązania do sprawdzenia

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.
Wzór z tablic: [6] wzory skróconego mnożenia, **s. 7** (`formulasPage` zadania jest już na 7).

## Treść

Dla każdej liczby rzeczywistej \(x\) różnej od \(-1\), \(0\) oraz \(1\) wartość wyrażenia

\[\frac{x}{x^{2} - 1} : \frac{3x^{2}}{x + 1}\]

jest równa wartości wyrażenia:

- A. \(\dfrac{x}{x-1}\)
- **B. \(\dfrac{1}{3x^{2}-3x}\)** ← poprawna (`correctAnswerIndex: 1`)
- C. \(-3x\)
- D. \(-\dfrac{1}{3x}\)

## Proponowane kroki

Pięć kroków, sześć kropek. Na zielono to, co się w danym kroku rusza.

### Krok 1 — zapisujemy wyrażenie

\[\frac{x}{x^{2} - 1} : \frac{3x^{2}}{x + 1}\]

*Opis:* Zapisujemy wyrażenie z zadania.

### Krok 2 — rozkładamy mianownik ze wzoru skróconego mnożenia

\[\frac{x}{\color{green}{x^{2}-1}} : \frac{3x^{2}}{x+1} \;\longrightarrow\; \frac{x}{\color{green}{(x-1)(x+1)}} : \frac{3x^{2}}{x+1}\]

\(a^{2}-b^{2}=(a-b)(a+b)\), czyli \(x^{2}-1=(x-1)(x+1)\). Robimy to **najpierw**, bo dopiero
w tej postaci widać, co się da skrócić.

*Opis:* Mianownik rozkładamy ze wzoru skróconego mnożenia: \(a^{2}-b^{2}=(a-b)(a+b)\), czyli \(x^{2}-1=(x-1)(x+1)\).

### Krok 3 — dzielenie zamieniamy na mnożenie przez odwrotność

\[\frac{x}{(x-1)(x+1)} \;{\color{green}:}\; \frac{3x^{2}}{x+1} \;\longrightarrow\; \frac{x}{(x-1)(x+1)} \;{\color{green}\cdot}\; \frac{\color{green}{x+1}}{\color{green}{3x^{2}}}\]

Drugi ułamek staje na głowie, a znak dzielenia zmienia się w mnożenie.

*Opis:* Dzielenie przez ułamek to mnożenie przez jego odwrotność — drugi ułamek odwracamy.

### Krok 4 — skracamy

\[\frac{x}{(x-1)(x+1)} \cdot \frac{x+1}{3x^{2}} \;\longrightarrow\; \frac{1}{x-1} \cdot \frac{1}{3x}\]

Skraca się \((x+1)\) — jest w liczniku i w mianowniku — oraz jedno \(x\) z \(x^{2}\).
Właśnie po to były założenia \(x \ne -1,\ 0,\ 1\): gwarantują, że nie dzielimy przez zero.

> **Moja decyzja, do korekty:** dwa skrócenia w jednym kroku. Rozbiłem to najpierw na dwa
> osobne, ale wtedy pośredni zapis \(\frac{x}{(x-1)}\cdot\frac{1}{3x^{2}}\) wygląda jak stan,
> w którym nikt normalnie nie zatrzymuje ręki. Jeśli wolisz wolniej — powiedz, dorobię krok.

*Opis:* Skracamy \((x+1)\) oraz jedno \(x\) z \(x^{2}\). Po to były założenia \(x \ne -1,\,0,\,1\) — dzięki nim nic tu nie jest zerem.

### Krok 5 — mnożymy ułamki

\[\frac{1}{x-1} \cdot \frac{1}{3x} \;\longrightarrow\; \frac{1}{3x(x-1)}\]

*Opis:* Mnożąc ułamki, mnożymy licznik przez licznik i mianownik przez mianownik.

### Krok 6 — wymnażamy mianownik, żeby zobaczyć odpowiedź

\[\frac{1}{3x(x-1)} \;\longrightarrow\; \frac{1}{3x^{2}-3x}\]

*Opis:* Wymnażamy mianownik: \(3x(x-1)=3x^{2}-3x\) — to odpowiedź **B**.

## Dlaczego pozostałe odpowiedzi są złe

| Odp. | Zapis | Skąd błąd |
|---|---|---|
| A | \(\dfrac{x}{x-1}\) | pominięcie drugiego ułamka — tak wygląda sam pierwszy składnik po skróceniu \((x+1)\) |
| **B** | \(\dfrac{1}{3x^{2}-3x}\) | **poprawna** |
| C | \(-3x\) | potraktowanie dzielenia jak mnożenia i pogubienie się w znakach |
| D | \(-\dfrac{1}{3x}\) | skrócenie \((x-1)\) z \((x+1)\), czego zrobić nie wolno — to nie są te same czynniki |
