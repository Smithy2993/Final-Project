#Alumni urls.py

#Import the django conf utility functions
#Also import the views.py from alumni
from django.conf.urls import patterns, url
from alumni import views

#Url patterns to map templates 
urlpatterns = [
        #Adding the find alumni page to the server usage
        url(r'^Find_Alumni/(?P<username>[a-zA-Z0-9]+)$', views.show_alumni, name='show_alumni'),
        url(r'^search/', views.search_alumni, name='search'),
]
