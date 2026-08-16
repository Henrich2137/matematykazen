# Dark mode: odwracanie kolorów grafik/wideo nie działa tak samo we wszystkich przeglądarkach

Status: PROBLEM A najprawdopodobniej ZAMKNIĘTY (przyczyna poza stroną), problem B otwarty.
Zgłoszone przez Henricha 2026-08-11 przy odbiorze paczki UI v15.

**Rozstrzygnięcie Problemu A (Henrich, 2026-08-16):** niedopasowanie tła grafik do tła strony
brało się z samej maszyny, czyli z Bazzite i Waylanda, a nie ze strony. Na Windowsie wszystko
wygląda poprawnie. To zgadza się z hipotezą 2 niżej (zarządzanie kolorem całego okna) i z tym,
co Henrich doprecyzował już 2026-08-10: jaśniejsze było tło CAŁEJ strony, nie sam prostokąt
grafiki. **Wniosek: nic w kodzie tego nie naprawi i nie ma czego naprawiać.** Rekomendacje
niżej (otagowanie wideo, `<meta name="color-scheme">`) zostają jako tanie porządki, ale nie są
już lekarstwem na zgłoszony objaw. Gdyby ktoś chciał to domknąć twardo, brakuje jednego
pomiaru z Bazzite: pipetą sprawdzić tło karty obok grafiki — jeśli nie jest `rgb(20,20,20)`,
sprawa jest przesądzona.

Mechanizm, który testujemy: `--filtr-grafik-zadan` (style/base.css, oba ciemne
bloki) nakładany na `.question img` oraz img/video w `.solution-step-by-step-container`
(style/sheet.css:610, 1185, 1242).

**Aktualizacja 2026-08-16:** filtr to teraz `invert(92%) hue-rotate(180deg)`, a nie samo
`invert(92%)`. Dołożony obrót odcienia sprawia, że odwraca się sama jasność (niebieski zostaje
niebieski). **Dla tego zgłoszenia nic się nie zmienia**: obrót o 180° nie rusza szarości, więc
biel z pliku dalej ląduje dokładnie na `rgb(20,20,20)`, cała arytmetyka „92%" niżej zostaje
w mocy. Doszedł natomiast NOWY objaw, opisany jako Problem C na końcu pliku.

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
  względu na daltonistów), więc kompromis „bez hue-rotate" był świadomy.
  **NIEAKTUALNE od 2026-08-16:** rysunki CKE faktycznie nic nie tracą, ale filmy z Manima owszem
  — w nich zielony znaczy „poprawne" (COLORS.md), a stary filtr robił z niego róż. Stąd v49
  i dołożone `hue-rotate(180deg)`.
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

**UWAGA: ta sekcja powstała, gdy Problem A uchodził za usterkę strony.** Po rozstrzygnięciu
z 2026-08-16 (przyczyna w środowisku Bazzite/Wayland, na Windowsie wszystko gra) żaden z tych
wariantów nie jest już potrzebny do naprawy rozjechanych szarości. Zostawione, bo Problem B
(Samsung) jest otwarty, a warianty 1 i 6 są tanie same z siebie.

- ~~**Brakująca diagnostyka.**~~ Odpowiedź już jest: to maszyna, nie strona. Zostaje tylko
  opcjonalne twarde potwierdzenie pipetą (opis na górze pliku).
- **Nadal tanie i sensowne same z siebie:** wariant 6 (jedna linijka, strzał w Samsunga)
  i wariant 1 (otagowanie wideo, usuwa całą klasę niejednoznaczności przy dekodowaniu).
- **Warianty 4 i 5 (osobne pliki na ciemny motyw) schodzą z listy pilnych.** Były jedyną drogą
  niezależną od tego, jak przeglądarka policzy filtr — a filtr okazał się liczony dobrze wszędzie
  tam, gdzie środowisko nie majstruje przy kolorze całego okna.
- Zostajemy przy `invert(92%) hue-rotate(180deg)`.

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


## Problem C: Firefox na Bazzite nie zawraca odcienia (zgłoszone 2026-08-16)

Po v49, w której filtr dostał `hue-rotate(180deg)`, Henrich sprawdził komplet maszyn:

| Maszyna / przeglądarka | Wynik |
|---|---|
| Windows | ✅ wszystko gra |
| Pixel 7a (GrapheneOS), Chrome | ✅ |
| Pixel 7a (GrapheneOS), Firefox | ✅ |
| Bazzite, Chrome | ✅ |
| Bazzite, **Firefox** | ❌ wygląda jak stary, goły `invert` — jakby obrotu odcienia nie było |
| Bazzite, Samsung Internet | ❌ białe tło i odwrócony odcień; przeglądarka świadomie odpuszczona |

To jest objaw **zerojedynkowy**, a nie przesunięcie barw. Zarządzanie kolorem czy profil
monitora potrafią kolory przesunąć, ale nie potrafią sprawić, że jedno z dwóch działań filtru
w ogóle nie zadziała. Dlatego kolejność sprawdzania jest taka:

1. **Numer wersji w rogu strony.** Ma być ten sam co w `template.html`. Starszy = Firefox podał
   stary arkusz stylów z pamięci i nie ma żadnej zagadki. Naprawa: `Ctrl+Shift+R`.
2. **`about:support`, wiersz o kompozycji.** Firefox na Linuksie bywa zrzucany z karty
   graficznej na procesor przez sterowniki, a to jest dokładnie ta warstwa, która liczy filtry.
   Bazzite jest dystrybucją pod granie, więc ma nietypowy zestaw sterowników — a ten sam Firefox
   na telefonie działa, co ładnie pasuje do tej hipotezy.
3. **Profil koloru ekranu i HDR.** Najmniej prawdopodobne z powodu opisanego wyżej, ale HDR
   na dystrybucji do grania bywa włączony domyślnie i warto go wykluczyć.

**Czego NIE robić:** nie dobierać filtru pod Firefoksa na jednej maszynie. Ta sama przeglądarka
na telefonie i ta sama strona na Windowsie działają poprawnie, więc problem jest w środowisku,
nie w regule CSS.
