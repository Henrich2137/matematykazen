# Jak projektować widżety (wnioski z pilotażu Fable, 2026-08-15)

Przewodnik dla modelu, który ma SAMODZIELNIE wymyślić widżet do nowego zadania,
w stylu wypracowanym z Henrichem na arkuszu 2026-maj (zad. 2, 8, 10, 11, 12, 13).
Mechanika (rejestr, helpery, klasy CSS): [README.md](README.md). Kolory:
[COLORS.md](../COLORS.md). Stan pilotażu i metoda wycinania rysunków z PDF:
[issues/fable-przekazanie-2026-maj.md](../issues/fable-przekazanie-2026-maj.md).

## Od czego zacząć myślenie

1. **Znajdź sedno zadania i typowy błąd ucznia.** Widżet istnieje po to, żeby
   uczeń ODKRYŁ przyczynę, nie obejrzał skutek. Przykłady z pilotażu:
   - zad. 2: błąd "2 razy 600 = 1200" kontra procent składany; widżet pokazuje,
     że drugi rok liczy się od powiększonego kapitału (strzałki +600 i +636).
   - zad. 8: suwak rusza x, NIE parametrem m, bo sednem jest "nawias się zeruje,
     więc iloczyn jest zerem". Suwak na m pokazywałby skutek zamiast przyczyny.
   - zad. 13.2: różnica między odpowiedziami 3/2 i -3/2; widżet pokazuje, że
     minus siedzi w ujemnym x (idziemy w lewo po ramieniu kąta), nie w y.
2. **Uczeń rusza tą wielkością, która odsłania mechanizm** i to ona dostaje
   kolor niewiadomej. Reszta zostaje czarna albo dostaje kolor drugiego
   parametru, jeśli też jest sterowalna.
3. **Odczyt pod płótnem to rachunek, nie wyrok**: podstawienie aktualnej
   wartości do wzoru/równania z zadania, linijka po linijce, a na końcu ✓/✗.
   Zielony znaczek zapala się, gdy uczeń trafi w wartości z zadania; nigdy nie
   przemalowuje elementu, którym rusza.

## Spójność, której pilnuje Henrich (każdy punkt to jego realna uwaga)

- **Zgodność z tablicami CKE i rysunkiem arkusza.** Notacja jak w tablicach
  (np. tg alfa = y/x, nie "slope"), trójkąty i oznaczenia jak na s. 11,
  wykres jak na rysunku zadania. Gdy zadanie ma rysunek, wytnij go z arkusza
  do media/ (metoda w notatce sztafetowej) i odwzoruj w widżecie.
- **Kratka układu współrzędnych ZAWSZE kwadratowa** (wgWysokoscKwadratowa).
  Ściśnięty wykres to błąd.
- **Nic się nie klei i nic nie zasłania**: liczby pod osią schodzą pod promień
  kropki, tytuł ma margines od separatora, strzałki nie dotykają rogów słupków,
  podpisy nie nachodzą na podziałkę.
- **Zakresy przeciągania do końca sensownego obszaru.** Prosta, która
  zatrzymuje się kawałek przed krawędzią, irytuje. Jeśli pełny zakres psuje
  matematykę (np. przedział wychodzi poza dziedzinę), dotnij wartości W ŚRODKU
  logiki, nie zakres ruchu.
- **Sterowanie płynne, nie skokowe**: suwaki step 0.05, przeciąganie
  zaokrąglane do 0.05, plus wgPrzyciagnij do wartości z zadania (dzięki temu
  trafienie palcem jest możliwe, a porównanie === działa). Wielkości z natury
  całkowite (liczba biletów) zostają skokowe.
- **Etykiety jednoznaczne dla ucznia, który widzi je pierwszy raz.**
  "+636 zł" nad słupkiem wyglądało na sumę odsetek; naprawa to strzałka MIĘDZY
  słupkami plus linia bazowa na poziomie wpłaty. Nazwy pełne ("suma odsetek"),
  jednostki przy liczbach.
