from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    url('^$', views.index, name='home'),
    url('logout/', LogoutView.as_view(), {"next_page":''}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

