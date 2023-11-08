from django.db import models

# Create your models here.
class Persone(models.Model):
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    