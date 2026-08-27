# Zadanie 8, kroki rozwiązania

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.

Scena: `solutionZad8.py`. Projekt dydaktyczny i uzasadnienie metody:
[../issues/spec-zad8-2024-grudzien.md](../issues/spec-zad8-2024-grudzien.md).

Animacja napisana **od nowa 2026-08-27 wieczorem**, po uwagach Henricha do pierwszej wersji
z tego samego dnia. Cztery uwagi i co z nich wyszło:

1. **„Morf wrzucony na całą stronę równania zasłania to, co dzieje się naprawdę."**
   Pierwsza wersja robiła każdy krok jednym `TransformMatchingTex(..., transform_mismatches=True)`.
   Automat dopasowywał sobie kawałki sam, więc w połowie animacji pół równania było kleksem,
   w którym nie dało się odczytać ani starego zapisu, ani nowego. Dziś w scenie **nie ma ani
   jednego automatycznego dopasowania**: każdy glif ma wskazaną parę, a to, co się pojawia albo
   znika, jest wypisane z nazwy. Mapa glifów siedzi w komentarzu na górze sceny i jest
   **policzona** z renderu `index_labels`, nie zgadnięta.
2. **„Krok mógłby zawierać wyjaśnienie, a dopiero się kończyć prostym."**
   Pięć kroków (2, 3, 6, 7, 10) liczy w środku rachunek pomocniczy i dopiero potem zostawia
   w kadrze czystą linijkę. Rachunek pomocniczy jest **mniejszy** od rachunku głównego, stoi
   w osobnym pasie pod równaniem i po użyciu znika.
3. **„Założenie mniej kontrastowe."** \(x \ne 1\) stoi w kadrze od kroku 2 do końca filmu,
   ale szarością `#666666`, nie czernią.
4. **„Daj to założenie na górze, a nie na dole, taka jest konwencja przy rozwiązywaniu na
   kartce."** Warunek stoi więc NAD rachunkiem, przy lewej krawędzi. Kadr ma trzy pasy:
   warunek na górze, rachunek na środku, rachunek pomocniczy pod spodem.

## Treść

Rozwiąż równanie: \[\frac{x + 3}{x - 1} = \frac{x}{2x - 2}\] Zapisz konieczne założenie i obliczenia.

Wynik: \(x = -6\). Zadanie otwarte, 3 punkty.

| Kryterium z klucza | Punkty | Gdzie to jest |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | krok 2, i zostaje w kadrze do końca filmu |
| równanie bez ułamków, np. \(2(x+3) = x\) | 1 | krok 6 |
| wynik \(x = -6\) należący do dziedziny | 1 | krok 10 |

## Metoda

Wspólny mianownik zamiast mnożenia na krzyż i zamiast równania kwadratowego: prawy mianownik
to \(2(x-1)\), więc najpierw mnożymy obie strony przez \((x-1)\) i skracamy nawias, a potem
przez \(2\). Dlaczego nie przez deltę: spec, sekcja o metodzie.

## Kroki

Dziesięć kroków, tyle samo linijek rachunku w rozwiązaniu opisowym. Kolumna „ruch" jest tu
ważniejsza od kolumny „zapis po kroku": to ona mówi, co uczeń ma zobaczyć.

