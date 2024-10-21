# teams/serializers.py
from rest_framework import serializers
from .models import Player, Team, Squad

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class SquadSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Squad
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    squads = SquadSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
