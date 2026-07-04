/*
co dodać jeszcze do exercisa?
{
type: "ABCD", // lub "PF" lub "closedFillGaps" lub "openFillGaps" lub "open"    selfScore już nie będzie potrzebne
number: 17, // numer zadania
numberSection: null, // null sprawia, że nie będzie traktowane jako wieloczęściowe, 0 to część główna, 1,2,... to części dodatkowe

}


*/



const maxTotalScore = 7; //to jest placeholder, jak będą wszystkie zadania to wpisze tu właścwą liczbe

// correctAnswerIndex: indeks poprawnej odpowiedzi w tablicy answers (0 = A, 1 = B, ...).
// -1 (lub brak pola) = zadanie otwarte / jeszcze niewypełnione — klik w odpowiedź
// jedynie przełącza znak "?" zamiast oceniać.
const exercises = [
    {
        question: "<b>Zadanie 1.</b> <br><br> Liczby 𝑥₁ i 𝑥₂ są różnymi rozwiązaniami równania |𝑥 + 4| = 7. Suma 𝑥₁ + 𝑥₂ jest równa:",
        answers: ["A. (−14)", "B. (−8)", "C. 3", "D. 8"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Z wartości bezwzględnej czyli |takich nawiasów| zawsze wyjdzie wartość nieujemna, czyli: |7| = 7 oraz |-7| = 7. Co więc musi stać zamiast x aby wychodziło podobnie jak w tych przykładach?",
        formulasPage: 4,
        solutionText: "",
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
            { type: "video", src: "zad1/zad1rozw_step9.mp4", text: "" },



        ],
        solutionInteractive: function (container) {
            container.innerHTML += `
                <canvas id="numberLine" width="500" height="100"></canvas> <br>

                <span class='mathText'>
                | 𝑥 + 
                <input type="number" id="aInput" value="4" oninput="drawNumberLine1(this)">
                | = 
                <input type="number" id="bInput" value="7" oninput="drawNumberLine1(this)">
                </span>
            `;

            drawNumberLine1(container.querySelector("#bInput")); // #aInput or #bInput whatever
        }
    },
    {
        question: '<b>Zadanie 2.</b> <br><br> Liczba <img src="zad2/zad2.png" style="width:160px;height:75px;display:inline-block;vertical-align:middle;"> jest równa:',
        answers: ["A. 5<sup>4</sup>", "B. 5<sup>-4</sup>", "C. 5<sup>0.25</sup>", "D. 5<sup>-0.25</sup>"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Stopień pierwiastaka jest jak mianownik w wykładniku. -5 możesz możesz włączyć do nawiasu (do każdego z czynników) i takie tam.",
        formulasPage: 5,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: [
            { type: "video", src: "zad2/zad2rozw_step1.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step2.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step3.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step4.mp4", text: "Opuszczamy nawias, więc wykładnik -5 musimy wymnożyć przez wykładniki obu potęg." },
            { type: "video", src: "zad2/zad2rozw_step5.mp4", text: "" },
            { type: "video", src: "zad2/zad2rozw_step6.mp4", text: "Mamy odpowiedź! To B." },
        ],
        solutionInteractive: null
        
    },
    {
        question: '<b>Zadanie 3.</b> <br><br> Wykaż, że liczba 𝟐<sup>𝟏𝟎𝟎</sup> + 𝟒<sup>𝟒𝟗</sup> + 𝟏𝟔<sup>𝟐𝟒</sup> jest podzielna przez 𝟐𝟏.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: true,
        hint: "Żeby wykazać podzielność przez <b>21</b>, będziemu rozłożyć tą liczbe na czynniki, czyli wyciągać coś przed nawias aby powstało: <b>... * 21</b>",
        formulasPage: 5,
        solutionText: "",
        solutionTextMore: "<b> 2<sup>100</sup> + 2<sup>98</sup> + 2<sup>96</sup> <br>2<sup>96</sup> * (2<sup>4</sup> + 2<sup>2</sup> + 2<sup>96</sup>) <br>2<sup>96</sup> * 21</b>  <- ta liczba jest podzielna przez <b>21</b>",
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
        hint: "Skorzystaj z własności logarytmów: <b>log<sub>a</sub>(x) + log<sub>a</sub>(y) = log<sub>a</sub>(x*y)</b> oraz <b>log<sub>a</sub>(x<sup>b</sup>) = b*log<sub>a</sub>(x)</b>",
        formulasPage: 5,
        solutionText: null,
        solutionTextMore: null,
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: "<b>Zadanie 5.</b> <br><br> Pani Aniela wpłaciła do banku kwotę <b>60 000 zł</b> na lokatę dwuletnią. Po każdym rocznym okresie oszczędzania bank doliczał odsetki w wysokości 𝑝% w skali roku od kwoty bieżącego kapitału znajdującego się na lokacie – zgodnie z procentem składanym. Na koniec okresu oszczędzania kwota na tej lokacie była równa <b> 67 925,76 zł </b> wraz z odsetkami (bez uwzględniania podatków). <br><br> Oprocentowanie lokaty w skali roku było równe:",
        answers: ["A. 6%", "B. 6,4%", "C. 6,5%", "D. 7%"],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Korzystamy z wzoru na procent składany: <b>P = P<sub>0</sub> * (1 + r)<sup>n</sup></b>",
        formulasPage: 10,
        solutionText: "Jak się podstawi dane wytłuszczone w tekście oraz 2 pod n do wzoru na procent składany to uzyskamy p. Tutaj warto dodać wykres eksponencjalny, próbowałem kiedyś, ale coś nie wyszło wtedy.",
        solutionTextMore: null,
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 6.</b> <br><br> Dla każdej liczby rzeczywistej 𝑥 różnej od (−1), 0 oraz 1 wartość wyrażenia' +
        '<img src="zad6/zad6.png" style="height:50px;"> <br>' +
        'jest równa wartości wyrażenia:'
        ,//Brzydki zapis matematyczny w html: <b> <sup>x</sup>&frasl;<sub>x<sup>2</sup> - 1<sub> : <sup>3x<sup>3</sup></sup>&frasl;<sub>x + 1<sub></b>
        answers: ['A. <img src="zad6/zad6odp1.png" style="height:50px;">', 'B. <img src="zad6/zad6odp2.png" style="height:50px;">', 'C. <img src="zad6/zad6odp3.png" style="height:50px;">', 'D. <img src="zad6/zad6odp4.png" style="height:40px;">'],
        correctAnswerIndex: 1,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj z własności logarytmów: <b>log<sub>a</sub>(x) + log<sub>a</sub>(y) = log<sub>a</sub>(x*y)</b> oraz <b>log<sub>a</sub>(x<sup>b</sup>) = b*log<sub>a</sub>(x)</b>",
        formulasPage: 5,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {//odtąd wszystko poniżej napisał chatgpt
        question: '<b>Zadanie 7.</b> <br><br> Para liczb <b>x = -1</b> i <b>y = 6</b> jest rozwiązaniem układu równań:<br>' +
                '<img src="zad7/zad7.png"> <br>' +
                'gdzie <i>a</i> oraz <i>b</i> są liczbami rzeczywistymi.<br><br>' +
                'Wartość wyrażenia <i>a·b</i> jest równa:',
        answers: ['A. -2', 'B. -0,5', 'C. 0,5', 'D. 2'],
        correctAnswerIndex: -1, // tu wpiszesz poprawną odpowiedź
        maxScore: 1,
        selfScore: false,
        hint: "Podstaw podane wartości x i y do obu równań, oblicz a i b, a następnie ich iloczyn.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 8.</b> <br><br> Rozwiąż równanie:<br>' +
                  '<img src="zad8/zad8.png"> <br>' +
                  'Zapisz konieczne założenie i obliczenia.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 3,
        selfScore: false,
        hint: "Zacznij od określenia dziedziny, następnie sprowadź obie strony do wspólnego mianownika i rozwiąż równanie.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 9.</b> <br><br> Rozwiąż nierówność:<br>' +
                '<span class="mathText">x(x - 6) ≤ 7</span><br>' +
                'Zapisz obliczenia.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Przenieś wszystkie wyrazy na jedną stronę, rozwiąż równanie kwadratowe, wyznacz przedziały i sprawdź, gdzie nierówność jest spełniona.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
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
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: false,
        hint: "Narysuj wykres funkcji z definicji, odczytaj dziedzinę, zbiór wartości oraz interesujące przedziały.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 11.</b> <br><br> Miejscem zerowym funkcji liniowej <i>f</i> jest liczba 2, a punkt przecięcia wykresu funkcji <i>f</i> z osią <i>Oy</i> ma współrzędne (0, 4).<br><br>' +
                  '<img src="zad11/zad11.png"> <br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.<br><br>' +
                  '1. Współczynnik kierunkowy prostej, która jest wykresem funkcji <i>f</i>, jest równy -2.<br>' +
                  '2. Pole trójkąta ograniczonego osiami układu współrzędnych oraz wykresem funkcji <i>f</i> jest równe 8.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj ze wzoru funkcji liniowej przez dwa punkty, a następnie oblicz pole trójkąta na podstawie współrzędnych przecięć z osiami.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 12.1.</b> <br><br> W układzie współrzędnych wykresem funkcji kwadratowej <b>f</b> jest parabola, której wierzchołkiem jest punkt (3, 0). ' +
                  'Ta parabola przechodzi przez punkt (0, -9).<br><br>' +
                  'Funkcja <b>f</b> jest malejąca w przedziale:<br>',
        answers: ['A. (-∞, 0]', 'B. (-∞, 3]', 'C. [0, +∞)', 'D. [3, +∞)'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Wykorzystaj położenie wierzchołka i kształt paraboli otwartej w dół.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 12.2.</b> <br><br> W układzie współrzędnych wykresem funkcji kwadratowej <i>f</i> jest parabola, której wierzchołkiem jest punkt (3, 0). ' +
                  'Ta parabola przechodzi przez punkt (0, -9).<br><br>' +
                  'Uzupełnij zdanie. Wybierz dwie właściwe odpowiedzi spośród oznaczonych literami A–F i wpisz je w wykropkowane miejsca.<br>' +
                  'Wzór funkcji <i>f</i> zapisano w odpowiedziach oznaczonych literami: … oraz …<br><br>' +
                  'A. f(x) = -x² - 9<br>' +
                  'B. f(x) = -(x - 3)²<br>' +
                  'C. f(x) = -(x + 3)²<br>' +
                  'D. f(x) = -x² + 6x - 9<br>' +
                  'E. f(x) = -x² - 6x + 9<br>' +
                  'F. f(x) = -x² - 6x - 9',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Podstaw dane punkty do ogólnego wzoru funkcji kwadratowej i sprawdź, które pasują.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 12.3.</b> <br><br> Funkcja kwadratowa <b>g</b> jest określona za pomocą funkcji <b>f</b> następująco: <b> g(x) = f(x) - 1. </b> <br><br>' +
                  'Oceń prawdziwość poniższych stwierdzeń. Wybierz <b>P</b>, jeśli stwierdzenie jest prawdziwe, albo <b>F</b> – jeśli jest fałszywe.<br><br>' +
                  '1. Funkcja <i>g</i> ma jedno miejsce zerowe.<br>' +
                  '2. W układzie współrzędnych osią symetrii wykresu funkcji <i>g</i> jest prosta x = 3.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Przesunięcie wykresu funkcji o 1 jednostkę w dół nie zmienia osi symetrii. Sprawdź liczbę miejsc zerowych nowej paraboli.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },    
    {
        question: '<b>Zadanie 13.</b> <br><br> Funkcja logarytmiczna <i>f</i> jest określona wzorem f(x) = log<sub>6</sub>x dla każdej dodatniej liczby rzeczywistej x.<br><br>' +
                  'Oceń prawdziwość stwierdzeń:<br>' +
                  '1. Wartość funkcji <i>f</i> dla argumentu 36 jest równa 6.<br>' +
                  '2. Funkcja <i>f</i> jest rosnąca.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Podstaw x=36 do definicji logarytmu, a następnie przypomnij sobie monotoniczność logarytmu przy podstawie > 1.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 14.</b> <br><br> Ciąg (a<sub>n</sub>) jest określony wzorem a<sub>n</sub> = 3·(-1)<sup>n</sup> + 10 dla każdej liczby naturalnej n ≥ 1.<br><br>' +
                  'Oceń prawdziwość stwierdzeń:<br>' +
                  '1. Ciąg (a<sub>n</sub>) jest geometryczny.<br>' +
                  '2. Suma ośmiu początkowych kolejnych wyrazów ciągu (a<sub>n</sub>) jest równa 80.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Rozważ, czy kolejne wyrazy powstają przez mnożenie przez stały współczynnik. Potem oblicz sumę pierwszych 8 wyrazów.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 15.</b> <br><br> Trzywyrazowy ciąg (5m, 4 + 2m, m) jest arytmetyczny, gdy liczba m jest równa:<br>',
        answers: ['A. -4', 'B. -1', 'C. 1', 'D. 4'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Warunek na ciąg arytmetyczny: drugi wyraz = średnia arytmetyczna pierwszego i trzeciego.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
    question: '<b>Zadanie 16.</b> <br><br> Dany jest ciąg geometryczny (a<sub>n</sub>) określony dla każdej liczby naturalnej n ≥ 1, w którym a<sub>2</sub> = 1/6 oraz a<sub>3</sub> = 1/9.<br><br>' +
              'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
              'Piąty wyraz ciągu (a<sub>n</sub>) jest równy:',
    answers: ['A. 1/15', 'B. 2/27', 'C. 4/81', 'D. 8/243'],
    correctAnswerIndex: -1,
    maxScore: 1,
    selfScore: false,
    hint: "Skorzystaj ze wzoru ogólnego ciągu geometrycznego: a<sub>n</sub> = a<sub>1</sub> · q<sup>n-1</sup>.",
    formulasPage: null,
    solutionText: "",
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
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj z definicji sinusa w trójkącie prostokątnym: sin(α) = przeciwprostokątna/przyprostokątna.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 17.2.</b> <br><br> Dany jest ten sam trójkąt.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Tangens kąta ostrego ADC jest równy:',
        answers: ['A. √15', 'B. 1/2', 'C. 7/8', 'D. √15/8'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Użyj definicji tangensa w trójkącie prostokątnym: tan(α) = przeciwległa/przyległa.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 18.</b> <br><br> Kąt o mierze α jest <u>rozwarty</u> oraz sin α = √3/4.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Cosinus kąta o mierze α jest równy:',
        answers: ['A. -√13/4', 'B. -1/2', 'C. 1/2', 'D. √13/4'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Skorzystaj z tożsamości trygonometrycznej sin²α + cos²α = 1 oraz faktu, że dla kąta rozwartgo cos α < 0.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 19.</b> <br><br> W trapezie prostokątnym ABCD dłuższa podstawa AB ma długość 7,5. Krótsza przekątna AC ma długość równą 6 i dzieli trapez na dwa trójkąty prostokątne.<br><br>' +
                '<img src="zad19/zad19.png"> <br>' +
                'Oblicz pole trapezu ABCD. Zapisz obliczenia.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 4,
        selfScore: false,
        hint: "Narysuj trapez, rozważ trójkąty prostokątne, wyznacz wysokość trapezu i oblicz pole ze wzoru P = (a+b)·h/2.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
        question: '<b>Zadanie 20.</b> <br><br> Dany jest okrąg o środku w punkcie S i promieniu 6. Miara kąta wpisanego ACB jest równa 60°.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Długość łuku AB, na którym oparty jest kąt wpisany ACB, jest równa:',
        answers: ['A. 2π', 'B. 4π', 'C. 6π', 'D. 12π'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Kąt wpisany oparty na łuku ma miarę równą połowie kąta środkowego. Oblicz długość łuku ze wzoru L = α/360° · 2πr.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
    },
    {
    question: '<b>Zadanie 21.</b> <br><br> W ostrosłupie prawidłowym czworokątnym wysokość ma długość 3, a krawędź podstawy ma długość 4.<br><br>' +
              'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
              'Pole powierzchni bocznej tego ostrosłupa jest równe:',
    answers: ['A. 24', 'B. 32', 'C. 48', 'D. 64'],
    correctAnswerIndex: -1,
    maxScore: 1,
    selfScore: false,
    hint: "Policz pole jednej ściany bocznej (trójkąta równoramiennego) i pomnóż razy cztery.",
    formulasPage: null,
    solutionText: "",
    solutionTextMore: "",
    solutionStepByStep: null,
    solutionInteractive: null
    // NOTE: klasyczne zadanie testowe wielokrotnego wyboru (jak 16,18,20).
    },
    {
        question: '<b>Zadanie 22.</b> <br><br> Dany jest graniastosłup prawidłowy sześciokątny o podstawie w postaci sześciokąta foremnego o boku długości 4 i wysokości 6.<br><br>' +
                'Dokończ zdanie. Wybierz właściwą odpowiedź spośród podanych.<br>' +
                'Pole powierzchni całkowitej tego graniastosłupa jest równe:',
        answers: ['A. 144√3', 'B. 192√3', 'C. 240√3', 'D. 288√3'],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Pole podstawy = (3√3/2)a², pole boczne = obwód·h. Dodaj dwa pola podstawy do pola bocznego.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: podobne do 21, zamknięte, ale bardziej skomplikowana geometria.
    },
    {
        question: '<b>Zadanie 23.</b> <br><br> Na rysunku przedstawiono fragment wykresu funkcji kwadratowej f.<br><br>' +
                '<img src="zad23/zad23.png"><br><br>' +
                'Na podstawie wykresu zapisz:<br>' +
                '1. wzór funkcji f,<br>' +
                '2. miejsca zerowe funkcji f.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Odczytaj miejsca zerowe i wierzchołek, a następnie zapisz wzór funkcji kwadratowej.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: zadanie otwarte, brak odpowiedzi A–D, obrazek (jak 19).
    },
    {
        question: '<b>Zadanie 24.</b> <br><br> Na rysunku przedstawiono fragment wykresu funkcji kwadratowej g.<br><br>' +
                '<img src="zad24/zad24.png"><br><br>' +
                'Na podstawie wykresu zapisz:<br>' +
                '1. współrzędne wierzchołka paraboli,<br>' +
                '2. zbiór wartości funkcji g.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Z wykresu odczytaj minimum lub maksimum paraboli i opisz zbiór wartości.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: otwarte, obrazek, podobne do 23.
    },
    {
        question: '<b>Zadanie 25.</b> <br><br> Wskaż rysunek, który przedstawia fragment wykresu funkcji wykładniczej f określonej wzorem f(x) = 3·(1/2)<sup>x</sup>.<br><br>' +
                '<img src="zad25/zad25.png">',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Rozpoznaj wykres funkcji malejącej wykładniczej, przechodzącej przez (0,3).",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: test graficzny – brak odpowiedzi tekstowych, wybór rysunku.
    },
    {
        question: '<b>Zadanie 26.</b> <br><br> Na rysunku przedstawiono fragment wykresu funkcji liniowej h.<br><br>' +
                '<img src="zad26/zad26.png"><br><br>' +
                'Na podstawie wykresu zapisz:<br>' +
                '1. współczynnik kierunkowy funkcji h,<br>' +
                '2. wzór funkcji h.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Z wykresu odczytaj przyrosty i wyznacz a, a potem wzór prostej.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: otwarte zadanie z obrazkiem.
    },
    {
        question: '<b>Zadanie 27.</b> <br><br> W tabeli podano niektóre wartości funkcji liniowej k.<br><br>' +
                '<img src="zad27/zad27.png"><br><br>' +
                'Na podstawie danych z tabeli zapisz:<br>' +
                '1. współczynnik kierunkowy funkcji k,<br>' +
                '2. wzór funkcji k.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Policz iloraz przyrostów Δy/Δx z tabeli i zapisz wzór y=ax+b.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: otwarte, dane w tabeli zamiast wykresu.
    },
    {
        question: '<b>Zadanie 28.</b> <br><br> Na rysunku przedstawiono fragment wykresu funkcji liniowej m.<br><br>' +
                '<img src="zad28/zad28.png"><br><br>' +
                'Na podstawie wykresu zapisz:<br>' +
                '1. współczynnik kierunkowy funkcji m,<br>' +
                '2. wzór funkcji m.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 2,
        selfScore: false,
        hint: "Odczytaj dwa punkty z wykresu i policz współczynnik kierunkowy, a potem b.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: otwarte, jak 26, ale inna funkcja.
    },
    {
        question: '<b>Zadanie 29.</b> <br><br> Wskaż rysunek, który przedstawia fragment wykresu funkcji logarytmicznej f określonej wzorem f(x) = log<sub>2</sub>x.<br><br>' +
                '<img src="zad29/zad29.png">',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Rozpoznaj wykres logarytmu: rosnący, przechodzący przez (1,0) i (2,1).",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: test graficzny, podobne do 25.
    },
    {
        question: '<b>Zadanie 30.</b> <br><br> Oceń prawdziwość poniższych stwierdzeń. Wybierz P, jeśli stwierdzenie jest prawdziwe, albo F – jeśli fałszywe.<br><br>' +
                '1. Liczba 25 jest pierwiastkiem równania log<sub>5</sub>x = 2.<br>' +
                '2. Wartość log<sub>2</sub>16 jest równa 4.',
        answers: [],
        correctAnswerIndex: -1,
        maxScore: 1,
        selfScore: false,
        hint: "Sprawdź, czy 25 spełnia równanie log₅x=2 i oblicz log₂16.",
        formulasPage: null,
        solutionText: "",
        solutionTextMore: "",
        solutionStepByStep: null,
        solutionInteractive: null
        // NOTE: zadanie typu P/F (jak 11,13,14,30).
    }

];