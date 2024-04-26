from django_filters.rest_framework import FilterSet

from .models import Team

class TeamFilter(FilterSet):
    class Meta:
        model = Team
        fields = {
            'name': ['contains'],
        }