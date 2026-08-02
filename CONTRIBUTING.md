# Współtworzenie MatematykaZen

Cześć! Każda pomoc się liczy — od literówki w treści zadania, przez poprawkę CSS,
po nowy interaktywny widżet.

- **Błąd w zadaniu?** Najszybsza droga to formularz „zgłoś błąd" pod zadaniem na stronie.
- **Błąd w kodzie lub pomysł na funkcję?** Załóż *issue*.
- **Masz gotową poprawkę?** Wyślij Pull Request. Przy większych zmianach lepiej
  najpierw otworzyć issue, żeby nie robić pracy na marne.

## Uruchomienie lokalne

Nie ma builda ani menedżera pakietów. Strona ładuje dane przez `fetch`, więc
**nie zadziała z `file://`** — uruchom serwer statyczny w katalogu repo:

```
npx serve
```

Szczegóły architektury: [ARCHITECTURE.md](ARCHITECTURE.md) i
[ARCHITECTURE_CSS.md](ARCHITECTURE_CSS.md). Treści i komentarze piszemy po polsku,
wzory w KaTeX.

## Licencja

Projekt jest na licencji **PolyForm Noncommercial 1.0.0** — pełny tekst
w [LICENSE.md](LICENSE.md), wersja źródłowa:
<https://polyformproject.org/licenses/noncommercial/1.0.0>. Wolno używać,
modyfikować i rozpowszechniać wyłącznie w celach niekomercyjnych.

Zadania maturalne, arkusze i klucze odpowiedzi pochodzą z Centralnej Komisji
Egzaminacyjnej i **nie są objęte tą licencją**.

## Zgoda na licencjonowanie wkładu

> Przesyłając Pull Request do tego repozytorium, oświadczasz że:
> 1. masz prawo licencjonować przesłany kod/treść,
> 2. udzielasz Henrich2137, jako właścicielowi projektu
>    MatematykaZen, nieodpłatnej, nieograniczonej terytorialnie, bezterminowej
>    i nieodwołalnej licencji na wykorzystanie, modyfikowanie, dystrybucję oraz
>    komercyjne wykorzystanie Twojego wkładu — również na warunkach innych niż
>    aktualna licencja projektu (PolyForm Noncommercial),
> 3. zachowujesz pełne prawo do wykorzystania własnego wkładu gdziekolwiek indziej.
>
> Otwarcie Pull Requesta jest równoznaczne z akceptacją powyższych warunków.
