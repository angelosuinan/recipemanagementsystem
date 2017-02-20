# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170220_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
