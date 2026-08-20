Ostatnia weryfikacja  20.08.2026 

# Matematyka Zen

Platforma do nauki matematyki pod maturę podstawową (CKE), inspirowana Brilliant.org. Dla maturzystów, a w przyszłości może też dla ósmoklasistów. Bez reklam, minimalistyczny UI. Obecnie projekt jest w Fazie 1. „Budowa" z rozpiski niżej — strona jest już publicznie dostępna na GitHub Pages , ale bez marketingu i bez własnej domeny; ładna domena (np. matematykazen.pl) i szukanie zainteresowania to dopiero Faza 2. Nadal statyczna, bez backendu i kont użytkowników (postęp trzymany lokalnie w przeglądarce).

Zobacz na żywo: https://henrich2137.github.io/matematykazen/

## Arkusze maturalne

**2024 grudzień (próbna)** - kompletny:
- Zadania (osobne karty): 33 (30 poleceń CKE, część z podpunktami), 50 pkt
- Podpowiedzi: 33/33
- Rozwiązania opisowe: 31/33 (zad. 1 i 2 mają samo wideo)
- Rozwiązania wideo (krok po kroku): 9/33 (zadania 1-9)
- Widżety interaktywne: 9 (nie 1:1 z zadaniami, nie każde tego wymaga)
- Zadania otwarte z kryteriami CKE: 7/7
- Odpowiedzi zweryfikowane z kluczem CKE: tak

**2026 maj (właściwa)** - w opracowaniu:
- Zadania (osobne karty): 37 (33 polecenia CKE, część z podpunktami), 50 pkt
- Podpowiedzi: 14/37
- Rozwiązania opisowe: 14/37
- Rozwiązania wideo (krok po kroku): 0/37
- Widżety interaktywne: 13
- Zadania otwarte z kryteriami CKE: 8/8
- Odpowiedzi zweryfikowane z kluczem CKE: tak

Treść wszystkich 33 zadań i odpowiedzi jest już wpięta, więc arkusz da się przeklikać w całości.
Komplet (podpowiedź + rozwiązanie opisowe + widżet) mają zadania 2, 8, 10, 11, 12, 13, 14, 19, 20, 26 i 33.
Rysunki z arkusza są wycięte i wstawione we wszystkie zadania, które ich wymagają.

**2025 maj (właściwa)** - niewpięty:
- Zadania: 0 (same PDF-y arkusza i klucza, bez `exercises.json`)
- Na stronie głównej się nie pojawia.

### Jak liczymy te statystyki (zasada)

Liczby wylicza skrypt **`tools/statystyki.py`** wprost z danych arkusza, żeby nikt nie musiał
liczyć ręcznie ani zgadywać:

```
python3 tools/statystyki.py            # wszystkie arkusze
python3 tools/statystyki.py 2026-maj   # jeden arkusz
python3 tools/statystyki.py --braki    # dodatkowo: numery zadań, w których czegoś brakuje
```

Definicje (źródłem prawdy jest skrypt, ta sekcja tylko przepisuje wynik):
- **Zadanie** = jedna punktowana karta w `exercises.json`. Wiązka typu „Zadanie 12." z podpunktami
  12.1 i 12.2 to trzy wpisy, ale tylko dwa zadania, bo nagłówek wiązki nie ma punktów.
- **Podpowiedź / rozwiązanie opisowe / rozwiązanie wideo / widżet** = odpowiednie pole zadania
  jest niepuste.
- **Widżety** liczone są jako liczba różnych widżetów w arkuszu, nie jako ułamek zadań: nie każde
  zadanie da się (i warto) zilustrować interaktywnie.
- **Odpowiedzi zweryfikowane z kluczem CKE** - odpowiedzi do zadań zamkniętych zostały porównane
  z oficjalnymi zasadami oceniania (`odpowiedzi.pdf`).

**Zasada aktualizacji:** po każdej porcji pracy nad arkuszem puść skrypt i przepisz liczby tutaj
(razem z datą na górze pliku). To jedno polecenie, więc nie ma powodu, żeby ta sekcja się rozjeżdżała.

## Funkcje

