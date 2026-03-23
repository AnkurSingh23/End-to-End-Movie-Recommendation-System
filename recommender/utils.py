# recommender/utils.py

import pickle
import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

movies = pickle.load(open(os.path.join(BASE_DIR, 'artifacts/movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'artifacts/similarity.pkl'), 'rb'))

# Optional
try:
    knn = pickle.load(open(os.path.join(BASE_DIR, 'artifacts/knn.pkl'), 'rb'))
    vectors = pickle.load(open(os.path.join(BASE_DIR, 'artifacts/vectors.pkl'), 'rb'))
except:
    knn = None
    vectors = None


def recommend_cosine(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]

        movies_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        return [movies.iloc[i[0]].title for i in movies_list]

    except:
        return ["Movie not found"]


def recommend_knn(movie):
    if knn is None or vectors is None:
        return ["KNN model not available"]

    try:
        movie_index = movies[movies['title'] == movie].index[0]

        # 🔥 FIX IS HERE
        distances, indices = knn.kneighbors([vectors[movie_index]], n_neighbors=6)

        return [movies.iloc[i].title for i in indices[0][1:]]

    except Exception as e:
        print("KNN ERROR:", e)  # 👈 add this for debugging
        return ["Movie not found"]