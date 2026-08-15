# Brief dla Fable — arkusz 2026-maj

Przygotowane 2026-08-15 przez Opusa. **Przeczytaj to zamiast zwiedzania repo.**

## Zadanie

Pilotaż na **trzech zadaniach** z `matura/2026-maj`. Dla każdego:

1. **podpowiedź** (`hint`) i **rozwiązanie opisowe** (`solutionText`) — arkusz nie ma ani jednego
2. ** Zwykłe rozwiązanie **
3. **widżet interaktywny** — nowy plik w `widgets/`, jeśli zadanie się do tego nadaje
4. Na razie jeszcze nie: **scenariusz filmu Manima** — tekst sceny, **bez renderowania**

Zadania (wybór Henricha):

- zad 2. - Interaktywne/widżet: Podobnie jak zad 5. w 2024-grudzien
- zad 8. - Interaktywne/widżet: Zmienianie x suwakiem zmienia:
  - liczbę na miejscu x w równaniu
  - punkt na osi liczbowej na której są oznaczone wszystkie 3 rozwiązania oznaczone tym samym kolorem co literki w równaniu
- zad 10. - Interaktywne/widżet: po uproszczeniu do 
postać ogólna >= 0
zrobić podobnie jak w zad 9. w 2024-grudzien

**Nie rozszerzaj zakresu sam**, nawet gdy zostanie budżet. Znalazłeś coś do poprawy poza zakresem → wpis do `TODO.md`, nie poprawka.

## ⛔ STOP po pierwszym zadaniu

Zrób **jedno** zadanie w komplecie, potem **zatrzymaj się i oddaj do testów.**
Nie rób pozostałych dwóch, dopóki Henrich nie potwierdzi. Chodzi o to, żeby
rozjazd stylu wyszedł po jednym zadaniu, a nie po trzech.

Oddając, napisz w **dwóch** miejscach — w czacie i w `TODO.md` w sekcji
`TESTOWANIE HENRICH:` - konkretne polecenia: co kliknąć i czego szukać.

**Muszą tam być te punkty, bo sam ich nie sprawdzisz:**

- **Widżet na telefonie, palcem.** Czy da się trafić w przeciągany punkt i czy nie
  ucieka poza ekran przy 390 px. Playwright klika myszą — to nie to samo co palec.
- **Przełączenie motywu przy otwartym widżecie.** Czy przemalowuje się od razu, czy
  zostaje w kolorach poprzedniego (typowy objaw braku `wgZarejestrujRysowanie`).
- **Czy podpowiedź faktycznie pomaga, a nie zdradza.** To ocena nauczyciela, nie modelu.
- JESZCZE NIE: **Czy scenariusz filmu da się obejrzeć w głowie** — czy kolejność kroków jest ta, którą
  uczeń sam by przeszedł.
- **Cokolwiek, co zmieniłeś w kodzie** - wymień z nazwy, osobno.

Podbij numer wersji **w dwóch plikach naraz**: `#wersja` w `template.html`
i `.landing-wersja` w `index.html`. Bez tego Henrich ogląda starą stronę i szuka
nieistniejącego błędu.

## Stan arkusza

**41 pozycji w tablicy, ~33 zadania CKE. Prawie pusty:** zero podpowiedzi, zero rozwiązań
opisowych, zero kroków, zero widżetów. Jedyne, co jest, to `gradingCriteria`
przy zadaniach otwartych. Cokolwiek dodasz, będzie pierwsze.

Dla porównania `matura/2024-grudzien` ma komplet podpowiedzi i rozwiązań oraz
9 widżetów i 9 rozwiązań krok po kroku — **stamtąd bierz wzorzec**, nie wymyślaj stylu.

## Cztery pułapki

