from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    thread_name = models.CharField(max_length=255)