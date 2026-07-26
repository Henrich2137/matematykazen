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

// ===== WALIDACJA OPISU (pole OBOWIĄZKOWE, z limitem długości) =====
// Trzy sygnały naraz (ustalone z Henrichem): wyszarzony przycisk „Wyślij",
// komunikat pod polem i focus. trim() jest istotny — same spacje to pusty opis.
//
// Limity liczone są PO trim(), więc spacje nie nabijają długości:
//   • MIN 3 znaki — odsiewa przypadkowe „a"/„." bez żadnej treści,
//   • MAX 2000 znaków — z zapasem starcza na dokładny opis błędu (~350 słów);
//     bez limitu jedno zgłoszenie potrafiło mieć kilkadziesiąt kB (test
//     Henricha 2026-07-26), co zaśmieca skrzynkę i payload Formspree.
// Górny limit jest też twardo w atrybucie maxlength textarei (przeglądarka nie
// pozwoli wpisać ani wkleić więcej), ale sprawdzamy go również tutaj, bo
// maxlength da się ominąć programowo.
const OPIS_MIN = 3;
const OPIS_MAX = 2000;

function dlugoscOpisu() {
    return zgOpis ? zgOpis.value.trim().length : 0;
}
// Zwraca komunikat o błędzie albo "" gdy opis jest w porządku.
function bladOpisu() {
    const n = dlugoscOpisu();
    if (n === 0) return "Opisz krótko, co jest nie tak — bez tego nie wiemy, czego szukać.";
    if (n < OPIS_MIN) return `Opis jest za krótki — napisz przynajmniej ${OPIS_MIN} znaki.`;
    if (n > OPIS_MAX) return `Opis jest za długi — zmieść się w ${OPIS_MAX} znakach (masz ${n}).`;
    return "";
}
function czyOpisWypelniony() {
    return bladOpisu() === "";
}
function wyczyscBladOpisu() {
    if (zgBlad) zgBlad.textContent = "";
    if (zgOpis) zgOpis.classList.remove("zglos-blad-pole-blad");
}
function pokazBladOpisu() {
    if (zgBlad) zgBlad.textContent = bladOpisu();
    if (zgOpis) {
        zgOpis.classList.add("zglos-blad-pole-blad");
        zgOpis.focus();
    }
}
// Licznik „123 / 2000" pod polem — ostrzega ostatnie 10% limitu, żeby nikt nie
// pisał długiego opisu w nieświadomości, że zaraz się utnie.
function odswiezLicznikOpisu() {
    if (!zgLicznik) return;
    const n = dlugoscOpisu();
    zgLicznik.textContent = `${n} / ${OPIS_MAX}`;
    zgLicznik.classList.toggle("zglos-blad-licznik-blisko", n > OPIS_MAX * 0.9);
}
function odswiezPrzyciskWyslij() {
    if (zgWyslij) zgWyslij.disabled = !czyOpisWypelniony();
}
if (zgOpis) {
    zgOpis.addEventListener("input", () => {
        odswiezPrzyciskWyslij();
        odswiezLicznikOpisu();
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

// Tekst elementu w formie czytelnej w mailu ze zgłoszeniem.
//
// UWAGA na KaTeX: renderuje każdy wzór w DWÓCH warstwach naraz — ukrytym
// MathML-u (dla czytników ekranu, razem z surowym LaTeX-em w <annotation>)
// i widocznym HTML-u. Samo .textContent zlepia obie w bełkot: przycisk
// „A. 5⁴" z zad. 2 dawał „A. 545^{4}54". Bierzemy więc surowy LaTeX
// z <annotation>, bo jest jednoznaczny — warstwa wizualna spłaszcza 5⁴ do
// nierozróżnialnego „54". Fallbackiem jest warstwa wizualna, gdyby kiedyś
// zabrakło anotacji.
//
// Pracujemy na KLONIE: podmiany nie mogą ruszyć żywego DOM-u strony.
function tekstOdpowiedzi(el) {
    if (!el) return "";
    const kopia = el.cloneNode(true);
    kopia.querySelectorAll(".katex").forEach(k => {
        if (!k.parentNode) return; // zagnieżdżony .katex już odpięty przy zewnętrznym
        const anotacja = k.querySelector('annotation[encoding="application/x-tex"]');
        const wizualna = k.querySelector(".katex-html");
        const tekst = anotacja ? anotacja.textContent : (wizualna ? wizualna.textContent : "");
        k.parentNode.replaceChild(document.createTextNode(tekst), k);
    });
    return kopia.textContent.replace(/\s+/g, " ").trim();
}

// Co uczeń zaznaczył/wpisał — czytane wprost z DOM karty zadania. Wyciągamy to
// JAWNIE (a nie tylko w zrzucie localStorage), żeby dało się przeczytać w mailu
// bez grzebania w JSON-ie. Obsługujemy trzy kształty odpowiedzi z render.js:
// przyciski ABCD/PF/multiSelect, pola „uzupełnij" (.fill-in-input) i pole
// odpowiedzi ostatecznej (.final-answer-input).
function odpowiedzUcznia(karta) {
    if (!karta) return "nieznana";
    const czesci = [];

    const przyciski = karta.querySelectorAll(
        ".answers-container button.selected, .answers-container button.correct, .answers-container button.incorrect"
    );
    przyciski.forEach(b => czesci.push(tekstOdpowiedzi(b)));

    karta.querySelectorAll(".fill-in-row").forEach(row => {
        const etykieta = row.querySelector(".fill-in-label");
        const pole = row.querySelector(".fill-in-input");
        if (pole && pole.value.trim() !== "") {
            // Etykieta pola też bywa wzorem KaTeX (np. „zbiorem rozwiązań jest \(x\in\)").
            const opisPola = etykieta ? tekstOdpowiedzi(etykieta) : "";
            czesci.push(`${opisPola ? opisPola + " " : ""}${pole.value.trim()}`);
        }
    });

    const finalne = karta.querySelector(".final-answer-input");
    if (finalne && finalne.value.trim() !== "") czesci.push(`odp. ostateczna: ${finalne.value.trim()}`);

    return czesci.length ? czesci.join(" | ") : "brak odpowiedzi";
}

// Poprawna odpowiedź jest w DOM od początku, oznaczona klasą .hiddenCorrect
// (patrz markCorrectAnswer w app/answers.js) — dla zadań przyciskowych.
function odpowiedzPoprawna(karta) {
    if (!karta) return "nieznana";
    const btn = karta.querySelector(".answers-container button.hiddenCorrect");
    return btn ? tekstOdpowiedzi(btn) : "nie dotyczy / nieoznaczona w DOM";
}

// Który krok rozwiązania był na ekranie. Licznik „3 / 7" i tak jest renderowany
// przez showStep (app/steps.js), więc czytamy go z DOM — obiekt ctx ze steps.js
// jest lokalny per zadanie i nieosiągalny stąd.
function krokRozwiazania(karta) {
    if (!karta) return "brak";
    const solutionOtwarte = karta.querySelector(".solution-container");
    const licznik = karta.querySelector(".step-counter");
    if (!licznik || !licznik.textContent.trim()) return "brak kroków";
    const widoczne = solutionOtwarte && solutionOtwarte.style.display !== "none";
    return `${licznik.textContent.trim()}${widoczne ? "" : " (rozwiązanie zamknięte)"}`;
}

// Wymiary ekranu — przy zgłoszeniach o rozjechany układ userAgent nie wystarcza.
function daneEkranu() {
    try {
        return {
            okno: `${window.innerWidth}×${window.innerHeight}`,
            ekran: `${screen.width}×${screen.height}`,
            dpr: window.devicePixelRatio,
            orientacja: window.innerWidth >= window.innerHeight ? "pozioma" : "pionowa",
        };
    } catch (e) { return { blad: "brak dostępu do wymiarów ekranu" }; }
}

// Dane dołączane automatycznie (użytkownik NIC z tego nie wpisuje ręcznie).
function zbierzDaneAuto() {
    return {
        zadanie: zgAktualnyNumer,
        arkusz: SHEET_ID,
        url: location.href,
        motyw: aktualnyMotyw(),
        tryb: document.body.classList.contains("tryb-egzaminu") ? "egzamin" : "ćwiczenia",
        odpowiedzUcznia: odpowiedzUcznia(zgAktualnaKarta),
        odpowiedzPoprawna: odpowiedzPoprawna(zgAktualnaKarta),
        krokRozwiazania: krokRozwiazania(zgAktualnaKarta),
        ekran: daneEkranu(),
        userAgent: navigator.userAgent,
        localStorage: zbierzLocalStorage(),
    };
}

function czyFormularzOtwarty() {
    return !!zgOverlay && zgOverlay.style.display !== "none" && zgOverlay.style.display !== "";
}

// Otwiera formularz W KARCIE danego zadania. Ponowny klik przy TYM SAMYM
// zadaniu zwija formularz (toggle, jak „Podpowiedź"); klik przy innym zadaniu
// przenosi go tam. Za każdym otwarciem czyścimy pola, żeby opis zaczęty przy
// zad. 7 nie poszedł przypadkiem jako zgłoszenie do zad. 9.
function otworzModalZgloszenia(numer, karta) {
    if (!zgOverlay) return;

    if (czyFormularzOtwarty() && zgAktualnaKarta === karta) {
        zamknijModalZgloszenia();
        return;
    }

    zgAktualnyNumer = numer;
    zgAktualnaKarta = karta || null;

    // Reset stanu z poprzedniego zgłoszenia.
    if (zgForm) zgForm.reset();
    wyczyscKategorie();
    wyczyscBladOpisu();
    odswiezPrzyciskWyslij();

    if (zgKontekst) zgKontekst.textContent = `Zadanie ${numer} — arkusz „${SHEET_ID}”.`;
    // Podgląd danych technicznych (transparentność — użytkownik widzi, co pójdzie).
    // Liczony PO ustawieniu zgAktualnaKarta, bo czyta odpowiedzi z tej karty.
    if (zgDanePodglad) zgDanePodglad.textContent = JSON.stringify(zbierzDaneAuto(), null, 2);

    // Przeniesienie węzła do karty zadania: nad rząd [Podpowiedź][Rozwiązanie],
    // czyli tuż pod odpowiedziami. insertBefore PRZENOSI (nie kopiuje), więc
    // w dokumencie nadal jest dokładnie jeden #zglos-blad-overlay.
    if (karta) {
        const kotwica = karta.querySelector(".light-button-container");
        if (kotwica) karta.insertBefore(zgOverlay, kotwica);
        else karta.appendChild(zgOverlay);
    }

    zgOverlay.style.display = "block";
    if (zgOpis) setTimeout(() => zgOpis.focus(), 0);
}

function zamknijModalZgloszenia() {
    if (zgOverlay) zgOverlay.style.display = "none";
    zgAktualnaKarta = null;
}

if (zgOverlay) {
    // Formularz stoi teraz W treści strony, więc nie ma tła do kliknięcia —
    // zamykają go „Anuluj", „✕" i Escape.
    zgOverlay.querySelectorAll(".zglos-blad-anuluj, .zglos-blad-x").forEach(b => {
        b.addEventListener("click", zamknijModalZgloszenia);
    });
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && czyFormularzOtwarty()) zamknijModalZgloszenia();
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

        // Opis jest OBOWIĄZKOWY. Przycisk „Wyślij" i tak jest wtedy wyszarzony,
        // ale walidujemy też tutaj — przez requestSubmit()/Enter da się ominąć
        // disabled, a i tak nie chcemy marnować limitu na puste zgłoszenie.
        if (!czyOpisWypelniony()) {
            pokazBladOpisu();
            odswiezPrzyciskWyslij();
            return;
        }

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

        // Blokada na czas wysyłki (Formspree AJAX: przycisk nieaktywny do końca
        // żądania). Po zakończeniu NIE odblokowujemy na sztywno — o stanie
        // decyduje odswiezPrzyciskWyslij(), bo pusty opis ma go trzymać szarym.
        if (zgWyslij) { zgWyslij.disabled = true; zgWyslij.textContent = "Wysyłanie…"; }

        const auto = zbierzDaneAuto();
        const kategorie = zebraneKategorie();
        const kategorieTekst = kategorie.length ? kategorie.join(", ") : "bez kategorii";
        // Formspree dostaje płaski obiekt pól (localStorage i ekran jako string
        // JSON, żeby nie zgubić struktury); _subject ustawia temat maila
        // powiadomienia — kategorie idą w temat, żeby dało się triażować
        // zgłoszenia z samej listy wiadomości w skrzynce.
        const payload = {
            opis: zgOpis ? zgOpis.value.trim() : "",
            kategorie: kategorieTekst,
            email: zgEmail ? zgEmail.value : "",
            zadanie: auto.zadanie,
            arkusz: auto.arkusz,
            url: auto.url,
            motyw: auto.motyw,
            tryb: auto.tryb,
            odpowiedzUcznia: auto.odpowiedzUcznia,
            odpowiedzPoprawna: auto.odpowiedzPoprawna,
            krokRozwiazania: auto.krokRozwiazania,
            ekran: JSON.stringify(auto.ekran),
            userAgent: auto.userAgent,
            localStorage: JSON.stringify(auto.localStorage),
            _subject: `MatematykaZen — zad. ${auto.zadanie} (${auto.arkusz}): ${kategorieTekst}`,
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
            // throttlingu (użytkownik może spróbować od razu). Opis został
            // wpisany, więc przycisk wraca do stanu aktywnego.
            if (zgWyslij) zgWyslij.textContent = "Wyślij zgłoszenie";
            odswiezPrzyciskWyslij();
            pokazZglosToast("Brak połączenia — nie udało się wysłać zgłoszenia. Sprawdź internet i spróbuj ponownie.", true);
            return;
        }

        // Żądanie dotarło do serwera (ok albo nie) — liczymy je do throttlingu,
        // żeby chronić miesięczny limit Formspree.
        try { localStorage.setItem(KLUCZ_ZGLOS_THROTTLE, String(teraz)); } catch (e) {}
        if (zgWyslij) zgWyslij.textContent = "Wyślij zgłoszenie";

        if (odpowiedz.ok) {
            zgForm.reset();
            wyczyscKategorie();
            wyczyscBladOpisu();
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
    // [\d.]+ zamiast \d+ — łapie też podnumery ("12.1", "12.2"), tak jak
    // numerZadania() w app/render.js. Kropka kończąca zdanie („Zadanie 12.")
    // jest ucinana niżej, żeby numer nie wyglądał jak „12.".
    const m = qText.match(/Zadanie\s*([\d.]+)/i);
    const numer = m ? m[1].replace(/\.$/, "") : "?";
    const link = document.createElement("button");
    link.type = "button";
    link.className = "report-error-link";
    link.textContent = "zgłoś błąd";
    link.title = "Zgłoś błąd w tym zadaniu (zła odpowiedź, literówka, problem z filmem…)";
    // Karta zadania idzie dalej, bo formularz jest do niej PRZENOSZONY, a dane
    // automatyczne (odpowiedź ucznia, krok rozwiązania) czytamy z jej DOM.
    link.addEventListener("click", () => otworzModalZgloszenia(numer, exerciseClone));
    exerciseClone.appendChild(link);
}
