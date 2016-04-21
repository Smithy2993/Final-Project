# skill urls.py

# Import urls and patterns aswell as the skill views
from django.conf.urls import patterns, url
from skill import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^add_skill/(?P<username>[a-zA-Z0-9]+)$', views.add_skill, name='add_skill'),
        url(r'^edit_skill/(?P<username>[a-zA-Z0-9]+)$', views.edit_skill, name='edit_skill'),
        url(r'^delete_skill/(?P<username>[a-zA-Z0-9]+)$', views.delete_skill, name='delete_skill'),
]
