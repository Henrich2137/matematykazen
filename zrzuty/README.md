# zrzuty/ — zrzuty ekranu strony w repo

Zdjęcia stanu strony, zatwierdzone w repozytorium, żeby **model bez przeglądarki
miał je od ręki** i nie musiał ich sobie robić (a w sesji chmurowej nie zawsze może).

Jeden katalog = jedna data, w formacie `RRRR-MM-DD`. Bez innych nazw i etykiet.

## Skąd się biorą

Robi je [tools/zrzuty.js](../tools/zrzuty.js) — komplet 16 ujęć jedną komendą,
zawsze tych samych, żeby dwa przebiegi dało się zestawić klatka w klatkę:

```
node tools/serwer.js 8001                      # w tle, obsługuje Range
NODE_PATH=/usr/local/share/npm-global/lib/node_modules \
  node tools/zrzuty.js --port=8001 --etykieta=RRRR-MM-DD
cp -r /tmp/zrzuty/RRRR-MM-DD zrzuty/
```

Domyślnie skrypt zapisuje do `/tmp/zrzuty/` — celowo poza repo. Ten katalog jest
wyjątkiem: **do repo trafia tylko okresowy stan odniesienia**, nie każdy przebieg
roboczy przy pracy nad CSS-em. Do porównań „przed/po" w trakcie zmian zostaje
`/tmp`.

## Co jest na zrzutach

Cztery widoki × dwa urządzenia × dwa motywy:

| Widok | Co pokazuje |
|---|---|
| `arkusz` | strona arkusza (2024-grudzień), góra listy zadań |
| `landing` | strona główna (`index.html`) |
| `sidebar` | panel boczny z opcjami, otwarty |
| `egzamin` | tryb egzaminacyjny |

Urządzenia: `desktop` i `telefon`. Motywy: `jasny` i `ciemny`.
Stąd nazwy plików w postaci `arkusz-telefon-ciemny.png`.

## Kiedy dorzucić nowy katalog

Po większej zmianie wyglądu, żeby był punkt odniesienia „jak było wcześniej".
Nie po każdej drobnej poprawce — 16 plików to ok. 1,3 MB.