| # | Zapis po kroku | Ruch, takt po takcie | Zieleń |
|---|---|---|---|
| 1 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2x-2}\) | równanie wypisuje się samo | brak, nic się jeszcze nie dzieje |
| 2 | nad rachunkiem, przy lewej krawędzi, szare \(x \ne 1\) | (a) lewy mianownik zapala się i jego kopia zjeżdża w lewą kolumnę, dopisuje się \(\ne 0\); (b) jedynka przelatuje przez \(\ne\), minus i zero znikają, zostaje \(x \ne 1\); (c) to samo z prawym mianownikiem, w prawej kolumnie: \(2x-2 \ne 0\), potem \(2x \ne 2\), potem dzielimy przez dwa i zostaje \(x \ne 1\); (d) prawy wynik dojeżdża do lewego, bo oba są takie same; (e) gotowe założenie jedzie pionowo w górę, nad rachunek, i tam zostaje do końca filmu | element, który się rusza albo powstaje, po jednym na takt |
| 3 | \(\dfrac{x+3}{x-1} = \dfrac{x}{2(x-1)}\) | (a) prawy mianownik zapala się, kopia zjeżdża pod ułamek; (b) dopisujemy ogniwo \(2\cdot x - 2\cdot 1\); (c) druga dwójka dojeżdża do pierwszej i zlewa się z nią, wjeżdżają nawiasy; (d) gotowe \(2(x-1)\) wraca w górę na miejsce starego mianownika, reszta równania przesuwa się glif po glifie | jedynka, gdy się pojawia; potem obie dwójki, gdy się zlewają |
| 4 | \(\dfrac{(x+3)(x-1)}{x-1} = \dfrac{x(x-1)}{2(x-1)}\) | (a) nawias z dopisku \(\big/ \cdot (x-1)\) rozdwaja się i obie kopie lecą **górą**, nad równanie, każda nad swój licznik; (b) zjeżdżają w liczniki, równanie robi im miejsce | oba dopisane nawiasy |
| 5 | \(x + 3 = \dfrac{x}{2}\) | najpierw lewa strona, potem prawa: nawias odjeżdża z licznika **i** z mianownika jednocześnie, do kreski ułamka, a kreska znika razem z nim | skracana para, osobno po lewej i po prawej |
| 6 | \(2(x + 3) = x\) | (a) dwójka z dopisku rozdwaja się i obie kopie stają nad swoimi miejscami; (b) zjeżdżają: po lewej przed nawias, po prawej przed ułamek, powstaje \(2(x+3) = 2\cdot\frac{x}{2}\); (c) dwójka sprzed ułamka i dwójka z mianownika skracają się | obie dwójki, potem skracana para |
| 7 | \(2x + 6 = x\) | (a) dwójka sprzed nawiasu rozdwaja się na \(2\cdot x + 2\cdot 3\), nawiasy znikają; (b) dwójka, kropka i trójka zjeżdżają się w szóstkę | obie dwójki, potem szóstka |
| 8 | \(2x = x - 6\) | plus i szóstka lecą **łukiem nad znakiem równości** (po prostej przechodziłyby po nim), plus po drodze zamienia się w minus | plus i szóstka |
| 9 | \(2x - x = -6\) | iks leci łukiem na lewą stronę, a przed nim pojawia się minus, bo wcześniej żadnego znaku tam nie było | przenoszony iks i nowy minus |
| 10 | \(x = -6\) | (a) przy drugim iksie pojawia się jedynka (\(x\) to \(1x\)); (b) minus i jedynka dojeżdżają do dwójki, dwójka staje się jedynką, drugi iks wtapia się w pierwszy; (c) jedynka sprzed iksa znika | jedynka, potem odejmowana trójka znaków, potem znikająca jedynka |

Dopiski działań (\(\big/ \cdot (x-1)\), \(\big/ \cdot 2\), \(\big/ - 6\), \(\big/ - x\)) są szare
`#888888`, pojawiają się na końcu kroku, w którym powstał stan, i gasną w kroku, który to
działanie wykonuje. Tak samo wyglądają w rozwiązaniu opisowym (klasa `.rozw-dzialanie`).

### Cztery chwyty, które warto powtórzyć w innych scenach

- **Postój nad celem.** Czynnik, który wylatuje z dopisku działania, nie leci po skosie przez
  środek równania (tak było w pierwszej wersji i w połowie animacji nie dało się nic odczytać),
  tylko najpierw staje **nad** miejscem, w które wejdzie, i dopiero potem zjeżdża. Kroki 4 i 6,
  funkcja `postoj()` w scenie.
- **Łuk przy przenoszeniu na drugą stronę.** Składnik przenoszony przez znak równości leci
  `path_arc`, nie po prostej: po prostej przez ułamek sekundy leży dokładnie na znaku równości
  i zasłania go. Kroki 8 i 9.
- **Pas rachunku pomocniczego.** Wszystko, co jest wyjaśnieniem, a nie linijką rozwiązania,
  liczy się mniejszym pismem pod równaniem i znika przed końcem kroku. Dzięki temu ostatnia
  klatka kroku dalej jest czysta i styk klatek wychodzi sam.
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
są policzone z podglądu `index_labels` i spisane w komentarzu na górze sceny; zmierzone przy
okazji: MathTex numeruje glify w kolejności czytania, w ułamku idzie licznik, potem kreska,
potem mianownik, a `\ne` to **dwa** glify (kreski i ukośnik).

## Sprawdzone po renderze

- `tools/styk-klatek.sh`: wszystkie dziewięć styków SSIM od 0,99970 do 0,99991.
- `tools/zielen-krokow.py`: w każdym kroku zieleń zapala się i gaśnie do zera jednym ruchem.
- `tools/test-krokow.js --zadania=7` na dwóch ziarnach: bez zastrzeżeń.
- Klatki obejrzane okiem w każdym kroku: pierwsza, po zapaleniu koloru, w połowie ruchu
  i ostatnia.