**1. Numer zadania ≠ pozycja w tablicy.** W `exercises.json` nie ma pola z numerem —
siedzi tylko w treści `question` („Zadanie 15."). Zadania wieloczęściowe mają wpis-rodzic
(`maxScore: 0`, puste pola, **nie wypełniaj go**) i osobne wpisy na części: `12.`, `12.1`,
`12.2`. **Numer czytaj z `question`.** Opus przejechał się na tym i wyciągnął fałszywy wniosek.

**2. Kroki typu `"text"` NIE działają.** `ARCHITECTURE.md:59` wymienia
`"video"|"image"|"text"`, ale `renderStep()` w `app/steps.js:88-109` obsługuje tylko dwa
pierwsze — `"text"` daje pusty kadr. Wszystkie 62 istniejące kroki to filmy.
**Dlatego kroki w tym pilotażu są scenariuszami, nie danymi.** Pole `text` kroku to co
innego i działa — to opis pod kadrem.

**3. Widżetu nie da się przełożyć.** Każdy z dziewięciu ma liczby swojego zadania wpisane
na sztywno. Nowy temat = **nowy plik + wpis w `widgets/_registry.js` + tag `<script>`
w `template.html`**. Pominięcie któregokolwiek z trzech daje ciche „brak widżetu", bez
błędu w konsoli. Spis i pomocniki: [widgets/README.md](../widgets/README.md).

**4. `python3 -m http.server` nie przewija filmów** (brak obsługi żądań zakresowych) —
wygląda to na błąd odtwarzacza. Używaj `node tools/serwer.js 8001`; `curl -r 0-100` na
plik `.mp4` ma zwrócić **206**. Na porcie 8000 może już stać cudzy serwer — nie ubijaj go.

## Oszczędzanie kontekstu

- ❌ **Nie czytaj `ARCHITECTURE.md` w całości** — akapity po 3 tys. znaków o wewnętrznej mechanice odtwarzacza. Do treści zadań bezużyteczne, **i miejscami nieprawdziwe**
  (patrz pułapka 2). Gdy stawka jest wysoka, czytaj kod, nie opis kodu.
- ❌ **Nie czytaj `done/`** ani `tablica-wzorow.pdf`.
- ✅ **Wzory z `tablica-wzorow-transkrypt/`**, przez skorowidz w jego `README.md` — mapuje
  treść zadania na numer wzoru, więc wczytujesz 300–800 tokenów zamiast całej tablicy.
  Te same nawiasy KaTeX co `exercises.json`; w JSON-ie pamiętaj o `\\`.
- ✅ **Oficjalne rozwiązania: `matura/2026-maj/odpowiedzi.txt`** (95 kB po wyrównaniu
  2026-08-15). Sekcje „Uwagi:" pod zasadami oceniania to gotowy materiał na kryteria.
  **Nie jest w UTF-8 w każdym arkuszu** — 2024-grudzień to cp1250.
- ✅ `2026-maj/exercises.json` ma 34 kB — można czytać w całości, wyciąg to zbędna robota.
- **Subagenci — Twoja decyzja**, ale subagent startuje **na zimno**: bez tej rozmowy i bez
  tego pliku. Każesz mu „przeczytać repo" → przeczyta te same dziesiątki tysięcy tokenów,
  i tak dla każdego osobno. Delegujesz — dawaj gotowy wyciąg w treści zlecenia.

## Bez pytania nie ruszaj

- **`app/steps.js` i reszty odtwarzacza** — delikatne, ma własny test `tools/test-krokow.js`
- **renderowania Manima** — scenariusze tak, produkcja plików nie
- **rozszerzania zakresu** poza trzy zadania
- **wątpliwości merytorycznej w matematyce** — Henrich jest nauczycielem matematyki,
  pytaj jego zamiast zgadywać

Nowy widżet **jest** w zakresie, mimo że to kod — o to w pilotażu chodzi.

## Drobiazgi, o które łatwo się potknąć

- Treść dla ucznia **i komentarze w kodzie po polsku**
- Matematyka w KaTeX: `\( … \)` i `\[ … \]`, w JSON-ie z `\\`
- Opisy kroków mają własne zasady w [manimations/README.md](../manimations/README.md) —
  przeczytaj **przed** pisaniem scenariusza: ostatnia klatka kroku = pierwsza klatka
  następnego, ruch ma iść za rachunkiem, kolor tylko na tym, na co uczeń ma patrzeć;
  w opisie krótkie linijki, wzory osobno, bez myślników i podkreśleń poza wzorami
- Jedna paczka zmian = **jeden commit**, trailer
  `Co-Authored-By: Local Fable 5 <Effort> <noreply@anthropic.com>`
- Zrzuty stanu strony sprzed Twoich zmian: [zrzuty/2026-08-15/](../zrzuty/2026-08-15/)
