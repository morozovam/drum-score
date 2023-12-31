from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(
        verbose_name="Артист", max_length=50, unique=True
    )

    def __str__(self):
        return self.artist_name

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"


class Song(models.Model):
    song_name = models.CharField(
        verbose_name="Песня", max_length=50, unique=True
    )
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    performer = models.ForeignKey(
        Artist,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="performer_song_set",
    )

    def __str__(self):
        if (self.artist_id == self.performer_id) or (self.performer is None):
            return f"{self.artist} - {self.song_name}"
        else:
            return (
                f"{self.artist} - {self.song_name} (cover by {self.performer})"
            )

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


def score_path(self, filename):
    return f"{self.song.artist}/{self.song.song_name}/{filename}"


class Score(models.Model):
    class ScoreTypes(models.TextChoices):
        GUITARPRO = "GP", _("GuitarPro file")
        PDF = "PDF", _("Adobe Reader file")
        JPG = "JPG", _("JPG picture")

    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    score = models.FileField(upload_to=score_path)
    score_type = models.CharField(
        max_length=3, choices=ScoreTypes.choices, default=ScoreTypes.PDF
    )

    def __str__(self):
        return f"{self.song.artist} - {self.song.song_name}"

    class Meta:
        verbose_name = "Ноты"
        verbose_name_plural = "Ноты"
