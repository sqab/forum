from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from . import forms

from forum import settings

urlpatterns = [
                  url(r'^$', views.feed, name='feed'),
                  url(r'^post/(?P<pk>\d+)/$', views.details, name='details'),
                  url(r'^posts_by_user/(?P<pk>\d+)/$', views.posts_by_user, name='posts_by_user'),
                  url(r'^post/new/$', views.new_post, name='new_post'),
                  url(r'/(?P<pk>\d+)/like/', views.like, name='like'),

                  # url(r'^signup/$', forms.RegisterFormView.as_view()),
                  url(r'^accounts/', include('django.contrib.auth.urls')),

                  url(r'^profile/', views.profile, name='profile'),
                  url(r'^avatar/', include('avatar.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
