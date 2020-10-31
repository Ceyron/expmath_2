import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def trigonometric_functions():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/trigonometrische_funktionen",
        width=1000,
        height=430
    )

details = {
    "german":{
        "title": "Trigonometrische Funktionen am Einheitskreis",
        "introduction": "",
        "theory": [
            (
                "Parametrisierung des Einheitskreises",
                r"""
                Die trigonometrischen Funktionen lassen sich am Einheitskreis
                    definieren. Der Einheitskreis ist dabei ein Kreis um den
                    Ursprung mit dem Radius $1$ beschrieben durch $x^2 + y^2 =
                    1$.

                Dieser Einheitskreis wird mithilfe einer Variablen
                    $t\in\mathbb{R}$ parametrisiert. Wenn $t$ größer wird,
                    laufen wir im mathematisch positiven Drehsinn entlang der
                    Kreislinie. So entstehen

                $t = 0 \mapsto \begin{pmatrix} 1 \\ 0 \end{pmatrix}  , 
                t = \frac{\pi}{2} \mapsto \begin{pmatrix} 0 \\ 1 \end{pmatrix} \
                , \,
                t = \pi \mapsto \begin{pmatrix} -1 \\ 0 \end{pmatrix} \
                \text{usw.}$

                Diese Parametrisierung ist $2\pi$-periodisch, $t$ und $t + 2\pi
                    k$ beschreiben also denselben Punkt des Einheitskreises.
                """
            ),
            (
                "Grad- oder Bogenmaß?",
                r"""
                Für die Angabe von Winkeln gibt es verschiedene Einheiten. Das
                    Gradmaß teilt einen vollständigen Umlauf in 360 Teile und
                    gibt relativ dazu den Winkel an. Im wissenschaftlichen
                    Bereich nutzt man das Bogenmaß, das auch als SI-Standard zur
                    Winkelmessung festgelegt ist.

                Als Referenzgröße im Bogenmaß dient die Länge $L = 2\pi$ des
                    Umfangs des Einheitskreises. Winkel werden durch die Länge
                    des Kreisbogenstücks, das durch diesen Winkel ausgeschnitten
                    wird, angegeben.
                """
            ),
            (
                "Trigonometrische Funktionen im Einheitskreis",
                r"""
                Kosinus und Sinus beschreiben die Seitenverhältnisse im
                    rechtwinkligen Dreieck. Der zwischen Ankathete und
                    Hypotenuse eingeschlossene Winkel $\varphi$ ist durch die
                    Verhältnisse der Längen der Dreiecksseiten festgelegt.

                Der Kosinus eines Winkels $\varphi$ wird durch

                $\cos \varphi = \frac{\text{Ankathete}}{\text{Hypotenuse}} =
                \frac{x}{r},$

                der Sinus durch

                $\sin\varphi = \frac{\text{Gegenkathete}}{\text{Hypotenuse}}
                =\frac{y}{r}$

                definiert.

                Im Einheitskreis mit $r = 1$ lassen sich die Werte dieser Größen
                also direkt am Dreieck ablesen.

                Auch für Werte $\varphi > 2\pi$ oder $\varphi < 0$ lassen sich
                    auf diese Weise sinnvoll Funktionswerte für Sinus und
                    Kosinus ablesen. Dazu nutzt man die $2\pi$-Periodizität der
                    Parametrisierung des Einheitskreises aus, die sich in der
                    $2\pi$-Periodizität der trigonometrischen Funktionen
                    widerspiegelt. Indem wir den Weg auf dem Einheitskreis
                    parametrisieren und durchlaufen, entstehen die
                    trigonometrischen Funktionen $\sin: \mathbb{R} \to
                    \mathbb{R}$ und $\cos: \mathbb{R} \to \mathbb{R}$.

                Eine weitere, gelegentlich vorkommende trigonometrische Funktion
                ist der Tangens. Der Tangens eines Winkels $\varphi$ wird durch

                $\operatorname{tan} \varphi =
                \frac{\text{Gegenkathete}}{\text{Ankathete}} = \frac{x}{y}$

                definiert. Auch hier können wir durch ein Durchlaufen des
                Einheitskreises eine Funktion $\displaystyle\operatorname{tan}:
                \mathbb{R}\backslash\left\{\frac{\pi}{2} + n \pi, n \in
                \mathbb{Z}\right\}$ erzeugen.
                """
            ),
            (
                "Trigonometrischer Pythagoras",
                r"""
                Wie in jedem rechtwinkligen Dreieck gilt auch in dem Dreieck im
                Einheitskreis mit den Katheten $\sin\varphi$, $\cos\varphi$ und
                der Hypotenuse $r = 1$  der Satz des Pythagoras:

                $\cos^2\varphi + \sin^2\varphi = 1 \ \forall \varphi \in
                \mathbb{R}.$
                """
            )
        ],
        "plot": trigonometric_functions,
        "questions": [
            (
                "Teil 1 - Trigonometrische Funktionen im Einheitskreis",
                r"""
                1. Fertigen Sie eine Skizze an, und erfinden Sie die Definition
                    der trigonometrischen Funktionen nach. Markieren Sie, wo Sie
                    welche Größe finden, und gehen Sie möglichst kleinschrittig
                    vor.
                1. Vergleichen Sie die oben beschriebene Konstruktion und
                    Definition der trigonometrischen Funktionen mit der Skizze
                    auf Ihrer
                    [Formelsammlung](https://www.tu-braunschweig.de/index.php?eID=dumpFile&t=f&f=47132&token=88937fc7f90ba68b87a277dfac00f46645defeb0)
                    . Wo finden Sie welche Größen wieder?
                """
            ),
            (
                "Teil 2 - Erkundung der Grafik",
                r"""
                1. Beschreiben Sie, was in der Grafik dargestellt ist. Wie
                   finden Sie den rechten im linken Graph wieder und umgekehrt?
                1. Erläutern Sie, wie es im Graph zum Sinus zu Extremstellen,
                    Nullstellen, fallenden und wachsenden Abschnitten kommt.
                    Nutzen Sie dazu beide Grafiken.
                1. Geben Sie an, an welchen Stellen auf ganz $\mathbb{R}$ der
                    Sinus Nullstellen hat. Wo liegen die Minima, wo die Maxima?
                    Lassen Sie sich von beiden Graphen unterstützen.
                1. Erläutern Sie, wie es im Graph zum Kosinus zu Extremstellen,
                    Nullstellen, fallenden und wachsenden Abschnitten kommt.
                    Nutzen Sie dazu beide Grafiken.
                1. Geben Sie an, an welchen Stellen auf ganz $\mathbb{R}$ der
                    Kosinus Nullstellen hat. Wo liegen die Minima, wo die
                    Maxima? Lassen Sie sich von beiden Graphen unterstützen.
                1. Was fällt Ihnen bei der Skizze zum Tangens auf? Fertigen Sie
                    eine eigene Skizze auf dem Papier an. Worin liegen die
                    Unterschiede? Warum ist nur einer der beiden Darstellungen
                    mathematisch korrekt? Welche?
                1. Warum ist der Tangens nicht auf ganz $\mathbb{R}$ definiert?
                    Warum liegen die Definitionslücken gerade bei $\displaystyle
                    \frac{\pi}{2} + n\pi$ mit $n\in\mathbb{Z}$?
                """
            ),
        ]
    }
}

if __name__ == "__main__":
    trigonometric_functions()