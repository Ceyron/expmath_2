"""
General Informtion on this topic
"""

import streamlit as st

def info():
    st.title("Analysis 2")

    st.markdown(
        r"""
        Analysis 2 beschäfigt sich mit multi-variater Infinitesimalrechnung
        sowie Laplace und Fourier-Transformationen.
        """
    )

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Paraboloid_of_Revolution.svg/1200px-Paraboloid_of_Revolution.svg.png", use_column_width=True)

details = {
    "german": {
        "run": info
    }
}