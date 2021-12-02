from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar1.jpeg', upload_to='img')



