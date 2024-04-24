from django.contrib import admin
from django.urls import path, include, re_path

from .yasg import urlpatterns as doc_urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls