from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=20, blank=True)
    phoneno = models.IntegerField()
    address = models.TextField(max_length=300)
    pincode = models.IntegerField()
    last_access = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
