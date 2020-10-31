import streamlit as st
from sites.site_overview import site_overview
from pathlib import Path
import importlib
from templates.overview import templates_overview
from sites.home import details as home

st.set_page_config(
    layout="centered",
    page_title="Expmath",
    page_icon="figs/icon.ico"
)

# Change color if necessary
st.markdown(r"""
    <style>
    body {
    background-color: #ffffff;
    }

    .sidebar .sidebar-content {
        padding: 1rem 1rem 3rem;
    }
    .reportview-container .main .block-container {
        box-shadow:
            0 2.8px 2.2px rgba(0, 0, 0, 0.034),
            0 6.7px 5.3px rgba(0, 0, 0, 0.048),
            0 12.5px 10px rgba(0, 0, 0, 0.06),
            0 22.3px 17.9px rgba(0, 0, 0, 0.072),
            0 41.8px 33.4px rgba(0, 0, 0, 0.086),
            0 100px 80px rgba(0, 0, 0, 0.12);
        padding: 1rem 2rem 10rem;
    }

    #MainMenu {visibility: hidden;}
    footer {display: none;}

    iframe {
        background-color: white;
    }

    </style>
""", unsafe_allow_html=True)

iframe_scaling = r"""
          zoom: 0.6;
  -moz-transform: scale(0.6);
  -moz-transform-origin: 0 0;
  -o-transform: scale(0.6);
  -o-transform-origin: 0 0;
  -webkit-transform: scale(0.6);
  -webkit-transform-origin: 0 0;
"""

site_overview_in_language = site_overview["german"]

st.sidebar.title("Expmath")
st.sidebar.markdown("Exploratory Mathematics")

st.sidebar.markdown("---")

language_key = st.sidebar.radio(
    label="Sprachauswahl",
    options=("Deutsch", "English")
)

language={
    "Deutsch": "german",
    "English": "english"
}[language_key]

st.sidebar.subheader("Themengebiet")
topic = st.sidebar.radio(
    label="",
    options=["Home", ] + list(site_overview_in_language["topics"].keys())
)

base_path = Path("sites/")

if topic == "Home":
    home[language]()
else:
    topic_overview = site_overview_in_language["topics"][topic]["overview"]
    topic_overview_in_language = topic_overview["german"]

    app = st.sidebar.radio(
        label="",
        options=list(topic_overview_in_language["apps"].keys())
    )

    app_details = topic_overview_in_language["apps"][app]["details"]
    app_details_in_language = app_details["german"]
    templates_overview[topic_overview_in_language["apps"][app]["type"]](app_details_in_language)

st.sidebar.markdown("---")

st.sidebar.markdown(
    r"<a href=https://github.com/Ceyron/expmath_2> <img src=https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png width=40%></a>",
    unsafe_allow_html=True
)
st.sidebar.markdown(
    r"<a href=https://www.tu-braunschweig.de/ipde> <img src=https://www.tu-braunschweig.de/typo3conf/ext/tu_braunschweig/Resources/Public/Images/Logos/tu_braunschweig_logo.svg width=40%></a>",

    unsafe_allow_html=True
)