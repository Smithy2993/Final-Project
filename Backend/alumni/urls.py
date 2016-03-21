from django.conf.urls import patterns, url
from alumni import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^Find_Alumni', views.Find_Alumni, name='Find_Alumni'),)
