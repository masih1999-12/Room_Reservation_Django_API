from django.contrib import admin
from .models import Reservation , Room , Point , Comment

# Register your models here.




@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'date' , 'room' , 'team')
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('point', 'reservation')

admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'reservation')