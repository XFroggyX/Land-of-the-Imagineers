from django.db import models


class Users(models.Model):
    email = models.EmailField(null=False, blank=False)
    nickname = models.CharField(max_length=255, verbose_name=u"Nickname", null=False, blank=False)
    password = models.CharField(max_length=25, verbose_name=u"Password", null=False, blank=False)
