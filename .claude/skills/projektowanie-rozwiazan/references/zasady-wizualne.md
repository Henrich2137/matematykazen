# Zasady wizualne (film krok po kroku)

Cztery rzeczy, o których warto wiedzieć, projektując animację. Wszystkie dotyczą tego, że
film to obraz, który **przemija**, a uczeń ogląda go bez lektora.

Podstawa naukowa jest tu opisana uczciwie: gdzie coś jest zmierzone, jest napisane, że
zmierzone, a gdzie to tylko sensownie brzmiąca zasada projektowa, też jest napisane.

---

## 1. Informacja, która znika, zanim ucznia doszła

**Na czym polega.** Sweller, Ayres i Kalyuga opisali *transient information effect*: uczenie
się siada, kiedy informacja znika, zanim uczeń zdążył ją przetworzyć albo powiązać z tym,
co przyszło po niej. W animacji jedna klatka szybko przechodzi w następną, więc uczeń musi
przerobić więcej materiału w narzuconym czasie niż przy obrazku, który po prostu leży.

To jest bezpośrednia konsekwencja naszej decyzji, że animacja ma być zrozumiała bez opisu:
cały ciężar niesie kanał, który sam siebie kasuje.

**Rozstrzygnięcie Henricha (2026-08-26): kadr zostaje czysty.** Podpowiedź, żeby poprzednia
linijka zostawała w kadrze wyszarzona, **odpada**. Kłóci się z zasadą, że krok zaczyna się
i kończy tym samym czystym obrazem (`manimations/README.md`), i wymagałaby szarego tokenu,
którego `COLORS.md` dla tej roli nie ma. Nie proponuj tego ponownie.

**Uwaga, żeby nie pomylić tego z czymś innym.** Zakaz dotyczy **poprzedniej linijki rachunku**.
Nie dotyczy **warunku**, który obowiązuje przez całe zadanie: założenie \(x \ne 1\) stoi
w kadrze na szaro od kroku, w którym powstało, do końca filmu, i tak ma być, bo CKE daje za nie
osobny punkt (zad. 8, 2026-08-27). Nie dotyczy też rachunku pomocniczego z punktu 2b: ten
pojawia się i znika w środku jednego kroku.

**Czym więc walczymy z przemijaniem.** Cztery rzeczy, wszystkie już w projekcie:

- **Rozwiązanie opisowe stoi obok filmu i nie znika.** To jest trwały zapis tego samego toku,
  linijka w linijkę. Dlatego wymóg „tyle linijek, ile kroków" nie jest porządkowym kaprysem:
  to jest właśnie ta trwała wersja, do której uczeń wraca wzrokiem.
- **Kropki i cofanie.** Odtwarzacz pozwala stanąć na dowolnym stanie i cofnąć krok, więc
  uczeń może obejrzeć przejście drugi raz. Projektuj tak, żeby pojedyncze przejście dało się
  zrozumieć przy powtórzeniu, a nie tak, żeby wymagało pamiętania trzech kroków wstecz.
- **Krótkie kroki.** Jedno przekształcenie na krok to nie tylko przejrzystość: to znaczy,
  że w pamięci ucznia w danej chwili siedzi jedna zmiana, nie trzy.
- **To, co rachunek każe zostawić, zostaje w kadrze.** Wzorzec jest w zad. 7 z 2024-grudnia:
  policzoną wartość odstawia się na górę kadru i tam leży, dopóki nie połączy się z drugą.
  Samo odstawienie jest osobnym krokiem.

**Czego z tego NIE wyciągać.** Że skoro obraz przemija, to trzeba dopisać dużo tekstu pod
filmem. Opis jest domyślnie zwinięty, więc to nie jest ratunek. Ratunkiem jest mniejszy krok.

---

## 2. Ruch ma znaczyć to samo, co działanie

**Na czym polega.** Tversky, Morrison i Bétrancourt sformułowali dwa warunki, bez których
animacja nie pomaga:

- **kongruencja**, czyli zgodność tego, co widać, z tym, co się dzieje w pojęciu,
- **uchwytność**, czyli to, że budowę i treść obrazu da się spostrzec łatwo i trafnie.

⚠️ **Uczciwie:** ich przegląd badań znalazł **mało dowodów** na to, że animacja bije zwykły
statyczny rysunek. Animacja nie jest darmowym ulepszeniem. Jeżeli w kroku nic sensownie się
nie porusza, to jest to znak, że ten krok chce być rysunkiem albo linijką tekstu, nie filmem.

**Co z tego wynika przy projektowaniu.** Do każdego kroku dopisz, **czym jest ruch**:

