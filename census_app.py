import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
@st.cache()
def load_dataset():
    df=pd.read_csv("adult.csv")
    df.columns=['age','workclass','fnlwgt','education','education-years','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
df=load_dataset()
st.title("Census app")
graph=st.sidebar.multiselect("Select the desired plot type",("pie-chart","countplot","box-plot","area chart","line-chart","correlation heatmap","histogram","bargraph"))
st.set_option('deprecation.showPyplotGlobalUse', False)    
if st.sidebar.checkbox("show raw data"):
    st.subheader("Census Data set")
    st.dataframe(df)      
    st.write(df.shape)
if "pie-chart" in graph:
    st.subheader("Pie-chart")
    plt.pie(df["income"].value_counts(),labels=df["income"].value_counts().index,startangle=45,autopct="%1.2f%%")
    st.pyplot()
if "countplot" in graph:
    st.subheader("countplot")
    col=st.selectbox("Select the catagory",df.columns)
    sns.countplot(df[col])
    st.pyplot()    
if "box-plot" in graph:
    st.subheader("boxplot")
    col=st.selectbox("Select the catagory",('age','education-years','capital-gain','capital-loss','hours-per-week',))
    sns.boxplot(df[col])
    st.pyplot()     
if "line-chart" in graph:
    st.subheader("line chart")
    col=st.selectbox("Select the column",df.columns)
    st.line_chart(df[col])
if "correlation heatmap" in graph:
    st.subheader("correlation heatmap")
    sns.heatmap(df.corr(),annot=True)
    st.pyplot()
if "bargraph" in graph:
    st.subheader("bargraph")
    col=st.selectbox("Select the category",df.columns)
    st.bar_chart(df[col])