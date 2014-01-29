from django.db import models

# Create your models here.


class Message(models.Model):
    author = models.TextField()
    text = models.TextField()
