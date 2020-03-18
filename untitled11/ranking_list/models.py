from django.db import models

# Create your models here.
class Ranking(models.Model):
    client = models.CharField(max_length=20)  # varchar(20)
    grade = models.IntegerField()  # int

