"""Wspólne klocki scen krok po kroku.

Trzy zasady, których pilnują funkcje z tego pliku, opisuje README (sekcja
„Jak ma wyglądać animacja"):

1. Ostatnia klatka kroku N musi wyglądać jak pierwsza klatka kroku N+1 —
   stąd `zakoncz_krok`, które ZDEJMUJE podświetlenia przed przytrzymaniem.
   Sprawdza to potem `tools/styk-klatek.sh`.
2. Ruch ma odpowiadać rachunkowi — stąd rezygnacja z `TransformMatchingShapes`
   na rzecz jawnych par (kawałek źródła → kawałek celu). Automat parował kształty
   po podobieństwie i szóstka z `60\\,000` lądowała w liczniku ułamka zamiast
   w mianowniku (zgłoszenie Henricha, zad. 5).
3. Kolor tylko na to, na co uczeń ma spojrzeć.

Sceny leżą w tym samym katalogu, więc `from _wspolne import *` działa przy
`manim --save_sections solutionZadN.py ZadN` uruchamianym z manimations/.
"""

from manim import *

# Zieleń: „popatrz tutaj". Czerwień: znak, który się pojawia albo znika.
ZIELONY = "#0AB32F"
CZERWONY = "#C0271A"

# Ułamek długości kadru, w który mają się zmieścić najszersze kroki.
MARGINES = 0.85

# Ile trwa przytrzymanie ostatniej klatki kroku. Bez niego przeglądarka
# zatrzymuje obraz kilka klatek przed końcem pliku i ostatni element animacji
# nie zostaje na ekranie (README, punkt 0 workflow).
PRZYTRZYMANIE = 0.25


def ustaw_kroki(kroki, rozmiar=100):
    """Jednolity rozmiar, kolor i skala WSPÓLNA dla wszystkich kroków.

    Skala liczona z najszerszego kroku, a nie osobno dla każdego — inaczej
    litery zmieniają wielkość w trakcie przekształcenia i Transform robi z tego
    zoom.
    """
    for krok in kroki:
        krok.set_color(BLACK)
        # Krok bywa zwykłym MathTex albo VGroup-em złożonym z kilku (gdy trzeba
        # mieć osobne uchwyty do ułamków). VGroup nie ma font_size, więc tam
        # rozmiar ustawia się przy tworzeniu składników.
        if rozmiar is not None and hasattr(krok, "font_size"):
            krok.font_size = rozmiar
    najszerszy = max(krok.width for krok in kroki)
    if najszerszy > config.frame_width * MARGINES:
        wspolczynnik = config.frame_width * MARGINES / najszerszy
        for krok in kroki:
            krok.scale(wspolczynnik)
    for krok in kroki:
        krok.move_to(ORIGIN)


def rozbij_ulamek(ulamek):
    """(licznik, kreska, mianownik) z glifów wyrażenia `\\frac{...}{...}`.

    Manim nie obiecuje, w jakiej kolejności ustawi glify ułamka, więc zamiast
    zgadywać indeksy dzielimy je po wysokości: kreska jest jedynym glifem
    szerokim i płaskim, reszta idzie nad nią i pod nią. Dzięki temu da się
    przenieść dzielnik DOKŁADNIE pod kreskę, a nie „gdzieś w okolice ułamka".
    """
    glify = list(ulamek)
    kreska = max(glify, key=lambda g: g.width / max(g.height, 1e-6))
    poziom = kreska.get_center()[1]
    licznik = VGroup(*[g for g in glify if g.get_center()[1] > poziom])
    mianownik = VGroup(*[g for g in glify if g.get_center()[1] < poziom])
    return licznik, kreska, mianownik


def zapal(scena, na_ekranie=(), poza_ekranem=(), czas=0.4):
    """Zapala podświetlenie JAKO ANIMACJĘ, a nie z góry.

    Gdyby kolor był ustawiony przed pierwszym `play`, pierwsza klatka kroku
    byłaby już podświetlona, a ostatnia klatka kroku poprzedniego czysta — czyli
    dokładnie ten przeskok, którego nie chcemy. Elementy `poza_ekranem` (kawałki
    docelowego zapisu, do których dopiero lecimy) można pomalować od razu, bo
    ich w kadrze jeszcze nie ma.
    """
    for m in poza_ekranem:
        m.set_color(ZIELONY)
    if na_ekranie:
        scena.play(*[m.animate.set_color(ZIELONY) for m in na_ekranie], run_time=czas)


def rozjasnij_scene(scena, czas=0.4):
    """Gasi kolory na WSZYSTKIM, co jest w kadrze, i dopiero potem przytrzymuje.

    Wersja dla scen, w których po serii `Transform` trudno wskazać, który obiekt
    trzyma jeszcze kolor: po dopasowaniu kształtów manim dokłada do źródła własne
    podobiekty, więc pomalowanie samego pierwotnego kroku potrafi ominąć np. domykający
    nawias (złapane w zad. 3, krok 6: klatka kończyła się szarym nawiasem).
    """
    if scena.mobjects:
        scena.wait(0.35)
        scena.play(*[m.animate.set_color(BLACK) for m in scena.mobjects], run_time=czas)
    scena.wait(PRZYTRZYMANIE)


def zakoncz_krok(scena, *podswietlone, czas=0.4):
    """Koniec kroku: zgaszenie podświetleń, a dopiero potem przytrzymanie.

    Kolor pokazuje, co się przed chwilą stało, więc ma być widoczny w trakcie
    animacji i chwilę po niej. Ale klatka, NA KTÓREJ krok się zatrzymuje, musi
    wyglądać tak samo jak pierwsza klatka następnego filmu, bo w odtwarzaczu to
    jest to samo miejsce. Stąd widoczne rozjaśnienie na końcu kroku (o to prosił
    Henrich przy zad. 3: „dodać rozjaśnienie przyciemnienia w kroku 4").
    """
    if podswietlone:
        scena.wait(0.35)
        scena.play(*[m.animate.set_color(BLACK) for m in podswietlone], run_time=czas)
    scena.wait(PRZYTRZYMANIE)
