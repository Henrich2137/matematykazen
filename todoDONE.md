W tym pliku będę zapisywał błędy oraz sugestie znalezione w wyniku smoke testu

ZROBIONE (2026-07-04):
- [DONE] Punkt nie cofał się po złej odpowiedzi → naprawione. Usunięto flag isScoreGiven; każde zadanie ma earnedScore (0 albo maxScore), a updateTotalScore() przelicza sumę od zera. Zła odpowiedź daje 0 / X pkt i zeruje earnedScore.
- [DONE] Kruche porównywanie odpowiedzi po stringu HTML → naprawione. Dane używają teraz correctAnswerIndex (0=A, 1=B, ...; -1 = otwarte/niewypełnione), a ocena to i === correctIndex. Cały exercises.js zmigrowany.
- [DONE] defaultPlaybackRate na oderwanym tempDiv → naprawione. renderStep() zwraca czysty string, a showStep() ustawia defaultPlaybackRate i playbackRate = 0.1 na realnym.
- [DONE] Pozostałe porządki Fazy 1 (usunięcie martwego kodu, scalenie listenerów .solution-button, deklaracje globali, przeniesienie)

ZROBIONE (2026-07-04, sesja 2 — uzupełnienie arkusza + interaktywność):
- [DONE] Uzupełnione wszystkie zadania: poprawne odpowiedzi (correctAnswerIndex), podpowiedzi, rozwiązania (solutionText + solutionTextMore) i strony tablic (formulasPage) dla zadań 1-20; treści 7-20 zweryfikowane z obrazkami zadN/ (cropami z arkusza).
- [DONE] BŁĄD MERYTORYCZNY zad 2: (⁵√5 · ⅕)⁻⁵ = 5⁴, czyli odpowiedź A, nie B. Dane poprawione; klatka końcowa filmiku step6 nadal pokazuje 5⁻⁴ (patrz niżej: do przerenderowania).
- [DONE] Poprawka rozwiązania zad 3 (było "2⁴ + 2² + 2⁹⁶" w nawiasie, ma być "2⁴ + 2² + 1 = 21") oraz podpowiedzi zad 6 (była skopiowana podpowiedź o logarytmach z zad 4).
- [DONE] Nowe typy zadań w silniku: PF (prawda/fałsz z przyciskami P/F przy każdym stwierdzeniu), multiSelect (np. zad 12.2 — wybór dwóch wzorów, punkty częściowe), open z samooceną (selfScore: true → przyciski 0..maxScore pkt; realizuje flow "rozwiąż na kartce i oceń się" z CLAUDE.md).
- [DONE] 9 widżetów interaktywnych (solutionInteractive): zad 1 (oś liczbowa z przeciąganym punktem i strzałkami odległości — realizuje pomysł z sekcji "było by idealnie"), zad 5 (procent składany — suwak p i słupki kapitału; naprawia martwe rysujWykresEksponencjalny), zad 9 (parabola nierówności z przedziałem rozwiązań), zad 10 (wykres przedziałami z podświetlanym wzorem), zad 12.1 (monotoniczność paraboli), zad 15 (ciąg arytmetyczny — suwak m i różnice), zad 18 (koło trygonometryczne z przeciąganym kątem), zad 20 (kąt wpisany/środkowy z przeciąganym C), zad 30 (optymalizacja prostokąta).
- [DONE] maxTotalScore liczone automatycznie z sumy maxScore (nie trzeba już synchronizować ręcznie).
- [DONE] zad17.PNG → zad17.png (wielkość liter psuła obrazek na hostingu case-sensitive, np. GitHub Pages).
- [DONE] Przycisk "Podpowiedź" chowa się, gdy zadanie nie ma podpowiedzi.
- [DONE] Zaznaczenie tekstu jasnoniebieskie bez zmiany koloru tekstu (::selection) — z sekcji "było by idealnie".
- [DONE] Krok filmu bez komentarza dostaje wypełniacz "· · ·" (.step-comment:empty) — z sekcji "było by idealnie".
- [DONE] Migotanie przy przełączaniu stepów zmniejszone: film następnego kroku jest preloadowany (preload="auto") w showStep().
- [DONE] Spacer <br><br><br><br> pod paskiem zastąpiony paddingiem #exercises-wrapper (gotcha z CLAUDE.md).
- [DONE] Zadania 23-30 (wymyślone przez ChatGPT, odwołujące się do nieistniejących obrazków zad23-29) zastąpione spójnymi zadaniami 21-31 w stylu CKE bez obrazków; brakujące grafiki przestały być problemem.

