# Brief dla Fable, arkusz 2026-maj

Przygotowane 2026-08-15 przez Opusa. **Przeczytaj to zamiast zwiedzania repo.**

## Zadanie

Pilotaż na **trzech zadaniach** z `matura/2026-maj`. Dla każdego:

1. **podpowiedź** (`hint`)
2. **Zwykłe, rozwiązanie opisowe** (`solutionText`)
3. **widżet interaktywny**, nowy plik w `widgets/`, jeśli zadanie się do tego nadaje

Zadania (wybór Henricha):

- zad 2. - Interaktywne/widżet: Podobnie jak zad 5. w 2024-grudzien
- zad 8. - Interaktywne/widżet: Zmienianie x suwakiem zmienia:
  - liczbę na miejscu x w równaniu
  - punkt na osi liczbowej na której są oznaczone wszystkie 3 rozwiązania oznaczone tym samym kolorem co literki w równaniu

  **Suwak rusza `x`, i to jest celowe, nie „poprawiaj" tego na `m`.** Owszem, pytanie
  zadania dotyczy `m`, a `x` jest niewiadomą, więc suwak na `m` wygląda na naturalniejszy.
  Ale rzecz w tym, co uczeń ma zobaczyć: przeciągając `x` trafia w moment, gdy **jeden
  nawias się zeruje**, a wtedy cały iloczyn robi się `0` i równanie jest spełnione.
  To jest sedno całego zadania, czyli dlaczego pierwiastek jest pierwiastkiem. Suwak na `m`
  pokazywałby tylko, że trzeci punkt jeździ po osi, czyli skutek zamiast przyczyny.
- zad 10. - Interaktywne/widżet: po uproszczeniu do 
postać ogólna >= 0
zrobić podobnie jak w zad 9. w 2024-grudzien

**Nie rozszerzaj zakresu sam**, nawet gdy zostanie budżet. Znalazłeś coś do poprawy poza zakresem → wpis do `TODO.md`, nie poprawka.

## ⛔ STOP po pierwszym zadaniu

Zrób **jedno** zadanie w komplecie, potem **zatrzymaj się i oddaj do testów.**
Nie rób pozostałych dwóch, dopóki Henrich nie potwierdzi. Chodzi o to, żeby
rozjazd stylu wyszedł po jednym zadaniu, a nie po trzech.

Oddając, napisz w **dwóch** miejscach, w czacie i w `TODO.md` w sekcji
`TESTOWANIE HENRICH:`, konkretne polecenia: co kliknąć i czego szukać.

**Muszą tam być te punkty, bo sam ich nie sprawdzisz:**

- **Widżet na telefonie, palcem.** Czy da się trafić w przeciągany punkt i czy nie
  ucieka poza ekran przy 390 px. Playwright klika myszą, to nie to samo co palec.
- **Przełączenie motywu przy otwartym widżecie.** Czy przemalowuje się od razu, czy
  zostaje w kolorach poprzedniego (typowy objaw braku `wgZarejestrujRysowanie`).
- **Czy podpowiedź faktycznie pomaga, a nie zdradza.** To ocena nauczyciela, nie modelu.
- **Cokolwiek, co zmieniłeś w kodzie**, wymień z nazwy, osobno. Dane psują jedno zadanie,
  ale `widgets/_registry.js` i `template.html` są wspólne dla wszystkich arkuszy, więc
  błąd w pracy nad majem potrafi popsuć grudzień.

Podbij numer wersji **w dwóch plikach naraz**: `#wersja` w `template.html`
i `.landing-wersja` w `index.html`. Bez tego Henrich ogląda starą stronę i szuka
nieistniejącego błędu. Ostatnia wydana wersja to **v40**.

Po ukończeniu sesji zapisz mi w czacie oraz w TODO.md sugestie zmian architektonuicznych które ułatwiłby Ci pracę, zaoszczędziły tokenów bez poświęcania jakości. Każdą z tych sugesti oceń 1-5:
  - ile kontekstu zaoszczędzi
  - ile będzie kosztować
  - Jak wpływa ryzyko wystąpienia błędów (1 - zwiększa ryzyko, 5 - zmniejsza ryzyko)

