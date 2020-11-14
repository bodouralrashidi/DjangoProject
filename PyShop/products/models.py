from django.db import models


class Product(models.Model):  # inherits all comman django application
    name = models.CharField(max_length=257)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=20083)


class Offer (models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


