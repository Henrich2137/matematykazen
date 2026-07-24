// app/bootstrap.js — punkt wejścia strony (startSheet + komunikaty błędów +
// applySheetMeta) oraz chrome paska/menu „⋯" (menu, reset, widok punktów,
// pokaż wszystkie rozwiązania). Ładowany OSTATNI z bloku app/*, bo startSheet()
// woła loadExercises() i wiele funkcji zdefiniowanych w pozostałych plikach.

// Okienko "więcej opcji" (⋯): pokaż/schowaj po kliknięciu przycisku,
// zamknij po kliknięciu gdziekolwiek poza okienkiem.
const menuButton = document.getElementById("menu-button");
const barMenu = document.getElementById("bar-menu");
menuButton.addEventListener("click", (e) => {
    e.stopPropagation();
    barMenu.style.display = barMenu.style.display === "block" ? "none" : "block";
});
document.addEventListener("click", (e) => {
    if (barMenu.style.display === "block" && !barMenu.contains(e.target)) {
        barMenu.style.display = "none";
    }
});

// "Resetuj punktację": kasuje zapisany postęp i przeładowuje stronę — punkty,
// kolory odpowiedzi i wpisy wracają do zera jedną, wspólną drogą (świeży render).
document.getElementById("reset-scores").addEventListener("click", () => {
    if (!confirm(
        "Wyczyścić zapisane odpowiedzi i punkty? Tej operacji nie można cofnąć.\n\n" +
        "Jeśli w innej karcie trwa właśnie próbny egzamin na tym arkuszu, zostanie on też zakończony."
    )) return;
    try {
        localStorage.removeItem(KLUCZ_POSTEPU);
        localStorage.removeItem(KLUCZ_OCENIANIA); // reset kasuje też fazę „oceń się"
        localStorage.removeItem(KLUCZ_EGZAMINU); // ...i ewentualny trwający egzamin w innej karcie
    } catch (e) {}
    location.reload();
});

// Przełącznik widoku punktów (menu „⋯"): wszystko → tylko suma → nic → ...
const scoreSwitchButton = document.getElementById("score-switch-button");


scoreSwitchButton.addEventListener("click", () => {

    //potem można to podmienić na switch(scoreSwitchButton.innerHTML){}
    if(scoreSwitchButton.innerHTML == "widok punktów: wszystko"){

        scoreSwitchButton.innerHTML="widok punktów: tylko suma"

        const elements = document.getElementsByClassName('exercise-score');
        for (let el of elements) {
            el.style.display = "none";
        }
    }else if(scoreSwitchButton.innerHTML == "widok punktów: tylko suma"){

        scoreSwitchButton.innerHTML="widok punktów: nic"

        document.getElementById('total-score').style.display = "none";

    }else{
        scoreSwitchButton.innerHTML="widok punktów: wszystko"

        document.getElementById('total-score').style.display = "block";
        const elements = document.getElementsByClassName('exercise-score');
        for (let el of elements) {
            el.style.display = "block";
        }


    }

})

// Toggle „natychmiastowa poprawność" (menu ⋯): ustawienie GLOBALNE (localStorage,
// bez sufiksu arkusza — patrz app/state.js). ON = klik odpowiedzi zamkniętej od
// razu koloruje ramkę; OFF = dopiero po kliknięciu „sprawdź". body.reczne-sprawdzanie
// (dodawane w trybie OFF) odsłania przyciski „sprawdź wszystkie odpowiedzi".
const natychmiastowaToggle = document.getElementById("natychmiastowa-toggle");
function odswiezTrybPoprawnosci() {
    const on = czyNatychmiastowaPoprawnosc();
    document.body.classList.toggle("reczne-sprawdzanie", !on);
    if (natychmiastowaToggle) {
        natychmiastowaToggle.textContent = on
            ? "pokazuj poprawność od razu: tak"
            : "pokazuj poprawność od razu: nie";
    }
}
odswiezTrybPoprawnosci();
if (natychmiastowaToggle) {
    natychmiastowaToggle.addEventListener("click", () => {
        const on = czyNatychmiastowaPoprawnosc();
        try { localStorage.setItem(KLUCZ_NATYCHM_POPRAWNOSC, on ? "0" : "1"); } catch (e) {}
        odswiezTrybPoprawnosci();
    });
}

