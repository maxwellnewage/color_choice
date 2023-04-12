from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Color(models.Model):
    name = models.CharField(max_length=10)
    hexa = ColorField(max_length=7, default="#FFF")

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} voted to {self.color}"
