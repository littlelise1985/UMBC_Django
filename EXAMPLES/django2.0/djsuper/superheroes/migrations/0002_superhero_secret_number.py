# Generated by Django 2.2.3 on 2019-07-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0001_squashed_0003_superhero_favorite_fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='secret_number',
            field=models.IntegerField(default=1),
        ),
    ]
