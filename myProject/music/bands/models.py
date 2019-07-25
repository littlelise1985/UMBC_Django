from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    member = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

