#Alumni urls.py

#Import the django conf utility functions
#Also import the views.py from alumni
from django.conf.urls import patterns, url
from alumni import views

#Url patterns to map templates 
urlpatterns = patterns('',
        #Adding the find alumni page to the server usage
        url(r'^Find_Alumni', views.alumni_search, name='Find_Alumni'),)
