import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.metadata import SimpleMetadata

from .models import Artist
from .models import Score
from .models import Song
from .serializers import ArtistSerializer
from .serializers import ScoreSerializer
from .serializers import SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    description = "Артисты"
    metadata_class = SimpleMetadata
    page_size = None


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    description = "Песни"
    page_size = None


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    description = "Ноты"
    filterset_fields = ["song", "score_type"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    page_size = None
