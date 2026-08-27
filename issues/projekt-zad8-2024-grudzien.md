# Projekt rozwiązania: zadanie 8, arkusz 2024-grudzień

Napisane od zera 2026-08-27, po skasowaniu poprzedniej wersji. Poprzedniego projektu
świadomie nie brałem pod uwagę: metoda, liczba linijek i układ zostały wybrane na nowo.

Zakres zamówienia (Henrich, 2026-08-27): projekt i **rozwiązanie opisowe**. Filmu krok
po kroku na razie nie robimy. Sprawdzenie wyniku przez podstawienie ma być, ale tylko
w rozwiązaniu opisowym.

## Treść i wynik

Rozwiąż równanie \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2x - 2}\). Zapisz konieczne
założenie i obliczenia. Zadanie otwarte, 3 punkty.

Wynik: \(x = -6\). Policzone samodzielnie i zgodne z kluczem CKE (`odpowiedzi.pdf`, s. 7).

## Kryteria CKE i gdzie są pokryte

| Kryterium | Punkty | Gdzie |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | blok nad rachunkiem |
| równanie sprowadzone do postaci bez ułamków, np. \((x+3)(2x-2) = x(x-1)\) | 1 | linijka 3 |
| wynik \(x = -6\) należący do dziedziny | 1 | pozycje 16 do 19 |

Klucz dopuszcza obie drogi: przez równanie liniowe i przez kwadratowe. Idziemy przez
kwadratowe, klucz wymienia je wprost jako poprawne.

## Wybór metody i dlaczego właśnie ta

Do wyboru były dwie: wyłączenie dwójki (\(2x-2 = 2(x-1)\)) z mnożeniem stronami przez
wspólny mianownik, albo mnożenie na krzyż z równaniem kwadratowym. Wybrane: **kwadratowa**,
z trzech powodów.

1. **Nie wymaga dostrzeżenia niczego.** Wyłączenie dwójki jest sprytne: uczeń albo zobaczy
   wspólny czynnik, albo utknie na starcie i cała reszta rozwiązania jest dla niego
   niedostępna. Mnożenie obu stron przez mianownik to czynność mechaniczna, wykonalna
   bez pomysłu.
2. **Założenie realnie coś odsiewa.** Przy drodze kwadratowej wychodzą dwa pierwiastki,
   \(-6\) oraz \(1\), i ten drugi wypada właśnie przez założenie. Uczeń widzi na własne
   oczy, po co się je pisze. Przy drodze liniowej założenie jest formalnością, nic nie
   zmienia w wyniku, więc uczy tego, że wystarczy je przepisać dla punktu.
3. **Finisz idzie schematem z tablicy.** Wyróżnik i wzory na pierwiastki są w tablicy
   wzorów ([7.1] i [7.4]) i są najlepiej wyćwiczonym schematem na poziomie podstawowym.
   Sąsiednie zadanie 9 w tym samym arkuszu kończy się tak samo, więc uczeń rozpoznaje rytm.

Koszt tej decyzji: rozwiązanie jest dłuższe, a w środku trzeba wymnożyć dwa nawiasy.
Dlatego rachunek jest pocięty drobno, patrz niżej.

## Zasada porządkująca: zero skoków

Henrich odrzucił poprzednie propozycje jako przejście na skróty. Dwa miejsca, w których
skrót normalnie się pojawia, są tu rozbite jawnie:

- **Mnożenie na krzyż nie jest jednym ruchem.** Mnożymy obie strony najpierw przez
  \((x-1)\), a dopiero potem przez \((2x-2)\). Każde mnożenie kasuje jeden ułamek. Uczeń
  nie musi wierzyć w regułę „licznik razy mianownik z drugiej strony", tylko widzi dwa
  zwykłe mnożenia obu stron, takie same jak w równaniach z klasy siódmej.
- **Przenoszenie na jedną stronę idzie po jednym składniku.** Osobno \(x^2\), osobno \(x\),
  za każdym razem z dopiskiem wykonywanego działania. To jest miejsce, w którym uczeń gubi
  minus, więc oba przeniesienia są widoczne oddzielnie.

## Założenie (blok nad rachunkiem)

> Mianownik nie może być zerem. Pierwszy: \(x - 1 \ne 0\), czyli \(x \ne 1\).
> Drugi: \(2x - 2 \ne 0\), czyli \(2x \ne 2\), czyli \(x \ne 1\).
> Założenie: \(x \ne 1\).

Wg `SOLUTION_TEXT_RULES.md` punkt 22 założenie stoi na górze, nad rachunkiem, razem
ze zdaniem, skąd się wzięło. CKE daje za nie osobny punkt, więc nie chowamy go w środku.

## Linijki rachunku

Dwadzieścia trzy pozycje: siedemnaście linijek rachunku, trzy zdania i wytłuszczony
wynik. Każda robi dokładnie jedną rzecz.

