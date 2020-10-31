import streamlit as st

def home():
    st.image("figs/altbau.jpg", use_column_width=True)
    st.title("Herzlich Willkommen")

    st.markdown(r"""
        Dies ist ExpMath ("explore mathematics"), ein sich in der Entwicklung
        befindenes Tool für interaktive Einblicke in die Inhalte der Vorlesungen
        Ingenieurmathematik A, B und V an der TU Braunschweig.

        ** In der Seitenleiste links kannst du aus den verfügbaren Anwendungen
        ausählen**

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

def home_eng():
    st.image("figs/altbau.jpg", use_column_width=True)
    st.title("Welcome to next Gen Expmath")

    st.write("Choose an available modul from the sidebar left")


details = {
    "german": home,
    "english": home_eng
}