from django.db import models
from shop.models import *

# Create your models here.

class CartList(models.Model):
    cart_id =models.CharField(max_length=250,unique=True)
    added_date = models.DateTimeField(auto_now_add=True)

class CartItems(models.Model):
    prodt = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quan = models.IntegerField()
    active = models.BooleanField(default=True)

    def total(self):
        return self.prodt.price*self.quan

