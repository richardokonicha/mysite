from django.db import models


# Create your models here.

class Resturant():
    name = models.CharField(max_length=250)
    label = models.SlugField(unique=True)
    