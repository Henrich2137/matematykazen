# Zadanie 8, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Napisane od nowa 2026-08-27 razem ze sceną `solutionZad8.py`. Projekt dydaktyczny
i uzasadnienie metody: [../issues/spec-zad8-2024-grudzien.md](../issues/spec-zad8-2024-grudzien.md).

Zadanie jest **otwarte, za 3 punkty**, więc każde kryterium ma swoje miejsce:

| Kryterium z klucza | Punkty | Gdzie to jest |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | krok 2, i zostaje w kadrze do końca filmu |
| równanie bez ułamków, np. \(2(x+3) = x\) | 1 | krok 6 |
| wynik \(x = -6\) należący do dziedziny | 1 | krok 10 |

## Treść

Rozwiąż równanie: \[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\] Zapisz konieczne założenie i obliczenia.

Wynik: \(x = -6\).

## Metoda

Wspólny mianownik zamiast mnożenia na krzyż i zamiast równania kwadratowego: prawy mianownik
to \(2(x-1)\), więc najpierw mnożymy obie strony przez \((x-1)\) i skracamy nawias, a potem
przez \(2\). Dlaczego nie przez deltę: spec, sekcja o metodzie.

## Kroki

Dziesięć kroków, tyle samo linijek rachunku w rozwiązaniu opisowym.

| # | Zapis po kroku | Co się dzieje | Zieleń |
|---|---|---|---|
| 1 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2}\) | równanie z zadania | brak |
| 2 | pod spodem \(x \ne 1\) | założenie, zostaje w kadrze do końca | całe założenie, bo się pojawia |
| 3 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)}\) | wyłączamy dwójkę, w obu mianownikach ten sam nawias | prawy ułamek |
| 4 | \(\dfrac{(x+3)(x-1)}{x-1} = \dfrac{x(x-1)}{2(x-1)}\) | mnożymy obie strony przez \((x-1)\) | dopisane nawiasy w licznikach |
| 5 | \(x + 3 = \dfrac{x}{2}\) | skracamy \((x-1)\) po obu stronach | nawiasy, które znikają |
| 6 | \(2(x+3) = x\) | mnożymy obie strony przez \(2\) | dwójka, która staje przed nawiasem |
| 7 | \(2x + 6 = x\) | opuszczamy nawias | szóstka, bo to nowa liczba |
| 8 | \(2x = x - 6\) | szóstka przechodzi na prawo, zmienia znak | szóstka po obu stronach przejścia |
| 9 | \(2x - x = -6\) | \(x\) przechodzi na lewo, zmienia znak | przenoszony \(x\) |
| 10 | \(x = -6\) | \(2x\) bez jednego \(x\) to \(x\) | wynik |

Dopiski działań (\(\big/ \cdot (x-1)\), \(\big/ \cdot 2\), \(\big/ - 6\), \(\big/ - x\)) pojawiają
się szare na końcu kroku, w którym powstał stan, i gasną w kroku, który to działanie wykonuje.
Tak samo wyglądają w rozwiązaniu opisowym (klasa `.rozw-dzialanie`).

## Czego film nie pokazuje

Sprawdzenia przez podstawienie \(x = -6\). Jest tylko w rozwiązaniu opisowym, jako osobna,
odkreślona część (decyzja Henricha, 2026-08-27). Klucz CKE go nie wymaga, a film kończy się
na wyniku, który stoi w kadrze razem z założeniem.

## Pułapka techniczna, na której ta scena się przejechała

**Ułamka nie wolno ciąć na argumenty `MathTex`.** Manim renderuje każdy argument osobno
i domyka w nim klamry, więc `MathTex(r"\frac{(x+3)", r"(x-1)", r"}{x-1}")` kompiluje kawałek
`\frac{(x+3)}`, czyli `\frac` z jednym argumentem, i render pada na `Missing } inserted`.
Uchwyty do wnętrza ułamka bierze się z glifów przez `rozbij_ulamek` z `_wspolne.py`; mapa
policzona, nie zgadnięta: licznik `(x+3)(x-1)` ma 10 glifów, ostatnie pięć to `(x-1)`.
