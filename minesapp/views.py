from django.shortcuts import render
from rest_framework import generics
from .models import SavedGames
from .serialisers import SavedGamesSerializer



# the api endpoint view for the saving and retrieving saved games
class SavedGamesApi(generics.ListCreateAPIView):
    queryset = SavedGames.objects.all()
    serializer_class = SavedGamesSerializer


class SavedGameRetrieve(generics.RetrieveDestroyAPIView):
    queryset = SavedGames.objects.all()
    serializer_class = SavedGamesSerializer