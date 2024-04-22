from django.contrib import admin
from .models import Reservation , Room , Point , Comment

# Register your models here.
admin.register(Reservation)
admin.register(Room)
admin.register(Point)
admin.register(Comment)