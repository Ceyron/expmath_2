"""
General Informtion on this topic
"""

import streamlit as st

def info():
    st.title("Lineare Algebra")

    st.markdown(
        r"""
        Lineare Algebra beschäftigt sich mit Zahlentheore, Vektorräumen und
        Matrizen.
        """
    )

    st.image("https://www.mathe-lerntipps.de/wp-content/uploads/2018/04/1437486549_Beispiel.png", use_column_width=True)

details = {
    "german": {
        "run": info
    }
}