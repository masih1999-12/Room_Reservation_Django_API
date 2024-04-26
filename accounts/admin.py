from django.contrib import admin
from .models import Team , CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_members', 'leader')
    def get_members(self, obj):
        return obj.members()
        