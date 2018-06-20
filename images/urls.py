from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import datetime

from . import views

urlpatterns = [
    url(r'^$', views.homePageElements, name='home'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.images_by_date,name = 'DatedProjects'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^image/(?P<image_id>\d+)',views.image,name='image'),
    url(r'^new/article$', views.new_article, name='new-article'),
    url(r'profile', views.profile_page, name='profile'),
    url(r'updateProfile', views.updateProfile, name='change'),
    url(r'^view/profiles', views.view_profiles, name='viewProfiles'),
    url(r'^follow/(\d+)',views.follow ,name='follow'), 
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)