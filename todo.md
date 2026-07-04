W tym pliku będę zapisywał błędy oraz sugestie znalezione w wyniku smoke testu

ZROBIONE (2026-07-04):
- [DONE] Punkt nie cofał się po złej odpowiedzi → naprawione. Usunięto flag isScoreGiven; każde zadanie ma earnedScore (0 albo maxScore), a updateTotalScore() przelicza sumę od zera. Zła odpowiedź daje 0 / X pkt i zeruje earnedScore.
- [DONE] Kruche porównywanie odpowiedzi po stringu HTML → naprawione. Dane używają teraz correctAnswerIndex (0=A, 1=B, ...; -1 = otwarte/niewypełnione), a ocena to i === correctIndex. Cały exercises.js zmigrowany.
- [DONE] defaultPlaybackRate na oderwanym tempDiv → naprawione. renderStep() zwraca czysty string, a showStep() ustawia defaultPlaybackRate i playbackRate = 0.1 na realnym.

- [DONE] Pozostałe porządki Fazy 1 (usunięcie martwego kodu, scalenie listenerów .solution-button, deklaracje globali, przeniesienie)



Sugestie na potem, to troche większe zadania (NIE REALIZUJ ICH JESZCZE):

- do zadań 23, 24 itd. nie wczytują się grafiki (chyba ich jeszcze nie ma)

- dodanie pól na własny tekst w zadaniach takich jak zadanie 10 w miejscach takich jak "..." i systemu sprawdzania odpowiedzi użytkownika czy pasuje chociaż do jednej wersji poprawnych odpowiedzi. Poniżej zadania powinien znajdować się przycisk sprawdź, po kliknięciu którego przy każdym z pól pojawi się oznaczenie na czerwono lub zielona w zależności od poprawności odpowiedzi. (moze być to w formie zmiany koloru ramki pola)

- dodanie strony głównej z opisem projektu i odnośnikiem do arkusza demo (tego który teraz jest stroną główną) oraz hiperłącza na logo lewy górnym rogu









Sugestie WYGLĄD / DESIGN:

DO REALIZACJI:
(wszystkie zrobione — patrz sekcja ZROBIONE WYGLĄD/DESIGN poniżej)

ZROBIONE WYGLĄD/DESIGN (2026-07-04):
- [DONE] "pokaż więcej" za bardzo przyklejone do lewej → .solution-text-more ma teraz padding 0 40px, treść odsunięta od krawędzi.
- [DONE] Zbędny separator pod rozwiązaniem tylko-tekstowym → loadExercises() zdejmuje border-bottom z ostatniego widocznego bloku rozwiązania (na podstawie hasText/hasSteps/hasInteractive/hasMore).
- [DONE] Przycisk "Pokaż/Schowaj tablice wzorów" zmieniał szerokość → #toggle-tablica ma min-width: 200px.
- [DONE] Skakała wysokość diva step-by-step → podpis kroku owinięty w .step-comment (min-height ~2 linijki), .steps-content min-height 250px; wysokość stała do ~2 linijek komentarza.
- [DONE] Litery A, B w przyciskach na dole → vertical-align: middle na przyciskach i obrazkach w nich (bez flexa, żeby nie zepsuć sup/sub).
- [DONE] Grafika w zad 10 nierówna / przesunięta w prawo → .question img jako blok wyśrodkowany; inline obrazek w zad2 nadpisany display:inline-block.

DO REALIZACJI:
(wszystkie zrobione — patrz sekcja ZROBIONE WYGLĄD/DESIGN 2 poniżej)

ZROBIONE WYGLĄD/DESIGN 2 (2026-07-04):
- [DONE] Przycisk "Rozwiązanie" tylko gdy istnieje jakiekolwiek rozwiązanie → loadExercises() chowa .solution-button, gdy brak tekstu/kroków/interaktywnego/"pokaż więcej".
- [DONE] Klik w filmik zatrzymuje/wznawia + ikonka ▶ gdy zatrzymany → .step-video z klasą .paused i nakładką .video-overlay-icon (widoczna, gdy film stoi lub się skończył).
- [DONE] Pasek postępu filmu → .video-progress / .video-progress-bar aktualizowany w timeupdate (pełny = skończony).
- [DONE] Krzyżyk zamykający tablicę wzorów → #tablica-close (✕) w prawym dolnym rogu #tablica-wzorow-panel, chowa panel przez schowajTablice().









Sugestie o najniższym priorytecie w stylu "było by idealnie" (NIE REALIZUJ ICH JESZCZE):
- zad 2 > interactiveSolution   Sprawić aby można było przesuwać punktu na osi liczbowej a liczby na dole zmieniały się odpowiednio. Oprócz tego można dodać strzałki kóre odchodzą od -4 lub innej go punktu który, który jest po środku pomarańczowych kropek

- filmiki nie powinny migać podczas przełączania

- zaznaczenie powinno być jasnoniebieskie i nie powinno zmieniać koloru tekstu na biały, wyglądałoby spójniej, tak myślę 

- tablica-wzorów którą dało by isę "odblokować" i przesuwać dowolnie jak sie chce i zmieniać rozmiar okna

