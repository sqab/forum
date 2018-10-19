from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path(r'', include('posts.urls')),
    url(r'^avatar/', include('avatar.urls')),
    path('admin/', admin.site.urls),
]
