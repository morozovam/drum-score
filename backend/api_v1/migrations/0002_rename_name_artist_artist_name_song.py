# Generated by Django 4.1.7 on 2023-03-10 12:16

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artist_name',
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50, unique=True, verbose_name='Песня')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_v1.artist')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
    ]
