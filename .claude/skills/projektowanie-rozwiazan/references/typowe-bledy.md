# Typowe błędy maturzysty, poziom podstawowy

Źródła: sprawozdania CKE 2024 i 2025 (poziom podstawowy), materiały korepetycyjne.
Zebrał Henrich, 2026-08-26.

**Tag przy nagłówku mówi, w którym artefakcie ten rodzaj błędu rozbraja się najlepiej.**
To wskazówka, nie przypisanie na sztywno: jeśli błąd grozi w zadaniu, które ma tylko
podpowiedź i rozwiązanie opisowe, rozbrajasz go tam.

## Jak z tego korzystać

1. **Wybierz najwyżej dwie pozycje**, które grożą w tym konkretnym zadaniu. Nie te, które
   pasują do działu, tylko te, na których uczeń wyłoży się przy tych liczbach i tej treści.
2. **Wpleć je w ten krok, w którym grożą.** Błąd ze znakiem przy nawiasie rozbraja się
   w kroku, w którym ten nawias się opuszcza, a nie w podsumowaniu.
3. **Nie doklejaj listy ostrzeżeń na końcu.** Nikt jej nie czyta, a w rozwiązaniu opisowym
   i w filmie pokazujemy wyłącznie poprawny tok.
4. **Nie pisz „uczniowie często mylą…".** Zamiast ostrzeżenia zaprojektuj krok tak, żeby
   pomyłka była widoczna: rozbij przekształcenie na dwa, zaznacz kolorem to, co zmienia znak,
   dopisz brakujące ogniwo.

---

## Znaki, nawiasy, ułamki  [animacja]

- Minus przed nawiasem: `5 − (2x − 3)` → ŹLE `5 − 2x − 3` | DOBRZE `5 − 2x + 3`
- Brak nawiasu przy sumie w liczniku: `(x+1)/2 · 4` → ŹLE `x + 1/2 · 4`
- Dodawanie ułamków: `1/3 + 1/4` → ŹLE `2/7` | DOBRZE `7/12`
- Dzielenie przez ułamek: `6 : (2/3)` → ŹLE `4` | DOBRZE `9`
- Kwadrat sumy: `(a+b)²` → ŹLE `a² + b²` | DOBRZE `a² + 2ab + b²`
- Wyłączanie czynnika: `4l² + 4l` → ŹLE `4(l² + 4l)` | DOBRZE `4(l² + l)`
- Redukcja po podstawieniu `n = 2l+1`: gubienie wyrazu przy rozwijaniu `3(2l+1)²`
- Potęgi: `(2³)²` → ŹLE `2⁵` | DOBRZE `2⁶`
- Pierwiastek z kwadratu: `√(x²)` → ŹLE `x` | DOBRZE `|x|`
- Skracanie mogącego być zerem: `(x²−x)/x → x−1` bez zastrzeżenia `x ≠ 0`

**Jak rozbroić:** to są błędy jednego ruchu, więc leczy je osobny krok filmu. Znak, który
zmienia znaczenie, ma się w to nowe znaczenie zamienić na oczach ucznia, a nie zniknąć
i pojawić się gdzie indziej. Przy wyłączaniu czynnika i przy kwadracie sumy pokaż pary
jawnie, czynnik po czynniku, zamiast podmieniać całą linijkę naraz.

## Funkcje, wykresy, nierówności  [widżet]

- Dziedzina i zbiór wartości: dziedzina z osi X, zbiór wartości z osi Y
- Pominięta dziedzina: `log(x−2)` bez `x > 2`; mianownik bez `≠ 0`
- Przesunięcie wykresu: `f(x) + b` (w pionie) mylone z `f(x + b)` (w poziomie)
- Nierówność kwadratowa: `x² − 4 > 0` → ŹLE `(−2, 2)` | DOBRZE `(−∞,−2) ∪ (2,∞)`
- Mnożenie nierówności przez liczbę ujemną bez odwrócenia znaku
- Odczyt z wykresu: mylenie miejsca zerowego z wartością minimalną

**Jak rozbroić:** tu jest co oglądać, więc to naturalne miejsce na widżet. Uczeń rusza tą
wielkością, która odsłania przyczynę, a pod płótnem idzie rachunek z podstawioną wartością.
Pokaż też, co **zostaje stałe**, bo bez niezmiennika uczeń wynosi wniosek „wszystko zależy
od wszystkiego". Bez widżetu: dziedzina idzie na górę rozwiązania, ze zdaniem, skąd się wzięła.

## Czytanie treści zadania  [podpowiedź]

- Procent od złej podstawy: liczy 13% z kwoty **wykorzystanej** zamiast **przyznanej**
- Procent składany tam, gdzie treść mówi o jednorazowym
- Dopisanie założenia nieobecnego w treści („kwotę podzielono po równo")
- Uznanie podanej danej za zbędną i nieużycie jej
- Model najbardziej znany zamiast opisanego: liczy ostrosłup prawidłowy albo
  prostopadłościan o podstawie kwadratu, gdy treść mówi co innego
- Odpowiedź na inne pytanie: policzył `x`, a pytali o pole

**Jak rozbroić:** te błędy powstają, zanim uczeń cokolwiek policzy, więc film ich nie złapie.
Podpowiedź ma odesłać do właściwego słowa w treści („sprawdź, od której kwoty liczysz ten
procent"), nie podać rachunku. Ostatni z listy zamyka się inaczej: ostatnią linijką
rozwiązania, która wraca do polecenia, patrz `zasady-tekstowe.md`.

## Dowody i strategia  [rozwiązanie opisowe]

- Sprawdzenie tezy dla kilku `n` (np. 1, 3, 5) uznane za dowód
- Doprowadzenie do `4(3l² + 4l + 3)` i **brak zdania kończącego** dowód
- Optymalizacja: liczenie pola dla kilku `x` zamiast wierzchołka paraboli
- Niewyznaczenie dziedziny funkcji w zadaniu optymalizacyjnym, czyli utrata punktu
- Ciąg arytmetyczny mylony z geometrycznym
- Cięższe narzędzie niż trzeba: tw. cosinusów tam, gdzie wystarczy trójkąt 30-60-90

**Jak rozbroić:** to są błędy punktowane przez CKE, więc sprawdź je wprost przy kryteriach
z `odpowiedzi.pdf`. Zdanie kończące dowód i wyznaczona dziedzina to osobne punkty, a nie
ozdobniki, i mają w rozwiązaniu stać na swoim miejscu: dziedzina na górze, wniosek w ostatniej
linijce przez całą szerokość.

## Brak kontroli wyniku  [widżet]

- Ujemna długość boku albo ujemne pole zapisane jako odpowiedź
- Prawdopodobieństwo `> 1` albo `< 0`
- Otrzymanie równania sprzecznego (`sin α = 0`) i zapisanie tego jako wynik
- Wynik rzędu wielkości bez sensu (kwota 12 zł przy budżecie 1,2 mln)

**Jak rozbroić:** jeden krótki sprawdzian sensu w ostatnim kroku, na liczbach, a nie zdanie
„sprawdź, czy wynik ma sens". Przy dwóch pierwiastkach równania to jest też moment na
odrzucenie tego, który odpada, ze zdaniem dlaczego („długość nie bywa ujemna").
