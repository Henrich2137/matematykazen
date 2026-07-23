// app/kroki.js — podsystem rozwiązań krok-po-kroku (film/obraz/tekst).
// Wydzielony z loadExercises (app/render.js). Funkcje są top-level, a stan
// wspólny dla showStep i strzałek ◄/► (currentStep, stepSwapToken oraz refy
// DOM kroków) przekazujemy JAWNIE w obiekcie `ctx` — dzięki temu currentStep/
// stepSwapToken pozostają jedną, współdzieloną instancją (nie kopią wartości).
// Logika podwójnego bufora, tokenu podmiany, loadeddata/fallback jest bez zmian.
//
// Kształt ctx budowanego per-zadanie w render.js:
//   { currentStep, stepSwapToken, steps, stepsContent, prevBtn, nextBtn,
//     stepCounter, exerciseClone }

function renderStep(step) {

    if (!step) return "";
    // Podpis kroku zawsze w .step-comment — rezerwuje stałe miejsce (~2 linijki),
    // dzięki czemu wysokość diva nie skacze między krokami o różnej długości tekstu.
    if (step.type === "video") {
        // Prędkość ustawiamy na realnym elemencie <video> w showStep(),
        // bo właściwość JS (defaultPlaybackRate) nie przetrwałaby
        // serializacji do stringa HTML. Tam też podpinamy klik (pauza/play)
        // i ikonkę ▶ (widoczną gdy zatrzymany).
        return `
            <div class="step-video">
                <video autoplay playsinline>
                    <source src="${mediaPath(step.src)}" type="video/mp4">
                </video>
                <div class="video-overlay-icon"></div>
            </div>
            <div class="step-comment">${step.text}</div>
        `;
    } else if (step.type === "image") {
        return `<img src="${mediaPath(step.src)}"><div class="step-comment">${step.text}</div>`;
    } else if (step.type === "text") {
        return `<div class="step-comment">${step.text}</div>`;
    }
    return "";
}

// Podwójny bufor kroków: przy przejściu na krok z filmem STARY krok zostaje
// widoczny (na ostatniej klatce), a nowy podmieniamy dopiero, gdy jego film ma
// zdekodowaną pierwszą klatkę (loadeddata) — dzięki temu nie ma błysku pustego
// miejsca. Token (ctx.stepSwapToken) chroni przed wyścigiem przy szybkim
// klikaniu ◄/► (spóźniona podmiana starego kroku jest ignorowana). Fallback
// setTimeout podmienia krok nawet, gdyby film ładował się wyjątkowo długo.
function showStep(ctx, idx) {
    ctx.currentStep = idx;
    const swapToken = ++ctx.stepSwapToken;
    const { steps, stepsContent, prevBtn, nextBtn, stepCounter, exerciseClone } = ctx;

    // Nawigacja aktualizuje się od razu (nie czeka na załadowanie filmu).
    stepCounter.textContent = `${ctx.currentStep + 1} / ${steps.length}`;
    prevBtn.disabled = ctx.currentStep === 0;
    nextBtn.disabled = ctx.currentStep === steps.length - 1;
    if (ctx.currentStep == steps.length - 1) {
        markCorrectAnswer(exerciseClone);
    }

    // Nowy krok budujemy w odłączonym elemencie i dopiero gotowy
    // wstawiamy w miejsce starego (replaceChildren).
    const nowyKrok = document.createElement("div");
    nowyKrok.innerHTML = renderStep(steps[ctx.currentStep]);
    renderMath(nowyKrok);

    const video = nowyKrok.querySelector("video");
    let krokWstawiony = false; // loadeddata i fallback setTimeout mogą przyjść oba
    const wstawKrok = () => {
        if (swapToken !== ctx.stepSwapToken) return; // w międzyczasie wybrano inny krok
        if (krokWstawiony) return;
        krokWstawiony = true;
        stepsContent.replaceChildren(...nowyKrok.childNodes);
        if (video) {
            // play() zamiast atrybutu autoplay: film ma wystartować
            // dopiero po wstawieniu do DOM, nie w buforze.
            video.play().catch(() => {});
        }
        podepnijSterowanieWideo(video);
    };

    if (video && stepsContent.childElementCount) {
        video.removeAttribute("autoplay");
        video.preload = "auto";
        video.load(); // element odłączony też się ładuje
        if (video.readyState >= 2) { // HAVE_CURRENT_DATA — np. film z cache
            wstawKrok();
        } else {
            video.addEventListener("loadeddata", wstawKrok, { once: true });
            setTimeout(wstawKrok, 1500);
        }
    } else {
        // Pierwszy render kroku albo krok bez filmu — podmiana od razu.
        wstawKrok();
    }

    // Podgrzewamy film następnego kroku, żeby przełączenie mniej migało —
    // przeglądarka ściąga go do cache, zanim użytkownik kliknie ►.
    const nextStep = steps[ctx.currentStep + 1];
    if (nextStep && nextStep.type === "video") {
        const preload = document.createElement("video");
        preload.preload = "auto";
        preload.src = mediaPath(nextStep.src);
    }
}

// Sterowanie filmem kroku (klik = pauza/play, ikonka stanu) —
// podpinane do realnego, już wstawionego <video>.
// (Pasek postępu z pętlą requestAnimationFrame usunięty: klatkował
// stronę w Firefoksie podczas przewijania, a bajer nie był tego wart.)
function podepnijSterowanieWideo(video) {
    if (video) {
        video.defaultPlaybackRate = 1;
        video.playbackRate = 1;

        const stepVideo = video.closest(".step-video");

        // Klik w film przełącza pauzę/odtwarzanie.
        video.addEventListener("click", () => {
            if (video.paused) {
                video.play();
            } else {
                video.pause();
            }
        });

        // Klasy stanu na kontenerze sterują ikonką:
        //  .paused (bez .ended) → dwie kreski (pauza),
        //  .ended               → zakręcona strzałka (odtwórz od nowa).
        const syncState = () => {
            if (stepVideo) {
                stepVideo.classList.toggle("paused", video.paused);
                stepVideo.classList.toggle("ended", video.ended);
            }
        };
        video.addEventListener("play", syncState);
        video.addEventListener("pause", syncState);
        video.addEventListener("ended", syncState);

        syncState();
    }
}
