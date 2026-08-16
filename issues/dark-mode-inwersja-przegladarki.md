# Dark mode: odwracanie kolorów grafik/wideo nie działa tak samo we wszystkich przeglądarkach

Status: OTWARTE. Zgłoszone przez Henricha 2026-08-11 przy odbiorze paczki UI v15.
Mechanizm, który testujemy: `--filtr-grafik-zadan` (style/base.css, oba ciemne
bloki) nakładany na `.question img` oraz img/video w `.solution-step-by-step-container`
(style/sheet.css:610, 1185, 1242).

**Aktualizacja 2026-08-16:** filtr to teraz `invert(92%) hue-rotate(180deg)`, a nie samo
`invert(92%)`. Dołożony obrót odcienia sprawia, że odwraca się sama jasność (niebieski zostaje
niebieski). **Dla tego zgłoszenia nic się nie zmienia**: obrót o 180° nie rusza szarości, więc
biel z pliku dalej ląduje dokładnie na `rgb(20,20,20)`, cała arytmetyka „92%" niżej zostaje
w mocy, a Problem A (tło grafiki ≠ tło strony na Bazzite/Samsungu) dotyczy tak samo obu wersji.
Wszystkie rekomendacje niżej zostają bez zmian.

## Co zgłosił Henrich

| Przeglądarka | Wynik |
|---|---|
| Firefox, desktop (Bazzite) | ✅ tip-top |
| Chrome / Brave, desktop (Bazzite) | ❌ odwrócenie działa, ale odwrócona biel jest JAŚNIEJSZA niż tło karty — widać prostokąt |
| Firefox, telefon (GrapheneOS / Pixel 7a) | ✅ tip-top |
| Chrome, telefon | ✅ tip-top |
| Samsung Internet, telefon | ❌ wymusza własny ciemny motyw mimo ustawionego jasnego, tło czarne, nasze odwrócenie w ogóle nie działa |

To są DWA różne problemy z dwiema różnymi przyczynami — nie da się ich naprawić jedną zmianą.

## Doprecyzowanie od Henricha (2026-08-10)

- Na Chrome/Brave **jaśniejsze jest tło CAŁEJ strony**, nie tylko prostokąt grafiki. To
  przesuwa winę z warstwy filtra (hipoteza 3) na zarządzanie kolorem całego okna (hipoteza 2).
- **Wariant 3 (biel → przezroczystość) odpada.** Powód: jeśli odwracanie nie zadziała albo
  przeglądarka wciśnie własny motyw, przezroczyste grafiki dadzą ciemne kreski na ciemnym tle
  (albo jasne na jasnym) — czyli treść zniknie. Białe tło w PNG jest tu zabezpieczeniem.
- **Zamiana barw to nie problem.** Treści zadań CKE nie niosą znaczenia w kolorze (m.in. ze
  względu na daltonistów), więc kompromis „bez hue-rotate" zostaje świadomie i na stałe.
- Tak, **wideo też jest odwracane** — `filter: var(--filtr-grafik-zadan)` siedzi na
  `.solution-step-by-step-container video` (style/sheet.css:1185), obok obrazków (610, 1242).

## Problem A: Chrome/Brave na desktopie — prostokąt jaśniejszy od tła

**Sama matematyka filtra jest poprawna i identyczna w Chromium.** Sprawdzone empirycznie
2026-08-11: headless Chromium 1234 (ta sama wersja co w kontenerze), biały `<div>` z
`filter: invert(92%)` na tle `#141414` → piksel wychodzi dokładnie `rgb(20,20,20)`, czyli
zlewa się co do jednego bitu. Czyli winne jest coś, co zmienia biel ŹRÓDŁA, zanim filtr ją
policzy — a nie sam filtr.

Hipotezy, od najbardziej prawdopodobnej:

- **1. Wideo bez otagowanego zakresu kolorów (`color_range`) — najmocniejszy trop.**
  `ffprobe` na plikach z Manima: `pix_fmt=yuv420p`, `color_range=unknown`,
  `color_space/transfer/primaries = unknown`. Przy braku tagu każda przeglądarka sama zgaduje,
  czy 16–235 rozciągnąć do 0–255, czy nie — i Firefox z Chrome zgadują INACZEJ. Jeśli biel
  w wideo dojdzie do filtra jako np. 245 zamiast 255, to po `invert(92%)` wychodzi `rgb(29)`
  zamiast `rgb(20)` — czyli dokładnie „jaśniejszy prostokąt".
  **CZĘŚCIOWO OBALONE 2026-08-11:** pierwsza klatka `zad1rozw_step1.mp4` wyciągnięta ffmpegiem
  ma biel dokładnie `rgb(255,255,255)` (cała klatka to jeden kolor), a `zad10rys.png` też ma
  czystą biel 255. Czyli same pliki są w porządku i ffmpeg zgaduje zakres dobrze. Hipoteza
  zostaje żywa tylko o tyle, że BRAK tagu nadal pozwala Chrome zgadnąć inaczej niż ffmpeg
  i Firefox — otagowanie jest tanie i usuwa całą klasę problemu, ale to już nie jest
  „na pewno to".
- **2. Zarządzanie kolorem (ICC / szeroki gamut / HDR) na desktopie.** Chrome kolor-manageuje
  zawartość do profilu monitora, Firefox na Linuksie domyślnie w sporej części nie. PNG-i zadań
  mają chunk `sRGB` + `gAMA` (sprawdzone: `zad10rys.png`, `zad11.png`), więc Chrome je
  przelicza. Pasuje do tego, że problem jest TYLKO na desktopie z Bazzite, a na telefonie
  Chrome działa dobrze.
