from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=1208)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discount = models.FloatField()