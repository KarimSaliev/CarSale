from django.db import models
from django.contrib.auth.models import User

class UserBio(models.Model):
    bio = models.TextField(blank=True, null=True, max_length=1000)
    birthday = models.DateField(null=True)
    country = models.CharField(blank=True, null=True, max_length=20)
    number = models.CharField(blank=True, null=True, max_length=100)
    user = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)