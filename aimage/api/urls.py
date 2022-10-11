from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ImageViewSet, StoryViewSet

router = SimpleRouter()

router.register('stories', StoryViewSet)
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
