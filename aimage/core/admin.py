from django.contrib import admin

from .forms import ImageAdminForm
from .models import Image, Story

admin.site.site_header = 'aimage'


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    search_fields = ('id', 'text', 'generated_story')
    list_display = ('type', 'text', 'generated_story', 'created_at')
    list_filter = ('type',)
    readonly_fields = ('id', 'type', 'text', 'generated_story', 'created_at')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm
    search_fields = ('story__text',)
    list_display = ('display_image', 'moderation_like', 'story', 'created_at')
    list_filter = ('story__type',)
    list_per_page = 10
    fieldsets = (
        (None, {
            'fields': ('count', 'moderation_like')
        }),)

    def save_model(self, request, obj, form, change):
        count = form.cleaned_data.get('count')
        for image in range(count):
            image = Image()
            image.save()
