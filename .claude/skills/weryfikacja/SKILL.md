---
name: weryfikacja
description: Zasady weryfikacji pracy w tym repo — użyj, gdy kończysz pracę subagenta, budujesz narzędzie diagnostyczne (zrzuty, testy, skrypty sprawdzające) albo gdy okazuje się, że sam popełniłeś błąd. Powstały z realnych wpadek w sesji 2026-08-09.
---

# Weryfikacja

Trzy zasady wyprowadzone z sesji, w której każda z nich została najpierw złamana.
Krótkie z założenia — szczegóły są w `done/04-biezace.md`.

## 1. Raport agenta to hipoteza, nie wynik

Po każdym subagencie sprawdź **kluczowy efekt własnym narzędziem**, zanim zamkniesz
temat. Nie wystarczy przeczytać, co napisał.

Dlaczego: paczka 1 planu UI zaraportowała „zweryfikowane zrzutami" dla poprawki
naniesionej na **niewłaściwy element** — raport brzmiał całkowicie wiarygodnie
i tylko obejrzenie zrzutu to wyłapało.

Minimum: jeden zrzut, jeden odczyt stanu albo jedna komenda potwierdzająca to,
co agent uznał za zrobione.

## 2. Narzędzie, które może skłamać po cichu, dostaje zapadkę

Gdy skrypt diagnostyczny może zwrócić wynik **prawdopodobny, ale fałszywy** —
dopisz asercję, która to wykryje. Nie komentarz ostrzegawczy, tylko sprawdzenie
w kodzie, które krzyczy.

Dlaczego: `tools/zrzuty.js` robił zrzuty „ciemnego motywu", które były jasne
(literówka w kluczu localStorage). Wyglądały wiarygodnie i cała praca nad ciemnym
motywem poszłaby na jasnych obrazkach. Skrypt sprawdza teraz klasę na `<html>`.

Pytanie kontrolne przy każdym narzędziu: *jak wygląda jego cichy błąd i co go
wykryje?*

## 3. Własny błąd: jedno zdanie i dalej

Zauważyłeś swoją wpadkę — powiedz o niej wprost, popraw i wróć do zadania.
Bez przeprosin, bez rozwodzenia się, bez rozliczania samego siebie.

Dotyczy tak samo sytuacji, w której Henrich wskazuje, że się myliłeś: wycofaj tezę
jednym zdaniem i idź dalej. Sprostowanie ma być krótsze niż błąd.

Nie dotyczy bloków myślenia — tam analizuj do woli.
