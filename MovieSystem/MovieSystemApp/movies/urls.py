from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    movie_search,
)

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/add/", MovieCreateView.as_view(), name="movie_add"),
    path("movie/<int:pk>/edit/", MovieUpdateView.as_view(), name="movie_edit"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
    path("movie-search/", movie_search, name="movie_search"),
]