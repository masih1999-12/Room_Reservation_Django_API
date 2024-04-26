from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import viewsets , mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import Room ,Reservation
from .pagination import DefaultPagination
from .filters import RoomFilter ,ReservationFilter
from .serializers import RoomSerializer ,ReservationSerializer

class ShowRoomsApiView(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name' , 'capacity']
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class ShowFinishedReservationsApiView(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReservationFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['room__name' , 'team__name']
    ordering_fields = ['room__name' , 'date']
    serializer_class = ReservationSerializer
    date = timezone.now().date()
    time = timezone.now().time()
    queryset = Reservation.objects.filter(date__gte = date , end__gt = time)
    
class ShowReservationsApiView(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            ):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReservationFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['room__name' , 'team__name']
    ordering_fields = ['room__name' , 'date']
    serializer_class = ReservationSerializer
    date = timezone.now().date()
    time = timezone.now().time()
    queryset = Reservation.objects.filter(date__lte = date , start__lt = time)