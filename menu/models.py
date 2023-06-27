from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)