# app.py
# Exploring the Spotify Tracks Dataset App
# Author: Natalie Astoquilca-May
# Date: 2.11.26

import streamlit as st
import pandas as pd

# introduction and context
st.title("🎵 Exploring the Spotify Tracks Dataset 🎵")
st.markdown(
    """
This is my very first Streamlit application. I built this dashboard to explore patterns between liviliness, danceability, and energy, impact song popularity using 
a sampled Spotify dataset. The dataset includes a range of 125+ genres.

Link to dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
"""
)
st.markdown("---")

# load the CSV file and the data
st.header("Let's explore our dataset!")
df = pd.read_csv("data/dataset.csv")

st.write("Below are some **summary statistics** for this dataset. The dataset includes Spotify songs with different genres and their audio features.")
#I only want certain columns to help the app look cleaner
important_columns = [
    "popularity",
    "danceability",
    "energy",
    "loudness",
    "valence"
]

st.write(df[important_columns].describe())

#I want to give context on what these variables measure
st.markdown(
    """
**What do these variables mean?**
- **popularity:** an algorithm-calculated value from 1-100 that describes how popular a track is. The popularity is largely calculated by number of recent plays.
- **danceability:** a value from 0.0 - 1.0 that describes how suitable a track is for danging based on tempo, beat strength, etc.
- **energy:** a value from 0.0 - 1.0 that describes the perceptual measure of intensity and activity.
- **loudness:** the overall loudness in decibels.
- **valence:** a value from 0.0 - 1.0 describing how positive a track feels. Tracks with a high valence sound more positive, and vice versa.
"""
)
st.markdown("---")

## ANALYSIS SECTION:

# Filtering by Genre
st.subheader("♫⋆♪ Filter by Genre ♫⋆♪")
genre_list = df["track_genre"].unique()
chosen_genre = st.selectbox("Choose a genre:", genre_list)

filtered_df = df[df["track_genre"] == chosen_genre]

st.write(f"You selected {chosen_genre}! Here are the top 10 most popular songs in that genre:")
top_10 = filtered_df.sort_values(by = "popularity", ascending = False).head(10)
st.dataframe(top_10[["track_name", "artists", "popularity"]])

# --------------------------------------

# Filtering by Artist
st.subheader("♫⋆♪ Filter by Artist ♫⋆♪")
artist_list = df["artists"].unique()
chosen_artist = st.selectbox("Choose an artist:", artist_list)

filtered_df_2 = df[df["artists"] == chosen_artist]

st.write(f"I love {chosen_artist} too! Here are the top 10 most popular songs by them:")
top_10 = filtered_df_2.sort_values(by = "popularity", ascending = False).head(10)
st.dataframe(top_10[["track_name", "track_genre", "popularity"]])

# --------------------------------------

# Filtering by Popularity
st.subheader("♫⋆♪ Filter by Popularity ♫⋆♪")
min_pop = st.slider("Minimum popularity:", 0, 100, 50)

pop_filtered_df = df[df["popularity"] >= min_pop]

st.write(f"Songs with popularity above {min_pop}")
st.dataframe(pop_filtered_df)
## in the future, would like to learn how to make this filter cleaner

st.markdown("---")
st.markdown(
    """
*Made by: Natalie Astoquilca-May*

*Date: February 11th, 2026*

*Course: Introduction to Data Science, University of Notre Dame*

"""
)
