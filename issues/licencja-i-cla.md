# Licencja i CLA — jak to jest poskładane

> **Uzupełnienie od 2026-08-20:** katalog `widgets/` nie jest już objęty PolyForm
> Noncommercial, tylko własną licencją zastrzeżoną (`widgets/LICENSE.md`).
> Cały rozdział licencyjny opisuje [licencja-premium.md](licencja-premium.md).
> Ten plik dotyczy warstwy PolyForm + CLA, która obowiązuje dla reszty repozytorium.

Opis konstrukcji, nie problem. Wyniesione z CLAUDE.md 2026-08-12 — do codziennej pracy nad
stroną nie jest potrzebne. Otwórz, gdy dotykasz `LICENSE.md` / `CONTRIBUTING.md` / `README.md` /
szablonu PR-a, albo gdy pojawia się pytanie o licencjonowanie wkładu.

Kontekst zrobienia: `done/00-stary-done.md`… właściwie `done/04-biezace.md`, wpis 2026-08-02
(„licencja PolyForm Noncommercial 1.0.0 + CLA").

## Pliki meta w rootcie (wszystkie po polsku poza samym tekstem licencji)

- **`LICENSE.md`** — **PolyForm Noncommercial 1.0.0**, oficjalny tekst dosłownie
  (**nie przeredagowuj go**), poprzedzony liniami copyright + `Required Notice:`, a po `---`
  polskie uwagi: zadania i klucze CKE **nie** są objęte licencją, odnośnik do CONTRIBUTING.md,
  kontakt w sprawie licencji komercyjnej.
- **`CONTRIBUTING.md`** — jak kontrybuować + **CLA**: otwarcie PR-a udziela właścicielowi
  szerokiej, nieodwołalnej, *także komercyjnej* licencji na wkład, żeby przyszła zmiana licencji
  (Faza 3 w OVERVIEW.md) nie była zablokowana prawami autorskimi kontrybutorów.
- **`README.md`** — strona tytułowa repo (czym jest projekt, jak serwować lokalnie,
  sekcja „Licencja").
- **`.github/PULL_REQUEST_TEMPLATE.md`** — checklista + wytłuszczona linia wiążąca autora PR-a
  z CLA (względny odnośnik `../CONTRIBUTING.md`).

## Dwa świadome placeholdery

Oba są też pilnowane w TODO.md (sekcja `OPUS DOPISAŁ`):

1. Właściciel występuje pod pseudonimem **`Henrich2137`** — `LICENSE.md` linie 1–2
   + `CONTRIBUTING.md` punkt 2. **Zmieniaj oba naraz**, jeśli prawdziwe nazwisko kiedyś zostanie
   upublicznione (CLA na pseudonim jest słabsze dowodowo).
2. URL w `Required Notice:` wskazuje na GitHub Pages, dopóki `matematykazen.pl` faktycznie
   nie ruszy. **Ta linia jest kopiowana przez każdego redystrybutora**, więc nigdy nie może
   prowadzić w martwy link.