// „Sprawdź wszystkie odpowiedzi" (menu ⋯ + kopia w stopce arkusza): odsłania
// ocenę wszystkich zadań zamkniętych, które mają zaznaczoną, a jeszcze
// nieodsłoniętą odpowiedź (to samo, co ręczne kliknięcie każdego widocznego
// „sprawdź"). Pomija zadania bez zaznaczenia i już sprawdzone.
function sprawdzWszystkieOdpowiedzi() {
    oczekujaceSprawdzenia.forEach(z => {
        if (z.maZaznaczenie() && !z.czySprawdzone()) z.ocen();
    });
}
["sprawdz-wszystkie", "sprawdz-wszystkie-stopka"].forEach(id => {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener("click", sprawdzWszystkieOdpowiedzi);
});

// Wypełnia chrome strony (tytuł karty, meta description, tytuł w pasku, PDF
// zasad oceniania, domyślna strona tablicy wzorów) danymi z pola "meta"
// exercises.json — jedyne miejsce, gdzie template.html dowiaduje się, JAKI
// to arkusz (poza samymi zadaniami).
function applySheetMeta(meta) {
    if (!meta) return;
    if (meta.pageTitle) document.title = meta.pageTitle;
    if (meta.metaDescription) {
        const opis = document.querySelector('meta[name="description"]');
        if (opis) opis.setAttribute("content", meta.metaDescription);
    }
    const tytulEl = document.getElementById("exercises-sheet-title");
    if (tytulEl && meta.sheetTitle) tytulEl.textContent = meta.sheetTitle;
    if (meta.zasadyPdf) {
        // zasadyPdf jest ścieżką względną do folderu arkusza (jak media),
        // więc idzie przez mediaPath. encodeURI na wypadek spacji w nazwie.
        document.getElementById("zasady-oceniania").data = `${encodeURI(mediaPath(meta.zasadyPdf))}#toolbar=0`;
    }
    if (meta.tablicaPdfDefaultPage) {
        document.getElementById("tablica-wzorow").data =
            `${TABLICE_PDF}#page=${meta.tablicaPdfDefaultPage}&toolbar=0`;
    }
}

// Wspólny sposób pokazania komunikatu zamiast arkusza (pusta strona myli).
function pokazKomunikat(html) {
    const info = document.createElement("div");
    info.className = "blad-wczytywania";
    info.innerHTML = html;
    document.getElementById("exercises-wrapper").appendChild(info);
}

// Nieznany / brakujący / pusty ?arkusz= — to nie jest awaria serwera, tylko
// błędny link (np. wpisany ręcznie). Kierujemy użytkownika na stronę główną.
function pokazBladLinku() {
    pokazKomunikat(
        "<b>Błędny link.</b><br>" +
        "Nie znaleziono takiego arkusza. " +
        '<a href="index.html">Wróć do strony głównej</a> i wybierz arkusz z listy.'
    );
}

