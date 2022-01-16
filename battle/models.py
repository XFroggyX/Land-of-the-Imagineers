from django.db import models
from django.contrib.auth.models import User


class Battle(models.Model):
    attackingID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attackingID_article_set")
    defendingID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="defendingID_article_set")
    result = models.ForeignKey(User, on_delete=models.CASCADE, related_name="result_article_set")
    msgAttacking = models.PositiveSmallIntegerField()
    msgDefending = models.PositiveSmallIntegerField()
