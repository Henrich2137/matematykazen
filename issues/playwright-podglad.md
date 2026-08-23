# Playwright + Chromium w kontenerze (podgląd zmian wizualnych)

**Status:** działa (od 2026-08-09). To nie jest problem do naprawienia — to opis konstrukcji.

## Po co

Kontener nie ma przeglądarki, więc model pracujący w środku nie widział efektu własnych zmian w CSS. Playwright + Chromium pozwalają zrobić zrzut strony arkusza i faktycznie ją obejrzeć.

## Jak to jest złożone

Trzy elementy:

1. **Chromium pobrany raz na hoście**, do `~/.cache/ms-playwright` (poza repo — ~650 MB binarek nie ma prawa trafić do gita).
2. **Bind tego katalogu do kontenera**, `readonly`, jako `/home/node/.cache/ms-playwright` (`.devcontainer/devcontainer.json`, `mounts` + `containerEnv.PLAYWRIGHT_BROWSERS_PATH`).
3. **Biblioteki systemowe, fonty i sama biblioteka `playwright`** doinstalowane w `.devcontainer/Dockerfile`.

## Dlaczego bind z hosta, a nie pobieranie w kontenerze

Firewall kontenera blokuje `cdn.playwright.dev`, `storage.googleapis.com` i `playwright.download.prss.microsoft.com` (sprawdzone: wszystkie zwracają 000). Dopisanie ich do allowlisty **zostało odrzucone** — to anycast Cloudflare/Azure, czyli dokładnie ten problem, dla którego wcześniej świadomie odrzucono `formspree.io` (patrz komentarz w `init-firewall.sh`, ~linia 102). Ta konstrukcja istnieje po to, żeby firewalla nie ruszać.

Wolumen zamiast bindu też odpada z tego samego powodu: wolumen trzeba by czymś wypełnić, a wypełnienie wymaga sieci.

`readonly`, bo Playwright w trakcie działania tylko czyta binarki — kontener nie ma po co móc podmienić pliku wykonywalnego, który sam uruchamia.

Edycja `.devcontainer/` jest możliwa **wyłącznie z hosta** (katalog jest podmontowany read-only), a w kontenerze nie działa `sudo` (`--cap-drop=ALL`) — dlatego pakiety systemowe idą przez Dockerfile i przebudowę obrazu.

## Przypięta wersja

**`playwright@1.62.1`** — Chrome for Testing 151.0.7922.34, katalogi `chromium-1234`, `chromium_headless_shell-1234`, `ffmpeg-1011`.

Wersja jest w dwóch miejscach i **muszą się zgadzać**: `ARG PLAYWRIGHT_VERSION` w Dockerfile oraz build faktycznie leżący w `~/.cache/ms-playwright` na hoście. Playwright żąda konkretnego builda przeglądarki — przy rozjeździe odmawia startu. To najbardziej prawdopodobny sposób, w jaki ta konstrukcja się zepsuje.

## Jak podbić wersję

Oba kroki naraz, na hoście:

```bash
podman run --rm \
  -v ~/.cache/ms-playwright:/ms:Z \
  -e PLAYWRIGHT_BROWSERS_PATH=/ms \
  node:20 npx --yes playwright@<NOWA> install chromium
```

potem zmień `ARG PLAYWRIGHT_VERSION=<NOWA>` w `.devcontainer/Dockerfile` i zrób **Rebuild Container**. Stare katalogi `chromium-*` można wtedy usunąć ręcznie.

## Jak tego użyć w kontenerze

Loopback jest w firewallu przepuszczony, więc wystarczy serwować repo lokalnie i wejść tam Playwrightem:

```bash
python3 -m http.server 8000 &
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  await p.goto('http://127.0.0.1:8000/template.html?arkusz=2024-grudzien');
  await p.screenshot({ path: '/tmp/zrzut.png', fullPage: true });
  await b.close();
})();
"
```

