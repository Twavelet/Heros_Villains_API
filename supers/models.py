from tkinter import CASCADE
from django.db import models
from super_types.models import SuperType

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=100)
    secondary_ability = models.CharField(max_length=100)
    catch_phrase = models.CharField(max_length=300)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)