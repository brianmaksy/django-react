from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.admin import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

# viewset = http methods without using http keywords. e.g. create, retrieve, update, destroy (CRUD)
# this class inherits those methods in ModelViewSet.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer # can just be one serializer, not '(MovieSerializer, )'

    # detail True means one specific movie
    @action(detail=True, methods=['POST']) # mark a viewset method as routable
    # intuition after viewing @action source code: add attribs to the func (method) in question
    # also pass pk (primary key)
    # the route is the func.__name__
    def rate_movie(self, request, pk=None):
        """
            # rate_movie gives rating to one movie.
        :param request:
        :param pk:
        :return:
        """
        # request will be passed into @action and then request.data will have meaning (?)
        # request is def by rest_framework. its request class has decorator, takes in HTTP request and enhances it
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # user = request.user # we're not logged in yet.
            user = User.objects.get(id=1)
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id) # so no need specify user&movie in post request.data
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False) # json
                response = {"message": "rating updated", "result": serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                Rating.objects.create(user=user.id, movie=movie.id, stars=stars) # if stars not an int, will fail
                # given the constraints of the create method
                serializer = RatingSerializer(rating, many=False)
                response = {"message": "rating created", "result": serializer.data}
        else:
            response = {"response": "user needs to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
