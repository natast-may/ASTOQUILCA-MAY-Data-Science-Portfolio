import streamlit as st
import pandas as pd

df = pd.read_csv("data/dataset.csv")

st.dataframe(df.head())