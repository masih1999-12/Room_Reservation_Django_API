from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets , mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import Team
from .pagination import DefaultPagination
from .filters import TeamFilter
from .serializers import TeamsSerializer


class MyTeamsApiVew(
                    viewsets.GenericViewSet ,
                    mixins.ListModelMixin ,
                    mixins.RetrieveModelMixin ,
                    ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TeamFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name']
    serializer_class = TeamsSerializer
    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(members__id = user.id).order_by('name')
    
class MyTeamsAsLeaderApiVew(
                    viewsets.GenericViewSet ,
                    mixins.ListModelMixin ,
                    mixins.RetrieveModelMixin ,
                    ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TeamFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name']
    serializer_class = TeamsSerializer
    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(leader__id = user.id).order_by('name')