# Generated by Django 4.1.7 on 2023-03-10 11:59

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Артист')),
            ],
            options={
                'verbose_name': 'Артист',
                'verbose_name_plural': 'Артисты',
            },
        ),
    ]
