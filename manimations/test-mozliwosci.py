"""Kontrola mozliwosci Manima w tym obrazie kontenera.

Nie sa to sceny produkcyjne, tylko sonda: "czy po przebudowie obrazu dalej
dziala wszystko, czego potrzebuje matura". Dlatego wolno ja renderowac
z flaga jakosci (-ql), zakazana dla scen idacych na strone.

    manim -ql test-mozliwosci.py A_LiczbyDynamiczne
    for s in A_LiczbyDynamiczne B_UkladWspolrzednych C_Bryly3D \
             D_GeometriaPlaska E_DaneITabele G_SamaMatematyka H_PolskiPrzezText; do
        manim -ql --disable_caching test-mozliwosci.py $s || echo "PADLO: $s"
    done

Wszystkie siedem przechodzi (sprawdzone 2026-08-25, Manim 0.18.1).
Osma sytuacja jest CELOWO nieobecna: polski tekst w Tex()/MathTex() wywala
render (OT1), patrz README.md, sekcja "Pulapki Manima". Stad H_PolskiPrzezText.
"""
from manim import *


class A_LiczbyDynamiczne(Scene):
    """Wyrazenie algebraiczne, w ktorym liczba zmienia sie plynnie."""
    def construct(self):
        a = ValueTracker(1)
        wzor = always_redraw(lambda: MathTex(
            r"f(x) = ", f"{a.get_value():.2f}", r"x^2 + 3x - 5"
        ).scale(1.2))
        self.add(wzor)
        self.play(a.animate.set_value(4), run_time=1)
        # drugi wariant: DecimalNumber podpiety do wzoru
        licznik = DecimalNumber(0, num_decimal_places=1).next_to(wzor, DOWN)
        licznik.add_updater(lambda m: m.set_value(a.get_value() * 2))
        self.add(licznik)
        self.play(a.animate.set_value(0.5), run_time=1)


class B_UkladWspolrzednych(Scene):
    """Uklad wspolrzednych, wykres funkcji, miejsce zerowe, pole pod wykresem."""
    def construct(self):
        osie = Axes(x_range=[-3, 3, 1], y_range=[-2, 6, 2], axis_config={"include_numbers": True})
        etykiety = osie.get_axis_labels(x_label="x", y_label="y")
        parabola = osie.plot(lambda x: x**2 - 1, color=BLUE)
        prosta = osie.plot(lambda x: 2 * x + 1, color=RED)
        pole = osie.get_area(parabola, x_range=[-1, 1], color=GREEN, opacity=0.4)
        punkt = Dot(osie.c2p(1, 0), color=YELLOW)
        self.add(osie, etykiety, parabola, prosta, pole, punkt)
        self.play(Create(parabola), run_time=0.5)


class C_Bryly3D(ThreeDScene):
    """Bryly z matury: stozek, walec, ostroslup, kula, szescian."""
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=40 * DEGREES)
        osie = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        kula = Sphere(radius=0.7).set_color(BLUE).shift(LEFT * 3)
        szescian = Cube(side_length=1.2).set_color(RED)
        stozek = Cone(base_radius=0.7, height=1.5).set_color(GREEN).shift(RIGHT * 3)
        walec = Cylinder(radius=0.6, height=1.4).set_color(YELLOW).shift(UP * 2.5)
        # ostroslup prawidlowy czworokatny, budowany recznie
        ostroslup = Polyhedron(
            vertex_coords=[[-.7, -.7, 0], [.7, -.7, 0], [.7, .7, 0], [-.7, .7, 0], [0, 0, 1.5]],
            faces_list=[[0, 1, 2, 3], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]],
        ).shift(DOWN * 2.5)
        powierzchnia = Surface(
            lambda u, v: np.array([u, v, 0.4 * (u**2 - v**2)]),
            u_range=[-1, 1], v_range=[-1, 1], resolution=(8, 8),
        ).set_opacity(0.6).shift(LEFT * 3 + DOWN * 2.5)
        self.add(osie, kula, szescian, stozek, walec, ostroslup, powierzchnia)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(0.5)


class D_GeometriaPlaska(Scene):
    """Figury plaskie, katy, oznaczenia bokow, okrag opisany."""
    def construct(self):
        A, B, C = np.array([-2, -1, 0]), np.array([2, -1, 0]), np.array([0.5, 2, 0])
        trojkat = Polygon(A, B, C, color=BLUE)
        kat = Angle(Line(A, B), Line(A, C), radius=0.6)
        kat_prosty = RightAngle(Line(B, A), Line(B, C), length=0.4)
        okrag = Circle(radius=2.2).move_to(ORIGIN)
        opis = MathTex(r"\alpha").next_to(kat, RIGHT, buff=0.1)
        bok = Brace(Line(A, B), direction=DOWN)
        dlugosc = bok.get_tex(r"a = 4")
        self.add(okrag, trojkat, kat, kat_prosty, opis, bok, dlugosc)


class E_DaneITabele(Scene):
    """Diagram slupkowy i tabela, czyli statystyka z matury."""
    def construct(self):
        wykres = BarChart(
            values=[3, 7, 5, 9, 2],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 10, 2],
        ).scale(0.6).shift(LEFT * 3)
        tabela = MathTable(
            [["x", "1", "2", "3"], ["y", "2", "4", "6"]],
            include_outer_lines=True,
        ).scale(0.5).shift(RIGHT * 3)
        self.add(wykres, tabela)


class G_SamaMatematyka(Scene):
    """To samo co F, ale BEZ polskiego tekstu w Tex()."""
    def construct(self):
        self.add(VGroup(
            MathTex(r"\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}"),
            MathTex(r"\sqrt[3]{27} = 3 \quad \left| -5 \right| = 5"),
            MathTex(r"\frac{a}{b} \div \frac{c}{d} \cdot \sqrt{\frac{2}{3}}"),
            MathTex(r"\sum_{i=1}^{n} a_i \qquad \lim_{x \to 0} \frac{\sin x}{x}"),
            MathTex(r"\binom{n}{k} \quad \log_{2} 8 \quad \sin^2\alpha + \cos^2\alpha = 1"),
            MathTex(r"x \in \langle -2; 3 \rangle \cup (5; +\infty)"),
        ).arrange(DOWN, buff=0.35).scale(0.8))

class H_PolskiPrzezText(Scene):
    """Polskie znaki przez Text() (Pango), z pominieciem LaTeXa."""
    def construct(self):
        self.add(VGroup(
            Text("Pole trójkąta wynosi", font_size=34),
            Text("Zażółć gęślą jaźń ĄĆĘŁŃÓŚŹŻ", font_size=34),
            VGroup(Text("wzór: ", font_size=34), MathTex(r"P=\tfrac12 ah").scale(1.1)).arrange(RIGHT),
        ).arrange(DOWN, buff=0.4))
