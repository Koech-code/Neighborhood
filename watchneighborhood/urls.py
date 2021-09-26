from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    url('^$', views.index, name='home'),
    url('all-hoods/', views.neighborhood, name='hood'),
    url('logout/', LogoutView.as_view(), {"next_page":''}),
    url('join/(\d+)', views.join_hood, name='hoodjoin'),
    url('leave/(\d+)', views.leave_hood, name='hoodleave'),
    url('profile/<user>', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

