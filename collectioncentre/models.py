from django.db import models

# Create your models here.
class Collectioncentre(models.Model):
    name=models.CharField(max_lenght=20)
    location=models.CharField(max_length=40)
    Id=models.IntegerField()
    

