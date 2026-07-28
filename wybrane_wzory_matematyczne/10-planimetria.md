# 10. Planimetria

Strony **15–22** tablicy (sekcja kończy się na górze s. 22, przed geometrią analityczną).

> **Rysunki:** prawie każdy punkt tej sekcji ma w PDF-ie rysunek, którego tutaj nie ma —
> zamiast niego podane są legendy oznaczeń (co znaczy każdy symbol). Do podstawienia do
> wzoru to wystarcza. Gdy potrzebujesz samej **konfiguracji** figury — który kąt jest oparty
> na którym łuku, jak leżą punkty względem siebie — otwórz `../wybrane_wzory_matematyczne.pdf`
> na stronie podanej przy wzorze. Najbardziej zależne od rysunku są [10.7], [10.8]
> (dwa trójkąty i odpowiadające sobie wierzchołki), [10.10] (dwa przypadki Talesa)
> oraz [10.14] (trzy różne położenia stycznej, cięciwy i punktu \(P\)).

## [10.0] Oznaczenia w trójkącie \(ABC\) — s. 15, góra

Obowiązują w całej sekcji:

- \(a\), \(b\), \(c\) — długości boków w trójkącie \(ABC\)
- \(\alpha\), \(\beta\), \(\gamma\) — miary kątów wewnętrznych trójkąta leżących, odpowiednio, przy wierzchołkach \(A\), \(B\) oraz \(C\)
- \(R\), \(r\) — długości promieni okręgów, odpowiednio, opisanego i wpisanego w trójkąt \(ABC\)
- \(h_a\), \(h_b\), \(h_c\) — wysokości trójkąta opuszczone, odpowiednio, z wierzchołków \(A\), \(B\) i \(C\)
- \(p\) — połowa obwodu trójkąta \(ABC\), tj. \(p = \dfrac{a + b + c}{2}\)

## [10.1] Twierdzenie Pitagorasa (wraz z twierdzeniem odwrotnym) — s. 15, środek

Jeżeli w trójkącie \(ABC\) kąt \(\gamma\) jest kątem prostym, to:

\[a^2 + b^2 = c^2\]

Jeżeli w trójkącie \(ABC\) długości boków spełniają równość \(a^2 + b^2 = c^2\), to kąt \(\gamma\) jest kątem prostym.

## [10.2] Twierdzenie sinusów — s. 15, środek/dół

\[\frac{a}{\sin \alpha} = 2R \qquad \frac{b}{\sin \beta} = 2R \qquad \frac{c}{\sin \gamma} = 2R\]

## [10.3] Twierdzenie cosinusów — s. 15, dół

\[a^2 = b^2 + c^2 - 2bc \cdot \cos \alpha\]

\[b^2 = a^2 + c^2 - 2ac \cdot \cos \beta\]

\[c^2 = a^2 + b^2 - 2ab \cdot \cos \gamma\]

## [10.4] Wzory na pole trójkąta \(ABC\) — s. 16, góra

\[P_{\Delta ABC} = \frac{1}{2} a \cdot h_a = \frac{1}{2} b \cdot h_b = \frac{1}{2} c \cdot h_c\]

\[P_{\Delta ABC} = \frac{1}{2} ab \cdot \sin \gamma = \frac{1}{2} bc \cdot \sin \alpha = \frac{1}{2} ca \cdot \sin \beta\]

\[P_{\Delta ABC} = \frac{abc}{4R} \qquad P_{\Delta ABC} = p \cdot r\]

\[P_{\Delta ABC} = \sqrt{p(p - a)(p - b)(p - c)}\]

\[P_{\Delta ABC} = \frac{1}{2} a^2 \cdot \frac{\sin \beta \cdot \sin \gamma}{\sin \alpha} = \frac{1}{2} b^2 \cdot \frac{\sin \gamma \cdot \sin \alpha}{\sin \beta} = \frac{1}{2} c^2 \cdot \frac{\sin \alpha \cdot \sin \beta}{\sin \gamma}\]

\[P_{\Delta ABC} = 2R^2 \cdot \sin \alpha \cdot \sin \beta \cdot \sin \gamma\]

## [10.5] Związki miarowe w trójkącie prostokątnym — s. 16, środek

Przyjmijmy, że w trójkącie \(ABC\) kąt przy wierzchołku \(C\) jest kątem prostym. Niech \(D\) będzie spodkiem wysokości opuszczonej z wierzchołka \(C\) na podstawę \(AB\) trójkąta. Wówczas:

\[h_c = \sqrt{|AD| \cdot |DB|} \qquad h_c = \frac{ab}{c}\]

\[r = \frac{a + b - c}{2} \qquad R = \frac{1}{2} c\]

\[a = c \cdot \sin \alpha = c \cdot \cos \beta = b \cdot \operatorname{tg} \alpha = b \cdot \frac{1}{\operatorname{tg} \beta}\]

