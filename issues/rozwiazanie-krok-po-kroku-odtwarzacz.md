# Odtwarzacz „krok po kroku" na stronie: pułapki podglądu i weryfikacji

Opis działania, nie problem do naprawy. Rzeczy, które kosztowały czas przy pracy
nad odtwarzaczem i których nie widać z samego kodu.

Zakres: **strona**, czyli `app/steps.js` i to, co widzi uczeń w przeglądarce.
Robienie samych filmów (render, sekcje, rewersy) opisuje
[manimations/README.md](../manimations/README.md). Jak odtwarzacz jest zbudowany:
`ARCHITECTURE.md`, hasło `solutionStepByStep`. Test automatyczny: `tools/test-krokow.js`.

## `python3 -m http.server` nie umie przewijać wideo

`SimpleHTTPRequestHandler` **nie obsługuje żądań zakresowych** (`Range`), a bez nich
przeglądarka nie ma jak skoczyć w środek filmu: `video.seekable` zostaje puste
(`seekable.end(0) === 0`), każde ustawienie `currentTime` cicho wraca do zera, a film
daje się tylko odtworzyć od początku.

Wygląda to dokładnie jak błąd w kodzie odtwarzacza i raz już nim nie było
(2026-08-11, sporo straconego czasu). Do wszystkiego, co przewija film (kropki, rewersy),
używaj [tools/serwer.js](../tools/serwer.js):

```
node tools/serwer.js 8000
```

Sprawdzenie: `curl -s -o /dev/null -w "%{http_code}" -r 0-100 <url-filmu>` ma zwrócić
**206**, nie 200. Ten sam skrypt umie dławić łącze (`--wolno=<ms> --bps=<bajty/s>`,
tylko na plikach wideo) i bez tego cała klasa błędów jest niewidoczna, bo na localhoście
krok podmienia się w milisekundach. Hosting Range obsługuje, więc produkcji to nie dotyczy.

## Odtwarzanie 4× gubi klatki

Zmierzone w Chromium: plik 720p120 przy 4× gubi 218 klatek z 720 (dekoder musi przerobić
480 kl./s) i kończy w 0,59 s zamiast 0,50. Przy 60 fps tego nie ma. Przy 1× i 0,25×
czas zgadza się co do setnej sekundy, gubi się 6 klatek.

Uznane za akceptowalne, bo 4× to tryb „przewiń", nie „oglądaj". Pomiar robiony
w kontenerze, na procesorze desktopowym; **telefon i Safari nie były sprawdzone**.

## Z pierwszej kropki nie da się cofnąć

Krok 1 rysuje działanie od zera, więc jego rewers kończy się pustym kadrem. Cofnięcie
z kropki 0 prowadziłoby do stanu „nic nie ma", dlatego jest zablokowane (decyzja
Henricha, 2026-08-11). To nie jest błąd rewersów ani odtwarzacza.

## Jak weryfikować, żeby nie dać się oszukać

- **Zrzut ekranu z Playwrighta potrafi kłamać przy wideo.** Ten sam zakończony film raz
  pokazywał się poprawnie, raz bez wykładnika, raz jako pusty kadr. To kwestia momentu
  malowania obrazu, nie zawartości pliku.
- **Wiarygodny jest odczyt pikseli**: `drawImage(video)` na `<canvas>` plus `getImageData`,
  i liczenie ciemnych pikseli oraz ich prostokąta obejmującego. Idzie przez JavaScript,
  z pominięciem kompozytora obrazu.
- **Miej wzorzec spoza przeglądarki.** Odczyt pikseli mówi, CO widać, ale nie mówi, czy to
  właściwa klatka. Wyciągnij tę samą klatkę z pliku (`ffmpeg -vf "select=eq(n\,K)"`)
  i porównaj liczbę ciemnych pikseli oraz ich prostokąt. Tak wyszło 2026-08-11, że
  kliknięcie ostatniej kropki pokazuje PIERWSZĄ klatkę ostatniego kroku: odtwarzacz
  raportował 3354 ciemne piksele w prostokącie (466, 310, 813, 409), a plik miał
  w ostatniej klatce 1557 w (594, 309, 685, 410). Bez wzorca „coś się wyświetla"
  wyglądałoby poprawnie.
- **Do porównania dwóch wersji filmu**: `ffmpeg -lavfi ssim`. Poziom szumu samej kompresji
  to około 0,9996, dopiero wyraźnie niżej oznacza różnicę w treści. SSIM nie mówi GDZIE
  jest różnica, więc dochodzi obejrzenie najgorszej klatki w powiększeniu.
- **Zanim porównasz cokolwiek**, sprawdź `ffprobe`, czy oba pliki mają te same wymiary
  i liczbę klatek. Inaczej „porównanie" przejdzie na niewłaściwym materiale.

## Skrypty Playwrighta

Pułapki wspólne dla całej strony (ukryty szablon zadania, przewijanie przed kliknięciem,
obowiązkowy `NODE_PATH`) zebrane są w [playwright-podglad.md](playwright-podglad.md).
Odtwarzacz ma własny test losowy: `tools/test-krokow.js`, puszczany na szybkim
i na zdławionym serwerze.
