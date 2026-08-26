# Projekt lepszych rozwiązań: zadanie 8, arkusz 2024-grudzień

Dokument projektowy, nie kod. Opisuje, co uczeń ma zobaczyć i zrozumieć.
Wpisanie do repozytorium rządzi się `SOLUTION_TEXT_RULES.md` i `manimations/README.md`.

Data: 2026-08-26. **Wdrożone tego samego dnia** (v85 Beta). Robione zaraz po tym samym przeglądzie zad. 7
(`issues/projekt-zad7-2024-grudzien.md`).

## Zadanie i klucz

Rozwiąż równanie \[\frac{x+3}{x-1} = \frac{x}{2x-2}\] Zapisz konieczne założenie i obliczenia.
Zadanie otwarte za 3 punkty, uczeń ocenia się sam (`selfScore`).

Policzone od zera: \(2x-2 = 2(x-1)\), więc oba mianowniki zerują się dla \(x=1\), stąd
założenie \(x \ne 1\). Po pomnożeniu obu stron przez \(2(x-1)\) zostaje \(2(x+3) = x\),
czyli \(2x + 6 = x\), a stąd \(x = -6\). Wynik mieści się w dziedzinie.

**Zgadza się z kluczem CKE** (`odpowiedzi.pdf`, zadanie 8): 3 pkt za poprawną metodę
razem z założeniem \(x \ne 1\) i wynikiem \(x = -6\). Klucz dopuszcza też drogę przez
równanie kwadratowe \((x+3)(2x-2) = x(x-1)\); my zostajemy przy liniowej, bo jest krótsza
i to ona stoi w kluczu jako pierwsza.

## Stan na wejściu: co jest dobre

Warto to zapisać, żeby nikt tego nie „poprawił". Scena filmu została napisana od nowa
2026-08-23 i trzyma się zasad z 21 sierpnia:

- **Założenie ma własny krok i zostaje na ekranie do końca filmu.** CKE daje za nie osobny
  punkt, więc nie ma prawa mignąć i zniknąć.
- **Miejsce pod równaniem jest zarezerwowane od pierwszej klatki**, więc zapis nie podskakuje,
  kiedy pojawia się założenie i sprawdzenie.
- **Ostatni krok wraca do założenia** i podstawia w nie wynik, zamiast poprzestać na \(x=-6\).
- **Rozwiązanie opisowe pokrywa wszystkie trzy kryteria CKE**: założenie na górze,
  \(2(x+3)=x\) w środku, wynik ze sprawdzeniem na dole. Sprawdzone punkt po punkcie.

## Co jest nie tak

| miejsce | co jest teraz | dlaczego to wada |
|---|---|---|
| podpowiedź | „Zacznij od określenia dziedziny. Zauważ, że \(2x-2 = 2(x-1)\), oba mianowniki znikną po pomnożeniu przez \(2(x-1)\)" | podaje całą metodę, a za samą metodę CKE daje dwa z trzech punktów. Po jej przeczytaniu zostaje do zrobienia rachunek na poziomie pierwszej klasy |
| podpowiedź | zawiera półpauzę | znak zakazany w całym projekcie (`CLAUDE.md`) |
| krok 7 | \(2x + 6 = x\) przechodzi od razu w \(2x - x = -6\) | dwa przeniesienia w jednym kroku: \(x\) idzie w lewo, a \(6\) w prawo. Oba zmieniają znak, więc to jest dokładnie to miejsce, w którym uczeń gubi minus |
| opis kroku 1 | „Zapisujemy równanie z zadania" | opisuje słowami to, co widać w kadrze |

## Dwie pułapki, które rozbrajamy

Z `references/typowe-bledy.md`, wplecione w te kroki, w których grożą.

