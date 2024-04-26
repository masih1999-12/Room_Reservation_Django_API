from django_filters.rest_framework import FilterSet

from .models import Room ,Reservation

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
            'date':['exact'],
            'date':['gte'],
            'date':['lte'],
        }