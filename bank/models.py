from django.db import models
from django.contrib.auth.models import User


class Banks(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar1.jpeg', upload_to='img')
    branch = models.TextField(unique=True, null=True)
    IFSC = models.TextField(unique=True, null=True)


class Service(models.Model):
    service_name = models.TextField(unique=True, null=True)
    max_customers = models.IntegerField(null=True)
    time_slot_from = models.TimeField(null=True)
    time_slot_to = models.TextField(null=True)
