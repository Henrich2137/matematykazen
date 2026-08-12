/* Lokalny serwer plików do pracy nad stroną — z obsługą ŻĄDAŃ ZAKRESOWYCH
 * i z opcjonalnym dławieniem łącza.
 *
 * PO CO TO JEST. Dwa powody, oba wynikają z filmów w rozwiązaniach krok po kroku:
 *
 * 1. `python3 -m http.server` NIE obsługuje nagłówka `Range`, a bez niego
 *    przeglądarka nie potrafi przewinąć filmu: `video.seekable` zostaje puste,
 *    a każde ustawienie `currentTime` cicho wraca do zera. Wygląda to jak błąd
 *    w kodzie odtwarzacza i raz już nim nie było (2026-08-11, sporo straconego
 *    czasu). `npx http-server` to potrafi, ale wymaga sieci — ten plik nie.
 *
 * 2. Odtwarzacz kroków ma stan, który ujawnia się DOPIERO przy wolnym łączu:
 *    między kliknięciem a pojawieniem się filmu w kadrze siedzi jeszcze
 *    poprzedni krok. Na localhoście to okno trwa milisekundy i wszystko wygląda
 *    dobrze; przy 60 kB/s trwa dwie sekundy i wychodzą błędy, których inaczej
 *    nie widać (patrz done/04-biezace.md, wpis z 2026-08-12). Dlatego dławienie
 *    jest tutaj, a nie w skrypcie testowym.
 *
 * UŻYCIE:
 *
 *   node tools/serwer.js                      # cały katalog repo na :8000
 *   node tools/serwer.js 8001 --wolno=1200 --bps=60000
 *
 * PRZEŁĄCZNIKI:
 *   <port>          domyślnie 8000
 *   --wolno=<ms>    opóźnienie przed pierwszym bajtem (tylko pliki wideo)
 *   --bps=<bajty/s> przepustowość (tylko pliki wideo)
 *   --katalog=<p>   co serwować (domyślnie katalog repo)
 *
 * Dławimy TYLKO wideo. Dławienie wszystkiego (razem z vendor/katex) sprawia,
 * że sama strona ładuje się dłużej niż limit Playwrighta i test pada na starcie
 * zamiast sprawdzić cokolwiek.
 *
 * Nasłuch na 127.0.0.1, nie 0.0.0.0 — brama hosta jest w firewallu kontenera
 * przepuszczona, więc serwer na 0.0.0.0 byłby widoczny poza kontenerem.
 *
 * Szybki sprawdzian, czy zakresy działają (ma zwrócić 206, nie 200):
 *   curl -s -o /dev/null -w "%{http_code}\n" -r 0-100 \
 *     http://127.0.0.1:8000/matura/2024-grudzien/media/zad1/solution-step-by-step/step1.mp4
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const flaga = (nazwa, dom) => {
    const t = args.find(a => a.startsWith(`--${nazwa}=`));
    return t ? t.slice(nazwa.length + 3) : dom;
};

const PORT = Number(args.find(a => /^\d+$/.test(a)) || 8000);
const ROOT = path.resolve(flaga('katalog', path.join(__dirname, '..')));
const WOLNO = Number(flaga('wolno', 0));
const BPS = Number(flaga('bps', 0));

const TYPY = {
    '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8',
    '.mp4': 'video/mp4', '.webm': 'video/webm', '.png': 'image/png',
    '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml',
    '.pdf': 'application/pdf', '.woff2': 'font/woff2', '.woff': 'font/woff',
    '.ttf': 'font/ttf', '.txt': 'text/plain; charset=utf-8',
};

// Wysyłka kawałkami co 100 ms, gdy dławimy — inaczej zwykły strumień.
function wyslij(res, plik, start, koniec, dlaw) {
    if (!BPS || !dlaw) {
        fs.createReadStream(plik, { start, end: koniec }).pipe(res);
        return;
    }
    const kawalek = Math.max(1024, Math.floor(BPS / 10));
    const fd = fs.openSync(plik, 'r');
    let poz = start;
    const tick = () => {
        if (poz > koniec || res.writableEnded) { fs.closeSync(fd); res.end(); return; }
        const n = Math.min(kawalek, koniec - poz + 1);
        const buf = Buffer.alloc(n);
        fs.readSync(fd, buf, 0, n, poz);
        poz += n;
        res.write(buf);
        setTimeout(tick, 100);
    };
    tick();
}

http.createServer((req, res) => {
    let sciezka;
    try {
        sciezka = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    } catch { res.writeHead(400).end('zła ścieżka'); return; }

    const plik = path.join(ROOT, sciezka);
    // Nie wypuszczamy się poza katalog repo (../../etc/passwd).
    if (!plik.startsWith(ROOT + path.sep) && plik !== ROOT) { res.writeHead(403).end('403'); return; }

    fs.stat(plik, (err, st) => {
        if (err || !st.isFile()) { res.writeHead(404).end('404 ' + sciezka); return; }
        const wideo = /\.(mp4|webm)$/i.test(plik);
        const naglowki = {
            'Content-Type': TYPY[path.extname(plik).toLowerCase()] || 'application/octet-stream',
            'Accept-Ranges': 'bytes',
            'Cache-Control': 'no-store',
        };
        const wyslijOdpowiedz = () => {
            const zakres = req.headers.range && /bytes=(\d*)-(\d*)/.exec(req.headers.range);
            if (zakres) {
                const start = zakres[1] ? Number(zakres[1]) : 0;
                const koniec = zakres[2] ? Number(zakres[2]) : st.size - 1;
                if (start >= st.size || koniec < start) {
                    res.writeHead(416, { 'Content-Range': `bytes */${st.size}` }).end();
                    return;
                }
                res.writeHead(206, { ...naglowki, 'Content-Range': `bytes ${start}-${koniec}/${st.size}`, 'Content-Length': koniec - start + 1 });
                if (req.method === 'HEAD') { res.end(); return; }
                wyslij(res, plik, start, koniec, wideo);
            } else {
                res.writeHead(200, { ...naglowki, 'Content-Length': st.size });
                if (req.method === 'HEAD') { res.end(); return; }
                wyslij(res, plik, 0, st.size - 1, wideo);
            }
        };
        if (wideo && WOLNO) setTimeout(wyslijOdpowiedz, WOLNO); else wyslijOdpowiedz();
    });
}).listen(PORT, '127.0.0.1', () => {
    const dlawienie = (WOLNO || BPS) ? `  [dławienie wideo: ${WOLNO} ms + ${BPS || '∞'} B/s]` : '';
    console.log(`serwer: ${ROOT} → http://127.0.0.1:${PORT}${dlawienie}`);
});
