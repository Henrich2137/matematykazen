# Hosting na Cloudflare (Worker ze statycznymi plikami)

Jak strona jest wdrażana na Cloudflare, co robi każdy z dołożonych plików i co
Henrich musi kliknąć u siebie. Zrobione 2026-08-22, po pierwszym nieudanym
wdrożeniu.

GitHub Pages **zostaje bez zmian** i jedzie z tego samego repozytorium
równolegle. Cloudflare to druga witryna tych samych plików, pod własną domeną.

## Stan na 2026-08-22: domena działa

| adres | hosting | gałąź |
|---|---|---|
| `matematykazen.pl` oraz `www.matematykazen.pl` | Cloudflare | `main` |
| `henrich2137.github.io/matematykazen/` | GitHub Pages | `dev` |

Domena kupiona u rejestratora **hitme**, przepięta na serwery nazw Cloudflare i
podpięta do Workera; certyfikat HTTPS wystawił Cloudflare sam. Obie postacie
adresu, z `www` i bez, prowadzą do tej samej strony. Henrich potwierdził
2026-08-22 z przeglądarki, że oba adresy działają, a stary adres na GitHub Pages
dalej stoi obok i jedzie z `dev`.

**Każdy hosting jedzie z innej gałęzi i to jest celowe.** `dev` to warsztat:
każdy push widać po chwili na GitHub Pages i tam się testuje. `main` to wersja
oficjalna pod domeną, aktualizowana dopiero wtedy, gdy Henrich uzna wersję za
dopracowaną, przez `git merge --ff-only dev`. Praktyczny wniosek dla asystenta:
sam push na `dev` **nie** zmienia niczego pod `matematykazen.pl`, więc prosząc o
sprawdzenie zmiany, podaj adres GitHub Pages. Układ gałęzi opisuje sekcja „Git"
w [CLAUDE.md](../CLAUDE.md).

Uwaga przy sprawdzaniu z devcontainera: `curl` na domenę kończy się tam
przeterminowaniem połączenia, bo firewall kontenera przepuszcza tylko wybrane
adresy. To **nie** jest dowód, że strona nie działa. Sprawdzaj z przeglądarki
poza kontenerem.

## Dlaczego Worker, a nie Pages

Cloudflare ma dwa produkty do hostowania stron: starsze **Pages** i nowsze
**Workers** z obsługą plików statycznych. Dla nowych projektów Cloudflare sam
kieruje do Workers: Pages dostaje już tylko poprawki błędów, rozwój idzie w
Workers. Dla naszej strony (same pliki, zero kodu serwerowego) różnica w
praktyce jest żadna, więc wybrany został wariant, który będzie rozwijany.

## Czemu w ogóle trzeba było cokolwiek dokładać do repo

Cloudflare potrafi wdrożyć repozytorium bez ani jednego pliku konfiguracyjnego:
`wrangler` sam zgaduje ustawienia. Pierwsze wdrożenie 2026-08-22 tak właśnie
poszło i padło:

```
✨ Read 484 files from the assets directory /opt/buildhome/repo
✘ [ERROR] Asset too large.
  We found a file /opt/buildhome/repo/.git/objects/pack/pack-….pack
  with a size of 27.7 MiB.
```

Zgadywanie ustawiło katalog z plikami na korzeń repozytorium i próbowało wysłać
na hosting **historię gita**, która jest większa niż limit 25 MiB na plik. To nie
jest błąd Cloudflare, tylko skutek zgadywania: automat nie wie, że `.git`,
`done/` czy `zrzuty/` to warsztat, a nie strona.

## Cztery pliki w korzeniu i po co są

| plik | co robi |
|---|---|
| `wrangler.jsonc` | ustawienia wdrożenia: nazwa Workera, katalog z plikami (korzeń repo), obsługa nieznanych adresów |
| `.assetsignore` | lista tego, czego NIE wysyłać (składnia jak `.gitignore`); to on rozwiązuje błąd powyżej |
| `_headers` | nagłówki HTTP: bezpieczeństwo dla wszystkiego, tydzień pamięci podręcznej dla `vendor/` |
| `404.html` | własna strona „nie ma takiej strony"; działa też na GitHub Pages |

Piąty plik to test: [tools/sprawdz-cloudflare.py](../tools/sprawdz-cloudflare.py).

### `assets.directory` = korzeń repo

Nie ma etapu budowania, więc nie ma katalogu wynikowego typu `dist/`. Pliki
źródłowe **są** stroną. Konsekwencja: odsiew rzeczy roboczych musi się odbyć
przez `.assetsignore`, bo inaczej pod domeną wylądowałaby cała kuchnia projektu.

Alternatywą byłoby kopiowanie plików strony do `dist/` skryptem przy każdym
wdrożeniu. Odrzucone: to jest system budowania tylnymi drzwiami, a projekt
świadomie żadnego nie ma.

### Czego `.assetsignore` NIE wycina

Trzy rzeczy, które kuszą, żeby je wyrzucić, a nie wolno:

- **`matura/*/odpowiedzi.pdf`** - panel „zasady oceniania" otwiera ten PDF
  prosto ze strony (`meta.zasadyPdf`).
- **`tablica-wzorow.pdf`** - to samo, panel tablicy wzorów.
- **`widgets/`** - kod zamknięty licencyjnie, ale strona bez niego nie działa.
  Do czasu, aż powstaną konta i płatności, widżety jadą tak samo jak reszta.
  Blokada i tak wymaga hostingu z logowaniem, a nie pominięcia pliku przy
  wysyłce: strona jest statyczna, więc wszystko, co wyślemy, trafia do
  przeglądarki ucznia.

