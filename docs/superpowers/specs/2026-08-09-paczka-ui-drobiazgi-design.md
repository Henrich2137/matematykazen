# Paczka: 3 drobiazgi UI (hover panelu, kontrolki na telefonie, dark mode grafik)

Data: 2026-08-09. Trzy niezależne, niewielkie zmiany UI zebrane w jedną paczkę robotą (jeden PR/branch), bo każda z osobna jest za mała, żeby robić dla niej osobny cykl spec→plan.

## 1. Usunięcie podglądu hover w panelu ustawień

**Problem:** przyciski panelu (Wskaźniki/Punktacja/Motyw) po najechaniu myszą chowają aktualną wartość (`.wartosc`) i pokazują `.wartosc-podglad` z tekstem „aktualna → następna" (np. „wszystkie → wypełnione"). Henrich: to odejmuje intuicyjności.

**Zmiana:** wartość jest widoczna zawsze, niezależnie od hoveru. Hover przestaje zamieniać tekst w tym miejscu (inne efekty hover z v14 — tło na chrome, ramka na odpowiedziach — zostają bez zmian, to osobna funkcja).

**Dotyczy:**
- `app/state.js` — funkcja `ustawWartosc()` przestaje liczyć/wypisywać tekst „→ następna" do `.wartosc-podglad`.
- `template.html` — elementy `<span class="wartosc-podglad">` (6 wystąpień).
- `style/sheet.css` — reguły `.wartosc-podglad` i hoverowa zamiana display (`@media (hover: hover) { .sidebar-ustawienie:hover .wartosc / .wartosc-podglad }`).

**Archiwizacja:** usuwany kod (CSS + fragment JS odpowiedzialny za tekst podglądu) trafia do nowego pliku `issues/archiwum-hover-podglad.md` — krótki opis + wycięty kod, na wypadek gdyby ktoś chciał do tego wrócić. W miejscu usunięcia w kodzie zostaje krótki komentarz odsyłający do tego pliku. Model wdrażający dobiera formę odnośnika (i ew. dopisanie referencji w innych plikach .md), byle była jasna ścieżka powrotna do usuniętego kodu.

## 2. Kontrolki odpowiedzi na telefonie: layout pionowy

**Problem:** na wąskim ekranie treść zadania/etykieta i kontrolka odpowiedzi (pole liczbowe „ostateczna odpowiedź"/fill-in, przyciski P/F) stoją obok siebie w jednym wierszu — kontrolka zabiera stałą szerokość, treści zostaje za mało miejsca i się ściska/łamie nieczytelnie (zgłoszone dla zad. 10 i zdań P/F).

**Zmiana (tylko na wąskim ekranie, media query — desktop bez zmian):**
- Treść/etykieta i kontrolka przechodzą z układu poziomego (obok siebie) na pionowy: treść na górze, kontrolka pod spodem, każda na swojej linii.
- Kontrolka pod spodem ma mniejszy margines z lewej (żeby nie była wyśrodkowana sztywno, tylko bliżej lewej krawędzi jak treść nad nią) i jest lekko przesunięta w prawo / ma mniejszy margines z prawej niż domyślne wyśrodkowanie by dawało.

**Dotyczy:** `.fill-in-row`, `.final-answer-row`, `.pf-row` (i analogiczne kontenery) w `style/responsive.css` pod istniejącym breakpointem telefonu — dokładne progi pikselowe i wartości marginesów dobiera model wdrażający, patrząc na realny wygląd na telefonie (zad. 10 to dobry przypadek testowy).

## 3. Dark mode: filtr CSS dla obrazków i wideo zadań

**Problem:** PNG z CKE i MP4 z Manima mają nieprzezroczyste białe tło — w dark mode świecą na biało na karcie o ciemnym tle (`issues/dark-mode-obrazki-wideo.md`, dotąd nienaprawione).

**Zmiana:** filtr CSS na `.question img` i `<video>` w trybie dark, oparty na **odwróceniu kolorów** (świadomie zaakceptowany kompromis: kolorowe elementy na obrazku — np. czerwone/niebieskie linie na wykresach — wyjdą w zamienionych, nienaturalnych barwach; w zamian tło przestaje razić bielą).

**Punkt startowy do wyliczenia (nie do ślepego wpisania na sztywno):** żeby biel tła obrazka po odwróceniu wylądowała na tym samym poziomie szarości co `--bg` karty w dark mode (`#141414`, jasność ≈ 8%), procent odwrócenia to `100% − jasność(--bg wyrażona w %)` ⇒ start ok. **92%** odwrócenia (nie 100%). Model wdrażający ma:
1. policzyć dokładną wartość startową tym wzorem z aktualnej `--bg`,
2. sprawdzić empirycznie na realnym obrazku z arkusza (np. `matura/*/media/zad*/*.png`) w przeglądarce (Playwright/`tools/zrzuty.js`),
3. dostroić (ew. dołożyć `brightness`/`contrast`, jeśli samo odwrócenie nie wygląda dobrze) tak, żeby całość spójnie pasowała do ciemnego motywu.

**Dotyczy:** nowa reguła w dark-mode sekcji `style/base.css` lub `style/sheet.css` (obok istniejącego `--canvas-bg: #fff`, który zostaje bez zmian — to świadomie białe tło widgetów, nie dotyczy tego punktu) celująca w `.question img` i elementy `<video>` w kroku rozwiązania.

## Poza zakresem

- Docelowy re-render grafik/wideo u źródła (osobny, większy temat — TODO.md → DLA HENRICHA, poza tą paczką).
- Jakiekolwiek zmiany w mechanizmie hover tła/ramki z v14 (etap 2 spójności UI) — zostaje bez zmian, temat 1 dotyczy wyłącznie tekstu wartości.
