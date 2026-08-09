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

## Czego tu NIE ma

Tylko Chromium. Firefox i WebKit potrzebowałyby własnych zestawów bibliotek systemowych i kolejnych setek MB — jeśli kiedyś będą potrzebne, dochodzą do komendy `install` i do listy pakietów w Dockerfile.
