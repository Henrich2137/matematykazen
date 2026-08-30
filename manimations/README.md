# manimations/

Skrypty Manim generujące wideo do `solutionStepByStep` w `exercises.json` (finalne pliki lądują w `matura/<sheet-id>/media/zadN/`).

## Środowisko

Render robi się **w devkontenerze** i tylko tam (Manim Community v0.18.1). Opis renderowania na Windowsie Henricha odpadł 2026-08-20, bo Henrich już na nim nie pracuje; wersje tamtej maszyny zostały w historii repo i w porównaniu niżej.

### Devkontener — Debian (dodane 2026-08-11)

Manim, ffmpeg i minimalny TeX Live siedzą w obrazie kontenera (blok w `.devcontainer/Dockerfile` z `ARG MANIM_VERSION`), więc render odpala się w kontenerze bez żadnego przygotowania: `manim solutionZadN.py <NazwaScenyKlasy>`.

- LaTeX to TeX Live w minimalnym zestawie z dokumentacji Manima (~1–1,5 GB), a nie `texlive-full` — pokrywa to, czego używają istniejące sceny. Gdyby render zgłosił brakujący plik `.sty`, dopisuje się konkretny pakiet w Dockerfile.
- Instalacja nie wymaga wyjątku w firewallu (`pypi.org` jest poza allowlistą): obraz buduje się, zanim host nałoży firewall, a po starcie kontenera Manim nic już nie pobiera.
- Przypięty jest **tylko sam Manim**. Zależności pod spodem instalują się w najnowszych wersjach (sprawdzone 2026-08-11: `ManimPango 0.6.1`, `numpy 2.4.6`, `Pillow 12.3.0`, ffmpeg **5.1.9** z Debiana 12). Dawny host Henricha miał inne (`0.6.0` / `2.2.1` / `11.0.0`, ffmpeg 7.1) i mimo to dawał ten sam obraz - patrz porównanie niżej.
- **Dokumentację API Manima czytaj lokalnie, nie z internetu.** Kontener ma cały kod źródłowy Manima (163 pliki `.py`) razem z opisami funkcji, a firewall i tak nie przepuszcza `docs.manim.community`. Zamiast zgadywać nazwy argumentów:
  ```sh
  python3 -c "import manim, inspect; print(inspect.signature(manim.MathTex.__init__))"
  python3 -c "import manim, inspect; print(inspect.getdoc(manim.TransformMatchingShapes))"
  python3 -c "import manim, inspect; print(inspect.getsource(manim.Transform.__init__))"
  ```
  Offline nie ma tylko poradników i galerii przykładów ze strony. Dlaczego nie otwieramy tej domeny: [../issues/dokumentacja-dla-modeli.md](../issues/dokumentacja-dla-modeli.md).
- **Co ten obraz na pewno umie: [test-mozliwosci.py](test-mozliwosci.py).** Siedem scen kontrolnych pokrywających to, co wychodzi na maturze: wyrażenia z liczbą zmienianą płynnie przez `ValueTracker`, układ współrzędnych z wykresami i polem pod krzywą, bryły 3D (kula, sześcian, stożek, walec, ostrosłup, powierzchnia siodłowa) z obracającą się kamerą, geometria płaska z kątami i klamrami, diagram słupkowy i tabela, trudniejszy LaTeX (układ równań, pierwiastek stopnia n, granica, symbol Newtona, przedziały) oraz polskie znaki. Wszystkie siedem przechodzi (sprawdzone 2026-08-25). **Puść je po każdej zmianie `MANIM_VERSION` w Dockerfile**, przepis w nagłówku pliku; to jedyny tani sposób, żeby wyłapać, że przebudowa obrazu coś urwała.
- **Nie podawaj flagi jakości** (`-ql`/`-qh` itd.). Flaga jakości nadpisuje `pixel_width`/`pixel_height` z `manim.cfg`, a wraz z rozdzielczością zmieniają się **proporcje kadru**, czyli rozmieszczenie wzorów wychodzi inne niż w plikach już wgranych na stronę. Samo `manim plik.py Scena` czyta `manim.cfg` i trafia w obowiązujące **1280×720 @ 120 fps** (16:9). Porównanie host ↔ kontener niżej robione było jeszcze na starym kadrze 840×360 @ 60 fps (21:9), sprzed zmiany z 2026-08-11.

#### Parametry renderu i waga plików

`manim.cfg`: **1280×720, 120 fps, tło białe.** Powody, żeby nikt tego nie „poprawił":

- 1280 pokrywa telefon przy gęstości pikseli 3 (potrzeba 900 px) i komputer przy 2 (840 px). Problemem starego kadru 840×360 nie była liczba pikseli, tylko kształt: na telefonie film dostawał 129 px wysokości.
- 120 fps to **zapas pod spowolnienie**, nie płynność przy 1×. Spowolnienie nie dorysowuje klatek, tylko trzyma je dłużej, więc materiał 60 fps przy 0,25× wygląda jak 15 fps, a to właśnie ten tryb służy przyglądaniu się przekształceniu.
- Waga jest bez znaczenia: krok trwający 1 do 2 s waży 17 do 67 kB. Przejście z 840×360/60 na 1280×720/120 dało około dwóch razy więcej, nie dziesięciu.

#### Porównanie host ↔ kontener (zrobione 2026-08-11) — ✅ zgodne

Ten sam skrypt (`solutionZad2.py`, `ScenaZadania2`, czyli krok 6) wyrenderowany w kontenerze i zestawiony z hostowym `matura/2024-grudzien/media/zad2/zad2rozw_step6.mp4`:

- **Parametry pliku identyczne**: 840×360, 60 fps, 120 klatek, 2,000 s, h264 High, yuv420p.
- **SSIM średnio 0,999856**, najgorsza klatka 0,999543 (klatka 95, w środku animacji przekształcenia).
- W powiększeniu 4× glify mają **tę samą geometrię i te same pozycje** — różnice siedzą wyłącznie na krawędziach antyaliasingu.
- Skąd bierze się ta resztkowa różnica — test izolujący koder (render `--format=png`, czyli bez kompresji, jako trzeci punkt odniesienia; klatka 95):

  | Porównanie | SSIM |
  |---|---|
  | bezstratny render kontenera ↔ własny MP4 kontenera (sam koder) | 0,999601 |
  | bezstratny render kontenera ↔ MP4 z hosta | 0,999480 |
  | MP4 kontener ↔ MP4 host | 0,999581 |

  Czyli **sama kompresja H.264 wprowadza różnicę tego samego rzędu co cała różnica host↔kontener** i wystarcza do jej wyjaśnienia. Obawa o metryki fontu (MiKTeX vs TeX Live) **się nie potwierdziła**.
- **Nie ustalono**, jaka część różnicy przypada na koder, a jaka na sam render — wymagałoby to bezstratnych klatek z hosta, a referencja istnieje wyłącznie jako H.264. Znane różnice po stronie kodera: ffmpeg 5.1.9 vs 7.1 i waga pliku 20 kB vs 27 kB.

Wniosek: kontener nadaje się także do **finalnych** renderów, nie tylko do podglądu.