- **Rachunek wielolinijkowy układa się w kolumny jak w tabelce i nie skacze**
  przy ruszaniu suwakiem: KaTeX \begin{array}, liczby dopychane \hphantom,
  etykiety suwaków o stałej szerokości.
- **Bez zbędnych elementów**: uchwyt-kropka, którego nie trzeba łapać, wylatuje;
  widok bez interakcji ma to napisane wprost w tytule.
- **Tytuł mówi, co ZROBIĆ** ("Zmień p przy pomocy suwaka"), nie co wyjdzie.
- **Mniej komentarzy, więcej rachunku**; jedno zdanie wyjaśnienia tylko tam,
  gdzie bez niego nie wiadomo, skąd wynik.

## Dopisane po zad. 14 i 19 (2026-08-16, uwagi Henricha)

- **Domyślnie JEDNA karta.** Zakładki dokładaj tylko wtedy, gdy zadanie ma dwa
  osobne kroki i sam o nie poprosisz. Henrich przy zad. 14 dostał dwie i przyjął
  je, ale zaznaczył, że prosił o jedną; zad. 19 z jedną kartą przeszło od razu.
- **Odczyt to jeden rachunek, nie protokół.** Cztery wiersze z zad. 19
  (`|∢ADC| = 50°`, `|∢AOC| = 2·50° = 100°`, …) zostały ścięte do jednej linijki
  `50° · 2 = 100° = 70° + 30°` i dopiero wtedy się broniły. Każda liczba w niej
  ma być liczona z rysunku, żeby szła za przeciąganymi punktami.
- **Podpisy na płótnie: tło w kolorze płótna.** Gdy element może się przesunąć
  (przeciągany punkt, ruchoma cięciwa), prędzej czy później przetnie jakiś
  napis. Prostokąt `WG_KOLORY.plotno` pod tekstem załatwia to raz na zawsze,
  taniej niż kombinowanie z położeniem etykiety.
- **Strzałki i miary czytaj się jednakowo.** Obie miary kątów przy jednym
  wierzchołku mają siedzieć po tej samej stronie swoich łuków (u nas: łuk + 16px),
  a nie jedna wewnątrz i jedna na zewnątrz.
- **Strzałka wektora idzie tam, gdzie jest wolne miejsce** (w zad. 14 pod
  wierzchołki, nie nad nie), a pod nią wystarczy sama liczba. Kierunek widać
  po grocie, dopisek „w lewo" jest zbędny.
- **Zakresy suwaków bierz szerokie, nawet gdy komplikują rysunek.** Prośba
  Henricha o `<-2; 2>` w zad. 14 wymusiła obsługę paraboli odwróconej ramionami
  w dół: nazwy krzywych schodzą pod wierzchołek, miejsca zerowe znikają, a
  wartość spoza kadru dostaje grot przy krawędzi zamiast kropki. To trzy
  poprawki, ale dopiero z nimi widżet pokazuje pełny obraz.
- **Rysunek z arkusza w treści nie może być szeroki na całą kartę.** Limit to
  380px (`.question img`). Rysunek szeroki i niski, złożony z dwóch wykresów,
  rozdziel na dwa pliki w `.rys-para`: na komputerze staną obok siebie, a na
  telefonie zawiną się jeden pod drugi i będą dwa razy większe.

## Merytoryka

- Policz zadanie samodzielnie od zera i porównaj z kluczem (odpowiedzi.txt),
  ZANIM zaprojektujesz widżet: konstrukcja często zależy od struktury
  rozwiązania (które nawiasy, jakie pierwiastki, skąd znak).
- Przy dwuznaczności matematycznej lub notacyjnej PYTAJ Henricha, nie zgaduj.
  Przykład z pilotażu: minus w tg alfa dało się przypisać do y (konwencja
  nachylenia) albo do x (definicja kąta z tablic); wybór zmieniał cały rysunek.
