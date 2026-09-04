# Projekt rozwiązań: zad. 22 i 23 (2024-grudzień)

Dokument projektowy w rozumieniu skilla `projektowanie-rozwiazan`: co ma zobaczyć uczeń.
Powstał 2026-09-04, w sesji chmurowej (bez Henricha na żywo) - decyzje niżej są moje,
nie jego, i tam gdzie było więcej niż jedna rozsądna opcja, zapisuję dlaczego wybrałem tę,
a nie inną, żeby dało się to podważyć przy przeglądzie.

Zakres z TODO.md: oba zadania mają już **rozwiązanie zwykłe** (gotowe wcześniej) i **hint**.
Brakuje wyłącznie **filmu krok po kroku**. Ten dokument projektuje tylko film; solutionText
się nie zmienia.

## Materiał

| co | zad. 22 | zad. 23 |
|---|---|---|
| treść | prosta \(k\colon y=-7x+3\), prosta \(l \parallel k\) przez \((0,6)\), punkt \((1,p)\) na \(l\) | cztery okręgi \(o_1..o_4\), szukamy tego bez punktu wspólnego z osiami |
| klucz CKE | B, 1 pkt | C, 1 pkt |
| formulasPage | 24 | 24 |
| wzór | proste równoległe \(a_1=a_2\) [11.8] | równanie okręgu \((x-a)^2+(y-b)^2=r^2\) [11.11] |

Warunek użyty w zad. 23 (\(|a|>r\) i \(|b|>r\) ⟺ okrąg nie ma punktu wspólnego z żadną osią)
**nie stoi w tablicy jako gotowy wzór** - to wniosek z odległości środka od osi versus promień.
Dlatego w filmie idzie zwykłym zdaniem, nie w ramce (zasada 3 „krok po kroku, wersja krótka").

Policzone od zera, zgodne z solutionText i kluczem:

- zad. 22: \(l\colon y=-7x+6\) (ten sam współczynnik kierunkowy co \(k\), wyraz wolny z punktu
  \((0,6)\)), \(p = -7\cdot 1+6=-1\).
- zad. 23: \(o_1\) ma \(S=(1,2)\), \(r=1\): \(|a|=1=r\) (styczny do \(Oy\), nie mniejszy).
  \(o_2\) ma \(S=(-1,-2)\), \(r=3\): \(|a|=1<3\) i \(|b|=2<3\) (przecina obie osie).
  \(o_3\) ma \(S=(3,4)\), \(r=2\): \(|a|=3>2\) i \(|b|=4>2\) (nie dotyka żadnej), **odpowiedź**.
  \(o_4\) ma \(S=(-3,-4)\), \(r=4\): \(|a|=3<4\) (przecina \(Oy\)), \(|b|=4=4\) (styczny do \(Ox\)).

## Zad. 22: film

Zadanie jest krótkie (solutionText to dwie linijki rachunku), więc film jest krótki, bez
podziału na dwa pasy: **jedna kolumna po prawej + wykres po lewej**, wzorem zad. 21.

Układ kadru: lewa połowa - układ współrzędnych z prostą \(k\) (szara, referencyjna, bo to
tylko dana wyjściowa, nie coś co liczymy) i budowaną prostą \(l\); prawa połowa - pas
odczytu/reguły na górze, rachunek na środku, odpowiedź na dole.

Kroki (5 z nich to linijki solutionText, dwa pierwsze to czysto rysunkowe „jedna myśl",
zasada 42):

1. **Rysunek.** Wjeżdża układ współrzędnych, prosta \(k\colon y=-7x+3\) (szara, bo dana, nie
   wynik), punkt \((0,6)\) zaznaczony na \(Oy\). Cały czarny/szary, nic się nie liczy.
2. **Prosta \(l\) jest równoległa: taki sam współczynnik kierunkowy.** Zdanie „proste
   równoległe mają ten sam współczynnik kierunkowy" (z [11.8], ale to zdanie z tablicy, nie
   wzór, więc bez ramki) plus \(a_1=a_2\) w ramce (to JEST wzór z tablicy). Prosta \(l\)
   rysuje się przez \((0,6)\) z tym samym nachyleniem co \(k\) (czarna, bo to już nie dana
   z treści, tylko to, co rysujemy dalej).
3. \(l\colon y = -7x + 6\) (współczynnik \(-7\) przylatuje z \(k\), \(6\) przylatuje z punktu
   na rysunku - README, punkt 37: liczba nigdy nie pojawia się znikąd).
