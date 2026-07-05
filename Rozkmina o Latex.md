# Manim (video) vs. JS+LaTeX dla `solutionStepByStep` — porównanie i rekomendacja

## Context

Henrich zastanawia się, czy animacje krok-po-kroku renderowane w **Manim** (eksportowane do `.mp4`) mają sens, czy dałoby się to zrobić stosunkowo łatwo w **JS pod warunkiem działającego LaTeX-a**. To pytanie decyzyjne/architektoniczne — celem jest porównanie obu podejść, żeby zdecydować kierunek zanim powstanie reszta z ~30 zadań.

### Stan faktyczny (zweryfikowany w repo)

- **Brak renderera LaTeX** na stronie dziś. Matematyka jest budowana ręcznie: znaki Unicode (⁵√5, ⅕, ≤), `<sup>/<sub>`, spany `.mathText`.
- **Tylko 3 z 30 zadań** mają `solutionStepByStep` (zad 1, 2, 3) — wszystkie wideo. Razem **23 pliki `.mp4`, ~880 KB** (~38 KB/plik).
- Schemat kroku **już wspiera `type: "video" | "image" | "text"`** — mieszane typy w jednej tablicy są dozwolone z założenia.
- Repo **już ma własny system animacji JS**: funkcje `widget*`, `wgCanvas`, `wgStrzalka`, `wgDraggable`, paleta `WG_KOLORY` — czyli animowana matematyka w JS jest zgodna z istniejącym ziarnem projektu, nie jest nowym paradygmatem.
- Znana tarcia są **specyficzne dla wideo**: zablokowana literówka `5⁻⁴`/`5⁴` w `zad2/...step6.mp4` (wymaga pełnego re-renderu Manim), oraz skakanie nawigacji przy różnej długości podpisów (opisane w CLAUDE.md).

---

## Porównanie

| Kryterium | Manim → `.mp4` (obecne) | JS + LaTeX (KaTeX) |
|---|---|---|
| **Jakość wizualna animacji** | Najwyższa. Prawdziwe „morphowanie" równań (`TransformMatchingTex`) — trudne do dorównania w JS. | Dobra przy fade/highlight/kolorowaniu członów; **prawdziwy morph jest trudny** i pracochłonny. |
| **Nakład na 1 zadanie** | Wysoki: skrypt Pythona → render → eksport → wrzucenie ~8 plików do `zadN/`. Skala: 30 zadań × ~8 kroków ≈ **~240 wideo** do wyprodukowania i utrzymania. | Niski po zbudowaniu odtwarzacza: krok = **string LaTeX w `exercises.js`**. Dodanie/edycja = edycja danych. |
| **Edytowalność / poprawki** | Bardzo słaba. Literówka = pełny re-render w zewnętrznym toolchainie (dowód: `5⁴` tkwi błędny do dziś). | Trywialna. Poprawka = edycja tekstu, natychmiast widoczna. |
| **Zależności** | Zewnętrzny Python/Manim poza repo; brak zależności runtime (wideo gra wszędzie). | Dodaje KaTeX — **trzeba zvendorować lokalnie** (`katex.min.js` + `.css` + folder fontów), bo nie ma builda. Jednorazowo kilkaset KB, działa offline/`file://`. |
| **Rozmiar / repo** | Binarne `.mp4` puchną repo z każdym zadaniem. | Brak binariów; treść to tekst w pliku danych (zgodne z planem migracji do `exercises.json`). |
| **Dostępność / UX** | Matematyka to piksele: nie zaznaczysz, nie skopiujesz, nie przeszuka wyszukiwarka; brak reflow na wąskich ekranach. | Tekst selektowalny/kopiowalny, dostępny, responsywny (reflow). |
| **Interaktywność** | Brak — nagranie liniowe. | Możliwa (zgodna z `solutionInteractive`/widgetami). |
| **Layout nawigacji** | Podpisy różnej długości → skakanie nav (już łatane `min-height`). | Ten sam problem podpisu, ale wysokość kroku kontrolowana w DOM. |
| **Player (pause/progress/replay)** | Zbudowany ręcznie wokół `<video>` w `renderStep`/`showStep`. | Trzeba zbudować odpowiednik (prev/next już jest; animacja przez CSS/anime.js). |

