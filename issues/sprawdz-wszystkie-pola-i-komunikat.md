# „Sprawdź wszystkie odpowiedzi": pomija pola tekstowe + brak potwierdzenia kliknięcia

Zgłoszone przez Henricha 2026-07-27. **Dla Sonneta High** — dwie zmiany w jednym miejscu
(`sprawdzWszystkieOdpowiedzi()`), więc jedno zlecenie. Część czysto-CSS z tego zgłoszenia
(ciemniejszy tekst przycisku w stopce) jest już zrobiona — patrz `DONE/04-biezace.md`.

## 1. Zbiorcze sprawdzanie pomija zadania z polem tekstowym (zad. 29, 8, 9…)

**Mechanizm.** `sprawdzWszystkieOdpowiedzi()` w [app/bootstrap.js:170](../app/bootstrap.js) iteruje po
rejestrze `oczekujaceSprawdzenia` (deklarowany w `app/state.js:175`):

```js
oczekujaceSprawdzenia.forEach(z => {
    if (z.maZaznaczenie() && !z.czySprawdzone()) z.ocen();
});
```

Do rejestru wpisują się **tylko zadania zamknięte** — `app/render.js` robi `push` w trzech miejscach
(linie ~222, ~294, ~390: ABCD, prawda/fałsz, multiSelect). Zadania z polem tekstowym mają własne
przyciski „Sprawdź" i **nie rejestrują się wcale**:

| typ | gdzie w render.js | przycisk | co robi ocena |
|---|---|---|---|
| `fillIn` (np. zad. 29) | ~570–597 | `.fill-in-check` | normalizuje wpisy, koloruje pola, **przyznaje punkty** (`setScore` proporcjonalnie do trafień) |
| `finalAnswer` (zad. 8, 9) | ~430–470 | `.final-answer-check` → `ocenKoncowaOdpowiedz()` | koloruje pole; **punktów NIE rusza** (za nie odpowiada samoocena) |

**Do zrobienia.** Zarejestrować oba typy w `oczekujaceSprawdzenia` z tym samym interfejsem
(`maZaznaczenie` / `czySprawdzone` / `ocen`), zamiast dopisywać do przycisku drugą ścieżkę:

- `fillIn`: `maZaznaczenie` = co najmniej jedno pole niepuste po `trim()`; `czySprawdzone` = pola mają
  już klasę `correct`/`incorrect` (ocena ustawia je wszystkie naraz, więc wystarczy sprawdzić pierwsze);
  `ocen` = to, co dziś robi handler `fillCheck` — **wydzielić z niego nazwaną funkcję** i wołać z obu
  miejsc, nie duplikować logiki normalizacji.
- `finalAnswer`: `ocen` = istniejąca `ocenKoncowaOdpowiedz()` (jest już osobną funkcją, wystarczy ją
  wpisać do rejestru); `czySprawdzone` = klasa na `finalInput`.
- Pamiętaj, że edycja pola `fillIn` kasuje klasy oceny (`input` listener, render.js ~571) — po takiej
  edycji zadanie musi znów wyjść jako „niesprawdzone", czyli `czySprawdzone` ma czytać DOM, nie flagę.

**Skutek uboczny do świadomej akceptacji:** po tej zmianie „sprawdź wszystkie" zacznie przyznawać
punkty za `fillIn` (dziś trzeba kliknąć każdy „Sprawdź" ręcznie). To jest cel zgłoszenia.

**Bonus — domyka drugi wpis z TODO.** „w zadaniach z oknem z ostateczną odpowiedzią (jak 8 czy 9),
po zrobieniu egzaminu ostateczna odpowiedź powinna się samodzielnie sprawdzić": gdy `finalAnswer`
siedzi już w rejestrze, wystarczy w `finishExam()` (`app/exam.js`) przelecieć rejestr i wywołać `ocen()`
dla wpisów tego typu. Wymaga oznaczenia wpisów (np. pole `typ: "finalAnswer"`), żeby egzamin nie
odsłaniał przy okazji zadań zamkniętych, których uczeń nie chciał sprawdzać. Jeśli to zrobisz, usuń
tamten punkt z TODO.md i opisz w DONE.

⚠️ Nie ruszaj widoczności przycisków w egzaminie: `.answer-check-floating` i `.final-answer-check` są
tam chowane, a „sprawdź wszystkie" jest wyszarzony (`OPCJE_MENU_EGZAMIN`, `app/exam.js:125`) — zbiorcze
sprawdzanie w trakcie egzaminu **musi** zostać niedostępne.

## 2. Brak potwierdzenia po kliknięciu

Dziś klik w „sprawdź wszystkie" nie daje żadnej informacji zwrotnej — jeśli akurat nic nie było
zaznaczone, wygląda jak zepsuty przycisk. Henrich: „powinny dawać slight komunikat obok na zielono
«sprawdzono :)» czy coś w tym stylu". Dotyczy **obu** kopii przycisku (stopka + wiersz panelu bocznego).