4. Na rysunku pojawia się punkt \((1, p)\) na prostej \(l\) (czarna kropka, współrzędna \(p\)
   nieznana - podpis „\(p\)" bez liczby). Podstawienie \(x=1\): \(p = -7\cdot 1 + 6\).
5. \(p = -7+6\)
6. \(p = \boldsymbol{-1}\), kropka na rysunku dostaje wynik jako podpis, odpowiedź **B**.

Pułapka ze sprawozdań CKE, którą rozbrajamy: wzięcie \(b\) z \(k\) zamiast z \(l\) (dystraktor
z użyciem \(3\) zamiast \(6\)). Rozbrajamy ją tym, że \(6\) na rysunku jest osobnym, wyraźnie
zaznaczonym punktem, a wyraz wolny \(k\)-a (\(3\)) w ogóle nie wchodzi do rachunku po kroku 1.

## Zad. 23: film

To zadanie **sprawdza**, nie liczy jedną ścieżką - cztery okręgi, dla każdego то samo pytanie.
Wzorem zad. 10/11 (zasada 42: „jednostką kroku jest jedna myśl"), **jeden okrąg = jeden krok**,
a nie jeden krok na każde z dwóch porównań (\(|a|\) i \(|b|\)) w środku.

Układ kadru: lewa połowa - jeden wspólny układ współrzędnych z wszystkimi czterema okręgami
narysowanymi od pierwszego kroku (uczeń widzi całą sytuację, zanim zaczniemy sprawdzać, tak
jak patrzyłby na treść zadania); prawa połowa - u góry reguła (zostaje przez cały film), na
środku pas sprawdzania bieżącego okręgu, na dole odpowiedź.

Reguła (krok 1, zdanie, nie wzór z ramki, bo nie stoi tak w tablicy):
„Okrąg o środku \((a,b)\) i promieniu \(r\) nie ma punktu wspólnego z żadną osią, gdy
\(|a|>r\) **i** \(|b|>r\)."

Kroki:

1. **Rysunek i reguła.** Wjeżdża układ współrzędnych z czterema okręgami (czarne, cienkie,
   podpisane \(o_1\)-\(o_4\) przy obwodzie) i zdanie reguły po prawej. Cały krok czarny/szary.
2. **Sprawdzamy \(o_1\).** Podświetla się na zielono, obok wjeżdżają jego dane
   \(S=(1,2)\), \(r=1\) (przywołane z podpisu przy okręgu, README punkt 37). Porównanie
   \(|a|=1\) vs \(r=1\): równe, nie większe, więc \(o_1\) **dotyka** \(Oy\) (widać to też na
   rysunku - okrąg styka się z osią \(Oy\) w jednym punkcie). Krok kończy się zgaszeniem
   \(o_1\) z powrotem na czarno (odpada z rozważań, ale zostaje na rysunku dla kontekstu).
3. **Sprawdzamy \(o_2\).** Ten sam wzorzec: \(S=(-1,-2)\), \(r=3\). \(|a|=1<3\) i \(|b|=2<3\),
   czyli \(o_2\) **przecina obie osie** (widoczne na rysunku - okrąg wystaje poza obie).
   Gaśnie na czarno.
4. **Sprawdzamy \(o_3\).** \(S=(3,4)\), \(r=2\). \(|a|=3>2\) i \(|b|=4>2\) - **żadnego punktu
   wspólnego**. Ten okrąg **zostaje zielony** (nie gaśnie - to kandydat na odpowiedź).
5. **Sprawdzamy \(o_4\).** \(S=(-3,-4)\), \(r=4\). \(|a|=3<4\) (przecina \(Oy\)) i \(|b|=4=4\)
   (styka \(Ox\)) - ma punkty wspólne. Gaśnie na czarno. \(o_3\) cały czas zielony w tle.
6. **Odpowiedź.** \(o_3\) zostaje jedynym zielonym okręgiem na rysunku, obok wjeżdża
   „Odpowiedź C".

Sześć kroków, solutionText się nie zmienia (jest zwarty, opisowy, nie linijka-do-linijki -
świadomy rozjazd, bo forma „sprawdź czworo po kolei" nie da się skrócić do jednej ścieżki
rachunku bez utraty czytelności, zasada z 2026-08-30).

## Czego nie ustalono

- Czy cztery okręgi na jednym wykresie (zad. 23) nie robią się za drobne na telefonie -
  promienie 1 do 4 w jednym kadrze 5,4 jednostki to spory rozrzut skali. Do sprawdzenia po
  renderze (`tools/klatki.sh stany`) i do `TODO.md`, `TESTOWANIE HENRICH`, jeśli klatki
  wyglądają dobrze na komputerze, ale wątpliwe na wąskim ekranie.
- Rendering zrobiony w tej sesji **poza standardowym devkontenerem** (opisanym w
  `manimations/README.md`) - środowisko chmurowe nie ma dostępu do obrazu kontenera, więc
  Manim i TeX Live zostały zainstalowane doraźnie z Ubuntu 24.04 (`apt-get`), nie z Debiana
  z Dockerfile. Wersje mogą się różnić od tych przypiętych w `.devcontainer/Dockerfile`.
  Zrobiony w README (2026-08-11) test host↔kontener pokazał, że różnice wersji TeX
  Live/ffmpeg dają SSIM rzędu 0,9995+ (szum kodera), więc ryzyko widocznej różnicy jest
  niskie, ale **nie jest to ten sam, zweryfikowany pipeline** - warto to wiedzieć, gdyby
  coś w tych dwóch filmach wyglądało nietypowo.
