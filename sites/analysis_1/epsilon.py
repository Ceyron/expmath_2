import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def epsilon():
    functions = {
        "Folge 1": lambda x: 1/x,
        "Folge 2": lambda x: np.sqrt(x),
        "Folde 3": lambda x: np.sin(x),
    }

    col_1, col_2 = st.beta_columns((1, 1))

    sequence_id = col_1.radio(
        label="Welche Folge",
        options=list(functions.keys())
    )
    n_points = col_1.slider(
        label="Anzahl der Folgenelemente",
        min_value=5,
        max_value=50,
        value=10,
        step=1
    )
    convergence_or_boundedness = col_2.radio(
        label="Welcher Modus?",
        options=("Konvergenz", "Beschränktheit")
    )

    if convergence_or_boundedness == "Konvergenz":
        limit = col_2.slider(
            label=r"Grenzwert",
            min_value=-2.0,
            max_value=3.0,
            value=1.0,
            step=0.05,
        )
        epsilon = col_2.slider(
            label=r"Schlauchweite",
            min_value=-2.0,
            max_value=3.0,
            value=1.0,
            step=0.05,
        )
        lower = limit - epsilon
        upper = limit + epsilon
    else:
        upper = col_2.slider(
            label=r"Obere Grenze",
            min_value=-2.0,
            max_value=3.0,
            value=1.0,
            step=0.05
        )
        lower = col_2.slider(
            label=r"Untere Grenze",
            min_value=-2.0,
            max_value=3.0,
            value=0.5,
            step=0.05
        )

    # Create the points that are displayes
    x = np.arange(1, n_points, 1)
    y = functions[sequence_id](x)
    is_inside = np.equal(np.greater(y, lower), np.greater(upper, y))

    # Create the horizontal lines
    endpoints = np.array([0, 50])
    upper_line = np.array([upper, upper])
    lower_line = np.array([lower, lower])


    # Display the points as scatter points
    fig = px.scatter(
        x=x,
        y=y,
        color=is_inside
    )
    fig.add_trace(go.Scatter(
        x=endpoints,
        y=upper_line,
        mode="lines",
        line_color="black",
        fill=None
    ))
    fig.add_trace(go.Scatter(
        x=endpoints,
        y=lower_line,
        mode="lines",
        line_color="black",
        fill="tonexty",
        fillcolor="rgba(255, 212, 96, 0.2)",
    ))

    fig.update_layout(
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        ),
        yaxis_range=(-2, 3),
        xaxis_title=None,
        yaxis_title=None,
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

