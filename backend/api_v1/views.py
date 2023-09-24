# from django.shortcuts import render
# import rest_framework.pagination
from rest_framework import viewsets
from .serializers import ArtistSerializer, SongSerializer, ScoreSerializer
from .models import Artist, Song, Score
# Create your views here.
from rest_framework.metadata import SimpleMetadata
import django_filters.rest_framework


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    description = 'Артисты'
    metadata_class = SimpleMetadata
    description = 'Артисты'
    page_size = None


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    description = 'Песни'
    # pagination_class = rest_framework.pagination.PageNumberPagination
    # page_size = 5
    page_size = None


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    description = 'Ноты'
    filterset_fields = ['song', 'score_type']
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    page_size = None
