from core.models import Image, Story

from .serializers import ImageSerializer, StorySerializer
from .viewsets import RetrieveListViewSet


class StoryViewSet(RetrieveListViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class ImageViewSet(RetrieveListViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
