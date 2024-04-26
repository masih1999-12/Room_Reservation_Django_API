from typing import Collection, Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    profile_image = models.ImageField(null=True , blank=True)
    phone = models.CharField(max_length = 11)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class Team(models.Model):
    name = models.CharField(max_length = 255 , unique = True)
    members = models.ManyToManyField(to=CustomUser)
    leader = models.ForeignKey(to=CustomUser , on_delete = models.PROTECT , related_name = 'leader')
    def __str__(self) -> str:
        return self.name