from django.db import models
from core.models import Base

from decimal import Decimal

class Product(Base):
    product = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=1000,decimal_places=2,default=Decimal('0'))
    def __str__(self):
        return self.product

class Recipe(Base):
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True)
    img_url = models.CharField(max_length=512,)
    prep_time = models.DecimalField(max_digits=2,decimal_places=0,default=Decimal('0'))
    servings = models.DecimalField(max_digits=2,decimal_places=0,default=Decimal('0'))
    direction = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
