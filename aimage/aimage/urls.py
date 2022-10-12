from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

BASE_API_URL = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_API_URL, include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
