// app/panels.js — pływające panele PDF: tablice wzorów i zasady oceniania
// (pokaż/schowaj, przeciąganie, zmiana rozmiaru) + openFormulasAtPage.

// Na telefonie panele PDF (<object>) i tak się nie renderują (Android nie
// osadza PDF-a), a przeciąganie/rozmiar nie mają sensu — więc zamiast panelu
// otwieramy PDF w NOWEJ KARCIE przeglądarki (podejście ustalone z Henrichem).
// noopener: bezpieczeństwo; nowa karta nie dostaje referencji do window.opener.
function otworzPdfWNowejKarcie(url) {
    if (url) window.open(url, "_blank", "noopener");
}

// Tablica wzorów: panel (kontener) + <object> z PDF-em w środku. Pokazywanie/
// chowanie działa na panelu, a etykieta przycisku w pasku jest z tym zsynchronizowana.
const tablicaPanel = document.getElementById("tablica-wzorow-panel");
const toggleTablicaButton = document.getElementById("toggle-tablica");

function showFormulasPanel() {
    // Na telefonie zamiast panelu — PDF w nowej karcie (patrz otworzPdfWNowejKarcie).
    if (czyTelefon()) {
        const tablica = document.getElementById("tablica-wzorow");
        otworzPdfWNowejKarcie((tablica && tablica.getAttribute("data")) || TABLICE_PDF);
        return;
    }
    tablicaPanel.style.display = "block";
    toggleTablicaButton.textContent = "▲ Schowaj tablice wzorów";
}
function hideFormulasPanel() {
    tablicaPanel.style.display = "none";
    toggleTablicaButton.textContent = "▼ Pokaż tablice wzorów";
}

toggleTablicaButton.addEventListener("click", function() {
    // Telefon: zawsze „otwórz w nowej karcie" (panel nie działa) — bez toggla.
    if (czyTelefon()) {
        showFormulasPanel();
        return;
    }
    const ukryta = tablicaPanel.style.display === "none" || tablicaPanel.style.display === "";
    if (ukryta) {
        showFormulasPanel();
    } else {
        hideFormulasPanel();
    }
});

// Krzyżyk w rogu tablicy wzorów po prostu ją chowa.
document.getElementById("tablica-close").addEventListener("click", hideFormulasPanel);

// Zasady oceniania: działa identycznie jak tablica wzorów, tylko po lewej
// stronie i bez podmieniania strony PDF-a (jeden dokument CKE z odpowiedziami).
const zasadyPanel = document.getElementById("zasady-oceniania-panel");
const toggleZasadyButton = document.getElementById("toggle-zasady");

function showGradingRules() {
    // Telefon: PDF zasad oceniania w nowej karcie zamiast panelu <object>.
    if (czyTelefon()) {
        const zasady = document.getElementById("zasady-oceniania");
        otworzPdfWNowejKarcie(zasady && zasady.getAttribute("data"));
        return;
    }
    zasadyPanel.style.display = "block";
    toggleZasadyButton.textContent = "▲ Schowaj zasady oceniania";
}
function hideGradingRules() {
    zasadyPanel.style.display = "none";
    toggleZasadyButton.textContent = "▼ Pokaż zasady oceniania";
}

toggleZasadyButton.addEventListener("click", function() {
    if (czyTelefon()) {
        showGradingRules();
        return;
    }
    const ukryte = zasadyPanel.style.display === "none" || zasadyPanel.style.display === "";
    if (ukryte) {
        showGradingRules();
    } else {
        hideGradingRules();
    }
});
document.getElementById("zasady-close").addEventListener("click", hideGradingRules);

