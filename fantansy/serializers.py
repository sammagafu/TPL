from rest_framework import serializers
from .models import FantasyTeam, Transfer, FantasySeason, CustomLeague, CustomLeagueMembership, StartingEleven, Chip

class StartingElevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartingEleven
        fields = '__all__'  # Adjust as needed

class FantasyTeamSerializer(serializers.ModelSerializer):
    starting_eleven = StartingElevenSerializer(many=True, read_only=True, source='startingeleven_set')  # Assuming you have a reverse relation

    class Meta:
        model = FantasyTeam
        fields = '__all__'  # Include 'starting_eleven' in the response

class CustomLeagueMembershipSerializer(serializers.ModelSerializer):
    fantasy_team = FantasyTeamSerializer(read_only=True)  # Nest fantasy team details

    class Meta:
        model = CustomLeagueMembership
        fields = '__all__'  # Adjust as needed

class CustomLeagueSerializer(serializers.ModelSerializer):
    memberships = CustomLeagueMembershipSerializer(many=True, read_only=True, source='memberships')  # Include all members

    class Meta:
        model = CustomLeague
        fields = '__all__'  # Include 'memberships' in the response

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'  # Adjust as needed

class FantasySeasonSerializer(serializers.ModelSerializer):
    fantasy_teams = FantasyTeamSerializer(many=True, read_only=True, source='fantasyteam_set')

    class Meta:
        model = FantasySeason
        fields = '__all__'  # Include 'fantasy_teams' in the response

class ChipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chip
        fields = '__all__'  # Adjust as needed
