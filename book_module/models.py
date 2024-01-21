from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import serializers


class BookManager(models.Manager):
    pass


class Book(models.Model):
    author = models.TextField()
    title = models.TextField()
    storyline = models.TextField()
    chapters_total_count = models.IntegerField()
    genres = ArrayField(models.IntegerField())
    chapters = ArrayField(models.TextField())

    objects = BookManager()

    def str(self):
        return self.author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
