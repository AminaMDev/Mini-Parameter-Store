from django.urls import re_path, path, include
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', include('api.urls')),
]
