from django.db import models
from django.contrib.auth import get_user_model
from teams.models import Player
from gameweeks.models import GameWeek
from league.models import League
import uuid

User = get_user_model()

class FantasyTeam(models.Model):
    """Fantasy teams managed by users."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fantasy_teams')
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player, related_name='fantasy_teams', blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)  # Budget for transfers
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def calculate_total_points(self):
        """Calculate total points based on players' performances."""
        self.total_points = self.point_earnings.aggregate(models.Sum('points_earned'))['points_earned__sum'] or 0
        self.save()

    def has_space_for_transfer(self):
        """Ensure there are exactly 16 players in the team."""
        return self.players.count() < 16

    def can_afford_transfer(self, player_value):
        """Check if the team has enough budget for the transfer."""
        return self.budget >= player_value

class Transfer(models.Model):
    """Handle player transfers."""
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, related_name='transfers')
    player_out = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='transfers_out')
    player_in = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='transfers_in')
    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name='transfers')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    points_deduction = models.IntegerField(default=0)
    transfer_date = models.DateTimeField(auto_now_add=True)

    def perform_transfer(self):
        """Perform the transfer and adjust the fantasy team's budget and points."""
        if self.fantasy_team.can_afford_transfer(self.player_in.value):
            if self.fantasy_team.has_space_for_transfer():
                # Remove player_out and add player_in
                self.fantasy_team.players.remove(self.player_out)
                self.fantasy_team.players.add(self.player_in)
                # Adjust budget
                self.fantasy_team.budget -= self.player_in.value
                self.fantasy_team.budget += self.player_out.value
                # Deduct points for additional transfers
                if self.points_deduction > 0:
                    self.fantasy_team.total_points -= self.points_deduction
                self.fantasy_team.save()
                return True
        return False

class FantasySeason(models.Model):
    """Represents each season for a league."""
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='seasons')
    name = models.CharField(max_length=20)  # e.g., "2024/2025"
    start_date = models.DateField()
    end_date = models.DateField()
    winner = models.ForeignKey(FantasyTeam, on_delete=models.SET_NULL, null=True, blank=True)
    is_current = models.BooleanField(default=False)

class CustomLeague(models.Model):
    """Custom leagues that fantasy managers can create."""
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_leagues')
    season = models.ForeignKey(FantasySeason, on_delete=models.CASCADE, related_name='custom_leagues')
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique code for joining
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.season.name} ({'Private' if self.is_private else 'Public'})"

class CustomLeagueMembership(models.Model):
    """Represents membership in a custom league."""
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, related_name='league_memberships')
    custom_league = models.ForeignKey(CustomLeague, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fantasy_team.name} in {self.custom_league.name}"

class StartingEleven(models.Model):
    """Tracks the starting eleven for a FantasyTeam in a specific GameWeek."""
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, related_name='starting_eleven')
    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name='starting_elevens')
    players = models.ManyToManyField(Player, related_name='starting_elevens')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Starting Eleven for {self.fantasy_team.name} - GW {self.gameweek.number}"

class Chip(models.Model):
    """Fantasy chips that managers can use during the season."""
    CHIP_CHOICES = [
        ('triple_captain', 'Triple Captain'),
        ('free_hit', 'Free Hit'),
        ('wildcard', 'Wildcard')
    ]
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, related_name='chips')
    type = models.CharField(max_length=20, choices=CHIP_CHOICES)
    used = models.BooleanField(default=False)
    gameweek_used = models.ForeignKey(GameWeek, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.fantasy_team.name}"

    def can_use_chip(self, current_gameweek):
        """Check if the chip can be used based on usage rules."""
        if self.used:
            return False
        if self.type == 'wildcard':
            # Allow wildcard only once before and once after January
            january_cutoff = 20  # Assuming January transfer window closes after GW 20
            if self.gameweek_used is None:
                return True  # First wildcard
            elif self.gameweek_used.gameweek.number >= january_cutoff and self.fantasy_team.chips.filter(type='wildcard', used=True).count() < 2:
                return True  # Second wildcard after January
            else:
                return False
        else:
            return True  # For other chips, can use once

    def use_chip(self, gameweek):
        """Use the chip for the given gameweek."""
        if self.can_use_chip(gameweek):
            self.used = True
            self.gameweek_used = gameweek
            self.save()
            return True
        return False
