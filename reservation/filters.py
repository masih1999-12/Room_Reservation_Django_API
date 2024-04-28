from django_filters.rest_framework import FilterSet

from .models import Room ,Reservation ,Comment

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'name': ['contains'],
            'is_active': ['exact'],
        }
        
class ReservationFilter(FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'room__name': ['contains'],
            'team__name': ['contains'],
            'date':['exact' , 'gte' ,'lte'],
        }
        
class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'reservation__room__name': ['contains'],
            'reservation__date':['exact' ,'gte' ,'lte'],
        }