import streamlit as st
import pickle
import pandas as pd
import requests


st.set_page_config(layout="wide")

# Add the custom HTML for the gradient background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white; /* Optional: Change text color to contrast with the background */
        }
    </style>
    """,
    unsafe_allow_html=True
)




def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8f21da0c1e1b6d8ae68f49a6203141fb'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_posters = []
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster using api from
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

font_css = """
<style>
    .custom-font {
        font-family: 'Bangers', cursive;
        font-weight: 800; 
        color: #FFA500;
    }
</style>
"""

# Center-align the title using HTML and CSS
st.markdown("""
    <div style="text-align: center;">
        <h1 class="custom-font">FlixHarbor</h1>
    </div>
    <div style="text-align: center;"> 
        <h3>A Movie Recommendation System</h3>
    </div>
""", unsafe_allow_html=True)


# Apply the custom font style
st.markdown(font_css, unsafe_allow_html=True)




selected_movie_name = st.selectbox('Select or type Movie Name :', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


    st.write("\n\n\n\n\n\n\n\n\n\n\n")
    st.markdown("______________________________________________________________________________")

    st.write("Contributors : Bushra Shaikh, Ayesha Shaikh and Neha Yadav ")

