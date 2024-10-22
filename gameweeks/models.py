from django.db import models
from teams.models import Team, Player

# Game Week Model
class GameWeek(models.Model):
    season = models.CharField(max_length=9)  # Example: '2023-2024'
    week_number = models.IntegerField()  # Game week number (e.g., 1, 2, 3...)
    start_date = models.DateField()  # Start of the game week
    end_date = models.DateField()  # End of the game week

    def __str__(self):
        return f"Game Week {self.week_number} ({self.season})"

# Fixture Model
class Fixture(models.Model):
    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name='fixtures')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    stadium = models.CharField(max_length=255)
    date = models.DateTimeField()  # Date and time of the fixture
    

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - Game Week {self.gameweek.week_number}"

# Goal Model
class Goal(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='goals')
    scored_by = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals')
    scored_at = models.PositiveIntegerField(help_text="Time in minutes when the goal was scored")
    goals_scored = models.PositiveIntegerField(default=1)  # Number of goals scored

    def __str__(self):
        return f"{self.scored_by.name} scored {self.goals_scored} goal(s) at {self.scored_at}' in {self.match_performance}"

# Shoot Model
class Shoot(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='shoots')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shoots')
    time = models.PositiveIntegerField(help_text="Time in minutes when the shot was taken")
    result = models.CharField(max_length=20, choices=[('on_target', 'On Target'), ('off_target', 'Off Target'), ('blocked', 'Blocked')])

    def __str__(self):
        return f"{self.player.name} shot {self.result} at {self.time}' in {self.match_performance}"

# Pass Model
class Pass(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='passes')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='passes')
    completed = models.BooleanField(default=False)
    time = models.PositiveIntegerField(help_text="Time in minutes when the pass was made")

# Tackle Model
class Tackle(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='tackles')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='tackles')
    successful = models.BooleanField(default=False)
    time = models.PositiveIntegerField(help_text="Time in minutes when the tackle was made")

# Duel Model
class Duel(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='duels')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='duels')
    outcome = models.CharField(max_length=10, choices=[('won', 'Won'), ('lost', 'Lost')])
    time = models.PositiveIntegerField(help_text="Time in minutes when the duel occurred")

# Yellow Card Model
class YellowCard(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='yellow_cards')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='yellow_cards')
    time = models.PositiveIntegerField(help_text="Time in minutes when the yellow card was shown")

# Red Card Model
class RedCard(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='red_cards')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='red_cards')
    time = models.PositiveIntegerField(help_text="Time in minutes when the red card was shown")

# Substitution Model
class Substitution(models.Model):
    match_performance = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='substitutions')
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substituted_out')
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substituted_in')
    time = models.PositiveIntegerField(help_text="Time in minutes when the substitution occurred")

# Match Statistics Model
class MatchStatistics(models.Model):
    fixture = models.OneToOneField(Fixture, on_delete=models.CASCADE)
    home_team_shots = models.PositiveIntegerField(default=0)
    away_team_shots = models.PositiveIntegerField(default=0)
    home_team_possession = models.PositiveIntegerField(default=0)  # percentage
    away_team_possession = models.PositiveIntegerField(default=0)  # percentage
    home_team_corners = models.PositiveIntegerField(default=0)
    away_team_corners = models.PositiveIntegerField(default=0)

    @property
    def home_team_shots_on_target(self):
        return self.fixture.shoots.filter(player__team=self.fixture.home_team, result='on_target').count()

    @property
    def away_team_shots_on_target(self):
        return self.fixture.shoots.filter(player__team=self.fixture.away_team, result='on_target').count()

    def __str__(self):
        return f"Match Statistics for {self.fixture}"
