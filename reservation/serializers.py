from rest_framework import serializers , response , status
from .models import Room

from accounts.models import  CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name' ,'last_name']

# class TeamsSerializer(serializers.ModelSerializer):
#     members = CustomUserSerializer(many = True)
#     leader = CustomUserSerializer()
#     class Meta:
#         model = Team
#         fields = ['id','name' ,'members' ,'leader']
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','capacity']