---
name: ogladanie-krokow
description: >
  Użyj, gdy trzeba obejrzeć wyrenderowany film „krok po kroku" z manimations/:
  po każdym renderze albo przerenderowaniu sceny, przed powiedzeniem „gotowe",
  przy sprawdzaniu, czy animacja pokazuje to, co miała, oraz gdy
  tools/styk-klatek.sh albo tools/zielen-krokow.py zgłosi zastrzeżenie i trzeba
  zobaczyć, na czym ono polega. Użyj też, gdy użytkownik prosi „zobacz, jak to
  wyszło", „sprawdź ten film", „obejrzyj krok N". Nie używaj do zrzutów ekranu
  strony (to tools/zrzuty.js) ani do pisania scen (to manimations/README.md).
---

# Oglądanie filmów krok po kroku

Nie widzisz plików `.mp4` - to dla Ciebie ciąg bajtów. Widzisz obrazki PNG. Jedyna
droga do obejrzenia animacji prowadzi więc przez zamianę wideo na klatki, i robi to
**[tools/klatki.sh](../../../tools/klatki.sh)**.

**„Wyrenderowało się bez błędu" nie znaczy nic.** Manim kończy z kodem 0 także wtedy, gdy
glif poleciał w złą stronę, zieleń została zapalona na czymś nie tym, dwa napisy nachodzą
na siebie, a ostatnia klatka nie zgadza się z pierwszą klatką następnego kroku. To są
dokładnie te usterki, których automaty z `tools/` nie złapią, bo one liczą piksele, a nie
patrzą na sens.

## Czego na klatkach NIE zobaczysz

Powiedz to wprost, zamiast udawać, że sprawdziłeś:

- **Płynności ruchu.** Klatki to przystanki, nie jazda. Czy coś szarpie albo jedzie
  nierówno, ocenia człowiek w przeglądarce.
- **Tego, czy tempo jest DOBRE.** Ile co trwa, owszem, zmierzysz - kafelki są podpisane
  czasem, a postoje mają swój znacznik. Ale „0,5 s bezruchu" to liczba, nie ocena; czy to
  za długo dla ucznia, wie Henrich, nie Ty.
- **Zachowania odtwarzacza.** Przewijanie, rewersy, przeskoki między krokami sprawdza
  [tools/test-krokow.js](../../../tools/test-krokow.js), nie obrazek.

## Trzy tryby i kiedy który

| tryb | co pokazuje | kiedy sięgasz |
|---|---|---|
| `stany` | pierwsza i ostatnia klatka **każdego** kroku, czytelnie | **domyślnie, po każdym renderze** - jeden obrazek na całe zadanie |
| `film` | jeden krok jako sekwencja, widać ruch | **tylko** gdy `stany` pokaże, że coś jest nie tak w konkretnym kroku |
| `styk` | para klatek na złączu + podbita różnica | gdy `styk-klatek.sh` zgłosi liczbę poniżej progu |

**`stany` jest tani i wystarcza w większości przypadków, więc rób nim całą bieżącą pracę
nad sceną**, nie tylko odbiór końcowy: po każdym przerenderowaniu jeden `stany --koniec`
na całe zadanie mówi, czy rachunek idzie poprawnie od pierwszego wiersza do ostatniego,
czy nic nie zostało zielone na klatce brzegowej i czy styk kroków się zgadza. Jeden obrazek,
koszt jednej klatki.

**Trybu `film` NIC nie wymaga.** Nie ma zasady „po każdym renderze obejrzyj krok w ruchu"
(stała w `manimations/README.md` do 2026-08-30 i została zdjęta): płaciło się kontekstem
za obrazki, które prawie zawsze potwierdzały to, co już było widać w `stany`. Po `film`
sięgasz, gdy masz konkretne pytanie o ruch, na które `stany` nie odpowiada.

```
tools/klatki.sh stany matura/<arkusz>/media/zadN/solution-step-by-step
tools/klatki.sh stany <katalog> --koniec          # same stany spoczynkowe, o połowę taniej
tools/klatki.sh film  <katalog> 7 --co 20         # DOMYŚLNIE: rzadziej, za to kafelek duży
tools/klatki.sh film  <katalog> 7 --co 6          # gęsto: tylko gdy oceniasz sam RUCH
tools/klatki.sh styk  <katalog> 3                 # złącze kroku 3 z krokiem 4
```

Skrypt wypisuje ścieżkę powstałego pliku. Otwierasz go zwykłym **Read** - i dopiero wtedy
naprawdę patrzysz, zamiast zgadywać z kodu sceny.

## Jak czytać kratkę z trybu `film`

Kafelki idą **od lewej do prawej, wierszami**, i każdy ma dwa oznaczenia:

- **Żółty podpis w lewym górnym rogu to czas w filmie w milisekundach**, a nie numer po
  kolei. To jest istotne: bezruch jest odsiewany, więc sąsiednie kafelki nie muszą dzielić
  równego odstępu. Skok w tych liczbach (np. `1800ms` obok `2250ms`) znaczy, że między nimi
  obraz stał.
- **Pomarańczowy pasek „bezruch +0.45s" na dole kafelka** mówi to samo wprost i siedzi na
  kafelku, na którym obraz **staje**. Ta treść wisi przez ten czas na ekranie ucznia.

Ta sama lista przerw leci na konsolę, więc widać ją jeszcze przed otwarciem obrazka.

