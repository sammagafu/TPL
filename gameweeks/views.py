from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    GameWeek, Fixture, Goal, Shoot, Pass, Tackle, Duel, 
    YellowCard, RedCard, Substitution, MatchStatistics
)
from .serializers import (
    GameWeekSerializer, FixtureSerializer, GoalSerializer, 
    ShootSerializer, PassSerializer, TackleSerializer, 
    DuelSerializer, YellowCardSerializer, RedCardSerializer, 
    SubstitutionSerializer, MatchStatisticsSerializer
)
from .permissions import IsStaffOrReadOnly

# GameWeek ViewSet
class GameWeekViewSet(viewsets.ModelViewSet):
    queryset = GameWeek.objects.all()
    serializer_class = GameWeekSerializer
    permission_classes = [IsStaffOrReadOnly]  # Use custom permission

# Fixture ViewSet
class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = [IsStaffOrReadOnly]

# Goal ViewSet
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsStaffOrReadOnly]

# Shoot ViewSet
class ShootViewSet(viewsets.ModelViewSet):
    queryset = Shoot.objects.all()
    serializer_class = ShootSerializer
    permission_classes = [IsStaffOrReadOnly]

# Pass ViewSet
class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    permission_classes = [IsStaffOrReadOnly]

# Tackle ViewSet
class TackleViewSet(viewsets.ModelViewSet):
    queryset = Tackle.objects.all()
    serializer_class = TackleSerializer
    permission_classes = [IsStaffOrReadOnly]

# Duel ViewSet
class DuelViewSet(viewsets.ModelViewSet):
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer
    permission_classes = [IsStaffOrReadOnly]

# YellowCard ViewSet
class YellowCardViewSet(viewsets.ModelViewSet):
    queryset = YellowCard.objects.all()
    serializer_class = YellowCardSerializer
    permission_classes = [IsStaffOrReadOnly]

# RedCard ViewSet
class RedCardViewSet(viewsets.ModelViewSet):
    queryset = RedCard.objects.all()
    serializer_class = RedCardSerializer
    permission_classes = [IsStaffOrReadOnly]

# Substitution ViewSet
class SubstitutionViewSet(viewsets.ModelViewSet):
    queryset = Substitution.objects.all()
    serializer_class = SubstitutionSerializer
    permission_classes = [IsStaffOrReadOnly]

# MatchStatistics ViewSet
class MatchStatisticsViewSet(viewsets.ModelViewSet):
    queryset = MatchStatistics.objects.all()
    serializer_class = MatchStatisticsSerializer
    permission_classes = [IsStaffOrReadOnly]
