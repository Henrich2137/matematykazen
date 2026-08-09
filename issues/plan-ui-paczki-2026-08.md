# Plan: UI w czterech paczkach (sierpień 2026)

Wsad dla sesji autonomicznych. **To jest jedyne źródło zadania** — sesja dostaje w promcie
tylko numer paczki i czyta resztę stąd.

Powstał 2026-08-09 z rozmowy z Henrichem, z listy otwartych punktów UI w TODO.md
(linie ~6–35). Pięć rozstrzygnięć gustu zapadło z góry, żeby żadna sesja nie musiała pytać —
patrz „Decyzje Henricha".

---

## Zasady wspólne dla wszystkich paczek

**Weryfikuj zrzutami, nie rozumowaniem.** W kontenerze jest Playwright + Chromium
(`issues/playwright-podglad.md`) i skrypt `tools/zrzuty.js`. Zmiana CSS bez zrzutu „przed/po"
to zgadywanie — a wszystkie punkty w tym planie są wizualne.

```
python3 -m http.server 8000 --bind 127.0.0.1
NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/zrzuty.js --przed
# … zmiany …
NODE_PATH=/usr/local/share/npm-global/lib/node_modules node tools/zrzuty.js --po
```

Szczegóły użycia i pułapki — nagłówek `tools/zrzuty.js`.

**Zakres jest zamknięty.** Rób punkty ze swojej paczki i nic poza nimi. Znalazłeś coś innego —
dopisz do TODO.md w swojej sekcji (`SONNET DOPISAŁ:` / `OPUS DOPISAŁ:` / `FABLE DOPISAŁ:`),
nie naprawiaj.

**Nie ruszaj cudzych paczek.** Paczki jadą sekwencyjnie po tych samych plikach CSS; wejście
w cudzy punkt „przy okazji" psuje następnej sesji punkt odniesienia.

**Każda paczka kończy się:**
1. commitem wg `CLAUDE.md` (trailer `Co-Authored-By: Local <Model> <Effort> …`, bez prefiksu
   w tytule);
2. przeniesieniem zrobionych punktów z TODO.md do bieżącego pliku w `done/`
   (patrz `done/README.md`) — TODO.md ma zostać krótki;
3. dopisaniem **1–3 pozycji do `TODO.md`, sekcja `TESTOWANIE HENRICH:`** — wyłącznie rzeczy,
   których **nie dało się zweryfikować zrzutem**: dotyk, odczucie „za blade / w sam raz",
   realne renderowanie na sprzęcie Henricha. Nie zakładaj na to osobnego pliku w `issues/` —
   Henrich tam nie zagląda. Napisz to samo w podsumowaniu dla niego. Nie wpisuj tego, co
   potwierdziłeś zrzutem;
4. **podbiciem numeru wersji** (`#wersja` w `template.html` ORAZ `.landing-wersja`
   w `index.html` — muszą się zgadzać) i **wypchnięciem commita na `origin`**. Bez tego Henrich
   ogląda na telefonie starą stronę. Patrz `CLAUDE.md`, sekcja „Oddawanie pracy do testów".

**Pułapki testowe** (z sesji 1 audytu, nadal aktualne):
- pierwszy `.exercise-container` w DOM to **pusty szablon** — w testach bierz `.nth(1)`;
- ciemna paleta jest w **dwóch bliźniaczych blokach** `style/base.css`
  (`@media (prefers-color-scheme: dark)` + `html.theme-dark`) — każdy token o innej wartości
  w ciemnym motywie dopisz w OBU;
- `style/responsive.css` ładuje się **ostatni** i nadpisuje resztę — sprawdź go, zanim uznasz,
  że reguła „nie działa".

**Poziom staranności.** Celujemy w solidne 75%, nie w 95%. Jeśli dopieszczenie punktu kosztuje
wyraźnie więcej niż jego wartość — zrób wersję dobrą, opisz w commicie, co zostało, i idź dalej.

---

## Decyzje Henricha (zapadły, nie podważaj)

1. **Karta zadania zostaje bez ramki i bez zaokrągleń.** Minimalizm i czystość; żadnych
   ozdobników, które byłyby przerostem formy nad treścią. Zamyka punkt „decyzja Henricha"
   z `ui-spojnosc-etap2.md`.
