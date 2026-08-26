# Wzorzec widżetu: Przewiduj, Obserwuj, Rozstrzygnij

Widżet projektujesz **tylko na wyraźne polecenie**. Ten plik mówi, jaki ma mieć kształt.
Mechanika, helpery, kolory i lista uwag Henricha: `widgets/PROJEKTOWANIE.md`.

Widżet ma odsłaniać **przyczynę** typowego błędu, a nie prezentować gotowy skutek.
To jedyne miejsce w projekcie, gdzie wolno pokazać błędną drogę, i tylko po to, żeby ją
na miejscu obalić.

---

## Trzy fazy

### 1. Przewiduj

Pytanie postawione uczniowi **zanim** cokolwiek się ruszy. Jedno, konkretne, z odpowiedzią
do wybrania albo do wpisania.

> „Wpłacasz 600 zł na dwa lata. Odsetki po drugim roku będą takie same jak po pierwszym
> czy większe?"

**Dlaczego to nie jest ozdobnik.** Chi i Wylie opisali cztery tryby zaangażowania ucznia:
interaktywny, konstruktywny, aktywny, pasywny, uporządkowane malejąco (I > C > A > P).
Sam suwak to tryb **aktywny**: uczeń manipuluje materiałem. Pytanie, na które musi
odpowiedzieć przed ruszeniem suwaka, przesuwa go do trybu **konstruktywnego**, a największy
przyrost wyników leży właśnie na granicy aktywny do konstruktywnego.

⚠️ **Uczciwie:** założenia ICAP są kwestionowane. Krytycy podważają zarówno to, że te tryby
da się rozpoznać z zewnątrz, jak i samą hierarchię. Traktuj to jako heurystykę projektową,
nie jako prawo. Ale to jest twardsze uzasadnienie fazy „Przewiduj" niż przeczucie, więc nie
wycinaj jej jako zbędnej.

### 2. Obserwuj

**Dokładnie jedna ruszana wielkość**, i to ta, która odsłania mechanizm, a nie ta, o którą
pyta zadanie. Wzorzec z zad. 8 arkusza 2026-maj: suwak rusza \(x\), a nie parametrem \(m\),
bo sednem jest „nawias się zeruje, więc iloczyn jest zerem". Suwak na \(m\) pokazywałby skutek.

Pod płótnem idzie **rachunek, nie wyrok**: podstawienie bieżącej wartości do wzoru z zadania,
linijka po linijce, a na końcu ✓ albo ✗. To wielkość ruszana przez ucznia dostaje kolor
niewiadomej, reszta zostaje czarna.

**Pokaż też, co się NIE zmienia.** Uczeń widzi, co się rusza, ale sensu uczy dopiero kontrast
z tym, co zostaje stałe. Przy zmianie \(a\) w paraboli zmienia się rozwarcie, a miejsca zerowe
zostają. Bez wskazania takiego niezmiennika uczeń wynosi z widżetu wniosek „wszystko zależy
od wszystkiego", czyli gorszy niż żaden.

W dokumencie projektowym wypisz to wprost dwiema listami: **co się zmienia** i **co zostaje**.

### 3. Rozstrzygnij

Jawne domknięcie: „dlatego właśnie…". Nigdy nie zostawiaj ucznia z samym „popatrz i pomyśl".
Nierozwiązane zdziwienie kończy się zamknięciem karty, a najbardziej prawdopodobny moment
dezorientacji to właśnie faza obserwacji.

**Obalenie musi być natychmiastowe, a błędna wersja nigdy nie jest stanem końcowym.**
Dwie twarde konsekwencje:

- **Stan startowy widżetu po załadowaniu jest poprawny albo neutralny, nigdy błędny.**
- **Uczeń, który zamknie kartę w losowym momencie, ma zapamiętać wersję poprawną.**

Skoro to jedyne miejsce z błędną drogą, ryzyko utrwalenia błędu jest realne, więc nie ma tu
miejsca na „uczeń sam dojdzie".

---

## Krótka lista kontrolna projektu widżetu

1. Jakie jest sedno zadania i **jaki błąd** popełnia uczeń, który go nie widzi?
2. Co uczeń **rusza** i dlaczego akurat to odsłania przyczynę, a nie skutek?
3. Jakie jest pytanie przewidujące, zadane **przed** ruchem?
4. Co się zmienia, a co zostaje stałe?
5. Jak brzmi zdanie domykające?
6. Czy widok bez interakcji broni się sam, czyli czy tytuł mówi, **co zrobić**?

Jeśli nie umiesz odpowiedzieć na punkt 1 albo 2, to zadanie prawdopodobnie nie nadaje się
na widżet. Powiedz to wprost i uzasadnij, zamiast projektować widżet, w którym nie ma
czego oglądać.
