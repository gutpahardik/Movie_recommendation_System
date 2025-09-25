# 🎬 Movie Recommender System

This is a **Streamlit web app** that recommends movies similar to a user-selected movie using a **pre-computed similarity matrix** and **TMDb API** to show both titles and posters

## Problem Statement

This app recommends similar movies to a user-selected movie using **content-based filtering**.

## Tech Stack

* **Python**: Pandas, Pickle, Requests
* **Web UI**: Streamlit
* **API**: TMDb API for movie posters

## Project Workflow

1. **Data Preparation**

   * Load and preprocess movie dataset
   * Compute **similarity matrix**
   * Save the matrix using Pickle

2. **Streamlit UI**

   * User selects a movie
   * `recommend()` function fetches top 5 similar movies
   * TMDb API fetches posters dynamically

## Future Improvements

* Add **collaborative filtering** using user ratings
* Deploy on **Streamlit Cloud** or **Heroku

