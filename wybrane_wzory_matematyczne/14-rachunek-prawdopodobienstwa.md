# 14. Rachunek prawdopodobieństwa

Strony **29–30** tablicy.

## [14.1] Własności prawdopodobieństwa — s. 29, góra/środek

Niech \(\Omega\) będzie niepustym zbiorem wszystkich zdarzeń elementarnych doświadczenia losowego, natomiast \(P\) — prawdopodobieństwem określonym na podzbiorach zbioru \(\Omega\). Wtedy:

\[0 \le P(A) \le 1 \quad \text{dla każdego zdarzenia } A \subset \Omega\]

\[P(\emptyset) = 0\]

\[P(\Omega) = 1\]

\[P(A) \le P(B) \quad \text{dla każdych zdarzeń } A \text{ oraz } B \text{ takich, że } A \subset B \subset \Omega\]

\[P(A') = 1 - P(A) \quad \text{gdzie } A' \text{ oznacza zdarzenie przeciwne do zdarzenia } A \subset \Omega\]

\[P(A \cup B) = P(A) + P(B) - P(A \cap B) \quad \text{dla każdych zdarzeń } A, B \subset \Omega\]

\[P(A \cup B) \le P(A) + P(B) \quad \text{dla każdych zdarzeń } A, B \subset \Omega\]

## [14.2] Klasyczna definicja prawdopodobieństwa — s. 29, środek

Niech \(\Omega\) będzie niepustym skończonym zbiorem wszystkich zdarzeń elementarnych doświadczenia losowego. Jeżeli wszystkie zdarzenia jednoelementowe są jednakowo prawdopodobne, to prawdopodobieństwo zdarzenia losowego \(A\) jest równe:

\[P(A) = \frac{|A|}{|\Omega|}\]

gdzie \(|A|\) oznacza liczbę zdarzeń elementarnych sprzyjających zdarzeniu losowemu \(A\), natomiast \(|\Omega|\) — liczbę elementów zbioru \(\Omega\).

## [14.3] Schemat Bernoullego — s. 29, dół

Próbą Bernoullego nazywamy doświadczenie losowe, w którym otrzymujemy jeden z dwóch możliwych wyników. Jeden z nich nazywamy sukcesem, a drugi — porażką. Jeżeli prawdopodobieństwo sukcesu jest równe \(p\), to prawdopodobieństwo porażki jest równe \(q = 1 - p\).

Schematem Bernoullego nazywamy ciąg niezależnych powtórzeń prób Bernoullego.

W schemacie Bernoullego prawdopodobieństwo \(P_n(k)\) uzyskania w \(n\) próbach dokładnie \(k\) sukcesów (\(0 \le k \le n\)) jest równe:

\[P_n(k) = \binom{n}{k} \cdot p^k \cdot q^{n-k}\]

## [14.4] Prawdopodobieństwo warunkowe — s. 30, góra

Niech \(A\), \(B\) będą zdarzeniami losowymi zawartymi w \(\Omega\), przy czym \(P(B) > 0\). Prawdopodobieństwem warunkowym \(P(A|B)\) zdarzenia \(A\) pod warunkiem zaistnienia zdarzenia \(B\) nazywamy liczbę:

\[P(A|B) = \frac{P(A \cap B)}{P(B)}\]

## [14.5] Twierdzenie o prawdopodobieństwie całkowitym — s. 30, góra/środek

Jeżeli zdarzenia losowe \(B_1, B_2, \ldots, B_n\) zawarte w \(\Omega\) spełniają warunki:

1. \(B_1, B_2, \ldots, B_n\) są parami rozłączne, tzn. \(B_i \cap B_j = \emptyset\) dla \(i \ne j\), \(1 \le i \le n\), \(1 \le j \le n\)
2. \(B_1 \cup B_2 \cup \ldots \cup B_n = \Omega\)
3. \(P(B_i) > 0\) dla \(1 \le i \le n\)

to dla każdego zdarzenia losowego \(A \subset \Omega\) prawdziwa jest równość:

\[P(A) = P(A|B_1) \cdot P(B_1) + P(A|B_2) \cdot P(B_2) + \ldots + P(A|B_n) \cdot P(B_n)\]

## [14.6] Twierdzenie Bayesa — s. 30, środek/dół

Jeżeli zdarzenia losowe \(A, B_1, B_2, \ldots, B_n\) zawarte w \(\Omega\) spełniają warunki:

1. \(B_1, B_2, \ldots, B_n\) są parami rozłączne, tzn. \(B_i \cap B_j = \emptyset\) dla \(i \ne j\), \(1 \le i \le n\), \(1 \le j \le n\)
2. \(B_1 \cup B_2 \cup \ldots \cup B_n = \Omega\)
3. \(P(B_i) > 0\) dla \(1 \le i \le n\)
4. \(P(A) > 0\)

to dla każdego \(k\) (\(1 \le k \le n\)) prawdziwa jest równość:

\[P(B_k|A) = \frac{P(B_k) \cdot P(A|B_k)}{P(A|B_1) \cdot P(B_1) + P(A|B_2) \cdot P(B_2) + \ldots + P(A|B_n) \cdot P(B_n)}\]

## [14.7] Wartość oczekiwana zmiennej losowej — s. 30, dół

Niech \(X\) będzie zmienną losową o wartościach \(x_1, x_2, \ldots, x_n \in \mathbb{R}\), określoną na zbiorze \(\Omega\), przy czym \(P(\{\omega : \omega \in \Omega \text{ oraz } X(\omega) = x_i\}) = p_i\) dla \(1 \le i \le n\). Wartością oczekiwaną zmiennej losowej \(X\) nazywamy liczbę:

\[E(X) = x_1 \cdot p_1 + x_2 \cdot p_2 + \ldots + x_n \cdot p_n\]
