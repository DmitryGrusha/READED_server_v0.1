# Generated by Django 5.0.1 on 2024-01-21 00:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('storyline', models.TextField()),
                ('chapters_total_count', models.IntegerField()),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('chapters', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
    ]