| # | Linijka | Co się w niej dzieje |
|---|---|---|
| 1 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2} \;\big/ \cdot (x-1)\) | zapis z treści, zapowiedź pierwszego mnożenia |
| 2 | \(x + 3 = \dfrac{x(x-1)}{2x-2} \;\big/ \cdot (2x-2)\) | lewy ułamek zniknął, zapowiedź drugiego mnożenia |
| 3 | \((x+3)(2x-2) = x(x-1)\) | zniknął drugi ułamek, równanie bez ułamków (punkt CKE) |
| 4 | \(2x^2 - 2x + 6x - 6 = x(x-1)\) | wymnożone nawiasy po lewej, każdy z każdym |
| 5 | \(2x^2 + 4x - 6 = x(x-1)\) | po lewej \(-2x + 6x = 4x\) |
| 6 | \(2x^2 + 4x - 6 = x^2 - x \;\big/ - x^2\) | wymnożony nawias po prawej |
| 7 | \(2x^2 + 4x - 6 - x^2 = -x \;\big/ + x\) | przeniesione \(x^2\), zmienia znak |
| 8 | \(2x^2 + 4x - 6 - x^2 + x = 0\) | przeniesione \(-x\), zmienia znak |
| 9 | \(2x^2 - x^2 + 4x + x - 6 = 0\) | podobne wyrazy stają obok siebie |
| 10 | \(x^2 + 4x + x - 6 = 0\) | \(2x^2 - x^2 = x^2\) |
| 11 | \(x^2 + 5x - 6 = 0\) | \(4x + x = 5x\), gotowa postać ogólna |
| 12 | \(a = 1,\quad b = 5,\quad c = -6\) | odczytane współczynniki, obok wzór na wyróżnik |
| 13 | \(\Delta = 5^2 - 4 \cdot 1 \cdot (-6)\) | samo podstawienie, bez liczenia |
| 14 | \(\Delta = 25 + 24 = 49\) | policzona wartość |
| 15 | \(\sqrt{\Delta} = 7\) | bo \(7 \cdot 7 = 49\), obok wzory na pierwiastki |
| 16 | \(x_1 = \dfrac{-5 - 7}{2 \cdot 1} = \dfrac{-12}{2} = -6\) | pierwszy pierwiastek |
| 17 | \(x_2 = \dfrac{-5 + 7}{2 \cdot 1} = \dfrac{2}{2} = 1\) | drugi pierwiastek |
| 18 | zdanie odrzucające jedynkę | tu pracuje założenie, patrz niżej |
| 19 | \(\boldsymbol{x = -6}\) | wynik rachunku, wytłuszczony |
| 20 | zapowiedź sprawdzenia, ze wskazaniem \(L\) i \(P\) | zmiana fazy rozwiązania |
| 21 | \(L = \dfrac{-6+3}{-6-1} = \dfrac{-3}{-7} = \dfrac{3}{7}\) | sprawdzenie, lewa strona |
| 22 | \(P = \dfrac{-6}{2 \cdot (-6) - 2} = \dfrac{-6}{-14} = \dfrac{3}{7}\) | sprawdzenie, prawa strona |
| 23 | zdanie zamykające | wraca do polecenia |

Linijka 13 i 14 są rozdzielone celowo: podstawienie do wzoru i liczenie to dwie różne
czynności, a przy \(c = -6\) właśnie na styku tych dwóch uczeń robi \(-24\) zamiast \(+24\).

## Pytanie retoryczne, jedno

W pozycji 18: „Dlaczego jedynka odpada, skoro wyszła z rachunku? Bo dla \(x = 1\) oba
mianowniki są zerem, a przez zero nie wolno dzielić."

Zgodnie z `references/zasady-tekstowe.md` takie pytanie ma być najwyżej jedno na
rozwiązanie i tylko tam, gdzie odpowiedź nie wynika z samego zapisu. Tu nie wynika:
rachunek pokazuje \(x_2 = 1\) i nic w nim nie mówi, że to nie jest rozwiązanie.

## Zamknięcie

Pozycja 23 brzmi: „Obie strony dały \(\dfrac{3}{7}\), więc rozwiązaniem równania jest
\(x = -6\)." Wraca do polecenia (pytali o rozwiązanie równania, nie o wyróżnik ani
o pierwiastki trójmianu) i domyka sprawdzenie z pozycji 21 i 22.

Sprawdzenie przez podstawienie nie jest wymagane przez klucz. Jest, bo Henrich chciał
i bo w tym zadaniu ma sens: uczeń dopiero co odrzucił jeden z dwóch pierwiastków, więc
warto, żeby zobaczył, że ten drugi naprawdę pasuje do wyjściowego równania.

## Rozbrojone typowe błędy, dwa

1. **Mianownik bez zastrzeżenia.** Rozbrojony nie ostrzeżeniem, tylko konstrukcją:
   założenie stoi na górze, a w pozycjach 17 i 18 realnie wyrzuca pierwiastek. Uczeń,
   który je pominie, poda dwa rozwiązania i sam zobaczy różnicę.