`playwright` jest zainstalowany globalnie (`NPM_CONFIG_PREFIX=/usr/local/share/npm-global`), więc `require('playwright')` z katalogu repo może wymagać `NODE_PATH=/usr/local/share/npm-global/lib/node_modules`.

## Pułapki przy pisaniu skryptu pod TĘ stronę

Trzy rzeczy, na których traci czas każdy, kto pisze skrypt pierwszy raz:

- **Pierwszy `.exercise-container` w DOM to ukryty szablon.** Bierz
  `.exercise-container:not(#exercise-template)`, inaczej czekasz w nieskończoność na coś,
  co nigdy nie stanie się widoczne.
- **Przed kliknięciem w płótno widżetu albo w kropki kroków zrób `scrollIntoViewIfNeeded()`.**
  `page.mouse` klika we współrzędnych okna, więc kliknięcie w element poniżej zgięcia idzie
  w powietrze, a widżet wygląda na zepsuty, choć działa.
- **Błędy KaTeXa licz przez `page.locator('.katex-error').count()`**, ma wyjść 0. Sam brak
  wyjątku w konsoli niczego nie dowodzi, bo `renderMath` ma `throwOnError: false`.

Do zwykłych zrzutów całej strony jest gotowe `tools/zrzuty.js`, nie pisz własnego skryptu.

## Błąd w konsoli, który zawsze będzie i nic nie znaczy

Każde wejście na stronę z kontenera zostawia w konsoli:

```
Failed to load resource: net::ERR_ADDRESS_UNREACHABLE   (//gc.zgo.at/count.js)
```

To **GoatCounter** — analityka wpięta w `template.html` i `index.html`. Firewall kontenera nie
przepuszcza `gc.zgo.at`, więc skrypt nigdy się nie wczyta. Jest to nieszkodliwe i **nie wymaga
naprawy**:

- skrypt jest `async` i tylko zlicza odsłonę — strona nie czyta z niego niczego,
- ta sama sytuacja zdarza się u zwykłych użytkowników (adblock, Privacy Badger), więc kod od
  początku ją przewiduje: handler błędów w `template.html` **świadomie pomija** zasoby z
  `gc.zgo.at`, żeby nie straszyć czerwonym banerem („Nie wczytano skryptu…"),
- poza kontenerem, na GitHub Pages, żądanie przechodzi normalnie.

Pisząc własny test, który zbiera błędy konsoli, odfiltruj `zgo.at` — inaczej każdy przebieg
kończy się „błędem", który nie jest błędem. **Uwaga na pułapkę:** adresu NIE ma w treści
komunikatu (`msg.text()` to samo „Failed to load resource: net::ERR_ADDRESS_UNREACHABLE"),
tylko w `msg.location().url`. Filtr po `text()` przepuści go i test zgłosi fałszywy alarm:

```js
page.on('console', m => {
    const url = (m.location() && m.location().url) || '';
    if (m.type() === 'error' && url.indexOf('zgo.at') === -1) bledy.push(m.text());
});
```

## Wideo H.264 — działa lokalnie, nie działało w chmurze

Chromium Playwrighta **odtwarza w tym kontenerze filmy `.mp4` (H.264)** — sprawdzone
2026-08-12 wprost na plikach arkusza, więc kroki rozwiązania testuje się na oryginałach,
bez kombinowania z kopiami WebM. Ograniczenie z 2026-08-11 dotyczyło tylko **kontenera
chmurowego**: tam Chromium nie miało kodeka, a Chrome'a nie dało się doinstalować, bo
firewall blokuje `dl.google.com`. Jeśli kiedyś odezwie się to samo w chmurze — logikę
odtwarzacza da się sprawdzić na kopiach WebM, a same pliki mp4 osobno przez ffmpeg/SSIM.

## Czego tu NIE ma

Tylko Chromium. Firefox i WebKit potrzebowałyby własnych zestawów bibliotek systemowych i kolejnych setek MB — jeśli kiedyś będą potrzebne, dochodzą do komendy `install` i do listy pakietów w Dockerfile.
