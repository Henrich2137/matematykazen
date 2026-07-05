/*
Schemat zadania (docelowo plik przejdzie na exercises.json):

{
    type: "ABCD" | "PF" | "multiSelect" | "open",
        // ABCD        – jednokrotny wybór (domyślne, gdy answers ma elementy, a type brak)
        // PF          – prawda/fałsz: pole `statements` zamiast `answers`
        // multiSelect – wybór kilku odpowiedzi: pole `correctAnswerIndices`
        // open        – zadanie otwarte (answers: []); przy selfScore: true renderuje
        //               się panel samooceny 0..maxScore pkt
    question: "HTML",
    answers: ["HTML", ...],            // ABCD/multiSelect; [] dla PF i open
    correctAnswerIndex: 0,             // ABCD: 0 = A, 1 = B, ...; -1 = niewypełnione (tryb "?")
    correctAnswerIndices: [1, 3],      // tylko multiSelect (kolejność bez znaczenia)
    statements: [{ text, answer }],    // tylko PF; answer: true = P, false = F
    maxScore: 1,
    selfScore: false,                  // open: true włącza panel samooceny
    hint: "HTML",                      // pusty string chowa przycisk "Podpowiedź"
    formulasPage: 4 | null,            // strona w wybrane_wzory_matematyczne.pdf
    solutionText: "HTML",
    solutionTextMore: "HTML",
    solutionStepByStep: null | [{ type: "video"|"image"|"text", src, text }],
    solutionInteractive: null | function (container) { ... }
}

maxTotalScore NIE jest już deklarowane tutaj — suma liczy się automatycznie
z pól maxScore w matematykazen.html.

Zadania 1-30 odpowiadają oryginalnemu arkuszowi CKE (MMAP-P0-100-2412,
grudzień 2024); treści i odpowiedzi 18-30 zweryfikowane z materiałem
przekazanym przez autora (suma punktów = 50, zgodnie z arkuszem).
Jedyny znany brak: tabela w zad 29 jest odtworzona tak, by dawała wyniki
z klucza (średnia 6,38, mediana 6,5) — do porównania z oryginałem, patrz todo.md.
*/

