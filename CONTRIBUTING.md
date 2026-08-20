# Współtworzenie projektu Matematyka Zen

Cześć! Każda pomoc się liczy - od literówki w treści zadania, przez poprawkę CSS,
aż po nowy widżet (mini-gierka pozwalająca lepiej zrozumiec zadanie).

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

## VIBE-CODING

Projekt zaczął się na przełomie 2024/2025, to dlatego najbardziej rozwiniętym arkuszem jest 2024-grudzien. Nie korzystałem wtedy jeszcze tak bardzo z AI i wiele linijek napisałem samodzielnie. Z upływem czasu (szczególnie od lipca 2026, kiedy załóżyłem to repo) zacząłem coraz więcej vibe-code-ować. Chcę rozbudować ten projekt do stanu gdzie będzie widać czy to ma racje bytu czy nie. Jeśli miałby coś z tego być to rozważam też  przekazanie tego projektu zewnętrzenmu deweloperowi, aby został napisany jak się należy, ja skupię się wtedy na rzeczywistym projektowaniu zadań. Jeśli chodzi o finansowanie to rozważam 2 opcje: donate-y oraz model freemium (dodatkowe zadania ukryte za paywallem). Sprawdź więcej w [OVERVIEW.md](OVERVIEW.md).

## Licencja

Projekt jest na licencji **PolyForm Noncommercial 1.0.0** - pełny tekst
w [LICENSE.md](LICENSE.md), wersja źródłowa:
<https://polyformproject.org/licenses/noncommercial/1.0.0>. Wolno używać,
modyfikować i rozpowszechniać wyłącznie w celach niekomercyjnych.

**Wyjątek: katalog `widgets/`.** Interaktywne widżety rozwiązań są zastrzeżone
(wszelkie prawa zastrzeżone, [widgets/LICENSE.md](widgets/LICENSE.md)) i mają
w przyszłości trafić do płatnego planu. PolyForm ich nie obejmuje. Możesz
zgłaszać błędy w widżetach i propozycje zmian, ale zanim napiszesz do nich
większy kod, otwórz najpierw issue - żeby nie robić pracy na marne.

Zadania maturalne, arkusze i klucze odpowiedzi pochodzą z Centralnej Komisji
Egzaminacyjnej i **nie są objęte żadną z tych licencji**.

## Zgoda na licencjonowanie wkładu

> Przesyłając Pull Request do tego repozytorium, oświadczasz że:
> 1. masz prawo licencjonować przesłany kod/treść,
> 2. udzielasz Henrich2137, jako właścicielowi projektu
>    Matematyka Zen, nieodpłatnej, nieograniczonej terytorialnie, bezterminowej
>    i nieodwołalnej licencji na wykorzystanie, modyfikowanie, dystrybucję oraz
>    komercyjne wykorzystanie Twojego wkładu — również na warunkach innych niż
>    aktualna licencja projektu (PolyForm Noncommercial),
> 3. zachowujesz pełne prawo do wykorzystania własnego wkładu gdziekolwiek indziej.
>
> Otwarcie Pull Requesta jest równoznaczne z akceptacją powyższych warunków.
