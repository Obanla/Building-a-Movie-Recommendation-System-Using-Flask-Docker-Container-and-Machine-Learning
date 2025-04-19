import pickle
import pandas as pd
from flask import Flask, render_template, request

# Load pickled model and similarity matrix
with open('model.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = []
    selected_movie = None  # Initialize selected_movie variable

    if request.method == 'POST':
        selected_movie = request.form.get('movie_title')
        if selected_movie in movies['title'].values:
            idx = movies[movies['title'] == selected_movie].index[0]
            distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
            recommendation = [movies.iloc[i[0]].title for i in distances[1:11]]

    # Pass all titles for the dropdown and the selected movie
    return render_template('index.html',
                           titles=movies['title'].values,
                           recommendation=recommendation,
                           selected_movie=selected_movie)  # Pass selected movie to template


if __name__ == '__main__':
    app.run(debug=True)