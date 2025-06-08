import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

names=st.text_input('Enter your name')

age=st.slider("Select your age: ",0,100,25)

options=["Python","Java","C++"]
choice=st.selectbox("Chose your favorite language: ",options)

if names:
    st.write(f"Hello, {names}, your age is {age}, and your language is {choice}.")

data={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    'City':["New York","Los Angeles","Chicago","Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file",type='csv')

if uploaded_file is not None:
    df1=pd.read_csv(uploaded_file)
    st.write(df1)