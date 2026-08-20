#!/usr/bin/env python3
"""Statystyki wypełnienia arkuszy - liczy to, co OVERVIEW.md podaje w sekcji "Arkusze maturalne".

    python3 tools/statystyki.py            # wszystkie arkusze
    python3 tools/statystyki.py 2026-maj   # jeden arkusz

Definicje (tu jest zrodlo prawdy, OVERVIEW.md tylko przepisuje wynik):
  * "zadanie" = jeden punktowany wpis w exercises.json, czyli osobna karta z odpowiedzia.
    Wpisy o maxScore 0 to naglowki wiazek ("Zadanie 12." nad 12.1 i 12.2) - nie licza sie.
  * podpowiedz  = niepuste "hint"
  * rozwiazanie opisowe = niepuste "solutionText"
  * rozwiazanie wideo = niepuste "solutionStepByStep"
  * widzet = niepuste "solutionWidget"
  * zadanie otwarte = "selfScore": true; z kryteriami = ma tez "gradingCriteria"
"""
import json, os, re, sys

KORZEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def numer(e):
    m = re.search(r'Zadanie\s+([\d.]+)', e.get('question', ''))
    return m.group(1).rstrip('.') if m else '?'


def statystyki(sid):
    plik = os.path.join(KORZEN, 'matura', sid, 'exercises.json')
    if not os.path.exists(plik):
        return None
    ex = json.load(open(plik, encoding='utf-8'))['exercises']
    zad = [e for e in ex if e.get('maxScore')]
    n = len(zad)
    licz = lambda k: sum(1 for e in zad if e.get(k))
    otwarte = [e for e in zad if e.get('selfScore')]
    widzety = {e['solutionWidget'] for e in zad if e.get('solutionWidget')}
    return {
        'polecenia': len({numer(e).split('.')[0] for e in zad}),
        'zadania': n,
        'podpowiedzi': licz('hint'),
        'opisowe': licz('solutionText'),
        'wideo': licz('solutionStepByStep'),
        'widzety': len(widzety),
        'otwarte': len(otwarte),
        'kryteria': sum(1 for e in otwarte if e.get('gradingCriteria')),
        'punkty': sum(e.get('maxScore', 0) for e in zad),
        'braki': {
            'podpowiedzi': [numer(e) for e in zad if not e.get('hint')],
            'opisowe': [numer(e) for e in zad if not e.get('solutionText')],
            'wideo': [numer(e) for e in zad if not e.get('solutionStepByStep')],
        },
    }


def wypisz(sid, s, braki=False):
    n = s['zadania']
    print(f"{sid} ({s['polecenia']} polecen CKE, {s['punkty']} pkt)")
    print(f"  Zadania (osobne karty): {n}")
    print(f"  Podpowiedzi: {s['podpowiedzi']}/{n}")
    print(f"  Rozwiazania opisowe: {s['opisowe']}/{n}")
    print(f"  Rozwiazania wideo: {s['wideo']}/{n}")
    print(f"  Widzety interaktywne: {s['widzety']}")
    print(f"  Zadania otwarte z kryteriami CKE: {s['kryteria']}/{s['otwarte']}")
    if braki:
        for k, v in s['braki'].items():
            print(f"  brak {k}: {', '.join(v) or '-'}")


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    braki = '--braki' in sys.argv
    ids = args or sorted(os.listdir(os.path.join(KORZEN, 'matura')))
    for sid in ids:
        s = statystyki(sid)
        if s:
            wypisz(sid, s, braki)
            print()
