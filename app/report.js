// app/report.js — „zgłoś błąd w zadaniu": dyskretny link tekstowy pod każdym
// zadaniem + modal z formularzem wysyłanym do Formspree (AJAX, bez przeładowania
// strony), antyspam (honeypot + throttling) i toast po wysłaniu. Toggle w menu
// „⋯" wyłącza link globalnie (localStorage, wzorem innych toggle'ów w app/*.js).
//
// Ładowany PRZED app/render.js — loadExercises() woła dodajLinkZgloszenia()
// przy budowaniu każdego zadania (klasyczne skrypty, wspólny scope).

const FORMSPREE_ENDPOINT = "https://formspree.io/f/xvzedgjg";

// Ustawienia GLOBALNE (wspólne dla wszystkich arkuszy — jak motyw czy tryb
// wskaźników), więc klucze BEZ sufiksu SHEET_ID:
//   • KLUCZ_ZGLASZANIE     — czy link „zgłoś błąd" jest w ogóle pokazywany,
//   • KLUCZ_ZGLOS_THROTTLE — znacznik czasu ostatniej wysyłki (throttling).
const KLUCZ_ZGLASZANIE = "matematykazen-zglaszanie-bledow";
const KLUCZ_ZGLOS_THROTTLE = "matematykazen-zglos-ostatnia";
// Formspree free tier ma limit 50 zgłoszeń/miesiąc — chronimy go lekkim
// throttlingiem: nie częściej niż raz na minutę (na tej przeglądarce).
const ZGLOS_THROTTLE_MS = 60 * 1000;

function czyZglaszanieWlaczone() {
    // Brak wpisu = domyślnie ON; tylko jawne "0" wyłącza link.
    try { return localStorage.getItem(KLUCZ_ZGLASZANIE) !== "0"; } catch (e) { return true; }
}

// ===== TOGGLE W MENU „⋯" (globalny włącznik linku) =====
// Widoczność samych linków steruje klasą body.bez-zglaszania (CSS chowa wtedy
// wszystkie .report-error-link) — wzorem body.reczne-sprawdzanie itd.
const zglosBladToggle = document.getElementById("zglos-blad-toggle");
function odswiezTrybZglaszania() {
    const on = czyZglaszanieWlaczone();
    document.body.classList.toggle("bez-zglaszania", !on);
    if (zglosBladToggle) {
        zglosBladToggle.textContent = on
            ? "zgłaszanie błędów: włączone"
            : "zgłaszanie błędów: wyłączone";
    }
}
odswiezTrybZglaszania();
if (zglosBladToggle) {
    zglosBladToggle.addEventListener("click", () => {
        const on = czyZglaszanieWlaczone();
        try { localStorage.setItem(KLUCZ_ZGLASZANIE, on ? "0" : "1"); } catch (e) {}
        odswiezTrybZglaszania();
    });
}

// ===== FORMULARZ (blok inline w karcie zadania) =====
// Formularz istnieje w JEDNEJ kopii w template.html, a przy otwarciu jest
// PRZENOSZONY (insertBefore przenosi węzeł, nie kopiuje) do karty klikniętego
// zadania — dzięki temu uczeń widzi treść zadania, opisując błąd, a ID
// pozostają unikalne i cały kod poniżej może korzystać z getElementById.
const zgOverlay = document.getElementById("zglos-blad-overlay");
const zgForm = document.getElementById("zglos-blad-form");
const zgKontekst = document.getElementById("zglos-blad-kontekst");
const zgOpis = document.getElementById("zglos-blad-opis");
const zgEmail = document.getElementById("zglos-blad-email");
const zgDanePodglad = document.getElementById("zglos-blad-dane-podglad");
const zgKategorie = document.getElementById("zglos-blad-kategorie");
const zgBlad = document.getElementById("zglos-blad-blad");
const zgWyslij = zgForm ? zgForm.querySelector(".zglos-blad-wyslij") : null;
let zgAktualnyNumer = null; // numer zadania, którego dotyczy otwarte zgłoszenie
let zgAktualnaKarta = null; // karta zadania, w której stoi teraz formularz

// ===== KATEGORIE (pigułki, wybór WIELOKROTNY, opcjonalne) =====
// Wielokrotny wybór jest tańszy niż jednokrotny: sam toggle na klikniętym
// przycisku, bez odznaczania rodzeństwa. Klasa .selected daje ten sam wygląd
// co neutralnie zaznaczona odpowiedź ABCD (style/sheet.css).
if (zgKategorie) {
    zgKategorie.addEventListener("click", (e) => {
        const pigulka = e.target.closest("button[data-kategoria]");
        if (pigulka) pigulka.classList.toggle("selected");
    });
}
function zebraneKategorie() {
    if (!zgKategorie) return [];
    return Array.from(zgKategorie.querySelectorAll("button.selected"))
        .map(b => b.dataset.kategoria);
}
function wyczyscKategorie() {
    if (!zgKategorie) return;
    zgKategorie.querySelectorAll("button.selected").forEach(b => b.classList.remove("selected"));
}

