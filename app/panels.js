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
// chowanie działa na panelu, a etykieta pozycji w panelu bocznym jest z tym
// zsynchronizowana. UWAGA: etykietę zmieniamy przez ustawEtykiete() (pisze do
// wewnętrznego <span class="etykieta">), NIE przez textContent całego przycisku
// — ten skasowałby ikonę SVG. Patrz komentarz w app/state.js.
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
    ustawEtykiete(toggleTablicaButton, "Schowaj tablicę wzorów");
}
function hideFormulasPanel() {
    tablicaPanel.style.display = "none";
    ustawEtykiete(toggleTablicaButton, "Otwórz tablicę wzorów");
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
    ustawEtykiete(toggleZasadyButton, "Schowaj zasady oceniania");
}
function hideGradingRules() {
    zasadyPanel.style.display = "none";
    ustawEtykiete(toggleZasadyButton, "Otwórz zasady oceniania");
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

    uchwyt.addEventListener("pointerdown", (e) => {
        const r = panel.getBoundingClientRect();
        const dx = e.clientX - r.left;
        const dy = e.clientY - r.top;
        // Pasek uchwytu (a więc "chwyt" panelu) musi zostać w widocznym
        // viewportcie, żeby nie dało się go zgubić: u dołu nie zjeżdża pod dolną
        // krawędź ekranu (za pasek zadań Windows), a w bok zostaje zawsze min.
        // kawałek do złapania. U góry ogranicza go WYŁĄCZNIE krawędź strony
        // (minTop = 0) — decyzja Henricha 2026-07-27: panel może wjechać na
        // wysokość logo i przejechać pod nim (logo ma z-index 10, panele 9, więc
        // panel schowa się POD prostokątem tła logo, a nie zasłoni go). Dawniej
        // klamp szedł od dolnej krawędzi #top-bara, którego już nie ma.
        const minTop = 0;
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

// Rozmiar strony tablicy wzorów w punktach PDF — wszystkie 36 stron mają ten sam
// (sprawdzone `pdfinfo`: 612.288 x 858.897 pt). Potrzebne, bo parametr
// `view=FitH,top` operuje we współrzędnych PDF-a, a nie w pikselach.
const TABLICE_STRONA_SZER_PT = 612.288;
const TABLICE_STRONA_WYS_PT = 858.897;

// Tryb dopasowania strony w panelu:
//   "FitH"  — do pełnej szerokości kartki (z marginesami),
//   "FitBH" — do samej treści, bez marginesów: tekst ~30% większy i w kadrze
//             mieści się mniej strony, więc przewijanie do wzoru w ogóle ma sens.
// Do porównania na żywo wystarczy zmienić tę jedną stałą. Marginesy w tablicy
// wzorów to ok. 72 pt z każdej strony, stąd TABLICE_STRONA_TRESC_SZER_PT.
const TABLICE_TRYB_WIDOKU = "FitH";
const TABLICE_STRONA_TRESC_SZER_PT = 468;

// Ile punktów strony widać w pionie w panelu przy widoku FitH (ten dopasowuje
// SZEROKOŚĆ strony do szerokości okna, więc skala wynika z samej szerokości).
// Gdy panelu nie da się zmierzyć (jest schowany albo jesteśmy na telefonie, gdzie
// PDF idzie do nowej karty) zwracamy 0 — wywołujący traktuje to jako „nie wiem".
function widocznaWysokoscTablicyPt() {
    const tablica = document.getElementById("tablica-wzorow");
    if (!tablica || !tablica.clientWidth || !tablica.clientHeight) return 0;
    const szerokoscWKadrzePt = TABLICE_TRYB_WIDOKU === "FitBH"
        ? TABLICE_STRONA_TRESC_SZER_PT
        : TABLICE_STRONA_SZER_PT;
    const pikseleNaPunkt = tablica.clientWidth / szerokoscWKadrzePt;
    return tablica.clientHeight / pikseleNaPunkt;
}

// Fragment URL-a PDF-a: strona plus — jeśli znamy pozycję wzoru — przewinięcie do
// niego. `yWzoru` to współrzędna w punktach liczona OD DOŁU strony (układ PDF),
// brana z transkryptu tablicy. `view=FitH,top` ustawia GÓRNĄ krawędź widoku, więc
// żeby wzór wypadł na środku okna, dokładamy połowę tego, co widać.
//
// UWAGA: gdy w kadrze mieści się cała strona (a przy domyślnym kształcie panelu —
// 28% szerokości na 80vh — właśnie tak jest), przewijać nie ma czego: `top`
// wychodzi wyżej niż górna krawędź strony i po przycięciu daje zwykły widok
// strony od góry. Kotwica zaczyna działać dopiero, gdy panel jest proporcjonalnie
// szerszy/niższy niż kartka.
function fragmentTablicy(numerStrony, yWzoru) {
    let fragment = `#page=${numerStrony}`;
    if (yWzoru != null) {
        const widoczneWPionie = widocznaWysokoscTablicyPt();
        // Bez pomiaru nie zgadujemy środka — celujemy prosto w wzór.
        const gornaKrawedz = yWzoru + (widoczneWPionie ? widoczneWPionie / 2 : 0);
        fragment += `&view=${TABLICE_TRYB_WIDOKU},${Math.round(Math.min(gornaKrawedz, TABLICE_STRONA_WYS_PT))}`;
    }
    return `${fragment}&toolbar=0`;
}

function openFormulasAtPage(numerStrony, yWzoru) {
    // Telefon: otwórz PDF z tablicami wzorów na właściwej stronie w nowej karcie
    // (panel <object> nie działa na Androidzie).
    if (czyTelefon()) {
        otworzPdfWNowejKarcie(`${TABLICE_PDF}${fragmentTablicy(numerStrony, yWzoru)}`);
        return;
    }

    // Panel pokazujemy NAJPIERW: dopóki ma display:none, jego <object> ma zerowe
    // wymiary i nie dałoby się policzyć, ile strony mieści się w kadrze.
    showFormulasPanel();

    const tablica = document.getElementById("tablica-wzorow");

    // Tworzymy nowy <object> zamiast tylko zmieniać `data` (przeglądarkowy
    // podgląd PDF nie zawsze przeładowuje się po samej zmianie atrybutu).
    const nowyObject = document.createElement("object");
    nowyObject.id = "tablica-wzorow";
    nowyObject.type = "application/pdf";
    nowyObject.data = `${TABLICE_PDF}${fragmentTablicy(numerStrony, yWzoru)}`;

    // Zamieniamy stary <object> na nowy w panelu (styl bierze się z CSS #tablica-wzorow).
    tablica.parentNode.replaceChild(nowyObject, tablica);
}
