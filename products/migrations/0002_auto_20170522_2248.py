# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
