# Generated by Django 5.0.1 on 2024-01-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0002_rename_phone_user_phone_number_user_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country_code',
            field=models.CharField(max_length=3),
        ),
    ]