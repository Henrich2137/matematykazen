# Brief dla Fable — arkusz 2024-grudzień

Materiał przygotowawczy zebrany 2026-08-15 przez Opusa, żeby sesja Fable'a nie
poszła na ustalanie rzeczy, które już są ustalone. **Zacznij od tego pliku** —
zawiera stan faktyczny, cztery pułapki i to, co jeszcze wymaga decyzji Henricha.

Zadanie z TODO.md (linie 108–110): `matura/2024-grudzień` → interaktywne
rozwiązania + sprawdzanie obliczeń (checkboxy).

---

## 1. Stan faktyczny — co arkusz już ma

Policzone z `exercises.json`, nie z pamięci. Arkusz ma **30 zadań CKE**
w **35 pozycjach** tablicy.

| Element | Stan |
|---|---|
| Podpowiedzi (`hint`) | ✅ **komplet** — wszystkie 33 pozycje merytoryczne |
| Rozwiązanie opisowe (`solutionText`) | ✅ **komplet** (poza zad. 1 i 2) |
| Checkboxy sprawdzania (`gradingCriteria`) | ✅ **komplet** — wszystkie 8 zadań otwartych |
| Rozwiązanie krok po kroku | ❌ **tylko zad. 1–9** (9 z 30) |
| Widżet interaktywny | ❌ **9 sztuk** (zad. 1, 5, 9, 10, 12.1, 15, 18, 20, 30) |
| Rozwinięcie (`solutionTextMore`) | 🟨 zad. 1–9 oraz 19 i 30 |

### ⚠️ Punkt „Sprawdzanie obliczeń (checkboxy)" jest już ZROBIONY

Wszystkie osiem zadań otwartych (3, 8, 9, 19, 26, 28, 30 oraz rodzice 12 i 17,
które kryteriów nie potrzebują) ma komplet `gradingCriteria`, i to spójny:
**liczba kryteriów = `maxScore` zadania**. Zad. 19 ma 4 pkt i 4 kryteria, zad. 8
ma 3 pkt i 3 kryteria, i tak dalej.

Nie ma tu czego uzupełniać. Zanim cokolwiek dopiszesz, potwierdź to z Henrichem —
możliwe, że chodziło mu o arkusz **2026-maj** (patrz niżej) albo o poprawienie
brzmienia istniejących kryteriów, a nie o dodanie brakujących.

### Prawdziwa luka to arkusz 2026-maj

Ma **41 pozycji i jest prawie pusty**: zero podpowiedzi, zero rozwiązań
opisowych, zero kroków, zero widżetów. Jedyne, co ma, to `gradingCriteria`
dla zadań otwartych. Jeśli szukasz roboty o największym efekcie, jest ona tam,
nie w 2024-grudniu.

---

## 2. Cztery pułapki

### Pułapka 1: numer zadania ≠ pozycja w tablicy

