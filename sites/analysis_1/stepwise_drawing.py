import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def stepwise_drawing():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/schrittweises_skizzieren",
        width=1200,
        height=410
    )

details = {
    "german": {
        "title": "Schrittweises Skizzieren von Funktionen",
        "introduction": "",
        "theory": [
            (
                "Skizzieren von Funktionen",
                r"""
                Über viele Funktionen wissen wir bereits eine Menge. Welche
                    Eigenschaften haben sie? Wie sieht die Funktion aus? Welche
                    charakteristischen Punkte müssen wir berücksichtigen?

                Allerdings sieht man nicht immer sofort vor dem inneren Auge,
                    wie eine Funktion aussieht. Dies kann vor allem bei
                    zusammengesetzten Funktionen schwierig sein.
                """
            ),
            (
                "Zerlegen in Teilfunktionen",
                r"""
                Bei Funktionen, die aus mehreren Teilen zusammengesetzt sind,
                kann man sich durch eine Rückführung auf bekannte Terme und
                Graphen Schritt für Schritt dem Funktionsgraphen nähern.

                Dazu untersuchen wir die Funktion und suchen nach einem Term,
                dessen Graph wir kennen.

                Durch schrittweise Erweiterung dieser Teilfunktion um die in der
                jeweiligen Funktion vorkommenden Terme entwickeln wir
                Teilgraphen, die mit jedem Schritt erweitert werden.

                Wenn wir dies so lange wiederholen, bis die ursprüngliche
                Funktion betrachtet wird, landen wir schließlich beim gesuchten
                Funktionsgraphen.
                """
            ),
        ],
        "plot": stepwise_drawing,
        "questions": [
            (
                "Teil 1 - Erkundung der Grafik",
                r"""
                1. Schauen Sie sich die vier verschiedenen Funktionen an. Haben
                    Sie ohne Nutzung der Grafik eine Vorstellung von den
                    zugehörigen Funktionsgraphen?
                1. Gehen Sie die Schritte für die erste Funktion
                    $\displaystyle\frac{1}{\sqrt{1+x^2}}$ durch. Welche Graphen
                    erkennen Sie in den einzelnen Schritten?
                1. Fertigen Sie eine eigene Skizze an, in die Sie die Schritte
                   aus der Grafik übertragen.
                1. Skizzieren Sie die Funktion $\displaystyle
                   \sin^2\left(x+\frac{\pi}{2}\right)$.
                    * Notieren Sie dazu zunächst die vorkommenden
                      Teilfunktionen.
                    * Skizzieren Sie die Teilfunktionen nacheinander in einem
                      Koordinatensystem.
                    * Überprüfen Sie Ihre Skizzen mithilfe der Grafik.
                1. Fertigen Sie Skizzen der übrigen in der Grafik auftauchenden
                    Funktionen an.
                1. Nutzen Sie auch hier Teilfunktionen und überprüfen Sie Ihre
                   Skizzen mithilfe der Grafik.
                1. Was fällt Ihnen bei der Skizze zu $\displaystyle \frac{1}{x^2
                    -2}$ auf? Wie unterscheidet sich Ihre Skizze von der Skizze
                    in der Grafik? Warum ist nur eine der beiden Darstellungen
                    mathematisch richtig? Welche?
                """
            ),
            (
                "Teil 2 - Zerlegen in Teilfunktionen",
                r"""
                1. Skizzieren Sie die Funktion $\displaystyle f(x) =
                   \frac{1}{(x-3)^2}$.
                    * Identifizieren Sie dazu zunächst die Teilfunktionen in
                      $f$.
                    * Skizzieren Sie die Funktionen $f_1(x) = x$, $f_2(x)=x-3$,
                        $f_3(x)=(x-3)^2$ und schließlich $f_4(x) = f(x)$
                        nacheinander in einem Koordinatensystem.
                1. Skizzieren Sie die Funktion $\displaystyle g(x) =
                   \frac{1}{(x+3)^2}$.
                    * Identifizieren Sie dazu die Teilfunktionen $g$ und
                        skizzieren Sie diese nacheinander in einem
                        Koordinatensystem.
                1. Skizzieren Sie die Funktion $\displaystyle h(x) =
                    \frac{1}{(x-3)^2} + \frac{1}{(x+3)^2}$. Nutzen Sie dazu die
                    Skizzen von $f$ und $g$.
                1. Trainieren Sie das schrittweise Skizzieren, indem Sie sich
                    weitere Beispiele ausdenken und dort jeweils Teilfunktionen
                    identifizieren und skizzieren.
                """
            )
        ]
    }
}

if __name__ == "__main__": stepwise_drawing()