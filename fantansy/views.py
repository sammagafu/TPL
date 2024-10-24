from rest_framework import viewsets
from .models import FantasyTeam, Transfer, FantasySeason, CustomLeague, CustomLeagueMembership, StartingEleven, Chip
from .serializers import (
    FantasyTeamSerializer,
    TransferSerializer,
    FantasySeasonSerializer,
    CustomLeagueSerializer,
    CustomLeagueMembershipSerializer,
    StartingElevenSerializer,
    ChipSerializer
)

class FantasyTeamViewSet(viewsets.ModelViewSet):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer

class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

class FantasySeasonViewSet(viewsets.ModelViewSet):
    queryset = FantasySeason.objects.all()
    serializer_class = FantasySeasonSerializer

class CustomLeagueViewSet(viewsets.ModelViewSet):
    queryset = CustomLeague.objects.all()
    serializer_class = CustomLeagueSerializer

class CustomLeagueMembershipViewSet(viewsets.ModelViewSet):
    queryset = CustomLeagueMembership.objects.all()
    serializer_class = CustomLeagueMembershipSerializer

class StartingElevenViewSet(viewsets.ModelViewSet):
    queryset = StartingEleven.objects.all()
    serializer_class = StartingElevenSerializer

class ChipViewSet(viewsets.ModelViewSet):
    queryset = Chip.objects.all()
    serializer_class = ChipSerializer
