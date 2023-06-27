from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phonenumber = models.CharField(max_length=32)
