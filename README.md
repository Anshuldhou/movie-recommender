# 🎬 Movie Recommender System (Content-Based Filtering)

This is a content-based movie recommendation system built using Python, Pandas, Scikit-Learn, and Streamlit. It suggests similar movies based on plot overview, cast, crew, genres, and keywords. The application also fetches movie posters in real-time using the TMDB API.

## 🚀 Features

- Content-based recommendations using similarity scores  
- Clean user interface with Streamlit  
- TMDB API integration to fetch posters  
- Secure API key handling using .env  
- Optimized .gitignore to exclude large .pkl files

## 🗂 Project Structure

movie-recommender/  
│  
├── app.py               # Main Streamlit app  
├── requirements.txt     # Python dependencies  
├── setup.sh             # Setup for hosting (Heroku/Render, etc.)  
├── Procfile             # Process declaration for deployment  
├── .env                 # Stores API Key (not pushed to Git)  
├── .gitignore           # Excludes venv, .env, and pickle files  
└── README.md            # Project documentation

## ⚙️ Installation & Setup

1. Clone the Repository  
git clone https://github.com/Anshuldhou/movie-recommender.git  
cd movie-recommender

2. Create Virtual Environment (Optional but Recommended)  
python -m venv venv  
venv\Scripts\activate       # Windows  
OR  
source venv/bin/activate    # Mac/Linux

3. Install Requirements  
pip install -r requirements.txt

4. Add API Key  
Create a .env file in the root directory and add:  
API_KEY=your_tmdb_api_key_here

5. Run the App  
streamlit run app.py

## 🧠 How It Works

1. Data Processing  
   The system uses movies_dict.pkl (movie data) and similarity.pkl (cosine similarity matrix).

2. Recommendation Logic  
   When the user selects a movie, the app finds the most similar movies using the similarity matrix.

3. Poster Fetching  
   A request is sent to TMDB API using the movie ID to retrieve the poster URL.

4. Display  
   The recommendations appear in columns with movie titles and posters.

## 🛡️ API Key Security

Your .env file is ignored using .gitignore, so your key is safe:

.env  
movies_dict.pkl  
similarity.pkl  
venv/

Use your API key in the app like:

import os  
from dotenv import load_dotenv  
load_dotenv()  
api_key = os.getenv("API_KEY")

## 🌐 Future Improvements

- Add search bar with auto-complete  
- Use TMDB IDs instead of movie titles  
- Improve UI using custom CSS or components  
- Deploy on Render, Vercel, or Hugging Face Spaces

## 🤝 Contributing

Pull requests and suggestions are welcome! If you’d like to improve the UI, add models, or optimize performance, feel free to contribute.

## 📬 Contact

GitHub: https://github.com/Anshuldhou
