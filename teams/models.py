from django.db import models
from django.utils.text import slugify
from league.models import League


class Team(models.Model):
    name = models.CharField(max_length=255)  # Team name
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_name = models.CharField(max_length=10, blank=True, null=True)  # Team abbreviation
    stadium_name = models.CharField(max_length=255, blank=True, null=True)  # Home stadium
    location = models.CharField(max_length=255, blank=True, null=True)  # City or location
    logo = models.ImageField(upload_to='teams/logos/', blank=True, null=True)  # Team logo
    founded_year = models.IntegerField(blank=True, null=True)  # Year team was founded
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')  # League association
    manager = models.CharField(max_length=255, blank=True, null=True)  # Current manager/coach
    colors = models.CharField(max_length=100, blank=True, null=True)  # Team colors
    championships_won = models.IntegerField(default=0)  # Number of championships won
    website = models.URLField(blank=True, null=True)  # Team website
    social_media_links = models.JSONField(blank=True, null=True)  # JSON for social media links
    external_team_id = models.CharField(max_length=100, blank=True, null=True)  # External API team ID
    active = models.BooleanField(default=True)  # Whether the team is currently active

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)  # Position on the field (e.g., Defender, Midfielder)
    nationality = models.CharField(max_length=100, blank=True, null=True)  # Player's nationality
    birthdate = models.DateField(blank=True, null=True)  # Player's birthdate
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    profile_image = models.ImageField(upload_to='teams/players/', blank=True, null=True)  # Player photo
    external_player_id = models.CharField(max_length=100, blank=True, null=True)  # External API player ID

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
