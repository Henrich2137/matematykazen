# Zadanie 9, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad9.py`. Projekt dydaktyczny i uzasadnienie metody:
[../issues/projekt-zad9-zad10-2024-grudzien.md](../issues/projekt-zad9-zad10-2024-grudzien.md).

Napisane **od nowa 2026-08-28, na wzór zadań 7 i 8**. Poprzednia wersja miała osiem
kroków, siedem linijek w rozwiązaniu opisowym (czyli rozjazd), liczyła ogniwa w głowie
i nie pokazywała paraboli, przez co wniosek o przedziale niósł wyłącznie zwinięty opis
pod krokiem. Wersja trzecia (2026-08-29, po uwagach Henricha) ma dwadzieścia jeden kroków; wersja druga miała dwadzieścia dwa, patrz sekcja o zmianach niżej.

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
| zbiór rozwiązań \(\langle -1,\ 7\rangle\) | 1 | 20 |

## Kroki

| # | Stan po kroku | Zielone |
|---|---|---|
| 1 | \(x(x - 6) \le 7\) | nic |
| 2 | \(x \cdot x - x \cdot 6 \le 7\) | dwa nowe \(x\) i kropki mnożenia |
| 3 | \(x^{2} - 6x \le 7\) | wykładnik \(2\) |
| 4 | \(x^{2} - 6x - 7 \le 0\) | minus przy siódemce i zero |
| 5 | \(1x^{2} - 6x - 7 \le 0\) oraz pas notatek \(a = 1\), \(b = -6\), \(c = -7\) | jedynka, potem oba minusy |
| 6 | \(\Delta = (-6)^{2} - 4 \cdot 1 \cdot (-7)\) | wartości przylatujące z pasa |
| 7 | \(\Delta = 36 + 28\) | plus przed \(28\) |
| 8 | \(\Delta = 64\) | nic |
| 9 | \(\sqrt{\Delta} = 8\) | \(8\) |
| 10 | oba wzory na pierwiastki, literowo; \(\sqrt{\Delta}\) dołącza do pasa | nic |
| 11 | \(x_{1} = \dfrac{-(-6) - 8}{2 \cdot 1}\) | wartości przywołane z pasa |
| 12 | \(x_{1} = \dfrac{6 - 8}{2}\) | \(6\) z dwóch minusów |
| 13 | \(x_{1} = \dfrac{-2}{2}\) | \(-2\) |
| 14 | \(x_{1} = -1\) | nic |
| 15 | \(x_{2} = \dfrac{-(-6) + 8}{2 \cdot 1}\), pierwszy wynik czeka po lewej | wartości przywołane z pasa |
| 16 | \(x_{2} = \dfrac{6 + 8}{2}\) | \(6\) z dwóch minusów |
| 17 | \(x_{2} = \dfrac{14}{2}\) | \(14\) |
| 18 | \(x_{2} = 7\) | nic |
| 19 | oba wyniki jadą w górę, wraca nierówność \(1x^{2} - 6x - 7 \le 0\), pas znika, a w jego miejscu powstaje szkic paraboli ramionami w górę przez \(-1\) i \(7\) | jedynka przy \(x^{2}\), w chwili rysowania paraboli |
| 20 | fragment pod osią i odcinek na osi | fragment, odcinek i \(\le 0\) w nierówności |
| 21 | nierówność znika, odcinek zamienia się w \(x \in \langle -1,\ 7\rangle\) | nic |

**Trzy ostatnie kroki mają przywołaną nierówność nad wynikami** (Henrich, 2026-08-30).
Bez niej rysunek wisiał w powietrzu: parabola brała się znikąd, a „pod osią" nie miało do
czego się odnieść. Teraz zieleń łączy zapis z rysunkiem dwa razy. Raz w kroku 19: zapala się
jedynka przy \(x^{2}\), czyli współczynnik \(a\), dokładnie wtedy, gdy rysuje się parabola,
bo to ona decyduje o kierunku ramion. Drugi raz w kroku 20: zapala się \(\le 0\) razem
z fragmentem pod osią, bo „mniejsze lub równe zeru" i „poniżej osi" to jedno i to samo.
W kroku 21 nierówność znika na starcie, żeby odpowiedź została w kadrze sama.

Trzy rzeczy, o które prosił Henrich po pierwszej wersji, i jak zostały zrobione:

