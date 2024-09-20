from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT, STATIC_ROOT, MEDIA_URL, STATIC_URL

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls')),
              ] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
