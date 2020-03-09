from django.db import models
from django.utils import timezone


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=250)
    label = models.SlugField(unique=True)

    def __str__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages',
        on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.message
        