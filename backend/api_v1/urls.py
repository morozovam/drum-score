from rest_framework import routers

from django.urls import include
from django.urls import path

from .views import ArtistViewSet
from .views import ScoreViewSet
from .views import SongViewSet

router = routers.DefaultRouter()
router.register(r"artist", ArtistViewSet)
router.register(r"song", SongViewSet)
router.register(r"score", ScoreViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]
