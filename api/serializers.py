from rest_framework import serializers
from .models import Movie, Rating

# serializer makes objects into datatypes understandable by frontend.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description') # will be json

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')