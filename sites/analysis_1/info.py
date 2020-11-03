"""
General Informtion on this topic
"""

import streamlit as st

def info():
    st.title("Analysis 1")

    st.markdown(
        r"""
        Analysis 1 beschäfigt sich mit Folgen, Reihen, Grenzwerten und
        elementaren Begriffen der eindimensionalen Infinitesimalrechung.
        """
    )

    st.image("https://online-learning.harvard.edu/sites/default/files/styles/social_share/public/course/bigstock-123382757-1280x640.jpg?itok=XpWP1P5J", use_column_width=True)
    
    st.markdown(
    r"""
    Viel Spaß!
    """)

details = {
    "german": {
        "run": info
    }
}
