# Spec: zadanie 8, arkusz 2024-grudzień, rozwiązanie opisowe i film

Stan na **2026-08-28**, wpisane do `exercises.json` i wyrenderowane. Trzecie podejście do
tego zadania:

1. rano 2026-08-27: przez równanie kwadratowe i deltę. Skasowane (Henrich: za dużo kroków,
   delta niepotrzebna);
2. 2026-08-27: wspólny mianownik, dziesięć linijek przeplecionych bledszymi komentarzami,
   film z pasem rachunku pomocniczego pod równaniem;
3. **2026-08-28, to podejście**: ta sama metoda, ale zapis i film przerobione „jakby stare
   nie istniało, na wzór zadania 7" (polecenie Henricha).

## Treść i wynik

Rozwiąż równanie \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2x - 2}\). Zapisz konieczne
założenie i obliczenia. Zadanie otwarte, 3 punkty. Wynik: \(x = -6\), zgodny z kluczem CKE.

## Metoda (bez zmian od 2026-08-27)

Wspólny mianownik i dwa mnożenia obu stron, każde przez inny czynnik:

1. widzimy, że prawy mianownik to \(2(x - 1)\), czyli ten sam nawias co po lewej,
2. mnożymy obie strony przez \((x - 1)\) i skracamy ten nawias po obu stronach,
3. mnożymy obie strony przez \(2\), znika ostatni ułamek,
4. zostaje zwykłe równanie pierwszego stopnia.

Żadnego wzoru z tablicy, żadnej delty, żadnego równania kwadratowego. Klucz CKE wymienia
tę drogę wprost jako poprawną (\(2(x+3) = x\) stoi w zasadach oceniania).

## Co zmieniło podejście „na wzór zadania 7"

Zadanie 7 ma dwie cechy, których zadanie 8 nie miało, i o te dwie chodziło:

**1. Dwa tory, które schodzą się w jedną linijkę.** W zadaniu 7 osobno liczy się \(a\),
osobno \(b\), a dopiero na końcu ich iloczyn. W zadaniu 8 taką parą są **dwa mianowniki**:
lewy daje warunek \(x - 1 \ne 0\), prawy \(2x - 2 \ne 0\), oba kończą się na \(x \ne 1\)
i dopiero wtedy powstaje jedno założenie. Wcześniej dziedzina spadała z nieba jako jedna
linijka z komentarzem „oba zerują się dla \(x = 1\)"; teraz uczeń widzi, że sprawdzono oba
mianowniki, i widzi, dlaczego wystarcza jeden warunek.

