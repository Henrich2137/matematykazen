# Spec: zadanie 8, arkusz 2024-grudzień, rozwiązanie opisowe

Stan na 2026-08-27, **wpisane do `exercises.json`**. Zastępuje wcześniejszy tego samego dnia
projekt przez równanie kwadratowe i deltę (Henrich: za dużo kroków, delta niepotrzebna);
tamten plik został usunięty.

## Treść i wynik

Rozwiąż równanie \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2x - 2}\). Zapisz konieczne
założenie i obliczenia. Zadanie otwarte, 3 punkty. Wynik: \(x = -6\), zgodny z kluczem CKE.

## Metoda

Wspólny mianownik i dwa mnożenia obu stron, każde przez inny czynnik:

1. widzimy, że prawy mianownik to \(2(x - 1)\), czyli ten sam nawias co po lewej,
2. mnożymy obie strony przez \((x - 1)\) i skracamy ten nawias po obu stronach,
3. mnożymy obie strony przez \(2\), znika ostatni ułamek,
4. zostaje zwykłe równanie pierwszego stopnia.

Żadnego wzoru z tablicy, żadnej delty, żadnego równania kwadratowego. Klucz CKE wymienia
tę drogę wprost jako poprawną (\(2(x+3) = x\) stoi w zasadach oceniania).

## Kryteria CKE i gdzie są pokryte

| Kryterium | Punkty | Gdzie |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | linijka 2 |
| równanie bez ułamków, np. \(2(x+3) = x\) | 1 | linijka 6 |
| wynik \(x = -6\) należący do dziedziny | 1 | linijki 10 i 11 |

## Budowa: linijka, pod nią bledszy komentarz

Zasada Henricha z tego dnia. Rachunek idzie linijka pod linijką, a między nimi stoi jedno
zdanie **bledszym kolorem**, mówiące, co się w tym przejściu dzieje. Zapis działania
wykonywanego na obu stronach (\(\big/ \cdot (x-1)\)) też jest bledszy i odsunięty od rachunku,
bo nie jest jego częścią. Znaczniki i reguły: `SOLUTION_TEXT_RULES.md`, sekcja „Komentarze
między linijkami"; wygląd: `ARCHITECTURE_CSS.md`.

Założenie **nie stoi już w osobnym akapicie nad blokiem**, tylko jest drugą linijką rachunku,
a zdanie o mianownikach jest komentarzem nad nim.

## Linijki i komentarze

| # | Linijka | Komentarz pod nią |
|---|---|---|
| 1 | \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2x - 2}\) | Mianownik nie może być zerem, a oba zerują się dla \(x = 1\). Zapisujemy założenie. |
| 2 | \(\boldsymbol{x \ne 1}\) | Prawy mianownik to dwójka razy ten sam nawias, który stoi po lewej: \(2x - 2 = 2(x - 1)\). |
| 3 | \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2(x - 1)}\) z dopiskiem \(\big/ \cdot (x - 1)\) | Mnożymy obie strony przez \(x - 1\), więc ten nawias dopisuje się w obu licznikach. |
| 4 | \(\dfrac{(x + 3)(x - 1)}{x - 1} = \dfrac{x(x - 1)}{2(x - 1)}\) | Ten sam nawias stoi teraz w liczniku i w mianowniku, po obu stronach, więc go skreślamy. |
| 5 | \(x + 3 = \dfrac{x}{2}\) z dopiskiem \(\big/ \cdot 2\) | Został jeden ułamek. Mnożymy obie strony przez dwójkę i po prawej też się ona skróci. |
| 6 | \(2(x + 3) = x\) | Opuszczamy nawias: dwójka mnoży osobno \(x\) i osobno \(3\). |
| 7 | \(2x + 6 = x\) z dopiskiem \(\big/ - 6\) | Liczby zbieramy po prawej stronie. Szóstka przechodzi ze zmianą znaku. |
| 8 | \(2x = x - 6\) z dopiskiem \(\big/ - x\) | Teraz to samo z niewiadomą: \(x\) przechodzi na lewo, też ze zmianą znaku. |
| 9 | \(2x - x = -6\) | Dwa iksy bez jednego iksa to jeden iks. |
| 10 | \(\boldsymbol{x = -6}\) | Wynik spełnia założenie, bo \(-6\) nie jest jedynką. |
| 11 | \(L = \dfrac{(-6) + 3}{(-6) - 1} = \dfrac{-3}{-7} = \dfrac{3}{7}\) | część odkreślona, patrz niżej |
| 12 | \(P = \dfrac{(-6)}{2 \cdot (-6) - 2} = \dfrac{-6}{-14} = \dfrac{3}{7}\) | |
| 13 | \(L = P\), więc rozwiązaniem równania jest \(x = -6\). | zdanie zamykające, wraca do polecenia |

