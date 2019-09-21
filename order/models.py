from django.db import models
from user.models import CustomUser


class Order(models.Model):
    user_details = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="User")
    assigned_driver = models.ForeignKey(CustomUser, limit_choices_to={'user_type': CustomUser.DRIVER}, on_delete=models.PROTECT, related_name="Driver")
    status = models.CharField(max_length=30)
    weight = models.IntegerField()
    date_of_order = models.DateField()
