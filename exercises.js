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

UWAGA (2026-07-04): zadania 21-31 NIE pochodzą z oryginalnego arkusza
(MMAP-P0-100-2412) — środowisko nie miało dostępu do PDF-a CKE. Są to spójne
matematycznie zadania w stylu CKE pokrywające brakujące działy (stereometria,
geometria analityczna, statystyka, kombinatoryka, prawdopodobieństwo,
optymalizacja). Do podmiany na oryginały — patrz todo.md.
*/

const exercises = [
    {
        question: "<b>Zadanie 1.</b> <br><br> Liczby 𝑥₁ i 𝑥₂ są różnymi rozwiązaniami równania |𝑥 + 4| = 7. Suma 𝑥₁ + 𝑥₂ jest równa:",
        answers: ["A. (−14)", "B. (−8)", "C. 3", "D. 8"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Z wartości bezwzględnej czyli |takich nawiasów| zawsze wyjdzie wartość nieujemna, czyli: |7| = 7 oraz |-7| = 7. Co więc musi stać zamiast x aby wychodziło podobnie jak w tych przykładach?",
        formulasPage: 4,
        solutionText: "Geometrycznie: |𝑥 + 4| = 7 to wszystkie liczby odległe o <b>7</b> od liczby <b>−4</b>, czyli 𝑥₁ = 3 i 𝑥₂ = −11. Suma: <b>3 + (−11) = −8</b> — odpowiedź <b>B</b>.",
        solutionTextMore: "po opuszczeniu nawiasów są dwie możliwości: <br><br> <span class='mathText'> 1. <br>  x + 4 = 7 <br> x = 7 - 4 <br> <b> x = 3 </b>  <br><br> 2. <br> x + 4 = -7 <br> x = -7 - 4  <br> <b> x = -11</b> <br><br>  <b> 3 - 11 = -8 </b> </span><br> czyli odp B.<br><br>",
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
        solutionText: "<span class='mathText'>(⁵√5 · ⅕)<sup>−5</sup> = (5<sup>1/5</sup> · 5<sup>−1</sup>)<sup>−5</sup> = 5<sup>−1</sup> · 5<sup>5</sup> = 5<sup>4</sup></span> — odpowiedź <b>A</b>.",
        solutionTextMore: "Krok po kroku: <br><br> <span class='mathText'> ⁵√5 = 5<sup>1/5</sup>, &nbsp; ⅕ = 5<sup>−1</sup> <br><br> (5<sup>1/5</sup> · 5<sup>−1</sup>)<sup>−5</sup> = (5<sup>1/5 − 1</sup>)<sup>−5</sup> = (5<sup>−4/5</sup>)<sup>−5</sup> = 5<sup>(−4/5)·(−5)</sup> = <b>5<sup>4</sup></b> </span> <br><br> czyli odp. A.",
        solutionStepByStep: [
            { type: "video", src: "zad2/zad2rozw_step1.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step2.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step3.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step4.mp4", text: "Opuszczamy nawias, więc wykładnik -5 musimy wymnożyć przez wykładniki obu potęg." },
            { type: "video", src: "zad2/zad2rozw_step5.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step6.mp4", text: "Z reguły aʳ · aˢ = aʳ⁺ˢ mamy 5⁻¹⁺⁵ = 5⁴, czyli odpowiedź A. (Na końcu filmu wkradł się błędny zapis 5⁻⁴ — poprawna jest odpowiedź A: 5⁴.)" },
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
        answers: ["A. log<sub>7</sub> (<sup>x</sup>&frasl;<sub>y<sup>6</sup>)</sub>", "B. log<sub>7</sub> ((xy)<sup>6</sup>)", "C. log<sub>7</sub>(6xy)", "D. log<sub>7</sub>(xy<sup>6</sup>)"],
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
        question: '<b>Zadanie 12.1.</b> <br><br> W układzie współrzędnych wykresem funkcji kwadratowej <b>f</b> jest parabola, której wierzchołkiem jest punkt (3, 0). ' +
                  'Ta parabola przechodzi przez punkt (0, -9).<br><br>' +
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
        question: '<b>Zadanie 12.2.</b> <br><br> W układzie współrzędnych wykresem funkcji kwadratowej <i>f</i> jest parabola, której wierzchołkiem jest punkt (3, 0). ' +
                  'Ta parabola przechodzi przez punkt (0, -9).<br><br>' +
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
       ZADANIA 21-31 — ZAMIENNIKI W STYLU CKE (patrz komentarz na górze
       pliku i todo.md: do podmiany na oryginały z arkusza).
       ============================================================ */
    {
        question: '<b>Zadanie 21.</b> <br><br> W ostrosłupie prawidłowym czworokątnym wysokość ostrosłupa ma długość 3, a krawędź podstawy ma długość 4.<br><br>' +
              'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
              'Pole powierzchni bocznej tego ostrosłupa jest równe:',
        answers: ['A. 24', 'B. 8√13', 'C. 16√13', 'D. 48'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Wysokość ściany bocznej znajdź z twierdzenia Pitagorasa: łączy się z wysokością ostrosłupa (3) i połową krawędzi podstawy (2). Potem policz pole jednego trójkąta i pomnóż przez 4.",
        formulasPage: 27,
        solutionText: "Wysokość ściany bocznej: <span class='mathText'>h = √(3² + 2²) = √13</span>. Pole jednej ściany: <span class='mathText'>½ · 4 · √13 = 2√13</span>, a całej powierzchni bocznej: <span class='mathText'>4 · 2√13 = <b>8√13</b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 22.</b> <br><br> Dany jest graniastosłup prawidłowy sześciokątny, w którym krawędź podstawy ma długość 4, a wysokość jest równa 6.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Pole powierzchni całkowitej tego graniastosłupa jest równe:',
        answers: ['A. 24√3 + 144', 'B. 48√3 + 144', 'C. 48√3 + 96', 'D. 96√3'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Pole sześciokąta foremnego o boku a: <b>P = (3√3/2)·a²</b> (to 6 trójkątów równobocznych). Do tego 6 prostokątnych ścian bocznych a × h. Nie zapomnij o DWÓCH podstawach.",
        formulasPage: 27,
        solutionText: "Podstawa: <span class='mathText'>P = (3√3/2) · 16 = 24√3</span>, dwie podstawy: 48√3. Ściany boczne: <span class='mathText'>6 · 4 · 6 = 144</span>. Razem: <b>48√3 + 144</b> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 23.</b> <br><br> W kartezjańskim układzie współrzędnych (x, y) dane są punkty <b>A = (−2, 5)</b> oraz <b>B = (4, −3)</b>.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Długość odcinka AB jest równa:',
        answers: ['A. 2√7', 'B. √52', 'C. 10', 'D. 100'],
        correctAnswerIndex: 2,
        maxScore: 1,
        selfScore: false,
        hint: "Wzór na długość odcinka: <b>|AB| = √((x<sub>B</sub> − x<sub>A</sub>)² + (y<sub>B</sub> − y<sub>A</sub>)²)</b>. Przy okazji: trójkąt 6-8-10 to wielokrotność trójki pitagorejskiej 3-4-5.",
        formulasPage: 22,
        solutionText: "<span class='mathText'>|AB| = √((4 − (−2))² + (−3 − 5)²) = √(6² + (−8)²) = √(36 + 64) = √100 = <b>10</b></span> — odpowiedź <b>C</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 24.</b> <br><br> Prosta <i>k</i> ma równanie <span class="mathText">y = 2x − 3</span>. Prosta <i>l</i> jest prostopadła do prostej <i>k</i> i przechodzi przez punkt <b>P = (4, 1)</b>.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Prosta <i>l</i> ma równanie:',
        answers: ['A. y = -½x + 3', 'B. y = -½x - 1', 'C. y = 2x - 7', 'D. y = -2x + 9'],
        correctAnswerIndex: 0,
        maxScore: 1,
        selfScore: false,
        hint: "Proste są prostopadłe, gdy iloczyn ich współczynników kierunkowych wynosi −1: <b>a₁ · a₂ = −1</b>. Wyraz wolny wyznacz podstawiając punkt P.",
        formulasPage: 24,
        solutionText: "Warunek prostopadłości: <span class='mathText'>2 · a = −1</span>, więc <span class='mathText'>a = −½</span>. Z punktu P: <span class='mathText'>1 = −½ · 4 + b</span>, czyli <span class='mathText'>b = 3</span>. Prosta l: <b>y = −½x + 3</b> — odpowiedź <b>A</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 25.</b> <br><br> Średnia arytmetyczna zestawu danych: <span class="mathText">3, 5, x, 9, 11</span> jest równa 7.<br><br>' +
                'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Liczba x jest równa 7.", answer: true },
            { text: "Mediana tego zestawu danych jest równa 9.", answer: false }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Suma pięciu liczb to 5 · 7 = 35 — stąd x. Mediana to środkowa liczba PO uporządkowaniu zestawu rosnąco.",
        formulasPage: 32,
        solutionText: "<span class='mathText'>3 + 5 + x + 9 + 11 = 35</span>, więc <b>x = 7</b> (zdanie 1: <b>P</b>). Po uporządkowaniu: 3, 5, 7, 9, 11 — środkową liczbą jest 7, a nie 9 (zdanie 2: <b>F</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 26.</b> <br><br> Ze zbioru cyfr <b>{1, 2, 3, 4, 5}</b> tworzymy liczby trzycyfrowe o <u>różnych</u> cyfrach.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Wszystkich takich liczb jest:',
        answers: ['A. 10', 'B. 60', 'C. 120', 'D. 125'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Reguła mnożenia: pierwszą cyfrę wybierasz na 5 sposobów, drugą (musi być inna) na 4, trzecią na 3.",
        formulasPage: 28,
        solutionText: "<span class='mathText'>5 · 4 · 3 = <b>60</b></span> — odpowiedź <b>B</b>. (Gdyby cyfry mogły się powtarzać, byłoby 5³ = 125.)",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 27.</b> <br><br> Rzucamy dwa razy symetryczną sześcienną kostką do gry.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Prawdopodobieństwo, że suma oczek w obu rzutach będzie równa 5, wynosi:',
        answers: ['A. 1/12', 'B. 1/9', 'C. 1/6', 'D. 5/36'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Wszystkich wyników jest 6 · 6 = 36. Wypisz pary, które dają sumę 5: (1,4), (2,3), ...",
        formulasPage: 29,
        solutionText: "Sprzyjają pary: (1,4), (2,3), (3,2), (4,1) — jest ich 4. <span class='mathText'>P = 4/36 = <b>1/9</b></span> — odpowiedź <b>B</b>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 28.</b> <br><br> Funkcja wykładnicza <i>f</i> jest określona wzorem <span class="mathText">f(x) = 3 · (½)<sup>x</sup></span> dla każdej liczby rzeczywistej x.<br><br>' +
                'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Wykres funkcji <i>f</i> przechodzi przez punkt (0, 3).", answer: true },
            { text: "Funkcja <i>f</i> jest rosnąca.", answer: false }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Policz f(0) — każda liczba w potędze 0 daje 1. Funkcja a<sup>x</sup> jest malejąca, gdy 0 < a < 1.",
        formulasPage: null,
        solutionText: "<span class='mathText'>f(0) = 3 · (½)⁰ = 3 · 1 = 3</span>, więc punkt (0, 3) należy do wykresu (zdanie 1: <b>P</b>). Podstawa ½ ∈ (0, 1), więc funkcja jest <b>malejąca</b>, a nie rosnąca (zdanie 2: <b>F</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 29.</b> <br><br> Przekątna sześcianu ma długość <span class="mathText">4√3</span>.<br><br>' +
                'Oblicz pole powierzchni całkowitej oraz objętość tego sześcianu. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Przekątna sześcianu o krawędzi a ma długość <b>a√3</b>. Porównaj to z 4√3.",
        formulasPage: 27,
        solutionText: "Z <span class='mathText'>a√3 = 4√3</span> mamy <b>a = 4</b>. Pole całkowite: <span class='mathText'>P = 6a² = 6 · 16 = <b>96</b></span>, objętość: <span class='mathText'>V = a³ = <b>64</b></span>.",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 30.</b> <br><br> Rozpatrujemy wszystkie prostokąty, których obwód jest równy 36.<br><br>' +
                'Wyznacz wymiary tego z rozpatrywanych prostokątów, którego pole jest największe. Oblicz to pole. Zapisz obliczenia.',
        type: "open",
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: true,
        hint: "Oznacz jeden bok przez a — wtedy drugi to 18 − a (bo połowa obwodu wynosi 18). Pole P(a) = a(18 − a) to funkcja kwadratowa: jej największa wartość jest w wierzchołku.",
        formulasPage: 7,
        solutionText: "Boki: a oraz 18 − a. Pole: <span class='mathText'>P(a) = a(18 − a) = −a² + 18a</span> — parabola z ramionami w dół, maksimum w wierzchołku <span class='mathText'>a = 18/2 = 9</span>. Największe pole ma <b>kwadrat 9 × 9</b>, a jego pole to <b>81</b>.",
        solutionTextMore: "Obwód: <span class='mathText'>2a + 2b = 36</span>, więc <span class='mathText'>b = 18 − a</span>, przy czym <span class='mathText'>a ∈ (0, 18)</span>. <br><br> <span class='mathText'>P(a) = a(18 − a) = −a² + 18a</span>. <br><br> Współczynnik przy a² jest ujemny, więc funkcja osiąga największą wartość w wierzchołku: <span class='mathText'>a<sub>w</sub> = −18/(2·(−1)) = 9</span>, wtedy <span class='mathText'>b = 18 − 9 = 9</span>. <br><br> <span class='mathText'>P(9) = 9 · 9 = <b>81</b></span>. Spośród prostokątów o stałym obwodzie największe pole ma kwadrat.",
        solutionStepByStep: null,
        solutionInteractive: function (container) {
            widgetProstokatPole(container);
        }
    },
    {
        question: '<b>Zadanie 31.</b> <br><br> Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.',
        type: "PF",
        answers: [],
        statements: [
            { text: "Liczba 25 jest pierwiastkiem równania log<sub>5</sub>x = 2.", answer: true },
            { text: "Wartość log<sub>2</sub>16 jest równa 4.", answer: true }
        ],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Sprawdź: czy log₅25 = 2? Do jakiej potęgi trzeba podnieść 2, żeby otrzymać 16?",
        formulasPage: 5,
        solutionText: "<span class='mathText'>log₅25 = 2</span>, bo 5² = 25 — liczba 25 spełnia równanie (zdanie 1: <b>P</b>). <span class='mathText'>log₂16 = 4</span>, bo 2⁴ = 16 (zdanie 2: <b>P</b>).",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    }
];