**Po co Ci to.** Bez tych oznaczeń kratka kłamie - dwa kafelki obok siebie wyglądają jak
ciąg ruchu, a naprawdę dzieli je pół sekundy postoju. Przerwa w środku kroku bywa
sygnałem, że krok robi dwie rzeczy zamiast jednej: coś się dzieje, zastój, dzieje się
druga rzecz. Wtedy sprawdź w scenie, czy to nie materiał na dwa kroki.

Odstępu czasu **nie mylić z oceną tempa** - że coś stoi 0,5 s, widzisz; czy to za długo,
nie. Zobacz sekcję wyżej.

## Kolejność, w której to robisz

1. **`stany --koniec`** na całym zadaniu. Jeden obrazek, cały tok rozwiązania. Czytasz go
   jak zapis na tablicy: czy rachunek idzie poprawnie od pierwszego wiersza do ostatniego.
2. Coś nie gra w kroku N → **`film <katalog> N`**. Widzisz, co się dokąd rusza.
3. `styk-klatek.sh` zgłosił parę → **`styk <katalog> N`**, plus liczba `najjaśniejszy piksel
   różnicy`, którą skrypt wypisuje. Kilka jednostek to szum kodera H.264 i nic więcej;
   kilkadziesiąt rozłożone po całej linii to też szum na krawędziach glifów; jasna plama
   w jednym miejscu to realny rozjazd i wtedy jest co poprawiać.

## Na co patrzysz (zasady domowe, nie ogólne)

Pełne brzmienie w [manimations/README.md](../../../manimations/README.md) i
[COLORS.md](../../../COLORS.md). Tu jest lista do odhaczenia przy oglądaniu:

- **Styk.** Ostatnia klatka kroku N wygląda tak samo jak pierwsza klatka kroku N+1. W
  odtwarzaczu to jedno i to samo miejsce, więc każda różnica to widoczny przeskok.
- **Zieleń tylko w środku.** Pierwsza i ostatnia klatka kroku mają być czyste. Zieleń
  zapala się animacją i gaśnie animacją, cała naraz - nie ratami i nie zostaje na koniec.
- **Ruch idzie za rachunkiem.** Glif ma jechać tam, gdzie idzie w działaniu. Jeśli w kadrze
  coś przelatuje na drugą stronę bez powodu, para glifów została dobrana automatem, a nie
  wskazana ręcznie.
- **Jeden krok = jedno przekształcenie.** Krok, w którym zmieniają się dwie rzeczy naraz,
  jest do rozbicia.
- **Nic na siebie nie nachodzi** i nic nie wychodzi poza kadr. Patrz szerzej niż na samo
  nachodzenie: **dwa zapisy postawione na tej samej wysokości czytają się jak jedna długa
  linijka**, nawet gdy formalnie dzieli je odstęp. To wychodzi TYLKO na klatce; w kodzie
  sceny obie współrzędne wyglądają na dobrze rozsunięte (złapane 2026-08-30 na zad. 12.2,
  gdzie dopisek \(f(0) = -9\) stanął obok \(q = 0\)).
- **Krzywa nie urywa się w powietrzu.** Wykres dochodzący dokładnie do krawędzi planszy
  kończy się wewnątrz kadru i wygląda, jakby funkcja się tam kończyła; punkt jadący po nim
  wyskakuje wtedy znikąd. Ma wychodzić POZA kadr.
- **Kolor znaczy to, co ma znaczyć.** Zieleń to „tu się zmienia", nie „to jest dobrze".

## Ile to kosztuje i jak nie przepalić kontekstu

Obrazek kosztuje mniej więcej **powierzchnia w pikselach podzielona przez 750**. Nie zależy
to od tego, ile klatek jest w środku - trzydzieści małych kafelków kosztuje tyle samo co
jedna duża klatka o tej samej powierzchni. Płaci się czytelnością: im więcej kafelków, tym
drobniejsze wzory.

Stąd pokrętło `--tokeny` (domyślnie 2000-2500). Skrypt sam dobiera wielkość kafelka pod ten
budżet, a gdy się nie mieści, dzieli wynik na strony i mówi, ile ich jest.

- **Nie oglądaj wszystkiego odruchowo.** Zacznij od jednego `stany --koniec`. Reszta tylko
  wtedy, gdy tamten obrazek da powód.
- **Nie czytaj kolejnych stron „dla porządku".** Strona 2 ma sens, gdy na stronie 1 coś
  zgrzytnęło albo gdy naprawdę oglądasz całe zadanie po dużym przerenderowaniu.
- **`film` z gęstym `--co` to najdroższy tryb pod względem czytelności**, i to jest jego
  jedyny prawdziwy koszt. Obrazek kosztuje tyle samo niezależnie od liczby kafelków, ale
  każdy kafelek jest wtedy mniejszy: przy `--co 6` wzoru w kafelku już się **nie odczyta**
  (zmierzone 2026-08-29 na zad. 7 i 10). Reguła: **`--co 20` albo rzadziej, gdy chcesz
  PRZECZYTAĆ, co jest w kadrze; gęsto tylko wtedy, gdy oceniasz sam RUCH** i treść jest
  bez znaczenia. Zaczynaj od rzadkiego i zagęszczaj dopiero, gdy rzadki nie odpowiedział.
- Bezruch (`self.wait`) jest odsiewany domyślnie, więc nie płacisz za tę samą klatkę
  powtórzoną czterdzieści razy.

## Zanim powiesz „gotowe"

Nie pisz, że film jest w porządku, jeżeli go nie otworzyłeś Read-em. Napisz, **który obrazek
obejrzałeś i co na nim widać** - tak samo jak przy testach wkleja się przebieg, a nie samo
słowo „działa".
