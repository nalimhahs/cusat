from django.db import models
class User(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=20,blank=True)
    phoneno=models.IntegerField()
    address=models.TextField(max_length=300)
    pincode=models.IntegerField()
    lastaccess=models.DateTimeField(auto_now_add=True)
    
