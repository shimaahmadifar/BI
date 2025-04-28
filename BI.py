import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Home","Data Preprocessing", "Data Analyse", "Modeling"],

    )
if selected == "Home":
    st.title(f"Information Systems & Business Intelligence")
    st.title(f"Professor FLORA AMATO")
    st.write("Insects Analysis and Prediction Using Weather Data and Time series")
    st.write("\n"
             "Seyed Sadeqh Elmi Mousavi-D030000?" "\n" "Negar Jafar Nejad-D030000?" "\n" "Shima Ahmadifar-D030000?" "\n")


if selected == "Data Preprocessing":
    st.title(f"You have selected {selected}")
if selected == "Data Analyse":
    st.title(f"You have selected {selected}")
if selected == "Modeling":
    st.title(f"You have selected {selected}")
