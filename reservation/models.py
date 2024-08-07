from django.db import models
from accounts.models import Team
from django.core.validators import MaxValueValidator , MinValueValidator
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length = 255 , unique = True)
    capacity = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    point = models.DecimalField(
        default = 0 ,
        max_digits = 3 ,
        decimal_places = 2 ,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )

class Reservation(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField()
    room = models.ForeignKey(to = Room , on_delete = models.PROTECT)
    team = models.ForeignKey(to = Team , on_delete = models.PROTECT)
    def clean(self):
        super().clean()
        if self.start >= self.end:
            raise ValidationError("End time must be after start time.")

class Comment(models.Model):
    text = models.TextField()
    point = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    reservation = models.ForeignKey(to = Reservation , on_delete = models.CASCADE)