| działanie w rachunku | co ma zrobić obraz |
|---|---|
| przeniesienie wyrazu na drugą stronę | wyraz przelatuje przez znak równości i po drodze zmienia znak |
| skracanie | czynnik odjeżdża z licznika i z mianownika jednocześnie, a nie znika sam z siebie |
| podstawienie | liczba wsuwa się dokładnie w miejsce litery |
| rozdzielenie potęgi iloczynu | wykładnik dojeżdża osobno do każdego czynnika |
| zamiana roli znaku | znak zamienia się w to, czym się staje, zamiast zniknąć i pojawić się obok |

**Zły ruch to zniknięcie i pojawienie się gdzie indziej.** Uczy „coś się stało", a nie
„co się stało". Tak samo lot przez pół kadru między miejscami, które nic ze sobą nie mają:
wtedy brakuje ogniwa i trzeba je dopisać jawnie, a ruch rozbić na dwie animacje w tym samym
kroku (wzorzec: `manimations/README.md`, punkt 17).

**Drugi zły ruch: morf całej strony równania naraz.** Henrich, 2026-08-27, o pierwszej wersji
filmu do zad. 8: „morf wrzucony na całą stronę równania zasłania to, co dzieje się naprawdę".
Przez pół animacji pół zapisu jest kleksem, więc uczeń nie ma czego czytać ani przed, ani po.
W dokumencie projektowym pisz więc, **co robi każdy znak z osobna**: który jedzie i dokąd,
który się pojawia, który znika, który zmienia się w co innego. Jeżeli tego nie umiesz napisać,
to znaczy, że krok jest za duży, a nie że opis jest za drobiazgowy.

W dokumencie projektowym pisz to zdaniami typu „piątka **przesuwa się** na miejsce podstawy",
„jedynka **pojawia się** jako wykładnik", „znak pierwiastka **znika**". Rozróżnienie
przesuwa/pojawia się/znika jest tym, co potem decyduje o kolorze.

---

## 2b. Krok może wyjaśniać, byle kończył się prostą linijką

**Rozstrzygnięcie Henricha, 2026-08-27** (zad. 8): „krok mógłby zawierać wyjaśnienie, a dopiero
się kończyć prostym". To nie łamie zasady „jeden krok = jedno przekształcenie": linijka, która
zostaje w kadrze na końcu kroku, dalej jest jedna. Zmienia się tylko to, że po drodze widać,
skąd się wzięła.

**Jak to zaprojektować:**

- Wyjaśnienie liczy się **w pasie pod rachunkiem, mniejszym pismem**, i znika przed końcem
  kroku. Rozmiar mówi uczniowi, co jest linijką rozwiązania, a co pracą na boku.
- Wyjaśnienie to najczęściej **dopisane ogniwo**: to, co ekspert robi w głowie.
  \(2x-2 = 2\cdot x - 2\cdot 1 = 2(x-1)\), \(2(x+3) = 2\cdot x + 2\cdot 3\), \(x = 1x\).
- **Warunek, który obowiązuje przez całe zadanie** (dziedzina, założenie), wyprowadź w kroku,
  w którym powstaje, a potem **odstaw go NAD rachunek, przy lewej krawędzi**, gdzie zostanie
  do końca filmu. Tak zapisuje się go na kartce.
- **Wolny krok jest w porządku**, jeśli niesie treść. Krok wyprowadzający dziedzinę z dwóch
  mianowników trwa w zad. 8 dwanaście sekund i tak ma być.
- To samo ogniwo **powtórz w komentarzu rozwiązania opisowego**. Film i tekst mają tłumaczyć
  to samo w tym samym miejscu.

---

## 3. Nie każ uczniowi patrzeć w dwa miejsca naraz

**Na czym polega.** Efekt podzielonej uwagi: kiedy jeden kanał, wzrok, niesie dwie rzeczy,
które trzeba scalić w głowie, uczeń traci część mocy na samo scalanie. Chandler i Sweller
pokazali doświadczalnie, że wpisanie tekstu **w** rysunek zamiast obok niego ten koszt
zdejmuje.

**Co z tego wynika:**

- **Etykieta idzie tam, czego dotyczy.** Miara kąta przy kącie, długość przy boku, nazwa
  krzywej przy krzywej. Nie legenda z boku, nie ramka pod spodem.
- **W geometrii odwzoruj oznaczenia z rysunku w arkuszu.** Uczeń ma jedno zadanie, nie dwa
  różne obrazki tej samej figury.
- **Podpis, który może zostać przecięty przez ruchomy element, dostaje tło w kolorze płótna.**
  To uwaga z widżetów, ale w scenie z przesuwającymi się napisami obowiązuje tak samo.
- **Jeden wzór na jeden krok.** Dwa wzory obok siebie to dwa miejsca do patrzenia.

---

## Czego świadomie nie stosujemy

- **Zasady Mayera zakładające lektora**: modality, redundancy, temporal contiguity, voice.
  Nasze filmy nie mają dźwięku. Każdy scenariusz, który mówi „narrator wyjaśnia", jest
  nie do zrealizowania i wraca do poprawki.
- **Wyszarzanie poprzedniego stanu**, patrz punkt 1.
