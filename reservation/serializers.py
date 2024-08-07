from rest_framework import serializers , response , status
from django.utils import timezone
from .models import Room ,Reservation ,Comment

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
        
class CommentSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer()
    class Meta:
        model = Comment
        fields = ['id','text','point','reservation']
    def get_fields(self):
        fields = super().get_fields()
        if self.context.get('request') and (self.context['request'].method == 'POST'):
            fields['reservation'] = serializers.PrimaryKeyRelatedField(Reservation)
        return fields
    def create(self, validated_data):
        user = self.context['user']
        reservation = validated_data['reservation']
        
        if reservation.team.leader != user:
            raise serializers.ValidationError('You not team leader for this reservation!')
        
        date = timezone.now().date()
        time = timezone.now().time()
        
        if reservation.date <= date and reservation.end <= time:
            raise serializers.ValidationError('Reservation not finished!')
        
        if validated_data['point'] > 5 or validated_data['reservation'] < 0:
            raise serializers.ValidationError('Unvalid point!')
        
        return validated_data
        
class RoomReservasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','capacity']