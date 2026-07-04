W tym pliku będę zapisywał błędy oraz sugestie znalezione w wyniku smoke testu

ZROBIONE (2026-07-04):
- [DONE] Punkt nie cofał się po złej odpowiedzi → naprawione. Usunięto flag isScoreGiven; każde zadanie ma earnedScore (0 albo maxScore), a updateTotalScore() przelicza sumę od zera. Zła odpowiedź daje 0 / X pkt i zeruje earnedScore.
- [DONE] Kruche porównywanie odpowiedzi po stringu HTML → naprawione. Dane używają teraz correctAnswerIndex (0=A, 1=B, ...; -1 = otwarte/niewypełnione), a ocena to i === correctIndex. Cały exercises.js zmigrowany.
- [DONE] defaultPlaybackRate na oderwanym tempDiv → naprawione. renderStep() zwraca czysty string, a showStep() ustawia defaultPlaybackRate i playbackRate = 0.1 na realnym <video>.

Pozostałe porządki Fazy 1 (usunięcie martwego kodu, scalenie listenerów .solution-button, deklaracje globali, przeniesienie <script>) — plik todoFaza1.md został usunięty; odtwórz go, jeśli chcesz przekazać tę fazę nowej sesji.



Sugestie na potem, to troche większe zadania (NIE REALIZUJ ICH JESZCZE):

- do zadań 23, 24 itd. nie wczytują się grafiki (chyba ich jeszcze nie ma)

- dodanie pól na własny tekst w zadaniach takich jak zadanie 10 w miejscach takich jak "..." i systemu sprawdzania odpowiedzi użytkownika czy pasuje chociaż do jednej wersji poprawnych odpowiedzi. Poniżej zadania powinien znajdować się przycisk sprawdź, po kliknięciu którego przy każdym z pól pojawi się oznaczenie na czerwono lub zielona w zależności od poprawności odpowiedzi. (moze być to w formie zmiany koloru ramki pola)

- dodanie strony głównej z opisem projektu i odnośnikiem do arkusza demo (tego który teraz jest stroną główną) oraz hiperłącza na logo lewy górnym rogu









Sugestie WYGLĄD / DESIGN (NIE REALIZUJ ICH JESZCZE):

- po kliknięciu "pokaż więcej" poniżej solution w formie stepbystep/interactive tekst powiniene znajdować się bardziej na środku, jest za bardzo przyklejony do lewej. Można tez zrobić tak, żeby matematyczne zapisy były wycentrowane a zwykły tekst do lewej

- dodać krzyżyk w prawym dolnym rogu przy tablicy wzorów który będzie ją wyłączał

- sprawić aby przycisk "Pokaż talblice wzorów" nie zmieniał swojej wielkości po zamienieniu sięw Schowaj tablicę wzorów

- podczas przełączania stepów w step by step solution wysokość całego diva się zmienia w zależności od ilości tekstu w komentarzu. Chciałbym, aby tak się nie działo, aby wysokość była z grubsza stała a dopiero gry komentarz przekracz np dwie linijki aby się zwiększyła. 

- pasek postępu lub jakaś ikonka obrazująca czy filmik trwa czy już się skończył

- klikanie na filmik mogłoby go zatrzymywac lub puszczać, jeżeli byłby zatrzymany mogłaby pojawić się ikonka gdzieś niżej

- brakuje rozwiązania powinien pojawić się komunikat "Nie udało się wczytać bądź nie ma jeszcze rozwiązania do tego zadania" lub w ogóle nie powinno być przycisku rozwiązanie

- literki A, B itd. czyli tekst w przyciskach odpowiedzi powinien znajdować się nie na dole ale na środku w osi pionowej.

- w zad 10 grafika jest nierówno, jest w środku tekstu i zbyt mocno przesunięta do prawej

- Jezeli rozwiąwiązanie istnieje tylko jako tekst to poniżej wyświetla się separator, który jest niepotrzebny








Sugestie o najniższym priorytecie w stylu "było by idealnie" (NIE REALIZUJ ICH JESZCZE):
- zad 2 > interactiveSolution   Sprawić aby można było przesuwać punktu na osi liczbowej a liczby na dole zmieniały się odpowiednio. Oprócz tego można dodać strzałki kóre odchodzą od -4 lub innej go punktu który, który jest po środku pomarańczowych kropek

- filmiki nie powinny migać podczas przełączania

- zaznaczenie powinno być jasnoniebieskie i nie powinno zmieniać koloru tekstu na biały, wyglądałoby spójniej, tak myślę 

- tablica-wzorów którą dało by isę "odblokować" i przesuwać dowolnie jak sie chce i zmieniać rozmiar okna

