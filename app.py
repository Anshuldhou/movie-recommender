import streamlit as st  # Streamlit for creating the web UI
import pickle  # To load pre-saved Python objects (models/data)
import pandas as pd  # To handle DataFrame operations
import requests  # To fetch data from APIs
import os  # To access environment variables
from dotenv import load_dotenv  # To load variables from .env file

# Load environment variables from .env file
load_dotenv()

# Read your TMDB API key from the .env file
API_KEY = os.getenv("TMDB_API_KEY")


def fetch_poster(movie_id):
    """Fetch the movie poster using the TMDB API and return its image URL."""

    # Create API URL using the movie_id and your API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)

    # If the API fails, show a placeholder image
    if response.status_code != 200:
        print("API Error:", response.text)
        return "https://via.placeholder.com/500x750?text=No+Image"

    data = response.json()

    # If poster exists, return its URL; otherwise return placeholder
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster+Found"


def recommend(movie):
    """Recommend 5 similar movies and return their names and posters."""

    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Get similarity scores for that movie
    distances = similarity[movie_index]

    # Sort movies based on similarity (top 5 except itself)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    # Loop through the top 5 similar movies
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        # Add movie title and fetch the poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Load movies data (title, id, etc.) from pickle file
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load precomputed similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Title of the Streamlit app
st.title('Movie Recommender System')

# Dropdown menu to select a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations',
    movies['title'].values
)

# On button click, show recommendations
if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)

    # Create 5 columns and display movie name with poster in each
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

# Alternative shorter way (commented):
# col1, col2, col3, col4, col5 = st.columns(5)
# for idx, col in enumerate([col1, col2, col3, col4, col5]):
#     col.text(names[idx])
#     col.image(posters[idx])
