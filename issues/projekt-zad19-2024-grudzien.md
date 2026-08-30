# Projekt: zadanie 19, grudzień 2024 (pole trapezu prostokątnego)

Wersja druga, 2026-08-30. Pierwsza (Sonnet, v106) liczyła przez cosinus i sinus kąta
\(BAC\); Henrich odrzucił ją w całości: „nie baw się w pokazywanie sinusa, znajdź inną
jak najprostszą do zrozumienia drogę, sugeruję podobieństwo trójkątów, bo można to fajnie
pokazać przez animację przeniesienia i przekręcenia jednego trójkąta w miejsce drugiego".
Stara scena i stare filmy zostały usunięte w commicie `cbc7be9`, więc to jest projekt
od czystej kartki.

## Zadanie i klucz

Trapez prostokątny \(ABCD\): \(|AB| = 7{,}5\) (dłuższa podstawa), przekątna \(|AC| = 6\),
kąty proste przy \(D\) oraz przy \(C\) w trójkącie \(ABC\). Szukane pole trapezu.

Rachunek policzony od zera i porównany z `odpowiedzi.pdf` (zasady oceniania, s. 17):

| etap | wynik | punkt CKE |
|---|---|---|
| \(\vert BC\vert\) z Pitagorasa | \(4{,}5\) | 1 pkt |
| skala podobieństwa \(k = 6 : 7{,}5\) | \(0{,}8\) | ten sam 1 pkt (wariant) |
| \(\vert DC\vert = 6 \cdot 0{,}8\) | \(4{,}8\) | 2 pkt |
| \(\vert AD\vert = 4{,}5 \cdot 0{,}8\) | \(3{,}6\) | 3 pkt (obie długości) |
| \(P = \frac{7{,}5 + 4{,}8}{2} \cdot 3{,}6\) | \(22{,}14\) | 4 pkt |

Zgadza się z kluczem (\(P = 22{,}14\), \(|AD| = 3{,}6\), \(|DC| = 4{,}8\), \(|BC| = 4{,}5\)).

Droga jest inna niż „Sposób I" CKE (tam z podobieństwa wychodzi proporcja
\(|DC| : 6 = 6 : 7{,}5\), a \(|AD|\) dolicza się drugim Pitagorasem). Wybór Henricha,
2026-08-30: liczymy \(|BC|\) Pitagorasem, a potem obie brakujące długości wychodzą
zwykłym mnożeniem przez skalę \(0{,}8\). Uczeń nie rozwiązuje żadnej proporcji, a skala
jest liczbą, którą widać w animacji.

## Dlaczego akurat podobieństwo

Trójkąty \(ACD\) i \(ABC\) mają po kącie prostym (przy \(D\) i przy \(C\)) oraz równe
kąty \(DCA\) i \(CAB\) (naprzemianległe przy \(DC \parallel AB\)), więc są podobne
z cechy kąt-kąt-kąt, wzór [10.8] z tablicy, s. 17. Odpowiedniość wierzchołków:
\(C \to A\), \(D \to C\), \(A \to B\), czyli:

- przeciwprostokątna \(AC = 6\) odpowiada przeciwprostokątnej \(AB = 7{,}5\),
- przyprostokątna \(DC\) odpowiada przyprostokątnej \(AC = 6\),
- przyprostokątna \(AD\) odpowiada przyprostokątnej \(CB = 4{,}5\).

**Zmierzone, bo to zmienia animację:** przy tej odpowiedniości trójka \((D, C, A)\) jest
zorientowana przeciwnie do swojego obrazu \((C, A, B)\) (pola zorientowane \(-17{,}28\)
i \(+27\) w jednostkach zadania). Podobieństwo jest więc **odwrotne**: sam obrót w
płaszczyźnie nie nałoży małego trójkąta na duży, trzeba go najpierw **przekręcić na drugą
stronę**, jak kartkę. Dobra wiadomość: to dokładnie to „przekręcanie", o którym pisał
Henrich, więc animacja go pokazuje wprost, a nie ukrywa.

## Kadr

Trzy pasy, tak jak w pozostałych scenach z rysunkiem (README, punkt 35):

- **lewa połowa: rysunek trapezu**, przez cały film, w prawdziwych proporcjach (bez tego
  nakładanie trójkątów by nie wyszło). Podpisy \(7{,}5\) i \(6\) od początku; \(4{,}5\),
  \(4{,}8\) i \(3{,}6\) dopisują się na rysunku w chwili, w której zostaną policzone,
