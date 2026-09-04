# Projekt rozwiązań: zad. 20 i 21 (2024-grudzień)

Dokument projektowy w rozumieniu skilla `projektowanie-rozwiazan`: co ma zobaczyć uczeń.
Powstał 2026-09-04, po pytaniach doprecyzowujących do Henricha.

Zakres z TODO.md: **zad. 20 rozwiązanie zwykłe**, **zad. 21 rozwiązanie zwykłe i film krok po kroku**.

## Materiał

| co | gdzie | ustalenie |
|---|---|---|
| treść | `exercises.json`, pozycje 24 i 25 | zad. 20: okrąg, \(r = 6\), kąt wpisany \(60^{\circ}\); zad. 21: \(A = (-2, -1)\), \(C = (3, 4)\), przeciwległe wierzchołki kwadratu |
| klucz CKE | `odpowiedzi.txt` (cp1250), s. 20 i 21 | zad. 20 **B**, zad. 21 **A**, oba 1 pkt, bez kryteriów cząstkowych |
| wzory | `tablica-wzorow-transkrypt/` | `[10.12]` długość łuku (s. 19), `[10.13]` kąt wpisany i środkowy (s. 19), `[10.1]` Pitagoras (s. 15), `[11.1]` długość odcinka (s. 22) |

Policzone od zera i zgodne z kluczem:

- zad. 20: kąt środkowy \(2 \cdot 60^{\circ} = 120^{\circ}\), łuk \(\frac{120}{360} \cdot 2\pi \cdot 6 = 4\pi\).
- zad. 21: \(|AC| = \sqrt{5^{2} + 5^{2}} = 5\sqrt{2}\), bok \(a = 5\).

**Czego w tablicy NIE MA:** wzoru „przekątna kwadratu \(= a\sqrt{2}\)". Sekcja 10 nie ma w ogóle
pozycji o kwadracie. Dlatego rozwiązanie zad. 21 idzie przez Pitagorasa (`[10.1]`), a nie przez
gotową przekątną, i w kolumnie wzorów nie stanie nic spoza tablicy.

## Zad. 20 (tylko rozwiązanie zwykłe)

Obok zadania stoi już widżet `widgetKatWpisany` (przeciąganie \(C\) po okręgu, kąt wpisany
zostaje \(60^{\circ}\), środkowy \(120^{\circ}\)). Rozwiązanie ma go **domykać rachunkiem**,
a nie powtarzać: widżet pokazuje, że zależność jest stała, tekst pokazuje, jak z niej policzyć łuk.
Notacja kąta ta sama co w widżecie: `\angle ASB`, nie `\sphericalangle`.

Układ: **jedna kolumna**, dwie części rozdzielone `rozw-odstep`.

1. Zdanie wprowadzające: który kąt jest wpisany, który środkowy, na czym oba są oparte.
   Zależność „wpisany to połowa środkowego" idzie **zdaniem**, bo w tablicy stoi zdaniem, a nie wzorem.
2. \(|\angle ASB| = 2 \cdot 60^{\circ}\)
3. \(|\angle ASB| = 120^{\circ}\)
4. Komentarz z częścią drugą plus wzór na długość łuku w ramce (jest w tablicy):
   \[L = \dfrac{\alpha}{360^{\circ}} \cdot 2\pi r\]
5. \(L = \dfrac{120^{\circ}}{360^{\circ}} \cdot 2\pi \cdot 6\)
6. Komentarz z ogniwem: \(\dfrac{120}{360} = \dfrac{1}{3}\), czyli łuk to trzecia część okręgu.
7. \(L = \dfrac{1}{3} \cdot 2\pi \cdot 6\)
8. \(L = \dfrac{1}{3} \cdot 12\pi\)
9. \(\boldsymbol{L = 4\pi}\)
10. Odpowiedź **B**.

