from django.shortcuts import render

from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Movie
from .forms import MovieForm


from django.http import JsonResponse
from django.urls import reverse

# View for listing movies with search, sorting, and pagination

class MovieListView(ListView):
    """List movies with search (name/genre/director), sorting and pagination."""
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    paginate_by = 3
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) | Q(genre__icontains=q) | Q(director__icontains=q)
            )
        sort = self.request.GET.get('sort')
        if sort in ('name', '-rating', '-release_date'):
            qs = qs.order_by(sort)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        ctx['sort'] = self.request.GET.get('sort', '')
        return ctx

# View for displaying movie details

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

# View for creating a new movie instance

class MovieCreateView(SuccessMessageMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')
    success_message = "Movie added successfully!"

# View for updating an existing movie instance

class MovieUpdateView(SuccessMessageMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')
    success_message = "Movie updated successfully!"

# View for deleting a movie instance

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete_movie.html'
    success_url = reverse_lazy('movie_list')

# View for searching movies and returning JSON response

def movie_search(request):
    query = request.GET.get('q', '').strip()

    movies = Movie.objects.all()

    if query:
        movies = movies.filter(
            Q(name__icontains=query) |
            Q(genre__icontains=query) |
            Q(director__icontains=query)
        )

    movies = movies.order_by('name')

    results = []

    for movie in movies:
        results.append({
            'name': movie.name,
            'genre': movie.genre,
            'director': movie.director,
            'release_date': str(movie.release_date),
            'detail_url': reverse('movie_detail', args=[movie.pk]),
            'poster_url': movie.poster.url if movie.poster else '',
        })

    return JsonResponse({'movies': results})