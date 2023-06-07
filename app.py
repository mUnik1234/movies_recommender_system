import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ac7035e2668f985dde379e4a1e95d4af&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movies Recommender System")

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    tab1, tab2, tab3, tab4, tab5 = st.beta_columns(5)
    with tab1:
        st.text(names[0])
        st.image(posters[0])

    with tab2:
        st.text(names[1])
        st.image(posters[1])

    with tab3:
        st.text(names[2])
        st.image(posters[2])

    with tab3:
        st.text(names[3])
        st.image(posters[3])

    with tab4:
        st.text(names[4])
        st.image(posters[4])