// "Odblokowane" panele PDF: przeciąganie za górny pasek i zmiana rozmiaru za
// narożnik. Używamy pointer capture na uchwytach, bo <object> z PDF-em połyka
// zdarzenia myszy — bez capture przeciąganie urywałoby się nad dokumentem.
function makePanelDraggable(panel) {
    const uchwyt = panel.querySelector(".panel-uchwyt");
    const rozmiar = panel.querySelector(".panel-rozmiar");

    const topBar = document.getElementById("top-bar");

    uchwyt.addEventListener("pointerdown", (e) => {
        const r = panel.getBoundingClientRect();
        const dx = e.clientX - r.left;
        const dy = e.clientY - r.top;
        // Pasek uchwytu (a więc "chwyt" panelu) musi zostać w widocznym
        // viewportcie, żeby nie dało się go zgubić: u góry nie chowa się pod
        // top-barem, u dołu nie zjeżdża pod dolną krawędź ekranu (za pasek
        // zadań Windows), a w bok zostaje zawsze min. kawałek do złapania.
        const minTop = topBar ? topBar.getBoundingClientRect().bottom : 0;
        const uchwytH = uchwyt.offsetHeight || 46;
        const minWidoczne = 60; // ile px panelu musi zostać na ekranie w poziomie
        uchwyt.setPointerCapture(e.pointerId);
        const move = (ev) => {
            const szer = panel.getBoundingClientRect().width;
            let noweLeft = ev.clientX - dx;
            let noweTop = ev.clientY - dy;
            noweLeft = Math.min(Math.max(noweLeft, minWidoczne - szer), window.innerWidth - minWidoczne);
            noweTop = Math.min(Math.max(noweTop, minTop), window.innerHeight - uchwytH);
            panel.style.left = noweLeft + "px";
            panel.style.top = noweTop + "px";
            panel.style.right = "auto"; // od tej pory pozycjonujemy od lewej/góry
        };
        const up = () => {
            uchwyt.removeEventListener("pointermove", move);
            uchwyt.removeEventListener("pointerup", up);
            uchwyt.removeEventListener("pointercancel", up);
        };
        uchwyt.addEventListener("pointermove", move);
        uchwyt.addEventListener("pointerup", up);
        uchwyt.addEventListener("pointercancel", up);
    });

    rozmiar.addEventListener("pointerdown", (e) => {
        const r = panel.getBoundingClientRect();
        rozmiar.setPointerCapture(e.pointerId);
        const move = (ev) => {
            panel.style.width = Math.max(260, ev.clientX - r.left) + "px";
            panel.style.height = Math.max(200, ev.clientY - r.top) + "px";
        };
        const up = () => {
            rozmiar.removeEventListener("pointermove", move);
            rozmiar.removeEventListener("pointerup", up);
            rozmiar.removeEventListener("pointercancel", up);
        };
        rozmiar.addEventListener("pointermove", move);
        rozmiar.addEventListener("pointerup", up);
        rozmiar.addEventListener("pointercancel", up);
    });
}
makePanelDraggable(tablicaPanel);
makePanelDraggable(zasadyPanel);

function openFormulasAtPage(numerStrony) {
    // Telefon: otwórz PDF z tablicami wzorów na właściwej stronie w nowej karcie
    // (panel <object> nie działa na Androidzie).
    if (czyTelefon()) {
        otworzPdfWNowejKarcie(`${TABLICE_PDF}#page=${numerStrony}&toolbar=0`);
        return;
    }

    const tablica = document.getElementById("tablica-wzorow");

    // Tworzymy nowy <object> zamiast tylko zmieniać `data` (przeglądarkowy
    // podgląd PDF nie zawsze przeładowuje się po samej zmianie atrybutu).
    const nowyObject = document.createElement("object");
    nowyObject.id = "tablica-wzorow";
    nowyObject.type = "application/pdf";
    nowyObject.data = `${TABLICE_PDF}#page=${numerStrony}&toolbar=0`;

    // Zamieniamy stary <object> na nowy w panelu (styl bierze się z CSS #tablica-wzorow).
    tablica.parentNode.replaceChild(nowyObject, tablica);

    showFormulasPanel();
}
