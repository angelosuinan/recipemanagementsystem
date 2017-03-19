from __future__ import unicode_literals

from django.db import models
from core.models import Base
# Create your models here.

class Spider(Base):
    name = models.CharField(max_length =50, unique=True)
    def __str__(self):
        return self.name
