// Rejestr widżetów: exercises.json nie może przechowywać funkcji, więc pole
// solutionWidget to nazwa (string), a tu leży mapa nazwa → funkcja. Wymaga,
// żeby wszystkie pliki widgets/*.js były załadowane WCZEŚNIEJ (kolejność
// tagów <script> w template.html) — stąd _registry.js jest ostatnim plikiem
// katalogu. Nowy widżet = nowy plik w widgets/ + wpis tutaj.
const WIDZETY = {
    widgetOsLiczbowa,
    widgetProcentSkladany,
    widgetNierownoscKwadratowa,
    widgetFunkcjaPrzedzialami,
    widgetParabola,
    widgetCiagArytmetyczny,
    widgetKoloTrygonometryczne,
    widgetKatWpisany,
    widgetProstopadloscian
};
