from rest_framework import serializers

from core.models import Image, Story


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('id', 'type', 'text', 'story')


class ImageSerializer(serializers.ModelSerializer):

    story = serializers.SlugField(source='story.text')

    class Meta:
        model = Image
        fields = ('id', 'image', 'story', 'created_at')
