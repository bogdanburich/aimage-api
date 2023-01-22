from core.models import Image, Story
from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('id', 'type', 'text', 'generated_story')


class ImageSerializer(serializers.ModelSerializer):

    story = serializers.SlugField(source='story.generated_story')

    class Meta:
        model = Image
        fields = ('id', 'image', 'story', 'created_at')
