from rest_framework import serializers
from .models import GameWeek, Fixture, Shoot, Pass, Tackle, Duel, Goal, YellowCard, RedCard, Substitution, MatchStatistics

# Serializer for Shoot
class ShootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoot
        fields = ['player', 'time', 'result']

# Serializer for Pass
class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['player', 'completed', 'time']

# Serializer for Tackle
class TackleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tackle
        fields = ['player', 'successful', 'time']

# Serializer for Duel
class DuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duel
        fields = ['player', 'outcome', 'time']

# Serializer for Goal
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['scored_by', 'scored_at', 'goals_scored']

# Serializer for Yellow Card
class YellowCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = YellowCard
        fields = ['player', 'time']

# Serializer for Red Card
class RedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedCard
        fields = ['player', 'time']

# Serializer for Substitution
class SubstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substitution
        fields = ['player_out', 'player_in', 'time']

# Serializer for MatchStatistics
class MatchStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchStatistics
        fields = ['home_team_shots', 'away_team_shots', 'home_team_possession', 'away_team_possession', 
                  'home_team_corners', 'away_team_corners']

# Serializer for Fixture
class FixtureSerializer(serializers.ModelSerializer):
    shoots = ShootSerializer(many=True, read_only=True)
    passes = PassSerializer(many=True, read_only=True)
    tackles = TackleSerializer(many=True, read_only=True)
    duels = DuelSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    yellow_cards = YellowCardSerializer(many=True, read_only=True)
    red_cards = RedCardSerializer(many=True, read_only=True)
    substitutions = SubstitutionSerializer(many=True, read_only=True)
    match_statistics = MatchStatisticsSerializer(read_only=True)

    class Meta:
        model = Fixture
        fields = ['id', 'gameweek', 'home_team', 'away_team', 'stadium', 'date',
                  'shoots', 'passes', 'tackles', 'duels', 'goals', 
                  'yellow_cards', 'red_cards', 'substitutions', 'match_statistics']

# Serializer for GameWeek
class GameWeekSerializer(serializers.ModelSerializer):
    fixtures = FixtureSerializer(many=True, read_only=True)

    class Meta:
        model = GameWeek
        fields = ['season', 'week_number', 'start_date', 'end_date', 'fixtures']
