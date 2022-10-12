from django.contrib import admin

from .forms import ImageAdminForm
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
    form = ImageAdminForm
    search_fields = ('story__text',)
    list_display = ('display_image', 'story', 'created_at')
    list_filter = ('story__type',)
    fieldsets = (
        (None, {
            'fields': ('count',)
        }),)

    def save_model(self, request, obj, form, change):
        count = form.cleaned_data.get('count')
        for image in range(count):
            image = Image()
            image.save()
