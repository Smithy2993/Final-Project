from django.conf.urls import patterns, url
from skill import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
