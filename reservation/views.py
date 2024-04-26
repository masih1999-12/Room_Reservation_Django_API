from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets , mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import Room
from .pagination import DefaultPagination
from .filters import RoomFilter
from .serializers import RoomSerializer

class ShowRoomsApiView(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            mixins.RetrieveModelMixin ,
            ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name' , 'capacity']
    serializer_class = RoomSerializer
    queryset = Room.objects.all()