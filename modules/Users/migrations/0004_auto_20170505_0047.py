# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20170505_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='biblioteca',
            field=models.ManyToManyField(to='Books.Book'),
        ),
    ]
