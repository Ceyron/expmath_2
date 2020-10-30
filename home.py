import streamlit as st

def home():
    st.image("figs/altbau.jpg", use_column_width=True)
    st.title("Welcome to next Gen Expmath")

    st.write("Wähle ein Modul aus der Option links")

    st.markdown(r"""
        Dies ist ExpMath ("explore mathematics"), ein sich in der Entwicklung
        befindenes Tool für interaktive Einblicke in die Inhalte der Vorlesungen
        Ingenieurmathematik A, B und V an der TU Braunschweig.

        Mit den Reitern in der Navigationsleiste kann auf die Bereiche und die
        dazugehörigen Themen zugegriffen werden. Zu jedem Lerninhalt gibt es
        eine Zusammenfassung der Inhalte sowie eine interaktive Graphik, welche
        am besten mit den darunter liegenden Fragen erkundet werden kann.

        ## Wie nutze ich die interaktiven Plots?

        Die meisten Plots bieten dir links ein Diagramm, welches mit Widgets auf
        der rechten Seite manipuliert werden kann. Dabei besteht oft die Auswahl
        abhängig vom Kontext des Moduls verschiedene
        Folgen/Funktionen/Differentialgleichungen zu betrachten. Mithilfe von
        Slidern werden deren Parameter angepasst.

        Zusätzlich zum eigentlichen Plot sind auf der Seite zu jedem Modul auch
        eine kurze Zusammenfassung zu finden sowie Fragen, mit deren Hilfe man
        die Fähigkeiten des Plots austesten kann.

        ## Wichtig

        Viele Plots sind komplexe Webapplikationen, welche aktuell noch
        (abhängig von deiner Internetgeschwindigkeit) mehrere Sekunden laden
        können. Dabei wird zuerst der statische Inhalt geladen und danach wird
        zwischen den Block zu Zusammenfassungen und Fragen der Plot auftauchen.

        Im aktuellen Testbetrieb kann es zudem noch zu Verzögerungen kommen,
        dadurch könnten sich manche Plots auch weniger interaktiv anfühlen und
        Reaktionen sind verzögert.
    """)

def analysis_1():
    st.title("Analysis 1")

    st.write("Übersichtsseite zu Analysis 1")

def linear_algebra():
    st.title("Lineare Algebra")

    st.write("Übersichtsseite")

def analysis_2():
    st.title("Analysis 2")

    st.write("Übersichtsseite")

def ode():
    st.title("Gewöhnliche Differentialgleichungen")

    st.write("Übersichtsseite")

def analysis_1():
    st.title("Analysis 1")

    st.write("Übersichtsseite zu Analysis 1")