details = {
    "german": {
        "title": "Folgen, Grenzwerte und das Epsilonkriterium",
        "introduction":
            """
            Hier könnte eine nette Einleitung stehen mit möglicher
            **Formatierung** oder einem Smiley 🤫.
            """,
        "theory": [
            (
                "Defintion einer Folge",
                r"""
                Eine Folge $\left ( a_n \right )_{n=0}^\infty: \mathbb{N} \to
                    \mathbb{R}$ ist eine Zuordnung einer natürlichen Zahl $n \in
                    \mathbb{N}$ auf eine reelle Zahl $a_n \in \mathbb{R}$
                    vermöge $n \mapsto a_n$.

                Die Zahl $a_n$ ist ein Folgenglied, also ein Element der Folge.
                """
            ),
            (
                "Monotonie von Folgen",
                r"""
                Eine Folge $\left ( a_n \right )_{n=0}^\infty$ heißt monoton
                wachsend, wenn $a_{n+1} \geq a_n$ für alle $n \in \mathbb{N}$
                gilt. Sie heißt streng monoton wachsend, wenn sogar $a_{n+1} >
                a_n$ für alle $n \in \mathbb{N}$ gilt. 

                Analog heißt eine Folge $\left ( a_n \right )_{n=0}^\infty$
                    monoton fallend, wenn $a_{n+1} \leq a_n$ für alle $n \in
                    \mathbb{N}$ gilt und streng monoton fallend, wenn $a_{n+1} <
                    a_n$ für alle $n \in \mathbb{N}$ gilt.
                """
            ),
            (
                "Beschränktheit von Folgen",
                r"""
                Eine Folge $\left ( a_n \right )_{n=0}^\infty$ ist nach oben
                    beschränkt, wenn es eine obere Schranke $s \in \mathbb{R}$
                    gibt, sodass $a_n \leq s$ für alle $n \in \mathbb{N}$ gilt.

                Eine Folge $\left ( a_n \right )_{n=0}^\infty$ ist nach unten
                    beschränkt, wenn es eine untere Schranke $u \in \mathbb{R}$
                    gibt, sodass $a_n \geq u$ für alle $n \in \mathbb{N}$ gilt.

                Eine Folge $\left ( a_n \right )_{n=0}^\infty$ ist beschränkt,
                wenn es eine obere und eine untere Schranke gibt.
                """
            ),
            (
                "Konvergenz",
                r"""
                Eine Folge $\left ( a_n \right )_{n=0}^\infty$ hat einen
                Grenzwert $a \in \mathbb{R}$, wenn

                $\forall \varepsilon >0 \, \exists N  \, : \, \lvert a_n - a
                \rvert < \varepsilon \, \forall n \geq N$

                gilt. 

                Wenn ein Grenzwert für eine Folge existiert, schreiben wir
                    $\displaystyle \lim_{n \to \infty} a_n =a$ oder kurz $a_n
                    \rightarrow a$. Die Folge konvergiert gegen den Grenzwert
                    $a$. Wenn dieser Grenzwert $a=0$ ist, so heißt die Folge
                    Nullfolge. Eine Folge, die nicht konvergiert, heißt
                    divergente Folge.
                """
            ),
        ],
        "plot": epsilon,
        "questions": [
            (
                "(1) Was ist eine Folge?",
                r"""
                1. Was unterscheidet eine Folge von einer Funktion $f:
                   \mathbb{R} \rightarrow \mathbb{R}$?
                2. Wie erkennt man dies graphisch?
                3. Warum ist es falsch, eine durchgezogene Linie anstelle von
                   einzelnen Punkten zu zeichnen?
                4. Bestimmen Sie die Zuordnungsvorschrift für eine der Folgen.
                    Prüfen Sie Ihre Vermutung durch eine Beispielrechnung und
                    eine graphische Überprüfung.
                5. Geben Sie für einzelne Folgenglieder die Abbildung von
                   $\mathbb{N}$ nach $\mathbb{R}$ an.
                6. Welcher Wert $a_1$ wird $n=1$ zugeordnet? Welcher Wert $a_2$
                    wird $n=2$ zugeordnet? Versuchen Sie eine Regelmäßigkeit für
                    höhere Werte von $n$ zu finden.
                """
            ),
            (
                "(2) Monotonie",
                r"""
                1. Skizzieren Sie jeweils eine
                    * monoton, aber nicht streng monoton, wachsende Folge.
                    * monoton, aber nicht streng monoton, fallende Folge.
                    * eine streng monoton wachsende Folge.
                    * eine Folge, die weder monoton wächst noch monoton fällt.
                2. Geben Sie die Monotonie-Eigenschaften der Folgen in der
                   Grafik an.
                3. Weisen Sie die vermutete Monotonie-Eigenschaft nach. Nutzen
                   Sie hierzu Ihre Ergebnisse aus Teil 1.
                4. Geben Sie einen allgemeinen Ausdruck für $a_{n+1}$ an, indem
                    Sie in die Zuordnungsvorschrift statt $n$ den Wert $n+1$
                    einsetzen. Formen Sie die entstandene Gleichung nun um. 
                5. Warum hat die Definition der Monotonie den Zusatz "für alle
                   $n \in \mathbb{N}$"?
                6. Was wäre, wenn die Definition z.B. für $n=5$ nicht gilt? Wie
                    unterscheidet sich eine solche Folge graphisch von einer,
                    bei der die Bedingung für alle $n \in \mathbb{N}$ gilt?
                """
            ),
            (
                "(3) Beschränktheit",
                r"""
                1. Geben Sie eine sprachliche Beschreibung der Beschränktheit einer
                Folge nach oben an.
                2. Angenommen, für eine Folge $\left ( a_n \right )_{n=0}^\infty$
                    existiert eine obere Schranke $s$. Gibt es dann ein Element $a_n$,
                    das größer ist als $s$?
                3. Angenommen, für eine Folge $\left ( a_n \right )_{n=0}^\infty$
                    existiert eine obere Schranke $s$. Gibt es dann ein Element $a_n$,
                    das gleich $s$ ist?
                4. Skizzieren Sie 
                    * eine nach oben, aber nicht nach unten beschränkte Folge.
                    * eine nach unten, aber nicht nach oben beschränkte Folge.
                    * eine beschränkte Folge.
                5. Überprüfen Sie die Folgen in der Grafik auf Beschränktheit.
                """
            ),
            (
                "(4) Grenzwert und Konvergenz",
                r"""
                1. Geben Sie die Definition für den Grenzwert einer Folge in Ihren
                Worten wieder.
                2. Was bedeuten die Quantoren $\forall$ und $\exists$?
                3. Betrachten Sie die Grafik und versuchen Sie, für jede der
                unterschiedlichen Folgen ihren Grenzwert zu finden.
                4. Raten Sie einen Grenzwert $a$, stellen Sie diesen ein und variieren
                Sie $\varepsilon$. Was beobachten Sie?
                5. Vergrößern Sie die Anzahl an Folgengliedern, die gezeichnet werden.
                    Finden Sie eine natürliche Zahl $N$, sodass alle Folgenglieder ab
                    diesem $N$ innerhalb des Epsilon-Schlauchs liegen?
                6. Kommentieren Sie die folgende Aussage: Wenn nur endlich viele
                    Folgenglieder nicht im Epsilon-Schlauch liegen, konvergiert die
                    Folge trotzdem.
                7. Zeichnen Sie die ersten 10 Folgenglieder von $\left ( b_n \right
                    )_{n=0}^\infty$  mit $b_n=1$ für $\{n \in \mathbb{N} : n= 5^k, k\in
                    \mathbb{N} \} = \{ 5, 25, 125, 600,  \dots \}$ und $b_n =0$ sonst.
                    Gibt es für jedes $\varepsilon >0$ ein $N \in \mathbb{N}$, sodass
                    die Ungleichung $\lvert b_n - b\rvert < \varepsilon$ erfüllt ist?
                8. Bestimmen Sie für die Folge $\left ( a_n \right )_{n=0}^\infty$ mit
                    $a_n= \frac{3}{4} -  \frac{1}{n}$ die Abhängigkeit für $N$ von
                    $\varepsilon$, sodass die Ungleichung $\lvert a_n - a\rvert <
                    \varepsilon$ erfüllt ist. Nutzen Sie Ihre Vermutung für den
                    Grenzwert von $\left ( a_n \right )_{n=0}^\infty$. Interpretieren
                    Sie das Ergebnis.
                9. Notieren Sie die Grenzwertdefinition mit der konkreten
                Zuordnungsvorschrift für $a_n$.
                10. Lösen Sie den Betrag auf.
                11. Stellen Sie die entstandene Gleichung nach N um. 
                11. Welche Folgenglieder liegen demnach im Epsilon-Schlauch?
                12. Aus welchem Zahlenbereich stammt $N$?
                13. Welche Auswirkung hat die Wahl von $N$ auf die Folge?
                """
            ),
        ]
    }
}


if __name__ == "__main__":
    epsilon()