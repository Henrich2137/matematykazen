Dziennik ukończonych zadań, partia bieżąca (otwarta 2026-07-27). Zasady formatu i podziału na pliki: patrz done/README.md — najnowsze wpisy na górze.

[ZROBIONE 2026-08-30] (Opus 5, medium) Zadania 9, 10, 11, 12.1, 12.2 i 12.3 z grudnia 2024:
druga runda uwag Henricha, plus zluzowanie reguły „film jeden do jednego z tekstem".
[2024-grudzien, zad9, zad10, zad11, zad12, manim, widzety, kolory, zasady]

Wersja v103. Uwagi z TODO.md, wszystkie wykonane.

- **Zad. 9, trzy ostatnie kroki filmu.** Wraca w kadr nierówność w postaci z zerem po prawej
  (\(1x^{2} - 6x - 7 \le 0\)), nad linijką wyników. Podczas rysowania paraboli zapala się
  w niej JEDYNKA przy \(x^{2}\), bo to ona odpowiada na pytanie, dlaczego ramiona idą
  w górę. Przy zaznaczaniu fragmentu pod osią zapala się \(\le 0\): to samo pytanie raz
  zapisane, raz narysowane. W ostatnim kroku nierówność znika na starcie i odpowiedź
  zostaje w kadrze sama.

- **Zad. 10, widżet.** Suwak nie dochodzi już do \(-4\) i to WIDOCZNIE: lewy koniec to
  \(-3{,}76\), czyli jedenaście pikseli od kółka. Stało tam \(-3{,}98\), formalnie poprawnie,
  ale różnica wynosiła niecały piksel, więc punkt siadał na kółku otwartym i wyglądało to
  tak, jakby \(-4\) należało do dziedziny. Drugi szczegół, złapany dopiero na zrzucie:
  `min` suwaka musi dzielić się przez `step`, bo przeglądarka liczy dozwolone wartości jako
  `min + k * step`; przy \(-3{,}75\) i kroku \(0{,}02\) zero było nieosiągalne i widżet
  startował od \(x = 0{,}01\).

- **Zad. 11, rozwiązanie zwykłe.** Werdykt każdego zdania dostał własną linijkę pod wynikiem,
  a zamknięcie brzmi „Odpowiedzi: **P**, **F**". Przedtem werdykt był doklejony do linijki
  z wynikiem i ginął w rachunku.

- **Zad. 12.1, film.** Wędrująca kropka wjeżdża zza krawędzi kadru i wyjeżdża za nią.
  Parabola jest rysowana kawałek poniżej dolnej krawędzi; przedtem kończyła się wewnątrz
  kadru, więc kropka wyskakiwała znikąd i znikała w niczym.

