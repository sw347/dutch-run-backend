from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['username', 'score', 'ghost_data']
    
class GameRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['username', 'score']