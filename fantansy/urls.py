from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FantasyTeamViewSet,
    TransferViewSet,
    FantasySeasonViewSet,
    CustomLeagueViewSet,
    CustomLeagueMembershipViewSet,
    StartingElevenViewSet,
    ChipViewSet
)

router = DefaultRouter()
router.register(r'fantasy-teams', FantasyTeamViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'fantasy-seasons', FantasySeasonViewSet)
router.register(r'custom-leagues', CustomLeagueViewSet)
router.register(r'custom-league-memberships', CustomLeagueMembershipViewSet)
router.register(r'starting-elevens', StartingElevenViewSet)
router.register(r'chips', ChipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
