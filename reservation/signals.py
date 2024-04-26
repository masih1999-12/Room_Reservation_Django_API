from django.db.models.signals import reciver , post_save
from django.db.models import Avg
from .models import Comment

@reciver(post_save , sender = Comment)
def RoomPointCaculations(sender,instance,created):
    room = instance.reservation.room
    point = Comment.objects.filter(reservation__room = room).aggregate(Avg('point'))
    room.point = point
    room.save()