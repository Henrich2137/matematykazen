# MatematykaZen

Interaktywna platforma do nauki matematyki pod **maturę podstawową** (CKE).
Statyczna strona — bez backendu i kont, postęp zapisywany lokalnie w przeglądarce.

Na żywo: <https://henrich2137.github.io/matematykazen/>

## Co jest w środku

- Arkusze CKE z zadaniami zamkniętymi (ocena automatyczna) i otwartymi
  (samoocena po porównaniu z rozwiązaniem modelowym).
- Podpowiedzi, rozwiązania krok po kroku (tekst + wideo) i interaktywne widżety.
- Tablica wzorów i zasady oceniania CKE w przesuwnych panelach.
- Tryb próbnego egzaminu z zegarem, motyw jasny / ciemny / auto.

## Uruchomienie lokalne

Brak builda i menedżera pakietów. Strona ładuje dane przez `fetch`, więc nie
zadziała z `file://` — uruchom serwer statyczny w katalogu repo:

```
npx serve
```

## Licencja

Kod, interfejs oraz autorskie treści (podpowiedzi, rozwiązania, widżety) są
udostępnione na licencji **PolyForm Noncommercial 1.0.0** — pełny tekst
w [LICENSE.md](LICENSE.md). Wolno używać, modyfikować i rozpowszechniać
**wyłącznie w celach niekomercyjnych**.

Zadania maturalne, arkusze i klucze odpowiedzi pochodzą z **Centralnej Komisji
Egzaminacyjnej** i **nie są objęte tą licencją**.

Chcesz pomóc? Zajrzyj do [CONTRIBUTING.md](CONTRIBUTING.md) — są tam też zasady
licencjonowania wkładu.

Zainteresowany licencją komercyjną? Napisz: henrich2@proton.me
