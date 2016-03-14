from django.conf.urls import patterns, url
from user import views

urlpatterns = patterns('',
        url(r'^$', views.user, name='user'))
