from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GameWeekViewSet,
    FixtureViewSet,
    GoalViewSet,
    ShootViewSet,
    PassViewSet,
    TackleViewSet,
    DuelViewSet,
    YellowCardViewSet,
    RedCardViewSet,
    SubstitutionViewSet,
    MatchStatisticsViewSet,
)

router = DefaultRouter()
router.register(r'', GameWeekViewSet)
router.register(r'fixtures', FixtureViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'shoots', ShootViewSet)
router.register(r'passes', PassViewSet)
router.register(r'tackles', TackleViewSet)
router.register(r'duels', DuelViewSet)
router.register(r'yellowcards', YellowCardViewSet)
router.register(r'redcards', RedCardViewSet)
router.register(r'substitutions', SubstitutionViewSet)
router.register(r'matchstatistics', MatchStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
