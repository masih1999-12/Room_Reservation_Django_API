from rest_framework import serializers , response , status
from .models import Team ,CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name' ,'last_name']

class TeamsSerializer(serializers.ModelSerializer):
    members = CustomUserSerializer(many = True)
    leader = CustomUserSerializer()
    class Meta:
        model = Team
        fields = ['id','name' ,'members' ,'leader' , 'count_of_members' ]