W rozwiązaniu opisowym tory stoją **obok siebie** (`rozw-2kol rozw-dwatory`, jak w zad. 7),
w filmie liczą się **po kolei**: najpierw cały lewy, potem cały prawy, a wynik lewego czeka
w kadrze. To też jest wprost zasada z zad. 7 (`manimations/README.md`, „Ile kroków", punkt 4).

**2. Ogniwo dostaje własny krok, a nie pracę na boku.** Zadanie 8 miało film z pasem
rachunku pomocniczego mniejszym pismem, w którym liczyło się to, czego ekspert nie zapisuje.
**Teraz każde takie ogniwo jest pełną linijką rachunku i pełnym krokiem filmu**, więc pas
pomocniczy zniknął. Tak samo robi zad. 7, gdzie „sama reguła znaku" i „sam porządek zapisu"
dostały własne kroki.

Cztery ogniwa wypisane jawnie: \(2 \cdot x - 2 \cdot 1\) (skąd \(2(x-1)\)),
\(2 \cdot \dfrac{x}{2}\) (co się z czym skraca), \(2 \cdot x + 2 \cdot 3\) (opuszczanie
nawiasu), \(2x - 1x\) (skąd jeden iks). Stąd dziewiętnaście kroków zamiast dziesięciu.

**Zdania między linijkami wróciły tego samego dnia, ale wybiórczo** (Henrich, po obejrzeniu
pierwszej wersji: „przywróć zdania tam, gdzie uczeń miałby problem zrozumieć, skąd się coś
wzięło, lub gdy dużo się zmieniało, np. podczas skracania \((x-1)\)"). Jest ich siedem na
dziewiętnaście linijek, a nie po jednym pod każdą, i stoją pod tymi przejściami, których
sam zapis nie tłumaczy: skąd pomysł na wspólny nawias, dlaczego wolno mnożyć przez \((x-1)\),
co dokładnie znika przy skracaniu, dlaczego dwójka staje przed nawiasem, po co dopisujemy
jedynkę przy iksie. Przejścia oczywiste (przeniesienie składnika, policzenie \(2 \cdot 3\))
zostają bez komentarza.

**Przerwy.** Po wyliczeniu dziedziny idzie szersza przerwa (`rozw-odstep`), żeby było widać,
że zaczyna się nowa część, i taka sama przed zdaniem zamykającym. Zdania są odsunięte od
rachunku z obu stron, bo w pierwszej wersji kleiły się do wzorów i całość czytała się jak
jeden blok.

**Koszt tej decyzji.** Kroków jest o dziewięć więcej i film trwa dłużej. Zysk: nie ma ani
jednego miejsca, w którym coś jest liczone „na boku", a uczeń, który zatrzyma dowolny krok,
widzi w kadrze pełną linijkę do przepisania, nie roboczy zapis mniejszym pismem.

## Kryteria CKE i gdzie są pokryte

| Kryterium | Punkty | Gdzie |
|---|---|---|
| zapisane założenie \(x \ne 1\) | 1 | linijka 7 (wytłuszczona, pod torami) |
| równanie bez ułamków, np. \(2(x+3) = x\) | 1 | linijka 13 |
| wynik \(x = -6\) należący do dziedziny | 1 | linijki 19 i 20 |

## Linijki

Dziewiętnaście linijek rachunku, potem zdanie zamykające, potem odkreślone sprawdzenie.
Linijek rachunku jest dokładnie tyle, ile kroków filmu.

| # | Linijka | Uwaga |
|---|---|---|
| 1 | \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2x - 2}\) | zapis z treści |
| 2 | \(x - 1 \ne 0\) | lewy tor |
| 3 | \(x \ne 1\) | lewy tor, koniec |
| 4 | \(2x - 2 \ne 0\) | prawy tor |
| 5 | \(2x \ne 2\) | |
| 6 | \(x \ne 1\) | prawy tor, koniec |
| 7 | \(\boldsymbol{x \ne 1}\) | oba tory dały to samo, więc jedno założenie |
| 8 | \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2 \cdot x - 2 \cdot 1}\) | ogniwo: skąd wspólny czynnik |
| 9 | \(\dfrac{x + 3}{x - 1} = \dfrac{x}{2(x - 1)}\) z dopiskiem \(\big/ \cdot (x - 1)\) | |
| 10 | \(\dfrac{(x + 3)(x - 1)}{x - 1} = \dfrac{x(x - 1)}{2(x - 1)}\) | |
| 11 | \(x + 3 = \dfrac{x}{2}\) z dopiskiem \(\big/ \cdot 2\) | |
| 12 | \(2(x + 3) = 2 \cdot \dfrac{x}{2}\) | ogniwo: co się z czym skraca |
| 13 | \(2(x + 3) = x\) | punkt CKE |
| 14 | \(2 \cdot x + 2 \cdot 3 = x\) | ogniwo: opuszczanie nawiasu |
| 15 | \(2x + 6 = x\) z dopiskiem \(\big/ - 6\) | |
| 16 | \(2x = x - 6\) z dopiskiem \(\big/ - x\) | |
| 17 | \(2x - x = -6\) | |
| 18 | \(2x - 1x = -6\) | ogniwo: \(x\) to \(1x\) |
| 19 | \(\boldsymbol{x = -6}\) | |
| 20 | Wynik spełnia założenie, bo \(-6 \ne 1\), więc rozwiązaniem równania jest \(x = -6\). | wiersz na całą szerokość, nie jest krokiem filmu |

Pod kreską sprawdzenie: \(L\), \(P\), \(L = P\).

## Sprawdzenie jako osobna część (bez zmian)

Sprawdzenie stoi **pod kreską**, w bloku `rozw-sprawdzenie`, i tak ma być z trzech powodów:

- **Rachunek punktowany kończy się wyżej.** Klucz CKE daje trzeci punkt za wynik należący
  do dziedziny, czyli za linijkę 19. Wszystko poniżej jest dobrowolne i uczeń ma to widzieć,
  żeby nie myślał, że bez sprawdzenia rozwiązanie jest niepełne.
