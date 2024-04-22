from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    profile_image = models.ImageField(null=True , blank=True)
    phone = models.CharField(max_length = 11)


class Team(models.Model):
    name = models.CharField(max_length = 255 , unique = True)
    members = models.ManyToManyField(to=CustomUser)
    leader = models.ForeignKey(to=CustomUser , on_delete = models.PROTECT , related_name = 'leader')