import random
from typing import Optional, Union

from django.db import models
from django.utils.html import format_html

from .clients import ImageClient, TextClient
from .config import CHARACTERISTICS, CHARACTERS, ENTITIES, STYLES


class Story(models.Model):
    """Story model."""

    type = models.CharField(max_length=255)
    text = models.TextField()
    story = models.TextField(null=True, blank=True)
    style = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.story

    def _random(self, objects) -> Union[str, int, dict]:
        return random.choice(objects)

    def _get_style(self) -> str:
        return self._random(STYLES)

    def _get_entity(self) -> dict:
        return ENTITIES[self._random(list(ENTITIES.keys()))]

    def _get_characteristic(self) -> str:
        return self._random(CHARACTERISTICS)

    def _get_character(self) -> str:
        return self._random(CHARACTERS)

    def _get_characters_count(self, entity) -> Optional[int]:
        return self._random(entity.get('characters'))

    def _get_characteres_text(self, count) -> str:
        if count == 1:
            return (f'{count} charachter which is {self._get_characteristic()}'
                    f' {self._get_character()}')

        text = (f'{count} charachters which are {self._get_characteristic()}'
                f' {self._get_character()}')
        return text + ' '.join(
            [f'and {self._get_characteristic()} {self._get_character()}'
             for _ in range(count - 1)]
        )

    def _get_context(self, entity) -> str:
        return self._random(entity['context'])

    def _generate_text(self, entity) -> str:
        """Generate text to generate story, exmaples:
           short description of fauvism landscape with forest
           short description of fauvism landscape with forest
           short description of mask item
        """
        base_text = 'Generate one sentence of'
        type = entity['type']
        characters = entity.get('characters', None)

        if characters:
            characters_count = self._get_characters_count(entity)
            if characters_count is not None:
                characters_text = self._get_characteres_text(characters_count)

        if type == 'landscape':
            text = (f'{base_text} landscape with {self._get_context(entity)}'
                    + (f' and {characters_text}' if characters_count else ''))
        elif type == 'character':
            text = f'{base_text} {characters_text}'
        elif type == 'item':
            text = (f'{base_text} {self._get_context(entity)} item')

        return text

    def _generate_story(self, text, style) -> str:
        """Generate story based on generated text"""
        client = TextClient()
        story = f'{client.get_text(text)} Style: {style}-dixit style'
        return story

    def save(self, *args, **kwargs) -> None:
        entity = self._get_entity()
        self.type = entity['type']
        self.style = self._get_style()
        self.text = self._generate_text(entity)
        self.story = self._generate_story(self.text, self.style)
        super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Stories"


class Image(models.Model):
    """Image model."""

    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    image = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return self.image

    def display_image(self):
        html = f'<img src="{self.image}" width="300" height="300" />'
        if self.image:
            return format_html(html)
        return 'No image'

    def save(self, *args, **kwargs):
        self.story = Story.objects.create()
        client = ImageClient()
        self.image = client.get_image(self.story.story)
        super(Image, self).save(*args, **kwargs)
