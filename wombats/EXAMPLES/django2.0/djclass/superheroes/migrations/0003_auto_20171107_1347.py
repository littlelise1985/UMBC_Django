# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_auto_20171102_0712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='superhero',
            options={'ordering': ['secret_identity']},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='power',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
