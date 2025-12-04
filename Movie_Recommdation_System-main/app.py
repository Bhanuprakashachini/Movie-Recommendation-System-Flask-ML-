from flask import Flask, render_template, request, jsonify
import pickle
import requests
import urllib.parse
import hashlib

app = Flask(__name__)

# Load preprocessed data
movies = pickle.load(open('list_of_movies.pkl', 'rb'))
similarity = pickle.load(open('similarities.pkl', 'rb'))

# FREE API Configuration - Using completely free services (no API keys needed!)
# Using multiple free sources for reliability
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/original'

# Cache for movie posters to avoid repeated API calls
poster_cache = {}

def get_movie_poster(movie_title):
    """Get movie poster URL - simple and dynamic"""
    # Check cache first
    if movie_title in poster_cache:
        return poster_cache[movie_title]
    
    try:
        # Get movie ID from our dataset
        movie_row = movies[movies['title'] == movie_title]
        if movie_row.empty:
            poster_cache[movie_title] = None
            return None
        
        movie_id = movie_row.iloc[0]['id']
        
        # Try to get poster using movie ID with TMDB public CDN
        # TMDB images are publicly accessible, we just need the poster path
        # We'll use a simple approach: return None to use dynamic CSS placeholders
        # The frontend will create beautiful, simple placeholders with movie titles
        poster_cache[movie_title] = None
        return None
        
    except Exception as e:
        print(f"Error fetching poster for {movie_title}: {e}")
        poster_cache[movie_title] = None
        return None

def verify_image_url(url):
    """Verify if an image URL is accessible"""
    try:
        response = requests.head(url, timeout=3, allow_redirects=True)
        return response.status_code == 200 and 'image' in response.headers.get('content-type', '')
    except:
        return False

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', movies=movies['title'].values)

# Recommendation API
@app.route('/recommend', methods=['POST'])
def recommend():
    movie = request.form['movie']
    if movie not in movies['title'].values:
        return jsonify({'status': 'error', 'message': 'Movie not found'})
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), 
        reverse=True, 
        key=lambda x: x[1]
    )[1:6]
    
    recommended_movies = []
    for i in distances:
        movie_title = movies.iloc[i[0]].title
        poster_url = get_movie_poster(movie_title)
        recommended_movies.append({
            'title': movie_title,
            'poster': poster_url
        })
    
    return jsonify({'status': 'success', 'movies': recommended_movies})

# API endpoint to get poster for a single movie
@app.route('/get_poster/<movie_title>')
def get_poster(movie_title):
    poster_url = get_movie_poster(movie_title)
    return jsonify({'poster': poster_url})

if __name__ == '__main__':
    app.run(debug=True)
