import streamlit as st
from sites.site_overview import site_overview
from pathlib import Path
import importlib
from templates.overview import templates_overview

st.set_page_config(
    layout="centered",
    page_title="Expmath",
)

# Change color if necessary
st.markdown(r"""
    <style> body {
    background-color: #ffffff;
    } </style>
""", unsafe_allow_html=True)

site_overview_in_language = site_overview["german"]

topic = st.sidebar.selectbox(
    label="Welches Themengebiet?",
    options=["Home", ] + list(site_overview_in_language["topics"].keys())
)

base_path = Path("sites/")

if topic == "Home":
    from home import home
    home()
else:
    topic_overview = site_overview_in_language["topics"][topic]["overview"]
    topic_overview_in_language = topic_overview["german"]

    app = st.sidebar.selectbox(
        label="Welche Anwendung",
        options=list(topic_overview_in_language["apps"].keys())
    )

    app_details = topic_overview_in_language["apps"][app]["details"]
    app_details_in_language = app_details["german"]
    templates_overview[topic_overview_in_language["apps"][app]["type"]](app_details_in_language)