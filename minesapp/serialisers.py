from django.db.models import fields
from rest_framework import serializers
from .models import SavedGames, PlayedGames


class SavedGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedGames
        fields =('id', 'user', 'level', 'mines_array', 'opened_array', 'time', 'name', 'time_saved')



class PlayedGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedGames
        fields = ('id', 'user', 'time_score', 'level')


