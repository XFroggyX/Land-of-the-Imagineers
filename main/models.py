from django.db import models
from django.contrib.auth.models import User

from towns.models import Town


class UsersOfTown(models.Model):
    UsersID = models.ForeignKey(User, on_delete=models.CASCADE)
    TownsID = models.ForeignKey(Town, on_delete=models.CASCADE)
