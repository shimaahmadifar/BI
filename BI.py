import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Home","Loading Dataset","Data Preprocessing", "Data Analyse", "Modeling"],

    )

df1 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dati-meteo-storici%20(Cicalino%201).csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dati-meteo-storici%20(Cicalino%202).csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dati-meteo-storici%20(Imola%201).csv")
df4 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dati-meteo-storici%20(Imola%202).csv")
df5 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dati-meteo-storici%20(Imola%203).csv")
db1 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/grafico-delle-catture%20(Cicalino%201).csv")
db2 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/grafico-delle-catture%20(Cicalino%202).csv")
db3 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/grafico-delle-catture%20(Imola%201).csv")
db4 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/grafico-delle-catture%20(Imola%202).csv")
db5 = pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/grafico-delle-catture%20(Imola%203).csv")
db= pd.read_csv("https://raw.githubusercontent.com/shimaahmadifar/BI/main/data.csv")


if selected == "Home":
    st.title(f"Information Systems & Business Intelligence")
    st.title(f"Professor FLORA AMATO")
    st.write("Insects Analysis and Prediction Using Weather Data and Time series")
    st.write("\n"
             "Seyed Sadeqh Elmi Mousavi-D030000?" "\n" "Negar Jafar Nejad-D030000?" "\n" "Shima Ahmadifar-D030000?" "\n")



if selected == "Loading Dataset":
    st.title(f"{selected}")
    if st.button("Load Data"):
        st.write("Data Loaded Successfully")
    st.title("Review Datasets")
    st.write("### First Rows of DataFrame:")
    st.dataframe(df1.head())  # head() by default shows first 5 rows

    st.title("Merge Datasets")
    st.dataframe(db.head())


if selected == "Data Preprocessing":
    st.title(f"{selected}")
    st.write("2.1. Dropping the First Row"
              "The first row likely contained redundant header information or invalid data that was not part of the actual measurements."
             "2.2. Adding Location Labels"
              "Each dataset was assigned a unique label indicating its source location:"
              "2.3. Separating Date and Time"
              "A custom function separate_datetime() was applied to each DataFrame:"
              "2.5. Renaming Columns"
              "Some columns were renamed to improve clarity:"
              "'Temperatura Intervallo' was renamed to 'Temperatura Intervallo Low'. 'Unnamed: 3' (an automatically generated name) was renamed to 'Temperatura Intervallo High'.Purpose: To make column names descriptive and self-explanatory."
               "2.6. Dropping Unnecessary Columns"
               "Since the focus of analysis was on daily measurements, detailed time information was no longer necessary,The Time column was dropped.")
               
            






             
if selected == "Data Analyse":
    st.title(f" {selected}")
if selected == "Modeling":
    st.title(f" {selected}")
