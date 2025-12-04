import numpy as np 
import pandas as pd
import ast
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Read movies data
movies = pd.read_csv('tmdb_5000_movies.csv')

print("Movies shape:", movies.shape)
print("Movies columns:", movies.columns.tolist())

# Feature selection - using only available columns
movies = movies[['id', 'title', 'overview', 'genres', 'keywords']]

print("After feature selection:")
print(movies.head())
print("Shape:", movies.shape)
print("Null values:\n", movies.isnull().sum())

# Remove rows with null values
movies.dropna(inplace=True)
print("Shape after dropping nulls:", movies.shape)

# Check for duplicates
print("Duplicate values:", movies.duplicated().sum())

# Function to convert JSON string to list of names
def convert(text):
    L = []
    if pd.isna(text) or text == '':
        return L
    try:
        for i in ast.literal_eval(text):
            L.append(i['name'])
    except:
        return L
    return L

# Process genres column
movies['genres'] = movies['genres'].apply(convert)
print("After processing genres column:")
print(movies.head())

# Process keywords column
movies['keywords'] = movies['keywords'].apply(convert)
print("After processing keywords column:")
print(movies.head())

# Process overview column (convert string to list)
movies['overview'] = movies['overview'].apply(lambda x: x.split() if pd.notna(x) else [])

# Remove spaces from tags
def remove_space(L):
    L1 = []
    for i in L:
        if isinstance(i, str):
            L1.append(i.replace(" ", ""))
    return L1

movies['genres'] = movies['genres'].apply(remove_space)
movies['keywords'] = movies['keywords'].apply(remove_space)

# Concatenate all features
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']

# Create new dataframe with required columns
new_data = movies[['id', 'title', 'tags']].copy()

# Convert list to string
new_data['tags'] = new_data['tags'].apply(lambda x: " ".join(x) if isinstance(x, list) else "")

# Convert to lowercase
new_data['tags'] = new_data['tags'].apply(lambda x: x.lower() if isinstance(x, str) else "")

# Stemming
ps = PorterStemmer()
def stems(text):
    if not isinstance(text, str) or text == "":
        return ""
    T = []
    for i in text.split():
        T.append(ps.stem(i))
    return " ".join(T)

new_data['tags'] = new_data['tags'].apply(stems)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new_data['tags']).toarray()
print("Vector shape:", vector.shape)

# Calculate similarity
similarity = cosine_similarity(vector)
print("Similarity matrix shape:", similarity.shape)

# Save pickle files
pickle.dump(new_data, open('list_of_movies.pkl', 'wb'))
pickle.dump(similarity, open('similarities.pkl', 'wb'))

print("\nPickle files generated successfully!")
print("Files created: list_of_movies.pkl, similarities.pkl")

