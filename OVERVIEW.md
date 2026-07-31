# Matematyka Zen

Platforma do nauki matematyki pod maturę podstawową (CKE), inspirowana Brilliant.org. Dla maturzystów, a w przyszłości może też dla ósmoklasistów. Bez reklam, minimalistyczny UI. Faza: demo/MVP — statyczna strona, bez hostingu, bez backendu i kont użytkowników (postęp trzymany lokalnie w przeglądarce).

Zobacz na żywo: brak jeszcze publicznego hostingu — sklonuj repozytorium i odpal dowolnym serwerem statycznym (np. `npx serve`).

## Arkusze maturalne

- **2024 grudzień (próbna)** — kompletny: wszystkie 30 zadań, podpowiedzi, rozwiązania (tekst + wideo krok po kroku), 9 interaktywnych widżetów, odpowiedzi zweryfikowane z oficjalnym kluczem CKE.
- **2026 maj** — wpięty jako same zadania z odpowiedziami do sprawdzenia; bez podpowiedzi, rozwiązań, wideo i widżetów.
- **2025 maj** — jeszcze niewpięty: same PDF-y arkusza i klucza, bez danych na stronie.

## Funkcje

- Dwa typy zadań: zamknięte (ABCD, prawda/fałsz, wielokrotny wybór, uzupełnianie) oceniane automatycznie na bieżąco, oraz otwarte — bez automatycznej oceny, rozwiązywane poza platformą i oceniane przez ucznia samodzielnie (patrz samoocena niżej).
- Tablica wzorów (oficjalny PDF CKE) w przesuwnym, skalowalnym okienku.
- Zasady oceniania (klucz odpowiedzi CKE) w analogicznym, osobnym okienku.
- Tryb próbnego egzaminu — 170 min z zegarem, ukrywa podpowiedzi/wyniki na czas trwania, podsumowanie po zakończeniu.
- Samoocena zadań otwartych: rozwiązanie na kartce → porównanie z modelowym rozwiązaniem → ocena punktowa przez użytkownika.
- Wskaźniki zadań czekających na samoocenę (po egzaminie).
- Zgłaszanie błędu w zadaniu wprost pod nim (formularz z kategoriami, bez opuszczania strony).
- Motyw jasny / ciemny / auto.
- Panel boczny z ustawieniami (natychmiastowa poprawność vs. „sprawdź później", widoczność punktacji, itd.).
- Postęp i ustawienia zapisywane lokalnie (bez konta, bez serwera).

## Model biznesowy

Freemium: treści z oficjalnych arkuszy CKE — bazowo za darmo; treści własne (plan na przyszłość) — płatne.

## Notatki robocze — utrzymywane przez Claude web (projekt „Matematyka Zen" na claude.ai)

- **W planach:** hosting, konta użytkowników, backend/płatności — na razie żadnego z tych nie ma (czysty statyczny MVP). Docelowo freemium: arkusze CKE zawsze darmowe, treści własne płatne.
- **Uwagi i pomysły z zewnątrz:** na razie brak dedykowanego kanału (poza „zgłoś błąd" pod każdym zadaniem, który dotyczy tylko konkretnego zadania) — do ustalenia w miarę rozwoju projektu.
