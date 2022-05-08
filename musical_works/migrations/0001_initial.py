# Generated by Django 4.0.4 on 2022-05-07 07:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('contributors', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=50), size=None)),
                ('iswc', models.CharField(max_length=50)),
            ],
        ),
    ]