- **jedynka przed \(x^{2}\)**: krok 5 najpierw dopisuje ją w samej nierówności, i dopiero
  z niej rodzi się \(a = 1\);
- **podstawianie do wzoru**: krok 6 najpierw pokazuje wzór literowy, a wartości przylatują
  z pasa notatek na miejsca liter, zamiast pojawiać się z niczego;
- **dwa wzory na pierwiastki**: krok 10 wprowadza oba naraz, tak jak stoją w tablicy, a potem
  pierwszy jest liczony do końca (kroki 11 do 14) i dopiero potem drugi (15 do 18).

**Pas notatek** (\(a\), \(b\), \(c\), a od kroku 10 też \(\sqrt{\Delta}\)) stoi pod
rachunkiem od kroku 5 do 18, mniejszym pismem i rozsunięty. To z niego wracają wartości
za każdym razem, gdy są potrzebne.

Rysunek w krokach 19 do 21 jest **szkicem**: oś \(x\), dwa podpisane punkty, gładka
parabola. Bez siatki, bez osi \(y\), bez skali. Chodzi o kształt i o to, gdzie parabola
leży pod osią.

### Co się zmieniło w wersji trzeciej (2026-08-29)

Dawne kroki 19 i 20 to dziś **jeden** krok. Krok 19 sklejał wtedy oba wyniki w jedną
linijkę \(x_{1} = -1,\ x_{2} = 7\) przez przecinek, a dopiero krok 20 odsyłał ją w górę
i rysował parabolę. Henrich: „animacja zmiany nie ma sensu i wprowadza niepotrzebne
zamieszanie, przecinek jest niepotrzebny, wystarczy aby zniknęły współczynniki i delta,
a w ich miejsce pojawiła się parabola. Może to być w jednym kroku". Sklejanie niczego nie
liczyło, a oba kroki robiły `Transform` na **kopii** stanu, po czym podmieniały obiekt na
scenie (`remove` + `add`), przez co linijka wyników **mrugała** na styku. Teraz w górę jadą
te same obiekty, które już stoją w kadrze, więc nie ma czego podmieniać.

Drugą poprawką jest **środek pasa notatek**. Pas był wyśrodkowany dla całej czwórki
(\(a\), \(b\), \(c\), \(\sqrt{\Delta}\)), a czwarta notatka dołącza dopiero
w kroku 10, więc przez pięć kroków trzy widoczne notatki wisiały zsunięte w lewo, z pustym
miejscem po prawej (Henrich: „\(b = -6\) powinno być na środku"). Teraz środek liczy się
dla **trójki**, a w kroku 10, razem z dołączeniem pierwiastka, cały pas zjeżdża w lewo
i czwórka staje na środku. Pas poszedł też o 0,15 jednostki wyżej.

## Co zmierzono po renderze (2026-08-29, wersja trzecia)

- `tools/styk-klatek.sh`: dwadzieścia styków, od 0,99928 do 0,99991, **bez zastrzeżeń**.
- `tools/klatki.sh stany --koniec`: obejrzane wszystkie dwadzieścia jeden stanów
  spoczynkowych. Rachunek idzie poprawnie od pierwszej linijki do ostatniej, trójka
  współczynników stoi na środku w krokach 5 do 9, czwórka w krokach 10 do 18, a kroki
  19 do 21 pokazują wykres bez zieleni na klatkach brzegowych.
- `tools/test-krokow.js --zadania=6,8,9`: bez zastrzeżeń.

## Co zmierzono po renderze (2026-08-28, wersja druga)

- `tools/styk-klatek.sh`: dwadzieścia jeden styków, od 0,99924 do 0,99995, bez zastrzeżeń.
- `tools/zielen-krokow.py`: każdy krok zaczyna i kończy się bez zieleni.
- `tools/test-krokow.js --zadania=8`: dwa ziarna, bez zastrzeżeń.
- Kroki 20 i 21 dostały dodatkowy postój 0,35 s na końcu, a krok 22 postój 0,2 s na starcie.
  Bez tego styki przy rysunku schodziły poniżej progu 0,999: rysunek zajmuje pół kadru
  gładkimi krzywymi, a koder H.264 potrzebuje kilku klatek bez ruchu. Postój na starcie
  kroku daje najwięcej, bo pierwsza klatka pliku jest wtedy czystym stanem, a nie klatką
  \(t = 0\) animacji (styk 21 do 22: 0,99895 przed, 0,99924 po).
