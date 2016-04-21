# extra_curricular urls.py

# Import urls and views
from django.conf.urls import patterns, url
from extra_curricular import views

# url patterns for the extra_curricular app
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^add_extra_curricular/(?P<username>[a-zA-Z0-9]+)$', views.add_extra_curricular, name='add_extra_curricular'),
        url(r'^edit_extra_curricular/(?P<username>[a-zA-Z0-9]+)$', views.edit_extra_curricular, name='edit_extra_curricular'),
        url(r'^delete_extra_curricular/(?P<username>[a-zA-Z0-9]+)$', views.delete_extra_curricular, name='delete_extra_curricular')
]
