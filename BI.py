import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Home","Loading Dataset","Data Preprocessing", "Data Analyse", "Classification", "Time series Analysis"],

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
    st.write("**Insects Analysis and Prediction Using Weather Data and Time series**")
    st.write("Seyed Sadeqh Elmi Mousavi-D03000009 \n Zahra JafarNejad-D03000083 \n Shima Ahmadifar-D03000079 \n")


#page l
if selected == "Loading Dataset":
    st.title(f"{selected}")
    if st.button("Load Data"):
        st.write('Data Loaded Successfully')
    st.title("Review Datasets")
    st.write("**1. Introduction**
              The purpose of this project was to systematically clean, transform, and prepare two datasets:Meteorological data (df): Includes temperature and humidity measurements.")
    st.dataframe(df1.head())  # head() by default shows first 5 rows
    st.write(" Entomological data (db): Includes insect capture events and cleaning events.")
    st.dataframe(db1.head())
    st.title("Merge Datasets")
    st.dataframe(db.head())
    
#End of page 1----------------------------------------------------

#page 2--------------------------------------------------------------

if selected == "Data Preprocessing":
    st.title(f"{selected}")
    st.write("2.1. Dropping the First Row"
              "The first row contained redundant header information that was not part of the actual measurements.")
    st.dataframe(df1.head())
    st.write("2.2. Adding Location Labels \n
              Each dataset was assigned a unique label indicating its source location: \n
              2.3. Separating Date and Time" \n
              A custom function separate_datetime() was applied to each DataFrame \n
              2.4. Merging Datasets \n
              All individual datasets were merged into a single DataFrame \n
              2.5. Renaming Columns \n
              To make column names descriptive and self-explanatory Some columns were renamed to improve clarity: \n
              'Temperatura Intervallo' was renamed to 'Temperatura Intervallo Low'. \n
              'Unnamed: 3' (an automatically generated name) was renamed to 'Temperatura Intervallo High' \n
               2.6. Dropping Unnecessary Columns \n
               Since the focus of analysis was on daily measurements, detailed time information was no longer necessary,The **Time** column was dropped.") \n
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/bi1.png")          
            






#End of page2              
if selected == "Data Analyse":
    st.title(f" {selected}")
if selected == "Classification":
    st.title(f" {selected}")
if selected == "Time series Analysis":
    st.title(f" {selected}")

