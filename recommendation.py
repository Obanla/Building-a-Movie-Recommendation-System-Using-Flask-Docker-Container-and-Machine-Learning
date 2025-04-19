import pandas as pd
import numpy as np
import ast
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

class RecommendationSystem:
    def __init__(self, load_from_pickle=False):
        # Check if pickle files exist to save time on restart
        if load_from_pickle and os.path.exists('movies.pkl') and os.path.exists('similarity.pkl'):
            self.load_model()
        else:
            self.movies = pd.read_csv('tmdb_5000_movies.csv')
            self.credits = pd.read_csv('tmdb_5000_credits.csv')
            self.preprocess_data()
            self.save_model()

    def save_model(self):
        # Save processed data and similarity matrix
        pickle.dump(self.movies, open('movies.pkl', 'wb'))
        pickle.dump(self.similarity, open('similarity.pkl', 'wb'))

    def load_model(self):
        # Load processed data and similarity matrix
        self.movies = pickle.load(open('movies.pkl', 'rb'))
        self.similarity = pickle.load(open('similarity.pkl', 'rb'))

    def preprocess_data(self):
        # Your existing preprocessing code
        self.movies = self.movies.merge(self.credits,on='title')
        self.movies.dropna(thresh=int(self.movies.shape[0]*0.95), axis=1, inplace=True)
        self.movies.dropna(subset=['crew'], inplace=True)
        self.movies = self.movies[['genres', 'id', 'keywords', 'original_language', 'overview', 'release_date', 'runtime', 'title', 'vote_average', 'vote_count', 'cast', 'crew']]

        def convert_keywords(obj):
            L = []
            for i in ast.literal_eval(obj):
                L.append(i['name'])
            return L

        def convert_genres(obj):
            l = []
            for i in ast.literal_eval(obj):
                l.append(i['name'])
            return l

        def extract_cast(obj):
            l = []
            count = 0
            if not isinstance(obj, str):
                return l
            try:
                for i in ast.literal_eval(obj):
                    if count != 3:
                        l.append(i['name'])
                        count += 1
                    else:
                        break
            except Exception as e:
                return l
            return l

        self.movies['keywords'] = self.movies['keywords'].apply(convert_keywords)
        self.movies['genres'] = self.movies['genres'].apply(convert_genres)
        self.movies['cast'] = self.movies['cast'].apply(extract_cast)
        self.movies['crew'] = self.movies['crew'].apply(lambda x: [x] if x is not None else [])
        self.movies['overview'] = self.movies['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])

        self.movies['tags'] = self.movies['overview'] + self.movies['cast'] + self.movies['crew'] + self.movies['keywords'] + self.movies['genres']

        # Stemming
        self.ps = PorterStemmer()

        def stemming(text):
            l = []
            for i in text:
                l.append(self.ps.stem(i))
            return " ".join(l)

        self.movies['tags'] = self.movies['tags'].apply(stemming)

        self.vectorizer = CountVectorizer(max_features=500, stop_words='english')
        self.vectors = self.vectorizer.fit_transform(self.movies['tags']).toarray()

        self.similarity = cosine_similarity(self.vectors)

    def get_recommendations(self, movie_title, num_recommendations=10):
        """Return a list of recommended movies"""
        try:
            movie_index = self.movies[self.movies['title'] == movie_title].index[0]
            distances = sorted(list(enumerate(self.similarity[movie_index])), reverse=True, key=lambda x: x[1])
            recommended_movies = []
            for i in distances[1:num_recommendations+1]:
                recommended_movies.append(self.movies.iloc[i[0]].title)
            return recommended_movies
        except IndexError:
            return []  # Return empty list if movie not found
        
    def get_all_titles(self):
        """Return all movie titles for the dropdown"""
        return self.movies['title'].tolist()