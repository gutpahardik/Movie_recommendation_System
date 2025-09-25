# Movie Recommender System 🎬

This is a Streamlit web app that uses a pre-computed similarity matrix and TMDb API
to recommend 5 movies similar to a user’s choice, showing both titles and posters.

## Problem Statement
This app recommends similar movies to a user-selected movie using content-based filtering.

## Tech Stack
- Python (Pandas, Pickle, Requests)
- Streamlit for Web UI
- TMDb API for posters

## Project Workflow
1. Data → Preprocessing → Similarity Matrix → Pickle Save
2. Streamlit UI → User selects a movie
3. Recommend function fetches top 5 similar movies
4. TMDb API fetches posters dynamically

## Future Improvements
- Add collaborative filtering using user ratings
- Deploy on Streamlit Cloud or Heroku
