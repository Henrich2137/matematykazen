# Zadanie 9 — kroki rozwiązania do sprawdzenia

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.
Wzory z tablic: [7] funkcja kwadratowa — wyróżnik i miejsca zerowe, **s. 8**
(`formulasPage` zadania jest już na 8; w TODO leży osobny pomysł, żeby dopisać też s. 7).

To zadanie **otwarte, za 2 punkty**, więc kroki są ułożone pod klucz CKE:

| Kryterium z klucza | Punkty | Krok |
|---|---|---|
| Nierówność w postaci \(x^{2}-6x-7\le 0\) | 0 (etap konieczny) | krok 3 |
| Obliczone miejsca zerowe \(x=-1\) i \(x=7\) | 1 | krok 7 |
| Zapisany zbiór rozwiązań \(\langle -1,\ 7\rangle\) | 1 | krok 8 |

## Treść

Rozwiąż nierówność \(x(x-6)\le 7\). Zapisz obliczenia.

Wynik: \(x \in \langle -1,\ 7\rangle\).

## Proponowane kroki

Siedem kroków, osiem kropek.

### Krok 1 — zapisujemy nierówność

\[x(x-6) \le 7\]

*Opis:* Zapisujemy nierówność z zadania.

### Krok 2 — wymnażamy nawias

\[x^{2}-6x \le 7\]

*Opis:* Wymnażamy nawias: \(x(x-6)=x^{2}-6x\).

### Krok 3 — przenosimy wszystko na lewo (punkt konieczny)

\[x^{2}-6x-7 \le 0\]

Dopiero teraz to jest nierówność kwadratowa w postaci, z którą umiemy pracować: po prawej
stronie zero.

*Opis:* Przenosimy 7 na lewą stronę, żeby po prawej zostało zero — bez tego nie ma jak korzystać z miejsc zerowych.

### Krok 4 — liczymy wyróżnik

\[\Delta = (-6)^{2} - 4 \cdot 1 \cdot (-7)\]

Tu siedzi najczęstszy błąd całego zadania: \(c=-7\), więc \(-4ac\) daje **plus** 28.

*Opis:* Wyróżnik \(\Delta=b^{2}-4ac\), gdzie \(a=1\), \(b=-6\), \(c=-7\). Uwaga na znaki: \(c\) jest ujemne, więc \(-4ac\) wychodzi na plus.

### Krok 5 — wynik wyróżnika

\[\Delta = 64 \qquad \sqrt{\Delta} = 8\]

*Opis:* \(36+28=64\), a \(\sqrt{64}=8\).

### Krok 6 — podstawiamy do wzorów na miejsca zerowe

\[x_{1} = \frac{6-8}{2} \qquad x_{2} = \frac{6+8}{2}\]

*Opis:* Miejsca zerowe: \(x_{1,2}=\frac{-b\pm\sqrt{\Delta}}{2a}\). Skoro \(b=-6\), to \(-b=6\).

### Krok 7 — miejsca zerowe (punkt)

\[x_{1} = -1 \qquad x_{2} = 7\]

*Opis:* Wychodzi \(x_{1}=-1\) oraz \(x_{2}=7\). Za samo to klucz CKE daje punkt.

### Krok 8 — odczytujemy zbiór rozwiązań (punkt)

\[x \in \langle -1,\ 7\rangle\]

Współczynnik przy \(x^{2}\) jest dodatni, więc parabola ma ramiona **w górę** — wartości
mniejsze lub równe zero przyjmuje **między** miejscami zerowymi. Przedział jest **domknięty**,
bo w nierówności jest \(\le\), a nie \(<\).

*Opis:* Współczynnik przy \(x^{2}\) jest dodatni, więc ramiona paraboli idą w górę i wartości \(\le 0\) są **między** miejscami zerowymi. Przedział domknięty, bo nierówność jest nieostra: \(x\in\langle -1,\ 7\rangle\).

> **Moja decyzja, do korekty.** Film nie rysuje paraboli — pokazuje sam rachunek, a wniosek
> „ramiona w górę → między miejscami zerowymi" jest tylko w opisie pod krokiem 8. Powód:
> to zadanie ma już widżet `widgetNierownoscKwadratowa`, który rysunek pokazuje
> interaktywnie, więc film by go dublował. Jeśli wolisz, żeby parabola pojawiła się też
> w filmie — powiedz, to osobna scena i osobny krok.
