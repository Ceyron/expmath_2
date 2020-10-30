"""
General Informtion on this topic
"""

import streamlit as st

def info():
    st.title("Partielle Differentialgleichungen")

    st.markdown(
        r"""
        Partielle Differentialgleichungen sind elementare Werkzeuge zur
        Modellierung von Naturphänomenen in Biologie, Mechanik und
        Elektrodynamik
        """
    )

    st.image("https://steemitimages.com/DQmR1QGXuufM9qxzAq3HCj58bypefGdXCu8d4tg4iWBmokW/ql_cabab8b787814b85ffa0071d15a3f2bf_l3.jpg", use_column_width=True)

details = {
    "german": {
        "run": info
    }
}