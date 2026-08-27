# Zadanie 9, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad9.py`. Projekt dydaktyczny i uzasadnienie metody:
[../issues/projekt-zad9-zad10-2024-grudzien.md](../issues/projekt-zad9-zad10-2024-grudzien.md).

Napisane **od nowa 2026-08-28, na wzór zadań 7 i 8**. Poprzednia wersja miała osiem
kroków, siedem linijek w rozwiązaniu opisowym (czyli rozjazd), liczyła ogniwa w głowie
i nie pokazywała paraboli, przez co wniosek o przedziale niósł wyłącznie zwinięty opis
pod krokiem. Ta wersja ma dwadzieścia jeden kroków, jeden do jednego z linijkami rachunku.

## Co się zmieniło wobec starej wersji

| dawniej | teraz |
|---|---|
| \(x(x-6)\) od razu na \(x^{2}-6x\) | osobny krok z ogniwem \(x \cdot x - x \cdot 6\) |
| współczynniki wchodziły prosto do delty | osobna linijka „Współczynniki: \(a = 1\), \(b = -6\), \(c = -7\)" |
| podstawienie do delty od razu na \(36+28\) | osobny krok: najpierw podstawienie w nawiasach, potem rozpisanie |
| \(x_{1}\) i \(x_{2}\) w jednym kroku | dwa tory liczone **po kolei**, wynik pierwszego czeka na górze kadru |
| \(\dfrac{6-8}{2}\) od razu na \(-1\) | osobne kroki z \(\dfrac{-2}{2}\) i \(\dfrac{14}{2}\) |
| paraboli nie było w kadrze | trzy ostatnie kroki rysują szkic: parabola, fragment pod osią, zapis przedziału |

## Treść

Rozwiąż nierówność \(x(x-6) \le 7\). Zapisz obliczenia. Zadanie otwarte, 2 punkty.

Wynik: \(x \in \langle -1,\ 7\rangle\), zgodny z kluczem CKE.

| Kryterium z klucza | Punkty | Krok |
|---|---|---|
| nierówność w postaci \(x^{2}-6x-7 \le 0\) | 0, etap konieczny | 4 |
| pierwiastki \(x_{1} = -1\), \(x_{2} = 7\) | 1 | 18 |
| zbiór rozwiązań \(\langle -1,\ 7\rangle\) | 1 | 21 |

## Kroki

| # | Stan po kroku | Zielone |
|---|---|---|
| 1 | \(x(x - 6) \le 7\) | nic |
| 2 | \(x \cdot x - x \cdot 6 \le 7\) | dwa nowe \(x\) i kropki mnożenia |
| 3 | \(x^{2} - 6x \le 7\) | wykładnik \(2\) |
| 4 | \(x^{2} - 6x - 7 \le 0\) | minus przy siódemce i zero |
| 5 | \(a = 1\), \(b = -6\), \(c = -7\) | znaki minus i nowa jedynka |
| 6 | \(\Delta = (-6)^{2} - 4 \cdot 1 \cdot (-7)\) | wstawiane liczby |
| 7 | \(\Delta = 36 + 28\) | plus przed \(28\) |
| 8 | \(\Delta = 64\) | nic |
| 9 | \(\sqrt{\Delta} = 8\) | \(8\) |
| 10 | \(x_{1,2} = \dfrac{-(-6) \pm 8}{2 \cdot 1}\) | wstawiane liczby |
| 11 | \(x_{1,2} = \dfrac{6 \pm 8}{2}\) | \(6\) z dwóch minusów |
| 12 | \(x_{1} = \dfrac{6 - 8}{2}\) | znak minus |
| 13 | \(x_{1} = \dfrac{-2}{2}\) | \(-2\) |
| 14 | \(x_{1} = -1\) | nic |
| 15 | wynik odjeżdża w górę, wjeżdża \(x_{2} = \dfrac{6+8}{2}\) | nic, krok przenoszący |
| 16 | \(x_{2} = \dfrac{14}{2}\) | \(14\) |
| 17 | \(x_{2} = 7\) | nic |
| 18 | \(x_{1} = -1\), \(x_{2} = 7\) w jednej linijce | nic |
| 19 | szkic paraboli ramionami w górę przez \(-1\) i \(7\) | nic |
| 20 | fragment pod osią i odcinek na osi | fragment i odcinek |
| 21 | \(x \in \langle -1,\ 7\rangle\) | nic |

Rysunek w krokach 19 do 21 jest **szkicem**: oś \(x\), dwa podpisane punkty, gładka
parabola. Bez siatki, bez osi \(y\), bez skali. Chodzi o kształt i o to, gdzie parabola
leży pod osią.

## Co zmierzono po renderze (2026-08-28)

- `tools/styk-klatek.sh`: dwadzieścia styków, od 0,99900 do 0,99995, bez zastrzeżeń.
- `tools/zielen-krokow.py`: każdy krok zaczyna i kończy się bez zieleni.
- `tools/test-krokow.js --zadania=8`: dwa ziarna, bez zastrzeżeń.
- Kroki 19 i 20 dostały dodatkowy postój 0,35 s na końcu. Bez niego styki 19→20 i 20→21
  schodziły poniżej progu 0,999: rysunek zajmuje pół kadru gładkimi krzywymi, a koder
  H.264 potrzebuje kilku klatek bez ruchu, żeby ostatnia klatka kroku zgadzała się
  z pierwszą klatką następnego. Wydłużenie postoju do 0,8 s nie dało już nic.
