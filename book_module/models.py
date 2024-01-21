from django.contrib.postgres.fields import ArrayField
from django.db import models
from sqlite3 import IntegrityError


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



def create_book(author: str, title: str, storyline: str, chapters_total_count: int, genres: [int], chapters: [str]) -> (bool, Book):
    try:
        book = Book(author=author,
                    title=title,
                    storyline=storyline,
                    chapters_total_count=chapters_total_count,
                    genres=genres,
                    chapters=chapters)
        book.save()
        return True, book
    except IntegrityError:
        return False, None