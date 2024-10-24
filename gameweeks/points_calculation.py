# fantasy_app/points_calculation.py
from django.db.models import Sum
from .models import Goal, Assist, YellowCard, RedCard, Tackle, Save, PlayerPoints

def calculate_fantasy_points(player_id, gameweek_id):
    points = 0

    # Fetch goals scored
    goals = Goal.objects.filter(
        scored_by__id=player_id,
        match_performance__gameweek__id=gameweek_id
    ).aggregate(total_goals=Sum('goals_scored'))['total_goals'] or 0
    points += goals * 4  # 4 points per goal

    # Fetch assists made
    assists = Assist.objects.filter(
        player__id=player_id,
        match_performance__gameweek__id=gameweek_id
    ).count()
    points += assists * 3  # 3 points per assist

    # Fetch yellow cards
    yellow_cards = YellowCard.objects.filter(
        player__id=player_id,
        match_performance__gameweek__id=gameweek_id
    ).count()
    points -= yellow_cards  # -1 point per yellow card

    # Fetch red cards
    red_cards = RedCard.objects.filter(
        player__id=player_id,
        match_performance__gameweek__id=gameweek_id
    ).count()
    points -= red_cards * 3  # -3 points per red card

    # Fetch tackles won
    successful_tackles = Tackle.objects.filter(
        player__id=player_id,
        match_performance__gameweek__id=gameweek_id,
        successful=True
    ).count()
    points += successful_tackles  # 1 point per successful tackle

    # Fetch saves made
    saves = Save.objects.filter(
        player__id=player_id,
        match_performance__gameweek__id=gameweek_id
    ).aggregate(total_saves=Sum('number_of_saves'))['total_saves'] or 0
    points += saves  # 1 point per save

    return points

def update_player_points(gameweek_id):
    from .models import Player, PlayerPoints, Fixture

    players = Player.objects.all()

    for player in players:
        # Calculate points for the player in the current game week
        points = calculate_fantasy_points(player.id, gameweek_id)

        # Update or create the PlayerPoints record
        PlayerPoints.objects.update_or_create(
            player=player,
            gameweek_id=gameweek_id,
            defaults={'total_points': points}
        )
