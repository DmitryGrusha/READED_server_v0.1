from django.db import models

class UserManager(models.Manager):
    pass


class User(models.Model):
    username = models.CharField(max_length=40, unique=True)
    country_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    # optional
    name = models.CharField(max_length=30,
                            blank=True,
                            null=True)
    last_name = models.CharField(max_length=30,
                                 blank=True,
                                 null=True)
    email = models.CharField(max_length=100,
                             blank=True,
                             null=True,
                             unique=True)
    # аватар
    # предпочтения по жанрам

    objects = UserManager()

    def str(self):
        return self.name
