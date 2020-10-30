import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def complex_roots():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/komplexes_wurzelziehen",
        width=1000,
        height=410
    )

details = {
    "german": {
        "title": "Komplexe Wurzeln",
        "introduction": "",
        "theory": [
            (
                "Definition: n-te komplexe Wurzel",
                r"""
                Die $n$-te komplexe Wurzel von $a\in\mathbb{C}$ ist die Lösung
                von

                $z^n = a.$

                Die $n$-te Einheitswurzel $\displaystyle \varepsilon_k =
                    {\rm{e}}^{2\pi i \frac{k}{n}}$ mit $k = 0, 1, \ldots, n-1$
                    hat die Eigenschaften

                $\lvert\varepsilon_k\rvert = 1 \text{ und } \varepsilon_k^n =
                    {\rm{e}}^{2\pi i k} = \left({\rm{e}}^{2\pi i}\right)^k = 1$

                und ist damit die Lösung von $z^n = 1$. Die $n$ Einheitswurzeln
                    $\varepsilon_k$ bilden in der Gaußschen Zahlenebene ein
                    regelmäßiges $n$-Eck.
                """
            ),
            (
                "Berechnung der n-ten Wurzeln",
                r"""
                Zur Berechnung der $n$ komplexen Wurzeln lösen wir die Gleichung
                $z^n = a.$

                Damit wir die Potenzgesetze ausnutzen können, nutzen wir die
                Polarkoordinatendarstellung von $z$ und $a$:

                $z^n = \left(r\cdot{\rm{e}}^{i\varphi}\right)^n =
                    r^n\cdot{\rm{e}}^{i\varphi\cdot n} = s\cdot {\rm{e}}^{i\psi}
                    = a.$

                Der entscheidende Schritt ist nun die Berücksichtigung der
                $2\pi$-Periodizität der Polarkoordinatendarstellung:

                $z^n = r\cdot{\rm{e}}^{i\psi + 2\pi i} = r\cdot{\rm{e}}^{i\psi +
                2 \pi i k}.$

                Nun können wir die Gleichung nach $z$ auflösen und es entstehen
                    $n$ von $k$ abhängige Lösungen $z_k$ mit $k =
                    0,1,\ldots,n-1$.
                """
            ),
        ],
        "plot": complex_roots,
        "questions": [
            (
                "Teil 1 - Erkundung der Grafik",
                r"""
                1. Erkunden Sie die unterschiedlichen Schaltflächen und
                   Schieberegler der Grafik.
                2. Was ist in der Skizze dargestellt? Welche Achsen gibt es?
                3. Was beobachten Sie, wenn Sie die Ordnung der Wurzel erhöhen?
                4. Denken Sie sich eine komplexe Zahl $a$ aus, und bestimmen Sie
                    Wurzeln unterschiedlicher Ordnung. Beschreiben Sie Ihre
                    Beobachtungen.
                """
            ),
            (
                "Teil 2 - Was sind komplexe Wurzeln?",
                r"""
                1. Bestimmen Sie die fünften komplexen Wurzeln aus
                    $\displaystyle a = \frac{1}{\sqrt{2}} + {\rm{i}} \cdot
                    \frac{1}{\sqrt{2}}$.
                2. Verwenden Sie dazu nicht auswendig gelernte Formeln, sondern
                    rechnen Sie sie Schritt für Schritt aus, indem Sie die
                    Gleichung $z^n = a$ nach $z$ umformen. Erläutern Sie Ihre
                    Gedankengang und Ihre Rechnung.
                3. Suchen Sie dazu zunächst nach den
                   Polarkoordinatendarstellungen von $z$ und $a$.
                4. Nutzen Sie zur Bestimmung der Polarkoordinatendarstellung von
                    $a$ beispielsweise die Eulersche Identität
                    ${\rm{e}}^{i\varphi} = \operatorname{cos}\varphi + {\rm{i}}
                    \operatorname{sin}\varphi$ oder eine Skizze, in der Sie
                    Winkel und Abstand vom Ursprung ablesen können.
                5. Überprüfen Sie Ihr Ergebnis mithilfe der Grafik. Wie gelingt
                   dies besonders leicht? Kann Ihr Ergebnis stimmen?
                """
            ),
            (
                "Teil 3 - Komplexe Wurzeln in der Gaußschen Zahlenebene",
                r"""
                1. Skizzieren Sie Ihre Ergebnisse zur fünften Wurzel aus Teil 2
                   in der Gaußschen Zahlenebene.
                2. Erläutern Sie, warum der Index $k$ von $0$ bis $n-1$ läuft.
                   Warum sollte er nicht unendlich weiter laufen?
                3. Testen Sie dies, indem Sie die fünften Wurzeln aus
                    $\displaystyle a = \frac{1}{\sqrt{2}} + {\rm{i}} \cdot
                    \frac{1}{\sqrt{2}}$ hernehmen, und den Laufindex
                    $k=0,1,2,3,4,5,6,\ldots $ beliebig hoch laufen lassen. Was
                    beobachten Sie?
                4. Kommentieren Sie die Aussagen: 
                    * Es gibt genau $n$ $n$-te Wurzeln aus $a\in\mathbb{C}$.
                    * Es gibt genau $n$ verschiedene $n$-te Wurzeln aus
                      $a\in\mathbb{C}$.
                    * Es gibt unendlich viele $n$-te Wurzeln aus
                      $a\in\mathbb{C}$.
                """
            )
        ]
    }
}

if __name__ == "__main__":
    complex_roots()