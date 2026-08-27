---
name: projektowanie-rozwiazan
description: >
  Użyj, gdy pada prośba o zaprojektowanie, napisanie, poprawienie albo
  uzupełnienie podpowiedzi, rozwiązania opisowego, filmu krok po kroku albo
  widżetu do zadania z arkusza CKE, także wtedy, gdy użytkownik nie użyje słowa
  „scenariusz" i po prostu poda numer zadania („zrób zadanie 14", „dopisz
  podpowiedź do 12.2", „to rozwiązanie jest za trudne"). Nie używaj do samego
  renderowania gotowej sceny Manim ani do kodowania widżetu, którego projekt
  już jest zatwierdzony.
---

# Projektowanie rozwiązań

Odbiorca to maturzysta celujący w około 30%, czyli w próg zdawalności. Nie matematyk.
Każdy dokument opisuje **co widzi i rozumie uczeń**, nie jak to zaimplementować.

**Wynik pracy tego skilla to dokument projektowy po polsku**, a nie kod i nie gotowy
wpis do `exercises.json`. Wzory zapisujesz w KaTeX (`\( … \)`), bo i tak tak pojadą
dalej, ale bez znaczników HTML, bez Pythona i bez JS. Kusi Cię kod, to znaczy, że opis
jest za mało konkretny: dopisz opis, nie kod.

**Proporcja uwagi: prawie cała idzie na dydaktykę, rachunek i ucznia.** Na technikalia tyle,
żeby nie zaprojektować czegoś, czego nie da się zrobić (ruch, którego Manim nie zrobi bez
walki, film z lektorem, widżet ruszający pięcioma rzeczami naraz) albo czegoś, co mocno
odstaje od tego, jak rozwiązania w tym projekcie wyglądają do tej pory. Reszta technikaliów
to nie Twój problem na tym etapie.

Wpisanie projektu do repozytorium to osobny krok i rządzą nim inne pliki:
[SOLUTION_TEXT_RULES.md](../../../SOLUTION_TEXT_RULES.md) (znaczniki `solutionText`),
[manimations/README.md](../../../manimations/README.md) (scena i render),
[widgets/PROJEKTOWANIE.md](../../../widgets/PROJEKTOWANIE.md) (widżet).

## 1. Najpierw materiał, dopiero potem projekt

**Nie projektuj z pamięci o „typowym zadaniu tego rodzaju".** Zadania CKE bywają
podchwytliwe w szczegółach, a numery w kluczu rzadko wyglądają tak, jak się spodziewasz.

| czego szukasz | gdzie to jest |
|---|---|
| treść zadania | `matura/<arkusz>/exercises.json`, pole `question`; oryginał w `arkusz.pdf` / `arkusz.txt` |
| poprawna odpowiedź i pełne zasady oceniania CKE | `matura/<arkusz>/odpowiedzi.pdf`, wyciąg tekstowy `odpowiedzi.txt` |
| kryteria punktowe już spisane (zadania otwarte) | pole `gradingCriteria` w `exercises.json` |
| wzory, które wolno położyć obok rachunku | `tablica-wzorow-transkrypt/`, zaczynając od `README.md` i jego skorowidza |
| wzorce rejestru i tempa | tabela wzorców w `SOLUTION_TEXT_RULES.md` (zad. 2, 3, 4, 6, 7, 8 z 2024-grudnia); filmy mają zad. 1 do 7 i 9 |
| jakie arkusze w ogóle istnieją | `matura/README.md` |

Dwie pułapki, które kosztowały czas:

- **Nie ma osobnego transkryptu zasad oceniania.** Zasady oceniania to `odpowiedzi.pdf`
  w katalogu arkusza, a `odpowiedzi.txt` jest ich maszynowym wyciągiem. Wyciąg dla
  `2024-grudzien` jest w kodowaniu cp1250 i **bez polskich ogonków**, więc czyta się go
  przez `iconv`, a i tak trzeba zweryfikować wątpliwe miejsca w PDF.
