# 8. Ciągi

Strony **9–10** tablicy.

## [8.1] Ciąg arytmetyczny — \(n\)-ty wyraz — s. 9, środek

Wzór na \(n\)-ty wyraz ciągu arytmetycznego \((a_n)\), określonego dla \(n \ge 1\), o pierwszym wyrazie \(a_1\) i różnicy \(r\):

\[a_n = a_1 + (n - 1)r\]

## [8.2] Ciąg arytmetyczny — suma \(n\) początkowych wyrazów — s. 9, środek

Wzory na sumę \(S_n\) początkowych \(n\) wyrazów ciągu arytmetycznego:

\[S_n = \frac{a_1 + a_n}{2} \cdot n \qquad S_n = \frac{2a_1 + (n - 1)r}{2} \cdot n\]

## [8.3] Ciąg arytmetyczny — własność sąsiednich wyrazów — s. 9, środek

Dla sąsiednich wyrazów ciągu arytmetycznego \((a_n)\) prawdziwa jest równość:

\[a_n = \frac{a_{n-1} + a_{n+1}}{2} \quad \text{dla } n \ge 2\]

## [8.4] Ciąg geometryczny — \(n\)-ty wyraz — s. 9, dół

Wzór na \(n\)-ty wyraz ciągu geometrycznego \((a_n)\), określonego dla \(n \ge 1\), o pierwszym wyrazie \(a_1\) i ilorazie \(q\):

\[a_n = a_1 \cdot q^{n-1} \quad \text{dla } n \ge 2\]

## [8.5] Ciąg geometryczny — suma \(n\) początkowych wyrazów — s. 9, dół

Wzory na sumę \(S_n\) początkowych \(n\) wyrazów ciągu geometrycznego:

\[S_n = a_1 \cdot \frac{1 - q^n}{1 - q} \quad \text{dla } q \ne 1 \qquad S_n = n \cdot a_1 \quad \text{dla } q = 1\]

## [8.6] Ciąg geometryczny — własność sąsiednich wyrazów — s. 10, góra

Dla sąsiednich wyrazów ciągu geometrycznego \((a_n)\) prawdziwa jest równość:

\[(a_n)^2 = a_{n-1} \cdot a_{n+1} \quad \text{dla } n \ge 2\]

## [8.7] Suma wyrazów nieskończonego ciągu geometrycznego — s. 10, góra

Dany jest nieskończony ciąg geometryczny \((a_n)\), określony dla \(n \ge 1\), o ilorazie \(q\). Niech \((S_n)\) oznacza ciąg sum początkowych wyrazów ciągu \((a_n)\), to znaczy ciąg określony wzorem \(S_n = a_1 + a_2 + \ldots + a_n\) dla \(n \ge 1\).

Jeżeli \(|q| < 1\), to ciąg \((S_n)\) ma granicę równą:

\[S = \lim_{n \to \infty} S_n = \frac{a_1}{1 - q}\]

Granicę tę nazywamy sumą wszystkich wyrazów ciągu geometrycznego \((a_n)\).

## [8.8] Twierdzenie o granicy sumy, różnicy, iloczynu i ilorazu ciągów zbieżnych — s. 10, środek

Jeżeli ciągi \((a_n)\) i \((b_n)\), określone dla każdej liczby naturalnej \(n \ge 1\), są zbieżne i \(\lim\limits_{n \to \infty} a_n = a\) oraz \(\lim\limits_{n \to \infty} b_n = b\), to ciągi \((a_n + b_n)\), \((a_n - b_n)\), \((a_n \cdot b_n)\) są zbieżne, a ponadto:

\[\lim_{n \to \infty} (a_n + b_n) = a + b \qquad \lim_{n \to \infty} (a_n - b_n) = a - b \qquad \lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b\]

Jeżeli ponadto \(b_n \ne 0\) dla \(n \ge 1\) oraz \(b \ne 0\), to ciąg \(\left( \frac{a_n}{b_n} \right)\) jest zbieżny i:

\[\lim_{n \to \infty} \left( \frac{a_n}{b_n} \right) = \frac{a}{b}\]

## [8.9] Twierdzenie o trzech ciągach — s. 10, dół

Jeżeli wyrazy ciągów \((a_n)\), \((b_n)\) i \((c_n)\), określonych dla \(n \ge 1\), spełniają nierówność \(a_n \le b_n \le c_n\) dla \(n \ge 1\), a ciągi \((a_n)\) i \((c_n)\) są zbieżne do wspólnej granicy \(\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} c_n = g\), to ciąg \((b_n)\) jest zbieżny, a ponadto \(\lim\limits_{n \to \infty} b_n = g\).
