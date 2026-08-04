// app/theme.js — motyw jasny / ciemny.

/* ===== MOTYW JASNY / CIEMNY =====
   Trzy stany: "auto" (za systemem, prefers-color-scheme), "jasny", "ciemny".
   Wybór ≠ auto zapisujemy w localStorage pod GLOBALNYM kluczem (bez SHEET_ID),
   żeby motyw był wspólny dla wszystkich arkuszy. Klasę theme-light/theme-dark
   na <html> ustawia już inline-skrypt w <head> (bez mignięcia) — tu tylko
   przełączamy stany i etykietę przycisku. */
const KLUCZ_MOTYWU = "matematykazen-motyw";
const MOTYWY = ["auto", "jasny", "ciemny"];
const themeToggle = document.getElementById("theme-toggle");

function readTheme() {
    try {
        const m = localStorage.getItem(KLUCZ_MOTYWU);
        if (m === "jasny" || m === "ciemny") return m;
    } catch (e) {}
    return "auto";
}
function applyTheme(motyw) {
    const html = document.documentElement;
    html.classList.toggle("theme-light", motyw === "jasny");
    html.classList.toggle("theme-dark", motyw === "ciemny");
    try {
        if (motyw === "auto") localStorage.removeItem(KLUCZ_MOTYWU);
        else localStorage.setItem(KLUCZ_MOTYWU, motyw);
    } catch (e) {}
    // Wartość w panelu bocznym (ustawWartosc pisze do .wartosc + data-stan;
    // NIE do textContent, żeby nie skasować ikony — patrz app/state.js).
    ustawWartosc(themeToggle, motyw);
}
applyTheme(readTheme()); // zsynchronizuj etykietę ze stanem z <head>
if (themeToggle) {
    // Motyw to WYJĄTEK od konwencji „klik ujmuje o stopień": nie jest skalą
    // więcej/mniej, więc nie ma „lewego wyłączenia" — zostaje kolejność z MOTYWY
    // i cykl w PRAWO (data-kierunek="prawo" w template.html). Kolejność musi się
    // zgadzać z data-stany, bo z niej biorą się kropki i podgląd po najechaniu.
    themeToggle.addEventListener("click", () => {
        applyTheme(nastepnyStan(themeToggle) || MOTYWY[0]);
    });
}
// Zmiana motywu w innej karcie (ten sam KLUCZ_MOTYWU w localStorage) ma się
// od razu odzwierciedlić tutaj — inaczej karty rozjeżdżają się aż do reloadu.
window.addEventListener("storage", e => {
    if (e.key === KLUCZ_MOTYWU) applyTheme(readTheme());
});
