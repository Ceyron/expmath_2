"""
General Informtion on this topic
"""

import streamlit as st

def info():
    st.title("Analysis 3")

    st.markdown(
        r"""
        Analysis 2 beschäfigt sich mit Vektoranalysis sowie den Integralsätzen
        von Gauß und Stokes.
        """
    )

    st.image("https://miro.medium.com/max/672/1*db0LuwdYFFVEqHh0coMbsA.jpeg", use_column_width=True)

details = {
    "german": {
        "run": info
    }
}