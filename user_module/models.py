from django.db import models
from sqlite3 import IntegrityError


class CustomUserManager:
    @staticmethod
    def create_user(name, last_name, phone, password, email):
        # Нужна нормальная валидация всего, и пустоты и неправильных символов в имени и фамилии, валидация номера и емейла, и пароля.
        # checking for value
        if not name:
            return False, "No name value."
        if not last_name:
            return False, "No last_name value."
        if not phone:
            return False, "No phone value."
        if not password:
            return False, "No password value."

        # checking the phone for matches in the database
        if is_phone_already_exist(phone):
            return False, "Phone number already exist."
        # checking the email for matches in the database
        if email is not None:
            if is_email_already_exist(email):
                return False, "Email already exist."

        try:
            user = User(name=name, last_name=last_name, phone=phone, password=password, email=email)
            user.save()
            return True, "User created."
        except IntegrityError:
            return False, "Creating user error."


class UserManager(models.Manager):
    pass


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    # optional
    email = models.CharField(max_length=100,
                             blank=True,
                             null=True)
    # аватар
    # предпочтения по жанрам

    manager = CustomUserManager()
    objects = UserManager()

    def str(self):
        return self.name


def is_phone_already_exist(phone):
    return User.objects.filter(phone=phone).exists()


def is_email_already_exist(email):
    return User.objects.filter(email=email).exists()
