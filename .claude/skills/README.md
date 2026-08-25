# Skille projektowe

Skille leżące tutaj Claude Code wczytuje automatycznie przy starcie sesji (scope projektu,
jadą z repo tak samo jak wpisy w `.claude/settings.json`).

## manim-composer, manimce-best-practices

Źródło: [adithya-s-k/manim_skill](https://github.com/adithya-s-k/manim_skill), licencja MIT,
skopiowane 2026-08-25 z commita `cef0450`. To nie jest plugin z marketplace'u, więc
`claude plugin install` go nie obsługuje: pliki są po prostu skopiowane z katalogu `skills/`
tamtego repo.

- `manimce-best-practices` - reguły i przykłady do Manim Community Edition (`from manim import *`),
  czyli tej wersji, której używa `manimations/` (CE 0.18.1).
- `manim-composer` - planowanie filmu scena po scenie, zanim powstanie kod.

**Świadomie NIE skopiowano `manimgl-best-practices`** (952 KB): to reguły do ManimGL, wersji
3Blue1Browna, która jest osobnym, niekompatybilnym frameworkiem. W tym projekcie nie jest używana.

### Pierwszeństwo mają zasady domowe

Te skille są ogólne i nie znają zasad tego projektu. W razie sprzeczności obowiązują
**nasze** pliki, nie one:

- [manimations/README.md](../../manimations/README.md) - „Zasady krok po kroku" (jeden krok =
  jedna transformacja, czarne → zielone → animacja → czarne, ostatnia klatka kroku = pierwsza
  klatka następnego) i pięć zasad dla opisu pod filmem.
- [COLORS.md](../../COLORS.md) - co znaczy który kolor. Skill zewnętrzny kolorystyki tego
  projektu nie zna.
- [SOLUTION_TEXT_RULES.md](../../SOLUTION_TEXT_RULES.md) - rozwiązanie opisowe ma iść krok w krok
  z filmem.
