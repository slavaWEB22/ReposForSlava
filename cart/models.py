from django.db import models
from products.models import Products
from accounts.models import Person
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    prod = models.ForeignKey(Products,on_delete=models.DB_CASCADE)
    user = models.ForeignKey(User,on_delete=models.DB_CASCADE)
    count = models.PositiveIntegerField(default=0)