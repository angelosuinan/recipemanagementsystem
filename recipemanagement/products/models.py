from django.db import models
from core.models import Base


class Recipe(Base):
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True)
    img_url = models.CharField(max_length=512, unique=True)
    def __str__(self):
        return self.name