Pułapka ze sprawozdań CKE, którą rozbrajamy: mylenie kąta wpisanego ze środkowym, czyli liczenie
łuku od razu z \(60^{\circ}\) (wychodzi wtedy dystraktor A, \(2\pi\)). Rozbrajamy ją **budową kroków**,
a nie ostrzeżeniem: kąt środkowy dostaje własną, osobną linijkę, zanim pojawi się wzór na łuk.

## Zad. 21: decyzje Henricha (2026-09-04)

Cztery pytania i odpowiedzi, bo one wyznaczają kształt filmu:

- **Metoda:** Pitagoras dwa razy, oba razy pokazany graficznie. Najpierw przekątna z trójkąta,
  którego przyprostokątne to różnice współrzędnych. Potem bok: najpierw ogólny wzór \(a^{2}+b^{2}=c^{2}\),
  a pod niego podstawiamy \(a\), \(a\) i \(5\sqrt{2}\).
- **Rysunek:** kwadrat widoczny od pierwszego kroku, na siatce kratek.
- **Skąd wzór na długość odcinka:** pokazujemy trójkąt pod przekątną, czyli \(5\) w bok i \(5\) w górę.
- **Kadr:** rysunek zostaje z boku do końca filmu, rachunek idzie obok niego.

Henrich dostał ostrzeżenie, że przy kwadracie leżącym równolegle do osi bok \(5\) daje się odczytać
z kratek, i mimo to wybrał rysunek od pierwszego kroku. To jest jego decyzja, nie przeoczenie.

### Co z tego wynika dla rysunku

Z danych wychodzi \(B = (3, -1)\) i \(D = (-2, 4)\), więc kwadrat leży równolegle do osi, a przekątna
biegnie pod \(45^{\circ}\). Trójkąt „różnic współrzędnych" pokrywa się wtedy z połową kwadratu, więc
gdyby obie części filmu użyły tego samego trójkąta, druga wyglądałaby jak liczenie czegoś, co już
stoi na rysunku.

**Rozwiązanie: dwie połowy kwadratu, po jednej na część.**

- **Część 1 (przekątna): górny trójkąt \(ACD\).** Z \(A\) w górę do \(D\), z \(D\) w prawo do \(C\).
  Te dwa odcinki są różnicami współrzędnych i tylko w tej roli występują.
- **Część 2 (bok): dolny trójkąt \(ABC\).** Przyprostokątne \(AB\) i \(BC\) to boki kwadratu, obie \(a\),
  przeciwprostokątną jest policzona przekątna \(5\sqrt{2}\).

Przekątna dzieli kwadrat na dwa trójkąty i każdy z nich robi w filmie inną robotę. Uczeń widzi
podział raz, na początku, i potem tylko wraca wzrokiem raz w górę, raz w dół.

### Kadr

Trzy pasy jak w zad. 11:

- **lewa połowa:** układ współrzędnych z siatką `#e0e0e0`, kwadrat \(ABCD\) z podpisanymi wierzchołkami,
  przekątna \(AC\);
- **prawa góra, mniejszym pismem:** pas odczytu (dane \(A\) i \(C\) z treści, potem różnice współrzędnych);
- **prawa środkowa:** główny rachunek, ten sam pas przez cały film;
- **prawa dół:** odpowiedź.

Wzór \(a^{2}+b^{2}=c^{2}\) wjeżdża na końcu kroku poprzedzającego podstawienie (README, punkt 53)
i stoi nad rachunkiem. Używamy go dwa razy, więc w części drugiej wraca w tej samej postaci literowej,
w tym samym miejscu.

### Kroki filmu

Format: *stan przed → co się rusza → stan po*. Zielone jest zawsze tylko to, co się w kroku zmienia.

1. **Kwadrat i dane.** Wjeżdża układ, kwadrat \(ABCD\), podpisy wierzchołków, przekątna \(AC\),
   a w pasie odczytu \(A = (-2,\ -1)\) i \(C = (3,\ 4)\). Cały krok czarny (nic się nie przelicza).
