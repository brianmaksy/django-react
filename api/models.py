from django.db import models
from django.contrib.auth.admin import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),) # if in a movie user has already rated, will be rejected
        index_together = (('user', 'movie'),) # create pointers to where data is stored.
        # Rating id in url is determined by user and movie.
