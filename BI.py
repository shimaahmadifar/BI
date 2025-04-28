import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title="Home",
        options=["Home","Loading Dataset","Data Preprocessing", "Exploratory Data Analysis", "Classification", "Time series Analysis"],

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
    st.write(""" \nSeyed Sadeqh Elmi Mousavi D03000009 
                 \nZahra JafarNejad-D03000083 
                 \nShima Ahmadifar-D03000079""")


#page l  Loading Dataset----------------------------------------------------------------------------------------
if selected == "Loading Dataset":
    st.title(f"{selected}")
    if st.button("Load Data"):
        st.write('Data Loaded Successfully')
    st.title("Review Datasets")
    st.write(""" This project contains two datasets: 
                                                            \n Meteorological data : Includes temperature and humidity measurements.""")
    st.dataframe(df1.head())  # head() by default shows first 5 rows
    st.write(" Entomological data : Includes insect capture events and cleaning events.")
    st.dataframe(db1.head())
    st.title("Merge Datasets")
    st.dataframe(db.head())
    
#End of page 1  Loading Dataset---------------------------------------------------------------------------------

#page 2 Data Preprocessing--------------------------------------------------------------------------------------------------------

if selected == "Data Preprocessing":
    st.title(f"{selected}")
    st.write("2.1. Dropping the First Row"
              "The first row contained redundant header information that was not part of the actual measurements.")
    st.dataframe(df1.head())
    st.write("""
              \n 2.2. Adding Location Labels \n
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
               Since the focus of analysis was on daily measurements, detailed time information was no longer necessary,The **Time** column was dropped.""")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/bi1.png")          
    st.write(""" \n2.7 Grouping by Date: Data was grouped by the Date column, and the following operations were performed:
                  \nFor numeric columns, the mean value was calculated for each day.
                 \nFor Label, the first occurrence was taken, assuming that all data for a given date belongs to the same location.
                 \n2.8 Correcting Number Formatting: Some numeric values used commas (,) instead of dots (.) as decimal separators.
                                                   \nReplace commas with dots.
                                                   \nConvert the corrected text into numeric types.
                 \n2.9: Renaming Columns for Clarity:
                                                   \n"Media Temperatura" to: "Avg Temperature",
                                                   \n"Temperatura Intervallo" to: "Temperature Low",
                                                   \n"Unnamed: 3" to: "Temperature High",
                                                   \n"Media Umidità" to: "Avg Humidity"     """)
       
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/bi2.png")
    st.write(""" 
                \n 2.10 Calculating Daily Statistics: Grouped our data by: Label (location) and Date. and calculated: 
                                                                       \n Mean of average temperature (Avg Temperature).
                                                                        \nMinimum of temperature low (Min Temperature).
                                                                       \n Maximum of temperature high (Max Temperature).
                                                                        \nMean of average humidity (Avg Humidity).
                                                                       \n To Summarize measurements at a daily level per location
                    \n2.11 Dropping Unnecessary Columns
                    \n2.12 Dropping Irrelevant Columns
                    \n2.13 Changing and Renaming Insect Capture Columns
                    \n2.14 Handling Missing Values
                    \n2.15 Merging Datasets
                    \n2.16 Preparing the Target Variable
            

                 """)







#End of page2 Data Preprocessing------------------------------------------------------------------------------------------------
#Page 3 EDA---------------------------------------------------------------------------------------------------------------------


if selected == "Exploratory Data Analysis":
    st.title(f" {selected}")


#End of Page 3 EDA-------------------------------------------------------------------------------------------------------------
#Page 4 Classification---------------------------------------------------------------------------------------------------------

if selected == "Classification":
    st.title(f" {selected}")
    
#End of Page 4--------------------------------------------------------------------------------------------------------------
#Page 5 Time series Analysis----------------------------------------------------------------------------------------------------


if selected == "Time series Analysis":
    st.title(f" {selected}")

