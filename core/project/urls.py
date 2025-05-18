from django.contrib import admin
from django.urls import path, include
from core.project.settings import base
from django.conf.urls.static import static
from core.api.main import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.apps.main.urls")),
    path("", api.urls),
]

if base.DEBUG:
    urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
