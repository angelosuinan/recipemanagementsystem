from __future__ import unicode_literals

from django.db import models
from decimal import Decimal
# Create your models here.
from core.models import Base

class Account(Base):
    name = models.CharField(max_length=500, unique=True,)
    price = models.DecimalField(max_digits=1000,decimal_places=2,default=Decimal('0'))
    order = models.CharField(max_length=4000,)
    f_name = models.CharField(max_length=500,)
    l_name = models. CharField(max_length=500,)
    s_address= models.TextField(blank=True,)
    def __str__(self):
        return self.name
