from django.db import models
from django.contrib.auth.models import User


class UsersOfTown(models.Model):
    UsersID = models.ForeignKey(User, on_delete=models.CASCADE)
    TownsID = models.ForeignKey('towns.Town', on_delete=models.CASCADE)
