from rest_framework import serializers

from .models import Artist
from .models import Score
from .models import Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
        depth = 1


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"
        depth = 2
