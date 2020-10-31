import streamlit as st

def regular(app_details):
    st.title(app_details["title"])

    st.markdown(app_details["introduction"])

    st.markdown("---")

    for name, description in app_details["theory"]:
        with st.beta_expander(label=name):
            st.markdown(description)

    st.markdown("---")
    
    app_details["plot"]()

    st.markdown("---")

    for name, description in app_details["questions"]:
        with st.beta_expander(label=name):
            st.markdown(description)