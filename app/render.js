// app/render.js — loadExercises(): render wszystkich zadań z tablicy `exercises`,
// obsługa odpowiedzi (ABCD/PF/multiSelect/open/fillIn), podpowiedzi, punktacji,
// zapisu/odtworzenia postępu. Podsystem kroków rozwiązania jest w app/steps.js
// (funkcje renderStep/showStep/podepnijSterowanieWideo wołane z krokiCtx).

// Fabryka przycisku „sprawdź" dla trybu „sprawdź później" (natychmiastowa
// poprawność OFF). Przycisk jest tworzony LENIWIE (przy pierwszym pokaż) i
// pozycjonowany absolutnie WZGLĘDEM kontenera odpowiedzi (po jego prawej
// stronie, patrz .answer-check-floating w sheet.css), więc nie zmienia
// wysokości zadania ani układu strony. onSprawdz odsłania ocenę zadania.
function utworzPrzyciskSprawdz(answersContainer, onSprawdz) {
    let btn = null;
    return {
        pokaz() {
            if (!btn) {
                btn = document.createElement("button");
                btn.type = "button";
                btn.className = "answer-check-floating";
                btn.textContent = "sprawdź";
                btn.title = "Sprawdź odpowiedź (odsłoń poprawność)";
                btn.addEventListener("click", onSprawdz);
                answersContainer.appendChild(btn);
            }
            btn.style.display = "block";
        },
        schowaj() { if (btn) btn.style.display = "none"; },
    };
}

// Numer zadania z treści („Zadanie N." lub „Zadanie N.M" dla podnumerowanych),
// z fallbackiem na index+1 — używane w komunikatach console.warn poniżej, żeby
// wskazywały prawdziwy numer CKE, a nie indeks w tablicy exercises.
function numerZadania(exercise, index) {
    const m = (exercise.question || "").match(/Zadanie\s*(\d+(?:\.\d+)?)/i);
    return m ? m[1] : String(index + 1);
}

