from rest_framework import serializers , response , status
from .models import Room ,Reservation

from accounts.models import  CustomUser, Team

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name' ,'last_name']

class TeamsSerializer(serializers.ModelSerializer):
    members = CustomUserSerializer(many = True)
    leader = CustomUserSerializer()
    class Meta:
        model = Team
        fields = ['id','name' ,'members' ,'leader' , 'count_of_members']
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','capacity']
        
class ReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    team = TeamsSerializer()
    class Meta:
        model = Reservation
        fields = ['id','room','team','date','start','end']