## [10.6] Związki miarowe w trójkącie równobocznym — s. 16, dół

Oznaczenia: \(a\) — długość boku trójkąta równobocznego; \(h\) — wysokość trójkąta równobocznego.

\[h = \frac{a\sqrt{3}}{2} \qquad P_{\Delta} = \frac{a^2 \sqrt{3}}{4}\]

\[r = \frac{1}{3} h \qquad R = \frac{2}{3} h\]

## [10.7] Cechy przystawania trójkątów — s. 17, góra/środek

**a)** cecha przystawania „bok–bok–bok" dla trójkątów \(ABC\) i \(KLM\): długości boków trójkąta \(ABC\) są równe odpowiednim długościom boków trójkąta \(KLM\), np.: \(|AB| = |KL|\), \(|BC| = |KM|\), \(|CA| = |ML|\)

**b)** cecha przystawania „bok–kąt–bok" dla trójkątów \(ABC\) i \(KLM\): długości dwóch boków trójkąta \(ABC\) są równe odpowiednim długościom dwóch boków trójkąta \(KLM\) i kąty między tymi parami boków są przystające, np.: \(|AB| = |KL|\), \(|BC| = |KM|\) i \(|\sphericalangle ABC| = |\sphericalangle LKM|\)

**c)** cecha przystawania „kąt–bok–kąt" dla trójkątów \(ABC\) i \(KLM\): długość jednego boku trójkąta \(ABC\) jest równa długości jednego boku trójkąta \(KLM\) i kąty przyległe do tego boku trójkąta \(ABC\) są przystające do odpowiednich kątów przyległych do odpowiedniego boku trójkąta \(KLM\), np.: \(|AB| = |KL|\) oraz \(|\sphericalangle BAC| = |\sphericalangle KLM|\) i \(|\sphericalangle ABC| = |\sphericalangle LKM|\)

## [10.8] Cechy podobieństwa trójkątów — s. 17, środek/dół

**a)** cecha podobieństwa „bok–bok–bok" dla trójkątów \(ABC\) i \(KLM\): długości boków trójkąta \(ABC\) są proporcjonalne do odpowiednich długości boków trójkąta \(KLM\), np.:

\[\frac{|AB|}{|KL|} = \frac{|BC|}{|LM|} = \frac{|CA|}{|MK|}\]

**b)** cecha podobieństwa „bok–kąt–bok" dla trójkątów \(ABC\) i \(KLM\): długości dwóch boków trójkąta \(ABC\) są proporcjonalne do odpowiednich długości dwóch boków trójkąta \(KLM\) i kąty między tymi parami boków są przystające, np.:

\[\frac{|AB|}{|KL|} = \frac{|AC|}{|KM|} \text{ i } |\sphericalangle BAC| = |\sphericalangle LKM|\]

**c)** cecha podobieństwa „kąt–kąt–kąt" dla trójkątów \(ABC\) i \(KLM\): kąty trójkąta \(ABC\) są przystające do odpowiednich kątów trójkąta \(KLM\), np.: \(|\sphericalangle BAC| = |\sphericalangle LKM|\) i \(|\sphericalangle ABC| = |\sphericalangle KLM|\) i \(|\sphericalangle ACB| = |\sphericalangle KML|\)

## [10.9] Twierdzenie o dwusiecznej kąta — s. 18, góra

Jeżeli dwusieczna kąta wewnętrznego (zewnętrznego) trójkąta \(ABC\) poprowadzona z wierzchołka \(C\) przecina prostą zawierającą odcinek \(AB\) w punkcie \(D\), to:

\[\frac{|AD|}{|BD|} = \frac{|AC|}{|BC|}\]

## [10.10] Twierdzenie Talesa (wraz z twierdzeniem odwrotnym) — s. 18, góra/środek

Różne proste \(AB\) i \(CD\) przecinają się w punkcie \(P\), przy czym spełniony jest jeden z warunków:

- punkt \(A\) leży wewnątrz odcinka \(PB\) oraz punkt \(C\) leży wewnątrz odcinka \(PD\)

LUB

- punkt \(A\) leży na zewnątrz odcinka \(PB\) oraz punkt \(C\) leży na zewnątrz odcinka \(PD\).

Jeżeli \(\dfrac{|AB|}{|PA|} = \dfrac{|CD|}{|PC|}\), to proste \(AC\) i \(BD\) są równoległe.

Jeżeli proste \(AC\) i \(BD\) są równoległe, to \(\dfrac{|AB|}{|PA|} = \dfrac{|CD|}{|PC|}\).

## [10.11] Koło — s. 18, dół

Pole \(P\) koła o promieniu \(r\) jest równe:

\[P = \pi r^2\]

Obwód \(L\) koła o promieniu \(r\) jest równy:

\[L = 2\pi r\]

## [10.12] Wycinek koła — s. 19, góra

