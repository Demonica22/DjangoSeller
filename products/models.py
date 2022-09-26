from django.db import models
from PIL import Image


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default="Good One")
    image = models.ImageField(default="no image")
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.brand) + " " + self.name