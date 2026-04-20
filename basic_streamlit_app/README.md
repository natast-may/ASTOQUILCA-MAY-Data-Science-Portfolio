# Basic Streamlit App

## Project Overview:
This project is a simple Streamlit application that allows the user to explore Kaggle's [Spotify tracks dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset). This dataset includes a range of 125+ genres. 

I built this dashboard to explore patterns between loudness, danceability, and energy impact song popularity.

## Features:
- Data set exploration
- Summary statistics
- Interactive filters
- Key variables include:
    - **popularity:** an algorithm-calculated value from 1-100 that describes how popular a track is. The popularity is largely calculated by number of recent plays.
    - **danceability:** a value from 0.0 - 1.0 that describes how suitable a track is for danging based on tempo, beat strength, etc.
    - **energy:** a value from 0.0 - 1.0 that describes the perceptual measure of intensity and activity.
    - **loudness:** the overall loudness in decibels.
    - **valence:** a value from 0.0 - 1.0 describing how positive a track feels. Tracks with a high valence sound more positive, and vice versa.

## Installation Instructions:
install the required libraries:
- bash
- pip install streamlit pandas
  
from your project folder, run:
`streamlit run basic_streamlit_app.py`

## References and Further Reading:
Maharshi Pandya. (2022). 🎹 Spotify Tracks Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/4372070