Pole \(P\) wycinka koła o promieniu \(r\) i kącie środkowym \(\alpha\) wyrażonym w stopniach jest równe:

\[P = \frac{\alpha}{360°} \cdot \pi r^2\]

Długość \(L\) łuku \(AB\) wycinka koła o promieniu \(r\) i kącie środkowym \(\alpha\) wyrażonym w stopniach jest równa:

\[L = \frac{\alpha}{360°} \cdot 2\pi r\]

## [10.13] Kąty w okręgu — s. 19, środek

Miara kąta wpisanego w okrąg o środku \(O\) jest równa połowie miary kąta środkowego, opartego na tym samym łuku.

W szczególności kąt wpisany oparty na półokręgu jest kątem prostym.

Miary kątów wpisanych w okrąg o środku \(O\), opartych na tym samym łuku, są równe.

## [10.14] Twierdzenie o kącie między styczną i cięciwą — s. 19, środek/dół

Dany jest okrąg o środku w punkcie \(O\) i cięciwa \(AB\) tego okręgu. Prosta \(AC\) jest styczna do tego okręgu w punkcie \(A\), natomiast punkt \(P\) leży na tym okręgu i nie należy do kąta \(CAB\). Wtedy:

\[|\sphericalangle APB| = |\sphericalangle CAB| \quad \text{i} \quad |\sphericalangle AOB| = 2 \cdot |\sphericalangle CAB|\]

przy czym wybieramy ten z kątów środkowych \(AOB\), który jest oparty na łuku znajdującym się wewnątrz kąta \(CAB\).

## [10.15] Twierdzenie o odcinkach stycznych — s. 20, góra

Jeżeli styczne do okręgu w punktach \(A\) i \(B\) przecinają się w punkcie \(P\), to:

\[|PA| = |PB|\]

## [10.16] Twierdzenie o odcinkach siecznej i stycznej — s. 20, środek

Dane są: prosta przecinająca okrąg w punktach \(A\) i \(B\) oraz prosta styczna do tego okręgu w punkcie \(C\). Jeżeli proste te przecinają się w punkcie \(P\), to:

\[|PA| \cdot |PB| = |PC|^2\]

## [10.17] Trapez — s. 20, dół

Trapez — czworokąt, który ma co najmniej jedną parę boków równoległych.

Oznaczenia: \(a\), \(b\) — długości boków równoległych; \(h\) — wysokość.

Wzór na pole \(P\) trapezu:

\[P = \frac{a + b}{2} \cdot h\]

## [10.18] Równoległobok — s. 21, góra

Równoległobok — czworokąt, który ma dwie pary boków równoległych.

Oznaczenia: \(a\), \(b\) — długości sąsiednich boków; \(h\) — wysokość opuszczona na bok \(a\); \(\alpha\) — kąt między bokami \(a\) i \(b\); \(\gamma\) — kąt między przekątnymi \(AC\) i \(BD\).

Wzory na pole \(P\) równoległoboku:

\[P = ah \qquad P = a \cdot b \cdot \sin \alpha\]

\[P = \frac{1}{2} \cdot |AC| \cdot |BD| \cdot \sin \gamma\]

## [10.19] Romb — s. 21, góra/środek

Romb — czworokąt, który ma wszystkie boki jednakowej długości.

Oznaczenia: \(a\) — długość boku; \(h\) — wysokość; \(\alpha\) — kąt wewnętrzny.

Wzory na pole \(P\) rombu:

\[P = ah \qquad P = a^2 \cdot \sin \alpha\]

\[P = \frac{1}{2} \cdot |AC| \cdot |BD|\]

## [10.20] Deltoid — s. 21, środek

Deltoid — czworokąt wypukły, który ma oś symetrii zawierającą jedną z przekątnych.

Wzór na pole \(P\) deltoidu:

\[P = \frac{1}{2} \cdot |AC| \cdot |BD|\]

## [10.21] Okrąg opisany na czworokącie — s. 21, dół

Na czworokącie można opisać okrąg wtedy i tylko wtedy, gdy sumy miar jego przeciwległych kątów wewnętrznych są równe \(180°\).

\[\alpha + \gamma = 180° \qquad \beta + \delta = 180°\]

## [10.22] Okrąg wpisany w czworokąt — s. 22, góra

W czworokąt wypukły można wpisać okrąg wtedy i tylko wtedy, gdy sumy długości jego przeciwległych boków są równe.

Oznaczenia: \(a\), \(b\), \(c\), \(d\) — długości kolejnych boków czworokąta.

\[a + c = b + d\]

## [10.23] Pola figur podobnych — s. 22, góra/środek

Jeżeli figura \(B\) o polu \(P_B\) jest podobna do figury \(A\) o polu \(P_A\) (różnym od zera) w skali \(k\), to stosunek pól tych figur jest równy kwadratowi skali podobieństwa.

\[\frac{P_B}{P_A} = k^2\]