Dziesięć linijek rachunku, potem odkreślone sprawdzenie: trzynaście pozycji razem.

## Sprawdzenie jako osobna część

Sprawdzenie stoi **pod kreską**, w bloku `rozw-sprawdzenie`, i tak ma być z trzech powodów:

- **Rachunek punktowany kończy się wyżej.** Klucz CKE daje trzeci punkt za wynik należący
  do dziedziny, czyli za linijkę 10. Wszystko poniżej jest dobrowolne i uczeń ma to widzieć,
  żeby nie myślał, że bez sprawdzenia rozwiązanie jest niepełne. Mówi to wprost pierwsze
  zdanie bloku.
- **Liczba ujemna wchodzi w nawiasie**: \((-6) + 3\), a nie \(-6 + 3\). Podstawianie liczby
  ujemnej bez nawiasu to jedno z najczęstszych miejsc, w których ucieka znak, więc pokazujemy
  zapis, który przed tym chroni, zamiast o tym ostrzegać.
- **Liczymy \(L\) i \(P\) osobno**, a wniosek \(L = P\) jest dopiero na końcu. Uczeń widzi
  metodę, którą może powtórzyć w każdym równaniu, a nie jednorazową sztuczkę.

## Trzy miejsca, w których celowo nie skracam

- **Komentarz pod linijką 2.** Bez niego cała metoda wisi na dostrzeżeniu wspólnego czynnika,
  a to jest ten pomysł, którego słabszy uczeń sam nie ma. Mówimy go wprost.
- **Linijka 4.** Mnożenie i skracanie to dwie czynności. Przejście z 3 od razu do
  \(x + 3 = \dfrac{x}{2}\) kasuje dwa nawiasy naraz i wygląda jak magia.
- **Linijki 7, 8 i 9.** Przenoszenie po jednym składniku, z dopiskiem działania. To jest
  miejsce, w którym ginie minus.

## Rozbrojone typowe błędy, dwa

1. **Mianownik bez zastrzeżenia.** Założenie jest drugą linijką, zaraz po zapisie z treści,
   a nie dopiskiem na końcu.
2. **Zgubiony znak przy przenoszeniu.** Linijki 7 i 8 przenoszą po jednym składniku, każda
   z widocznym dopiskiem działania, a komentarz obok nazywa zmianę znaku.

## Co zmierzono

Serwer `tools/serwer.js`, Playwright, zadanie 8 z rozwiniętym rozwiązaniem, cztery ujęcia:
komputer i telefon, motyw jasny i ciemny.

- Strona nie przewija się w bok: `scrollWidth === clientWidth`, 1280 i 390.
- Blok mieści się w karcie telefonu: 298 px treści na 298 px miejsca.
- Żadna linijka nie łamie się w środku wzoru. Dopisek działania przy najszerszej linijce
  zawija się pod rachunek jako całość, i tak było zaprojektowane.
- Rachunek sprawdzony osobno: wszystkie przejścia są tożsamościami (test na 20 tysiącach
  losowych ułamków), \(-6\) spełnia równanie wyjściowe (\(L = P = \tfrac{3}{7}\)),
  a \(x = 1\) zeruje oba mianowniki.

## Film krok po kroku (zrobiony 2026-08-27, animacja napisana od nowa tego samego dnia)

