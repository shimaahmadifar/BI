import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import io

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
    st.write(""" \nSeyed Sadeqh Elmi Mousavi-D03000009 
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
    
    st.title("Merged Dataset")
    st.dataframe(db.head())
    
    st.title("3.1Basic Information")
    info_df = pd.DataFrame({
    "Column": db.columns,
    "Non-Null Count": db.notnull().sum().values,
    "Data Type": db.dtypes.values
     })
    st.dataframe(info_df)
    
    
    st.title("3.2 Summary Statistics")
    st.dataframe(db.describe())
    
    st.title("3.3 Checking for Missing Values")
    st.dataframe(db.isnull().sum())
    
    st.title("3.4 Correlation Analysis")
    import seaborn as sns
    import matplotlib.pyplot as plt
    st.subheader("Correlation Heatmap of Numeric Features")
    numeric_data = db.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)
    
    st.title("3.5 Bar Plot: Number of New Captures per Label")
    # Subheader for context
    st.subheader("Number of 'New Captures = 1' per Label")
    # Filter only rows where 'New Captures (per Event)' = 1
    new_captures_1 = db[db['New Captures (per Event)'] == 1]
    # Count occurrences per Label
    count_by_label = new_captures_1['Label'].value_counts()
    # Plot in Streamlit
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=count_by_label.index, y=count_by_label.values, palette="viridis", ax=ax)
    # Customize
    ax.set_title("Number of 'New Captures = 1' per Label", fontsize=14)
    ax.set_xlabel("Label", fontsize=12)
    ax.set_ylabel("Count of New Captures = 1", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)
    # Show plot in Streamlit
    st.pyplot(fig)

    st.title("3.6 Scatter Plot: Avg Temperature vs. Avg Humidity Colored by Captures")
   
    import streamlit as st
    import plotly.express as px
    # Ensure that 'New Captures (per Event)' is of type string for proper categorical mapping
    db['New Captures (per Event)'] = db['New Captures (per Event)'].astype(str)
    # Create the interactive scatter plot
    fig = px.scatter(
        data_frame=db,
        x="Avg Temperature",
        y="Avg Humidity",
        color="New Captures (per Event)",
        symbol="New Captures (per Event)",
        color_discrete_map={"0": "blue", "1": "red"},
        symbol_map={"0": "circle", "1": "square"},
        labels={
            "Avg Temperature": "Average Temperature (°C)",
            "Avg Humidity": "Average Humidity (%)",
            "New Captures (per Event)": "New Captures"
        },
        title="Avg Temp vs. Humidity (Captures=1 as Squares, 0 as Circles)"
    )
    # Display the plot in Streamlit
    st.plotly_chart(fig)
    

    st.title("3.7 Boxplots: Avg Temperature and Humidity by Capture Events")
    # Ensure the capture column is string for plotting consistency
    db['New Captures (per Event)'] = db['New Captures (per Event)'].astype(str)
    # Boxplot for Avg Temperature
    fig1 = px.box(
        db, 
        x="New Captures (per Event)", 
        y="Avg Temperature", 
        color="New Captures (per Event)",
        color_discrete_map={'0': 'lightblue', '1': 'salmon'},
        title="Avg Temperature by Capture Event",
        labels={"New Captures (per Event)": "New Captures", "Avg Temperature": "Avg Temperature (°C)"}
    )
    # Boxplot for Avg Humidity
    fig2 = px.box(
        db, 
        x="New Captures (per Event)", 
        y="Avg Humidity", 
        color="New Captures (per Event)",
        color_discrete_map={'0': 'lightblue', '1': 'salmon'},
        title="Avg Humidity by Capture Event",
        labels={"New Captures (per Event)": "New Captures", "Avg Humidity": "Avg Humidity (%)"}
    )
    # Display side-by-side in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)


    st.title("3.8 Time Series Plot: Trends of Temperature, Humidity, and Captures Over Time")
    import plotly.graph_objects as go
    import pandas as pd
    # Convert Date column to datetime
    db['Date'] = pd.to_datetime(db['Date'])
    # Split out captures = 1
    captures = db[db['New Captures (per Event)'] == 1]
    # Create figure
    fig = go.Figure()
    # Line for temperature
    fig.add_trace(go.Scatter(
        x=db['Date'], y=db['Avg Temperature'],
        mode='lines',
        name='Avg Temp (°C)',
        line=dict(color='red', width=2),
        opacity=0.7
    ))
    # Line for humidity
    fig.add_trace(go.Scatter(
        x=db['Date'], y=db['Avg Humidity'],
        mode='lines',
        name='Avg Humidity (%)',
        line=dict(color='blue', width=2),
        opacity=0.7
    ))
    # Scatter for capture events - Temp
    fig.add_trace(go.Scatter(
        x=captures['Date'], y=captures['Avg Temperature'],
        mode='markers',
        name='Capture Event (Temp)',
        marker=dict(color='black', size=10, symbol='x')
    ))
    # Scatter for capture events - Humidity
    fig.add_trace(go.Scatter(
        x=captures['Date'], y=captures['Avg Humidity'],
        mode='markers',
        name='Capture Event (Humidity)',
        marker=dict(color='green', size=10, symbol='circle')
    ))
    # Layout
    fig.update_layout(
        title="Trends of Temperature, Humidity, and Insect Captures Over Time",
        xaxis_title="Date",
        yaxis_title="Value",
        legend=dict(orientation='h'),
        xaxis=dict(tickangle=45),
        margin=dict(t=60),
        height=600
    )
    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/bi3.png") 


#End of Page 3 EDA-------------------------------------------------------------------------------------------------------------
#Page 4 Classification---------------------------------------------------------------------------------------------------------

if selected == "Classification":
    st.title(f" {selected}")
    
    st.title("4.1 Logistic Regression")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/logr1.png")
    st.write("Accuracy Score: 0.8666666666666667")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/logr2.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/logr3.png")
    
    st.title("4.2 Random Forest")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/RF1.png")
    st.write("Accuracy Score for Random Forest: 0.9")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/RF2.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/RF3.png")
    
    st.title("4.3 XGBoost")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/xgb1.png")
    st.write("Accuracy Score for XGBoost: 0.9")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/xgb2.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/xgb3.png")

    
    st.title("4.4 Decision Tree")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dt1.png")
    st.write("Accuracy Score for Decision Tree: 0.9")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dt2.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/dt3.png")

    
    st.title("4.5 SVM")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/svm1.png")
    st.write("Accuracy Score for SVM: 0.7333333333333333")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/svm2.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/svm3.png")

    
    st.title( "Comparison")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/all.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/all2.png")
    
#End of Page 4--------------------------------------------------------------------------------------------------------------
#Page 5 Time series Analysis----------------------------------------------------------------------------------------------------


if selected == "Time series Analysis":
    st.title(f" {selected}")
    
    st.title("5.1 SARIMAX Forecast ")
    if st.button("Show Explanation & Results"):
        st.subheader("Evaluation Results:")
        st.write("""
                    \n MAE  (Mean Absolute Error): 0.69
                    \n R² Score (Coefficient of Determination): 0.03""")
        st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/sarimax.png")
    
    st.title("5.2 XGBoost Forecast ")
    st.subheader("Evaluation Results:")
    st.write("""
            \n MAE  (Mean Absolute Error): 0.73
            \n R² Score (Coefficient of Determination): 0.39""")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/xgb4.png")
    
    st.title("5.3 ARIMA")
    st.subheader("Evaluation Results:")
    st.write("""
                \n  MAE  (Mean Absolute Error): 0.90
                \n R² Score: -0.16
                    """)
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/arima.png")
    
    st.title("5.4 ETS")
    st.subheader("Evaluation Results:")
    st.write("""
            \n MAE  (Mean Absolute Error): 0.91
            \n R² Score: -0.15      """)
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/ETS.png")
    st.image("https://raw.githubusercontent.com/shimaahmadifar/BI/main/ETS2.png")
    

