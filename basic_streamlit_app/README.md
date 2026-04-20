# Basic Streamlit App

## Project Overview:
This project is a simple Streamlit application that allows the user to explore Kaggle's [Spotify tracks dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset). This dataset includes a range of 125+ genres. 

I built this dashboard to explore patterns between loudness, danceability, and energy impact song popularity. The goal is to allow the user to explore how different features relate to one another, revealing high-level patterns. 

## Features:
- Interactive data set exploration
- Summary statistics of key variables (pandas)
- Interactive filters
     - Filter by *genre* (drop-down filter selection)
     - Filter by *artist* (drop-down filter selection)
     - Filter by *popularity* (sliding bar of minimum popularity)
- Key variables include:
    - **popularity:** an algorithm-calculated value from 1-100 that describes how popular a track is. The popularity is largely calculated by number of recent plays.
    - **danceability:** a value from 0.0 - 1.0 that describes how suitable a track is for danging based on tempo, beat strength, etc.
    - **energy:** a value from 0.0 - 1.0 that describes the perceptual measure of intensity and activity.
    - **loudness:** the overall loudness in decibels.
    - **valence:** a value from 0.0 - 1.0 describing how positive a track feels. Tracks with a high valence sound more positive, and vice versa.

## Demo:
<img width="812" height="858" alt="Spotify ss" src="https://github.com/user-attachments/assets/5ca00f66-58ac-4bf5-a49d-0366e308c83a" />

## Installation Instructions:
install the required libraries:
- bash
- pip install streamlit pandas
  
from your project folder, run:
`streamlit run main.py`

## References and Further Reading:
Maharshi Pandya. (2022). 🎹 Spotify Tracks Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/4372070