- **Pominięta dziedzina** (grupa „Funkcje, wykresy, nierówności"). Tu nie jest to ozdobnik,
  tylko jeden z trzech punktów. Rozbrojone już dziś i zostaje bez zmian: własny krok filmu,
  założenie widoczne do końca, sprawdzenie w ostatnim kroku.
- **Zmiana znaku przy przenoszeniu na drugą stronę** (grupa „Znaki, nawiasy, ułamki").
  Uczeń, który przeniesie jedno i zapomni o drugim, dostaje \(x = 6\) albo \(x = -2\).
  Rozbrajamy rozbiciem kroku 7 na dwa, żeby w jednym kroku zmieniał znak dokładnie
  jeden składnik.

## Podpowiedź

> Zanim cokolwiek policzysz, sprawdź, dla jakiego \(x\) mianownik byłby zerem.
> Potem popatrz na oba mianowniki uważnie: nie są tak różne, jak wyglądają.

Dlaczego tak: pierwsza linijka kieruje na dziedzinę, czyli na punkt, który uczeń
najczęściej po prostu pomija, a nie na metodę. Druga mówi, gdzie patrzeć, ale **nie mówi,
co zobaczyć**: to uczeń ma dostrzec, że \(2x-2\) to \(2(x-1)\). Dziś podpowiedź podaje mu
to gotowe razem z całym planem.

## Rozwiązanie opisowe

Układ **jednej kolumny** bez zmian (`rozwiazanie-kroki`): wzoru z tablicy tu nie ma wcale,
więc nie ma czego stawiać obok i nie ma czego kolorować.

Nad rachunkiem zostaje bez zmian założenie razem ze zdaniem, skąd się wzięło.

Linijki rachunku:

1. \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2}\)
2. \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)}\)
3. \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)} \;\big/ \cdot\, 2(x-1)\)
4. \(2(x+3) = x\)
5. \(2x + 6 = x\)
6. \(2x = x - 6\)  ← **nowa linijka**
7. \(2x - x = -6\)
8. \(\boldsymbol{x = -6}\)

Pod rachunkiem zostaje bez zmian zdanie sprawdzające założenie i wracające do polecenia.

Razem **osiem linijek rachunku plus założenie i zdanie końcowe**, czyli dziesięć kroków
filmu. Dziś jest siedem plus dwa, czyli dziewięć.

## Film krok po kroku

Zmieniają się dwa kroki i jeden opis. Reszta zostaje dokładnie taka, jaka jest.

**Krok 1, zmiana opisu.** Animacja bez zmian. Opis znika, bo mówił tylko to, co widać.
Nic tu nie ma do dodania, czego uczeń nie widzi na ekranie.

**Krok 7, nowy.** Przed: \(2x + 6 = x\). Zapala się na zielono plus przed szóstką
oraz sama szóstka, bo to one zmieniają stronę i znak. Ruch: **plus przelatuje przez znak
równości razem z szóstką i po drodze zamienia się w minus**, a nie znika i pojawia się obok.
Litera \(x\) po prawej zostaje na miejscu i zostaje czarna: w tym kroku nikt jej nie rusza.
Po: \(2x = x - 6\).
Opis: „Najpierw przenosimy tylko liczbę. Szóstka zmienia znak, bo przechodzi na drugą stronę."

**Krok 8, dawny krok 7 po odchudzeniu.** Przed: \(2x = x - 6\). Zapala się na zielono
litera \(x\) po prawej stronie. Ruch: \(x\) przelatuje przez znak równości na lewo, a przed
nim **pojawia się** zielony minus, którego wcześniej nie było. Szóstka razem ze swoim minusem
stoi w miejscu i jest czarna. Po: \(2x - x = -6\).
Opis: „Teraz przenosimy \(x\). On też zmienia znak."

Kroki 2 do 6 oraz 9 i 10 to dawne kroki 2 do 6 oraz 8 i 9, bez zmian w animacji.

## Widżet

**Nie projektuję i nie polecam.** Rozwiązywanie równania wymiernego to ciąg przekształceń:
nie ma tu wielkości, którą uczeń mógłby poruszyć, ani zależności do zaobserwowania.
Pole `solutionWidget` zostaje puste.

## Rozważone i odrzucone

- **Rozbicie kroku 5 (skracanie) na dwa.** Kusi, bo w jednym kroku dzieje się mnożenie obu
  stron i skracanie po obu stronach naraz. Odrzucone z powodu technicznego, nie dydaktycznego:
  stan pośredni musiałby wyglądać jak \(\dfrac{(x+3)\cdot 2(x-1)}{x-1} = \dfrac{x \cdot 2(x-1)}{2(x-1)}\),
  a scena skaluje **wszystkie** kroki do najszerszego stanu. Jedna szeroka klatka zmniejszyłaby
  cały film, łącznie z krokami, które są dziś czytelne. Zysk w jednym kroku, strata w dziesięciu.
  Gdyby kiedyś wracać do tego pomysłu, trzeba najpierw rozwiązać skalowanie, a nie sam krok.

## Czego nie ustalono

- **Czy nowa podpowiedź nie jest już za słaba.** Trzecia linijka celowo nie mówi, co uczeń
  ma zobaczyć w mianownikach. Sprawdzalne tylko na uczniu.
- **Czy krok 5 rzeczywiście czyta się jako skracanie.** Zasady wizualne mówią, że czynnik ma
  odjechać z licznika i z mianownika jednocześnie, a nie zniknąć sam z siebie. W obecnej
  scenie oba mianowniki gasną razem, co spełnia literę tej zasady, ale czy uczeń widzi w tym
  parę, tego z klatek nie ocenię.
