import streamlit as st
pip install streamlit-option-menu
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Data Preprocessing", "Data Analyse", "Modeling"],

    )
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Data Preprocessing":
    st.title(f"You have selected {selected}")
if selected == "Data Analyse":
    st.title(f"You have selected {selected}")
if selected == "Modeling":
    st.title(f"You have selected {selected}")
