# 11. Geometria analityczna na płaszczyźnie kartezjańskiej

Strony **22–26** tablicy (sekcja kończy się na górze s. 26, przed stereometrią).

> **Rysunki:** [11.1]/[11.2] (odcinek w układzie współrzędnych) i [11.3] (prosta z kątem
> nachylenia \(\alpha\)) mają w PDF-ie rysunki poglądowe — nie wnoszą wzorów ponad to, co
> jest w tekście. W razie potrzeby: `../wybrane_wzory_matematyczne.pdf`, s. 22–23.

## [11.1] Długość odcinka — s. 22, środek/dół

Długość odcinka \(AB\) o końcach w punktach \(A = (x_A, y_A)\) oraz \(B = (x_B, y_B)\) jest równa:

\[|AB| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}\]

## [11.2] Współrzędne środka odcinka — s. 22, dół

Współrzędne środka \(S = (x_S, y_S)\) odcinka \(AB\) o końcach w punktach \(A = (x_A, y_A)\) oraz \(B = (x_B, y_B)\) są równe:

\[x_S = \frac{x_A + x_B}{2} \qquad y_S = \frac{y_A + y_B}{2}\]

## [11.3] Równanie kierunkowe prostej — s. 23, góra

Jeżeli prosta nie jest równoległa do osi \(Oy\), to można opisać ją równaniem kierunkowym:

\[y = ax + b\]

Liczba \(a\) to współczynnik kierunkowy prostej:

\[a = \operatorname{tg} \alpha\]

Prosta o równaniu \(y = ax + b\) przecina oś \(Oy\) w punkcie \((0, b)\).

## [11.4] Prosta o danym współczynniku kierunkowym przechodząca przez punkt — s. 23, góra/środek

Równanie kierunkowe prostej o danym współczynniku kierunkowym \(a\), która przechodzi przez punkt \(P = (x_0, y_0)\):

\[y = a(x - x_0) + y_0\]

## [11.5] Prosta przechodząca przez dwa punkty — postać kierunkowa — s. 23, środek

Równanie kierunkowe prostej, która przechodzi przez dwa dane punkty \(A = (x_A, y_A)\) oraz \(B = (x_B, y_B)\):

\[y - y_A = a(x - x_A)\]

gdzie:

\[a = \frac{y_B - y_A}{x_B - x_A} \quad \text{gdy } x_B \ne x_A\]

## [11.6] Równanie ogólne prostej — s. 23, środek/dół

\[Ax + By + C = 0, \quad \text{gdzie } A, B, C \in \mathbb{R} \text{ i } A^2 + B^2 \ne 0\]

Jeżeli \(A = 0\), to prosta jest równoległa do osi \(Ox\); jeżeli \(B = 0\), to prosta jest równoległa do osi \(Oy\); jeżeli \(C = 0\), to prosta przechodzi przez początek układu współrzędnych.

## [11.7] Prosta przechodząca przez dwa punkty — postać ogólna — s. 23, dół

Równanie ogólne prostej, która przechodzi przez dwa dane punkty \(A = (x_A, y_A)\) oraz \(B = (x_B, y_B)\):

\[(y - y_A)(x_B - x_A) - (y_B - y_A)(x - x_A) = 0\]

## [11.8] Proste równoległe — s. 24, góra

Dwie proste o równaniach kierunkowych \(y = a_1 x + b_1\) oraz \(y = a_2 x + b_2\) są równoległe wtedy i tylko wtedy, gdy:

\[a_1 = a_2\]

Dwie proste o równaniach ogólnych \(A_1 x + B_1 y + C_1 = 0\) oraz \(A_2 x + B_2 y + C_2 = 0\) są równoległe wtedy i tylko wtedy, gdy:

\[A_1 \cdot B_2 - A_2 \cdot B_1 = 0\]

## [11.9] Proste prostopadłe — s. 24, góra/środek

Dwie proste o równaniach kierunkowych \(y = a_1 x + b_1\) oraz \(y = a_2 x + b_2\) są prostopadłe wtedy i tylko wtedy, gdy:

\[a_1 \cdot a_2 = -1\]

Dwie proste o równaniach ogólnych \(A_1 x + B_1 y + C_1 = 0\) oraz \(A_2 x + B_2 y + C_2 = 0\) są prostopadłe wtedy i tylko wtedy, gdy:

\[A_1 \cdot A_2 + B_1 \cdot B_2 = 0\]

## [11.10] Odległość punktu od prostej — s. 24, środek

Odległość \(d\) punktu \(P(x_0, y_0)\) od prostej o równaniu ogólnym \(Ax + By + C = 0\) jest równa:

\[d = \frac{|A \cdot x_0 + B \cdot y_0 + C|}{\sqrt{A^2 + B^2}}\]

## [11.11] Równanie okręgu — s. 24, dół

Równanie okręgu o środku \(S = (a, b)\) i promieniu \(r > 0\) w postaci kanonicznej:

\[(x - a)^2 + (y - b)^2 = r^2\]

Równanie okręgu o środku \(S = (a, b)\) i promieniu \(r > 0\) w postaci ogólnej:

\[x^2 + y^2 - 2ax - 2by + c = 0\]

gdzie \(c = a^2 + b^2 - r^2\).

## [11.12] Wektory — współrzędne, długość, działania — s. 25, góra

Dane są punkty \(A = (x_A, y_A)\) oraz \(B = (x_B, y_B)\). Współrzędne wektora \(\overrightarrow{AB}\) zaczepionego w punkcie \(A\):

\[\overrightarrow{AB} = [x_B - x_A, \; y_B - y_A]\]

Jeżeli \(\vec{u} = [u_1, u_2]\) oraz \(\vec{v} = [v_1, v_2]\) są wektorami oraz \(a \in \mathbb{R}\), to:

\[\vec{u} + \vec{v} = [u_1 + v_1, \; u_2 + v_2] \qquad a \cdot \vec{u} = [a \cdot u_1, \; a \cdot u_2]\]

Długością \(|\vec{u}|\) wektora \(\vec{u} = [u_1, u_2]\) nazywamy liczbę:

\[|\vec{u}| = \sqrt{(u_1)^2 + (u_2)^2}\]

## [11.13] Przekształcenia geometryczne — s. 25, środek

Przesunięcie o wektor \(\vec{u} = [a, b]\) przekształca punkt \(P = (x, y)\) na punkt \(P' = (x + a, y + b)\).

Symetria osiowa \(S_{Ox}\) względem osi \(Ox\) przekształca punkt \(P = (x, y)\) na punkt \(P' = (x, -y)\).

Symetria osiowa \(S_{Oy}\) względem osi \(Oy\) przekształca punkt \(P = (x, y)\) na punkt \(P' = (-x, y)\).

Symetria środkowa \(S_K\) względem punktu \(K = (a, b)\) przekształca punkt \(P = (x, y)\) na punkt \(P' = (2a - x, 2b - y)\).

W szczególności symetria środkowa względem początku układu współrzędnych przekształca punkt \(P = (x, y)\) na punkt \(P' = (-x, -y)\).

## [11.14] Pole trójkąta z współrzędnych wierzchołków — s. 25, dół

Pole trójkąta \(ABC\) o wierzchołkach \(A = (x_A, y_A)\), \(B = (x_B, y_B)\) oraz \(C = (x_C, y_C)\) jest równe:

\[P_{\Delta ABC} = \frac{1}{2} \cdot \left| (x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A) \right|\]

## [11.15] Współrzędne środka ciężkości trójkąta — s. 26, góra

Współrzędne środka ciężkości \(S = (x_S, y_S)\) trójkąta \(ABC\) o wierzchołkach \(A = (x_A, y_A)\), \(B = (x_B, y_B)\) oraz \(C = (x_C, y_C)\), czyli punktu przecięcia jego środkowych:

\[x_S = \frac{x_A + x_B + x_C}{3} \qquad y_S = \frac{y_A + y_B + y_C}{3}\]