### Wniosek z porównania
Na etapie **demo/MVP, jeden autor, 3/30 zadań pokryte, a pipeline wideo już generuje tarcie** (zablokowana literówka, skakanie), koszt skalowania Manima do ~240 wideo jest nieproporcjonalny do zysku wizualnego. JS+LaTeX wygrywa na **edytowalności, skali, rozmiarze repo, dostępności** i jest zgodny z istniejącym systemem widgetów. Manim wygrywa tylko tam, gdzie **prawdziwa animacja wnosi realną wartość** (geometria, dynamiczne wykresy, morphy) — a takich kroków jest mało.

---

## Rekomendacja: hybryda przez nowy typ kroku `type: "math"`

Nie wyrzucać Manima — **rozszerzyć** istniejący, już-wieloтyповy schemat kroków o typ LaTeX. Schemat `{ type: "video"|"image"|"text", ... }` już to zaprasza; dodajemy `type: "math"` (albo `"latex"`) i pozwalamy mieszać kroki w jednej tablicy. Domyślnie kroki są LaTeX-owe (tanie, edytowalne); wideo zostaje dla nielicznych kroków, gdzie animacja jest tego warta.

To daje: tanie skalowanie na 30 zadań, natychmiastowe poprawki (w tym `5⁴`), dostępność — przy zachowaniu opcji Manim tam, gdzie ma sens, i bez łamania obecnych zad 1–3.

---

## Zakres wdrożenia (proponowany PoC, potem rollout)

Pliki dotknięte: [matematykazen.html](matematykazen.html) (inline `<script>` + `<head>`), [exercises.js](exercises.js), [style.css](style.css); nowy katalog `vendor/katex/`.

1. **Zvendorować KaTeX lokalnie** (`vendor/katex/katex.min.js`, `katex.min.css`, `fonts/`) i dołączyć w `<head>` [matematykazen.html](matematykazen.html) przez lokalne `<link>`/`<script>` (bez CDN — strona ma działać z `file://`/offline, jak PDF wzorów).
2. **Rozszerzyć `renderStep()`** (inline w [matematykazen.html](matematykazen.html)) o gałąź `type === "math"`: wstawić kontener, a w `showStep()` (gdzie element już jest w DOM — analogicznie do obsługi `<video>`) wywołać `katex.render(step.src, el)`. Reużyć istniejącej nawigacji prev/next, `.step-comment`, dzielników.
3. **Lekka animacja kroku** w JS/CSS: fade-in + opcjonalne podświetlenie zmienianych członów kolorami `WG_KOLORY` (spójność z widgetami). Bez bibliotek zewnętrznych na start; jeśli potrzeba płynniejszych przejść — rozważyć zvendorowany anime.js.
4. **PoC na zad 1**: przepisać `solutionStepByStep` zad 1 na kroki `type: "math"` (LaTeX), zostawiając wideo zad 2/3 nietknięte — bezpośrednie porównanie side-by-side w tej samej stronie.
5. **Styl**: reguły KaTeX/rozmiar w `.solution-step-by-step-container` w [style.css](style.css); zaktualizować sekcję „CSS & layout reference" i opis `solutionStepByStep`/schematu w CLAUDE.md (typ `math`) — zgodnie z zasadą utrzymywania dokumentacji w synchronie.
6. Wpisać zadanie/wynik do [todo3.md](todo3.md) (po polsku, sekcja „NOWE PUNKTY TODO ZAPISYWANE PRZEZ CLAUDE").

### Weryfikacja (bez build/test tooling)
Otworzyć [matematykazen.html](matematykazen.html) w przeglądarce (lub `python -m http.server`, żeby PDF/`object` i lokalne assety ładowały się poprawnie) i klik-test:
- Zad 1: rozwinąć „Rozwiązanie" → kroki LaTeX renderują się (nie surowy `$...$`), prev/next działa, wysokość nie skacze, ostatni krok odsłania poprawną odpowiedź (`markCorrectAnswer`).
- Zad 2/3: wideo nadal grają (pause/progress/replay) — brak regresji.
- Sprawdzić `file://` (offline) i wąski viewport (reflow LaTeX).

---

## Alternatywy (odrzucone dla tej fazy)
- **MathJax zamiast KaTeX** — cięższy i wolniejszy przy renderze synchronicznym; KaTeX lepszy dla wielu wstawek na stronie statycznej.
- **Zostać przy czystym Unicode** (jak teraz w `solutionText`) — działa dla statyki, ale ubogie do animowanych, wieloliniowych przekształceń; LaTeX daje lepszą typografię i skalę.
- **Pełne odejście od Manim** — niepotrzebne; hybryda zachowuje go tam, gdzie wygrywa.