- **3. Warstwy GPU.** `filter` wypycha element na osobną warstwę kompozytora; przy rasteryzacji
  GPU-owej bywa ona kolor-managowana inaczej niż tło malowane bezpośrednio. Mój test był
  z `--disable-gpu` i wyszedł czysto, co tej hipotezie nie przeczy.

## Problem B: Samsung Internet — własny wymuszony ciemny motyw

Samsung Internet ma tryb ciemny, który **algorytmicznie przemalowuje stronę po swojemu**,
niezależnie od tego, co strona deklaruje — dlatego widać ciemne tło mimo wybranego u nas
jasnego motywu, i dlatego nasz filtr „nie działa" (obraz przechodzi jeszcze przez ich warstwę).
Henrich zauważył przy tym, że tło jest tam **czarne**, a nie nasze `#141414` — czyli Samsung
nadpisuje nawet `--bg`, co potwierdza, że przemalowuje gotowy render, a nie czyta naszego CSS-a.
Mamy już `color-scheme: light` / `dark` w base.css (linie 37, 170, 269), ale **nie mamy
`<meta name="color-scheme">` w `<head>`** template.html — to jedyny tani strzał, jaki tu
zostaje, i nie ma gwarancji, że pomoże.

Wniosek do przełknięcia: **żadna poprawka po stronie CSS nie da nam kontroli nad tą
przeglądarką.** Jedyne, co jest na nią odporne, to grafiki, które nie mają białego tła
u źródła.

## Warianty naprawy

| # | Wariant | Naprawia A | Naprawia B | Koszt |
|---|---|---|---|---|
| 1 | Otagować wideo (`-color_range pc/tv`, `-colorspace bt709`) przy re-enkodowaniu | ✅ (jeśli hipoteza 1 trafiona) | ❌ | 🟨 mały, ale trzeba przepuścić wszystkie MP4 przez ffmpeg |
| 2 | `invert(100%)` zamiast `92%` + własne czarne tło pod grafiką | 🟨 częściowo — 100% nie ma interpolacji szarości, więc jest odporne na hipotezę 3, ale nie na 1 i 2 | ❌ | ✅ jedna linijka |
| 3 | ~~Usunąć białe tło z PNG-ów (biel → przezroczystość)~~ | — | — | ❌ **ODRZUCONE 2026-08-10** — bez białego tła grafika znika, gdy odwracanie zawiedzie lub przeglądarka narzuci swój motyw |
| 4 | Osobne warianty grafik na ciemny motyw (`<picture>` + `media="(prefers-color-scheme: dark)"`) | ✅ | 🟨 (Samsung i tak przemaluje, ale start jest ciemny) | ❌ podwaja pliki, trzeba pilnować spójności |
| 5 | Re-render z Manima z przezroczystym/ciemnym tłem, wideo jako WebM z alfą | ✅ | ✅ | ❌ duży — wymaga zewnętrznego re-renderu (jest już taki dług: zad2 step6) |
| 6 | `<meta name="color-scheme" content="light dark">` w `<head>` | ❌ | 🟨 strzał, do przetestowania | ✅ jedna linijka |

## Rekomendacja

- **Brakująca diagnostyka (tylko Henrich może ją zrobić — to jego maszyna).** Otworzyć arkusz
  w Chrome/Brave na Bazzite w ciemnym motywie, zrobić zrzut ekranu i sprawdzić pipetą DWIE
  wartości: tło karty obok grafiki i wnętrze grafiki. Jeśli tło karty ≠ `rgb(20,20,20)` —
  winne jest zarządzanie kolorem całej strony (hipoteza 2). Jeśli tło karty = 20, a grafika
  jaśniejsza — winna jest warstwa filtra (hipoteza 3). Bez tego wybieramy wariant w ciemno.
- **Krótka ścieżka (dziś):** wariant 6 (jedna linijka, test na Samsungu) + wariant 1
  (otagowanie wideo jest tanie i nic nie psuje, nawet jeśli nie to jest przyczyną).
- **Docelowo:** wariant 5 — re-render z Manima z ciemnym tłem jako osobne pliki na ciemny
  motyw (albo wariant 4, jeśli re-render jest za drogi). To jedyna droga, która nie zależy od
  tego, jak przeglądarka policzy filtr, a jednocześnie NIE zostawia grafiki bez własnego tła
  (patrz odrzucony wariant 3). Do czasu re-renderu zostajemy przy `invert(92%)`.

### Diagnostyka Problemu A — do wykonania w Chrome/Brave na Bazzite

Trzy uruchomienia, każde rozstrzyga jedną rzecz (po każdym: czy strona nadal jest jaśniejsza?):

```
brave --force-color-profile=srgb        # wymusza sRGB → jeśli znika, winne zarządzanie kolorem/profil monitora
brave --disable-gpu                     # jeśli znika, winna rasteryzacja/kompozycja GPU
brave --disable-features=WebContentsForceDark   # jeśli znika, winny „Auto Dark Mode" w chrome://flags
```
- **Czego NIE robić:** nie dobierać `invert()` metodą prób i błędów pod konkretną przeglądarkę.
  Liczba 92% jest wyliczona poprawnie i w Chromium działa co do bitu — kręcenie nią naprawi
  jedną przeglądarkę i zepsuje drugą.
