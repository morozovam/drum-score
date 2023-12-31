# Generated by Django 4.1.7 on 2023-03-11 21:16

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_alter_score_options_score_score_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='performer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='performer_song_set', to='api_v1.artist'),
        ),
    ]
