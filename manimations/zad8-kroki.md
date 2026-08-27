# Zadanie 8, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad8.py`. Projekt dydaktyczny i uzasadnienie metody:
[../issues/spec-zad8-2024-grudzien.md](../issues/spec-zad8-2024-grudzien.md).

Napisane **od nowa 2026-08-28, na wzór zadania 7** (polecenie Henricha: „zrób
rozwiązanie zwykłe i krok po kroku zupełnie od nowa, jakby stare nie istniało,
inspiruj się zadaniem 7"). Wersja z 2026-08-27 miała dziesięć kroków, pas rachunku
pomocniczego pod równaniem i rozwiązanie opisowe przeplecione zdaniami. Ta ma
dziewiętnaście kroków, żadnego pasa pomocniczego i rozwiązanie opisowe złożone
z samych wzorów.

## Co dokładnie wzięliśmy z zadania 7

| z zad. 7 | jak wygląda w zad. 8 |
|---|---|
| dwa tory liczone niezależnie, schodzące się na końcu w jedną linijkę | dziedzina: lewy mianownik ma swój tor, prawy swój, oba kończą się na \(x \ne 1\) i dopiero wtedy powstaje jedno założenie |
| tory liczone **po kolei**, nie równolegle, wynik pierwszego zostaje w kadrze | film robi najpierw cały lewy tor (kroki 2 i 3), potem cały prawy (kroki 4 do 6); lewy wynik czeka na dole po lewej |
| rozwiązanie opisowe to same wzory, bez zdań między linijkami | między linijkami nie ma ani jednego komentarza; wyjaśnienia poszły pod film |
| brakujące ogniwo dostaje **własny krok**, a nie przypis (zad. 7: „sama reguła znaku", „sam porządek zapisu") | osobne kroki dostały: \(2 \cdot x - 2 \cdot 1\), \(2 \cdot \frac{x}{2}\), \(2 \cdot x + 2 \cdot 3\), \(2x - 1x\) |

Ostatni wiersz jest powodem, dla którego kroków jest dziewiętnaście, a nie dziesięć.
Wcześniej te cztery ogniwa liczyły się **na boku**, mniejszym pismem, w pasie pod
równaniem. Teraz każde z nich jest pełną linijką rachunku i pełnym krokiem filmu,
więc pas pomocniczy przestał być potrzebny i scena go nie ma.

## Treść

Rozwiąż równanie: \[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\] Zapisz konieczne założenie i obliczenia.

Wynik: \(x = -6\). Zadanie otwarte, 3 punkty.

| Kryterium z klucza | Punkty | Gdzie to jest |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | krok 7, i zostaje w kadrze do końca filmu |
| równanie bez ułamków, np. \(2(x+3) = x\) | 1 | krok 13 |
| wynik \(x = -6\) należący do dziedziny | 1 | krok 19 |

## Metoda

Wspólny mianownik zamiast mnożenia na krzyż i zamiast równania kwadratowego: prawy
mianownik to \(2(x-1)\), więc najpierw mnożymy obie strony przez \((x-1)\) i skracamy
nawias, a potem przez \(2\). Dlaczego nie przez deltę: spec, sekcja o metodzie.

## Układ kadru

Trzy miejsca, przez cały film te same:

- **góra po lewej**: gotowe założenie \(x \ne 1\), szare `#666666`, od kroku 7 do końca;
- **środek**: rachunek, który nie rusza się ani razu;
- **dół, dwie kolumny**: tory dziedziny, ale tylko w krokach 2 do 7. Potem to miejsce
  zostaje puste do końca filmu.

Tory są **tej samej wielkości co rachunek**, bo to też są linijki rozwiązania, a nie
praca na boku. Tym się różnią od pasa pomocniczego z poprzedniej wersji, który był
celowo mniejszy.

## Kroki

Dziewiętnaście kroków, tyle samo linijek w rozwiązaniu opisowym.

### Dziedzina, dwa tory (kroki 1 do 7)

| # | Zapis po kroku | Ruch | Zieleń |
|---|---|---|---|
| 1 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2}\) | równanie wypisuje się samo | brak, nic się jeszcze nie dzieje |
| 2 | w lewej kolumnie \(x - 1 \ne 0\) | kopia lewego mianownika zjeżdża w lewą kolumnę, dopisuje się \(\ne 0\) | mianownik, gdy się odrywa |
| 3 | \(x \ne 1\) | jedynka leci **łukiem** nad znakiem \(\ne\), minus i zero znikają | minus i jedynka |
| 4 | w prawej kolumnie \(2x - 2 \ne 0\) | to samo z prawym mianownikiem; lewy wynik zostaje na miejscu | mianownik, gdy się odrywa |
| 5 | \(2x \ne 2\) | dwójka leci łukiem nad \(\ne\) | minus i dwójka |
| 6 | \(x \ne 1\) | dwójka sprzed iksa znika, dwójka po prawej staje się jedynką | obie dwójki |
| 7 | \(x \ne 1\) nad rachunkiem, szare | prawy wynik dojeżdża do lewego (są takie same), a gotowe założenie jedzie **pionowo** wzdłuż lewej krawędzi w górę | brak, nic się nie przelicza |

### Rachunek, jeden tor (kroki 8 do 19)

