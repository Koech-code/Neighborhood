from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.index, name='home'),
    url(r'^all-hoods/(\d+)', views.neighborhood, name='hood'),
    url('join/(\d+)', views.join_hood, name='hoodjoin'),
    url('leave/(\d+)', views.leave_hood, name='hoodleave'),
    url('profile/', views.profile, name='profile'),
    url('new-post/(\d+)', views.create_post, name='post'),
    url('business/', views.business, name='business'),
    url('search/', views.business_search, name='search'),
    url('update/', views.update_profile, name='update'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

