from django.db import models
from user.models import User
from driver.models import Driver
class Order(models.Model):
    user_details=models.ForeignKey(User)
    assigned_driver=models.ForeignKey(Driver)
    status=models.CharField(max_length=30)
    weight=models.IntegerField()
    date_of_order=models.DateField()