| # | Zapis po kroku | Ruch | Zieleń |
|---|---|---|---|
| 8 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2 \cdot x - 2 \cdot 1}\) | w mianowniku dopisują się kropki mnożenia i jedynka | jedynka, bo jej wcześniej nie było |
| 9 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)}\) | druga dwójka dojeżdża do pierwszej i zlewa się z nią, wjeżdżają nawiasy | obie dwójki |
| 10 | \(\dfrac{(x+3)(x-1)}{x-1} = \dfrac{x(x-1)}{2(x-1)}\) | nawias z dopisku \(\big/ \cdot (x-1)\) rozdwaja się, obie kopie lecą **górą** nad równanie, każda nad swój licznik, i dopiero potem zjeżdżają | samo \(x-1\) w środku nowych nawiasów, nawiasy zostają czarne |
| 11 | \(x + 3 = \dfrac{x}{2}\) | najpierw lewa strona, potem prawa: nawias odjeżdża z licznika i z mianownika naraz, do kreski ułamka | skracana para, osobno po lewej i po prawej |
| 12 | \(2(x+3) = 2 \cdot \dfrac{x}{2}\) | dwójka z dopisku rozdwaja się, staje nad swoimi miejscami i zjeżdża: po lewej przed nawias, po prawej przed ułamek | obie dwójki |
| 13 | \(2(x+3) = x\) | dwójka sprzed ułamka i dwójka z mianownika odjeżdżają do kreski | skracana para |
| 14 | \(2 \cdot x + 2 \cdot 3 = x\) | dwójka sprzed nawiasu rozdwaja się, nawiasy znikają, wjeżdżają kropki | obie dwójki |
| 15 | \(2x + 6 = x\) | kropka przy \(2 \cdot x\) znika, a \(2\), kropka i \(3\) zjeżdżają się w szóstkę | dwójka, trójka i powstająca szóstka |
| 16 | \(2x = x - 6\) | plus i szóstka lecą **łukiem nad znakiem równości**, plus po drodze zamienia się w minus | plus i szóstka |
| 17 | \(2x - x = -6\) | iks leci łukiem na lewą stronę, a przed nim pojawia się minus, bo wcześniej żadnego znaku tam nie było | przenoszony iks i nowy minus |
| 18 | \(2x - 1x = -6\) | przy drugim iksie pojawia się jedynka | jedynka |
| 19 | \(x = -6\) | minus i jedynka dojeżdżają do dwójki, dwójka staje się jedynką, drugi iks wtapia się w pierwszy, a na końcu jedynka sprzed iksa znika | odejmowana trójka znaków, potem znikająca jedynka |

Dopiski działań (\(\big/ \cdot (x-1)\), \(\big/ \cdot 2\), \(\big/ - 6\), \(\big/ - x\)) są szare
`#888888`, pojawiają się na końcu kroku, w którym powstał stan, i gasną w kroku, który to
działanie wykonuje. Tak samo wyglądają w rozwiązaniu opisowym (klasa `.rozw-dzialanie`).

### Cztery chwyty, które warto powtórzyć w innych scenach

- **Postój nad celem.** Czynnik, który wylatuje z dopisku działania, nie leci po skosie przez
  środek równania, tylko najpierw staje **nad** miejscem, w które wejdzie, i dopiero potem
  zjeżdża. Kroki 10 i 12, funkcja `postoj()` w scenie.
- **Łuk przy przenoszeniu na drugą stronę.** Składnik przenoszony przez znak równości (albo
  przez \(\ne\)) leci `path_arc`, nie po prostej: po prostej przez ułamek sekundy leży
  dokładnie na znaku i zasłania go. Kroki 3, 5, 16 i 17.
- **Ogniwo jako pełny krok.** To, co ekspert liczy w głowie, dostaje własną linijkę i własny
  krok, zamiast być liczone mniejszym pismem na boku. Kroki 8, 12, 14 i 18.
- **Warunek na górze, przy lewej krawędzi.** Wjeżdża tam pionowo, wzdłuż lewego brzegu kadru,
  a nie po skosie przez środek: po skosie przelatywałby po literach równania.

## Czego film nie pokazuje

Sprawdzenia przez podstawienie \(x = -6\). Jest tylko w rozwiązaniu opisowym, jako osobna,
odkreślona część (decyzja Henricha, 2026-08-27). Klucz CKE go nie wymaga, a film kończy się
na wyniku, który stoi w kadrze razem z założeniem.

## Pułapka techniczna, na której ta scena się przejechała

**Ułamka nie wolno ciąć na argumenty `MathTex`.** Manim renderuje każdy argument osobno
i domyka w nim klamry, więc `MathTex(r"\frac{(x+3)", r"(x-1)", r"}{x-1}")` kompiluje kawałek
`\frac{(x+3)}`, czyli `\frac` z jednym argumentem, i render pada na `Missing } inserted`.
Dlatego każdy stan jest **jednym** `MathTex`, a uchwyty bierze się z numerów glifów. Numery
są policzone z pozycji glifów, nie zgadnięte, i spisane w komentarzu na górze sceny;
zmierzone przy okazji: MathTex numeruje glify w kolejności czytania, w ułamku idzie licznik,
potem kreska, potem mianownik, a `\ne` to **dwa** glify (kreski i ukośnik).

## Sprawdzone po renderze (2026-08-28)

- `tools/styk-klatek.sh`: wszystkie osiemnaście styków SSIM od 0,99977 do 0,99993.
- `tools/zielen-krokow.py`: w każdym kroku zieleń zapala się i gaśnie do zera jednym ruchem,
  a kroki 1 i 7 nie mają jej wcale, bo nic się w nich nie przelicza.
- `tools/test-krokow.js --zadania=7` na ziarnach 3 i 11, na serwerze zdławionym: bez zastrzeżeń.
- Klatki obejrzane okiem: końcowe wszystkich kroków plus środek kroków 2, 6, 7, 10 i 11.
- Zrzuty rozwiązania opisowego: komputer i telefon (485 px), motyw jasny i ciemny; strona
  nie przewija się w bok, siatka torów nie obcina się (\(0\) px w każdym z czterech ujęć).
