# league/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeagueViewSet, SeasonsViewSet, RefereeViewSet

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'seasons', SeasonsViewSet)
router.register(r'referees', RefereeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
