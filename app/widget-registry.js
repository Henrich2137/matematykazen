// app/widget-registry.js - rejestr widżetów: exercises.json nie może
// przechowywać funkcji, więc pole solutionWidget to nazwa (string), a tu leży
// mapa nazwa → funkcja. Wymaga, żeby wszystkie pliki widgets/*.js były
// załadowane WCZEŚNIEJ (kolejność tagów <script> w template.html), dlatego ten
// plik ładuje się PO całym katalogu widgets/, mimo że leży w app/.
// Nowy widżet = nowy plik w widgets/ + wpis tutaj + tag <script>.
//
// LICENCJA: ten plik jest wolny (PolyForm Noncommercial, patrz LICENSE.md).
// Same widżety w widgets/ są zastrzeżone (widgets/LICENSE.md).
const WIDZETY = {
    widgetOsLiczbowa,
    widgetProcentSkladany,
    widgetOdsetkiSkladane,
    widgetRownanieIloczynowe,
    widgetNierownoscTrojmianu,
    widgetBilety,
    widgetLamana121,
    widgetLamana122,
    widgetLiniowaWspolczynniki,
    widgetLiniowaTangens,
    widgetPrzesuniecieParaboli,
    widgetKatyWOkregu,
    widgetProporcjeProste,
    widgetProsteRownolegle,
    widgetRzutPileczki,
    widgetNierownoscKwadratowa,
    widgetFunkcjaPrzedzialami,
    widgetParabola,
    widgetCiagArytmetyczny,
    widgetKoloTrygonometryczne,
    widgetKatWpisany,
    widgetProstopadloscian
};
