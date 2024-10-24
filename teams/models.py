# teams/models.py
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=255)  # Team name
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_name = models.CharField(max_length=10, blank=True, null=True)  # Team abbreviation
    stadium_name = models.CharField(max_length=255, blank=True, null=True)  # Home stadium
    location = models.CharField(max_length=255, blank=True, null=True)  # City or location
    logo = models.ImageField(upload_to='teams/logos/', blank=True, null=True)  # Team logo
    founded_year = models.IntegerField(blank=True, null=True)  # Year team was founded
    league = models.ForeignKey('league.League', on_delete=models.CASCADE, related_name='teams')  # Use string format
    colors = models.CharField(max_length=100, blank=True, null=True)  # Team colors
    website = models.URLField(blank=True, null=True)  # Team website
    social_media_links = models.JSONField(blank=True, null=True)  # JSON for social media links
    active = models.BooleanField(default=True)  # Whether the team is currently active

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Player(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(max_length=50, choices=[
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ])
    date_of_birth = models.DateField(default=timezone.now)
    nationality = models.CharField(max_length=100,default="Tanzanian")
    height = models.DecimalField(max_digits=5, decimal_places=2,default=160.00)  # Height in cm
    weight = models.DecimalField(max_digits=5, decimal_places=2,default=80.00)  # Weight in kg

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Squad(models.Model):
    season = models.CharField(max_length=9)  # Example: '2023-2024'
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='squads')
    players = models.ManyToManyField(Player, related_name='squads')  # Squad players for the season

    def __str__(self):
        return f"{self.team.name} Squad {self.season}" 
