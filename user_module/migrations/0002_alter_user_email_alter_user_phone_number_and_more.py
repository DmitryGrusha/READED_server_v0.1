# Generated by Django 5.0.1 on 2024-01-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]