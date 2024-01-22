from django.contrib.postgres.fields import ArrayField
from django.db import models


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
