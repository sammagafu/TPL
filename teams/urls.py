from django.urls import path
from .views import player,squad,team

urlpatterns = [
    path('',team.TeamListCreateView.as_view(),name="team-list"),
    path('<str:slug>/',team.TeamDetailView.as_view(),name="team-detail"),

    path('player/',player.PlayerListCreateView.as_view(),name="player-list"),
    path('player/<str:slug>/',player.PlayerRetrieveUpdateDestroyView.as_view(),name="player-detail"),

    path('squad/',squad.SquadListCreateView.as_view(),name="team-list"),
    path('squad/<str:slug>/',squad.SquadDetailView.as_view(),name="team-detail"),
]