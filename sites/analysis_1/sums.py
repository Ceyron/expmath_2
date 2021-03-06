import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def sums():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/reihen",
        width=1000,
        height=430
    )

details = {
    "german": {
        "title": "Partialsummen und Reihen",
        "introduction": "",
        "theory": [
            (
                "Definition einer Reihe als Folge von Partialsummen",
                r"""
                Die Reihe oder unendliche Summe

                $\sum_{k = 0}^{\infty} a_k = a_0 + a_1 + a_2 + a_3 + \ldots$

                mit den Summanden $a_k$, $k\in \mathbb{N}$, ist die Folge
                $(s_n)_{n = 0}^{\infty}$ der Partialsummen

                $s_n = \sum_{k=0}^n a_k = a_0 + a_1 + a_2 + \ldots + a_n.$
                """
            ),
            (
                "Wann konvergiert eine Reihe?",
                r"""
                Konvergiert die Partialsummenfolge $(s_n)_{n=0}^\infty$, so
                    heißt die zugehörige Reihe konvergent. Der Grenzwert
                    $\displaystyle \lim_{n\to \infty} (s_n)_{n=0}^\infty$ heißt
                    dann der Wert der Reihe.

                Konvergiert die Reihe $\displaystyle\sum_{k = 0}^{\infty} a_k$,
                so bilden ihre Summanden $a_k$ eine Nullfolge.

                Eine Reihe $\displaystyle\sum_{k = 0}^{\infty} a_k$ konvergiert
                    absolut, wenn die Reihe $\displaystyle\sum_{k = 0}^{\infty}
                    \lvert a_k\rvert$ der Absolutbeträge konvergiert.
                """
            ),
            (
                "Konvergenzkriterien",
                r"""
                Um die Konvergenz von Reihen zu überprüfen, gibt es verschiedene
                Kriterien.

                * Vergleichskriterium
                    * $\displaystyle\sum_{k = 0}^{\infty} b_k$ konvergente
                            Majorante mit $\lvert a_k\rvert \leq \lvert
                            b_k\rvert$ $\Rightarrow$ $\displaystyle\sum_{k =
                            0}^{\infty} a_k$ absolut konvergent
                    * $\displaystyle\sum_{k = 0}^{\infty} b_k$ divergente
                      Minorante mit $a_k \geq b_k$ $\Rightarrow$
                      $\displaystyle\sum_{k = 0}^{\infty} a_k$ divergent
                * Quotientenkriterium:
                    * $\displaystyle\limsup_{k \to
                      \infty}\biggl|\frac{a_{k+1}}{a_k}\biggr| \begin{cases} < 1
                      & {\scriptstyle\text{ Reihe absolut konvergent}} \\ = 1 &
                      {\scriptstyle\text{ keine Aussage möglich}} \\ > 1 &
                      {\scriptstyle\text{ keine Aussage möglich}} \end{cases}$
                * Wurzelkriterium:
                    * $\displaystyle\limsup_{k\to\infty} \sqrt[k]{\lvert a_k
                      \rvert} \begin{cases} < 1 & {\scriptstyle\text{ Reihe
                      absolut konvergent}} \\ = 1 & {\scriptstyle\text{ keine
                      Aussage möglich}} \\ > 1 & {\scriptstyle\text{ Reihe
                      divergent}} \end{cases}$
                * Leibniz-Kriterium: wenn für eine Reihe $\displaystyle\sum_{k =
                  0}^{\infty} a_k$ die Bedingungen
                    * $\displaystyle\lim_{k \to \infty} a_k = 0$
                    * $(\lvert a_k\rvert)_{k=0}^\infty$ monoton fallend
                    * alternierend erfüllt sind, ist sie konvergent.
                """
            ),
        ],
        "plot": sums,
        "questions": [
            (
                "Teil 1 - Was ist eine Reihe?",
                r"""
                1. Was unterscheidet eine Reihe von einer Folge?
                2. Welche Gemeinsamkeiten haben Reihen und Folgen?
                3. Welche unterschiedlichen Möglichkeiten gibt es, eine Reihe
                   darzustellen?
                4. Denken Sie sich ein Beispiel für eine Folge aus. Wie sieht
                    die zugehörige Reihe aus? Notieren Sie jeweils die ersten
                    fünf Folgen- und Reihenglieder.
                5. Wo finden Sie die Folge, wo die Reihe in den obigen Skizzen?
                   Erkunden Sie, was Sie mit der Grafik anstellen können.
                6. Fertigen Sie ähnliche Skizzen auch für Ihr eigenes Beispiel
                   an.
                """
            ),
            (
                "Teil 2 - Konvergenz einer Reihe und Konvergenzkriterien",
                r"""
                1. Untersuchen Sie die vier Reihen in der Grafik auf Konvergenz.
                   Variieren Sie dazu auch die Anzahl der angezeigten Glieder.
                2. Stellen Sie begründete Vermutungen auf, welche der Reihen
                   konvergent ist, und welche nicht.
                3. Welchen Einfluss hat eine Änderung des Parameters $a$ auf das
                   Konvergenzverhalten?
                4. Können die vier Reihen überhaupt konvergent sein? Wie lässt
                   sich das ggf. in Abhängigkeit vom Parameter $a$ entscheiden?
                5. Kommentieren Sie die Aussage: Wenn die Reihe eine Nullfolge
                   enthält, ist sie konvergent.
                6. Wieso führt uns eine konvergente Majorante zu einer
                    konvergenten Reihe, warum eine divergente Minorante zu einer
                    divergenten Reihe?
                7. Kann eine divergente Majorante bzw. eine konvergente
                    Minorante zu einer Aussage über die Konvergenz einer Reihe
                    führen? Warum? Warum nicht?
                8. Nutzen Sie das Vergleichskriterium, um Ihre Vermutungen über
                    die Konvergenz der vier Reihen zu überprüfen. Versuchen Sie,
                    jeweils eine konvergente Majorante oder divergente Minorante
                    anzulegen.
                9. Interpretieren Sie Ihre Beobachtungen. Was bedeuten sie für
                   die Konvergenz der Reihen?
                10. Ist Ihre eigene Reihe konvergent? Was vermuten Sie anhand
                    Ihrer Skizzen aus Teil 1?
                11. Wie können Sie überprüfen, ob eine Konvergenz Ihrer Reihe
                    überhaupt möglich ist?
                12. Finden Sie zu Ihrer eigenen Reihe eine konvergente Majorante
                    oder eine divergente Minorante.
                """
            ),
            (
                "Teil 3 - Quotienten- und Wurzelkriterium",
                r"""
                1. Geben Sie das Quotientenkriterium in Ihren Worten wieder.
                    Erläutern Sie, warum es eine Aussage über die Konvergenz
                    einer Reihe machen kann. Warum untersucht es genau den
                    Quotienten $\displaystyle
                    \biggl|\frac{a_{n+1}}{a_n}\biggr|$?
                2. Warum sagt man, dass das Wurzelkriterium eine stärkere
                   Aussage als das Quotientenkrieterium liefert?
                3. Wenden Sie das Quotientenkriterium auf die vier Reihen in der
                   Grafik an.
                4. Notieren Sie dazu jeweils den Quotienten $\displaystyle
                    \biggl|\frac{a_{n+1}}{a_n}\biggr|$, und vereinfachen diesen
                    so weit wie möglich.
                5. Suchen Sie nach dem größten Häufungspunkt der so entstandenen
                    Folge. Welche Aussage können sie daraus über die Konvergenz
                    der zugehörigen Reihe treffen?
                6. Was fällt Ihnen bei den unterschiedlichen Reihen auf?
                7. Wenden Sie das Wurzelkriterium auf die vier Reihen in der
                   Grafik an. Was fällt Ihnen hier auf?
                8. Können Sie auch Ihre eigene Reihe mit den beiden Kriterien
                   auf Konvergenz untersuchen? Welche Aussage können Sie jeweils
                   treffen?
                """
            )
        ]
    }
}

if __name__ == "__main__":
    sums()