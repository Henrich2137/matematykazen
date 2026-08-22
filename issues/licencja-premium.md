# Rozdział licencyjny: `widgets/` jako treść premium

Opis konstrukcji, nie problem. Zrobione 2026-08-20. Otwórz, gdy dotykasz `LICENSE.md`,
`widgets/LICENSE.md`, nagłówków w plikach widżetów albo gdy zastanawiasz się, gdzie
położyć nowy plik. Sąsiedni plik [licencja-i-cla.md](licencja-i-cla.md) opisuje starszą
warstwę (PolyForm + CLA) i dalej obowiązuje.

## Po co to jest

Widżety mają w przyszłości trafić do płatnego planu (Faza 3 w OVERVIEW.md). PolyForm
Noncommercial tego nie zabezpiecza: zabrania zarabiania, ale **wprost pozwala
rozpowszechniać kopie w celach niekomercyjnych** (sekcja „Distribution License"
w połączeniu z „Noncommercial Purposes"). Czyli ktoś mógłby postawić darmową kopię
widżetów i byłby w porządku wobec licencji. To zabija paywall równie skutecznie
jak piractwo, więc widżety musiały wyjść spod PolyForma.

## Jak to jest poskładane

Wzorzec jest standardowy (open core). Formuła w głównym `LICENSE.md` jest
wzorowana na tej, której używa GitLab dla katalogu `ee/`.

| Plik | Rola |
|---|---|
| `LICENSE.md` | PolyForm Noncommercial na całą resztę + **blok „Zakres / Scope"** nad tekstem licencji i notka po polsku pod nim, obie wyłączające `widgets/` |
| `widgets/LICENSE.md` | pełny tekst licencji zastrzeżonej, **dwujęzyczny**: polski wiążący, angielskie streszczenie informacyjne |
| `widgets/*.js` | cztery linijki nagłówka SPDX na samej górze każdego pliku |
| `README.md`, `CONTRIBUTING.md`, `widgets/README.md`, `ARCHITECTURE.md`, `CLAUDE.md` | opis podziału dla ludzi i dla modeli |

**Tekst PolyForma nie został tknięty ani w jednym znaku.** Dopiski siedzą przed nim
i za nim. `LICENSE.md` ma zakończenia linii CRLF (tak przyszedł ze strony PolyForma)
i trzeba je zachować, inaczej diff pokazuje przepisanie całego pliku i wygląda to
jak przeredagowanie licencji.

## Dlaczego bez daty i hasha commita

Bo licencja obowiązuje **per zdjęcie repozytorium**: kto bierze kod na danym commicie,
podlega temu, co w tym commicie jest w plikach licencji. Historia gita sama odpowiada
na pytanie „co obowiązywało kiedy", więc wpisywanie daty ani hasha do treści licencji
niczego nie dodaje. Żaden z dużych projektów (GitLab, Mattermost, Elastic) tego nie robi.

Konsekwencja, o której trzeba pamiętać: **wersje widżetów opublikowane przed
2026-08-20 zostają na PolyForm na zawsze**, razem z prawem do robienia z nich dzieł
pochodnych. Zamknięcie działa tylko w przód. Nie da się tego cofnąć i nie ma sensu
próbować.

Z tego samego powodu **nie przepisuj historii na `dev` ani `main`** (żadnego `squash`,
`rebase` ani `force-push` po tej zmianie). Historia jest dowodem na to, kiedy
i co zostało ogłoszone.

## Przeniesienie hydrauliki poza `widgets/`

`widgets/_helpers.js` → `app/widget-helpers.js`, `widgets/_registry.js` →
`app/widget-registry.js` (2026-08-20). Powód: granica licencyjna musi biec **po
katalogach**, a te dwa pliki są potrzebne, żeby darmowa część strony w ogóle działała.
Gdyby zostały w `widgets/`, zamknięcie katalogu wyłączyłoby darmową stronę.

Efekt uboczny, sam w sobie dobry: zniknęły nazwy zaczynające się od `_`, które kiedyś
wywróciły stronę na GitHub Pages (Jekyll pomija pliki od podkreślnika, patrz
[zadania-nie-renderuja-sie-mobile.md](zadania-nie-renderuja-sie-mobile.md); `.nojekyll`
nadal jest w repo i nadal jest potrzebny).

Kolejność ładowania w `template.html` się nie zmieniła, tylko ścieżki:
`app/widget-helpers.js` → 20 plików `widgets/*.js` → `app/widget-registry.js` →
reszta `app/*.js`. To znaczy, że **dwa pliki z `app/` ładują się poza wspólnym blokiem
`app/*.js`** i tak ma być. Kto to „posprząta", zsuwając wszystkie tagi `app/` razem,
dostanie ciche „brak widżetu" albo `WIDZETY is not defined`.

## Zasada na przyszłość (najważniejsze zdanie w tym pliku)

**W `widgets/` wolno kłaść wyłącznie same pliki `widget*.js`.** Wszystko, czego
potrzebuje darmowa część strony (pomocniki, rejestry, konfiguracja, style, narzędzia,
dane arkuszy), idzie do `app/`, `style/`, `tools/` albo `matura/`.

Powód: wszystko, co leży w `widgets/`, znika z darmowej wersji w dniu, w którym
katalog pojedzie za paywall. Jeden wspólny plik wciągnięty tam przez nieuwagę wyłącza
darmową stronę i nikt tego nie zauważy aż do wdrożenia.

Drugi obowiązek: **każdy nowy plik w `widgets/` dostaje nagłówek SPDX** (cztery linijki,
skopiuj z dowolnego istniejącego widżetu). Bez niego skopiowany pojedynczy plik
wygląda na niczyj, a to właśnie te pliki najłatwiej skopiować pojedynczo.

## Czego ta zmiana świadomie NIE robi

- **Nie jest paywallem.** Strona jest statyczna, więc każdy plik widżetu i tak ląduje
  w przeglądarce każdego odwiedzającego. Licencja daje podstawę do żądania usunięcia
  kopii (DMCA), a nie techniczną blokadę. Prawdziwy paywall wymaga serwera, który nie
  wysyła pliku, dopóki ktoś nie zapłaci (Cloudflare Workers, Netlify, Vercel, VPS).
  GitHub Pages tego nie umie, a jego regulamin i tak zabrania hostować tam płatnego
  serwisu.
- **Nie rusza `exercises.json`.** Podpowiedzi i rozwiązania opisowe zostają na
  PolyForm, bo w jednym pliku siedzą wymieszane: treści CKE, treści darmowe
  i przyszłe premium. Rozdzielenie ich do osobnego `matura/<id>/premium.json` to
  osobne zadanie (jest w TODO.md) i warto je zrobić, zanim treści premium powstaną.
- **Nie zmienia CLA.** `CONTRIBUTING.md` już daje właścicielowi prawa również
  komercyjne, więc przyszła zmiana licencji nie jest zablokowana prawami
  kontrybutorów. Dodane zostało tylko zdanie uprzedzające, że `widgets/` jest zamknięty.
- **Nie naprawia rejestru.** `app/widget-registry.js` wymienia funkcje widżetów po
  nazwie, więc bez katalogu `widgets/` wywala się na `ReferenceError` i zabiera ze sobą
  całą stronę. Dopóki oba katalogi jadą razem, nic się nie dzieje; przy pierwszym
  wdrożeniu bez widżetów trzeba to uodpornić (wpis w TODO.md).

## Placeholder do domknięcia przed sprzedażą

Właściciel występuje pod pseudonimem `Henrich2137` (patrz
[licencja-i-cla.md](licencja-i-cla.md)). Przy darmowym projekcie to drobiazg, przy
płatnym przestaje nim być: do dochodzenia praw przed sądem albo w zgłoszeniu DMCA
potrzebne są prawdziwe dane. Do przemyślenia, zanim ruszy pierwsza sprzedaż.
