import pickle
import pandas as pd
import streamlit as st

movies = pickle.load(open('movie.pkl', mode='rb'))
data = pd.DataFrame(movies)
similarity = pd.DataFrame(pickle.load(open('similarities.pkl', mode='rb')))


def recommend(movie):
    
    recommended_movies = []

    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies


# Streamlit Web App

st.title('Movie Recommendation System :clapper:')
selected_movie = st.selectbox("Select a movie to get recommendations:", list(data['title'].values))
btn = st.button('Recommend')

if btn:
    recommended_movie_list = recommend(selected_movie)

    for i in recommended_movie_list:
        st.write(i)