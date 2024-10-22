# league/views.py
from rest_framework import viewsets
from .models import League, Seasons, Referee
from gameweeks.permissions import IsStaffOrReadOnly
from .serializers import LeagueSerializer, SeasonsSerializer, RefereeSerializer

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsStaffOrReadOnly]

class SeasonsViewSet(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [IsStaffOrReadOnly]

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    permission_classes = [IsStaffOrReadOnly]