2. **Hover w menu = podświetlone tło** (nie ramka). To jest wzorzec dla chrome strony.
3. **Marginesy zostają w obecnych proporcjach.** Obecna skala „nie jest zła". Ujednolicaj tylko
   tam, gdzie to bezpieczne i widocznie poprawia rzecz — bez przebudowy skali.
4. **Link licencyjny w stopce**: `https://github.com/Henrich2137/matematykazen/blob/HEAD/LICENSE.md`
   (`HEAD`, nie `master` — przeżyje zmianę nazwy gałęzi).
5. **Przesunięcie punktacji** dobierz tak, żeby wyglądało dobrze na popularnych szerokościach
   telefonów, nie tylko na desktopie. Model sam ocenia na zrzutach.

---

## Paczka 1 — Drobnica

**Model: Sonnet 5 High.** Mała, dobrze określona. Jest też testem całego łańcucha
(serwer → zrzut → poprawka → zrzut), więc rób ją pierwszą.

1. **„Sprawdź obliczenia" → „Sprawdzanie obliczeń"** w rozwijanej liście przy zadaniach
   otwartych. Zmiana napisu; sprawdź, czy ten sam ciąg nie występuje gdzieś jeszcze.
2. **Punktacja bliżej zadań** — przesunąć w lewo o ~40px (`#total-score` / pigułka punktowa
   przy zadaniu). Patrz decyzja 5: dobierz wartość na zrzutach desktop **i** telefon; suma
   ma wyglądać spójnie z punktacją zadań i z kluczem punktowym w zadaniach otwartych.
3. **Stopka: copyright + licencja.** Dopisać dyskretną linijkę, np.
   `© 2026 Henrich2137 · Licencja` z linkiem z decyzji 4. Styl stopki jest już ustalony —
   dopasuj się do niego, nie wymyślaj nowego. Dotyczy `template.html` i `index.html`
   (landing też ma sekcję „Licencja" — sprawdź, czy nie dublujesz).
4. **Przyciski na telefonie łamią się po dwa w rzędzie** (Podpowiedź / Rozwiązanie / Zgłoś błąd /
   Pokaż wzory) i wiersze są zbyt ciasno. Zwiększyć odstęp **między liniami** (`row-gap`),
   nie między kolumnami. Zawijanie jest zamierzone (`flex: 1 1 0` + breakpoint 720px,
   patrz `ui-spojnosc-etap2.md` punkt 4) — poprawiamy tylko oddech.

---

## Paczka 2 — Panel boczny

**Model: Opus 5 Medium.** Miks CSS i JS w jednym regionie ekranu. Swipe to jedyna nowa
funkcjonalność w całym planie i ma realne pułapki, stąd mocniejszy model.

Kontekst: `app/bootstrap.js` (panel `#sidebar`), `app/exam.js` (mechanizm `setExamMenuDisabled`).

1. **`#sprawdz-wszystkie` ma być zawsze widoczny.** Dziś znika i pojawia się przy przełączaniu
   „Poprawność odpowiedzi" (natychmiast ↔ po „sprawdź"), przez co panel skacze. Ma być stale
   obecny: aktywny w trybie „po sprawdź", wyszarzony/`disabled` w „natychmiast" — **wzoruj się
   na `setExamMenuDisabled` w `app/exam.js`**, ten mechanizm już istnieje.
2. **„Poprawność" wyszarzona w trybie egzaminu**, dokładnie tak jak „Punktacja". Ten sam
   mechanizm co wyżej.
3. **Przełączniki są zbyt blade** — wyglądają na nieaktywne/zablokowane, choć działają.
   Podnieść kontrast stanu normalnego tak, żeby dało się je odróżnić od stanu `disabled`
   z punktów 1–2. To jest warunek konieczny: po tej paczce „wyszarzony" musi znaczyć
   „wyłączony", a nie „domyślny". Sprawdź w obu motywach.
4. **Tekst stanów przełącznika wygląda na rozmyty** („ciemny", „jasny", „wł.", „wszystko").
   Henrich opisuje to jako bleeding/bloom. Najbardziej prawdopodobna przyczyna: segment
   aktywny ma `font-weight: 600` przy 13px (patrz inwentarz w `ui-spojnosc-etap2.md`) —
   pogrubiony mały tekst na kolorowym tle rozlewa się przy subpikselowym wygładzaniu.
   Zdiagnozuj na zrzucie w powiększeniu, zanim zmienisz; kandydaci: waga fontu, kontrast
   tła segmentu.
