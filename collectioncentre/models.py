from django.db import models

# Create your models here.
class CollectionCentre(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=40)
    Id=models.IntegerField()
    

