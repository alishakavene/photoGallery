from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photo_today,name='photoToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photo,name = 'pastPhoto')
]