Wycinane są za to ekstrakty `matura/*/*.txt` (są dla modeli, nie dla ucznia),
cały Markdown, `tablica-wzorow-transkrypt/`, `done/`, `issues/`, `docs/`,
`tools/`, `zrzuty/`, `manimations/` i konfiguracja narzędzi.

Odnośnik „Licencja" w stopce prowadzi do `LICENSE.md` **na GitHubie**, więc
wycięcie Markdownu nie urywa wymaganej informacji o licencji.

### `not_found_handling: "404-page"`

Bez tego nieznany adres pokazuje surowy komunikat Cloudflare. Z tym pokazuje
nasze `404.html`.

`404.html` jest celowo samowystarczalne: własne style w środku pliku, zero
odnośników do `style/` czy `app/`. Powód jest praktyczny. Hosting podstawia tę
stronę pod dowolny adres, także zagnieżdżony (`/matura/cos/tam/`), więc ścieżki
względne prowadziłyby w pustkę, a ścieżki od korzenia (`/style/base.css`)
działałyby na domenie, ale nie na GitHub Pages, gdzie strona siedzi w
podkatalogu. Ta sama historia dotyczy odnośnika powrotnego, dlatego poprawia go
trzylinijkowy skrypt na dole pliku.

### `_headers`

Nagłówki bezpieczeństwa dla całej strony plus jeden wyjątek na pamięć podręczną:
`vendor/` (KaTeX i czcionki) może leżeć w przeglądarce tydzień, bo te pliki są
przypięte do wersji.

Reszta, a zwłaszcza `exercises.json` i filmy, zostaje przy domyślnym zachowaniu
Cloudflare, czyli przeglądarka za każdym razem pyta, czy plik się zmienił.
Świadomy wybór: poprawka w zadaniu albo przerenderowany film mają być widoczne
od razu. Tak było z filmem do zad. 2 z 2024-grudnia (błędne 5⁻⁴ poprawione
2026-08-11) - gdyby stary plik leżał w przeglądarkach na miesiąc, uczniowie
mieliby błąd w kadrze mimo poprawki.

## Test: `tools/sprawdz-cloudflare.py`

Odtwarza przemarsz wranglera po repozytorium i sprawdza trzy rzeczy: limity
Cloudflare (25 MiB na plik, 20 000 plików), brak plików roboczych w wysyłce i
obecność wszystkiego, czego strona potrzebuje w przeglądarce.

Trzeci punkt jest najważniejszy, bo najłatwiej tu o cichą szkodę: `.assetsignore`
napisany za grubo wycina plik, bez którego strona się sypie, i nikt tego nie
zauważy aż do ucznia.

```
python3 tools/sprawdz-cloudflare.py           # cicho, gdy dobrze
python3 tools/sprawdz-cloudflare.py --lista   # wypisz wszystko, co pojedzie
```

Przebieg z 2026-08-22: przed dołożeniem `.assetsignore` skrypt zgłasza 160
błędów, w tym tę samą paczkę gita, na której padło wdrożenie; po dołożeniu:
„Na Cloudflare pojedzie 237 plików, razem 28.7 MB. Wszystko się zgadza".

Potwierdzone też prawdziwym wranglerem (nie tylko naszym skryptem):

```
npx --yes wrangler@4.125.0 deploy --dry-run
```

bez `.assetsignore` kończy się `✘ [ERROR] Asset too large`, a z nim przechodzi
czysto. **Uwaga na mylącą linijkę** `✨ Read 505 files from the assets
directory`: to liczba obejrzanych plików przed odsiewem, nie liczba wysyłanych.
Nie zmienia się po zmianie `.assetsignore` i nie jest powodem do niepokoju.

## Co klikał Henrich (zrobione 2026-08-22)

1. **Serwery nazw domeny na Cloudflare.** W panelu rejestratora (hitme) trzeba
   wskazać serwery nazw podane przez Cloudflare. Domena zostaje kupiona tam,
   gdzie jest; zmienia się tylko to, kto odpowiada na pytanie „gdzie stoi ta
   strona". Bez tego kroku Worker żyje wyłącznie pod adresem
   `matematykazen.workers.dev`, bo własną domenę da się podpiąć tylko wtedy, gdy
   jest obsługiwana przez Cloudflare.
2. **Podpięcie domeny do Workera**: Worker → Settings → Domains & Routes → Add
   custom domain. Certyfikat HTTPS Cloudflare wystawia sam.
3. **Wdrożenia z GitHuba** są już podpięte (Workers Builds). Polecenie
   wdrożeniowe `npx wrangler deploy` zostaje bez zmian, teraz tylko czyta nasz
   `wrangler.jsonc` zamiast zgadywać. Ustawienia z panelu („Detected Project
   Settings") przestają mieć znaczenie.

## Do zrobienia teraz, gdy domena ruszyła

Linia `Required Notice:` w `LICENSE.md` wskazuje dziś na GitHub Pages i jest
**kopiowana przez każdego, kto rozpowszechnia kod**, więc nie może prowadzić w
martwy adres. Gdy docelowa domena zacznie działać, trzeba ją tam wpisać. To jest
jeden z dwóch świadomych placeholderów opisanych w
[licencja-i-cla.md](licencja-i-cla.md); zmiana idzie w parze z resztą tamtej
listy, nie na własną rękę.

Warto też wtedy przemyśleć, czy GitHub Pages ma dalej stać obok domeny (dwa
adresy z tą samą treścią to dla wyszukiwarek duplikat), ale to temat na osobno.