2. **Zgubiony znak przy przenoszeniu.** Rozbrojony rozbiciem na linijki 6, 7 i 8, każda
   z jawnym dopiskiem wykonywanego działania przy stanie sprzed.

## Układ i kolor

- **Jedna kolumna** (`rozwiazanie-kroki`), oba wzory z tablicy nad rachunkiem, tak jak
  w zadaniu 9 z tego samego arkusza. Pierwszy projekt zakładał dwie kolumny, bo wzory
  wchodzą w środku rachunku, i **to okazało się nie do utrzymania na telefonie**. Pomiar
  przy szerokości okna 390 px: kolumna wzorów bierze 104 px, przerwa między kolumnami
  40 px, więc na rachunek zostaje 154 px z 298 px bloku i **łamie się siedemnaście
  linijek z dwudziestu trzech**. KaTeX łamie wzór w przypadkowym miejscu, więc
  \(\dfrac{x}{2x-2}\) rozjeżdża się na dwa wiersze i wygląda jak inne wyrażenie.
  W jednej kolumnie rachunek dostaje całe 298 px i **nie łamie się ani jedna linijka**.
- **Wzór na pierwiastki zapisany z \(\pm\)**, czyli \(x_{1,2} = \dfrac{-b \pm \sqrt{\Delta}}{2a}\).
  Tablica podaje \(x_1\) i \(x_2\) osobno, ale dwa wzory obok siebie mają 334 px i wystają
  poza kartę telefonu. Zapis z \(\pm\) mieści się i jest dokładnie tym, którego używa
  zadanie 9 w tym samym arkuszu, więc uczeń widzi ten sam wzór w obu miejscach.
- **Bez zieleni.** Zielony w tym projekcie idzie zawsze w parze ze wzorem obok i wskazuje
  fragment, do którego wzór się odnosi. Oba tutejsze wzory odnoszą się do całego trójmianu,
  a nie do jednego fragmentu, więc nie ma czego wskazywać (punkt 13 zasad). Kolorowanie
  trzech współczynników naraz dałoby trzy podświetlenia w jednej linijce, czyli dokładnie
  to, czego zasady zabraniają.

## Co zmierzono

Serwer `tools/serwer.js`, Playwright, arkusz otwarty na zadaniu 8 z rozwiniętym
rozwiązaniem, cztery ujęcia: komputer i telefon, motyw jasny i ciemny.

- Strona nie przewija się w bok: `scrollWidth === clientWidth`, 1280 i 390.
- Blok rozwiązania mieści się w karcie: 298 px treści na 298 px miejsca.
- Oba wzory nad rachunkiem mieszczą się w karcie telefonu: 298 na 298 (przed zmianą
  zapisu na \(\pm\) było 334 na 298, czyli wystawały).
- Żadna z dwudziestu trzech pozycji nie łamie się na telefonie (wysokości 26 do 49 px,
  czyli jeden wiersz, ułamki wliczone).

## Film krok po kroku, na kiedyś

Nie robimy go teraz. Gdy przyjdzie, ma mieć **dwadzieścia trzy kroki**, jeden do jednego
z linijkami powyżej, plus krok z założeniem na starcie. Trzy uwagi na wejście:

- Krok 1 i 2 niosą dopisek działania przy stanie sprzed, więc dopisek pojawia się na końcu
  poprzedniego kroku, a nie na początku następnego.
- Sprawdzenie z pozycji 20 do 22 jest w rozwiązaniu opisowym z decyzji Henricha. Przed
  renderem trzeba zapytać, czy wchodzi też do filmu, bo to trzy kroki na sprawdzanie
  czegoś, co klucz uznaje za zbędne.
- Najszerszym stanem jest linijka 8, więc to ona wyznaczy skalę całego filmu.

## Do decyzji: podpowiedź została z poprzedniej wersji

Henrich nie zamówił nowej podpowiedzi, więc pole `hint` zostało nietknięte. Brzmi ono:
„Zanim cokolwiek policzysz, sprawdź, dla jakiego \(x\) mianownik byłby zerem. Potem popatrz
na oba mianowniki uważnie: nie są tak różne, jak wyglądają."

Druga część **prowadzi do drugiej z rozważanych dróg**, tej z wyłączeniem dwójki, a nie do
tej, którą pokazuje rozwiązanie. Uczeń, który za nią pójdzie, dostanie poprawny wynik, więc
nie jest to błąd, ale podpowiedź i rozwiązanie mówią o dwóch różnych pomysłach. Propozycja
do akceptacji, gdyby miały mówić o jednym:

„Zanim cokolwiek policzysz, sprawdź, dla jakiego \(x\) mianownik byłby zerem. Potem pozbądź
się ułamków: pomnóż obie strony przez jeden mianownik, a potem przez drugi."

## Czego nie ustalono

Nie wiadomo, co dokładnie było złe w poprzedniej wersji rozwiązania: Henrich poprosił
o pracę od zera bez podawania przyczyny. Ten projekt nie naprawia tamtych wad świadomie,
bo ich nie znam. Jeśli któraś wróci, trzeba będzie nazwać ją wprost.