**Zmiany w `.devcontainer/Dockerfile` robi się z hosta, nie z kontenera** — `.devcontainer/` jest w kontenerze zamontowany read-only (patrz `.devcontainer/README.md`). Po edycji trzeba przebudować obraz: Dev Containers → „Rebuild Container".

## Workflow

0. **Każdy krok musi kończyć się `self.wait(0.25)`** — inaczej ostatni element animacji nie zostaje na ekranie. Przeglądarka po zakończeniu odtwarzania zatrzymuje obraz kilka klatek przed końcem pliku (przy 120 fps klatka trwa 8 ms, więc gubi się ich więcej niż kiedyś). Wykryte 2026-08-11 na kroku 1 zadania 2: w pliku ostatnia klatka miała wykładnik `⁻⁵` (obszar do x=925), a przeglądarka pokazywała w spoczynku obraz bez niego (do x=792). Po dodaniu przytrzymania oba obszary są identyczne. To nie jest kosmetyka — właśnie ta klatka zostaje na ekranie, gdy uczeń patrzy na krok.
1. Render sceny: `manim --save_sections solutionZadN.py <NazwaScenyKlasy>` (bez flagi jakości, patrz wyżej) — wynik ląduje w `media/videos/solutionZadN/720p120/`, a **każdy krok osobnym plikiem** w podkatalogu `sections/`, w kolejności `<Scena>_0000_krok1.mp4`, `_0001_krok2.mp4`, …
2. Cięcie jest **zrobione samym renderem** (2026-08-12) — granice kroków wyznacza `self.next_section("krokN")` w scenie. Wcześniej automatu nie było: kroki przełączało się komentarzem `"""` i renderowało po jednym, przez co w repo leżały skrypty z zakomentowaną większością treści, a `solutionZad2.py` w tej postaci **nie odtwarzał** wgranych plików (brakowało w nim m.in. przytrzymań `self.wait(0.25)`). Wszystkie cztery sceny są już przepisane na sekcje.

**To załatwiło problem stanu przenoszonego między krokami.** Odtworzenie zadania 2 krok po kroku (2026-08-11) pokazało, że **krok 2 nie renderuje się poprawnie w izolacji**: przekształca tylko `kroki[0][0..2]`, więc domykający nawias z wykładnikiem (`kroki[0][3]`) w ogóle nie trafia na scenę — w oryginalnej procedurze był tam już narysowany przez krok 1. Przy renderze przez sekcje ten problem znika z definicji: scena jedzie w całości, a sekcja to tylko miejsce cięcia gotowego materiału, więc każdy krok zaczyna się dokładnie tam, gdzie skończył poprzedni. Sprawdzone: sześć kroków zadania 2 wyrenderowanych przez `--save_sections` wychodzi **identycznych co do piksela** (SSIM 1,000000) z plikami wgranymi wcześniej na stronę.

**Dwie zasady, których trzeba pilnować w scenie:**

- `self.wait(0.25)` na końcu KAŻDEJ sekcji (punkt 0 wyżej) i **zawsze przed** `self.clear()`/`self.remove()`. Przytrzymanie po wyczyszczeniu sceny trzyma białą planszę — i to ona zostaje uczniowi na ekranie. Złapane porównaniem SSIM z wgranym plikiem (krok 2 zad. 2 wypadał 0,9967 zamiast 1,0).
- Wspólne skalowanie kroków pod kadr 16:9: jeden współczynnik liczony z najszerszego kroku (`MARGINES = 0.85`), a nie dopasowanie każdego kroku osobno — inaczej litery zmieniają rozmiar w trakcie przekształcenia i `Transform` robi z tego zoom. Wzorzec jest w każdej z czterech scen.
2a. **Zmniejszasz liczbę kroków w scenie? Usuń najpierw `media/videos/<scena>/` ręcznie**
   (złapane 2026-08-28 na zad. 10). Manim nie czyści katalogu `sections/`, więc po renderze
   sceny z dziewięcioma krokami leżą tam nadal pliki z poprzednich szesnastu, a
   `tools/wgraj-kroki.sh` skopiuje mieszankę obu wersji i wszystko wygląda na wyrenderowane.
   Objaw: `styk-klatek.sh` pokazuje więcej kroków, niż ma scena.

3. Skopiować pocięte pliki do `matura/<sheet-id>/media/zadN/solution-step-by-step/` pod nazwami `stepM.mp4` (nazwy lowercase, patrz CLAUDE.md). Zmiana z 2026-08-11: wcześniej leżały płasko jako `zadNrozw_stepM.mp4`.
4. Wygenerować rewersy: `tools/rewersy.sh matura/<sheet-id>/media/zadN/solution-step-by-step`. Przycisk ◄ w odtwarzaczu odtwarza `stepMreverse.mp4`. Rewersu **nie renderuje Manim**, powstaje z gotowego pliku jedną linijką ffmpega, więc nie może się z nim rozjechać:

   ```
   ffmpeg -i stepN.mp4 -vf "reverse,tpad=stop_mode=clone:stop_duration=0.25" -an stepNreverse.mp4
   ```

   Trzy rzeczy, które przy tym wybuchną, jeśli się o nich nie pomyśli:

   - **Przytrzymanie stanu końcowego ląduje na POCZĄTKU rewersu.** Odwrócenie zamienia końce miejscami, więc 0,25 s bezruchu z końca kroku staje się bezruchem na starcie cofki, a rewers kończy się dokładnie w tej klatce, której przeglądarka nie zdąży namalować (punkt 0 wyżej). Załatwia to `tpad`: klonuje ostatnią klatkę rewersu przez 0,25 s, więc przytrzymanie jest po obu stronach bez dotykania scen.
   - **`-an` jest istotne.** Pliki nie mają dźwięku, a bez tej flagi ffmpeg potrafi dołożyć pustą ścieżkę i niepotrzebnie zwiększyć wagę.
   - **Nazwy są sztywne**: `stepN.mp4` obok `stepNreverse.mp4`, w katalogu `solution-step-by-step/`. Odtwarzacz nie czyta nazwy rewersu z danych, tylko dokłada `reverse` przed rozszerzeniem, więc `exercises.json` wymienia wyłącznie plik w przód.

   Zmierzone po pierwszym przebiegu (23 kroki): rewers ma dokładnie tyle klatek co oryginał plus 0,25 s (15 przy 60 fps, 30 przy 120), a SSIM końca kroku wobec startu rewersu i startu kroku wobec końca rewersu wynosi ≥ 0,9994, przy szumie samej kompresji rzędu 0,9996. Rewers kroku 1 kończy się pustym kadrem, bo krok 1 rysuje działanie od zera; dlatego z pierwszej kropki cofać się nie da (decyzja Henricha).

**`manimations/` zostaje na wierzchu repo**, a nie w katalogu arkusza (decyzja Henricha, 2026-08-11): produkcja ma być oddzielona od statycznej strony, żeby hosting nie ciągnął za sobą źródeł animacji. Gotowe pliki idą wyłącznie do `matura/<sheet-id>/media/zadN/solution-step-by-step/`; wcześniej leżały płasko jako `zadNrozw_stepM.mp4` i mieszały się z rysunkami zadania.

