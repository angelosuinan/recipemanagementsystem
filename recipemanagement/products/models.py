from django.db import models
from core.models import Base
import uuid
from decimal import Decimal

class Product(Base):
    name = models.CharField(max_length=1000, unique=True, default=uuid.uuid1)
    price = models.DecimalField(max_digits=1000,decimal_places=2,default=Decimal('0'))
    def __str__(self):
        return self.name

class Recipe(Base):
    name = models.CharField(max_length=2512, unique=True)
    description = models.TextField(blank=True)
    img_url = models.CharField(max_length=1512,)
    prep_time = models.CharField(max_length=115)
    servings = models.CharField(max_length=201)
    direction = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
