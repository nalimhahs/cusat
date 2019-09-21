from django.db import models

# Create your models here.
class Driver(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=20,blank=True)
    phoneno=models.IntegerField()
    age=models.IntegerField()
    vehiclecarrysize=models.IntegerField()
    dimensions=models.DecimalField()
    licenseno=models.IntegerField()
    vehicleregno=models.IntegerField()
    region=models.CharField(max_length=80)
    totalearnings=models.DecimalField()

    