ZROBIONE (2026-07-05, sesja 3 — oryginalne zadania 21-30 + strona główna):
- [DONE] Zadania 21-30 podmienione na ORYGINAŁY z arkusza CKE (treści i klucz odpowiedzi wklejone przez autora; wszystkie odpowiedzi przeliczone i zgodne z kluczem). Suma punktów arkusza = 50 pkt — zgadza się z oficjalną, co potwierdza też punktację zadań otwartych 8 (3 pkt), 10 (4 pkt), 19 (4 pkt).
- [DONE] Zweryfikowane z kluczem zadania 18 (A), 19 (22,14), 20 (B) — były poprawne.
- [DONE] Widżet zad 30 przerobiony z prostokąta na prostopadłościan z arkusza (P(x) = −26x² + 96x, dziedzina (0,3), maksimum x = 24/13) — widgetProstopadloscian.
- [DONE] Strona główna index.html (przeniesiona z gałęzi claude/practical-rubin-t7g7ya, style .landing-* w style.css) + logo w arkuszu jest teraz linkiem do index.html.
- [DONE] Tabelka danych zad 29 jako HTML (.data-table), nie obrazek.




Sugestie WYGLĄD / DESIGN:

ZROBIONE WYGLĄD/DESIGN (2026-07-04):
- [DONE] "pokaż więcej" za bardzo przyklejone do lewej → .solution-text-more ma teraz padding 0 40px, treść odsunięta od krawędzi.
- [DONE] Zbędny separator pod rozwiązaniem tylko-tekstowym → loadExercises() zdejmuje border-bottom z ostatniego widocznego bloku rozwiązania (na podstawie hasText/hasSteps/hasInteractive/hasMore).
- [DONE] Przycisk "Pokaż/Schowaj tablice wzorów" zmieniał szerokość → #toggle-tablica ma min-width: 200px.
- [DONE] Skakała wysokość diva step-by-step → podpis kroku owinięty w .step-comment (min-height ~2 linijki), .steps-content min-height 250px; wysokość stała do ~2 linijek komentarza.
- [DONE] Litery A, B w przyciskach na dole → vertical-align: middle na przyciskach i obrazkach w nich (bez flexa, żeby nie zepsuć sup/sub).
- [DONE] Grafika w zad 10 nierówna / przesunięta w prawo → .question img jako blok wyśrodkowany; inline obrazek w zad2 nadpisany display:inline-block.
- [DONE] Przycisk "Rozwiązanie" tylko gdy istnieje jakiekolwiek rozwiązanie → loadExercises() chowa .solution-button, gdy brak tekstu/kroków/interaktywnego/"pokaż więcej".
- [DONE] Klik w filmik zatrzymuje/wznawia + ikonka ▶ gdy zatrzymany → mała .video-overlay-icon w lewym dolnym rogu (nie na środku, nie zasłania filmu).
- [DONE] Pasek postępu filmu → cienki (2px) szary .video-progress-bar aktualizowany w timeupdate, płynne przejście width (pełny = skończony).
- [DONE] Krzyżyk zamykający tablicę wzorów → #tablica-close (✕) w prawym GÓRNYM rogu #tablica-wzorow-panel, chowa panel przez schowajTablice().

Uwaga: wyśrodkowanie liter A/B w odpowiedziach jest w style.css (ogólne, wszystkie zadania), nie w exercises.js. Zmiana w exercises.js dotyczyła tylko grafiki w treści zad2.




Byłoby idealnie:
- [DONE 2026-07-04] zad 2 (=zad 1?) > interactiveSolution: przesuwanie punktu na osi liczbowej + strzałki od środka — zrealizowane w widgetOsLiczbowa (zad 1).
- [DONE 2026-07-04] zaznaczenie jasnoniebieskie bez białego tekstu (::selection).
- [DONE 2026-07-04] gdyby nie było tekstu/komentarza pod video to pojawia się wypełniacz "· · ·" w jego miejsce.