# league/models.py
from django.db import models

class League(models.Model):
    name = models.CharField(max_length=255)  # Name of the league
    division = models.CharField(max_length=50, blank=True, null=True)  # Division within the league
    founded_year = models.IntegerField(blank=True, null=True)  # Year the league was founded
    number_of_teams = models.IntegerField(default=0)  # Total number of teams in the league
    logo = models.ImageField(upload_to='league_logos/', blank=True, null=True)  # League logo
    website = models.URLField(blank=True, null=True)  # Official league website
    country = models.CharField(max_length=100,default="Tanzania")

    def __str__(self):
        return self.name
    

class Seasons(models.Model):
    league = models.ForeignKey('league.League', on_delete=models.CASCADE, related_name='seasons')  # Use string format to avoid circular imports
    name = models.CharField(max_length=20)  # e.g., "2023/2024"
    start_date = models.DateField()
    end_date = models.DateField()
    winner = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, blank=True)  # Use string format for Team reference
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.league.name} - {self.name}"
    

class Referee(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=100,default="Tanzanian")

    def __str__(self):
        return self.name if self.name else "Unnamed Referee"