- **Zad. 12.1, widżet: kolory kłamały o odpowiedzi.** Gałąź rosnąca była na stałe ZIELONA,
  malejąca na stałe CZERWONA, a pytanie brzmi „w jakim przedziale funkcja maleje", więc
  poprawna odpowiedź świeciła na czerwono, a dystraktor na zielono. Teraz cała parabola jest
  fioletowa, zapala się na zielono ta gałąź, na której właśnie stoi punkt ucznia, punkt jest
  błękitny (rola „podstawianie pod \(x\)"), wierzchołek pomarańczowy. Zieleń jest RUCHOMA,
  więc znaczy „tu jesteś", a nie „to jest dobra odpowiedź".

- **Zad. 12.2, film przebudowany: czternaście kroków zamiast dwunastu.** Krok 1 pokazuje
  trójkę danych naraz (wzór postaci kanonicznej, punkt \(W\), punkt \(A\)); punkt
  \((0,\ -9)\) nazywa się teraz \(A\), a \(f(0) = -9\) dopisuje się dopiero przy
  podstawieniu, jako tłumaczenie „przechodzi przez \(A\)" na język równania. Krok 8 CZYŚCI
  GÓRĘ KADRU: dane i pas odczytu znikają, a \(a = -1\) jedzie na ich miejsce, na środek.
  Wzór na kwadrat różnicy wjeżdża już na końcu kroku 10. Lista odpowiedzi to
  „Odpowiedzi: B, D". Krok 14 zdejmuje \(a = -1\) i zostawia w kadrze obie postacie wzoru,
  jedna pod drugą.

- **Zad. 12.3, film.** W kroku 2 na zielono zapala się nie tylko strzałka „o ile", ale też
  \(- 1\) we wzorze \(g\).

**Zasada zluzowana przez Henricha: film i rozwiązanie zwykłe nie muszą być jeden do jednego**
(„szczególnie jeśli miałoby to zaszkodzić uczniowi w zrozumieniu któregoś z nich"). Zaczyna
się od jeden do jednego i trzyma tego, dopóki nic nie boli; rozjazd ma być decyzją, nie
zaniedbaniem. Zapisane w `manimations/README.md` (punkt 2), `SOLUTION_TEXT_RULES.md`
(punkt 6) i `CLAUDE.md`.

**Zdjęty przymus trybu `film` w `tools/klatki.sh`.** `manimations/README.md` kazał po każdym
renderze obejrzeć „pierwszą klatkę, po zapaleniu koloru, w połowie ruchu i ostatnią", czyli
wymuszał `film`. Płaciło się kontekstem za obrazki, które prawie zawsze potwierdzały to, co
już widać w `stany`. Teraz `stany --koniec` jest narzędziem pierwszego wyboru do CAŁEJ pracy
nad sceną (jeden obrazek na zadanie, koszt jednej klatki), a `film` odpala się dopiero, gdy
`stany` da powód. Dopisany też wniosek o gęstości: `--co 20` albo rzadziej, gdy chcesz
PRZECZYTAĆ, co jest w kadrze; gęsto tylko wtedy, gdy oceniasz sam RUCH, bo przy `--co 6`
wzoru w kafelku już się nie odczyta.

**Pięć nowych reguł w `manimations/README.md` (51 do 55), wyciągniętych z tej paczki:**
krzywa musi wychodzić poza kadr, sprzątanie kadru zasługuje na własny krok, wzór z tablicy
wjeżdża na końcu poprzedniego kroku, napis który dorasta ustawia się z góry w całości,
nowa notatka dostaje własny wiersz. Do tego sekcja „Kolor nie może odpowiadać na pytanie
zadania" w `COLORS.md`, powtórzona w `widgets/PROJEKTOWANIE.md` i w skillu
`projektowanie-rozwiazan`.

**W OVERVIEW.md doszła statystyka „Odpicowane: 6 (zad. 7-12)"** — jedyna liczba w tej sekcji,
której `tools/statystyki.py` nie policzy, bo to ocena, a nie pole w danych. Podbija się ją
ręcznie po zamknięciu paczki uwag.

Sprawdzone: `tools/styk-klatek.sh` bez zastrzeżeń na czterech scenach (zad. 9 dwadzieścia
styków, 12.1 cztery, 12.2 trzynaście, 12.3 cztery); `tools/zielen-krokow.py` bez zastrzeżeń
na wszystkich czterech; `tools/test-krokow.js --zadania=8,12,13,14` bez zastrzeżeń;
`tools/klatki.sh stany --koniec` na zad. 9 i 12.2, `film` na krokach 3 i 4 zad. 12.1 oraz
kroku 2 zad. 12.3; zrzuty rozwiązań zad. 10, 11 i 12.1 przez `tools/zrzut-rozwiazania.js`.
Pierwsza wersja układu 12.2 padła właśnie na obrazku ze `stany`: dopisek \(f(0) = -9\)
stanął obok \(q = 0\) i cała góra kadru czytała się jako jedna linijka.


[ZROBIONE 2026-08-29] (Opus 5, medium) Zadania 7, 8, 9 i 10 z grudnia 2024: paczka poprawek
Henricha do filmów i rozwiązań zwykłych.
[2024-grudzien, zad7, zad8, zad9, zad10, manim, solution-text, css]

Uwagi z TODO.md, wszystkie wykonane. Wersja v102.

- **Zad. 7, film, klamra układu.** Henrich: „klamra jest za gruba, wygląda jakbyś powiększył
  zwykły nawias". I dokładnie tym była: `MathTex(r"\{")` przeskalowany `scale_to_fit_height`
  na wysokość dwóch równań, więc razem z wysokością rosła grubość kreski. Zamiast tego
  klamra ROZCIĄGALNA, składana przez LaTeX z kawałków o stałej grubości:
  `MathTex(r"\left\{\rule{0pt}{40pt}\right.")`. Zmierzone porównanie czterech wariantów
  na jednej klatce (`\{`, `\left\{\begin{array}…`, `\rule` 40pt i 80pt): 40pt wygrywa,
  80pt gubi już przewężenie w talii. Zasada dopisana do manimations/README.md.

- **Zad. 7, rozwiązanie zwykłe.** Brakowało komentarzy, jakie mają zadania 8 do 17. Doszło
  siedem zdań między wierszami, w tym wyjaśnienie znaku przy \(a \cdot (-1)\) i porządku
  zapisu przy \(b \cdot 6 = 6b\). Wytłuszczone są też wyniki cząstkowe \(a = -2\)
  i \(b = 1\). Komentarz w układzie DWUTOROWYM musi stać wewnątrz siatki (nowa reguła CSS
  `.rozw-2kol > .rozw-wiersz.rozw-pelny > .rozw-komentarz`), bo każdy blok `.rozw-2kol`
  liczy szerokość kolumn osobno i rozbicie rachunku na kilka bloków rozjeżdża tory w pionie.

- **Zad. 8, sprawdzenie.** Zdjęta pozioma kreska nad częścią „Sprawdzenie" (Henrich:
  „wygląda to jakby było oddzielną częścią niż rozwiązanie zwykłe"). Odstęp został tej samej
  wielkości, co dawny margines plus wypełnienie (3,9em). Po samym słowie „Sprawdzenie." idzie
  nowa linijka, a zdanie o nawiasie przy liczbie ujemnej stało się komentarzem.

- **Zad. 9, film, pas notatek.** Pas był wyśrodkowany dla całej czwórki (a, b, c, pierwiastek
  z delty), a czwarta notatka dołącza dopiero w kroku 10, więc przez pięć kroków trzy widoczne
  notatki wisiały zsunięte w lewo. Teraz środek liczy się dla trójki, a w kroku 10 cały pas
  zjeżdża w lewo i czwórka staje na środku. Pas poszedł też o 0,15 jednostki wyżej.

- **Zad. 9, film, koniec.** Dawne kroki 19 i 20 to dziś jeden krok, więc film ma 21 kroków
  zamiast 22. Krok 19 sklejał wcześniej oba wyniki w jedną linijkę przez przecinek, a dopiero
  krok 20 odsyłał ją w górę i rysował parabolę. Sklejanie niczego nie liczyło, a OBA kroki
  robiły `Transform` na kopii stanu i podmieniały obiekt na scenie (`remove` + `add`), przez
  co linijka wyników mrugała na styku. Teraz w górę jadą te same obiekty, które już stoją
  w kadrze. Rozwiązanie zwykłe poszło za tym: linijka „a = 1 > 0, ramiona w górę" wtopiła się
  w komentarz pod miejscami zerowymi.

- **Zad. 9, drobiazgi.** Przerwa przed „Miejsca zerowe" (`rozw-odstep`) i przerwa między
  poleceniem widżetu a płótnem (`.widget-title` margin-bottom 4px → 16px, dotyczy wszystkich
  widżetów).

- **Zad. 10, film przepisany od nowa: pięć kroków zamiast dziewięciu.** Henrich: „zapisy
  przedziałów, które pojawiają się pod nagłówkami, źle się renderują". Renderowały się źle
  z powodu, który był w samym pomyśle: przedział powstawał ze SKRAWKÓW (`"(-4"`, `",\ "`,
  `"4\rangle"`) ustawionych obok siebie przez `arrange()`, a trzy osobne `MathTex`-y nie
  stoją na wspólnej linii bazowej i mają przypadkowy odstęp. Etap pośredni wypadł w całości:
  zielony pas na osi zamienia się od razu w gotowy przedział, złożony jednym `MathTex`-em,
  i ląduje wprost na liście odpowiedzi. Krok 1 to sam rysunek, kroki 2 do 5 to po jednym
  zdaniu do uzupełnienia, każdy tym samym schematem (podświetlenie na wykresie, rzut
  kreskowany na oś, zielony pas z właściwymi końcami, pas zamienia się w zapis). Schemat
  wzięty z dawnego kroku 9, o którym Henrich napisał, że wygląda świetnie.

- **Zad. 10, rozwiązanie zwykłe.** Dziedzina wyprowadzana ze WZORU, a nie opisywana słowami
  z wykresu: w kadrze stoi definicja klamrowa z zieloną częścią `(-4` w pierwszym wierszu
  i `4⟩` w ostatnim, a pod nią gotowa dziedzina. Pozostałe trzy części skrócone.

- **Dwa tory na telefonie.** Przy oknie 485px (telefon Henricha) na kolumnę zostaje około
  200px i najdłuższa linijka zad. 7 („a · (-1) + 3 · 6 = 20") łamała się po znaku równości,
  zostawiając samo „20" w drugim wierszu. `.rozw-2kol.rozw-dwatory` dostało poniżej 560px
  `font-size: 0.85em`; przy tym rozmiarze mieszczą się też wszystkie ułamki zad. 9.

Sprawdzone: `tools/styk-klatek.sh` bez zastrzeżeń na wszystkich trzech scenach (zad. 7
trzynaście styków, zad. 9 dwadzieścia, zad. 10 cztery); `tools/test-krokow.js
--zadania=6,8,9` bez zastrzeżeń; klatki obejrzane przez `tools/klatki.sh` (tryb `stany`
dla zad. 9 i 10, tryb `film` dla kroku 1 zad. 7 i kroku 2 zad. 10); zrzuty rozwiązań
zwykłych desktop i 485px nowym `tools/zrzut-rozwiazania.js`.


[ZROBIONE 2026-08-28] (Opus 5, high) Zadania 9 i 10 z grudnia 2024, wersja druga: poprawki
Henricha do filmów i rozwiązań, plus zasady wyciągnięte z tych uwag.
[2024-grudzien, zad9, zad10, manim, solution-text, zasady]

Henrich obejrzał pierwszą wersję (v95) i wpisał uwagi do TODO.md. Wszystkie wykonane.

- Zad. 9, dwadzieścia dwa kroki zamiast dwudziestu jeden. Krok 5 najpierw dopisuje jedynkę
  przed \(x^{2}\), i dopiero z niej rodzi się \(a = 1\). Krok 6 pokazuje wzór na deltę
  w postaci literowej, a wartości przylatują z pasa notatek na miejsca liter, zamiast
  pojawiać się z niczego. Krok 10 wprowadza OBA wzory na pierwiastki, tak jak stoją
  w tablicy, a potem pierwszy jest liczony do końca i dopiero potem drugi; wartości wracają
  z pasa za każdym razem. Pas notatek (a, b, c, a od kroku 10 też pierwiastek z delty) stoi
  pod rachunkiem mniejszym pismem i rozsunięty.
- Zad. 10, dziewięć kroków zamiast szesnastu. Oba końce przedziału odczytuje się jednym
  krokiem, krok ze strzałką \(y < 0\) wypadł, a w ostatnim kroku znika etykieta części,
  więc na koniec w kadrze zostaje sam wykres i cztery odpowiedzi. Pierwsza część idzie
  wolniej (trzy kroki), bo tam pierwszy raz tłumaczy się kółko i kropkę.
- Zasady spisane tam, gdzie ich poszuka następna sesja: manimations/README.md punkty 37 do 45
  (liczba przylatuje z miejsca odczytu, wartość wraca gdy znów potrzebna, brakującą jedynkę
  najpierw dopisz na jej miejscu, dwa wzory używane po kolei wjeżdżają razem, notatka obok
  rachunku jest mniejsza; osobno: kiedy krok NIE zasługuje na własną kropkę i po co postój
  na starcie kroku), SOLUTION_TEXT_RULES.md 15j do 15l oraz punkt 2c w skillu
  projektowanie-rozwiazan.
- Dwie pułapki złapane po drodze i zapisane: Manim nie czyści katalogu sections, więc przy
  ZMNIEJSZANIU liczby kroków trzeba go usunąć ręcznie (inaczej wgrywa się mieszanka dwóch
  wersji); a kopia znacznika dołożona wprost na oryginał robi podwójną krawędź już
  w pierwszej klatce kroku i psuje styk klatek.
- Zmierzone: styki klatek obu zadań w całości powyżej progu (zad. 9 od 0,99924, zad. 10 od
  0,99929), zieleń kroków i tools/test-krokow.js bez zastrzeżeń, strona bez błędów KaTeX
  i bez przewijania w bok na 1280 i 485 px. Wersja v96.

[ZROBIONE 2026-08-28] (Opus 5, high) Zadania 9 i 10 z grudnia 2024: rozwiązanie opisowe
i film krok po kroku napisane od nowa, na wzór zadań 7 i 8.
[2024-grudzien, zad9, zad10, manim, solution-text, wykres]

Projekt dydaktyczny powstał najpierw jako osobny dokument
(issues/projekt-zad9-zad10-2024-grudzien.md) i dopiero potem był wykonywany, więc opis
kroków, kolory i liczba linijek były ustalone przed pisaniem sceny.

- Zadanie 9 (nierówność \(x(x-6) \le 7\)): dwadzieścia jeden linijek i dwadzieścia jeden
  kroków zamiast siedmiu i ośmiu, czyli koniec rozjazdu tekst/film. Ogniwa liczone dotąd
  w głowie dostały własne kroki: \(x \cdot x - x \cdot 6\), odczyt współczynników
  (tu ginie \(c = -7\)), \(36 + 28\) przed \(64\), \(-(-6)\) przed \(6\), oba
  dzielenia. Miejsca zerowe idą dwoma torami po kolei, jak w zad. 7. Trzy ostatnie kroki
  rysują szkic paraboli: wcześniej wniosek „ramiona w górę, więc między pierwiastkami"
  niósł wyłącznie zwinięty opis pod filmem, a to jest krok wart punktu CKE.
- Zadanie 10 (odczyt z wykresu): pierwszy film w projekcie, który nie rozpisuje rachunku,
  tylko czyta rysunek. Szesnaście kroków, wykres po lewej stoi przez cały film, po prawej
  rośnie lista czterech odpowiedzi, więc na końcu widać wszystkie naraz. Cztery pytania to
  cztery różne ruchy: rzut na oś x, rzut na oś y, fragment pod osią, poziom największej
  wartości. Rozwiązanie opisowe napisane w jedną całość, więc zniknął doklejony blok
  „DAWNE POKAŻ WIĘCEJ" (zostają zad. 19 i 30).
- Zmierzone: styki klatek zad. 9 od 0,99900 do 0,99995 bez zastrzeżeń, zieleń kroków
  i tools/test-krokow.js bez zastrzeżeń w obu zadaniach, strona bez błędów KaTeX i bez
  przewijania w bok na 1280 i 485 px. W zad. 10 dwa styki (1→2 i 2→3) wypadają 0,9988;
  pomiar wyklucza różnicę treści, przyczyny NIE ustalono i tak jest to zapisane.
- Wzorce dopisane do SOLUTION_TEXT_RULES.md (wiersze 9 i 10 w tabeli), kroki opisowo
  w manimations/zad9-kroki.md i zad10-kroki.md, statystyki i OVERVIEW zaktualizowane
  (wideo 10/33), wersja v95.

[ZROBIONE 2026-08-27] (Opus 5, medium) Domknięcie zad. 8: założenie przeniesione nad rachunek,
rozwiązanie opisowe zgrane z filmem, a wzorzec z tej pracy wpisany do plików z zasadami.
[2024-grudzien, zad8, manim, zasady, solution-text, colors]

Trzy rzeczy w jednej paczce, wszystkie z uwag Henricha po obejrzeniu poprzedniej wersji:

1. Założenie stoi teraz NAD rachunkiem, przy lewej krawędzi kadru, a nie pod nim. Tak
   zapisuje się warunek na kartce: najpierw założenie, pod nim liczenie. W kroku 2 oba wyniki
   schodzą się w jeden i jadą pionowo w górę, wzdłuż lewego brzegu, żeby nie przelatywać po
   literach równania. Kadr ma odtąd trzy stałe pasy: warunek, rachunek, rachunek pomocniczy.
2. Rozwiązanie opisowe doszlifowane pod film: te same ogniwa pośrednie w komentarzach
   (2x = 2*x oraz 2 = 2*1, 2*x = 2x oraz 2*3 = 6, x to 1x), to samo uzasadnienie mnożenia
   obu stron i to samo zdanie o zmianie znaku. Dziesięć linijek na dziesięć kroków, treść
   też się zgadza, nie tylko liczba.
3. Zasady spisane tam, gdzie ich szuka następna sesja:
   - manimations/README.md: zasada 18 rozszerzona o zakaz TransformMatchingTex z
     transform_mismatches, nowe zasady 27 i 28 (lot bokiem albo górą, postój nad celem, łuk
     nad znakiem równości), nowe sekcje „Wyjaśnienie w środku kroku" (29 do 33) i „Układ
     kadru" (34 do 36),
   - SOLUTION_TEXT_RULES.md: 15g (komentarz niesie ogniwo, którego w rachunku nie widać),
     15h (film i tekst tłumaczą to samo w tym samym miejscu), zasada 26 rozszerzona o zgodność
     treści, nie tylko liczby linijek,
   - COLORS.md: tabelka dwóch szarości filmowych (#666666 założenie, #888888 dopisek) razem
     z tym, co z nich wychodzi w ciemnym motywie,
   - skill projektowanie-rozwiazan: nowy punkt 2b w references/zasady-wizualne.md („krok może
     wyjaśniać, byle kończył się prostą linijką") plus doprecyzowanie, że zakaz wyszarzania
     dotyczy poprzedniej linijki, a nie warunku trzymanego przez cały film.

Zmierzone po zmianie: styki klatek SSIM 0,99970 do 0,99991, zieleń bez zastrzeżeń,
test-krokow.js na dwóch ziarnach bez zastrzeżeń, telefon 390 px bez przewijania w bok
(298 na 298) i bez łamania wzoru w środku (jeden komentarz trzeba było w tym celu rozbić
na trzy krótkie wzory zamiast jednego długiego ciągu równości).

[ZROBIONE 2026-08-27] (Opus 5, medium) Film krok po kroku do zad. 8 z 2024-grudnia napisany
od nowa: koniec z automatycznym morfem całej strony równania, ruch wskazany co do glifu.
[2024-grudzien, zad8, manim, animacja, krok-po-kroku]

Punkt z TODO brzmiał „rozwiązanie zwykłe napisane od nowa, ale FILM zostal stary i się z nim
nie zgadza". Rozwiązanie opisowe i liczba kroków zgadzały się już rano, więc zostało samo
przepisanie animacji, po trzech uwagach Henricha: morf zasłania to, co się dzieje; krok może
zawierać wyjaśnienie i dopiero kończyć się prostą linijką; założenie ma być mniej kontrastowe.

Co zrobione:
- każdy z dziesięciu kroków ma ruch wskazany ręcznie, glif po glifie (zero
  `TransformMatchingTex`), a mapa glifów jest policzona z renderu `index_labels`
  i spisana w komentarzu sceny,
- pięć kroków (2, 3, 6, 7, 10) liczy w środku rachunek pomocniczy i dopiero potem zostawia
  czystą linijkę; krok 2 wyprowadza założenie z obu mianowników po kolei,
- założenie `x \ne 1` jest szare `#666666`, dopiski działań `#888888`,
- czynnik z dopisku najpierw staje NAD miejscem, w które wejdzie, a składnik przenoszony
  na drugą stronę leci łukiem nad znakiem równości: po prostej oba przechodziły po literach,
- opisy pod krokami przepisane, bo film pokazuje teraz to, co wcześniej niósł sam tekst.

Sprawdzone: styki klatek SSIM 0,99978 do 0,99993, `tools/zielen-krokow.py` bez zastrzeżeń,
`tools/test-krokow.js --zadania=7` na dwóch ziarnach bez zastrzeżeń, klatki obejrzane okiem
w każdym kroku. Szczegóły: `manimations/zad8-kroki.md` i `issues/spec-zad8-2024-grudzien.md`.

[ZROBIONE 2026-08-25] (Opus 5, high) Zamknięte dwa punkty hostowe z TODO.md: rebuild
kontenera z dokumentacją LaTeX-a i przegląd firewalla pod dokumentację dla modeli.
[kontener, latex, firewall, todo, dokumentacja]

Rebuild Container został zrobiony przez Henricha, sprawdzone w kontenerze:
`texdoc -l amsmath` wypisuje trzy PDF-y (`amsldoc.pdf`, `amsmath.pdf`, `subeqn.pdf`)
z `/usr/share/texlive/texmf-dist/doc/latex/amsmath/`, więc nazwy pakietów
`texlive-latex-base-doc` i `texlive-latex-recommended-doc` były trafione
(wcześniej były tylko przypuszczeniem, patrz wpis wyżej z tego samego dnia).

Wpis o firewallu usunięty z TODO.md, bo był wynikiem przeglądu („nic nie trzeba
otwierać"), a nie zadaniem do wykonania, i nic się przez to nie gubi:
uzasadnienia dla `docs.manim.community` i `katex.org` leżą w
`issues/dokumentacja-dla-modeli.md`, a `pypi.org` + `files.pythonhosted.org`
siedzą w `.devcontainer/init-firewall.sh` jako gotowy, zakomentowany kandydat
z opisem, kiedy je odkomentować (linie 159-163).

Przy okazji przegląd stanu kontenera (nic nie zmieniane w repo): Manim renderuje
scenę z MathTex, Playwright/Chromium otwiera arkusz (42 karty, 481 wzorów KaTeX),
`tools/serwer.js` oddaje 206 na żądanie zakresu, `statystyki.py`
i `sprawdz-cloudflare.py` przechodzą, firewall przepuszcza listę dozwolonych
i blokuje resztę.


[ZROBIONE 2026-08-25] (Opus 5, medium) Dokumentacja LaTeX-a dla modeli dopisana
do obrazu devkontenera (praca z hosta, bo zmiana jest w Dockerfile).
[dockerfile, kontener, latex, manim, dokumentacja, host]

Zamknięcie opcjonalnego punktu hostowego z TODO. `texdoc` był w obrazie, ale nie miał
czego pokazywać (`texdoc -l amsmath` zwracało „nie znaleziono"), bo TeX Live jest tam
okrojony do plików roboczych. Model pytany o składnię MathTex nie miał więc gdzie
zajrzeć i pisał z pamięci.

Do bloku `apt-get` w `.devcontainer/Dockerfile` dopisane `texlive-latex-base-doc`
i `texlive-latex-recommended-doc`, czyli dokumentacja dokładnie tych kawałków,
w których siedzą polecenia używane w scenach. Świadomie bez `texlive-latex-extra-doc`
i `texlive-fonts-extra-doc` (setki megabajtów opisów pakietów, których sceny nie
tykają); nazwy tych dwóch leżą w komentarzu nad blokiem jako kandydaci na później.

Czego NIE ustalono: nazw obu pakietów nie zweryfikowano w repozytorium Debiana,
bo host stoi na Fedorze, a sprawdzenie w sieci wymagałoby zgody (HOSTRULES.md).
To nazwy siostrzane wobec już zainstalowanych, czyli przypuszczenie, nie pomiar;
zły wpis wywali rebuild z komunikatem „Unable to locate package". Rozmiaru dodatku
też nie mierzono. Szczegóły w `issues/dokumentacja-dla-modeli.md`.

Działa dopiero po „Rebuild Container" - wpis dla Henricha jest w TODO.md.


[ZROBIONE 2026-08-25] (Opus 5, medium) Poprawiony komentarz przy pypi.org
w `.devcontainer/init-firewall.sh` (praca z hosta, plik jest w kontenerze tylko do odczytu).
[firewall, kontener, manim, host, dokumentacja]

Przy zakomentowanych wpisach `pypi.org` / `files.pythonhosted.org` stało „Odkomentuj,
gdyby Manim albo inne narzędzia pythonowe miały renderować wideo w kontenerze". To tekst
sprzed wrzucenia Manima do obrazu (2026-08-11): dziś paczki pythonowe wchodzą przy
budowaniu obrazu, zanim firewall się nałoży, więc do samego renderu wideo ten wyjątek
nie jest potrzebny i komentarz mylił. Nowa treść mówi, że wyjątek przydaje się wyłącznie
przy doinstalowaniu paczki w DZIAŁAJĄCYM kontenerze, bez przebudowy obrazu, i że
potrzebne są oba wpisy naraz (metadane + pliki). Sam wpis zostaje zakomentowany,
firewall bez zmian. Sprawdzone `bash -n`.


[ZROBIONE 2026-08-25] (Opus 5, medium) Dokumentacja dla modeli: rozpoznawanie środowiska,
luka w liście stabilnych ID, przegląd tego, czego modelom brakuje offline.
[dokumentacja, kontener, podman, host, firewall, manim, katex, id, exam-mode]

Wyszło z sesji, w której model przez pół rozmowy twierdził, że jest na hoście, siedząc
w devkontenerze.

1. **Rozpoznanie host/kontener naprawione.** Model sprawdzał `/.dockerenv`, a ten plik
   tworzy wyłącznie docker; kontenery stoją na rootless podmanie, więc test zawsze
   wychodził „host". Nowy test bierze cztery markery naraz (`$REMOTE_CONTAINERS`,
   `$DEVCONTAINER`, `$container`, `/run/.containerenv`, `/.dockerenv`) i jest sprawdzony
   w obie strony. Trafił do CLAUDE.md, szczegóły w `issues/host-czy-kontener.md`.
   Przy okazji: system hosta da się rozpoznać ze środka kontenera po `uname -r`
   (jądro jest wspólne, `fc` = Bazzite), bo `/etc/os-release` opisuje obraz kontenera.
   Tabelka markerów per maszyna w `MACHINES.md`, kolumna Kubuntu czeka na pomiar.

2. **`issues/dokumentacja-exam-mode-luka.md` zamknięte.** Cztery braki wypunktowane
   w zgłoszeniu (`#egzamin-koniec-bar`, `#egzamin-start-stopka`, `KLUCZ_OCENIANIA`,
   faza „oceń się") były już uzupełnione w ARCHITECTURE.md; zgłoszenie było nieaktualne.
   Natomiast **lista stabilnych ID w ARCHITECTURE_CSS.md faktycznie miała luki** i to
   większe, niż zgłoszenie opisywało. Porównanie skryptem (ID z template.html kontra
   użycia w `app/*.js`) pokazało 19 identyfikatorów odpytywanych z kodu, a nieobecnych
   na liście: cała stopka arkusza, overlay podsumowania egzaminu, `#exercises-wrapper`,
   `#exercise-template` i dziewięć pól formularza zgłaszania błędów. Dodane w czterech
   grupach. Poprawiona też sama zapowiedź listy: dwa wpisy (`#wersja`,
   `#tryb-przelacznik`) NIE są odpytywane z JS i są stabilne z innych powodów, co
   wcześniej lista przemilczała. Po poprawce skrypt daje zero luk.
   Uwaga metodyczna: pierwsze porównanie dało sześć fałszywych trafień, bo część ID
   kod pobiera pętlą po tablicy stringów, nie literalnym `getElementById("…")`.

3. **Przegląd „czego modelom brakuje offline"** (`issues/dokumentacja-dla-modeli.md`).
   Wniosek: firewalla nie trzeba otwierać na nic. Pełne źródła Manima 0.18.1 leżą
   w kontenerze i czyta się je przez `inspect` (przepis dopisany do
   `manimations/README.md`), a listę poleceń KaTeX da się wyłuskać wprost
   z `vendor/katex/katex.min.js` (1011 nazw, z jednym zmierzonym fałszywym trafieniem
   na pięć kontrolnych). `docs.manim.community` stoi na współdzielonym adresie
   Cloudflare (104.16.254.120), czyli tym samym przypadku co odrzucony formspree.io.
   Wykryta pułapka: `texdoc` jest zainstalowany, ale nie ma czego pokazywać.

4. **Sprawdzone renderem, co Manim w tym obrazie faktycznie umie** (pytanie Henricha
   o maturalne typy rysunków). Siedem scen kontrolnych przeszło i każda została
   obejrzana klatka po klatce, nie tylko „render nie zwrócił błędu": liczby zmieniane
   płynnie przez `ValueTracker`, układ współrzędnych z wykresami i polem pod krzywą,
   bryły 3D z obrotem kamery, geometria płaska z kątami i klamrami, diagram słupkowy
   i tabela, trudniejszy LaTeX. Sceny wylądowały jako `manimations/test-mozliwosci.py`,
   do puszczenia po każdej zmianie `MANIM_VERSION`.
   **Jedna rzecz NIE działa:** polskie znaki w `Tex()`/`MathTex()` wywalają render
   (`Command \k unavailable in encoding OT1`, czyli ogonek od „ą"); napisy z polskimi
   znakami idą przez `Text()` (Pango). Dopisane do „Pułapek Manima" w README.
   Ślad, że ktoś się już na tym przejechał: zakomentowany `MathTex` z „liczbą
   całkowitą" w `solutionZad3.py`.


[ZROBIONE 2026-08-24] (Opus 5, medium) Trzy punkty z sekcji „DO ZROBIENIA HOŚCIE":
poprawki, których nie dało się zrobić z kontenera, plus przegląd repo pod kątem dwóch gałęzi.
[host, devcontainer, firewall, galezie, dev, main, cloudflare, hosting]

Robione na hoście, bo `.devcontainer/` jest w kontenerze tylko do odczytu.

1. `.devcontainer/README.md`: trzy wzmianki o `origin/master` (linie 202, 203, 204)
   zamienione na `origin/dev`. Chodzi o przepis na naprawę rozjazdu HEAD-a po nieudanym
   `pull`, więc wskazywanie na nieistniejącą gałąź czyniło ten przepis nie do wykonania.

2. `.devcontainer/init-firewall.sh`: `matematykazen.pl` odkomentowana i wpisana do
   CONTENT_DOMAINS, razem z `www.matematykazen.pl`. Usunięta stara adnotacja z sekcji
   „Czego tu ŚWIADOMIE NIE MA" (mówiła, że domeny nie ma w DNS).
   Zweryfikowane przed wpisaniem, dokładnie tą linią, której używa `add_domain`:
   `dig +noall +answer A matematykazen.pl | awk '$4 == "A" {print $5}'` → 172.67.172.150
   i 104.21.63.231, oba warianty adresu dają ten sam wynik. Format przechodzi regex
   skryptu, duplikat obsłuży `ipset add -exist`, więc wejścia do kontenera to nie wywali.
   `bash -n` na skrypcie czysty.
   ŚWIADOMY KOMPROMIS, opisany też w komentarzu przy wpisie: to anycast Cloudflare,
   adresy współdzielone z tysiącami cudzych stron, a filtrujemy po IP, nie po SNI.
   Dokładnie ten powód trzyma `formspree.io` wśród odrzuconych. Wpuszczone mimo to,
   bo inaczej z kontenera nie widać własnej produkcji.

3. Przegląd „czy wszystko gra z nowymi gałęziami". Zgodne i bez zmian: `README.md`,
   `OVERVIEW.md`, `CLAUDE.md`, `issues/cloudflare-hosting.md`, `issues/git-i-gitdoc.md`,
   `.vscode/tasks.json`, `wrangler.jsonc`, `.assetsignore`. Wystąpienia słowa „master"
   poza `done/` są już tylko historyczne, czyli opisują przeszłość i są prawdziwe.
   `python3 tools/sprawdz-cloudflare.py` cicho, 241 plików, 28,9 MB.
   ZNALEZIONA I NAPRAWIONA JEDNA USTERKA: `refs/remotes/origin/HEAD` w klonie wskazywał
   na skasowany `origin/master` („dangling symref"), więc `git rev-parse origin/HEAD`
   kończył się `fatal: Needed a single revision`. Naprawione za zgodą Henricha przez
   `git remote set-head origin -a`, teraz wskazuje na `origin/main` (czyli GitHub ma
   `main` jako gałąź domyślną).
   POTWIERDZONE NA ŻYWO, że podział gałęzi działa: `matematykazen.pl` i `www.matematykazen.pl`
   serwują v81 (stan `main`), a `henrich2137.github.io/matematykazen/` v83 (stan `dev`).
   `git merge-base --is-ancestor main dev` przechodzi, więc awans `--ff-only` jest gotowy;
   `main` czeka na siedem commitów z `dev`.

Numeru wersji nie podbijałem: żadna z tych zmian nie dotyka strony w przeglądarce.

[ZROBIONE 2026-08-23] (Opus 5, medium) Porządki w dokumentacji: trzy pliki z issues/
rozebrane na części i skasowane, treść trafiła tam, gdzie się jej szuka.
[dokumentacja, issues, porzadki, krok-po-kroku, playwright, manim]

Powód: te same rzeczy leżały w dwóch miejscach naraz, a część zdążyła się zdezaktualizować.

- `issues/krok-po-kroku-produkcja.md` (198 linii) → rozdzielony. Produkcja filmu (parametry
  renderu 1280x720/120 fps z uzasadnieniem, pełny przepis na rewersy z `tpad` i `-an`,
  decyzja o `manimations/` na wierzchu repo) poszła do `manimations/README.md`. Odtwarzacz
  na stronie (serwer bez obsługi Range, gubienie klatek przy 4x, jak weryfikować wideo,
  żeby zrzut ekranu nie skłamał) poszedł do nowego `issues/rozwiazanie-krok-po-kroku-odtwarzacz.md`.
  Wyrzucone jako martwe: tabelka numerów linii do ręcznego cięcia sceny (zastąpił ją
  `tools/wgraj-kroki.sh`) i plan paska postępu między kropkami (zrobiony w v27).
  Przy okazji poprawione: `manimations/README.md` twierdził, że `manim.cfg` daje
  840x360 @ 60 fps, a daje 1280x720 @ 120 od 2026-08-11.
- `issues/lekcje-z-sesji.md` (112 linii, jeden wpis) → cztery reguły o odróżnianiu
  zmierzonego od prawdopodobnego przeniesione do `CLAUDE.md` jako sekcja „Przypuszczenie
  to nie ustalenie". Pomiary host↔kontener, których wpis dotyczył, i tak już siedziały
  w `manimations/README.md`.
- `issues/fable-brief-2026-maj.md` (219 linii) → brief jednorazowego pilotażu, w większości
  nieaktualny (v40, „arkusz prawie pusty", ścieżka `widgets/_registry.js`). Uratowane trzy
  rzeczy: pułapki pisania skryptów Playwrighta pod tę stronę → `issues/playwright-podglad.md`;
  kroki typu `"text"` nie działają (renderer zna tylko `video` i `image`) → poprawka
  nieprawdziwego zdania w `ARCHITECTURE.md`; brak pola z numerem zadania w danych →
  nowy punkt w schemacie w `ARCHITECTURE.md`. Zasady widżetów i kolorów były już
  w `widgets/PROJEKTOWANIE.md` i `COLORS.md`.

Odnośniki przepięte wszędzie, gdzie żyją: `CLAUDE.md`, `ARCHITECTURE.md`,
`manimations/README.md`, `issues/README.md`, `issues/krok-po-kroku-v20-testy.md`,
`issues/fable-przekazanie-2026-maj.md`, a także w kodzie: `app/state.js` i `tools/rewersy.sh`.
Wzmianki w starych wpisach `done/` zostały nietknięte, bo są zapisem tego, co było wtedy.
Sprawdzone skryptem: żaden odnośnik `.md` w plikach poza `done/` nie prowadzi w pustkę.

[ZROBIONE 2026-08-23] (Opus 5, medium) Zasady opisu kroków i układu rozwiązania zwykłego
doprecyzowane na zad. 2 z 2024-grudnia; nieaktualny wpis z TODO.md usunięty.
[zasady, opisy-krokow, solutionText, rozw-2kol, zad2, 2024-grudzien]

Wpis w TODO.md („podpisy pod krokami jedno pod drugim, wywal czyli" oraz „rozwiązanie zwykłe
jedno pod drugim zamiast dwóch kolumn") pochodził sprzed przerobienia zadania 2 i mówił coś
innego, niż Henrich chce dzisiaj. Obowiązujące zasady:

- opis kroku to wzór plus wyjaśnienie słowne; obliczeń widocznych w kadrze się nie przepisuje;
- dwie kolumny w rozwiązaniu zwykłym są układem chcianym, gdy wzorów jest kilka, a rachunek
  jest szeroki. Nie spłaszcza się ich do jednej kolumny.

Samo zadanie 2 spełnia obie zasady od v67, więc exercises.json i scena zostały bez zmian.
Otwarta zostaje jedna poprawka, wpisana przez Henricha do TODO.md: w kroku 3 filmu jedynka
przejeżdża dziś z licznika ułamka do wykładnika, a to dla ucznia dwa niepowiązane miejsca.
Ma to iść dwiema animacjami (najpierw zielona jedynka pojawia się jako wykładnik piątki
w mianowniku, potem ta sama jedynka jedzie na nowy wykładnik, a w tym czasie znika „1/"
i pojawia się minus).
Zapisane w: manimations/README.md (sekcja „Jak pisać opisy kroków", nowy punkt na górze
listy) i SOLUTION_TEXT_RULES.md (sekcja „Który układ wybrać", punkt o dwóch kolumnach).

[ZROBIONE 2026-08-22] (Opus 5, medium) Repo przygotowane pod hosting Cloudflare.
[cloudflare, hosting, wrangler, wdrozenie]

Cztery pliki w korzeniu: `wrangler.jsonc` (ustawienia wdrożenia), `.assetsignore` (czego
nie wysyłać), `_headers` (nagłówki HTTP), `404.html` (własna strona błędu, działa też na
GitHub Pages). Do tego test `tools/sprawdz-cloudflare.py`: pilnuje limitu 25 MiB na plik
i tego, żeby `.assetsignore` nie wyciął czegoś, bez czego strona się sypie.

Pierwsze wdrożenie padło, bo automat wysyłał na hosting katalog `.git`. Po poprawce
przechodzi, sprawdzone prawdziwym wranglerem. Mechanika, czyli dlaczego Worker zamiast
Pages i czego odsiewać nie wolno: `issues/cloudflare-hosting.md`.

Zostaje jako otwarte, w TODO.md w „INNE NOTATKI": dwa adresy z tą samą treścią (Pages
i domena) są dla wyszukiwarek duplikatem, więc kiedyś trzeba wskazać główny.

[ZROBIONE 2026-08-22] (Opus 5, medium) Domena matematykazen.pl działa na Cloudflare,
a repo dostało dwie gałęzie: dev (GitHub Pages) i main (domena).
[cloudflare, hosting, domena, git, galezie, dev, main]

Domena kupiona u rejestratora hitme, przepięta na serwery nazw Cloudflare i podpięta do
Workera; HTTPS wystawił Cloudflare sam. Działa i `matematykazen.pl`, i `www.matematykazen.pl`.
Zamyka to trzy kliknięcia z sekcji „DLA HENRICHA" w TODO.md (serwery nazw, custom domain,
podanie nazwy domeny) oraz punkt 2.3 ścieżki biznesowej.

Gałęzie ułożone tak, że każdy hosting jedzie z innej:

- `dev` → GitHub Pages, codzienna praca, tu idą wszystkie commity i pushe.
- `main` (przemianowany dawny `master`) → Cloudflare i domena, wersja oficjalna.
- `origin/master` już nie istnieje; `origin/master-old` zostaje jako archiwum.

Lokalny klon miał tylko `master` wskazujący na skasowaną gałąź zdalną, więc odtworzone od
zera: `dev` i `main` śledzą swoje odpowiedniki, stary `master` usunięty. Na `main` ustawione
`branch.main.mergeOptions = --ff-only`, żeby awans z `dev` nie mógł po cichu zrobić commitu
scalającego: pod domeną ma stać dokładnie ten ciąg commitów, który wcześniej był przetestowany
na Pages.

Zasada od Henricha, spisana w CLAUDE.md: **„push" bez dopowiedzenia zawsze znaczy `dev`**.
Na `main` idzie tylko to, o czym powie wprost, że ma być widoczne publicznie dla użytkowników.
Praktyczny skutek: numer wersji w rogu strony mówi też, którą z dwóch witryn się właśnie
ogląda, bo `main` bywa kilka commitów za `dev`.

Udokumentowane w: CLAUDE.md (sekcja Git przepisana, sekcja Hosting z tabelką adresów),
issues/cloudflare-hosting.md (stan domeny, kto jedzie z której gałęzi, pułapka z curlem),
issues/git-i-gitdoc.md (nowa sekcja o gałęziach + przepis na odtworzenie układu w świeżym
klonie), OVERVIEW.md (adres na żywo, „Dwa adresy strony", faza 2.3 na DONE).

Pułapka do zapamiętania: **z devcontainera nie sprawdzisz, czy domena żyje**. `curl` na
`matematykazen.pl` kończy się przeterminowaniem, bo firewall kontenera przepuszcza tylko
wybrane adresy, a to wygląda jak padnięta strona. Sprawdzać z przeglądarki poza kontenerem.

Do dokończenia z hosta: `.devcontainer/README.md` w dwóch miejscach mówi jeszcze o
`origin/master` (katalog jest w kontenerze tylko do odczytu). Wpisane do TODO.md.


[ZROBIONE 2026-08-20] (Opus 5, medium) Devcontainer sprawdzony na Kubuntu
pod rootless podmanem. Punkt „DO ZROBIENIA HOŚCIE" zamknięty, sekcja pusta.
[devcontainer, podman, kubuntu, firewall]

Wpis w TODO mówił, że kontener testowano wyłącznie pod rootless podmanem na Bazzite,
i kazał sprawdzić go na Kubuntu z Dockerem. Henrich doprecyzował 2026-08-20, że na
Kubuntu też pracuje **tylko na podmanie**, więc Docker wypada z zakresu i nie ma
po co go badać, dopóki nikt na nim nie pracuje.

Zostało pytanie, czy pod Kubuntu wszystko działa tak jak na Bazzite. **Działa** -
sprawdzone od środka działającej sesji, bez ruszania hosta:

- Host to Ubuntu: jądro `7.0.0-30-generic #30-Ubuntu`, zbudowane przez buildd,
  gcc `Ubuntu 15.2.0`. Bazzite jest na Fedorze, więc to inna maszyna niż referencyjna.
- Runtime to podman, nie Docker: jest `/run/.containerenv`, nie ma `/.dockerenv`,
  a DNS wskazuje `169.254.1.1`, czyli pastę (pod Dockerem byłoby `127.0.0.11`).
- Firewall działa w obie strony: `github.com` i `api.github.com` zwracają 200,
  a `pypi.org` i `example.com` nie łączą się w ogóle (kod 000, curl pada).
- Git i gh działają: `git ls-remote origin` przechodzi, `gh auth status` pokazuje
  zalogowanego `Henrich2137` z konfiguracją w `/home/node/.config/gh/hosts.yml`
  (czyli wolumen z konfiguracją gh też się podpiął).
- Montowania read-only trzymają: `touch .devcontainer/…` i `touch .vscode/…`
  kończą się „Read-only file system".
- Narzędzia z obrazu wstają: Manim Community 0.18.1, Node 20.20.2, Python 3.11.2
  oraz Chromium Playwrighta (bind z cache'a hosta).

**Uwaga na przyszłość:** tego nie dało się dopisać do `.devcontainer/README.md`,
bo ten katalog jest w kontenerze read-only i edytuje się go z hosta. Gdyby ktoś
chciał mieć to przy konfiguracji, a nie w dzienniku, trzeba przenieść ten wpis
z hosta.

[ZROBIONE 2026-08-20] (Opus 5, medium) v63 - Henrich przeklikał CAŁĄ sekcję
TESTOWANIE HENRICH (paczki v33-v62). Wszystko działa; sekcja wyczyszczona do zera.
[testowanie, henrich-potwierdził, ciemny-motyw, zad20, landing]

Odpowiedzi Henricha, punkt po punkcie:

- Ciemny motyw: zielone piątki w filmie zad. 2 są zielone, wykres zad. 10 fioletowy,
  rysunki CKE bez czarnej ramki, przemalowanie przy otwartym widżecie działa. ✅
- Zad. 8, 10, 12 i 13 maja: barwy w WIDŻETACH się zgadzają. Filmów do maja jeszcze nie ma,
  więc porównanie z filmem przeniesione do sekcji „Treść w 2026-maj" jako warunek
  do sprawdzenia PRZED renderem (tools/odwroc-kolor.py).
- Skrajne położenia i blokady: wszystkie siedem punktów działa (12.2 domykanie przedziału,
  trójkącik w zad. 14, blokada D na dolnym łuku, B przy A, k do 16 i l do 12, piłeczka
  przy zerze, blokada przycisku w locie).
- Odczyty: ułamki zwykłe zamiast dziesiętnych działają, czas lotu piłki się zgadza.
- Kreska pod blokiem rozwiązania: Henrich nie widzi problemu, kreska po całym zadaniu jest
  i ma być. Nic do zmiany.
- Telefon i słabe łącze: cztery punkty, wszystkie działają.

Jedyna poprawka, jaka z tego wyszła, i dwie rzeczy przy okazji:

- **Zad. 20 maja, ciemniejsze odcienie odcinków** („można jednak troszeczkę przyciemnić
  ciemniejsze"). NIE przyciemniono `--wg-niewiadoma` ani `--wg-zolty`, bo ten błękit jest
  związany z barwą „podstawiam pod x" w filmach (base.css mówi o tym wprost) i używa go
  każdy widżet. Zamiast tego dwa NOWE tokeny, na razie wyłącznie dla zad. 20:
  `--wg-niewiadoma-ciemna` (#005d8e jasny / #2f86b4 ciemny) i `--wg-zolty-ciemny`
  (#a17900 / #c69a34), plus wpisy w `WG_KOLORY` i mapie zmiennych w `app/widget-helpers.js`.
  `widgets/proporcjeProste.js` bierze je dla odcinków OA i OC. Sprawdzone zrzutem
  w obu motywach: obie pary nadal rozróżnialne, kontrast w parze większy.
- Poprawiona literówka w komentarzu `style/landing.css`: „Stała szerokość 5z0 px" na 480 px,
  i dwie wzmianki o 520 px (landing.css oraz komentarz w index.html) na 480, bo Henrich
  sam zmienił szerokość przycisków. Zmiany szerokości nie ruszano.
- Zostawiona bez zmian twarda spacja, którą Henrich wstawił w „grudzień 2024" w index.html:
  renderuje się identycznie, a trzyma datę w jednym kawałku przy zawijaniu.

Do decyzji, które Henrich zamknął sam: napisy na przyciskach arkuszy zostają jego wersją,
a nagłówki „DAWNE POKAŻ WIĘCEJ" w ośmiu zadaniach grudnia już scalił (w exercises.json
nie ma po nich śladu).

[ZROBIONE 2026-08-20] (Opus 5, medium) Przegląd sekcji „Zweryfikować poprawność
matematyczną 2024-grudzien": zamknięte dwa punkty, reszta zmierzona i uściślona.
[weryfikacja, krok-po-kroku, styk-klatek, todo]

- **Zad. 2, merytoryka kroków 1 i 6 (wykładnik -1, potem 5, wynik \(5^4\)) - ZGADZA SIĘ.**
  Sprawdzone wprost w `manimations/solutionZad2.py`, gdzie stoi cały łańcuch:
  \((\sqrt[5]{5}\cdot\frac15)^{-5} = (5^{1/5}\cdot 5^{-1})^{-5} = 5^{1/5\cdot(-5)}\cdot 5^{(-1)(-5)}
  = 5^{-1}\cdot 5^{5} = 5^{4}\). Punkt skreślony z TODO.
- **Marginesy podpisu pod filmem - punkt odpadł sam** i sam wpis to zresztą mówił
  (od v20 nie ma podpisu, opis kroku siedzi w rozwijanym ROW 3; zmierzone 24 px kontra
  25 px na telefonie 390 px). Skreślony.
- **Zad. 9, pierwszy checkbox „Sprawdzania obliczeń" - nie ma czego naprawiać po stronie
  punktacji.** `gradingCriteria` w grudniu ma 0 + 1 + 1 pkt i to zgadza się z kluczem CKE
  (`odpowiedzi.txt`): punkt leci dopiero za pierwiastki, a przepisanie nierówności do postaci
  \(x^2-6x-7\le 0\) samo w sobie nie punktuje. Wpis nie mówił, co konkretnie jest nie tak,
  więc został w TODO z dopiskiem, żeby Henrich dopowiedział.
- **Styki klatek przemierzone w całym arkuszu** (`tools/styk-klatek.sh`, wszystkie 62 kroki).
  Stary opis w TODO był nieaktualny: mówił „zad. 3, 5 i 6 poprawione w v30" i kazał dopiero
  przejrzeć zad. 2, 7, 8 i 9. Teraz stoi tam gotowa lista dokładnie sześciu par poniżej progu:
  zad. 2 (2→3, 0,9861), zad. 8 (1→2 i 2→3), zad. 7 (5→6), zad. 9 (7→8), zad. 4 (2→3),
  zad. 3 (6→7). Zad. 1, 5 i 6 są czyste w całości.
- Przy okazji uściślony punkt o zad. 3: rozjaśnianie działa już w krokach 2 i 4, zostaje sam
  krok 6. Wcześniej wpis wymieniał wszystkie trzy.

[ZROBIONE 2026-08-20] (Opus 5, medium) v62 - wycięte postoje na wejściu w filmach
krok po kroku (zad. 1 krok 9, zad. 2 krok 6, zad. 3 krok 5).
POTWIERDZONE PRZEZ HENRICHA (2026-08-20): „wygląda dobrze".
[manim, krok-po-kroku, wait, tempo]

- Zgłoszenie Henricha: „kroki mają za długie czekania na początku i na końcu filmu,
  małe waity w środku kroku są okej, najmocniej widać w zad. 1".
- Zmierzone skryptem doraźnym (dekodowanie do rgb24, porównanie każdej klatki
  z pierwszą i z ostatnią): ile w każdym pliku stoi nieruchomy obraz. Wynik dla
  wszystkich 62 kroków grudnia jest w opisie commita; martwy start powyżej 1 s
  wypadł w dziewięciu krokach.
- Ustalenia z Henrichem przed pracą (pytania zadane na starcie):
  - ciąć wyłącznie na początkach i końcach kroków, NIE w środku,
  - animacji kolorów (zapalanie i gaszenie podświetleń) nie ruszać,
  - przytrzymanie na końcu zostaje 0,25 s (dolna granica 0,1 s, ale 0,25 jest
    zweryfikowane, patrz manimations/README.md punkt 0).
- Przy tych warunkach do cięcia kwalifikują się DOKŁADNIE trzy miejsca, czyli
  wszystkie `self.wait()` stojące w sekcji przed pierwszym `self.play()`:
  `solutionZad1.py` krok 9, `solutionZad2.py` krok 6, `solutionZad3.py` krok 5.
  Znalezione parserem sekcji, nie okiem.
- W zad. 2 ten postój był opatrzony komentarzem, że jest CELOWY (żeby uczeń
  zobaczył punkt wyjścia). Wycięty mimo to, bo punkt wyjścia stoi już na ostatniej
  klatce kroku 5, a w odtwarzaczu to jest to samo miejsce.
- Reszta martwych startów w zad. 1 (kroki 4, 5, 7, 8: od 1,25 do 2,36 s) to NIE są
  `wait()`, tylko sekundowe animacje `ReplacementTransform`/`FadeTransform`,
  które zmieniają wyłącznie kolor dwóch glifów, oraz `wait(1)` w środku kroku.
  Zostały nietknięte zgodnie z decyzją Henricha; jeśli kiedyś mają zniknąć, to jest
  osobna zmiana (skrócenie run_time kolorowania).
- Efekt: martwy start 1,08 → 0,08 s (zad. 1 krok 9), 1,18 → 0,17 s (zad. 2 krok 6),
  1,27 → 0,27 s (zad. 3 krok 5). Każdy z trzech plików o 1,00 s krótszy.
- Sprawdzone: `tools/styk-klatek.sh` (styki bez pogorszenia), `tools/test-krokow.js`
  na serwerze szybkim i zdławionym (30 przebiegów, bez zastrzeżeń).
- Uwaga na przyszłość: `tools/styk-klatek.sh` zgłasza dwa styki poniżej progu,
  zad. 2 kroki 2→3 (SSIM 0,9861) i zad. 3 kroki 6→7 (0,9990). To defekty SPRZED
  tej zmiany - sprawdzone przez uruchomienie skryptu na plikach wyciągniętych
  z HEAD, wartości co do cyfry te same. Osobny punkt, nie regresja.
- Render w kontenerze jest powtarzalny co do bajtu: po przerenderowaniu trzech
  scen `git status` pokazał zmienione tylko te trzy kroki (plus rewersy), reszta
  z 23 plików wyszła identyczna.

[ZROBIONE 2026-08-20] (Opus 5, medium) v61 - przyciski arkuszy na stronie głównej:
stała szerokość, nowe napisy, koniec pustych akapitów rozdzielających.
[landing, cta, responsive]

- `.landing-cta-sub` usunięty. Były to dwa PUSTE akapity, których jedynym zadaniem
  było rozepchnięcie przycisków (inline-block same stanęłyby obok siebie). Odstęp
  robi teraz `margin: 0 auto 16px` na samym przycisku.
- `.landing-cta` z inline-block na block o stałej szerokości 520 px (`max-width: 100%`
  zwęża go sam na wąskim ekranie). Powód: arkusze to równorzędny wybór, więc mają
  wyglądać jak dwa jednakowe klawisze, a nie dwa napisy różnej długości.
  `box-sizing: border-box` jest tu konieczne, bo arkusz stylów nie ma globalnego
  resetu i bez tego padding z ramką doszłyby do 520 px.
- W responsive.css (breakpoint 720 px) ciaśniejszy padding 13/16 i 17 px czcionki:
  przy desktopowym paddingu 28 px na bok dłuższy napis łamał się na telefonie
  na trzy linijki.
- Napisy zmienione z „Matura podstawowa, CKE, maj 2026" na „Rozwiąż arkusz CKE,
  maj 2026" (i analogicznie „arkusz próbny", grudzień 2024). Powód: „Matura
  podstawowa, CKE" powtarzało się w obu przyciskach, a mówi to już tytuł strony
  i lede; zostaje czasownik plus to, co student faktycznie porównuje.
  Propozycja modelu, nie polecenie Henricha - do zatwierdzenia (TODO, TESTOWANIE).
- Zmierzone Playwrightem: 520 px na desktopie, 445 px w oknie 485 px (telefon
  Henricha, napis w jednej linijce), 320 px przy 360 px szerokości (napis łamie
  się po przecinku, strona nie przewija się w poziomie).

[ZROBIONE 2026-08-20] (Sonnet 5 + Opus 5, medium) v60 - koniec z „pokaż więcej":
pole solutionTextMore usunięte z danych i z kodu, film zamienił się kolejnością z tekstem.
[solutionTextMore, kolejnosc-rozwiazan, render, sprzatanie]

- Dane. Treść `solutionTextMore` z dziesięciu zadań arkusza 2024-grudzień doklejona na koniec
  `solutionText` pod nagłówkiem `<br><br><b>DAWNE "POKAŻ WIĘCEJ":</b><br>` (tam, gdzie
  `solutionText` był pusty albo `null`, treść weszła wprost, bez nagłówka). Nagłówek jest
  celowo brzydki i tymczasowy: to znacznik dla Henricha, gdzie rozwiązanie trzeba jeszcze
  ręcznie zredagować w jedną całość. W 2026-maj pole było puste we wszystkich 41 zadaniach,
  więc tam sam klucz zniknął.
- Migracja szła po LINIACH, nie przez `json.load` + `json.dump`. Pierwsze podejście przez
  bibliotekę przeformatowało oba pliki od góry do dołu (inne wcięcia w `gradingCriteria`,
  1500+ zmienionych linii w każdym arkuszu) i diff nie dawał się przeczytać. Wersja liniowa
  ruszyła tylko te dwie linie na zadanie: 55 zmienionych linii zamiast 2064.
- Kod. Wycięty cały mechanizm: `.solution-text-more-container` z przyciskiem i span z
  template.html, obsługa kliknięcia i ustawianie treści w app/render.js, `hasMore`
  z tablicy `solutionBlocks`, reguły `.solution-text-more*` ze style/sheet.css i
  style/responsive.css.
- Kolejność bloków rozwiązania odwrócona na życzenie Henricha: teraz KROKI, potem TEKST,
  potem widżet. Kolejność siedzi w DWÓCH miejscach naraz i muszą się zgadzać - kolejność
  `<div>`ów w template.html (to ona decyduje o tym, co widać) i tablica `solutionBlocks`
  w `loadExercises` (ona tylko zdejmuje dolną kreskę z ostatniego widocznego bloku).
- Sprawdzone Playwrightem na obu arkuszach: 0 pozostałości po „pokaż więcej" w DOM,
  kolejność bloków identyczna w 76 zadaniach, kreska zdjęta z właściwego bloku,
  konsola czysta (jedyny błąd to zablokowany firewallem gc.zgo.at, jak zwykle).
- Dokumentacja zaktualizowana: ARCHITECTURE.md (schemat pola), ARCHITECTURE_CSS.md
  (kolejność bloków + `.light-button`), widgets/PROJEKTOWANIE.md, oba briefy dla Fable
  w issues/ (żeby nie wskrzesiła pola) i tablica-wzorow-transkrypt/README.md.

[ZROBIONE 2026-08-16] (Opus 5, xhigh) v57 - poprawki zad. 20, 26 i 33.2 po uwagach Henricha
plus wyrównanie formatowania rozwiązań do stylu Fable.
[2026-maj, widzety, kolory, formatowanie]

- Trzy nowe tokeny w palecie (`--wg-niewiadoma-jasna`, `--wg-zolty-jasny`, `--wg-wykres-jasny`)
  w obu motywach. Potrzebne tam, gdzie JEDNA prosta wyznacza DWA odcinki naraz.
  Fiolet jasny musiał być ciemniejszy, niż wynikałoby z nazwy (#8e57bb, nie #a97fd0): Chrome
  dobiera kolor toru suwaka kontrastowo do accent-color i przy jaśniejszym fiolecie malował
  tor na czarno, co wyglądało jak usterka.
- Zad. 20: skala 11 -> 14 px na jednostkę, płótno 380 -> 430 px, zakres przesuwania rozszerzony
  tak, że |OA| dochodzi do 16, a |OC| do 12 (życzenie Henricha). Kolor niosą już TYLKO cztery
  odcinki z wypisaną długością: OA i OD w dwóch odcieniach błękitu (prosta k), OC i OB w dwóch
  odcieniach żółci (prosta l). Same proste k, l, m, n oraz ich nazwy są neutralne, więc kawałki
  m i n poza pasem między równoległymi wychodzą szare same z siebie.
- Zad. 26: punkt (2, -2) zmieniony z pomarańczowego na neutralny (to gwóźdź, nie odpowiedź).
  Oba suwaki w barwach prostej k, którą sterują. Odczyt przebudowany wg szkicu Henricha:
  równanie prostej k pod suwakami w tych samych odcieniach, niżej zdanie „Prosta l przecina
  oś y-greków w punkcie:" i sam wynik na niebiesko.
- Zad. 33.2 (dopracowane w v58 po uwagach Henricha): pociskiem jest biało-czarna piłka nożna
  (białe koło, pięciokąt i trzy szwy), a nie kolejna kropka pomiarowa. Czerwona odpadła świadomie:
  czerwień w tym projekcie znaczy błąd (COLORS.md). Kolory piłki mają własne tokeny BEZ wariantu
  ciemnego, bo piłka nożna jest czarno-biała niezależnie od tła. Przycisk „Wystrzel piłeczkę"
  przeniesiony do ramki po lewej od suwaka (styl przycisków odpowiedzi: lekka ramka, zaokrąglone
  rogi), licznik czasu zszedł z płótna pod przycisk. Przycisk ma sztywne 52 px wysokości, bo napis
  przełącza się z dwuwierszowego na jednowierszowy i bez tego suwak obok skakał w pionie; miara
  musi być w pikselach, bo przy box-sizing: border-box wartość w em obejmuje padding i ramkę.
- Zad. 33.2: piłeczka czeka w (0, 0), przycisk „wystrzel piłeczkę" puszcza ją po torze w tempie
  RZECZYWISTYM (przy 14,7 lot trwa 3 s, zmierzone 3,04 s), przy piłeczce jedzie licznik „t = … s".
  W locie przycisk jest zablokowany, ruszenie suwaka sprowadza piłeczkę na ziemię, a przy zerowej
  wartości przycisk jest nieaktywny. Pułapka przy pisaniu: zegar trzeba wyzerować PRZED
  sprawdzeniem stanu przycisku, inaczej blokada nie zdąży się włączyć.
- Formatowanie sześciu moich rozwiązań (14, 19, 20, 26, 33.1, 33.2) wyrównane do Fable, w dwóch
  punktach wskazanych przez Henricha: krótkie wprowadzenie przed wzorem („Postać kanoniczna:"
  zamiast zdania z numerem strony) oraz jednostki poza wzorem (`\(t = 3\) s`, nie `\(t = 3\ \text{s}\)`).
  Puste linie między krokami ZOSTAJĄ - Henrich świadomie ich nie wybrał, bo sam o nie prosił po zad. 14.
- Weryfikacja (Playwright): zero błędów KaTeX i strony na desktopie i przy 485px w obu motywach,
  przeciąganie obu prostych w zad. 20, oba suwaki w zad. 26, pełny cykl lotu piłeczki wraz
  z przerwaniem go suwakiem.

[ZROBIONE 2026-08-16] (Opus 5, xhigh) v56 - zad. 20, 26, 33.1 i 33.2 (2026-maj) w komplecie.
[2026-maj, widzety, zadanie-20, zadanie-26, zadanie-33]

- Wszystkie policzone od zera i zgodne z kluczem: |OD| = 9 (B), (0, -4/3) (D), t = 3 s (D), t = 1,5 s (A).
- `widgets/proporcjeProste.js` (zad. 20). Proste m i n stoją, uczeń przesuwa k oraz l NIEZALEŻNIE,
  a punkty przecięcia jadą po m i n. Wszystkie cztery odcinki zmieniają długość, ale oba ilorazy
  zostają równe - i to jest cała odpowiedź na pytanie, skąd wolno ułożyć proporcję.
  Kąty prostych (60 st. i -48,19 st.) są dobrane tak, żeby przy pionowych k, l wyszły dokładnie
  długości 12, 8, 9 i 6; rysunek CKE nie jest w skali, więc odwzorowanie kąt w kąt nie miałoby sensu.
  Odczyt pokazuje JEDEN wspólny iloraz liczony z dokładnych położeń, a długości z dwoma miejscami
  po przecinku: przy jednym miejscu 11,2/10,6 wychodziło 1,06 przy wypisanym 1,05 i wyglądało to
  na sprzeczność.
- `widgets/prosteRownolegle.js` (zad. 26). Suwak a zmienia wynik, suwak b nie zmienia go wcale
  i o to chodzi: równoległość przenosi na l tylko współczynnik kierunkowy. Suwak a chodzi po
  wielokrotnościach 1/12, żeby -1/3 z zadania było osiągalne dokładnie, a odczyt pokazuje ułamki
  (-1/3, -4/3), nie 0,33.
- `widgets/rzutPileczki.js` (zad. 33.1 i 33.2, jeden widżet na obie części; rozwiązanie 33.1 odsyła
  do 33.2, zgodnie z decyzją Henricha). Suwak zmienia liczbę przy t, a moment szczytu i moment
  upadku jadą razem w stosunku 1 do 2. Wysokość płótna podana WPROST, nie przez wgWysokoscKwadratowa:
  osie mają różne wielkości (sekundy i metry), więc zrównanie pikseli na jednostkę dałoby płótno
  na 3600 px. Skala to 1 s w poziomie = 10 m w pionie, siatka rysowana ręcznie.
- formulasPage poprawione zgodnie z transkryptem tablic: zad. 20 -> s. 17 (cechy podobieństwa),
  zad. 26 -> s. 24 (proste równoległe), zad. 33.1 i 33.2 -> s. 8 (miejsca zerowe i wierzchołek).
- Weryfikacja (Playwright, `node tools/serwer.js 8001`), desktop i 485px x oba motywy: zero błędów
  KaTeX, zero błędów strony. Przeciąganie w zad. 20 (k i l osobno), oba suwaki w zad. 26 wraz
  ze sprawdzeniem, że b faktycznie NIE rusza wyniku, oraz skrajne wartości suwaka w zad. 33.2
  (29,4 -> szczyt 3 s i upadek 6 s; 0 -> komunikat zamiast wykresu; 14,7 -> 1,5 s i 3 s z ptaszkiem).

[ZROBIONE 2026-08-16] (Opus 5, xhigh) v52 - zad. 19 (2026-maj) w komplecie, rysunki z arkusza w pięciu
zadaniach, limit szerokości rysunków, poprawki zad. 14 po uwagach Henricha.
[2026-maj, widzety, rysunki, css, zadanie-19, zadanie-14]

- Zad. 19 (kąt wpisany i środkowy). Policzone od zera i zgodne z kluczem: kąt ADC jest wpisany na łuku
  AC, więc kąt środkowy AOC ma 2 * 50° = 100°; B leży między A i C, stąd AOB = 100° - 30° = 70°,
  odpowiedź C. Notacja kąta wzięta z tablic (`\sphericalangle`, s. 19).
- Nowy `widgets/katyWOkregu.js` (`widgetKatyWOkregu`), JEDNA karta (Henrich woli jedną):
  - D przeciągany po dłuższym łuku, kąt przy nim stoi na 50° niezależnie od położenia. To jest sedno
    zadania i widać je dopiero w ruchu.
  - B przeciągany po krótszym łuku AC, z dojazdem do samego A i do samego C (życzenie Henricha),
    kąt środkowy dzieli się inaczej, ale suma zostaje 100°.
  - D trzyma się 20° od A i od C. Przy mniejszym luzie jego podpis zlewał się z podpisem C, a cięciwa
    DC robiła się krótsza niż łuczek kąta przy D.
  - Odczyt to jedna linijka `50° * 2 = 100° = 70° + 30°` (v54, życzenie Henricha zamiast czterech
    osobnych wierszy), wszystkie liczby liczone z rysunku. Miary 70° i 30° siedzą po zewnętrznej
    stronie swoich łuków, tytuł skrócony do „Możesz przeciągać punkty B i D".
  - Miary kątów wypisywane na tle w kolorze płótna: bez tego liczby bywały przekreślone cięciwami DA
    i DC, których położenie zależy od tego, gdzie uczeń przeciągnie D (widoczne przy BOC = 80°).
- Rysunki z arkusza wycięte dla zad. 18, 19, 20, 21 i 31 (metoda ctypes/libgs z notatki sztafetowej
  Fable). Zadania 19, 20 i 31 miały w treści `<img>` wskazujący na nieistniejący plik, czyli na stronie
  był połamany obrazek; 18 i 21 nie miały rysunku wcale, choć arkusz go ma. Przy okazji treść zad. 19
  przepisana na notację KaTeX, a opisy `alt` z „TODO: dodać obraz" zmienione na opisy dla czytników
  ekranu. Pełny przegląd wszystkich 35 stron PDF potwierdził, że innych rysunków w tym arkuszu nie ma.
- Zad. 31 jest wyjątkiem od limitu (v55): jeden szeroki plik z dwoma diagramami przy 380px dawał po
  ~190px na wykres. Rozdzielony na `zad31rysA/B.png` w kontenerze `.rys-para` (flex z zawijaniem):
  na komputerze wykresy stoją obok siebie po 310px, na telefonie zawijają się jeden pod drugi i biorą
  całą szerokość karty (433px), czyli są dwa razy większe niż przed rozdzieleniem.
- `.question img` dostaje `max-width: min(100%, 380px)` (v52 miało 450px, Henrich uznał je za wciąż za duże). Rysunki wycinane z PDF-u mają po ~700px
  i ciągnęły się przez całą kartę na komputerze (uwaga Henricha do zad. 12 i 13). Pliki zostają
  w pełnej rozdzielczości, żeby były ostre na telefonie, gdzie i tak ogranicza je szerokość karty.
- Poprawki zad. 14 po testach Henricha: rozwiązanie opisowe rozbite na krótsze linijki z przerwami;
  strzałka przesunięcia przeniesiona POD wierzchołki i skrócona do samej liczby (kierunek widać po
  grocie); suwak rozwarcia rozszerzony z 0,2..1,3 na -2..2. Ujemne a wymagało trzech rzeczy naraz:
  nazwy krzywych schodzą pod wierzchołek (nad nim nie ma już ramion), miejsca zerowe g znikają, bo
  ich nie ma, a wartość g(0) ucieka poza kadr i zamiast kropki dostaje trójkącik przy krawędzi.
  Wartości tuż przy zerze są wycięte, bo przy a = 0 nie ma paraboli, tylko pozioma prosta.
- Weryfikacja (Playwright, `node tools/serwer.js 8001`):
  - zad. 19 na desktopie i telefonie x oba motywy: `.katex-error` = 0, zero błędów strony;
  - przeciąganie: D z 85° na 150° nie zmienia kąta przy D, próba wejścia D na łuk AC kończy się
    zatrzymaniem przed C, B z 280° na 230° daje BOC = 80° i AOB = 20°, a dociągnięty do A daje 0°;
  - rysunki: wszystkie 7 obrazków w arkuszu wczytuje się (naturalWidth > 0) i schodzi do 450px na
    komputerze oraz 433px na telefonie. Uwaga na przyszłość: `app/render.js` ustawia im `loading="lazy"`,
    więc test MUSI do nich przewinąć, inaczej mierzy niezaładowane obrazki i fałszywie alarmuje;
  - zad. 14 przy skrajnych wartościach suwaków (t = -3 i 3, a = -2, -0,05 i 2): odczyty zgodne
    z rachunkiem, zero błędów, suwak wraca na wartość faktycznie użytą w martwej strefie przy zerze.

[ZROBIONE 2026-08-16] (Opus 5, xhigh) v51 - zad. 14 (2026-maj) w komplecie: podpowiedź, rozwiązanie
opisowe i widżet przesunięcia paraboli. Plus naprawa skakania suwaków we wszystkich widżetach.
[2026-maj, widzety, css, zadanie-14]

- Zadanie: parabola f o wierzchołku W = (3, -2), g(x) = f(x + 1), jednym z miejsc zerowych g jest 0,
  wyznaczyć f w postaci ogólnej. Policzone od zera i zgodne z kluczem CKE: a(1-3)² - 2 = 0 daje
  a = 1/2, czyli f(x) = ½x² - 3x + 5/2. `formulasPage` poprawione z 7 na 8, bo postać kanoniczna
  (potrzebna do startu) siedzi w tablicach na stronie 8, a nie 7.
- Nowy `widgets/przesuniecieParaboli.js` (`widgetPrzesuniecieParaboli`), dwie zakładki:
  - „Przesunięcie": a = 1/2 na sztywno, suwak zmienia liczbę w nawiasie od -3 do 3. Sedno zadania,
    czyli że PLUS w nawiasie przesuwa wykres w LEWO. Strzałka między wierzchołkami mówi wprost
    „1 w lewo" / „2 w prawo", odczyt podaje wierzchołek i miejsca zerowe g, ✓ przy jedynce.
  - „Rozwarcie": jedynka zablokowana, suwak zmienia a (0,2 do 1,3), uczeń doprowadza g do przejścia
    przez pomarańczowy pierścień w punkcie (0, 0) i trafia w a = 1/2. Odczyt to podstawienie
    4a - 2 = 0, po trafieniu pokazuje gotowy wzór f w postaci ogólnej.
  - Obie zakładki: parabolę można ZŁAPAĆ i przeciągnąć (zakładka 1 w bok, zakładka 2 za ramię
    w pionie). Chwyt zapamiętuje odstęp od wierzchołka, więc wykres nie skacze pod palec, a przy
    chwycie zapisywane jest, KTÓRĄ parabolę złapano (bez tego przeciąganie w zakładce 2 liczyło
    rozwarcie z drugiej krzywej i wartość uciekała do końca zakresu).
- Decyzja Henricha: przesunięcie nie dostaje żadnej litery. „c" kolidowałoby z wyrazem wolnym
  postaci ogólnej, „p" z pierwszą współrzędną wierzchołka; uczeń widzi samą liczbę w f(x + 1).
- Wspólny CSS suwaków: `.wg-suwak-etykieta` ma teraz szerokość STAŁĄ (`width` zamiast `min-width`,
  z nadpisaniem przez `--wg-etykieta-szer`), więc dłuższy napis rośnie w lewo i suwak stoi w miejscu.
  To była realna uwaga Henricha („suwak skacze lewa-prawa"), dotyczyła też zad. 13.
- `style/responsive.css`: poniżej 560px suwak widżetu zwężony do 210px. Przy 320px plus etykieta
  wychodził poza krawędź karty na telefonie (procentowy `max-width` nie wie o szerokości etykiety).
- Weryfikacja (Playwright, `node tools/serwer.js 8001`), wszystko na świeżo po zmianach:
  - zad. 14 na desktopie i telefonie (485px) × motyw jasny i ciemny: `.katex-error` = 0, ✓ zapala się
    dokładnie przy a = 0,5, zrzuty obu zakładek i obu skrajnych wartości suwaka;
  - przeciąganie: chwyt ramienia g i ruch o 1,5 w prawo daje liczbę -0,5 (odwrotność, zgodnie
    z matematyką), przeciągnięcie ramienia w zakładce 2 trafia w a = 0,5, a chwyt w pustym miejscu
    płótna nie rusza niczego;
  - widżety dotknięte zmianą wspólnego CSS (zad. 2, 11, 13.1, 13.2 w maju oraz 5, 15, 30 w grudniu),
    desktop i telefon: każdy suwak mieści się w karcie z zapasem 63-144px;
  - wysokość tytułu widżetu przy zmianie zakładki: 23 → 23px na desktopie, 44 → 42px na telefonie,
    czyli płótno nie skacze (tytuły obu zakładek celowo podobnej długości).

[ZROBIONE 2026-08-16] (Opus 5, medium) v50 — domknięcie odwracania kolorów: jedna barwa w widżecie i w filmie.
[dark-mode, kolory, widzety, dokumentacja]

- `--wg-niewiadoma` w ciemnym motywie: pomarańcz `#eb9614` → błękit `#46aadf`, w obu
  bliźniaczych blokach style/base.css. Widżetów nie trzeba było ruszać, wszystkie czytają token
  przez `WG_KOLORY` (sprawdzone: 9 plików w widgets/ używa `WG_KOLORY.niewiadoma`, żaden nie ma
  wpisanego hexa).
- Powód: `#46aadf` to dokładnie to, co filtr v49 robi z błękitem `#0077b6` ze scen Manima.
  Pomarańcz istniał tylko po to, żeby zgadzać się z filmem po STARYM filtrze; po v49 film zostaje
  niebieski, więc widżet i film pokazywały dwie różne barwy tej samej rzeczy.
- Kontrast sprawdzony: `#46aadf` na tle `#141414` daje 7,08:1, czyli powyżej progu AAA.
  Zrzuty w obu motywach (oś liczbowa zad. 11, parabola zad. 19): punkt podstawiania jest teraz
  niebieski w obu motywach, zero błędów JS.
- COLORS.md przebudowane wg uwagi Henricha: znika opowieść o „innym kolorze w każdym motywie",
  bo po v49 nie ma już ani jednej takiej roli. Tabela ról dostała kolumnę „barwa" (jedna nazwa
  na oba motywy), a dwie kolumny z hexami są opisane jako dokładne odcienie tej samej barwy,
  dobrane pod kontrast. Sekcja o filtrze mówi wprost, że ciemny wariant tokenu się LICZY
  (tools/odwroc-kolor.py), a nie wybiera.
- Zaktualizowane wszystkie miejsca mówiące o odwracaniu: COLORS.md, ARCHITECTURE_CSS.md,
  issues/dark-mode-inwersja-przegladarki.md, tools/odwroc-kolor.py.
- Rozstrzygnięte przy okazji (Henrich): rozjechane odcienie ciemnej szarości między tłem grafiki
  a tłem strony na Bazzite (Chrome/Brave) to sprawa maszyny, czyli Bazzite i Waylanda, a nie
  strony. Na Windowsie wszystko gra. Problem A w issues/dark-mode-inwersja-przegladarki.md
  zamknięty, warianty naprawy (osobne pliki na ciemny motyw) schodzą z listy pilnych.
- Nowe zgłoszenie od Henricha (OTWARTE, w TODO): Firefox na Bazzite jako jedyny zachowuje się
  tak, jakby obrotu odcienia nie było. Chrome na tej samej maszynie, Windows oraz Pixel 7a
  (Chrome i Firefox) działają poprawnie. Kolejność diagnozy: numer wersji w rogu (stary CSS
  w pamięci przeglądarki) → about:support (rysowanie na karcie graficznej) → profil koloru/HDR.
  Samsung Browser świadomie odpuszczony, sam przemalowuje strony.

[ZROBIONE 2026-08-16] (Opus 5, medium) v49 — ciemny motyw przestał przekłamywać kolory na rysunkach i w filmach.
[dark-mode, kolory, css, wideo, manim]

- `--filtr-grafik-zadan` w style/base.css: `invert(92%)` → `invert(92%) hue-rotate(180deg)`,
  w obu blokach (motyw z systemu i wymuszony klasą). Reszta CSS bez zmian, bo wszystkie trzy
  miejsca filtrujące (`.question img`, wideo kroków, obrazki kroków) biorą tę samą zmienną.
- Problem: goły invert odwraca każdy kanał osobno, więc barwa lądowała po przeciwnej stronie
  koła kolorów. Fioletowy wykres w zad. 10 (2024-grudzień) był w ciemnym motywie ZIELONY,
  a zielone piątki w filmie zad. 2 były RÓŻOWE — czyli kolor niosący „poprawne" (COLORS.md)
  pokazywał w ciemnym motywie coś zupełnie innego.
- Dołożone `hue-rotate(180deg)` zawraca odcień, przez co odwraca się sama jasność.
  Sprawdzone rachunkiem i zrzutami: `#0077b6` → `#46aadf`, `#7030a0` → `#d49efc`,
  `#003366` → `#a1ccf7`. Rysunki czarno-białe (większość CKE) wyglądają identycznie jak dotąd.
- 92% zostało celowo, nie 100%: biel z pliku dalej ląduje dokładnie na `#141414`, czyli w tle
  strony, więc grafiki nie dostały czarnej ramki. Przy `invert(1) hue-rotate(180deg)` biel
  poszłaby na czyste `#000` i ramka by się pojawiła.
- Rozważany był filtr SVG `feColorMatrix` odwracający luminancję. Odrzucony, bo daje
  liczbowo TEN SAM wynik (różnica 1/255 z zaokrągleń współczynników w specyfikacji CSS),
  a wymaga wklejenia SVG w stronę i pamiętania o `color-interpolation-filters="sRGB"`
  (bez tego SVG liczy w linearRGB i wynik jest bezużyteczny: szary 50% wychodzi prawie biały).
  Do `feColorMatrix` warto wrócić tylko wtedy, gdy zechcemy REGULOWAĆ nasycenie — `hue-rotate`
  nie ma pokrętła.
- Ograniczenie do zapamiętania przy scenach Manima: bardzo jaskrawe barwy nie mieszczą się
  w skali i są przycinane (żółty `#ffcc00` → brązowy `#714600`, czysta zieleń blednie).
  `tools/odwroc-kolor.py` douczony nowego filtru i ostrzega o przycięciu; COLORS.md zaktualizowane.
- ZOSTAWIONE BYŁO DO DECYZJI: pomarańczowy `--wg-niewiadoma` w ciemnym motywie. Henrich zgodził
  się tego samego dnia, zrobione w v50 (wpis wyżej).

[ZROBIONE 2026-08-15] (Fable 5, medium) v48 — poprawki widżetów maja po uwagach Henricha z testów.
[2026-maj, widzety, pilotaz-fable]

- 12.1 zd. 2: zakres prostych przedziału [-4, 5,5] (prawa kończyła na 4,75 i to irytowało);
  lewa prosta z capem 4,5, a kandydat maksimum z capem min(b, 5), żeby przedział zawsze
  zahaczał o dziedzinę [-4, 5). Punkt maksimum r=7, kreska do osi w kolorze punktu
  (pomarańczowa przerywana 1,5 px), "4" w odczycie też pomarańczowe.
- 12.2 zd. 1: tytuł z dopiskiem "Ten widok nie jest interaktywny."; zd. 2: usunięta kropka
  uchwytu z osi y (prostą i tak ciągnie się w dowolnym miejscu płótna), nowy tytuł.
- Płynne sterowanie zamiast progów 0,25 (zamówienie: "bez progów, jeśli banalnie proste"):
  suwaki step 0.05 + wgPrzyciagnij do wartości zadania na input (13.1: a->-1,5 i b->-3,
  13.2: a->-1,5, 12.2: c->1), przeciąganie zaokrąglane do 0,05 zamiast 0,25 (zad. 8, 10,
  12.1 obie zakładki, 12.2, 13.1). Trafienia (===) działają dzięki snapowi. Zad. 2 (krok 0,1)
  i zad. 11 (bilety całkowite) celowo bez zmian.

[ZROBIONE 2026-08-15] (Fable 5, medium) v47 — zad. 13 (2026-maj): rysunek + widżety 13.1/13.2, kwadratowa kratka układów.
[2026-maj, widzety, tresc, pilotaz-fable, media]

- Rysunek zad. 13 wycięty z arkusza (ta sama metoda libgs/ctypes co zad. 12) => media/zad13/zad13rys.png.
- widgets/funkcjaLiniowa.js: widgetLiniowaWspolczynniki (13.1: suwak a niebieski obraca prostą
  wokół (0,b), suwak b żółty unosi, żółty punkt na osi y przeciągalny; łuk kąta alfa jak na
  rysunku CKE; odczyt ze znakami a i b pod zdania P/F) i widgetLiniowaTangens (13.2: trójkąt
  na RAMIENIU kąta alfa, jak definicja funkcji tryg. dowolnego kąta z tablic s. 11: y = 3
  w górę, x = 3/a ze znakiem; tg = y/x, minus z ujemnego x, nie z y - rozstrzygnięte
  z Henrichem po jego czujnym pytaniu, pierwotny plan "minus z delta y" był konwencją
  nachylenia i nie pasował do narysowanego kąta). Etykiety suwaków .wg-suwak-etykieta
  (stała szerokość, sheet.css).
- wgWysokoscKwadratowa w _helpers.js: wysokość płótna dająca kwadratową kratkę; zad. 12 i 13
  przestawione na nią po uwadze Henricha, że wykres 12 był ściśnięty.

[ZROBIONE 2026-08-15] (Fable 5, medium) v46 — zad. 12 (2026-maj): rysunek z arkusza + widżety 12.1/12.2 z zakładkami, nowe klocki wielorazowe.
[2026-maj, widzety, tresc, pilotaz-fable, helpers, media]

- Rysunek do treści zad. 12: w kontenerze nie ma rasteryzatora PDF (brak poppler/gs binarki,
  PyPI za firewallem, headless Chromium nie renderuje PDF, dvisvgm daje czarne kafle na
  bitmapach), ale JEST /usr/lib/.../libgs.so.10 (zależność dvisvgm) - strona 12 arkusza
  zrasteryzowana Ghostscriptem wołanym przez python3 + ctypes (gsapi_*, png16m, 220 dpi),
  wykres wycięty PIL-em z autotrymem bieli => media/zad12/zad12rys.png (707x695), alt
  uzupełniony. Metoda do powtórki przy następnych rysunkach.
- Nowe klocki wielorazowe w widgets/_helpers.js (zamówienie: projektować pod ponowne użycie):
  wgZakladki (pasek kart nad widżetem, style .wg-zakladki w sheet.css, aktywna karta w kolorze
  wyboru ucznia), wgUklad (mapowanie wartość<->piksel z marginesami), wgRysujUklad (siatka,
  osie ze strzałkami, podziałka z odstępem pod kropki). Opisane w widgets/README.md.
- widgets/funkcjaLamana.js: wspólna łamana f (x+2 na [-4,2], -x+5 na (2,5), pełne/puste kółka)
  + dwa widżety: widgetLamana121 (zakładka 1: pozioma prosta f(x)=c z punktami przecięcia
  i ✓ przy c=3; zakładka 2: dwie pionowe proste przedziału z zapisem [a,b] pod nimi,
  pomarańczowy punkt maksimum z kreską do osi y, ✓ przy [2,3]) i widgetLamana122 (zakładka 1
  statyczna: pas i odcinek zbioru wartości [-2,4] na osi y; zakładka 2: prosta y=c sterowana
  punktem na osi y lub suwakiem, zielony przedział rozwiązań na osi x z pełnymi/pustymi
  kółkami, domknięcie prawego końca na 2 dla c w [3,4), ✓ przy c=1). Komplet: hinty
  i rozwiązania opisowe dla 12.1 i 12.2; wpis-rodzic zad. 12 tylko z rysunkiem.

[ZROBIONE 2026-08-15] (Fable 5, medium) v45 — zad. 11 (2026-maj) w komplecie, wg opisu widżetu od Henricha.
[2026-maj, widzety, tresc, pilotaz-fable]

- Podpowiedź (oznaczenie niewiadomych + przepis na układ), rozwiązanie opisowe (podstawienie
  n = 200 − u, wynik u = 78), nowy widżet widgets/bilety.js: suwak n (kolor niewiadomej,
  accentColor jak w zad. 2), niski wykres kwoty po kosztach (prosta 3750 + 7,5n, NIE parabola,
  bo zależność jest liniowa; zamówienie mówiło "wykres funkcji kwadratowej", zgłoszone w czacie)
  z zieloną przerywaną linią celu "zostało: 4 665 zł" (wzór: linia celu zad. 5 grudnia).
- Rachunek pod suwakiem w kolumnach (KaTeX array {rclcl}: n pod n, u pod u, wyniki pod sobą),
  liczby dopychane \hphantom do 3 cyfr, żeby kolumny nie skakały przy przewijaniu suwaka;
  ostatnia linijka "6220 zł − 25% = 4665 zł" z ✓/✗ (wg szkicu Henricha z czatu).
- \text{zł} renderuje się w KaTeX-ie poprawnie (sprawdzone, 0 błędów).

[ZROBIONE 2026-08-15] (Fable 5, medium) v44 — zad. 10 (2026-maj) w komplecie + drobne do zad. 2 i 8.
[2026-maj, widzety, tresc, pilotaz-fable]

- Zad. 10, komplet: podpowiedź (przepis jak w zad. 9 grudnia), rozwiązanie opisowe (uproszczenie
  do 3x² − 2x − 8 ≥ 0, delta, pierwiastki −4/3 i 2, przedziały na zewnątrz), nowy widżet
  widgets/nierownoscTrojmianu.js na wzór nierownoscKwadratowa.js: parabola, zielone promienie
  rozwiązań, przeciągany punkt z przyciąganiem do pierwiastków; podstawienie −4/3 wyświetlane
  ułamkiem (nie zaokrągleniem), ✓/✗ liczone z dokładnej wartości.
- Zad. 2: strzałki między słupkami skrócone o ~22% z każdej strony (kleiły się do rogów),
  "odsetki:" -> "suma odsetek:" w odczycie.
- Zad. 8 (punkty z TODO od Henricha): trzecia linijka rozwiązania brzmi teraz "Wystarczy, że
  któryś z nawiasów będzie równy 0, to całość też się wyzeruje, więc:"; .widget-title dostał
  margines 14 px z góry (wszystkie widżety), bo kleił się do separatora.

[ZROBIONE 2026-08-15] (Fable 5, medium) v43 — druga runda uwag Henricha do zad. 2 i 8 (2026-maj).
[2026-maj, widzety, tresc, pilotaz-fable]

- Zad. 2: kwoty odsetek przeniesione na strzałki MIĘDZY słupkami (podpis "( + 636 zł )" nad
  słupkiem wyglądał na sumę odsetek, nie przyrost roku), przerywana linia bazowa na 10 000 zł,
  przywrócona linijka "odsetki: 600 + 636 = 1236" (miała sens, usunięta przez nieporozumienie);
  p i suwak w kolorze niewiadomej (slider.style.accentColor odświeżany w draw()); większe płótno
  (250 px) i czcionka 13 px.
- Zad. 8: rozwiązanie opisowe w 3 kolumnach (KaTeX \begin{array}{ccc}; separator @{\qquad} nie
  istnieje w KaTeX-ie, \qquad wkładane do komórek); widżet bez suwaka (klik/przeciąganie), m bez
  specjalnego koloru (token --wg-fiolet-mocny wycofany z base.css i _helpers.js), odczyt: iloczyn
  z obliczonymi nawiasami i "0 = 0" ✓ zamiast linijki o sumie (suma została w rozwiązaniu opisowym).
- Uniwersalnie: .widget-readout powiększony i z line-height 2.1 (spójnie z .rozwiazanie-kroki);
  liczby pod osią schodzą pod promień punktu także w osLiczbowa.js i nierownoscKwadratowa.js.

[ZROBIONE 2026-08-15] (Fable 5, medium) v42 — poprawki Henricha do zad. 2 (2026-maj) + zad. 8 w komplecie.
[2026-maj, widzety, tresc, pilotaz-fable]

- Zad. 2, poprawki po testach v41: podpowiedź skrócona do samego wzoru; suwak startuje na 6,0%;
  segment odsetek i podpisy w kolorze niewiadomej (--wg-niewiadoma, odwraca się z motywem);
  podpisy w formie "( + 600 zł )" i pół linijki wyżej; słupki przesunięte 25 px w lewo (środkowy
  na środku płótna); odczyt bez strzałki, w dwóch linijkach, linijka "odsetki: ..." skasowana
  (dublowała podpisy na słupkach).
- Zad. 8, komplet: podpowiedź (iloczyn równy 0), rozwiązanie opisowe (rozwiązania z nawiasów,
  suma równa 0, m = 5), nowy widżet widgets/rownanieIloczynowe.js: suwak i przeciąganie ruszają
  x po osi (celowo x, nie m - uczeń widzi, jak zeruje się nawias), rozwiązania -3, -2, m jednym
  fioletem, m wyróżnione nowym tokenem --wg-fiolet-mocny (base.css x3 + WG_ZMIENNE/WG_KOLORY),
  odczyt: równanie, podstawienie z ✓/✗, linijka -3 + m - 2 = 0 => m = 5 (zamówienie Henricha).

[ZROBIONE 2026-08-14] (Opus 5, high) v34 — logo pod welonem przy otwartym panelu bocznym.
[ui, css, sidebar, mobile, a11y]

Zamówienie Henricha: przy otwartym panelu logo ma być przygaszone, „z tyłu" i nieklikalne,
a dotknięcie go ma zamykać panel — bo pomiędzy leży welon.

- **Naprawdę schować logo pod welon się nie da.** `body.sidebar-otwarty #naroznik-lewy` ma
  od v32 `z-index: 13`, żeby strzałka była klikalna, a to tworzy kontekst piętrzenia — żadne
  dziecko nie zejdzie poniżej rodzica.
- **Zrobione więc pozorem, ale wiernym** (`style/responsive.css`, w bloku 1299 px, czyli tam,
  gdzie w ogóle jest welon): `pointer-events: none` na CAŁYM narożniku, `pointer-events: auto`
  z powrotem na strzałce, do tego przygaszona etykieta (`--text-faint`) i ta sama zasłonka
  `rgba(0,0,0,.25)` co welon, malowana jako `linear-gradient` na tle pigułki. Kliknięcie
  spada na welon, a klik w welon to druga ścieżka zamykania panelu (app/bootstrap.js).
- **Dwie pułapki, obie zmierzone, nie zgadnięte:**
  - `pointer-events` MUSI iść na narożnik, nie na samo `#logo` — narożnik jest flexem
    rozciągniętym na oba dzieci, więc to on łapie kliknięcie obok napisu (`elementFromPoint`
    pokazywał `naroznik-lewy`, panel się nie zamykał).
  - NIE `opacity` — półprzezroczysta pigułka pokazuje treść zadania spod napisu; ten sam
    wariant odpadł już przy v32.
- **Klawiatura zrównana z myszą** (`app/bootstrap.js`): `tabindex="-1"` + `aria-hidden` na
  logo, gdy panel nakłada się na treść, zdejmowane przy zamknięciu i przy zmianie rozmiaru
  okna. Bez tego Tab wchodził w link, którego myszą kliknąć się nie da, a Enter wychodziłby
  ze strony.

Sprawdzone Playwrightem: 485 px jasny i ciemny — `pointer-events: none`, kolor przygaszony,
`tabindex="-1"`, pod kursorem `sidebar-przyciemnienie`, klik zamyka panel i NIE nawiguje;
1400 px bez zmian (logo dalej zwykłym linkiem). Osobno regresja z v32: strzałka zamyka
otwarty panel przy 485 / 900 / 1400 px. Konsola czysta.

[ZROBIONE 2026-08-14] (Opus 5, high) Sprzątanie sekcji „DOPISANE PRZEZ CLAUDE-A" w TODO.md.
[porzadki, todo, dokumentacja]

Rozdysponowane wg komentarzy Henricha pisanych WIELKIMI LITERAMI. Gdzie co poszło:

- **na górę, do „HENRICH MÓWI MA TO SENS"** (skrócone do jednej-dwóch linijek): domena
  matematykazen.pl jako FAZA 2.3 (URL „Required Notice" w LICENSE.md + wpis w firewallu
  kontenera — dwa punkty złączone w jeden, bo mają ten sam wyzwalacz), kaskada progów
  w kryteriach zadań 4-punktowych, tryb testowy zgłoszeń `?test-zgloszenie=1`, podmiana
  pseudonimu na nazwisko.
- **do `DO ZROBIENIA HOŚCIE`**: sprawdzenie devcontainera na Kubuntu/Dockerze (wymaga
  drugiej maszyny, więc nie jest to zadanie dla modelu w kontenerze).
- **do `NIE REALIZUJ, CZEKAJĄ W KOLEJCE`**: martwe `finalAnswer.label` w danych — obok
  bliźniaczego `solutionTextMore`.
- **do `ULEPSZANIE WORKFLOW`**: „stworzyć własne skille pod ten projekt" (z punktu o skillach
  zostało tylko to; pobieranie i wpinanie jest zrobione). Przy okazji zdjęte stamtąd trzy
  pozycje oznaczone DONE — plugin frontend-design, superpowers i zasada o tłumaczeniu.
- **skasowane jako już opisane gdzie trzeba**: trzy notatki o devcontainerze (sockety VS Code,
  `sudo` bez SETUID/SETGID, dozwolone domeny jako kanał danych) — wszystkie trzy są
  w `.devcontainer/README.md`, sekcje „Czego to NIE chroni" i „`--cap-drop=ALL` bez wyjątków";
  nazwa rewersu dokładana przez odtwarzacz — `issues/krok-po-kroku-produkcja.md`; awaryjne
  przyciski „0..N pkt" bez `gradingCriteria` — `ARCHITECTURE.md`; decyzje projektowe z paczki
  v15 (Sonnet) i z odtwarzacza v20 — opisane w tym pliku przy swoich wpisach, a Henrich je
  przyjął po testach.
- **przeniesione do plików**: ostrzeżenie o `python3 -m http.server` przy pracy nad wideo →
  `manimations/README.md`, punkt 5 workflow (Henrich prosił, żeby leżało tam, gdzie się
  renderuje filmy); H.264 w Chromium — działa lokalnie, nie działało w chmurze →
  `issues/playwright-podglad.md`; kontrast `--text-faint-2/-3` i cienie kropek wskaźników →
  `ARCHITECTURE_CSS.md`, przy opisie tokenów.

[ZROBIONE 2026-08-14] (Henrich — testy) odbiór v32, panel boczny w lewym górnym rogu: strzałka nad welonem działa w obu motywach, biały prostokąt tła pod logo zostaje (zdjęcie go przepuszczało treść zadania spod napisu — wariant odrzucony przy v32). Punkt zamknięty.
[ui, sidebar, testy, odbior]

[ZROBIONE 2026-08-14] (Opus 5, high) v33 — wczytywanie kroków: prefetch, który naprawdę działa, i kropki zamiast pulsowania kadru.
[krok-po-kroku, wideo, wydajnosc, ui, css]

Dwa punkty „DODATKOWO" z TODO.md, oba o czekaniu na film.

1. **Prefetch nie docierał do odtwarzacza** (zgłoszenie Henricha: „w logach widać zapis do
   cache, ale odtwarzacz z niego nie korzysta"). Pobieranie w tle było zwykłym `fetch`em
   liczącym na to, że `<video>` weźmie plik z cache'u HTTP przeglądarki. `<video>` pyta
   jednak ŻĄDANIEM ZAKRESOWYM, a to trafia w cache tylko przy komplecie warunków (walidator
   od serwera, cache'owalna odpowiedź, brak „Disable cache" w DevTools, chętna przeglądarka).
   Teraz pobrany plik zostaje u nas jako `Blob`, a `<video>` dostaje adres `blob:` — podmiana
   kroku nie kosztuje ani jednego bajtu z sieci. Zmierzone Playwrightem: po otwarciu
   rozwiązania i pięciu przejściach **0 żądań mp4** (wcześniej jedno na krok).
   Budżet pamięci 64 MB z LRU (cały arkusz 2024-grudzień to ~9 MB), nigdy nie zwalniamy
   adresu, który siedzi w kadrze. Do tego priorytet dla widza: gdy odtwarzacz sam musi
   sięgnąć do sieci, kolejka **przerywa** swoje pobranie i milknie na 2 s, a przerwany plik
   wraca na jej czoło — na wolnym łączu pasmo idzie do filmu, na który ktoś patrzy.
   `<video>` niesie teraz `data-plik` ze ścieżką, bo z „blob:…" nie widać, który to krok
   (czyta to tools/test-krokow.js).

2. **Pulsowanie kadru wyrzucone.** Zamiast pulsu tła i przygaszania obrazu jest
   `.steps-ladowanie`: trzy kropki w pigułce przy dolnej krawędzi kadru, wchodzące dopiero
   po 500 ms (`transition-delay`), gasnące natychmiast. Obraz zostaje nietknięty, więc nic
   już nie miga przy zmianie kierunku ani przy spamowaniu ►. Wskaźnik musiał zamieszkać
   poza `.steps-content` (ten dostaje `replaceChildren` przy każdej podmianie), stąd nowa
   owijka `.steps-kadr` — przejęła też ograniczenie szerokości i margines, żeby margines nie
   przeciekał poza kadr.

Sprawdzone: tools/test-krokow.js na szybkim i na zdławionym serwerze (60 kB/s) — komplet bez
zastrzeżeń; geometria kadru bez zmian (608×342 desktop, 447×251 telefon, brak poziomego
scrolla); zrzuty kropek w obu motywach, nad pustym kadrem i nad poprzednim krokiem.

[ZROBIONE 2026-08-14] (Opus 5, medium) Plugin frontend-design przeniesiony do `.claude/settings.json` — jedzie z repo.
[pluginy, konfiguracja]

Decyzja Henricha. Włącznik siedział w `.claude/settings.local.json` (poza gitem), więc na
nowej maszynie trzeba by go doklikiwać. Teraz jest obok `superpowers`, czyli przychodzi
razem z klonem repo. Plugin dotyczy wyglądu strony, więc należy do projektu, nie do jednego
stanowiska.

W `settings.local.json` **zostają świadomie** `chrome-devtools-mcp` i `github` — oba są
narzędziami tego konkretnego kontenera, a nie projektu: pierwszy zależy od wrappera Chrome'a
w obrazie, drugi od tokenu Henricha. Klon repo dostałby je niedziałające.

[ZROBIONE 2026-08-14] (Henrich — testy) odbiór v32: jedna wspólna szerokość ramki „sprawdzanie obliczeń" / pola na notatki / rozwiązania / formularza zgłoszenia błędu, i odrobinę szersze przyciski A/B/C/D w zadaniach zamkniętych — oba potwierdzone na telefonie, bez błędów.
[ui, css, mobile, testy, odbior]

[ZROBIONE 2026-08-14] (Opus 5, medium) chrome-devtools-mcp wreszcie otwiera strony — trzy warstwy problemu zdjęte.
[devcontainer, pluginy, chrome, testy]

Plugin był martwy od instalacji 13.08. Każda naprawa odsłaniała kolejną przyczynę:

1. **EACCES na `~/.cache`** — katalog należał do roota, `node` nie mógł założyć w nim
   podkatalogu. Naprawione `chown`em w Dockerfile.
2. **Brak Chrome'a** — plugin szuka sztywno `/opt/google/chrome/chrome`. Zamiast
   instalować prawdziwego Chrome'a (+150 MB, dziura w firewallu na repozytorium Google)
   podstawiliśmy Chromium Playwrighta, które i tak jest w kontenerze bindem z hosta.
   Przedstawia się jako „Google Chrome for Testing 151", więc kanał „stable" je przyjmuje.
3. **Piaskownica Chrome'a** — `Check failed: sys_chroot(…)`, bo kontener ma `--cap-drop=ALL`.
   To był prawdziwy powód komunikatu „Protocol error: Target closed". **Playwright chodzi
   tu od zawsze, bo sam dokłada `--no-sandbox`; plugin tego nie robi**, a flag nie mamy jak
   mu podać — jego `args` siedzą w cache'u pluginu poza repo i giną przy aktualizacji.

Rozwiązanie punktu 3: `/opt/google/chrome/chrome` przestał być symlinkiem, a stał się
jednolinijkowym wrapperem, który dokłada `--no-sandbox --headless=new` i przekazuje resztę
argumentów dalej. Dzięki temu plugin zostaje **nietknięty razem ze swoimi pięcioma skillami**
(a11y, LCP, wycieki pamięci, troubleshooting, debugowanie ogólne), nic się nie dubluje i nie
trzeba samemu pilnować wersji `chrome-devtools-mcp@x`. Odrzucony wariant: własny wpis serwera
w `.mcp.json` w repo — działałby bez przebudowy, ale kosztem wyłączenia pluginu i jego skilli.

Metoda, która to odblokowała: flagi sprawdzono **przed** przebudową, ręcznym klientem MCP po
stdio (`spawn` serwera + surowy JSON-RPC), więc Henrich nie rebuildował kontenera na ślepo.
Warto o tym pamiętać przy następnym problemie z serwerem MCP — nie trzeba restartu sesji.

Odbiór po Rebuildzie: `navigate_page` wchodzi na arkusz, `take_screenshot` zwraca realny zrzut
ze złożonym KaTeX-em, żadne okno nie wyskoczyło na ekran hosta. Pełna historia z dowodami
i odrzuconymi wariantami: `issues/chrome-devtools-mcp-cache-eacces.md`.

**Przy podbiciu Playwrighta** ścieżka w wrapperze ma numer builda (`chromium-1234`) — trzeba
poprawić `CHROMIUM_BUILD` w Dockerfile, inaczej wraca „Could not find Google Chrome executable".

[ZROBIONE 2026-08-14] (Opus 5, medium) Weryfikacja kontenera po Rebuild Container — komplet testów odebrany.
[devcontainer, pluginy, testy, odbior, narzedzia]

Wszystkie trzy poprawki z commita 14b0715 działają w przebudowanym obrazie:

- **`~/.cache` należy do `node`** i jest zapisywalny — EACCES zniknął, `chrome-devtools-mcp`
  sam założył sobie `~/.cache/chrome-devtools-mcp/chrome-profile`.
- **Plugin `github`** — `claude mcp list` pokazuje ✔ Connected zamiast HTTP 400. Zmienna
  `GITHUB_PERSONAL_ACCESS_TOKEN` ustawiona, `gh` zalogowany **z wolumenu**, czyli
  `matematykazen-gh-config` faktycznie przeżył przebudowę i drugie `gh auth login` nie było
  potrzebne. Uwaga na przyszłość: pierwsze wywołanie potrafi zwrócić „tools fetch failed —
  timeout", drugie przechodzi.
- **`ms-python.python`** wjechał sam — Henrich potwierdził kolorowanie w `manimations/`.
- **„Allow Automatic Tasks in Folder?"** — Henrich: „nigdy nie widziałem tego pytania"
  (szczegóły we wpisie niżej).

Przy okazji przetestowana reszta środowiska: firewall trzyma (`api.github.com` 200,
`example.com` odcięte), `tools/serwer.js` zwraca 206 na `Range`, `tools/zrzuty.js` robi
komplet 16 zrzutów, `tools/test-krokow.js` przechodzi bez zastrzeżeń na szybkim **i** na
zdławionym serwerze (czyli v31/v32 nie ruszyły odtwarzacza), konsola strony czysta poza
`gc.zgo.at` (analityka, celowo blokowana). Wersja v32 zgodna w `template.html` i `index.html`.

**Co wyszło spod spodu i ZOSTAJE OTWARTE:** `chrome-devtools-mcp` dalej nie otwiera strony,
ale z zupełnie innego powodu — w kontenerze nie ma Google Chrome'a, jest tylko Chromium
Playwrighta. Warianty wyjścia w `issues/chrome-devtools-mcp-cache-eacces.md`, punkt wisi
w TODO.md pod OPUS DOPISAŁ. Pracy nie blokuje, bo zrzuty i tak idą przez `tools/zrzuty.js`.

[ZROBIONE 2026-08-14] (Opus 5, medium, na hoście) Zadania z sekcji „DO ZROBIENIA HOŚCIE" + odbiór testów v32.
[devcontainer, pluginy, host, testy, odbior]

- **Odbiór v32 (Henrich):** przyciski ◄ ► pod filmem, wyrównanie ikon, marginesy paska kropek
  i wcięcie tekstu w „pokaż wyjaśnienie kroku" — potwierdzone, skasowane z TODO.md. Dwie uwagi
  wróciły do DO ZROBIENIA: strzałka wychodzi nad welon tylko w ciemnym motywie, a biały prostokąt
  tła pod logo ma zniknąć (logo nie musi wychodzić nad welon — wtedy odpada też problem
  przebijającej treści zadania, opisany we wpisie niżej). Ostatni punkt v32 (wspólna szerokość
  ramek na telefonie) czeka na przeklikanie.

- **Rozszerzenie Pythona** (`.devcontainer/devcontainer.json`): dopisane `ms-python.python`,
  żeby przeżywało Rebuild Container. Pylance i debugpy przychodzą z nim jako extension pack,
  więc nie są wypisane osobno. Marketplace jest na allowliście firewalla, instalacja przejdzie.

- **`~/.cache` należało do roota** (`.devcontainer/Dockerfile`): dołożone do istniejącego
  `mkdir -p … && chown -R node:node`. To wariant 1 z `issues/chrome-devtools-mcp-cache-eacces.md`
  — naprawia całą klasę problemu, nie tylko chrome-devtools-mcp. Wymaga Rebuild Container.

- **Plugin `github`** (HTTP 400, pusty nagłówek Bearer): Dockerfile dopisuje do `~/.zshrc`
  i `~/.bashrc` `export GITHUB_PERSONAL_ACCESS_TOKEN="$(cat ~/.config/gh/mcp-token || gh auth token)"`.
  W repo nie ląduje żaden sekret — token czytany jest lokalnie z zalogowanego `gh`; `mcp-token`
  to furtka na węższy PAT, gdyby pełne uprawnienia `gh` były za szerokie (pytanie Henricha
  w trakcie sesji: klon repo NIE dostaje jego uprawnień).

- **„Allow Automatic Tasks in Folder?"** — punkt okazał się nieaktualny: `task.allowAutomaticTasks:
  "on"` siedzi w `~/.config/Code/User/settings.json` od 2026-08-12. **Potwierdzone
  2026-08-14** — Henrich: „nigdy nie widziałem tego pytania". Punkt skreślony z testów.

- **Backup `~/backup-vscode-flatpak/`** skasowany (decyzja Henricha). Weryfikacja przed
  kasowaniem: flatpaka nie ma w systemie, `snippets/` puste, a jedyna unikatowa treść
  (trzy osierocone ustawienia) jest przepisana do `issues/flatpak-osierocone-dane.md`.

- **frontend-design** zostaje jedynym otwartym punktem sekcji hosta: działa, ale jego włącznik
  jest w nieśledzonym `.claude/settings.local.json` — do decyzji, czy ma jechać z repo.

[ZROBIONE 2026-08-14] (Opus 5, medium, lokalnie) v32 — strzałka panelu bocznego nad przyciemnieniem.
Punkt leżał w sekcji NIE REALIZUJ; Henrich kazał go wziąć po tym, jak testy regresji v31 pokazały,
że klik w strzałkę jest przechwytywany.

- **Objaw i dlaczego nikt tego nie zgłaszał:** poniżej progu 1300 px welon `#sidebar-przyciemnienie`
  (z-index 11) leżał NA lewym narożniku (10), a więc i na strzałce. Strzałka wyglądała na wyszarzoną,
  nie łapała hoveru, a kliknięcie trafiało w welon. Panel mimo to się zamykał — klik w welon jest
  jego drugą ścieżką zamykania (`app/bootstrap.js`) — więc z zewnątrz wszystko wyglądało poprawnie
  („u mnie działa"). Wyszło dopiero z Playwrighta: `page.click` czeka na realną klikalność elementu
  i przekroczył czas. To NIE był problem z siecią ani z serwerem.

- **Naprawa** (`style/sheet.css`): `body.sidebar-otwarty #naroznik-lewy { z-index: 13 }` — narożnik
  wychodzi nad welon (11) i nad panel (12) tylko na czas otwartego panelu. Narożnik kończy się nad
  górną krawędzią panelu (56 px, na telefonie 48 px), więc wyższa warstwa niczego nie zasłania.
  Zweryfikowane na 390/1280/1400 px: pod kursorem jest teraz SVG strzałki, panel zamyka się jej
  kliknięciem przy każdej z tych szerokości.

- **Dwa warianty odrzucone po zrzutach**, obie próby są opisane w ARCHITECTURE_CSS.md:
  welon od 56 px w dół zamiast `inset: 0` — nad panelem zostaje niewyciemniony pasek treści zadania
  („Zadanie 3" wystaje zza narożnika); zdjęcie tła `#logo` na czas otwartego panelu — spod napisu
  wyłazi ta sama treść. Logo zostaje więc z prostokątem i razem ze strzałką czyta się jako
  wyniesione nad welon; prawa pigułka z punktami zostaje przygaszona.

- **Przy okazji** dopisana notatka do `issues/playwright-podglad.md`: błąd konsoli
  `gc.zgo.at/count.js — ERR_ADDRESS_UNREACHABLE` w kontenerze jest nieszkodliwy (analityka
  GoatCounter blokowana przez firewall; kod od początku pomija ten zasób w handlerze błędów),
  a testy zbierające konsolę mają go odfiltrowywać.

[ui, panel-boczny, mobile, css, testy]

[ZROBIONE 2026-08-14] (Opus 5, medium, lokalnie) v31 — cztery drobiazgi UI wybrane przez Henricha
z listy „samotnych michałków". Same style, zero zmian w JS. Weryfikacja: Playwright (pomiary
computed style + zrzuty 390/1440 px) i tools/test-krokow.js (zad. 1–3, ziarna 3 i 11) — bez zastrzeżeń.

- **◄ ► rozsunięte i powiększone** (style/sheet.css, `.steps-nav`, `.step-ikona`): odstęp 10 → 48 px,
  ikony 22 → 26 px. Henrich wybrał wariant „stały większy odstęp" (trójka zostaje wyśrodkowana)
  zamiast rozrzucania strzałek na krawędzie kadru. Skoro wszystkie trzy ikony mają teraz 26 px,
  osobna reguła `.step-play .step-ikona` zniknęła jako zbędna. Pole dotyku bez zmian (44×44).

- **Marginesy paska kropek** (`.steps-dots-okno`): po 8 px z każdej strony, żeby skrajne kropki nie
  stykały się z krawędzią. Margines na oknie przewijania, NIE padding na `.steps-dots` — ten drugi
  dokłada się do `min-width: 100%` przy content-box i uruchamiał przewijanie już przy siedmiu
  kropkach (pułapka opisana w komentarzu w sheet.css od 2026-08-11). Powiększenia kropek Henrich
  nie chciał — punkt „rozważyć lekkie powiększenie" został w TODO.md.

- **Wcięcie wyjaśnienia kroku** (`.step-explain-tresc`): padding `6px 2px 8px` → `8px 0 10px 30px`.
  Reszta typografii była już wspólna z `.solution-text-container` (18 px, ten sam kolor i rodzina —
  wszystko dziedziczone), różniło je wyłącznie lewe wcięcie. Na telefonie oba akapity startują teraz
  w tym samym miejscu: 18 px karty + 12 px podokna + 30 px wcięcia. Pionowych 30 px z rozwiązania
  celowo nie kopiowałem — tam odcinają tekst od ramki podokna, tu nad tekstem jest sam przycisk zwijania.

- **Szerokość ramki „sprawdzanie obliczeń" na telefonie** (style/responsive.css, `.answers-container`
  → `width: 100%` pod 720 px): przyczyną było bazowe `.button-container { width: 90% }` (sheet.css),
  które ścinało cały blok odpowiedzi do 319 px, gdy rozwiązanie i formularz zgłoszenia miały 354 px.
  Zmierzone po zmianie: `.ocena-box`, `.open-answer`, `.solution-container` i `.zglos-blad-okno`
  mają komplet 354 px i lewą krawędź na 18 px. Efekt uboczny, świadomy: przyciski A/B/C/D zadań
  zamkniętych są na telefonie o te 35 px szersze (na desktopie 90% zostaje — trzyma siatkę w kolumnie).

[krok-po-kroku, ui, mobile, css]

[ZROBIONE 2026-08-14] (Henrich — testy) Odbiór reszty v22 (kropki/panele/formatowanie) i v24
(filmy zad. 1/3/4/6/8). Sekcje testowe obu wersji skasowane z TODO.md; niesprawdzone zostały
v27, v29, v30.

- **Potwierdzone jako działające:** czerwony baner „ResizeObserver loop..." już się nie pojawia
  (regresja z v21 naprawiona); dziesięć kropek zad. 1 mieści się na telefonie bez przewijania;
  rozwiązanie i formularz zgłoszenia błędu mają już właściwy margines (25 px) na telefonie;
  filmy zad. 1 i 3 w kadrze 16:9 bez czarnych pasów, treść przekształceń zgodna klatka w klatkę.

- **v24 — potwierdzone wizualnie, merytoryka odłożona:** opisy kroków zad. 3 (osiem kroków),
  wzory pomocnicze przeniesione do opisów, nowe kroki zad. 4 (logarytmy) i zad. 6/8 — wszystko
  wygląda dobrze, ale dokładną weryfikację matematyczną Henrich robi później, przy pełnym
  sprawdzeniu merytoryki arkusza (patrz TODO.md, sekcja „INNE NOTATKI").

- **Nowe zamówienia z tych testów, wróciły do TODO.md jako DO ZROBIENIA:** przewijanie paska
  kropek przy większej liczbie kroków niż się mieści + opcjonalnie marginesy boczne żeby
  krańcowe kropki nie stykały krawędzi (kropki są dziś na granicy wygody dla kciuka); sformatować
  „step-explain-tresc" jak „solution-text-container"; usunąć całkowicie „solutionTextMore" z
  exercises.json i kodu; poszerzyć panel „sprawdzanie obliczeń" na telefonie do tej samej
  szerokości (25 px) co reszta podokien.

[krok-po-kroku, wideo, ui, testy, odbior]

[ZROBIONE 2026-08-13] (Henrich — testy) Odbiór odtwarzacza krok po kroku, paczki v22, v23, v26 i v28.
Sekcje testowe tych czterech wersji skasowane z TODO.md; niesprawdzone zostały v24, v27, v29, v30.

- **Potwierdzone jako działające:** cofka wciśnięta w trakcie odtwarzania i drugi raz w trakcie cofania;
  koniec cofki (◄ cofa poprzedni krok, ► odtwarza ten sam do przodu); ◄ przerwane przez ► zmienia tylko
  kierunek; kilka ◄ pod rząd; szybkie ► przy słabym łączu; odtwórz wciśnięty w trakcie wczytywania;
  minuta losowego klikania kończy się spoczynkiem; duża kropka zostaje na początku obejrzanego filmu;
  gradacja kresek między kropkami w obu motywach.

- **Nie działa, wróciło do TODO.md jako DO ZROBIENIA:** opóźnienie pulsowania (Henrich: „ta chwila albo
  jest za krótka, albo nie istnieje") — miga przy każdej zmianie kierunku, a przy spamowaniu ► wygląda
  jak wieczne ładowanie; prefetch filmów (Chrome: płaski wykres sieci przy czekaniu, spajki dopiero przy
  klikaniu, w logach zapis do cache bez odczytu). Decyzja Henricha: pulsowanie wyrzucić w całości,
  w zamian trzy kropki / kółko na dole kadru po ~500 ms.

- **Nowe zamówienia z tych testów:** wyciąć długie `wait()` na początku i końcu każdego kroku (najmocniej
  w zad. 1); rozsunąć i powiększyć ◄ ►. Plus zgłoszony crash strony przy spamowaniu next-step
  (Brave na Bazzite, kod błędu 5) — do odtworzenia.

- **Uwaga do sposobu pisania testów:** dwa punkty (koniec cofki w v26, „licznik" w v23) były dla Henricha
  niezrozumiałe — w v23 nie ma na ekranie żadnego licznika, o którym pisałem. Wpis testowy ma mówić, co
  kliknąć i co ma się stać, bez odwołań do nazw z kodu. Zasada jest już w TODO.md („ZASADY DLA CLAUDE-A").

[krok-po-kroku, wideo, ui, testy, odbior]

[ZROBIONE 2026-08-12] (Local Opus 5 High) Filmy krok po kroku: zad. 5 i 6 napisane od nowa,
zad. 3 rozjaśnione. v30 Beta. **Paczka przerwana w połowie na prośbę Henricha (limit sesji)** —
co zostało, jest w TODO.md pod „Błędy w filmach — ZOSTAŁO".

- **Diagnoza.** Zgłoszenie brzmiało „animacje nie mają sensu, cyfry i znaki tańczą bez ładu
  i składu". Winne było `TransformMatchingShapes`: paruje glify po PODOBIEŃSTWIE KSZTAŁTU,
  więc przy dwóch szóstkach w kadrze sam wybiera, która dokąd leci. Stąd szóstka z `60\,000`
  w liczniku ułamka zamiast w mianowniku. Zad. 4, które Henrich uznał za wzorowe, jako jedyne
  miało pary wypisane ręcznie.

- **`manimations/_wspolne.py`** (nowy) — wspólne klocki: `ustaw_kroki` (wspólna skala),
  `rozbij_ulamek` (licznik/kreska/mianownik wyłuskane po współrzędnej y, bo manim nie obiecuje
  kolejności glifów `\frac`), `zapal` (podświetlenie JAKO animacja, żeby pierwsza klatka kroku
  była jeszcze czysta), `zakoncz_krok` i `rozjasnij_scene` (gaszenie koloru przed przytrzymaniem).

- **`tools/styk-klatek.sh`** (nowy) — porównuje ostatnią klatkę kroku N z pierwszą klatką
  kroku N+1 (ffmpeg + SSIM, próg 0,999). To jest maszynowe pilnowanie zasady ciągłości.
  Przy pierwszym uruchomieniu znalazł dokładnie to, co zgłosił Henrich (zad. 3: 2→3, 4→5, 6→7),
  plus niezgłoszone: zad. 2 (2→3), 4 (2→3), 7 (5→6), 8 (1→2, 2→3), 9 (7→8).

- **`tools/wgraj-kroki.sh`** (nowy) — cztery kroki workflow z README (render → kopia → rewersy
  → sprawdzenie styków) jednym poleceniem. Ważny szczegół: rewersy przelicza z `--nadpisz`,
  bo po przerenderowaniu sceny stare pliki `stepNreverse.mp4` pokazują POPRZEDNIĄ wersję
  animacji, a zwykłe `rewersy.sh` po cichu je pomija.

- **zad. 5 od nowa** — każda para „skąd → dokąd" wypisana wprost. 60 000 zjeżdża pod kreskę,
  \((1+p)^2\) przesuwa się w lewo, kropka mnożenia znika. Kolor już tylko na tym, co się rusza.

- **zad. 6 od nowa** — ułamki trzymane jako osobne mobiekty, żeby dało się przenieść licznik
  pod kreskę i odwrotnie (krok 3, odwracanie ułamka). **Skracanie rozbite na dwa kroki**
  (najpierw \((x+1)\), potem \(x\) z \(x^2\)) — w jednym działy się cztery rzeczy naraz.
  Kroków jest przez to siedem, nie sześć; `exercises.json` i opisy zaktualizowane.
  Skracane czynniki są najpierw przekreślane na czerwono, tak jak na kartce.

- **zad. 3** — dodane rozjaśnienie na końcu kroków 2, 4 i 6. Pułapka: samo pomalowanie
  następnego kroku na czarno nic nie dawało, bo w kadrze siedzą kawałki kroku POPRZEDNIEGO
  przekształcone w cel, a `Transform` interpoluje do koloru celu. Trzeba animować obiekt,
  który jest na ekranie.

- **Zostało do zrobienia:** zad. 2, 4, 7, 8 i 9 (ta sama metoda, więc te same wątpliwości),
  oraz szary nawias domykający na końcu kroku 6 zad. 3.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Opisy kroków (pole `text`) przepisane w zad. 1–9
plus spisanie zasad, wedle których mają powstawać. v29 Beta.

- **Zasady od Henricha, spisane w `manimations/README.md`** (dwie nowe sekcje: „Jak ma
  wyglądać animacja" i „Jak pisać opisy kroków"), z jednozdaniowym odnośnikiem w CLAUDE.md.
  Cztery reguły dla opisów: nie opisuj słowami tego, co widać na filmie; tłumacz po chłopsku,
  nie językiem podręcznika; krótkie linijki i wzór w osobnym wierszu; **żadnych myślników
  ani podkreśleń poza wzorami**, bo mylą się z minusem (Henrich: „za minus myli się
  z myślnikiem"). Trzy reguły dla animacji zapisane przy okazji, do wykonania w następnej
  paczce.

- **51 opisów przepisanych** w zad. 1–9. Wzorcem był przykład Henricha z zad. 1 krok 2:
  zamiast „wyrażenie w środku jest równe 7 albo \(-7\)" pokazane na liczbach, co ta wartość
  bezwzględna właściwie robi, i dopiero z tego dwa przypadki.

- **Podmiana surowym tekstem, nie `json.dump`** — diff to dokładnie 51 zmienionych linii przy
  ~5 tys. linii pliku. Skrypt szukał starej wartości przez `json.dumps(stary)`, sprawdzał, że
  występuje dokładnie raz, i na końcu parsował plik z powrotem. (Poprzednim razem `json.dump`
  przeformatował 800+ linii i trzeba było cofać.)

- **Weryfikacja:** wszystkie 87 wzorów z opisów przepuszczone przez wersję KaTeX z `vendor/`
  z `throwOnError: true`; ten sam skrypt szukał myślników i podkreśleń poza wzorami. Zrzuty
  rozwiniętego ROW 3 na 390 px dla trzech najdłuższych opisów: `scrollWidth` równy szerokości
  okna, czyli nic nie rozpycha strony (`.katex-display` ma własny `overflow-x`). Przy okazji
  poprawione `|-7|`, gdzie KaTeX robił z minusa znak dwuargumentowy i wstawiał odstępy —
  `\left|-7\right|`.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Odtwarzacz krok po kroku — trzy poprawki z listy
DO ZROBIENIA Henricha. v28 Beta.

- **Głowica zostaje na początku obejrzanego filmu** (`biezacaKropka` w app/steps.js). Było:
  po `ended` kropka przeskakiwała na `krok + 1`, czyli na koniec obejrzanego odcinka.
  Jest: zawsze lewa kropka odcinka, tak samo jak przy cofce. Jedyny wyjątek to koniec
  OSTATNIEGO kroku — tam nie ma już następnego filmu, więc głowica idzie na ostatnią kropkę
  (decyzja Henricha po moim pytaniu: „kropka zmienia się na dużą dopiero po dotarciu do
  ostatniej klatki"). Wypełnienie odcinka zostaje pełne, bo pisze je `rysujPostep` z `uKonca`,
  nie z położenia głowicy.

- **► w trakcie cofki tylko odwraca kierunek** (`krokDalej`). Było: przeskok do następnego
  kroku, czyli krok, który się właśnie oglądało od tyłu, wypadał. Jest: przeładowanie tego
  samego kroku w przód na pozycji, do której doszedł rewers, i granie dalej — jednym
  kliknięciem to, co wcześniej wymagało pauzy i play. Wyjątek z v25 (skończona cofka → ten
  sam krok od pierwszej klatki) wypada z tego SAM, bo pozycja wynosi wtedy 0; osobna gałąź
  `naPoczatkuPoCofce` w `krokDalej` przestała być potrzebna.

- **Trzy stopnie kontrastu na pasku** (style/sheet.css). Było: przerobione i bieżący odcinek
  malowane tym samym `--text`. Jest: pusty `--border-muted` → przerobiony `--text-faint` →
  bieżący `--text`. Henrich: „obecna linia ma być bardziej uwydatniona, bardziej kontrastowa"
  (mówił w kontekście ciemnego motywu, w jasnym wychodzi to odwrotnie kolorystycznie —
  tokeny załatwiają to same).

- **Test najpierw czerwony.** Do `tools/test-krokow.js` doszły: niezmiennik położenia dużej
  kropki (sprawdzany po każdym losowym ruchu) oraz dwa zachowania deterministyczne
  (kropka po dograniu kroku do końca, ► w trakcie trwającej cofki — z porównaniem czasu
  w skali kroku, tolerancja 1,2 s). Na kodzie sprzed poprawki wszystkie trzy padają
  i odtwarzają dokładnie zgłoszenie Henricha; po poprawce: zad. 1–4 × 3 ziarna na szybkim
  serwerze i zad. 1 i 4 na dławionym (250 ms, 80 kB/s) — bez zastrzeżeń.

- Wygląd paska sprawdzony zrzutem w obu motywach.

[SPRAWDZONE 2026-08-12] (Local Opus 5 High) Checklista kontenera z 2026-08-10 (firewall +
Playwright + read-only `.vscode`) — odpalona z wnętrza kontenera, wszystko przechodzi, więc
punkt znika z TESTOWANIE HENRICH. `dig +short github.com` zwraca adresy; `curl` na 192.168.1.1
nie przechodzi; `curl -sI https://cke.gov.pl` daje 200; `npm ping` odpowiada; `git push` działał
w tej sesji; `verify-firewall.sh` kończy się sukcesem; `findmnt` na `.vscode` pokazuje `ro`;
Chromium z Playwrighta startuje. Henrich robił Rebuild Container tego samego dnia.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Rozwiązania krok po kroku do zad. 5, 7 i 9. v27 Beta. Po tej paczce kroki mają zadania **1–9**, czyli komplet od początku arkusza.

- Trzy zadania dobrane pod tę formę animacji i z trzech różnych działów:
  - **zad. 5** (procent składany), 6 kroków: podstawienie do \(P_0(1+p)^n\) → dzielenie obu
    stron → policzony ułamek → pierwiastek (z uzasadnieniem, czemu tylko dodatni) →
    odjęcie jedynki → zamiana na procent.
  - **zad. 7** (układ z parametrami), 7 kroków: oba równania jadą **równolegle, jedno pod
    drugim** przez cały film — sedno tego zadania jest takie, że nie ma tu układu do
    rozwiązywania, tylko dwa niezależne równania z jedną niewiadomą każde. Osobny krok na
    samo wstawienie do \(a\cdot b\), bo tam ludzie gubią punkt, odpowiadając wartością \(a\).
  - **zad. 9** (nierówność kwadratowa, OTWARTE na 2 pkt), 8 kroków pod klucz CKE: postać
    z zerem po prawej, wyróżnik (z ostrzeżeniem o znaku \(c\)), miejsca zerowe = 1 pkt,
    zapis przedziału = 1 pkt.

- **Świadomy podział pracy w zad. 9:** film robi sam rachunek i NIE rysuje paraboli, bo
  zadanie ma już widżet `widgetNierownoscKwadratowa`, który pokazuje wykres interaktywnie
  tuż pod odtwarzaczem. Sprawdzone zrzutem — jedno uzupełnia drugie, zamiast dublować.

- Scenariusze najpierw jako `.md` do sprawdzenia merytoryki (`zad5-kroki.md`, `zad7-kroki.md`,
  `zad9-kroki.md`), z tabelką „kryterium z klucza → krok" tam, gdzie zadanie jest otwarte.
  `\begin{cases}` renderuje się w Manimie bez dodatków.

- `tools/test-krokow.js` na wszystkich trzech: bez zastrzeżeń.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Odtwarzacz krok po kroku: koniec cofki, zawieszanie przy klikaniu w kropkę, pobieranie filmów z góry. v26 Beta. Trzy punkty zgłoszone przez Henricha.

- **Koniec rewersu ≡ pierwsza klatka zwykłego filmu.** Zgłoszenie brzmiało: „końcowa klatka
  video reverse nie reaguje mechanicznie tak samo jak pierwsza klatka zwykłego video".
  Faktycznie: `krokWstecz` sprawdzało samo `ctx.wstecz`, więc po dobiegnięciu cofki ◄ tylko
  doskakiwało na pierwszą klatkę zamiast cofać krok POPRZEDNI, a ► przeskakiwało do
  następnego kroku, zamiast odtworzyć TEN SAM w przód. Doszedł predykat
  `naPoczatkuPoCofce()`; ► w tym stanie deleguje wprost do `przelaczOdtwarzanie()`, więc oba
  przyciski nie mają jak się rozjechać.

- **Zawieszanie po podwójnym kliknięciu w kropkę — moja regresja z v23.** Wydłużyłem wtedy
  strażnik ładowania z 1,5 s na sztywne 8 s. Porzucone przy szybkim klikaniu elementy
  `<video>` nadal wisiały na łączu i zajmowały miejsce w niewielkiej puli jednocześnie
  ładowanych mediów, głodząc ten element, na który odtwarzacz faktycznie czekał. Odtworzone
  na dławionym łączu: **5,6 s** w stanie „ładuję" po czterech kliknięciach w pierwszą kropkę
  zad. 4; po poprawce **1,6 s**, czyli tyle, ile trwa samo pobranie. Dwie zmiany: porzucony
  element jest jawnie zwalniany (`zwolnijWideo` — zdjęcie źródła + `load()`), a strażnik
  liczy teraz BEZRUCH (5 s bez zdarzenia `progress`), a nie łączny czas ładowania.

- **Filmy pobierają się z góry, w tle.** Start, gdy zadanie wjedzie w pole widzenia
  (`IntersectionObserver` na przycisku „Rozwiązanie", zapas 300 px), z wskoczeniem na czoło
  kolejki, gdy rozwiązanie zostanie faktycznie otwarte. Jedna kolejka na całą stronę, po
  jednym pliku naraz, w kolejności zamówionej przez Henricha: najpierw wszystkie filmy
  w przód, potem wszystkie rewersy. Zwykły `fetch`, nie `<video preload>` — chodzi o cache
  przeglądarki, z którego skorzysta dopiero PÓŹNIEJ tworzony element; bufor podgrzewanego
  elementu jest jego prywatny. Wyłączone przy `saveData` i przy łączu 2g. Zastąpiło to
  podgrzewanie samego następnego kroku niczyim elementem `<video>`.

- **Testy tych zachowań są w repo.** `tools/test-krokow.js` dostał blok deterministyczny obok
  losowego: koniec cofki + ◄, koniec cofki + ►, seria kliknięć w kropkę z limitem czasu
  powrotu do spoczynku. Sprawdzone, że **padają na kodzie sprzed poprawki** (dokładnie te dwa
  komunikaty) i przechodzą po niej. Przy okazji `tools/serwer.js` pozwala teraz cache'ować
  wideo (`max-age=60`), a kodu strony nadal nie — inaczej nie dałoby się przetestować
  pobierania z góry.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Filmy krok po kroku: zad. 1–4 w nowym kadrze, cięcie na kroki zautomatyzowane. v24 Beta.

- **Cięcie sceny na kroki robi teraz sam render.** `manim --save_sections` plus
  `self.next_section("krokN")` w scenie kładzie każdy krok osobnym plikiem. Wcześniej kroki
  przełączało się komentarzem `"""` i renderowało po jednym — dlatego w repo leżały skrypty
  z zakomentowaną większością treści. Przy okazji wyszło, że `solutionZad2.py` w tej postaci
  **nie odtwarzał** wgranych plików (brak przytrzymań `self.wait(0.25)`). Po przepisaniu na
  sekcje sześć kroków zad. 2 wychodzi **identycznych co do piksela** (SSIM 1,000000) z tym,
  co wisi na stronie — to był test całej metody.
  Znika też problem opisany w manimations/README: krok nie musi być samowystarczalny, bo
  scena jedzie w całości i sekcja tylko tnie gotowy materiał.

- **Pułapka złapana SSIM-em:** `self.wait(0.25)` musi iść PRZED `self.clear()`/`self.remove()`.
  Po wyczyszczeniu sceny przytrzymanie trzyma białą planszę — i to ona zostaje na ekranie,
  bo przeglądarka zatrzymuje film kilka klatek przed końcem. Krok 2 zad. 2 wypadał wtedy
  0,9967 zamiast 1,0.

- **Zad. 1 i zad. 3 przerenderowane** ze starego kadru 21:9 (840×360, 60 fps) na 1280×720
  @120. Treść przekształceń bez zmian — zestawione klatka po klatce z poprzednimi plikami.
  Doszło wspólne skalowanie kroków pod węższy kadr (jeden współczynnik z najszerszego kroku,
  jak w zad. 2) i w zad. 3 wyjęcie wzorów pomocniczych z filmu na stronę, zgodnie z zasadą
  z 2026-08-11. Rewersy przeliczone `tools/rewersy.sh --nadpisz`.

- **Zad. 3 dostało opisy wszystkich ośmiu kroków** (miało jeden, przy ostatnim) — punkt
  z TODO „opisy w zad3 uzupełnimy potem".

- **Zad. 4 (logarytmy) zrobione od zera**: scenariusz najpierw w `manimations/zad4-kroki.md`
  (LaTeX-em, do czytania w podglądzie — Henrich zatwierdził przed pisaniem kodu), potem scena,
  render, rewersy i wpięcie w exercises.json. Cztery kroki: wciągnięcie szóstki jako wykładnika,
  suma logarytmów → logarytm iloczynu, opuszczenie kropki mnożenia.

- **Sprawdzone w przeglądarce:** `tools/test-krokow.js` na wszystkich czterech zadaniach
  (losowe klikanie + niezmienniki) — bez zastrzeżeń.

- **Dwa dodatkowe zadania (v25), wybrane przeze mnie jako najlepiej pasujące do tej formy
  animacji — czyste łańcuchy przekształceń:**
  - **zad. 6** (dzielenie wyrażeń wymiernych), 6 kroków: rozkład \(x^2-1\) ze wzoru
    skróconego mnożenia → dzielenie na mnożenie przez odwrotność → skrócenie \((x+1)\) i \(x\)
    → połączenie ułamków → wymnożony mianownik.
  - **zad. 8** (równanie wymierne, OTWARTE na 3 pkt), 7 kroków ułożonych pod klucz CKE:
    każde kryterium z klucza ma swój krok, a założenie \(x\ne1\) dostaje własny krok i zostaje
    pod równaniem do końca — bo to za nie jest osobny punkt.
  - Scenariusze najpierw w `manimations/zad6-kroki.md` i `zad8-kroki.md`, tak jak przy zad. 4.
  - Przejścia robi `TransformMatchingShapes`, a nie ręczne mapowanie indeksów glifów:
    przy ułamkach zmieniających budowę (rosnące kreski, pojawiające się nawiasy) mapowanie
    indeksów jest bardzo kruche, a tu wystarczy, żeby te same symbole przejechały na miejsce.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Odtwarzacz krok po kroku — wielokrotne cofanie i odtwarzanie przy słabym łączu. v23 Beta.

- **Jedna przyczyna pod obydwoma objawami z TODO.** Podmiana kroku TRWA: `pokazKrok()` ustawia
  `ctx.krok`/`ctx.wstecz` w chwili kliknięcia, ale nowy film musi jeszcze przyjść z sieci —
  i przez cały ten czas w kadrze siedzi **poprzedni** krok. Każdy element sterowania czytał go
  przez `querySelector("video")` tak, jakby należał do nowego stanu. Zmierzone Playwrightem na
  serwerze dławionym do 60 kB/s (skrypty w scratchpadzie sesji, serwer z obsługą `Range`):
  kropki i licznik uciekały o kilka kroków przed obrazem (licznik „6 / 9" przy widocznym
  `step2.mp4`), pasek postępu nowego odcinka rysował się z `currentTime` starego filmu, „play"
  pauzował film, który za sekundę znikał, i zostawiał przychodzący krok zatrzymany na zerowej
  klatce, a ◄ podejmował decyzje na podstawie pozycji w zupełnie innym kroku.

- **Naprawa: drugi licznik.** `swapToken` to podmiana ZAMÓWIONA, `tokenNaEkranie` — POKAZANA,
  a różnica między nimi (`wPodmianie()`) znaczy „krok się jeszcze ładuje". Wtedy
  `biezaceWideo()` zwraca `null` (przez nie idzie już całe sterowanie), `pozycjaWKroku()` zwraca
  pozycję zamówioną zamiast czasu obcego filmu (`Infinity` = „koniec kroku, długości jeszcze nie
  znamy" — tak startuje cofka całego poprzedniego kroku), a zamiar grania siedzi w
  `ctx.grajPoPodmianie`, więc play/pauza w trakcie ładowania **odwraca zamiar**, zamiast ruszać
  skazany element.

- **Strażnik 1,5 s → 8 s + obsługa `error`.** Stary limit przy wolnym łączu wpuszczał do kadru
  element bez ani jednej zdekodowanej klatki: obraz gasł i przychodził drugi raz. Teraz podmiana
  czeka na klatkę, a kończy się wcześniej tylko na błędzie pliku — brak rewersu (nieprzerobiony
  arkusz) ląduje od razu na pierwszej klatce kroku, czyli tam, gdzie cofka i tak by się
  skończyła. Sprawdzone przez chwilowe schowanie `step4reverse.mp4`.

- **Widać, że się ładuje.** Puls tła (`.laduje`) był niewidoczny, gdy w kadrze wisiał poprzedni
  krok — bo tło siedzi ZA filmem. Doszła klasa `.podmiana`, która pulsuje przezroczystością
  samego obrazu, z tą samą zwłoką 200 ms, więc przy szybkim łączu nadal nic nie mruga
  (zmierzone: opacity 1 → 0,47 → 1, klasa znika w chwili wejścia kroku).

- **Czym to sprawdzone.** Test losowy (40 kliknięć ◄/►/play/kropka z losowymi odstępami)
  z niezmiennikami: plik w kadrze musi pasować do licznika, odtwarzacz nie może zostać
  w stanie „ładuję", kadr nie może zostać pusty. 18 przebiegów × 3 prędkości łącza
  (natychmiastowe / 60 kB/s / 12 kB/s) × 3 zadania — zero naruszeń, zero błędów JS.
  Przy okazji odhaczone dwa punkty z TESTOWANIA v22: 10 kropek mieści się na 390 i 360 px bez
  strzałek, a obracanie ekranu w trzech zadaniach nie wywołuje już błędu ResizeObservera.

- **Ustalenie sprzętowe:** Chromium z Playwrighta W TYM kontenerze **odtwarza H.264** — notatka
  z 2026-08-11 o braku kodeka dotyczyła kontenera chmurowego. Filmy mp4 z arkusza da się więc
  testować wprost, bez kopii WebM. Warunek: serwer z obsługą żądań zakresowych.

[ZROBIONE 2026-08-12] (Local Opus 5 High) Odtwarzacz krok po kroku — 5 poprawek po testach v21 + naprawa własnej regresji. v22 Beta.

- **Błąd `ResizeObserver loop completed with undelivered notifications`** — regresja z v21, moja.
  Henrich zobaczył baner na Pixelu 7a i w symulacji Pixela 7 (zad. 3). Przyczyna:
  `odswiezStrzalkiKropek()` mierzyło dostępne miejsce, **chowając najpierw strzałki** — a te
  siedzą w tym samym wierszu co okno kropek, więc każdy pomiar zmieniał układ i budził
  obserwatora od nowa; zapis szedł w dodatku wprost z jego uchwytu. Teraz pomiar niczego nie
  przestawia (porównanie „ile kropki chcą" z szerokością całego wiersza, niezależną od
  strzałek), zapis idzie tylko przy realnej zmianie stanu i jest odłożony do najbliższej klatki,
  a obserwowany jest wiersz, nie okno.
  **Metodycznie ważne:** pierwsza wersja testu pokazywała „0 błędów" także na WADLIWYM kodzie,
  więc nic nie dowodziła. Ten błąd trzeba łapać tak, jak łapie go strona — zdarzeniem `error`
  na `window`, nie `pageerror` Playwrighta. Po poprawieniu testu: stary kod 2 błędy + ten sam
  baner co u Henricha, nowy zero.

- **Przycisk ◄ ma trzy zachowania** zależne od stanu filmu. Doszło brakujące trzecie: wciśnięty
  gdy film już się cofa, doskakuje na pierwszą klatkę kroku i staje (wcześniej startował rewers
  od nowego miejsca i obraz się zacinał). Pokazywany jest wtedy plik w przód na czasie zero — ta
  sama klatka co koniec rewersu, ale stan, z którego start/pauza rusza naturalnie naprzód.

- **Pasek kropek mieści więcej kropek**: szerokość 80% → 96%, ale odzyskane miejsce poszło
  w kropki, nie w rozciągnięcie (padding kropki 8→5 px, odcinki 18/14→14/10, strzałki 32→24,
  gap 4→2). Wyszło lepiej, niż zakładałem: zad. 1 z dziesięcioma kropkami mieści się w całości
  na telefonie 390 px, więc przewijanie w ogóle się nie włącza. Pionowy padding kropki nietknięty
  — to on daje 44 px wysokości pola dotyku.

- **ROW 3 wyśrodkowany**, rozwinięty tekst zostaje wyrównany do lewej (to akapit do czytania)
  i dostaje na telefonie własny padding — jechał razem z filmem poza padding podokna i kleił się
  do krawędzi ekranu.

- **Podokna bliżej krawędzi na telefonie**: boczne wcięcie karty 16→10 px, padding podokien
  20/22→12 px, ujemny margines filmu −20→−12 px, żeby sięgał dokładnie krawędzi karty. Zmierzone
  na 390 px: ramka 18 px od krawędzi zamiast 25.

- **Puls tła w miejscu kadru na czas ładowania.** Czysty CSS, bez dodatkowego elementu i bez
  skryptu. Zwłoka 200 ms zrobiona `animation-delay` przy starcie z przezroczystości, więc przy
  szybkim łączu nic nie mrugnie; `prefers-reduced-motion` zostawia samo statyczne tło. Klasa
  `.laduje` siada **tylko gdy kadr jest pusty** — przy zmianie kroku podwójny bufor trzyma na
  ekranie poprzedni film i puls migałby nad gotowym obrazem.

- Uwaga do historii: pierwsze podejście do commitów wrzuciło trzy tematy do commita opisującego
  jeden (`git add app/steps.js` bierze cały plik). Poprawione przed pushem — commity zostały
  rozbite tak, żeby opis zgadzał się z zawartością.


[ZROBIONE 2026-08-12] (Henrich — testy) v21 odebrane. Henrich przeklikał całą sekcję TESTOWANIE HENRICH
dla odtwarzacza krok po kroku (arkusz 2024-grudzień, wszystkie trzy zadania z wideo). Potwierdzone jako
działające: skok ► w trakcie odtwarzania, natychmiastowe podświetlenie kropki przy ◄, start/pauza
w trakcie cofania, klik w kropkę (obcą i bieżącą) bez resetu paska, wypełnione odcinki na lewo od głowicy,
węższy pasek kropek i strzałki ‹ › tylko wtedy, gdy trzeba, nowy wygląd przycisków ROW 2 (daszki + jeden
przycisk odtwórz/pauza/restart, bez nakładek na filmie), cykl prędkości 1x → 2x → 4x → 0.25x → 0.5x → 1x
z kropką dziesiętną, zarezerwowane miejsce na kadr (karta nie podskakuje), brak 404 po przenosinach
do `media/zadN/solution-step-by-step/`. Pięć uwag z tych testów NIE jest błędami v21, tylko zamówieniem
kolejnej porcji — wróciły do TODO.md jako „PO TESTACH v21": trzystanowy prev-step „<", szerszy pasek
kropek, wyśrodkowany przycisk „pokaż wyjaśnienie kroku" + margines tekstu na telefonie, węższe wcięcia
podokien na telefonie, animacja ładowania filmu po ~200 ms.  [krok-po-kroku, wideo, ui, testy, odbior]

[ZROBIONE 2026-08-11] (Local Opus 5 High) Odtwarzacz krok po kroku — 15 poprawek po testach v20. v21 Beta.
Zamknięta cała sekcja „Usprawnić Rozwiązanie krok po kroku, Ocena po testach" z TODO.md plus prośba
o zmianę nazwy podkatalogu. Testowane w Chromium DEVKONTENERA na prawdziwych plikach mp4 — w odróżnieniu
od sesji chmurowej, gdzie Chromium nie miał H.264 i trzeba było robić kopie WebM.

- **Pasek zostawał w miejscu ostatnio odtwarzanym** (punkt, który Henrich zgłosił jako „wciąż nierozwiązany
  bug"). Reprodukcja pomiarem: klik w kropkę 3 podczas odtwarzania kroku 1 przenosił film poprawnie na
  step4.mp4 / t=0, ale odcinek nr 3 pokazywał **55%** — pozycję STAREGO filmu. Przyczyna: pętla postępu
  poprzedniego `<video>` czyta `ctx.krok` w chwili rysowania, a `video.isConnected` jej nie zatrzymuje, bo
  stary element siedzi w DOM aż do `replaceChildren`. Każdy element dostaje teraz pieczątkę `swapToken`
  i milknie, gdy przestaje być bieżący. Dotyczyło to też uchwytów play/pause/ended.

- **Kropka początku kroku podświetla się od razu przy ◄**, nie po dojechaniu cofki (`uKonca` gaszone
  w chwili kliknięcia). To odwraca decyzję z v20, gdzie głowica czekała na koniec rewersu — rysunek ROW 1
  w TODO.md dopuszczał obie lektury, a testy rozstrzygnęły na rzecz tej.

- **► pomija krok także w trakcie odtwarzania.** Wcześniej klik w trakcie nie robił nic (wołał `play()`
  na już grającym filmie). Początek kroku k+1 to ta sama klatka co koniec kroku k, więc pomijana jest
  wyłącznie animacja, nie kawałek rozwiązania.

- **Start/pauza nigdy nie odpala rewersu**: w trakcie cofania pierwszy klik zatrzymuje je w miejscu,
  dopiero drugi rusza stamtąd do przodu. Klik w kropkę, na której już stoimy, puszcza jej krok.
  Odcinki na lewo od głowicy są wypełnione w całości.

- **ROW 2 na inline SVG.** Glify tekstowe siedziały krzywo w polu przycisku i różniły się kształtem
  między przeglądarkami; pauza wychodziła kwadratem. Zaokrąglone daszki dla kroków, pełny trójkąt dla
  odtwarzania — sam kształt je rozróżnia, więc obwódka wokół środkowego przycisku (dodana w v20 właśnie
  po to, żeby ▶ nie mylił się z ►) mogła zniknąć. Środkowy przycisk ma trzy stany w jednym: odtwórz /
  pauza / odtwórz ponownie, przy czym restart pojawia się wyłącznie po filmie odtworzonym W PRZÓD.
  Nakładane na film ikonki pauzy i restartu usunięte.

- **Strzałki przewijania kropek liczone z faktycznego przepełnienia**, nie z liczby kropek (>7): zad. 3
  ma dziewięć kropek, które na komputerze mieszczą się bez reszty, a strzałki i tak wisiały. Pomiar robimy
  przy schowanych strzałkach, żeby nie zjadał własnego efektu, i powtarzamy przez `ResizeObserver`.

- **Kadr rezerwowany przed wczytaniem filmu** (`aspect-ratio` na `.steps-content`, do czasu poznania
  metadanych 16/9). Zmierzone przy sztucznie opóźnionych plikach: 608×342 już wtedy, gdy elementu
  `<video>` jeszcze w ogóle nie ma, więc karta nie podskakuje.

- **Prędkość**: „Prędkość filmów" → „Prędkość animacji", klik ZWIĘKSZA (`data-kierunek="prawo"` — domyślny
  kierunek w tym panelu ujmuje, bo pozostałe ustawienia mają stan domyślny na prawym końcu skali).
  Wartości dziesiętnie z KROPKĄ: `data-stany` rozdziela stany przecinkiem, więc „0,25×" rozpadłoby się
  na dwa stany.

- **ROW 3** przestał się rozciągać na całą szerokość — przycisk jest szeroki na tyle, ile zajmuje napis
  ze strzałką (znika pusty pas między nimi), z większym marginesem nad i pod i tekstem odsuniętym od tytułu.

- **Katalog `media/zadN/krok-po-kroku/` → `media/zadN/solution-step-by-step/`** (23 ścieżki w danych plus
  skrypt, komentarze i dokumentacja). Świadomie NIE ruszone nazwy plików z tym samym członem —
  `issues/krok-po-kroku-produkcja.md`, `issues/krok-po-kroku-v20-testy.md` i spec projektowy — bo to
  dokumenty, do których prowadzi mnóstwo odnośników, a nie ścieżki katalogu.

- Zarzut „podpis pod filmem na telefonie ma za wąskie marginesy" odpadł sam: w v20 podpisu już nie ma,
  opis kroku siedzi w ROW 3. Zmierzone na 390 px — treść zadania ma 24 px marginesu, film i ROW 3 po 25 px.


[ODEBRANE 2026-08-11] (Henrich, testy ręczne) Paczka drobiazgów UI v15 — 3 z 5 punktów odebrane
bez uwag: (1) panel boczny bez hoverowego podglądu wartości („zajebiście jest"), (4) „Sprawdź
wszystkie odpowiedzi" jako podpunkt pod „Poprawność" („bardzo dobrze"), (5) pigułki kategorii
po dwie w rzędzie na telefonie („bardzo dobrze"). Dwa pozostałe wróciły do TODO.md:
(2) kontrolki pod treścią zdania — czytelniej, ale brak odstępu między kolejnymi zdaniami 1/2/3…;
(3) odwracanie kolorów grafik w dark mode — OK w Firefoksie (desktop+telefon) i Chrome na
telefonie, prostokąt jaśniejszy od tła w Chrome/Brave na desktopie, całkiem nieczynne
w Samsung Internet (własny wymuszony dark mode). Rozpoznanie: issues/dark-mode-inwersja-przegladarki.md
[ui, dark-mode, mobile, odbior]

[ZROBIONE 2026-08-11] (Cloud Opus 5 High) Odtwarzacz „krok po kroku" przebudowany w całości — v20 Beta.
Zamknięte całą sekcją „Rozwiązanie krok po kroku" z TODO.md wraz z blokiem „Z SESJI 2026-08-11" i trzema
pytaniami, na które Henrich odpowiedział w tym samym pliku. Projekt: `docs/superpowers/specs/2026-08-11-rozwiazania-krok-po-kroku-design.md`.

- **Rewersy i nowe nazewnictwo.** Pliki przeniesione z `media/zadN/zadNrozw_stepM.mp4` do
  `media/zadN/solution-step-by-step/stepM.mp4`, obok każdego `stepMreverse.mp4`. Objęte wszystkie trzy
  zadania z krokami: zad. 1 (9), zad. 2 (6), zad. 3 (8) — razem 23 kroki i 23 rewersy.
  Rewers robi ffmpeg z gotowego pliku (nie Manim), z `tpad` doklejającym 0,25 s bezruchu na KOŃCU —
  bez tego przytrzymanie stanu końcowego ląduje na początku cofki, a rewers kończy się klatką,
  której przeglądarka nie zdąży namalować. Odtwarza to `tools/rewersy.sh`.
  Zweryfikowane pomiarem: liczba klatek zgadza się co do sztuki (+15 przy 60 fps, +30 przy 120),
  a SSIM końca kroku wobec startu rewersu i odwrotnie ≥ 0,9994 na wszystkich 23 krokach.

- **Model interfejsu: kropka = STAN, film = PRZEJŚCIE**, stąd kropek jest o jedną więcej niż filmów.
  Głowica stoi na kropce, na której naprawdę jesteśmy — na lewej, dopóki film leci, na prawej po
  dobiegnięciu; w rewersie tak samo, tylko w drugą stronę. **Rysunek ROW 1 w TODO.md sam sobie
  przeczy** („po skończeniu 3. kroku" ma pełny pasek po prawej od O, „po obejrzeniu całości" po
  lewej) — przyjąłem wariant bez wyjątku (O przeskakuje po dobiegnięciu filmu) i wypisałem to
  do potwierdzenia w sekcji TESTOWANIE HENRICH.

- **ROW 1** kropki w trzech stanach, klikalne (skok do pierwszej klatki kroku, film zatrzymany),
  ostatnia kropka = stan końcowy. Pasek postępu przeniesiony spod filmu w odstęp między kropką
  bieżącą a następną; pętla `requestAnimationFrame` chodzi tylko w trakcie odtwarzania i sama się
  kończy. Powyżej siedmiu kropek pasek przewija się w poziomie strzałkami po bokach — poziomy
  padding musiał zejść do zera, bo przy dokładnie siedmiu dokładał 8 px i przewijanie włączało się
  o jedną kropkę za wcześnie. **ROW 2** ◄ / start-pauza / ►, pole dotyku 44×44; start-pauza dostał
  obwódkę, bo inaczej ▶ i ► to dwa prawie identyczne trójkąty obok siebie. **ROW 3** zwijane
  „Pokaż/Schowaj wyjaśnienie kroku" zajęło miejsce pola `text` — zgodnie z odpowiedzią Henricha
  pod filmem nie został żaden zawsze widoczny podpis.

- **Cofanie ◄** odtwarza `stepMreverse.mp4` od klatki odpowiadającej bieżącej pozycji (czas t w
  wersji w przód = `dlugoscPrzod - t` w rewersie) i zatrzymuje się na początku kroku; kliknięte już
  na pierwszej klatce cofa cały poprzedni krok. Z kropki 0 nie cofa nic. Do tego przesuwanie palcem,
  klawiatura ← → (działa na odtwarzaczu ostatnio dotykanym — arkusz ma wiele zadań) i prędkość
  0,25×–4× w panelu bocznym, z etykietami ułamkowymi, bo `data-stany` rozdziela stany przecinkiem.

- **Zdjęte:** `markCorrectAnswer` przy ostatnim kroku (Henrich uznał za mylące) i podpis pod filmem.
  Licznik „3 / 6" został, ale niewidoczny — czyta go `krokRozwiazania()` w `app/report.js`.

- **Dwa formaty naraz.** Zad. 1 i 3 mają filmy wciąż w 21:9 (840×360, 60 fps), zad. 2 już w 16:9.
  Kadr bierze proporcje z pliku (`--proporcje-filmu` z `videoWidth/videoHeight`), więc martwy pas
  nad i pod starymi filmami spadł z 81 px do 0. Przerobienie samych scen zad. 1 i 3 zostaje otwarte.

- **Błąd złapany odczytem pikseli, nie zrzutem ekranu:** kliknięcie ostatniej kropki pokazywało
  PIERWSZĄ klatkę ostatniego kroku (3354 ciemne piksele w prostokącie 466,310,813,409) zamiast stanu
  końcowego (1557 w 594,309,685,410). Przewinięcie zamawiane na odłączonym elemencie nie zdążało
  przed awaryjnym `setTimeout`, więc czas jest teraz egzekwowany ponownie po wstawieniu do DOM.
  Po poprawce klatka zgadza się z plikiem co do prostokąta we wszystkich trzech zadaniach.

- **Pułapka narzędziowa, która wyglądała jak błąd w kodzie:** `python3 -m http.server` nie obsługuje
  żądań zakresowych, więc `video.seekable` zostaje puste i każde ustawienie `currentTime` cicho wraca
  do zera. Dopisane do CLAUDE.md i `issues/krok-po-kroku-produkcja.md`.

[ZROBIONE 2026-08-11] (Cloud Opus 5 High) Ręcznie wymuszony ciemny motyw odwraca wreszcie rysunki i filmy.
`html.theme-dark` nie miał `--filtr-grafik-zadan`, choć blok systemowy (`@media prefers-color-scheme: dark`)
ma go od początku, a komentarz nad obiema paletami mówi, że są identyczne. Skutek: ciemny WYBRANY PRZEZ
SYSTEM przygaszał białe PNG/MP4 poprawnie, a ten sam motyw WYMUSZONY RĘCZNIE zostawiał je świecące na biało.
Zmierzone w Chromium: `getComputedStyle(video).filter` dawało `none` przy `html.theme-dark` i `invert(0.92)`
przy motywie systemowym; po poprawce oba dają `invert(0.92)`. Znalezione przy przebudowie odtwarzacza —
to prawdopodobny powód, dla którego punkt o świecącym wideo z paczki v15 mógł wyglądać na niezrobiony.

[ZROBIONE 2026-08-11] (Local Opus 5 Medium) Zadanie 2 przerenderowane w całości w kontenerze — v16 Beta.
Pierwsze użycie pipeline'u do prawdziwej pracy, nie do testu. Wszystkie 6 kroków (`zad2rozw_step1..6.mp4`)
podmienione na rendery kontenerowe; stare pliki usunięte.

- **Naprawiony błąd 5⁻⁴ w kroku 6** (pozycja z „DLA HENRICHA"): `manimations/solutionZad2.py` linia 45,
  `MathTex(r" 5^{-4}")` → `5^{4}`. Sprawdzona klatka końcowa nowego pliku — pokazuje 5⁴. Z podpisu
  w `exercises.json` usunięte nieaktualne już sprostowanie „(na końcu filmu błędny zapis \(5^{-4}\))".
- **Zgodność z poprzednimi plikami**: każdy z 6 kroków ma identyczne wymiary, czas i liczbę klatek
  (840×360, 60 fps; kroki 1–5 po 1,000 s / 60 klatek, krok 6 — 2,000 s / 120 klatek), a SSIM względem
  starych plików wynosi 0,99911–0,99993, czyli tyle, ile wnosi sama kompresja. Nowe pliki są o 15–25%
  lżejsze (inna wersja ffmpega, patrz wpis niżej).
- **Ustalone przy okazji: kroki NIE są samowystarczalne.** Krok 2 wyrenderowany w izolacji wypadł
  SSIM 0,9929 — o rząd wielkości gorzej niż reszta. Nie szum, tylko brak fragmentu obrazu: krok 2
  przekształca wyłącznie `kroki[0][0..2]`, więc domykający nawias z wykładnikiem (`kroki[0][3]`)
  nie trafia na scenę; w oryginalnej procedurze narysował go wcześniej krok 1. Po dodaniu jawnego
  `self.add(kroki[0])` na wejściu — 0,999614. Pozostałe 5 kroków renderuje się w izolacji poprawnie.
  **Konsekwencja dla warstwy 2**: cięcie na sekcje musi pilnować stanu przenoszonego między krokami,
  a nie tylko granic czasowych. Zapisane w `manimations/README.md`.
- Granice kroków odtworzone z bloku komentarza w `solutionZad2.py` (kroki: linie 55-57, 60-76, 80-96,
  99-115, 122-124, 128-133 — krok 4 BEZ końcowego `clear/add/wait`, bo to przygotowanie stanu pod
  krok 5, nie część jego wideo). Potwierdzenie poprawności granic: zgodność czasu i liczby klatek
  ze starymi plikami we wszystkich sześciu przypadkach.

[ZROBIONE 2026-08-11] (Local Opus 5 Medium) Kontener: Manim, paczka 1 — środowisko zweryfikowane.
Spec: `docs/superpowers/specs/2026-08-11-manim-w-kontenerze-design.md` (warstwy 1 i 4). Instalacja
poszła z hosta (`.devcontainer/` jest read-only), weryfikacja renderu z kontenera.

- `manim --version` → `Manim Community v0.18.1`, zgodnie z hostem. Render `solutionZad2.py`
  (`ScenaZadania2`) przechodzi w **14,6 s**, bez błędu LaTeX-a — czyli **minimalny TeX Live
  wystarcza** i `texlive-full` (~5 GB) nie jest potrzebny.
- **Porównanie host ↔ kontener wypadło zgodnie.** Ten sam skrypt vs `zad2rozw_step6.mp4`:
  identyczne parametry pliku (840×360, 60 fps, 120 klatek, 2,000 s, h264 High/yuv420p),
  SSIM średnio 0,999856 (najgorsza klatka 0,999543), a w powiększeniu 4× ta sama geometria
  glifów. Obawa ze spec-a o metryki fontu (MiKTeX vs TeX Live) **się nie potwierdziła**.
  Test izolujący koder (render `--format=png`, bez kompresji, jako trzeci punkt odniesienia,
  klatka 95): sam koder kontenera daje SSIM 0,999601 względem własnego bezstratnego renderu,
  a plik z hosta — 0,999480. Kompresja H.264 wprowadza więc różnicę tego samego rzędu co cała
  różnica host↔kontener i wystarcza do jej wyjaśnienia. **Nie ustalono**, jaka część przypada
  na koder, a jaka na render — brakuje bezstratnych klatek z hosta (referencja istnieje tylko
  jako H.264). Wniosek: kontener nadaje się także do **finalnych** renderów, nie tylko do podglądu.
- **Poprawka do instrukcji z samego spec-a**: komenda weryfikacyjna miała tam `-qh` i była błędna.
  Flaga jakości nadpisuje `pixel_width`/`pixel_height` z `manim.cfg`, więc `-qh` renderuje
  1920×1080 (16:9) zamiast 840×360 (21:9) — inne proporcje kadru niż pliki na stronie, a więc
  materiał nieporównywalny. Poprawna komenda to samo `manim plik.py Scena`. Zapisane w README.
- **Rozwiązana zagadka „cięcia na kroki"** (README miał tu od miesiąca „domysł, niepotwierdzone",
  a spec zostawiał to warstwie 2) — **dla zadania 2**. Odczytane wprost z `solutionZad2.py`:
  żadnego cięcia nie było, kroki 1–5 są zakomentowane jednym blokiem `"""` (linie 54–126),
  aktywny jest krok 6, a wyrenderowany z tego klip ma 2,000 s / 120 klatek, czyli dokładnie tyle
  co `zad2rozw_step6.mp4`. To nie jest martwy kod, tylko ostatni stan ręcznej procedury.
  **Nie uogólniać na pozostałe zadania**: `solutionZad3.py` nie ma ani jednego bloku `"""`,
  a `solutionZad1.py`/`solutionZad4.py` mają, ale nie sprawdzono, czy pełnią tę samą rolę.
- **Znaleziona przyczyna błędu 5⁻⁴ w kroku 6 zad. 2** (pozycja „DLA HENRICHA" w TODO.md):
  `manimations/solutionZad2.py` linia 45, `kroki[5] = MathTex(r" 5^{-4}")` — literówka w samym
  skrypcie, nie w renderze. Poprawka to jeden znak, a scena jest już ustawiona dokładnie na tym
  kroku, więc render naprawionego pliku da gotowy plik bez żadnego dodatkowego cięcia.

- **Wnioski o sposobie pracy** (nie o Manimie) — trzy rzeczy prawdopodobne trafiły do dokumentacji
  jako ustalone: `issues/lekcje-z-sesji.md`, wpis 2026-08-11.


[ZROBIONE 2026-08-10] (Opus 5 High) Kontener, paczka trzech zmian: brama w firewallu zawężona
do samego DNS, `.vscode/` read-only, automatyczny pull przy starcie faktycznie działa.

**1. Firewall — brama tylko 53/udp + 53/tcp** (`.devcontainer/init-firewall.sh`).
Były tam dwie bezwarunkowe reguły (`-A INPUT -s $HOST_IP -j ACCEPT` i `-A OUTPUT -d $HOST_IP`),
czyli WSZYSTKIE porty bramy. Pod pastą bramą jest prawdziwy router, więc skan `192.168.1.1`
z kontenera pokazywał otwarte 80, 443, 445 (SMB) i 631 (IPP) — panel WWW, udziały plików
i drukarka. Zastąpione dwiema regułami OUTPUT na port 53. Ruch zwrotny NIE dostał własnej
reguły: sprawdzone, że łańcuch INPUT ma niżej `ESTABLISHED,RELATED`, a conntrack śledzi także
UDP. TCP obok UDP jest konieczne — odpowiedzi >512 B (flaga TC) wymuszają ponowienie po TCP.
Reguła na 53 w ogóle zostaje tylko jako zabezpieczenie przenośności: pod pastą resolwerem
z `resolv.conf` jest `169.254.1.1` (nie brama), więc te dwie linie są tam martwe — ale gdy
resolwerem jest sam router, są jedyną furtką. Istniejący bezpiecznik (`dig api.github.com` →
przy braku odpowiedzi przywraca ogólną regułę UDP 53 przez `-I`) pilnuje teraz OBU zawężeń
naraz, bo testuje efekt końcowy, a nie to, która reguła przepuściła pakiet.

**2. `.vscode/` montowane readonly** (`.devcontainer/devcontainer.json`), tak jak `.devcontainer/`.
Powód mniej oczywisty niż przy tamtym katalogu: `tasks.json` ma `"runOn": "folderOpen"`, czyli
polecenie powłoki uruchamiane przez VS Code SAMO, bez pytania, przy każdym otwarciu folderu.
Kontener mógłby podmienić `git pull --ff-only` na dowolną komendę i poczekać — a odpali się ona
tam, gdzie folder zostanie otwarty, czyli na hoście, poza izolacją, przy otwarciu repo lokalnie.
Sprzężenie z punktem 3 jest tu istotne: włączenie `task.allowAutomaticTasks` usuwa pytanie, które
było ostatnią barierą, więc te dwie zmiany muszą iść razem.

**3. Automatyczny `git pull` przy starcie faktycznie się odpala.** Zadanie z `runOn: folderOpen`
istniało od 2026-08-07, ale VS Code przy każdym otwarciu pytał „Allow Automatic Tasks in Folder?"
i do czasu odpowiedzi nie pullował. Brakowało `"task.allowAutomaticTasks": "on"` w GLOBALNYCH
(User) ustawieniach — tego przełącznika nie da się ustawić z workspace'u i to jest celowe,
inaczej repo przyznawałoby sobie samo prawo do uruchamiania poleceń. Dopisane w `~/.config/Code/User/
settings.json`. W `tasks.json` został komentarz o tej zależności.

**Przy okazji: skasowane osierocone dane po flatpakowym VS Code** (852 MB w
`~/.var/app/com.visualstudio.code/`). Sam flatpak był już odinstalowany — zostały po nim tylko
dane, ostatnio używane 2026-08-06. Zweryfikowane przed kasowaniem: `flatpak list` nie zna tej
aplikacji; z 14 rozszerzeń tylko 4 nie miały odpowiednika natywnie (GitLens, Containers, gitdoc,
Claude Code — wszystkie wracają z marketplace'u); `History/` zawierało wyłącznie stare wersje
`settings.json` i `.devcontainer/devcontainer.json` (ten drugi i tak jest w gicie);
`workspaceStorage/` dotyczyło tylko tego repo (stan UI, nie treść). Ustawienia, snippety i lista
rozszerzeń zachowane w `~/backup-vscode-flatpak/` (8 kB; Henrich zdecydował 2026-08-10, że tych
ustawień nie potrzebuje, ale backup na razie zostaje). Dwa ustawienia istniały TYLKO we flatpaku
i nie zostały przeniesione: `chat.viewSessions.orientation: "stacked"` i
`chat.agent.sandbox.enabled: "on"`; do tego `terminal.integrated.gpuAcceleration: "off"`, które
natywnie jest zakomentowane. Zostaje jedna instalacja — natywna przez rpm-ostree.

Tego samego dnia skasowane też osiem pozostałych sierot w `~/.var/app` (EasyEffects, Geekbench
i sześć pustych skorup po przeglądarkach, ~328 kB) — zysk symboliczny, ale `~/.var/app` jest
teraz wiarygodną listą zainstalowanych aplikacji: 23 katalogi, zero sierot.

Przepis na powtórkę (jak wykryć sieroty w `~/.var/app`, jak sprawdzić dane przed kasowaniem
i których ustawień NIE przenosić — `flatpak-spawn --host podman` zepsułby natywne devcontenery)
zapisany w **issues/flatpak-osierocone-dane.md**.

Dokumentacja: `.devcontainer/README.md` — sekcja „Brama `/32`, nie `/24`" przepisana na
„Brama: `/24` → `/32` → tylko port 53" (z historią obu zawężeń), sekcja „`.devcontainer/`
tylko do odczytu" rozszerzona o `.vscode/`, w „Czego to NIE chroni" punkt o panelu WWW routera
przekreślony jako nieaktualny i dopisany punkt o DNS jako kanale danych, w „Diagnostyka" trzy
nowe objawy (DNS po zmianie reguł bramy — z komendami i opisem bezpiecznika; brak dostępu do
LAN-u jako zamierzony; brak zapisu do `.devcontainer`/`.vscode`). TODO.md: z punktu o świadomie
niedomkniętych dziurach usunięta część (1) o bramie, część (2) o GitHubie/npm została.

NIEZWERYFIKOWANE W MOMENCIE ZAPISU: zmiany robione z hosta (`.devcontainer/` jest w kontenerze
readonly), a `init-firewall.sh` jest kopiowany do obrazu, więc wszystko wymaga Rebuild Container.
Lista rzeczy do sprawdzenia po przebudowie trafiła do TODO.md → TESTOWANIE HENRICH.

[tagi: devcontainer, firewall, iptables, dns, podman, pasta, bezpieczenstwo, vscode, zadania]

[ZROBIONE 2026-08-09] (Sonnet 5) Test v14 przez Henricha — 2 z 3 punktów potwierdzone bez zastrzeżeń,
trzeci (dynamiczny podgląd hoveru) i pole „ostateczna odpowiedź" przepisane na nowe punkty w
TODO.md → DO ZROBIENIA:
- Hover myszą (tło na chrome, ramka na odpowiedziach ABCD/PF/„N pkt") — Henrich: „jest dobrze".
- Jasny motyw, poprawka kontrastu WCAG drobnych szarych tekstów — Henrich: „jest dobrze".

[ZROBIONE 2026-08-09] (Fable 5) Paczka 4 „Spójność UI, etap 2" — audyt całego style/, v14 Beta.

Zamknięte wszystkie punkty z issues/ui-spojnosc-etap2.md (plik przeniesiony do done/ui-spojnosc-etap2.md):
- **Zasada hoveru** zapisana w komentarzu przy `#naroznik-prawy button:hover` (sheet.css): chrome = podświetlone tło (decyzja Henricha), kontrolki treści = ciemniejsza ramka. Pigułki narożników, strzałka panelu i przełącznik motywu landingu przeszły z ramki na tło.
- **Hover na odpowiedziach** (ABCD/PF/„N pkt") — nowy, ramką `--border-strong`, z `:not(...)` na stany poprawne/błędne/.selected.
- **Skala kontrolek karty zadania** — trzy klasy (duża 18px / kontrolka 17px, 8px 11px / tekstowa 16px) opisane przy banerze „PRZYCISKI ODPOWIEDZI"; ujednolicone paddingi pól fillIn i „ostatecznej odpowiedzi" (6px 8px → 8px 11px) oraz oba przyciski „Sprawdź" (wspólne 15px / 8px 18px).
- **`--shadow-modal`** — nowy token (oba ciemne bloki) zamiast cienia wpisanego na sztywno w oknie podsumowania egzaminu; okno dostało też `--radius-kontrolka` (było ostatnią „kartą" z ostrymi rogami).
- **Ramki 2px → 1px** tam, gdzie grubość nic nie kodowała: `#wskazniki-ukryj` i trzy separatory bloków rozwiązania (`.solution-text/step-by-step/interactive-container`).
- **Landing vs arkusz**: typografia już spójna (lede/CTA 18px = treść zadania; CTA świadomie trzyma wagę w rozmiarze — komentarz z 2026-07-27), zapisana komentarzem przy `.landing-lede`. Kontrast WCAG zmierzony z getComputedStyle w obu motywach: jedyny oblewający był jasny `--text-faint` #858585 (3.7:1 przy 13px) → #767676 (4.54:1); ciemny motyw przechodził w całości. Zamyka to też issues/dark-mode-css-zmienne-landing.md (punkty --border-close/--bg-hover naprawione już wcześniej, plik usunięty).
- Punkty rozstrzygnięte decyzjami Henricha, bez zmian w kodzie: karta zadania bez ramki/zaokrągleń, marginesy w obecnych proporcjach.
Weryfikacja: komplet 16 zrzutów przed/po + ujęcia celowane (podsumowanie egzaminu, pola zadań otwartych, hovery, separatory) + liczbowo przez getComputedStyle. ARCHITECTURE_CSS.md zaktualizowany (sekcja „Shape tokens": zasada hoveru, --shadow-modal, skala kontrolek).

[tagi: css, ui, tokeny, hover, wcag, kontrast, landing, egzamin, spojnosc]

[ZROBIONE 2026-08-09] (Opus 5 Medium) Fałszywy alarm: blokada scrolla pod panelem bocznym
na Pixelu 7a — to był cache przeglądarki, nie błąd.

Po wypchnięciu v13 Henrich zgłosił, że na Pixelu 7a (GrapheneOS) arkusz nadal przewija się
pod otwartym panelem, mimo że w Chromium i w symulowanym telefonie w Firefoksie blokada
działa. Wpis trafił do TODO.md razem z czterema tropami (visual viewport przy przybliżonej
stronie, próg 1300px liczony z `innerWidth`, brak `touch-action` na `#sidebar-przyciemnienie`,
pokrewieństwo z issues/zadania-nie-renderuja-sie-mobile.md).

**Po odświeżeniu strony na telefonie blokada zadziałała poprawnie** — w symulowanym Firefoksie
również. Żaden z tropów nie okazał się potrzebny; telefon trzymał starą wersję plików.
Punkt usunięty z TODO.md bez żadnej zmiany w kodzie. Mechanizm z v13 zostaje bez poprawek:
`body.blokada-scrolla` (`position: fixed` + zapamiętany `scrollY` w ujemnym `top`), zakładana
poniżej progu 1300px — `app/bootstrap.js`, `style/sheet.css:175`.

**Wniosek na przyszłość, wart zapamiętania przy każdym teście na telefonie:** pierwszy objaw
po wdrożeniu bywa cache'em, nie regresją. Numer wersji przy logo („vN Beta") istnieje dokładnie
po to — zanim ktokolwiek zacznie diagnozować zgłoszenie z telefonu, warto najpierw sprawdzić,
czy w rogu widnieje ta wersja, która zawiera poprawkę. Tu tego kroku zabrakło i kosztowało
to wpis w TODO.md plus cztery hipotezy do zbadania.

Przy okazji tej samej sesji Henrich potwierdził, że **zadania renderują się na Pixelu 7a
poprawnie** — dotyczy to issues/zadania-nie-renderuja-sie-mobile.md, ale że tamta awaria bywała
przerywana, plik zostaje w issues/ do świadomej decyzji Henricha, a nie zamykany przy okazji.

[tagi: mobile, cache, panel-boczny, falszywy-alarm]


[ZROBIONE 2026-08-09] (Opus 5 Medium) Paczka 3 „Kolory i motyw ciemny" + dwie dokładki
z issues/plan-ui-paczki-2026-08.md (wersja v13 Beta):

1. **Tło widżetów w ciemnym = tło strony.** Przyczyną nie był żaden styl widżetu, tylko osobny
   token `--canvas-bg` (`canvas { background-color: var(--canvas-bg) }` w sheet.css): w ciemnym
   miał `#1c1c1c` przy tle strony `#141414`. Ustawiony na `#141414` w OBU blokach ciemnej palety
   w base.css. Zweryfikowane `getComputedStyle`: ciemny `rgb(28,28,28)` → `rgb(20,20,20)` = body;
   jasny bez zmian, potwierdzone liczbowo `rgb(255,255,255)` = body.
2. **Tło formularza zgłoszenia — „coś pomiędzy".** Żaden istniejący token nie pasował
   (`--bg-subtle` #222 zmieniłby też jasny motyw na jaśniejszy), więc nowy `--bg-formularz`:
   jasny `#f7f7f7` (dokładnie jak dotąd, zero zmian), ciemny `#1e1e1e` między tłem strony
   `#141414` a `--bg-muted` `#262626`. `.zglos-blad-okno` czyta ten token.
3. **„Zgłoś błąd pod zadaniem" blokowane w egzaminie** — `zglos-blad-toggle` dopisany do
   `OPCJE_MENU_EGZAMIN` w app/exam.js (linki „zgłoś błąd" i tak znikają w egzaminie razem
   z `.light-button-container`). `enableExamMode()` zamyka dodatkowo otwarty formularz, bo jego
   kotwica właśnie znikała i blok zostawał wiszący. Sprawdzone: w egzaminie `disabled=true`,
   `opacity 0.4`, formularz `display:none`; po zakończeniu egzaminu wraca `disabled=false`.
4. **Otwarty panel boczny nie przewija arkusza pod spodem.** `body.blokada-scrolla`
   (`position: fixed`, sheet.css) + w app/bootstrap.js `zablokujScrollTla()`/`odblokujScrollTla()`
   zapamiętujące pozycję w ujemnym `top` i przywracające ją `scrollTo` — świadomie nie
   `overflow: hidden`, bo na iOS nie działa, i z zapamiętaniem pozycji, bo `position: fixed`
   sam z siebie skacze na górę. Zakładane tylko poniżej progu 1300 px (`sidebarNaklada()`),
   plus handler `resize` zdejmujący blokadę po przekroczeniu progu z otwartym panelem.
   Test (390×780, hasTouch): pozycja 900 → w trakcie `top:-900px`, po zamknięciu znów 900;
   swipe w lewo z paczki 2 nadal zwija panel i zdejmuje blokadę. Panel jest `position: fixed`
   z `overflow-y: auto`, więc reguła go nie dotyczy i scroll w środku zostaje.

[ZROBIONE 2026-08-09] (Opus 5 Medium) Paczka 2 „Panel boczny" z issues/plan-ui-paczki-2026-08.md
(wszystkie pięć punktów, wersja v12 Beta):

1. **„Sprawdź wszystkie odpowiedzi" nie znika i panel nie skacze.** Reguły `display:none` /
   `body.reczne-sprawdzanie #sprawdz-wszystkie` w style/exam.css usunięte; pozycja jest teraz
   stale w panelu, a przy poprawności „natychmiast" tylko `disabled`. Potwierdzone pomiarem:
   `top` sąsiedniej pozycji przed i po przełączeniu = 337.78 px, bez zmiany.
2. **„Poprawność" wyszarzona w egzaminie** — `natychmiastowa-toggle` dopisany do
   `OPCJE_MENU_EGZAMIN` (w egzaminie poprawność jest i tak ukryta, więc przełączanie „kiedy ją
   pokazać" niczego nie zmieniało).
   Mechanizm z punktów 1–2 to jedna funkcja `odswiezBlokadyMenu()` w app/exam.js, która zastąpiła
   `setExamMenuDisabled()`: dwa niezależne powody blokady (egzamin, tryb poprawności) sumują się
   w jednym miejscu, bo przy dwóch osobnych setterach koniec egzaminu odblokowywałby „sprawdź
   wszystkie" niezależnie od trybu poprawności. Funkcja odkłada oryginalny `title` w
   `dataset.titleBazowy`, żeby odblokowanie go nie skasowało. Wołana też z
   `odswiezTrybPoprawnosci()` w app/bootstrap.js. Wygląd `:disabled` przeniesiony z exam.css do
   sheet.css jako `#sidebar button:disabled` (blokada nie jest już tylko egzaminacyjna).
3. **Przełączniki przestały wyglądać na wyłączone**: etykieta wiersza ustawienia
   `--text-faint-2` → `--text-muted` (#909090→#555 / #8c8c8c→#bcbcbc), nieaktywna kropka stanu
   `--border-muted` → `--border-strong`. To warunek konieczny punktów 1–2: „wyszarzone" musi
   teraz znaczyć „wyłączone", a nie „domyślne".
4. **Bleeding/bloom stanów przełącznika**: przyczyną była WAGA, nie kontrast tła. Lora jest
   szeryfowa i mocno kontrastowa; jej odmiana 600 przy 12px zlepiała szeryfy w plamę (najgorzej
   jasny tekst na ciemnym). Zdiagnozowane porównaniem 600/400 × 12/13px w powiększeniu ×5 na
   pojedynczym wierszu. Fix: `.sidebar-ustawienie .wartosc` → `font-weight: 400` przy tym samym
   12px (zero ryzyka dla szerokości wiersza); hierarchię wobec etykiety trzyma teraz kolor
   (--text vs --text-muted) i kropki.
5. **Swipe w lewo zwija panel na telefonie** (app/bootstrap.js). Listenery touchstart/move/
   cancel/end wyłącznie na `#sidebar`, wszystkie `passive: true` i bez `preventDefault()` — gest
   tylko obserwuje dotyk, więc nie może przechwycić ani pionowego scrolla panelu, ani
   przeciągania po treści zadania. Progi: ≥60px w poziomie, ≤45px w pionie, |dx| > 1,5·|dy|,
   ≤700 ms, ≥0,25 px/ms; dotyk zaczęty <24px od prawej krawędzi jest ignorowany (strefa
   systemowego gestu „do przodu"), drugi palec kasuje gest. Przetestowane 7 scenariuszy dotyku
   w Playwright (hasTouch, CDP Input.dispatchTouchEvent): swipe w lewo zwija; scroll pionowy,
   muśnięcie, wolne przeciąganie, ukos, swipe w prawo i start przy prawej krawędzi — nie zwijają.

Weryfikacja: tools/zrzuty.js --przed/--po (16 ujęć) + własne zbliżenia na `#sidebar` i pojedyncze
wiersze w ×4/×5, jasny i ciemny, ćwiczenia i egzamin; osobny test funkcjonalny przejść stanu
(ćwiczenia → egzamin → koniec egzaminu → zmiana poprawności) bez błędów JS.
Płynność gestu na prawdziwym telefonie i odczucie „w sam raz mocne" idą na listę TESTOWANIE HENRICH.
[css, ui, panel-boczny, sidebar, dotyk, gesty, egzamin, kontrast, typografia]

[ZROBIONE 2026-08-09] (Sonnet 5 High) Paczka 1 „Drobnica" z issues/plan-ui-paczki-2026-08.md:
napis „Sprawdź obliczenia" → „Sprawdzanie obliczeń" (render.js + exam.js + template.html +
ARCHITECTURE.md/OVERVIEW.md); pigułka punktowa `.exercise-score` przy każdym zadaniu przysunięta
~40px bliżej treści karty (`right: -120px` → `-80px` w style/sheet.css:586, próg zawijania na
telefon w responsive.css nieruszony — poprawka dotyczy tylko szerokiego ekranu; pierwsza wersja
tego punktu błędnie ruszała `#total-score` w górnym pasku zamiast tego — cofnięte, pasek wrócił
do stanu sprzed paczki); stopka arkusza (template.html) i landing (index.html) dostały linijkę
„© 2026 Henrich2137 · Licencja” (nowe klasy .stopka-copyright / .landing-footer a); row-gap
wiersza przycisków (Podpowiedź/Rozwiązanie/Zgłoś błąd/Pokaż wzory) na telefonie 10px→20px.
Zweryfikowane zrzutami Playwright (jasny/ciemny × desktop/telefon, w tym wariant „0 / 4 pkt")
na template.html i index.html.  [css, ui, stopka, tekst, drobnica]

[ZROBIONE 2026-08-09] (Opus 5) Devcontainer nie wstawał: `mkdir: cannot create directory
'/vscode/vscode-server/bin': Permission denied`. Diagnoza i naprawa, zero zmian w plikach repo.

PRZYCZYNA. Rozszerzenie Dev Containers samo tworzy nazwany wolumen `vscode` montowany pod
`/vscode` (cache serwera VS Code między przebudowami) — nie ma go w `devcontainer.json`, dzieje
się pod spodem. Ten wolumen powstał 2026-08-06 z właścicielem ns-uid 1000 = host uid **525287**,
czyli tak, jakby tworzył go kontener BEZ `--userns=keep-id`. Tymczasem właściwy devcontainer
działa Z keep-id (`remoteUser: node` + `updateRemoteUserUID: false` → rozszerzenie dokłada
`--userns=keep-id` pod podmanem), gdzie `node` = host uid **1000**. Rozjazd uid → brak zapisu
do `/vscode`. Potwierdzone liczbowo: `UidMap ["0:1:1000","1000:0:1","1001:1001:64536"]` —
`1000:0:1` to właśnie keep-id. Dla porównania wolumen `matematykazen-claude-config` był i jest
zdrowy (host uid 1000), bo Dockerfile chownuje `/home/node/.claude`, a podman przy pierwszym
montowaniu robi copy-up i przenosi na wolumen właściciela katalogu z obrazu.

WYZWALACZ. Henrich robił porządki na dysku (`podman prune` i podobne). `system prune -a` nie
kasuje nazwanych wolumenów, ale usunął stary, DZIAŁAJĄCY kontener — a rozszerzenie utworzyło
nowy, który podpiął się pod stary wolumen z 6 sierpnia o niepasującym uid. Poszlaka: ostatni
zapis w `matematykazen-claude-config` to 08-08 16:39, a kontener powstał 09-08 00:51, czyli
najpewniej nigdy poprawnie nie wystartował.

NAPRAWA. `podman rm <kontener>` (zatrzymany kontener w stanie `exited` nadal trzyma referencję
do wolumenu i blokuje `volume rm` — to NIE jest hibernacja), potem `podman volume rm vscode`
(bezpieczne: wolumen miał 0 bajtów, to wyłącznie cache binarki serwera), potem rebuild z VS Code.
Po odtworzeniu wolumen miał już poprawnego właściciela (host uid 1000), a ostatecznie środowisko
wstało po restarcie hosta. Wykluczone po drodze: obraz kontenera (nowy kontener, ten sam poprawny
obraz) oraz SELinux (host `Enforcing`, ale kontener dostaje `--security-opt label=disable`).

CZEGO NIE RUSZAĆ przy przyszłym sprzątaniu: wolumenu `matematykazen-claude-config` (tam siedzi
`.credentials.json` z logowaniem Claude Code, `projects/`, `sessions/`) ani wolumenu `open-webui`
(2,9 GB, obca usługa). `podman volume prune` i `system prune -a --volumes` są NIEBEZPIECZNE —
gdy devcontainer nie działa, jego wolumen liczy się jako nieużywany i leci. Wolumeny usuwać
zawsze imiennie. Gdyby problem wrócił, utwardzenie to `RUN mkdir -p /vscode && chown -R
node:node /vscode` w `.devcontainer/Dockerfile` przed `USER node` (ten sam mechanizm copy-up,
który uratował `/home/node/.claude`); awaryjnie `podman volume create vscode` +
`podman unshare chown 0:0 <mountpoint>` (ns 0 = host 1000 = `node` pod keep-id).
Uwaga na przyszłość: rozszerzenie WZNAWIA istniejący kontener po etykietach
`devcontainer.local_folder` — samo „Reopen in Container" nie tworzy nowego, dopiero `podman rm`.

[ZROBIONE 2026-08-07] (Opus 5 Medium) Konfiguracja narzędzi, zero zmian w kodzie strony:

1. Auto-fetch + auto-pull przy starcie VS Code. `.vscode/settings.json` → `git.autofetch: true`
   (fetch w tle co ~3 min, nic nie scala), `.vscode/tasks.json` → task `git pull --ff-only`
   z `runOn: folderOpen` (pull raz, przy otwarciu folderu). Świadomie natywnym mechanizmem VS Code,
   a NIE przez `gitdoc.pullOnOpen`: gitdoc jest pakietem wszystko-albo-nic, więc włączenie go dla
   samego pull-on-open wróciłoby z auto-commitem i `forcePush` (wyłączonymi celowo 2026-08-01).
   `--ff-only` z założenia — nigdy nie nadpisze lokalnych commitów, przy rozjeździe po prostu nie
   wykona się. Oba pliki śledzone przez gita, więc działa tak samo w kontenerze i poza nim (o to
   chodziło Henrichowi: parytet obu środowisk). Na nowej maszynie VS Code pyta raz „Allow Automatic
   Tasks in Folder?".

2. Plugin superpowers 6.2.0 FAKTYCZNIE zainstalowany (scope `project`). Deklaracja
   `enabledPlugins` w `.claude/settings.json` była poprawna od początku — brakowało samej
   instalacji, `installed_plugins.json` był pusty `{}`, więc żaden z 14 skilli (m.in.
   `brainstorming`) nigdy się nie ładował. Instalacja z oficjalnego marketplace'u Anthropic,
   który przypina SHA `44c9b2d` — sprawdzone u źródła: to ten sam commit co ówczesny HEAD
   `obra/superpowers`, więc przypięcie nic nie kosztuje. Duplikat instalacji w scope `user`
   usunięty (decyzja Henricha: ma działać w tym repo, nie we wszystkich projektach).
   Przy okazji instalator znormalizował końcówki linii w tym pliku CRLF→LF.
   Pułapka na przyszłość, na którą sam się nabrałem: superpowers NIE jest podkatalogiem w cache
   marketplace'u (jego wpis ma źródło typu `url`, klonowane dopiero przy instalacji), więc `ls`
   po `plugins/` i `external_plugins/` fałszywie sugeruje, że pluginu tam nie ma.
   Szczegóły w CLAUDE.md, sekcja „Claude Code — plugins / skills".
   [narzedzia, git, vscode, claude-code, pluginy, skille]

[ZROBIONE 2026-08-06] (Opus 5 Medium) Paczka czterech punktów doprecyzowanych z Sonnetem 2026-08-06
(pliki issues/dark-mode-widzety-kolory.md i issues/zadania-otwarte-redesign.md — oba usunięte):

1. Widżety spójne z motywem. `--canvas-bg` przestało być na sztywno białe (`#fff` → `#1c1c1c` w ciemnym),
   doszedł blok tokenów `--wg-*` (osie, siatka, tekst, trzy klasy linii pomocniczych, punkt, żółty, słupek,
   etykieta info, półprzezroczyste wypełnienia obszarów) w :root i w OBU blokach ciemnych base.css.
   Z plików `widgets/*.js` zniknęły WSZYSTKIE literały kolorów — paleta `WG_KOLORY` jest teraz czytana
   ze zmiennych CSS przez `wgOdswiezKolory()` (mapa nazwa→zmienna: `WG_ZMIENNE`; `rgb()` konwertowane
   na hex, bo KaTeXowy `\textcolor` w zad. 18 przyjmuje tylko hex). Przemalowanie BEZ reloadu: każdy
   widżet rejestruje swoją funkcję rysującą przez `wgZarejestrujRysowanie(canvas, draw)`, a `wgPrzemaluj()`
   odświeża paletę i przerysowuje wszystkie canvasy nadal obecne w DOM — wołane z `applyTheme()`
   (app/theme.js) oraz z nasłuchu `matchMedia("(prefers-color-scheme: dark)")` dla trybu „auto".
   (Obrazki CKE i wideo z Manima to osobna, nadal otwarta sprawa — issues/dark-mode-obrazki-wideo.md.)
   [widzety, dark-mode, canvas, tokeny]

2. „Pokaż potrzebne wzory" → „Pokaż wzory" (template.html + komentarze w exam.css/ARCHITECTURE*).  [ui, teksty]

3. „zgłoś błąd" przeniesiony do wiersza light-buttonów: kolejność Podpowiedź / Rozwiązanie / Zgłoś błąd /
   Pokaż wzory, wygląd dokładnie taki jak sąsiadów (klasa `.light-button`; `.report-error-link` została
   już tylko uchwytem dla `body.bez-zglaszania`). `.light-button-container` jest flexem, a przyciski mają
   `flex: 1 1 0` zamiast sztywnych 30% — wiersz sam rozkłada szerokości, gdy zniknie „Pokaż wzory"
   (formulasPage: null), podpowiedź albo gdy zgłaszanie jest wyłączone w panelu. Poniżej 720px łamie się
   po dwa przyciski w rzędzie (przy okazji domyka punkt „przyciski łamią się na telefonie" z sekcji
   spójności UI). Formularz zgłoszenia działa bez zmian (nadal wsuwa się nad ten wiersz).  [ui, zglaszanie, responsywnosc]

4. Zadania otwarte — redesign. Usunięte cztery rozwlekłe etykiety; textarea ma placeholder „miejsce na
   notatki", a `finalAnswer.label` jest przez renderer IGNOROWANE (pole zostaje w danych wszystkich
   arkuszy, żeby nie przepisywać ich bez potrzeby). Checklista kryteriów przeniesiona do zwijanego
   `<details class="ocena-box">` z tytułem „Sprawdź obliczenia", domyślnie ZWINIĘTEGO (to samo załatwia
   stary zarzut, że checklista spojlerowała rozwiązanie), stylizowanego jak mały panel boczny.
   Najważniejsze: checklista PRZYZNAJE PUNKTY — `gradingCriteria` to teraz obiekty `{ tekst, punkty }`,
   wynik zadania = suma zaznaczonych przycięta do `maxScore` (suma kryteriów NIE musi równać się
   maxScore — zad. 9 ma 0+1+1 przy maxScore 2). Przyciski „0 pkt / 1 pkt / 2 pkt" zniknęły; zostały
   wyłącznie jako awaryjna ścieżka dla zadań bez kryteriów w danych (dziś takich nie ma). Każde kryterium
   ma po prawej mały licznik punktów wzorowany na `.exercise-score` (kryterium warte 0 pkt zostaje szare
   także po zaznaczeniu). Punkty NIE są zapisywane — po reloadzie przeliczają się z `stan.kryteria`, więc
   ścieżka oceniania pozostaje jedna. Dla wskaźników „oceń się" „ocenione" znaczy teraz „otwarty boks"
   (`stan.ocenaOtwarta`), bo uczeń, który przejrzał listę i nic nie zaznaczył, też się ocenił — na 0 pkt.
   Kryteria dopisane do WSZYSTKICH 15 zadań otwartych obu arkuszy (2024-grudzień: 3, 8, 9, 19, 26, 28, 30;
   2026-maj: 7, 10, 11, 14, 15, 21, 27, 30) — treść to kolejne PROGI punktowe z zasad oceniania CKE,
   alternatywy („ALBO" z klucza) sklejone w jedno zdanie słowem „lub", każdy próg po 1 pkt. Wariant progów
   1:1 z kluczem wybrał Henrich (2026-08-06), po tym jak okazało się, że klucz CKE nie jest listą
   niezależnych kroków, tylko kaskadą („2 pkt — to co na 1 pkt oraz…").  [zadania-otwarte, punktacja, schemat-danych, cke]

Przy okazji domknięte i usunięte: issues/formularz-oceniania-otwarte.md (punkt 1 „ostateczna odpowiedź"
i punkt 2 „checklista" zrobione/zastąpione redesignem, punkt 3 „zastrzeżenie prawne raz w stopce" jest
w template.html jako `.samoocena-disclaimer` — przeredagowany, bo checklista przyznaje teraz punkty)
oraz punkty 4 i 5 z issues/ui-spojnosc-etap2.md (sztywne 30% szerokości light-buttonów i krzywy układ
przycisków samooceny na telefonie — oba zniknęły razem z tą paczką).

Weryfikacja: brak przeglądarki w kontenerze (CDN Playwrighta odcięty przez firewall), więc do testów
na żywo posłużył headless Chromium z npmowej paczki `@sparticuz/chromium` + biblioteki z jej `al2023.tar.br`
(LD_LIBRARY_PATH). Przeklikane oba arkusze × oba motywy × 1400px i 390px: renderowanie wszystkich zadań,
brak poziomego scrolla, boksy zwinięte, brak starych etykiet i przycisków punktowych, przycisk zgłoszenia
w wierszu, KaTeX w kryteriach, naliczanie i przycinanie punktów, przetrwanie reloadu, ukrycie boksu
w trybie egzaminu, gaszenie kropek „oceń się", przemalowanie widżetów po przełączeniu motywu bez reloadu.

[ZROBIONE 2026-08-06] (Sonnet 5) Porządki w repo: usunięte `.idea/` (stary, niespójny konfig JetBrains —
`.name` wskazywał na `matematykazen11.html`, `.iml` na `matematykazen10`, ślad skopiowania folderu
z innego projektu) oraz pusty `package-lock.json` bez towarzyszącego `package.json` (projekt nie ma
build systemu ani package managera). Do tego wcześniej ręcznie usunięte przez Henricha: testowy agent
`.claude/agents/testowy agent claude w zakladce Chat.agent.md` i log `remoteContainers-*.log`. Zmiany
tylko wystagowane, niezacommitowane na życzenie Henricha.

[ZROBIONE 2026-08-04] Projekt udało się uruchomić w Dockerze na komputerze w domu — strona była dostępna lokalnie w przeglądarce i działała zgodnie z oczekiwaniami.

[ZROBIONE 2026-08-02] (Opus 5 Medium) Licencja i zasady kontrybucji. `LICENSE.md` (wklejony ręcznie przez
Henricha) zweryfikowany sekcja po sekcji z oficjalnym PolyForm Noncommercial 1.0.0 — tekst kompletny i wierny,
poprawki tylko kosmetyczne: usunięte trailing spaces w polskiej części po `---` i dopisana sekcja „Wkład
społeczności" z linkiem do CONTRIBUTING.md. Nowe pliki: `CONTRIBUTING.md` (jak pomagać + CLA — otwarcie PR-a
= udzielenie właścicielowi szerokiej, nieodwołalnej, także komercyjnej licencji na wkład, przy zachowaniu praw
kontrybutora; sens: nie zablokować przyszłej zmiany licencji z Fazy 3), `README.md` (repo go nie miało w ogóle)
i `.github/PULL_REQUEST_TEMPLATE.md` (checklista + pogrubione odesłanie do CLA).
Dwie decyzje świadome, obie z przypomnieniem w TODO.md pod `OPUS DOPISAŁ`: (1) właściciel występuje jako
pseudonim `Henrich2137`, nie imię i nazwisko — CLA na pseudonim jest słabsze dowodowo, a podmiana wymaga
DWÓCH miejsc (LICENSE.md linie 1–2 i punkt 2 w CONTRIBUTING.md); (2) URL w linii `Required Notice:` zmieniony
z `https://matematykazen.pl` (domena jeszcze nie działa) na GitHub Pages — ta linia jest z definicji kopiowana
przez każdego redystrybutora, więc martwy link by się propagował.
Przy okazji odkłamana OVERVIEW.md: pisała, że strona jest wystawiona „pod docelową ładną domeną" i że celem
obecnej fazy jest zdobywanie zainteresowania — a to cel Fazy 2, podczas gdy Faza 1 jest jawnie bez marketingu
i bez domeny; dopisana też sekcja „Licencja" i zaktualizowana notatka o kanałach kontaktu (są już issues/PR-y)
[licencja, cla, dokumentacja, github]

[ZROBIONE 2026-08-01] Ikona strzałki #sidebar-toggle (template.html) zamieniona kierunkiem — SVG path
z lewoskrętnego `M15 5l-7 7 7 7` na prawoskrętny `M9 5l7 7-7 7`. Rotacja o 180° przy otwarciu panelu
(`body.sidebar-otwarty #sidebar-toggle` w style/sheet.css) zostaje bez zmian [ui, sidebar, css]

[ZROBIONE 2026-08-01] Ujednolicenie nazw plików-przewodników po katalogach: `tablica-wzorow-transkrypt/INDEX.md`
→ `README.md` (`git mv`), referencje zaktualizowane w CLAUDE.md (3 miejsca), done/README.md i w tym pliku.
Powód (pytanie Henricha): trzy katalogi — `done/`, `issues/`, `tablica-wzorow-transkrypt/` — miały plik o tej
samej funkcji (zasady katalogu + indeks jego zawartości), ale dwie różne nazwy. `README.md` wygrywa, bo w
podkatalogu ma ustaloną konwencję „wyjaśnij ten folder" (wizytówką projektu jest tylko README w roocie, a tego
repo nie ma), jest auto-renderowane przez GitHub/VS Code i to pierwsza nazwa, której szuka człowiek i model.
Świadomie NIE użyto `CLAUDE.md` w podkatalogach, mimo że te pliki są pisane dla modeli: nested CLAUDE.md
doczytuje się automatycznie, co kłóci się z zasadą „NIE wczytuj done/ domyślnie". Audytorium sygnalizuje
pierwsza linijka treści, nie nazwa pliku.
Drugi krok tego samego porządkowania: katalog `DONE/` → `done/` (19 odwołań przepisanych w 10 plikach .md).
`DONE` był jedynym katalogiem WIELKIMI w repo — konwencja „krzyczącej nazwy" dotyczy plików meta w roocie
(`TODO.md`, `README`, `LICENSE` — sortują się w ASCII przed małymi, więc wypływają nad kod), a nie katalogów,
które wszędzie są małymi. UWAGA przy podobnych zmianach na Windowsie: NTFS jest case-insensitive, więc
`git mv DONE done` nie zadziała wprost — trzeba przez nazwę pośrednią (`DONE` → `_tmp_done` → `done`),
inaczej git nie zapisze zmiany wielkości liter i na Linuksie/CI zostanie stara nazwa. Z tego samego powodu
stare referencje `DONE/...` działałyby dalej lokalnie, ale pękłyby na GitHubie/Linuksie — dlatego przepisane
wszystkie, mimo że lokalnie „i tak działały"  [dokumentacja, konwencje]

[ZROBIONE 2026-08-01] Martwe referencje w ARCHITECTURE.md po lipcowych podziałach plików — wszystkie
wskazują teraz na FAKTYCZNY plik, ustalony przez grep definicji, nie zgadywany:
- `script.js` (nie istnieje od 2026-07-23) → konkretny moduł przy każdej wzmiance: `SHEET_ID`,
  `renderMath()`, `mediaPath()`, `TABLICE_PDF` → app/state.js; `startSheet()` → app/bootstrap.js;
  `loadExercises()` → app/render.js; ogólne „rendering logic" → app/.
- `style.css` (podzielony na style/*.css) → `.katex 1.08em` → style/base.css; reguła stylowania zadań
  → style/ z podpowiedzią „karty zadań w sheet.css, kolory/tokeny w base.css"; nagłówek sekcji CSS → style/.
- `[exercises.json](exercises.json)` → `matura/2024-grudzien/exercises.json` (sekcja provenance dotyczy
  konkretnie tego arkusza).
- Przy okazji WYKRYTY BŁĄD LICZBOWY: ARCHITECTURE.md i CLAUDE.md mówiły o „nine `app/*.js` files",
  a plików jest DZIESIĘĆ (state, theme, exam, indicators, panels, answers, steps, report, render,
  bootstrap). Poprawione w obu; kolejność ładowania dopisana wprost do ARCHITECTURE.md, bo wcześniej
  była tylko w CLAUDE.md. Widżetów faktycznie jest dziewięć — ta liczba była dobra.
- `issues/dwie-karty-tryb-egzaminu.md` wskazywał `finishExam()` „w script.js" → app/exam.js (3 miejsca).
  Zostawione: `issues/wskazniki-reload-faza-oceniania.md`, gdzie „podział script.js → app/*.js" to opis
  historycznego zdarzenia, a nie wskaźnik na plik.
Weryfikacja: skrypt sprawdzający KAŻDY link markdown w repo względem katalogu jego pliku — zero wiszących
(wcześniej 3). Zgłoszone przeze mnie do TODO.md kilka minut wcześniej, usunięte stamtąd po zrobieniu
[dokumentacja, refaktor]

[ZROBIONE 2026-08-01] Porządki nazewnicze, część druga — cztery zmiany z listy „co jeszcze uspójnić"
(Henrich wybrał 1–4, punkt 5 o osieroconych notatkach w roocie zostaje na później):

1. PLIKI ŹRÓDŁOWE ARKUSZY mają teraz CZTERY STAŁE NAZWY w każdym `matura/<id>/`: `arkusz.pdf`,
   `arkusz.txt`, `odpowiedzi.pdf`, `odpowiedzi.txt` (12 plików przez `git mv`, we wszystkich trzech
   arkuszach). Dawniej `matematyka-2024-grudzien-probna-podstawowa-odpowiedzi.pdf` itp. — nazwa
   powtarzała id katalogu i miała zmienny człon (`probna` vs `matura`), więc model NIE MÓGŁ złożyć
   ścieżki z głowy i musiał najpierw listować katalog. Teraz ścieżka wynika z samego `<id>`.
   `meta.zasadyPdf` w obu `exercises.json` → `"odpowiedzi.pdf"` (oba pliki przeparsowane po zmianie).
2. NOWY `matura/README.md` — ŹRÓDŁO PRAWDY o tym, czym są te arkusze (poziom podstawowy, Formuła 2023,
   CKE, 180 min, 50 pkt — liczba potwierdzona w nagłówkach obu arkuszy, nie z pamięci) i co jest w
   katalogu arkusza. Tabela arkuszy: 2024-grudzień (próbna/test diagnostyczny, MMAP-P0-100-2412, wpięty),
   2025-maj (właściwa, same PDF-y, NIEwpięty), 2026-maj (właściwa, 5 maja 2026, MMAP-P0-100-2605, wpięty).
   ARCHITECTURE.md i CLAUDE.md linkują tu zamiast powtarzać listę.
3. TABLICA WZORÓW: plik `wybrane_wzory_matematyczne.pdf` → `tablica-wzorow.pdf`, katalog transkryptu
   `wybrane_wzory_matematyczne/` → `tablica-wzorow-transkrypt/`. Powód: plik i katalog miały IDENTYCZNĄ
   nazwę przy zupełnie różnej roli (PDF serwowany userom vs transkrypt tylko dla modeli) — glob łapał oba
   i przy każdej wzmiance trzeba było rozstrzygać, o który chodzi. Zmienione też `TABLICE_PDF` w
   app/state.js i `data=` w template.html. Uwaga: ID elementów `#tablica-wzorow` / `#tablica-wzorow-panel`
   w HTML/CSS to CO INNEGO niż nazwa pliku — nie ruszane.
4. `done/STARY_PRZENIESIONY_DONE.md` → `done/00-stary-done.md` (wpasowane w sekwencję 00→04).
5. USUNIĘTE MARTWE OPISY: `inne arkusze PDF/` był opisany w ARCHITECTURE.md i CLAUDE.md, a tego katalogu
   NIE MA już w repo. Przyczyna była strukturalna — układ katalogów żył zduplikowany w dwóch plikach
   naraz i się rozjeżdżał. Teraz: struktura katalogu arkusza opisana raz, w `matura/README.md`, a oba
   pliki dokumentacji tylko do niej linkują. Przy okazji przycięty przerośnięty akapit o transkrypcie
   w CLAUDE.md (miał doklejony ogon o PDF-ach arkuszy, niezwiązany z tablicą wzorów).

Weryfikacja: `grep` po całym repo nie znajduje ani jednej wiszącej starej ścieżki; oba `exercises.json`
parsują się poprawnie; `TABLICE_PDF`/`data=` wskazują na istniejący plik. Jedyne pozostawione świadomie
wystąpienia starych nazw to proza historyczna w `done/00-stary-done.md` i `done/03-2026-07-27.md`
opisująca nieistniejący już katalog „inne arkusze PDF/" — tego nie da się „naprawić" na aktualną ścieżkę,
bo opisuje stan sprzed usunięcia  [dokumentacja, konwencje, arkusze, tablica-wzorow]

[ZROBIONE 2026-07-28] Transkrypt tablicy wzorów dla modeli — `tablica-wzorow-transkrypt/`
(README.md + 16 plików sekcji, ~780 wzorów ze stron 4–33 PDF-a CKE). Cel: model ładuje jedną
sekcję (300–800 tokenów) zamiast całego PDF-a; „Skorowidz" w README.md mapuje słownictwo zadania
na ID wzoru i stronę, co ma przyspieszyć uzupełnianie `formulasPage`. Ustalenia z Henrichem:
KaTeX w konwencji `\( … \)` / `\[ … \]` identycznej jak w exercises.json (kopiowanie bez konwersji;
`$…$` NIE zadziałałoby — `renderMath` w app/state.js rejestruje tylko te dwa delimitery), pełne
zdania opisowe CKE, pozycja wzoru słownie (góra/środek/dół), sekcja 17 (tablica wartości
trygonometrycznych, s. 34) pominięta, rysunki jako legendy oznaczeń zamiast opisów figur, bez PNG,
bez znaczników podstawa/rozszerzenie. Wyciąg z PDF-a: `pdftohtml -xml` + normalizacja Unicode
Mathematical Italic (U+1D400+) na ASCII — `pdftotext` gubi zmienne i strukturę ułamków.
Weryfikacja: (1) wszystkie 782 wzory renderują się w vendorowanym KaTeX-ie, (2) 26 352 losowych
sprawdzeń numerycznych tożsamości (skrócone mnożenie, potęgi, logarytmy, Newton, Viète, ciągi,
cała trygonometria, tw. sinusów/cosinusów, Heron, pola, wariancja, pochodne) — bez błędu.
Do sprawdzenia wyrywkowego przez Henricha zostają rzeczy nieweryfikowalne liczbowo: definicje
słowne, cechy przystawania/podobieństwa, legendy oznaczeń.

[UZUPEŁNIONE 2026-07-28] Kontrola kompletności transkryptu + sekcja „Czego tu NIE MA" w README.md.
Powód: transkrypt nigdzie nie mówił, że czegoś w nim brakuje, więc model widzący wyłącznie
transkrypt nie miałby powodu otworzyć PDF-a (zgłosił Henrich). Przy okazji wyszła luka —
[8.10] procent składany ze s. 10 był pominięty (dopisany wcześniej przez Sonneta). Przyczyna
techniczna warta zapamiętania: odczyty PDF-a robiłem przez `python czytaj.py X Y | head -N`
i dla stron 9–10 limit `head` **uciął dolną część s. 10** — wzór wypadł poza widziany fragment.
Wniosek na przyszłość: przy przepisywaniu PDF-a nie ucinać outputu odczytu, albo weryfikować
kompletność osobnym przebiegiem. Zrobiona kontrola: skrypt wypisał wszystkie punkty „•"
i nagłówki sekcji ze stron 4–34, porównane jeden-do-jednego z ID w transkrypcie — po dopisaniu
[8.10] pokrycie jest pełne, dodatkowo pełne odczyty s. 10 i 17 potwierdziły brak dalszych luk.
Dopisane: tabela „Czego tu NIE MA" w README.md (rysunki → strony PDF-a, sekcja 17, strony
redakcyjne) oraz notki o rysunkach w nagłówkach sekcji 7, 9, 10, 11, 12 ze wskazaniem strony
PDF-a; przy [9.3] (wykresy sin/cos/tg) zaznaczone, że tam **rysunek jest jedyną treścią** —
w tablicy nie ma przy nim żadnego wzoru.

[ODRZUCONE 2026-07-28] Celowanie w konkretny wzór na stronie PDF-a (`#page=N&view=FitH,<top>`
zamiast samego `#page=N`). Zbudowane i przetestowane (współrzędne wzorów z `pdftohtml -xml`,
centrowanie liczone z rozmiaru panelu), po czym wycofane: Firefox i Brave przewijają poprawnie,
ale Chrome i Edge lądują zdecydowanie za nisko — wzoru nie widać. Dodatkowo przy domyślnym
kształcie panelu (28% × 80vh) cała strona i tak mieści się w kadrze przy FitH, więc kotwica
nic by nie dawała bez zmiany proporcji panelu. Ostrzeżenie zostawione w app/panels.js i
ARCHITECTURE.md, żeby nikt nie próbował drugi raz. Pole `formulasY` w exercises.json usunięte.

[ZROBIONE 2026-07-28] Skok formularza „zgłoś błąd" (link na dole karty, formularz otwiera się wyżej,
nad Podpowiedź/Rozwiązanie) — sprawdzone, zachowanie takie samo na desktop i mobile (DOM insertBefore
bez media query), Henrich zaakceptował, bez zmian. [formularz, ui]

[ZROBIONE 2026-07-28] Analityka: GoatCounter wpięty w template.html i index.html
(`data-goatcounter="https://henrich.goatcounter.com/count"`), błąd ładowania skryptu wyciszony
w belce diagnostycznej (adblock/Privacy Badger często go blokują — to nieszkodliwe, nie powinno
straszyć banerem błędu). Potwierdzone przez Henricha na żywo w panelu goatcounter.com — dzisiejsze
odwiedziny się liczą. Do pamiętania przy czytaniu statystyk: część ruchu z adblockami nie zostanie
zliczona, więc realne liczby są wyższe niż panel pokazuje. [analityka, goatcounter]

[ZROBIONE 2026-07-28] Zadania nie renderowały się na telefonie (arkusz 2024-grudzień) — potwierdzone
przez Henricha na żywo, że fix z 2026-07-24 (`.nojekyll` w rootcie, patrz issues/zadania-nie-renderuja-sie-mobile.md)
faktycznie działa na urządzeniu. [mobile, bugfix, github-pages]

[ZROBIONE 2026-07-27] (Sonnet High) „Sprawdź wszystkie odpowiedzi" pomijało zadania z polem tekstowym
+ brak potwierdzenia kliknięcia — pełny spec z (usuniętego) issues/sprawdz-wszystkie-pola-i-komunikat.md,
v0.08. Weryfikacja: Playwright headless, oba motywy, tryb „sprawdź później", brak scrolla 360px.

- REJESTR: `fillIn` i `finalAnswer` dopisane do `oczekujaceSprawdzenia` (app/render.js) obok
  ABCD/PF/multiSelect. `fillIn` — ocena wydzielona do nazwanej `ocenFillIn()` (przycisk „Sprawdź" i
  rejestr wołają tę samą funkcję, zero duplikacji normalizacji/punktacji); `czySprawdzone` czyta klasę
  `correct`/`incorrect` z DOM pierwszego pola (nie flagę) — edycja pola kasuje tę klasę, więc zadanie
  wraca do „niesprawdzone" automatycznie. `finalAnswer` — istniejąca `ocenKoncowaOdpowiedz()` wpisana do
  rejestru z `typ: "finalAnswer"` (znacznik pod bonus niżej). Skutek uboczny świadomie zaakceptowany:
  „sprawdź wszystkie" teraz też PRZYZNAJE PUNKTY za fillIn (dawniej trzeba było kliknąć każdy „Sprawdź").
- BONUS (domyka wpis z TODO.md „ostateczna odpowiedź sprawdza się sama po egzaminie"): `finishExam()`
  (app/exam.js) po zakończeniu egzaminu przelatuje rejestr i woła `ocen()` tylko dla wpisów
  `typ: "finalAnswer"` z niepustą, jeszcze nieodsłoniętą wartością — nie odsłania przy okazji zadań
  zamkniętych, których uczeń nie zdążył sprawdzić.
- KOMUNIKAT „sprawdzono ✓": nowy `<span role="status" aria-live="polite">` przy obu kopiach przycisku.
  Stopka — komunikat `position: absolute` względem nowego `#sprawdz-wszystkie-stopka-wrap` (jak
  `.answer-check-floating`), więc nigdy nie przesuwa przycisku; pod 720px przesuwa się pod przycisk
  (wycentrowany), ale ZOSTAJE `position: absolute` — zmieniają się tylko `left`/`top`/`transform`.
  Panel boczny — tylko glif „✓" (`margin-left: auto` we flexowym `.sidebar-akcja`), bo 260px
  nie mieści zdania; prawdziwy tekst leci do `aria-label`, nie do widocznej treści. Zielony (`--correct`)
  gdy jest cokolwiek zaznaczone (czy to właśnie ocenione, czy już wcześniej sprawdzone), przygaszony
  (`--text-faint`) przy pustym arkuszu — inaczej „sprawdzono" kłamałoby. Znika po ~2,5s przez `opacity`;
  kolejny klik resetuje timer; `prefers-reduced-motion: reduce` bez animacji (dopisane do wspólnego
  bloku w sheet.css). Egzamin: bez zmian — przyciski zostają `disabled` jak dotychczas, więc handler
  (i komunikat) w ogóle się nie odpala.
- POPRAWKA tego samego dnia (zgłoszone przez Henricha na żywo): pierwsza wersja mobilnego fallbacku
  (pod 720px) przełączała komunikat z `position: absolute` na `position: static; display: block` —
  wciągnęło go to z powrotem do flow `#sprawdz-wszystkie-stopka-wrap`, więc nawet PUSTY/niewidoczny
  komunikat (opacity: 0, bez treści) dokładał ~6px wysokości pod przyciskiem przez `margin-top` +
  wysokość pustej linii („sprawdź wszystkie" wyglądało na stałe za grubo na telefonie, nie tylko po
  kliknięciu). Naprawione: mobilny fallback zostaje `position: absolute`, tylko przesunięty pod
  przycisk (`left: 50%; top: 100%; transform: translateX(-50%)`) — zero wysokości w layoucie, kiedy
  komunikat jest pusty. Zweryfikowane Playwright: `bottomDiff` wrappera i przycisku 0px (było 6px).

[ZROBIONE 2026-07-27] (wpis Henricha, przeniesiony z TODO.md 2026-07-27) W trybie ćwiczeń przycisk
„sprawdź wszystkie odpowiedzi" na dole arkusza obok „rozpocznij egzamin", zostaje też w panelu bocznym.
W trybie egzaminu ostatecznie NIE jest niewidoczny, a wyszarzony — zmiana decyzji z 2026-07-26
(znikający przycisk mylił, jakby zniknęła sama funkcja; patrz komentarz przy #sprawdz-wszystkie-stopka
w style/exam.css). Wygląd obu przycisków stopki ujednolicony w sesji „spójność UI" (wpis niżej).

[ZROBIONE 2026-07-27] (Opus High, lokalnie) Trzy drobnice po przeglądzie sesji 1 przez Henricha — v0.07.
Weryfikacja: Playwright, zrzuty light/dark × 1440/1280/390 + pomiary computed style.

- CIENIE: #sidebar traci box-shadow (Henrich: „nie współgrają z logiem ani z kreską"). Panel jest przypięty
  do krawędzi i ma własną kreskę #sidebar-linia, więc cień dublował tę granicę. Panele PDF i toast cień
  ZOSTAWIAJĄ — pływają nad treścią i nie mają żadnej kreski (decyzja Henricha: „tylko panel boczny").
  Token --shadow-panel zostaje w użyciu, tylko bez sidebara.
- STOPKA: #sprawdz-wszystkie-stopka z --text-muted na pełne --text — oba przyciski stopki są teraz
  identyczne, o kolejności czytania decyduje pozycja, nie kontrast (zmierzone: rgb(17,17,17) w light,
  rgb(230,230,230) w dark, oba przyciski).
- TYTUŁ ARKUSZA: .sheet-title-heading dostał max-width: 32% (456px przy 1440px) + margin: 0 auto —
  typowy tytuł CKE zawija się na dwie wyśrodkowane linie zamiast ciągnąć się przez cały ekran.
  Pod 720px ograniczenie zdjęte (max-width: none), bo 32% z 390px zostawiłoby po dwa słowa w linii.

[ZROBIONE 2026-08-14] (Opus 5, medium, lokalnie) Wysypywanie się strony przy szybkim spamowaniu
next-step (Brave na Bazzite, kod błędu 5) — punkt zamknięty jako nieodtwarzalny. Henrich nie widział
już błędu, testy to potwierdziły; naprawa siedzi w wcześniejszych poprawkach odtwarzacza (tokeny
podmiany kroku, jedno żądanie na łączu), nic nowego nie było trzeba zmieniać.
Weryfikacja (nowych zmian w kodzie NIE ma):
- tools/test-krokow.js na szybkim serwerze (tools/serwer.js 8000), 40 ruchów × ziarna 3/11/29,
  zad. 1–3 → bez zastrzeżeń;
- to samo na łączu dławionym (--wolno=1200 --bps=60000, port 8001), 25 ruchów × ziarna 3/11 → bez zastrzeżeń;
- celowany skrypt spamujący samo ► : 120 kliknięć z odstępem 30–90 ms na każdym z zadań 1–3
  (360 kliknięć łącznie) — zero pageerror, zero crashy, video.error puste, odtwarzacz kończy
  na ostatnim kroku (step9/step6/step8). Jedyny wpis w konsoli to ERR_ADDRESS_UNREACHABLE
  z zasobu spoza strony (firewall kontenera), nie z odtwarzacza.

[ZROBIONE 2026-08-21] (Opus 5, medium, lokalnie) Zad. 2 z 2024-grudnia: rozwiązanie opisowe
przepisane na dwie kolumny (rachunek z lewej, użyty wzór z prawej), a film rozbity z sześciu
kroków na osiem, żeby jedna linijka rachunku odpowiadała jednemu krokowi filmu.
- nowy układ: klasy .rozw-2kol/.rozw-wiersz/.rozw-obl/.rozw-wzor w style/sheet.css, siatka
  siedzi na kontenerze, a wiersz znika przez display: contents, więc kolumna wzorów ma jedną
  wspólną krawędź w całym rozwiązaniu (opis w ARCHITECTURE_CSS.md);
- zaznaczanie fragmentów: \htmlClass{zielony}{...} w exercises.json, barwa z --accent-green,
  co wymagało wąskiego `trust` w renderMath (app/state.js) przepuszczającego wyłącznie to
  jedno polecenie; \textcolor z gotowym hexem odpadł, bo nie zmieniłby się w ciemnym motywie;
- scena manimations/solutionZad2.py przepisana: stany jako MathTex pocięty na części, każda
  para glifów wskazana ręcznie, więc podstawy potęg przesuwają się zamiast morfować;
- kroki 4 i 6 rozbite na 4/5 i 7/8; każdy krok ma ten sam przebieg (wszystko czarne, kluczowy
  element zapala się na zielono, animacja, znów wszystko czarne), więc jest samodzielny
  i zgodność styku z sąsiadem wychodzi sama z siebie. Zielony to --accent-green, ten sam,
  którym rozwiązanie opisowe obok zaznacza fragmenty;
- domknij() w scenie robi clear+add PRZED wait(0.25), żeby przytrzymanie pokazywało czysty
  następny stan; to zbiło rozjazd styku z ~2000 pikseli do szumu kompresji.
Weryfikacja:
- tools/wgraj-kroki.sh 2 2024-grudzien → 8 kroków, rewersy przeliczone, styk klatek SSIM
  0,99943 do 0,99994 na wszystkich siedmiu przejściach, "bez zastrzeżeń";
- tools/test-krokow.js --zadania=1, ziarna 3/11/29 → bez zastrzeżeń, Range na wideo zwraca 206;
- zrzuty rozwiązania opisowego: 900 px i 485 px, jasny i ciemny motyw, scrollWidth == clientWidth,
  siatka 345 px w 423 px karty, nic nie obcięte.
Zasady spisane na koniec: nowa sekcja „Zasady krok po kroku, wersja krótka" w
manimations/README.md (20 punktów: ile kroków, przebieg kroku, kolor, ruch, co sprawdzić po
renderze) i bliźniaczy SOLUTION_TEXT_RULES.md dla rozwiązań opisowych; wskaźnik do obu
w CLAUDE.md. Reguła koloru w obu brzmi tak samo: zielone jest to, co się ZMIENIA, a nie to,
co tylko zmienia miejsce.
Przy okazji naprawione: w v67 zniknął z exercises.json pierwszy krok zadania 2 (step1.mp4),
zjedzony przez moje własne podstawienie w surowym tekście pliku. Wykryte porównaniem obiektów
JSON z wersją sprzed zmian; poza tym jednym polem nic innego w arkuszu się nie ruszyło.

---

## [ZROBIONE 2026-08-23] Zad. 2 krok 3 przerenderowany na dwie animacje, zad. 8 napisane od nowa (v83)

**Zad. 2, krok 3** (`1/5` na `5^{-1}`). Henrich: jedynka nie ma jechać z licznika ułamka do
wykładnika, bo te dwa miejsca nic ze sobą nie mają, a uczeń widzi tylko lot przez pół kadru.
Krok idzie teraz dwiema animacjami w jednej kropce (kroków dalej osiem, `solutionText` bez zmian):
- A: przy piątce w mianowniku pojawia się zielona jedynka, czyli brakujące ogniwo `1/5 = 1/5^1`;
- B: ta sama jedynka jedzie na miejsce wykładnika, „1/" znika, a przed jedynką pojawia się minus.
Zieleń niesie tylko jedynka i minus. Znikający licznik i kreska zostają czarne, bo inaczej kolor
przestaje wskazywać, na co patrzeć. Stan pośredni `\frac{1}{5^{1}}` wchodzi do wspólnego
skalowania kroków, żeby litery nie zmieniały rozmiaru w trakcie ruchu.

**Zad. 8** (`(x+3)/(x-1) = x/(2x-2)`, wynik `x = -6`). Scena napisana od zera, bo poprzednia
powstała przed zasadami z 21 sierpnia i łamała je wszystkie naraz: cały ruch szedł przez
`TransformMatchingShapes`, kolor ustawiany był przed animacją (czyli pierwsza klatka kroku była
już podświetlona), założenie było szare, a mnożenie obu stron i skracanie mianowników działy się
w jednym kroku. Siedem kroków zastąpiło dziewięć, uzgodnionych z Henrichem przed pisaniem:
1. równanie z zadania, 2. założenie `x ≠ 1` wjeżdża pod spodem i zostaje do końca (osobny punkt
CKE), 3. `2x-2` na `2(x-1)`, 4. dopisek `/· 2(x-1)`, 5. skracanie do `2(x+3) = x`, 6. `2x+6 = x`,
7. `2x-x = -6`, 8. `x = -6`, 9. pod założeniem staje `-6 ≠ 1`, gdzie `-6` przylatuje kopią z wyniku.
`solutionText` dostał jedną linijkę więcej (rozdzielone `= x/(2(x-1))` od dopisku), więc linijek
jest tyle co kroków; opisy pod filmem napisane od nowa pod nowy podział.

Świadome uproszczenie w kroku 5: mnożnik `2(x-1)` jest w kadrze jeden, choć działa na obie strony.
Jego dwójka jedzie przed nawias po lewej, a mianowniki gasną. Rozdwajanie mnożnika na dwie kopie
dodawałoby ruchu, którego uczeń nie potrzebuje.

Weryfikacja:
- `tools/wgraj-kroki.sh 2` → 8 kroków, `tools/wgraj-kroki.sh 8` → 9 kroków, rewersy przeliczone
  od nowa, styk klatek SSIM 0,99973 do 0,99994, „bez zastrzeżeń" w obu;
- nowe `tools/zielen-krokow.py` (liczy zielone piksele klatka po klatce): wszystkie 17 kroków
  startują i kończą na zerze, zieleń gaśnie jednym ruchem;
- `tools/test-krokow.js --zadania=1,7`, ziarna 3/11/29, na szybkim serwerze i na zdławionym
  (`--wolno=1200 --bps=60000`) → bez zastrzeżeń, Range na wideo zwraca 206;
- klatki obejrzane okiem: pierwsza, po zapaleniu koloru, w połowie ruchu i ostatnia w każdym
  zmienionym kroku;
- zrzuty karty zad. 8 (1280 px jasny i ciemny, 390 px) plus pomiar `scrollWidth - clientWidth`
  przy 320/390/768 px → zero, nic nie przewija się w bok.

Nowe narzędzie: `tools/zielen-krokow.py`, opisane w `manimations/README.md` przy punkcie 26.
Zasada 11 w tym README miała jeszcze stary przykład kroku 3 i została poprawiona.

## [ZROBIONE 2026-08-23] Required Notice i README pokazują domenę

`LICENSE.md` linia 2 wskazuje na `https://matematykazen.pl` zamiast na GitHub Pages. Ta linijka
jest kopiowana przez każdego redystrybutora, więc nie może prowadzić w martwy adres; teraz
prowadzi pod adres oficjalny. `README.md` podaje domenę jako adres główny, a GitHub Pages jako
wersję roboczą z gałęzi `dev`. Notatki zaktualizowane: `issues/licencja-i-cla.md` (punkt 2 opisuje
stan po zmianie i warunek powrotu, gdyby domena wygasła) oraz `issues/cloudflare-hosting.md`
(sekcja „Do zrobienia teraz" zamieniona na „Zrobione").

Zostało dla Henricha, bo `.devcontainer/` jest w kontenerze tylko do odczytu: odkomentowanie
`matematykazen.pl` w `CONTENT_DOMAINS` w `.devcontainer/init-firewall.sh` i poprawka dwóch
wzmianek o `origin/master` w `.devcontainer/README.md`.

## [ZROBIONE 2026-08-23] Testy Henricha na domenie odklikane

Sprawdzone przez Henricha na telefonie pod `matematykazen.pl` (Cloudflare):
- przewijanie filmu kropkami w przód i w tył w rozwiązaniu krok po kroku: film skacze, nie wraca
  do zera, czyli hosting obsługuje żądania zakresowe („WYGLĄDA WSZYSTKO DOBRZE");
- panel „zasady oceniania": PDF wyświetla się w panelu, nie pobiera jako plik, także na telefonach
  („DZIAŁA, DZIAŁA TEŻ TAK JAK POWINNO NA TELEFONACH").

## [ZROBIONE 2026-08-23] Sprawdzenie auto-fetcha i spójności kontenera z gałęzią dev

Henrich: „upewnij się, żeby automatyczny fetch i rzeczy związane z kontenerem dobrze działały
w kontenerze i ładnie łączyły się z branchem dev". Przejrzane po kolei, wynik:

Działa i jest spójne:
- `.vscode/settings.json` ma `git.autofetch: true`, czyli fetch w tle co około 3 minuty,
  bez dotykania drzewa roboczego;
- `.vscode/tasks.json` odpala przy otwarciu folderu `git fetch --prune` (a nie `pull`,
  świadomie od 2026-08-15, bo pull wywracał się na read-only `.devcontainer/` i `.vscode/`,
  zostawiając drzewo z nową treścią i HEAD na starym commicie);
- fetch z wnętrza kontenera przechodzi w 0,6 s, czyli firewall przepuszcza GitHuba;
- `dev` śledzi `origin/dev`, więc `git push` bez argumentów idzie tam, gdzie ma;
- `main` śledzi `origin/main` i ma `branch.main.mergeoptions --ff-only` na stałe;
- `origin/master` już nie istnieje, zdalne gałęzie to `dev`, `main` i archiwalny `master-old`;
- klon na bieżąco, `git rev-list --left-right --count HEAD...@{u}` daje 0/0.

Nie do sprawdzenia z kontenera i dlatego oddane Henrichowi:
- `task.allowAutomaticTasks: "on"` musi stać w GLOBALNYCH (User) ustawieniach VS Code, bo
  workspace nie ma prawa sam sobie tego przyznać. W kontenerze `~/.vscode-server/data/User/settings.json`
  nie istnieje (ustawienia User są po stronie hosta), więc stanu tego przełącznika stąd nie widać.
  Bez niego zadanie startowe nie odpala się samo, a klon po cichu zostaje w tyle. Wpisane
  do TESTOWANIE HENRICH.

Do poprawy z hosta (`.devcontainer/` jest w kontenerze read-only):
- `.devcontainer/README.md` mówi o `origin/master` w TRZECH miejscach (linie 202, 203, 204),
  a nie w dwóch, jak zakładał wcześniejszy wpis w TODO. Doprecyzowane, z gotową komendą.

## [ZROBIONE] 2026-08-26 - skill `projektowanie-rozwiazan` plus domknięcie `task.allowAutomaticTasks`

**Skill.** `.claude/skills/projektowanie-rozwiazan/` (scope projektu, jedzie z repo). Pierwszy
własny skill tego projektu, reszta w `.claude/skills/` to kopie z zewnątrz. Odpowiada na pytanie
„co uczeń ma zobaczyć i zrozumieć", zanim powstanie scena Manim, znaczniki `solutionText` albo
widżet. Oddaje **dokument projektowy po polsku, nie kod** (decyzja Henricha 2026-08-26: skill ma
skupiać uwagę na dydaktyce i rachunku, a na technikaliach tylko tyle, żeby nie zaprojektować
czegoś niewykonalnego albo odstającego od dotychczasowych rozwiązań).

Powstał ze szkicu Henricha plus listy dziewięciu technik dydaktycznych z researchu. Cztery pliki
w `references/`: `zasady-wizualne.md` (film), `zasady-tekstowe.md` (rozwiązanie opisowe),
`poe-wzorzec.md` (widżet), `typowe-bledy.md` (lista Henricha ze sprawozdań CKE 2024 i 2025).

Trzy rzeczy w szkicu były nietrafione i zostały poprawione przy pisaniu:
- szkic odsyłał po „wpis w transkrypcie zasad oceniania CKE", a takiego transkryptu nie ma:
  zasady oceniania to `matura/<arkusz>/odpowiedzi.pdf`, wyciąg tekstowy to `odpowiedzi.txt`
  (dla `2024-grudzien` w cp1250 i bez ogonków). SKILL.md ma teraz tabelę, gdzie co leży;
- szkic odsyłał do `references/typowe-bledy.md`, którego nie było. Listę dosłał Henrich w tej
  samej sesji, weszła w całości, z dopisaną pod każdą grupą linijką „Jak rozbroić";
- technika „informacji przemijającej" kazała zostawiać poprzednią linijkę w kadrze wyszarzoną.
  **Rozstrzygnięcie Henricha: kadr zostaje czysty**, zasada domowa z `manimations/README.md`
  wygrywa. Zapisane w `zasady-wizualne.md` jako decyzja z datą, żeby kolejny model tego nie
  „poprawił"; przemijanie obrazu rekompensują rozwiązanie opisowe obok filmu, kropki i cofanie.

Nie odpalono testów na podagentach, których wymaga `superpowers:writing-skills` (kosztowne,
Henrich prosi o ostrzeżenie przed taką robotą). Skill sprawdzi się na pierwszym prawdziwym zadaniu.

**`task.allowAutomaticTasks`.** Wpis z TESTOWANIE HENRICH domknięty i usunięty z TODO.md:
Henrich sprawdził na hoście, przełącznik stoi na `on`, a klon w tej sesji był na bieżąco
(`git rev-list --left-right --count HEAD...@{u}` dało 0/0), czyli zadanie startowe faktycznie
się odpala.

## [ZROBIONE 2026-08-27] Zadanie 8 z 2024-grudnia napisane od zera, razem z filmem

Poprzednie rozwiązanie opisowe i film Henrich kazał skasować i pisać na świeżo, bez
podawania, co konkretnie było złe. Powstały trzy wersje w jednej sesji, dwie pierwsze
odrzucone przez Henricha:

1. droga przez mnożenie na krzyż i równanie kwadratowe z deltą, 23 pozycje. Odrzucona:
   „za dużo kroków i niepotrzebnie uwzględnia deltę";
2. droga przez wspólny mianownik, 15 pozycji, zdania wplecione w ciąg rachunku;
3. **wersja przyjęta**: ten sam rachunek, ale linijki i zdania rozdzielone. Każda linijka
   w `.rozw-linia`, między nimi bledszy `.rozw-komentarz` mówiący, co się dzieje
   w przejściu, dopisek działania obustronnego w osobnym `.rozw-dzialanie`, założenie
   \(x \ne 1\) jako druga linijka rachunku, a sprawdzenie przez podstawienie jako
   odkreślona część na dole (`.rozw-sprawdzenie`).

Trzy rzeczy warte zapamiętania:

- **Dwie kolumny nie mieszczą się na telefonie przy długim rachunku.** Zmierzone: przy oknie
  390 px kolumna wzorów bierze 104 px, przerwa 40 px, na rachunek zostaje 154 px z 298 px
  i łamie się 17 linijek z 23. Stąd układ jednokolumnowy. Ostrzeżenie z liczbami wisi
  w `SOLUTION_TEXT_RULES.md`.
- **Ułamka nie wolno ciąć na argumenty `MathTex`**: Manim renderuje każdy argument osobno
  i domyka klamry, więc `\frac{(x+3)` staje się `\frac{(x+3)}` i render pada. Uchwyty do
  wnętrza ułamka bierze się z glifów przez `rozbij_ulamek`.
- **Film ma 10 kroków, rozwiązanie opisowe 13 pozycji** i to jest świadomy rozjazd: trzy
  ostatnie pozycje to sprawdzenie, którego na życzenie Henricha film nie pokazuje.

Film: `matura/2024-grudzien/media/zad8/solution-step-by-step/`, scena `manimations/solutionZad8.py`,
scenariusz `manimations/zad8-kroki.md`, spec `issues/spec-zad8-2024-grudzien.md`.
Styki klatek SSIM ≥ 0,99976, zieleń bez zastrzeżeń, `tools/test-krokow.js` na zad. 8 czysty.

## [ZROBIONE] 2026-08-29 — model widzi wyrenderowane filmy: tools/klatki.sh + skill ogladanie-krokow

Punkt z TODO „dla Henricha: przekminić i zainstalować visualise czy coś". Okazało się, że
**nie ma czego instalować**: w oficjalnym magazynie pluginów Claude Code (sprawdzone
2026-08-29, `plugins/` i `external_plugins/` w cache marketplace'u) nie ma nic do oglądania
wideo, a jedyny kandydat wizualny, `playwright`, dubluje zainstalowany już
`chrome-devtools-mcp`. Model przyjmuje na wejściu obrazki, nie pliki mp4, więc jedyna droga
prowadzi przez zamianę filmu na klatki. To nie jest obejście ograniczenia, tylko jedyny
format, który wchodzi.

**Co powstało:**

- **[tools/klatki.sh](../tools/klatki.sh)** — trzy tryby:
  - `stany` — pierwsza i ostatnia klatka każdego kroku w zadaniu, sklejone w jedną kratkę
    z podpisami. Jeden obrazek pokazuje cały tok rozwiązania; przy zad. 9 (22 kroki) to
    strona 1 z 2 przy budżecie 2500 tokenów.
  - `film` — jeden krok jako sekwencja co N-tej klatki. `--co 6` daje 20 klatek na sekundę,
    `--co 20` mniej klatek, za to dużych i czytelnych.
  - `styk` — para klatek na złączu kroków w pełnej rozdzielczości plus różnica wzmocniona
    (domyślnie x25). Uzupełnia `styk-klatek.sh`: tamten mówi, ŻE para nie przechodzi, ten
    pokazuje, GDZIE.
- **`.claude/skills/ogladanie-krokow/SKILL.md`** — kiedy sięgać po który tryb, na co patrzeć
  (styk, zieleń tylko w środku, ruch za rachunkiem), czego na klatkach nie widać i jak nie
  przepalić kontekstu.
- Punkt 25 w `manimations/README.md` („obejrzyj klatki okiem") dostał wreszcie narzędzie —
  dotąd był poleceniem bez sposobu wykonania.

**Cztery rzeczy warte zapamiętania:**

- **Koszt obrazka zależy wyłącznie od jego powierzchni** (mniej więcej piksele/750), nie od
  tego, ile klatek jest w środku. Trzydzieści małych kafelków kosztuje tyle samo co jedna
  duża klatka o tej samej powierzchni; płaci się czytelnością. Stąd pokrętło `--tokeny`:
  skrypt dobiera wielkość kafelka pod budżet i dzieli na strony, gdy się nie mieści.
- **Bezruch trzeba odsiewać, ale wyrzucony czas trzeba OZNACZYĆ.** Zmierzone na zad. 9,
  krok 3: po wzięciu co szóstej klatki zostają 72, z czego **44 to ta sama klatka**
  (`self.wait`). Bez `mpdecimate` większość budżetu szła na powtórzenia; po odsianiu
  kafelki urosły ze 186 do 242 px przy tym samym koszcie. Samo odsianie jednak **kłamie** —
  dwa sąsiednie kafelki wyglądają jak ciąg ruchu, a dzieli je pół sekundy postoju (pytanie
  Henricha, które to wyłapało). Stąd podpis kafelka to **czas w filmie w milisekundach**,
  a nie numer po kolei, plus pomarańczowy pasek „bezruch +X.XXs" na kafelku, na którym
  obraz staje. Czasy bierze `showinfo` z przebiegu na sucho: `mpdecimate` zachowuje
  oryginalne `pts`, więc luka między wypisanymi `pts_time` to dokładnie wyrzucony bezruch.
  Próg „to już postój" to 2,5-krotność zwykłego odstępu (`--co` / fps).
- **`drawtext` nie ma formatu ułamkowego z zadaną liczbą miejsc.** `%{eif:t:f:2}` odpada
  („Invalid format 'f'"), `%{pts:flt}` wypisuje sześć miejsc po przecinku („0.200000").
  Stąd milisekundy przez `%{eif:t*1000:d}`. Dwukropki w środku `%{...}` trzeba eskejpować,
  inaczej ffmpeg czyta je jako separator opcji i skarży się o „both text and text file".
- **`eq=contrast` nie nadaje się do podbijania różnicy klatek.** Przy SSIM 0,9999 różnice
  są rzędu jednostek na 255 i mnożenie przez 10 dało obraz nie do odróżnienia od czerni.
  Działa dopiero `geq=lum='min(255,lum(X,Y)*25)'`. Do obrazka dochodzi liczba
  `YMAX` z `signalstats`, bo bez niej nie wiadomo, czy jasne miejsca to rozjazd, czy szum
  kodera podbity dwudziestopięciokrotnie.
- **`ffmpeg -v error` gasi wynik filtra `ssim`** (wypisuje się na poziomie „info"), a
  `metadata=print` wymaga `file=-`, żeby trafić na standardowe wyjście. Obie rzeczy
  wyglądały jak brak wyniku.

**Sprawdzone na zad. 9 arkusza 2024-grudzien** (22 kroki): wszystkie trzy tryby, obie strony
`stany`, gęstsze i rzadsze `--co`, oraz błędy (nieistniejący krok, ostatni krok bez
następnika). Tryb `styk` na parze 3/4 pokazał, że szare `/−7` widoczne na końcu kroku 3
jest w OBU klatkach — różnica to same kontury glifów, czyli szum kodera H.264 (YMAX 55/255
rozłożone po krawędziach całej linii), a nie usterka sceny.
