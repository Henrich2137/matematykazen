# Spójność UI — etap 2: reszta drobnic z audytu

Wsad dla **Sonneta High**. Powstał z audytu w sesji 1 (Opus High, 2026-07-27) — tam wprowadzono
warstwę tokenów i zamknięto 6 punktów Henricha, patrz `done/` (wpis „Spójność UI, sesja 1").
Tokeny są już na miejscu i to ich należy używać: `--radius-kontrolka`, `--radius-pigulka`,
`--border-kontrolka`, `--shadow-panel`, `--segment-bg` / `--segment-text` (style/base.css).

⚠️ Ciemna paleta jest w **dwóch bliźniaczych blokach** base.css (`@media prefers-color-scheme:
dark` + `html.theme-dark`) — każdy nowy token o innej wartości w dark dopisz w OBU.

## Metoda

Ta sama, co w sesji 1 (bez zrzutów to zgadywanie): `python -m http.server 8123` +
playwright z cache npx (`NODE_PATH=/c/Users/T580Admin/AppData/Local/npm-cache/_npx/705bc6b22212b352/node_modules`),
zrzuty light/dark × 1440/1280/390 × stany (ćwiczenia, egzamin, sidebar, panel PDF, stopka, landing).
Uwaga na jedną pułapkę testową: **pierwszy `.exercise-container` w DOM to pusty szablon** —
w testach bierz `.nth(1)`.

## Inwentarz kontrolek po sesji 1 (1440, motyw jasny)

| kontrolka | font | waga | padding | ramka | radius |
|---|---|---|---|---|---|
| pigułka narożnika (`#total-score`) | 13px | 400 | 6px 12px | 1px | 6px |
| `#logo` | 16px | 400 | 6px 10px | — | 6px |
| `#sidebar-toggle` | — (32×32) | — | 0 | 1px | 6px |
| wiersz sidebara (akcja/ustawienie) | 13px | 400 | 0 6px, h 40px | — | 6px |
| segment przełącznika (aktywny) | 13px | **600** | 5px 14px | — (obrys kontenera) | — |
| przyciski stopki (×3) | 17px | 400 | 10px 24px | 1px | 6px |
| odpowiedź ABCD | **18px** | 400 | **10px 12px** | 1px | 6px |
| samoocena „N pkt" | 17px | 400 | **8px 11px** | 1px | 6px |
| pole fillIn / „ostateczna odpowiedź" | 17px | 400 | **6px 8px** | 1px | 6px |
| textarea rozwiązania | **16px** | 400 | 10px 12px | 1px | 6px |
| przycisk tekstowy (`.light-button`) | 16px | 400 | 0 | — | — |

Promienie i grubości ramek są już jednolite. **Zostaje rozjazd rozmiarów i paddingów** — to
główna robota etapu 2.

## Do zrobienia (posortowane po widoczności dla użytkownika)

1. **Skala rozmiarów kontrolek w treści zadania.** Cztery rozmiary fontu na jednej karcie
   (18 / 17 / 16 px) i cztery różne paddingi — patrz tabela wyżej. Ustalić dwie–trzy klasy
   (np. „kontrolka duża" = odpowiedzi ABCD, „kontrolka" = pola i samoocena, „tekstowa") i sprowadzić
   do nich `sheet.css`: `.button-container button` (534), `.self-score-container button` (764),
   `.fill-in-input` (685), `.final-answer-input` (804), `.open-answer` (736).

2. **Przyciski odpowiedzi nie mają `:hover`.** Chrome strony reaguje (pigułki → `--border-strong`,
   wiersze sidebara → tło `--bg-muted`), a klikalne odpowiedzi ABCD, P/F i „N pkt" nie dają
   żadnej informacji zwrotnej przed kliknięciem. Dodać jeden model hoveru dla kontrolek treści
   (rekomendacja: `border-color: var(--border-strong)` — nie tło, żeby nie kolidowało ze stanami
   poprawne/błędne/`.selected`, które grają tłem i `inset box-shadow`).

3. **Dwa modele hoveru w chrome.** Ramka (narożniki, panele) vs tło (sidebar). Rozstrzygnąć,
   który jest wzorcem, i opisać wybór w komentarzu — dziś nie ma zapisanej zasady.

4. **`.light-button { width: 30% }`** (sheet.css:894) — sztywny procent na trzy przyciski
   („Podpowiedź / Rozwiązanie / Pokaż potrzebne wzory"). Na 390px trzeci zawija się na trzy
   linie i wiersz robi się nierówny (widać na zrzucie `dark-390-stopka`). Kandydat: flex z `gap`
   i zawijaniem, zamiast procentów.

5. **Samoocena na telefonie**: pięć przycisków „0–4 pkt" schodzi 2 + 2 + 1 z osamotnionym
   ostatnim na środku. Rozważyć siatkę o równych kolumnach.

6. **Cienie poza tokenem.** `--shadow-panel` objął sidebar, panele PDF i toast. Zostały:
   `#egzamin-podsumowanie .egzamin-okno` (exam.css: `0 6px 24px rgba(0,0,0,.10)`) oraz kropki
   wskaźników (`0 1px 4px`). Modal ma prawo mieć mocniejszy cień, ale wtedy niech to będzie
   **nazwany** `--shadow-modal`, a nie wartość wpisana w miejscu.

7. **Ostatnie ramki 2px.** `#wskazniki-ukryj` (exam.css:268) i `.solution-text-container`
   (`border-bottom: 2px solid var(--border-subtle)`, sheet.css:924) — jedyne miejsca poza
   widżetami, gdzie 2px nie niesie znaczenia. W widżetach (`.wg-a` / `.wg-b`) 2px zostaje
   celowo: koduje kolor wartości.

8. **`#egzamin-podsumowanie .egzamin-okno` bez `border-radius`** — jedyna „karta" strony z ostrymi
   narożnikami po sesji 1. Dołożyć `--radius-kontrolka`.

9. **Odstępy: brak skali.** Marginesy w chrome i stopce to dziś 10 / 16 / 20 / 40 / 50 / 60 / 70 /
   80px bez systemu (np. `#tryb-przelacznik` ma 50px góra / 40px dół, `.landing-section` 70px,
   `#exercises-wrapper` 66px, `.landing-page` 60px góra). Jeśli po przejrzeniu widać powtarzalny
   rytm — wprowadzić `--space-*` i sprowadzić do niego wartości. **Nie robić tego na zapas**:
   zmiana odstępów jest najbardziej widoczna wizualnie, więc tylko z porównaniem zrzutów.

10. **`.exercise-container` (karta zadania) jest bez ramki i promienia** — po sesji 1 wszystko
    wokół jest zaokrąglone, więc warto sprawdzić na zrzucie, czy karta nie wygląda teraz jak
    element z innego systemu. Zmiana jest odwracalna i czysto wizualna — decyzja Henricha.

11. **Landing kontra arkusz.** Po sesji 1 CTA i karty landingu jadą już na tokenach, ale zostaje
    typografia: `.landing-cta` 18px, `.landing-card h3` 17px, `.landing-lede` 18px vs 16px treści
    arkusza. Przy okazji zajrzeć do `issues/dark-mode-css-zmienne-landing.md` (kontrast WCAG) —
    część zmiennych landingu wciąż wskazuje nie te warstwy, co arkusz.

## Poza zakresem

- Białe tła widżetów w dark (`--canvas-bg` jest celowo jasny) — osobny punkt w TODO.md.
- Obrazki CKE i wideo Manima w dark — `issues/dark-mode-obrazki-wideo.md`.
- Filtrowanie kartki PDF w panelach — Henrich zdecydował, że kartka zostaje biała.
- Zmiany zachowania (kolejność pozycji w panelu, „Punktacja" w egzaminie, wskaźniki na telefonie)
  — siedzą w „INNE NOTATKI" w TODO.md, to nie jest praca nad spójnością wizualną.
