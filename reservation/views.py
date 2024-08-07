from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import viewsets , mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import Room ,Reservation ,Comment
from .pagination import DefaultPagination
from .filters import RoomFilter ,ReservationFilter ,CommentFilter
from .serializers import RoomSerializer ,ReservationSerializer ,CommentSerializer , RoomReservasionSerializer

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
    ordering_fields = ['room__name' , 'date' , 'start' , 'end']
    serializer_class = ReservationSerializer
    date = timezone.now().date()
    time = timezone.now().time()
    queryset = Reservation.objects.filter(date__lte = date , end__lte = time)
    
class MyCommentsApiView(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            mixins.CreateModelMixin ,
            ):
    
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CommentFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['reservation__room__name' , 'reservation__team__name']
    ordering_fields = ['point' , 'reservation__room__name' , 'reservation__team__name']
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(reservation__team__leader = self.request.user)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

class FreeTimesForGivenRoom(
            viewsets.GenericViewSet ,
            mixins.ListModelMixin ,
            mixins.CreateModelMixin ,
            ):
    pagination_class = DefaultPagination
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_class = ReservationFilter
    # search_fields = ['room__name' , 'team__name']
    # ordering_fields = ['room__name' , 'date' , 'start' , 'end']
    permission_classes = [IsAuthenticated]
    serializer_class = ...