`exercises.json` **nie ma pola z numerem zadania.** Numer siedzi wyłącznie
w treści pola `question` („Zadanie 15."). Tablica ma więcej pozycji niż arkusz
ma zadań, bo zadania wieloczęściowe mają wpis-rodzic i wpisy na części:

- zad. 12 zajmuje 4 pozycje: `12.`, `12.1`, `12.2`, `12.3`
- zad. 17 zajmuje 3 pozycje: `17.`, `17.1`, `17.2`

Skutek: `exercises[24]` to **zadanie 20**, nie 25. Liczenie po indeksie daje
ciche trafienie w cudze zadanie — Opus przejechał się na tym 2026-08-15
i wyciągnął z tego fałszywy wniosek o brakujących checkboxach.

**Numer czytaj z pola `question`.**

Wpisy-rodzice (`12.`, `17.`) mają `maxScore: 0` i puste wszystkie pola treści —
to czyste kontenery odwzorowujące strukturę arkusza. Nie wypełniaj ich.

### Pułapka 2: kroki tekstowe NIE działają

`ARCHITECTURE.md:59` opisuje krok jako `{ type: "video"|"image"|"text", … }`.
**To nieprawda.** `renderStep()` w [app/steps.js](../app/steps.js) (linie 88–109)
obsługuje wyłącznie `"video"` i `"image"`; dla `"text"` zwraca pusty string,
czyli pusty kadr.

W danych obu arkuszy jest 62 kroki i **wszystkie są filmami** — ani jednego
obrazka, ani jednego tekstu. Ta ścieżka nigdy nie była użyta.

Pole `text` kroku to co innego i **działa** — to opis w rozwijanym panelu pod
kadrem (`app/steps.js:316`). Ale sam kadr musi być filmem albo obrazkiem.

Wniosek: **nie da się dziś dodać rozwiązania krok po kroku bez pliku wideo lub
obrazka.** Odtwarzacz ma już gałąź na krok bez filmu (`steps.js:145-149`), więc
dorobienie typu `"text"` jest prawdopodobnie małą zmianą — ale to zmiana w kodzie
i wymaga zgody Henricha oraz testu `tools/test-krokow.js`.

### Pułapka 3: widżetów nie da się przełożyć

Jest ich dziewięć i **każdy ma liczby swojego zadania wpisane na sztywno**
(np. `widgetProcentSkladany` zna kwoty 60 000 i 67 925,76 zł z zadania 5).
Nie istnieje żaden uniwersalny.

Nowy temat = nowy plik w `widgets/` + wpis w `_registry.js` + tag `<script>`
w `template.html`. Pominięcie któregokolwiek z trzech kroków daje ciche „brak
widżetu", bez błędu w konsoli.

To jest **praca programistyczna**, nie wypełnianie danych — wyceniaj ją inaczej.
Spis wszystkich dziewięciu i dostępnych pomocników: [widgets/README.md](../widgets/README.md).

### Pułapka 4: serwer bez obsługi przewijania

`python3 -m http.server` **nie obsługuje żądań zakresowych**. Bez nich filmy się
nie przewijają i wygląda to na błąd w odtwarzaczu — raz już kogoś na to nabrało.

Używaj `node tools/serwer.js 8001`. Sprawdzian: `curl -s -o /dev/null -w "%{http_code}" -r 0-100 <plik.mp4>`
ma zwrócić **206**, nie 200.

Uwaga: **na porcie 8000 w tym kontenerze może już stać cudzy `python3 -m http.server`**
(tak było 2026-08-15). Nie ubijaj go — wystartuj swój na innym porcie.

---

## 3. Czego NIE czytać

Sesja idzie na tokeny, a repo ma kilka plików, które potrafią zjeść jej sporą
część bez pożytku:

- ❌ **`ARCHITECTURE.md` w całości** — akapity po 3 tys. znaków o wewnętrznej
  mechanice odtwarzacza wideo (podwójne buforowanie, tokeny podmiany, kolejka
  pobierania). Do wypełniania treści zadań to bezużyteczne. Czytaj punktowo.
- ❌ **cokolwiek w `done/`** — historia projektu, tylko gdy naprawdę czegoś szukasz
- ❌ **`tablica-wzorow.pdf`** — jest transkrypt tekstowy, patrz niżej
- ❌ **całe `exercises.json` naraz** (65 kB), jeśli pracujesz nad kilkoma zadaniami

**Wzory bierz z `tablica-wzorow-transkrypt/`**, zaczynając od jego `README.md` —
skorowidz mapuje treść zadania („nierówność wykładnicza", „pole trapezu") na
numer wzoru i sekcję, więc wczytujesz 300–800 tokenów zamiast całej tablicy.
Wzory są w tych samych nawiasach KaTeX-a co `exercises.json`, więc wklejają się
wprost — pamiętaj tylko o podwójnym backslashu w JSON-ie.

## 4. Subagenci

Henrich zostawił decyzję Tobie. Jedna rzecz do uwzględnienia: **subagent startuje
na zimno**, bez tej rozmowy i bez tego pliku. Jeśli każesz mu „przeczytać repo
i zrobić zadanie 14", przeczyta te same 40 tys. tokenów co Ty — i tak dla każdego
subagenta osobno. Oszczędność zamienia się wtedy w stratę.

Jeśli delegujesz, dawaj gotowy wyciąg: treść zadania, oficjalne rozwiązanie CKE
i wzorzec do naśladowania w treści zlecenia.

## 5. Zasady, o których łatwo zapomnieć

- Cała treść dla ucznia i **komentarze w kodzie po polsku**
- Matematyka w KaTeX-ie: `\( … \)` i `\[ … \]`, w JSON-ie z `\\`
- Opisy kroków mają własne zasady w [manimations/README.md](../manimations/README.md):
  krótkie linijki, wzory w osobnych wierszach, bez wstępów typu „zaczynamy od…",
  bez myślników i podkreśleń poza wzorami (czytają się jak minus)
- Jedna paczka zmian = **jeden commit**, z trailerem `Co-Authored-By: Local Fable 5 <Effort> <noreply@anthropic.com>`
- Rzeczy do sprawdzenia przez Henricha wpisz w **dwóch** miejscach: w czacie
  i w `TODO.md` w sekcji `TESTOWANIE HENRICH:`
- Jeśli zmiana jest widoczna na stronie — **podbij numer wersji w dwóch plikach
  naraz**: `#wersja` w `template.html` i `.landing-wersja` w `index.html`
- Zrzuty stanu strony sprzed Twoich zmian: [zrzuty/2026-08-15/](../zrzuty/2026-08-15/)

## 6. Otwarta decyzja Henricha

Ustalone przed sesją: **bez filmów** (żadnego Manima), **pilotaż na kilku
zadaniach**, nie na całym arkuszu.

Nierozstrzygnięte przez pułapkę 2 — skoro kroków tekstowych nie ma, to co robimy:

1. dorobić obsługę kroków tekstowych w `app/steps.js` (zmiana w kodzie), czy
2. zostać przy rozwiązaniach opisowych bez kroków, czy
3. robić kroki jako obrazki

**Nie wybieraj tego sam** — spytaj Henricha na starcie sesji.
