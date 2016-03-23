# extra_curricular urls.py

# Import urls and views
from django.conf.urls import patterns, url
from extra_curricular import views

# url patterns for the extra_curricular app
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_extra_curricular/$', views.add_extra_curricular, name='add_extra_curricular'),)