// ===== WALIDACJA OPISU (pole OBOWIĄZKOWE) =====
// Trzy sygnały naraz (ustalone z Henrichem): wyszarzony przycisk „Wyślij",
// komunikat pod polem i focus. trim() jest istotny — same spacje to pusty opis.
function czyOpisWypelniony() {
    return !!(zgOpis && zgOpis.value.trim() !== "");
}
function wyczyscBladOpisu() {
    if (zgBlad) zgBlad.textContent = "";
    if (zgOpis) zgOpis.classList.remove("zglos-blad-pole-blad");
}
function pokazBladOpisu() {
    if (zgBlad) zgBlad.textContent = "Opisz krótko, co jest nie tak — bez tego nie wiemy, czego szukać.";
    if (zgOpis) {
        zgOpis.classList.add("zglos-blad-pole-blad");
        zgOpis.focus();
    }
}
function odswiezPrzyciskWyslij() {
    if (zgWyslij) zgWyslij.disabled = !czyOpisWypelniony();
}
if (zgOpis) {
    zgOpis.addEventListener("input", () => {
        odswiezPrzyciskWyslij();
        if (czyOpisWypelniony()) wyczyscBladOpisu();
    });
}

// Efektywny motyw do dołączenia w danych: rozróżniamy ręczny wybór od „auto"
// (i doprecyzowujemy, co auto oznacza na tym systemie), żeby zgłoszenie mówiło,
// co użytkownik REALNIE widział.
function aktualnyMotyw() {
    const html = document.documentElement;
    if (html.classList.contains("theme-dark")) return "ciemny";
    if (html.classList.contains("theme-light")) return "jasny";
    try {
        return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "auto (ciemny)" : "auto (jasny)";
    } catch (e) { return "auto"; }
}

// Cała zawartość localStorage tej strony (wszystkie klucze) — diagnostyka
// stanu, w którym użytkownik zobaczył błąd (postęp, tryb, ustawienia).
function zbierzLocalStorage() {
    const out = {};
    try {
        for (let i = 0; i < localStorage.length; i++) {
            const k = localStorage.key(i);
            out[k] = localStorage.getItem(k);
        }
    } catch (e) { out._blad = "brak dostępu do localStorage"; }
    return out;
}

// Dane dołączane automatycznie (użytkownik NIC z tego nie wpisuje ręcznie).
function zbierzDaneAuto() {
    return {
        zadanie: zgAktualnyNumer,
        arkusz: SHEET_ID,
        url: location.href,
        motyw: aktualnyMotyw(),
        tryb: document.body.classList.contains("tryb-egzaminu") ? "egzamin" : "ćwiczenia",
        userAgent: navigator.userAgent,
        localStorage: zbierzLocalStorage(),
    };
}

function otworzModalZgloszenia(numer) {
    if (!zgOverlay) return;
    zgAktualnyNumer = numer;
    if (zgKontekst) zgKontekst.textContent = `Zadanie ${numer} — arkusz „${SHEET_ID}”.`;
    // Podgląd danych technicznych (transparentność — użytkownik widzi, co pójdzie).
    if (zgDanePodglad) zgDanePodglad.textContent = JSON.stringify(zbierzDaneAuto(), null, 2);
    zgOverlay.style.display = "flex";
    if (zgOpis) setTimeout(() => zgOpis.focus(), 0);
}
function zamknijModalZgloszenia() {
    if (zgOverlay) zgOverlay.style.display = "none";
}

if (zgOverlay) {
    // Klik w tło (poza oknem) zamyka — jak nakładka podsumowania egzaminu.
    zgOverlay.addEventListener("click", (e) => {
        if (e.target === zgOverlay) zamknijModalZgloszenia();
    });
    zgOverlay.querySelectorAll(".zglos-blad-anuluj, .zglos-blad-x").forEach(b => {
        b.addEventListener("click", zamknijModalZgloszenia);
    });
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && zgOverlay.style.display === "flex") zamknijModalZgloszenia();
    });
}

// ===== TOAST =====
let zgToastEl = null;
let zgToastTimer = null;
function pokazZglosToast(wiadomosc, czyBlad) {
    if (!zgToastEl) {
        zgToastEl = document.createElement("div");
        zgToastEl.className = "zglos-toast";
        zgToastEl.setAttribute("role", "status");
        document.body.appendChild(zgToastEl);
    }
    zgToastEl.textContent = wiadomosc;
    zgToastEl.classList.toggle("zglos-toast-blad", !!czyBlad);
    zgToastEl.classList.add("zglos-toast-widoczny");
    if (zgToastTimer) clearTimeout(zgToastTimer);
    zgToastTimer = setTimeout(() => {
        if (zgToastEl) zgToastEl.classList.remove("zglos-toast-widoczny");
    }, czyBlad ? 6000 : 4000);
}

