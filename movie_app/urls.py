from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.show_all_movie),
    path('directors', views.show_directors, name='show_directors'),
    path('directors/<slug:slug_director>', views.show_director, name='show_director'),
    path('actors', views.show_all_actors, name='show_actors'),
    path('actors/<slug:slug_actor>', views.show_one_actor, name='show_ane_actor'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('__debug__/', include('debug_toolbar.urls'))

]