`media/` w tym folderze to cache Manim (Tex/svg, obrazy, wideo pośrednie) — odtwarzalny z plików `.py`, dlatego wyklucza go `manimations/.gitignore`.

5. Obejrzeć wynik na stronie **wyłącznie przez `node tools/serwer.js 8000`**. `python3 -m http.server` **nie nadaje się do pracy nad wideo**: nie obsługuje żądań zakresowych (`Range`), a bez nich przeglądarka nie potrafi przewinąć filmu — `video.seekable` zostaje pusty, a każde ustawienie `currentTime` cicho wraca do zera. Wygląda to jak błąd w kodzie odtwarzacza i raz już nim nie było (2026-08-11, sporo straconego czasu). Sprawdzian: `curl -s -o /dev/null -w "%{http_code}\n" -r 0-100 <url filmu>` ma zwrócić **206**, nie 200. Pozostałe pułapki podglądu (zrzut ekranu potrafi przy wideo pokazać co innego niż jest w pliku, gubienie klatek przy 4×, jak porównywać wiarygodnie) zebrane są w [issues/rozwiazanie-krok-po-kroku-odtwarzacz.md](../issues/rozwiazanie-krok-po-kroku-odtwarzacz.md).

## Jak ma wyglądać animacja (zasady Henricha, 2026-08-12)

Wszystkie trzy wyszły z jego przeglądu zadań 3, 5 i 6 (v27). Łamie je automatyczne
`TransformMatchingShapes` bez nadzoru — Manim paruje wtedy kształty po podobieństwie, więc
szóstka z `60\,000` potrafi polecieć do licznika ułamka zamiast do mianownika, a nawias
`(1+p)^2` zamiast przesunąć się, znika i pojawia się na nowo. **Sprawdzaj każdy krok okiem
na gotowym pliku, a nie po samym „wyrenderowało się bez błędu".**

1. **Ciągłość między krokami.** Ostatnia klatka kroku N musi wyglądać dokładnie tak jak
   pierwsza klatka kroku N+1 — bo w odtwarzaczu to jest jedno i to samo miejsce, uczeń
   zatrzymuje się na nim i dopiero potem puszcza dalej. Wszelkie podświetlenia zdejmuj
   **przed** końcowym `self.wait(0.25)`, nie po nim. Jeśli coś ma zostać podświetlone przez
   kilka kroków (np. założenie \(x\ne 1\)), to musi być podświetlone w obu filmach.
   Sprawdzalne maszynowo: ostatnia klatka `stepN.mp4` kontra pierwsza klatka `stepN+1.mp4`.
2. **Ruch ma odpowiadać rachunkowi.** Element, który w rachunku wędruje w konkretne miejsce,
   ma tam dolecieć — a nie zniknąć i pojawić się gdzie indziej. Przy dłuższych wyrażeniach
   nie licz na automatyczne parowanie: wskazuj pary indeksami glifów (wzorzec z `solutionZad4.py`).
3. **Kolor to wskazówka, nie ozdoba.** Kolorem (czyli czymkolwiek poza czernią/bielą)
   oznaczasz **tylko to, na co uczeń ma spojrzeć**: składnik przenoszony na drugą stronę,
   czynnik, który się skraca. Znak, który się pojawia albo znika, może być czerwony.
   Nie koloruje się całego wyrażenia „bo się w nim coś zmieniło".

## Jak pisać opisy kroków (ROW 3, pole `text` w exercises.json)

Też zasady Henricha (2026-08-12). Priorytetem jest to, żeby uczeń zrozumiał, a nie żeby
zapis był formalnie poprawny.

- **Opis to wzór plus wyjaśnienie słowne, nie powtórka rachunku** (Henrich, 2026-08-23,
  potwierdzone na zad. 2 z 2024-grudnia). Pod filmem ma stać zdanie, dlaczego wolno tak
  przekształcić, i wzór z tablicy w osobnym wierszu. Samych obliczeń nie przepisujemy,
  bo widać je w kadrze.
- **Nie opisuj słowami tego, co widać na filmie.** „Zaczynamy od równania z wartością
  bezwzględną: \(|x+4|=7\)" nie mówi nic ponad obraz. Wystarczy „Zapisujemy \(|x+4|=7\)".
- **Tłumacz to, co naprawdę wymaga tłumaczenia, ale po ludzku.** Nie „wyrażenie pod modułem
  przyjmuje wartości przeciwne", tylko pokazane na liczbach, czym ta wartość bezwzględna
  właściwie jest. Żargonu tyle, ile uczeń musi znać na maturze, reszta zwykłymi słowami.
- **Krótkie linijki, wzór w osobnym wierszu.** Pole `text` trafia do DOM przez `innerHTML`,
  więc `<br>` i `\[ … \]` działają. Zbity akapit czyta się gorzej niż cztery linijki.
- **Wzór w ramce `\[ … \]` tylko wtedy, gdy stoi w tablicy wzorów** (`tablica-wzorow-transkrypt/`).
  Reszta, np. wyłączanie wspólnego czynnika przed nawias, idzie zwykłym zdaniem z przykładem
  na liczbach, żeby uczeń nie szukał w tablicy czegoś, czego tam nie ma (Henrich, 2026-08-21).
- **Żadnych myślników ani podkreśleń poza wzorami.** `-`, `—`, `_` mylą się z minusem,
  zwłaszcza w zdaniu, w którym obok stoi liczba ujemna. Zamiast myślnika: przecinek, kropka
  albo nowa linijka.

## Zasady krok po kroku, wersja krótka (ustalone 2026-08-21 na zad. 2)

Twarde reguły. Przed renderem przeczytaj, po renderze sprawdź.

### Ile kroków

