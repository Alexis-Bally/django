from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=5000)
