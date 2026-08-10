Dziennik ukończonych zadań, partia bieżąca (otwarta 2026-07-27). Zasady formatu i podziału na pliki: patrz done/README.md — najnowsze wpisy na górze.

[ZROBIONE 2026-08-10] (Opus 5 High) Kontener, paczka trzech zmian: brama w firewallu zawężona
do samego DNS, `.vscode/` read-only, automatyczny pull przy starcie faktycznie działa.

**1. Firewall — brama tylko 53/udp + 53/tcp** (`.devcontainer/init-firewall.sh`).
Były tam dwie bezwarunkowe reguły (`-A INPUT -s $HOST_IP -j ACCEPT` i `-A OUTPUT -d $HOST_IP`),
czyli WSZYSTKIE porty bramy. Pod pastą bramą jest prawdziwy router, więc skan `192.168.1.1`
z kontenera pokazywał otwarte 80, 443, 445 (SMB) i 631 (IPP) — panel WWW, udziały plików
i drukarka. Zastąpione dwiema regułami OUTPUT na port 53. Ruch zwrotny NIE dostał własnej
reguły: sprawdzone, że łańcuch INPUT ma niżej `ESTABLISHED,RELATED`, a conntrack śledzi także
UDP. TCP obok UDP jest konieczne — odpowiedzi >512 B (flaga TC) wymuszają ponowienie po TCP.
Reguła na 53 w ogóle zostaje tylko jako zabezpieczenie przenośności: pod pastą resolwerem
z `resolv.conf` jest `169.254.1.1` (nie brama), więc te dwie linie są tam martwe — ale gdy
resolwerem jest sam router, są jedyną furtką. Istniejący bezpiecznik (`dig api.github.com` →
przy braku odpowiedzi przywraca ogólną regułę UDP 53 przez `-I`) pilnuje teraz OBU zawężeń
naraz, bo testuje efekt końcowy, a nie to, która reguła przepuściła pakiet.

**2. `.vscode/` montowane readonly** (`.devcontainer/devcontainer.json`), tak jak `.devcontainer/`.
Powód mniej oczywisty niż przy tamtym katalogu: `tasks.json` ma `"runOn": "folderOpen"`, czyli
polecenie powłoki uruchamiane przez VS Code SAMO, bez pytania, przy każdym otwarciu folderu.
Kontener mógłby podmienić `git pull --ff-only` na dowolną komendę i poczekać — a odpali się ona
tam, gdzie folder zostanie otwarty, czyli na hoście, poza izolacją, przy otwarciu repo lokalnie.
Sprzężenie z punktem 3 jest tu istotne: włączenie `task.allowAutomaticTasks` usuwa pytanie, które
było ostatnią barierą, więc te dwie zmiany muszą iść razem.

**3. Automatyczny `git pull` przy starcie faktycznie się odpala.** Zadanie z `runOn: folderOpen`
istniało od 2026-08-07, ale VS Code przy każdym otwarciu pytał „Allow Automatic Tasks in Folder?"
i do czasu odpowiedzi nie pullował. Brakowało `"task.allowAutomaticTasks": "on"` w GLOBALNYCH
(User) ustawieniach — tego przełącznika nie da się ustawić z workspace'u i to jest celowe,
inaczej repo przyznawałoby sobie samo prawo do uruchamiania poleceń. Dopisane w `~/.config/Code/User/
settings.json`. W `tasks.json` został komentarz o tej zależności.

