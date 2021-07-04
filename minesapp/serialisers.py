from rest_framework import serializers
from .models import SavedGames


class SavedGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedGames
        fields =('id', 'user', 'level', 'mines_array', 'opened_array', 'time')