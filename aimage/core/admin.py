from django.contrib import admin

from .models import Image, Story

admin.site.site_header = 'aimage'


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    search_fields = ('id', 'text', 'story')
    list_display = ('type', 'text', 'story', 'created_at')
    list_filter = ('type',)
    readonly_fields = ('id', 'type', 'text', 'story', 'created_at')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ('story__text',)
    list_display = ('display_image', 'story', 'created_at')
    list_filter = ('story__type',)
    readonly_fields = ('id', 'image', 'story', 'created_at')
