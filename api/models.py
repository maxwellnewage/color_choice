from django.contrib.auth.models import User
from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=10)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
