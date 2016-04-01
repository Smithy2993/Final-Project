# student urls.py

# Import urls and patterns aswell as student views
from django.conf.urls import patterns, url
from student import views

urlpatterns = patterns('',
        url(r'^(?P<username>[a-zA-Z0-9]+)$', views.index, name='index'))