// Function to load exercises
function loadExercises() {
    const exercisesWrapper = document.getElementById("exercises-wrapper");
    const template = document.getElementById("exercise-template");

    const totalScoreSpan = document.getElementById("total-score");

    // Maksymalna liczba punktów liczona wprost z danych — nie trzeba już ręcznie
    // synchronizować stałej w exercises.js z sumą pól maxScore.
    const maxTotalScore = exercises.reduce((sum, e) => sum + (e.maxScore || 0), 0);

    // Suma punktów = suma zdobytych punktów ze wszystkich zadań. Liczymy ją od nowa
    // przy każdej zmianie, więc kolejność klików nie ma znaczenia i nie da się
    // podwójnie naliczyć ani zapomnieć odjąć punktu.
    function updateTotalScore() {
        totalScore = exercises.reduce((sum, e) => sum + (e.earnedScore || 0), 0);
        // Procent na bieżąco (tryb ćwiczeniowy — w trybie egzaminu #total-score
        // i tak jest ukryty). Próg zdawalności matury podstawowej to 30%: od
        // niego procent robi się zielony, a tooltip mówi "zdałeś" zamiast
        // "nie zdałeś (jeszcze)".
        const procent = maxTotalScore ? Math.round(totalScore / maxTotalScore * 100) : 0;
        const zdane = procent >= 30;
        totalScoreSpan.innerHTML =
            `${totalScore} / ${maxTotalScore} pkt ` +
            `<span class="total-percent${zdane ? " zdane" : ""}" ` +
            `title="${zdane ? "zdałeś" : "nie zdałeś (jeszcze)"}">${procent}%</span>`;
    }
    updateTotalScore();

    // ZAPIS POSTĘPU (localStorage). Zapamiętujemy "co użytkownik kliknął/wpisał",
    // a przy wczytaniu strony odtwarzamy to symulując te same kliknięcia — dzięki
    // temu ocena, kolory i punkty liczą się dokładnie tą samą drogą co na żywo.
    // Zapis z inną liczbą zadań (zmiana arkusza/schematu) jest ignorowany.
    // (KLUCZ_POSTEPU jest zadeklarowany globalnie w app/state.js.)
    let zapis = null;
    try { zapis = JSON.parse(localStorage.getItem(KLUCZ_POSTEPU)); } catch (e) { zapis = null; }
    if (!zapis || zapis.n !== exercises.length || !Array.isArray(zapis.stany)) zapis = null;
    const stanOdpowiedzi = exercises.map(() => ({}));
    // Zasiej cały zapisany stan PRZED odtwarzającymi klikami: każdy klik niżej
    // wywołuje zapiszPostep(), który serializuje CAŁĄ tablicę stanOdpowiedzi —
    // bez tego zadania o wyższym indeksie (jeszcze nieodtworzone) zostałyby
    // nadpisane pustym {} i traciłyby zapisany tok rozwiązania po odświeżeniu.
    if (zapis) {
        zapis.stany.forEach((zap, i) => {
            if (zap && stanOdpowiedzi[i]) Object.assign(stanOdpowiedzi[i], zap);
        });
    }
    function zapiszPostep() {
        try {
            localStorage.setItem(KLUCZ_POSTEPU, JSON.stringify({ n: exercises.length, stany: stanOdpowiedzi }));
        } catch (e) { /* np. zablokowane localStorage — działamy dalej bez zapisu */ }
    }

    exercises.forEach((exercise, index) => {
        exercise.earnedScore = 0;
        const stan = stanOdpowiedzi[index];

        // Odnośniki do elementów odpowiedzi, przez które odtwarzamy zapisany
        // postęp na końcu budowania zadania (patrz blok "Przywrócenie postępu").
        const abcdButtons = [];
        const pfButtons = [];      // tablica tablic [przyciskP, przyciskF]
        const multiButtons = [];
        const selfButtons = [];
        const fillRows = [];
        let fillCheck = null;
        let openTextarea = null;   // textarea zadania otwartego (tok rozwiązania)
        // Ustawiane przez gałęzie zadań zamkniętych (ABCD/PF/multiSelect) na funkcję
        // odsłaniającą ocenę tego zadania. Używa jej przywracanie postępu, by w
        // trybie „sprawdź później" odsłonić ocenę tylko tam, gdzie użytkownik już
        // ją wcześniej odsłonił (klik „sprawdź").
        let ocenTegoZadania = null;

        //in the future we can make something like studentAttempt object that is passed by php after login and maybe chossing certan attempt in acc menu or smth

        const exerciseClone = template.cloneNode(true);
        exerciseClone.style.display = "block";
        exerciseClone.id = `exercise-${index}`;

        const scoreSpan = exerciseClone.querySelector(".exercise-score");

        // Jeden wspólny sposób ustawiania punktów zadania: aktualizuje earnedScore,
        // badge przy zadaniu (kolor zależny od 0 / część / komplet) i sumę w pasku.
        function setScore(points) {
            exercise.earnedScore = points;
            scoreSpan.textContent = `${points} / ${exercise.maxScore} pkt`;
            scoreSpan.classList.remove("low-exercise-score", "mid-exercise-score", "high-exercise-score");
            scoreSpan.classList.add(
                points === exercise.maxScore ? "high-exercise-score"
                : points > 0 ? "mid-exercise-score"
                : "low-exercise-score"
            );
            updateTotalScore();
        }

        // Set question
        exerciseClone.querySelector(".question").innerHTML = exercise.question;
        // Grafiki zadań spoza pierwszego ekranu dociągają się dopiero przy scrollu.
        exerciseClone.querySelectorAll(".question img").forEach(img => { img.loading = "lazy"; });

        // Set answers
        const answersContainer = exerciseClone.querySelector(".answers-container");

        // Typ zadania: jawny (exercise.type) albo wywnioskowany — odpowiedzi w answers
        // oznaczają zwykły test jednokrotnego wyboru, brak odpowiedzi = zadanie otwarte.
        const type = exercise.type || (exercise.answers && exercise.answers.length ? "ABCD" : "open");

        if (type === "ABCD") {
            // Poprawną odpowiedź wskazuje indeks z danych (0 = A, 1 = B, ...).
            // -1 lub brak pola = zadanie jeszcze niewypełnione -> tryb "?".
            const correctIndex = Number.isInteger(exercise.correctAnswerIndex) ? exercise.correctAnswerIndex : -1;
            if (correctIndex >= exercise.answers.length) {
                console.warn(`Zadanie ${numerZadania(exercise, index)}: correctAnswerIndex (${correctIndex}) wykracza poza liczbę odpowiedzi`);
            }

            let sprawdzone = false; // czy ocena (kolor/punkty) jest już odsłonięta

            // Odsłonięcie oceny wybranej odpowiedzi (na podstawie stan.abcd).
            // Idempotentne: wołane i w trybie natychmiastowym (klik = od razu),
            // i z przycisku „sprawdź" / „sprawdź wszystkie". Bez zaznaczenia no-op.
            function ocenAbcd() {
                if (!Number.isInteger(stan.abcd) || !abcdButtons[stan.abcd]) return;
                abcdButtons.forEach(b => b.classList.remove("correct", "incorrect", "selected"));
                if (stan.abcd === correctIndex) {
                    abcdButtons[stan.abcd].classList.add("correct");
                    setScore(exercise.maxScore);
                } else {
                    // Zła odpowiedź: zawsze 0 / X pkt.
                    abcdButtons[stan.abcd].classList.add("incorrect");
                    setScore(0);
                }
                sprawdzone = true;
                stan.sprawdzone = true;
                sprawdz.schowaj();
                zapiszPostep();
            }
            const sprawdz = utworzPrzyciskSprawdz(answersContainer, ocenAbcd);

            exercise.answers.forEach((answer, i) => {
                const answerButton = document.createElement("button");
                answerButton.innerHTML = answer;
                if (i === correctIndex) {
                    answerButton.classList.add("hiddenCorrect");
                }
                answerButton.addEventListener("click", () => {
                    // Tryb "?" — brak zdefiniowanej poprawnej odpowiedzi (niewypełnione).
                    // Klik dokłada lub zdejmuje znak "?" (tylko jeden na zadanie).
                    if (correctIndex === -1) {
                        const hadFeedback = !!answerButton.querySelector(".feedback");
                        answersContainer.querySelectorAll(".feedback").forEach(f => f.remove());
                        if (!hadFeedback) {
                            answerButton.innerHTML += `<span class="feedback">?</span>`;
                        }
                        return;
                    }

                    stan.abcd = i;
                    sprawdzone = false;
                    stan.sprawdzone = false;
                    if (natychmiastowaOcenaAktywna()) {
                        ocenAbcd();
                    } else {
                        // Tryb „sprawdź później": tylko neutralne zaznaczenie, bez
                        // odsłaniania poprawności; ocenę odkryje przycisk „sprawdź".
                        abcdButtons.forEach(b => b.classList.remove("correct", "incorrect", "selected"));
                        answerButton.classList.add("selected");
                        sprawdz.pokaz();
                    }
                    zapiszPostep();
                });
                abcdButtons.push(answerButton);
                answersContainer.appendChild(answerButton);
            });

            ocenTegoZadania = ocenAbcd;
            oczekujaceSprawdzenia.push({
                ocen: ocenAbcd,
                maZaznaczenie: () => Number.isInteger(stan.abcd),
                czySprawdzone: () => sprawdzone,
            });
        } else if (type === "PF") {
            // Prawda/Fałsz: każde stwierdzenie dostaje własny wiersz z przyciskami P i F.
            // Punkty (0 albo maxScore) wpadają dopiero, gdy WSZYSTKIE odpowiedzi są
            // zaznaczone i poprawne — jak w arkuszu CKE.
            answersContainer.classList.add("pf-container");
            const chosen = new Array(exercise.statements.length).fill(null);
            let sprawdzone = false;

            // Odsłonięcie oceny wszystkich wierszy (na podstawie chosen). Punkty
            // (0 albo maxScore) wpadają tylko, gdy WSZYSTKIE odpowiedzi są
            // zaznaczone i poprawne — jak w arkuszu CKE. Idempotentne.
            function ocenPf() {
                if (chosen.every(c => c === null)) return;
                pfButtons.forEach((btns, si) => {
                    btns.forEach(b => b.classList.remove("correct", "incorrect", "selected"));
                    if (chosen[si] === null) return;
                    const btn = chosen[si] ? btns[0] : btns[1];
                    btn.classList.add(chosen[si] === exercise.statements[si].answer ? "correct" : "incorrect");
                });
                const answeredAll = chosen.every(c => c !== null);
                const allCorrect = chosen.every((c, ci) => c === exercise.statements[ci].answer);
                setScore(answeredAll && allCorrect ? exercise.maxScore : 0);
                sprawdzone = true;
                stan.sprawdzone = true;
                sprawdz.schowaj();
                zapiszPostep();
            }
            const sprawdz = utworzPrzyciskSprawdz(answersContainer, ocenPf);

            exercise.statements.forEach((statement, si) => {
                const row = document.createElement("div");
                row.className = "pf-row";

                const label = document.createElement("span");
                label.className = "pf-text";
                label.innerHTML = `${si + 1}. ${statement.text}`;
                row.appendChild(label);

                const buttons = [];
                [["P", true], ["F", false]].forEach(([caption, value]) => {
                    const btn = document.createElement("button");
                    btn.textContent = caption;
                    btn.addEventListener("click", () => {
                        chosen[si] = value;
                        sprawdzone = false;
                        stan.sprawdzone = false;
                        stan.pf = [...chosen];
                        if (natychmiastowaOcenaAktywna()) {
                            ocenPf();
                        } else {
                            // Tryb „sprawdź później": tylko neutralne zaznaczenie
                            // w tym wierszu, bez odsłaniania poprawności.
                            buttons.forEach(b => b.classList.remove("correct", "incorrect", "selected"));
                            btn.classList.add("selected");
                            sprawdz.pokaz();
                        }
                        zapiszPostep();
                    });
                    buttons.push(btn);
                    row.appendChild(btn);
                });
                pfButtons.push(buttons);

                answersContainer.appendChild(row);
            });

            ocenTegoZadania = ocenPf;
            oczekujaceSprawdzenia.push({
                ocen: ocenPf,
                maZaznaczenie: () => chosen.some(c => c !== null),
                czySprawdzone: () => sprawdzone,
            });
        } else if (type === "multiSelect") {
            // Wybór kilku odpowiedzi: klik zaznacza (jasnoniebieska ramka), ponowny klik
            // odznacza. Gdy komplet już zaznaczony, klik kolejnej odpowiedzi podmienia
            // najdawniej wybraną (okno przesuwne) — nie trzeba nic ręcznie odklikiwać.
            // Ocena następuje dopiero po zaznaczeniu wymaganej liczby odpowiedzi;
            // punkty częściowe: po 1 pkt za każde trafienie (maxScore/wymagane).
            answersContainer.classList.add("multi-select-container");
            const required = exercise.correctAnswerIndices.length;
            const selected = new Set();
            const buttons = [];
            let sprawdzone = false;

            const note = document.createElement("div");
            note.className = "multi-select-note";
            note.textContent = `Wybierz ${required === 2 ? "dwie odpowiedzi" : required + " odpowiedzi"}.`;
            answersContainer.appendChild(note);

            // Neutralne pokazanie samego zaznaczenia (bez oceny) — tryb „sprawdź później".
            function pokazZaznaczenie() {
                buttons.forEach((btn, i) => {
                    btn.classList.remove("correct", "incorrect", "selected");
                    if (selected.has(i)) btn.classList.add("selected");
                });
            }

            // Odsłonięcie oceny: po skompletowaniu wymaganej liczby odpowiedzi
            // koloruje trafienia/pudła i przyznaje punkty częściowe (po równo za
            // trafienie). Przy niepełnym zaznaczeniu tylko pokazuje wybór (0 pkt) —
            // dokładnie tak jak dawne refresh(), więc w trybie natychmiastowym
            // zachowanie jest identyczne jak wcześniej.
            function ocenMulti() {
                buttons.forEach((btn, i) => {
                    btn.classList.remove("correct", "incorrect", "selected");
                    if (!selected.has(i)) return;
                    if (selected.size === required) {
                        btn.classList.add(exercise.correctAnswerIndices.includes(i) ? "correct" : "incorrect");
                    } else {
                        btn.classList.add("selected");
                    }
                });
                if (selected.size === required) {
                    const hits = [...selected].filter(i => exercise.correctAnswerIndices.includes(i)).length;
                    setScore(Math.round(exercise.maxScore * hits / required));
                    sprawdzone = true;
                    stan.sprawdzone = true;
                } else {
                    setScore(0);
                    sprawdzone = false;
                    stan.sprawdzone = false;
                }
                sprawdz.schowaj();
                zapiszPostep();
            }
            const sprawdz = utworzPrzyciskSprawdz(answersContainer, ocenMulti);

            exercise.answers.forEach((answer, i) => {
                const btn = document.createElement("button");
                btn.innerHTML = answer;
                btn.addEventListener("click", () => {
                    if (selected.has(i)) {
                        selected.delete(i);
                    } else {
                        // Komplet już zaznaczony? Klik nowej odpowiedzi podmienia
                        // najdawniej wybraną (okno przesuwne), więc nie trzeba nic
                        // ręcznie odklikiwać, żeby zmienić zdanie. Set zachowuje
                        // kolejność wstawiania → najstarszy wybór to pierwszy element.
                        if (selected.size >= required) {
                            selected.delete(selected.values().next().value);
                        }
                        selected.add(i);
                    }
                    sprawdzone = false;
                    stan.sprawdzone = false;
                    stan.multi = [...selected];
                    if (natychmiastowaOcenaAktywna()) {
                        ocenMulti();
                    } else {
                        // Tryb „sprawdź później": tylko zaznaczenie; „sprawdź"
                        // pojawia się dopiero po skompletowaniu wyboru.
                        pokazZaznaczenie();
                        if (selected.size === required) sprawdz.pokaz();
                        else sprawdz.schowaj();
                    }
                    zapiszPostep();
                });
                buttons.push(btn);
                multiButtons.push(btn);
                answersContainer.appendChild(btn);
            });

            ocenTegoZadania = ocenMulti;
            oczekujaceSprawdzenia.push({
                ocen: ocenMulti,
                maZaznaczenie: () => selected.size === required,
                czySprawdzone: () => sprawdzone,
            });
        } else if (type === "open" && exercise.selfScore && exercise.maxScore) {
            // Textarea na własną odpowiedź / tok rozwiązania. OSOBNY kontener
            // (nie w .self-score-container, bo ta jest chowana w trybie egzaminu):
            // podczas egzaminu samoocena znika, ale uczeń ma tu gdzie zapisać
            // rozwiązanie, a po egzaminie — gdy rozwiązania i samoocena wracają —
            // porównuje wpisany tok z kluczem i przyznaje sobie punkty. Zapis
            // idzie do localStorage tą samą drogą co reszta odpowiedzi (stan.open).
            const openBox = document.createElement("div");
            openBox.className = "open-answer-container";

            const openLabel = document.createElement("div");
            openLabel.className = "open-answer-label";
            openLabel.textContent = "Twoja odpowiedź / tok rozwiązania:";
            openBox.appendChild(openLabel);

            openTextarea = document.createElement("textarea");
            openTextarea.className = "open-answer";
            openTextarea.rows = 4;
            openTextarea.placeholder = "Zapisz tu swoją odpowiedź lub tok rozwiązania — po odsłonięciu rozwiązania porównasz je z kluczem i ocenisz się.";
            openTextarea.addEventListener("input", () => {
                stan.open = openTextarea.value;
                zapiszPostep();
                // W trybie "tylko wypełnione" wpisanie tekstu w fazie "oceń się"
                // ma od razu dołożyć kropkę temu zadaniu (poza tą fazą no-op).
                odswiezWskaznikiOtwarte();
            });
            openBox.appendChild(openTextarea);
            answersContainer.appendChild(openBox);

            // Zadanie otwarte z samooceną: uczeń rozwiązuje na kartce, porównuje
            // z rozwiązaniem i sam przyznaje sobie punkty (0..maxScore).
            const box = document.createElement("div");
            box.className = "self-score-container";

            const label = document.createElement("div");
            label.className = "self-score-label";
            label.textContent = "Rozwiąż na kartce, porównaj z rozwiązaniem i oceń się:";
            box.appendChild(label);

            const buttons = [];
            for (let n = 0; n <= exercise.maxScore; n++) {
                const btn = document.createElement("button");
                btn.textContent = `${n} pkt`;
                btn.addEventListener("click", () => {
                    buttons.forEach(b => b.classList.remove("selected"));
                    btn.classList.add("selected");
                    setScore(n);
                    stan.self = n;
                    zapiszPostep();
                    // Zadanie właśnie ocenione — jego wskaźnik (jeśli był) znika.
                    odswiezWskaznikiOtwarte();
                });
                buttons.push(btn);
                selfButtons.push(btn);
                box.appendChild(btn);
            }
            answersContainer.appendChild(box);

            // Do rejestru dla pływających wskaźników „oceń się" po egzaminie.
            // Numer bierzemy z treści („Zadanie N."), NIE z index+1 — indeksy
            // w tablicy rozjeżdżają się z numeracją CKE przez zadania nadrzędne
            // (maxScore: 0) i wieloczęściowe (kilka wpisów „Zadanie 12/17").
            const qText = (exerciseClone.querySelector(".question")?.textContent) || "";
            const mNumer = qText.match(/Zadanie\s*(\d+(?:\.\d+)?)/i);
            const numer = mNumer ? mNumer[1] : String(index + 1);
            zadaniaOtwarte.push({ el: exerciseClone, stan, numer });
        } else if (type === "fillIn") {
            // Zadanie z polami do uzupełnienia ("...") — uczeń wpisuje odpowiedzi
            // ręcznie, a przycisk "Sprawdź" koloruje ramki pól na zielono/czerwono
            // i przyznaje punkty proporcjonalnie do trafień (po równo za pole).
            // Wpis porównujemy z listą akceptowanych wariantów po normalizacji
            // (patrz normalizeAnswer), więc "(−4, 4⟩" i "(-4,4>" są równoważne.
            answersContainer.classList.add("fill-in-container");

            exercise.blanks.forEach(blank => {
                const row = document.createElement("div");
                row.className = "fill-in-row";

                const label = document.createElement("span");
                label.className = "fill-in-label";
                label.innerHTML = blank.label;
                row.appendChild(label);

                const input = document.createElement("input");
                input.type = "text";
                input.className = "fill-in-input";
                // Edycja pola kasuje jego poprzednią ocenę, żeby kolor nie kłamał.
                input.addEventListener("input", () => {
                    input.classList.remove("correct", "incorrect");
                });
                row.appendChild(input);

                answersContainer.appendChild(row);
                fillRows.push({ blank, input });
            });

            fillCheck = document.createElement("button");
            fillCheck.className = "fill-in-check";
            fillCheck.textContent = "Sprawdź";
            fillCheck.addEventListener("click", () => {
                let trafienia = 0;
                fillRows.forEach(({ blank, input }) => {
                    const wpis = normalizeAnswer(input.value);
                    const ok = wpis !== "" && blank.accepted.some(acc => normalizeAnswer(acc) === wpis);
                    input.classList.remove("correct", "incorrect");
                    input.classList.add(ok ? "correct" : "incorrect");
                    if (ok) trafienia++;
                });
                setScore(Math.round(exercise.maxScore * trafienia / fillRows.length));
                stan.fill = fillRows.map(r => r.input.value);
                zapiszPostep();
            });
            answersContainer.appendChild(fillCheck);
        }

        // Set score. Zadanie nadrzędne (maxScore: 0, np. wspólny wstęp Zadania 12/17)
        // nie ma badge'a punktów wcale — usuwamy go z DOM (samo display:none nie
        // wystarczy, bo przełącznik widoku punktów ustawia display na wszystkich
        // .exercise-score i by go przywrócił).
        if (exercise.maxScore) {
            scoreSpan.textContent = `0 / ${exercise.maxScore} pkt`;
        } else {
            scoreSpan.remove();
        }

        // Set hint — przycisk "Podpowiedź" znika, gdy zadanie nie ma podpowiedzi.
        const hintContainer = exerciseClone.querySelector(".hint-container");
        const hasHint = !!(exercise.hint && exercise.hint.trim() !== "");
        hintContainer.innerHTML = exercise.hint || "";
        if (!hasHint) {
            exerciseClone.querySelector(".hint-button").style.display = "none";
        }

        // Set solution
        const solutionContainer = exerciseClone.querySelector(".solution-container");
        const solutionTextContainer = solutionContainer.querySelector(".solution-text-container");

        const solutionStepByStepContainer = exerciseClone.querySelector(".solution-step-by-step-container");

        const solutionInteractiveContainer = exerciseClone.querySelector(".solution-interactive-container");

        const solutionTextMoreContainer = solutionContainer.querySelector(".solution-text-more-container");
        const solutionTextMoreSpan = solutionTextMoreContainer.querySelector(".solution-text-more");
        const showMoreButton = solutionTextMoreContainer.querySelector("button");

        // Set solutionTextMore content
        solutionTextMoreSpan.innerHTML = exercise.solutionTextMore || "";

        // Initially hide the solutionTextMore content
        solutionTextMoreSpan.style.display = "none";

        // Add click event listener to show/hide button
        showMoreButton.addEventListener("click", () => {
            if (solutionTextMoreSpan.style.display === "none") {
                solutionTextMoreSpan.style.display = "block";
                showMoreButton.textContent = "Schowaj więcej";
            } else {
                solutionTextMoreSpan.style.display = "none";
                showMoreButton.textContent = "Pokaż więcej";
            }
        });

        // Hide the entire container if there's no solutionTextMore content
        if (!exercise.solutionTextMore || exercise.solutionTextMore.trim() === "") {
            solutionTextMoreContainer.style.display = "none";
        }

        solutionTextContainer.innerHTML = exercise.solutionText || "";

        // Widżet interaktywny: w danych (JSON) jest tylko NAZWA widżetu (string),
        // funkcję bierzemy z rejestru WIDZETY (widgets/_registry.js, załadowany
        // przed tym plikiem — patrz kolejność <script> w template.html).
        if (exercise.solutionWidget) {
            const widget = WIDZETY[exercise.solutionWidget];
            if (widget) {
                widget(solutionInteractiveContainer);
            } else {
                console.warn(`Zadanie ${numerZadania(exercise, index)}: nieznany widżet "${exercise.solutionWidget}"`);
            }
        }

        // Add event listeners for hint and solution buttons
        const formulasButton = exerciseClone.querySelector(".formulas-button")

        if(exercise.formulasPage != null){
            formulasButton.addEventListener("click", () => {
                openFormulasAtPage(exercise.formulasPage)
            });
        }else{
            formulasButton.style.display = "none";

        }

        exerciseClone.querySelector(".hint-button").addEventListener("click", () => {
            hintContainer.style.display = hintContainer.style.display === "block" ? "none" : "block";
            solutionContainer.style.display = "none";
        });

        // SOLUTION STEP BY STEP
        // Właściwy podsystem kroków (renderStep/showStep/podepnijSterowanieWideo)
        // mieszka w app/steps.js. Tu tylko zbieramy refy DOM kroków, budujemy stan
        // wspólny (krokiCtx) i podpinamy strzałki ◄/► oraz przycisk "Rozwiązanie".
        const stepsContent = solutionStepByStepContainer.querySelector(".steps-content");
        const stepsNav = solutionStepByStepContainer.querySelector(".steps-nav");
        const prevBtn = stepsNav.querySelector(".step-prev");
        const nextBtn = stepsNav.querySelector(".step-next");
        const stepCounter = stepsNav.querySelector(".step-counter");

        const hasSteps = Array.isArray(exercise.solutionStepByStep);
        const steps = hasSteps ? exercise.solutionStepByStep : [];

        // Separator (dolna kreska) rozdziela kolejne bloki rozwiązania. Pod ostatnim
        // widocznym blokiem jest zbędny (np. gdy rozwiązanie to sam tekst) — zdejmujemy
        // go z ostatniego widocznego bloku.
        const hasText = !!(exercise.solutionText && exercise.solutionText.trim() !== "");
        const hasInteractive = !!(exercise.solutionWidget && WIDZETY[exercise.solutionWidget]);
        const hasMore = !!(exercise.solutionTextMore && exercise.solutionTextMore.trim() !== "");
        const solutionBlocks = [
            hasText ? solutionTextContainer : null,
            hasSteps ? solutionStepByStepContainer : null,
            hasInteractive ? solutionInteractiveContainer : null,
            hasMore ? solutionTextMoreContainer : null,
        ].filter(Boolean);
        if (solutionBlocks.length) {
            solutionBlocks[solutionBlocks.length - 1].style.borderBottom = "none";
        }

        // Przycisk "Rozwiązanie" ma sens tylko, gdy istnieje jakiekolwiek rozwiązanie
        // (tekst / kroki / interaktywne / "pokaż więcej"). W przeciwnym razie go chowamy.
        const hasAnySolution = solutionBlocks.length > 0;
        const solutionButton = exerciseClone.querySelector(".solution-button");
        if (!hasAnySolution) {
            solutionButton.style.display = "none";
        }
        // Rejestr dla przycisku "pokaż wszystkie rozwiązania" w pasku.
        wszystkieRozwiazania.push({ przycisk: solutionButton, panel: solutionContainer, ma: hasAnySolution });

        // Stan wspólny kroków przekazywany do showStep (app/steps.js). currentStep
        // i stepSwapToken MUSZĄ być te same dla showStep i strzałek ◄/►, dlatego
        // trzymamy je w jednym obiekcie (nie kopiujemy wartości).
        const krokiCtx = {
            currentStep: 0,
            stepSwapToken: 0,
            steps,
            stepsContent,
            prevBtn,
            nextBtn,
            stepCounter,
            exerciseClone,
        };

        if (hasSteps) {
            prevBtn.addEventListener("click", () => {
                if (krokiCtx.currentStep > 0) showStep(krokiCtx, krokiCtx.currentStep - 1);
            });
            nextBtn.addEventListener("click", () => {
                if (krokiCtx.currentStep < steps.length - 1) showStep(krokiCtx, krokiCtx.currentStep + 1);
            });
        }

        // Jeden handler przycisku "Rozwiązanie": chowa podpowiedź, przełącza panel
        // rozwiązania, a gdy zadanie ma kroki — pokazuje je i renderuje bieżący krok
        // (kroki pojawiają się dopiero po tym kliknięciu, ostatni woła markCorrectAnswer).
        solutionButton.addEventListener("click", () => {
            hintContainer.style.display = "none";
            solutionContainer.style.display = solutionContainer.style.display === "block" ? "none" : "block";

            if (hasSteps) {
                solutionStepByStepContainer.style.display = "block";
                showStep(krokiCtx, krokiCtx.currentStep);
            } else {
                solutionStepByStepContainer.style.display = "none";
            }
        });


        // Przywrócenie postępu: symulujemy dokładnie te kliknięcia/wpisy, które
        // użytkownik wykonał wcześniej — ocena i punkty liczą się tą samą drogą,
        // więc nie ma drugiej, równoległej logiki oceniania do utrzymywania.
        const zap = zapis ? zapis.stany[index] : null;
        if (zap) {
            if (Number.isInteger(zap.abcd) && abcdButtons[zap.abcd]) {
                abcdButtons[zap.abcd].click();
            }
            if (Array.isArray(zap.pf)) {
                zap.pf.forEach((wybor, si) => {
                    if (wybor !== null && pfButtons[si]) pfButtons[si][wybor ? 0 : 1].click();
                });
            }
            if (Array.isArray(zap.multi)) {
                zap.multi.forEach(i => { if (multiButtons[i]) multiButtons[i].click(); });
            }
            if (Number.isInteger(zap.self) && selfButtons[zap.self]) {
                selfButtons[zap.self].click();
            }
            if (typeof zap.open === "string" && openTextarea) {
                // stan.open jest już ustawiony (zasiany z zapisu przed pętlą forEach
                // wyżej), więc samo ustawienie .value wystarczy — nie trzeba drugi
                // raz przypisywać stan.open (input i tak się tu nie odpala).
                openTextarea.value = zap.open;
            }
            if (Array.isArray(zap.fill) && fillRows.length) {
                zap.fill.forEach((tekst, i) => { if (fillRows[i]) fillRows[i].input.value = tekst || ""; });
                if (zap.fill.some(t => t) && fillCheck) fillCheck.click();
            }
            // Tryb „sprawdź później" (natychmiastowa poprawność OFF): powyższe kliki
            // odtworzyły tylko ZAZNACZENIE (bez koloru). Jeśli użytkownik przed
            // odświeżeniem odsłonił ocenę (klik „sprawdź"), odtwórz też odsłonięcie —
            // inaczej po reloadzie zniknąłby kolor i punkty za to zadanie. W trybie
            // natychmiastowym klik już ocenił, a ocenTegoZadania jest idempotentne.
            if (zap.sprawdzone && ocenTegoZadania) ocenTegoZadania();
        }

        // Obrazki osadzone w HTML zadania (treść, podpowiedź, rozwiązanie) mają
        // w danych ścieżki względne do folderu arkusza (np. "media/zad11/…") —
        // przepisujemy je przez mediaPath, bo strona renderuje się z rootu.
        // (Filmy/obrazki kroków step-by-step idą osobno przez renderStep.)
        exerciseClone.querySelectorAll("img[src]").forEach((img) => {
            img.setAttribute("src", mediaPath(img.getAttribute("src")));
        });

        // KaTeX: renderujemy wzory w całym zbudowanym zadaniu (treść, odpowiedzi,
        // podpowiedź, rozwiązania). Kroki step-by-step renderują się osobno w
        // showStep(), bo ich HTML powstaje dopiero przy przełączaniu kroków.
        renderMath(exerciseClone);

        // Dyskretny link „zgłoś błąd w tym zadaniu" pod zadaniem (app/report.js).
        // Widoczność steruje globalnie klasa body.bez-zglaszania (toggle w menu ⋯).
        dodajLinkZgloszenia(exerciseClone);

        // Append the exercise to the wrapper
        exercisesWrapper.appendChild(exerciseClone);
    });

    // Arkusz faktycznie wyrenderowany — dopiero teraz mają sens przyciski
    // zależne od jego zawartości (np. start egzaminu w stopce, style/exam.css).
    // Bez tej klasy strona błędu (zły ?arkusz=) albo czas wczytywania
    // exercises.json pokazywałyby te przyciski na pusto.
    document.body.classList.add("arkusz-wczytany");
}