**Dziesięć kroków**, jeden do jednego z linijkami 1 do 10. Sprawdzenia film nie pokazuje
(decyzja Henricha), więc rozwiązanie opisowe ma trzynaście pozycji, a film dziesięć kroków,
i ten rozjazd jest świadomy.

- Scena: `manimations/solutionZad8.py`, scenariusz ruchu z tabelą taktów i zieleni:
  `manimations/zad8-kroki.md`.
- Założenie \(x \ne 1\) pojawia się w kroku 2 i **zostaje w kadrze do końca filmu**, bo za nie
  jest osobny punkt. Od drugiej wersji jest **szare** (`#666666`), nie czarne: ma być czytelne,
  ale nie ma konkurować wzrokowo z rachunkiem.
- Dopiski działań są jeszcze bledsze (`#888888`) i pojawiają się na końcu kroku, w którym
  powstał stan, a gasną w kroku, który to działanie wykonuje. Tak samo jak w rozwiązaniu
  opisowym.

### Co było złe w pierwszej wersji i co się zmieniło

Henrich, wieczorem 2026-08-27: *„morf wrzucony na całą stronę równania zasłania to, co dzieje
się naprawdę"*, *„krok mógłby zawierać wyjaśnienie, a dopiero się kończyć prostym"*,
*„animacje zrób dokładnie, co do znaku"*.

- Pierwsza wersja robiła każdy krok jednym `TransformMatchingTex(..., transform_mismatches=True)`,
  czyli oddawała ruch automatowi. W połowie animacji pół równania było kleksem, w którym nie
  dało się odczytać ani starego zapisu, ani nowego. Sprawdzone na klatkach: w kroku 4 nawiasy
  i cyfry nakładały się na siebie w jednym miejscu.
- Druga wersja nie ma **ani jednego** automatycznego dopasowania. Każdy glif ma wskazaną parę,
  a to, co się pojawia albo znika, jest wypisane z nazwy. Mapa glifów jest policzona z renderu
  `index_labels` i spisana w komentarzu na górze sceny.
- Pięć kroków (2, 3, 6, 7, 10) liczy w środku **rachunek pomocniczy** i dopiero potem zostawia
  czystą linijkę. Największy jest krok 2: pokazuje, skąd bierze się \(x \ne 1\), bo oba
  mianowniki zjeżdżają w dół, dostają warunek \(\ne 0\) i zostają rozwiązane po kolei.
  Krok 2 trwa przez to około jedenastu sekund, i taka jest cena za to, że założenie przestaje
  spadać z nieba.
- Dwa chwyty przeciw zasłanianiu: czynnik wylatujący z dopisku najpierw staje **nad** miejscem,
  w które wejdzie (kroki 4 i 6), a składnik przenoszony na drugą stronę leci **łukiem nad
  znakiem równości** (kroki 8 i 9). Po prostej oba przechodziły po literach.

### Sprawdzone po renderze

Styki klatek SSIM od 0,99978 do 0,99993 (`tools/styk-klatek.sh`), zieleń zapala się i gaśnie
w każdym kroku do zera jednym ruchem (`tools/zielen-krokow.py`), `tools/test-krokow.js
--zadania=7` przechodzi na dwóch ziarnach, klatki obejrzane okiem w każdym kroku (pierwsza,
po zapaleniu koloru, w połowie ruchu, ostatnia).

### Opisy pod filmem

Przepisane razem z animacją. Film pokazuje teraz to, co wcześniej niósł sam tekst (dlaczego
\(x \ne 1\), skąd \(2(x-1)\), co się z czym skraca), więc opisy mówią już tylko **dlaczego
wolno** tak przekształcić, a nie **co widać**.

## Podpowiedź

Pole `hint` zostaje bez zmian: „Zanim cokolwiek policzysz, sprawdź, dla jakiego \(x\)
mianownik byłby zerem. Potem popatrz na oba mianowniki uważnie: nie są tak różne, jak
wyglądają." Przy tej metodzie podpowiedź i rozwiązanie mówią o tym samym pomyśle.

## Czego nie ustalono

Nie wiadomo, co dokładnie było złe w rozwiązaniu skasowanym rano 2026-08-27: Henrich
poprosił o pracę od zera bez podawania przyczyny.
