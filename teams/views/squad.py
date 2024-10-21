from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from teams.models import Squad
from teams.serializers import SquadSerializer

class SquadListCreateView(generics.ListCreateAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SquadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    permission_classes = [IsAuthenticated]