- **Policz zadanie sam od zera i porównaj z kluczem, zanim cokolwiek zaprojektujesz.**
  Struktura rozwiązania decyduje o liczbie kroków i o tym, co uczeń ma zobaczyć.
  Rozbieżność z kluczem = zatrzymaj się i zgłoś Henrichowi, nie naginaj wyniku.

## 2. Reguła nadrzędna: brak skoków

Najczęstsza wada rozwiązań pisanych przez model to *expert blind spot*: pomijanie kroków
wtopionych we własny skompresowany kawałek wiedzy. Ekspert zapytany, jak przeskoczył
z linijki na linijkę, jest szczerze zaskoczony, że cokolwiek pominął. Uczeń widzi w tym
miejscu magię i się wyłącza.

**Test na każdym przejściu: czy uczeń, który zna tylko wzór z tablic i podstawowe
działania, potrafi wskazać palcem, co się zmieniło i dlaczego?** Jeśli nie, rozbij krok.

Wzorzec rozbicia jest w `manimations/README.md`, punkt 17: jedynka z licznika ułamka nie
leci prosto do wykładnika, tylko najpierw pojawia się brakujące ogniwo (`5 = 5^1`),
a dopiero potem ruch.

## 3. Cztery artefakty

### Podpowiedź (pole `hint`)

Jeden poziom, 1 do 2 linijek, poziom „wskazujący": na jaki wzór spojrzeć, od czego zacząć
i z grubsza jak.

**Próg:** jeśli po przeczytaniu podpowiedzi da się przepisać pierwszy rachunek bez
myślenia, jest za mocna. Podpowiedź to rusztowanie, nie skrót do odpowiedzi.

### Rozwiązanie opisowe (pole `solutionText`)

- Prostsze i bardziej zrozumiałe niż zasady oceniania. Uczeń klucz ma i tak obok.
- **Ale samo w sobie musi zdobyć komplet punktów.** Przed oddaniem przejdź po kryteriach
  z `odpowiedzi.pdf` (albo z `gradingCriteria`) i sprawdź, że każde jest pokryte.
- Ta sama ziarnistość co w filmie: jedna linijka = jedno przekształcenie.
- **Tyle linijek, ile kroków filmu.** Zmieniasz jedno, projektujesz drugie od nowa.
- Trzy techniki tekstowe, które realnie podnoszą zrozumiałość:
  [references/zasady-tekstowe.md](references/zasady-tekstowe.md).

### Film krok po kroku (pole `solutionStepByStep`)

- **Jeden krok = jedno przekształcenie algebraiczne.** Nie dwa naraz, nawet jeśli „to oczywiste".
  Krok **może** za to pokazać po drodze, skąd to przekształcenie się bierze, i dopiero potem
  zostawić w kadrze czystą linijkę (Henrich, 2026-08-27; wzorzec i warunki:
  [references/zasady-wizualne.md](references/zasady-wizualne.md), punkt 2b).
- **Animacja musi być zrozumiała bez czytania opisu.** Opis pod filmem jest domyślnie
  zwinięty i większość uczniów go nie rozwinie, więc cały ciężar niesie ruch, kolor
  i pozycja. Opis to bonus, nie proteza.
- **Filmy nie mają lektora.** Tekst w kadrze i pod kadrem to jedyny kanał werbalny.
  Nie projektuj niczego, co zakłada narrację.
- **Wyróżniaj tylko to, co się w tym kroku zmienia.** Trzy podświetlenia naraz i uczeń
  nie wie, gdzie patrzeć. Domyślnie nie kolorujesz nic, patrz `COLORS.md`.