// Start strony: dane zadań przychodzą fetchem z matura/<SHEET_ID>/exercises.json
// (obiekt { meta, exercises } — patrz ARCHITECTURE.md). UWAGA: fetch nie
// działa z file:// — wtedy (i przy każdym innym niepowodzeniu) pokazujemy
// czytelny komunikat zamiast pustej strony.
async function startSheet() {
    // Brak parametru albo pusty ?arkusz= — bez fetchu, od razu błędny link.
    if (!SHEET_ID) {
        pokazBladLinku();
        return;
    }

    let odpowiedz;
    try {
        odpowiedz = await fetch(`matura/${SHEET_ID}/exercises.json`);
    } catch (blad) {
        // Brak odpowiedzi z serwera: najczęściej file:// (fetch zablokowany),
        // rzadziej padnięta sieć — to nie to samo co nieznany arkusz.
        pokazKomunikat(location.protocol === "file:"
            ? "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
              "Strona jest otwarta bezpośrednio z pliku (<code>file://</code>), a przeglądarka " +
              "blokuje wtedy wczytywanie danych. Uruchom ją przez lokalny serwer, np. " +
              "<code>npx serve</code> albo <code>python -m http.server</code> w folderze strony."
            : "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
              "Odśwież stronę; jeśli błąd wraca, sprawdź, czy plik exercises.json jest na serwerze. " +
              `<small>(${blad.message})</small>`);
        return;
    }

    // Serwer odpowiedział błędem (404 itp.) — nie ma folderu arkusza o tym id,
    // czyli ?arkusz= wskazuje na nieistniejący arkusz: błędny link.
    if (!odpowiedz.ok) {
        pokazBladLinku();
        return;
    }

    try {
        const dane = await odpowiedz.json();
        exercises = dane.exercises;
        applySheetMeta(dane.meta);
    } catch (blad) {
        pokazKomunikat(
            "<b>Nie udało się wczytać zadań (exercises.json).</b><br>" +
            "Odśwież stronę; jeśli błąd wraca, plik może być uszkodzony. " +
            `<small>(${blad.message})</small>`);
        return;
    }
    try {
        loadExercises();
    } catch (blad) {
        // loadExercises jest już odporne na błędy pojedynczych zadań, ale gdyby
        // padło wcześniej (np. brak #exercises-wrapper), nie zostawiamy pustej
        // strony — pokazujemy komunikat i sygnalizujemy błąd na belce diagnostycznej.
        console.error("Błąd renderowania arkusza", blad);
        pokazKomunikat(
            "<b>Nie udało się wyświetlić zadań.</b><br>" +
            "Odśwież stronę; jeśli błąd wraca, przekaż autorowi treść komunikatu z czerwonego paska na dole. " +
            `<small>(${blad && blad.message ? blad.message : blad})</small>`);
        if (window.__pokazBladStrony) window.__pokazBladStrony(blad, "loadExercises");
        return;
    }
    // Jeśli czas egzaminu minął, gdy karta była zamknięta — zakończ od razu
    // (tickExam ma warunek na wczytane zadania, teraz już spełniony).
    if (readExamState()) tickExam();
    // Faza „oceń się" po egzaminie (nie w trakcie egzaminu): odtwórz pływające
    // wskaźniki nieocenionych zadań otwartych, żeby przetrwały odświeżenie strony.
    else if (czyFazaOceniania()) pokazWskaznikiOtwarte();
}
startSheet();

// "Pokaż/schowaj wszystkie rozwiązania": przełącznik w pasku. Otwiera lub
// zamyka panel rozwiązania każdego zadania klikając jego własny przycisk
// (ta sama ścieżka co ręczne klikanie — kroki, filmy itd. działają normalnie).
// Pomijamy zadania będące już w docelowym stanie, więc ręcznie otwarte
// rozwiązania nie "mrugają" i nie zamykają się przy "pokaż wszystkie".
const showAllButton = document.getElementById("show-all-solutions");
let wszystkieOtwarte = false;
showAllButton.addEventListener("click", () => {
    wszystkieOtwarte = !wszystkieOtwarte;
    wszystkieRozwiazania.forEach(({ przycisk, panel, ma }) => {
        if (!ma) return;
        const otwarty = panel.style.display === "block";
        if (otwarty !== wszystkieOtwarte) przycisk.click();
    });
    showAllButton.textContent = wszystkieOtwarte
        ? "schowaj wszystkie rozwiązania"
        : "pokaż wszystkie rozwiązania";
});