// ===== WYSYŁKA (AJAX do Formspree) =====
if (zgForm) {
    zgForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Honeypot: pole ukryte przed ludźmi (CSS), wypełniają je tylko boty.
        // Wypełnione → udajemy sukces i NIC nie wysyłamy (nie zdradzamy botowi
        // mechanizmu ani nie marnujemy limitu Formspree).
        const hp = zgForm.querySelector('input[name="_gotcha"]');
        if (hp && hp.value.trim() !== "") {
            zamknijModalZgloszenia();
            pokazZglosToast("Dziękujemy, zgłoszenie wysłane.", false);
            return;
        }

        // Throttling: nie częściej niż raz na minutę (ochrona limitu 50/mies.).
        const teraz = Date.now();
        let ostatnia = 0;
        try { ostatnia = parseInt(localStorage.getItem(KLUCZ_ZGLOS_THROTTLE), 10) || 0; } catch (e) {}
        if (teraz - ostatnia < ZGLOS_THROTTLE_MS) {
            const sek = Math.ceil((ZGLOS_THROTTLE_MS - (teraz - ostatnia)) / 1000);
            pokazZglosToast(`Chwila — zgłoszenie można wysłać raz na minutę. Spróbuj za ${sek} s.`, true);
            return;
        }

        // Endpoint jeszcze nieustawiony (placeholder) — czytelny komunikat zamiast
        // mylącego błędu sieci. NIE ustawiamy throttlingu (nic nie wysłano).
        if (!/^https?:\/\/formspree\.io\/f\//.test(FORMSPREE_ENDPOINT)) {
            pokazZglosToast("Zgłoszenia nie są jeszcze skonfigurowane — daj znać autorowi strony.", true);
            return;
        }

        const przyciskWyslij = zgForm.querySelector(".zglos-blad-wyslij");
        if (przyciskWyslij) { przyciskWyslij.disabled = true; przyciskWyslij.textContent = "Wysyłanie…"; }

        const auto = zbierzDaneAuto();
        // Formspree dostaje płaski obiekt pól (localStorage jako string JSON, żeby
        // nie zgubić struktury); _subject ustawia temat maila powiadomienia.
        const payload = {
            opis: zgOpis ? zgOpis.value : "",
            email: zgEmail ? zgEmail.value : "",
            zadanie: auto.zadanie,
            arkusz: auto.arkusz,
            url: auto.url,
            motyw: auto.motyw,
            tryb: auto.tryb,
            userAgent: auto.userAgent,
            localStorage: JSON.stringify(auto.localStorage),
            _subject: `MatematykaZen — zgłoszenie błędu: zad. ${auto.zadanie} (${auto.arkusz})`,
        };

        let odpowiedz = null;
        try {
            odpowiedz = await fetch(FORMSPREE_ENDPOINT, {
                method: "POST",
                headers: { "Content-Type": "application/json", "Accept": "application/json" },
                body: JSON.stringify(payload),
            });
        } catch (blad) {
            // Sieć padła — żądanie NIE dotarło do Formspree, więc nie ustawiamy
            // throttlingu (użytkownik może spróbować od razu).
            if (przyciskWyslij) { przyciskWyslij.disabled = false; przyciskWyslij.textContent = "Wyślij zgłoszenie"; }
            pokazZglosToast("Brak połączenia — nie udało się wysłać zgłoszenia. Sprawdź internet i spróbuj ponownie.", true);
            return;
        }

        // Żądanie dotarło do serwera (ok albo nie) — liczymy je do throttlingu,
        // żeby chronić miesięczny limit Formspree.
        try { localStorage.setItem(KLUCZ_ZGLOS_THROTTLE, String(teraz)); } catch (e) {}
        if (przyciskWyslij) { przyciskWyslij.disabled = false; przyciskWyslij.textContent = "Wyślij zgłoszenie"; }

        if (odpowiedz.ok) {
            zgForm.reset();
            zamknijModalZgloszenia();
            pokazZglosToast("Dziękujemy, zgłoszenie wysłane.", false);
        } else {
            // Np. wyczerpany miesięczny limit (429) albo błąd walidacji Formspree.
            pokazZglosToast("Nie udało się wysłać zgłoszenia (być może wyczerpano miesięczny limit). Spróbuj później.", true);
        }
    });
}

// ===== LINK POD ZADANIEM =====
// Wołane z loadExercises() (app/render.js) dla każdego zadania: dokłada na końcu
// klonu dyskretny link „zgłoś błąd w tym zadaniu". Numer bierzemy z treści
// („Zadanie N.") — jak wskaźniki „oceń się" — bo indeks w tablicy rozjeżdża się
// z numeracją CKE (zadania nadrzędne / wieloczęściowe). Widoczność steruje
// globalnie klasa body.bez-zglaszania (CSS), więc tu tworzymy link zawsze.
function dodajLinkZgloszenia(exerciseClone) {
    const qText = (exerciseClone.querySelector(".question")?.textContent) || "";
    const m = qText.match(/Zadanie\s*(\d+)/i);
    const numer = m ? m[1] : "?";
    const link = document.createElement("button");
    link.type = "button";
    link.className = "report-error-link";
    link.textContent = "zgłoś błąd";
    link.title = "Zgłoś błąd w tym zadaniu (zła odpowiedź, literówka, problem z filmem…)";
    link.addEventListener("click", () => otworzModalZgloszenia(numer));
    exerciseClone.appendChild(link);
}
