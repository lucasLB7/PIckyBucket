from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import datetime
from . import views

urlpatterns = [
    url(r'^$', views.home_main, name='home'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.images_by_date,name = 'DatedProjects'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.images,name='image')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)