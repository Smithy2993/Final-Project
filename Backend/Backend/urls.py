#Backend urls.py

#Import necessary functions including url patterns and the admin function
#Also import settings from settings.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import Backend.views


#Define url patterns for all apps
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^module/', include('module.urls')),
    url(r'^skill/', include('skill.urls')),
    url(r'^extra_curricular/', include('extra_curricular.urls')),
    url(r'^alumni/', include('alumni.urls')),

    
    # user auth urls. For user login authorisation purposes
    url(r'^accounts/login/$', Backend.views.user_login),
    url(r'^accounts/auth/$', Backend.views.auth_view),
    url(r'^accounts/logout/$', Backend.views.logout),
    url(r'^accounts/loggedin/$', Backend.views.loggedin),
    url(r'^accounts/invalid/$', Backend.views.invalid_login),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
