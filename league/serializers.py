# league/serializers.py
from rest_framework import serializers
from .models import League, Seasons, Referee

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'  # Use '__all__' to include all fields in the serializer

class SeasonsSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()  # Nesting LeagueSerializer for the league field
    winner = serializers.PrimaryKeyRelatedField(queryset='teams.Team.objects.all', required=False)

    class Meta:
        model = Seasons
        fields = '__all__'  # Use '__all__' to include all fields in the serializer

class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'  # Use '__all__' to include all fields in the serializer
