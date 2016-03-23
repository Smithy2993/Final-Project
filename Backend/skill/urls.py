# skill urls.py

# Import urls and patterns aswell as the skill views
from django.conf.urls import patterns, url
from skill import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
