from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns=[
    url(r'^$',views.todays_photo,name='photoToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)