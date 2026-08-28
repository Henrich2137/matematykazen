Ostatnia weryfikacja  28.08.2026

# Matematyka Zen

Platforma do nauki matematyki pod maturę podstawową (CKE), inspirowana Brilliant.org. Dla maturzystów, a w przyszłości może też dla ósmoklasistów. Bez reklam, minimalistyczny UI. Obecnie projekt jest w Fazie 2. Nadal statyczna, bez backendu i kont użytkowników (postęp trzymany lokalnie w przeglądarce).

Zobacz na żywo: **https://matematykazen.pl** (działa też z www). Wersja robocza, zwykle o krok do przodu: https://henrich2137.github.io/matematykazen/

> **Po co ten plik.** To jedyne miejsce, w którym cały projekt da się ogarnąć z lotu ptaka, bez otwierania repozytorium. Pisany jest dla Claude web (projekt „Matematyka Zen" na claude.ai), który zajmuje się stroną biznesową, planowaniem i decyzjami produktowymi, a nie dla Claude Code, który siedzi w kodzie i ma do tego pozostałe pliki repozytorium. Dlatego ma być **krótki i przejrzysty**: co jest zrobione, co strona umie i dokąd zmierza. Szczegóły techniczne (jak co działa, jak się to liczy, jak się to uruchamia) tutaj nie wchodzą, ich miejsce jest w `CLAUDE.md` i plikach obok kodu.


## Arkusze maturalne - statystyki dostępnych treści

**2024 grudzień (próbna)** - kompletny:
- Zadania (osobne karty): 33 (30 poleceń CKE, część z podpunktami), 50 pkt
- Podpowiedzi: 33/33
- Rozwiązania opisowe: 33/33
- Rozwiązania wideo (krok po kroku): 14/33 (zadania 1-12)
- Widżety interaktywne: 9 (nie 1:1 z zadaniami, nie każde tego wymaga)
- Zadania otwarte z kryteriami CKE: 7/7
- Odpowiedzi zweryfikowane z kluczem CKE: tak

Zadania 1-12 są wstępnie odpicowane (rozwiązania i filmy dopracowane wg obecnych zasad). Pozostałe zadania wymagają jeszcze przeglądnięcia i poprawek.

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


## Funkcje

- Dwa typy zadań: zamknięte (ABCD, prawda/fałsz, wielokrotny wybór, uzupełnianie) oceniane automatycznie na bieżąco, oraz otwarte — rozwiązywane poza platformą, punktowane przez ucznia z checklisty kryteriów CKE (patrz samoocena niżej).

- Rozwiązania chowają się pod przyciskiem „Rozwiązanie", żeby uczeń najpierw spróbował sam. Jedno zadanie może mieć kilka rodzajów naraz, wyświetlanych jeden pod drugim, zawsze w tej samej kolejności: najpierw film, potem tekst, na końcu widżet.
  - Krok po kroku - krótkie animacje matematyczne (Manim), jedna na przejście między dwoma stanami działania. Pod filmem klikalny pasek kropek z paskiem postępu, krok da się cofnąć, prędkość od 0,25× do 4×, sterowanie palcem i strzałkami. Opis kroku chowa się pod przyciskiem, żeby widok domyślny był minimalistyczny. To docelowo najczęstszy rodzaj rozwiązania, ale jego produkcja jest najdroższa, więc na razie ma go tylko część zadań (aktualne liczby w statystykach wyżej).
  - Zwykłe (opisowe) - rozpisany tok rozumowania, tekst ze wzorami. To podstawa, docelowo ma je każde zadanie. Całość widać od razu; dawny przycisk „Pokaż więcej", pod którym chowały się dłuższe wtręty, został usunięty w sierpniu 2026, bo dzielił jedno rozwiązanie na dwa kawałki i mało kto go rozwijał.
  - Interaktywne (widżety) -  mały rysunek do ruszania, w którym uczeń sam przesuwa tę jedną wielkość, od której zależy wynik, i widzi, jak zmienia się rachunek pod spodem. Chodzi o to, żeby odkryć przyczynę typowego błędu, a nie obejrzeć gotowy skutek. Z natury nie pasuje do każdego zadania, więc ma je tylko część.

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

+ Faza 1 - Budowa - Beta testy ale bez marketingu i domeny co czyni je bardziej zamkniętymi.

+ Faza 2 - Soft Launch i Beta testy - Marketing, naprawa zgłaszanych błędów, zbieranie pieniędzy na patronite.
    - Hosting: nadal GitHub Pages (2.1) DONE
    - Licencja PolyForm Noncommercial (2.2) - zmienione na strukture z fazy 3 (Claude, wstaw tu datę zamknięcia widgets/ jak będziesz aktualizował)
    - Branche - hostingi - domeny DONE
        - main - Cloudflare - matematykazen.pl - oficjalna wersja która będzie promowana
        - dev - GitHub Pages - https://henrich2137.github.io/matematykazen/
    - 2 doszlifowane arkusze maturalne - 2026-maj i 2024-grudzien
    
Cel: zdobyć zainteresowanie i sprawdzić, czy projekt przyjmie się w społeczności.


+ Faza 3 - Open Core Freemium
    
    - Marketing (matematykazen.pl)
    - Licencje: DONE
        - Zamknięta - widgets/
        - Otwarta Polyform Noncomertial - dla reszty

    - Maybe Handover do profesjonalnego web deva
    - Paywall. 75% Rozwiązań interaktywnych oraz autorskie arkusze za abonamentem
    - Baza danych z prawdziwego zdarzenia
    - Dotacje i tak można odpalić (np. suppi.pl)
    - Aplikacja-wrapper?
    - "wyczyszczenie" repo aby friendly dla ludzi którz se je pobiorą


## Licencja

Repozytorium ma od 20.08.2026 **dwie** licencje, bo widżety mają w przyszłości trafić do płatnego planu:

- **Kod strony i pozostałe treści autorskie** (podpowiedzi, rozwiązania opisowe, animacje): **PolyForm Noncommercial 1.0.0**, użytek wyłącznie niekomercyjny, licencja komercyjna do uzgodnienia mailowo.
- **Interaktywne widżety** (katalog `widgets/`): **wszelkie prawa zastrzeżone**, własna licencja, dwujęzyczna. Wolno je obejrzeć, nie wolno rozpowszechniać ani udostępniać publicznie, również nieodpłatnie.

Powód rozdziału: PolyForm zabrania zarabiania na cudzej treści, ale pozwala rozdawać ją za darmo, więc przy paywallu byłby bezużyteczny. Zamknięcie działa tylko w przód: wersje widżetów opublikowane wcześniej zostają na PolyForm na zawsze. Sama licencja nie jest jeszcze paywallem, bo strona jest statyczna i wszystkie pliki i tak trafiają do przeglądarki; prawdziwa blokada wymaga hostingu z logowaniem (Faza 3).

Zadania i klucze CKE nie są objęte żadną z tych licencji. Kontrybutorzy przy wysyłaniu Pull Requesta zgadzają się na przekazanie właścicielowi projektu szerokiej licencji na swój wkład (również komercyjnej), zachowując prawo do własnego wkładu, dzięki czemu przyszła zmiana licencji nie jest zablokowana.


## Dwa adresy strony

Od 22.08.2026 strona stoi w dwóch miejscach naraz, z tego samego repozytorium, ale z dwóch różnych gałęzi. Oba adresy sprawdzone i działające.

| adres | rola | co tam trafia |
|---|---|---|
| **matematykazen.pl** (i z www) | witryna oficjalna, ten adres podaje się uczniom i w marketingu | tylko wersje uznane za dopracowane |
| **henrich2137.github.io/matematykazen** | wersja robocza do testów (dawny jedyny adres) | każda bieżąca zmiana, od razu |

Domena stoi na Cloudflare, stary adres nadal na GitHub Pages. Praca w toku nie jest więc widoczna pod domeną, a jednocześnie jest gdzie obejrzeć zmianę przed pokazaniem jej światu. Wypuszczenie nowej wersji na domenę to osobna, świadoma decyzja, a nie skutek uboczny zapisania zmiany.

Do przemyślenia przy marketingu: dwa adresy z tą samą treścią wyszukiwarki traktują jak duplikat, więc warto w pewnym momencie wskazać jeden jako główny. Nie pali się.


## Numer wersji w rogu strony (zasada robocza)

Obok logo widnieje numer wersji (np „v12 Beta"). Jest podbijany ręcznie przy każdym oddaniu pracy do testów i **służy wyłącznie fazie demo**: po odświeżeniu na telefonie od razu widać, czy przeglądarka wczytała już nową wersję, czy pokazuje wersję z cache'u. Zasada: przed przekazaniem czegokolwiek do sprawdzenia podbij numer, zacommituj i wypchnij na `origin` — inaczej testowana jest stara strona. Numer pokazuje też, którą z dwóch witryn się właśnie ogląda, bo domena bywa kilka wersji za wersją roboczą.

**Do skasowania (albo zamiany na prawdziwe wersjonowanie) w momencie rozpowszechniania strony.** Uczniowi numer wersji w rogu nic nie mówi, a sugeruje produkt niegotowy.


## Notatki robocze — utrzymywane przez Claude web (projekt „Matematyka Zen" na claude.ai)

- **Uwagi i pomysły z zewnątrz:** „zgłoś błąd" pod każdym zadaniem (dotyczy tylko konkretnego zadania) oraz — od 02.08.2026 — issues i Pull Requesty na GitHubie, opisane w CONTRIBUTING.md. Kanał publiczny, ale jeszcze nierozreklamowany.