1. **Jeden krok = jedno przekształcenie.** Robisz dwie rzeczy naraz, rozbij na dwa kroki.
2. **Tyle kroków filmu, ile linijek w rozwiązaniu opisowym, ale to jest DOMYŚLNIE, a nie
   za wszelką cenę** (zluzowane przez Henricha 2026-08-30: „rozwiązania krok po kroku
   i zwykłe nie muszą być koniecznie ze sobą zgrane, szczególnie jeśli miałoby to zaszkodzić
   uczniowi w zrozumieniu któregoś z nich"). Zaczynaj od jeden do jednego, po kolei, i trzymaj
   się tego, dopóki nic nie boli. Rozjazd jest dozwolony wtedy, gdy któraś forma traci na
   dopasowaniu: film ma swoje kroki bez rachunku (sprzątanie kadru, podsumowanie), a tekst
   swoje zdania, których film nie musi rozbijać na osobne kropki. **Rozjazd ma być decyzją,
   nie zaniedbaniem**: jeśli zmieniasz jedno, przejrzyj drugie i albo popraw, albo świadomie
   zostaw.
3. **Jeden wzór na jeden krok.** Krok bez wzoru (sam rachunek na liczbach) jest w porządku.
   Wzór w ramce pod filmem tylko wtedy, gdy stoi w tablicy; reszta zwykłym zdaniem.
4. **Dwie niezależne rzeczy licz PO KOLEI, nie równolegle** (Henrich, 2026-08-21, zad. 7).
   Najpierw jedno równanie do końca, potem drugie. Wynik pierwszego etapu odjeżdża na górę
   kadru i tam zostaje, więc na końcu obie wartości są na ekranie i mogą zjechać w jeden
   zapis. Samo przejście („wynik w górę, wjeżdża drugie równanie") jest osobnym krokiem,
   inaczej ostatnia klatka nie zgadza się z pierwszą klatką następnego kroku.
5. **Krok, który tylko coś wybiera albo przesuwa** (wyjęcie jednego równania z klamry,
   odstawienie wyniku na górę), nie ma koloru: nic się w nim nie przelicza.

### Przebieg kroku

6. **Każdy krok wygląda tak samo:**
   wszystko czarne → kluczowy element zapala się na zielono → animacja przekształcenia,
   zielone zostaje zielone → wszystko znów czarne.
7. **Krok zaczyna się i kończy tym samym czystym obrazem.** Dzięki temu zgodność ostatniej
   klatki kroku N z pierwszą klatką kroku N+1 wychodzi sama, bez przenoszenia podświetlenia
   między plikami.
8. **Kolejność na końcu kroku:** zgaszenie koloru → podmiana na czysty następny stan →
   `self.wait(0.25)`. Nie odwrotnie: przytrzymanie po Transformie trzyma obiekty, które
   potrafią różnić się od czystego stanu.
9. Zakaz z punktu 0 workflow nadal obowiązuje: **nigdy `self.clear()` bez natychmiastowego
   `self.add()`** czegoś w zamian.

### Kolor

10. **Zielony to `#2e7d32`** (`--accent-green`), ten sam, którym zaznacza rozwiązanie opisowe.
11. **Zielone jest to, co się ZMIENIA**: znika, pojawia się, zmienia wartość albo zmienia rolę.
   **Czarne zostaje to, co jedzie w nowe miejsce zapisu, ale dalej znaczy to samo.**
   - `1/5` → `5^{-1}`: piątka dalej jest tą samą piątką i tylko jedzie na podstawę, więc czarna.
     Zielona jest jedynka, która pojawia się jako wykładnik piątki w mianowniku (`1/5 = 1/5^1`),
     a potem jedzie na miejsce wykładnika, oraz minus, który przy tym powstaje. Dlaczego
     dwoma ruchami, a nie jednym: punkt 17 niżej.
   - `⁵√5` → `5^{1/5}`: liczba spod pierwiastka była podstawą i nią zostaje, więc czarna.
     Zielony jest znak pierwiastka (znika), licznik `1` (pojawia się) i stopień pierwiastka,
     bo przestaje być stopniem, a zaczyna być mianownikiem wykładnika.
   - W razie wątpliwości pytaj Henricha, to jego rozstrzygnięcie.
12. **Krok, w którym nic się nie zmienia, nie ma koloru.** Pierwszy krok (samo zapisanie
    zadania) jest cały czarny.
13. **Nawiasów nie koloruj** (Henrich, 2026-08-21), nawet gdy nawias właśnie się pojawia
    albo znika. Kolor noszą liczby i litery, nie znaki zapisu. Tak samo **podstawa potęgi
    zostaje czarna**, także ta, która dopiero się pojawia: podstawa to dalej ta sama liczba.
14. **Gaś DOKŁADNIE to, co po przekształceniu leży w kadrze.** `Transform` zostawia na
    ekranie obiekt ŹRÓDŁOWY (a po `Transform(VGroup(a, b), cel)` oba składniki grupy), więc
    wpisanie do gaszenia celu albo połowy źródeł daje najbrzydszy możliwy efekt: część zapisu
    gaśnie, a część zostaje zielona aż do cięcia. Sprawdzalne maszynowo: licz zielone piksele
    klatka po klatce, krzywa ma zjechać do zera jednym ruchem.

### Ruch

15. **Znak, który zmienia znaczenie, ma się w to nowe znaczenie ZAMIENIĆ, a nie zniknąć.**
    Plus z wykładnika `2^{96+4}` przy rozdzielaniu na iloczyn zjeżdża w dół i staje się kropką
    mnożenia; nie wygaszamy go, dokładając obok nową kropkę (Henrich, 2026-08-21).
16. **Co nie zmienia formy, ma się PRZESUWAĆ, nie morfować.** Podstawa potęgi ma dojechać
    na miejsce, a nie przelać się w inną podstawę.
17. **Nie przewoź znaku między miejscami, które nic ze sobą nie mają** (Henrich, 2026-08-23,
    na zad. 2, krok 3). Jedynka z licznika ułamka nie ma jechać do wykładnika: uczeń widzi
    lot przez pół kadru i nie wie, co się właściwie stało. Brakujące ogniwo dopisz jawnie
    i rozbij ruch na dwie animacje w tym samym kroku: najpierw pojawia się to, czego dotąd
    nie było widać (tu zielona jedynka jako wykładnik piątki w mianowniku), dopiero potem
    ten sam znak jedzie na miejsce docelowe, a to, co przestaje być potrzebne, znika w tym
    samym ruchu (tu „1/" gaśnie, a w wykładniku pojawia się minus).
18. **Pary wskazuj ręcznie, co do glifu. Żadnego automatycznego dopasowania.**
    Dotyczy to `TransformMatchingShapes` (paruje kształty po podobieństwie i wysyła cyfry nie
    tam, gdzie idą w rachunku) oraz `TransformMatchingTex(..., transform_mismatches=True)`,
    który wygląda niewinnie, a robi gorszą rzecz: **morfuje całą niedopasowaną stronę równania
    naraz**. W połowie takiej animacji pół zapisu jest kleksem i nie da się odczytać ani
    starego, ani nowego. Henrich, 2026-08-27, o pierwszej wersji zad. 8: „morf wrzucony na całą
    stronę równania zasłania to, co dzieje się naprawdę". Pisz więc jawnie, glif po glifie:
    `ReplacementTransform` na to, co jedzie w nowe miejsce, `FadeIn` na to, czego wcześniej nie
    było, `FadeOut` na to, co znika. Wzorzec: `solutionZad8.py`.
19. **Stany pisz jako `MathTex` pocięty na CZĘŚCI** (osobno podstawa, wykładnik, kropka,
    nawiasy). Wtedy parę wskazujesz czytelnym indeksem części, a nie zgadywanym numerem glifu.
20. **Mapę glifów policz, nie zgaduj.** Wyrenderuj podgląd, w którym każdy glif ma inny kolor
    i numer, i wpisz mapę w komentarz na górze sceny (wzorzec: `solutionZad2.py`).
21. **Pojawia się tylko to, czego wcześniej nie było** (nowy nawias, nowa kropka).
    Reszta ma skądś przylecieć.
27. **Nie prowadź niczego po literach. Lot ma iść bokiem albo górą** (ustalone 2026-08-27
    na zad. 8). Dwa miejsca, w których to wychodzi:
    - **czynnik wylatujący z dopisku działania** (`\big/ \cdot (x-1)`) najpierw staje NAD
      miejscem, w które wejdzie, i dopiero potem zjeżdża. Po skosie przez środek przechodziłby
      po całym równaniu. Wzorzec: funkcja `postoj()` w `solutionZad8.py`, kroki 10 i 12;
    - **składnik przenoszony na drugą stronę** leci `path_arc` nad znakiem równości, a nie
      przez niego. Po prostej przez ułamek sekundy leży dokładnie na nim i oba znaki są
      nieczytelne. Łuk dobierz do długości lotu: przy krótkim przeskoku `PI/3` jeszcze nie
      podnosi glifu ponad znak, `2*PI/3` już tak.
28. **Kopia, która ma trafić w dwa miejsca, rozdwaja się w obu naraz**, gdy działanie dotyczy
    obu stron równania (mnożenie obu stron). To jest ten rzadki przypadek, w którym dwie
    rzeczy dzieją się równolegle i tak ma być: uczeń widzi, że to jedna czynność.

### Wyjaśnienie w środku kroku (ustalone 2026-08-27 na zad. 8, dziś nieużywane)

Zasada Henricha: **krok może w środku pokazać wyjaśnienie, byle kończył się prostą linijką.**
Nie łam dla tego reguły „jeden krok = jedno przekształcenie": linijka, która zostaje w kadrze
na końcu kroku, dalej jest jedna. Zmienia się tylko to, że po drodze widać, SKĄD się wzięła.

**Uwaga, stan na 2026-08-28: pasa rachunku pomocniczego nie ma już w żadnej scenie.**
Zad. 8, jedyny użytkownik, został przepisany na wzór zad. 7 i każde ogniwo dostało tam
**własny krok**, pełnym pismem, w głównym pasie rachunku (kroki 8, 12, 14 i 18). Jest to
droższe, bo kroków robi się dziewiętnaście zamiast dziesięciu, ale uczeń w każdej klatce
widzi linijkę do przepisania, a nie zapis roboczy. Zanim sięgniesz po pas pomocniczy,
sprawdź, czy nie wystarczy dołożyć kroku.

29. **Rachunek pomocniczy liczy się w osobnym pasie pod równaniem, mniejszym pismem** (72
    zamiast 100), i **znika przed końcem kroku**. Dzięki temu ostatnia klatka kroku dalej jest
    czysta i styk klatek wychodzi sam, bez sztuczek.
30. **Rozmiar niesie znaczenie**: duże pismo to linijka rozwiązania, małe to praca na boku.
    Uczeń nie musi się zastanawiać, co przepisać do zeszytu.
31. **Wyjaśnienie to najczęściej dopisane OGNIWO**, czyli to, co ekspert liczy w głowie:
    \(2x-2 = 2\cdot x - 2\cdot 1 = 2(x-1)\), \(2(x+3) = 2\cdot x + 2\cdot 3\),
    \(x = 1x\). Wypisz je jawnie, potem zwiń do wyniku.
32. **To samo ogniwo ma stać w komentarzu rozwiązania opisowego.** Film i tekst mają tłumaczyć
    to samo w tym samym miejscu, inaczej uczeń dostaje dwie różne wersje rachunku.
33. **Wolny krok jest w porządku, ale krótkie kroki są lepsze.** Wersja zad. 8 z 2026-08-27
    wyprowadzała całą dziedzinę w JEDNYM kroku trwającym dwanaście sekund i Henrich to
    zaakceptował. Wersja z 2026-08-28 rozbiła to na sześć kroków po parę sekund, dwoma
    torami jak w zad. 7. Zasada, która z tego zostaje: założenie nigdy nie spada z nieba,
    a jeśli wybierasz między jednym długim krokiem a kilkoma krótkimi, bierz krótkie.

### Układ kadru (ustalone 2026-08-27 na zad. 8)

34. **Warunek, który obowiązuje przez całe zadanie (dziedzina, założenie), stoi NAD rachunkiem,
    przy lewej krawędzi** i zostaje tam do końca filmu. Tak zapisuje się go na kartce: najpierw
    warunek, pod nim liczenie. Do 2026-08-27 wisiał pod równaniem i czytał się jak dopisek
    zrobiony na końcu (poprawione na prośbę Henricha).
35. **Trzy pasy, zawsze te same**: warunek na górze, rachunek na środku, a pod spodem pas
    roboczy. W zad. 8 ten dolny pas trzymają dziś **dwa tory dziedziny** (kroki 2 do 7,
    pełnym pismem, bo to są linijki rozwiązania), a od kroku 8 zostaje pusty. Rachunek nie
    rusza się przez cały film, więc oko wie, gdzie patrzeć.
36. **Szarość zamiast czerni tam, gdzie coś nie jest rachunkiem**: założenie `#666666`
    (czytelne, ale słabsze), dopisek działania `#888888` (jeszcze słabsze, bo to zapowiedź,
    a nie zapis). Sprawdzone `tools/odwroc-kolor.py`: w ciemnym motywie wychodzą `#959595`
    i `#6a6a6a`, czyli nadal czytelnie.

### Podstawianie do wzoru i przywoływanie wartości (ustalone 2026-08-28 na zad. 9)

Uwagi Henricha po pierwszej wersji filmu do zad. 9. Wszystkie sprowadzają się do jednego:
**liczba nigdy nie pojawia się z niczego, tylko przylatuje stamtąd, skąd ją wzięliśmy.**

37. **Liczba wchodząca do wzoru ma PRZYLECIEĆ z miejsca, w którym została odczytana.**
    `FadeIn` w miejscu docelowym uczy „coś się wstawiło", a nie „to jest ten sam \(b\),
    którego odczytaliśmy dwa kroki wcześniej". Podstawienie robi się dwutaktowo w jednym
    kroku: najpierw w kadrze staje wzór w postaci literowej (\(\Delta = b^{2} - 4ac\)),
    potem każda litera zamienia się w liczbę, która do niej dojechała.
38. **Wartość policzona wcześniej wraca w kadr, kiedy jest znów potrzebna.** Współczynniki
    odczytane przed liczeniem wyróżnika mają wrócić przy wzorze na pierwiastki, a nie
    wjeżdżać drugi raz znikąd.
39. **Wartości, której w zapisie NIE WIDAĆ, najpierw dopisz na jej miejscu.** Przy
    \(x^{2}\) nie stoi żadna liczba, więc najpierw pojawia się tam jedynka, i dopiero
    z niej rodzi się \(a = 1\). To ta sama zasada, co ogniwo \(x = 1x\): brakujący znak
    staje się widoczny tam, gdzie należy, a dopiero potem wędruje.
40. **Dwa wzory, z których korzysta się po kolei, wjeżdżają razem, a używa się ich
    pojedynczo.** Najpierw oba stoją w kadrze, potem pierwszy dostaje podstawienie i wynik,
    dopiero potem drugi. Uczeń widzi, że to jeden wzór z \(\pm\), a nie dwa różne przepisy.
41. **Zapisy odstawione obok siebie są MNIEJSZE od rachunku i wyraźnie rozdzielone.** Trzy
    współczynniki złożone tym samym pismem co równanie i postawione blisko siebie czytają się
    jak jedno długie wyrażenie.

45. **Krok, ktory zaczyna sie od razu animacja, dostaje krotki `self.wait(0.2)` na
    starcie** (zmierzone 2026-08-28 na zad. 9, krok 22). Pierwsza klatka pliku jest wtedy
    czystym stanem koncowym poprzedniego kroku, a nie klatka `t = 0` animacji, ktora potrafi
    juz roznic sie o wlos. Styk 21 do 22 podskoczyl z 0,99895 (ponizej progu) na 0,99924
    samym dodaniem tego postoju.

### Kiedy krok NIE zasługuje na własną kropkę (ustalone 2026-08-28 na zad. 10)

42. **„Jeden krok = jedno przekształcenie" dotyczy RACHUNKU.** W filmie, który nie liczy,
    tylko czyta rysunek, jednostką kroku jest jedna myśl, a nie jeden symbol. Dwa końce tego
    samego przedziału odczytane tym samym sposobem to jeden krok, nie dwa (Henrich: „krok 2
    i 3 mogą być razem", „kroki 11, 12 i 13 mogą być połączone"). Rozbicie na osobne kropki
    ma sens dopiero wtedy, gdy każda niesie inną myśl.
43. **Krok, który tylko nazywa to, co i tak zaraz widać, wypada.** W zad. 10 osobny krok
    z warunkiem \(y < 0\) i strzałką w dół został wycięty: następny krok zapala fragment
    wykresu pod osią, więc strzałka nie dokładała niczego.
44. **Elementy tej samej roli mają jeden rozmiar i jedno wyrównanie.** Przedział budowany
    pod nagłówkiem części i ten sam przedział na liście odpowiedzi to jedna rzecz w dwóch
    chwilach, więc nie wolno im się różnić wielkością ani osią, do której są dosunięte.

### Sceny z wykresem: co psuje styk klatek (ustalone 2026-08-28 na zad. 11 i 12)

Cztery sceny do zadań 11, 12.1, 12.2 i 12.3 to pierwsze, w których przez cały film stoi
w kadrze **wykres**: prosta albo parabola. Okazało się, że `tools/styk-klatek.sh` schodzi
wtedy poniżej progu 0,999 nawet wtedy, gdy obraz jest identyczny co do treści, bo cienka
krzywa i szara siatka to dużo drobnego szczegółu, a koder H.264 koduje ostatnią klatkę
kroku i pierwszą klatkę następnego pliku niezależnie od siebie. Wszystkie cztery punkty
niżej są **zmierzone**, każdy osobnym renderem, a nie wydedukowane.

46. **Podświetlenie krzywej zmienia TYLKO kolor, nigdy grubość.** To była największa
    pojedyncza poprawka: zapalanie gałęzi paraboli przez `set_color(ZIELONY).set_stroke(width=9)`
    i gaszenie z powrotem na `width=6` przerysowuje krzywą, koder inaczej ustala jej brzeg
    i styk siada. Zdjęcie samej zmiany grubości podniosło styki zad. 12.1 z **0,9985 na 0,9998**.
    Przy okazji: zielona nakładka położona NA fioletowej krzywej jest gorsza od pomalowania
    samej krzywej, więc wykres dziel na kawałki (lewa gałąź, prawa gałąź) i zapalaj kawałek.
47. **Przytrzymanie na końcu kroku co najmniej 0,45 s.** Wymagane w punkcie 0 workflow
    `0.25` wystarcza scenom z samym rachunkiem, ale przy wykresie jest za krótkie:
    w zad. 11 trzy styki po `wait(0.3)` wypadały na 0,9988, a po podbiciu do `wait(0.45)`
    weszły na 0,9992 i wyżej. Dłużej niż 0,45 s nic już nie daje.
48. **Krok nie zaczyna się od największego ruchu w scenie.** Pierwsza klatka pliku jest
    klatką kluczową kodowaną razem z resztą swojego kawałka, więc gdy zaraz po niej jedzie
    cały wykres, dostaje mniej bitów i różni się od spoczynkowej klatki poprzedniego kroku.
    W zad. 12.3 przestawienie kolejności (najpierw strzałka „o ile", dopiero potem zsunięcie
    wykresu) podniosło styk **0,99854 na 0,99901**, a przy okazji jest lepsze dydaktycznie.
    Odwrotny zabieg, czyli `self.wait(0.2)` na starcie sekcji (punkt 45), przy wykresie
    **szkodzi**: wszystkie styki zad. 12.3 spadły wtedy do 0,9975.
49. **Siatka `#e0e0e0`, nie jaśniejsza.** `#e8e8e8` na białym tle jest tak słaba, że koder
    raz ją zostawia, a raz zgniata do bieli. Samo przyciemnienie siatki podniosło pierwszy
    styk zad. 12.1 z 0,9983 na 0,9995.
50. **Zanim uznasz spadek styku za błąd sceny, policz różniące się piksele.** Szum kodera
    wygląda inaczej niż przeskok obrazu: to kilkaset pikseli rozsianych po BRZEGU krzywej,
    a nie zwarty kształt.

    ```sh
    ffmpeg -sseof -0.05 -i stepN.mp4 -frames:v 1 /tmp/a.png -y
    ffmpeg -i stepN+1.mp4 -frames:v 1 /tmp/b.png -y
    python3 -c "
    from PIL import Image; import numpy as np
    A=np.asarray(Image.open('/tmp/a.png').convert('RGB')).astype(int)
    B=np.asarray(Image.open('/tmp/b.png').convert('RGB')).astype(int)
    d=np.abs(A-B).sum(axis=2); print('pikseli >30:', int((d>30).sum()))
    Image.fromarray((255-(d>30).astype('uint8')*255)).save('/tmp/roznica.png')"
    ```

    Obejrzyj `/tmp/roznica.png`. Zwarta plama znaczy prawdziwy przeskok i wtedy poprawiasz
    scenę. Sam kontur krzywej znaczy szum kodera i wtedy pomagają punkty 46 do 49.

### Wnioski z zadan 9, 11 i 12 (ustalone 2026-08-30)

51. **Krzywa, ktora urywa sie w powietrzu, klamie.** Wykres narysowany dokladnie do
    krawedzi planszy konczy sie WEWNATRZ kadru, wiec wedrujaca po nim kropka wyskakuje
    znikad i znika w niczym. Rysuj krzywa kawalek POZA kadr (w zad. 12.1 do \(y = -11{,}2\)
    przy planszy siegajacej \(-10{,}2\)); przycieta krawedzia czyta sie jako „to leci dalej",
    a punkt wjezdza i wyjezdza tam, gdzie powinien.
52. **Sprzatanie kadru zasluguje na wlasny krok.** Material, ktory zrobil swoje (dane
    z tresci, pas odczytu), ma zniknac, a jedyna wartosc potrzebna dalej jedzie na jego
    miejsce, na srodek. W zad. 12.2 dane wisialy do konca filmu i konkurowaly z rachunkiem;
    osobny krok „gora sie czysci, zostaje \(a = -1\)" kosztuje pare sekund, a reszta filmu
    ma czysty kadr. Krok bez rachunku jest tu w porzadku: jednostka kroku jest jedna mysl.
53. **Wzor z tablicy wjezdza na KONCU poprzedniego kroku.** Wtedy krok, ktory z niego
    korzysta, zaczyna sie od rachunku, a nie od wjazdu wzoru. Dwa zyski naraz: uczen ma wzor
    przed oczami, zanim zacznie sie przeksztalcenie, a pierwsza klatka pliku jest spokojna,
    wiec styk klatek nie siada (to samo, co punkt 48).
54. **Napis, ktory dorasta, ustawiaj z gory w calosci i odslaniaj po kawalku.** Lista
    odpowiedzi „Odpowiedzi: B", do ktorej w ostatnim kroku dochodzi „, D", musi byc
    zbudowana i wysrodkowana od razu jako cztery czesci; inaczej dopisanie drugiej litery
    przesuwa pierwsza i na styku widac skok.
55. **Nowa notatka w kadrze dostaje WLASNY wiersz.** Dwa zapisy postawione na tej samej
    wysokosci czytaja sie jak jedna dluga linijka, nawet gdy formalnie sie nie nachodza:
    w zad. 12.2 dopisek \(f(0) = -9\) stanal obok \(q = 0\) i gora kadru zlala sie w jeden
    ciag. Zlapane na `tools/klatki.sh stany`, nie w kodzie: w scenie obie wspolrzedne
    wygladaly na dobrze rozsuniete.

56. **`ReplacementTransform(cos, cel.copy())` zostawia tę kopię na ekranie.** To nie
    jest niewinny zapis „przekształć w coś takiego jak cel": `ReplacementTransform` na
    koniec USUWA źródło i DODAJE do sceny swój cel, więc każda `.copy()` podana jako cel
    zostaje w kadrze na stałe. Gdy dwa glify łączą się w jeden (\(5m + 1m \to 6m\),
    \(1 \cdot 6 \to 6\)), na wyniku leżą wtedy dwie albo trzy kopie tego samego znaku
    i całość wygląda na rozmazaną albo pogrubioną, a przy drugiej animacji w tym samym
    kroku część z nich zostaje w miejscu i widać zapis, którego już nie powinno być.
    Znalezione 2026-08-30 przez Henricha jako „krok 7 się źle renderuje" (zad. 15)
    i „strzałka q" (zad. 16); wzorzec siedział w obu scenach po kilka razy.

    Tego samego celu nie wolno też podać DWA razy bez `.copy()`: `Scene.replace` wymaga,
    żeby nowy obiekt nie był jeszcze w scenie, więc druga animacja doda go ponownie.

    Poprawnie łączenie zapisuje się tak: jeden składnik jedzie `ReplacementTransform`,
    a każdy następny **znika lecąc w to samo miejsce**:

    ```python
    ReplacementTransform(a, cel),
    FadeOut(b, target_position=cel.get_center(), scale=0.4),
    ```

    `Transform(cos, cel.copy())` jest bezpieczne (Transform celu do sceny nie dodaje),
    ale `.copy()` jest tam zbędne.

57. **Elementy sklejane ręcznie wyrównuj po LINII PISMA, nie po dole prostokąta.**
    `align_to(..., DOWN)` zrównuje dolne krawędzie ramek, a nawiasy, przecinki i litery
    z podcięciem sięgają poniżej linii pisma, więc zapis zaczyna chodzić po wysokości:
    przecinki jadą do góry, nawiasy wyglądają na przesunięte. Najprościej w ogóle tego
    nie sklejać: **jeden `MathTex` z kilkoma argumentami** składa LaTeX poprawnie, a każdy
    argument dalej jest osobnym podobiektem, więc uchwyty do pojedynczych kawałków zostają.
    Podpisy stawiane NAD częściami takiego zapisu licz od góry CAŁEGO zapisu, nie od góry
    swojej części: samotne `m` jest niższe niż `4+2m`, więc podpis liczony od niego zjeżdża
    w dół i wchodzi na nawias. Zad. 15, uwaga Henricha „wyraz w kroku 1 źle się renderuje".

### Po renderze

22. `tools/wgraj-kroki.sh <nr> <arkusz>` robi render, kopię, rewersy i styk klatek jedną komendą.
    **Rewersy przelicza od nowa**, bo po przerenderowaniu stare pokazują poprzednią animację.
23. **Styk klatek musi przejść** (`tools/styk-klatek.sh`, wchodzi w skład powyższego).
24. **Puść `tools/test-krokow.js`** na zadaniu, które ruszałeś.
25. **Obejrzyj klatki okiem.** „Wyrenderowało się bez błędu" nic nie znaczy.

    Model nie widzi plików mp4, widzi obrazki, więc robi to
    **[tools/klatki.sh](../tools/klatki.sh)** (dodane 2026-08-29). Kiedy sięgać po który
    tryb i na co patrzeć, mówi skill `.claude/skills/ogladanie-krokow/`:

    ```
    tools/klatki.sh stany matura/2024-grudzien/media/zad9/solution-step-by-step --koniec
    tools/klatki.sh film  <katalog> 7 --co 20    # jeden krok jako sekwencja, widać ruch
    tools/klatki.sh styk  <katalog> 3            # złącze 3/4 + podbita różnica
    ```

    **Domyślnie i najczęściej: `stany --koniec`.** Jeden obrazek pokrywa całe zadanie,
    kosztuje tyle co jedna klatka, a pokazuje cały tok rozwiązania jak zapis na tablicy.
    Przy PRACY nad sceną (a nie tylko przy odbiorze) to jest narzędzie pierwszego wyboru:
    po każdym przerenderowaniu jeden `stany --koniec` mówi, czy rachunek idzie poprawnie
    od pierwszego wiersza do ostatniego i czy nic nie zostało zielone na klatce brzegowej.

    **`film` nie jest obowiązkowy.** Sięgasz po niego dopiero wtedy, gdy `stany` da powód:
    coś w konkretnym kroku nie zgadza się z zamysłem i trzeba zobaczyć, co się dokąd rusza.
    Wcześniej stało tu „obejrzyj pierwszą, po zapaleniu koloru, w połowie ruchu i ostatnią",
    czyli wymuszenie `film` po każdym renderze; zdjęte 2026-08-30, bo płaciło się kontekstem
    za obrazki, które prawie zawsze potwierdzały to, co już było widać w `stany`.

    Tryb `styk` jest uzupełnieniem punktu 23: `styk-klatek.sh` mówi, ŻE para nie przechodzi,
    a ten pokazuje, GDZIE siedzi różnica, i podaje najjaśniejszy piksel różnicy w skali
    0-255 (kilka jednostek to szum kodera, nie usterka).

    **Gęste `--co` w trybie `film` kosztuje czytelnością, nie tokenami** (zmierzone
    2026-08-29 na zad. 7 i 10). Obrazek kosztuje tyle samo niezależnie od tego, ile kafelków
    jest w środku, ale im więcej kafelków, tym każdy mniejszy, i przy `--co 6` wzoru
    w kafelku już się nie odczyta. Stąd prosta reguła: **`--co 20` albo rzadziej, gdy chcesz
    PRZECZYTAĆ, co jest w kadrze; gęsto tylko wtedy, gdy oceniasz sam RUCH** (czy glif jedzie
    tam, gdzie powinien) i treść jest bez znaczenia.

    W trybie `film` bezruch (`self.wait`) jest odsiewany, bo pochłaniał połowę obrazka:
    na zad. 9, kroku 3 z 72 przerzedzonych klatek 44 były tą samą klatką. Wyrzucony czas
    jest jednak **oznaczony**, inaczej kratka kłamie: żółty podpis kafelka to czas w filmie
    w milisekundach (a nie numer po kolei), a pomarańczowy pasek „bezruch +0.45s" siedzi na
    kafelku, na którym obraz staje. Przerwa w ŚRODKU kroku bywa sygnałem, że krok robi dwie
    rzeczy zamiast jednej, czyli łamie zasadę 1 z „Zasad krok po kroku".
26. Sprawdzian koloru na sucho: pierwsza i ostatnia klatka każdego kroku mają mieć **zero**
    zielonych pikseli, środek ma mieć ich sporo. Sam zero na końcu **nie wystarcza**, bo cięcie
    i tak obcina obraz na czystym stanie. Policz zielone piksele w CAŁYM kroku, klatka po
    klatce, i popatrz na krzywą: ma zjechać do zera jednym ruchem. Zatrzymanie się na małej,
    stałej wartości tuż przed końcem znaczy, że jeden glif nie gaśnie razem z resztą.

    Robi to **[tools/zielen-krokow.py](../tools/zielen-krokow.py)** (dodane 2026-08-23),
    więc nie licz tego ręcznie:

    ```
    python3 tools/zielen-krokow.py matura/2024-grudzien/media/zad7/solution-step-by-step
    python3 tools/zielen-krokow.py <katalog> --krok 3 --krzywa   # jeden krok, klatka po klatce
    ```

    Skrypt wypisuje na każdy krok liczbę zielonych pikseli na starcie, w szczycie i na końcu,
    i sam zgłasza trzy usterki: brudną pierwszą klatkę, brudną ostatnią i zieleń gasnącą ratami.

### Pułapki Manima, na których te sceny się przejechały (2026-08-21, zad. 3 i 7)

Każda kosztowała osobny render, więc warto je znać z góry.

- **Polskie znaki NIE przechodzą przez `Tex()` ani `MathTex()`** (zmierzone 2026-08-25).
  LaTeX w tym obrazie jedzie w kodowaniu OT1, więc `Tex("Pole trójkąta")` wywala render
  z błędem `Command \k unavailable in encoding OT1` (to ogonek od „ą"). Napisy z polskimi
  znakami rób przez **`Text()`**, który idzie przez Pango i LaTeXa w ogóle nie dotyka;
  sprawdzone na pełnym „Zażółć gęślą jaźń ĄĆĘŁŃÓŚŹŻ". `Text()` i `MathTex()` wolno
  spokojnie łączyć w jednym `VGroup(...).arrange(RIGHT)`. W `solutionZad3.py` leży
  zakomentowany `MathTex` z „liczbą całkowitą" w środku, czyli ktoś już się na tym przejechał.
- **`Transform` zostawia w kadrze obiekt ŹRÓDŁOWY**, tylko wyglądający jak cel. Do gaszenia
  koloru wpisuj więc źródła, nie cele. A po `Transform(VGroup(a, b), cel)` w kadrze leżą OBA
  składniki grupy, więc oba trzeba wygasić. Tak właśnie gasło nierówno: pół zapisu czerniało,
  reszta zostawała zielona aż do cięcia.
- **Sklejanie kilku elementów w jeden**: każdą kopię przekształcaj osobno w `cel.copy()`
  (`Transform(drugie_2_96, k[5][0].copy())`). Wszystkie dojadą w to samo miejsce i nałożą się
  na siebie; nadmiarowe obiekty nie szkodzą, bo krok kończy się `clear()` plus `add()` czystego
  następnego stanu.
- **Uchwyt do połowy wykładnika bierze się z rozcięcia MathTexa na argumenty**, nie z indeksu
  glifu: `MathTex(r"2", r"^{96", r"+4}")` skleja się w LaTeXu w `2^{96+4}`, a daje osobny
  uchwyt do „96" i do „+4". Numery glifów zgaduje się źle i psują się przy każdej zmianie
  zapisu.
- **Do gaszenia nie wpisuj niczego, co wyszło z kadru przez `FadeOut`.** Animacja na
  obiekcie spoza sceny WSTAWIA go z powrotem, więc wygaszony kawałek zapisu wróciłby na
  ostatnią klatkę. Jeśli po kroku nie zostaje nic zielonego, wywołaj gaszenie z pustą listą.
- **Układ równań buduj z części, nie jednym `\begin{cases}`**: dwa `MathTex`-y ustawione
  `arrange(DOWN, aligned_edge=LEFT)` plus osobna klamra. Wtedy każde równanie ma własny
  uchwyt i da się je wyjąć z klamry. Klamrę skaluj `scale_to_fit_height`, a nie
  `stretch_to_fit_height`: rozciąganie tylko w pionie robi z niej cienką kreskę z haczykiem.
- **Klamra ma być ROZCIĄGALNA, a nie powiększonym małym nawiasem** (Henrich, 2026-08-29,
  zad. 7: „klamra jest za gruba, wygląda jakbyś powiększył zwykły nawias"). `MathTex(r"\{")`
  przeskalowany na wysokość dwóch równań rośnie w obie strony naraz, więc razem z wysokością
  tyje kreska i wychodzi klamra grubsza niż całe pismo obok. Rozciągalną klamrę LaTeX składa
  z osobnych kawałków o stałej grubości, więc rośnie sama w pionie:

  ```python
  # \rule to niewidzialna rozporka, która mówi LaTeX-owi, jak wysokiej klamry zażądać.
  # 40pt daje kształt zbliżony do \begin{cases}, więc dalsze skalowanie jest niewielkie.
  klamra = MathTex(r"\left\{\rule{0pt}{40pt}\right.", color=BLACK)
  klamra.scale_to_fit_height(VGroup(r1, r2).height * 1.35)
  ```

  Zmierzone porównanie czterech wariantów (`\{`, `\left\{\begin{array}…`, `\rule` 40pt
  i 80pt) na jednej klatce: 40pt wygrywa. Przy 80pt klamra jest już tak wyciągnięta, że gubi
  przewężenie w talii i czyta się jak pionowa kreska.
- **Kolor zapalaj animacją, nie przed pierwszym `play`.** Inaczej pierwsza klatka kroku jest
  już podświetlona, a ostatnia klatka kroku poprzedniego czysta, czyli dokładnie ten przeskok,
  którego pilnuje `tools/styk-klatek.sh`.