- Dwa typy zadań: zamknięte (ABCD, prawda/fałsz, wielokrotny wybór, uzupełnianie) oceniane automatycznie na bieżąco, oraz otwarte — rozwiązywane poza platformą, punktowane przez ucznia z checklisty kryteriów CKE (patrz samoocena niżej).
- Rozwiązania „krok po kroku": krótkie animacje matematyczne (Manim) odtwarzane stan po stanie. Pod filmem pasek kropek — kropka to stan działania, film to przejście między dwoma stanami — z paskiem postępu w odstępie między kropką bieżącą a następną. Kropki są klikalne, krok da się cofnąć (osobny plik puszczony od tyłu, bo przeglądarki nie odtwarzają wideo wstecz), prędkość regulowana od 0,25× do 4×, obsługa przesuwaniem palca i strzałkami klawiatury. Wyjaśnienie kroku (opis + wzór) chowa się pod przyciskiem, żeby widok domyślny był minimalistyczny.
- Tablica wzorów (oficjalny PDF CKE) w przesuwnym, skalowalnym okienku.
- Zasady oceniania (klucz odpowiedzi CKE) w analogicznym, osobnym okienku.
- Tryb próbnego egzaminu — 170 min z zegarem, ukrywa podpowiedzi/wyniki na czas trwania, podsumowanie po zakończeniu.
- Samoocena zadań otwartych: rozwiązanie na kartce → porównanie z modelowym rozwiązaniem → rozwijana checklista „Sprawdzanie obliczeń" z kryteriami z oficjalnych zasad oceniania CKE; zaznaczenie kryterium od razu dolicza jego punkty do wyniku zadania (checklista jest domyślnie zwinięta, żeby nie zdradzać rozwiązania).
- Przy każdym zadaniu otwartym miejsce na notatki oraz pole „ostateczna odpowiedź" sprawdzane automatycznie.
- Wskaźniki zadań czekających na samoocenę (po egzaminie).
- Zgłaszanie błędu w zadaniu wprost pod nim (formularz z kategoriami, bez opuszczania strony).
- Motyw jasny / ciemny / auto — razem z motywem przełączają się też interaktywne widżety (ciemne płótno, jasne osie i opisy).
- Panel boczny z ustawieniami (natychmiastowa poprawność vs. „sprawdź później", widoczność punktacji, itd.). Pozycje niedostępne w danym trybie nie znikają, tylko szarzeją — panel nie skacze. Na telefonie zwija się też przeciągnięciem palcem w lewo.
- Postęp i ustawienia zapisywane lokalnie (bez konta, bez serwera).

## Ścieżka biznesowa

+ Faza 1 - Budowa (obecna) - Beta testy ale bez marketingu i domeny co czyni je bardziej zamkniętymi.

+ Faza 2 - Soft Launch i Beta testy - Marketing, naprawa zgłaszanych błędów, zbieranie pieniędzy na patronite.
    - Hosting: nadal GitHub Pages (2.1) DONE
    - Licencja PolyForm Noncommercial (2.2) DONE
    - Domena matematykazen.pl (2.3)
    - Hosting: np Cloudflare / Netlify
    - Aplikacja-wrapper?
    - Odpicowanie stronki, "wyczyszczenie" repo aby friendly dla ludzi którz se je pobiorą
    
Cel: zdobyć zainteresowanie i sprawdzić, czy projekt przyjmie się w społeczności.


Faza 3 - Rozwidlenie
- Marketing
W zależności od przychodów z dotacji oraz liczby użytkowników wybiorę jedną z dwóch ścieżek:

- ALBO: Freemium
    - Bardziej zamknięta licencja
    - Handover do profesjonalnego web deva
    - Paywall. Autorskie zadania za abonamentem

- ALBO: Open-source
    - Otwarta licencja
    - Rozwijanie wraz ze społecznościa opensourcową
    - Brak paywalla
    - Przychód z dotacji (np. suppi.pl)





## Licencja

Kod i treści autorskie: **PolyForm Noncommercial 1.0.0** (użytek wyłącznie niekomercyjny; licencja komercyjna do uzgodnienia mailowo). Zadania i klucze CKE nie są objęte tą licencją. Kontrybutorzy przy wysyłaniu Pull Requesta zgadzają się na przekazanie właścicielowi projektu szerokiej licencji na swój wkład (również komercyjnej), zachowując prawo do własnego wkładu — dzięki temu przyszła zmiana licencji (Faza 3) nie będzie zablokowana.

## Numer wersji w rogu strony (zasada robocza)

Obok logo widnieje numer wersji („v12 Beta"). Jest podbijany ręcznie przy każdym oddaniu pracy do testów i **służy wyłącznie fazie demo**: po odświeżeniu na telefonie od razu widać, czy przeglądarka wczytała już nową wersję, czy pokazuje wersję z cache'u. Zasada: przed przekazaniem czegokolwiek do sprawdzenia podbij numer, zacommituj i wypchnij na `origin` — inaczej testowana jest stara strona.

**Do skasowania (albo zamiany na prawdziwe wersjonowanie) w momencie rozpowszechniania strony.** Uczniowi numer wersji w rogu nic nie mówi, a sugeruje produkt niegotowy.

## Notatki robocze — utrzymywane przez Claude web (projekt „Matematyka Zen" na claude.ai)

- **Uwagi i pomysły z zewnątrz:** „zgłoś błąd" pod każdym zadaniem (dotyczy tylko konkretnego zadania) oraz — od 02.08.2026 — issues i Pull Requesty na GitHubie, opisane w CONTRIBUTING.md. Kanał publiczny, ale jeszcze nierozreklamowany.