from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
    ]

    name = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    director = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    poster = models.ImageField(upload_to='movie_posters/',blank=True,null=True)

    def __str__(self):
        return self.name