- **Liczba ujemna wchodzi w nawiasie**: \((-6) + 3\), a nie \(-6 + 3\). Podstawianie liczby
  ujemnej bez nawiasu to jedno z najczęstszych miejsc, w których ucieka znak, więc pokazujemy
  zapis, który przed tym chroni, zamiast o tym ostrzegać.
- **Liczymy \(L\) i \(P\) osobno**, a wniosek \(L = P\) jest dopiero na końcu. Uczeń widzi
  metodę, którą może powtórzyć w każdym równaniu, a nie jednorazową sztuczkę.

## Trzy miejsca, w których celowo nie skracam

- **Linijki 2 do 7.** Cała metoda wisi na dostrzeżeniu wspólnego czynnika, a dziedzina jest
  pierwszym miejscem, w którym oba mianowniki stoją obok siebie. Uczeń widzi tam, że
  \(2x-2\) i \(x-1\) dają ten sam warunek, zanim jeszcze zacznie liczyć.
- **Linijki 9 i 10.** Mnożenie i skracanie to dwie czynności. Przejście od razu do
  \(x + 3 = \dfrac{x}{2}\) kasuje dwa nawiasy naraz i wygląda jak magia.
- **Linijki 15 do 19.** Przenoszenie po jednym składniku, z dopiskiem działania. To jest
  miejsce, w którym ginie minus.

## Rozbrojone typowe błędy, dwa

1. **Mianownik bez zastrzeżenia.** Dziedzina zajmuje sześć pierwszych linijek rachunku,
   zanim cokolwiek się policzy, a w filmie gotowy warunek stoi nad rachunkiem do końca.
2. **Zgubiony znak przy przenoszeniu.** Linijki 16 i 17 przenoszą po jednym składniku, każda
   z widocznym dopiskiem działania, a w filmie przenoszony składnik leci łukiem NAD znakiem
   równości, więc widać, że to ten sam znak zmienia się w drodze.

## Co zmierzono (2026-08-28)

Serwer `tools/serwer.js`, Playwright, zadanie 8 z rozwiniętym rozwiązaniem, cztery ujęcia:
komputer 1280 i telefon 485, motyw jasny i ciemny.

- Strona nie przewija się w bok: `scrollWidth - clientWidth = 0` w każdym ujęciu.
- Siatka dwóch torów nie obcina się: `el.scrollWidth - el.clientWidth = 0` w każdym ujęciu.
- Film: `tools/styk-klatek.sh` wszystkie osiemnaście styków od 0,99977 do 0,99993;
  `tools/zielen-krokow.py` bez zastrzeżeń; `tools/test-krokow.js --zadania=7` na dwóch
  ziarnach, na serwerze zdławionym, bez zastrzeżeń.
- Rachunek sprawdzony osobno: wszystkie przejścia są tożsamościami, \(-6\) spełnia równanie
  wyjściowe (\(L = P = \tfrac{3}{7}\)), a \(x = 1\) zeruje oba mianowniki.

## Podpowiedź

Pole `hint` zostaje bez zmian: „Zanim cokolwiek policzysz, sprawdź, dla jakiego \(x\)
mianownik byłby zerem. Potem popatrz na oba mianowniki uważnie: nie są tak różne, jak
wyglądają." Przy tej metodzie podpowiedź, dwa tory dziedziny i rozwiązanie mówią o tym
samym pomyśle.

## Czego nie ustalono

- Nie wiadomo, co dokładnie było złe w wersji z 2026-08-27: Henrich poprosił o pracę od
  zera „na wzór zadania 7" bez podawania przyczyny. Powyższe dwie cechy zadania 7 to
  odczytanie tego polecenia, potwierdzone przez niego przed pisaniem sceny, a nie diagnoza
  poprzedniej wersji.
- Nie wiadomo, czy dziewiętnaście kropek kroków dobrze się klika na telefonie Henricha:
  to najdłuższy film w arkuszu (poprzedni rekord to czternaście kroków w zad. 7). Wpisane
  do `TODO.md`, sekcja `TESTOWANIE HENRICH`.
- Zad. 8 jest nadal **jedynym** zadaniem z komentarzami `rozw-komentarz`. Czy siedem zdań
  na dziewiętnaście linijek to dobra proporcja, wyjdzie dopiero na innych zadaniach.
