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
    if (themeToggle) themeToggle.textContent = "motyw: " + motyw;
}
applyTheme(readTheme()); // zsynchronizuj etykietę ze stanem z <head>
if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const next = MOTYWY[(MOTYWY.indexOf(readTheme()) + 1) % MOTYWY.length];
        applyTheme(next);
    });
}
// Zmiana motywu w innej karcie (ten sam KLUCZ_MOTYWU w localStorage) ma się
// od razu odzwierciedlić tutaj — inaczej karty rozjeżdżają się aż do reloadu.
window.addEventListener("storage", e => {
    if (e.key === KLUCZ_MOTYWU) applyTheme(readTheme());
});
