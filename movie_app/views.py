from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director, Actor

# Create your views here.


def show_all_movie(request):
    movies = Movie.objects.order_by(F('year',).desc(nulls_last=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        str_bool=Value('Hi'),
        int_bool=Value(666),
        ffff=F('rating')*F('year')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Min('year'), Count('id'))
    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movies.html', {
        'movie': movie
    })

def show_directors(request):
    directors = Director.objects.all()
    for director in directors:
        director.save()
    return render(request, 'movie_app/show_directors.html', {
        'directors': directors
    })

def show_director(request, slug_director:str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/show_director.html', {
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/show_actors.html', {
        'actors': actors
    })

def show_one_actor(request, slug_actor:str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/show_one_actor.html', {
        'actor': actor
    })