**Przy okazji: skasowane osierocone dane po flatpakowym VS Code** (852 MB w
`~/.var/app/com.visualstudio.code/`). Sam flatpak był już odinstalowany — zostały po nim tylko
dane, ostatnio używane 2026-08-06. Zweryfikowane przed kasowaniem: `flatpak list` nie zna tej
aplikacji; z 14 rozszerzeń tylko 4 nie miały odpowiednika natywnie (GitLens, Containers, gitdoc,
Claude Code — wszystkie wracają z marketplace'u); `History/` zawierało wyłącznie stare wersje
`settings.json` i `.devcontainer/devcontainer.json` (ten drugi i tak jest w gicie);
`workspaceStorage/` dotyczyło tylko tego repo (stan UI, nie treść). Ustawienia, snippety i lista
rozszerzeń zachowane w `~/backup-vscode-flatpak/` (8 kB; Henrich zdecydował 2026-08-10, że tych
ustawień nie potrzebuje, ale backup na razie zostaje). Dwa ustawienia istniały TYLKO we flatpaku
i nie zostały przeniesione: `chat.viewSessions.orientation: "stacked"` i
`chat.agent.sandbox.enabled: "on"`; do tego `terminal.integrated.gpuAcceleration: "off"`, które
natywnie jest zakomentowane. Zostaje jedna instalacja — natywna przez rpm-ostree.

Przepis na powtórkę (jak wykryć sieroty w `~/.var/app`, jak sprawdzić dane przed kasowaniem
i których ustawień NIE przenosić — `flatpak-spawn --host podman` zepsułby natywne devcontenery)
zapisany w **issues/flatpak-osierocone-dane.md**.

Dokumentacja: `.devcontainer/README.md` — sekcja „Brama `/32`, nie `/24`" przepisana na
„Brama: `/24` → `/32` → tylko port 53" (z historią obu zawężeń), sekcja „`.devcontainer/`
tylko do odczytu" rozszerzona o `.vscode/`, w „Czego to NIE chroni" punkt o panelu WWW routera
przekreślony jako nieaktualny i dopisany punkt o DNS jako kanale danych, w „Diagnostyka" trzy
nowe objawy (DNS po zmianie reguł bramy — z komendami i opisem bezpiecznika; brak dostępu do
LAN-u jako zamierzony; brak zapisu do `.devcontainer`/`.vscode`). TODO.md: z punktu o świadomie
niedomkniętych dziurach usunięta część (1) o bramie, część (2) o GitHubie/npm została.

NIEZWERYFIKOWANE W MOMENCIE ZAPISU: zmiany robione z hosta (`.devcontainer/` jest w kontenerze
readonly), a `init-firewall.sh` jest kopiowany do obrazu, więc wszystko wymaga Rebuild Container.
Lista rzeczy do sprawdzenia po przebudowie trafiła do TODO.md → TESTOWANIE HENRICH.

[tagi: devcontainer, firewall, iptables, dns, podman, pasta, bezpieczenstwo, vscode, zadania]

[ZROBIONE 2026-08-09] (Sonnet 5) Test v14 przez Henricha — 2 z 3 punktów potwierdzone bez zastrzeżeń,
trzeci (dynamiczny podgląd hoveru) i pole „ostateczna odpowiedź" przepisane na nowe punkty w
TODO.md → DO ZROBIENIA:
- Hover myszą (tło na chrome, ramka na odpowiedziach ABCD/PF/„N pkt") — Henrich: „jest dobrze".
- Jasny motyw, poprawka kontrastu WCAG drobnych szarych tekstów — Henrich: „jest dobrze".

[ZROBIONE 2026-08-09] (Fable 5) Paczka 4 „Spójność UI, etap 2" — audyt całego style/, v14 Beta.

Zamknięte wszystkie punkty z issues/ui-spojnosc-etap2.md (plik przeniesiony do done/ui-spojnosc-etap2.md):
- **Zasada hoveru** zapisana w komentarzu przy `#naroznik-prawy button:hover` (sheet.css): chrome = podświetlone tło (decyzja Henricha), kontrolki treści = ciemniejsza ramka. Pigułki narożników, strzałka panelu i przełącznik motywu landingu przeszły z ramki na tło.
- **Hover na odpowiedziach** (ABCD/PF/„N pkt") — nowy, ramką `--border-strong`, z `:not(...)` na stany poprawne/błędne/.selected.
- **Skala kontrolek karty zadania** — trzy klasy (duża 18px / kontrolka 17px, 8px 11px / tekstowa 16px) opisane przy banerze „PRZYCISKI ODPOWIEDZI"; ujednolicone paddingi pól fillIn i „ostatecznej odpowiedzi" (6px 8px → 8px 11px) oraz oba przyciski „Sprawdź" (wspólne 15px / 8px 18px).
- **`--shadow-modal`** — nowy token (oba ciemne bloki) zamiast cienia wpisanego na sztywno w oknie podsumowania egzaminu; okno dostało też `--radius-kontrolka` (było ostatnią „kartą" z ostrymi rogami).
- **Ramki 2px → 1px** tam, gdzie grubość nic nie kodowała: `#wskazniki-ukryj` i trzy separatory bloków rozwiązania (`.solution-text/step-by-step/interactive-container`).
- **Landing vs arkusz**: typografia już spójna (lede/CTA 18px = treść zadania; CTA świadomie trzyma wagę w rozmiarze — komentarz z 2026-07-27), zapisana komentarzem przy `.landing-lede`. Kontrast WCAG zmierzony z getComputedStyle w obu motywach: jedyny oblewający był jasny `--text-faint` #858585 (3.7:1 przy 13px) → #767676 (4.54:1); ciemny motyw przechodził w całości. Zamyka to też issues/dark-mode-css-zmienne-landing.md (punkty --border-close/--bg-hover naprawione już wcześniej, plik usunięty).
- Punkty rozstrzygnięte decyzjami Henricha, bez zmian w kodzie: karta zadania bez ramki/zaokrągleń, marginesy w obecnych proporcjach.
Weryfikacja: komplet 16 zrzutów przed/po + ujęcia celowane (podsumowanie egzaminu, pola zadań otwartych, hovery, separatory) + liczbowo przez getComputedStyle. ARCHITECTURE_CSS.md zaktualizowany (sekcja „Shape tokens": zasada hoveru, --shadow-modal, skala kontrolek).

[tagi: css, ui, tokeny, hover, wcag, kontrast, landing, egzamin, spojnosc]

[ZROBIONE 2026-08-09] (Opus 5 Medium) Fałszywy alarm: blokada scrolla pod panelem bocznym
na Pixelu 7a — to był cache przeglądarki, nie błąd.

Po wypchnięciu v13 Henrich zgłosił, że na Pixelu 7a (GrapheneOS) arkusz nadal przewija się
pod otwartym panelem, mimo że w Chromium i w symulowanym telefonie w Firefoksie blokada
działa. Wpis trafił do TODO.md razem z czterema tropami (visual viewport przy przybliżonej
stronie, próg 1300px liczony z `innerWidth`, brak `touch-action` na `#sidebar-przyciemnienie`,
pokrewieństwo z issues/zadania-nie-renderuja-sie-mobile.md).

**Po odświeżeniu strony na telefonie blokada zadziałała poprawnie** — w symulowanym Firefoksie
również. Żaden z tropów nie okazał się potrzebny; telefon trzymał starą wersję plików.
Punkt usunięty z TODO.md bez żadnej zmiany w kodzie. Mechanizm z v13 zostaje bez poprawek:
`body.blokada-scrolla` (`position: fixed` + zapamiętany `scrollY` w ujemnym `top`), zakładana
poniżej progu 1300px — `app/bootstrap.js`, `style/sheet.css:175`.

**Wniosek na przyszłość, wart zapamiętania przy każdym teście na telefonie:** pierwszy objaw
po wdrożeniu bywa cache'em, nie regresją. Numer wersji przy logo („vN Beta") istnieje dokładnie
po to — zanim ktokolwiek zacznie diagnozować zgłoszenie z telefonu, warto najpierw sprawdzić,
czy w rogu widnieje ta wersja, która zawiera poprawkę. Tu tego kroku zabrakło i kosztowało
to wpis w TODO.md plus cztery hipotezy do zbadania.

Przy okazji tej samej sesji Henrich potwierdził, że **zadania renderują się na Pixelu 7a
poprawnie** — dotyczy to issues/zadania-nie-renderuja-sie-mobile.md, ale że tamta awaria bywała
przerywana, plik zostaje w issues/ do świadomej decyzji Henricha, a nie zamykany przy okazji.

[tagi: mobile, cache, panel-boczny, falszywy-alarm]


[ZROBIONE 2026-08-09] (Opus 5 Medium) Paczka 3 „Kolory i motyw ciemny" + dwie dokładki
z issues/plan-ui-paczki-2026-08.md (wersja v13 Beta):

1. **Tło widżetów w ciemnym = tło strony.** Przyczyną nie był żaden styl widżetu, tylko osobny
   token `--canvas-bg` (`canvas { background-color: var(--canvas-bg) }` w sheet.css): w ciemnym
   miał `#1c1c1c` przy tle strony `#141414`. Ustawiony na `#141414` w OBU blokach ciemnej palety
   w base.css. Zweryfikowane `getComputedStyle`: ciemny `rgb(28,28,28)` → `rgb(20,20,20)` = body;
   jasny bez zmian, potwierdzone liczbowo `rgb(255,255,255)` = body.
2. **Tło formularza zgłoszenia — „coś pomiędzy".** Żaden istniejący token nie pasował
   (`--bg-subtle` #222 zmieniłby też jasny motyw na jaśniejszy), więc nowy `--bg-formularz`:
   jasny `#f7f7f7` (dokładnie jak dotąd, zero zmian), ciemny `#1e1e1e` między tłem strony
   `#141414` a `--bg-muted` `#262626`. `.zglos-blad-okno` czyta ten token.
3. **„Zgłoś błąd pod zadaniem" blokowane w egzaminie** — `zglos-blad-toggle` dopisany do
   `OPCJE_MENU_EGZAMIN` w app/exam.js (linki „zgłoś błąd" i tak znikają w egzaminie razem
   z `.light-button-container`). `enableExamMode()` zamyka dodatkowo otwarty formularz, bo jego
   kotwica właśnie znikała i blok zostawał wiszący. Sprawdzone: w egzaminie `disabled=true`,
   `opacity 0.4`, formularz `display:none`; po zakończeniu egzaminu wraca `disabled=false`.
4. **Otwarty panel boczny nie przewija arkusza pod spodem.** `body.blokada-scrolla`
   (`position: fixed`, sheet.css) + w app/bootstrap.js `zablokujScrollTla()`/`odblokujScrollTla()`
   zapamiętujące pozycję w ujemnym `top` i przywracające ją `scrollTo` — świadomie nie
   `overflow: hidden`, bo na iOS nie działa, i z zapamiętaniem pozycji, bo `position: fixed`
   sam z siebie skacze na górę. Zakładane tylko poniżej progu 1300 px (`sidebarNaklada()`),
   plus handler `resize` zdejmujący blokadę po przekroczeniu progu z otwartym panelem.
   Test (390×780, hasTouch): pozycja 900 → w trakcie `top:-900px`, po zamknięciu znów 900;
   swipe w lewo z paczki 2 nadal zwija panel i zdejmuje blokadę. Panel jest `position: fixed`
   z `overflow-y: auto`, więc reguła go nie dotyczy i scroll w środku zostaje.

[ZROBIONE 2026-08-09] (Opus 5 Medium) Paczka 2 „Panel boczny" z issues/plan-ui-paczki-2026-08.md
(wszystkie pięć punktów, wersja v12 Beta):

1. **„Sprawdź wszystkie odpowiedzi" nie znika i panel nie skacze.** Reguły `display:none` /
   `body.reczne-sprawdzanie #sprawdz-wszystkie` w style/exam.css usunięte; pozycja jest teraz
   stale w panelu, a przy poprawności „natychmiast" tylko `disabled`. Potwierdzone pomiarem:
   `top` sąsiedniej pozycji przed i po przełączeniu = 337.78 px, bez zmiany.
2. **„Poprawność" wyszarzona w egzaminie** — `natychmiastowa-toggle` dopisany do
   `OPCJE_MENU_EGZAMIN` (w egzaminie poprawność jest i tak ukryta, więc przełączanie „kiedy ją
   pokazać" niczego nie zmieniało).
   Mechanizm z punktów 1–2 to jedna funkcja `odswiezBlokadyMenu()` w app/exam.js, która zastąpiła
   `setExamMenuDisabled()`: dwa niezależne powody blokady (egzamin, tryb poprawności) sumują się
   w jednym miejscu, bo przy dwóch osobnych setterach koniec egzaminu odblokowywałby „sprawdź
   wszystkie" niezależnie od trybu poprawności. Funkcja odkłada oryginalny `title` w
   `dataset.titleBazowy`, żeby odblokowanie go nie skasowało. Wołana też z
   `odswiezTrybPoprawnosci()` w app/bootstrap.js. Wygląd `:disabled` przeniesiony z exam.css do
   sheet.css jako `#sidebar button:disabled` (blokada nie jest już tylko egzaminacyjna).
3. **Przełączniki przestały wyglądać na wyłączone**: etykieta wiersza ustawienia
   `--text-faint-2` → `--text-muted` (#909090→#555 / #8c8c8c→#bcbcbc), nieaktywna kropka stanu
   `--border-muted` → `--border-strong`. To warunek konieczny punktów 1–2: „wyszarzone" musi
   teraz znaczyć „wyłączone", a nie „domyślne".
4. **Bleeding/bloom stanów przełącznika**: przyczyną była WAGA, nie kontrast tła. Lora jest
   szeryfowa i mocno kontrastowa; jej odmiana 600 przy 12px zlepiała szeryfy w plamę (najgorzej
   jasny tekst na ciemnym). Zdiagnozowane porównaniem 600/400 × 12/13px w powiększeniu ×5 na
   pojedynczym wierszu. Fix: `.sidebar-ustawienie .wartosc` → `font-weight: 400` przy tym samym
   12px (zero ryzyka dla szerokości wiersza); hierarchię wobec etykiety trzyma teraz kolor
   (--text vs --text-muted) i kropki.
5. **Swipe w lewo zwija panel na telefonie** (app/bootstrap.js). Listenery touchstart/move/
   cancel/end wyłącznie na `#sidebar`, wszystkie `passive: true` i bez `preventDefault()` — gest
   tylko obserwuje dotyk, więc nie może przechwycić ani pionowego scrolla panelu, ani
   przeciągania po treści zadania. Progi: ≥60px w poziomie, ≤45px w pionie, |dx| > 1,5·|dy|,
   ≤700 ms, ≥0,25 px/ms; dotyk zaczęty <24px od prawej krawędzi jest ignorowany (strefa
   systemowego gestu „do przodu"), drugi palec kasuje gest. Przetestowane 7 scenariuszy dotyku
   w Playwright (hasTouch, CDP Input.dispatchTouchEvent): swipe w lewo zwija; scroll pionowy,
   muśnięcie, wolne przeciąganie, ukos, swipe w prawo i start przy prawej krawędzi — nie zwijają.

Weryfikacja: tools/zrzuty.js --przed/--po (16 ujęć) + własne zbliżenia na `#sidebar` i pojedyncze
wiersze w ×4/×5, jasny i ciemny, ćwiczenia i egzamin; osobny test funkcjonalny przejść stanu
(ćwiczenia → egzamin → koniec egzaminu → zmiana poprawności) bez błędów JS.
Płynność gestu na prawdziwym telefonie i odczucie „w sam raz mocne" idą na listę TESTOWANIE HENRICH.
[css, ui, panel-boczny, sidebar, dotyk, gesty, egzamin, kontrast, typografia]

[ZROBIONE 2026-08-09] (Sonnet 5 High) Paczka 1 „Drobnica" z issues/plan-ui-paczki-2026-08.md:
napis „Sprawdź obliczenia" → „Sprawdzanie obliczeń" (render.js + exam.js + template.html +
ARCHITECTURE.md/OVERVIEW.md); pigułka punktowa `.exercise-score` przy każdym zadaniu przysunięta
~40px bliżej treści karty (`right: -120px` → `-80px` w style/sheet.css:586, próg zawijania na
telefon w responsive.css nieruszony — poprawka dotyczy tylko szerokiego ekranu; pierwsza wersja
tego punktu błędnie ruszała `#total-score` w górnym pasku zamiast tego — cofnięte, pasek wrócił
do stanu sprzed paczki); stopka arkusza (template.html) i landing (index.html) dostały linijkę
„© 2026 Henrich2137 · Licencja” (nowe klasy .stopka-copyright / .landing-footer a); row-gap
wiersza przycisków (Podpowiedź/Rozwiązanie/Zgłoś błąd/Pokaż wzory) na telefonie 10px→20px.
Zweryfikowane zrzutami Playwright (jasny/ciemny × desktop/telefon, w tym wariant „0 / 4 pkt")
na template.html i index.html.  [css, ui, stopka, tekst, drobnica]

[ZROBIONE 2026-08-09] (Opus 5) Devcontainer nie wstawał: `mkdir: cannot create directory
'/vscode/vscode-server/bin': Permission denied`. Diagnoza i naprawa, zero zmian w plikach repo.

PRZYCZYNA. Rozszerzenie Dev Containers samo tworzy nazwany wolumen `vscode` montowany pod
`/vscode` (cache serwera VS Code między przebudowami) — nie ma go w `devcontainer.json`, dzieje
się pod spodem. Ten wolumen powstał 2026-08-06 z właścicielem ns-uid 1000 = host uid **525287**,
czyli tak, jakby tworzył go kontener BEZ `--userns=keep-id`. Tymczasem właściwy devcontainer
działa Z keep-id (`remoteUser: node` + `updateRemoteUserUID: false` → rozszerzenie dokłada
`--userns=keep-id` pod podmanem), gdzie `node` = host uid **1000**. Rozjazd uid → brak zapisu
do `/vscode`. Potwierdzone liczbowo: `UidMap ["0:1:1000","1000:0:1","1001:1001:64536"]` —
`1000:0:1` to właśnie keep-id. Dla porównania wolumen `matematykazen-claude-config` był i jest
zdrowy (host uid 1000), bo Dockerfile chownuje `/home/node/.claude`, a podman przy pierwszym
montowaniu robi copy-up i przenosi na wolumen właściciela katalogu z obrazu.

WYZWALACZ. Henrich robił porządki na dysku (`podman prune` i podobne). `system prune -a` nie
kasuje nazwanych wolumenów, ale usunął stary, DZIAŁAJĄCY kontener — a rozszerzenie utworzyło
nowy, który podpiął się pod stary wolumen z 6 sierpnia o niepasującym uid. Poszlaka: ostatni
zapis w `matematykazen-claude-config` to 08-08 16:39, a kontener powstał 09-08 00:51, czyli
najpewniej nigdy poprawnie nie wystartował.

NAPRAWA. `podman rm <kontener>` (zatrzymany kontener w stanie `exited` nadal trzyma referencję
do wolumenu i blokuje `volume rm` — to NIE jest hibernacja), potem `podman volume rm vscode`
(bezpieczne: wolumen miał 0 bajtów, to wyłącznie cache binarki serwera), potem rebuild z VS Code.
Po odtworzeniu wolumen miał już poprawnego właściciela (host uid 1000), a ostatecznie środowisko
wstało po restarcie hosta. Wykluczone po drodze: obraz kontenera (nowy kontener, ten sam poprawny
obraz) oraz SELinux (host `Enforcing`, ale kontener dostaje `--security-opt label=disable`).

CZEGO NIE RUSZAĆ przy przyszłym sprzątaniu: wolumenu `matematykazen-claude-config` (tam siedzi
`.credentials.json` z logowaniem Claude Code, `projects/`, `sessions/`) ani wolumenu `open-webui`
(2,9 GB, obca usługa). `podman volume prune` i `system prune -a --volumes` są NIEBEZPIECZNE —
gdy devcontainer nie działa, jego wolumen liczy się jako nieużywany i leci. Wolumeny usuwać
zawsze imiennie. Gdyby problem wrócił, utwardzenie to `RUN mkdir -p /vscode && chown -R
node:node /vscode` w `.devcontainer/Dockerfile` przed `USER node` (ten sam mechanizm copy-up,
który uratował `/home/node/.claude`); awaryjnie `podman volume create vscode` +
`podman unshare chown 0:0 <mountpoint>` (ns 0 = host 1000 = `node` pod keep-id).
Uwaga na przyszłość: rozszerzenie WZNAWIA istniejący kontener po etykietach
`devcontainer.local_folder` — samo „Reopen in Container" nie tworzy nowego, dopiero `podman rm`.

[ZROBIONE 2026-08-07] (Opus 5 Medium) Konfiguracja narzędzi, zero zmian w kodzie strony:

1. Auto-fetch + auto-pull przy starcie VS Code. `.vscode/settings.json` → `git.autofetch: true`
   (fetch w tle co ~3 min, nic nie scala), `.vscode/tasks.json` → task `git pull --ff-only`
   z `runOn: folderOpen` (pull raz, przy otwarciu folderu). Świadomie natywnym mechanizmem VS Code,
   a NIE przez `gitdoc.pullOnOpen`: gitdoc jest pakietem wszystko-albo-nic, więc włączenie go dla
   samego pull-on-open wróciłoby z auto-commitem i `forcePush` (wyłączonymi celowo 2026-08-01).
   `--ff-only` z założenia — nigdy nie nadpisze lokalnych commitów, przy rozjeździe po prostu nie
   wykona się. Oba pliki śledzone przez gita, więc działa tak samo w kontenerze i poza nim (o to
   chodziło Henrichowi: parytet obu środowisk). Na nowej maszynie VS Code pyta raz „Allow Automatic
   Tasks in Folder?".

2. Plugin superpowers 6.2.0 FAKTYCZNIE zainstalowany (scope `project`). Deklaracja
   `enabledPlugins` w `.claude/settings.json` była poprawna od początku — brakowało samej
   instalacji, `installed_plugins.json` był pusty `{}`, więc żaden z 14 skilli (m.in.
   `brainstorming`) nigdy się nie ładował. Instalacja z oficjalnego marketplace'u Anthropic,
   który przypina SHA `44c9b2d` — sprawdzone u źródła: to ten sam commit co ówczesny HEAD
   `obra/superpowers`, więc przypięcie nic nie kosztuje. Duplikat instalacji w scope `user`
   usunięty (decyzja Henricha: ma działać w tym repo, nie we wszystkich projektach).
   Przy okazji instalator znormalizował końcówki linii w tym pliku CRLF→LF.
   Pułapka na przyszłość, na którą sam się nabrałem: superpowers NIE jest podkatalogiem w cache
   marketplace'u (jego wpis ma źródło typu `url`, klonowane dopiero przy instalacji), więc `ls`
   po `plugins/` i `external_plugins/` fałszywie sugeruje, że pluginu tam nie ma.
   Szczegóły w CLAUDE.md, sekcja „Claude Code — plugins / skills".
   [narzedzia, git, vscode, claude-code, pluginy, skille]

[ZROBIONE 2026-08-06] (Opus 5 Medium) Paczka czterech punktów doprecyzowanych z Sonnetem 2026-08-06
(pliki issues/dark-mode-widzety-kolory.md i issues/zadania-otwarte-redesign.md — oba usunięte):

1. Widżety spójne z motywem. `--canvas-bg` przestało być na sztywno białe (`#fff` → `#1c1c1c` w ciemnym),
   doszedł blok tokenów `--wg-*` (osie, siatka, tekst, trzy klasy linii pomocniczych, punkt, żółty, słupek,
   etykieta info, półprzezroczyste wypełnienia obszarów) w :root i w OBU blokach ciemnych base.css.
   Z plików `widgets/*.js` zniknęły WSZYSTKIE literały kolorów — paleta `WG_KOLORY` jest teraz czytana
   ze zmiennych CSS przez `wgOdswiezKolory()` (mapa nazwa→zmienna: `WG_ZMIENNE`; `rgb()` konwertowane
   na hex, bo KaTeXowy `\textcolor` w zad. 18 przyjmuje tylko hex). Przemalowanie BEZ reloadu: każdy
   widżet rejestruje swoją funkcję rysującą przez `wgZarejestrujRysowanie(canvas, draw)`, a `wgPrzemaluj()`
   odświeża paletę i przerysowuje wszystkie canvasy nadal obecne w DOM — wołane z `applyTheme()`
   (app/theme.js) oraz z nasłuchu `matchMedia("(prefers-color-scheme: dark)")` dla trybu „auto".
   (Obrazki CKE i wideo z Manima to osobna, nadal otwarta sprawa — issues/dark-mode-obrazki-wideo.md.)
   [widzety, dark-mode, canvas, tokeny]

2. „Pokaż potrzebne wzory" → „Pokaż wzory" (template.html + komentarze w exam.css/ARCHITECTURE*).  [ui, teksty]

3. „zgłoś błąd" przeniesiony do wiersza light-buttonów: kolejność Podpowiedź / Rozwiązanie / Zgłoś błąd /
   Pokaż wzory, wygląd dokładnie taki jak sąsiadów (klasa `.light-button`; `.report-error-link` została
   już tylko uchwytem dla `body.bez-zglaszania`). `.light-button-container` jest flexem, a przyciski mają
   `flex: 1 1 0` zamiast sztywnych 30% — wiersz sam rozkłada szerokości, gdy zniknie „Pokaż wzory"
   (formulasPage: null), podpowiedź albo gdy zgłaszanie jest wyłączone w panelu. Poniżej 720px łamie się
   po dwa przyciski w rzędzie (przy okazji domyka punkt „przyciski łamią się na telefonie" z sekcji
   spójności UI). Formularz zgłoszenia działa bez zmian (nadal wsuwa się nad ten wiersz).  [ui, zglaszanie, responsywnosc]

4. Zadania otwarte — redesign. Usunięte cztery rozwlekłe etykiety; textarea ma placeholder „miejsce na
   notatki", a `finalAnswer.label` jest przez renderer IGNOROWANE (pole zostaje w danych wszystkich
   arkuszy, żeby nie przepisywać ich bez potrzeby). Checklista kryteriów przeniesiona do zwijanego
   `<details class="ocena-box">` z tytułem „Sprawdź obliczenia", domyślnie ZWINIĘTEGO (to samo załatwia
   stary zarzut, że checklista spojlerowała rozwiązanie), stylizowanego jak mały panel boczny.
   Najważniejsze: checklista PRZYZNAJE PUNKTY — `gradingCriteria` to teraz obiekty `{ tekst, punkty }`,
   wynik zadania = suma zaznaczonych przycięta do `maxScore` (suma kryteriów NIE musi równać się
   maxScore — zad. 9 ma 0+1+1 przy maxScore 2). Przyciski „0 pkt / 1 pkt / 2 pkt" zniknęły; zostały
   wyłącznie jako awaryjna ścieżka dla zadań bez kryteriów w danych (dziś takich nie ma). Każde kryterium
   ma po prawej mały licznik punktów wzorowany na `.exercise-score` (kryterium warte 0 pkt zostaje szare
   także po zaznaczeniu). Punkty NIE są zapisywane — po reloadzie przeliczają się z `stan.kryteria`, więc
   ścieżka oceniania pozostaje jedna. Dla wskaźników „oceń się" „ocenione" znaczy teraz „otwarty boks"
   (`stan.ocenaOtwarta`), bo uczeń, który przejrzał listę i nic nie zaznaczył, też się ocenił — na 0 pkt.
   Kryteria dopisane do WSZYSTKICH 15 zadań otwartych obu arkuszy (2024-grudzień: 3, 8, 9, 19, 26, 28, 30;
   2026-maj: 7, 10, 11, 14, 15, 21, 27, 30) — treść to kolejne PROGI punktowe z zasad oceniania CKE,
   alternatywy („ALBO" z klucza) sklejone w jedno zdanie słowem „lub", każdy próg po 1 pkt. Wariant progów
   1:1 z kluczem wybrał Henrich (2026-08-06), po tym jak okazało się, że klucz CKE nie jest listą
   niezależnych kroków, tylko kaskadą („2 pkt — to co na 1 pkt oraz…").  [zadania-otwarte, punktacja, schemat-danych, cke]

Przy okazji domknięte i usunięte: issues/formularz-oceniania-otwarte.md (punkt 1 „ostateczna odpowiedź"
i punkt 2 „checklista" zrobione/zastąpione redesignem, punkt 3 „zastrzeżenie prawne raz w stopce" jest
w template.html jako `.samoocena-disclaimer` — przeredagowany, bo checklista przyznaje teraz punkty)
oraz punkty 4 i 5 z issues/ui-spojnosc-etap2.md (sztywne 30% szerokości light-buttonów i krzywy układ
przycisków samooceny na telefonie — oba zniknęły razem z tą paczką).

Weryfikacja: brak przeglądarki w kontenerze (CDN Playwrighta odcięty przez firewall), więc do testów
na żywo posłużył headless Chromium z npmowej paczki `@sparticuz/chromium` + biblioteki z jej `al2023.tar.br`
(LD_LIBRARY_PATH). Przeklikane oba arkusze × oba motywy × 1400px i 390px: renderowanie wszystkich zadań,
brak poziomego scrolla, boksy zwinięte, brak starych etykiet i przycisków punktowych, przycisk zgłoszenia
w wierszu, KaTeX w kryteriach, naliczanie i przycinanie punktów, przetrwanie reloadu, ukrycie boksu
w trybie egzaminu, gaszenie kropek „oceń się", przemalowanie widżetów po przełączeniu motywu bez reloadu.

[ZROBIONE 2026-08-06] (Sonnet 5) Porządki w repo: usunięte `.idea/` (stary, niespójny konfig JetBrains —
`.name` wskazywał na `matematykazen11.html`, `.iml` na `matematykazen10`, ślad skopiowania folderu
z innego projektu) oraz pusty `package-lock.json` bez towarzyszącego `package.json` (projekt nie ma
build systemu ani package managera). Do tego wcześniej ręcznie usunięte przez Henricha: testowy agent
`.claude/agents/testowy agent claude w zakladce Chat.agent.md` i log `remoteContainers-*.log`. Zmiany
tylko wystagowane, niezacommitowane na życzenie Henricha.

[ZROBIONE 2026-08-04] Projekt udało się uruchomić w Dockerze na komputerze w domu — strona była dostępna lokalnie w przeglądarce i działała zgodnie z oczekiwaniami.

[ZROBIONE 2026-08-02] (Opus 5 Medium) Licencja i zasady kontrybucji. `LICENSE.md` (wklejony ręcznie przez
Henricha) zweryfikowany sekcja po sekcji z oficjalnym PolyForm Noncommercial 1.0.0 — tekst kompletny i wierny,
poprawki tylko kosmetyczne: usunięte trailing spaces w polskiej części po `---` i dopisana sekcja „Wkład
społeczności" z linkiem do CONTRIBUTING.md. Nowe pliki: `CONTRIBUTING.md` (jak pomagać + CLA — otwarcie PR-a
= udzielenie właścicielowi szerokiej, nieodwołalnej, także komercyjnej licencji na wkład, przy zachowaniu praw
kontrybutora; sens: nie zablokować przyszłej zmiany licencji z Fazy 3), `README.md` (repo go nie miało w ogóle)
i `.github/PULL_REQUEST_TEMPLATE.md` (checklista + pogrubione odesłanie do CLA).
Dwie decyzje świadome, obie z przypomnieniem w TODO.md pod `OPUS DOPISAŁ`: (1) właściciel występuje jako
pseudonim `Henrich2137`, nie imię i nazwisko — CLA na pseudonim jest słabsze dowodowo, a podmiana wymaga
DWÓCH miejsc (LICENSE.md linie 1–2 i punkt 2 w CONTRIBUTING.md); (2) URL w linii `Required Notice:` zmieniony
z `https://matematykazen.pl` (domena jeszcze nie działa) na GitHub Pages — ta linia jest z definicji kopiowana
przez każdego redystrybutora, więc martwy link by się propagował.
Przy okazji odkłamana OVERVIEW.md: pisała, że strona jest wystawiona „pod docelową ładną domeną" i że celem
obecnej fazy jest zdobywanie zainteresowania — a to cel Fazy 2, podczas gdy Faza 1 jest jawnie bez marketingu
i bez domeny; dopisana też sekcja „Licencja" i zaktualizowana notatka o kanałach kontaktu (są już issues/PR-y)
[licencja, cla, dokumentacja, github]

[ZROBIONE 2026-08-01] Ikona strzałki #sidebar-toggle (template.html) zamieniona kierunkiem — SVG path
z lewoskrętnego `M15 5l-7 7 7 7` na prawoskrętny `M9 5l7 7-7 7`. Rotacja o 180° przy otwarciu panelu
(`body.sidebar-otwarty #sidebar-toggle` w style/sheet.css) zostaje bez zmian [ui, sidebar, css]

[ZROBIONE 2026-08-01] Ujednolicenie nazw plików-przewodników po katalogach: `tablica-wzorow-transkrypt/INDEX.md`
→ `README.md` (`git mv`), referencje zaktualizowane w CLAUDE.md (3 miejsca), done/README.md i w tym pliku.
Powód (pytanie Henricha): trzy katalogi — `done/`, `issues/`, `tablica-wzorow-transkrypt/` — miały plik o tej
samej funkcji (zasady katalogu + indeks jego zawartości), ale dwie różne nazwy. `README.md` wygrywa, bo w
podkatalogu ma ustaloną konwencję „wyjaśnij ten folder" (wizytówką projektu jest tylko README w roocie, a tego
repo nie ma), jest auto-renderowane przez GitHub/VS Code i to pierwsza nazwa, której szuka człowiek i model.
Świadomie NIE użyto `CLAUDE.md` w podkatalogach, mimo że te pliki są pisane dla modeli: nested CLAUDE.md
doczytuje się automatycznie, co kłóci się z zasadą „NIE wczytuj done/ domyślnie". Audytorium sygnalizuje
pierwsza linijka treści, nie nazwa pliku.
Drugi krok tego samego porządkowania: katalog `DONE/` → `done/` (19 odwołań przepisanych w 10 plikach .md).
`DONE` był jedynym katalogiem WIELKIMI w repo — konwencja „krzyczącej nazwy" dotyczy plików meta w roocie
(`TODO.md`, `README`, `LICENSE` — sortują się w ASCII przed małymi, więc wypływają nad kod), a nie katalogów,
które wszędzie są małymi. UWAGA przy podobnych zmianach na Windowsie: NTFS jest case-insensitive, więc
`git mv DONE done` nie zadziała wprost — trzeba przez nazwę pośrednią (`DONE` → `_tmp_done` → `done`),
inaczej git nie zapisze zmiany wielkości liter i na Linuksie/CI zostanie stara nazwa. Z tego samego powodu
stare referencje `DONE/...` działałyby dalej lokalnie, ale pękłyby na GitHubie/Linuksie — dlatego przepisane
wszystkie, mimo że lokalnie „i tak działały"  [dokumentacja, konwencje]

[ZROBIONE 2026-08-01] Martwe referencje w ARCHITECTURE.md po lipcowych podziałach plików — wszystkie
wskazują teraz na FAKTYCZNY plik, ustalony przez grep definicji, nie zgadywany:
- `script.js` (nie istnieje od 2026-07-23) → konkretny moduł przy każdej wzmiance: `SHEET_ID`,
  `renderMath()`, `mediaPath()`, `TABLICE_PDF` → app/state.js; `startSheet()` → app/bootstrap.js;
  `loadExercises()` → app/render.js; ogólne „rendering logic" → app/.
- `style.css` (podzielony na style/*.css) → `.katex 1.08em` → style/base.css; reguła stylowania zadań
  → style/ z podpowiedzią „karty zadań w sheet.css, kolory/tokeny w base.css"; nagłówek sekcji CSS → style/.
- `[exercises.json](exercises.json)` → `matura/2024-grudzien/exercises.json` (sekcja provenance dotyczy
  konkretnie tego arkusza).
- Przy okazji WYKRYTY BŁĄD LICZBOWY: ARCHITECTURE.md i CLAUDE.md mówiły o „nine `app/*.js` files",
  a plików jest DZIESIĘĆ (state, theme, exam, indicators, panels, answers, steps, report, render,
  bootstrap). Poprawione w obu; kolejność ładowania dopisana wprost do ARCHITECTURE.md, bo wcześniej
  była tylko w CLAUDE.md. Widżetów faktycznie jest dziewięć — ta liczba była dobra.
- `issues/dwie-karty-tryb-egzaminu.md` wskazywał `finishExam()` „w script.js" → app/exam.js (3 miejsca).
  Zostawione: `issues/wskazniki-reload-faza-oceniania.md`, gdzie „podział script.js → app/*.js" to opis
  historycznego zdarzenia, a nie wskaźnik na plik.
Weryfikacja: skrypt sprawdzający KAŻDY link markdown w repo względem katalogu jego pliku — zero wiszących
(wcześniej 3). Zgłoszone przeze mnie do TODO.md kilka minut wcześniej, usunięte stamtąd po zrobieniu
[dokumentacja, refaktor]

[ZROBIONE 2026-08-01] Porządki nazewnicze, część druga — cztery zmiany z listy „co jeszcze uspójnić"
(Henrich wybrał 1–4, punkt 5 o osieroconych notatkach w roocie zostaje na później):

1. PLIKI ŹRÓDŁOWE ARKUSZY mają teraz CZTERY STAŁE NAZWY w każdym `matura/<id>/`: `arkusz.pdf`,
   `arkusz.txt`, `odpowiedzi.pdf`, `odpowiedzi.txt` (12 plików przez `git mv`, we wszystkich trzech
   arkuszach). Dawniej `matematyka-2024-grudzien-probna-podstawowa-odpowiedzi.pdf` itp. — nazwa
   powtarzała id katalogu i miała zmienny człon (`probna` vs `matura`), więc model NIE MÓGŁ złożyć
   ścieżki z głowy i musiał najpierw listować katalog. Teraz ścieżka wynika z samego `<id>`.
   `meta.zasadyPdf` w obu `exercises.json` → `"odpowiedzi.pdf"` (oba pliki przeparsowane po zmianie).
2. NOWY `matura/README.md` — ŹRÓDŁO PRAWDY o tym, czym są te arkusze (poziom podstawowy, Formuła 2023,
   CKE, 180 min, 50 pkt — liczba potwierdzona w nagłówkach obu arkuszy, nie z pamięci) i co jest w
   katalogu arkusza. Tabela arkuszy: 2024-grudzień (próbna/test diagnostyczny, MMAP-P0-100-2412, wpięty),
   2025-maj (właściwa, same PDF-y, NIEwpięty), 2026-maj (właściwa, 5 maja 2026, MMAP-P0-100-2605, wpięty).
   ARCHITECTURE.md i CLAUDE.md linkują tu zamiast powtarzać listę.
3. TABLICA WZORÓW: plik `wybrane_wzory_matematyczne.pdf` → `tablica-wzorow.pdf`, katalog transkryptu
   `wybrane_wzory_matematyczne/` → `tablica-wzorow-transkrypt/`. Powód: plik i katalog miały IDENTYCZNĄ
   nazwę przy zupełnie różnej roli (PDF serwowany userom vs transkrypt tylko dla modeli) — glob łapał oba
   i przy każdej wzmiance trzeba było rozstrzygać, o który chodzi. Zmienione też `TABLICE_PDF` w
   app/state.js i `data=` w template.html. Uwaga: ID elementów `#tablica-wzorow` / `#tablica-wzorow-panel`
   w HTML/CSS to CO INNEGO niż nazwa pliku — nie ruszane.
4. `done/STARY_PRZENIESIONY_DONE.md` → `done/00-stary-done.md` (wpasowane w sekwencję 00→04).
5. USUNIĘTE MARTWE OPISY: `inne arkusze PDF/` był opisany w ARCHITECTURE.md i CLAUDE.md, a tego katalogu
   NIE MA już w repo. Przyczyna była strukturalna — układ katalogów żył zduplikowany w dwóch plikach
   naraz i się rozjeżdżał. Teraz: struktura katalogu arkusza opisana raz, w `matura/README.md`, a oba
   pliki dokumentacji tylko do niej linkują. Przy okazji przycięty przerośnięty akapit o transkrypcie
   w CLAUDE.md (miał doklejony ogon o PDF-ach arkuszy, niezwiązany z tablicą wzorów).

Weryfikacja: `grep` po całym repo nie znajduje ani jednej wiszącej starej ścieżki; oba `exercises.json`
parsują się poprawnie; `TABLICE_PDF`/`data=` wskazują na istniejący plik. Jedyne pozostawione świadomie
wystąpienia starych nazw to proza historyczna w `done/00-stary-done.md` i `done/03-2026-07-27.md`
opisująca nieistniejący już katalog „inne arkusze PDF/" — tego nie da się „naprawić" na aktualną ścieżkę,
bo opisuje stan sprzed usunięcia  [dokumentacja, konwencje, arkusze, tablica-wzorow]

[ZROBIONE 2026-07-28] Transkrypt tablicy wzorów dla modeli — `tablica-wzorow-transkrypt/`
(README.md + 16 plików sekcji, ~780 wzorów ze stron 4–33 PDF-a CKE). Cel: model ładuje jedną
sekcję (300–800 tokenów) zamiast całego PDF-a; „Skorowidz" w README.md mapuje słownictwo zadania
na ID wzoru i stronę, co ma przyspieszyć uzupełnianie `formulasPage`. Ustalenia z Henrichem:
KaTeX w konwencji `\( … \)` / `\[ … \]` identycznej jak w exercises.json (kopiowanie bez konwersji;
`$…$` NIE zadziałałoby — `renderMath` w app/state.js rejestruje tylko te dwa delimitery), pełne
zdania opisowe CKE, pozycja wzoru słownie (góra/środek/dół), sekcja 17 (tablica wartości
trygonometrycznych, s. 34) pominięta, rysunki jako legendy oznaczeń zamiast opisów figur, bez PNG,
bez znaczników podstawa/rozszerzenie. Wyciąg z PDF-a: `pdftohtml -xml` + normalizacja Unicode
Mathematical Italic (U+1D400+) na ASCII — `pdftotext` gubi zmienne i strukturę ułamków.
Weryfikacja: (1) wszystkie 782 wzory renderują się w vendorowanym KaTeX-ie, (2) 26 352 losowych
sprawdzeń numerycznych tożsamości (skrócone mnożenie, potęgi, logarytmy, Newton, Viète, ciągi,
cała trygonometria, tw. sinusów/cosinusów, Heron, pola, wariancja, pochodne) — bez błędu.
Do sprawdzenia wyrywkowego przez Henricha zostają rzeczy nieweryfikowalne liczbowo: definicje
słowne, cechy przystawania/podobieństwa, legendy oznaczeń.

[UZUPEŁNIONE 2026-07-28] Kontrola kompletności transkryptu + sekcja „Czego tu NIE MA" w README.md.
Powód: transkrypt nigdzie nie mówił, że czegoś w nim brakuje, więc model widzący wyłącznie
transkrypt nie miałby powodu otworzyć PDF-a (zgłosił Henrich). Przy okazji wyszła luka —
[8.10] procent składany ze s. 10 był pominięty (dopisany wcześniej przez Sonneta). Przyczyna
techniczna warta zapamiętania: odczyty PDF-a robiłem przez `python czytaj.py X Y | head -N`
i dla stron 9–10 limit `head` **uciął dolną część s. 10** — wzór wypadł poza widziany fragment.
Wniosek na przyszłość: przy przepisywaniu PDF-a nie ucinać outputu odczytu, albo weryfikować
kompletność osobnym przebiegiem. Zrobiona kontrola: skrypt wypisał wszystkie punkty „•"
i nagłówki sekcji ze stron 4–34, porównane jeden-do-jednego z ID w transkrypcie — po dopisaniu
[8.10] pokrycie jest pełne, dodatkowo pełne odczyty s. 10 i 17 potwierdziły brak dalszych luk.
Dopisane: tabela „Czego tu NIE MA" w README.md (rysunki → strony PDF-a, sekcja 17, strony
redakcyjne) oraz notki o rysunkach w nagłówkach sekcji 7, 9, 10, 11, 12 ze wskazaniem strony
PDF-a; przy [9.3] (wykresy sin/cos/tg) zaznaczone, że tam **rysunek jest jedyną treścią** —
w tablicy nie ma przy nim żadnego wzoru.

[ODRZUCONE 2026-07-28] Celowanie w konkretny wzór na stronie PDF-a (`#page=N&view=FitH,<top>`
zamiast samego `#page=N`). Zbudowane i przetestowane (współrzędne wzorów z `pdftohtml -xml`,
centrowanie liczone z rozmiaru panelu), po czym wycofane: Firefox i Brave przewijają poprawnie,
ale Chrome i Edge lądują zdecydowanie za nisko — wzoru nie widać. Dodatkowo przy domyślnym
kształcie panelu (28% × 80vh) cała strona i tak mieści się w kadrze przy FitH, więc kotwica
nic by nie dawała bez zmiany proporcji panelu. Ostrzeżenie zostawione w app/panels.js i
ARCHITECTURE.md, żeby nikt nie próbował drugi raz. Pole `formulasY` w exercises.json usunięte.

[ZROBIONE 2026-07-28] Skok formularza „zgłoś błąd" (link na dole karty, formularz otwiera się wyżej,
nad Podpowiedź/Rozwiązanie) — sprawdzone, zachowanie takie samo na desktop i mobile (DOM insertBefore
bez media query), Henrich zaakceptował, bez zmian. [formularz, ui]

[ZROBIONE 2026-07-28] Analityka: GoatCounter wpięty w template.html i index.html
(`data-goatcounter="https://henrich.goatcounter.com/count"`), błąd ładowania skryptu wyciszony
w belce diagnostycznej (adblock/Privacy Badger często go blokują — to nieszkodliwe, nie powinno
straszyć banerem błędu). Potwierdzone przez Henricha na żywo w panelu goatcounter.com — dzisiejsze
odwiedziny się liczą. Do pamiętania przy czytaniu statystyk: część ruchu z adblockami nie zostanie
zliczona, więc realne liczby są wyższe niż panel pokazuje. [analityka, goatcounter]

[ZROBIONE 2026-07-28] Zadania nie renderowały się na telefonie (arkusz 2024-grudzień) — potwierdzone
przez Henricha na żywo, że fix z 2026-07-24 (`.nojekyll` w rootcie, patrz issues/zadania-nie-renderuja-sie-mobile.md)
faktycznie działa na urządzeniu. [mobile, bugfix, github-pages]

[ZROBIONE 2026-07-27] (Sonnet High) „Sprawdź wszystkie odpowiedzi" pomijało zadania z polem tekstowym
+ brak potwierdzenia kliknięcia — pełny spec z (usuniętego) issues/sprawdz-wszystkie-pola-i-komunikat.md,
v0.08. Weryfikacja: Playwright headless, oba motywy, tryb „sprawdź później", brak scrolla 360px.

- REJESTR: `fillIn` i `finalAnswer` dopisane do `oczekujaceSprawdzenia` (app/render.js) obok
  ABCD/PF/multiSelect. `fillIn` — ocena wydzielona do nazwanej `ocenFillIn()` (przycisk „Sprawdź" i
  rejestr wołają tę samą funkcję, zero duplikacji normalizacji/punktacji); `czySprawdzone` czyta klasę
  `correct`/`incorrect` z DOM pierwszego pola (nie flagę) — edycja pola kasuje tę klasę, więc zadanie
  wraca do „niesprawdzone" automatycznie. `finalAnswer` — istniejąca `ocenKoncowaOdpowiedz()` wpisana do
  rejestru z `typ: "finalAnswer"` (znacznik pod bonus niżej). Skutek uboczny świadomie zaakceptowany:
  „sprawdź wszystkie" teraz też PRZYZNAJE PUNKTY za fillIn (dawniej trzeba było kliknąć każdy „Sprawdź").
- BONUS (domyka wpis z TODO.md „ostateczna odpowiedź sprawdza się sama po egzaminie"): `finishExam()`
  (app/exam.js) po zakończeniu egzaminu przelatuje rejestr i woła `ocen()` tylko dla wpisów
  `typ: "finalAnswer"` z niepustą, jeszcze nieodsłoniętą wartością — nie odsłania przy okazji zadań
  zamkniętych, których uczeń nie zdążył sprawdzić.
- KOMUNIKAT „sprawdzono ✓": nowy `<span role="status" aria-live="polite">` przy obu kopiach przycisku.
  Stopka — komunikat `position: absolute` względem nowego `#sprawdz-wszystkie-stopka-wrap` (jak
  `.answer-check-floating`), więc nigdy nie przesuwa przycisku; pod 720px przesuwa się pod przycisk
  (wycentrowany), ale ZOSTAJE `position: absolute` — zmieniają się tylko `left`/`top`/`transform`.
  Panel boczny — tylko glif „✓" (`margin-left: auto` we flexowym `.sidebar-akcja`), bo 260px
  nie mieści zdania; prawdziwy tekst leci do `aria-label`, nie do widocznej treści. Zielony (`--correct`)
  gdy jest cokolwiek zaznaczone (czy to właśnie ocenione, czy już wcześniej sprawdzone), przygaszony
  (`--text-faint`) przy pustym arkuszu — inaczej „sprawdzono" kłamałoby. Znika po ~2,5s przez `opacity`;
  kolejny klik resetuje timer; `prefers-reduced-motion: reduce` bez animacji (dopisane do wspólnego
  bloku w sheet.css). Egzamin: bez zmian — przyciski zostają `disabled` jak dotychczas, więc handler
  (i komunikat) w ogóle się nie odpala.
- POPRAWKA tego samego dnia (zgłoszone przez Henricha na żywo): pierwsza wersja mobilnego fallbacku
  (pod 720px) przełączała komunikat z `position: absolute` na `position: static; display: block` —
  wciągnęło go to z powrotem do flow `#sprawdz-wszystkie-stopka-wrap`, więc nawet PUSTY/niewidoczny
  komunikat (opacity: 0, bez treści) dokładał ~6px wysokości pod przyciskiem przez `margin-top` +
  wysokość pustej linii („sprawdź wszystkie" wyglądało na stałe za grubo na telefonie, nie tylko po
  kliknięciu). Naprawione: mobilny fallback zostaje `position: absolute`, tylko przesunięty pod
  przycisk (`left: 50%; top: 100%; transform: translateX(-50%)`) — zero wysokości w layoucie, kiedy
  komunikat jest pusty. Zweryfikowane Playwright: `bottomDiff` wrappera i przycisku 0px (było 6px).

[ZROBIONE 2026-07-27] (wpis Henricha, przeniesiony z TODO.md 2026-07-27) W trybie ćwiczeń przycisk
„sprawdź wszystkie odpowiedzi" na dole arkusza obok „rozpocznij egzamin", zostaje też w panelu bocznym.
W trybie egzaminu ostatecznie NIE jest niewidoczny, a wyszarzony — zmiana decyzji z 2026-07-26
(znikający przycisk mylił, jakby zniknęła sama funkcja; patrz komentarz przy #sprawdz-wszystkie-stopka
w style/exam.css). Wygląd obu przycisków stopki ujednolicony w sesji „spójność UI" (wpis niżej).

[ZROBIONE 2026-07-27] (Opus High, lokalnie) Trzy drobnice po przeglądzie sesji 1 przez Henricha — v0.07.
Weryfikacja: Playwright, zrzuty light/dark × 1440/1280/390 + pomiary computed style.

- CIENIE: #sidebar traci box-shadow (Henrich: „nie współgrają z logiem ani z kreską"). Panel jest przypięty
  do krawędzi i ma własną kreskę #sidebar-linia, więc cień dublował tę granicę. Panele PDF i toast cień
  ZOSTAWIAJĄ — pływają nad treścią i nie mają żadnej kreski (decyzja Henricha: „tylko panel boczny").
  Token --shadow-panel zostaje w użyciu, tylko bez sidebara.
- STOPKA: #sprawdz-wszystkie-stopka z --text-muted na pełne --text — oba przyciski stopki są teraz
  identyczne, o kolejności czytania decyduje pozycja, nie kontrast (zmierzone: rgb(17,17,17) w light,
  rgb(230,230,230) w dark, oba przyciski).
- TYTUŁ ARKUSZA: .sheet-title-heading dostał max-width: 32% (456px przy 1440px) + margin: 0 auto —
  typowy tytuł CKE zawija się na dwie wyśrodkowane linie zamiast ciągnąć się przez cały ekran.
  Pod 720px ograniczenie zdjęte (max-width: none), bo 32% z 390px zostawiłoby po dwa słowa w linii.
