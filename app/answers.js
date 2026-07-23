// app/answers.js — normalizacja wpisów fillIn i odsłanianie poprawnej
// odpowiedzi (helpery używane przez app/render.js i app/steps.js).

// Normalizacja odpowiedzi wpisywanych ręcznie (typ fillIn): bez spacji i bez
// różnic zapisu — nawiasy przedziałów ⟨ ⟩ oraz klawiaturowe < > sprowadzamy
// do [ ], minus typograficzny do zwykłego, średnik do przecinka. Dodatkowo
// wycinamy znaki zmiennej/przynależności (x, y, E/∈), żeby "x∈(-4,4]" czy
// "y ∈ [-1,3]" pasowało do samego przedziału z klucza — żadna poprawna
// odpowiedź w danych ich nie zawiera, więc usunięcie z obu stron jest bezpieczne.
// Obie strony porównania (wpis ucznia i wzorzec z danych) przechodzą przez tę samą funkcję.
function normalizeAnswer(s) {
    let wynik = (s || "")
        .replace(/\s+/g, "")
        .replace(/[−–]/g, "-")
        .replace(/[⟨<]/g, "[")
        .replace(/[⟩>]/g, "]")
        .replace(/;/g, ",")
        .replace(/[xye∈]/gi, "")
        .toLowerCase();
    // Zbędne zera na końcu części dziesiętnej: "6,50" ≡ "6,5", "7,0" ≡ "7".
    // Tylko gdy CAŁY wpis jest pojedynczą liczbą dziesiętną — w przedziale
    // typu "(-4,40]" przecinek rozdziela końce i nie wolno go ruszać.
    if (/^-?\d+[,.]\d*$/.test(wynik)) {
        wynik = wynik.replace(/0+$/, "").replace(/[,.]$/, "");
    }
    return wynik;
}

function markCorrectAnswer(exercise) {
    const button = exercise.querySelector(".answers-container button.hiddenCorrect");
    if (button) {
        button.classList.add("correct");
    }
}
