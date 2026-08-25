# Czego modelom brakuje offline, a co już mają

Przegląd zrobiony 2026-08-25 po pytaniu Henricha „czy otworzyć firewall na
dokumentację Manima". Odpowiedź brzmi: nie, i poniżej jest dlaczego.
Wniosek ogólny: **więcej problemów bierze się z tego, że model nie wie,
co ma pod ręką, niż z faktycznego braku dostępu.**

## Manim: pełne API jest lokalnie, tylko nikt o tym nie mówił

W kontenerze siedzi Manim 0.18.1 razem z kodem źródłowym
(`/usr/local/lib/python3.11/dist-packages/manim`, 163 pliki `.py`). Opisy
i listy argumentów odczytuje się bez sieci:

```sh
python3 -c "import manim, inspect; print(inspect.signature(manim.MathTex.__init__))"
python3 -c "import manim, inspect; print(inspect.getdoc(manim.TransformMatchingShapes))"
```

Sprawdzone: `MathTex` ma 682 znaki opisu, `TransformMatchingShapes` 705.
Brakuje wyłącznie **poradników i galerii przykładów** ze strony, czyli tego,
czego i tak nie da się wprost przenieść do sceny.

Przepis trafił do `manimations/README.md`, sekcja „Środowisko".

### Dlaczego nie otwieramy `docs.manim.community`

Zmierzone 2026-08-25: adres to `104.16.254.120`, czyli Cloudflare. To ten sam
przypadek współdzielonego adresu, dla którego `formspree.io` leży w
`init-firewall.sh` wśród odrzuconych. Wpuszczenie tej nazwy wpuszcza przy okazji
tysiące cudzych stron, a w zamian daje materiał, który w 90% jest już lokalnie.

## KaTeX: największa realna dziura, ale bez sieci

`vendor/katex/` ma sam silnik (`katex.min.js`, `katex.min.css`) i **żadnej listy
obsługiwanych poleceń**, a cała matematyka w `exercises.json` jest w KaTeX.
Model, który nie wie, czy `\cfrac` zadziała, zgaduje, a błąd wychodzi dopiero
na stronie.

Nie trzeba tego ściągać. Lista siedzi w samym zwendorowanym pliku:

```sh
grep -oE '\\\\[a-zA-Z]{2,}' vendor/katex/katex.min.js | sort -u
```

Zwraca **1011 nazw** i, co ważniejsze, dotyczy dokładnie tej wersji, która stoi
na stronie, a nie najnowszej z internetu.

**Ograniczenie, sprawdzone:** to prosty odsiew tekstu, więc łapie też pojedyncze
fałszywe trafienia. Kontrola negatywna na pięciu poleceniach, których KaTeX nie
wspiera, dała cztery poprawne odpowiedzi („brak") i jedno pudło
(`includegraphics` wychodzi jako obecne, choć KaTeX go nie renderuje). Traktuj
wynik jako **listę kandydatów do sprawdzenia**, nie jako wyrocznię. Ostateczny
dowód jest i tak darmowy: wyrenderować wyrażenie zwendorowanym KaTeX-em.

Dlatego `katex.org` zostaje zamknięty, mimo że ma zwykłe, własne adresy
(`63.176.8.218`), więc byłby bezpieczny. Po prostu jest zbędny.

## TeX: `texdoc` jest, ale pusty

Pułapka warta zapamiętania, bo wygląda na działające narzędzie:
`texdoc` jest zainstalowany, natomiast `texdoc -l amsmath` zwraca „nie
znaleziono". TeX Live w obrazie jest okrojony do plików roboczych, bez
dokumentacji pakietów. Czyli przy pytaniu o pakiet LaTeX-a **nie ma dokąd
zajrzeć w kontenerze**.

Mniej pilne niż KaTeX, bo sceny Manima używają wąskiego zestawu poleceń.

**Stan od 2026-08-25: załatwione w `.devcontainer/Dockerfile`, czeka na rebuild.**
Do bloku `apt-get` z pakietami TeX Live dopisane są `texlive-latex-base-doc`
i `texlive-latex-recommended-doc`, czyli dokumentacja dokładnie tych kawałków,
w których siedzą polecenia używane w scenach (amsmath, amssymb, ułamki,
środowiska równań). Dokumentacja zacznie istnieć dopiero po „Rebuild Container",
bo zmiana jest w obrazie, nie w kontenerze.

Sprawdzenie po rebuildzie, jednym poleceniem w kontenerze:

```sh
texdoc -l amsmath
```

Ma wypisać ścieżkę do pliku PDF. Jeśli dalej mówi „nie znaleziono", rebuild się
nie odbył albo nazwa pakietu w Debianie jest inna, niż zakładaliśmy (patrz niżej).

## Czego NIE ustalono

- Nie sprawdzano, ile z 1011 nazw wyłuskanych z `katex.min.js` to fałszywe
  trafienia. Zmierzono tylko, że na pięciu kontrolnych przypadkach jedno pudło
  się zdarzyło.
- Nie sprawdzano, jak duża jest paczka dokumentacji TeX Live ani czy mieści się
  w rozsądnym rozmiarze obrazu. Wpisane do Dockerfile'a dwa pakiety wybrano jako
  najmniejszy zestaw pokrywający amsmath, nie zmierzono ich rozmiaru.
- Nie zweryfikowano nazw `texlive-latex-base-doc` i `texlive-latex-recommended-doc`
  w repozytorium Debiana: host stoi na Fedorze (Bazzite), więc nie ma tam bazy
  pakietów Debiana, a sprawdzenie w sieci wymagałoby zgody (HOSTRULES.md).
  To są nazwy siostrzane wobec już zainstalowanych `texlive-latex-base`
  i `texlive-latex-recommended`, czyli mocne przypuszczenie, nie pomiar.
  Gdyby któraś była zła, rebuild padnie głośno, z komunikatem
  „Unable to locate package", a wtedy poprawka to jedna linijka w Dockerfile.
