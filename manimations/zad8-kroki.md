# Zadanie 8, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

**Ten plik był nieaktualny od 2026-08-23** i opisywał siedem kroków w innej kolejności,
czyli scenę sprzed przepisania `solutionZad8.py`. Przepisany 2026-08-26 pod stan faktyczny,
przy okazji rozbicia kroku z przenoszeniem stron. Projekt tamtej zmiany:
`issues/projekt-zad8-2024-grudzien.md`.

Zadanie jest **otwarte, za 3 punkty**, więc każdy punkt z kryteriów CKE ma swoje miejsce:

| Kryterium z klucza | Punkty | Gdzie to jest |
|---|---|---|
| Zapisane założenie (dziedzina): \(x \ne 1\) | 1 | krok 2, i zostaje w kadrze do końca |
| Równanie bez ułamków, np. \(2(x+3)=x\) | 1 | krok 5 |
| Wynik \(x=-6\) należący do dziedziny | 1 | kroki 9 i 10 |

## Treść

Rozwiąż równanie: \[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\] Zapisz konieczne założenie i obliczenia.

Wynik: \(x = -6\).

## Kroki

Dziesięć kroków, tyle samo pozycji w rozwiązaniu opisowym: osiem linijek rachunku,
założenie nad nimi i zdanie sprawdzające pod nimi.

| # | Zapis po kroku | Co się dzieje |
|---|---|---|
| 1 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2}\) | równanie z zadania, bez koloru |
| 2 | pod spodem \(x \ne 1\) | założenie, zostaje w kadrze do końca filmu |
| 3 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)}\) | wyłączamy dwójkę, widać ten sam nawias w obu mianownikach |
| 4 | to samo z dopiskiem \(\big/ \cdot\, 2(x-1)\) | zapowiedź działania, nic się jeszcze nie przelicza |
| 5 | \(2(x+3) = x\) | mnożymy obie strony, mianowniki się skracają |
| 6 | \(2x + 6 = x\) | opuszczamy nawias, dwójka mnoży osobno \(x\) i osobno \(3\) |
| 7 | \(2x = x - 6\) | przenosimy **samą liczbę**, szóstka zmienia znak |
| 8 | \(2x - x = -6\) | przenosimy **samą niewiadomą**, \(x\) zmienia znak |
| 9 | \(x = -6\) | \(2x\) bez jednego \(x\) to \(x\) |
| 10 | pod spodem \(-6 \ne 1\) | wynik wraca do założenia i mieści się w dziedzinie |

Kroki 7 i 8 były do 2026-08-26 jednym krokiem. Przenosiły naraz szóstkę w prawo i \(x\)
w lewo, czyli dwa składniki zmieniały znak w jednym ruchu, a to jest właśnie to miejsce,
w którym uczeń gubi minus.

## Dlaczego krok 5 nie jest rozbity

Kusi, bo w jednym kroku dzieje się mnożenie obu stron i skracanie po obu stronach naraz.
Powód jest techniczny, nie dydaktyczny: stan pośredni musiałby wyglądać jak
\(\dfrac{(x+3)\cdot 2(x-1)}{x-1} = \dfrac{x \cdot 2(x-1)}{2(x-1)}\), a scena skaluje
**wszystkie** kroki do najszerszego stanu. Jedna szeroka klatka zmniejszyłaby cały film.

## Czego film nie pokazuje

Sprawdzenia przez podstawienie
(\(\frac{-6+3}{-6-1} = \frac{-3}{-7} = \frac{3}{7}\) oraz \(\frac{-6}{-14} = \frac{3}{7}\)).
Klucz CKE tego nie wymaga, a film sprawdza założenie, nie wynik. Powiedz, jeśli uważasz,
że warto dorobić z tego jedenasty krok.
