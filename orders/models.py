from django.db import models
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #must have ondelete
    items = models.TextField() 
    status = models.CharField(max_length=32)
    #id comes from database 