- Wartości niewymierne/ułamkowe pokazuj dokładnie (np. -4/3 ułamkiem), nie
  zaokrąglone, jeśli ✓ przy nich się zapala.

## Rytm oddawania pracy

Jedna paczka = jedna wersja (template.html + index.html naraz) = jeden commit
z push. Do TODO.md (TESTOWANIE HENRICH) wpisy "co kliknąć -> czego szukać",
zawsze z punktami: telefon (palec, 485 px), zmiana motywu przy otwartym
widżecie, zmienione pliki wspólne (mogą zepsuć inne arkusze). Szczegóły
wersji do done/04-biezace.md. Weryfikacja przed commitem: Playwright
(serwer `node tools/serwer.js 8001`, `.katex-error` musi być 0, zrzuty w obu
motywach), nigdy "na oko".

## Dopisane po zad. 10 i 12.1 (2026-08-30, uwagi Henricha)

- **Kolor nie może odpowiadać na pytanie zadania.** Pełna reguła i dlaczego, w COLORS.md,
  sekcja „Kolor nie może odpowiadać na pytanie zadania". Skrót: zieleń i czerwień
  przypisane na stałe dwóm kawałkom rysunku czytają się jako „ta odpowiedź dobra, ta zła",
  i w zad. 12.1 wyszło dokładnie odwrotnie, niż jest naprawdę. Zieleń ma WĘDROWAĆ za
  punktem ucznia, a nie siedzieć na jednym kawałku.
- **Ograniczenie zakresu suwaka bywa treścią, nie kosmetyką.** W zad. 10 dziedzina to
  \((-4,\ 4\rangle\), więc suwak nie może dochodzić do \(-4\). Stało tam \(-3{,}98\):
  formalnie poprawnie, ale różnica wynosiła niecały piksel, więc punkt siadał na kółku
  otwartym i wyglądało to tak, jakby \(-4\) do dziedziny należało. **Jeśli coś ma być
  WIDAĆ, zmierz to w pikselach, a nie w jednostkach dziedziny.**
- **`min` suwaka musi być podzielne przez `step`.** Przeglądarka liczy dozwolone wartości
  jako `min + k * step`, więc przy `min="-3.75" step="0.02"` zero nie jest osiągalne
  i widżet startuje od \(x = 0{,}01\). Zapis \(-3{,}76\) wygląda tak samo, a wraca okrągłe
  wartości. Sprawdzasz to zrzutem odczytu, nie w kodzie.

## Checklist nowego widżetu

1. Sedno + typowy błąd ucznia -> co uczeń rusza i co ma zauważyć.
2. Liczby zadania policzone ręcznie, zgodne z kluczem.
3. Plik w widgets/ (para widżetów jednego zadania może dzielić plik),
   nagłówek SPDX na górze pliku (katalog jest zastrzeżony, patrz
   widgets/LICENSE.md), wpis w app/widget-registry.js, tag <script>
   w template.html, wiersz w README.md.
4. Budowa na klockach: wgUklad + wgRysujUklad + wgWysokoscKwadratowa
   (wykresy), wgZakladki (kilka widoków), wgDraggable + wgPrzyciagnij,
   wgMath/wgTexLiczba/wgUstawHTML (odczyt), wgZarejestrujRysowanie
   (OBOWIĄZKOWE, inaczej motyw nie przemaluje płótna).
5. Kolory tylko z WG_KOLORY; suwak slider.style.accentColor w draw().
   Sprawdź, czy zieleń/czerwień nie pokrywa się z podziałem na odpowiedź dobrą
   i złą (COLORS.md), a przy suwaku, czy `min` dzieli się przez `step`.
6. hint (nie zdradza) + solutionText (wzór, potem rozwiazanie-kroki).
7. Test w Playwright, wersja, TODO, done/, commit, push.
