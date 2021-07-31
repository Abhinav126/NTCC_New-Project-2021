from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Python Developer Survey Analysis')

@st.cache
def load_data():
    pd.set_option('display.max_columns',None)
    return pd.read_csv('Data/2020_sharing_data_outside.csv')

@st.cache
def load_ques():
    return pd.read_csv('Data/Python Developers Survey questions_outside.csv')

df = load_data()
ques = load_ques()

def show_plot(func,col):
    data = df[col].value_counts()
    st.markdown(ques[ques.shortname == col]['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(func(None,data.index,data.values))


def multi_col(func,name):
    names = [i for i in df.columns if i.startswith(name)]
    values = [list(df[i].value_counts())[0] for i in names]
    names = [i.split('.')[-1] for i in names]
    st.markdown(ques[ques.shortname == name]['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(func(None, names, values))

def page0():

   


def page1():
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
    fig.show()   

    

def page2():
    st.title('Question and plots')
    st.write('')
    show_plot(px.pie,'is.python.main')
    multi_col(px.bar,'other.lang')
    show_plot(px.pie,'main.purposes')
    multi_col(px.pie,'other.purposes')
    multi_col(px.bar,'cloud.platform')
    multi_col(px.pie,'run.in.cloud')
    multi_col(px.bar,'develop.for.cloud')
    multi_col(px.pie,'devenv.os')
    multi_col(px.bar,'orm')
    multi_col(px.bar,'database')
    show_plot(px.pie,'ide.main')
    multi_col(px.bar,'ide.editor')
    multi_col(px.bar,'web.frameworks')
    multi_col(px.bar,'data.frameworks')
    multi_col(px.bar,'other.frameworks')

def page3():
    st.header('Country wise number of respondents')
    data = df['country.live'].value_counts()
    st.markdown(ques[ques.shortname == 'country.live']['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(px.scatter(None,data.index,data.values,data.index,size=data.values))
    show_plot(px.bar,'age')

def page4():
    st.title('About this Analysis')

pages = {
    'Introduction' : page0,
    'Raw Data Format' : page1,
    'Survey results' : page2,
    'About responders' : page3,
    'About project' : page4,
    }

page = st.sidebar.radio('Select a page',list(pages.keys()))

pages[page]()


