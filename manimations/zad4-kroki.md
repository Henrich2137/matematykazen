# Zadanie 4 — kroki rozwiązania do sprawdzenia

**Do czego to jest:** propozycja podziału na kroki, ZANIM powstanie scena w Manimie.
Otwórz w podglądzie (Ctrl+Shift+V) i sprawdź, czy merytoryka i kolejność się zgadzają.
Notacja jak w `tablica-wzorow-transkrypt/` — `\( … \)` w linii, `\[ … \]` na środku.

Wzory z tablic: [3.2] Działania na logarytmach, **s. 5, dół**
(`tablica-wzorow-transkrypt/03-logarytmy.md`). W danych zadania `formulasPage` jest już
ustawione na 5 — zgadza się.

## Treść

Dla każdej dodatniej liczby rzeczywistej \(x\) i dla każdej dodatniej liczby rzeczywistej \(y\)
wartość wyrażenia \(\log_{7} x + 6\log_{7} y\) jest równa wartości wyrażenia:

- A. \(\log_{7}\dfrac{x}{y^{6}}\)
- B. \(\log_{7}(xy)^{6}\)
- C. \(\log_{7}(6xy)\)
- **D. \(\log_{7}\left(xy^{6}\right)\)** ← poprawna (klucz CKE, `correctAnswerIndex: 3`)

## Proponowane kroki

Cztery kroki, czyli pięć kropek na pasku. Model jest ten sam co w zad. 2: **kropka = stan
zapisu, film = jedno przekształcenie**. Na zielono to, co się w danym kroku zmienia.

### Krok 1 — zapisujemy wyrażenie

\[\log_{7} x + 6\log_{7} y\]

Nic się jeszcze nie dzieje — wyrażenie wjeżdża w kadr. Tak samo zaczyna się zad. 2
(„Zapisujemy działanie z zadania").

*Opis pod filmem:* Zapisujemy wyrażenie z zadania.

### Krok 2 — szóstka wchodzi do logarytmu jako wykładnik

\[\log_{7} x + \underbrace{6\log_{7} y}_{\text{to się zmienia}} \;\longrightarrow\; \log_{7} x + \log_{7}\left(y^{6}\right)\]

Wzór [3.2] czytany **od prawej do lewej**: \(\log_a x^{r} = r \cdot \log_a x\), czyli
\(6\log_{7} y = \log_{7}\left(y^{6}\right)\).

Animacja: szóstka stojąca przed logarytmem przelatuje na miejsce wykładnika przy \(y\).

*Opis pod filmem:* Współczynnik przed logarytmem wciągamy do środka jako wykładnik:
\(r\log_a x=\log_a x^{r}\), czyli \(6\log_{7}y=\log_{7}y^{6}\).

### Krok 3 — suma logarytmów staje się logarytmem iloczynu

\[\log_{7} x + \log_{7}\left(y^{6}\right) \;\longrightarrow\; \log_{7}\left(x \cdot y^{6}\right)\]

Wzór [3.2] czytany **od prawej do lewej**: \(\log_a x + \log_a y = \log_a (x\cdot y)\).
Podstawa jest w obu składnikach ta sama (siódemka) — to jest warunek, żeby wolno było
tak zrobić, i warto, żeby było widać, że oba siedmiaki się zgadzają.

Animacja: dwa logarytmy zbiegają się w jeden, znak `+` zamienia się w kropkę mnożenia.

*Opis pod filmem:* Suma logarytmów o **tej samej podstawie** to logarytm iloczynu:
\(\log_a x+\log_a y=\log_a(x\cdot y)\).

### Krok 4 — zapis bez kropki, czyli gotowa odpowiedź

\[\log_{7}\left(x \cdot y^{6}\right) \;\longrightarrow\; \log_{7}\left(xy^{6}\right)\]

*Opis pod filmem:* Kropkę mnożenia zwyczajowo pomijamy — \(\log_{7}\left(xy^{6}\right)\)
to odpowiedź **D**.

> **Moja decyzja, do Twojej korekty.** Ten krok to sama kosmetyka zapisu — matematycznie nic
> się nie dzieje. Zostawiłem go z jednego powodu: odpowiedź D w arkuszu jest zapisana
> **bez** kropki, a krok 3 kończy się **z** kropką, więc bez tego uczeń musi sam zrobić
> ostatnie porównanie. Jeśli uznasz to za przerost, wystarczy powiedzieć — wtedy kroki 3 i 4
> zlewają się w jeden i zostają trzy.

## Dlaczego pozostałe odpowiedzi są złe

Nie wchodzi to do filmu (film pokazuje samo przekształcenie, tak jak w zad. 2) — sprawdź
tylko, czy się zgadza, bo to samo siedzi w podpowiedzi i w „Pokaż więcej".

| Odp. | Zapis | Skąd się bierze błąd |
|---|---|---|
| A | \(\log_{7}\dfrac{x}{y^{6}}\) | użycie wzoru na **różnicę** logarytmów zamiast na sumę — czyli przeczytanie `+` jako `−` |
| B | \(\log_{7}(xy)^{6}\) | wciągnięcie szóstki jako wykładnika **całego iloczynu**, a nie samego \(y\); to jest \(\log_7 x^6+6\log_7 y\), a nie nasze wyrażenie |
| C | \(\log_{7}(6xy)\) | potraktowanie szóstki jak zwykłego czynnika, jakby \(6\log_7 y=\log_7 (6y)\) |
| **D** | \(\log_{7}\left(xy^{6}\right)\) | **poprawna** |

## Czego ten plik NIE ustala

- Nazw plików i pól w `exercises.json` — to idzie automatycznie po Twojej akceptacji
  (`media/zad4/solution-step-by-step/step1..4.mp4` + rewersy z `tools/rewersy.sh`).
- Wyglądu animacji w detalach (tempo, dokładny tor lotu szóstki) — to widać dopiero
  na wyrenderowanym filmie.
