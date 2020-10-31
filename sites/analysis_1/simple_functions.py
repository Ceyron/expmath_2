import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def simple_functions():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/einfache_funktionen",
        width=1000,
        height=830
    )

details = {
    "german": {
        "title": "Die Standardfunktionen",
        "introduction": "",
        "theory": [
            (
                "Was ist eine Funktion?",
                r"""
                Eine Funktion $f: \mathcal{U} \to \mathcal{V}$ ist eine
                    Zuordnung, die jedem Element $u\in\mathcal{U}$ des
                    Definitionsbereichs $\mathcal{U}$ genau ein Element
                    $v\in\mathcal{V}$ des Bild- bzw. Wertebereichs $\mathcal{V}$
                    vermöge $f: u \mapsto v$, d.h. $f(u) = v$, zuordnet.

                Hier wenden wir uns Funktionen $f: D \to B$ mit dem Definitions-
                    bzw. Bildbereich $D,B \subseteq \mathbb{R}$ zu, die reelle
                    Zahlen auf reelle Zahlen abbilden.
                """
            ),
            (
                "Eigenschaften von Funktionen",
                r"""
                Unterschiedliche Funktionen haben unterschiedliche
                    Eigenschaften, die das charakteristische Verhalten und
                    Aussehen der jeweiligen Funktion beschreiben.

                * Injektivitat und Surjektivität
                    * **injektive Funktion** $\quad$ $x_1 \neq x_2, x_1,x_2\in
                      D  \Rightarrow  f(x_1) \neq f(x_2)$
                    * **surjektive Funktion** $\quad$ $\forall y\in B 
                      \exists x\in D:  f(x) = y$
                    * Eine Funktion heißt **bijektiv**, wenn sie sowohl
                      injektiv als auch surjektiv ist.
                * Monotonie
                    * **monoton wachsende Funktion** $\quad$ $x_1 < x_2 
                      \Rightarrow  f(x_1) \leq f(x_2)$
                    * **streng monoton wachsende Funktion** $\quad$ $x_1 < x_2
                       \Rightarrow f(x_1) < f(x_2)$
                    * Analog lassen sich monoton fallende und streng monoton
                      fallende Funktionen definieren.
                * Gerade und ungerade Funktionen
                    * **gerade Funktion** $\quad$ $f(x) = f(-x)  \forall x\in
                        D$: eine gerade Funktion ist spiegelsymmetrisch zur
                        $y$-Achse.
                    * **ungerade Funktion** $\quad$ $f(x) = -f(x)  \forall
                        x\in D$: eine ungerade Funktion ist drehsymmetrisch zum
                        Ursprung.
                * Periodizität
                    * Eine periodische Funktion $f: D \to B$ erfüllt die
                      Eigenschaft $f(x) = f(x+T)  \forall x\in D$. Darin ist
                      $T\neq0$ die Periode, nach der sich die Funktionswerte
                      wiederholen. Periodizität zeichnet sich also durch immer
                      wiederkehrendes Verhalten aus.
                * Globale und lokale Extrema
                    * Der Funktionswert $f_{\text{max}} = f(x_{\text{max}})$
                        heißt <b>globales Maximum</b> von $f$ in $D$, wenn
                        $f_{\text{max}} \geq f(x)  \forall x \in D$ gilt.
                    * Die Funktion $f$ hat an der Stelle $x_{\text{M}}$ ein
                        **lokales Maximum**, wenn gilt: $\exists 
                        \varepsilon:  f(x_{\text{M}}) \geq f(x)  \forall
                        x\in(x_{\text{M}}-\varepsilon, x_{\text{M}}+
                        \varepsilon) \cap D  \subseteq D.$
                    * Analog lassen sich die Bedingungen für globale und lokale
                      Minima definieren.
                """
            ),
            (
                "Standardfunktionen",
                r"""
                * Potenzfunktionen $f(x) = x^a$
                    * $f: \mathbb{R} \to \mathbb{R}$ mit $a \in \mathbb{N}$
                    * $f: \mathbb{R}\backslash\{0\} \to \mathbb{R}$ mit $a < 0$,
                      $a\in\mathbb{Z}$
                    * $f: [0, \infty) \to \mathbb{R}$ für $a \geq 0$, sonst $f:
                      (0,\infty) \to \mathbb{R}$
                * Polynom vom Grad $n$: $f(x) = a_0 + a_1 x + a_2 x^2 + \ldots +
                  a_{n-1}x^{n-1} + a_n x^n$
                    * Polynome sind in $\mathbb{C}$ in Linearfaktoren zerlegbar.
                        Damit haben sie höchstens $n$ Nullstellen in
                        $\mathbb{R}$.
                * Exponentialfunktionen $f: (0,\infty) \to \mathbb{R}$ vermöge
                  $f(x) = a^x$ mit $a > 0$
                    * Exponentialfunktionen sind die Umkehrfunktionen zum
                      Logarithmus (s.u.)
                    * Logarithmusfunktionen $f: (0,\infty) \to \mathbb{R}$
                      vermöge $f(x) = \operatorname{log}_a x$ mit $a>1$
                """
            )
        ],
        "plot": simple_functions,
        "questions": [
            (
                "Teil 1 - Was ist eine Funktion?",
                r"""
                1. Welche Informationen sind nötig, um eine Funktion zu
                   definieren?
                2. Erläutern Sie, warum eine Änderung des Definitions- bzw.
                    Bildbereichs eine andere Funktion bedeutet. Versuchen Sie,
                    dies an einer Skizze zu erklären.
                3. Kann eine Zahl $y\in B$ zwei Urbilder $x \in D$ haben? Warum?
                    Warum nicht? Wie kann man dies in einer Skizze erkennen?
                4. Kann eine Zahl $x\in D$ zwei Bilder $y\in B$ haben? Warum?
                   Warum nicht? Wie kann man dies in einer Skizze erkennen?
                """
            ),
            (
                "Teil 2 - Erkundung der Grafik",
                r"""
                1. Untersuchen Sie die unterschiedlichen Schaltflächen der
                    Grafik. Welchen Einfluss hat eine Veränderung der Parameter
                    auf das Aussehen der unterschiedlichen Funktionen?
                2. Was fällt Ihnen bei der Skizze zur Heaviside-Funktion auf?
                    Wie würden Sie die Funktion auf dem Papier skizzieren? Worin
                    liegen die Unterschiede?
                3. Was fällt Ihnen bei der Skizze zum Tangens auf? Wie würden
                    Sie die Funktion auf dem Papier skizzieren? Worin liegen die
                    Unterschiede? Warum ist nur einer der beiden Darstellungen
                    mathematisch korrekt? Welche?
                """
            ),
            (
                "Teil 3 - Eigenschaften von Funktionen",
                r"""
                1. Was bedeutet Injektivität anschaulich? Woran erkennt man dies
                    an der Definition der Injektivität? Fertigen Sie Skizzen von
                    injektiven und nicht injektiven Funktionen an.
                1. Was bedeutet Surjektivität anschaulich? Woran erkennt man
                    dies an der Definition der Surjektivität? Fertigen Sie
                    Skizzen von surjektiven und nicht surjektiven Funktionen an.
                1. Ist die Funktion $f(x) = x^2$ injektiv oder surjektiv? Können
                    Sie dies in der Form, in der die Funktion angegeben ist,
                    beurteilen?
                1. Passen Sie die Angabe von $f$ so an, dass Sie die beiden
                    Eigenschaften der Injektivität und Surjektivität überprüfen
                    können.
                1. Für welche Definitions- bzw. Wertebereiche ist $f$ mit $f(x)
                   = x^2$ injektiv bzw. surjektiv?
                1. Kommentieren Sie die beiden Aussagen: 
                    * Injektivität ist eine Eigenschaft, die durch den
                      Definitionsbereich bestimmt wird.
                    * Surjektivität wird durch den Bildbereich beeinflusst.
                1. Leiten Sie die Definition für (streng) monoton fallende
                    Funktionen aus der obigen Definition wachsender Funktionen
                    ab.
                1. Skizzieren Sie je eine streng monoton wachsende bzw. fallende
                    und eine monoton wachsende bzw. fallende Funktion. Worin
                    erkennen Sie den entscheidenden Unterschied.
                1. Kommentieren Sie:
                    * Wenn eine Funktion nicht monoton fällt, wächst sie
                      monoton.
                    * Wenn eine Funktion nicht ungerade ist, ist sie gerade.
                1. Worin liegt der Unterschied zwischen globalen und lokalen
                    Maxima bzw. Minima? Woran erkennt man dies an der Definition
                    der beiden Begriffe?
                1. Skizzieren Sie eine Funktion, die ein lokales, aber kein
                    globales Maximum hat.
                """
            )
        ]
    }
}

if __name__ == "__main__": simple_functions()