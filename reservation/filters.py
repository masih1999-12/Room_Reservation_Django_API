from django_filters.rest_framework import FilterSet

from .models import Room

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'name': ['contains'],
            'is_active': ['exact'],
        }