Spec (ustalony jako rozsądny domyślny; drobne brzmienie/format zostawiam do oceny na zrzucie):

- **Stopka** (`#sprawdz-wszystkie-stopka`): komunikat inline **obok** przycisku, `--correct`,
  drobny (13–14px), np. „sprawdzono ✓". Nie może przesuwać przycisku — trzymaj go poza flow
  (`position: absolute` względem opakowania) albo w stałej szerokości, tak jak zrobiono to z
  `.answer-check-floating`.
- **Panel boczny** (`#sprawdz-wszystkie`): 260px nie zmieści zdania obok etykiety — pokaż tylko zielony
  ✓ na prawym końcu wiersza (`.sidebar-akcja` jest flexem, wystarczy `<span>` z `margin-left: auto`).
  **Nie używaj `textContent` na wierszu panelu** — wymazałoby ikonę SVG i etykietę (patrz
  „Never write textContent on a sidebar button" w ARCHITECTURE_CSS.md); dokładaj/pokazuj osobny węzeł.
- **Zniknięcie:** po ~2,5 s, `opacity` z tranzycją; kolejny klik resetuje licznik. W
  `@media (prefers-reduced-motion: reduce)` bez animacji.
- **Gdy nie ma czego sprawdzać** (zero ocenionych zadań): komunikat **przygaszony**, nie zielony
  (`--text-faint`), np. „brak zaznaczonych odpowiedzi" — inaczej „sprawdzono ✓" kłamie.
- **A11y:** kontener komunikatu z `aria-live="polite"` i `role="status"`, żeby czytnik ekranu ogłosił
  wynik akcji.
- Kolory tylko przez tokeny (`--correct`, `--text-faint`) — dark mode wtedy działa sam.
- Do rozważenia na zrzucie: czy dołożyć liczbę („sprawdzono 12 ✓"). Henrich prosił o „slight", więc
  domyślnie bez liczby.

Alternatywa, którą warto odrzucić świadomie: istniejący `.zglos-toast` (fixed, dolny środek, zielona
ramka) dałby to za darmo — ale toast jest zarezerwowany dla zgłoszeń błędów i pojawia się w zupełnie
innym miejscu ekranu niż kliknięty przycisk, więc „obok" z prośby Henricha nie byłoby spełnione.

## Weryfikacja

Playwright (przepis w `issues/ui-spojnosc-etap2.md`, sekcja „Metoda"), arkusz `2024-grudzien`:
1. wpisz odpowiedź w zad. 29 (`fillIn`) i w zad. 8 (`finalAnswer`), **nie** klikaj ich „Sprawdź";
2. klik „sprawdź wszystkie" (raz w stopce, raz w panelu) → pola dostają `correct`/`incorrect`,
   suma punktów rośnie o `fillIn`, komunikat się pokazuje i gaśnie;
3. klik przy pustym arkuszu → komunikat przygaszony, nie zielony;
4. w trybie egzaminu przycisk nadal `disabled`, pola nieodsłonięte;
5. edytuj sprawdzone pole `fillIn` → klik „sprawdź wszystkie" ocenia je ponownie.
**Pułapka testowa:** pierwszy `.exercise-container` w DOM to pusty szablon — bierz `.nth(1)`.
