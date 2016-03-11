from django.conf.urls import patterns, url
from extra_curricular import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