const exercises = [
    {
        question: "<b>Zadanie 1.</b> <br><br> Liczby 𝑥₁ i 𝑥₂ są różnymi rozwiązaniami równania |𝑥 + 4| = 7. <br>Suma 𝑥₁ + 𝑥₂ jest równa:",
        answers: ["A. (−14)", "B. (−8)", "C. 3", "D. 8"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Z wartości bezwzględnej czyli |takich nawiasów| zawsze wyjdzie wartość nieujemna, czyli: |7| = 7 oraz |-7| = 7. Co więc musi stać zamiast x aby wychodziło podobnie jak w tych przykładach?",
        formulasPage: 4,
        solutionText: "Geometrycznie: |𝑥 + 4| = 7 to wszystkie liczby odległe o <b>7</b> od liczby <b>−4</b>, czyli 𝑥₁ = 3 i 𝑥₂ = −11. Suma: <b>3 + (−11) = −8</b> — odpowiedź <b>B</b>.",
        solutionTextMore: "po opuszczeniu nawiasów są dwie możliwości: <br><br> <span class='mathText'> 1. <br>  x + 4 = 7 <br> x = 7 - 4 <br> <b> x = 3 </b>  <br><br> 2. <br> x + 4 = -7 <br> x = -7 - 4  <br> <b> x = -11</b> <br><br>  <b> 3 + (-11) = -8 </b> </span><br><br> czyli odp B.<br><br>",
        solutionStepByStep: [
            { type: "video", src: "zad1/zad1rozw_step1.mp4", text: "Tu będą pojawiać się różne komentarze" },
            { type: "video", src: "zad1/zad1rozw_step2.mp4", text: "Niestety będą miały one różną długość więc jeśli przesadzę to albo zacznie to wchodzić na nawigacje albo nawigacja będzie skakać. Mogę coś tu jeszcze popisać aby to sprawdzić." },
            { type: "video", src: "zad1/zad1rozw_step3.mp4", text: "Rozwiązaniem może być przesinięcie komentarzy poniżej nawigacji ale to będzie pewnie dziwnie wyglądać" },
            { type: "video", src: "zad1/zad1rozw_step4.mp4", text: "W razie braku komentarzy będę mógł tu wstawić linię" },
            { type: "video", src: "zad1/zad1rozw_step5.mp4", text: "" },
            { type: "video", src: "zad1/zad1rozw_step6.mp4", text: "" },
            { type: "video", src: "zad1/zad1rozw_step7.mp4", text: "" },
            { type: "video", src: "zad1/zad1rozw_step8.mp4", text: "" },
            { type: "video", src: "zad1/zad1rozw_step9.mp4", text: "" }
        ],
        solutionInteractive: function (container) {
            widgetOsLiczbowa(container);
        }
    },
    {
        question: '<b>Zadanie 2.</b> <br><br> Liczba <img src="zad2/zad2.png" style="width:160px;height:75px;display:inline-block;vertical-align:middle;"> jest równa:',
        answers: ["A. 5<sup>4</sup>", "B. 5<sup>-4</sup>", "C. 5<sup>0.25</sup>", "D. 5<sup>-0.25</sup>"],
        // Rachunek: (⁵√5 · ⅕)⁻⁵ = (5^(1/5) · 5⁻¹)⁻⁵ = (5^(−4/5))⁻⁵ = 5⁴ → A.
        // (ostatnia klatka filmiku pokazuje błędnie 5⁻⁴ — do przerenderowania, patrz todo.md)
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "Stopień pierwiastka jest jak mianownik w wykładniku, a ⅕ = 5⁻¹. Wykładnik −5 możesz włączyć do nawiasu (do każdego z czynników) i takie tam.",
        formulasPage: 5,
        solutionText: null,
        solutionTextMore: "Krok po kroku: <br><br> <span class='mathText'> ⁵√5 = 5<sup>1/5</sup>, &nbsp; ⅕ = 5<sup>−1</sup> <br><br> (5<sup>1/5</sup> · 5<sup>−1</sup>)<sup>−5</sup> = (5<sup>1/5 − 1</sup>)<sup>−5</sup> = (5<sup>−4/5</sup>)<sup>−5</sup> = 5<sup>(−4/5)·(−5)</sup> = <b>5<sup>4</sup></b> </span> <br><br> czyli odp. A.",
        solutionStepByStep: [
            { type: "video", src: "zad2/zad2rozw_step1.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step2.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step3.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step4.mp4", text: "Opuszczamy nawias, więc wykładnik -5 musimy wymnożyć przez wykładniki obu potęg." },
            { type: "video", src: "zad2/zad2rozw_step5.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step6.mp4", text: "5⁻¹⁺⁵ = 5⁴, czyli odpowiedź A (na końcu filmu błędny zapis 5⁻⁴)." },
        ],
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 3.</b> <br><br> Wykaż, że liczba 𝟐<sup>𝟏𝟎𝟎</sup> + 𝟒<sup>𝟒𝟗</sup> + 𝟏𝟔<sup>𝟐𝟒</sup> jest podzielna przez 𝟐𝟏.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Żeby wykazać podzielność przez <b>21</b>, będziemy rozkładać tę liczbę na czynniki, czyli wyciągać coś przed nawias aby powstało: <b>... · 21</b>",
        formulasPage: 5,
        solutionText: "Wszystkie składniki zapisujemy jako potęgi dwójki i wyciągamy najmniejszą z nich przed nawias — w nawiasie zostaje <b>21</b>.",
        solutionTextMore: "<span class='mathText'><b> 2<sup>100</sup> + 4<sup>49</sup> + 16<sup>24</sup> = 2<sup>100</sup> + 2<sup>98</sup> + 2<sup>96</sup> <br> = 2<sup>96</sup> · (2<sup>4</sup> + 2<sup>2</sup> + 1) <br> = 2<sup>96</sup> · (16 + 4 + 1) = 2<sup>96</sup> · 21</b></span>  &nbsp;<- ta liczba jest podzielna przez <b>21</b>, co należało wykazać.",
        solutionStepByStep: [
            { type: "video", src: "zad3/zad3rozw_step1.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step2.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step3.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step4.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step5.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step6.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step7.mp4", text: "" },
            { type: "video", src: "zad3/zad3rozw_step8.mp4", text: "liczba c * 21 jest podzielne przez 21 (c - cokolwiek całkowitego)" }
        ],
        solutionInteractive: null
    },
    {
        question: "<b>Zadanie 4.</b> <br><br> Dla każdej dodatniej liczby rzeczywistej <b>x</b> i dla każdej dodatniej liczby rzeczywistej <b>y</b> wartość wyrażenia <b>log<sub>7</sub> x + 6 log<sub>7</sub> y</b> jest równa wartości wyrażenia:",
        answers: ["A. log<sub>7</sub> (<sup>x</sup>&frasl;<sub>y<sup>6</sup>)</sub>", "B. log<sub>7</sub> (xy)<sup>6</sup>", "C. log<sub>7</sub>(6xy)", "D. log<sub>7</sub>(xy<sup>6</sup>)"],
        correctAnswerIndex: 3,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj z własności logarytmów: <b>log<sub>a</sub>(x) + log<sub>a</sub>(y) = log<sub>a</sub>(x·y)</b> oraz <b>log<sub>a</sub>(x<sup>b</sup>) = b·log<sub>a</sub>(x)</b>",
        formulasPage: 5,
        solutionText: "<span class='mathText'>log<sub>7</sub> x + 6 log<sub>7</sub> y = log<sub>7</sub> x + log<sub>7</sub> y<sup>6</sup> = <b>log<sub>7</sub>(xy<sup>6</sup>)</b></span> — odpowiedź <b>D</b>.",
        solutionTextMore: "Najpierw „chowamy\" 6 do logarytmu: <span class='mathText'>6 log<sub>7</sub> y = log<sub>7</sub> y<sup>6</sup></span> (własność log<sub>a</sub> x<sup>b</sup> = b·log<sub>a</sub> x, czytana od prawej). <br><br> Potem sumę logarytmów o tej samej podstawie zamieniamy na logarytm iloczynu: <span class='mathText'>log<sub>7</sub> x + log<sub>7</sub> y<sup>6</sup> = log<sub>7</sub>(x·y<sup>6</sup>)</span>.",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: "<b>Zadanie 5.</b> <br><br> Pani Aniela wpłaciła do banku kwotę <b>60 000 zł</b> na lokatę dwuletnią. Po każdym rocznym okresie oszczędzania bank doliczał odsetki w wysokości 𝑝% w skali roku od kwoty bieżącego kapitału znajdującego się na lokacie – zgodnie z procentem składanym. Na koniec okresu oszczędzania kwota na tej lokacie była równa <b> 67 925,76 zł </b> wraz z odsetkami (bez uwzględniania podatków). <br><br> Oprocentowanie lokaty w skali roku było równe:",
        answers: ["A. 6%", "B. 6,4%", "C. 6,5%", "D. 7%"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Korzystamy z wzoru na procent składany: <b>P = P<sub>0</sub> · (1 + r)<sup>n</sup></b>",
        formulasPage: 10,
        solutionText: "Podstawiamy do wzoru na procent składany: <span class='mathText'>60 000 · (1 + p)<sup>2</sup> = 67 925,76</span>, stąd <span class='mathText'>(1 + p)<sup>2</sup> = 1,132096</span>, czyli <span class='mathText'>1 + p = 1,064</span> i <b>p = 6,4%</b> — odpowiedź <b>B</b>.",
        solutionTextMore: "<span class='mathText'>(1 + p)<sup>2</sup> = 67 925,76 / 60 000 = 1,132096 <br><br> 1 + p = √1,132096 = 1,064 <br><br> p = 0,064 = <b>6,4%</b></span> <br><br> Warto zauważyć, że wystarczyło sprawdzić odpowiedzi: 60 000 · 1,064² = 67 925,76 zł. ✓",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetProcentSkladany(container);
        }
    },
    {
        question: '<b>Zadanie 6.</b> <br><br> Dla każdej liczby rzeczywistej 𝑥 różnej od (−1), 0 oraz 1 wartość wyrażenia' +
        '<img src="zad6/zad6.png" style="height:50px;"> <br>' +
        'jest równa wartości wyrażenia:'
        ,
        answers: ['A. <img src="zad6/zad6odp1.png" style="height:50px;">', 'B. <img src="zad6/zad6odp2.png" style="height:50px;">', 'C. <img src="zad6/zad6odp3.png" style="height:50px;">', 'D. <img src="zad6/zad6odp4.png" style="height:40px;">'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Dzielenie przez ułamek to mnożenie przez jego odwrotność. Rozłóż też mianownik: <b>x² − 1 = (x − 1)(x + 1)</b> i skróć, co się da.",
        formulasPage: 7,
        solutionText: "Zamieniamy dzielenie na mnożenie przez odwrotność i skracamy: <span class='mathText'><sup>x</sup>&frasl;<sub>(x−1)(x+1)</sub> · <sup>(x+1)</sup>&frasl;<sub>3x²</sub> = <b><sup>1</sup>&frasl;<sub>3x(x−1)</sub> = <sup>1</sup>&frasl;<sub>3x²−3x</sub></b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "Po kolei: <br><br> 1. Mianownik pierwszego ułamka rozkładamy ze wzoru skróconego mnożenia: <span class='mathText'>x² − 1 = (x − 1)(x + 1)</span>. <br><br> 2. Dzielenie zamieniamy na mnożenie przez odwrotność: <span class='mathText'>· <sup>(x+1)</sup>&frasl;<sub>3x²</sub></span>. <br><br> 3. Skracamy (x + 1) oraz jedno x: zostaje <span class='mathText'><sup>1</sup>&frasl;<sub>3x(x−1)</sub></span>, czyli po wymnożeniu mianownika <span class='mathText'><sup>1</sup>&frasl;<sub>3x²−3x</sub></span>. <br><br> Założenia x ≠ −1, 0, 1 gwarantują, że nic po drodze nie dzieliło przez zero.",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 7.</b> <br><br> Para liczb <b>x = -1</b> i <b>y = 6</b> jest rozwiązaniem układu równań:<br>' +
                '<img src="zad7/zad7.png"> <br>' +
                'gdzie <i>a</i> oraz <i>b</i> są liczbami rzeczywistymi.<br><br>' +
                'Wartość wyrażenia <i>a·b</i> jest równa:',
        answers: ['A. -2', 'B. -0,5', 'C. 0,5', 'D. 2'],
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "Podstaw podane wartości x i y do obu równań, oblicz a i b, a następnie ich iloczyn.",
        formulasPage: null,
        solutionText: "Po podstawieniu x = −1, y = 6: z pierwszego równania <span class='mathText'>−a + 18 = 20</span>, więc <b>a = −2</b>; z drugiego <span class='mathText'>−1 + 6b = 5</span>, więc <b>b = 1</b>. Zatem <b>a·b = −2</b> — odpowiedź <b>A</b>.",
        solutionTextMore: "<span class='mathText'>a·(−1) + 3·6 = 20 <br> −a + 18 = 20 <br> −a = 2 <br> <b>a = −2</b> <br><br> (−1) + b·6 = 5 <br> 6b = 6 <br> <b>b = 1</b> <br><br> a·b = (−2)·1 = <b>−2</b></span>",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 8.</b> <br><br> Rozwiąż równanie:<br>' +
                  '<img src="zad8/zad8.png"> <br>' +
                  'Zapisz konieczne założenie i obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 3,
        selfScore: true,
        hint: "Zacznij od określenia dziedziny (mianowniki ≠ 0). Zauważ, że <b>2x − 2 = 2(x − 1)</b> — oba mianowniki znikną po pomnożeniu przez 2(x − 1).",
        formulasPage: null,
        solutionText: "Założenie: <b>x ≠ 1</b>. Po pomnożeniu obu stron przez <span class='mathText'>2(x − 1)</span> dostajemy <span class='mathText'>2(x + 3) = x</span>, czyli <b>x = −6</b> (należy do dziedziny).",
        solutionTextMore: "<span class='mathText'>2x − 2 = 2(x − 1)</span>, więc dziedzina: <b>x ≠ 1</b>. <br><br> <span class='mathText'><sup>x+3</sup>&frasl;<sub>x−1</sub> = <sup>x</sup>&frasl;<sub>2(x−1)</sub> &nbsp;&nbsp;| · 2(x−1) <br><br> 2(x + 3) = x <br> 2x + 6 = x <br> <b>x = −6</b></span> <br><br> −6 ≠ 1, więc rozwiązaniem równania jest <b>x = −6</b>.",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 9.</b> <br><br> Rozwiąż nierówność:<br>' +
                '<span class="mathText">x(x - 6) ≤ 7</span><br>' +
                'Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Przenieś wszystkie wyrazy na jedną stronę, rozwiąż równanie kwadratowe, naszkicuj parabolę i odczytaj, gdzie nierówność jest spełniona.",
        formulasPage: 7,
        solutionText: "Po uporządkowaniu: <span class='mathText'>x² − 6x − 7 ≤ 0</span>. Miejsca zerowe: <b>x = −1</b> i <b>x = 7</b>, ramiona paraboli w górę, więc rozwiązaniem jest przedział <b>⟨−1, 7⟩</b>.",
        solutionTextMore: "<span class='mathText'>x² − 6x − 7 ≤ 0 <br><br> Δ = 36 + 28 = 64, &nbsp; √Δ = 8 <br> x₁ = (6 − 8)/2 = −1, &nbsp; x₂ = (6 + 8)/2 = 7 <br><br></span> Współczynnik przy x² jest dodatni → parabola ma ramiona w górę → wartości ≤ 0 przyjmuje <b>między</b> miejscami zerowymi: <b>x ∈ ⟨−1, 7⟩</b>.",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetNierownoscKwadratowa(container);
        }
    },
    {
        question: '<b>Zadanie 10.</b> <br><br> Funkcja <b>f</b> jest określona następująco:<br><br>' +
                  '<img src="zad10/zad10.png"> <br>' +
                  'Wykres funkcji <i class="mathText"> y = f(x) </i> przedstawiono w kartezjańskim układzie współrzędnych (𝑥, 𝑦) na rysunku poniżej'+
                  '<img src="zad10/zad10rys.png"> <br>' +
                  'Uzupełnij zdania. Wpisz odpowiednie przedziały w wykropkowanych miejscach, aby zdania były prawdziwe.<br><br>' +
                  '1. Dziedziną funkcji <b>f</b> jest przedział …<br>' +
                  '2. Zbiorem wartości funkcji <b>f</b> jest przedział …<br>' +
                  '3. Zbiorem wszystkich argumentów, dla których funkcja <b>f</b> przyjmuje wartości ujemne, jest przedział …<br>' +
                  '4. Zbiorem wszystkich argumentów, dla których funkcja <b>f</b> przyjmuje największą wartość, jest przedział …',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: true,
        hint: "Dziedzina to wszystkie x, dla których wykres istnieje (uwaga na kółko otwarte przy x = −4). Zbiór wartości odczytasz z osi y. Wartości ujemne = fragmenty wykresu POD osią x.",
        formulasPage: null,
        solutionText: "1. Dziedzina: <b>(−4, 4⟩</b>. &nbsp; 2. Zbiór wartości: <b>⟨−1, 3⟩</b>. &nbsp; 3. Wartości ujemne dla <b>x ∈ (1, 3)</b>. &nbsp; 4. Największą wartość (3) funkcja przyjmuje dla <b>x ∈ (−4, −2⟩</b>.",
        solutionTextMore: "1. Wykres zaczyna się w x = −4 (kółko otwarte → −4 nie należy) i kończy w x = 4 (kropka pełna → 4 należy): dziedzina <b>(−4, 4⟩</b>. <br><br> 2. Najniższy punkt wykresu to y = −1 (w x = 2), najwyższy to y = 3: zbiór wartości <b>⟨−1, 3⟩</b>. <br><br> 3. Pod osią x wykres jest między x = 1 a x = 3 (w obu tych punktach f(x) = 0, więc ich nie zaliczamy): <b>(1, 3)</b>. <br><br> 4. Wartość 3 (największa) jest przyjmowana na całym poziomym fragmencie: <b>(−4, −2⟩</b>.",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetFunkcjaPrzedzialami(container);
        }
    },
    {
        question: '<b>Zadanie 11.</b> <br><br> Miejscem zerowym funkcji liniowej <i>f</i> jest liczba 2, a punkt przecięcia wykresu funkcji <i>f</i> z osią <i>Oy</i> ma współrzędne (0, 4).<br><br>' +
                  '<img src="zad11/zad11.png"> <br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Współczynnik kierunkowy prostej, która jest wykresem funkcji <i>f</i>, jest równy −2.", answer: true },
            { text: "Pole trójkąta ograniczonego osiami układu współrzędnych oraz wykresem funkcji <i>f</i> jest równe 8.", answer: false }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Wyznacz wzór funkcji z dwóch punktów: (2, 0) i (0, 4). Trójkąt ma wierzchołki (0,0), (2,0), (0,4) — jego pole to połowa iloczynu przyprostokątnych.",
        formulasPage: null,
        solutionText: "f(x) = ax + 4 i f(2) = 0, więc 2a + 4 = 0, czyli <b>a = −2</b> (zdanie 1: <b>P</b>). Pole trójkąta: <span class='mathText'>½ · 2 · 4 = <b>4</b></span>, a nie 8 (zdanie 2: <b>F</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 12.</b> <br><br> W układzie współrzędnych wykresem funkcji kwadratowej <b>f</b> jest parabola, której wierzchołkiem jest punkt (3, 0). ' +
                  'Ta parabola przechodzi przez punkt (0, -9).<br><br>' +
                  '<b>Zadanie 12.1.</b> <br><br>' +
                  'Funkcja <b>f</b> jest malejąca w przedziale:<br>',
        answers: ['A. (-∞, 0⟩', 'B. (-∞, 3⟩', 'C. ⟨0, +∞)', 'D. ⟨3, +∞)'],
        correctAnswerIndex: 3,
        maxScore: 1,
        selfScore: false,
        hint: "Punkt (0, −9) leży PONIŻEJ wierzchołka (3, 0) — jakie muszą być ramiona paraboli? Funkcja kwadratowa zmienia monotoniczność dokładnie w wierzchołku.",
        formulasPage: 7,
        solutionText: "Parabola przechodzi przez punkt leżący poniżej wierzchołka, więc ma ramiona skierowane <b>w dół</b>. Taka funkcja rośnie do wierzchołka i maleje od niego, czyli jest malejąca w przedziale <b>⟨3, +∞)</b> — odpowiedź <b>D</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetParabola(container);
        }
    },
    {
        question: '<b>Zadanie 12.2.</b> <br><br> Dana jest ta sama funkcja <i>f</i> (parabola o wierzchołku (3, 0), przechodząca przez punkt (0, -9)).<br><br>' +
                  'Wzór funkcji <i>f</i> zapisano w dwóch spośród poniższych odpowiedzi. <b>Wybierz je obie.</b>',
        type: "multiSelect",
        answers: [
            'A. f(x) = -x² - 9',
            'B. f(x) = -(x - 3)²',
            'C. f(x) = -(x + 3)²',
            'D. f(x) = -x² + 6x - 9',
            'E. f(x) = -x² - 6x + 9',
            'F. f(x) = -x² - 6x - 9'
        ],
        correctAnswerIndices: [1, 3],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Wierzchołek (p, q) = (3, 0) → postać kanoniczna f(x) = a(x − 3)². Punkt (0, −9) daje a = −1. Drugi poprawny wzór to ta sama funkcja po rozwinięciu nawiasu.",
        formulasPage: 7,
        solutionText: "Postać kanoniczna: <span class='mathText'>f(x) = a(x − 3)²</span>; z f(0) = −9 mamy 9a = −9, czyli a = −1, więc <b>f(x) = −(x − 3)²</b> (odp. <b>B</b>). Po rozwinięciu: <span class='mathText'>−(x² − 6x + 9) = <b>−x² + 6x − 9</b></span> (odp. <b>D</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 12.3.</b> <br><br> Funkcja kwadratowa <b>g</b> jest określona za pomocą funkcji <b>f</b> następująco: <b> g(x) = f(x) - 1. </b> <br><br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Funkcja <i>g</i> ma jedno miejsce zerowe.", answer: false },
            { text: "W układzie współrzędnych osią symetrii wykresu funkcji <i>g</i> jest prosta x = 3.", answer: true }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "g to wykres f przesunięty o 1 w dół: g(x) = −(x − 3)² − 1. Jaka jest największa wartość g? Czy przesunięcie w dół zmienia oś symetrii?",
        formulasPage: 7,
        solutionText: "g(x) = −(x − 3)² − 1 ma wierzchołek (3, −1) i ramiona w dół, więc największa wartość to −1 < 0 — funkcja <b>nie ma</b> miejsc zerowych (zdanie 1: <b>F</b>). Przesunięcie pionowe nie zmienia osi symetrii: nadal x = 3 (zdanie 2: <b>P</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 13.</b> <br><br> Funkcja logarytmiczna <i>f</i> jest określona wzorem f(x) = log<sub>6</sub>x dla każdej dodatniej liczby rzeczywistej x.<br><br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Wartość funkcji <i>f</i> dla argumentu 36 jest równa 6.", answer: false },
            { text: "Funkcja <i>f</i> jest rosnąca.", answer: true }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "log₆36 to wykładnik, do którego trzeba podnieść 6, żeby dostać 36. Funkcja log<sub>a</sub>x jest rosnąca, gdy a > 1.",
        formulasPage: 5,
        solutionText: "<span class='mathText'>f(36) = log₆36 = <b>2</b></span> (bo 6² = 36), a nie 6 — zdanie 1: <b>F</b>. Podstawa 6 > 1, więc logarytm jest funkcją rosnącą — zdanie 2: <b>P</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 14.</b> <br><br> Ciąg (a<sub>n</sub>) jest określony wzorem a<sub>n</sub> = 3·(-1)<sup>n</sup> + 10 dla każdej liczby naturalnej n ≥ 1.<br><br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Ciąg (a<sub>n</sub>) jest geometryczny.", answer: false },
            { text: "Suma ośmiu początkowych kolejnych wyrazów ciągu (a<sub>n</sub>) jest równa 80.", answer: true }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Wypisz kilka pierwszych wyrazów: a₁ = 7, a₂ = 13, a₃ = 7, ... Czy iloraz kolejnych wyrazów jest stały? Ile wynosi suma jednej pary (7 + 13)?",
        formulasPage: 9,
        solutionText: "Wyrazy to na przemian 7 i 13: <span class='mathText'>13/7 ≠ 7/13</span>, więc iloraz nie jest stały — ciąg <b>nie jest</b> geometryczny (zdanie 1: <b>F</b>). Suma ośmiu wyrazów to cztery pary (7 + 13): <span class='mathText'>4 · 20 = <b>80</b></span> (zdanie 2: <b>P</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 15.</b> <br><br> Trzywyrazowy ciąg (5m, 4 + 2m, m) jest arytmetyczny, gdy liczba m jest równa:<br>',
        answers: ['A. -4', 'B. -1', 'C. 1', 'D. 4'],
        correctAnswerIndex: 3,
        maxScore: 1,
        selfScore: false,
        hint: "Warunek na ciąg arytmetyczny: wyraz środkowy jest średnią arytmetyczną wyrazów sąsiednich: <b>2·(4 + 2m) = 5m + m</b>.",
        formulasPage: 9,
        solutionText: "Z warunku ciągu arytmetycznego: <span class='mathText'>2(4 + 2m) = 5m + m</span>, czyli <span class='mathText'>8 + 4m = 6m</span>, stąd <b>m = 4</b> — odpowiedź <b>D</b>. (Ciąg: 20, 12, 4 — różnica r = −8.)",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetCiagArytmetyczny(container);
        }
    },
    {
        question: '<b>Zadanie 16.</b> <br><br> Dany jest ciąg geometryczny (a<sub>n</sub>) określony dla każdej liczby naturalnej n ≥ 1, w którym a<sub>2</sub> = 1/6 oraz a<sub>3</sub> = 1/9.<br><br>' +
              'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
              'Piąty wyraz ciągu (a<sub>n</sub>) jest równy:',
        answers: ['A. 1/15', 'B. 2/27', 'C. 4/81', 'D. 8/243'],
        correctAnswerIndex: 2,
        maxScore: 1,
        selfScore: false,
        hint: "Najpierw iloraz: q = a₃/a₂. Potem a₅ = a₃ · q².",
        formulasPage: 10,
        solutionText: "<span class='mathText'>q = a₃/a₂ = (1/9)·(6/1) = 2/3</span>. Zatem <span class='mathText'>a₅ = a₃ · q² = (1/9)·(4/9) = <b>4/81</b></span> — odpowiedź <b>C</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 17.</b> <br><br> Dany jest trójkąt prostokątny ABC, w którym |AC| = √15 i |BC| = 8. Na przyprostokątnej AB leży taki punkt D, że |BD| = 6.<br><br>' +
                '<img src="zad17/zad17.png"> <br><br>' +
                '<b>Zadanie 17.1.</b> <br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Sinus kąta ostrego ABC jest równy:',
        answers: ['A. 1/2', 'B. 7/8', 'C. √15/4', 'D. √15/8'],
        correctAnswerIndex: 3,
        maxScore: 1,
        selfScore: false,
        hint: "Sinus = przyprostokątna naprzeciw kąta / przeciwprostokątna. Naprzeciw kąta przy B leży bok AC, a przeciwprostokątną jest BC = 8.",
        formulasPage: 11,
        solutionText: "Kąt prosty jest przy A, więc przeciwprostokątna to <b>BC = 8</b>. Naprzeciw kąta ABC leży przyprostokątna AC = √15, zatem <span class='mathText'>sin(∠ABC) = <b>√15/8</b></span> — odpowiedź <b>D</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 17.2.</b> <br><br> Dany jest ten sam trójkąt.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Tangens kąta ostrego ADC jest równy:',
        answers: ['A. √15', 'B. 1/2', 'C. 7/8', 'D. √15/8'],
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "Najpierw oblicz AB z twierdzenia Pitagorasa (AB² + AC² = BC²), potem AD = AB − BD. Tangens = przyprostokątna naprzeciw / przyprostokątna przy kącie.",
        formulasPage: 11,
        solutionText: "Z Pitagorasa: <span class='mathText'>|AB| = √(8² − (√15)²) = √49 = 7</span>, więc <span class='mathText'>|AD| = 7 − 6 = 1</span>. W trójkącie ACD (prostokątnym przy A): <span class='mathText'>tg(∠ADC) = |AC|/|AD| = √15/1 = <b>√15</b></span> — odpowiedź <b>A</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 18.</b> <br><br> Kąt o mierze α jest <u>rozwarty</u> oraz sin α = √3/4.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Cosinus kąta o mierze α jest równy:',
        answers: ['A. -√13/4', 'B. -1/2', 'C. 1/2', 'D. √13/4'],
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj z jedynki trygonometrycznej sin²α + cos²α = 1 oraz z faktu, że dla kąta rozwartego cos α < 0.",
        formulasPage: 12,
        solutionText: "Z jedynki trygonometrycznej: <span class='mathText'>cos²α = 1 − 3/16 = 13/16</span>, więc <span class='mathText'>cos α = ±√13/4</span>. Kąt jest rozwarty, więc cosinus jest ujemny: <b>cos α = −√13/4</b> — odpowiedź <b>A</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetKoloTrygonometryczne(container);
        }
    },
    {
        question: '<b>Zadanie 19.</b> <br><br> W trapezie prostokątnym ABCD dłuższa podstawa AB ma długość 7,5. Krótsza przekątna AC ma długość równą 6 i dzieli trapez na dwa trójkąty prostokątne.<br><br>' +
                '<img src="zad19/zad19.png"> <br>' +
                'Oblicz pole trapezu ABCD. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: true,
        hint: "W trójkącie ABC (prostokątnym przy C) oblicz BC z Pitagorasa. Kąty CAB i DCA są naprzemianległe (DC ∥ AB) — wykorzystaj to w trójkącie ACD do wyznaczenia wysokości AD i podstawy DC.",
        formulasPage: 20,
        solutionText: "|BC| = √(7,5² − 6²) = 4,5. Z podobieństwa kątów: |AD| = 3,6 i |DC| = 4,8. Pole: <span class='mathText'>P = ½ · (7,5 + 4,8) · 3,6 = <b>22,14</b></span>.",
        solutionTextMore: "1. Trójkąt ABC jest prostokątny przy C: <span class='mathText'>|BC| = √(7,5² − 6²) = √20,25 = 4,5</span>. <br><br> 2. W tym trójkącie: <span class='mathText'>sin(∠CAB) = 4,5/7,5 = 0,6</span> oraz <span class='mathText'>cos(∠CAB) = 6/7,5 = 0,8</span>. <br><br> 3. DC ∥ AB, więc ∠DCA = ∠CAB (kąty naprzemianległe). W trójkącie ACD (prostokątnym przy D): <br> <span class='mathText'>|AD| = |AC| · sin(∠DCA) = 6 · 0,6 = 3,6</span> (wysokość trapezu), <br> <span class='mathText'>|DC| = |AC| · cos(∠DCA) = 6 · 0,8 = 4,8</span> (krótsza podstawa). <br><br> 4. <span class='mathText'>P = ½ (a + b) · h = ½ (7,5 + 4,8) · 3,6 = ½ · 12,3 · 3,6 = <b>22,14</b></span>.",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 20.</b> <br><br> Dany jest okrąg o środku w punkcie S i promieniu 6. Miara kąta wpisanego ACB jest równa 60°.<br><br>' +
                '<img src="zad20/zad20.png"> <br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Długość łuku AB, na którym oparty jest kąt wpisany ACB, jest równa:',
        answers: ['A. 2π', 'B. 4π', 'C. 6π', 'D. 12π'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Kąt środkowy oparty na tym samym łuku jest DWA razy większy od kąta wpisanego. Długość łuku to odpowiedni ułamek całego obwodu 2πr.",
        formulasPage: 19,
        solutionText: "Kąt środkowy ASB = 2 · 60° = 120°, czyli ⅓ pełnego kąta. Długość łuku: <span class='mathText'>⅓ · 2π · 6 = <b>4π</b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetKatWpisany(container);
        }
    },


    /* ============================================================
       ZADANIA 21-30 — zgodne z oryginalnym arkuszem CKE (treści
       i odpowiedzi przekazane przez autora). Tabela w zad 29:
       patrz todo.md (odtworzona pod wyniki z klucza).
       ============================================================ */
    {
        question: '<b>Zadanie 21.</b> <br><br> W kartezjańskim układzie współrzędnych (x, y) punkty <b>A = (−2, −1)</b> oraz <b>C = (3, 4)</b> są przeciwległymi wierzchołkami kwadratu ABCD.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Długość boku kwadratu ABCD jest równa:',
        answers: ['A. 5', 'B. 10', 'C. 5√2', 'D. √10'],
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "AC to przekątna kwadratu. Policz ją ze wzoru na długość odcinka, a potem skorzystaj z zależności: przekątna = bok · √2.",
        formulasPage: 22,
        solutionText: "<span class='mathText'>|AC| = √(5² + 5²) = 5√2</span>, a bok kwadratu to przekątna podzielona przez √2: <b>a = 5</b> — odpowiedź <b>A</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 22.</b> <br><br> W kartezjańskim układzie współrzędnych (x, y) dana jest prosta <i>k</i> o równaniu <span class="mathText">y = −7x + 3</span>. Prosta <i>l</i> jest równoległa do prostej <i>k</i> i przecina oś Oy w punkcie (0, 6). Punkt o współrzędnych (1, p) należy do prostej <i>l</i>.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Liczba p jest równa:',
        answers: ['A. (−4)', 'B. (−1)', 'C. 5/7', 'D. 7'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Proste równoległe mają ten sam współczynnik kierunkowy. Punkt (0, 6) od razu daje wyraz wolny prostej l.",
        formulasPage: 24,
        solutionText: "Prosta l: <span class='mathText'>y = −7x + 6</span>, więc <span class='mathText'>p = −7 · 1 + 6 = <b>−1</b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 23.</b> <br><br> W kartezjańskim układzie współrzędnych (x, y) dane są cztery okręgi o równaniach:<br><br>' +
                '<span class="mathText">o₁: (x − 1)² + (y − 2)² = 1</span><br>' +
                '<span class="mathText">o₂: (x + 1)² + (y + 2)² = 9</span><br>' +
                '<span class="mathText">o₃: (x − 3)² + (y − 4)² = 4</span><br>' +
                '<span class="mathText">o₄: (x + 3)² + (y + 4)² = 16</span><br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Okręgiem, który nie ma żadnego punktu wspólnego z osiami układu współrzędnych (x, y), jest:',
        answers: ['A. o₁', 'B. o₂', 'C. o₃', 'D. o₄'],
        correctAnswerIndex: 2,
        maxScore: 1,
        selfScore: false,
        hint: "Okrąg o środku (a, b) i promieniu r nie dotyka osi, gdy |a| > r oraz |b| > r. Sprawdź każdy okrąg po kolei.",
        formulasPage: 24,
        solutionText: "o₃ ma środek (3, 4) i promień 2: odległości od osi (3 i 4) są większe od promienia, więc <b>o₃</b> nie dotyka żadnej z osi — odpowiedź <b>C</b>. (o₁ jest styczny do osi Oy, o₂ i o₄ przecinają osie.)",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 24.</b> <br><br> Podstawą ostrosłupa prawidłowego czworokątnego jest kwadrat o boku długości 4. Ściana boczna tego ostrosłupa jest nachylona do płaszczyzny podstawy pod takim kątem α, że <span class="mathText">tg α = 3</span>.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Wysokość tego ostrosłupa jest równa:',
        answers: ['A. 3', 'B. 6', 'C. 6√2', 'D. 12'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Kąt nachylenia ściany bocznej leży w trójkącie: wysokość ostrosłupa H i połowa boku podstawy (2). tg α = H / 2.",
        formulasPage: 27,
        solutionText: "<span class='mathText'>tg α = H / (a/2)</span>, czyli <span class='mathText'>3 = H / 2</span>, stąd <b>H = 6</b> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 25.</b> <br><br> Długości trzech krawędzi wychodzących z jednego wierzchołka prostopadłościanu są trzema kolejnymi parzystymi liczbami naturalnymi. Najdłuższa krawędź tego prostopadłościanu ma długość p.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Objętość tego prostopadłościanu jest równa:',
        answers: ['A. p³ − 3p² + 2p', 'B. p³ + 3p² + 2p', 'C. p³ − 6p² − 8p', 'D. p³ − 6p² + 8p'],
        correctAnswerIndex: 3,
        maxScore: 1,
        selfScore: false,
        hint: "Kolejne parzyste liczby różnią się o 2, więc krawędzie to p − 4, p − 2 oraz p. Wymnóż.",
        formulasPage: 26,
        solutionText: "<span class='mathText'>V = (p − 4)(p − 2)p = (p² − 6p + 8)p = <b>p³ − 6p² + 8p</b></span> — odpowiedź <b>D</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 26.</b> <br><br> Objętość stożka o wysokości 2 jest równa 8π. Oblicz miarę kąta rozwarcia tego stożka. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Z wzoru V = ⅓πr²h wyznacz promień podstawy. Kąt rozwarcia to 2× kąt między wysokością a tworzącą: tg(α/2) = r / h.",
        formulasPage: 27,
        solutionText: "<span class='mathText'>⅓ · πr² · 2 = 8π → r² = 12 → r = 2√3</span>. Dalej <span class='mathText'>tg(α/2) = r/h = 2√3/2 = √3</span>, więc α/2 = 60° i kąt rozwarcia <b>α = 120°</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 27.</b> <br><br> Wszystkich liczb naturalnych pięciocyfrowych <u>nieparzystych</u>, w których zapisie dziesiętnym występują wyłącznie cyfry 0, 1, 2, 3 (np. 12303, 11111), jest:',
        answers: ['A. 32', 'B. 384', 'C. 512', 'D. 576'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Reguła mnożenia: pierwsza cyfra nie może być zerem, ostatnia musi być nieparzysta (1 albo 3), środkowe trzy — dowolne z czterech cyfr.",
        formulasPage: 28,
        solutionText: "<span class='mathText'>3 · 4 · 4 · 4 · 2 = <b>384</b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 28.</b> <br><br> Dane są dwa zbiory: <b>C = {1, 2, 3, 4, 5, 6}</b> oraz <b>D = {7, 8, 9, 10}</b>. Losujemy jedną liczbę ze zbioru C, a następnie losujemy jedną liczbę ze zbioru D.<br><br>' +
                'Oblicz prawdopodobieństwo zdarzenia A polegającego na tym, że wylosujemy liczby, których iloczyn będzie podzielny przez 4. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Wszystkich par jest 6 · 4 = 24. Przejrzyj liczby z D: przy 8 iloczyn zawsze dzieli się przez 4; przy 7 i 9 musi pomóc liczba z C; przy 10 wystarczy, że liczba z C jest parzysta.",
        formulasPage: 29,
        solutionText: "|Ω| = 24. Sprzyjające: z 8 — każde c (6 par); z 7 i 9 — tylko c = 4 (2 pary); z 10 — c parzyste: 2, 4, 6 (3 pary). Razem 11, więc <span class='mathText'><b>P(A) = 11/24</b></span>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 29.</b> <br><br> Do szkolnego koła czytelniczego należy 50 uczniów. Opiekun koła zebrał dane dotyczące liczby książek przeczytanych przez tych uczniów w listopadzie 2024 roku. W poniższej tabeli przedstawiono wyniki zebrane przez opiekuna.<br><br>' +
                '<table class="data-table"><tr><th>Liczba przeczytanych książek</th><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>' +
                '<tr><th>Liczba uczniów</th><td>5</td><td>8</td><td>12</td><td>13</td><td>12</td></tr></table><br>' +
                'Uzupełnij zdania. Wpisz odpowiednie liczby w wykropkowanych miejscach, aby zdania były prawdziwe.<br><br>' +
                '1. Średnia arytmetyczna liczby przeczytanych książek w tej grupie uczniów jest równa …<br>' +
                '2. Mediana liczby przeczytanych książek w tej grupie uczniów jest równa …',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Średnia: suma (liczba książek · liczba uczniów) podzielona przez 50. Mediana przy 50 uczniach to średnia 25. i 26. wyniku po uporządkowaniu.",
        formulasPage: 31,
        solutionText: "1. Średnia: <span class='mathText'>(4·5 + 5·8 + 6·12 + 7·13 + 8·12) / 50 = 319/50 = <b>6,38</b></span>. <br> 2. Mediana: 25. wynik to 6, a 26. to 7, więc <span class='mathText'>(6 + 7)/2 = <b>6,5</b></span>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 30.</b> <br><br> Rozważamy wszystkie prostopadłościany ABCDEFGH, w których krawędź AE jest 3 razy dłuższa od krawędzi AB, a suma długości wszystkich dwunastu krawędzi prostopadłościanu jest równa 48. Niech P(x) oznacza funkcję pola powierzchni całkowitej takiego prostopadłościanu w zależności od długości x krawędzi AB.<br><br>' +
                'Wyznacz wzór i dziedzinę funkcji P. Oblicz długość x krawędzi AB tego z rozważanych prostopadłościanów, którego pole powierzchni całkowitej jest największe. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: true,
        hint: "Oznacz AB = x, AE = 3x, a trzecią krawędź (AD) wyznacz z sumy krawędzi: 4(x + AD + 3x) = 48. Pole całkowite to suma pól trzech par ścian; maksimum funkcji kwadratowej jest w wierzchołku.",
        formulasPage: 7,
        solutionText: "Z sumy krawędzi: <span class='mathText'>AD = 12 − 4x</span>, stąd <span class='mathText'><b>P(x) = −26x² + 96x</b></span> dla <span class='mathText'><b>x ∈ (0, 3)</b></span>. Maksimum w wierzchołku: <span class='mathText'>x = 96/52 = <b>24/13</b></span>.",
        solutionTextMore: "Krawędzie: <span class='mathText'>AB = x, AE = 3x, AD = y</span>. Suma: <span class='mathText'>4(x + y + 3x) = 48 → y = 12 − 4x</span>; warunek y > 0 daje dziedzinę <span class='mathText'>x ∈ (0, 3)</span>. <br><br> <span class='mathText'>P(x) = 2xy + 2·x·3x + 2·y·3x = 6x² + 8xy = 6x² + 8x(12 − 4x) = <b>−26x² + 96x</b></span>. <br><br> Ramiona w dół, więc największa wartość w wierzchołku: <span class='mathText'>x = −96 / (2·(−26)) = <b>24/13</b></span> (należy do dziedziny).",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetProstopadloscian(container);
        }
    }
];
