from django.shortcuts import render
from .utils import recommend_cosine, recommend_knn, movies
# Create your views here.
def index(request):
    movie_list = movies['title'].values

    selected_movie = None
    selected_model = "cosine"  # default
    recommendations = []

    if request.method == "POST":
        selected_movie = request.POST.get('movie')
        selected_model = request.POST.get('model')

        if selected_model == "cosine":
            recommendations = recommend_cosine(selected_movie)
        else:
            recommendations = recommend_knn(selected_movie)

    return render(request, 'recommender/index.html', {
        'movies': movie_list,
        'recommendations': recommendations,
        'selected_movie': selected_movie,
        'selected_model': selected_model
    })
