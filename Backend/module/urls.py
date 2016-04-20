# module urls.py

# Import the urls and patterns aswell as the views for module
from django.conf.urls import patterns, url
from module import views

urlpatterns = [
        url(r'^$', views.index, name='index')
        ]
