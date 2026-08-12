# Zadanie 5 — kroki rozwiązania do sprawdzenia

Otwórz w podglądzie (Ctrl+Shift+V). Notacja jak w `tablica-wzorow-transkrypt/`.
Wzór z tablic: [8.10] procent składany, **s. 10** (`formulasPage` zadania jest już na 10).

## Treść

Pani Aniela wpłaciła **60 000 zł** na lokatę dwuletnią, odsetki \(p\%\) w skali roku,
procent składany. Po dwóch latach na lokacie było **67 925,76 zł**. Oprocentowanie roczne:

- A. 6%
- **B. 6,4%** ← poprawna (`correctAnswerIndex: 1`)
- C. 6,5%
- D. 7%

## Proponowane kroki

Sześć kroków, siedem kropek. Film pokazuje sam rachunek; wzór \(P=P_0(1+p)^n\) siedzi
w opisie pod filmem, zgodnie z zasadą z 2026-08-11.

### Krok 1 — podstawiamy dane do wzoru

\[60\,000 \cdot (1+p)^{2} = 67\,925{,}76\]

Dwójka w wykładniku to dwa lata — przy procencie składanym każdy rok mnoży kapitał przez
to samo \((1+p)\).

*Opis:* Podstawiamy dane do wzoru na procent składany \(P=P_0\cdot(1+p)^{n}\): kapitał początkowy 60 000 zł, dwa lata, wynik 67 925,76 zł.

### Krok 2 — dzielimy obie strony przez 60 000

\[(1+p)^{2} = \frac{67\,925{,}76}{60\,000}\]

*Opis:* Dzielimy obie strony przez 60 000, żeby zostawić po lewej samą potęgę.

### Krok 3 — liczymy ułamek

\[(1+p)^{2} = 1{,}132096\]

*Opis:* Liczymy dzielenie: \(67\,925{,}76 : 60\,000 = 1{,}132096\).

### Krok 4 — pierwiastkujemy

\[1+p = 1{,}064\]

Formalnie pierwiastek daje dwie możliwości, ale \(1+p\) jest dodatnie (kapitał rośnie),
więc bierzemy tylko wartość dodatnią.

*Opis:* Pierwiastkujemy obie strony. Bierzemy wartość dodatnią, bo \(1+p>0\) — kapitał na lokacie nie może być ujemny.

### Krok 5 — odejmujemy 1

\[p = 0{,}064\]

*Opis:* Odejmujemy 1 od obu stron i zostaje samo \(p\).

### Krok 6 — zamieniamy na procenty

\[p = 6{,}4\%\]

*Opis:* Zamieniamy ułamek dziesiętny na procent: \(0{,}064 = 6{,}4\%\) — odpowiedź **B**.

## Czego film NIE pokazuje

Skrótu przez sprawdzanie odpowiedzi: \(60\,000\cdot 1{,}064^{2}=67\,925{,}76\) zł. Jest
w „Pokaż więcej" i bywa na maturze szybszy niż liczenie wprost. Powiedz, jeśli uważasz, że
warto zrobić z tego osobny krok albo drugie rozwiązanie.

## Dlaczego pozostałe odpowiedzi są złe

| Odp. | Skąd błąd |
|---|---|
| A. 6% | \(60\,000\cdot 1{,}06^{2}=67\,416\) zł — za mało |
| **B. 6,4%** | **poprawna** |
| C. 6,5% | \(60\,000\cdot 1{,}065^{2}=68\,053{,}5\) zł — za dużo |
| D. 7% | policzenie odsetek jako prostych, nie składanych, albo strzał w ciemno |