## ⭐ Wzorzec: zadania 5 i 9 z 2024-grudnia

Henrich i Opus dopieścili je 2026-08-15 (wersje v35 do v40) **właśnie po to, żeby
były wzorcem dla Ciebie**. Otwórz oba na stronie i podejrzyj ich dane, zanim
cokolwiek napiszesz.

⚠️ **Kopiuj TYLKO te dwa.** Pozostałe 33 zadania w grudniu są w starym stylu,
jednym akapitem ciągłej prozy. To nie jest wzór do naśladowania.

### Rozwiązanie opisowe (`solutionText`)

Układ jest stały:

1. wzór na starcie, przez `\[ \]`, więc KaTeX centruje go sam
2. pod nim rachunek **linijka po linijce**, zwykłe `\( \)` rozdzielone `<br>`
3. całość po wzorze opakowana w `<div class="rozwiazanie-kroki">…</div>`

Ta klasa (w `style/sheet.css`) daje wyśrodkowanie i większe odstępy między
linijkami. **Nie ustawiaj tego stylami w danych**, klasa jest po to, żeby
wszystkie zadania wyglądały tak samo.

Zasady treści, od Henricha:

- Linijki mają iść **w ślad za krokami filmu**, ten sam rachunek w tej samej kolejności.
- Wzór **tylko na starcie**, nie powtarzaj go przy każdej linijce.
- **Bez długich wyjaśnień i zbędnych komentarzy.** Zostaje sam rachunek plus najwyżej
  jedno zdanie tam, gdzie bez niego nie wiadomo, skąd wynik (np. „ramiona paraboli idą
  w górę, więc wartości ≤ 0 leżą między miejscami zerowymi").
- `solutionTextMore` zostaw **pustym stringiem**. Pole musi istnieć, ale treść w nim
  powtarzałaby to, co widać już wyżej, a przycisk „pokaż więcej" chowa się sam.

### Widżet

- **Tytuł mówi, co zrobić, nie co wyjdzie.** „Zmień oprocentowanie p przy pomocy suwaka",
  a nie „sprawdź, kiedy kapitał trafi w 67 925,76 zł". Tytuł zapowiadający wynik odbiera
  uczniowi to, czego ma sam poszukać.
- **Odczyt pokazuje podstawienie, nie wynik.** Zad. 9 wypisuje `2,25 ⋅ (2,25 − 6) ≤ 7`
  i zostawia rachunek uczniowi; ✓ albo ✗ mówi, czy trafił. Wersja licząca za niego
  (`x(x − 6) = −8`) pokazywała skutek zamiast czynności.
- **Element, którym uczeń rusza, nie zmienia koloru na zielony ani czerwony.** Trzyma
  swój kolor zawsze, a poprawność niesie osobny znak obok. Inaczej jeden element mówi
  dwie rzeczy naraz.
- Ujemne liczby biorą nawias tylko tam, gdzie bez niego zlałyby się ze znakiem działania:
  `(−2,5) ⋅ (−2,5 − 6)`, a nie `(−2,5) ⋅ ((−2,5) − 6)`.

## 🎨 Kolory: przeczytaj COLORS.md, zanim cokolwiek pokolorujesz

Nowy plik, [COLORS.md](../COLORS.md), krótki. Trzy rzeczy, na których najłatwiej polec:

- **Domyślnie NIE koloruj.** Kolor bierze się z czynności ucznia, nie z tego, że coś jest
  ważne. W zad. 8 uczeń rusza `x`, więc `x` jest kolorowe, a parametr `m` zostaje czarny.
- **Żadnych kolorów wpisanych wprost.** W widżecie przez `WG_KOLORY`, w CSS przez zmienną.
  Kod na sztywno nie przełączy się z motywem i w jasnym motywie wygląda dobrze, więc
  nikt tego nie zauważy. Nowy kolor to nowy token w `base.css` w **trzech** miejscach
  (`:root` plus oba bliźniacze bloki ciemne) plus wpis w `WG_ZMIENNE`.
- **Zielony i czerwony znaczą wyłącznie poprawność.** Chcesz wyróżnić bez oceniania,
  weź niebieski albo pomarańczowy. (W zad. 5 linia celu była czerwona i to było błędem:
  cel nie jest pomyłką ucznia.)

**Sprawdzaj kontrast, zanim wybierzesz kolor tekstu.** Zapisany w notatkach jasny błękit
`#72d9fe` miał na białym tle 1,6:1, czyli był nieczytelny; poszedł `#0077b6` przy 4,87:1.
Próg to 4,5:1.

## ✍️ Zakaz pauzy i półpauzy

Nowa zasada w `CLAUDE.md`: **nie używaj znaków `—` ani `–`, nawet w zwykłych zdaniach.**
Zamiast nich przecinek, dwukropek, kropka albo nawias. Dotyczy treści dla ucznia,
komentarzy w kodzie, dokumentacji, opisów commitów i czatu. Powód: ten znak kojarzy się
czytelnikom z tekstem wklejonym na odczepnego i psuje wrażenie niezależnie od jakości treści.

## Stan arkusza

**41 pozycji w tablicy, ~33 zadania CKE. Prawie pusty:** zero podpowiedzi, zero rozwiązań
opisowych, zero kroków, zero widżetów. Jedyne, co jest, to `gradingCriteria`
przy zadaniach otwartych. Cokolwiek dodasz, będzie pierwsze.

## Cztery pułapki

**1. Numer zadania ≠ pozycja w tablicy.** W `exercises.json` nie ma pola z numerem,
siedzi tylko w treści `question` („Zadanie 15."). Zadania wieloczęściowe mają wpis-rodzic
(`maxScore: 0`, puste pola, **nie wypełniaj go**) i osobne wpisy na części: `12.`, `12.1`,
`12.2`. **Numer czytaj z `question`.** Opus przejechał się na tym i wyciągnął fałszywy wniosek.

**2. Kroki typu `"text"` NIE działają.** `ARCHITECTURE.md:59` wymienia
`"video"|"image"|"text"`, ale `renderStep()` w `app/steps.js:88-109` obsługuje tylko dwa
pierwsze, a `"text"` daje pusty kadr. Wszystkie 62 istniejące kroki to filmy.
**Dlatego rozwiązań krok po kroku w tym pilotażu nie ma w ogóle**, bo nie da się ich dodać
bez pliku wideo, a filmów nie robimy. Pole `text` kroku to co innego i działa, to opis
pod kadrem.

**3. Widżetu nie da się przełożyć.** Każdy z dziewięciu ma liczby swojego zadania wpisane
na sztywno. Nowy temat = **nowy plik + wpis w `widgets/_registry.js` + tag `<script>`
w `template.html`**. Pominięcie któregokolwiek z trzech daje ciche „brak widżetu", bez
błędu w konsoli. Spis i pomocniki: [widgets/README.md](../widgets/README.md).

**4. `python3 -m http.server` nie przewija filmów** (brak obsługi żądań zakresowych),
co wygląda na błąd odtwarzacza. Używaj `node tools/serwer.js 8001`; `curl -r 0-100` na
plik `.mp4` ma zwrócić **206**. Na porcie 8000 może już stać cudzy serwer, nie ubijaj go.

## Jak sprawdzać swoją pracę

W kontenerze jest Playwright z Chromium. Trzy rzeczy, na których Opus stracił dziś czas,
żebyś Ty nie musiał:

- **`NODE_PATH=/usr/local/share/npm-global/lib/node_modules` jest obowiązkowe**, inaczej
  „Cannot find module". Nigdy nie uruchamiaj `npx playwright install`, przeglądarka
  przychodzi bindem z hosta, a CDN jest za firewallem.
- **Pierwszy `.exercise-container` w DOM to ukryty szablon.** Bierz
  `.exercise-container:not(#exercise-template)`, inaczej czekasz w nieskończoność
  na coś, co nigdy nie będzie widoczne.
- **Zrób `scrollIntoViewIfNeeded()` przed klikaniem w płótno.** `page.mouse` klika we
  współrzędnych okna, więc kliknięcia w element poniżej zgięcia idą w powietrze,
  a widżet wygląda na zepsuty, choć działa.

Licz błędy KaTeXa przez `page.locator('.katex-error').count()`, ma wyjść **0**.
Do zwykłych zrzutów całej strony jest gotowe [tools/zrzuty.js](../tools/zrzuty.js),
nie pisz własnego skryptu na to.

`pkill -f "tools/serwer.js 8001"` **zabija też własną powłokę**, bo wzorzec pasuje do
polecenia, w którym siedzi. Ubijaj serwer osobnym wywołaniem.

## Oszczędzanie kontekstu

- ❌ **Nie czytaj `ARCHITECTURE.md` w całości**, akapity po 3 tys. znaków o wewnętrznej
  mechanice odtwarzacza. Do treści zadań bezużyteczne, **i miejscami nieprawdziwe**
  (patrz pułapka 2). Gdy stawka jest wysoka, czytaj kod, nie opis kodu.
- ❌ **Nie czytaj `done/`** ani `tablica-wzorow.pdf`.
- ✅ **Wzory z `tablica-wzorow-transkrypt/`**, przez skorowidz w jego `README.md`, który
  mapuje treść zadania na numer wzoru, więc wczytujesz 300 do 800 tokenów zamiast całej
  tablicy. Te same nawiasy KaTeX co `exercises.json`; w JSON-ie pamiętaj o `\\`.
- ✅ **Oficjalne rozwiązania: `matura/2026-maj/odpowiedzi.txt`** (95 kB po wyrównaniu
  2026-08-15). Sekcje „Uwagi:" pod zasadami oceniania to gotowy materiał na kryteria.
  **Nie każdy arkusz jest w UTF-8**, 2024-grudzień to cp1250.
- ✅ `2026-maj/exercises.json` ma 34 kB, można czytać w całości, wyciąg to zbędna robota.
- **Subagenci, Twoja decyzja**, ale subagent startuje **na zimno**: bez tej rozmowy i bez
  tego pliku. Każesz mu „przeczytać repo" → przeczyta te same dziesiątki tysięcy tokenów,
  i tak dla każdego osobno. Delegujesz, dawaj gotowy wyciąg w treści zlecenia.

## Bez pytania nie ruszaj

- **`app/steps.js` i reszty odtwarzacza**, delikatne, ma własny test `tools/test-krokow.js`
- ⛔ **NIE RENDERUJ FILMÓW.** Manim i TeX Live są w tym kontenerze zainstalowane, więc
  renderowanie *da się* odpalić, i o to właśnie chodzi, żebyś tego nie zrobił. Jeden
  film to długie czekanie i spalona sesja. Nie twórz scen, nie uruchamiaj `manim`, nie
  wchodź do `manimations/`. Filmy są poza zakresem tego pilotażu w całości.
- **rozszerzania zakresu** poza trzy zadania
- **wątpliwości merytorycznej w matematyce**, Henrich jest nauczycielem matematyki,
  pytaj jego zamiast zgadywać

Nowy widżet **jest** w zakresie, mimo że to kod, o to w pilotażu chodzi.

## Drobiazgi, o które łatwo się potknąć

- Treść dla ucznia **i komentarze w kodzie po polsku**
- Matematyka w KaTeX: `\( … \)` i `\[ … \]`, w JSON-ie z `\\`
- Jedna paczka zmian = **jeden commit**, trailer
  `Co-Authored-By: Local Fable 5 <Effort> <noreply@anthropic.com>`
- Zrzuty stanu strony sprzed Twoich zmian: [zrzuty/2026-08-15/](../zrzuty/2026-08-15/)
