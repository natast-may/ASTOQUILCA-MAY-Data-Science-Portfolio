import streamlit as st

st.title("Hello, streamlit!")
st.markdown("# Hello, streamlit!")
st.write("This is my first streamlit app.")
if st.button("Click me!"):
    st.write ("you clicked the button!")
else: 
    st.write("click the button, and see what happens...")

### loading our csv file
import pandas as pd

st.header("Exploring Our Dataset")

# load the CSV file
df = pd.read_csv("data/sample_data-1.csv")
st.write("Here's our data!")
st.dataframe(df)

city = st.selectbox("Select a city", df["City"].unique())
filtered_df = df[df["City"] == city]

st.write(f"people in {city}")
st.dataframe(filtered_df)
st.bar_chart(df["Salary"])

import seaborn as sns

box_plot = sns.boxplot(x = df["City"], y = df["Salary"])
st.pyplot(box_plot.get_figure())

