import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def fourier_reihen():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/fourier_reihen",
        width=1000,
        height=830
    )

details={
    "german":{
 "title":"Fourier-Reihen",
 "introduction":"Die Fourier-Reihen werden häufig zur Schwingungsanalyse verwendet und gehören daher zum Handwerkszeug von Ingenieurinnen und Ingenieuren.",
 "theory":[
 ("Theorie1",
 r"""
 Hallo
 """),
    ],
 "plot":fourier_reihen,
 "questions":[
  ("Teil 1",
 r"""
 Hallo
 """
 )
 ],
}
}

if __name__ == "__main__": fourier_reihen()