- **Żadnych ozdobników, które nie niosą matematyki.**
- **Etykiety podcelów** („wyznaczamy dziedzinę") tylko przy zmianie fazy rozwiązania,
  nie przy każdym kroku.
- Format kroku w dokumencie: *stan przed → co dokładnie się rusza, zmienia albo znika →
  stan po → (opcjonalnie) jedno zdanie opisu.*
- Jak ruch ma się mieć do rachunku i co zrobić z tym, że obraz przemija:
  [references/zasady-wizualne.md](references/zasady-wizualne.md).

### Widżet (pole `solutionWidget`)

**Projektuj tylko na wyraźne polecenie.** Domyślnie widżetu nie ma.

Nadają się zadania z czymś obserwowalnym: funkcje, geometria, zależność parametr do wyniku.
Nie nadają się przekształcenia algebraiczne i rozwiązywanie równań, bo nie ma tam czego
oglądać. Wolno Ci odmówić i uzasadnić.

Schemat Przewiduj, Obserwuj, Rozstrzygnij oraz to, dlaczego pytanie przed suwakiem nie
jest ozdobnikiem: [references/poe-wzorzec.md](references/poe-wzorzec.md).
Mechanika, spójność i lista uwag Henricha: `widgets/PROJEKTOWANIE.md`.

## 4. Zasady domowe wygrywają

Ten skill mówi, **co** uczeń ma zobaczyć. O tym, **jak** to zapisać, rozstrzygają pliki
projektu i w razie sprzeczności to one mają rację: `SOLUTION_TEXT_RULES.md`,
`manimations/README.md`, `COLORS.md`, `widgets/PROJEKTOWANIE.md`.

Trzy miejsca, w których łatwo zaprojektować coś, czego repozytorium nie przyjmie:

- **Wzór w ramce obok linijki albo pod filmem tylko wtedy, gdy stoi w tablicy wzorów.**
  Reszta idzie zwykłym zdaniem z przykładem na liczbach. Uczeń nie ma szukać w tablicy
  czegoś, czego tam nie ma.
- **Zieleń w rozwiązaniu i w filmie nie znaczy „dobrze"**, tylko „tu patrz". Poprawność
  ma osobny token.
- **Bez myślników i półpauz** w tekstach dla ucznia. W opisach kroków pod filmem zakaz
  jest ostrzejszy: żadnych `-` ani `_` poza wzorami, bo czytają się jak minus.

## 5. Typowe błędy: wybierz 0 do 2

[references/typowe-bledy.md](references/typowe-bledy.md) to lista pułapek ze sprawozdań CKE
2024 i 2025, w pięciu grupach, każda z tagiem artefaktu, w którym rozbraja się najlepiej.
Wybierz **najwyżej dwie**, które grożą w tym konkretnym zadaniu, i wpleć je **w ten krok,
w którym grożą**. Nie doklejaj listy ostrzeżeń na końcu, bo nikt jej nie czyta.

**Nie pisz „uczniowie często mylą…".** Zamiast ostrzeżenia zaprojektuj krok tak, żeby pomyłka
była widoczna: rozbij przekształcenie na dwa, zaznacz to, co zmienia znak, dopisz ogniwo.

**Błędną drogę wolno pokazać tylko w widżecie** i tylko po to, żeby ją na miejscu obalić.
W filmie i w rozwiązaniu opisowym pokazujesz wyłącznie poprawny tok.

## 6. Weryfikacja przed oddaniem

1. Wynik zgodny z kluczem CKE. Rozbieżność = stop i pytanie, nie naginanie.
2. Każde kryterium z zasad oceniania pokryte (dotyczy rozwiązań opisowych).
3. Żadne przejście nie przeskakuje więcej niż jednego przekształcenia.
4. Liczba linijek rozwiązania opisowego = liczba kroków filmu.
5. W każdym kroku wyróżnione jest najwyżej jedno miejsce.
6. Zero kodu w dokumencie, zero myślników w tekstach dla ucznia.
7. Napisane wprost, czego **nie** dało się ustalić. „Nie ustalono" jest pełnoprawnym
   wynikiem i nie wolno go podmieniać na wyjaśnienie, które brzmi sensownie.