- **prawa połowa: jedna linijka rachunku**, przekształcana krok po kroku, ze wzorem
  z tablicy nad nią,
- prawa połowa jest wolna od kroku 8, więc kroki 9 i 10 używają jej jako warsztatu:
  tam ląduje przekręcona kopia małego trójkąta.

## Kroki filmu (17) i linijki rozwiązania zwykłego

Jeden do jednego, poza krokami 1, 8, 9 i 10, które w tekście są zdaniem komentarza,
a nie osobną linijką rachunku (zasada 6 z SOLUTION_TEXT_RULES.md, rozjazd świadomy).

| krok | co się dzieje w kadrze | co zostaje na końcu |
|---|---|---|
| 1 | wjeżdża trapez z danymi \(7{,}5\), \(6\) i dwoma kątami prostymi; nic się nie liczy, brak koloru | rysunek |
| 2 | zapala się trójkąt \(ABC\), nad rachunkiem staje wzór [10.1] \(a^2 + b^2 = c^2\) | wzór |
| 3 | liczby przylatują z rysunku na miejsca liter | \(6^{2} + \vert BC\vert^{2} = 7{,}5^{2}\) |
| 4 | \(6^{2}\) przechodzi na drugą stronę ze zmianą znaku | \(\vert BC\vert^{2} = 7{,}5^{2} - 6^{2}\) |
| 5 | podnosimy do kwadratu | \(\vert BC\vert^{2} = 56{,}25 - 36\) |
| 6 | odejmowanie | \(\vert BC\vert^{2} = 20{,}25\) |
| 7 | pierwiastkujemy, wynik jedzie na rysunek przy boku \(BC\) | \(\vert BC\vert = 4{,}5\) |
| 8 | łuki przy \(A\) i przy \(C\): te dwa kąty są równe, bo \(DC \parallel AB\); kąty proste już stoją | rysunek z kątami |
| 9 | kopia trójkąta \(ACD\) odkleja się, **przekręca się na drugą stronę** i staje w prawej połowie w tej samej pozie co duży trójkąt | mały trójkąt obok |
| 10 | mały rośnie \(1{,}25\) raza i wjeżdża na trójkąt \(ABC\), pokrywając go dokładnie | pokrycie |
| 11 | z przeciwprostokątnych wychodzi skala | \(k = \dfrac{6}{7{,}5} = 0{,}8\) |
| 12 | bok \(DC\) odpowiada bokowi \(AC = 6\) | \(\vert DC\vert = 6 \cdot 0{,}8 = 4{,}8\) |
| 13 | bok \(AD\) odpowiada bokowi \(CB = 4{,}5\) | \(\vert AD\vert = 4{,}5 \cdot 0{,}8 = 3{,}6\) |
| 14 | wzór [10.17] na pole trapezu, liczby przylatują z rysunku | \(P = \dfrac{7{,}5 + 4{,}8}{2} \cdot 3{,}6\) |
| 15 | dodawanie w liczniku | \(P = \dfrac{12{,}3}{2} \cdot 3{,}6\) |
| 16 | dzielenie | \(P = 6{,}15 \cdot 3{,}6\) |
| 17 | mnożenie i wynik | \(P = 22{,}14\) |

## Kolor

Zieleń tylko na to, co się w danym kroku zmienia (COLORS.md, README punkt 11):

- kroki 3 do 7: liczba, która właśnie wchodzi do rachunku albo właśnie się przeliczyła,
- krok 8: łuki kątów są **szare**, nie zielone: to oznaczenie, nie rachunek (README 36),
- kroki 9 i 10: przekręcana kopia jest zielona przez cały ruch, bo to ona jest tym,
  na co uczeń ma patrzeć; zieleń gaśnie przed końcem kroku 10,
- kroki 12 i 13: zielona jest ta długość, która właśnie powstała, oraz jej podpis
  dopisany na rysunku.

## Czego ten film NIE pokazuje

- **Nie ma dowodu, że \(DC \parallel AB\)**: to definicja trapezu, uczeń ma ją z treści.
- **Nie ma nazwy „cecha kąt-kąt-kąt"** w kadrze. Nazwa cechy nic tu nie tłumaczy, a film
  i tak pokazuje oba równe kąty. Nazwa stoi w rozwiązaniu zwykłym, bo tam jest miejsce
  na zdanie i bo klucz CKE mówi o cechach podobieństwa.
- **Nie ma drogi przez sinus i cosinus** (decyzja Henricha), mimo że klucz ją dopuszcza.
