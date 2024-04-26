from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import MyTeamsApiVew ,MyTeamsAsLeaderApiVew

router = DefaultRouter()

router.register('my_teams' , MyTeamsApiVew ,  basename='my_teams')
router.register('my_teams_as_leader' , MyTeamsAsLeaderApiVew ,  basename='my_teams_as_leader')

urlpatterns = [
    path('', include(router.urls)),
]