2. **Przekątna dzieli kwadrat na dwa trójkąty prostokątne.** Zapala się górna połowa (\(ACD\)):
   przyprostokątne \(AD\) i \(DC\), a przekątna zostaje przeciwprostokątną. Zielone: dwie przyprostokątne.
3. **Różnice współrzędnych.** Przy \(AD\) i \(DC\) pojawiają się piątki, a w pasie odczytu, mniejszym
   pismem, ogniwo: \(4 - (-1) = 4 + 1 = 5\) oraz \(3 - (-2) = 3 + 2 = 5\). Zielone: piątki.
   Na końcu kroku wjeżdża wzór \(a^{2} + b^{2} = c^{2}\).
4. **Podstawienie.** Piątki z rysunku lecą pod \(a\) i \(b\), pod \(c\) wchodzi \(|AC|\):
   \(5^{2} + 5^{2} = |AC|^{2}\).
5. \(25 + 25 = |AC|^{2}\)
6. \(50 = |AC|^{2}\)
7. \(|AC| = \sqrt{50}\) (pierwiastkujemy obie strony, ujemny wynik odpada, bo to długość).
8. \(|AC| = 5\sqrt{2}\), z ogniwem \(\sqrt{50} = \sqrt{25 \cdot 2} = \sqrt{25} \cdot \sqrt{2}\).
9. **Sprzątanie kadru.** Pas odczytu znika, wynik \(5\sqrt{2}\) siada jako podpis przekątnej na rysunku,
   gaśnie górny trójkąt, zapala się dolny (\(ABC\)), a jego przyprostokątne dostają podpis \(a\).
   Krok bez rachunku, jedna myśl (README, punkt 52).
10. **Podstawienie drugi raz, do tego samego wzoru:** \(a^{2} + a^{2} = (5\sqrt{2})^{2}\).
11. \(2a^{2} = (5\sqrt{2})^{2}\)
12. \(2a^{2} = 50\), z ogniwem \((5\sqrt{2})^{2} = 5^{2} \cdot (\sqrt{2})^{2} = 25 \cdot 2\).
13. \(a^{2} = 25\) (dzielimy obie strony przez \(2\)).
14. \(a = 5\), ujemny odpada.
15. **Odpowiedź A**, a \(5\) siada przy boku kwadratu na rysunku.

Pułapka ze sprawozdań CKE, którą rozbrajamy budową kroków: **zatrzymanie się na przekątnej**
(dystraktor C, \(5\sqrt{2}\)). Wynik pierwszej części jawnie zjeżdża na rysunek jako podpis przekątnej,
więc widać, że to jeszcze nie jest bok. Druga pułapka, odejmowanie liczby ujemnej, ma własne ogniwo
w kroku 3.

### Rozwiązanie opisowe

Jedna kolumna, wzór \(a^{2}+b^{2}=c^{2}\) nad rachunkiem, dwie części rozdzielone `rozw-odstep`.
Linijki rachunku jeden do jednego z krokami 4 do 8 i 10 do 14 filmu; kroki filmowe bez rachunku
(1, 2, 3, 9) siedzą w tekście jako komentarze, a nie jako osobne linijki. To jest **świadomy rozjazd**
w rozumieniu zluzowanej zasady z 2026-08-30: film musi narysować to, co tekst może powiedzieć zdaniem.

## Czego nie ustalono

- Czy przy szerokości telefonu (485 px) rysunek w lewej połowie kadru filmu nie robi się za drobny,
  żeby odczytać podpisy \(A\), \(B\), \(C\), \(D\) i \(5\sqrt{2}\). Kadr jest ten sam co w zad. 11 i 12,
  gdzie wyszło dobrze, ale tam po lewej stała prosta, a nie kwadrat z czterema podpisami.
  To idzie do `TODO.md`, sekcja `TESTOWANIE HENRICH`.
