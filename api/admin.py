from django.contrib import admin
from .models import Movie, Rating

# register once model migrations applied
admin.site.register(Movie)
admin.site.register(Rating)