import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/weather.csv',parse_dates=['Date/Time'],dayfirst=True, index_col = "Date/Time")
# st.write(df.head())
# st.write(df.shape)
# st.write(df.describe())
st.sidebar.write(df.columns)

# basic version
# fig,ax = plt.subplots(figsize=(20,5))
# df.plot(x="Date/Time",y="Temp (C)",ax=ax, title="temperature plot for the year")
# st.pyplot(fig)
if st.checkbox("show yearly distribution"):
    fig,ax = plt.subplots(figsize=(20,5))
    df["Temp (C)"].plot(ax=ax, title="temperature plot for the year")
    st.pyplot(fig)

    fig,ax = plt.subplots(figsize=(20,5))
    df["Dew Point Temp (C)"].plot(ax=ax, title="humidity plot for the year")
    st.pyplot(fig)

    fig,ax = plt.subplots(figsize=(20,5))
    df["Wind Spd (km/h)"].plot(ax=ax, title="Wind Speed plot for the year")
    st.pyplot(fig)

weather_count = df['Weather'].value_counts()
st.write(weather_count)

fig,ax = plt.subplots(figsize=(20,5))
weather_count.plot(kind='bar',ax=ax)
st.pyplot(fig)

weather_list = df['Weather'].unique()
choice = st.selectbox("select a weather condition",weather_list)
condition = df['Weather'] == choice
filtered_df = df[condition]
st.write(filtered_df)
fig,ax = plt.subplots(figsize=(10,5))
filtered_df["Temp (C)"].plot(ax=ax, title=f"temperature plot for the {choice} weather",style='g.')
st.pyplot(fig)

st.title("comparing relation")

cols = ['Temp (C)','Dew Point Temp (C)',
        'Rel Hum (%)','Wind Spd (km/h)',
        'Visibility (km)','Stn Press (kPa)']
choices = st.multiselect("select any two columns",cols)
if (len(choices)==2):
    fig,ax = plt.subplots(figsize=(7,7))
    df.plot(kind='scatter',x=choices[0], y=choices[1], ax=ax)
    st.pyplot(fig)