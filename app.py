import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


st.title("Movie Recommendation System")
option = st.selectbox("Enter the name of a movie",movies['title'].values)