5. **Swipe w lewo zwija panel — tylko na telefonie.** Pułapki, których zrzut nie pokaże:
   gest nie może przechwytywać pionowego scrolla ani przeciągania po treści zadania;
   próg (dystans + prędkość) musi odsiewać przypadkowe muśnięcia; nie może się kłócić
   z gestem „wstecz" przeglądarki przy krawędzi ekranu. Playwright potrafi zasymulować
   dotyk (`hasTouch: true`), ale ostateczna ocena płynności idzie na listę dla Henricha.

---

## Paczka 3 — Kolory i motyw ciemny

**Model: Opus 5 Medium.** Mała, ale wymaga porównywania wartości piksel po pikselu.

1. **Tło widżetów w ciemnym motywie = tło strony.** Dziś się nieznacznie różni. Zamiast
   dobierać na oko: wyciągnij obliczone `background-color` widżetu i `body` przez
   `getComputedStyle` i porównaj liczby — różnica ma zniknąć, nie zmaleć. W jasnym motywie
   wygląda dobrze, ale **potwierdź tak samo liczbowo**, że to faktycznie ta sama wartość.
2. **Tło formularza zgłoszenia błędu ciemniejsze niż dziś, ale jaśniejsze niż główne tło
   strony** — ma być „coś pomiędzy". Użyj istniejącego tokenu, jeśli któryś pasuje
   (`--bg-muted` i sąsiedzi w `style/base.css`); nowy token zakładaj dopiero, gdy żaden nie
   pasuje, i dopisz go w obu blokach ciemnej palety. Formularz żyje w `app/report.js`
   (jeden wspólny węzeł przenoszony `insertBefore` między kartami zadań).

---

## Paczka 4 — Spójność UI, etap 2

**Model: Fable.** Największa i najbardziej oceniająca — audyt całego `style/`.
**Idzie ostatnia**, bo zamiata po wartościach ustalonych w paczkach 2 i 3.

Pełny wsad: **`issues/ui-spojnosc-etap2.md`** (inwentarz kontrolek, numery linii, tokeny
z sesji 1). Czytaj go w całości, tu jest tylko mapa różnic wobec tamtego pliku:

- punkt 3 („dwa modele hoveru") jest **rozstrzygnięty** — decyzja 2: tło. Zastosuj i opisz
  zasadę w komentarzu;
- punkt o **ramce/zaokrągleniu karty zadania** jest rozstrzygnięty na „zostaje jak jest" —
  decyzja 1. Nie realizuj go;
- **marginesy** — decyzja 3: bez przebudowy skali;
- reszta punktów bez zmian: skala rozmiarów kontrolek, hover na odpowiedziach ABCD/PF/pkt,
  cień okienka podsumowania jako token, dwa miejsca z ramką 2px zamiast 1px, zaokrąglenie
  okienka podsumowania, landing vs arkusz (rozmiary fontu + kontrast WCAG, patrz
  `issues/dark-mode-css-zmienne-landing.md`).

⚠️ Punkt 2 tamtego pliku rekomenduje hover **ramką** na przyciskach odpowiedzi — i to zostaje
w mocy. Decyzja 2 dotyczy **menu / chrome**, nie kontrolek w treści zadania; w treści tło
koliduje ze stanami poprawne/błędne/`.selected`, które już grają tłem.

---

## Kolejność i zależności

```
etap 0: tools/zrzuty.js  ──►  P1 drobnica  ──►  P2 panel boczny  ──►  P3 kolory  ──►  P4 spójność
```

- **P1 przed resztą**: potwierdza, że łańcuch narzędziowy działa, zanim powierzymy mu coś
  większego.
- **P2 przed P3**: obie dotykają kontrastu i tła; panel boczny ustala, jak wygląda „aktywne"
  kontra „wyszarzone".
- **P4 na końcu**: ujednolica tokeny, więc musi widzieć wartości już ustalone.
- Paczki **nie mogą** iść równolegle — grzebią w tych samych regionach `style/`.
