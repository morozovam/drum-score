from django.urls import path, include
# from django.conf import settings
from rest_framework import routers
from .views import ArtistViewSet, SongViewSet, ScoreViewSet


router = routers.DefaultRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'song', SongViewSet)
router.register(r'score', ScoreViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
